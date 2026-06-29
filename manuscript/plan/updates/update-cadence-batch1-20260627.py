#!/usr/bin/env python3
"""
todo/035 style pass, batch 1: apply the 11 cadence rewrites accepted by the
cadence-style-pass workflow (fidelity / budget / cadence lenses, all pass).
Source of record: verification/cache/cadence-batch1.json.

Guard: each rewrite is applied only if its math ($...$), citation/cross-ref (@...),
and prose-number token multisets match the CURRENT draft_prose exactly. Any
mismatch is skipped and reported (no silent token drift). Idempotent.

Run:  py manuscript/plan/updates/update-cadence-batch1-20260627.py
Then: py scripts/check_plan.py ; py scripts/cadence_flag.py
"""
import json, re
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"
BATCH = REPO / "verification" / "cache" / "cadence-batch1.json"

MATH = re.compile(r"\$\$.*?\$\$|\$[^$]*\$", re.S)
REF = re.compile(r"@[A-Za-z0-9:_\-]+")
NUM = re.compile(r"\d[\d.,]*\d|\d")


def tokens(s):
    math = sorted(MATH.findall(s))
    refs = sorted(REF.findall(s))
    blanked = MATH.sub(" ", s)            # don't double-count math-internal digits
    nums = sorted(NUM.findall(blanked))
    return math, refs, nums


def main():
    accepted = json.loads(BATCH.read_text(encoding="utf-8"))
    d = json.loads(L3.read_text(encoding="utf-8"))
    by_id = {p["id"]: p for p in d["paragraphs"]}

    applied, skipped = [], []
    for item in accepted:
        pid, rewrite = item["paragraph_id"], item["rewrite"]
        cur = by_id[pid]["draft_prose"]
        if cur == rewrite:
            skipped.append((pid, "already applied"))
            continue
        cm, cr, cn = tokens(cur)
        rm, rr, rn = tokens(rewrite)
        problems = []
        if cm != rm:
            problems.append(f"math tokens differ ({len(cm)} vs {len(rm)})")
        if cr != rr:
            problems.append(f"citation/ref tokens differ: {set(cm)^set(rm)} {sorted(set(cr)^set(rr))}")
        if cn != rn:
            problems.append(f"numbers differ: cur-only={sorted(set(cn)-set(rn))} new-only={sorted(set(rn)-set(cn))}")
        if problems:
            skipped.append((pid, "; ".join(problems)))
            continue
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
