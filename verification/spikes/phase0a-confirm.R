# phase0a-confirm.R — properly-powered confirmation of the two load-bearing
# quantitative claims from the Phase-0 DA finding (todo/040 §8):
#   Arm A  magnitude at N=200, R=200: conjugate / amelia / gauss / deflated
#          (cluster, R's own RNG) + norm::da.norm at R=100 serial (rngseed-fragile).
#   Arm B  N-persistence, R=200, conjugate at N in {200,500,1000,2000}
#          (10x N range vs the R=30 / 5x pilot) — the input to the theory's
#          "persistent O(tr(RIV)) vs vanishing" question.
# All gaps are per-replicate paired to the exact FITTED value and normalized by
# tr(RIV). Seeds set.seed(20260522+r) (cluster-invariant for the R's-RNG engines).
#
# Run: Rscript verification/spikes/phase0a-confirm.R [R] [n_cores] [R_norm]

source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")
suppressPackageStartupMessages({ library(parallel); library(pbapply) })

args   <- commandArgs(trailingOnly = TRUE)
Rn     <- if (length(args) >= 1) as.integer(args[1]) else 200
ncores <- if (length(args) >= 2) as.integer(args[2]) else 20
Rnorm  <- if (length(args) >= 3) as.integer(args[3]) else 100
M <- 50; burnin <- 100; thin <- 40

# --- engine variants (R's own RNG; cluster-safe under per-rep set.seed) --------
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
impute_conj_deflated <- function(Y, M, burnin, thin, theta_init) {
  N<-nrow(Y);p<-ncol(Y);R<-matrix(as.numeric(is.na(Y)),N,p)
  patterns<-apply(R,1,paste,collapse="");upat<-unique(patterns)
  pr<-lapply(upat,function(pk)which(patterns==pk));pM<-lapply(upat,function(pk)which(R[which(patterns==pk)[1],]==1));pO<-lapply(upat,function(pk)which(R[which(patterns==pk)[1],]==0))
  mu<-theta_init$mu;Sigma<-theta_init$Sigma;Xc<-Y
  fill<-function(mu,Sigma){for(j in seq_along(upat)){Mi<-pM[[j]];if(length(Mi)==0)next
    Oi<-pO[[j]];rows<-pr[[j]];n_pat<-length(rows)
    if(length(Oi)==0){CM<-matrix(mu,n_pat,length(Mi),byrow=TRUE);cc<-Sigma}else{
      Soo<-chol2inv(chol(Sigma[Oi,Oi,drop=FALSE]));reg<-Sigma[Mi,Oi,drop=FALSE]%*%Soo
      cc<-Sigma[Mi,Mi,drop=FALSE]-reg%*%Sigma[Oi,Mi,drop=FALSE]
      Yo<-sweep(Xc[rows,Oi,drop=FALSE],2,mu[Oi],"-");CM<-matrix(mu[Mi],n_pat,length(Mi),byrow=TRUE)+Yo%*%t(reg)}
    Xc[rows,Mi]<<-CM+matrix(rnorm(n_pat*length(Mi)),n_pat,length(Mi))%*%t(t(chol(0.5*(cc+t(cc)))))}}
  draw<-function(){yb<-colMeans(Xc);Cc<-sweep(Xc,2,yb,"-");SS<-crossprod(Cc);SS<-0.5*(SS+t(SS))+diag(1e-8,p)
    SSstar<-SS*(N-p-2)/(N-1);Snew<-rinvwishart_draw(N-1,SSstar);mnew<-yb+as.numeric(t(chol(Snew/N))%*%rnorm(p));list(mu=mnew,Sigma=Snew)}
  for(b in seq_len(burnin)){fill(mu,Sigma);st<-draw();mu<-st$mu;Sigma<-st$Sigma}
  imp<-vector("list",M);for(m in seq_len(M)){for(t in seq_len(thin)){fill(mu,Sigma);st<-draw();mu<-st$mu;Sigma<-st$Sigma};imp[[m]]<-Xc};imp
}

# One replicate: all cluster-safe engines (conjugate/amelia/gauss/deflated).
run_all_engines <- function(r, Nn) {
  set.seed(20260522 + r)
  X <- gen_data(Nn, default_mu, default_Sigma)
  ell_com_com <- loglik_mvn(mle_complete_mvn(X), X)
  mar <- apply_mar(X); em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)
  trRIV <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  T_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ell_com_com
  Tof <- function(imps) mean(vapply(imps, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  cj <- impute_mvn_conjugate(mar$Y, M, burnin, thin, theta_obs)$imputed
  cd <- impute_conj_deflated(mar$Y, M, burnin, thin, theta_obs)
  gp <- impute_gauss_post(mar$Y, mar$R, theta_obs, M)
  am <- impute_mvn_amelia(mar$Y, M)
  c(trRIV=trRIV, T_fiml=T_fiml, T_cj=Tof(cj), T_cd=Tof(cd), T_gp=Tof(gp), T_am=Tof(am))
}
# Lean conjugate-only replicate for the large-N persistence arm.
run_conj_only <- function(r, Nn) {
  set.seed(20260522 + r)
  X <- gen_data(Nn, default_mu, default_Sigma)
  ell_com_com <- loglik_mvn(mle_complete_mvn(X), X)
  mar <- apply_mar(X); em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)
  trRIV <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  T_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ell_com_com
  cj <- impute_mvn_conjugate(mar$Y, M, burnin, thin, theta_obs)$imputed
  T_cj <- mean(vapply(cj, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  c(trRIV=trRIV, T_fiml=T_fiml, T_cj=T_cj)
}

cl <- makeCluster(ncores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); source("verification/da-conjugate-engine.R"); NULL }))
clusterExport(cl, c("run_all_engines","run_conj_only","impute_gauss_post","impute_conj_deflated","M","burnin","thin"))
mcse <- function(x) sd(x)/sqrt(length(x))

# ---- Arm A: magnitude at N=200, R=200 ----
cat(sprintf("\n=== Arm A: magnitude at N=200, R=%d (paired to FITTED, /tr(RIV)) ===\n\n", Rn))
A <- do.call(rbind, pblapply(seq_len(Rn), function(r) run_all_engines(r, 200), cl=cl))
trA <- mean(A[,"trRIV"]); fitA <- A[,"T_fiml"]
cat(sprintf("mean tr(RIV)=%.3f   mean FITTED=%+.3f\n\n", trA, mean(fitA)))
cat("engine        (T-FITTED)/tr(RIV)\n----------    ------------------\n")
for (nm in c("T_cj","T_cd","T_gp","T_am")) {
  d <- (A[,nm]-fitA)/trA
  cat(sprintf("%-10s    %+7.3f (se %.3f)\n",
      c(T_cj="conjugate",T_cd="deflated",T_gp="gauss-post",T_am="amelia")[nm], mean(d), mcse(d)))
}

# ---- Arm B: N-persistence, conjugate, R=200 ----
cat(sprintf("\n=== Arm B: N-persistence (conjugate, R=%d) ===\n\n", Rn))
cat("   N   tr(RIV)   (T_conj-FITTED)/tr(RIV)\n  ---  -------   ----------------------\n")
for (Nn in c(200, 500, 1000, 2000)) {
  clusterExport(cl, "Nn", envir = environment())   # carry the loop var to workers
  B <- do.call(rbind, pblapply(seq_len(Rn), function(r) run_conj_only(r, Nn), cl=cl))
  tr <- mean(B[,"trRIV"]); d <- (B[,"T_cj"]-B[,"T_fiml"])/tr
  cat(sprintf("  %4d  %6.3f    %+7.3f (se %.3f)\n", Nn, tr, mean(d), mcse(d)))
}
stopCluster(cl)

# ---- norm::da.norm serial (rngseed-fragile) at N=200 ----
cat(sprintf("\n=== norm::da.norm (Schafer canonical Jeffreys DA), serial, R=%d, N=200 ===\n\n", Rnorm))
norm::rngseed(20260701)
Dn <- t(vapply(seq_len(Rnorm), function(r) {
  set.seed(20260522 + r)
  X <- gen_data(200, default_mu, default_Sigma)
  ell_com_com <- loglik_mvn(mle_complete_mvn(X), X)
  mar <- apply_mar(X); em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)
  trRIV <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  T_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ell_com_com
  imps <- impute_mvn(mar$Y, M=M, burnin=200, thin=100, em_fit=em)
  T_norm <- mean(vapply(imps, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  c(trRIV=trRIV, gap=(T_norm-T_fiml)/trRIV)
}, numeric(2)))
cat(sprintf("norm::da.norm  (T-FITTED)/tr(RIV) = %+.3f (se %.3f)   [mean tr(RIV)=%.3f]\n",
            mean(Dn[,"gap"]), mcse(Dn[,"gap"]), mean(Dn[,"trRIV"])))

dir.create("verification/cache/spikes", recursive=TRUE, showWarnings=FALSE)
saveRDS(list(ArmA=A, Rn=Rn, norm_gap=Dn), "verification/cache/spikes/phase0a-confirm.rds")
cat("\nDone. Cache: verification/cache/spikes/phase0a-confirm.rds\n")
