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
| D-14 | 2026-06-07 | Simulation-studies exhibits are committed PNG figures drawn by `verification/figures.R` from the gate-confirmed caches into `manuscript/figures/`, included in S5 via Quarto image syntax; the qmd stays a pure compile-from-JSON artifact and the figures carry their own provenance. Rejected: executable ggplot chunks in the qmd (adds an R-execution dependency to the manuscript build and breaks the level3-JSON-is-source invariant) | **ratified** (in-chat, todo/033) |

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
| T-08 | 2026-06-26 | Reader-facing prose: the complete-data sense of "oracle" -> "complete-data benchmark" (insider term; applied across S5 + G6 + S4-P21). The conditioning sense ("fitted-versus-oracle", the Q-function conditioned on the truth) is a distinct load-bearing derivation term, still present in S3-P6 / S4-P4 / S4-P7, pending a separate rename decision | ratified (in-chat, 2026-06-26) |

## Per-section adjudications

**S5 rebuild (2026-06-07, todo/033).** Setup became 11 per-study Methods blocks
(apparatus + grading + 8 study designs), each reproducible from the paragraph. Results
became 9 committed PNG figures plus the ladder selection table and a structural-limits
table, each carrying an explicit perfect reference (oracle / nominal level / analytic
target / y=x) and the achieved value. S5 grew 14 → 22 paragraphs (handoff anticipated
the growth). Three reconciliations made during the rebuild, flagged for Marcus's
per-paragraph review:

- The theorem-validation figure (`fig-w1-theorem`) draws from the preregistered
  `W1-prod-fiml*` caches, which are the source of the verified pooled `2.43 ± 0.26`, the
  target `2.77`, and the `N=1000` 2.6-se miss. The todo/033 inventory listed
  `phase1-w1/summary.csv` for this exhibit, but that re-run is a different design (3
  sample sizes, half-trace ≈ 2.63) and does not carry the registered numbers. The
  `W1-prod-fiml*` caches were NOT in the 2026-06-07 regeneration gate (only `run_all` and
  the ladder were) — a candidate to add to the pre-submission regen, cheap and
  deterministic.
- The non-nested per-candidate `(A)+(C)` levels were re-sourced from the committed
  `w4-dissimilar-summary.csv` (`lvl_diag ≈ 2.62`, `lvl_ar ≈ 2.85` under MAR, collapsing
  to `1.40` / `0.43` under MCAR). The previous prose's "+2.33 against +2.85" did not match
  any committed summary column; the figure and new prose use the committed values.
- Structural limits became a table rather than a figure (the three quantities are scalar
  limit-checks, not a headline comparison).

**S5 tribunal amendments (2026-06-26, cross-family adversarial review).** S5's simulation
claims were stress-tested by a cross-family tribunal (Claude + GPT-5.5 + Gemini via
`tkal-in-ket`; run `tkal-reviews/tribunal-20260627T014721Z/`). The harness defender had no
repository access and conceded everything; a repo-grounded defense + a cross-family press
round on it returned **verdict AMEND** — no result retracted, no headline number changed.
The two unanimous "blockers" were rebutted on the evidence: the W1 "goalpost" (pooled
2.43 +/- 0.26 has a 95% CI [1.93, 2.94] that *contains* the registered 2.77, and the
O(1) (A)+(C) term is independently derived and dated, todo/004 Amendment 2), and the
block-diagonal "luck" (the equality is already tabled; "overstates elsewhere" is proved
@prp-naive + measured in Study 8). The "hidden failure" charge was rebutted by todo/005
(uncongenial/MNAR registered observational, "no required pass"). Seven local edits applied:
S5-P12 W1 leading-order-anchor bridge ("consistent with" not "confirms"); S5-P15 52-sigma
localized to the engineered cell; S5-P17 W3C direction-not-mechanism; S5-P18/P19 two-sided
MCSE interval + named ncratio factors; S5-P20 moment-map decoupled from trace-formula
superiority; S5-P22 engine-sensitivity pointer tightened (phase6-info + phase2-w3); and a
NEW S6-P4b (G6) congeniality limit that fulfils the todo/005 H5 section-6 disclosure
commitment. Full record: `tkal-reviews/tribunal-20260627T014721Z/VERDICT-SYNTHESIS.md`.

## T-08 conditioning-sense rename (2026-06-27)

The conditioning-sense "oracle" (the Q-function conditioned on the truth, $\mathbb{E}[\ell_{\text{com}}\mid Y_{\text{obs}}]$ under the data-generating law, which no real procedure computes) is renamed to **"true-model expectation"** in S3-P6, S4-P4, and S4-P7. This completes T-08: the complete-data sense became "complete-data benchmark" (2026-06-26) and S5's "fitted-versus-oracle" became "fitted-model-versus-true-model". The word "oracle" no longer appears in level3 prose. (derivation.qmd, a separate sourced artifact, is out of scope for this prose pass and may retain its own usages.)

## Display-equation line-breaks (2026-06-27, todo/034 #1+2)

Wide display equations that overflowed the right text margin in the assembled preview (21 blocks across 11 paragraphs: S2-P13, S4-P10, S4-P11, S4-P19, S4-P20, S4-P3, S4-P4, S4-P5, S4-P6, S4-P7, S4-P7b) were broken at their relation symbols and comma/\qquad separators onto aligned lines (\begin{aligned}/\end{aligned}, one gathered list). This clears the xelatex Overfull \hbox warnings (worst was eq-lrt-bias at 112pt over) and the associated "equation renders as $$ / not given" symptom, which was clipping at the page edge, not malformed markup. Every mathematical token is preserved verbatim -- the edits only insert alignment ampersands and line breaks, verified by a normalize-and-compare check.

## Preview switched to the arXiv Quarto template (2026-06-27, todo/034 #4)

The visual preview build (manuscript/preview-jasa/build_preview.py) was switched
from the `jasa-pdf` format to the community arXiv format extension
**mikemahoney218/quarto-arxiv** (`arxiv-pdf`, LaTeX/xelatex, version 0.2.3),
installed with `quarto add mikemahoney218/quarto-arxiv`. Front matter adjusted to
that schema: the JASA `journal:` block dropped; `linenumbers`/`doublespacing`/
`runninghead` added; the D-11 provenance declaration moved from the (unsupported)
author `acknowledgements` slot to the title `\thanks{}` footnote (the `thanks:`
key), where the arxiv title partial renders it. Re-render: 0 Overfull \hbox
warnings (the wider arXiv text block also absorbed the lone remaining inline-math
overflow in S4-P11 that the JASA column clipped), and page count fell 55 -> 24.

Scope note: `manuscript/preview-jasa/` is gitignored (.gitignore:52), so the build
script and the installed extension live only in the local working tree -- this
record is the tracked trace of the choice. The eventual canonical compile
(scripts/compile_manuscript.py -> manuscript/mi-spectral.qmd, still
compile_enabled=false) should adopt `arxiv-pdf` when compile is enabled.
