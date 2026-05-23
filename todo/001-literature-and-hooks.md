# Todo 001 — Literature acquisition and citation-discipline hooks

**Status:** Open. Blocks any citation in `manuscript/`.

**Why first.** AI-assisted derivations are vulnerable to citation hallucination: a paper that says "Smith (2019) shows X" when Smith (2019) doesn't show X. The only defense is to (a) acquire actual PDFs, (b) convert to markdown stored locally in the repo, and (c) require that any citation in the manuscript be backed by a markdown copy that has actually been read in-session. The hooks below operationalize (c).

---

## Phase 1 — Identify the citation corpus

**Citekey convention (locked 2026-05-22):** Better BibTeX `firstauthor[+coauthors]ShortTitleYEAR` — e.g., `chanmengMultipleImprovementsMultiple2022`. Matches the convention used in MI-IC's `manuscript/references.bib`.

Initial list (from `IDEAS.md` and the manuscript stub). Add to as drafting reveals more.

| Citekey | Citation | Zotero | PDF | Markdown | Notes |
|---|---|---|---|---|---|
| `rubinMultipleImputationNonresponse1987` | Rubin, D. B. (1987). *Multiple Imputation for Nonresponse in Surveys.* Wiley. | ✓ `AHC9H39Z` (not in `mi-spectral` collection) | needed | needed | Foundational. RIV and MI variance pooling. Book — chapter-scoped acquisition. |
| `mengrubinPerformingLikelihoodRatio1992` | Meng, X.-L. & Rubin, D. B. (1992). Performing likelihood ratio tests with multiply-imputed data sets. *Biometrika* 79(1), 103–111. | needed | ✓ on disk | ✓ `literature/mengrubinPerformingLikelihoodRatio1992.md` (Mathpix, 30KB) | D_1, D_2, D_3 statistics. JSTOR 2337151. |
| `mengMultipleImputationInferences1994` | Meng, X.-L. (1994). Multiple-imputation inferences with uncongenial sources of input. *Statistical Science* 9(4), 538–573. | ✓ `S46WGHG3` (not in `mi-spectral`) | ✓ on disk | ✓ `literature/mengMultipleImputationInferences1994.md` (Mathpix, 117KB) | Defines congeniality. Corrected page range to 538–573. |
| `chanmengMultipleImprovementsMultiple2022` | Chan, K. W. & Meng, X.-L. (2022). Multiple improvements of multiple imputation likelihood ratio tests. *Statistica Sinica* 32(3), 1489–1514. | needed | not located on disk (todo claim of "partially fetched" not verified) | needed | Direct comparator; stacked-data LRT + EFMI. **Acquisition open question** — see Open Items section. |
| `xiemengDissectingMultipleImputation2017` | Xie, X. & Meng, X.-L. (2017). Dissecting multiple imputation from a multi-phase inference perspective: What happens when god's, imputer's, and analyst's models are uncongenial? *Statistica Sinica* 27, 1485–1545. | needed | needed | needed | Cited extensively by Chan-Meng. **Acquisition open question** — see Open Items section. |
| `cavanaughshumwayAkaikeInformationCriterion1998` | Cavanaugh, J. E. & Shumway, R. H. (1998). An Akaike information criterion for model selection in the presence of incomplete data. *Journal of Statistical Planning and Inference* 67, 45–65. | needed | ✓ on disk | ✓ `literature/cavanaughshumwayAkaikeInformationCriterion1998.md` (Mathpix, 74KB) | The +2·tr(RIV) AIC under MI. PII S0378-3758(97)00115-8. **Note:** IDEAS.md cites this as "Cavanaugh–Shumway (2001)" — the correct year is 1998. Update IDEAS.md after user confirms there is no separate 2001 paper. |
| `asparouhovmuthen-TBD` | Asparouhov & Muthén — scaled-and-shifted chi-square. Specific reference TBD. | needed | needed | needed | The Mplus/lavaan robust correction form we adapt. Likely Asparouhov & Muthén (2010) Mplus technical note. |
| `vandervaartAsymptoticStatistics1998` | van der Vaart, A. W. (1998). *Asymptotic Statistics.* Cambridge University Press. | needed | needed | needed | For Le Cam's third lemma and contiguity. Book — chapter-scoped acquisition. |
| `schaferAnalysisIncompleteMultivariate1997` | Schafer, J. L. (1997). *Analysis of Incomplete Multivariate Data.* Chapman & Hall. | ✓ `6HXQQM6A` (duplicate `KRTM8QBZ` — clean up) | needed | needed | NORM / joint MVN MI; relevant for the full-MVN worked example. Book — chapter-scoped. |
| `magnusneudeckerMatrixDifferentialCalculus-TBD` | Magnus & Neudecker. *Matrix Differential Calculus.* (edition/year to confirm) | needed | needed | needed | Duplication matrix machinery for the MVN covariance-block information matrix. Book — chapter-scoped. |

**TBD as drafting progresses:** Hotelling T² references; classical MVN test references (Anderson textbook?); possibly Reiter/Raghunathan for MI test alternatives; possibly Wilks (1938) for the LR test classical result.

---

## Phase 2 — Acquisition workflow per paper

For each citekey in the table:

1. **Zotero.** Add to the `mi-spectral` Zotero collection (or whichever collection the user designates; see below). Generate citation key matching the table above (Better BibTeX setting).
2. **PDF.** Attach the PDF to the Zotero entry. For paywalled papers, use institutional access.
3. **Convert to markdown.** Use `mcp__litrev__convert_pdf` (or pandoc) to produce `literature/<citekey>.md`. Preserve section structure; OCR if needed.
4. **Mark "read & verified".** Once the markdown is opened in-session and the relevant claims have been checked, update the table status to "Verified — claim Y on p.Z" with a specific page/equation reference.

**Output:** one markdown file per citekey at `literature/<citekey>.md`. Filename matches the citekey used in the manuscript.

---

## Phase 3 — Hook to enforce non-hallucination

**Goal.** When Claude proposes an edit to anything in `manuscript/` that introduces a citation `@<citekey>`, a PreToolUse hook checks whether `literature/<citekey>.md` exists. If it doesn't, the hook blocks (or strongly warns) with: *"Cite @<citekey> requires literature/<citekey>.md to exist. Run the literature acquisition workflow for this reference before citing."*

**Design.**

- **Hook type:** PreToolUse on Edit and Write.
- **Trigger condition:** target file path starts with `manuscript/` AND the new content contains `@<citekey>` patterns (Pandoc citation syntax).
- **Action:** For each unique citekey extracted from the diff, check `literature/<citekey>.md`. If any are missing, exit non-zero with a clear message.
- **Implementation:** PowerShell script at `.claude/hooks/check-citations.ps1`, wired up in `.claude/settings.json` under `hooks.PreToolUse`.
- **Bypass:** for legitimate cases (e.g., draft pseudocitations), a `@TODO:` prefix on the citekey skips the check.

**Settings file inclusion.** `.claude/settings.json` and `.claude/hooks/` should be committed (so the hook fires for all collaborators on this repo). `.claude/settings.local.json` stays gitignored. Adjust `.gitignore` accordingly when implementing.

**Status: not yet implemented.** Spec written here; build in Phase 3 work.

---

## Phase 4 — Discipline reinforcement

- `CLAUDE.md` carries a strong directive: *"Any citation in `manuscript/` must reference a paper whose markdown copy exists at `literature/<citekey>.md` AND has been read in the current session. Reliance on training-weight knowledge of cited papers is prohibited."*
- A memory feedback entry codifies the same rule across sessions.

---

## Decisions (locked 2026-05-22)

1. **Zotero collection:** new `mi-spectral` collection. Overlapping references (Rubin '87, Meng '94, Schafer '97) live in the Zotero library but are not assigned to MI-IC — they'll be added to `mi-spectral` directly. Schafer 1997 has a duplicate to clean up (`6HXQQM6A` vs `KRTM8QBZ`).
2. **Citekey convention:** Better BibTeX `firstauthor[+coauthors]ShortTitleYEAR`, matching MI-IC's `manuscript/references.bib`. Example: `chanmengMultipleImprovementsMultiple2022`. The table above has been rewritten in this form. Three citekeys remain `-TBD` because the exact paper/edition needs confirming first (Cavanaugh-Shumway, Asparouhov-Muthen, Magnus-Neudecker).
3. **PDF → markdown:** `mcp__litrev__convert_pdf` (Mathpix-backed; the only mode the tool exposes). Pandoc as last-resort fallback for anything Mathpix can't handle.
4. **Hook strictness:** block edits to `manuscript/` introducing an unverified `@<citekey>`, with `@TODO:<slug>` as the bypass for legitimate drafting placeholders.

## Open items requiring user input

(Surfaced 2026-05-22 while executing Phase 1; need answers before remaining acquisition can proceed.)

1. **Cavanaugh-Shumway year discrepancy.** IDEAS.md lineage line says "Cavanaugh–Shumway (2001, predictive AIC, target = θ̂_obs)". The PDF on disk (verified) is the 1998 JSPI paper. Is there a separate 2001 paper, or is "2001" a typo in IDEAS.md and the 1998 paper is the one?
2. **Chan–Meng 2022 PDF location.** Filesystem scan found no Chan–Meng PDF. Earlier note in the todo said it was "partially fetched in prior session." Do you have it locally somewhere I missed, should I pull from Statistica Sinica (http://www3.stat.sinica.edu.tw/statistica/), or via Semantic Scholar/Google Scholar?
3. **Asparouhov–Muthén scaled-shifted reference.** Specific paper unclear. Likely candidates: (a) Asparouhov & Muthén (2010) "Computationally Efficient Estimation of Multilevel High-Dimensional Latent Variable Models" — wrong topic; (b) Asparouhov & Muthén (2010) Mplus Web Notes #4/#10; (c) Satorra & Bentler (1988/2010) for the *original* scaled chi-square. Which paper do you intend to cite for the scaled-shifted form?
4. **Xie–Meng 2017 acquisition path.** Pull from Statistica Sinica direct, or do you have institutional access I should use?
5. **Magnus–Neudecker edition.** First edition (1988 Wiley), revised second (1999), or third (2007/2019)?
6. **Books strategy reconfirm.** I provisionally locked "chapter-scoped PDFs only" — for each book, which chapters/sections do you have in mind? Tentative scope:
   - Rubin (1987): Chapters 3 (combining rules, RIV) and 4 (multivariate)
   - Schafer (1997): Chapter 5 (multivariate normal model, joint imputation)
   - van der Vaart (1998): Chapter 6 (contiguity) and §7.2 (Le Cam's third lemma)
   - Magnus–Neudecker: chapters covering duplication matrix and matrix differentials

## Books — scope discipline

Four books in the corpus (Rubin '87, Schafer '97, van der Vaart '98, Magnus-Neudecker). Full Mathpix conversion of a 400+ page book is expensive and wasteful. Acquisition strategy: **chapter-scoped PDFs only** — extract just the chapters/sections actually cited (e.g., Rubin '87 §3.3 on RIV; van der Vaart §6 on Le Cam's third lemma; Magnus-Neudecker chapters on duplication matrix). One `literature/<citekey>.md` per book, containing only the relevant chapters concatenated.
