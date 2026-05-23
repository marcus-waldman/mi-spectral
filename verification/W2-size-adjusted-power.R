# W2-size-adjusted-power.R
#
# Size-adjusted power comparison for the W2 pilot caches. For each test
# (C2 Chan-corrected, C3 Chan-uncorrected, C5 SB; C1 oracle for reference),
# compute the empirical critical p-value c* from the delta=0 distribution
# such that P(p <= c* | H_0) = 0.05 exactly. Then evaluate power at delta>0
# using that empirically calibrated critical value.
#
# This isolates the power of each test from its size miscalibration.

cache_dir <- "verification/cache"

extract_pvals <- function(rds_path) {
  z <- readRDS(rds_path)
  deltas <- as.numeric(names(z$all_results))
  out <- list()
  for (d in deltas) {
    res <- z$all_results[[as.character(d)]]
    out[[as.character(d)]] <- list(
      p_oracle      = vapply(res, `[[`, numeric(1), "p_oracle"),
      p_corrected   = vapply(res, `[[`, numeric(1), "p_corrected"),
      p_uncorrected = vapply(res, `[[`, numeric(1), "p_uncorrected"),
      p_sb          = vapply(res, `[[`, numeric(1), "p_sb")
    )
  }
  return(list(deltas = deltas, pvals = out, engine = z$engine,
              cfg = z$cfg))
}

size_adjust <- function(pvals_by_delta, alpha = 0.05) {
  configs <- c("p_oracle", "p_corrected", "p_uncorrected", "p_sb")
  # Empirical critical p-values from delta = 0.
  p0 <- pvals_by_delta[["0"]]
  crit <- sapply(configs, function(cf) {
    quantile(p0[[cf]], probs = alpha, na.rm = TRUE, names = FALSE)
  })
  deltas <- as.numeric(names(pvals_by_delta))
  tab_raw  <- matrix(NA, length(deltas), length(configs),
                     dimnames = list(deltas, configs))
  tab_size <- matrix(NA, length(deltas), length(configs),
                     dimnames = list(deltas, configs))
  for (i in seq_along(deltas)) {
    d <- as.character(deltas[i])
    for (cf in configs) {
      tab_raw[i, cf]  <- mean(pvals_by_delta[[d]][[cf]] < alpha,        na.rm = TRUE)
      tab_size[i, cf] <- mean(pvals_by_delta[[d]][[cf]] <= crit[[cf]],  na.rm = TRUE)
    }
  }
  return(list(raw = tab_raw, size_adjusted = tab_size, crit = crit))
}

format_table <- function(tab, title) {
  cat(sprintf("\n%s\n", title))
  cat(sprintf("%-7s  %-9s  %-12s  %-15s  %-7s\n",
              "delta", "C1 oracle", "C2 corrected", "C3 uncorrected", "C5 SB"))
  for (i in seq_len(nrow(tab))) {
    cat(sprintf("%-7s  %9.3f  %12.3f  %15.3f  %7.3f\n",
                rownames(tab)[i],
                tab[i, "p_oracle"], tab[i, "p_corrected"],
                tab[i, "p_uncorrected"], tab[i, "p_sb"]))
  }
}

for (engine in c("fiml", "amelia")) {
  path <- file.path(cache_dir, sprintf("W2-pilot-%s.rds", engine))
  if (!file.exists(path)) next
  cat(sprintf("\n========================================================\n"))
  cat(sprintf(" %s pilot (path: %s)\n", toupper(engine), path))
  cat(sprintf("========================================================\n"))
  px <- extract_pvals(path)
  sa <- size_adjust(px$pvals, alpha = 0.05)
  cat(sprintf("\nEmpirical critical p-values at delta=0 (alpha=0.05):\n"))
  print(round(sa$crit, 4))
  format_table(sa$raw,           "Raw rejection rates at nominal alpha=0.05")
  format_table(sa$size_adjusted, "SIZE-ADJUSTED power (each test using its own empirical c*)")
}
