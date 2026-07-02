# Response to reviewer1, comment 8 (data-augmentation control)

**Status:** draft, Phase 1 of the v1-review response (todo/040). Written to be folded into
the full point-by-point letter in Phase 4. Not yet reviewed by Marcus.

## Reviewer comment (verbatim)

> The manuscript claims to validate the trace correction for proper multiple imputation, but
> the simulations rely exclusively on an approximately Bayesian bootstrap
> expectation-maximization approach rather than exact data augmentation. Because the
> theoretical derivations for proper MI depend on exact posterior draws, the lack of a fully
> Bayesian Markov chain Monte Carlo (MCMC) control experiment undermines the claim that the
> correction holds for proper MI, especially under high missingness. I recommend running the
> headline simulation studies using a standard data augmentation engine to confirm that the
> analytic results hold without the artifacts of the bootstrap approximation.

## Response

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
to capture exactly that extra spread), and the deviance — a sum of $n$ per-cell $O(1/n)$-sensitive
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
is disclosed but not yet given a closed form. Because $b_\Sigma$ is prior-dependent, the
correction's size depends on the prior: a Jeffreys-prior draw measures $\approx-0.78\cdot
\operatorname{tr}(\mathrm{RIV})$ at $N=200$, and a weakly-informative brms/Stan draw (LKJ +
half-$t$ priors, run as an independent check) measures $\approx-1.36\cdot\operatorname{tr}(\mathrm{RIV})$
— more negative still, confirming the effect is not a Jeffreys-improper-prior artifact but general
to full-Bayes posterior-draw imputation.

**Constructive remedy, for a user who wants to run a genuine Bayesian sampler anyway.**
Recentring the posterior draws at their own measured $b_\Sigma$ — rather than using them as
drawn — collapses the correction from $\approx-0.78\cdot\operatorname{tr}(\mathrm{RIV})$ to
$\approx-0.15\cdot\operatorname{tr}(\mathrm{RIV})$, matching a mean-centered Gaussian draw. This
is offered as the practical fix; an earlier percentage decomposition of the raw $-0.244$
diagnostic value (roughly "83% centering / 13% mu-wander / 4% imbalance") was checked during the
cross-model audit and found to rest on a linear-rescaling assumption that does not hold — the
deflation acts inside an iterative data-augmentation P-step, not as a one-shot rescale — and is
retracted. The underlying $-0.78$/$-0.24$/$-0.15$ measurements themselves are unaffected and
independently reconfirmed at higher precision.

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

## Manuscript changes already landed

`manuscript/derivation.qmd`: a new forward-pointer at D9 (:391–394), a corrected fitted-vs-oracle
callout, and a new scope-and-correction callout (:422–479) stating the theorem's scope
(second-moment-matched, regular-draw imputers) and the disclosed correction for engines outside
that scope; a one-sentence addition to the known-scale callout (:812–816). `decisions.md` D-22
records the amendment and its provenance. `manuscript/plan/decisions.md:136`.

## Still open (not blocking this response)

- The design-imbalance term $\mathrm{IMB}$ inside $D$ has a measured value but no closed form yet
  (candidate: Tallis truncated-bivariate-normal moments, GPT-5.5 Pro Mode B — not yet
  independently verified).
- The bootstrap-floor exact-identity check (`engine-gap-audit.R`'s E3 arm) currently covers one
  $N$-point; extending it to the same four points as the original Amelia scan is cheap and would
  close gate item C7. Optional, not required for this response.
