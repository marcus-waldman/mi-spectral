# Todo 023 — FOLLOW-UP PAPER capture: distributional calibration of MI information criteria

**Status:** PARKED (2026-06-03). Scope decision: this paper = bias correction + LRT application
(W1/W2, plus the existing W3 results with calibrated wording). Everything below is the **sequel**,
captured from the 2026-06-03 design discussion so it does not evaporate. Do NOT start in the
current paper's sessions.

## Premise

The `+tr(RIV)` correction fixes the **first moment** of the MI deviance. Model selection, however,
consumes the **distribution of pairwise ΔAIC** — selection error ≈ Φ(−Δmean/sd(Δ)). Mean
correction alone leaves an excess-variance flip rate (the measured π≈0.81 corrected vs ≈0.90
oracle residual in `cache/run_all-prod/phase2-w3/summary.csv`). Sequel title-shape: *"From bias
correction to full distributional calibration of MI information criteria."*

## The correction ladder (rungs, each strictly stronger)

1. **Mean-only**: `−tr(RIV_k)` per model (this paper). Linear ⇒ coherent across all pairwise
   comparisons; telescopes along nested chains.
2. **Two-moment (SB-type)**: `a·(d − bias_corr) + b` — Satorra–Bentler scaled-and-shifted form
   with an MI-specific target (complete-data deviance variance from the within/between
   decomposition). This is what the W3 "SB arm" was *intended* to be (CLAUDE.md issue #1 — being
   retired from this paper, becomes rung 2 here).
3. **Equipercentile equating**: `d_eq = F_com⁻¹(F_MI(d))` via a Chan-2022-style MC reference.
   Matches ALL moments — but only **under the null of the pair being equated**.

## Key structural results from the design discussion (derive + verify in the sequel)

- **The right calibrand is pairwise ΔAIC, not marginal AIC.** Selection only consumes signs of
  differences; matching marginals is neither necessary nor sufficient (copula matters).
- **Equating is decision-equivalent to Chan's test for W2-type testing** (monotone map ⇒ same
  p-values). Its value is exclusively for deviance-*scale* consumers (IC). Equating = the bridge
  that transports Chan's test-calibration machinery into model selection.
- **Null/noncentral asymmetry (the toy):** with RIV=1, MI scales a 1-df statistic by ~(1+RIV) and
  shrinks its noncentrality by ~1/(1+RIV). The null equating map (÷2) is exact for null pairs
  (overfit comparisons) but maps a noncentral gap χ²₁(λ=20)→mean 11 where complete data has
  mean 21 — equating **understates evidence against underfit models**. Information loss is not
  equatable; no monotone transform restores destroyed Fisher information.
- **Circularity and its candidate fix:** correctly equating a noncentral pair needs λ (the
  estimand). BUT λ is method-of-moments estimable (λ̂ ≈ T − df, RMSEA logic) and the shrinkage
  factor ≈ 1/(1+RIV) is estimable from the between/within decomposition ⇒ a
  **noncentrality-aware de-shrinkage equating map** is constructible from observed quantities.
  NEW ANALYTIC CLAIM ⇒ GPT-5.5 blind cross-check required before relying on it.
- **Transitivity:** per-pair equating maps are nonlinear ⇒ pairwise-calibrated comparisons can be
  intransitive. Fix: common-reference scheme, scores `s_X = eq_X(D_X − D_A)` with A = the
  encompassing/saturated model (the SEM model-chi-square convention, rederived). Cost: indirect
  B-vs-C comparisons inherit distortion (difference of nonlinear transforms ≠ transform of
  difference); baseline choice is a stated convention.
- **Marginal scale ≠ joint scale:** equating is a coordinatewise transform — it places marginals
  exactly and **cannot touch the copula**. Two perfectly-χ²₁ marginals give Var(diff)=4 if
  independent, 0.4 if corr 0.9. MI's shared-imputation noise changes corr(s_B, s_C) relative to
  complete data (plausibly upward ⇒ could *help* difference conditioning) — measure it.
- **Saturated anchoring is a free control variate:** in the MVN setting the saturated model IS
  the congenial imputation model; D_k − D_sat cancels the common realized heavy-tailed (A)+(C)
  component; bias of T_k is the clean differential tr(RIV_k) − tr(RIV_sat).

## Designed testbed (for the sequel's simulations)

Full pairwise matrix over {Z=independence, …candidates…, A=saturated}:

- **Triangle-closure residuals** `eq_ZA(Δ_ZA) − [eq_ZB(Δ_ZB) + eq_BA(Δ_BA)]` — a truth-free
  internal measurement of equating nonlinearity/intransitivity error (raw deviances telescope
  exactly; linear corrections telescope; equating breaks closure by a measurable amount).
- **Two anchors bracket the regimes:** A-anchored pairs = null regime (equating exact);
  Z-anchored pairs = strongly noncentral (equating shrinks). Compare A-anchored vs Z-anchored
  rankings: agreement ⇒ noncentral distortion practically irrelevant.
- **Copula diagnostic:** corr(s_B, s_C) under MI vs complete-data analog.
- **Stress cells:** weak true coefficient (small λ, near-tied pairs) = where equating's
  underfit-retention cost should appear; junk-heavy candidate sets = where its calibration win
  should appear.
- **Ladder prediction:** each rung closes more of the corrected-vs-oracle gap; asymptote sits
  BELOW oracle by the irreducible information-loss floor (decomposes the residual into fixable
  calibration error vs unfixable information loss).

## Scope guardrails (carried from this paper)

- Z-vs-A is one step from CFI/TLI ⇒ SEM fit indices stay OUT (MI-IC repo). Z is a calibration
  probe only; any "MI-corrected fit index" implication is a one-line pointer to MI-IC.
- Heavy-tailed (A)+(C) statistics ⇒ paired/control-variate estimators, never brute-force means.
- Any analytic derivation ⇒ blind GPT-5.5 xhigh/24h cross-check (Mode A + Mode B, leakage-scanned),
  per the standing directive.

## What this paper (mi-spectral) keeps

- W3 results as-is with honest "substantially recovers, π≈0.81 vs oracle ≈0.90" wording.
- A short future-work paragraph: full selection recovery requires matching the distribution of
  pairwise ΔAIC, not just its mean → points here.
- SB arm formally retired (issue #1 closed with rationale: two-moment matching belongs to the
  distributional-calibration program).

*Captured 2026-06-03 from the W3-redesign discussion; parked pending the current paper's submission.*
