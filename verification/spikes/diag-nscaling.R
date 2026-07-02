# diag-nscaling.R — does the exact-DA vs Amelia deviance-bias gap persist or
# vanish as N grows? Report (T_engine - T_fitted)/tr(RIV) at N=200,500,1000.
# Persistent ratio => O(tr(RIV)) engine divergence (serious). Shrinking => finite-N.
# Second conjugate arm 'conj_defl': IW centred at the MLE (df bumped so
# E[Sigma*]=S, removing the (N-1)/(N-p-2) prior inflation) — if this collapses
# onto Amelia, the Jeffreys inflation is confirmed as the mechanism.
source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")
suppressPackageStartupMessages({ library(parallel); library(pbapply) })

# Deflated conjugate: rescale each IW draw so its posterior mean matches the MLE
# SS/(N-1) instead of SS/(N-p-2). Achieved by drawing IW(df, SS*) with
# SS* = SS*(N-p-2)/(N-1) so that E[Sigma*] = SS*/(N-p-2) = SS/(N-1) = S_MLE-ish.
impute_conj_deflated <- function(Y, M, burnin, thin, theta_init) {
  N <- nrow(Y); p <- ncol(Y); R <- matrix(as.numeric(is.na(Y)), N, p)
  patterns <- apply(R,1,paste,collapse=""); upat <- unique(patterns)
  pr <- lapply(upat, function(pk) which(patterns==pk))
  pM <- lapply(upat, function(pk) which(R[which(patterns==pk)[1],]==1))
  pO <- lapply(upat, function(pk) which(R[which(patterns==pk)[1],]==0))
  mu <- theta_init$mu; Sigma <- theta_init$Sigma; Xc <- Y
  fill <- function(mu,Sigma){ for(j in seq_along(upat)){ Mi<-pM[[j]]; if(length(Mi)==0)next
    Oi<-pO[[j]]; rows<-pr[[j]]; n_pat<-length(rows)
    if(length(Oi)==0){CM<-matrix(mu,n_pat,length(Mi),byrow=TRUE);cc<-Sigma}else{
      Soo<-chol2inv(chol(Sigma[Oi,Oi,drop=FALSE]));reg<-Sigma[Mi,Oi,drop=FALSE]%*%Soo
      cc<-Sigma[Mi,Mi,drop=FALSE]-reg%*%Sigma[Oi,Mi,drop=FALSE]
      Yo<-sweep(Xc[rows,Oi,drop=FALSE],2,mu[Oi],"-");CM<-matrix(mu[Mi],n_pat,length(Mi),byrow=TRUE)+Yo%*%t(reg)}
    Xc[rows,Mi]<<-CM+matrix(rnorm(n_pat*length(Mi)),n_pat,length(Mi))%*%t(t(chol(0.5*(cc+t(cc)))))}}
  draw <- function(){ yb<-colMeans(Xc);Cc<-sweep(Xc,2,yb,"-");SS<-crossprod(Cc);SS<-0.5*(SS+t(SS))+diag(1e-8,p)
    SSstar <- SS*(N-p-2)/(N-1)                 # deflate so E[Sigma*]=SS/(N-1)
    Snew<-rinvwishart_draw(N-1,SSstar); mnew<-yb+as.numeric(t(chol(Snew/N))%*%rnorm(p)); list(mu=mnew,Sigma=Snew)}
  for(b in seq_len(burnin)){fill(mu,Sigma);st<-draw();mu<-st$mu;Sigma<-st$Sigma}
  imp<-vector("list",M); for(m in seq_len(M)){for(t in seq_len(thin)){fill(mu,Sigma);st<-draw();mu<-st$mu;Sigma<-st$Sigma};imp[[m]]<-Xc}
  imp
}

run_one <- function(r, Nn) {
  set.seed(20260522 + r)
  X <- gen_data(Nn, default_mu, default_Sigma)
  ell_com_com <- loglik_mvn(mle_complete_mvn(X), X)
  mar <- apply_mar(X); em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)
  trRIV <- tr_riv_analytic(theta_obs, mar$Y, mar$R)$tr_RIV
  T_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ell_com_com
  cj <- impute_mvn_conjugate(mar$Y, 50, 100, 40, theta_obs)$imputed
  T_cj <- mean(vapply(cj, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  cd <- impute_conj_deflated(mar$Y, 50, 100, 40, theta_obs)
  T_cd <- mean(vapply(cd, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  am <- impute_mvn_amelia(mar$Y, 50)
  T_am <- mean(vapply(am, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com
  c(trRIV=trRIV, T_fiml=T_fiml, T_cj=T_cj, T_cd=T_cd, T_am=T_am)
}

cl <- makeCluster(12)
clusterEvalQ(cl, { source("verification/00-setup.R"); source("verification/da-conjugate-engine.R") })
clusterExport(cl, c("run_one","impute_conj_deflated"))
Rn <- 40
cat(sprintf("\nN-scaling of the deviance-bias gap (R=%d/cell), paired to FITTED, /tr(RIV):\n\n", Rn))
cat("   N   tr(RIV)   (T_conj-FIT)/tr   (T_defl-FIT)/tr   (T_amelia-FIT)/tr\n")
cat("  ---  -------   --------------    --------------    ---------------\n")
for (Nn in c(200, 500, 1000)) {
  M <- do.call(rbind, pblapply(seq_len(Rn), function(r) run_one(r, Nn), cl=cl))
  tr <- mean(M[,"trRIV"])
  fit <- M[,"T_fiml"]
  g_cj <- mean(M[,"T_cj"]-fit)/tr; g_cd <- mean(M[,"T_cd"]-fit)/tr; g_am <- mean(M[,"T_am"]-fit)/tr
  se_cj <- sd(M[,"T_cj"]-fit)/sqrt(Rn)/tr
  cat(sprintf("  %4d  %6.3f    %+7.3f (se %.3f)   %+7.3f          %+7.3f\n",
              Nn, tr, g_cj, se_cj, g_cd, g_am))
}
stopCluster(cl)
