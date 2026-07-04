source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")
set.seed(20260522 + 1)
X <- gen_data(200, default_mu, default_Sigma)
theta_com <- mle_complete_mvn(X)
ell_com_com <- loglik_mvn(theta_com, X)
mar <- apply_mar(X)
em <- em_mvn(mar$Y); theta_obs <- list(mu = em$mu, Sigma = em$Sigma)
ell_com_obs <- loglik_mvn(theta_obs, X)
cat(sprintf("theta_obs mu1=%.3f sigma11=%.3f ; miss X1=%d X2=%d\n",
            theta_obs$mu[1], theta_obs$Sigma[1,1], sum(mar$R[,1]), sum(mar$R[,2])))

# True conditional mean/var of the missing X1 given observed (at theta_obs) for a
# reference: how dispersed SHOULD proper imputations be?
mi1 <- which(mar$R[,1] == 1)

diag_engine <- function(imps, label) {
  barL <- vapply(imps, function(Z) loglik_mvn(theta_obs, Z), numeric(1))
  # imputed X1 values across imputations: matrix (n_miss1 x M)
  impX1 <- sapply(imps, function(Z) Z[mi1, 1])
  # per-cell: mean across M (should ~ conditional mean), sd across M (within+param)
  cell_mean <- rowMeans(impX1); cell_sd <- apply(impX1, 1, sd)
  # true values at those cells
  truth1 <- X[mi1, 1]
  fits <- lapply(imps, mle_with_cov_mvn)
  mu1_hat <- sapply(fits, function(f) f$theta$mu[1])
  s11_hat <- sapply(fits, function(f) f$theta$Sigma[1,1])
  cat(sprintf("\n[%s]\n", label))
  cat(sprintf("  barL: mean=%.3f  A=barL-ell_com_obs=%.3f  (pred tr(RIV))\n",
              mean(barL), mean(barL) - ell_com_obs))
  cat(sprintf("  imputed X1: cell-mean vs truth  RMSE=%.3f  bias=%.3f\n",
              sqrt(mean((cell_mean - truth1)^2)), mean(cell_mean - truth1)))
  cat(sprintf("  imputed X1: mean within-cell sd across M = %.3f (dispersion)\n",
              mean(cell_sd)))
  cat(sprintf("  imputed X1 grand mean=%.3f (truth mean=%.3f, obs-cell truth mean=%.3f)\n",
              mean(impX1), mean(truth1), mean(truth1)))
  cat(sprintf("  theta_hat across M: mu1 mean=%.3f sd=%.3f ; s11 mean=%.3f sd=%.3f\n",
              mean(mu1_hat), sd(mu1_hat), mean(s11_hat), sd(s11_hat)))
}

set.seed(20260522 + 1)  # reset so amelia/conjugate see same RNG start as spike
cj <- impute_mvn_conjugate(mar$Y, M = 50, burnin = 100, thin = 50, theta_init = theta_obs)
diag_engine(cj$imputed, "conjugate DA")

am <- impute_mvn_amelia(mar$Y, M = 50)
diag_engine(am, "amelia EMB")

cat(sprintf("\nell_com_at_obs=%.3f  ell_com_at_com=%.3f\n", ell_com_obs, ell_com_com))
