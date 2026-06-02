# Todo 015 — Reconcile the Layer-3 (GPT-5.5) conjectures against evidence

**Status:** C1 + C3 **CONFIRMED and applied** to `manuscript/derivation.qmd` (2026-06-01); C2
**CONFIRMED and reconciled** (2026-06-02, `todo/017`); C4 untouched. See the Resolution log
below. These were **conjectures** raised by the cross-model adversarial check (Layer 3 of
`todo/013`); each needed reconciliation + evidence before any derivation change.

## Resolution log (2026-06-01)

Built + ran the known-variance adjudicating experiment (`verification/rederivation-knownvar.R`;
N=200/800, R up to 2e5, 20 cores). Evidence:
`verification/cache/rederivation-knownvar-results-2026-06-01.md`.

- **C1 (non-universality) — CONFIRMED.** Known-variance (mean-only) `E[T] ≈ 0` (FIML) /
  `−½tr(RIV)` (proper); **neither is `+½tr(RIV)`**. Tightest run (N=200, R=2e5):
  `E[A_fiml]/½trRIV=1.04`, `E[T_fiml]≈0`, `E[T_proper]/(−½trRIV)=0.96`, `E[B]/(−½trRIV)=0.997`.
  Also derived analytically (matches the manuscript's own A3 pieces): with a known scale `α=0` so
  `(A)=0`, but `H_φφ=−I_mis|obs` (Isserlis) so `(C)=−½tr(RIV)` survives uncancelled **even under
  MCAR**, halving `E[A]` to `½tr(RIV)`. **Applied:** theorem (`@sec-thm`) + intro
  (`@sec-intro-result`) + Tier B (`@sec-verify-tierB`) + A5 now scope the headline to models that
  estimate a scale/covariance; new "Scope" callout after the theorem states the condition,
  mechanism, evidence, and confirms the IC application (`@sec-intro-why`, estimated Σ) is in-regime.
- **C3 (FIML ≠ proper) — CONFIRMED.** FIML and proper differ by **exactly** `C_n = ½tr(RIV)`
  (ratio 1.000, SE 2e-4), validated analytically + by a built-in MC spot-check of the analytic
  proper `barQ`. **Applied:** scope callout + softened the `00-setup.R` `barQ_fiml_analytic`
  "same prediction as MI" comment.
- **C2 (Δ_n entropy reframing) — CONFIRMED and reconciled (2026-06-02), not adopted as primary.**
  The full symbolic identity `Δ_n = ½tr(RIV)+(A)+(C)` (hence `E[T]=Δ_n`) is proved via the
  entropy-Hessian split `∇²C_n=H_φ+I_mis|obs` and confirmed by two CAS + MC (paired
  `E[T_fitted−Δ_n]≈0`; known-var `Δ_n=0`). `H_φφ=−I_mis|obs` is now a corollary of the split's μ-block.
  **Kept `+½tr(RIV)` as the headline** (author intent); added a one-paragraph reconciliation remark to
  `derivation.qmd` (after `@sec-combine`). C2b settled (no θ-free floating constant for normalized
  unknown-Σ MVN ⟹ `T` convention-free). Closed in `todo/017`;
  evidence `verification/cache/c2-deltan-derivation-2026-06-02.md`.
- **C4 (BvM / self-efficiency assumptions) — UNTOUCHED.** Not addressed this session; still open
  (see below). Independent of C1/C3.

Original conjecture text retained below for provenance.

---

## Where the headline stands after Layers 0–3

- **Solid (do not re-litigate):** `E[B] = E[ℓ_com(θ̂_obs) − ℓ_com(θ̂_com)] = −½tr(RIV)` with
  `Var(θ̂_obs−θ̂_com)=I_obs⁻¹−I_com⁻¹` and `Cov(θ̂_obs,θ̂_com)=I_com⁻¹` — triangulated by 9/9 blind
  Claude routes, the Wolfram/SymPy CAS, the MC experiment, **and** GPT-5.5. The `θ̂_com`-as-target
  premise is bulletproof.
- **Fixed + independently validated:** the D9 fitted-vs-oracle ambiguity (committed `6bc7206`).
  GPT-5.5 spontaneously flagged the same tower-property trap.
- **In question (this file):** the *universality* and the *`+tr/−½tr` decomposition* of the
  `+½tr(RIV)` headline.

Evidence base already collected:
- `verification/rederivation-L0-fitted-vs-oracle.R` (N=200, R=4000): unknown-(μ,Σ) MVN, FIML →
  `E[A]/trRIV≈1.09`, `E[T]/(½trRIV)≈0.985`; oracle → `E[A]≈0`, `E[T]≈−½trRIV`.
- W1 caches: FIML `Ahat/trRIV≈0.71–1.15`, `That/trRIV≈0.16–0.55`; Amelia (proper) `Ahat/trRIV≈0.95`,
  `That/trRIV≈0.42`.
- Hand-calc (known-variance univariate, fully-missing units): FIML `E[A]=½tr(RIV)`, `E[T]=0`;
  proper `E[A]=0`, `E[T]=−½tr(RIV)`. GPT-5.5 reproduces both.
- GPT-5.5 raw: `verification/cache/layer3-gpt-5.5-mode{A,B}.md`. Results log:
  `verification/cache/rederivation-L0-L2-results-2026-06-01.md` (Layer-3 section).

---

## Conjecture C1 (DECISIVE, testable) — Non-universality of `+½tr(RIV)`

**Claim.** `E[T]=+½tr(RIV)` is **not** universal over regular likelihoods. It holds when the
*conditional entropy* `H_θ(Y_mis|Y_obs)` depends on the estimated parameters (i.e. covariance is
estimated). For **known-variance / mean-only** models the conditional entropy is θ-free and
`E[T]=0` (deterministic FIML) or `−½tr(RIV)` (proper MI) — **not** `+½tr(RIV)`. Hence the manuscript
theorem's "`+½tr(RIV)` for *any* regular likelihood fit on congenially imputed data" is an overreach.

**Evidence so far.** Hand-calc + GPT-5.5 agree on the known-variance values. The unknown-Σ MVN
(`+½tr(RIV)`) is confirmed by the MC experiment. The two regimes genuinely differ.

**Decisive check (build this).** A clean known-variance simulation (see "Adjudicating experiment"
below). **Prediction:** `E[A]→½tr(RIV)` (FIML) / `0` (proper); `E[B]→−½tr(RIV)`; `E[T]→0` (FIML) /
`−½tr(RIV)` (proper) — and crucially NOT `+½tr(RIV)`.

**If it pans out → derivation update.** Restate the Theorem (`@sec-thm`) and intro (`@sec-intro-result`)
scope: the `+½tr(RIV)` holds for models whose **conditional (missing-data) entropy depends on the
estimated parameters** — concretely, covariance/scale estimation — and is the conditional-entropy
plug-in bias `Δ_n`, which vanishes for mean-only/known-scale fits. Check the **IC application (§5 / W3)**
explicitly lives in the estimated-covariance regime (it does: MI-AIC/BIC over MVN models with
estimated Σ), so the headline empirical claim survives; the *general* phrasing does not.

---

## Conjecture C2 (analytical) — The `Δ_n` reframing / the `½+½` cancellation

**Claim.** The cleanest statement is `E[T]=Δ_n`, the conditional-entropy plug-in bias
`Δ_n = E[C_n(θ̂_obs) − C_n(θ_0)]`, `C_n(θ)=Σ_i E_θ[log p(Y_mis,i|Y_obs,i,θ)|Y_obs,i]`. GPT-5.5's
decomposition is `E[A] = ½tr(RIV) [KL term] + Δ_n`, `E[B] = −½tr(RIV)`, so the two `½tr(RIV)` halves
**cancel** and the manuscript's "`+tr(RIV)` imputation / `−½tr(RIV)` estimation" split is a *different*
(and convention-dependent) bookkeeping of the same total. Reconciliation requires
`Δ_n = ½tr(RIV) + (A)+(C)` for the unknown-Σ MVN.

**To reconcile.** Show analytically (SymPy/Wolfram or by hand) whether, for the unknown-(μ,Σ) MVN,
the log-determinant entropy bias `Δ_n = −½ E Σ_i log(|Σ̂_{mis|obs,i}|/|Σ_{0,mis|obs,i}|)` equals
`½tr(RIV) + (A)+(C)` to leading order. If yes, the two decompositions are equivalent and we can
**choose** the clearer exposition. If no, one of them is wrong — investigate which.

**Convention-dependence sub-point (C2b).** GPT-5.5 shows `E[A]=+tr(RIV)` is not invariant to θ-free,
Y-dependent additive constants in `ℓ_com` (e.g. the `−½Σy²` term for known-variance Gaussian). For
the **full normalized MVN density with unknown Σ** the y-quadratic is θ-dependent (via `Σ⁻¹`), so
arguably no floating constant exists and `T` is well-defined — **verify this** and state it, so the
result is manifestly convention-free in the paper's setting. Document the known-variance subtlety.

**If it pans out → derivation update.** Consider presenting `E[T]=Δ_n` (conditional-entropy plug-in
bias) as the primary, model-agnostic statement, with `+½tr(RIV)` as its evaluation for estimated-Σ
MVN — this is *more* general and pre-empts C1/C2b simultaneously. Decide whether to keep the
`+tr/−½tr` split as a heuristic (with the convention noted) or demote it.

---

## Conjecture C3 (testable) — Deterministic FIML ≠ proper MI in general

**Claim.** `barQ_fiml_analytic` (deterministic E-step at `θ̂_obs`) and genuine proper MI
(posterior-draw `φ̃`) give **different** `E[A]`/`E[T]` in general. Known-variance: FIML `E[T]=0` vs
proper `E[T]=−½tr(RIV)`. The D9 margin's "`[mc]` equal to this construction" and the
`00-setup.R` comment ("same prediction as MI") may be too strong.

**Evidence so far.** Hand-calc shows they differ for known-variance. For unknown-Σ the MC numbers are
close but not identical (FIML `That/trRIV≈0.55` vs Amelia `≈0.42` at N=200 — could be MCSE or a real
gap from the proper-draw `(C)`-term).

**Decisive check.** In the known-variance experiment, run **both** FIML and proper arms and compare.
Also re-examine the unknown-Σ FIML-vs-Amelia gap with larger R. **Prediction:** they differ by the
posterior-draw variance contribution to the `(C)`/entropy term.

**If it pans out → derivation update.** Either (i) restrict the headline to the proper-MI object and
treat FIML as a *distinct* (deterministic) object with its own constant, or (ii) state explicitly the
regime where they coincide. Soften the D9 margin / `00-setup.R` comment accordingly.

---

## Conjecture C4 (assumptions) — Congeniality/properness as stated is insufficient

**Claim.** The Term-A cross-term `Cov(φ̃,θ̂_obs)=I_obs⁻¹` needs a **Bernstein–von Mises**
posterior-alignment condition `E_imp(φ̃|Y_obs)=θ̂_obs+o_p(n^{-1/2})`, and `T_∞=I_obs⁻¹` needs a
self-efficient/congenial setup — neither follows from "proper MI" (R5) alone. (`m→∞` only removes
Monte Carlo error.)

**To reconcile.** Check the ledger (R4–R7, L4) and the A5 step: is the BvM alignment already implied
by R4 (congeniality) + regularity, or is it a genuine extra assumption? Likely it should be stated.

**If it pans out → derivation update.** Add the BvM posterior-alignment condition explicitly to the
assumptions (near R4/R5 or L4) and cite it at A5; note self-efficiency (R6) is what gives
`T_∞=I_obs⁻¹` beyond properness.

---

## Adjudicating experiment (build in the new session)

A **known-variance** MVN simulation, Σ **fixed/known**, estimate the mean only. Mirror
`rederivation-L0-fitted-vs-oracle.R` but with known Σ:
- `θ̂_com` = complete-data mean MLE (Σ known) = column means of full `X`.
- `θ̂_obs` = observed-data mean MLE with known Σ (GLS / observed-score=0; closed form per pattern).
- `ℓ_com(μ;X)` = full normalized MVN log-density at known Σ.
- `Q̄(μ_eval; μ_imp)` = `E_imp[ℓ_com(μ_eval)]` with imputation conditional mean
  `μ_imp,M + Σ_MO Σ_OO⁻¹(y_O−μ_imp,O)`, conditional cov `Σ_MM·O` (known); **FIML arm** uses
  `μ_imp=θ̂_obs` (point), **proper arm** adds posterior draw `μ̃~N(θ̂_obs, I_obs⁻¹)`.
- Compute `A=Q̄(θ̂_obs;·)−ℓ_com(θ̂_obs)`, `B=ℓ_com(θ̂_obs)−ℓ_com(θ̂_com)`, `T=A+B`, `tr(RIV)`
  (μ-block only) per replicate; aggregate over R≈4000 with the 20-core cluster.
- Report ratios `E[A]/trRIV`, `E[B]/(−½trRIV)`, `E[T]/(½trRIV)` for FIML and proper.

**Predictions (if C1/C3 hold):** FIML `E[A]≈½trRIV`, `E[T]≈0`; proper `E[A]≈0`, `E[T]≈−½trRIV`;
both `E[B]≈−½trRIV`. Compare to the unknown-Σ baseline (`E[T]≈+½trRIV`).

## Decision gates

| Outcome | Reading | Action |
|---|---|---|
| known-var `E[T]≈0`/`−½` (not `+½`) | C1 confirmed: non-universal | restate theorem scope (estimated-entropy regime); verify IC app lives there |
| known-var `E[T]≈+½trRIV` | C1 refuted: headline universal after all | GPT-5.5 wrong on known-var; close C1, keep universal claim, document why |
| `Δ_n = ½trRIV+(A)+(C)` analytically | C2 confirmed | optionally adopt `E[T]=Δ_n` as primary statement |
| FIML vs proper differ materially | C3 confirmed | restrict to proper object / soften `[mc] equal` claims |

## Files & pointers

- Update targets: `manuscript/derivation.qmd` — `@sec-intro-result`, Theorem `@sec-thm`, Term A
  `@sec-termA` (A3–A5), the ledger (R4–R7, L4) for C4. **No edits until a conjecture is confirmed.**
- Evidence: `verification/cache/rederivation-L0-L2-results-2026-06-01.md`,
  `verification/cache/layer3-gpt-5.5-mode{A,B}.md`, `verification/rederivation-L0-fitted-vs-oracle.R`.
- New experiment: `verification/rederivation-knownvar.R` (to be written).
- Memory: `[[project_fitted_vs_oracle_sign]]`.

## Resume prompt for the new session

> Resume mi-spectral `todo/015-chat-conjectures-reconciliation.md`. Build the known-variance
> adjudicating experiment (`verification/rederivation-knownvar.R`) and run it (20 cores, R≈4000) to
> test Conjecture C1 (non-universality) and C3 (FIML vs proper). Then reconcile C2 (the `Δ_n`
> entropy reframing) analytically. Use the decision gates in this file; only edit
> `manuscript/derivation.qmd` for a conjecture that is confirmed by evidence. The `−½` Term B and the
> D9 fix are settled — don't re-litigate. Context in the file's "Where the headline stands" section.
