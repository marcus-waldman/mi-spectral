# W3-sweep-rivs-preflight.R
#
# Pre-flight tr(RIV) table for the W3 candidate models {M_A, M_B, M_C, M_D}
# across (pattern, mech, N) combinations (todo/006 Step 6b).
#
# For each cell, generate `n_seeds` replicates of (X, missingness) at the
# truth and compute analytic tr(RIV) per candidate via
# tr_riv_analytic_general (restricted to each model's free-parameter set).
# Average across seeds to give a stable estimate of "expected" tr(RIV) per
# cell.
#
# H1 prediction (monotone vs non-monotone): monotone is predicted to have
# MORE heterogeneous tr(RIV) across candidates (esp larger spread between
# M_C and M_D), producing a larger W3-A.
#
# Cache: verification/cache/W3-sweep-rivs-preflight.csv.

source("verification/00-setup.R")

cat("\n== Pre-flight tr(RIV) table ==\n\n")

Sigma_truth <- w3_sigma(rho = 0.4)
theta_truth <- list(mu = default_mu, Sigma = Sigma_truth)

n_seeds <- 50
prop    <- 0.40
Ns      <- c(200, 500, 1000)
mechs   <- c("MAR", "MNAR")
patts   <- c("non_monotone", "monotone")
models  <- c("MA", "MB", "MC", "MD")

rows <- list()
t0 <- Sys.time()

for (pat in patts) for (mech in mechs) for (N in Ns) {
  trRIV_mat <- matrix(NA_real_, nrow = n_seeds, ncol = length(models))
  colnames(trRIV_mat) <- models
  for (s in seq_len(n_seeds)) {
    set.seed(20260601 + s)
    X <- gen_data(N = N, mu = theta_truth$mu, Sigma = theta_truth$Sigma)
    mar <- apply_missingness_ampute(X, prop = prop, mech = mech,
                                    pattern_type = pat)
    for (k in models) {
      trRIV_mat[s, k] <- tr_riv_analytic_general(theta_truth,
                                                  mar$Y, mar$R,
                                                  W3_FREE_IDX[[k]])
    }
  }
  means <- colMeans(trRIV_mat)
  ord_idx <- order(means)
  ordering <- paste(models[ord_idx], collapse = " < ")

  row <- data.frame(
    pattern = pat, mech = mech, N = N,
    tr_MA = means["MA"], tr_MB = means["MB"],
    tr_MC = means["MC"], tr_MD = means["MD"],
    spread_MD_minus_MC = means["MD"] - means["MC"],
    spread_MD_minus_MA = means["MD"] - means["MA"],
    ordering = ordering,
    stringsAsFactors = FALSE
  )
  cat(sprintf("  %-13s %4s N=%4d   MA=%.2f  MB=%.2f  MC=%.2f  MD=%.2f   D-C=%.2f   order: %s\n",
              pat, mech, N, means["MA"], means["MB"], means["MC"],
              means["MD"], means["MD"] - means["MC"], ordering))
  rows[[length(rows) + 1]] <- row
}

elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("\nElapsed: %.1fs (%d cells x %d seeds)\n",
            elapsed, length(rows), n_seeds))

df <- do.call(rbind, rows)
out_path <- "verification/cache/W3-sweep-rivs-preflight.csv"
if (!dir.exists("verification/cache")) {
  dir.create("verification/cache", recursive = TRUE)
}
write.csv(df, file = out_path, row.names = FALSE)
cat(sprintf("\nCSV written: %s\n", out_path))

# -----------------------------------------------------------------------------
# H1 anchor: does monotone show larger spread (M_D - M_C) than non_monotone?
# Larger spread => larger differential bias => larger W3-A.
# -----------------------------------------------------------------------------
cat("\n-- H1 anchor --\n")
agg <- aggregate(spread_MD_minus_MC ~ pattern, data = df, FUN = mean)
cat("Mean(tr_MD - tr_MC) across cells:\n")
for (i in seq_len(nrow(agg))) {
  cat(sprintf("  %-13s : %+.3f\n", agg$pattern[i], agg$spread_MD_minus_MC[i]))
}
if (agg$spread_MD_minus_MC[agg$pattern == "monotone"] >
    agg$spread_MD_minus_MC[agg$pattern == "non_monotone"]) {
  cat("=> Monotone shows LARGER M_D - M_C spread.\n",
      "   H1 directional anchor favorable.\n", sep = "")
} else {
  cat("=> Monotone shows SMALLER M_D - M_C spread than non-monotone.\n",
      "   H1's prediction (larger W3-A under monotone) is at risk.\n", sep = "")
}
