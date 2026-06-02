#!/usr/bin/env python
r"""Independent Wolfram derivation of the NON-MONOTONE covariance-MLE second-order
bias b_Sigma = lim_n n*E[Sigma_hat_obs - Sigma], via the Cox-Snell (1968, eq. 20)
machinery [coxGeneralDefinitionResiduals1968; cordeiroBiasCorrectionARMA1994;
patriotaBiasCorrectionMultivariate2009].  This is Layer-2 TODO-B of todo/013 and the
one open ingredient of the general-MVN (A)+(C) design-imbalance asymptote
(manuscript/derivation.qmd @sec-termA): (A)+(C)_inf = alpha^T b_Sigma + 1/2 tr(H_phi I_obs^-1).
The monotone closed form (verify_term_ac.py, d2ba31c) is the reduction target; for
non-monotone patterns the observed-data likelihood does NOT factor and no published
b_Sigma exists, so we derive it.

SETUP (minimal non-factoring case -- todo/014 sec.3).  Bivariate (X1,X2)~N(mu,Sigma)
with THREE unit groups under a coherent non-monotone MAR mechanism:
  * complete   (observe X1,X2)         per-unit logdensity l_c
  * X1-missing (observe X2)            l_a = log N(x2; mu2, s22)
  * X2-missing (observe X1)            l_b = log N(x1; mu1, s11)
The two incomplete patterns {X2},{X1} do not nest => non-monotone; the joint MLE has
no closed form.  Parameter theta = (m1,m2,s11,s12,s22) (vech order = R's column-major
lower-tri (sig11,sig21,sig22)).

MAR MECHANISM (additive half-sigmoid, todo/014).  sigma(.) the logistic sigmoid,
eta1=a1+b1*x2, eta2=a2+b2*x1:
  P(miss1|x) = (1/2) sigma(eta1)   -- depends ONLY on the observed x2,
  P(miss2|x) = (1/2) sigma(eta2)   -- depends ONLY on the observed x1,
  P(complete|x) = 1 - P(miss1) - P(miss2).
The 1/2 caps keep P(complete) in [0,1].  This is genuinely MAR (each pattern's prob
depends only on that pattern's OBSERVED block -- a shared multinomial-logit denominator
would make P(miss1) depend on x1, i.e. MNAR; the zero-score gate detects that), so the
observed-data score has mean zero at theta0 (consistency/ignorability).  b1=b2=0 => MCAR.

COX-SNELL.  Per-unit cumulants (joint expectation over (X,pattern) at theta0):
  i_rs   = -E[ d^2 l_P ],  j_{t,ru} = E[ d l_P d^2 l_P ],  k_rtu = E[ d^3 l_P ],
each = E_X[ wc*(.)_c + wa*(.)_a + wb*(.)_b ].  Then (per-unit cumulants give the
n->inf limit directly):
  b_s = 1/2 sum_{r,t,u} i^{rs} i^{tu} ( k_rtu + 2 j_{t,ru} ),   b_Sigma = (b_s11,b_s12,b_s22).

INTERNAL GATES (printed): (1) zero-score max|E[U_r]| ~ 0 (validates the expectation
setup + ignorability); (2) Bartlett max|E[U U^T] - i| ~ 0 (info = Var(score)).
SCENARIO GATES: non-monotone (headline), MCAR (b1=b2=0), monotone-reduction (drop miss2
via a2->-inf).  The monotone-reduction b_Sigma is cross-checked against the verified
recursion in R (verify_term_ac_nonmonotone.R).

Run:    py verification/cas-wolfram/verify_term_ac_nonmonotone.py
Writes: verification/cache/coxsnell-nonmonotone-bsigma.json  (consumed by the R assembler).
Exit:   0 internal gates pass; 1 a gate failed; 2 setup missing.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _wolfram import open_session


# --- theta0 (exact rationals) and mechanism (decimals). rho=1/2 matches TAMAR_BIV_SIG. ---
# selection a (~20% each missing at b=0) and slope b overridable via TAMAR_A / TAMAR_B env
# (run at the headline b to match the SymPy sweep's two-CAS check).
THETA0 = {"M1": "0", "M2": "0", "S11": "1", "S12": "1/2", "S22": "1"}
A_SEL = os.environ.get("TAMAR_A", "-0.4")
B_SEL = os.environ.get("TAMAR_B", "1.6")
MECH_NONMONO = {"A1": A_SEL, "B1": B_SEL, "A2": A_SEL, "B2": B_SEL}
MECH_MCAR    = {"A1": A_SEL, "B1": "0.0", "A2": A_SEL, "B2": "0.0"}
# monotone reduction: a2 -> -inf (sigma(eta2)~0 => no X2-missing group). keep miss1 selection.
MECH_MONO    = {"A1": A_SEL, "B1": B_SEL, "A2": "-50.0", "B2": "0.0"}


WL_TEMPLATE = r"""
Module[{pars, mu, Sig, lc, la, lb, sub0, Uc, Ua, Ub, Vc, Va, Vb, Wc, Wa, Wb,
        eta1, eta2, Zden, wc, wa, wb, pdf2, mkMoms, momC, momA, momB, EW, Etot,
        imat, jt, kt, iinv, biasOf, bS, bm, zsr, EUU, bart, fracs, mlist},
  pars = {m1, m2, s11, s12, s22};
  mu  = {m1, m2};
  Sig = {{s11, s12}, {s12, s22}};
  lc = -(1/2) Log[Det[Sig]] - (1/2) ({x1, x2} - mu) . Inverse[Sig] . ({x1, x2} - mu);
  la = -(1/2) Log[s22] - (x2 - m2)^2/(2 s22);   (* miss1: observe x2 *)
  lb = -(1/2) Log[s11] - (x1 - m1)^2/(2 s11);   (* miss2: observe x1 *)
  sub0 = {m1 -> @M1@, m2 -> @M2@, s11 -> @S11@, s12 -> @S12@, s22 -> @S22@};

  (* exact symbolic 1st/2nd/3rd derivatives, then evaluate theta0 -> polynomials in x1,x2 *)
  Uc = Table[D[lc, pars[[r]]], {r, 5}] /. sub0;
  Ua = Table[D[la, pars[[r]]], {r, 5}] /. sub0;
  Ub = Table[D[lb, pars[[r]]], {r, 5}] /. sub0;
  Vc = Table[D[lc, pars[[r]], pars[[s]]], {r, 5}, {s, 5}] /. sub0;
  Va = Table[D[la, pars[[r]], pars[[s]]], {r, 5}, {s, 5}] /. sub0;
  Vb = Table[D[lb, pars[[r]], pars[[s]]], {r, 5}, {s, 5}] /. sub0;
  Wc = Table[D[lc, pars[[r]], pars[[s]], pars[[t]]], {r, 5}, {s, 5}, {t, 5}] /. sub0;
  Wa = Table[D[la, pars[[r]], pars[[s]], pars[[t]]], {r, 5}, {s, 5}, {t, 5}] /. sub0;
  Wb = Table[D[lb, pars[[r]], pars[[s]], pars[[t]]], {r, 5}, {s, 5}, {t, 5}] /. sub0;

  (* additive half-sigmoid MAR weights: P(miss1) depends only on x2, P(miss2) only on x1 *)
  eta1 = @A1@ + @B1@ x2;
  eta2 = @A2@ + @B2@ x1;
  wa = (1/2)/(1 + Exp[-eta1]);
  wb = (1/2)/(1 + Exp[-eta2]);
  wc = 1 - wa - wb;

  pdf2 = PDF[MultinormalDistribution[{@M1@, @M2@}, {{@S11@, @S12@}, {@S12@, @S22@}}], {x1, x2}];
  (* moment table E[w * x1^a x2^b], a+b<=4 (covers all deg-<=4 derivative products) *)
  mkMoms[w_] := Association @@ Flatten[Table[
      {ai, bi} -> Quiet[NIntegrate[pdf2 w x1^ai x2^bi, {x1, -8, 8}, {x2, -8, 8},
                             Method -> {"GlobalAdaptive", "SymbolicProcessing" -> 0},
                             MaxRecursion -> 16, PrecisionGoal -> 8, AccuracyGoal -> 12],
                        NIntegrate::slwcon],
      {ai, 0, 4}, {bi, 0, 4 - ai}]];
  momC = mkMoms[wc]; momA = mkMoms[wa]; momB = mkMoms[wb];
  (* E[w * poly]: expand poly in monomials, dot with the moment table *)
  EW[mom_, poly_] := Module[{cr}, cr = CoefficientRules[Expand[poly], {x1, x2}];
     Total[(Last /@ cr) * (mom /@ (First /@ cr))]];
  Etot[ec_, ea_, eb_] := EW[momC, ec] + EW[momA, ea] + EW[momB, eb];

  (* per-unit Cox-Snell cumulants *)
  imat = Table[-Etot[Vc[[r, s]], Va[[r, s]], Vb[[r, s]]], {r, 5}, {s, 5}];
  jt   = Table[ Etot[Uc[[t]] Vc[[r, u]], Ua[[t]] Va[[r, u]], Ub[[t]] Vb[[r, u]]],
               {t, 5}, {r, 5}, {u, 5}];
  kt   = Table[ Etot[Wc[[r, t, u]], Wa[[r, t, u]], Wb[[r, t, u]]],
               {r, 5}, {t, 5}, {u, 5}];
  iinv = Inverse[imat];
  biasOf[s_] := (1/2) Sum[iinv[[r, s]] iinv[[t, u]] (kt[[r, t, u]] + 2 jt[[t, r, u]]),
                          {r, 5}, {t, 5}, {u, 5}];
  bS = biasOf /@ {3, 4, 5};      (* b_sigma : (s11, s12, s22) *)
  bm = biasOf /@ {1, 2};         (* b_mu    : (m1, m2)        *)

  (* gates *)
  zsr  = Table[Etot[Uc[[r]], Ua[[r]], Ub[[r]]], {r, 5}];                  (* ~ 0 *)
  EUU  = Table[Etot[Uc[[r]] Uc[[s]], Ua[[r]] Ua[[s]], Ub[[r]] Ub[[s]]], {r, 5}, {s, 5}];
  bart = Max[Abs[Flatten[EUU - imat]]];                                  (* ~ 0 *)
  fracs = {EW[momC, 1], EW[momA, 1], EW[momB, 1]};                       (* f_c, f_a, f_b *)

  mlist = Join[bS, bm, fracs, {Max[Abs[zsr]], bart}];
  N[mlist, 12]
]
"""


def build_wl(mech):
    wl = WL_TEMPLATE
    for k, v in {**THETA0, **mech}.items():
        wl = wl.replace("@" + k + "@", v)
    return wl


def run_scenario(session, wlexpr, name, mech):
    res = session.evaluate(wlexpr(build_wl(mech)))
    vals = [float(x) for x in res]
    out = {
        "scenario": name,
        "b_sigma": {"s11": vals[0], "s12": vals[1], "s22": vals[2]},
        "b_mu": {"m1": vals[3], "m2": vals[4]},
        "fracs": {"complete": vals[5], "miss1": vals[6], "miss2": vals[7]},
        "zeroscore_max": vals[8],
        "bartlett_max": vals[9],
        "mech": mech,
    }
    return out


def main():
    try:
        session, wlexpr = open_session()
    except RuntimeError as e:
        print(e)
        return 2
    try:
        print(f"Wolfram kernel: {session.evaluate(wlexpr('$Version'))}\n")
        scenarios = [
            ("nonmonotone", MECH_NONMONO),
            ("mcar", MECH_MCAR),
            ("monotone_reduction", MECH_MONO),
        ]
        results = {}
        for name, mech in scenarios:
            print(f"-- scenario: {name}  (mech {mech}) --")
            r = run_scenario(session, wlexpr, name, mech)
            results[name] = r
            bs = r["b_sigma"]; f = r["fracs"]
            print(f"   fracs: complete={f['complete']:.4f} miss1={f['miss1']:.4f} miss2={f['miss2']:.4f}")
            print(f"   b_Sigma: s11={bs['s11']:+.5f} s12={bs['s12']:+.5f} s22={bs['s22']:+.5f}")
            print(f"   b_mu:    m1={r['b_mu']['m1']:+.2e} m2={r['b_mu']['m2']:+.2e}")
            print(f"   [gate] zero-score max|E[U]| = {r['zeroscore_max']:.2e}")
            print(f"   [gate] Bartlett max|E[UU]-i| = {r['bartlett_max']:.2e}\n")
    finally:
        session.terminate()

    # internal gates
    tol = 1e-5
    ok = True
    for name, r in results.items():
        zs = r["zeroscore_max"] < tol
        bt = r["bartlett_max"] < tol
        ok = ok and zs and bt
        print(f"[{'PASS' if zs else 'FAIL'}] {name}: zero-score identity  ({r['zeroscore_max']:.1e})")
        print(f"[{'PASS' if bt else 'FAIL'}] {name}: Bartlett info=Var(score)  ({r['bartlett_max']:.1e})")
    # b_mu: ~0 under MCAR; a small GENUINE O(1/n) mean bias under MAR (the mean MLE couples
    # to the biased Sigma_hat in the non-factoring non-monotone likelihood; both CAS agree on
    # it).  alpha is covariance-only, so b_mu never enters (A)+(C).
    for name, r in results.items():
        mb = max(abs(r["b_mu"]["m1"]), abs(r["b_mu"]["m2"]))
        if name == "mcar":
            good = mb < 1e-5
            ok = ok and good
            print(f"[{'PASS' if good else 'FAIL'}] {name}: b_mu ~ 0 (MCAR)  ({mb:.1e})")
        else:
            print(f"[info] {name}: b_mu = {mb:.2e}  (genuine small O(1/n) mean bias under MAR; cov-irrelevant)")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "cache", "coxsnell-nonmonotone-bsigma.json")
    out_path = os.path.abspath(out_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\nwrote {out_path}")
    print("\nWolfram CAS:", "NON-MONOTONE b_Sigma DERIVED (internal gates pass)" if ok
          else "INTERNAL GATE FAILED -- investigate")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
