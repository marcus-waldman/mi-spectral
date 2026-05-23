# 00-setup.R
#
# Shared simulation primitives for the W1/W2/W3 witnesses.
# Companion to todo/004-simulation-hypotheses.md (preregistered at SHA ddc9037).
#
# Every primitive below is documented by which §0.6 entry it implements.
# Unit tests live in 00-test-primitives.R; pilot/cross-witness checks in
# 00-pilot-checks.R. Production W1/W2/W3 runs depend on these.

suppressPackageStartupMessages({
  library(norm)
  library(mvtnorm)
  library(lavaan)
})


# -----------------------------------------------------------------------------
# Parameter vectorization helpers
#
# Theta is represented internally as a list(mu = numeric(p), Sigma = matrix(p,p)).
# For RIV pooling, we vectorize to a flat parameter vector of length
# p + p*(p+1)/2 via vech() on Sigma.
# -----------------------------------------------------------------------------

vech <- function(M) {
  # Half-vectorization: lower triangle (including diagonal) of M, column-major.
  return(M[lower.tri(M, diag = TRUE)])
}

invvech <- function(v, p) {
  # Inverse of vech: rebuild symmetric matrix from lower-triangular vector.
  M <- matrix(0, p, p)
  M[lower.tri(M, diag = TRUE)] <- v
  M <- M + t(M) - diag(diag(M))
  return(M)
}

theta_to_vec <- function(theta) {
  return(c(theta$mu, vech(theta$Sigma)))
}

vec_to_theta <- function(v, p) {
  mu <- v[seq_len(p)]
  Sigma <- invvech(v[(p + 1):length(v)], p)
  return(list(mu = mu, Sigma = Sigma))
}


# -----------------------------------------------------------------------------
# §0.6 primitive: gen_data(N, mu, Sigma)
#
# Draws N i.i.d. observations from MVN(mu, Sigma). Returns the complete-data
# matrix X (N x p).
# -----------------------------------------------------------------------------

gen_data <- function(N, mu, Sigma) {
  p <- length(mu)
  stopifnot(nrow(Sigma) == p, ncol(Sigma) == p, isSymmetric(Sigma))
  X <- mvtnorm::rmvnorm(n = N, mean = mu, sigma = Sigma)
  return(X)
}


# -----------------------------------------------------------------------------
# §0.6 primitive: apply_mar(X)
#
# Implements the §0.2 MAR mechanism:
#   R_1 | X_3 ~ Bernoulli(Phi(a1 + b1 * X_3))
#   R_2 | X_4 ~ Bernoulli(Phi(a2 + b2 * X_4))
#   R_3 = R_4 = 0 (fully observed)
# Default coefficients (a, b) = (-0.5, 0.4) reproduce the preregistered formula
# in §0.2 (marginal missingness ~32% per variable, not 40% — see comment).
# Returns list(Y = matrix with NAs, R = 0/1 mask).
#
# Note on the "~40% missing" comment in §0.2: with a = -0.5, b = 0.4 and
# X_3 ~ N(0,1), Pr(R_1 = 1) = Phi(-0.5 / sqrt(1 + 0.4^2)) ~ 0.32. To actually
# hit 40% marginal, set a = -0.273. The preregistered binding formula is the
# (-0.5, 0.4) version; if implementation reveals this matters, an amendment
# to §0.2 with reasoning is required (see Sign-off rules).
# -----------------------------------------------------------------------------

apply_mar <- function(X, a1 = -0.5, b1 = 0.4, a2 = -0.5, b2 = 0.4) {
  N <- nrow(X)
  p <- ncol(X)
  stopifnot(p == 4)
  pi1 <- pnorm(a1 + b1 * X[, 3])
  pi2 <- pnorm(a2 + b2 * X[, 4])
  R <- matrix(0, N, p)
  R[, 1] <- as.numeric(runif(N) < pi1)
  R[, 2] <- as.numeric(runif(N) < pi2)
  Y <- X
  Y[R == 1] <- NA
  return(list(Y = Y, R = R))
}


# -----------------------------------------------------------------------------
# §0.6 primitive: em_mvn(Y)
#
# Observed-data MLE under MVN. Wraps norm::em.norm. Returns
# list(mu, Sigma) and the internal 'param' representation for use with da.norm.
# -----------------------------------------------------------------------------

em_mvn <- function(Y, maxits = 1000, criterion = 1e-6) {
  s <- norm::prelim.norm(Y)
  thetahat_flat <- norm::em.norm(s, showits = FALSE, maxits = maxits,
                                 criterion = criterion)
  pars <- norm::getparam.norm(s, thetahat_flat, corr = FALSE)
  return(list(mu = pars$mu, Sigma = pars$sigma,
              s = s, theta_flat = thetahat_flat))
}


# -----------------------------------------------------------------------------
# §0.6 primitive: impute_mvn(Y, M, burnin, thin)
#
# Joint MVN proper imputation via data augmentation (Schafer 1997 Alg 5.2)
# under Jeffreys prior, as implemented in norm::da.norm. Returns a list of
# M completed datasets (each a matrix of the same shape as Y, with no NAs).
#
# Pipeline: prelim -> em (init point) -> burn-in chain -> thinned draws,
# imputing the missing values from each draw of theta.
# -----------------------------------------------------------------------------

impute_mvn <- function(Y, M, burnin = 200, thin = 100, em_fit = NULL) {
  if (is.null(em_fit)) {
    em_fit <- em_mvn(Y)
  }
  s <- em_fit$s
  theta_state <- em_fit$theta_flat
  # Burn-in.
  theta_state <- norm::da.norm(s, theta_state, steps = burnin, showits = FALSE)
  imputed <- vector("list", M)
  for (m in seq_len(M)) {
    theta_state <- norm::da.norm(s, theta_state, steps = thin, showits = FALSE)
    imputed[[m]] <- norm::imp.norm(s, theta_state, Y)
  }
  return(imputed)
}


# -----------------------------------------------------------------------------
# Alternate §0.6 primitive: impute_mvn_amelia(Y, M)
#
# Amelia II (Honaker, King, Blackwell) — EMB-based joint MVN imputation. For
# each imputation: (i) bootstrap-resample the rows, (ii) run EM on the
# bootstrap to convergence, (iii) draw missing values from the implied
# conditional distribution.
#
# This is a parallel proper-MI engine to norm::da.norm. Switching between
# them isolates "engine-specific behavior" vs "theory-level finding" when
# the W1 prediction fails. Both target the same posterior in the asymptotic
# limit; finite-sample differences inform engine diagnostics.
# -----------------------------------------------------------------------------

impute_mvn_amelia <- function(Y, M, ...) {
  # Amelia warns / errors if too many rows are missing OR if the data is
  # singular under bootstrap. Suppress non-essential output via p2s=0.
  df <- as.data.frame(Y)
  colnames(df) <- sprintf("V%d", seq_len(ncol(df)))
  a_out <- Amelia::amelia(df, m = M, p2s = 0, ...)
  imputed <- lapply(a_out$imputations, function(d) { return(as.matrix(d)) })
  return(imputed)
}


# -----------------------------------------------------------------------------
# Analytic FIML-marginalized Q-function
#
# Computes bar_Q_inf(theta_eval) under the FIML "imputation" where tilde_phi
# = theta_obs deterministically for every observation. The integral
# E_{Y^mis|Y^obs, theta_obs}[ell_com(theta_eval; Y^obs, Y^mis)] has closed
# form because the inner expectation is a quadratic form in Y^mis under
# Gaussianity.
#
# Per observation i with observed positions O_i and missing positions M_i,
# under theta_obs the conditional is X_i^{M_i} | X_i^{O_i} ~ N(m_i, V_i):
#   m_i = mu^{M_i}_obs + Sigma^{M_i,O_i}_obs (Sigma^{O_i,O_i}_obs)^{-1}
#         (Y_i^{O_i} - mu^{O_i}_obs)
#   V_i = Sigma^{M_i,M_i}_obs
#         - Sigma^{M_i,O_i}_obs (Sigma^{O_i,O_i}_obs)^{-1} Sigma^{O_i,M_i}_obs
# Building hat_X_i with observed entries Y_i^{O_i} and missing entries m_i,
# and Vbar_i a p x p matrix with V_i in the (M_i, M_i) block:
#   E[log phi(X_i; theta_eval)] = log phi(hat_X_i; theta_eval)
#                               - 0.5 tr(Sigma_eval^{-1} Vbar_i)
#
# Sums over i. Output is the analytic bar_Q_inf at theta_eval under FIML
# imputation parameter theta_obs.
#
# Connection to v4.5 line 218: with tilde_phi = theta_obs deterministically,
# Cov(Delta_tilde_phi, theta_obs) = 0 trivially (because Delta_tilde_phi=0),
# so Term 1 = tr(I_{mis|obs} Var(theta_obs)) = tr(RIV) — same prediction
# as MI but computed without Monte Carlo over imputations.
# -----------------------------------------------------------------------------

barQ_fiml_analytic <- function(theta_eval, theta_obs, Y, R) {
  N <- nrow(Y)
  p <- ncol(Y)
  Sigma_eval_inv <- solve(theta_eval$Sigma)
  logdet_Sigma_eval <- as.numeric(determinant(theta_eval$Sigma, logarithm = TRUE)$modulus)
  half_log2pi <- 0.5 * log(2 * pi)
  total <- 0
  # Group observations by missingness pattern for efficiency.
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat)
    R_pat <- R[rows[1], ]
    Mi <- which(R_pat == 1)
    Oi <- which(R_pat == 0)
    Y_pat <- Y[rows, , drop = FALSE]
    n_pat <- length(rows)
    if (length(Mi) == 0) {
      # Fully observed: no integration needed.
      lp <- mvtnorm::dmvnorm(Y_pat, mean = theta_eval$mu,
                             sigma = theta_eval$Sigma, log = TRUE)
      total <- total + sum(lp)
    } else if (length(Oi) == 0) {
      # All missing: hat_X_i = mu_obs, V_i = Sigma_obs (whole matrix).
      diff <- theta_obs$mu - theta_eval$mu
      quad <- as.numeric(t(diff) %*% Sigma_eval_inv %*% diff)
      tr_term <- sum(diag(Sigma_eval_inv %*% theta_obs$Sigma))
      per_obs <- -p * half_log2pi - 0.5 * logdet_Sigma_eval - 0.5 * quad - 0.5 * tr_term
      total <- total + n_pat * per_obs
    } else {
      # Partial. Conditional under theta_obs.
      Sigma_OO <- theta_obs$Sigma[Oi, Oi, drop = FALSE]
      Sigma_MO <- theta_obs$Sigma[Mi, Oi, drop = FALSE]
      Sigma_MM <- theta_obs$Sigma[Mi, Mi, drop = FALSE]
      Sigma_OO_inv <- solve(Sigma_OO)
      reg <- Sigma_MO %*% Sigma_OO_inv  # |M| x |O|
      cond_V <- Sigma_MM - reg %*% t(Sigma_MO)
      # Trace term: tr(Sigma_eval^{-1} Vbar_i) with Vbar_i zero outside (M,M).
      tr_term <- sum(diag(Sigma_eval_inv[Mi, Mi, drop = FALSE] %*% cond_V))
      # Loop over observations in this pattern (each has its own cond mean).
      for (i in rows) {
        cond_m <- theta_obs$mu[Mi] +
          as.numeric(reg %*% (Y[i, Oi] - theta_obs$mu[Oi]))
        X_hat <- numeric(p)
        X_hat[Oi] <- Y[i, Oi]
        X_hat[Mi] <- cond_m
        diff <- X_hat - theta_eval$mu
        quad <- as.numeric(t(diff) %*% Sigma_eval_inv %*% diff)
        total <- total + (-p * half_log2pi - 0.5 * logdet_Sigma_eval -
                          0.5 * quad - 0.5 * tr_term)
      }
    }
  }
  return(total)
}


# -----------------------------------------------------------------------------
# Observed-data log-likelihood for MVN with arbitrary missingness pattern
#
# ell_obs(theta; Y, R) = sum_i log p(Y_i^{O_i}; mu^{O_i}, Sigma^{O_i,O_i})
# under MVN. Used for computing I_obs via numerical Hessian.
# -----------------------------------------------------------------------------

loglik_obs_mvn <- function(theta, Y, R) {
  N <- nrow(Y)
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  total <- 0
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat)
    R_pat <- R[rows[1], ]
    Oi <- which(R_pat == 0)
    if (length(Oi) == 0) { next }
    Y_pat <- Y[rows, Oi, drop = FALSE]
    mu_O <- theta$mu[Oi]
    Sigma_OO <- theta$Sigma[Oi, Oi, drop = FALSE]
    lp <- mvtnorm::dmvnorm(Y_pat, mean = mu_O, sigma = Sigma_OO, log = TRUE)
    total <- total + sum(lp)
  }
  return(total)
}


# -----------------------------------------------------------------------------
# Complete-data MVN Fisher information (closed form)
#
# Block diagonal on theta = (mu, vech(Sigma)):
#   I_mu(theta)        = N * Sigma^{-1}
#   I_vechSigma(theta) = (N/2) * D_p' (Sigma^{-1} (x) Sigma^{-1}) D_p
# Cross-block zero.
# -----------------------------------------------------------------------------

fisher_info_com_mvn <- function(theta, N) {
  p <- length(theta$mu)
  Sigma_inv <- solve(theta$Sigma)
  Dp <- duplication_matrix(p)
  K <- kronecker(Sigma_inv, Sigma_inv)
  I_mu <- N * Sigma_inv
  I_sig <- (N / 2) * t(Dp) %*% K %*% Dp
  k <- p + p * (p + 1) / 2
  I_com <- matrix(0, k, k)
  I_com[seq_len(p), seq_len(p)] <- I_mu
  I_com[(p + 1):k, (p + 1):k] <- I_sig
  return(I_com)
}


# -----------------------------------------------------------------------------
# Observed-data Fisher information (closed-form, pattern-mixed MVN)
#
# Per observation i with observed positions O_i (size q_i):
#   I_mu block contribution        : Sigma_{O,O}^{-1} embedded at rows/cols
#                                    (O_i, O_i) of the p x p mu block.
#   I_vechSigma block contribution : (1/2) D_q^T (Sigma_OO^{-1} (x) Sigma_OO^{-1}) D_q
#                                    embedded at the full-vech indices that
#                                    correspond to entries with both indices
#                                    observed.
# Cross-block contribution: 0 (MVN block-diagonal info).
#
# Summed over patterns weighted by N_P (count of observations in pattern P).
# This is the expected Fisher info per the pattern-mixture decomposition; under
# MAR-ignorable it equals the asymptotic variance inverse of theta_obs.
#
# Replaces numDeriv-based fisher_info_obs_mvn() — same I_obs to numerical
# precision, ~1000x faster. Verified by the smoke test in 00-test-primitives.R.
# -----------------------------------------------------------------------------

vech_index_table <- function(p) {
  # vech_idx[i, j] = position of M[i, j] in vech(M) (column-major lower tri).
  # Symmetric: vech_idx[j, i] = vech_idx[i, j].
  vech_idx <- matrix(0, p, p)
  count <- 0
  for (j in seq_len(p)) {
    for (i in j:p) {
      count <- count + 1
      vech_idx[i, j] <- count
      vech_idx[j, i] <- count
    }
  }
  return(vech_idx)
}

fisher_info_obs_mvn <- function(theta_obs, Y, R) {
  p <- length(theta_obs$mu)
  k <- p + p * (p + 1) / 2
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  vech_idx <- vech_index_table(p)
  I_obs_total <- matrix(0, k, k)
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat)
    n_pat <- length(rows)
    R_pat <- R[rows[1], ]
    Oi <- which(R_pat == 0)
    q <- length(Oi)
    if (q == 0) { next }
    Sigma_OO <- theta_obs$Sigma[Oi, Oi, drop = FALSE]
    Sigma_OO_inv <- solve(Sigma_OO)
    # mu block
    I_obs_total[Oi, Oi] <- I_obs_total[Oi, Oi] + n_pat * Sigma_OO_inv
    # vech(Sigma) block
    Dq <- duplication_matrix(q)
    I_subvech <- 0.5 * t(Dq) %*% kronecker(Sigma_OO_inv, Sigma_OO_inv) %*% Dq
    # Map sub-vech indices to full-vech indices (offset by p for the mu block).
    sub_count <- 0
    full_idx <- numeric(q * (q + 1) / 2)
    for (b in seq_len(q)) {
      for (a in b:q) {
        sub_count <- sub_count + 1
        full_idx[sub_count] <- p + vech_idx[Oi[a], Oi[b]]
      }
    }
    I_obs_total[full_idx, full_idx] <-
      I_obs_total[full_idx, full_idx] + n_pat * I_subvech
  }
  return(I_obs_total)
}


# -----------------------------------------------------------------------------
# Analytic tr(RIV) at the observed-data MLE
#
# tr(RIV) = tr(I_{mis|obs} I_obs^{-1})
#         = tr((I_com - I_obs) I_obs^{-1})
#         = tr(I_com I_obs^{-1}) - k
# where k is the parameter dimension.
# -----------------------------------------------------------------------------

tr_riv_analytic <- function(theta_obs, Y, R) {
  N <- nrow(Y)
  p <- ncol(Y)
  I_com <- fisher_info_com_mvn(theta_obs, N)
  I_obs <- fisher_info_obs_mvn(theta_obs, Y, R)
  k <- nrow(I_com)
  tr_total <- sum(diag(solve(I_obs, I_com))) - k
  return(list(tr_RIV = tr_total, I_com = I_com, I_obs = I_obs))
}


# -----------------------------------------------------------------------------
# Analytic tr(RIV) for the sigma_{12} = 0 constrained MVN model
#
# Under the constraint, the free parameter vector is the 13-dim subset of the
# full 14-dim vector that excludes the entry for sigma_{2,1}. Fisher info on
# the constrained model = the 13x13 principal submatrix of the unconstrained
# 14x14 info at the constrained MLE (standard sub-model Fisher info).
# -----------------------------------------------------------------------------

constrained_param_indices_sigma12_zero <- function() {
  # vech-of-Sigma ordering (column-major lower triangle, prefixed by p mu
  # entries): sigma_{2,1} is the 6th of the 14 total parameters (4 mu +
  # vech position 2 = 4 + 2). Free params under sigma_{12} = 0:
  return(c(1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14))
}

tr_riv_analytic_constrained_sigma12 <- function(theta_cn_obs, Y, R) {
  N <- nrow(Y)
  idx <- constrained_param_indices_sigma12_zero()
  I_com_full <- fisher_info_com_mvn(theta_cn_obs, N)
  I_obs_full <- fisher_info_obs_mvn(theta_cn_obs, Y, R)
  I_com_cn <- I_com_full[idx, idx]
  I_obs_cn <- I_obs_full[idx, idx]
  k_cn <- length(idx)
  tr_total <- sum(diag(solve(I_obs_cn, I_com_cn))) - k_cn
  return(tr_total)
}


# -----------------------------------------------------------------------------
# §0.6 primitive: loglik_mvn(theta, X)
#
# Sum of MVN log-densities of rows of X under MVN(theta$mu, theta$Sigma).
# Used to evaluate (i) ell_com on the complete data, (ii) per-imputation
# log-likelihood for the Q-function average bar L_M.
# -----------------------------------------------------------------------------

loglik_mvn <- function(theta, X) {
  return(sum(mvtnorm::dmvnorm(X, mean = theta$mu, sigma = theta$Sigma,
                              log = TRUE)))
}


# -----------------------------------------------------------------------------
# §0.6 primitive: lrt_complete(theta_full, theta_null, X)
#
# Complete-data LRT statistic: 2 * (ell_full - ell_null).
# -----------------------------------------------------------------------------

lrt_complete <- function(theta_full, theta_null, X) {
  return(2 * (loglik_mvn(theta_full, X) - loglik_mvn(theta_null, X)))
}


# -----------------------------------------------------------------------------
# Complete-data MVN MLE (closed form)
#
# Helper used by W1 step 2 ("compute hat_theta_com"). Uses the MLE divisor (N),
# not the unbiased divisor (N-1), so that it actually maximizes ell_com.
# -----------------------------------------------------------------------------

mle_complete_mvn <- function(X) {
  N <- nrow(X)
  mu_hat <- colMeans(X)
  X_centered <- sweep(X, 2, mu_hat, FUN = "-")
  Sigma_hat <- crossprod(X_centered) / N
  return(list(mu = mu_hat, Sigma = Sigma_hat))
}


# -----------------------------------------------------------------------------
# Per-imputation MLE + analytic covariance for the FULL MVN model
#
# For Rubin pooling we need (theta_hat_m, U_m) per imputation. U_m is the
# parameter covariance matrix evaluated at theta_hat_m; for the unstructured
# MVN model with complete-data divisor N, this has closed form:
#
#   Var(mu_hat)        = Sigma / N
#   Var(vech Sigma_hat) = (2/N) * D_p^+ (Sigma ⊗ Sigma) D_p^{+T}
#
# where D_p^+ = (D_p' D_p)^{-1} D_p' is the Moore-Penrose pseudo-inverse of
# the duplication matrix. Cross-block covariance is zero asymptotically.
# -----------------------------------------------------------------------------

duplication_matrix <- function(p) {
  # Builds D_p such that D_p %*% vech(A) = vec(A) for symmetric A.
  k <- p * (p + 1) / 2
  D <- matrix(0, p * p, k)
  count <- 0
  for (j in seq_len(p)) {
    for (i in j:p) {
      count <- count + 1
      D[(j - 1) * p + i, count] <- 1
      if (i != j) {
        D[(i - 1) * p + j, count] <- 1
      }
    }
  }
  return(D)
}

dup_pinv <- function(p) {
  Dp <- duplication_matrix(p)
  return(solve(crossprod(Dp), t(Dp)))
}

mle_with_cov_mvn <- function(X) {
  N <- nrow(X)
  p <- ncol(X)
  theta_hat <- mle_complete_mvn(X)
  Dpinv <- dup_pinv(p)
  # Asymptotic covariance of vech(Sigma_hat) under MVN MLE.
  K <- kronecker(theta_hat$Sigma, theta_hat$Sigma)
  V_sigma <- (2 / N) * Dpinv %*% K %*% t(Dpinv)
  V_mu <- theta_hat$Sigma / N
  k_sigma <- p * (p + 1) / 2
  U <- matrix(0, p + k_sigma, p + k_sigma)
  U[seq_len(p), seq_len(p)] <- V_mu
  U[(p + 1):(p + k_sigma), (p + 1):(p + k_sigma)] <- V_sigma
  return(list(theta = theta_hat, U = U))
}


# -----------------------------------------------------------------------------
# §0.6 primitive: riv_sample(theta_imps, U_imps)
#
# Rubin (1987) sample-based RIV. Returns the full RIV matrix and its trace.
#
# Inputs:
#   theta_imps: list of M parameter vectors (each a flat numeric vector of
#               length p + p(p+1)/2, i.e. theta_to_vec output).
#   U_imps    : list of M parameter covariance matrices (each square of
#               matching dimension).
#
# Computes:
#   thetabar = mean across m of theta_m
#   W        = mean across m of U_m         (within-imputation variance)
#   B        = sample cov of {theta_m}      (between-imputation variance)
#   RIV      = (1 + 1/M) * solve(W) %*% B
# -----------------------------------------------------------------------------

riv_sample <- function(theta_imps, U_imps) {
  M <- length(theta_imps)
  stopifnot(length(U_imps) == M, M >= 2)
  k <- length(theta_imps[[1]])
  theta_mat <- do.call(rbind, theta_imps)
  thetabar <- colMeans(theta_mat)
  W <- Reduce("+", U_imps) / M
  centered <- sweep(theta_mat, 2, thetabar, FUN = "-")
  B <- crossprod(centered) / (M - 1)
  RIV <- (1 + 1 / M) * solve(W, B)
  return(list(thetabar = thetabar, W = W, B = B, RIV = RIV,
              tr_RIV = sum(diag(RIV))))
}


# -----------------------------------------------------------------------------
# §0.6 primitive: riv_population(mu, Sigma, n_seeds, N_huge)
#
# DEFERRED to a later iteration. Per §1.3 fallback step 1, we cross-check
# analytical RIV against the sample-based estimator averaged over replicates;
# if W1 succeeds with sample-based as the reference, the analytical version
# is bonus precision. If W1 fails this is where we start digging.
#
# Stub returns NULL with a message. To call it currently produces a clear
# error rather than wrong numbers.
# -----------------------------------------------------------------------------

riv_population <- function(mu, Sigma, n_seeds = NA, N_huge = NA, ...) {
  stop("riv_population() not yet implemented. Use riv_sample averaged across ",
       "replicates (Phase B) as the empirical reference; see todo/004 §1.3 ",
       "fallback step 1.")
}


# -----------------------------------------------------------------------------
# Bundle: theta_to_vec / vec_to_theta convenience for the MI block
# -----------------------------------------------------------------------------

mi_fit_mvn <- function(imputed_list) {
  # Given M completed datasets, returns the list of (theta_m, U_m) tuples
  # using the closed-form MVN MLE on each completion.
  fits <- lapply(imputed_list, mle_with_cov_mvn)
  theta_imps <- lapply(fits, function(f) { return(theta_to_vec(f$theta)) })
  U_imps <- lapply(fits, function(f) { return(f$U) })
  return(list(theta_imps = theta_imps, U_imps = U_imps,
              theta_list = lapply(fits, function(f) { return(f$theta) })))
}


# -----------------------------------------------------------------------------
# Constrained MVN MLE under sigma_{12} = 0
#
# Cholesky parameterization: Sigma = L %*% t(L) with L lower triangular and
# positive diagonal. sigma_{12} = L[1,1] * L[2,1]; setting L[2,1] = 0 forces
# the constraint while leaving the rest of Sigma free. 9 free entries in L
# (instead of 10) plus 4 in mu = 13 parameters total.
#
# Optimization uses log-diagonals (unconstrained parameterization for L_ii > 0)
# and stats::optim with BFGS. The starting point is the unconstrained MLE
# projected to sigma_{12} = 0 (zero out that entry, take Cholesky); the
# objective is the negative complete-data log-likelihood.
#
# Returns list(mu, Sigma, converged, value).
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Lavaan-based MVN fitting for the W2 constrained / observed-data cases
#
# The unconstrained complete-data MLE has closed form (mle_complete_mvn); for
# constrained MLEs or observed-data FIML under missingness we delegate to
# lavaan. Empirical comparison vs a hand-rolled Cholesky optimizer showed
# lavaan FIML is ~38x faster on N=2000 (0.15s vs 5.7s) and gives bit-
# identical estimates.
#
# Model strings:
#   un : unrestricted 4-dim MVN (saturated).
#   cn : same with sigma_{1,2} = 0.
#
# Returns list(mu, Sigma, logLik, npar).
# -----------------------------------------------------------------------------

LAVAAN_MOD_UN <- "
  X1 ~~ X1 + X2 + X3 + X4
  X2 ~~ X2 + X3 + X4
  X3 ~~ X3 + X4
  X4 ~~ X4
  X1 + X2 + X3 + X4 ~ 1
"
LAVAAN_MOD_CN_SIGMA12 <- "
  X1 ~~ X1 + 0*X2 + X3 + X4
  X2 ~~ X2 + X3 + X4
  X3 ~~ X3 + X4
  X4 ~~ X4
  X1 + X2 + X3 + X4 ~ 1
"

lavaan_to_theta <- function(fit) {
  mu_named <- lavaan::fitted(fit)$mean
  Sigma_named <- lavaan::fitted(fit)$cov
  ll <- as.numeric(lavaan::fitMeasures(fit, "logl"))
  return(list(mu = as.numeric(mu_named),
              Sigma = unname(Sigma_named),
              logLik = ll,
              npar = length(lavaan::coef(fit))))
}

# Fit unrestricted or constrained MVN on complete data (no missing values).
lavaan_fit_mvn <- function(X, constrained = FALSE) {
  df <- as.data.frame(X)
  colnames(df) <- sprintf("X%d", seq_len(ncol(df)))
  mod <- if (constrained) { LAVAAN_MOD_CN_SIGMA12 } else { LAVAAN_MOD_UN }
  fit <- lavaan::sem(mod, data = df)
  return(lavaan_to_theta(fit))
}

# Fit on observed data with FIML (handles missing values).
lavaan_fit_mvn_fiml <- function(Y, constrained = FALSE) {
  df <- as.data.frame(Y)
  colnames(df) <- sprintf("X%d", seq_len(ncol(df)))
  mod <- if (constrained) { LAVAAN_MOD_CN_SIGMA12 } else { LAVAAN_MOD_UN }
  fit <- lavaan::sem(mod, data = df, missing = "fiml")
  return(lavaan_to_theta(fit))
}

# Generic versions that accept any lavaan model string (used by W3).
lavaan_fit_mvn_model <- function(X, mod) {
  df <- as.data.frame(X)
  colnames(df) <- sprintf("X%d", seq_len(ncol(df)))
  fit <- lavaan::sem(mod, data = df)
  return(lavaan_to_theta(fit))
}

lavaan_fit_mvn_fiml_model <- function(Y, mod) {
  df <- as.data.frame(Y)
  colnames(df) <- sprintf("X%d", seq_len(ncol(df)))
  fit <- lavaan::sem(mod, data = df, missing = "fiml")
  return(lavaan_to_theta(fit))
}


# -----------------------------------------------------------------------------
# Chan (2022, Ann. Stat.) SMI test (k = 1, Jackknife selection rule).
#
# Per the preregistration §0.3 Amendment 1 the imputation engine is Amelia.
# This function implements Algorithm 2.1 of Chan (2022) for the k = 1 case
# (one tested parameter), using the Jackknife selection rule (eq 3.9).
#
# Inputs:
#   imps           : list of M completed datasets (matrices, all same shape).
#   test_device    : function(X) -> scalar test statistic d_L(X). For our
#                    LRT case, test_device is `lrt_sigma12_device` below.
#   bias_correction: scalar to subtract from d^{1:m} before forming D_hat
#                    (our paper's bias-correction differential). Default 0.
#   N_mc           : number of MC draws for the reference distribution.
#
# Outputs (named list):
#   D_hat   : test statistic in (2.3).
#   r_hat   : OMI estimate (scalar, since k=1).
#   p_value : Chan's MC p-value referring D_hat to D_hat distribution (5.1).
#   d_1_to_m, d_singles, d_leave_outs, T_ell : diagnostics.
#
# Implementation notes:
#   d^{1:m}   = d(X^{1:m}) / m, where X^{1:m} is the row-stacked m datasets.
#   d^{-ell}  = d(X^{-ell}) / (m-1), leave-one-out stacked.
#   d^{ell}   = d(X^ell), single-imputation.
#   T_ell     = (m-1) d^{-ell} + d^{ell} - m d^{1:m}   (Jackknife SMI).
#   r_hat     = mean_{ell} T_ell           (k=1 case: t_hat_1 = r_hat).
#   D_hat     = (d^{1:m} - bias_correction) / (1 + (1+1/m) r_hat).
#   D_hat_MC  = (1+(1+1/m) r_hat) G / (1 + (1+1/m) r_hat H),
#               G ~ chi^2_1, H ~ chi^2_{m-1}/(m-1) independent.
#
# References:
#   Chan, K. W. (2022) "General and Feasible Tests with Multiply-Imputed
#   Datasets." Annals of Statistics 50(2). Algorithm 2.1, eq (2.3), (3.9),
#   (4.5), (5.1).
# -----------------------------------------------------------------------------

chan_smi_test_k1 <- function(imps, test_device, bias_correction = 0,
                             N_mc = 10000) {
  m <- length(imps)
  stopifnot(m >= 2)
  # Per-imputation test statistics.
  d_singles <- vapply(imps, test_device, numeric(1))
  # Stacked-all (X^{1:m}).
  X_all <- do.call(rbind, imps)
  d_1_to_m <- test_device(X_all) / m
  # Leave-one-out stacked statistics.
  d_leave_outs <- numeric(m)
  for (ell in seq_len(m)) {
    X_minus_ell <- do.call(rbind, imps[-ell])
    d_leave_outs[ell] <- test_device(X_minus_ell) / (m - 1)
  }
  # SMI statistics under Jackknife rule (eq 3.9).
  T_ell <- (m - 1) * d_leave_outs + d_singles - m * d_1_to_m
  t_hat_1 <- mean(T_ell)
  r_hat <- max(t_hat_1, 0)  # truncate to keep the reference well-defined
  # Test statistic (eq 2.3) with bias correction applied to numerator.
  D_hat <- (d_1_to_m - bias_correction) / (1 + (1 + 1 / m) * r_hat)
  # MC reference distribution (eq 5.1, k = 1).
  G <- rchisq(N_mc, df = 1)
  H <- rchisq(N_mc, df = m - 1) / (m - 1)
  D_mc <- (1 + (1 + 1 / m) * r_hat) * G / (1 + (1 + 1 / m) * r_hat * H)
  p_value <- mean(D_mc >= D_hat)
  return(list(D_hat = D_hat, r_hat = r_hat, p_value = p_value,
              d_1_to_m = d_1_to_m, d_singles = d_singles,
              d_leave_outs = d_leave_outs, T_ell = T_ell))
}


# -----------------------------------------------------------------------------
# W3 candidate-model lavaan strings (preregistration §3.1).
#
# Truth Sigma_0^W3 has sigma_13 = sigma_24 = 0.4 and all other off-diagonals
# zero, so M_C below is true. (M_B and M_C have the same df = 10 but
# different RIV exposure — load-bearing for W3's directional prediction.)
# -----------------------------------------------------------------------------

LAVAAN_MOD_MA <- "
  X1 ~~ X1 + 0*X2 + 0*X3 + 0*X4
  X2 ~~ X2 + 0*X3 + 0*X4
  X3 ~~ X3 + 0*X4
  X4 ~~ X4
  X1 + X2 + X3 + X4 ~ 1
"  # diagonal Sigma (8 free params)

LAVAAN_MOD_MB <- "
  X1 ~~ X1 + X2 + 0*X3 + 0*X4
  X2 ~~ X2 + 0*X3 + 0*X4
  X3 ~~ X3 + X4
  X4 ~~ X4
  X1 + X2 + X3 + X4 ~ 1
"  # sigma_12 and sigma_34 free, cross-block = 0 (10 free params)

LAVAAN_MOD_MC <- "
  X1 ~~ X1 + 0*X2 + X3 + 0*X4
  X2 ~~ X2 + 0*X3 + X4
  X3 ~~ X3 + 0*X4
  X4 ~~ X4
  X1 + X2 + X3 + X4 ~ 1
"  # sigma_13 and sigma_24 free, others = 0 (10 free params) — TRUE under Sigma_0^W3

LAVAAN_MOD_MD <- LAVAAN_MOD_UN  # full unrestricted (14 free params)

W3_MODELS <- list(MA = LAVAAN_MOD_MA, MB = LAVAAN_MOD_MB,
                  MC = LAVAAN_MOD_MC, MD = LAVAAN_MOD_MD)

# Free-parameter indices in the full 14-dim theta vector (mu_{1:4},
# vech(Sigma)) for each candidate. vech order (column-major lower-tri,
# offset by 4 for mu) gives the Sigma entries:
#   pos 1=sigma_11, 2=sigma_21, 3=sigma_31, 4=sigma_41, 5=sigma_22,
#   pos 6=sigma_32, 7=sigma_42, 8=sigma_33, 9=sigma_43, 10=sigma_44
# +4 offset for the 4 mu entries -> full indices 5..14.
W3_FREE_IDX <- list(
  MA = c(1:4, 4 + c(1, 5, 8, 10)),                  # diag only
  MB = c(1:4, 4 + c(1, 2, 5, 8, 9, 10)),            # +sigma_12, +sigma_34
  MC = c(1:4, 4 + c(1, 3, 5, 7, 8, 10)),            # +sigma_13, +sigma_24
  MD = 1:14                                          # full
)

W3_NPAR <- sapply(W3_FREE_IDX, length)  # 8, 10, 10, 14


# -----------------------------------------------------------------------------
# Generic analytic tr(RIV) for an arbitrary sub-model (free_indices in the
# full 14-dim parameter space). Same construction as tr_riv_analytic and
# tr_riv_analytic_constrained_sigma12 but for any model.
# -----------------------------------------------------------------------------

tr_riv_analytic_general <- function(theta, Y, R, free_indices) {
  N <- nrow(Y)
  I_com_full <- fisher_info_com_mvn(theta, N)
  I_obs_full <- fisher_info_obs_mvn(theta, Y, R)
  I_com_sub  <- I_com_full[free_indices, free_indices]
  I_obs_sub  <- I_obs_full[free_indices, free_indices]
  return(sum(diag(solve(I_obs_sub, I_com_sub))) - length(free_indices))
}

# Sum-of-squared RIV eigenvalues on a sub-model's free parameters.
#   sum_lambda_sq = tr(RIV^2) where RIV = I_obs^{-1} I_{mis|obs}
#                 = tr((I_obs^{-1} I_com - I)^2)
#                 = tr((I_obs^{-1} I_com)^2) - 2 tr(I_obs^{-1} I_com) + p
# Returns the sum-of-squared eigenvalues of RIV on the specified subspace.
# Also returns tr_RIV for convenience.
riv_spectrum_analytic_general <- function(theta, Y, R, free_indices) {
  N <- nrow(Y)
  I_com_full <- fisher_info_com_mvn(theta, N)
  I_obs_full <- fisher_info_obs_mvn(theta, Y, R)
  I_com_sub  <- I_com_full[free_indices, free_indices]
  I_obs_sub  <- I_obs_full[free_indices, free_indices]
  p <- length(free_indices)
  M <- solve(I_obs_sub, I_com_sub)
  tr1 <- sum(diag(M))
  tr2 <- sum(M * t(M))  # tr(M^2) = sum of elementwise products with transpose
  tr_RIV <- tr1 - p
  sum_lambda_sq <- tr2 - 2 * tr1 + p
  return(list(tr_RIV = tr_RIV, sum_lambda_sq = sum_lambda_sq))
}


# -----------------------------------------------------------------------------
# Custom constrained MLE for sigma_{12} = 0: Cholesky parameterization
# (L[2,1] = 0 forces the constraint) with analytic gradient.
#
# Optim has 9 free Cholesky entries; mu is closed-form at the sample mean
# even under the Sigma constraint (constraint touches only Sigma).
#
# loss(L) = log|Sigma| + tr(Sigma^{-1} S),     Sigma = L L^T
# grad    = 2 L^{-T} - 2 Sigma^{-1} S Sigma^{-1} L  (projected to free entries
#                                                    of L, with chain rule for
#                                                    log-parameterized diagonals)
#
# Benchmark: ~40x faster per call than lavaan_fit_mvn with default settings.
# -----------------------------------------------------------------------------

mle_chol_sigma12 <- function(X) {
  N <- nrow(X)
  p <- ncol(X)
  stopifnot(p == 4)
  mu_hat <- colMeans(X)
  Xc <- sweep(X, 2, mu_hat, FUN = "-")
  S <- crossprod(Xc) / N

  build_L <- function(tau) {
    L <- matrix(0, 4, 4)
    L[1, 1] <- exp(tau[1])
    L[2, 2] <- exp(tau[2])
    L[3, 1] <- tau[3]
    L[3, 2] <- tau[4]
    L[3, 3] <- exp(tau[5])
    L[4, 1] <- tau[6]
    L[4, 2] <- tau[7]
    L[4, 3] <- tau[8]
    L[4, 4] <- exp(tau[9])
    return(L)
  }
  diag_idx <- c(1, 2, 5, 9)

  neg_loglik_raw <- function(tau) {
    L <- build_L(tau)
    # log|Sigma| = 2 * sum(log diag(L)) = 2 * sum(tau on diag positions)
    logdet_2 <- 2 * sum(tau[diag_idx])
    # Sigma^{-1} via Cholesky.
    Sigma_inv <- tryCatch(chol2inv(t(L)), error = function(e) { return(NULL) })
    if (is.null(Sigma_inv)) { return(1e10) }
    quad <- sum(Sigma_inv * S)  # = tr(Sigma^{-1} S) since S is symmetric
    return(logdet_2 + quad)
  }

  neg_loglik_grad <- function(tau) {
    L <- build_L(tau)
    L_inv <- tryCatch(solve(L), error = function(e) { return(NULL) })
    if (is.null(L_inv)) { return(rep(0, 9)) }
    Sigma_inv <- crossprod(L_inv)  # L^{-T} L^{-1}
    # grad of (log|Sigma| + tr(Sigma^{-1} S)) wrt full L matrix.
    G <- 2 * (t(L_inv) - Sigma_inv %*% S %*% Sigma_inv %*% L)
    grad <- numeric(9)
    grad[1] <- G[1, 1] * L[1, 1]
    grad[2] <- G[2, 2] * L[2, 2]
    grad[3] <- G[3, 1]
    grad[4] <- G[3, 2]
    grad[5] <- G[3, 3] * L[3, 3]
    grad[6] <- G[4, 1]
    grad[7] <- G[4, 2]
    grad[8] <- G[4, 3]
    grad[9] <- G[4, 4] * L[4, 4]
    return(grad)
  }

  # Starting Cholesky from sample covariance with sigma_12 zeroed.
  S_init <- S; S_init[1, 2] <- 0; S_init[2, 1] <- 0
  L_init <- tryCatch(t(chol(S_init)), error = function(e) {
    diag(sqrt(diag(S) + 1e-6))
  })
  par_init <- c(log(max(L_init[1, 1], 1e-3)),
                log(max(L_init[2, 2], 1e-3)),
                L_init[3, 1], L_init[3, 2], log(max(L_init[3, 3], 1e-3)),
                L_init[4, 1], L_init[4, 2], L_init[4, 3],
                log(max(L_init[4, 4], 1e-3)))
  opt <- stats::optim(par_init, neg_loglik_raw, gr = neg_loglik_grad,
                      method = "BFGS",
                      control = list(reltol = 1e-10, maxit = 200))
  L_hat <- build_L(opt$par)
  Sigma_hat <- tcrossprod(L_hat)
  ll <- -N / 2 * (p * log(2 * pi) + opt$value)
  return(list(mu = mu_hat, Sigma = Sigma_hat, logLik = ll,
              converged = opt$convergence == 0, iters = opt$counts[1]))
}


# Test device: complete-data LRT for sigma_{12} = 0.
#
# Unconstrained: closed-form MLE (microseconds).
# Constrained:  mle_chol_sigma12 (custom Cholesky optim with analytic
#               gradient) instead of lavaan — ~40x faster per call.
lrt_sigma12_device <- function(X) {
  theta_un <- mle_complete_mvn(X)
  ll_un <- loglik_mvn(theta_un, X)
  fit_cn <- mle_chol_sigma12(X)
  return(2 * (ll_un - fit_cn$logLik))
}


# -----------------------------------------------------------------------------
# §0.1 default DGP fixtures
# -----------------------------------------------------------------------------

default_mu <- c(0, 0, 0, 0)
default_Sigma <- matrix(c(
  1.0, 0.6, 0.3, 0.0,
  0.6, 1.0, 0.0, 0.3,
  0.3, 0.0, 1.0, 0.5,
  0.0, 0.3, 0.5, 1.0
), nrow = 4, byrow = TRUE)

# W3 truth: only sigma_13 and sigma_24 nonzero (per §3.1).
w3_sigma <- function(rho = 0.4) {
  S <- diag(4)
  S[1, 3] <- rho
  S[3, 1] <- rho
  S[2, 4] <- rho
  S[4, 2] <- rho
  return(S)
}
