#!/usr/bin/env python3
r"""
Fluff / filler flagger (READ-ONLY scout for the todo/036 tightening pass).

Scans the manuscript prose (manuscript/plan/level3-paragraphs.json draft_prose) for
empty intensifiers, filler phrases, and vague force-metaphors -- the words that carry
no information and can be cut WITHOUT losing a logical step, a hedge, or a scope
condition. Ranks paragraphs worst-first by weighted fluff load so the tightening pass
hits the fluffiest paragraphs first. This is a deterministic CANDIDATE list, not a
verdict: whether a given hit is genuine fluff or load-bearing redundancy is decided
downstream (the proposed tightening + a single adversary + Marcus's call). The
weights only sort the work; nothing is cut here.

Deliberately NOT flagged (load-bearing per the todo/035 accuracy pass): "substantially"
(the softener on IC selection), "to leading order", "at the null", known-scale scope
words. "rather" excludes the contrastive "rather than".

  py scripts/fluff_flag.py [--out PATH] [--worst N]
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"


def _rx(body):
    return re.compile(r"\b" + body.replace(" ", r"\s+") + r"\b", re.I)


# (matcher, display label, category, weight). Weight reflects how reliably the phrase
# is empty: 1.0 = almost always cuttable; <1 = context-dependent, the adversary/Marcus
# decides. Categories: empty_phrase, force, intensifier, weak (often load-bearing).
FLUFF = []


def add(body, cat, w, rx=None):
    FLUFF.append((rx or _rx(body), body, cat, w))


# -- empty phrases: filler that adds words, never information --
for b in ["it is important to note", "it should be noted", "it is worth noting",
          "it is worth mentioning", "it is interesting to note", "as we have seen",
          "in order to", "due to the fact that", "owing to the fact that",
          "needless to say", "at the end of the day", "for all intents and purposes"]:
    add(b, "empty_phrase", 1.0)
for b, w in [("the fact that", 0.8), ("for the purpose of", 0.8),
             ("for the purposes of", 0.8), ("a number of", 0.8),
             ("it turns out that", 0.8), ("with respect to", 0.5),
             ("in terms of", 0.6), ("in relation to", 0.6),
             ("as (noted|mentioned|discussed)", 0.7)]:
    add(b, "empty_phrase", w)

# -- vague force / weight metaphors (Marcus called these out by name) --
add(r"gives? \w+ (its|their) force", "force", 1.0)
add(r"lends? \w+ (its|their) force", "force", 1.0)
add("its real force", "force", 1.0)
add(r"the (real )?force of (this|the|its)", "force", 0.8)
add(r"what gives \w+ (its|their) force", "force", 1.0)

# -- empty intensifiers --
for b in ["very", "quite", "somewhat", "basically", "obviously"]:
    add(b, "intensifier", 1.0)
for b, w in [("fairly", 0.9), ("simply", 0.9), ("essentially", 0.9),
             ("relatively", 0.8), ("plainly", 0.8)]:
    add(b, "intensifier", w)
add("rather", "intensifier", 0.8, rx=re.compile(r"\brather\b(?!\s+than)", re.I))

# -- weak / context-dependent: often load-bearing, so low weight (still surfaced) --
for b, w in [("just", 0.4), ("actually", 0.5), ("really", 0.5), ("indeed", 0.5),
             ("notably", 0.4), ("importantly", 0.5), ("clearly", 0.5),
             ("particularly", 0.3), ("especially", 0.3), ("of course", 0.6),
             ("naturally", 0.4), ("certainly", 0.5), ("evidently", 0.5),
             ("in fact", 0.5), ("there is", 0.3), ("there are", 0.3)]:
    add(b, "weak", w)


def clean(s):
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " M ", s)                     # protect math (decimals)
    s = re.sub(r"\[[^\]]*@[^\]]*\]", " ", s)
    s = re.sub(r"@[A-Za-z0-9:_\-]+", " ", s)
    s = re.sub(r"\{#[^}]*\}", " ", s)
    s = re.sub(r"!\[.*?\]\([^)]*\)", " ", s, flags=re.S)   # drop image markdown
    s = re.sub(r":::[^\n]*", " ", s)
    s = re.sub(r"^#+\s+", " ", s, flags=re.M)              # heading markers
    s = s.replace("**", " ")
    return s


def analyze(prose):
    text = clean(prose)
    words = len(text.split())
    if words < 1:
        return None
    hits, weighted, by_cat = [], 0.0, Counter()
    for rx, label, cat, w in FLUFF:
        n = len(rx.findall(text))
        if n:
            hits.append({"phrase": label, "category": cat, "count": n, "weight": w})
            weighted += n * w
            by_cat[cat] += n
    if not hits:
        return None
    raw = sum(h["count"] for h in hits)
    hits.sort(key=lambda h: -h["count"] * h["weight"])
    return {
        "words": words, "hits": raw, "weighted": round(weighted, 1),
        "density": round(weighted / words * 100, 2), "by_category": dict(by_cat),
        "flagged": hits,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(REPO / "verification" / "cache" / "fluff-scores.json"))
    ap.add_argument("--worst", type=int, default=15)
    args = ap.parse_args()

    d = json.loads(L3.read_text(encoding="utf-8"))
    rows = []
    for p in d["paragraphs"]:
        m = analyze(p.get("draft_prose") or "")
        if m:
            rows.append({"id": p["id"], "section": p["section"], **m})
    # worst-first: weighted fluff load, ties broken by density
    rows.sort(key=lambda r: (-r["weighted"], -r["density"]))

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps({"n_paragraphs": len(rows), "paragraphs": rows},
                                         indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"{len(rows)} paragraphs carry fluff candidates. "
          f"Worst-first (weighted load; density = weighted per 100 words):\n")
    print(f"{'id':8} {'sec':4} {'wrds':>4} {'hits':>4} {'wt':>5} {'dens':>5}  flagged (count)")
    for r in rows[:args.worst]:
        tags = ", ".join(f"{h['phrase']}x{h['count']}" for h in r["flagged"][:6])
        print(f"{r['id']:8} {r['section']:4} {r['words']:>4} {r['hits']:>4} "
              f"{r['weighted']:>5} {r['density']:>5}  {tags}")

    tot = Counter()
    for r in rows:
        for h in r["flagged"]:
            tot[h["phrase"]] += h["count"]
    print("\nmost common fluff phrases: "
          + ", ".join(f"{p}x{n}" for p, n in tot.most_common(15)))
    print(f"\ncorpus: {sum(r['hits'] for r in rows)} fluff hits across {len(rows)} paragraphs; "
          f"work-list -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
