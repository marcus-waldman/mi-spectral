# _modules/term-a-mar-correction.R
#
# Phase 8 of run_all.R: the Term-A MAR design-imbalance term (A)+(C).
# Reproducible promotion of the standalone verification/term-a-mar-diagnostic.R (S1/S2),
# so the (A)+(C) evidence is committed (RDS + summary.csv + an aggregate verdict) rather
# than print-only. See todo/008 and manuscript/derivation.qmd @sec-termA.
#
# Quantity: (A)+(C) = E[A_rb] - tr(RIV_obs), the part of Term A beyond tr(RIV).
#   RB-A: A_rb = barQ(theta_obs,theta_obs) - barQ(theta_obs,theta_true), E[A_rb]=E[A]
#   (Rao-Blackwellized over the true completion; low variance, unbiased).
#   tr(RIV_obs) = tr(O_obs^-1 I_com) - k with the cross-inclusive observed info (K&M 1998).
#
# S1 (bivariate monotone, closed-form MLE): sweep selection strength b in
#     P(X1 missing | X2) = Phi(-0.4 + b X2); b=0 is MCAR. Validates the leading-order
#     closed form (A)+(C) = n_mis/n_obs - 1/2 tr(M_mis M_obs^-1) against the measured
#     remainder, and the RIV decomposition tr(RIV_obs) = n_mis/n_obs + tr(M_mis M_obs^-1),
#     with M_. = sum over (missing / observed) units of [1,X2][1,X2]^T. b=0 -> (A)+(C)~0.
#
# S2 (4-variate W1 regime, lavaan FIML): the empirical (A)+(C) surface under ampute MAR
#     (non_monotone, monotone) across N. No general-MVN closed form yet (that is Phase 3a);
#     this measures the target the Phase-3a derivation must reproduce. The constant is O(1)
#     (N-independent), so it persists rather than shrinking with N.
#
# Idempotent given (R_per_cell, seed). seed = 20260522 + r per replicate (repo convention).

TAMAR_BIV_MU   <- c(0, 0)
TAMAR_BIV_SIG  <- matrix(c(1, 0.5, 0.5, 1), 2, 2)
TAMAR_BIV_K    <- 5
TAMAR_BIV_TRUE <- list(mu = TAMAR_BIV_MU, Sigma = TAMAR_BIV_SIG)
TAMAR_S1_B <- c(0.0, 0.2, 0.4, 0.8)            # b = 0 is MCAR (control)
TAMAR_S1_N <- 800
TAMAR_S2_PATTERNS <- c("non_monotone", "monotone")
TAMAR_S2_N <- c(300, 800, 1500)                # O(1) constant: stable across N

tamar_mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

tamar_fiml_mono <- function(Y, R) {
  x2 <- Y[, 2]; mu2 <- mean(x2); s22 <- mean((x2 - mu2)^2)
  comp <- R[, 1] == 0; x1c <- Y[comp, 1]; x2c <- Y[comp, 2]
  b1 <- sum((x1c - mean(x1c)) * (x2c - mean(x2c))) / sum((x2c - mean(x2c))^2)
  b0 <- mean(x1c) - b1 * mean(x2c); v <- mean((x1c - (b0 + b1 * x2c))^2)
  return(list(mu = c(b0 + b1 * mu2, mu2),
              Sigma = matrix(c(v + b1^2 * s22, b1 * s22, b1 * s22, s22), 2, 2)))
}

tamar_s1_one <- function(r, N, b) {
  set.seed(20260522 + r)
  X <- mvtnorm::rmvnorm(N, TAMAR_BIV_MU, TAMAR_BIV_SIG)
  miss <- runif(N) < pnorm(-0.4 + b * X[, 2])
  if (sum(miss) < 5 || sum(!miss) < 8) { return(NULL) }
  Y <- X; Y[miss, 1] <- NA; R <- cbind(as.integer(miss), 0)
  to <- tamar_fiml_mono(Y, R)
  A_rb <- barQ_fiml_analytic(to, to, Y, R) - barQ_fiml_analytic(to, TAMAR_BIV_TRUE, Y, R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, Y, R), fisher_info_com_mvn(to, N)))) - TAMAR_BIV_K
  Z <- cbind(1, X[, 2]); Mmis <- crossprod(Z[miss, , drop = FALSE]); Mobs <- crossprod(Z[!miss, , drop = FALSE])
  nm <- sum(miss); no <- sum(!miss); trMM <- sum(diag(solve(Mobs, Mmis)))
  return(c(A_rb = A_rb, tr_obs = tr_obs, rem_meas = A_rb - tr_obs,
           rem_ana = nm / no - 0.5 * trMM, riv_ana = nm / no + trMM, miss = mean(miss)))
}

tamar_s2_one <- function(r, N, pattern) {
  set.seed(20260522 + r)
  q_true <- list(mu = default_mu, Sigma = default_Sigma)
  q_k <- length(default_mu) + length(default_mu) * (length(default_mu) + 1) / 2
  X <- gen_data(N, default_mu, default_Sigma)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = pattern),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) })
  if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, q_true, mar$Y, mar$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), fisher_info_com_mvn(to, N)))) - q_k
  return(c(rem = A_rb - tr_obs, tr_obs = tr_obs, A_rb = A_rb))
}

run_term_a_mar <- function(R_per_cell, cl, out_dir) {
  if (!dir.exists(out_dir)) { dir.create(out_dir, recursive = TRUE) }
  cat(sprintf("\n== Phase 8: Term-A MAR design-imbalance (A)+(C) [R=%d] ==\n", R_per_cell))
  has_cl <- !is.null(cl)
  if (has_cl) {
    clusterExport(cl, c("tamar_s1_one", "tamar_fiml_mono", "tamar_s2_one",
                        "TAMAR_BIV_MU", "TAMAR_BIV_SIG", "TAMAR_BIV_K", "TAMAR_BIV_TRUE"))
  }
  papply <- function(items, fn) {
    if (has_cl) { return(parLapply(cl, items, fn)) } else { return(lapply(items, fn)) }
  }
  rows <- list()

  # S1: bivariate monotone selection sweep (closed-form validation + MCAR control).
  cat(sprintf("  -- S1 (bivariate monotone, N=%d): MCAR control + closed-form check --\n", TAMAR_S1_N))
  for (b in TAMAR_S1_B) {
    N <- TAMAR_S1_N
    M <- do.call(rbind, Filter(Negate(is.null),
           papply(seq_len(R_per_cell), function(r) { return(tamar_s1_one(r, N, b)) })))
    cell_id <- sprintf("S1_b%.1f_N%d", b, N)
    saveRDS(M, file.path(out_dir, paste0(cell_id, ".rds")))
    rows[[cell_id]] <- data.frame(
      cell_id = cell_id, study = "S1", pattern = "biv_monotone", b = b, N = N,
      miss = mean(M[, "miss"]), tr_obs = mean(M[, "tr_obs"]), riv_ana = mean(M[, "riv_ana"]),
      rem_meas = mean(M[, "rem_meas"]), rem_meas_mcse = tamar_mcse(M[, "rem_meas"]),
      rem_ana = mean(M[, "rem_ana"]), n_ok = nrow(M), stringsAsFactors = FALSE)
    cat(sprintf("     b=%.1f miss=%.3f tr_obs=%.3f rem_meas=%+.3f(%.3f) rem_ana=%+.3f riv_ana=%.3f\n",
                b, rows[[cell_id]]$miss, rows[[cell_id]]$tr_obs, rows[[cell_id]]$rem_meas,
                rows[[cell_id]]$rem_meas_mcse, rows[[cell_id]]$rem_ana, rows[[cell_id]]$riv_ana))
  }

  # S2: 4-variate ampute MAR (the (A)+(C) surface; general-MVN closed form is Phase 3a).
  cat("  -- S2 (4-variate ampute MAR): empirical (A)+(C) surface across N --\n")
  for (pat in TAMAR_S2_PATTERNS) {
    for (N in TAMAR_S2_N) {
      M <- do.call(rbind, Filter(Negate(is.null),
             papply(seq_len(R_per_cell), function(r) { return(tamar_s2_one(r, N, pat)) })))
      cell_id <- sprintf("S2_%s_N%d", pat, N)
      saveRDS(M, file.path(out_dir, paste0(cell_id, ".rds")))
      rows[[cell_id]] <- data.frame(
        cell_id = cell_id, study = "S2", pattern = pat, b = NA, N = N,
        miss = NA, tr_obs = mean(M[, "tr_obs"]), riv_ana = NA,
        rem_meas = mean(M[, "rem"]), rem_meas_mcse = tamar_mcse(M[, "rem"]),
        rem_ana = NA, n_ok = nrow(M), stringsAsFactors = FALSE)
      cat(sprintf("     %-13s N=%4d rem_meas=%+.3f(%.3f) tr_obs=%.3f n_ok=%d\n",
                  pat, N, rows[[cell_id]]$rem_meas, rows[[cell_id]]$rem_meas_mcse,
                  rows[[cell_id]]$tr_obs, rows[[cell_id]]$n_ok))
    }
  }

  summary <- do.call(rbind, rows)
  write.csv(summary, file.path(out_dir, "summary.csv"), row.names = FALSE)
  cat(sprintf("  wrote %s\n", file.path(out_dir, "summary.csv")))
  return(summary)
}
