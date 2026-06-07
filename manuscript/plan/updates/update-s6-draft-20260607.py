# S6 Discussion - from-scratch draft (D-12), 2026-06-07
#
# Final Level-3 drafting cycle, under the approved S6 blueprint (a21120a):
# inverse gradient (opens technical, broadens to the S1 reader); G1-G6 next to
# the claims they qualify; power-dominance as a labeled conjecture; three
# directions; the plain-language replication-principle verdict as the takeaway
# block; trust-ordered workflow reflection as the close. NO Conclusion section;
# NO provenance section (D-11: title page). Quarried from 180e2b5 sec-discussion
# (:921-:981); old sec-provenance (:983-:995) does NOT come over (title page +
# S3 carry its content). Eight paragraphs (blueprint estimate 9-11; G-limits
# grouped two per paragraph - flagged).

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

P1 = (
    "The result is scoped by its own mechanism, and the scope comes first. The bias "
    "exists only when the fit estimates a scale or covariance, so that the "
    "conditional missing-data entropy depends on the estimated parameters. A "
    "known-scale, location-only fit has no such bias, which is why the "
    "estimated-scale clause sits in the theorem rather than in a footnote. "
    "Congeniality is assumed throughout, and what the bias becomes without it "
    "[@mengMultipleImputationInferencesUncongenial1994a] is a separate question this "
    "paper does not take up. Beyond these scope conditions, six specific limits "
    "remain. Each is stated next to the claim it qualifies, with its evidential "
    "standing, and they are followed by one conjecture, three directions, and the "
    "answer to the question the paper opened with."
)

P2 = (
    "**G1.** The absolute magnitude of $(A)+(C)$ is not independently pinned, and "
    "this qualifies the theorem. Firm: its structure, sign, $O(1)$ order, exact MCAR "
    "vanishing, the closed form @eq-ac, and the $O(1/n)$ order of the correction "
    "beyond the leading-order analytic value. Not firm: the absolute magnitude "
    "itself. The direct Monte Carlo estimates are heavy-tailed and untrended, and "
    "the variance-reduced estimate of the higher-order remainder is conditional on "
    "the analytic anchor it is paired against. Every comparison in this paper "
    "therefore uses $(A)+(C)$ only through the better-conditioned paired "
    "differential. **G2.** The proper-MI carry-over of the likelihood-ratio "
    "propositions is structural, not separately measured, and this qualifies the "
    "likelihood-ratio part of @sec-derivations. The propositions are proved and "
    "confirmed for the deterministic-FIML $\\bar Q_\\infty$. Under proper MI the "
    "imputation-side quantities remain common to both fits, which preserves the "
    "cancellation arguments, but no dedicated proper-MI replication of the "
    "differential experiments exists."
)

P3 = (
    "**G3.** Imputation-engine robustness is empirical and scoped, and this "
    "qualifies @sec-simulations. The EMB engine tracks deterministic FIML within "
    "the stated tolerances on the designs studied. Exact data augmentation was not "
    "run, and nothing here establishes engine-independence beyond those designs. "
    "**G4.** The weak-signal floor is a measurement, not an impossibility proof, "
    "and this qualifies the selection part of @sec-derivations. The residual in the "
    "weak-signal cell is information loss as measured through these corrections. No "
    "argument here shows that no estimator built from the same observed data could "
    "do better."
)

P4 = (
    "**G5.** For dissimilar candidate pairs, a mechanism-independent "
    "misspecification $O(1)$ coexists with the design-imbalance $O(1)$, and this "
    "qualifies @prp-ac-diff and its use in selection. The MCAR contrast separates "
    "the two in measurement, but they can reinforce or partially offset each other "
    "in the net ranking bias a criterion sees. We make no claim that the "
    "design-imbalance term dominates every pair. **G6.** All instantiation is "
    "multivariate normal, and this qualifies the theorem. The theorem is stated for "
    "general regular likelihoods with an estimated scale, but every constant is "
    "verified, symbolically and by simulation, only in the normal family."
)

P5 = (
    "One question is left as a conjecture, and it is labeled as one. We conjecture "
    "that the bias-corrected likelihood-ratio comparison dominates its uncorrected "
    "counterpart in power uniformly. The preregistered likelihood-ratio study's "
    "power arms provide partial support (@sec-simulations). We state no theorem."
)

P6 = (
    "Three directions seem most worth pursuing. The first is covariate shift. The "
    "concluding section of @shimodairaInformationCriterionModel2017 names the "
    "combination of a missing mechanism with other sampling mechanisms as future "
    "work. The design-imbalance term derived here is nonzero exactly when the "
    "missing and observed units differ on the conditioning variables, which is a "
    "step into that program, and the weighting machinery exists "
    "[@shimodairahidetoshiImprovingPredictiveInference2000]. The second is an "
    "exact-engine replication. Running the headline studies under data augmentation "
    "would convert G3 from an empirical tolerance into a tested equivalence. The "
    "third is the calibration program beyond per-model null maps. De-shrinkage of "
    "estimated noncentrality and joint calibration of score vectors across "
    "candidates are developed separately, as is the extension beyond the normal "
    "family."
)

P7 = (
    "The paper closes where it began, with the replication principle. The question "
    "was whether an analyst working from multiply imputed data reaches the same "
    "conclusions, as often, as the analyst who never lost the data. The answer now "
    "has three parts. For the criterion itself, yes: after correction, a deviance "
    "or information criterion computed from imputed data means what its "
    "complete-data counterpart means, on average, at any signal strength. For "
    "decisions when the competing models fit alike, yes: corrected selection and "
    "calibrated tests behave as they would have with complete data. For decisions "
    "when one model genuinely fits better, no, and the shortfall is not fixable: "
    "the missing data carried part of the evidence, less information means less "
    "power, and no transformation of the observed data manufactures the lost "
    "evidence back. The practical summary for an applied reader is short. Correct "
    "the criterion, or match its null distribution, and trust the result the way "
    "complete-data results are trusted, except where the comparison was close "
    "enough that the missing data could have decided it. There, the honest answer "
    "is that the data no longer say."
)

P8 = (
    "A final word on the workflow, held to the same standard as everything it "
    "produced. What it demonstrably caught is on the record: a sign error that "
    "eight of nine blind re-derivations shipped, a wrong shortcut in an early "
    "entropy-gradient argument, and every failed prediction now reported in "
    "@sec-simulations. What it cost is also visible: claims arrive slower, hedged "
    "to their tier, and two preregistered headlines were given up rather than "
    "rescued. What it cannot catch was stated in @sec-methods and bears repeating "
    "once: errors shared across model lineages, misreadings of real sources, and "
    "designs that answer the wrong question reproducibly. Whether this workflow "
    "generalizes beyond one paper is asserted, not demonstrated. The record it "
    "leaves behind, the decision log, the preregistrations with their amendments, "
    "the verification gates, and the session transcripts, is published so that the "
    "assertion can be tested by someone other than its authors."
)

def mk(idx, goal, proposition, dep, deptypes, prose, serves_L2, sets_up, topic, closing, flags, citations, numbers, notes):
    return {
        "id": idx, "section": "S6", "goal": goal, "proposition": proposition,
        "depends_on": dep, "dep_types": deptypes,
        "review": {"serves_L2": serves_L2, "serves_L1": "M5 DISCUSSION (inverse gradient; D-11 no provenance section; no Conclusion)",
                   "sets_up": sets_up, "topic_sentence": topic, "closing_sentence": closing,
                   "status": "drafted", "flags": flags},
        "draft_prose": prose,
        "audit": {"status": "complete", "citations": citations, "numbers": numbers, "notes": notes}
    }

s6 = [
    mk("S6-P1", "scope_limit", "Mechanism scope (estimated scale; congeniality) + the discussion roadmap.",
       ["S4-P6", "S5-P14"], ["qualifies", "builds_on"], P1, "S6-SP1 (framing)", "P2-P8",
       "The result is scoped by its own mechanism, and the scope comes first.",
       "...one conjecture, three directions, and the answer to the question the paper opened with.",
       "S6 drafted at 8 paragraphs vs blueprint estimate 9-11 (G-limits grouped two per paragraph).",
       {"mengMultipleImputationInferencesUncongenial1994a": "verified (read in-session)"},
       {}, "Quarried from 180e2b5 discussion opening."),
    mk("S6-P2", "scope_limit", "G1 ((A)+(C) magnitude, firm/not-firm split) + G2 (proper-MI carry-over structural).",
       ["S4-P7b", "S4-P15"], ["qualifies", "qualifies"], P2, "S6-SP1", "-",
       "The absolute magnitude of $(A)+(C)$ is not independently pinned, and this qualifies the theorem.",
       "...no dedicated proper-MI replication of the differential experiments exists.",
       None, {}, {"G1 standing split": "deriv:sec-lrt-ac"}, "G1+G2."),
    mk("S6-P3", "scope_limit", "G3 (engine robustness empirical, scoped) + G4 (floor is a measurement).",
       ["S5-P14", "S5-P11"], ["qualifies", "qualifies"], P3, "S6-SP1", "-",
       "Imputation-engine robustness is empirical and scoped, and this qualifies @sec-simulations.",
       "No argument here shows that no estimator built from the same observed data could do better.",
       None, {}, {}, "G3+G4."),
    mk("S6-P4", "scope_limit", "G5 (misspecification O(1) coexists) + G6 (MVN instantiation, D-07).",
       ["S4-P13", "S4-P6"], ["qualifies", "qualifies"], P4, "S6-SP1", "-",
       "For dissimilar candidate pairs, a mechanism-independent misspecification $O(1)$ coexists with the design-imbalance $O(1)$.",
       "...every constant is verified, symbolically and by simulation, only in the normal family.",
       None, {}, {}, "G5+G6 (G6 = D-07)."),
    mk("S6-P5", "scope_limit", "The power-dominance conjecture, labeled, with its partial support pointed at S5.",
       ["S4-P14"], ["qualifies"], P5, "S6-SP2", "-",
       "One question is left as a conjecture, and it is labeled as one.",
       "We state no theorem.",
       None, {}, {"partial support": "verif:verification/W2-lrt-power.R"}, "The conjecture (T-04: labeled)."),
    mk("S6-P6", "position_lineage", "Three directions: covariate shift (Shimodaira SS8), exact-engine replication, selection-aware calibration + beyond-normal (sequel, D-06).",
       ["S6-P4"], ["builds_on"], P6, "S6-SP3", "-",
       "Three directions seem most worth pursuing.",
       "...as is the extension beyond the normal family.",
       None,
       {"shimodairaInformationCriterionModel2017": "verified (read in-session; SS8 future work)",
        "shimodairahidetoshiImprovingPredictiveInference2000": "verified (read in-session; weighting machinery)"},
       {}, "Quarried; D-06 sequel scope respected."),
    mk("S6-P7", "summarize", "The plain-language replication-principle verdict: criterion yes; null-side decisions yes; signal-side no, irreducibly; the applied summary.",
       ["S5-P11", "S1-P3"], ["builds_on", "summarizes"], P7, "S6-SP4 (the takeaway block)", "-",
       "The paper closes where it began, with the replication principle.",
       "There, the honest answer is that the data no longer say.",
       None, {}, {}, "The broadening turn; no numbers (D-03-A1 permits summaries here, none needed)."),
    mk("S6-P8", "evaluate_evidence", "The workflow reflection, trust-ordered: what it caught (on the record), what it cost, what it cannot catch, what is asserted vs demonstrated; the published record as the test.",
       ["S3-P8", "S6-P7"], ["builds_on", "builds_on"], P8, "S6-SP5 (the close)", "-",
       "A final word on the workflow, held to the same standard as everything it produced.",
       "...so that the assertion can be tested by someone other than its authors.",
       None, {},
       {"the catches on the record": "xmodel:verification/cache/derivation-audit-run-w2diff.json",
        "published transcripts": "verif:verification/collaboration-analysis.md"},
       "The close; D-13 transcripts referenced; no provenance section follows (D-11)."),
]

l3["paragraphs"].extend(s6)
l3["metadata"]["status"] = "all_six_sections_drafted"
l3["metrics_gate"]["notes"] = (
    "ALL SIX SECTIONS DRAFTED (2026-06-07): S1 7 + S2 13 + S3 8 + S4 23 + S5 14 + "
    "S6 8 = 73 paragraphs. compile_enabled remains false pending Marcus's "
    "per-paragraph passes (D-12) and the regeneration gate. Flags: S1 length; S1 "
    "decomposition-sentence placement; S1-P6 'improper'; S5 14 vs 10-13; S6 8 vs "
    "9-11; P20 outcome-phrasing soften pending."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)
l4["evidence_map"].extend([
    {"id": "E-S6-P5-1", "proposition_id": "S6-P5", "pointer": "verif:verification/W2-lrt-power.R", "evidence_status": "verified",
     "passage_or_value": "Power arms + size-adjusted analysis.", "note": "Partial support for the labeled conjecture."},
    {"id": "E-S6-P6-1", "proposition_id": "S6-P6", "pointer": "lit:shimodairaInformationCriterionModel2017", "evidence_status": "verified",
     "passage_or_value": "SS8: mechanism combinations named as future work.", "note": "Direction 1."},
    {"id": "E-S6-P8-1", "proposition_id": "S6-P8", "pointer": "verif:verification/collaboration-analysis.md", "evidence_status": "verified",
     "passage_or_value": "The committed collaboration analysis; transcripts public per D-13.", "note": "The record the reflection points to."},
])
l4["metrics_gate"]["notes"] = "S1-S6 populated (87 entries); all pointers resolve. Full gate at compile."

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S6 drafted: 8 paragraphs, 3 evidence entries - ALL SIX SECTIONS DRAFTED")
