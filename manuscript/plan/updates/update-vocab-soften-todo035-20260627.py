#!/usr/bin/env python3
"""
todo/035 follow-up (Marcus, 2026-06-27): soften the workflow / engineering-metaphor
vocabulary that scripts/corpus_vocab_check.py flagged as over-represented vs the
indexed literature and absent from the source papers. Priority 1 (positioning verb
`sits`; the metaphor words that leak into the technical sections S4-S6) AND
Priority 2 (the Methods/S1B density). Per-paragraph targeted replacements; no
claim, number, citation, cross-ref, or math token is changed. Idempotent.

False positives deliberately NOT changed: `scope`/`scoped` (standard usage),
`transcripts` (literal). `headline`/`perfect`/`shipped` left for the annotation pass.

Run:  py manuscript/plan/updates/update-vocab-soften-todo035-20260627.py
Then: py scripts/check_plan.py ; py scripts/corpus_vocab_check.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

# {paragraph id: [(exact current text, replacement), ...]}
R = {
    "S1-P6": [
        ("These results sit upstream of the test-calibration literature",
         "These results stand upstream of the test-calibration literature"),
        ("Two other routes sit nearby.", "Two other routes stand nearby."),
    ],
    "S1-P6b": [
        ("with transparent provenance and gates the reader can check. These are sourced citations,",
         "with transparent provenance and checks the reader can run. These are citations checked against their sources,"),
    ],
    "S2-P7": [
        ("the entire deterministic-EM lineage in which",
         "the entire deterministic-EM line of work in which"),
    ],
    "S3-P1": [
        ("The first is sourced citations. The second is a verification pipeline with explicit trust tiers.",
         "The first is citations checked against their sources. The second is a verification sequence with explicit trust grades."),
        ("the grading sheets, the amendment histories",
         "the assessment records, the amendment histories"),
    ],
    "S3-P3": [
        ("**Sourced citations.**", "**Citations checked against the source.**"),
        ("was pinned to a source document", "was traced to a source document"),
    ],
    "S3-P4": [
        ("**The claim pipeline and trust tiers.**", "**The verification sequence and trust grades.**"),
        ("by the gates they cleared.", "by the checks they passed."),
        ("but not pinned in closed form.", "but not established in closed form."),
        ("The pipeline has a limit,", "The sequence has a limit,"),
    ],
    "S3-P6": [
        ("by a model of an independent lineage.", "by a model from an independent family."),
        ("The grading records are committed.", "The assessment records are committed."),
        ("shows what this gate catches,", "shows what this check catches,"),
        ("within a single model lineage would likely", "within a single model family would likely"),
        ("The gate's limit is the mirror of its strength. Independent lineages are trained on overlapping corpora.",
         "The check's limit is the mirror of its strength. Independent model families are trained on overlapping corpora."),
    ],
    "S3-P8": [
        ("arrives with a tier label.", "arrives with a grade label."),
    ],
    "S4-P1": [
        ("one of the four tier labels defined", "one of the four grade labels defined"),
    ],
    "S4-P8": [
        ("The applications therefore sit in the estimated-scale regime.",
         "The applications therefore fall in the estimated-scale regime."),
    ],
    "S4-P10": [
        ("is graded in @sec-simulations.", "is assessed in @sec-simulations."),
    ],
    "S4-P11": [
        ("when the design sits near the invariance case.",
         "when the design lies near the invariance case."),
    ],
    "S4-P15": [
        ("The cross-model gate of @sec-methods", "The cross-model check of @sec-methods"),
    ],
    "S4-P17": [
        ("happens to sit at the exact equality case.", "happens to fall at the exact equality case."),
    ],
    "S4-P19": [
        ("This motivates a graded contrast, pre-registered",
         "This motivates a three-step contrast, pre-registered"),
    ],
    "S4-P21": [
        ("they were graded against.", "they were assessed against."),
    ],
    "S5-P1": [
        ("carries the *measured* tier of @sec-methods", "carries the *measured* grade of @sec-methods"),
    ],
    "S5-P3": [
        ("**Grading and registration.**", "**Assessment and registration.**"),
        ("Each study is graded against pass criteria", "Each study is assessed against pass criteria"),
    ],
    "S5-P6": [
        ("if it sits near nominal,", "if it lies near nominal,"),
    ],
    "S5-P11": [
        ("The run is graded on three separate points.", "The run is assessed on three separate points."),
        ("similar-pair headline is graded honestly against", "similar-pair headline is assessed honestly against"),
    ],
    "S5-P12": [
        ("which sits $1.3$ standard errors away.", "which lies $1.3$ standard errors away."),
        ("the grading reports only the totals", "the assessment reports only the totals"),
    ],
    "S5-P14": [
        ("Both sit near the nominal $0.05$.", "Both lie near the nominal $0.05$."),
        ("The uncorrected numerator sits at $0.042$ and the corrected one at $0.034$.",
         "The uncorrected numerator lies at $0.042$ and the corrected one at $0.034$."),
    ],
    "S5-P15": [
        ("The same statistic sits $52$ standard errors from",
         "The same statistic lies $52$ standard errors from"),
    ],
    "S5-P17": [
        ("The uncorrected criterion sits well below it,", "The uncorrected criterion lies well below it,"),
    ],
    "S5-P19": [
        ("equating points sit on the diagonal.", "equating points lie on the diagonal."),
    ],
    "S5-P21": [
        ("It sits three and a half standard errors from zero",
         "It lies three and a half standard errors from zero"),
        ("the differential sits below Monte Carlo resolution.",
         "the differential lies below Monte Carlo resolution."),
    ],
    "S4-P3": [
        ("an artifact of grading against the naive block-diagonal information.",
         "an artifact of comparing against the naive block-diagonal information."),
    ],
    "S6-P2": [
        ("is not independently pinned.", "is not independently determined."),
    ],
    "S6-P7b": [
        ("That evidence is sourced citations, independent symbolic checks,",
         "That evidence is citations checked against their sources, independent symbolic checks,"),
    ],
    "S6-P8": [
        ("the verification gates, and the session transcripts",
         "the verification checks, and the session transcripts"),
        ("hedged to their tier,", "hedged to their grade,"),
    ],
}


def main():
    d = json.loads(L3.read_text(encoding="utf-8"))
    by_id = {p["id"]: p for p in d["paragraphs"]}
    applied = skipped = 0
    for pid, subs in R.items():
        prose = by_id[pid]["draft_prose"]
        for old, new in subs:
            if old in prose:
                prose = prose.replace(old, new, 1)
                applied += 1
            elif new in prose:
                skipped += 1
            else:
                raise SystemExit(f"ERROR: in {pid}, neither old nor new found:\n  OLD: {old!r}")
        by_id[pid]["draft_prose"] = prose

    with L3.open("w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"vocab-soften applied: {applied} replacement(s), {skipped} already-applied.")


if __name__ == "__main__":
    main()
