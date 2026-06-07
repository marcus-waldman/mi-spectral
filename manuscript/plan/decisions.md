# Locked decisions — mi-spectral manuscript

Dated, human-ratified choices. Not relitigated without an explicit, dated amendment
(same discipline as the pre-registration amendments in `todo/004` / `todo/029`).
Strategic decisions D-01…D-08 live in full (chosen + rejected options + rationale) in
`level1-thesis.json`; this file is the running index plus everything ratified later
(style rules, terminology, per-section adjudications).

## Status key

- **ratified** — Marcus approved; binding.
- **ratified_in_prior_work** — decided and acted on in committed work before this system
  existed; listed for the record, confirm during Level-1 annotation.
- **proposed** — recorded by Claude, awaiting Marcus.
- **amended (date)** — superseded by a later dated entry; keep both.

## Strategic (Level 1)

| id | date | decision | status |
|---|---|---|---|
| D-01 | 2026-05-22 | Deviance-bias framing, upstream of Chan's calibration | ratified_in_prior_work |
| D-02 | 2026-06-02 | Fitted-imputation headline (+1/2), oracle contrast stated in setup | ratified_in_prior_work |
| D-03 | 2026-06-05 | Consolidated numerics section + inline headline numbers | **ratified** (2026-06-06, cycle 2); **amended 2026-06-07** (A1) |
| D-03-A1 | 2026-06-07 | Amendment 1: the Derivations section carries NO Monte Carlo numbers and no simulation findings — preregistered claims get one-line forward pointers to @sec-simulations; ALL empirical content consolidates in S5; inline headline numbers remain permitted in S1 and the S6 verdict (summary, not substantiation). Rationale: a Derivations section must derive; "from multimodal evidence we know this is true" undercuts the formal posture, and S3 Methods already establishes the verification pipeline once. Rejected: keeping inline numbers at point of claim in S4 (the original D-03 choice — made before D-09 split Results into Derivations + Simulation studies, which changes the calculus) | **ratified** (in-chat) |
| D-04 | 2026-06-05 | Background as precision restatement with displays | **ratified** (2026-06-06, cycle 2) |
| D-05 | 2026-06-05 | Trust-ordered claims; failures reported in main text | **ratified** (2026-06-06, cycle 2) |
| D-06 | 2026-06-04 | Scope split: ladder rungs 1–3 in-paper; de-shrinkage etc. to sequel | ratified_in_prior_work |
| D-07 | 2026-06-05 | General statement, MVN verification (G6) | ratified_in_prior_work |
| D-08 | 2026-06-05 | Companion-document posture (statements here, proofs in derivation.qmd); 2026-06-06 note: three-tier — paper → appendices (protocol records; single-document upload) → companion + repo | **ratified** (2026-06-06, cycle 2) |
| D-09 | 2026-06-05 | IMRaD macro-structure with Methods-as-workflow; fourth (methodological) thesis component; rejected: 180e2b5 theory-paper shape with workflow as end-matter | **ratified** (in-chat); **amended 2026-06-06** (Amendment 1) |
| D-09-A1 | 2026-06-06 | Amendment 1 to D-09: Results umbrella split into M4a Derivations + M4b Simulation studies (subheads "Simulation studies: setup" / "Simulation studies: results"); arc is 6 moves; rejected: keeping the umbrella ("Results" a strained name for theorems; simulation design would crowd the workflow Methods) | **ratified** (in-chat, cycle 2) |
| D-10 | 2026-06-06 | Complete-data replication principle (term from the MI-IC companion) as the paper's organizing question, posed at three levels (estimates / criterion-in-expectation / decision rates); asserted-here, confirmed unposed in Schomaker–Heumann 2014; rejected: new "decision equivalence" coinage, unqualified rate-replication claim, IC-only scope | **ratified** (in-chat, cycle 2) |
| D-11 | 2026-06-06 | JAIGP provenance declaration lives in a title-page declaration block (AI lineage + role, ORCID-verified human prompter of record, repo + companion pointers) — the reader knows the paper's nature before page one; Discussion ends on the workflow reflection; rejected: standalone provenance section (180e2b5 S8), Discussion closing block, end-matter placement | **ratified** (in-chat, level2 cycle 1) |
| D-12 | 2026-06-06 | Level 3 authored FROM SCRATCH under the approved Level-2 blueprints, section-by-section drafting cycles; 180e2b5 is the QUARRY — verified material (displays, theorem statements, headline numbers, citation-backed sentences) lifted deliberately where a blueprint paragraph matches, never imported wholesale; mi-spectral.qmd frozen at 180e2b5 until the first compile; compile_enabled flips only when all six sections exist; the protocol's level3-decomposition target is retired for this paper; rejected: mechanical decomposition (~70% of paragraphs would need rewriting under the old framing anyway), full import-then-edit | **ratified** (in-chat) |
| D-13 | 2026-06-07 | The raw session transcripts (mi-spectral project only, 35 files 2026-05-22→) ENTER THE PUBLIC RECORD as provenance, to build trust; the committed collaboration analysis (todo/032 → verification/collaboration-analysis.md) is the citable summary S3-P2 rests on; MI-IC sessions are OUT of scope for the analysis; rejected: analysis-only publication (selective quotation invites the suspicion the protocol exists to dispel), cross-project scope (different paper, muddies the record) | **ratified** (in-chat) |

## Style and terminology

| id | date | decision | status |
|---|---|---|---|
| T-01 | 2026-06-05 | One RIV, normalized by I_obs; never conflate with the EM rate matrix / fraction-of-missing-information D | ratified_in_prior_work |
| T-02 | 2026-06-05 | Information convention: Kenward–Molenberghs unconditional (observed) information under MAR | ratified_in_prior_work |
| T-03 | 2026-06-05 | Banned vocabulary (manuscript and conversation): "ledger", "numerical witness", "tagged", "machine-checked", figurative jargon ("where it bites", "honest fences", "funnel/hub") | ratified_in_prior_work |
| T-04 | 2026-06-05 | Claims trust-ordered: firm first, measurements next, conjectures labeled | ratified_in_prior_work |
| T-05 | 2026-06-06 | Methods (M3) written factually in the passive voice — deliberate exception to the paper's general active-voice preference; the protocol is described as procedure, not narrated as achievement | ratified (in-chat, cycle 2) |
| T-06 | 2026-06-06 | Unresolved-status claims in the Introduction are typed: documented-open cited to the stating passage; asserted-here stated in the authors' voice and flagged as contribution | ratified (in-chat, cycle 2) |
| T-07 | 2026-06-06 | "Complete-data replication" (D-10) vs Monte Carlo repetitions: simulations say "repetitions", never "replications" | ratified (in-chat, cycle 2) |

## Per-section adjudications

(none yet — populated by the review loop)
