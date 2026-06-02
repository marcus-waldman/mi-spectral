# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Open issues:** [#1](https://github.com/marcus-waldman/mi-spectral/issues/1) — W3 (IC) SB arm applies the scaled-shift to the uncorrected deviance; intended to wrap the bias correction. Auxiliary arm only; headline results unaffected. See `todo/000-current-status.md`.

## Scope

**JAIGP theory paper.** A deviance-bias correction for the Q-function under congenial multiple imputation, with applications to likelihood-ratio model comparison and information-criterion-based model selection. **Reframed 2026-05-22** after reading Chan (2022, *Annals of Statistics*): the original "spectral chi-square correction" framing was preempted; the paper now sits upstream of Chan's test calibration as the deviance-numerator bias correction. See `IDEAS.md` (Reframing note + archive section) for the full provenance, including the 2026-05-23 comprehensive-sweep empirical landings.

## Out of scope

**Redirect to `~/git-repositories/MI-IC`:**
- SEM specifics: lavaan, CFI/TLI/RMSEA, saturated SEM imputation, `miicsem` package.
- Congeniality / PMM empirics (separate applied note, not this paper).
- Empirical SEM simulations (Bollen et al. design, Type I tables, etc.).
- Model fit indices in SEM.

**Archived — do not draft from these:**
- Spectral chi-square correction / scaled-shifted form / generalized eigendecomposition of RIV_⊥ — preempted by Chan (2022, AoS). Cite Chan as the canonical reference for non-EFMI test calibration.
- Le Cam-style power-dominance theorem — demoted to a Discussion conjecture; W2 provides partial empirical support.

**Other out-of-scope:** FIML / EM-based observed-data MLE inference (Cavanaugh-Shumway universe — adjacent, not competing); semiparametric / Wald-only variants; Bayes-factor analogues; non-regular settings (boundary, label-switching mixtures).

If the work drifts into any of the above, push it back to MI-IC or cite Chan (2022) and move on.

## Authorship model

AI-assisted derivation, target venue JAIGP (Journal for AI Generated Papers). Provenance is transparent per JAIGP norms. ORCID-verified human prompter: marcus.waldman.

## Core contribution

**Theorem.** Under congenial proper MI with the complete-data MLE as the target, the Q-function deviance bias decomposes as
$$\text{Bias}[\bar Q_\infty(\hat\theta_{\text{obs}})] = +\text{tr}(\text{RIV}) - \tfrac{1}{2}\text{tr}(\text{RIV}) = +\tfrac{1}{2}\text{tr}(\text{RIV}),$$
where the $+\text{tr}$ term is imputation bias and the $-\tfrac{1}{2}\text{tr}$ term is estimation mismatch (MI's target is $\hat\theta_{\text{com}}$, not $\hat\theta_{\text{obs}}$). Holds for any regular likelihood model fit on congenially imputed data **that estimates a scale or covariance** (so the conditional missing-data entropy depends on the estimated parameters; MVN with estimated Σ throughout) — a known-scale, location-only fit collapses to 0 (FIML) / $-\tfrac12\text{tr(RIV)}$ (proper MI). Under MAR there is an additional $O(1)$ design-imbalance term $(A)+(C)$ (0 under MCAR; sign + order firm, absolute value not independently pinned).

**Two applications:**

1. **Likelihood-ratio model comparison (§4).** The LRT numerator $\hat d_L = 2[\bar Q_\infty(\hat\psi^*) - \bar Q_\infty(\hat\psi_0^*)]$ inherits a differential bias $\text{tr}(\text{RIV}(\hat\psi^*)) - \text{tr}(\text{RIV}(\hat\psi_0^*))$. Vanishes at $H_0$; non-zero under local alternatives and non-nested model comparison. Distorts power and ranking even when the reference distribution (Chan 2022 AoS) is correctly calibrated.

2. **Information criteria (§5, headline empirical claim).** MI-AIC and MI-BIC consume $-2\bar Q_\infty$; the bias $-\text{tr}(\text{RIV})$ is **model-specific** (different candidate models have different RIVs). Uncorrected MI-AIC/BIC systematically favor models with **larger** RIV — the downward bias of $-2\bar Q_\infty$ scales with $\text{tr}(\text{RIV})$, making high-RIV candidates look artificially better than they would under complete data. Bias correction restores complete-data-equivalent model selection (same direction as Cavanaugh-Shumway's AICcd, which penalizes high-RIV models with $+2\text{tr}(\text{RIV})$ on top of $2q$).

**Witness apparatus (W1/W2/W3).** Each application is paired with a pre-registered numerical witness (`todo/004-simulation-hypotheses.md`). Predictions written before simulations; framing modifies if reality differs. Extended robustness via the comprehensive sweep (`todo/005`, `todo/006`).

## Lineage

Rubin (1987) → Cavanaugh–Shumway (1998, AICcd for EM-based observed-data MLE — *parallel universe, different target*) → Meng (1994, congeniality) → Meng–Rubin (1992) → Claeskens-Consentino (2008, missing covariates) → Chan–Meng (2022, *Stat Sinica*; stacked-data LRT + EFMI) → Chan (2022, *Annals of Statistics*; SMI, drops EFMI, full eigenvalue spectrum, MC reference distribution — **canonical reference for MI test calibration**) → **this work (deviance-bias correction, upstream of all test-calibration work)**.

Chan & Meng (2022) and Chan (2022) handle the reference distribution; we handle the bias of the numerator being referred to it. Both are necessary for complete-data inferential recovery under MI.

## Repo layout

Three-layer reproducibility: `IDEAS.md` is *what we found and what it means*; `verification/run_all.R` is *how to reproduce it*; per-phase `.rds` caches and summary CSVs are *the raw evidence*.

```
manuscript/
  mi-spectral.qmd                        # Quarto stub for the JAIGP submission (in progress)
  derivation.qmd                         # canonical sourced derivation (notation, ledger, tagged proof);
                                         #   Appendix B = executable Sympy/NumPy verification (jupyter: python3)
  proof-verification-fixture.json        # W1 replicate + cache read by derivation.qmd Appendix B (committed)

verification/
  run_all.R                              # SINGLE ENTRYPOINT for the comprehensive sweep
  _modules/                              # phase functions sourced by run_all.R:
                                         #   smoke-tests.R, w1-sweep.R, w3-sweep.R,
                                         #   w3-rate.R, mnar-bias.R, aggregate.R
  _legacy/                               # retired standalone sweep scripts (see _legacy/README.md
                                         # for the old-file -> module mapping). Do NOT re-execute.
  00-setup.R                             # shared primitives (MVN gen, MI engines, lavaan wrappers,
                                         #   apply_missingness_ampute, mle_chol_sigma12 w/ par_init,
                                         #   chan_smi_test_k1, analytic Fisher info / tr(RIV))
  00-test-primitives.R                   # smoke tests for 00-setup primitives
  W1-bias-decomposition.R                # ORIGINAL preregistered W1 (frozen at SHA ddc9037)
  W2-lrt-power.R                         # ORIGINAL preregistered W2
  W2-size-adjusted-power.R               # W2 post-hoc size-adjusted analysis
  W3-model-selection.R                   # ORIGINAL preregistered W3
  W1-sympy-fixture.R                     # JSON fixture writer for the Sympy notebook (todo/007)
  cache/run_all-prod/phase{0..5}/        # canonical centralized-sweep outputs (RDS + summary CSV)
  cache/W{1,3}-{pilot,prod}-*.rds        # preregistered W1/W2/W3 outputs

literature/
  <citekey>.md                           # CITATION-PROTECTED corpus — hook enforces existence + read
  mi-spectral-better-bibTeX.bib          # BBT export from Zotero; source of truth for citekeys

todo/
  000-current-status.md                  # resume entrypoint
  001-literature-and-hooks.md            # citation infrastructure (closed)
  003-references-to-acquire.md           # living reference-proposal backlog
  004-simulation-hypotheses.md           # preregistered W1/W2/W3 (frozen at SHA ddc9037)
  005-comprehensive-sweep-hypotheses.md  # preregistered comprehensive sweep
  006-comprehensive-sweep-execution.md   # closed (executed)
  007-sympy-proof-verification.md        # open side artifact (Sympy verification spec)

.claude/
  hooks/check_citations.py               # PreToolUse hook: blocks @<citekey> writes if
                                         #   literature/<citekey>.md absent. Bypass via @TODO:<slug>.
  skills/lit-sync/                       # /lit-sync slash command (BBT -> literature/ bridge)

scripts/
  lit_sync.py                            # Zotero BBT -> literature/<citekey>.md sync (see skill)
```

**Module organization for `verification/run_all.R`.** Five phases, each in its own module under `_modules/`:

| Phase | Module | What it does |
|---|---|---|
| 0 | smoke-tests.R | ampute-vs-apply_mar parity check + pre-flight tr(RIV) table (gates the rest) |
| 1 | w1-sweep.R | 18 FIML cells (2 patterns × 3 mechs × 3 N), analytic Q-function + analytic tr(RIV) |
| 2 | w3-sweep.R | 60 cells (2 patterns × 2 mechs × 3 N × 5 engine/M/cong slots), MI-AIC selection |
| 3 | w3-rate.R | H3b rate side experiment (low-rate arm only; rate=60% deferred for Amelia stability) |
| 4 | mnar-bias.R | Direct E[θ_obs − θ_truth] measurement under MAR / MNAR / MNAR_targeted |
| 5 | aggregate.R | Combine summaries, evaluate H1/H2-MAR/H2-MNAR/H3/H3b/H4/H5/H6 against pass criteria |

Originals (`W1-bias-decomposition.R`, `W2-lrt-power.R`, `W3-model-selection.R`) are the preregistered scripts cited at SHA ddc9037 and **not** routed through `run_all.R`. Touch them only for the preregistered cell or with an explicit preregistration amendment.

## Commands

R is at `C:\Program Files\R\R-4.5.1\bin\Rscript.exe`. The 20-core PSOCK cluster is the default parallelism on this Windows host.

**Reproduce the full comprehensive sweep** (~3 hours on 20 cores, all 5 phases):
```
Rscript verification/run_all.R 2000 prod all 20
```

**Fast smoke run** of run_all.R (R=100, ~10 minutes, all phases):
```
Rscript verification/run_all.R 100 smoke all 20
```

**Run individual phases** (comma-separated):
```
Rscript verification/run_all.R <R> <out_suffix> "1,4,5" <n_cores>
```
Outputs land in `verification/cache/run_all-<out_suffix>/phase{0..5}/`.

**Preregistered W1/W2/W3 originals** (todo/004; only for reproducing the SHA ddc9037 results, not for new analysis):
```
Rscript verification/W1-bias-decomposition.R <mode> <engine> [n_cores] [N_override]
Rscript verification/W2-lrt-power.R <mode> <engine> [n_cores]
Rscript verification/W3-model-selection.R <mode> <engine> [n_cores]
```
`mode` is `pilot` or `prod`; `engine` is `fiml` or `amelia`.

**Render the manuscript / proof verification:**
```
quarto render manuscript/mi-spectral.qmd
quarto render manuscript/derivation.qmd   # executes Appendix B (needs sympy, numpy, the fixture json)
```

**Sync the literature corpus** (Zotero BBT export → `literature/<citekey>.md`):
```
py scripts/lit_sync.py
```
Or invoke `/lit-sync` as a slash command.

**Smoke-test the primitives** (independent of the sweep):
```
Rscript verification/00-test-primitives.R
```

## Related repos

- `~/git-repositories/MI-IC` — companion SEM methodology paper; v4.5 derivation, `miicsem` package, and SEM simulations live there. JAIGP paper is cited from there.

## Citation discipline (load-bearing)

**Any citation in `manuscript/` must reference a paper whose markdown copy exists at `literature/<citekey>.md` AND has been read in the current session.** Reliance on training-weight knowledge of cited papers is prohibited. The acquisition workflow and enforcement hook are specified in `todo/001-literature-and-hooks.md`. The `PreToolUse` hook at `.claude/hooks/check_citations.py` blocks Edit/Write/MultiEdit on `manuscript/` files when an unbacked `@<citekey>` appears.

**Bypass**: `@TODO:<slug>` is allowed as a drafting placeholder (the hook explicitly skips these).

Rationale: AI-assisted derivations fail in review when citations are hallucinated. The only defense is acquiring actual PDFs and reading them locally before claiming what they say.

If asked to cite something and `literature/<citekey>.md` does not exist, stop and run the acquisition workflow first.

## Proposing references in conversation

Naming papers in conversation that aren't yet in `literature/` is allowed for planning purposes, **but every such proposal must be logged in `todo/003-references-to-acquire.md` in the same response.** Otherwise proposals leak silently and we end up drafting around references that were never actually acquired.

For each proposed paper, record: (a) approximate citation, (b) the claim it would support, (c) where in the manuscript it would land, (d) priority. Promotion from `proposed → queued → acquired → verified → cited` is tracked in that file. Only `verified` references (markdown read in-session, claim checked against text) are eligible for `@cite` in `manuscript/`.

## R style

Inherit `~/.claude/CLAUDE.md` global instructions if computation is added.
