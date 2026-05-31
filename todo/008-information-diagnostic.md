# Todo 008 — Finite-sample information diagnostic (expected vs sample RIV)

**Status:** Exploratory / post-hoc (NOT pre-registered). Folded into the comprehensive
battery as **Phase 6** of `verification/run_all.R`
(`_modules/w1-information-diagnostic.R`, output `cache/run_all-<suffix>/phase6-info/`).
Surfaced 2026-05-30/31 while interrogating the W1 finite-sample remainder.

## What it establishes

The W1 theorem's per-term identities (`E[A]=+tr(RIV)`, `E[B]=-½tr(RIV)`) hold to leading
order against the **expected-information** RIV, but the two terms calibrate to **different
finite-sample RIVs**:

1. **A (imputation bias) → expected-information RIV** `tr(I_obs⁻¹ I_mis)`. A consumes
   `Var(θ̂_obs)`, which equals `I_obs⁻¹` even at finite n (well-behaved).
2. **B (estimation mismatch) → sample / observed RIV** (Rubin between/within ≈ observed-
   information). B consumes `Var(θ̂_obs − θ̂_com)`, whose asymptotic identity
   `I_obs⁻¹ − I_com⁻¹` (derivation Lemma L2) is finite-sample **inflated** by ~10% at n≤2000.
3. **Information equality holds** — `tr(𝒥̂ 𝓘⁻¹) ≈ k` (correct specification). So the split is
   the **finite-sample (Efron–Hinkley)** face of the J-vs-I distinction, **not** the
   misspecification (TIC/Pawitan §13.6) face.
4. **T = A + B** therefore sits below `½tr(RIV)` at finite n by ≈ `½(tr_samp − tr_exp)`,
   closing only as the Efron–Hinkley gap closes (slowly — empirically slower than O(n⁻¹)).
5. **Engine-independent**: proper MI (Amelia) gives the same picture as deterministic FIML;
   proper MI even *lowers* A slightly vs FIML (Jensen — dispersed imputations averaged
   through the concave complete-data loglik), so posterior draws do not push A onto the
   sample RIV.

This refutes the earlier "individual terms ~10–20% off but residuals cancel so T holds"
story (derivation.qmd note after `@eq-combine`) — T does **not** exactly hold at finite n;
the deviation is the expected-vs-sample information gap. Drives the derivation edits
(define both informations, state which variance each term consumes, correct that note).

## Headline numbers (high-R reference; apply_mar, RB-A)

Proper-MI (Amelia M=80), N=2000, R=40000:

| | A_proper | A_FIML | B | T_proper | tr_exp | tr_samp |
|---|---|---|---|---|---|---|
| mean | 5.36 | 5.62 | −3.03 | 2.33 | 5.51 | 6.09 |

- `A_proper − tr_exp ≈ −0.15` (≈0); `A_proper − tr_samp ≈ −0.73` (and not closing) → A tracks **expected**.
- `B + ½tr_samp ≈ +0.01` (B tracks **sample**); `B + ½tr_exp ≈ −0.27` (off).
- `T_proper − ½tr_exp ≈ −0.43`, not closing over n≤2000.
- proper − FIML A ≈ −0.26 (robustly negative, ~10σ; Jensen).

J-vs-I check (R=4000): `tr(𝒥̂ 𝓘_obs⁻¹) ≈ 13.9 ≈ k=14` (info equality); `tr(I_obs·Var̂(θ̂_obs)) ≈ 14.3`
(θ̂_obs variance clean); `tr(I_com·Var̂(gap)) ≈ 6.0` vs expected `5.5` — the inflation lives in
the **gap** variance (Lemma L2 / the `Cov(θ̂_obs,θ̂_com)=I_com⁻¹` step), not in `Var(θ̂_obs)`.

## Rejected — do NOT re-attempt

**Control variate (b): regress A on the score at θ_true.** Reduces variance (residual sd flat
~3.4 across N) but is **biased ~+0.25 (≈9σ at R=15k)** because A is *quadratic* in θ̂_obs and a
linear regression on the score cannot preserve the quadratic's mean when the score→θ̂ map is
random. Use plain brute force (unbiased) for E[A]/E[T] precision. Confirmed 2026-05-31.

## Reproduce

```
Rscript verification/run_all.R 2000 prod "6,5" 20   # phase 6 + aggregate fold-in
```

Phase 6 is MAR cells only (congenial regime), 2 patterns × N∈{200,500,1000,2000}, Amelia M=50,
info-equality on a capped subset (score_cap=600). Self-contained verdicts; aggregate (phase 5)
folds the `INFO` row into `phase5/verdicts.md` when both run.

## References (acquired this session — see todo/003)

- `efronAssessingAccuracyMaximum1978` — observed vs expected Fisher information
- `pawitanAllLikelihoodStatistical2013` — 𝒥/𝓘, sandwich, 𝒥=𝓘 under correct spec, `tr(𝒥𝓘⁻¹)`
- `konishiGeneralisedInformationCriteria1996` — GIC/TIC under misspecification
