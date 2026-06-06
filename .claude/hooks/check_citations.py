#!/usr/bin/env python3
"""
PreToolUse hook: enforce citation discipline for mi-spectral.

Triggers on Edit / Write / MultiEdit to any file under manuscript/.
Extracts @<citekey> tokens from the content being written, and blocks the tool
call if any citekey lacks a backing literature/<citekey>.md.

Also enforces the manuscript-plan pointer grammar (manuscript/plan/*.json and
any other manuscript/ file): 'lit:<citekey>' pointers, citekeys in
'key_citations' arrays, and citekey-shaped keys of 'citations' audit objects
must all have backing literature files. This is the fragment-level first line
of defense; the authoritative whole-file check is scripts/check_plan.py, which
also catches scripted JSON mutations that never pass through this hook.

Bypass: use @TODO:slug for legitimate drafting placeholders.

Exit codes (Claude Code hook convention):
  0 = allow
  2 = block; stderr message is shown back to Claude

Wired via .claude/settings.json under hooks.PreToolUse.
"""

import json
import re
import sys
from pathlib import Path

PATTERN = re.compile(r"(?<!\w)@(?!TODO:)([A-Za-z][A-Za-z0-9_:\-]+)")
LIT_POINTER = re.compile(r"\blit:([A-Za-z][A-Za-z0-9_\-]+)")
KEY_CITATIONS_BLOCK = re.compile(r"\"key_citations\"\s*:\s*\[([^\]]*)\]")
QUOTED_STRING = re.compile(r"\"([^\"]+)\"")
CITATIONS_OBJECT = re.compile(r"\"citations\"\s*:\s*\{([^{}]*)\}")
OBJECT_KEY = re.compile(r"\"([^\"]+)\"\s*:")
# Bare-citekey shape (BBT: letters then a 4-digit year, optional suffix).
CITEKEY_SHAPE = re.compile(r"^[A-Za-z][A-Za-z0-9]+\d{4}[a-z]?$")

# Quarto cross-reference prefixes (@eq-foo, @fig-bar, @sec-baz, ...) are not
# bibliographic citekeys — they reference equations/figures/tables/sections/
# theorem-environments within the document. Skip them so crossrefs don't trip
# the citation check. (BBT citekeys here are camelCase with no early hyphen,
# so matching "<prefix>-" is unambiguous.)
CROSSREF_PREFIX = re.compile(
    r"^(eq|fig|tbl|sec|lst|thm|lem|cor|prp|cnj|def|exm|exr|sol|rem)-"
)


def main() -> int:
    raw = sys.stdin.read()
    if not raw:
        return 0
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        # Fail open on malformed input rather than block.
        return 0

    tool_name = payload.get("tool_name")
    if tool_name not in ("Edit", "Write", "MultiEdit"):
        return 0

    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path") or ""
    if not file_path:
        return 0

    # Only enforce inside manuscript/. Match either slash direction.
    if not re.search(r"[/\\]manuscript[/\\]", file_path):
        return 0

    # Pull the new content depending on tool type.
    new_content = ""
    if tool_name == "Edit":
        new_content = tool_input.get("new_string") or ""
    elif tool_name == "Write":
        new_content = tool_input.get("content") or ""
    elif tool_name == "MultiEdit":
        edits = tool_input.get("edits") or []
        new_content = "\n".join((e.get("new_string") or "") for e in edits)

    if not new_content:
        return 0

    # Find the sibling literature/ directory.
    repo_root = Path(re.sub(r"[/\\]manuscript[/\\].*$", "", file_path))
    lit_dir = repo_root / "literature"

    # Extract citekeys.
    missing = []
    seen = set()

    def require(citekey):
        if citekey in seen:
            return
        seen.add(citekey)
        if not (lit_dir / f"{citekey}.md").exists():
            missing.append(citekey)

    for m in PATTERN.finditer(new_content):
        citekey = m.group(1)
        if CROSSREF_PREFIX.match(citekey):
            continue  # Quarto crossref, not a citation
        require(citekey)

    # Plan pointer grammar: lit:<citekey> anywhere in the fragment.
    for m in LIT_POINTER.finditer(new_content):
        require(m.group(1))

    # Structured fields: "key_citations": ["citekey", ...]
    for block in KEY_CITATIONS_BLOCK.finditer(new_content):
        for q in QUOTED_STRING.finditer(block.group(1)):
            if CITEKEY_SHAPE.match(q.group(1)):
                require(q.group(1))

    # Structured fields: "citations": { "citekey": "verdict", ... }
    for block in CITATIONS_OBJECT.finditer(new_content):
        for q in OBJECT_KEY.finditer(block.group(1)):
            if CITEKEY_SHAPE.match(q.group(1)):
                require(q.group(1))

    if not missing:
        return 0

    lines = [
        "Citation discipline check failed.",
        "",
        "The following @citekey tokens have no backing literature/<citekey>.md:",
        "",
    ]
    for k in sorted(missing):
        lines.append(f"  @{k}  (expected at {lit_dir}\\{k}.md)")
    lines += [
        "",
        "Resolutions:",
        "  - Add the reference to the Zotero mi-spectral collection, re-export BBT, run /lit-sync, then retry.",
        "  - Or use @TODO:slug as a deliberate placeholder (bypasses this check).",
        "",
        "See: todo/001-literature-and-hooks.md and .claude/skills/lit-sync/SKILL.md",
    ]
    sys.stderr.write("\n".join(lines) + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
