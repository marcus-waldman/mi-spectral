# Evidence-map table (S5-P1b): add apa-longtable="true" to {#tbl-evidence-map} so the
# extension's apafloatlatex.lua skips the table-float wrapper (a longtable inside a
# float cannot break pages -- the rendered Table 1 clipped at the page bottom and its
# remaining rows were lost; Marcus's report 2026-07-05). Rendering attribute only; the
# caption text and every table cell are untouched.
# Guards: unique-substring assert; any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

OLD = "{#tbl-evidence-map}"
NEW = '{#tbl-evidence-map apa-longtable="true"}'

p = para["S5-P1b"]
cur = p["draft_prose"]
if cur.count(OLD) != 1:
    raise SystemExit(f"S5-P1b: substring count {cur.count(OLD)} != 1 -- aborting.")
p["draft_prose"] = cur.replace(OLD, NEW)
print("S5-P1b: apa-longtable attribute added.")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("done: 1 unit touched.")
