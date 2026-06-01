# scratch-sanity-var.R [EXPLORATORY] — sanity: N*bias of fully-observed variance MLE = -1.0
source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
mu0 <- default_mu; Sig0 <- default_Sigma
n_cores = 20; R = 40000
one <- function(r, N) { set.seed(20260601 + r); X <- gen_data(N, mu0, Sig0); x1 <- X[, 1]; return(mean((x1 - mean(x1))^2) - 1) }
cl <- makeCluster(n_cores)
on.exit({ try(stopCluster(cl), silent = TRUE) }, add = TRUE)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R") }))
clusterExport(cl, c("mu0", "Sig0", "one"))
for (N in c(200, 800)) {
  clusterExport(cl, "N")
  v <- unlist(parLapply(cl, seq_len(R), function(r) { return(one(r, N)) }))
  cat(sprintf("N=%d  N*bias(sigma11 MLE, fully observed) = %+.4f (mcse %.4f)  [expect -1.0]\n",
              N, N * mean(v), N * sd(v) / sqrt(length(v))))
}
