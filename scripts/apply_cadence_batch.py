#!/usr/bin/env python3
"""
Apply a cadence-pass batch (list of {paragraph_id, rewrite}) to level3, replacing
each paragraph's draft_prose with its rewrite -- but ONLY if the math ($...$ /
$$...$$), citation/cross-ref (@...), and prose-number token multisets match the
CURRENT draft_prose exactly. Any mismatch is skipped and reported (no silent token
drift). Idempotent.

  py scripts/apply_cadence_batch.py verification/cache/cadence-batch2.json
"""
import json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

MATH = re.compile(r"\$\$.*?\$\$|\$[^$]*\$", re.S)
REF = re.compile(r"@[A-Za-z0-9:_\-]+")
NUM = re.compile(r"\d[\d.,]*\d|\d")


def tokens(s):
    math = sorted(MATH.findall(s))
    refs = sorted(REF.findall(s))
    nums = sorted(NUM.findall(MATH.sub(" ", s)))
    return math, refs, nums


def main():
    batch = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    d = json.loads(L3.read_text(encoding="utf-8"))
    by_id = {p["id"]: p for p in d["paragraphs"]}
    applied, skipped = [], []
    for item in batch:
        pid, rewrite = item["paragraph_id"], item.get("rewrite", "")
        if not rewrite:
            skipped.append((pid, "empty rewrite")); continue
        cur = by_id[pid]["draft_prose"]
        if cur == rewrite:
            skipped.append((pid, "already applied")); continue
        cm, cr, cn = tokens(cur)
        rm, rr, rn = tokens(rewrite)
        probs = []
        if cm != rm: probs.append(f"math {len(cm)}->{len(rm)} diff={sorted(set(cm)^set(rm))[:3]}")
        if cr != rr: probs.append(f"refs diff={sorted(set(cr)^set(rr))}")
        if cn != rn: probs.append(f"numbers cur-only={sorted(set(cn)-set(rn))} new-only={sorted(set(rn)-set(cn))}")
        if probs:
            skipped.append((pid, "; ".join(probs))); continue
        by_id[pid]["draft_prose"] = rewrite
        applied.append(pid)
    with L3.open("w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"applied {len(applied)}: {', '.join(applied)}")
    if skipped:
        print("SKIPPED:")
        for pid, why in skipped:
            print(f"  {pid}: {why}")


if __name__ == "__main__":
    main()
