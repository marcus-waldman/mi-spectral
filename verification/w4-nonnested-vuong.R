# w4-nonnested-vuong.R  [todo/029 -- the non-nested (Vuong-regime) (A)+(C) differential]
#
# Measures the design-imbalance (A)+(C) differential for a NON-NESTED candidate pair
# (compound symmetry vs AR(1)) -- the only derived-but-never-measured quantity in the paper
# (Proposition L4, derivation.qmd @sec-lrt-ac). PREREGISTERED in todo/029 BEFORE this script
# existed (commit 7677777). The frozen W1/W2/W3 originals and ic-ladder.R are untouched.
#
# Per replicate: fit the saturated MVN by FIML -> E-step moments (m*, S*); fit CS and AR(1)
# by constrained Qbar-maximization on S* (CS closed form, AR(1) 1-D profile); the
# saturated-anchored deviance T_k uses the FULL curved form (trace term kept as a convergence
# guard). Paired differential D_pair = (T_MI(CS)-T_MI(AR1)) - (T_com(CS)-T_com(AR1)); the
# residual D_pair - [tr(RIV_perp,CS)-tr(RIV_perp,AR1)] estimates the (A)+(C) differential
# (tr(RIV_perp,k) via the general-Jacobian spectrum at each candidate's own pseudo-true).
# Flat null reference = the mu_1=0 nested LRT (q_d=1, truth mu=0); fixed-alternative nested
# diagnostic = Independence-vs-candidate (M2-aux). MAR-residual minus MCAR-residual isolates
# (A)+(C) from generic non-nested O(1)s.
#
# Usage: Rscript verification/w4-nonnested-vuong.R [R_per_cell] [n_cores] [cells] [Ns]
#        defaults: 2000 8 A,B,Aprime,Bprime 500,1000,2000
#        pilot:    Rscript verification/w4-nonnested-vuong.R 300 6 A 500

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })

args <- commandArgs(trailingOnly = TRUE)
R_per_cell = if (length(args) >= 1) { as.integer(args[1]) } else { 2000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 8 }
cell_names <- if (length(args) >= 3) { strsplit(args[3], ",")[[1]] } else { c("A", "B", "Aprime", "Bprime") }
Ns = if (length(args) >= 4) { as.integer(strsplit(args[4], ",")[[1]]) } else { c(500, 1000, 2000) }

P = 4
K = 14
SEED0 = 20260604
mu0 <- c(0, 0, 0, 0)
Jm <- matrix(1, P, P)
Im <- diag(P)
Qm <- Im - Jm / P

# frozen truths (nonnested-pseudotrue-prep.R)
Sigma_A <- 0.5 ^ abs(outer(seq_len(P), seq_len(P), "-"))            # AR(1) rho=0.5
tau_B <- c(1, 0.473555, 0.355782, 0.296895)
Sigma_B <- stats::toeplitz(tau_B)                                   # equal-KL Toeplitz
CELLS <- list(
  A      = list(Sigma = Sigma_A, mech = "MAR"),
  B      = list(Sigma = Sigma_B, mech = "MAR"),
  Aprime = list(Sigma = Sigma_A, mech = "MCAR"),
  Bprime = list(Sigma = Sigma_B, mech = "MCAR")
)

# ---- candidate covariance builders + analytic Jacobians ----
cs_Sigma <- function(s2, rho) { return(s2 * ((1 - rho) * Im + rho * Jm)) }
ar1_R <- function(rho) { return(rho ^ abs(outer(seq_len(P), seq_len(P), "-"))) }
ar1_dR <- function(rho) {
  d <- abs(outer(seq_len(P), seq_len(P), "-"))
  out <- matrix(0, P, P)
  nz <- d != 0
  out[nz] <- d[nz] * rho ^ (d[nz] - 1)
  return(out)
}
jac_cs <- function(s2, rho) {
  G <- matrix(0, K, 6)
  G[seq_len(P), seq_len(P)] <- diag(P)
  G[(P + 1):K, 5] <- vech((1 - rho) * Im + rho * Jm)
  G[(P + 1):K, 6] <- vech(s2 * (Jm - Im))
  return(G)
}
jac_ar1 <- function(s2, rho) {
  G <- matrix(0, K, 6)
  G[seq_len(P), seq_len(P)] <- diag(P)
  G[(P + 1):K, 5] <- vech(ar1_R(rho))
  G[(P + 1):K, 6] <- vech(s2 * ar1_dR(rho))
  return(G)
}

# ---- constrained Qbar-maximizers on a moment matrix S ----
fit_cs <- function(S) {
  a = as.numeric(t(rep(1, P)) %*% S %*% rep(1, P)) / P
  b = sum(diag(Qm %*% S)) / (P - 1)
  s2 = (a + (P - 1) * b) / P
  rho = (a - b) / (a + (P - 1) * b)
  Sigma <- cs_Sigma(s2, rho)
  return(list(sigma2 = s2, rho = rho, Sigma = Sigma,
              tr_check = sum(diag(solve(Sigma, S))), conv = TRUE))
}
fit_ar1 <- function(S) {
  obj <- function(rho) {
    s2 = sum(diag(solve(ar1_R(rho), S))) / P
    return(P * log(s2) + (P - 1) * log(1 - rho^2))
  }
  grid <- seq(-0.95, 0.95, by = 0.025)
  gv <- vapply(grid, obj, numeric(1))
  r0 = grid[which.min(gv)]
  opt <- stats::optimize(obj, c(max(-0.985, r0 - 0.05), min(0.985, r0 + 0.05)), tol = 1e-9)
  rho = opt$minimum
  s2 = sum(diag(solve(ar1_R(rho), S))) / P
  Sigma <- s2 * ar1_R(rho)
  return(list(sigma2 = s2, rho = rho, Sigma = Sigma,
              tr_check = sum(diag(solve(Sigma, S))), conv = abs(rho) < 0.94))
}
fit_indep <- function(S) {
  s2 = sum(diag(S)) / P
  Sigma <- s2 * Im
  return(list(sigma2 = s2, rho = 0, Sigma = Sigma,
              tr_check = sum(diag(solve(Sigma, S))), conv = TRUE))
}
# closed-form mu_1 = 0 constrained MVN MLE from moment stats (w2-paired-differential-mu1-cell.R)
cn_mu1_moments <- function(m, S) {
  W <- solve(S)
  d <- numeric(P)
  d[1] = m[1]
  d[-1] <- as.numeric(-solve(W[-1, -1, drop = FALSE], W[-1, 1, drop = FALSE])) * m[1]
  return(list(mu = m - d, Sigma = S + tcrossprod(d)))
}

# ---- saturated-anchored deviance, full form: 2[Qbar(sat) - Qbar(k)] ----
# = N[ log|Sigma_k| + tr(Sigma_k^-1 (S + (m-mk)(m-mk)')) - log|S| - p ]
dev_anchored <- function(Sigma_k, m_k, m_star, S_star, N) {
  d <- m_star - m_k
  M <- S_star + tcrossprod(d)
  val = N * (as.numeric(determinant(Sigma_k, logarithm = TRUE)$modulus)
             + sum(diag(solve(Sigma_k, M)))
             - as.numeric(determinant(S_star, logarithm = TRUE)$modulus) - P)
  return(val)
}

# ---- general-Jacobian spectrum (generalizes ic-ladder.R::ladder_spectrum, free_idx -> G) ----
spectrum_G <- function(theta, Y, R, G) {
  N = nrow(Y)
  p_free = ncol(G)
  q_d = K - p_free
  I_com <- fisher_info_com_mvn(theta, N)
  I_obs <- fisher_info_obs_mvn(theta, Y, R)
  I_mis <- I_com - I_obs
  IoinvImis <- solve(I_obs, I_mis)
  tr_full = sum(diag(IoinvImis))
  GtIcomG <- t(G) %*% I_com %*% G
  Mproj <- I_com %*% IoinvImis
  tr_proj = sum(diag(solve(GtIcomG, t(G) %*% Mproj %*% G)))
  tr_perp = tr_full - tr_proj
  GtIobsG <- t(G) %*% I_obs %*% G
  tr_riv_f = sum(diag(solve(I_obs, I_com))) - K
  tr_riv_0 = sum(diag(solve(GtIobsG, GtIcomG))) - p_free
  tr_naive = tr_riv_f - tr_riv_0
  A <- solve(I_com) - G %*% solve(GtIcomG, t(G))
  V <- I_com %*% solve(I_obs, I_com)
  eV <- eigen((V + t(V)) / 2, symmetric = TRUE)
  Vh <- eV$vectors %*% (sqrt(pmax(eV$values, 0)) * t(eV$vectors))
  lam_all <- eigen(Vh %*% ((A + t(A)) / 2) %*% Vh, symmetric = TRUE, only.values = TRUE)$values
  lam <- sort(lam_all, decreasing = TRUE)[seq_len(q_d)]
  spec_gap = abs(sum(lam) - (q_d + tr_perp)) / max(1, q_d + tr_perp)
  return(list(lam = lam, q_d = q_d, tr_perp = tr_perp, tr_naive = tr_naive,
              spec_gap = spec_gap, lam_min = min(lam)))
}

# ---- E-step moments at theta_obs (ic-ladder.R / w2-mu1-cell construction) ----
estep_moments <- function(theta_obs, Y, R) {
  N = nrow(Y)
  Xhat <- Y
  Vbar <- matrix(0, P, P)
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat)
    R_pat <- R[rows[1], ]
    Mi <- which(R_pat == 1); Oi <- which(R_pat == 0)
    if (length(Mi) == 0) { next }
    if (length(Oi) == 0) {
      Xhat[rows, ] <- matrix(theta_obs$mu, length(rows), P, byrow = TRUE)
      Vbar <- Vbar + length(rows) * theta_obs$Sigma
    } else {
      Soo_inv <- solve(theta_obs$Sigma[Oi, Oi, drop = FALSE])
      reg <- theta_obs$Sigma[Mi, Oi, drop = FALSE] %*% Soo_inv
      cond_V <- theta_obs$Sigma[Mi, Mi, drop = FALSE] -
        reg %*% t(theta_obs$Sigma[Mi, Oi, drop = FALSE])
      cm <- sweep(Y[rows, Oi, drop = FALSE], 2, theta_obs$mu[Oi], FUN = "-") %*% t(reg)
      Xhat[rows, Mi] <- sweep(cm, 2, theta_obs$mu[Mi], FUN = "+")
      Vfull <- matrix(0, P, P); Vfull[Mi, Mi] <- cond_V
      Vbar <- Vbar + length(rows) * Vfull
    }
  }
  m_star <- colMeans(Xhat)
  Xc <- sweep(Xhat, 2, m_star, FUN = "-")
  S_star <- crossprod(Xc) / N + Vbar / N
  return(list(m = m_star, S = S_star))
}

# ---- amputation: X1-heavy MAR + matched MCAR twin ----
amp_mar <- function(X) {
  N <- nrow(X)
  R <- matrix(0, N, P)
  R[, 1] <- as.numeric(runif(N) < pnorm(0.8 + 1.2 * X[, 3]))
  R[, 2] <- as.numeric(runif(N) < pnorm(-3.0))
  Y <- X; Y[R == 1] <- NA
  return(list(Y = Y, R = R))
}
amp_mcar <- function(X) {
  N <- nrow(X)
  R <- matrix(0, N, P)
  R[, 1] <- as.numeric(runif(N) < 0.696)        # matched X1 marginal, independent of data
  R[, 2] <- as.numeric(runif(N) < pnorm(-3.0))
  Y <- X; Y[R == 1] <- NA
  return(list(Y = Y, R = R))
}

# ---- one replicate ----
one <- function(seed, N, Sigma_truth, mech) {
  set.seed(seed)
  X <- gen_data(N, mu0, Sigma_truth)
  amp <- tryCatch(if (mech == "MAR") { amp_mar(X) } else { amp_mcar(X) },
                  error = function(e) { return(NULL) })
  if (is.null(amp)) { return(list(error = "ampute")) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(amp$Y, FALSE), error = function(e) { return(NULL) })
  if (is.null(fit)) { return(list(error = "fiml")) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values = TRUE)$values) < 1e-6) {
    return(list(error = "fiml-pd"))
  }
  em <- estep_moments(to, amp$Y, amp$R)
  if (min(eigen(em$S, only.values = TRUE)$values) < 1e-6) { return(list(error = "estep-pd")) }
  th_com <- mle_complete_mvn(X)
  Sc <- th_com$Sigma; mc <- th_com$mu
  # candidate fits on MI moments (S*) and complete-data moments (S_com)
  cs <- fit_cs(em$S); ar <- fit_ar1(em$S); ind <- fit_indep(em$S)
  csc <- fit_cs(Sc); arc <- fit_ar1(Sc); indc <- fit_indep(Sc)
  trchk = max(abs(c(cs$tr_check, ar$tr_check, ind$tr_check) - P))
  # saturated-anchored deviances (cov candidates: mu_k = m*)
  T_MI_cs = dev_anchored(cs$Sigma, em$m, em$m, em$S, N)
  T_MI_ar = dev_anchored(ar$Sigma, em$m, em$m, em$S, N)
  T_MI_ind = dev_anchored(ind$Sigma, em$m, em$m, em$S, N)
  T_co_cs = dev_anchored(csc$Sigma, mc, mc, Sc, N)
  T_co_ar = dev_anchored(arc$Sigma, mc, mc, Sc, N)
  T_co_ind = dev_anchored(indc$Sigma, mc, mc, Sc, N)
  if (min(T_MI_cs, T_MI_ar, T_MI_ind, T_co_cs, T_co_ar, T_co_ind) < -1e-6) {
    return(list(error = "negT"))
  }
  dT_MI = T_MI_cs - T_MI_ar
  dT_com = T_co_cs - T_co_ar
  D_pair = dT_MI - dT_com
  # general-Jacobian tr(RIV_perp) at each candidate's own per-replicate pseudo-true
  sp_cs <- tryCatch(spectrum_G(list(mu = em$m, Sigma = cs$Sigma), amp$Y, amp$R,
                               jac_cs(cs$sigma2, cs$rho)), error = function(e) { return(NULL) })
  sp_ar <- tryCatch(spectrum_G(list(mu = em$m, Sigma = ar$Sigma), amp$Y, amp$R,
                               jac_ar1(ar$sigma2, ar$rho)), error = function(e) { return(NULL) })
  if (is.null(sp_cs) || is.null(sp_ar)) { return(list(error = "spectrum")) }
  d_trperp = sp_cs$tr_perp - sp_ar$tr_perp
  resid = D_pair - d_trperp
  # mu_1 = 0 NULL control (flat reference; q_d=1)
  cn_q <- cn_mu1_moments(em$m, em$S)
  cn_c <- cn_mu1_moments(mc, Sc)
  T_mu1_MI = dev_anchored(cn_q$Sigma, cn_q$mu, em$m, em$S, N)
  T_mu1_co = dev_anchored(cn_c$Sigma, cn_c$mu, mc, Sc, N)
  D_mu1 = T_mu1_MI - T_mu1_co
  G_mu1 <- diag(K)[, 2:K, drop = FALSE]
  sp_mu1 <- tryCatch(spectrum_G(cn_q, amp$Y, amp$R, G_mu1), error = function(e) { return(NULL) })
  if (is.null(sp_mu1)) { return(list(error = "spectrum-mu1")) }
  resid_mu1 = D_mu1 - sp_mu1$tr_perp
  # fixed-alternative nested diagnostic (Independence vs each candidate; false rho=0)
  D_nest_cs = (T_MI_ind - T_MI_cs) - (T_co_ind - T_co_cs)
  D_nest_ar = (T_MI_ind - T_MI_ar) - (T_co_ind - T_co_ar)
  spec_gap = max(sp_cs$spec_gap, sp_ar$spec_gap, sp_mu1$spec_gap)
  lam_min = min(sp_cs$lam_min, sp_ar$lam_min, sp_mu1$lam_min)
  out <- c(r = seed - SEED0,
           D_pair = D_pair, dT_MI = dT_MI, dT_com = dT_com, d_trperp = d_trperp, resid = resid,
           T_MI_cs = T_MI_cs, T_MI_ar = T_MI_ar, T_co_cs = T_co_cs, T_co_ar = T_co_ar,
           D_mu1 = D_mu1, resid_mu1 = resid_mu1, trperp_mu1 = sp_mu1$tr_perp,
           D_nest_cs = D_nest_cs, D_nest_ar = D_nest_ar,
           trperp_cs = sp_cs$tr_perp, trnaive_cs = sp_cs$tr_naive,
           trperp_ar = sp_ar$tr_perp, trnaive_ar = sp_ar$tr_naive,
           rho_cs = cs$rho, rho_ar = ar$rho, s2_cs = cs$sigma2, s2_ar = ar$sigma2,
           sel_oracle = as.numeric(dT_com < 0),
           sel_MI_unc = as.numeric(dT_MI < 0),
           sel_MI_corr = as.numeric(dT_MI - d_trperp < 0),
           spec_gap = spec_gap, lam_min = lam_min, trchk = trchk, ar_conv = as.numeric(ar$conv))
  return(list(error = NA, stats = out))
}

# ---------------------------------------------------------------------------
# build-time smoke: general-G ≡ selection-index spectrum (the silent-failure guard)
# ---------------------------------------------------------------------------
smoke_check <- function() {
  set.seed(SEED0)
  X <- gen_data(400, mu0, Sigma_A)
  amp <- amp_mar(X)
  fit <- lavaan_fit_mvn_fiml(amp$Y, FALSE)
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  em <- estep_moments(to, amp$Y, amp$R)
  cs <- fit_cs(em$S)
  # (a) general-G with a SELECTION matrix equals the direct selection-index formula
  free_idx <- c(1, 2, 3, 4, 7, 9, 14)            # arbitrary 7-param sub-model
  Gsel <- diag(K)[, free_idx, drop = FALSE]
  theta <- list(mu = em$m, Sigma = cs$Sigma)
  I_com <- fisher_info_com_mvn(theta, 400)
  I_obs <- fisher_info_obs_mvn(theta, amp$Y, amp$R)
  I_mis <- I_com - I_obs
  IoinvImis <- solve(I_obs, I_mis)
  tr_sel = sum(diag(IoinvImis)) -
    sum(diag(solve(I_com[free_idx, free_idx], (I_com %*% IoinvImis)[free_idx, free_idx])))
  sg <- spectrum_G(theta, amp$Y, amp$R, Gsel)
  e1 = abs(sg$tr_perp - tr_sel)
  # (b) tr_check ~ p for the curved candidates
  ar <- fit_ar1(em$S)
  e2 = max(abs(c(cs$tr_check, ar$tr_check) - P))
  # (c) spectrum identity + weights on the real curved G_k
  sp <- spectrum_G(list(mu = em$m, Sigma = ar$Sigma), amp$Y, amp$R, jac_ar1(ar$sigma2, ar$rho))
  cat(sprintf("SMOKE: |tr_perp(G_sel) - tr_perp(idx)|=%.2e  max|tr_chk-p|=%.2e  spec_gap=%.2e  lam_min=%.4f\n",
              e1, e2, sp$spec_gap, sp$lam_min))
  if (e1 > 1e-9 || e2 > 1e-6 || sp$spec_gap > 1e-6 || sp$lam_min < 1 - 1e-6) {
    stop("SMOKE FAILED -- general-G spectrum or trace-cancellation guard broken")
  }
  cat("SMOKE PASS\n\n")
}

# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------
dir.create("verification/cache", showWarnings = FALSE, recursive = TRUE)
cat("====== W4 non-nested (Vuong) (A)+(C) differential (todo/029) ======\n")
cat(sprintf("R_per_cell=%d  n_cores=%d  cells={%s}  Ns={%s}  seeds %d+r\n\n",
            R_per_cell, n_cores, paste(cell_names, collapse = ","),
            paste(Ns, collapse = ","), SEED0))
smoke_check()

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, {
  source("verification/00-setup.R")
  suppressPackageStartupMessages(library(lavaan))
}))
clusterExport(cl, c("P", "K", "SEED0", "mu0", "Jm", "Im", "Qm", "cs_Sigma", "ar1_R", "ar1_dR",
                    "jac_cs", "jac_ar1", "fit_cs", "fit_ar1", "fit_indep", "cn_mu1_moments",
                    "dev_anchored", "spectrum_G", "estep_moments", "amp_mar", "amp_mcar", "one"))

summary_rows <- list()
for (cn in cell_names) {
  cell <- CELLS[[cn]]
  if (is.null(cell)) { stop(sprintf("unknown cell %s", cn)) }
  for (N in Ns) {
    t0 <- Sys.time()
    results <- parLapply(cl, seq_len(R_per_cell),
                         function(r, NN, Sig, mech) { return(one(SEED0 + r, NN, Sig, mech)) },
                         NN = N, Sig = cell$Sigma, mech = cell$mech)
    elapsed = as.numeric(difftime(Sys.time(), t0, units = "secs"))
    errs <- sapply(results, function(rr) { return(!is.na(rr$error)) })
    ok <- results[!errs]
    M <- do.call(rbind, lapply(ok, `[[`, "stats"))
    err_types <- if (sum(errs) > 0) { table(sapply(results[errs], `[[`, "error")) } else { NULL }
    saveRDS(list(cell = cn, mech = cell$mech, N = N, R_per_cell = R_per_cell,
                 n_ok = nrow(M), n_err = sum(errs), err_types = err_types,
                 stats = M, elapsed_sec = elapsed),
            file = sprintf("verification/cache/w4-nonnested-%s-N%d.rds", cn, N))
    # asserts
    a_spec = max(M[, "spec_gap"]); a_lam = min(M[, "lam_min"]); a_trchk = max(M[, "trchk"])
    if (a_spec > 1e-6 || a_lam < 1 - 1e-6 || a_trchk > 1e-6) {
      stop(sprintf("ASSERT VIOLATED (cell %s N=%d): spec=%.2e lam=%.6f trchk=%.2e", cn, N, a_spec, a_lam, a_trchk))
    }
    Rn = nrow(M)
    se <- function(x) { return(sd(x) / sqrt(Rn)) }
    row <- data.frame(
      cell = cn, mech = cell$mech, N = N, R = R_per_cell, n_ok = Rn, n_err = sum(errs),
      elapsed_sec = elapsed,
      resid = mean(M[, "resid"]), resid_se = se(M[, "resid"]),
      D_pair = mean(M[, "D_pair"]), d_trperp = mean(M[, "d_trperp"]),
      sd_Dpair = sd(M[, "D_pair"]),
      resid_mu1 = mean(M[, "resid_mu1"]), resid_mu1_se = se(M[, "resid_mu1"]),
      sd_Dmu1 = sd(M[, "D_mu1"]),
      sd_Dnest_cs = sd(M[, "D_nest_cs"]), sd_Dnest_ar = sd(M[, "D_nest_ar"]),
      resid_nest_cs = mean(M[, "D_nest_cs"]), resid_nest_ar = mean(M[, "D_nest_ar"]),
      pCS_oracle = mean(M[, "sel_oracle"]), pCS_MIunc = mean(M[, "sel_MI_unc"]),
      pCS_MIcorr = mean(M[, "sel_MI_corr"]),
      trperp_cs = mean(M[, "trperp_cs"]), trnaive_cs = mean(M[, "trnaive_cs"]),
      trperp_ar = mean(M[, "trperp_ar"]), trnaive_ar = mean(M[, "trnaive_ar"]),
      rho_cs = mean(M[, "rho_cs"]), rho_ar = mean(M[, "rho_ar"]),
      ar_conv = mean(M[, "ar_conv"]), spec_gap = a_spec, lam_min = a_lam, trchk = a_trchk,
      stringsAsFactors = FALSE)
    summary_rows[[paste(cn, N, sep = "_")]] <- row
    cat(sprintf("-- %-7s N=%4d (%d ok, %d err, %.0fs) --\n", cn, N, Rn, sum(errs), elapsed))
    cat(sprintf("   resid (A+C est) = %+.4f (%.4f)  [%.1f se] | D_pair=%+.3f d_trperp=%+.3f\n",
                row$resid, row$resid_se, row$resid / row$resid_se, row$D_pair, row$d_trperp))
    cat(sprintf("   sd(D_pair)=%.3f  sd(D_mu1)=%.3f  sd(D_nest_cs)=%.3f | mu1 resid=%+.4f (%.4f)\n",
                row$sd_Dpair, row$sd_Dmu1, row$sd_Dnest_cs, row$resid_mu1, row$resid_mu1_se))
    cat(sprintf("   P(sel CS): oracle=%.3f MIunc=%.3f MIcorr=%.3f | trperp/naive CS=%.3f/%.3f AR=%.3f/%.3f\n",
                row$pCS_oracle, row$pCS_MIunc, row$pCS_MIcorr,
                row$trperp_cs, row$trnaive_cs, row$trperp_ar, row$trnaive_ar))
    cat(sprintf("   rho_cs=%.3f rho_ar=%.3f ar_conv=%.3f | asserts specgap=%.1e lam=%.4f trchk=%.1e\n\n",
                row$rho_cs, row$rho_ar, row$ar_conv, a_spec, a_lam, a_trchk))
  }
}
stopCluster(cl)

summary_df <- do.call(rbind, summary_rows)
write.csv(summary_df, "verification/cache/w4-nonnested-summary.csv", row.names = FALSE)
cat("wrote verification/cache/w4-nonnested-summary.csv\n")

# MAR-minus-MCAR identification (the (A)+(C) isolator), per N, where twins are present
twin <- list(A = "Aprime", B = "Bprime")
for (base in names(twin)) {
  prime = twin[[base]]
  for (N in Ns) {
    rb <- summary_rows[[paste(base, N, sep = "_")]]
    rp <- summary_rows[[paste(prime, N, sep = "_")]]
    if (is.null(rb) || is.null(rp)) { next }
    iso = rb$resid - rp$resid
    iso_se = sqrt(rb$resid_se^2 + rp$resid_se^2)
    cat(sprintf("ISO  cell %s N=%4d:  MAR resid=%+.4f  MCAR resid=%+.4f  =>  (A)+(C) = %+.4f (%.4f) [%.1f se]\n",
                base, N, rb$resid, rp$resid, iso, iso_se, iso / iso_se))
  }
}
cat("====================================================================\n")
