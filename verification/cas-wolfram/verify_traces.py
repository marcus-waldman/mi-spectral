#!/usr/bin/env python
r"""Independent second-CAS verification (Wolfram, via wolframclient) of the
symbolic identities behind manuscript/derivation.qmd Appendix B.

Three groups, written from the math in Wolfram Language (NOT transliterated from
the SymPy), so agreement is implementation-decorrelated from the SymPy/NumPy
checks -- which had to hand-roll `trace_normal` around a sympy `Trace`/`simplify`
bug (see derivation.qmd:1255):

  1. [trace]  Headline algebra: Term A = +tr(RIV), Term B = -1/2 tr(RIV),
              Combine = +1/2 tr(RIV). Mirrors lst-mc-trriv/terma/termb/combine.
              -> independent re-check of the SymPy core.
  2. [mvn]    The Magnus duplication-matrix inverse identity that inverts the
              covariance-block information I_{vech S} = (N/2) D2'(S^-1 (x) S^-1) D2
              (sec-alg, cited to Magnus 2019), verified SYMBOLICALLY for p=2.
              -> upgrade: the repo otherwise checks the MVN info only numerically
                 (lst-mc-fisher).
  3. [A+C]    CONSISTENCY checks of the published design-imbalance closed form
              (derivation.qmd:728,772 -- itself derived in the MI-IC companion,
              v4 Steps 6-7, not here): the bivariate 2x2 MCAR collapse and the
              Exp(lambda) O(1/n) table row.
              -> consistency of the STATED form, NOT an independent re-derivation.

Run:    py verification/cas-wolfram/verify_traces.py
Needs:  py -m pip install wolframclient  +  a local Wolfram kernel (Engine/Mathematica).
        Auto-discovers the kernel on Windows; override with WOLFRAM_KERNEL.
Exit:   0 all pass; 1 a mismatch (investigate); 2 setup missing.
"""
import glob
import os
import sys
import time


# --- Group 1: trace identities (each scalar must reduce to 0) -----------------
WL_TRACE = r"""
Module[{n = 3, sym, Icom, Iobs, Imis, trRIV},
  sym[s_] := With[{M = Array[s, {n, n}]}, (M + Transpose[M])/2];   (* generic symmetric *)
  Icom = sym[c]; Iobs = sym[o]; Imis = Icom - Iobs;               (* I_{mis|obs} := I_com - I_obs *)
  trRIV = Tr[Inverse[Iobs] . Icom] - n;                           (* tr(RIV) = tr(I_obs^-1 I_com) - n *)
  {
    Simplify[Tr[Imis . Inverse[Iobs]] - trRIV],                              (* Term A  *)
    Simplify[(-1/2) Tr[Icom . (Inverse[Iobs] - Inverse[Icom])] + trRIV/2],   (* Term B  *)
    Simplify[(Tr[Imis . Inverse[Iobs]]
              - (1/2) Tr[Icom . (Inverse[Iobs] - Inverse[Icom])]) - trRIV/2] (* Combine *)
  }
]
"""

# --- Group 2: MVN Magnus duplication-matrix inverse identity (p=2) ------------
# (D2'(S^-1 (x) S^-1) D2)^-1 == (D2'D2)^-1 D2' (S (x) S) D2 (D2'D2)^-1   [Magnus 2019]
# i.e. the closed-form inverse of the covariance-block Fisher information
# I_{vech S} = (N/2) D2'(S^-1 (x) S^-1) D2 (sec-alg / D15). Symbolic, parameter-free.
WL_MVN = r"""
Module[{Sig, Sinv, D2, DtD, lhs, rhs},
  Sig = {{s11, s12}, {s12, s22}};
  Sinv = Inverse[Sig];
  D2 = {{1, 0, 0}, {0, 1, 0}, {0, 1, 0}, {0, 0, 1}};   (* vec(A) = D2 . vech(A), p=2 *)
  DtD = Transpose[D2] . D2;
  lhs = Inverse[Transpose[D2] . KroneckerProduct[Sinv, Sinv] . D2];
  rhs = Inverse[DtD] . Transpose[D2] . KroneckerProduct[Sig, Sig] . D2 . Inverse[DtD];
  AllTrue[Flatten[FullSimplify[lhs - rhs]], (# === 0) &]
]
"""

# --- Group 3: (A)+(C) published-closed-form consistency -----------------------
# The forms are derived in the MI-IC companion (v4 Steps 6-7); here we only check
# the STATED forms are internally consistent: the bivariate MCAR collapse (2x2
# design moment Q = intercept + conditioning variable) and the Exp(lambda) row.
WL_AC = r"""
Module[{Q, Qm, Qo, mcar, mar, expRow},
  Q = {{q11, q12}, {q12, q22}};                                     (* 2x2 design 2nd-moment *)
  mcar = FullSimplify[(nmis/nobs) (1 - (1/2) Tr[Q . Inverse[Q]])];  (* Q_mis = Q_obs -> 0 *)
  Qm = {{a11, a12}, {a12, a22}}; Qo = {{b11, b12}, {b12, b22}};
  mar = FullSimplify[(nmis/nobs) (1 - (1/2) Tr[Qm . Inverse[Qo]])]; (* generic MAR -> nonzero *)
  expRow = Simplify[nmis/(nobs - 1) - nmis/nobs - nmis/(nobs (nobs - 1))];  (* Exp(lambda) -> 0 *)
  {mcar, mar =!= 0, expRow}
]
"""


def discover_kernel():
    r"""Locate the Wolfram kernel binary.

    wolframclient's autodiscovery can miss it on Windows, and the top-level
    ``...\<ver>\WolframKernel.exe`` is a launcher that does not complete the WSTP
    handshake with the client -- the architecture binary under
    SystemFiles\Kernel\Binaries is the one that works. Honor WOLFRAM_KERNEL if
    set, else find the deep binary, else fall back to wolframclient autodiscovery.
    """
    env = os.environ.get("WOLFRAM_KERNEL")
    if env:
        return env
    roots = [
        r"C:\Program Files\Wolfram Research\*\*\SystemFiles\Kernel\Binaries\Windows-x86-64\WolframKernel.exe",
        r"C:\Program Files\Wolfram Research\*\SystemFiles\Kernel\Binaries\Windows-x86-64\WolframKernel.exe",
    ]
    matches = sorted(m for r in roots for m in glob.glob(r))
    return matches[-1] if matches else None  # None -> let wolframclient autodiscover


def _start_with_retry(session_cls, wlexpr, kernel, attempts=3, delay=3):
    """Start a Wolfram session, retrying transient handshake failures.

    Fresh Wolfram installs intermittently abort the WSTP/ZMQ startup on the
    first few launches (background activation / paclet setup); a short retry
    self-heals it. Forces a trivial evaluation so the handshake actually
    completes before the session is returned.
    """
    last = None
    for i in range(1, attempts + 1):
        session = None
        try:
            session = session_cls(kernel) if kernel else session_cls()
            session.evaluate(wlexpr("1"))  # force kernel start + handshake
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
        tA, tB, tC = session.evaluate(wlexpr(WL_TRACE))
        mvn = session.evaluate(wlexpr(WL_MVN))
        mcar, mar_nonzero, exp_row = session.evaluate(wlexpr(WL_AC))
    finally:
        session.terminate()

    # kind "zero" -> pass iff value == 0; kind "true" -> pass iff value is True
    checks = [
        ("[trace] Term A   Tr(I_mis I_obs^-1) - tr(RIV)                  == 0", "zero", tA),
        ("[trace] Term B   -1/2 Tr(I_com(I_obs^-1 - I_com^-1)) + tr(RIV)/2 == 0", "zero", tB),
        ("[trace] Combine  A + B - tr(RIV)/2                              == 0", "zero", tC),
        ("[mvn]   Magnus duplication-matrix inverse identity (p=2)        symbolic", "true", mvn),
        ("[A+C]   bivariate MCAR collapse  (Q_mis = Q_obs, 2x2)           == 0", "zero", mcar),
        ("[A+C]   MAR generic design imbalance is nonzero                 (sanity)", "true", mar_nonzero),
        ("[A+C]   Exp(lambda) row  = n_mis/[n_obs(n_obs-1)]               == 0", "zero", exp_row),
    ]
    ok = True
    for label, kind, val in checks:
        passed = (val == 0) if kind == "zero" else (val is True)
        ok = ok and passed
        print(f"[{'PASS' if passed else 'FAIL'}] {label}   (Wolfram -> {val})")

    print("\nWolfram CAS:", "ALL CHECKS CONFIRMED" if ok
          else "MISMATCH -- investigate before trusting the SymPy result")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
