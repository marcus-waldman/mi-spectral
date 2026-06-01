# scratch-bsigma-analytic.R  [EXPLORATORY — Phase 3a, todo/010]
#
# Step 3: analytic b_Sigma = lim N*E[Sigma_hat_obs - Sigma_0] for the 4-step monotone MAR
# pattern, via the per-step recursion (cross-step covariances vanish because each step's OLS
# slope is conditionally unbiased given the conditioning variables, and Sigma_hat_{<j} is a
# function of those variables only => Cov(beta_hat_j, Sigma_hat_{<j}) = 0):
#
#   b[1,1]       = -sigma_11
#   for j>=2, P = 1:(j-1):
#     b[j,P]     = b_j %*% b[P,P]                          (slope-propagated cov-block bias)
#     b[j,j]     = -(j/f_j) sigma_{jj.<j}                  (residual-variance MLE bias)
#                  + b_j %*% b[P,P] %*% t(b_j)             (recursive predictor-block bias)
#                  + (sigma_{jj.<j}/f_j) tr(Sigma_PP (Sigma_PP^{(j)})^{-1})  (slope-variance back-transform)
#
# where f_j = E[r_j]/N and Sigma_PP^{(j)} = Cov(X_P | observed through step j) is the selected
# (design-imbalanced) predictor covariance. Under MCAR Sigma_PP^{(j)}=Sigma_PP => tr=(j-1).
# Prints vech(b_Sigma) to compare with the direct measurement (scratch-bsigma-measure.R).
#
# Usage: Rscript verification/scratch-bsigma-analytic.R [N_sel] [R_sel]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
N_sel = if (length(args) >= 1) { as.integer(args[1]) } else { 20000 }
R_sel = if (length(args) >= 2) { as.integer(args[2]) } else { 400 }

mu0 <- default_mu
Sig0 <- default_Sigma
p = length(mu0)

# ---- estimate selected design moments f_j and Sigma_PP^{(j)} at theta_0 ----------------
# Pool over R_sel datasets: for each step j, accumulate centered 2nd-moment of X_P among
# units observed through step j, and the observed fraction f_j. These are O(1)-stable.
est_selected_moments <- function(N_sel, R_sel) {
  sums_xpxp <- vector("list", p)   # sum over selected units of x_P x_P^T (uncentered)
  sums_xp   <- vector("list", p)   # sum over selected units of x_P
  counts    <- numeric(p)
  for (j in 1:p) { sums_xpxp[[j]] <- matrix(0, p, p); sums_xp[[j]] <- numeric(p) }
  for (r in 1:R_sel) {
    set.seed(77000 + r)
    X <- gen_data(N_sel, mu0, Sig0)
    mar <- apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone")
    Rm <- mar$R
    for (j in 1:p) {
      sel = if (j == 1) { Rm[, 1] == 0 } else { rowSums(Rm[, 1:j, drop = FALSE]) == 0 }
      counts[j] = counts[j] + sum(sel)
      if (j >= 2) {
        Xp <- X[sel, 1:(j - 1), drop = FALSE]
        sums_xpxp[[j]][1:(j - 1), 1:(j - 1)] <- sums_xpxp[[j]][1:(j - 1), 1:(j - 1)] + crossprod(Xp)
        sums_xp[[j]][1:(j - 1)] <- sums_xp[[j]][1:(j - 1)] + colSums(Xp)
      }
    }
  }
  f <- counts / (N_sel * R_sel)
  Spp_sel <- vector("list", p)
  for (j in 2:p) {
    n_j = counts[j]
    P = 1:(j - 1)
    mxx <- sums_xpxp[[j]][P, P, drop = FALSE] / n_j
    mx  <- sums_xp[[j]][P] / n_j
    Spp_sel[[j]] <- mxx - outer(mx, mx)   # selected (design-imbalanced) Cov(X_P)
  }
  return(list(f = f, Spp_sel = Spp_sel))
}

cat(sprintf("\n== analytic b_Sigma (monotone MAR), selected moments from N_sel=%d x R_sel=%d ==\n",
            N_sel, R_sel))
sm <- est_selected_moments(N_sel, R_sel)
f <- sm$f
cat(sprintf("  f_j (observed-through-j fractions): %s\n",
            paste(sprintf("f%d=%.4f", 1:p, f), collapse = "  ")))

# ---- b_Sigma recursion ----------------------------------------------------------------
bSig <- matrix(0, p, p)
bSig[1, 1] = -Sig0[1, 1]
for (j in 2:p) {
  P = 1:(j - 1)
  Spp <- Sig0[P, P, drop = FALSE]
  b_j <- Sig0[j, P, drop = FALSE] %*% solve(Spp)            # 1 x (j-1) population slopes
  sig_cond = as.numeric(Sig0[j, j] - b_j %*% Sig0[P, j])    # sigma_{jj.<j}
  bSpp <- bSig[P, P, drop = FALSE]
  bSig[j, P] <- b_j %*% bSpp
  bSig[P, j] <- t(bSig[j, P, drop = FALSE])
  var_term = (sig_cond / f[j]) * sum(diag(Spp %*% solve(sm$Spp_sel[[j]])))
  bSig[j, j] = -(j / f[j]) * sig_cond + as.numeric(b_j %*% bSpp %*% t(b_j)) + var_term
}

lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
cat("\n  analytic b_Sigma (vech, to compare with N*bias measurement):\n")
for (i in seq_len(nrow(lt))) {
  cat(sprintf("    s%d%d = %+.4f\n", lt[i, 1], lt[i, 2], bSig[lt[i, 1], lt[i, 2]]))
}
cat(sprintf("\n  per-step sigma_{jj.<j}: %s\n",
            paste(sapply(2:p, function(j) {
              P = 1:(j - 1); b_j <- Sig0[j, P, drop = FALSE] %*% solve(Sig0[P, P, drop = FALSE])
              sprintf("s_%d.<%d=%.4f", j, j, as.numeric(Sig0[j, j] - b_j %*% Sig0[P, j]))
            }), collapse = "  ")))
