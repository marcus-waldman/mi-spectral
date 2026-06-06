#!/usr/bin/env python3
# Level-1 amendment, 2026-06-05: D-09 ratified by Marcus in-chat.
# "We are going to need to do more of an introduction, background, methods,
#  results, conclusion. This whole AI-human derivation is a new thing. The
#  methods section is really where we state the workflow we used to arrive at
#  claims we can strongly defend."
#
# Changes applied atomically to manuscript/plan/level1-thesis.json:
#   1. thesis.methodological added (fourth thesis component, promoted from
#      venue_alignment).
#   2. persuasion_arc replaced: 8-move theory-paper arc -> 5-move IMRaD arc
#      with Methods = the derivation-and-verification workflow.
#   3. D-09 decision block appended (ratified; rejected option = the 180e2b5
#      theory-paper structure with workflow as end-matter provenance).
#   4. D-03 annotated: under D-09 the consolidated evidence account becomes
#      the closing Results subsection; placement choice itself unchanged,
#      still proposed.
#   5. metadata + metrics_gate updated (5 moves, amendment recorded).
#
# Not changed (still awaiting Marcus's annotation): thesis primary/secondary/
# tertiary text; D-03/D-04/D-05/D-08 ratification. Results internal order kept
# at theorem -> LRT -> IC -> numerics (Marcus did not amend D-03).

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
F = REPO / "manuscript" / "plan" / "level1-thesis.json"

doc = json.loads(F.read_text(encoding="utf-8"))

# ------------------------------------------------------------------
# 1. Fourth thesis component
# ------------------------------------------------------------------
thesis = doc["thesis"]
new_thesis = {}
for k in ("primary", "secondary", "tertiary"):
    new_thesis[k] = thesis[k]
new_thesis["methodological"] = (
    "The AI-human derivation workflow is itself a contribution, stated as the paper's "
    "Methods: preregistration before code with dated amendments and failures reported, "
    "a sourced derivation in which every external claim is pinned to a locally archived "
    "session-read passage with citation discipline enforced mechanically, a claim "
    "pipeline of derive -> dual computer-algebra verification -> Monte Carlo "
    "confirmation against frozen pass criteria, cross-model blind re-derivation with an "
    "adversarial instructed-to-refute gate, and full reproducibility (seeds, caches, "
    "single-entrypoint scripts). The claim: this workflow yields AI-assisted "
    "mathematical results defensible at the standard a skeptical referee applies to "
    "human-derived work - and the Results section is the demonstration, with every "
    "claim carrying its trust tier (firm / measured / structural / conjecture) and the "
    "gates it cleared. The fitted-vs-oracle sign episode (8 of 9 blind re-derivations "
    "landing on the opposite sign until the conditioning was pinned) is the worked "
    "example of why the verification gates exist."
)
new_thesis["venue_alignment"] = thesis["venue_alignment"]
doc["thesis"] = new_thesis

# ------------------------------------------------------------------
# 2. IMRaD arc
# ------------------------------------------------------------------
doc["persuasion_arc"] = {
    "total_moves": 5,
    "design_note": (
        "IMRaD adapted to an AI-human derivation (D-09): the workflow that makes the "
        "claims defensible is the Methods, not end-matter. The reader evaluates the "
        "Results through the Methods, as in empirical work. Within Results the "
        "internal order stays theorem -> LRT -> IC -> numerics (D-03 unamended)."
    ),
    "moves": [
        {
            "id": "M1",
            "label": "INTRODUCTION",
            "section_anchor": "sec-intro",
            "title": "Introduction",
            "function": (
                "Two-layer opening. Scientific layer: the averaged log-likelihood is not an "
                "unbiased stand-in for the complete-data log-likelihood; headline bias "
                "+(1/2)tr(RIV) + (A)+(C); the two applications; positioning upstream of the "
                "Chan calibration line and against the model-selection lineage; what is new "
                "and what is not. Meta layer: this is an AI-human derivation under a "
                "defensibility protocol, the paper reports both the results and the workflow, "
                "and the Methods section is where that workflow is stated."
            ),
            "serves_thesis": ["primary", "secondary", "tertiary", "methodological"],
            "key_claims": [
                "Deviances built from the averaged log-likelihood are systematically too favorable, by an exactly characterized amount",
                "Calibration (Chan line) makes the reference right; this work makes the statistic referred to it centered - complementary",
                "The trace penalty is Shimodaira's AIC_{x;y}; new: the decomposition, the MAR term, proper-MI scope, and the two application-level results",
                "The derivation is AI-assisted under a stated verification protocol; the workflow is a contribution, reported as Methods"
            ],
            "evidence_base": ["lit:chanGeneralFeasibleTests2022", "lit:shimodairaInformationCriterionModel2017", "lit:hensModelSelectionIncomplete2006a", "deriv:sec-intro"],
            "rhetorical_role": "State the whole result and the trust framework in the first two pages."
        },
        {
            "id": "M2",
            "label": "BACKGROUND",
            "section_anchor": "sec-background",
            "title": "Background",
            "function": (
                "Restate each standard result in its source's own terms at the precision later "
                "steps need - the EM rate matrix is NOT the RIV, Rubin's rules are exact given "
                "one named approximation, observed and expected information differ under MAR - "
                "each restatement naming the proposition that depends on it (D-04)."
            ),
            "serves_thesis": ["primary"],
            "key_claims": [
                "Ignorability; EM/Q-function; missing-information principle; Rubin's rules as exact posterior-moment identities; MCEM bridge; congeniality; AIC as bias-corrected plug-in; Wilks; observed-vs-expected information under MAR; MI test combining and calibration"
            ],
            "evidence_base": ["lit:kenwardLikelihoodBasedFrequentist1998", "lit:rubinMultipleImputationNonresponse1987", "lit:akaikeNewLookStatistical1974a", "deriv:sec-sources"],
            "rhetorical_role": "Pre-empt the standard misreadings before they can occur."
        },
        {
            "id": "M3",
            "label": "METHODS",
            "section_anchor": "sec-methods",
            "title": "Methods: the derivation and verification workflow",
            "function": (
                "State the AI-human workflow as method, in six parts: (1) roles and decision "
                "discipline - human prompter of record (direction, gates, decisions recorded "
                "with rejected options), AI derivation, dated decision log; (2) sourced "
                "derivation - every external claim pinned to a source passage in a locally "
                "archived session-read copy, citation discipline enforced mechanically by a "
                "pre-write hook; (3) claim pipeline - derive, then symbolic verification in "
                "two independent computer-algebra systems, then Monte Carlo confirmation, "
                "with trust tiers (firm / measured / structural / conjecture) assigned by the "
                "gates cleared; (4) preregistration before code - predictions and pass "
                "criteria frozen and committed first, dated amendments, failures reported; "
                "(5) cross-model adversarial verification - blind re-derivation by an "
                "independent model lineage plus an instructed-to-refute pass, grading records "
                "committed, with the fitted-vs-oracle sign episode as the worked example of "
                "what this gate catches; (6) reproducibility - seeds, caches, "
                "single-entrypoint scripts, environment records."
            ),
            "serves_thesis": ["methodological"],
            "key_claims": [
                "Each verification gate is stated with what it can and cannot catch",
                "Trust tiers used throughout Results are defined here, once",
                "The fitted-vs-oracle episode: 8 of 9 blind re-derivations produced the opposite sign until the conditioning was pinned - the protocol caught a sign error a single-lineage derivation would likely have shipped",
                "Failed preregistered predictions are part of the record, not the supplement"
            ],
            "evidence_base": ["deriv:sec-verify", "deriv:sec-sources", "verif:todo/004-simulation-hypotheses.md", "verif:todo/027-ladder-preregistration.md", "verif:verification/run_all.R", "verif:verification/ic-ladder.R", "xmodel:verification/cache/derivation-audit-run-w2diff.json"],
            "rhetorical_role": "Answer 'why believe an AI derivation' before any result is asked to be believed."
        },
        {
            "id": "M4",
            "label": "RESULTS",
            "section_anchor": "sec-results",
            "title": "Results",
            "function": (
                "The output of the Methods, graded by its trust tiers, in four subsections "
                "kept in the current internal order (D-03 unamended): (a) setup and main "
                "theorem - one RIV, fitted-vs-oracle stated up front, the A/B split, the "
                "(A)+(C) term with its three-tier standing, known-scale collapse, "
                "entropy-plug-in consistency check; (b) likelihood-ratio comparison - "
                "tr(RIV_perp) in the I_com metric, the naive-difference overstatement with "
                "exact gap, the paired-noise collapse, the null cancellation and its return "
                "under separation, the absorption argument; (c) information-criterion "
                "selection - corrected criterion = AIC_{x;y}, directional misclassification "
                "signature, the calibration ladder with the null/noncentral split and the "
                "two exact structural limits; (d) the pre-registered numerical studies - "
                "apparatus once, findings including the misses, engine sensitivity scoped."
            ),
            "serves_thesis": ["primary", "secondary", "tertiary"],
            "key_claims": [
                "E[T] = +(1/2)tr(RIV) + (A)+(C); pooled MC 2.43 +/- 0.26 vs augmented range 2.42-2.55",
                "LRT differential = tr(RIV_perp) in the I_com metric; naive always overstates (52 se discrimination); pairing O(1); null cancellation exact",
                "IC: misclassifications land on the largest-RIV candidate; rungs 2-3 reach the oracle on the null side (0.904/0.903 vs 0.899); noncentral shrinkage at predicted factors; weak-signal floor 0.17",
                "Failures reported: similar-pair differential below resolution; N=1000 cell at 2.6 se; component-level 9-20% misses"
            ],
            "evidence_base": ["deriv:sec-thm", "deriv:sec-lrt", "deriv:sec-ic", "verif:verification/cache/ic-ladder-summary.csv", "verif:verification/cache/w4-nonnested-summary.csv"],
            "rhetorical_role": "Every claim arrives pre-graded; the reader never has to guess a claim's standing."
        },
        {
            "id": "M5",
            "label": "DISCUSSION",
            "section_anchor": "sec-discussion",
            "title": "Discussion and conclusion",
            "function": (
                "Scope and limits G1-G6, each next to the claim it qualifies; the "
                "power-dominance conjecture stated as a conjecture with partial support; "
                "three directions (covariate shift per Shimodaira's named future work, "
                "exact-engine replication, selection-aware calibration developed "
                "separately); and a short reflection on the workflow itself - what the "
                "gates caught, what they cost, what they cannot catch. Ends with the formal "
                "JAIGP provenance declaration (the former standalone section, shrunk)."
            ),
            "serves_thesis": ["primary", "secondary", "tertiary", "methodological"],
            "key_claims": [
                "G1-G6 with evidential standing stated",
                "The workflow reflection is itself trust-ordered: what is demonstrated about the protocol vs what is asserted"
            ],
            "evidence_base": ["deriv:sec-lrt-ac", "lit:shimodairaInformationCriterionModel2017"],
            "rhetorical_role": "Explicit limits as the closing trust move; the declaration is a formality because the whole paper performed it."
        }
    ]
}

# ------------------------------------------------------------------
# 3. D-09
# ------------------------------------------------------------------
doc["decisions"].append({
    "id": "D-09",
    "date": "2026-06-05",
    "label": "Paper macro-structure: IMRaD with Methods-as-workflow",
    "chosen": (
        "Introduction / Background / Methods / Results / Discussion-Conclusion. Methods "
        "states the AI-human derivation-and-verification workflow as method (roles and "
        "decision discipline; sourced derivation with mechanical citation enforcement; "
        "derive -> dual-CAS -> Monte Carlo pipeline with trust tiers; preregistration "
        "before code with amendments and reported failures; cross-model blind plus "
        "adversarial verification, fitted-vs-oracle episode as worked example; "
        "reproducibility). Results = setup+theorem, LRT, IC, preregistered numerics, in "
        "that order. A fourth, methodological thesis component is added. Rationale: the "
        "AI-human derivation is itself a new contribution and the venue's central "
        "question is 'why believe an AI derivation' - the workflow is where claims "
        "become strongly defensible, so it is Methods, not end-matter."
    ),
    "rejected_options": {
        "theory_paper_structure": (
            "The 180e2b5 draft structure (problem -> background -> theorem -> applications "
            "-> numerics -> discussion -> provenance statement): buries the workflow in an "
            "end-of-paper statement, underselling the venue's central question."
        ),
        "workflow_in_supplement": (
            "A pure results paper with the protocol in supplementary material: "
            "contradicts the trust posture the paper itself argues for."
        )
    },
    "provenance": "Marcus, in-chat Level-1 annotation, 2026-06-05",
    "status": "ratified"
})

# ------------------------------------------------------------------
# 4. D-03 note under D-09
# ------------------------------------------------------------------
for d in doc["decisions"]:
    if d["id"] == "D-03":
        d["note_d09"] = (
            "Under D-09 the consolidated evidence account becomes the closing Results "
            "subsection; the placement choice (consolidated account + inline headline "
            "numbers at point of claim) is unchanged and still proposed. Marcus did not "
            "amend it when ratifying D-09."
        )

# ------------------------------------------------------------------
# 5. Metadata + gate
# ------------------------------------------------------------------
doc["metadata"]["amended"] = (
    "2026-06-05: D-09 ratified in-chat - arc restructured from 8-move theory-paper "
    "shape to 5-move IMRaD with Methods-as-workflow; methodological thesis component "
    "added. Thesis text and D-03/D-04/D-05/D-08 still await annotation."
)
doc["metrics_gate"] = {
    "arc_moves": 5,
    "target_range": "5-8",
    "every_move_serves_thesis": True,
    "every_decision_has_rejected_options": True,
    "venue_alignment_explicit": True,
    "passes": True,
    "notes": (
        "Five IMRaD moves (D-09). M3 METHODS serves the methodological thesis; M1/M5 "
        "serve all components. Section anchors sec-methods and sec-results do not exist "
        "in the qmd yet - they are targets for the Level-2 blueprint and the "
        "restructuring decomposition. Gate re-evaluated at every Level-1 amendment."
    )
}

F.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("level1-thesis.json amended: D-09 recorded, IMRaD arc (5 moves), methodological thesis added")
