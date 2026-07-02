# spikes/phase0a-da-conjugate.R
#
# Phase-0 spike 0a (todo/040): smoke-test the hand-rolled conjugate DA imputer
# on the W1 theorem cell, R=100, and check the pass criteria fixed in todo/040 §4:
#   G0a-1  conjugate sample tr(RIV) ~ analytic tr(RIV) within MC error
#   G0a-2  conjugate T_hat contains +1/2 * (sample tr(RIV)) in its 95% MC CI
#   G0a-3  conjugate T_hat agrees with Amelia T_hat (paired, same mar$Y)
#   G0a-4  zero non-PSD events across the 20 workers; RNG bit-reproducible
#
# Apples-to-apples with the frozen original W1: default DGP, N=200, apply_mar(X)
# (non-monotone, X1/X2 driven by X3/X4), theta_obs = EM observed-data MLE. All
# three engines scored on the SAME mar$Y per replicate (paired).
#
# Usage:
#   Rscript verification/spikes/phase0a-da-conjugate.R [R] [n_cores] [M] [burnin] [thin]

source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")
suppressPackageStartupMessages({ library(parallel); library(pbapply) })

args    <- commandArgs(trailingOnly = TRUE)
R_reps  <- if (length(args) >= 1) as.integer(args[1]) else 100
n_cores <- if (length(args) >= 2) as.integer(args[2]) else 20
M       <- if (length(args) >= 3) as.integer(args[3]) else 50
burnin  <- if (length(args) >= 4) as.integer(args[4]) else 100
thin    <- if (length(args) >= 5) as.integer(args[5]) else 50

cat(sprintf("\nPhase-0a conjugate DA spike  [R=%d, cores=%d, M=%d, burnin=%d, thin=%d]\n",
            R_reps, n_cores, M, burnin, thin))
cat(sprintf("  cell: W1 theorem, N=200, apply_mar, theta_obs=EM MLE\n\n"))


run_one_0a <- function(r, M, burnin, thin, mu0, Sigma0) {
  set.seed(20260522 + r)                          # W1 seed governance
  X <- gen_data(N = 200, mu = mu0, Sigma = Sigma0)
  theta_com <- mle_complete_mvn(X)
  ell_com_at_com <- loglik_mvn(theta_com, X)
  mar <- apply_mar(X)
  em_fit <- em_mvn(mar$Y)
  theta_obs <- list(mu = em_fit$mu, Sigma = em_fit$Sigma)
  ell_com_at_obs <- loglik_mvn(theta_obs, X)

  # Analytic tr(RIV) at theta_obs.
  trRIV_analytic <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV

  # (i) Conjugate DA.
  cj <- impute_mvn_conjugate(mar$Y, M = M, burnin = burnin, thin = thin,
                             theta_init = theta_obs)
  barL_c <- mean(vapply(cj$imputed, function(Z) loglik_mvn(theta_obs, Z), numeric(1)))
  mi_c <- mi_fit_mvn(cj$imputed)
  trRIV_c <- riv_sample(mi_c$theta_imps, mi_c$U_imps)$tr_RIV

  # (ii) Amelia (same mar$Y).
  amelia_ok <- TRUE
  barL_a <- NA; trRIV_a <- NA
  a <- tryCatch(impute_mvn_amelia(mar$Y, M = M), error = function(e) NULL)
  if (is.null(a)) {
    amelia_ok <- FALSE
  } else {
    barL_a <- mean(vapply(a, function(Z) loglik_mvn(theta_obs, Z), numeric(1)))
    mi_a <- mi_fit_mvn(a)
    trRIV_a <- riv_sample(mi_a$theta_imps, mi_a$U_imps)$tr_RIV
  }

  return(list(
    # conjugate
    T_c = barL_c - ell_com_at_com,
    A_c = barL_c - ell_com_at_obs,
    B_c = ell_com_at_obs - ell_com_at_com,
    trRIV_c = trRIV_c,
    psd_fail = cj$psd_fail,
    # amelia
    T_a = if (amelia_ok) barL_a - ell_com_at_com else NA,
    trRIV_a = trRIV_a,
    amelia_ok = amelia_ok,
    # analytic
    trRIV_analytic = trRIV_analytic
  ))
}

t0 <- Sys.time()
if (n_cores > 1) {
  cl <- parallel::makeCluster(n_cores)
  on.exit(parallel::stopCluster(cl), add = TRUE)
  parallel::clusterEvalQ(cl, {
    source("verification/00-setup.R")
    source("verification/da-conjugate-engine.R")
  })
  parallel::clusterExport(cl, varlist = c("run_one_0a", "M", "burnin", "thin"))
  results <- pbapply::pblapply(seq_len(R_reps), function(r) {
    return(run_one_0a(r, M, burnin, thin, default_mu, default_Sigma))
  }, cl = cl)
} else {
  results <- pbapply::pblapply(seq_len(R_reps), function(r) {
    return(run_one_0a(r, M, burnin, thin, default_mu, default_Sigma))
  })
}
elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("\nDone in %.1fs.\n\n", elapsed))

grab <- function(nm) { return(vapply(results, function(x) x[[nm]], numeric(1))) }
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

T_c <- grab("T_c"); A_c <- grab("A_c"); B_c <- grab("B_c")
trRIV_c <- grab("trRIV_c"); trRIV_an <- grab("trRIV_analytic")
psd_fail <- grab("psd_fail")
amelia_ok <- vapply(results, function(x) x$amelia_ok, logical(1))
T_a <- grab("T_a"); trRIV_a <- grab("trRIV_a")

# --- G0a-1: conjugate sample tr(RIV) vs analytic tr(RIV) ---
d_riv <- trRIV_c - trRIV_an                       # paired difference
d_riv_mean <- mean(d_riv); d_riv_mcse <- mcse(d_riv)
G0a1 <- abs(d_riv_mean) <= 2 * d_riv_mcse

# --- G0a-2: conjugate T_hat contains +1/2 sample tr(RIV) ---
That_c <- mean(T_c); half_c <- 0.5 * mean(trRIV_c)
ci_Tc <- That_c + qnorm(c(0.025, 0.975)) * mcse(T_c)
G0a2 <- ci_Tc[1] <= half_c && half_c <= ci_Tc[2]

# --- G0a-3: conjugate vs Amelia T_hat (paired) ---
ok <- amelia_ok
d_T <- T_c[ok] - T_a[ok]
d_T_mean <- mean(d_T); d_T_mcse <- mcse(d_T)
G0a3 <- abs(d_T_mean) <= 2 * d_T_mcse

# --- G0a-4: PSD/RNG stability ---
psd_total <- sum(psd_fail)
# RNG bit-reproducibility: re-run rep 1 twice in the master process.
rep1a <- run_one_0a(1, M, burnin, thin, default_mu, default_Sigma)
rep1b <- run_one_0a(1, M, burnin, thin, default_mu, default_Sigma)
rng_ok <- identical(rep1a$trRIV_c, rep1b$trRIV_c) && identical(rep1a$T_c, rep1b$T_c)
G0a4 <- (psd_total == 0) && rng_ok

cat("== Phase-0a results ==\n\n")
cat(sprintf("Replicates: %d ok (Amelia ok in %d)\n", R_reps, sum(amelia_ok)))
cat(sprintf("Conjugate DA:  T=%+7.4f (MCSE %.4f)   A=%+7.4f   B=%+7.4f\n",
            That_c, mcse(T_c), mean(A_c), mean(B_c)))
cat(sprintf("  sample tr(RIV) = %.4f (MCSE %.4f)\n", mean(trRIV_c), mcse(trRIV_c)))
cat(sprintf("  analytic tr(RIV) = %.4f (MCSE %.4f)\n", mean(trRIV_an), mcse(trRIV_an)))
cat(sprintf("Amelia:        T=%+7.4f (MCSE %.4f)   sample tr(RIV) = %.4f\n\n",
            mean(T_a[ok]), mcse(T_a[ok]), mean(trRIV_a[ok])))

cat("Gate     Check                                            Value                          Pass\n")
cat("-------  -----------------------------------------------  -----------------------------  ----\n")
cat(sprintf("G0a-1    sample tr(RIV) - analytic (paired)               %+7.4f (2*MCSE %.4f)      %s\n",
            d_riv_mean, 2 * d_riv_mcse, if (G0a1) "PASS" else "FAIL"))
cat(sprintf("G0a-2    T_hat contains +1/2 sample tr(RIV)               pred %+7.4f in [%+.4f,%+.4f]  %s\n",
            half_c, ci_Tc[1], ci_Tc[2], if (G0a2) "PASS" else "FAIL"))
cat(sprintf("G0a-3    T_conjugate - T_amelia (paired)                  %+7.4f (2*MCSE %.4f)      %s\n",
            d_T_mean, 2 * d_T_mcse, if (G0a3) "PASS" else "FAIL"))
cat(sprintf("G0a-4    PSD events=%d ; RNG bit-reproducible=%s                                     %s\n",
            psd_total, rng_ok, if (G0a4) "PASS" else "FAIL"))

all_pass <- G0a1 && G0a2 && G0a3 && G0a4
cat(sprintf("\nPhase-0a overall: %s\n", if (all_pass) "ALL PASS" else "SEE FAILS"))

dir.create("verification/cache/spikes", recursive = TRUE, showWarnings = FALSE)
saveRDS(list(args = list(R = R_reps, M = M, burnin = burnin, thin = thin),
             elapsed = elapsed, results = results,
             gates = c(G0a1 = G0a1, G0a2 = G0a2, G0a3 = G0a3, G0a4 = G0a4),
             summary = list(That_c = That_c, half_c = half_c,
                            trRIV_c = mean(trRIV_c), trRIV_an = mean(trRIV_an),
                            T_amelia = mean(T_a[ok]), trRIV_amelia = mean(trRIV_a[ok]),
                            psd_total = psd_total, rng_ok = rng_ok)),
        file = "verification/cache/spikes/phase0a-da-conjugate.rds")
cat("\nCache: verification/cache/spikes/phase0a-da-conjugate.rds\n")
