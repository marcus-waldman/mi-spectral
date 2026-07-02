# audit-engine-formula.R — numerical checks for the todo/040 cross-model audit
# (Claude Fable 5, max effort, 2026-07-01).
#
# Object. For any imputation engine that draws phi = (mu*, Sigma*) given Y_obs
# and imputes each unit's missing block from N(m_i(phi), V_i(phi)), the
# engine-vs-FITTED Q-gap at the fixed evaluation point theta_obs is EXACTLY
#
#   D := barQ_engine(theta_obs) - barQ_fitted(theta_obs)
#      = -1/2 sum_i { E_phi[ d_i' Vhat_i^{-1} d_i ]
#                     + tr( Vhat_i^{-1} ( E_phi[V_i(Sigma*)] - Vhat_i ) ) },
#
# where d_i = m_i(phi) - m_i(theta_obs), Vhat_i = V_i(Sigma_hat), and
# Vhat_i^{-1} = [Sigma_hat^{-1}]_{MM}. No Taylor step: the identity uses only
# (a) E[quadratic form] for the Gaussian completion given phi and (b) the
# block-inverse orthogonality [Sigma_hat^{-1} r]_M = 0 for the fitted-completed
# residual r. So we can evaluate every engine's D by Monte Carlo over its
# PARAMETER draws alone — no imputation, no loglik calls, no M-noise.
#
# Predictions under audit (see the audit write-up):
#   P1 (Laplace/BvM draw, theta* ~ N(theta_obs, I_obs^{-1})):
#        D/tr(RIV) -> -tr(RIV_mumu)/(2 tr(RIV)); Sigma-draw pieces self-cancel
#        (Schur concavity vs Sigma-mean-wander). So mu-only draw == full draw,
#        Sigma-only draw == 0, to O(1) accuracy.
#   P2 (exact Jeffreys-IW DA): D = Laplace value
#        - 1/2 sum_i tr(Vhat_i^{-1} C_i b_Sigma C_i') with b_Sigma the
#        posterior mean bias E[Sigma*|Y_obs] - Sigma_hat; recentring the draws
#        by the measured b_Sigma collapses D onto the Laplace value (no
#        persistent "IW-shape" term).
#   P3 (bootstrap EMB = resample rows + EM): b_Sigma^boot ~ -Var(mu~), so
#        Xi = b_Sigma + Var(mu~) ~ 0 and D ~ 0 (the Amelia anomaly).
#
# Run:  Rscript verification/spikes/audit-engine-formula.R [ncores] [R_lap] [R_cj] [R_boot]
# Cache: verification/cache/spikes/audit-engine-formula.rds

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel); library(pbapply) })

args <- commandArgs(trailingOnly = TRUE)
ncores = if (length(args) >= 1) { as.integer(args[1]) } else { 20 }
R_lap = if (length(args) >= 2) { as.integer(args[2]) } else { 240 }
R_cj = if (length(args) >= 3) { as.integer(args[3]) } else { 120 }
R_boot = if (length(args) >= 4) { as.integer(args[4]) } else { 120 }
N_data = if (length(args) >= 5) { as.integer(args[5]) } else { 200 }
mcar_flag = if (length(args) >= 6) { as.integer(args[6]) == 1 } else { FALSE }
S_lap = 2000     # Laplace parameter draws per dataset
S_cj = 1500      # kept conjugate-DA parameter draws per dataset
S_boot = 400     # bootstrap-EM parameter draws per dataset
S_am = 250       # Amelia's own theta~ draws per dataset

# ---------------------------------------------------------------------------
# Pattern preparation at theta_obs.
# ---------------------------------------------------------------------------
prep_patterns <- function(theta_obs, Y, R) {
  p <- ncol(Y)
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  out <- list()
  for (pk in unique(patterns)) {
    rows <- which(patterns == pk)
    Mi <- which(R[rows[1], ] == 1)
    if (length(Mi) == 0) { next }
    Oi <- which(R[rows[1], ] == 0)
    Soo_inv <- solve(theta_obs$Sigma[Oi, Oi, drop = FALSE])
    Bhat <- theta_obs$Sigma[Mi, Oi, drop = FALSE] %*% Soo_inv
    Vhat <- theta_obs$Sigma[Mi, Mi, drop = FALSE] -
      Bhat %*% theta_obs$Sigma[Oi, Mi, drop = FALSE]
    Vhat <- 0.5 * (Vhat + t(Vhat))
    Vhat_inv <- solve(Vhat)
    out[[pk]] <- list(rows = rows, Mi = Mi, Oi = Oi, n_pat = length(rows),
                      Yo = Y[rows, Oi, drop = FALSE], Bhat = Bhat,
                      Vhat = Vhat, Vhat_inv = Vhat_inv)
  }
  return(out)
}

# ---------------------------------------------------------------------------
# Exact per-draw evaluation of the two identity pieces, summed over units.
# arm: "full" (draw both), "mu" (Sigma* := Sigma_hat), "sigma" (mu* := mu_hat).
# Returns c(mean_term, cov_term): sum_i d'Vhat^{-1}d and sum_i tr(Vhat^{-1}(V*-Vhat)).
# ---------------------------------------------------------------------------
eval_one_draw <- function(theta_star, theta_obs, prep, arm) {
  mu_s <- theta_star$mu
  Sig_s <- theta_star$Sigma
  if (arm == "mu") { Sig_s <- theta_obs$Sigma }
  if (arm == "sigma") { mu_s <- theta_obs$mu }
  mean_term = 0
  cov_term = 0
  for (pp in prep) {
    Soo_inv_s <- solve(Sig_s[pp$Oi, pp$Oi, drop = FALSE])
    Bs <- Sig_s[pp$Mi, pp$Oi, drop = FALSE] %*% Soo_inv_s
    Vs <- Sig_s[pp$Mi, pp$Mi, drop = FALSE] -
      Bs %*% Sig_s[pp$Oi, pp$Mi, drop = FALSE]
    d <- matrix(rep(mu_s[pp$Mi] - theta_obs$mu[pp$Mi], each = pp$n_pat),
                pp$n_pat, length(pp$Mi)) +
      sweep(pp$Yo, 2, mu_s[pp$Oi], FUN = "-") %*% t(Bs) -
      sweep(pp$Yo, 2, theta_obs$mu[pp$Oi], FUN = "-") %*% t(pp$Bhat)
    mean_term = mean_term + sum((d %*% pp$Vhat_inv) * d)
    cov_term = cov_term + pp$n_pat * sum(pp$Vhat_inv * (Vs - pp$Vhat))
  }
  return(c(mean_term, cov_term))
}

# D from a list of draws: -1/2 * mean over draws of (mean_term + cov_term).
eval_engine <- function(draws, theta_obs, prep, arms = c("full", "mu", "sigma")) {
  out <- list()
  for (arm in arms) {
    tm <- vapply(draws, function(th) {
      return(eval_one_draw(th, theta_obs, prep, arm))
    }, numeric(2))
    out[[arm]] <- c(D = -0.5 * (mean(tm[1, ]) + mean(tm[2, ])),
                    mean_term = mean(tm[1, ]), cov_term = mean(tm[2, ]))
  }
  return(out)
}

# Master-formula contraction: -1/2 sum_i n_pat tr(Vhat^{-1} C Xi C') for a
# p x p symmetric Xi acting on the mu-coordinates (C = [I, -Bhat]).
contract_Xi <- function(Xi, prep) {
  total = 0
  for (pp in prep) {
    CXiC <- Xi[pp$Mi, pp$Mi, drop = FALSE] -
      pp$Bhat %*% Xi[pp$Oi, pp$Mi, drop = FALSE] -
      Xi[pp$Mi, pp$Oi, drop = FALSE] %*% t(pp$Bhat) +
      pp$Bhat %*% Xi[pp$Oi, pp$Oi, drop = FALSE] %*% t(pp$Bhat)
    total = total + pp$n_pat * sum(pp$Vhat_inv * CXiC)
  }
  return(-0.5 * total)
}

# ---------------------------------------------------------------------------
# Draw sources.
# ---------------------------------------------------------------------------
draw_laplace <- function(theta_obs, Y, R, S) {
  p <- ncol(Y)
  vobs <- theta_to_vec(theta_obs)
  Vpost <- solve(fisher_info_obs_mvn(theta_obs, Y, R))
  Lp <- t(chol(0.5 * (Vpost + t(Vpost))))
  draws <- vector("list", S)
  s = 0
  n_reject = 0
  while (s < S) {
    th <- vec_to_theta(vobs + as.numeric(Lp %*% stats::rnorm(length(vobs))), p)
    ev <- eigen(th$Sigma, symmetric = TRUE, only.values = TRUE)$values
    if (min(ev) <= 1e-6) { n_reject = n_reject + 1; next }
    s = s + 1
    draws[[s]] <- th
  }
  attr(draws, "reject_rate") <- n_reject / (n_reject + S)
  return(draws)
}

# Exact split of the Sigma-only gap into a design-imbalance part (contraction
# against the realized within-pattern residual second moment minus its
# Sigma_hat_OO match; zero in expectation under MCAR at all orders of the draw)
# and a matched part (the second-order-cancelling pair; remainder = truncation
# mean-shift + quartic higher-order).
diag_sigma_split <- function(draws, theta_obs, prep) {
  imb = 0
  matched = 0
  for (pp in prep) {
    ro <- sweep(pp$Yo, 2, theta_obs$mu[pp$Oi], FUN = "-")
    Sr <- crossprod(ro)                                  # sum_rows r_O r_O'
    Soo_hat <- theta_obs$Sigma[pp$Oi, pp$Oi, drop = FALSE]
    t_imb = 0
    t_mat = 0
    for (th in draws) {
      Soo_inv_s <- solve(th$Sigma[pp$Oi, pp$Oi, drop = FALSE])
      Bs <- th$Sigma[pp$Mi, pp$Oi, drop = FALSE] %*% Soo_inv_s
      Vs <- th$Sigma[pp$Mi, pp$Mi, drop = FALSE] -
        Bs %*% th$Sigma[pp$Oi, pp$Mi, drop = FALSE]
      Bd <- Bs - pp$Bhat
      W <- t(Bd) %*% pp$Vhat_inv %*% Bd
      t_imb = t_imb + sum(W * (Sr - pp$n_pat * Soo_hat))
      t_mat = t_mat + pp$n_pat * (sum(W * Soo_hat) +
                                    sum(pp$Vhat_inv * (Vs - pp$Vhat)))
    }
    imb = imb + t_imb / length(draws)
    matched = matched + t_mat / length(draws)
  }
  return(c(imb = -0.5 * imb, matched = -0.5 * matched))
}

# Conjugate Jeffreys DA chain that RECORDS theta after each P-step (same math
# as verification/da-conjugate-engine.R, seeded at theta_obs).
draw_conjugate <- function(theta_obs, Y, R, S, burnin = 200, thin = 2) {
  N <- nrow(Y)
  p <- ncol(Y)
  prep <- prep_patterns(theta_obs, Y, R)   # pattern bookkeeping only
  Xc <- Y
  mu <- theta_obs$mu
  Sigma <- theta_obs$Sigma
  i_step <- function(mu, Sigma) {
    for (pp in prep) {
      Soo_inv <- solve(Sigma[pp$Oi, pp$Oi, drop = FALSE])
      reg <- Sigma[pp$Mi, pp$Oi, drop = FALSE] %*% Soo_inv
      cc <- Sigma[pp$Mi, pp$Mi, drop = FALSE] -
        reg %*% Sigma[pp$Oi, pp$Mi, drop = FALSE]
      cc <- 0.5 * (cc + t(cc))
      Lc <- t(chol(cc + diag(1e-10, length(pp$Mi))))
      CM <- matrix(rep(mu[pp$Mi], each = pp$n_pat), pp$n_pat, length(pp$Mi)) +
        sweep(Xc[pp$rows, pp$Oi, drop = FALSE], 2, mu[pp$Oi], FUN = "-") %*% t(reg)
      E <- matrix(stats::rnorm(pp$n_pat * length(pp$Mi)), pp$n_pat, length(pp$Mi))
      Xc[pp$rows, pp$Mi] <<- CM + E %*% t(Lc)
    }
    invisible(NULL)
  }
  p_step <- function() {
    ybar <- colMeans(Xc)
    Cc <- sweep(Xc, 2, ybar, FUN = "-")
    SS <- crossprod(Cc)
    SS <- 0.5 * (SS + t(SS)) + diag(1e-8, p)
    V <- chol2inv(chol(SS))
    W <- stats::rWishart(1, df = N - 1, Sigma = V)[, , 1]
    Sigma_new <- chol2inv(chol(W))
    Sigma_new <- 0.5 * (Sigma_new + t(Sigma_new))
    Lm <- t(chol(Sigma_new / N + diag(1e-12, p)))
    mu_new <- ybar + as.numeric(Lm %*% stats::rnorm(p))
    return(list(mu = mu_new, Sigma = Sigma_new))
  }
  for (b in seq_len(burnin)) {
    i_step(mu, Sigma)
    st <- p_step(); mu <- st$mu; Sigma <- st$Sigma
  }
  draws <- vector("list", S)
  for (s in seq_len(S)) {
    for (t in seq_len(thin)) {
      i_step(mu, Sigma)
      st <- p_step(); mu <- st$mu; Sigma <- st$Sigma
    }
    draws[[s]] <- list(mu = mu, Sigma = Sigma)
  }
  return(draws)
}

# Bootstrap EMB draws: resample rows (with their missingness), EM -> theta~.
draw_boot_em <- function(Y, S) {
  N <- nrow(Y)
  draws <- vector("list", S)
  s = 0
  tries = 0
  while (s < S) {
    tries = tries + 1
    idx <- sample.int(N, N, replace = TRUE)
    th <- tryCatch(em_mvn(Y[idx, , drop = FALSE]),
                   error = function(e) { return(NULL) })
    if (is.null(th)) { next }
    s = s + 1
    draws[[s]] <- list(mu = th$mu, Sigma = th$Sigma)
  }
  return(list(draws = draws, tries = tries))
}

# NOTE (audit finding): Amelia's a$mu / a$covMatrices are NOT the raw-scale
# theta~ ensemble — with boot.type = "none" they do not reproduce the EM MLE
# (internal reordering/standardization). Do not harvest them for this formula;
# the structural emulation draw_boot_em (resample + em_mvn) is the valid
# surrogate and matches Amelia's engine-measured D to ~0.0015 at N=200.

# Recentre a draw set's Sigma by its own measured mean bias (guard PD).
recentre_sigma <- function(draws, theta_obs) {
  p <- length(theta_obs$mu)
  Sbar <- Reduce(`+`, lapply(draws, function(th) { return(th$Sigma) })) / length(draws)
  b_Sigma <- Sbar - theta_obs$Sigma
  out <- lapply(draws, function(th) {
    S2 <- th$Sigma - b_Sigma
    ev <- eigen(S2, symmetric = TRUE, only.values = TRUE)$values
    if (min(ev) <= 1e-8) { S2 <- S2 + diag(1e-8 - min(ev), p) }
    return(list(mu = th$mu, Sigma = S2))
  })
  return(list(draws = out, b_Sigma = b_Sigma))
}

# Empirical mu-covariance and Sigma-mean-bias of a draw set.
draw_moments <- function(draws, theta_obs) {
  MU <- do.call(rbind, lapply(draws, function(th) { return(th$mu) }))
  Sbar <- Reduce(`+`, lapply(draws, function(th) { return(th$Sigma) })) / length(draws)
  return(list(var_mu = stats::cov(MU), b_Sigma = Sbar - theta_obs$Sigma))
}

# ---------------------------------------------------------------------------
# Per-dataset worker.
# ---------------------------------------------------------------------------
run_one <- function(r, do_cj, do_boot) {
  set.seed(20260522 + r)                       # same data stream as the spikes
  X <- gen_data(N_data, default_mu, default_Sigma)
  mar <- if (mcar_flag) {
    apply_mar(X, a1 = -0.468, b1 = 0, a2 = -0.468, b2 = 0)   # MCAR, same ~32% rate
  } else {
    apply_mar(X)
  }
  em <- em_mvn(mar$Y)
  theta_obs <- list(mu = em$mu, Sigma = em$Sigma)
  tri <- tr_riv_analytic(theta_obs, mar$Y, mar$R)
  I_mis <- tri$I_com - tri$I_obs
  rivdiag <- diag(solve(tri$I_obs, I_mis))
  p <- ncol(mar$Y)
  tr_riv = tri$tr_RIV
  tr_riv_mu = sum(rivdiag[seq_len(p)])
  n_mis = sum(mar$R)
  prep <- prep_patterns(theta_obs, mar$Y, mar$R)
  Vpost <- solve(tri$I_obs)
  Phi_mumu <- Vpost[seq_len(p), seq_len(p)]

  out <- list(r = r, tr_riv = tr_riv, tr_riv_mu = tr_riv_mu, n_mis = n_mis)

  # --- Laplace arm (P1) ---
  set.seed(31000000 + r)
  dl <- draw_laplace(theta_obs, mar$Y, mar$R, S_lap)
  el <- eval_engine(dl, theta_obs, prep)
  out$lap_full = el$full[["D"]] / tr_riv
  out$lap_mu = el$mu[["D"]] / tr_riv
  out$lap_sigma = el$sigma[["D"]] / tr_riv
  out$lap_pred_mu = -0.5 * tr_riv_mu / tr_riv                 # -tr(RIVmumu)/2tr
  out$lap_master = contract_Xi(Phi_mumu, prep) / tr_riv       # master formula
  sp <- diag_sigma_split(dl, theta_obs, prep)
  out$lap_sig_imb = sp[["imb"]] / tr_riv
  out$lap_sig_matched = sp[["matched"]] / tr_riv
  out$lap_reject = attr(dl, "reject_rate")
  moml <- draw_moments(dl, theta_obs)
  out$lap_bshift = contract_Xi(moml$b_Sigma, prep) / tr_riv   # truncation shift

  # --- Conjugate Jeffreys-IW arm (P2) ---
  if (do_cj) {
    set.seed(32000000 + r)
    dc <- draw_conjugate(theta_obs, mar$Y, mar$R, S_cj)
    ec <- eval_engine(dc, theta_obs, prep, arms = "full")
    mom <- draw_moments(dc, theta_obs)
    rc <- recentre_sigma(dc, theta_obs)
    ecr <- eval_engine(rc$draws, theta_obs, prep, arms = "full")
    out$cj_full = ec$full[["D"]] / tr_riv
    out$cj_recentred = ecr$full[["D"]] / tr_riv
    out$cj_b_contract = contract_Xi(mom$b_Sigma, prep) / tr_riv
    out$cj_master = contract_Xi(mom$b_Sigma + mom$var_mu, prep) / tr_riv
    out$cj_kappa = mean(diag(mom$b_Sigma) / diag(theta_obs$Sigma)) * N_data
    out$cj_var_mu_ratio = sum(diag(mom$var_mu)) / sum(diag(Phi_mumu))
  }

  # --- Bootstrap EMB arm (P3) ---
  if (do_boot) {
    set.seed(33000000 + r)
    db <- draw_boot_em(mar$Y, S_boot)
    eb <- eval_engine(db$draws, theta_obs, prep, arms = "full")
    momb <- draw_moments(db$draws, theta_obs)
    out$boot_full = eb$full[["D"]] / tr_riv
    out$boot_master = contract_Xi(momb$b_Sigma + momb$var_mu, prep) / tr_riv
    out$boot_b_contract = contract_Xi(momb$b_Sigma, prep) / tr_riv
    out$boot_wander = contract_Xi(momb$var_mu, prep) / tr_riv
    out$boot_var_mu_ratio = sum(diag(momb$var_mu)) / sum(diag(Phi_mumu))
  }
  return(out)
}

# ---------------------------------------------------------------------------
# Drive.
# ---------------------------------------------------------------------------
cl <- makeCluster(ncores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); NULL }))
clusterExport(cl, c("run_one", "prep_patterns", "eval_one_draw", "eval_engine",
                    "contract_Xi", "draw_laplace", "draw_conjugate",
                    "draw_boot_em", "recentre_sigma", "draw_moments",
                    "diag_sigma_split",
                    "N_data", "S_lap", "S_cj", "S_boot", "R_cj", "R_boot",
                    "mcar_flag"))
R_all = max(R_lap, R_cj, R_boot)
res <- pblapply(seq_len(R_all), function(r) {
  return(run_one(r, do_cj = (r <= R_cj), do_boot = (r <= R_boot)))
}, cl = cl)
stopCluster(cl)

grab <- function(nm) {
  v <- vapply(res, function(x) {
    if (is.null(x[[nm]])) { return(NA) } else { return(x[[nm]]) }
  }, numeric(1))
  return(v[!is.na(v)])
}
msd <- function(v) { return(sprintf("%+.4f (se %.4f, R=%d)", mean(v), sd(v) / sqrt(length(v)), length(v))) }

cat("\n=== audit-engine-formula: exact-identity evaluation, N =", N_data, "===\n")
cat("tr(RIV)            :", sprintf("%.3f", mean(grab("tr_riv"))), "\n")
cat("tr(RIV_mumu)       :", sprintf("%.3f", mean(grab("tr_riv_mu"))),
    sprintf("(mu share %.3f)", mean(grab("tr_riv_mu")) / mean(grab("tr_riv"))), "\n")
cat("n_mis per row      :", sprintf("%.3f", mean(grab("n_mis")) / N_data), "\n\n")

cat("P1 Laplace draw N(theta_obs, I_obs^-1)   [engine measured: -0.121]\n")
cat("  D/tr full draw       :", msd(grab("lap_full")), "\n")
cat("  D/tr mu-only draw    :", msd(grab("lap_mu")), "\n")
cat("  D/tr Sigma-only draw :", msd(grab("lap_sigma")), "\n")
cat("  pred -trRIVmu/2tr    :", msd(grab("lap_pred_mu")), "\n")
cat("  master formula       :", msd(grab("lap_master")), "\n")
cat("  Sigma-split imbalance:", msd(grab("lap_sig_imb")), "\n")
cat("  Sigma-split matched  :", msd(grab("lap_sig_matched")), "\n")
cat("  truncation b-shift   :", msd(grab("lap_bshift")), "\n")
cat("  PD reject rate       :", msd(grab("lap_reject")), "\n\n")

cat("P2 conjugate Jeffreys-IW DA               [engine measured: -0.783]\n")
cat("  D/tr full            :", msd(grab("cj_full")), "\n")
cat("  D/tr recentred       :", msd(grab("cj_recentred")), "  <- should equal Laplace full\n")
cat("  b_Sigma contraction  :", msd(grab("cj_b_contract")), "\n")
cat("  master (b+Var mu)    :", msd(grab("cj_master")), "\n")
cat("  kappa*N (rel. infl.) :", msd(grab("cj_kappa")), "  [complete-data (p+2) = 6]\n")
cat("  Var(mu*)/[Iobs^-1]mu :", msd(grab("cj_var_mu_ratio")), "\n\n")

cat("P3 bootstrap EMB (resample + EM)          [engine measured: -0.087 -> 0]\n")
cat("  D/tr full            :", msd(grab("boot_full")), "\n")
cat("  master (b+Var mu)    :", msd(grab("boot_master")), "\n")
cat("  b_Sigma contraction  :", msd(grab("boot_b_contract")), "\n")
cat("  mu-wander contraction:", msd(grab("boot_wander")), "\n")
cat("  Var(mu~)/[Iobs^-1]mu :", msd(grab("boot_var_mu_ratio")), "\n")

dir.create("verification/cache/spikes", showWarnings = FALSE, recursive = TRUE)
saveRDS(res, "verification/cache/spikes/audit-engine-formula.rds")
cat("\nCache: verification/cache/spikes/audit-engine-formula.rds\n")
