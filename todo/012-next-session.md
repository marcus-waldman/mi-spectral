# Todo 012 — Next session: lit-sync the monotone refs → swap prose to `@cite`, then promote + Phase 3b (2026-06-01)

**Resume entrypoint.** Supersedes `todo/011` (read it for the full closed-form record). The Phase-3a
closed-form general-MVN `(A)+(C)` for **monotone MAR** is **DERIVED, fully analytic, verified, and in
the manuscript** — committed on `main` (`914bbf0`, `b938d17`). `derivation.qmd` renders clean.
Headline: `(A)+(C)_∞ = α⊤b_Σ + ½tr(H_φφ I_obs⁻¹) ≈ −0.22` (4-var monotone), MCAR control → 0.

The ONLY thing that was blocked on the literature is turning two **prose** citations in `§sec-termA`
into formal `@cite`s. A parallel session is acquiring + indexing the refs; **assume the PDFs are in
Zotero/Drive and Mathpix-indexed, but `literature/<citekey>.md` does NOT exist yet → lit-sync must be
run.**

---

## STEP 1 (do first) — lit-sync, read+verify, then swap prose → `@cite`

### 1a. Run lit-sync (BBT → `literature/<citekey>.md`)
- **Prereq check:** `literature/mi-spectral-better-bibTeX.bib` must contain the new entries (the BBT
  export must have been refreshed in the acquiring session). If the new papers aren't in that `.bib`,
  lit-sync can't create their markdown — ask the user to re-export BBT first.
- Invoke **`/lit-sync`** (slash command / Skill) — or `py scripts/lit_sync.py`. It parses the BBT
  `.bib`, finds each PDF in the MI-SPECTRAL Drive folder by author/year, looks up the cached Mathpix
  conversion by SHA256, and writes `literature/<citekey>.md`. Idempotent.
- After it runs, list the new files: `git status --short literature/` (new `*.md`), or
  `Glob literature/{hyodo,kanda}*.md`.

### 1b. Identify the citekeys + READ them in-session (citation discipline is load-bearing)
The exact citekeys come from the BBT export (convention `firstauthorShortTitleYEAR`); expected:
- **Hyodo, Shutoh, Seo & Pavlenko (2016)**, "Estimation of the large covariance matrix with two-step
  monotone missing data," *Comm. Stat. — Theory & Methods* — likely `hyodoEstimation…2016`.
- **Kanda & Fujikoshi (1998)**, "Some Basic Properties of the MLEs … Monotone Missing Data,"
  *AJMMS* 18(1–2):161–190, DOI 10.1080/01966324.1998.10737458 — likely `kanda…1998`.

**Read each `literature/<citekey>.md` in-session and confirm the claim before `@cite`ing** (the hook
only checks file existence, but CLAUDE.md requires an in-session read + claim check):
- Hyodo: Sec. 2 should carry the explicit **2-step monotone MLE** of every Σ-block (Anderson–Olkin
  form) **and** an **exactly-unbiased estimator (Lemma 2.1)** with explicit divisors. (NB: the paper's
  headline is *shrinkage*; the MLE/unbiased pair is the Sec-2 background — confirm the Mathpix
  conversion actually includes it. The openly-readable TR13-05 had it; the published version should too.)
- Kanda–Fujikoshi: the **exact bias of Σ̂** for k=2,3-step monotone (on Σ̂ directly).
- If one of them converts thin / lacks the passage, cite the other (either supports the claim) and/or
  adjust the prose; don't `@cite` a paper whose backing passage you can't see.

### 1c. Swap the prose → `@cite` in `manuscript/derivation.qmd` (`§sec-termA`)
Find this exact string (the monotone-`b_Σ` provenance) and replace the parenthetical:
> `missingness is classical (Hyodo, Shutoh, Seo & Pavlenko 2016; Kanda & Fujikoshi 1998 — pending`
> `acquisition, `todo/003`); this recursion is its $n\to\infty$ coefficient for the FIML estimator.)`

→ replace `(Hyodo … 1998 — pending acquisition, `todo/003`)` with
`[@<hyodo-citekey>; @<kanda-citekey>]`.

**Only if** Cox–Snell (1968) + Cordeiro–Klein (1994) were ALSO synced (they're the *non-monotone*
branch, lower priority), likewise swap the other parenthetical:
> `(Cox–Snell / Cordeiro–Klein) machinery (Cox & Snell 1968; Cordeiro & Klein 1994 — pending`
> `acquisition, `todo/003`);`
→ `[@<coxsnell-citekey>; @<cordeiroklein-citekey>]`. Otherwise leave that prose as-is.

### 1d. Verify + record
- `quarto render manuscript/derivation.qmd` → must stay clean (the citation hook now passes because
  `literature/<citekey>.md` exists; pandoc resolves the keys from the BBT `.bib`).
- Update `todo/003` lifecycle rows for these refs: `proposed → cited` (the 2026-06-01 `b_Σ` section).
- Commit (on `main`, matching repo convention; end message with the Co-Authored-By line).

---

## STEP 2 — promote the closed form into the reproducible sweep (NOT lit-gated; can do anytime)
`verification/term-a-mar-closedform.R` is currently a standalone (fully-analytic, ~1 min) script.
Project discipline wants it as a `run_all.R` phase module so `(A)+(C)_∞ ≈ −0.22` + MCAR→0 are
committed evidence (RDS + `summary.csv` + an `aggregate.R` verdict), like W1/W3 and phase 8.
- New module e.g. `verification/_modules/term-a-closedform.R` (or extend phase 8); follow the
  `run_<name>(R_per_cell, cl, out_dir)` pattern, seed `20260522 + r`, write to
  `cache/run_all-<suffix>/phaseN-…/`; wire a verdict into `_modules/aggregate.R`.
- Optional **Appendix-B inline check** in `derivation.qmd` mirroring `@lst-mc-crossterm`: a render-time
  Sympy/NumPy cell verifying the **bivariate reduction** `(A)+(C)=n_mis/n_obs − ½tr(M_mis M_obs⁻¹)`
  (the 2-step case) and **MCAR → 0**.

## STEP 3 — Phase 3b: proper-MI generalization (has its own small lit step)
Extend the result from the EM/plug-in `barQ_∞` to **congenial proper (posterior-draw) MI**: show both
`½tr(RIV)` and the `(A)+(C)` term carry over (Rubin's rules, finite-M, impute-once/select-many).
- Prereq reads (already acquired, NOT yet read in-session per `todo/010`): **Wang & Robins (1998)**
  `wangLargesampleTheoryParametric1998`, **Nielsen (2003)** `nielsenProperImproperMultiple2003`. If
  their `literature/*.md` exist, read them; if not, lit-sync them too.
- Empirical support already exists: phase-6 (`w1-information-diagnostic.R`) records `A_prop` (Amelia)
  vs `A_fiml` (plug-in). Phase 4.2 = fold an `A_prop − A_fiml → 0` verdict into `aggregate.R`.

## STEP 4 — Phase 5 (user-gated): manuscript + cross-repo
- mi-spectral **manuscript** rebuild (the JAIGP paper proper, not just `derivation.qmd`) — needs the
  user's outline; recover the deleted scaffold via `git show 4da1e0c:manuscript/mi-spectral.qmd`.
- **MI-IC coordination:** port the `(A)+(C)` finding + add `@shimodairaInformationCriterionModel2017`
  (reattribute `tr(RIV)`, currently Shimodaira-1994-only) **before** MI-IC's Study 1 runs (it expects
  bias = ½tr(RIV) under MAR and will hit `(A)+(C)`).

## Non-monotone (optional, later) — the empirical −0.46 branch
Closed form open; needs Cox–Snell/Cordeiro–Klein on the FIML observed-data (pattern-mixed) likelihood,
with Patriota–Lemonte (2008) as the complete-data MVN template. Currently reported empirically
(phase-8 ≈ −0.46). Triage the S2 lead `96e04824…` ("Expectations and Variances of MLEs of the MVN
Parameters with Missing Data") first — if it gives a general closed form, this collapses to reuse.

## Key files / commands / gotchas
- Closed form: `manuscript/derivation.qmd` `§sec-termA` (α, b_Σ recursion, H_φφ all explicit).
- Artifact (fully analytic): `verification/term-a-mar-closedform.R` (`Rscript … 2000 600 20`, ~1 min).
- Validation scratch (committed): `scratch-alpha-analytic.R` (α), `scratch-hphi-analytic.R` (H_φφ),
  `scratch-AC-pathb.R` ((C) coupled/decoupled), `scratch-bsigma-*.R` (b_Σ), `scratch-AC-highR.R`
  (measured curve). `scratch-AC-asymptote.R`/`-predict.R` superseded by the analytic artifact.
- R not on Bash PATH: `"/c/Program Files/R/R-4.5.1/bin/Rscript.exe"`. Quarto/git/py on PATH.
- parLapply closures must `clusterExport` loop vars; inline `Rscript -e` + PSOCK cluster segfaults —
  use a script file.
- Citation hook (`.claude/hooks/check_citations.py`) blocks `@<citekey>` in `manuscript/` unless
  `literature/<citekey>.md` exists; `@TODO:slug` bypasses. So STEP 1a (lit-sync) must precede 1c.
- Plan of record: `~/.claude/plans/toasty-launching-hummingbird.md`.
