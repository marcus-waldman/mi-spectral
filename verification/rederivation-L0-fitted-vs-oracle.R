# rederivation-L0-fitted-vs-oracle.R
#
# Layer-0/1 grounding experiment for todo/013 (independent re-derivation).
#
# The blind re-derivation produced an 8/9 majority for E[T] = -1/2 tr(RIV),
# the OPPOSITE sign of the manuscript's headline +1/2 tr(RIV). The whole
# disagreement lives in Term A = barQ(theta_obs) - ell_com(theta_obs):
#   * solvers read barQ as the ORACLE conditional expectation E[ell_com|Y_obs]
#     under the TRUE law theta0  ->  tower property  ->  E[A] = 0  ->  T = -1/2.
#   * the manuscript/repo use the FITTED imputation law P(.|Y_obs, theta_obs)
#     (barQ_fiml_analytic's second arg)         ->  E[A] = +tr(RIV) ->  T = +1/2.
#
# This script measures BOTH objects on the repo's own DGP + MAR + primitives,
# so the fork is settled numerically rather than by hand.
#   A_fitted = barQ_fiml_analytic(theta_obs, theta_obs, .) - ell_com(theta_obs)
#   A_oracle = barQ_fiml_analytic(theta_obs, theta_TRUE, .) - ell_com(theta_obs)
# B is common. Prediction: fitted -> +tr/+1/2 ; oracle -> 0/-1/2.
#
# Run: Rscript verification/rederivation-L0-fitted-vs-oracle.R [R] [N] [cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
  library(pbapply)
})

args <- commandArgs(trailingOnly = TRUE)
R = if (length(args) >= 1) { as.integer(args[1]) } else { 4000 }
N = if (length(args) >= 2) { as.integer(args[2]) } else { 200 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

mu0 <- default_mu
Sigma0 <- default_Sigma
theta_true <- list(mu = mu0, Sigma = Sigma0)

# Conditional-entropy object C_n(theta) and the plug-in bias Delta_n (todo/017 C2):
# Delta_n = E[ C_n(theta_obs) - C_n(theta0) ] = 1/2 tr(RIV) + (A)+(C) = E[T_fitted]
# (entropy-Hessian split grad^2 C_n = H_phi + I_mis|obs; two CAS in
# verification/cas-wolfram/verify_term_ac{,_sympy}.py). cond_entropy_Cn is a
# shared primitive in 00-setup.R; the known-variance script is the Delta_n -> 0 anchor.

# ---- (1) Dump the committed W1 caches for cross-reference --------------------
cat("=== Committed W1 caches (engine=fiml) ===\n")
for (f in c("W1-prod-fiml.rds", "W1-prod-fiml-N500.rds",
            "W1-prod-fiml-N1000.rds", "W1-prod-fiml-N2000.rds")) {
  path <- file.path("verification/cache", f)
  if (!file.exists(path)) { next }
  w <- readRDS(path)
  s <- w$summary
  cat(sprintf("%-26s N=%-4d  trRIV=%.3f | Ahat=%+.3f (=%.2f*trRIV) | Bhat=%+.3f (=%.2f*trRIV) | That=%+.3f (=%.2f*trRIV) | passA=%s passB=%s passT=%s\n",
              f, w$cfg$N, s$trRIV_emp,
              s$Ahat, s$Ahat / s$trRIV_emp,
              s$Bhat, s$Bhat / s$trRIV_emp,
              s$That, s$That / s$trRIV_emp,
              s$pass["A"], s$pass["B"], s$pass["T"]))
}
cat("\n")

# ---- (2) Controlled fitted-vs-oracle experiment ------------------------------
run_one <- function(r, N) {
  set.seed(20260522 + r)
  X <- gen_data(N = N, mu = mu0, Sigma = Sigma0)
  theta_com <- mle_complete_mvn(X)
  ell_com_at_com = loglik_mvn(theta_com, X)
  mar <- apply_mar(X)
  em_fit <- em_mvn(mar$Y)
  theta_obs <- list(mu = em_fit$mu, Sigma = em_fit$Sigma)
  ell_com_at_obs = loglik_mvn(theta_obs, X)
  barQ_fitted = barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R)
  barQ_oracle = barQ_fiml_analytic(theta_obs, theta_true, mar$Y, mar$R)
  trRIV = tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  # Conditional-entropy plug-in bias Delta_n = C_n(theta_obs) - C_n(theta0) (C2).
  Delta_n = cond_entropy_Cn(theta_obs, mar$R) - cond_entropy_Cn(theta_true, mar$R)
  return(list(
    A_fitted = barQ_fitted - ell_com_at_obs,
    A_oracle = barQ_oracle - ell_com_at_obs,
    B        = ell_com_at_obs - ell_com_at_com,
    T_fitted = barQ_fitted - ell_com_at_com,
    T_oracle = barQ_oracle - ell_com_at_com,
    Delta_n  = Delta_n,
    trRIV    = trRIV
  ))
}

cat(sprintf("=== Controlled experiment: N=%d, R=%d, cores=%d ===\n", N, R, n_cores))
if (n_cores > 1) {
  cl <- makeCluster(n_cores)
  on.exit(stopCluster(cl), add = TRUE)
  clusterEvalQ(cl, source("verification/00-setup.R"))
  clusterExport(cl, varlist = c("mu0", "Sigma0", "theta_true", "run_one", "N"))
  res <- pblapply(seq_len(R), function(r) { return(run_one(r, N)) }, cl = cl)
} else {
  res <- pblapply(seq_len(R), function(r) { return(run_one(r, N)) })
}

grab <- function(nm) { return(vapply(res, `[[`, numeric(1), nm)) }
A_f <- grab("A_fitted")
A_o <- grab("A_oracle")
B   <- grab("B")
T_f <- grab("T_fitted")
T_o <- grab("T_oracle")
dn  <- grab("Delta_n")
tr  <- grab("trRIV")
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }
mtr = mean(tr)

cat(sprintf("\nmean tr(RIV) = %.4f\n\n", mtr))
cat(sprintf("E[B]        = %+.4f (SE %.4f)   target -1/2 trRIV = %+.4f   ratio B/(-1/2 trRIV) = %.3f\n\n",
            mean(B), mcse(B), -0.5 * mtr, mean(B) / (-0.5 * mtr)))
cat("--- FITTED imputation  P(.|Y_obs, theta_obs)   [repo / manuscript Term A] ---\n")
cat(sprintf("E[A_fitted] = %+.4f (SE %.4f)   target +trRIV    = %+.4f   ratio A/trRIV       = %.3f\n",
            mean(A_f), mcse(A_f), mtr, mean(A_f) / mtr))
cat(sprintf("E[T_fitted] = %+.4f (SE %.4f)   target +1/2 trRIV = %+.4f   ratio T/(1/2 trRIV) = %.3f\n\n",
            mean(T_f), mcse(T_f), 0.5 * mtr, mean(T_f) / (0.5 * mtr)))
cat("--- C2: conditional-entropy plug-in bias Delta_n   [todo/017; should equal E[T_fitted]] ---\n")
cat(sprintf("E[Delta_n]  = %+.4f (SE %.4f)   E[T_fitted]      = %+.4f   ratio Delta_n/T_fitted = %.3f\n",
            mean(dn), mcse(dn), mean(T_f), mean(dn) / mean(T_f)))
cat(sprintf("paired E[T_fitted - Delta_n] = %+.5f (SE %.5f)   [target 0; both = 1/2 trRIV + (A)+(C)]\n",
            mean(T_f - dn), mcse(T_f - dn)))
cat(sprintf("E[Delta_n]/(1/2 trRIV) = %.3f   ((A)+(C) design-imbalance = E[Delta_n] - 1/2 trRIV = %+.4f)\n\n",
            mean(dn) / (0.5 * mtr), mean(dn) - 0.5 * mtr))
cat("--- ORACLE imputation  P(.|Y_obs, theta_TRUE)  [solvers' tower-property Term A] ---\n")
cat(sprintf("E[A_oracle] = %+.4f (SE %.4f)   target 0          (ratio A/trRIV = %.3f)\n",
            mean(A_o), mcse(A_o), mean(A_o) / mtr))
cat(sprintf("E[T_oracle] = %+.4f (SE %.4f)   target -1/2 trRIV = %+.4f   ratio T/(-1/2 trRIV)= %.3f\n",
            mean(T_o), mcse(T_o), -0.5 * mtr, mean(T_o) / (-0.5 * mtr)))
