# scratch-rem-realized-expected-lavaan.R  [todo/016 follow-up]
#
# Clean lavaan-FIML re-measurement of the phase-8 non-monotone (A)+(C) remainder, decomposing
# it into the analytic leading-order (EXPECTED information) + a realized-information term.
# Replaces the earlier em_mvn probe, which gave unreliable (opposite-sign) fits here.
#
# Per replicate (SAME seeds as the committed phase-8 _modules/term-a-mar-correction.R, so
# rem_real must reproduce its -0.336(n=800) / -0.456(n=1500) -- a pipeline sanity check):
#   to       = lavaan FIML fit
#   A_rb     = barQ(to,to) - barQ(to,truth)
#   tr_real  = tr(observed_info(to)^-1 I_com(to)) - k     (REALIZED Hessian; = committed)
#   tr_exp   = tr(fisher_info_obs(to)^-1 I_com(to)) - k   (EXPECTED Fisher info)
#   rem_real = A_rb - tr_real     [-> committed empirical ~ -0.46]
#   rem_exp  = A_rb - tr_exp      [-> my analytic leading order ~ -0.24 ?]
#   gap      = tr_exp - tr_real = rem_real - rem_exp (PAIRED, low variance) = realized-info term
#
# Decision: (a) rem_exp ~ -0.24 & gap carries the rest -> the -0.46 IS analytic-leading +
# realized-information term (upgrade the manuscript's "finite-n" wording to a derived statement);
# (b) rem_exp far from -0.24 -> residual still unaccounted. Also report the N-trend of `gap`
# (growing => realized-info term is the engine of the empirical's increase with n).

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_data  = if (length(args) >= 1) { as.integer(args[1]) } else { 4000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }
Ns      = if (length(args) >= 3) { as.integer(strsplit(args[3], ",")[[1]]) } else { c(800, 1500) }

p = 4; mu0 <- default_mu; Sig0 <- default_Sigma; k = p + p * (p + 1) / 2
TRUTH <- list(mu = mu0, Sigma = Sig0)
COMMITTED <- c("300" = -0.0315, "800" = -0.3358, "1500" = -0.4563)   # _modules/term-a-mar-correction.R, R=40k
ANALYTIC_LEADING = -0.24   # (A)+(C) two-term -0.22 + B_cov -0.02 (expected info); verify_term_ac_nonmonotone_4v.R

one <- function(seed, N) {
  set.seed(seed)                                   # MATCH the committed module's seed convention
  X <- gen_data(N, default_mu, default_Sigma)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone"),
                  error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values = TRUE)$values) < 1e-6) { return(NULL) }
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, TRUTH, mar$Y, mar$R)
  Icom <- fisher_info_com_mvn(to, N)
  tr_real <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), Icom))) - k
  tr_exp  <- sum(diag(solve(fisher_info_obs_mvn(to, mar$Y, mar$R), Icom))) - k
  return(c(rem_real = A_rb - tr_real, rem_exp = A_rb - tr_exp,
           tr_real = tr_real, tr_exp = tr_exp, gap = tr_exp - tr_real))
}

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); suppressPackageStartupMessages(library(lavaan)) }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "TRUTH", "one"))
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

cat("====== lavaan-FIML rem: realized- vs expected-information decomposition (phase-8 non-monotone) ======\n")
cat(sprintf("R=%d per N; committed empirical (R=40k): -0.336(800) -> -0.456(1500); analytic leading ~ %.2f\n",
            R_data, ANALYTIC_LEADING))
rows <- list()
for (N in Ns) {
  M <- do.call(rbind, Filter(Negate(is.null),
        parLapply(cl, seq_len(R_data), function(s, NN) one(20260522 + s, NN), NN = N)))
  comm <- if (as.character(N) %in% names(COMMITTED)) { COMMITTED[[as.character(N)]] } else { NA }
  cat(sprintf("\n-- N=%d (%d ok) --\n", N, nrow(M)))
  cat(sprintf("   rem_real = A_rb - tr_obs(realized) = %+.4f (%.4f)   [committed %s]\n",
              mean(M[, "rem_real"]), mcse(M[, "rem_real"]),
              if (is.na(comm)) "n/a" else sprintf("%.3f", comm)))
  cat(sprintf("   rem_exp  = A_rb - tr_obs(expected) = %+.4f (%.4f)   [analytic leading ~ %.2f]\n",
              mean(M[, "rem_exp"]), mcse(M[, "rem_exp"]), ANALYTIC_LEADING))
  cat(sprintf("   gap = tr_exp - tr_real (PAIRED)    = %+.4f (%.4f)   <-- realized-information term\n",
              mean(M[, "gap"]), mcse(M[, "gap"])))
  cat(sprintf("   (tr_real=%.3f  tr_exp=%.3f)\n", mean(M[, "tr_real"]), mean(M[, "tr_exp"])))
  rows[[as.character(N)]] <- c(N = N, rem_real = mean(M[, "rem_real"]), rem_real_se = mcse(M[, "rem_real"]),
                               rem_exp = mean(M[, "rem_exp"]), rem_exp_se = mcse(M[, "rem_exp"]),
                               gap = mean(M[, "gap"]), gap_se = mcse(M[, "gap"]), n_ok = nrow(M))
}
stopCluster(cl)

cat("\n-- summary --\n")
S <- do.call(rbind, rows)
print(round(S, 4))
if (length(Ns) >= 2) {
  cat(sprintf("\n   gap N-trend: %s  =>  %s\n",
              paste(sprintf("N%d:%+.3f", S[, "N"], S[, "gap"]), collapse = "  "),
              "growing|.| => realized-info term drives the empirical's increase with n; shrinking => finite-n"))
}
saveRDS(S, "verification/cache/rem-realized-expected-lavaan.rds")
cat("\nwrote verification/cache/rem-realized-expected-lavaan.rds\n")
cat("=====================================================================================================\n")
