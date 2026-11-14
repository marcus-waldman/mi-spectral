---
type: Overview
title: mi-spectral — overview
description: One-screen briefing — what mi-spectral is, why it exists, and where it stands.
sources:
  - ".prometheus/charter.md (Goal, Current milestone, Milestones, Next 3 actions)"
  - "CLAUDE.md (Scope, Core contribution, Authorship model)"
updated: "2026-11-13"
---

# Overview

## What & why

mi-spectral is a theory paper on **multiple imputation (MI) and likelihood-based model
comparison**. Its core result: for the multivariate normal with an unrestricted covariance,
imputed by deterministic FIML or bootstrap-EM, the MI Q-function's deviance carries a bias of **+½·tr(RIV)** (RIV = relative increase in variance), from imputation bias
(+tr) minus estimation mismatch (−½tr). Because that bias is *model-specific*, uncorrected
MI-AIC/MI-BIC favor the candidate models with the most missing information; the paper
derives the correction and applies it to likelihood-ratio tests and information criteria.
The predicted empirical signature — uncorrected MI-AIC errors concentrate on the
highest-RIV candidate — held in every cell of the selection sweep (W3-C = 1.000).

The project was **reframed on 2026-05-22** after Chan (2022, *Annals of Statistics*)
preempted the original "spectral chi-square correction" framing; the paper now sits
*upstream* of test calibration, correcting the numerator that Chan's reference distribution
calibrates. It is a human-prompted
AI derivation with ORCID-verified provenance, targeting **JAIGP**.

See [the core result](/concepts/core-result.md) for the theorem and its scope, and
[reproducibility](/architecture/reproducibility.md) for how evidence and prose are produced.

## Where it stands

*As of the charter wrap of 2026-11-13 (second session). The paper is **not yet submitted**
(Marcus, 2026-11-13).*

**Scope corrections before submission.** An adversarial review of the derivation (Gemini,
run by the theoretical-statistician-agent session) was checked by hand. Two findings change
the paper's statements, though no reported number: the theorem's stated scope was too broad
(a shared-variance covariance breaks +½·tr(RIV) under MCAR), and decision D-22's imputer
restriction never reached the manuscript prose. Marcus ratified the corrections as D-27; the
plan of record is `todo/051-scope-corrections-plan.md`. Everything else repo-side was already
done: derivation and proofs (incl. CAS verification), pre-registered simulations, the response
to the v1 AI review (all 15 comments, closure-validated), the Lemma P canonical-GLM extension,
the D-26 register pass, and compile-enablement (level3 prose locked).

## Where it goes next

1. **Two exploratory checks** (todo/051 §4), predictions written first: a Monte Carlo and CAS
   check of the shared-variance case, and the non-monotone selection-covariance check.
2. **Apply the D-27 corrections:** `derivation.qmd` first, then the locked level3 prose unit
   by unit with Marcus, one update script, rebuild and render.
3. **Marcus submits to JAIGP** with the corrected `manuscript/mi-spectral-apa.pdf` and
   `manuscript/reviews/v1/response/response-letter.pdf`. Machine move: confirm the Drive
   PDFs and Mathpix cache (nothing to repoint; `lit_sync.py` is retired). Optional
   presentation residuals are unchanged and listed in the charter.

For the settled calls behind all of this, see [decisions](/decisions/decisions.md).
