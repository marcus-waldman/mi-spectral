# term-a-mar-general.R
#
# Phase 3a verification: the GENERAL-MVN (A)+(C) via the exact Term-A identity
#   A = sum_{i:mis} 1/2[ (m0_i - mhat_i)' Shat_i^{-1} (m0_i - mhat_i) + tr(Shat_i^{-1} S0_i) - d_i ],
# which is exactly what barQ_fiml_analytic computes for A_rb (verified against 00-setup.R:336).
#
# Taylor-expanding A(thetahat) about theta_0 (delta = thetahat - theta_0):
#   E[A] = alpha' E[delta] + 1/2 tr( H E[delta delta'] ),   alpha = grad_theta A|_0,  H = hess_theta A|_0.
# Then (A)+(C) = E[A] - tr(RIV). This script:
#   (1) measures E[A_rb] and tr_obs (the phase-8 quantity) -- cross-check;
#   (2) finite-differences the EXACT A(thetahat) at theta_0 per replicate to get alpha, H;
#   (3) reconstructs E[A] via the 2nd-order Taylor and checks it matches measured E[A_rb]
#       (a robust ~tr(RIV)-magnitude match), validating the decomposition;
#   (4) reports (A)+(C) = E[A_rb] - tr_obs and the Taylor split alpha'bias / curvature.
#
# Usage: Rscript verification/term-a-mar-general.R [pattern] [N] [R] [n_cores]
#        pattern in {non_monotone, monotone}; defaults non_monotone 500 200 20.

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
pattern = if (length(args) >= 1) { args[1] } else { "non_monotone" }
N_arg   = if (length(args) >= 2) { as.integer(args[2]) } else { 500 }
R_arg   = if (length(args) >= 3) { as.integer(args[3]) } else { 200 }
n_cores = if (length(args) >= 4) { as.integer(args[4]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p <- length(mu0)
k <- p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)

# --- pack/unpack theta = (mu, lower-tri-incl-diag of Sigma) ----------------------------
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)            # k-p rows: (row,col)
pack <- function(theta) { return(c(theta$mu, theta$Sigma[lower.tri(theta$Sigma, diag = TRUE)])) }
unpack <- function(par) {
  mu <- par[1:p]
  S <- matrix(0, p, p)
  S[lower.tri(S, diag = TRUE)] <- par[(p + 1):k]
  S[upper.tri(S)] <- t(S)[upper.tri(S)]
  return(list(mu = mu, Sigma = S))
}
par0 <- pack(theta0)

# --- exact A(thetahat) = A_rb as a function of the packed parameter --------------------
A_of_par <- function(par, Y, R) {
  th <- unpack(par)
  return(barQ_fiml_analytic(th, th, Y, R) - barQ_fiml_analytic(th, theta0, Y, R))
}

# central-difference gradient + Hessian of A_of_par at par0 (A(par0) = 0) --------------
grad_hess_A <- function(Y, R, h = 1e-3) {
  g <- numeric(k); H <- matrix(0, k, k)
  fp <- numeric(k); fm <- numeric(k)
  for (i in 1:k) {
    ei <- numeric(k); ei[i] <- h
    fp[i] <- A_of_par(par0 + ei, Y, R)
    fm[i] <- A_of_par(par0 - ei, Y, R)
    g[i] <- (fp[i] - fm[i]) / (2 * h)
    H[i, i] <- (fp[i] - 2 * 0 + fm[i]) / (h^2)          # A(par0) = 0
  }
  for (i in 1:(k - 1)) {
    for (j in (i + 1):k) {
      eij <- numeric(k); eij[i] <- h; eij[j] <- h
      eimj <- numeric(k); eimj[i] <- h; eimj[j] <- -h
      fpp <- A_of_par(par0 + eij, Y, R)
      fpm <- A_of_par(par0 + eimj, Y, R)
      fmp <- A_of_par(par0 - eimj, Y, R)
      fmm <- A_of_par(par0 - eij, Y, R)
      H[i, j] <- (fpp - fpm - fmp + fmm) / (4 * h^2)
      H[j, i] <- H[i, j]
    }
  }
  return(list(g = g, H = H))
}

one_rep <- function(r) {
  set.seed(20260522 + r)
  X <- gen_data(N_arg, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = pattern),
                  error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  th <- list(mu = fit$mu, Sigma = fit$Sigma)
  A_rb <- barQ_fiml_analytic(th, th, mar$Y, mar$R) - barQ_fiml_analytic(th, theta0, mar$Y, mar$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(th, mar$Y, mar$R), fisher_info_com_mvn(th, N_arg)))) - k
  gh <- grad_hess_A(mar$Y, mar$R)
  return(list(A_rb = A_rb, tr_obs = tr_obs, delta = pack(th) - par0, g = gh$g, H = gh$H))
}

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "pack", "unpack",
                    "A_of_par", "grad_hess_A", "pattern", "N_arg"))

cat(sprintf("\n== Term-A general-MVN check: %s, N=%d, R=%d ==\n", pattern, N_arg, R_arg))
res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_arg), one_rep))
nok <- length(res)

A_rb   <- sapply(res, `[[`, "A_rb")
tr_obs <- sapply(res, `[[`, "tr_obs")
D      <- do.call(rbind, lapply(res, `[[`, "delta"))      # nok x k
g_bar  <- Reduce(`+`, lapply(res, `[[`, "g")) / nok
bias   <- colMeans(D)

# Per-replicate 2nd-order Taylor of A about theta_0, T_r = g_r' d_r + 1/2 d_r' H_r d_r,
# which captures the g<->delta correlation (the (B)main/tr(RIV) cross term) exactly.
Tr   <- sapply(res, function(z) { return(sum(z$g * z$delta) + 0.5 * as.numeric(z$delta %*% z$H %*% z$delta)) })
# Linear (entropy-gradient) part per replicate -> (A); quadratic part -> (B)main + (C).
lin  <- sapply(res, function(z) { return(sum(z$g * z$delta)) })
quad <- sapply(res, function(z) { return(0.5 * as.numeric(z$delta %*% z$H %*% z$delta)) })

EA_meas   <- mean(A_rb)
EA_taylor <- mean(Tr)
trRIV     <- mean(tr_obs)

cat(sprintf("n_ok              = %d\n", nok))
cat(sprintf("E[A_rb] measured  = %+.4f (mcse %.4f)\n", EA_meas, sd(A_rb) / sqrt(nok)))
cat(sprintf("E[A]   Taylor(2)  = %+.4f (mcse %.4f)   [E linear = %+.4f ; E quad = %+.4f]\n",
            EA_taylor, sd(Tr) / sqrt(nok), mean(lin), mean(quad)))
cat(sprintf("  --> Taylor reconstruction error = %+.4f (should be ~0 / O(n^-3/2))\n", EA_taylor - EA_meas))
cat(sprintf("tr(RIV) = mean tr_obs            = %.4f\n", trRIV))
cat(sprintf("(A)+(C) = E[A_rb] - tr(RIV)      = %+.4f   [via Taylor: %+.4f]\n",
            EA_meas - trRIV, EA_taylor - trRIV))
cat(sprintf("  factored alpha'bias (entropy-grad x bias) = %+.4f ; max|alpha_mu| = %.2e (expect ~0: mean-params)\n",
            as.numeric(g_bar %*% bias), max(abs(g_bar[1:p]))))
