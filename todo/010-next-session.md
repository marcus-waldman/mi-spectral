# Todo 010 — Next-session handoff: closed-form general-MVN `(A)+(C)` (2026-06-01)

**Resume entrypoint.** Supersedes the in-session update in `todo/009`. Read this, then
`todo/008` (the Term-A MAR record) and the `derivation.qmd` §sec-termA lemma for full detail.
The next move (your plan) is the **closed-form general-MVN `(A)+(C)` asymptote**. First thing to do:
**enter plan mode** — this file is the context for that plan.

---

## State (what is DONE + committed this session — commit `2c02bdf` on `main`, not pushed)

- **Shimodaira positioning settled (Phase 1 gate → Branch A).** The net `tr(RIV)` IC penalty is
  **precedented = Shimodaira–Maeda (2017) `AIC_{x;y}`** (cite, don't claim); AICcd/PDIO carry the
  over-penalized `2·tr(RIV)`; Claeskens–Consentino (adjusted-likelihood target) and Hens–Aerts
  (CC + IPW route, penalty `2K`, *flags imputation-based IC as open*) are adjacent, **none carries
  `(A)+(C)`**. Full verdict table: `todo/003` "Phase-1 novelty gate" section.
- **`derivation.qmd` truth-repaired + Phase-3a structure written (Phase 2 + 3a), renders clean.**
  Theorem now `E[T] = ½tr(RIV) + [(A)+(C)] + O(n⁻¹)` — MCAR-exact, MAR-`O(1)`. The false
  "`(A)+(C)=O(n⁻¹)` for any regular family" lemma is **retracted** (true only under MCAR).
- **Phase-4 reproducible evidence committed.** New `run_all.R` **phase 8** module
  `_modules/term-a-mar-correction.R` (+ `aggregate.R` `TERMA` verdict wiring); R=40k evidence cache
  `verification/cache/run_all-terma/phase8-terma-mar/`.
- **Acquired + lit-synced + cited**: Wang–Robins (1998), Nielsen (2003), Hens–Aerts–Molenberghs
  (2006). `todo/003` lifecycle + `todo/009` updated.

## The verified result the closed form builds on (all checked this session)

The exact Term-A integrand (verified **line-by-line** against `barQ_fiml_analytic`; it IS the
Rao-Blackwellized `A_rb`):
$$ A = \sum_{i:\,M_i\neq\varnothing}\tfrac12\big[(m_{0,i}-m_{\hat\theta,i})^\top S_{\hat\theta,i}^{-1}(m_{0,i}-m_{\hat\theta,i}) + \operatorname{tr}(S_{\hat\theta,i}^{-1}S_{0,i}) - |M_i|\big] $$
($m_{\theta,i},S_{\theta,i}$ = MVN conditional mean/cov of the missing block given observed, under
$\theta$). Taylor in $\delta=\hat\theta_{\text{obs}}-\theta_0$:
$$ (A)+(C) = \alpha^\top \mathbb{E}[\delta] + \tfrac12\operatorname{tr}(\mathcal H\,I_{\text{obs}}^{-1}) - \operatorname{tr}(\mathrm{RIV}),\quad \alpha=\nabla_\theta A|_{\theta_0},\ \mathcal H=\nabla^2_\theta A|_{\theta_0}. $$
**Key enabling facts (numerically verified):**
- `α` is **covariance-only** (`∂_θ S_i=0` for means; `max|α_μ|≈2e-12`, `term-a-mar-general.R`).
- **`tr Cov(g,δ)=+0.002` ⇒ negligible** (`term-a-mar-cov-check.R`): the decomposition is a **clean
  product of 4 pieces — no cross-covariance terms.** This is the enabler: closing `(A)+(C)` = closing
  4 ingredients, 3 of them mechanical.
- Per-rep 2nd-order Taylor reproduces `E[A_rb]` within MCSE (machinery validated).
- **Bivariate-monotone closed form** (validated, S1): `(A)+(C)=(n_mis/n_obs)[1−½tr(Q_mis Q_obs⁻¹)]`, `=0` iff MCAR.
- **`(A)/(C)` split** at n=800 non-mono: `(A)=+0.49`, `(C)=−0.82`.
- **Empirical asymptote (phase-8, R=40k, the manuscript number)**: `(A)+(C)` grows MORE negative
  with n — non-mono `−0.34(n=800)→−0.46(n=1500)`, mono `−0.18→−0.27` — asymptote `≲−0.46`
  (≈−0.5 non-mono, ≈−0.3 mono), up to ≈10% of ½tr(RIV).

## THE TASK to plan: closed-form general-MVN `(A)+(C)` asymptote

`(A)+(C)_∞ = α_u^⊤ b + ½tr(𝓗_u I_u⁻¹) − tr(RIV)`, all N-independent per-unit. Three ingredients are
**mechanical** (matrix calculus, owned lit): `α` (entropy gradient, cov-only), `𝓗` (curvature),
`I_obs` (`observed_info_obs_mvn`, have it). **The crux is the one hard ingredient:** `b = lim n·𝔼[δ]`
= the **second-order FIML MLE bias of `Σ̂` under MAR** (only the Σ-block matters, since α is cov-only).

- **Monotone (tractable, recommended first):** monotone MVN FIML *factors into a sequence of
  complete-data regressions* (Little–Rubin §7.4.2). Each step has the classical
  regression-variance MLE bias (the `−2v/n_obs` that gave the bivariate `n_mis/n_obs`). So
  monotone-general `(A)+(C)` should close as a **sum of per-step design-imbalance terms** — the clean
  generalization of the validated bivariate. Covers the S2-monotone pattern.
- **Non-monotone (hard, open frontier):** no regression factorization → needs the full Cox–Snell /
  Cordeiro–Klein second-order MLE bias. May not close cleanly.

**Why the cheap shortcut failed (do NOT repeat):** `term-a-mar-asymptote.R` (FLAGGED EXPLORATORY/
FLAWED in its header) gave `−0.18` — WRONG (phase-8 says ≲−0.46, growing). The factored form is fine
at a *single* N (cov-check confirms), but it mis-combined `α` at N_ref=8000 with `b` at N_bias=1000
under a `bias∝1/N` assumption that doesn't hold. **A correct *value* (not symbolic) is cheaply
obtainable** by computing the factored `(A)+(C)` at several *consistent* N and extrapolating the
sequence (cheaper than phase-8; cross-checks the closed form).

## LITERATURE — status + the "don't reinvent the wheel" searches to run

**Already searched/acquired/read (contribution-novelty is reasonably gated):**
- IC-under-missingness predecessors all read in-session: Shimodaira–Maeda 2017, Shimodaira 2000,
  Cavanaugh–Shumway 1998, Claeskens–Consentino 2008, Hens–Aerts 2006, Kenward–Molenberghs 1998.
  **None carries the `(A)+(C)` design-imbalance term.** Consensus search (2026-05-31, saved
  `literature/consensus-searches/AIC_bias_correction_multiple_imputation_MAR_2026-05-31.md`) found no
  direct predecessor. So the *contribution* (an `(A)+(C)` IC correction) is novel.
- **Acquired but NOT yet read in-session** (must read before `@cite`ing): **Wang–Robins (1998)**
  `wangLargesampleTheoryParametric1998`, **Nielsen (2003)** `nielsenProperImproperMultiple2003` —
  these are for the **proper-MI layer (Phase 3b)**, not the closed form. Read when 3b starts.

**NOT yet searched — DO THIS BEFORE DERIVING THE BIAS (the explicit "don't reinvent the wheel" ask):**
The closed form's crux — the **second-order/closed-form MLE bias of MVN (μ,Σ) under monotone /
general missing data** — is a *classical statistics* problem that very likely has established results
to **reuse, not re-derive**. Before hand-deriving `b_Σ`:
1. **Search the MVN-missing MLE-bias literature.** Suggested queries (litrev
   `semantic_scholar_search` / `pubmed_search` / `mcp__consensus__search`, and `ask_papers`/
   `search_papers` over the MI-IC RAG db): "bias maximum likelihood multivariate normal monotone
   missing data", "second-order bias FIML covariance estimator", "small-sample bias monotone missing
   data MLE", "Cox-Snell bias missing data". The per-step regression-variance bias is classical
   normal theory (likely in **Anderson 2003** [owned] / **Little–Rubin** [owned] directly).
2. **Confirm/locate the bias-formula references** already flagged in `todo/003`: **Cox–Snell (1968)**
   "A General Definition of Residuals" (general 2nd-order MLE bias) and **Cordeiro–Klein (1994)**
   (matrix form) — `todo/003` has Cox–Snell as *conditional* ("acquire only if we generalize beyond
   monotone"). We are now at that fork. Decide whether to acquire.
3. **Owned and likely sufficient for monotone**: Little–Rubin §7.4.2 (monotone factored likelihood),
   Anderson 2003 (MVN MLE moments + bias), Magnus 2019 (matrix/`vech` calculus). Check these FIRST.

**Tools available** (litrev MCP loaded): `semantic_scholar_search`, `pubmed_search`, `convert_pdf`,
`ask_papers`/`search_papers` (RAG over MI-IC db), `migrate_zotero_attachments`, `mcp__consensus__search`.
Acquisition pipeline is **user-driven**: migrate → Mathpix convert → `py scripts/lit_sync.py` → read.
DOIs verified this session for the 3 new refs (see `todo/003`).

## Open decisions for the plan
1. **Monotone-first vs full-general?** (lean: monotone-general closed form now — high-confidence win.)
2. **Is the *empirical* non-monotone asymptote (≈−0.5) acceptable for the manuscript**, with the
   closed form scoped to monotone? (matches the "keep scope MVN" lineage; lean: yes.)
3. **Acquire Cox–Snell/Cordeiro–Klein now**, or only if a reviewer demands the non-monotone constant?
4. **Verification**: Sympy symbolic check of the derived closed form + numeric match to phase-8
   (the project's discipline). The consistent-N extrapolation harness is the value cross-check.

## Other open threads (don't lose these)
- **Phase 4.2 (not done):** add the proper-MI `A_prop − A_fiml → 0` verdict from existing phase-6
  (`w1-information-diagnostic.R` already records both) to `aggregate.R`.
- **Phase 5 (user-gated):** (a) mi-spectral manuscript rebuild — needs user outline; recover deleted
  `mi-spectral.qmd` via `git show 4da1e0c:manuscript/mi-spectral.qmd`. (b) **MI-IC coordination**:
  add `@shimodairaInformationCriterionModel2017` + reattribute `tr(RIV)` (it cites only Shimodaira
  1994); **port the `(A)+(C)` finding into MI-IC before its Study 1 runs** (Study 1 plans to validate
  "bias=½tr(RIV) under MAR" → will hit `(A)+(C)`). MI-IC already uses correct 1×`tr(RIV)`.
- **derivation-audit WARNs to clear** (ran clean, 0 BLOCKER): `derivation.qmd:1135` stale
  `verification/W1-sweep.R` pointer (→ `_modules/w1-sweep.R`); `lst-mc-trriv` has no `assert`;
  `@littleStatisticalAnalysisMissing2019`/`@rubinInferenceMissingData1976b`/
  `@andersonIntroductionMultivariateStatistical2003` cited but untracked in `todo/003` lifecycle.
- **`.claude/skills/derivation-audit/` is UNTRACKED** (user built it; commit it if wanted).
- **Open issue #1** (W3 IC SB-arm), auxiliary, headline-unaffected (`todo/000`).

## Key files / reproduction
- Derivation: `manuscript/derivation.qmd` (§sec-termA lemma = the `(A)+(C)` content; renders via
  `quarto render manuscript/derivation.qmd`).
- Reproducible evidence: `verification/run_all.R` phase 8 (`Rscript verification/run_all.R 40000 terma "8" 28`).
- Sound diagnostics (keep): `verification/term-a-mar-general.R` (Taylor machinery + α_μ=0),
  `term-a-mar-cov-check.R` (Cov(g,δ)≈0). **FLAWED/exploratory (ignore as evidence):**
  `term-a-mar-asymptote.R` (mis-extrapolates; header flagged).
- R is NOT on the Bash-tool PATH: use `"/c/Program Files/R/R-4.5.1/bin/Rscript.exe"`. `py`, `quarto`,
  `git` are on PATH. Avoid `cmd | tail` (masks exit codes) and `/usr/bin/time` (absent in Git-bash).
- Plan file from this session: `~/.claude/plans/jaunty-squishing-breeze.md` (the 5-phase plan).
- Memory: `project_shimodaira_positioning.md` (the positioning verdict).
