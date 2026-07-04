#!/usr/bin/env python
r"""Close the two ESCALATE items from the todo/045b Mode B response (2026-07-04).

Mode B (GPT-5.5 Pro, xhigh, red-team) sustained every algebraic claim C1-C8 and
escalated ONLY the numerical quadrature constants, asking for independent
reproduction:
  (E1) C7's K = E[eta A''' X'Omega^-1 X] = -1.042 (Bernoulli design)
  (E2) C6's Poisson parts: bias +0.688, curvature -1.084, Delta_h/tr = -0.396

Independent-route policy: the registered constants came from Gauss-Hermite with
160 nodes (verify_bernoulli_fitted_gap.py, route 1); Mode A independently
reproduced K via its own quadrature (-1.0416, route 2). This script is route 3:
composite Simpson on a wide uniform grid (completely different node placement),
with a grid-halving convergence check, plus an evaluation of Mode B's OWN
reduced one-dimensional forms for the Poisson parts. The Poisson blind arm's
empirical landing (+0.1132 +/- 0.0274 vs the predicted +0.1039 at N=200,
R=100k) is the sim-side reproduction and is quoted for the record.

Run:  py verification/cas-wolfram/verify_045b_escalations.py
Exit: 0 if all reproductions agree to the stated tolerances, 1 otherwise.
"""
import math
import sys

import numpy as np

FAIL = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


def simpson(vals, h):
    n = len(vals) - 1
    assert n % 2 == 0
    return (h / 3) * (vals[0] + vals[-1] + 4 * vals[1:-1:2].sum() + 2 * vals[2:-2:2].sum())


BETA0 = np.array([0.3, 0.9])
PHI = lambda x: np.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def grid_vals(npts, lo=-9.0, hi=9.0):
    x = np.linspace(lo, hi, npts)
    h = x[1] - x[0]
    return x, h


# -----------------------------------------------------------------------------
# (E1) Bernoulli K on a Simpson grid
# -----------------------------------------------------------------------------
def bern_K(npts):
    x, h = grid_vals(npts)
    eta = BETA0[0] + BETA0[1] * x
    p = 1 / (1 + np.exp(-eta))
    w = p * (1 - p)
    t = w * (1 - 2 * p)
    X = np.stack([np.ones_like(x), x], axis=1)
    dens = PHI(x)
    Om = np.zeros((2, 2))
    for a in range(2):
        for b in range(2):
            Om[a, b] = simpson(dens * w * X[:, a] * X[:, b], h)
    Om_inv = np.linalg.inv(Om)
    z = np.einsum("ij,jk,ik->i", X, Om_inv, X)
    K = simpson(dens * eta * t * z, h)
    return K


K1, K2 = bern_K(4001), bern_K(8001)
print(f"(E1) K by Simpson: {K1:.6f} (n=4001) vs {K2:.6f} (n=8001)")
print(f"     registered GH-160 value: -1.042393; Mode A's own value: -1.0416")
check("E1: Simpson reproduces K to 1e-4 and grids agree",
      abs(K2 - (-1.042393)) < 1e-4 and abs(K1 - K2) < 1e-6,
      f"K = {K2:.6f}")

# -----------------------------------------------------------------------------
# (E2) Poisson parts on a Simpson grid (my original expressions)
# -----------------------------------------------------------------------------
def pois_L1_L2(mu):
    kmax = int(mu + 20 * math.sqrt(mu) + 40)   # different truncation rule than route 1
    k = np.arange(kmax + 1)
    logpmf = k * math.log(mu) - mu - np.array([math.lgamma(kk + 1) for kk in k])
    pmf = np.exp(logpmf)
    return float(pmf @ np.log(k + 1.0)), float(pmf @ np.log((k + 2.0) / (k + 1.0)))


def pois_parts(npts, lo=-8.0, hi=8.0):
    x, h = grid_vals(npts, lo, hi)
    eta = BETA0[0] + BETA0[1] * x
    mu = np.exp(eta)
    X = np.stack([np.ones_like(x), x], axis=1)
    dens = PHI(x)
    Om = np.zeros((2, 2))
    for a in range(2):
        for b in range(2):
            Om[a, b] = simpson(dens * mu * X[:, a] * X[:, b], h)
    Om_inv = np.linalg.inv(Om)
    z = np.einsum("ij,jk,ik->i", X, Om_inv, X)
    L1 = np.empty_like(mu)
    L2 = np.empty_like(mu)
    for i, m in enumerate(mu):
        L1[i], L2[i] = pois_L1_L2(m)
    gp = -mu * L1
    gpp = -mu * L1 - mu * mu * L2
    lhs_g = np.array([simpson(dens * gp * X[:, a], h) for a in range(2)])
    rhs = np.array([simpson(dens * mu * z * X[:, a], h) for a in range(2)])
    bias_part = -0.5 * float(lhs_g @ Om_inv @ rhs) / 2      # /q, q=2
    curv_part = 0.5 * simpson(dens * gpp * z, h) / 2
    return bias_part, curv_part


b1, c1 = pois_parts(2001)
b2, c2 = pois_parts(4001)
print(f"\n(E2) Poisson parts by Simpson (n=2001 vs 4001):")
print(f"     bias  {b1:+.6f} vs {b2:+.6f}   (registered +0.687997)")
print(f"     curv  {c1:+.6f} vs {c2:+.6f}   (registered -1.084067)")
print(f"     Delta_h/tr = {b2 + c2:+.6f}     (registered -0.396070)")
check("E2: Simpson reproduces the Poisson parts to 2e-4 and grids agree",
      abs(b2 - 0.687997) < 2e-4 and abs(c2 - (-1.084067)) < 2e-4
      and abs(b1 - b2) < 1e-5 and abs(c1 - c2) < 1e-5)

# -----------------------------------------------------------------------------
# (E2b) Mode B's own reduced one-dimensional forms
#   bias/tr = E[mu L1(mu)] / (2 m),  m = E[mu] = exp(0.3 + 0.9^2/2)
#   curv/tr = -(1/4) E[(mu L1 + mu^2 L2) z]
# -----------------------------------------------------------------------------
x, h = grid_vals(4001, -8.0, 8.0)
eta = BETA0[0] + BETA0[1] * x
mu = np.exp(eta)
dens = PHI(x)
L1v = np.empty_like(mu)
L2v = np.empty_like(mu)
for i, m_ in enumerate(mu):
    L1v[i], L2v[i] = pois_L1_L2(m_)
m_mean = math.exp(0.3 + 0.81 / 2)
X = np.stack([np.ones_like(x), x], axis=1)
Om = np.zeros((2, 2))
for a in range(2):
    for b in range(2):
        Om[a, b] = simpson(dens * mu * X[:, a] * X[:, b], h)
z = np.einsum("ij,jk,ik->i", X, np.linalg.inv(Om), X)
bias_modeB = simpson(dens * mu * L1v, h) / (2 * m_mean)
curv_modeB = -0.25 * simpson(dens * (mu * L1v + mu * mu * L2v) * z, h)
print(f"\n(E2b) Mode B's reduced forms: bias {bias_modeB:+.6f}, curv {curv_modeB:+.6f}")
check("E2b: Mode B's reduced bias form matches (2e-3)",
      abs(bias_modeB - 0.687997) < 2e-3, f"{bias_modeB:+.6f}")
check("E2b: Mode B's reduced curvature form matches (2e-3)",
      abs(curv_modeB - (-1.084067)) < 2e-3, f"{curv_modeB:+.6f}")

print(f"\nEmpirical reproduction (blind arm, for the record): Poisson FITTED ratio "
      f"+0.1132 (se 0.0274) at N=200, R=100k vs predicted 0.5 + ({b2 + c2:+.4f}) "
      f"= {0.5 + b2 + c2:+.4f}")

print("\n== summary ==")
if FAIL:
    print("FAILED:", ", ".join(FAIL))
    sys.exit(1)
print("Both Mode B escalations closed: three independent numerical routes agree "
      "(GH-160, Mode A's own quadrature, Simpson), and Mode B's reduced forms "
      "evaluate to the same constants.")
sys.exit(0)
