# term-a-mar-asymptote.R
#
# *** EXPLORATORY / FLAWED -- NOT EVIDENCE (2026-06-01). ***
# This cheap per-unit extrapolation MIS-PREDICTS the asymptote: it gave (A)+(C)=-0.18 (non-monotone),
# but the committed phase-8 sweep (term-a-mar-correction.R, R=40k) shows (A)+(C) growing past -0.46
# with n -- the WRONG SIGN of the n-trend. The factored alpha_u'b mixes per-unit gradients (N_ref)
# with a bias coefficient (N_bias) under a bias proportional 1/N assumption that does not hold; it
# does NOT capture the n-dependence of the MLE bias / per-unit moments. (The gradient<->deviation
# covariance is NOT the cause: tr Cov(g,delta)=+0.002, see term-a-mar-cov-check.R.) The asymptote
# VALUE is taken from the phase-8 sweep, not this script. Kept only as a record of the attempt.
# See manuscript/derivation.qmd @sec-termA lemma (Scope).
#
# Phase 3a: predict the N -> infinity asymptote of the Term-A MAR design-imbalance
#   (A)+(C)_inf = alpha_u' b  +  1/2 tr(H_u I_u^{-1}) - tr(RIV),
# with everything N-INDEPENDENT (per-unit), so no high-R brute force is needed:
#   alpha_u, H_u = (per-unit) gradient/Hessian of the exact A(thetahat) at theta_0,
#                  from ONE large reference dataset (self-averaging);
#   I_u          = (per-unit) observed-data information;
#   b            = lim n * E[thetahat - theta0]  (the MLE bias coefficient), measured
#                  from cheap FIML-only fits (alpha is covariance-only, so only b_Sigma matters).
# See term-a-mar-general.R (machinery validated: Taylor reconstructs E[A_rb]; alpha_mu = 0).
#
# Usage: Rscript verification/term-a-mar-asymptote.R [N_ref] [N_bias] [R_bias] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
N_ref   = if (length(args) >= 1) { as.integer(args[1]) } else { 8000 }
N_bias  = if (length(args) >= 2) { as.integer(args[2]) } else { 1000 }
R_bias  = if (length(args) >= 3) { as.integer(args[3]) } else { 2000 }
n_cores = if (length(args) >= 4) { as.integer(args[4]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p <- length(mu0)
k <- p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)
pack <- function(theta) { return(c(theta$mu, theta$Sigma[lower.tri(theta$Sigma, diag = TRUE)])) }
unpack <- function(par) {
  S <- matrix(0, p, p); S[lower.tri(S, diag = TRUE)] <- par[(p + 1):k]
  S[upper.tri(S)] <- t(S)[upper.tri(S)]
  return(list(mu = par[1:p], Sigma = S))
}
par0 <- pack(theta0)
A_of_par <- function(par, Y, R) {
  th <- unpack(par)
  return(barQ_fiml_analytic(th, th, Y, R) - barQ_fiml_analytic(th, theta0, Y, R))
}
grad_hess_A <- function(Y, R, h = 1e-3) {
  g <- numeric(k); H <- matrix(0, k, k); fp <- numeric(k); fm <- numeric(k)
  for (i in 1:k) {
    ei <- numeric(k); ei[i] <- h
    fp[i] <- A_of_par(par0 + ei, Y, R); fm[i] <- A_of_par(par0 - ei, Y, R)
    g[i] <- (fp[i] - fm[i]) / (2 * h); H[i, i] <- (fp[i] + fm[i]) / (h^2)
  }
  for (i in 1:(k - 1)) for (j in (i + 1):k) {
    epp <- numeric(k); epp[i] <- h; epp[j] <- h
    epm <- numeric(k); epm[i] <- h; epm[j] <- -h
    H[i, j] <- (A_of_par(par0 + epp, Y, R) - A_of_par(par0 + epm, Y, R) -
                A_of_par(par0 - epm, Y, R) + A_of_par(par0 - epp, Y, R)) / (4 * h^2)
    H[j, i] <- H[i, j]
  }
  return(list(g = g, H = H))
}

fit_one <- function(r, N, pattern) {
  set.seed(20260522 + r)
  X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = pattern),
                  error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  return(pack(list(mu = fit$mu, Sigma = fit$Sigma)) - par0)
}

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "pack", "unpack", "fit_one"))

cat(sprintf("\n== Term-A MAR asymptote (N_ref=%d, N_bias=%d, R_bias=%d) ==\n", N_ref, N_bias, R_bias))
for (pattern in c("non_monotone", "monotone")) {
  # 1) population per-unit alpha_u, H_u, I_u, tr(RIV) from one large reference dataset
  set.seed(20260522)
  Xr <- gen_data(N_ref, mu0, Sig0)
  marr <- apply_missingness_ampute(Xr, prop = 0.40, mech = "MAR", pattern_type = pattern)
  gh <- grad_hess_A(marr$Y, marr$R)
  alpha_u <- gh$g / N_ref
  H_u <- gh$H / N_ref
  Iobs_pop <- observed_info_obs_mvn(theta0, marr$Y, marr$R)
  trRIV <- sum(diag(solve(Iobs_pop, fisher_info_com_mvn(theta0, N_ref)))) - k
  curv <- 0.5 * sum(diag(gh$H %*% solve(Iobs_pop))) - trRIV   # 1/2 tr(H_u I_u^{-1}) - tr(RIV); N_ref cancels

  # 2) bias coefficient b = N_bias * E[thetahat - theta0] (only Sigma-block enters via alpha_u)
  D <- do.call(rbind, Filter(Negate(is.null),
         parLapply(cl, seq_len(R_bias), function(r, pat, nb) { return(fit_one(r, nb, pat)) },
                   pattern, N_bias)))
  bias <- colMeans(D)
  b <- N_bias * bias
  termA <- as.numeric(alpha_u %*% b)

  asymp <- termA + curv
  cat(sprintf("\n[%s]  tr(RIV)=%.3f\n", pattern, trRIV))
  cat(sprintf("  (A) alpha_u' b              = %+.4f   (b_Sigma drives it; max|alpha_u_mu|=%.1e)\n",
              termA, max(abs(alpha_u[1:p]))))
  cat(sprintf("  (C) 1/2 tr(H_u I_u^-1)-trRIV = %+.4f\n", curv))
  cat(sprintf("  (A)+(C) asymptote           = %+.4f\n", asymp))
  cat(sprintf("    [phase-8 finite-N (R=40k): N=800 %+.3f, N=1500 %+.3f, growing toward this]\n",
              if (pattern == "non_monotone") -0.336 else -0.179,
              if (pattern == "non_monotone") -0.456 else -0.270))
}
