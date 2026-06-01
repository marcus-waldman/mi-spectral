# scratch-sanity-seed.R [EXPLORATORY] — is consecutive per-rep seeding biasing/distorting MC?
# Compare N*bias of fully-observed variance MLE under (a) one continuous RNG stream vs
# (b) the repo's set.seed(base+r) per rep. Both must give -1.0 in expectation.
N = 800; R = 40000
# (a) single continuous stream
set.seed(1)
v_single <- numeric(R)
for (r in seq_len(R)) { x <- rnorm(N); v_single[r] <- mean((x - mean(x))^2) - 1 }
cat(sprintf("(a) single stream : N*bias = %+.4f (mcse %.4f)  [expect -1.0]\n",
            N * mean(v_single), N * sd(v_single) / sqrt(R)))
# (b) consecutive per-rep seeds (repo convention)
v_consec <- numeric(R)
for (r in seq_len(R)) { set.seed(20260601 + r); x <- rnorm(N); v_consec[r] <- mean((x - mean(x))^2) - 1 }
cat(sprintf("(b) consec seeds  : N*bias = %+.4f (mcse %.4f)  [expect -1.0]\n",
            N * mean(v_consec), N * sd(v_consec) / sqrt(R)))
# (c) consecutive seeds but using mvtnorm::rmvnorm (as gen_data does)
suppressPackageStartupMessages({ library(mvtnorm) })
S1 <- diag(4); mu0 <- rep(0, 4)
v_rmv <- numeric(R)
for (r in seq_len(R)) { set.seed(20260601 + r); X <- rmvnorm(N, mu0, S1); x <- X[, 1]; v_rmv[r] <- mean((x - mean(x))^2) - 1 }
cat(sprintf("(c) consec+rmvnorm: N*bias = %+.4f (mcse %.4f)  [expect -1.0]\n",
            N * mean(v_rmv), N * sd(v_rmv) / sqrt(R)))
