#!/usr/bin/env python
r"""Independent SymPy verification of the algebraic core behind the todo/040
cross-model audit (Claude Fable 5, max effort; `todo/040-audit-response-fable5.md`),
which resolves the DA-engine deviance-gap fork. The audit's master formula is

    D = -1/2 tr(RIV_mumu) - 1/2 sum_i tr(Vhat_i^-1 C_i b_Sigma C_i') - IMB,

D being the engine-vs-FITTED Q-gap barQ_engine(theta_obs) - barQ_fitted(theta_obs).
Two groups here, mirroring the derivation.qmd Appendix B convention: SymPy proves the
BOOKKEEPING (that the pieces assemble into the claimed closed forms), not the
underlying statistical facts (IW/Inv-Gamma posterior means, Fisher information) --
those are cited/standard and taken as inputs, exactly as Appendix B's "what SymPy
does not prove" scope note describes for the rest of the derivation.

  1. [lemma]   The four building blocks of Sec. 2 of the audit response, checked in
               one concrete-but-generic instantiation: p=3 variables, one unit with
               missing block M={1} and observed block O={2,3} (every Sigma/Delta
               entry left as a free symbol, so nothing is numerically special-cased).
                 L1  V'[Delta]  = C Delta C'                      (Schur envelope theorem)
                 L2  V''[D,D]   = -2 Bdot(D) Sigma_OO Bdot(D)'     (Schur concavity)
                 L3  the cancellation: under a pure-Sigma perturbation (mu fixed),
                     the exact per-unit identity's eps^2 coefficient equals
                     tr(W (r_O r_O' - Sigma_OO)),  W = Bdot(Delta)' Vhat^-1 Bdot(Delta)
                     -- the DIRECTIONAL (fixed-Delta) identity underlying the audit's
                     "cancels in expectation under MCAR" claim; the expectation-level
                     statement is measured, not algebraic, and lives in the R module
                     (verification/_modules/engine-gap-audit.R, diag_sigma_split()).
                 L4  C' Vhat^-1 C = Sigma^-1 - embed(Sigma_OO^-1)  (block-inverse identity)

  2. [toy-p1]  The univariate (p=1) closed-form engine-gap table promised in the
               todo/040 handoff. Toy: NO covariates, so "missing" means an entire
               unit's scalar value is unobserved (necessarily MCAR -- p=1 offers no
               auxiliary variable to condition a mechanism on). In this toy the mu-
               and sigma^2-blocks of RIV carry EQUAL missing information, so
               tr(RIV_mumu)/tr(RIV) = 1/2 exactly, which is what turns the Laplace/BvM
               engine's persistent term into exactly -1/4 (vs -0.101/tr(RIV) in the
               W1 cell, where the mu-share is only ~0.20). Verified in closed form:
                 tr(RIV_mumu)/tr(RIV)         = 1/2      (exact, all n_obs)
                 D_Laplace   / tr(RIV)        = -1/4     (exact, all n_obs)
                 D_Jeffreys(n_obs) / tr(RIV)  = -n_obs/(n_obs-3)  ->  -1  as n_obs -> oo
                 D_bootstrap / tr(RIV)        = 0        (exact, all n_obs -- the
                     complete-data second-moment identity of audit Sec. 4, checked
                     both as a symbolic per-resample parallel-axis identity and by
                     full enumeration of an n_obs=3 bootstrap distribution)

Run:    py verification/cas-wolfram/verify_engine_gap_sympy.py
Exit:   0 all pass; 1 a mismatch (investigate).
"""
import itertools
import sys

import sympy as sp


# =============================================================================
# Group 1 -- Section-2 lemmas, concrete p=3 (M={0}, O={1,2}) instantiation.
# =============================================================================

def build_p3():
    """Symbols for a generic 3x3 symmetric covariance Sigma and a symmetric
    perturbation Delta, split M={0} (zero-based) / O={1,2}."""
    s11, s12, s13, s22, s23, s33 = sp.symbols("s11 s12 s13 s22 s23 s33", real=True)
    Sigma = sp.Matrix([[s11, s12, s13], [s12, s22, s23], [s13, s23, s33]])
    d11, d12, d13, d22, d23, d33 = sp.symbols("d11 d12 d13 d22 d23 d33", real=True)
    Delta = sp.Matrix([[d11, d12, d13], [d12, d22, d23], [d13, d23, d33]])
    M, O = [0], [1, 2]
    return Sigma, Delta, M, O


def schur(Sig, M, O):
    """V(Sigma) = Sig_MM - Sig_MO Sig_OO^-1 Sig_OM, and B = Sig_MO Sig_OO^-1."""
    Soo = Sig.extract(O, O)
    Smo = Sig.extract(M, O)
    Som = Sig.extract(O, M)
    Smm = Sig.extract(M, M)
    B = Smo * Soo.inv()
    V = Smm - B * Som
    return V, B, Soo


def build_C(B0, M, O, p):
    """C = [I_M, -B] as a len(M) x p matrix (natural, non-permuted column order)."""
    C = sp.zeros(len(M), p)
    for a, ia in enumerate(M):
        C[a, ia] = 1
    for a in range(len(M)):
        for b in range(len(O)):
            C[a, O[b]] = -B0[a, b]
    return C


def embed(block, idx, p):
    """Embed a |idx|x|idx| block into a pxp zero matrix at rows/cols idx."""
    out = sp.zeros(p, p)
    for a, ia in enumerate(idx):
        for b, ib in enumerate(idx):
            out[ia, ib] = block[a, b]
    return out


def is_zero(expr):
    """True iff a scalar or every entry of a Matrix simplifies to 0."""
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(e) == 0 for e in expr)
    return sp.simplify(expr) == 0


def check_lemma1(Sigma, Delta, M, O):
    """L1: d/dt V(Sigma + t Delta)|_{t=0} == C Delta C'."""
    t = sp.symbols("t", real=True)
    p = Sigma.shape[0]
    V_t, _, _ = schur(Sigma + t * Delta, M, O)
    Vprime = sp.diff(V_t, t).subs(t, 0)
    _, B0, _ = schur(Sigma, M, O)
    C = build_C(B0, M, O, p)
    rhs = C * Delta * C.T
    return sp.simplify((Vprime - rhs)[0, 0])


def check_lemma2(Sigma, Delta, M, O):
    """L2: d^2/dt^2 V(Sigma + t Delta)|_{t=0} == -2 Bdot(Delta) Sigma_OO Bdot(Delta)',
    Bdot(Delta) = (Delta_MO - B Delta_OO) Sigma_OO^-1."""
    t = sp.symbols("t", real=True)
    V_t, _, _ = schur(Sigma + t * Delta, M, O)
    Vpp = sp.diff(V_t, t, 2).subs(t, 0)
    _, B0, Soo0 = schur(Sigma, M, O)
    Dmo = Delta.extract(M, O)
    Doo = Delta.extract(O, O)
    Bdot = (Dmo - B0 * Doo) * Soo0.inv()
    rhs = -2 * Bdot * Soo0 * Bdot.T
    return sp.simplify((Vpp - rhs)[0, 0])


def check_lemma3(Sigma, Delta, M, O):
    """L3 (the cancellation, directional form): under a pure Sigma perturbation (mu
    fixed), the exact per-unit identity mean_term(eps) + cov_term(eps) has an eps^2
    coefficient equal to tr(W (r_O r_O' - Sigma_OO)), W = Bdot(Delta)' Vhat^-1 Bdot(Delta),
    r_O a generic (symbolic) observed-block residual for one row.
      mean_term(eps) = d(eps)' Vhat^-1 d(eps),  d(eps) = [B(Sigma+eps Delta)-Bhat] r_O
      cov_term(eps)  = tr(Vhat^-1 (V(Sigma+eps Delta) - Vhat))
    """
    eps = sp.symbols("eps", real=True)
    rO = sp.Matrix(sp.symbols(f"rO0:{len(O)}", real=True))
    V0, B0, Soo0 = schur(Sigma, M, O)
    Vinv0 = V0.inv()
    Vt, Bt, _ = schur(Sigma + eps * Delta, M, O)
    d_eps = (Bt - B0) * rO
    mean_term = (d_eps.T * Vinv0 * d_eps)[0, 0]
    cov_term = sp.trace(Vinv0 * (Vt - V0))
    f = sp.expand(mean_term + cov_term)
    coeff2 = sp.diff(f, eps, 2).subs(eps, 0) / 2

    Dmo = Delta.extract(M, O)
    Doo = Delta.extract(O, O)
    Bdot = (Dmo - B0 * Doo) * Soo0.inv()
    W = Bdot.T * Vinv0 * Bdot
    rhs = sp.trace(W * (rO * rO.T - Soo0))
    return sp.simplify(coeff2 - rhs)


def check_lemma4(Sigma, M, O):
    """L4: C' Vhat^-1 C == Sigma^-1 - embed(Sigma_OO^-1)."""
    p = Sigma.shape[0]
    V0, B0, Soo0 = schur(Sigma, M, O)
    Vinv0 = V0.inv()
    C = build_C(B0, M, O, p)
    lhs = C.T * Vinv0 * C
    rhs = Sigma.inv() - embed(Soo0.inv(), O, p)
    return sp.simplify(lhs - rhs)


# =============================================================================
# Group 2 -- p=1 closed-form engine-gap toy table.
# =============================================================================

def toy_p1_table():
    """Univariate (p=1) MCAR entirely-missing-unit toy. nobs = n_obs (symbolic,
    > 3), r = n_mis/n_obs (fixed ratio, symbolic). theta_obs=(mu_hat, sigma2_hat) is
    the MLE fit to the n_obs observed scalars; n_mis units are imputed from the
    fitted marginal N(mu*, sigma2*) with NO conditioning (there is no second
    variable to regress on, so B == 0 and C == [1] identically for every missing
    unit -- the Schur/concavity apparatus of Group 1 is vacuous here by
    construction, not merely small)."""
    nobs, r, s2 = sp.symbols("nobs r sigma2", positive=True)

    # tr(RIV): mu- and sigma^2-blocks are Fisher-orthogonal for the normal, and
    # both scale as (n_obs+n_mis)/n_obs under complete-vs-observed information, so
    # they carry an IDENTICAL missing-information ratio -- the feature that makes
    # this toy's mu-share exactly 1/2 (vs ~0.20 in the paper's W1 cell).
    I_obs_mu, I_com_mu = nobs / s2, (nobs * (1 + r)) / s2
    I_obs_s2, I_com_s2 = nobs / (2 * s2 ** 2), (nobs * (1 + r)) / (2 * s2 ** 2)
    RIV_mu = sp.simplify(I_com_mu / I_obs_mu - 1)
    RIV_s2 = sp.simplify(I_com_s2 / I_obs_s2 - 1)
    tr_RIV = sp.simplify(RIV_mu + RIV_s2)
    ratio_mumu_resid = sp.simplify(RIV_mu / tr_RIV - sp.Rational(1, 2))

    n_mis = r * nobs

    # -- Laplace/BvM draw: theta* ~ N(theta_hat, I_obs^-1); Var(mu*) = s2/n_obs
    #    exactly; no Sigma-centering bias (mean-centered by construction), and the
    #    Sigma-only piece is identically 0 here (no B, so no Schur nonlinearity).
    Var_mu_laplace = s2 / nobs
    D_laplace = -sp.Rational(1, 2) * n_mis * Var_mu_laplace / s2
    D_laplace_resid = sp.simplify(D_laplace / tr_RIV - sp.Rational(-1, 4))

    # -- Jeffreys-IW draw: sigma2* | Y_obs ~ Inv-Gamma((nobs-1)/2, (nobs-1)S/2) with
    #    (nobs-1)S = nobs*s2 (same sum of squares), so E[sigma2*] = nobs s2/(nobs-3)
    #    EXACTLY (Schafer 1997; audit Sec. 2f's (p+2)/n leading-order constant, here
    #    exact rather than truncated -- p=1 gives divisor nobs-3, not an approximation).
    E_s2_star = nobs * s2 / (nobs - 3)
    b_sigma = E_s2_star - s2
    Var_mu_jeff = E_s2_star / nobs  # law of total variance, mu*|s2* ~ N(., s2*/nobs)
    D_jeff = -sp.Rational(1, 2) * n_mis * (b_sigma / s2 + Var_mu_jeff / s2)
    D_jeff_norm = sp.simplify(D_jeff / tr_RIV)
    D_jeff_closed_form_resid = sp.simplify(D_jeff_norm - (-nobs / (nobs - 3)))
    D_jeff_limit_resid = sp.simplify(sp.limit(D_jeff_norm, nobs, sp.oo) - (-1))

    return {
        "ratio_mumu_resid": ratio_mumu_resid,
        "D_laplace_resid": D_laplace_resid,
        "D_jeff_closed_form_resid": D_jeff_closed_form_resid,
        "D_jeff_limit_resid": D_jeff_limit_resid,
    }


def bootstrap_identity_check():
    """The mechanism behind 'bootstrap 0' (audit Sec. 4): for ANY n numbers z_1..z_n
    and ANY reference point m,
        (1/n) sum_j (z_j - m)^2  ==  sigma_tilde^2 + (mu_tilde - m)^2   (parallel axis)
    Checked symbolically for a generic n=3 resample. Then E*[Xi] = 0 (Xi = the
    bootstrap's b_Sigma piece plus its mu-wander piece) is checked by FULL
    enumeration of an n_obs=3 bootstrap distribution (27 equally likely resamples,
    exact rational arithmetic; the mechanism -- each resampled y*_j is marginally
    uniform over the n_obs original points -- does not depend on n_obs=3, but n=2
    is too degenerate to exercise it: every resample gives Xi=0 pointwise there, not
    just on average, so n_obs=3 is the smallest genuine check)."""
    z1, z2, z3, m = sp.symbols("z1 z2 z3 m", real=True)
    z = [z1, z2, z3]
    mu_t = sp.Rational(1, 3) * sum(z)
    sigma2_t = sp.Rational(1, 3) * sum((zj - mu_t) ** 2 for zj in z)
    lhs = sp.Rational(1, 3) * sum((zj - m) ** 2 for zj in z)
    rhs = sigma2_t + (mu_t - m) ** 2
    parallel_axis_residual = sp.simplify(sp.expand(lhs - rhs))

    y = [sp.Rational(3, 1), sp.Rational(-5, 2), sp.Rational(1, 1)]
    n_obs = len(y)
    mu_hat = sp.Rational(1, n_obs) * sum(y)
    s2_hat = sp.Rational(1, n_obs) * sum((yi - mu_hat) ** 2 for yi in y)
    total = sp.Integer(0)
    n_draws = 0
    for resample in itertools.product(y, repeat=n_obs):
        mu_s = sp.Rational(1, n_obs) * sum(resample)
        s2_s = sp.Rational(1, n_obs) * sum((v - mu_s) ** 2 for v in resample)
        xi = (s2_s - s2_hat) + (mu_s - mu_hat) ** 2
        total += xi
        n_draws += 1
    E_star_Xi = sp.simplify(total / n_draws)
    return parallel_axis_residual, E_star_Xi


# =============================================================================
# Drive.
# =============================================================================

def main():
    Sigma, Delta, M, O = build_p3()
    l1 = check_lemma1(Sigma, Delta, M, O)
    l2 = check_lemma2(Sigma, Delta, M, O)
    l3 = check_lemma3(Sigma, Delta, M, O)
    l4 = check_lemma4(Sigma, M, O)

    toy = toy_p1_table()
    parallel_axis_residual, E_star_Xi = bootstrap_identity_check()

    checks = [
        ("[lemma]  L1  V'[Delta] = C Delta C'                         == 0", l1),
        ("[lemma]  L2  V''[D,D] = -2 Bdot(D) Sigma_OO Bdot(D)'        == 0", l2),
        ("[lemma]  L3  cancellation: eps^2 coeff == tr(W(rOrO'-Soo))  == 0", l3),
        ("[lemma]  L4  C'Vhat^-1C = Sigma^-1 - embed(Sigma_OO^-1)     == 0", l4),
        ("[toy-p1] tr(RIV_mumu)/tr(RIV) == 1/2                        == 0", toy["ratio_mumu_resid"]),
        ("[toy-p1] D_Laplace/tr(RIV) == -1/4  (exact, all nobs)       == 0", toy["D_laplace_resid"]),
        ("[toy-p1] D_Jeffreys(nobs)/tr(RIV) == -nobs/(nobs-3) (exact) == 0", toy["D_jeff_closed_form_resid"]),
        ("[toy-p1] lim_{nobs->inf} D_Jeffreys/tr(RIV) == -1           == 0", toy["D_jeff_limit_resid"]),
        ("[toy-p1] bootstrap parallel-axis identity (symbolic, n=3)   == 0", parallel_axis_residual),
        ("[toy-p1] bootstrap E*[Xi] (enumerated n_obs=3, exact ratl.) == 0", E_star_Xi),
    ]

    ok = True
    for label, resid in checks:
        passed = is_zero(resid)
        ok = ok and passed
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        if not passed:
            print(f"       residual: {resid}")

    print("\nSymPy CAS:", "ALL CHECKS CONFIRMED" if ok
          else "MISMATCH -- investigate before trusting the derivation")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
