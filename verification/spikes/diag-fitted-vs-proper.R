# diag-fitted-vs-proper.R
# Is the conjugate-DA offset a BUG or the FITTED-vs-ORACLE sign subtlety?
# Per rep, compare against the DETERMINISTIC FITTED value (barQ_fiml_analytic,
# zero MC noise) as the anchor:
#   T_fiml       exact FITTED  (theory: +1/2 tr(RIV))
#   T_conj_fix   impute at FIXED theta_obs, M conditional draws (no param uncert.)
#   T_conj_full  full conjugate DA (parameter uncertainty via IW/N P-step)
#   T_amelia     Amelia EMB
# Also check the P-step posterior spread of Sigma vs the analytic sampling var.
source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")
suppressPackageStartupMessages({ library(parallel); library(pbapply) })

Rn <- 40; M <- 50

# Fixed-theta stochastic imputation: Y_mis | theta_obs, M independent draws.
impute_fixed_theta <- function(Y, theta, M) {
  N <- nrow(Y); p <- ncol(Y)
  R <- matrix(as.numeric(is.na(Y)), N, p)
  patterns <- apply(R, 1, paste, collapse = "")
  upat <- unique(patterns)
  out <- vector("list", M)
  for (m in seq_len(M)) {
    Z <- Y
    for (pk in upat) {
      rows <- which(patterns == pk); Mi <- which(R[rows[1], ] == 1)
      if (length(Mi) == 0) next
      Oi <- which(R[rows[1], ] == 0); n_pat <- length(rows)
      if (length(Oi) == 0) {
        CM <- matrix(theta$mu, n_pat, length(Mi), byrow = TRUE)
        cc <- theta$Sigma
      } else {
        Soo_inv <- solve(theta$Sigma[Oi, Oi, drop = FALSE])
        reg <- theta$Sigma[Mi, Oi, drop = FALSE] %*% Soo_inv
        cc <- theta$Sigma[Mi, Mi, drop = FALSE] - reg %*% theta$Sigma[Oi, Mi, drop = FALSE]
        Yo_c <- sweep(Z[rows, Oi, drop = FALSE], 2, theta$mu[Oi], FUN = "-")
        CM <- matrix(theta$mu[Mi], n_pat, length(Mi), byrow = TRUE) + Yo_c %*% t(reg)
      }
      Lc <- t(chol(0.5 * (cc + t(cc))))
      E <- matrix(rnorm(n_pat * length(Mi)), n_pat, length(Mi))
      Z[rows, Mi] <- CM + E %*% t(Lc)
    }
    out[[m]] <- Z
  }
  return(out)
}

run_one <- function(r) {
  set.seed(20260522 + r)
  X <- gen_data(200, default_mu, default_Sigma)
  theta_com <- mle_complete_mvn(X); ell_com_com <- loglik_mvn(theta_com, X)
  mar <- apply_mar(X)
  em <- em_mvn(mar$Y); theta_obs <- list(mu = em$mu, Sigma = em$Sigma)
  trRIV_an <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  # exact FITTED value (deterministic)
  barL_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R)
  T_fiml <- barL_fiml - ell_com_com
  # fixed-theta stochastic
  fx <- impute_fixed_theta(mar$Y, theta_obs, M)
  T_fix <- mean(vapply(fx, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  # full conjugate
  cj <- impute_mvn_conjugate(mar$Y, M = M, burnin = 100, thin = 50, theta_init = theta_obs)
  T_full <- mean(vapply(cj$imputed, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  # amelia
  am <- impute_mvn_amelia(mar$Y, M = M)
  T_am <- mean(vapply(am, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  list(trRIV = trRIV_an, T_fiml = T_fiml, T_fix = T_fix, T_full = T_full, T_am = T_am)
}

cl <- makeCluster(10)
clusterEvalQ(cl, { source("verification/00-setup.R"); source("verification/da-conjugate-engine.R") })
clusterExport(cl, c("run_one", "impute_fixed_theta", "M"))
res <- pblapply(seq_len(Rn), run_one, cl = cl)
stopCluster(cl)

g <- function(nm) vapply(res, `[[`, numeric(1), nm)
trRIV <- g("trRIV"); half <- 0.5 * mean(trRIV)
mcse <- function(x) sd(x) / sqrt(length(x))
cat(sprintf("\nR=%d  mean tr(RIV)=%.3f  +1/2=%.3f  -1/2=%.3f\n\n", Rn, mean(trRIV), half, -half))
for (nm in c("T_fiml","T_fix","T_full","T_am")) {
  v <- g(nm)
  cat(sprintf("  %-8s  mean=%+7.3f (MCSE %.3f)\n", nm, mean(v), mcse(v)))
}
cat("\nPaired deviations from the exact FITTED value (T_fiml):\n")
for (nm in c("T_fix","T_full","T_am")) {
  d <- g(nm) - g("T_fiml")
  cat(sprintf("  %-8s - T_fiml : mean=%+7.3f (MCSE %.3f)   [half tr(RIV)=%.3f]\n",
              nm, mean(d), mcse(d), half))
}
