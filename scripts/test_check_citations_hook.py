#!/usr/bin/env python3
"""Smoke tests for .claude/hooks/check_citations.py (run: py scripts/test_check_citations_hook.py)."""

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HOOK = REPO / ".claude" / "hooks" / "check_citations.py"
PLAN = str(REPO / "manuscript" / "plan" / "level4-evidence.json")
QMD = str(REPO / "manuscript" / "mi-spectral-apa.qmd")
OUTSIDE = str(REPO / "todo" / "scratch.md")


def run(tool_name, file_path, content):
    payload = {"tool_name": tool_name, "tool_input": {"file_path": file_path}}
    if tool_name == "Write":
        payload["tool_input"]["content"] = content
    else:
        payload["tool_input"]["new_string"] = content
        payload["tool_input"]["old_string"] = "x"
    p = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload).encode("utf-8"),
        capture_output=True,
    )
    return p.returncode


CASES = [
    # (name, tool, path, content, expected_exit)
    ("good @cite in qmd", "Edit", QMD, "as shown by @rubinMultipleImputationNonresponse1987.", 0),
    ("bad @cite in qmd", "Edit", QMD, "as shown by @fakeAuthorBogusPaper2099.", 2),
    ("TODO bypass", "Edit", QMD, "placeholder @TODO:bogus-paper here.", 0),
    ("crossref exempt", "Edit", QMD, "see @sec-lrt and @eq-thm and @thm-bias.", 0),
    ("good lit: pointer in plan json", "Edit", PLAN, '"pointer": "lit:chanGeneralFeasibleTests2022"', 0),
    ("bad lit: pointer in plan json", "Edit", PLAN, '"pointer": "lit:fakeAuthorBogusPaper2099"', 2),
    ("bad key_citations entry", "Edit", PLAN, '"key_citations": ["fakeAuthorBogusPaper2099"]', 2),
    ("good key_citations entry", "Edit", PLAN, '"key_citations": ["mengPerformingLikelihoodRatio1992b"]', 0),
    ("bad citations object key", "Edit", PLAN, '"citations": {"fakeAuthorBogusPaper2099": "verified"}', 2),
    ("good citations object key", "Edit", PLAN, '"citations": {"kenwardLikelihoodBasedFrequentist1998": "verified"}', 0),
    ("non-citekey-shaped strings ignored", "Edit", PLAN, '"key_citations": ["Nebraska data (Script 03)"]', 0),
    ("outside manuscript/ not enforced", "Edit", OUTSIDE, "mentions @fakeAuthorBogusPaper2099 freely.", 0),
    ("Write full content checked", "Write", PLAN, '{"evidence_map": [{"pointer": "lit:fakeAuthorBogusPaper2099"}]}', 2),
]


def main():
    failures = 0
    for name, tool, path, content, expected in CASES:
        rc = run(tool, path, content)
        ok = rc == expected
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} (exit {rc}, expected {expected})")
        if not ok:
            failures += 1
    print(f"\n{len(CASES) - failures}/{len(CASES)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
