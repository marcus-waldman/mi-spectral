# W1-sweep.R
#
# W1 bias-decomposition across the comprehensive sweep grid (todo/006 §7).
# Per todo/006 §7, "FIML engine only is fine (W1 result is engine-independent
# for total bias)". The sweep here iterates over the 12 (pattern x mech x N)
# combinations and computes T = bar L_M(theta_obs) - ell_com(theta_com),
# A (imputation bias) = bar L_M(theta_obs) - ell_com(theta_obs), and
# B (estimation mismatch) = ell_com(theta_obs) - ell_com(theta_com), with the
# analytic FIML Q-function (barQ_fiml_analytic) and analytic tr(RIV).
#
# Predicted (theorem): E[T] = +1/2 tr(RIV), E[A] = +tr(RIV),
#                      E[B] = -1/2 tr(RIV).
#
# Usage:
#   Rscript verification/W1-sweep.R <R> <out_suffix> [n_cores]
#
# Cache: verification/cache/W1-sweep-<out_suffix>/<cell-id>.rds + summary.csv.

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args       <- commandArgs(trailingOnly = TRUE)
R_per_cell <- if (length(args) >= 1) { as.integer(args[1]) } else { 200 }
out_suffix <- if (length(args) >= 2) { args[2] } else { "sanity" }
n_cores    <- if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

out_dir <- sprintf("verification/cache/W1-sweep-%s", out_suffix)
if (!dir.exists(out_dir)) { dir.create(out_dir, recursive = TRUE) }

cat(sprintf("\nW1 sweep (FIML, analytic)  [R=%d, out=%s, cores=%d]\n\n",
            R_per_cell, out_suffix, n_cores))

# -----------------------------------------------------------------------------
# Cell grid: 12 (pattern x mech x N) combinations, FIML engine, prop=0.40.
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
      id      = sprintf("fiml_%s_%s_N%d", pat, mech, N),
      pattern = pat, mech = mech, N = N, prop = 0.40
    )
  }
  return(out)
}

cells <- build_cells()
cat(sprintf("Cells: %d\n", length(cells)))


# -----------------------------------------------------------------------------
# Per-replicate work: FIML, analytic Q + analytic tr(RIV).
# -----------------------------------------------------------------------------

run_one_W1 <- function(r, cell, mu0, Sigma0) {
  set.seed(20260522 + r)
  X <- gen_data(N = cell$N, mu = mu0, Sigma = Sigma0)
  theta_com <- mle_complete_mvn(X)
  ell_com_at_com <- loglik_mvn(theta_com, X)

  mar <- tryCatch(apply_missingness_ampute(X, prop = cell$prop,
                                            mech = cell$mech,
                                            pattern_type = cell$pattern),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(list(error = "ampute failed")) }

  # Observed-data MLE via FIML (analysis-model = unrestricted MVN).
  fit_obs <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE),
                      error = function(e) { return(NULL) })
  if (is.null(fit_obs)) { return(list(error = "FIML MLE failed")) }
  theta_obs <- list(mu = fit_obs$mu, Sigma = fit_obs$Sigma)

  ell_com_at_obs <- loglik_mvn(theta_obs, X)
  barL_obs <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R)

  riv_info <- tr_riv_analytic(theta_obs, mar$Y, mar$R)
  trRIV <- riv_info$tr_RIV

  return(list(
    error   = NA_character_,
    T_r     = barL_obs - ell_com_at_com,
    A_r     = barL_obs - ell_com_at_obs,
    B_r     = ell_com_at_obs - ell_com_at_com,
    trRIV_r = trRIV,
    miss1   = mean(mar$R[, 1]),
    miss2   = mean(mar$R[, 2]),
    miss3   = mean(mar$R[, 3]),
    miss4   = mean(mar$R[, 4])
  ))
}


# -----------------------------------------------------------------------------
# Cluster setup.
# -----------------------------------------------------------------------------

if (n_cores > 1) {
  cl <- parallel::makeCluster(n_cores)
  on.exit(parallel::stopCluster(cl), add = TRUE)
  parallel::clusterEvalQ(cl, { invisible(source("verification/00-setup.R")) })
  parallel::clusterExport(cl, varlist = c("run_one_W1"))
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
  cat(sprintf("[%d/%d] %s  ", i, length(cells), cell$id))

  if (!is.null(cl)) {
    parallel::clusterExport(cl, varlist = c("cell"), envir = environment())
  }
  t0 <- Sys.time()
  if (is.null(cl)) {
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_W1(r, cell, default_mu, default_Sigma))
    })
  } else {
    results <- pbapply::pblapply(seq_len(R_per_cell), function(r) {
      return(run_one_W1(r, cell, default_mu, default_Sigma))
    }, cl = cl)
  }
  elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))

  errors <- sapply(results, function(rr) { return(!is.null(rr$error) && !is.na(rr$error)) })
  n_err <- sum(errors); ok <- results[!errors]
  if (length(ok) == 0) {
    summary_rows[[i]] <- data.frame(
      cell_id = cell$id, n_ok = 0, n_err = n_err,
      T_hat = NA, A_hat = NA, B_hat = NA, trRIV = NA,
      half_trRIV_pred = NA, T_minus_pred = NA,
      passT = NA, passA = NA, passB = NA,
      stringsAsFactors = FALSE
    )
    cat(sprintf("FAIL: %d errors\n", n_err))
    next
  }

  T_arr     <- vapply(ok, `[[`, numeric(1), "T_r")
  A_arr     <- vapply(ok, `[[`, numeric(1), "A_r")
  B_arr     <- vapply(ok, `[[`, numeric(1), "B_r")
  trRIV_arr <- vapply(ok, `[[`, numeric(1), "trRIV_r")

  mcse <- function(x) { return(sd(x) / sqrt(length(x))) }
  T_hat <- mean(T_arr); A_hat <- mean(A_arr); B_hat <- mean(B_arr)
  trRIV_emp <- mean(trRIV_arr)
  half      <- 0.5 * trRIV_emp
  neg_half  <- -half

  ci_T <- T_hat + qnorm(c(0.025, 0.975)) * mcse(T_arr)
  ci_A <- A_hat + qnorm(c(0.025, 0.975)) * mcse(A_arr)
  ci_B <- B_hat + qnorm(c(0.025, 0.975)) * mcse(B_arr)
  passT <- ci_T[1] <= half     && half     <= ci_T[2]
  passA <- ci_A[1] <= trRIV_emp && trRIV_emp <= ci_A[2]
  passB <- ci_B[1] <= neg_half && neg_half <= ci_B[2]

  cache_path <- file.path(out_dir, sprintf("%s.rds", cell$id))
  saveRDS(list(
    cell = cell, R_per_cell = R_per_cell, elapsed_sec = elapsed,
    results = results,
    T_arr = T_arr, A_arr = A_arr, B_arr = B_arr, trRIV_arr = trRIV_arr,
    summary = list(T_hat = T_hat, A_hat = A_hat, B_hat = B_hat,
                   trRIV_emp = trRIV_emp,
                   half_trRIV_pred = half,
                   pass = c(T = passT, A = passA, B = passB))
  ), file = cache_path)

  cat(sprintf("done %5.1fs  T=%+6.3f (pred %+6.3f)  trRIV=%5.3f   T:%s A:%s B:%s\n",
              elapsed, T_hat, half, trRIV_emp,
              if (passT) "PASS" else "FAIL",
              if (passA) "PASS" else "FAIL",
              if (passB) "PASS" else "FAIL"))

  summary_rows[[i]] <- data.frame(
    cell_id = cell$id,
    pattern = cell$pattern, mech = cell$mech, N = cell$N,
    n_ok = length(ok), n_err = n_err,
    T_hat = T_hat, A_hat = A_hat, B_hat = B_hat,
    trRIV = trRIV_emp,
    half_trRIV_pred = half,
    T_minus_pred = T_hat - half,
    A_minus_pred = A_hat - trRIV_emp,
    B_minus_pred = B_hat - neg_half,
    passT = passT, passA = passA, passB = passB,
    stringsAsFactors = FALSE
  )
}

elapsed_total <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
cat(sprintf("\nTotal W1 sweep elapsed: %.1fs (%.2f min)\n",
            elapsed_total, elapsed_total / 60))

summary_df <- do.call(rbind, summary_rows)
summary_path <- file.path(out_dir, "summary.csv")
write.csv(summary_df, file = summary_path, row.names = FALSE)
cat(sprintf("\nSummary: %s\n\n", summary_path))

print(summary_df[, c("cell_id", "n_ok", "T_hat", "half_trRIV_pred",
                     "trRIV", "passT", "passA", "passB")],
      row.names = FALSE, digits = 3)
