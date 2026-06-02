# Todo 017 — C2: reconcile the `Δ_n` conditional-entropy framing with the `(A)+(C)` decomposition

**Status: CLOSED — CONFIRMED (2026-06-02).** The identity holds; `+½tr(RIV)` kept as headline (author
intent); a one-paragraph reconciliation remark added to `manuscript/derivation.qmd` (collapsed callout
after `@sec-combine`). Continuation of conjecture **C2** in `todo/015` (C1+C3+C4 closed).

## Resolution log (2026-06-02)

**`E[T] = Δ_n` and `Δ_n = ½tr(RIV) + (A)+(C)` — CONFIRMED**, two CAS (exact, symbolic) + MC.

- **The proof** is the entropy-Hessian split `∇²C_n(θ₀) = H_φ + I_mis|obs` (chain rule on
  `C_n(θ)=F(θ,θ)`, `F(φ,ψ)=E_{Y_mis~φ}[log p(Y_mis|Y_obs,ψ)]`: sampling-slot Hessian `H_φ`,
  eval-slot `−I_mis|obs`, mixed `+I_mis|obs` by Bartlett) together with `∇C_n(θ₀)=α`. Taylor-expanding
  `Δ_n` sends 1st order → `(A)=αᵀE[δ]`, 2nd order → `½tr(H_φ I_obs⁻¹)+½tr(RIV) = (C)+½tr(RIV)`. So
  `Δ_n = ½tr(RIV)+(A)+(C)`, and since `E[T]=½tr(RIV)+(A)+(C)` (@eq-combine), `E[T]=Δ_n`. Full write-up:
  `verification/cache/c2-deltan-derivation-2026-06-02.md`.
- **CAS.** `verify_term_ac.py` (Wolfram) + `verify_term_ac_sympy.py` (SymPy): (I1) `∇C_n=α`, α
  covariance-only; (I2) the split; Bartlett; Isserlis mu-block; scalar `Δ_n−[½tr(RIV)+(A)+(C)]=0` —
  all `→0`, symbolic in `x`, full 5-param natural `(μ,Σ)`.
- **MC.** `rederivation-L0-fitted-vs-oracle.R` (R=4000): paired `E[T_fitted−Δ_n] = +0.013 (SE .126)`
  at N=200, `+0.271 (SE .255)` at N=800; `E[Δ_n]/(½trRIV) = 0.980/0.989`. `E[Δ_n]` is cleaner than
  `E[T_fitted]` and pins `½tr(RIV)+(A)+(C)`.
- **Boundary anchor.** `rederivation-knownvar.R`: `E[Δ_n]=0` exactly (C_n is Σ-free for known scale).
  The known-scale Isserlis identity `H_φφ=−I_mis|obs` is now a *corollary* of (I2)'s μ-block, unifying
  the Scope callout (C1) and the `(A)+(C)` story.
- **C2b (convention-free) — settled.** The full normalized unknown-Σ MVN density has no θ-free,
  `Y_mis`-dependent additive constant (every `Y`-quadratic carries `Σ⁻¹`), so `T` is well-defined and
  convention-free. The known-variance kernel `−½σ⁻²Σy²` is the contrast (θ-free + `Y`-dependent), whose
  inclusion shifts `E[A]` by the entropy term — the same `Δ_n=0` boundary.

Original plan retained below for provenance.

---

**Optional** — the `+½tr(RIV)` headline does not depend on this; it is a unification
that would pre-empt a referee asking whether the manuscript's `+tr/−½tr` split is the same object as
the entropy-bias story.

## Goal

Prove (or refute) analytically that, for the unknown-`(μ,Σ)` MVN, the net Q-function bias equals the
**conditional-entropy plug-in bias** `Δ_n`, and that `Δ_n` is exactly the manuscript's
`½tr(RIV)+(A)+(C)` to leading order. If it holds, the manuscript's `(A)/(B-main)/(C)` decomposition
and GPT-5.5's `½tr(RIV)[KL]+Δ_n[entropy]` decomposition are the *same total*, differently grouped —
and we can **choose** the clearer exposition.

Definitions:
- `C_n(θ) = Σ_i E_θ[ log p(Y_mis,i | Y_obs,i, θ) | Y_obs,i ]` (per-unit conditional log-density,
  averaged under θ). For the MVN this is `−½ Σ_i [ |M_i| log 2πe + log|Σ_{M|O,i}(θ)| ]` up to the
  conditional-mean quadratic, i.e. essentially the (negative) **conditional entropy**.
- `Δ_n = E[ C_n(θ̂_obs) − C_n(θ0) ]` (the plug-in bias from evaluating the conditional entropy at the
  estimate vs the truth).
- **Target identity:** `E[T] = Δ_n` and `Δ_n = ½tr(RIV) + (A)+(C) + O(n^{-1})` for unknown-Σ MVN.

## What is already nailed (warm context — do not re-derive)

- **Known-variance anchor (C1/C3, `verification/rederivation-knownvar.R`, committed):**
  `E[A_fiml]=½tr(RIV)`, `E[T_fiml]=0`, proper differs by `C_n=½tr(RIV)`, `E[B]=−½tr(RIV)`. Confirmed by
  MC (R=2e5) **and** by hand.
- **The regime mechanism, proven both ways.** Apply the manuscript's own A3 pieces to a *known* scale:
  the entropy gradient `α=−E'(θ0)` is supported only on the (co)variance parameters (`α_μ=0`,
  `α_Σ≠0` — the A3 warning callout), so `(A)=E[δᵀα]=0`. The cross-entropy curvature for a **fixed**
  conditional covariance `V` is `H_φφ = −I_mis|obs` (Isserlis: for `ε~N(0,V)`,
  `E[εᵀV⁻¹ε (εεᵀ−V)] = 2V`), so `(C)=½tr(H_φφ I_obs⁻¹) = −½tr(RIV)` **survives even under MCAR**.
  Hence `E[A]=tr(RIV)+0−½tr(RIV)=½tr(RIV)` for known scale — matching the experiment. The
  `½tr(RIV)` that the headline gains when Σ *is* estimated is exactly the entropy contribution `Δ_n`.
  (This is the boundary value: `Δ_n=0` known-scale, `Δ_n=½tr(RIV)+(A)+(C)` estimated-Σ.)
- **`(A)+(C)` itself** is already derived/verified for the bivariate monotone and non-monotone MVN
  (`verification/term-a-mar-closedform.R`, `verification/cas-wolfram/verify_term_ac{,_nonmonotone}.py`).

## The analytic task (the actual work)

For the unknown-`(μ,Σ)` MVN, expand the conditional log-determinant entropy bias
`Δ_n = ½ Σ_i E[ log|Σ̂_{M|O,i}| − log|Σ0_{M|O,i}| ]` to second order in `(θ̂_obs−θ0)` and show it equals
`½tr(RIV)+(A)+(C)`:
- First-order term ↔ pairs the MLE bias `E[δ]` with the entropy gradient → the `(A)` piece.
- Second-order term `½ E[δᵀ ∇²(½log|Σ_{M|O}|) δ] = ½ tr(∇²entropy · I_obs⁻¹)` → splits into the
  `½tr(RIV)` KL piece + the `(C)` curvature piece. Identify precisely which part is the intrinsic
  `½tr(RIV)` and which is the design-dependent `(C)`.
- Watch the **μ–Σ cross terms** under MAR (the observed score carries the mean–covariance cross term,
  @sec-riv / Appendix C).

**Convention sub-point (C2b) — verify and state.** GPT-5.5 noted `E[A]=+tr(RIV)` is not invariant to
θ-free, Y-dependent additive constants in `ℓ_com` (e.g. the `−½Σy²` term for a known-variance
Gaussian *kernel*). For the **full normalized MVN density with unknown Σ**, the y-quadratic is
θ-dependent (through `Σ⁻¹`), so no floating θ-free constant exists and `T` is well-defined /
convention-free. Confirm this explicitly so the paper's object is manifestly unambiguous; document the
known-variance kernel subtlety as the contrast.

## Verification path (two engines + MC, per project norm)

1. **CAS, bivariate.** Extend `verification/cas-wolfram/verify_term_ac.py` (already derives bivariate
   `(A)+(C)` from the Gaussian cross-entropy) to also form `Δ_n` (the conditional log-det entropy
   bias) and assert `Δ_n − [½tr(RIV)+(A)+(C)] = 0` symbolically. Mirror in the SymPy engine
   (`..._sympy.py`) for the two-CAS check.
2. **Monte-Carlo, unknown-Σ.** Add a `Δ_n` measurement per replicate to
   `verification/rederivation-L0-fitted-vs-oracle.R` (or a new `rederivation-deltan.R`): compute
   `C_n(θ̂_obs)` and `C_n(θ0)` from the conditional log-dets, and check `E[Δ_n] ≈ E[T_fitted] ≈
   ½tr(RIV)+(A)+(C)` at N=200/800, R≈4000, 20 cores. The known-variance script is the boundary
   sanity check (`Δ_n→0` there).

## Decision gate

| Outcome | Action |
|---|---|
| `Δ_n = ½tr(RIV)+(A)+(C)` (CAS + MC agree) | Decompositions equivalent. **Per author intent, keep `+½tr(RIV)` as headline** and add a one-paragraph reconciliation **remark** in `derivation.qmd` (near the Scope callout / `@sec-combine`): `E[T]` is the conditional-entropy plug-in bias `Δ_n`, evaluating to `½tr(RIV)+(A)+(C)` for estimated-Σ MVN and to `0`/`−½tr(RIV)` for known scale — unifying C1 and the `(A)+(C)` story. Do **not** promote `E[T]=Δ_n` to the primary statement unless the author opts in. |
| Identity fails | One decomposition is wrong. Re-derive `(A)+(C)` and `Δ_n` independently; the known-variance anchor (both give consistent values there) localizes the error. |

## Files & pointers

- Verify: `verification/cas-wolfram/verify_term_ac{,_sympy}.py` (extend); MC in
  `verification/rederivation-L0-fitted-vs-oracle.R` (extend) or new `rederivation-deltan.R`.
- Manuscript target (only if confirmed): `manuscript/derivation.qmd` — reconciliation remark near the
  "Scope" callout (after `@sec-thm`) and/or `@sec-combine`; optional note in `@sec-termA` that
  `(A)+(C)` and `Δ_n` are one object decomposed two ways.
- Evidence: `verification/cache/`; the known-variance results
  `verification/cache/rederivation-knownvar-results-2026-06-01.md`.
- Memory: `[[project_fitted_vs_oracle_sign]]`.

## Resume prompt for the new session

> Resume mi-spectral `todo/017-c2-deltan-entropy-reconciliation.md` (conjecture C2). The known-variance
> result (C1/C3) is committed and closed; `Δ_n=0` there is the boundary anchor. Derive analytically
> whether, for the unknown-(μ,Σ) MVN, `E[T]=Δ_n` and `Δ_n=½tr(RIV)+(A)+(C)` — a second-order expansion
> of the conditional log-det entropy bias, verified by two CAS (extend `verify_term_ac.py`) + an MC
> measurement (extend the L0 script). Also settle C2b (the full normalized MVN density has no θ-free
> floating constant, so `T` is convention-free). Use the decision gate in the file; keep `+½tr(RIV)`
> as headline (author intent) and add only a reconciliation remark if it confirms. The `−½` Term B,
> the D9 fix, and the C1 scope restatement are settled — don't re-litigate.

*Draft 2026-06-01. Continues `todo/015-chat-conjectures-reconciliation.md` C2.*
