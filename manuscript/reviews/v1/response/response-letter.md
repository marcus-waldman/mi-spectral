# Response to Reviewers — v1 AI Review (Paper 88)

**Source review:** `manuscript/reviews/v1/ai-review-paper-88.md` (Reviewer3.com, 15 comments
across 5 personas: reviewer1, reviewer2, reviewer3, proof-verifier, contradictions-reviewer).
**Triage of record:** `todo/040-v1-review-response-registration.md` §1 (four tiers) and
`.prometheus/charter.md`. This letter is assembled incrementally as each tier's work completes;
entries marked **PENDING** below are tracked but not yet drafted.

Status legend: **DRAFTED** (text below is final, reviewed by Marcus) · **EXECUTED, PENDING TEXT**
(underlying work is done and landed in the manuscript, but the response-letter prose itself is
not yet written or reviewed) · **PENDING** (neither the underlying work nor the text exists yet).

---

## reviewer3 — r3#1 (MI-BIC formulation) — Tier B — Status: EXECUTED, PENDING TEXT

> Although the title explicitly promises a deviance correction for BIC, the manuscript focuses
> entirely on AIC and likelihood-ratio tests. The formulation of an MI-BIC is completely absent
> from the text. [...] The authors must explicitly formulate the corrected MI-BIC, discuss the
> appropriate sample size penalty in this context, and ideally include it in the simulation
> studies to support the title's claim.

*Response not yet drafted.* Underlying work is done: MI-BIC computed alongside MI-AIC in the
same 60-cell R=2000 grid (`verification/_modules/w3-sweep.R`, `run_all-prod-bic`), landed as
Discussion caveat G8 (`S6-P4c`, `decisions.md` D-23) — BIC's own penalty resists most of the
saturated-model pull at N>=200 (uncorrected 0.98 / corrected 0.99 / benchmark 1.00), and a
small-N (50/100) follow-up found the ambiguous regime directly. Response-letter prose to be
drafted in Phase 4.

## reviewer3 — r3#2 (non-normal / GLM generalizability) — Tier D — Status: PENDING

> The manuscript relies exclusively on a four-dimensional multivariate normal distribution for
> all empirical validations. [...] The authors should discuss how the derived trace penalty and
> design-imbalance terms are expected to behave under non-normal likelihoods [...]

*Gated on Phase 3* (non-normal fork, gated on a scope decision per `todo/040` §2). Resolves either
as an empirical two-regime illustration or a Discussion-only prediction paragraph.

## reviewer3 — r3#3 (congeniality diagnosis) — Tier D — Status: PENDING

> [...] the manuscript does not provide, nor does it cite, any practical methods or established
> literature for how an applied researcher should actually perform this diagnosis. [...]

Reference backlog tracked in `todo/003-references-to-acquire.md`; resolves as a Discussion
sentence in Phase 4 once a citable diagnostic method is acquired and verified.

## reviewer2 — r2#4 (+/- dispersion measure undefined) — Tier C — Status: PENDING

> Throughout the simulation results, the manuscript uses the "+/-" symbol without defining the
> measure of dispersion in the main text. [...]

Easy level3 fix, Phase 4.

## reviewer2 — r2#5 (name all four selection-sweep models) — Tier C — Status: PENDING

> The authors define the extremes of the candidate set (diagonal and saturated) but omit the
> definitions of the two intermediate nested models [...]

Easy level3 fix, Phase 4.

## reviewer2 — r2#6 (Sigma / correlation placement) — Tier C — Status: PENDING

> The manuscript does not specify which of the six possible coordinate pairs [...] are assigned
> the correlations of 0.6, 0.3, and 0.5. [...]

Easy level3 fix, Phase 4.

## reviewer1 — r1#7 (heavy-tail N=1000 remark) — Tier A — Status: PENDING

> The authors justify the failure of the N=1000 cell to hit the analytic target by claiming the
> standard deviation of the per-repetition statistic grows with sample size due to heavy tails.
> [...] The authors must either clarify why the variance of this specific statistic scales
> positively with N [...]

Triaged as a reviewer conflation of sample size N with repetition count R (finite variance; one
clarifying sentence resolves it). Response-letter prose not yet drafted; Phase 4.

## reviewer1 — r1#8 (data-augmentation control) — Tier A -> Phase 1 — Status: DRAFTED

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

*Manuscript changes already landed:* `manuscript/derivation.qmd` — a new forward-pointer at D9
(:391–394), a corrected fitted-vs-oracle callout, and a new scope-and-correction callout
(:422–479) stating the theorem's scope (second-moment-matched, regular-draw imputers) and the
disclosed correction for engines outside that scope; a one-sentence addition to the known-scale
callout (:812–816). `decisions.md` D-22 records the amendment and its provenance.

*Still open (not blocking this response):* the design-imbalance term IMB inside D has a measured
value but no closed form yet (candidate: Tallis truncated-bivariate-normal moments, GPT-5.5 Pro
Mode B — not yet independently verified); the bootstrap-floor exact-identity check
(`engine-gap-audit.R`'s E3 arm) currently covers one N-point, extending it to the same four
points as the original Amelia scan is cheap and would close gate item C7 (optional, not required
for this response).

## reviewer1 — r1#9 (nested-confound control) — Tier A — Status: PENDING

> In the selection-sweep design, the candidate models are nested, meaning that model complexity
> (parameter count) is perfectly confounded with the amount of missing information. [...] the
> authors should include a control experiment comparing non-nested candidate models that have the
> same number of parameters but differ significantly in their fractions of missing information.

Triaged as already answered by existing evidence: the W4 non-nested measurement plus the MCAR
twins design already isolate the missing-information mechanism from raw model complexity.
Response-letter prose not yet drafted; Phase 4.

## proof-verifier — proof#10 (abstract estimated-scale qualifier) — Tier C — Status: PENDING

> The abstract's formulation implies the $+1/2\operatorname{tr}(\mathrm{RIV})$ bias is a universal
> property of proper MI, whereas the proof establishes it only for the estimated-scale regime.

Easy level3 fix (abstract qualifier), Phase 4.

## proof-verifier — proof#11 ("trace component" scoping) — Tier C — Status: PENDING

> [...] the claim should be scoped to clarify that the correction removes only the trace
> component [not the design-imbalance term $(A)+(C)$].

Easy level3 fix, Phase 4.

## contradictions-reviewer — contra#12 (alpha sign) — Tier C — Status: PENDING

> The text defines $\alpha$ as $-\mathcal{E}'(\theta_0)$ and describes it as 'the gradient of the
> conditional missing-data entropy'. [...] making $\alpha$ the negative gradient, not the gradient
> itself.

Easy level3 fix, Phase 4.

## contradictions-reviewer — contra#13 (KS 0.019 vs. 0.018) — Tier C — Status: PENDING

> The main text states that the Kolmogorov-Smirnov distance falls to 0.019 under equating. However,
> Figure 8 displays the value 0.018 above the equating bar.

Easy level3/figure fix, Phase 4.

## contradictions-reviewer — contra#14 (k: parameter count vs. model index) — Tier C — Status: PENDING

> The symbol $k$ is initially defined as the number of parameters [...] However, in Section 5's
> information-criterion selection, $k$ is redefined as a model index in $\text{AIC}_{MI}(k)$ [...]

Easy level3 notation fix, Phase 4.

## contradictions-reviewer — contra#15 (m vs. M for number of imputations) — Tier C — Status: PENDING

> The manuscript uses both $m$ and $M$ to denote the number of imputations. [...]

Easy level3 notation standardization, Phase 4.
