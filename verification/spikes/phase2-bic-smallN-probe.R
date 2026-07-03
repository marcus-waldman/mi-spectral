# phase2-bic-smallN-probe.R
#
# Focused follow-up to todo/040 Phase 2 (MI-BIC). The main 60-cell grid puts
# uncorrected BIC near ceiling (98.3% recovery) almost everywhere, because
# BIC's npar*log(N) penalty already resists the saturated-model pull at
# N>=200. This probe looks for a regime where BIC is genuinely ambiguous by
# going to smaller N, where log(N) is small relative to the roughly
# N-invariant chi-square deviance-noise scale that drives AIC-style
# selection. Reuses run_one_w3 from w3-sweep.R unchanged (it is already
# generic in cell$N) -- only the cell list here is new.
#
# Scope: non_monotone / MAR / congenial slice only (the existing headline
# cell), N in {50, 100}, one fiml cell + one amelia M=20 congenial cell per
# N (4 cells total). NOT part of the main run_all.R 60-cell grid; output goes
# to its own cache directory.
#
# Usage:
#   Rscript verification/spikes/phase2-bic-smallN-probe.R <R> <out_suffix> [n_cores]
# Examples:
#   Rscript verification/spikes/phase2-bic-smallN-probe.R 100  smoke 20
#   Rscript verification/spikes/phase2-bic-smallN-probe.R 2000 prod  20

source("verification/00-setup.R")
source("verification/_modules/w3-sweep.R")

suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args <- commandArgs(trailingOnly = TRUE)
R_per_cell <- if (length(args) >= 1) as.integer(args[1]) else 100
out_suffix <- if (length(args) >= 2) args[2] else "smoke"
n_cores    <- if (length(args) >= 3) as.integer(args[3]) else 20

out_dir <- sprintf("verification/cache/smallN-bic-probe-%s", out_suffix)
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)

cat(sprintf("\n=== phase2-bic-smallN-probe [R=%d, out_suffix=%s, n_cores=%d] ===\n",
            R_per_cell, out_suffix, n_cores))
cat(sprintf("out dir: %s\n", out_dir))

Sigma_truth_w3 <- w3_sigma(rho = 0.4)

cells <- list()
cid <- 0
for (N in c(50, 100)) {
  cid <- cid + 1
  cells[[cid]] <- list(id = sprintf("fiml_non_monotone_MAR_N%d", N),
                        pattern = "non_monotone", mech = "MAR", N = N,
                        engine = "fiml", M = NA_integer_, empri_frac = 0,
                        prop = 0.40)
  cid <- cid + 1
  cells[[cid]] <- list(id = sprintf("amelia_non_monotone_MAR_N%d_M20_cong", N),
                        pattern = "non_monotone", mech = "MAR", N = N,
                        engine = "amelia", M = 20, empri_frac = 0,
                        prop = 0.40)
}
cat(sprintf("Cells: %d\n", length(cells)))

cl <- NULL
if (n_cores > 1) {
  cl <- parallel::makeCluster(n_cores)
  parallel::clusterEvalQ(cl, { invisible(source("verification/00-setup.R")) })
  parallel::clusterEvalQ(cl, { invisible(source("verification/_modules/w3-sweep.R")) })
  parallel::clusterExport(cl, varlist = c("Sigma_truth_w3"), envir = environment())
  on.exit({ if (!is.null(cl)) try(parallel::stopCluster(cl), silent = TRUE) }, add = TRUE)
}

rows <- list()
t_master <- Sys.time()
for (i in seq_along(cells)) {
  cell <- cells[[i]]
  if (!is.null(cl)) parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
  cat(sprintf("[%d/%d] %-45s  ", i, length(cells), cell$id))
  t0 <- Sys.time()
  results <- if (is.null(cl)) {
    pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_w3(r, cell, default_mu, Sigma_truth_w3))
    })
  } else {
    pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_w3(r, cell, default_mu, Sigma_truth_w3))
    }, cl = cl)
  }
  elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
  errors <- sapply(results, function(rr) !is.null(rr$error) && !is.na(rr$error))
  n_err <- sum(errors); ok <- results[!errors]
  tab <- function(field) {
    if (length(ok) == 0) return(setNames(rep(NA_real_, 4), W3_MODEL_NAMES))
    sels <- sapply(ok, `[[`, field)
    return(sapply(W3_MODEL_NAMES, function(k) mean(sels == k)))
  }
  rt <- rbind(oracle = tab("sel_oracle"), uncorrected = tab("sel_uncorr"),
              corrected = tab("sel_corrected"), SB = tab("sel_sb"))
  rt_bic <- rbind(oracle = tab("sel_bic_oracle"), uncorrected = tab("sel_bic_uncorr"),
                   corrected = tab("sel_bic_corrected"))
  miscl <- sapply(ok, `[[`, "sel_uncorr"); miscl <- miscl[miscl != TRUE_MODEL]
  W3C <- if (length(miscl) > 0) mean(miscl == "MD") else NA_real_
  W3A <- rt["corrected", TRUE_MODEL] - rt["uncorrected", TRUE_MODEL]
  W3B <- rt["oracle", TRUE_MODEL] - rt["corrected", TRUE_MODEL]
  miscl_bic <- sapply(ok, `[[`, "sel_bic_uncorr"); miscl_bic <- miscl_bic[miscl_bic != TRUE_MODEL]
  W3C_bic <- if (length(miscl_bic) > 0) mean(miscl_bic == "MD") else NA_real_
  W3A_bic <- rt_bic["corrected", TRUE_MODEL] - rt_bic["uncorrected", TRUE_MODEL]
  W3B_bic <- rt_bic["oracle", TRUE_MODEL] - rt_bic["corrected", TRUE_MODEL]
  saveRDS(list(cell = cell, R_per_cell = R_per_cell, elapsed_sec = elapsed,
               results = results, rates_table = rt, rates_table_bic = rt_bic),
          file = file.path(out_dir, sprintf("%s.rds", cell$id)))
  cat(sprintf("%5.1fs ok=%4d err=%2d  AIC W3A=%+.3f W3C=%.3f  BIC W3A=%+.3f W3C=%.3f  pi_bic[u/c/o]=%.3f/%.3f/%.3f\n",
              elapsed, length(ok), n_err, W3A, W3C, W3A_bic, W3C_bic,
              rt_bic["uncorrected", TRUE_MODEL], rt_bic["corrected", TRUE_MODEL],
              rt_bic["oracle", TRUE_MODEL]))
  rows[[i]] <- data.frame(
    cell_id = cell$id, pattern = cell$pattern, mech = cell$mech, N = cell$N,
    engine = cell$engine, M = cell$M, empri_frac = cell$empri_frac, prop = cell$prop,
    elapsed_sec = elapsed, n_ok = length(ok), n_err = n_err,
    pi_oracle = rt["oracle", TRUE_MODEL], pi_uncorrected = rt["uncorrected", TRUE_MODEL],
    pi_corrected = rt["corrected", TRUE_MODEL], pi_SB = rt["SB", TRUE_MODEL],
    W3A_corr_minus_uncorr = W3A, W3B_oracle_minus_corr = W3B,
    W3C_high_RIV_frac = W3C, W3C_n_miscl = length(miscl),
    pi_bic_oracle = rt_bic["oracle", TRUE_MODEL],
    pi_bic_uncorrected = rt_bic["uncorrected", TRUE_MODEL],
    pi_bic_corrected = rt_bic["corrected", TRUE_MODEL],
    W3A_bic_corr_minus_uncorr = W3A_bic, W3B_bic_oracle_minus_corr = W3B_bic,
    W3C_bic_high_RIV_frac = W3C_bic, W3C_bic_n_miscl = length(miscl_bic),
    stringsAsFactors = FALSE
  )
}
elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
cat(sprintf("\nsmallN-bic-probe elapsed: %.1fs (%.2f min)\n", elapsed_total, elapsed_total / 60))
df <- do.call(rbind, rows)
write.csv(df, file.path(out_dir, "summary.csv"), row.names = FALSE)
cat(sprintf("=== smallN-bic-probe complete ===\n"))
