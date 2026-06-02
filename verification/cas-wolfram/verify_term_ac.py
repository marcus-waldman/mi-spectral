#!/usr/bin/env python
r"""Independent Wolfram re-derivation of the bivariate-monotone (A)+(C) closed form
(manuscript/derivation.qmd:728,772), derived from the SETUP only -- not transcribed
from the MI-IC v4 Steps 6-7 derivation that the manuscript imports.

This upgrades the earlier consistency check (verify_traces.py group 3) to a genuine
re-derivation: Wolfram symbolically derives the two model-specific objects -- the
conditional cross-entropy gradient alpha and curvature H_phi -- and assembles
(A)+(C). Only two textbook quantities are taken as inputs (flagged below):
  * E[delta_s2] = -2 s2 / n_obs : the p=2 regression residual-variance MLE bias
                                  (E[hat-sigma^2] = sigma^2 (n-p)/n);
  * I_obs(mean block) = (1/s2) Mobs : complete-case Gaussian regression information.

Setup (bivariate monotone MVN): X2 fully observed; X1 observed on n_obs complete
units and missing on n_mis units; MAR selection on X2 makes the X2 design moment of
the missing units (Mmis = sum [1,X2][1,X2]^T) differ from that of the complete units
(Mobs). The analyst's congenial MLE imputation has phi = theta_obs, so

  f0(phi) = sum_{i:mis} E_{X1~phi}[ log p(X1_i | X2_i ; theta0) ]   (conditional cross-entropy)
  (A) = E[delta]^T alpha,   alpha = grad_phi f0 |theta0   (variance-only)
  (C) = 1/2 tr(H_phi I_obs^-1),  H_phi = hess_phi f0 |theta0

DERIVED by Wolfram here: alpha, H_phi (from the Gaussian cross-entropy).
Target:  (A)+(C) = (n_mis/n_obs)[1 - 1/2 tr(Q_mis Q_obs^-1)],  Q = M/n,  = 0 under MCAR.

Run:    py verification/cas-wolfram/verify_term_ac.py
Needs:  wolframclient + a local Wolfram kernel (auto-discovered; override WOLFRAM_KERNEL).
Exit:   0 all pass; 1 a mismatch (investigate); 2 setup missing.
"""
import glob
import os
import sys
import time


# Wolfram derivation. s2 = true conditional variance; (b0,b1) true regression coefs;
# (c0,c1,sf) the phi-conditional coefs/variance; x a generic observed X2 value;
# Mmis = {{m11,m12},{m12,m22}}, Mobs = {{p11,p12},{p12,p22}} the summed design moments.
WL = r"""
Module[{b0, b1, s2, c0, c1, sf, x, m0, mphi, g, sub0, aC0, aC1, aS,
        Hmean, Hphi, Iobs, alpha, Edelta, termA, termC, ac, target, mcar},
  m0   = b0 + b1 x;
  mphi = c0 + c1 x;
  (* per-unit conditional cross-entropy: E_{X1 ~ N(mphi,sf)}[ log N(X1; m0, s2) ] *)
  g = -(1/2) Log[2 Pi s2] - (1/(2 s2)) ((mphi - m0)^2 + sf);
  sub0 = {c0 -> b0, c1 -> b1, sf -> s2};                         (* evaluate at phi = theta0 *)

  (* --- DERIVED: entropy gradient alpha (per unit), at phi = theta0 --- *)
  aC0 = D[g, c0] /. sub0;                                        (* -> 0 (mean coef) *)
  aC1 = D[g, c1] /. sub0;                                        (* -> 0 (mean coef) *)
  aS  = D[g, sf]  /. sub0;                                       (* -> -1/(2 s2) (variance) *)

  (* --- DERIVED: cross-entropy curvature H_phi (mean block, per unit) --- *)
  Hmean = {{D[g, {c0, 2}], D[D[g, c0], c1]},
           {D[D[g, c0], c1], D[g, {c1, 2}]}} /. sub0;            (* -> -(1/s2){{1,x},{x,x^2}} *)

  (* --- ASSEMBLE: sum the verified per-unit pieces over the n_mis missing units --- *)
  Hphi  = -(1/s2) {{m11, m12}, {m12, m22}};                      (* sum_{mis} -(1/s2)[1,x][1,x]^T = -(1/s2) Mmis *)
  alpha = nmis * aS;                                             (* sum_{mis} aS = -nmis/(2 s2) *)
  Iobs   = (1/s2) {{p11, p12}, {p12, p22}};                      (* INPUT: complete-case regression info = (1/s2) Mobs *)
  Edelta = -2 s2 / nobs;                                         (* INPUT: p=2 residual-variance MLE bias *)

  (* alpha is variance-only, so (A) picks up only the variance coordinate *)
  termA = Edelta * alpha;                                        (* -> nmis/nobs *)
  termC = (1/2) Tr[Hphi . Inverse[Iobs]];                        (* -> -(nmis/2nobs) tr(Mmis Mobs^-1) *)
  ac    = Simplify[termA + termC];

  target = (nmis/nobs) (1 - (1/2) Tr[({{m11, m12}, {m12, m22}}/nmis) .
                                     Inverse[{{p11, p12}, {p12, p22}}/nobs]]);
  (* MCAR: equal per-unit design moments  Mmis = (nmis/nobs) Mobs *)
  mcar = Simplify[ac /. {m11 -> (nmis/nobs) p11, m12 -> (nmis/nobs) p12, m22 -> (nmis/nobs) p22}];

  {
    Simplify[aC0],                                                          (* 0   *)
    Simplify[aC1],                                                          (* 0   *)
    Simplify[aS + 1/(2 s2)],                                                (* 0   *)
    AllTrue[Flatten[Simplify[Hmean + (1/s2) {{1, x}, {x, x^2}}]], (# === 0) &],  (* True *)
    Simplify[termA - nmis/nobs],                                            (* 0   *)
    Simplify[ac - target],                                                  (* 0   *)
    mcar                                                                    (* 0   *)
  }
]
"""


def discover_kernel():
    r"""Locate the Wolfram kernel binary (see verify_traces.py for the why)."""
    env = os.environ.get("WOLFRAM_KERNEL")
    if env:
        return env
    roots = [
        r"C:\Program Files\Wolfram Research\*\*\SystemFiles\Kernel\Binaries\Windows-x86-64\WolframKernel.exe",
        r"C:\Program Files\Wolfram Research\*\SystemFiles\Kernel\Binaries\Windows-x86-64\WolframKernel.exe",
    ]
    matches = sorted(m for r in roots for m in glob.glob(r))
    return matches[-1] if matches else None


def _start_with_retry(session_cls, wlexpr, kernel, attempts=3, delay=3):
    last = None
    for i in range(1, attempts + 1):
        session = None
        try:
            session = session_cls(kernel) if kernel else session_cls()
            session.evaluate(wlexpr("1"))
            return session
        except Exception as e:
            last = e
            if session is not None:
                try:
                    session.terminate()
                except Exception:
                    pass
            if i < attempts:
                print(f"  kernel start attempt {i} failed ({type(e).__name__}); retrying in {delay}s...")
                time.sleep(delay)
    raise last


def main():
    try:
        from wolframclient.evaluation import WolframLanguageSession
        from wolframclient.language import wlexpr
    except ImportError:
        print("wolframclient not installed  ->  py -m pip install wolframclient")
        return 2

    kernel = discover_kernel()
    if kernel:
        print(f"Using kernel: {kernel}")
    try:
        session = _start_with_retry(WolframLanguageSession, wlexpr, kernel)
    except Exception as e:
        print(f"No Wolfram kernel after retries ({type(e).__name__}: {e}).")
        print("Launch the Wolfram app once to finish first-run activation, or set WOLFRAM_KERNEL.")
        return 2

    try:
        print(f"Wolfram kernel: {session.evaluate(wlexpr('$Version'))}\n")
        aC0, aC1, aS, hmean, termA, ac, mcar = session.evaluate(wlexpr(WL))
    finally:
        session.terminate()

    checks = [
        ("[derived] entropy gradient alpha, intercept coef            == 0", "zero", aC0),
        ("[derived] entropy gradient alpha, slope coef                == 0", "zero", aC1),
        ("[derived] entropy gradient alpha, variance = -1/(2 s^2)     == 0", "zero", aS),
        ("[derived] cross-entropy curvature H_phi = -(1/s^2)[1,x][1,x]^T   matrix", "true", hmean),
        ("[assemble] (A) = n_mis/n_obs                                == 0", "zero", termA),
        ("[assemble] (A)+(C) = (n_mis/n_obs)[1 - 1/2 tr(Q_mis Q_obs^-1)] == 0", "zero", ac),
        ("[collapse] MCAR (equal per-unit design moments)             == 0", "zero", mcar),
    ]
    ok = True
    for label, kind, val in checks:
        passed = (val == 0) if kind == "zero" else (val is True)
        ok = ok and passed
        print(f"[{'PASS' if passed else 'FAIL'}] {label}   (Wolfram -> {val})")

    print("\nWolfram CAS:", "(A)+(C) BIVARIATE CLOSED FORM RE-DERIVED" if ok
          else "MISMATCH -- investigate")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
