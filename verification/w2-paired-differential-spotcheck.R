# w2-paired-differential-spotcheck.R  [todo/024 D1-D3 -- SMALL paired MC spot check ONLY]
#
# Setting: nested MVN pair (full unstructured vs sigma_12 = 0), p = 4, ampute MAR
# non-monotone 40% (phase-8 design), SHARED deterministic-FIML imputation at the
# FULL model's observed-data MLE theta_obs. Per dataset:
#   psi*    = argmax Qbar          ( = E-step moments (m*, S*); EM fixed point: = theta_obs )
#   gamma*  = argmax Qbar o g      ( Cholesky optim on the E-step moments, L[2,1] = 0 )
#   d_L     = 2[Qbar(psi*) - Qbar(g(gamma*))]
#   d_com   = 2[ell_com(theta_com) - ell_com(null com MLE)]    (complete data, same X)
#   T_f     = Qbar(psi*) - ell_com(theta_com)        (full-model level; sd ~ c sqrt(n))
#   T_0     = Qbar(g(gamma*)) - ell_com(null com)    (null-model level)
#   D       = T_f - T_0 = (d_L - d_com)/2            (per-dataset PAIRED differential)
#
# PREREGISTERED PREDICTIONS (derived first, session 2026-06-04; CAS:
# verification/cas-wolfram/verify_w2_differential.py):
#   P1 (D2): sd(T_f) grows ~ sqrt(n); sd(D) = O(1), ~flat in n, at H0 and local arms.
#   P2 (D1): at H0, E[d_L - d_com] -> B_direct = tr(M_com I_com I_obs^-1 I_com) - q_d
#            (I_com metric, complement-restricted), NOT the naive
#            D_naive = tr(RIV_f) - tr(RIV_0); B_direct <= D_naive with strict gap
#            unless col(G) is invariant under I_obs^-1 I_com. mean(D) -> B_direct/2.
#   P3 (D3): the (A)+(C) differential at H0 is 0 to second order: no O(1) offset of
#            mean(D) beyond B_direct/2.
#   P4 (D3): local arm (sigma_12 = 2/sqrt(N)): mean(D) = B_direct/2 + O(n^-1/2);
#            sd(D) still O(1).
#   P5 (D2): fixed arm (sigma_12 = 0.6): sd(D) reverts to ~sqrt(n) growth
#            (pseudo-truths O(1) apart; the exact realized cancellation fails).
#
# Usage: Rscript verification/w2-paired-differential-spotcheck.R [R_main] [R_mom] [cores] [Ns]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_main  = if (length(args) >= 1) { as.integer(args[1]) } else { 1200 }
R_mom   = if (length(args) >= 2) { as.integer(args[2]) } else { 400 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 6 }
Ns      = if (length(args) >= 4) { as.integer(strsplit(args[4], ",")[[1]]) } else { c(500, 1000, 2000) }

p = 4; k = p + p * (p + 1) / 2
mu0 <- default_mu
idx_cn <- constrained_param_indices_sigma12_zero()   # 13 of 14 free under sigma_12 = 0
q_d = k - length(idx_cn)

sigma_truth <- function(arm, N) {
  S <- default_Sigma
  s12 = if (arm == "H0") { 0 } else if (arm == "local") { 2 / sqrt(N) } else { 0.6 }
  S[1, 2] <- s12; S[2, 1] <- s12
  return(S)
}
amp_fun <- function(X) { return(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone")) }

# ---- E-step moments at theta_obs: m* and S* (within + between), Qbar's sufficient stats ----
estep_moments <- function(theta_obs, Y, R) {
  N <- nrow(Y)
  Xhat <- Y
  Vbar <- matrix(0, p, p)
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat)
    R_pat <- R[rows[1], ]
    Mi <- which(R_pat == 1); Oi <- which(R_pat == 0)
    if (length(Mi) == 0) { next }
    if (length(Oi) == 0) {
      Xhat[rows, ] <- matrix(theta_obs$mu, length(rows), p, byrow = TRUE)
      Vbar <- Vbar + length(rows) * theta_obs$Sigma
    } else {
      Soo_inv <- solve(theta_obs$Sigma[Oi, Oi, drop = FALSE])
      reg <- theta_obs$Sigma[Mi, Oi, drop = FALSE] %*% Soo_inv
      cond_V <- theta_obs$Sigma[Mi, Mi, drop = FALSE] - reg %*% t(theta_obs$Sigma[Mi, Oi, drop = FALSE])
      cm <- sweep(Y[rows, Oi, drop = FALSE], 2, theta_obs$mu[Oi], FUN = "-") %*% t(reg)
      Xhat[rows, Mi] <- sweep(cm, 2, theta_obs$mu[Mi], FUN = "+")
      Vfull <- matrix(0, p, p); Vfull[Mi, Mi] <- cond_V
      Vbar <- Vbar + length(rows) * Vfull
    }
  }
  m_star <- colMeans(Xhat)
  Xc <- sweep(Xhat, 2, m_star, FUN = "-")
  S_star <- crossprod(Xc) / N + Vbar / N
  return(list(m = m_star, S = S_star))
}

# ---- constrained MVN MLE (sigma_12 = 0) given moment stats (m, S): Cholesky optim ----
mle_chol_sigma12_moments <- function(m, S, N) {
  build_L <- function(tau) {
    L <- matrix(0, 4, 4)
    L[1, 1] <- exp(tau[1]); L[2, 2] <- exp(tau[2])
    L[3, 1] <- tau[3]; L[3, 2] <- tau[4]; L[3, 3] <- exp(tau[5])
    L[4, 1] <- tau[6]; L[4, 2] <- tau[7]; L[4, 3] <- tau[8]; L[4, 4] <- exp(tau[9])
    return(L)
  }
  diag_idx <- c(1, 2, 5, 9)
  nll <- function(tau) {
    L <- build_L(tau)
    Sigma_inv <- tryCatch(chol2inv(t(L)), error = function(e) { return(NULL) })
    if (is.null(Sigma_inv)) { return(1e10) }
    return(2 * sum(tau[diag_idx]) + sum(Sigma_inv * S))
  }
  gr <- function(tau) {
    L <- build_L(tau)
    L_inv <- tryCatch(solve(L), error = function(e) { return(NULL) })
    if (is.null(L_inv)) { return(rep(0, 9)) }
    Sigma_inv <- crossprod(L_inv)
    G <- 2 * (t(L_inv) - Sigma_inv %*% S %*% Sigma_inv %*% L)
    g <- numeric(9)
    g[1] <- G[1, 1] * L[1, 1]; g[2] <- G[2, 2] * L[2, 2]
    g[3] <- G[3, 1]; g[4] <- G[3, 2]; g[5] <- G[3, 3] * L[3, 3]
    g[6] <- G[4, 1]; g[7] <- G[4, 2]; g[8] <- G[4, 3]; g[9] <- G[4, 4] * L[4, 4]
    return(g)
  }
  S_init <- S; S_init[1, 2] <- 0; S_init[2, 1] <- 0
  L_init <- tryCatch(t(chol(S_init)), error = function(e) { return(diag(sqrt(diag(S) + 1e-6))) })
  par0 <- c(log(max(L_init[1, 1], 1e-3)), log(max(L_init[2, 2], 1e-3)),
            L_init[3, 1], L_init[3, 2], log(max(L_init[3, 3], 1e-3)),
            L_init[4, 1], L_init[4, 2], L_init[4, 3], log(max(L_init[4, 4], 1e-3)))
  opt <- stats::optim(par0, nll, gr = gr, method = "BFGS",
                      control = list(reltol = 1e-12, maxit = 300))
  L_hat <- build_L(opt$par)
  return(list(mu = m, Sigma = tcrossprod(L_hat), converged = opt$convergence == 0))
}

# ---- analytic trace targets at a truth (population informations) ----
trace_targets <- function(Sig0, N, R_mom, seed0) {
  TR <- list(mu = mu0, Sigma = Sig0)
  Iobs_sum <- matrix(0, k, k); n_ok = 0
  for (r in 1:R_mom) {
    set.seed(seed0 + r)
    X <- gen_data(N, mu0, Sig0)
    mar <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(mar)) { next }
    Iobs_sum <- Iobs_sum + observed_info_obs_mvn(TR, mar$Y, mar$R)
    n_ok = n_ok + 1
  }
  I_obs <- Iobs_sum / n_ok
  I_com <- fisher_info_com_mvn(TR, N)
  riv_f = sum(diag(solve(I_obs, I_com))) - k
  riv_0 = sum(diag(solve(I_obs[idx_cn, idx_cn], I_com[idx_cn, idx_cn]))) - length(idx_cn)
  D_naive = riv_f - riv_0
  # B_direct = tr(M_com I_com I_obs^-1 I_com) - q_d, M_com = I_com^-1 - G(G'I_com G)^-1 G'
  W <- I_com %*% solve(I_obs, I_com)              # I_com I_obs^-1 I_com
  B_direct = sum(diag(solve(I_com, W))) - sum(diag(solve(I_com[idx_cn, idx_cn], W[idx_cn, idx_cn]))) - q_d
  return(c(trRIV_f = riv_f, trRIV_0 = riv_0, D_naive = D_naive, B_direct = B_direct))
}

# ---- per-replicate work ----
one <- function(seed, N, Sig0) {
  set.seed(seed)
  X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values = TRUE)$values) < 1e-6) { return(NULL) }
  em <- estep_moments(to, mar$Y, mar$R)
  fp_gap = max(abs(c(em$m - to$mu, em$S - to$Sigma)))       # EM fixed-point check
  psi_star <- list(mu = em$m, Sigma = em$S)
  cn_q <- mle_chol_sigma12_moments(em$m, em$S, N)
  if (!cn_q$converged) { return(NULL) }
  Qf = barQ_fiml_analytic(psi_star, to, mar$Y, mar$R)
  Q0 = barQ_fiml_analytic(cn_q, to, mar$Y, mar$R)
  dL = 2 * (Qf - Q0)
  th_com <- mle_complete_mvn(X)
  ll_f = loglik_mvn(th_com, X)
  cn_com <- mle_chol_sigma12(X)
  dcom = 2 * (ll_f - cn_com$logLik)
  T_f = Qf - ll_f
  T_0 = Q0 - cn_com$logLik
  # realized naive differential (observed-info RIVs at the respective fits)
  d_naive_real <- tryCatch(
    tr_riv_observed_general(to, mar$Y, mar$R, 1:k) -
      tr_riv_observed_general(list(mu = cn_q$mu, Sigma = cn_q$Sigma), mar$Y, mar$R, idx_cn),
    error = function(e) { return(NA) })
  return(c(T_f = T_f, T_0 = T_0, D = T_f - T_0, dL = dL, dcom = dcom,
           fp_gap = fp_gap, d_naive_real = d_naive_real))
}

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); suppressPackageStartupMessages(library(lavaan)) }))
clusterExport(cl, c("mu0", "p", "k", "idx_cn", "amp_fun", "estep_moments",
                    "mle_chol_sigma12_moments", "one"))

cat("====== W2 paired-differential spot check (todo/024 D1-D3) ======\n")
cat(sprintf("R_main=%d per cell, R_mom=%d, cores=%d, Ns=%s; q_d=%d\n\n",
            R_main, R_mom, n_cores, paste(Ns, collapse = ","), q_d))

rows <- list()
reps <- list()
for (arm in c("H0", "local", "fixed")) {
  for (N in Ns) {
    Sig0 <- sigma_truth(arm, N)
    tg <- trace_targets(Sig0, N, R_mom, 880000)
    M <- do.call(rbind, Filter(Negate(is.null),
           parLapply(cl, seq_len(R_main), function(s, NN, SS) one(20260604 + s, NN, SS),
                     NN = N, SS = Sig0)))
    mD = mean(M[, "D"]); seD = sd(M[, "D"]) / sqrt(nrow(M))
    cat(sprintf("-- arm=%-5s N=%4d (%d ok) --\n", arm, N, nrow(M)))
    cat(sprintf("   targets: trRIV_f=%.3f trRIV_0=%.3f  D_naive=%.4f  B_direct=%.4f  (gap=%.4f)\n",
                tg["trRIV_f"], tg["trRIV_0"], tg["D_naive"], tg["B_direct"],
                tg["D_naive"] - tg["B_direct"]))
    cat(sprintf("   sd(T_f)=%8.3f   sd(D)=%7.3f   [P1/P5: sd(T_f)~sqrt(n); sd(D) flat at H0/local]\n",
                sd(M[, "T_f"]), sd(M[, "D"])))
    cat(sprintf("   mean(D)=%+.4f (%.4f)  vs B_direct/2=%+.4f  vs D_naive/2=%+.4f\n",
                mD, seD, tg["B_direct"] / 2, tg["D_naive"] / 2))
    cat(sprintf("   mean(dL-dcom)=%+.4f (%.4f);  mean fp_gap=%.2e;  mean d_naive_real=%+.4f\n\n",
                mean(M[, "dL"] - M[, "dcom"]), 2 * seD, mean(M[, "fp_gap"]),
                mean(M[, "d_naive_real"], na.rm = TRUE)))
    # Wilks control variate: E[dcom] = q_d + O(1/n) exactly, so regressing
    # dL on dcom sharpens mean(dL - dcom) without bias.
    a_cv = stats::cov(M[, "dL"], M[, "dcom"]) / stats::var(M[, "dcom"])
    cv <- M[, "dL"] - q_d - a_cv * (M[, "dcom"] - q_d)
    cat(sprintf("   CV: E[dL]-q_d = %+.4f (%.4f)  [a=%.3f; targets: B_direct=%+.4f D_naive=%+.4f]\n\n",
                mean(cv), sd(cv) / sqrt(length(cv)), a_cv, tg["B_direct"], tg["D_naive"]))
    rows[[paste(arm, N, sep = "_")]] <- c(N = N, arm = which(c("H0", "local", "fixed") == arm),
      n_ok = nrow(M), sd_Tf = sd(M[, "T_f"]), sd_D = sd(M[, "D"]),
      mean_D = mD, se_D = seD, tg, mean_dnaive_real = mean(M[, "d_naive_real"], na.rm = TRUE),
      cv_mean = mean(cv), cv_se = sd(cv) / sqrt(length(cv)), a_cv = a_cv)
    reps[[paste(arm, N, sep = "_")]] <- M
  }
}
stopCluster(cl)
S <- do.call(rbind, rows)
cat("-- summary --\n"); print(round(S, 4))
saveRDS(list(summary = S, reps = reps), "verification/cache/w2-paired-differential-spotcheck.rds")
cat("\nwrote verification/cache/w2-paired-differential-spotcheck.rds\n")
cat("Verdicts: P1 sd(D) flat + sd(T_f) ~ sqrt(n) at H0/local; P2 mean(D) -> B_direct/2 (not D_naive/2\n")
cat("if gap resolvable); P5 fixed arm sd(D) grows ~ sqrt(n).\n")
cat("=================================================================\n")
