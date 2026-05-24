# _modules/w3-rate.R
#
# Phase 3 of run_all.R: H3b rate side experiment, low-rate arm only.
#
# 3 cells: N in {200, 500, 1000} at rate=0.20, MAR + non_monotone, M=200,
# congenial Amelia. The rate=0.60 cells from the original preregistration
# (todo/005 §H3b) were deferred due to Amelia bootstrap chol() failures
# at 90% incomplete-case prevalence — see todo/005 version history.
#
# Combined with the rate=0.40 cells from the main W3 sweep (MAR +
# non_monotone + M=200 + congenial Amelia), this gives 2 rate points
# (20%, 40%) at each N for partial monotone-in-rate testing.

run_w3_rate <- function(R_per_cell, cl, out_dir) {
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  cat(sprintf("\n== Phase 3: H3b rate experiment (R=%d) ==\n\n", R_per_cell))
  Sigma_truth_w3 <- w3_sigma(rho = 0.4)

  cells <- lapply(c(200, 500, 1000), function(N) {
    list(id = sprintf("amelia_non_monotone_MAR_N%d_M200_cong_rate20", N),
         pattern = "non_monotone", mech = "MAR", N = N,
         engine = "amelia", M = 200, empri_frac = 0, prop = 0.20)
  })
  cat(sprintf("Cells: %d\n", length(cells)))

  if (!is.null(cl)) {
    parallel::clusterExport(cl, varlist = c("run_one_w3",
                                            "W3_MODEL_NAMES",
                                            "TRUE_MODEL",
                                            "Sigma_truth_w3"),
                            envir = environment())
  }

  rows <- list()
  t_master <- Sys.time()
  for (i in seq_along(cells)) {
    cell <- cells[[i]]
    cache_path <- file.path(out_dir, sprintf("%s.rds", cell$id))
    if (file.exists(cache_path)) {
      cat(sprintf("[%d/%d] %s  (cached, skipping)\n",
                  i, length(cells), cell$id))
      cached <- readRDS(cache_path)
      ok <- cached$results
      ok <- ok[!sapply(ok, function(rr) !is.null(rr$error) && !is.na(rr$error))]
      rt <- cached$rates_table
      miscl <- sapply(ok, `[[`, "sel_uncorr")
      miscl <- miscl[miscl != TRUE_MODEL]
      W3C <- if (length(miscl) > 0) mean(miscl == "MD") else NA_real_
      W3A <- rt["corrected", TRUE_MODEL] - rt["uncorrected", TRUE_MODEL]
      W3B <- rt["oracle", TRUE_MODEL] - rt["corrected", TRUE_MODEL]
      rows[[i]] <- data.frame(
        cell_id = cell$id, pattern = cell$pattern, mech = cell$mech,
        N = cell$N, M = cell$M, empri_frac = cell$empri_frac,
        prop = cell$prop, elapsed_sec = cached$elapsed_sec,
        n_ok = length(ok), n_err = length(cached$results) - length(ok),
        pi_oracle = rt["oracle", TRUE_MODEL],
        pi_uncorrected = rt["uncorrected", TRUE_MODEL],
        pi_corrected = rt["corrected", TRUE_MODEL],
        pi_SB = rt["SB", TRUE_MODEL],
        W3A = W3A, W3B = W3B, W3C = W3C, W3C_n_miscl = length(miscl),
        stringsAsFactors = FALSE
      )
      next
    }
    if (!is.null(cl)) {
      parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
    }
    cat(sprintf("[%d/%d] %s  ", i, length(cells), cell$id))
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
    errors <- sapply(results, function(rr) {
      return(!is.null(rr$error) && !is.na(rr$error))
    })
    ok <- results[!errors]; n_err <- sum(errors)
    tab <- function(field) {
      sels <- sapply(ok, `[[`, field)
      return(sapply(W3_MODEL_NAMES, function(k) mean(sels == k)))
    }
    rt <- rbind(oracle = tab("sel_oracle"),
                uncorrected = tab("sel_uncorr"),
                corrected = tab("sel_corrected"),
                SB = tab("sel_sb"))
    saveRDS(list(cell = cell, R_per_cell = R_per_cell, elapsed_sec = elapsed,
                 results = results, rates_table = rt),
            file = cache_path)
    miscl <- sapply(ok, `[[`, "sel_uncorr")
    miscl <- miscl[miscl != TRUE_MODEL]
    W3C <- if (length(miscl) > 0) mean(miscl == "MD") else NA_real_
    W3A <- rt["corrected", TRUE_MODEL] - rt["uncorrected", TRUE_MODEL]
    W3B <- rt["oracle", TRUE_MODEL] - rt["corrected", TRUE_MODEL]
    cat(sprintf("%5.1fs ok=%4d err=%2d  W3A=%+.3f W3C=%.3f\n",
                elapsed, length(ok), n_err, W3A, W3C))
    rows[[i]] <- data.frame(
      cell_id = cell$id, pattern = cell$pattern, mech = cell$mech,
      N = cell$N, M = cell$M, empri_frac = cell$empri_frac,
      prop = cell$prop, elapsed_sec = elapsed,
      n_ok = length(ok), n_err = n_err,
      pi_oracle = rt["oracle", TRUE_MODEL],
      pi_uncorrected = rt["uncorrected", TRUE_MODEL],
      pi_corrected = rt["corrected", TRUE_MODEL],
      pi_SB = rt["SB", TRUE_MODEL],
      W3A = W3A, W3B = W3B, W3C = W3C, W3C_n_miscl = length(miscl),
      stringsAsFactors = FALSE
    )
  }
  elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
  cat(sprintf("\nPhase 3 H3b elapsed: %.1fs\n", elapsed_total))
  df <- do.call(rbind, rows)
  write.csv(df, file.path(out_dir, "summary.csv"), row.names = FALSE)
  return(df)
}
