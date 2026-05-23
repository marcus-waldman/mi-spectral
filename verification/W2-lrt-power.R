# W2-lrt-power.R
#
# Empirical LRT power under local alternatives for H_0: sigma_{12} = 0
# vs H_1: sigma_{12} = n^{-1/2} delta. Preregistered at SHA ddc9037,
# todo/004-simulation-hypotheses.md §2.
#
# Configurations:
#   C1 (oracle)        : complete-data LRT vs chi^2_1.
#   C2 (corrected)     : Chan (2022 AoS) D_hat with bias-corrected numerator,
#                        vs Chan's MC reference distribution.
#   C3 (uncorrected)   : Chan (2022 AoS) D_hat with uncorrected numerator,
#                        vs Chan's MC reference distribution.
#   C4 (Chan-Meng EFMI F-reference) deferred.
#   C5 (Satorra-Bentler scaled-shifted) : chi^2_SB = a * (d_L - bias_corr) + b
#                        with a = sqrt(2df/(2df + 4 tr_perp + 2 sum_lambda_sq_perp))
#                        and b = df(1-a). Refer to chi^2_1.
#                        For k=1 (one tested parameter), sum_lambda_sq_perp =
#                        (tr_perp)^2 since there is one OMI eigenvalue.
#                        MI-IC validated this empirically at N=500 to match
#                        the complete-data oracle exactly (chi^2_MI_corr).
#
# Engine paths (per §0.3 Amendment 1):
#   amelia : Chan SMI test on M imputed datasets (chan_smi_test_k1) and
#            Satorra-Bentler on (d_L - bias_corr).
#   fiml   : observed-data LRT via lavaan FIML. Chan's MC reference doesn't
#            apply (no actual imputations); reference is chi^2_1 by Wilks.
#            Satorra-Bentler still computed via analytic tr_perp.
#
# Usage:
#   Rscript W2-lrt-power.R                          # pilot, fiml, 20 cores
#   Rscript W2-lrt-power.R pilot amelia             # pilot, amelia
#   Rscript W2-lrt-power.R prod fiml                # full, fiml
#   Rscript W2-lrt-power.R prod amelia              # full, amelia
#
# Per-replicate seed governance: set.seed(20260522 + r) per worker.

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args    <- commandArgs(trailingOnly = TRUE)
mode    <- if (length(args) >= 1) { args[1] } else { "pilot" }
engine  <- if (length(args) >= 2) { args[2] } else { "fiml" }
n_cores <- if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

stopifnot(engine %in% c("amelia", "fiml"))

cfg <- switch(mode,
  pilot = list(N = 200, M = 50,  R = 200,  delta_grid = c(0, 1, 2, 3)),
  prod  = list(N = 200, M = 200, R = 1000,
               delta_grid = c(0, 0.5, 1, 1.5, 2, 2.5, 3, 4)),
  stop(sprintf("Unknown mode '%s'", mode))
)

cat(sprintf("\nW2 LRT power  [mode=%s, engine=%s, cores=%d]\n",
            mode, engine, n_cores))
cat(sprintf("  N=%d   M=%d   R=%d   delta_grid=[%s]\n",
            cfg$N, cfg$M, cfg$R, paste(cfg$delta_grid, collapse = ", ")))


# -----------------------------------------------------------------------------
# Truth construction: Sigma_0(delta) = default_Sigma but with sigma_{12}
# replaced by delta / sqrt(N) (local-alternative scaling).
# -----------------------------------------------------------------------------

make_sigma_alt <- function(delta_value, N) {
  Sigma_alt <- default_Sigma
  Sigma_alt[1, 2] <- delta_value / sqrt(N)
  Sigma_alt[2, 1] <- delta_value / sqrt(N)
  return(Sigma_alt)
}


# -----------------------------------------------------------------------------
# Per-replicate work.
# -----------------------------------------------------------------------------

run_one_replicate_w2 <- function(r, cfg, engine, mu0, delta) {
  set.seed(20260522 + r)
  Sigma_truth <- make_sigma_alt(delta, cfg$N)
  X <- gen_data(N = cfg$N, mu = mu0, Sigma = Sigma_truth)

  # ---- Oracle (C1): complete-data LRT vs chi^2_1 ----
  un_com <- lavaan_fit_mvn(X, constrained = FALSE)
  cn_com <- lavaan_fit_mvn(X, constrained = TRUE)
  LRT_oracle <- 2 * (un_com$logLik - cn_com$logLik)
  p_oracle <- pchisq(LRT_oracle, df = 1, lower.tail = FALSE)

  # ---- MAR ----
  mar <- apply_mar(X)

  # ---- Observed-data unconstrained & constrained FIML MLEs ----
  un_obs <- lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE)
  cn_obs <- lavaan_fit_mvn_fiml(mar$Y, constrained = TRUE)
  theta_un_obs <- list(mu = un_obs$mu, Sigma = un_obs$Sigma)
  theta_cn_obs <- list(mu = cn_obs$mu, Sigma = cn_obs$Sigma)

  # ---- Bias correction differential (used by C2 in both engines) ----
  trRIV_un <- tr_riv_analytic(theta_un_obs, mar$Y, mar$R)$tr_RIV
  trRIV_cn <- tr_riv_analytic_constrained_sigma12(theta_cn_obs, mar$Y, mar$R)
  bias_correction <- trRIV_un - trRIV_cn

  # SB scaled-shifted helper (k = 1 single-parameter test):
  #   sum_lambda_sq_perp = tr_perp^2 since there's one eigenvalue.
  sb_chi2_from_lrt <- function(d_L) {
    tr_perp <- bias_correction
    sum_lambda_sq_perp <- bias_correction^2  # k = 1 only
    var_target <- 2  # 2 * df with df = 1
    var_predicted <- var_target + 4 * tr_perp + 2 * sum_lambda_sq_perp
    if (var_predicted <= 0) { return(list(stat = NA, p = NA, a = NA, b = NA)) }
    a <- sqrt(var_target / var_predicted)
    b <- 1 - a  # df * (1 - a) with df = 1
    stat <- a * (d_L - bias_correction) + b
    p <- pchisq(stat, df = 1, lower.tail = FALSE)
    return(list(stat = stat, p = p, a = a, b = b))
  }

  if (engine == "amelia") {
    # ---- Chan (2022, AoS) SMI test on M Amelia imputations ----
    imps <- impute_mvn_amelia(mar$Y, M = cfg$M)
    smi_un <- chan_smi_test_k1(imps, lrt_sigma12_device,
                               bias_correction = 0,    N_mc = 5000)
    smi_co <- chan_smi_test_k1(imps, lrt_sigma12_device,
                               bias_correction = bias_correction,
                               N_mc = 5000)
    p_uncorrected <- smi_un$p_value
    p_corrected   <- smi_co$p_value
    D_hat_un      <- smi_un$D_hat
    D_hat_co      <- smi_co$D_hat
    r_hat         <- smi_un$r_hat
    # SB-style scaled-shifted on the stacked-all LRT (= d_1_to_m * m).
    d_L_amelia <- smi_un$d_1_to_m  # = (1/m) d_L(X^{1:m}) ~ d_hat_L asymptotically
    sb <- sb_chi2_from_lrt(d_L_amelia)
    p_sb          <- sb$p
    chi2_sb_stat  <- sb$stat
  } else if (engine == "fiml") {
    LRT_fiml_obs <- 2 * (un_obs$logLik - cn_obs$logLik)
    p_uncorrected <- pchisq(LRT_fiml_obs, df = 1, lower.tail = FALSE)
    barL_un <- barQ_fiml_analytic(theta_un_obs, theta_un_obs, mar$Y, mar$R)
    barL_cn <- barQ_fiml_analytic(theta_cn_obs, theta_un_obs, mar$Y, mar$R)
    d_L_fiml <- 2 * (barL_un - barL_cn)
    LRT_Q_corrected <- d_L_fiml - bias_correction
    p_corrected   <- pchisq(LRT_Q_corrected, df = 1, lower.tail = FALSE)
    D_hat_un      <- LRT_fiml_obs
    D_hat_co      <- LRT_Q_corrected
    r_hat         <- NA
    sb <- sb_chi2_from_lrt(d_L_fiml)
    p_sb          <- sb$p
    chi2_sb_stat  <- sb$stat
  }

  return(list(
    delta_r        = delta,
    LRT_oracle     = LRT_oracle,
    p_oracle       = p_oracle,
    p_corrected    = p_corrected,
    p_uncorrected  = p_uncorrected,
    p_sb           = p_sb,
    chi2_sb        = chi2_sb_stat,
    D_hat_un       = D_hat_un,
    D_hat_co       = D_hat_co,
    r_hat          = r_hat,
    trRIV_un       = trRIV_un,
    trRIV_cn       = trRIV_cn,
    bias_corr      = bias_correction,
    miss1          = mean(mar$R[, 1]),
    miss2          = mean(mar$R[, 2]),
    sigma12_un_obs = theta_un_obs$Sigma[1, 2],
    sigma12_un_com = un_com$Sigma[1, 2]
  ))
}


# -----------------------------------------------------------------------------
# Run grid: for each delta, R replicates.
# -----------------------------------------------------------------------------

all_results <- list()
t0_all <- Sys.time()

cluster_active <- (n_cores > 1)
if (cluster_active) {
  cl <- parallel::makeCluster(n_cores)
  on.exit(parallel::stopCluster(cl), add = TRUE)
  parallel::clusterEvalQ(cl, { source("verification/00-setup.R") })
  parallel::clusterExport(cl, varlist = c("run_one_replicate_w2",
                                          "make_sigma_alt"))
  # chan_smi_test_k1 and lrt_sigma12_device are sourced in 00-setup.R.
}

for (delta_value in cfg$delta_grid) {
  cat(sprintf("\n  delta = %g\n", delta_value))
  t0 <- Sys.time()
  if (cluster_active) {
    parallel::clusterExport(cl, varlist = c("cfg", "engine", "delta_value"))
    res <- pbapply::pblapply(seq_len(cfg$R), function(r) {
      return(run_one_replicate_w2(r, cfg, engine, default_mu, delta_value))
    }, cl = cl)
  } else {
    res <- pbapply::pblapply(seq_len(cfg$R), function(r) {
      return(run_one_replicate_w2(r, cfg, engine, default_mu, delta_value))
    })
  }
  all_results[[as.character(delta_value)]] <- res
  cat(sprintf("    %.1fs\n", as.numeric(difftime(Sys.time(), t0, units = "secs"))))
}

elapsed_total <- as.numeric(difftime(Sys.time(), t0_all, units = "secs"))
cat(sprintf("\nDone in %.1f seconds.\n", elapsed_total))


# -----------------------------------------------------------------------------
# Rejection rates at alpha = 0.05. Reference depends on engine: amelia uses
# Chan's MC reference (p_value already computed); fiml uses chi^2_1 (Wilks).
# -----------------------------------------------------------------------------

alpha <- 0.05
mcse_rate <- function(p, n) { return(sqrt(p * (1 - p) / n)) }

rejection_table <- data.frame(
  delta            = numeric(),
  C1_oracle        = numeric(),
  C2_corrected     = numeric(),
  C3_uncorrected   = numeric(),
  C5_SB            = numeric(),
  mcse_corrected   = numeric(),
  mcse_uncorrected = numeric(),
  mcse_sb          = numeric(),
  median_bias_corr = numeric(),
  median_trRIV_un  = numeric(),
  median_trRIV_cn  = numeric(),
  median_r_hat     = numeric()
)

for (delta_value in cfg$delta_grid) {
  res <- all_results[[as.character(delta_value)]]
  p_or  <- vapply(res, `[[`, numeric(1), "p_oracle")
  p_co  <- vapply(res, `[[`, numeric(1), "p_corrected")
  p_un  <- vapply(res, `[[`, numeric(1), "p_uncorrected")
  p_sb_ <- vapply(res, `[[`, numeric(1), "p_sb")
  bias_c <- vapply(res, `[[`, numeric(1), "bias_corr")
  tr_un  <- vapply(res, `[[`, numeric(1), "trRIV_un")
  tr_cn  <- vapply(res, `[[`, numeric(1), "trRIV_cn")
  r_hat  <- vapply(res, `[[`, numeric(1), "r_hat")
  rejection_table <- rbind(rejection_table, data.frame(
    delta            = delta_value,
    C1_oracle        = mean(p_or < alpha),
    C2_corrected     = mean(p_co < alpha),
    C3_uncorrected   = mean(p_un < alpha),
    C5_SB            = mean(p_sb_ < alpha, na.rm = TRUE),
    mcse_corrected   = mcse_rate(mean(p_co < alpha), length(p_co)),
    mcse_uncorrected = mcse_rate(mean(p_un < alpha), length(p_un)),
    mcse_sb          = mcse_rate(mean(p_sb_ < alpha, na.rm = TRUE),
                                  sum(!is.na(p_sb_))),
    median_bias_corr = median(bias_c),
    median_trRIV_un  = median(tr_un),
    median_trRIV_cn  = median(tr_cn),
    median_r_hat     = if (engine == "amelia") { median(r_hat, na.rm = TRUE) } else { NA }
  ))
}

cat(sprintf("\n== W2 results: rejection rates at alpha=%.2f ==\n", alpha))
ref_msg <- if (engine == "amelia") { "C2/C3 Chan (2022 AoS) MC" } else { "C2/C3 chi^2_1 (Wilks)" }
cat(sprintf("Reference distributions: C1 chi^2_1; %s\n\n", ref_msg))
print(rejection_table, row.names = FALSE, digits = 4)

cache_path <- sprintf("verification/cache/W2-%s-%s.rds", mode, engine)
saveRDS(list(
  cfg = cfg, mode = mode, engine = engine, n_cores = n_cores,
  elapsed_total = elapsed_total,
  all_results = all_results,
  rejection_table = rejection_table
), file = cache_path)

cat(sprintf("\nCache: %s\n", cache_path))
