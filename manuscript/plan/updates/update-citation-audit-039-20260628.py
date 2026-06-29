#!/usr/bin/env python3
"""Apply the todo/039 citation-audit adjudicated edits to level3-paragraphs.json.

Audit: 69 attachments / 35 sources, repo-grounded against literature/<key>.md,
flagged set independently re-verified (todo/039-citation-audit-results.md).
3 flagged attachments -> 3 edits (Marcus-confirmed 2026-06-28); plus 1 folded
consistency item (S4-P22 "developed separately", mirroring the 1a S6-P6 fix).

Edit 2 note (due diligence against the DATA): verification/W2-lrt-power.R C5 computes
chi2_SB = a*(d_L - bias) + b (a genuine scaled-AND-shifted statistic, df=1, ref chi^2_1),
so the prose "scaled-and-shifted" is ACCURATE and is kept; the audit's "drop shifted"
was driven by the sources, not the code. The fix reframes the two cites as the
scaled/adjusted-difference TRADITION (neither source gives the exact a*T+b form):
satorra2010 = scaled (mean-only); asparouhov2006 = mean-and-variance adjusted.

Two-pass: validate every `old` matches exactly once, THEN apply + write. Aborts on any
mismatch so no partial edit is written.
"""
import json
from pathlib import Path

L3 = Path(r"C:/Users/marcu/git-repositories/mi-spectral/manuscript/plan/level3-paragraphs.json")

# (loc, id, old, new, note)
EDITS = [
 ("S2-P7", "CA-01-misattributed",
  "This paper's analyst always uses the complete-data MLE, which is the case where congeniality implies properness [@mengMultipleImputationInferencesUncongenial1994a; @nielsenProperImproperMultiple2003].",
  "This paper's analyst always uses the complete-data MLE, which is the case where congeniality implies properness [@nielsenProperImproperMultiple2003].",
  "Meng (1994) text states only the CONVERSE non-implication and never invokes the MLE; the directional 'congeniality implies properness' (MLE case) is Nielsen 2003 Result 1. Drop Meng here (still cited S1-P6/S2-P9/S4-P5/S6-P1)."),
 ("S5-P6", "CA-02-partial-cite",
  r"By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006] referred to $\chi^2_1$.",
  r"By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic referred to $\chi^2_1$, in the scaled and adjusted chi-square difference tradition [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006].",
  "prose kept (code does a*T+b); cites reframed to the tradition -- 'scaled'=satorra2010, 'adjusted'=asparouhov2006 -- since neither gives the exact a*T+b form."),
 ("S4-P22", "CA-03-consistency",
  "Selection-aware refinements are developed separately.",
  "Selection-aware refinements are left to future work.",
  "fold-in: mirror the 1a S6-P6 fix ('developed separately' -> 'left to future work'); no published companion."),
]

doc = json.loads(L3.read_text(encoding="utf-8"))
paras = {p["id"]: p for p in doc["paragraphs"]}

def get_text(loc):
    return paras[loc]["draft_prose"]

def set_text(loc, txt):
    paras[loc]["draft_prose"] = txt

# ---- PASS 1: validate every old matches exactly once ----
work = {}
errors = []
for loc, cid, old, new, note in EDITS:
    if loc not in work:
        work[loc] = get_text(loc)
    n = work[loc].count(old)
    if n != 1:
        errors.append(f"  {cid} [{loc}]: old-string found {n}x (expected 1)")
    else:
        work[loc] = work[loc].replace(old, new)

if errors:
    print("ABORT -- old-string validation failed; NOTHING written:")
    print("\n".join(errors))
    raise SystemExit(1)

# ---- PASS 2: apply + write ----
for loc, txt in work.items():
    set_text(loc, txt)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"APPLIED {len(EDITS)} edits across {len(work)} locations.")
for loc, cid, old, new, note in EDITS:
    print(f"  {cid:22} [{loc}]")
print("\nParagraph count:", len(doc["paragraphs"]), "(expect 85)")
