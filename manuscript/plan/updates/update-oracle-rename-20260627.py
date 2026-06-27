# Conditioning-sense "oracle" rename (T-08 follow-up), 2026-06-27
#
# DECISION (Marcus, 2026-06-27): the conditioning-sense "oracle" -- the Q-function
# conditioned on the truth, E[l_com|Y_obs] under the data-generating law, which no real
# procedure can compute -- is renamed to "true-model expectation". This is consistent
# with the already-applied S5 rename "fitted-versus-oracle" -> "fitted-model-versus-
# true-model". The complete-data sense was renamed separately to "complete-data
# benchmark". After this edit the word "oracle" no longer appears in level3 prose.
#
# Targeted, meaning-preserving substring swaps in S3-P6, S4-P4, S4-P7 (5 occurrences).
# No number, math span, citation, or cross-reference changed.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
DEC = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\decisions.md"

# (paragraph id, old substring, new substring)
EDITS = [
    ("S3-P6",
     "defined at an oracle conditioned on the truth",
     "defined as the true-model expectation conditioned on the truth"),
    ("S3-P6",
     "the oracle conditioning had been silently substituted",
     "the true-model conditioning had been silently substituted"),
    ("S4-P4",
     "the oracle expectation $\\mathbb{E}",
     "the true-model expectation $\\mathbb{E}"),
    ("S4-P4",
     "not from an oracle.",
     "not from the true model."),
    ("S4-P7",
     "which is the oracle case of @eq-qbar",
     "which is the true-model case of @eq-qbar"),
]

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
by_id = {p["id"]: p for p in l3["paragraphs"]}

FLAG = "oracle-rename 2026-06-27 (T-08 follow-up): conditioning-sense 'oracle' -> 'true-model expectation' per Marcus."
touched = set()
for pid, old, new in EDITS:
    p = by_id[pid]
    prose = p["draft_prose"]
    assert prose.count(old) == 1, f"{pid}: expected exactly 1 of {old!r}, found {prose.count(old)}"
    p["draft_prose"] = prose.replace(old, new)
    touched.add(pid)

# guard: no conditioning-sense (or any) 'oracle' left in level3 prose
left = [p["id"] for p in l3["paragraphs"] if "oracle" in (p.get("draft_prose") or "").lower()]
assert not left, f"'oracle' still present in: {left}"

for pid in touched:
    fl = by_id[pid]["review"].get("flags")
    by_id[pid]["review"]["flags"] = (fl + " | " if fl else "") + FLAG

l3["metrics_gate"]["notes"] = (
    "Oracle rename 2026-06-27 (T-08 follow-up): conditioning-sense 'oracle' -> "
    "'true-model expectation' in S3-P6/S4-P4/S4-P7 (5 occurrences); 'oracle' no longer "
    "appears in level3 prose. Prior note: " + (l3["metrics_gate"].get("notes") or "")
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# decisions.md amendment
entry = (
    "\n## T-08 conditioning-sense rename (2026-06-27)\n\n"
    "The conditioning-sense \"oracle\" (the Q-function conditioned on the truth, "
    "$\\mathbb{E}[\\ell_{\\text{com}}\\mid Y_{\\text{obs}}]$ under the data-generating "
    "law, which no real procedure computes) is renamed to **\"true-model expectation\"** "
    "in S3-P6, S4-P4, and S4-P7. This completes T-08: the complete-data sense became "
    "\"complete-data benchmark\" (2026-06-26) and S5's \"fitted-versus-oracle\" became "
    "\"fitted-model-versus-true-model\". The word \"oracle\" no longer appears in level3 "
    "prose. (derivation.qmd, a separate sourced artifact, is out of scope for this prose "
    "pass and may retain its own usages.)\n"
)
with open(DEC, "a", encoding="utf-8") as f:
    f.write(entry)

print("oracle rename applied to:", sorted(touched))
print("decisions.md amended (T-08 conditioning-sense)")
