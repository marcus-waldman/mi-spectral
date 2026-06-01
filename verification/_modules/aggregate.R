# _modules/aggregate.R
#
# Phase 5 of run_all.R: aggregate the per-phase summary CSVs into one
# tidy frame, evaluate the pre-registered hypotheses (H1..H6 + H3b) per
# todo/005, write a final markdown verdict report.

fmt_pct <- function(x, digits = 3) {
  return(format(round(x, digits), nsmall = digits))
}

run_aggregate <- function(out_suffix,
                          w1_dir, w3_dir, rate_dir, bias_dir,
                          out_dir, info_dir = NULL, terma_dir = NULL) {
  if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
  cat(sprintf("\n== Phase 5: Aggregate + evaluate hypotheses ==\n\n"))
  w1   <- read.csv(file.path(w1_dir,   "summary.csv"), stringsAsFactors = FALSE)
  w3   <- read.csv(file.path(w3_dir,   "summary.csv"), stringsAsFactors = FALSE)
  rate <- read.csv(file.path(rate_dir, "summary.csv"), stringsAsFactors = FALSE)
  bias <- read.csv(file.path(bias_dir, "summary.csv"), stringsAsFactors = FALSE)

  w3$cong <- ifelse(w3$engine == "fiml", "fiml",
              ifelse(w3$empri_frac == 0, "cong", "uncong"))
  cong_subset <- w3[w3$engine == "fiml" | w3$cong == "cong", ]

  cat("-- Per-factor margins (mean W3-A in congenial + FIML cells only) --\n")
  for (fac in c("pattern", "mech", "N", "engine")) {
    cat(sprintf("\n%s:\n", fac))
    ag <- aggregate(cong_subset$W3A_corr_minus_uncorr,
                    by = list(level = cong_subset[[fac]]), FUN = mean)
    names(ag)[2] <- "mean_W3A"
    ag$mean_W3A <- round(ag$mean_W3A, 4)
    print(ag, row.names = FALSE)
  }

  verdicts <- list()

  # H1: monotone vs non_monotone W3-A
  agg_pat <- aggregate(cong_subset$W3A_corr_minus_uncorr,
                       by = list(pattern = cong_subset$pattern),
                       FUN = median)
  W3A_mon <- agg_pat$x[agg_pat$pattern == "monotone"]
  W3A_non <- agg_pat$x[agg_pat$pattern == "non_monotone"]
  H1_pass <- W3A_mon >= W3A_non + 0.05
  verdicts$H1 <- list(pass = H1_pass,
                       detail = sprintf("median monotone=%+.4f, non_monotone=%+.4f, diff=%+.4f",
                                         W3A_mon, W3A_non, W3A_mon - W3A_non))

  # H2-MAR: at MAR+cong, W3-C>=0.80 AND W3-A>=0.05
  H2mar <- w3[w3$mech == "MAR" & (w3$engine == "fiml" | w3$cong == "cong"), ]
  H2_mar_pass <- all(H2mar$W3C_high_RIV_frac >= 0.80, na.rm = TRUE) &&
                 all(H2mar$W3A_corr_minus_uncorr >= 0.05, na.rm = TRUE)
  verdicts$H2_MAR <- list(pass = H2_mar_pass,
                           detail = sprintf("min W3-C=%.3f, min W3-A=%.3f",
                                             min(H2mar$W3C_high_RIV_frac, na.rm = TRUE),
                                             min(H2mar$W3A_corr_minus_uncorr, na.rm = TRUE)))

  # H2-MNAR: observational; report parameter bias for the refined claim
  H2mnar <- w3[w3$mech == "MNAR" & (w3$engine == "fiml" | w3$cong == "cong"), ]
  bias_mnar <- bias[bias$mech == "MNAR", ]
  verdicts$H2_MNAR <- list(pass = "observational",
                            detail = sprintf("W3-A range [%+.3f,%+.3f] med %+.3f; W3-C range [%.3f,%.3f]; mean param ||bias|| under MNAR=%.3f (max rel bias on sigma_24 = %+.1f%%)",
                                              min(H2mnar$W3A_corr_minus_uncorr, na.rm = TRUE),
                                              max(H2mnar$W3A_corr_minus_uncorr, na.rm = TRUE),
                                              median(H2mnar$W3A_corr_minus_uncorr, na.rm = TRUE),
                                              min(H2mnar$W3C_high_RIV_frac, na.rm = TRUE),
                                              max(H2mnar$W3C_high_RIV_frac, na.rm = TRUE),
                                              mean(bias_mnar$norm_bias, na.rm = TRUE),
                                              100 * min(bias_mnar$rel_sigma_24, na.rm = TRUE)))

  # H3
  H3 <- w3[w3$mech == "MAR" & (w3$engine == "fiml" | w3$cong == "cong"), ]
  W3B_byN <- aggregate(H3$W3B_oracle_minus_corr, by = list(N = H3$N), FUN = median)
  W3A_byN <- aggregate(H3$W3A_corr_minus_uncorr, by = list(N = H3$N), FUN = median)
  W3C_byN <- aggregate(H3$W3C_high_RIV_frac,     by = list(N = H3$N), FUN = min)
  W3B_shrinks <- W3B_byN$x[W3B_byN$N == 1000] < W3B_byN$x[W3B_byN$N == 200]
  W3A_inv <- (max(W3A_byN$x) - min(W3A_byN$x)) <= 0.05
  W3C_all <- all(W3C_byN$x >= 0.80, na.rm = TRUE)
  H3_pass <- W3B_shrinks && W3A_inv && W3C_all
  verdicts$H3 <- list(pass = H3_pass,
                       detail = sprintf("W3-B shrinks: %s (%.3f vs %.3f); W3-A inv: max-min=%.3f; W3-C all>=0.80: %s",
                                         W3B_shrinks,
                                         W3B_byN$x[W3B_byN$N == 200],
                                         W3B_byN$x[W3B_byN$N == 1000],
                                         max(W3A_byN$x) - min(W3A_byN$x),
                                         W3C_all))

  # H3b: partial (rate=60% deferred). Use 20% + 40% rate points.
  base_40 <- w3[w3$pattern == "non_monotone" & w3$mech == "MAR" &
                w3$engine == "amelia" & w3$M == 200 & w3$cong == "cong",
                c("N", "prop", "W3A_corr_minus_uncorr", "pi_oracle",
                  "pi_uncorrected", "pi_corrected")]
  names(base_40)[3] <- "W3A"
  rate_min <- rate[, c("N", "prop", "W3A", "pi_oracle",
                       "pi_uncorrected", "pi_corrected")]
  rate_combined <- rbind(rate_min, base_40)
  rate_combined <- rate_combined[order(rate_combined$N, rate_combined$prop), ]
  monotone_in_rate <- all(sapply(unique(rate_combined$N), function(N) {
    sub <- rate_combined[rate_combined$N == N, ]
    sub <- sub[order(sub$prop), ]
    return(all(diff(sub$W3A) >= 0))
  }))
  ratio_by_N <- sapply(unique(rate_combined$N), function(N) {
    sub <- rate_combined[rate_combined$N == N, ]
    w20 <- sub$W3A[sub$prop == 0.20]; w40 <- sub$W3A[sub$prop == 0.40]
    if (length(w20) == 0 || length(w40) == 0 || abs(w20) < 1e-3) return(NA)
    return(w40 / w20)
  })
  ratio_mean <- mean(ratio_by_N, na.rm = TRUE)
  verdicts$H3b <- list(
    pass = "observational (partial - rate=60% deferred)",
    detail = sprintf("monotone-in-rate: %s; mean ratio W3A(40%%)/W3A(20%%) = %.2f (linear scaling predicts 2.0)",
                      monotone_in_rate, ratio_mean))

  # H4: W3-A(M=200) >= W3-A(M=20) - 0.02
  H4 <- w3[w3$mech == "MAR" & w3$engine == "amelia" & w3$cong == "cong", ]
  H4_pass <- TRUE
  H4_max_violation <- 0
  for (pat in unique(H4$pattern)) {
    for (N in unique(H4$N)) {
      sub <- H4[H4$pattern == pat & H4$N == N, ]
      w200 <- sub$W3A_corr_minus_uncorr[sub$M == 200]
      w20  <- sub$W3A_corr_minus_uncorr[sub$M == 20]
      if (length(w200) == 0 || length(w20) == 0) next
      violation <- w20 - w200 - 0.02  # positive = violation
      if (violation > 0) {
        H4_pass <- FALSE
        H4_max_violation <- max(H4_max_violation, violation)
      }
    }
  }
  verdicts$H4 <- list(pass = H4_pass,
                       detail = if (H4_pass) {
                         "all MAR+cong cells satisfy W3-A(M=200) >= W3-A(M=20) - 0.02"
                       } else {
                         sprintf("violation: max (W3-A(M=20) - W3-A(M=200) - 0.02) = +%.3f",
                                  H4_max_violation)
                       })

  # H5: congenial vs uncongenial — observational
  H5c <- w3[w3$engine == "amelia" & w3$cong == "cong"   & w3$mech == "MAR", ]
  H5u <- w3[w3$engine == "amelia" & w3$cong == "uncong" & w3$mech == "MAR", ]
  verdicts$H5 <- list(
    pass = "observational",
    detail = sprintf("median W3-A: cong=%+.3f uncong=%+.3f; median W3-C: cong=%.3f uncong=%.3f",
                      median(H5c$W3A_corr_minus_uncorr, na.rm = TRUE),
                      median(H5u$W3A_corr_minus_uncorr, na.rm = TRUE),
                      median(H5c$W3C_high_RIV_frac, na.rm = TRUE),
                      median(H5u$W3C_high_RIV_frac, na.rm = TRUE)))

  # H6: FIML vs Amelia cong M=200 within 3pp
  H6_pass <- TRUE; max_gap <- 0
  for (pat in c("non_monotone", "monotone")) {
    for (mech in c("MAR", "MNAR")) {
      for (N in c(200, 500, 1000)) {
        f <- w3[w3$engine == "fiml"   & w3$pattern == pat & w3$mech == mech & w3$N == N, ]
        a <- w3[w3$engine == "amelia" & w3$cong == "cong" & w3$M == 200 &
                w3$pattern == pat     & w3$mech == mech   & w3$N == N, ]
        if (nrow(f) == 0 || nrow(a) == 0) next
        gap <- abs(f$W3A_corr_minus_uncorr - a$W3A_corr_minus_uncorr)
        max_gap <- max(max_gap, gap)
        if (gap > 0.03) H6_pass <- FALSE
      }
    }
  }
  verdicts$H6 <- list(pass = H6_pass,
                       detail = sprintf("max |FIML - Amelia cong M=200| W3-A gap = %.3f", max_gap))

  # INFO: phase-6 information diagnostic (exploratory; folded in if present).
  if (!is.null(info_dir) && file.exists(file.path(info_dir, "summary.csv"))) {
    info <- read.csv(file.path(info_dir, "summary.csv"), stringsAsFactors = FALSE)
    k = length(default_mu) + length(default_mu) * (length(default_mu) + 1) / 2
    verdicts$INFO <- list(
      pass = "observational (exploratory; todo/008)",
      detail = sprintf(
        "ONE RIV (observed-data): E[A]~+tr_obs (max|A-tr_obs|=%.2f), E[B]~-tr_obs/2 (max|B+tr_obs/2|=%.2f); lemmas vs observed info L1 in [%.1f,%.1f] L3 in [%.1f,%.1f] (~k=%d); info-eq tr(J O_obs^-1) in [%.1f,%.1f] (correct spec); naive RIV smaller: tr_obs-tr_exp in [%.2f,%.2f], Rubin tr_samp~tr_obs (max|tr_samp-tr_obs|=%.2f)",
        max(abs(info$A_minus_obs)), max(abs(info$B_plus_half_obs)),
        min(info$L1_trace), max(info$L1_trace), min(info$L3_trace), max(info$L3_trace), k,
        min(info$info_eq, na.rm = TRUE), max(info$info_eq, na.rm = TRUE),
        min(info$tr_obs - info$tr_exp), max(info$tr_obs - info$tr_exp),
        max(abs(info$tr_samp - info$tr_obs), na.rm = TRUE)))
  }

  # TERMA: phase-8 Term-A MAR design-imbalance (A)+(C) (exploratory; todo/008).
  if (!is.null(terma_dir) && file.exists(file.path(terma_dir, "summary.csv"))) {
    ta <- read.csv(file.path(terma_dir, "summary.csv"), stringsAsFactors = FALSE)
    s1 <- ta[ta$study == "S1", ]
    s2 <- ta[ta$study == "S2", ]
    mcar_rem       <- s1$rem_meas[abs(s1$b) < 1e-9]                 # MCAR control: ~0
    s1_closed_gap  <- max(abs(s1$rem_meas - s1$rem_ana))            # closed-form match
    riv_decomp_gap <- max(abs(s1$tr_obs - s1$riv_ana))             # RIV decomposition exact
    s2_big <- s2[s2$N == max(s2$N), ]                              # MAR O(1) at largest N
    verdicts$TERMA <- list(
      pass = "observational (exploratory; todo/008)",
      detail = sprintf(
        "MCAR control (S1 b=0) rem=%+.3f (~0); S1 closed-form max|meas-ana|=%.3f; RIV-decomp max|tr_obs-(n_mis/n_obs+trMM)|=%.3f; MAR (A)+(C) at N=%d: %s",
        if (length(mcar_rem) == 1) mcar_rem else NA,
        s1_closed_gap, riv_decomp_gap, max(s2$N),
        paste(sprintf("%s=%+.3f(%.3f)", s2_big$pattern, s2_big$rem_meas, s2_big$rem_meas_mcse),
              collapse = ", ")))
  }

  # Print + persist verdicts.
  cat("\n\n-- Hypothesis verdicts --\n\n")
  for (h in names(verdicts)) {
    v <- verdicts[[h]]
    cat(sprintf("  %-10s : %s\n             %s\n",
                h,
                if (isTRUE(v$pass)) "PASS"
                else if (identical(v$pass, FALSE)) "FAIL"
                else v$pass,
                v$detail))
  }

  # Markdown report.
  md_path <- file.path(out_dir, "verdicts.md")
  md <- c(
    sprintf("# Comprehensive sweep verdicts (run_all out_suffix = %s)", out_suffix),
    "",
    sprintf("Generated %s", format(Sys.time())),
    "",
    "| Hypothesis | Verdict | Detail |",
    "|---|---|---|"
  )
  for (h in names(verdicts)) {
    v <- verdicts[[h]]
    verdict_str <- if (isTRUE(v$pass)) "PASS"
                   else if (identical(v$pass, FALSE)) "FAIL"
                   else v$pass
    md <- c(md, sprintf("| %s | %s | %s |", h, verdict_str, v$detail))
  }
  writeLines(md, md_path)
  cat(sprintf("\nMarkdown verdicts: %s\n", md_path))

  # Combined tidy frame.
  combined_path <- file.path(out_dir, "combined.csv")
  w3$cell_class   <- "w3_main"
  rate$cell_class <- "w3_rate_h3b"; rate$engine <- "amelia"
  bias$cell_class <- "mnar_bias"
  # Harmonize column names where possible.
  common_w3 <- c("cell_id", "pattern", "mech", "N", "n_ok", "n_err",
                  "pi_oracle", "pi_uncorrected", "pi_corrected", "pi_SB",
                  "cell_class")
  if (!"pi_SB" %in% names(rate)) rate$pi_SB <- NA_real_
  combined <- rbind(
    w3[, common_w3],
    rate[, intersect(common_w3, names(rate))][, common_w3[common_w3 %in% names(rate)]]
  )
  write.csv(combined, combined_path, row.names = FALSE)
  cat(sprintf("Combined tidy frame: %s\n", combined_path))

  return(verdicts)
}
