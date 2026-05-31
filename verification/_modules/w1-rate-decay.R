# _modules/w1-rate-decay.R
#
# Phase 7 of run_all.R: fitted decay rate of the finite-sample remainders.
#
# Converts the derivation's "the expected-vs-sample (Efron-Hinkley) gap closes
# slowly, not as a clean O(1/n)" claim from eyeballed to measured. Fits the
# decay exponent b in  gap(N) = tr_samp(N) - tr_exp(N) ~ c * N^b  by WLS log-log
# regression over a FIXED LOG-SPACED grid of N, averaging per N before taking
# the log (so the per-replicate Jensen bias of log|.| and its zero-crossings do
# not contaminate the slope). See todo/008 for the design.
#
# Engine: FIML / analytic. The gap needs only the FIML fit theta_obs plus the
# expected (tr_riv_analytic) and observed (tr_riv_observed_general) RIVs -- no
# imputations, no numerical derivatives -- so a long grid + large R is cheap.
# A, B, T are computed too (cheap under FIML) and reported per N, but only the
# gap is rate-fit (A/T are MCSE-limited and the remainders cross zero).

run_one_rate <- function(r, cell, mu0, Sigma0) {
  set.seed(20260522 + r)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma0)
  theta_com <- mle_complete_mvn(X)
  ll_cc = loglik_mvn(theta_com, X)
  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop, mech = cell$mech,
                                           pattern_type = cell$pattern),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(list(error = "ampute")) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE),
                  error = function(e) { return(NULL) })
  if (is.null(fit)) { return(list(error = "FIML")) }
  theta_obs <- list(mu = fit$mu, Sigma = fit$Sigma)
  ll_co = loglik_mvn(theta_obs, X)
  k = length(mu0) + length(mu0) * (length(mu0) + 1) / 2
  tr_exp  = tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  tr_samp = tr_riv_observed_general(theta_obs, mar$Y, mar$R, seq_len(k))
  A = barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ll_co
  B = ll_co - ll_cc
  return(list(error = NA_character_, tr_exp = tr_exp, tr_samp = tr_samp,
              gap = tr_samp - tr_exp, A = A, B = B, T = A + B))
}

run_w1_rate_decay <- function(R_per_cell, cl, out_dir,
                              Ns = round(exp(seq(log(200), log(1e4), length.out = 10))),
                              patterns = c("non_monotone", "monotone")) {
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  cat(sprintf("\n== Phase 7: rate-of-decay of the E-H gap (R=%d/cell, MAR, FIML) ==\n", R_per_cell))
  cat(sprintf("log-spaced N grid: %s\n", paste(Ns, collapse = ", ")))
  if (!is.null(cl)) {
    parallel::clusterExport(cl, varlist = c("run_one_rate"), envir = environment())
  }
  mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

  rows <- list(); cid = 0; fits <- list()
  for (pat in patterns) {
    cat(sprintf("\n-- pattern: %s --\n", pat))
    g_mean <- numeric(length(Ns)); g_se <- numeric(length(Ns))
    for (j in seq_along(Ns)) {
      cell <- list(pattern = pat, mech = "MAR", N = Ns[j], prop = 0.40)
      if (!is.null(cl)) { parallel::clusterExport(cl, varlist = c("cell"), envir = environment()) }
      res <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
        return(run_one_rate(r, cell, default_mu, default_Sigma))
      }, cl = cl)
      ok <- Filter(function(z) { return(is.null(z$error) || is.na(z$error)) }, res)
      g  <- vapply(ok, `[[`, numeric(1), "gap")
      te <- vapply(ok, `[[`, numeric(1), "tr_exp")
      ts <- vapply(ok, `[[`, numeric(1), "tr_samp")
      Av <- vapply(ok, `[[`, numeric(1), "A")
      Bv <- vapply(ok, `[[`, numeric(1), "B")
      Tv <- vapply(ok, `[[`, numeric(1), "T")
      g_mean[j] = mean(g); g_se[j] = mcse(g)
      cid = cid + 1
      rows[[cid]] <- data.frame(
        pattern = pat, N = Ns[j], n_ok = length(ok),
        tr_exp = mean(te), tr_samp = mean(ts),
        gap = mean(g), gap_se = mcse(g),
        A = mean(Av), A_se = mcse(Av), B = mean(Bv), B_se = mcse(Bv),
        T = mean(Tv), T_se = mcse(Tv), stringsAsFactors = FALSE)
      cat(sprintf("   N=%6d  gap=%.3f (%.3f)  tr_exp=%.3f tr_samp=%.3f\n",
                  Ns[j], mean(g), mcse(g), mean(te), mean(ts)))
    }
    # WLS log-log fit of the gap decay (weights = precision of log mean_gap).
    w <- (g_mean / g_se)^2
    f <- lm(log(g_mean) ~ log(Ns), weights = w)
    b   = unname(coef(f)[2])
    ci  <- unname(confint(f)[2, ])
    fits[[pat]] <- list(b = b, ci = ci, g_mean = g_mean, g_se = g_se, Ns = Ns)
    cat(sprintf("   >> gap decay exponent b = %.3f  (95%% CI [%.3f, %.3f])  [b=-1 is O(1/n), -0.5 is O(1/sqrt n)]\n",
                b, ci[1], ci[2]))
  }

  df <- do.call(rbind, rows)
  write.csv(df, file.path(out_dir, "summary.csv"), row.names = FALSE)
  saveRDS(fits, file.path(out_dir, "gap_decay_fits.rds"))
  cat("\n-- Phase 7 fitted gap-decay exponents --\n")
  for (pat in patterns) {
    cat(sprintf("  %-13s b = %+.3f  CI [%+.3f, %+.3f]\n",
                pat, fits[[pat]]$b, fits[[pat]]$ci[1], fits[[pat]]$ci[2]))
  }
  return(df)
}
