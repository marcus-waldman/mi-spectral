# term-ac-realized-info.R  [todo/018 Step 1 -- WAY 1 (Claude analytic)]
#
# Closed-form derivation of the REALIZED-INFORMATION term in the MAR design-imbalance
# (A)+(C), settling the information-convention question (todo/018). Step 0 (Kenward &
# Molenberghs 1998) fixed the convention: under MAR the OBSERVED (realized Hessian)
# information is the principled choice; the naive expected (population Sigma_OO) info is
# biased, and the bias is exactly zero iff MCAR. So the reported (A)+(C) is the realized
# value (the committed empirical -0.34 -> -0.46), and the analytic -0.22 is the naive
# expected-info value.
#
# This script derives the gap between the two conventions ANALYTICALLY, with no per-dataset
# fitting and no parallelism (deterministic; segfault-safe). Quantity:
#
#   Delta_KM(N) = tr(I_N^{-1} I_com) - tr(I_U^{-1} I_com)          ( = tr_exp - tr_real )
#
# where, at theta_0:
#   I_com = fisher_info_com_mvn(theta_0, N)                         [exact]
#   I_N   = NAIVE expected info: per pattern n_P * [ Sigma_OO^{-1} (mu) ;
#           1/2 D'(Sigma_OO^{-1} (x) Sigma_OO^{-1})D (vechSigma) ; ZERO cross block ]
#           -- block-diagonal, population Sigma_OO (= fisher_info_obs_mvn in expectation).
#   I_U   = E[ realized observed info ]: the SAME assembly with the population moments
#           replaced by the per-pattern SELECTED moments the design induces:
#             vechSigma block uses  M2_P = E[e_O e_O^T | P]   (selected 2nd moments)
#             mu x vechSigma cross  uses  m1_P = E[e_O | P]    (the K&M selection shift alpha_1)
#           (= observed_info_obs_mvn in expectation; built here from m1_P, M2_P).
#
# I_U - I_N is the K&M observed-minus-naive information bias (their eqs 9-11, bivariate
# Gaussian section): a mu x Sigma cross block proportional to the selection shift m1_P, plus
# a Sigma-block proportional to the selected-vs-population 2nd-moment shift (M2_P - Sigma_OO).
# BOTH vanish iff m1_P = 0 and M2_P = Sigma_OO -- i.e. under MCAR (K&M's necessary-and-
# sufficient condition). Hence Delta_KM is O(1) under MAR, 0 under MCAR.
#
# PREDICTION (to confirm): Delta_KM matches the committed lavaan paired gap tr_exp - tr_real
#   ~ -0.63 (n=800) -> -0.58 (n=1500) for the non-monotone design, and (A)+(C)_naive + Delta_KM
#   reproduces the realized empirical -0.34 -> -0.46. MCAR controls ~ 0.
#
# Usage: Rscript verification/term-ac-realized-info.R [R_mom] [Ns]
#   e.g. Rscript verification/term-ac-realized-info.R 1000 800,1500,3000

source("verification/00-setup.R")
args <- commandArgs(trailingOnly = TRUE)
R_mom = if (length(args) >= 1) { as.integer(args[1]) } else { 1000 }
Ns    = if (length(args) >= 2) { as.integer(strsplit(args[2], ",")[[1]]) } else { c(800, 1500, 3000) }

p = 4; mu0 <- default_mu; Sig0 <- default_Sigma; k = p + p * (p + 1) / 2
TRUTH <- list(mu = mu0, Sigma = Sig0)
vech_idx <- vech_index_table(p)

# ---- missingness designs (match phase-8 / verify_term_ac_nonmonotone_4v.R) ----
amp_mar_nonmono <- function(X) { return(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone")) }
amp_mar_mono    <- function(X) { return(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone")) }
NONMONO_PATTERNS <- rbind(c(1, 0, 0, 0), c(0, 1, 0, 0), c(1, 1, 0, 0))
MONO_PATTERNS    <- rbind(c(0, 0, 0, 1), c(0, 0, 1, 1), c(0, 1, 1, 1))
FREQ3 <- c(1, 1, 1) / 3
amp_mcar_from <- function(PATS, prop_inc) {
  force(PATS); force(prop_inc)
  return(function(X) {
    N <- nrow(X); amp <- runif(N) < prop_inc; Y <- X; R <- matrix(0, N, p); idx <- which(amp)
    if (length(idx) > 0) { pat <- sample.int(3, length(idx), replace = TRUE, prob = FREQ3)
      for (t in 1:3) { ii <- idx[pat == t]; mc <- which(PATS[t, ] == 1); if (length(ii) > 0) { Y[ii, mc] <- NA; R[ii, mc] <- 1 } } }
    return(list(Y = Y, R = R)) })
}
amp_mcar_nonmono <- amp_mcar_from(NONMONO_PATTERNS, 1.5 * 0.40)
amp_mcar_mono    <- amp_mcar_from(MONO_PATTERNS, 0.40)

# ---- single moment pass at theta_0: per-pattern selected moments + E[I_obs] (= i_U, MC) ----
est_moments <- function(amp_fun, N, R) {
  pacc <- list(); Iobs_sum <- matrix(0, k, k); n_ok = 0
  for (r in 1:R) {
    set.seed(990000 + r); X <- gen_data(N, mu0, Sig0)
    mar <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(mar)) { next }
    Rm <- mar$R; n_ok = n_ok + 1
    patt <- apply(Rm, 1, function(row) { return(paste(row, collapse = "")) })
    for (pp in unique(patt)) {
      Rp <- Rm[which(patt == pp)[1], ]; O <- which(Rp == 0)   # INCLUDE complete cases (O = 1:p): they
      # are MAR-selected too and contribute their own realized-vs-naive shift via observed_info_obs_mvn
      rows <- which(patt == pp); e <- sweep(X[rows, O, drop = FALSE], 2, mu0[O], FUN = "-")
      if (is.null(pacc[[pp]])) { pacc[[pp]] <- list(count = 0, s1 = numeric(p), s2 = matrix(0, p, p), O = O, M = which(Rp == 1)) }
      pacc[[pp]]$count <- pacc[[pp]]$count + nrow(e)
      pacc[[pp]]$s1[O] <- pacc[[pp]]$s1[O] + colSums(e)
      pacc[[pp]]$s2[O, O] <- pacc[[pp]]$s2[O, O] + crossprod(e)
    }
    Iobs_sum <- Iobs_sum + observed_info_obs_mvn(TRUTH, mar$Y, Rm)
  }
  pm <- list()
  for (key in names(pacc)) { a <- pacc[[key]]; O <- a$O
    pm[[key]] <- list(frac = a$count / (N * n_ok), m1 = a$s1[O] / a$count,
                      M2 = a$s2[O, O, drop = FALSE] / a$count, O = O, M = a$M) }
  return(list(pm = pm, Iobs_mc = Iobs_sum / n_ok, N = N))
}

# ---- analytic info assemblies from per-pattern selected moments (per-unit, scaled by n_P) ----
# mode = "naive" (population Sigma_OO, block-diagonal) or "realized" (selected M2_P + cross m1_P).
build_info <- function(pm, N, mode) {
  I <- matrix(0, k, k)
  for (key in names(pm)) {
    P <- pm[[key]]; O <- P$O; q <- length(O); nP = P$frac * N
    Si <- solve(Sig0[O, O, drop = FALSE])
    Dq <- duplication_matrix(q)
    # full-vech indices for entries with both indices in O (offset by p for the mu block)
    full_idx <- numeric(q * (q + 1) / 2); sc = 0
    for (b in seq_len(q)) { for (a in b:q) { sc = sc + 1; full_idx[sc] <- p + vech_idx[O[a], O[b]] } }
    # mu block (identical for both conventions)
    I[O, O] <- I[O, O] + nP * Si
    if (mode == "naive") {
      Isub <- 0.5 * t(Dq) %*% kronecker(Si, Si) %*% Dq
      I[full_idx, full_idx] <- I[full_idx, full_idx] + nP * Isub
    } else {
      M2 <- P$M2; SiMSi <- Si %*% M2 %*% Si   # per-unit selected 2nd moment (P$M2 is already q x q)
      cov_vec <- -0.5 * (kronecker(Si, Si)) + 0.5 * (kronecker(SiMSi, Si) + kronecker(Si, SiMSi))
      I[full_idx, full_idx] <- I[full_idx, full_idx] + nP * (t(Dq) %*% cov_vec %*% Dq)
      cross <- kronecker(t(P$m1) %*% Si, Si) %*% Dq               # K&M selection-shift cross block
      I[O, full_idx] <- I[O, full_idx] + nP * cross
      I[full_idx, O] <- I[full_idx, O] + nP * t(cross)
    }
  }
  return(I)
}

riv <- function(I_obs, I_com) { return(sum(diag(solve(I_obs, I_com))) - k) }

run_cell <- function(label, amp_fun, N, R) {
  mm <- est_moments(amp_fun, N, R)
  I_com <- fisher_info_com_mvn(TRUTH, N)
  I_N <- build_info(mm$pm, N, "naive")
  I_U <- build_info(mm$pm, N, "realized")
  sane <- max(abs(I_U - mm$Iobs_mc))                 # analytic realized == MC realized?
  tr_N <- riv(I_N, I_com); tr_U <- riv(I_U, I_com)
  delta <- tr_N - tr_U                               # = tr_exp - tr_real (K&M info bias)
  cat(sprintf("  %-18s N=%4d | tr_exp(naive)=%+.4f  tr_real(realized)=%+.4f  Delta_KM=%+.4f  [|I_U-I_mc|=%.1e]\n",
              label, N, tr_N, tr_U, delta, sane))
  return(c(N = N, tr_exp = tr_N, tr_real = tr_U, delta = delta, sane = sane))
}

cat("\n==================== REALIZED-INFORMATION TERM Delta_KM = tr_exp - tr_real ====================\n")
cat(sprintf("theta0 = default_mu/default_Sigma; ampute prop=0.40; k=%d; R_mom=%d (deterministic, single-proc)\n", k, R_mom))
cat("Step 0 (K&M 1998): realized observed info is the principled MAR convention; naive expected biased; 0 iff MCAR.\n")
cat("Committed lavaan paired gap (tr_exp - tr_real): non-mono -0.63(800) -> -0.58(1500); empirical (A)+(C) -0.34 -> -0.46.\n\n")

for (cell in list(
  list(lab = "MAR  non-monotone", f = amp_mar_nonmono),
  list(lab = "MCAR non-monotone", f = amp_mcar_nonmono),
  list(lab = "MAR  monotone",     f = amp_mar_mono),
  list(lab = "MCAR monotone",     f = amp_mcar_mono))) {
  cat(sprintf("-- %s --\n", cell$lab))
  for (N in Ns) { run_cell(cell$lab, cell$f, N, R_mom) }
  cat("\n")
}

cat("Reading: Delta_KM is the realized-information term (K&M observed-minus-naive info bias).\n")
cat("  MAR  => Delta_KM ~ -0.6 (O(1)), reproducing the lavaan paired gap.\n")
cat("  MCAR => Delta_KM ~ 0 (K&M necessary-and-sufficient).\n")
cat("  (A)+(C)_realized = (A)+(C)_naive + Delta_KM ; naive-convention value measured at theta-hat by lavaan (rem_exp).\n")
cat("===============================================================================================\n")
