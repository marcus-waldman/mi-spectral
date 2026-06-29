# mi-spectral

**Model selection after multiple imputation: a deviance correction for AIC, BIC, and likelihood-ratio tests.**

A deviance-bias correction for the Q-function (the imputation-averaged complete-data
log-likelihood) under congenial multiple imputation, with two applications:
likelihood-ratio model comparison and information-criterion model selection. A
human-prompted AI theory paper targeting [JAIGP](https://jaigp.org), with a stated and
auditable verification protocol.

**📄 Read the sourced derivation:** <https://marcus-waldman.github.io/mi-spectral/derivation.html>
&nbsp;·&nbsp; **Project page:** <https://marcus-waldman.github.io/mi-spectral/>

---

## What the paper shows

Multiple imputation lets you apply complete-data tools to each completed data set and
combine the results. Many of those tools — likelihood-ratio statistics, information
criteria, deviance-based fit indices — are built on the averaged complete-data
log-likelihood across imputations, and that averaged log-likelihood is biased: evaluated
at the observed-data estimate and measured against the complete-data benchmark, it
overstates the fit.

For a model that estimates a scale or covariance, under congenial proper multiple
imputation with the complete-data maximum likelihood estimate as the target, the bias is

```
Bias = +tr(RIV)  −  ½ tr(RIV)  =  +½ tr(RIV)
```

a positive imputation-bias term and a negative estimation-mismatch term that do not
cancel. RIV is the relative-increase-in-variance matrix, and under missing-at-random data
there is an additional `O(1)` design-imbalance term that is zero under MCAR. The bias is
**specific to each candidate model** and grows with that model's missing information, so a
model-comparison table built on imputed data favors the candidates with the most missing
information — which, in the nested model families studied here, are the more complex models.

### Contributions

Stated for use, in the order an applied reader is likely to need them:

1. **A correction for model selection after imputation.** Comparing models by AIC or BIC on
   imputed data is biased; the bias is specific to each candidate and grows with that
   candidate's missing information, so the uncorrected criteria favor the candidates with
   the most missing information. Adding one term per candidate — the trace of its RIV
   matrix — removes the trace component of the bias and substantially restores the ranking
   complete data would have given.
2. **The deviance bias behind the correction.** For a model that estimates a scale or
   covariance, the averaged log-likelihood overstates its complete-data counterpart by
   ½ tr(RIV), plus a design-imbalance term that appears only under missing-at-random data
   and vanishes under MCAR. The proof for proper imputation and the design-imbalance term
   are new; the trace itself matches a penalty already known from a related prediction
   problem.
3. **The bias of a likelihood-ratio comparison.** For two nested models compared at the
   null, the relevant bias is the missing information carried by the tested directions
   alone, measured in the complete-data metric — not the difference of the two models'
   separate corrections, which always overstates it. A correctly calibrated reference
   distribution (Chan 2022, *Annals of Statistics*) already absorbs this null mean, so the
   correction must not be added on top of such a test.
4. **A sharper way to run that comparison.** Fitting the competing models to the same
   imputed data sets, rather than to separate ones, cancels most of the shared noise and
   tightens the comparison.
5. **An auditable human-prompted AI workflow.** The way the derivations were produced is a
   contribution in its own right: transparent provenance and checks the reader can run —
   citations verified against their sources, independent symbolic verification, preregistered
   simulations whose failures are reported, adversarial re-derivation (which caught a sign
   error in this work), and full reproducibility.

Each load-bearing claim is paired with a preregistered numerical check and, where
derivable, an independent symbolic (computer-algebra) check.

## Authorship and provenance

A human-prompted AI derivation prepared under [JAIGP](https://jaigp.org) norms: ORCID-verified
human prompting and transparent AI co-authorship.

- **Human prompter / corresponding author:** Marcus Waldman
  ([ORCID 0000-0002-3288-4803](https://orcid.org/0000-0002-3288-4803)), Department of
  Biostatistics and Informatics, University of Colorado Anschutz Medical Campus.
- **AI collaboration:** the derivation was developed in dialogue with Claude (Anthropic)
  and cross-checked with GPT-5.5 Pro (OpenAI) and Gemini (Google).

**Session transcripts.** The complete Claude Code session logs that produced this work are
the provenance record:

➡️ **[AI-collaboration session transcripts (redacted, Google Drive)](https://drive.google.com/drive/folders/1WUwqgkYQ0RUfzNt5pLZ8TmBEdYCb2GR7?usp=sharing)**

These are the session logs (`.jsonl`) with personal file paths and credentials redacted. No
external work is quoted in the manuscript; cited claims are checked against locally read
sources.

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

This repository is made publicly readable for transparency of the human-prompted AI
research process. No license to reuse, redistribute, or create derivative works is granted.
