# diag-pstep-variance.R
# Decisive test: is the conjugate P-step's theta* draw variance correct?
# Proper MI requires theta* ~ p(theta | Y_obs)  =>  Var(theta*) ~ I_obs^{-1}.
# If my chain's theta* draws are over-dispersed vs I_obs^{-1}, the engine is buggy.
# Compare the sampled Var(theta*) to BOTH analytic references:
#   I_obs^{-1}  (fisher_info_obs_mvn)   -- the CORRECT proper-MI target
#   I_com^{-1}  (fisher_info_com_mvn)   -- the complete-data (too-tight) reference
source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")

# Instrumented conjugate chain: returns the theta* (mu,Sigma) at each kept draw.
chain_thetastar <- function(Y, M, burnin, thin, theta_init) {
  N <- nrow(Y); p <- ncol(Y)
  R <- matrix(as.numeric(is.na(Y)), N, p)
  patterns <- apply(R, 1, paste, collapse = "")
  upat <- unique(patterns)
  pr <- lapply(upat, function(pk) which(patterns == pk))
  pM <- lapply(upat, function(pk) which(R[which(patterns==pk)[1], ]==1))
  pO <- lapply(upat, function(pk) which(R[which(patterns==pk)[1], ]==0))
  mu <- theta_init$mu; Sigma <- theta_init$Sigma
  Xc <- Y
  i_step <- function(mu, Sigma) {
    for (j in seq_along(upat)) {
      Mi <- pM[[j]]; if (length(Mi)==0) next
      Oi <- pO[[j]]; rows <- pr[[j]]; n_pat <- length(rows)
      if (length(Oi)==0) { CM <- matrix(mu, n_pat, length(Mi), byrow=TRUE); cc <- Sigma } else {
        Soo <- chol2inv(chol(Sigma[Oi,Oi,drop=FALSE])); reg <- Sigma[Mi,Oi,drop=FALSE] %*% Soo
        cc <- Sigma[Mi,Mi,drop=FALSE] - reg %*% Sigma[Oi,Mi,drop=FALSE]
        Yo <- sweep(Xc[rows,Oi,drop=FALSE], 2, mu[Oi], "-")
        CM <- matrix(mu[Mi], n_pat, length(Mi), byrow=TRUE) + Yo %*% t(reg)
      }
      Lc <- t(chol(0.5*(cc+t(cc))))
      Xc[rows,Mi] <<- CM + matrix(rnorm(n_pat*length(Mi)), n_pat, length(Mi)) %*% t(Lc)
    }
  }
  p_step <- function() {
    yb <- colMeans(Xc); Cc <- sweep(Xc,2,yb,"-"); SS <- crossprod(Cc); SS <- 0.5*(SS+t(SS))+diag(1e-8,p)
    Snew <- rinvwishart_draw(N-1, SS)
    mnew <- yb + as.numeric(t(chol(Snew/N)) %*% rnorm(p))
    list(mu=mnew, Sigma=Snew)
  }
  for (b in seq_len(burnin)) { i_step(mu,Sigma); st<-p_step(); mu<-st$mu; Sigma<-st$Sigma }
  thetas <- vector("list", M)
  for (m in seq_len(M)) {
    for (t in seq_len(thin)) { i_step(mu,Sigma); st<-p_step(); mu<-st$mu; Sigma<-st$Sigma }
    thetas[[m]] <- list(mu=mu, Sigma=Sigma)   # theta* that generated draw m's chain state
  }
  thetas
}

set.seed(20260522 + 1)
X <- gen_data(200, default_mu, default_Sigma)
mar <- apply_mar(X)
em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)

# Big M for a clean variance estimate of theta*.
Mbig <- 4000
th <- chain_thetastar(mar$Y, M=Mbig, burnin=200, thin=5, theta_init=theta_obs)
vecs <- t(sapply(th, function(t) theta_to_vec(t)))   # Mbig x 14
Vstar <- cov(vecs)                                    # sampled Var(theta*)

I_obs <- fisher_info_obs_mvn(theta_obs, mar$Y, mar$R)
I_com <- fisher_info_com_mvn(theta_obs, 200)
V_obs <- solve(I_obs)      # correct proper target
V_com <- solve(I_com)      # too-tight reference

d <- function(A,B) sqrt(mean((A-B)^2)) / sqrt(mean(B^2))   # relative Frobenius
cat(sprintf("\nSampled Var(theta*) from the conjugate chain (M=%d):\n", Mbig))
cat(sprintf("  rel-Frobenius  Var(theta*) vs I_obs^-1  = %.3f\n", d(Vstar, V_obs)))
cat(sprintf("  rel-Frobenius  Var(theta*) vs I_com^-1  = %.3f\n", d(Vstar, V_com)))
cat(sprintf("  tr(Var theta*) = %.4f ;  tr(I_obs^-1) = %.4f ;  tr(I_com^-1) = %.4f\n",
            sum(diag(Vstar)), sum(diag(V_obs)), sum(diag(V_com))))
cat("\nDiagonal comparison (param: Var* / I_obs^-1 / I_com^-1):\n")
lab <- c("mu1","mu2","mu3","mu4","s11","s21","s31","s41","s22","s32","s42","s33","s43","s44")
for (i in 1:14) cat(sprintf("  %-4s  %.5f  %.5f  %.5f   (ratio*/obs=%.2f)\n",
    lab[i], Vstar[i,i], V_obs[i,i], V_com[i,i], Vstar[i,i]/V_obs[i,i]))
