# S2 Background and notation - from-scratch draft (D-12), 2026-06-06
#
# Second Level-3 drafting cycle, under the approved S2 blueprint (a21120a):
# dual-purpose (notation + precision restatement), three-tier gradient
# (calculus-based entry -> graduate -> specialist), gradient NOT announced in the
# text, each restatement names the later result that depends on it (D-04),
# plain expository cadence per CLAUDE.md prose-style section (11fe928).
# Quarried heavily from 180e2b5 sec-background (all quotes citation-verified there
# AND re-read in-session today); notation paragraph new (moved forward from old
# sec-setup 'Objects', generalized - the MVN instantiation stays in S4).
# Twelve paragraphs:
#   P1 opener (why restate; the two conflations; notation-once rule)
#   Tier 1: P2 notation (Y, R, two likelihoods, two MLE targets)
#           P3 ignorability (Rubin 1976)
#           P4 missing-information principle + RIV defined + EM rate matrix warning
#   Tier 2: P5 EM and the Q-function (Dempster; Q = L + H; curvature I_com)
#           P6 imputation as Monte Carlo E-step (Wei-Tanner bridge)
#           P7 Rubin's rules as exact identities (Result 3.2; r_inf; one approximation)
#           P8 congeniality (Meng 1994)
#   Tier 3: P9 AIC as bias-corrected plug-in (Akaike)
#           P10 Wilks
#           P11 observed vs expected information under MAR (Kenward-Molenberghs)
#           P12 MI test combining + calibration + the prior MI-AIC (launch points)
# Level 4: 21 new entries appended for S2.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

P1 = (
    "The argument of this paper rests on results that are individually standard. This "
    "section restates them rather than merely cites them. The reason is precision: each "
    "result is used later in a form that a casual recollection would miss. The EM rate "
    "matrix is not the RIV. Rubin's rules are exact, given one named approximation. The "
    "observed and the expected information differ under MAR. Each restatement below "
    "names the later result that depends on it. The section also fixes the paper's "
    "notation: every symbol is introduced here once and reused unchanged."
)

P2 = (
    "**Notation: two likelihoods, two estimators.** The basic objects are a data matrix "
    "and a missingness indicator. Write $Y = (Y_{\\text{obs}}, Y_{\\text{mis}})$ for the "
    "complete data, split into its observed and missing parts, and write $R$ for the "
    "indicator of which entries are observed. Two likelihoods can be formed from a "
    "parametric model $f(Y \\mid \\theta)$. The complete-data likelihood is "
    "$f(Y \\mid \\theta)$ itself. The observed-data likelihood integrates the missing "
    "part out: $f(Y_{\\text{obs}} \\mid \\theta) = \\int f(Y_{\\text{obs}}, "
    "Y_{\\text{mis}} \\mid \\theta)\\, dY_{\\text{mis}}$. Each likelihood has its own "
    "maximizer, and the two play different roles. The complete-data maximum likelihood "
    "estimate $\\hat\\theta_{\\text{com}}$ is computable only when nothing is missing; "
    "it is the target an analyst would have reached with full data. The observed-data "
    "maximum likelihood estimate $\\hat\\theta_{\\text{obs}}$ is the best that can be "
    "computed from the data at hand. The bias at the center of this paper measures what "
    "happens when likelihood values built around one of these estimators are read as if "
    "they were built around the other. @sec-derivations instantiates this notation for "
    "the multivariate normal model; everything in this section is general."
)

P3 = (
    "**Ignorability.** @rubinInferenceMissingData1976b gives the weakest general "
    "conditions under which the process that causes missing data can be ignored. For "
    "likelihood and Bayesian inference, two conditions suffice. The data must be missing "
    "at random: the conditional probability of the observed missingness pattern is the "
    "same for all values of the missing data. The mechanism's parameter must also be "
    "distinct from the data parameter. Sampling-distribution inference is stricter. It "
    "requires in addition that the observed data are observed at random, which together "
    "with MAR amounts to MCAR, and it is otherwise generally conditional on the observed "
    "pattern. Everything in this paper assumes the likelihood-side conditions. The gap "
    "Rubin identified between the two senses of \"ignorable\" matters later, because two "
    "objects of this paper live inside it: the design-imbalance term $(A)+(C)$ of the "
    "main theorem, and the information-matrix distinction restated at the end of this "
    "section."
)

P4 = (
    "**The missing-information principle and the RIV.** Information matrices add across "
    "the missing-data split. @woodburyMissingInformationPrinciple1972 decompose the "
    "information in the complete data as the observed-data information plus what they "
    "call the lost information, together with a score identity: the observed-data score "
    "is the conditional expectation of the complete-data score. @Meng01121991 state the "
    "same principle in the form used throughout this paper,\n"
    "$$ I_{\\text{obs}} \\;=\\; I_{\\text{com}} - I_{\\text{mis}\\mid\\text{obs}}, $$ {#eq-bg-mip}\n"
    "\"observed information = complete information $-$ missing information.\" The "
    "central matrix of this paper is built from these ingredients:\n"
    "$$ \\mathrm{RIV} \\;=\\; I_{\\text{obs}}^{-1}\\, I_{\\text{mis}\\mid\\text{obs}}. $$ {#eq-bg-riv}\n"
    "Its trace adds up the odds of missing information about each parameter, and it is "
    "the matrix form of Rubin's scalar relative increase in variance, restated below. "
    "One warning is needed here, and it is the reason this section exists. The EM "
    "literature works with a different normalization of the same ingredients: the EM "
    "rate matrix $DM = I_{\\text{mis}\\mid\\text{obs}}\\, I_{\\text{com}}^{-1}$ of "
    "@dempsterMaximumLikelihoodIncomplete1977a and @Meng01121991. The RIV divides by the "
    "observed-data information; the rate matrix divides by the complete-data "
    "information. The two matrices have different eigenvalues, and conflating them "
    "corrupts every trace formula in this paper. The notation keeps them apart."
)

P5 = (
    "**EM and the Q-function.** @dempsterMaximumLikelihoodIncomplete1977a define\n"
    "$$ Q(\\phi' \\mid \\phi) \\;=\\; E\\big(\\log f(\\mathbf{x} \\mid \\phi') "
    "\\,\\big|\\, \\mathbf{y}, \\phi\\big), $$ {#eq-bg-q}\n"
    "the expected complete-data log-likelihood given the observed data. The E-step "
    "computes $Q(\\cdot \\mid \\phi^{(p)})$ and the M-step maximizes it. Their heuristic "
    "is direct: \"since we do not know $\\log f(\\mathbf{x}\\mid\\phi)$, we maximize "
    "instead its current expectation given the data $\\mathbf{y}$ and the current fit "
    "$\\phi^{(p)}$.\" Two facts from their analysis carry the weight later. First, the "
    "Q-function decomposes as $Q(\\phi'\\mid\\phi) = L(\\phi') + H(\\phi'\\mid\\phi)$, "
    "where $L$ is the observed-data log-likelihood and $H$ is a conditional-entropy "
    "term. The main theorem of @sec-derivations is, at bottom, an account of what the "
    "$H$ term does when its parameters are estimated rather than known. Second, the "
    "curvature of $Q$ at its maximizer is the complete-data information "
    "$I_{\\text{com}}$, not the observed-data information. This single geometric fact "
    "drives the likelihood-ratio result of @sec-derivations: constrained fits of the "
    "averaged log-likelihood project in the $I_{\\text{com}}$ metric."
)

P6 = (
    "**Imputation is Monte Carlo integration of the E-step.** "
    "@weiMonteCarloImplementation1990 implement the E-step by simulation. Draws "
    "$z^{(1)},\\dots,z^{(m)}$ from the conditional predictive distribution of the "
    "missing data replace the integral in @eq-bg-q by an average over completed data "
    "sets. Their Remark 2 makes the connection to multiple imputation explicit: \"Rubin "
    "(1987) referred to the quantities $z^{(1)}, \\ldots, z^{(m)}$ as multiple "
    "imputations.\" This is the precise sense in which the averaged log-likelihood over "
    "imputations is a Q-function. Its $m \\to \\infty$ limit, written "
    "$\\bar Q_\\infty(\\theta)$, is the central object of this paper. One detail of the "
    "definition matters more than any other: the conditioning is on the fitted (or "
    "drawn) imputation model, not on the true parameter. That choice of conditioning "
    "determines the sign of the main theorem, and @sec-derivations states both versions "
    "to prevent the standard confusion."
)

P7 = (
    "**Rubin's rules are exact posterior-moment identities.** For multiply imputed "
    "data, Result 3.2 of @rubinMultipleImputationNonresponse1987 shows two things. The "
    "posterior mean of an estimand given the observed data equals the average of the "
    "completed-data posterior means. The posterior variance equals the average "
    "completed-data variance plus the variance of the completed-data means. These are "
    "the ordinary rules for conditional moments, applied to imputation, and with "
    "infinitely many imputations they are exact identities rather than asymptotic "
    "approximations. In Rubin's notation they give $\\bar Q_\\infty$, "
    "$\\bar U_\\infty$, $B_\\infty$, and the total variance "
    "$T_\\infty = \\bar U_\\infty + B_\\infty$. Rubin then defines the scalar relative "
    "increase in variance due to nonresponse,\n"
    "$$ r_\\infty \\;=\\; B_\\infty / \\bar U_\\infty $$ {#eq-bg-rinf}\n"
    "(his equation 3.1.7). The RIV matrix of @eq-bg-riv is this quantity in matrix "
    "form. A single approximation separates the exact identities from usable "
    "inference: \"the usual approximation of the posterior distribution as normal\" "
    "(a Laplace-type approximation; @Tierney01031986). The main theorem describes what "
    "happens when the exact moment identities are used not as moments but through the "
    "likelihood itself."
)

P8 = (
    "**Congeniality.** @mengMultipleImputationInferencesUncongenial1994a formalizes "
    "when the imputer and the analyst agree. An analysis procedure is congenial to an "
    "imputation model if there exists one Bayesian model that reproduces both: its "
    "posterior means and variances asymptotically match the analyst's complete-data and "
    "incomplete-data procedures, and its posterior predictive distribution for the "
    "missing data is the imputation model. Everything in this paper assumes congenial, "
    "proper imputation. This assumption is what gives the main theorem its force: the "
    "bias derived there is not an artifact of imputer-analyst disagreement. It is what "
    "remains after they agree."
)

P9 = (
    "**AIC is a bias-corrected plug-in estimate.** @akaikeNewLookStatistical1974a "
    "evaluates a fitted model by its mean log-likelihood against the true distribution. "
    "The maximized log-likelihood is the natural estimate of this criterion, and it is "
    "too optimistic: it \"needs a correction for the downward bias introduced by "
    "replacing $\\theta$ by $\\hat\\theta$. This correction is simply realized by "
    "adding $k$,\" the parameter count. The result is\n"
    "$$ \\mathrm{AIC} \\;=\\; -2\\log(\\text{maximum likelihood}) + 2k. $$ {#eq-bg-aic}\n"
    "The model-selection application of @sec-derivations repeats this accounting with "
    "one additional bias source. Under multiple imputation the goodness-of-fit term is "
    "$-2\\bar Q_\\infty$ rather than the complete-data deviance, and the additional "
    "bias is exactly what the main theorem quantifies."
)

P10 = (
    "**Wilks.** Under a null hypothesis fixing $h - m$ of $h$ parameters, "
    "@wilksLargeSampleDistributionLikelihood1938a shows that $-2\\log\\lambda$ is "
    "distributed as $\\chi^2_{h-m}$ in large samples. This is the complete-data "
    "reference distribution. Every multiply imputed deviance in @sec-derivations is "
    "ultimately compared against it, and the complete-data replication principle asks "
    "when that comparison behaves as it would have with full data."
)

P11 = (
    "**Observed versus expected information under MAR.** "
    "@kenwardLikelihoodBasedFrequentist1998 sharpen Rubin's caution about frequentist "
    "inference. Under MAR the missingness indicator is not ancillary. The correct "
    "sampling framework is therefore unconditional over both the data and the "
    "missingness pattern. A \"naive\" expected information, computed as if the realized "
    "pattern were fixed by design, is biased, and MCAR is necessary and sufficient for "
    "the naive and unconditional forms to agree. Their recommendation is to use the "
    "observed information. Their bivariate Gaussian example shows where the difference "
    "lodges: under MAR dropout, the unconditional information acquires mean-covariance "
    "cross terms that the naive form misses. Both facts recur in @sec-derivations. The "
    "design-imbalance term $(A)+(C)$ is nonzero exactly when MCAR fails, and it is "
    "computed against the observed information, as they recommend. The observed-data "
    "information behind the one RIV of this paper carries exactly their MAR cross term."
)

P12 = (
    "**MI test combining, calibration, and the prior MI-AIC.** Three strands of prior "
    "work meet the applications directly, and each is restated here as the launch point "
    "it provides. First, the combining rule. @mengPerformingLikelihoodRatio1992b "
    "combine complete-data likelihood-ratio statistics across imputations into a single "
    "test statistic, calibrated against an $F$ reference under an equal-fractions "
    "assumption. @chanMultipleImprovementsMultiple2022 repair the procedure's known "
    "defects by switching the order of operations: their statistic\n"
    "$$ \\hat d_{\\mathrm{L}} \\;=\\; 2\\big\\{\\bar L(\\hat\\psi^{*}) - "
    "\\bar L(\\hat\\psi_0^{*})\\big\\}, \\qquad \\hat\\psi^{*} = \\arg\\max_\\psi "
    "\\bar L(\\psi), $$ {#eq-bg-dl}\n"
    "maximizes the averaged log-likelihood rather than averaging the maxima, and is "
    "nonnegative and invariant by construction. The numerator analyzed in "
    "@sec-derivations is exactly this maximize-then-average statistic. Second, the "
    "reference distribution. @chanGeneralFeasibleTests2022 drops the equal-fractions "
    "assumption entirely: stacking the imputed data sets yields estimators of every "
    "eigenvalue $r_j$ of the odds-of-missing-information matrix, and the limiting null "
    "law of the combined statistic is a weighted sum whose mean exceeds the parameter "
    "count by the total odds of missing information in the tested directions. That "
    "excess matters later: a reference built this way absorbs the corresponding bias in "
    "the numerator, so the bias bears on procedures that use no such reference. Third, "
    "the criterion. @consentinoclaeskensOrderSelectionTests2010 propose an AIC for "
    "multiply imputed data by attaching the Meng-Rubin combined statistic to the "
    "standard penalty. Their criterion does not analyze the bias of the averaged "
    "log-likelihood, and their closing assessment leaves the theory open. The corrected "
    "criterion of @sec-derivations is the answer to the question their proposal poses."
)

new_paras = []

def mk(idx, goal, proposition, dep, deptypes, prose, serves_L2, sets_up, topic, closing, flags, citations, numbers, notes):
    return {
        "id": idx, "section": "S2", "goal": goal, "proposition": proposition,
        "depends_on": dep, "dep_types": deptypes,
        "review": {"serves_L2": serves_L2, "serves_L1": "M2 BACKGROUND (three-tier gradient, D-04)",
                   "sets_up": sets_up, "topic_sentence": topic, "closing_sentence": closing,
                   "status": "drafted", "flags": flags},
        "draft_prose": prose,
        "audit": {"status": "complete", "citations": citations, "numbers": numbers, "notes": notes}
    }

new_paras.append(mk("S2-P1", "transition",
    "Why this section restates rather than cites: precision, the two standard conflations, and the notation-once rule.",
    ["S1-P7"], ["builds_on"], P1, "S2 goal statement (framing)", "all S2 paragraphs",
    "The argument of this paper rests on results that are individually standard.",
    "The section also fixes the paper's notation: every symbol is introduced here once and reused unchanged.",
    None, {}, {}, "Opener quarried from 180e2b5 background lead; plain cadence."))

new_paras.append(mk("S2-P2", "define_concept",
    "Notation: Y = (Y_obs, Y_mis), R; the two likelihoods; the two MLE targets theta_com and theta_obs and their roles.",
    ["S2-P1"], ["builds_on"], P2, "S2-SP1", "every later formal statement; S4 setup",
    "The basic objects are a data matrix and a missingness indicator.",
    "@sec-derivations instantiates this notation for the multivariate normal model; everything in this section is general.",
    None, {}, {}, "NEW paragraph (Tier 1 entry point); generalizes 180e2b5 sec-setup Objects, MVN instantiation deferred to S4."))

new_paras.append(mk("S2-P3", "define_concept",
    "Rubin 1976 ignorability: MAR + distinctness for likelihood/Bayes; stricter OAR/MCAR for sampling inference; the gap hosts (A)+(C) and the K-M distinction.",
    ["S2-P2"], ["builds_on"], P3, "S2-SP2", "S2-P11; S4 (A)+(C)",
    "@rubinInferenceMissingData1976b gives the weakest general conditions under which the process that causes missing data can be ignored.",
    "...two objects of this paper live inside it: the design-imbalance term $(A)+(C)$ of the main theorem, and the information-matrix distinction restated at the end of this section.",
    None,
    {"rubinInferenceMissingData1976b": "verified (read in-session 2026-06-06; MAR and distinctness definitions at :61-:65; sampling-vs-likelihood distinction SS9)"},
    {}, "Quarried from 180e2b5; plain cadence."))

new_paras.append(mk("S2-P4", "define_concept",
    "The missing-information principle (Orchard-Woodbury; Meng-Rubin form), the RIV defined and normalized by I_obs, and the EM-rate-matrix conflation warning.",
    ["S2-P2"], ["builds_on"], P4, "S2-SP3 (+ the EM-rate half of S2-SP7)", "every trace formula; S4 throughout",
    "Information matrices add across the missing-data split.",
    "The notation keeps them apart.",
    None,
    {"woodburyMissingInformationPrinciple1972": "verified (read in-session 2026-06-06; score identity and information decomposition at :59-:86)",
     "Meng01121991": "verified (read in-session 2026-06-06; 'missing information principle' :211; rate matrix DM :137)",
     "dempsterMaximumLikelihoodIncomplete1977a": "verified (read in-session 2026-06-06; DM form per Meng-Rubin's attribution)"},
    {}, "Quarried from 180e2b5; RIV definition display added (was prose); T-01 one-RIV discipline."))

new_paras.append(mk("S2-P5", "define_concept",
    "Dempster Q-function: definition, the Q = L + H split (the theorem is an account of H), and curvature I_com (the geometric fact behind the LRT result).",
    ["S2-P4"], ["builds_on"], P5, "S2-SP4", "S4a (H-term account), S4b (I_com metric)",
    "@dempsterMaximumLikelihoodIncomplete1977a define [the Q-function].",
    "...constrained fits of the averaged log-likelihood project in the $I_{\\text{com}}$ metric.",
    None,
    {"dempsterMaximumLikelihoodIncomplete1977a": "verified (read in-session 2026-06-06; 'since we do not know...' quote verbatim at :259; Q definition)"},
    {}, "Quarried from 180e2b5; the two load-bearing facts kept, rate-quote trimmed (rate material lives in P4)."))

new_paras.append(mk("S2-P6", "define_concept",
    "Wei-Tanner: imputation is Monte Carlo integration of the E-step; Q-bar-infinity defined; FITTED conditioning flagged as sign-determining.",
    ["S2-P5"], ["builds_on"], P6, "S2-SP4", "S4a (fitted-vs-oracle, D-02)",
    "@weiMonteCarloImplementation1990 implement the E-step by simulation.",
    "...@sec-derivations states both versions to prevent the standard confusion.",
    None,
    {"weiMonteCarloImplementation1990": "verified (read in-session 2026-06-06; Remark 2 quote verbatim at :74)"},
    {}, "Quarried from 180e2b5; MCEM display dropped for cadence (the average is described in words; the formal object returns in S4)."))

new_paras.append(mk("S2-P7", "define_concept",
    "Rubin's rules are exact posterior-moment identities (Result 3.2); r_inf = B/U-bar (3.1.7); one named approximation separates identities from inference.",
    ["S2-P4"], ["builds_on"], P7, "S2-SP5", "S4a (the theorem uses the identities through the likelihood)",
    "For multiply imputed data, Result 3.2 of @rubinMultipleImputationNonresponse1987 shows two things.",
    "The main theorem describes what happens when the exact moment identities are used not as moments but through the likelihood itself.",
    None,
    {"rubinMultipleImputationNonresponse1987": "verified (read in-session 2026-06-06; Result 3.2 at :2438-:2476; r_inf eq 3.1.7 at :2534; 'usual approximation' quote at :2538)",
     "Tierney01031986": "verified (Laplace-approximation pointer; held from 180e2b5 verification, role unchanged)"},
    {}, "Quarried from 180e2b5; plain cadence."))

new_paras.append(mk("S2-P8", "define_concept",
    "Congeniality (Meng 1994): definition; assumed throughout; the bias is what remains after imputer-analyst agreement.",
    ["S2-P7"], ["builds_on"], P8, "S2-SP5", "S4 scope; S6 limits",
    "@mengMultipleImputationInferencesUncongenial1994a formalizes when the imputer and the analyst agree.",
    "It is what remains after they agree.",
    None,
    {"mengMultipleImputationInferencesUncongenial1994a": "verified (read in-session 2026-06-06; congeniality formalization per abstract + SS1)"},
    {}, "Quarried from 180e2b5; plain cadence."))

new_paras.append(mk("S2-P9", "define_concept",
    "Akaike: AIC as a bias-corrected plug-in estimate; the IC application repeats the accounting with one additional bias source.",
    ["S2-P6"], ["builds_on"], P9, "S2-SP6", "S4c (corrected criterion)",
    "@akaikeNewLookStatistical1974a evaluates a fitted model by its mean log-likelihood against the true distribution.",
    "...the additional bias is exactly what the main theorem quantifies.",
    None,
    {"akaikeNewLookStatistical1974a": "verified (read in-session 2026-06-06; 'downward bias... adding k' quote verbatim at :148)"},
    {}, "Quarried from 180e2b5; plain cadence."))

new_paras.append(mk("S2-P10", "define_concept",
    "Wilks: -2 log lambda -> chi-square_{h-m}; the complete-data reference the replication principle compares against.",
    ["S2-P9"], ["builds_on"], P10, "S2-SP6", "S4b/S4c references; S1-P3 principle",
    "Under a null hypothesis fixing $h - m$ of $h$ parameters, @wilksLargeSampleDistributionLikelihood1938a shows that $-2\\log\\lambda$ is distributed as $\\chi^2_{h-m}$ in large samples.",
    "...the complete-data replication principle asks when that comparison behaves as it would have with full data.",
    None,
    {"wilksLargeSampleDistributionLikelihood1938a": "verified (read in-session 2026-06-06; chi-square characteristic-function conclusion at :96)"},
    {}, "Quarried from 180e2b5; tied to the principle (new clause)."))

new_paras.append(mk("S2-P11", "define_concept",
    "Kenward-Molenberghs: R not ancillary under MAR; unconditional framework; naive vs unconditional expected information (MCAR iff equal); observed information recommended; MAR cross terms.",
    ["S2-P3"], ["builds_on"], P11, "S2-SP7", "S4a ((A)+(C) convention, T-02); the one-RIV (T-01)",
    "@kenwardLikelihoodBasedFrequentist1998 sharpen Rubin's caution about frequentist inference.",
    "The observed-data information behind the one RIV of this paper carries exactly their MAR cross term.",
    None,
    {"kenwardLikelihoodBasedFrequentist1998": "verified (read in-session 2026-06-06; naive vs unconditional construction at :128-:140; observed-information recommendation :111)"},
    {}, "Quarried from 180e2b5; plain cadence."))

new_paras.append(mk("S2-P12", "position_lineage",
    "Three launch points: Meng-Rubin combining -> Chan-Meng maximize-then-average numerator (the analyzed statistic) -> Chan reference (absorption); and the prior MI-AIC (C-C 2010) whose open theory Application II answers.",
    ["S2-P7", "S2-P10"], ["builds_on", "builds_on"], P12, "S2-SP8", "S4b (numerator + absorption), S4c (criterion)",
    "Three strands of prior work meet the applications directly, and each is restated here as the launch point it provides.",
    "The corrected criterion of @sec-derivations is the answer to the question their proposal poses.",
    None,
    {"mengPerformingLikelihoodRatio1992b": "verified (read in-session 2026-06-06; D_L procedure SS3)",
     "chanMultipleImprovementsMultiple2022": "verified (read in-session 2026-06-06; maximize-then-average construction; defects repaired)",
     "chanGeneralFeasibleTests2022": "verified (read in-session 2026-06-06; r_1:k estimation; weighted-sum null law, eq 1.10)",
     "consentinoclaeskensOrderSelectionTests2010": "verified (read in-session 2026-06-06; SS5 aic_D = D-tilde_S - 2p_S; open-theory closing quote :404)"},
    {"null-law mean exceeds k by total odds of missing information": "lit:chanGeneralFeasibleTests2022"},
    "Quarried from 180e2b5 with the C-C 2010 strand ADDED (level2 cycle-1 decision: the prior MI-AIC enters the lineage)."))

l3["paragraphs"].extend(new_paras)
l3["metadata"]["status"] = "drafting_s2_complete"
l3["metrics_gate"]["notes"] = (
    "Partial evaluation after S2 drafting (2026-06-06): S1 7 + S2 12 = 19 paragraphs; "
    "all carry propositions/goals; S2 quotes re-verified in-session against the "
    "literature files; dependency graph acyclic (S2-P1 hangs off S1-P7). S2 estimated "
    "12-15 in the blueprint, drafted at 12. Full gate when all six sections drafted."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# ---------------------------------------------------------------- Level 4 (S2)
with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)

s2 = [
    ("E-S2-P3-1", "S2-P3", "lit:rubinInferenceMissingData1976b", "MAR definition :61; distinctness :65; sampling-vs-likelihood SS9.", "Ignorability restatement."),
    ("E-S2-P4-1", "S2-P4", "lit:woodburyMissingInformationPrinciple1972", "Score identity + information decomposition (:59-:86).", "MIP primary source."),
    ("E-S2-P4-2", "S2-P4", "lit:Meng01121991", "'missing information principle' :211; DM rate matrix :137.", "The I_obs = I_com - I_mis form + the rate-matrix contrast."),
    ("E-S2-P5-1", "S2-P5", "lit:dempsterMaximumLikelihoodIncomplete1977a", "'since we do not know...' :259; Q definition.", "Q-function restatement; Q = L + H; curvature I_com."),
    ("E-S2-P6-1", "S2-P6", "lit:weiMonteCarloImplementation1990", "Remark 2 :74: 'Rubin (1987) referred to the quantities z(1),...,z(m) as multiple imputations.'", "The MCEM bridge."),
    ("E-S2-P7-1", "S2-P7", "lit:rubinMultipleImputationNonresponse1987", "Result 3.2 :2438; r_inf (3.1.7) :2534; 'usual approximation' :2538.", "Exact identities + the one approximation."),
    ("E-S2-P7-2", "S2-P7", "lit:Tierney01031986", "Laplace-type posterior approximation.", "The named approximation's source."),
    ("E-S2-P8-1", "S2-P8", "lit:mengMultipleImputationInferencesUncongenial1994a", "Congeniality formalization (abstract + SS1).", "Scope assumption."),
    ("E-S2-P9-1", "S2-P9", "lit:akaikeNewLookStatistical1974a", "'downward bias... simply realized by adding k' :148.", "AIC as plug-in correction."),
    ("E-S2-P10-1", "S2-P10", "lit:wilksLargeSampleDistributionLikelihood1938a", "chi-square_{h-m} conclusion :96.", "Complete-data reference."),
    ("E-S2-P11-1", "S2-P11", "lit:kenwardLikelihoodBasedFrequentist1998", "Naive vs unconditional information :128-:140; observed-info recommendation :111.", "T-02 convention + MAR cross terms."),
    ("E-S2-P12-1", "S2-P12", "lit:mengPerformingLikelihoodRatio1992b", "Combining rule (SS2-3).", "Launch point 1."),
    ("E-S2-P12-2", "S2-P12", "lit:chanMultipleImprovementsMultiple2022", "Maximize-then-average statistic; defect repairs.", "The analyzed numerator."),
    ("E-S2-P12-3", "S2-P12", "lit:chanGeneralFeasibleTests2022", "Eigenvalue estimation; weighted-sum null law (eq 1.10).", "Absorption property feeding S4b."),
    ("E-S2-P12-4", "S2-P12", "lit:consentinoclaeskensOrderSelectionTests2010", "SS5: aic_D; open-theory closing statement :404.", "The prior MI-AIC whose question S4c answers."),
]
l4["evidence_map"].extend([
    {"id": a, "proposition_id": b, "pointer": c, "evidence_status": "verified", "passage_or_value": d, "note": e}
    for a, b, c, d, e in s2
])
l4["metrics_gate"]["notes"] = (
    "S1 + S2 populated (2026-06-06): every drafted paragraph has >=1 entry; all "
    "pointers resolve. Full gate when all sections drafted."
)

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S2 drafted: 12 paragraphs into level3, 15 evidence entries into level4")
