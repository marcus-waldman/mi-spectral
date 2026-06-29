#!/usr/bin/env python3
"""
Full-file lint for the manuscript plan system (manuscript/plan/*.json).

Authoritative enforcement point for citation and evidence discipline in the plan
JSONs. The PreToolUse hook (.claude/hooks/check_citations.py) checks fragments on
direct Edit/Write; THIS script checks whole files, and therefore also catches
changes applied by one-time update scripts, which bypass the hook entirely.
It must pass green before the commit phase of every review cycle.

Checks
------
1. Every plan JSON parses.
2. Evidence pointers (anywhere in any string value):
     lit:<citekey>     -> literature/<citekey>.md exists
     deriv:<anchor>    -> '{#<anchor>' occurs in manuscript/derivation.qmd
     verif:<relpath>   -> file exists at repo-relative path
     xmodel:<relpath>  -> file exists at repo-relative path
3. Quarto citations: every @<citekey> token in any string value has a backing
   literature/<citekey>.md (crossref prefixes and @TODO:slug exempt — same rules
   as the hook).
4. Structured citation fields: bare citekeys in 'key_citations' arrays and as keys
   of 'citations' objects (inside audit blocks) must have backing literature files.
5. Level-4 ladder: evidence_status 'cited' or 'verified' on a lit: entry requires
   the literature file to exist (earlier ladder states are allowed to dangle —
   that IS the acquisition backlog).
6. Structural gates (only when the relevant arrays are populated):
   - level2/level3: dependency graph acyclic; no dangling depends_on ids.
   - level3: every paragraph has a non-null proposition OR a goal in the
     rhetorical set; review and audit objects present.
   - level4: every entry's pointer resolves; proposition_id non-empty.
7. Prose-style gate (level3 draft_prose): the CLAUDE.md punctuation budget.
   Rhetorical colons and semicolons are flagged. Display/table/quotation/heading
   colons and math/citation-bracket semicolons are allowed. See
   prose_punctuation_hits().

Exit 0 = green; exit 1 = violations (listed on stdout).

Usage: py scripts/check_plan.py [--repo <path>]
"""

import argparse
import json
import re
import sys
from pathlib import Path

POINTER = re.compile(r"\b(lit|deriv|verif|xmodel):([A-Za-z0-9_][A-Za-z0-9_:\-./\\]*)")
CITE = re.compile(r"(?<!\w)@(?!TODO:)([A-Za-z][A-Za-z0-9_:\-]+)")
CROSSREF_PREFIX = re.compile(
    r"^(eq|fig|tbl|sec|lst|thm|lem|cor|prp|cnj|def|exm|exr|sol|rem)-"
)
# Bare citekey shape (BBT: camelCase author+title+year). Used only to sanity-check
# structured fields, not free text.
CITEKEY_SHAPE = re.compile(r"^[A-Za-z][A-Za-z0-9]+\d{4}[a-z]?$")
RHETORICAL_GOALS = {"transition", "summarize", "summarize_section", "hedge", "roadmap"}

# todo/037 accuracy invariant (CLAUDE.md): data-quantity attribution to candidate models.
# All candidates are fit to the SAME imputed data; the per-candidate driver is the model's
# own tr(RIV). Scoped to spare legitimate complete-data-vs-missingness phrasing (e.g.
# "the analyst who never lost the data") and "missing data".
DATA_QUANTITY = [
    re.compile(r"\b(model|candidate)s?\b[^.\n]{0,60}?\b(lost|lose|loses|losing|"
               r"discard\w*|drop\w*|most|more|fewer|less|least)\s+(?!missing\b)data\b", re.I),
    re.compile(r"\b(lost|lose|loses|losing)\s+the\s+(most|more|least|fewer)\s+data\b", re.I),
]

# todo/037 pattern 4 (CLAUDE.md 'No color commentary'): evaluative narration that TELLS
# the reader an object is important instead of stating the fact and its consequence.
# High-confidence subset of scripts/color_commentary_flag.py; deliberately EXCLUDES
# "central" (the motivate-by-use opener). Recurrence guard on a corpus the pass cleared.
COLOR_COMMENTARY = [
    re.compile(r"\b(gives?|lends?)\s+\w+\s+(its|their)\s+force\b", re.I),
    re.compile(r"\bdoes?\s+(the\s+)?(real|actual|hard)\s+work\b", re.I),
    re.compile(r"\bdoes?\s+(the\s+)?heavy\s+lifting\b", re.I),
    re.compile(r"\bthe\s+workhorse\b", re.I),
    re.compile(r"\bload-bearing\b", re.I),
    re.compile(r"\bcrucially\b", re.I),
    re.compile(r"\bis\s+what\s+(makes|drives|gives|powers)\b", re.I),
    re.compile(r"\b(the\s+)?(heart|crux|linchpin)\s+of\s+(the|this|its|it)\b", re.I),
    re.compile(r"\b(the\s+)?(key|crucial|essential|pivotal)\s+"
               r"(assumption|ingredient|step|fact|point|idea|insight|observation|"
               r"property|feature|move|object|quantity|term|result)\b", re.I),
]

PLAN_FILES = [
    "level1-thesis.json",
    "level2-sections.json",
    "level3-paragraphs.json",
    "level4-evidence.json",
    "status.json",
]


def iter_strings(node, path="$"):
    """Yield (json_path, string) for every string in a JSON tree."""
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from iter_strings(item, f"{path}[{i}]")
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from iter_strings(v, f"{path}.{k}")


def iter_field(node, field_name, path="$"):
    """Yield (json_path, value) for every occurrence of a named field."""
    if isinstance(node, list):
        for i, item in enumerate(node):
            yield from iter_field(item, field_name, f"{path}[{i}]")
    elif isinstance(node, dict):
        for k, v in node.items():
            if k == field_name:
                yield f"{path}.{k}", v
            yield from iter_field(v, field_name, f"{path}.{k}")


def check_pointer(kind, target, repo, deriv_anchors):
    if kind == "lit":
        if not (repo / "literature" / f"{target}.md").exists():
            return f"lit:{target} -> literature/{target}.md missing"
    elif kind == "deriv":
        if target not in deriv_anchors:
            return f"deriv:{target} -> no '{{#{target}' anchor in manuscript/derivation.qmd"
    elif kind in ("verif", "xmodel"):
        rel = target.replace("\\", "/")
        if not (repo / rel).exists():
            return f"{kind}:{target} -> file missing at {rel}"
    return None


def detect_cycles(nodes):
    """nodes: dict id -> list of dependency ids. Returns list of ids on a cycle."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {k: WHITE for k in nodes}
    on_cycle = []

    def visit(u, stack):
        color[u] = GRAY
        for v in nodes.get(u, []):
            if v not in nodes:
                continue  # dangling handled separately
            if color[v] == GRAY:
                on_cycle.extend(stack + [v])
            elif color[v] == WHITE:
                visit(v, stack + [v])
        color[u] = BLACK

    for k in nodes:
        if color[k] == WHITE:
            visit(k, [k])
    return on_cycle


def prose_punctuation_hits(prose):
    """
    Manuscript prose-style gate (CLAUDE.md 'Punctuation budget').

    Flags rhetorical colons, em-dashes, and 2+ semicolons per paragraph. A single
    semicolon between tightly-linked clauses is allowed (sparse budget v2). Allowed and
    therefore NOT flagged:
      - colons introducing a display ($$...$$), a markdown table, a heading run-in
        (a **bold:** label, or a '## ...:' subhead), or a verbatim quotation;
      - semicolons inside math ($...$) and inside citation brackets ([@a; @b]);
      - the em-dash / arithmetic uses of ':' inside math.
    Returns a list of short human-readable strings (empty when clean).
    """
    hits = []
    # Blank out the always-allowed regions so their inner punctuation is invisible.
    text = re.sub(r"\$\$.*?\$\$", " §DISPLAY ", prose, flags=re.S)  # display math
    text = re.sub(r"\$[^$]*\$", " §MATH ", text)                    # inline math
    text = re.sub(r"^\|.*$", "", text, flags=re.M)                       # table rows
    text = re.sub(r"\[[^\]]*@[^\]]*\]", " §CITE ", text)            # citation brackets
    text = re.sub(r"\{#[^}]*\}", "", text)                                # crossref anchors
    text = re.sub(r":::[^\n]*", "", text)                                # fenced-div markers

    for m in re.finditer(r"([^.\n]{0,55}):(\s|$)", text):
        frag = m.group(1).strip()
        after = text[m.end():m.end() + 16].lstrip()
        if not frag:
            continue
        if after.startswith(('"', "“", "§DISPLAY")):
            continue  # quotation- or display-introducing colon
        if frag.startswith("#") or frag.startswith("**") or frag.endswith("**"):
            continue  # subhead or bold run-in label
        if "Monte Carlo standard error" in frag:
            continue  # introduces the results table
        hits.append(f"rhetorical colon after '...{frag[-40:]}'")

    # Semicolons: allowed but SPARSE (punctuation budget v2). At most one per
    # paragraph; two or more (including semicolon-chained lists) is a violation.
    n_semi = len(re.findall(r";", text))
    if n_semi > 1:
        hits.append(f"{n_semi} semicolons in one paragraph (sparse budget allows at most one)")

    # Em-dashes stay banned (appositive / gloss chains).
    if "—" in text:
        hits.append("em-dash present (banned; use a connective or a new sentence)")

    return hits


def prose_mechanism_hits(prose):
    """
    Manuscript accuracy gate (CLAUDE.md 'Accuracy invariant - data quantity', todo/037).

    Flags data-quantity attributions to candidate models -- 'the models that lost the
    most data' and kin. Every candidate is fit to the SAME imputed data, so any such
    phrase is wrong by construction; the per-candidate driver is the model's own
    tr(RIV). Math is blanked first. The patterns are scoped to spare 'missing data' and
    analyst/data-reality phrasing that is not model-bound. Returns short strings.
    """
    text = re.sub(r"\$\$.*?\$\$", " ", prose, flags=re.S)
    text = re.sub(r"\$[^$]*\$", " ", text)
    hits = []
    for rx in DATA_QUANTITY:
        for m in rx.finditer(text):
            hits.append(
                f"data-quantity attribution '{m.group(0).strip()}' "
                f"(candidates share the imputed data; attribute to missing information / RIV)"
            )
    return hits


def prose_color_hits(prose):
    """
    Manuscript prose-style gate (CLAUDE.md 'No color commentary', todo/037 pattern 4).

    Flags evaluative narration that tells the reader an object is important instead of
    stating the fact and its consequence ("does real work", "gives X its force",
    "load-bearing", "the key/crucial <noun>", "crucially", "heart/crux of"). Math is
    blanked first. High-confidence subset; "central" is intentionally allowed (the
    motivate-by-use opener). Returns short strings.
    """
    text = re.sub(r"\$\$.*?\$\$", " ", prose, flags=re.S)
    text = re.sub(r"\$[^$]*\$", " ", text)
    hits = []
    for rx in COLOR_COMMENTARY:
        for m in rx.finditer(text):
            hits.append(
                f"color commentary '{m.group(0).strip()}' "
                f"(state the fact and its consequence; show what changes, don't assert importance)"
            )
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=None, help="repo root (default: parent of this script's dir)")
    args = ap.parse_args()

    repo = Path(args.repo) if args.repo else Path(__file__).resolve().parent.parent
    plan_dir = repo / "manuscript" / "plan"
    if not plan_dir.exists():
        print("check_plan: manuscript/plan/ not found - nothing to check.")
        return 0

    deriv = repo / "manuscript" / "derivation.qmd"
    deriv_anchors = set()
    if deriv.exists():
        deriv_anchors = set(re.findall(r"\{#([A-Za-z0-9\-]+)", deriv.read_text(encoding="utf-8")))

    problems = []
    docs = {}

    for name in PLAN_FILES:
        fp = plan_dir / name
        if not fp.exists():
            continue
        try:
            docs[name] = json.loads(fp.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            problems.append(f"{name}: JSON parse error: {e}")

    # --- pointer + @citekey checks over every string in every doc ---
    for name, doc in docs.items():
        seen = set()
        for jpath, s in iter_strings(doc):
            for m in POINTER.finditer(s):
                kind, target = m.group(1), m.group(2).rstrip(".,;)")
                key = (kind, target)
                if key in seen:
                    continue
                seen.add(key)
                err = check_pointer(kind, target, repo, deriv_anchors)
                if err:
                    problems.append(f"{name} {jpath}: {err}")
            for m in CITE.finditer(s):
                citekey = m.group(1)
                if CROSSREF_PREFIX.match(citekey):
                    continue
                key = ("cite", citekey)
                if key in seen:
                    continue
                seen.add(key)
                if not (repo / "literature" / f"{citekey}.md").exists():
                    problems.append(
                        f"{name} {jpath}: @{citekey} has no literature/{citekey}.md"
                    )

    # --- structured citation fields ---
    for name, doc in docs.items():
        for jpath, val in iter_field(doc, "key_citations"):
            if isinstance(val, list):
                for v in val:
                    if isinstance(v, str) and CITEKEY_SHAPE.match(v):
                        if not (repo / "literature" / f"{v}.md").exists():
                            problems.append(
                                f"{name} {jpath}: key_citations citekey '{v}' has no literature file"
                            )
        for jpath, val in iter_field(doc, "citations"):
            if isinstance(val, dict):
                for k in val:
                    if CITEKEY_SHAPE.match(k):
                        if not (repo / "literature" / f"{k}.md").exists():
                            problems.append(
                                f"{name} {jpath}: audit citation key '{k}' has no literature file"
                            )

    # --- level 4 ladder ---
    l4 = docs.get("level4-evidence.json")
    if l4:
        for i, entry in enumerate(l4.get("evidence_map") or []):
            ptr = entry.get("pointer") or ""
            status = entry.get("evidence_status") or ""
            pid = entry.get("proposition_id") or ""
            if not pid:
                problems.append(f"level4-evidence.json evidence_map[{i}]: empty proposition_id")
            m = POINTER.match(ptr)
            if not m:
                problems.append(
                    f"level4-evidence.json evidence_map[{i}]: pointer '{ptr}' does not match the pointer grammar"
                )
                continue
            if m.group(1) == "lit" and status in ("verified", "cited"):
                if not (repo / "literature" / f"{m.group(2)}.md").exists():
                    problems.append(
                        f"level4-evidence.json evidence_map[{i}]: status '{status}' but literature/{m.group(2)}.md missing"
                    )

    # --- structural gates (only when populated) ---
    l2 = docs.get("level2-sections.json")
    if l2 and (l2.get("sections") or []):
        deps = {}
        for s in l2["sections"]:
            deps[s.get("id")] = list(s.get("depends_on") or [])
        for sid, dlist in deps.items():
            for d in dlist:
                if d not in deps:
                    problems.append(f"level2-sections.json: section {sid} depends_on dangling id '{d}'")
        cyc = detect_cycles(deps)
        if cyc:
            problems.append(f"level2-sections.json: dependency cycle involving {sorted(set(cyc))}")
        for s in l2["sections"]:
            for j, sp in enumerate(s.get("super_propositions") or []):
                ev = sp.get("evidence") or []
                if not ev and sp.get("evidence_status") != "needs_grounding":
                    problems.append(
                        f"level2-sections.json: {s.get('id')} SP[{j}] has no evidence pointers and is not flagged needs_grounding"
                    )

    l3 = docs.get("level3-paragraphs.json")
    if l3 and (l3.get("paragraphs") or []):
        deps = {}
        for p in l3["paragraphs"]:
            pid = p.get("id")
            deps[pid] = list(p.get("depends_on") or [])
            goal = p.get("goal") or ""
            if p.get("proposition") is None and goal not in RHETORICAL_GOALS:
                problems.append(
                    f"level3-paragraphs.json: {pid} has null proposition and non-rhetorical goal '{goal}'"
                )
            if not isinstance(p.get("review"), dict):
                problems.append(f"level3-paragraphs.json: {pid} missing review object")
            if not isinstance(p.get("audit"), dict):
                problems.append(f"level3-paragraphs.json: {pid} missing audit object")
            for hit in prose_punctuation_hits(p.get("draft_prose") or ""):
                problems.append(f"level3-paragraphs.json: {pid} prose-style: {hit}")
            for hit in prose_mechanism_hits(p.get("draft_prose") or ""):
                problems.append(f"level3-paragraphs.json: {pid} prose-accuracy: {hit}")
            for hit in prose_color_hits(p.get("draft_prose") or ""):
                problems.append(f"level3-paragraphs.json: {pid} prose-style: {hit}")
        for pid, dlist in deps.items():
            for d in dlist:
                if d not in deps:
                    problems.append(f"level3-paragraphs.json: {pid} depends_on dangling id '{d}'")
        cyc = detect_cycles(deps)
        if cyc:
            problems.append(f"level3-paragraphs.json: dependency cycle involving {sorted(set(cyc))}")

    if problems:
        print(f"check_plan: {len(problems)} violation(s)\n")
        for p in problems:
            print(f"  - {p}")
        return 1

    n = len(docs)
    print(f"check_plan: green ({n} plan file(s) checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
