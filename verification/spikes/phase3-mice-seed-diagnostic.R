# spikes/phase3-mice-seed-diagnostic.R  (todo/045 Q2, 2026-07-04)
#
# Diagnostic: why does the ORIGINAL phase-3 mice draw arm
# (phase3-nonnormal-illustration.R, cache phase3-nonnormal-prod.rds) give
# diff-ratio -0.223 at N=200 while the new per-rep-seed scan
# (phase3-family-scan.R bern_draw) gives -0.383 on the same design?
#
# Three arms, same data seeds (BASE 20260703 + r, the ORIGINAL script's stream,
# so arm (a) is an exact-mechanism replica of the original):
#   (a) fixed1: mice seed = 1 for EVERY rep (the original script's usage)
#   (b) perrep: mice seed = r (fresh per rep; the new scan's usage)
#   (c) bypass: mice bypassed -- own draws beta* ~ N(beta_hat_obs, V_glm),
#       fresh z per imputation, analytic p-average (Rao-Blackwellized)
#
# Result (2026-07-04, R=500):
#   fixed1: -0.2410 (se 0.0314)  -- reproduces the original -0.2232 (se 0.0216)
#   perrep: -0.2968 (se 0.0308)  -- freeing the mice seed moves the value
#   bypass: -0.2769 (se 0.0158)  -- textbook draws sit 1.0 se from the derived
#                                   asymptote -0.2606; mice internals are not
#                                   the anomaly
# Attribution: the original script called mice(..., seed = 1) on EVERY
# repetition, so all 1000 repetitions shared one 50-draw z-set; its quoted se
# treated those draws as independent across repetitions, which they were not.
#
# Usage: Rscript verification/spikes/phase3-mice-seed-diagnostic.R

suppressPackageStartupMessages(library(mice))
suppressPackageStartupMessages(library(parallel))

N <- 200
M <- 50
R <- 500
MISS_RATE <- 0.22
BETA0 <- c(0.3, 0.9)
BASE_SEED <- 20260703   # the ORIGINAL phase-3 stream

sim_bern <- function(seed) {
  set.seed(seed)
  X <- rnorm(N)
  p <- plogis(BETA0[1] + BETA0[2] * X)
  Y <- rbinom(N, 1, p)
  miss <- runif(N) < MISS_RATE
  return(list(X = X, Y = Y, miss = miss))
}

fit_logit <- function(Y, X) {
  f <- suppressWarnings(glm.fit(cbind(1, X), Y, family = binomial()))
  return(unname(f$coefficients))
}

diff_one <- function(r, mice_seed_mode) {
  cell <- sim_bern(BASE_SEED + r)
  if (length(unique(cell$Y[!cell$miss])) < 2 || sum(cell$miss) < 2) { return(NA) }
  beta_obs <- fit_logit(cell$Y[!cell$miss], cell$X[!cell$miss])
  eta <- beta_obs[1] + beta_obs[2] * cell$X
  p_hat <- plogis(eta)
  mis <- which(cell$miss)
  if (mice_seed_mode == "bypass") {
    fo <- suppressWarnings(glm(cell$Y[!cell$miss] ~ cell$X[!cell$miss], family = binomial()))
    V <- unname(vcov(fo))
    ch <- chol(V)
    set.seed(BASE_SEED + 7e6 + r)
    zbar_mis <- rowMeans(vapply(seq_len(M), function(m) {
      bstar <- beta_obs + drop(t(ch) %*% rnorm(2))
      return(plogis(bstar[1] + bstar[2] * cell$X[mis]))
    }, numeric(length(mis))))
    # E over imputation draws done analytically per beta*: Z_i ~ Bern(p(beta*)),
    # E[Zbar_i] = mean_m p(beta*_m); using p directly removes binomial noise
    return(sum((zbar_mis - p_hat[mis]) * eta[mis]))
  }
  Y_na <- cell$Y
  Y_na[cell$miss] <- NA
  df <- data.frame(Y = factor(Y_na), X = cell$X)
  sd_use <- if (mice_seed_mode == "fixed1") { 1 } else { r }
  imp <- mice::mice(df, method = c("logreg", ""), m = M, printFlag = FALSE, seed = sd_use)
  zbar <- rowMeans(vapply(seq_len(M), function(m) {
    return(as.numeric(as.character(mice::complete(imp, m)$Y))[mis])
  }, numeric(length(mis))))
  return(sum((zbar - p_hat[mis]) * eta[mis]))
}

cl <- makeCluster(16)
clusterExport(cl, c("diff_one", "sim_bern", "fit_logit", "N", "M", "MISS_RATE",
                    "BETA0", "BASE_SEED"))
invisible(clusterEvalQ(cl, suppressPackageStartupMessages(library(mice))))
for (mode in c("fixed1", "perrep", "bypass")) {
  v <- unlist(parLapply(cl, seq_len(R), function(r, m) { return(diff_one(r, m)) }, m = mode))
  v <- v[!is.na(v)]
  tr <- 2 * MISS_RATE / (1 - MISS_RATE)
  cat(sprintf("%-7s: R=%d  mean diff=%+.4f (se %.4f)  diff-ratio=%+.4f (se %.4f)\n",
              mode, length(v), mean(v), sd(v) / sqrt(length(v)),
              mean(v) / tr, sd(v) / sqrt(length(v)) / tr))
}
stopCluster(cl)
