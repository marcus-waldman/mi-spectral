#!/usr/bin/env python
r"""General-p non-monotone Cox-Snell covariance-MLE second-order bias b_Sigma.

Generalizes verify_term_ac_nonmonotone_sympy.py (bivariate, commit 08ee37b) to
ARBITRARY p and an arbitrary non-monotone missing-pattern set, via tensor
Gauss-Hermite quadrature over X ~ N(mu0, Sigma0).  See todo/015.

Cox-Snell (1968, eq. 20):  b_s = 1/2 sum_{r,t,u} i^{rs} i^{tu} (k_rtu + 2 j_{t,ru}),
per-unit cumulants as joint (X, pattern) expectations at theta0:
  i_rs    = -E[ sum_P w_P V^P_rs ],
  j_{t,ru} =  E[ sum_P w_P U^P_t V^P_ru ],
  k_rtu   =  E[ sum_P w_P W^P_rtu ],
with w_P(x) = P(pattern P | x) genuine-MAR weights (every driver lies in the
pattern's OBSERVED block).  Parameter theta = (mu, vech Sigma), vech in R's
column-major lower-tri order (matching Epert / vech_index_table in 00-setup.R).

Per-pattern marginal log-density on the observed block O_P:
  l_P = -1/2 log|Sigma_OO| - 1/2 (x_O - mu_O)^T Sigma_OO^{-1} (x_O - mu_O).
SymPy supplies the exact 1st/2nd/3rd derivatives; theta0 is substituted, leaving
degree-<=2 polynomials in x evaluated on the Gauss-Hermite grid.

Internal gates: zero-score max|E[U]| ~ 0 (validates the MAR mechanism + expectation
setup), Bartlett max|E[UU^T]-i| ~ 0 (info = Var(score)).

p=2 reproduces the committed bivariate b_Sigma (reduction gate, additive
half-sigmoid mechanism).  p=4 targets the phase-8 apply_missingness_ampute(prop=
0.40, mech=MAR, pattern_type=non_monotone) design on default_mu/default_Sigma
(softmax mechanism driven by the always-observed X3, X4).

Run:  py verification/cas-wolfram/verify_term_ac_nonmonotone_genp.py [p]
Env:  N_GH (nodes/dim), TAMAR_A / TAMAR_B (bivariate selection), TAMAR_BETA (p=4 selection)
Writes: verification/cache/coxsnell-nonmonotone-bsigma-genp{p}.json
"""
import hashlib
import itertools
import json
import os
import pickle
import sys
import time

import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss


# ----------------------------------------------------------------------------- vech bookkeeping
def vech_pairs(p):
    """Column-major lower-tri (i>=j), 0-based -- matches R lower.tri(diag=TRUE)."""
    return [(i, j) for j in range(p) for i in range(j, p)]


# ----------------------------------------------------------------------------- DGP fixtures
DEFAULT_SIGMA_4 = [
    [1.0, 0.6, 0.3, 0.0],
    [0.6, 1.0, 0.0, 0.3],
    [0.3, 0.0, 1.0, 0.5],
    [0.0, 0.3, 0.5, 1.0],
]


def get_config(p):
    """Return (mu0, Sig0, patterns, scenarios, n_gh_default).

    patterns: list of dict(name, O=observed 0-based indices).
    scenarios: list of dict(name, mech, params) -- mech in {"additive","softmax"};
      each scenario maps grid X-arrays -> per-incomplete-pattern weight arrays
      (complete weight = 1 - sum), via make_weight_fn below.
    """
    if p == 2:
        mu0 = np.array([0.0, 0.0])
        Sig0 = np.array([[1.0, 0.5], [0.5, 1.0]])
        patterns = [
            dict(name="complete", O=[0, 1]),
            dict(name="miss1", O=[1]),   # X1 missing, observe X2
            dict(name="miss2", O=[0]),   # X2 missing, observe X1
        ]
        A = float(os.environ.get("TAMAR_A", "-0.4"))
        bsweep = [0.0, 0.4, 0.8, 1.2, 1.6]
        scenarios = []
        for b in bsweep:
            scenarios.append(dict(
                name=f"b{b:.1f}", mech="additive",
                params=dict(cap=0.5,
                            spec={"miss1": (A, b, [(1, 1.0)]),    # driver x2 (idx1)
                                  "miss2": (A, b, [(0, 1.0)])}))) # driver x1 (idx0)
        # monotone reduction: drop the X2-missing group (a2 -> -inf)
        scenarios.append(dict(
            name="monotone_reduction", mech="additive",
            params=dict(cap=0.5,
                        spec={"miss1": (A, 1.6, [(1, 1.0)]),
                              "miss2": (-50.0, 0.0, [(0, 1.0)])})))
        n_gh = int(os.environ.get("N_GH", "64"))
        return mu0, Sig0, patterns, scenarios, n_gh

    if p == 4:
        mu0 = np.array([0.0, 0.0, 0.0, 0.0])
        Sig0 = np.array(DEFAULT_SIGMA_4)
        # phase-8 apply_missingness_ampute(non_monotone): X3,X4 always observed.
        patterns = [
            dict(name="complete", O=[0, 1, 2, 3]),
            dict(name="p1", O=[1, 2, 3]),   # X1 missing  (ampute row 0,1,1,1)
            dict(name="p2", O=[0, 2, 3]),   # X2 missing  (ampute row 1,0,1,1)
            dict(name="p3", O=[2, 3]),      # X1,X2 missing (ampute row 0,0,1,1)
        ]
        # softmax over {complete,p1,p2,p3} driven ONLY by X3 (idx2), X4 (idx3):
        # eta_complete=0; eta_p1=a+beta x3; eta_p2=a+beta x4; eta_p3=a+beta(x3+x4).
        # a=log(0.5) gives fractions (0.4,0.2,0.2,0.2) at beta=0 == phase-8 MCAR.
        a0 = float(np.log(0.5))
        bsweep = [0.0, 0.4, 0.8, 1.2]
        beta_head = float(os.environ.get("TAMAR_BETA", "0.8"))
        scenarios = []
        for b in bsweep:
            scenarios.append(dict(
                name=f"beta{b:.1f}", mech="softmax",
                params=dict(eta={"p1": (a0, [(2, b)]),
                                 "p2": (a0, [(3, b)]),
                                 "p3": (a0, [(2, b), (3, b)])})))
        if beta_head not in bsweep:
            scenarios.append(dict(
                name=f"beta{beta_head:.1f}", mech="softmax",
                params=dict(eta={"p1": (a0, [(2, beta_head)]),
                                 "p2": (a0, [(3, beta_head)]),
                                 "p3": (a0, [(2, beta_head), (3, beta_head)])})))
        # additive half-sigmoid sweep, FRACTION-PRESERVING (cap=1/3, intercept a1 so
        # E[w_P] ~ 0.2 at b=0) -- mirrors mice::ampute (candidate pattern by freq 1/3,
        # then amputed by a logistic in the observed drivers X3/X4).  Isolates the pure
        # selection effect on b_Sigma at the phase-8 fractions.
        a1 = float(np.log(0.6 / 0.4))      # sigma(a1)=0.6 -> cap/3 * 0.6 = 0.2
        for b in [0.0, 0.4, 0.8, 1.2]:
            scenarios.append(dict(
                name=f"add{b:.1f}", mech="additive",
                params=dict(cap=1.0 / 3.0,
                            spec={"p1": (a1, b, [(2, 1.0)]),
                                  "p2": (a1, b, [(3, 1.0)]),
                                  "p3": (a1, b, [(2, 1.0), (3, 1.0)])})))
        # monotone reduction sanity: drop p2 and p3 (only X1-missing remains, monotone)
        scenarios.append(dict(
            name="monotone_reduction", mech="softmax",
            params=dict(eta={"p1": (a0, [(2, beta_head)]),
                             "p2": (-50.0, [(3, 0.0)]),
                             "p3": (-50.0, [(2, 0.0), (3, 0.0)])})))
        # drivers X3,X4 load mainly on z3,z4 (chol(default_Sigma) lower-tri); put
        # few nodes on z1,z2 (deg<=4 polynomial only) and many on z3,z4 (sigmoid).
        env_n = os.environ.get("N_GH")
        n_gh = int(env_n) if env_n else [10, 10, 26, 26]
        return mu0, Sig0, patterns, scenarios, n_gh

    if p == 3:
        # Three-variate non-monotone for the two-CAS gate. X3 always observed,
        # drives the missingness (genuine MAR).  rho structure echoes default_Sigma.
        mu0 = np.array([0.0, 0.0, 0.0])
        Sig0 = np.array([[1.0, 0.5, 0.3],
                         [0.5, 1.0, 0.2],
                         [0.3, 0.2, 1.0]])
        patterns = [
            dict(name="complete", O=[0, 1, 2]),
            dict(name="p1", O=[1, 2]),   # X1 missing
            dict(name="p2", O=[0, 2]),   # X2 missing
        ]
        a0 = float(np.log(0.5))
        bsweep = [0.0, 0.8]
        beta_head = float(os.environ.get("TAMAR_BETA", "0.8"))
        scenarios = []
        for b in bsweep:
            scenarios.append(dict(
                name=f"beta{b:.1f}", mech="softmax",
                params=dict(eta={"p1": (a0, [(2, b)]),
                                 "p2": (a0, [(2, b)])})))
        scenarios.append(dict(
            name="monotone_reduction", mech="softmax",
            params=dict(eta={"p1": (a0, [(2, beta_head)]),
                             "p2": (-50.0, [(2, 0.0)])})))
        n_gh = int(os.environ.get("N_GH", "32"))
        return mu0, Sig0, patterns, scenarios, n_gh

    raise ValueError(f"no config for p={p}")


# ----------------------------------------------------------------------------- symbolic derivs
def build_pattern_derivs(p, patterns, mu0, Sig0):
    """Exact U/V/W derivative expressions per pattern, theta0-substituted.

    Returns (xsyms, {name: (U, V, W)}) where U[r], V[r][s], W[r][s][t] are SymPy
    expressions in x1..xp (degree <= 2).  The (expensive) symbolic differentiation
    is cached to a pickle keyed by (p, patterns, theta0)."""
    here = os.path.dirname(os.path.abspath(__file__))
    cache_dir = os.path.abspath(os.path.join(here, "..", "cache"))
    os.makedirs(cache_dir, exist_ok=True)
    key = repr((p, [tuple(pp["O"]) for pp in patterns],
                [round(float(v), 12) for v in np.ravel(mu0)],
                [round(float(v), 12) for v in np.ravel(Sig0)]))
    cpath = os.path.join(cache_dir, f"genp-derivs-p{p}-{hashlib.md5(key.encode()).hexdigest()[:10]}.pkl")
    if os.path.exists(cpath):
        with open(cpath, "rb") as fh:
            xstr, out = pickle.load(fh)
        xsyms = sp.symbols(xstr, real=True)
        xsyms = list(xsyms) if isinstance(xsyms, (tuple, list)) else [xsyms]
        print(f"   [derivs] loaded symbolic cache {os.path.basename(cpath)}")
        return xsyms, out
    pairs = vech_pairs(p)
    msyms = list(sp.symbols(f"m1:{p + 1}", real=True))
    xsyms = list(sp.symbols(f"x1:{p + 1}", real=True))
    sig = {}
    sig_list = []
    for (i, j) in pairs:
        s = sp.Symbol(f"s{i + 1}{j + 1}", real=True)
        sig[(i, j)] = s
        sig[(j, i)] = s
        sig_list.append(s)
    pars = msyms + sig_list                       # theta = (mu, vech Sigma); len k
    k = len(pars)
    Sig = sp.Matrix(p, p, lambda i, j: sig[(i, j)])
    muv = sp.Matrix(msyms)
    xv = sp.Matrix(xsyms)

    sub0 = {}
    for i in range(p):
        sub0[msyms[i]] = sp.Float(mu0[i])
    for a, (i, j) in enumerate(pairs):
        sub0[sig_list[a]] = sp.nsimplify(sp.Float(Sig0[i, j]))

    out = {}
    for pat in patterns:
        O = list(pat["O"])
        SigOO = Sig[O, O]
        muO = muv[O, :]
        xO = xv[O, :]
        q = xO - muO
        lP = -sp.Rational(1, 2) * sp.log(SigOO.det()) \
             - sp.Rational(1, 2) * (q.T * SigOO.inv() * q)[0]
        t0 = time.time()
        # gradient
        g = [sp.diff(lP, pars[r]) for r in range(k)]
        U = [sp.expand(g[r].subs(sub0)) for r in range(k)]
        # Hessian (upper-tri symbolic, reused for 3rd); store pre-subs for reuse
        Hsym = [[None] * k for _ in range(k)]
        V = [[None] * k for _ in range(k)]
        for r in range(k):
            for s in range(r, k):
                hrs = sp.diff(g[r], pars[s])
                Hsym[r][s] = hrs
                v = sp.expand(hrs.subs(sub0))
                V[r][s] = v
                V[s][r] = v
        # third (upper-tri symbolic), fill all permutations
        W = [[[None] * k for _ in range(k)] for _ in range(k)]
        for r in range(k):
            for s in range(r, k):
                for t in range(s, k):
                    wrst = sp.expand(sp.diff(Hsym[r][s], pars[t]).subs(sub0))
                    for (a, b, c) in set(itertools.permutations((r, s, t))):
                        W[a][b][c] = wrst
        out[pat["name"]] = (U, V, W)
        print(f"   [derivs] pattern {pat['name']:10s} |O|={len(O)}  "
              f"({time.time() - t0:.1f}s)")
    with open(cpath, "wb") as fh:
        pickle.dump((",".join(str(s) for s in xsyms), out), fh)
    print(f"   [derivs] wrote symbolic cache {os.path.basename(cpath)}")
    return xsyms, out


# ----------------------------------------------------------------------------- GH grid
def gh_grid(p, mu0, Sig0, n_gh):
    """Tensor Gauss-Hermite grid for X ~ N(mu0, Sig0).  Returns (Xg list, Wgrid).

    n_gh may be a scalar (uniform nodes/dim) or a per-z-dimension list.  Using
    fewer nodes on the weakly-loaded z-dims and more on the strong driver dims
    keeps the smooth-MAR-weight quadrature accurate at modest total grid size."""
    if np.isscalar(n_gh):
        ngh = [int(n_gh)] * p
    else:
        ngh = [int(v) for v in n_gh]
    tw = [hermgauss(ngh[d]) for d in range(p)]
    mesh = np.meshgrid(*[tw[d][0] for d in range(p)], indexing="ij")
    shape = mesh[0].shape
    Wgrid = np.ones(shape)
    for d in range(p):
        sh = [1] * p
        sh[d] = ngh[d]
        Wgrid = Wgrid * tw[d][1].reshape(sh)
    Wgrid = Wgrid / (np.pi ** (p / 2.0))
    Z = [np.sqrt(2.0) * mesh[d] for d in range(p)]
    L = np.linalg.cholesky(Sig0)             # lower-tri
    Xg = []
    for d in range(p):
        xd = np.full(shape, mu0[d])
        for e in range(d + 1):
            xd = xd + L[d, e] * Z[e]
        Xg.append(xd)
    return Xg, Wgrid


def lambdify_grid(expr, xsyms, Xg, shape):
    f = sp.lambdify(xsyms, expr, "numpy")
    v = f(*Xg)
    return np.broadcast_to(np.asarray(v, dtype=float), shape).astype(float)


# ----------------------------------------------------------------------------- MAR weights
def make_incomplete_weights(scn, Xg):
    """Return {pattern_name: weight_array} for INCOMPLETE patterns (complete = 1 - sum)."""
    mech = scn["mech"]
    out = {}
    if mech == "additive":
        cap = scn["params"]["cap"]
        for name, (a, b, drv) in scn["params"]["spec"].items():
            # eta = a + b * (sum coef*x_idx)
            lin = np.zeros_like(Xg[0])
            for idx, coef in drv:
                lin = lin + coef * Xg[idx]
            eta = a + b * lin
            out[name] = cap / (1.0 + np.exp(-eta))
        return out
    if mech == "softmax":
        etas = {}
        for name, (a, drv) in scn["params"]["eta"].items():
            lin = np.zeros_like(Xg[0])
            for idx, coef in drv:
                lin = lin + coef * Xg[idx]
            etas[name] = a + lin
        # denominator includes complete (eta=0 -> exp=1)
        denom = np.ones_like(Xg[0])
        exps = {}
        for name, e in etas.items():
            exps[name] = np.exp(e)
            denom = denom + exps[name]
        for name in etas:
            out[name] = exps[name] / denom
        return out
    raise ValueError(mech)


# ----------------------------------------------------------------------------- Cox-Snell
def coxsnell_bsigma(p, patterns, derivs, xsyms, Xg, Wgrid, scn):
    k = p + p * (p + 1) // 2
    shape = Wgrid.shape

    # incomplete weights, then complete = 1 - sum
    inc_w = make_incomplete_weights(scn, Xg)
    wsum = np.zeros(shape)
    for name in inc_w:
        wsum = wsum + inc_w[name]
    weights = {"complete": 1.0 - wsum}
    weights.update(inc_w)
    # per-pattern integration weight = GH weight * P(pattern | x)
    Wp = {name: Wgrid * weights[name] for name in weights}

    imat = np.zeros((k, k))
    jt = np.zeros((k, k, k))
    kt = np.zeros((k, k, k))
    zsr = np.zeros(k)
    EUU = np.zeros((k, k))
    fracs = {}

    for pat in patterns:
        name = pat["name"]
        U, V, W = derivs[name]
        wp = Wp[name]
        # grid-evaluate U, V (upper-tri), accumulate; stream W
        Ug = [lambdify_grid(U[r], xsyms, Xg, shape) for r in range(k)]
        Vg = [[None] * k for _ in range(k)]
        for r in range(k):
            for s in range(r, k):
                g = lambdify_grid(V[r][s], xsyms, Xg, shape)
                Vg[r][s] = g
                Vg[s][r] = g
        fracs[name] = float(np.sum(wp))
        for r in range(k):
            zsr[r] += float(np.sum(wp * Ug[r]))
        for r in range(k):
            for s in range(r, k):
                val = float(np.sum(wp * Ug[r] * Ug[s]))
                EUU[r, s] += val
                if s != r:
                    EUU[s, r] += val
        for r in range(k):
            for s in range(r, k):
                val = -float(np.sum(wp * Vg[r][s]))
                imat[r, s] += val
                if s != r:
                    imat[s, r] += val
        # jt[t,r,u] = sum_P E[w_P U_t V_ru]  (symmetric in r,u)
        for tt in range(k):
            for r in range(k):
                for u in range(r, k):
                    val = float(np.sum(wp * Ug[tt] * Vg[r][u]))
                    jt[tt, r, u] += val
                    if u != r:
                        jt[tt, u, r] += val
        # kt[r,t,u] = sum_P E[w_P W_rtu]  (fully symmetric); stream W upper-tri
        for r in range(k):
            for s in range(r, k):
                for t in range(s, k):
                    wexpr = W[r][s][t]
                    val = float(np.sum(wp * lambdify_grid(wexpr, xsyms, Xg, shape)))
                    for (a, b, c) in set(itertools.permutations((r, s, t))):
                        kt[a, b, c] += val
        del Ug, Vg

    iinv = np.linalg.inv(imat)
    # b_s = 1/2 sum_{r,t,u} iinv[r,s] iinv[t,u] (kt[r,t,u] + 2 jt[t,r,u])
    Kterm = kt + 2.0 * np.transpose(jt, (1, 0, 2))   # [r,t,u] = kt[r,t,u] + 2 jt[t,r,u]
    # contract: b[s] = 1/2 sum_{r,t,u} iinv[r,s] iinv[t,u] Kterm[r,t,u]
    bvec = 0.5 * np.einsum("rs,tu,rtu->s", iinv, iinv, Kterm)

    bart = float(np.max(np.abs(EUU - imat)))
    zs = float(np.max(np.abs(zsr)))
    return bvec, zs, bart, fracs


# ----------------------------------------------------------------------------- main
def main():
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    mu0, Sig0, patterns, scenarios, n_gh = get_config(p)
    k = p + p * (p + 1) // 2
    pairs = vech_pairs(p)
    sigma_param_idx = list(range(p, k))          # which theta indices are sigma
    sigma_labels = [f"s{i + 1}{j + 1}" for (i, j) in pairs]

    print(f"== General-p Cox-Snell b_Sigma  (p={p}, k={k}, N_GH={n_gh}) ==")
    print(f"   patterns: {[(pp['name'], pp['O']) for pp in patterns]}")
    t0 = time.time()
    xsyms, derivs = build_pattern_derivs(p, patterns, mu0, Sig0)
    print(f"   symbolic derivatives done ({time.time() - t0:.1f}s); building GH grid...")
    Xg, Wgrid = gh_grid(p, mu0, Sig0, n_gh)
    print(f"   grid: nodes/dim={n_gh}  total points={Wgrid.size}")

    results = {}
    for scn in scenarios:
        ts = time.time()
        bvec, zs, bart, fracs = coxsnell_bsigma(p, patterns, derivs, xsyms, Xg, Wgrid, scn)
        b_sigma_vech = [bvec[s] for s in sigma_param_idx]
        b_mu = [bvec[s] for s in range(p)]
        results[scn["name"]] = dict(
            b_sigma_vech=b_sigma_vech,
            b_sigma={lab: b_sigma_vech[a] for a, lab in enumerate(sigma_labels)},
            b_mu=b_mu,
            fracs=fracs,
            zeroscore_max=zs,
            bartlett_max=bart,
        )
        fr = "  ".join(f"{n}={fracs[n]:.3f}" for n in fracs)
        bs = "  ".join(f"{lab}={b_sigma_vech[a]:+.5f}" for a, lab in enumerate(sigma_labels))
        print(f"-- {scn['name']:20s} ({time.time() - ts:.1f}s)")
        print(f"     fracs: {fr}")
        print(f"     b_Sigma: {bs}")
        print(f"     b_mu max={max(abs(x) for x in b_mu):.2e}  "
              f"zero-score={zs:.2e}  Bartlett={bart:.2e}")

    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.abspath(os.path.join(here, "..", "cache", f"coxsnell-nonmonotone-bsigma-genp{p}.json"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\nwrote {out}")

    # gates
    ok = True
    for name, r in results.items():
        if r["zeroscore_max"] > 1e-6 or r["bartlett_max"] > 1e-6:
            ok = False
            print(f"[FAIL] {name}: zs={r['zeroscore_max']:.1e} bart={r['bartlett_max']:.1e}")

    # p=2 reduction gate vs committed bivariate b_Sigma
    if p == 2:
        committed = {"s11": -1.1912171453634937, "s21": -0.4820346365730676,
                     "s22": -1.191217145363207}
        r = results.get("b1.6")
        if r is not None:
            print("\n-- p=2 reduction gate vs committed (08ee37b) --")
            dmax = 0.0
            for lab, want in committed.items():
                got = r["b_sigma"][lab]
                d = abs(got - want)
                dmax = max(dmax, d)
                print(f"   {lab}: genp={got:+.6f} committed={want:+.6f} |d|={d:.2e}")
            print(f"   max|d|={dmax:.2e}  [{'PASS' if dmax < 1e-4 else 'FAIL'}]")
            ok = ok and dmax < 1e-4

    print("\nGeneral-p Cox-Snell:", "b_Sigma CONFIRMED" if ok else "GATE FAILED -- investigate")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
