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
