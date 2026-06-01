# scratch-AC-asymptote.R  [EXPLORATORY — Phase 3a, todo/010]
#
# Lean (A)+(C) evaluator for the monotone MAR pattern, combining:
#   (A) = alpha^T (b_Sigma / N)          alpha analytic (validated), b_Sigma analytic (recursion)
#   (C) = 1/2 tr(H I_obs^-1) - tr(RIV)   H finite-diff at theta_0, I_obs/tr_obs numeric at theta_0
# One loop per N (R reps, one ampute each) gives H_bar, I_obs_bar, tr_obs_bar, and a sanity
# AC_meas = E[A_rb] - tr_obs. AC_pred should track AC_meas and the phase-8 monotone curve
# (-0.111/-0.179/-0.270 at N=300/800/1500) and stabilize at the asymptote as N grows.
#
# Usage: Rscript verification/scratch-AC-asymptote.R [R] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_arg   = if (length(args) >= 1) { as.integer(args[1]) } else { 600 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p = length(mu0)
k = p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
Ngrid <- c(300, 800, 1500, 3000)
phase8 <- c("300" = -0.111, "800" = -0.179, "1500" = -0.270, "3000" = NA)

pack <- function(theta) { return(c(theta$mu, theta$Sigma[lower.tri(theta$Sigma, diag = TRUE)])) }
unpack <- function(par) {
  mu <- par[1:p]; S <- matrix(0, p, p)
  S[lower.tri(S, diag = TRUE)] <- par[(p + 1):k]; S[upper.tri(S)] <- t(S)[upper.tri(S)]
  return(list(mu = mu, Sigma = S))
}
par0 <- pack(theta0)
A_of_par <- function(par, Y, R) { th <- unpack(par); return(barQ_fiml_analytic(th, th, Y, R) - barQ_fiml_analytic(th, theta0, Y, R)) }
hess_A <- function(Y, R, h = 1e-3) {
  H <- matrix(0, k, k); fp <- numeric(k); fm <- numeric(k)
  for (i in 1:k) { ei <- numeric(k); ei[i] <- h; fp[i] <- A_of_par(par0 + ei, Y, R); fm[i] <- A_of_par(par0 - ei, Y, R); H[i, i] <- (fp[i] + fm[i]) / (h^2) }
  for (i in 1:(k - 1)) { for (j in (i + 1):k) {
    eij <- numeric(k); eij[i] <- h; eij[j] <- h; eimj <- numeric(k); eimj[i] <- h; eimj[j] <- -h
    H[i, j] <- (A_of_par(par0 + eij, Y, R) - A_of_par(par0 + eimj, Y, R) - A_of_par(par0 - eimj, Y, R) + A_of_par(par0 - eij, Y, R)) / (4 * h^2)
    H[j, i] <- H[i, j]
  } }
  return(H)
}
Epert <- function(s) { i = lt[s, 1]; j = lt[s, 2]; E <- matrix(0, p, p); E[i, j] <- 1; E[j, i] <- 1; return(E) }
alpha_analytic <- function(R) {
  patt <- apply(R, 1, function(row) { return(paste(row, collapse = "")) }); alpha <- numeric(k)
  for (pp in unique(patt)) {
    rows <- which(patt == pp); n_pat = length(rows); Rp <- R[rows[1], ]
    M <- which(Rp == 1); O <- which(Rp == 0); if (length(M) == 0) { next }
    Soo_inv <- solve(Sig0[O, O, drop = FALSE]); B <- Sig0[M, O, drop = FALSE] %*% Soo_inv
    S0inv <- solve(Sig0[M, M, drop = FALSE] - B %*% Sig0[O, M, drop = FALSE])
    for (s in 1:(k - p)) {
      E <- Epert(s); dS <- E[M, M, drop = FALSE] - E[M, O, drop = FALSE] %*% t(B) - B %*% E[O, M, drop = FALSE] + B %*% E[O, O, drop = FALSE] %*% t(B)
      alpha[p + s] <- alpha[p + s] - 0.5 * n_pat * sum(diag(S0inv %*% dS))
    }
  }
  return(alpha)
}
fiml_monotone_kstep <- function(Y, R) {
  obs_through <- function(j) { if (j == 1) { return(R[, 1] == 0) } else { return(rowSums(R[, 1:j, drop = FALSE]) == 0) } }
  mu <- numeric(p); Sigma <- matrix(0, p, p); s1 <- obs_through(1); x1 <- Y[s1, 1]
  mu[1] = mean(x1); Sigma[1, 1] = mean((x1 - mu[1])^2)
  for (j in 2:p) {
    sj <- obs_through(j); Xpred <- cbind(1, Y[sj, 1:(j - 1), drop = FALSE]); yj <- Y[sj, j]
    coef <- solve(crossprod(Xpred), crossprod(Xpred, yj)); b_j <- coef[-1]; v_j = mean((yj - Xpred %*% coef)^2)
    Sig_prev <- Sigma[1:(j - 1), 1:(j - 1), drop = FALSE]; mu[j] = coef[1] + sum(b_j * mu[1:(j - 1)])
    Sigma[j, 1:(j - 1)] <- as.numeric(b_j %*% Sig_prev); Sigma[1:(j - 1), j] <- Sigma[j, 1:(j - 1)]
    Sigma[j, j] = v_j + as.numeric(b_j %*% Sig_prev %*% b_j)
  }
  return(list(mu = mu, Sigma = Sigma))
}

# ---- analytic b_Sigma (selected moments + recursion) ----------------------------------
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
Edelta_unit <- c(numeric(p), bSig_vech)          # b_Sigma (apply /N per N below); mu ignored (alpha_mu=0)

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "lt", "pack", "unpack",
                    "A_of_par", "hess_A", "Epert", "alpha_analytic", "fiml_monotone_kstep"))

one <- function(r, N) {
  set.seed(20260601 + r); X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone"), error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  to <- tryCatch(fiml_monotone_kstep(mar$Y, mar$R), error = function(e) { return(NULL) }); if (is.null(to)) { return(NULL) }
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, theta0, mar$Y, mar$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), fisher_info_com_mvn(to, N)))) - k
  H <- hess_A(mar$Y, mar$R); Iobs <- observed_info_obs_mvn(theta0, mar$Y, mar$R); al <- alpha_analytic(mar$R)
  return(list(A_rb = A_rb, tr_obs = tr_obs, H = H, Iobs = Iobs, al = al))
}

cat("\n== (A)+(C) asymptote evaluator (analytic alpha + analytic b_Sigma + numeric H/I_obs), monotone MAR ==\n")
cat(sprintf("  f_j: %s\n", paste(sprintf("%.4f", sm$f), collapse = " ")))
cat(sprintf("%-6s %14s %12s %12s %12s %10s\n", "N", "AC_meas", "AC_pred", "A_pred", "C_pred", "phase8"))
clusterExport(cl, "one")
for (N in Ngrid) {
  clusterExport(cl, "N")
  res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_arg), function(r) { return(one(r, N)) }))
  nok = length(res)
  A_rb <- sapply(res, `[[`, "A_rb"); tr_obs <- sapply(res, `[[`, "tr_obs")
  H_bar <- Reduce(`+`, lapply(res, `[[`, "H")) / nok
  Iobs_bar <- Reduce(`+`, lapply(res, `[[`, "Iobs")) / nok
  al_bar <- Reduce(`+`, lapply(res, `[[`, "al")) / nok
  A_pred = sum(al_bar * (Edelta_unit / N))
  C_pred = 0.5 * sum(diag(H_bar %*% solve(Iobs_bar))) - mean(tr_obs)
  AC_meas = mean(A_rb) - mean(tr_obs); AC_mcse = sd(A_rb) / sqrt(nok)
  cat(sprintf("%-6d %+8.4f(%.3f) %+12.4f %+12.4f %+12.4f %10s\n",
              N, AC_meas, AC_mcse, A_pred + C_pred, A_pred, C_pred,
              if (!is.na(phase8[[as.character(N)]])) { sprintf("%+.3f", phase8[[as.character(N)]]) } else { "-" }))
}
cat("\n  [AC_pred = closed-form prediction; should track AC_meas/phase8 and stabilize at the asymptote]\n")
