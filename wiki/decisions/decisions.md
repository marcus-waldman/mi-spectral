---
type: DecisionLog
title: Decisions
description: The single canonical list of settled calls, including supersessions.
sources:
  - ".prometheus/charter.md (Decisions made)"
  - "manuscript/plan/decisions.md (D-numbered decisions of record, as referenced by the charter)"
updated: "2026-11-13"
---

# Decisions

The **single canonical decisions page** — every other wiki page links here rather than
restating a decision (`schema.md` §7). This page mirrors the charter's append-only
"Decisions made" log *as settled state*: related calls are grouped, and where the charter
superseded a call, the current ruling is shown with the replaced one noted. `D-nn` labels
refer to `manuscript/plan/decisions.md`.

## Scope and framing

- **Scope:** congenial MI + regular likelihood only; non-congenial, FIML, and EM are separate
  universes. MVN stays the default scope; a non-normal extension needs an explicit call.
- **Reframed after Chan (2022, *AoS*)** to a deviance-bias decomposition *upstream* of test
  calibration. Le Cam power dominance is demoted to a Discussion conjecture.
- **Structure of the evidence:** three pre-registered witnesses (W1 theorem, W2 LRT, W3 model
  selection) and two applications (LRT, information criteria). The +tr / −½tr terms are
  reported separately, not just their sum.
- **W3-C = 1.000 under uncongeniality is genuine** (pre-registered, held in all 60 cells), but
  it confirms the bias *direction*, not the decomposition; uncongenial behavior is disclosed as
  limit G7.

## Theory results that changed the paper

- **Engine scope (D-22, ratified 2026-07-02).** The +½tr(RIV) headline holds for
  second-moment-matched engines (FITTED; bootstrap/EMB such as Amelia, which the paper's
  validation used). Bayesian posterior draws carry a derived, disclosed discount. The earlier
  "Schur–Jensen inflation" mechanism and the "83%/13%/4%" percentage decomposition were
  **retracted** and must not be used.
- **MI-BIC (D-23).** The correction transfers to BIC's deviance numerator verbatim, with the
  complete-data N in the penalty. Yield is small at N ≥ 200; at N = 50/100 the
  error-concentration pattern weakens. Landed as limit G8, which now states the explicit
  corrected MI-BIC formula.
- **Non-normal families (D-25 supersedes D-24).** The original Phase-3 Bernoulli
  classification was a category error (HARKing, found by Marcus, adjudicated AMENDED by a
  cross-family quorum). It was replaced by a derived theorem — Lemma P, the canonical-GLM
  extension with a base-measure term Δ_h — confirmed by pre-registered blind scans (incl. a
  blind Poisson arm and a Student-t known-scale exemplar), a GPT-5.5 Pro gate, and a
  repo-grounded Gemini compliance check. Landed as limit G9 and as `@sec-glm` in
  `derivation.qmd`.
- **LRT differential:** the H₀ bias is tr(RIV_⊥) in the I_com metric; the naive difference of
  traces always overstates it (see [the core result](/concepts/core-result.md)).

## Evidence and verification discipline

- **Trust gate:** hard evidence must survive adversarial scrutiny before entering the
  manuscript; each figure is tied to the exact claim it supports. The S5 cross-family tribunal
  returned AMEND with no result retracted.
- **Due diligence against the data:** verify wording against results and sources, not against
  prose or a panel's assumption.
- **Reproducibility fold-in gate (standing policy):** a cited verification result must be
  reproducible through `run_all.R` + `aggregate.R` + `CLAUDE.md` before it is cited.
- **Citation discipline:** every citekey is backed by a locally read `literature/` copy; a
  repo-grounded audit (todo/039) checked all 69 citation attachments (66 support, 2 partial,
  1 misattributed — fixed).
- **Validation pattern:** for staged text, use a repo-grounded validator (Gemini via
  Antigravity, read-only) rather than API-only panels; run closure validation twice, the
  second round blind.

## Manuscript structure, authorship, and build

- **Arc:** seven moves (D-12 added an "AI–human collaboration" section between Introduction
  and Background; supersedes the six-section IMRaD). No Conclusion. Contributions list in the
  Introduction and an applied-implications passage in the Discussion (D-15).
- **Title (D-19):** "Model selection after multiple imputation: a deviance correction for AIC,
  BIC, and likelihood-ratio tests."
- **Authorship (D-18 amends D-16; reordered 2026-07-05):** Marcus Waldman first with
  affiliation, then the AI authors (Claude Opus 4.7–4.8, Claude Fable 5, GPT-5.5 Pro,
  Gemini 3.1 Pro). The "Prompters" label was dropped with the reorder (restorable).
- **Terminology (D-20):** "human-prompted AI derivation," not "AI-assisted." Also: "complete-data
  benchmark" replaces "oracle" in reader-facing prose; "repetitions" for Monte Carlo.
- **No direct quotes (D-17)** of other work in manuscript prose — paraphrase and cite.
- **Canonical render (D-21):** the apaquarto build from level3 is the only manuscript build;
  the JASA/arXiv preview and the old HTML pipeline are retired. The build emits PDF and a
  self-contained HTML.
- **Compile enabled (2026-07-05):** Marcus declined further annotation; level3 is locked; six
  discretionary items defaulted to keep-as-is and remain overridable in `status.json`.
- **Scope limits** are introduced by name as G1–G9, one per paragraph. An evidence-map table
  (claim → basis → study → result → verdict) leads the results section.

## Prose register

- **Current register: D-26 (v3, 2026-07-05)**, grounded in the owned Rubin-era exemplars.
  It **supersedes** the 2026-06-27 readability pass's FK-10 / short-declarative target and the
  punctuation-budget v2 (semicolons now up to 3 per paragraph; parentheticals and provenance
  appositives allowed; em-dash ban kept; color-commentary ban narrowed to a register-attested
  evaluative set). Vocabulary must stay within the literature-corpus distribution (gate is
  fatal). R11 typed precision: "exactly" only for genuine identities.
- **Standing invariants:** models never lose or gain data — per-candidate differences are
  attributed to tr(RIV); no orphaned pronouns; no color commentary.
- **Method:** prose passes run per paragraph with a human gate and a single adversary, not
  via batch multi-agent workflows. The full fluff-tightening sweep (todo/036) was shelved as
  not worth the overclaim risk.

## Submission tail

- **No Zenodo deposit:** the public GitHub repo and Pages site are the public record.
- **Response letter:** finalized; rendered to PDF. It was first GitHub-linked for reviewers,
  then **delinked** for the submission copy because the AI reviewer crawls links into the code
  and hangs. The linked version remains in history at `7327d37`.
- **Closure validation:** two Antigravity rounds; round 1 found three real gaps (fixed at
  `64950b0`); round 2 (blind) found all 15 original concerns addressed.

## Recorded tooling gotchas

- The citation hook misfires on Edit/Write in `manuscript/` subdirectories — write via Bash.
- Content with backslashes must go through a written `.py` file, never a Bash heredoc.
- A slow render is a one-time TinyTeX update — let it finish.
- Confirm `git branch --show-current` before rendering; a concurrent session can switch it.
- tkal quorum: read per-peer `determination.json`, not the headline class ("REFUTED"
  aggregation bug).
- Drive PDFs for multi-word surnames must be renamed to `<citekey>.pdf` for lit-sync.
- Never harvest Amelia's internal `mu`/`covMatrices` (reordered, standardized scale).
