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
comparison**. Its core result: under congenial proper MI, the MI Q-function's deviance
carries a bias of **+½·tr(RIV)** (RIV = relative increase in variance), from imputation bias
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

*As of the last charter wrap (2026-11-13). The last manuscript work was 2026-07-05; whether
the JAIGP submission has since happened is not recorded in the repo (an open question in the
charter).*

**Submission-ready and closure-validated.** Every repo-side milestone is done: derivation and
proofs (incl. CAS verification), pre-registered simulation witnesses, the response to the v1
AI review (all 15 comments), the Lemma P canonical-GLM extension, the D-26 style-register
pass, compile-enablement (level3 prose locked), and two repo-grounded Antigravity validation
rounds — the second blind — confirming all 15 original review concerns ADDRESSED.

The one open milestone is the **JAIGP submission itself**, which is Marcus's action. The
deliverables are `manuscript/mi-spectral-apa.pdf` and
`manuscript/reviews/v1/response/response-letter.pdf` (the delinked, AI-reviewer-safe letter).
Zenodo was dropped; the public GitHub repo and Pages site are the public record.

## Where it goes next

1. **Marcus submits to JAIGP** with the two deliverables above.
2. **Machine move:** confirm on drive.google.com that `Literature/MI-SPECTRAL` holds all 72
   PDFs; on the new machine, point `scripts/lit_sync.py` (lines 42–43) at wherever Drive
   mounts before the first `/lit-sync`. Details in
   [reproducibility](/architecture/reproducibility.md).
3. **Presentation residuals and optional items (Marcus's call, none blocking):** compact
   Table 1; publish `mi-spectral-apa.html` to the Pages site; restore the "Prompters"
   title-page label; any override of the six keep-as-is defaults in `status.json`; an
   optional register-deepening pass; extend the bootstrap-floor arm to N=500/2000 (gate C7);
   verify Mode B's IMB closed form before ever citing it; silence apaquarto's
   affiliation-noise ERROR lines; the transcripts-link loop; merge the duplicate Cox–Snell
   Zotero item.

For the settled calls behind all of this, see [decisions](/decisions/decisions.md).
