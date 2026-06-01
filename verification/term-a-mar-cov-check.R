# term-a-mar-cov-check.R
#
# Diagnostic for the asymptote-script discrepancy (predicted (A)+(C)=-0.18 vs phase-8 ~-0.46).
# Hypothesis: the factored (A)=mean(g)'mean(delta) drops the covariance between the
# data-dependent entropy gradient g(Y)=grad_thetahat A|theta0 and the fit deviation
# delta=thetahat-theta0 (both functions of the same observed data). The FULL (A) is
#   (A) = E[g' delta] = mean(g)'mean(delta) + tr(Cov(g,delta)).
# This script measures both (gradient only per replicate -- no Hessian -- so it's cheap)
# at a single N (default 800, a phase-8 comparison point) and reports the covariance.
#
# Usage: Rscript verification/term-a-mar-cov-check.R [pattern] [N] [R] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
pattern = if (length(args) >= 1) { args[1] } else { "non_monotone" }
N_arg   = if (length(args) >= 2) { as.integer(args[2]) } else { 800 }
R_arg   = if (length(args) >= 3) { as.integer(args[3]) } else { 8000 }
n_cores = if (length(args) >= 4) { as.integer(args[4]) } else { 24 }

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
grad_A <- function(Y, R, h = 1e-3) {   # central-difference gradient only (2k evals)
  g <- numeric(k)
  for (i in 1:k) {
    ei <- numeric(k); ei[i] <- h
    g[i] <- (A_of_par(par0 + ei, Y, R) - A_of_par(par0 - ei, Y, R)) / (2 * h)
  }
  return(g)
}
one_rep <- function(r) {
  set.seed(20260522 + r)
  X <- gen_data(N_arg, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = pattern),
                  error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  th <- list(mu = fit$mu, Sigma = fit$Sigma)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(th, mar$Y, mar$R), fisher_info_com_mvn(th, N_arg)))) - k
  return(list(g = grad_A(mar$Y, mar$R), delta = pack(th) - par0, tr_obs = tr_obs))
}

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "pack", "unpack",
                    "A_of_par", "grad_A", "one_rep", "pattern", "N_arg"))

cat(sprintf("\n== Cov(g,delta) check: %s, N=%d, R=%d ==\n", pattern, N_arg, R_arg))
res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_arg), one_rep))
nok <- length(res)
G <- do.call(rbind, lapply(res, `[[`, "g"))       # nok x k
D <- do.call(rbind, lapply(res, `[[`, "delta"))   # nok x k
gd <- rowSums(G * D)                               # per-rep g' delta
g_bar <- colMeans(G); d_bar <- colMeans(D)

factored_A <- sum(g_bar * d_bar)
full_A     <- mean(gd)
cov_A      <- full_A - factored_A
trRIV      <- mean(sapply(res, `[[`, "tr_obs"))

cat(sprintf("n_ok                       = %d\n", nok))
cat(sprintf("factored (A) = mean(g)'mean(d) = %+.4f\n", factored_A))
cat(sprintf("full     (A) = mean(g' d)      = %+.4f (mcse %.4f)\n", full_A, sd(gd) / sqrt(nok)))
cat(sprintf("  tr(Cov(g,delta)) = full - factored = %+.4f   <- the dropped term\n", cov_A))
cat(sprintf("tr(RIV) = mean tr_obs          = %.4f\n", trRIV))
cat(sprintf("phase-8 (A)+(C) at N=%d (R=40k): %+.3f\n", N_arg,
            if (pattern == "non_monotone") -0.336 else -0.179))
cat(sprintf("  --> if (C)-side covariance is small, corrected (A)+(C) ~ full_A + [factored-asymptote (C)]\n"))
