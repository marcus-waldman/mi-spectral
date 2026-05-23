# W1-bias-decomposition.R
#
# Empirical validation of the Q-function deviance-bias decomposition.
# Preregistered at SHA ddc9037, todo/004-simulation-hypotheses.md §1.
#
# Quantities estimated (anchored to MI-IC v4.5 §3.3 lines 162, 214, 288):
#   T = E[bar L_M(theta_obs) - ell_com(theta_com)]    -> +1/2 tr(RIV)
#   A = E[bar L_M(theta_obs) - ell_com(theta_obs)]    -> +tr(RIV)
#   B = E[ell_com(theta_obs)  - ell_com(theta_com)]   -> -1/2 tr(RIV)
#
# Identity: T = A + B per replicate (within-replicate sanity check).
#
# Usage:
#   Rscript W1-bias-decomposition.R                       # pilot, amelia, 20 cores
#   Rscript W1-bias-decomposition.R pilot fiml            # pilot, fiml, 20 cores
#   Rscript W1-bias-decomposition.R prod                  # prod, amelia, 20 cores
#   Rscript W1-bias-decomposition.R prod amelia 8         # prod, amelia, 8 cores
#   Rscript W1-bias-decomposition.R prod fiml 20 500      # prod cfg with N=500
#   Rscript W1-bias-decomposition.R prod fiml 20 1000     # prod cfg with N=1000
#
# Per-replicate seed governance: set.seed(20260522 + r) inside each worker
# so X^(r) is bit-for-bit identical across engines, modes, and core counts.

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args       <- commandArgs(trailingOnly = TRUE)
mode       <- if (length(args) >= 1) { args[1] } else { "pilot" }
engine     <- if (length(args) >= 2) { args[2] } else { "amelia" }
n_cores    <- if (length(args) >= 3) { as.integer(args[3]) } else { 20 }
N_override <- if (length(args) >= 4) { as.integer(args[4]) } else { NA }

stopifnot(engine %in% c("amelia", "fiml"))

cfg <- switch(mode,
  pilot = list(N = 200, M = 50,  R = 100,  burnin = 100, thin = 50),
  prod  = list(N = 200, M = 200, R = 1000, burnin = 200, thin = 100),
  stop(sprintf("Unknown mode '%s'. Use 'pilot' or 'prod'.", mode))
)
if (!is.na(N_override)) { cfg$N <- N_override }

cat(sprintf("\nW1 bias-decomposition  [mode=%s, engine=%s, cores=%d]\n",
            mode, engine, n_cores))
cat(sprintf("  N=%d   M=%d   R=%d   burnin=%d   thin=%d\n",
            cfg$N, cfg$M, cfg$R, cfg$burnin, cfg$thin))
cat(sprintf("  total imputations: %d\n\n", cfg$M * cfg$R))


# -----------------------------------------------------------------------------
# Single-replicate work. Pure function of r + config + engine + DGP fixtures.
# Returns the per-replicate quantities needed for aggregation.
# -----------------------------------------------------------------------------

run_one_replicate <- function(r, cfg, engine, mu0, Sigma0) {
  set.seed(20260522 + r)

  X <- gen_data(N = cfg$N, mu = mu0, Sigma = Sigma0)

  theta_com <- mle_complete_mvn(X)
  ell_com_at_com <- loglik_mvn(theta_com, X)

  mar <- apply_mar(X)
  miss1 <- mean(mar$R[, 1])
  miss2 <- mean(mar$R[, 2])

  em_fit <- em_mvn(mar$Y)
  theta_obs <- list(mu = em_fit$mu, Sigma = em_fit$Sigma)

  ell_com_at_obs <- loglik_mvn(theta_obs, X)

  if (engine == "amelia") {
    imps <- impute_mvn_amelia(mar$Y, M = cfg$M)
    ll_imp <- sapply(imps, function(Z) { return(loglik_mvn(theta_obs, Z)) })
    barL_obs <- mean(ll_imp)
    mi <- mi_fit_mvn(imps)
    riv <- riv_sample(mi$theta_imps, mi$U_imps)
    trRIV <- riv$tr_RIV
  } else if (engine == "fiml") {
    barL_obs <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R)
    riv_info <- tr_riv_analytic(theta_obs, mar$Y, mar$R)
    trRIV <- riv_info$tr_RIV
  }

  return(list(
    T_r     = barL_obs - ell_com_at_com,
    A_r     = barL_obs - ell_com_at_obs,
    B_r     = ell_com_at_obs - ell_com_at_com,
    trRIV_r = trRIV,
    miss1_r = miss1,
    miss2_r = miss2
  ))
}


# -----------------------------------------------------------------------------
# Dispatch: parallel via PSOCK cluster if n_cores > 1, serial otherwise.
# -----------------------------------------------------------------------------

t0 <- Sys.time()

if (n_cores > 1) {
  cl <- parallel::makeCluster(n_cores)
  on.exit(parallel::stopCluster(cl), add = TRUE)
  parallel::clusterEvalQ(cl, {
    source("verification/00-setup.R")
  })
  parallel::clusterExport(cl, varlist = c("cfg", "engine", "run_one_replicate"))
  results <- pbapply::pblapply(seq_len(cfg$R), function(r) {
    return(run_one_replicate(r, cfg, engine, default_mu, default_Sigma))
  }, cl = cl)
} else {
  results <- pbapply::pblapply(seq_len(cfg$R), function(r) {
    return(run_one_replicate(r, cfg, engine, default_mu, default_Sigma))
  })
}

elapsed_total <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("\nDone in %.1f seconds.\n\n", elapsed_total))


# -----------------------------------------------------------------------------
# Re-shape per-replicate results.
# -----------------------------------------------------------------------------

rep_T     <- vapply(results, `[[`, numeric(1), "T_r")
rep_A     <- vapply(results, `[[`, numeric(1), "A_r")
rep_B     <- vapply(results, `[[`, numeric(1), "B_r")
rep_trRIV <- vapply(results, `[[`, numeric(1), "trRIV_r")
rep_miss1 <- vapply(results, `[[`, numeric(1), "miss1_r")
rep_miss2 <- vapply(results, `[[`, numeric(1), "miss2_r")


# -----------------------------------------------------------------------------
# Aggregate.
# -----------------------------------------------------------------------------

mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

That      <- mean(rep_T)
Ahat      <- mean(rep_A)
Bhat      <- mean(rep_B)
trRIV_emp <- mean(rep_trRIV)

half_trRIV     <- 0.5 * trRIV_emp
neg_half_trRIV <- -0.5 * trRIV_emp

z_T <- (That - half_trRIV)      / mcse(rep_T)
z_A <- (Ahat - trRIV_emp)       / mcse(rep_A)
z_B <- (Bhat - neg_half_trRIV)  / mcse(rep_B)

ci_T <- That + qnorm(c(0.025, 0.975)) * mcse(rep_T)
ci_A <- Ahat + qnorm(c(0.025, 0.975)) * mcse(rep_A)
ci_B <- Bhat + qnorm(c(0.025, 0.975)) * mcse(rep_B)

passT <- ci_T[1] <= half_trRIV     && half_trRIV     <= ci_T[2]
passA <- ci_A[1] <= trRIV_emp      && trRIV_emp      <= ci_A[2]
passB <- ci_B[1] <= neg_half_trRIV && neg_half_trRIV <= ci_B[2]

identity_check <- max(abs(rep_T - (rep_A + rep_B)))

cat("== W1 results ==\n\n")
cat(sprintf("Empirical tr(RIV) (mean across replicates) = %.4f (MCSE %.4f)\n",
            trRIV_emp, mcse(rep_trRIV)))
cat(sprintf("Marginal missingness: X_1 = %.3f, X_2 = %.3f\n",
            mean(rep_miss1), mean(rep_miss2)))
cat(sprintf("Within-replicate identity max |T - (A+B)| = %.2e (should be 0)\n\n",
            identity_check))

cat("Quantity   Empirical (MCSE)     Predicted               z       95% CI                       Pass\n")
cat("--------   ------------------   --------------------    -----   --------------------------   ----\n")
cat(sprintf("T (total)  %+8.4f (%.4f)    +1/2 tr(RIV) = %+7.4f    %+5.2f   [%+8.4f, %+8.4f]    %s\n",
            That, mcse(rep_T), half_trRIV, z_T, ci_T[1], ci_T[2],
            if (passT) { "PASS" } else { "FAIL" }))
cat(sprintf("A (imp.b.) %+8.4f (%.4f)        tr(RIV) = %+7.4f    %+5.2f   [%+8.4f, %+8.4f]    %s\n",
            Ahat, mcse(rep_A), trRIV_emp, z_A, ci_A[1], ci_A[2],
            if (passA) { "PASS" } else { "FAIL" }))
cat(sprintf("B (est.m.) %+8.4f (%.4f)    -1/2 tr(RIV) = %+7.4f    %+5.2f   [%+8.4f, %+8.4f]    %s\n",
            Bhat, mcse(rep_B), neg_half_trRIV, z_B, ci_B[1], ci_B[2],
            if (passB) { "PASS" } else { "FAIL" }))

cache_suffix <- if (!is.na(N_override)) { sprintf("-N%d", cfg$N) } else { "" }
cache_path <- sprintf("verification/cache/W1-%s-%s%s.rds", mode, engine, cache_suffix)
saveRDS(list(
  cfg = cfg, mode = mode, engine = engine, n_cores = n_cores,
  elapsed_total = elapsed_total,
  rep_T = rep_T, rep_A = rep_A, rep_B = rep_B, rep_trRIV = rep_trRIV,
  rep_miss1 = rep_miss1, rep_miss2 = rep_miss2,
  summary = list(That = That, Ahat = Ahat, Bhat = Bhat,
                 trRIV_emp = trRIV_emp,
                 mcse = c(T = mcse(rep_T), A = mcse(rep_A), B = mcse(rep_B),
                          trRIV = mcse(rep_trRIV)),
                 pass = c(T = passT, A = passA, B = passB))
), file = cache_path)

cat(sprintf("\nCache: %s\n", cache_path))
