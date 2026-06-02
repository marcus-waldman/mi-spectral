# term-ac-rem-distribution.R  [todo/020 -- theory-vs-empirics tension]
#
# Question: the SECOND-ORDER theory robustly gives (A)+(C)_realized ~ -0.22 (assembly + FD,
# eval-point fully accounted via the total-derivative form grad^2 A_RB = 2 I_mis|obs + H_phi),
# with higher-order O(1/n). The committed EMPIRICAL realized rem = A_rb - tr_real is -0.34(800)
# -> -0.46(1500), "still increasing" -- NOT converging to -0.22 and not a clean 1/n or 1/sqrt(n)
# correction. Is the empirical MEAN dragged by a heavy LEFT tail (rare near-singular realized
# observed-info O_obs => tr_real explodes => rem very negative), so that the CENTRAL value is
# actually ~ -0.22 (= theory) while the mean is an unstable heavy-tail statistic?
#
# This script measures the rem DISTRIBUTION (not just the mean) at a few n:
#   mean / median / 10%-trimmed mean / sd / IQR / min / max,
#   the correlation of rem_real with tr_real (does extreme tr_real drive extreme rem?),
#   and the mean after dropping the most extreme tr_real draws (winsor/trim on tr_real).
# Same seeds + primitives as _modules/term-a-mar-correction.R / term-ac-rivgap-lavaan.R.
#
# Usage: Rscript verification/term-ac-rem-distribution.R [R] [cores] [Ns]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_data  = if (length(args) >= 1) { as.integer(args[1]) } else { 8000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 4 }
Ns      = if (length(args) >= 3) { as.integer(strsplit(args[3], ",")[[1]]) } else { c(800, 1500) }

p = 4; mu0 <- default_mu; Sig0 <- default_Sigma; k = p + p * (p + 1) / 2
TRUTH <- list(mu = mu0, Sigma = Sig0)

one <- function(seed, N) {
  set.seed(seed)
  X <- gen_data(N, default_mu, default_Sigma)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone"),
                  error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values = TRUE)$values) < 1e-6) { return(NULL) }
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, TRUTH, mar$Y, mar$R)
  Icom <- fisher_info_com_mvn(to, N)
  Oobs <- observed_info_obs_mvn(to, mar$Y, mar$R)
  ev <- min(eigen(Oobs, only.values = TRUE)$values)            # smallest eig of realized obs info
  tr_real <- sum(diag(solve(Oobs, Icom))) - k
  tr_exp  <- sum(diag(solve(fisher_info_obs_mvn(to, mar$Y, mar$R), Icom))) - k
  return(c(A_rb = A_rb, rem_real = A_rb - tr_real, rem_exp = A_rb - tr_exp,
           tr_real = tr_real, tr_exp = tr_exp, Oobs_mineig = ev))
}

tmean <- function(x, tr = 0.10) { return(mean(x, trim = tr)) }
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); suppressPackageStartupMessages(library(lavaan)) }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "TRUTH", "one"))

cat("============ rem DISTRIBUTION diagnostic (heavy-tail / asymptote test) ============\n")
cat(sprintf("R=%d per N; second-order theory (A)+(C)_realized ~ -0.22; committed mean -0.34(800)/-0.46(1500)\n\n", R_data))
for (N in Ns) {
  M <- do.call(rbind, Filter(Negate(is.null),
        parLapply(cl, seq_len(R_data), function(s, NN) one(20260522 + s, NN), NN = N)))
  rr <- M[, "rem_real"]; tr <- M[, "tr_real"]
  # drop the 1% most extreme tr_real (largest |tr_real|) and recompute the mean
  keep <- abs(tr - median(tr)) <= quantile(abs(tr - median(tr)), 0.99)
  cat(sprintf("-- N=%d (%d ok) --\n", N, nrow(M)))
  cat(sprintf("   rem_real: mean=%+.4f(se %.4f)  median=%+.4f  trim10%%=%+.4f  sd=%.3f  IQR=%.3f\n",
              mean(rr), mcse(rr), median(rr), tmean(rr), sd(rr), IQR(rr)))
  cat(sprintf("            min=%+.3f  max=%+.3f  | cor(rem_real, tr_real)=%+.3f\n",
              min(rr), max(rr), cor(rr, tr)))
  cat(sprintf("   tr_real : mean=%+.3f  median=%+.3f  max=%+.3f  min_eig(O_obs) min=%.2e (q01=%.2e)\n",
              mean(tr), median(tr), max(tr), min(M[, "Oobs_mineig"]), quantile(M[, "Oobs_mineig"], 0.01)))
  cat(sprintf("   rem_real mean after dropping 1%% extreme tr_real = %+.4f (n=%d)\n",
              mean(rr[keep]), sum(keep)))
  cat(sprintf("   rem_exp : mean=%+.4f  median=%+.4f  trim10%%=%+.4f\n\n",
              mean(M[, "rem_exp"]), median(M[, "rem_exp"]), tmean(M[, "rem_exp"])))
}
stopCluster(cl)
cat("Reading: if mean << median ~ trim ~ -0.22 and cor(rem,tr_real) strongly negative => the -0.46\n")
cat("  empirical mean is a heavy-left-tail statistic (near-singular O_obs); central value ~ second-order theory.\n")
cat("===================================================================================\n")
