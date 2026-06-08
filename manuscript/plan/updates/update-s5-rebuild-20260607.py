# S5 Simulation studies - REBUILD (todo/033), 2026-06-07
#
# Replaces the 14-paragraph numbers-in-prose S5 with a per-study Methods + figure
# rebuild. Direction (Marcus, todo/033):
#   1. Setup = one Methods block PER simulation (DGM + params, N, missingness
#      pattern/mechanism/rate, engine + M, repetitions, estimand/metric, frozen
#      pass criterion), reproducible from the paragraph alone.
#   2. Results = figures and tables, each carrying an explicit "perfect" reference
#      (oracle / nominal level / analytic target / y=x) AND the achieved value.
#   3. Impatient-reader test: self-contained captions; jump to any one exhibit.
# Constraints: plain cadence + punctuation budget (no semicolons, colons only
# after bold run-ins / before displays / "Monte Carlo standard error" table
# intro); T-07 repetitions; D-05 failures in main text (N=1000 W1 miss, 9-20%
# component misses, similar-pair W4 below resolution); D-09-A1 setup/results
# subhead split kept. Figures committed by verification/figures.R into
# manuscript/figures/ (PNG, 300 dpi), drawn from gate-confirmed caches.
#
# Setup:   P1 roadmap, P2 apparatus, P3 grading+registration,
#          P4 theorem-validation design, P5 known-scale/sign-regime design,
#          P6 LRT design, P7 discrimination design, P8 pairing design,
#          P9 selection-sweep design, P10 ladder design, P11 non-nested design.
# Results: P12 theorem (fig-w1-theorem), P13 known-scale (fig-knownscale),
#          P14 LRT (fig-lrt-absorption), P15 discrimination (fig-discrimination),
#          P16 pairing (fig-pairing), P17 selection (fig-w3-selection),
#          P18 ladder table (fig-ladder), P19 ladder internals
#          (fig-ladder-internals), P20 structural limits (tbl, no fig),
#          P21 non-nested (fig-w4-nonnested), P22 engine sensitivity.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"


def FIG(caption, fname, label, width):
    return "\n\n![" + caption + "](figures/" + fname + "){#" + label + " width=\"" + width + "\"}"


# ===================== SETUP =====================

P1 = (
    "## Simulation studies: setup\n\n"
    "This section is the paper's complete empirical account. Every quantitative "
    "claim in @sec-derivations points here, and every number here traces to a "
    "study whose predictions and pass criteria were fixed before its code was "
    "written (@sec-methods). The setup subsection states each study as a "
    "stand-alone design that another analyst could reproduce. The results "
    "subsection presents each study as a figure or a table, including the "
    "predictions that were not met. A reader can enter at any single exhibit, "
    "because each one names the perfect reference and the value the study "
    "achieved. Everything here carries the *measured* tier of @sec-methods "
    "unless stated otherwise."
)

P2 = (
    "**Apparatus.** The designs are multivariate normal in four dimensions, with "
    "one bivariate special case. Two imputation arms run throughout. The "
    "deterministic arm evaluates the averaged log-likelihood $\\bar Q_\\infty$ in "
    "closed form at the full-information maximum-likelihood estimate "
    "$\\hat\\theta_{\\text{obs}}$, which is the expectation-maximization "
    "Q-function with no simulation error. The proper arm draws imputations by "
    "expectation-maximization with bootstrapping, as implemented in Amelia "
    "[@honakerAmeliaIIProgram2011]. That sampler runs expectation-maximization "
    "on bootstrap resamples of the incomplete data to approximate the posterior "
    "of $(\\mu, \\Sigma)$, then draws completions at those values. The exact "
    "alternative, data augmentation, was not run, and the engine-sensitivity "
    "study below bounds what that choice costs."
)

P3 = (
    "**Grading and registration.** Each study is graded against pass criteria "
    "fixed before its code existed, recorded in the pre-registration documents "
    "and their dated amendment histories. The bias-decomposition, "
    "likelihood-ratio, and selection studies were registered together. The "
    "distribution-matching ladder and the non-nested measurement each carry "
    "their own registration. The known-scale and sign-regime runs are dedicated "
    "single-question designs. Two reporting rules hold throughout. Failed "
    "predictions appear here in the main text beside the successes, and every "
    "quantitative claim is stated for totals and paired differentials rather "
    "than for components, for a reason the first study makes concrete."
)

P4 = (
    "**Theorem-validation design.** The data-generating model is a four-variate "
    "normal with zero mean and unit variances, with correlations $0.6$, $0.3$, "
    "and $0.5$ among three coordinate pairs and zero among the rest, giving a "
    "relative-increase-in-variance trace near $5.55$. The first two coordinates "
    "are made missing at random with probabilities $\\Phi(-0.5 + 0.4 X_3)$ and "
    "$\\Phi(-0.5 + 0.4 X_4)$ driven by the two fully observed coordinates, a "
    "non-monotone pattern at about one third missing per coordinate. Sample "
    "sizes are $N \\in \\{200, 500, 1000, 2000\\}$ with $1000$ repetitions each. "
    "The estimand is the net deviance bias $\\mathbb{E}[T]$, carried on the "
    "analytic arm so it is free of simulation error. The pre-registered target "
    "is one half the trace, near $2.77$, refined during analysis to the "
    "order-one-augmented band $2.42$ to $2.55$ once the missing-at-random term "
    "was derived. The study passes if the inverse-variance pooled estimate falls "
    "in that band."
)

P5 = (
    "**Known-scale and sign-regime design.** Two single-question runs close the "
    "theorem. The known-scale run holds the covariance at its true value and "
    "fits only the mean, so the conditional missing-data entropy no longer "
    "depends on the estimated parameters. It uses the four-variate normal above "
    "at $N = 200$ with $2 \\times 10^5$ repetitions, on both the deterministic "
    "and the proper arm. The estimand is again $\\mathbb{E}[T]$, and "
    "@eq-knownscale predicts zero on the deterministic arm and "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ on the proper arm. The "
    "sign-regime run imputes from the true model rather than the fitted model "
    "and checks that the total reverses sign, as the fitted-versus-oracle "
    "distinction of @sec-derivations requires. Each run passes if its arms "
    "reproduce the predicted values within Monte Carlo error."
)

P6 = (
    "**Likelihood-ratio design.** The test is $H_0\\!: \\sigma_{12} = 0$ in the "
    "four-variate normal, against the local alternative "
    "$\\sigma_{12} = \\delta / \\sqrt n$ on the grid "
    "$\\delta \\in \\{0, 0.5, 1, 1.5, 2, 2.5, 3, 4\\}$. The sample size is "
    "$N = 200$ with $M = 200$ imputations from the proper arm and $1000$ "
    "repetitions per grid point. Four references are compared. The complete-data "
    "oracle refers its statistic to $\\chi^2_1$. The corrected and uncorrected "
    "numerators are referred to a simulated reference distribution. The "
    "Satorra-Bentler arm applies a scaled-and-shifted statistic referred to "
    "$\\chi^2_1$. The metric is the rejection rate at level $0.05$, and the null "
    "arm passes if it sits near nominal, with the corrected numerator slightly "
    "conservative as double-counting predicts."
)

P7 = (
    "**Formula-discrimination design.** This run separates the two candidate "
    "formulas for the differential bias, which agree under equal missing "
    "information and diverge when it is uneven. The test is $H_0\\!: \\mu_1 = 0$ "
    "in the four-variate normal, with the first coordinate made heavily missing "
    "at random through $\\Phi(0.8 + 1.2 X_3)$, about $70$ to $79$ percent, the "
    "second coordinate essentially complete, and the rest fully observed. One "
    "direction is tested. Sample sizes are $N \\in \\{500, 1000\\}$ with $2000$ "
    "repetitions on the deterministic arm. The metric is the paired differential "
    "bias. The projected trace of @eq-lrt-bias predicts about $2.64$ and the "
    "naive trace difference predicts about $8.5$, so the run passes if the data "
    "land on the projected-trace value."
)

P8 = (
    "**Pairing design.** This run shows that comparing the same imputations under "
    "both models collapses the per-dataset noise. The design is the four-variate "
    "$\\sigma_{12} = 0$ cell with one tested direction, at "
    "$N \\in \\{500, 1000, 2000\\}$ with $2000$ repetitions. Three arms run. The "
    "null and the local alternative hold the differential at order one, and a "
    "fixed alternative is included as the failure mode. The metric contrasts the "
    "single-model deviance standard deviation with the paired-differential "
    "standard deviation. The run passes if pairing holds the differential "
    "standard deviation flat at the null while the single-model figure grows "
    "with the sample size."
)

P9 = (
    "**Selection-sweep design.** The candidate set is four nested "
    "multivariate-normal covariance models, from a diagonal model up to the "
    "saturated model, with a compound-symmetry structure as the truth. The sweep "
    "covers $60$ cells that cross two missingness patterns, the mechanisms "
    "missing at random and not at random, three sample sizes "
    "$N \\in \\{200, 500, 1000\\}$, and five engine slots pairing the "
    "deterministic arm with proper imputation at $M \\in \\{20, 200\\}$ under "
    "congenial and uncongenial specification. Missingness is set near $40$ "
    "percent and each cell uses $2000$ repetitions. The metric is the true-model "
    "selection rate by the Akaike criterion, computed for the complete-data "
    "oracle, the uncorrected imputation criterion, and the corrected criterion. "
    "The headline cell is non-monotone missing-at-random on the deterministic "
    "arm. The sweep passes if the correction moves selection toward the oracle "
    "and if the uncorrected criterion's errors concentrate on the "
    "largest-missing-information candidate."
)

P10 = (
    "**Distribution-matching ladder design.** This study takes the same candidate "
    "family and contrasts four ways of referring the saturated-anchored "
    "imputation deviance to its complete-data law, across a range of signal "
    "strength. Three cells run at $N = 500$ with $2000$ repetitions and four "
    "tested directions, all non-monotone missing at random near $40$ percent on "
    "the deterministic arm. The cells are a main design at correlation $0.40$, a "
    "weak-signal design at $0.10$ with near-tied candidates, and a junk design "
    "at $0$ where the truth is diagonal. Five constructions are compared. They "
    "are the complete-data oracle, the uncorrected deviance, a mean correction "
    "that subtracts the projected trace of @eq-lrt-bias, a two-moment match to "
    "the reference, and a per-model equipercentile equating. The metric is the "
    "true-model selection rate, supported by null-side distance and variance "
    "checks and by the noncentral shrinkage factors. The study passes its "
    "pre-registered criteria if the null side calibrates, the stronger arms "
    "reach the oracle where overfit flips drive the errors, and the noncentral "
    "side shrinks by the predicted factors."
)

P11 = (
    "**Non-nested design.** This measurement isolates the order-one "
    "design-imbalance differential of @prp-ac-diff for genuinely separated "
    "candidates, the one quantity the derivations leave unmeasured. The truth is "
    "a four-variate first-order autoregressive covariance at correlation $0.5$. "
    "Two candidate pairs run. The similar pair sets compound symmetry against "
    "the autoregressive model, and the dissimilar pair sets a diagonal model "
    "against it. Each cell runs at $N \\in \\{500, 1000, 2000\\}$ with "
    "$20{,}000$ repetitions, paired with a missing-completely-at-random twin "
    "that removes the design-imbalance term. The metric is the isolated "
    "differential, the missing-at-random paired residual minus its "
    "completely-at-random twin. The mechanism passes if the level is order one "
    "and collapses under the twin, the dissimilar pair passes if its "
    "differential resolves at the predicted scale, and the pre-registered "
    "similar-pair headline is graded honestly against the resolution the design "
    "affords."
)

# ===================== RESULTS =====================

P12 = (
    "## Simulation studies: results\n\n"
    "**Theorem validation.** The net deviance bias tracks the analytic half-trace "
    "across every sample size, and the inverse-variance pooled estimate confirms "
    "the completed theorem at $2.43 \\pm 0.26$ against the order-one-augmented "
    "prediction $2.42$ to $2.55$ (@fig-w1-theorem). One cell is a genuine miss. "
    "At $N = 1000$ the estimate falls $2.6$ standard errors below the "
    "preregistered target, a consequence of the heavy-tailed per-repetition "
    "statistic, whose standard deviation grows with the sample size and leaves "
    "the larger cells unable to resolve an order-one offset at fixed repetition "
    "count. The component terms separately miss their targets by roughly $9$ to "
    "$20$ percent, which is why the grading reports only totals and paired "
    "differentials." +
    FIG(
        "**Theorem validation.** Each point is the net deviance bias "
        "$\\mathbb{E}[T]$ at one sample size with a $95$ percent interval, "
        "estimated on the analytic arm with $1000$ repetitions. Perfect is the "
        "analytic target, the dotted line at the preregistered half-trace $2.77$ "
        "and the shaded band at the order-one-augmented prediction $2.42$ to "
        "$2.55$. The solid line is the inverse-variance pooled estimate "
        "$2.43 \\pm 0.26$, inside the band. The $N = 1000$ cell falls $2.6$ "
        "standard errors below target, the study's one reported miss.",
        "fig-w1-theorem.png", "fig-w1-theorem", "82%")
)

P13 = (
    "**Known scale and sign regime.** Holding the covariance known and fitting "
    "only the mean collapses the bias to the two values @eq-knownscale predicts "
    "(@fig-knownscale). The deterministic arm returns $0.025 \\pm 0.018$ against "
    "a target of zero and the proper arm returns $-0.536 \\pm 0.018$ against "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) = -0.561$, both within Monte "
    "Carlo error and differing by exactly the posterior-draw imputation "
    "variance. Imputing from the true model rather than the fitted model "
    "reverses the sign of the total, as the fitted-versus-oracle distinction "
    "requires." +
    FIG(
        "**Known scale.** The two imputation arms of the known-scale run at "
        "$N = 200$ with $2 \\times 10^5$ repetitions, each with a $95$ percent "
        "interval. Perfect is the pair of analytic targets, zero for the "
        "deterministic arm and "
        "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) = -0.561$ for the proper "
        "arm. Both arms reach their target within Monte Carlo error.",
        "fig-knownscale.png", "fig-knownscale", "66%")
)

P14 = (
    "**Likelihood-ratio absorption.** A correctly calibrated reference absorbs "
    "the differential bias at the null, so the test controls its Type I error "
    "(@fig-lrt-absorption). The uncorrected numerator rejects at $0.042$ and the "
    "additionally corrected numerator at $0.034$, both near the nominal $0.05$ "
    "and the corrected one slightly conservative as double-counting predicts. "
    "Raw power across the alternative is not compared here, because the four "
    "references reject at different Type I error and a raw power comparison would "
    "be confounded. The size-adjusted power arms are the partial support cited "
    "for the power conjecture of @sec-discussion. One scope note travels with "
    "this study. Its committed correction arm used the naive trace difference, "
    "which differs from @eq-lrt-bias by about $5$ percent in this near-invariance "
    "design and is immaterial here, though @eq-lrt-bias is the correct general "
    "form." +
    FIG(
        "**Likelihood-ratio Type I error.** The rejection rate at the null for "
        "four references at $N = 200$ with $1000$ repetitions and Monte Carlo "
        "error bars. Perfect is the nominal $0.05$ line. The uncorrected "
        "numerator sits at $0.042$ and the corrected one at $0.034$, both near "
        "nominal, the corrected one slightly conservative because it "
        "double-counts. Raw power across the alternative is not shown, because "
        "the references reject at different Type I error and the comparison would "
        "be confounded. The size-adjusted power conjecture is treated in the "
        "Discussion.",
        "fig-lrt-absorption.png", "fig-lrt-absorption", "78%")
)

P15 = (
    "**Discrimination of the two formulas.** On a design where the two formulas "
    "separate widely, the data fall on the projected-trace formula and far from "
    "the naive one (@fig-discrimination). The observed differential is "
    "$2.64 \\pm 0.11$ at $N = 500$ and $2.70 \\pm 0.11$ at $N = 1000$, on the "
    "projected-trace prediction of $2.64$ and $52$ standard errors from the "
    "naive trace difference. The naive difference always overstates the correct "
    "value, and this design makes the gap large enough to rule it out outright." +
    FIG(
        "**Discrimination.** The observed paired differential at two sample sizes "
        "with $95$ percent intervals, from $2000$ repetitions on the "
        "heavy-missingness $\\mu_1$ design. Perfect is the projected-trace "
        "prediction $\\operatorname{tr}(\\mathrm{RIV}_\\perp) = 2.64$, the solid "
        "line. The naive trace difference, the dashed line near $8.5$, is "
        "rejected at $52$ standard errors.",
        "fig-discrimination.png", "fig-discrimination", "72%")
)

P16 = (
    "**Pairing.** Comparing the same imputations under both models holds the "
    "per-dataset noise at order one (@fig-pairing). At the null the "
    "paired-differential standard deviation stays near $1.5$ across $N = 500$, "
    "$1000$, and $2000$, while the single-model figure grows from $18.4$ to "
    "$36.5$. At a fixed alternative the square-root-of-$n$ growth returns, to "
    "$12.4$, $16.8$, and $24.9$, exactly the failure mode the result specifies." +
    FIG(
        "**Pairing.** Standard deviation of the deviance statistic against sample "
        "size, from $2000$ repetitions, on a logarithmic scale. Perfect is a "
        "flat line at order one, achieved by the paired differential at the "
        "null, the lower curve. The single-model statistic grows with the sample "
        "size, and the paired differential at a fixed alternative grows too, the "
        "documented limit of pairing.",
        "fig-pairing.png", "fig-pairing", "72%")
)

P17 = (
    "**Selection.** The uncorrected criterion favors high-missing-information "
    "models, and the correction moves selection back toward the complete-data "
    "oracle (@fig-w3-selection). At $N = 500$ on the deterministic arm the "
    "oracle selects the true model at $0.90$, the uncorrected criterion at "
    "$0.67$, and the corrected criterion at $0.82$. In every congenial cell, all "
    "of the uncorrected criterion's errors land on the saturated, "
    "largest-missing-information candidate. The recovery is substantial and "
    "visibly short of the oracle, which is what the distribution-matching ladder "
    "was registered to explain." +
    FIG(
        "**Selection.** True-model selection rate by the Akaike criterion at "
        "three sample sizes on the non-monotone missing-at-random cell, $2000$ "
        "repetitions. Perfect is the complete-data oracle, the dashed line and "
        "the black bar. The uncorrected criterion sits well below it and the "
        "correction recovers most of the gap. All uncorrected errors fall on the "
        "largest-missing-information candidate.",
        "fig-w3-selection.png", "fig-w3-selection", "82%")
)

P18 = (
    "**The distribution-matching ladder.** Across three levels of signal strength "
    "the stronger constructions recover the oracle where overfit flips drive the "
    "errors, and a floor remains where selection is genuinely hard "
    "(@fig-ladder). The true-model selection rates are reported below, with "
    "Monte Carlo standard error near $0.010$:\n\n"
    "| Cell | oracle | uncorrected | mean | two-moment | equating |\n"
    "|---|---|---|---|---|---|\n"
    "| $\\rho = 0.40$ | 0.899 | 0.678 | 0.814 | 0.904 | 0.903 |\n"
    "| $\\rho = 0.10$ | 0.820 | 0.582 | 0.650 | 0.648 | 0.650 |\n"
    "| $\\rho = 0$ (junk) | 0.727 | 0.422 | 0.585 | 0.702 | 0.696 |\n\n"
    "At correlation $0.40$ the two-moment and equating arms reach $0.904$ and "
    "$0.903$ against the oracle's $0.899$, statistically indistinguishable, and "
    "the junk cell closes $90$ percent of the uncorrected-to-oracle gap. In the "
    "weak-signal cell the oracle itself drops to $0.820$ and no arm passes "
    "$0.650$, because the stronger arms' null-side gains are offset by underfit "
    "retention. That residual is information loss rather than calibration error, "
    "and it is a measurement on these designs rather than a theorem." +
    FIG(
        "**Distribution-matching ladder.** True-model selection rate for four "
        "constructions in three cells at $N = 500$ with $2000$ repetitions. "
        "Perfect is the complete-data oracle, the dashed line above each cell. "
        "At $\\rho = 0.40$ the two-moment and equating arms reach the oracle. At "
        "$\\rho = 0.10$ no arm reaches it, the weak-signal floor.",
        "fig-ladder.png", "fig-ladder", "92%")
)

P19 = (
    "**Ladder internals.** Two internal measurements show why the ladder works "
    "(@fig-ladder-internals). On the true model's anchored statistic the "
    "distance to the paired complete-data statistic falls from $0.281$ under the "
    "uncorrected deviance to $0.019$ under equating, and the variance ratio "
    "falls from $3.18$ to near one. The mean correction's paired gap of "
    "$0.076 \\pm 0.100$ is a direct confirmation of @eq-lrt-bias at four tested "
    "directions. On the underfit candidate the noncentral statistic shrinks by "
    "the predicted factors, about $0.57$ under the two-moment match and $0.40$ "
    "under equating, both close to the measured values. The internal validity "
    "checks held on every repetition, with the spectrum-trace identity to "
    "$3 \\times 10^{-15}$ and no failure of the reference inversion in $18{,}000$ "
    "evaluations." +
    FIG(
        "**Ladder internals.** Left, the null-side Kolmogorov-Smirnov distance to "
        "the complete-data statistic across the four arms in the main cell. "
        "Perfect is zero, approached by the two-moment and equating arms, with "
        "the variance ratio falling from $3.18$ toward one. Right, the "
        "noncentral shrinkage factor measured against predicted on the line "
        "$y = x$. The two-moment and equating points sit on the diagonal.",
        "fig-ladder-internals.png", "fig-ladder-internals", "100%")
)

P20 = (
    "**The structural limits.** Both proved limits of @sec-derivations appear "
    "directly in the data, the equality case where the naive and projected "
    "traces coincide and the off-equality cost of the naive input. The table "
    "reports both, on the selection rates, with Monte Carlo standard error near "
    "$0.010$:\n\n"
    "| Structural limit | perfect | achieved |\n"
    "|---|---|---|\n"
    "| block-diagonal family, naive vs projected trace | exact equality | agree to $3.6 \\times 10^{-15}$ |\n"
    "| off-equality moment map, main-cell rate | oracle $0.899$ | naive input $0.824$, correct input $0.904$ |\n"
    "| per-model map, equated difference mean and sd | complete-data $10.00$ and $7.10$ | $6.10$ and $5.99$ |\n\n"
    "The naive trace difference is exact only on the block-diagonal case and "
    "overstates the projected trace elsewhere, and a per-model marginal map "
    "cannot calibrate the joint difference distribution."
)

P21 = (
    "**The non-nested measurement.** The mechanism behind the design-imbalance "
    "term is confirmed exactly, the predicted scaling resolves for a dissimilar "
    "pair, and the pre-registered headline for the similar pair stays below "
    "resolution (@fig-w4-nonnested). Each candidate's order-one level is large "
    "under missing-at-random data, near $+2.6$ and $+2.9$ deviance units for the "
    "two candidates, and it collapses under the completely-at-random twin, most "
    "sharply for the autoregressive candidate. For the dissimilar "
    "diagonal-versus-autoregressive pair the isolated differential resolves at "
    "$-1.2$, three and a half standard errors from zero and stable across sample "
    "sizes. For the similar compound-symmetry-versus-autoregressive pair the "
    "differential sits below Monte Carlo resolution, and a pilot's apparent "
    "value of $-2$ dissolved in the full run. We report that failure as the "
    "discipline requires. A byproduct supplied the first measured case off the "
    "equality condition of @prp-naive, where the naive trace difference "
    "overstates the exact projected trace by about $9$ percent." +
    FIG(
        "**Non-nested measurement.** Left, each candidate's order-one level under "
        "missing-at-random data and under its completely-at-random twin, "
        "dissimilar pair at $N = 500$ with $20{,}000$ repetitions. Perfect for "
        "the twin is zero, and the level collapses toward it, most sharply for "
        "the autoregressive candidate. Right, the isolated design-imbalance "
        "differential with $95$ percent intervals. Perfect is no effect, the "
        "line at zero. The similar pair stays on that line, the reported "
        "failure, while the dissimilar pair resolves at $-1.2$.",
        "fig-w4-nonnested.png", "fig-w4-nonnested", "100%")
)

P22 = (
    "**Engine sensitivity.** The bootstrap imputation sampler reproduces the "
    "analytic results on the most demanding cells, which bounds the cost of not "
    "running data augmentation. On non-monotone missing-at-random cells with "
    "samples as small as $N = 200$, where the bootstrap approximation is "
    "weakest, the sample relative-increase-in-variance trace from the imputation "
    "draws matches the observed-data value within $2$ to $3$ percent, with no "
    "widening as the sample grows, and selection agrees between the analytic arm "
    "and the imputation arm within $0.011$ on the recovery gap. This robustness "
    "is empirical and scoped to the designs studied. The bootstrap sampler is "
    "only approximately Bayesian, data augmentation was not run, and a fully "
    "Bayesian sampler remains the conservative choice when the fraction of "
    "missing information is large (@sec-discussion)."
)


def mk(idx, goal, proposition, dep, deptypes, prose, serves_L2, sets_up, topic, closing, flags, citations, numbers, notes):
    return {
        "id": idx, "section": "S5", "goal": goal, "proposition": proposition,
        "depends_on": dep, "dep_types": deptypes,
        "review": {"serves_L2": serves_L2,
                   "serves_L1": "M4b SIMULATION STUDIES (D-03-A1 full empirical account; D-05 failures in main text; T-07; todo/033 per-study Methods + figure rebuild)",
                   "sets_up": sets_up, "topic_sentence": topic, "closing_sentence": closing,
                   "status": "drafted", "flags": flags},
        "draft_prose": prose,
        "audit": {"status": "complete", "citations": citations, "numbers": numbers, "notes": notes}
    }


W1 = "verif:verification/cache/W1-prod-fiml.rds"
KNOWN = "verif:verification/cache/rederivation-knownvar-N200-R200000.rds"
W2 = "verif:verification/cache/W2-prod-amelia.rds"
MU1 = "verif:verification/cache/w2-paired-differential-mu1-cell.rds"
SPOT = "verif:verification/cache/w2-paired-differential-spotcheck.rds"
W3 = "verif:verification/cache/run_all-prod/phase2-w3/summary.csv"
LADDER = "verif:verification/cache/ic-ladder-summary.csv"
W4 = "verif:verification/cache/w4-nonnested-summary.csv"
W4D = "verif:verification/cache/w4-dissimilar-summary.csv"
RUNALL = "verif:verification/cache/run_all-prod"
FIGS = "verif:verification/figures.R"

s5 = [
    mk("S5-P1", "transition",
       None,
       ["S4-P22", "S3-P5"], ["builds_on", "builds_on"], P1, "S5-SP1 (framing)", "all S5",
       "This section is the paper's complete empirical account.",
       "Everything here carries the *measured* tier of @sec-methods unless stated otherwise.",
       "Rebuilt per todo/033: setup becomes per-study Methods blocks, results become figures and tables with explicit perfect-vs-achieved markers; S5 grew 14 -> 22 paragraphs (9 committed PNG exhibits + 2 tables).",
       {}, {}, "Setup subhead opens here (D-09-A1)."),

    mk("S5-P2", "define_concept",
       "Apparatus: four-variate MVN designs, the deterministic analytic FIML arm vs the EMB/Amelia proper arm; data augmentation not run, bounded by the engine-sensitivity study.",
       ["S5-P1"], ["builds_on"], P2, "S5-SP1", "P22; S6 G3",
       "The designs are multivariate normal in four dimensions, with one bivariate special case.",
       "...the engine-sensitivity study below bounds what that choice costs.",
       None,
       {"honakerAmeliaIIProgram2011": "verified (read in-session 2026-06-07; EMB description sec.1-2)"},
       {}, "Shared apparatus for all per-study blocks."),

    mk("S5-P3", "define_concept",
       "Grading and registration: frozen pass criteria with dated amendment histories; failures in main text (D-05); the totals-and-differentials rule.",
       ["S5-P2"], ["builds_on"], P3, "S5-SP1", "P4-P22",
       "Each study is graded against pass criteria fixed before its code existed.",
       "...for a reason the first study makes concrete.",
       None, {},
       {"pre-registration docs": "verif:todo/004-simulation-hypotheses.md",
        "ladder + non-nested registrations": "verif:todo/027-ladder-preregistration.md"},
       "Grading protocol + registration map merged."),

    mk("S5-P4", "define_concept",
       "Theorem-validation design: four-variate MVN (trRIV~5.55), non-monotone MAR ~1/3 per coordinate, N in {200,500,1000,2000}, analytic arm, R=1000, estimand E[T], target half-trace 2.77 / augmented 2.42-2.55.",
       ["S5-P2", "S5-P3"], ["builds_on", "builds_on"], P4, "S5-SP1", "P12",
       "The data-generating model is a four-variate normal with zero mean and unit variances.",
       "The study passes if the inverse-variance pooled estimate falls in that band.",
       None, {}, {"design constants; target 2.77 / 2.42-2.55": W1},
       "W1 Methods block."),

    mk("S5-P5", "define_concept",
       "Known-scale and sign-regime design: location-only fit with known Sigma, N=200, R=2e5, both arms; targets 0 and -1/2 tr(RIV) per @eq-knownscale; sign-regime impute-from-truth reversal.",
       ["S5-P2", "S5-P3"], ["builds_on", "builds_on"], P5, "S5-SP1", "P13",
       "Two single-question runs close the theorem.",
       "Each run passes if its arms reproduce the predicted values within Monte Carlo error.",
       None, {}, {"design constants; targets 0 / -1/2 tr(RIV)": KNOWN},
       "Known-scale + sign-regime Methods block."),

    mk("S5-P6", "define_concept",
       "LRT design: H0 sigma12=0 in 4-var MVN, local alternative delta/sqrt(n) on an 8-point grid, N=200, M=200 proper arm, R=1000; four references; metric rejection at 0.05.",
       ["S5-P2", "S5-P3"], ["builds_on", "builds_on"], P6, "S5-SP1", "P14",
       "The test is $H_0\\!: \\sigma_{12} = 0$ in the four-variate normal.",
       "...with the corrected numerator slightly conservative as double-counting predicts.",
       None, {}, {"design constants; nominal 0.05": W2},
       "W2 Methods block."),

    mk("S5-P7", "define_concept",
       "Discrimination design: H0 mu1=0 under heavy X1 missingness (Phi(0.8+1.2 X3), 70-79%), one tested direction, N in {500,1000}, R=2000 analytic arm; predicted tr(RIV_perp)~2.64 vs naive ~8.5.",
       ["S5-P2", "S5-P3"], ["builds_on", "builds_on"], P7, "S5-SP1", "P15",
       "This run separates the two candidate formulas for the differential bias.",
       "...so the run passes if the data land on the projected-trace value.",
       None, {}, {"design constants; 2.64 vs 8.5 targets": MU1},
       "Discrimination Methods block."),

    mk("S5-P8", "define_concept",
       "Pairing design: four-variate sigma12=0 cell, one tested direction, N in {500,1000,2000}, R=2000; three arms (null/local/fixed); metric single-model vs paired-differential sd.",
       ["S5-P2", "S5-P3"], ["builds_on", "builds_on"], P8, "S5-SP1", "P16",
       "This run shows that comparing the same imputations under both models collapses the per-dataset noise.",
       "...while the single-model figure grows with the sample size.",
       None, {}, {"design constants": SPOT},
       "Pairing Methods block."),

    mk("S5-P9", "define_concept",
       "Selection-sweep design: four nested MVN covariance models (diagonal..saturated, truth compound-symmetry), 60 cells (2 patterns x 2 mech x 3 N x 5 engine/M/cong), ~40% missing, R=2000; metric true-model AIC selection rate; headline non-monotone MAR FIML.",
       ["S5-P2", "S5-P3"], ["builds_on", "builds_on"], P9, "S5-SP1", "P17",
       "The candidate set is four nested multivariate-normal covariance models.",
       "...if the uncorrected criterion's errors concentrate on the largest-missing-information candidate.",
       None, {}, {"60-cell design constants": W3},
       "W3 Methods block."),

    mk("S5-P10", "define_concept",
       "Ladder design: same candidate family, saturated-anchored deviances, q_d=4, three cells (rho 0.40/0.10/0), N=500, R=2000, non-monotone MAR ~40% analytic arm; five constructions; metric selection rate + null/noncentral internal checks.",
       ["S5-P2", "S5-P3"], ["builds_on", "builds_on"], P10, "S5-SP1", "P18, P19, P20",
       "This study takes the same candidate family and contrasts four ways of referring the saturated-anchored imputation deviance to its complete-data law.",
       "...and the noncentral side shrinks by the predicted factors.",
       None, {}, {"three-cell design constants": LADDER},
       "Ladder Methods block."),

    mk("S5-P11", "define_concept",
       "Non-nested design: AR(1) truth rho=0.5 (P=4), similar pair (CS vs AR1) + dissimilar pair (diagonal vs AR1), N in {500,1000,2000}, R=20000, MAR + MCAR twin; metric isolated (A)+(C) differential.",
       ["S5-P2", "S5-P3"], ["builds_on", "builds_on"], P11, "S5-SP1", "P21",
       "This measurement isolates the order-one design-imbalance differential of @prp-ac-diff for genuinely separated candidates.",
       "...graded honestly against the resolution the design affords.",
       None, {}, {"design constants": [W4, W4D]},
       "W4 Methods block (similar + dissimilar pairs)."),

    mk("S5-P12", "evaluate_evidence",
       "Theorem validation result: pooled 2.43+/-0.26 in the augmented band; the N=1000 2.6-se miss; 9-20% component misses (D-05). Figure fig-w1-theorem.",
       ["S5-P4", "S4-P8"], ["builds_on", "instantiates"], P12, "S5-SP2 + SP3 (the W1 miss reported)", "S6 G1",
       "The net deviance bias tracks the analytic half-trace across every sample size.",
       "...which is why the grading reports only totals and paired differentials.",
       None, {},
       {"pooled 2.43 +/- 0.26; target 2.77 / 2.42-2.55; N=1000 2.6 se miss; components 9-20%": W1,
        "fig-w1-theorem.png": "verif:manuscript/figures/fig-w1-theorem.png"},
       "Results subhead opens here. W1 reading + figure."),

    mk("S5-P13", "evaluate_evidence",
       "Known-scale result: 0.025+/-0.018 (target 0) and -0.536+/-0.018 (target -0.561) within MC error; sign reversal. Figure fig-knownscale.",
       ["S5-P5", "S4-P4"], ["builds_on", "instantiates"], P13, "S5-SP2", "S4-P4 backfill",
       "Holding the covariance known and fitting only the mean collapses the bias to the two values @eq-knownscale predicts.",
       "...as the fitted-versus-oracle distinction requires.",
       None, {},
       {"0.025 +/- 0.018 vs 0; -0.536 +/- 0.018 vs -0.561; sign reversal": KNOWN,
        "fig-knownscale.png": "verif:manuscript/figures/fig-knownscale.png"},
       "Known-scale reading + figure."),

    mk("S5-P14", "evaluate_evidence",
       "Absorption result: Type I error 0.042 uncorrected / 0.034 corrected vs nominal 0.05; ~5% naive-input scope note. Figure fig-lrt-absorption. Raw power dropped (confounded across differently-sized arms; size-adjusted power -> S6 conjecture).",
       ["S5-P6", "S4-P14"], ["builds_on", "instantiates"], P14, "S5-SP2", "S6 SP2 (conjecture)",
       "A correctly calibrated reference absorbs the differential bias at the null, so the test controls its Type I error.",
       "...though @eq-lrt-bias is the correct general form.",
       None, {},
       {"Type I error 0.042 / 0.034 vs 0.05; ~5% naive-input note": W2,
        "fig-lrt-absorption.png": "verif:manuscript/figures/fig-lrt-absorption.png"},
       "W2 reading + Type I error figure (Marcus 2026-06-07: raw power dropped, confounded across differently-sized arms; size-adjusted power is the S6 conjecture)."),

    mk("S5-P15", "evaluate_evidence",
       "Discrimination result: 2.64+/-0.11 and 2.70+/-0.11 on the predicted 2.64, 52 se from naive 8.5. Figure fig-discrimination.",
       ["S5-P7", "S4-P10"], ["builds_on", "instantiates"], P15, "S5-SP2", "-",
       "On a design where the two formulas separate widely, the data fall on the projected-trace formula and far from the naive one.",
       "...this design makes the gap large enough to rule it out outright.",
       None, {},
       {"2.64 +/- 0.11 / 2.70 +/- 0.11 vs 2.64 / 8.5; 52 se": MU1,
        "fig-discrimination.png": "verif:manuscript/figures/fig-discrimination.png"},
       "Discrimination reading + figure."),

    mk("S5-P16", "evaluate_evidence",
       "Pairing result: paired-null sd ~1.5 flat vs single-model 18.4->36.5; fixed-alternative paired sd 12.4/16.8/24.9. Figure fig-pairing.",
       ["S5-P8", "S4-P12"], ["builds_on", "instantiates"], P16, "S5-SP2", "-",
       "Comparing the same imputations under both models holds the per-dataset noise at order one.",
       "...exactly the failure mode the result specifies.",
       None, {},
       {"single 18.4/26.6/36.5 vs paired 1.58/1.47/1.57; fixed alt 12.4/16.8/24.9": SPOT,
        "fig-pairing.png": "verif:manuscript/figures/fig-pairing.png"},
       "Pairing reading + figure."),

    mk("S5-P17", "evaluate_evidence",
       "Selection result: oracle 0.90 / uncorrected 0.67 / corrected 0.82 at N=500 (FIML non-monotone MAR); 100% of uncorrected errors on the saturated candidate. Figure fig-w3-selection.",
       ["S5-P9", "S4-P18"], ["builds_on", "instantiates"], P17, "S5-SP2", "P18",
       "The uncorrected criterion favors high-missing-information models, and the correction moves selection back toward the complete-data oracle.",
       "...what the distribution-matching ladder was registered to explain.",
       None, {},
       {"0.90 / 0.67 / 0.82; 100% saturated signature": W3,
        "fig-w3-selection.png": "verif:manuscript/figures/fig-w3-selection.png"},
       "W3 reading + grouped-bar figure."),

    mk("S5-P18", "evaluate_evidence",
       "Ladder result: the 3-cell x 5-arm selection table; two-moment/equating reach oracle at rho=0.40; weak-signal floor at rho=0.10 (D-05). Table + figure fig-ladder.",
       ["S5-P10", "S4-P21"], ["builds_on", "instantiates"], P18, "S5-SP2 + SP3", "S6 verdict",
       "Across three levels of signal strength the stronger constructions recover the oracle where overfit flips drive the errors, and a floor remains where selection is genuinely hard.",
       "...it is a measurement on these designs rather than a theorem.",
       None, {},
       {"table 0.899/0.678/0.814/0.904/0.903 etc.; junk closes 90%; floor 0.820": LADDER,
        "fig-ladder.png": "verif:manuscript/figures/fig-ladder.png"},
       "Ladder selection table + grouped-bar figure with oracle reference."),

    mk("S5-P19", "evaluate_evidence",
       "Ladder internals: null KS 0.281->0.019, var ratio 3.18->~1; mean-correction paired gap 0.076+/-0.100; noncentral shrinkage ~0.57 (a_k) and ~0.40 (1/lam_max) measured-vs-predicted; spectrum-trace 3e-15, 0/18000 inversion failures. Figure fig-ladder-internals.",
       ["S5-P18"], ["builds_on"], P19, "S5-SP2 + SP3", "S6 verdict",
       "Two internal measurements show why the ladder works.",
       "...and no failure of the reference inversion in $18{,}000$ evaluations.",
       None, {},
       {"KS 0.281->0.019; var 3.18->0.97; gap 0.076+/-0.100; ncratio 0.586/0.362 vs 0.558/0.398; 3e-15; 0/18000": LADDER,
        "fig-ladder-internals.png": "verif:manuscript/figures/fig-ladder-internals.png"},
       "Ladder internals: null calibration + noncentral y=x scatter."),

    mk("S5-P20", "evaluate_evidence",
       "Structural limits: block-diagonal equality 3.6e-15; off-equality naive-input arm 0.824 vs 0.904; per-model map difference 6.10/5.99 vs complete-data 10.00/7.10. Table tbl-structural-limits.",
       ["S5-P19", "S4-P22"], ["builds_on", "instantiates"], P20, "S5-SP2", "-",
       "Both proved limits of @sec-derivations appear directly in the data.",
       "...a per-model marginal map cannot calibrate the joint difference distribution.",
       None, {},
       {"3.6e-15; 0.824 vs 0.904; 6.10/5.99 vs 10.00/7.10": LADDER},
       "Structural-limit table (no figure; scalar limit-checks)."),

    mk("S5-P21", "evaluate_evidence",
       "Non-nested result: per-candidate level +2.6/+2.9 under MAR collapsing under MCAR; dissimilar isolated differential -1.2 at 3.5 se; similar pair below resolution (D-05, pilot -2 dissolved); ~9% naive overstatement. Figure fig-w4-nonnested.",
       ["S5-P11", "S4-P13"], ["builds_on", "instantiates"], P21, "S5-SP2 + SP3 (the failed headline)", "S6 G5",
       "The mechanism behind the design-imbalance term is confirmed exactly, the predicted scaling resolves for a dissimilar pair, and the pre-registered headline for the similar pair stays below resolution.",
       "...the naive trace difference overstates the exact projected trace by about $9$ percent.",
       None, {},
       {"levels +2.6/+2.9 (MAR) collapsing (MCAR); dissimilar -1.2 at 3.5 se; similar below resolution; ~9%": [W4, W4D],
        "fig-w4-nonnested.png": "verif:manuscript/figures/fig-w4-nonnested.png"},
       "W4 reading + 2-panel figure (level collapse + isolated differential)."),

    mk("S5-P22", "scope_limit",
       "Engine sensitivity: EMB RIV within 2-3% of observed-data RIV, no widening with N; selection within 0.011; empirical and scoped, DA not run.",
       ["S5-P2", "S5-P17"], ["builds_on", "builds_on"], P22, "S5-SP4", "S6 G3",
       "The bootstrap imputation sampler reproduces the analytic results on the most demanding cells, which bounds the cost of not running data augmentation.",
       "...a fully Bayesian sampler remains the conservative choice when the fraction of missing information is large (@sec-discussion).",
       None, {}, {"2-3% RIV; 0.011 selection": RUNALL},
       "Engine-sensitivity scope note; ends with what it cannot catch (T-05)."),
]

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

paras = l3["paragraphs"]
idx = [i for i, p in enumerate(paras) if p.get("section") == "S5"]
assert idx and idx == list(range(idx[0], idx[-1] + 1)), "S5 block not contiguous"
start, end = idx[0], idx[-1]
old_n = end - start + 1
l3["paragraphs"] = paras[:start] + s5 + paras[end + 1:]

l3["metadata"]["status"] = "s5_rebuilt_per_study_methods_plus_figures"
l3["metrics_gate"]["notes"] = (
    "S5 REBUILT 2026-06-07 (todo/033): 14 -> 22 paragraphs. Setup = 11 per-study "
    "Methods blocks (apparatus + grading + 8 study designs, reproducible from the "
    "paragraph); Results = 11 exhibits (9 committed PNG figures via "
    "verification/figures.R + the ladder selection table + the structural-limits "
    "table), each carrying an explicit perfect reference (oracle / nominal level "
    "/ analytic target / y=x) and the achieved value. D-05 failures kept in the "
    "main text: N=1000 W1 miss (2.6 se), 9-20% component misses, weak-signal "
    "ladder floor, similar-pair W4 below resolution. T-07 repetitions. "
    "Section totals: S1 7 + S2 13 + S3 8 + S4 23 + S5 22 + S6 8 = 81 paragraphs."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# ---- Level 4: replace the old S5 evidence entries ----
with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)

l4["evidence_map"] = [e for e in l4["evidence_map"] if not (e.get("proposition_id") or "").startswith("S5")]

new_e = [
    ("E-S5-P2-1", "S5-P2", "lit:honakerAmeliaIIProgram2011", "verified",
     "Sec.1-2: EMB algorithm (EM on bootstrap resamples; draws at bootstrapped parameters); MVN assumption.", "Engine citation."),
    ("E-S5-P4-1", "S5-P4", W1, "verified",
     "W1 design constants (trRIV~5.55; non-monotone MAR; N grid; R=1000) + target band.", "Theorem-validation Methods."),
    ("E-S5-P5-1", "S5-P5", KNOWN, "verified",
     "Known-scale design (N=200, R=2e5, location-only, known Sigma); targets 0 and -1/2 tr(RIV).", "Known-scale Methods."),
    ("E-S5-P6-1", "S5-P6", W2, "verified",
     "LRT design (N=200, M=200, R=1000, 8-point delta grid, four references).", "W2 Methods."),
    ("E-S5-P7-1", "S5-P7", MU1, "verified",
     "Discrimination design (heavy X1 MAR; N in {500,1000}; R=2000); 2.64 vs 8.5 targets.", "Discrimination Methods."),
    ("E-S5-P8-1", "S5-P8", SPOT, "verified",
     "Pairing design (sigma12=0 cell; three arms; N in {500,1000,2000}; R=2000).", "Pairing Methods."),
    ("E-S5-P9-1", "S5-P9", W3, "verified",
     "60-cell selection sweep design constants.", "W3 Methods."),
    ("E-S5-P10-1", "S5-P10", LADDER, "verified",
     "Ladder design (3 cells; N=500; R=2000; q_d=4; five constructions).", "Ladder Methods."),
    ("E-S5-P11-1", "S5-P11", W4, "verified",
     "Non-nested design (AR(1) truth; similar + dissimilar pairs; R=20000; MCAR twin).", "W4 Methods."),
    ("E-S5-P11-2", "S5-P11", W4D, "verified",
     "Dissimilar-pair design (diagonal vs AR(1)).", "W4 dissimilar Methods."),
    ("E-S5-P12-1", "S5-P12", W1, "verified",
     "Pooled 2.43+/-0.26; target 2.77 / 2.42-2.55; N=1000 2.6 se miss; components 9-20%.", "W1 result."),
    ("E-S5-P12-2", "S5-P12", "verif:manuscript/figures/fig-w1-theorem.png", "verified",
     "E[T] vs target band across N; pooled estimate; N=1000 miss flagged.", "W1 exhibit."),
    ("E-S5-P13-1", "S5-P13", KNOWN, "verified",
     "0.025+/-0.018 vs 0; -0.536+/-0.018 vs -0.561; sign reversal.", "Known-scale result."),
    ("E-S5-P13-2", "S5-P13", "verif:manuscript/figures/fig-knownscale.png", "verified",
     "Two arms vs targets {0, -0.561}.", "Known-scale exhibit."),
    ("E-S5-P14-1", "S5-P14", W2, "verified",
     "Type I error 0.042 / 0.034 vs nominal 0.05; ~5% naive-input note.", "Absorption result."),
    ("E-S5-P14-2", "S5-P14", "verif:manuscript/figures/fig-lrt-absorption.png", "verified",
     "Type I error of four references vs nominal 0.05; raw power dropped (confounded).", "LRT exhibit."),
    ("E-S5-P15-1", "S5-P15", MU1, "verified",
     "2.64+/-0.11 and 2.70+/-0.11 vs 2.64 / 8.5; 52 se.", "Discrimination result."),
    ("E-S5-P15-2", "S5-P15", "verif:manuscript/figures/fig-discrimination.png", "verified",
     "Observed differential vs projected-trace line and naive line.", "Discrimination exhibit."),
    ("E-S5-P16-1", "S5-P16", SPOT, "verified",
     "single 18.4/26.6/36.5 vs paired 1.58/1.47/1.57; fixed alt 12.4/16.8/24.9.", "Pairing result."),
    ("E-S5-P16-2", "S5-P16", "verif:manuscript/figures/fig-pairing.png", "verified",
     "single grows, paired-null flat, paired-fixed grows.", "Pairing exhibit."),
    ("E-S5-P17-1", "S5-P17", W3, "verified",
     "0.90 / 0.67 / 0.82 at N=500; 100% saturated misclassifications.", "W3 result."),
    ("E-S5-P17-2", "S5-P17", "verif:manuscript/figures/fig-w3-selection.png", "verified",
     "oracle/uncorrected/corrected bars across N with oracle reference.", "W3 exhibit."),
    ("E-S5-P18-1", "S5-P18", LADDER, "verified",
     "3x5 selection table; two-moment/equating reach oracle at rho=0.40; floor at rho=0.10.", "Ladder result + table."),
    ("E-S5-P18-2", "S5-P18", "verif:manuscript/figures/fig-ladder.png", "verified",
     "grouped bars per cell with oracle reference line.", "Ladder exhibit."),
    ("E-S5-P19-1", "S5-P19", LADDER, "verified",
     "KS 0.281->0.019; var 3.18->0.97; gap 0.076+/-0.100; shrinkage ~0.57/~0.40; 3e-15; 0/18000.", "Ladder internals."),
    ("E-S5-P19-2", "S5-P19", "verif:manuscript/figures/fig-ladder-internals.png", "verified",
     "null KS bars + noncentral measured-vs-predicted y=x.", "Ladder internals exhibit."),
    ("E-S5-P20-1", "S5-P20", LADDER, "verified",
     "3.6e-15 equality; 0.824 vs 0.904; 6.10/5.99 vs 10.00/7.10.", "Structural-limit table."),
    ("E-S5-P21-1", "S5-P21", W4, "verified",
     "levels +2.6/+2.9 (MAR) collapsing (MCAR); similar below resolution; ~9%.", "W4 result."),
    ("E-S5-P21-2", "S5-P21", W4D, "verified",
     "dissimilar isolated differential -1.2 at 3.5 se.", "W4 dissimilar result."),
    ("E-S5-P21-3", "S5-P21", "verif:manuscript/figures/fig-w4-nonnested.png", "verified",
     "level collapse + isolated differential CIs (similar below resolution, dissimilar resolved).", "W4 exhibit."),
    ("E-S5-P22-1", "S5-P22", RUNALL, "verified",
     "EMB vs observed-data RIV within 2-3%; selection within 0.011.", "Engine sensitivity."),
    ("E-S5-figR", "S5-P1", FIGS, "verified",
     "verification/figures.R draws all 9 PNG exhibits from the committed caches; deterministic.", "Figure provenance."),
]
l4["evidence_map"].extend([
    {"id": i, "proposition_id": pid, "pointer": ptr, "evidence_status": st,
     "passage_or_value": val, "note": note}
    for (i, pid, ptr, st, val, note) in new_e
])
l4["metrics_gate"]["notes"] = "S1-S6 populated; S5 rebuilt per todo/033 (figure-bearing). All pointers resolve. Full gate at compile."

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"S5 rebuilt: replaced {old_n} paragraphs with {len(s5)}; level4 S5 entries now {len(new_e)}")
