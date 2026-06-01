# term-a-mar-diagnostic.R
#
# Tests whether Term A's remainder (A)+(C) = E[A] - tr(RIV_obs) vanishes (O(1/n)) or is a
# nonzero O(1) constant under MAR -- i.e. whether E[A] = tr(RIV) holds under MAR or only MCAR.
# See todo/008. RB-A throughout: A_rb = barQ(theta_obs,theta_obs) - barQ(theta_obs,theta_true),
# E[A_rb] = E[A] (Rao-Blackwellization over the true completion).
#
# S1 (bivariate monotone, closed-form MLE): sweep selection strength b in the missingness
#    P(X1 missing | X2) = Phi(a + b X2); b=0 is MCAR. Compare the MEASURED remainder
#    E[A_rb] - tr(RIV_obs) to the leading-order ANALYTIC prediction
#       (A)+(C) = n_mis/n_obs - 1/2 tr(M_mis M_obs^-1),
#    with M_. = sum over (missing / observed) units of [1,X2][1,X2]^T. Also checks the RIV
#    decomposition tr(RIV_obs) ?= n_mis/n_obs + tr(M_mis M_obs^-1).
#
# S2 (4-variate W1 regime, lavaan FIML): precise E[A_rb] - tr(RIV_obs) under ampute MAR
#    (non_monotone, monotone), to see whether a small systematic nonzero hides there too.
#
# Usage: Rscript verification/term-a-mar-diagnostic.R <S1|S2|both> [R] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
study   = if (length(args) >= 1) { args[1] } else { "both" }
R_arg   = if (length(args) >= 2) { as.integer(args[2]) } else { 8000 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

# ---- S1: bivariate monotone, selection-strength sweep -----------------------------------
biv_mu <- c(0, 0); biv_Sig <- matrix(c(1, 0.5, 0.5, 1), 2, 2); biv_k <- 5
biv_true <- list(mu = biv_mu, Sigma = biv_Sig)
fiml_mono <- function(Y, R) {
  x2 <- Y[, 2]; mu2 <- mean(x2); s22 <- mean((x2 - mu2)^2)
  comp <- R[, 1] == 0; x1c <- Y[comp, 1]; x2c <- Y[comp, 2]
  b1 <- sum((x1c - mean(x1c)) * (x2c - mean(x2c))) / sum((x2c - mean(x2c))^2)
  b0 <- mean(x1c) - b1 * mean(x2c); v <- mean((x1c - (b0 + b1 * x2c))^2)
  return(list(mu = c(b0 + b1 * mu2, mu2),
              Sigma = matrix(c(v + b1^2 * s22, b1 * s22, b1 * s22, s22), 2, 2)))
}
s1_one <- function(r, N, b) {
  set.seed(20260522 + r)
  X <- mvtnorm::rmvnorm(N, biv_mu, biv_Sig)
  miss <- runif(N) < pnorm(-0.4 + b * X[, 2])
  if (sum(miss) < 5 || sum(!miss) < 8) { return(NULL) }
  Y <- X; Y[miss, 1] <- NA; R <- cbind(as.integer(miss), 0L)
  to <- fiml_mono(Y, R)
  A_rb <- barQ_fiml_analytic(to, to, Y, R) - barQ_fiml_analytic(to, biv_true, Y, R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, Y, R), fisher_info_com_mvn(to, N)))) - biv_k
  Z <- cbind(1, X[, 2]); Mmis <- crossprod(Z[miss, , drop = FALSE]); Mobs <- crossprod(Z[!miss, , drop = FALSE])
  nm <- sum(miss); no <- sum(!miss); trMM <- sum(diag(solve(Mobs, Mmis)))
  return(c(A_rb = A_rb, tr_obs = tr_obs, rem_meas = A_rb - tr_obs,
           rem_ana = nm / no - 0.5 * trMM, riv_ana = nm / no + trMM, miss = mean(miss)))
}
run_S1 <- function(cl, R) {
  cat(sprintf("\n== S1: bivariate monotone, selection sweep (N=800, R=%d) ==\n", R))
  cat(sprintf("%5s %7s %12s %12s %14s %14s\n", "b", "miss",
              "tr_obs", "RIV_ana", "rem_MEASURED", "rem_ANALYTIC"))
  for (b in c(0.0, 0.2, 0.4, 0.8)) {
    N <- 800   # N and b are captured by the parLapply closure below (no clusterExport needed)
    M <- do.call(rbind, Filter(Negate(is.null), parLapply(cl, seq_len(R), function(r) { return(s1_one(r, N, b)) })))
    cat(sprintf("%5.1f %7.3f %12.3f %12.3f %8.3f(%.3f) %12.3f\n", b, mean(M[, "miss"]),
                mean(M[, "tr_obs"]), mean(M[, "riv_ana"]),
                mean(M[, "rem_meas"]), mcse(M[, "rem_meas"]), mean(M[, "rem_ana"])))
  }
  cat("  [b=0 is MCAR -> rem ~ 0; rem_MEASURED should match rem_ANALYTIC; tr_obs ~ RIV_ana]\n")
}

# ---- S2: 4-variate W1 regime ------------------------------------------------------------
q_mu <- default_mu; q_Sig <- default_Sigma; q_k <- 14; q_true <- list(mu = q_mu, Sigma = q_Sig)
s2_one <- function(r, N, pattern) {
  set.seed(20260522 + r)
  X <- gen_data(N, q_mu, q_Sig)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = pattern),
                  error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, q_true, mar$Y, mar$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), fisher_info_com_mvn(to, N)))) - q_k
  return(c(rem = A_rb - tr_obs))
}
run_S2 <- function(cl, R) {
  cat(sprintf("\n== S2: 4-variate ampute MAR, E[A]-tr_obs (R=%d) ==\n", R))
  cat(sprintf("%-13s %6s %16s\n", "pattern", "N", "E[A]-tr_obs"))
  for (pat in c("non_monotone", "monotone")) {
    for (N in c(300, 800)) {   # smaller N: less A-variance; the MAR (A)+(C) constant is N-independent
      M <- do.call(rbind, Filter(Negate(is.null), parLapply(cl, seq_len(R), function(r) { return(s2_one(r, N, pat)) })))
      cat(sprintf("%-13s %6d %9.3f(%.3f)\n", pat, N, mean(M[, "rem"]), mcse(M[, "rem"])))
    }
  }
  cat("  [if Term A cancels under MAR -> ~0 shrinking with N; if not -> stable nonzero]\n")
}

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("s1_one", "fiml_mono", "biv_mu", "biv_Sig", "biv_k", "biv_true",
                    "s2_one", "q_mu", "q_Sig", "q_k", "q_true"))
if (study %in% c("S1", "both")) { run_S1(cl, R_arg) }
if (study %in% c("S2", "both")) { run_S2(cl, R_arg) }
