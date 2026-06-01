# _modules/w1-information-diagnostic.R
#
# Phase 6 of run_all.R: W1 information diagnostic, in the ONE-RIV framing.
#
# Establishes, per cell, that the deviance-bias terms calibrate to a SINGLE RIV --
# the OBSERVED-data RIV  tr(O_obs^-1 I_com) - k, with O_obs the observed information
# (observed_info_obs_mvn). Under MAR that information carries a mean x covariance
# cross term (Kenward & Molenberghs 1998, Sec 3.2) that the naive block-diagonal
# form (fisher_info_obs_mvn / tr_riv_analytic) omits; the naive RIV is therefore the
# as-if-MCAR, incomplete one. Per cell:
#   - A (imputation bias) and B (estimation mismatch) BOTH track the observed-data
#     RIV:  E[A] ~ +tr_obs,  E[B] ~ -1/2 tr_obs   (the earlier "A->expected,
#     B->sample" split was an artifact of grading against the naive info);
#   - the asymptotic lemmas hold against the observed info:
#       L1  tr(O_obs . Var[theta_obs])      ~ k
#       L3  tr(I_com . Cov[theta_obs,theta_com]) ~ k
#       L2  tr(I_com . Var[gap])            ~ tr_obs
#   - information equality tr(J_hat . O_obs^-1) ~ k holds (correct specification);
#   - the naive RIV tr_exp < tr_obs by the cross term; the Rubin between/within
#     sample RIV tr_samp ~ tr_obs.
#
# The dedicated FIML lemma traces also live in verification/lemma-revalidation.R;
# this phase adds the proper-MI (Amelia) confirmation and both patterns x 4 N.
#
# EXPLORATORY / post-hoc -- not pre-registered. See todo/008. MAR cells only
# (the congenial regime where the theorem applies).
#
# Per cell, per replicate (seed 20260522 + r):
#   A_fiml  = barQ(theta_obs, theta_obs) - barQ(theta_obs, theta_true)  [RB FIML A]
#   A_prop  = mean_m ell_com(theta_obs; completion_m) - barQ(theta_obs, theta_true)
#                                                          [RB proper-MI A, Amelia]
#   B       = ell_com(theta_obs; X) - ell_com(theta_com; X)
#   tr_obs  = tr(O_obs^-1 I_com) - k             (observed-data RIV; THE RIV)
#   tr_exp  = tr_riv_analytic(theta_obs)         (naive / as-if-MCAR RIV, for contrast)
#   tr_samp = riv_sample(Amelia imps)            (Rubin between/within sample RIV)
#   th_obs, th_com = theta vectors               (-> L1/L3 lemma traces, gap variance)
#   O_obs   = observed_info_obs_mvn(theta_obs)   (-> mean, for the L1 trace)
#   score, J_denom = grad ell_obs at truth + observed info at truth (-> info equality)

run_one_w1info <- function(r, cell, mu0, Sigma0, M, score_cap) {
  set.seed(20260522 + r)
  theta_true <- list(mu = mu0, Sigma = Sigma0)
  k_dim = length(mu0) + length(mu0) * (length(mu0) + 1) / 2
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

  # The RIV: observed-data information in the denominator (vs the naive block-diagonal).
  O_obs <- observed_info_obs_mvn(theta_obs, mar$Y, mar$R)
  I_com_at_obs <- fisher_info_com_mvn(theta_obs, cell$N)
  tr_obs = sum(diag(solve(O_obs, I_com_at_obs))) - k_dim
  tr_exp = tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV          # naive / as-if-MCAR

  imps <- tryCatch(impute_mvn_amelia(mar$Y, M = M), error = function(e) { return(NULL) })
  if (is.null(imps)) { return(list(error = "amelia")) }
  barL = mean(vapply(imps, function(d) { return(loglik_mvn(theta_obs, d)) }, numeric(1)))
  A_prop = barL - term2
  mf <- mi_fit_mvn(imps)
  tr_samp = tryCatch(riv_sample(mf$theta_imps, mf$U_imps)$tr_RIV,
                     error = function(e) { return(NA) })

  out <- list(error = NA_character_,
              A_fiml = A_fiml, A_prop = A_prop, B = B, T_prop = A_prop + B,
              tr_obs = tr_obs, tr_exp = tr_exp, tr_samp = tr_samp,
              th_obs = theta_to_vec(theta_obs), th_com = theta_to_vec(theta_com),
              O_obs = O_obs, score = NULL, J_denom = NULL)
  # Info-equality inputs on a capped subset (the score grad is the expensive piece).
  # Denominator is the OBSERVED info at the truth (not the naive form): info equality
  # is J = E[-d^2 ell_obs] = the observed information under MAR.
  if (r <= score_cap) {
    v_true <- theta_to_vec(theta_true)
    out$score <- numDeriv::grad(
      function(v) { return(loglik_obs_mvn(vec_to_theta(v, ncol(X)), mar$Y, mar$R)) },
      v_true)
    out$J_denom <- observed_info_obs_mvn(theta_true, mar$Y, mar$R)
  }
  return(out)
}

run_w1_info_diagnostic <- function(R_per_cell, cl, out_dir,
                                   Ns = c(200, 500, 1000, 2000),
                                   M = 50, score_cap = 600) {
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  cat(sprintf("\n== Phase 6: W1 information diagnostic (R=%d, M=%d, MAR; one-RIV) ==\n\n",
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
    trO    <- vapply(ok, `[[`, numeric(1), "tr_obs")
    trE    <- vapply(ok, `[[`, numeric(1), "tr_exp")
    trS    <- vapply(ok, `[[`, numeric(1), "tr_samp")
    TO <- do.call(rbind, lapply(ok, `[[`, "th_obs"))       # n_ok x k
    TC <- do.call(rbind, lapply(ok, `[[`, "th_com"))
    G  <- TO - TC
    Obar <- Reduce(`+`, lapply(ok, `[[`, "O_obs")) / length(ok)

    tr_obs = mean(trO)
    tr_exp = mean(trE)
    tr_samp = mean(trS, na.rm = TRUE)
    I_com_true <- fisher_info_com_mvn(list(mu = default_mu, Sigma = default_Sigma), cell$N)

    # Lemma traces against the observed-data information.
    L1_trace = sum(diag(Obar %*% var(TO)))        # ~ k     if Var(theta_obs) = O_obs^-1
    L3_trace = sum(diag(I_com_true %*% var(TO, TC)))  # ~ k if Cov(obs,com) = I_com^-1
    gap_riv  = sum(diag(I_com_true %*% var(G)))    # ~ tr_obs if Var(gap)=O_obs^-1-I_com^-1

    # Info equality against the observed info: tr(J_hat O_obs^-1) ~ k.
    have_score <- !vapply(ok, function(z) { return(is.null(z$score)) }, logical(1))
    info_eq = NA
    if (sum(have_score) >= k + 1) {
      S <- do.call(rbind, lapply(ok[have_score], `[[`, "score"))
      Jden_list <- lapply(ok[have_score], `[[`, "J_denom")
      Jden_mean <- Reduce(`+`, Jden_list) / length(Jden_list)
      info_eq = sum(diag(var(S) %*% solve(Jden_mean)))
    }

    saveRDS(list(cell = cell, elapsed_sec = elapsed,
                 A_fiml = A_fiml, A_prop = A_prop, B = B_arr, T_prop = T_arr,
                 tr_obs_arr = trO, tr_exp_arr = trE, tr_samp_arr = trS, gap = G,
                 summary = list(tr_obs = tr_obs, tr_exp = tr_exp, tr_samp = tr_samp,
                                gap_riv = gap_riv, info_eq = info_eq,
                                L1_trace = L1_trace, L3_trace = L3_trace)),
            file = file.path(out_dir, sprintf("%s.rds", cell$id)))

    rows[[i]] <- data.frame(
      cell_id = cell$id, pattern = cell$pattern, N = cell$N, n_ok = length(ok),
      A_prop = mean(A_prop), A_prop_se = mcse(A_prop),
      A_fiml = mean(A_fiml),
      B = mean(B_arr), B_se = mcse(B_arr),
      T_prop = mean(T_arr), T_prop_se = mcse(T_arr),
      tr_obs = tr_obs, tr_exp = tr_exp, tr_samp = tr_samp,
      gap_riv = gap_riv, info_eq = info_eq,
      L1_trace = L1_trace, L3_trace = L3_trace,
      # one-RIV residuals (observed-data RIV)
      A_minus_obs = mean(A_prop) - tr_obs,
      B_plus_half_obs = mean(B_arr) + 0.5 * tr_obs,
      T_minus_half_obs = mean(T_arr) - 0.5 * tr_obs,
      # naive contrast (kept for the record)
      A_minus_exp = mean(A_prop) - tr_exp,
      B_plus_half_samp = mean(B_arr) + 0.5 * tr_samp,
      T_minus_half_exp = mean(T_arr) - 0.5 * tr_exp,
      stringsAsFactors = FALSE)
    cat(sprintf("%5.1fs  A_prop=%.2f tr_obs=%.2f (naive %.2f, samp %.2f)  L1=%.1f L3=%.1f info_eq=%.1f\n",
                elapsed, mean(A_prop), tr_obs, tr_exp, tr_samp, L1_trace, L3_trace, info_eq))
  }

  df <- do.call(rbind, rows)
  write.csv(df, file.path(out_dir, "summary.csv"), row.names = FALSE)

  # Verdict block (one-RIV framing).
  cat("\n-- Phase 6 verdicts (one-RIV, observed-data information) --\n")
  cat(sprintf("  E[A] ~ +tr_obs   : max|A_prop - tr_obs| = %.3f\n", max(abs(df$A_minus_obs))))
  cat(sprintf("  E[B] ~ -tr_obs/2 : max|B + tr_obs/2|    = %.3f\n", max(abs(df$B_plus_half_obs))))
  cat(sprintf("  lemmas vs observed info: L1 tr(O.Var[obs]) in [%.1f,%.1f] (~k=%d); L3 tr(Ic.Cov[o,c]) in [%.1f,%.1f] (~k); L2 tr(Ic.Var[gap]) vs tr_obs max gap = %.3f\n",
              min(df$L1_trace), max(df$L1_trace), k, min(df$L3_trace), max(df$L3_trace),
              max(abs(df$gap_riv - df$tr_obs))))
  cat(sprintf("  info equality tr(J O_obs^-1) ~ k=%d : range [%.1f, %.1f] (correct spec)\n",
              k, min(df$info_eq, na.rm = TRUE), max(df$info_eq, na.rm = TRUE)))
  cat(sprintf("  naive RIV (as-if-MCAR) is smaller: tr_obs - tr_exp in [%.2f, %.2f]; Rubin sample tr_samp ~ tr_obs (max |tr_samp - tr_obs| = %.2f)\n",
              min(df$tr_obs - df$tr_exp), max(df$tr_obs - df$tr_exp),
              max(abs(df$tr_samp - df$tr_obs), na.rm = TRUE)))
  return(df)
}
