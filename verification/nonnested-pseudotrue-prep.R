# nonnested-pseudotrue-prep.R  [todo/029 -- deterministic pre-registration inputs]
#
# Computes and FREEZES the population pseudo-true (sigma^2, rho) and KL divergences for the
# non-nested CS-vs-AR(1) measurement (Proposition L4, derivation.qmd @sec-lrt-ac). These numbers
# go into todo/029 BEFORE any measurement-engine code exists.
#
# Candidate definitions use the complete-data E-step moment S_inf = Sigma_truth (the candidates'
# KL balance and Vuong separation are population properties of the truth, not of the MI draws).
#
# Cell A: truth = AR(1) rho=0.5, sigma^2=1 (AR1 correctly specified, CS misspecified).
# Cell B: truth = a one-parameter Toeplitz-correlation family tuned so KL(truth||CS*)=KL(truth||AR1*)
#         -- the "money cell" where complete-data selection between CS and AR(1) is a coin flip.
#
# Gates (Vuong non-degeneracy): both pseudo-true |rho| >= 0.15 (well away from the CS-cap-AR1
# intersection at rho=0); truth covariance positive definite.
#
# Base R only; deterministic; no RNG. Usage: Rscript verification/nonnested-pseudotrue-prep.R

p = 4
J <- matrix(1, p, p)
Imat <- diag(p)
Qmat <- Imat - J / p              # projection onto the complement of span(1)
RHO_GATE = 0.15

# ---- candidate covariance builders ----
cs_Sigma <- function(sigma2, rho) {
  return(sigma2 * ((1 - rho) * Imat + rho * J))
}

ar1_R <- function(rho) {
  return(rho ^ abs(outer(seq_len(p), seq_len(p), "-")))
}

ar1_Sigma <- function(sigma2, rho) {
  return(sigma2 * ar1_R(rho))
}

# ---- closed-form CS pseudo-true given a target covariance S ----
cs_project <- function(S) {
  a_hat = as.numeric(t(rep(1, p)) %*% S %*% rep(1, p)) / p     # rank-1 1-vector eigenspace
  b_hat = sum(diag(Qmat %*% S)) / (p - 1)                      # complement eigenspace
  sigma2 = (a_hat + (p - 1) * b_hat) / p                       # = tr(S)/p
  rho = (a_hat - b_hat) / (a_hat + (p - 1) * b_hat)
  return(list(sigma2 = sigma2, rho = rho, Sigma = cs_Sigma(sigma2, rho),
              a = a_hat, b = b_hat))
}

# ---- 1-D-profile AR(1) pseudo-true given a target covariance S ----
ar1_profile_dev <- function(rho, S) {
  Rinv <- solve(ar1_R(rho))
  sigma2 = sum(diag(Rinv %*% S)) / p
  return(p * log(sigma2) + (p - 1) * log(1 - rho^2))          # concentrated deviance (up to const)
}

ar1_project <- function(S) {
  grid <- seq(-0.97, 0.97, by = 0.02)                          # coarse pre-scan vs optimize
  gvals <- vapply(grid, function(r) { return(ar1_profile_dev(r, S)) }, numeric(1))
  r0 = grid[which.min(gvals)]
  lo = max(-0.985, r0 - 0.05); hi = min(0.985, r0 + 0.05)
  opt <- stats::optimize(function(r) { return(ar1_profile_dev(r, S)) },
                         interval = c(lo, hi), tol = 1e-10)
  rho = opt$minimum
  Rinv <- solve(ar1_R(rho))
  sigma2 = sum(diag(Rinv %*% S)) / p
  return(list(sigma2 = sigma2, rho = rho, Sigma = ar1_Sigma(sigma2, rho),
              grid_rho = r0))
}

# ---- Gaussian KL: KL( N(0,Sigma_T) || N(0,Sigma_k) ) ----
kl_mvn <- function(Sigma_T, Sigma_k) {
  ld_k = as.numeric(determinant(Sigma_k, logarithm = TRUE)$modulus)
  ld_T = as.numeric(determinant(Sigma_T, logarithm = TRUE)$modulus)
  return(0.5 * (ld_k - ld_T + sum(diag(solve(Sigma_k, Sigma_T))) - p))
}

# ---- per-cell report ----
report_cell <- function(name, Sigma_T) {
  cs <- cs_project(Sigma_T)
  ar <- ar1_project(Sigma_T)
  kl_cs = kl_mvn(Sigma_T, cs$Sigma)
  kl_ar = kl_mvn(Sigma_T, ar$Sigma)
  mineig = min(eigen(Sigma_T, symmetric = TRUE, only.values = TRUE)$values)
  rho_min = min(abs(cs$rho), abs(ar$rho))
  cat(sprintf("\n=== Cell %s ===\n", name))
  cat("Sigma_truth =\n"); print(round(Sigma_T, 6))
  cat(sprintf("  min eig(Sigma_truth) = %.6f  (PD: %s)\n", mineig, mineig > 1e-8))
  cat(sprintf("  CS*  : sigma2 = %.6f  rho = %.6f   KL(truth||CS*)  = %.6f\n",
              cs$sigma2, cs$rho, kl_cs))
  cat(sprintf("  AR1* : sigma2 = %.6f  rho = %.6f   KL(truth||AR1*) = %.6f\n",
              ar$sigma2, ar$rho, kl_ar))
  cat(sprintf("  KL gap (CS-AR1) = %+.3e\n", kl_cs - kl_ar))
  cat(sprintf("  min|pseudo-true rho| = %.4f  (gate >= %.2f: %s)\n",
              rho_min, RHO_GATE, rho_min >= RHO_GATE))
  return(list(name = name, Sigma_T = Sigma_T, cs = cs, ar = ar,
              kl_cs = kl_cs, kl_ar = kl_ar, mineig = mineig, rho_min = rho_min))
}

cat("############ todo/029 frozen pseudo-true inputs (p=4) ############\n")

# ---- Cell A: truth = AR(1) rho=0.5 ----
Sigma_A <- ar1_Sigma(1, 0.5)
resA <- report_cell("A (truth = AR(1) rho=0.5)", Sigma_A)

# ---- Cell B: equal-KL Toeplitz money cell ----
# one-parameter family interpolating an AR1-leaning and a CS-leaning correlation shape
tau_of_w <- function(w) {
  ar_lean <- c(1, 0.5, 0.25, 0.125)
  cs_lean <- c(1, 0.45, 0.45, 0.45)
  return((1 - w) * ar_lean + w * cs_lean)
}
Sigma_B_of_w <- function(w) {
  return(stats::toeplitz(tau_of_w(w)))
}
dKL_of_w <- function(w) {
  S <- Sigma_B_of_w(w)
  return(kl_mvn(S, cs_project(S)$Sigma) - kl_mvn(S, ar1_project(S)$Sigma))
}

cat("\n-- Cell B equal-KL tuning: scan dKL(w) over the Toeplitz family --\n")
ws <- seq(0, 1, by = 0.1)
for (w in ws) { cat(sprintf("   w=%.2f  dKL=%+.6f\n", w, dKL_of_w(w))) }
root <- stats::uniroot(dKL_of_w, interval = c(0, 1), tol = 1e-10)
w_star = root$root
cat(sprintf("\n  equal-KL solution: w* = %.6f  (dKL residual = %+.3e)\n",
            w_star, root$f.root))
cat(sprintf("  tau(w*) = (%s)\n", paste(sprintf("%.6f", tau_of_w(w_star)), collapse = ", ")))
Sigma_B <- Sigma_B_of_w(w_star)
resB <- report_cell("B (truth = equal-KL Toeplitz)", Sigma_B)

# ---- consolidated freeze block ----
cat("\n\n############ FREEZE FOR todo/029 ############\n")
freeze_one <- function(res) {
  cat(sprintf("[%s]\n", res$name))
  cat(sprintf("  Sigma_truth first row = (%s)\n",
              paste(sprintf("%.6f", res$Sigma_T[1, ]), collapse = ", ")))
  cat(sprintf("  CS*  (sigma2, rho) = (%.6f, %.6f)   KL = %.6f\n",
              res$cs$sigma2, res$cs$rho, res$kl_cs))
  cat(sprintf("  AR1* (sigma2, rho) = (%.6f, %.6f)   KL = %.6f\n",
              res$ar$sigma2, res$ar$rho, res$kl_ar))
  cat(sprintf("  min|rho|=%.4f (gate %s)  PD min-eig=%.6f\n",
              res$rho_min, res$rho_min >= RHO_GATE, res$mineig))
}
freeze_one(resA)
cat(sprintf("  [cell B only] equal-KL w* = %.6f, KL_CS=KL_AR1 = %.6f\n", w_star, resB$kl_cs))
freeze_one(resB)

all_ok = (resA$rho_min >= RHO_GATE) && (resB$rho_min >= RHO_GATE) &&
         (resA$mineig > 1e-8) && (resB$mineig > 1e-8)
cat(sprintf("\n==> ALL GATES PASS: %s\n", all_ok))
if (!all_ok) { stop("pseudo-true gates FAILED -- re-scope before freezing") }
