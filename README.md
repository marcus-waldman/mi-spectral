# mi-spectral

**The deviance bias of congenial multiple imputation, with applications to likelihood-ratio comparison and model selection.**

A deviance-bias correction for the Q-function (the imputation-averaged complete-data
log-likelihood) under congenial multiple imputation, with two applications:
likelihood-ratio model comparison and information-criterion model selection. An
AI-assisted theory paper targeting [JAIGP](https://jaigp.org), with a stated and
auditable verification protocol.

**📄 Read the sourced derivation:** <https://marcus-waldman.github.io/mi-spectral/derivation.html>
&nbsp;·&nbsp; **Project page:** <https://marcus-waldman.github.io/mi-spectral/>

---

## What the paper shows

Multiple imputation lets you apply complete-data tools to each completed data set and
combine the results. Many of those tools (likelihood-ratio statistics, information
criteria, deviance-based fit indices) are built on the averaged complete-data
log-likelihood. That averaged log-likelihood is biased: evaluated at the observed-data
estimate and measured against the complete-data benchmark, it overstates the fit.

Under congenial proper multiple imputation with the complete-data maximum likelihood
estimate as the target, the bias decomposes as

```
Bias = +tr(RIV)  −  ½ tr(RIV)  =  +½ tr(RIV)
```

a positive imputation-bias term and a negative estimation-mismatch term that do not
cancel for any model estimating a scale or covariance. (RIV is the relative-increase-in-variance
matrix. Under missing-at-random data there is an additional `O(1)` design-imbalance term
that is zero under MCAR.)

The bias is **specific to each candidate model**, so a model-comparison table built on
imputed data favors the candidates with the most missing information. Two consequences:

- **Model selection.** Uncorrected MI-AIC and MI-BIC systematically favor higher-RIV
  models. Adding one trace term per candidate substantially restores
  complete-data-equivalent selection.
- **Likelihood-ratio comparison.** At the null, the differential bias is the missing
  information of the tested directions alone, projected in the complete-data metric —
  not the naive difference of the two models' trace corrections, which always overstates
  it. This is exactly the value a correctly calibrated reference distribution (Chan 2022,
  *Annals of Statistics*) already absorbs, so the correction must not be applied twice.

Each load-bearing claim is paired with a preregistered numerical check and, where
derivable, an independent symbolic (computer-algebra) check.

## Authorship and provenance

AI-assisted derivation prepared under [JAIGP](https://jaigp.org) norms: ORCID-verified
human prompting and transparent AI co-authorship.

- **Human prompter / corresponding author:** Marcus Waldman, Department of Biostatistics
  and Informatics, University of Colorado Anschutz Medical Campus.
- **AI collaboration:** the derivation was developed in dialogue with Claude (Anthropic)
  and cross-checked with GPT-5.5 Pro (OpenAI) and Gemini (Google).

**Session transcripts.** The complete Claude Code session logs that produced this work are
the provenance record. A redacted copy is being prepared for public release, and the link
will be added here. No external work is quoted in the manuscript; cited claims are checked
against locally read sources.

## Repository layout

```
manuscript/
  derivation.qmd        Canonical sourced derivation (setup, assumptions, proof);
                        executable Sympy/NumPy verification inline. Rendered to
                        docs/derivation.html.
  mi-spectral.qmd       Submission document (working draft).
  plan/                 Leveled manuscript plan (thesis → sections → paragraphs →
                        evidence) and locked decisions.
  figures/             Generated figures for the simulation evidence.

verification/
  run_all.R             Single entry point for the comprehensive simulation sweep.
  _modules/             Phase functions sourced by run_all.R.
  00-setup.R            Shared primitives (data generation, MI engines, analytic
                        Fisher information / tr(RIV)).
  ic-ladder.R           Information-criterion calibration ladder.
  W1/W2/W3-*.R          Preregistered numerical witnesses.

literature/             Per-citation markdown corpus (every manuscript citation is
                        backed by a locally read source).
docs/                   GitHub Pages site (landing page + rendered HTML).
IDEAS.md                Directional anchor: what was found and what it means.
CLAUDE.md               Scope, conventions, and working guidance.
```

## Reproduce

R is required (developed on R 4.5.1). The comprehensive sweep runs on a PSOCK cluster.

```sh
# Full sweep (all phases). The last argument is the core count.
Rscript verification/run_all.R 2000 prod all 20

# Fast smoke run.
Rscript verification/run_all.R 100 smoke all 20

# Information-criterion calibration ladder.
Rscript verification/ic-ladder.R 2000 6 MAIN,WEAK,JUNK
```

Render the documents (requires [Quarto](https://quarto.org); the derivation also needs
Python with `sympy` and `numpy`):

```sh
quarto render manuscript/derivation.qmd     # → manuscript/derivation.html
quarto render manuscript/mi-spectral.qmd
```

## Lineage

Rubin (1987) → Meng (1994, congeniality) → Meng–Rubin (1992) → Chan–Meng (2022,
*Statistica Sinica*) → Chan (2022, *Annals of Statistics*; the canonical reference for
multiple-imputation test calibration) → **this work**. Chan & Meng (2022) and Chan (2022)
handle the reference distribution; this paper handles the bias of the numerator being
referred to it. Both are needed to recover complete-data inferential behavior under
multiple imputation.

## Copyright

© 2026 Marcus Waldman. All rights reserved. See [`COPYRIGHT`](COPYRIGHT).

This repository is made publicly readable for transparency of the AI-assisted research
process. No license to reuse, redistribute, or create derivative works is granted.
