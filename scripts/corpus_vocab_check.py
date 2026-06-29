#!/usr/bin/env python3
"""
Corpus vocabulary check (READ-ONLY diagnostic).

Compares the manuscript prose (manuscript/plan/level3-paragraphs.json draft_prose)
against the indexed source literature (literature/*.md) and reports:

  A. unigrams the manuscript uses disproportionately to the field (weighted
     log-odds with an informative Dirichlet prior; Monroe-Colaresi-Quinn 2008),
     plus manuscript words ABSENT from the source corpus;
  B. the same for two-word phrases (content-word bigrams) -- catches cadence/
     construction tells a single-word list misses;
  C. a banned-vocabulary scan (CLAUDE.md T-03) + a flag list of the same
     engineering-metaphor family, each with paragraph-level locations.

Run after any drafting pass to watch the distribution:
  py scripts/corpus_vocab_check.py [--top 40] [--min 3] [--report PATH]

Exit 0 always (diagnostic); a nonzero count of T-03 banned hits is printed loudly.
"""
import argparse, json, re, math, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"
LITDIR = REPO / "literature"

STOP = set("""
a an the and or but if then else of for to in on at by with from as is are was were be been being
this that these those it its it's their there here we our us you your they them he she his her i
not no nor so such than too very can could should would may might must will shall do does did done
have has had having get got which who whom whose what when where why how all any both each few more
most other some only own same up down out over under again further once about into through during
before after above below between against because while also however thus hence therefore moreover
one two three four five first second third given let us via per i.e e.g eq fig sec table figure
section equation appendix et al ie eg cf vs versus within without upon across among along around
yet still already now then since until whether either neither toward towards onto off
""".split())

# CLAUDE.md T-03 banned vocabulary (manuscript AND conversation).
BANNED = [
    "ledger", "numerical witness", "machine-checked", "machine checked",
    "tagged", "consume", "consumes", "consuming", "consumed",
    "where it bites", "honest fence", "honest fences", "funnel", "hub",
]
BANNED_RE = [(b, re.compile(r"\b" + re.escape(b) + r"\b", re.I)) for b in BANNED]
STAGE_RE = re.compile(r"\bstage\s+\d", re.I)  # "Stage N" labels
# Same engineering-metaphor family -- NOT banned, flagged for review.
FLAG = ["pipeline", "gates", "tier", "tiers", "pinned", "scoped", "grading",
        "lineage", "harness", "sourced", "transcripts"]
FLAG_RE = [(f, re.compile(r"\b" + re.escape(f) + r"\b", re.I)) for f in FLAG]


def tok(text):
    return [w for w in re.findall(r"[a-z]{3,}", text.lower()) if w not in STOP]


def clean_manuscript(s):
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\[[^\]]*@[^\]]*\]", " ", s)
    s = re.sub(r"@[A-Za-z0-9:_\-]+", " ", s)
    s = re.sub(r"\{#[^}]*\}", " ", s)
    s = re.sub(r"\]\([^)]*\)", " ", s)
    s = re.sub(r'width="[^"]*"', " ", s)
    s = re.sub(r":::[^\n]*", " ", s)
    return s.replace("**", " ").replace("#", " ")


def clean_literature(s):
    if s.startswith("---"):
        parts = s.split("\n---", 1)
        s = parts[1] if len(parts) > 1 else s
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\\\[.*?\\\]", " ", s, flags=re.S)
    s = re.sub(r"\\\(.*?\\\)", " ", s, flags=re.S)
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)
    s = re.sub(r"https?://\S+", " ", s)
    return s


def bigrams(tokens):
    return [f"{a} {b}" for a, b in zip(tokens, tokens[1:])]


def logodds(M, L, total_M, total_L, a0=1000.0):
    N = total_M + total_L
    out = []
    for w in set(M) | set(L):
        yM, yL = M.get(w, 0), L.get(w, 0)
        aw = a0 * (yM + yL) / N
        nM, nL = yM + aw, yL + aw
        dM, dL = (total_M + a0) - nM, (total_L + a0) - nL
        delta = math.log(nM / dM) - math.log(nL / dL)
        z = delta / math.sqrt(1.0 / nM + 1.0 / nL)
        out.append((w, yM, yL, z))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--min", type=int, default=3, help="min manuscript count to report")
    ap.add_argument("--report", default=str(REPO / "verification" / "cache" / "corpus-vocab-check.md"))
    args = ap.parse_args()

    d = json.loads(L3.read_text(encoding="utf-8"))
    uM, bM = Counter(), Counter()
    para_text = {}
    for p in d["paragraphs"]:
        prose = p.get("draft_prose") or ""
        para_text[p["id"]] = prose
        t = tok(clean_manuscript(prose))
        uM.update(t); bM.update(bigrams(t))
    tot_uM, tot_bM = sum(uM.values()), sum(bM.values())

    uL, bL = Counter(), Counter()
    for fp in sorted(LITDIR.glob("*.md")):
        t = tok(clean_literature(fp.read_text(encoding="utf-8", errors="ignore")))
        uL.update(t); bL.update(bigrams(t))
    tot_uL, tot_bL = sum(uL.values()), sum(bL.values())

    uni = sorted([r for r in logodds(uM, uL, tot_uM, tot_uL) if r[1] >= args.min], key=lambda r: -r[3])
    big = sorted([r for r in logodds(bM, bL, tot_bM, tot_bL) if r[1] >= max(2, args.min - 1)], key=lambda r: -r[3])
    absent = sorted([r for r in uni if r[2] == 0], key=lambda r: -r[1])

    L = []
    L.append("# Corpus vocabulary check\n")
    L.append(f"Manuscript prose: {tot_uM:,} content tokens ({len(uM):,} types). "
             f"Indexed literature ({len(list(LITDIR.glob('*.md')))} files): {tot_uL:,} tokens "
             f"({len(uL):,} types).\n")

    L.append("\n## A. Unigrams most over-represented vs the field\n")
    L.append("| word | manuscript | /10k | literature | /10k | z |")
    L.append("|---|---|---|---|---|---|")
    for w, yM, yL, z in uni[:args.top]:
        L.append(f"| {w} | {yM} | {10000*yM/tot_uM:.1f} | {yL} | {10000*yL/tot_uL:.2f} | {z:.1f} |")

    L.append("\n## A2. Manuscript words absent from the source literature (>= "
             f"{args.min}x)\n")
    L.append(", ".join(f"{w} ({yM})" for w, yM, yL, z in absent) or "(none)")

    L.append("\n\n## B. Two-word phrases most over-represented vs the field\n")
    L.append("| phrase | manuscript | literature | z |")
    L.append("|---|---|---|---|")
    for w, yM, yL, z in big[:args.top]:
        L.append(f"| {w} | {yM} | {yL} | {z:.1f} |")

    # --- C. banned + flagged scan with locations ---
    banned_hits, flag_hits = [], Counter()
    flag_locs = {}
    for pid, prose in para_text.items():
        for term, rx in BANNED_RE:
            for m in rx.finditer(prose):
                seg = prose[max(0, m.start()-30):m.end()+30].replace("\n", " ")
                banned_hits.append((pid, term, seg))
        for m in STAGE_RE.finditer(prose):
            seg = prose[max(0, m.start()-30):m.end()+30].replace("\n", " ")
            banned_hits.append((pid, "Stage N", seg))
        for term, rx in FLAG_RE:
            n = len(rx.findall(prose))
            if n:
                flag_hits[term] += n
                flag_locs.setdefault(term, []).append(pid)

    L.append("\n\n## C. Banned-vocabulary scan (CLAUDE.md T-03)\n")
    if banned_hits:
        L.append(f"**{len(banned_hits)} BANNED hit(s):**")
        for pid, term, seg in banned_hits:
            L.append(f"- [{pid}] `{term}`: ...{seg}...")
    else:
        L.append("No banned-vocabulary hits. CLEAN.")

    L.append("\n### Flagged engineering-metaphor family (not banned -- review)\n")
    if flag_hits:
        for term, n in flag_hits.most_common():
            L.append(f"- **{term}** x{n} -- {', '.join(sorted(set(flag_locs[term])))}")
    else:
        L.append("(none)")

    report = "\n".join(L) + "\n"
    rp = Path(args.report)
    rp.parent.mkdir(parents=True, exist_ok=True)
    rp.write_text(report, encoding="utf-8")

    # console summary
    print(f"manuscript {tot_uM:,} tok / literature {tot_uL:,} tok")
    print(f"top unigrams: " + ", ".join(w for w, *_ in uni[:15]))
    print(f"top bigrams:  " + "; ".join(w for w, *_ in big[:15]))
    print(f"absent-from-lit: " + ", ".join(w for w, *_ in absent[:20]))
    print(f"T-03 banned hits: {len(banned_hits)}" + (" -- see report" if banned_hits else " (clean)"))
    print(f"flagged-family: " + ", ".join(f"{t}x{n}" for t, n in flag_hits.most_common()))
    print(f"report -> {rp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
