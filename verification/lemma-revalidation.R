# lemma-revalidation.R
#
# Revalidates the derivation's asymptotic lemmas L1-L3 and the one-RIV result
# against the CROSS-INCLUSIVE OBSERVED information (observed_info_obs_mvn), not
# the naive block-diagonal form (fisher_info_obs_mvn). Standalone, reproducible
# home for the diagnostics that were run as scratch on 2026-05-31 and are quoted
# in todo/008 and manuscript/derivation.qmd (@sec-riv, the note after @eq-combine,
# the Term A scope note).
#
# Background: under MAR the observed-data information carries a mean x covariance
# cross term (Kenward & Molenberghs 1998, Sec 3.2); the naive block-diagonal form
# omits it. The derivation's RIV uses the observed-data information. This script
# confirms that the lemmas hold against THAT information:
#
#   L1   Var(theta_obs)            = I_obs^-1        =>  tr(O_obs . Var[obs]) ~ k
#   L3   Cov(theta_obs, theta_com) = I_com^-1        =>  tr(I_com . Cov[obs,com]) ~ k
#   L2   Var(theta_obs - theta_com)= I_obs^-1-I_com^-1 => tr(I_com . Var[gap]) ~ tr(RIV_obs)
#   one-RIV   E[A] ~ +tr(RIV_obs),  E[B] ~ -1/2 tr(RIV_obs)   (both on the SAME RIV)
#
# where O_obs = observed info, I_com = complete info, RIV_obs = tr(O_obs^-1 I_com)-k.
# The naive contrast tr(E_naive . Var[obs]) and RIV_naive are reported alongside;
# they do NOT match (the cross term matters).
#
# Usage:  Rscript verification/lemma-revalidation.R [R] [n_cores]
#   R        replicates per N      (default 8000)
#   n_cores  PSOCK workers         (default 20)
# Cells: ampute non_monotone MAR 40%, N in {500, 2000}. Seed 20260522 + r.

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })

args <- commandArgs(trailingOnly = TRUE)
R_per_N = if (length(args) >= 1) { as.integer(args[1]) } else { 8000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }

p = length(default_mu)
k = p + p * (p + 1) / 2

# theta as the (mu, vech Sigma) vector in the column-major lower-triangle order
# that the info matrices in 00-setup use.
vech_lt <- function(S) {
  v <- numeric(0)
  for (j in 1:p) { for (i in j:p) { v <- c(v, S[i, j]) } }
  return(v)
}
theta_vec <- function(mu, S) { return(c(mu, vech_lt(S))) }

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
  # Rao-Blackwellized FIML A and the elementary B.
  A_rb = barQ_fiml_analytic(to, to, mar$Y, mar$R) -
         barQ_fiml_analytic(to, theta_true, mar$Y, mar$R)
  B = loglik_mvn(to, X) - ll_com_com
  return(list(
    th_obs = theta_vec(to$mu, to$Sigma),
    th_com = theta_vec(tc$mu, tc$Sigma),
    O  = observed_info_obs_mvn(to, mar$Y, mar$R),   # cross-inclusive observed info
    E  = fisher_info_obs_mvn(to, mar$Y, mar$R),     # naive block-diagonal
    Ic = fisher_info_com_mvn(to, N),                # complete info
    A_rb = A_rb, B = B))
}

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("run_one", "theta_vec", "vech_lt", "p"))

cat(sprintf("\n== lemma-revalidation (R=%d/N, ampute non_monotone MAR 40%%) ==\n", R_per_N))
for (N in c(500, 2000)) {
  clusterExport(cl, "N")
  res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_per_N), function(r) { return(run_one(r, N)) }))
  TO <- do.call(rbind, lapply(res, `[[`, "th_obs"))
  TC <- do.call(rbind, lapply(res, `[[`, "th_com"))
  Ob <- Reduce(`+`, lapply(res, `[[`, "O")) / length(res)
  Eb <- Reduce(`+`, lapply(res, `[[`, "E")) / length(res)
  Icb <- Reduce(`+`, lapply(res, `[[`, "Ic")) / length(res)
  Vo <- cov(TO); Vg <- cov(TO - TC); Coc <- cov(TO, TC); Vc <- cov(TC)
  riv_o = sum(diag(solve(Ob, Icb))) - k
  riv_n = sum(diag(solve(Eb, Icb))) - k
  A_rb <- vapply(res, `[[`, numeric(1), "A_rb")
  B_arr <- vapply(res, `[[`, numeric(1), "B")
  cat(sprintf("\n--- N=%d (R=%d) ---  RIV_obs=%.3f  RIV_naive=%.3f\n",
              N, length(res), riv_o, riv_n))
  cat(sprintf("  L1   tr(O_obs   . Var[obs])  = %7.3f   [= k=%d if Var(obs)=O_obs^-1]\n",
              sum(diag(Ob %*% Vo)), k))
  cat(sprintf("  L1n  tr(E_naive . Var[obs])  = %7.3f   [= k if Var(obs)=E_naive^-1 -- it is not]\n",
              sum(diag(Eb %*% Vo))))
  cat(sprintf("  L3   tr(I_com   . Cov[o,c])  = %7.3f   [= k=%d if Cov=I_com^-1]\n",
              sum(diag(Icb %*% Coc)), k))
  cat(sprintf("  L2   tr(I_com   . Var[gap])  = %7.3f   [= RIV_obs %.3f if Var(gap)=O_obs^-1-I_com^-1]\n",
              sum(diag(Icb %*% Vg)), riv_o))
  cat(sprintf("  san  tr(I_com   . Var[com])  = %7.3f   [= k=%d, complete-data MLE sanity]\n",
              sum(diag(Icb %*% Vc)), k))
  cat(sprintf("  A    E[A_rb] = %7.3f (se %.3f)   [= +tr(RIV_obs) %.3f]\n",
              mean(A_rb), sd(A_rb) / sqrt(length(A_rb)), riv_o))
  cat(sprintf("  B    E[B]    = %7.3f (se %.3f)   [= -1/2 tr(RIV_obs) %.3f]\n",
              mean(B_arr), sd(B_arr) / sqrt(length(B_arr)), -0.5 * riv_o))
}
cat("\n")
