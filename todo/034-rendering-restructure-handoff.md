# todo/034 — Rendering polish + AI-collaboration section restructure (HANDOFF)

**Status:** OPEN, not started. Authored 2026-06-27 as a handoff after the prose
readability pass (commit `675323a` on branch `prose-readability-pass`).

**Read first:** this builds on the readability pass. That work is committed on branch
`prose-readability-pass` (FK 11.9→10.1, T-08 oracle rename, G7 renumber) but **NOT yet
merged to `main`** — `main` does not have it. Merge that branch (or rebase this work on
it) before starting, so the prose base is current.

Six work items, from Marcus reading the JASA preview PDF
(`manuscript/preview-jasa/mi-spectral-preview.pdf`). Items 1–4 are rendering/figure
polish; item 5 is the template switch; item 6 is a structural restructure that needs one
decision from Marcus before drafting.

Ground rules (unchanged): level3-paragraphs.json is the prose source of truth; make
changes via atomic scripts under `manuscript/plan/updates/`; `check_plan` must stay
green; the preview is rebuilt with `manuscript/preview-jasa/build_preview.py` then
`quarto render` (quarto is at
`C:\Program Files\RStudio\resources\app\bin\quarto\bin\quarto.exe`).

---

## 1. Long display equations run off the page → break at commas onto new lines

**Symptom (Marcus):** long equations overflow the right margin. Fix: where a long
display equation contains `,` (or `\qquad`/`\quad` separators), put the pieces on
separate lines.

**Where:** the `$$…$$` blocks live inside `draft_prose` in level3-paragraphs.json.
**Method:** wrap the multi-part equations in an `aligned`/`gathered`/`split` environment
and break after each `,` / `\qquad` with `\\`. Keep every token verbatim (same
token-preservation discipline as the readability pass — do not alter any symbol).

**Concrete candidates** (display blocks >110 chars with ≥1 comma; from
`scratchpad/scan_eqs.py`):

| Paragraph | blocks to break |
|---|---|
| S2-P13 | the `\hat d_L … , \qquad …` combining statistic (2 commas) |
| S4-P3 | RIV definition chain (219 chars) |
| S4-P4 | `\bar Q_\infty` definition (280 chars, 4 commas) |
| S4-P5 | the `T = …` decomposition (332 chars) |
| S4-P6 | three blocks (210/267/199 chars) — covariance identities |
| S4-P7 | three blocks (206/240/382 chars) — the `T_imp` expansion |
| S4-P7b | `(A)=…,\qquad(C)=…` and the `(A)+(C)` block |
| S4-P8 | the known-scale `\begin{cases}` block |
| S4-P10 | two blocks (375/249 chars) |
| S4-P11 | three blocks (Gram/Schur inequalities) |
| S4-P19 | the projector block (246 chars, 10 commas) |
| S4-P20 | the `\hat d^{(2)}` / `\hat d^{(3)}` equating maps (the worst offenders) |

These are the most likely cause of item 4 as well (see below).

## 2. "Some sections render as `$$` / equation not given"

**Diagnosis done:** every `$$` in level3 is balanced (no unclosed math), so this is NOT
malformed markup. Two live hypotheses, check both:
- **(a) Overflow (most likely).** The long single-line equations of item 1 overflow and
  look clipped/blank. After fixing item 1, re-render and check the xelatex log for
  `Overfull \hbox` warnings:
  `manuscript/preview-jasa/mi-spectral-preview.log` (or the `.tex`).
- **(b) Blank-line separation.** `build_preview.py` emits each paragraph with one blank
  line before it (line 84–86), but inside a `draft_prose` string the `$$…$$` blocks are
  flanked by single `\n`, not blank lines, and some carry a `{#eq-…}` label right after
  the closing `$$`. If any equation renders as literal `$$`, grep the generated
  `mi-spectral-preview.tex` for a literal `$$` or an unparsed `{#eq-` and, if found, have
  `build_preview.py` insert blank lines around `$$…$$` blocks (or normalize the prose so
  each display block is blank-line separated).

## 3. Figures — legend outside, transparency, coherent color scheme

**Where:** `verification/figures.R` (442 lines, **base R graphics**, not ggplot — uses
`grDevices::png`, `legend()`, `adjustcolor`). Palette object is `COL$…` and a
`bandfill` defined near lines 40–52. Find the driver that calls it (the figures land in
`manuscript/figures/`; locate the source that runs `figures.R` and regenerate after
editing — the tool rejected the `ls` mid-session, so confirm the figures dir path first).

Four changes:
- **(a) Legends outside the plot area.** Every panel currently places the legend inside
  via `legend("topright"/"right"/"left"/"bottomright"/...)`. Move them out: reserve
  margin with `par(mar=…)` (or `par(oma=…)` + `xpd=NA`) and draw the legend at outer
  coordinates, or below/right of the plot. (~8 `legend()` calls, lines 130, 167, 239,
  269, 298, 333, 399, 424.)
- **(b) Slight transparency on data points AND bars** — Marcus: overlaid labels are
  camouflaged against the background; fix with alpha on points/bars so labels read
  through. Some alpha already exists (`adjustcolor(..., alpha.f=0.08/0.10)` for bands);
  extend consistently to point/bar fills.
- **(c) Consistent, cogent color scheme** designed to work WITH the transparency. Define
  one coherent palette in `COL` (e.g. a colorblind-safe set) and use it across all
  panels; pick alpha levels that keep labels legible.
- **(d) CONSISTENCY CATCH (do this here):** several figure legends still say
  `"oracle (perfect)"` / `"complete-data oracle (perfect)"` (lines ~298–299, 333–334).
  The prose was renamed under T-08 (oracle → "complete-data benchmark" / "true-model
  expectation"). Rename the legend labels to **"complete-data benchmark (perfect)"** to
  match. The figure CAPTIONS in level3 already say "complete-data benchmark"; the PNGs
  are stale.

## 4. Switch to the arXiv Quarto template

Marcus: "switch to the arxiv quarto template (find and install online)."
- Find an arXiv **format extension** for Quarto online and install with
  `quarto add <org/repo>` (or `quarto use template <…>`) in `manuscript/preview-jasa/`.
  (There is no arXiv format in the official `quarto-journals`; use a vetted community
  extension. Requires internet.)
- Switch the front-matter `format:` in `build_preview.py` (currently `jasa-pdf`, lines
  ~37–49) to the arXiv format; adjust author/affiliation/abstract keys to that template's
  schema. Re-render.
- Note: the eventual **canonical** compile (`scripts/compile_manuscript.py` →
  `manuscript/mi-spectral.qmd`, still `compile_enabled=false`) should adopt the same
  format when compile is enabled.

## 5. New section "AI human collaboration" (between Introduction and Background)

**Marcus's intent:** the subsections about the AI–human workflow should be pulled out
into a NEW section, placed between the Introduction and the Background, titled
**"AI human collaboration"**. Be explicit that this is **a novelty in the age of AI**,
and that **one stated goal of the paper is to demonstrate a workflow that is both
productive and produces accurate conclusions.**

**Source material already in the manuscript** (where the AI/human/workflow content lives
now):
- **S1-P7** (end of Introduction) — "One feature of this paper bears on how it was made…"
  (AI/human/ORCID/workflow). Natural seed for the new section's opening.
- **S3-P1, S3-P2, S3-P3, S3-P8** (Methods: "the derivation and verification workflow") —
  S3-P1 "derivations produced by…", S3-P2 "Roles and decision records", S3-P3 "Sourced
  citations", S3-P8 the section wrap.
- **S6-P8** (Discussion) — "A final word on the workflow" (likely STAYS as the closing
  reflection; confirm).

**DECISION NEEDED FROM MARCUS before drafting** (do not guess):
- S3 is literally titled *"Methods: the derivation and verification workflow."* The new
  "AI human collaboration" section overlaps it. Decide the split: does the new early
  section take the **narrative/novelty framing** (why AI-human collaboration, the
  productivity+accuracy goal, roles, provenance) while S3 keeps the **operational methods
  detail** (citation discipline, verification gates, CAS/cross-model checks)? Or does the
  whole workflow material move forward, leaving S3 to be renamed/absorbed?
- Section numbering/anchors: inserting between S1 and S2 means either a new id like
  `S1B` (anchor e.g. `sec-ai-collab`) or renumbering S2→S3→… Pick the scheme.

**Structural work once decided:** add the section to `sections_order`; create/move the
paragraphs (new framing prose making the novelty + productivity-and-accuracy goal
explicit); update `level1-thesis.json` (the IMRaD arc/move map) and
`level2-sections.json` (section list + super-propositions) so the plan stays coherent;
fix `depends_on`/`dep_types`; run `check_plan`; rebuild preview. This is a real
restructure of the plan scaffold, not just a prose edit — budget for it.

---

## Suggested order
1. Merge `prose-readability-pass` to `main` first.
2. Items 1+2 together (equations — fixes overflow and likely the "$$" symptom).
3. Item 3 (figures) — including the oracle→benchmark legend rename.
4. Item 4 (arXiv template).
5. Item 5 (restructure) last, after Marcus answers the split/numbering question.

## State at handoff
- Branch `prose-readability-pass` @ `675323a` (committed, check_plan green, **unmerged**).
- Preview PDF is local-only (untracked): `manuscript/preview-jasa/mi-spectral-preview.pdf`.
- Helper scripts used this session are in the session scratchpad (readability measure,
  token verifier, equation scanner) — re-creatable, not committed.
