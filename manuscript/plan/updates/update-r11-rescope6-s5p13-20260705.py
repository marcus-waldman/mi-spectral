# R11 rescope #6 (S5-P13) -- the D-26 straggler, applied per Marcus's gate (todo/049,
# 2026-07-05). Authorized at D-26 ("The addendum's six E2 rescopes are AUTHORIZED",
# precision-addendum-2026-07-05.md item 6) but missing from the S5 batch script, which
# touched S5-P13 only for the caption convention. Ratified wording from the addendum.
# Guards: unique-substring assert; any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

OLD = "and the two arms differ by exactly the posterior-draw imputation variance"
NEW = "and the difference between the two arms matches the predicted posterior-draw imputation variance"

p = para["S5-P13"]
cur = p["draft_prose"]
if cur.count(OLD) != 1:
    raise SystemExit(f"S5-P13: substring count {cur.count(OLD)} != 1 -- aborting.")
p["draft_prose"] = cur.replace(OLD, NEW)
print("S5-P13: R11 rescope #6 applied.")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("done: 1 unit touched.")
