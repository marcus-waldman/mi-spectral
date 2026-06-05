#!/usr/bin/env python
r"""CAS check of the non-nested CS-vs-AR(1) measurement's analytic pieces (todo/029, A1-A5).

The measurement (Proposition L4, derivation.qmd @sec-lrt-ac) compares two curved covariance
candidates fit by constrained Qbar-maximization on the MI E-step moments S*:

  CS  : Sigma = sigma^2 [(1-rho) I + rho J]          -- closed-form maximizer
  AR1 : Sigma = sigma^2 R(rho), R_ij = rho^|i-j|     -- 1-D profile maximizer

and uses the GENERAL-JACOBIAN form of the @sec-lrt spectrum machinery: for candidate k with
analytic Jacobian G_k = d(mu, vech Sigma)/d(mu, sigma^2, rho) (14 x 6), the bias correction is
tr(RIV_perp,k) and the null law W_k = sum lambda_{k,j} chi^2_1 with lambda = nonzero eig of A V,
A = I_com^-1 - G (G' I_com G)^-1 G', V = I_com I_obs^-1 I_com, q_d = 14 - 6 = 8.

verify_ic_ladder.py L-A3 already blesses the spectrum-trace identity for generic full-rank G with
random PD information matrices. This file pins the pieces SPECIFIC to the curved candidates:

  [A1] CS closed form (a_hat = 1'S1/p on span(1), b_hat = tr(QS)/(p-1) on the complement;
       sigma^2 = tr(S)/p, rho = (a-b)/(a+(p-1)b)) is the exact minimizer of the Qbar deviance
       f(Sigma) = log|Sigma| + tr(Sigma^-1 S) over the CS family: zero gradient + local min, on
       the frozen Sigma_truth and on random S.
  [A2] AR(1) profile identities: KMS tridiagonal R^-1 (R @ Rinv = I), |R| = (1-rho^2)^(p-1),
       sigma_hat^2(rho) = tr(R^-1 S)/p; the 1-D-profiled minimizer equals a full 2-D grid min.
  [A3] (MUST-HAVE) spectrum-trace identity sum lambda = q_d + tr(RIV_perp) and min lambda >= 1
       on the ACTUAL CS / AR1 G_k, with I_com = MVN closed form and I_obs the MVN observed-info
       at real missingness patterns (so I_mis = I_com - I_obs is genuinely PSD); plus a
       FINITE-DIFFERENCE check of every G_k column against the duplication-matrix vech convention
       (the silent-failure class the engine depends on).
  [A5] equal-KL Toeplitz money cell: KL(truth||CS*) = KL(truth||AR1*) at w* (cell B residual).

Run:    py verification/cas-wolfram/verify_w4_nonnested.py
Exit:   0 all pass; 1 mismatch.
"""
import sys

import numpy as np

FAIL = 0
P = 4
K = P + P * (P + 1) // 2   # 14
RNG = np.random.default_rng(20260604)


def check(name, ok, detail=""):
    global FAIL
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAIL = 1
    print(f"  [{tag}] {name}" + (f"   {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# vech / duplication / MVN information -- numpy ports matching 00-setup.R exactly
# (column-major lower triangle).
# ---------------------------------------------------------------------------
def vech(M):
    p = M.shape[0]
    return np.array([M[i, j] for j in range(p) for i in range(j, p)])


def duplication_matrix(p):
    k = p * (p + 1) // 2
    D = np.zeros((p * p, k))
    count = 0
    for j in range(p):
        for i in range(j, p):
            D[j * p + i, count] = 1.0
            if i != j:
                D[i * p + j, count] = 1.0
            count += 1
    return D


def vech_index_table(p):
    idx = np.zeros((p, p), dtype=int)
    count = 0
    for j in range(p):
        for i in range(j, p):
            idx[i, j] = count
            idx[j, i] = count
            count += 1
    return idx


DP = duplication_matrix(P)
VIDX = vech_index_table(P)


def I_com_mvn(Sigma, N):
    Si = np.linalg.inv(Sigma)
    I = np.zeros((K, K))
    I[:P, :P] = N * Si
    I[P:, P:] = (N / 2.0) * DP.T @ np.kron(Si, Si) @ DP
    return I


def I_obs_mvn(Sigma, patterns):
    """Expected MVN observed info summed over (pattern, count); pattern = boolean
    'observed' mask of length p. Mirrors fisher_info_obs_mvn in 00-setup.R."""
    I = np.zeros((K, K))
    for mask, n_pat in patterns:
        Oi = [a for a in range(P) if mask[a]]
        q = len(Oi)
        if q == 0:
            continue
        Soo = Sigma[np.ix_(Oi, Oi)]
        Soo_inv = np.linalg.inv(Soo)
        for a in range(q):
            for b in range(q):
                I[Oi[a], Oi[b]] += n_pat * Soo_inv[a, b]
        Dq = duplication_matrix(q)
        Isub = 0.5 * Dq.T @ np.kron(Soo_inv, Soo_inv) @ Dq
        full = [P + VIDX[Oi[a], Oi[b]] for b in range(q) for a in range(b, q)]
        for a in range(len(full)):
            for b in range(len(full)):
                I[full[a], full[b]] += n_pat * Isub[a, b]
    return I


# ---------------------------------------------------------------------------
# candidate covariance + analytic Jacobians
# ---------------------------------------------------------------------------
Jm = np.ones((P, P))
Im = np.eye(P)
Qm = Im - Jm / P


def cs_Sigma(s2, rho):
    return s2 * ((1 - rho) * Im + rho * Jm)


def ar1_R(rho):
    idx = np.abs(np.subtract.outer(np.arange(P), np.arange(P)))
    return rho ** idx


def ar1_dR(rho):
    d = np.abs(np.subtract.outer(np.arange(P), np.arange(P)))
    out = np.zeros((P, P))
    for i in range(P):
        for j in range(P):
            if d[i, j] != 0:
                out[i, j] = d[i, j] * rho ** (d[i, j] - 1)
    return out


def jac_cs(s2, rho):
    G = np.zeros((K, 6))
    G[:P, :P] = np.eye(P)
    G[P:, 4] = vech((1 - rho) * Im + rho * Jm)   # dSigma/ds2
    G[P:, 5] = vech(s2 * (Jm - Im))              # dSigma/drho
    return G


def jac_ar1(s2, rho):
    G = np.zeros((K, 6))
    G[:P, :P] = np.eye(P)
    G[P:, 4] = vech(ar1_R(rho))                  # dSigma/ds2
    G[P:, 5] = vech(s2 * ar1_dR(rho))            # dSigma/drho
    return G


def qbar_dev(Sigma, S):
    return np.log(np.linalg.det(Sigma)) + np.trace(np.linalg.solve(Sigma, S))


def cs_project(S):
    a = np.ones(P) @ S @ np.ones(P) / P
    b = np.trace(Qm @ S) / (P - 1)
    s2 = (a + (P - 1) * b) / P
    rho = (a - b) / (a + (P - 1) * b)
    return s2, rho


def ar1_profile_fit(S):
    grid = np.linspace(-0.97, 0.97, 1941)
    best = None
    for rho in grid:
        Rinv = np.linalg.inv(ar1_R(rho))
        s2 = np.trace(Rinv @ S) / P
        g = P * np.log(s2) + (P - 1) * np.log(1 - rho ** 2)
        if best is None or g < best[0]:
            best = (g, s2, rho)
    return best[1], best[2]


def kl_mvn(St, Sk):
    return 0.5 * (np.log(np.linalg.det(Sk) / np.linalg.det(St))
                  + np.trace(np.linalg.solve(Sk, St)) - P)


# ---------------------------------------------------------------------------
# [A1] CS closed form = exact minimizer of the Qbar deviance over the CS family
# ---------------------------------------------------------------------------
print("[A1] CS closed-form pseudo-true is the exact constrained maximizer")
Sigma_A = ar1_R(0.5)                            # cell A truth
tau_B = np.array([1.0, 0.473555, 0.355782, 0.296895])
Sigma_B = np.array([[tau_B[abs(i - j)] for j in range(P)] for i in range(P)])
test_S = [Sigma_A, Sigma_B]
for _ in range(6):
    Qr = RNG.normal(size=(P, P))
    test_S.append(Qr @ Qr.T + P * Im)
max_grad = 0.0
all_min = True
for S in test_S:
    s2, rho = cs_project(S)
    h = 1e-6
    g_s2 = (qbar_dev(cs_Sigma(s2 + h, rho), S) - qbar_dev(cs_Sigma(s2 - h, rho), S)) / (2 * h)
    g_rho = (qbar_dev(cs_Sigma(s2, rho + h), S) - qbar_dev(cs_Sigma(s2, rho - h), S)) / (2 * h)
    max_grad = max(max_grad, abs(g_s2), abs(g_rho))
    f0 = qbar_dev(cs_Sigma(s2, rho), S)
    for ds, dr in [(1e-3, 0), (-1e-3, 0), (0, 1e-3), (0, -1e-3)]:
        if qbar_dev(cs_Sigma(s2 + ds, rho + dr), S) < f0 - 1e-9:
            all_min = False
    # recovery identity: a = s2(1+(p-1)rho), b = s2(1-rho) reproduce the projections
    a = np.ones(P) @ S @ np.ones(P) / P
    b = np.trace(Qm @ S) / (P - 1)
    if abs(s2 * (1 + (P - 1) * rho) - a) > 1e-10 or abs(s2 * (1 - rho) - b) > 1e-10:
        all_min = False
check("CS closed form: zero Qbar-deviance gradient on 8 targets (frozen + random)",
      max_grad < 1e-4, f"max|grad| = {max_grad:.2e}")
check("CS closed form: local minimum + (sigma^2,rho)<->(a,b) recovery identity", all_min)

# ---------------------------------------------------------------------------
# [A2] AR(1) profile identities
# ---------------------------------------------------------------------------
print("[A2] AR(1) KMS inverse, determinant, profiled scale, profile vs full grid")
ok_kms = True
ok_det = True
for rho in (-0.7, -0.3, 0.2, 0.5, 0.8):
    R = ar1_R(rho)
    Rinv = np.linalg.inv(R)
    c = 1.0 / (1 - rho ** 2)
    kms = np.zeros((P, P))
    for i in range(P):
        kms[i, i] = c * (1.0 if i in (0, P - 1) else (1 + rho ** 2))
    for i in range(P - 1):
        kms[i, i + 1] = kms[i + 1, i] = -c * rho
    if np.max(np.abs(kms - Rinv)) > 1e-9:
        ok_kms = False
    if abs(np.linalg.det(R) - (1 - rho ** 2) ** (P - 1)) > 1e-9:
        ok_det = False
check("KMS tridiagonal R^-1 matches solve(R) on 5 rho", ok_kms)
check("|R(rho)| = (1-rho^2)^(p-1) on 5 rho", ok_det)
# profile vs full 2-D grid minimizer of qbar_dev = p log s2 + (p-1) log(1-rho^2) + (1/s2)tr(R^-1 S)
# (correlation-scale targets -- the candidates live on correlation data; arbitrary high-scale
# random S would push the AR(1) optimal s2 outside any fixed grid).
ar1_test_S = [Sigma_A, Sigma_B, ar1_R(0.3), ar1_R(-0.5), cs_Sigma(1.0, 0.4)]
ok_prof = True
for S in ar1_test_S:
    s2p, rhop = ar1_profile_fit(S)
    scale = np.trace(S) / P
    best = None
    for rho in np.linspace(-0.95, 0.95, 381):
        for s2 in np.linspace(0.2 * scale, 3.0 * scale, 561):
            f = qbar_dev(s2 * ar1_R(rho), S)
            if best is None or f < best[0]:
                best = (f, s2, rho)
    if abs(rhop - best[2]) > 0.02 or abs(s2p - best[1]) > 0.03 * scale:
        ok_prof = False
check("profiled AR(1) minimizer agrees with full 2-D grid (rho tol .02)", ok_prof)

# ---------------------------------------------------------------------------
# [A3] general-Jacobian spectrum-trace identity on the ACTUAL CS / AR1 G_k
#      + finite-difference Jacobian check (the vech-convention silent-failure guard)
# ---------------------------------------------------------------------------
print("[A3] curved-G_k: sum lambda == q_d + tr(RIV_perp), min lambda >= 1; G_k finite-diff")
# a handful of realistic missingness pattern sets (X1-heavy + others)
patt_sets = [
    [((False, True, True, True), 70), ((True, True, True, True), 30)],     # X1 ~70% missing
    [((False, True, True, True), 50), ((True, False, True, True), 20),
     ((True, True, True, True), 30)],
    [((True, True, False, True), 40), ((True, True, True, False), 40),
     ((True, True, True, True), 20)],
]
q_d = K - 6
max_gap = 0.0
min_w = np.inf
ok_a3 = True
for (name, jac, s2, rho) in [("CS", jac_cs, 1.3, 0.35), ("CS", jac_cs, 0.8, -0.2),
                             ("AR1", jac_ar1, 1.0, 0.5), ("AR1", jac_ar1, 1.5, 0.62)]:
    Sigma = cs_Sigma(s2, rho) if name == "CS" else s2 * ar1_R(rho)
    Icom = I_com_mvn(Sigma, 500)
    for patt in patt_sets:
        Iobs = I_obs_mvn(Sigma, patt)
        Imis = Icom - Iobs
        if np.min(np.linalg.eigvalsh((Iobs + Iobs.T) / 2)) < 1e-8:
            continue
        if np.min(np.linalg.eigvalsh((Imis + Imis.T) / 2)) < -1e-8:
            ok_a3 = False
        G = jac(s2, rho)
        GtIG = G.T @ Icom @ G
        tr_full = np.trace(np.linalg.solve(Iobs, Imis))
        tr_proj = np.trace(np.linalg.solve(GtIG, G.T @ Icom @ np.linalg.solve(Iobs, Imis) @ G))
        tr_perp = tr_full - tr_proj
        A = np.linalg.inv(Icom) - G @ np.linalg.solve(GtIG, G.T)
        V = Icom @ np.linalg.solve(Iobs, Icom)
        w, U = np.linalg.eigh((V + V.T) / 2)
        Vh = U @ np.diag(np.sqrt(np.maximum(w, 0))) @ U.T
        lam = np.sort(np.linalg.eigvalsh(Vh @ ((A + A.T) / 2) @ Vh))[::-1][:q_d]
        gap = abs(lam.sum() - (q_d + tr_perp)) / max(1.0, q_d + tr_perp)
        max_gap = max(max_gap, gap)
        min_w = min(min_w, lam.min())
        if gap > 1e-7 or lam.min() < 1 - 1e-7:
            ok_a3 = False
check(f"curved-G spectrum identity (q_d={q_d}) on CS & AR1 x 3 pattern sets",
      ok_a3 and max_gap <= 1e-7, f"max rel gap = {max_gap:.2e}")
check("curved-G null-law weights min lambda >= 1", min_w >= 1 - 1e-7, f"min = {min_w:.8f}")
# finite-difference Jacobian (vech convention)
hh = 1e-6
ok_fd = True
max_fd = 0.0
for (jac, sig_fun, s2, rho) in [(jac_cs, cs_Sigma, 1.2, 0.3),
                                (jac_ar1, lambda a, b: a * ar1_R(b), 1.0, 0.45)]:
    G = jac(s2, rho)
    fd_s2 = vech((sig_fun(s2 + hh, rho) - sig_fun(s2 - hh, rho)) / (2 * hh))
    fd_rho = vech((sig_fun(s2, rho + hh) - sig_fun(s2, rho - hh)) / (2 * hh))
    max_fd = max(max_fd, np.max(np.abs(G[P:, 4] - fd_s2)), np.max(np.abs(G[P:, 5] - fd_rho)))
    if not np.allclose(G[:P, :P], np.eye(P)) or np.any(G[:P, 4:] != 0) or np.any(G[P:, :P] != 0):
        ok_fd = False
check("G_k analytic columns match finite differences (vech order)",
      ok_fd and max_fd < 1e-5, f"max|dG| = {max_fd:.2e}")

# ---------------------------------------------------------------------------
# [A5] equal-KL Toeplitz money cell (cell B)
# ---------------------------------------------------------------------------
print("[A5] cell B equal-KL: KL(truth||CS*) == KL(truth||AR1*)")
s2c, rc = cs_project(Sigma_B)
s2a, ra = ar1_profile_fit(Sigma_B)
kl_cs = kl_mvn(Sigma_B, cs_Sigma(s2c, rc))
kl_ar = kl_mvn(Sigma_B, s2a * ar1_R(ra))
check("cell B KL gap < 5e-4 (coin flip)", abs(kl_cs - kl_ar) < 5e-4,
      f"KL_CS={kl_cs:.6f} KL_AR1={kl_ar:.6f} gap={kl_cs - kl_ar:+.2e}")
check("cell B pseudo-true rho away from 0 (Vuong)", min(abs(rc), abs(ra)) > 0.15,
      f"rho_CS={rc:.4f} rho_AR1={ra:.4f}")

print()
if FAIL:
    print("RESULT: FAIL")
    sys.exit(1)
print("RESULT: ALL PASS")
sys.exit(0)
