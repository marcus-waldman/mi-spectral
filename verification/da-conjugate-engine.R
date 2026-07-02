# da-conjugate-engine.R
#
# Hand-rolled conjugate data-augmentation (DA) imputer for the MVN missing-data
# model under the reference prior  p(mu, Sigma) ∝ |Sigma|^{-(p+1)/2}.
#
# This is the EXACT-posterior proper-MI engine reviewer r1#8 (v1 AI review,
# paper 88) asked for: a standard Gibbs / data-augmentation sampler that draws
# from the true conditional posteriors, NOT Amelia's EMB (bootstrap + EM)
# approximation. Registration: todo/040 (Phase 0/1).
#
# One DA sweep alternates:
#   I-step  (impute)   : for each observation, draw the missing block given the
#                        observed block under the CURRENT (mu, Sigma):
#                          X_i^{M} | X_i^{O} ~ N( mu_M + S_MO S_OO^{-1}(y_O - mu_O),
#                                                 S_MM - S_MO S_OO^{-1} S_OM ).
#   P-step  (posterior): from the CURRENT completed data (ybar, sum-of-squares
#                        SS with the complete-data divisor N):
#                          Sigma ~ Inverse-Wishart(N-1, SS)          [SS = (N-1) S]
#                          mu | Sigma ~ N(ybar, Sigma / N).
#
# The alternation IS data augmentation (Tanner & Wong 1987; Schafer 1997 Alg 5.2).
# Our non-monotone pattern has no one-shot closed form, so the iteration is
# required. Everything uses R's own Mersenne-Twister RNG, so a worker that has
# called set.seed(.) is fully reproducible and core-count invariant — the
# property norm::da.norm's separate rngseed() state does not give us.
#
# Depends on 00-setup.R for: loglik_mvn, mle_with_cov_mvn, mi_fit_mvn,
# riv_sample, theta_to_vec (only used downstream by the caller). This file adds
# no dependency beyond base R + stats::rWishart.


# -----------------------------------------------------------------------------
# Inverse-Wishart draw via a Wishart draw + inverse.
#
# We want Sigma ~ Inverse-Wishart(df, scale = Psi) with the convention
#   E[Sigma] = Psi / (df - p - 1).
# If W ~ Wishart(df, V) (E[W] = df V), then W^{-1} ~ Inverse-Wishart(df, V^{-1}).
# So set V = Psi^{-1}, draw W ~ Wishart(df, V), return Sigma = W^{-1}.
# stats::rWishart uses rnorm/rchisq internally => R's RNG, cluster-reproducible.
# -----------------------------------------------------------------------------

rinvwishart_draw <- function(df, Psi) {
  V <- chol2inv(chol(Psi))                       # Psi^{-1}, PSD by construction
  W <- stats::rWishart(1, df = df, Sigma = V)[, , 1]
  Sigma <- chol2inv(chol(W))                     # W^{-1}
  return(0.5 * (Sigma + t(Sigma)))               # symmetrize away fp asymmetry
}


# -----------------------------------------------------------------------------
# impute_mvn_conjugate(Y, M, burnin, thin, theta_init)
#
# Y         : N x p matrix with NAs in the missing cells (mask derived here).
# M         : number of completed datasets to return.
# burnin    : DA sweeps discarded before the first kept draw.
# thin      : DA sweeps between kept draws.
# theta_init: optional list(mu, Sigma) to seed the chain (e.g. the EM / FIML
#             observed-data MLE). If NULL, seeded from the available-case moments.
#
# Returns list(imputed = <list of M completed matrices>, psd_fail = <integer>),
# psd_fail counting any non-PSD Cholesky event across all sweeps (should be 0).
# -----------------------------------------------------------------------------

impute_mvn_conjugate <- function(Y, M, burnin = 100, thin = 50,
                                 theta_init = NULL) {
  N <- nrow(Y)
  p <- ncol(Y)
  R <- matrix(as.numeric(is.na(Y)), nrow = N, ncol = p)

  # Group rows by missingness pattern (same key convention as 00-setup.R).
  patterns <- apply(R, 1, function(row) { return(paste(row, collapse = "")) })
  upat <- unique(patterns)
  pat_rows <- lapply(upat, function(pk) { return(which(patterns == pk)) })
  pat_Mi   <- lapply(upat, function(pk) { return(which(R[which(patterns == pk)[1], ] == 1)) })
  pat_Oi   <- lapply(upat, function(pk) { return(which(R[which(patterns == pk)[1], ] == 0)) })

  # Initial (mu, Sigma).
  if (is.null(theta_init)) {
    # Available-case moments (pairwise complete) as a rough seed.
    mu <- colMeans(Y, na.rm = TRUE)
    Sigma <- stats::cov(Y, use = "pairwise.complete.obs")
    Sigma[is.na(Sigma)] <- 0
    diag(Sigma)[diag(Sigma) <= 0 | is.na(diag(Sigma))] <- 1
    Sigma <- 0.5 * (Sigma + t(Sigma)) + diag(1e-6, p)
  } else {
    mu <- theta_init$mu
    Sigma <- theta_init$Sigma
  }

  Xc <- Y                                        # working completed matrix
  psd_fail <- 0

  # One I-step: fill the missing cells under the current (mu, Sigma).
  i_step <- function(mu, Sigma) {
    for (j in seq_along(upat)) {
      Mi <- pat_Mi[[j]]
      if (length(Mi) == 0) { next }              # fully observed pattern
      Oi <- pat_Oi[[j]]
      rows <- pat_rows[[j]]
      n_pat <- length(rows)
      if (length(Oi) == 0) {
        cond_mean_fixed <- mu
        cond_cov <- Sigma
        reg <- NULL
      } else {
        Soo_inv <- chol2inv(chol(Sigma[Oi, Oi, drop = FALSE]))
        reg <- Sigma[Mi, Oi, drop = FALSE] %*% Soo_inv          # |M| x |O|
        cond_cov <- Sigma[Mi, Mi, drop = FALSE] -
          reg %*% Sigma[Oi, Mi, drop = FALSE]
        cond_mean_fixed <- mu[Mi]
      }
      cond_cov <- 0.5 * (cond_cov + t(cond_cov))
      Lc <- tryCatch(t(chol(cond_cov)), error = function(e) { NULL })
      if (is.null(Lc)) {
        psd_fail <<- psd_fail + 1
        Lc <- t(chol(cond_cov + diag(1e-8, length(Mi))))
      }
      # Conditional means: n_pat x |M|.
      if (is.null(reg)) {
        CM <- matrix(cond_mean_fixed, n_pat, length(Mi), byrow = TRUE)
      } else {
        Yo_c <- sweep(Xc[rows, Oi, drop = FALSE], 2, mu[Oi], FUN = "-")
        CM <- matrix(cond_mean_fixed, n_pat, length(Mi), byrow = TRUE) +
          Yo_c %*% t(reg)
      }
      E <- matrix(stats::rnorm(n_pat * length(Mi)), n_pat, length(Mi))
      Xc[rows, Mi] <<- CM + E %*% t(Lc)          # each row ~ N(CM_row, cond_cov)
    }
    invisible(NULL)
  }

  # One P-step: draw (Sigma, mu) from the posterior given the completed data.
  p_step <- function() {
    ybar <- colMeans(Xc)
    Cc <- sweep(Xc, 2, ybar, FUN = "-")
    SS <- crossprod(Cc)                          # sum of squares = (N-1) S
    SS <- 0.5 * (SS + t(SS)) + diag(1e-8, p)     # guard fp asymmetry / singularity
    Sigma_new <- rinvwishart_draw(df = N - 1, Psi = SS)
    Lm <- tryCatch(t(chol(Sigma_new / N)), error = function(e) { NULL })
    if (is.null(Lm)) {
      psd_fail <<- psd_fail + 1
      Lm <- t(chol(Sigma_new / N + diag(1e-8, p)))
    }
    mu_new <- ybar + as.numeric(Lm %*% stats::rnorm(p))
    return(list(mu = mu_new, Sigma = Sigma_new))
  }

  # Burn-in.
  for (b in seq_len(burnin)) {
    i_step(mu, Sigma)
    st <- p_step(); mu <- st$mu; Sigma <- st$Sigma
  }
  # Kept draws, thinned.
  imputed <- vector("list", M)
  for (m in seq_len(M)) {
    for (t in seq_len(thin)) {
      i_step(mu, Sigma)
      st <- p_step(); mu <- st$mu; Sigma <- st$Sigma
    }
    imputed[[m]] <- Xc                           # completed data at this draw
  }
  return(list(imputed = imputed, psd_fail = psd_fail))
}
