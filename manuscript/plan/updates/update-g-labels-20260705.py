# G-label readability (Marcus, 2026-07-05): (1) the Discussion's opening paragraph now
# introduces the notation ("labeled G1 through G9") so the reader does not meet **G1.**
# cold; (2) each G-limit starts its own paragraph -- S6-P2/P3/P4 each carried two limits
# in one paragraph (G1+G2, G3+G4, G5+G6); G7-G9 already stand alone. Prose content of
# every limit is untouched; the splits insert a paragraph break only.
# Guards: unique-substring asserts; any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

SUBS = [
    ("S6-P1",
     "nine specific limits remain, each stated next to the claim it qualifies",
     "nine specific limits remain, labeled G1 through G9, each stated next to the claim it qualifies"),
    ("S6-P2", " **G2.**", "\n\n**G2.**"),
    ("S6-P3", " **G4.**", "\n\n**G4.**"),
    ("S6-P4", " **G6.**", "\n\n**G6.**"),
]

for pid, old, new in SUBS:
    p = para[pid]
    cur = p["draft_prose"]
    if cur.count(old) != 1:
        raise SystemExit(f"{pid}: substring count {cur.count(old)} != 1 -- aborting:\n  {old[:60]}")
    p["draft_prose"] = cur.replace(old, new)
    print(f"{pid}: applied.")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("done: 4 units touched.")
