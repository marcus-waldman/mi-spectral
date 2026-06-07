# S4 Derivations - from-scratch draft (D-12), 2026-06-07
#
# Fourth Level-3 drafting cycle, under the approved S4 blueprint (a21120a +
# cycle-1 repairs: entropy-plug-in tail on SP1, SP5b absorption, SP7 + I7 limits).
# Three subsections, each opening with the replication-principle level it
# addresses (SP8): (a) setup and main theorem -> criterion replication;
# (b) likelihood-ratio comparison -> decision rates for testing;
# (c) information-criterion selection -> decision rates for selection.
# Quarried from 180e2b5 sec-setup/sec-lrt/sec-ic (displays, propositions, and
# numbers verbatim; prose REWRITTEN to the CLAUDE.md style: use-first openers,
# plain cadence, punctuation budget, results announced, trust-tier labels from
# S3-P4). Headline numbers inline per D-03; proofs in the companion per D-08.
# 22 paragraphs: A1-A8 (setup+theorem), B1-B7 (LRT), C1-C7 (IC).

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

PA1 = (
    "This section delivers the paper's analytic results, in three parts. The first part "
    "states the main theorem, which is the answer to the replication principle's second "
    "level: it prices the bias of the averaged log-likelihood exactly, so the criterion "
    "can be restored to its complete-data expectation. The second and third parts take "
    "up the third level, decision rates, for testing and for selection in turn. Every "
    "claim carries one of the four tier labels defined in @sec-methods. Full proofs are "
    "in the companion document. Headline numbers are quoted where the claims are made, "
    "and the studies behind them are reported in @sec-simulations."
)

PA2 = (
    "## Setup and main theorem\n\n"
    "The theorem is stated for a general regular likelihood with an estimated scale or "
    "covariance and is instantiated in the multivariate normal family. Let "
    "$Y \\in \\mathbb{R}^{N \\times p}$ collect $N$ independent rows "
    "$Y_i \\sim \\mathcal{N}_p(\\mu, \\Sigma)$ with estimand "
    "$\\theta = (\\mu, \\operatorname{vech}\\Sigma)$ of dimension "
    "$k = p + \\tfrac12 p(p+1)$. Missingness is ignorable throughout. The two "
    "estimators of @sec-background take concrete form here. The complete-data maximizer "
    "$\\hat\\theta_{\\text{com}}$ is the target an analyst with full data would have "
    "reached. The observed-data maximizer $\\hat\\theta_{\\text{obs}}$ sums each row's "
    "marginal density over its observed coordinates "
    "[@schaferAnalysisIncompleteMultivariate1997] and is the best available from the "
    "data at hand. The scope of the normal instantiation is taken up in @sec-discussion."
)

PA3 = (
    "The RIV of @eq-bg-riv is instantiated with one convention fixed and one warning "
    "repeated. In this family\n"
    "$$ \\mathrm{RIV} \\;=\\; I_{\\text{obs}}^{-1}\\, I_{\\text{mis}\\mid\\text{obs}} "
    "\\;=\\; I_{\\text{obs}}^{-1} I_{\\text{com}} - I_k, \\qquad "
    "\\operatorname{tr}(\\mathrm{RIV}) = \\operatorname{tr}(I_{\\text{obs}}^{-1} "
    "I_{\\text{com}}) - k. $$ {#eq-riv}\n"
    "Under congenial proper MI with $m \\to \\infty$, Rubin's rules give "
    "$\\bar U_\\infty = I_{\\text{com}}^{-1}$ and $T_\\infty = I_{\\text{obs}}^{-1}$, "
    "so this matrix is exactly Rubin's $r_\\infty$ in matrix form. The convention: "
    "under MAR the expectation defining $I_{\\text{obs}}$ is taken unconditionally over "
    "data and pattern jointly, as @kenwardLikelihoodBasedFrequentist1998 require, and "
    "the resulting information carries their mean-covariance cross term. Computed this "
    "way there is a single RIV, and both bias terms of the theorem calibrate to it. An "
    "earlier reading of our own simulation output, in which the two terms appeared to "
    "attach to two different RIVs, was an artifact of grading against the naive "
    "block-diagonal information. The warning repeats @sec-background in local form: the "
    "fraction-of-missing-information matrix "
    "$D = I_{\\text{com}}^{-1} I_{\\text{mis}\\mid\\text{obs}}$ "
    "[@schaferAnalysisIncompleteMultivariate1997] has the same trace ingredients but "
    "the other normalization, the two relate by "
    "$D = (I_k + \\mathrm{RIV})^{-1}\\mathrm{RIV}$, and substituting one for the other "
    "changes every constant below."
)

PA4 = (
    "The object of the theorem is the infinite-imputation Q-function, and its "
    "definition contains the choice that fixes the sign of everything that follows. "
    "Under congenial proper MI the imputation parameter $\\tilde\\phi$ is a draw from "
    "the imputation posterior fit to $Y_{\\text{obs}}$. Under deterministic FIML "
    "imputation it collapses to the point value $\\hat\\theta_{\\text{obs}}$. Each "
    "completion is drawn at $\\tilde\\phi$, and\n"
    "$$ \\bar Q_\\infty(\\theta) \\;:=\\; \\lim_{M\\to\\infty} \\frac1M "
    "\\sum_{l=1}^{M} \\ell_{\\text{com}}\\big(\\theta;\\, Y_{\\text{obs}}, "
    "\\tilde Y_{\\text{mis}}^{(l)}\\big) \\;=\\; \\mathbb{E}_{\\tilde\\phi}\\, "
    "\\mathbb{E}_{Y_{\\text{mis}} \\mid Y_{\\text{obs}}, "
    "\\tilde\\phi}\\big[\\ell_{\\text{com}}(\\theta)\\big]. $$ {#eq-qbar}\n"
    "The inner expectation conditions on the fitted or drawn parameter, exactly as the "
    "EM E-step conditions on the current iterate. It does not condition on the truth. "
    "This is the fork that @sec-methods reported as the sign episode, and both branches "
    "are stated here to prevent the standard confusion. Were $\\bar Q_\\infty$ instead "
    "the oracle expectation $\\mathbb{E}[\\ell_{\\text{com}}(\\theta) \\mid "
    "Y_{\\text{obs}}]$ under the data-generating law, the tower property would force "
    "the imputation-bias term to zero and the total bias would be "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$, with the opposite sign. The analyst "
    "imputes from a model fit to the data, not from an oracle. Both regimes were "
    "confirmed by direct simulation: imputing from the truth drives the imputation bias "
    "to zero, and imputing from the fitted model produces the constants of the theorem "
    "(@sec-simulations)."
)

PA5 = (
    "The bias is split at the pivot $\\hat\\theta_{\\text{obs}}$ into two terms with "
    "distinct mechanisms,\n"
    "$$ T \\;=\\; \\underbrace{\\big[\\bar Q_\\infty(\\hat\\theta_{\\text{obs}}) - "
    "\\ell_{\\text{com}}(\\hat\\theta_{\\text{obs}})\\big]}_{A:\\ \\text{imputation "
    "bias}} \\;+\\; \\underbrace{\\big[\\ell_{\\text{com}}(\\hat\\theta_{\\text{obs}}) "
    "- \\ell_{\\text{com}}(\\hat\\theta_{\\text{com}})\\big]}_{B:\\ \\text{estimation "
    "mismatch}}, $$ {#eq-split}\n"
    "on the log-likelihood scale. Deviance-scale statements double everything. Seven "
    "regularity conditions are in force and none is exotic. R1 and R2 are smoothness "
    "and positive-definite information [@vaartAsymptoticStatistics1998a]. R3 is "
    "ignorability [@rubinInferenceMissingData1976b]. R4 through R6 are congeniality, "
    "properness, and self-efficiency [@mengMultipleImputationInferencesUncongenial1994a; "
    "@rubinMultipleImputationNonresponse1987]. R7 is the infinite-imputation "
    "idealization, with Rubin's finite-$m$ corrections applying otherwise. Together "
    "they deliver the variance-recovery property "
    "$T_\\infty = I_{\\text{obs}}^{-1}$ that identifies @eq-riv with $r_\\infty$."
)

PA6 = (
    "::: {#thm-bias}\n"
    "## Q-function deviance bias\n\n"
    "Under R1-R7, for a model that estimates a scale or covariance, to leading order\n"
    "$$ \\mathbb{E}[T] \\;=\\; +\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) \\;+\\; "
    "\\big[(A)+(C)\\big] \\;+\\; O(n^{-1}), $$ {#eq-thm}\n"
    "decomposing as $\\mathbb{E}[A] = +\\operatorname{tr}(\\mathrm{RIV}) + [(A)+(C)] + "
    "O(n^{-1})$ and $\\mathbb{E}[B] = -\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) + "
    "O(n^{-1})$. The design-imbalance term $(A)+(C)$ vanishes under MCAR and is a "
    "nonzero $O(1)$ under MAR.\n"
    ":::\n\n"
    "The theorem is firm in the sense of @sec-methods. Term $B$ is an elementary Taylor "
    "argument. Expanding $\\ell_{\\text{com}}$ about its own maximizer kills the "
    "first-order term, and the variance that enters the second-order term is the "
    "variance of the estimator gap,\n"
    "$$ \\operatorname{Var}\\big(\\hat\\theta_{\\text{obs}} - "
    "\\hat\\theta_{\\text{com}}\\big) \\;=\\; I_{\\text{obs}}^{-1} - "
    "I_{\\text{com}}^{-1}, $$ {#eq-vargap}\n"
    "which follows from the conditional-score form of the missing-information "
    "principle. Substituting and reducing the trace gives "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$. One trap is worth naming. "
    "Substituting $\\operatorname{Var}(\\hat\\theta_{\\text{obs}})$ for the variance of "
    "the gap produces a spurious $-\\tfrac12 k$, and @eq-vargap is displayed to "
    "forestall it."
)

PA7 = (
    "Term $A$ is the delicate half. Factoring the complete-data log-likelihood as "
    "$\\ell_{\\text{obs}} + \\log P(Y_{\\text{mis}} \\mid Y_{\\text{obs}}, \\theta)$ "
    "cancels the observed parts, and a second-order expansion in $\\tilde\\phi$ leaves "
    "three pieces. The main cross term pairs the imputation error with the estimation "
    "error through $I_{\\text{mis}\\mid\\text{obs}}$ and contributes the leading "
    "$+\\operatorname{tr}(\\mathrm{RIV})$. The piece labeled $(A)$ pairs the bias of "
    "$\\tilde\\phi$ with the gradient of the conditional missing-data entropy. The "
    "piece labeled $(C)$ pairs the variance of $\\tilde\\phi$ with the curvature of "
    "the conditional cross-entropy. The entropy gradient is not zero. A tempting appeal "
    "to Gibbs' inequality fails, because the gradient varies the sampling distribution "
    "of the completions rather than the evaluation point of the log-density, and for "
    "the normal family it is supported entirely on the covariance parameters. The "
    "leading parts of $(A)$ and $(C)$ cancel exactly when the missing and observed "
    "units share a conditioning-variable distribution, which is MCAR. Under MAR their "
    "sum is the design-imbalance term, with bivariate monotone closed form\n"
    "$$ (A)+(C) \\;=\\; \\frac{n_{\\text{mis}}}{n_{\\text{obs}}} \\Big[\\, 1 - "
    "\\tfrac12 \\operatorname{tr}\\big(Q_{\\text{mis}} Q_{\\text{obs}}^{-1}\\big) "
    "\\Big] + O(n^{-1}), $$ {#eq-ac}\n"
    "zero exactly when the two conditioning-variable distributions agree. Three "
    "statements about $(A)+(C)$ have different standing, and the labels of "
    "@sec-methods keep them separate. Firm: its structure, sign, $O(1)$ order, MCAR "
    "vanishing, the closed form @eq-ac, and the information convention. Measured but "
    "imprecise: its absolute magnitude, because the per-replicate statistic is "
    "heavy-tailed and direct estimates scatter without trend around the analytic "
    "leading-order value. Structural: comparisons touch $(A)+(C)$ only through "
    "differences across candidates fit to the same imputations, and the differential "
    "is derived and measured precisely in the next part."
)

PA8 = (
    "Two checks close the theorem, one on its scope and one on its form. The scope "
    "check is the known-scale collapse. With a known scale and a location-only fit the "
    "conditional missing-data entropy is parameter-free, and the net bias collapses to\n"
    "$$ \\mathbb{E}[T]_{\\text{known scale}} \\;=\\; \\begin{cases} 0 & "
    "\\text{deterministic FIML}, \\\\[2pt] "
    "-\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) & \\text{proper MI}, \\end{cases} "
    "$$ {#eq-knownscale}\n"
    "the two arms differing by exactly the posterior-draw imputation variance of "
    "@sec-background's proper-imputation paragraph. A dedicated experiment with "
    "$R = 2\\times10^5$ repetitions confirms all four values within 4%. Every model "
    "compared below estimates a covariance, so the applications sit in the "
    "estimated-scale regime. The form check is the entropy-plug-in reading. Writing "
    "$C_n(\\theta)$ for the conditional entropy of the missing block given the "
    "observed block, the bias @eq-thm equals the plug-in bias of evaluating $C_n$ at "
    "the estimate rather than the truth. One curvature identity, "
    "$\\nabla^2 C_n(\\theta_0) = H_{\\phi\\phi} + I_{\\text{mis}\\mid\\text{obs}}$, "
    "regroups the proof's three pieces into one expansion and delivers the known-scale "
    "collapse as the parameter-free special case. The total is convention-free, and "
    "both readings are verified symbolically and by simulation. The pre-registered "
    "Monte Carlo confirmation of @eq-thm pools to $\\hat T = 2.43 \\pm 0.26$ against "
    "the augmented target range $2.42$ to $2.55$ in the four-variate MAR design "
    "(@sec-simulations)."
)

PB1 = (
    "## Likelihood-ratio comparison\n\n"
    "This part takes up the replication principle's third level for testing. The "
    "theorem prices one model's bias. A likelihood-ratio comparison involves two such "
    "quantities on the same imputed data, and everything here follows from asking what "
    "survives the subtraction. Let the null model be a smooth submodel "
    "$\\theta = g(\\gamma)$ with full-rank Jacobian $G$ and $q_{\\mathrm{d}}$ tested "
    "constraints. Both models are fit to the same imputations, and the numerator is\n"
    "$$ \\hat d_L \\;=\\; 2\\big[\\bar Q_\\infty(\\hat\\psi^{*}) - "
    "\\bar Q_\\infty(\\hat\\psi_0^{*})\\big], $$ {#eq-dl}\n"
    "the infinite-$m$ limit of the maximize-then-average statistic of "
    "@chanMultipleImprovementsMultiple2022 restated in @sec-background. One definition "
    "matters here. The constrained fit $\\hat\\psi_0^{*}$ maximizes the shared "
    "$\\bar Q_\\infty$ over the null manifold. It is not the null model's own "
    "observed-data MLE. The complete-data counterpart has null expectation "
    "$q_{\\mathrm{d}} + O(n^{-1})$ by Wilks' theorem, and the object of interest is "
    "the differential."
)

PB2 = (
    "::: {#prp-lrt}\n"
    "## Differential bias at the null\n\n"
    "Under R1-R7, at the null,\n"
    "$$ \\mathbb{E}\\big[\\hat d_L - \\hat d_{\\text{com}}\\big] \\;=\\; "
    "\\operatorname{tr}(\\mathrm{RIV}_\\perp) + O(n^{-1}), $$ {#eq-lrt-bias}\n"
    "where $\\operatorname{tr}(\\mathrm{RIV}_\\perp)$ is the missing information of "
    "the tested directions, projected onto the null tangent space in the "
    "$I_{\\text{com}}$ metric.\n"
    ":::\n\n"
    "This result is firm. The metric is its substance. The score of $\\bar Q_\\infty$ "
    "at the truth has variance built from "
    "$I_{\\text{com}} I_{\\text{obs}}^{-1} I_{\\text{com}}$, while its curvature is "
    "$I_{\\text{com}}$, the geometric fact restated in @sec-background. The "
    "constrained fit therefore projects in the $I_{\\text{com}}$ metric, and taking "
    "expectations of the difference of quadratic forms gives @eq-lrt-bias. The natural "
    "error is to substitute $I_{\\text{obs}}$ for the curvature, which is the same as "
    "conflating $\\hat\\psi_0^{*}$ with the null model's own observed-data MLE. That "
    "error reproduces exactly the naive formula that the next proposition shows always "
    "overstates. The derivation was carried through three independent routes. On a "
    "four-variate design built to separate the two formulas, @eq-lrt-bias gives "
    "$2.64$ where the naive difference gives $8.47$, and the Monte Carlo mean lands on "
    "@eq-lrt-bias within sampling error, which is $52$ standard errors from the naive "
    "value (@sec-simulations)."
)

PB3 = (
    "::: {#prp-naive}\n"
    "## The naive difference always overstates\n\n"
    "With $\\operatorname{tr}(\\mathrm{RIV}_0)$ the null model's own self-contained "
    "trace correction, always\n"
    "$$ \\operatorname{tr}(\\mathrm{RIV}_\\perp) \\;\\le\\; "
    "\\operatorname{tr}(\\mathrm{RIV}) - \\operatorname{tr}(\\mathrm{RIV}_0), "
    "$$ {#eq-overstate}\n"
    "with equality if and only if $\\operatorname{col}(I_{\\text{obs}}^{1/2} G)$ is an "
    "invariant subspace of the standardized missing information.\n"
    ":::\n\n"
    "This result is firm, and the proof is one matrix inequality. The gap has an exact "
    "closed form. Partitioning the standardized missing information by retained "
    "against tested directions,\n"
    "$$ \\big[\\operatorname{tr}(\\mathrm{RIV}) - "
    "\\operatorname{tr}(\\mathrm{RIV}_0)\\big] - "
    "\\operatorname{tr}(\\mathrm{RIV}_\\perp) \\;=\\; "
    "\\operatorname{tr}\\big[(I + H_{11})^{-1} H_{12} H_{12}^\\top\\big] \\;\\ge\\; 0, "
    "$$ {#eq-gap}\n"
    "zero exactly when tested and retained directions carry independent missing "
    "information. Equal fractions of missing information is a special case of "
    "equality. The practical reading is direct. Correcting an MI deviance comparison "
    "by the difference of the two models' own traces over-corrects at the null "
    "whenever the tested directions mix unequally-missing information. The "
    "overstatement is about 5% in the pre-registered covariance-test design, which "
    "sits near the equality case. It is a factor above three in the $\\mu_1$ design "
    "above."
)

PB4 = (
    "::: {#prp-pairing}\n"
    "## Pairing collapses the noise\n\n"
    "Let $D$ be the per-dataset paired differential. At the null and under local "
    "alternatives, $\\operatorname{sd}(D) = O(1)$, against $O(\\sqrt n)$ for either "
    "level separately. At a fixed alternative the cancellation fails and "
    "$\\operatorname{sd}(D)$ reverts to $O(\\sqrt n)$.\n"
    ":::\n\n"
    "This result is firm, and the mechanism is exact cancellation of realizations "
    "rather than averaging. The large noise of each level lives in fit-independent "
    "realized constants. Both fits maximize the same realized $\\bar Q_\\infty$ built "
    "from the same imputation parameter, so these constants are identical in the two "
    "levels and cancel dataset by dataset. The measurement matches. At the null, the "
    "single-model standard deviation grows $18.4$, $26.6$, $36.5$ across "
    "$N = 500$, $1000$, $2000$, while the paired differential stays flat at $1.58$, "
    "$1.47$, $1.57$. At the fixed alternative the growth returns. This is why every "
    "comparison-relevant quantity in this paper is estimated by paired contrasts and "
    "never by differencing separately estimated levels."
)

PB5 = (
    "::: {#prp-ac-diff}\n"
    "## The design-imbalance differential cancels at the null\n\n"
    "The $(A)+(C)$ contributions of the two levels are properties of the imputation, "
    "not of which model is fit. At the null they are identical realizations and cancel "
    "exactly to leading order. Under local alternatives the differential is "
    "$O(n^{-1/2})$. It becomes a genuine $O(1)$ only when the candidates' pseudo-true "
    "values are separated at $O(1)$, the regime of @vuongLikelihoodRatioTests1989.\n"
    ":::\n\n"
    "Separation, not nesting, is the criterion. A nested but false restriction "
    "triggers the decoupling just as a non-nested pair does. A direct measurement "
    "confirms the mechanism and adds one refinement, and its findings are measured in "
    "the sense of @sec-methods. Fitting compound-symmetry and AR(1) candidates to the "
    "same imputations under a strong MAR design, with $20{,}000$ repetitions per cell "
    "and an MCAR twin to isolate the design-imbalance contribution: the per-candidate "
    "level is a large $O(1)$ of about $+2.5$ deviance units that collapses under MCAR, "
    "and the two candidates' levels decouple. The differential between these two "
    "similar candidates is below Monte Carlo resolution, because they respond to the "
    "imbalance almost identically. A maximally dissimilar pair, a structure-blind "
    "diagonal model against AR(1), carries a resolved differential of $-1.2$ at "
    "$3.5$ standard errors. The differential's size scales with how differently the "
    "competitors handle the missing data. One caveat travels with the dissimilar case "
    "and is restated in @sec-discussion. A badly misspecified candidate also carries a "
    "mechanism-independent misspecification $O(1)$, separable by the MCAR contrast but "
    "able to offset part of the design-imbalance term in the net ranking bias."
)

PB6 = (
    "The last result of this part locates which procedures the differential bias "
    "actually affects. At the null, @eq-lrt-bias is precisely the mean inflation that "
    "a correctly calibrated reference distribution already absorbs. The limiting law "
    "of $\\hat d_L$ is the weighted sum "
    "$\\sum_{j} \\lambda_j \\chi^2_1$ with $\\lambda_j = 1 + r_{\\perp,j}$ "
    "[@chanGeneralFeasibleTests2022], and\n"
    "$$ \\sum_{j=1}^{q_{\\mathrm{d}}} \\lambda_j \\;=\\; q_{\\mathrm{d}} + "
    "\\operatorname{tr}(\\mathrm{RIV}_\\perp). $$ {#eq-spectrum-sum}\n"
    "A test that refers the uncorrected numerator to such a reference is therefore "
    "approximately calibrated at the null. Correcting the numerator on top of it "
    "double-counts. The pre-registered null rates agree: $0.042$ uncorrected against "
    "the simulated reference, $0.034$ and slightly conservative with the additional "
    "correction. The differential bias matters instead exactly where no reference "
    "distribution stands between the statistic and its use. Three procedures qualify. "
    "Information-criterion ranking compares penalized values directly. Explicit "
    "numerator corrections must use @eq-lrt-bias rather than the naive difference. "
    "Non-nested comparison brings back both the design-imbalance differential and the "
    "heavy-tailed noise. The first of these is taken up next."
)

PB7 = (
    "A scope statement closes this part, and it is structural in the sense of "
    "@sec-methods. The propositions above are proved for the deterministic-FIML "
    "$\\bar Q_\\infty$. Under proper MI the imputation-side quantities acquire "
    "posterior smearing but remain common to both fits, the same posterior and the "
    "same draws, so the cancellation structure and the leading-order form carry over "
    "structurally. This carry-over is argued, not separately measured, and it is "
    "listed as a limitation in @sec-discussion. The cross-model gate of @sec-methods "
    "was run on this part in full. A blind re-derivation reproduced the "
    "$I_{\\text{com}}$ metric, @eq-lrt-bias term by term, the definite sign of "
    "@eq-overstate with a third independent proof, and the noise orders. An "
    "adversarial pass instructed to break each claim sustained all four."
)

PC1 = (
    "## Information-criterion selection\n\n"
    "This part takes up the replication principle's third level for selection, and it "
    "is where the bias has no reference distribution to hide behind. Model selection "
    "by information criterion compares penalized deviances as numbers and takes the "
    "smallest. Whatever bias each candidate's $-2\\bar Q_\\infty$ carries lands "
    "directly in the ranking. By @thm-bias the bias is model-specific, because "
    "$\\mathrm{RIV}_k$ is computed on candidate $k$'s own parameter space. The "
    "corrected criterion is\n"
    "$$ \\mathrm{AIC}_{\\mathrm{MI}}^{c}(k) \\;=\\; -2\\bar Q_\\infty(\\hat\\psi^{*}_k) "
    "+ 2q_k + \\operatorname{tr}(\\mathrm{RIV}_k). $$ {#eq-ic-corrected}\n"
    "As a penalty this reproduces $\\mathrm{AIC}_{x;y}$ of "
    "@shimodairaInformationCriterionModel2017, whose missing-data surcharge is exactly "
    "half that of the earlier complete-data-discrepancy criteria "
    "[@cavanaughAkaikeInformationCriterion1998a]. What @thm-bias adds is the anatomy, "
    "the MAR term, and the proper-MI scope. The ranking consequence is immediate. For "
    "two candidates the uncorrected difference carries a differential bias of exactly "
    "the surplus of missing information, so the candidate with more missing "
    "information about its own parameters looks artificially better by exactly that "
    "surplus."
)

PC2 = (
    "Two qualifications follow from the likelihood-ratio part. First, candidate sets "
    "are generally not nested chains. For pairs with $O(1)$-separated pseudo-true "
    "values, the design-imbalance differential of @prp-ac-diff is a genuine $O(1)$ "
    "that @eq-ic-corrected does not remove and no reference absorbs. It is small for "
    "similar candidates and grows with dissimilarity. Second, the per-model trace "
    "corrections are exactly the self-contained levels whose difference @prp-naive "
    "shows can overstate the projected trace. The candidate family studied below "
    "happens to sit at the exact equality case. That is a structural fact, and it is "
    "established at the end of this part."
)

PC3 = (
    "The pre-registered selection evidence shows the directional signature the "
    "theorem predicts, and its findings are measured in the sense of @sec-methods. "
    "The study draws four-variate normal data whose only nonzero correlations are "
    "$\\sigma_{13} = \\sigma_{24} = \\rho$, imposes 40% MAR missingness, and ranks "
    "four zero-pattern covariance candidates by MI-AIC under congenial imputation. At "
    "$N = 500$ with $\\rho = 0.40$, uncorrected MI-AIC selects the true model in "
    "$0.674$ of repetitions against an oracle rate of $0.898$, and 100% of its "
    "misclassifications land on the saturated, largest-RIV candidate. The corrected "
    "criterion recovers selection to $0.816$. That is substantial and visibly short "
    "of the oracle. The residual is not an error in the trace. It is the subject of "
    "the rest of this part."
)

PC4 = (
    "Selection depends on more than a mean. At the null the limiting law of each "
    "anchored deviance is a weighted sum with every weight at least one "
    "(@eq-spectrum-sum), so even a correctly centered criterion has inflated spread, "
    "and inflated spread flips rankings. This motivates a graded contrast, "
    "pre-registered in full before any code was written: match the first moment, the "
    "first two moments, or the entire null distribution, and measure what each step "
    "achieves. The working statistic anchors every candidate at the saturated model "
    "fit to the same imputations, $T_k = 2[\\bar Q_\\infty(\\hat\\psi^{*}_{\\text{sat}}) "
    "- \\bar Q_\\infty(\\hat\\psi^{*}_k)]$. Anchoring costs nothing, because AIC "
    "ranking is invariant to the common shift, and it buys three things. The anchor is "
    "the congenial imputation model itself, so the heavy-tailed realized $(A)+(C)$ "
    "component and the large noise cancel dataset by dataset, which is the "
    "@prp-pairing mechanism applied to every candidate. Every $T_k$ is a "
    "likelihood-ratio statistic with an analytic per-model null law, available without "
    "knowing the global truth. And for block-diagonal zero patterns the constrained "
    "maximizer is closed-form."
)

PC5 = (
    "Three maps are compared, each built from the analytic null weights "
    "$\\lambda_{k,j}$. The mean map subtracts "
    "$\\operatorname{tr}(\\mathrm{RIV}_{\\perp,k})$ per model. It telescopes, so all "
    "pairwise comparisons are simultaneously mean-corrected. The two-moment map is "
    "the unique affine map carrying the null law's mean and variance onto the "
    "complete-data $\\chi^2$'s. Matching a misbehaving statistic's first two moments "
    "is the standard repair in the structural-equation tradition "
    "[@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006], but "
    "here the coefficients come from the analytic null law rather than from estimated "
    "sandwich matrices. The equating map applies the equipercentile equating function "
    "of observed-score test equating [@kolenTestEquatingScaling2014] with the analytic "
    "null law as the source distribution, and by the probability integral transform "
    "it matches the entire null distribution. The weighted-$\\chi^2$ distribution "
    "function is evaluated by numerical inversion of the characteristic function "
    "[@imhofComputingDistributionQuadratic1961; @daviesAlgorithm155Distribution1980]. "
    "A simulated reference in the style of Chan's Monte Carlo null was the "
    "pre-registered fallback and was never needed. The pre-registration predicted the "
    "split the data then delivered. Each step closes more of the null-side gap, while "
    "the two stronger maps shrink evidence against misspecified candidates, because "
    "no transform built from the observed data can restore destroyed Fisher "
    "information."
)

PC6 = (
    "The graded run uses three cells at $N = 500$ with $R = 2000$ repetitions each. "
    "True-model selection rates, with Monte Carlo standard error about $0.010$:\n\n"
    "| Cell | oracle | uncorrected | mean | two-moment | equating |\n"
    "|---|---|---|---|---|---|\n"
    "| $\\rho = 0.40$ | 0.899 | 0.678 | 0.814 | 0.904 | 0.903 |\n"
    "| $\\rho = 0.10$ | 0.820 | 0.582 | 0.650 | 0.648 | 0.650 |\n"
    "| $\\rho = 0$ (junk) | 0.727 | 0.422 | 0.585 | 0.702 | 0.696 |\n\n"
    "Every pre-registered pass criterion was met, and four findings summarize the "
    "table. The null side calibrates completely. On the true model's anchored "
    "statistic the distance to the paired complete-data statistic falls from $0.281$ "
    "to $0.019$ across the four arms, and the variance ratio falls from $3.18$ to "
    "$0.97$. The mean correction's paired gap is itself a direct confirmation of "
    "@eq-lrt-bias at $q_{\\mathrm{d}} = 4$. Where overfit flips drive the errors, "
    "distribution matching reaches the oracle. In the $\\rho = 0.40$ design the "
    "two-moment and equating arms select at $0.904$ and $0.903$, statistically "
    "indistinguishable from complete-data AIC, and the junk cell closes 90% of the "
    "uncorrected-to-oracle gap. The noncentral side shrinks as the law predicts. The "
    "underfit candidate's mean statistic, relative to its complete-data counterpart, "
    "is $1.002$ under the mean correction, $0.586$ under two moments against a "
    "predicted $0.570$, and $0.362$ under equating against a predicted far-tail "
    "factor of $0.398$. Conservatism against misspecified candidates is the price of "
    "null-side calibration, and the factor is known in advance. Where selection is "
    "genuinely hard, nothing closes the floor. In the weak-signal cell the oracle "
    "itself drops to $0.820$ and no correction passes $0.650$. The $0.17$ residual is "
    "information loss, not calibration error. The floor is a measurement on these "
    "designs, not a theorem."
)

PC7 = (
    "Two structural limits close this part, and both are exact. First, in this "
    "candidate family the naive trace difference and the exact projected trace agree "
    "to machine precision, at $3.6 \\times 10^{-15}$. That is not luck. "
    "Block-diagonal covariance patterns decompose both informations over within-block "
    "and cross-block coordinates, which is precisely the equality condition of "
    "@prp-naive. The overstatement is therefore invisible in this family and material "
    "only for constraints that do not block-decompose, where it reaches the factor "
    "above three of the $\\mu_1$ design. Second, per-model marginal transforms cannot "
    "calibrate a difference distribution. The dependence between two candidates' "
    "scores is invariant under marginal maps, and in the weak-signal near-tied pair "
    "the equated score difference has mean $6.10$ against the complete-data "
    "$10.00$. Selection-aware refinements are developed separately. The standings "
    "differ and are stated. The noncentral shrinkage and the difference-distribution "
    "invariance are firm. The weak-signal floor is measured. As in the "
    "likelihood-ratio part, everything here is stated and measured for the "
    "deterministic-FIML $\\bar Q_\\infty$. The anchoring cancellations are properties "
    "of sharing the imputation model, so the construction carries to proper MI "
    "unchanged, and the pre-registered sweep's proper-MI cells track the FIML cells "
    "within $0.011$ on the headline rates (@sec-simulations)."
)

def mk(idx, goal, proposition, dep, deptypes, prose, serves_L2, sets_up, topic, closing, flags, citations, numbers, notes):
    return {
        "id": idx, "section": "S4", "goal": goal, "proposition": proposition,
        "depends_on": dep, "dep_types": deptypes,
        "review": {"serves_L2": serves_L2, "serves_L1": "M4a DERIVATIONS (D-03 inline numbers; D-08 proofs in companion; D-10 principle spine)",
                   "sets_up": sets_up, "topic_sentence": topic, "closing_sentence": closing,
                   "status": "drafted", "flags": flags},
        "draft_prose": prose,
        "audit": {"status": "complete", "citations": citations, "numbers": numbers, "notes": notes}
    }

s4 = [
    mk("S4-P1", "transition", "Section roadmap: three parts answering the principle level by level; tier labels in force; proofs in companion; numbers inline.",
       ["S3-P8"], ["builds_on"], PA1, "S4-SP8 (+ section framing)", "all S4 paragraphs",
       "This section delivers the paper's analytic results, in three parts.",
       "...the studies behind them are reported in @sec-simulations.",
       None, {}, {}, "Use-first roadmap; principle-level openers per SP8."),
    mk("S4-P2", "define_concept", "MVN instantiation: objects, estimand, the two maximizers concrete; general statement scoped to @sec-discussion.",
       ["S2-P2"], ["builds_on"], PA2, "S4-SP1 (setup)", "S4-P3..P8",
       "The theorem is stated for a general regular likelihood with an estimated scale or covariance and is instantiated in the multivariate normal family.",
       "The scope of the normal instantiation is taken up in @sec-discussion.",
       None,
       {"schaferAnalysisIncompleteMultivariate1997": "verified (read in-session 2026-06-07; observed-data loglik construction, ToC 5.3.5; quarried sentence audit-passed at 180e2b5)"},
       {}, "Quarried from 180e2b5 sec-setup Objects; cadence rewrite."),
    mk("S4-P3", "define_concept", "RIV instantiated (@eq-riv); single-RIV unconditional convention (K-M); D-matrix normalization warning; the two-RIV artifact disclosed.",
       ["S4-P2", "S2-P4"], ["builds_on", "builds_on"], PA3, "S4-SP1", "every trace below",
       "The RIV of @eq-bg-riv is instantiated with one convention fixed and one warning repeated.",
       "...substituting one for the other changes every constant below.",
       None,
       {"kenwardLikelihoodBasedFrequentist1998": "verified (read in-session 2026-06-07; unconditional convention + cross term)",
        "schaferAnalysisIncompleteMultivariate1997": "verified (D matrix eq 3.21 usage; audit-passed at 180e2b5)"},
       {}, "Quarried; includes the honest two-RIV artifact disclosure (T-04)."),
    mk("S4-P4", "define_concept", "Q-bar-infinity defined (@eq-qbar); the fitted-vs-oracle fork stated with both signs (D-02), tied to the S3 sign episode; both regimes simulated.",
       ["S2-P6", "S2-P7", "S3-P6"], ["builds_on", "builds_on", "builds_on"], PA4, "S4-SP1 (fitted-vs-oracle up front)", "the theorem's sign; S5",
       "The object of the theorem is the infinite-imputation Q-function, and its definition contains the choice that fixes the sign of everything that follows.",
       "...imputing from the fitted model produces the constants of the theorem (@sec-simulations).",
       None, {},
       {"oracle branch -1/2 tr(RIV)": "deriv:sec-qfun", "both regimes confirmed by simulation": "verif:verification/cache/rederivation-knownvar-N200-R20000.rds"},
       "Quarried; D-02 statement; links to S3-P6's episode."),
    mk("S4-P5", "define_concept", "The A/B split (@eq-split) and the seven regularity conditions, compressed; variance-recovery anchor.",
       ["S4-P4"], ["builds_on"], PA5, "S4-SP1", "the theorem",
       "The bias is split at the pivot into two terms with distinct mechanisms.",
       "Together they deliver the variance-recovery property that identifies @eq-riv with $r_\\infty$.",
       None,
       {"vaartAsymptoticStatistics1998a": "verified (R1-R2 smoothness/positive-definite info; quarried citation audit-passed at 180e2b5; spot-checked in-session)",
        "rubinInferenceMissingData1976b": "verified (read in-session 2026-06-06/07)",
        "mengMultipleImputationInferencesUncongenial1994a": "verified (read in-session)",
        "rubinMultipleImputationNonresponse1987": "verified (read in-session)"},
       {}, "Quarried; assumptions compressed to one passage per D-08 (full list in companion)."),
    mk("S4-P6", "state_result", "THE THEOREM (@eq-thm, firm) + Term B sketch with the variance-of-the-gap display (@eq-vargap) and the named trap.",
       ["S4-P5"], ["builds_on"], PA6, "S4-SP1", "S4-SP4/SP6 applications; S6 verdict",
       "Under R1-R7, for a model that estimates a scale or covariance, to leading order [the theorem].",
       "...@eq-vargap is displayed to forestall it.",
       None, {},
       {"E[T] = +1/2 tr(RIV) + (A)+(C)": "deriv:sec-thm", "Var(gap) = I_obs^-1 - I_com^-1": "deriv:sec-thm"},
       "Theorem div quarried verbatim; tier label firm attached in prose."),
    mk("S4-P7", "prove_sketch", "Term A sketch: three pieces, nonzero entropy gradient (Gibbs trap), MCAR cancellation, (A)+(C) closed form (@eq-ac), three-tier standing (firm/measured/structural).",
       ["S4-P6"], ["builds_on"], PA7, "S4-SP2", "S4-P13 (B5); S6 G1",
       "Term $A$ is the delicate half.",
       "...the differential is derived and measured precisely in the next part.",
       None, {},
       {"(A)+(C) bivariate monotone closed form": "deriv:sec-lrt-ac", "analytic leading-order value ~ -0.22": "deriv:sec-lrt-ac"},
       "Quarried; the three-standing passage is D-05/T-04 in action."),
    mk("S4-P8", "state_result", "Known-scale collapse (@eq-knownscale, prices proper vs improper) + entropy-plug-in consistency check + pooled MC 2.43 +/- 0.26 inline.",
       ["S4-P6", "S2-P7"], ["builds_on", "builds_on"], PA8, "S4-SP2 + SP1 tail + SP3", "S5 grading",
       "Two checks close the theorem, one on its scope and one on its form.",
       "...pools to $\\hat T = 2.43 \\pm 0.26$ against the augmented target range $2.42$ to $2.55$ in the four-variate MAR design (@sec-simulations).",
       None, {},
       {"known-scale arms 0 / -1/2 tr(RIV); R=2e5 within 4%": "verif:verification/cache/rederivation-knownvar-N200-R20000.rds",
        "entropy-Hessian identity": "deriv:sec-thm",
        "pooled 2.43 +/- 0.26 vs 2.42-2.55": "verif:verification/cache/run_all-prod"},
       "Quarried; ties the collapse to S2-P7's proper-imputation pricing."),
    mk("S4-P9", "define_concept", "LRT part opener: principle level (testing); the shared-imputation numerator (@eq-dl); psi_0* is NOT the null model's own MLE; the differential as object.",
       ["S4-P6", "S2-P13"], ["builds_on", "builds_on"], PB1, "S4-SP4 (+SP8 opener)", "B2-B7",
       "This part takes up the replication principle's third level for testing.",
       "...the object of interest is the differential.",
       None,
       {"chanMultipleImprovementsMultiple2022": "verified (read in-session; maximize-then-average)"},
       {}, "Quarried from sec-lrt opening; principle-level opener added."),
    mk("S4-P10", "state_result", "Proposition L1 (@eq-lrt-bias, firm): tr(RIV_perp) in the I_com metric; the natural error reproduces the naive formula; 2.64 vs 8.47, 52 se inline.",
       ["S4-P9"], ["builds_on"], PB2, "S4-SP4", "B3; C-part anchoring",
       "Under R1-R7, at the null [the proposition].",
       "...$52$ standard errors from the naive value (@sec-simulations).",
       None, {},
       {"2.64 vs naive 8.47; 52 se": "deriv:sec-lrt + verif:verification/cache/run_all-prod"},
       "Prop div quarried; metric explanation rewritten plain."),
    mk("S4-P11", "state_result", "Proposition naive-overstates (@eq-overstate, firm) + exact gap (@eq-gap) + 5% / factor-3 practical reading.",
       ["S4-P10"], ["builds_on"], PB3, "S4-SP4", "C2; C7 (equality case)",
       "With the null model's own self-contained trace correction, always [the inequality].",
       "It is a factor above three in the $\\mu_1$ design above.",
       None, {},
       {"gap = tr[(I+H11)^-1 H12 H12^T]": "deriv:sec-lrt", "5% / factor >3": "deriv:sec-lrt"},
       "Quarried; Gram/Schur proof pointer in companion."),
    mk("S4-P12", "state_result", "Proposition pairing (firm): O(1) paired noise at null/local via exact realization cancellation; sd 18.4->36.5 vs flat 1.5x inline.",
       ["S4-P10"], ["builds_on"], PB4, "S4-SP5 (pairing half)", "C4 anchoring; S5",
       "Let $D$ be the per-dataset paired differential [the proposition].",
       "...never by differencing separately estimated levels.",
       None, {},
       {"sd 18.4/26.6/36.5 vs 1.58/1.47/1.57": "verif:verification/cache/run_all-prod"},
       "Quarried; mechanism stated as cancellation of realizations."),
    mk("S4-P13", "state_result", "Proposition (A)+(C) differential (firm for structure): exact null cancellation; separation criterion (Vuong regime); W4 measurements (level +2.5, similar below resolution, dissimilar -1.2 at 3.5 se) + misspecification caveat.",
       ["S4-P7", "S4-P12"], ["builds_on", "builds_on"], PB5, "S4-SP5 (cancellation half)", "C2; S6 G5",
       "The $(A)+(C)$ contributions of the two levels are properties of the imputation, not of which model is fit [the proposition].",
       "...able to offset part of the design-imbalance term in the net ranking bias.",
       None,
       {"vuongLikelihoodRatioTests1989": "verified (read in-session 2026-06-07; pseudo-true values + nested/non-nested/overlapping taxonomy, abstract + SS1)"},
       {"+2.5 per-candidate level; similar-pair below resolution; dissimilar -1.2 at 3.5 se; 20k repetitions": "verif:verification/cache/w4-nonnested-summary.csv"},
       "Quarried; W4 findings labeled measured; caveat restated for S6."),
    mk("S4-P14", "state_result", "The absorption result (SP5b): spectrum sum (@eq-spectrum-sum); calibrated reference absorbs the bias; double-counting (0.042 vs 0.034); the three no-reference procedures.",
       ["S4-P10", "S2-P13"], ["builds_on", "builds_on"], PB6, "S4-SP5b", "C1 (the bridge)",
       "The last result of this part locates which procedures the differential bias actually affects.",
       "The first of these is taken up next.",
       None,
       {"chanGeneralFeasibleTests2022": "verified (read in-session; eq 1.10 weighted sum)"},
       {"0.042 uncorrected / 0.034 over-corrected": "verif:verification/cache/W2-prod-amelia.rds"},
       "The (b)->(c) bridge added in cycle 1 (DAG L5)."),
    mk("S4-P15", "scope_limit", "LRT scope: FIML-proved, proper-MI carry-over structural (G2); the cross-model gate record for this part.",
       ["S4-P13", "S3-P6"], ["builds_on", "builds_on"], PB7, "S4-SP4 scope", "S6 G2",
       "A scope statement closes this part, and it is structural in the sense of @sec-methods.",
       "An adversarial pass instructed to break each claim sustained all four.",
       None, {},
       {"blind re-derivation + adversarial pass sustained": "xmodel:verification/cache/derivation-audit-run-w2diff.json"},
       "Quarried; tier label structural; gate record cited."),
    mk("S4-P16", "state_result", "IC part opener: principle level (selection); no reference to hide behind; corrected criterion (@eq-ic-corrected) = AIC_{x;y}; ranking consequence.",
       ["S4-P14", "S2-P10"], ["builds_on", "builds_on"], PC1, "S4-SP6 (+SP8 opener)", "C2-C7",
       "This part takes up the replication principle's third level for selection, and it is where the bias has no reference distribution to hide behind.",
       "...looks artificially better by exactly that surplus.",
       None,
       {"shimodairaInformationCriterionModel2017": "verified (read in-session; AIC_{x;y}, half surcharge)",
        "cavanaughAkaikeInformationCriterion1998a": "verified (read in-session; AICcd)"},
       {}, "Quarried; principle-level opener added."),
    mk("S4-P17", "scope_limit", "Two qualifications inherited from the LRT part: non-nested O(1) differential not removed by the trace; the naive-overstatement and the family's equality case.",
       ["S4-P16", "S4-P11", "S4-P13"], ["builds_on", "qualifies", "qualifies"], PC2, "S4-SP6 (qualifications)", "C7",
       "Two qualifications follow from the likelihood-ratio part.",
       "That is a structural fact, and it is established at the end of this part.",
       None, {}, {}, "Quarried; dep_types use 'qualifies' backward edges."),
    mk("S4-P18", "evaluate_evidence", "Pre-registered selection evidence: 0.674 vs oracle 0.898; 100% of misclassifications on the largest-RIV candidate; corrected 0.816; the residual motivates the ladder.",
       ["S4-P16"], ["builds_on"], PC3, "S4-SP6", "C4-C6",
       "The pre-registered selection evidence shows the directional signature the theorem predicts, and its findings are measured in the sense of @sec-methods.",
       "It is the subject of the rest of this part.",
       None, {},
       {"0.674 / 0.816 / 0.898; 100% largest-RIV": "verif:verification/cache/run_all-prod"},
       "Quarried; the W3 headline."),
    mk("S4-P19", "define_concept", "Beyond the mean: spread flips rankings; the saturated-anchored statistic T_k and its three properties (pairing cancellation, analytic null law, closed form).",
       ["S4-P18", "S4-P12", "S4-P14"], ["builds_on", "builds_on", "builds_on"], PC4, "S4-SP7 (setup)", "C5-C6",
       "Selection depends on more than a mean.",
       "And for block-diagonal zero patterns the constrained maximizer is closed-form.",
       None, {},
       {"anchored statistic properties": "deriv:sec-ic"},
       "Quarried; ladder setup."),
    mk("S4-P20", "define_concept", "The three maps (mean / two-moment / equating) with their sources; the fallback never needed; the pre-registered prediction of the null/noncentral split.",
       ["S4-P19"], ["builds_on"], PC5, "S4-SP7 (maps)", "C6",
       "Three maps are compared, each built from the analytic null weights.",
       "...no transform built from the observed data can restore destroyed Fisher information.",
       None,
       {"satorraEnsuringPositivenessScaled2010": "verified (read in-session 2026-06-07; scaled difference procedure :76)",
        "asparouhovRobustChiSquare2006": "verified (read in-session 2026-06-04 + quarried; mean-and-variance adjustment)",
        "kolenTestEquatingScaling2014": "verified (equating definition ch.2; quarried citation audit-passed at 180e2b5)",
        "imhofComputingDistributionQuadratic1961": "verified (read in-session 2026-06-04 + quarried; CF inversion)",
        "daviesAlgorithm155Distribution1980": "verified (read in-session 2026-06-04 + quarried; AS155)"},
       {"fallback 0 of 18,000 evaluations": "verif:verification/cache/ic-ladder-summary.csv"},
       "Quarried; SEM-tradition framing retained."),
    mk("S4-P21", "evaluate_evidence", "The ladder table + four findings: null side calibrates completely (KS 0.281->0.019, var ratio 3.18->0.97); oracle reached (0.904/0.903 vs 0.899); noncentral shrinkage exact (0.586 vs 0.570; 0.362 vs 0.398); weak-signal floor 0.17 = information loss.",
       ["S4-P20"], ["builds_on"], PC6, "S4-SP7 (results)", "S6 verdict; S5",
       "The graded run uses three cells at $N = 500$ with $R = 2000$ repetitions each.",
       "The floor is a measurement on these designs, not a theorem.",
       None, {},
       {"table rows + KS 0.281->0.019 + var 3.18->0.97 + shrinkage 0.586/0.570, 0.362/0.398 + floor 0.17": "verif:verification/cache/ic-ladder-summary.csv"},
       "Quarried table verbatim; findings compressed to one paragraph."),
    mk("S4-P22", "scope_limit", "Two exact structural limits (I7): block-decomposition equality (3.6e-15; naive-input arm scores 0.824 vs 0.904) and difference-distribution invariance (6.10 vs 10.00); standings stated; proper-MI tracking within 0.011.",
       ["S4-P21", "S4-P11"], ["builds_on", "qualifies"], PC7, "S4-SP7 (limits) + I7", "S6 G2-G4; S5",
       "Two structural limits close this part, and both are exact.",
       "...track the FIML cells within $0.011$ on the headline rates (@sec-simulations).",
       None, {},
       {"3.6e-15 agreement; 6.10 vs 10.00; 0.011 proper-MI tracking": "verif:verification/cache/ic-ladder-summary.csv + verif:verification/cache/run_all-prod"},
       "Quarried; the naive-input arm comparison (0.824 vs 0.904) folded into C7? NO - kept implicit here, full version in S5. Flag if Marcus wants it inline."),
]

l3["paragraphs"].extend(s4)
l3["metadata"]["status"] = "drafting_s4_complete"
l3["metrics_gate"]["notes"] = (
    "After S4 drafting (2026-06-07): S1 7 + S2 13 + S3 8 + S4 22 = 50 paragraphs. S4 "
    "quarried from 180e2b5 sec-setup/sec-lrt/sec-ic with displays, propositions, and "
    "numbers verbatim and prose rewritten to the style rules; principle-level openers "
    "on all three parts; tier labels attached in prose; all quoted numbers pointered. "
    "Dependency graph acyclic. Remaining: S5, S6."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)

s4e = [
    ("E-S4-P6-1", "S4-P6", "deriv:sec-thm", "Theorem statement + Term B variance-of-gap argument.", "The theorem (firm)."),
    ("E-S4-P7-1", "S4-P7", "deriv:sec-lrt-ac", "(A)+(C) structure, sign, closed form, three-tier standing.", "Term A sketch."),
    ("E-S4-P8-1", "S4-P8", "verif:verification/cache/rederivation-knownvar-N200-R20000.rds", "Known-scale arms, R=2e5, all four values within 4%.", "Scope check."),
    ("E-S4-P8-2", "S4-P8", "verif:verification/cache/run_all-prod", "Pooled 2.43 +/- 0.26 vs target 2.42-2.55.", "Headline MC, inline per D-03."),
    ("E-S4-P10-1", "S4-P10", "deriv:sec-lrt", "Prop L1, I_com metric, three routes; 2.64 vs 8.47.", "LRT differential (firm)."),
    ("E-S4-P11-1", "S4-P11", "deriv:sec-lrt", "Overstatement inequality + exact Schur gap.", "Naive overstates (firm)."),
    ("E-S4-P12-1", "S4-P12", "verif:verification/cache/run_all-prod", "sd growth 18.4/26.6/36.5 vs flat 1.58/1.47/1.57.", "Pairing collapse measurement."),
    ("E-S4-P13-1", "S4-P13", "verif:verification/cache/w4-nonnested-summary.csv", "W4: +2.5 level; similar below resolution; dissimilar -1.2 (3.5 se).", "Separation-regime measurements."),
    ("E-S4-P13-2", "S4-P13", "lit:vuongLikelihoodRatioTests1989", "Pseudo-true values; nested/non-nested/overlapping; weighted chi-square law (abstract).", "The separation regime's source."),
    ("E-S4-P14-1", "S4-P14", "lit:chanGeneralFeasibleTests2022", "Eq 1.10 weighted-sum null law; spectrum mean exceeds q_d by tr(RIV_perp).", "Absorption."),
    ("E-S4-P14-2", "S4-P14", "verif:verification/cache/W2-prod-amelia.rds", "Null rates 0.042 / 0.034.", "Double-counting measurement."),
    ("E-S4-P16-1", "S4-P16", "deriv:sec-ic", "Corrected criterion; model-specific bias; ranking consequence.", "IC criterion (firm)."),
    ("E-S4-P16-2", "S4-P16", "lit:shimodairaInformationCriterionModel2017", "AIC_{x;y} penalty identity; half the PDIO/AICcd surcharge.", "Penalty precedent."),
    ("E-S4-P18-1", "S4-P18", "verif:verification/cache/run_all-prod", "W3: 0.674/0.816/0.898; 100% largest-RIV misclassifications.", "Directional signature."),
    ("E-S4-P20-1", "S4-P20", "deriv:sec-ic", "The three maps from the analytic null weights.", "Ladder maps (firm)."),
    ("E-S4-P21-1", "S4-P21", "verif:verification/cache/ic-ladder-summary.csv", "Table; KS 0.281->0.019; var 3.18->0.97; shrinkage 0.586/0.570 + 0.362/0.398; floor 0.17.", "Ladder results (measured)."),
    ("E-S4-P22-1", "S4-P22", "verif:verification/cache/ic-ladder-summary.csv", "3.6e-15 equality-case agreement; difference 6.10 vs 10.00.", "The two structural limits (firm)."),
]
l4["evidence_map"].extend([
    {"id": a, "proposition_id": b, "pointer": c, "evidence_status": "verified", "passage_or_value": d, "note": e}
    for a, b, c, d, e in s4e
])
l4["metrics_gate"]["notes"] = "S1-S4 populated; all pointers resolve. Full gate when S5-S6 drafted."

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S4 drafted: 22 paragraphs into level3, 17 evidence entries into level4")
