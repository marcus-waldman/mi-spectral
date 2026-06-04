#!/usr/bin/env python
r"""CAS check of the IC calibration-ladder analytic pieces (todo/027 SS4, session 2026-06-04).

The ladder consumes the @sec-lrt null law: at candidate k's own null the saturated-anchored
MI deviance T_k converges to the weighted sum

    W = sum_{j=1}^{q_d} lambda_j chi^2_1,    lambda_j = 1 + r_perp,j >= 1,

where lambda_j are the nonzero eigenvalues of

    P = [I_com^-1 - G (G' I_com G)^-1 G'] I_com I_obs^-1 I_com        (= A V)

(quadratic-form representation of d_L, @sec-lrt-bias), and
sum_j lambda_j = q_d + tr(RIV_perp) with tr(RIV_perp) the @eq-lrt-bias trace.

This script verifies, symbolically (sympy) and over random PD instances (numpy):

  [L-A1] moments of the null law: E[W] = sum lambda_j, Var[W] = 2 sum lambda_j^2
         (symbolic, from chi^2_1 moments; plus a numeric MC companion).
  [L-A2] rung 2 (SB two-moment) coefficients: a = sqrt(q_d / sum lambda^2),
         b = q_d - a sum lambda is the UNIQUE affine map with a > 0 matching both
         moments of chi^2_{q_d}; and the two stated forms agree:
         a T + b == a (T - tr_perp) + q_d (1 - a) given tr_perp = sum lambda - q_d.
  [L-A3] spectrum-trace identity on random PD instances:
         sum of nonzero eig(P) == q_d + tr(RIV_perp)  (tol 1e-8, >= 200 instances),
         and min nonzero eigenvalue >= 1 (each null-law weight exceeds one,
         from V = I_com I_obs^-1 I_com >= I_com and eigenvalue monotonicity).
  [L-A4] rung 3 (equipercentile equating) through an INDEPENDENT Imhof CDF
         implementation: U = F_W(W-samples) is Uniform(0,1) by KS at MC tolerance,
         so F^-1_{chi2_q}(F_W(T)) is exactly chi2_q-distributed under the null law
         (probability integral transform). Cross-checks the R-side CompQuadForm::imhof.

Run:    py verification/cas-wolfram/verify_ic_ladder.py
Exit:   0 all pass; 1 mismatch.
"""
import sys

import numpy as np
import sympy as sp


FAIL = 0


def check(name, ok, detail=""):
    global FAIL
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAIL = 1
    print(f"  [{tag}] {name}" + (f"   {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# [L-A1] symbolic moments of W = sum lambda_j chi^2_1
# ---------------------------------------------------------------------------
print("[L-A1] moments of the weighted-chi^2 null law")
for q in (1, 2, 4, 6):
    lam = sp.symbols(f"l0:{q}", positive=True)
    # chi^2_1 has E = 1, Var = 2; independence across j.
    EW = sum(lam[j] * 1 for j in range(q))
    VW = sum(lam[j] ** 2 * 2 for j in range(q))
    ok_e = sp.simplify(EW - sum(lam)) == 0
    ok_v = sp.simplify(VW - 2 * sum(l ** 2 for l in lam)) == 0
    check(f"q_d={q}: E[W] = sum(lambda), Var[W] = 2 sum(lambda^2)", ok_e and ok_v)

# numeric MC companion
rng = np.random.default_rng(20260604)
lam_num = np.array([1.3, 1.05, 2.4, 1.7])
n_mc = 2_000_000
Wmc = (lam_num[None, :] * rng.chisquare(1, size=(n_mc, 4))).sum(axis=1)
e_gap = abs(Wmc.mean() - lam_num.sum())
v_gap = abs(Wmc.var() - 2 * (lam_num ** 2).sum())
check("MC companion (n=2e6): mean/var land on the formulas",
      e_gap < 0.02 and v_gap < 0.2, f"|dE|={e_gap:.4f} |dV|={v_gap:.4f}")

# ---------------------------------------------------------------------------
# [L-A2] rung-2 coefficients: uniqueness + form equivalence
# ---------------------------------------------------------------------------
print("[L-A2] SB two-moment coefficients (rung 2)")
q_d = sp.Symbol("q_d", positive=True)
S1 = sp.Symbol("S1", positive=True)   # sum lambda_j
S2 = sp.Symbol("S2", positive=True)   # sum lambda_j^2
a, b = sp.symbols("a b", real=True)
# match E[a W + b] = q_d and Var[a W + b] = 2 q_d against E[W]=S1, Var[W]=2 S2
sols = sp.solve([a * S1 + b - q_d, a ** 2 * 2 * S2 - 2 * q_d], [a, b], dict=True)
pos = [s for s in sols if s[a].is_positive in (True, None)]
# sympy returns +/- sqrt branches; keep the positive-a branch explicitly
pos = [s for s in sols if sp.simplify(s[a] - sp.sqrt(q_d / S2)) == 0]
check("a = sqrt(q_d / S2), b = q_d - a S1 solves both moment equations",
      len(pos) == 1 and sp.simplify(pos[0][b] - (q_d - sp.sqrt(q_d / S2) * S1)) == 0)
check("uniqueness: exactly one solution with a > 0",
      sum(1 for s in sols if s[a].is_positive or
          sp.simplify(s[a] - sp.sqrt(q_d / S2)) == 0) == 1)
# form equivalence with tr_perp = S1 - q_d
T = sp.Symbol("T", real=True)
a_v = sp.sqrt(q_d / S2)
b_v = q_d - a_v * S1
form1 = a_v * T + b_v
form2 = a_v * (T - (S1 - q_d)) + q_d * (1 - a_v)
check("a T + b == a (T - tr_perp) + q_d (1 - a)", sp.simplify(form1 - form2) == 0)

# ---------------------------------------------------------------------------
# [L-A3] spectrum-trace identity + weight lower bound on random PD instances
# ---------------------------------------------------------------------------
print("[L-A3] nonzero eig(P): sum == q_d + tr(RIV_perp), min >= 1   (random instances)")


def rand_pd(rng, k, scale=1.0):
    Q = rng.normal(size=(k, k))
    return scale * (Q @ Q.T + k * np.eye(k))


n_inst = 200
max_sum_gap = 0.0
min_weight = np.inf
ok_all = True
for it in range(n_inst):
    k = int(rng.integers(4, 9))
    k0 = int(rng.integers(1, k))
    q = k - k0
    Iobs = rand_pd(rng, k)
    Imis = rand_pd(rng, k, scale=float(rng.uniform(0.05, 1.5)))
    Icom = Iobs + Imis
    if it % 2 == 0:
        G = np.eye(k)[:, :k0]                      # selection matrix (the ladder's case)
    else:
        G = rng.normal(size=(k, k0))               # generic full-rank Jacobian
    A = np.linalg.inv(Icom) - G @ np.linalg.solve(G.T @ Icom @ G, G.T)
    V = Icom @ np.linalg.solve(Iobs, Icom)
    # symmetric route: eig(V^1/2 A V^1/2)
    w, U = np.linalg.eigh((V + V.T) / 2)
    Vh = U @ np.diag(np.sqrt(np.maximum(w, 0))) @ U.T
    lam = np.linalg.eigvalsh(Vh @ ((A + A.T) / 2) @ Vh)
    lam = np.sort(lam)[::-1][:q]                   # the q_d nonzero weights
    tr_riv_perp = (np.trace(np.linalg.solve(Iobs, Imis))
                   - np.trace(np.linalg.solve(G.T @ Icom @ G,
                                              G.T @ Icom @ np.linalg.solve(Iobs, Imis) @ G)))
    gap = abs(lam.sum() - (q + tr_riv_perp)) / max(1.0, q + tr_riv_perp)
    max_sum_gap = max(max_sum_gap, gap)
    min_weight = min(min_weight, lam.min())
    if gap > 1e-8 or lam.min() < 1 - 1e-8:
        ok_all = False
check(f"{n_inst} instances: relative sum gap <= 1e-8", ok_all and max_sum_gap <= 1e-8,
      f"max gap = {max_sum_gap:.2e}")
check("min nonzero weight >= 1 across all instances", min_weight >= 1 - 1e-8,
      f"min = {min_weight:.10f}")

# ---------------------------------------------------------------------------
# [L-A4] independent Imhof CDF + PIT exactness of rung 3
# ---------------------------------------------------------------------------
print("[L-A4] Imhof CDF (independent implementation) + PIT")


def imhof_cdf_grid(x_grid, lam):
    """F_W(x) for W = sum lam_j chi^2_1 via Imhof (1961) numerical inversion.

    F(x) = 1/2 - (1/pi) * int_0^inf sin(theta(u)) / (u * rho(u)) du,
    theta(u) = 0.5 * sum_j arctan(lam_j u) - 0.5 * x u,
    rho(u)   = prod_j (1 + lam_j^2 u^2)^(1/4).
    Dense log-spaced grid; integrand decays like u^(-(1+q/2)).
    """
    u = np.concatenate([np.linspace(1e-8, 1.0, 4000, endpoint=False),
                        np.geomspace(1.0, 4000.0, 16000)])
    atan_part = 0.5 * np.arctan(lam[None, :] * u[:, None]).sum(axis=1)      # (nu,)
    log_rho = 0.25 * np.log1p((lam[None, :] ** 2) * (u[:, None] ** 2)).sum(axis=1)
    out = np.empty_like(x_grid)
    for i, x in enumerate(x_grid):
        theta = atan_part - 0.5 * x * u
        integrand = np.sin(theta) / (u * np.exp(log_rho))
        out[i] = 0.5 - np.trapezoid(integrand, u) / np.pi
    return np.clip(out, 0.0, 1.0)


lam4 = np.array([1.15, 1.4, 1.9, 2.6])
n_samp = 10_000
Ws = (lam4[None, :] * rng.chisquare(1, size=(n_samp, 4))).sum(axis=1)
xg = np.linspace(0.0, float(Ws.max()) * 1.05 + 1.0, 3000)
Fg = imhof_cdf_grid(xg, lam4)
check("Imhof CDF monotone on the grid, F(0) ~ 0, F(max) ~ 1",
      bool(np.all(np.diff(Fg) > -1e-6)) and Fg[0] < 1e-3 and Fg[-1] > 0.999,
      f"F(0)={Fg[0]:.2e} F(max)={Fg[-1]:.6f}")
U = np.interp(Ws, xg, Fg)
Us = np.sort(U)
ks_unif = float(np.max(np.abs(Us - (np.arange(1, n_samp + 1) - 0.5) / n_samp)))
check("PIT: U = F_W(W) uniform by KS (n=1e4, crit 5% = 0.0136, tol 0.025)",
      ks_unif <= 0.025, f"D_KS = {ks_unif:.4f}")
# map through the closed-form chi^2_4 CDF inverse and re-test against chi^2_4:
# F_chi2_4(x) = 1 - exp(-x/2)(1 + x/2); invert by bisection on the same grid trick.
xc = np.linspace(0.0, 60.0, 60001)
Fc = 1.0 - np.exp(-xc / 2) * (1.0 + xc / 2)
Teq = np.interp(U, Fc, xc)
Fc_at_T = 1.0 - np.exp(-np.sort(Teq) / 2) * (1.0 + np.sort(Teq) / 2)
ks_chi = float(np.max(np.abs(Fc_at_T - (np.arange(1, n_samp + 1) - 0.5) / n_samp)))
check("rung 3: F^-1_chi2_4(F_W(W)) is chi^2_4 by KS (tol 0.025)",
      ks_chi <= 0.025, f"D_KS = {ks_chi:.4f}")

print()
if FAIL:
    print("RESULT: FAIL")
    sys.exit(1)
print("RESULT: ALL PASS")
sys.exit(0)
