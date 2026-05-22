# Todo 001 — Literature acquisition and citation-discipline hooks

**Status:** Open. Blocks any citation in `manuscript/`.

**Why first.** AI-assisted derivations are vulnerable to citation hallucination: a paper that says "Smith (2019) shows X" when Smith (2019) doesn't show X. The only defense is to (a) acquire actual PDFs, (b) convert to markdown stored locally in the repo, and (c) require that any citation in the manuscript be backed by a markdown copy that has actually been read in-session. The hooks below operationalize (c).

---

## Phase 1 — Identify the citation corpus

Initial list (from `IDEAS.md` and the manuscript stub). Add to as drafting reveals more.

| Citekey (proposed) | Citation | Status | Notes |
|---|---|---|---|
| `rubin1987multiple` | Rubin, D. B. (1987). *Multiple Imputation for Nonresponse in Surveys.* Wiley. | Needed | Foundational. RIV and MI variance pooling. |
| `mengrubin1992` | Meng, X.-L. & Rubin, D. B. (1992). Performing likelihood ratio tests with multiply-imputed data sets. *Biometrika* 79(1), 103–111. | Needed | D_1, D_2, D_3 statistics. |
| `meng1994uncongenial` | Meng, X.-L. (1994). Multiple-imputation inferences with uncongenial sources of input. *Statistical Science* 9(4), 538–558. | Needed | Defines congeniality. |
| `chanmeng2022` | Chan, K. W. & Meng, X.-L. (2022). Multiple improvements of multiple imputation likelihood ratio tests. *Statistica Sinica* 32(3), 1489–1514. | Partially read — already fetched as PDF during conversation. Needs Zotero + markdown. | Direct comparator; stacked-data LRT + EFMI. |
| `xiemeng2017` | Xie, X. & Meng, X.-L. (2017). Dissecting multiple imputation from a multi-phase inference perspective: What happens when god's, imputer's, and analyst's models are uncongenial? *Statistica Sinica* 27, 1485–1545. | Needed | Cited extensively by Chan-Meng. |
| `cavanaughshumway2001` | Cavanaugh & Shumway — AICcd reference. Exact citation TBD. | Needed | The +2·tr(RIV) AIC under MI. Verify exact paper title and venue. |
| `aspmuthen-scaledchisq` | Asparouhov & Muthén — scaled-and-shifted chi-square. Specific reference TBD. | Needed | The Mplus/lavaan robust correction form we adapt. Verify which paper introduces the scaled-shifted form (likely a 2010-era Mplus technical note). |
| `vandervaart1998asymptotic` | van der Vaart, A. W. (1998). *Asymptotic Statistics.* Cambridge University Press. | Needed | For Le Cam's third lemma and contiguity. |
| `schafer1997analysis` | Schafer, J. L. (1997). *Analysis of Incomplete Multivariate Data.* Chapman & Hall. | Needed | NORM / joint MVN MI; relevant for the full-MVN worked example. |
| `magnusneudecker` | Magnus & Neudecker. *Matrix Differential Calculus.* | Needed | Duplication matrix machinery for the MVN covariance-block information matrix. |

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

## Open questions for the user

1. **Zotero collection:** new `mi-spectral` collection, or share with MI-IC? (Several references overlap; MI-IC's collection may already have them.)
2. **Citekey convention:** the proposed convention is `firstauthorYEARkeyword` (e.g., `chanmeng2022`). Match MI-IC's existing convention if different.
3. **PDF → markdown conversion:** `mcp__litrev__convert_pdf` if available, else pandoc CLI. Confirm preferred pipeline.
4. **Hook strictness:** block on missing literature file, or warn-only? Recommend blocking with `@TODO:` escape hatch.
