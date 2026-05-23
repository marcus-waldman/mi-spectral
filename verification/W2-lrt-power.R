# W2-lrt-power.R
#
# Empirical LRT power under local alternatives for H_0: sigma_{12} = 0
# vs H_1: sigma_{12} = n^{-1/2} delta. Preregistered at SHA ddc9037,
# todo/004-simulation-hypotheses.md §2.
#
# This first-pass implementation runs three of the four preregistered
# configurations, all referring the statistic to chi^2_1:
#   C1 (oracle)        : complete-data LRT.
#   C2 (corrected)     : MI LRT statistic minus bias-correction differential.
#   C3 (uncorrected)   : MI LRT statistic as-is.
# C4 (Chan-Meng F-reference) is deferred to a follow-up commit pending the
# Chan (2022, AoS) MC reference distribution machinery.
#
# Engine paths (per §0.3 Amendment 1):
#   amelia : per-imputation lavaan fits, pooled MI estimate, bar L_M evaluated
#            at the pooled estimate over the M imputations.
#   fiml   : lavaan FIML on observed data; bar L_M computed analytically via
#            barQ_fiml_analytic with theta_obs as the imputation parameter.
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

  # ---- Oracle (C1): complete-data LRT ----
  un_com <- lavaan_fit_mvn(X, constrained = FALSE)
  cn_com <- lavaan_fit_mvn(X, constrained = TRUE)
  LRT_oracle <- 2 * (un_com$logLik - cn_com$logLik)

  # ---- MAR and observed-data fits ----
  mar <- apply_mar(X)
  miss1 <- mean(mar$R[, 1])
  miss2 <- mean(mar$R[, 2])

  # Observed-data unconstrained & constrained FIML MLEs (lavaan).
  un_obs <- lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE)
  cn_obs <- lavaan_fit_mvn_fiml(mar$Y, constrained = TRUE)
  theta_un_obs <- list(mu = un_obs$mu, Sigma = un_obs$Sigma)
  theta_cn_obs <- list(mu = cn_obs$mu, Sigma = cn_obs$Sigma)

  # ---- bar L_M at the unconstrained and constrained MLEs ----
  if (engine == "fiml") {
    # Analytic FIML-marginalized bar Q under theta_un_obs as the imputation
    # parameter (the unconstrained EM-MLE; this is the natural "fitted" model
    # used for imputation in the FIML setup).
    barL_un <- barQ_fiml_analytic(theta_un_obs, theta_un_obs, mar$Y, mar$R)
    barL_cn <- barQ_fiml_analytic(theta_cn_obs, theta_un_obs, mar$Y, mar$R)
  } else if (engine == "amelia") {
    imps <- impute_mvn_amelia(mar$Y, M = cfg$M)
    barL_un <- mean(sapply(imps, function(Z) {
      return(loglik_mvn(theta_un_obs, Z))
    }))
    barL_cn <- mean(sapply(imps, function(Z) {
      return(loglik_mvn(theta_cn_obs, Z))
    }))
  }

  d_hat <- 2 * (barL_un - barL_cn)

  # ---- tr(RIV) differential for bias correction ----
  # For FIML: analytic computation. For Amelia: we use the analytic version
  # as well for consistency in this first-pass W2 (rather than per-imputation
  # Rubin pooling on each model separately). Can be replaced with sample-based
  # in a follow-up if preregistration §2.4 demands.
  trRIV_un <- tr_riv_analytic(theta_un_obs, mar$Y, mar$R)$tr_RIV
  trRIV_cn <- tr_riv_analytic_constrained_sigma12(theta_cn_obs, mar$Y, mar$R)
  bias_correction <- trRIV_un - trRIV_cn

  LRT_uncorrected <- d_hat                       # C3
  LRT_corrected   <- d_hat - bias_correction     # C2

  return(list(
    delta_r        = delta,
    LRT_oracle     = LRT_oracle,
    LRT_corrected  = LRT_corrected,
    LRT_uncorrected = LRT_uncorrected,
    trRIV_un       = trRIV_un,
    trRIV_cn       = trRIV_cn,
    bias_corr      = bias_correction,
    miss1          = miss1,
    miss2          = miss2,
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
# Rejection rates at alpha = 0.05 against chi^2_1.
# -----------------------------------------------------------------------------

crit_val <- qchisq(0.95, df = 1)
mcse_rate <- function(p, n) { return(sqrt(p * (1 - p) / n)) }

rejection_table <- data.frame(
  delta             = numeric(),
  C1_oracle         = numeric(),
  C2_corrected      = numeric(),
  C3_uncorrected    = numeric(),
  mcse_corrected    = numeric(),
  mcse_uncorrected  = numeric(),
  median_bias_corr  = numeric(),
  median_trRIV_un   = numeric(),
  median_trRIV_cn   = numeric()
)

for (delta_value in cfg$delta_grid) {
  res <- all_results[[as.character(delta_value)]]
  lrt_or <- vapply(res, `[[`, numeric(1), "LRT_oracle")
  lrt_co <- vapply(res, `[[`, numeric(1), "LRT_corrected")
  lrt_un <- vapply(res, `[[`, numeric(1), "LRT_uncorrected")
  bias_c <- vapply(res, `[[`, numeric(1), "bias_corr")
  tr_un  <- vapply(res, `[[`, numeric(1), "trRIV_un")
  tr_cn  <- vapply(res, `[[`, numeric(1), "trRIV_cn")
  rejection_table <- rbind(rejection_table, data.frame(
    delta             = delta_value,
    C1_oracle         = mean(lrt_or > crit_val),
    C2_corrected      = mean(lrt_co > crit_val),
    C3_uncorrected    = mean(lrt_un > crit_val),
    mcse_corrected    = mcse_rate(mean(lrt_co > crit_val), length(lrt_co)),
    mcse_uncorrected  = mcse_rate(mean(lrt_un > crit_val), length(lrt_un)),
    median_bias_corr  = median(bias_c),
    median_trRIV_un   = median(tr_un),
    median_trRIV_cn   = median(tr_cn)
  ))
}

cat("\n== W2 results: rejection rates at alpha = 0.05 (chi^2_1 reference) ==\n\n")
print(rejection_table, row.names = FALSE, digits = 4)

cache_path <- sprintf("verification/cache/W2-%s-%s.rds", mode, engine)
saveRDS(list(
  cfg = cfg, mode = mode, engine = engine, n_cores = n_cores,
  elapsed_total = elapsed_total,
  all_results = all_results,
  rejection_table = rejection_table
), file = cache_path)

cat(sprintf("\nCache: %s\n", cache_path))
