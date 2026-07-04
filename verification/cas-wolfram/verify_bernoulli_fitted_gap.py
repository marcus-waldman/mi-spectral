#!/usr/bin/env python
r"""CAS verification for todo/045 Q2 (3a): the FITTED-arm deviance gap of a
canonical-link GLM under response-only MCAR missingness.

Claim verified here (derived 2026-07-04, todo/045 Sec.3a, BEFORE the N-scan or
any new simulation ran):

  For a one-parameter exponential-family response  f(y|x;beta) =
  h(y) exp{ y*eta - A(eta) },  eta = x'beta  (canonical link), with Y MCAR at
  rate r and X fully observed, the FITTED (deterministic FIML plug-in) arm has

     E[T_fitted] = +1/2 tr(RIV) + Delta_h + O(1/N),

  where the paper's design-imbalance pieces (derivation.qmd @sec-termA A4)

     (A) = alpha' E[delta],  alpha_i = (g'(eta_i) + eta_i A''(eta_i)) x_i
     (C) = 1/2 tr(H_phi I_obs^-1),  H_phi = sum_mis (g''+eta A''') x_i x_i'

  cancel EXACTLY at leading order in their (eta*A'', eta*A''') parts -- the
  Cox-Snell MLE bias term against the cross-entropy curvature term -- because
  eta is linear in X and, for a canonical link, the information weight and the
  third cumulant are the same A-derivatives:

     E[eta*w*X'] Omega^-1 E[A'''(X'Omega^-1 X) X] = E[eta*A'''(X'Omega^-1 X)]
     (Omega = E[w X X'], w = A'')                                  [Lemma P]

  The leftover Delta_h collects the base-measure terms g(eta) = E_eta[log h(Y)]:

     Delta_h = (r/(1-r)) * [ -1/2 E[g' X'] Omega^-1 E[A'''(X'Omega^-1 X) X]
                             +1/2 E[g'' X'Omega^-1 X] ]

  * Bernoulli (h == 1): g == 0, so Delta_h = 0 and the FITTED asymptote is
    EXACTLY the paper's general-case +1/2 tr(RIV). This resolves quorum
    objections OBJ-02/OBJ-06 (the +0.5 magnitude is now derived, not assumed).
  * Poisson (h = 1/y!): Delta_h != 0 -- an explicit, computable departure from
    +1/2, quadrature-evaluated below BEFORE any Poisson simulation existed in
    this repo (blind out-of-sample test of the framework).
  * Proper-draw corollary: a second-moment-proper draw beta* ~ (theta_obs,
    I_obs^-1) doubles the variance entering (C) only, so
       E[T_draw] - E[T_fitted] = 1/2 sum_mis (g''+eta A''') x'I_obs^-1 x + O(1/N)
    which for Bernoulli is the (C) functional Delta_c < 0.

Checks:
  [1] sympy: entropy identities H = A - eta A' - g;  for h==1:
      H' = -eta A'', H'' = -A'' - eta A''' (logistic, concrete).
  [2] sympy: Lemma P symbolically on a 3-point design with FREE symbols
      (w_k, t_k, m_k, x_k, b0, b1) -- exact zero; plus 12 random exact-rational
      4-point designs (probabilistic identity check over Q).
  [3] sympy: the canonical-GLM Cox-Snell bias b = -1/2 J^-1 sum A'''(x'J^-1 x)x
      reduces on the intercept-only design to the delta-method value
      -(1-2p)/(2 n w), i.e. E[logit(pbar)] - logit(p) to O(1/n).
  [4] exact enumeration (no Monte Carlo): intercept-only Bernoulli, p0 =
      plogis(0.3), r = 0.22 -- ratio(n) = E[T]*n_obs/n_mis -> 1/2 with O(1/n)
      residual (exact binomial sums; degenerate corners exactly handled, H=0).
  [5] exact enumeration: two-point design x = +/-1, beta0 = (0.3, 0.9) --
      E[beta_hat_obs] matches the Cox-Snell b (validates the bias formula on a
      covariate design), and ratio(n) -> 1/2.
  [6] Gauss-Hermite quadrature, the ACTUAL phase-3 design (X~N(0,1),
      beta0=(0.3,0.9), r=0.22): Lemma P numerically; the predicted proper-draw
      discount Delta_c/tr(RIV) = E[eta A''' X'Omega^-1 X]/(2q) -- printed next
      to the ALREADY-MEASURED paired N=200 value -0.2232 (se 0.0216) from
      verification/cache/phase3-nonnormal-prod.rds (measured 2026-07-03, before
      this formula was written -- disclosed in todo/045 Sec.3a).
  [7] Poisson design (same X, beta0): Delta_h/tr(RIV) by quadrature + series ->
      the registered Poisson FITTED target for the blind arm.
  [8] Student-t location (nu=5, sigma=1, both FIXED): H is location-free
      (dH/dmu = 0 exactly), so the registered known-scale exemplar targets are
      FITTED -> 0 and proper-draw -> -1/2 (numeric shift-invariance check).

Run:  py verification/cas-wolfram/verify_bernoulli_fitted_gap.py
Exit: 0 if all checks pass, 1 otherwise.
"""
import math
import sys

import numpy as np
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# [1] Entropy identities for a unit-base-measure canonical family (logistic)
# ---------------------------------------------------------------------------
print("== [1] entropy identities (h == 1, logistic) ==")
eta = sp.symbols("eta", real=True)
A = sp.log(1 + sp.exp(eta))
H = A - eta * sp.diff(A, eta)          # H = A - eta A'   (g == 0)
lhs1 = sp.simplify(sp.diff(H, eta) + eta * sp.diff(A, eta, 2))
lhs2 = sp.simplify(sp.diff(H, eta, 2) + sp.diff(A, eta, 2) + eta * sp.diff(A, eta, 3))
check("H' = -eta A''", lhs1 == 0)
check("H'' = -A'' - eta A'''", lhs2 == 0)
# and H really is the binary entropy -H(p) = p log p + (1-p) log(1-p)
p = sp.exp(eta) / (1 + sp.exp(eta))
Hp = -(p * sp.log(p) + (1 - p) * sp.log(1 - p))
check("H == binary entropy", sp.simplify(H - Hp) == 0)

# ---------------------------------------------------------------------------
# [2] Lemma P (projection cancellation), symbolic 3-point + rational 4-point
# ---------------------------------------------------------------------------
print("\n== [2] Lemma P: E[eta w X']Om^-1 E[t(X'Om^-1X)X] == E[eta t (X'Om^-1X)] ==")


def lemma_p_expr(K, xs, ms, ws, ts, b0, b1):
    X = [sp.Matrix([1, xs[k]]) for k in range(K)]
    etas = [b0 + b1 * xs[k] for k in range(K)]
    Om = sp.zeros(2, 2)
    for k in range(K):
        Om += ms[k] * ws[k] * (X[k] * X[k].T)
    Om_inv = Om.inv()
    v1 = sp.zeros(1, 2)   # E[eta w X']
    v2 = sp.zeros(2, 1)   # E[t (X'Om^-1X) X]
    rhs = sp.Integer(0)   # E[eta t (X'Om^-1X)]
    for k in range(K):
        q = (X[k].T * Om_inv * X[k])[0, 0]
        v1 += ms[k] * etas[k] * ws[k] * X[k].T
        v2 += ms[k] * ts[k] * q * X[k]
        rhs += ms[k] * etas[k] * ts[k] * q
    return (v1 * Om_inv * v2)[0, 0] - rhs


K = 3
xs = sp.symbols("x0:3", real=True)
ms = sp.symbols("m0:3", positive=True)
ws = sp.symbols("w0:3", positive=True)
ts = sp.symbols("t0:3", real=True)
b0, b1 = sp.symbols("b0 b1", real=True)
expr = lemma_p_expr(K, xs, ms, ws, ts, b0, b1)
check("symbolic 3-point design: identity == 0", sp.simplify(sp.together(expr)) == 0)

rng = np.random.default_rng(20260704)
ok_rat = True
for trial in range(12):
    subs = {}
    K4 = 4
    xs4 = sp.symbols("y0:4", real=True)
    ms4 = sp.symbols("n0:4", positive=True)
    ws4 = sp.symbols("v0:4", positive=True)
    ts4 = sp.symbols("s0:4", real=True)
    e4 = lemma_p_expr(K4, xs4, ms4, ws4, ts4, b0, b1)
    for s in list(xs4) + list(ts4) + [b0, b1]:
        subs[s] = sp.Rational(int(rng.integers(-9, 10)), int(rng.integers(1, 8)))
    for s in list(ms4) + list(ws4):
        subs[s] = sp.Rational(int(rng.integers(1, 12)), int(rng.integers(1, 6)))
    # make x-values distinct to keep Omega invertible
    xvals = {subs[s] for s in xs4}
    if len(xvals) < 4:
        continue
    val = sp.simplify(e4.subs(subs))
    if val != 0:
        ok_rat = False
        break
check("12 exact-rational 4-point designs: identity == 0", ok_rat)

# ---------------------------------------------------------------------------
# [3] Cox-Snell canonical bias reduces to the delta-method on intercept-only
# ---------------------------------------------------------------------------
print("\n== [3] Cox-Snell bias, intercept-only reduction ==")
n = sp.symbols("n", positive=True)
w_s = sp.diff(A, eta, 2)               # A''
t_s = sp.diff(A, eta, 3)               # A'''
J = n * w_s
b_formula = -(sp.Rational(1, 2)) * (1 / J) * (n * t_s * (1 / J))   # -1/2 J^-1 [n A''' (x'J^-1 x) x], x=1
# delta method: E[logit(pbar)] - eta ~ 1/2 g''(p) Var(pbar), g = logit, Var = w/n
ps = sp.symbols("ps", positive=True)
g2 = sp.diff(sp.log(ps / (1 - ps)), ps, 2).subs(ps, p)   # g'' evaluated at p(eta)
delta_val = sp.Rational(1, 2) * g2 * (w_s / n)           # w = p(1-p)
check("b_CoxSnell == delta-method bias (intercept-only)",
      sp.simplify(b_formula - delta_val) == 0,
      f"both = {sp.simplify(b_formula)}")

# ---------------------------------------------------------------------------
# numeric helpers
# ---------------------------------------------------------------------------
def plogis(x):
    return 1.0 / (1.0 + np.exp(-x))


def binH(pv):
    pv = np.asarray(pv, dtype=float)
    out = np.zeros_like(pv)
    inner = (pv > 0) & (pv < 1)
    q = pv[inner]
    out[inner] = -(q * np.log(q) + (1 - q) * np.log(1 - q))
    return out


def binom_pmf(nn, pp):
    k = np.arange(nn + 1)
    lg = np.array([math.lgamma(nn + 1) - math.lgamma(kk + 1) - math.lgamma(nn - kk + 1) for kk in k])
    return np.exp(lg + k * math.log(pp) + (nn - k) * math.log1p(-pp))


# ---------------------------------------------------------------------------
# [4] Intercept-only Bernoulli: exact ratio(n) -> 1/2
# ---------------------------------------------------------------------------
print("\n== [4] exact enumeration, intercept-only Bernoulli (p0 = plogis(0.3), r = 0.22) ==")
p0 = plogis(0.3)
r_miss = 0.22
rows = []
for ntot in [50, 100, 200, 400, 800, 1600]:
    n_mis = int(round(r_miss * ntot))
    n_obs = ntot - n_mis
    pmf_o = binom_pmf(n_obs, p0)
    pmf_m = binom_pmf(n_mis, p0)
    k_o = np.arange(n_obs + 1)
    k_m = np.arange(n_mis + 1)
    p_o = k_o / n_obs
    # T(k_o, k_m) = ntot * [H(p_com) - H(p_obs)]  (exact; edges give H = 0)
    p_c = (k_o[:, None] + k_m[None, :]) / ntot
    Tmat = ntot * (binH(p_c) - binH(p_o)[:, None])
    ET = float(pmf_o @ Tmat @ pmf_m)
    ratio = ET * n_obs / n_mis
    rows.append((ntot, ET, ratio))
    print(f"  n={ntot:5d}  E[T]={ET:+.6f}  ratio={ratio:+.6f}  (ratio-1/2)*n={(ratio-0.5)*ntot:+.3f}")
# convergence to 1/2 with O(1/n) residual: (ratio-0.5)*n should stabilize
resid_n = [(rat - 0.5) * ntot for ntot, _, rat in rows]
check("intercept-only ratio -> 1/2 (last |ratio-0.5| < 0.01)",
      abs(rows[-1][2] - 0.5) < 0.01,
      f"ratio(1600) = {rows[-1][2]:+.5f}")
check("intercept-only residual is O(1/n) ((ratio-0.5)*n stabilizes within 25% at the last two n)",
      abs(resid_n[-1] - resid_n[-2]) < 0.25 * max(abs(resid_n[-1]), abs(resid_n[-2]), 1e-9),
      f"(ratio-0.5)*n at n=800,1600: {resid_n[-2]:+.3f}, {resid_n[-1]:+.3f}")

# ---------------------------------------------------------------------------
# [5] Two-point design x = +/-1: exact E[beta_hat] vs Cox-Snell; ratio -> 1/2
# ---------------------------------------------------------------------------
print("\n== [5] exact enumeration, two-point design x=+/-1, beta0=(0.3,0.9), r=0.22 ==")
beta0 = np.array([0.3, 0.9])
p_plus = plogis(beta0[0] + beta0[1])
p_minus = plogis(beta0[0] - beta0[1])


def twopoint_exact(n_g):
    """n_g units at x=+1 and n_g at x=-1; per-group missing count = round(r*n_g).
    Saturated 2-cell model: beta1 = (etap+etam)/2, beta2 = (etap-etam)/2."""
    n_mis_g = int(round(r_miss * n_g))
    n_obs_g = n_g - n_mis_g
    pmf_op = binom_pmf(n_obs_g, p_plus)
    pmf_om = binom_pmf(n_obs_g, p_minus)
    pmf_mp = binom_pmf(n_mis_g, p_plus)
    pmf_mm = binom_pmf(n_mis_g, p_minus)
    k = np.arange(n_obs_g + 1)
    ph_o = k / n_obs_g
    # E[beta_hat_obs] excluding the degenerate cells (observed group all 0/1)
    inner = (k > 0) & (k < n_obs_g)
    mass_p = pmf_op[inner].sum()
    mass_m = pmf_om[inner].sum()
    etap = np.log(ph_o[inner] / (1 - ph_o[inner]))
    etam = etap  # same grid; expectations taken separately below
    Ep = (pmf_op[inner] / mass_p) @ etap
    Em = (pmf_om[inner] / mass_m) @ np.log(ph_o[inner] / (1 - ph_o[inner]))
    Eb1 = 0.5 * (Ep + Em)
    Eb2 = 0.5 * (Ep - Em)
    excl_mass = 1 - mass_p * mass_m
    # Cox-Snell b at the observed design: per group, intercept-only-in-group
    #   E[eta_hat_g] - eta_g = -(1-2p_g)/(2 n_obs_g w_g)
    bp = -(1 - 2 * p_plus) / (2 * n_obs_g * (p_plus * (1 - p_plus)))
    bm = -(1 - 2 * p_minus) / (2 * n_obs_g * (p_minus * (1 - p_minus)))
    b_cs = np.array([0.5 * (bp + bm), 0.5 * (bp - bm)])
    # E[T]: per group T_g = n_g [H(p_com,g) - H(p_obs,g)], groups independent
    ET = 0.0
    for pmf_o_g, pmf_m_g, pg in [(pmf_op, pmf_mp, p_plus), (pmf_om, pmf_mm, p_minus)]:
        k_o = np.arange(n_obs_g + 1)
        k_m = np.arange(n_mis_g + 1)
        p_o = k_o / n_obs_g
        p_c = (k_o[:, None] + k_m[None, :]) / n_g
        Tg = n_g * (binH(p_c) - binH(p_o)[:, None])
        ET += float(pmf_o_g @ Tg @ pmf_m_g)
    trRIV_exact = 2.0 * n_mis_g / n_obs_g   # q=2, homogeneous within groups
    return np.array([Eb1, Eb2]) - beta0, b_cs, excl_mass, ET, ET / trRIV_exact


for n_g in [60, 120, 240]:
    bias_exact, b_cs, excl, ET, ratio = twopoint_exact(n_g)
    print(f"  n_g={n_g:4d}: exact E[beta_hat]-beta0 = ({bias_exact[0]:+.5f},{bias_exact[1]:+.5f})"
          f"  CoxSnell = ({b_cs[0]:+.5f},{b_cs[1]:+.5f})  excl.mass={excl:.2e}"
          f"  ratio = {ratio:+.5f}")
bias_exact, b_cs, excl, ET, ratio = twopoint_exact(240)
check("two-point: exact MLE bias matches Cox-Snell within 15% (n_g=240, both comps)",
      np.all(np.abs(bias_exact - b_cs) <= 0.15 * np.abs(b_cs) + 1e-5),
      f"exact {bias_exact}, formula {b_cs}")
check("two-point: ratio -> 1/2 (|ratio-0.5| < 0.02 at n_g=240)",
      abs(ratio - 0.5) < 0.02, f"ratio = {ratio:+.5f}")

# ---------------------------------------------------------------------------
# [6] The actual phase-3 Bernoulli design: quadrature constants
# ---------------------------------------------------------------------------
print("\n== [6] Gauss-Hermite quadrature, phase-3 design X~N(0,1), beta0=(0.3,0.9) ==")
nodes, wts = np.polynomial.hermite_e.hermegauss(160)
wts = wts / math.sqrt(2 * math.pi)
x_nodes = nodes
eta_v = beta0[0] + beta0[1] * x_nodes
p_v = plogis(eta_v)
w_v = p_v * (1 - p_v)
t_v = w_v * (1 - 2 * p_v)                      # A'''
X_mat = np.stack([np.ones_like(x_nodes), x_nodes], axis=1)
Om = (X_mat * (wts * w_v)[:, None]).T @ X_mat   # E[w X X']
Om_inv = np.linalg.inv(Om)
qform = np.einsum("ij,jk,ik->i", X_mat, Om_inv, X_mat)   # X'Om^-1X per node
K_functional = float(np.sum(wts * eta_v * t_v * qform))  # E[eta A''' X'Om^-1 X]
lhs_vec = (wts * eta_v * w_v) @ X_mat                     # E[eta w X']
rhs_vec = (wts * t_v * qform) @ X_mat                     # E[A''' (X'Om^-1X) X]
lemmaP_num = float(lhs_vec @ Om_inv @ rhs_vec) - K_functional
check("Lemma P numerically on the N(0,1) design (|diff| < 1e-10)",
      abs(lemmaP_num) < 1e-10, f"diff = {lemmaP_num:.2e}")
q_dim = 2
draw_discount = K_functional / (2 * q_dim)
print(f"  K = E[eta A''' X'Om^-1 X]            = {K_functional:+.6f}")
print(f"  predicted (T_draw - T_fitted)/trRIV  = K/(2q) = {draw_discount:+.6f}")
print(f"  measured  (N=200, R=1000, cache)     = -0.2232 (se 0.0216)  [paired, analytic den]")
print(f"  predicted FITTED asymptote           = +0.5 exactly (Delta_h = 0, h == 1)")
N_ref, r_ref = 200, 0.22
n_obs_ref = int(round((1 - r_ref) * N_ref))
b_ref = -0.5 * (Om_inv @ rhs_vec) / n_obs_ref * (1 - r_ref) ** 0  # J_obs ~ n_obs*Om
# more precisely: b = -1/2 (n_obs Om)^-1 * n_obs E[A'''(X'(n_obs Om)^-1 X)X] = -1/(2 n_obs) Om^-1 rhs_vec
print(f"  Cox-Snell b at n_obs={n_obs_ref}: ({b_ref[0]:+.5f}, {b_ref[1]:+.5f})  (magnitude reference)")
check("draw-discount prediction within 2 se of the measured paired value",
      abs(draw_discount - (-0.2232)) < 2 * 0.0216,
      f"pred {draw_discount:+.4f} vs meas -0.2232 +/- 0.0216")

# ---------------------------------------------------------------------------
# [7] Poisson design: Delta_h by quadrature + series (registered blind target)
# ---------------------------------------------------------------------------
print("\n== [7] Poisson (log link, canonical), X~N(0,1), beta0=(0.3,0.9): Delta_h ==")
# truncate the node set for the Poisson part: beyond |x| = 8 the GH weight is
# < 4e-15 while the integrands grow only polynomially-in-mu times mu ~ e^eta,
# so dropped mass is < 1e-11; this keeps the log(y!) series lengths sane.
mask = np.abs(x_nodes) <= 8.0
xs_p = x_nodes[mask]
wts_p = wts[mask]
eta_p = beta0[0] + beta0[1] * xs_p
X_p = np.stack([np.ones_like(xs_p), xs_p], axis=1)
mu_v = np.exp(eta_p)


def pois_E_log_factorial_terms(mu):
    """Return (E[log(y+1)], E[log((y+2)/(y+1))]) under Poisson(mu), by series."""
    kmax = int(mu + 15 * math.sqrt(mu) + 30)
    k = np.arange(kmax + 1)
    logpmf = k * math.log(mu) - mu - np.array([math.lgamma(kk + 1) for kk in k])
    pmf = np.exp(logpmf)
    E1 = float(pmf @ np.log(k + 1.0))
    E2 = float(pmf @ np.log((k + 2.0) / (k + 1.0)))
    return E1, E2


# g(eta) = E[log h] = -E[log y!];  dg/deta = -mu E[log(y+1)];
# d2g/deta2 = -mu E[log(y+1)] - mu^2 E[log((y+2)/(y+1))]
gp = np.empty_like(mu_v)
gpp = np.empty_like(mu_v)
for i, mu in enumerate(mu_v):
    E1, E2 = pois_E_log_factorial_terms(mu)
    gp[i] = -mu * E1
    gpp[i] = -mu * E1 - mu * mu * E2
w_pois = mu_v                    # A'' = mu
t_pois = mu_v                    # A''' = mu
Om_p = (X_p * (wts_p * w_pois)[:, None]).T @ X_p
Om_p_inv = np.linalg.inv(Om_p)
qform_p = np.einsum("ij,jk,ik->i", X_p, Om_p_inv, X_p)
lhs_g = (wts_p * gp) @ X_p                       # E[g' X']
rhs_p = (wts_p * t_pois * qform_p) @ X_p         # E[A'''(X'Om^-1X)X]
term_bias = -0.5 * float(lhs_g @ Om_p_inv @ rhs_p)
term_curv = 0.5 * float(np.sum(wts_p * gpp * qform_p))
Delta_h_over_tr = (term_bias + term_curv) / q_dim   # (r/(1-r)) cancels against tr(RIV)
# also confirm the (eta w, eta A''') parts cancel for Poisson too (Lemma P is family-generic)
lhsP = (wts_p * eta_p * w_pois) @ X_p
KP = float(np.sum(wts_p * eta_p * t_pois * qform_p))
check("Lemma P numerically on the Poisson design (|diff| < 1e-9)",
      abs(float(lhsP @ Om_p_inv @ rhs_p) - KP) < 1e-9)
print(f"  bias part  (-1/2 E[g'X']Om^-1E[A'''qX])/q = {term_bias / q_dim:+.6f}")
print(f"  curv part  (+1/2 E[g'' q])/q              = {term_curv / q_dim:+.6f}")
print(f"  Delta_h / tr(RIV)                          = {Delta_h_over_tr:+.6f}")
print(f"  REGISTERED Poisson FITTED target           = 0.5 + ({Delta_h_over_tr:+.4f}) "
      f"= {0.5 + Delta_h_over_tr:+.4f}")

# ---------------------------------------------------------------------------
# [8] Student-t location, fixed scale/df: entropy is location-free
# ---------------------------------------------------------------------------
print("\n== [8] Student-t(nu=5, sigma=1) location: known-scale exemplar targets ==")
nu = 5.0


def t_logpdf(z, nu_):
    c = math.lgamma((nu_ + 1) / 2) - math.lgamma(nu_ / 2) - 0.5 * math.log(nu_ * math.pi)
    return c - (nu_ + 1) / 2 * np.log1p(z * z / nu_)


zg = np.linspace(-60, 60, 400001)
fz = np.exp(t_logpdf(zg, nu))
H_num = -np.trapezoid(fz * t_logpdf(zg, nu), zg)
H_closed = ((nu + 1) / 2) * (sp.digamma((nu + 1) / 2) - sp.digamma(nu / 2)) \
    + sp.log(sp.sqrt(nu) * sp.beta(nu / 2, sp.Rational(1, 2)))
H_closed = float(H_closed)
check("t entropy: numeric == closed form (|diff| < 1e-6)",
      abs(H_num - H_closed) < 1e-6, f"H = {H_closed:.6f}")
# location-free: entropy of f(.-mu) is the same integral after substitution --
# verify numerically at mu = 0 and mu = 3 on an absolute grid
for mu_test in [0.0, 3.0]:
    fz2 = np.exp(t_logpdf(zg - mu_test, nu))
    H2 = -np.trapezoid(fz2 * t_logpdf(zg - mu_test, nu), zg)
    check(f"t entropy is location-free (mu={mu_test})", abs(H2 - H_closed) < 1e-5)
I1_t = (nu + 1) / (nu + 3)   # per-unit Fisher info, sigma=1
print(f"  per-unit Fisher info I1 = (nu+1)/(nu+3) = {I1_t:.4f}")
print(f"  REGISTERED t-exemplar targets: FITTED -> 0 exactly; proper-draw -> -1/2 tr(RIV)")

# ---------------------------------------------------------------------------
print("\n== summary ==")
if FAIL:
    print("FAILED checks:", ", ".join(FAIL))
    sys.exit(1)
print("All checks pass.")
print(f"Registered constants (todo/045 Sec.3, 2026-07-04):")
print(f"  Bernoulli FITTED asymptote          : +0.5000 (Delta_h = 0)")
print(f"  Bernoulli draw-fitted discount ratio: {draw_discount:+.4f}")
print(f"  Poisson  FITTED asymptote           : {0.5 + Delta_h_over_tr:+.4f}")
print(f"  Student-t exemplar                  : FITTED 0, draw -0.5")
sys.exit(0)
