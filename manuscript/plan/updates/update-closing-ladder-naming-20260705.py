# D-26 sweep closing read, item 1: the "ladder" naming clause.
#
# D-26 kept "ladder" as a named construction ON CONDITION it is introduced
# explicitly at first use (Bucket-3 Option A). No section batch added the
# introduction; the closing whole-document read caught it. The construction is
# defined in S4-P19 (the three-step contrast), which precedes every later use
# (S5-P3, S5-P10, S5-P18, S5-P19), so the naming clause lands there.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

p = {q["id"]: q for q in l3["paragraphs"]}["S4-P19"]
old = (
    "that matches the first moment, the first two moments, or the entire null "
    "distribution and then measures what each step achieves."
)
new = (
    "that matches the first moment, the first two moments, or the entire null "
    "distribution and then measures what each step achieves; we call this graded "
    "comparison the distribution-matching ladder."
)
if p["draft_prose"].count(old) != 1:
    raise SystemExit("S4-P19: anchor not found uniquely -- aborting.")
p["draft_prose"] = p["draft_prose"].replace(old, new)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S4-P19: ladder naming clause added.")
