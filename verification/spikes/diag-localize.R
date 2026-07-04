# diag-localize.R  — localize the conjugate-DA over-dispersion at large M, r=1.
# Compare, on the SAME rep, per-cell imputed-value moments and barL:
#   (A) conjugate DA chain
#   (B) direct Gaussian-posterior sampler theta* ~ N(theta_obs, I_obs^-1)
#   (C) fixed-theta (theta_obs) conditional draws  [= the FITTED reference]
source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")

impute_gauss_post <- function(Y, R, theta_obs, M) {
  N <- nrow(Y); p <- ncol(Y); vobs <- theta_to_vec(theta_obs)
  Vpost <- solve(fisher_info_obs_mvn(theta_obs, Y, R)); Lp <- t(chol(0.5*(Vpost+t(Vpost))))
  patterns <- apply(R, 1, paste, collapse=""); upat <- unique(patterns); out <- vector("list", M); m <- 0
  while (m < M) {
    th <- vec_to_theta(vobs + as.numeric(Lp %*% rnorm(length(vobs))), p)
    if (min(eigen(th$Sigma, symmetric=TRUE, only.values=TRUE)$values) <= 1e-6) next
    m <- m + 1; Z <- Y
    for (pk in upat) { rows <- which(patterns==pk); Mi <- which(R[rows[1],]==1); if (length(Mi)==0) next
      Oi <- which(R[rows[1],]==0); n_pat <- length(rows)
      Soo <- solve(th$Sigma[Oi,Oi,drop=FALSE]); reg <- th$Sigma[Mi,Oi,drop=FALSE] %*% Soo
      cc <- th$Sigma[Mi,Mi,drop=FALSE] - reg %*% th$Sigma[Oi,Mi,drop=FALSE]
      Yo <- sweep(Z[rows,Oi,drop=FALSE], 2, th$mu[Oi], "-")
      CM <- matrix(th$mu[Mi], n_pat, length(Mi), byrow=TRUE) + Yo %*% t(reg)
      Z[rows,Mi] <- CM + matrix(rnorm(n_pat*length(Mi)), n_pat, length(Mi)) %*% t(t(chol(0.5*(cc+t(cc)))))
    }
    out[[m]] <- Z
  }
  out
}
impute_fixed <- function(Y, R, th, M) {
  N<-nrow(Y);p<-ncol(Y);patterns<-apply(R,1,paste,collapse="");upat<-unique(patterns);out<-vector("list",M)
  for (m in seq_len(M)) { Z<-Y
    for (pk in upat){rows<-which(patterns==pk);Mi<-which(R[rows[1],]==1);if(length(Mi)==0)next
      Oi<-which(R[rows[1],]==0);n_pat<-length(rows)
      Soo<-solve(th$Sigma[Oi,Oi,drop=FALSE]);reg<-th$Sigma[Mi,Oi,drop=FALSE]%*%Soo
      cc<-th$Sigma[Mi,Mi,drop=FALSE]-reg%*%th$Sigma[Oi,Mi,drop=FALSE]
      Yo<-sweep(Z[rows,Oi,drop=FALSE],2,th$mu[Oi],"-")
      CM<-matrix(th$mu[Mi],n_pat,length(Mi),byrow=TRUE)+Yo%*%t(reg)
      Z[rows,Mi]<-CM+matrix(rnorm(n_pat*length(Mi)),n_pat,length(Mi))%*%t(t(chol(0.5*(cc+t(cc)))))}
    out[[m]]<-Z }
  out
}

set.seed(20260522 + 1)
X <- gen_data(200, default_mu, default_Sigma)
mar <- apply_mar(X); em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)
ell_obs <- loglik_mvn(theta_obs, X)
mi1 <- which(mar$R[,1]==1); mi2 <- which(mar$R[,2]==1)
Mb <- 3000

set.seed(101); cj <- impute_mvn_conjugate(mar$Y, M=Mb, burnin=200, thin=5, theta_init=theta_obs)$imputed
set.seed(102); gp <- impute_gauss_post(mar$Y, mar$R, theta_obs, Mb)
set.seed(103); fx <- impute_fixed(mar$Y, mar$R, theta_obs, Mb)

summ <- function(imps, lab) {
  barL <- mean(vapply(imps, function(Z) loglik_mvn(theta_obs, Z), numeric(1)))
  X1 <- sapply(imps, function(Z) Z[mi1,1])   # (n_miss1 x M)
  # decompose imputed-X1 variance: total = Var over (m and cells)
  cell_mean <- rowMeans(X1); within_sd <- mean(apply(X1,1,sd))
  cat(sprintf("[%-12s] barL=%.3f  A=%.3f  | X1-imp: mean within-cell sd=%.4f  sd of cell-means=%.4f\n",
              lab, barL, barL-ell_obs, within_sd, sd(cell_mean)))
}
cat(sprintf("theta_obs sigma11=%.4f ; conditional-only sd would be ~%.4f\n\n",
            theta_obs$Sigma[1,1], NA))
summ(fx, "fixed-theta"); summ(gp, "gauss-post"); summ(cj, "conjugate-DA")
