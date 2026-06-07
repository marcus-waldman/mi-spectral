# S2 - use-first restructure + proper-imputation paragraph, 2026-06-06
#
# Marcus's feedback on the first S2 draft (4f7733c):
#   1. Read like a literature review - "why are you telling me all this?" Every
#      restatement must open with its ROLE in this paper (assumption / central
#      object / machinery / baseline / launch point), source second. Recorded in
#      CLAUDE.md prose-style section + feedback memory.
#   2. P1 read as self-justification - replaced by a five-item roadmap.
#   3. MISSING SUBSTANCE: proper imputation was never restated. The MCEM/Wei-Tanner
#      construction is IMPROPER (draws at a fixed parameter); the deterministic-EM
#      lineage (Cavanaugh-Shumway, Shimodaira) lives there; this paper's extension
#      to PROPER MI is novelty three and the known-scale arms (0 vs -1/2 tr) price
#      the distinction exactly. New P7 added (Rubin 1987 ch.4; Nielsen 2003);
#      P6 ending sharpened to mark the improperness; P1 roadmap names proper
#      imputation among the standing assumptions.
# S2 is now 13 paragraphs (blueprint range 12-15). Old P7-P12 -> P8-P13.
# Note for the S1 session: consider adding "improper" to S1-P6's
# "deterministic EM estimation" clause for terminological continuity.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

s1_paras = [p for p in l3["paragraphs"] if p["section"] == "S1"]
old_s2 = {p["id"]: p for p in l3["paragraphs"] if p["section"] == "S2"}

P1 = (
    "This section fixes the paper's notation and assembles the results the derivations "
    "use. The reader needs five things. First, the two likelihoods of incomplete data "
    "and their two maximizers; the bias this paper derives is the distance between "
    "functions of these. Second, the standing assumptions: ignorable missingness, and "
    "congenial, proper imputation. Third, the paper's central matrix, the RIV, which "
    "comes from the missing-information principle. Fourth, the machinery behind the "
    "averaged log-likelihood: the EM Q-function, its Monte Carlo implementation, and "
    "Rubin's combining rules. Fifth, the complete-data baselines --- AIC and Wilks --- "
    "and the three prior results the applications extend. Each item is restated in its "
    "source's own terms, and each restatement names the later result that uses it. "
    "Symbols introduced here are used unchanged throughout."
)

P2 = old_s2["S2-P2"]["draft_prose"]  # unchanged (already use-first)

P3 = (
    "**Ignorability.** This paper assumes throughout that the missingness mechanism is "
    "ignorable. The assumption and its conditions are Rubin's "
    "[@rubinInferenceMissingData1976b]: the data must be missing at random --- the "
    "conditional probability of the observed missingness pattern is the same for all "
    "values of the missing data --- and the mechanism's parameter must be distinct from "
    "the data parameter. These are the weakest general conditions for ignoring the "
    "mechanism in likelihood and Bayesian inference. Sampling-distribution inference is "
    "stricter. It requires in addition that the observed data are observed at random, "
    "which together with MAR amounts to MCAR, and it is otherwise generally conditional "
    "on the observed pattern. The gap between the two senses of \"ignorable\" is not a "
    "technicality for this paper; two of its objects live inside that gap. The "
    "design-imbalance term $(A)+(C)$ of the main theorem is one. The information-matrix "
    "distinction restated at the end of this section is the other."
)

P4 = (
    "**The missing-information principle and the RIV.** The paper's central matrix is "
    "the relative-increase-in-variance matrix, and it comes from the "
    "missing-information principle. @woodburyMissingInformationPrinciple1972 decompose "
    "the information in the complete data as the observed-data information plus what "
    "they call the lost information, together with a score identity: the observed-data "
    "score is the conditional expectation of the complete-data score. @Meng01121991 "
    "state the same principle in the form used throughout this paper,\n"
    "$$ I_{\\text{obs}} \\;=\\; I_{\\text{com}} - I_{\\text{mis}\\mid\\text{obs}}, $$ {#eq-bg-mip}\n"
    "\"observed information = complete information $-$ missing information.\" The "
    "central matrix is built from these ingredients:\n"
    "$$ \\mathrm{RIV} \\;=\\; I_{\\text{obs}}^{-1}\\, I_{\\text{mis}\\mid\\text{obs}}. $$ {#eq-bg-riv}\n"
    "Its trace adds up the odds of missing information about each parameter, and it is "
    "the matrix form of Rubin's scalar relative increase in variance, restated below. "
    "One warning is needed here. The EM literature works with a different normalization "
    "of the same ingredients: the EM rate matrix "
    "$DM = I_{\\text{mis}\\mid\\text{obs}}\\, I_{\\text{com}}^{-1}$ of "
    "@dempsterMaximumLikelihoodIncomplete1977a and @Meng01121991. The RIV divides by "
    "the observed-data information; the rate matrix divides by the complete-data "
    "information. The two matrices have different eigenvalues, and conflating them "
    "corrupts every trace formula in this paper. The notation keeps them apart."
)

P5 = (
    "**EM and the Q-function.** The object whose bias this paper derives is a "
    "Q-function, so its definition and one geometric fact about it are needed. "
    "@dempsterMaximumLikelihoodIncomplete1977a define\n"
    "$$ Q(\\phi' \\mid \\phi) \\;=\\; E\\big(\\log f(\\mathbf{x} \\mid \\phi') "
    "\\,\\big|\\, \\mathbf{y}, \\phi\\big), $$ {#eq-bg-q}\n"
    "the expected complete-data log-likelihood given the observed data. The E-step "
    "computes $Q(\\cdot \\mid \\phi^{(p)})$ and the M-step maximizes it. Their "
    "heuristic is direct: \"since we do not know $\\log f(\\mathbf{x}\\mid\\phi)$, we "
    "maximize instead its current expectation given the data $\\mathbf{y}$ and the "
    "current fit $\\phi^{(p)}$.\" Two facts from their analysis carry the weight later. "
    "First, the Q-function decomposes as "
    "$Q(\\phi'\\mid\\phi) = L(\\phi') + H(\\phi'\\mid\\phi)$, where $L$ is the "
    "observed-data log-likelihood and $H$ is a conditional-entropy term. The main "
    "theorem is, at bottom, an account of what the $H$ term does when its parameters "
    "are estimated rather than known. Second, the curvature of $Q$ at its maximizer is "
    "the complete-data information $I_{\\text{com}}$, not the observed-data "
    "information. This single geometric fact drives the likelihood-ratio result: "
    "constrained fits of the averaged log-likelihood project in the $I_{\\text{com}}$ "
    "metric."
)

P6 = (
    "**Imputation is Monte Carlo integration of the E-step.** The averaged "
    "log-likelihood over imputations is itself a Q-function, computed by Monte Carlo. "
    "@weiMonteCarloImplementation1990 implement the E-step by simulation: draws "
    "$z^{(1)},\\dots,z^{(m)}$ from the conditional predictive distribution of the "
    "missing data replace the E-step integral by an average over completed data sets. "
    "Their Remark 2 makes the connection to multiple imputation explicit: \"Rubin "
    "(1987) referred to the quantities $z^{(1)}, \\ldots, z^{(m)}$ as multiple "
    "imputations.\" One feature of this construction must be marked at once: the draws "
    "are taken at a *fixed* parameter value --- the current iterate, or in the limit "
    "the observed-data estimate. Imputation at a fixed parameter value is what Rubin "
    "calls *improper*. The $m \\to \\infty$ limit of the averaged log-likelihood, "
    "written $\\bar Q_\\infty(\\theta)$, is the central object of this paper, and the "
    "next paragraph states the form of imputation under which this paper studies it."
)

P7 = (
    "**Proper imputation.** The imputations this paper studies are proper in Rubin's "
    "sense, and the distinction between proper and improper imputation does real work "
    "in the theorem. Proper imputation propagates parameter uncertainty: a parameter "
    "value is first drawn from its posterior given the observed data, and the missing "
    "values are then drawn from the predictive distribution at that drawn value. "
    "Chapter 4 of @rubinMultipleImputationNonresponse1987 states the validity "
    "conditions and gives the fully normal Bayesian scheme as the canonical example. "
    "Improper imputation skips the first draw and imputes at a fixed parameter value. "
    "The Monte Carlo E-step of the previous paragraph is improper by construction, and "
    "so is the entire deterministic-EM lineage in which the earlier missing-data "
    "criteria were derived [@cavanaughAkaikeInformationCriterion1998a; "
    "@shimodairaInformationCriterionModel2017]. The distinction is not bookkeeping. "
    "The extra posterior draw contributes its own variation to the averaged "
    "log-likelihood, and the main theorem prices it exactly: in the known-scale case, "
    "the bias is zero under improper imputation at the observed-data estimate and "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ under proper imputation, so the two "
    "forms differ by precisely the posterior-draw contribution. Properness is also not "
    "absolute: @nielsenProperImproperMultiple2003 shows that Bayesian imputations are "
    "proper when the analyst's complete-data estimator is the maximum likelihood "
    "estimator, and that the same imputations can fail to be proper for a different "
    "estimator. This paper's analyst always uses the complete-data MLE, which is the "
    "case where congeniality implies properness "
    "[@mengMultipleImputationInferencesUncongenial1994a; "
    "@nielsenProperImproperMultiple2003]. The extension of the bias accounting from "
    "the improper, deterministic Q-function to proper multiple imputation is one of "
    "the things this paper adds."
)

P8 = (
    "**Rubin's rules are exact posterior-moment identities.** The derivations use "
    "Rubin's combining rules not as moment formulas but through the likelihood, and "
    "for that they are needed in their exact form. Result 3.2 of "
    "@rubinMultipleImputationNonresponse1987 shows two things. The posterior mean of "
    "an estimand given the observed data equals the average of the completed-data "
    "posterior means. The posterior variance equals the average completed-data "
    "variance plus the variance of the completed-data means. These are the ordinary "
    "rules for conditional moments, applied to imputation, and with infinitely many "
    "imputations they are exact identities rather than asymptotic approximations. In "
    "Rubin's notation they give $\\bar Q_\\infty$, $\\bar U_\\infty$, $B_\\infty$, and "
    "the total variance $T_\\infty = \\bar U_\\infty + B_\\infty$. Rubin then defines "
    "the scalar relative increase in variance due to nonresponse,\n"
    "$$ r_\\infty \\;=\\; B_\\infty / \\bar U_\\infty $$ {#eq-bg-rinf}\n"
    "(his equation 3.1.7). The RIV matrix of @eq-bg-riv is this quantity in matrix "
    "form. A single approximation separates the exact identities from usable "
    "inference: \"the usual approximation of the posterior distribution as normal\" (a "
    "Laplace-type approximation; @Tierney01031986). The main theorem describes what "
    "happens when the exact moment identities are used not as moments but through the "
    "likelihood itself."
)

P9 = (
    "**Congeniality.** The second standing assumption is congeniality: the imputer and "
    "the analyst agree. @mengMultipleImputationInferencesUncongenial1994a formalizes "
    "the agreement. An analysis procedure is congenial to an imputation model if there "
    "exists one Bayesian model that reproduces both --- its posterior means and "
    "variances asymptotically match the analyst's complete-data and incomplete-data "
    "procedures, and its posterior predictive distribution for the missing data is the "
    "imputation model. Everything in this paper assumes congenial, proper imputation. "
    "This assumption is what gives the main theorem its force: the bias derived there "
    "is not an artifact of imputer-analyst disagreement. It is what remains after they "
    "agree."
)

P10 = (
    "**AIC is a bias-corrected plug-in estimate.** The model-selection application "
    "corrects AIC, so AIC's own logic is needed first. @akaikeNewLookStatistical1974a "
    "evaluates a fitted model by its mean log-likelihood against the true "
    "distribution. The maximized log-likelihood is the natural estimate of this "
    "criterion, and it is too optimistic: it \"needs a correction for the downward "
    "bias introduced by replacing $\\theta$ by $\\hat\\theta$. This correction is "
    "simply realized by adding $k$,\" the parameter count. The result is\n"
    "$$ \\mathrm{AIC} \\;=\\; -2\\log(\\text{maximum likelihood}) + 2k. $$ {#eq-bg-aic}\n"
    "The model-selection application repeats this accounting with one additional bias "
    "source. Under multiple imputation the goodness-of-fit term is $-2\\bar Q_\\infty$ "
    "rather than the complete-data deviance, and the additional bias is exactly what "
    "the main theorem quantifies."
)

P11 = (
    "**Wilks.** The complete-data baseline for testing is Wilks' theorem, and the "
    "replication principle is defined against it. Under a null hypothesis fixing "
    "$h - m$ of $h$ parameters, @wilksLargeSampleDistributionLikelihood1938a shows "
    "that $-2\\log\\lambda$ is distributed as $\\chi^2_{h-m}$ in large samples. Every "
    "multiply imputed deviance in this paper is ultimately compared against this "
    "reference, and the complete-data replication principle asks when that comparison "
    "behaves as it would have with full data."
)

P12 = (
    "**Observed versus expected information under MAR.** One convention must be fixed "
    "before any trace in this paper is computed: which information matrix to use under "
    "MAR. @kenwardLikelihoodBasedFrequentist1998 settle it. Under MAR the missingness "
    "indicator is not ancillary, so the correct sampling framework is unconditional "
    "over both the data and the missingness pattern. A \"naive\" expected information, "
    "computed as if the realized pattern were fixed by design, is biased, and MCAR is "
    "necessary and sufficient for the naive and unconditional forms to agree. Their "
    "recommendation is to use the observed information, and this paper follows it. "
    "Their bivariate Gaussian example shows where the difference lodges: under MAR "
    "dropout, the unconditional information acquires mean-covariance cross terms that "
    "the naive form misses. Both facts recur in @sec-derivations. The design-imbalance "
    "term $(A)+(C)$ is nonzero exactly when MCAR fails, and it is computed against the "
    "observed information. The observed-data information behind the one RIV of this "
    "paper carries exactly their MAR cross term."
)

P13 = old_s2["S2-P12"]["draft_prose"]  # launch points - opening already functional

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

o = old_s2
new_s2 = [
    mk("S2-P1", "transition",
       "Roadmap: notation; standing assumptions (ignorability, congenial proper imputation); the RIV; the Q-machinery; the baselines and launch points.",
       ["S1-P7"], ["builds_on"], P1, "S2 goal statement (framing)", "all S2 paragraphs",
       "This section fixes the paper's notation and assembles the results the derivations use.",
       "Symbols introduced here are used unchanged throughout.",
       None, {}, {}, "Rewritten as a roadmap (use-first feedback); self-justification removed."),
    mk("S2-P2", o["S2-P2"]["goal"], o["S2-P2"]["proposition"], ["S2-P1"], ["builds_on"], P2,
       "S2-SP1", o["S2-P2"]["review"]["sets_up"],
       o["S2-P2"]["review"]["topic_sentence"], o["S2-P2"]["review"]["closing_sentence"],
       None, o["S2-P2"]["audit"]["citations"], {}, o["S2-P2"]["audit"]["notes"]),
    mk("S2-P3", "define_concept",
       "First standing assumption: ignorability (assumption-first), with Rubin's conditions and the gap that hosts (A)+(C) and the information convention.",
       ["S2-P2"], ["builds_on"], P3, "S2-SP2", "S2-P12; S4 (A)+(C)",
       "This paper assumes throughout that the missingness mechanism is ignorable.",
       "The information-matrix distinction restated at the end of this section is the other.",
       None, o["S2-P3"]["audit"]["citations"], {}, "Use-first rewrite of the first draft."),
    mk("S2-P4", "define_concept",
       "The central matrix (RIV) defined use-first from the missing-information principle; EM-rate-matrix conflation warning.",
       ["S2-P2"], ["builds_on"], P4, "S2-SP3 (+ the EM-rate half of S2-SP7)", "every trace formula; S4 throughout",
       "The paper's central matrix is the relative-increase-in-variance matrix, and it comes from the missing-information principle.",
       "The notation keeps them apart.",
       None, o["S2-P4"]["audit"]["citations"], {}, "Use-first rewrite."),
    mk("S2-P5", "define_concept",
       "The Q-function (use-first): definition, Q = L + H, curvature I_com.",
       ["S2-P4"], ["builds_on"], P5, "S2-SP4", "S4a (H-term account), S4b (I_com metric)",
       "The object whose bias this paper derives is a Q-function, so its definition and one geometric fact about it are needed.",
       "...constrained fits of the averaged log-likelihood project in the $I_{\\text{com}}$ metric.",
       None, o["S2-P5"]["audit"]["citations"], {}, "Use-first rewrite."),
    mk("S2-P6", "define_concept",
       "The MCEM bridge with the improperness marked: draws at a FIXED parameter value; Q-bar-infinity named; hands off to proper imputation.",
       ["S2-P5"], ["builds_on"], P6, "S2-SP4", "S2-P7 (proper imputation); S4a (fitted-vs-oracle)",
       "The averaged log-likelihood over imputations is itself a Q-function, computed by Monte Carlo.",
       "...the next paragraph states the form of imputation under which this paper studies it.",
       None, o["S2-P6"]["audit"]["citations"], {}, "Improperness of fixed-parameter draws made explicit (Marcus 2026-06-06); hands off to the new P7."),
    mk("S2-P7", "define_concept",
       "NEW: proper vs improper imputation - definition (posterior draw first), Rubin ch.4 conditions; MCEM and the deterministic-EM lineage are improper; the theorem prices the distinction (known-scale arms 0 vs -1/2 tr); properness is analysis-relative (Nielsen); MLE analyst => congeniality implies properness; extension to proper MI is a contribution.",
       ["S2-P6"], ["builds_on"], P7, "S2-SP5 (+ scope of SP8's lineage)", "S4a (known-scale collapse, C_n); S1-P6 novelty item three",
       "The imputations this paper studies are proper in Rubin's sense, and the distinction between proper and improper imputation does real work in the theorem.",
       "The extension of the bias accounting from the improper, deterministic Q-function to proper multiple imputation is one of the things this paper adds.",
       None,
       {"rubinMultipleImputationNonresponse1987": "verified (read in-session 2026-06-06; ch.4 SS4.2-4.4 validity conditions + proper/improper examples incl. fully normal Bayesian, per ToC :236-:254)",
        "cavanaughAkaikeInformationCriterion1998a": "verified (read in-session 2026-06-06; EM/SEM complete-data-tools construction = deterministic, improper)",
        "shimodairaInformationCriterionModel2017": "verified (read in-session 2026-06-06; deterministic EM estimation, fixed-pattern setting)",
        "nielsenProperImproperMultiple2003": "verified (read in-session 2026-06-06; :177 Bayesian MI proper when complete-data estimator is the MLE; :265 properness analysis-relative; :335 congeniality implies properness)",
        "mengMultipleImputationInferencesUncongenial1994a": "verified (congeniality; via Nielsen :335 link)"},
       {"known-scale arms: 0 (improper at theta-hat-obs) vs -1/2 tr(RIV) (proper)": "deriv:sec-thm"},
       "NEW paragraph (Marcus 2026-06-06: proper imputation was never invoked; MCEM is improper; Shumway-line results do not touch proper MI)."),
    mk("S2-P8", "define_concept", o["S2-P7"]["proposition"], ["S2-P4"], ["builds_on"], P8,
       "S2-SP5", o["S2-P7"]["review"]["sets_up"],
       "The derivations use Rubin's combining rules not as moment formulas but through the likelihood, and for that they are needed in their exact form.",
       o["S2-P7"]["review"]["closing_sentence"],
       None, o["S2-P7"]["audit"]["citations"], {}, "Use-first rewrite; renumbered from P7."),
    mk("S2-P9", "define_concept", o["S2-P8"]["proposition"], ["S2-P7", "S2-P8"], ["builds_on", "builds_on"], P9,
       "S2-SP5", o["S2-P8"]["review"]["sets_up"],
       "The second standing assumption is congeniality: the imputer and the analyst agree.",
       "It is what remains after they agree.",
       None, o["S2-P8"]["audit"]["citations"], {}, "Use-first rewrite; renumbered from P8; now also depends on P7 (proper)."),
    mk("S2-P10", "define_concept", o["S2-P9"]["proposition"], ["S2-P6"], ["builds_on"], P10,
       "S2-SP6", o["S2-P9"]["review"]["sets_up"],
       "The model-selection application corrects AIC, so AIC's own logic is needed first.",
       "...the additional bias is exactly what the main theorem quantifies.",
       None, o["S2-P9"]["audit"]["citations"], {}, "Use-first rewrite; renumbered from P9."),
    mk("S2-P11", "define_concept", o["S2-P10"]["proposition"], ["S2-P10"], ["builds_on"], P11,
       "S2-SP6", o["S2-P10"]["review"]["sets_up"],
       "The complete-data baseline for testing is Wilks' theorem, and the replication principle is defined against it.",
       o["S2-P10"]["review"]["closing_sentence"],
       None, o["S2-P10"]["audit"]["citations"], {}, "Use-first rewrite; renumbered from P10."),
    mk("S2-P12", "define_concept", o["S2-P11"]["proposition"], ["S2-P3"], ["builds_on"], P12,
       "S2-SP7", o["S2-P11"]["review"]["sets_up"],
       "One convention must be fixed before any trace in this paper is computed: which information matrix to use under MAR.",
       o["S2-P11"]["review"]["closing_sentence"],
       None, o["S2-P11"]["audit"]["citations"], {}, "Use-first rewrite; renumbered from P11."),
    mk("S2-P13", "position_lineage", o["S2-P12"]["proposition"], ["S2-P8", "S2-P11"], ["builds_on", "builds_on"], P13,
       "S2-SP8", o["S2-P12"]["review"]["sets_up"],
       o["S2-P12"]["review"]["topic_sentence"], o["S2-P12"]["review"]["closing_sentence"],
       None, o["S2-P12"]["audit"]["citations"], o["S2-P12"]["audit"]["numbers"],
       "Renumbered from P12; opening already functional."),
]

l3["paragraphs"] = s1_paras + new_s2
l3["metadata"]["status"] = "drafting_s2_rewritten"
l3["metrics_gate"]["notes"] = (
    "After the S2 use-first rewrite (2026-06-06): S1 7 + S2 13 = 20 paragraphs; "
    "use-first openings throughout S2; new P7 (proper imputation) with in-session "
    "verified sources; dependency graph acyclic. Note for the S1 session: add "
    "'improper' to S1-P6's deterministic-EM clause. Full gate when all sections drafted."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# ---------------------------------------------------------------- Level 4
with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)

renumber = {"S2-P7": "S2-P8", "S2-P8": "S2-P9", "S2-P9": "S2-P10",
            "S2-P10": "S2-P11", "S2-P11": "S2-P12", "S2-P12": "S2-P13"}
for e in l4["evidence_map"]:
    pid = e["proposition_id"]
    if pid in renumber:
        e["proposition_id"] = renumber[pid]
        for a, b in renumber.items():
            if "-" + a.split("-")[1] + "-" in e["id"] and e["id"].startswith("E-S2"):
                pass  # ids kept stable except the section-paragraph token below
        e["id"] = e["id"].replace("E-" + pid + "-", "E-" + renumber[pid] + "-") if ("E-" + pid + "-") in e["id"] else e["id"]

l4["evidence_map"].extend([
    {"id": "E-S2-P7-1", "proposition_id": "S2-P7", "pointer": "lit:rubinMultipleImputationNonresponse1987",
     "evidence_status": "verified",
     "passage_or_value": "Ch.4: SS4.2 randomization-validity conditions; SS4.3 proper/improper examples incl. Example 4.2 (fully normal Bayesian); SS4.4 further discussion.",
     "note": "Proper-imputation definition and conditions."},
    {"id": "E-S2-P7-2", "proposition_id": "S2-P7", "pointer": "lit:nielsenProperImproperMultiple2003",
     "evidence_status": "verified",
     "passage_or_value": ":177 'Bayesian multiple imputations are proper, when the complete data estimator is the complete data MLE'; :265 properness analysis-relative; :335 congeniality implies properness (m=inf).",
     "note": "Properness scoping; the MLE-analyst case this paper occupies."},
    {"id": "E-S2-P7-3", "proposition_id": "S2-P7", "pointer": "deriv:sec-thm",
     "evidence_status": "verified",
     "passage_or_value": "Known-scale arms: 0 (deterministic/improper) vs -1/2 tr(RIV) (proper MI); difference = posterior-draw contribution C_n.",
     "note": "Why the distinction does work in the theorem."},
])
l4["metrics_gate"]["notes"] = (
    "S1 + S2 populated; S2 renumbered after the proper-imputation insertion "
    "(P7 new; old P7-P12 -> P8-P13). All pointers resolve."
)

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S2 rewritten: 13 paragraphs (use-first + proper imputation); level4 renumbered + 3 new entries")
