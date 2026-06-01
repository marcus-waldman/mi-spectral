---
name: derivation-audit
description: >-
  Audit the mi-spectral sourced derivation (manuscript/derivation.qmd, or any
  manuscript/*.qmd) for verification and citation-discipline compliance, and
  emit a flag-only report. READ-ONLY: it diagnoses and flags, it never edits the
  manuscript or literature. Use this whenever the user asks to audit, check,
  verify, vet, or review the derivation / the proof / the sourced derivation for
  citation integrity, broken source pointers, hallucinated or unsupported
  citations, unreproducible numbers, dangling cross-references, missing Monte
  Carlo asserts, or over-claiming — and when they say "/derivation-audit",
  "audit the derivation", "is every claim sourced", "check the proof's
  citations", or "does the evidence actually back the claims".
---

# Derivation audit

Audit a sourced derivation in `manuscript/` against this repo's verification and
citation-discipline conventions, and produce a **flag-only report**. You
diagnose and flag; you **never edit** the manuscript, the `literature/` corpus,
the `.bib`, or any `todo/`/`verification/` file. The deliverable is the report.

**Target.** The argument is the path to audit. Default to
`manuscript/derivation.qmd` (the canonical sourced derivation) when none is
given; also accept `manuscript/mi-spectral.qmd` or any `manuscript/*.qmd`.

## Why this skill exists

This is a citation-disciplined, AI-assisted theory paper for JAIGP. The
load-bearing defense against the way AI-assisted derivations fail in review is
that **every external claim points to a real source passage that actually says
what the claim attributes to it**, and **every number points to a reproducible
artifact that exists**. The repo enforces a slice of this at edit time (the
`PreToolUse` hook in `.claude/hooks/check_citations.py` blocks `@citekey` writes
with no backing `literature/<citekey>.md`). This skill is the standing,
whole-document audit the hook can't do: it mirrors the hook's mechanical rule
**and** checks the things the hook never sees — whether the source text supports
the claim, whether the cited numbers reproduce, whether the cross-references and
`[mc]` asserts hold together, and whether the prose over-claims its own scope.

## How the document is built (the idioms you are auditing)

Read `manuscript/derivation.qmd` once to ground yourself before judging it. The
conventions it follows, and that your checks key off:

- **`@citekey`** — a bibliographic citation. Must have BOTH a
  `literature/<citekey>.md` (the Mathpix-converted source text, with YAML
  frontmatter: `citekey, authors, year, title, venue, doi, source_pdf,
  pdf_sha256, converted_via, last_synced`) AND an entry in
  `literature/mi-spectral-better-bibTeX.bib`. This is the hook's rule.
- **`@eq-… @sec-… @lst-… @fig-… @tbl-… @thm-…`** (and `lem/cor/prp/cnj/def/exm/
  exr/sol/rem`) — Quarto **cross-references**, NOT citations. They resolve to a
  `{#label}` defined in the doc (or a `#| label:` on a code cell). Never treat
  these as citekeys — that is the classic false positive (the repo's own
  `lit_sync.py` trips on it).
- **`@TODO:<slug>`** — a deliberate drafting placeholder that bypasses the hook.
- **"Source." margin notes** (`::: {.column-margin}`) — carry the provenance: a
  source equation/theorem number, a verbatim snippet, and a `:lineref` of the
  form `<a href="#sec-src-<alias>"><code>:NNNN</code></a>` pointing into the
  `literature/<citekey>.md` copy. The snippet is a re-pagination-stable anchor.
- **Step tags** — `[derived]` (proved here, not cited), `[mc]`
  (machine-checked: additionally has an executable assert in Appendix B),
  `[cited]`. Definition/regularity/lemma labels are `D-`, `R-`, `L-`, `A-`.
- **Appendix A** (`#sec-src-*`) — verbatim source passages grouped by reference,
  each `> quoted` from the `literature/` copy with its equation/theorem number
  and line.
- **Appendix B** (`#sec-verify`) — inline ```` ```{python} ```` cells labelled
  `#| label: lst-mc-*`, each reducing `lhs - rhs` to `0` symbolically or
  asserting a match to `verification/00-setup.R` to machine precision. Every
  `[mc]` tag should correspond to one of these with a real `assert`.
- **Reproducibility layering** — numbers trace to `verification/run_all.R`
  phases (outputs under `verification/cache/run_all-<suffix>/phase{0..N}/`),
  standalone `verification/*.R` diagnostics, or committed `*.rds`/`summary.csv`
  caches. The originals `W1-bias-decomposition.R` etc. are preregistered;
  `_legacy/` scripts are retired and **must not** be cited as live artifacts.

## Step 1 — run the mechanical engine

Run the bundled script from the repo root. It does the deterministic checks
(citation backing, crossref resolution, reproducibility-pointer existence,
`[mc]`↔assert pairing, lineref resolution, Appendix-A snippet fingerprints,
todo/003 lifecycle) and prints a markdown report plus a JSON dump.

```
py .claude/skills/derivation-audit/scripts/audit_derivation.py <target.qmd> --json <tmp>/derivation-audit.json
```

(`Rscript` is not involved; this is pure Python, stdlib only.) Read both the
markdown and the JSON. The JSON `summary` block gives you the working lists you
need for Step 2: `cites.citekeys`, `mc.listings`, `alias_map`
(`sec-src-<alias>` → citekey), and the resolved/total lineref counts.

The engine is the source of truth for dimensions **A** (citation integrity),
**D** (crossref resolution), **C** (reproducibility pointers + `[mc]` asserts),
**F** (lifecycle), and the **mechanical** half of **B** (linerefs resolve;
snippet fingerprints). Carry its findings into your report verbatim (adjust
severity only with a stated reason). Do **not** re-derive what it already
computed.

## Step 2 — the semantic source check (dimension B, the hard part)

This is the check the engine cannot do and the reason the skill exists: **does
the cited source actually support the claim made about it?** A citation that
resolves to a real file and a real line can still attribute an equation the
source never states, or assert something the source contradicts. Mirror the
repo rule: *reliance on training-weight knowledge of a cited paper is
prohibited — verify against the local text.*

For each cited `@citekey` (use `cites.citekeys` from the JSON), and for each
distinct claim the derivation attributes to it (the margin "Source." notes and
the Appendix-A entries name the equation/theorem number and the proposition the
derivation leans on):

1. Read the relevant span of `literature/<citekey>.md` (use the `:lineref`
   anchors and the Appendix-A line numbers to jump to the right place — you do
   not need the whole file).
2. Confirm the source **contains** the cited equation/theorem/result, and that
   the **claim the derivation makes about it** is supported by the source text —
   not merely that the paper is cited near the claim.
3. Confirm each Appendix-A `> verbatim` block is genuinely present (exact or
   near-exact, modulo Mathpix math markup) in that file. The engine flags
   fingerprint misses as INFO; you make the call on whether the quote is
   faithful or drifted.

Grade each attribution:

- **supported** — no finding.
- **mismatch / unsupported / unverifiable from the local text** — **BLOCKER**.
  This is the user's "evidence tangibly validated against external exact text":
  a claim whose attributed source does not back it fails the audit.

Also flag (here, where you have the source in hand):

- An **external or non-trivial assertion that carries no source pointer and is
  not marked `[derived]`** — WARN (an un-sourced claim that reads as if
  external).
- A step **marked `[derived]` that secretly leans on an external result** —
  WARN (it should cite, or the derivation should actually be self-contained).

**Bound the work.** This can fan out. If a subagent tool is available, dispatch
one reader per cited citekey (or per source-section), each returning a short
verdict list `{claim, source eq/thm, supported|mismatch|unverifiable,
evidence}`; then fold the verdicts into your report. Otherwise read the sources
inline, prioritizing the load-bearing citations (the ones the theorem and the
two applications actually turn on — e.g. the missing-information identity, the
RIV identification, the variance-recovery lemma, the observed-information-under-
MAR choice, and whatever the headline-IC positioning rests on) over the
boilerplate matrix-identity citations.

## Step 3 — evidence-type vs claim-type (dimension C, semantic)

Beyond "does the artifact exist" (engine), check that the **kind** of evidence
matches the **kind** of claim:

- An **"exact" / "symbolic" / "parameterization-free"** claim backed **only by
  Monte Carlo or a single numeric replicate** → WARN (evidence weaker than the
  claim).
- An **`O(1)` / asymptotic / "does not decay" / `O(n^-1)`** claim backed **only
  by a single finite-`n` point** → WARN.
- A number or "the simulation confirms / the cache gives" with **no
  reproducible pointer at all** → WARN (the engine catches broken pointers; you
  catch *missing* ones in prose).

## Step 4 — internal consistency of the headline (dimension D, semantic)

The engine confirms cross-refs resolve. You additionally confirm the **headline
result is stated consistently** across the introduction, the theorem statement,
and the combine step — same governing equation, same scope conditions. Flag
contradictions (WARN), e.g. an MCAR-only clean result stated as general in one
place and scoped in another, or the `(A)+(C)` design-imbalance term present in
one statement and silently dropped in another.

## Step 5 — honesty / over-claiming (dimension E)

- Flag language that **outruns its stated verification** — "proved", "exact",
  "for any regular family", "general", "holds in general" — wherever the doc's
  own scope notes say "asserted", "spot-checked", "to leading order",
  "`O(n^-1)`", "open", "MVN instantiation", "bivariate-monotone only", or
  "verified empirically (symbolic check deferred)". Surface any claim stronger
  than the evidence the same document admits. Severity: **WARN** (BLOCKER only
  if the overclaim is the headline itself).
- Flag **house-jargon in outside-reader-facing prose** (intro, roadmap, proof
  sketch, motivated narrative): `ledger`, `numerical witness`, `tagged`,
  `machine-checked`, `Stage N`, `consume`. Severity: **INFO**. (These are fine
  in margin notes and internal scaffolding; the ban is about reader-facing
  prose.)

## Output — one flag-only markdown report

Print a single report. Begin with a one-line **PASS / FAIL** summary (FAIL iff
any BLOCKER) and per-dimension counts, then group findings by severity. Each
finding is one line:

```
<file>:<line> — <issue> — evidence: <found | "snippet not in source" | "no cache" | …> — fix: <one-line suggested fix>
```

Severity:

- **BLOCKER** — a missing `literature/<citekey>.md` for a real citekey (the
  hook's rule); a claim whose attributed source does not support it or cannot be
  verified from the local text; a lineref that overruns its source file; an
  `[mc]`/`@lst-mc-*` reference with no backing listing. These fail the audit.
- **WARN** — over-claiming beyond stated scope; evidence-type vs claim-type
  mismatch; un-sourced non-trivial assertion; `[mc]` listing with no `assert`;
  reproducibility pointer to a missing or `_legacy/` artifact; dangling
  crossref; headline inconsistency; cited-but-not-logged-as-verified in
  todo/003; `@TODO:` placeholder; citekey missing from the `.bib`.
- **INFO** — house-jargon in reader-facing prose; Appendix-A snippet fingerprint
  misses you judged to be markup artifacts rather than real drift; foundational
  corpus not in the todo/003 lifecycle (tracked in todo/001).

Suggested-fix lines describe the fix; **do not apply it**. Use the template
below.

```
## Derivation audit — <file>

**<PASS|FAIL>** — <nB> BLOCKER / <nW> WARN / <nI> INFO
A citation <a/b/c> · B evidence↔source <…> · C reproducibility <…> · D consistency <…> · E honesty <…> · F lifecycle <…>

### BLOCKER (<n>)
- <file>:<line> — <issue> — evidence: <…> — fix: <…>

### WARN (<n>)
- …

### INFO (<n>)
- …
```

## Guardrails

- **Read-only.** Never Edit/Write/MultiEdit the manuscript, `literature/`, the
  `.bib`, or `todo/`/`verification/` files. If asked to fix something, propose
  the fix in the report and stop. (Writing this report to a scratch file the
  user asked for is fine; touching the audited material is not.)
- **No training-weight citations.** Every B verdict must rest on text you read
  in `literature/<citekey>.md` this session. If a source file is missing, that
  is the BLOCKER — do not paper over it from memory.
- **Don't re-flag what the engine flagged**; fold its findings in and add the
  semantic ones. If you disagree with an engine severity, say so with a reason.
- Use Windows-style backslash paths with the file tools (per the repo's
  `CLAUDE.md`), and run the script with `py` from the repo root.
