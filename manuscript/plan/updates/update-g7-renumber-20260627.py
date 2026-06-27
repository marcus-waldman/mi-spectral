# Resolve the G-number collision (Marcus, 2026-06-27)
#
# The tribunal added a congeniality scope limit (S6-P4b) and provisionally numbered it
# "G6", colliding with the pre-existing MVN-instantiation limit (S6-P4, G6, D-07).
# RESOLUTION: the MVN limit keeps G6; the new congeniality limit becomes G7 (it sits
# after the MVN limit in the text). The collective range "G1-G6" -> "G1-G7" in the
# level1/level2 records. The MVN-specific G6 references (level1 "G6 says so" /
# "G6 in mi-spectral.qmd") are unchanged.

import json

L1 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level1-thesis.json"
L2 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level2-sections.json"
L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

# --- level3: renumber S6-P4b's congeniality limit G6 -> G7 ---
with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
p4b = next(p for p in l3["paragraphs"] if p["id"] == "S6-P4b")

assert p4b["draft_prose"].count("**G6.**") == 1
p4b["draft_prose"] = p4b["draft_prose"].replace("**G6.**", "**G7.**", 1)

assert "Congeniality limit (G6):" in p4b["proposition"]
p4b["proposition"] = p4b["proposition"].replace("Congeniality limit (G6):", "Congeniality limit (G7):")

old_flag = "G-number G6 provisional, Marcus may renumber."
assert old_flag in p4b["review"]["flags"]
p4b["review"]["flags"] = p4b["review"]["flags"].replace(
    old_flag, "G-number resolved to G7 (Marcus, 2026-06-27); the MVN limit keeps G6.")

# guard: S6-P4 (MVN) still G6; S6-P4b now G7; no duplicate G6 label across S6 prose
s6_labels = []
import re
for p in l3["paragraphs"]:
    if p.get("section") == "S6":
        s6_labels += re.findall(r"\*\*G\d+\.\*\*", p.get("draft_prose") or "")
assert s6_labels.count("**G6.**") == 1, f"G6 label count = {s6_labels.count('**G6.**')}"
assert s6_labels.count("**G7.**") == 1, f"G7 label count = {s6_labels.count('**G7.**')}"

l3["metrics_gate"]["notes"] = (
    "G-number collision resolved 2026-06-27: congeniality limit (S6-P4b) G6 -> G7; "
    "MVN limit (S6-P4) keeps G6; range G1-G6 -> G1-G7 in level1/level2. Prior note: "
    + (l3["metrics_gate"].get("notes") or "")
)
with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# --- level1 + level2: collective range G1-G6 -> G1-G7 (ranges only) ---
for path, expect in ((L1, 3), (L2, 2)):
    txt = open(path, encoding="utf-8").read()
    n = txt.count("G1-G6")
    assert n == expect, f"{path}: expected {expect} 'G1-G6', found {n}"
    txt = txt.replace("G1-G6", "G1-G7")
    # confirm the MVN-specific standalone 'G6' references survive in level1
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"{path.split(chr(92))[-1]}: {n} range(s) G1-G6 -> G1-G7")

# guard: MVN-specific G6 references intact in level1
l1txt = open(L1, encoding="utf-8").read()
assert "G6 says so" in l1txt and "G6 in mi-spectral.qmd" in l1txt, "MVN G6 ref lost in level1"

print("S6-P4b congeniality limit renumbered G6 -> G7; MVN limit keeps G6.")
