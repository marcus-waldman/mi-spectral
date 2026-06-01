# remainder-rate.R
#
# Confirms the theorem's O(1/n) remainder for the MC-RESOLVABLE component.
#
# E[T] = +1/2 tr(RIV_obs) + O(1/n), with T = A + B (derivation.qmd @eq-theorem).
# Term B = ell_com(theta_obs) - ell_com(theta_com) is a weighted-chi^2 quadratic form:
# O(1) variance, so its remainder  r_B(n) = E[B] + 1/2 tr(RIV_obs)  is cleanly estimable
# and its decay rate is fittable. Term A's variance grows as O(n) while its remainder
# shrinks as O(1/n), so the A-remainder ((A)+(C)) is NOT MC-resolvable at feasible R --
# it is established analytically (the (A)+(C) cancellation; derivation.qmd Appendix B/C).
#
# This script fits, on a log-spaced n grid, the decay exponent of two low-variance
# O(1/n) quantities (WLS log-log, averaging per n before logging, as in phase 7):
#   r_B   = E[B] + 1/2 tr(RIV_obs)                    (Term B remainder)
#   r_L2  = tr(I_com Var[gap]) - tr(RIV_obs)          (the L2 finite-n discrepancy,
#                                                      = -2 r_B to leading order)
# b ~ -1 confirms O(1/n). The noisy A and T remainders are reported per n descriptively.
#
# Engine: FIML / analytic (no imputations). Usage:
#   Rscript verification/remainder-rate.R [R] [n_cores]
#   R       replicates per n  (default 20000; B is low-variance but the remainder is small)

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })

args <- commandArgs(trailingOnly = TRUE)
R_per_N = if (length(args) >= 1) { as.integer(args[1]) } else { 20000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }

p = length(default_mu)
k = p + p * (p + 1) / 2

run_one <- function(r, N) {
  set.seed(20260522 + r)
  theta_true <- list(mu = default_mu, Sigma = default_Sigma)
  X <- gen_data(N, default_mu, default_Sigma)
  tc <- mle_complete_mvn(X)
  ll_com_com = loglik_mvn(tc, X)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR",
                                           pattern_type = "non_monotone"),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE),
                  error = function(e) { return(NULL) })
  if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  O_obs <- observed_info_obs_mvn(to, mar$Y, mar$R)
  I_com <- fisher_info_com_mvn(to, N)
  tr_obs = sum(diag(solve(O_obs, I_com))) - k
  A_rb = barQ_fiml_analytic(to, to, mar$Y, mar$R) -
         barQ_fiml_analytic(to, theta_true, mar$Y, mar$R)
  B = loglik_mvn(to, X) - ll_com_com
  return(list(A = A_rb, B = B, tr_obs = tr_obs,
              gap = theta_to_vec(to) - theta_to_vec(tc)))
}

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("run_one", "p", "k"))

Ns = round(exp(seq(log(60), log(1200), length.out = 8)))
cat(sprintf("\n== remainder-rate (R=%d/n, FIML, ampute non_monotone MAR 40%%) ==\n", R_per_N))
cat(sprintf("log-spaced n grid: %s\n\n", paste(Ns, collapse = ", ")))
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

rB_mean <- numeric(length(Ns)); rB_se <- numeric(length(Ns))
rL2 <- numeric(length(Ns))
cat(sprintf("%6s %12s %10s %10s | %12s %12s %12s\n",
            "n", "r_B=E[B]+tr/2", "r_B_se", "r_L2", "E[A]-tr", "E[B]", "tr_obs"))
for (j in seq_along(Ns)) {
  N <- Ns[j]; clusterExport(cl, "N")
  res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_per_N), function(r) { return(run_one(r, N)) }))
  A <- vapply(res, `[[`, numeric(1), "A")
  B <- vapply(res, `[[`, numeric(1), "B")
  trO <- vapply(res, `[[`, numeric(1), "tr_obs")
  G <- do.call(rbind, lapply(res, `[[`, "gap"))
  to = mean(trO)
  I_com_true <- fisher_info_com_mvn(list(mu = default_mu, Sigma = default_Sigma), N)
  gap_riv = sum(diag(I_com_true %*% cov(G)))
  rB = mean(B) + 0.5 * to
  rB_mean[j] = rB; rB_se[j] = mcse(B)            # B's MCSE dominates r_B's MCSE
  rL2[j] = gap_riv - to
  cat(sprintf("%6d %12.4f %10.4f %10.4f | %12.3f %12.3f %12.3f\n",
              N, rB, mcse(B), rL2[j], mean(A) - to, mean(B), to))
}

# WLS log-log fits of |r_B| and |r_L2| (both expected O(1/n), low variance).
fit_rate <- function(y, se, Ns, label) {
  ya <- abs(y); w <- (ya / se)^2
  f <- lm(log(ya) ~ log(Ns), weights = w)
  b <- unname(coef(f)[2]); ci <- unname(confint(f)[2, ])
  cat(sprintf("  %-22s b = %+.3f  (95%% CI [%+.3f, %+.3f])   [b=-1 is O(1/n)]\n",
              label, b, ci[1], ci[2]))
  return(b)
}
cat("\n-- fitted decay exponents (WLS log-log) --\n")
fit_rate(rB_mean, rB_se, Ns, "r_B = E[B]+tr/2")
fit_rate(rL2, pmax(rB_se, 1e-6), Ns, "r_L2 = gapRIV - tr_obs")
cat("\n(Term A remainder (A)+(C) is not MC-resolvable -- variance O(n), remainder O(1/n);\n",
    " established analytically by the (A)+(C) cancellation, derivation.qmd Appendix B/C.)\n", sep = "")
