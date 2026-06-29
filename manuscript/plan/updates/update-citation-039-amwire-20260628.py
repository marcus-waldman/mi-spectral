#!/usr/bin/env python3
"""todo/039 follow-up: wire the exact affine-form anchor into S5-P6.

After acquiring Asparouhov & Muthén (2010) "Simple Second Order Chi-Square
Correction" (Zotero J26NMQEW → Drive → Mathpix → lit-sync →
literature/asparouhovSimpleSecondOrder2010.md, read in-session), attach it to the
"scaled-and-shifted statistic" clause as the precise source of the affine T3 = a*T + b
(fixed df, ref chi^2_1) form the W2 C5 arm computes. The two SEM cites stay as the
scaled/adjusted-difference tradition (T1 scaled = satorra2010; T2 eff-df = asparouhov2006).
Verified: AM2010 eq. (4) T3 = T*sqrt(D/tr(M^2)) + D - sqrt(D*tr(M)^2/tr(M^2)).
"""
import json
from pathlib import Path

L3 = Path(r"C:/Users/marcu/git-repositories/mi-spectral/manuscript/plan/level3-paragraphs.json")
EDITS = [
 ("S5-P6", "CA-04-amwire",
  r"By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic referred to $\chi^2_1$, in the scaled and adjusted chi-square difference tradition [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006].",
  r"By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic [@asparouhovSimpleSecondOrder2010] referred to $\chi^2_1$, in the scaled and adjusted chi-square difference tradition [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006].",
  "attach AM2010 (exact affine a*T+b anchor) to the scaled-and-shifted clause; keep the two tradition cites"),
]

doc = json.loads(L3.read_text(encoding="utf-8"))
paras = {p["id"]: p for p in doc["paragraphs"]}
work, errors = {}, []
for loc, cid, old, new, note in EDITS:
    if loc not in work:
        work[loc] = paras[loc]["draft_prose"]
    n = work[loc].count(old)
    if n != 1:
        errors.append(f"  {cid} [{loc}]: old-string found {n}x (expected 1)")
    else:
        work[loc] = work[loc].replace(old, new)
if errors:
    print("ABORT -- validation failed; NOTHING written:"); print("\n".join(errors)); raise SystemExit(1)
for loc, txt in work.items():
    paras[loc]["draft_prose"] = txt
with open(L3, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False); f.write("\n")
print(f"APPLIED {len(EDITS)} edit(s).")
for loc, cid, old, new, note in EDITS:
    print(f"  {cid} [{loc}]")
print("Paragraph count:", len(doc["paragraphs"]), "(expect 85)")
