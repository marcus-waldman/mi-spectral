# _modules/w3-sweep.R
#
# Phase 2 of run_all.R: W3 main sweep — MI-AIC/BIC selection across the
# 60-cell grid (2 patterns x 2 mechanisms x 3 Ns x 5 engine/M/cong slots).
#
# Per todo/005 §0.6. R_per_cell replicates per cell with seed
# 20260522 + r. Mechanisms restricted to {MAR, MNAR} for the main sweep;
# MNAR_targeted is *not* included in the W3 main grid (pilot showed it
# does not materially amplify load-bearing bias vs MNAR; including it
# would double compute for marginal evidence) — it appears in Phase 4
# (mnar bias measurement) only.

W3_MODEL_NAMES <- c("MA", "MB", "MC", "MD")
TRUE_MODEL <- "MC"

run_one_w3 <- function(r, cell, mu0, Sigma_truth) {
  set.seed(20260522 + r)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma_truth)
  ell_com <- numeric(4); names(ell_com) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    fit_k <- tryCatch(lavaan_fit_mvn_model(X, W3_MODELS[[k]]),
                      error = function(e) NULL)
    if (is.null(fit_k)) { return(list(error = "complete-fit")) }
    ell_com[k] <- fit_k$logLik
  }
  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop,
                                            mech = cell$mech,
                                            pattern_type = cell$pattern),
                  error = function(e) NULL)
  if (is.null(mar)) { return(list(error = "ampute")) }
  theta_obs_list <- list()
  for (k in W3_MODEL_NAMES) {
    fit_k <- tryCatch(lavaan_fit_mvn_fiml_model(mar$Y, W3_MODELS[[k]]),
                      error = function(e) NULL)
    if (is.null(fit_k)) { return(list(error = sprintf("FIML-%s", k))) }
    theta_obs_list[[k]] <- list(mu = fit_k$mu, Sigma = fit_k$Sigma)
  }
  theta_D_obs <- theta_obs_list[["MD"]]
  barL <- numeric(4); names(barL) <- W3_MODEL_NAMES
  if (cell$engine == "fiml") {
    for (k in W3_MODEL_NAMES) {
      theta_k <- list(mu = theta_obs_list[[k]]$mu,
                      Sigma = theta_obs_list[[k]]$Sigma)
      barL[k] <- barQ_fiml_analytic(theta_k, theta_D_obs, mar$Y, mar$R)
    }
  } else {
    empri_actual <- cell$empri_frac * cell$N
    imps <- tryCatch(impute_mvn_amelia(mar$Y, M = cell$M, empri = empri_actual),
                     error = function(e) NULL)
    if (is.null(imps)) { return(list(error = "amelia")) }
    for (k in W3_MODEL_NAMES) {
      theta_k <- list(mu = theta_obs_list[[k]]$mu,
                      Sigma = theta_obs_list[[k]]$Sigma)
      barL[k] <- mean(sapply(imps, function(Z) {
        return(loglik_mvn(theta_k, Z))
      }))
    }
  }
  trRIV         <- numeric(4); names(trRIV)         <- W3_MODEL_NAMES
  sum_lambda_sq <- numeric(4); names(sum_lambda_sq) <- W3_MODEL_NAMES
  trRIV_obs     <- numeric(4); names(trRIV_obs)     <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    theta_k <- list(mu = theta_obs_list[[k]]$mu,
                    Sigma = theta_obs_list[[k]]$Sigma)
    sp <- riv_spectrum_analytic_general(theta_k, mar$Y, mar$R, W3_FREE_IDX[[k]])
    trRIV[k]         <- sp$tr_RIV                                       # expected-info RIV (Term A)
    sum_lambda_sq[k] <- sp$sum_lambda_sq
    trRIV_obs[k]     <- tr_riv_observed_general(theta_k, mar$Y, mar$R,  # observed/sample RIV (Term B)
                                                W3_FREE_IDX[[k]])
  }
  # RETIRED ARM (issue #1, closed 2026-06-04): scaled-shift applied to the UNCORRECTED
  # chi2_MI with naive-difference tr/sum_lsq inputs. Superseded by the ladder rung 2 in
  # verification/ic-ladder.R (todo/027; derived a_k, b_k from the @sec-lrt null law).
  # Frozen as committed; not re-run; headline arms unaffected. Do not fix in place.
  chi2_MI_per_k <- 2 * (barL["MD"] - barL)
  trRIV_D <- trRIV["MD"]; sum_lsq_D <- sum_lambda_sq["MD"]
  chi2_SB <- numeric(4); names(chi2_SB) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    if (k == "MD") { chi2_SB[k] <- 0; next }
    df_k <- W3_NPAR["MD"] - W3_NPAR[k]
    tr_perp_k <- trRIV_D - trRIV[k]
    sum_lsq_perp <- max(sum_lsq_D - sum_lambda_sq[k], 0)
    var_target <- 2 * df_k
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
  # Bias correction uses the OBSERVED-data RIV. The deviance bias is 2 E[T] = tr(RIV)
  # per model, with RIV = tr(I_obs^-1 I_mis) on the OBSERVED information -- the single
  # correct RIV under MAR (Kenward-Molenberghs 1998; the naive block-diagonal trRIV is
  # the as-if-MCAR form, incomplete under MAR). The earlier `termspec` arm
  # (2*trRIV - trRIV_obs) was built on the retired two-RIV split and is removed.
  # See derivation.qmd Appendix C and todo/008.
  AIC_corrected <- -2 * barL    + 2 * W3_NPAR + trRIV_obs
  AIC_sb        <- chi2_SB      + 2 * W3_NPAR
  return(list(
    error = NA_character_,
    sel_oracle    = names(which.min(AIC_oracle)),
    sel_uncorr    = names(which.min(AIC_uncorr)),
    sel_corrected = names(which.min(AIC_corrected)),
    sel_sb        = names(which.min(AIC_sb)),
    trRIV = trRIV, trRIV_obs = trRIV_obs
  ))
}

run_w3_sweep <- function(R_per_cell, cl, out_dir,
                          mechs = c("MAR", "MNAR")) {
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  cat(sprintf("\n== Phase 2: W3 main sweep (R=%d, mechs={%s}) ==\n\n",
              R_per_cell, paste(mechs, collapse = ", ")))
  Sigma_truth_w3 <- w3_sigma(rho = 0.4)

  cells <- list()
  cid <- 0
  for (pat in c("non_monotone", "monotone")) {
    for (mech in mechs) {
      for (N in c(200, 500, 1000)) {
        cid <- cid + 1
        cells[[cid]] <- list(
          id = sprintf("fiml_%s_%s_N%d", pat, mech, N),
          pattern = pat, mech = mech, N = N,
          engine = "fiml", M = NA_integer_, empri_frac = 0,
          prop = 0.40
        )
        for (M in c(20, 200)) {
          for (empri_frac in c(0, 0.5)) {
            cong_tag <- if (empri_frac == 0) "cong" else "uncong"
            cid <- cid + 1
            cells[[cid]] <- list(
              id = sprintf("amelia_%s_%s_N%d_M%d_%s",
                            pat, mech, N, M, cong_tag),
              pattern = pat, mech = mech, N = N,
              engine = "amelia", M = M, empri_frac = empri_frac,
              prop = 0.40
            )
          }
        }
      }
    }
  }
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
    if (!is.null(cl)) {
      parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
    }
    cat(sprintf("[%2d/%2d] %-50s  ", i, length(cells), cell$id))
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
    n_err <- sum(errors); ok <- results[!errors]
    tab <- function(field) {
      if (length(ok) == 0) return(setNames(rep(NA_real_, 4), W3_MODEL_NAMES))
      sels <- sapply(ok, `[[`, field)
      return(sapply(W3_MODEL_NAMES, function(k) mean(sels == k)))
    }
    rt <- rbind(oracle = tab("sel_oracle"),
                uncorrected = tab("sel_uncorr"),
                corrected = tab("sel_corrected"),
                SB = tab("sel_sb"))
    miscl <- sapply(ok, `[[`, "sel_uncorr")
    miscl <- miscl[miscl != TRUE_MODEL]
    W3C <- if (length(miscl) > 0) mean(miscl == "MD") else NA_real_
    W3A <- rt["corrected", TRUE_MODEL] - rt["uncorrected", TRUE_MODEL]
    W3B <- rt["oracle", TRUE_MODEL] - rt["corrected", TRUE_MODEL]
    saveRDS(list(cell = cell, R_per_cell = R_per_cell, elapsed_sec = elapsed,
                 results = results, rates_table = rt),
            file = file.path(out_dir, sprintf("%s.rds", cell$id)))
    cat(sprintf("%5.1fs ok=%4d err=%2d  W3A=%+.3f W3C=%.3f  pi[corr/orc]=%.3f/%.3f\n",
                elapsed, length(ok), n_err, W3A, W3C,
                rt["corrected", TRUE_MODEL],
                rt["oracle", TRUE_MODEL]))
    rows[[i]] <- data.frame(
      cell_id = cell$id, pattern = cell$pattern, mech = cell$mech,
      N = cell$N, engine = cell$engine, M = cell$M,
      empri_frac = cell$empri_frac, prop = cell$prop,
      elapsed_sec = elapsed, n_ok = length(ok), n_err = n_err,
      pi_oracle = rt["oracle", TRUE_MODEL],
      pi_uncorrected = rt["uncorrected", TRUE_MODEL],
      pi_corrected = rt["corrected", TRUE_MODEL],
      pi_SB = rt["SB", TRUE_MODEL],
      W3A_corr_minus_uncorr = W3A,
      W3B_oracle_minus_corr = W3B,
      W3C_high_RIV_frac = W3C,
      W3C_n_miscl = length(miscl),
      stringsAsFactors = FALSE
    )
  }
  elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
  cat(sprintf("\nPhase 2 W3 sweep elapsed: %.1fs (%.2f min)\n",
              elapsed_total, elapsed_total / 60))
  df <- do.call(rbind, rows)
  write.csv(df, file.path(out_dir, "summary.csv"), row.names = FALSE)
  return(df)
}
