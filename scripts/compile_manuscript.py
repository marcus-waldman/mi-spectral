#!/usr/bin/env python3
"""
Compile manuscript/mi-spectral.qmd from manuscript/plan/level3-paragraphs.json.

The plan JSON is the source of truth for prose (see manuscript/plan/README.md);
this script is the only writer of the compiled qmd once level3 metadata has
compile_enabled = true. Until then it refuses to run, so the pre-system draft
cannot be clobbered by accident.

Document assembly:
  1. metadata.qmd_header  - emitted verbatim (YAML front matter + any preamble,
     e.g. the draft-status callout). Set during the level3 decomposition.
  2. For each section in metadata.sections_order (array order):
       '# <title> {#<anchor>}'   - or the section's optional 'heading' override
       then its paragraphs in array order; each paragraph may carry an optional
       'pre_markdown' (subsection heading, table, figure include) emitted
       verbatim before its 'draft_prose'.
  3. metadata.qmd_footer  - emitted verbatim (e.g. the references div).

Paragraph entries with draft_prose == null are skipped with a warning (they are
planned but unwritten).

Usage: py scripts/compile_manuscript.py [--out <path>] [--check]
  --check : compile to memory and report what WOULD change (no write).
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEVEL3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"
DEFAULT_OUT = REPO / "manuscript" / "mi-spectral.qmd"


def compile_doc(doc):
    meta = doc.get("metadata") or {}
    out = []
    warnings = []

    header = meta.get("qmd_header")
    if not header:
        warnings.append("metadata.qmd_header missing - compiled file will have no YAML front matter")
    else:
        out.append(header.rstrip("\n"))

    sections = doc.get("sections_order") or meta.get("sections_order") or []
    paragraphs = doc.get("paragraphs") or []
    by_section = {}
    for p in paragraphs:
        by_section.setdefault(p.get("section"), []).append(p)

    for s in sections:
        sid = s.get("id")
        heading = s.get("heading")
        if heading is None:
            heading = f"# {s.get('title')} {{#{s.get('anchor')}}}"
        out.append("")
        out.append(heading)
        for p in by_section.get(sid, []):
            pre = p.get("pre_markdown")
            if pre:
                out.append("")
                out.append(pre.rstrip("\n"))
            prose = p.get("draft_prose")
            if prose is None:
                warnings.append(f"{p.get('id')}: draft_prose is null - skipped")
                continue
            out.append("")
            out.append(prose.rstrip("\n"))
        orphan_check = [p.get("id") for p in by_section.get(sid, []) if not p.get("id")]
        if orphan_check:
            warnings.append(f"section {sid}: paragraphs without ids")

    known = {s.get("id") for s in sections}
    for sid in by_section:
        if sid not in known:
            warnings.append(f"paragraphs reference unknown section '{sid}' - NOT emitted")

    footer = meta.get("qmd_footer")
    if footer:
        out.append("")
        out.append(footer.rstrip("\n"))

    return "\n".join(out) + "\n", warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    if not LEVEL3.exists():
        print("compile_manuscript: level3-paragraphs.json not found.")
        return 1
    doc = json.loads(LEVEL3.read_text(encoding="utf-8"))
    meta = doc.get("metadata") or {}

    if not meta.get("compile_enabled"):
        print(
            "compile_manuscript: refusing to run - metadata.compile_enabled is not true.\n"
            "The level3 decomposition is not complete; manuscript/mi-spectral.qmd is still\n"
            "the working draft and must not be overwritten. See manuscript/plan/README.md."
        )
        return 1

    if not (doc.get("paragraphs") or []):
        print("compile_manuscript: refusing to run - paragraphs array is empty.")
        return 1

    text, warnings = compile_doc(doc)
    for w in warnings:
        print(f"  warning: {w}")

    out_path = Path(args.out)
    if args.check:
        if out_path.exists() and out_path.read_text(encoding="utf-8") == text:
            print("compile_manuscript --check: compiled output matches the existing file.")
        else:
            print("compile_manuscript --check: compiled output DIFFERS from the existing file.")
        return 0

    out_path.write_text(text, encoding="utf-8")
    n = len(doc.get("paragraphs") or [])
    print(f"compile_manuscript: wrote {out_path} ({n} paragraphs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
