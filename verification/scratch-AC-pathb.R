# scratch-AC-pathb.R  [EXPLORATORY — Phase 3a path b, todo/011]
#
# Exact (C) via the PURE cross-entropy curvature H_phi = grad^2_phi f_0(phi)|_{theta_0},
# where f_0(phi) = barQ_fiml_analytic(theta_eval = theta_0, theta_obs = phi, Y, R) =
# E_{X_M ~ phi}[ log N(X; theta_0) ] summed over missing units. Differentiating ONLY the
# obs/imputation slot (eval fixed at theta_0) excludes the eval-obs cross block that produces
# (B)main = tr(RIV); so the Term-A correction is, cleanly,
#     (A)+(C) = alpha^T E[delta] + (C),   (C) = 1/2 E[delta^T H_phi delta]   (no -tr(RIV)).
# Decoupled asymptote form: (C)_inf = 1/2 tr(H_phi I_obs^{-1}).
#
# Reports, per N: (A) = alpha_analytic^T (b_Sigma/N); (C) THREE ways
#   (C)_coupled   = mean 1/2 delta^T H_phi delta            (exact finite-N (C))
#   (C)_decVar    = 1/2 tr(Hphi_bar * mean(delta delta^T))  (decoupling test: differs by Cov(H,dd))
#   (C)_decIobs   = 1/2 tr(Hphi_bar * Iobs_bar^{-1})         (asymptote form)
# and the measured (A)+(C) = E[A_rb] - tr_obs. Cross-checks: grad of f_0 == alpha; and
# (A)+(C)_coupled should track measured (A)+(C).
#
# Usage: Rscript verification/scratch-AC-pathb.R [R] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_arg   = if (length(args) >= 1) { as.integer(args[1]) } else { 800 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p = length(mu0)
k = p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
Ngrid <- c(300, 800, 1500)

pack <- function(theta) { return(c(theta$mu, theta$Sigma[lower.tri(theta$Sigma, diag = TRUE)])) }
unpack <- function(par) {
  mu <- par[1:p]; S <- matrix(0, p, p)
  S[lower.tri(S, diag = TRUE)] <- par[(p + 1):k]; S[upper.tri(S)] <- t(S)[upper.tri(S)]
  return(list(mu = mu, Sigma = S))
}
par0 <- pack(theta0)
# f_0(phi) = barQ(eval = theta_0, obs = phi): the cross-entropy (eval slot FIXED at theta_0)
f_phi <- function(par, Y, R) { return(barQ_fiml_analytic(theta0, unpack(par), Y, R)) }
grad_hess_phi <- function(Y, R, h = 1e-3) {
  g <- numeric(k); H <- matrix(0, k, k); f0 <- f_phi(par0, Y, R); fp <- numeric(k); fm <- numeric(k)
  for (i in 1:k) { ei <- numeric(k); ei[i] <- h; fp[i] <- f_phi(par0 + ei, Y, R); fm[i] <- f_phi(par0 - ei, Y, R)
    g[i] <- (fp[i] - fm[i]) / (2 * h); H[i, i] <- (fp[i] - 2 * f0 + fm[i]) / (h^2) }
  for (i in 1:(k - 1)) { for (j in (i + 1):k) {
    eij <- numeric(k); eij[i] <- h; eij[j] <- h; eimj <- numeric(k); eimj[i] <- h; eimj[j] <- -h
    H[i, j] <- (f_phi(par0 + eij, Y, R) - f_phi(par0 + eimj, Y, R) - f_phi(par0 - eimj, Y, R) + f_phi(par0 - eij, Y, R)) / (4 * h^2)
    H[j, i] <- H[i, j] } }
  return(list(g = g, H = H))
}
Epert <- function(s) { i = lt[s, 1]; j = lt[s, 2]; E <- matrix(0, p, p); E[i, j] <- 1; E[j, i] <- 1; return(E) }
alpha_analytic <- function(R) {
  patt <- apply(R, 1, function(row) { return(paste(row, collapse = "")) }); alpha <- numeric(k)
  for (pp in unique(patt)) {
    rows <- which(patt == pp); n_pat = length(rows); Rp <- R[rows[1], ]
    M <- which(Rp == 1); O <- which(Rp == 0); if (length(M) == 0) { next }
    Soo_inv <- solve(Sig0[O, O, drop = FALSE]); B <- Sig0[M, O, drop = FALSE] %*% Soo_inv
    S0inv <- solve(Sig0[M, M, drop = FALSE] - B %*% Sig0[O, M, drop = FALSE])
    for (s in 1:(k - p)) { E <- Epert(s)
      dS <- E[M, M, drop = FALSE] - E[M, O, drop = FALSE] %*% t(B) - B %*% E[O, M, drop = FALSE] + B %*% E[O, O, drop = FALSE] %*% t(B)
      alpha[p + s] <- alpha[p + s] - 0.5 * n_pat * sum(diag(S0inv %*% dS)) }
  }
  return(alpha)
}
fiml_monotone_kstep <- function(Y, R) {
  obs_through <- function(j) { if (j == 1) { return(R[, 1] == 0) } else { return(rowSums(R[, 1:j, drop = FALSE]) == 0) } }
  mu <- numeric(p); Sigma <- matrix(0, p, p); s1 <- obs_through(1); x1 <- Y[s1, 1]
  mu[1] = mean(x1); Sigma[1, 1] = mean((x1 - mu[1])^2)
  for (j in 2:p) { sj <- obs_through(j); Xpred <- cbind(1, Y[sj, 1:(j - 1), drop = FALSE]); yj <- Y[sj, j]
    coef <- solve(crossprod(Xpred), crossprod(Xpred, yj)); b_j <- coef[-1]; v_j = mean((yj - Xpred %*% coef)^2)
    Sig_prev <- Sigma[1:(j - 1), 1:(j - 1), drop = FALSE]; mu[j] = coef[1] + sum(b_j * mu[1:(j - 1)])
    Sigma[j, 1:(j - 1)] <- as.numeric(b_j %*% Sig_prev); Sigma[1:(j - 1), j] <- Sigma[j, 1:(j - 1)]
    Sigma[j, j] = v_j + as.numeric(b_j %*% Sig_prev %*% b_j) }
  return(list(mu = mu, Sigma = Sigma))
}
# analytic b_Sigma (recursion + selected moments)
est_selected_moments <- function(N_sel, R_sel) {
  sxx <- vector("list", p); sx <- vector("list", p); cnt <- numeric(p)
  for (j in 1:p) { sxx[[j]] <- matrix(0, p, p); sx[[j]] <- numeric(p) }
  for (r in 1:R_sel) { set.seed(77000 + r); X <- gen_data(N_sel, mu0, Sig0)
    Rm <- apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone")$R
    for (j in 1:p) { sel = if (j == 1) { Rm[, 1] == 0 } else { rowSums(Rm[, 1:j, drop = FALSE]) == 0 }
      cnt[j] = cnt[j] + sum(sel)
      if (j >= 2) { Xp <- X[sel, 1:(j - 1), drop = FALSE]
        sxx[[j]][1:(j - 1), 1:(j - 1)] <- sxx[[j]][1:(j - 1), 1:(j - 1)] + crossprod(Xp); sx[[j]][1:(j - 1)] <- sx[[j]][1:(j - 1)] + colSums(Xp) } } }
  f <- cnt / (N_sel * R_sel); Spp_sel <- vector("list", p)
  for (j in 2:p) { P = 1:(j - 1); mxx <- sxx[[j]][P, P, drop = FALSE] / cnt[j]; mx <- sx[[j]][P] / cnt[j]; Spp_sel[[j]] <- mxx - outer(mx, mx) }
  return(list(f = f, Spp_sel = Spp_sel))
}
compute_bSigma <- function(sm) {
  bSig <- matrix(0, p, p); bSig[1, 1] = -Sig0[1, 1]
  for (j in 2:p) { P = 1:(j - 1); Spp <- Sig0[P, P, drop = FALSE]
    b_j <- Sig0[j, P, drop = FALSE] %*% solve(Spp); sig_cond = as.numeric(Sig0[j, j] - b_j %*% Sig0[P, j])
    bSpp <- bSig[P, P, drop = FALSE]; bSig[j, P] <- b_j %*% bSpp; bSig[P, j] <- t(bSig[j, P, drop = FALSE])
    var_term = (sig_cond / sm$f[j]) * sum(diag(Spp %*% solve(sm$Spp_sel[[j]])))
    bSig[j, j] = -(j / sm$f[j]) * sig_cond + as.numeric(b_j %*% bSpp %*% t(b_j)) + var_term }
  return(bSig)
}
sm <- est_selected_moments(20000, 300)
bSig <- compute_bSigma(sm)
bSig_vech <- bSig[lower.tri(bSig, diag = TRUE)]

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "lt", "pack", "unpack",
                    "f_phi", "grad_hess_phi", "Epert", "alpha_analytic", "fiml_monotone_kstep"))
one <- function(r, N) {
  set.seed(20260601 + r); X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone"), error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  to <- tryCatch(fiml_monotone_kstep(mar$Y, mar$R), error = function(e) { return(NULL) }); if (is.null(to)) { return(NULL) }
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, theta0, mar$Y, mar$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), fisher_info_com_mvn(to, N)))) - k
  gh <- grad_hess_phi(mar$Y, mar$R); Iobs <- observed_info_obs_mvn(theta0, mar$Y, mar$R)
  al <- alpha_analytic(mar$R); delta <- pack(to) - par0
  return(list(A_rb = A_rb, tr_obs = tr_obs, g = gh$g, H = gh$H, Iobs = Iobs, al = al,
              dd = outer(delta, delta), quad = 0.5 * as.numeric(delta %*% gh$H %*% delta)))
}
clusterExport(cl, "one")
cat("\n== Path b: exact (C) via cross-entropy curvature H_phi (monotone MAR) ==\n")
cat(sprintf("  f_j: %s\n", paste(sprintf("%.4f", sm$f), collapse = " ")))
cat(sprintf("%-6s %10s %10s %10s %10s %10s %12s\n", "N", "A_pred", "C_coupl", "C_decVar", "C_decIobs", "AC_pred", "AC_meas"))
for (N in Ngrid) {
  clusterExport(cl, "N")
  res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_arg), function(r) { return(one(r, N)) }))
  nok = length(res)
  A_rb <- sapply(res, `[[`, "A_rb"); tr_obs <- sapply(res, `[[`, "tr_obs")
  g_bar <- Reduce(`+`, lapply(res, `[[`, "g")) / nok
  H_bar <- Reduce(`+`, lapply(res, `[[`, "H")) / nok
  Iobs_bar <- Reduce(`+`, lapply(res, `[[`, "Iobs")) / nok
  al_bar <- Reduce(`+`, lapply(res, `[[`, "al")) / nok
  dd_bar <- Reduce(`+`, lapply(res, `[[`, "dd")) / nok
  C_coupled = mean(sapply(res, `[[`, "quad"))
  C_decVar  = 0.5 * sum(diag(H_bar %*% dd_bar))
  C_decIobs = 0.5 * sum(diag(H_bar %*% solve(Iobs_bar)))
  A_pred = sum(al_bar * c(numeric(p), bSig_vech) / N)
  AC_meas = mean(A_rb) - mean(tr_obs)
  cat(sprintf("%-6d %+10.4f %+10.4f %+10.4f %+10.4f %+10.4f %+9.4f(%.3f)\n",
              N, A_pred, C_coupled, C_decVar, C_decIobs, A_pred + C_decIobs, AC_meas, sd(A_rb) / sqrt(nok)))
  if (N == Ngrid[1]) { cat(sprintf("    [check] grad f_0 == alpha?  max|g_bar - alpha| = %.2e (cov-only check ok)\n", max(abs(g_bar - al_bar)))) }
}
cat("\n  [AC_pred uses C_decIobs (asymptote form). A_pred+C_coupled should match AC_meas. C_decVar vs C_coupled = decoupling error.]\n")
