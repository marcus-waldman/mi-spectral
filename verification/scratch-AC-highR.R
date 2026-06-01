# scratch-AC-highR.R  [EXPLORATORY — Phase 3a, todo/010]
#
# Decisive measured curve: high-R (Rao-Blackwellized) (A)+(C) = E[A_rb] - tr_obs at LARGER N
# than phase-8 reached (it stopped at N=1500 = -0.270, still growing). Fast (closed-form monotone
# MLE, no finite differences), so R=40000 at large N is affordable. Confirms the measured curve
# continues to climb toward the closed-form asymptote AC_pred ~ -0.30 (scratch-AC-asymptote.R).
#
# Usage: Rscript verification/scratch-AC-highR.R [R] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_arg   = if (length(args) >= 1) { as.integer(args[1]) } else { 40000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p = length(mu0)
k = p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)
Ngrid <- c(800, 1500, 3000, 6000)

fiml_monotone_kstep <- function(Y, R) {
  obs_through <- function(j) { if (j == 1) { return(R[, 1] == 0) } else { return(rowSums(R[, 1:j, drop = FALSE]) == 0) } }
  mu <- numeric(p); Sigma <- matrix(0, p, p); s1 <- obs_through(1); x1 <- Y[s1, 1]
  mu[1] = mean(x1); Sigma[1, 1] = mean((x1 - mu[1])^2)
  for (j in 2:p) {
    sj <- obs_through(j); Xpred <- cbind(1, Y[sj, 1:(j - 1), drop = FALSE]); yj <- Y[sj, j]
    coef <- solve(crossprod(Xpred), crossprod(Xpred, yj)); b_j <- coef[-1]; v_j = mean((yj - Xpred %*% coef)^2)
    Sig_prev <- Sigma[1:(j - 1), 1:(j - 1), drop = FALSE]; mu[j] = coef[1] + sum(b_j * mu[1:(j - 1)])
    Sigma[j, 1:(j - 1)] <- as.numeric(b_j %*% Sig_prev); Sigma[1:(j - 1), j] <- Sigma[j, 1:(j - 1)]
    Sigma[j, j] = v_j + as.numeric(b_j %*% Sig_prev %*% b_j)
  }
  return(list(mu = mu, Sigma = Sigma))
}
one <- function(r, N) {
  set.seed(20260601 + r); X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone"), error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  to <- tryCatch(fiml_monotone_kstep(mar$Y, mar$R), error = function(e) { return(NULL) }); if (is.null(to)) { return(NULL) }
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, theta0, mar$Y, mar$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), fisher_info_com_mvn(to, N)))) - k
  return(c(rem = A_rb - tr_obs))
}
cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "fiml_monotone_kstep", "one"))

cat(sprintf("\n== high-R measured (A)+(C) = E[A_rb]-tr_obs (monotone MAR, R=%d) ==\n", R_arg))
cat(sprintf("%-6s %16s\n", "N", "(A)+(C)_meas"))
for (N in Ngrid) {
  clusterExport(cl, "N")
  v <- unlist(Filter(Negate(is.null), parLapply(cl, seq_len(R_arg), function(r) { return(one(r, N)) })))
  cat(sprintf("%-6d %+9.4f(%.4f)\n", N, mean(v), sd(v) / sqrt(length(v))))
}
cat("\n  [phase-8: -0.111/-0.179/-0.270 at N=300/800/1500; closed-form AC_pred ~ -0.30]\n")
