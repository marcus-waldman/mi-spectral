#!/usr/bin/env python3
"""
todo/037 precision pass, pattern-3 (mechanism accuracy) + pattern-2 (entry-point
self-containment): fix the S1-P6b Contributions list.

Item 1 sentence 2 attributed the bias to "the models that lost the most data" -- the
recurring mechanism error (all candidates are fit to the SAME imputed data; the
per-candidate driver is the model's own tr(RIV) / missing information). This twins the
abstract fix (53b96bc) and matches companion S1-P4. The orphaned "It grows" is joined
into a compound predicate at the same time. Item 2's bold run-in label "behind it"
carried a back-referencing pronoun at an entry point and is made self-contained.

Adversary verdict (independent, todo/037 charge): APPLY AS-IS, grounded in
derivation.qmd:93 / :1542 and S1-P4. No math/citation/number token changed.
Per-paragraph targeted replacement, idempotent.

Run:  py manuscript/plan/updates/update-s1p6b-mechanism-todo037-20260628.py
Then: py scripts/check_plan.py ; py scripts/mechanism_flag.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

R = {
    "S1-P6b": [
        ("the bias is specific to each candidate. It grows with the candidate's missing information, so the uncorrected criteria favor the models that lost the most data.",
         "the bias is specific to each candidate and grows with that candidate's missing information. The uncorrected criteria therefore favor the candidates with the most missing information."),
        ("2. **The deviance bias behind it.**",
         "2. **The deviance bias behind the correction.**"),
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

    with L3.open("w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"S1-P6b mechanism/entry-point fixes applied: {applied}, already-applied: {skipped} (of 2)")


if __name__ == "__main__":
    main()
