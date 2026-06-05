# w4-dissimilar-vuong.R  [todo/029 Amendment 2 -- the DISSIMILAR non-nested pair: Diagonal vs AR(1)]
#
# Companion to w4-nonnested-vuong.R (the similar CS-vs-AR1 pair). Same apparatus, same frozen
# helpers; the only new candidate is Diagonal (free per-variable variances, structure-blind):
# Sigma_D = diag(diag(S*)), constrained Qbar-maximizer on the E-step moments (closed form), a
# block-diagonal (1x1-block) candidate whose spectrum uses a SELECTION-matrix G_D (free vech
# indices {1,5,8,10} + 4 means; q_d = 6) -- the already-CAS-blessed machinery (no new identity).
#
# Truth = AR(1) rho=0.5 (AR1 correct, Diagonal maximally misspecified). X1-heavy MAR (cell A) +
# matched MCAR twin (Aprime); MAR-minus-MCAR isolates the (A)+(C) differential. Tests whether a
# DISSIMILAR pair carries a resolved nonzero differential (the fence's positive anchor) vs the
# similar CS-vs-AR1 pair's below-resolution value. PREREGISTERED in todo/029 Amendment 2
# (commit 39cfc38) before this script existed.
#
# Usage: Rscript verification/w4-dissimilar-vuong.R [R_per_cell] [n_cores] [cells] [Ns]
#        defaults: 20000 8 A,Aprime 500,1000,2000

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })

args <- commandArgs(trailingOnly = TRUE)
R_per_cell = if (length(args) >= 1) { as.integer(args[1]) } else { 20000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 8 }
cell_names <- if (length(args) >= 3) { strsplit(args[3], ",")[[1]] } else { c("A", "Aprime") }
Ns = if (length(args) >= 4) { as.integer(strsplit(args[4], ",")[[1]]) } else { c(500, 1000, 2000) }

P = 4
K = 14
SEED0 = 20260604
mu0 <- c(0, 0, 0, 0)
Sigma_A <- 0.5 ^ abs(outer(seq_len(P), seq_len(P), "-"))           # AR(1) rho=0.5 truth
IDX_DIAG <- c(1, 2, 3, 4, 5, 9, 12, 14)                            # 4 means + diag vech {1,5,8,10}
CELLS <- list(A = list(Sigma = Sigma_A, mech = "MAR"),
              Aprime = list(Sigma = Sigma_A, mech = "MCAR"))

# ---- AR(1) candidate (copied verbatim from w4-nonnested-vuong.R) ----
ar1_R <- function(rho) { return(rho ^ abs(outer(seq_len(P), seq_len(P), "-"))) }
ar1_dR <- function(rho) {
  d <- abs(outer(seq_len(P), seq_len(P), "-"))
  out <- matrix(0, P, P); nz <- d != 0; out[nz] <- d[nz] * rho ^ (d[nz] - 1)
  return(out)
}
jac_ar1 <- function(s2, rho) {
  G <- matrix(0, K, 6); G[seq_len(P), seq_len(P)] <- diag(P)
  G[(P + 1):K, 5] <- vech(ar1_R(rho)); G[(P + 1):K, 6] <- vech(s2 * ar1_dR(rho))
  return(G)
}
fit_ar1 <- function(S) {
  obj <- function(rho) {
    s2 = sum(diag(solve(ar1_R(rho), S))) / P
    return(P * log(s2) + (P - 1) * log(1 - rho^2))
  }
  grid <- seq(-0.95, 0.95, by = 0.025)
  r0 = grid[which.min(vapply(grid, obj, numeric(1)))]
  opt <- stats::optimize(obj, c(max(-0.985, r0 - 0.05), min(0.985, r0 + 0.05)), tol = 1e-9)
  rho = opt$minimum; s2 = sum(diag(solve(ar1_R(rho), S))) / P
  Sigma <- s2 * ar1_R(rho)
  return(list(sigma2 = s2, rho = rho, Sigma = Sigma,
              tr_check = sum(diag(solve(Sigma, S))), conv = abs(rho) < 0.94))
}
# ---- Diagonal candidate (NEW): closed-form, selection-matrix Jacobian ----
fit_diag <- function(S) {
  Sigma <- diag(diag(S))
  return(list(Sigma = Sigma, tr_check = sum(diag(solve(Sigma, S))), conv = TRUE))
}
G_diag <- diag(K)[, IDX_DIAG, drop = FALSE]

# ---- shared machinery (copied verbatim from w4-nonnested-vuong.R) ----
dev_anchored <- function(Sigma_k, m_k, m_star, S_star, N) {
  d <- m_star - m_k; M <- S_star + tcrossprod(d)
  val = N * (as.numeric(determinant(Sigma_k, logarithm = TRUE)$modulus)
             + sum(diag(solve(Sigma_k, M)))
             - as.numeric(determinant(S_star, logarithm = TRUE)$modulus) - P)
  return(val)
}
spectrum_G <- function(theta, Y, R, G) {
  N = nrow(Y); p_free = ncol(G); q_d = K - p_free
  I_com <- fisher_info_com_mvn(theta, N)
  I_obs <- fisher_info_obs_mvn(theta, Y, R)
  I_mis <- I_com - I_obs
  IoinvImis <- solve(I_obs, I_mis); tr_full = sum(diag(IoinvImis))
  GtIcomG <- t(G) %*% I_com %*% G; Mproj <- I_com %*% IoinvImis
  tr_proj = sum(diag(solve(GtIcomG, t(G) %*% Mproj %*% G)))
  tr_perp = tr_full - tr_proj
  GtIobsG <- t(G) %*% I_obs %*% G
  tr_riv_f = sum(diag(solve(I_obs, I_com))) - K
  tr_riv_0 = sum(diag(solve(GtIobsG, GtIcomG))) - p_free
  tr_naive = tr_riv_f - tr_riv_0
  A <- solve(I_com) - G %*% solve(GtIcomG, t(G)); V <- I_com %*% solve(I_obs, I_com)
  eV <- eigen((V + t(V)) / 2, symmetric = TRUE)
  Vh <- eV$vectors %*% (sqrt(pmax(eV$values, 0)) * t(eV$vectors))
  lam_all <- eigen(Vh %*% ((A + t(A)) / 2) %*% Vh, symmetric = TRUE, only.values = TRUE)$values
  lam <- sort(lam_all, decreasing = TRUE)[seq_len(q_d)]
  spec_gap = abs(sum(lam) - (q_d + tr_perp)) / max(1, q_d + tr_perp)
  return(list(tr_perp = tr_perp, tr_naive = tr_naive, spec_gap = spec_gap, lam_min = min(lam)))
}
estep_moments <- function(theta_obs, Y, R) {
  N = nrow(Y); Xhat <- Y; Vbar <- matrix(0, P, P)
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  for (pat in unique(patterns)) {
    rows <- which(patterns == pat); R_pat <- R[rows[1], ]
    Mi <- which(R_pat == 1); Oi <- which(R_pat == 0)
    if (length(Mi) == 0) { next }
    if (length(Oi) == 0) {
      Xhat[rows, ] <- matrix(theta_obs$mu, length(rows), P, byrow = TRUE)
      Vbar <- Vbar + length(rows) * theta_obs$Sigma
    } else {
      Soo_inv <- solve(theta_obs$Sigma[Oi, Oi, drop = FALSE])
      reg <- theta_obs$Sigma[Mi, Oi, drop = FALSE] %*% Soo_inv
      cond_V <- theta_obs$Sigma[Mi, Mi, drop = FALSE] - reg %*% t(theta_obs$Sigma[Mi, Oi, drop = FALSE])
      cm <- sweep(Y[rows, Oi, drop = FALSE], 2, theta_obs$mu[Oi], FUN = "-") %*% t(reg)
      Xhat[rows, Mi] <- sweep(cm, 2, theta_obs$mu[Mi], FUN = "+")
      Vfull <- matrix(0, P, P); Vfull[Mi, Mi] <- cond_V; Vbar <- Vbar + length(rows) * Vfull
    }
  }
  m_star <- colMeans(Xhat); Xc <- sweep(Xhat, 2, m_star, FUN = "-")
  return(list(m = m_star, S = crossprod(Xc) / N + Vbar / N))
}
amp_mar <- function(X) {
  N <- nrow(X); R <- matrix(0, N, P)
  R[, 1] <- as.numeric(runif(N) < pnorm(0.8 + 1.2 * X[, 3]))
  R[, 2] <- as.numeric(runif(N) < pnorm(-3.0))
  Y <- X; Y[R == 1] <- NA; return(list(Y = Y, R = R))
}
amp_mcar <- function(X) {
  N <- nrow(X); R <- matrix(0, N, P)
  R[, 1] <- as.numeric(runif(N) < 0.696); R[, 2] <- as.numeric(runif(N) < pnorm(-3.0))
  Y <- X; Y[R == 1] <- NA; return(list(Y = Y, R = R))
}

# ---- one replicate: Diagonal (A) vs AR(1) (B) ----
one <- function(seed, N, Sigma_truth, mech) {
  set.seed(seed)
  X <- gen_data(N, mu0, Sigma_truth)
  amp <- tryCatch(if (mech == "MAR") { amp_mar(X) } else { amp_mcar(X) }, error = function(e) { return(NULL) })
  if (is.null(amp)) { return(list(error = "ampute")) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(amp$Y, FALSE), error = function(e) { return(NULL) })
  if (is.null(fit)) { return(list(error = "fiml")) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values = TRUE)$values) < 1e-6) { return(list(error = "fiml-pd")) }
  em <- estep_moments(to, amp$Y, amp$R)
  if (min(eigen(em$S, only.values = TRUE)$values) < 1e-6) { return(list(error = "estep-pd")) }
  th_com <- mle_complete_mvn(X); Sc <- th_com$Sigma; mc <- th_com$mu
  ad <- fit_diag(em$S); ar <- fit_ar1(em$S); adc <- fit_diag(Sc); arc <- fit_ar1(Sc)
  trchk = max(abs(c(ad$tr_check, ar$tr_check) - P))
  T_MI_d = dev_anchored(ad$Sigma, em$m, em$m, em$S, N)
  T_MI_a = dev_anchored(ar$Sigma, em$m, em$m, em$S, N)
  T_co_d = dev_anchored(adc$Sigma, mc, mc, Sc, N)
  T_co_a = dev_anchored(arc$Sigma, mc, mc, Sc, N)
  if (min(T_MI_d, T_MI_a, T_co_d, T_co_a) < -1e-6) { return(list(error = "negT")) }
  dT_MI = T_MI_d - T_MI_a; dT_com = T_co_d - T_co_a; D_pair = dT_MI - dT_com
  sp_d <- tryCatch(spectrum_G(list(mu = em$m, Sigma = ad$Sigma), amp$Y, amp$R, G_diag), error = function(e) { return(NULL) })
  sp_a <- tryCatch(spectrum_G(list(mu = em$m, Sigma = ar$Sigma), amp$Y, amp$R, jac_ar1(ar$sigma2, ar$rho)), error = function(e) { return(NULL) })
  if (is.null(sp_d) || is.null(sp_a)) { return(list(error = "spectrum")) }
  d_trperp = sp_d$tr_perp - sp_a$tr_perp; resid = D_pair - d_trperp
  out <- c(r = seed - SEED0, D_pair = D_pair, dT_MI = dT_MI, dT_com = dT_com,
           d_trperp = d_trperp, resid = resid,
           bias_diag = T_MI_d - T_co_d, bias_ar = T_MI_a - T_co_a,
           trperp_diag = sp_d$tr_perp, trperp_ar = sp_a$tr_perp,
           trnaive_diag = sp_d$tr_naive, trnaive_ar = sp_a$tr_naive,
           rho_ar = ar$rho, spec_gap = max(sp_d$spec_gap, sp_a$spec_gap),
           lam_min = min(sp_d$lam_min, sp_a$lam_min), trchk = trchk, ar_conv = as.numeric(ar$conv))
  return(list(error = NA, stats = out))
}

# ---- build-time smoke ----
smoke <- function() {
  set.seed(SEED0); X <- gen_data(400, mu0, Sigma_A); amp <- amp_mar(X)
  to <- { f <- lavaan_fit_mvn_fiml(amp$Y, FALSE); list(mu = f$mu, Sigma = f$Sigma) }
  em <- estep_moments(to, amp$Y, amp$R); ad <- fit_diag(em$S); ar <- fit_ar1(em$S)
  sp <- spectrum_G(list(mu = em$m, Sigma = ad$Sigma), amp$Y, amp$R, G_diag)
  e2 = max(abs(c(ad$tr_check, ar$tr_check) - P))
  cat(sprintf("SMOKE (diag): max|tr_chk-p|=%.2e  diag spec_gap=%.2e  lam_min=%.4f\n", e2, sp$spec_gap, sp$lam_min))
  if (e2 > 1e-6 || sp$spec_gap > 1e-6 || sp$lam_min < 1 - 1e-6) { stop("SMOKE FAILED") }
  cat("SMOKE PASS\n\n")
}

# ---- driver ----
dir.create("verification/cache", showWarnings = FALSE, recursive = TRUE)
cat("====== W4 DISSIMILAR pair: Diagonal vs AR(1) (todo/029 Amendment 2) ======\n")
cat(sprintf("R_per_cell=%d  n_cores=%d  cells={%s}  Ns={%s}  truth=AR(1) rho=0.5\n\n",
            R_per_cell, n_cores, paste(cell_names, collapse = ","), paste(Ns, collapse = ",")))
smoke()
cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); suppressPackageStartupMessages(library(lavaan)) }))
clusterExport(cl, c("P", "K", "SEED0", "mu0", "IDX_DIAG", "ar1_R", "ar1_dR", "jac_ar1", "fit_ar1",
                    "fit_diag", "G_diag", "dev_anchored", "spectrum_G", "estep_moments",
                    "amp_mar", "amp_mcar", "one"))
summary_rows <- list()
for (cn in cell_names) {
  cell <- CELLS[[cn]]
  for (N in Ns) {
    t0 <- Sys.time()
    results <- parLapply(cl, seq_len(R_per_cell),
                         function(r, NN, Sig, mech) { return(one(SEED0 + r, NN, Sig, mech)) },
                         NN = N, Sig = cell$Sigma, mech = cell$mech)
    elapsed = as.numeric(difftime(Sys.time(), t0, units = "secs"))
    errs <- sapply(results, function(rr) { return(!is.na(rr$error)) })
    M <- do.call(rbind, lapply(results[!errs], `[[`, "stats")); Rn = nrow(M)
    saveRDS(list(cell = cn, mech = cell$mech, N = N, R_per_cell = R_per_cell, n_ok = Rn,
                 n_err = sum(errs), stats = M, elapsed_sec = elapsed),
            file = sprintf("verification/cache/w4-dissimilar-%s-N%d.rds", cn, N))
    a_spec = max(M[, "spec_gap"]); a_lam = min(M[, "lam_min"]); a_trchk = max(M[, "trchk"])
    if (a_spec > 1e-6 || a_lam < 1 - 1e-6 || a_trchk > 1e-6) {
      stop(sprintf("ASSERT VIOLATED (cell %s N=%d): spec=%.2e lam=%.6f trchk=%.2e", cn, N, a_spec, a_lam, a_trchk))
    }
    se <- function(x) { return(sd(x) / sqrt(Rn)) }
    lvl_d = mean(M[, "bias_diag"]) - mean(M[, "trperp_diag"])
    lvl_a = mean(M[, "bias_ar"]) - mean(M[, "trperp_ar"])
    row <- data.frame(cell = cn, mech = cell$mech, N = N, R = R_per_cell, n_ok = Rn, n_err = sum(errs),
                      elapsed_sec = elapsed, resid = mean(M[, "resid"]), resid_se = se(M[, "resid"]),
                      D_pair = mean(M[, "D_pair"]), d_trperp = mean(M[, "d_trperp"]), sd_Dpair = sd(M[, "D_pair"]),
                      lvl_diag = lvl_d, lvl_diag_se = se(M[, "bias_diag"] - M[, "trperp_diag"]),
                      lvl_ar = lvl_a, lvl_ar_se = se(M[, "bias_ar"] - M[, "trperp_ar"]),
                      trperp_diag = mean(M[, "trperp_diag"]), trnaive_diag = mean(M[, "trnaive_diag"]),
                      trperp_ar = mean(M[, "trperp_ar"]), trnaive_ar = mean(M[, "trnaive_ar"]),
                      rho_ar = mean(M[, "rho_ar"]), ar_conv = mean(M[, "ar_conv"]),
                      spec_gap = a_spec, lam_min = a_lam, trchk = a_trchk, stringsAsFactors = FALSE)
    summary_rows[[paste(cn, N, sep = "_")]] <- row
    cat(sprintf("-- %-7s N=%4d (%d ok, %d err, %.0fs) --\n", cn, N, Rn, sum(errs), elapsed))
    cat(sprintf("   resid (A+C diff) = %+.4f (%.4f) [%.1f se] | (A+C)_diag=%+.3f(%.3f) (A+C)_ar=%+.3f(%.3f)\n",
                row$resid, row$resid_se, row$resid / row$resid_se, lvl_d, row$lvl_diag_se, lvl_a, row$lvl_ar_se))
    cat(sprintf("   D_pair=%+.3f d_trperp=%+.3f sd(D_pair)=%.2f | trperp/naive diag=%.2f/%.2f ar=%.2f/%.2f rho_ar=%.3f\n\n",
                row$D_pair, row$d_trperp, row$sd_Dpair, row$trperp_diag, row$trnaive_diag,
                row$trperp_ar, row$trnaive_ar, row$rho_ar))
  }
}
stopCluster(cl)
write.csv(do.call(rbind, summary_rows), "verification/cache/w4-dissimilar-summary.csv", row.names = FALSE)
cat("wrote verification/cache/w4-dissimilar-summary.csv\n")
for (N in Ns) {
  rb <- summary_rows[[paste("A", N, sep = "_")]]; rp <- summary_rows[[paste("Aprime", N, sep = "_")]]
  if (is.null(rb) || is.null(rp)) { next }
  iso = rb$resid - rp$resid; iso_se = sqrt(rb$resid_se^2 + rp$resid_se^2)
  cat(sprintf("ISO  N=%4d:  MAR resid=%+.4f  MCAR resid=%+.4f  =>  (A)+(C) diff = %+.4f (%.4f) [%.1f se]\n",
              N, rb$resid, rp$resid, iso, iso_se, iso / iso_se))
}
cat("==========================================================================\n")
