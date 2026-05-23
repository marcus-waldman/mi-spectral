# Todo 003 — Reference acquisition backlog

**Status:** Living document. New entries added whenever a paper is proposed during planning but not yet acquired.

## Why this exists

The PreToolUse citation hook prevents `@<citekey>` tokens from landing in `manuscript/` without a backing `literature/<citekey>.md`. That catches violations *at the edit*. But during planning/conversation Claude (or the human) often **proposes** papers by name from training knowledge — citations of intent, not yet citations of record. Without tracking, these proposals leak silently: by the time we draft a section, the question "did we ever acquire that?" gets lost.

This file is the running list of proposals through to either acquisition (paper enters Zotero → lit-sync → eligible for `@cite`) or rejection (we don't actually need it).

## Lifecycle

```
proposed ──► queued ──► acquired ──► verified ──► cited
              │
              └──► rejected (we decided we don't need it)
```

- **proposed** — first mentioned in conversation. Probably from Claude's training-weight knowledge. **Not yet citeable.**
- **queued** — confirmed we want to acquire. Added to Zotero `mi-spectral` collection (possibly as a stub `_needs-pdf` entry).
- **acquired** — PDF in `Google Drive/Literature/MI-SPECTRAL/`, Mathpix-converted, `literature/<citekey>.md` exists.
- **verified** — read in-session, the claim attributed to it has been checked against the actual text. **Eligible for citation per CLAUDE.md.**
- **cited** — actually appears as `@<citekey>` in `manuscript/`.
- **rejected** — examined and decided unnecessary; remove from active queue.

## Discipline

- Whenever Claude proposes a paper by name in conversation (e.g., "as in Ledoit-Wolf shrinkage"), **add a row to this table within the same session**, even if it's just `[proposed]` with a partial citation. Otherwise the proposal evaporates.
- The conversation entry should record: (a) what claim it was meant to support, (b) approximately where in the manuscript it would land, (c) whether it's a "must have" or "nice to have" for the paper.
- Promote `proposed → queued` only when a human (the user, not Claude) confirms acquisition.
- Once acquired, follow the normal acquisition pipeline (Zotero → migrate → index_papers → lit-sync). Then mark `acquired`.

## Active queue

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| Ledoit, O. & Wolf, M. — shrinkage estimation of covariance matrices | **rejected (subsumed by Lam 2019)** | — | — | — | Initially proposed 2026-05-22 from my training-weight knowledge. After Consensus search (2026-05-22, saved at `~/Google Drive/Literature/MI-SPECTRAL/_notes/consensus-regularized-covariance-2026-05-22.md`), decided Lam (2019) review is the single canonical citation. |
| Marchenko, V. A. & Pastur, L. A. (1967) | **rejected (subsumed by Lam 2019)** | — | — | — | Same — generic-phrasing decision plus Lam (2019) covers MP-based methods. |
| **Lam, C. (2019).** "High-dimensional covariance matrix estimation." *Wiley Interdisciplinary Reviews: Computational Statistics* 12. DOI: 10.1002/wics.1485 | acquired | **Single future-work citation** for the small-$M$ / $M \leq k$ regime. WIREs review covers all the families (structural, shrinkage, rotation-invariant, Bayesian/robust). | Discussion (§10) future-work paragraph | Medium | In `literature/lamHighdimensionalCovarianceMatrix2020.md`; in RAG. Treated as future-reference pointer only — no deep read needed. |
| **Chan, K. W. (2021).** "General and feasible tests with multiply-imputed datasets." *Annals of Statistics* (date as listed in Chan-Meng 2022 references; volume TBD — may have been published post-2022). | **proposed — URGENT** | **Potentially closest predecessor to mi-spectral.** Chan-Meng (2022) explicitly cite this paper as "a possible remedy" for the EFMI-violation regime, which is precisely mi-spectral's target. **Must read before finalizing §1 contribution claims** — may reshape what we claim as novel, or in the worst case fully preempt our contribution. | §1 Introduction (lineage), C1–C4 framing, §7 Related Work | **High — read carefully** | Discovered 2026-05-22 in §2.3 of Chan-Meng (2022). Search hint: title is "General and feasible tests with multiply-imputed datasets" by Kwun Chuen Gary Chan, *Annals of Statistics*. Listed as "to appear" in 2022 references — actual publication may be late 2022 or 2023. Try Annals of Statistics archive or arXiv. |
| **Satterthwaite, F. E. (1946).** "An Approximate Distribution of Estimates of Variance Components." *Biometrics Bulletin* 2(6), 110–114. DOI: 10.2307/3002019 | queued (in Zotero, 2026-05-22) | **HIGH — anchor for moment-matching variance approximation.** Our scaled-shifted form $a\chi^2 + b$ is the two-moment Satterthwaite generalization. | §6 and §7 (introducing the correction); reviewers will demand this cite. | High | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| **Imhof, J. P. (1961).** "Computing the Distribution of Quadratic Forms in Normal Variables." *Biometrika* 48(3–4), 419–426. DOI: 10.1093/biomet/48.3-4.419 | queued (in Zotero, 2026-05-22) | Exact distribution of $\sum_j \lambda_j Z_j^2$ (generalized chi-squared) that our scaled-shifted approximates | §6 (defining the target distribution); V5/V6 witnesses for exact-vs-approximation comparison | Medium | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| **Davies, R. B. (1980).** "Algorithm AS 155: The Distribution of a Linear Combination of χ² Random Variables." *Applied Statistics* 29(3), 323–333. DOI: 10.2307/2346911 | queued (in Zotero, 2026-05-22) | Computational algorithm for generalized chi-squared distribution (Imhof alternative) | §6 if we discuss computational details of the exact reference distribution | Medium | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| `claeskensconsentinoVariableSelectionIncomplete2008` | acquired (literature/) | Anchor citation for the block-diagonal decomposition of RIV under $(β, α)$ when $X$ has missingness | Discussion (§10), one sentence on the missing-covariates extension | Medium | Zotero key U3F5HN8W (also in MI-IC); markdown synced; in MI-SPECTRAL RAG. Not yet read in-session. |
| `consentinoclaeskensOrderSelectionTests2010` | **verified (cold-read 2026-05-22)** | Adjacent prior MI-testing work — omnibus order-selection lack-of-fit testing. **NOT a competitor for our headline.** They use Meng-Rubin's scalar-r F-reference as-is; no EFMI/anisotropy treatment; "order" in their sense ≠ our spectral order. | §7 Related Work, one sentence | Medium | Zotero key 9U4662KK; markdown synced; in RAG. Cited in body as adjacent literature; doesn't preempt any C1–C3 claim. |

## Recently rejected (kept as a record so we don't re-propose)

- **2026-05-22 — Wood, A. T. A. (1989).** "An F approximation to the distribution of a linear combination of chi-squared variables." *Comm. Stat. — Simul. Comp.* 18(4), 1439–1456. DOI: `10.1080/03610918908812585`. Reason: We're sticking with χ² reference (not F), so the F-approximation is not load-bearing. Citation lineage for the scaled-shifted moment-matching form is already covered by Satterthwaite (1946) + Satorra-Bentler (2010) + Asparouhov-Muthén (2006). Imhof (1961) + Davies (1980) cover the exact reference distribution. Full text was also not freely available, which would have been a small acquisition cost — combined with non-load-bearing status → reject. Re-propose only if we change framing to F-reference.
- **2026-05-22 — Ledoit & Wolf (specific paper TBD)** and **Marchenko & Pastur (1967).** Reason: Subsumed by Lam (2019) review which covers the same ground in one citation. See proposed entry above.

## Recently promoted to `literature/` (kept as a record)

- **2026-05-22:** `claeskensconsentinoVariableSelectionIncomplete2008` and `consentinoclaeskensOrderSelectionTests2010` — both acquired via Zotero/migrate/index/lit-sync. The 2010 paper has been read cold and `verified` (synthesis in conversation 2026-05-22; reads as adjacent, not competing).
- *(Phase 1 corpus from `todo/001` already in `literature/` since session opening.)*

---

*Last updated: 2026-05-22*
