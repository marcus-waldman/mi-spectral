# phase0a-calibrated.R — the discriminating test for Spec 1 vs Spec 2.
# The R=20000 cache already showed: calibrating the exact DA (deflate mean ->
# Gaussianize shape) collapses -0.77 down to the correctly-centered proper
# baseline (amelia -0.069, gauss -0.104 BELOW the +1/2 headline at N=200).
# Remaining question: does that small correctly-centered residual PERSIST or
# VANISH with N? Persist => genuine small proper-vs-headline gap (Spec 2);
# vanish => proper MI = +1/2 asymptotically (paper exactly right, Spec 1 only).
#
# Engines: amelia (bootstrap) + gauss (Laplace N(theta_obs, I_obs^-1)) — the two
# correctly-centered proper imputers — plus conjugate (Jeffreys IW) as the anchor
# at N=200. All reported HEADLINE-relative: (T - 1/2 tr(RIV))/tr(RIV).
#
# Run: Rscript verification/spikes/phase0a-calibrated.R [ncores]

source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")
suppressPackageStartupMessages({ library(parallel); library(pbapply) })

args   <- commandArgs(trailingOnly = TRUE)
ncores <- if (length(args) >= 1) as.integer(args[1]) else 20
Rsmoke <- if (length(args) >= 2) as.integer(args[2]) else 0
M <- 50
R_by_N <- c(`200`=8000, `500`=6000, `1000`=4000, `2000`=3000)
if (Rsmoke > 0) R_by_N[] <- Rsmoke

impute_gauss_post <- function(Y, R, theta_obs, M) {
  N <- nrow(Y); p <- ncol(Y); vobs <- theta_to_vec(theta_obs)
  Vpost <- solve(fisher_info_obs_mvn(theta_obs, Y, R)); Lp <- t(chol(0.5*(Vpost+t(Vpost))))
  patterns <- apply(R,1,paste,collapse=""); upat <- unique(patterns); out <- vector("list", M); m <- 0
  while (m < M) {
    th <- vec_to_theta(vobs + as.numeric(Lp %*% rnorm(length(vobs))), p)
    if (min(eigen(th$Sigma, symmetric=TRUE, only.values=TRUE)$values) <= 1e-6) next
    m <- m + 1; Z <- Y
    for (pk in upat){ rows<-which(patterns==pk); Mi<-which(R[rows[1],]==1); if(length(Mi)==0)next
      Oi<-which(R[rows[1],]==0); n_pat<-length(rows)
      Soo<-solve(th$Sigma[Oi,Oi,drop=FALSE]); reg<-th$Sigma[Mi,Oi,drop=FALSE]%*%Soo
      cc<-th$Sigma[Mi,Mi,drop=FALSE]-reg%*%th$Sigma[Oi,Mi,drop=FALSE]
      Yo<-sweep(Z[rows,Oi,drop=FALSE],2,th$mu[Oi],"-"); CM<-matrix(th$mu[Mi],n_pat,length(Mi),byrow=TRUE)+Yo%*%t(reg)
      Z[rows,Mi]<-CM+matrix(rnorm(n_pat*length(Mi)),n_pat,length(Mi))%*%t(t(chol(0.5*(cc+t(cc))))) }
    out[[m]]<-Z }
  out
}

# amelia + gauss + conjugate(anchor); report headline-relative and fitted-relative.
run_calib <- function(r, Nn, with_conj=FALSE) {
  set.seed(20260522 + r)
  X <- gen_data(Nn, default_mu, default_Sigma)
  ell_com_com <- loglik_mvn(mle_complete_mvn(X), X)
  mar <- apply_mar(X); em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)
  trRIV <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  T_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ell_com_com
  Tof <- function(imps) mean(vapply(imps, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  am <- impute_mvn_amelia(mar$Y, M); T_am <- Tof(am)
  gp <- impute_gauss_post(mar$Y, mar$R, theta_obs, M); T_gp <- Tof(gp)
  out <- c(trRIV=trRIV, T_fiml=T_fiml, T_am=T_am, T_gp=T_gp)
  if (with_conj) { cj <- impute_mvn_conjugate(mar$Y, M, 100, 40, theta_obs)$imputed
    out <- c(out, T_cj=Tof(cj)) }
  out
}

cl <- makeCluster(ncores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); source("verification/da-conjugate-engine.R"); NULL }))
clusterExport(cl, c("run_calib","impute_gauss_post","M"))
mcse <- function(x) sd(x)/sqrt(length(x))

cat("\n=== Discriminating test: does the correctly-centered proper baseline persist? ===\n")
cat("PRIMARY = FITTED-relative (paired, tight): (T - T_fiml)/tr(RIV)  [proper-vs-FITTED]\n")
cat("Also: (A)+(C)/tr = (T_fiml - 1/2 tr)/tr [design term], and headline-relative for amelia.\n\n")
cat("   N      R    tr(RIV)   amelia-FIT        gauss-FIT         (A)+(C)/tr        amelia-headline\n")
cat("  ---  -----  -------   --------------    --------------    --------------    --------------\n")
res <- list()
for (Nn in c(200, 500, 1000, 2000)) {
  RN <- R_by_N[[as.character(Nn)]]
  wc <- (Nn == 200)                                # conjugate anchor only at N=200
  clusterExport(cl, c("Nn","wc"), envir=environment())
  B <- do.call(rbind, pblapply(seq_len(RN), function(r) run_calib(r, Nn, with_conj=wc), cl=cl))
  tr <- mean(B[,"trRIV"]); fit <- B[,"T_fiml"]
  fr <- function(nm) { d <- (B[,nm]-fit)/tr; c(mean(d), mcse(d)) }          # fitted-relative (paired)
  a <- fr("T_am"); g <- fr("T_gp")
  ac <- (fit - 0.5*B[,"trRIV"])/tr                                          # design term
  ahl <- (B[,"T_am"] - 0.5*B[,"trRIV"])/tr                                  # amelia headline-relative
  cat(sprintf("  %4d  %5d  %6.3f   %+.4f(%.4f)   %+.4f(%.4f)   %+.4f(%.4f)   %+.4f(%.4f)\n",
              Nn, RN, tr, a[1],a[2], g[1],g[2], mean(ac),mcse(ac), mean(ahl),mcse(ahl)))
  res[[as.character(Nn)]] <- list(N=Nn, R=RN, tr=tr, amelia_fit=a, gauss_fit=g,
                                  ac=c(mean(ac),mcse(ac)), amelia_hl=c(mean(ahl),mcse(ahl)),
                                  raw=B)
}
stopCluster(cl)
cat("\nRead the PAIRED amelia-FIT / gauss-FIT columns (tight at all N):\n")
cat("  -> 0 as N grows  => proper MI converges to FITTED (paper's proper~=fitted holds).\n")
cat("  holds ~ -0.09    => small persistent proper-vs-FITTED gap (Spec 2).\n")
saveRDS(res, "verification/cache/spikes/phase0a-calibrated.rds")
cat("\nCache: verification/cache/spikes/phase0a-calibrated.rds\n")
