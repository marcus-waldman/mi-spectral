# W3-sweep-rate.R
#
# H3b rate side experiment (todo/005 §H3b, todo/006 §9).
#
# 6 cells: 3 (N in {200, 500, 1000}) x 2 (rate in {0.20, 0.60}) at fixed
# (MAR, non_monotone, M=200, congenial Amelia). R=2000 per cell.
#
# Tests H3b's predictions:
#  - W3-A monotone in rate (corrected - uncorrected gap grows with rate).
#  - W3-A approximately N-invariant at each rate.
#  - W3-A(rate=0.60) / W3-A(rate=0.20) approximately 3.

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args       <- commandArgs(trailingOnly = TRUE)
R_per_cell <- if (length(args) >= 1) { as.integer(args[1]) } else { 2000 }
out_suffix <- if (length(args) >= 2) { args[2] } else { "prod" }
n_cores    <- if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

out_dir <- sprintf("verification/cache/W3-sweep-rate-%s", out_suffix)
if (!dir.exists(out_dir)) { dir.create(out_dir, recursive = TRUE) }

cat(sprintf("\nW3 rate sweep  [R=%d, out=%s, cores=%d]\n\n",
            R_per_cell, out_suffix, n_cores))

W3_MODEL_NAMES <- c("MA", "MB", "MC", "MD")
TRUE_MODEL <- "MC"
Sigma_truth_w3 <- w3_sigma(rho = 0.4)


# -----------------------------------------------------------------------------
# 6-cell grid: 3 Ns x 2 rates, all Amelia M=200 congenial, MAR + non_monotone.
# -----------------------------------------------------------------------------

build_rate_cells <- function() {
  Ns    <- c(200, 500, 1000)
  # Preregistered H3b grid was rate in {0.20, 0.60}. The rate=0.60 cells
  # encountered Amelia bootstrap chol() failures at high rate (90%
  # incomplete cases under non_monotone), which bypass R-level tryCatch
  # and kill the PSOCK worker. After discussion 2026-05-23 the user chose
  # to defer rate=0.60 to a follow-up rather than amend the preregistration
  # with an empri stability prior. H3b therefore runs as a "low-rate arm
  # only" preliminary, paired with the existing 40% data from the main W3
  # sweep to give us 2 rate points (20% and 40%) for monotone-in-rate
  # testing; H3b's "ratio approx 3" criterion is treated as observational.
  rates <- c(0.20)
  out <- list()
  cid <- 0
  for (N in Ns) for (rate in rates) {
    cid <- cid + 1
    out[[cid]] <- list(
      id      = sprintf("amelia_non_monotone_MAR_N%d_M200_cong_rate%d",
                        N, as.integer(100 * rate)),
      pattern    = "non_monotone",
      mech       = "MAR",
      N          = N,
      engine     = "amelia",
      M          = 200,
      empri_frac = 0,
      prop       = rate
    )
  }
  return(out)
}

cells <- build_rate_cells()
cat(sprintf("Cells: %d (all Amelia M=200 congenial, MAR + non_monotone)\n",
            length(cells)))


# -----------------------------------------------------------------------------
# Per-replicate work (identical to W3-sweep.R but rate is per-cell).
# -----------------------------------------------------------------------------

run_one_replicate_sweep <- function(r, cell, mu0, Sigma_truth) {
  set.seed(20260522 + r)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma_truth)

  ell_com <- numeric(4); names(ell_com) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    fit_k <- tryCatch(lavaan_fit_mvn_model(X, W3_MODELS[[k]]),
                      error = function(e) { return(NULL) })
    if (is.null(fit_k)) { return(list(error = "complete-fit failed")) }
    ell_com[k] <- fit_k$logLik
  }

  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop,
                                            mech = cell$mech,
                                            pattern_type = cell$pattern),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(list(error = "ampute failed")) }

  theta_obs_list <- list()
  for (k in W3_MODEL_NAMES) {
    fit_k <- tryCatch(lavaan_fit_mvn_fiml_model(mar$Y, W3_MODELS[[k]]),
                      error = function(e) { return(NULL) })
    if (is.null(fit_k)) { return(list(error = sprintf("FIML fit failed for %s", k))) }
    theta_obs_list[[k]] <- list(mu = fit_k$mu, Sigma = fit_k$Sigma)
  }

  empri_actual <- cell$empri_frac * cell$N
  imps <- tryCatch(impute_mvn_amelia(mar$Y, M = cell$M, empri = empri_actual),
                   error = function(e) { return(NULL) })
  if (is.null(imps)) { return(list(error = "amelia imputation failed")) }

  barL <- numeric(4); names(barL) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    theta_k <- list(mu = theta_obs_list[[k]]$mu,
                    Sigma = theta_obs_list[[k]]$Sigma)
    barL[k] <- mean(sapply(imps, function(Z) {
      return(loglik_mvn(theta_k, Z))
    }))
  }

  trRIV         <- numeric(4); names(trRIV)         <- W3_MODEL_NAMES
  sum_lambda_sq <- numeric(4); names(sum_lambda_sq) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    theta_k <- list(mu = theta_obs_list[[k]]$mu,
                    Sigma = theta_obs_list[[k]]$Sigma)
    sp <- riv_spectrum_analytic_general(theta_k, mar$Y, mar$R, W3_FREE_IDX[[k]])
    trRIV[k]         <- sp$tr_RIV
    sum_lambda_sq[k] <- sp$sum_lambda_sq
  }

  chi2_MI_per_k <- 2 * (barL["MD"] - barL)
  trRIV_D       <- trRIV["MD"]
  sum_lsq_D     <- sum_lambda_sq["MD"]
  chi2_SB       <- numeric(4); names(chi2_SB) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    if (k == "MD") { chi2_SB[k] <- 0; next }
    df_k          <- W3_NPAR["MD"] - W3_NPAR[k]
    tr_perp_k     <- trRIV_D - trRIV[k]
    sum_lsq_perp  <- max(sum_lsq_D - sum_lambda_sq[k], 0)
    var_target    <- 2 * df_k
    var_predicted <- var_target + 4 * tr_perp_k + 2 * sum_lsq_perp
    if (var_predicted <= 0) {
      chi2_SB[k] <- chi2_MI_per_k[k]
    } else {
      a_k <- sqrt(var_target / var_predicted)
      b_k <- df_k * (1 - a_k)
      chi2_SB[k] <- a_k * chi2_MI_per_k[k] + b_k
    }
  }

  AIC_oracle    <- -2 * ell_com + 2 * W3_NPAR
  AIC_uncorr    <- -2 * barL    + 2 * W3_NPAR
  AIC_corrected <- -2 * barL    + 2 * W3_NPAR + trRIV
  AIC_sb        <- chi2_SB      + 2 * W3_NPAR

  return(list(
    error         = NA_character_,
    sel_oracle    = names(which.min(AIC_oracle)),
    sel_uncorr    = names(which.min(AIC_uncorr)),
    sel_corrected = names(which.min(AIC_corrected)),
    sel_sb        = names(which.min(AIC_sb)),
    trRIV         = trRIV,
    miss          = colMeans(mar$R)
  ))
}


# -----------------------------------------------------------------------------
# Cluster setup.
# -----------------------------------------------------------------------------

if (n_cores > 1) {
  cl <- parallel::makeCluster(n_cores)
  on.exit(parallel::stopCluster(cl), add = TRUE)
  parallel::clusterEvalQ(cl, { invisible(source("verification/00-setup.R")) })
  parallel::clusterExport(cl, varlist = c("run_one_replicate_sweep",
                                          "Sigma_truth_w3",
                                          "W3_MODEL_NAMES"))
} else {
  cl <- NULL
}


# -----------------------------------------------------------------------------
# Main loop.
# -----------------------------------------------------------------------------

summary_rows <- list()
t_master <- Sys.time()

for (i in seq_along(cells)) {
  cell <- cells[[i]]
  cache_existing <- file.path(out_dir, sprintf("%s.rds", cell$id))
  if (file.exists(cache_existing)) {
    cat(sprintf("[%d/%d] %s  (cached, skipping)\n",
                i, length(cells), cell$id))
    cached <- readRDS(cache_existing)
    ok <- cached$results
    ok <- ok[!sapply(ok, function(rr) !is.null(rr$error) && !is.na(rr$error))]
    rt <- cached$rates_table
    miscl_sel <- sapply(ok, `[[`, "sel_uncorr")
    miscl_sel <- miscl_sel[miscl_sel != TRUE_MODEL]
    W3C <- if (length(miscl_sel) > 0) mean(miscl_sel == "MD") else NA_real_
    W3A <- rt["corrected", TRUE_MODEL] - rt["uncorrected", TRUE_MODEL]
    W3B <- rt["oracle", TRUE_MODEL] - rt["corrected", TRUE_MODEL]
    summary_rows[[i]] <- data.frame(
      cell_id = cell$id, pattern = cell$pattern, mech = cell$mech,
      N = cell$N, M = cell$M, empri_frac = cell$empri_frac,
      prop = cell$prop, elapsed_sec = cached$elapsed_sec,
      n_ok = length(ok), n_err = length(cached$results) - length(ok),
      pi_oracle = rt["oracle", TRUE_MODEL],
      pi_uncorrected = rt["uncorrected", TRUE_MODEL],
      pi_corrected   = rt["corrected", TRUE_MODEL],
      pi_SB          = rt["SB", TRUE_MODEL],
      W3A = W3A, W3B = W3B, W3C = W3C, W3C_n_miscl = length(miscl_sel),
      stringsAsFactors = FALSE
    )
    next
  }
  cat(sprintf("[%d/%d] %s  ", i, length(cells), cell$id))
  if (!is.null(cl)) {
    parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
  }
  t0 <- Sys.time()
  if (is.null(cl)) {
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_replicate_sweep(r, cell, default_mu, Sigma_truth_w3))
    })
  } else {
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_replicate_sweep(r, cell, default_mu, Sigma_truth_w3))
    }, cl = cl)
  }
  elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))

  errors <- sapply(results, function(rr) { return(!is.null(rr$error) && !is.na(rr$error)) })
  ok <- results[!errors]; n_err <- sum(errors)

  tab <- function(field) {
    sels <- sapply(ok, `[[`, field)
    out <- sapply(W3_MODEL_NAMES, function(k) { mean(sels == k) })
    names(out) <- W3_MODEL_NAMES
    return(out)
  }
  rt <- if (length(ok) > 0) {
    rbind(oracle = tab("sel_oracle"),
          uncorrected = tab("sel_uncorr"),
          corrected = tab("sel_corrected"),
          SB = tab("sel_sb"))
  } else {
    matrix(NA, 4, 4, dimnames = list(c("oracle","uncorrected","corrected","SB"),
                                     W3_MODEL_NAMES))
  }

  cache_path <- file.path(out_dir, sprintf("%s.rds", cell$id))
  saveRDS(list(cell = cell, R_per_cell = R_per_cell, elapsed_sec = elapsed,
               results = results, rates_table = rt),
          file = cache_path)

  miscl_sel <- sapply(ok, `[[`, "sel_uncorr")
  miscl_sel <- miscl_sel[miscl_sel != TRUE_MODEL]
  W3C <- if (length(miscl_sel) > 0) mean(miscl_sel == "MD") else NA_real_

  W3A <- rt["corrected", TRUE_MODEL] - rt["uncorrected", TRUE_MODEL]
  W3B <- rt["oracle", TRUE_MODEL] - rt["corrected", TRUE_MODEL]

  cat(sprintf("done %5.1fs  n_ok=%d n_err=%d  W3A=%+.3f W3B=%+.3f W3C=%.3f\n",
              elapsed, length(ok), n_err, W3A, W3B, W3C))

  summary_rows[[i]] <- data.frame(
    cell_id = cell$id, pattern = cell$pattern, mech = cell$mech,
    N = cell$N, M = cell$M, empri_frac = cell$empri_frac,
    prop = cell$prop, elapsed_sec = elapsed,
    n_ok = length(ok), n_err = n_err,
    pi_oracle      = rt["oracle",      TRUE_MODEL],
    pi_uncorrected = rt["uncorrected", TRUE_MODEL],
    pi_corrected   = rt["corrected",   TRUE_MODEL],
    pi_SB          = rt["SB",          TRUE_MODEL],
    W3A = W3A, W3B = W3B, W3C = W3C,
    W3C_n_miscl = length(miscl_sel),
    stringsAsFactors = FALSE
  )
}

elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
cat(sprintf("\nTotal rate sweep elapsed: %.1fs (%.2f min)\n",
            elapsed_total, elapsed_total / 60))

summary_df <- do.call(rbind, summary_rows)
summary_path <- file.path(out_dir, "summary.csv")
write.csv(summary_df, file = summary_path, row.names = FALSE)
cat(sprintf("\nSummary: %s\n\n", summary_path))

print(summary_df[, c("cell_id", "prop", "N", "n_ok",
                     "pi_oracle", "pi_uncorrected", "pi_corrected",
                     "W3A", "W3C")],
      row.names = FALSE, digits = 3)
