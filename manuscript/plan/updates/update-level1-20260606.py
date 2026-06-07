# Level-1 review cycle 2 — 2026-06-06 (in-chat annotation, Marcus + Claude)
#
# Minutes of the cycle, one block per unit:
#
# U1-U5 (thesis): approved as-is, EXCEPT U2/U3 each gain one clause tying the
#   application to the complete-data replication principle (term adopted from the
#   MI-IC companion, mi-ic-article.qmd:136; Marcus confirmed the principle is
#   asserted-here and three-leveled: estimates / criterion-in-expectation /
#   decision rates).
#
# M1 INTRODUCTION: rewritten as an applied-reader funnel (MI mature -> LRT/IC the
#   exception -> typed unresolved questions via the replication principle -> what
#   this paper resolves at which level -> meta layer as the FINAL paragraph only).
#   Unresolved-status claims are explicitly typed documented-open vs asserted-here;
#   typing evidence acquired and verified this session (vanbuuren 2018a ch.5,
#   schomaker-heumann 2014a, enders 2025, schafer-graham 2002a synced).
#
# M2 BACKGROUND: dual-purpose (notation + precision restatement), organized as a
#   three-tier gradient (calculus-based stat-inference entry -> graduate ->
#   specialist); RIV defined in Tier 1; D-04 mechanism unamended.
#
# M3 METHODS: factual passive voice (dated style decision T-05); every gate
#   paragraph must state what the gate cannot catch (structural requirement);
#   one paragraph per part + sign episode as the single narrative; protocol
#   records go to APPENDICES (single-document constraint), not supplementary
#   materials — recorded as a D-08 note.
#
# M4 split (D-09 Amendment 1): M4a DERIVATIONS (theorem -> LRT -> IC,
#   replication-principle spine, headline numbers inline per D-03) and
#   M4b SIMULATION STUDIES (subheads "Simulation studies: setup" /
#   "Simulation studies: results"; the consolidated preregistered account).
#   Arc 5 -> 6 moves; gate target range 5-8 still passes.
#
# M5 DISCUSSION: inverse gradient (opens technical with G1-G6, broadens until the
#   close is readable by the M1 reader); plain-language replication-principle
#   verdict as the de facto takeaway block; NO separate Conclusion section;
#   provenance declaration closes the paper.
#
# Decisions: D-03, D-04, D-05, D-08 RATIFIED (2026-06-06). D-09 amended
#   (Amendment 1, M4 split). NEW D-10: complete-data replication principle as the
#   paper's organizing question. NEW T-05 (passive voice in Methods) recorded in
#   decisions.md.

import json

PATH = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level1-thesis.json"

with open(PATH, encoding="utf-8") as f:
    plan = json.load(f)

# ---------------------------------------------------------------- metadata
plan["metadata"]["amended"] = (
    "2026-06-05: D-09 ratified in-chat - arc restructured from 8-move theory-paper shape "
    "to 5-move IMRaD with Methods-as-workflow; methodological thesis component added. || "
    "2026-06-06 (cycle 2, in-chat): thesis U1-U5 approved (U2/U3 gain replication-principle "
    "clauses); all five moves rewritten per the cycle minutes in "
    "updates/update-level1-20260606.py; M4 split into Derivations + Simulation studies "
    "(D-09 Amendment 1, arc now 6 moves); D-03/D-04/D-05/D-08 ratified; D-10 added "
    "(complete-data replication principle)."
)
plan["metadata"]["status"] = "ratified_cycle2"

# ---------------------------------------------------------------- thesis (U2/U3 clauses)
plan["thesis"]["secondary"] += (
    " In the vocabulary of the complete-data replication principle (D-10): a correctly "
    "calibrated MI likelihood-ratio test recovers complete-data rejection rates at the "
    "null, while power under alternatives is bounded by the information actually lost - "
    "decision-rate replication splits along the null/noncentral axis."
)
plan["thesis"]["tertiary"] += (
    " In the vocabulary of the complete-data replication principle (D-10): adding "
    "tr(RIV_k) restores criterion replication in expectation for any signal strength; "
    "the calibration ladder locates the exact boundary of decision-rate replication - "
    "complete on the null side, information-bounded under signal."
)

# ---------------------------------------------------------------- persuasion arc
plan["persuasion_arc"]["total_moves"] = 6
plan["persuasion_arc"]["design_note"] = (
    "IMRaD adapted to an AI-human derivation (D-09, Amendment 1 of 2026-06-06): "
    "Introduction / Background / Methods-as-workflow / Derivations / Simulation studies / "
    "Discussion. The Results umbrella of the original D-09 is split into M4a Derivations "
    "and M4b Simulation studies; within Derivations the internal order stays theorem -> "
    "LRT -> IC (D-03 ratified: consolidated preregistered account in M4b + headline "
    "numbers inline at point of claim in M4a). Technical-gradient design: M2 ramps the "
    "reader up, M3 sits low (process, not mathematics), M4a is the peak, M4b steps back "
    "down, M5 descends to the M1 reader (no announcement of this in the text)."
)

plan["persuasion_arc"]["moves"] = [
    {
        "id": "M1",
        "label": "INTRODUCTION",
        "section_anchor": "sec-intro",
        "title": "Introduction",
        "function": (
            "Opening written for an applied researcher with quantitative training and "
            "working knowledge of multiple imputation. Four-paragraph arc. (1) Maturity: "
            "MI is a gold-standard treatment for missing data, now 40+ years old, and "
            "most of its major inferential results are long settled - the role of the "
            "missing-data mechanism, unbiased point estimation, valid single-parameter "
            "and multi-parameter Wald tests (anchored by the field's own before/after "
            "accounting: Schafer-Graham 2002 and Enders 2025). (2) The exception: "
            "likelihood-ratio tests and information criteria, despite first proposals in "
            "the 1990s, remain unsettled. The unsettled questions are posed via the "
            "complete-data replication principle (D-10; term shared with the MI-IC "
            "companion): would the same conclusion have been reached, on average over "
            "repeated samples, had the data been complete? Posed at three levels - "
            "replication of estimates (settled: Rubin), replication of the criterion in "
            "expectation, replication of decision rates. Each unsettled item is "
            "explicitly typed: gaps the prior literature itself states as open are cited "
            "to the stating passage (Schomaker-Heumann 2014: literature 'surprisingly "
            "sparse', averaged criteria 'not supported by MI literature'; FIMD 2018 and "
            "Enders 2025: no IC-after-MI treatment at all - documented by absence); gaps "
            "this paper is first to frame - the centering question and the replication "
            "principle itself - are asserted in the authors' voice and flagged as part "
            "of the contribution. (3) What this paper resolves: criterion replication is "
            "made achievable everywhere - the pooled deviance overstates its "
            "complete-data target by exactly +(1/2)tr(RIV) + (A)+(C), and the correction "
            "restores criterion replication in expectation for any signal strength; "
            "decision-rate replication splits along the null/noncentral axis identically "
            "for testing and selection - fully achievable at the null, provably bounded "
            "under signal by information loss rather than calibration error, with the "
            "boundary characterized exactly. Positioning: upstream of the Chan "
            "calibration line (calibration makes the reference right; this work makes "
            "the statistic centered); the trace penalty itself is Shimodaira's AIC_{x;y}, "
            "and prior corrections of that size target prediction, not replication - the "
            "replication question was unposed. (4) Final paragraph, meta layer: this is "
            "an AI-human derivation under a stated verification protocol, reported in "
            "full as the Methods section; one paragraph, no more."
        ),
        "serves_thesis": ["primary", "secondary", "tertiary", "methodological"],
        "key_claims": [
            "Pooled deviances and MI information criteria systematically overstate model fit by an exactly characterized amount; the LRT and IC consequences follow",
            "The complete-data replication principle, three levels (estimates / criterion-in-expectation / decision rates): level 1 classical, level 2 resolved here for any signal, level 3 resolved as a split - complete at the null, information-bounded under signal",
            "Unresolved-status claims are typed: documented-open cited to the stating passage; asserted-here stated in the authors' voice (typing evidence verified 2026-06-06; theory-side pass over Chan / Chan-Meng / Meng-Rubin still pending before Level-2 drafting)",
            "Calibration (Chan line) and centering (this work) are complementary; the trace penalty is precedented (Shimodaira; prediction-targeted 2x variants), the decomposition, MAR term, proper-MI scope, and replication framing are new",
            "The derivation is AI-assisted under a stated verification protocol, reported as Methods - final paragraph only"
        ],
        "evidence_base": [
            "lit:chanGeneralFeasibleTests2022",
            "lit:shimodairaInformationCriterionModel2017",
            "lit:hensModelSelectionIncomplete2006a",
            "lit:schaferMissingDataOur2002a",
            "lit:endersMissingDataUpdate2025",
            "lit:vanbuurenFlexibleImputationMissing2018a",
            "lit:schomakerModelSelectionModel2014a",
            "deriv:sec-intro"
        ],
        "rhetorical_role": (
            "An applied MI-literate reader finishes the introduction knowing what was "
            "settled, what was not, the principle by which 'resolved' is judged, what "
            "this paper resolves at which level - and only then that an AI derived it."
        )
    },
    {
        "id": "M2",
        "label": "BACKGROUND",
        "section_anchor": "sec-background",
        "title": "Background and notation",
        "function": (
            "Dual-purpose section: establishes the paper's notation AND restates each "
            "standard result in its source's own terms at the precision later steps "
            "need. Organized as a deliberate gradient - entry level is a calculus-based "
            "statistical-inference course, narrowing toward the technical, so a reader "
            "at the entry level is graduated upward rather than hitting a cliff. "
            "Tier 1 (accessible foundations, with equations): the notation "
            "Y = {Y_obs, Y_mis} and the missingness indicator R; full-data vs "
            "observed-data likelihoods and the two MLE targets theta_com / theta_obs "
            "this paper lives between; ignorability and when R drops out; the "
            "missing-information principle stated through Hessians "
            "(I_com = I_obs + I_mis|obs); RIV defined from it. "
            "Tier 2 (graduate): EM and the Q-function; the MCEM bridge (MI's averaged "
            "log-likelihood as a Monte Carlo Q); Rubin's rules as exact posterior-moment "
            "identities given one named approximation; congeniality. "
            "Tier 3 (specialist): AIC as a bias-corrected plug-in estimator; Wilks; "
            "observed-vs-expected information under MAR and the Kenward-Molenberghs "
            "convention; the EM rate matrix is NOT the RIV; MI test combining and the "
            "calibration line. Throughout, each restatement names the proposition that "
            "later depends on it (D-04 ratified); notation introduced here is the "
            "paper's notation - no symbol is introduced twice."
        ),
        "serves_thesis": ["primary"],
        "key_claims": [
            "Notation is established here, once; no symbol is introduced twice",
            "Tier 1: Y = {Y_obs, Y_mis}, R, ignorability, theta_com vs theta_obs, missing-information principle via Hessians, RIV defined",
            "Tier 2: EM/Q-function, MCEM bridge, Rubin's rules as exact posterior-moment identities, congeniality",
            "Tier 3: AIC as bias-corrected plug-in, Wilks, observed-vs-expected information under MAR (Kenward-Molenberghs), EM rate matrix is NOT the RIV, MI test combining and calibration"
        ],
        "evidence_base": [
            "lit:rubinInferenceMissingData1976b",
            "lit:kenwardLikelihoodBasedFrequentist1998",
            "lit:rubinMultipleImputationNonresponse1987",
            "lit:dempsterMaximumLikelihoodIncomplete1977a",
            "lit:akaikeNewLookStatistical1974a",
            "lit:endersMissingDataUpdate2025",
            "deriv:sec-sources"
        ],
        "rhetorical_role": (
            "Carry the M1 reader as far up the technical ramp as their training allows - "
            "pre-empting the standard misreadings on the way - so that wherever they "
            "stop, it is a gradient and not a cliff, and the notation is already theirs."
        )
    },
    {
        "id": "M3",
        "label": "METHODS",
        "section_anchor": "sec-methods",
        "title": "Methods: the derivation and verification workflow",
        "function": (
            "State the AI-human workflow as method, in six parts, one tight paragraph "
            "each: (1) roles and decision discipline - human prompter of record "
            "(direction, gates, decisions recorded with rejected options), AI "
            "derivation, dated decision log; (2) sourced derivation - every external "
            "claim pinned to a source passage in a locally archived session-read copy, "
            "citation discipline enforced mechanically by a pre-write hook; (3) claim "
            "pipeline - derive, then symbolic verification in two independent "
            "computer-algebra systems, then Monte Carlo confirmation, with trust tiers "
            "(firm / measured / structural / conjecture) assigned by the gates cleared; "
            "(4) preregistration before code - predictions and pass criteria frozen and "
            "committed first, dated amendments, failures reported; (5) cross-model "
            "adversarial verification - blind re-derivation by an independent model "
            "lineage plus an instructed-to-refute pass, grading records committed, with "
            "the fitted-vs-oracle sign episode as the single narrative passage; "
            "(6) reproducibility - seeds, caches, single-entrypoint scripts, environment "
            "records. STYLE (T-05): written factually in the passive voice - the "
            "protocol is described as a procedure, not narrated as an achievement. "
            "STRUCTURAL REQUIREMENT: every gate paragraph ends with what that gate "
            "cannot catch. LENGTH: full protocol records (grading records, amendment "
            "logs, hook mechanics, per-gate specifications) go to appendices (single "
            "submission document; repo cited for the full audit trail) - recorded as a "
            "D-08 note. Drafting guidance (not announced in the text): M3 sits lower on "
            "the technical gradient than M2/M4a; keep it that way."
        ),
        "serves_thesis": ["methodological"],
        "key_claims": [
            "Each verification gate is stated with what it can and cannot catch (structural requirement: every gate paragraph ends with its blind spot)",
            "Trust tiers used throughout Derivations and Simulation studies are defined here, once",
            "The fitted-vs-oracle episode: 8 of 9 blind re-derivations produced the opposite sign until the conditioning was pinned - the protocol caught a sign error a single-lineage derivation would likely have shipped",
            "Failed preregistered predictions are part of the record, not the appendix",
            "Written in factual passive voice (T-05); protocol detail in appendices, statements in text"
        ],
        "evidence_base": [
            "deriv:sec-verify",
            "deriv:sec-sources",
            "verif:todo/004-simulation-hypotheses.md",
            "verif:todo/027-ladder-preregistration.md",
            "verif:verification/run_all.R",
            "verif:verification/ic-ladder.R",
            "xmodel:verification/cache/derivation-audit-run-w2diff.json"
        ],
        "rhetorical_role": (
            "Answer 'why believe an AI derivation' before any result is asked to be "
            "believed - as procedure, in passive voice, with each gate's blind spot "
            "stated."
        )
    },
    {
        "id": "M4a",
        "label": "DERIVATIONS",
        "section_anchor": "sec-derivations",
        "title": "Derivations",
        "function": (
            "The analytic output of the Methods, graded by its trust tiers, in three "
            "subsections kept in the established internal order (D-03 ratified), each "
            "opening with the level of the replication principle (D-10) it addresses: "
            "(a) setup and main theorem - one RIV, fitted-vs-oracle stated up front, "
            "the A/B split, the (A)+(C) term with its three-tier standing, known-scale "
            "collapse, entropy-plug-in consistency check; addresses criterion "
            "replication in expectation; (b) likelihood-ratio comparison - tr(RIV_perp) "
            "in the I_com metric, the naive-difference overstatement with exact gap, "
            "the paired-noise collapse, the null cancellation and its return under "
            "separation, the absorption argument; addresses decision-rate replication "
            "for testing; (c) information-criterion selection - corrected criterion = "
            "AIC_{x;y}, directional misclassification signature, the calibration ladder "
            "with the null/noncentral split and the two exact structural limits; "
            "addresses decision-rate replication for selection. Headline numbers quoted "
            "inline at the point of each claim (D-03); the full preregistered account "
            "lives in M4b."
        ),
        "serves_thesis": ["primary", "secondary", "tertiary"],
        "key_claims": [
            "E[T] = +(1/2)tr(RIV) + (A)+(C); pooled MC 2.43 +/- 0.26 vs augmented range 2.42-2.55",
            "LRT differential = tr(RIV_perp) in the I_com metric; naive always overstates (52 se discrimination); pairing O(1); null cancellation exact",
            "IC: misclassifications land on the largest-RIV candidate; rungs 2-3 reach the oracle on the null side (0.904/0.903 vs 0.899); noncentral shrinkage at predicted factors; weak-signal floor 0.17",
            "Each subsection opens by naming the replication-principle level it addresses"
        ],
        "evidence_base": [
            "deriv:sec-thm",
            "deriv:sec-lrt",
            "deriv:sec-ic",
            "verif:verification/cache/ic-ladder-summary.csv"
        ],
        "rhetorical_role": (
            "Every claim arrives pre-graded and tied to the question M1 posed; the "
            "reader never has to guess a claim's standing. The technical peak of the "
            "paper."
        )
    },
    {
        "id": "M4b",
        "label": "SIMULATION STUDIES",
        "section_anchor": "sec-simulations",
        "title": "Simulation studies",
        "function": (
            "The consolidated pre-registered evidence account (D-03 ratified), in two "
            "subsections: 'Simulation studies: setup' - the apparatus once (designs, "
            "engines, R, seeds, preregistration protocol and amendment history); "
            "'Simulation studies: results' - prediction-by-prediction grading against "
            "the frozen pass criteria, findings including the misses (similar-pair "
            "differential below resolution; N=1000 cell at 2.6 se; component-level "
            "9-20% misses), engine sensitivity scoped. Steps back down the technical "
            "gradient from M4a toward the applied reader."
        ),
        "serves_thesis": ["primary", "secondary", "tertiary", "methodological"],
        "key_claims": [
            "Apparatus stated once; every number traces to a committed pre-registered artifact",
            "Failures reported in the main text as a unit (D-05): similar-pair differential below resolution; N=1000 cell at 2.6 se; component-level 9-20% misses",
            "Engine sensitivity scoped (EMB/Amelia vs engine-free observed-data RIV within 2-3%)"
        ],
        "evidence_base": [
            "verif:todo/004-simulation-hypotheses.md",
            "verif:todo/005-comprehensive-sweep-hypotheses.md",
            "verif:todo/027-ladder-preregistration.md",
            "verif:verification/run_all.R",
            "verif:verification/ic-ladder.R",
            "verif:verification/cache/ic-ladder-summary.csv",
            "verif:verification/cache/w4-nonnested-summary.csv"
        ],
        "rhetorical_role": (
            "The preregistration narrative (predictions, amendments, failures) auditable "
            "as a single unit - the provenance exhibit JAIGP needs to see whole."
        )
    },
    {
        "id": "M5",
        "label": "DISCUSSION",
        "section_anchor": "sec-discussion",
        "title": "Discussion",
        "function": (
            "Inverse gradient: opens at the technical level the derivations earned and "
            "broadens until the closing passages are fully readable by the M1 reader. "
            "Order: (1) scope and limits G1-G6, each next to the claim it qualifies; "
            "(2) the power-dominance conjecture stated as a conjecture with partial "
            "empirical support (W2); (3) three directions - covariate shift (per "
            "Shimodaira's named future work), exact-engine replication, selection-aware "
            "calibration (the sequel, developed separately); (4) the broadening turn: "
            "the replication-principle verdict in plain language - what an applied "
            "researcher can now do and expect (on average the corrected criterion "
            "matches what complete data would have given; at the null, selection "
            "behaves as if the data were complete; under signal, missing information "
            "costs power and no post-processing can buy it back) and what remains open; "
            "(5) a short trust-ordered reflection on the workflow - what the gates "
            "caught, what they cost, what they cannot catch; (6) ends with the formal "
            "JAIGP provenance declaration (the former standalone section, shrunk). NO "
            "separate Conclusion section - item (4) is the de facto takeaway block."
        ),
        "serves_thesis": ["primary", "secondary", "tertiary", "methodological"],
        "key_claims": [
            "G1-G6 with evidential standing stated",
            "The replication-principle verdict stated in plain language for the M1 reader",
            "The workflow reflection is itself trust-ordered: what is demonstrated about the protocol vs what is asserted",
            "No separate Conclusion; the Discussion broadens out instead"
        ],
        "evidence_base": [
            "deriv:sec-lrt-ac",
            "lit:shimodairaInformationCriterionModel2017"
        ],
        "rhetorical_role": (
            "Open at the technical peak, descend to the M1 reader; the paper's last "
            "fully technical sentence comes early in the Discussion, and its last page "
            "belongs to anyone who could read its first. The declaration closes the "
            "paper as the final accountability statement."
        )
    }
]

# ---------------------------------------------------------------- decisions
for d in plan["decisions"]:
    if d["id"] in ("D-03", "D-04", "D-05", "D-08"):
        d["status"] = "ratified"
        d["ratified"] = "2026-06-06 (Level-1 review cycle 2, in-chat)"
    if d["id"] == "D-08":
        d["note_appendices"] = (
            "2026-06-06: extended to a three-tier posture applied to Methods - paper "
            "(statements + the sign-episode worked example) -> appendices (protocol "
            "records: grading summaries, amendment log, hook mechanics, per-gate "
            "specifications; appendices NOT separate supplementary materials, because "
            "the venue may accept only one document upload) -> companion derivation "
            "document + repo for the full audit trail."
        )
    if d["id"] == "D-09":
        d["amendment_1"] = (
            "2026-06-06: the Results umbrella splits into two top-level moves - M4a "
            "Derivations (theorem -> LRT -> IC, headline numbers inline) and M4b "
            "Simulation studies (subheads 'Simulation studies: setup' / 'Simulation "
            "studies: results'; the consolidated preregistered account). Arc is 6 "
            "moves. Rationale: 'Results' was a strained name for proven theorems, and "
            "the split gives the simulations their own setup/results structure without "
            "stuffing simulation design into the workflow Methods. D-03's consolidation "
            "logic is preserved (M4b is its completion)."
        )

plan["decisions"].append({
    "id": "D-10",
    "date": "2026-06-06",
    "label": "Complete-data replication principle as the paper's organizing question",
    "chosen": (
        "The paper poses and is organized around the complete-data replication "
        "principle (term adopted from the MI-IC companion, mi-ic-article.qmd:136): "
        "would the same conclusion have been reached, on average over repeated finite "
        "samples, had the data been complete? Posed at three levels - (1) replication "
        "of estimates (classical: Rubin's unbiasedness), (2) replication of the "
        "criterion in expectation (this paper makes achievable everywhere via the "
        "centering correction), (3) replication of decision rates (achievable "
        "completely at the null; provably information-bounded under signal, for "
        "testing and selection alike). The principle is asserted-here (confirmed "
        "unposed in the closest prior work, Schomaker-Heumann 2014, which explicitly "
        "sidesteps averaged criteria as 'not supported by MI literature'); it is "
        "introduced in M1, answered level-by-level in M4a, and given a plain-language "
        "verdict in M5. Terminology guard: distinguish from Monte Carlo 'replications' "
        "at Level 3 drafting (say 'simulation repetitions')."
    ),
    "rejected_options": {
        "decision_equivalence_coinage": (
            "A new name ('complete-data decision equivalence') coined for this paper - "
            "rejected for cross-repo consistency; MI-IC already terms it complete-data "
            "replication and is cited from here."
        ),
        "unqualified_rate_replication": (
            "Claiming decision-rate replication universally - wrong: information loss "
            "bounds power under alternatives for LRT and shrinks noncentral IC gaps "
            "alike (the ladder's split); the three-level form builds the todo/026 "
            "qualification into the principle itself."
        ),
        "ic_only_scope": (
            "Restricting the principle to IC selection - rejected: the null/noncentral "
            "split is structurally identical for testing and selection, and the "
            "symmetric statement is the stronger, honest form."
        )
    },
    "provenance": "Marcus in-chat, Level-1 review cycle 2, 2026-06-06; MI-IC companion framing",
    "status": "ratified"
})

# ---------------------------------------------------------------- metrics gate
plan["metrics_gate"] = {
    "arc_moves": 6,
    "target_range": "5-8",
    "every_move_serves_thesis": True,
    "every_decision_has_rejected_options": True,
    "venue_alignment_explicit": True,
    "passes": True,
    "notes": (
        "Six moves after D-09 Amendment 1 (M4 split). M3 METHODS serves the "
        "methodological thesis; M1/M4b/M5 serve all components. Section anchors "
        "sec-methods, sec-derivations, sec-simulations do not exist in the qmd yet - "
        "they are targets for the Level-2 blueprint and the restructuring "
        "decomposition. Gate re-evaluated at every Level-1 amendment."
    )
}

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("level1-thesis.json updated: 6 moves, D-03/04/05/08 ratified, D-09 amended, D-10 added")
