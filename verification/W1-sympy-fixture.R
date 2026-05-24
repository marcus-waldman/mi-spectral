# W1-sympy-fixture.R
#
# Read-only consumer of the W1 primitives (00-setup.R) + the W1-sweep prod
# cache. Reproduces a single W1 replicate deterministically (the same seed
# convention as W1-sweep.R) and dumps every load-bearing intermediate to a
# JSON fixture that manuscript/derivation.qmd (Appendix B) reads.
#
# Appendix B reimplements I_com / I_obs / barQ_fiml / tr(RIV) in numpy and
# asserts machine-precision agreement against the values dumped here. That is
# the gate that the symbolic construction equals the R code the simulations
# actually ran. The cache aggregates (T_hat, MCSE, trRIV mean) anchor the
# softer "1/2 tr(RIV) within MCSE of E[T]" check.
#
# Usage:  Rscript verification/W1-sympy-fixture.R
# Output: manuscript/proof-verification-fixture.json

source("verification/00-setup.R")

CELL_PATTERN = "non_monotone"
CELL_MECH    = "MAR"
CELL_N       = 500
CELL_PROP    = 0.40
REP          = 1
CACHE_RDS    = "verification/cache/W1-sweep-prod/fiml_non_monotone_MAR_N500.rds"

# Reproduce run_one_W1(r = REP, ...) exactly: same seed, same call order.
set.seed(20260522 + REP)
X <- gen_data(N = CELL_N, mu = default_mu, Sigma = default_Sigma)
theta_com <- mle_complete_mvn(X)
ell_com_at_com = loglik_mvn(theta_com, X)

mar <- apply_missingness_ampute(X, prop = CELL_PROP, mech = CELL_MECH,
                                pattern_type = CELL_PATTERN)
fit_obs <- lavaan_fit_mvn_fiml(mar$Y, constrained = FALSE)
theta_obs <- list(mu = fit_obs$mu, Sigma = fit_obs$Sigma)

ell_com_at_obs = loglik_mvn(theta_obs, X)
barL_obs = barQ_fiml_analytic(theta_obs, theta_obs, mar$Y, mar$R)

riv_info <- tr_riv_analytic(theta_obs, mar$Y, mar$R)

T_r = barL_obs - ell_com_at_com
A_r = barL_obs - ell_com_at_obs
B_r = ell_com_at_obs - ell_com_at_com

# Cache aggregates for the MCSE band.
cache <- readRDS(CACHE_RDS)
T_arr = cache$T_arr
cache_block <- list(
  cell_id   = cache$cell$id,
  R_per_cell = cache$R_per_cell,
  T_hat     = mean(T_arr),
  T_mcse    = sd(T_arr) / sqrt(length(T_arr)),
  A_hat     = mean(cache$A_arr),
  A_mcse    = sd(cache$A_arr) / sqrt(length(cache$A_arr)),
  B_hat     = mean(cache$B_arr),
  B_mcse    = sd(cache$B_arr) / sqrt(length(cache$B_arr)),
  trRIV_mean = mean(cache$trRIV_arr),
  half_trRIV_pred = 0.5 * mean(cache$trRIV_arr)
)

fixture <- list(
  meta = list(
    note    = "Single W1 replicate (seed 20260522+1) + W1-sweep-prod cell aggregates.",
    pattern = CELL_PATTERN, mech = CELL_MECH, N = CELL_N, prop = CELL_PROP,
    rep     = REP, p = ncol(X),
    k       = ncol(X) + ncol(X) * (ncol(X) + 1) / 2
  ),
  truth = list(mu = default_mu, Sigma = default_Sigma),
  data  = list(X = X, Y = mar$Y, R = mar$R),
  theta_com = list(mu = theta_com$mu, Sigma = theta_com$Sigma),
  theta_obs = list(mu = theta_obs$mu, Sigma = theta_obs$Sigma),
  fisher = list(I_com = riv_info$I_com, I_obs = riv_info$I_obs),
  scalars = list(
    trRIV_replicate = riv_info$tr_RIV,
    ell_com_at_com  = ell_com_at_com,
    ell_com_at_obs  = ell_com_at_obs,
    barL_obs        = barL_obs,
    T_r = T_r, A_r = A_r, B_r = B_r
  ),
  cache = cache_block
)

out_path = "manuscript/proof-verification-fixture.json"
writeLines(jsonlite::toJSON(fixture, matrix = "rowmajor", digits = 17,
                            auto_unbox = TRUE, pretty = TRUE), out_path)
cat(sprintf("Wrote %s\n", out_path))
cat(sprintf("  trRIV(rep)=%.6f  T_r=%.6f  A_r=%.6f  B_r=%.6f\n",
            riv_info$tr_RIV, T_r, A_r, B_r))
cat(sprintf("  cache: T_hat=%.6f +/- %.6f  trRIV_mean=%.6f  half=%.6f\n",
            cache_block$T_hat, cache_block$T_mcse,
            cache_block$trRIV_mean, cache_block$half_trRIV_pred))
