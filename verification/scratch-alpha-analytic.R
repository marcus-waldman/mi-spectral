# scratch-alpha-analytic.R  [EXPLORATORY — Phase 3a, todo/010]
#
# A2: validate the analytic entropy gradient alpha = grad_theta A|_{theta_0} against the
# finite-difference g_bar from the harness. Derived form (per missing unit i, pattern M|O):
# at theta_0 the quadratic (m_0 - m_theta) factor vanishes, leaving
#   alpha_a = -1/2 * sum_{i:mis} tr( S0_i^{-1} dS_i[E_a] ),
# where S_i = Sigma_{MM} - Sigma_{MO} Sigma_{OO}^{-1} Sigma_{OM} (Schur complement, Sigma-only
# => alpha is COV-ONLY, alpha_mu = 0), E_a is the symmetric perturbation of the a-th packed
# Sigma parameter (lower-tri incl diag; off-diagonals perturb (i,j) and (j,i) together to match
# A_of_par's unpack), and
#   dS[dSigma] = dMM - dMO B^T - B dOM + B dOO B^T,   B = Sigma_{MO} Sigma_{OO}^{-1}.
# alpha per unit is DETERMINISTIC (no y dependence) => alpha = sum_patterns n_pat * alpha_pat.
#
# Usage: Rscript verification/scratch-alpha-analytic.R [N] [R] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
N_arg   = if (length(args) >= 1) { as.integer(args[1]) } else { 500 }
R_arg   = if (length(args) >= 2) { as.integer(args[2]) } else { 300 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

mu0 <- default_mu; Sig0 <- default_Sigma; p = length(mu0)
k = p + p * (p + 1) / 2
theta0 <- list(mu = mu0, Sigma = Sig0)
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)   # (k-p) x 2 rows: Sigma param (row,col)

pack <- function(theta) { return(c(theta$mu, theta$Sigma[lower.tri(theta$Sigma, diag = TRUE)])) }
unpack <- function(par) {
  mu <- par[1:p]; S <- matrix(0, p, p)
  S[lower.tri(S, diag = TRUE)] <- par[(p + 1):k]; S[upper.tri(S)] <- t(S)[upper.tri(S)]
  return(list(mu = mu, Sigma = S))
}
par0 <- pack(theta0)
A_of_par <- function(par, Y, R) {
  th <- unpack(par)
  return(barQ_fiml_analytic(th, th, Y, R) - barQ_fiml_analytic(th, theta0, Y, R))
}
grad_A <- function(Y, R, h = 1e-3) {
  g <- numeric(k)
  for (i in 1:k) { ei <- numeric(k); ei[i] <- h; g[i] <- (A_of_par(par0 + ei, Y, R) - A_of_par(par0 - ei, Y, R)) / (2 * h) }
  return(g)
}

# symmetric perturbation matrix for packed Sigma-parameter index s (1..k-p)
Epert <- function(s) {
  i = lt[s, 1]; j = lt[s, 2]; E <- matrix(0, p, p)
  E[i, j] <- 1; E[j, i] <- 1                  # diagonal (i==j) => E[i,i]=1; off-diag => both
  return(E)
}

alpha_analytic <- function(R) {
  patt <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  alpha <- numeric(k)
  for (pp in unique(patt)) {
    rows <- which(patt == pp); n_pat = length(rows); Rp <- R[rows[1], ]
    M <- which(Rp == 1); O <- which(Rp == 0)
    if (length(M) == 0) { next }
    Soo_inv <- solve(Sig0[O, O, drop = FALSE]); B <- Sig0[M, O, drop = FALSE] %*% Soo_inv  # |M| x |O|
    S0 <- Sig0[M, M, drop = FALSE] - B %*% Sig0[O, M, drop = FALSE]
    S0inv <- solve(S0)
    for (s in 1:(k - p)) {
      E <- Epert(s); dMM <- E[M, M, drop = FALSE]; dMO <- E[M, O, drop = FALSE]
      dOM <- E[O, M, drop = FALSE]; dOO <- E[O, O, drop = FALSE]
      dS <- dMM - dMO %*% t(B) - B %*% dOM + B %*% dOO %*% t(B)
      alpha[p + s] <- alpha[p + s] - 0.5 * n_pat * sum(diag(S0inv %*% dS))
    }
  }
  return(alpha)
}

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "theta0", "par0", "lt", "pack", "unpack",
                    "A_of_par", "grad_A", "Epert", "alpha_analytic", "N_arg"))

one <- function(r) {
  set.seed(20260601 + r)
  X <- gen_data(N_arg, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone"), error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  return(list(g = grad_A(mar$Y, mar$R), a = alpha_analytic(mar$R)))
}
res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_arg), one))
g_bar <- Reduce(`+`, lapply(res, `[[`, "g")) / length(res)
a_bar <- Reduce(`+`, lapply(res, `[[`, "a")) / length(res)

cat(sprintf("\n== analytic alpha vs finite-diff g_bar (monotone MAR, N=%d, R=%d) ==\n", N_arg, R_arg))
cat(sprintf("%-8s %14s %14s %12s\n", "param", "g_bar(numeric)", "alpha(analytic)", "diff"))
labels <- c(sprintf("mu%d", 1:p), sprintf("s%d%d", lt[, 1], lt[, 2]))
for (i in 1:k) { cat(sprintf("%-8s %+14.4f %+14.4f %+12.5f\n", labels[i], g_bar[i], a_bar[i], a_bar[i] - g_bar[i])) }
cat(sprintf("\n  max|alpha - g_bar| = %.4e   max|alpha_mu| = %.2e (expect 0)\n",
            max(abs(a_bar - g_bar)), max(abs(a_bar[1:p]))))
