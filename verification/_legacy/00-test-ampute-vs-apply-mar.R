# 00-test-ampute-vs-apply-mar.R
#
# Validation smoke test (todo/006 Step 3): confirm that
# apply_missingness_ampute(..., mech="MAR", pattern_type="non_monotone")
# produces statistically equivalent marginal rates and conditional structure
# to the legacy apply_mar() at a matched target proportion. Also verifies
# the other three combinations (MAR/MNAR x non_monotone/monotone) ampute
# successfully and hit their target marginals.
#
# Gate: must PASS before running the comprehensive sweep.

source("verification/00-setup.R")

cat("\n== ampute-vs-apply_mar smoke test ==\n\n")

set.seed(20260523)
N_big <- 10000

# Truth fixture: default DGP from 00-setup.R.
X_big <- gen_data(N = N_big, mu = default_mu, Sigma = default_Sigma)

# -----------------------------------------------------------------------------
# Part A: ampute MAR/non_monotone vs apply_mar (legacy).
#
# apply_mar uses (a,b) = (-0.5, 0.4) on standard-normal X_3, X_4 -> marginal
# missingness on X_1, X_2 each ~= Phi(-0.5 / sqrt(1 + 0.4^2)) ~= 0.318.
# We feed ampute a target prop = 0.318 to match.
# -----------------------------------------------------------------------------

set.seed(20260523)
ml_legacy <- apply_mar(X_big)

set.seed(20260523)
ml_ampute <- apply_missingness_ampute(X_big, prop = 0.318,
                                       mech = "MAR",
                                       pattern_type = "non_monotone")

mrg <- function(m) { return(colMeans(m$R)) }
mrg_legacy <- mrg(ml_legacy)
mrg_ampute <- mrg(ml_ampute)

cat("Part A: ampute MAR/non_monotone (prop=0.318) vs apply_mar\n")
cat(sprintf("  marginals legacy : X_1=%.3f X_2=%.3f X_3=%.3f X_4=%.3f\n",
            mrg_legacy[1], mrg_legacy[2], mrg_legacy[3], mrg_legacy[4]))
cat(sprintf("  marginals ampute : X_1=%.3f X_2=%.3f X_3=%.3f X_4=%.3f\n",
            mrg_ampute[1], mrg_ampute[2], mrg_ampute[3], mrg_ampute[4]))

# Tolerance: 1 pp for marginal rates.
tol_mrg <- 0.015
passA_mrg <- (abs(mrg_legacy[1] - mrg_ampute[1]) <= tol_mrg) &&
             (abs(mrg_legacy[2] - mrg_ampute[2]) <= tol_mrg) &&
             (mrg_legacy[3] == 0) && (mrg_legacy[4] == 0) &&
             (mrg_ampute[3] == 0) && (mrg_ampute[4] == 0)

# Conditional structure: P(X_1 missing | X_3 above/below median).
above_X3 <- X_big[, 3] >  median(X_big[, 3])
below_X3 <- X_big[, 3] <= median(X_big[, 3])
above_X4 <- X_big[, 4] >  median(X_big[, 4])
below_X4 <- X_big[, 4] <= median(X_big[, 4])
cond_legacy <- c(
  X1_givenHi_X3 = mean(ml_legacy$R[above_X3, 1]),
  X1_givenLo_X3 = mean(ml_legacy$R[below_X3, 1]),
  X2_givenHi_X4 = mean(ml_legacy$R[above_X4, 2]),
  X2_givenLo_X4 = mean(ml_legacy$R[below_X4, 2])
)
cond_ampute <- c(
  X1_givenHi_X3 = mean(ml_ampute$R[above_X3, 1]),
  X1_givenLo_X3 = mean(ml_ampute$R[below_X3, 1]),
  X2_givenHi_X4 = mean(ml_ampute$R[above_X4, 2]),
  X2_givenLo_X4 = mean(ml_ampute$R[below_X4, 2])
)
cat("  conditional rates (legacy / ampute):\n")
for (k in names(cond_legacy)) {
  cat(sprintf("    %-15s : %.3f / %.3f\n",
              k, cond_legacy[k], cond_ampute[k]))
}

# Sanity: each method shows the "more missing at high X_j" direction.
dir_legacy_ok <- (cond_legacy["X1_givenHi_X3"] > cond_legacy["X1_givenLo_X3"]) &&
                 (cond_legacy["X2_givenHi_X4"] > cond_legacy["X2_givenLo_X4"])
dir_ampute_ok <- (cond_ampute["X1_givenHi_X3"] > cond_ampute["X1_givenLo_X3"]) &&
                 (cond_ampute["X2_givenHi_X4"] > cond_ampute["X2_givenLo_X4"])

passA <- passA_mrg && dir_legacy_ok && dir_ampute_ok
cat(sprintf("  marginals match within %.2f : %s\n", tol_mrg,
            if (passA_mrg) "PASS" else "FAIL"))
cat(sprintf("  legacy direction (X_j miss more at high driver) : %s\n",
            if (dir_legacy_ok) "PASS" else "FAIL"))
cat(sprintf("  ampute direction (X_j miss more at high driver) : %s\n",
            if (dir_ampute_ok) "PASS" else "FAIL"))


# -----------------------------------------------------------------------------
# Part B: the other three combinations ampute successfully and hit targets.
# -----------------------------------------------------------------------------

cat("\nPart B: other ampute combinations at prop=0.40\n")

target <- 0.40
tol_target <- 0.03  # 3 pp tolerance on marginal-rate target
results_B <- list()

for (mech in c("MAR", "MNAR")) {
  for (pat in c("non_monotone", "monotone")) {
    key <- sprintf("%s+%s", mech, pat)
    set.seed(20260523)
    ml <- apply_missingness_ampute(X_big, prop = target,
                                   mech = mech, pattern_type = pat)
    mr <- colMeans(ml$R)
    # Target marginal: X_1 and X_2 for non_monotone; X_4 for monotone.
    if (pat == "non_monotone") {
      hit_target <- abs(mean(mr[1:2]) - target) <= tol_target
      cat(sprintf("  %-20s : marginals %.3f %.3f %.3f %.3f  target X1,X2 mean = %.3f  %s\n",
                  key, mr[1], mr[2], mr[3], mr[4], mean(mr[1:2]),
                  if (hit_target) "PASS" else "FAIL"))
    } else {  # monotone
      hit_target <- abs(mr[4] - target) <= tol_target
      # Sanity: monotone structure (rate increases with index depth).
      monotone_ok <- (mr[1] == 0) && (mr[2] <= mr[3]) && (mr[3] <= mr[4])
      cat(sprintf("  %-20s : marginals %.3f %.3f %.3f %.3f  target X_4 = %.3f  %s  (monotone-ok: %s)\n",
                  key, mr[1], mr[2], mr[3], mr[4], mr[4],
                  if (hit_target) "PASS" else "FAIL",
                  if (monotone_ok) "yes" else "no"))
      hit_target <- hit_target && monotone_ok
    }
    results_B[[key]] <- list(marginals = mr, hit_target = hit_target)
  }
}

passB <- all(sapply(results_B, function(rr) rr$hit_target))


# -----------------------------------------------------------------------------
# Overall verdict.
# -----------------------------------------------------------------------------

cat("\n== Overall ==\n")
cat(sprintf("  Part A (ampute MAR/non_monotone vs apply_mar) : %s\n",
            if (passA) "PASS" else "FAIL"))
cat(sprintf("  Part B (4 mech x pattern combos hit targets)  : %s\n",
            if (passB) "PASS" else "FAIL"))

if (passA && passB) {
  cat("\nSMOKE TEST PASS — comprehensive sweep is gated to proceed.\n\n")
} else {
  cat("\nSMOKE TEST FAIL — fix before running the sweep.\n\n")
  quit(status = 1)
}
