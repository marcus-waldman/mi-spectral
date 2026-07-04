# spikes/phase3-family-scan.R
#
# todo/045 Q2 (Sec.3b/3c): the pre-registered follow-up to the Phase-3
# non-normal illustration (phase3-nonnormal-illustration.R). Four arms, each
# with a target DERIVED AND DATED (todo/045 Sec.3a, 2026-07-04; CAS:
# verification/cas-wolfram/verify_bernoulli_fitted_gap.py) BEFORE this script
# first ran -- the Q1 process fix applied prospectively.
#
#   bern_fitted : Bernoulli FITTED-arm N-scan, N in {200,500,1000,2000}, big R
#                 (analytic anchor only, no imputation engine -- cheap).
#                 Registered target: ratio -> +0.5 as N grows (the canonical-GLM
#                 cancellation lemma, Delta_h = 0), with an O(1/N) residual whose
#                 constant the scan MEASURES (not derived). A flat ratio near
#                 +0.85 across N REFUTES the lemma.
#   bern_draw   : Bernoulli mice-logreg draw arm at the same N grid, R=1000,
#                 M=50, paired with FITTED per repetition. Registered target:
#                 (T_draw - T_fitted)/tr(RIV) constant in N at the quadrature
#                 value K/(2q) from the CAS script (approx -0.20; see todo/045).
#   pois_fitted : Poisson (log link, canonical) FITTED arm, N in {200,1000} --
#                 a family chosen AFTER the lemma was derived, with its target
#                 registered BEFORE any Poisson simulation existed in this repo:
#                 ratio -> 0.5 + Delta_h/tr(RIV) with Delta_h != 0 (base measure
#                 h = 1/y! is non-constant), quadrature value in todo/045.
#   t_exemplar  : Student-t location, nu=5 sigma=1 BOTH FIXED (a genuine
#                 known-scale non-normal family; smooth, so R1 holds -- the
#                 reason to prefer t over Laplace). Registered targets:
#                 FITTED -> 0, proper mu-draw -> -1/2 (derived from the paper's
#                 known-scale collapse + dH/dmu = 0 exactly, todo/045 Sec.3c).
#
# Estimator note: ratios are ratio-of-means (mean T over reps / mean tr(RIV)
# over reps), matching phase3-nonnormal-illustration.R; the FITTED arms also
# report the analytic-denominator ratio (q*r/(1-r)) and the realized-design
# denominator mean tr(J_obs^-1 J_mis) at theta_0.
#
# Usage:
#   Rscript verification/spikes/phase3-family-scan.R <arm> <out_suffix> [n_cores]
#   arm in {bern_fitted, bern_draw, pois_fitted, t_exemplar, all}
#   out_suffix "smoke" divides all R counts by 100.
#
# Outputs: verification/cache/phase3-family-scan-<arm>-<out_suffix>.rds

source("verification/00-setup.R")
suppressPackageStartupMessages({
  library(parallel)
})

args <- commandArgs(trailingOnly = TRUE)
ARM <- if (length(args) >= 1) args[1] else "all"
OUT_SUFFIX <- if (length(args) >= 2) args[2] else "prod"
N_CORES <- if (length(args) >= 3) as.integer(args[3]) else 20

BASE_SEED <- 20260704
MISS_RATE <- 0.22
SMOKE_DIV <- if (OUT_SUFFIX == "smoke") { 100 } else { 1 }

cat(sprintf("\nphase3-family-scan  [arm=%s, out=%s, cores=%d]\n", ARM, OUT_SUFFIX, N_CORES))

# -----------------------------------------------------------------------------
# shared: Bernoulli design (identical generator to phase3-nonnormal-illustration.R)
# -----------------------------------------------------------------------------

BETA0 <- c(0.3, 0.9)

sim_bern <- function(seed, N) {
  set.seed(seed)
  X <- rnorm(N)
  p <- plogis(BETA0[1] + BETA0[2] * X)
  Y <- rbinom(N, 1, p)
  miss <- runif(N) < MISS_RATE
  return(list(X = X, Y = Y, miss = miss))
}

fit_logit <- function(Y, X) {
  # glm.fit on the raw design matrix (no model.frame overhead)
  f <- suppressWarnings(glm.fit(cbind(1, X), Y, family = binomial()))
  return(unname(f$coefficients))
}

loglik_bern <- function(beta, Y, X) {
  eta <- beta[1] + beta[2] * X
  return(sum(Y * eta - log1p(exp(eta))))
}

# analytic FIML anchor at theta_obs: observed rows actual log-density, missing
# rows -H(p_hat) (exactly the M -> infinity FITTED average for any family,
# since E_{Y~f(.;theta)}[log f(Y;theta)] = -H(theta))
anchor_bern <- function(beta, Y, X, miss) {
  eta <- beta[1] + beta[2] * X
  p <- plogis(eta)
  ll_obs <- sum(Y[!miss] * eta[!miss] - log1p(exp(eta[!miss])))
  pm <- p[miss]
  Hm <- -(ifelse(pm > 0 & pm < 1, pm * log(pm) + (1 - pm) * log(1 - pm), 0))
  return(ll_obs + sum(-Hm))
}

# realized-design tr(RIV) at beta0: tr(J_obs^-1 J_mis), J = sum w x x'
trRIV_realized_bern <- function(X, miss) {
  eta <- BETA0[1] + BETA0[2] * X
  w <- plogis(eta) * (1 - plogis(eta))
  Xm <- cbind(1, X)
  J_obs <- crossprod(Xm[!miss, , drop = FALSE] * w[!miss], Xm[!miss, , drop = FALSE])
  J_mis <- crossprod(Xm[miss, , drop = FALSE] * w[miss], Xm[miss, , drop = FALSE])
  return(sum(diag(solve(J_obs, J_mis))))
}

rep_bern_fitted <- function(r, N) {
  cell <- sim_bern(BASE_SEED + r, N)
  if (sum(cell$miss) < 2 || length(unique(cell$Y[!cell$miss])) < 2) { return(NULL) }
  beta_com <- fit_logit(cell$Y, cell$X)
  beta_obs <- fit_logit(cell$Y[!cell$miss], cell$X[!cell$miss])
  T_fitted = anchor_bern(beta_obs, cell$Y, cell$X, cell$miss) -
    loglik_bern(beta_com, cell$Y, cell$X)
  return(c(T_fitted = T_fitted, trRIV = trRIV_realized_bern(cell$X, cell$miss)))
}

# -----------------------------------------------------------------------------
# arm A: bern_fitted N-scan
# -----------------------------------------------------------------------------

run_bern_fitted <- function() {
  grid <- data.frame(N = c(200, 500, 1000, 2000),
                     R = c(200000, 80000, 40000, 20000) %/% SMOKE_DIV)
  out <- list()
  for (g in seq_len(nrow(grid))) {
    N <- grid$N[g]; R <- grid$R[g]
    cl <- makeCluster(N_CORES)
    on.exit(stopCluster(cl), add = TRUE)
    clusterExport(cl, c("sim_bern", "fit_logit", "loglik_bern", "anchor_bern",
                        "trRIV_realized_bern", "rep_bern_fitted",
                        "BASE_SEED", "MISS_RATE", "BETA0"), envir = environment())
    res <- parLapply(cl, seq_len(R), function(r) {
      # per-rep seed offset by N so the four N's use disjoint streams
      tryCatch(rep_bern_fitted(r + N * 1000, N), error = function(e) NULL)
    })
    stopCluster(cl); on.exit()
    res <- do.call(rbind, Filter(Negate(is.null), res))
    trRIV_analytic = 2 * MISS_RATE / (1 - MISS_RATE)
    m = colMeans(res)
    se_T = sd(res[, "T_fitted"]) / sqrt(nrow(res))
    out[[as.character(N)]] <- list(N = N, R = nrow(res),
                                   mean_T = m[["T_fitted"]], se_T = se_T,
                                   mean_trRIV_realized = m[["trRIV"]],
                                   trRIV_analytic = trRIV_analytic,
                                   ratio_analytic = m[["T_fitted"]] / trRIV_analytic,
                                   se_ratio_analytic = se_T / trRIV_analytic,
                                   ratio_realized = m[["T_fitted"]] / m[["trRIV"]])
    cat(sprintf("  [bern_fitted N=%4d R=%6d] mean T=%+.4f (se %.4f)  ratio(analytic den)=%+.4f (se %.4f)  ratio(realized den)=%+.4f\n",
                N, nrow(res), m[["T_fitted"]], se_T,
                m[["T_fitted"]] / trRIV_analytic, se_T / trRIV_analytic,
                m[["T_fitted"]] / m[["trRIV"]]))
  }
  return(out)
}

# -----------------------------------------------------------------------------
# arm B: bern_draw (mice logreg), paired with FITTED, N-scan
# -----------------------------------------------------------------------------

rep_bern_draw <- function(r, N, M) {
  cell <- sim_bern(BASE_SEED + 5e6 + r + N * 1000, N)
  if (sum(cell$miss) < 2 || length(unique(cell$Y[!cell$miss])) < 2) { return(NULL) }
  Y_obs <- cell$Y
  Y_obs[cell$miss] <- NA
  beta_com <- fit_logit(cell$Y, cell$X)
  beta_obs <- fit_logit(cell$Y[!cell$miss], cell$X[!cell$miss])
  ell_com = loglik_bern(beta_com, cell$Y, cell$X)
  T_fitted = anchor_bern(beta_obs, cell$Y, cell$X, cell$miss) - ell_com
  df <- data.frame(Y = factor(Y_obs), X = cell$X)
  imp <- mice::mice(df, method = c("logreg", ""), m = M, printFlag = FALSE, seed = r)
  comps <- lapply(seq_len(M), function(m) {
    dc <- mice::complete(imp, action = m)
    return(as.numeric(as.character(dc$Y)))
  })
  barL = mean(vapply(comps, function(Z) { return(loglik_bern(beta_obs, Z, cell$X)) },
                     numeric(1)))
  T_draw = barL - ell_com
  fits <- lapply(comps, function(Z) {
    f <- suppressWarnings(glm.fit(cbind(1, cell$X), Z, family = binomial()))
    XtWX <- crossprod(cbind(1, cell$X) * f$weights, cbind(1, cell$X))
    return(list(theta = unname(f$coefficients), U = solve(XtWX)))
  })
  riv <- riv_sample(lapply(fits, `[[`, "theta"), lapply(fits, `[[`, "U"))
  return(c(T_fitted = T_fitted, T_draw = T_draw, trRIV_sample = riv$tr_RIV,
           trRIV_realized = trRIV_realized_bern(cell$X, cell$miss)))
}

run_bern_draw <- function() {
  grid <- data.frame(N = c(200, 500, 1000, 2000),
                     R = rep(max(1000 %/% SMOKE_DIV, 10), 4))
  M <- 50
  out <- list()
  for (g in seq_len(nrow(grid))) {
    N <- grid$N[g]; R <- grid$R[g]
    cl <- makeCluster(N_CORES)
    clusterExport(cl, c("sim_bern", "fit_logit", "loglik_bern", "anchor_bern",
                        "trRIV_realized_bern", "rep_bern_draw", "riv_sample",
                        "BASE_SEED", "MISS_RATE", "BETA0"), envir = environment())
    res <- parLapply(cl, seq_len(R), function(r) {
      tryCatch(rep_bern_draw(r, N, M), error = function(e) NULL)
    })
    stopCluster(cl)
    res <- do.call(rbind, Filter(Negate(is.null), res))
    trRIV_analytic = 2 * MISS_RATE / (1 - MISS_RATE)
    d <- res[, "T_draw"] - res[, "T_fitted"]
    out[[as.character(N)]] <- list(N = N, R = nrow(res), M = M,
                                   mean_T_fitted = mean(res[, "T_fitted"]),
                                   mean_T_draw = mean(res[, "T_draw"]),
                                   mean_diff = mean(d), se_diff = sd(d) / sqrt(nrow(res)),
                                   diff_ratio_analytic = mean(d) / trRIV_analytic,
                                   se_diff_ratio = sd(d) / sqrt(nrow(res)) / trRIV_analytic,
                                   mean_trRIV_sample = mean(res[, "trRIV_sample"]),
                                   mean_trRIV_realized = mean(res[, "trRIV_realized"]),
                                   trRIV_analytic = trRIV_analytic)
    cat(sprintf("  [bern_draw   N=%4d R=%4d] paired diff=%+.4f (se %.4f)  diff-ratio=%+.4f (se %.4f)  trRIV sample=%.4f analytic=%.4f\n",
                N, nrow(res), mean(d), sd(d) / sqrt(nrow(res)),
                mean(d) / trRIV_analytic, sd(d) / sqrt(nrow(res)) / trRIV_analytic,
                mean(res[, "trRIV_sample"]), trRIV_analytic))
  }
  return(out)
}

# -----------------------------------------------------------------------------
# arm C: Poisson FITTED (log link, canonical). Entropy via series + spline
# interpolant (validated below against direct series and brute-force MC).
# -----------------------------------------------------------------------------

pois_H_direct <- function(mu) {
  kmax <- ceiling(mu + 15 * sqrt(mu) + 30)
  k <- 0:kmax
  logpmf <- k * log(mu) - mu - lgamma(k + 1)
  pmf <- exp(logpmf)
  return(-sum(pmf * logpmf))
}

build_pois_H_interp <- function() {
  lmu_grid <- seq(log(1e-4), log(4000), length.out = 4000)
  Hg <- vapply(exp(lmu_grid), pois_H_direct, numeric(1))
  return(splinefun(lmu_grid, Hg, method = "natural"))
}

rep_pois_fitted <- function(r, N, H_interp) {
  set.seed(BASE_SEED + 9e6 + r + N * 1000)
  X <- rnorm(N)
  mu <- exp(BETA0[1] + BETA0[2] * X)
  Y <- rpois(N, mu)
  miss <- runif(N) < MISS_RATE
  if (sum(miss) < 2) { return(NULL) }
  fit_com <- suppressWarnings(glm.fit(cbind(1, X), Y, family = poisson()))
  fit_obs <- suppressWarnings(glm.fit(cbind(1, X[!miss]), Y[!miss], family = poisson()))
  b_com <- unname(fit_com$coefficients)
  b_obs <- unname(fit_obs$coefficients)
  eta_obs <- b_obs[1] + b_obs[2] * X
  ll_obs_rows = sum(dpois(Y[!miss], exp(eta_obs[!miss]), log = TRUE))
  H_mis = H_interp(pmin(pmax(eta_obs[miss], log(1e-4)), log(4000)))
  anchor = ll_obs_rows + sum(-H_mis)
  ell_com = sum(dpois(Y, exp(b_com[1] + b_com[2] * X), log = TRUE))
  # realized tr(RIV) at beta0 (w = mu)
  w <- mu
  Xm <- cbind(1, X)
  J_obs <- crossprod(Xm[!miss, , drop = FALSE] * w[!miss], Xm[!miss, , drop = FALSE])
  J_mis <- crossprod(Xm[miss, , drop = FALSE] * w[miss], Xm[miss, , drop = FALSE])
  return(c(T_fitted = anchor - ell_com, trRIV = sum(diag(solve(J_obs, J_mis)))))
}

run_pois_fitted <- function() {
  # validate the interpolant + the entropy construction before use
  H_interp <- build_pois_H_interp()
  for (mu_chk in c(0.05, 0.7, 3.3, 41, 900)) {
    stopifnot(abs(H_interp(log(mu_chk)) - pois_H_direct(mu_chk)) < 1e-6)
  }
  set.seed(1)
  for (mu_chk in c(0.7, 12)) {   # brute-force MC validation of -H as E[log f]
    ymc <- rpois(2e6, mu_chk)
    mc <- mean(dpois(ymc, mu_chk, log = TRUE))
    stopifnot(abs(mc - (-pois_H_direct(mu_chk))) < 2e-3)
  }
  cat("  [pois_fitted] entropy interpolant + MC validation ok\n")
  grid <- data.frame(N = c(200, 1000), R = c(100000, 30000) %/% SMOKE_DIV)
  out <- list()
  for (g in seq_len(nrow(grid))) {
    N <- grid$N[g]; R <- grid$R[g]
    cl <- makeCluster(N_CORES)
    clusterExport(cl, c("rep_pois_fitted", "pois_H_direct", "BASE_SEED",
                        "MISS_RATE", "BETA0"), envir = environment())
    clusterExport(cl, "H_interp", envir = environment())
    res <- parLapply(cl, seq_len(R), function(r) {
      tryCatch(rep_pois_fitted(r, N, H_interp), error = function(e) NULL)
    })
    stopCluster(cl)
    res <- do.call(rbind, Filter(Negate(is.null), res))
    trRIV_analytic = 2 * MISS_RATE / (1 - MISS_RATE)
    m = colMeans(res)
    se_T = sd(res[, "T_fitted"]) / sqrt(nrow(res))
    out[[as.character(N)]] <- list(N = N, R = nrow(res),
                                   mean_T = m[["T_fitted"]], se_T = se_T,
                                   mean_trRIV_realized = m[["trRIV"]],
                                   trRIV_analytic = trRIV_analytic,
                                   ratio_analytic = m[["T_fitted"]] / trRIV_analytic,
                                   se_ratio_analytic = se_T / trRIV_analytic,
                                   ratio_realized = m[["T_fitted"]] / m[["trRIV"]])
    cat(sprintf("  [pois_fitted N=%4d R=%6d] mean T=%+.4f (se %.4f)  ratio(analytic den)=%+.4f (se %.4f)  ratio(realized den)=%+.4f\n",
                N, nrow(res), m[["T_fitted"]], se_T,
                m[["T_fitted"]] / trRIV_analytic, se_T / trRIV_analytic,
                m[["T_fitted"]] / m[["trRIV"]]))
  }
  return(out)
}

# -----------------------------------------------------------------------------
# arm D: Student-t location exemplar (nu=5, sigma=1 FIXED), FITTED + proper draw
# -----------------------------------------------------------------------------

T_NU <- 5
MU0_T <- 0.3

t_loglik <- function(mu, y) { return(sum(dt(y - mu, df = T_NU, log = TRUE))) }

t_mle <- function(y) {
  o <- optimize(function(m) { return(-t_loglik(m, y)) },
                interval = c(mean(y) - 6, mean(y) + 6))
  return(o$minimum)
}

t_entropy <- function() {
  nu <- T_NU
  return((nu + 1) / 2 * (digamma((nu + 1) / 2) - digamma(nu / 2)) +
           log(sqrt(nu) * beta(nu / 2, 1 / 2)))
}

rep_t_exemplar <- function(r, N, M) {
  set.seed(BASE_SEED + 13e6 + r)
  Y <- MU0_T + rt(N, df = T_NU)
  miss <- runif(N) < MISS_RATE
  n_obs <- sum(!miss)
  if (sum(miss) < 2) { return(NULL) }
  mu_com = t_mle(Y)
  mu_obs = t_mle(Y[!miss])
  ell_com = t_loglik(mu_com, Y)
  H_t = t_entropy()
  anchor = t_loglik(mu_obs, Y[!miss]) + sum(miss) * (-H_t)
  T_fitted = anchor - ell_com
  # proper draw: mu* ~ N(mu_obs, 1/(n_obs I1)), I1 = (nu+1)/(nu+3) (sigma=1)
  I1 <- (T_NU + 1) / (T_NU + 3)
  V_draw <- 1 / (n_obs * I1)
  comps <- lapply(seq_len(M), function(m) {
    mu_star <- rnorm(1, mu_obs, sqrt(V_draw))
    Z <- Y
    Z[miss] <- mu_star + rt(sum(miss), df = T_NU)
    return(Z)
  })
  barL = mean(vapply(comps, function(Z) { return(t_loglik(mu_obs, Z)) }, numeric(1)))
  T_draw = barL - ell_com
  fits <- lapply(comps, function(Z) {
    return(list(theta = t_mle(Z), U = matrix(1 / (N * I1), 1, 1)))
  })
  riv <- riv_sample(lapply(fits, function(f) { return(f$theta) }),
                    lapply(fits, function(f) { return(f$U) }))
  return(c(T_fitted = T_fitted, T_draw = T_draw, trRIV_sample = riv$tr_RIV,
           trRIV_realized = sum(miss) / n_obs))
}

run_t_exemplar <- function() {
  N <- 200
  # R raised 20k -> 200k by dated amendment (todo/045 Sec.3.3, 2026-07-04, pre-production):
  # the smoke run showed per-rep sd ~ 21 ratio units, so 20k gives se ~ 0.15 -- too wide
  # for a sharp zero-test. Precision-only change; targets and design untouched.
  R <- max(200000 %/% SMOKE_DIV, 10)
  M <- 50
  cl <- makeCluster(N_CORES)
  clusterExport(cl, c("rep_t_exemplar", "t_loglik", "t_mle", "t_entropy",
                      "riv_sample", "BASE_SEED", "MISS_RATE", "T_NU", "MU0_T"),
                envir = environment())
  res <- parLapply(cl, seq_len(R), function(r) {
    tryCatch(rep_t_exemplar(r, N, M), error = function(e) NULL)
  })
  stopCluster(cl)
  res <- do.call(rbind, Filter(Negate(is.null), res))
  trRIV_analytic = MISS_RATE / (1 - MISS_RATE)
  mT = mean(res[, "T_fitted"]); seT = sd(res[, "T_fitted"]) / sqrt(nrow(res))
  mD = mean(res[, "T_draw"]); seD = sd(res[, "T_draw"]) / sqrt(nrow(res))
  out <- list(N = N, R = nrow(res), M = M, nu = T_NU,
              mean_T_fitted = mT, se_T_fitted = seT,
              mean_T_draw = mD, se_T_draw = seD,
              ratio_fitted = mT / trRIV_analytic, se_ratio_fitted = seT / trRIV_analytic,
              ratio_draw = mD / trRIV_analytic, se_ratio_draw = seD / trRIV_analytic,
              mean_trRIV_sample = mean(res[, "trRIV_sample"]),
              mean_trRIV_realized = mean(res[, "trRIV_realized"]),
              trRIV_analytic = trRIV_analytic)
  cat(sprintf("  [t_exemplar N=%d R=%d] FITTED ratio=%+.4f (se %.4f)  DRAW ratio=%+.4f (se %.4f)  trRIV sample=%.4f analytic=%.4f\n",
              N, nrow(res), out$ratio_fitted, out$se_ratio_fitted,
              out$ratio_draw, out$se_ratio_draw,
              out$mean_trRIV_sample, trRIV_analytic))
  return(out)
}

# -----------------------------------------------------------------------------
# dispatch
# -----------------------------------------------------------------------------

dir.create("verification/cache", recursive = TRUE, showWarnings = FALSE)
arms <- if (ARM == "all") { c("bern_fitted", "bern_draw", "pois_fitted", "t_exemplar") } else { ARM }
for (a in arms) {
  cat(sprintf("\n== arm: %s ==\n", a))
  t0 <- Sys.time()
  res <- switch(a,
                bern_fitted = run_bern_fitted(),
                bern_draw = run_bern_draw(),
                pois_fitted = run_pois_fitted(),
                t_exemplar = run_t_exemplar(),
                stop("unknown arm: ", a))
  elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
  path <- sprintf("verification/cache/phase3-family-scan-%s-%s.rds", a, OUT_SUFFIX)
  saveRDS(list(arm = a, out = res, base_seed = BASE_SEED, miss_rate = MISS_RATE,
               beta0 = BETA0, elapsed_sec = elapsed), file = path)
  cat(sprintf("  cache: %s  (%.1f s)\n", path, elapsed))
}
cat("\ndone.\n")
