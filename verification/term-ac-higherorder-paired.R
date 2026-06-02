# term-ac-higherorder-paired.R  [todo/020 -- decisive better simulation]
#
# QUESTION. Is the realized (A)+(C) = E[A_rb - tr(RIV)] captured by its second-order
# (delta-method) value (~ -0.22), with the leading correction O(1/n) -- so the raw MC mean's
# departure (pooled ~ -0.35) is heavy-tailed sampling noise? Or is there a GENUINE O(1)
# higher-order term (value ~ -0.35, -0.22 incomplete)? Direct MC cannot tell: sd(A_rb) ~ 0.65 sqrt(n)
# makes the mean un-pinnable. Variance reduction by a PAIRED control variate settles it.
#
# DESIGN. Per dataset, along the segment theta_0 -> theta_hat (delta = theta_hat - theta_0):
#   phi(t) = A_rb(theta_0 + t delta) = barQ(theta_t,theta_t,Y,R) - barQ(theta_t,TRUTH,Y,R),
#   phi(0) = 0 exactly; phi(1) = A_rb(theta_hat) exact.
#   phi'(0), phi''(0) by central FD at t=0 (cheap; a few barQ evals along delta).
#   taylor2 = phi'(0) + 1/2 phi''(0)            (2nd-order Taylor of phi at t=1)
#   resid   = phi(1) - taylor2 = 1/6 phi'''(0) + ...  (3rd+ order remainder)
# The O(sqrt n) noise lives in phi'(0) ~ g.delta and appears in BOTH phi(1) and taylor2, so it
# CANCELS in resid; sd(resid) ~ n^{-1/2} (DECREASES with n). Hence rbar_n = mean(resid) is
# pinnable, and it is exactly the higher-order correction:
#   full (A)+(C) = [2nd-order (A)+(C)] + rbar_n.
#
# VERDICT.
#   rbar_n -> 0 like 1/n  (n*rbar_n ~ const)  => remainder O(1/n); -0.22 is the asymptote;
#                                                the raw -0.35 mean is noise. (confirms reframing)
#   rbar_n -> const != 0                       => genuine O(1) higher-order term; value ~ -0.22 + const.
# Built-in check: mean(taylor2 - tr_obs) should land near the known 2nd-order -0.22 (validates FD).
#
# Usage: Rscript verification/term-ac-higherorder-paired.R [R] [cores] [Ns] [h]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel) })
args <- commandArgs(trailingOnly = TRUE)
R_data  = if (length(args) >= 1) { as.integer(args[1]) } else { 8000 }
n_cores = if (length(args) >= 2) { as.integer(args[2]) } else { 6 }
Ns      = if (length(args) >= 3) { as.integer(strsplit(args[3], ",")[[1]]) } else { c(800, 1500, 3000) }
h_fd    = if (length(args) >= 4) { as.numeric(args[4]) } else { 1e-2 }

p = 4; mu0 <- default_mu; Sig0 <- default_Sigma; k = p + p * (p + 1) / 2
TRUTH <- list(mu = mu0, Sigma = Sig0)

# A_rb along the segment theta_0 + t*delta, delta = (dmu, dSig).
phi_at <- function(t, dmu, dSig, Y, R) {
  th <- list(mu = mu0 + t * dmu, Sigma = Sig0 + t * dSig)
  return(barQ_fiml_analytic(th, th, Y, R) - barQ_fiml_analytic(th, TRUTH, Y, R))
}

one <- function(seed, N, h) {
  set.seed(seed)
  X <- gen_data(N, default_mu, default_Sigma)
  mar <- tryCatch(apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type = "non_monotone"),
                  error = function(e) { return(NULL) }); if (is.null(mar)) { return(NULL) }
  fit <- tryCatch(lavaan_fit_mvn_fiml(mar$Y, FALSE), error = function(e) { return(NULL) }); if (is.null(fit)) { return(NULL) }
  to <- list(mu = fit$mu, Sigma = fit$Sigma)
  if (any(!is.finite(to$Sigma)) || min(eigen(to$Sigma, only.values = TRUE)$values) < 1e-6) { return(NULL) }
  dmu <- to$mu - mu0; dSig <- to$Sigma - Sig0
  Y <- mar$Y; Rm <- mar$R
  phi1 <- phi_at(1, dmu, dSig, Y, Rm)                  # exact A_rb(theta_hat)
  php  <- phi_at(h, dmu, dSig, Y, Rm)                  # phi(+h)
  phm  <- phi_at(-h, dmu, dSig, Y, Rm)                 # phi(-h); phi(0)=0 exactly
  d1 <- (php - phm) / (2 * h)                          # phi'(0)
  d2 <- (php + phm) / (h^2)                            # phi''(0)  (phi(0)=0)
  taylor2 <- d1 + 0.5 * d2
  resid <- phi1 - taylor2
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, Y, Rm), fisher_info_com_mvn(to, N)))) - k
  return(c(A_rb = phi1, taylor2 = taylor2, resid = resid, tr_obs = tr_obs,
           ac_full = phi1 - tr_obs, ac_2nd = taylor2 - tr_obs))
}

mcse <- function(x) { return(sd(x) / sqrt(length(x))) }

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); suppressPackageStartupMessages(library(lavaan)) }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "TRUTH", "phi_at", "one"))

cat("====== higher-order PAIRED diagnostic: resid = A_rb - 2nd-order Taylor (variance-reduced) ======\n")
cat(sprintf("R=%d per N; h_fd=%.0e; design = phase-8 ampute MAR non-monotone.\n", R_data, h_fd))
cat("rbar_n = mean(resid) is the higher-order correction; full (A)+(C) = 2nd-order + rbar_n.\n")
cat("VERDICT: rbar_n ~ 1/n (n*rbar const) => -0.22 is the asymptote (raw -0.35 is noise);")
cat(" rbar_n ~ const != 0 => genuine O(1) term.\n\n")
rows <- list()
for (N in Ns) {
  M <- do.call(rbind, Filter(Negate(is.null),
        parLapply(cl, seq_len(R_data), function(s, NN, hh) one(20260522 + s, NN, hh), NN = N, hh = h_fd)))
  rb <- mean(M[, "resid"]); rb_se <- mcse(M[, "resid"])
  cat(sprintf("-- N=%4d (%d ok) --\n", N, nrow(M)))
  cat(sprintf("   rbar_n = mean(resid)              = %+.4f (%.4f)   [sd(resid)=%.3f]   n*rbar = %+.2f\n",
              rb, rb_se, sd(M[, "resid"]), N * rb))
  cat(sprintf("   2nd-order (A)+(C) = mean(taylor2 - tr_obs) = %+.4f (%.4f)   [target ~ -0.22; validates FD]\n",
              mean(M[, "ac_2nd"]), mcse(M[, "ac_2nd"])))
  cat(sprintf("   full (A)+(C)      = mean(A_rb - tr_obs)    = %+.4f (%.4f)   [noisy; should = 2nd + rbar]\n",
              mean(M[, "ac_full"]), mcse(M[, "ac_full"])))
  cat(sprintf("   check: (2nd) + rbar = %+.4f  vs  full = %+.4f   [paired, must agree]\n\n",
              mean(M[, "ac_2nd"]) + rb, mean(M[, "ac_full"])))
  rows[[as.character(N)]] <- c(N = N, rbar = rb, rbar_se = rb_se, n_rbar = N * rb,
                               ac_2nd = mean(M[, "ac_2nd"]), ac_full = mean(M[, "ac_full"]),
                               resid_sd = sd(M[, "resid"]), n_ok = nrow(M))
}
stopCluster(cl)
S <- do.call(rbind, rows)
cat("-- summary --\n"); print(round(S, 4))
cat(sprintf("\n   rbar_n trend: %s\n", paste(sprintf("N%d: %+.4f (n*rbar=%+.2f)", S[, "N"], S[, "rbar"], S[, "n_rbar"]), collapse = "  ")))
cat("   If n*rbar ~ constant => rbar = O(1/n) => -0.22 is the asymptote. If rbar ~ constant => genuine O(1).\n")
saveRDS(S, "verification/cache/higherorder-paired-diag.rds")
cat("\nwrote verification/cache/higherorder-paired-diag.rds\n")
cat("================================================================================================\n")
