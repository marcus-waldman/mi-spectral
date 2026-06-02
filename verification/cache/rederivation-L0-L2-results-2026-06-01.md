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
