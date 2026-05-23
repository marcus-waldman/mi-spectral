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
#   Rscript verification/W1-bias-decomposition.R                # pilot, amelia
#   Rscript verification/W1-bias-decomposition.R pilot fiml     # pilot, fiml-analytic
#   Rscript verification/W1-bias-decomposition.R prod           # full, amelia (preregistered primary)
#   Rscript verification/W1-bias-decomposition.R prod fiml      # full, fiml-analytic (cross-check)
#
# Engines per preregistration §0.3 Amendment 1 (2026-05-22):
#   amelia : Amelia II EMB — primary preregistered engine.
#   fiml   : analytic FIML-marginalized Q-function — cross-check, no MC.
#
# `norm::da.norm` was the original §0.3 engine but was deprecated in
# Amendment 1 after the pilot showed Term 1 ~5x too small; not exposed here.
#
# Output: writes a tidy summary to verification/cache/W1-<mode>-<engine>.rds
# and echoes the comparison table to stdout.
#
# Per-replicate seed governance: set.seed(20260522 + r) inside the loop so
# X^(r) is bit-for-bit identical across engines and modes.

source("verification/00-setup.R")

args <- commandArgs(trailingOnly = TRUE)
mode   <- if (length(args) >= 1) { args[1] } else { "pilot" }
engine <- if (length(args) >= 2) { args[2] } else { "amelia" }

stopifnot(engine %in% c("amelia", "fiml"))

cfg <- switch(mode,
  pilot = list(N = 200, M = 50,  R = 100,  burnin = 100, thin = 50),
  prod  = list(N = 200, M = 200, R = 1000, burnin = 200, thin = 100),
  stop(sprintf("Unknown mode '%s'. Use 'pilot' or 'prod'.", mode))
)

cat(sprintf("\nW1 bias-decomposition  [mode=%s, engine=%s]\n", mode, engine))
cat(sprintf("  N=%d   M=%d   R=%d   burnin=%d   thin=%d\n",
            cfg$N, cfg$M, cfg$R, cfg$burnin, cfg$thin))
cat(sprintf("  total imputations: %d\n\n", cfg$M * cfg$R))

# Pre-allocate per-replicate storage.
rep_T <- numeric(cfg$R)
rep_A <- numeric(cfg$R)
rep_B <- numeric(cfg$R)
rep_trRIV <- numeric(cfg$R)
rep_miss1 <- numeric(cfg$R)
rep_miss2 <- numeric(cfg$R)

t0 <- Sys.time()
for (r in seq_len(cfg$R)) {
  # Per-replicate seed: identical X^(r) across engines regardless of how many
  # base-R RNG draws each engine consumes after data generation.
  set.seed(20260522 + r)

  # 1. Generate complete data.
  X <- gen_data(N = cfg$N, mu = default_mu, Sigma = default_Sigma)

  # 2. Complete-data MLE and its log-likelihood on X.
  theta_com <- mle_complete_mvn(X)
  ell_com_at_com <- loglik_mvn(theta_com, X)

  # 3. Apply MAR mask.
  mar <- apply_mar(X)
  rep_miss1[r] <- mean(mar$R[, 1])
  rep_miss2[r] <- mean(mar$R[, 2])

  # 4. Observed-data MLE via EM (= FIML estimate).
  em_fit <- em_mvn(mar$Y)
  theta_obs <- list(mu = em_fit$mu, Sigma = em_fit$Sigma)

  # 5. ell_com evaluated at theta_obs (uses the original complete X).
  ell_com_at_obs <- loglik_mvn(theta_obs, X)

  # 6 & 7. bar_L_M(theta_obs) — engine paths.
  if (engine == "amelia") {
    imps <- impute_mvn_amelia(mar$Y, M = cfg$M)
    ll_imp <- sapply(imps, function(Z) { return(loglik_mvn(theta_obs, Z)) })
    barL_obs <- mean(ll_imp)
  } else if (engine == "fiml") {
    # Closed-form bar_Q_inf at theta_obs under deterministic FIML imputation.
    barL_obs <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R)
    imps <- NULL  # no imputations under this path
  }

  # 8. Per-replicate quantities (T = A + B by construction).
  rep_T[r] <- barL_obs - ell_com_at_com
  rep_A[r] <- barL_obs - ell_com_at_obs
  rep_B[r] <- ell_com_at_obs - ell_com_at_com

  # 9. tr(RIV) — engine-dependent path.
  if (engine == "fiml") {
    # Analytic tr(RIV) from MVN information matrices at theta_obs.
    riv_info <- tr_riv_analytic(theta_obs, mar$Y, mar$R)
    rep_trRIV[r] <- riv_info$tr_RIV
  } else {
    mi <- mi_fit_mvn(imps)
    riv <- riv_sample(mi$theta_imps, mi$U_imps)
    rep_trRIV[r] <- riv$tr_RIV
  }

  if (r %% max(1, cfg$R %/% 10) == 0) {
    elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
    eta <- elapsed * (cfg$R - r) / r
    cat(sprintf("  r=%d/%d  elapsed=%.1fs  eta=%.1fs\n",
                r, cfg$R, elapsed, eta))
  }
}

elapsed_total <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("\nDone in %.1f seconds.\n\n", elapsed_total))

# Aggregate.
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

That <- mean(rep_T)
Ahat <- mean(rep_A)
Bhat <- mean(rep_B)
trRIV_emp <- mean(rep_trRIV)

half_trRIV <- 0.5 * trRIV_emp
neg_half_trRIV <- -0.5 * trRIV_emp

z_T <- (That - half_trRIV)      / mcse(rep_T)
z_A <- (Ahat - trRIV_emp)       / mcse(rep_A)
z_B <- (Bhat - neg_half_trRIV)  / mcse(rep_B)

# CI containment check (preregistered pass criterion: 95% MC CI contains predicted).
ci_T <- That + qnorm(c(0.025, 0.975)) * mcse(rep_T)
ci_A <- Ahat + qnorm(c(0.025, 0.975)) * mcse(rep_A)
ci_B <- Bhat + qnorm(c(0.025, 0.975)) * mcse(rep_B)

passT <- ci_T[1] <= half_trRIV     && half_trRIV     <= ci_T[2]
passA <- ci_A[1] <= trRIV_emp      && trRIV_emp      <= ci_A[2]
passB <- ci_B[1] <= neg_half_trRIV && neg_half_trRIV <= ci_B[2]

# Within-replicate identity check: T_r = A_r + B_r exactly.
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

cache_path <- sprintf("verification/cache/W1-%s-%s.rds", mode, engine)
saveRDS(list(
  cfg = cfg, mode = mode, engine = engine, elapsed_total = elapsed_total,
  rep_T = rep_T, rep_A = rep_A, rep_B = rep_B, rep_trRIV = rep_trRIV,
  rep_miss1 = rep_miss1, rep_miss2 = rep_miss2,
  summary = list(That = That, Ahat = Ahat, Bhat = Bhat,
                 trRIV_emp = trRIV_emp,
                 mcse = c(T = mcse(rep_T), A = mcse(rep_A), B = mcse(rep_B),
                          trRIV = mcse(rep_trRIV)),
                 pass = c(T = passT, A = passA, B = passB))
), file = cache_path)

cat(sprintf("\nCache: %s\n", cache_path))
