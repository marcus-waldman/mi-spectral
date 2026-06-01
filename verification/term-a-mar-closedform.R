# term-a-mar-closedform.R  [Phase 3a closed form — todo/011]
#
# FULLY ANALYTIC general-MVN Term-A design-imbalance (A)+(C) for the monotone pattern. No finite
# differences, no per-replicate MLE fit: a single cheap moment pass at theta_0 supplies the design
# inputs (per-step selected predictor covariances for b_Sigma; per-missing-pattern selected moments
# of e_O for H_phi; expected observed information), and everything else is closed-form matrix algebra.
#
#   (A)+(C)_inf = alpha^T b_Sigma  +  1/2 tr( H_phi I_obs^{-1} )
#
# alpha  : entropy gradient, alpha_a = -1/2 sum_{i:mis} tr(S0_i^{-1} dS_i[E_a]) (cov-only, per-pattern
#          deterministic).  [validated vs finite-diff to 3e-5: scratch-alpha-analytic.R]
# b_Sigma: lim N*E[Sigma_hat_obs - Sigma_0], monotone per-step MLE-bias recursion (cross-step
#          covariances vanish by conditional unbiasedness of each step's OLS slope).
# H_phi  : cross-entropy curvature grad^2_phi barQ(theta_0, phi)|_{theta_0}. At theta_0,
#          (Sig0^{-1} e_bar)_M = 0, so the 2nd-derivative-of-mean term drops and, per missing unit,
#            H_phi = -J_d^T S0^{-1} J_d  +  (Sigma-Sigma T-part),
#          J_d = d m_phi/d phi (mu-block determ.: I on M, -B0 on O; Sigma-block G_a U e_O),
#          G_a = (E_a)_{MO} - B0 (E_a)_{OO}, U=Sig0_{OO}^{-1}, B0=Sig0_{MO}U, S0=Schur,
#          T-part[a,b] = 1/2 tr(S0^{-1}(G_a U G_b^T + G_b U G_a^T)).
#          Expectations reduce to per-pattern selected moments m1_P=E[e_O|P], M2_P=E[e_O e_O^T|P]:
#            H[mu,mu]=-Dmu^T S0^{-1} Dmu ; H[mu,a]=-Dmu^T S0^{-1} G_a U m1_P ;
#            H[a,b]=-tr((G_a U)^T S0^{-1}(G_b U) M2_P) + T-part[a,b].
#          [validated vs finite-diff: mu-mu (deterministic) block to 0.2%, (C) to 0.003;
#           scratch-hphi-analytic.R]
# I_obs  : expected observed-data information at theta_0 (cross-inclusive, K&M 1998).
#
# Verification: MCAR control (monotone pattern assigned independent of the data) => (A)+(C) -> 0;
# the bivariate reduction (A)+(C)=n_mis/n_obs - 1/2 tr(M_mis M_obs^{-1}) is the 2-step case
# (run_all.R phase 8 / S1).
#
# Usage: Rscript verification/term-a-mar-closedform.R [N] [R_mom] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
N_arg   = if (length(args) >= 1) { as.integer(args[1]) } else { 2000 }
R_mom   = if (length(args) >= 2) { as.integer(args[2]) } else { 600 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p = length(mu0)
k = p + p * (p + 1) / 2
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
Epert <- function(s) { i = lt[s, 1]; j = lt[s, 2]; E <- matrix(0, p, p); E[i, j] <- 1; E[j, i] <- 1; return(E) }

MONO_PATTERNS <- rbind(c(0, 0, 0, 1), c(0, 0, 1, 1), c(0, 1, 1, 1))   # X4 / X3,X4 / X2,X3,X4 missing
MONO_FREQ <- c(1, 1, 1) / 3
PROP = 0.40
apply_mcar_monotone <- function(X) {
  N <- nrow(X); amp <- runif(N) < PROP; Y <- X; R <- matrix(0, N, p); idx <- which(amp)
  if (length(idx) > 0) { pat <- sample.int(3, length(idx), replace = TRUE, prob = MONO_FREQ)
    for (t in 1:3) { ii <- idx[pat == t]; mc <- which(MONO_PATTERNS[t, ] == 1); if (length(ii) > 0) { Y[ii, mc] <- NA; R[ii, mc] <- 1 } } }
  return(list(Y = Y, R = R))
}
amp_mar  <- function(X) { return(apply_missingness_ampute(X, prop = PROP, mech = "MAR", pattern_type = "monotone")) }
amp_mcar <- function(X) { return(apply_mcar_monotone(X)) }

# ---- single moment pass at theta_0: per-step (b_Sigma), per-pattern (H_phi), E[I_obs] ----
est_moments <- function(amp_fun, N, R) {
  # per-step accumulators (obs-through-j): count, sum/sumsq of X_{<j}
  cs <- numeric(p); sx <- vector("list", p); sxx <- vector("list", p)
  for (j in 1:p) { sx[[j]] <- numeric(p); sxx[[j]] <- matrix(0, p, p) }
  # per-missing-pattern accumulators: count, sum/sumsq of e_O = y_O - mu0_O
  pacc <- list()
  Iobs_sum <- matrix(0, k, k); n_ok = 0
  for (r in 1:R) {
    set.seed(990000 + r); X <- gen_data(N, mu0, Sig0); mar <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(mar)) { next }
    Rm <- mar$R; n_ok = n_ok + 1
    for (j in 1:p) { sel = if (j == 1) { Rm[, 1] == 0 } else { rowSums(Rm[, 1:j, drop = FALSE]) == 0 }
      cs[j] = cs[j] + sum(sel)
      if (j >= 2) { Xp <- X[sel, 1:(j - 1), drop = FALSE]; sx[[j]][1:(j - 1)] <- sx[[j]][1:(j - 1)] + colSums(Xp); sxx[[j]][1:(j - 1), 1:(j - 1)] <- sxx[[j]][1:(j - 1), 1:(j - 1)] + crossprod(Xp) } }
    patt <- apply(Rm, 1, function(row) { return(paste(row, collapse = "")) })
    for (pp in unique(patt)) { Rp <- Rm[which(patt == pp)[1], ]; O <- which(Rp == 0); if (length(O) == p) { next }
      rows <- which(patt == pp); e <- sweep(X[rows, O, drop = FALSE], 2, mu0[O], FUN = "-")
      if (is.null(pacc[[pp]])) { pacc[[pp]] <- list(count = 0, s1 = numeric(p), s2 = matrix(0, p, p), O = O, M = which(Rp == 1)) }
      pacc[[pp]]$count <- pacc[[pp]]$count + nrow(e); pacc[[pp]]$s1[O] <- pacc[[pp]]$s1[O] + colSums(e); pacc[[pp]]$s2[O, O] <- pacc[[pp]]$s2[O, O] + crossprod(e) }
    Iobs_sum <- Iobs_sum + observed_info_obs_mvn(list(mu = mu0, Sigma = Sig0), mar$Y, Rm)
  }
  f <- cs / (N * n_ok); Spp_sel <- vector("list", p)
  for (j in 2:p) { P = 1:(j - 1); mxx <- sxx[[j]][P, P, drop = FALSE] / cs[j]; mx <- sx[[j]][P] / cs[j]; Spp_sel[[j]] <- mxx - outer(mx, mx) }
  pm <- list()
  for (key in names(pacc)) { a <- pacc[[key]]; O <- a$O; pm[[key]] <- list(frac = a$count / (N * n_ok), m1 = a$s1[O] / a$count, M2 = a$s2[O, O, drop = FALSE] / a$count, O = O, M = a$M) }
  return(list(f = f, Spp_sel = Spp_sel, pm = pm, Iobs = Iobs_sum / n_ok, N = N))
}

compute_bSigma <- function(mm) {
  bSig <- matrix(0, p, p); bSig[1, 1] = -Sig0[1, 1]
  for (j in 2:p) { P = 1:(j - 1); Spp <- Sig0[P, P, drop = FALSE]; b_j <- Sig0[j, P, drop = FALSE] %*% solve(Spp); sig_cond = as.numeric(Sig0[j, j] - b_j %*% Sig0[P, j])
    bSpp <- bSig[P, P, drop = FALSE]; bSig[j, P] <- b_j %*% bSpp; bSig[P, j] <- t(bSig[j, P, drop = FALSE])
    var_term = (sig_cond / mm$f[j]) * sum(diag(Spp %*% solve(mm$Spp_sel[[j]]))); bSig[j, j] = -(j / mm$f[j]) * sig_cond + as.numeric(b_j %*% bSpp %*% t(b_j)) + var_term }
  return(bSig)
}
alpha_expected <- function(mm, N) {                 # alpha summed over E[missing units] at size N
  alpha <- numeric(k)
  for (key in names(mm$pm)) { P <- mm$pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    U <- solve(Sig0[O, O, drop = FALSE]); B0 <- Sig0[M, O, drop = FALSE] %*% U; S0i <- solve(Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE])
    for (s in 1:(k - p)) { E <- Epert(s); dS <- E[M, M, drop = FALSE] - E[M, O, drop = FALSE] %*% t(B0) - B0 %*% E[O, M, drop = FALSE] + B0 %*% E[O, O, drop = FALSE] %*% t(B0)
      alpha[p + s] <- alpha[p + s] - 0.5 * nP * sum(diag(S0i %*% dS)) } }
  return(alpha)
}
hphi_expected <- function(mm, N) {
  H <- matrix(0, k, k)
  for (key in names(mm$pm)) { P <- mm$pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    U <- solve(Sig0[O, O, drop = FALSE]); B0 <- Sig0[M, O, drop = FALSE] %*% U; S0i <- solve(Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE])
    m1 <- P$m1; M2 <- P$M2
    Dmu <- matrix(0, length(M), p); for (jj in seq_along(M)) { Dmu[jj, M[jj]] <- 1 }; Dmu[, O] <- -B0
    GU <- vector("list", k - p); Gs <- vector("list", k - p)
    for (s in 1:(k - p)) { E <- Epert(s); G <- E[M, O, drop = FALSE] - B0 %*% E[O, O, drop = FALSE]; Gs[[s]] <- G; GU[[s]] <- G %*% U }
    Hp <- matrix(0, k, k); Hp[1:p, 1:p] <- - t(Dmu) %*% S0i %*% Dmu
    for (s in 1:(k - p)) { v <- as.numeric(GU[[s]] %*% m1); col <- - t(Dmu) %*% (S0i %*% v); Hp[1:p, p + s] <- col; Hp[p + s, 1:p] <- col }
    for (a in 1:(k - p)) { for (b in a:(k - p)) {
      qpart = - sum(diag(t(GU[[a]]) %*% S0i %*% GU[[b]] %*% M2))
      tpart = 0.5 * sum(diag(S0i %*% (Gs[[a]] %*% U %*% t(Gs[[b]]) + Gs[[b]] %*% U %*% t(Gs[[a]]))))
      Hp[p + a, p + b] <- qpart + tpart; Hp[p + b, p + a] <- Hp[p + a, p + b] } }
    H <- H + nP * Hp }
  return(H)
}

cat("\n== Term-A closed form (A)+(C)_inf [fully analytic]: MAR (design-imbalance) vs MCAR (control) ==\n")
cat(sprintf("%-6s %10s %10s %12s\n", "mech", "(A)", "(C)", "(A)+(C)"))
for (cell in list(list(m = "MAR", f = amp_mar), list(m = "MCAR", f = amp_mcar))) {
  mm <- est_moments(cell$f, N_arg, R_mom)
  bSig <- compute_bSigma(mm); bvech <- bSig[lower.tri(bSig, diag = TRUE)]
  al <- alpha_expected(mm, N_arg); Hphi <- hphi_expected(mm, N_arg)
  A = sum(al * c(numeric(p), bvech) / N_arg)
  C = 0.5 * sum(diag(Hphi %*% solve(mm$Iobs)))
  cat(sprintf("%-6s %+10.4f %+10.4f %+12.4f\n", cell$m, A, C, A + C))
}
cat("\n  [MAR (A)+(C) ~ -0.22 (design imbalance); MCAR (A)+(C) ~ 0 (control). Fully analytic, no finite diff.]\n")
