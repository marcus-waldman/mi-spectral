#!/usr/bin/env python3
r"""
Color-commentary flagger (READ-ONLY scout for the todo/037 precision pass, pattern 4).

Scans the manuscript prose (manuscript/plan/level3-paragraphs.json draft_prose) for
EVALUATIVE NARRATION: sentences that tell the reader an object is important or narrate
the "work" it does, instead of stating the object and its consequence. For an expert
reviewer this is padding that invites "don't tell me, show me". Generalizes the
`force_metaphor` category already in fluff_flag.py ("gives it its force") to the whole
evaluative-narration class (key/crucial/essential, heart/crux, heavy lifting, workhorse,
"what makes X work", "does real work", "plays a role").

Ranks paragraphs worst-first by weighted load so the precision pass hits the most
editorialized paragraphs first. This is a deterministic CANDIDATE list, not a verdict:
the keep-rule guard (handoff todo/037) keeps the rare gloss that genuinely aids
comprehension ("We use Result 3.2 here" stays; "Result 3.2 does the real work here"
goes) -- the call is made downstream by the proposed rewrite + a single adversary +
Marcus.

Deliberately NOT flagged: factual uses of "carries"/"drives" (e.g. "the difference
carries a differential bias" -- a real quantity, not a role gloss); the scout restricts
those to role-noun objects. "use"/"apply" a result is never color commentary.

  py scripts/color_commentary_flag.py [--out PATH] [--worst N]
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

COLOR = []


def add(pattern, label, w):
    COLOR.append((re.compile(pattern, re.I), label, w))


# -- force / weight metaphors (the fluff_flag force category, kept here too) --
add(r"\bgives?\s+\w+\s+(its|their)\s+force\b", "gives X its force", 1.0)
add(r"\blends?\s+\w+\s+(its|their)\s+force\b", "lends X its force", 1.0)
add(r"\bthe\s+(real\s+)?force\s+of\s+(this|the|its)\b", "the force of", 0.8)
add(r"\bwhat\s+gives\s+\w+\s+(its|their)\s+force\b", "what gives X its force", 1.0)

# -- "does the work" narration --
add(r"\bdoes?\s+(the\s+)?(real|actual|hard)\s+work\b", "does real work", 1.0)
add(r"\bdoes?\s+(the\s+)?heavy\s+lifting\b", "does the heavy lifting", 1.0)
add(r"\bthe\s+workhorse\b", "the workhorse", 1.0)
add(r"\bwhat\s+makes\s+(it|this|that|the\s+\w+)\s+work\b", "what makes X work", 0.9)
add(r"\bis\s+what\s+(makes|drives|gives|powers)\b", "is what makes/drives", 0.9)

# -- importance assertions: telling the reader what to find important --
# NB: "central" is deliberately EXCLUDED -- "this paper's central result/object/matrix"
# is the CLAUDE-endorsed motivate-by-use opener, not evaluative narration.
add(r"\b(the\s+)?(key|crucial|essential|critical|pivotal)\s+"
    r"(assumption|ingredient|step|fact|point|idea|insight|observation|property|"
    r"feature|move|object|quantity|term|result)\b",
    "key/crucial <noun>", 1.0)
add(r"\bcrucially\b", "crucially", 1.0)
add(r"\bimportantly\b", "importantly", 0.7)
add(r"\bcritically\b", "critically", 0.7)
add(r"\b(the\s+)?(heart|crux|core|essence|linchpin)\s+of\b", "heart/crux of", 0.9)
add(r"\b(lies?|sits?|stands?)\s+at\s+the\s+(heart|core|center|centre)\b",
    "lies at the heart", 0.9)
add(r"\bplays?\s+a\s+(key|crucial|central|pivotal|major|important|critical)?\s*role\b",
    "plays a role", 0.8)
add(r"\bload-bearing\b", "load-bearing (house jargon)", 1.0)

# -- role gloss with a load-bearing object (restricted so factual "carries a bias"
#    is NOT flagged) --
add(r"\b(carries|drives|powers|underpins|anchors)\s+(the\s+)?"
    r"(argument|theorem|result|proof|claim|correction|theory|analysis|case)\b",
    "carries/drives the <argument>", 0.8)
add(r"\bdoes\s+(the\s+)?real\s+work\s+(in|for|here)\b", "does real work in/for", 1.0)


def clean(s):
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " M ", s)
    s = re.sub(r"\[[^\]]*@[^\]]*\]", " ", s)
    s = re.sub(r"@[A-Za-z0-9:_\-]+", " ", s)
    s = re.sub(r"\{#[^}]*\}", " ", s)
    s = re.sub(r"!\[.*?\]\([^)]*\)", " ", s, flags=re.S)
    s = re.sub(r":::[^\n]*", " ", s)
    s = re.sub(r"^#+\s+", " ", s, flags=re.M)
    s = s.replace("**", " ")
    return s


def analyze(prose):
    text = clean(prose)
    words = len(text.split())
    if words < 1:
        return None
    hits, weighted, examples = [], 0.0, []
    for rx, label, w in COLOR:
        found = rx.findall(text)
        n = len(found)
        if n:
            hits.append({"phrase": label, "count": n, "weight": w})
            weighted += n * w
            m = rx.search(text)
            if m:
                examples.append(m.group(0).strip())
    if not hits:
        return None
    raw = sum(h["count"] for h in hits)
    hits.sort(key=lambda h: -h["count"] * h["weight"])
    return {
        "words": words, "hits": raw, "weighted": round(weighted, 1),
        "flagged": hits, "examples": examples[:6],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(REPO / "verification" / "cache" / "color-commentary-scores.json"))
    ap.add_argument("--worst", type=int, default=20)
    args = ap.parse_args()

    d = json.loads(L3.read_text(encoding="utf-8"))
    rows = []
    for p in d["paragraphs"]:
        m = analyze(p.get("draft_prose") or "")
        if m:
            rows.append({"id": p["id"], "section": p["section"], **m})
    rows.sort(key=lambda r: (-r["weighted"], -r["hits"]))

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps({"n_paragraphs": len(rows), "paragraphs": rows},
                                         indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"{len(rows)} paragraphs carry color-commentary candidates. Worst-first:\n")
    print(f"{'id':8} {'sec':4} {'wrds':>4} {'hits':>4} {'wt':>5}  flagged (count) | example")
    for r in rows[:args.worst]:
        tags = ", ".join(f"{h['phrase']}x{h['count']}" for h in r["flagged"][:4])
        ex = r["examples"][0] if r["examples"] else ""
        print(f"{r['id']:8} {r['section']:4} {r['words']:>4} {r['hits']:>4} "
              f"{r['weighted']:>5}  {tags} | {ex}")

    tot = Counter()
    for r in rows:
        for h in r["flagged"]:
            tot[h["phrase"]] += h["count"]
    print("\nmost common color-commentary phrases: "
          + ", ".join(f"{p}x{n}" for p, n in tot.most_common(15)))
    print(f"\ncorpus: {sum(r['hits'] for r in rows)} hits across {len(rows)} paragraphs; "
          f"work-list -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
