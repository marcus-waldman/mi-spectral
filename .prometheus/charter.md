---
schema_version: 1
project_id: d51ab9db-0748-44c5-ad94-2eee09e126f5
project_name: mi-spectral
status: active
current_milestone: "Socratic review of the S5 simulation evidence -- does each figure actually prove its claim? (confidence gate before more drafting)"
last_synced_commit: a3b3da6
tree_state: dirty
updated: "2026-06-27T04:32:38Z"
updated_by: wrap
supermemory_container: proj-d51ab9db-0748-44c5-ad94-2eee09e126f5
cockpit: { provider: null, list_id: null }
---



# Goal

A finite-M spectral correction for likelihood-based hypothesis tests under *congenial* multiple imputation (MI), with applications to likelihood-ratio model comparison and information-criterion model selection. Core result: the MI Q-function carries a deviance bias that decomposes as +1/2 * tr(RIV) (RIV = relative-increase-in-variance). It is an AI-assisted derivation with transparent, ORCID-verified human prompting, targeting JAIGP; every load-bearing claim is meant to be paired with a preregistered numerical witness. Predicted empirical signature: uncorrected MI-AIC misclassifications should concentrate on the highest-RIV candidate model -- confirmed (W3-C = 1.000) and adversarially reviewed.

# Current milestone

Prose readability pass over the whole manuscript, before compile and submission. The S5 Socratic review is COMPLETE: it ran as a cross-family tribunal (Claude + GPT-5.5 + Gemini) with a repo-grounded defense and a press round, returning verdict AMEND -- no result retracted, no headline number changed, and the figure that looked clearly off was claim-overreach in wording, not a plotting or scaling bug. Reading the full manuscript in PDF then surfaced the next gate: the prose still demands inference and reads above grade level. Every paragraph (level3 draft_prose, S1-S6) must run a clear topic-sentence -> supporting-details -> wrap-up/hand-off arc, state each logical step plainly even at the cost of a little redundancy, and read at a lower grade level.

# Milestones

The arc from start to the Goal. Mark each: `[x]` done - `[~]` current - `[ ]` upcoming.

- [x] Theory & derivation -- the +1/2*tr(RIV) deviance-bias decomposition (reframed after Chan 2022, AoS)
- [x] Preregistration of witness hypotheses (W1 theorem - W2 LRT power - W3 model selection)
- [x] Empirical validation runs executed (comprehensive sweep; W4 non-nested)
- [x] Proof of correctness -- formal propositions + CAS verification
- [x] Socratic review of the simulation evidence (S5) -- done as a cross-family tribunal; verdict AMEND, no result retracted (the "off" figure was claim-overreach, not a plotting bug)
- [~] Prose readability pass (S1-S6) -- per-paragraph rewrite for the topic/support/wrap arc, plain statements, lower grade level
- [ ] Per-paragraph annotation (Marcus passes) + compile-enablement (port front matter into level3 metadata)
- [ ] Compile + derivation-audit (0 blocker/0 warn) + Zenodo deposit -> JAIGP submission

# Next 3 actions

1. Prose readability pass over level3 draft_prose (S1-S6): per-paragraph rewrite to the topic-sentence -> supporting-details -> wrap-up/hand-off arc; unpack compressed inferences into explicit plain sentences (a little redundancy is fine); lower sentence complexity / grade level (measure Flesch-Kincaid before/after). Includes today's S5 amendments (some, e.g. S5-P12/P20, are dense). Then regenerate the JASA preview to re-read in manuscript form.
2. Merge branch `s5-tribunal-amendments` into main (commits 2b10f67 S5 amendments + a3b3da6 readability directive); resolve the deferred conditioning-sense "oracle" rename in S3-P6/S4-P4/S4-P7 (T-08 follow-up).
3. Then the per-paragraph annotation passes + compile-enablement (port qmd_header / references footer / provenance title-page into level3 metadata) -> compile -> derivation-audit -> submission.

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

# Open questions

- Real-data demonstration (HRS wealth components vs NHANES lipids) -- defer unless the manuscript stalls or a reviewer requests it.
- What plain term replaces the conditioning-sense "oracle" (the fitted-versus-oracle / Q-function-conditioned-on-the-truth contrast) in S3-P6 / S4-P4 / S4-P7? T-08 follow-up; e.g. "true-parameter expectation" / "conditioned on the truth".
- Formalize the (correct but informal) MI-IC v4.5 derivation as an appendix theorem, generalized to arbitrary regular-likelihood models.
- Optional citation backlog (White 2011, Grund 2021, Schomaker 2007) -- none load-bearing.

(Resolved this session, moved to Decisions made: the S5 "which figures actually prove their claim / what is wrong with the figure that looked off" question -- answered by the tribunal, AMEND, claim-overreach not a plotting bug; and the W3-C-under-uncongeniality artifact-or-genuine question -- genuine, registered observational, direction-confirming.)
