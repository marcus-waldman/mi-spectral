# _modules/mnar-bias.R
#
# Phase 4 of run_all.R: direct parameter-bias measurement for theta_obs
# under MAR vs MNAR vs MNAR_targeted. Companion to the W3 sweep — answers
# "did our MNAR mechanism actually produce substantial bias?"
#
# 18 cells = 2 patterns x 3 mechs x 3 N. R per cell. FIML only (no MI).

PARAM_NAMES <- c(sprintf("mu_%d", 1:4),
                 "sigma_11", "sigma_21", "sigma_31", "sigma_41",
                 "sigma_22", "sigma_32", "sigma_42",
                 "sigma_33", "sigma_43", "sigma_44")

run_one_bias <- function(r, cell, mu0, Sigma_truth) {
  set.seed(20260522 + r)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma_truth)
  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop,
                                            mech = cell$mech,
                                            pattern_type = cell$pattern),
                  error = function(e) NULL)
  if (is.null(mar)) { return(list(error = "ampute")) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE),
                  error = function(e) NULL)
  if (is.null(fit)) { return(list(error = "FIML")) }
  v <- theta_to_vec(list(mu = fit$mu, Sigma = fit$Sigma))
  return(list(error = NA_character_, theta_obs_vec = v))
}

run_mnar_bias <- function(R_per_cell, cl, out_dir) {
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  cat(sprintf("\n== Phase 4: MNAR parameter bias (R=%d) ==\n\n", R_per_cell))
  Sigma_truth_w3 <- w3_sigma(rho = 0.4)
  theta_truth_vec <- theta_to_vec(list(mu = default_mu, Sigma = Sigma_truth_w3))

  cells <- list()
  cid <- 0
  for (pat in c("non_monotone", "monotone")) {
    for (mech in c("MAR", "MNAR", "MNAR_targeted")) {
      for (N in c(200, 500, 1000)) {
        cid <- cid + 1
        cells[[cid]] <- list(
          id = sprintf("%s_%s_N%d", pat, mech, N),
          pattern = pat, mech = mech, N = N, prop = 0.40
        )
      }
    }
  }
  cat(sprintf("Cells: %d\n", length(cells)))

  if (!is.null(cl)) {
    parallel::clusterExport(cl, varlist = c("run_one_bias",
                                            "Sigma_truth_w3",
                                            "theta_truth_vec", "PARAM_NAMES"),
                            envir = environment())
  }

  rows <- list()
  t_master <- Sys.time()
  for (i in seq_along(cells)) {
    cell <- cells[[i]]
    if (!is.null(cl)) {
      parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
    }
    cat(sprintf("[%2d/%2d] %-40s  ", i, length(cells), cell$id))
    t0 <- Sys.time()
    results <- if (is.null(cl)) {
      pbapply::pblapply(seq_len(R_per_cell), function(r) {
        return(run_one_bias(r, cell, default_mu, Sigma_truth_w3))
      })
    } else {
      pbapply::pblapply(seq_len(R_per_cell), function(r) {
        return(run_one_bias(r, cell, default_mu, Sigma_truth_w3))
      }, cl = cl)
    }
    elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
    errors <- sapply(results, function(rr) {
      return(!is.null(rr$error) && !is.na(rr$error))
    })
    ok <- results[!errors]; n_err <- sum(errors)
    if (length(ok) == 0) { cat("FAIL\n"); next }
    theta_obs_mat <- do.call(rbind, lapply(ok, `[[`, "theta_obs_vec"))
    bias_mean <- colMeans(theta_obs_mat) - theta_truth_vec
    sd_estimate <- apply(theta_obs_mat, 2, sd)
    bias_mcse <- sd_estimate / sqrt(nrow(theta_obs_mat))
    bias_z <- bias_mean / bias_mcse
    norm_bias <- sqrt(sum(bias_mean^2))
    rel_bias <- norm_bias / sqrt(sum(theta_truth_vec^2))
    bias_sigma_13 <- bias_mean[which(PARAM_NAMES == "sigma_31")]
    bias_sigma_24 <- bias_mean[which(PARAM_NAMES == "sigma_42")]
    saveRDS(list(cell = cell, R_per_cell = R_per_cell, elapsed_sec = elapsed,
                 theta_obs_mat = theta_obs_mat,
                 bias_mean = bias_mean, bias_mcse = bias_mcse,
                 bias_z = bias_z, PARAM_NAMES = PARAM_NAMES),
            file = file.path(out_dir, sprintf("%s.rds", cell$id)))
    cat(sprintf("%5.1fs ok=%4d  ||bias||=%.3f rel=%.4f  sig13=%+.4f (%+.1f%%)  sig24=%+.4f (%+.1f%%)\n",
                elapsed, nrow(theta_obs_mat),
                norm_bias, rel_bias,
                bias_sigma_13, 100 * bias_sigma_13 / 0.4,
                bias_sigma_24, 100 * bias_sigma_24 / 0.4))
    rows[[i]] <- data.frame(
      cell_id = cell$id, pattern = cell$pattern, mech = cell$mech, N = cell$N,
      n_ok = nrow(theta_obs_mat), n_err = n_err, elapsed_sec = elapsed,
      norm_bias = norm_bias, rel_bias = rel_bias,
      bias_sigma_13 = bias_sigma_13, bias_sigma_24 = bias_sigma_24,
      rel_sigma_13  = bias_sigma_13 / 0.4,
      rel_sigma_24  = bias_sigma_24 / 0.4,
      max_abs_bias_z = max(abs(bias_z)),
      stringsAsFactors = FALSE
    )
  }
  elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
  cat(sprintf("\nPhase 4 MNAR bias elapsed: %.1fs (%.2f min)\n",
              elapsed_total, elapsed_total / 60))
  df <- do.call(rbind, rows)
  write.csv(df, file.path(out_dir, "summary.csv"), row.names = FALSE)
  return(df)
}
