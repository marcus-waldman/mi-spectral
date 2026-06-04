# scratch-w2diff-design-search.R -- find a MAR design where B_direct vs D_naive
# differ enough for MC discrimination (gap >= ~0.4). Targets only, no main MC.
source("verification/00-setup.R")
p = 4; k = 14
mu0 <- default_mu
Sig0 <- default_Sigma; Sig0[1, 2] <- 0; Sig0[2, 1] <- 0   # H0 truth
idx_cn <- constrained_param_indices_sigma12_zero()
q_d = 1

targets_for <- function(amp, N, R_mom, seed0) {
  TR <- list(mu = mu0, Sigma = Sig0)
  Iobs_sum <- matrix(0, k, k); n_ok = 0
  for (r in 1:R_mom) {
    set.seed(seed0 + r)
    X <- gen_data(N, mu0, Sig0)
    mar <- tryCatch(amp(X), error = function(e) { return(NULL) }); if (is.null(mar)) { next }
    Iobs_sum <- Iobs_sum + observed_info_obs_mvn(TR, mar$Y, mar$R)
    n_ok = n_ok + 1
  }
  I_obs <- Iobs_sum / n_ok
  I_com <- fisher_info_com_mvn(TR, N)
  riv_f = sum(diag(solve(I_obs, I_com))) - k
  riv_0 = sum(diag(solve(I_obs[idx_cn, idx_cn], I_com[idx_cn, idx_cn]))) - length(idx_cn)
  W <- I_com %*% solve(I_obs, I_com)
  B_direct = sum(diag(solve(I_com, W))) - sum(diag(solve(I_com[idx_cn, idx_cn], W[idx_cn, idx_cn]))) - q_d
  return(c(riv_f = riv_f, riv_0 = riv_0, D_naive = riv_f - riv_0, B_direct = B_direct,
           gap = riv_f - riv_0 - B_direct))
}

# custom MAR amputers (X3, X4 always observed -> MAR; X1/X2 missingness asymmetric)
mk_amp <- function(p1_base, p1_slope, p2_base, p2_slope) {
  return(function(X) {
    N <- nrow(X)
    pi1 <- pnorm(p1_base + p1_slope * X[, 3])
    pi2 <- pnorm(p2_base + p2_slope * X[, 4])
    R <- matrix(0, N, 4)
    R[, 1] <- as.numeric(runif(N) < pi1)
    R[, 2] <- as.numeric(runif(N) < pi2)
    Y <- X; Y[R == 1] <- NA
    return(list(Y = Y, R = R))
  })
}

designs <- list(
  base_ampute = function(X) { return(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone")) },
  x1_heavy = mk_amp(0.8, 1.2, -3.0, 0.0),     # X1 ~79% missing (steep in X3), X2 ~0.1%
  x1_only_steep = mk_amp(0.5, 2.0, -8.0, 0.0), # X1 ~62% missing, very steep in X3; X2 never
  x1x2_asym = mk_amp(0.8, 1.5, -1.5, 0.3),     # X1 heavy/steep, X2 light
  x1_mod = mk_amp(0.0, 1.5, -8.0, 0.0)         # X1 ~50% steep, X2 never
)

for (nm in names(designs)) {
  tg <- targets_for(designs[[nm]], 1000, 150, 770000)
  cat(sprintf("%-15s riv_f=%6.3f riv_0=%6.3f  D_naive=%7.4f  B_direct=%7.4f  GAP=%7.4f\n",
              nm, tg["riv_f"], tg["riv_0"], tg["D_naive"], tg["B_direct"], tg["gap"]))
}

# ---- same designs, but testing H0: mu_1 = 0 (exercises the MAR mu x Sigma cross term) ----
idx_cn <- 2:14   # free params under mu_1 = 0
Sig0 <- default_Sigma   # full Sigma (sigma_12 = 0.6); truth has mu_1 = 0 anyway
cat("\n--- H0: mu_1 = 0 (q_d = 1) ---\n")
for (nm in names(designs)) {
  tg <- targets_for(designs[[nm]], 1000, 150, 770000)
  cat(sprintf("%-15s riv_f=%6.3f riv_0=%6.3f  D_naive=%7.4f  B_direct=%7.4f  GAP=%7.4f\n",
              nm, tg["riv_f"], tg["riv_0"], tg["D_naive"], tg["B_direct"], tg["gap"]))
}
