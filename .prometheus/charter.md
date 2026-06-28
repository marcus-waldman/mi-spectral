---
schema_version: 1
project_id: d51ab9db-0748-44c5-ad94-2eee09e126f5
project_name: mi-spectral
status: active
current_milestone: "Per-paragraph annotation (Marcus passes) + compile-enablement -- the next milestone now that todo/035 is DONE"
last_synced_commit: 65642a5
tree_state: dirty
updated: "2026-06-28T04:58:40Z"
updated_by: wrap
supermemory_container: proj-d51ab9db-0748-44c5-ad94-2eee09e126f5
cockpit: { provider: null, list_id: null }
---








# Goal

A finite-M spectral correction for likelihood-based hypothesis tests under *congenial* multiple imputation (MI), with applications to likelihood-ratio model comparison and information-criterion model selection. Core result: the MI Q-function carries a deviance bias that decomposes as +1/2 * tr(RIV) (RIV = relative-increase-in-variance). It is an AI-assisted derivation with transparent, ORCID-verified human prompting, targeting JAIGP; every load-bearing claim is meant to be paired with a preregistered numerical witness. Predicted empirical signature: uncorrected MI-AIC misclassifications should concentrate on the highest-RIV candidate model -- confirmed (W3-C = 1.000) and adversarially reviewed.

# Current milestone

Prose-polish phase, then per-paragraph annotation + compile-enablement. This session (since the bdc5a3a wrap) ran a full **prose-quality arc** on top of todo/035: (1) a **vocabulary softening** from a manuscript-vs-literature log-odds diagnostic (`scripts/corpus_vocab_check.py`) -- the workflow/engineering-metaphor words over-represented vs the source corpus were plained down (sits->lies, gate->check, tier->grade, pipeline->sequence, graded->assessed, pinned->traced, lineage->family, sourced->checked-against-source); (2) an **accuracy / overclaim pass** (`scripts/overclaim_flag.py` scout + an adversarial workflow, 3 lenses proof/measurement/scope-skeptic): 16 suspects -> 15 confirmed 3/3, applied at 3d0d844 -- estimated-scale scope restored on the +1/2 tr(RIV) headline, "exactly" softened on measured/leading-order quantities, "at the null" restored on the LRT differential, "restores"->"substantially restores" on IC selection, and the workflow claims made honest (productive->active+human-directed, self-coding caveat, "is public"->"enters the public record"); (3) **punctuation budget v2** (the near-zero-connective rule had produced a monotone short-declarative column -- v2 encourages connectives and allows sparse semicolons; CLAUDE.md + check_plan gate updated); (4) a **cadence/style pass** (`scripts/cadence_flag.py` + per-paragraph rewrite + 3-lens adversarial verify): 45 paragraphs rewritten, corpus connective rate 0.07 -> 0.16/sentence. The **next chunk is todo/036**, a per-paragraph **tightening pass** (cut fluff, keep meaning) -- explicitly NOT a Workflow (Marcus: "problematic"), but with a single independent Agent-tool adversary per paragraph, human-gated. After todo/036: Marcus's annotation pass and compile-enablement. Branch `contributions-delphi-todo035`, head af2f22c, **unmerged/unpushed**; render clean (arxiv-pdf, 26 pp, 0 Overfull). check_plan green throughout.

# Milestones

The arc from start to the Goal. Mark each: `[x]` done - `[~]` current - `[ ]` upcoming.

- [x] Theory & derivation -- the +1/2*tr(RIV) deviance-bias decomposition (reframed after Chan 2022, AoS)
- [x] Preregistration of witness hypotheses (W1 theorem - W2 LRT power - W3 model selection)
- [x] Empirical validation runs executed (comprehensive sweep; W4 non-nested)
- [x] Proof of correctness -- formal propositions + CAS verification
- [x] Socratic review of the simulation evidence (S5) -- cross-family tribunal; verdict AMEND, no result retracted
- [x] Prose readability pass (S1-S6) -- 67/82 paragraphs rewritten, corpus FK 11.9 -> 10.1; T-08 closed; G6/G7 resolved (merged to main)
- [x] Rendering polish + AI-collaboration restructure (todo/034) -- equation line-breaks, figure legibility, arXiv template, new S1B section (D-12); MERGED to main (FF, f666dc2)
- [x] Contributions + applied-implications + abstract, Delphi-vetted (todo/035) -- Intro Contributions list (S1-P6b) + Discussion implications (S6-P7b) + tracked applied-first abstract; pool-then-axes Delphi (8/8 unanimous; 5/7/0); four-author title page (D-16); direct quotes paraphrased (D-17)
- [x] Prose-quality passes (this session): vocab softening (corpus_vocab_check), accuracy/overclaim audit (overclaim_flag + adversarial workflow, 15 fixes @ 3d0d844), punctuation budget v2 (99eca65), cadence/style pass (cadence_flag + per-paragraph rewrite, 45 paragraphs, connectives 0.07 -> 0.16/sentence)
- [~] todo/036 tightening pass -- per-paragraph, human-gated, single Agent-tool adversary per paragraph (NOT a Workflow); cut fluff, keep meaning, obey the standards
- [ ] Per-paragraph annotation (Marcus passes) + compile-enablement (port front matter into the compile path)
- [ ] Compile + derivation-audit (0 blocker/0 warn) + Zenodo deposit -> JAIGP submission

# Next 3 actions

1. **todo/036 tightening pass** (handoff committed at 65642a5): build `scripts/fluff_flag.py` (filler/empty-phrase scout, worst-first); per paragraph propose a tightened version + spawn ONE independent adversary via the Agent tool (charge: meaning/hedge/scope preserved, tighter-not-shorter, not over-tightened, v2/T-03 standards, cadence not regressed, token+newline guard); Marcus decides each. FIRST add a newline-structure guard to `scripts/apply_cadence_batch.py` (the token guard missed the literal-`\n` corruption that broke the render). Optionally fold in the 36 cadence-flagged paragraphs (softer cadence pass-3).
2. **Per-paragraph annotation (Marcus) + compile-enablement**: flip `compile_enabled`; port the front matter into the compile path -- title, the four-author block + affiliations + corresponding-author label, keywords (only in the gitignored build_preview.py; D-16 is the tracked trace); the abstract is already tracked in level3. Annotation discretionary items in Open questions.
3. **Branch hygiene**: merge `contributions-delphi-todo035` to main and push when Marcus signs off on the PDF. NOTE: main itself is unpushed -- the whole stack from `bf98d77` onward is unpushed. Then the final milestone: compile + derivation-audit 0/0 + Zenodo deposit + JAIGP submission.

# Decisions made

- Scope = congenial MI + regular likelihood only (non-congenial / FIML / EM are separate universes).
- Three witnesses (W1/W2/W3) + two applications (LRT, IC); Le Cam power-dominance demoted to a Discussion conjecture.
- Reframed after Chan (2022, AoS) to a deviance-bias decomposition *upstream* of test calibration (lineage: Rubin -> Meng-Rubin -> Chan -> this work).
- Bias = +tr(RIV) - 1/2*tr(RIV); the opposite-sign terms cancel in the sum -- reported honestly.
- Custom Cholesky for the one-zero-constrained MVN MLE -- ~25x faster than lavaan; made M=200 W2 feasible.
- Six-section IMRaD, no Conclusion; Methods in factual passive voice; each gate paragraph states what it cannot catch. (SUPERSEDED 2026-06-27 by D-12: arc is now 7 moves -- a new "AI-human collaboration" move sits between Introduction and Background; still no Conclusion.)
- AI-assisted derivation with ORCID-verified provenance per JAIGP; no hallucinated citations (every citekey backed by a locally-read PDF).
- Level-3 paragraphs are the prose source of truth -- never edit the rendered qmd directly once compile is enabled.
- TRUST GATE (2026-06-16): hard evidence must survive adversarial/Socratic scrutiny before it enters the manuscript -- every figure tied to the exact claim it proves, no confident-but-wrong AI narration over results.
- S5 SOCRATIC REVIEW DONE (2026-06-26): cross-family tribunal (Claude + GPT-5.5 + Gemini via tkal-in-ket) -> repo-grounded defense -> press round. Verdict AMEND; no result retracted, no headline number changed. The two unanimous "blockers" were rebutted on the evidence (W1 pooled 2.43+/-0.26 CI [1.93,2.94] CONTAINS the registered 2.77; block-diagonal "overstates elsewhere" proved @prp-naive + measured Study 8). Method note: the tkal tribunal defender has no repo access and concedes everything; the informative pattern is challenges -> repo-grounded defense -> press round. Run: tkal-reviews/tribunal-20260627T014721Z/.
- W3-C = 1.000 UNDER UNCONGENIALITY is genuine, not an artifact: a preregistered directional prediction (todo/005 H2/H5) that held across all 60 cells. "100% land on saturated" confirms the bias DIRECTION but does not discriminate the decomposition (nested RIV-ordering makes the saturated model the natural overfit sink; rescoped in S5-P17). Uncongenial behavior disclosed in the new S6 G7 congeniality limit.
- TERMINOLOGY T-08 (2026-06-26): "oracle" (complete-data sense) -> "complete-data benchmark" in reader-facing prose. CLOSED 2026-06-27 (Marcus): conditioning-sense "oracle" -> "true-model expectation" (S3-P6/S4-P4/S4-P7); "oracle" no longer in level3 prose; figures regenerated with "complete-data benchmark".
- PROSE READABILITY (2026-06-26): the manuscript must run the full high-school paragraph arc (topic -> support -> wrap), state logical steps plainly (redundancy acceptable), read at a lower grade level.
- READABILITY PASS EXECUTED (2026-06-27): 67/82 level3 paragraphs rewritten; corpus FK 11.9 -> 10.1, mean sentence length 15.2 -> 11.1. No number/claim/hedge/citation/cross-ref/figure markup changed (mechanically verified). Method (reusable): calibrate on one paragraph against Marcus's eye, then scale under a strict spec + a mechanical token-preservation verifier. Commit 675323a, merged to main.
- G-NUMBER COLLISION RESOLVED (2026-06-27): congeniality limit -> G7 (after MVN G6); collective range G1-G7.
- todo/034 EXECUTED (2026-06-27): all five items on branch rendering-restructure-todo034; MERGED to main (FF to f666dc2, unpushed). Equation line-breaks, figure legibility (margin legends + alpha + halos + Okabe-Ito), arXiv template (55->24 pp), new S1B section.
- D-12 AI-COLLABORATION RESTRUCTURE (2026-06-27, Marcus, AskUserQuestion): SPLIT -- new early section "AI-human collaboration" (sec-ai-collab, S1B, M1b) between Introduction and Background; takes the novelty framing + relocated roles material; Methods drops to five parts. Inserted as S1B with NO renumber of S2 onward.
- arXiv PREVIEW FORMAT (2026-06-27): preview uses mikemahoney218/quarto-arxiv (arxiv-pdf, xelatex). manuscript/preview-jasa/ is gitignored; decisions.md is the tracked trace; canonical compile adopts arxiv-pdf when compile_enabled flips.
- FIGURE LEGIBILITY APPROACH (2026-06-27): base-R figures get bottom-margin legends (margin_legend helper), alpha ~0.72 fills, white-halo value labels, one Okabe-Ito palette.
- INFRA BUG (2026-06-27): the check_citations pre-write hook misfires on Edit/Write of files in manuscript/ SUBDIRECTORIES and on ANY Edit/Write while the shell cwd sits in a subdir (it resolves <cwd>/.claude/hooks/...). Workaround: write via Bash, or `cd` back to repo root before an Edit/Write. Easy fix: resolve the hook path against repo root.
- todo/035 PLACEMENT (D-15, 2026-06-27, Marcus via AskUserQuestion): Intro Contributions enumeration (S1-P6b) + a Discussion "Implications for applied research" passage (S6-P7b) -- TWO units. The abstract is given a tracked home (level3 top-level `abstract`, consumed by build_preview.py) and leads with the applied hook.
- DELPHI VETTING DONE (2026-06-27, tkal-in-ket pool-then-axes; opus-4-8 / gpt-5.5-pro / gemini-3.1-pro): pool 8/8 unanimous at round 5; axes 5 unanimous / 7 majority / 0 split, all KEEP-WITH-REVISION. Workflow ratified FIRST-CLASS (self-coding caveat in-sentence); applied-first lead = the tr(RIV_k) IC correction; three IC items consolidated to two; 8-item set sufficient. Artifacts: tkal-reviews/delphi-{pool,axes}-*/.
- D-16 AUTHORSHIP (2026-06-27, Marcus): corresponding author Marcus Waldman, Department of Biostatistics and Informatics, University of Colorado Anschutz Medical Campus, marcus.waldman@cuanschutz.edu (was single-author / Univ. of Nebraska Medical Center). AI co-authors in order with parent-company affiliations: Claude Opus 4.7-4.8 (Anthropic), GPT-5.5 Pro (OpenAI), Gemini 3.1 Pro (Google). Corresponding-author label in the title \thanks{} footnote. YAML in gitignored build_preview.py; decisions.md D-16 is the tracked trace.
- D-17 NO DIRECT QUOTES (2026-06-27, Marcus): no verbatim quotation of other work anywhere in the manuscript prose -- paraphrase/summarize + cite the stating passage. Amends T-06; CLAUDE.md updated. Applied to S1-P2, S2-P8, S2-P10. Scope = main manuscript (level3); derivation.qmd (sourced-audit companion, D-08) OUT of scope.
- tkal-in-ket GOTCHA (2026-06-27, reusable): the claude provider's `thinking_budget` param sends `thinking.type.enabled`, which opus-4-8 REJECTS (drop it). The engine `.env` supplies all three API keys even when the process env lacks ANTHROPIC_API_KEY; `tkal preflight` is the definitive check; axes batches all axes per call.
- VOCAB SOFTENING (2026-06-27): `scripts/corpus_vocab_check.py` = manuscript-vs-literature weighted log-odds (Monroe). Priority 1+2 applied (bf5b853): the engineering-metaphor cluster over-represented vs the 61 source papers and absent from them was plained (sits->lies/stand/fall, gate->check, tier->grade, pipeline->sequence, graded->assessed, pinned->traced, lineage->model family, sourced->checked-against-source). `scope`/`transcripts` kept (false positives). T-03 banned-vocab scan clean (0).
- ABSTRACT 1ST SENTENCE FIX (2026-06-27, Marcus): "biased toward the models that lost the most data" was nonsensical -- models do not lose data (all candidates fit the SAME imputed data); the driver is model-specific tr(RIV). Replaced (53b96bc) with "Model selection on multiply imputed data is biased toward more complex models, because their larger relative increase in variance makes the fit look better than it is" -- keeps the cause on RIV.
- ACCURACY / OVERCLAIM PASS (2026-06-27): `scripts/overclaim_flag.py` scout (331 lexical candidates) + an adversarial workflow (per-section triage -> 3 diverse-lens verifiers proof/measurement/scope-skeptic, majority). 16 genuine suspects -> 15 confirmed 3/3, 1 cleared, 0 split; applied at 3d0d844. Each scoped to exactly what the proofs and measured results back: estimated-scale condition restored on the +1/2 tr(RIV) headline (S1-P4/S1-P6b/S6-P1; known-scale flips the sign), "exactly" -> "to leading order"/"we predict"/dropped on measured/leading-order quantities, "at the null" restored on the LRT differential (S1-P6), "restores" -> "substantially restores" on IC selection (0.17 weak-signal floor), and the workflow claims made defensible ("productive" -> "active and human-directed" (no solo baseline), self-coding caveat, "is public" -> "enters the public record" per D-13). Reusable: overclaim_flag.py + the workflow.
- PUNCTUATION BUDGET v2 (2026-06-27, Marcus): the v1 near-zero-connective rule forced every clause relationship into a period, leaving a monotone short-declarative column (and orphaned "it" pronouns). v2 (CLAUDE.md + check_plan gate, 99eca65): ENCOURAGE connectives between clauses (", because / , but / , so / , while / . However, / . Therefore,"); ALLOW semicolons but SPARSE (<=1 per paragraph, tightly-linked clauses, never a list); still BAN em-dash chains, nested glosses, list-semicolons; new "no orphaned pronouns" rule (name the noun). The check_plan prose gate now flags 2+ semicolons/paragraph and em-dashes, allows a single semicolon.
- CADENCE / STYLE PASS (2026-06-27): `scripts/cadence_flag.py` (monotony scout: length-uniformity, opener repetition, connective rate, orphan-pronoun openers) + per-paragraph rewrite + a 3-lens adversarial verify (fidelity/budget/cadence, accept only if all pass). 45 paragraphs rewritten (batch1 10 @ a1092bf, batch2 35 @ d6fc514); corpus connective rate 0.07 -> 0.16/sentence, sentence count 1101 -> 909. 36 paragraphs flagged by the strict cadence lens (not applied), S4-P6 skipped (token guard). GOTCHA: the rewrite agents emitted literal `\n` (backslash-n) for real newlines at heading/image boundaries in S4-P2/S5-P1/S5-P21, which broke the render (undefined control sequence) because the token guard checks math/numbers/citations NOT newline structure; fixed at af2f22c, and todo/036 must ADD a newline-structure guard to apply_cadence_batch.py.
- WORKFLOW PALATABILITY (2026-06-27, Marcus): the multi-agent Workflow tool is "problematic" for prose passes -- opaque auto-reject (36 paragraphs flagged invisibly), batch auto-apply, the `\n` corruption it hid, and an args-stringification bug that forced hardcoded id lists. For the tightening pass (todo/036) use per-paragraph human-in-the-loop with a SINGLE independent adversary via the Agent tool (NOT Workflow); the human is the gate, the adversary only surfaces objections.
- RENDER GOTCHA (2026-06-27, Marcus): a slow preview render is a one-time tinytex `tlmgr` package update over the network (log: "updating tlmgr"; a `curl` child is the tell). LET IT FINISH (background it so the 2-min tool timeout doesn't kill it); do NOT kill it mid-update or hand-roll a direct xelatex/.tex compile (Marcus called that churn "unhealthy"; killing it mid-update also makes the next render re-run it). Memory: feedback_render_use_standard_quarto.

# Open questions

- The 36 cadence-flagged paragraphs (strict cadence lens rejected, not applied) -- fold a softer cadence "pass-3" into todo/036 tightening, or skip. Ids in todo/036.
- Whether to version-control the gitignored preview build (build_preview.py + the arXiv extension + the four-author front matter) so the arXiv setup is reproducible, or keep local-only (decisions.md D-11/D-16 are the tracked traces). Load-bearing at compile-enablement, when the front matter must be ported.
- Discretionary items for Marcus's annotation pass: (a) trim S1-P6's inline "five new things" enumeration if redundant with the new S1-P6b Contributions list (note: S1-P6's "exact differential bias" gained "at the null" in the accuracy pass); (b) applied-first contributions ordering (IC correction leads, theorem second) -- keep or flip; (c) the workflow first-class framing carries GPT-5.5's minority "supporting unless caveat prominent" as the in-sentence self-coding caveat -- confirm.
- Real-data demonstration (HRS wealth components vs NHANES lipids) -- defer unless the manuscript stalls or a reviewer requests it.
- Formalize the (correct but informal) MI-IC v4.5 derivation as an appendix theorem, generalized to arbitrary regular-likelihood models.
- Optional citation backlog (White 2011, Grund 2021, Schomaker 2007) -- none load-bearing.

(Resolved this session, moved to Decisions made: the whole prose-quality arc -- vocab softening, the abstract first-sentence fix, the accuracy/overclaim pass (15 fixes), punctuation budget v2, and the cadence/style pass (45 paragraphs); plus the workflow-palatability and render gotchas. The tightening pass is now queued as todo/036 with a committed handoff.)
