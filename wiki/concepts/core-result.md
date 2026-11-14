---
type: Concept
title: The core result and its scope
description: The +½·tr(RIV) deviance-bias theorem, its two applications (LRT, information criteria), and where it does and does not hold.
sources:
  - "CLAUDE.md (Core contribution, Lineage, Out of scope)"
  - ".prometheus/charter.md (Decisions made — incl. scope narrowed, D-27, 2026-11-13)"
  - "todo/051-scope-corrections-plan.md (findings F1-F8)"
updated: "2026-11-13"
---

# The core result and its scope

## The theorem

Under congenial MI with the complete-data MLE as the target, imputed by a second-moment-matched
engine, the Q-function deviance bias decomposes as **Bias[Q̄∞(θ̂_obs)] = +tr(RIV) − ½tr(RIV) = +½tr(RIV)**: the +tr term is
imputation bias, the −½tr term is estimation mismatch (MI targets θ̂_com, not θ̂_obs). As
narrowed by D-27 (2026-11-13), it holds for the multivariate normal with an **unrestricted**
covariance (what the proof covers) and, up to an offset, the canonical GLMs of Lemma P. A
known-scale, location-only fit collapses to 0 (FIML) / −½tr(RIV) (proper MI).

## Two applications

- **Likelihood-ratio model comparison.** At H₀ the numerator's differential bias is
  tr(RIV_⊥), the missing information of the tested directions projected in the
  **I_com metric** — not the naive tr(RIV) − tr(RIV₀), which always overstates it. The
  MAR design-imbalance term (A)+(C) cancels exactly at H₀ and returns at O(1) only for
  non-nested comparison.
- **Information criteria (headline empirical claim).** MI-AIC/MI-BIC take −2Q̄∞ as their
  deviance; its bias −tr(RIV_k) differs by candidate, so uncorrected criteria favor
  high-RIV models. The correction restores complete-data-equivalent selection in
  expectation (substantially, not completely — a weak-signal shortfall remains). For BIC the
  same correction applies to the numerator, with the complete-data N in the penalty; its
  yield is much smaller at N ≥ 200 (Discussion limit G8).

## Scope, as settled

- **Engines.** The +½ headline holds for *second-moment-matched* imputation engines
  (FITTED; bootstrap/EMB such as Amelia). Bayesian posterior-draw engines carry a derived,
  disclosed discount (decision D-22). D-22 had
  reached only `derivation.qmd`; D-27 carries it into the manuscript (pending, `todo/051`).
- **Structured covariances (D-27).** A constrained covariance can break the result even
  under MCAR: with N₂(μ, σ²I), one variable always observed and the other MCAR-missing on a
  fraction π, E[T] = 3π/(2(2−π)) against ½tr(RIV), an O(1) gap. The paper's simulations are
  unaffected because they impute under the saturated model, where the per-candidate level comes
  from the likelihood-ratio propositions L1/L2.
- **Beyond MVN.** The canonical-GLM extension (Lemma P, response-only MCAR) gives
  +½tr(RIV) + Δ_h, with Δ_h a base-measure term: 0 for Bernoulli, −0.396·tr(RIV) for Poisson
  at the studied design (decision D-25). MVN remains the default scope.
- **Out of scope:** SEM specifics (companion repo MI-IC), FIML/EM observed-data inference,
  test-calibration itself (cite Chan 2022), non-regular settings.

## Lineage

Rubin (1987) → Meng (1994, congeniality) → Chan–Meng (2022) → Chan (2022, *AoS*; canonical
reference for MI test calibration) → this work, upstream of test calibration. Cavanaugh–Shumway
(1998) is a parallel universe (EM-based observed-data MLE).

Decision history for each of these points lives in [decisions](/decisions/decisions.md).
