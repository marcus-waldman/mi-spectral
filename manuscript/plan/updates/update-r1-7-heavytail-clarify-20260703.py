# r1#7 clarifying sentence (v1 AI-review response, Tier A, 2026-07-03)
#
# Reviewer conflated the per-dataset sample size N with the Monte Carlo repetition
# count: S5-P12 already said the N=1000 miss is "a consequence of the heavy-tailed
# per-repetition statistic, whose standard deviation grows with the sample size and
# leaves the larger cells unable to resolve an order-one offset at fixed repetition
# count" -- true, but it never states the repetition count explicitly or says the
# per-replicate variance is finite, so a reader can read "standard deviation grows"
# as the Monte Carlo standard ERROR of the pooled mean failing to shrink, which
# would indeed be invalid under infinite variance. One clarifying sentence: the
# repetition count (1000) is identical at every N, and the per-replicate spread is
# finite (heavy-tailed, not infinite-variance), so the figure's SE bars are valid,
# just wider at the largest cell. See manuscript/reviews/v1/response/response-letter.md r1#7.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

OLD = (
    "The cause is the per-repetition statistic, which has heavy tails, so its "
    "standard deviation grows with the sample size. At a fixed repetition count "
    "the larger cells therefore cannot resolve an order-one offset."
)
NEW = (
    "The cause is the per-repetition statistic, which has heavy tails, so its "
    "standard deviation grows with the sample size. The repetition count is the "
    "same $1000$ at every sample size; it is the per-replicate statistic's own "
    "spread that grows with $N$, and that spread is finite, so the figure's "
    "standard-error bars stay valid, just wider at the largest cell, and the "
    "larger cells therefore cannot resolve an order-one offset as tightly as the "
    "smaller ones."
)

found = False
for p in l3["paragraphs"]:
    if p["id"] == "S5-P12":
        if OLD not in p["draft_prose"]:
            raise SystemExit("S5-P12 draft_prose does not contain the expected OLD text -- aborting.")
        p["draft_prose"] = p["draft_prose"].replace(OLD, NEW)
        found = True
        break

if not found:
    raise SystemExit("S5-P12 not found in level3-paragraphs.json")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)

print("S5-P12 updated: added the repetition-count / finite-variance clarifying sentence.")
