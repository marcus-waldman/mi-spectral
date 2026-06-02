# scratch-realized-vs-expected.R  [todo/015 / todo/016]
#
# Decisive test of WHERE the -0.46-vs-(-0.24) gap lives. The empirical rem subtracts the
# REALIZED observed information (observed_info_obs_mvn, data-dependent Hessian) at the fit;
# my analytic leading-order (A)+(C) uses the EXPECTED observed information. Compute both,
# PAIRED per dataset (so A_rb cancels in the difference -> low variance):
#   rem_realized = A_rb - tr(RIV; observed-info Hessian)   [= committed empirical, ~ -0.46]
#   rem_expected = A_rb - tr(RIV; expected Fisher info)    [= my analytic leading order?]
#   gap          = rem_realized - rem_expected = tr_expected - tr_realized   (paired, precise)
# If rem_expected ~ -0.24 and the gap carries the rest, the -0.46 is a realized-information
# effect; if rem_expected ~ -0.46 too, the gap is elsewhere and a real O(1) term is missing.

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_data  = if (length(args) >= 1) { as.integer(args[1]) } else { 3000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 20 }

p = 4; mu0 <- default_mu; Sig0 <- default_Sigma; k = p + p*(p+1)/2
TRUTH <- list(mu = mu0, Sigma = Sig0)
amp_mar <- function(X) { return(apply_missingness_ampute(X, prop=0.40, mech="MAR", pattern_type="non_monotone")) }

one <- function(seed, N) {
  set.seed(seed); X <- gen_data(N, mu0, Sig0)
  mar <- tryCatch(amp_mar(X), error=function(e) NULL); if (is.null(mar)) { return(NULL) }
  if (sum(rowSums(mar$R)==0) < 8) { return(NULL) }
  to <- tryCatch(em_mvn(mar$Y), error=function(e) NULL); if (is.null(to)) { return(NULL) }
  to <- list(mu=to$mu, Sigma=to$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values=TRUE)$values) < 1e-6) { return(NULL) }
  A_rb <- barQ_fiml_analytic(to, to, mar$Y, mar$R) - barQ_fiml_analytic(to, TRUTH, mar$Y, mar$R)
  Icom <- fisher_info_com_mvn(to, N)
  tr_real <- sum(diag(solve(observed_info_obs_mvn(to, mar$Y, mar$R), Icom))) - k    # realized Hessian
  tr_exp  <- sum(diag(solve(fisher_info_obs_mvn(to, mar$Y, mar$R), Icom))) - k       # expected Fisher
  return(c(rem_real = A_rb - tr_real, rem_exp = A_rb - tr_exp,
           tr_real = tr_real, tr_exp = tr_exp, gap = tr_exp - tr_real))
}

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, source("verification/00-setup.R")))
clusterExport(cl, c("mu0","Sig0","p","k","TRUTH","amp_mar","one"))
mcse <- function(x) { return(sd(x)/sqrt(length(x))) }

cat("======== realized- vs expected-information decomposition of the (A)+(C) gap ========\n")
for (N in c(800, 1500)) {
  M <- do.call(rbind, Filter(Negate(is.null),
        parLapply(cl, seq_len(R_data), function(s, NN) one(770000+s, NN), NN=N)))
  cat(sprintf("\n-- N=%d (%d datasets) --\n", N, nrow(M)))
  cat(sprintf("   rem_realized = A_rb - tr_obs(Hessian)   = %+.4f (%.4f)   [committed empirical ~ %.3f]\n",
              mean(M[,"rem_real"]), mcse(M[,"rem_real"]), if (N==800) -0.336 else -0.456))
  cat(sprintf("   rem_expected = A_rb - tr_obs(Fisher)    = %+.4f (%.4f)   [my analytic leading order ~ -0.24?]\n",
              mean(M[,"rem_exp"]), mcse(M[,"rem_exp"])))
  cat(sprintf("   gap = tr_exp - tr_real (PAIRED)         = %+.4f (%.4f)   <-- realized-info contribution\n",
              mean(M[,"gap"]), mcse(M[,"gap"])))
}
stopCluster(cl)
cat("\n===================================================================================\n")
