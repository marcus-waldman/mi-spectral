#!/usr/bin/env python3
"""D-20: 'AI-assisted derivation' -> 'human-prompted AI derivation' across binding
manuscript surfaces + internal guidance docs. Byte-level replace (line endings
preserved). Validate every old-string count, then write. Frozen tkal-reviews/,
historical update scripts, and todo/035 handoffs intentionally NOT touched.
"""
import sys
from pathlib import Path

REPO = Path(r"C:/Users/marcu/git-repositories/mi-spectral")

# rel -> list of (old, new, expected_count)
REPL = {
 "manuscript/plan/level3-paragraphs.json": [
   ("AI-assisted, with an ORCID-verified human prompter of record", "human-prompted AI derivations, with an ORCID-verified prompter of record", 2),
   ("failures of AI-assisted scholarship", "failures of human-prompted AI scholarship", 1),
   ("rely on an AI-assisted derivation", "rely on a human-prompted AI derivation", 1),
   ("require of an AI-assisted derivation before relying", "require of a human-prompted AI derivation before relying", 1),
   ("The derivation is AI-assisted under a stated, auditable verification protocol", "The derivation is human-prompted AI work under a stated, auditable verification protocol", 1),
 ],
 "manuscript/plan/level2-sections.json": [
   ("the derivation is AI-assisted under a verification protocol stated as Methods", "the derivation is human-prompted AI work under a verification protocol stated as Methods", 1),
   ("The derivation is AI-assisted under a stated verification protocol reported in full", "The derivation is human-prompted AI work under a stated verification protocol reported in full", 1),
 ],
 "manuscript/plan/level1-thesis.json": [
   ("workflow yields AI-assisted mathematical results", "workflow yields human-prompted AI mathematical results", 1),
   ("an AI-assisted derivation with an ORCID-verified human prompter", "a human-prompted AI derivation with an ORCID-verified prompter", 1),
   ("The derivation is AI-assisted; the collaboration is foregrounded", "The derivation is human-prompted AI work; the collaboration is foregrounded", 1),
 ],
 "manuscript/mi-spectral.qmd": [
   ("human prompter of an AI-assisted derivation", "human prompter of an AI derivation", 1),
   ("an AI-assisted derivation with a human prompter of record", "a human-prompted AI derivation with a prompter of record", 1),
 ],
 "manuscript/derivation.qmd": [
   ("Because this is an AI-assisted derivation, every external claim", "Because this is a human-prompted AI derivation, every external claim", 1),
 ],
 "CLAUDE.md": [
   ("AI-assisted derivation, target venue JAIGP", "Human-prompted AI derivation, target venue JAIGP", 1),
   ("Rationale: AI-assisted derivations fail in review", "Rationale: human-prompted AI derivations fail in review", 1),
 ],
 ".prometheus/charter.md": [
   ("It is an AI-assisted derivation with transparent, ORCID-verified human prompting", "It is a human-prompted AI derivation with transparent, ORCID-verified provenance", 1),
   ("AI-assisted derivation with ORCID-verified provenance per JAIGP", "Human-prompted AI derivation with ORCID-verified provenance per JAIGP", 1),
 ],
 "IDEAS.md": [
   ("Because the derivation is AI-assisted, the reader is afforded", "Because this is a human-prompted AI derivation, the reader is afforded", 1),
 ],
 ".claude/skills/derivation-audit/SKILL.md": [
   ("citation-disciplined, AI-assisted theory paper", "citation-disciplined, human-prompted AI theory paper", 1),
   ("the way AI-assisted derivations fail in review", "the way human-prompted AI derivations fail in review", 1),
 ],
}

results, errors = {}, []
for rel, edits in REPL.items():
    p = REPO / rel
    data = p.read_bytes()
    for old, new, cnt in edits:
        ob = old.encode("utf-8")
        n = data.count(ob)
        if n != cnt:
            errors.append(f"  {rel}: '{old[:55]}...' found {n}x (expected {cnt})")
        else:
            data = data.replace(ob, new.encode("utf-8"))
    results[p] = data

if errors:
    print("ABORT -- validation failed; NOTHING written:")
    print("\n".join(errors)); sys.exit(1)

for p, data in results.items():
    p.write_bytes(data)
    print("updated", p.relative_to(REPO))

# Append D-20 to decisions.md (preserve the file's newline style)
dec = REPO / "manuscript/plan/decisions.md"
ddata = dec.read_bytes()
nl = "\r\n" if b"\r\n" in ddata else "\n"
para = ('Replace "AI-assisted derivation" with "human-prompted AI derivation" across the '
 'binding manuscript surfaces (level3 prose + abstract, level1/level2 plan claims, the '
 'mi-spectral.qmd author note + provenance statement, the derivation.qmd provenance note) '
 'and the internal guidance docs (CLAUDE.md, .prometheus/charter.md, IDEAS.md, the '
 'derivation-audit SKILL.md). Rationale: under D-18 the AI are the authors and the human is '
 'the prompter, so "assisted" inverts the roles -- it frames a human author with AI help. '
 '"Human-prompted AI derivation" states the direction the right way round: the AI derived, '
 'the human prompted. Chosen by Marcus via AskUserQuestion over "AI-prompted derivation" '
 '(ambiguous -- parses as prompted *by* an AI) and "AI-generated derivation" (drops the '
 'prompting emphasis). Where "human prompter" already sits adjacent the redundant "human" is '
 'dropped (e.g., "a human-prompted AI derivation with a prompter of record"); predicate uses '
 'read "is human-prompted AI work". Frozen tkal-reviews/ records, the historical update '
 'scripts, and the todo/035 handoffs deliberately retain the old phrasing so the '
 'point-in-time record is not falsified. Applied via '
 'manuscript/plan/updates/update-d20-attribution-terminology-20260628.py.')
block = nl + nl + '## Attribution terminology: "human-prompted AI derivation" (2026-06-28, Marcus, AskUserQuestion, D-20)' + nl + nl + para + nl
dec.write_bytes(ddata + block.encode("utf-8"))
print("appended D-20 to decisions.md")

# Verify no stray 'AI-assisted' remains in the touched files
print("\n=== residual 'AI-assisted' in touched files (expect none) ===")
stray = 0
for rel in list(REPL.keys()) + ["manuscript/plan/decisions.md"]:
    c = (REPO / rel).read_bytes().count(b"AI-assisted")
    if c:
        print(f"  {rel}: {c}"); stray += c
print("none" if stray == 0 else f"TOTAL STRAY: {stray}")
