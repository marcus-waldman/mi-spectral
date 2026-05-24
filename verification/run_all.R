# run_all.R
#
# Single-entry-point script for the comprehensive sweep. Centralizes
# the W1/W3/H3b/MNAR-bias work that previously lived across 8+ files
# (W1-sweep.R, W3-sweep.R, W3-sweep-rate.R, W3-sweep-rivs-preflight.R,
# W3-sweep-summary.R, W3-mnar-bias-measurement.R,
# 00-test-ampute-vs-apply-mar.R, plus assorted smoke / pilot scripts).
#
# Phases:
#   0. Smoke tests (ampute vs apply_mar + pre-flight tr(RIV) table)
#   1. W1 sweep (theorem validation, FIML analytic)
#   2. W3 main sweep (60 cells: 2 patterns x 2 mechs x 3 N x 5 engine/M/cong)
#   3. H3b rate side experiment (low-rate arm; rate=60% deferred)
#   4. MNAR parameter bias measurement (3 mechs incl. MNAR_targeted)
#   5. Aggregation + hypothesis evaluation + markdown verdicts
#
# Usage:
#   Rscript verification/run_all.R <R> <out_suffix> [phases] [n_cores]
#
# Examples:
#   Rscript verification/run_all.R 100  smoke  all  20    # full R=100 dry run
#   Rscript verification/run_all.R 2000 prod   all  20    # production
#   Rscript verification/run_all.R 2000 prod   "1,2,5" 20 # only phases 1,2,5
#
# Cache layout (after a run with out_suffix=prod):
#   verification/cache/run_all-prod/
#     phase0/           preflight-trRIV.csv
#     phase1-w1/        <cell-id>.rds + summary.csv
#     phase2-w3/        <cell-id>.rds + summary.csv
#     phase3-rate/      <cell-id>.rds + summary.csv
#     phase4-mnar-bias/ <cell-id>.rds + summary.csv
#     phase5/           verdicts.md + combined.csv

source("verification/00-setup.R")
source("verification/_modules/smoke-tests.R")
source("verification/_modules/w1-sweep.R")
source("verification/_modules/w3-sweep.R")
source("verification/_modules/w3-rate.R")
source("verification/_modules/mnar-bias.R")
source("verification/_modules/aggregate.R")

suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})


# -----------------------------------------------------------------------------
# CLI args.
# -----------------------------------------------------------------------------

args <- commandArgs(trailingOnly = TRUE)
R_per_cell <- if (length(args) >= 1) as.integer(args[1]) else 100
out_suffix <- if (length(args) >= 2) args[2] else "smoke"
phases_arg <- if (length(args) >= 3) args[3] else "all"
n_cores    <- if (length(args) >= 4) as.integer(args[4]) else 20

phases <- if (phases_arg == "all") {
  c(0, 1, 2, 3, 4, 5)
} else {
  as.integer(strsplit(phases_arg, ",")[[1]])
}

base_dir <- sprintf("verification/cache/run_all-%s", out_suffix)
if (!dir.exists(base_dir)) dir.create(base_dir, recursive = TRUE)

cat(sprintf("\n=== run_all.R [R=%d, out_suffix=%s, phases=%s, n_cores=%d] ===\n",
            R_per_cell, out_suffix, paste(phases, collapse = ","), n_cores))
cat(sprintf("base cache dir: %s\n", base_dir))


# -----------------------------------------------------------------------------
# Cluster setup (reused across all phases).
# -----------------------------------------------------------------------------

cl <- NULL
if (n_cores > 1) {
  cl <- parallel::makeCluster(n_cores)
  parallel::clusterEvalQ(cl, { invisible(source("verification/00-setup.R")) })
  on.exit({
    if (!is.null(cl)) try(parallel::stopCluster(cl), silent = TRUE)
  }, add = TRUE)
}


# -----------------------------------------------------------------------------
# Run phases in order.
# -----------------------------------------------------------------------------

t_master <- Sys.time()

if (0 %in% phases) {
  smoke <- run_smoke_tests(out_dir = file.path(base_dir, "phase0"))
  if (!smoke$pass) {
    stop("Phase 0 smoke tests failed — aborting before downstream phases.")
  }
}

if (1 %in% phases) {
  run_w1_sweep(R_per_cell, cl, out_dir = file.path(base_dir, "phase1-w1"))
}

if (2 %in% phases) {
  run_w3_sweep(R_per_cell, cl, out_dir = file.path(base_dir, "phase2-w3"))
}

if (3 %in% phases) {
  run_w3_rate(R_per_cell, cl, out_dir = file.path(base_dir, "phase3-rate"))
}

if (4 %in% phases) {
  run_mnar_bias(R_per_cell, cl, out_dir = file.path(base_dir, "phase4-mnar-bias"))
}

if (5 %in% phases) {
  run_aggregate(out_suffix = out_suffix,
                 w1_dir   = file.path(base_dir, "phase1-w1"),
                 w3_dir   = file.path(base_dir, "phase2-w3"),
                 rate_dir = file.path(base_dir, "phase3-rate"),
                 bias_dir = file.path(base_dir, "phase4-mnar-bias"),
                 out_dir  = file.path(base_dir, "phase5"))
}

elapsed <- as.numeric(difftime(Sys.time(), t_master, units = "secs"))
cat(sprintf("\n=== run_all complete: %.1fs (%.2f min) ===\n",
            elapsed, elapsed / 60))
