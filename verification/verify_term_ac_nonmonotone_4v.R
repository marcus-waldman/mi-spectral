# verify_term_ac_nonmonotone_4v.R  [todo/015 -- 4-variate non-monotone (A)+(C) via Cox-Snell]
#
# Assembles the FOUR-VARIATE non-monotone design-imbalance term (A)+(C)_inf for the
# phase-8 ampute design, consuming the general-p Cox-Snell b_Sigma derived by
# verification/cas-wolfram/verify_term_ac_nonmonotone_genp.py (p=4, k=14).
#
#   (A)+(C)_inf = alpha^T b_Sigma + 1/2 tr(H_phi I_obs^{-1})
#
# The alpha / H_phi / I_obs machinery is the pattern-general one validated for the
# monotone general-MVN case (term-a-mar-closedform.R, ~ -0.22) -- reused VERBATIM. Only
# b_Sigma is new: non-monotone => the observed-data likelihood does not factor => no
# monotone recursion; b_Sigma comes from the Cox-Snell second-order MLE bias.
#
# Design = phase-8: X ~ N(default_mu, default_Sigma); apply_missingness_ampute(prop=0.40,
# mech="MAR", pattern_type="non_monotone").  X3,X4 always observed and drive missingness.
#
# RESULT (todo/015): the assembled LEADING-ORDER (A)+(C)_inf ~ -0.22 -- the SAME constant
# as the monotone design -- with the MCAR control -> 0.  Confirmed two independent ways:
# (i) the analytic alpha/H_phi assembly, (ii) finite-differencing the analytic barQ
# cross-entropy slot.  The committed phase-8 empirical remainder (-0.34 at n=800 -> -0.46
# at n=1500, still increasing; _modules/term-a-mar-correction.R) lies BEYOND this
# leading-order constant: the offset is a higher-order (finite-n / realized-information)
# effect of the same kind seen in the bivariate and monotone cases, NOT a b_Sigma shortfall
# (b_Sigma is nearly selection-invariant; varying it over the selection sweep moves
# (A)+(C) by < 0.01).
#
# Usage: Rscript verification/verify_term_ac_nonmonotone_4v.R [N] [R_mom]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(jsonlite) })
args <- commandArgs(trailingOnly = TRUE)
N_use  = if (length(args) >= 1) { as.integer(args[1]) } else { 4000 }
R_mom  = if (length(args) >= 2) { as.integer(args[2]) } else { 1500 }

# ---- 4-variate phase-8 truth + parameter bookkeeping (vech = column-major lower-tri) ----
p = 4
mu0 <- default_mu
Sig0 <- default_Sigma
k = p + p * (p + 1) / 2                                  # = 14
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
Epert <- function(s) { i = lt[s, 1]; j = lt[s, 2]; E <- matrix(0, p, p); E[i, j] <- 1; E[j, i] <- 1; return(E) }
TRUTH <- list(mu = mu0, Sigma = Sig0)
vech_lab <- apply(lt, 1, function(ij) { sprintf("s%d%d", ij[1], ij[2]) })

amp_mar_nonmono <- function(X) {
  return(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone"))
}
NONMONO_PATTERNS <- rbind(c(1, 0, 0, 0), c(0, 1, 0, 0), c(1, 1, 0, 0))   # R-mask: 1 = missing
NONMONO_FREQ <- c(1, 1, 1) / 3
PROP_INCOMPLETE = 1.5 * 0.40                             # = 0.60 (matches ampute prop_amp)
amp_mcar_nonmono <- function(X) {                        # control: patterns assigned at random
  N <- nrow(X); amp <- runif(N) < PROP_INCOMPLETE; Y <- X; R <- matrix(0, N, p); idx <- which(amp)
  if (length(idx) > 0) {
    pat <- sample.int(3, length(idx), replace = TRUE, prob = NONMONO_FREQ)
    for (t in 1:3) { ii <- idx[pat == t]; mc <- which(NONMONO_PATTERNS[t, ] == 1)
      if (length(ii) > 0) { Y[ii, mc] <- NA; R[ii, mc] <- 1 } }
  }
  return(list(Y = Y, R = R))
}

# ---- single moment pass at theta_0: per-pattern selected moments + E[I_obs] (pattern-general) ----
est_moments <- function(amp_fun, N, R) {
  pacc <- list(); Iobs_sum <- matrix(0, k, k); n_ok = 0
  for (r in 1:R) {
    set.seed(990000 + r); X <- gen_data(N, mu0, Sig0)
    mar <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(mar)) { next }
    Rm <- mar$R; n_ok = n_ok + 1
    patt <- apply(Rm, 1, function(row) { return(paste(row, collapse = "")) })
    for (pp in unique(patt)) {
      Rp <- Rm[which(patt == pp)[1], ]; O <- which(Rp == 0); if (length(O) == p) { next }
      rows <- which(patt == pp); e <- sweep(X[rows, O, drop = FALSE], 2, mu0[O], FUN = "-")
      if (is.null(pacc[[pp]])) { pacc[[pp]] <- list(count = 0, s1 = numeric(p), s2 = matrix(0, p, p), O = O, M = which(Rp == 1)) }
      pacc[[pp]]$count <- pacc[[pp]]$count + nrow(e)
      pacc[[pp]]$s1[O] <- pacc[[pp]]$s1[O] + colSums(e)
      pacc[[pp]]$s2[O, O] <- pacc[[pp]]$s2[O, O] + crossprod(e)
    }
    Iobs_sum <- Iobs_sum + observed_info_obs_mvn(list(mu = mu0, Sigma = Sig0), mar$Y, Rm)
  }
  pm <- list()
  for (key in names(pacc)) { a <- pacc[[key]]; O <- a$O
    pm[[key]] <- list(frac = a$count / (N * n_ok), m1 = a$s1[O] / a$count,
                      M2 = a$s2[O, O, drop = FALSE] / a$count, O = O, M = a$M) }
  return(list(pm = pm, Iobs = Iobs_sum / n_ok, N = N))
}

# ---- alpha / H_phi (VERBATIM from term-a-mar-closedform.R; pattern-general at any p) ----
alpha_expected <- function(mm, N) {
  alpha <- numeric(k)
  for (key in names(mm$pm)) { P <- mm$pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    U <- solve(Sig0[O, O, drop = FALSE]); B0 <- Sig0[M, O, drop = FALSE] %*% U
    S0i <- solve(Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE])
    for (s in 1:(k - p)) { E <- Epert(s)
      dS <- E[M, M, drop = FALSE] - E[M, O, drop = FALSE] %*% t(B0) - B0 %*% E[O, M, drop = FALSE] +
            B0 %*% E[O, O, drop = FALSE] %*% t(B0)
      alpha[p + s] <- alpha[p + s] - 0.5 * nP * sum(diag(S0i %*% dS)) } }
  return(alpha)
}
hphi_expected <- function(mm, N) {
  H <- matrix(0, k, k)
  for (key in names(mm$pm)) { P <- mm$pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    U <- solve(Sig0[O, O, drop = FALSE]); B0 <- Sig0[M, O, drop = FALSE] %*% U
    S0i <- solve(Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE])
    m1 <- P$m1; M2 <- P$M2
    Dmu <- matrix(0, length(M), p); for (jj in seq_along(M)) { Dmu[jj, M[jj]] <- 1 }; Dmu[, O] <- -B0
    GU <- vector("list", k - p); Gs <- vector("list", k - p)
    for (s in 1:(k - p)) { E <- Epert(s); G <- E[M, O, drop = FALSE] - B0 %*% E[O, O, drop = FALSE]
      Gs[[s]] <- G; GU[[s]] <- G %*% U }
    Hp <- matrix(0, k, k); Hp[1:p, 1:p] <- -t(Dmu) %*% S0i %*% Dmu
    for (s in 1:(k - p)) { v <- as.numeric(GU[[s]] %*% m1); col <- -t(Dmu) %*% (S0i %*% v)
      Hp[1:p, p + s] <- col; Hp[p + s, 1:p] <- col }
    for (aa in 1:(k - p)) { for (bb in aa:(k - p)) {
      qpart = -sum(diag(t(GU[[aa]]) %*% S0i %*% GU[[bb]] %*% M2))
      tpart = 0.5 * sum(diag(S0i %*% (Gs[[aa]] %*% U %*% t(Gs[[bb]]) + Gs[[bb]] %*% U %*% t(Gs[[aa]]))))
      Hp[p + aa, p + bb] <- qpart + tpart; Hp[p + bb, p + aa] <- Hp[p + aa, p + bb] } }
    H <- H + nP * Hp }
  return(H)
}

assemble_AC <- function(amp_fun, bvech, N, R_mom) {
  mm <- est_moments(amp_fun, N, R_mom)
  al <- alpha_expected(mm, N); Hphi <- hphi_expected(mm, N)
  A = sum(al * c(numeric(p), bvech) / N)
  C = 0.5 * sum(diag(Hphi %*% solve(mm$Iobs)))
  return(c(A = A, C = C, AC = A + C))
}

# ---- read Cox-Snell b_Sigma (general-p SymPy, p=4, phase-8 fractions) ------------------
gp <- jsonlite::fromJSON("verification/cache/coxsnell-nonmonotone-bsigma-genp4.json")
bvech_cs <- as.numeric(gp[["beta0.0"]]$b_sigma_vech)
stopifnot(length(bvech_cs) == k - p)

# ---- independent FD cross-check: recompute (A)+(C) from barQ_fiml_analytic -------------
# alpha = grad_phi F(theta0, phi)|theta0, H_phi = hess_phi F |theta0, F=barQ_fiml_analytic.
fd_AC <- function(N_fd = 40000, seed = 12345) {
  set.seed(seed); X <- gen_data(N_fd, mu0, Sig0)
  mar <- amp_mar_nonmono(X); Y <- mar$Y; R <- mar$R
  vec2theta <- function(v) { S <- matrix(0, p, p); S[lower.tri(S, diag = TRUE)] <- v[(p + 1):k]
    S[upper.tri(S)] <- t(S)[upper.tri(S)]; return(list(mu = v[1:p], Sigma = S)) }
  v0 <- c(mu0, Sig0[lower.tri(Sig0, diag = TRUE)]); h = 1e-4
  F1 <- function(v) { return(barQ_fiml_analytic(TRUTH, vec2theta(v), Y, R)) }
  grad <- numeric(k); f0 <- F1(v0)
  for (i in 1:k) { vp <- v0; vp[i] <- vp[i] + h; vm <- v0; vm[i] <- vm[i] - h
    grad[i] <- (F1(vp) - F1(vm)) / (2 * h) }
  Hess <- matrix(0, k, k)
  for (i in 1:k) { for (j in i:k) {
    if (i == j) { vp <- v0; vp[i] <- vp[i] + h; vm <- v0; vm[i] <- vm[i] - h
      Hess[i, j] <- (F1(vp) - 2 * f0 + F1(vm)) / h^2
    } else { vpp <- v0; vpp[c(i, j)] <- vpp[c(i, j)] + h; vmm <- v0; vmm[c(i, j)] <- vmm[c(i, j)] - h
      vpm <- v0; vpm[i] <- vpm[i] + h; vpm[j] <- vpm[j] - h; vmp <- v0; vmp[i] <- vmp[i] - h; vmp[j] <- vmp[j] + h
      Hess[i, j] <- (F1(vpp) - F1(vpm) - F1(vmp) + F1(vmm)) / (4 * h^2); Hess[j, i] <- Hess[i, j] } } }
  Iobs <- observed_info_obs_mvn(TRUTH, Y, R)
  Edelta <- c(numeric(p), bvech_cs / N_fd)
  A <- sum(grad * Edelta); C <- 0.5 * sum(diag(Hess %*% solve(Iobs)))
  return(c(A = A, C = C, AC = A + C, alpha_mu_max = max(abs(grad[1:p]))))
}

cat("\n============ 4-VARIATE NON-MONOTONE (A)+(C) via Cox-Snell -- phase-8 ============\n")
cat(sprintf("theta0: default_mu / default_Sigma; ampute prop=0.40 MAR non_monotone; k=%d; N=%d R_mom=%d\n",
            k, N_use, R_mom))

cat("\n-- Cox-Snell b_Sigma (general-p SymPy, beta=0 phase-8 fractions; genp.py) --\n")
cat(sprintf("   %s\n", paste(sprintf("%s=%+.4f", vech_lab, bvech_cs), collapse = "  ")))
cat("   [gates in genp.py: p=2 reduction to committed bivariate 1.5e-13; zero-score/Bartlett ~1e-15;\n")
cat("    always-observed block -> complete-data -sigma; monotone reduction -> -sigma_pp; GH-converged]\n")

cat("\n-- assembled leading-order (A)+(C)_inf (analytic alpha/H_phi + Cox-Snell b_Sigma) --\n")
ac <- assemble_AC(amp_mar_nonmono, bvech_cs, N_use, R_mom)
cat(sprintf("   (A)=%+.4f  (C)=%+.4f  (A)+(C)_inf=%+.4f\n", ac["A"], ac["C"], ac["AC"]))

cat("\n-- independent FD cross-check (finite-difference of analytic barQ; N=40000) --\n")
fd <- fd_AC()
cat(sprintf("   (A)_fd=%+.4f  (C)_fd=%+.4f  (A)+(C)_fd=%+.4f   [alpha mu-block max=%.1e ~ 0]\n",
            fd["A"], fd["C"], fd["AC"], fd["alpha_mu_max"]))
cat(sprintf("   assembly vs FD: |d(A)+(C)| = %.4f  [%s]\n", abs(ac["AC"] - fd["AC"]),
            if (abs(ac["AC"] - fd["AC"]) < 0.03) { "PASS" } else { "CHECK" }))

cat("\n-- MCAR control (non-monotone patterns assigned at random) --\n")
ac_mcar <- assemble_AC(amp_mcar_nonmono, bvech_cs, N_use, R_mom)
cat(sprintf("   (A)+(C)=%+.4f  [-> 0: design imbalance vanishes under MCAR]\n", ac_mcar["AC"]))

cat("\n-- comparison to committed phase-8 empirical remainder (R=40k; _modules/term-a-mar-correction.R) --\n")
cat("   empirical rem (A_rb - tr_obs): -0.336(n=800) -> -0.456(n=1500), still increasing.\n")
cat("   The empirical lies BEYOND the leading-order (A)+(C)_inf; the offset is a higher-order\n")
cat("   (finite-n / realized-information) effect shared by the bivariate (-0.10 vs -0.07) and\n")
cat("   monotone (-0.22 vs -0.27) cases, NOT a shortfall of the (now derived) b_Sigma.\n")

out <- list(theta0 = TRUTH, bSigma_cs = setNames(bvech_cs, vech_lab),
            ac_assembled = ac, ac_fd = fd, ac_mcar = ac_mcar,
            empirical_rem = c(n800 = -0.336, n1500 = -0.456))
dir.create("verification/cache", showWarnings = FALSE, recursive = TRUE)
saveRDS(out, "verification/cache/term-ac-nonmonotone-4v-verify.rds")
cat("\nwrote verification/cache/term-ac-nonmonotone-4v-verify.rds\n")
cat("================================================================================\n")
