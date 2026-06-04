#!/usr/bin/env python3
"""
Mechanical audit engine for the mi-spectral sourced derivation.

READ-ONLY. Diagnoses and flags; never edits the manuscript or literature.

Runs the deterministic half of the derivation audit and emits a structured
report (markdown to stdout, JSON via --json). The semantic half — does the
cited source's text actually support the claim, and does any prose over-claim
beyond its stated verification — is left to the model invoking the skill
(SKILL.md), which reads literature/<citekey>.md and grades each attribution.

Dimensions covered here:
  A. Citation integrity     - @citekey -> literature/<key>.md + .bib entry;
                              @TODO:<slug> placeholders; crossref exclusion.
  B. (mechanical only)      - Source-note :lineref anchors resolve to a real
                              line in literature/<key>.md; Appendix-A verbatim
                              snippets are substring-present in the source.
  C. Reproducibility        - every verification/* path, run_all phase, and
                              todo/* pointer the doc names actually exists.
  C. [mc] <-> assert         - each [mc] tag's @lst-mc-* listing has an assert;
                              flag lst-mc blocks with no assert.
  D. Internal consistency   - every @eq-/@sec-/@lst-/@fig-/@tbl-/@thm- crossref
                              resolves to a defined {#label} (or #| label:).
  F. Reference lifecycle     - cited citekeys are marked verified/cited in
                              todo/003-references-to-acquire.md.

Usage:
  python audit_derivation.py <path-to.qmd> [--repo <root>] [--json <out.json>]

If --repo is omitted the repo root is inferred as the parent of the directory
holding the target file (i.e. the parent of manuscript/).
"""

import argparse
import json
import os
import re
import sys


# ----------------------------------------------------------------------------
# Token patterns
# ----------------------------------------------------------------------------

# Mirror the hook's citekey pattern exactly (.claude/hooks/check_citations.py):
# an @ not preceded by a word char, not the TODO sentinel, then a citekey.
CITE_RE = re.compile(r"(?<!\w)@(?!TODO:)([A-Za-z][A-Za-z0-9_:\-]+)")
TODO_RE = re.compile(r"(?<!\w)@TODO:([A-Za-z0-9_\-]+)")

# Quarto crossref prefixes (same list the hook uses). An @<prefix>-... is an
# internal cross-reference, never a bibliographic citekey.
CROSSREF_PREFIX = re.compile(
    r"^(eq|fig|tbl|sec|lst|thm|lem|cor|prp|cnj|def|exm|exr|sol|rem)-"
)

# A {#label} definition anywhere (headers, after $$ displays, on divs).
LABEL_DEF_RE = re.compile(r"\{#([A-Za-z]+-[A-Za-z0-9_:\-]+)\}")
# A code-cell label: `#| label: lst-mc-foo`
CELL_LABEL_RE = re.compile(r"^\s*#\|\s*label:\s*([A-Za-z][A-Za-z0-9_:\-]+)\s*$")

# Source-note line anchors: <a href="#sec-src-<alias>"><code>:1477</code></a>
LINEREF_RE = re.compile(
    r'href="#sec-src-([A-Za-z0-9]+)"\s*>\s*<code>:(\d+)</code>'
)

# Appendix-A source-section header: ### Title {#sec-src-<alias>}
SRC_SECTION_RE = re.compile(r"^#{2,4}\s+.*\{#(sec-src-[A-Za-z0-9]+)\}\s*$")
# The [@citekey] that names the reference inside a source section.
INLINE_CITE_RE = re.compile(r"\[@([A-Za-z][A-Za-z0-9_:\-]+)")


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()


def strip_code_fences(lines):
    """Return a parallel list marking which lines are inside ``` fenced code.

    Citations/crossrefs inside python code blocks (e.g. variable names) should
    not be treated as bibliographic tokens; but #| label: lines and lst-mc
    blocks ARE meaningful. We return the in_code flag per line so callers can
    decide. Margin notes and prose live outside fences.
    """
    in_code = []
    fence = False
    for ln in lines:
        if re.match(r"^\s*```", ln):
            # the fence line itself is a boundary (treat as code)
            in_code.append(True)
            fence = not fence
            continue
        in_code.append(fence)
    return in_code


# ----------------------------------------------------------------------------
# A. Citations + D. crossrefs
# ----------------------------------------------------------------------------

def collect_labels(lines):
    labels = set()
    for ln in lines:
        for m in LABEL_DEF_RE.finditer(ln):
            labels.add(m.group(1))
        cm = CELL_LABEL_RE.match(ln)
        if cm:
            labels.add(cm.group(1))
    return labels


def audit_citations(lines, in_code, repo, findings):
    lit_dir = os.path.join(repo, "literature")
    bib_path = os.path.join(lit_dir, "mi-spectral-better-bibTeX.bib")
    bibkeys = set()
    if os.path.exists(bib_path):
        with open(bib_path, encoding="utf-8", errors="replace") as f:
            for ln in f:
                m = re.match(r"^@[A-Za-z]+\{([^,]+),", ln.strip())
                if m:
                    bibkeys.add(m.group(1).strip())

    labels = collect_labels(lines)

    cite_seen = {}      # citekey -> first line number
    crossref_seen = {}  # ref -> [line numbers]
    todo_seen = {}      # slug -> first line number

    for i, ln in enumerate(lines, 1):
        for m in TODO_RE.finditer(ln):
            todo_seen.setdefault(m.group(1), i)
        for m in CITE_RE.finditer(ln):
            key = m.group(1)
            if CROSSREF_PREFIX.match(key):
                # A literal template placeholder like `@sec-src-<key>` leaves a
                # dangling prefix; skip it. And strip trailing punctuation the
                # greedy class captured (a real label never ends in ':' or '-').
                tail = ln[m.end():m.end() + 1]
                if tail == "<":
                    continue
                ref = key.rstrip(":-")
                if ref:
                    crossref_seen.setdefault(ref, []).append(i)
                continue
            # Bibliographic citekey. Ignore obvious code identifiers inside
            # fenced python (citekeys carry a 4-digit year tail).
            if in_code[i - 1] and not re.search(r"\d{4}", key):
                continue
            cite_seen.setdefault(key, i)

    # A: each real citekey must have literature/<key>.md AND a .bib entry.
    for key, line in sorted(cite_seen.items()):
        md = os.path.join(lit_dir, f"{key}.md")
        has_md = os.path.exists(md)
        has_bib = key in bibkeys
        if not has_md:
            findings.append(dict(
                sev="BLOCKER", dim="A", line=line,
                issue=f"@{key} has no backing literature/{key}.md",
                evidence=f"missing {md}",
                fix="acquire the PDF -> Mathpix -> /lit-sync, or use @TODO:<slug>",
            ))
        if not has_bib:
            findings.append(dict(
                sev="WARN", dim="A", line=line,
                issue=f"@{key} is not in the .bib (citekey unresolved at render)",
                evidence=f"absent from {os.path.basename(bib_path)}",
                fix="re-export Better BibTeX from Zotero so the key resolves",
            ))

    # A: @TODO placeholders are unresolved drafting citations.
    for slug, line in sorted(todo_seen.items()):
        findings.append(dict(
            sev="WARN", dim="A", line=line,
            issue=f"@TODO:{slug} unresolved drafting-citation placeholder",
            evidence="bypasses the citation hook deliberately",
            fix="resolve to a real @citekey before submission, or drop the claim",
        ))

    # D: crossrefs must resolve to a defined label.
    for ref, occ in sorted(crossref_seen.items()):
        if ref not in labels:
            findings.append(dict(
                sev="WARN", dim="D", line=occ[0],
                issue=f"@{ref} crossref does not resolve to any {{#label}}",
                evidence=f"no {{#{ref}}} or '#| label: {ref}' defined ({len(occ)} use(s))",
                fix=f"define {{#{ref}}} at its target, or fix the reference",
            ))

    return dict(
        citekeys=sorted(cite_seen.keys()),
        cite_lines=cite_seen,
        crossrefs=sorted(crossref_seen.keys()),
        labels=sorted(labels),
        bibkeys=sorted(bibkeys),
        todo=sorted(todo_seen.keys()),
    )


# ----------------------------------------------------------------------------
# B (mechanical). Source-note linerefs resolve; Appendix-A snippets present.
# ----------------------------------------------------------------------------

def build_alias_map(lines):
    """Map sec-src-<alias> anchors to the citekey named inside that section."""
    alias_to_key = {}
    cur_alias = None
    for ln in lines:
        m = SRC_SECTION_RE.match(ln)
        if m:
            cur_alias = m.group(1)  # e.g. sec-src-schafer
            continue
        if cur_alias:
            cm = INLINE_CITE_RE.search(ln)
            if cm:
                alias_to_key[cur_alias] = cm.group(1)
                cur_alias = None
    return alias_to_key


_LINECOUNT_CACHE = {}


def lit_line_count(repo, citekey):
    if citekey in _LINECOUNT_CACHE:
        return _LINECOUNT_CACHE[citekey]
    p = os.path.join(repo, "literature", f"{citekey}.md")
    n = None
    if os.path.exists(p):
        with open(p, encoding="utf-8", errors="replace") as f:
            n = sum(1 for _ in f)
    _LINECOUNT_CACHE[citekey] = n
    return n


def audit_linerefs(lines, repo, alias_map, findings):
    """Each href-style :NNNN anchor must point inside the source's md file."""
    bad = 0
    total = 0
    for i, ln in enumerate(lines, 1):
        for m in LINEREF_RE.finditer(ln):
            total += 1
            alias = "sec-src-" + m.group(1)
            line_no = int(m.group(2))
            key = alias_map.get(alias)
            if key is None:
                findings.append(dict(
                    sev="WARN", dim="B", line=i,
                    issue=f"lineref :{line_no} cites #{alias} with no Appendix-A section",
                    evidence=f"no '### ... {{#{alias}}}' header found",
                    fix="add the source section, or fix the href anchor",
                ))
                bad += 1
                continue
            n = lit_line_count(repo, key)
            if n is None:
                continue  # already reported by citation audit
            if line_no > n:
                findings.append(dict(
                    sev="BLOCKER", dim="B", line=i,
                    issue=f"lineref :{line_no} overruns literature/{key}.md ({n} lines)",
                    evidence=f"file has {n} lines; anchor points past EOF",
                    fix="re-sync the literature copy or correct the line number",
                ))
                bad += 1
    return dict(linerefs_total=total, linerefs_bad=bad)


def _normalize(text):
    """Lowercase, drop math/markup punctuation, collapse whitespace."""
    text = re.sub(r"\$[^$]*\$", " ", text)       # inline math
    text = re.sub(r"\\[a-zA-Z]+", " ", text)     # latex commands
    text = re.sub(r"[^a-z0-9 ]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def audit_appendix_snippets(lines, repo, alias_map, findings):
    """For each Appendix-A blockquote, check a distinctive word-run appears in
    the source md. Reported as INFO when not found (Mathpix math markup makes
    exact matching unreliable; the model does the authoritative check)."""
    cur_alias = None
    checked = 0
    not_found = 0
    src_cache = {}

    def source_text(key):
        if key in src_cache:
            return src_cache[key]
        p = os.path.join(repo, "literature", f"{key}.md")
        t = ""
        if os.path.exists(p):
            with open(p, encoding="utf-8", errors="replace") as f:
                t = _normalize(f.read())
        src_cache[key] = t
        return t

    for i, ln in enumerate(lines, 1):
        m = SRC_SECTION_RE.match(ln)
        if m:
            cur_alias = m.group(1)
            continue
        if cur_alias and ln.lstrip().startswith(">"):
            key = alias_map.get(cur_alias)
            if not key or lit_line_count(repo, key) is None:
                continue
            quote = _normalize(ln.lstrip()[1:])
            words = quote.split()
            # longest contiguous run of alphabetic words as a fingerprint that
            # survives math stripping
            run, best = [], []
            for w in words:
                if w.isalpha() and len(w) > 2:
                    run.append(w)
                    if len(run) > len(best):
                        best = run[:]
                else:
                    run = []
            if len(best) < 6:
                continue  # too math-heavy to fingerprint mechanically
            checked += 1
            fp = " ".join(best[:8])
            if fp not in source_text(key):
                not_found += 1
                findings.append(dict(
                    sev="INFO", dim="B", line=i,
                    issue=f"Appendix-A snippet fingerprint not found verbatim in literature/{key}.md",
                    evidence=f'"{fp}..." (mechanical substring miss; verify manually)',
                    fix="confirm the quote against the source; re-sync if drifted",
                ))
    return dict(snippets_checked=checked, snippets_not_found=not_found)


# ----------------------------------------------------------------------------
# C. Reproducibility pointers + [mc] <-> assert pairing
# ----------------------------------------------------------------------------

PATH_RE = re.compile(r"`([^`]*?(?:verification|todo|manuscript)[^`]*?)`")
PHASE_RE = re.compile(r"\bphase[\s-]?(\d+)\b", re.IGNORECASE)


def _brace_expand(s):
    """Expand one level of {a,b}/{0..5} brace groups into the full list of
    alternatives (cartesian product across groups). Returns [s] if no
    expandable group is present."""
    m = re.search(r"\{([^{}]*)\}", s)
    if not m:
        return [s]
    body = m.group(1)
    rng = re.match(r"^(\d+)\.\.(\d+)$", body)
    if rng:
        alts = [str(i) for i in range(int(rng.group(1)), int(rng.group(2)) + 1)]
    elif "," in body:
        alts = body.split(",")
    else:
        return [s]  # not an expandable group (e.g. literal braces)
    out = []
    for alt in alts:
        out.extend(_brace_expand(s[:m.start()] + alt + s[m.end():]))
    return out


def _pointer_exists(repo, target_dir, cand):
    """Resolve a backticked path against the repo root, the target file's dir
    (manuscript/), a todo/0NN prefix, or a glob base. Return True if any hits.
    Brace groups `{a,b}` / `{0..5}` are expanded; the pointer counts as
    existing only if EVERY expansion resolves (it names a set of artifacts)."""
    import glob
    norm = cand.replace("\\", "/")
    expansions = _brace_expand(norm)
    if len(expansions) > 1:
        return all(_pointer_exists(repo, target_dir, e) for e in expansions)
    base = re.split(r"[*{]", norm)[0].rstrip("/")
    parts = base.split("/")
    for root in (repo, target_dir):
        full = os.path.join(root, *parts)
        if os.path.exists(full):
            return True
        if base.endswith("/") and os.path.isdir(full):
            return True
        # globbed/wildcard tail: the resolved base directory existing is enough
        if ("*" in norm or "{" in norm) and os.path.isdir(full):
            return True
    # todo/008  -> matches todo/008-*.md  (numeric todo item shorthand)
    tm = re.match(r"^todo/(\d+)$", base)
    if tm and glob.glob(os.path.join(repo, "todo", tm.group(1) + "*")):
        return True
    return False


def audit_repro_pointers(lines, in_code, repo, target_dir, findings):
    """Every backticked verification/* , todo/* path the prose names should
    exist on disk. Phase-N mentions should map to a run_all phase dir."""
    seen = {}
    for i, ln in enumerate(lines, 1):
        if in_code[i - 1]:
            continue  # code blocks reference their own paths legitimately
        for m in PATH_RE.finditer(ln):
            raw = m.group(1).strip()
            cand = raw.split()[0].rstrip(").,;")
            # require a real path shape: a separator or a file extension
            if not re.search(r"[\\/]", cand) and not re.search(
                r"\.(R|csv|rds|json|md|qmd)$", cand
            ):
                continue
            seen.setdefault(cand, i)

    for cand, line in sorted(seen.items()):
        if _pointer_exists(repo, target_dir, cand):
            continue
        norm = cand.replace("\\", "/")
        base = re.split(r"[*{]", norm)[0].rstrip("/")
        full = os.path.join(repo, *base.split("/"))
        note = ""
        legacy = os.path.join(os.path.dirname(full), "_legacy",
                              os.path.basename(full))
        modular = os.path.join(os.path.dirname(full), "_modules",
                               os.path.basename(full).lower())
        if os.path.exists(legacy):
            note = " (exists only under _legacy/ - CLAUDE.md says do not re-run it)"
        elif os.path.exists(modular):
            note = f" (canonical module is _modules/{os.path.basename(full).lower()})"
        findings.append(dict(
            sev="WARN", dim="C", line=line,
            issue=f"reproducibility pointer `{cand}` does not exist{note}",
            evidence=f"no file/dir at {full}",
            fix="correct the path to the artifact that actually reproduces the claim",
        ))

    # Phase-N mentions in prose -> run_all-*/phaseN* dirs anywhere
    cache_root = os.path.join(repo, "verification", "cache")
    phase_dirs = set()
    if os.path.isdir(cache_root):
        for d in os.listdir(cache_root):
            sub = os.path.join(cache_root, d)
            if os.path.isdir(sub):
                for p in os.listdir(sub):
                    pm = re.match(r"phase(\d+)", p)
                    if pm:
                        phase_dirs.add(pm.group(1))
    phase_mentions = {}
    for i, ln in enumerate(lines, 1):
        if in_code[i - 1]:
            continue
        for m in PHASE_RE.finditer(ln):
            phase_mentions.setdefault(m.group(1), i)
    for num, line in sorted(phase_mentions.items()):
        if num not in phase_dirs:
            findings.append(dict(
                sev="WARN", dim="C", line=line,
                issue=f"prose cites run_all phase {num} but no phase{num}* cache dir exists",
                evidence=f"phase dirs present: {sorted(phase_dirs)}",
                fix="run that phase, or correct the phase number cited",
            ))
    return dict(repro_pointers=sorted(seen.keys()), phase_dirs=sorted(phase_dirs))


def audit_mc_blocks(lines, findings):
    """Pair each lst-mc-* python listing with an assert; pair each @lst-mc-*
    reference with a listing that has one."""
    listings = {}            # label -> {line, has_assert}
    cur_start = None
    in_block = False
    block_has_assert = False
    block_label = None
    for i, ln in enumerate(lines, 1):
        if re.match(r"^\s*```\{", ln):       # opening a code cell
            in_block = True
            block_has_assert = False
            block_label = None
            cur_start = i
            continue
        if in_block and re.match(r"^\s*```\s*$", ln):  # closing
            if block_label:
                listings[block_label] = dict(
                    line=cur_start, has_assert=block_has_assert)
            in_block = False
            continue
        if in_block:
            cm = CELL_LABEL_RE.match(ln)
            if cm and cm.group(1).startswith("lst-mc"):
                block_label = cm.group(1)
            if re.search(r"\bassert\b", ln):
                block_has_assert = True

    for label, info in sorted(listings.items()):
        if not info["has_assert"]:
            findings.append(dict(
                sev="WARN", dim="C", line=info["line"],
                issue=f"listing {label} has no `assert` (an [mc] check with nothing checked)",
                evidence="code cell defines the label but asserts no identity",
                fix="add an assert reducing lhs-rhs to 0, or drop the [mc] claim",
            ))

    mc_tag_lines = [i for i, ln in enumerate(lines, 1)
                    if re.search(r"\[mc\]", ln)]
    referenced = {}
    for i, ln in enumerate(lines, 1):
        for m in re.finditer(r"@(lst-mc-[A-Za-z0-9_\-]+)", ln):
            referenced.setdefault(m.group(1), i)
    for label, line in sorted(referenced.items()):
        if label not in listings:
            findings.append(dict(
                sev="BLOCKER", dim="C", line=line,
                issue=f"[mc] references @{label} but no such listing exists in Appendix B",
                evidence=f"no '#| label: {label}' code cell found",
                fix="add the listing, or correct the @lst-mc reference",
            ))

    return dict(
        listings=sorted(listings.keys()),
        listings_without_assert=[k for k, v in listings.items()
                                 if not v["has_assert"]],
        mc_tag_count=len(mc_tag_lines),
        referenced_listings=sorted(referenced.keys()),
    )


# ----------------------------------------------------------------------------
# F. Reference lifecycle (todo/003)
# ----------------------------------------------------------------------------

def _author_year(key):
    """Leading lowercase author run + 4-digit year of a BBT citekey."""
    author = re.match(r"^[a-z]+", key)
    year = re.search(r"(\d{4})", key)
    return (author.group(0) if author else key.lower(),
            year.group(1) if year else "")


def audit_lifecycle(repo, citekeys, cite_lines, findings):
    path = os.path.join(repo, "todo", "003-references-to-acquire.md")
    if not os.path.exists(path):
        return dict(todo003="missing")
    with open(path, encoding="utf-8", errors="replace") as f:
        txt = f.read()
    low = txt.lower()
    # Foundational corpus is tracked in todo/001, not the 003 proposal lifecycle.
    found_path = os.path.join(repo, "todo", "001-literature-and-hooks.md")
    found_txt = ""
    if os.path.exists(found_path):
        with open(found_path, encoding="utf-8", errors="replace") as f:
            found_txt = f.read().lower()
    for key in citekeys:
        if key.lower() not in low:
            auth, yr = _author_year(key)
            in_001 = (len(auth) >= 3 and auth in found_txt
                      and (not yr or yr in found_txt))
            if in_001:
                findings.append(dict(
                    sev="INFO", dim="F", line=cite_lines.get(key, 0),
                    issue=f"@{key} not in todo/003 lifecycle (foundational corpus, tracked in todo/001)",
                    evidence=f"author/year '{auth} {yr}' present in 001-literature-and-hooks.md",
                    fix="expected for the Phase-1 corpus; no action unless you want it in 003",
                ))
                continue
            findings.append(dict(
                sev="WARN", dim="F", line=cite_lines.get(key, 0),
                issue=f"@{key} cited in manuscript but untracked in any lifecycle log",
                evidence="named in neither todo/003 nor todo/001",
                fix="add a row marking it verified/cited (proposal-tracking discipline)",
            ))
            continue
        ok = False
        for m in re.finditer(re.escape(key.lower()), low):
            window = low[max(0, m.start() - 400): m.end() + 400]
            if "verified" in window or "cited" in window:
                ok = True
                break
        if not ok:
            findings.append(dict(
                sev="WARN", dim="F", line=cite_lines.get(key, 0),
                issue=f"@{key} cited but not marked verified/cited in todo/003",
                evidence="named in 003 but no 'verified'/'cited' status nearby",
                fix="promote to verified once read in-session and claim checked",
            ))
    return dict(todo003="present")


# ----------------------------------------------------------------------------
# Reporting
# ----------------------------------------------------------------------------

SEV_ORDER = {"BLOCKER": 0, "WARN": 1, "INFO": 2}
DIM_NAME = {
    "A": "Citation integrity",
    "B": "Evidence <-> external text",
    "C": "Reproducibility / simulation",
    "D": "Internal consistency",
    "E": "Honesty / over-claiming",
    "F": "Reference lifecycle",
}


def render_markdown(target, findings, summary):
    findings = sorted(findings, key=lambda f: (SEV_ORDER[f["sev"]],
                                               f["dim"], f["line"]))
    n_block = sum(1 for f in findings if f["sev"] == "BLOCKER")
    n_warn = sum(1 for f in findings if f["sev"] == "WARN")
    n_info = sum(1 for f in findings if f["sev"] == "INFO")
    verdict = "FAIL" if n_block else ("PASS-WITH-WARNINGS" if n_warn else "PASS")

    base = os.path.basename(target)
    out = []
    out.append(f"# Derivation audit (mechanical) - `{base}`")
    out.append("")
    out.append(f"**{verdict}** - {n_block} BLOCKER / {n_warn} WARN / {n_info} INFO "
               "(mechanical dimensions A / B-linerefs / C / D / F only; "
               "semantic B and honesty E are graded by the skill model).")
    out.append("")
    out.append("| Dim | Dimension | BLOCKER | WARN | INFO |")
    out.append("|---|---|---|---|---|")
    for d in ["A", "B", "C", "D", "F"]:
        b = sum(1 for f in findings if f["dim"] == d and f["sev"] == "BLOCKER")
        w = sum(1 for f in findings if f["dim"] == d and f["sev"] == "WARN")
        ii = sum(1 for f in findings if f["dim"] == d and f["sev"] == "INFO")
        out.append(f"| {d} | {DIM_NAME[d]} | {b} | {w} | {ii} |")
    out.append("")
    for sev in ["BLOCKER", "WARN", "INFO"]:
        group = [f for f in findings if f["sev"] == sev]
        if not group:
            continue
        out.append(f"## {sev} ({len(group)})")
        out.append("")
        for f in group:
            loc = f"{base}:{f['line']}" if f["line"] else base
            out.append(f"- `{loc}` [{f['dim']}] - {f['issue']} - "
                       f"evidence: {f['evidence']} - fix: {f['fix']}")
        out.append("")
    out.append("---")
    out.append("## Context for the semantic pass (not findings)")
    out.append(f"- citekeys cited: {', '.join(summary['cites']['citekeys']) or '(none)'}")
    out.append(f"- lst-mc listings: {', '.join(summary['mc']['listings']) or '(none)'}")
    out.append(f"- linerefs resolved: "
               f"{summary['linerefs']['linerefs_total'] - summary['linerefs']['linerefs_bad']}"
               f"/{summary['linerefs']['linerefs_total']}")
    out.append(f"- Appendix-A snippets fingerprint-checked: "
               f"{summary['snippets']['snippets_checked']} "
               f"({summary['snippets']['snippets_not_found']} fingerprint-miss)")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--repo", default=None)
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    target = os.path.abspath(args.target)
    if not os.path.exists(target):
        print(f"ERROR: target not found: {target}", file=sys.stderr)
        return 3
    repo = args.repo or os.path.dirname(os.path.dirname(target))
    repo = os.path.abspath(repo)

    lines = read_lines(target)
    in_code = strip_code_fences(lines)
    findings = []

    cites = audit_citations(lines, in_code, repo, findings)
    alias_map = build_alias_map(lines)
    linerefs = audit_linerefs(lines, repo, alias_map, findings)
    snippets = audit_appendix_snippets(lines, repo, alias_map, findings)
    repro = audit_repro_pointers(lines, in_code, repo, os.path.dirname(target),
                                 findings)
    mc = audit_mc_blocks(lines, findings)
    audit_lifecycle(repo, cites["citekeys"], cites["cite_lines"], findings)

    summary = dict(cites=cites, linerefs=linerefs, snippets=snippets,
                   repro=repro, mc=mc, alias_map=alias_map)

    md = render_markdown(target, findings, summary)
    print(md)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(dict(target=target, repo=repo, findings=findings,
                           summary=summary), f, indent=2)
    return 2 if any(f["sev"] == "BLOCKER" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
