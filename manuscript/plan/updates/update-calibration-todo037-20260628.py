#!/usr/bin/env python3
"""
todo/037 precision pass -- CALIBRATION SET (all four patterns together, per-paragraph,
human-gated with a single independent adversary; Marcus rules each).

Each (old, new) pair is an approved precision rewrite: specificity (name the direction,
not "one/the other"), orphaned-pronoun joins, mechanism accuracy, color-commentary cuts.
Precision rewrites may legitimately ADD a math symbol (naming an estimator), so this goes
through the level3 update-script path rather than apply_cadence_batch.py (whose token
guard would reject the addition). Targeted replacement, idempotent.

Run:  py manuscript/plan/updates/update-calibration-todo037-20260628.py
Then: py scripts/check_plan.py

Approved paragraphs (adversary verdict in parens):
  S2-P2  -- pattern 1 specificity (name theta_obs -> theta_com) + 2 orphan joins
            (APPLY WITH REVISION: change 2 uses the named-anchor "The comparison")
  S2-P9  -- pattern 4 color cut ("is what gives the main theorem its force") +
            2 orphan joins; closing_sentence metadata synced (APPLY AS-IS)
  S2-P7  -- pattern 4 color cut ("does real work in the theorem" -> the concrete
            consequence "changes the bias the theorem derives") (APPLY AS-IS)
  S1-P4  -- pattern 2 orphan cluster: the metronomic "It reflects ... It vanishes ..."
            double-opener folded to one compound predicate (APPLY AS-IS)
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

R = {
    "S2-P2": [
        ("The complete-data maximum likelihood estimate $\\hat\\theta_{\\text{com}}$ is computable only when nothing is missing. It is the target an analyst would have reached with full data.",
         "The complete-data maximum likelihood estimate $\\hat\\theta_{\\text{com}}$ is computable only when no data are missing and is the target an analyst would have reached with full data."),
        ("The bias at the center of this paper compares likelihood values built around these two estimators. It measures what happens when values built around one estimator are read as if they were built around the other.",
         "The bias at the center of this paper compares the likelihood values built around these two estimators. The comparison measures what happens when a value built around the observed-data estimate $\\hat\\theta_{\\text{obs}}$ is read as if it were built around the complete-data target $\\hat\\theta_{\\text{com}}$."),
    ],
    "S2-P9": [
        ("The second standing assumption is congeniality. It says the imputer and the analyst must agree.",
         "The second standing assumption is congeniality, which requires the imputer and the analyst to agree."),
        ("Everything in this paper assumes congenial, proper imputation. This assumption is what gives the main theorem its force. The bias derived there is not an artifact of imputer-analyst disagreement. It is what remains after they agree.",
         "Everything in this paper assumes congenial, proper imputation. The bias derived in the main theorem is therefore not an artifact of imputer-analyst disagreement, but what remains after they agree."),
    ],
    "S2-P7": [
        ("The imputations this paper studies are proper in Rubin's sense, and the distinction between proper and improper imputation does real work in the theorem.",
         "The imputations this paper studies are proper in Rubin's sense, and whether imputation is proper or improper changes the bias the theorem derives."),
    ],
    "S1-P4": [
        ("The second term is smaller. It reflects imbalance between the observed and the missing units on the conditioning variables. It vanishes when the data are missing completely at random.",
         "The second term is smaller. It reflects imbalance between the observed and the missing units on the conditioning variables, and vanishes when the data are missing completely at random."),
    ],
}

# Metadata syncs (review fields that quote a now-changed sentence). plan hygiene only.
META = {
    "S2-P9": [
        ("closing_sentence",
         "It is what remains after they agree.",
         "The bias derived in the main theorem is therefore not an artifact of imputer-analyst disagreement, but what remains after they agree."),
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
                raise SystemExit(f"ERROR: {pid}: neither old nor new found:\n  OLD: {old!r}")
        by_id[pid]["draft_prose"] = prose

    meta_applied = meta_skipped = 0
    for pid, fields in META.items():
        review = by_id[pid]["review"]
        for field, old, new in fields:
            if review.get(field) == old:
                review[field] = new
                meta_applied += 1
            elif review.get(field) == new:
                meta_skipped += 1
            else:
                raise SystemExit(f"ERROR: {pid}.review.{field}: neither old nor new found:\n  OLD: {old!r}\n  GOT: {review.get(field)!r}")

    with L3.open("w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    n = sum(len(v) for v in R.values())
    nm = sum(len(v) for v in META.values())
    print(f"calibration fixes applied: {applied}, already-applied: {skipped} (of {n})")
    print(f"metadata syncs applied: {meta_applied}, already-applied: {meta_skipped} (of {nm})")


if __name__ == "__main__":
    main()
