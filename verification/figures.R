# =============================================================================
# verification/figures.R
#
# Draws every Simulation-studies (@sec-simulations) exhibit from the committed
# caches and writes 300-dpi PNGs into manuscript/figures/. The manuscript prose
# (manuscript/plan/level3-paragraphs.json, section S5) includes these PNGs;
# the qmd stays a pure compile-from-JSON artifact. Run:
#
#   Rscript verification/figures.R
#
# Deterministic: reads cached summaries only, no simulation, no random numbers.
# Each exhibit carries an explicit "perfect" reference (oracle / nominal level /
# analytic target / y=x) and the achieved value, so the gap is visual.
#
# Data sources (committed, regeneration receipt 2026-06-07; W2/W4 in the
# pre-submission regen, receipt appended):
#   W1 theorem      verification/cache/W1-prod-fiml{,-N500,-N1000,-N2000}.rds
#   known-scale     verification/cache/rederivation-knownvar-N200-R200000.rds
#   LRT             verification/cache/W2-prod-amelia.rds
#   discrimination  verification/cache/w2-paired-differential-mu1-cell.rds
#   pairing         verification/cache/w2-paired-differential-spotcheck.rds
#   selection       verification/cache/run_all-prod/phase2-w3/summary.csv
#   ladder          verification/cache/ic-ladder-summary.csv
#   non-nested      verification/cache/w4-nonnested-summary.csv
#                   verification/cache/w4-dissimilar-summary.csv
# =============================================================================

options(stringsAsFactors = FALSE)
FIGDIR = "manuscript/figures"
if (!dir.exists(FIGDIR)) { dir.create(FIGDIR, recursive = TRUE) }

## ---- shared style -----------------------------------------------------------
# Okabe-Ito colourblind-safe palette, with fixed role -> colour mapping.
COL <- list(
  perfect     = "#111111",   # oracle / nominal / analytic target / y=x
  oracle      = "#111111",
  uncorrected = "#D55E00",   # vermillion
  corrected   = "#0072B2",   # blue
  mean        = "#E69F00",   # orange   (ladder rung 1)
  twomoment   = "#009E73",   # green    (ladder rung 2)
  equating    = "#CC79A7",   # purple   (ladder rung 3)
  sb          = "#7F7F7F",   # grey
  mar         = "#0072B2",
  mcar        = "#E69F00",
  band        = "#1110",     # (unused placeholder)
  bandfill    = grDevices::adjustcolor("#111111", alpha.f = 0.10)
)
PAR_DEF = list(mar = c(4.2, 4.4, 3.0, 1.2), mgp = c(2.5, 0.7, 0), las = 1,
               cex.lab = 1.05, cex.axis = 0.95, cex.main = 1.12, font.main = 1)

png_open <- function(file, w_in, h_in) {
  grDevices::png(file.path(FIGDIR, file), width = w_in, height = h_in,
                 units = "in", res = 300, type = "cairo")
  do.call(par, PAR_DEF)
}
errbar <- function(x, lo, hi, col = "#111111", lwd = 2, wd = 0.04) {
  segments(x, lo, x, hi, col = col, lwd = lwd)
  segments(x - wd, lo, x + wd, lo, col = col, lwd = lwd)
  segments(x - wd, hi, x + wd, hi, col = col, lwd = lwd)
}
ref_line <- function(y, lab, col = COL$perfect, lty = 2, at = NULL, cex = 0.85, side = "left") {
  abline(h = y, col = col, lty = lty, lwd = 1.6)
  if (!is.null(lab)) {
    usr <- par("usr")
    if (is.null(at)) {
      xx <- usr[1] + 0.015 * diff(usr[1:2])   # just inside the left axis
      text(xx, y, lab, col = col, pos = 4, offset = 0.1, cex = cex, font = 3)
    } else {
      text(at, y, lab, col = col, pos = 4, offset = 0.1, cex = cex, font = 3)
    }
  }
}
note <- function(x, y, lab, col = "#111111", cex = 0.8, pos = 4) {
  text(x, y, lab, col = col, cex = cex, pos = pos, font = 3, xpd = NA)
}

cat("Drawing S5 exhibits into", FIGDIR, "\n")

# =============================================================================
# FIG 1 -- Theorem validation (W1). E[T] vs the analytic 1/2 tr(RIV) target.
# Perfect: the (A)+(C)-augmented target band 2.42-2.55 (and the preregistered
# half-trace 2.77). Achieved: per-N points + inverse-variance pooled estimate.
# Failure (D-05): the N=1000 cell sits 2.6 se below target.
# =============================================================================
draw_w1 <- function() {
  files <- c("200"  = "verification/cache/W1-prod-fiml.rds",
             "500"  = "verification/cache/W1-prod-fiml-N500.rds",
             "1000" = "verification/cache/W1-prod-fiml-N1000.rds",
             "2000" = "verification/cache/W1-prod-fiml-N2000.rds")
  N = as.integer(names(files)); Tm = Tse = half = numeric(length(files))
  for (i in seq_along(files)) {
    o <- readRDS(files[i])
    Tm[i]   = mean(o$rep_T)
    Tse[i]  = sd(o$rep_T) / sqrt(length(o$rep_T))
    half[i] = mean(o$rep_trRIV) / 2
  }
  w = 1 / Tse^2; pooled = sum(w * Tm) / sum(w); pooled_se = sqrt(1 / sum(w))
  target = mean(half)                       # 2.77, preregistered half-trace
  aug_lo = 2.42; aug_hi = 2.55              # (A)+(C)-augmented target range
  miss_se = (Tm[N == 1000] - target) / Tse[N == 1000]

  png_open("fig-w1-theorem.png", 6.6, 4.7)
  xx = seq_along(N)
  ylim = range(c(Tm - 1.96 * Tse, Tm + 1.96 * Tse, target, aug_lo, aug_hi), na.rm = TRUE)
  ylim = c(min(ylim) - 0.3, max(ylim) + 0.5)
  plot(xx, Tm, type = "n", xaxt = "n", xlim = c(0.7, length(N) + 0.3), ylim = ylim,
       xlab = "Sample size N", ylab = expression("Net deviance bias  E[T]"),
       main = "Theorem validation: E[T] tracks the predicted half-trace")
  axis(1, at = xx, labels = N)
  # augmented target band = "perfect"
  rect(0.7, aug_lo, length(N) + 0.3, aug_hi, col = COL$bandfill, border = NA)
  ref_line(target, sprintf("preregistered target 1/2 tr(RIV) = %.2f", target),
           col = COL$perfect, lty = 3, at = 1.4)
  text(length(N) + 0.30, aug_hi + 0.02,
       sprintf("(A)+(C)-augmented\ntarget %.2f-%.2f", aug_lo, aug_hi),
       col = COL$perfect, cex = 0.7, font = 3, pos = 2, xpd = NA)
  # pooled estimate band
  abline(h = pooled, col = COL$corrected, lwd = 1.4)
  rect(0.7, pooled - pooled_se, length(N) + 0.3, pooled + pooled_se,
       col = grDevices::adjustcolor(COL$corrected, alpha.f = 0.08), border = NA)
  # per-N points + 95% CI
  errbar(xx, Tm - 1.96 * Tse, Tm + 1.96 * Tse, col = "#444444", lwd = 2)
  points(xx, Tm, pch = 21, bg = COL$corrected, col = "#111111", cex = 1.5)
  # flag the N=1000 miss
  j = which(N == 1000)
  note(xx[j] + 0.08, Tm[j], sprintf("N=1000: %.1f se\nbelow target", miss_se),
       col = COL$uncorrected, cex = 0.74)
  note(1.5, pooled - 0.02, sprintf("pooled %.2f +/- %.2f", pooled, pooled_se),
       col = COL$corrected, cex = 0.78, pos = 1)
  legend("topright", bty = "n", cex = 0.78,
         legend = c("E[T] per N (95% CI)", "inverse-variance pooled",
                    "analytic target (perfect)"),
         pch = c(21, NA, NA), pt.bg = c(COL$corrected, NA, NA),
         lty = c(NA, 1, 3), col = c("#111111", COL$corrected, COL$perfect),
         lwd = c(NA, 1.4, 1.6))
  grDevices::dev.off()
  cat("  fig-w1-theorem.png  (pooled", round(pooled, 3), "+/-", round(pooled_se, 3),
      "; N=1000 miss", round(miss_se, 2), "se)\n")
}

# =============================================================================
# FIG 2 -- Sign regime / known scale. Two arms vs their analytic targets.
# Perfect: 0 (deterministic FIML) and -1/2 tr(RIV) (proper MI).
# =============================================================================
draw_knownscale <- function() {
  o <- readRDS("verification/cache/rederivation-knownvar-N200-R200000.rds")$summary
  half = o$trRIV / 2
  est = c(o$T_fiml, o$T_proper); se = c(o$se$T_fiml, o$se$T_proper)
  tgt = c(0, -half)
  lab = c("deterministic FIML", "proper MI")
  png_open("fig-knownscale.png", 5.8, 4.6)
  xx = c(1, 2)
  ylim = c(min(est - 1.96 * se, tgt) - 0.12, max(est + 1.96 * se, tgt) + 0.12)
  plot(xx, est, type = "n", xaxt = "n", xlim = c(0.6, 2.4), ylim = ylim,
       xlab = "", ylab = expression("Net deviance bias  E[T]   (known scale)"),
       main = "Known scale: the two imputation arms hit 0 and -1/2 tr(RIV)")
  axis(1, at = xx, labels = lab)
  abline(h = 0, col = "#cccccc", lwd = 1)
  # target markers (perfect)
  segments(xx - 0.22, tgt, xx + 0.22, tgt, col = COL$perfect, lwd = 2.4, lty = 1)
  text(xx, tgt, c("perfect = 0", sprintf("perfect = -1/2 tr(RIV) = %.3f", -half)),
       col = COL$perfect, pos = c(3, 1), cex = 0.8, font = 3, offset = 0.6)
  # achieved
  errbar(xx, est - 1.96 * se, est + 1.96 * se, col = "#444444", lwd = 2, wd = 0.05)
  points(xx, est, pch = 23, bg = COL$corrected, col = "#111111", cex = 1.7)
  note(xx, est, sprintf("%.3f", est), col = COL$corrected, pos = 4, cex = 0.82)
  legend("right", bty = "n", cex = 0.8,
         legend = c("achieved E[T] (95% CI)", "analytic target (perfect)"),
         pch = c(23, NA), pt.bg = c(COL$corrected, NA),
         lty = c(NA, 1), col = c("#111111", COL$perfect), lwd = c(NA, 2.4))
  grDevices::dev.off()
  cat("  fig-knownscale.png\n")
}

# =============================================================================
# FIG 3 -- LRT absorption (W2). Type I error at the null for the four references
# vs nominal 0.05 (perfect). The study's claim is size control: a correctly
# calibrated reference absorbs the differential bias, so the test holds its
# Type I error. (Raw power across the local alternative is not shown: the arms
# have different Type I error, so a raw power comparison is confounded; the
# size-adjusted power conjecture is treated in the Discussion.)
# =============================================================================
draw_lrt <- function() {
  rt <- readRDS("verification/cache/W2-prod-amelia.rds")$rejection_table
  r0 = rt[rt$delta == 0, ]
  arms = c("oracle", "corrected", "uncorrected", "Satorra-\nBentler")
  vals = as.numeric(r0[, c("C1_oracle", "C2_corrected", "C3_uncorrected", "C5_SB")])
  mcse = c(NA, r0$mcse_corrected, r0$mcse_uncorrected, r0$mcse_sb)
  cols = c(COL$oracle, COL$corrected, COL$uncorrected, COL$sb)
  png_open("fig-lrt-absorption.png", 6.4, 4.7)
  xx = seq_along(arms)
  plot(xx, vals, type = "n", xaxt = "n", xlim = c(0.6, length(arms) + 0.4),
       ylim = c(0, 0.075), xlab = "",
       ylab = "Type I error (rejection rate at the null)",
       main = "Likelihood-ratio Type I error: the reference absorbs the bias")
  axis(1, at = xx, labels = arms, padj = 0.5)
  # nominal 0.05 = perfect
  rect(0.6, 0.05 - 0.005, length(arms) + 0.4, 0.05 + 0.005, col = COL$bandfill, border = NA)
  abline(h = 0.05, col = COL$perfect, lty = 2, lwd = 1.6)
  note(0.7, 0.058, "nominal 0.05 (perfect)", col = COL$perfect, cex = 0.82, pos = 4)
  for (i in seq_along(arms)) {
    if (!is.na(mcse[i])) { errbar(xx[i], vals[i] - mcse[i], vals[i] + mcse[i], col = "#444444", lwd = 2, wd = 0.06) }
  }
  points(xx, vals, pch = 21, bg = cols, col = "#111111", cex = 2)
  text(xx + 0.13, vals, sprintf("%.3f", vals), pos = 4, offset = 0.1, cex = 0.85, col = "#222222")
  note(2.5, 0.012, "corrected is slightly conservative (double-counting); uncorrected is\nabsorbed by the calibrated reference -- both near nominal",
       col = "#666666", cex = 0.72, pos = 3)
  grDevices::dev.off()
  cat("  fig-lrt-absorption.png  (Type I error: oracle", vals[1], "/ corrected", vals[2], "/ uncorrected", vals[3], ")\n")
}

# =============================================================================
# FIG 4 -- Discrimination of the two formulas (mu1 cell). Observed paired
# differential vs the correct projected-trace prediction (perfect) and the
# naive trace difference (rejected). ~52 se separation.
# =============================================================================
draw_discrimination <- function() {
  m <- readRDS("verification/cache/w2-paired-differential-mu1-cell.rds")$summary
  N = as.integer(rownames(m)); est = m[, "est"]; se = m[, "se"]
  pred = mean(m[, "B_direct"]); naive = mean(m[, "D_naive"])
  sep = (naive - mean(est)) / mean(se)
  png_open("fig-discrimination.png", 6.4, 4.7)
  xx = seq_along(N)
  plot(xx, est, type = "n", xaxt = "n", xlim = c(0.7, length(N) + 0.6), ylim = c(0, 9.4),
       xlab = "Sample size N", ylab = "Observed differential bias (deviance units)",
       main = "Discrimination: the data sit on the projected-trace formula")
  axis(1, at = xx, labels = N)
  abline(h = pred, col = COL$perfect, lty = 1, lwd = 1.6)
  abline(h = naive, col = COL$uncorrected, lty = 2, lwd = 1.6)
  note(0.72, naive + 0.35, sprintf("naive trace difference = %.1f  (rejected)", naive),
       col = COL$uncorrected, cex = 0.82, pos = 4)
  note(0.72, pred + 0.9, sprintf("projected trace  tr(RIV_perp) = %.2f  (correct, perfect)", pred),
       col = COL$perfect, cex = 0.82, pos = 4)
  errbar(xx, est - 1.96 * se, est + 1.96 * se, col = "#444444", lwd = 2.2, wd = 0.05)
  points(xx, est, pch = 21, bg = COL$corrected, col = "#111111", cex = 1.6)
  note(xx, est, sprintf("%.2f", est), col = COL$corrected, pos = 4, cex = 0.82)
  arrows(length(N) + 0.45, pred, length(N) + 0.45, naive, code = 3, length = 0.06, col = "#888888")
  note(length(N) + 0.45, mean(c(pred, naive)), sprintf("%.0f se", sep), col = "#555555", pos = 4, cex = 0.78)
  legend("left", bty = "n", cex = 0.8,
         legend = c("observed differential (95% CI)", "correct formula (perfect)", "naive formula (rejected)"),
         pch = c(21, NA, NA), pt.bg = c(COL$corrected, NA, NA),
         lty = c(NA, 1, 2), col = c("#111111", COL$perfect, COL$uncorrected), lwd = c(NA, 1.6, 1.6))
  grDevices::dev.off()
  cat("  fig-discrimination.png  (", round(sep), "se )\n")
}

# =============================================================================
# FIG 5 -- Pairing (spotcheck). Single-model deviance sd grows as sqrt(n);
# the paired differential stays O(1) at the null (perfect) but the sqrt(n)
# growth returns at a fixed alternative (the documented failure mode).
# =============================================================================
draw_pairing <- function() {
  s <- readRDS("verification/cache/w2-paired-differential-spotcheck.rds")$summary
  N = c(500, 1000, 2000)
  single_h0 = s[paste0("H0_", N), "sd_Tf"]
  paired_h0 = s[paste0("H0_", N), "sd_D"]
  paired_fx = s[paste0("fixed_", N), "sd_D"]
  png_open("fig-pairing.png", 6.4, 4.7)
  ylim = c(min(paired_h0) * 0.8, max(single_h0) * 1.18)
  plot(N, single_h0, type = "n", log = "xy", ylim = ylim, xlab = "Sample size N",
       ylab = "Standard deviation of the deviance statistic",
       main = "Pairing keeps the null differential O(1) while single-model sd grows")
  lines(N, single_h0, col = COL$uncorrected, lwd = 2.2); points(N, single_h0, pch = 16, col = COL$uncorrected)
  lines(N, paired_fx, col = COL$sb, lwd = 2.0, lty = 2); points(N, paired_fx, pch = 17, col = COL$sb)
  lines(N, paired_h0, col = COL$corrected, lwd = 2.4); points(N, paired_h0, pch = 16, col = COL$corrected)
  note(2000, single_h0[3], "single model (~sqrt(n))", col = COL$uncorrected, pos = 2, cex = 0.78)
  note(2000, paired_fx[3], "paired, fixed alt (sqrt(n) returns)", col = COL$sb, pos = 2, cex = 0.78)
  note(1000, paired_h0[2], "paired at null: O(1)  (perfect)", col = COL$corrected, pos = 3, cex = 0.78)
  legend("left", bty = "n", cex = 0.8,
         legend = c("single-model sd, null", "paired sd, null (perfect)", "paired sd, fixed alternative"),
         col = c(COL$uncorrected, COL$corrected, COL$sb), lwd = c(2.2, 2.4, 2.0),
         lty = c(1, 1, 2), pch = c(16, 16, 17))
  grDevices::dev.off()
  cat("  fig-pairing.png\n")
}

# =============================================================================
# FIG 6 -- Selection sweep (W3). True-model selection rate: oracle (perfect)
# vs uncorrected MI-AIC vs corrected, deterministic FIML, non-monotone MAR.
# =============================================================================
draw_w3 <- function() {
  w3 <- read.csv("verification/cache/run_all-prod/phase2-w3/summary.csv")
  s = w3[w3$engine == "fiml" & w3$pattern == "non_monotone" & w3$mech == "MAR", ]
  s = s[order(s$N), ]
  N = s$N
  M = rbind(oracle = s$pi_oracle, uncorrected = s$pi_uncorrected, corrected = s$pi_corrected)
  png_open("fig-w3-selection.png", 7.0, 4.7)
  cols = c(COL$oracle, COL$uncorrected, COL$corrected)
  bp = barplot(M, beside = TRUE, names.arg = paste0("N=", N), col = cols, border = NA,
               ylim = c(0, 1.02), ylab = "True-model selection rate",
               main = "Selection: correction recovers toward the complete-data oracle")
  for (j in seq_along(N)) {
    abline(h = M["oracle", j], col = COL$perfect, lty = 3, lwd = 1.2)
  }
  text(as.vector(bp), as.vector(M), sprintf("%.2f", as.vector(M)), pos = 3, cex = 0.68, offset = 0.35, xpd = NA)
  note(mean(bp), 0.30, "100% of uncorrected misclassifications\nland on the largest-RIV candidate",
       col = "#555555", cex = 0.78, pos = 3)
  legend("bottomright", bty = "n", cex = 0.82, horiz = FALSE,
         legend = c("complete-data oracle (perfect)", "uncorrected MI-AIC", "corrected MI-AIC"),
         fill = cols, border = NA)
  grDevices::dev.off()
  cat("  fig-w3-selection.png\n")
}

# =============================================================================
# FIG 7 -- The distribution-matching ladder. True-model selection rate per cell;
# oracle per cell is the "perfect" reference line. Two-moment and equating reach
# the oracle at rho=0.40; the weak-signal floor at rho=0.10 is the failure.
# =============================================================================
draw_ladder <- function() {
  L <- read.csv("verification/cache/ic-ladder-summary.csv")
  L = L[match(c("MAIN", "WEAK", "JUNK"), L$cell), ]
  cell_lab = c(expression(rho == 0.40), expression(rho == 0.10), expression(rho == 0))
  arms = c("uncorrected", "mean", "two-moment", "equating")
  M = rbind(L$pi_r0, L$pi_r1, L$pi_r2, L$pi_r3)
  cols = c(COL$uncorrected, COL$mean, COL$twomoment, COL$equating)
  png_open("fig-ladder.png", 8.2, 4.8)
  bp = barplot(M, beside = TRUE, col = cols, border = NA, ylim = c(0, 1.02),
               names.arg = rep("", 3), ylab = "True-model selection rate",
               main = "Distribution-matching ladder: arms vs the complete-data oracle")
  grp_centre = colMeans(bp)
  axis(1, at = grp_centre, labels = FALSE)
  mtext(cell_lab, side = 1, line = 1.0, at = grp_centre)
  for (j in 1:3) {
    segments(bp[1, j] - 0.5, L$pi_oracle[j], bp[4, j] + 0.5, L$pi_oracle[j],
             col = COL$perfect, lty = 2, lwd = 1.8)
    text(bp[1, j] - 0.5, L$pi_oracle[j], sprintf("oracle %.2f", L$pi_oracle[j]),
         col = COL$perfect, cex = 0.68, font = 3, pos = 3, offset = 0.2, xpd = NA)
  }
  text(as.vector(bp), as.vector(M), sprintf("%.2f", as.vector(M)), pos = 3, cex = 0.58, offset = 0.25, xpd = NA)
  note(grp_centre[2], 0.745, "weak-signal floor:", col = COL$uncorrected, cex = 0.74, pos = 3)
  note(grp_centre[2], 0.745, "no arm reaches the oracle", col = COL$uncorrected, cex = 0.74, pos = 1)
  legend("topright", bty = "n", cex = 0.78, ncol = 2,
         legend = c(arms, "oracle (perfect)"),
         fill = c(cols, NA), border = NA, lty = c(NA, NA, NA, NA, 2),
         col = c(NA, NA, NA, NA, COL$perfect), lwd = c(NA, NA, NA, NA, 1.8))
  grDevices::dev.off()
  cat("  fig-ladder.png\n")
}

# =============================================================================
# FIG 8 -- Ladder internals (MAIN cell). Left: null-side Kolmogorov-Smirnov
# distance to the paired complete-data statistic falls across the four arms
# (perfect = 0). Right: noncentral shrinkage, measured vs predicted on y=x.
# =============================================================================
draw_ladder_internals <- function() {
  L <- read.csv("verification/cache/ic-ladder-summary.csv")
  m = L[L$cell == "MAIN", ]
  png_open("fig-ladder-internals.png", 9.4, 4.6)
  par(mfrow = c(1, 2))
  ## panel A: null-side KS across arms
  arms = c("uncorrected", "mean", "two-moment", "equating")
  ks = as.numeric(m[, c("ks0_MC", "ks1_MC", "ks2_MC", "ks3_MC")])
  vr = as.numeric(m[, c("varratio0_MC", "varratio2_MC", "varratio3_MC")])
  cols = c(COL$uncorrected, COL$mean, COL$twomoment, COL$equating)
  bp = barplot(ks, names.arg = arms, col = cols, border = NA, ylim = c(0, 0.33),
               ylab = "KS distance to complete-data null", main = "A. Null side calibrates")
  text(bp, ks, sprintf("%.3f", ks), pos = 3, cex = 0.78, offset = 0.5, xpd = NA)
  ref_line(0, "perfect = 0", col = COL$perfect, lty = 2, at = bp[1])
  note(bp[3], 0.30, sprintf("variance ratio falls\n%.2f -> %.2f", m$varratio0_MC, m$varratio2_MC),
       col = "#555555", cex = 0.78, pos = 3)
  ## panel B: noncentral shrinkage measured vs predicted (y=x)
  pred = c(two_moment = m$a_MC_mean, equating = 1 / m$lammax_MC_mean)
  meas = c(two_moment = m$ncratio2_MA, equating = m$ncratio3_MA)
  lim = c(0.3, 0.65)
  plot(pred, meas, type = "n", xlim = lim, ylim = lim, xlab = "Predicted shrinkage factor",
       ylab = "Measured shrinkage factor", main = "B. Noncentral shrinkage on y = x")
  abline(0, 1, col = COL$perfect, lty = 2, lwd = 1.8)
  text(mean(lim), max(lim), "y = x (perfect)", col = COL$perfect, font = 3, cex = 0.82, pos = 1)
  points(pred, meas, pch = c(16, 17), col = c(COL$twomoment, COL$equating), cex = 1.7)
  text(pred, meas, c(sprintf("two-moment (a_k=%.2f)", pred[1]),
                     sprintf("equating (1/lam_max=%.2f)", pred[2])),
       pos = c(2, 4), cex = 0.76, col = c(COL$twomoment, COL$equating))
  grDevices::dev.off()
  cat("  fig-ladder-internals.png\n")
}

# =============================================================================
# FIG 9 -- Non-nested (W4). Left: each candidate's (A)+(C) level is a large O(1)
# under MAR and collapses under MCAR (mechanism). Right: the isolated
# design-imbalance differential with 95% CI -- below resolution for the similar
# pair (failure, CI spans 0) and resolved at -1.2 for the dissimilar pair.
# =============================================================================
draw_w4 <- function() {
  D <- read.csv("verification/cache/w4-dissimilar-summary.csv")
  NN <- read.csv("verification/cache/w4-nonnested-summary.csv")
  png_open("fig-w4-nonnested.png", 9.6, 4.7)
  par(mfrow = c(1, 2))
  ## panel A: per-candidate (A)+(C) level, MAR vs MCAR (dissimilar pair, N=500)
  d_mar  = D[D$cell == "A"      & D$N == 500, ]
  d_mcar = D[D$cell == "Aprime" & D$N == 500, ]
  M = rbind(MAR  = c(d_mar$lvl_diag,  d_mar$lvl_ar),
            MCAR = c(d_mcar$lvl_diag, d_mcar$lvl_ar))
  colnames(M) = c("diagonal", "AR(1)")
  bp = barplot(M, beside = TRUE, col = c(COL$mar, COL$mcar), border = NA, ylim = c(0, 3.3),
               ylab = "(A)+(C) level (deviance units)", main = "A. Level collapses under MCAR")
  text(as.vector(bp), as.vector(t(M)), sprintf("%.2f", as.vector(t(M))), pos = 3, cex = 0.74, offset = 0.4, xpd = NA)
  ref_line(0, "MCAR target = 0 (perfect)", col = COL$perfect, lty = 2, at = bp[1])
  legend("topright", bty = "n", cex = 0.82, fill = c(COL$mar, COL$mcar), border = NA,
         legend = c("MAR", "MCAR twin"))
  ## panel B: isolated differential +/- 95% CI, similar vs dissimilar
  Ns = c(500, 1000, 2000)
  iso <- function(df) {
    mar  = df[df$cell == "A"      & df$N %in% Ns, ]
    mcar = df[df$cell == "Aprime" & df$N %in% Ns, ]
    mar = mar[order(mar$N), ]; mcar = mcar[order(mcar$N), ]
    list(N = mar$N, est = mar$resid - mcar$resid,
         se = sqrt(mar$resid_se^2 + mcar$resid_se^2))
  }
  sim = iso(NN); dis = iso(D)
  xs = seq_along(Ns)
  plot(0, 0, type = "n", xlim = c(0.6, length(Ns) + 0.4),
       ylim = c(-2.4, 1.4), xaxt = "n", xlab = "Sample size N",
       ylab = "Isolated (A)+(C) differential", main = "B. Resolved only for the dissimilar pair")
  axis(1, at = xs, labels = Ns)
  abline(h = 0, col = COL$perfect, lty = 2, lwd = 1.8)
  text(length(Ns) + 0.3, 0, "no effect", col = COL$perfect, font = 3, cex = 0.76, pos = 3)
  off = 0.12
  errbar(xs - off, sim$est - 1.96 * sim$se, sim$est + 1.96 * sim$se, col = COL$sb, lwd = 2, wd = 0.05)
  points(xs - off, sim$est, pch = 16, col = COL$sb, cex = 1.4)
  errbar(xs + off, dis$est - 1.96 * dis$se, dis$est + 1.96 * dis$se, col = COL$corrected, lwd = 2.2, wd = 0.05)
  points(xs + off, dis$est, pch = 18, col = COL$corrected, cex = 1.8)
  note(1 + off, dis$est[1], sprintf("-1.2 (%.1f se)", dis$est[1] / dis$se[1]), col = COL$corrected, pos = 1, cex = 0.76)
  legend("bottomleft", bty = "n", cex = 0.8,
         legend = c("similar pair: CS vs AR(1)  (below resolution)",
                    "dissimilar pair: diagonal vs AR(1)  (resolved)"),
         pch = c(16, 18), col = c(COL$sb, COL$corrected), lwd = c(2, 2.2))
  grDevices::dev.off()
  cat("  fig-w4-nonnested.png\n")
}

## ---- draw all ---------------------------------------------------------------
draw_w1()
draw_knownscale()
draw_lrt()
draw_discrimination()
draw_pairing()
draw_w3()
draw_ladder()
draw_ladder_internals()
draw_w4()
cat("Done. 9 PNG exhibits in", FIGDIR, "\n")
