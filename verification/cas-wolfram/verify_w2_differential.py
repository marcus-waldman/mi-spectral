#!/usr/bin/env python
r"""CAS check of the W2 LRT-differential trace algebra (todo/024 D1, session 2026-06-04).

The MI LRT numerator d_L = 2[Qbar(psi*) - Qbar(g(gamma*))] is, at H0 and to leading
order, a difference of constrained/unconstrained maxima of the SAME quadratic with
gradient Z = grad Qbar(theta_0) and curvature J -> I_com, so

    E[d_L]   = tr( M_com Var(Z) ) + o(1),   M_com := I_com^-1 - G (G' I_com G)^-1 G',
    Var(Z)   = I_com I_obs^-1 I_com + O(sqrt n),
    E[d_com] = q_d + O(1/n)                  (Wilks),

giving the DIRECT H0 differential bias

    B_direct := tr( M_com I_com I_obs^-1 I_com ) - q_d .

The naive "difference of self-contained levels" prediction (each model imputing
from its own fit, e.g. the committed W2 bias_correction = trRIV_un - trRIV_cn) is

    D_naive := [tr(I_obs^-1 I_com) - k] - [tr((G' I_obs G)^-1 G' I_com G) - k0]
             = tr(RIV_f) - tr(RIV_0).

This script verifies, exactly (sympy) and over random PD instances (numpy):

  [A1] assembly identity:
       B_direct == [tr(I_obs^-1 I_com) - k] - [tr((G' I_com G)^-1 G' I_com I_obs^-1 I_com G) - k0].
  [A2] projection algebra: M_com I_com M_com == M_com,  M_com I_com G == 0.
  [A3] proportional-information (EFMI) collapse: I_com = (1+r) I_obs
       ==> B_direct == D_naive == r * q_d, symbolically.
  [B1] Gram/Schur matrix inequality behind the comparison:
       G' B A^-1 B G  >=  (G'BG)(G'AG)^-1(G'BG)   (A = I_obs, B = I_com, both PD)
       ==> B_direct <= D_naive ALWAYS; strict generically.
  [B2] equality case: col(G) invariant under I_obs^-1 I_com (constructed via
       simultaneously block-diagonal I_obs, I_com) ==> B_direct == D_naive.
  [B3] generic strictness: random PD instances give B_direct < D_naive with a
       strictly positive gap (reported), i.e. the naive difference OVERSTATES the
       H0 differential bias whenever col(G) is not invariant under I_obs^-1 I_com.

Run:    py verification/cas-wolfram/verify_w2_differential.py
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


def sym_pd(prefix, n):
    """Generic symmetric symbolic matrix (entries free symbols)."""
    M = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            s = sp.Symbol(f"{prefix}{i}{j}")
            M[i, j] = s
            M[j, i] = s
    return M


def b_direct(Iobs, Icom, G, k, k0):
    Mcom = Icom.inv() - G * (G.T * Icom * G).inv() * G.T
    return sp.trace(Mcom * Icom * Iobs.inv() * Icom) - (k - k0)


def d_naive(Iobs, Icom, G, k, k0):
    riv_f = sp.trace(Iobs.inv() * Icom) - k
    riv_0 = sp.trace((G.T * Iobs * G).inv() * (G.T * Icom * G)) - k0
    return riv_f - riv_0


def np_b_direct(Iobs, Icom, G):
    k = Iobs.shape[0]
    k0 = G.shape[1]
    Mcom = np.linalg.inv(Icom) - G @ np.linalg.inv(G.T @ Icom @ G) @ G.T
    return np.trace(Mcom @ Icom @ np.linalg.solve(Iobs, Icom)) - (k - k0)


def np_d_naive(Iobs, Icom, G):
    k = Iobs.shape[0]
    k0 = G.shape[1]
    riv_f = np.trace(np.linalg.solve(Iobs, Icom)) - k
    riv_0 = np.trace(np.linalg.solve(G.T @ Iobs @ G, G.T @ Icom @ G)) - k0
    return riv_f - riv_0


def rand_pd(rng, n):
    A = rng.standard_normal((n, n))
    return A @ A.T + n * np.eye(n)


def main():
    print("== [A] exact symbolic checks (k=3, k0=2, flat nesting G = [e1 e2]) ==")
    k = 3
    k0 = 2
    G = sp.Matrix([[1, 0], [0, 1], [0, 0]])
    Iobs = sym_pd("o", k)
    Icom = sym_pd("c", k)

    # A1: assembly identity
    lhs = b_direct(Iobs, Icom, G, k, k0)
    rhs = (sp.trace(Iobs.inv() * Icom) - k) - (
        sp.trace((G.T * Icom * G).inv() * (G.T * Icom * Iobs.inv() * Icom * G)) - k0
    )
    check("A1 assembly identity", sp.simplify(lhs - rhs) == 0)

    # A2: projection algebra
    Mcom = Icom.inv() - G * (G.T * Icom * G).inv() * G.T
    check("A2a  M_com I_com M_com == M_com",
          sp.simplify(Mcom * Icom * Mcom - Mcom) == sp.zeros(k, k))
    check("A2b  M_com I_com G == 0",
          sp.simplify(Mcom * Icom * G) == sp.zeros(k, k0))

    # A3: proportional information => both formulas collapse to r*q_d
    r = sp.Symbol("r", positive=True)
    Icom_p = (1 + r) * Iobs
    bd = sp.simplify(b_direct(Iobs, Icom_p, G, k, k0))
    dn = sp.simplify(d_naive(Iobs, Icom_p, G, k, k0))
    check("A3a  EFMI: B_direct == r*q_d", sp.simplify(bd - r * (k - k0)) == 0)
    check("A3b  EFMI: D_naive == r*q_d", sp.simplify(dn - r * (k - k0)) == 0)

    # A4: route-form equivalences (Stage-1 routes, session 2026-06-04):
    #   levels route:    tr(RIV_f) - tr((G'I_com G)^-1 G'I_com I_obs^-1 I_mis G)
    #   quadratic route: tr(RIV_f) - [tr((G'I_com G)^-1 G'I_com I_obs^-1 I_com G) - k0]
    # both must equal B_direct exactly.
    Imis = Icom - Iobs
    riv_f = sp.trace(Iobs.inv() * Icom) - k
    lev = riv_f - sp.trace((G.T * Icom * G).inv() * (G.T * Icom * Iobs.inv() * Imis * G))
    quad = riv_f - (sp.trace((G.T * Icom * G).inv() * (G.T * Icom * Iobs.inv() * Icom * G)) - k0)
    bd_gen = b_direct(Iobs, Icom, G, k, k0)
    check("A4a  levels-route form == B_direct", sp.simplify(lev - bd_gen) == 0)
    check("A4b  quadratic-route form == B_direct", sp.simplify(quad - bd_gen) == 0)

    print("== [B] numeric checks over random PD instances ==")
    rng = np.random.default_rng(20260604)
    n_inst = 400
    gaps = []
    schur_min_eig = np.inf
    for _ in range(n_inst):
        kk = int(rng.integers(3, 9))
        kk0 = int(rng.integers(1, kk))
        A = rand_pd(rng, kk)                      # I_obs
        B = A + rand_pd(rng, kk) * 0.5            # I_com > I_obs (PD missing info)
        Gn = rng.standard_normal((kk, kk0))
        # B1 matrix inequality: G'BA^-1BG - (G'BG)(G'AG)^-1(G'BG) >= 0
        D0 = Gn.T @ B @ np.linalg.solve(A, B @ Gn)
        C0 = Gn.T @ B @ Gn
        A0 = Gn.T @ A @ Gn
        Q = D0 - C0 @ np.linalg.solve(A0, C0)
        schur_min_eig = min(schur_min_eig, float(np.linalg.eigvalsh((Q + Q.T) / 2).min()))
        gaps.append(np_d_naive(A, B, Gn) - np_b_direct(A, B, Gn))
    gaps = np.array(gaps)
    check("B1a  Gram/Schur inequality (min eig >= -1e-9)", schur_min_eig >= -1e-9,
          f"min eig = {schur_min_eig:.3e}")
    check("B1b  B_direct <= D_naive on all instances", bool((gaps >= -1e-9).all()),
          f"min gap = {gaps.min():.3e}")
    check("B3   strict generically", bool((gaps > 1e-8).mean() > 0.95),
          f"median gap = {np.median(gaps):.4f}, frac strict = {(gaps > 1e-8).mean():.3f}")

    # B2: equality when col(G) invariant under I_obs^-1 I_com
    # (construct: I_obs, I_com simultaneously block-diagonal in the G-split)
    eq_gaps = []
    for _ in range(60):
        kk = int(rng.integers(3, 8))
        kk0 = int(rng.integers(1, kk))
        A1b = rand_pd(rng, kk0)
        A2b = rand_pd(rng, kk - kk0)
        B1b = A1b + 0.5 * rand_pd(rng, kk0)
        B2b = A2b + 0.5 * rand_pd(rng, kk - kk0)
        Z01 = np.zeros((kk0, kk - kk0))
        A = np.block([[A1b, Z01], [Z01.T, A2b]])
        B = np.block([[B1b, Z01], [Z01.T, B2b]])
        Gn = np.vstack([np.eye(kk0), np.zeros((kk - kk0, kk0))])
        eq_gaps.append(abs(np_d_naive(A, B, Gn) - np_b_direct(A, B, Gn)))
    check("B2   equality under invariant col(G)", max(eq_gaps) < 1e-9,
          f"max |gap| = {max(eq_gaps):.3e}")

    # B4: Mode-B closed form for the overstatement gap (GPT-5.5 red-team bonus, todo/024).
    #   gap := D_naive - B_direct = tr( (I + H11)^-1 H12 H12' ),
    # where H = Iobs^-1/2 I_mis Iobs^-1/2 is the standardized missing information and
    # (H11, H12) is its partition by the model/tested orthonormal split (U1 spanning
    # col(Iobs^1/2 G), U2 the complement). The gap is >= 0 (PSD), = 0 iff H12 = 0 (the
    # invariance/EFMI / block-diagonal case) -- a sharp form of Proposition L2.
    cf_err = []
    for _ in range(200):
        kk = int(rng.integers(3, 9))
        kk0 = int(rng.integers(1, kk))
        A = rand_pd(rng, kk)                          # I_obs
        B = A + 0.5 * rand_pd(rng, kk)                # I_com (PSD missing info)
        Gn = rng.standard_normal((kk, kk0))
        wo, Uo = np.linalg.eigh((A + A.T) / 2)
        Ah = Uo @ np.diag(np.sqrt(wo)) @ Uo.T         # I_obs^1/2
        Aih = Uo @ np.diag(wo ** -0.5) @ Uo.T         # I_obs^-1/2
        H = Aih @ (B - A) @ Aih
        Qf, _ = np.linalg.qr(np.hstack([Ah @ Gn, rng.standard_normal((kk, kk - kk0))]))
        U1 = Qf[:, :kk0]
        U2 = Qf[:, kk0:]
        H11 = U1.T @ H @ U1
        H12 = U1.T @ H @ U2
        gap_cf = np.trace(np.linalg.solve(np.eye(kk0) + H11, H12 @ H12.T))
        gap_direct = np_d_naive(A, B, Gn) - np_b_direct(A, B, Gn)
        cf_err.append(abs(gap_cf - gap_direct))
    check("B4   gap == tr((I+H11)^-1 H12 H12') (Mode-B closed form)", max(cf_err) < 1e-7,
          f"max |closed-form - direct| = {max(cf_err):.2e}")

    print()
    if FAIL:
        print("RESULT: MISMATCH — investigate before landing D1.")
    else:
        print("RESULT: all CAS checks pass. B_direct <= D_naive (equality iff col(G)")
        print("        invariant under I_obs^-1 I_com, incl. EFMI); naive difference of")
        print("        self-contained tr(RIV)s OVERSTATES the H0 differential bias otherwise.")
    return FAIL


if __name__ == "__main__":
    sys.exit(main())
