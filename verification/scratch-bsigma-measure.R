# scratch-bsigma-measure.R  [EXPLORATORY — Phase 3a, todo/010]
#
# Step 2: directly measure b_Sigma = lim N*E[Sigma_hat_obs - Sigma_0] under the 4-step
# monotone MAR pattern, using the fast closed-form factored MLE (validated vs lavaan in
# scratch-bsigma-monotone.R). High R is affordable because the MLE is ~100x faster than
# lavaan. Reports N*bias per Sigma element across N to confirm O(1/N) (N*bias stable) and
# to expose the structure the analytic delta-method formula must reproduce.
#
# Usage: Rscript verification/scratch-bsigma-measure.R [R] [n_cores]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_arg   = if (length(args) >= 1) { as.integer(args[1]) } else { 200000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }

mu0 <- default_mu
Sig0 <- default_Sigma
p = length(mu0)
Ngrid <- c(200, 400, 800)

fiml_monotone_kstep <- function(Y, R) {
  p = ncol(Y)
  obs_through <- function(j) {
    if (j == 1) { return(R[, 1] == 0) }
    return(rowSums(R[, 1:j, drop = FALSE]) == 0)
  }
  mu <- numeric(p)
  Sigma <- matrix(0, p, p)
  s1 <- obs_through(1)
  x1 <- Y[s1, 1]
  mu[1] = mean(x1)
  Sigma[1, 1] = mean((x1 - mu[1])^2)
  for (j in 2:p) {
    sj <- obs_through(j)
    Xpred <- cbind(1, Y[sj, 1:(j - 1), drop = FALSE])
    yj <- Y[sj, j]
    coef <- solve(crossprod(Xpred), crossprod(Xpred, yj))
    b_j <- coef[-1]
    resid <- yj - Xpred %*% coef
    v_j = mean(resid^2)
    Sig_prev <- Sigma[1:(j - 1), 1:(j - 1), drop = FALSE]
    mu[j] = coef[1] + sum(b_j * mu[1:(j - 1)])
    Sigma[j, 1:(j - 1)] <- as.numeric(b_j %*% Sig_prev)
    Sigma[1:(j - 1), j] <- Sigma[j, 1:(j - 1)]
    Sigma[j, j] = v_j + as.numeric(b_j %*% Sig_prev %*% b_j)
  }
  return(list(mu = mu, Sigma = Sigma))
}

one_rep <- function(r, N) {
  set.seed(20260601 + r)
  X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "monotone"),
                  error = function(e) { return(NULL) })
  if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(fiml_monotone_kstep(mar$Y, mar$R), error = function(e) { return(NULL) })
  if (is.null(fit)) { return(NULL) }
  vechS <- fit$Sigma[lower.tri(fit$Sigma, diag = TRUE)]
  return(c(fit$mu - mu0, vechS - Sig0[lower.tri(Sig0, diag = TRUE)]))
}

cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "p", "fiml_monotone_kstep", "one_rep"))

lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)
sig_lab <- sprintf("s%d%d", lt[, 1], lt[, 2])
labels <- c(sprintf("mu%d", 1:p), sig_lab)

cat(sprintf("\n== b_Sigma measurement: N*E[theta_hat - theta_0], monotone MAR, R=%d ==\n", R_arg))
cat(sprintf("%-6s", "param"))
for (N in Ngrid) { cat(sprintf("  %10s", sprintf("N=%d", N))) }
cat("   (N*bias; stable => O(1/N))\n")

res_by_N <- list()
for (N in Ngrid) {
  clusterExport(cl, "N")
  M <- do.call(rbind, Filter(Negate(is.null),
         parLapply(cl, seq_len(R_arg), function(r) { return(one_rep(r, N)) })))
  res_by_N[[as.character(N)]] <- list(nbias = N * colMeans(M), nmcse = N * apply(M, 2, sd) / sqrt(nrow(M)), nok = nrow(M))
}
for (i in seq_along(labels)) {
  cat(sprintf("%-6s", labels[i]))
  for (N in Ngrid) { cat(sprintf("  %+10.4f", res_by_N[[as.character(N)]]$nbias[i])) }
  cat("\n")
}
cat("\nmcse (N=800 column):\n  ")
for (i in seq_along(labels)) { cat(sprintf("%s=%.3f ", labels[i], res_by_N[["800"]]$nmcse[i])) }
cat(sprintf("\n  n_ok(N=800)=%d\n", res_by_N[["800"]]$nok))
