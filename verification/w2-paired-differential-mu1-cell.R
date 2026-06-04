# w2-paired-differential-mu1-cell.R  [todo/024 D1 -- DISCRIMINATING cell for the
# differential-bias formula: B_direct (I_com-metric projection) vs D_naive
# (self-contained tr(RIV) difference)]
#
# The sigma_12 = 0 spot check (w2-paired-differential-spotcheck.R) cannot separate the
# two formulas (gap 0.065, ~5%). This cell tests H0: mu_1 = 0 under HEAVY X1
# missingness (P(miss X1) = Phi(0.8 + 1.2 X3) ~ 70-79%, X2 essentially complete,
# X3/X4 complete): the MAR mu x Sigma cross term + concentrated missing information
# make the tested direction strongly non-aligned, giving targets (N=1000, at truth)
#   D_naive ~ 8.4   vs   B_direct ~ 2.6     (gap ~ 5.8 on a q_d = 1 test).
#
# PREREGISTERED PREDICTION (D1, I_com metric): mean(dL - dcom) lands on B_direct,
# decisively NOT on D_naive (>30 se separation at R = 2000).
#
# The mu_1 = 0 constrained MVN MLE given moment stats (m, S) is CLOSED FORM:
# minimize log|S + dd'| = log|S| + log(1 + d'S^{-1}d) over d = m - mu with d_1 = m_1:
# d_{-1} = -W_{22}^{-1} W_{21} m_1 (W = S^{-1}), mu-hat = m - d, Sigma-hat = S + dd'.
#
# Usage: Rscript verification/w2-paired-differential-mu1-cell.R [R_main] [R_mom] [cores] [Ns]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_main  = if (length(args) >= 1) { as.integer(args[1]) } else { 2000 }
R_mom   = if (length(args) >= 2) { as.integer(args[2]) } else { 400 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 6 }
Ns      = if (length(args) >= 4) { as.integer(strsplit(args[4], ",")[[1]]) } else { c(500, 1000) }

p = 4; k = 14
mu0 <- c(0, 0, 0, 0)            # H0 truth: mu_1 = 0
Sig0 <- default_Sigma           # full Sigma (sigma_12 = 0.6)
TR <- list(mu = mu0, Sigma = Sig0)
idx_cn <- 2:14                  # free params under mu_1 = 0
q_d = 1

amp_fun <- function(X) {        # "x1_heavy": X1 ~70-79% missing MAR on X3; X2 ~complete
  N <- nrow(X)
  pi1 <- pnorm(0.8 + 1.2 * X[, 3])
  pi2 <- pnorm(-3.0 + 0 * X[, 4])
  R <- matrix(0, N, 4)
  R[, 1] <- as.numeric(runif(N) < pi1)
  R[, 2] <- as.numeric(runif(N) < pi2)
  Y <- X; Y[R == 1] <- NA
  return(list(Y = Y, R = R))
}

# E-step moments at theta_obs (same as the sigma12 spot check)
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

# closed-form mu_1 = 0 constrained MVN MLE from moment stats
cn_mu1_moments <- function(m, S) {
  W <- solve(S)
  d <- numeric(p)
  d[1] = m[1]
  d[-1] <- as.numeric(-solve(W[-1, -1, drop = FALSE], W[-1, 1, drop = FALSE])) * m[1]
  return(list(mu = m - d, Sigma = S + tcrossprod(d)))
}

trace_targets <- function(N, seed0) {
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
  W <- I_com %*% solve(I_obs, I_com)
  B_direct = sum(diag(solve(I_com, W))) - sum(diag(solve(I_com[idx_cn, idx_cn], W[idx_cn, idx_cn]))) - q_d
  return(c(trRIV_f = riv_f, trRIV_0 = riv_0, D_naive = riv_f - riv_0, B_direct = B_direct))
}

one <- function(seed, N) {
  set.seed(seed)
  X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values = TRUE)$values) < 1e-6) { return(NULL) }
  em <- estep_moments(to, mar$Y, mar$R)
  psi_star <- list(mu = em$m, Sigma = em$S)
  cn_q <- cn_mu1_moments(em$m, em$S)
  Qf = barQ_fiml_analytic(psi_star, to, mar$Y, mar$R)
  Q0 = barQ_fiml_analytic(cn_q, to, mar$Y, mar$R)
  dL = 2 * (Qf - Q0)
  th_com <- mle_complete_mvn(X)
  cn_com <- cn_mu1_moments(th_com$mu, th_com$Sigma)
  ll_f = loglik_mvn(th_com, X)
  ll_0 = loglik_mvn(cn_com, X)
  dcom = 2 * (ll_f - ll_0)
  T_f = Qf - ll_f
  return(c(dL = dL, dcom = dcom, D = (dL - dcom) / 2, T_f = T_f,
           fp_gap = max(abs(c(em$m - to$mu, em$S - to$Sigma)))))
}

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); suppressPackageStartupMessages(library(lavaan)) }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "amp_fun", "estep_moments", "cn_mu1_moments", "one"))

cat("====== W2 differential DISCRIMINATING cell: H0 mu_1 = 0, X1-heavy MAR ======\n")
cat(sprintf("R_main=%d, R_mom=%d, cores=%d, Ns=%s; q_d=%d\n\n", R_main, R_mom, n_cores,
            paste(Ns, collapse = ","), q_d))
rows <- list(); reps <- list()
for (N in Ns) {
  tg <- trace_targets(N, 660000)
  M <- do.call(rbind, Filter(Negate(is.null),
         parLapply(cl, seq_len(R_main), function(s, NN) one(20260604 + s, NN), NN = N)))
  est = mean(M[, "dL"] - M[, "dcom"]); se = sd(M[, "dL"] - M[, "dcom"]) / sqrt(nrow(M))
  cat(sprintf("-- N=%4d (%d ok) --\n", N, nrow(M)))
  cat(sprintf("   targets: D_naive=%7.4f   B_direct=%7.4f   (gap=%.3f)\n",
              tg["D_naive"], tg["B_direct"], tg["D_naive"] - tg["B_direct"]))
  cat(sprintf("   mean(dL-dcom) = %+.4f (%.4f)\n", est, se))
  cat(sprintf("   => vs B_direct: %+7.4f (%6.1f se) | vs D_naive: %+8.4f (%6.1f se)\n",
              est - tg["B_direct"], (est - tg["B_direct"]) / se,
              est - tg["D_naive"], (est - tg["D_naive"]) / se))
  cat(sprintf("   sd(T_f)=%8.3f  sd(D)=%7.3f  mean fp_gap=%.2e\n\n",
              sd(M[, "T_f"]), sd(M[, "D"]), mean(M[, "fp_gap"])))
  rows[[as.character(N)]] <- c(N = N, n_ok = nrow(M), est = est, se = se, tg,
                               sd_Tf = sd(M[, "T_f"]), sd_D = sd(M[, "D"]))
  reps[[as.character(N)]] <- M
}
stopCluster(cl)
S <- do.call(rbind, rows)
cat("-- summary --\n"); print(round(S, 4))
saveRDS(list(summary = S, reps = reps), "verification/cache/w2-paired-differential-mu1-cell.rds")
cat("\nwrote verification/cache/w2-paired-differential-mu1-cell.rds\n")
cat("=============================================================================\n")
