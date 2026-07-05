# Sweep batch 2 proposal: S2 Background (D-26 register, for Marcus's gate)

**Date: 2026-07-05. GATE DOCUMENT — nothing applied to level3 until Marcus approves.**
Same protocol as batch 1 (`8057b4f`). S2 graded best of the body sections in Phase B
(the definitional entries, warning paragraphs, and strand structure all conform), so this
batch is mostly surgical: one full rewrite from the ratified Demo 3, one opener fix, six
one-phrase repairs, five NO CHANGE.

## Batch summary

| unit | action |
|---|---|
| S2-P1 | opener fix ("The reader needs five things." folded into the contract sentence) |
| S2-P2 | NO CHANGE (definitional entry conforms) |
| S2-P3 | NO CHANGE (ignorability; already subordinated) |
| S2-P4 | one verb ("corrupts" → "invalidates") |
| S2-P5 | three repairs (retired "The reasoning is direct." formula folded; "carry the weight" metaphor out; "drives" → "underlies" with a merge) |
| S2-P6 | one verb phrase ("must be marked at once" → "should be noted at once") |
| S2-P7 | ratified Demo 3 + authorized R11 rescopes #3 and #4; the demo's em-dash becomes a semicolon (D-26 kept the em-dash ban) |
| S2-P8 | NO CHANGE (Rubin's exact identities — E1 "exact" keeps per the addendum) |
| S2-P9 | NO CHANGE (congeniality) |
| S2-P10 | one join ("That estimate is too optimistic. It needs a correction..." → one sentence) |
| S2-P11 | NO CHANGE (Wilks) |
| S2-P12 | one verb ("lodges" → "lies") |
| S2-P13 | one noun ("launch point" → "starting point") |

---

## S2-P1 — opener fix

Replace only the first two sentences:

> This section fixes the paper's notation and assembles the results the derivations use.
> The reader needs five things.

with

> This section fixes the paper's notation and assembles, in five items, the results the
> derivations use.

(The First/.../Fifth enumeration and everything after it are untouched.)

---

## S2-P4 — one verb

> Conflating them corrupts every trace formula in this paper.

becomes

> Conflating them invalidates every trace formula in this paper.

("corrupts" was flagged as more dramatic than the register; the warning's content — the
DM-vs-RIV normalization trap — is untouched, and the paragraph's short closer "The
notation keeps them apart." stays as the emphasis sentence.)

---

## S2-P5 — three repairs

### Current (the affected sentences)

> The object whose bias this paper derives is a Q-function. So its definition and one
> geometric fact about it are needed. [...] The reasoning is direct. We do not know
> $\log f(\mathbf{x}\mid\phi)$, so we maximize instead its current expectation given the
> data $\mathbf{y}$ and the current fit $\phi^{(p)}$. Two facts from their analysis carry
> the weight later. [...] This single geometric fact drives the likelihood-ratio result.
> Constrained fits of the averaged log-likelihood project in the $I_{\text{com}}$ metric.

### Proposed

> The object whose bias this paper derives is a Q-function, so its definition and one
> geometric fact about it are needed. [...] The reasoning is direct: we do not know
> $\log f(\mathbf{x}\mid\phi)$, so we maximize instead its current expectation given the
> data $\mathbf{y}$ and the current fit $\phi^{(p)}$. Two facts from their analysis recur
> throughout what follows. [...] This single geometric fact underlies the
> likelihood-ratio result, because constrained fits of the averaged log-likelihood
> project in the $I_{\text{com}}$ metric.

("carry the weight" is inside the banned metaphor family even under the narrowed C5;
"The reasoning is direct." as a bare sentence is the retired R10 formula, folded into a
colon sentence; "drives" de-metaphorized with the mechanism attached by "because".
Everything between the quoted spans — the definition display, the decomposition, the
$H$-term sentence — is untouched.)

---

## S2-P6 — one verb phrase

> One feature of this construction must be marked at once.

becomes

> One feature of this construction should be noted at once.

---

## S2-P7 — ratified Demo 3 + authorized R11 rescopes #3 and #4

Demo 3's proposed text with three deltas, all pre-authorized in D-26: "quantifies that
contribution exactly" → "quantifies that contribution to leading order" (rescope #3);
"differ by precisely the posterior-draw contribution" → "differ, to leading order, by
the posterior-draw contribution" (rescope #4); the demo's display em-dash becomes a
semicolon (the demo itself flagged this contingency; D-26 kept the em-dash ban). Full
proposed text:

> **Proper imputation.** The imputations this paper studies are proper in Rubin's sense,
> and whether imputation is proper or improper changes the bias the theorem derives.
> Proper imputation propagates parameter uncertainty: a parameter value is first drawn
> from its posterior given the observed data, and the missing values are then drawn from
> the predictive distribution at that drawn value; Chapter 4 of
> @rubinMultipleImputationNonresponse1987 states the validity conditions and gives the
> fully normal Bayesian scheme as the canonical example. Improper imputation, by
> contrast, skips the first draw and imputes at a fixed parameter value; the Monte Carlo
> E-step of the previous paragraph is improper by construction, as is the entire
> deterministic-EM line of work in which the earlier missing-data criteria were derived
> [@cavanaughAkaikeInformationCriterion1998a; @shimodairaInformationCriterionModel2017].
> The distinction is more than a matter of bookkeeping, because the extra posterior draw
> contributes its own variation to the averaged log-likelihood, and the main theorem
> quantifies that contribution to leading order: in the known-scale case the bias is
> zero under improper imputation at the observed-data estimate but
> $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ under proper imputation, so the two forms
> differ, to leading order, by the posterior-draw contribution. Nor is properness
> absolute. @nielsenProperImproperMultiple2003 shows that Bayesian imputations are
> proper when the analyst's complete-data estimator is the maximum likelihood estimator,
> yet the same imputations can fail to be proper for a different estimator; this paper's
> analyst always uses the complete-data MLE, which is the case where congeniality
> implies properness [@nielsenProperImproperMultiple2003]. The extension of the bias
> accounting from the improper, deterministic Q-function to proper multiple imputation
> is one of the things this paper adds.

Invariance: as certified in Demo 3 (all four citation attachment points, the
0 vs $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ contrast, Nielsen's estimator-dependence,
the closing modesty) plus the two authorized claim-strength rescopes. Semicolons: 3 (at
the v3 cap).

---

## S2-P10 — one join

> That estimate is too optimistic. It needs a correction for the downward bias from
> replacing $\theta$ with its estimate $\hat\theta$, and that correction is simply to add
> the parameter count $k$.

becomes

> That estimate is too optimistic, and the needed correction for the downward bias from
> replacing $\theta$ with its estimate $\hat\theta$ is simply to add the parameter count
> $k$.

---

## S2-P12 — one verb

> The bivariate Gaussian example they give shows where the difference lodges, because
> under MAR dropout the unconditional information acquires mean-covariance cross terms
> that the naive form misses.

becomes

> The bivariate Gaussian example they give shows where the difference lies, because under
> MAR dropout the unconditional information acquires mean-covariance cross terms that the
> naive form misses.

---

## S2-P13 — one noun

> Three strands of prior work meet the applications directly, and each is restated here
> as the launch point it provides.

becomes

> Three strands of prior work meet the applications directly, and each is restated here
> as the starting point it provides.

---

## NO CHANGE justifications

- **S2-P2** (notation): the definitional entry matches the register
  (`kenwardLikelihoodBasedFrequentist1998:67`, `mengMultipleImputationInferencesUncongenial1994a:84`).
- **S2-P3** (ignorability): already subordinated; the two-senses discussion conforms.
- **S2-P8** (Rubin's rules): its four "exact" instances are all E1 (Result 3.2 identities)
  per the adopted addendum — they stay.
- **S2-P9** (congeniality), **S2-P11** (Wilks): conformant; texture deferred to the
  closing read.

## Gate

Approve / amend per unit. On approval: atomic script → check_plan → rebuild → render →
scouts. No vocabulary-gate movement expected from this batch (S2 carries no Bucket-2
warnings).
