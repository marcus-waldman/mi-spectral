# _modules/w1-sweep.R
#
# Phase 1 of run_all.R: W1 (theorem validation) sweep — analytic FIML
# Q-function with analytic tr(RIV). 12 cells = 2 patterns x 3 mechanisms
# x 3 Ns. Per-replicate seed: set.seed(20260522 + r).
#
# (Note: MNAR_targeted included as a 3rd mech to mirror the W3 grid; see
# pilot-targeted-mnar conclusions — material difference vs MNAR is small,
# but inclusion is cheap and verifies the conclusion at R=2000.)

run_one_w1 <- function(r, cell, mu0, Sigma0) {
  set.seed(20260522 + r)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma0)
  theta_com <- mle_complete_mvn(X)
  ell_com_at_com <- loglik_mvn(theta_com, X)
  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop,
                                            mech = cell$mech,
                                            pattern_type = cell$pattern),
                  error = function(e) NULL)
  if (is.null(mar)) { return(list(error = "ampute")) }
  fit_obs <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE),
                      error = function(e) NULL)
  if (is.null(fit_obs)) { return(list(error = "FIML")) }
  theta_obs <- list(mu = fit_obs$mu, Sigma = fit_obs$Sigma)
  ell_com_at_obs <- loglik_mvn(theta_obs, X)
  barL_obs <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R)
  riv_info <- tr_riv_analytic(theta_obs, mar$Y, mar$R)
  return(list(
    error = NA_character_,
    T_r = barL_obs - ell_com_at_com,
    A_r = barL_obs - ell_com_at_obs,
    B_r = ell_com_at_obs - ell_com_at_com,
    trRIV_r = riv_info$tr_RIV
  ))
}

run_w1_sweep <- function(R_per_cell, cl, out_dir,
                          mechs = c("MAR", "MNAR", "MNAR_targeted")) {
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  cat(sprintf("\n== Phase 1: W1 sweep (R=%d, mechs={%s}) ==\n\n",
              R_per_cell, paste(mechs, collapse = ", ")))

  cells <- list()
  cid <- 0
  for (pat in c("non_monotone", "monotone")) {
    for (mech in mechs) {
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
    parallel::clusterExport(cl, varlist = c("run_one_w1"),
                            envir = environment())
  }

  rows <- list()
  t_master <- Sys.time()
  for (i in seq_along(cells)) {
    cell <- cells[[i]]
    cat(sprintf("[%d/%d] %-35s  ", i, length(cells), cell$id))
    if (!is.null(cl)) {
      parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
    }
    t0 <- Sys.time()
    results <- if (is.null(cl)) {
      pbapply::pblapply(seq_len(R_per_cell), function(r) {
        return(run_one_w1(r, cell, default_mu, default_Sigma))
      })
    } else {
      pbapply::pblapply(seq_len(R_per_cell), function(r) {
        return(run_one_w1(r, cell, default_mu, default_Sigma))
      }, cl = cl)
    }
    elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
    errors <- sapply(results, function(rr) {
      return(!is.null(rr$error) && !is.na(rr$error))
    })
    ok <- results[!errors]; n_err <- sum(errors)
    if (length(ok) == 0) {
      cat(sprintf("FAIL (%d errors)\n", n_err)); next
    }
    T_arr     <- vapply(ok, `[[`, numeric(1), "T_r")
    A_arr     <- vapply(ok, `[[`, numeric(1), "A_r")
    B_arr     <- vapply(ok, `[[`, numeric(1), "B_r")
    trRIV_arr <- vapply(ok, `[[`, numeric(1), "trRIV_r")
    T_hat <- mean(T_arr); A_hat <- mean(A_arr); B_hat <- mean(B_arr)
    trRIV_emp <- mean(trRIV_arr); half <- 0.5 * trRIV_emp
    mcse <- function(x) sd(x) / sqrt(length(x))
    ci_T <- T_hat + qnorm(c(0.025, 0.975)) * mcse(T_arr)
    passT <- ci_T[1] <= half && half <= ci_T[2]
    saveRDS(list(cell = cell, elapsed_sec = elapsed,
                 T_arr = T_arr, A_arr = A_arr, B_arr = B_arr,
                 trRIV_arr = trRIV_arr,
                 summary = list(T_hat = T_hat, A_hat = A_hat, B_hat = B_hat,
                                trRIV_emp = trRIV_emp,
                                half_trRIV_pred = half,
                                pass = c(T = passT))),
            file = file.path(out_dir, sprintf("%s.rds", cell$id)))
    cat(sprintf("%5.1fs  T=%+6.3f (pred %+6.3f)  trRIV=%5.3f  T:%s\n",
                elapsed, T_hat, half, trRIV_emp,
                if (passT) "PASS" else "FAIL"))
    rows[[i]] <- data.frame(
      cell_id = cell$id, pattern = cell$pattern, mech = cell$mech,
      N = cell$N, n_ok = length(ok), n_err = n_err,
      T_hat = T_hat, A_hat = A_hat, B_hat = B_hat, trRIV = trRIV_emp,
      half_trRIV_pred = half, passT = passT,
      stringsAsFactors = FALSE
    )
  }
  elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
  cat(sprintf("\nPhase 1 W1 sweep elapsed: %.1fs (%.2f min)\n",
              elapsed_total, elapsed_total / 60))
  df <- do.call(rbind, rows)
  write.csv(df, file.path(out_dir, "summary.csv"), row.names = FALSE)
  return(df)
}
