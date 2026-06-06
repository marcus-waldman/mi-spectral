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
