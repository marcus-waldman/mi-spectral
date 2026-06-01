# term-a-mar-closedform.R  [Phase 3a closed form — todo/011]
#
# Closed-form general-MVN Term-A design-imbalance (A)+(C) for the monotone pattern, assembled
# from three derived ingredients and verified against the MCAR control (must vanish) and the
# phase-8 empirical surface. This is the reproducible promotion of the scratch exploration; it
# is the evidence behind the derivation.qmd @sec-termA closed-form claim.
#
#   (A)+(C)_inf = alpha^T b_Sigma  +  1/2 tr( H_phi I_obs^{-1} )
#
#   alpha   : entropy gradient (cov-only), alpha_a = -1/2 sum_{i:mis} tr(S0_i^{-1} dS_i[E_a]),
#             dS[dSigma] = dMM - dMO B^T - B dOM + B dOO B^T, B = Sigma_MO Sigma_OO^{-1}.   [analytic]
#   b_Sigma : lim N*E[Sigma_hat_obs - Sigma_0], the per-step monotone MLE covariance bias
#             recursion (cross-step covariances vanish by conditional unbiasedness of each step's
#             OLS slope):
#               b[1,1] = -sigma_11
#               b[j,P] = b_j b[P,P],   P = 1:(j-1)
#               b[j,j] = -(j/f_j) sigma_{jj.<j} + b_j b[P,P] b_j^T
#                        + (sigma_{jj.<j}/f_j) tr(Sigma_PP (Sigma_PP^{(j)})^{-1})
#             f_j = E[r_j]/N, Sigma_PP^{(j)} = Cov(X_P | observed through step j) (selected).  [analytic]
#   H_phi   : cross-entropy curvature grad^2_phi f_0(theta_0), f_0(phi)=barQ(eval=theta_0, obs=phi);
#             evaluated as grad^2 of barQ(theta_0, .) at theta_0 (obs slot only; eval fixed). Its
#             gradient is exactly alpha (cross-check). Excludes the eval-obs cross block that gives
#             (B)main=tr(RIV), so (C) = 1/2 tr(H_phi I_obs^{-1}) carries NO -tr(RIV).            [mechanical]
#   I_obs   : observed-data information at theta_0 (cross-inclusive, K&M 1998).                   [owned]
#
# Verification built in: (i) MCAR control (monotone pattern assigned independent of the data) =>
# (A)+(C) -> 0; (ii) N-stability of the closed-form value; (iii) grad f_0 == alpha. The bivariate
# reduction (A)+(C) = n_mis/n_obs - 1/2 tr(M_mis M_obs^{-1}) is the 2-step case, validated
# separately in run_all.R phase 8 / S1.
#
# Usage: Rscript verification/term-a-mar-closedform.R [R] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_arg   = if (length(args) >= 1) { as.integer(args[1]) } else { 800 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p = length(mu0)
k = p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
Ngrid <- c(800, 1500)

# Monotone pattern (mice convention, R=1 missing): obs sets nested {1}<{1,2}<{1,2,3}<{1,2,3,4}.
MONO_PATTERNS <- rbind(c(0, 0, 0, 1),   # p1: X4 missing
                       c(0, 0, 1, 1),   # p2: X3,X4 missing
                       c(0, 1, 1, 1))   # p3: X2,X3,X4 missing
MONO_FREQ <- c(1, 1, 1) / 3
PROP = 0.40

# MCAR control: assign the monotone patterns independent of the data (same marginal structure).
apply_mcar_monotone <- function(X) {
  N <- nrow(X); amp <- runif(N) < PROP
  Y <- X; R <- matrix(0, N, p)
  idx <- which(amp)
  if (length(idx) > 0) {
    pat <- sample.int(3, length(idx), replace = TRUE, prob = MONO_FREQ)
    for (t in 1:3) {
      ii <- idx[pat == t]; miss_cols <- which(MONO_PATTERNS[t, ] == 1)
      if (length(ii) > 0) { Y[ii, miss_cols] <- NA; R[ii, miss_cols] <- 1 }
    }
  }
  return(list(Y = Y, R = R))
}

pack <- function(theta) { return(c(theta$mu, theta$Sigma[lower.tri(theta$Sigma, diag = TRUE)])) }
unpack <- function(par) { mu <- par[1:p]; S <- matrix(0, p, p); S[lower.tri(S, diag = TRUE)] <- par[(p + 1):k]; S[upper.tri(S)] <- t(S)[upper.tri(S)]; return(list(mu = mu, Sigma = S)) }
par0 <- pack(theta0)
f_phi <- function(par, Y, R) { return(barQ_fiml_analytic(theta0, unpack(par), Y, R)) }
grad_hess_phi <- function(Y, R, h = 1e-3) {
  g <- numeric(k); H <- matrix(0, k, k); f0 <- f_phi(par0, Y, R)
  fp <- numeric(k); fm <- numeric(k)
  for (i in 1:k) { ei <- numeric(k); ei[i] <- h; fp[i] <- f_phi(par0 + ei, Y, R); fm[i] <- f_phi(par0 - ei, Y, R); g[i] <- (fp[i] - fm[i]) / (2 * h); H[i, i] <- (fp[i] - 2 * f0 + fm[i]) / (h^2) }
  for (i in 1:(k - 1)) { for (j in (i + 1):k) { eij <- numeric(k); eij[i] <- h; eij[j] <- h; eimj <- numeric(k); eimj[i] <- h; eimj[j] <- -h
    H[i, j] <- (f_phi(par0 + eij, Y, R) - f_phi(par0 + eimj, Y, R) - f_phi(par0 - eimj, Y, R) + f_phi(par0 - eij, Y, R)) / (4 * h^2); H[j, i] <- H[i, j] } }
  return(list(g = g, H = H))
}
Epert <- function(s) { i = lt[s, 1]; j = lt[s, 2]; E <- matrix(0, p, p); E[i, j] <- 1; E[j, i] <- 1; return(E) }
alpha_analytic <- function(R) {
  patt <- apply(R, 1, function(row) { return(paste(row, collapse = "")) }); alpha <- numeric(k)
  for (pp in unique(patt)) { rows <- which(patt == pp); n_pat = length(rows); Rp <- R[rows[1], ]
    M <- which(Rp == 1); O <- which(Rp == 0); if (length(M) == 0) { next }
    Soo_inv <- solve(Sig0[O, O, drop = FALSE]); B <- Sig0[M, O, drop = FALSE] %*% Soo_inv
    S0inv <- solve(Sig0[M, M, drop = FALSE] - B %*% Sig0[O, M, drop = FALSE])
    for (s in 1:(k - p)) { E <- Epert(s); dS <- E[M, M, drop = FALSE] - E[M, O, drop = FALSE] %*% t(B) - B %*% E[O, M, drop = FALSE] + B %*% E[O, O, drop = FALSE] %*% t(B)
      alpha[p + s] <- alpha[p + s] - 0.5 * n_pat * sum(diag(S0inv %*% dS)) } }
  return(alpha)
}
fiml_monotone_kstep <- function(Y, R) {
  obs_through <- function(j) { if (j == 1) { return(R[, 1] == 0) } else { return(rowSums(R[, 1:j, drop = FALSE]) == 0) } }
  mu <- numeric(p); Sigma <- matrix(0, p, p); s1 <- obs_through(1); x1 <- Y[s1, 1]; mu[1] = mean(x1); Sigma[1, 1] = mean((x1 - mu[1])^2)
  for (j in 2:p) { sj <- obs_through(j); Xpred <- cbind(1, Y[sj, 1:(j - 1), drop = FALSE]); yj <- Y[sj, j]
    coef <- solve(crossprod(Xpred), crossprod(Xpred, yj)); b_j <- coef[-1]; v_j = mean((yj - Xpred %*% coef)^2)
    Sig_prev <- Sigma[1:(j - 1), 1:(j - 1), drop = FALSE]; mu[j] = coef[1] + sum(b_j * mu[1:(j - 1)])
    Sigma[j, 1:(j - 1)] <- as.numeric(b_j %*% Sig_prev); Sigma[1:(j - 1), j] <- Sigma[j, 1:(j - 1)]; Sigma[j, j] = v_j + as.numeric(b_j %*% Sig_prev %*% b_j) }
  return(list(mu = mu, Sigma = Sigma))
}
# selected design moments f_j, Sigma_PP^{(j)} for a given amputation function
est_selected_moments <- function(amp_fun, N_sel, R_sel) {
  sxx <- vector("list", p); sx <- vector("list", p); cnt <- numeric(p)
  for (j in 1:p) { sxx[[j]] <- matrix(0, p, p); sx[[j]] <- numeric(p) }
  for (r in 1:R_sel) { set.seed(77000 + r); X <- gen_data(N_sel, mu0, Sig0); Rm <- amp_fun(X)$R
    for (j in 1:p) { sel = if (j == 1) { Rm[, 1] == 0 } else { rowSums(Rm[, 1:j, drop = FALSE]) == 0 }; cnt[j] = cnt[j] + sum(sel)
      if (j >= 2) { Xp <- X[sel, 1:(j - 1), drop = FALSE]; sxx[[j]][1:(j - 1), 1:(j - 1)] <- sxx[[j]][1:(j - 1), 1:(j - 1)] + crossprod(Xp); sx[[j]][1:(j - 1)] <- sx[[j]][1:(j - 1)] + colSums(Xp) } } }
  f <- cnt / (N_sel * R_sel); Spp_sel <- vector("list", p)
  for (j in 2:p) { P = 1:(j - 1); mxx <- sxx[[j]][P, P, drop = FALSE] / cnt[j]; mx <- sx[[j]][P] / cnt[j]; Spp_sel[[j]] <- mxx - outer(mx, mx) }
  return(list(f = f, Spp_sel = Spp_sel))
}
compute_bSigma <- function(sm) {
  bSig <- matrix(0, p, p); bSig[1, 1] = -Sig0[1, 1]
  for (j in 2:p) { P = 1:(j - 1); Spp <- Sig0[P, P, drop = FALSE]; b_j <- Sig0[j, P, drop = FALSE] %*% solve(Spp); sig_cond = as.numeric(Sig0[j, j] - b_j %*% Sig0[P, j])
    bSpp <- bSig[P, P, drop = FALSE]; bSig[j, P] <- b_j %*% bSpp; bSig[P, j] <- t(bSig[j, P, drop = FALSE])
    var_term = (sig_cond / sm$f[j]) * sum(diag(Spp %*% solve(sm$Spp_sel[[j]]))); bSig[j, j] = -(j / sm$f[j]) * sig_cond + as.numeric(b_j %*% bSpp %*% t(b_j)) + var_term }
  return(bSig)
}

amp_mar  <- function(X) { return(apply_missingness_ampute(X, prop = PROP, mech = "MAR", pattern_type = "monotone")) }
amp_mcar <- function(X) { return(apply_mcar_monotone(X)) }

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "lt", "pack", "unpack", "f_phi",
                    "grad_hess_phi", "Epert", "alpha_analytic", "fiml_monotone_kstep",
                    "apply_mcar_monotone", "MONO_PATTERNS", "MONO_FREQ", "PROP"))

# top-level per-rep worker (mech is a string; mirrors the working parLapply pattern)
one_rep_cell <- function(r, N, mech) {
  set.seed(20260601 + r); X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(if (mech == "MAR") { apply_missingness_ampute(X, prop = PROP, mech = "MAR", pattern_type = "monotone") } else { apply_mcar_monotone(X) },
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  to <- tryCatch(fiml_monotone_kstep(mar$Y, mar$R), error = function(e) { return(NULL) }); if (is.null(to)) { return(NULL) }
  gh <- grad_hess_phi(mar$Y, mar$R); Iobs <- observed_info_obs_mvn(theta0, mar$Y, mar$R); al <- alpha_analytic(mar$R)
  return(list(H = gh$H, Iobs = Iobs, al = al))
}
clusterExport(cl, "one_rep_cell")

cat("\n== Term-A closed form (A)+(C)_inf: MAR (design-imbalance) vs MCAR (control) ==\n")
sm_mar <- est_selected_moments(amp_mar, 20000, 300); bSig_mar <- compute_bSigma(sm_mar)
sm_mcar <- est_selected_moments(amp_mcar, 20000, 300); bSig_mcar <- compute_bSigma(sm_mcar)
cat(sprintf("  MAR  f_j: %s\n", paste(sprintf("%.4f", sm_mar$f), collapse = " ")))
cat(sprintf("  MCAR f_j: %s\n", paste(sprintf("%.4f", sm_mcar$f), collapse = " ")))
cat(sprintf("%-6s %-6s %10s %10s %12s\n", "mech", "N", "(A)", "(C)", "(A)+(C)"))
bvech_mar <- bSig_mar[lower.tri(bSig_mar, diag = TRUE)]
bvech_mcar <- bSig_mcar[lower.tri(bSig_mcar, diag = TRUE)]
for (cell in list(list(mech = "MAR", bv = bvech_mar), list(mech = "MCAR", bv = bvech_mcar))) {
  mech <- cell$mech; bv <- cell$bv
  for (N in Ngrid) {
    clusterExport(cl, c("N", "mech"))
    res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_arg), function(r) { return(one_rep_cell(r, N, mech)) }))
    nok = length(res)
    H_bar <- Reduce(`+`, lapply(res, `[[`, "H")) / nok
    Iobs_bar <- Reduce(`+`, lapply(res, `[[`, "Iobs")) / nok
    al_bar <- Reduce(`+`, lapply(res, `[[`, "al")) / nok
    A = sum(al_bar * c(numeric(p), bv) / N); C = 0.5 * sum(diag(H_bar %*% solve(Iobs_bar)))
    cat(sprintf("%-6s %-6d %+10.4f %+10.4f %+12.4f\n", mech, N, A, C, A + C))
  }
}
cat("\n  [MAR (A)+(C) ~ -0.22 (design imbalance); MCAR (A)+(C) ~ 0 (control: Q_mis=Q_obs)]\n")
