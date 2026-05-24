# W3-mnar-bias-measurement.R
#
# Direct measurement of theta_obs parameter bias under MAR vs MNAR at the
# W3 DGP (Sigma_truth with sigma_13 = sigma_24 = 0.4, others zero).
# Companion to the comprehensive sweep — answers the question "did our
# MNAR mechanism actually produce substantial parameter bias, or did
# W3's MNAR cells survive because the mechanism happened to be weak?"
#
# Per replicate:
#   1. Generate X ~ MVN(mu_0, Sigma_truth_w3), N rows
#   2. Apply missingness (pattern, mech, prop=0.40) via ampute
#   3. Fit FIML observed-data MLE
#   4. Record theta_obs vector and its deviation from theta_truth
#
# Aggregated across R=2000 replicates per cell:
#   - bias_mu (4-vector), bias_vech_Sigma (10-vector)
#   - ||bias||_2 in raw and standardized (per analytic SE) units
#   - relative magnitudes: how big is MNAR bias vs MAR bias?
#
# Output: verification/cache/mnar-bias-prod/<cell-id>.rds + summary.csv

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args       <- commandArgs(trailingOnly = TRUE)
R_per_cell <- if (length(args) >= 1) { as.integer(args[1]) } else { 2000 }
out_suffix <- if (length(args) >= 2) { args[2] } else { "prod" }
n_cores    <- if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

out_dir <- sprintf("verification/cache/mnar-bias-%s", out_suffix)
if (!dir.exists(out_dir)) { dir.create(out_dir, recursive = TRUE) }

cat(sprintf("\nMNAR bias measurement  [R=%d, out=%s, cores=%d]\n\n",
            R_per_cell, out_suffix, n_cores))

Sigma_truth_w3 <- w3_sigma(rho = 0.4)
theta_truth_vec <- theta_to_vec(list(mu = default_mu, Sigma = Sigma_truth_w3))

PARAM_NAMES <- c(sprintf("mu_%d", 1:4),
                 "sigma_11", "sigma_21", "sigma_31", "sigma_41",
                 "sigma_22", "sigma_32", "sigma_42",
                 "sigma_33", "sigma_43", "sigma_44")
stopifnot(length(theta_truth_vec) == length(PARAM_NAMES))


# -----------------------------------------------------------------------------
# Cells: 12 = (pattern: non_monotone, monotone) x (mech: MAR, MNAR) x N: 200/500/1000.
# -----------------------------------------------------------------------------

build_cells <- function() {
  patterns <- c("non_monotone", "monotone")
  mechs    <- c("MAR", "MNAR")
  Ns       <- c(200, 500, 1000)
  out <- list()
  cid <- 0
  for (pat in patterns) for (mech in mechs) for (N in Ns) {
    cid <- cid + 1
    out[[cid]] <- list(
      id      = sprintf("%s_%s_N%d", pat, mech, N),
      pattern = pat, mech = mech, N = N, prop = 0.40
    )
  }
  return(out)
}

cells <- build_cells()
cat(sprintf("Cells: %d\n", length(cells)))


# -----------------------------------------------------------------------------
# Per-replicate work: gen X, apply missingness, fit FIML, return theta_obs.
# -----------------------------------------------------------------------------

run_one <- function(r, cell, mu0, Sigma_truth) {
  set.seed(20260522 + r)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma_truth)
  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop,
                                            mech = cell$mech,
                                            pattern_type = cell$pattern),
                  error = function(e) NULL)
  if (is.null(mar)) { return(list(error = "ampute")) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE),
                  error = function(e) NULL)
  if (is.null(fit)) { return(list(error = "FIML")) }
  theta_obs_vec <- theta_to_vec(list(mu = fit$mu, Sigma = fit$Sigma))
  return(list(error = NA_character_,
              theta_obs_vec = theta_obs_vec))
}


# -----------------------------------------------------------------------------
# Cluster setup.
# -----------------------------------------------------------------------------

if (n_cores > 1) {
  cl <- parallel::makeCluster(n_cores)
  on.exit(parallel::stopCluster(cl), add = TRUE)
  parallel::clusterEvalQ(cl, { invisible(source("verification/00-setup.R")) })
  parallel::clusterExport(cl, varlist = c("run_one", "Sigma_truth_w3",
                                          "theta_truth_vec", "PARAM_NAMES"))
} else {
  cl <- NULL
}


# -----------------------------------------------------------------------------
# Main loop.
# -----------------------------------------------------------------------------

summary_rows <- list()
t_master <- Sys.time()

for (i in seq_along(cells)) {
  cell <- cells[[i]]
  if (!is.null(cl)) {
    parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
  }
  cat(sprintf("[%d/%d] %s  ", i, length(cells), cell$id))
  t0 <- Sys.time()
  if (is.null(cl)) {
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one(r, cell, default_mu, Sigma_truth_w3))
    })
  } else {
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one(r, cell, default_mu, Sigma_truth_w3))
    }, cl = cl)
  }
  elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
  errors <- sapply(results, function(rr) {
    return(!is.null(rr$error) && !is.na(rr$error))
  })
  ok <- results[!errors]
  n_err <- sum(errors)

  theta_obs_mat <- do.call(rbind,
                           lapply(ok, function(rr) { return(rr$theta_obs_vec) }))
  bias_mean <- colMeans(theta_obs_mat) - theta_truth_vec
  bias_mcse <- apply(theta_obs_mat, 2, sd) / sqrt(nrow(theta_obs_mat))
  bias_z <- bias_mean / bias_mcse  # |z| > 2 indicates significant bias

  # Standardized: bias relative to within-replicate SD of theta_obs estimates
  # (this is the "how many SEs of estimate is the bias" metric, roughly
  # analogous to bias/SE for the MLE itself at finite N).
  sd_estimate <- apply(theta_obs_mat, 2, sd)
  bias_std    <- bias_mean / sd_estimate

  # ||bias||_2 normalized by ||theta_truth||_2 (relative bias).
  norm_bias  <- sqrt(sum(bias_mean^2))
  norm_truth <- sqrt(sum(theta_truth_vec^2))
  rel_bias   <- norm_bias / norm_truth

  # Cross-block bias (sigma_13, sigma_24 which are the load-bearing
  # off-diagonals for W3's true model M_C).
  bias_sigma13 <- bias_mean[which(PARAM_NAMES == "sigma_31")]  # = sigma_13
  bias_sigma24 <- bias_mean[which(PARAM_NAMES == "sigma_42")]  # = sigma_24

  saveRDS(list(cell = cell, R_per_cell = R_per_cell,
               elapsed_sec = elapsed, n_ok = nrow(theta_obs_mat),
               n_err = n_err,
               theta_obs_mat = theta_obs_mat,
               bias_mean = bias_mean, bias_mcse = bias_mcse,
               bias_z = bias_z, bias_std = bias_std,
               PARAM_NAMES = PARAM_NAMES),
          file = file.path(out_dir, sprintf("%s.rds", cell$id)))

  cat(sprintf("done %5.1fs  n_ok=%d n_err=%d  ||bias||=%.3f (rel %.4f)  bias[sigma_13]=%+.3f  bias[sigma_24]=%+.3f\n",
              elapsed, nrow(theta_obs_mat), n_err,
              norm_bias, rel_bias, bias_sigma13, bias_sigma24))

  summary_rows[[i]] <- data.frame(
    cell_id = cell$id, pattern = cell$pattern, mech = cell$mech, N = cell$N,
    n_ok = nrow(theta_obs_mat), n_err = n_err, elapsed_sec = elapsed,
    norm_bias = norm_bias,
    rel_bias  = rel_bias,
    bias_sigma_13 = bias_sigma13,
    bias_sigma_24 = bias_sigma24,
    max_abs_bias_z   = max(abs(bias_z)),
    max_abs_bias_std = max(abs(bias_std)),
    stringsAsFactors = FALSE
  )
}

elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
cat(sprintf("\nTotal elapsed: %.1fs (%.2f min)\n",
            elapsed_total, elapsed_total / 60))

summary_df <- do.call(rbind, summary_rows)
summary_path <- file.path(out_dir, "summary.csv")
write.csv(summary_df, file = summary_path, row.names = FALSE)
cat(sprintf("\nSummary: %s\n\n", summary_path))


# -----------------------------------------------------------------------------
# Headline comparison: MAR vs MNAR bias side-by-side.
# -----------------------------------------------------------------------------

cat("-- MAR vs MNAR bias magnitudes (parameter-level) --\n\n")
print(summary_df[, c("cell_id", "norm_bias", "rel_bias",
                     "bias_sigma_13", "bias_sigma_24",
                     "max_abs_bias_z", "max_abs_bias_std")],
      row.names = FALSE, digits = 4)

cat("\n-- MAR vs MNAR side-by-side --\n")
for (pat in c("non_monotone", "monotone")) {
  for (N in c(200, 500, 1000)) {
    mar  <- summary_df[summary_df$pattern == pat & summary_df$mech == "MAR"  & summary_df$N == N, ]
    mnar <- summary_df[summary_df$pattern == pat & summary_df$mech == "MNAR" & summary_df$N == N, ]
    cat(sprintf("  %-13s N=%4d   MAR ||bias||=%.3f rel=%.4f   MNAR ||bias||=%.3f rel=%.4f   ratio=%.2f\n",
                pat, N, mar$norm_bias, mar$rel_bias,
                mnar$norm_bias, mnar$rel_bias,
                mnar$norm_bias / mar$norm_bias))
  }
}

cat("\nDone.\n")
