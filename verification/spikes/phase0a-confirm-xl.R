# phase0a-confirm-xl.R — 100x-more-replications confirmation of the Phase-0 DA
# finding. Headline N=200 magnitude table at R=20000 (100x the R=200 run);
# N-persistence at large-but-bounded R per N (all >= 12x the original R=200);
# norm::da.norm parallelized via per-replicate rngseed (cross-checked against
# the validated serial R=100 anchor -0.743).
#
# All gaps: per-rep paired to the exact FITTED value, normalized by tr(RIV),
# seed set.seed(20260522+r) (cluster-invariant for the R's-RNG engines).
#
# Run: Rscript verification/spikes/phase0a-confirm-xl.R [ncores]

source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")
suppressPackageStartupMessages({ library(parallel); library(pbapply) })

args   <- commandArgs(trailingOnly = TRUE)
ncores <- if (length(args) >= 1) as.integer(args[1]) else 20
Rsmoke <- if (length(args) >= 2) as.integer(args[2]) else 0   # >0 overrides all R
M <- 50; burnin <- 100; thin <- 40
R_mag  <- 20000                              # N=200 magnitude table (100x)
R_by_N <- c(`200`=20000, `500`=10000, `1000`=5000, `2000`=2500)  # persistence
R_norm <- 10000                              # norm parallel (per-rep rngseed)
if (Rsmoke > 0) { R_mag <- Rsmoke; R_by_N[] <- Rsmoke; R_norm <- Rsmoke }

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
# norm::da.norm, parallel-safe via per-rep rngseed (each rep fully determines
# its own norm RNG => no cross-worker collision).
run_norm <- function(r) {
  set.seed(20260522 + r)
  X <- gen_data(200, default_mu, default_Sigma)
  ell_com_com <- loglik_mvn(mle_complete_mvn(X), X)
  mar <- apply_mar(X); em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)
  trRIV <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  T_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ell_com_com
  norm::rngseed(20260701 + r)
  imps <- impute_mvn(mar$Y, M=M, burnin=200, thin=100, em_fit=em)
  T_norm <- mean(vapply(imps, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  c(trRIV=trRIV, gap=(T_norm-T_fiml)/trRIV)
}

t0 <- Sys.time()
cl <- makeCluster(ncores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); source("verification/da-conjugate-engine.R"); NULL }))
clusterExport(cl, c("run_all_engines","run_conj_only","run_norm","impute_gauss_post","impute_conj_deflated","M","burnin","thin"))
mcse <- function(x) sd(x)/sqrt(length(x))

cat(sprintf("\n=== Arm A: magnitude, N=200, R=%d (100x) ===\n\n", R_mag))
A <- do.call(rbind, pblapply(seq_len(R_mag), function(r) run_all_engines(r, 200), cl=cl))
trA <- mean(A[,"trRIV"]); fitA <- A[,"T_fiml"]
cat(sprintf("mean tr(RIV)=%.4f\n\nengine        (T-FITTED)/tr(RIV)\n----------    ------------------\n", trA))
for (nm in c("T_cj","T_cd","T_gp","T_am")) { d <- (A[,nm]-fitA)/trA
  cat(sprintf("%-10s    %+7.4f (se %.4f)\n", c(T_cj="conjugate",T_cd="deflated",T_gp="gauss-post",T_am="amelia")[nm], mean(d), mcse(d))) }

cat("\n=== Arm B: N-persistence (conjugate) ===\n\n")
cat("   N       R     tr(RIV)   (T_conj-FITTED)/tr(RIV)\n  ---   ------   -------   ----------------------\n")
persist <- list()
for (Nn in c(200, 500, 1000, 2000)) {
  RN <- R_by_N[[as.character(Nn)]]
  if (Nn == 200) { B <- A[, c("trRIV","T_fiml","T_cj")] }  # reuse the R=20000 arm
  else { clusterExport(cl, "Nn", envir=environment())
    B <- do.call(rbind, pblapply(seq_len(RN), function(r) run_conj_only(r, Nn), cl=cl)) }
  tr <- mean(B[,"trRIV"]); d <- (B[,"T_cj"]-B[,"T_fiml"])/tr
  persist[[as.character(Nn)]] <- c(N=Nn, R=nrow(B), tr=tr, gap=mean(d), se=mcse(d))
  cat(sprintf("  %4d  %6d   %6.4f    %+7.4f (se %.4f)\n", Nn, nrow(B), tr, mean(d), mcse(d)))
}

cat(sprintf("\n=== norm::da.norm parallel (per-rep rngseed), R=%d, N=200 ===\n\n", R_norm))
Dn <- do.call(rbind, pblapply(seq_len(R_norm), run_norm, cl=cl))
cat(sprintf("norm::da.norm  (T-FITTED)/tr(RIV) = %+.4f (se %.4f)   [serial R=100 anchor was -0.743]\n",
            mean(Dn[,"gap"]), mcse(Dn[,"gap"])))
stopCluster(cl)

el <- as.numeric(difftime(Sys.time(), t0, units="mins"))
cat(sprintf("\nTotal wall-clock: %.1f min\n", el))
dir.create("verification/cache/spikes", recursive=TRUE, showWarnings=FALSE)
saveRDS(list(ArmA=A, persist=persist, norm=Dn, elapsed_min=el),
        "verification/cache/spikes/phase0a-confirm-xl.rds")
cat("Cache: verification/cache/spikes/phase0a-confirm-xl.rds\n")
