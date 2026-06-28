#!/usr/bin/env python3
r"""
Mechanism-accuracy flagger (READ-ONLY scout for the todo/037 precision pass, pattern 3).

Catches one specific, recurring mechanism error: attributing a DIFFERENT AMOUNT OF DATA
to a candidate model. Every candidate is fit to the SAME imputed data, so any phrasing
that says a model "lost the most data" / has "more data" / "less data" is wrong by
construction. The correct per-candidate driver is the model's own
tr(RIV) -- its missing information about the parameters. This twins the abstract fix
(53b96bc) and the standing accuracy invariant in CLAUDE.md.

The scout SPARES the correct vocabulary:
  - "missing data" / "data are missing" / "missing at random" -- the phenomenon, not a
    quantity attribution;
  - "missing information" / "relative increase in variance" / "tr(RIV)" -- the correct
    driver (a model CAN have more missing information; that is right).
It flags only DATA-quantity attributions. High precision, low recall by design: this is
a targeted guard for the known error class, not a broad style sweep.

  py scripts/mechanism_flag.py [--out PATH]
"""
import argparse, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

# Quantity / loss words that, when bound to "data", attribute differing data amounts to
# a model. "missing" is excluded by a negative lookahead so "missing data" never fires.
QUANT = r"(?:most|more|less|least|fewer|extra|additional)"
LOSS = r"(?:lose|loses|lost|losing|discard|discards|discarded|drop|drops|dropped|"\
       r"throw\s+away|threw\s+away|sacrifice|sacrifices|sacrificed)"

PATTERNS = [
    # "lost the most data", "discards more data"
    (re.compile(rf"\b{LOSS}\b(?:\s+the)?(?:\s+{QUANT})?\s+(?!missing\b)data\b", re.I),
     "lose/discard ... data"),
    # "more data", "the most data", "less data" -- but NOT "missing data"
    (re.compile(rf"\b{QUANT}\s+(?!missing\b)data\b", re.I),
     "more/less/most data"),
    # "data ... lost/discarded/thrown away"
    (re.compile(r"\bdata\s+(?:that\s+(?:is|are|was|were)\s+)?"
                r"(?:lost|discarded|dropped|thrown\s+away|sacrificed)\b", re.I),
     "data ... lost/discarded"),
    # "models/candidates that lose ... data"
    (re.compile(rf"\b(?:model|candidate)s?\s+(?:that|which)\s+\w+\s+(?!missing\b)data\b", re.I),
     "models that ... data"),
]


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
    hits = []
    for rx, label in PATTERNS:
        for m in rx.finditer(text):
            start = max(0, m.start() - 30)
            ctx = re.sub(r"\s+", " ", text[start:m.end() + 15]).strip()
            hits.append({"phrase": label, "match": m.group(0).strip(), "context": ctx})
    if not hits:
        return None
    return {"count": len(hits), "flagged": hits}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(REPO / "verification" / "cache" / "mechanism-scores.json"))
    args = ap.parse_args()

    d = json.loads(L3.read_text(encoding="utf-8"))
    rows = []
    for p in d["paragraphs"]:
        m = analyze(p.get("draft_prose") or "")
        if m:
            rows.append({"id": p["id"], "section": p["section"], **m})
    rows.sort(key=lambda r: -r["count"])

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps({"n_paragraphs": len(rows), "paragraphs": rows},
                                         indent=2, ensure_ascii=False), encoding="utf-8")

    if not rows:
        print("mechanism_flag: CLEAN -- no data-quantity attributions found.")
    else:
        print(f"mechanism_flag: {len(rows)} paragraph(s) with data-quantity attributions "
              f"(wrong by construction -- all candidates share the imputed data):\n")
        for r in rows:
            print(f"  {r['id']} ({r['section']}): {r['count']} hit(s)")
            for h in r["flagged"]:
                print(f"      [{h['phrase']}] ...{h['context']}...")
    print(f"\nwork-list -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
