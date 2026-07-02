# spikes/phase0b-brms-imputer.R
#
# Phase-0 spike 0b (todo/040): brms-as-imputer FEASIBILITY + RUNTIME gate.
# NOT a full engine and NOT a sweep — the deliverable is:
#   G0b-1  does brms build the MVN imputer + return posterior-predictive
#          completions of the missing cells?
#   G0b-2  do those completions give a sample tr(RIV) consistent with analytic?
#   G0b-3  per-dataset wall-clock (compile-once amortised + per-fit sampling) —
#          this decides brms's role: workhorse / cross-check / non-normal-only /
#          infeasible. No target pre-committed; the number decides.
#
# brms AS AN IMPUTER: an intercept-only joint 4-variate Gaussian (residual
# correlations => the unstructured MVN, congenial with our analysis model), the
# missing cells drawn from the posterior. NOT bf(y|mi()) full-Bayes coupling,
# NOT brm_multiple pooling. Completions feed our EXISTING mi_fit_mvn/riv_sample.
#
# Same W1 theorem cell as 0a: default DGP, N=200, apply_mar, theta_obs = EM MLE.
#
# Usage:
#   Rscript verification/spikes/phase0b-brms-imputer.R [n_fits] [M] [chains] [iter]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(brms) })

args   <- commandArgs(trailingOnly = TRUE)
n_fits <- if (length(args) >= 1) as.integer(args[1]) else 3     # reps to time
M      <- if (length(args) >= 2) as.integer(args[2]) else 50
chains <- if (length(args) >= 3) as.integer(args[3]) else 2
iter   <- if (length(args) >= 4) as.integer(args[4]) else 1000

cat(sprintf("\nPhase-0b brms-as-imputer spike  [n_fits=%d, M=%d, chains=%d, iter=%d]\n",
            n_fits, M, chains, iter))
cat(sprintf("  brms %s\n", as.character(packageVersion("brms"))))

# --- Backend selection: cmdstanr if a cmdstan install is present, else rstan ---
backend <- "rstan"
cmdstan_ok <- FALSE
if (requireNamespace("cmdstanr", quietly = TRUE)) {
  v <- tryCatch(cmdstanr::cmdstan_version(), error = function(e) NULL)
  if (!is.null(v)) { backend <- "cmdstanr"; cmdstan_ok <- TRUE
    cat(sprintf("  backend=cmdstanr (cmdstan %s)\n", v)) }
}
if (!cmdstan_ok) { cat("  backend=rstan (no cmdstan install found)\n") }
options(mc.cores = chains)

# --- Build one replicate's cell (r) exactly as 0a / the frozen W1 ---
make_cell <- function(r) {
  set.seed(20260522 + r)
  X <- gen_data(N = 200, mu = default_mu, Sigma = default_Sigma)
  theta_com <- mle_complete_mvn(X)
  ell_com_at_com <- loglik_mvn(theta_com, X)
  mar <- apply_mar(X)
  em_fit <- em_mvn(mar$Y)
  theta_obs <- list(mu = em_fit$mu, Sigma = em_fit$Sigma)
  ell_com_at_obs <- loglik_mvn(theta_obs, X)
  trRIV_analytic <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  # FITTED anchor (deterministic FIML plug-in) — the +1/2 tr(RIV) reference.
  T_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ell_com_at_com
  df <- as.data.frame(mar$Y); colnames(df) <- sprintf("X%d", 1:4)
  return(list(df = df, Y = mar$Y, R = mar$R, theta_obs = theta_obs,
              ell_com_at_com = ell_com_at_com, ell_com_at_obs = ell_com_at_obs,
              trRIV_analytic = trRIV_analytic, T_fiml = T_fiml))
}

# --- Joint 4-variate Gaussian imputer with residual correlations ---
# X1, X2 carry missingness (mi()); X3, X4 fully observed.
bform_rescor <- bf(X1 | mi() ~ 1) + bf(X2 | mi() ~ 1) +
                bf(X3 ~ 1) + bf(X4 ~ 1) + set_rescor(TRUE)
# Fallback: fully-conditional (FCS-style) imputer if rescor+mi is unsupported.
bform_fcs <- bf(X1 | mi() ~ mi(X2) + X3 + X4) +
             bf(X2 | mi() ~ mi(X1) + X3 + X4) + set_rescor(FALSE)

fit_imputer <- function(df, form, ...) {
  brms::brm(form, data = df, backend = backend, chains = chains, iter = iter,
            refresh = 0, silent = 2, seed = 1, ...)
}

# --- Extract M posterior-predictive completions of the missing cells ---
build_completions <- function(fit, Y, M) {
  N <- nrow(Y); p <- ncol(Y)
  vn <- brms::variables(fit)
  draws <- posterior::as_draws_matrix(fit)
  S <- nrow(draws)
  sel <- round(seq(1, S, length.out = M))
  miss_idx <- lapply(seq_len(p), function(j) which(is.na(Y[, j])))
  ymi_cols <- lapply(seq_len(p), function(j) {
    cols <- grep(sprintf("^Ymi_X%d\\[", j), vn, value = TRUE)
    if (length(cols) == 0) return(character(0))
    idx <- as.integer(sub(".*\\[(\\d+)\\]$", "\\1", cols))
    return(cols[order(idx)])                       # numeric, not lexical, order
  })
  comps <- lapply(sel, function(s) {
    Z <- Y
    for (j in seq_len(p)) {
      if (length(miss_idx[[j]]) == 0) next
      Z[miss_idx[[j]], j] <- as.numeric(draws[s, ymi_cols[[j]]])
    }
    return(Z)
  })
  return(comps)
}

# --- Run: fit rep 1 (compile + sample), then reps 2.. (compile cached) ---
cell1 <- make_cell(1)
cat("\n[fit 1] compiling + sampling (first fit includes Stan compile)...\n")
t_a <- Sys.time()
fit1 <- tryCatch(fit_imputer(cell1$df, bform_rescor),
                 error = function(e) { cat("  rescor+mi failed:", conditionMessage(e), "\n"); NULL })
form_used <- "rescor"
if (is.null(fit1)) {
  cat("[fit 1] falling back to fully-conditional (FCS) imputer...\n")
  t_a <- Sys.time()
  fit1 <- tryCatch(fit_imputer(cell1$df, bform_fcs),
                   error = function(e) { cat("  FCS failed:", conditionMessage(e), "\n"); NULL })
  form_used <- "fcs"
}
t_first <- as.numeric(difftime(Sys.time(), t_a, units = "secs"))

if (is.null(fit1)) {
  cat("\nG0b-1 FAIL: brms could not build the imputer under either form.\n")
  cat("Phase-0b verdict: INFEASIBLE in this environment.\n")
  quit(status = 0)
}
cat(sprintf("[fit 1] done in %.1fs (form=%s, includes compile)\n", t_first, form_used))

# tr(RIV) + T from the completions. THE KEY NUMBER: the deviance-bias gap
# (T_brms - FITTED)/tr(RIV), directly comparable to the 0a split
# (conjugate/norm -0.75, Amelia/gauss ~0). Tells us which branch brms's prior lands on.
score_fit <- function(fit, cell, lab, dt) {
  comps <- build_completions(fit, cell$Y, M)
  n_ymi <- length(grep("^Ymi_", brms::variables(fit)))
  mi <- mi_fit_mvn(comps)
  trRIV <- riv_sample(mi$theta_imps, mi$U_imps)$tr_RIV
  barL <- mean(vapply(comps, function(Z) loglik_mvn(cell$theta_obs, Z), numeric(1)))
  Tb <- barL - cell$ell_com_at_com
  gap <- (Tb - cell$T_fiml) / cell$trRIV_analytic
  cat(sprintf("[%s] %.1fs  Ymi=%d  sample tr(RIV)=%.3f (an %.3f)  T=%+.3f  (T-FITTED)/tr=%+.3f\n",
              lab, dt, n_ymi, trRIV, cell$trRIV_analytic, Tb, gap))
  list(n_ymi = n_ymi, trRIV = trRIV, T = Tb, gap = gap, n_comps = length(comps))
}
s1 <- score_fit(fit1, cell1, "fit 1", t_first)
gaps <- s1$gap; trRIV_brms1 <- s1$trRIV
G0b1 <- s1$n_ymi > 0 && s1$n_comps == M
G0b2 <- abs(s1$trRIV - cell1$trRIV_analytic) <= 0.5 * cell1$trRIV_analytic

# Time additional fits (compile now cached) to isolate per-fit sampling + gap.
per_fit_times <- numeric(0)
if (n_fits > 1) {
  for (r in 2:n_fits) {
    cellr <- make_cell(r)
    tb <- Sys.time()
    fitr <- tryCatch(fit_imputer(cellr$df, if (form_used == "rescor") bform_rescor else bform_fcs),
                     error = function(e) NULL)
    dt <- as.numeric(difftime(Sys.time(), tb, units = "secs"))
    if (is.null(fitr)) { cat(sprintf("[fit %d] FAILED\n", r)); next }
    per_fit_times <- c(per_fit_times, dt)
    sr <- score_fit(fitr, cellr, sprintf("fit %d", r), dt)
    gaps <- c(gaps, sr$gap)
  }
}
per_fit_med <- if (length(per_fit_times) > 0) median(per_fit_times) else t_first
mean_gap <- mean(gaps); se_gap <- if (length(gaps) > 1) sd(gaps)/sqrt(length(gaps)) else NA
T_brms1 <- s1$T

cat("\n== Phase-0b results ==\n\n")
cat(sprintf("Backend: %s ; imputer form: %s\n", backend, form_used))
cat(sprintf("First fit (compile+sample): %.1fs\n", t_first))
cat(sprintf("Per-fit sampling (cached compile), median of %d: %.1fs\n",
            length(per_fit_times), per_fit_med))
cat(sprintf("Sample tr(RIV) brms (rep1): %.4f  vs analytic %.4f\n",
            trRIV_brms1, cell1$trRIV_analytic))
cat(sprintf("\nDEVIANCE-BIAS BRANCH: (T_brms - FITTED)/tr(RIV) over %d fit(s) = %+.3f%s\n",
            length(gaps), mean_gap,
            if (!is.na(se_gap)) sprintf(" (se %.3f)", se_gap) else ""))
cat("  compare 0a: conjugate/norm Jeffreys-IW ~ -0.75 ; Amelia/gauss-posterior ~ 0\n")
cat(sprintf("  => brms (weakly-informative prior) lands %s\n",
            if (mean_gap < -0.4) "on the EXACT-DA branch (prior-general full-Bayes effect)"
            else if (mean_gap > -0.2) "on the Amelia/FITTED branch (Jeffreys-inflation-specific)"
            else "BETWEEN the two branches"))
cat("\nGate     Check                                          Pass\n")
cat("-------  ---------------------------------------------  ----\n")
cat(sprintf("G0b-1    fits + returns %d completions                  %s\n", M, if (G0b1) "PASS" else "FAIL"))
cat(sprintf("G0b-2    sample tr(RIV) within 50%% of analytic (n=1)   %s\n", if (G0b2) "PASS" else "SEE"))

# Runtime-gate verdict (per-fit median vs the sweep scale ~R*cells).
verdict <- if (per_fit_med <= 2) {
  "WORKHORSE-CANDIDATE (fast enough to consider for a full sweep)"
} else if (per_fit_med <= 20) {
  "CROSS-CHECK (feasible for tens of cells / focused reps; too slow for full R=1000 sweep)"
} else {
  "NON-NORMAL-ONLY or INFEASIBLE for large R (reserve for a focused Phase-3 illustration)"
}
cat(sprintf("\nRuntime gate (per-fit median %.1fs): %s\n", per_fit_med, verdict))
cat(sprintf("  extrapolation: R=1000 single cell ~= %.1f min ; 60-cell sweep ~= %.1f hr\n",
            per_fit_med * 1000 / 60, per_fit_med * 1000 * 60 / 3600))

dir.create("verification/cache/spikes", recursive = TRUE, showWarnings = FALSE)
saveRDS(list(backend = backend, form_used = form_used,
             t_first = t_first, per_fit_times = per_fit_times,
             per_fit_med = per_fit_med, gaps = gaps,
             mean_gap = mean_gap, se_gap = se_gap,
             trRIV_brms1 = trRIV_brms1,
             trRIV_analytic = cell1$trRIV_analytic, T_brms1 = T_brms1,
             gates = c(G0b1 = G0b1, G0b2 = G0b2), verdict = verdict),
        file = "verification/cache/spikes/phase0b-brms-imputer.rds")
cat("\nCache: verification/cache/spikes/phase0b-brms-imputer.rds\n")
