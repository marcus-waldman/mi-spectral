#!/usr/bin/env python3
"""
Cadence flagger (READ-ONLY scout for the style / de-machining pass).

Scores each manuscript paragraph (level3 draft_prose) on the signals that make
prose read as machine-written: uniform sentence length, repeated sentence
openers, a low connective rate (the punctuation-budget-v1 side effect), and
sentence-initial "it/this/that" pronouns whose antecedent the reader must recall.
Ranks worst-first so the style pass hits the most metronomic paragraphs first.
Diagnostic only; the actual rewrites are proposed and adversarially checked
downstream.

  py scripts/cadence_flag.py [--out PATH]
"""
import argparse, json, re, statistics, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

CONNECTIVES = ["because", "since", "while", "although", "whereas", "but", "yet",
               "so", "however", "therefore", "thus", "hence", "though",
               "nonetheless", "nevertheless", "as a result", "by contrast"]
CONN_RE = re.compile(r"\b(" + "|".join(CONNECTIVES) + r")\b", re.I)
PRONOUN_OPENERS = {"it", "this", "that", "they", "these", "those"}

# todo/037 pattern 2: back-referencing pronouns whose antecedent the reader must recall.
# An orphaned one signals two clauses that want to be JOINED (and / which / so / then).
BACKREF = {"it", "its", "itself", "this", "that", "these", "those", "them", "they"}
BACKREF_RE = re.compile(r"\b(" + "|".join(sorted(BACKREF)) + r")\b", re.I)
# "this/that <noun>" is anchored (demonstrative + noun), so it is NOT orphaned.
DEMONSTRATIVE_NOUN = re.compile(r"\b(this|that|these|those)\s+[a-z]", re.I)
# A pronoun right after a clause boundary (comma/semicolon) reaches back across a clause.
CLAUSE_PRONOUN_RE = re.compile(r"[,;]\s+(it|this|that|they|these|those)\b", re.I)
BOLD_LABEL_RE = re.compile(r"\*\*(.+?)\*\*", re.S)
HEADING_RE = re.compile(r"^#+\s+(.*)$", re.M)


def clean(s):
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " M ", s)                     # math -> token (no decimals leak)
    s = re.sub(r"\[[^\]]*@[^\]]*\]", " ", s)
    s = re.sub(r"@[A-Za-z0-9:_\-]+", " ", s)
    s = re.sub(r"\{#[^}]*\}", " ", s)
    s = re.sub(r"!\[.*?\]\([^)]*\)", " ", s, flags=re.S)
    s = re.sub(r":::[^\n]*", " ", s)
    s = re.sub(r"^\d+\.\s+", " ", s, flags=re.M)           # numbered-list markers
    s = s.replace("**", " ").replace("#", " ")
    return s


def sentences(text):
    text = re.sub(r"\s+", " ", text).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def first_word(sent):
    m = re.search(r"[A-Za-z]+", sent)
    return m.group(0) if m else ""


def label_orphans(label):
    """Back-referencing pronouns in a header / bold run-in label (zero tolerance at
    entry points). Personal it/its/itself/them/they always orphan; a demonstrative is
    orphan only when BARE (not 'this correction' etc.)."""
    out = []
    for m in re.finditer(r"\b[A-Za-z]+\b", label):
        w = m.group(0).lower()
        if w in {"it", "its", "itself", "them", "they"}:
            out.append(w)
        elif w in {"this", "that", "these", "those"}:
            rest = label[m.end():].lstrip()
            if not re.match(r"[A-Za-z]", rest):       # bare: ends the label / hits punctuation
                out.append(w)
    return out


def pronoun_audit(prose):
    """todo/037 pattern 2. Returns orphaned-pronoun signals (a lexical ASSIST, not a
    verdict) plus zero-tolerance entry-point hits (headers / bold run-in labels / a
    topic sentence that opens with a back-referencing pronoun)."""
    entry = []
    for m in BOLD_LABEL_RE.finditer(prose):
        lbl = m.group(1).strip()
        # only treat short run-in labels (not whole bold sentences) as entry points
        if len(lbl.split()) <= 9:
            for w in label_orphans(lbl):
                entry.append(f"label '{lbl[:48]}' -> '{w}'")
    for m in HEADING_RE.finditer(prose):
        for w in label_orphans(m.group(1).strip()):
            entry.append(f"heading '{m.group(1).strip()[:48]}' -> '{w}'")

    sents = sentences(clean(prose))
    real = [s for s in sents if len(s.split()) >= 4]
    openers = [first_word(s).lower() for s in real]
    pron_open = sum(1 for o in openers if o in PRONOUN_OPENERS)
    orphan_open = sum(1 for o in openers if o in {"it", "they"})
    # topic sentence (first real sentence) opening with a back-referencing pronoun
    if openers and openers[0] in PRONOUN_OPENERS:
        ts = real[0]
        if not DEMONSTRATIVE_NOUN.match(ts):          # 'This correction...' is anchored
            entry.append(f"topic sentence opens '{ts[:48]}...'")
    clause_pron = len(CLAUSE_PRONOUN_RE.findall(clean(prose)))
    return {
        "pron_open": pron_open, "orphan_open": orphan_open,
        "clause_pron": clause_pron, "entrypoint": entry,
        "load": len(entry) * 2 + orphan_open + 0.5 * clause_pron,
    }


def analyze(prose):
    sents = sentences(clean(prose))
    real = [s for s in sents if len(s.split()) >= 4]       # drop labels/fragments
    if len(real) < 2:
        return None
    lens = [len(s.split()) for s in real]
    mean_len = statistics.mean(lens)
    cv = (statistics.pstdev(lens) / mean_len) if mean_len else 0.0
    openers = [first_word(s).lower() for s in real]
    the_share = sum(1 for o in openers if o == "the") / len(real)
    pron_open = sum(1 for o in openers if o in PRONOUN_OPENERS)
    # longest run of consecutive identical openers
    run = best = 1
    for a, b in zip(openers, openers[1:]):
        run = run + 1 if a == b else 1
        best = max(best, run)
    conn = len(CONN_RE.findall(clean(prose)))
    conn_rate = conn / len(real)
    # monotony score (higher = worse): uniform length + The-openers + pronoun
    # openers + same-opener runs, minus connective rate.
    score = (1.0 - min(cv, 1.0)) + the_share + 0.6 * (pron_open / len(real)) \
        + 0.4 * (best / len(real)) - 0.8 * min(conn_rate, 1.0)
    return {
        "n_sent": len(real), "mean_len": round(mean_len, 1), "cv_len": round(cv, 2),
        "the_share": round(the_share, 2), "pronoun_openers": pron_open,
        "max_same_opener_run": best, "connectives": conn,
        "conn_rate": round(conn_rate, 2), "score": round(score, 3),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(REPO / "verification" / "cache" / "cadence-scores.json"))
    args = ap.parse_args()
    d = json.loads(L3.read_text(encoding="utf-8"))
    rows = []
    pron_rows = []
    for p in d["paragraphs"]:
        prose = p.get("draft_prose") or ""
        m = analyze(prose)
        if m:
            rows.append({"id": p["id"], "section": p["section"], **m})
        pa = pronoun_audit(prose)
        if pa["load"] > 0:
            pron_rows.append({"id": p["id"], "section": p["section"], **pa})
    rows.sort(key=lambda r: -r["score"])
    pron_rows.sort(key=lambda r: (-len(r["entrypoint"]), -r["load"]))
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(
        json.dumps({"paragraphs": rows, "pronoun_audit": pron_rows}, indent=2),
        encoding="utf-8")

    print(f"{len(rows)} paragraphs scored. Worst-first (most metronomic):\n")
    print(f"{'id':8} {'sec':4} {'n':>3} {'mlen':>5} {'cv':>4} {'The%':>5} {'pron':>4} {'run':>3} {'conn':>4} {'score':>6}")
    for r in rows[:25]:
        print(f"{r['id']:8} {r['section']:4} {r['n_sent']:>3} {r['mean_len']:>5} "
              f"{r['cv_len']:>4} {r['the_share']:>5} {r['pronoun_openers']:>4} "
              f"{r['max_same_opener_run']:>3} {r['connectives']:>4} {r['score']:>6}")
    corpus_conn = sum(r["connectives"] for r in rows)
    corpus_sent = sum(r["n_sent"] for r in rows)
    print(f"\ncorpus: {corpus_sent} sentences, {corpus_conn} connectives "
          f"({corpus_conn/corpus_sent:.2f}/sentence), "
          f"mean cv_len {statistics.mean(r['cv_len'] for r in rows):.2f}")

    # --- todo/037 pattern 2: orphaned pronouns + entry-point self-containment ---
    print(f"\n{'='*72}\npattern-2 (orphaned pronouns / entry points), worst-first "
          f"-- {len(pron_rows)} paragraph(s):\n")
    print(f"{'id':8} {'sec':4} {'open':>4} {'orph':>4} {'claus':>5}  entry-point hits (zero tolerance)")
    for r in pron_rows:
        ep = " | ".join(r["entrypoint"][:3]) if r["entrypoint"] else ""
        print(f"{r['id']:8} {r['section']:4} {r['pron_open']:>4} {r['orphan_open']:>4} "
              f"{r['clause_pron']:>5}  {ep}")
    ep_total = sum(len(r["entrypoint"]) for r in pron_rows)
    print(f"\nentry-point violations (headers/labels/topic openers): {ep_total}")
    print(f"scores -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
