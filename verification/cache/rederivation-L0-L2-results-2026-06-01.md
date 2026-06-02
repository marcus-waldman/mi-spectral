# Independent re-derivation — Layer 0/1/2 results log (2026-06-01)

Execution of `todo/013-independent-rederivation-plan.md`. Free layers (0,1,2) run;
Layer-3 cross-model package assembled separately (`todo/013b-layer3-crossmodel-package.md`).

## Headline finding (run to ground)

The headline `E[T] = +½ tr(RIV)` is **correct for the operational MI Q-function**
(imputations drawn from the analyst's *fitted* model), confirmed empirically under
**both** deterministic FIML and proper Amelia. **But its sign is acutely sensitive to a
notational ambiguity in Definition D9** that the blind re-derivation exposed: written as
`Q̄_∞(θ) = E[ℓ_com(θ;Y) | Y_obs]` and read literally as the conditional expectation under
the *true* data law, `θ̂_obs`'s `Y_obs`-measurability makes Term A vanish by the tower
property and flips the headline to `−½ tr(RIV)`. **8 of 9 independent blind solvers took
exactly this (oracle) reading and derived the opposite sign.** This is an *exposition*
vulnerability, not a math error — but it is load-bearing and a sharp referee would hit it.

## Layer 0 — information-isolated blind re-derivation [free; DONE]

5 solvers, each handed only the NPB (no answer, no manuscript), rigor-lens nudges only.

| Solver | Net E[T] | E[A] (imputation) | E[B] (estimation) | MAR term |
|---|---|---|---|---|
| L0-1 | **−½ tr(RIV)** | 0 (tower/congeniality) | −½ tr(RIV) | no |
| L0-2 | +½ tr(RIV) (RIV-part) + spurious O(n) | +½ via Q̄-pivot | — | yes (but mis-ordered O(n)) |
| L0-3 | **−½ tr(RIV)** | 0 (tower) | −½ tr(RIV) | no |
| L0-4 | **−½ tr(RIV)** (muddled) | +½ then "cancels" | −½ tr(RIV) | no |
| L0-5 | **−½** literal / +½ "project framing" | 0 oracle / +tr fitted | −½ tr(RIV) | no |

Layer-0 verdict: **MIXED/DIVERGE**. Majority `−½`. Every solver localizes the split to
Term A and sets it to 0 via the tower property under the oracle reading of D9.

## Layer 1 — method-diverse routes R1–R4 [free; DONE]

| Route | Net E[T] | Note |
|---|---|---|
| R1 obs-pivot | −½ tr(RIV) | imputation bracket **= 0 exactly** by tower + `Y_obs`-measurability |
| R2 com-pivot | −½ tr(RIV) **+ O(1) D_design** | framing-independent; **independently re-derived the MAR (A)+(C) term** (0 under MCAR) |
| R3 no-split direct | −½ tr(RIV) | k/2 self-fit bonuses cancel; level term 0 by tower; cleanest |
| R4 optimism/AIC | −½ tr(RIV) | imputation cross-term 0 via score-projection `Cov(U_com,U_obs)=I_obs` |

Layer-1 verdict: **DIVERGE on net sign** (all four → `−½` for the literal/oracle object),
but two strong corroborations of *novel* pieces: R2 independently rediscovered the MAR
`(A)+(C)` design-imbalance term; R2/R3 (framing-independent of the manuscript's A/B split)
both confirm `E[B] = −½ tr(RIV)`.

## Layer 2 — CAS ground-truth [free; DONE + TODO-B open]

- `verification/cas-wolfram/verify_traces.py` (committed) — trace algebra `+tr / −½tr / +½tr`,
  Magnus duplication-matrix inverse (p=2), `(A)+(C)` consistency: **ALL PASS** (Wolfram 14.3).
- `verification/cas-wolfram/verify_term_ac.py` (untracked) — **TODO-A**: *independent* Wolfram
  re-derivation of the bivariate `(A)+(C)` (derives `α`, `H_φ` from the Gaussian cross-entropy):
  **ALL PASS**. TODO-A is now done + verified. **(File is untracked but cited by `derivation.qmd:738` — commit it.)**
- **TODO-B** (non-monotone `(A)+(C)` via Cox–Snell / Cordeiro–Klein): still open.

The CAS confirms the trace *bookkeeping* (given `E[A]=+tr`, `E[B]=−½tr` ⇒ `+½tr`). It does
**not** adjudicate the fitted-vs-oracle fork — that is a modeling premise, not algebra,
exactly as the plan anticipated.

## Decisive grounding experiment (`verification/rederivation-L0-fitted-vs-oracle.R`)

N=200, R=4000, repo DGP + `apply_mar`, both imputation laws measured on the same replicates:

```
mean tr(RIV) = 5.5523
E[B]        = -3.3397   target -1/2 trRIV = -2.7762   (ratio 1.20; finite-n, ->1 with n)
FITTED  P(.|Y_obs, theta_obs)   [repo / manuscript]:
  E[A_fitted] = +6.0741   target +trRIV    = +5.5523   ratio 1.094
  E[T_fitted] = +2.7345   target +1/2 trRIV= +2.7762   ratio 0.985   <-- manuscript +1/2 CONFIRMED
ORACLE  P(.|Y_obs, theta_TRUE)  [solvers' tower reading]:
  E[A_oracle] = -0.0468   target 0          ratio -0.008             <-- tower property CONFIRMED
  E[T_oracle] = -3.3865   target -1/2 trRIV= -2.7762   ratio 1.22    <-- solvers' -1/2 CONFIRMED
```

Committed W1 caches (cross-reference): FIML `Ahat/trRIV ≈ 0.71–1.15`, `That/trRIV ≈ 0.16–0.55`;
Amelia (proper MI) `Ahat/trRIV ≈ 0.95`, `That/trRIV ≈ 0.42`. Both engines → fitted object →
`+tr / +½`. (The `<1` `That/½trRIV` reflects the negative MAR `(A)+(C)` correction + finite-n.)

## Verdict against the decision gates

- **−½ estimation half + θ̂_com-as-target premise** (the plan's "single most framing-dependent
  claim"): **survived with near-unanimity** (9/9 + framing-independent R2/R3 + the experiment).
  This is the most strongly triangulated element. PASS.
- **MAR `(A)+(C)` term**: independently re-derived by R2 (Layer 1) *and* by Wolfram (TODO-A).
  Upgraded from single-source to triangulated. PASS.
- **Net `+½ tr(RIV)` headline**: **correct for the operational/fitted object** (empirically robust,
  FIML + Amelia), but DIVERGES to `−½` under the literal oracle reading of D9. The divergence is
  a real, localized soft spot — a definitional ambiguity, not an algebra error.

## Recommended action (NOT yet applied — awaiting author sign-off)

Rewrite **Definition D9** so `Q̄_∞` is unambiguously the average over the *fitted* imputation
predictive `P(· | Y_obs, φ̂)` (φ̂ the imputation parameter ≈ `θ̂_obs`), and **drop or heavily
caveat** the equality `= E[ℓ_com(θ;Y)|Y_obs]`: under fitted congenial MI this equality is false
(it would force `E[A]=0`), and the gap between the fitted average and the true conditional
expectation **is exactly Term A's `+tr(RIV)`** — i.e. the gap is the result, so the notation must
not assert it away. Add a one-line lemma: `θ̂_obs` is `Y_obs`-measurable, so the *oracle* object
`E[ℓ_com(θ̂_obs)|Y_obs] − ℓ_com(θ̂_obs)` has mean 0 by the tower property; Term A is nonzero
precisely because the imputations use `φ̂ ≠ θ0`. This pre-empts the most natural referee objection.

## Layer 3 — cross-model adversarial (GPT-5.5, reasoning_effort=xhigh) [executed 2026-06-01]

Ran the `todo/013b` packet against GPT-5.5 (FrontierMath leader, June 2026) via
`verification/run_layer3_openai.py` — a different model family, fully off the Claude lineage.
Raw responses: `verification/cache/layer3-gpt-5.5-mode{A,B}.md`.

**Mode B (red-team) — the headline Layer-3 win.** GPT-5.5 *spontaneously* named the D9
fitted-vs-oracle ambiguity as "the weakest premise," independently reproducing the tower-property
argument verbatim: under the literal `Q̄_∞ = E[ℓ_com|Y_obs]`, Term A = 0 ⇒ headline is
`−½tr(RIV)`, not `+½`. **This is independent cross-model confirmation of the Layer-0/1 finding and
validates the D9 fix.** It also re-derived `E[B] = −½tr(RIV)` with `Cov(θ̂_obs,θ̂_com)=I_com⁻¹` and
flagged the `−½k` trap exactly as the manuscript does. The `−½` premise is now triangulated across
Claude (9/9), the CAS, the experiment, *and* an independent model family.

**New finding GPT-5.5 surfaced that the free layers missed — convention-dependence + non-universality.**
Even with the fitted definition pinned, GPT-5.5 shows `E[A] = +tr(RIV)` is **not invariant to
θ-free, Y-dependent additive constants** in the log-likelihood. It decomposes
`E[A] = ½tr(RIV) [KL term] + Δ_n [conditional-entropy plug-in bias]`, giving
`E[T] = E[A] + E[B] = Δ_n` (the two `½tr(RIV)` halves **cancel**). Then:
- `Δ_n = 0` when the conditional entropy does not depend on the estimated parameters — e.g.
  **known-variance MVN (mean only): `E[T] = 0`, not `+½tr(RIV)`.** Confirmed by hand (FIML→0,
  proper→`−½tr(RIV)`) and by GPT-5.5's own normal-mean check.
- `Δ_n ≈ +½tr(RIV)` for the **unknown-(μ,Σ) MVN** (covariance estimated) — matching the manuscript
  and the experiment.

So `E[T] = Δ_n` reconciles with the manuscript's `½tr(RIV)+(A)+(C)` **iff** `Δ_n = ½tr(RIV)+(A)+(C)`
— i.e. GPT-5.5 lumps the whole bias into one conditional-entropy object, and argues the "+½tr(RIV)"
is **not an intrinsic RIV penalty** but the entropy plug-in bias, RIV-sized only when (co)variance
is estimated. **The manuscript's "`+½tr(RIV)` for *any* regular likelihood fit" is therefore an
overreach: it fails (gives 0 or `−½`) for known-variance / mean-only models.**

GPT-5.5 also flagged that the Term-A cross-term needs more than "proper MI": specifically
`E_imp(φ̃|Y_obs)=θ̂_obs+o_p(n^{-1/2})` (a Bernstein–von Mises posterior-alignment condition) and a
self-efficient/congenial setup for `T_∞=I_obs⁻¹` — properness alone is insufficient. The MAR
`(A)+(C)` it accepts as plausibly `O(1)` and confirms the bivariate-monotone MCAR cancellation
algebra, but calls it model-specific, not a general MAR theorem.

**Layer-3 verdict.** PASS on the `−½` and the D9 fix (independently confirmed). ESCALATE the new
finding: the headline's **universality and its `+tr/−½tr` decomposition are convention-dependent**
(kernel vs full density; estimated-variance vs known-variance). This is the highest-value finding of
the whole exercise and the cross-model layer is exactly what surfaced it.

**Decisive adjudicating test (proposed, not yet run):** measure `E[A]`, `E[B]`, `E[T]` for a
**known-variance** model (estimate the mean only, Σ fixed), FIML and proper. Prediction: `E[T] → 0`
(FIML) / `−½tr(RIV)` (proper), *not* `+½tr(RIV)`. If confirmed, the theorem must be restated as
holding for models with parameter-dependent conditional entropy (covariance estimation), not "any
regular likelihood."
