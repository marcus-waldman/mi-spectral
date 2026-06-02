# rederivation-knownvar.R
#
# Adjudicating experiment for todo/015-chat-conjectures-reconciliation.md.
#
# Tests Conjecture C1 (NON-UNIVERSALITY of the +1/2 tr(RIV) headline) and
# C3 (deterministic FIML != proper MI) on a KNOWN-VARIANCE MVN: Sigma is
# fixed/known and only the mean mu is estimated. This is the regime where
# the conditional (missing-data) entropy does NOT depend on the estimated
# parameter, so the conjectures predict the headline collapses.
#
# Per replicate (Sigma = Sigma0 known throughout):
#   theta_com  = complete-data mean MLE (known Sigma) = colMeans(X)
#   theta_obs  = observed-data mean MLE (known Sigma) = GLS / observed-score=0,
#                closed form: (sum_i S_i' Sigma_OO^{-1} S_i) mu = sum_i S_i' Sigma_OO^{-1} y_O
#   ell_com(mu;X) = full normalized MVN log-density at known Sigma0
#   barQ_fiml(mu_eval)   = E_{X_mis|Y_obs,theta_obs}[ell_com(mu_eval;X)]
#                          (deterministic E-step at the point theta_obs)
#   barQ_proper(mu_eval) = E_{mu~}E_{X_mis|Y_obs,mu~}[ell_com(mu_eval;X)],
#                          mu~ ~ N(theta_obs, I_obs(mu)^{-1}) (proper posterior draw).
#                          m->infinity analytic form: barQ_fiml - C_n, where
#                          C_n = 1/2 sum_i tr(Sigma0^{-1} H_i Phi H_i') is the
#                          posterior-uncertainty contribution to the imputation
#                          covariance (Phi = I_obs(mu)^{-1}, H_i the Jacobian of
#                          the imputed full vector w.r.t. mu~). Verified by the
#                          built-in MC spot-check (arm 4 below) and by the
#                          univariate fully-missing hand-calc (C_n -> 1/2 tr(RIV)).
#
#   A_fiml   = barQ_fiml(theta_obs)   - ell_com(theta_obs)
#   A_proper = barQ_proper(theta_obs) - ell_com(theta_obs)   ( = A_fiml - C_n )
#   B        = ell_com(theta_obs)     - ell_com(theta_com)
#   T_*      = A_* + B
#   tr(RIV)  = mu-block only: tr(I_com(mu) I_obs(mu)^{-1}) - p,
#              I_com(mu) = N Sigma0^{-1}, I_obs(mu) = sum_i S_i' Sigma_OO^{-1} S_i.
#
# PREDICTIONS (if C1/C3 hold; contrast the unknown-Sigma baseline E[T]~=+1/2 trRIV):
#   FIML  : E[A] ~= +1/2 trRIV, E[T] ~= 0
#   proper: E[A] ~= 0,          E[T] ~= -1/2 trRIV
#   both  : E[B] ~= -1/2 trRIV
#   ==> NEITHER arm gives +1/2 trRIV  ==> headline non-universal (C1 confirmed),
#       FIML != proper by C_n ~= +1/2 trRIV (C3 confirmed).
#
# Run: Rscript verification/rederivation-knownvar.R [R] [N] [cores] [mc_draws]
#   mc_draws > 0 enables the analytic-vs-MC proper spot-check on a few replicates.

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args <- commandArgs(trailingOnly = TRUE)
R = if (length(args) >= 1) { as.integer(args[1]) } else { 4000 }
N = if (length(args) >= 2) { as.integer(args[2]) } else { 200 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }
mc_draws = if (length(args) >= 4) { as.integer(args[4]) } else { 0 }

mu0 <- default_mu
Sigma0 <- default_Sigma
Sig0inv <- solve(Sigma0)
p = length(mu0)

# ---- observed-data mean MLE with KNOWN Sigma (GLS) + I_obs(mu) block ---------
# Returns the closed-form mean estimate and the mu-block observed information
# I_obs(mu) = sum_i S_i' Sigma_{O_i O_i}^{-1} S_i (deterministic given Sigma0).
mle_obs_mean_knownvar <- function(Y, R, Sigma) {
  pp = ncol(Y)
  A <- matrix(0, pp, pp)
  b <- numeric(pp)
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat)
    Oi <- which(R[rows[1], ] == 0)
    if (length(Oi) == 0) { next }
    Soo_inv <- solve(Sigma[Oi, Oi, drop = FALSE])
    n_pat = length(rows)
    A[Oi, Oi] <- A[Oi, Oi] + n_pat * Soo_inv
    Ysub <- Y[rows, Oi, drop = FALSE]
    b[Oi] <- b[Oi] + as.numeric(Soo_inv %*% colSums(Ysub))
  }
  mu_hat <- as.numeric(solve(A, b))
  return(list(mu = mu_hat, I_obs_mu = A))
}

# ---- proper-MI posterior-uncertainty term C_n -------------------------------
# C_n = 1/2 sum_i tr(Sigma0^{-1} H_i Phi H_i'), Phi = I_obs(mu)^{-1}.
# H_i (p x p): rows in M_i = (E_M - reg_i E_O), rows in O_i = 0; reg_i = Sigma_MO Sigma_OO^{-1}.
# Depends only on the pattern, so accumulate per pattern weighted by count.
proper_Cn <- function(R, Sigma, Phi) {
  pp = ncol(R)
  Sinv <- solve(Sigma)
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  Cn = 0
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat)
    n_pat = length(rows)
    Oi <- which(R[rows[1], ] == 0)
    Mi <- which(R[rows[1], ] == 1)
    if (length(Mi) == 0) { next }
    H <- matrix(0, pp, pp)
    Hm <- matrix(0, length(Mi), pp)
    Hm[, Mi] <- diag(length(Mi))
    if (length(Oi) > 0) {
      reg <- Sigma[Mi, Oi, drop = FALSE] %*% solve(Sigma[Oi, Oi, drop = FALSE])
      Hm[, Oi] <- Hm[, Oi] - reg
    }
    H[Mi, ] <- Hm
    Cn = Cn + n_pat * 0.5 * sum(diag(Sinv %*% H %*% Phi %*% t(H)))
  }
  return(Cn)
}

# ---- one replicate ----------------------------------------------------------
run_one <- function(r, N, mc_draws = 0) {
  set.seed(20260522 + r)
  X <- gen_data(N = N, mu = mu0, Sigma = Sigma0)
  theta_com <- list(mu = colMeans(X), Sigma = Sigma0)
  mar <- apply_mar(X)
  fit <- mle_obs_mean_knownvar(mar$Y, mar$R, Sigma0)
  theta_obs <- list(mu = fit$mu, Sigma = Sigma0)
  Phi <- solve(fit$I_obs_mu)

  ell_com_at_obs = loglik_mvn(theta_obs, X)
  ell_com_at_com = loglik_mvn(theta_com, X)

  # FIML: deterministic E-step at theta_obs, eval at theta_obs, Sigma0 throughout.
  barQ_fiml = barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R)
  Cn = proper_Cn(mar$R, Sigma0, Phi)
  barQ_proper = barQ_fiml - Cn

  I_com_mu <- N * Sig0inv
  trRIV = sum(diag(solve(fit$I_obs_mu, I_com_mu))) - p

  # Boundary anchor (todo/017 C2): with Sigma known/fixed, C_n depends only on
  # the (fixed) Sigma, so Delta_n = C_n(theta_obs) - C_n(theta0) = 0 identically.
  Delta_n = cond_entropy_Cn(theta_obs, mar$R) -
    cond_entropy_Cn(list(mu = mu0, Sigma = Sigma0), mar$R)

  out <- list(
    A_fiml   = barQ_fiml - ell_com_at_obs,
    A_proper = barQ_proper - ell_com_at_obs,
    B        = ell_com_at_obs - ell_com_at_com,
    T_fiml   = barQ_fiml - ell_com_at_com,
    T_proper = barQ_proper - ell_com_at_com,
    Cn       = Cn,
    Delta_n  = Delta_n,
    trRIV    = trRIV
  )

  # Optional MC spot-check of the analytic proper barQ: average barQ over
  # posterior draws mu~ ~ N(theta_obs, Phi) (eval point held at theta_obs).
  if (mc_draws > 0) {
    L <- chol(Phi)  # upper; mu_draw = theta_obs$mu + t(L) %*% z
    acc = 0
    for (d in seq_len(mc_draws)) {
      z <- rnorm(p)
      mu_draw <- as.numeric(theta_obs$mu + t(L) %*% z)
      acc = acc + barQ_fiml_analytic(theta_obs, list(mu = mu_draw, Sigma = Sigma0),
                                     mar$Y, mar$R)
    }
    out$barQ_proper_mc = acc / mc_draws
    out$barQ_proper_an = barQ_proper
  }
  return(out)
}

# ---- run --------------------------------------------------------------------
cat(sprintf("=== Known-variance adjudicating experiment: N=%d, R=%d, cores=%d ===\n",
            N, R, n_cores))
cat("Sigma fixed/known; estimating the mean only (mu-block RIV).\n\n")

if (n_cores > 1) {
  cl <- makeCluster(n_cores)
  on.exit(stopCluster(cl), add = TRUE)
  clusterEvalQ(cl, source("verification/00-setup.R"))
  clusterExport(cl, varlist = c("mu0", "Sigma0", "Sig0inv", "p", "N", "mc_draws",
                                "run_one", "mle_obs_mean_knownvar", "proper_Cn"))
  res <- pblapply(seq_len(R), function(r) { return(run_one(r, N, mc_draws)) }, cl = cl)
} else {
  res <- pblapply(seq_len(R), function(r) { return(run_one(r, N, mc_draws)) })
}

grab <- function(nm) { return(vapply(res, `[[`, numeric(1), nm)) }
A_f <- grab("A_fiml")
A_p <- grab("A_proper")
B   <- grab("B")
T_f <- grab("T_fiml")
T_p <- grab("T_proper")
Cn  <- grab("Cn")
dn  <- grab("Delta_n")
tr  <- grab("trRIV")
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }
mtr = mean(tr)

cat(sprintf("mean tr(RIV_mu) = %.4f   (1/2 trRIV = %.4f)\n\n", mtr, 0.5 * mtr))

cat(sprintf("E[B]        = %+.4f (SE %.4f)   target -1/2 trRIV = %+.4f   ratio B/(-1/2 trRIV) = %.3f\n\n",
            mean(B), mcse(B), -0.5 * mtr, mean(B) / (-0.5 * mtr)))

cat("--- FIML (deterministic E-step at theta_obs) ---\n")
cat(sprintf("E[A_fiml] = %+.4f (SE %.4f)   pred +1/2 trRIV = %+.4f   ratio A/(1/2 trRIV) = %.3f\n",
            mean(A_f), mcse(A_f), 0.5 * mtr, mean(A_f) / (0.5 * mtr)))
cat(sprintf("E[T_fiml] = %+.4f (SE %.4f)   pred 0           (E[T]/(1/2 trRIV) = %+.3f ; E[T]/(-1/2 trRIV) = %+.3f)\n\n",
            mean(T_f), mcse(T_f), mean(T_f) / (0.5 * mtr), mean(T_f) / (-0.5 * mtr)))

cat("--- proper MI (posterior draw mu~ ~ N(theta_obs, I_obs^{-1})) ---\n")
cat(sprintf("E[A_proper] = %+.4f (SE %.4f)   pred 0           (E[A]/(1/2 trRIV) = %+.3f)\n",
            mean(A_p), mcse(A_p), mean(A_p) / (0.5 * mtr)))
cat(sprintf("E[T_proper] = %+.4f (SE %.4f)   pred -1/2 trRIV = %+.4f   ratio T/(-1/2 trRIV) = %.3f\n\n",
            mean(T_p), mcse(T_p), -0.5 * mtr, mean(T_p) / (-0.5 * mtr)))

cat(sprintf("E[C_n] (FIML-proper gap) = %+.4f (SE %.4f)   pred +1/2 trRIV = %+.4f   ratio = %.3f\n",
            mean(Cn), mcse(Cn), 0.5 * mtr, mean(Cn) / (0.5 * mtr)))

cat(sprintf("E[Delta_n] (entropy plug-in bias) = %+.2e (max|.| %.1e)   pred 0  [known-scale boundary anchor: C_n is Sigma-free, todo/017 C2]\n",
            mean(dn), max(abs(dn))))

cat("\n--- DISCRIMINATING CHECK vs +1/2 trRIV (the universality claim) ---\n")
cat(sprintf("FIML   E[T]/(+1/2 trRIV) = %+.3f   proper E[T]/(+1/2 trRIV) = %+.3f   (universal headline would be ~ +1.0)\n",
            mean(T_f) / (0.5 * mtr), mean(T_p) / (0.5 * mtr)))

if (mc_draws > 0) {
  an <- vapply(res, function(e) { return(e$barQ_proper_an) }, numeric(1))
  mc <- vapply(res, function(e) { return(e$barQ_proper_mc) }, numeric(1))
  cat(sprintf("\n--- proper barQ analytic vs MC (%d draws/rep) ---\n", mc_draws))
  cat(sprintf("max |analytic - MC| = %.4g   mean |analytic - MC| = %.4g   (MC noise ~ O(1/sqrt(draws)))\n",
              max(abs(an - mc)), mean(abs(an - mc))))
}

# ---- persist ----------------------------------------------------------------
out_path <- file.path("verification/cache",
                      sprintf("rederivation-knownvar-N%d-R%d.rds", N, R))
saveRDS(list(
  cfg = list(N = N, R = R, mu0 = mu0, Sigma0 = Sigma0, seed_base = 20260522),
  per_rep = res,
  summary = list(
    trRIV = mtr,
    A_fiml = mean(A_f), A_proper = mean(A_p), B = mean(B),
    T_fiml = mean(T_f), T_proper = mean(T_p), Cn = mean(Cn),
    se = list(A_fiml = mcse(A_f), A_proper = mcse(A_p), B = mcse(B),
              T_fiml = mcse(T_f), T_proper = mcse(T_p), Cn = mcse(Cn))
  )
), out_path)
cat(sprintf("\nSaved -> %s\n", out_path))
