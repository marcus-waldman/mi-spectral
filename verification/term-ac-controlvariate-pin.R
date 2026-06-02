# term-ac-controlvariate-pin.R  [todo/020 -- DECISIVE pin of (A)+(C); analytic-surrogate control variate]
#
# Settles: is the full (A)+(C) = E[A_rb - tr(RIV)] equal to the DECOUPLED analytic value (~ -0.22),
# or does a genuine O(1) coefficient-fit COUPLING (dropped by the decoupled assembly, because A_rb,i is
# a DATA-DEPENDENT functional) push it to ~ -0.46?
#
# ESTIMATOR (control variate; cancels the O(sqrt n) linear-in-delta noise):
#   surrogate_i = gbar' delta_i + 1/2 delta_i' Hbar delta_i - tr_obs_i           (POPULATION gbar,Hbar)
#   (A)+(C)_full = decoupled_analytic + mean( ac_full_i - surrogate_i )
# where ac_full_i = A_rb_i - tr_obs_i, gbar = alpha (entropy gradient), Hbar = 2 I_mis|obs + H_phi,
# decoupled_analytic = alpha_Sigma' (b_Sigma/N) + 1/2 tr(H_phi I_obs^-1)  (= the assembly's -0.22).
# E[surrogate_i] = decoupled_analytic (analytic); the noise gbar'delta cancels between A_rb and
# surrogate, so mean(ac_full - surrogate) is LOW variance and equals the coupling + higher.
#
# VERDICT: coupling = mean(ac_full - surrogate) ~ -0.24 => true ~ -0.46, -0.22 undercounts (todo/018);
#          coupling ~ 0 => -0.22 is correct (reframing OK).
# SANITY: decoupled_analytic must be ~ -0.22; mean(ac_full) [noisy] must ~ (A)+(C)_full within MCSE.
#
# Usage: Rscript verification/term-ac-controlvariate-pin.R [R_main] [R_mom] [cores] [Ns]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel); library(jsonlite) })
args <- commandArgs(trailingOnly = TRUE)
R_main  = if (length(args) >= 1) { as.integer(args[1]) } else { 16000 }
R_mom   = if (length(args) >= 2) { as.integer(args[2]) } else { 2000 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 6 }
Ns      = if (length(args) >= 4) { as.integer(strsplit(args[4], ",")[[1]]) } else { c(800, 1500, 3000) }

p = 4; mu0 <- default_mu; Sig0 <- default_Sigma; k = p + p * (p + 1) / 2
TRUTH <- list(mu = mu0, Sigma = Sig0)
lt_mat <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
lt <- lower.tri(Sig0, diag = TRUE)
Epert <- function(s) { i = lt_mat[s, 1]; j = lt_mat[s, 2]; E <- matrix(0, p, p); E[i, j] <- 1; E[j, i] <- 1; return(E) }
amp_fun <- function(X) { return(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone")) }

# ---- population coefficients (copied from verify_term_ac_nonmonotone_4v.R; pattern-general) ----
est_moments <- function(N, R) {
  pacc <- list(); Iobs_sum <- matrix(0, k, k); n_ok = 0
  for (r in 1:R) {
    set.seed(990000 + r); X <- gen_data(N, mu0, Sig0)
    mar <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(mar)) { next }
    Rm <- mar$R; n_ok = n_ok + 1
    patt <- apply(Rm, 1, function(row) { return(paste(row, collapse = "")) })
    for (pp in unique(patt)) {
      Rp <- Rm[which(patt == pp)[1], ]; O <- which(Rp == 0); if (length(O) == p) { next }
      rows <- which(patt == pp); e <- sweep(X[rows, O, drop = FALSE], 2, mu0[O], FUN = "-")
      if (is.null(pacc[[pp]])) { pacc[[pp]] <- list(count = 0, s1 = numeric(p), s2 = matrix(0, p, p), O = O, M = which(Rp == 1)) }
      pacc[[pp]]$count <- pacc[[pp]]$count + nrow(e)
      pacc[[pp]]$s1[O] <- pacc[[pp]]$s1[O] + colSums(e)
      pacc[[pp]]$s2[O, O] <- pacc[[pp]]$s2[O, O] + crossprod(e)
    }
    Iobs_sum <- Iobs_sum + observed_info_obs_mvn(TRUTH, mar$Y, Rm)
  }
  pm <- list()
  for (key in names(pacc)) { a <- pacc[[key]]; O <- a$O
    pm[[key]] <- list(frac = a$count / (N * n_ok), m1 = a$s1[O] / a$count,
                      M2 = a$s2[O, O, drop = FALSE] / a$count, O = O, M = a$M) }
  return(list(pm = pm, Iobs = Iobs_sum / n_ok, N = N))
}
alpha_expected <- function(mm, N) {
  alpha <- numeric(k)
  for (key in names(mm$pm)) { P <- mm$pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    B0 <- Sig0[M, O, drop = FALSE] %*% solve(Sig0[O, O, drop = FALSE])
    S0i <- solve(Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE])
    for (s in 1:(k - p)) { E <- Epert(s)
      dS <- E[M, M, drop = FALSE] - E[M, O, drop = FALSE] %*% t(B0) - B0 %*% E[O, M, drop = FALSE] +
            B0 %*% E[O, O, drop = FALSE] %*% t(B0)
      alpha[p + s] <- alpha[p + s] - 0.5 * nP * sum(diag(S0i %*% dS)) } }
  return(alpha)
}
hphi_expected <- function(mm, N) {
  H <- matrix(0, k, k)
  for (key in names(mm$pm)) { P <- mm$pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    U <- solve(Sig0[O, O, drop = FALSE]); B0 <- Sig0[M, O, drop = FALSE] %*% U
    S0i <- solve(Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE])
    m1 <- P$m1; M2 <- P$M2
    Dmu <- matrix(0, length(M), p); for (jj in seq_along(M)) { Dmu[jj, M[jj]] <- 1 }; Dmu[, O] <- -B0
    GU <- vector("list", k - p); Gs <- vector("list", k - p)
    for (s in 1:(k - p)) { E <- Epert(s); G <- E[M, O, drop = FALSE] - B0 %*% E[O, O, drop = FALSE]
      Gs[[s]] <- G; GU[[s]] <- G %*% U }
    Hp <- matrix(0, k, k); Hp[1:p, 1:p] <- -t(Dmu) %*% S0i %*% Dmu
    for (s in 1:(k - p)) { v <- as.numeric(GU[[s]] %*% m1); col <- -t(Dmu) %*% (S0i %*% v)
      Hp[1:p, p + s] <- col; Hp[p + s, 1:p] <- col }
    for (aa in 1:(k - p)) { for (bb in aa:(k - p)) {
      qpart = -sum(diag(t(GU[[aa]]) %*% S0i %*% GU[[bb]] %*% M2))
      tpart = 0.5 * sum(diag(S0i %*% (Gs[[aa]] %*% U %*% t(Gs[[bb]]) + Gs[[bb]] %*% U %*% t(Gs[[aa]]))))
      Hp[p + aa, p + bb] <- qpart + tpart; Hp[p + bb, p + aa] <- Hp[p + aa, p + bb] } }
    H <- H + nP * Hp }
  return(H)
}

gp <- jsonlite::fromJSON("verification/cache/coxsnell-nonmonotone-bsigma-genp4.json")
bvech_cs <- as.numeric(gp[["beta0.0"]]$b_sigma_vech)
stopifnot(length(bvech_cs) == k - p)
Edelta <- c(numeric(p), bvech_cs)           # E[delta] = Edelta / N  (mu-block 0; alpha is cov-only)

main_one <- function(seed, N) {
  set.seed(seed)
  X <- gen_data(N, default_mu, default_Sigma)
  mar <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values = TRUE)$values) < 1e-6) { return(NULL) }
  dvec <- c(to$mu - mu0, (to$Sigma - Sig0)[lt])
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, TRUTH, mar$Y, mar$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), fisher_info_com_mvn(to, N)))) - k
  return(c(ac_full = A_rb - tr_obs, dvec, tr_obs = tr_obs))
}

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); suppressPackageStartupMessages(library(lavaan)) }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "TRUTH", "lt", "amp_fun", "main_one"))

cat("====== analytic-SURROGATE control-variate pin of (A)+(C) ======\n")
cat(sprintf("R_main=%d, R_mom=%d (population coeffs); design = phase-8 MAR non-monotone.\n", R_main, R_mom))
cat("coupling = mean(ac_full - surrogate); (A)+(C)_full = decoupled_analytic + coupling.\n")
cat("VERDICT: coupling ~ -0.24 => true ~ -0.46 (-0.22 undercounts); coupling ~ 0 => -0.22 correct.\n\n")
rows <- list()
for (N in Ns) {
  mm <- est_moments(N, R_mom)
  I_obs <- mm$Iobs; I_com <- fisher_info_com_mvn(TRUTH, N); I_mis <- I_com - I_obs
  alpha <- alpha_expected(mm, N); Hphi <- hphi_expected(mm, N)
  Hbar <- 2 * I_mis + Hphi
  tr_riv_pop <- sum(diag(solve(I_obs, I_com))) - k
  decoupled <- sum(alpha * Edelta / N) + 0.5 * sum(diag(Hphi %*% solve(I_obs)))   # = assembly (A)+(C) ~ -0.22
  M <- do.call(rbind, Filter(Negate(is.null),
          parLapply(cl, seq_len(R_main), function(s, NN) main_one(20260522 + s, NN), NN = N)))
  ac <- M[, "ac_full"]; D <- M[, 2:(k + 1)]
  # per-dataset surrogate on the (A)+(C) scale: gbar'd + 1/2 d'Hbar d - tr_obs ; ac_full - surrogate cancels tr_obs
  lin <- as.numeric(D %*% alpha)
  quad <- 0.5 * rowSums((D %*% Hbar) * D)
  surrogate_minus_trobs <- lin + quad - M[, "tr_obs"]
  diff <- ac - surrogate_minus_trobs            # = A_rb - (gbar'd + 1/2 d'Hbar d)  (tr_obs cancels)
  coupling <- mean(diff); coupling_se <- sd(diff) / sqrt(length(diff))
  theta_full <- decoupled + coupling
  naive <- mean(ac); naive_se <- sd(ac) / sqrt(length(ac))
  cat(sprintf("-- N=%4d (%d ok) --\n", N, nrow(M)))
  cat(sprintf("   decoupled_analytic   = %+.4f   [sanity: must be ~ -0.22]   tr(RIV)_pop=%.3f\n", decoupled, tr_riv_pop))
  cat(sprintf("   coupling = mean(ac - surrogate) = %+.4f (%.4f)   [sd(diff)=%.3f; LOW-variance]\n",
              coupling, coupling_se, sd(diff)))
  cat(sprintf("   (A)+(C)_full = decoupled + coupling = %+.4f (%.4f)\n", theta_full, coupling_se))
  cat(sprintf("   naive mean(ac_full) = %+.4f (%.4f)   [noisy cross-check; must ~ (A)+(C)_full]\n", naive, naive_se))
  cat(sprintf("   => vs -0.22: %+.3f (%.1f se) | vs -0.46: %+.3f (%.1f se)\n\n",
              theta_full + 0.22, (theta_full + 0.22) / coupling_se, theta_full + 0.46, (theta_full + 0.46) / coupling_se))
  rows[[as.character(N)]] <- c(N = N, decoupled = decoupled, coupling = coupling, coupling_se = coupling_se,
                               theta_full = theta_full, naive = naive, naive_se = naive_se, n_ok = nrow(M))
}
stopCluster(cl)
S <- do.call(rbind, rows)
cat("-- summary --\n"); print(round(S, 4))
saveRDS(S, "verification/cache/coupling-surrogate-cv.rds")
cat("\nwrote verification/cache/coupling-surrogate-cv.rds\n")
cat("VERDICT: coupling ~ -0.24 => true ~ -0.46 (-0.22 undercounts); coupling ~ 0 => -0.22 correct.\n")
cat("================================================================================================\n")
