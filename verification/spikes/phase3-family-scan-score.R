# spikes/phase3-family-scan-score.R
#
# Scores the todo/045 Q2 production scan against the PRE-REGISTERED criteria
# P1-P6 (todo/045 Sec.3.2/3.3, dated 2026-07-04, committed at 4aaeaae BEFORE the
# production run). Reads the four phase3-family-scan-*-prod.rds caches and
# prints a pass/fail scorecard plus the quantities the write-up cites.
#
# Usage: Rscript verification/spikes/phase3-family-scan-score.R [out_suffix]

args <- commandArgs(trailingOnly = TRUE)
SUF <- if (length(args) >= 1) args[1] else "prod"

path <- function(arm) {
  return(sprintf("verification/cache/phase3-family-scan-%s-%s.rds", arm, SUF))
}

pass <- function(name, ok, detail) {
  cat(sprintf("[%s] %s\n        %s\n", if (ok) { "PASS" } else { "FAIL" }, name, detail))
  return(ok)
}

all_ok <- TRUE

# -----------------------------------------------------------------------------
# P1: Bernoulli FITTED asymptote via WLS fit ratio(N) = a + C/N
# -----------------------------------------------------------------------------
bf <- readRDS(path("bern_fitted"))$out
Ns <- vapply(bf, function(z) { return(z$N) }, numeric(1))
ratios <- vapply(bf, function(z) { return(z$ratio_analytic) }, numeric(1))
ses <- vapply(bf, function(z) { return(z$se_ratio_analytic) }, numeric(1))
wls <- lm(ratios ~ I(1 / Ns), weights = 1 / ses^2)
a_hat = unname(coef(wls)[1])
C_hat = unname(coef(wls)[2])
# WLS coefficient se with known variances (no residual rescaling): use the
# unscaled covariance (X'WX)^-1, not summary.lm's sigma^2-scaled one
Xd <- cbind(1, 1 / Ns)
W <- diag(1 / ses^2)
cov_known <- solve(t(Xd) %*% W %*% Xd)
a_se = sqrt(cov_known[1, 1])
cat("\n== P1: Bernoulli FITTED N-scan ==\n")
for (i in seq_along(Ns)) {
  cat(sprintf("   N=%4d  ratio=%+.4f (se %.4f)\n", Ns[i], ratios[i], ses[i]))
}
cat(sprintf("   WLS: a_hat=%+.4f (se %.4f, known-variance), C_hat=%+.2f\n", a_hat, a_se, C_hat))
ok <- abs(a_hat - 0.5) <= 2 * a_se
all_ok <- pass("P1 asymptote a_hat within 2 se of +0.500", ok,
               sprintf("a_hat=%+.4f, |a-0.5|/se=%.2f", a_hat, abs(a_hat - 0.5) / a_se)) && all_ok
# continuity vs the cached phase-3 N=200 value +0.846 (se 0.161), analytic den
cont_diff = abs(ratios[Ns == 200] - 0.846)
cont_se = sqrt(0.161^2 + ses[Ns == 200]^2)
all_ok <- pass("P1 continuity vs cached +0.846 (se 0.161) at N=200 (2 combined se)",
               cont_diff <= 2 * cont_se,
               sprintf("new=%+.4f, |diff|=%.3f = %.2f combined se", ratios[Ns == 200],
                       cont_diff, cont_diff / cont_se)) && all_ok

# -----------------------------------------------------------------------------
# P2: draw discount at N=2000 within 2 se of -0.2606
# -----------------------------------------------------------------------------
bd <- readRDS(path("bern_draw"))$out
cat("\n== P2: Bernoulli draw-FITTED paired discount ==\n")
for (z in bd) {
  cat(sprintf("   N=%4d  diff-ratio=%+.4f (se %.4f)   trRIV sample=%.4f analytic=%.4f\n",
              z$N, z$diff_ratio_analytic, z$se_diff_ratio,
              z$mean_trRIV_sample, z$trRIV_analytic))
}
z2k <- bd[["2000"]]
ok <- abs(z2k$diff_ratio_analytic - (-0.2606)) <= 2 * z2k$se_diff_ratio
all_ok <- pass("P2 diff-ratio at N=2000 within 2 se of -0.2606", ok,
               sprintf("meas=%+.4f (se %.4f), |diff|/se=%.2f", z2k$diff_ratio_analytic,
                       z2k$se_diff_ratio,
                       abs(z2k$diff_ratio_analytic + 0.2606) / z2k$se_diff_ratio)) && all_ok

# -----------------------------------------------------------------------------
# P3: Poisson blind arm at N=1000 within 2 se of +0.1039
# -----------------------------------------------------------------------------
pf <- readRDS(path("pois_fitted"))$out
cat("\n== P3: Poisson FITTED (blind out-of-family arm) ==\n")
for (z in pf) {
  cat(sprintf("   N=%4d  ratio=%+.4f (se %.4f)\n", z$N, z$ratio_analytic, z$se_ratio_analytic))
}
z1k <- pf[["1000"]]
ok <- abs(z1k$ratio_analytic - 0.1039) <= 2 * z1k$se_ratio_analytic
all_ok <- pass("P3 Poisson ratio at N=1000 within 2 se of +0.1039", ok,
               sprintf("meas=%+.4f (se %.4f), |diff|/se=%.2f", z1k$ratio_analytic,
                       z1k$se_ratio_analytic,
                       abs(z1k$ratio_analytic - 0.1039) / z1k$se_ratio_analytic)) && all_ok

# -----------------------------------------------------------------------------
# P4: mice sample tr(RIV) within 3% of analytic at every N
# -----------------------------------------------------------------------------
cat("\n== P4: sample tr(RIV) sanity ==\n")
dev <- vapply(bd, function(z) {
  return(abs(z$mean_trRIV_sample / z$trRIV_analytic - 1))
}, numeric(1))
all_ok <- pass("P4 sample trRIV within 3% of analytic at every N", all(dev <= 0.03),
               sprintf("max deviation = %.2f%%", 100 * max(dev))) && all_ok

# -----------------------------------------------------------------------------
# P5/P6: Student-t exemplar
# -----------------------------------------------------------------------------
tx <- readRDS(path("t_exemplar"))$out
cat("\n== P5/P6: Student-t known-scale exemplar ==\n")
cat(sprintf("   FITTED ratio=%+.4f (se %.4f)   DRAW ratio=%+.4f (se %.4f)   R=%d\n",
            tx$ratio_fitted, tx$se_ratio_fitted, tx$ratio_draw, tx$se_ratio_draw, tx$R))
all_ok <- pass("P5 t-exemplar FITTED within 2 se of 0",
               abs(tx$ratio_fitted) <= 2 * tx$se_ratio_fitted,
               sprintf("meas=%+.4f (se %.4f), |diff|/se=%.2f", tx$ratio_fitted,
                       tx$se_ratio_fitted, abs(tx$ratio_fitted) / tx$se_ratio_fitted)) && all_ok
all_ok <- pass("P6 t-exemplar DRAW within 2 se of -0.500",
               abs(tx$ratio_draw - (-0.5)) <= 2 * tx$se_ratio_draw,
               sprintf("meas=%+.4f (se %.4f), |diff|/se=%.2f", tx$ratio_draw,
                       tx$se_ratio_draw, abs(tx$ratio_draw + 0.5) / tx$se_ratio_draw)) && all_ok

cat(sprintf("\n== scorecard: %s ==\n", if (all_ok) { "ALL REGISTERED CRITERIA PASS" } else { "AT LEAST ONE CRITERION FAILED" }))
