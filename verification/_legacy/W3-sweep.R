# W3-sweep.R
#
# Comprehensive 60-cell W3 sweep (todo/005 §0.6, todo/006 Steps 5-8).
#
# 60 main cells = 2 patterns x 2 mechanisms x 3 Ns x 5 engine/M/cong
# combinations, with the constraint that FIML is M-independent and
# congeniality-independent (so the 5-th slot is effectively 1 FIML + 4
# Amelia variants -> 12 FIML cells + 48 Amelia cells = 60).
#
# Each cell runs R replicates of the W3 model-selection pipeline using
# the new apply_missingness_ampute mechanism. Per-cell cache files are
# written to verification/cache/W3-sweep-<out_suffix>/<cell-id>.rds and a
# summary CSV is written at the top of the directory.
#
# Usage:
#   Rscript verification/W3-sweep.R <R> <out_suffix> [engine_filter] [n_cores]
#
# Examples:
#   Rscript verification/W3-sweep.R 100 sanity              # full R=100 sanity sweep
#   Rscript verification/W3-sweep.R 2000 prod               # full R=2000 production
#   Rscript verification/W3-sweep.R 2000 prod fiml          # only FIML cells
#   Rscript verification/W3-sweep.R 2000 prod amelia 20     # only Amelia cells, 20 cores
#
# engine_filter values: "all" (default), "fiml", "amelia",
#                       "amelia20" (M=20 only), "amelia200" (M=200 only),
#                       "amelia20cong", "amelia200cong", "amelia20uncong",
#                       "amelia200uncong".

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args <- commandArgs(trailingOnly = TRUE)
R_per_cell <- if (length(args) >= 1) { as.integer(args[1]) } else { 100 }
out_suffix <- if (length(args) >= 2) { args[2] } else { "sanity" }
engine_flt <- if (length(args) >= 3) { args[3] } else { "all" }
n_cores    <- if (length(args) >= 4) { as.integer(args[4]) } else { 20 }

stopifnot(R_per_cell > 0)
out_dir <- sprintf("verification/cache/W3-sweep-%s", out_suffix)
if (!dir.exists(out_dir)) { dir.create(out_dir, recursive = TRUE) }

cat(sprintf("\nW3 sweep  [R=%d, out=%s, filter=%s, cores=%d]\n\n",
            R_per_cell, out_suffix, engine_flt, n_cores))

W3_MODEL_NAMES <- c("MA", "MB", "MC", "MD")
TRUE_MODEL <- "MC"
Sigma_truth_w3 <- w3_sigma(rho = 0.4)


# -----------------------------------------------------------------------------
# Build the 60-cell grid.
# -----------------------------------------------------------------------------

build_cells <- function() {
  patterns <- c("non_monotone", "monotone")
  mechs    <- c("MAR", "MNAR")
  Ns       <- c(200, 500, 1000)
  cells <- list()
  cid <- 0
  # FIML cells (M and cong irrelevant).
  for (pat in patterns) for (mech in mechs) for (N in Ns) {
    cid <- cid + 1
    cells[[cid]] <- list(
      id          = sprintf("fiml_%s_%s_N%d", pat, mech, N),
      pattern     = pat,
      mech        = mech,
      N           = N,
      engine      = "fiml",
      M           = NA_integer_,
      empri_frac  = 0,
      prop        = 0.40,
      tag_engine  = "fiml"
    )
  }
  # Amelia cells.
  for (pat in patterns) for (mech in mechs) for (N in Ns) {
    for (M in c(20, 200)) {
      for (empri_frac in c(0, 0.5)) {
        cong_tag <- if (empri_frac == 0) { "cong" } else { "uncong" }
        cid <- cid + 1
        cells[[cid]] <- list(
          id          = sprintf("amelia_%s_%s_N%d_M%d_%s", pat, mech, N, M, cong_tag),
          pattern     = pat,
          mech        = mech,
          N           = N,
          engine      = "amelia",
          M           = M,
          empri_frac  = empri_frac,
          prop        = 0.40,
          tag_engine  = sprintf("amelia%d%s", M, cong_tag)
        )
      }
    }
  }
  return(cells)
}

apply_engine_filter <- function(cells, flt) {
  if (flt == "all") { return(cells) }
  keep <- vapply(cells, function(cl) {
    if (flt == "fiml")             { return(cl$engine == "fiml") }
    if (flt == "amelia")           { return(cl$engine == "amelia") }
    if (flt == "amelia20")         { return(cl$engine == "amelia" && cl$M == 20) }
    if (flt == "amelia200")        { return(cl$engine == "amelia" && cl$M == 200) }
    if (flt == "amelia20cong")     { return(cl$engine == "amelia" && cl$M == 20  && cl$empri_frac == 0) }
    if (flt == "amelia200cong")    { return(cl$engine == "amelia" && cl$M == 200 && cl$empri_frac == 0) }
    if (flt == "amelia20uncong")   { return(cl$engine == "amelia" && cl$M == 20  && cl$empri_frac == 0.5) }
    if (flt == "amelia200uncong")  { return(cl$engine == "amelia" && cl$M == 200 && cl$empri_frac == 0.5) }
    return(FALSE)
  }, logical(1))
  return(cells[keep])
}

cells <- build_cells()
stopifnot(length(cells) == 60)
cells <- apply_engine_filter(cells, engine_flt)
cat(sprintf("Cells after filter '%s': %d (of 60 total)\n", engine_flt, length(cells)))


# -----------------------------------------------------------------------------
# Per-replicate work (sweep version using apply_missingness_ampute).
# -----------------------------------------------------------------------------

run_one_replicate_sweep <- function(r, cell, mu0, Sigma_truth) {
  set.seed(20260522 + r)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma_truth)

  # --- Complete-data MLE per candidate ---
  ell_com <- numeric(4); names(ell_com) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    fit_k <- tryCatch(lavaan_fit_mvn_model(X, W3_MODELS[[k]]),
                      error = function(e) { return(NULL) })
    if (is.null(fit_k)) {
      return(list(error = sprintf("complete-data fit failed for %s", k),
                  miss1 = NA, miss2 = NA, miss3 = NA, miss4 = NA))
    }
    ell_com[k] <- fit_k$logLik
  }

  # --- Apply missingness via ampute wrapper ---
  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop,
                                           mech = cell$mech,
                                           pattern_type = cell$pattern),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) {
    return(list(error = "ampute failed",
                miss1 = NA, miss2 = NA, miss3 = NA, miss4 = NA))
  }

  # --- Observed-data FIML MLE per candidate ---
  theta_obs_list <- list()
  for (k in W3_MODEL_NAMES) {
    fit_k <- tryCatch(lavaan_fit_mvn_fiml_model(mar$Y, W3_MODELS[[k]]),
                      error = function(e) { return(NULL) })
    if (is.null(fit_k)) {
      return(list(error = sprintf("FIML fit failed for %s", k),
                  miss1 = mean(mar$R[,1]), miss2 = mean(mar$R[,2]),
                  miss3 = mean(mar$R[,3]), miss4 = mean(mar$R[,4])))
    }
    theta_obs_list[[k]] <- list(mu = fit_k$mu, Sigma = fit_k$Sigma,
                                logLik_obs = fit_k$logLik)
  }
  theta_D_obs <- theta_obs_list[["MD"]]

  # --- bar L_M per candidate (engine-dependent) ---
  barL <- numeric(4); names(barL) <- W3_MODEL_NAMES
  if (cell$engine == "fiml") {
    for (k in W3_MODEL_NAMES) {
      theta_k <- list(mu = theta_obs_list[[k]]$mu,
                      Sigma = theta_obs_list[[k]]$Sigma)
      barL[k] <- barQ_fiml_analytic(theta_k, theta_D_obs, mar$Y, mar$R)
    }
  } else {  # amelia
    empri_actual <- cell$empri_frac * cell$N
    imps <- tryCatch(impute_mvn_amelia(mar$Y, M = cell$M, empri = empri_actual),
                     error = function(e) { return(NULL) })
    if (is.null(imps)) {
      return(list(error = "amelia imputation failed",
                  miss1 = mean(mar$R[,1]), miss2 = mean(mar$R[,2]),
                  miss3 = mean(mar$R[,3]), miss4 = mean(mar$R[,4])))
    }
    for (k in W3_MODEL_NAMES) {
      theta_k <- list(mu = theta_obs_list[[k]]$mu,
                      Sigma = theta_obs_list[[k]]$Sigma)
      barL[k] <- mean(sapply(imps, function(Z) {
        return(loglik_mvn(theta_k, Z))
      }))
    }
  }

  # --- tr(RIV) + sum_lambda_sq per candidate (analytic) ---
  trRIV         <- numeric(4); names(trRIV)         <- W3_MODEL_NAMES
  sum_lambda_sq <- numeric(4); names(sum_lambda_sq) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    theta_k <- list(mu = theta_obs_list[[k]]$mu,
                    Sigma = theta_obs_list[[k]]$Sigma)
    sp <- riv_spectrum_analytic_general(theta_k, mar$Y, mar$R, W3_FREE_IDX[[k]])
    trRIV[k]         <- sp$tr_RIV
    sum_lambda_sq[k] <- sp$sum_lambda_sq
  }

  # --- SB-corrected differential deviance against M_D ---
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
    ell_com       = ell_com,
    barL          = barL,
    trRIV         = trRIV,
    sum_lambda_sq = sum_lambda_sq,
    miss1         = mean(mar$R[, 1]),
    miss2         = mean(mar$R[, 2]),
    miss3         = mean(mar$R[, 3]),
    miss4         = mean(mar$R[, 4])
  ))
}


# -----------------------------------------------------------------------------
# Per-cell driver: run R_per_cell replicates and cache.
# -----------------------------------------------------------------------------

run_cell <- function(cell, R_per_cell, cl) {
  t0 <- Sys.time()
  if (is.null(cl)) {
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_replicate_sweep(r, cell, default_mu, Sigma_truth_w3))
    })
  } else {
    parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_replicate_sweep(r, cell, default_mu, Sigma_truth_w3))
    }, cl = cl)
  }
  elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))

  # Aggregate selection rates.
  errors <- sapply(results, function(rr) { return(!is.na(rr$error)) })
  n_err <- sum(errors)
  ok    <- results[!errors]
  if (length(ok) == 0) {
    rates_table <- matrix(NA_real_, 4, 4,
      dimnames = list(c("oracle","uncorrected","corrected","SB"),
                      W3_MODEL_NAMES))
    selection_summary <- list(n_ok = 0, n_err = n_err)
  } else {
    tab <- function(field) {
      sels <- sapply(ok, `[[`, field)
      out <- sapply(W3_MODEL_NAMES, function(k) { mean(sels == k) })
      names(out) <- W3_MODEL_NAMES
      return(out)
    }
    rates_table <- rbind(
      oracle      = tab("sel_oracle"),
      uncorrected = tab("sel_uncorr"),
      corrected   = tab("sel_corrected"),
      SB          = tab("sel_sb")
    )
    selection_summary <- list(n_ok = length(ok), n_err = n_err)
  }

  cache_path <- file.path(out_dir, sprintf("%s.rds", cell$id))
  saveRDS(list(
    cell = cell, R_per_cell = R_per_cell, elapsed_sec = elapsed,
    results = results, rates_table = rates_table,
    selection_summary = selection_summary
  ), file = cache_path)

  return(list(elapsed = elapsed, n_err = n_err, n_ok = length(ok),
              rates_table = rates_table, cache_path = cache_path))
}


# -----------------------------------------------------------------------------
# Cluster setup.
# -----------------------------------------------------------------------------

cluster_active <- (n_cores > 1)
if (cluster_active) {
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
# Main loop: iterate cells, accumulate summary table.
# -----------------------------------------------------------------------------

summary_rows <- list()
t_master <- Sys.time()

for (i in seq_along(cells)) {
  cell <- cells[[i]]
  cat(sprintf("[%d/%d] %s   ", i, length(cells), cell$id))
  out <- run_cell(cell, R_per_cell, cl)
  cat(sprintf("done in %5.1fs   (n_ok=%d / n_err=%d)\n",
              out$elapsed, out$n_ok, out$n_err))
  rt <- out$rates_table
  row <- data.frame(
    cell_id     = cell$id,
    pattern     = cell$pattern,
    mech        = cell$mech,
    N           = cell$N,
    engine      = cell$engine,
    M           = cell$M,
    empri_frac  = cell$empri_frac,
    prop        = cell$prop,
    elapsed_sec = out$elapsed,
    n_ok        = out$n_ok,
    n_err       = out$n_err,
    pi_oracle      = if (all(is.na(rt))) NA else rt["oracle", TRUE_MODEL],
    pi_uncorrected = if (all(is.na(rt))) NA else rt["uncorrected", TRUE_MODEL],
    pi_corrected   = if (all(is.na(rt))) NA else rt["corrected", TRUE_MODEL],
    pi_SB          = if (all(is.na(rt))) NA else rt["SB", TRUE_MODEL],
    stringsAsFactors = FALSE
  )
  row$W3A_corr_minus_uncorr <- row$pi_corrected - row$pi_uncorrected
  row$W3B_oracle_minus_corr <- row$pi_oracle    - row$pi_corrected
  # W3-C: fraction of uncorrected misclassifications on the high-RIV
  # candidate(s). For all sweep cells we use the same definition as the
  # preregistered prod: among uncorrected != TRUE_MODEL replicates, what
  # fraction land on M_D (max-RIV by construction).
  if (out$n_ok > 0) {
    results_ok <- readRDS(out$cache_path)$results
    results_ok <- results_ok[!sapply(results_ok, function(rr) !is.na(rr$error))]
    miscl_sel <- sapply(results_ok, function(rr) { return(rr$sel_uncorr) })
    miscl_sel <- miscl_sel[miscl_sel != TRUE_MODEL]
    if (length(miscl_sel) > 0) {
      row$W3C_high_RIV_frac <- mean(miscl_sel == "MD")
      row$W3C_n_miscl       <- length(miscl_sel)
    } else {
      row$W3C_high_RIV_frac <- NA_real_
      row$W3C_n_miscl       <- 0
    }
  } else {
    row$W3C_high_RIV_frac <- NA_real_
    row$W3C_n_miscl       <- 0
  }
  summary_rows[[length(summary_rows) + 1]] <- row
}

elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
cat(sprintf("\nTotal sweep elapsed: %.1fs (%.2f min)\n",
            elapsed_total, elapsed_total / 60))


# -----------------------------------------------------------------------------
# Write summary CSV at the top of the output directory.
# -----------------------------------------------------------------------------

summary_df <- do.call(rbind, summary_rows)
summary_path <- file.path(out_dir, "summary.csv")
write.csv(summary_df, file = summary_path, row.names = FALSE)
cat(sprintf("\nSummary CSV: %s\n", summary_path))

cat("\nPer-cell W3 selection rates (top of TRUE-model column):\n\n")
print(summary_df[, c("cell_id", "n_ok", "n_err",
                     "pi_oracle", "pi_uncorrected", "pi_corrected", "pi_SB",
                     "W3A_corr_minus_uncorr", "W3C_high_RIV_frac")],
      row.names = FALSE, digits = 3)

cat("\nDone.\n")
