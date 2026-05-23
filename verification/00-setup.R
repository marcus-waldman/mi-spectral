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
