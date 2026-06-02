#!/usr/bin/env python
r"""Independent SymPy re-derivation of the non-monotone covariance-MLE second-order bias
b_Sigma (cross-check of the Wolfram derivation in verify_term_ac_nonmonotone.py).

Same recipe (todo/014), independent engine:
  * SymPy computes the exact per-pattern 1st/2nd/3rd log-density derivatives.
  * Expectations E[w_P(X) g(X)] use tensor Gauss-Hermite quadrature over X~N(mu0,Sigma0)
    -- exact for the degree-<=4 polynomial derivative products, high-accuracy for the
    smooth multinomial-logit weights w_P.
  * Cox-Snell (1968 eq.20): b_s = 1/2 sum_{r,t,u} i^{rs} i^{tu} (k_rtu + 2 j_{t,ru}).

If verification/cache/coxsnell-nonmonotone-bsigma.json (the Wolfram output) is present,
the two b_Sigma are compared and the script exits 1 on any disagreement > 1e-4.

Run:  py verification/cas-wolfram/verify_term_ac_nonmonotone_sympy.py
"""
import json
import os
import sys

import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss

# theta0 (rho = 0.5 matches TAMAR_BIV_SIG).  Selection a = -0.4; slope b swept over BSWEEP
# (b=0 is MCAR) so (A)+(C) can be traced from the MCAR limit (-> 0) to strong selection,
# paralleling the validated phase-8 S1 sweep.  B_HEAD = the headline strength (monotone
# reduction + the direct-MC gate use it).
TH0 = dict(m1=0.0, m2=0.0, s11=1.0, s12=0.5, s22=1.0)
A = float(os.environ.get("TAMAR_A", "-0.4"))
BSWEEP = [0.0, 0.4, 0.8, 1.2, 1.6]
B_HEAD = float(os.environ.get("TAMAR_B", "1.6"))
SCEN = {f"b{b:.1f}": dict(a1=A, b1=b, a2=A, b2=b) for b in BSWEEP}
SCEN["monotone_reduction"] = dict(a1=A, b1=B_HEAD, a2=-50.0, b2=0.0)
N_GH = int(os.environ.get("N_GH", "64"))


def build_symbolic():
    """Return lists/arrays of exact derivative expressions (functions of x1,x2 at theta0)."""
    m1, m2, s11, s12, s22, x1, x2 = sp.symbols("m1 m2 s11 s12 s22 x1 x2", real=True)
    pars = [m1, m2, s11, s12, s22]
    mu = sp.Matrix([m1, m2])
    Sig = sp.Matrix([[s11, s12], [s12, s22]])
    xv = sp.Matrix([x1, x2])
    q = xv - mu
    lc = -sp.Rational(1, 2) * sp.log(Sig.det()) - sp.Rational(1, 2) * (q.T * Sig.inv() * q)[0]
    la = -sp.Rational(1, 2) * sp.log(s22) - (x2 - m2) ** 2 / (2 * s22)   # miss1: observe x2
    lb = -sp.Rational(1, 2) * sp.log(s11) - (x1 - m1) ** 2 / (2 * s11)   # miss2: observe x1
    sub0 = {m1: TH0["m1"], m2: TH0["m2"], s11: TH0["s11"], s12: TH0["s12"], s22: TH0["s22"]}

    def derivs(l):
        U = [sp.diff(l, pars[r]).subs(sub0) for r in range(5)]
        V = [[sp.diff(l, pars[r], pars[s]).subs(sub0) for s in range(5)] for r in range(5)]
        W = [[[sp.diff(l, pars[r], pars[s], pars[t]).subs(sub0)
               for t in range(5)] for s in range(5)] for r in range(5)]
        return U, V, W

    return (x1, x2), derivs(lc), derivs(la), derivs(lb)


def main():
    (X1, X2), (Uc, Vc, Wc), (Ua, Va, Wa), (Ub, Vb, Wb) = build_symbolic()

    # Gauss-Hermite grid for X ~ N(mu0, Sigma0): X = mu + L z, z ~ N(0,I).
    t, w = hermgauss(N_GH)
    T1, T2 = np.meshgrid(t, t, indexing="ij")
    Wgrid = np.outer(w, w) / np.pi               # d=2  ->  pi^{1}
    Z1, Z2 = np.sqrt(2) * T1, np.sqrt(2) * T2
    L11 = np.sqrt(TH0["s11"])
    L21 = TH0["s12"] / L11
    L22 = np.sqrt(TH0["s22"] - L21 ** 2)
    x1g = TH0["m1"] + L11 * Z1
    x2g = TH0["m2"] + L21 * Z1 + L22 * Z2

    def grid(expr):
        f = sp.lambdify((X1, X2), expr, "numpy")
        v = f(x1g, x2g)
        return np.broadcast_to(np.asarray(v, dtype=float), x1g.shape).astype(float)

    # pre-evaluate every derivative entry on the grid
    def gridify(U, V, W):
        Ug = [grid(U[r]) for r in range(5)]
        Vg = [[grid(V[r][s]) for s in range(5)] for r in range(5)]
        Wg = [[[grid(W[r][s][t]) for t in range(5)] for s in range(5)] for r in range(5)]
        return Ug, Vg, Wg

    Ucg, Vcg, Wcg = gridify(Uc, Vc, Wc)
    Uag, Vag, Wag = gridify(Ua, Va, Wa)
    Ubg, Vbg, Wbg = gridify(Ub, Vb, Wb)

    def E(arr):
        return float(np.sum(Wgrid * arr))

    results = {}
    for name, mech in SCEN.items():
        eta1 = mech["a1"] + mech["b1"] * x2g
        eta2 = mech["a2"] + mech["b2"] * x1g
        wa = 0.5 / (1.0 + np.exp(-eta1))   # P(miss1) depends only on x2
        wb = 0.5 / (1.0 + np.exp(-eta2))   # P(miss2) depends only on x1
        wc = 1.0 - wa - wb

        def Etot(gc, ga, gb):
            return E(wc * gc) + E(wa * ga) + E(wb * gb)

        imat = np.array([[-Etot(Vcg[r][s], Vag[r][s], Vbg[r][s]) for s in range(5)]
                         for r in range(5)])
        jt = np.array([[[Etot(Ucg[tt] * Vcg[r][u], Uag[tt] * Vag[r][u], Ubg[tt] * Vbg[r][u])
                         for u in range(5)] for r in range(5)] for tt in range(5)])
        kt = np.array([[[Etot(Wcg[r][tt][u], Wag[r][tt][u], Wbg[r][tt][u])
                         for u in range(5)] for tt in range(5)] for r in range(5)])
        iinv = np.linalg.inv(imat)

        def bias_of(s):
            tot = 0.0
            for r in range(5):
                for tt in range(5):
                    for u in range(5):
                        tot += iinv[r, s] * iinv[tt, u] * (kt[r, tt, u] + 2 * jt[tt, r, u])
            return 0.5 * tot

        bS = [bias_of(s) for s in range(5)]
        zsr = max(abs(Etot(Ucg[r], Uag[r], Ubg[r])) for r in range(5))
        EUU = np.array([[Etot(Ucg[r] * Ucg[s], Uag[r] * Uag[s], Ubg[r] * Ubg[s])
                         for s in range(5)] for r in range(5)])
        bart = float(np.max(np.abs(EUU - imat)))
        fr = (E(wc * np.ones_like(x1g)), E(wa * np.ones_like(x1g)), E(wb * np.ones_like(x1g)))
        results[name] = dict(
            b_sigma=dict(s11=bS[2], s12=bS[3], s22=bS[4]),
            b_mu=dict(m1=bS[0], m2=bS[1]),
            fracs=dict(complete=fr[0], miss1=fr[1], miss2=fr[2]),
            zeroscore_max=zsr, bartlett_max=bart, mech=mech)
        print(f"-- {name}: fracs=({fr[0]:.4f},{fr[1]:.4f},{fr[2]:.4f})  "
              f"b_Sigma=(s11={bS[2]:+.5f}, s12={bS[3]:+.5f}, s22={bS[4]:+.5f})")
        print(f"   b_mu=({bS[0]:+.1e},{bS[1]:+.1e})  zero-score={zsr:.1e}  Bartlett={bart:.1e}")

    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.abspath(os.path.join(here, "..", "cache", "coxsnell-nonmonotone-bsigma-sympy.json"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\nwrote {out}")

    # internal gates
    ok = True
    for name, r in results.items():
        if r["zeroscore_max"] > 1e-6 or r["bartlett_max"] > 1e-6:
            ok = False
            print(f"[FAIL] {name}: internal gate (zs={r['zeroscore_max']:.1e}, bart={r['bartlett_max']:.1e})")

    # cross-check vs Wolfram if present
    wpath = os.path.abspath(os.path.join(here, "..", "cache", "coxsnell-nonmonotone-bsigma.json"))
    if os.path.exists(wpath):
        with open(wpath) as fh:
            wolf = json.load(fh)
        print("\n-- SymPy vs Wolfram b_Sigma (Wolfram run at the headline b) --")
        wmap = {"nonmonotone": f"b{B_HEAD:.1f}", "mcar": "b0.0",
                "monotone_reduction": "monotone_reduction"}
        for wname, sname in wmap.items():
            if wname not in wolf or sname not in results:
                continue
            for key in ("s11", "s12", "s22"):
                a = results[sname]["b_sigma"][key]
                b = wolf[wname]["b_sigma"][key]
                d = abs(a - b)
                flag = "ok" if d < 1e-4 else "MISMATCH"
                if d >= 1e-4:
                    ok = False
                print(f"   {wname:20s} {key}: sympy={a:+.5f} wolfram={b:+.5f}  |d|={d:.1e} {flag}")
    else:
        print("\n(Wolfram JSON not found; run verify_term_ac_nonmonotone.py to enable cross-check.)")

    print("\nSymPy CAS:", "b_Sigma CONFIRMED" if ok else "MISMATCH -- investigate")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
