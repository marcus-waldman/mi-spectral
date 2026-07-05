# Sweep batch 5 follow-up (same gate): the @fig-ladder caption tail.
#
# The approved batch-S5 proposal's stated scope is "clears all 16 S5 vocabulary
# warnings"; the main script missed one instance -- the caption's closing
# "the weak-signal floor" -- leaving one S5 warning. This companion lands it,
# same commit, same Bucket-2 replacement the prose already uses (Demo 5's
# "shortfall").

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

p = {q["id"]: q for q in l3["paragraphs"]}["S5-P18"]
old = "no arm reaches it, the weak-signal floor."
new = "no arm reaches it, the weak-signal shortfall."
if p["draft_prose"].count(old) != 1:
    raise SystemExit("S5-P18: caption tail not found uniquely -- aborting.")
p["draft_prose"] = p["draft_prose"].replace(old, new)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S5-P18 caption tail: replaced.")
