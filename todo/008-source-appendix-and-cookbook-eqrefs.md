# Todo 008 — Verbatim-source appendix + Matrix Cookbook equation numbers

**Purpose.** Two enhancements to `manuscript/derivation.qmd`'s provenance apparatus,
for a future session. The derivation (notation + ledger + tagged proof) is complete;
provenance currently lives in the right margin as: citekey + the source's own
equation/theorem number (where known) + the `literature/<citekey>.md` line number +
a short verbatim snippet. These two tasks deepen that.

**Resume context.** Read `manuscript/derivation.qmd` (the three stages and their margin
`::: {.column-margin}` provenance blocks) and skim the `literature/<citekey>.md` files
(Mathpix conversions — the verbatim source text lives here).

---

## Task 1 — Verbatim-source appendix, organized by reference

**Goal.** Add an appendix to `derivation.qmd` that reproduces, *grouped by reference*,
the verbatim source passages the derivation relies on. Each citation/margin then links
to the relevant appendix subsection, so a reviewer can read the actual source text
without leaving the document.

**Spec.**
- New appendix section, one subsection per reference, e.g. `### Schafer (1997) {#sec-src-schafer}`,
  `### Magnus & Neudecker (2019) {#sec-src-magnus}`, etc.
- Under each: the full citation, then the verbatim quoted passages we cite — each with
  the source's own equation/theorem number **and** the `literature/<citekey>.md` line
  number. Pull the text from the `literature/<citekey>.md` Mathpix conversions.
- Cross-link from the body: each margin provenance entry links to its appendix
  subsection. The citation hook now whitelists Quarto crossref prefixes (commit
  `5bc7e6b`), so `{#sec-src-<key>}` labels + `@sec-src-<key>` references work.
- Once the verbatim text lives in the appendix, consider **trimming the margin blocks**
  to just (equation/theorem number + appendix link), since the full quote is then one
  click away — keeps the margin light while the appendix carries the audit detail.
- References to cover (all already in `literature/`): `schafer…1997`, `magnus…2019`,
  `vaart…1998a`, `mengMultipleImputationInferencesUncongenial1994a`,
  `rubinMultipleImputationNonresponse1987`, `rubinInferenceMissingData1976b`,
  `littleStatisticalAnalysisMissing2019`, `andersonIntroductionMultivariateStatistical2003`,
  `petersen2008matrix`.

**Consideration (flag, don't block).** Verbatim reproduction of source text is fine for
this working/audit document. For the JAIGP submission, keep quotes to short
equation/definition excerpts (fair use); if a reviewer or the venue objects, trim to
equation numbers + line refs and drop the verbatim block.

---

## Task 2 — Matrix Cookbook (Petersen & Pedersen) equation numbers

**Goal.** The Cookbook numbers its equations (e.g. the vec rule is "Eq 520"). Our
A1–A4 citations currently give a section (§1.1, §10.2.2) + `md:line` but **not** the
book's equation number. Add it.

**Spec.** Look up the Cookbook's own equation numbers in `literature/petersen2008matrix.md`
for each cited identity and add them to the A1–A4 ledger citations (and the appendix):
- **A1** trace linearity `Tr(A+B)=Tr A+Tr B` (§1.1, `:183`)
- **A2** trace cyclicity `Tr(AB)=Tr(BA)`, `Tr(ABC)=Tr(BCA)` (§1.1, `:182`/`:184`)
- **A3** `tr(I_k)=k` from `Tr(A)=Σ_i A_ii` (§1.1, `:179`)
- **A4** `vec(AXB)=(Bᵀ⊗A)vec X`; `Tr(AᵀB)=vec(A)ᵀvec(B)` (§10.2.2, `:3345`/`:3346`)

The §1.1 trace list may be a numbered block — record each identity's number. (Magnus
already cites eq (23); Schafer/Rubin/Meng/Anderson cite their own equation numbers;
this gap is specific to Petersen.)

---

## Done-when

- Appendix renders, organized by reference, each entry carrying verbatim text +
  source equation/theorem number + `md:line`.
- Every margin provenance block links to its appendix subsection; links resolve.
- A1–A4 citations carry the Cookbook's equation numbers.
- `quarto render` clean; `@`-citations and `@sec-`/`@eq-` crossrefs all resolve.

## Notes

- `@sec-`/`@eq-`/`@fig-`/`@tbl-` crossrefs work since the hook whitelist (`5bc7e6b`).
- The verbatim text's source of truth is `literature/<citekey>.md`; `lit-sync`
  re-pagination shifts line numbers, so keep the verbatim snippet as the stable anchor
  (a future `check_provenance.py` could re-locate snippets and self-heal the line refs —
  see the deferred idea from the proof-verification session).
