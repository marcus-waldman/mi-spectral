# Sweep batch 3: S3 Methods to the D-26 register (todo/048 Phase D(ii)).
#
# Gate: Marcus approved manuscript/reviews/style/batch-S3-proposal-2026-07-05.md
# with the deliberate-call flag resolved as KEEP (the S3-P8 trust/check closing
# parallel stays verbatim). Five surgical repairs; S3-P3/S3-P7 untouched.
# The S3-P4 edit carries the authorized E3 thin (addendum, qmd :133).
# Guards: unique-substring asserts; any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

SUBS = [
    ("S3-P1",
     "One question motivates that protocol. Why do the results that follow deserve the "
     "same scrutiny that is applied to human-derived mathematics? The protocol answers "
     "that question in five parts.",
     "One question motivates that protocol: why do the results that follow deserve the "
     "same scrutiny that is applied to human-derived mathematics? The protocol answers "
     "in five parts."),
    ("S3-P4",
     "The sequence has a limit, and the limit is shared setup. Both algebra systems "
     "verify the expressions they are given. An error upstream of the algebra passes "
     "both. A wrong conditioning or a misstated expectation is exactly that kind of "
     "error.",
     "The sequence's limit is shared setup: both algebra systems verify the expressions "
     "they are given, so an error upstream of the algebra passes both, and a wrong "
     "conditioning or a misstated expectation is an error of that kind."),
    ("S3-P5",
     "alongside those that held. The limit is stated directly. Preregistration "
     "disciplines the reporting and nothing more,",
     "alongside those that held. Preregistration disciplines the reporting and nothing "
     "more,"),
    ("S3-P6",
     "The check's limit is the mirror of its strength. Independent model families are "
     "trained on overlapping corpora. An error common to the corpus can survive both.",
     "The check's limit mirrors its strength: independent model families are trained on "
     "overlapping corpora, so an error common to the corpus can survive both."),
    ("S3-P8",
     "Read with this section in hand, the rest of the paper carries its evidence with "
     "it. Each claim in the Derivations and Simulation studies sections arrives with a "
     "grade label. Each quantitative claim also arrives with a committed artifact "
     "behind it.",
     "Read with this section in hand, each claim in the Derivations and Simulation "
     "studies sections arrives with a grade label, and each quantitative claim arrives "
     "with a committed artifact behind it."),
]

for pid, old, new in SUBS:
    p = para[pid]
    cur = p["draft_prose"]
    if old not in cur:
        raise SystemExit(f"{pid}: expected substring not found -- aborting.")
    if cur.count(old) != 1:
        raise SystemExit(f"{pid}: substring not unique -- aborting.")
    p["draft_prose"] = cur.replace(old, new)
    print(f"{pid}: replaced (sub).")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("batch 3 applied: 5 units touched; S3-P3/S3-P7 untouched.")
