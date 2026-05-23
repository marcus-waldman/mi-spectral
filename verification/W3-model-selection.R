# W3-model-selection.R
#
# MI-AIC / MI-BIC model selection accuracy.
# Preregistered at SHA ddc9037, todo/004-simulation-hypotheses.md §3.
#
# Truth: Sigma_0^W3 with sigma_13 = sigma_24 = 0.4 and all other off-
# diagonals zero, so M_C is the true model. Candidates:
#   M_A (diagonal, 8 free params) — over-restrictive
#   M_B (sigma_12, sigma_34 free; 10 free params) — wrong off-diagonals, high RIV
#   M_C (sigma_13, sigma_24 free; 10 free params) — TRUE
#   M_D (unrestricted, 14 free params) — over-fit, highest RIV
#
# Three selection rules:
#   Oracle               : argmin_k [-2 ell_com(theta_k_com) + 2 * p_k]
#   Uncorrected MI-AIC   : argmin_k [-2 bar L_M(theta_k_obs) + 2 * p_k]
#   Bias-corrected MI-AIC: argmin_k [-2 bar L_M(theta_k_obs) + 2 * p_k + tr(RIV_k)]
#
# Engine paths:
#   amelia : per-imputation lavaan fits per candidate, pool, bar L_M
#            averaged across imputations at the pooled estimate.
#   fiml   : lavaan FIML per candidate, analytic bar L_M^FIML via
#            barQ_fiml_analytic with theta_un_obs (M_D's FIML estimate)
#            as the imputation parameter.
#
# tr(RIV) for each candidate: analytic via fisher_info_*_mvn restricted
# to the candidate's free-parameter subset (tr_riv_analytic_general).
#
# Usage:
#   Rscript W3-model-selection.R                  # pilot, fiml, 20 cores
#   Rscript W3-model-selection.R pilot amelia
#   Rscript W3-model-selection.R prod fiml
#   Rscript W3-model-selection.R prod amelia

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
  pilot = list(N = 200, M = 50,  R = 200),
  prod  = list(N = 200, M = 200, R = 1000),
  stop(sprintf("Unknown mode '%s'", mode))
)

cat(sprintf("\nW3 model selection  [mode=%s, engine=%s, cores=%d]\n",
            mode, engine, n_cores))
cat(sprintf("  N=%d   M=%d   R=%d\n\n", cfg$N, cfg$M, cfg$R))

W3_MODEL_NAMES <- c("MA", "MB", "MC", "MD")
TRUE_MODEL <- "MC"


# -----------------------------------------------------------------------------
# Per-replicate work.
# -----------------------------------------------------------------------------

run_one_replicate_w3 <- function(r, cfg, engine, mu0, Sigma_truth) {
  set.seed(20260522 + r)
  X <- gen_data(N = cfg$N, mu = mu0, Sigma = Sigma_truth)

  # --- Complete-data MLE per candidate ---
  ell_com <- numeric(4); names(ell_com) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    fit_k <- lavaan_fit_mvn_model(X, W3_MODELS[[k]])
    ell_com[k] <- fit_k$logLik
  }

  # --- MAR mask ---
  mar <- apply_mar(X)

  # --- Observed-data FIML MLE per candidate ---
  theta_obs_list <- list()
  for (k in W3_MODEL_NAMES) {
    fit_k <- lavaan_fit_mvn_fiml_model(mar$Y, W3_MODELS[[k]])
    theta_obs_list[[k]] <- list(mu = fit_k$mu, Sigma = fit_k$Sigma,
                                logLik_obs = fit_k$logLik)
  }
  theta_D_obs <- theta_obs_list[["MD"]]  # imputation parameter for FIML engine

  # --- bar L_M per candidate (engine-dependent) ---
  barL <- numeric(4); names(barL) <- W3_MODEL_NAMES
  if (engine == "fiml") {
    for (k in W3_MODEL_NAMES) {
      theta_k <- list(mu = theta_obs_list[[k]]$mu,
                      Sigma = theta_obs_list[[k]]$Sigma)
      barL[k] <- barQ_fiml_analytic(theta_k, theta_D_obs, mar$Y, mar$R)
    }
  } else if (engine == "amelia") {
    imps <- impute_mvn_amelia(mar$Y, M = cfg$M)
    for (k in W3_MODEL_NAMES) {
      theta_k <- list(mu = theta_obs_list[[k]]$mu,
                      Sigma = theta_obs_list[[k]]$Sigma)
      barL[k] <- mean(sapply(imps, function(Z) {
        return(loglik_mvn(theta_k, Z))
      }))
    }
  }

  # --- tr(RIV) per candidate (analytic) ---
  trRIV <- numeric(4); names(trRIV) <- W3_MODEL_NAMES
  for (k in W3_MODEL_NAMES) {
    theta_k <- list(mu = theta_obs_list[[k]]$mu,
                    Sigma = theta_obs_list[[k]]$Sigma)
    trRIV[k] <- tr_riv_analytic_general(theta_k, mar$Y, mar$R, W3_FREE_IDX[[k]])
  }

  # --- Three selection rules ---
  AIC_oracle     <- -2 * ell_com + 2 * W3_NPAR
  AIC_uncorr     <- -2 * barL    + 2 * W3_NPAR
  AIC_corrected  <- -2 * barL    + 2 * W3_NPAR + trRIV

  sel_oracle    <- names(which.min(AIC_oracle))
  sel_uncorr    <- names(which.min(AIC_uncorr))
  sel_corrected <- names(which.min(AIC_corrected))

  return(list(
    sel_oracle    = sel_oracle,
    sel_uncorr    = sel_uncorr,
    sel_corrected = sel_corrected,
    ell_com       = ell_com,
    barL          = barL,
    trRIV         = trRIV,
    AIC_oracle    = AIC_oracle,
    AIC_uncorr    = AIC_uncorr,
    AIC_corrected = AIC_corrected,
    miss1         = mean(mar$R[, 1]),
    miss2         = mean(mar$R[, 2])
  ))
}


# -----------------------------------------------------------------------------
# Setup: truth fixture + parallel cluster.
# -----------------------------------------------------------------------------

Sigma_truth_w3 <- w3_sigma(rho = 0.4)

t0 <- Sys.time()

cluster_active <- (n_cores > 1)
if (cluster_active) {
  cl <- parallel::makeCluster(n_cores)
  on.exit(parallel::stopCluster(cl), add = TRUE)
  parallel::clusterEvalQ(cl, { source("verification/00-setup.R") })
  parallel::clusterExport(cl, varlist = c("cfg", "engine",
                                          "run_one_replicate_w3",
                                          "Sigma_truth_w3",
                                          "W3_MODEL_NAMES"))
  results <- pbapply::pblapply(seq_len(cfg$R), function(r) {
    return(run_one_replicate_w3(r, cfg, engine, default_mu, Sigma_truth_w3))
  }, cl = cl)
} else {
  results <- pbapply::pblapply(seq_len(cfg$R), function(r) {
    return(run_one_replicate_w3(r, cfg, engine, default_mu, Sigma_truth_w3))
  })
}

elapsed_total <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("\nDone in %.1f seconds.\n\n", elapsed_total))


# -----------------------------------------------------------------------------
# Aggregate: selection-rate table per rule per candidate model.
# -----------------------------------------------------------------------------

tab_selection <- function(results, field) {
  sels <- sapply(results, `[[`, field)
  out <- sapply(W3_MODEL_NAMES, function(k) { mean(sels == k) })
  names(out) <- W3_MODEL_NAMES
  return(out)
}

oracle_rates    <- tab_selection(results, "sel_oracle")
uncorr_rates    <- tab_selection(results, "sel_uncorr")
corrected_rates <- tab_selection(results, "sel_corrected")

rates_table <- rbind(oracle = oracle_rates,
                     uncorrected = uncorr_rates,
                     corrected   = corrected_rates)

mcse_rate <- function(p, n) { return(sqrt(p * (1 - p) / n)) }
mcse_true <- sapply(list(oracle = oracle_rates, uncorr = uncorr_rates,
                          corrected = corrected_rates),
                    function(rr) { mcse_rate(rr[TRUE_MODEL], cfg$R) })

# Average tr(RIV) by candidate model.
trRIV_mat <- do.call(rbind, lapply(results, function(rr) { return(rr$trRIV) }))
median_trRIV <- apply(trRIV_mat, 2, median)

cat(sprintf("Selection rates (R = %d) — TRUE model is %s\n\n",
            cfg$R, TRUE_MODEL))
print(round(rates_table, 3))
cat(sprintf("\nMedian tr(RIV) per candidate:\n"))
print(round(median_trRIV, 3))
cat(sprintf("\nTrue-model selection rate (with MCSE):\n"))
cat(sprintf("  oracle        : %.3f (MCSE %.3f)\n",
            oracle_rates[TRUE_MODEL],    mcse_true["oracle"]))
cat(sprintf("  uncorrected   : %.3f (MCSE %.3f)\n",
            uncorr_rates[TRUE_MODEL],    mcse_true["uncorr"]))
cat(sprintf("  corrected     : %.3f (MCSE %.3f)\n",
            corrected_rates[TRUE_MODEL], mcse_true["corrected"]))

gap_co_un  <- corrected_rates[TRUE_MODEL] - uncorr_rates[TRUE_MODEL]
gap_or_co  <- oracle_rates[TRUE_MODEL]    - corrected_rates[TRUE_MODEL]
cat(sprintf("\n(W3-A) pi*_corrected - pi*_uncorrected = %+.3f  (target >= 0.10)\n", gap_co_un))
cat(sprintf("(W3-B) pi*_oracle    - pi*_corrected    = %+.3f  (target <= 0.05)\n", gap_or_co))
# Direction: among uncorrected misclassifications, what fraction go to the
# larger-RIV candidates (MB, MD)?
miscl_idx <- which(sapply(results, function(rr) { return(rr$sel_uncorr != TRUE_MODEL) }))
if (length(miscl_idx) > 0) {
  miscl_sels <- sapply(results[miscl_idx], `[[`, "sel_uncorr")
  pct_high_riv <- mean(miscl_sels %in% c("MB", "MD"))
  cat(sprintf("(W3-C) Among uncorrected misclassifications, P[pick high-RIV] = %.3f  (target >= 0.60)\n",
              pct_high_riv))
}

cache_path <- sprintf("verification/cache/W3-%s-%s.rds", mode, engine)
saveRDS(list(
  cfg = cfg, mode = mode, engine = engine, n_cores = n_cores,
  elapsed_total = elapsed_total,
  results = results, rates_table = rates_table,
  median_trRIV = median_trRIV
), file = cache_path)
cat(sprintf("\nCache: %s\n", cache_path))
