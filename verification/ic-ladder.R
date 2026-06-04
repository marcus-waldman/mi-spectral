# ic-ladder.R — the IC calibration ladder (todo/027, PREREGISTERED before this script).
#
# Saturated-anchored MI deviances T_k = 2[Qbar(psi*_sat) - Qbar(psi*_k)] for the W3
# candidate set (00-setup.R), with the correction ladder
#   rung 0: T                               (uncorrected)
#   rung 1: T - tr(RIV_perp)                (I_com-metric complement trace, @eq-lrt-bias —
#                                            NOT the naive trace difference)
#   rung 2: a T + b                         (two-moment match to chi2_qd; a, b DERIVED from
#                                            the analytic weighted-chi2 null law; CAS check
#                                            cas-wolfram/verify_ic_ladder.py L-A2)
#   rung 3: qchisq(F_W(T), qd)              (per-model null equipercentile equating;
#                                            F_W closed-form via CompQuadForm::imhof,
#                                            Chan-style MC fallback counted)
# plus the complete-data oracle and the FROZEN W3 SB arm's functional form (scaled-shift
# on the uncorrected statistic with naive-difference inputs — the issue-#1 construction)
# reproduced for the P7 comparison only. The frozen preregistered originals are untouched.
#
# Candidates are block-diagonal zero patterns, so every constrained Qbar-maximizer is
# closed-form from the E-step moments (m*, S*) at the saturated FIML fit:
# mu_k = m*, Sigma_k = block-restriction of S*, and T_k = N [log|Sigma_k| - log|S*|] >= 0.
#
# Cells (todo/027 §1.4): MAIN rho=0.40 / WEAK rho=0.10 / JUNK rho=0.00, all N=500,
# MAR non-monotone prop=0.40, deterministic-FIML engine, seeds 20260604 + r.
#
# Usage: Rscript verification/ic-ladder.R [R_per_cell] [n_cores] [cells]
#        defaults: 2000 6 MAIN,WEAK,JUNK

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(CompQuadForm)
})

args <- commandArgs(trailingOnly = TRUE)
R_per_cell = if (length(args) >= 1) { as.integer(args[1]) } else { 2000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 6 }
cell_names <- if (length(args) >= 3) { strsplit(args[3], ",")[[1]] } else { c("MAIN", "WEAK", "JUNK") }

N_LADDER = 500
P_FULL = 14
LADDER_MODELS <- c("MA", "MB", "MC", "MD")
LADDER_BLOCKS <- list(
  MA = list(1, 2, 3, 4),
  MB = list(c(1, 2), c(3, 4)),
  MC = list(c(1, 3), c(2, 4))
)
LADDER_CELLS <- list(
  MAIN = list(rho = 0.40, true_model = "MC"),
  WEAK = list(rho = 0.10, true_model = "MC"),
  JUNK = list(rho = 0.00, true_model = "MA")
)

# E-step moments of the saturated MVN at theta_obs (same construction as
# w2-paired-differential-mu1-cell.R).
ladder_estep_moments <- function(theta_obs, Y, R) {
  N = nrow(Y)
  p = ncol(Y)
  Xhat <- Y
  Vbar <- matrix(0, p, p)
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat)
    R_pat <- R[rows[1], ]
    Mi <- which(R_pat == 1)
    Oi <- which(R_pat == 0)
    if (length(Mi) == 0) { next }
    if (length(Oi) == 0) {
      Xhat[rows, ] <- matrix(theta_obs$mu, length(rows), p, byrow = TRUE)
      Vbar <- Vbar + length(rows) * theta_obs$Sigma
    } else {
      Soo_inv <- solve(theta_obs$Sigma[Oi, Oi, drop = FALSE])
      reg <- theta_obs$Sigma[Mi, Oi, drop = FALSE] %*% Soo_inv
      cond_V <- theta_obs$Sigma[Mi, Mi, drop = FALSE] -
        reg %*% t(theta_obs$Sigma[Mi, Oi, drop = FALSE])
      cm <- sweep(Y[rows, Oi, drop = FALSE], 2, theta_obs$mu[Oi], FUN = "-") %*% t(reg)
      Xhat[rows, Mi] <- sweep(cm, 2, theta_obs$mu[Mi], FUN = "+")
      Vfull <- matrix(0, p, p)
      Vfull[Mi, Mi] <- cond_V
      Vbar <- Vbar + length(rows) * Vfull
    }
  }
  m_star <- colMeans(Xhat)
  Xc <- sweep(Xhat, 2, m_star, FUN = "-")
  S_star <- crossprod(Xc) / N + Vbar / N
  return(list(m = m_star, S = S_star))
}

# Block-diagonal restriction of a covariance matrix (the closed-form constrained
# Qbar / complete-data MLE for the zero-pattern candidates).
ladder_block_restrict <- function(S, blocks) {
  Sig <- matrix(0, nrow(S), ncol(S))
  for (b in blocks) {
    Sig[b, b] <- S[b, b, drop = FALSE]
  }
  return(Sig)
}

# Anchored deviance T_k = N [log|Sigma_k| - log|S|] for a moment matrix S.
ladder_T_anchored <- function(S, blocks, N) {
  Sig_k <- ladder_block_restrict(S, blocks)
  val = N * (determinant(Sig_k, logarithm = TRUE)$modulus -
             determinant(S, logarithm = TRUE)$modulus)
  return(as.numeric(val))
}

# Analytic null-law spectrum + traces for candidate free_idx at theta (todo/027 §1.3):
# lam = nonzero eig of [I_com^-1 - G (G'I_com G)^-1 G'] I_com I_obs^-1 I_com,
# tr_perp per @eq-lrt-bias, naive trace difference for the P7/L2 comparison, and the
# per-model self-contained spectra feeding the frozen-SB-arm reconstruction.
ladder_spectrum <- function(theta, Y, R, free_idx) {
  N = nrow(Y)
  q_d = P_FULL - length(free_idx)
  I_com <- fisher_info_com_mvn(theta, N)
  I_obs <- fisher_info_obs_mvn(theta, Y, R)
  I_mis <- I_com - I_obs
  IoinvImis <- solve(I_obs, I_mis)
  tr_full = sum(diag(IoinvImis))
  Mproj <- I_com %*% IoinvImis
  tr_proj = sum(diag(solve(I_com[free_idx, free_idx, drop = FALSE],
                           Mproj[free_idx, free_idx, drop = FALSE])))
  tr_perp = tr_full - tr_proj
  M_full <- solve(I_obs, I_com)
  tr_riv_f = sum(diag(M_full)) - P_FULL
  M_sub <- solve(I_obs[free_idx, free_idx, drop = FALSE],
                 I_com[free_idx, free_idx, drop = FALSE])
  tr_riv_0 = sum(diag(M_sub)) - length(free_idx)
  tr_naive = tr_riv_f - tr_riv_0
  slsq_f = sum(M_full * t(M_full)) - 2 * (tr_riv_f + P_FULL) + P_FULL
  slsq_0 = sum(M_sub * t(M_sub)) - 2 * (tr_riv_0 + length(free_idx)) + length(free_idx)
  A <- solve(I_com)
  A[free_idx, free_idx] <- A[free_idx, free_idx] -
    solve(I_com[free_idx, free_idx, drop = FALSE])
  V <- I_com %*% solve(I_obs, I_com)
  eV <- eigen((V + t(V)) / 2, symmetric = TRUE)
  Vh <- eV$vectors %*% (sqrt(pmax(eV$values, 0)) * t(eV$vectors))
  lam_all <- eigen(Vh %*% ((A + t(A)) / 2) %*% Vh, symmetric = TRUE,
                   only.values = TRUE)$values
  lam <- sort(lam_all, decreasing = TRUE)[seq_len(q_d)]
  spec_gap = abs(sum(lam) - (q_d + tr_perp)) / max(1, q_d + tr_perp)
  return(list(lam = lam, q_d = q_d, tr_perp = tr_perp, tr_naive = tr_naive,
              tr_riv_f = tr_riv_f, tr_riv_0 = tr_riv_0,
              slsq_f = slsq_f, slsq_0 = slsq_0, spec_gap = spec_gap))
}

# F_W(x) for W = sum lam_j chi2_1 via Imhof; NA on failure (caller falls back to MC).
ladder_imhof_cdf <- function(x, lam) {
  out <- tryCatch(CompQuadForm::imhof(x, lambda = lam, epsabs = 1e-9,
                                      epsrel = 1e-9, limit = 50000),
                  error = function(e) { return(NULL) })
  if (is.null(out)) { return(NA) }
  Fx = 1 - out$Qq
  if (!is.finite(Fx) || Fx < -0.01 || Fx > 1.01) { return(NA) }
  return(min(max(Fx, 1e-12), 1 - 1e-12))
}

# Chan-style MC fallback for the equating CDF (counted; preregistered tolerance < 1%).
ladder_mc_cdf <- function(x, lam, n_mc = 200000) {
  W <- as.numeric(matrix(rchisq(n_mc * length(lam), df = 1), n_mc,
                         length(lam)) %*% lam)
  Fx = mean(W <= x)
  return(min(max(Fx, 1e-12), 1 - 1e-12))
}

run_one_ladder <- function(r, cell) {
  set.seed(20260604 + r)
  Sigma_truth <- w3_sigma(rho = cell$rho)
  X <- gen_data(N = N_LADDER, mu = default_mu, Sigma = Sigma_truth)
  th_com <- mle_complete_mvn(X)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR",
                                           pattern_type = "non_monotone"),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(list(error = "ampute")) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE),
                  error = function(e) { return(NULL) })
  if (is.null(fit)) { return(list(error = "fiml")) }
  theta_obs <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(theta_obs$Sigma)) ||
      min(eigen(theta_obs$Sigma, only.values = TRUE)$values) < 1e-6) {
    return(list(error = "fiml-pd"))
  }
  em <- ladder_estep_moments(theta_obs, mar$Y, mar$R)
  if (min(eigen(em$S, only.values = TRUE)$values) < 1e-6) {
    return(list(error = "estep-pd"))
  }
  out <- c(r = r)
  spec_gap_max = 0
  lam_min_global = Inf
  n_fallback = 0
  sel_scores <- list(oracle = numeric(4), r0 = numeric(4), r1 = numeric(4),
                     r2 = numeric(4), r3 = numeric(4), frozen = numeric(4))
  for (nm in names(sel_scores)) {
    names(sel_scores[[nm]]) <- LADDER_MODELS
    sel_scores[[nm]]["MD"] <- 2 * W3_NPAR["MD"]
  }
  for (k in c("MA", "MB", "MC")) {
    blocks <- LADDER_BLOCKS[[k]]
    free_idx <- W3_FREE_IDX[[k]]
    q_d = P_FULL - length(free_idx)
    T_com = ladder_T_anchored(th_com$Sigma, blocks, N_LADDER)
    T_mi = ladder_T_anchored(em$S, blocks, N_LADDER)
    if (T_com < -1e-6 || T_mi < -1e-6) { return(list(error = "negT")) }
    T_com = max(T_com, 0)
    T_mi = max(T_mi, 0)
    psi_k <- list(mu = em$m, Sigma = ladder_block_restrict(em$S, blocks))
    sp <- tryCatch(ladder_spectrum(psi_k, mar$Y, mar$R, free_idx),
                   error = function(e) { return(NULL) })
    if (is.null(sp)) { return(list(error = sprintf("spectrum-%s", k))) }
    spec_gap_max = max(spec_gap_max, sp$spec_gap)
    lam_min_global = min(lam_min_global, min(sp$lam))
    # rungs
    T0 = T_mi
    T1 = T_mi - sp$tr_perp
    a_k = sqrt(q_d / sum(sp$lam^2))
    b_k = q_d - a_k * sum(sp$lam)
    T2 = a_k * T_mi + b_k
    Fx = ladder_imhof_cdf(T_mi, sp$lam)
    if (is.na(Fx)) {
      n_fallback = n_fallback + 1
      Fx = ladder_mc_cdf(T_mi, sp$lam)
    }
    T3 = qchisq(Fx, df = q_d)
    # frozen W3 SB arm functional form (issue-#1 construction; P7 report only):
    # scaled-shift on the UNCORRECTED statistic with naive-difference inputs.
    tr_perp_naive = sp$tr_riv_f - sp$tr_riv_0
    slsq_perp_naive = max(sp$slsq_f - sp$slsq_0, 0)
    var_target = 2 * q_d
    var_predicted = var_target + 4 * tr_perp_naive + 2 * slsq_perp_naive
    T_frozen = if (var_predicted <= 0) { T_mi } else {
      a_f = sqrt(var_target / var_predicted)
      a_f * T_mi + q_d * (1 - a_f)
    }
    sel_scores$oracle[k] <- T_com + 2 * W3_NPAR[k]
    sel_scores$r0[k] <- T0 + 2 * W3_NPAR[k]
    sel_scores$r1[k] <- T1 + 2 * W3_NPAR[k]
    sel_scores$r2[k] <- T2 + 2 * W3_NPAR[k]
    sel_scores$r3[k] <- T3 + 2 * W3_NPAR[k]
    sel_scores$frozen[k] <- T_frozen + 2 * W3_NPAR[k]
    vals <- c(T_com, T0, T1, T2, T3, T_frozen, sp$tr_perp, tr_perp_naive,
              max(sp$lam), a_k)
    names(vals) <- paste0(c("Tcom_", "T0_", "T1_", "T2_", "T3_", "Tfz_",
                            "trperp_", "trnaive_", "lammax_", "a_"), k)
    out <- c(out, vals)
  }
  sels <- sapply(sel_scores, function(s) { return(which.min(s)) })
  names(sels) <- paste0("sel_", names(sel_scores))
  out <- c(out, sels,
           specgap = spec_gap_max, lammin = lam_min_global, nfb = n_fallback)
  return(list(error = NA, stats = out))
}

# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------

dir.create("verification/cache", showWarnings = FALSE, recursive = TRUE)
cat(sprintf("====== IC calibration ladder (todo/027) ======\n"))
cat(sprintf("R_per_cell=%d  n_cores=%d  cells={%s}  N=%d  seeds 20260604+r\n\n",
            R_per_cell, n_cores, paste(cell_names, collapse = ","), N_LADDER))

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, {
  source("verification/00-setup.R")
  suppressPackageStartupMessages({
    library(lavaan)
    library(CompQuadForm)
  })
}))
clusterExport(cl, c("N_LADDER", "P_FULL", "LADDER_MODELS", "LADDER_BLOCKS",
                    "LADDER_CELLS", "ladder_estep_moments", "ladder_block_restrict",
                    "ladder_T_anchored", "ladder_spectrum", "ladder_imhof_cdf",
                    "ladder_mc_cdf", "run_one_ladder"))

summary_rows <- list()
for (cn in cell_names) {
  cell <- LADDER_CELLS[[cn]]
  if (is.null(cell)) { stop(sprintf("unknown cell %s", cn)) }
  cat(sprintf("-- cell %s (rho=%.2f, true=%s) --\n", cn, cell$rho, cell$true_model))
  t0 <- Sys.time()
  clusterExport(cl, "cell", envir = environment())
  results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
    return(run_one_ladder(r, cell))
  }, cl = cl)
  elapsed = as.numeric(difftime(Sys.time(), t0, units = "secs"))
  errs <- sapply(results, function(rr) { return(!is.na(rr$error)) })
  ok <- results[!errs]
  M <- do.call(rbind, lapply(ok, `[[`, "stats"))
  err_types <- if (sum(errs) > 0) { table(sapply(results[errs], `[[`, "error")) } else { NULL }
  saveRDS(list(cell = cn, config = cell, N = N_LADDER, R_per_cell = R_per_cell,
               n_ok = nrow(M), n_err = sum(errs),
               err_types = err_types,
               stats = M, elapsed_sec = elapsed),
          file = sprintf("verification/cache/ic-ladder-%s.rds", cn))
  # asserts (todo/027 §1.5)
  a_spec = max(M[, "specgap"])
  a_lam = min(M[, "lammin"])
  fb_frac = sum(M[, "nfb"]) / (3 * nrow(M))
  cat(sprintf("   ok=%d err=%d (%.1fs)   asserts: max specgap=%.2e  min lam=%.6f  imhof fallback=%.3f%%\n",
              nrow(M), sum(errs), elapsed, a_spec, a_lam, 100 * fb_frac))
  if (a_spec > 1e-6 || a_lam < 1 - 1e-6 || fb_frac >= 0.01) {
    stop("PREREGISTERED ASSERT VIOLATED — run not gradable (todo/027 §1.5)")
  }
  true_idx = which(LADDER_MODELS == cell$true_model)
  pis <- sapply(c("oracle", "r0", "r1", "r2", "r3", "frozen"), function(arm) {
    return(mean(M[, paste0("sel_", arm)] == true_idx))
  })
  under <- sapply(c("oracle", "r0", "r1", "r2", "r3", "frozen"), function(arm) {
    return(mean(M[, paste0("sel_", arm)] %in% c(1, 2)))
  })
  cat(sprintf("   pi(true=%s): oracle=%.3f  r0=%.3f  r1=%.3f  r2=%.3f  r3=%.3f  frozenSB=%.3f\n",
              cell$true_model, pis["oracle"], pis["r0"], pis["r1"], pis["r2"],
              pis["r3"], pis["frozen"]))
  cat(sprintf("   P(select underfit MA/MB):  oracle=%.3f  r0=%.3f  r1=%.3f  r2=%.3f  r3=%.3f\n",
              under["oracle"], under["r0"], under["r1"], under["r2"], under["r3"]))
  # distributional measures on the cell-relevant statistics
  ks2 <- function(x, y) {
    return(suppressWarnings(as.numeric(ks.test(x, y)$statistic)))
  }
  meas <- list()
  null_set <- if (cn == "JUNK") { c("MA", "MB", "MC") } else { "MC" }
  for (k in null_set) {
    Tc <- M[, paste0("Tcom_", k)]
    for (j in 0:3) {
      Tj <- M[, paste0("T", j, "_", k)]
      meas[[sprintf("ks%d_%s", j, k)]] <- ks2(Tj, Tc)
      meas[[sprintf("varratio%d_%s", j, k)]] <- var(Tj) / var(Tc)
      meas[[sprintf("meangap%d_%s", j, k)]] <- mean(Tj - Tc)
      meas[[sprintf("meangapse%d_%s", j, k)]] <- sd(Tj - Tc) / sqrt(nrow(M))
    }
  }
  if (cn != "JUNK") {
    for (j in 1:3) {
      meas[[sprintf("ncratio%d_MA", j)]] <-
        mean(M[, paste0("T", j, "_MA")]) / mean(M[, "Tcom_MA"])
    }
  }
  if (cn == "WEAK") {
    dmi <- M[, "T3_MB"] - M[, "T3_MC"]
    dcom <- M[, "Tcom_MB"] - M[, "Tcom_MC"]
    meas[["p8_mean_dMI"]] <- mean(dmi)
    meas[["p8_mean_dcom"]] <- mean(dcom)
    meas[["p8_sd_dMI"]] <- sd(dmi)
    meas[["p8_sd_dcom"]] <- sd(dcom)
    meas[["p8_corr_MI"]] <- cor(M[, "T3_MB"], M[, "T3_MC"])
    meas[["p8_corr_com"]] <- cor(M[, "Tcom_MB"], M[, "Tcom_MC"])
  }
  meas[["trperp_MC_mean"]] <- mean(M[, "trperp_MC"])
  meas[["trnaive_MC_mean"]] <- mean(M[, "trnaive_MC"])
  meas[["trperp_MA_mean"]] <- mean(M[, "trperp_MA"])
  meas[["trnaive_MA_mean"]] <- mean(M[, "trnaive_MA"])
  meas[["lammax_MC_mean"]] <- mean(M[, "lammax_MC"])
  meas[["a_MC_mean"]] <- mean(M[, "a_MC"])
  for (nm in names(meas)) {
    cat(sprintf("   %-18s %10.4f\n", nm, meas[[nm]]))
  }
  row <- data.frame(cell = cn, rho = cell$rho, true_model = cell$true_model,
                    N = N_LADDER, R = R_per_cell, n_ok = nrow(M),
                    n_err = sum(errs), elapsed_sec = elapsed,
                    pi_oracle = pis["oracle"], pi_r0 = pis["r0"],
                    pi_r1 = pis["r1"], pi_r2 = pis["r2"], pi_r3 = pis["r3"],
                    pi_frozenSB = pis["frozen"],
                    under_oracle = under["oracle"], under_r0 = under["r0"],
                    under_r1 = under["r1"], under_r2 = under["r2"],
                    under_r3 = under["r3"],
                    stringsAsFactors = FALSE)
  for (nm in names(meas)) {
    row[[nm]] <- meas[[nm]]
  }
  summary_rows[[cn]] <- row
  cat("\n")
}
stopCluster(cl)

# long-format union of columns across cells
all_cols <- unique(unlist(lapply(summary_rows, names)))
summary_df <- do.call(rbind, lapply(summary_rows, function(row) {
  for (cc in setdiff(all_cols, names(row))) {
    row[[cc]] <- NA
  }
  return(row[, all_cols])
}))
write.csv(summary_df, "verification/cache/ic-ladder-summary.csv", row.names = FALSE)
cat("wrote verification/cache/ic-ladder-summary.csv\n")
cat("==============================================\n")
