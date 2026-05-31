# 00-test-primitives.R
#
# Smoke tests for the primitives in 00-setup.R. Each block prints PASS/FAIL.
# Run before any pilot or production simulation.
#
# Cost: ~5 seconds. Uses small N, small M for speed; production parameters
# (N=200, M=200, R=1000) are NOT used here.

source("verification/00-setup.R")

set.seed(20260522)

pass <- function(label) {
  cat(sprintf("  PASS  %s\n", label))
}

fail <- function(label, info = "") {
  cat(sprintf("  FAIL  %s  %s\n", label, info))
  stop("smoke test failed")
}

check <- function(cond, label, info = "") {
  if (isTRUE(cond)) { pass(label) } else { fail(label, info) }
}

cat("\n--- vech / invvech ---\n")
M0 <- matrix(c(1, 2, 3, 2, 4, 5, 3, 5, 6), 3, 3)
v <- vech(M0)
check(length(v) == 6, "vech length")
check(all(invvech(v, 3) == M0), "invvech roundtrip")

cat("\n--- theta_to_vec / vec_to_theta ---\n")
theta0 <- list(mu = c(1, 2, 3, 4), Sigma = default_Sigma)
v_theta <- theta_to_vec(theta0)
check(length(v_theta) == 4 + 10, "theta vec length (p + p(p+1)/2)")
theta_back <- vec_to_theta(v_theta, 4)
check(all(theta_back$mu == theta0$mu), "mu roundtrip")
check(all(theta_back$Sigma == theta0$Sigma), "Sigma roundtrip")

cat("\n--- duplication_matrix ---\n")
Dp <- duplication_matrix(4)
check(all(dim(Dp) == c(16, 10)), "Dp dimension (p^2 x p(p+1)/2)")
v_I <- vech(diag(4))
check(all(Dp %*% v_I == as.vector(diag(4))), "Dp %*% vech(I) = vec(I)")

cat("\n--- gen_data ---\n")
X_big <- gen_data(N = 10000, mu = default_mu, Sigma = default_Sigma)
check(all(dim(X_big) == c(10000, 4)), "gen_data shape")
check(max(abs(colMeans(X_big) - default_mu)) < 0.05, "sample mean near truth")
check(max(abs(cov(X_big) - default_Sigma)) < 0.05, "sample cov near truth")

cat("\n--- apply_mar ---\n")
mar_out <- apply_mar(X_big)
check(all(dim(mar_out$Y) == dim(X_big)), "Y shape")
check(all(dim(mar_out$R) == dim(X_big)), "R shape")
check(all(mar_out$R[, 3] == 0), "X_3 fully observed (R_3 = 0)")
check(all(mar_out$R[, 4] == 0), "X_4 fully observed (R_4 = 0)")
miss_rate_1 <- mean(mar_out$R[, 1])
miss_rate_2 <- mean(mar_out$R[, 2])
check(miss_rate_1 > 0.2 && miss_rate_1 < 0.5, "X_1 missing in (0.2, 0.5)")
check(miss_rate_2 > 0.2 && miss_rate_2 < 0.5, "X_2 missing in (0.2, 0.5)")
check(all(is.na(mar_out$Y[mar_out$R == 1])), "NAs match mask")
check(!any(is.na(mar_out$Y[mar_out$R == 0])), "non-NA where mask = 0")
cat(sprintf("    [info] empirical marginal missingness: X_1 = %.3f, X_2 = %.3f\n",
            miss_rate_1, miss_rate_2))
cat("    [info] preregistration §0.2 says ~40% but the formula gives ~32%;\n")
cat("           this is a known doc/formula mismatch flagged in 00-setup.R\n")
cat("           apply_mar() docstring. Amendment to §0.2 to be discussed.\n")

cat("\n--- loglik_mvn ---\n")
ll <- loglik_mvn(theta0, X_big)
ll_manual <- sum(mvtnorm::dmvnorm(X_big, mean = theta0$mu,
                                  sigma = theta0$Sigma, log = TRUE))
check(abs(ll - ll_manual) < 1e-9, "loglik matches manual sum")

cat("\n--- mle_complete_mvn ---\n")
theta_com <- mle_complete_mvn(X_big)
check(max(abs(theta_com$mu - default_mu)) < 0.05, "MLE mu near truth")
check(max(abs(theta_com$Sigma - default_Sigma)) < 0.05, "MLE Sigma near truth")

cat("\n--- mle_with_cov_mvn ---\n")
fit <- mle_with_cov_mvn(X_big)
check(all(dim(fit$U) == c(14, 14)), "U dimension")
eigs <- eigen(fit$U, only.values = TRUE)$values
check(all(eigs > 0), "U positive definite")
check(max(abs(fit$U[1:4, 5:14])) < 1e-12, "mu-Sigma cross-block zero")

cat("\n--- em_mvn (no missingness reduces to complete-data MLE) ---\n")
# Note: norm::em.norm requires at least one NA to operate. Test with 1 NA.
X_small <- gen_data(N = 200, mu = default_mu, Sigma = default_Sigma)
Y_one_na <- X_small
Y_one_na[1, 1] <- NA
em_fit_close <- em_mvn(Y_one_na)
theta_com_small <- mle_complete_mvn(X_small)
diff_mu <- max(abs(em_fit_close$mu - theta_com_small$mu))
diff_sig <- max(abs(em_fit_close$Sigma - theta_com_small$Sigma))
check(diff_mu < 0.1, "EM mu close to complete-data MLE with 1 NA")
check(diff_sig < 0.1, "EM Sigma close to complete-data MLE with 1 NA")

cat("\n--- em_mvn (real MAR missingness) ---\n")
X_med <- gen_data(N = 1000, mu = default_mu, Sigma = default_Sigma)
mar_med <- apply_mar(X_med)
em_fit_real <- em_mvn(mar_med$Y)
diff_mu_em <- max(abs(em_fit_real$mu - default_mu))
diff_sig_em <- max(abs(em_fit_real$Sigma - default_Sigma))
check(diff_mu_em < 0.15, "EM mu within 0.15 of truth at N=1000 with MAR")
check(diff_sig_em < 0.25, "EM Sigma within 0.25 of truth at N=1000 with MAR")

cat("\n--- impute_mvn ---\n")
norm::rngseed(123)
imps <- impute_mvn(mar_med$Y, M = 5, burnin = 50, thin = 20)
check(length(imps) == 5, "M imputations returned")
check(all(sapply(imps, function(Z) { return(!any(is.na(Z))) })),
      "all completed datasets have no NAs")
# Imputations should differ across m (random draws).
diff_across <- max(abs(imps[[1]] - imps[[2]]))
check(diff_across > 0, "imputations differ across m")
# Observed cells should be identical across imputations.
obs_mask <- mar_med$R == 0
check(all(imps[[1]][obs_mask] == imps[[2]][obs_mask]),
      "observed cells preserved across imputations")

cat("\n--- mi_fit_mvn + riv_sample ---\n")
mi_out <- mi_fit_mvn(imps)
check(length(mi_out$theta_imps) == 5, "M theta_imps returned")
check(length(mi_out$U_imps) == 5, "M U_imps returned")
riv_out <- riv_sample(mi_out$theta_imps, mi_out$U_imps)
check(all(dim(riv_out$RIV) == c(14, 14)), "RIV matrix shape")
check(riv_out$tr_RIV > 0, "tr(RIV) positive under missingness")
cat(sprintf("    [info] sample tr(RIV) = %.3f at N=1000, M=5 (single replicate)\n",
            riv_out$tr_RIV))

cat("\n--- fisher_info_obs_mvn (analytic expected Fisher info) ---\n")
# Anchor checks that don't depend on numDeriv (which computes observed
# Hessian, a different estimator that only agrees with expected Fisher info
# in expectation, not realization-by-realization).
#
# Anchor 1: at 0% missingness, the per-pattern sum equals the closed-form
# complete-data Fisher info exactly.
N_fi <- 200
X_fi <- gen_data(N = N_fi, mu = default_mu, Sigma = default_Sigma)
R_zero <- matrix(0, N_fi, 4)
theta_truth <- list(mu = default_mu, Sigma = default_Sigma)
I_obs_nomis <- fisher_info_obs_mvn(theta_truth, X_fi, R_zero)
I_com_truth <- fisher_info_com_mvn(theta_truth, N_fi)
check(max(abs(I_obs_nomis - I_com_truth)) < 1e-9,
      "at 0% missingness, analytic obs info == complete-data info")

# Anchor 2: I_com - I_obs is positive semi-definite (missing information
# can only ADD information to "complete"; it must be a PSD matrix).
mar_fi <- apply_mar(X_fi)
em_fi <- em_mvn(mar_fi$Y)
theta_fi <- list(mu = em_fi$mu, Sigma = em_fi$Sigma)
I_obs_partial <- fisher_info_obs_mvn(theta_fi, mar_fi$Y, mar_fi$R)
I_com_partial <- fisher_info_com_mvn(theta_fi, N_fi)
I_mis <- I_com_partial - I_obs_partial
eigs_mis <- eigen(I_mis, symmetric = TRUE, only.values = TRUE)$values
check(min(eigs_mis) > -1e-9,
      sprintf("I_com - I_obs PSD (min eig %.2e)", min(eigs_mis)))

# Anchor 3: tr(RIV) > 0 under missingness.
tr_riv_val <- sum(diag(solve(I_obs_partial, I_com_partial))) - 14
check(tr_riv_val > 0,
      sprintf("analytic tr(RIV) = %.3f > 0 under MAR missingness", tr_riv_val))

cat("\n--- observed_info_obs_mvn (analytic observed info = numerical Hessian) ---\n")
set.seed(20260522 + 7)
X_oi <- gen_data(500, default_mu, default_Sigma)
mar_oi <- apply_mar(X_oi)
fit_oi <- lavaan_fit_mvn_fiml(mar_oi$Y, constrained = FALSE)
theta_oi <- list(mu = fit_oi$mu, Sigma = fit_oi$Sigma)
H_analytic <- observed_info_obs_mvn(theta_oi, mar_oi$Y, mar_oi$R)
check(isSymmetric(round(H_analytic, 8)), "observed info matrix symmetric")
if (requireNamespace("numDeriv", quietly = TRUE)) {
  H_numeric <- -numDeriv::hessian(
    function(v) { return(loglik_obs_mvn(vec_to_theta(v, 4), mar_oi$Y, mar_oi$R)) },
    theta_to_vec(theta_oi))
  rel = max(abs(H_analytic - H_numeric)) / max(abs(H_numeric))
  check(rel < 1e-4,
        sprintf("observed info matches numerical Hessian (rel err = %.1e)", rel))
} else {
  cat("    [skip] numDeriv not installed; analytic-vs-numerical check skipped\n")
}
I_com_oi <- fisher_info_com_mvn(theta_oi, 500)
tr_obs = sum(diag(solve(H_analytic, I_com_oi))) - 14
tr_exp = sum(diag(solve(fisher_info_obs_mvn(theta_oi, mar_oi$Y, mar_oi$R), I_com_oi))) - 14
check(tr_obs > 0, sprintf("observed/sample tr(RIV) = %.3f > 0", tr_obs))
cat(sprintf("    [info] sample/observed RIV = %.3f vs expected RIV = %.3f (Efron-Hinkley gap)\n",
            tr_obs, tr_exp))

cat("\n--- lrt_complete (sanity) ---\n")
# Nested: theta_null fixes sigma_12 = 0; theta_full is unrestricted MLE.
theta_null_test <- theta_com_small
theta_null_test$Sigma[1, 2] <- 0
theta_null_test$Sigma[2, 1] <- 0
lrt <- lrt_complete(theta_com_small, theta_null_test, X_small)
check(lrt >= -1e-9, "LRT non-negative (full fits at least as well)")
cat(sprintf("    [info] complete-data LRT for sigma_12 = 0: %.3f\n", lrt))

cat("\nAll smoke tests PASSED.\n")
