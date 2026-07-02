# diag-tiebreak.R
# Tiebreaker: conjugate DA gives T_proper = FITTED - 0.77 tr(RIV); Amelia gives
# ~ FITTED. Both should have theta* ~ observed posterior. Who is right?
#  (1) Measure Amelia's own theta-tilde dispersion (a_out$mu, a_out$covMatrices)
#      against I_obs^{-1}. Under-dispersed => Amelia under-propagates.
#  (2) A THIRD independent proper sampler: theta* ~ N(theta_obs, I_obs^{-1})
#      drawn directly (PSD-repaired), impute Y_mis|theta*. If it matches the
#      conjugate (~ -0.77 tr(RIV)), two independent exact samplers agree.
source("verification/00-setup.R")
source("verification/da-conjugate-engine.R")
suppressPackageStartupMessages({ library(parallel); library(pbapply) })

# direct-Gaussian proper imputer: theta* ~ N(theta_obs_vec, I_obs^{-1}) per m.
impute_gauss_post <- function(Y, R, theta_obs, M) {
  N <- nrow(Y); p <- ncol(Y)
  vobs <- theta_to_vec(theta_obs)
  Vpost <- solve(fisher_info_obs_mvn(theta_obs, Y, R))
  Lp <- t(chol(0.5*(Vpost+t(Vpost))))
  patterns <- apply(R, 1, paste, collapse="")
  upat <- unique(patterns)
  out <- vector("list", M); n_reject <- 0
  m <- 0
  while (m < M) {
    thv <- vobs + as.numeric(Lp %*% rnorm(length(vobs)))
    th <- vec_to_theta(thv, p)
    ev <- tryCatch(min(eigen(th$Sigma, symmetric=TRUE, only.values=TRUE)$values), error=function(e) -1)
    if (ev <= 1e-6) { n_reject <- n_reject + 1; next }   # reject non-PSD Sigma*
    m <- m + 1
    Z <- Y
    for (pk in upat) {
      rows <- which(patterns==pk); Mi <- which(R[rows[1],]==1); if (length(Mi)==0) next
      Oi <- which(R[rows[1],]==0); n_pat <- length(rows)
      if (length(Oi)==0) { CM <- matrix(th$mu, n_pat, length(Mi), byrow=TRUE); cc <- th$Sigma } else {
        Soo <- solve(th$Sigma[Oi,Oi,drop=FALSE]); reg <- th$Sigma[Mi,Oi,drop=FALSE] %*% Soo
        cc <- th$Sigma[Mi,Mi,drop=FALSE] - reg %*% th$Sigma[Oi,Mi,drop=FALSE]
        Yo <- sweep(Z[rows,Oi,drop=FALSE], 2, th$mu[Oi], "-")
        CM <- matrix(th$mu[Mi], n_pat, length(Mi), byrow=TRUE) + Yo %*% t(reg)
      }
      Lc <- t(chol(0.5*(cc+t(cc))))
      Z[rows,Mi] <- CM + matrix(rnorm(n_pat*length(Mi)), n_pat, length(Mi)) %*% t(Lc)
    }
    out[[m]] <- Z
  }
  list(imputed=out, n_reject=n_reject)
}

run_one <- function(r) {
  set.seed(20260522 + r)
  X <- gen_data(200, default_mu, default_Sigma)
  theta_com <- mle_complete_mvn(X); ell_com_com <- loglik_mvn(theta_com, X)
  mar <- apply_mar(X)
  em <- em_mvn(mar$Y); theta_obs <- list(mu=em$mu, Sigma=em$Sigma)
  T_fiml <- barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R) - ell_com_com
  I_obs <- fisher_info_obs_mvn(theta_obs, mar$Y, mar$R); V_obs <- solve(I_obs)

  # amelia + its theta-tilde dispersion
  df <- as.data.frame(mar$Y); colnames(df) <- sprintf("V%d",1:4)
  a <- Amelia::amelia(df, m=50, p2s=0)
  T_am <- mean(vapply(a$imputations, function(d) loglik_mvn(theta_obs, as.matrix(d)), numeric(1))) - ell_com_com
  # theta-tilde: a$mu is p x m ; a$covMatrices is p x p x m
  tt_vecs <- t(sapply(seq_len(50), function(k) {
    theta_to_vec(list(mu=a$mu[,k], Sigma=a$covMatrices[,,k]))
  }))
  V_amelia_tt <- cov(tt_vecs)

  # direct gaussian posterior sampler
  gp <- impute_gauss_post(mar$Y, mar$R, theta_obs, 50)
  T_gp <- mean(vapply(gp$imputed, function(Z) loglik_mvn(theta_obs, Z), numeric(1))) - ell_com_com

  list(T_fiml=T_fiml, T_am=T_am, T_gp=T_gp,
       tr_Vobs=sum(diag(V_obs)), tr_Vamelia=sum(diag(V_amelia_tt)),
       reject=gp$n_reject)
}

cl <- makeCluster(10)
clusterEvalQ(cl, { source("verification/00-setup.R"); source("verification/da-conjugate-engine.R") })
clusterExport(cl, c("run_one","impute_gauss_post"))
Rn <- 40
res <- pblapply(seq_len(Rn), run_one, cl=cl)
stopCluster(cl)

g <- function(nm) vapply(res, `[[`, numeric(1), nm)
mcse <- function(x) sd(x)/sqrt(length(x))
cat(sprintf("\nR=%d\n", Rn))
cat(sprintf("  T_fiml (FITTED)         mean=%+7.3f\n", mean(g("T_fiml"))))
cat(sprintf("  T_amelia                mean=%+7.3f  (dev from FITTED: %+.3f +/- %.3f)\n",
            mean(g("T_am")), mean(g("T_am")-g("T_fiml")), mcse(g("T_am")-g("T_fiml"))))
cat(sprintf("  T_gauss_post (direct)   mean=%+7.3f  (dev from FITTED: %+.3f +/- %.3f)\n",
            mean(g("T_gp")), mean(g("T_gp")-g("T_fiml")), mcse(g("T_gp")-g("T_fiml"))))
cat(sprintf("\n  theta-tilde dispersion:  tr(Var_amelia)=%.4f   tr(I_obs^-1)=%.4f   ratio=%.2f\n",
            mean(g("tr_Vamelia")), mean(g("tr_Vobs")), mean(g("tr_Vamelia"))/mean(g("tr_Vobs"))))
cat(sprintf("  gauss-post PSD rejections (total): %d\n", sum(g("reject"))))
