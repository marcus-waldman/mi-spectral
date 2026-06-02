# verify_term_ac_nonmonotone.R  [todo/014 -- non-monotone (A)+(C) via Cox-Snell]
#
# R-side verification + assembly for the bivariate NON-MONOTONE (A)+(C) design-imbalance
# term, consuming the Cox-Snell b_Sigma derived by the CAS scripts
# (verification/cas-wolfram/verify_term_ac_nonmonotone{,_sympy}.py).
#
#   (A)+(C)_inf = alpha^T b_Sigma + 1/2 tr(H_phi I_obs^{-1})
#
# The alpha / H_phi / I_obs machinery is the pattern-general one validated for the
# monotone case (term-a-mar-closedform.R); ONLY b_Sigma is new (non-monotone => the
# observed-data likelihood does not factor => no monotone recursion).  This script:
#   (G2)  monotone-reduction gate: the verified bivariate-monotone recursion reproduces
#         the CAS monotone_reduction b_Sigma (drop the X2-missing group);
#   (G4)  direct Monte-Carlo gate: n*E[Sigma_hat_obs - Sigma] matches the CAS b_Sigma;
#   (G2b) empirical rem = A_rb - tr_obs (bivariate) matches the assembled (A)+(C)_inf;
#   (sweep) (A)+(C)(b) over selection strength b: -> 0 as b->0 (MCAR), grows with b.
#
# Setup matches the CAS scripts: bivariate N(0, [[1,.5],[.5,1]]); additive half-sigmoid
# MAR  P(miss1|x)=0.5*sigmoid(a+b x2), P(miss2|x)=0.5*sigmoid(a+b x1).
#
# Usage: Rscript verification/verify_term_ac_nonmonotone.R [R_bias] [R_mom] [n_cores] [N]

source("verification/00-setup.R")
suppressPackageStartupMessages({ library(parallel); library(mvtnorm) })
args <- commandArgs(trailingOnly = TRUE)
R_bias  = if (length(args) >= 1) { as.integer(args[1]) } else { 60000 }
R_mom   = if (length(args) >= 2) { as.integer(args[2]) } else { 4000 }
n_cores = if (length(args) >= 3) { as.integer(args[3]) } else { 20 }
N_use   = if (length(args) >= 4) { as.integer(args[4]) } else { 800 }

# ---- bivariate truth + parameter bookkeeping (vech order = column-major lower-tri) ----
p = 2
mu0 <- c(0, 0)
Sig0 <- matrix(c(1, 0.5, 0.5, 1), 2, 2)
k = p + p * (p + 1) / 2                       # = 5
lt <- which(lower.tri(Sig0, diag = TRUE), arr.ind = TRUE)   # rows: (1,1),(2,1),(2,2)
Epert <- function(s) { i = lt[s, 1]; j = lt[s, 2]; E <- matrix(0, p, p); E[i, j] <- 1; E[j, i] <- 1; return(E) }
TRUTH <- list(mu = mu0, Sigma = Sig0)

A_SEL  = as.numeric(Sys.getenv("TAMAR_A", "-0.4"))
BSWEEP = c(0.0, 0.4, 0.8, 1.2, 1.6)
B_HEAD = as.numeric(Sys.getenv("TAMAR_B", "1.6"))

# ---- non-monotone MAR mechanism: additive half-sigmoid ------------------------------
amp_nonmono <- function(X, bb = B_HEAD, a = A_SEL) {
  N <- nrow(X)
  wa <- 0.5 / (1 + exp(-(a + bb * X[, 2])))     # P(miss1: X1 missing) ~ observed x2
  wb <- 0.5 / (1 + exp(-(a + bb * X[, 1])))     # P(miss2: X2 missing) ~ observed x1
  u <- runif(N)
  patt <- ifelse(u < wa, 1L, ifelse(u < wa + wb, 2L, 0L))   # 1=miss1, 2=miss2, 0=complete
  Y <- X; R <- matrix(0, N, p)
  i1 <- which(patt == 1); if (length(i1)) { Y[i1, 1] <- NA; R[i1, 1] <- 1 }
  i2 <- which(patt == 2); if (length(i2)) { Y[i2, 2] <- NA; R[i2, 2] <- 1 }
  return(list(Y = Y, R = R))
}
amp_mono <- function(X, bb = B_HEAD, a = A_SEL) {  # monotone reduction: only miss1
  N <- nrow(X); wa <- 0.5 / (1 + exp(-(a + bb * X[, 2])))
  u <- runif(N); Y <- X; R <- matrix(0, N, p); i1 <- which(u < wa)
  if (length(i1)) { Y[i1, 1] <- NA; R[i1, 1] <- 1 }
  return(list(Y = Y, R = R))
}

# ---- bivariate FIML MLE (no closed form for non-monotone): direct optimisation ------
fiml_biv <- function(Y, R) {
  comp <- R[, 1] == 0 & R[, 2] == 0
  o1 <- R[, 1] == 0; o2 <- R[, 2] == 0           # x1 observed / x2 observed
  m1s = mean(Y[o1, 1]); m2s = mean(Y[o2, 2])
  s1s = mean((Y[o1, 1] - m1s)^2); s2s = mean((Y[o2, 2] - m2s)^2)
  if (sum(comp) >= 3) { s12s = cov(Y[comp, 1], Y[comp, 2]) } else { s12s = 0 }
  s12s = max(min(s12s, 0.95 * sqrt(s1s * s2s)), -0.95 * sqrt(s1s * s2s))
  L11 = sqrt(s1s); L21 = s12s / L11; L22 = sqrt(max(s2s - L21^2, 1e-6))
  par0 = c(m1s, m2s, log(L11), L21, log(L22))
  nll <- function(par) {
    mu <- par[1:2]; L <- matrix(c(exp(par[3]), par[4], 0, exp(par[5])), 2, 2); S <- L %*% t(L)
    ll = 0
    if (any(comp)) { ll = ll + sum(dmvnorm(Y[comp, , drop = FALSE], mu, S, log = TRUE)) }
    m1o <- o1 & !comp; if (any(m1o)) { ll = ll + sum(dnorm(Y[m1o, 1], mu[1], sqrt(S[1, 1]), log = TRUE)) }
    m2o <- o2 & !comp; if (any(m2o)) { ll = ll + sum(dnorm(Y[m2o, 2], mu[2], sqrt(S[2, 2]), log = TRUE)) }
    return(-ll)
  }
  opt <- tryCatch(optim(par0, nll, method = "BFGS", control = list(maxit = 200, reltol = 1e-10)),
                  error = function(e) { return(NULL) })
  if (is.null(opt)) { return(NULL) }
  mu <- opt$par[1:2]; L <- matrix(c(exp(opt$par[3]), opt$par[4], 0, exp(opt$par[5])), 2, 2)
  return(list(mu = mu, Sigma = L %*% t(L)))
}

# ---- moment pass (per-pattern selected moments + expected I_obs) -- pattern-general --
est_moments_biv <- function(amp_fun, N, R) {
  pacc <- list(); Iobs_sum <- matrix(0, k, k); n_ok = 0
  for (r in 1:R) {
    set.seed(880000 + r); X <- gen_data(N, mu0, Sig0)
    a <- tryCatch(amp_fun(X), error = function(e) { return(NULL) }); if (is.null(a)) { next }
    Rm <- a$R; n_ok = n_ok + 1
    patt <- apply(Rm, 1, function(row) { return(paste(row, collapse = "")) })
    for (pp in unique(patt)) {
      Rp <- Rm[which(patt == pp)[1], ]; O <- which(Rp == 0); if (length(O) == p) { next }
      rows <- which(patt == pp); e <- sweep(X[rows, O, drop = FALSE], 2, mu0[O], FUN = "-")
      if (is.null(pacc[[pp]])) { pacc[[pp]] <- list(count = 0, s1 = numeric(p), s2 = matrix(0, p, p), O = O, M = which(Rp == 1)) }
      pacc[[pp]]$count <- pacc[[pp]]$count + nrow(e)
      pacc[[pp]]$s1[O] <- pacc[[pp]]$s1[O] + colSums(e)
      pacc[[pp]]$s2[O, O] <- pacc[[pp]]$s2[O, O] + crossprod(e)
    }
    Iobs_sum <- Iobs_sum + observed_info_obs_mvn(list(mu = mu0, Sigma = Sig0), a$Y, Rm)
  }
  pm <- list()
  for (key in names(pacc)) { a <- pacc[[key]]; O <- a$O
    pm[[key]] <- list(frac = a$count / (N * n_ok), m1 = a$s1[O] / a$count,
                      M2 = a$s2[O, O, drop = FALSE] / a$count, O = O, M = a$M) }
  return(list(pm = pm, Iobs = Iobs_sum / n_ok, N = N))
}

alpha_expected_biv <- function(mm, N) {
  alpha <- numeric(k)
  for (key in names(mm$pm)) { P <- mm$pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    U <- solve(Sig0[O, O, drop = FALSE]); B0 <- Sig0[M, O, drop = FALSE] %*% U
    S0i <- solve(Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE])
    for (s in 1:(k - p)) { E <- Epert(s)
      dS <- E[M, M, drop = FALSE] - E[M, O, drop = FALSE] %*% t(B0) - B0 %*% E[O, M, drop = FALSE] +
            B0 %*% E[O, O, drop = FALSE] %*% t(B0)
      alpha[p + s] <- alpha[p + s] - 0.5 * nP * sum(diag(S0i %*% dS)) } }
  return(alpha)
}

hphi_expected_biv <- function(mm, N) {
  H <- matrix(0, k, k)
  for (key in names(mm$pm)) { P <- mm$pm[[key]]; O <- P$O; M <- P$M; nP = P$frac * N
    U <- solve(Sig0[O, O, drop = FALSE]); B0 <- Sig0[M, O, drop = FALSE] %*% U
    S0i <- solve(Sig0[M, M, drop = FALSE] - B0 %*% Sig0[O, M, drop = FALSE])
    m1 <- P$m1; M2 <- P$M2
    Dmu <- matrix(0, length(M), p); for (jj in seq_along(M)) { Dmu[jj, M[jj]] <- 1 }; Dmu[, O] <- -B0
    GU <- vector("list", k - p); Gs <- vector("list", k - p)
    for (s in 1:(k - p)) { E <- Epert(s); G <- E[M, O, drop = FALSE] - B0 %*% E[O, O, drop = FALSE]
      Gs[[s]] <- G; GU[[s]] <- G %*% U }
    Hp <- matrix(0, k, k); Hp[1:p, 1:p] <- -t(Dmu) %*% S0i %*% Dmu
    for (s in 1:(k - p)) { v <- as.numeric(GU[[s]] %*% m1); col <- -t(Dmu) %*% (S0i %*% v)
      Hp[1:p, p + s] <- col; Hp[p + s, 1:p] <- col }
    for (aa in 1:(k - p)) { for (bb in aa:(k - p)) {
      qpart = -sum(diag(t(GU[[aa]]) %*% S0i %*% GU[[bb]] %*% M2))
      tpart = 0.5 * sum(diag(S0i %*% (Gs[[aa]] %*% U %*% t(Gs[[bb]]) + Gs[[bb]] %*% U %*% t(Gs[[aa]]))))
      Hp[p + aa, p + bb] <- qpart + tpart; Hp[p + bb, p + aa] <- Hp[p + aa, p + bb] } }
    H <- H + nP * Hp }
  return(H)
}

assemble_AC <- function(amp_fun, bvech, N, R_mom) {
  mm <- est_moments_biv(amp_fun, N, R_mom)
  al <- alpha_expected_biv(mm, N); Hphi <- hphi_expected_biv(mm, N)
  A = sum(al * c(numeric(p), bvech) / N)
  C = 0.5 * sum(diag(Hphi %*% solve(mm$Iobs)))
  return(c(A = A, C = C, AC = A + C))
}

# ---- monotone-reduction recursion (verified bivariate closed form) ------------------
mono_recursion_bSigma <- function(R_mom) {
  fc_acc = 0; sx2 = 0; sxx2 = 0; n_units = 0
  for (r in 1:R_mom) {
    set.seed(770000 + r); X <- gen_data(2000, mu0, Sig0); a <- amp_mono(X)
    comp <- a$R[, 1] == 0; n_units = n_units + nrow(X); fc_acc = fc_acc + sum(comp)
    x2c <- X[comp, 2]; sx2 = sx2 + sum(x2c); sxx2 = sxx2 + sum(x2c^2)
  }
  f_c = fc_acc / n_units; m2_sel = sx2 / fc_acc; s22_sel = sxx2 / fc_acc - m2_sel^2
  beta = Sig0[1, 2] / Sig0[2, 2]; tau2 = Sig0[1, 1] - Sig0[1, 2]^2 / Sig0[2, 2]
  bX2X2 = -Sig0[2, 2]; bX1X2 = beta * bX2X2
  bX1X1 = -(2 / f_c) * tau2 + beta^2 * bX2X2 + (tau2 / f_c) * (Sig0[2, 2] / s22_sel)
  return(c(s11 = bX1X1, s12 = bX1X2, s22 = bX2X2, f_c = f_c, s22_sel = s22_sel))
}

# ---- read CAS b_Sigma (sympy sweep primary; wolfram for two-CAS check) ---------------
read_bsig <- function(path, scen) {
  if (!file.exists(path)) { return(NULL) }
  bs <- jsonlite::fromJSON(path)[[scen]]$b_sigma
  if (is.null(bs)) { return(NULL) }
  return(c(s11 = bs$s11, s12 = bs$s12, s22 = bs$s22))
}
spath <- "verification/cache/coxsnell-nonmonotone-bsigma-sympy.json"
wpath <- "verification/cache/coxsnell-nonmonotone-bsigma.json"
bkey  <- function(b) { sprintf("b%.1f", b) }
bSig_head      <- read_bsig(spath, bkey(B_HEAD))
bSig_head_wolf <- read_bsig(wpath, "nonmonotone")    # wolfram run at headline b (see below)
bSig_mono_cas  <- read_bsig(spath, "monotone_reduction")
if (is.null(bSig_head)) { stop("No SymPy b_Sigma sweep JSON; run verify_term_ac_nonmonotone_sympy.py first.") }

# ---- direct Monte-Carlo: n*E[Sigma_hat - Sigma] and empirical rem = A_rb - tr_obs ----
mc_one <- function(r, N, bb) {
  set.seed(660000 + r); X <- gen_data(N, mu0, Sig0); a <- amp_nonmono(X, bb = bb)
  if (sum(a$R[, 1] == 0 & a$R[, 2] == 0) < 5) { return(NULL) }
  to <- fiml_biv(a$Y, a$R); if (is.null(to)) { return(NULL) }
  dS <- to$Sigma - Sig0
  A_rb <- barQ_fiml_analytic(to, to, a$Y, a$R) - barQ_fiml_analytic(to, TRUTH, a$Y, a$R)
  tr_obs <- sum(diag(solve(observed_info_obs_mvn(to, a$Y, a$R), fisher_info_com_mvn(to, N)))) - k
  return(c(d11 = dS[1, 1], d12 = dS[1, 2], d22 = dS[2, 2], rem = A_rb - tr_obs, tr_obs = tr_obs))
}

cl <- makeCluster(n_cores)
invisible(clusterEvalQ(cl, { source("verification/00-setup.R"); suppressPackageStartupMessages(library(mvtnorm)) }))
clusterExport(cl, c("mu0", "Sig0", "p", "k", "A_SEL", "B_HEAD", "TRUTH", "amp_nonmono", "fiml_biv", "mc_one"))
mcse <- function(x) { return(sd(x) / sqrt(length(x))) }
run_bias <- function(N, bb) {
  M <- do.call(rbind, Filter(Negate(is.null), parLapply(cl, seq_len(R_bias), mc_one, N = N, bb = bb)))
  return(list(n = N, bb = bb, n_ok = nrow(M),
    nb11 = N * mean(M[, "d11"]), nb12 = N * mean(M[, "d12"]), nb22 = N * mean(M[, "d22"]),
    nb11_se = N * mcse(M[, "d11"]), nb12_se = N * mcse(M[, "d12"]), nb22_se = N * mcse(M[, "d22"]),
    rem = mean(M[, "rem"]), rem_se = mcse(M[, "rem"]), tr_obs = mean(M[, "tr_obs"])))
}

cat("\n================ NON-MONOTONE (A)+(C) via Cox-Snell -- verification ================\n")
cat(sprintf("theta0: mu=(0,0) Sigma=[[1,.5],[.5,1]]; mech a=%.2f; N=%d R_bias=%d R_mom=%d; headline b=%.1f\n",
            A_SEL, N_use, R_bias, R_mom, B_HEAD))

cat("\n-- two-CAS check at headline b (Wolfram NIntegrate vs SymPy Gauss-Hermite) --\n")
if (!is.null(bSig_head_wolf)) {
  cat(sprintf("   sympy  : s11=%+.5f s12=%+.5f s22=%+.5f\n", bSig_head[1], bSig_head[2], bSig_head[3]))
  cat(sprintf("   wolfram: s11=%+.5f s12=%+.5f s22=%+.5f\n", bSig_head_wolf[1], bSig_head_wolf[2], bSig_head_wolf[3]))
  d2cas = max(abs(bSig_head - bSig_head_wolf))
  cat(sprintf("   max|d| = %.2e  [%s]\n", d2cas, if (d2cas < 1e-4) { "PASS" } else { "(wolfram at different b -- rerun at headline)" }))
}

cat("\n-- G2: monotone-reduction recursion vs CAS (headline b) --\n")
mr <- mono_recursion_bSigma(R_mom)
cat(sprintf("   recursion  : s11=%+.5f s12=%+.5f s22=%+.5f  (f_c=%.4f, s22_sel=%.4f)\n",
            mr["s11"], mr["s12"], mr["s22"], mr["f_c"], mr["s22_sel"]))
cat(sprintf("   CAS (sympy): s11=%+.5f s12=%+.5f s22=%+.5f\n", bSig_mono_cas[1], bSig_mono_cas[2], bSig_mono_cas[3]))
d_mono = max(abs(mr[c("s11", "s12", "s22")] - bSig_mono_cas))
cat(sprintf("   recursion-vs-CAS max|d| = %.2e  [%s]\n", d_mono, if (d_mono < 5e-3) { "PASS" } else { "FAIL" }))

cat("\n-- (A)+(C) sweep over selection strength b  [(A)+(C)->0 as b->0 (MCAR)] --\n")
cat(sprintf("   %4s %10s %10s %12s\n", "b", "(A)", "(C)", "(A)+(C)"))
sweep_rows <- list()
for (b in BSWEEP) {
  bsg <- read_bsig(spath, bkey(b))
  ac <- assemble_AC(function(X) amp_nonmono(X, bb = b), bsg, N_use, R_mom)
  sweep_rows[[bkey(b)]] <- c(b = b, ac)
  cat(sprintf("   %4.1f %+10.4f %+10.4f %+12.4f\n", b, ac["A"], ac["C"], ac["AC"]))
}

cat("\n-- G4: direct MC n*E[Sigma_hat - Sigma] vs CAS b_Sigma (headline b) + empirical rem --\n")
bias_rows <- list()
for (N in unique(c(400, N_use, 1500))) {
  rb <- run_bias(N, B_HEAD); bias_rows[[as.character(N)]] <- rb
  cat(sprintf("   N=%4d (n_ok=%d): n*b11=%+.3f(%.3f) n*b12=%+.3f(%.3f) n*b22=%+.3f(%.3f) | rem=%+.4f(%.4f)\n",
              rb$n, rb$n_ok, rb$nb11, rb$nb11_se, rb$nb12, rb$nb12_se, rb$nb22, rb$nb22_se, rb$rem, rb$rem_se))
}
cat(sprintf("   CAS target  : n*b11=%+.3f   n*b12=%+.3f   n*b22=%+.3f\n", bSig_head[1], bSig_head[2], bSig_head[3]))

# empirical rem (MCAR control, b=0) and assembled comparison at headline
rb_mc <- run_bias(N_use, 0.0)
ac_head <- sweep_rows[[bkey(B_HEAD)]]
ac_mcar <- sweep_rows[[bkey(0.0)]]
rb_head <- bias_rows[[as.character(N_use)]]
cat("\n-- (A)+(C) assembled vs empirical rem = A_rb - tr_obs --\n")
cat(sprintf("   headline b=%.1f : (A)+(C)_assembled=%+.4f   empirical rem(N=%d)=%+.4f(%.4f)\n",
            B_HEAD, ac_head["AC"], N_use, rb_head$rem, rb_head$rem_se))
cat(sprintf("   MCAR     b=0.0 : (A)+(C)_assembled=%+.4f   empirical rem(N=%d)=%+.4f(%.4f)\n",
            ac_mcar["AC"], N_use, rb_mc$rem, rb_mc$rem_se))

stopCluster(cl)

out <- list(theta0 = list(mu = mu0, Sigma = Sig0), a_sel = A_SEL, bsweep = BSWEEP, b_head = B_HEAD,
            bSigma_head_sympy = bSig_head, bSigma_head_wolfram = bSig_head_wolf,
            mono_recursion = mr, mono_CAS = bSig_mono_cas,
            ac_sweep = do.call(rbind, sweep_rows), bias_mc = lapply(bias_rows, unlist),
            rem_head = c(rem = rb_head$rem, se = rb_head$rem_se),
            rem_mcar = c(rem = rb_mc$rem, se = rb_mc$rem_se))
dir.create("verification/cache", showWarnings = FALSE, recursive = TRUE)
saveRDS(out, "verification/cache/term-ac-nonmonotone-verify.rds")
cat("\nwrote verification/cache/term-ac-nonmonotone-verify.rds\n")
cat("================================================================================\n")
