# scratch-hphi-analytic.R  [EXPLORATORY — Phase 3a, todo/011]
#
# Analytic cross-entropy curvature H_phi = grad^2_phi f_0(phi)|_{theta_0}, replacing the
# finite-difference of barQ(theta_0, .). Per missing unit (blocks M|O, e_O = y_O - mu0_O):
#   f_0 = const - 1/2[ e_bar^T Sig0^{-1} e_bar + tr(S0^{-1} S_phi) ],  e_bar = (e_O ; m_phi - mu0_M).
# At theta_0, (Sig0^{-1} e_bar)_M = 0 (block-inverse identity), so the 2nd-derivative-of-mean term
# drops and the Hessian is, per unit,
#   H_phi = -J_d^T S0^{-1} J_d  +  (T-part, Sigma-Sigma only),
#   J_d = d m_phi/d phi:  mu-block deterministic (I on M, -B0 on O);  Sigma-block = G_a U e_O,
#   G_a = (E_a)_{MO} - B0 (E_a)_{OO},  U = Sig0_{OO}^{-1},  B0 = Sig0_{MO} U,  S0 = Schur complement.
#   T-part[a,b] = 1/2 tr( S0^{-1} (G_a U G_b^T + G_b U G_a^T) )   (from d^2 tr(S0^{-1} S_phi)).
# Expectations over a pattern reduce to the SELECTED moments of e_O: m1_P=E[e_O|P], M2_P=E[e_O e_O^T|P].
#   H[mu,mu]  = -Dmu^T S0^{-1} Dmu                                   (deterministic)
#   H[mu,a]   = -Dmu^T S0^{-1} G_a U m1_P                            (linear in selected mean shift)
#   H[a,b]    = -tr((G_a U)^T S0^{-1} (G_b U) M2_P)  +  T-part[a,b]  (quadratic in selected 2nd moment)
# E[H_phi] = sum_patterns n_P * H_P. Validated here against the finite-diff H_bar and against
# C = 1/2 tr(H_phi I_obs^{-1}) ~ -0.76 (scratch-AC-pathb.R).
#
# Usage: Rscript verification/scratch-hphi-analytic.R [N] [R_fd] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
N_arg   = if (length(args) >= 1) { as.integer(args[1]) } else { 1500 }
R_fd    = if (length(args) >= 2) { as.integer(args[2]) } else { 200 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p = length(mu0)
k = p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
Epert <- function(s) { i = lt[s, 1]; j = lt[s, 2]; E <- matrix(0, p, p); E[i, j] <- 1; E[j, i] <- 1; return(E) }

# ---- per-missing-pattern selected moments of e_O = y_O - mu0_O (at theta_0) ------------
est_pattern_moments <- function(N_sel, R_sel) {
  acc <- list()   # keyed by pattern string -> list(count, s1 (full p), s2 (full pxp), O)
  for (r in 1:R_sel) {
    set.seed(880000 + r); X <- gen_data(N_sel, mu0, Sig0)
    mar <- apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone")
    Rm <- mar$R; patt <- apply(Rm, 1, function(row) { return(paste(row, collapse = "")) })
    for (pp in unique(patt)) {
      Rp <- Rm[which(patt == pp)[1], ]; O <- which(Rp == 0); if (length(O) == p) { next }  # skip complete
      rows <- which(patt == pp); e <- sweep(X[rows, O, drop = FALSE], 2, mu0[O], FUN = "-")  # n x |O|
      key <- pp
      if (is.null(acc[[key]])) { acc[[key]] <- list(count = 0, s1 = numeric(p), s2 = matrix(0, p, p), O = O, M = which(Rp == 1)) }
      acc[[key]]$count <- acc[[key]]$count + nrow(e)
      acc[[key]]$s1[O] <- acc[[key]]$s1[O] + colSums(e)
      acc[[key]]$s2[O, O] <- acc[[key]]$s2[O, O] + crossprod(e)
    }
  }
  out <- list()
  for (key in names(acc)) {
    a <- acc[[key]]; O <- a$O
    out[[key]] <- list(frac = a$count / (N_sel * R_sel), m1 = a$s1[O] / a$count,
                       M2 = a$s2[O, O, drop = FALSE] / a$count, O = O, M = a$M)
  }
  return(out)
}

# ---- analytic E[H_phi] at sample size N ------------------------------------------------
hphi_expected <- function(pm, N) {
  H <- matrix(0, k, k)
  for (key in names(pm)) {
    P <- pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    U <- solve(Sig0[O, O, drop = FALSE]); B0 <- Sig0[M, O, drop = FALSE] %*% U
    S0 <- Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE]; S0i <- solve(S0)
    m1 <- P$m1; M2 <- P$M2
    # Dmu: |M| x p  (d m_phi / d mu): col j in M -> indicator; col j in O -> -B0[,j]; else 0
    Dmu <- matrix(0, length(M), p)
    for (jj in seq_along(M)) { Dmu[jj, M[jj]] <- 1 }
    Dmu[, O] <- -B0
    # G_s U  for each Sigma param s  (|M| x |O|)
    GU <- vector("list", k - p)
    for (s in 1:(k - p)) { E <- Epert(s); G <- E[M, O, drop = FALSE] - B0 %*% E[O, O, drop = FALSE]; GU[[s]] <- G %*% U }
    Hp <- matrix(0, k, k)
    # mu,mu block (deterministic)
    Hp[1:p, 1:p] <- - t(Dmu) %*% S0i %*% Dmu
    # mu,Sigma block (linear in m1): H[j, p+s] = - Dmu[,j]^T S0i (G_s U m1)
    for (s in 1:(k - p)) {
      v <- as.numeric(GU[[s]] %*% m1)            # |M|
      col <- - t(Dmu) %*% (S0i %*% v)            # p
      Hp[1:p, p + s] <- col; Hp[p + s, 1:p] <- col
    }
    # Sigma,Sigma block: Q-part - tr((G_a U)^T S0i (G_b U) M2) ; T-part 1/2 tr(S0i(GaU Gb^T + GbU Ga^T))...
    # note G_b^T below uses G_b (|M|x|O|) so G_a U G_b^T is |M|x|M|; reconstruct G from GU: G = (GU) %*% solve(U)?
    # simpler: recompute G_s alongside GU.
    Gs <- vector("list", k - p)
    for (s in 1:(k - p)) { E <- Epert(s); Gs[[s]] <- E[M, O, drop = FALSE] - B0 %*% E[O, O, drop = FALSE] }
    for (a in 1:(k - p)) { for (b in a:(k - p)) {
      qpart = - sum(diag( t(GU[[a]]) %*% S0i %*% GU[[b]] %*% M2 ))
      tpart = 0.5 * sum(diag( S0i %*% (Gs[[a]] %*% U %*% t(Gs[[b]]) + Gs[[b]] %*% U %*% t(Gs[[a]])) ))
      Hp[p + a, p + b] <- qpart + tpart; Hp[p + b, p + a] <- Hp[p + a, p + b]
    } }
    H <- H + nP * Hp
  }
  return(H)
}

# ---- finite-diff H_bar (validation target) --------------------------------------------
pack <- function(theta) { return(c(theta$mu, theta$Sigma[lower.tri(theta$Sigma, diag = TRUE)])) }
unpack <- function(par) { mu <- par[1:p]; S <- matrix(0, p, p); S[lower.tri(S, diag = TRUE)] <- par[(p + 1):k]; S[upper.tri(S)] <- t(S)[upper.tri(S)]; return(list(mu = mu, Sigma = S)) }
par0 <- pack(theta0)
f_phi <- function(par, Y, R) { return(barQ_fiml_analytic(theta0, unpack(par), Y, R)) }
hess_phi <- function(Y, R, h = 1e-3) {
  H <- matrix(0, k, k); f0 <- f_phi(par0, Y, R)
  fp <- numeric(k); fm <- numeric(k)
  for (i in 1:k) { ei <- numeric(k); ei[i] <- h; fp[i] <- f_phi(par0 + ei, Y, R); fm[i] <- f_phi(par0 - ei, Y, R); H[i, i] <- (fp[i] - 2 * f0 + fm[i]) / (h^2) }
  for (i in 1:(k - 1)) { for (j in (i + 1):k) { eij <- numeric(k); eij[i] <- h; eij[j] <- h; eimj <- numeric(k); eimj[i] <- h; eimj[j] <- -h
    H[i, j] <- (f_phi(par0 + eij, Y, R) - f_phi(par0 + eimj, Y, R) - f_phi(par0 - eimj, Y, R) + f_phi(par0 - eij, Y, R)) / (4 * h^2); H[j, i] <- H[i, j] } }
  return(H)
}

cat(sprintf("\n== analytic H_phi vs finite-diff (monotone MAR, N=%d, R_fd=%d) ==\n", N_arg, R_fd))
pm <- est_pattern_moments(20000, 300)
cat(sprintf("  missing patterns: %s (fracs %s)\n", paste(names(pm), collapse = ","),
            paste(sprintf("%.3f", sapply(pm, function(z) { return(z$frac) })), collapse = ",")))
H_an <- hphi_expected(pm, N_arg)

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "pack", "unpack", "f_phi", "hess_phi", "N_arg"))
one <- function(r) {
  set.seed(20260601 + r); X <- gen_data(N_arg, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone"), error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  Iobs <- observed_info_obs_mvn(theta0, mar$Y, mar$R)
  return(list(H = hess_phi(mar$Y, mar$R), Iobs = Iobs))
}
clusterExport(cl, "one")
res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_fd), one))
H_fd <- Reduce(`+`, lapply(res, `[[`, "H")) / length(res)
Iobs_bar <- Reduce(`+`, lapply(res, `[[`, "Iobs")) / length(res)

mu_idx <- 1:p; sig_idx <- (p + 1):k
blkmax <- function(ai, bi) { return(max(abs((H_an - H_fd)[ai, bi, drop = FALSE]))) }
cat(sprintf("  max|H_an - H_fd| by block:  mu-mu (DETERMINISTIC) = %.4e ;  mu-Sigma = %.4e ;  Sigma-Sigma = %.4e\n",
            blkmax(mu_idx, mu_idx), blkmax(mu_idx, sig_idx), blkmax(sig_idx, sig_idx)))
cat(sprintf("  mu-mu block |H_fd| range = [%.2f, %.2f]  (if det. block matches => analytic structure correct)\n",
            min(abs(H_fd[mu_idx, mu_idx])), max(abs(H_fd[mu_idx, mu_idx]))))
cat(sprintf("  overall max|H_an - H_fd|             = %.4e\n", max(abs(H_an - H_fd))))
cat(sprintf("  (C) = 1/2 tr(H_an  I_obs^-1)         = %+.4f\n", 0.5 * sum(diag(H_an %*% solve(Iobs_bar)))))
cat(sprintf("  (C) = 1/2 tr(H_fd  I_obs^-1)         = %+.4f  [target ~ -0.76]\n", 0.5 * sum(diag(H_fd %*% solve(Iobs_bar)))))
