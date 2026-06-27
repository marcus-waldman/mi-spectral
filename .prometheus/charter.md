---
schema_version: 1
project_id: d51ab9db-0748-44c5-ad94-2eee09e126f5
project_name: mi-spectral
status: active
current_milestone: "Rendering polish + new 'AI human collaboration' section (todo/034): equation line-breaks, figure legibility (legends outside + transparency + palette), arXiv template, restructure -- prose readability pass DONE (FK 11.9->10.1; T-08 closed; G6/G7 fixed)"
last_synced_commit: cd9cc3a
tree_state: dirty
updated: "2026-06-27T14:39:54Z"
updated_by: wrap
supermemory_container: proj-d51ab9db-0748-44c5-ad94-2eee09e126f5
cockpit: { provider: null, list_id: null }
---






# Goal

A finite-M spectral correction for likelihood-based hypothesis tests under *congenial* multiple imputation (MI), with applications to likelihood-ratio model comparison and information-criterion model selection. Core result: the MI Q-function carries a deviance bias that decomposes as +1/2 * tr(RIV) (RIV = relative-increase-in-variance). It is an AI-assisted derivation with transparent, ORCID-verified human prompting, targeting JAIGP; every load-bearing claim is meant to be paired with a preregistered numerical witness. Predicted empirical signature: uncorrected MI-AIC misclassifications should concentrate on the highest-RIV candidate model -- confirmed (W3-C = 1.000) and adversarially reviewed.

# Current milestone

Rendering polish + a new "AI human collaboration" section (todo/034), before annotation and compile. The prose readability pass is DONE: 67 of 82 level3 paragraphs rewritten to the topic/support/wrap arc, corpus Flesch-Kincaid grade 11.9 -> 10.1, mean sentence length 15.2 -> 11.1, with numbers/claims/citations mechanically verified and all S5 rewrites read for claim drift (commit 675323a, merged to main). Reading the assembled JASA preview then surfaced the next batch of work, captured in todo/034: (1) long display equations run off the page -- break at commas onto new lines; (2) some equations render as literal "$$" / not given (balanced math confirmed, so overflow or blank-line separation); (3) figures (verification/figures.R, base R) need legends OUTSIDE the plot area, slight transparency on points/bars so camouflaged labels read through, a coherent color scheme, and the stale "oracle" legend labels renamed to "complete-data benchmark" (T-08); (4) switch the preview to an arXiv Quarto format extension; (5) pull the AI-human-workflow material into a NEW "AI human collaboration" section between Introduction and Background, making explicit that this is a novelty in the age of AI and that a stated goal is a workflow that is both productive AND yields accurate conclusions.

# Milestones

The arc from start to the Goal. Mark each: `[x]` done - `[~]` current - `[ ]` upcoming.

- [x] Theory & derivation -- the +1/2*tr(RIV) deviance-bias decomposition (reframed after Chan 2022, AoS)
- [x] Preregistration of witness hypotheses (W1 theorem - W2 LRT power - W3 model selection)
- [x] Empirical validation runs executed (comprehensive sweep; W4 non-nested)
- [x] Proof of correctness -- formal propositions + CAS verification
- [x] Socratic review of the simulation evidence (S5) -- done as a cross-family tribunal; verdict AMEND, no result retracted (the "off" figure was claim-overreach, not a plotting bug)
- [x] Prose readability pass (S1-S6) -- 67/82 paragraphs rewritten, corpus FK 11.9 -> 10.1; T-08 conditioning-sense "oracle" closed; G6/G7 collision resolved (commits 675323a + d3aa962, merged to main)
- [~] Rendering polish + AI-collaboration restructure (todo/034) -- equation line-breaks, figure legibility (legends outside + transparency + palette), arXiv template, and a new "AI human collaboration" section between Intro and Background
- [ ] Per-paragraph annotation (Marcus passes) + compile-enablement (port front matter into level3 metadata)
- [ ] Compile + derivation-audit (0 blocker/0 warn) + Zenodo deposit -> JAIGP submission

# Next 3 actions

1. todo/034 items 1+2 (equations): break the ~21 long display blocks (worst: S4-P4/P5/P7/P10/P20) at commas/`\qquad` onto new lines via `aligned`/`split` with `\\`, tokens preserved; re-render and confirm the "$$"-not-given symptom clears (check the xelatex `Overfull \hbox` log).
2. todo/034 item 3 (figures, verification/figures.R, base R): legends outside the plot area (par(mar/oma) + xpd=NA), slight alpha on points/bars, one coherent palette, and rename the "oracle (perfect)" legends to "complete-data benchmark" (T-08); then item 4 -- find + `quarto add` an arXiv format extension and swap build_preview.py's `jasa-pdf` front matter.
3. todo/034 item 5 (restructure): AFTER Marcus answers the split/numbering question, add the "AI human collaboration" section (source: S1-P7, S3-P1/P2/P3/P8, S6-P8), making the AI-era novelty + productive-and-accurate-workflow goal explicit; update sections_order + level1/level2/level3 + deps; check_plan; rebuild preview. Then the annotation + compile-enablement milestone.

# Decisions made

- Scope = congenial MI + regular likelihood only (non-congenial / FIML / EM are separate universes).
- Three witnesses (W1/W2/W3) + two applications (LRT, IC); Le Cam power-dominance demoted to a Discussion conjecture.
- Reframed after Chan (2022, AoS) to a deviance-bias decomposition *upstream* of test calibration (lineage: Rubin -> Meng-Rubin -> Chan -> this work).
- Bias = +tr(RIV) - 1/2*tr(RIV); the opposite-sign terms cancel in the sum -- reported honestly.
- Custom Cholesky for the one-zero-constrained MVN MLE -- ~25x faster than lavaan; made M=200 W2 feasible (timing claim to verify in the Socratic review).
- Six-section IMRaD, no Conclusion; Methods in factual passive voice; each gate paragraph states what it cannot catch.
- AI-assisted derivation with ORCID-verified provenance per JAIGP; no hallucinated citations (every citekey backed by a locally-read PDF).
- Level-3 paragraphs are the prose source of truth -- never edit the rendered qmd directly once compile is enabled.
- TRUST GATE (2026-06-16): hard evidence must survive adversarial/Socratic scrutiny before it enters the manuscript -- every figure tied to the exact claim it proves, no confident-but-wrong AI narration over results. Triggered by S5 evidence that was unconvincing/mis-explained, with a figure that looked clearly off.
- S5 SOCRATIC REVIEW DONE (2026-06-26): run as a cross-family tribunal (Claude + GPT-5.5 + Gemini via tkal-in-ket) -> repo-grounded defense -> cross-family press round. Verdict AMEND; no result retracted, no headline number changed. The two unanimous "blockers" were rebutted on the evidence (W1 pooled 2.43+/-0.26 has a 95% CI [1.93,2.94] that CONTAINS the registered 2.77; block-diagonal "overstates elsewhere" is proved @prp-naive + measured in Study 8). The figure that "looked clearly off" was claim-overreach in wording, not a plotting/scaling bug -- fixed by 7 local amendments + a new S6 G6 congeniality limit. Method note: the tkal tribunal defender has no repo access and concedes everything; the informative pattern is challenges -> repo-grounded defense -> press round. Run: tkal-reviews/tribunal-20260627T014721Z/.
- W3-C = 1.000 UNDER UNCONGENIALITY is genuine, not an artifact (resolves the prior open question): it was a preregistered directional prediction (todo/005 H2/H5, registered observational, expected to drop) that held across all 60 cells. But "100% land on saturated" confirms the bias DIRECTION; it does not discriminate the specific decomposition, because the nested RIV-ordering makes the saturated model the natural overfit sink (rescoped in S5-P17). The uncongenial behavior (uncorrected exceeds the complete-data benchmark; the correction overshoots past it) is now disclosed in the new S6 G6 congeniality limit.
- TERMINOLOGY T-08 (2026-06-26): "oracle" (complete-data sense) -> "complete-data benchmark" in reader-facing prose, applied across S5 + G6 + S4-P21. The conditioning sense ("fitted-versus-oracle", the Q-function conditioned on the truth) is a distinct load-bearing term still in S3-P6 / S4-P4 / S4-P7, pending a separate rename (see Open questions).
- PROSE READABILITY (2026-06-26): the manuscript must run the full high-school paragraph arc (topic sentence -> supporting details -> wrap-up/hand-off), state logical steps plainly rather than forcing inference (redundancy acceptable), and read at a lower grade level. Why: reading the full assembled PDF showed the existing cadence/punctuation rules were not enough -- the prose still demands inference and runs high.
- READABILITY PASS EXECUTED (2026-06-27): 67/82 level3 paragraphs rewritten for the arc; corpus FK 11.9 -> 10.1, mean sentence length 15.2 -> 11.1; S3 (already FK 8.4) and the cleanest S1/S2 paragraphs left as-is. No number, claim, hedge, citation, cross-ref, or figure markup changed -- mechanically verified (math/ref/figure-token multisets preserved on all 67; prose punctuation gate 0 hits) and all 22 S5 rewrites read against originals for claim drift. Method (reusable): calibrate on one paragraph against Marcus's eye, then scale via per-section subagents under a strict spec + a mechanical token-preservation verifier; S5 (tribunal-fresh) authored/reviewed by the main agent. Commit 675323a, merged to main.
- T-08 CLOSED (2026-06-27, Marcus): conditioning-sense "oracle" -> "true-model expectation" (S3-P6/S4-P4/S4-P7), consistent with the S5 "fitted-model-versus-true-model" rename. "oracle" no longer appears in level3 prose. Note: figure legends in verification/figures.R still say "oracle" -- to be renamed when figures are regenerated (todo/034 item 3).
- G-NUMBER COLLISION RESOLVED (2026-06-27, Marcus): the tribunal-added congeniality limit (S6-P4b) was provisionally G6, colliding with the MVN-instantiation limit (S6-P4, G6). Resolution: congeniality -> G7 (it sits after MVN in the text), MVN keeps G6, and the collective range G1-G6 -> G1-G7 in level1/level2.
- NEW WORK CHUNK from Marcus's PDF read (2026-06-27): rendering polish + a foregrounded AI-collaboration section, captured in todo/034 (equation line-breaks; figures legends-outside + transparency + coherent palette; arXiv Quarto template; new "AI human collaboration" section between Intro and Background that states the AI-era novelty and the "productive AND accurate workflow" goal). Why: the assembled PDF still has equation overflow + figure-legibility problems, and the AI-human-workflow material deserves a dedicated, up-front section rather than being scattered across Intro/Methods/Discussion.

# Open questions

- AI-COLLABORATION RESTRUCTURE -- decision needed from Marcus (todo/034 item 5): how to split the new "AI human collaboration" section against S3 ("Methods: the derivation and verification workflow"), which it overlaps. Does the new early section take the narrative/novelty framing (why AI-human collaboration, the productivity+accuracy goal, roles, provenance) while S3 keeps the operational methods detail, or does the whole workflow material move forward? And the section numbering/anchor scheme (new id like S1B / anchor sec-ai-collab, vs renumber S2 onward)?
- Real-data demonstration (HRS wealth components vs NHANES lipids) -- defer unless the manuscript stalls or a reviewer requests it.
- Formalize the (correct but informal) MI-IC v4.5 derivation as an appendix theorem, generalized to arbitrary regular-likelihood models.
- Optional citation backlog (White 2011, Grund 2021, Schomaker 2007) -- none load-bearing.

(Resolved this session, moved to Decisions made: the conditioning-sense "oracle" rename -- Marcus chose "true-model expectation" (T-08 closed); and the G6/G7 numbering collision -- congeniality -> G7, MVN keeps G6.)
