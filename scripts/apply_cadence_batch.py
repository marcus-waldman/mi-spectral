#!/usr/bin/env python3
"""
Apply a cadence-pass batch (list of {paragraph_id, rewrite}) to level3, replacing
each paragraph's draft_prose with its rewrite -- but ONLY if the math ($...$ /
$$...$$), citation/cross-ref (@...), prose-number, AND newline-structure tokens match
the CURRENT draft_prose. Any mismatch is skipped and reported (no silent token or
structure drift). Idempotent.

  py scripts/apply_cadence_batch.py verification/cache/cadence-batch2.json
"""
import json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

MATH = re.compile(r"\$\$.*?\$\$|\$[^$]*\$", re.S)
REF = re.compile(r"@[A-Za-z0-9:_\-]+")
NUM = re.compile(r"\d[\d.,]*\d|\d")
LITNL = re.compile(r"\\n")               # literal backslash-n: the todo/035 render-breaker


def tokens(s):
    math = sorted(MATH.findall(s))
    refs = sorted(REF.findall(s))
    nums = sorted(NUM.findall(MATH.sub(" ", s)))
    return math, refs, nums


def check(cur, rewrite):
    r"""Reasons to skip this rewrite (empty list -> safe to apply).

    Guards the token multisets (math / refs / numbers) AND newline structure. The
    newline guard was added in todo/036: a literal backslash-n corruption (real
    newlines emitted as the two characters '\' then 'n' at heading/image boundaries)
    slipped past the token guard in todo/035 and broke the render with undefined
    control sequences. Reject any rewrite that changes the real newline count or
    introduces a literal '\n' outside math, so LaTeX control words like \nu or \neq
    inside $...$ never false-trigger.
    """
    cm, cr, cn = tokens(cur)
    rm, rr, rn = tokens(rewrite)
    probs = []
    if cm != rm: probs.append(f"math {len(cm)}->{len(rm)} diff={sorted(set(cm)^set(rm))[:3]}")
    if cr != rr: probs.append(f"refs diff={sorted(set(cr)^set(rr))}")
    if cn != rn: probs.append(f"numbers cur-only={sorted(set(cn)-set(rn))} new-only={sorted(set(rn)-set(cn))}")
    cur_nl, rw_nl = cur.count("\n"), rewrite.count("\n")
    if cur_nl != rw_nl:
        probs.append(f"newlines {cur_nl}->{rw_nl} (structure changed)")
    cur_lit = len(LITNL.findall(MATH.sub(" ", cur)))
    rw_lit = len(LITNL.findall(MATH.sub(" ", rewrite)))
    if rw_lit > cur_lit:
        probs.append(f"literal backslash-n {cur_lit}->{rw_lit} (would break render)")
    return probs


def main():
    batch = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    d = json.loads(L3.read_text(encoding="utf-8"))
    by_id = {p["id"]: p for p in d["paragraphs"]}
    applied, skipped = [], []
    for item in batch:
        pid, rewrite = item["paragraph_id"], item.get("rewrite", "")
        if not rewrite:
            skipped.append((pid, "empty rewrite")); continue
        if pid not in by_id:
            skipped.append((pid, "unknown id")); continue
        cur = by_id[pid]["draft_prose"]
        if cur == rewrite:
            skipped.append((pid, "already applied")); continue
        probs = check(cur, rewrite)
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
