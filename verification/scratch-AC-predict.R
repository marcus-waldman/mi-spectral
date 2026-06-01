# scratch-AC-predict.R  [EXPLORATORY — Phase 3a, todo/010]
#
# Step 4 (B2 harness): predict (A)+(C) for the monotone MAR pattern by COMBINING the
# analytic b_Sigma (per-step recursion) with the validated numeric machinery for the
# entropy gradient alpha (= g_bar), the curvature H, and the observed info I_obs, all at
# CONSISTENT N (never mixing scales -- the mistake term-a-mar-asymptote.R made). Compares:
#
#   (A)+(C)_meas = E[A_rb] - tr_obs                          (precise, Rao-Blackwellized)
#   (A)+(C)_pred = alpha^T (b_Sigma/N) + 1/2 tr(H I_obs^-1) - tr_obs
#                = A_pred                + C_pred
#
# against each other and the phase-8 S2-monotone asymptote (-0.11/-0.18/-0.27 at N=300/800/1500).
# alpha=g_bar, H=H_bar from finite differences of the exact Term-A integrand (barQ_fiml_analytic)
# at theta_0; b_Sigma analytic. If A_pred uses the analytic bias and reproduces the measured
# (A)+(C), the closed form is validated.
#
# Usage: Rscript verification/scratch-AC-predict.R [R_ac] [R_gh] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_ac    = if (length(args) >= 1) { as.integer(args[1]) } else { 20000 }
R_gh    = if (length(args) >= 2) { as.integer(args[2]) } else { 400 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

mu0 <- default_mu
Sig0 <- default_Sigma
p = length(mu0)
k = p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)
Ngrid <- c(300, 800, 1500)

# ---- packing + exact Term-A integrand machinery (from term-a-mar-general.R) ------------
pack <- function(theta) { return(c(theta$mu, theta$Sigma[lower.tri(theta$Sigma, diag = TRUE)])) }
unpack <- function(par) {
  mu <- par[1:p]
  S <- matrix(0, p, p)
  S[lower.tri(S, diag = TRUE)] <- par[(p + 1):k]
  S[upper.tri(S)] <- t(S)[upper.tri(S)]
  return(list(mu = mu, Sigma = S))
}
par0 <- pack(theta0)
A_of_par <- function(par, Y, R) {
  th <- unpack(par)
  return(barQ_fiml_analytic(th, th, Y, R) - barQ_fiml_analytic(th, theta0, Y, R))
}
grad_hess_A <- function(Y, R, h = 1e-3) {
  g <- numeric(k); H <- matrix(0, k, k)
  fp <- numeric(k); fm <- numeric(k)
  for (i in 1:k) {
    ei <- numeric(k); ei[i] <- h
    fp[i] <- A_of_par(par0 + ei, Y, R); fm[i] <- A_of_par(par0 - ei, Y, R)
    g[i] <- (fp[i] - fm[i]) / (2 * h)
    H[i, i] <- (fp[i] + fm[i]) / (h^2)
  }
  for (i in 1:(k - 1)) {
    for (j in (i + 1):k) {
      eij <- numeric(k); eij[i] <- h; eij[j] <- h
      eimj <- numeric(k); eimj[i] <- h; eimj[j] <- -h
      fpp <- A_of_par(par0 + eij, Y, R); fpm <- A_of_par(par0 + eimj, Y, R)
      fmp <- A_of_par(par0 - eimj, Y, R); fmm <- A_of_par(par0 - eij, Y, R)
      H[i, j] <- (fpp - fpm - fmp + fmm) / (4 * h^2); H[j, i] <- H[i, j]
    }
  }
  return(list(g = g, H = H))
}

# ---- fast closed-form k-step monotone MLE ---------------------------------------------
fiml_monotone_kstep <- function(Y, R) {
  obs_through <- function(j) { if (j == 1) { return(R[, 1] == 0) } else { return(rowSums(R[, 1:j, drop = FALSE]) == 0) } }
  mu <- numeric(p); Sigma <- matrix(0, p, p)
  s1 <- obs_through(1); x1 <- Y[s1, 1]
  mu[1] = mean(x1); Sigma[1, 1] = mean((x1 - mu[1])^2)
  for (j in 2:p) {
    sj <- obs_through(j)
    Xpred <- cbind(1, Y[sj, 1:(j - 1), drop = FALSE]); yj <- Y[sj, j]
    coef <- solve(crossprod(Xpred), crossprod(Xpred, yj)); b_j <- coef[-1]
    v_j = mean((yj - Xpred %*% coef)^2)
    Sig_prev <- Sigma[1:(j - 1), 1:(j - 1), drop = FALSE]
    mu[j] = coef[1] + sum(b_j * mu[1:(j - 1)])
    Sigma[j, 1:(j - 1)] <- as.numeric(b_j %*% Sig_prev); Sigma[1:(j - 1), j] <- Sigma[j, 1:(j - 1)]
    Sigma[j, j] = v_j + as.numeric(b_j %*% Sig_prev %*% b_j)
  }
  return(list(mu = mu, Sigma = Sigma))
}

# ---- analytic b_Sigma (per-step recursion + selected design moments) -------------------
est_selected_moments <- function(N_sel, R_sel) {
  sxx <- vector("list", p); sx <- vector("list", p); cnt <- numeric(p)
  for (j in 1:p) { sxx[[j]] <- matrix(0, p, p); sx[[j]] <- numeric(p) }
  for (r in 1:R_sel) {
    set.seed(77000 + r)
    X <- gen_data(N_sel, mu0, Sig0)
    Rm <- apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone")$R
    for (j in 1:p) {
      sel = if (j == 1) { Rm[, 1] == 0 } else { rowSums(Rm[, 1:j, drop = FALSE]) == 0 }
      cnt[j] = cnt[j] + sum(sel)
      if (j >= 2) {
        Xp <- X[sel, 1:(j - 1), drop = FALSE]
        sxx[[j]][1:(j - 1), 1:(j - 1)] <- sxx[[j]][1:(j - 1), 1:(j - 1)] + crossprod(Xp)
        sx[[j]][1:(j - 1)] <- sx[[j]][1:(j - 1)] + colSums(Xp)
      }
    }
  }
  f <- cnt / (N_sel * R_sel); Spp_sel <- vector("list", p)
  for (j in 2:p) { P = 1:(j - 1); mxx <- sxx[[j]][P, P, drop = FALSE] / cnt[j]; mx <- sx[[j]][P] / cnt[j]; Spp_sel[[j]] <- mxx - outer(mx, mx) }
  return(list(f = f, Spp_sel = Spp_sel))
}
compute_bSigma <- function(sm) {
  bSig <- matrix(0, p, p); bSig[1, 1] = -Sig0[1, 1]
  for (j in 2:p) {
    P = 1:(j - 1); Spp <- Sig0[P, P, drop = FALSE]
    b_j <- Sig0[j, P, drop = FALSE] %*% solve(Spp)
    sig_cond = as.numeric(Sig0[j, j] - b_j %*% Sig0[P, j])
    bSpp <- bSig[P, P, drop = FALSE]
    bSig[j, P] <- b_j %*% bSpp; bSig[P, j] <- t(bSig[j, P, drop = FALSE])
    var_term = (sig_cond / sm$f[j]) * sum(diag(Spp %*% solve(sm$Spp_sel[[j]])))
    bSig[j, j] = -(j / sm$f[j]) * sig_cond + as.numeric(b_j %*% bSpp %*% t(b_j)) + var_term
  }
  return(bSig)
}

cat("\n== (A)+(C) predictor: analytic b_Sigma + numeric alpha/H/I_obs, monotone MAR ==\n")
sm <- est_selected_moments(20000, 300)
bSig <- compute_bSigma(sm)
bSig_vech <- bSig[lower.tri(bSig, diag = TRUE)]
Edelta_Sig <- bSig_vech                       # per-unit: E[delta]_Sigma = b_Sigma / N (apply /N below)

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "pack", "unpack",
                    "A_of_par", "grad_hess_A", "fiml_monotone_kstep"))

ac_one <- function(r, N) {
  set.seed(20260601 + r)
  X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone"), error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  to <- tryCatch(fiml_monotone_kstep(mar$Y, mar$R), error = function(e) { return(NULL) })
  if (is.null(to)) { return(NULL) }
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, theta0, mar$Y, mar$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), fisher_info_com_mvn(to, N)))) - k
  return(c(A_rb = A_rb, tr_obs = tr_obs))
}
gh_one <- function(r, N) {
  set.seed(990000 + r)
  X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone"), error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  gh <- grad_hess_A(mar$Y, mar$R)
  Iobs <- observed_info_obs_mvn(theta0, mar$Y, mar$R)   # at theta_0 (Var(delta)->I_obs^-1)
  return(list(g = gh$g, H = gh$H, Iobs = Iobs))
}

clusterExport(cl, c("ac_one", "gh_one"))
cat(sprintf("%-6s %12s %12s %12s %12s %12s\n", "N", "AC_meas", "AC_pred", "A_pred", "C_pred", "phase8"))
phase8 <- c("300" = -0.111, "800" = -0.179, "1500" = -0.270)
for (N in Ngrid) {
  clusterExport(cl, "N")
  Mac <- do.call(rbind, Filter(Negate(is.null), parLapply(cl, seq_len(R_ac), function(r) { return(ac_one(r, N)) })))
  AC_meas = mean(Mac[, "A_rb"]) - mean(Mac[, "tr_obs"])
  AC_mcse = sd(Mac[, "A_rb"]) / sqrt(nrow(Mac))
  gh <- Filter(Negate(is.null), parLapply(cl, seq_len(R_gh), function(r) { return(gh_one(r, N)) }))
  g_bar <- Reduce(`+`, lapply(gh, `[[`, "g")) / length(gh)
  H_bar <- Reduce(`+`, lapply(gh, `[[`, "H")) / length(gh)
  Iobs_bar <- Reduce(`+`, lapply(gh, `[[`, "Iobs")) / length(gh)
  Edelta <- c(numeric(p), Edelta_Sig / N)               # mu bias ignored (alpha_mu~0)
  A_pred = sum(g_bar * Edelta)
  C_pred = 0.5 * sum(diag(H_bar %*% solve(Iobs_bar))) - mean(Mac[, "tr_obs"])
  AC_pred = A_pred + C_pred
  cat(sprintf("%-6d %+8.4f(%.3f) %+12.4f %+12.4f %+12.4f %12s\n",
              N, AC_meas, AC_mcse, AC_pred, A_pred, C_pred,
              if (as.character(N) %in% names(phase8)) { sprintf("%+.3f", phase8[[as.character(N)]]) } else { "-" }))
}
cat("\n  [AC_pred should track AC_meas and the phase8 column; closed-form value = limit of AC_pred as N->inf]\n")
