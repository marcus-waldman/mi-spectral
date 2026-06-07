# S3 Methods: the derivation and verification workflow - from-scratch draft, 2026-06-07
#
# Third Level-3 drafting cycle. NEW WRITING (no quarry; old S8's substance absorbed).
# Under the approved S3 blueprint (a21120a) + cycle decisions:
#   T-05: factual passive voice; the protocol described as procedure, not achievement.
#   Structural requirement: every gate paragraph ENDS with what it cannot catch.
#   Sign episode = the single narrative passage (P6).
#   Protocol records -> appendices (D-08 note); this section states the design.
#   Sits low on the technical gradient (unannounced).
#   Use-first openers + plain expository cadence per CLAUDE.md prose style.
# Eight paragraphs:
#   P1 roadmap (the question this section answers; six parts; tier preview; appendix pointer)
#   P2 roles and decision discipline             (blind spot: records, not correctness)
#   P3 sourced citations, mechanical enforcement (blind spot: existence, not understanding)
#   P4 claim pipeline + the four trust tiers     (blind spot: shared wrong setup passes both CAS)
#   P5 preregistration before code               (blind spot: disciplines reporting, validates nothing)
#   P6 cross-model blind + adversarial review; the fitted-vs-oracle sign episode
#                                                (blind spot: shared training corpora)
#   P7 reproducibility                           (blind spot: numbers, not meaning)
#   P8 closing: how to read the Results through this protocol
# Level 4: 11 entries appended.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

P1 = (
    "The derivations in this paper were produced by an AI system and verified under a "
    "protocol that this section states as the paper's methods. The section answers one "
    "question: why the results that follow deserve the same scrutiny, no more and no "
    "less, that is applied to human-derived mathematics. The protocol has six parts: "
    "roles and decision records; sourced citations; a verification pipeline with "
    "explicit trust tiers; preregistration of every simulation; adversarial cross-model "
    "review; and full reproducibility. Each part is stated below together with what it "
    "can catch and what it cannot. The complete protocol records --- decision logs, "
    "grading sheets, amendment histories, and the enforcement code --- are collected in "
    "the appendices and the public repository; this section states the design."
)

P2 = (
    "**Roles and decision records.** Direction, scope, and the acceptance or rejection "
    "of every result were decided by the human author of record; derivations, drafts, "
    "and computations were produced by an AI assistant. Each strategic decision was "
    "recorded with its date, the options rejected, and the rationale, and recorded "
    "decisions were not revisited without a dated amendment. The log is part of the "
    "public record, so the division of labor is auditable after the fact. What this "
    "discipline cannot do is certify correctness: recording who decided what catches "
    "nothing about whether a derivation is right. The remaining parts exist for that."
)

P3 = (
    "**Sourced citations.** Every claim about prior literature was pinned to a source "
    "document archived locally and read in the working session that used it. The rule "
    "was enforced mechanically: a pre-write check blocked any manuscript edit that "
    "cited a paper whose archived copy did not exist. Reliance on the AI system's "
    "trained recollection of a paper was prohibited throughout, because invented or "
    "misattributed citations are among the most common failures of AI-assisted "
    "scholarship. The enforcement has a stated limit: it checks existence and "
    "provenance, not understanding. A real passage can still be misread, and only "
    "review catches that."
)

P4 = (
    "**The claim pipeline and trust tiers.** Every analytic claim passed through a "
    "fixed sequence: derivation first, then symbolic verification in two independent "
    "computer-algebra systems, then Monte Carlo confirmation against criteria fixed in "
    "advance. Results are labeled throughout the paper by the gates they cleared. A "
    "claim is *firm* if it was derived in closed form and passed both symbolic systems "
    "and Monte Carlo. It is *measured* if it is a quantitative finding confirmed by "
    "preregistered simulation but not pinned in closed form. It is *structural* if it "
    "is argued from the form of the problem but not separately measured. Anything "
    "weaker is a *conjecture* and is labeled as one. These four labels are used in the "
    "Derivations and Simulation studies sections without further comment. The "
    "pipeline's limit is shared setup: both algebra systems verify the expressions "
    "they are given, so an error upstream of the algebra --- a wrong conditioning, a "
    "misstated expectation --- passes both. The next two parts exist for that class "
    "of error."
)

P5 = (
    "**Preregistration before code.** Every simulation in this paper was preregistered: "
    "predictions, designs, and pass criteria were committed to the repository before "
    "the simulation code was written. Changes were handled by dated amendments, "
    "themselves committed before any new runs. Predictions that failed are reported in "
    "the main text alongside those that held. The limit is stated directly: "
    "preregistration disciplines the reporting, and nothing more. A frozen prediction "
    "can rest on a wrong premise, and committing it early validates neither the "
    "derivation behind it nor the design that tests it."
)

P6 = (
    "**Cross-model adversarial review.** Load-bearing claims were re-derived blind by "
    "a model of an independent lineage, which was given the setup but not the result, "
    "and were then subjected to a second pass in which that model was instructed to "
    "refute each claim with the strongest available argument. The grading records are "
    "committed. One episode shows what this gate catches and is reported here as the "
    "worked example. The main theorem's sign depends on a conditioning choice: the "
    "averaged log-likelihood can be defined at the fitted imputation model, which is "
    "what multiple imputation computes, or at an oracle conditioned on the truth, "
    "which is not. Eight of nine blind re-derivations produced the opposite sign, "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$, because the oracle conditioning "
    "had been silently substituted. The error was not algebraic; every algebra check "
    "passed, because the algebra was correct for the definition it was given. The fork "
    "is now stated explicitly where the theorem is set up, with both conditionings and "
    "both signs. A derivation produced and checked within a single model lineage would "
    "likely have shipped one sign without noticing that there was a choice. The "
    "gate's limit is the mirror of its strength: independent lineages are trained on "
    "overlapping corpora, and an error common to the corpus can survive both."
)

P7 = (
    "**Reproducibility.** Every number in this paper regenerates from committed code. "
    "The simulations run from fixed entry points with fixed seeds; outputs are cached "
    "as committed artifacts; the software environment is recorded. Where a result is "
    "quoted in the text, its audit trail names the artifact it comes from. The limit "
    "is the usual one: reproducibility guarantees the numbers, not their meaning. A "
    "wrong design reproduces its artifact exactly."
)

P8 = (
    "Read with this section in hand, the rest of the paper carries its evidence with "
    "it. Each claim in the Derivations and Simulation studies sections arrives with a "
    "tier label and, where quantitative, a committed artifact behind it. The "
    "appendices hold the records; the repository holds everything. The protocol does "
    "not ask the reader to trust an AI derivation. It asks the reader to check one, "
    "and states where the checking has already been done and where it cannot be."
)

def mk(idx, goal, proposition, dep, deptypes, prose, serves_L2, sets_up, topic, closing, flags, citations, numbers, notes):
    return {
        "id": idx, "section": "S3", "goal": goal, "proposition": proposition,
        "depends_on": dep, "dep_types": deptypes,
        "review": {"serves_L2": serves_L2, "serves_L1": "M3 METHODS (methodological thesis; T-05; D-08 appendix note)",
                   "sets_up": sets_up, "topic_sentence": topic, "closing_sentence": closing,
                   "status": "drafted", "flags": flags},
        "draft_prose": prose,
        "audit": {"status": "complete", "citations": citations, "numbers": numbers, "notes": notes}
    }

s3 = [
    mk("S3-P1", "transition",
       "Roadmap: the question (why AI-derived results deserve normal scrutiny), the six parts, the tier preview, the appendix posture.",
       ["S1-P7"], ["builds_on"], P1, "S3 goal statement (framing)", "all S3 paragraphs; S4/S5 tier usage",
       "The derivations in this paper were produced by an AI system and verified under a protocol that this section states as the paper's methods.",
       "...this section states the design.",
       None, {}, {}, "Use-first roadmap; passive voice (T-05); appendix posture per D-08 note."),
    mk("S3-P2", "define_concept",
       "Roles and decision discipline: human author of record decides, AI produces; dated decision log with rejected options; blind spot = records not correctness.",
       ["S3-P1"], ["builds_on"], P2, "S3-SP1", "S3-P4..P7 (the verification parts)",
       "Direction, scope, and the acceptance or rejection of every result were decided by the human author of record; derivations, drafts, and computations were produced by an AI assistant.",
       "The remaining parts exist for that.",
       None, {}, {}, "Evidence: the decision log itself (manuscript/plan/decisions.md)."),
    mk("S3-P3", "define_concept",
       "Sourced citations with mechanical enforcement; trained-recollection reliance prohibited; blind spot = existence not understanding.",
       ["S3-P2"], ["builds_on"], P3, "S3-SP2", "every literature citation in the paper",
       "Every claim about prior literature was pinned to a source document archived locally and read in the working session that used it.",
       "A real passage can still be misread, and only review catches that.",
       None, {}, {}, "Evidence: the pre-write hook + the companion's source-passage apparatus."),
    mk("S3-P4", "define_concept",
       "The derive -> dual-CAS -> Monte Carlo pipeline; the four trust tiers defined once (firm / measured / structural / conjecture); blind spot = shared wrong setup passes both CAS.",
       ["S3-P2"], ["builds_on"], P4, "S3-SP3", "tier labels used throughout S4/S5",
       "Every analytic claim passed through a fixed sequence: derivation first, then symbolic verification in two independent computer-algebra systems, then Monte Carlo confirmation against criteria fixed in advance.",
       "The next two parts exist for that class of error.",
       None, {}, {}, "Tier definitions align with the todo/030 standing classes (T/M/E + conjecture)."),
    mk("S3-P5", "define_concept",
       "Preregistration before code, dated amendments, failures reported in main text; blind spot = disciplines reporting only.",
       ["S3-P4"], ["builds_on"], P5, "S3-SP4", "S5 (the preregistered account)",
       "Every simulation in this paper was preregistered: predictions, designs, and pass criteria were committed to the repository before the simulation code was written.",
       "...committing it early validates neither the derivation behind it nor the design that tests it.",
       None, {}, {}, "Evidence: todo/004 (frozen at ddc9037), todo/027, todo/005; amendment history within."),
    mk("S3-P6", "evaluate_evidence",
       "Cross-model blind re-derivation + instructed-to-refute pass; the fitted-vs-oracle sign episode as the worked example (8 of 9 opposite sign; error definitional, not algebraic); blind spot = shared training corpora.",
       ["S3-P4"], ["builds_on"], P6, "S3-SP5", "S4a (the two-conditioning statement, D-02)",
       "Load-bearing claims were re-derived blind by a model of an independent lineage, which was given the setup but not the result, and were then subjected to a second pass in which that model was instructed to refute each claim with the strongest available argument.",
       "...an error common to the corpus can survive both.",
       None, {},
       {"8 of 9 blind re-derivations produced the opposite sign": "deriv:sec-qfun"},
       "The single narrative passage of S3 (blueprint requirement). Model lineages deliberately unnamed in prose; named in the title-page declaration and appendices."),
    mk("S3-P7", "define_concept",
       "Reproducibility: fixed entry points, seeds, committed caches, environment records; blind spot = numbers not meaning.",
       ["S3-P5"], ["builds_on"], P7, "S3-SP6", "S5 setup; every quoted number's audit trail",
       "Every number in this paper regenerates from committed code.",
       "A wrong design reproduces its artifact exactly.",
       None, {}, {}, "Evidence: verification/run_all.R, verification/ic-ladder.R, cached artifacts + sessioninfo records."),
    mk("S3-P8", "transition",
       "Closing: how to read the Results through the protocol - check, don't trust; where checking is done and where it cannot be.",
       ["S3-P6", "S3-P7"], ["builds_on", "builds_on"], P8, "S3 rhetorical role", "S4 opening",
       "Read with this section in hand, the rest of the paper carries its evidence with it.",
       "It asks the reader to check one, and states where the checking has already been done and where it cannot be.",
       None, {}, {}, "Hands off to S4."),
]

l3["paragraphs"].extend(s3)
l3["metadata"]["status"] = "drafting_s3_complete"
l3["metrics_gate"]["notes"] = (
    "After S3 drafting (2026-06-07): S1 7 + S2 13 + S3 8 = 28 paragraphs; S3 is new "
    "writing (no quarry), zero literature citations by design (all evidence "
    "verif:/deriv:/xmodel:); every gate paragraph ends with its blind spot (blueprint "
    "structural requirement); dependency graph acyclic. Full gate when all six "
    "sections drafted."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)

l4["evidence_map"].extend([
    {"id": "E-S3-P2-1", "proposition_id": "S3-P2", "pointer": "verif:manuscript/plan/decisions.md",
     "evidence_status": "verified", "passage_or_value": "Dated decisions D-01..D-12, T-01..T-07, each with rejected options.",
     "note": "The decision log the paragraph describes."},
    {"id": "E-S3-P3-1", "proposition_id": "S3-P3", "pointer": "verif:.claude/hooks/check_citations.py",
     "evidence_status": "verified", "passage_or_value": "PreToolUse hook blocking unbacked citation tokens on manuscript/ + plan JSONs.",
     "note": "The mechanical enforcement."},
    {"id": "E-S3-P3-2", "proposition_id": "S3-P3", "pointer": "deriv:sec-sources",
     "evidence_status": "verified", "passage_or_value": "Source-passage apparatus in the companion derivation.",
     "note": "The archived-and-read discipline in practice."},
    {"id": "E-S3-P4-1", "proposition_id": "S3-P4", "pointer": "deriv:sec-verify",
     "evidence_status": "verified", "passage_or_value": "Dual-CAS + MC verification apparatus (executable Appendix B).",
     "note": "The pipeline the tiers are defined by."},
    {"id": "E-S3-P5-1", "proposition_id": "S3-P5", "pointer": "verif:todo/004-simulation-hypotheses.md",
     "evidence_status": "verified", "passage_or_value": "W1/W2/W3 preregistration frozen at SHA ddc9037; dated amendments.",
     "note": "Preregistration-before-code, instance 1."},
    {"id": "E-S3-P5-2", "proposition_id": "S3-P5", "pointer": "verif:todo/027-ladder-preregistration.md",
     "evidence_status": "verified", "passage_or_value": "IC-ladder preregistration with frozen pass criteria C1-C6.",
     "note": "Instance 2."},
    {"id": "E-S3-P5-3", "proposition_id": "S3-P5", "pointer": "verif:todo/005-comprehensive-sweep-hypotheses.md",
     "evidence_status": "verified", "passage_or_value": "Comprehensive-sweep preregistration H1-H6.",
     "note": "Instance 3."},
    {"id": "E-S3-P6-1", "proposition_id": "S3-P6", "pointer": "xmodel:verification/cache/derivation-audit-run-w2diff.json",
     "evidence_status": "verified", "passage_or_value": "Cross-model gate record (blind Mode A + adversarial Mode B, sustained).",
     "note": "The committed grading record the paragraph cites."},
    {"id": "E-S3-P6-2", "proposition_id": "S3-P6", "pointer": "deriv:sec-qfun",
     "evidence_status": "verified", "passage_or_value": "Fitted-vs-oracle callout: both conditionings, both signs; the 8/9 blind episode.",
     "note": "The sign-episode resolution in the companion."},
    {"id": "E-S3-P7-1", "proposition_id": "S3-P7", "pointer": "verif:verification/run_all.R",
     "evidence_status": "verified", "passage_or_value": "Single entry point, seeds, phase caches.",
     "note": "Reproducibility instance 1."},
    {"id": "E-S3-P7-2", "proposition_id": "S3-P7", "pointer": "verif:verification/ic-ladder.R",
     "evidence_status": "verified", "passage_or_value": "Seeded (20260604+r), core-count-invariant; sessioninfo recorded.",
     "note": "Reproducibility instance 2."},
])
l4["metrics_gate"]["notes"] = (
    "S1 + S2 + S3 populated; every drafted paragraph with a proposition has >=1 entry; "
    "all pointers resolve. Full gate when all sections drafted."
)

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S3 drafted: 8 paragraphs into level3, 11 evidence entries into level4")
