#!/usr/bin/env python
r"""Independent SymPy re-derivation of the C2 reconciliation identity (todo/017):
the conditional-entropy plug-in bias Delta_n equals 1/2 tr(RIV) + (A)+(C), so
E[T] = Delta_n -- the manuscript's (A)/(B-main)/(C) split and the entropy story
are the SAME total, regrouped. Second CAS for the Wolfram check in
verify_term_ac.py (WL_DELTAN); exact symbolic, no quadrature.

One bivariate seed surface (X1 | X2 = x), draw at phi, evaluate at psi, in the
FULL natural (mu1,mu2,s11,s12,s22) parametrization (the conditional mean carries
the covariance via beta = s12/s22):

  F(phi,psi) = E_{X1 ~ N(m_phi,v_phi)}[ log N(X1; m_psi, v_psi) ]
             = -1/2 log(2 pi v_psi) - 1/(2 v_psi) [ (m_phi-m_psi)^2 + v_phi ].

Three slices: f0(phi)=F(phi,th0) [cross-entropy], g0(psi)=F(th0,psi) [expected
loglik], C_n(th)=F(th,th) [neg. conditional entropy]. DERIVED, symbolic in x:

  (I1) grad C_n(th0) = alpha            (entropy grad = cross-entropy grad; alpha_mu=0)
  (I2) hess C_n(th0) = H_phi + I_F       (entropy-Hessian split -- the key identity),
       with H_phi = d2_phiphi F, I_F = -d2_psipsi F, Bartlett d2_phipsi F = +I_F
  (Iss) H_phi + I_F mu-block = 0          (the known-scale Isserlis identity, as a corollary)

Assembling Delta_n = alpha.E[delta] + 1/2 tr((H_phi+I_F) Iobs^-1):
  Delta_n = (A) + (C) + 1/2 tr(RIV)      [asserted with generic Iobs^-1, E[delta]].

Run:  py verification/cas-wolfram/verify_term_ac_sympy.py
Exit: 0 all pass; 1 a mismatch.
"""
import sys

import sympy as sp


def cond(mu1, mu2, S11, S12, S22, xx):
    """Conditional mean / variance of X1 given X2 = xx under N(mu, Sigma)."""
    beta = S12 / S22
    m = mu1 + beta * (xx - mu2)
    v = S11 - S12 ** 2 / S22
    return m, v


def build():
    # theta0 = (m1,m2,s11,s12,s22); phi = sampling slot; psi = eval slot; x conditioning value.
    m1, m2, s11, s12, s22 = sp.symbols("m1 m2 s11 s12 s22", real=True)
    a1, a2, p11, p12, p22 = sp.symbols("a1 a2 p11 p12 p22", real=True)
    d1, d2, q11, q12, q22 = sp.symbols("d1 d2 q11 q12 q22", real=True)
    x = sp.symbols("x", real=True)

    mp, vp = cond(a1, a2, p11, p12, p22, x)   # draw slot phi
    mq, vq = cond(d1, d2, q11, q12, q22, x)   # eval slot psi
    F = -sp.Rational(1, 2) * sp.log(2 * sp.pi * vq) - (1 / (2 * vq)) * ((mp - mq) ** 2 + vp)

    phi = [a1, a2, p11, p12, p22]
    psi = [d1, d2, q11, q12, q22]
    th = [m1, m2, s11, s12, s22]
    sub0 = {a1: m1, a2: m2, p11: s11, p12: s12, p22: s22,
            d1: m1, d2: m2, q11: s11, q12: s12, q22: s22}

    alpha = [sp.diff(F, phi[r]).subs(sub0) for r in range(5)]                       # cross-entropy gradient
    Hphi = [[sp.diff(F, phi[r], phi[s]).subs(sub0) for s in range(5)] for r in range(5)]  # cross-entropy curvature
    IF = [[-sp.diff(F, psi[r], psi[s]).subs(sub0) for s in range(5)] for r in range(5)]   # conditional Fisher info
    MIX = [[sp.diff(F, phi[r], psi[s]).subs(sub0) for s in range(5)] for r in range(5)]   # mixed (Bartlett)

    # C_n(theta) = F(theta,theta): collapse both slots onto the shared theta = (m1..s22)
    Cn = F.subs(sub0)
    gradCn = [sp.diff(Cn, th[r]) for r in range(5)]
    hessCn = [[sp.diff(Cn, th[r], th[s]) for s in range(5)] for r in range(5)]

    A = sp.Matrix
    return dict(alpha=A(alpha), Hphi=A(Hphi), IF=A(IF), MIX=A(MIX),
                gradCn=A(gradCn), hessCn=A(hessCn))


def main():
    o = build()
    alpha, Hphi, IF, MIX = o["alpha"], o["Hphi"], o["IF"], o["MIX"]
    gradCn, hessCn = o["gradCn"], o["hessCn"]

    def z_vec(v):
        return sp.simplify(v) == sp.zeros(*v.shape)

    def z_mat(M):
        return sp.simplify(M) == sp.zeros(*M.shape)

    # generic Iobs^-1 (V symmetric 5x5) and MLE bias E[delta] = g for the scalar assembly
    V = sp.Matrix(5, 5, lambda i, j: sp.Symbol(f"v{min(i, j)}{max(i, j)}"))
    g = sp.Matrix([sp.Symbol(f"g{i}") for i in range(5)])
    termA = (alpha.T * g)[0]                      # (A) = alpha^T E[delta]
    termC = sp.Rational(1, 2) * (Hphi * V).trace()         # (C) = 1/2 tr(H_phi Iobs^-1)
    halfRIV = sp.Rational(1, 2) * (IF * V).trace()         # 1/2 tr(RIV) = 1/2 tr(I_F Iobs^-1)
    Deltan = termA + sp.Rational(1, 2) * ((Hphi + IF) * V).trace()   # Delta_n (Taylor)
    scalar_ok = sp.simplify(Deltan - (halfRIV + termA + termC)) == 0

    checks = [
        ("(I1)  grad C_n(th0) = alpha  (entropy grad = cross-entropy grad)", z_vec(gradCn - alpha)),
        ("      alpha is covariance-only (alpha_mu = 0)", sp.simplify(alpha[0]) == 0 and sp.simplify(alpha[1]) == 0),
        ("(Bart) mixed d2_phipsi F = +I_F", z_mat(MIX - IF)),
        ("(I2)  hess C_n(th0) = H_phi + I_F  [entropy-Hessian split]", z_mat(hessCn - (Hphi + IF))),
        ("(Iss) H_phi + I_F mu-block = 0  (known-scale Isserlis identity)", z_mat((Hphi + IF)[0:2, 0:2])),
        ("[scalar] Delta_n - [1/2 tr(RIV) + (A) + (C)] == 0", scalar_ok),
    ]
    ok = True
    for label, passed in checks:
        ok = ok and bool(passed)
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")

    print(f"       sanity: entropy gradient alpha_sigma22 (nonzero) -> {sp.simplify(alpha[4])}")
    print("\nSymPy CAS:", "Delta_n = 1/2 tr(RIV) + (A)+(C) CONFIRMED" if ok
          else "MISMATCH -- investigate")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
