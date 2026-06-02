# scratch-bcov-check.R  [todo/015 / todo/016 — GPT-5.5 Layer-3 catch]
#
# DECISIVE check of the GPT-5.5 adversarial finding: the leading-order (A)+(C) has a THIRD
# O(1) term under MAR that the two-term assembly (alpha^T E[delta] + 1/2 tr(H_phi I_obs^-1))
# dropped. Mode A's form:
#   E[g^T delta] = E[g]^T E[delta]  +  tr( I_obs^{-1} Cov(S_obs, g) ),
#   g = grad_phi F(theta0,phi)|theta0  (entropy gradient),  S_obs = grad_theta ell_obs|theta0.
# The first piece is (A)=B_bias (already computed); the second, B_cov, is the missed term:
# zero under MCAR (S_obs independent of the pattern-driven g), nonzero under MAR.
#
# Test: does (A)+(C)+B_cov reproduce the empirical -0.46 (non-monotone)? And B_cov -> 0 (MCAR)?
# Also checks E[S_obs] ~ 0 (ignorability) and the magnitude of E[C]-vs-RIV (Mode B's Delta).

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel); library(jsonlite) })
args <- commandArgs(trailingOnly = TRUE)
R_data  = if (length(args) >= 1) { as.integer(args[1]) } else { 400 }
N_use   = if (length(args) >= 2) { as.integer(args[2]) } else { 1500 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }

p = 4; mu0 <- default_mu; Sig0 <- default_Sigma; k = p + p * (p + 1) / 2
TRUTH <- list(mu = mu0, Sigma = Sig0)
gp <- jsonlite::fromJSON("verification/cache/coxsnell-nonmonotone-bsigma-genp4.json")
bvech <- as.numeric(gp[["beta0.0"]]$b_sigma_vech)
v0 <- c(mu0, Sig0[lower.tri(Sig0, diag = TRUE)]); hstep = 1e-4

amp_mar  <- function(X) { return(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone")) }
NMP <- rbind(c(1,0,0,0), c(0,1,0,0), c(1,1,0,0)); NMF <- c(1,1,1)/3; PI = 0.60
amp_mcar <- function(X) { N <- nrow(X); a <- runif(N) < PI; Y <- X; R <- matrix(0,N,p); idx <- which(a)
  if (length(idx)) { pat <- sample.int(3, length(idx), TRUE, NMF)
    for (t in 1:3) { ii <- idx[pat==t]; mc <- which(NMP[t,]==1); if (length(ii)) { Y[ii,mc] <- NA; R[ii,mc] <- 1 } } }
  return(list(Y=Y, R=R)) }

vec2theta <- function(v) { S <- matrix(0,p,p); S[lower.tri(S,diag=TRUE)] <- v[(p+1):k]
  S[upper.tri(S)] <- t(S)[upper.tri(S)]; return(list(mu=v[1:p], Sigma=S)) }

one <- function(seed, N, amp_fun) {
  set.seed(seed); X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(amp_fun(X), error=function(e) NULL); if (is.null(mar)) { return(NULL) }
  Y <- mar$Y; R <- mar$R
  # g = grad_phi barQ(theta0, phi)|theta0 (impute slot)
  g <- numeric(k)
  for (i in 1:k) { vp <- v0; vp[i] <- vp[i]+hstep; vm <- v0; vm[i] <- vm[i]-hstep
    g[i] <- (barQ_fiml_analytic(TRUTH, vec2theta(vp), Y, R) - barQ_fiml_analytic(TRUTH, vec2theta(vm), Y, R))/(2*hstep) }
  # S_obs = grad_theta ell_obs(theta)|theta0
  S <- numeric(k)
  for (i in 1:k) { vp <- v0; vp[i] <- vp[i]+hstep; vm <- v0; vm[i] <- vm[i]-hstep
    S[i] <- (loglik_obs_mvn(vec2theta(vp), Y, R) - loglik_obs_mvn(vec2theta(vm), Y, R))/(2*hstep) }
  Iobs <- observed_info_obs_mvn(TRUTH, Y, R)
  return(list(g=g, S=S, Sg=outer(S, g), Iobs=Iobs))
}

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, source("verification/00-setup.R")))
clusterExport(cl, c("mu0","Sig0","p","k","TRUTH","v0","hstep","vec2theta","one","amp_mar","amp_mcar","NMP","NMF","PI"))

run <- function(N, amp_fun, label) {
  res <- Filter(Negate(is.null), parLapply(cl, seq_len(R_data), function(s, NN, af) one(20260602+s, NN, af),
                                           NN=N, af=amp_fun))
  ng <- length(res)
  G  <- Reduce(`+`, lapply(res, `[[`, "g")) / ng
  Sm <- Reduce(`+`, lapply(res, `[[`, "S")) / ng
  Sg <- Reduce(`+`, lapply(res, `[[`, "Sg")) / ng
  Iobs <- Reduce(`+`, lapply(res, `[[`, "Iobs")) / ng
  Cov <- Sg - outer(Sm, G)                 # Cov(S_obs, g)
  Iinv <- solve(Iobs)
  Bcov <- sum(diag(Iinv %*% Cov))
  Bbias <- sum(G * c(numeric(p), bvech) / N)   # = (A) recomputed = E[g]^T E[delta]
  cat(sprintf("\n-- %s (N=%d, %d datasets) --\n", label, N, ng))
  cat(sprintf("   E[S_obs] max|.| = %.2e  (ignorability: ~0)\n", max(abs(Sm))))
  cat(sprintf("   B_bias = E[g]^T E[delta] = %+.4f   (the (A) term)\n", Bbias))
  cat(sprintf("   B_cov  = tr(I_obs^-1 Cov(S_obs,g)) = %+.4f   <-- GPT-5.5's missed term\n", Bcov))
  return(c(Bbias=Bbias, Bcov=Bcov))
}

cat("============ B_cov verification (GPT-5.5 Layer-3 catch) ============\n")
cat(sprintf("(A)=+0.778  (C)=-0.998  [from verify_term_ac_nonmonotone_4v.R]; empirical D: -0.336(800) -> -0.456(1500)\n"))
A = 0.778; C = -0.998
mar_n <- run(N_use, amp_mar, "MAR non-monotone")
cat(sprintf("   => (A)+(C)+B_cov = %+.4f  vs empirical -0.456   [%s]\n",
            A + C + mar_n["Bcov"], if (abs(A+C+mar_n["Bcov"] - (-0.456)) < 0.06) { "MATCH -- three-term closes the gap" } else { "partial" }))
mcar_n <- run(N_use, amp_mcar, "MCAR control")
cat(sprintf("   => B_cov(MCAR) = %+.4f  (should be ~0)\n", mcar_n["Bcov"]))
stopCluster(cl)
cat("====================================================================\n")
