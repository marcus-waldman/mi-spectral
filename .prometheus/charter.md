---
schema_version: 1
project_id: d51ab9db-0748-44c5-ad94-2eee09e126f5
project_name: mi-spectral
status: active
current_milestone: "Socratic review of the S5 simulation evidence -- does each figure actually prove its claim? (confidence gate before more drafting)"
last_synced_commit: "7768357"
tree_state: dirty
updated: "2026-06-16T15:10:03Z"
updated_by: wrap
supermemory_container: proj-d51ab9db-0748-44c5-ad94-2eee09e126f5
cockpit: { provider: null, list_id: null }
---


# Goal

A finite-M spectral correction for likelihood-based hypothesis tests under *congenial* multiple imputation (MI), with applications to likelihood-ratio model comparison and information-criterion model selection. Core result: the MI Q-function carries a deviance bias that decomposes as +1/2 * tr(RIV) (RIV = relative-increase-in-variance). It is an AI-assisted derivation with transparent, ORCID-verified human prompting, targeting JAIGP; every load-bearing claim is meant to be paired with a preregistered numerical witness. Predicted empirical signature: uncorrected MI-AIC misclassifications should concentrate on the highest-RIV candidate model -- but whether the simulation evidence actually shows this convincingly is exactly what is now in question.

# Current milestone

GATE: before any further drafting or compile, the simulation evidence (S5) must pass a skeptical, figure-by-figure Socratic review. When last reviewed, the S5 evidence was unconvincing or poorly explained, and at least one figure looked clearly off yet was presented as proof that something works. That dented confidence -- the failure mode here is confident-but-wrong AI narration applied to hard evidence, which is worse than weak prose. Tie every result/figure to the precise claim it must support and adversarially test whether it does, before resuming prose annotation or compiling.

# Milestones

The arc from start to the Goal. Mark each: `[x]` done - `[~]` current - `[ ]` upcoming.

- [x] Theory & derivation -- the +1/2*tr(RIV) deviance-bias decomposition (reframed after Chan 2022, AoS)
- [x] Preregistration of witness hypotheses (W1 theorem - W2 LRT power - W3 model selection)
- [x] Empirical validation runs executed (comprehensive sweep; W4 non-nested)
- [x] Proof of correctness -- formal propositions + CAS verification
- [~] Socratic review of the simulation evidence (S5) -- does each figure actually prove its claim? (incl. the figure that looked clearly off)
- [ ] Per-paragraph annotation of S1-S6
- [ ] Compile + derivation-audit (0 blocker/0 warn) + Zenodo deposit -> JAIGP submission

# Next 3 actions

1. Socratic review of S5: for each figure/result, state the exact claim it must support, then adversarially test whether it does -- and find/diagnose the figure that looked clearly off (a real surprising result vs a plotting/scaling bug vs a claim that overreaches the evidence).
2. Repair what the review surfaces -- re-run, re-plot, or rewrite the claim -- until each figure demonstrably earns its place; no claim survives on confident prose alone.
3. Only then resume per-paragraph annotation (S1-S6), and proceed to compile + derivation-audit + submission.

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

# Open questions

- Which S5 figures/results actually demonstrate the predicted mechanism, and which are unconvincing or mis-explained? Specifically: what is wrong with the figure that looked clearly off -- a real (surprising) result, a plotting/scaling bug, or a claim that overreaches the evidence?
- Real-data demonstration (HRS wealth components vs NHANES lipids) -- defer unless the manuscript stalls or a reviewer requests it.
- Uncongeniality robustness: W3-C directional concordance reportedly = 1.000 even under uncongeniality -- design artifact or genuine property? (re-examine in the Socratic review.)
- Formalize the (correct but informal) MI-IC v4.5 derivation as an appendix theorem, generalized to arbitrary regular-likelihood models.
- Optional citation backlog (White 2011, Grund 2021, Schomaker 2007) -- none load-bearing.
