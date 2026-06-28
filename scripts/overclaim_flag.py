#!/usr/bin/env python3
"""
Overclaim / sweeping-claim flagger (READ-ONLY scout for the accuracy pass).

Scans the manuscript prose (manuscript/plan/level3-paragraphs.json draft_prose)
for precision / universality / completeness / necessity words and lists every
sentence that carries one, ranked worst-first by trigger count. This is the
deterministic work-list; whether each flagged claim is actually BACKED at its
asserted strength is decided downstream (adversarial verification against the
derivation proofs, the simulation results, and the firm/measured/structural/
conjecture grade). The flag is a candidate, not a verdict.

  py scripts/overclaim_flag.py [--out PATH]   # writes JSON + prints worst-first summary
"""
import argparse, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

TRIGGERS = {
    "precision": ["exactly", "precisely", "exact", "identical", "identically",
                  "coincides", "reproduces", "restores", "restore", "recovers",
                  "recover", "equals", "the same"],
    "universality": ["always", "never", "every", "all", "any", "none", "each",
                     "universal", "universally", "uniform", "uniformly",
                     "invariant", "throughout", "everywhere", "in general",
                     "in every", "for all"],
    "completeness": ["complete", "completely", "fully", "full", "entire",
                     "entirely", "wholly", "perfect", "perfectly", "total"],
    "necessity": ["must", "cannot", "guarantees", "guarantee", "ensures",
                  "ensure", "proves", "proven", "necessarily", "certainly",
                  "clearly", "obviously", "trivially", "simply", "immediately",
                  "of course", "strictly", "only", "purely", "solely"],
}
ALL_TRIG = sorted({w for v in TRIGGERS.values() for w in v}, key=len, reverse=True)
TRIG_RE = {w: re.compile(r"\b" + re.escape(w) + r"\b", re.I) for w in ALL_TRIG}
GRADES = ["firm", "measured", "structural", "conjecture"]


def clean(s):
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " §M ", s)                    # protect math (decimals!)
    s = re.sub(r"\[[^\]]*@[^\]]*\]", " ", s)
    s = re.sub(r"@[A-Za-z0-9:_\-]+", " ", s)
    s = re.sub(r"\{#[^}]*\}", " ", s)
    s = re.sub(r"!\[.*?\]\([^)]*\)", " ", s, flags=re.S)   # drop image markdown
    s = re.sub(r":::[^\n]*", " ", s)
    return s


def sentences(text):
    text = re.sub(r"\s+", " ", text).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(REPO / "verification" / "cache" / "overclaim-candidates.json"))
    args = ap.parse_args()

    d = json.loads(L3.read_text(encoding="utf-8"))
    cands, per_para = [], []
    for p in d["paragraphs"]:
        prose = p.get("draft_prose") or ""
        cleaned = clean(prose)
        grade = [g for g in GRADES if re.search(r"\b" + g + r"\b", prose, re.I)]
        n_para = 0
        for sent in sentences(cleaned):
            hits = sorted({w.lower() for w in ALL_TRIG if TRIG_RE[w].search(sent)})
            if hits:
                cands.append({
                    "id": p["id"], "section": p["section"], "goal": p.get("goal"),
                    "grade_words_in_paragraph": grade,
                    "sentence": sent.replace(" §M ", " <math> "),
                    "triggers": hits,
                })
                n_para += len(hits)
        if n_para:
            per_para.append((p["id"], p["section"], n_para))

    out = {"n_candidates": len(cands), "candidates": cands}
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    per_para.sort(key=lambda r: -r[2])
    print(f"{len(cands)} flagged sentences across {len(per_para)} paragraphs")
    print("\nworst-first (paragraph : trigger count):")
    for pid, sec, n in per_para[:20]:
        print(f"  {pid:8} [{sec}]  {n}")
    from collections import Counter
    tc = Counter(t for c in cands for t in c["triggers"])
    print("\nmost common triggers: " + ", ".join(f"{w}x{n}" for w, n in tc.most_common(20)))
    print(f"\ncandidates -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
