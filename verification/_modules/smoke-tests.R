# _modules/smoke-tests.R
#
# Phase 0 of run_all.R: ampute-vs-apply_mar smoke test + pre-flight
# tr(RIV) table. Gates the rest of the sweep — if smoke fails, abort.

run_smoke_tests <- function(out_dir, n_seeds_riv = 50) {
  cat("\n== Phase 0a: ampute vs apply_mar smoke test ==\n\n")
  set.seed(20260523)
  N_big <- 10000
  X_big <- gen_data(N = N_big, mu = default_mu, Sigma = default_Sigma)

  set.seed(20260523)
  ml_legacy <- apply_mar(X_big)
  set.seed(20260523)
  ml_ampute <- apply_missingness_ampute(X_big, prop = 0.318,
                                         mech = "MAR",
                                         pattern_type = "non_monotone")
  mrg_legacy <- colMeans(ml_legacy$R)
  mrg_ampute <- colMeans(ml_ampute$R)
  cat(sprintf("  marginals legacy : %.3f %.3f %.3f %.3f\n",
              mrg_legacy[1], mrg_legacy[2], mrg_legacy[3], mrg_legacy[4]))
  cat(sprintf("  marginals ampute : %.3f %.3f %.3f %.3f\n",
              mrg_ampute[1], mrg_ampute[2], mrg_ampute[3], mrg_ampute[4]))
  match_within_1pp <- (abs(mrg_legacy[1] - mrg_ampute[1]) <= 0.015) &&
                       (abs(mrg_legacy[2] - mrg_ampute[2]) <= 0.015)
  cat(sprintf("  marginals match within 1.5pp: %s\n",
              if (match_within_1pp) "PASS" else "FAIL"))

  cat("\n  ampute all combinations at prop=0.40:\n")
  combo_ok <- TRUE
  for (mech in c("MAR", "MNAR", "MNAR_targeted")) {
    for (pat in c("non_monotone", "monotone")) {
      set.seed(20260523)
      ml <- apply_missingness_ampute(X_big, prop = 0.40,
                                      mech = mech, pattern_type = pat)
      mr <- colMeans(ml$R)
      target_hit <- if (pat == "non_monotone") {
        abs(mean(mr[1:2]) - 0.40) <= 0.03
      } else {
        abs(mr[4] - 0.40) <= 0.03 && (mr[1] == 0) && (mr[2] <= mr[3]) && (mr[3] <= mr[4])
      }
      cat(sprintf("    %-15s %-13s : %.3f %.3f %.3f %.3f  %s\n",
                  mech, pat, mr[1], mr[2], mr[3], mr[4],
                  if (target_hit) "ok" else "FAIL"))
      combo_ok <- combo_ok && target_hit
    }
  }

  ampute_pass <- match_within_1pp && combo_ok

  cat("\n== Phase 0b: pre-flight tr(RIV) table ==\n\n")
  Sigma_truth <- w3_sigma(rho = 0.4)
  theta_truth <- list(mu = default_mu, Sigma = Sigma_truth)
  models <- c("MA", "MB", "MC", "MD")
  rows <- list()
  for (pat in c("non_monotone", "monotone")) {
    for (mech in c("MAR", "MNAR")) {
      for (N in c(200, 500, 1000)) {
        tr_mat <- matrix(NA_real_, nrow = n_seeds_riv, ncol = length(models))
        colnames(tr_mat) <- models
        for (s in seq_len(n_seeds_riv)) {
          set.seed(20260601 + s)
          X <- gen_data(N = N, mu = theta_truth$mu, Sigma = theta_truth$Sigma)
          mar <- apply_missingness_ampute(X, prop = 0.40, mech = mech,
                                           pattern_type = pat)
          for (k in models) {
            tr_mat[s, k] <- tr_riv_analytic_general(theta_truth, mar$Y, mar$R,
                                                     W3_FREE_IDX[[k]])
          }
        }
        means <- colMeans(tr_mat)
        rows[[length(rows) + 1]] <- data.frame(
          pattern = pat, mech = mech, N = N,
          tr_MA = means["MA"], tr_MB = means["MB"],
          tr_MC = means["MC"], tr_MD = means["MD"],
          spread_D_minus_C = means["MD"] - means["MC"],
          stringsAsFactors = FALSE
        )
        cat(sprintf("  %-13s %-4s N=%4d   MA=%.2f MB=%.2f MC=%.2f MD=%.2f   D-C=%.2f\n",
                    pat, mech, N, means["MA"], means["MB"], means["MC"],
                    means["MD"], means["MD"] - means["MC"]))
      }
    }
  }
  riv_df <- do.call(rbind, rows)
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  write.csv(riv_df, file.path(out_dir, "preflight-trRIV.csv"),
            row.names = FALSE)

  return(list(pass = ampute_pass, riv_df = riv_df))
}
