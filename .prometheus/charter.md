---
schema_version: 1
project_id: d51ab9db-0748-44c5-ad94-2eee09e126f5
project_name: mi-spectral
status: active
current_milestone: "Rendering polish + new 'AI human collaboration' section (todo/034): equation line-breaks, figure legibility (legends outside + transparency + palette), arXiv template, restructure -- prose readability pass DONE (FK 11.9->10.1; T-08 closed; G6/G7 fixed)"
last_synced_commit: bf98d77
tree_state: dirty
updated: "2026-06-27T17:17:31Z"
updated_by: wrap
supermemory_container: proj-d51ab9db-0748-44c5-ad94-2eee09e126f5
cockpit: { provider: null, list_id: null }
---







# Goal

A finite-M spectral correction for likelihood-based hypothesis tests under *congenial* multiple imputation (MI), with applications to likelihood-ratio model comparison and information-criterion model selection. Core result: the MI Q-function carries a deviance bias that decomposes as +1/2 * tr(RIV) (RIV = relative-increase-in-variance). It is an AI-assisted derivation with transparent, ORCID-verified human prompting, targeting JAIGP; every load-bearing claim is meant to be paired with a preregistered numerical witness. Predicted empirical signature: uncorrected MI-AIC misclassifications should concentrate on the highest-RIV candidate model -- confirmed (W3-C = 1.000) and adversarially reviewed.

# Current milestone

Contributions + applied-implications subsection, Delphi-vetted (todo/035), then abstract + Discussion-close updates -- the next chunk before per-paragraph annotation and compile-enablement. The rendering-polish + AI-collaboration milestone (todo/034) is DONE: all five items executed on branch `rendering-restructure-todo034` (5 commits, **unmerged, unpushed**). (1) 21 wide display equations broken into aligned/gathered lines -- display Overfull \hbox 4 -> 0 (the "renders as $$" symptom was overflow-clipping, not bad markup). (2) figures.R re-styled -- legends moved OUTSIDE the plot into the bottom margin, alpha on every point/bar fill, white-halo value labels, one Okabe-Ito palette, and oracle -> "complete-data benchmark" (T-08); all 9 PNGs regenerated. (3) preview switched to the arXiv Quarto template (mikemahoney218/quarto-arxiv, arxiv-pdf) -- D-11 declaration moved to the title \thanks{} footnote, pages 55 -> 24, 0 Overfull. (4) new "AI-human collaboration" section (S1B / sec-ai-collab) inserted between Introduction and Background per Marcus's SPLIT + no-renumber decision (D-12) -- all four plan JSONs updated, check_plan green, renders as section 2. Next, per todo/035: add a "Contributions and implications for applied research" subsection (applied skim-hook; the structured AI-human workflow/provenance is a first-class contribution), vet the contributions through a tkal-in-ket Delphi, then update the abstract and the Discussion close.

# Milestones

The arc from start to the Goal. Mark each: `[x]` done - `[~]` current - `[ ]` upcoming.

- [x] Theory & derivation -- the +1/2*tr(RIV) deviance-bias decomposition (reframed after Chan 2022, AoS)
- [x] Preregistration of witness hypotheses (W1 theorem - W2 LRT power - W3 model selection)
- [x] Empirical validation runs executed (comprehensive sweep; W4 non-nested)
- [x] Proof of correctness -- formal propositions + CAS verification
- [x] Socratic review of the simulation evidence (S5) -- done as a cross-family tribunal; verdict AMEND, no result retracted (the "off" figure was claim-overreach, not a plotting bug)
- [x] Prose readability pass (S1-S6) -- 67/82 paragraphs rewritten, corpus FK 11.9 -> 10.1; T-08 conditioning-sense "oracle" closed; G6/G7 collision resolved (commits 675323a + d3aa962, merged to main)
- [x] Rendering polish + AI-collaboration restructure (todo/034) -- equation line-breaks (4->0 overflow), figure legibility (legends outside + alpha + halos + Okabe-Ito + oracle->benchmark), arXiv template (55->24 pp), and the new S1B "AI-human collaboration" section (D-12); branch rendering-restructure-todo034, unmerged/unpushed
- [~] Contributions + applied-implications subsection, Delphi-vetted (todo/035) -- add a "Contributions and implications for applied research" subsection (workflow/provenance a first-class contribution), vet via a tkal-in-ket Delphi, then update the abstract + Discussion close
- [ ] Per-paragraph annotation (Marcus passes) + compile-enablement (port front matter into level3 metadata)
- [ ] Compile + derivation-audit (0 blocker/0 warn) + Zenodo deposit -> JAIGP submission

# Next 3 actions

1. todo/035 decisions (confirm at session start): placement of the subsection (Discussion default vs end-of-Intro contributions list vs both), one subsection vs two, Delphi mode (pool default vs axes vs pool-then-axes), and whether the abstract gets a tracked home now or waits for compile-enablement. Then draft the candidate contributions brief (seed list in todo/035; the workflow/provenance contribution foregrounded).
2. Run the tkal-in-ket Delphi on the contributions -- self-contained grounded brief (each claim + its evidence; the panel has no repo access), needs ANTHROPIC_/OPENAI_/GEMINI_API_KEY. Then write the subsection from the converged set, update the abstract + Discussion close, check_plan, rebuild the arXiv preview, show Marcus.
3. Then the per-paragraph annotation (Marcus passes) + compile-enablement milestone. (Branch hygiene: merge rendering-restructure-todo034 to main when ready -- it is unmerged/unpushed.)

# Decisions made

- Scope = congenial MI + regular likelihood only (non-congenial / FIML / EM are separate universes).
- Three witnesses (W1/W2/W3) + two applications (LRT, IC); Le Cam power-dominance demoted to a Discussion conjecture.
- Reframed after Chan (2022, AoS) to a deviance-bias decomposition *upstream* of test calibration (lineage: Rubin -> Meng-Rubin -> Chan -> this work).
- Bias = +tr(RIV) - 1/2*tr(RIV); the opposite-sign terms cancel in the sum -- reported honestly.
- Custom Cholesky for the one-zero-constrained MVN MLE -- ~25x faster than lavaan; made M=200 W2 feasible (timing claim to verify in the Socratic review).
- Six-section IMRaD, no Conclusion; Methods in factual passive voice; each gate paragraph states what it cannot catch. (SUPERSEDED 2026-06-27 by D-12: arc is now 7 moves -- a new "AI-human collaboration" move sits between Introduction and Background; still no Conclusion.)
- AI-assisted derivation with ORCID-verified provenance per JAIGP; no hallucinated citations (every citekey backed by a locally-read PDF).
- Level-3 paragraphs are the prose source of truth -- never edit the rendered qmd directly once compile is enabled.
- TRUST GATE (2026-06-16): hard evidence must survive adversarial/Socratic scrutiny before it enters the manuscript -- every figure tied to the exact claim it proves, no confident-but-wrong AI narration over results. Triggered by S5 evidence that was unconvincing/mis-explained, with a figure that looked clearly off.
- S5 SOCRATIC REVIEW DONE (2026-06-26): run as a cross-family tribunal (Claude + GPT-5.5 + Gemini via tkal-in-ket) -> repo-grounded defense -> cross-family press round. Verdict AMEND; no result retracted, no headline number changed. The two unanimous "blockers" were rebutted on the evidence (W1 pooled 2.43+/-0.26 has a 95% CI [1.93,2.94] that CONTAINS the registered 2.77; block-diagonal "overstates elsewhere" is proved @prp-naive + measured in Study 8). The figure that "looked clearly off" was claim-overreach in wording, not a plotting/scaling bug -- fixed by 7 local amendments + a new S6 G6 congeniality limit. Method note: the tkal tribunal defender has no repo access and concedes everything; the informative pattern is challenges -> repo-grounded defense -> press round. Run: tkal-reviews/tribunal-20260627T014721Z/.
- W3-C = 1.000 UNDER UNCONGENIALITY is genuine, not an artifact (resolves the prior open question): it was a preregistered directional prediction (todo/005 H2/H5, registered observational, expected to drop) that held across all 60 cells. But "100% land on saturated" confirms the bias DIRECTION; it does not discriminate the specific decomposition, because the nested RIV-ordering makes the saturated model the natural overfit sink (rescoped in S5-P17). The uncongenial behavior (uncorrected exceeds the complete-data benchmark; the correction overshoots past it) is now disclosed in the new S6 G6 congeniality limit.
- TERMINOLOGY T-08 (2026-06-26): "oracle" (complete-data sense) -> "complete-data benchmark" in reader-facing prose, applied across S5 + G6 + S4-P21. The conditioning sense ("fitted-versus-oracle", the Q-function conditioned on the truth) is a distinct load-bearing term still in S3-P6 / S4-P4 / S4-P7, pending a separate rename (see Open questions).
- PROSE READABILITY (2026-06-26): the manuscript must run the full high-school paragraph arc (topic sentence -> supporting details -> wrap-up/hand-off), state logical steps plainly rather than forcing inference (redundancy acceptable), and read at a lower grade level. Why: reading the full assembled PDF showed the existing cadence/punctuation rules were not enough -- the prose still demands inference and runs high.
- READABILITY PASS EXECUTED (2026-06-27): 67/82 level3 paragraphs rewritten for the arc; corpus FK 11.9 -> 10.1, mean sentence length 15.2 -> 11.1; S3 (already FK 8.4) and the cleanest S1/S2 paragraphs left as-is. No number, claim, hedge, citation, cross-ref, or figure markup changed -- mechanically verified (math/ref/figure-token multisets preserved on all 67; prose punctuation gate 0 hits) and all 22 S5 rewrites read against originals for claim drift. Method (reusable): calibrate on one paragraph against Marcus's eye, then scale via per-section subagents under a strict spec + a mechanical token-preservation verifier; S5 (tribunal-fresh) authored/reviewed by the main agent. Commit 675323a, merged to main.
- T-08 CLOSED (2026-06-27, Marcus): conditioning-sense "oracle" -> "true-model expectation" (S3-P6/S4-P4/S4-P7), consistent with the S5 "fitted-model-versus-true-model" rename. "oracle" no longer appears in level3 prose. Note: figure legends in verification/figures.R still say "oracle" -- to be renamed when figures are regenerated (todo/034 item 3). (DONE 2026-06-27: figures regenerated with "complete-data benchmark".)
- G-NUMBER COLLISION RESOLVED (2026-06-27, Marcus): the tribunal-added congeniality limit (S6-P4b) was provisionally G6, colliding with the MVN-instantiation limit (S6-P4, G6). Resolution: congeniality -> G7 (it sits after MVN in the text), MVN keeps G6, and the collective range G1-G6 -> G1-G7 in level1/level2.
- NEW WORK CHUNK from Marcus's PDF read (2026-06-27): rendering polish + a foregrounded AI-collaboration section, captured in todo/034 (equation line-breaks; figures legends-outside + transparency + coherent palette; arXiv Quarto template; new "AI human collaboration" section between Intro and Background that states the AI-era novelty and the "productive AND accurate workflow" goal). Why: the assembled PDF still has equation overflow + figure-legibility problems, and the AI-human-workflow material deserves a dedicated, up-front section rather than being scattered across Intro/Methods/Discussion.
- todo/034 EXECUTED (2026-06-27): all five items done on branch `rendering-restructure-todo034` (commits afb658e #1+2 equations, 49b8c43 #3 figures, 60e72a5 #4 arXiv, 79b1e85 #5 section; bf98d77 = todo/035 handoff). check_plan green throughout; arXiv preview clean (0 Overfull, 26 pp). Unmerged, unpushed.
- D-12 AI-COLLABORATION RESTRUCTURE (2026-06-27, Marcus, via AskUserQuestion): SPLIT -- the new early section "AI-human collaboration" (anchor sec-ai-collab, internal id S1B, arc move M1b) takes the narrative/novelty framing (AI-human collaboration is a novelty in the age of AI; a stated goal is a workflow that is both productive AND yields accurate conclusions) plus the roles material relocated from the Methods opener (old S3-P2), while Methods keeps the operational verification detail and drops from six parts to five. Inserted as S1B with NO renumber of S2 onward (reader-facing section numbers are auto-generated by Quarto from order). Why split: moving all workflow material forward would leave Methods thin and put procedure before the Background the reader needs. Resolves the prior open question.
- arXiv PREVIEW FORMAT (2026-06-27): the visual preview uses mikemahoney218/quarto-arxiv (arxiv-pdf, xelatex). Note: manuscript/preview-jasa/ is gitignored, so build_preview.py and the installed extension are local-only; decisions.md is the tracked trace. The canonical compile should adopt arxiv-pdf when compile_enabled flips.
- FIGURE LEGIBILITY APPROACH (2026-06-27): base-R figures get legends in the bottom margin via a margin_legend() helper (par("fig") + grconvert + xpd=NA), alpha (~0.72) on point/bar fills, white-halo value labels (halo_text()) so labels read through bars/bands/lines, and one Okabe-Ito palette. Why: Marcus's read showed legends overlapping data and labels camouflaged against fills.
- INFRA BUG (2026-06-27): the check_citations pre-write hook (.claude/hooks/check_citations.py) misfires on Edit/Write of files in manuscript/ SUBDIRECTORIES -- it resolves its script path against the edited file's directory and errors out (not a real citation block). Workaround used all session: write manuscript/ files via Bash (heredoc, or Write to scratchpad then run + cp). Easy fix: resolve the hook path against repo root.
- NEXT WORK CHUNK (2026-06-27, Marcus): todo/035 -- a Delphi-vetted "Contributions and implications for applied research" subsection (so skimming applied researchers find the work important), with the structured AI-human workflow/collaboration-with-provenance credited as a first-class contribution; then update the abstract and the Discussion close. The contributions go through a tkal-in-ket Delphi before finalizing. Comes BEFORE the annotation + compile-enablement milestone.

# Open questions

- todo/035 DECISIONS needed from Marcus (confirm at session start): (a) placement of the "Contributions and implications for applied research" subsection -- a subsection in the Discussion (proposed default) vs a Contributions enumeration at the end of the Introduction vs both; (b) one subsection (contributions + implications) vs two; (c) Delphi mode -- pool (proposed default, converge the set) vs axes (ratify each per criterion) vs pool-then-axes; (d) does the abstract get a tracked home now or wait for compile-enablement (it currently lives only in the gitignored build_preview.py front matter).
- Whether to version-control the gitignored preview build (build_preview.py + the installed arXiv extension) so the arXiv setup is reproducible, or keep the preview dir local-only (the established convention).
- Real-data demonstration (HRS wealth components vs NHANES lipids) -- defer unless the manuscript stalls or a reviewer requests it.
- Formalize the (correct but informal) MI-IC v4.5 derivation as an appendix theorem, generalized to arbitrary regular-likelihood models.
- Optional citation backlog (White 2011, Grund 2021, Schomaker 2007) -- none load-bearing.

(Resolved this session, moved to Decisions made: the AI-collaboration restructure split/numbering -- Marcus chose SPLIT + insert as S1B with no renumber (D-12); and todo/034 was fully executed across all five items.)
