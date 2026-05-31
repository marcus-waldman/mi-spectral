# _modules/w1-information-diagnostic.R
#
# Phase 6 of run_all.R: finite-sample expected-vs-sample RIV diagnostic.
#
# Consolidates the exploratory scratch diagnostics (2026-05-30/31) into the
# reproducible battery. Establishes, per cell:
#   - A (imputation bias) tracks the EXPECTED-information RIV  tr(I_obs^-1 I_mis);
#   - B (estimation mismatch) tracks the SAMPLE / observed RIV (Rubin between/
#     within), which finite-sample exceeds the expected one (Efron-Hinkley);
#   - information equality tr(J_hat I_obs^-1) ~ k holds (correct specification),
#     so the split is the finite-sample (E-H) face of the J-vs-I distinction,
#     NOT the misspecification (TIC) face;
#   - T = A + B therefore sits below 1/2 tr(RIV) at finite n by ~1/2 the
#     expected-vs-sample gap, closing only as that gap closes.
#
# EXPLORATORY / post-hoc -- not pre-registered. See todo/008. MAR cells only
# (the congenial regime where the theorem applies). Uses the battery-standard
# apply_missingness_ampute (vs the apply_mar of the original scratch runs).
#
# Per cell, per replicate (seed 20260522 + r):
#   A_fiml  = barQ(theta_obs, theta_obs) - barQ(theta_obs, theta_true)  [RB FIML A]
#   A_prop  = mean_m ell_com(theta_obs; completion_m) - barQ(theta_obs, theta_true)
#                                                          [RB proper-MI A, Amelia]
#   B       = ell_com(theta_obs; X) - ell_com(theta_com; X)
#   tr_exp  = tr_riv_analytic(theta_obs)        (expected-information RIV)
#   tr_samp = riv_sample(Amelia imps)           (sample / Rubin RIV)
#   gap     = vec(theta_obs) - vec(theta_com)   (-> empirical gap variance)
#   score   = grad ell_obs at theta_true        (subset only; -> info equality)

run_one_w1info <- function(r, cell, mu0, Sigma0, M, score_cap) {
  set.seed(20260522 + r)
  theta_true <- list(mu = mu0, Sigma = Sigma0)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma0)
  theta_com <- mle_complete_mvn(X)
  ll_com_com = loglik_mvn(theta_com, X)
  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop, mech = cell$mech,
                                           pattern_type = cell$pattern),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(list(error = "ampute")) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE),
                  error = function(e) { return(NULL) })
  if (is.null(fit)) { return(list(error = "FIML")) }
  theta_obs <- list(mu = fit$mu, Sigma = fit$Sigma)
  ll_com_obs = loglik_mvn(theta_obs, X)
  term1 = barQ_fiml_analytic(theta_obs, theta_obs,  mar$Y, mar$R)   # cond @ theta_obs
  term2 = barQ_fiml_analytic(theta_obs, theta_true, mar$Y, mar$R)   # cond @ truth (RB)
  A_fiml = term1 - term2
  B = ll_com_obs - ll_com_com
  tr_exp = tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  imps <- tryCatch(impute_mvn_amelia(mar$Y, M = M), error = function(e) { return(NULL) })
  if (is.null(imps)) { return(list(error = "amelia")) }
  barL = mean(vapply(imps, function(d) { return(loglik_mvn(theta_obs, d)) }, numeric(1)))
  A_prop = barL - term2
  mf <- mi_fit_mvn(imps)
  tr_samp = tryCatch(riv_sample(mf$theta_imps, mf$U_imps)$tr_RIV,
                     error = function(e) { return(NA) })
  gap <- theta_to_vec(theta_obs) - theta_to_vec(theta_com)
  out <- list(error = NA_character_,
              A_fiml = A_fiml, A_prop = A_prop, B = B, T_prop = A_prop + B,
              tr_exp = tr_exp, tr_samp = tr_samp, gap = gap,
              score = NULL, I_obs_true = NULL)
  # Info-equality inputs on a capped subset (score grad is the expensive piece).
  if (r <= score_cap) {
    v_true <- theta_to_vec(theta_true)
    out$score <- numDeriv::grad(
      function(v) { return(loglik_obs_mvn(vec_to_theta(v, ncol(X)), mar$Y, mar$R)) },
      v_true)
    out$I_obs_true <- fisher_info_obs_mvn(theta_true, mar$Y, mar$R)
  }
  return(out)
}

run_w1_info_diagnostic <- function(R_per_cell, cl, out_dir,
                                   Ns = c(200, 500, 1000, 2000),
                                   M = 50, score_cap = 600) {
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  cat(sprintf("\n== Phase 6: W1 information diagnostic (R=%d, M=%d, MAR) ==\n\n",
              R_per_cell, M))

  cells <- list()
  cid = 0
  for (pat in c("non_monotone", "monotone")) {
    for (N in Ns) {
      cid = cid + 1
      cells[[cid]] <- list(id = sprintf("%s_MAR_N%d", pat, N),
                           pattern = pat, mech = "MAR", N = N, prop = 0.40)
    }
  }
  cat(sprintf("Cells: %d\n", length(cells)))

  if (!is.null(cl)) {
    parallel::clusterExport(cl, varlist = c("run_one_w1info"), envir = environment())
  }
  k = length(default_mu) + length(default_mu) * (length(default_mu) + 1) / 2  # 14

  mcse <- function(x) { return(sd(x, na.rm = TRUE) / sqrt(sum(!is.na(x)))) }
  rows <- list()
  for (i in seq_along(cells)) {
    cell <- cells[[i]]
    cat(sprintf("[%d/%d] %-26s  ", i, length(cells), cell$id))
    if (!is.null(cl)) {
      parallel::clusterExport(cl, varlist = c("cell", "M", "score_cap"),
                              envir = environment())
    }
    t0 <- Sys.time()
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_w1info(r, cell, default_mu, default_Sigma, M, score_cap))
    }, cl = cl)
    elapsed = as.numeric(difftime(Sys.time(), t0, units = "secs"))
    errs <- vapply(results, function(z) {
      return(!is.null(z$error) && !is.na(z$error))
    }, logical(1))
    ok <- results[!errs]
    if (length(ok) == 0) { cat(sprintf("FAIL (all errored)\n")); next }

    A_fiml <- vapply(ok, `[[`, numeric(1), "A_fiml")
    A_prop <- vapply(ok, `[[`, numeric(1), "A_prop")
    B_arr  <- vapply(ok, `[[`, numeric(1), "B")
    T_arr  <- vapply(ok, `[[`, numeric(1), "T_prop")
    trE    <- vapply(ok, `[[`, numeric(1), "tr_exp")
    trS    <- vapply(ok, `[[`, numeric(1), "tr_samp")
    G      <- do.call(rbind, lapply(ok, `[[`, "gap"))      # n_ok x k

    tr_exp = mean(trE)
    tr_samp = mean(trS, na.rm = TRUE)
    I_com_true <- fisher_info_com_mvn(list(mu = default_mu, Sigma = default_Sigma), cell$N)
    gap_riv = sum(diag(I_com_true %*% var(G)))             # = 2 |E[B]| target

    # Info equality on the scored subset.
    have_score <- !vapply(ok, function(z) { return(is.null(z$score)) }, logical(1))
    info_eq = NA
    if (sum(have_score) >= k + 1) {
      S <- do.call(rbind, lapply(ok[have_score], `[[`, "score"))
      Iobs_list <- lapply(ok[have_score], `[[`, "I_obs_true")
      Iobs_mean <- Reduce(`+`, Iobs_list) / length(Iobs_list)
      info_eq = sum(diag(var(S) %*% solve(Iobs_mean)))
    }

    saveRDS(list(cell = cell, elapsed_sec = elapsed,
                 A_fiml = A_fiml, A_prop = A_prop, B = B_arr, T_prop = T_arr,
                 tr_exp_arr = trE, tr_samp_arr = trS, gap = G,
                 summary = list(tr_exp = tr_exp, tr_samp = tr_samp,
                                gap_riv = gap_riv, info_eq = info_eq)),
            file = file.path(out_dir, sprintf("%s.rds", cell$id)))

    rows[[i]] <- data.frame(
      cell_id = cell$id, pattern = cell$pattern, N = cell$N, n_ok = length(ok),
      A_prop = mean(A_prop), A_prop_se = mcse(A_prop),
      A_fiml = mean(A_fiml),
      B = mean(B_arr), B_se = mcse(B_arr),
      T_prop = mean(T_arr), T_prop_se = mcse(T_arr),
      tr_exp = tr_exp, tr_samp = tr_samp, gap_riv = gap_riv, info_eq = info_eq,
      A_minus_exp = mean(A_prop) - tr_exp,
      B_plus_half_samp = mean(B_arr) + 0.5 * tr_samp,
      T_minus_half_exp = mean(T_arr) - 0.5 * tr_exp,
      stringsAsFactors = FALSE)
    cat(sprintf("%5.1fs  A_prop=%.2f tr_exp=%.2f tr_samp=%.2f  info_eq=%.1f\n",
                elapsed, mean(A_prop), tr_exp, tr_samp, info_eq))
  }

  df <- do.call(rbind, rows)
  write.csv(df, file.path(out_dir, "summary.csv"), row.names = FALSE)

  # Verdict block (the exploratory claims).
  cat("\n-- Phase 6 verdicts (exploratory) --\n")
  cat(sprintf("  info equality tr(J I^-1) ~ k=%d : range [%.1f, %.1f]  (=> correct spec, E-H not TIC)\n",
              k, min(df$info_eq, na.rm = TRUE), max(df$info_eq, na.rm = TRUE)))
  cat(sprintf("  A tracks EXPECTED RIV : |A - tr_exp| max = %.3f ; |A - tr_samp| max = %.3f\n",
              max(abs(df$A_minus_exp)), max(abs(df$A_prop - df$tr_samp))))
  cat(sprintf("  B tracks SAMPLE  RIV : |B + tr_samp/2| max = %.3f ; |B + tr_exp/2| max = %.3f\n",
              max(abs(df$B_plus_half_samp)), max(abs(df$B + 0.5 * df$tr_exp))))
  cat(sprintf("  expected-vs-sample RIV gap (tr_samp - tr_exp): %s\n",
              paste(sprintf("%.2f", df$tr_samp - df$tr_exp), collapse = ", ")))
  return(df)
}
