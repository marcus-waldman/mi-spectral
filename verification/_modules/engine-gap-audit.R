# _modules/engine-gap-audit.R
#
# Promotion of verification/spikes/audit-engine-formula.R (todo/040 cross-model
# audit, Claude Fable 5, max effort) into a run_all.R-style module: cached RDS per
# cell + a summary.csv, instead of print-only. See todo/040-audit-response-fable5.md
# and the staged manuscript/derivation.qmd amendment (todo/040-derivation-amendment-
# draft.md; NOT yet landed -- awaiting the GPT-5.5 gate + Marcus's ratification).
#
# Object. For any imputation engine that draws phi = (mu*, Sigma*) given Y_obs and
# imputes each unit's missing block from N(m_i(phi), V_i(phi)), the engine-vs-FITTED
# Q-gap at the fixed evaluation point theta_obs is EXACTLY
#
#   D := barQ_engine(theta_obs) - barQ_fitted(theta_obs)
#      = -1/2 sum_i { E_phi[ d_i' Vhat_i^{-1} d_i ]
#                     + tr( Vhat_i^{-1} ( E_phi[V_i(Sigma*)] - Vhat_i ) ) },
#
# evaluated by Monte Carlo over each engine's PARAMETER draws alone -- no imputation,
# no loglik calls, no M-noise. The four algebraic lemmas behind the reduction to the
# master formula D = -1/2 tr(RIV_mumu) - 1/2 sum_i tr(Vhat_i^-1 C_i b_Sigma C_i') - IMB
# are checked symbolically in verification/cas-wolfram/verify_engine_gap_sympy.py
# `[mc]`; this module supplies the numerical (Monte Carlo) side.
#
# Three cells, matching the audit response's own reproduction commands (same seed
# stream: 20260522 + r per replicate, repo convention; per-arm draw streams offset
# by a fixed constant -- 31000000 Laplace, 32000000 conjugate, 33000000 bootstrap --
# so arms never share a stream):
#   N200_MAR   "production"    (audit Sec. 2g table, Sec. 3 discrimination table)
#   N1000_MAR  "persistence"   (N-scan: confirms the terms are O(1), not decaying)
#   N200_MCAR  "discriminator" (audit Sec. 5: IMB predicted exactly 0 under MCAR;
#                                Laplace-only -- the conjugate/bootstrap arms add
#                                nothing MCAR-specific beyond what the MAR cells show)
#
# R_per_cell drives the cheap Laplace arm directly; the conjugate-DA and
# bootstrap-EM arms are far more expensive per replicate (an MCMC chain with
# burn-in/thinning, resp. an EM fit, vs. one Cholesky draw), so they run at
# ceiling(R_per_cell/2) -- the same ~2:1 ratio the audit's own ad hoc runs used
# (240/120/120 at N=200). Idempotent given (R_per_cell, seed).

ENGA_CELLS <- list(
  list(cell_id = "N200_MAR",  N = 200,  mcar = FALSE, include_cj_boot = TRUE),
  list(cell_id = "N1000_MAR", N = 1000, mcar = FALSE, include_cj_boot = TRUE),
  list(cell_id = "N200_MCAR", N = 200,  mcar = TRUE,  include_cj_boot = FALSE)
)
ENGA_S_LAP <- 2000   # Laplace parameter draws per dataset
ENGA_S_CJ <- 1500    # kept conjugate-DA parameter draws per dataset
ENGA_S_BOOT <- 400   # bootstrap-EM parameter draws per dataset

# ---------------------------------------------------------------------------
# Pattern preparation at theta_obs (unchanged from the spike).
# ---------------------------------------------------------------------------
enga_prep_patterns <- function(theta_obs, Y, R) {
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

# Exact per-draw evaluation of the two identity pieces, summed over units.
# arm: "full" (draw both), "mu" (Sigma* := Sigma_hat), "sigma" (mu* := mu_hat).
enga_eval_one_draw <- function(theta_star, theta_obs, prep, arm) {
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
enga_eval_engine <- function(draws, theta_obs, prep, arms = c("full", "mu", "sigma")) {
  out <- list()
  for (arm in arms) {
    tm <- vapply(draws, function(th) {
      return(enga_eval_one_draw(th, theta_obs, prep, arm))
    }, numeric(2))
    out[[arm]] <- c(D = -0.5 * (mean(tm[1, ]) + mean(tm[2, ])),
                    mean_term = mean(tm[1, ]), cov_term = mean(tm[2, ]))
  }
  return(out)
}

# Master-formula contraction: -1/2 sum_i n_pat tr(Vhat^{-1} C Xi C') for a
# p x p symmetric Xi acting on the mu-coordinates (C = [I, -Bhat]).
enga_contract_Xi <- function(Xi, prep) {
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

enga_draw_laplace <- function(theta_obs, Y, R, S) {
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
# mean-shift + quartic higher-order). See @sec-audit Sec. 5.
enga_diag_sigma_split <- function(draws, theta_obs, prep) {
  imb = 0
  matched = 0
  for (pp in prep) {
    ro <- sweep(pp$Yo, 2, theta_obs$mu[pp$Oi], FUN = "-")
    Sr <- crossprod(ro)
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

# Conjugate Jeffreys DA chain that RECORDS theta after each P-step (same math as
# verification/da-conjugate-engine.R, seeded at theta_obs).
enga_draw_conjugate <- function(theta_obs, Y, R, S, burnin = 200, thin = 2) {
  N <- nrow(Y)
  p <- ncol(Y)
  prep <- enga_prep_patterns(theta_obs, Y, R)
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
enga_draw_boot_em <- function(Y, S) {
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

# NOTE (audit finding): Amelia's a$mu / a$covMatrices are NOT the raw-scale theta~
# ensemble -- with boot.type = "none" they do not reproduce the EM MLE (internal
# reordering/standardization). Do not harvest them for this formula; the structural
# emulation enga_draw_boot_em (resample + em_mvn) is the valid surrogate and matches
# Amelia's engine-measured D to ~0.0015 at N=200.

# Recentre a draw set's Sigma by its own measured mean bias (guard PD).
enga_recentre_sigma <- function(draws, theta_obs) {
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
enga_draw_moments <- function(draws, theta_obs) {
  MU <- do.call(rbind, lapply(draws, function(th) { return(th$mu) }))
  Sbar <- Reduce(`+`, lapply(draws, function(th) { return(th$Sigma) })) / length(draws)
  return(list(var_mu = stats::cov(MU), b_Sigma = Sbar - theta_obs$Sigma))
}

# ---------------------------------------------------------------------------
# Per-dataset worker. Cell parameters (N_data, mcar_flag, S_lap/S_cj/S_boot,
# do_cj/do_boot) are explicit arguments, not enclosing-scope globals, so the
# function is self-contained for clusterExport.
# ---------------------------------------------------------------------------
enga_run_one <- function(r, N_data, mcar_flag, S_lap, S_cj, S_boot, do_cj, do_boot) {
  set.seed(20260522 + r)
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
  prep <- enga_prep_patterns(theta_obs, mar$Y, mar$R)
  Vpost <- solve(tri$I_obs)
  Phi_mumu <- Vpost[seq_len(p), seq_len(p)]

  out <- list(r = r, tr_riv = tr_riv, tr_riv_mu = tr_riv_mu, n_mis = n_mis)

  # --- Laplace arm ---
  set.seed(31000000 + r)
  dl <- enga_draw_laplace(theta_obs, mar$Y, mar$R, S_lap)
  el <- enga_eval_engine(dl, theta_obs, prep)
  out$lap_full = el$full[["D"]] / tr_riv
  out$lap_mu = el$mu[["D"]] / tr_riv
  out$lap_sigma = el$sigma[["D"]] / tr_riv
  out$lap_pred_mu = -0.5 * tr_riv_mu / tr_riv
  out$lap_master = enga_contract_Xi(Phi_mumu, prep) / tr_riv
  sp <- enga_diag_sigma_split(dl, theta_obs, prep)
  out$lap_sig_imb = sp[["imb"]] / tr_riv
  out$lap_sig_matched = sp[["matched"]] / tr_riv
  out$lap_reject = attr(dl, "reject_rate")
  moml <- enga_draw_moments(dl, theta_obs)
  out$lap_bshift = enga_contract_Xi(moml$b_Sigma, prep) / tr_riv

  # --- Conjugate Jeffreys-IW arm ---
  if (do_cj) {
    set.seed(32000000 + r)
    dc <- enga_draw_conjugate(theta_obs, mar$Y, mar$R, S_cj)
    ec <- enga_eval_engine(dc, theta_obs, prep, arms = "full")
    mom <- enga_draw_moments(dc, theta_obs)
    rc <- enga_recentre_sigma(dc, theta_obs)
    ecr <- enga_eval_engine(rc$draws, theta_obs, prep, arms = "full")
    out$cj_full = ec$full[["D"]] / tr_riv
    out$cj_recentred = ecr$full[["D"]] / tr_riv
    out$cj_b_contract = enga_contract_Xi(mom$b_Sigma, prep) / tr_riv
    out$cj_master = enga_contract_Xi(mom$b_Sigma + mom$var_mu, prep) / tr_riv
    out$cj_kappa = mean(diag(mom$b_Sigma) / diag(theta_obs$Sigma)) * N_data
    out$cj_var_mu_ratio = sum(diag(mom$var_mu)) / sum(diag(Phi_mumu))
  }

  # --- Bootstrap EMB arm ---
  if (do_boot) {
    set.seed(33000000 + r)
    db <- enga_draw_boot_em(mar$Y, S_boot)
    eb <- enga_eval_engine(db$draws, theta_obs, prep, arms = "full")
    momb <- enga_draw_moments(db$draws, theta_obs)
    out$boot_full = eb$full[["D"]] / tr_riv
    out$boot_master = enga_contract_Xi(momb$b_Sigma + momb$var_mu, prep) / tr_riv
    out$boot_b_contract = enga_contract_Xi(momb$b_Sigma, prep) / tr_riv
    out$boot_wander = enga_contract_Xi(momb$var_mu, prep) / tr_riv
    out$boot_var_mu_ratio = sum(diag(momb$var_mu)) / sum(diag(Phi_mumu))
  }
  return(out)
}

enga_mcse <- function(x) { return(sd(x, na.rm = TRUE) / sqrt(sum(!is.na(x)))) }
enga_grab <- function(res, nm) {
  v <- vapply(res, function(x) {
    if (is.null(x[[nm]])) { return(NA) } else { return(x[[nm]]) }
  }, numeric(1))
  return(v[!is.na(v)])
}

# One summary.csv row per cell: means (+ MC SE where the console table historically
# reported one) of every quantity the audit response's own tables cite.
enga_summarize_cell <- function(cell, res, R_lap, R_cj) {
  g <- function(nm) { return(enga_grab(res, nm)) }
  gm <- function(nm) { return(mean(g(nm))) }
  na_unless <- function(val) { if (cell$include_cj_boot) { return(val) } else { return(NA) } }
  return(data.frame(
    cell_id = cell$cell_id, N = cell$N, mcar = cell$mcar, R_lap = R_lap, R_cj = R_cj,
    tr_riv = gm("tr_riv"), tr_riv_mu_share = gm("tr_riv_mu") / gm("tr_riv"),
    n_mis_frac = gm("n_mis") / cell$N,
    lap_full = gm("lap_full"), lap_full_mcse = enga_mcse(g("lap_full")),
    lap_mu = gm("lap_mu"), lap_sigma = gm("lap_sigma"), lap_pred_mu = gm("lap_pred_mu"),
    lap_master = gm("lap_master"),
    lap_sig_imb = gm("lap_sig_imb"), lap_sig_imb_mcse = enga_mcse(g("lap_sig_imb")),
    lap_sig_matched = gm("lap_sig_matched"), lap_bshift = gm("lap_bshift"),
    lap_reject = gm("lap_reject"),
    cj_full = na_unless(gm("cj_full")), cj_full_mcse = na_unless(enga_mcse(g("cj_full"))),
    cj_recentred = na_unless(gm("cj_recentred")), cj_b_contract = na_unless(gm("cj_b_contract")),
    cj_master = na_unless(gm("cj_master")), cj_kappa = na_unless(gm("cj_kappa")),
    cj_var_mu_ratio = na_unless(gm("cj_var_mu_ratio")),
    boot_full = na_unless(gm("boot_full")), boot_full_mcse = na_unless(enga_mcse(g("boot_full"))),
    boot_master = na_unless(gm("boot_master")), boot_b_contract = na_unless(gm("boot_b_contract")),
    boot_wander = na_unless(gm("boot_wander")), boot_var_mu_ratio = na_unless(gm("boot_var_mu_ratio")),
    n_ok = length(res), stringsAsFactors = FALSE))
}

# ---------------------------------------------------------------------------
# Driver, run_all.R-shaped: run_engine_gap_audit(R_per_cell, cl, out_dir). `cl` is
# an externally-managed cluster (or NULL for serial); this module does not create
# or stop its own cluster, matching the other _modules/ files.
# ---------------------------------------------------------------------------
run_engine_gap_audit <- function(R_per_cell, cl, out_dir) {
  if (!dir.exists(out_dir)) { dir.create(out_dir, recursive = TRUE) }
  cat(sprintf("\n== engine-gap-audit (todo/040): DA-engine deviance-gap [R=%d] ==\n", R_per_cell))
  has_cl <- !is.null(cl)
  if (has_cl) {
    clusterExport(cl, c("enga_run_one", "enga_prep_patterns", "enga_eval_one_draw",
                        "enga_eval_engine", "enga_contract_Xi", "enga_draw_laplace",
                        "enga_draw_conjugate", "enga_draw_boot_em", "enga_recentre_sigma",
                        "enga_draw_moments", "enga_diag_sigma_split"))
  }
  papply <- function(items, fn) {
    if (has_cl) { return(parLapply(cl, items, fn)) } else { return(lapply(items, fn)) }
  }
  rows <- list()

  for (cell in ENGA_CELLS) {
    R_lap <- R_per_cell
    R_cj <- if (cell$include_cj_boot) { max(1, ceiling(R_per_cell / 2)) } else { 0 }
    cat(sprintf("  -- %-11s N=%4d mcar=%s R_lap=%d R_cj=R_boot=%d --\n",
                cell$cell_id, cell$N, cell$mcar, R_lap, R_cj))
    res <- papply(seq_len(R_lap), function(r) {
      return(enga_run_one(r, cell$N, cell$mcar, ENGA_S_LAP, ENGA_S_CJ, ENGA_S_BOOT,
                          do_cj = (r <= R_cj), do_boot = (r <= R_cj)))
    })
    saveRDS(res, file.path(out_dir, paste0(cell$cell_id, ".rds")))
    row <- enga_summarize_cell(cell, res, R_lap, R_cj)
    rows[[cell$cell_id]] <- row
    cat(sprintf("     tr(RIV)=%.3f mu-share=%.3f lap_full=%+.4f(%.4f) cj_full=%s boot_full=%s\n",
                row$tr_riv, row$tr_riv_mu_share, row$lap_full, row$lap_full_mcse,
                if (is.na(row$cj_full)) { "--" } else { sprintf("%+.4f", row$cj_full) },
                if (is.na(row$boot_full)) { "--" } else { sprintf("%+.4f", row$boot_full) }))
  }

  summary <- do.call(rbind, rows)
  write.csv(summary, file.path(out_dir, "summary.csv"), row.names = FALSE)
  cat(sprintf("  wrote %s\n", file.path(out_dir, "summary.csv")))
  return(summary)
}

# Standalone smoke test (not wired into run_all.R's phase dispatch -- that
# integration is a follow-up once Marcus ratifies the framing, see todo/040):
#   Rscript -e 'source("verification/00-setup.R"); source("verification/_modules/engine-gap-audit.R"); run_engine_gap_audit(20, NULL, "verification/cache/engine-gap-audit")'
