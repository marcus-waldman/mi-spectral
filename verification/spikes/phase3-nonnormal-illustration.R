# spikes/phase3-nonnormal-illustration.R
#
# Phase 3 (todo/040-v1-review-response-registration.md §9, reviewer r3#2): a
# non-normal empirical illustration of the two-regime known-scale/estimated-scale
# prediction already given by the theorem's scope callout (derivation.qmd
# :792-827), extended here to two genuinely non-MVN likelihoods. This is NOT a
# re-derivation of the exact closed-form engine-gap D for a Gamma shape parameter
# (that formula is MVN-Wishart-specific and out of scope for a modest
# illustration) -- the Gamma/brms branch is a directional check only; the
# Bernoulli/mice branch is scored against the already-derived, already-MC-verified
# known-scale collapse identity.
#
# Two families, two engines each (a deterministic FIML-analytic anchor + a genuine
# posterior-draw engine), N=200, MCAR missingness on Y only (X fully observed,
# each row's Y conditionally independent given X -- so the FIML-analytic anchor is
# a closed form: observed rows contribute their actual log-density, missing rows
# contribute the MODEL'S OWN differential entropy at that row's fitted mean,
# i.e. E_{Y~f(.|X,theta)}[log f(Y|X,theta)], validated against brute-force MC
# to 1e-4 before use -- see the registration doc):
#   Gamma (estimated-scale):  FITTED = analytic FIML anchor (Gamma differential
#                             entropy); draw = brms (weakly-informative default
#                             priors, posterior-predictive completions)
#   Bernoulli (scale-free):   FITTED = analytic FIML anchor (binary entropy);
#                             draw    = mice(method = "logreg")
#
# Both branches are normalized by the SAME sample tr(RIV) (Rubin's rule via the
# genuine-draw engine's M completions, refit per completion) -- mirrors
# verification/spikes/phase0b-brms-imputer.R's (Tb - T_fiml)/trRIV construction.
#
# Usage:
#   Rscript verification/spikes/phase3-nonnormal-illustration.R [R] [M] [out_suffix]

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(brms)
  library(mice)
  library(MASS)
})

args <- commandArgs(trailingOnly = TRUE)
R <- if (length(args) >= 1) as.integer(args[1]) else 200
M <- if (length(args) >= 2) as.integer(args[2]) else 50
out_suffix <- if (length(args) >= 3) args[3] else "prod"

N <- 200
MISS_RATE <- 0.22
BASE_SEED <- 20260703

options(mc.cores = 2)
cat(sprintf("\nPhase-3 non-normal illustration  [R=%d, M=%d, N=%d, out=%s]\n", R, M, N, out_suffix))


# -----------------------------------------------------------------------------
# Gamma family (estimated-scale exemplar)
# -----------------------------------------------------------------------------

sim_gamma <- function(seed) {
  set.seed(seed)
  X <- rnorm(N)
  mu <- exp(0.5 + 0.8 * X)
  Y <- rgamma(N, shape = 4, rate = 4 / mu)
  miss <- runif(N) < MISS_RATE
  Y_obs <- Y
  Y_obs[miss] <- NA
  return(list(X = X, Y_full = Y, Y_obs = Y_obs, miss = miss))
}

loglik_gamma <- function(beta, shape, Y, X) {
  mu <- exp(beta[1] + beta[2] * X)
  return(sum(dgamma(Y, shape = shape, rate = shape / mu, log = TRUE)))
}

mle_gamma <- function(Y, X) {
  fit <- glm(Y ~ X, data = data.frame(Y = Y, X = X), family = Gamma(link = "log"))
  shape_fit <- MASS::gamma.shape(fit)
  beta <- unname(coef(fit))
  shape <- unname(shape_fit$alpha)
  U <- matrix(0, 3, 3)
  U[1:2, 1:2] <- vcov(fit)
  U[3, 3] <- unname(shape_fit$SE)^2
  return(list(beta = beta, shape = shape, theta_vec = c(beta, shape), U = U))
}

# Analytic FIML anchor: observed rows contribute their actual log-density;
# missing rows contribute the Gamma differential entropy at that row's fitted
# mean (validated against brute-force MC to 1e-4, see the registration doc).
ell_fiml_gamma <- function(theta, cell) {
  mu <- exp(theta$beta[1] + theta$beta[2] * cell$X)
  shape <- theta$shape
  scale <- mu / shape
  ll <- numeric(N)
  obs_idx <- which(!cell$miss)
  ll[obs_idx] <- dgamma(cell$Y_full[obs_idx], shape = shape, rate = shape / mu[obs_idx], log = TRUE)
  mis_idx <- which(cell$miss)
  ll[mis_idx] <- -(shape + log(scale[mis_idx]) + lgamma(shape) + (1 - shape) * digamma(shape))
  return(sum(ll))
}


# -----------------------------------------------------------------------------
# Bernoulli family (scale-free / known-scale exemplar)
# -----------------------------------------------------------------------------

sim_bernoulli <- function(seed) {
  set.seed(seed)
  X <- rnorm(N)
  p <- plogis(0.3 + 0.9 * X)
  Y <- rbinom(N, 1, p)
  miss <- runif(N) < MISS_RATE
  Y_obs <- Y
  Y_obs[miss] <- NA
  return(list(X = X, Y_full = Y, Y_obs = Y_obs, miss = miss))
}

loglik_bernoulli <- function(beta, Y, X) {
  p <- plogis(beta[1] + beta[2] * X)
  return(sum(dbinom(Y, size = 1, prob = p, log = TRUE)))
}

mle_bernoulli <- function(Y, X) {
  fit <- glm(Y ~ X, data = data.frame(Y = Y, X = X), family = binomial())
  beta <- unname(coef(fit))
  return(list(beta = beta, theta_vec = beta, U = vcov(fit)))
}

# Analytic FIML anchor: observed rows contribute their actual log-density;
# missing rows contribute the binary entropy at that row's fitted probability.
ell_fiml_bernoulli <- function(theta, cell) {
  p <- plogis(theta$beta[1] + theta$beta[2] * cell$X)
  ll <- numeric(N)
  obs_idx <- which(!cell$miss)
  ll[obs_idx] <- dbinom(cell$Y_full[obs_idx], size = 1, prob = p[obs_idx], log = TRUE)
  mis_idx <- which(cell$miss)
  ll[mis_idx] <- p[mis_idx] * log(p[mis_idx]) + (1 - p[mis_idx]) * log(1 - p[mis_idx])
  return(sum(ll))
}


# -----------------------------------------------------------------------------
# brms posterior-draw imputer (Gamma only -- brms's mi() addition term hard-
# refuses discrete families; confirmed 2026-07-03, see the registration doc).
# -----------------------------------------------------------------------------

brms_impute_gamma <- function(cell, M) {
  df <- data.frame(Y = cell$Y_obs, X = cell$X)
  fit <- brm(bf(Y | mi() ~ X), data = df, family = Gamma(link = "log"),
             backend = "cmdstanr", chains = 2, iter = 1000, refresh = 0, silent = 2, seed = 1)
  vn <- brms::variables(fit)
  draws <- posterior::as_draws_matrix(fit)
  S <- nrow(draws)
  sel <- round(seq(1, S, length.out = M))
  mis_idx <- which(cell$miss)
  ymi_cols <- sprintf("Ymi[%d]", mis_idx)
  stopifnot(all(ymi_cols %in% vn))
  comps <- lapply(sel, function(s) {
    Z <- cell$Y_obs
    Z[mis_idx] <- as.numeric(draws[s, ymi_cols])
    return(Z)
  })
  return(comps)
}


# -----------------------------------------------------------------------------
# mice posterior-draw imputer (Bernoulli logreg -- the scale-free scored arm)
# -----------------------------------------------------------------------------

mice_impute_bernoulli <- function(cell, M) {
  df <- data.frame(Y = factor(cell$Y_obs), X = cell$X)
  imp <- mice::mice(df, method = c("logreg", ""), m = M, printFlag = FALSE, seed = 1)
  comps <- lapply(seq_len(M), function(m) {
    dc <- mice::complete(imp, action = m)
    return(as.numeric(as.character(dc$Y)))
  })
  return(comps)
}


# -----------------------------------------------------------------------------
# Per-repetition scoring. T = barL_obs - ell_com_at_com; sample tr(RIV) via
# Rubin's rule (riv_sample, reused verbatim from 00-setup.R) on the genuine-
# draw engine's M completions.
# -----------------------------------------------------------------------------

score_gamma <- function(cell, comps) {
  theta_com <- mle_gamma(cell$Y_full, cell$X)
  ell_com_at_com <- loglik_gamma(theta_com$beta, theta_com$shape, cell$Y_full, cell$X)
  obs_idx <- which(!cell$miss)
  theta_obs <- mle_gamma(cell$Y_obs[obs_idx], cell$X[obs_idx])
  barL <- mean(vapply(comps, function(Z) {
    return(loglik_gamma(theta_obs$beta, theta_obs$shape, Z, cell$X))
  }, numeric(1)))
  fits <- lapply(comps, function(Z) { return(mle_gamma(Z, cell$X)) })
  theta_imps <- lapply(fits, function(f) { return(f$theta_vec) })
  U_imps <- lapply(fits, function(f) { return(f$U) })
  riv <- riv_sample(theta_imps, U_imps)
  T_fitted <- ell_fiml_gamma(theta_obs, cell) - ell_com_at_com
  T_draw <- barL - ell_com_at_com
  return(list(trRIV = riv$tr_RIV, T_fitted = T_fitted, T_draw = T_draw,
              gap_fitted = T_fitted / riv$tr_RIV, gap_draw = T_draw / riv$tr_RIV))
}

score_bernoulli <- function(cell, comps) {
  theta_com <- mle_bernoulli(cell$Y_full, cell$X)
  ell_com_at_com <- loglik_bernoulli(theta_com$beta, cell$Y_full, cell$X)
  obs_idx <- which(!cell$miss)
  theta_obs <- mle_bernoulli(cell$Y_obs[obs_idx], cell$X[obs_idx])
  barL <- mean(vapply(comps, function(Z) {
    return(loglik_bernoulli(theta_obs$beta, Z, cell$X))
  }, numeric(1)))
  fits <- lapply(comps, function(Z) { return(mle_bernoulli(Z, cell$X)) })
  theta_imps <- lapply(fits, function(f) { return(f$theta_vec) })
  U_imps <- lapply(fits, function(f) { return(f$U) })
  riv <- riv_sample(theta_imps, U_imps)
  T_fitted <- ell_fiml_bernoulli(theta_obs, cell) - ell_com_at_com
  T_draw <- barL - ell_com_at_com
  return(list(trRIV = riv$tr_RIV, T_fitted = T_fitted, T_draw = T_draw,
              gap_fitted = T_fitted / riv$tr_RIV, gap_draw = T_draw / riv$tr_RIV))
}


# -----------------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------------

bootstrap_ratio_se <- function(num, den, B = 2000) {
  n <- length(num)
  boot <- vapply(seq_len(B), function(b) {
    idx <- sample.int(n, n, replace = TRUE)
    return(mean(num[idx]) / mean(den[idx]))
  }, numeric(1))
  return(sd(boot))
}

run_family <- function(label, sim_fn, impute_fn, score_fn) {
  cat(sprintf("\n== %s ==\n", label))
  T_fitted_v <- numeric(0)
  T_draw_v <- numeric(0)
  trRIVs <- numeric(0)
  n_fail <- 0
  for (r in seq_len(R)) {
    cell <- tryCatch(sim_fn(BASE_SEED + r), error = function(e) NULL)
    if (is.null(cell)) { n_fail <- n_fail + 1; next }
    comps <- tryCatch(impute_fn(cell, M), error = function(e) {
      cat(sprintf("  [rep %d] imputer FAILED: %s\n", r, conditionMessage(e))); return(NULL)
    })
    if (is.null(comps)) { n_fail <- n_fail + 1; next }
    sc <- tryCatch(score_fn(cell, comps), error = function(e) {
      cat(sprintf("  [rep %d] scoring FAILED: %s\n", r, conditionMessage(e))); return(NULL)
    })
    if (is.null(sc)) { n_fail <- n_fail + 1; next }
    T_fitted_v <- c(T_fitted_v, sc$T_fitted)
    T_draw_v <- c(T_draw_v, sc$T_draw)
    trRIVs <- c(trRIVs, sc$trRIV)
    if (r %% 25 == 0) { cat(sprintf("  [rep %d/%d] fitted=%+.3f draw=%+.3f trRIV=%.3f\n",
                                    r, R, sc$gap_fitted, sc$gap_draw, sc$trRIV)) }
  }
  n_ok <- length(T_fitted_v)
  # Ratio-of-means (aggregate T over reps, aggregate tr(RIV) over reps, THEN divide) is
  # the appropriate estimator here, not the mean of per-replicate ratios: tr(RIV) is a
  # noisy SAMPLE quantity (Rubin's rule over M completions, unlike the analytic
  # denominator used elsewhere in this repo), so a per-replicate ratio amplifies
  # denominator noise; the theorem's own claim is about E[T]/E[tr(RIV)], which the
  # ratio-of-means estimates directly. SE via a paired bootstrap over repetitions.
  ratio_fitted <- mean(T_fitted_v) / mean(trRIVs)
  ratio_draw <- mean(T_draw_v) / mean(trRIVs)
  se_fitted <- bootstrap_ratio_se(T_fitted_v, trRIVs)
  se_draw <- bootstrap_ratio_se(T_draw_v, trRIVs)
  cat(sprintf("\n%s: n_ok=%d n_fail=%d\n", label, n_ok, n_fail))
  cat(sprintf("  sample tr(RIV): mean=%.4f\n", mean(trRIVs)))
  cat(sprintf("  FITTED ratio-of-means (E[T]/E[trRIV]): %+.4f (bootstrap se %.4f)\n", ratio_fitted, se_fitted))
  cat(sprintf("  DRAW   ratio-of-means (E[T]/E[trRIV]): %+.4f (bootstrap se %.4f)\n", ratio_draw, se_draw))
  return(list(label = label, n_ok = n_ok, n_fail = n_fail, trRIVs = trRIVs,
              T_fitted_v = T_fitted_v, T_draw_v = T_draw_v,
              mean_fitted = ratio_fitted, se_fitted = se_fitted,
              mean_draw = ratio_draw, se_draw = se_draw))
}

res_gamma <- run_family("Gamma (estimated-scale): FITTED analytic vs brms draw",
                         sim_gamma, brms_impute_gamma, score_gamma)
res_bernoulli <- run_family("Bernoulli (scale-free): FITTED analytic vs mice logreg draw",
                             sim_bernoulli, mice_impute_bernoulli, score_bernoulli)

cat("\n== Phase-3 summary ==\n")
cat("Predicted: Gamma FITTED ~ +0.5 (scored); Gamma brms more negative than FITTED (directional only)\n")
cat("Predicted: Bernoulli FITTED ~ 0 (scored); Bernoulli mice ~ -0.5 (scored)\n\n")
cat(sprintf("Gamma     FITTED = %+.4f (se %.4f)   brms  = %+.4f (se %.4f)  [brms < fitted: %s]\n",
            res_gamma$mean_fitted, res_gamma$se_fitted, res_gamma$mean_draw, res_gamma$se_draw,
            res_gamma$mean_draw < res_gamma$mean_fitted))
cat(sprintf("Bernoulli FITTED = %+.4f (se %.4f)   mice  = %+.4f (se %.4f)\n",
            res_bernoulli$mean_fitted, res_bernoulli$se_fitted,
            res_bernoulli$mean_draw, res_bernoulli$se_draw))

dir.create("verification/cache", recursive = TRUE, showWarnings = FALSE)
saveRDS(list(res_gamma = res_gamma, res_bernoulli = res_bernoulli,
             R = R, M = M, N = N, miss_rate = MISS_RATE, base_seed = BASE_SEED),
        file = sprintf("verification/cache/phase3-nonnormal-%s.rds", out_suffix))
cat(sprintf("\nCache: verification/cache/phase3-nonnormal-%s.rds\n", out_suffix))
