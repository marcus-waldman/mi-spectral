# scratch-bsigma-monotone.R  [EXPLORATORY — Phase 3a, todo/010]
#
# Step 1 of the closed-form general-MVN (A)+(C): validate the fast closed-form
# 4-step monotone (factored/sweep) MLE against lavaan FIML, and confirm the
# ampute "monotone" pattern is a clean nested pattern (obs sets {1}<{1,2}<{1,2,3}<{1,2,3,4}).
#
# The fast factored MLE is ~100x faster than lavaan FIML, which is what lets us
# measure the O(1/N) covariance bias b_Sigma at the high R needed (N*bias needs
# R ~ 800N to resolve). This script only checks the MLE matches lavaan; the
# b_Sigma measurement + analytic formula come next.
#
# Usage: Rscript verification/scratch-bsigma-monotone.R [N]

source("verification/00-setup.R")
args <- commandArgs(trailingOnly = TRUE)
N_arg = if (length(args) >= 1) { as.integer(args[1]) } else { 200000 }

mu0 <- default_mu
Sig0 <- default_Sigma
p = length(mu0)

# ---- closed-form k-step monotone MLE (nesting order 1,2,...,p) -------------------------
# Assumes a monotone pattern with observation nested in the natural order: unit observed
# through step j has X_1..X_j present. Step j regresses X_j on X_1..X_{j-1} (intercept +
# slopes) by OLS on the r_j units observed through j; residual variance is the MLE (/r_j).
# Reconstructs (mu, Sigma) by the inverse-sweep:
#   Sigma_{j,<j} = b_j Sigma_{<j,<j},   Sigma_jj = v_j + b_j Sigma_{<j,<j} b_j^T.
fiml_monotone_kstep <- function(Y, R) {
  p = ncol(Y)
  obs_through <- function(j) {
    # units with X_1..X_j all observed (R==0). Nested => equals X_j observed under monotone.
    if (j == 1) { return(R[, 1] == 0) }
    return(rowSums(R[, 1:j, drop = FALSE]) == 0)
  }
  mu <- numeric(p)
  Sigma <- matrix(0, p, p)
  # step 1: marginal X_1
  s1 <- obs_through(1)
  x1 <- Y[s1, 1]
  mu[1] = mean(x1)
  Sigma[1, 1] = mean((x1 - mu[1])^2)
  for (j in 2:p) {
    sj <- obs_through(j)
    Xpred <- cbind(1, Y[sj, 1:(j - 1), drop = FALSE])   # r_j x j (intercept + predictors)
    yj <- Y[sj, j]
    coef <- solve(crossprod(Xpred), crossprod(Xpred, yj))  # (intercept, slopes)
    a_j = coef[1]
    b_j <- coef[-1]                                          # length j-1 slope vector
    resid <- yj - Xpred %*% coef
    v_j = mean(resid^2)                                      # residual-variance MLE (/r_j)
    Sig_prev <- Sigma[1:(j - 1), 1:(j - 1), drop = FALSE]
    mu[j] = a_j + sum(b_j * mu[1:(j - 1)])
    Sigma[j, 1:(j - 1)] <- as.numeric(b_j %*% Sig_prev)
    Sigma[1:(j - 1), j] <- Sigma[j, 1:(j - 1)]
    Sigma[j, j] = v_j + as.numeric(b_j %*% Sig_prev %*% b_j)
  }
  return(list(mu = mu, Sigma = Sigma))
}

# ---- confirm pattern nesting + complete cases -----------------------------------------
set.seed(20260601)
X <- gen_data(N_arg, mu0, Sig0)
mar <- apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone")
Y <- mar$Y
R <- mar$R
patt <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
cat(sprintf("\n== monotone MAR pattern frequencies (N=%d) ==\n", N_arg))
tab <- sort(table(patt), decreasing = TRUE)
for (nm in names(tab)) {
  cat(sprintf("  R=%s  (obs cols %s)  n=%d  frac=%.4f\n",
              nm, paste(which(strsplit(nm, "")[[1]] == "0"), collapse = ","),
              tab[[nm]], tab[[nm]] / N_arg))
}

# per-step observed counts r_j (units with X_1..X_j all observed)
cat("\n  per-step r_j / N (units observed through step j):\n")
for (j in 1:p) {
  rj = if (j == 1) { sum(R[, 1] == 0) } else { sum(rowSums(R[, 1:j, drop = FALSE]) == 0) }
  cat(sprintf("    step %d: r_%d/N = %.4f\n", j, j, rj / N_arg))
}

# ---- compare closed-form monotone MLE vs lavaan FIML ----------------------------------
fit_fast <- fiml_monotone_kstep(Y, R)
fit_lav  <- lavaan_fit_mvn_fiml(Y, FALSE)
cat("\n== closed-form monotone MLE vs lavaan FIML ==\n")
cat(sprintf("  max|Sigma_fast - Sigma_lavaan| = %.3e\n", max(abs(fit_fast$Sigma - fit_lav$Sigma))))
cat(sprintf("  max|mu_fast    - mu_lavaan|    = %.3e\n", max(abs(fit_fast$mu - fit_lav$mu))))
cat(sprintf("  (at this huge N, both ~ Sigma0; max|Sigma_fast - Sigma0| = %.3e)\n",
            max(abs(fit_fast$Sigma - Sig0))))
