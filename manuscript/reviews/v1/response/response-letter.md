---
title: "Response to Reviewers — v1 Review (Paper 88)"
author: "Marcus Waldman"
date: last-modified
format:
  pdf:
    documentclass: article
    fontsize: 11pt
    geometry: margin=1in
    colorlinks: true
bibliography: ../../../../literature/mi-spectral-better-bibTeX.bib
csl: ../../../_extensions/wjschne/apaquarto/apa.csl
---

We thank the reviewers for their careful reading. Every comment is addressed below,
grouped by reviewer, with the reviewer's text quoted first in each case. Manuscript
changes are identified in place. The verification scripts, computer-algebra checks, and
cross-model review records cited in the responses are committed in the public repository,
so each claim about what was run can be checked against the artifact itself. The review
being answered is archived at `manuscript/reviews/v1/ai-review-paper-88.md` (15 comments
across five reviewer personas).

---

## Reviewer 1, comment 7 (heavy-tail N=1000 remark)

> The authors justify the failure of the N=1000 cell to hit the analytic target by claiming the
> standard deviation of the per-repetition statistic grows with sample size due to heavy tails.
> [...] The authors must either clarify why the variance of this specific statistic scales
> positively with N [...]

This reads the manuscript's wording as saying the Monte Carlo standard *error* of the pooled
mean grows with $N$, which would indeed be invalid if the per-repetition statistic had infinite
variance. That is not the claim. The repetition count is $1{,}000$ at every sample size in this
study ($N=200,500,1000,2000$) — it never changes across cells. What changes is $N$, and what grows
with $N$ is the *per-replicate* statistic's own spread: at a fixed number of repetitions, a
larger-$N$ cell's individual draws are more dispersed, so the resulting standard error is wider,
not because repeated averaging fails to converge, but because there is more to average over in
each cell. The per-replicate variance is finite throughout — "heavy-tailed" describes a slowly
decaying tail relative to a Gaussian, not an infinite-variance pathology — so the standard
asymptotic confidence intervals in Figure 1 remain valid; they are simply wider at $N=1{,}000$
because that cell's underlying statistic is itself more variable, a property the paper already
discloses (G1) rather than papers over.

*Manuscript change landed:* the results paragraph reporting the pooled theorem-validation
estimate now states this explicitly — the repetition count ($1{,}000$) is named as identical
across every sample size, and the per-replicate spread (not the Monte Carlo standard error) is
what grows with $N$, and that spread is finite.

## Reviewer 1, comment 8 (data-augmentation control)

> The manuscript claims to validate the trace correction for proper multiple imputation, but the
> simulations rely exclusively on an approximately Bayesian bootstrap expectation-maximization
> approach rather than exact data augmentation. Because the theoretical derivations for proper MI
> depend on exact posterior draws, the lack of a fully Bayesian Markov chain Monte Carlo (MCMC)
> control experiment undermines the claim that the correction holds for proper MI, especially
> under high missingness. I recommend running the headline simulation studies using a standard
> data augmentation engine to confirm that the analytic results hold without the artifacts of the
> bootstrap approximation.

We ran the requested control. Two independent exact data-augmentation engines were built: a
hand-rolled conjugate Gibbs sampler under the reference prior $p(\mu,\Sigma)\propto|\Sigma|^{-(p+1)/2}$
(`verification/da-conjugate-engine.R`), and, as a cross-check, `norm::da.norm`. Both were run on
the paper's own headline W1 cell (four-variate MVN, $N=200$ non-monotone MAR) to $R=20{,}000$
repetitions, and the conjugate engine was extended across $N\in\{200,500,1000,2000\}$. The two
engines agree to the third decimal ($-0.783$ and $-0.783$, standard errors $.0023$/$.0031$,
normalized by $\operatorname{tr}(\mathrm{RIV})$), which rules out an implementation artifact:
this is a property of the *method*, not of our code.

The control surfaces a genuine, and now fully characterized, engine difference. **The bootstrap
engine this paper validates with (Amelia's EMB) is not undermined by this finding — it is
confirmed.** As $N\to\infty$ its finite-sample gap from the $+\tfrac12\operatorname{tr}(\mathrm{RIV})$
headline shrinks toward zero ($-0.099,-0.047,-0.029,-0.019\cdot\operatorname{tr}(\mathrm{RIV})$
at $N=200,500,1000,2000$, consistent with an $O(1/N)$ finite-sample term), and its $N=200$
shortfall sits inside the same noise band as the paper's already-disclosed design-imbalance term.
A genuine Bayesian posterior draw, by contrast, does *not* converge to the headline as $N$ grows;
it carries a persistent $O(1)$ correction, because a proper posterior draw is over-dispersed
relative to the fitted plug-in by construction (Rubin's between-imputation variance rule exists
to capture that extra spread), and the deviance — a sum of $n$ per-cell $O(1/n)$-sensitive
terms — resolves that over-dispersion into an $O(1)$ effect that a finite-sample argument cannot
make vanish.

We derived this correction in closed form and verified it two ways: symbolically
(`verification/cas-wolfram/verify_engine_gap_sympy.py`, 10/10 checks, including a $p=1$ toy table
that independently reconstructs a withheld grading key) and via an independent cross-model
derivation (GPT-5.5 Pro, blind and red-team passes, xhigh reasoning effort;
`todo/040b-gpt55-gate-package.md`). For a genuine posterior draw the correction to the headline is

$$
D=-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})-\tfrac12\sum_i\operatorname{tr}\!\big(\hat V_i^{-1}C_i\,b_\Sigma\,C_i^\top\big)-\mathrm{IMB}+o(1),
$$

every term of which is computable from quantities the derivation already defines, except a small
design-imbalance term ($\approx-0.006\operatorname{tr}(\mathrm{RIV})$ here, zero under MCAR) that
is disclosed as measured and bounded; a closed form for it is left to future work. Because
$b_\Sigma$ is prior-dependent, the correction's size depends on the prior: a Jeffreys-prior draw
measures $\approx-0.78\cdot\operatorname{tr}(\mathrm{RIV})$ at $N=200$, and a weakly-informative
brms/Stan draw (LKJ + half-$t$ priors, run as an independent check) measures
$\approx-1.36\cdot\operatorname{tr}(\mathrm{RIV})$ — more negative still, confirming the effect
is not a Jeffreys-improper-prior artifact but general to full-Bayes posterior-draw imputation.

**Constructive remedy, for a user who wants to run a genuine Bayesian sampler anyway.**
Recentring the posterior draws at their own measured $b_\Sigma$ — rather than using them as
drawn — collapses the correction from $\approx-0.78\cdot\operatorname{tr}(\mathrm{RIV})$ to
$\approx-0.15\cdot\operatorname{tr}(\mathrm{RIV})$, matching a mean-centered Gaussian draw; the
underlying measurements were independently reconfirmed at higher precision.

**Framing.** This is confirmation-with-characterization, not a retraction. The paper's own
simulations use Amelia's EMB throughout, and that choice is now validated by an asymptotic
argument in addition to the original finite-sample tolerance check. Genuine Bayesian
posterior-draw MI — the construction the reviewer specifically asked us to test — carries a
disclosed, derived, and (for the studied designs) fully computable correction rather than an
open gap. The engine split this exposes (deterministic/MLE-centered imputation vs. genuine
posterior-draw imputation) is not ad hoc: it is the same PDMI-vs-MLMI distinction developed as a
first-class construction in the imputation literature [@vonhippelMaximumLikelihoodMultiple2021],
where posterior-draw MI is independently documented to carry more small-sample bias than
MLE-centered imputation [@vonhippelNewConfidenceIntervals2016] through the same mechanism —
posterior draws add their own sampling variability on top of the MLE's, roughly doubling it.
That the bootstrap engine escapes this correction follows from the classical bootstrap
bias-estimation identity [@efronBootstrapMethodsAnother1979]: bootstrap resampling with an EM
plug-in estimates the sampling bias of $\hat\Sigma_{\text{obs}}$ directly, which is exactly the
complete-data second-moment identity ($\mathbb{E}^\ast[\tilde\Sigma+(\tilde\mu-\hat\mu)^{\otimes2}]
=\hat\Sigma$) that makes Amelia's EMB second-moment-matched.

*Manuscript changes already landed:* `manuscript/derivation.qmd` — a forward-pointer at the
Q-function definition, a corrected fitted-vs-oracle callout, and a new scope-and-correction
callout following the theorem's setup, stating the theorem's scope (second-moment-matched,
regular-draw imputers) and the disclosed correction for engines outside that scope; a
one-sentence addition to the known-scale callout. The repository's decision log (D-22) records
the amendment and its provenance.

## Reviewer 1, comment 9 (nested-confound control)

> In the selection-sweep design, the candidate models are nested, meaning that model complexity
> (parameter count) is perfectly confounded with the amount of missing information. [...] the
> authors should include a control experiment comparing non-nested candidate models that have the
> same number of parameters but differ significantly in their fractions of missing information.

The main selection sweep the reviewer describes (the nested diagonal-to-saturated candidate
family, $\S5$) is indeed confounded in exactly the way described — in that family, complexity and
missing information increase together at every nesting step, so its "100% concentrate on the
saturated model" result establishes the *direction* of the bias, not that missing information
specifically (rather than under-penalized complexity generally) drives it. The manuscript already
scopes that result this way: the selection-sweep results state that the finding "confirms the
predicted direction of the bias rather than discriminating the specific mechanism," because the
nested family makes the saturated candidate the natural destination for any downward-biased
deviance regardless of cause.

The control the reviewer asks for is a separate study already in the paper: the non-nested
measurement of $\S5$. It runs two candidate pairs that are *not* part of the nested family —
diagonal versus first-order autoregressive, and compound-symmetry versus the same autoregressive
truth — and pairs each missing-at-random cell with a missing-completely-at-random
twin that uses the *identical* candidate models and parameter counts but removes the
design-imbalance mechanism the reviewer is asking us to isolate (missing-completely-at-random data
makes that term vanish by construction). Because the candidates and their parameter counts are
held fixed across the two arms and only the missingness mechanism changes, the missing-at-random-
minus-missing-completely-at-random difference isolates what missing information contributes,
separately from whatever a merely under-penalized deviance would do by complexity alone. For the
dissimilar diagonal-versus-autoregressive pair that isolated differential resolves at $-1.2$, three
and a half standard errors from zero and stable across sample sizes — a genuine, measured effect
attributable to missing information under a design where complexity itself never changes between
the two arms being compared. For the more similar compound-symmetry-versus-autoregressive pair,
the same differential fell below Monte Carlo resolution (a pre-registered pilot value of $-2$
dissolved on the full run), which we report as the study's own honest limit rather than a
confirming result (G5 also discloses that a mechanism-independent misspecification term
coexists with the design-imbalance term for dissimilar pairs and can partly offset it in the net
ranking bias).

*No new work needed:* the requested control already exists in the manuscript; this response
points to it rather than proposing new simulations.

## Reviewer 2, comment 4 (+/- dispersion measure undefined)

> Throughout the simulation results, the manuscript uses the "+/-" symbol without defining the
> measure of dispersion in the main text. [...]

Checked the actual computations rather than assuming: the pooled theorem-validation estimate
($2.43\pm0.26$) uses `pooled_se = 1/sqrt(sum(w))`, one Monte Carlo standard error
(`verification/w1-h1-pooled-reconciliation.R`), while every figure's whiskers plot
`est +/- 1.96*se`, a $95$ percent interval (`verification/figures.R`) — two different, unlabeled
conventions in the same document. *Manuscript change landed:* the theorem-validation results
paragraph now states at first use that its $\pm$ is one Monte Carlo standard error and explicitly
distinguishes it from the figure's $95$ percent whiskers.

## Reviewer 2, comment 5 (name all four selection-sweep models)

> The authors define the extremes of the candidate set (diagonal and saturated) but omit the
> definitions of the two intermediate nested models [...]

*Manuscript change landed:* the selection-sweep design paragraph now names all four candidates
from the actual sweep code (`verification/W3-model-selection.R`): the diagonal model (eight free
parameters), a model that frees the wrong off-diagonal pair $\sigma_{12},\sigma_{34}$ (ten free
parameters), a model that frees the correct pair $\sigma_{13},\sigma_{24}$ matching the truth
(ten free parameters, the true model), and the saturated model (fourteen free parameters). While
tracing this down we also found and fixed a separate factual error the reviewer did not flag:
the paragraph described the truth as having "a compound-symmetry structure," which is actually
the truth used in the *different* non-nested study; this sweep's truth sets
$\sigma_{13}=\sigma_{24}=0.4$ with every other off-diagonal entry zero, now stated correctly.

## Reviewer 2, comment 6 (Sigma / correlation placement)

> The manuscript does not specify which of the six possible coordinate pairs [...] are assigned
> the correlations of 0.6, 0.3, and 0.5. [...]

*Manuscript change landed:* the simulation-design paragraph now states the placement from the
actual covariance matrix (`verification/00-setup.R`, `default_Sigma`): $\sigma_{12}=0.6$ between
the two coordinates that carry missingness, $\sigma_{13}=\sigma_{24}=0.3$ between each missing
coordinate and the fully observed coordinate that drives its own missingness, $\sigma_{34}=0.5$
between the two fully observed driving coordinates, and $\sigma_{14}=\sigma_{23}=0$.

## Reviewer 3, comment 1 (MI-BIC formulation)

> Although the title explicitly promises a deviance correction for BIC, the manuscript focuses
> entirely on AIC and likelihood-ratio tests. The formulation of an MI-BIC is completely absent
> from the text. [...] The authors must explicitly formulate the corrected MI-BIC, discuss the
> appropriate sample size penalty in this context, and ideally include it in the simulation
> studies to support the title's claim.

The correction transfers to BIC without a new derivation, because it acts on the deviance
*numerator*, not the penalty. Both MI-AIC and MI-BIC are built from the same quantity,
$-2\bar Q_\infty$, the MI-averaged complete-data deviance at the observed-data estimate; the
$+\operatorname{tr}(\mathrm{RIV})$ correction removes that quantity's bias regardless of which
model-complexity penalty ($2q$ for AIC, $q\log n$ for BIC) is added afterward. This sidesteps the
effective-sample-size question the reviewer raises: rather than inventing an MI-specific effective
$n$, we use the complete-data $n$ in the penalty, matching the paper's stated target of
complete-data-equivalent selection — comparing against what BIC would select if the data had never
been missing, not against some alternative notion of information content under imputation.

We formulated the corrected MI-BIC and added it to the same simulation grid the paper already
uses for MI-AIC (60 cells, $R=2{,}000$ repetitions, `verification/_modules/w3-sweep.R`), so the
BIC numbers below are measured under the identical design, not a separate study. The correction is
directionally right for BIC — uncorrected selection favors the higher-missing-information
candidates, and correcting narrows that — but the *yield* is much smaller than for AIC, because
BIC's own $q\log n$ penalty already resists most of the pull toward the saturated model at the
sample sizes the paper studies ($N\geq200$): median uncorrected recovery of the true model is
$0.993$, corrected $0.996$, against a complete-data benchmark of $1.000$ (compare AIC's $0.693$
uncorrected / $0.818$ corrected / $0.899$ benchmark over the same cells). At this scale BIC is
already close enough to its own ceiling that there is little room left for a correction to recover.

Because that headline comparison risked reading as "BIC barely needs the correction," we went
looking for a design point where BIC is more ambiguous, rather than reporting only the reassuring
number. A model with the same parameter count as the truth is never selected under either
criterion across all $120{,}000$ existing repetitions, ruling out an equal-penalty ambiguity. A
small follow-up outside the pre-registered sweep, at $N=50$ and $N=100$, found the ambiguous
regime directly: uncorrected BIC's recovery falls to about $0.75$ ($N=50$) and $0.94$ ($N=100$),
against benchmarks of $0.93$ and $0.99$, and the correction recovers proportionally more of the
gap at those sizes. More importantly, the paper's existing claim that BIC's errors concentrate on
the largest-missing-information candidate (stated for AIC in the selection-sweep results) is
itself a large-$N$ property: only about $0.55$–$0.62$ of BIC's more frequent errors land on that
candidate at $N=50$, rising to $0.88$–$0.89$ at $N=100$ and to essentially all of them by
$N=200$. We added this as a new Discussion scope-limit paragraph (G8) rather than a full new BIC
results section, since it is an honest qualification of an existing claim, not a new headline.

*Manuscript changes already landed:* Discussion paragraph G8 states the BIC formulation, the
large-$N$ recovery numbers, and the small-$N$ follow-up; the repository's decision log (D-23)
records the design decision and the numbers' provenance.

*Reproducibility.* The BIC computation lives inside `verification/_modules/w3-sweep.R`, which
`run_all.R`'s phase 2 already sources, so it reproduces from the standard documented command with
no extra steps; a `verdicts$BIC` block in `_modules/aggregate.R` reports the numbers above (median
`pi_bic[uncorrected/corrected/oracle]`, the BIC/AIC yield ratio, and the concentration fraction)
from any future `run_all.R` run, and `00-test-primitives.R` covers the BIC penalty/correction
arithmetic directly against synthetic inputs.

## Reviewer 3, comment 2 (non-normal / GLM generalizability)

> The manuscript relies exclusively on a four-dimensional multivariate normal distribution for
> all empirical validations. [...] The authors should discuss how the derived trace penalty and
> design-imbalance terms are expected to behave under non-normal likelihoods [...]

We ran checks outside the multivariate normal family rather than leaving this as a
prediction-only paragraph — and the first round exposed an error in our own registration, which
we report first, because the corrected analysis only exists on account of that miss.

**What was registered, and what happened.** Two families were pre-registered before any code ran
(`todo/040-v1-review-response-registration.md` §9), chosen to match the reviewer's own "skewed
continuous" and "categorical" examples: Gamma (estimated dispersion) and Bernoulli, which the
registration classified as the known-scale exemplar on the reasoning "no explicit dispersion
parameter." The registered Bernoulli targets were approximately $0$ for the deterministic plug-in
and approximately $-0.5$ for the genuine posterior draw. The measured values ($R{=}1{,}000$,
$N{=}200$) were $+0.85$ (se $0.16$), about $5$ standard errors from the registered target, and
$+0.63$ (se $0.16$), about $7$ standard errors away and of the opposite sign. The family
selection was pre-registered; the theoretical target attached to it was not correct, and it was
corrected only after the miss. The error is a category error, not a computation: the known-scale
collapse requires the family's conditional missing-data entropy to be flat in the estimated
parameter, and the binary entropy is not flat ($dH/dp=-\operatorname{logit}(p)$, zero only at
$p=\tfrac12$). "Has no dispersion parameter" and "has a dispersion parameter, held fixed" are
opposite structural situations, and the registration mapped one onto the other.

**The corrected target was then derived, not asserted — and verified blind.** Because a post-hoc
correction prompted by a miss is the pattern an adversarial review flagged in our own
process, the corrected analysis was rebuilt to a higher standard than the original: (i) a full
derivation of what a canonical-link GLM should show, from the paper's own Term-A objects — under
response-only MCAR the two order-one design terms (entropy-gradient $\times$ MLE-bias, and
cross-entropy curvature) cancel exactly for any canonical link, leaving the general
$+\tfrac12\operatorname{tr}(\mathrm{RIV})$ plus a base-measure term that is zero for Bernoulli
and nonzero for Poisson; (ii) a 15-check computer-algebra verification, including exact finite-$n$
enumerations that need no Monte Carlo; (iii) pre-registration of every new target in a commit
that precedes the production runs in the git history; and (iv) an independent, blinded
cross-model re-derivation requested from a different model family given only the problem setup.

**Every registered criterion the corrected theory implies then passed.** An $N$-scan of the
Bernoulli plug-in arm ($N{=}200$ to $2{,}000$, up to $R{=}200{,}000$) gives an asymptote of
$+0.512\pm0.037$ against the derived $+0.500$; its $N{=}200$ value is $+0.518\pm0.012$, which
also settles the residual the earlier run left unattributed — the $+0.85$ was Monte-Carlo noise
at $R{=}1{,}000$ around a true value near $+0.52$, not a hidden term. A Poisson model, simulated
in this project for the first time only after its target was fixed, lands at $+0.113\pm0.027$
against its derived target of $+0.104$ — a target far from both naive candidates ($+0.5$ and
$0$), because Poisson's base measure ($1/y!$) contributes a derived $-0.40$ correction that
Bernoulli's constant base measure does not have. The posterior-draw arm matches its derived
discount ($-0.31\pm0.07$ at $N{=}2{,}000$ against $-0.261$). And a Student-t location model with
scale and degrees of freedom held fixed — a genuine known-scale family outside the normal, with
both targets derived and dated before any code ran — measures $+0.02\pm0.05$ (plug-in) and
$-0.48\pm0.05$ (posterior draw) against the derived $0$ and $-0.5$, so the known-scale collapse
is no longer verified only in the multivariate normal family. In the course of this the original
Bernoulli draw value was found to carry a second defect: the original script fixed the imputation
seed across all repetitions, so its quoted standard error overstated independence
(`verification/spikes/phase3-mice-seed-diagnostic.R` reproduces the old value with the fixed
seed and the corrected one without it). All superseded numbers stay in the record; none is
load-bearing.

**The Gamma check stays a directional confirmation.** The plug-in measures $+0.32$ (se $0.20$),
inside a wide interval around the predicted one half, and the posterior draw is more negative
($-0.52$, se $0.20$), the same direction as the multivariate-normal posterior-draw result
(reviewer 1, comment 8). Gamma's log link is not canonical, so the new lemma does not cover it,
and its run shares the fixed-seed caveat above — we therefore claim direction, not magnitude, for
this family.

**Scope of what this answers.** This addresses the trace penalty and design-imbalance terms named
in the reviewer's question — the quantities the paper's applications use — now with a derived,
blind-tested GLM extension rather than only an empirical spot-check; and separately it closes the
known-scale boundary result's non-normal gap with the Student-t exemplar. The remaining
non-normal opening is stated in the manuscript (G9): non-canonical links (including Gamma's) have
no derived magnitude, and general missingness patterns beyond response-only are not covered by
the new lemma.

*Manuscript change landed:* Discussion paragraph G9 rewritten to the corrected,
chronology-first account; the repository's decision log records the correction (D-25, with a
superseding pointer at D-24). *Reproducibility:* `verification/spikes/phase3-family-scan.R`
(four arms) + `phase3-family-scan-score.R` (registered-criteria scorecard) +
`phase3-mice-seed-diagnostic.R`, all with documented commands; CAS companion
`verification/cas-wolfram/verify_bernoulli_fitted_gap.py` (15 checks); registration and results
are separate commits (`4aaeaae` then `afa4438`), so the pre-registration is checkable in the git
history, not asserted. Cross-model verification: a blinded GPT-5.5 Pro re-derivation plus
red-team (both archived at `verification/cache/layer3-gpt-5.5-pro-bern-glm-mode{A,B}.md`) and a
repo-grounded Gemini compliance validation of this very text against the adversarial review's
amendments (`tkal-reviews/gemini-045c-compliance-20260704/REPORT.md`).

## Reviewer 3, comment 3 (congeniality diagnosis)

> [...] the manuscript does not provide, nor does it cite, any practical methods or established
> literature for how an applied researcher should actually perform this diagnosis. [...]

The reviewer is right that the Discussion recommended diagnosing congeniality without pointing
at any way to do it. The congeniality-limit paragraph (G7) now closes with three sentences of
practical pointers, each backed by a reference acquired and read in full for this response
(acquisition and claim-verification trail in `todo/003-references-to-acquire.md`):

- **He & Zaslavsky (2012, *Statistics in Medicine*)** give the closest published
  operationalization of a congeniality check: a posterior predictive diagnostic that applies the
  analyst's own target analysis to the completed data and to replicates simulated under the
  imputation model, with a re-imputation implementation that runs on standard MI software (their
  §3.3) and applies to non-fully-Bayesian imputation engines. Their framing is explicitly about
  detecting analysis/imputation uncongeniality ("model uncongeniality" is one of the paper's
  keywords).
- **Bondarenko & Raghunathan (2016, *Statistics in Medicine*)** build graphical and numerical
  checks that compare observed and imputed values conditional on the response propensity; their
  stated first objective is that "the analyst can diagnose uncongeniality" without knowing the
  imputation model — the exact one-sided situation an applied secondary analyst is in.
- **Nguyen, Carlin & Lee (2017, *Emerging Themes in Epidemiology*)** review the available
  checking methods for applied use (graphical observed-vs-imputed comparisons, the
  propensity-conditional checks above, regression diagnostics, cross-validation, and posterior
  predictive checking); their case study shows the posterior predictive check catching just such an
  imputation/analysis incompatibility.

*Manuscript change landed:* the G7 Discussion paragraph gains the three-sentence pointer with
all three citations; all three references were verified against their texts before citing, per
the repository's citation discipline.

## Proof-verifier, comment 10 (abstract estimated-scale qualifier)

> The abstract's formulation implies the $+1/2\operatorname{tr}(\mathrm{RIV})$ bias is a universal
> property of proper MI, whereas the proof establishes it only for the estimated-scale regime.

*Manuscript change landed:* the abstract now reads "under congenial proper multiple imputation
with the complete-data maximum likelihood estimate as target and an estimated scale or
covariance," naming the scope condition where the headline bias previously stated it without
qualification.

## Proof-verifier, comment 11 ("trace component" scoping)

> [...] the claim should be scoped to clarify that the correction removes only the trace
> component [not the design-imbalance term $(A)+(C)$].

*Manuscript change landed:* the abstract's "adding one trace term per candidate removes the
deviance bias in expectation" now reads "removes *that trace component* of the deviance bias in
expectation," consistent with the abstract's own preceding sentence naming the separate
design-imbalance term the correction does not touch.

## Contradictions reviewer, comment 12 (alpha sign)

> The text defines $\alpha$ as $-\mathcal{E}'(\theta_0)$ and describes it as 'the gradient of the
> conditional missing-data entropy'. [...] making $\alpha$ the negative gradient, not the gradient
> itself.

Correct as flagged: $\mathcal{E}'(\theta_0)$ is the entropy's gradient, so $\alpha=-\mathcal{E}'(\theta_0)$
is its negative. *Manuscript change landed:* the definition now reads "is the negative gradient
of the conditional missing-data entropy."

## Contradictions reviewer, comment 13 (KS 0.019 vs. 0.018)

> The main text states that the Kolmogorov-Smirnov distance falls to 0.019 under equating. However,
> Figure 8 displays the value 0.018 above the equating bar.

Traced to source: the underlying value is stored in `verification/cache/ic-ladder-summary.csv` as
$0.0185$, which sits exactly on a floating-point rounding boundary — R represents it as
$0.01849999\ldots$, so `sprintf("%.3f", ks)` in the figure-generating code
(`verification/figures.R`) mechanically rounds to $0.018$, while the manuscript prose had been
rounded by hand to $0.019$. *Manuscript change landed:* the calibration-ladder results paragraph
now states $0.018$, matching the figure and the value's actual floating-point representation.

## Contradictions reviewer, comment 14 (k: parameter count vs. model index)

> The symbol $k$ is initially defined as the number of parameters [...] However, in Section 5's
> information-criterion selection, $k$ is redefined as a model index in $\text{AIC}_{MI}(k)$ [...]

Confirmed as described, and traced to two further occurrences of the same double-duty
$k$ the reviewer's example did not cite (the RIV display with its fraction-of-missing-information
identity, and the derivation of the estimation-mismatch term). *Manuscript change landed:*
every parameter-count use of $k$ (the dimension $q=p+\tfrac12p(p+1)$, with its matching
identity-matrix and bare-$k$ trace terms) is renamed to $q$; the model-index use of $k$ in the
information-criterion section, where $q_k$ already denotes candidate $k$'s own parameter count,
is unchanged.

## Contradictions reviewer, comment 15 (m vs. M for number of imputations)

> The manuscript uses both $m$ and $M$ to denote the number of imputations. [...]

*Manuscript change landed:* standardized on $M$ throughout — the four lowercase-$m$
asymptotic-limit uses (the Wei–Tanner/Rubin draws and their $m\to\infty$ limit in the Background,
the $m\to\infty$ Rubin's-rules statement, the "finite-$m$ corrections," and the "infinite-$m$
limit") now read $M$, matching the simulation's own $M\in\{20,200\}$ used everywhere else.

## References

::: {#refs}
:::
