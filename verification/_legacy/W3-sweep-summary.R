# W3-sweep-summary.R
#
# Aggregate the comprehensive W3 sweep outputs (60 main cells + 6 H3b rate
# cells) and the W1 sweep into per-factor margins, then evaluate the
# pre-registered hypotheses H1, H2-MAR, H2-MNAR, H3, H3b, H4, H5, H6 from
# todo/005 against their pass criteria.
#
# Inputs (default suffixes can be overridden via CLI args):
#   verification/cache/W3-sweep-prod/summary.csv
#   verification/cache/W3-sweep-rate-prod/summary.csv
#   verification/cache/W1-sweep-prod/summary.csv
#
# Output:
#   verification/cache/W3-sweep-summary.csv (combined tidy frame)
#   stdout: per-factor margins + hypothesis verdicts

args   <- commandArgs(trailingOnly = TRUE)
suffix <- if (length(args) >= 1) { args[1] } else { "prod" }

main_path  <- sprintf("verification/cache/W3-sweep-%s/summary.csv", suffix)
rate_path  <- sprintf("verification/cache/W3-sweep-rate-%s/summary.csv", suffix)
w1_path    <- sprintf("verification/cache/W1-sweep-%s/summary.csv", suffix)

cat("\n== W3 sweep summary ==\n")
cat(sprintf("  main : %s\n  rate : %s\n  W1   : %s\n",
            main_path, rate_path, w1_path))
if (!file.exists(main_path)) { stop("main summary CSV not found") }

main_df <- read.csv(main_path, stringsAsFactors = FALSE)
rate_df <- if (file.exists(rate_path)) {
  read.csv(rate_path, stringsAsFactors = FALSE)
} else {
  cat("  (rate sweep not found — H3b will be skipped)\n")
  NULL
}
w1_df <- if (file.exists(w1_path)) {
  read.csv(w1_path, stringsAsFactors = FALSE)
} else {
  cat("  (W1 sweep not found — W1 marginal table will be skipped)\n")
  NULL
}

cat(sprintf("\nMain sweep: %d cells\n", nrow(main_df)))
cat(sprintf("Rate sweep: %s cells\n",
            if (is.null(rate_df)) "N/A" else as.character(nrow(rate_df))))

if (!"W3A_corr_minus_uncorr" %in% names(main_df)) {
  main_df$W3A_corr_minus_uncorr <- main_df$pi_corrected - main_df$pi_uncorrected
}
if (!"W3B_oracle_minus_corr" %in% names(main_df)) {
  main_df$W3B_oracle_minus_corr <- main_df$pi_oracle - main_df$pi_corrected
}

main_df$cong <- ifelse(main_df$engine == "fiml", "fiml",
                ifelse(main_df$empri_frac == 0, "cong", "uncong"))


# -----------------------------------------------------------------------------
# Margin tables.
# -----------------------------------------------------------------------------

cat("\n-- Per-factor margins (mean W3-A across cells with that factor level) --\n")

cong_subset <- main_df[main_df$engine == "fiml" | main_df$cong == "cong", ]

fmt_agg <- function(df) {
  # Round only the numeric column(s); leave grouping columns as-is.
  for (j in seq_along(df)) {
    if (is.numeric(df[[j]])) df[[j]] <- round(df[[j]], 4)
  }
  return(df)
}
for (fac in c("pattern", "mech", "N", "engine")) {
  cat(sprintf("\n%s (congenial + FIML cells only):\n", fac))
  ag <- aggregate(cong_subset$W3A_corr_minus_uncorr,
                  by = list(level = cong_subset[[fac]]),
                  FUN = mean)
  names(ag)[2] <- "mean_W3A"
  print(fmt_agg(ag), row.names = FALSE)
}
cat("\nM (Amelia congenial only):\n")
amelia_cong <- main_df[main_df$engine == "amelia" & main_df$cong == "cong", ]
ag <- aggregate(amelia_cong$W3A_corr_minus_uncorr,
                by = list(M = amelia_cong$M), FUN = mean)
names(ag)[2] <- "mean_W3A"
print(fmt_agg(ag), row.names = FALSE)

cat("\nCongeniality (Amelia only):\n")
amelia_only <- main_df[main_df$engine == "amelia", ]
ag <- aggregate(amelia_only$W3A_corr_minus_uncorr,
                by = list(cong = amelia_only$cong), FUN = mean)
names(ag)[2] <- "mean_W3A"
print(fmt_agg(ag), row.names = FALSE)


# -----------------------------------------------------------------------------
# Hypothesis evaluation.
# -----------------------------------------------------------------------------

cat("\n\n== Hypothesis verdicts ==\n\n")
verdicts <- list()

# ---- H1 (Pattern effect: monotone > non_monotone W3-A) ----
agg_pat <- aggregate(W3A_corr_minus_uncorr ~ pattern, data = cong_subset, FUN = median)
W3A_monotone     <- agg_pat$W3A_corr_minus_uncorr[agg_pat$pattern == "monotone"]
W3A_non_monotone <- agg_pat$W3A_corr_minus_uncorr[agg_pat$pattern == "non_monotone"]
H1_pass <- W3A_monotone >= W3A_non_monotone + 0.05
cat(sprintf("H1 (monotone > non_monotone W3-A by >= 0.05): %s\n",
            if (H1_pass) "PASS" else "FAIL"))
cat(sprintf("    median W3-A monotone     = %+.4f\n", W3A_monotone))
cat(sprintf("    median W3-A non_monotone = %+.4f\n", W3A_non_monotone))
cat(sprintf("    diff = %+.4f\n", W3A_monotone - W3A_non_monotone))
verdicts[["H1"]] <- H1_pass

# ---- H2-MAR (at all MAR + congenial cells, W3-C >= 0.80 and W3-A >= 0.05) ----
H2_mar_cells <- main_df[main_df$mech == "MAR" &
                        (main_df$engine == "fiml" | main_df$cong == "cong"), ]
H2_mar_W3C <- all(H2_mar_cells$W3C_high_RIV_frac >= 0.80, na.rm = TRUE)
H2_mar_W3A <- all(H2_mar_cells$W3A_corr_minus_uncorr >= 0.05, na.rm = TRUE)
H2_mar_pass <- H2_mar_W3C && H2_mar_W3A
cat(sprintf("\nH2-MAR (all MAR+cong cells: W3-C>=0.80 AND W3-A>=0.05): %s\n",
            if (H2_mar_pass) "PASS" else "FAIL"))
cat(sprintf("    min W3-C = %.3f (need >= 0.80)\n",
            min(H2_mar_cells$W3C_high_RIV_frac, na.rm = TRUE)))
cat(sprintf("    min W3-A = %.3f (need >= 0.05)\n",
            min(H2_mar_cells$W3A_corr_minus_uncorr, na.rm = TRUE)))
verdicts[["H2-MAR"]] <- H2_mar_pass

# ---- H2-MNAR (observational only) ----
H2_mnar_cells <- main_df[main_df$mech == "MNAR" &
                         (main_df$engine == "fiml" | main_df$cong == "cong"), ]
cat(sprintf("\nH2-MNAR (observational):\n"))
cat(sprintf("    range W3-A across MNAR+cong: [%+.3f, %+.3f] (median %+.3f)\n",
            min(H2_mnar_cells$W3A_corr_minus_uncorr, na.rm = TRUE),
            max(H2_mnar_cells$W3A_corr_minus_uncorr, na.rm = TRUE),
            median(H2_mnar_cells$W3A_corr_minus_uncorr, na.rm = TRUE)))
cat(sprintf("    range W3-C across MNAR+cong: [%.3f, %.3f] (median %.3f)\n",
            min(H2_mnar_cells$W3C_high_RIV_frac, na.rm = TRUE),
            max(H2_mnar_cells$W3C_high_RIV_frac, na.rm = TRUE),
            median(H2_mnar_cells$W3C_high_RIV_frac, na.rm = TRUE)))
verdicts[["H2-MNAR"]] <- "observational"

# ---- H3 (N effects) ----
# (a) W3-B at N=1000 < W3-B at N=200
H3_cells <- main_df[main_df$mech == "MAR" &
                    (main_df$engine == "fiml" | main_df$cong == "cong"), ]
W3B_byN <- aggregate(W3B_oracle_minus_corr ~ N, data = H3_cells, FUN = median)
W3A_byN <- aggregate(W3A_corr_minus_uncorr ~ N, data = H3_cells, FUN = median)
W3C_byN <- aggregate(W3C_high_RIV_frac    ~ N, data = H3_cells, FUN = min)
W3B_shrinks <- W3B_byN$W3B_oracle_minus_corr[W3B_byN$N == 1000] <
               W3B_byN$W3B_oracle_minus_corr[W3B_byN$N == 200]
W3A_diff_max <- max(W3A_byN$W3A_corr_minus_uncorr) - min(W3A_byN$W3A_corr_minus_uncorr)
W3A_invariant <- W3A_diff_max <= 0.05
W3C_all_high <- all(W3C_byN$W3C_high_RIV_frac >= 0.80, na.rm = TRUE)
H3_pass <- W3B_shrinks && W3A_invariant && W3C_all_high
cat(sprintf("\nH3 (W3-B shrinks; W3-A N-invariant; W3-C >= 0.80 all N): %s\n",
            if (H3_pass) "PASS" else "FAIL"))
cat(sprintf("    W3-B by N (median): %s\n",
            paste(sprintf("N=%d:%.3f", W3B_byN$N, W3B_byN$W3B_oracle_minus_corr),
                  collapse = " ")))
cat(sprintf("    W3-A by N (median): %s   (max - min = %.3f)\n",
            paste(sprintf("N=%d:%.3f", W3A_byN$N, W3A_byN$W3A_corr_minus_uncorr),
                  collapse = " "),
            W3A_diff_max))
cat(sprintf("    W3-C by N (min)    : %s\n",
            paste(sprintf("N=%d:%.3f", W3C_byN$N, W3C_byN$W3C_high_RIV_frac),
                  collapse = " ")))
verdicts[["H3"]] <- H3_pass

# ---- H3b (rate scaling) ----
if (!is.null(rate_df)) {
  # Add prop=0.40 from main MAR+non_monotone+M200+cong cells.
  base_40 <- main_df[main_df$pattern == "non_monotone" &
                     main_df$mech == "MAR" &
                     main_df$engine == "amelia" &
                     main_df$M == 200 &
                     main_df$cong == "cong", ]
  base_40$W3A <- base_40$W3A_corr_minus_uncorr
  base_40$prop <- 0.40
  base_40_min <- base_40[, c("N", "prop", "W3A", "pi_oracle",
                             "pi_uncorrected", "pi_corrected")]
  rate_min <- rate_df[, c("N", "prop", "W3A", "pi_oracle",
                          "pi_uncorrected", "pi_corrected")]
  rate_combined <- rbind(rate_min, base_40_min)
  rate_combined <- rate_combined[order(rate_combined$N, rate_combined$prop), ]

  # Monotone in rate within each N.
  monotone_in_rate <- all(sapply(unique(rate_combined$N), function(N) {
    sub <- rate_combined[rate_combined$N == N, ]
    sub <- sub[order(sub$prop), ]
    return(all(diff(sub$W3A) >= 0))
  }))

  # Rate-doubling ratio: W3A(higher) / W3A(lower) at each N. With the
  # H3b scope cut (rate=60% deferred — see todo/005 version history), we
  # have rates {0.20, 0.40}. Doubling rate predicts ratio approximately 2.
  available_rates <- sort(unique(rate_combined$prop))
  ratio_by_N <- sapply(unique(rate_combined$N), function(N) {
    sub <- rate_combined[rate_combined$N == N, ]
    if (length(available_rates) < 2) return(NA)
    rmin <- min(available_rates); rmax <- max(available_rates)
    wlo <- sub$W3A[sub$prop == rmin]
    whi <- sub$W3A[sub$prop == rmax]
    if (length(wlo) == 0 || length(whi) == 0 || abs(wlo) < 1e-3) return(NA)
    return(whi / wlo)
  })
  ratio_avg <- mean(ratio_by_N, na.rm = TRUE)
  # Target ratio = max_rate / min_rate (under linear scaling).
  target_ratio <- if (length(available_rates) >= 2) {
    max(available_rates) / min(available_rates)
  } else {
    NA_real_
  }
  ratio_linear <- !is.na(ratio_avg) && !is.na(target_ratio) &&
                  abs(ratio_avg - target_ratio) <= 1.0

  agg_W3A <- aggregate(W3A ~ N + prop, data = rate_combined, FUN = mean)
  N_inv_by_prop <- sapply(unique(agg_W3A$prop), function(p) {
    sub <- agg_W3A[agg_W3A$prop == p, ]
    return(max(sub$W3A) - min(sub$W3A))
  })
  N_invariant <- all(N_inv_by_prop <= 0.06, na.rm = TRUE)

  H3b_status <- if (!(0.60 %in% available_rates)) {
    # Partial H3b (rate=60% deferred). Downgrade to observational; report
    # what we have.
    "observational (partial — rate=60% deferred)"
  } else {
    if (isTRUE(monotone_in_rate) && isTRUE(ratio_linear) && isTRUE(N_invariant)) {
      "PASS"
    } else {
      "FAIL"
    }
  }
  cat(sprintf("\nH3b: %s\n", H3b_status))
  cat("    rate combined table:\n")
  print(rate_combined, row.names = FALSE, digits = 3)
  cat(sprintf("    monotone in rate    : %s\n", if (isTRUE(monotone_in_rate)) "PASS" else "FAIL"))
  cat(sprintf("    rate ratio W3A(max=%.0f%%) / W3A(min=%.0f%%) mean = %.2f (target approx %.2f under linear scaling)\n",
              100 * max(available_rates), 100 * min(available_rates),
              ratio_avg, target_ratio))
  cat(sprintf("    N-invariance (max diff per rate): %s\n",
              paste(sprintf("%.0f%%:%.3f", 100 * unique(agg_W3A$prop), N_inv_by_prop),
                    collapse = " ")))
  verdicts[["H3b"]] <- H3b_status
} else {
  verdicts[["H3b"]] <- "skipped"
}

# ---- H4 (M sensitivity at MAR+congenial: W3-A at M=200 >= W3-A at M=20 - 0.02) ----
H4_cells <- main_df[main_df$mech == "MAR" & main_df$engine == "amelia" &
                    main_df$cong == "cong", ]
H4_pass <- TRUE
for (pat in unique(H4_cells$pattern)) {
  for (N in unique(H4_cells$N)) {
    sub <- H4_cells[H4_cells$pattern == pat & H4_cells$N == N, ]
    if (nrow(sub) < 2) next
    w200 <- sub$W3A_corr_minus_uncorr[sub$M == 200]
    w20  <- sub$W3A_corr_minus_uncorr[sub$M == 20]
    if (length(w200) == 0 || length(w20) == 0) next
    if (w200 < w20 - 0.02) {
      H4_pass <- FALSE
      cat(sprintf("    H4 violation at pattern=%s N=%d: W3A(M=200)=%.3f, W3A(M=20)=%.3f\n",
                  pat, N, w200, w20))
    }
  }
}
cat(sprintf("\nH4 (MAR+cong: W3-A(M=200) >= W3-A(M=20) - 0.02 at every cell): %s\n",
            if (H4_pass) "PASS" else "FAIL"))
verdicts[["H4"]] <- H4_pass

# ---- H5 (Congeniality) — observational, but report ----
H5_cong <- main_df[main_df$engine == "amelia" & main_df$cong == "cong" &
                   main_df$mech == "MAR", ]
H5_uncong <- main_df[main_df$engine == "amelia" & main_df$cong == "uncong" &
                     main_df$mech == "MAR", ]
cat(sprintf("\nH5 (Congeniality, observational):\n"))
cat(sprintf("    median W3-A congenial = %+.3f\n",
            median(H5_cong$W3A_corr_minus_uncorr, na.rm = TRUE)))
cat(sprintf("    median W3-A uncongenial = %+.3f\n",
            median(H5_uncong$W3A_corr_minus_uncorr, na.rm = TRUE)))
cat(sprintf("    median W3-C congenial = %.3f\n",
            median(H5_cong$W3C_high_RIV_frac, na.rm = TRUE)))
cat(sprintf("    median W3-C uncongenial = %.3f\n",
            median(H5_uncong$W3C_high_RIV_frac, na.rm = TRUE)))
verdicts[["H5"]] <- "observational"

# ---- H6 (FIML vs Amelia congenial M=200 agree within 3 pp) ----
H6_pass <- TRUE
for (pat in c("non_monotone", "monotone")) {
  for (mech in c("MAR", "MNAR")) {
    for (N in c(200, 500, 1000)) {
      f <- main_df[main_df$engine == "fiml" & main_df$pattern == pat &
                   main_df$mech == mech & main_df$N == N, ]
      a <- main_df[main_df$engine == "amelia" & main_df$cong == "cong" &
                   main_df$M == 200 & main_df$pattern == pat &
                   main_df$mech == mech & main_df$N == N, ]
      if (nrow(f) == 0 || nrow(a) == 0) next
      gap <- abs(f$W3A_corr_minus_uncorr - a$W3A_corr_minus_uncorr)
      if (gap > 0.03) {
        H6_pass <- FALSE
        cat(sprintf("    H6 violation at pattern=%s mech=%s N=%d: |fiml-amelia| W3A = %.3f\n",
                    pat, mech, N, gap))
      }
    }
  }
}
cat(sprintf("\nH6 (FIML vs Amelia cong M=200 agree within 0.03 pp): %s\n",
            if (H6_pass) "PASS" else "FAIL"))
verdicts[["H6"]] <- H6_pass


# -----------------------------------------------------------------------------
# Save combined tidy summary.
# -----------------------------------------------------------------------------

out_path <- "verification/cache/W3-sweep-summary.csv"
main_df$cell_class <- "main"
if (!is.null(rate_df)) {
  rate_df$cell_class <- "rate_h3b"
  rate_df$cong <- "cong"
  rate_df$engine <- "amelia"
  rate_df$W3A_corr_minus_uncorr <- rate_df$W3A
  rate_df$W3B_oracle_minus_corr <- rate_df$W3B
  rate_df$W3C_high_RIV_frac <- rate_df$W3C
}
if (!is.null(rate_df)) {
  common_cols <- intersect(names(main_df), names(rate_df))
  combined <- rbind(main_df[, common_cols], rate_df[, common_cols])
} else {
  combined <- main_df
}
write.csv(combined, file = out_path, row.names = FALSE)
cat(sprintf("\nCombined summary: %s\n", out_path))


# -----------------------------------------------------------------------------
# Verdict table.
# -----------------------------------------------------------------------------

cat("\n\n== Final verdicts ==\n")
for (h in names(verdicts)) {
  v <- verdicts[[h]]
  if (isTRUE(v)) {
    cat(sprintf("  %-8s : PASS\n", h))
  } else if (identical(v, FALSE)) {
    cat(sprintf("  %-8s : FAIL\n", h))
  } else {
    cat(sprintf("  %-8s : %s\n", h, v))
  }
}

n_pass <- sum(sapply(verdicts, isTRUE))
n_fail <- sum(sapply(verdicts, function(v) identical(v, FALSE)))
cat(sprintf("\nQuantitative hypotheses: %d pass, %d fail, %d observational/skipped\n",
            n_pass, n_fail, length(verdicts) - n_pass - n_fail))
