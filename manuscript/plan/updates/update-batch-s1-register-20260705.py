# Sweep batch 1: abstract + S1 + S1B to the D-26 register (todo/048 Phase D(ii)).
#
# Gate: Marcus approved manuscript/reviews/style/batch-S1-proposal-2026-07-05.md
# ("I approve", 2026-07-05). Register changes and R11 precision changes are
# labeled per unit below. Propositions are untouched: a style pass changes how
# things are said, never what is claimed (todo/048 ground rule 2).
#
# Units: S1-P1 (Demo 1), S1-P2, S1-P3 (register), S1-P4 (Demo 2 + R11 rescope #1),
# S1-P5 (register + Bucket-2 "genuinely"->"truly" + E3 thin + R10 formula retired;
# signature sentence kept per D-26), S1-P6 (register + R11 rescope #2),
# S1B-P1 (one-sentence R10 formula retirement). Abstract, S1-P6b, S1-P7, S1B-P2:
# NO CHANGE per the approved proposal.
#
# Guards: every replacement asserts the CURRENT text exactly (full-string for
# whole-paragraph rewrites, substring for the S1B-P1 partial) so drift aborts
# the script before any write.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

# ---------------------------------------------------------------- S1-P1 (Demo 1)
OLD_P1 = (
    "Multiple imputation treats missing data through a division of labor, and that "
    "division has served applied research for nearly four decades. An imputer fills in "
    "the missing values several times from a model for the complete data. An analyst "
    "then fits the model of substantive interest to each completed data set, and simple "
    "rules combine the results [@rubinMultipleImputationNonresponse1987]. The field's "
    "own accounts of its state of the art describe a mature methodology "
    "[@schaferMissingDataOur2002a; @endersMissingDataUpdate2025]. In those accounts the "
    "role of the missing-data mechanism is understood, point estimates recover their "
    "complete-data targets under stated conditions, and Wald-type tests for single and "
    "multiple parameters are well calibrated. On that testimony, the major inferential "
    "questions read as settled."
)
NEW_P1 = (
    "Multiple imputation treats missing data through a division of labor that has "
    "served applied research for nearly four decades: an imputer fills in the missing "
    "values several times from a model for the complete data, an analyst fits the model "
    "of substantive interest to each completed data set, and simple rules combine the "
    "results [@rubinMultipleImputationNonresponse1987]. Reviews of the field's state of "
    "the art describe a mature methodology [@schaferMissingDataOur2002a; "
    "@endersMissingDataUpdate2025], in which the role of the missing-data mechanism is "
    "understood, point estimates recover their complete-data targets under stated "
    "conditions, and Wald-type tests for single and multiple parameters are well "
    "calibrated. On these accounts, the major inferential questions appear settled."
)

# ---------------------------------------------------------------- S1-P2 (register)
OLD_P2 = (
    "The exception is inference carried by the likelihood itself. For likelihood-ratio "
    "tests, a combining rule has existed since @mengPerformingLikelihoodRatio1992b. Its "
    "modern repairs give tests with accurate size [@chanMultipleImprovementsMultiple2022; "
    "@chanGeneralFeasibleTests2022]. For likelihood-based model selection, the picture "
    "is different. Here the literature's assessment of itself is that the question is "
    "open. Only one information criterion has been proposed specifically for averaging "
    "over multiply imputed data. Its authors call for further theoretical and practical "
    "study of the method and place that work beyond their own scope "
    "[@consentinoclaeskensOrderSelectionTests2010]. The first comprehensive study of "
    "model selection after multiple imputation describes the available literature as "
    "unexpectedly thin [@schomakerModelSelectionModel2014a]. That study also cautions "
    "that selecting models by averaged criteria has no support in the "
    "multiple-imputation literature. A dedicated study of variable selection with "
    "multiply imputed data reports that no guidelines yet exist "
    "[@woodHowShouldVariable2008a]. The applied guides are silent in the same "
    "direction. The standard book-length treatment does not treat information criteria "
    "for multiply imputed data at all [@vanbuurenFlexibleImputationMissing2018a]. "
    "Neither does the current state-of-the-art review [@endersMissingDataUpdate2025]."
)
NEW_P2 = (
    "The exception is inference carried by the likelihood itself. For likelihood-ratio "
    "tests, a combining rule has existed since @mengPerformingLikelihoodRatio1992b, and "
    "its modern repairs give tests with accurate size "
    "[@chanMultipleImprovementsMultiple2022; @chanGeneralFeasibleTests2022]. For "
    "likelihood-based model selection the picture is different, because here the "
    "literature assesses the question as open. Only one information criterion has been "
    "proposed specifically for averaging over multiply imputed data, and its authors "
    "call for further theoretical and practical study of the method while placing that "
    "work beyond their own scope [@consentinoclaeskensOrderSelectionTests2010]. The "
    "first comprehensive study of model selection after multiple imputation describes "
    "the available literature as unexpectedly thin [@schomakerModelSelectionModel2014a], "
    "and it cautions that selecting models by averaged criteria has no support in the "
    "multiple-imputation literature; a dedicated study of variable selection with "
    "multiply imputed data likewise reports that no guidelines yet exist "
    "[@woodHowShouldVariable2008a]. The applied guides are silent on the same question: "
    "the standard book-length treatment does not treat information criteria for "
    "multiply imputed data at all [@vanbuurenFlexibleImputationMissing2018a], and "
    "neither does the current state-of-the-art review [@endersMissingDataUpdate2025]."
)

# ---------------------------------------------------------------- S1-P3 (register)
OLD_P3 = (
    "What, then, should \"settled\" mean? We propose a standard and organize this paper "
    "around it. We call it the *complete-data replication principle*. A procedure for "
    "multiply imputed data replicates complete-data inference under one condition. On "
    "average over repeated samples, it must reach the same conclusion that would have "
    "been reached had no data been missing. The principle can be demanded at three "
    "levels. At the first level, estimates recover their complete-data targets. This is "
    "the classical level, and Rubin's rules settle it. At the second level, the "
    "decision criterion itself recovers its complete-data counterpart in expectation. "
    "This criterion is a deviance or an information criterion. At the third level, "
    "decision rates match. The same model is selected, and the same hypotheses are "
    "rejected, as often as they would have been with complete data. Stated this way, "
    "the settled results are settled because they pass at the first level. Posing the "
    "second and third levels reframes these open questions, which had been posed only "
    "at the first level. Benchmarking selection methods against the full data is not "
    "new in itself. Simulation comparisons of that kind appear in "
    "@woodHowShouldVariable2008a and @consentinoclaeskensOrderSelectionTests2010. The "
    "principle as an explicit yardstick is, to our knowledge, stated here for the first "
    "time. We add a characterization of when it can and cannot be met."
)
NEW_P3 = (
    "What, then, should \"settled\" mean? We propose a standard, the *complete-data "
    "replication principle*, and organize this paper around it: a procedure for "
    "multiply imputed data replicates complete-data inference when, on average over "
    "repeated samples, it reaches the same conclusion that would have been reached had "
    "no data been missing. The principle can be demanded at three levels. At the first "
    "level, estimates recover their complete-data targets; this is the classical level, "
    "and Rubin's rules settle it. At the second level, the decision criterion itself (a "
    "deviance or an information criterion) recovers its complete-data counterpart in "
    "expectation. At the third level, decision rates match: the same model is selected, "
    "and the same hypotheses are rejected, as often as they would have been with "
    "complete data. Stated this way, the settled results are settled because they pass "
    "at the first level, and posing the second and third levels reframes the open "
    "questions, which had been posed only at the first level. Benchmarking selection "
    "methods against the full data is not new in itself, because simulation comparisons "
    "of that kind appear in @woodHowShouldVariable2008a and "
    "@consentinoclaeskensOrderSelectionTests2010; the principle as an explicit "
    "yardstick is, to our knowledge, stated here for the first time, and we add a "
    "characterization of when it can and cannot be met."
)

# ------------------------------------------- S1-P4 (Demo 2 register + R11 rescope #1)
OLD_P4 = (
    "The obstacle is a bias in the averaged log-likelihood. This paper's central result "
    "describes that bias exactly. Suppose a likelihood model with an estimated variance "
    "or covariance is fit to congenially imputed data. We show that the averaged "
    "log-likelihood then overstates its complete-data counterpart by\n"
    "$$ \\tfrac{1}{2}\\operatorname{tr}(\\mathrm{RIV}) \\;+\\; (A){+}(C). $$\n"
    "The first term is one half the trace of the relative-increase-in-variance matrix. "
    "This matrix is a standard object in the MI literature. Its trace adds up the "
    "missing information about the model's parameters. The second term is smaller. It "
    "reflects imbalance between the observed and the missing units on the conditioning "
    "variables, and vanishes when the data are missing completely at random. The "
    "practical consequence is that, for such a model, every deviance and information "
    "criterion built on the averaged log-likelihood across imputations is, in "
    "expectation, too optimistic. Worse, the optimism is not uniform across models. "
    "Each candidate's criterion is inflated in proportion to that candidate's own "
    "missing information. A model-comparison table built on imputed data therefore "
    "tends, all else equal, to favor the candidates with the most missing information. "
    "In our pre-registered simulations, 100% of uncorrected MI-AIC's misclassifications "
    "fell on the candidate with the largest RIV. The fix is direct. Add each "
    "candidate's own trace back to its criterion. We show that the corrected criterion "
    "recovers its complete-data expectation at any signal strength. This is the "
    "principle's second level, met in full."
)
NEW_P4 = (
    # register: Demo 2 as ratified; precision: R11 rescope #1 ("describes the leading
    # term of that bias exactly") per the authorized addendum.
    "The obstacle is a bias in the averaged log-likelihood, and this paper's central "
    "result describes the leading term of that bias exactly. When a likelihood model "
    "with an estimated variance or covariance is fit to congenially imputed data, we "
    "show that the averaged log-likelihood overstates its complete-data counterpart by\n"
    "$$ \\tfrac{1}{2}\\operatorname{tr}(\\mathrm{RIV}) \\;+\\; (A){+}(C). $$\n"
    "The first term, one half the trace of the relative-increase-in-variance matrix (a "
    "standard object in the MI literature), adds up the missing information about the "
    "model's parameters; the second, smaller term reflects imbalance between the "
    "observed and the missing units on the conditioning variables, and vanishes when "
    "the data are missing completely at random. The practical consequence is that, for "
    "such a model, every deviance and information criterion built on the averaged "
    "log-likelihood across imputations is, in expectation, too optimistic. The more "
    "serious consequence is that the optimism is not uniform across models: because "
    "each candidate's criterion is inflated in proportion to that candidate's own "
    "missing information, a model-comparison table built on imputed data tends, all "
    "else equal, to favor the candidates with the most missing information, and in our "
    "pre-registered simulations 100% of uncorrected MI-AIC's misclassifications fell on "
    "the candidate with the largest RIV. The correction is direct. Adding each "
    "candidate's own trace back to its criterion recovers, as we show, the criterion's "
    "complete-data expectation at any signal strength, so the principle's second level "
    "is met in full."
)

# ------------------- S1-P5 (register + Bucket-2 + E3 thin; signature sentence KEPT)
OLD_P5 = (
    "The principle's third level asks for more. It asks for the same decisions at the "
    "same rates as the complete data. We show that the answer splits into two cases. In "
    "the first case, the competing models fit equally well, in the sense that the "
    "smaller model is true. Correction then restores complete-data behavior in this "
    "case. Calibrated tests reject at the complete-data rate "
    "[@chanGeneralFeasibleTests2022]. Selection that matches the criterion's full null "
    "distribution chooses models indistinguishably from complete-data AIC in our "
    "pre-registered design. In the second case, one model genuinely fits better. The "
    "missing data have then destroyed part of the evidence in its favor, and the "
    "corrected criteria and calibrated tests studied here cannot recover it. The "
    "relevant statistics shrink by factors we predict, and the remaining shortfall is "
    "information loss rather than a fixable calibration error. The practical reading is "
    "this. Corrected criteria are honest, not clairvoyant. Less information means less "
    "power, and the third level is met exactly to the extent the data permit."
)
NEW_P5 = (
    "The principle's third level asks for more: the same decisions at the same rates as "
    "the complete data. The answer, we show, splits into two cases. In the first, the "
    "competing models fit equally well, in the sense that the smaller model is true, "
    "and correction then restores complete-data behavior: calibrated tests reject at "
    "the complete-data rate [@chanGeneralFeasibleTests2022], and selection that matches "
    "the criterion's full null distribution chooses models indistinguishably from "
    "complete-data AIC in our pre-registered design. In the second, one model truly "
    "fits better. The missing data have then destroyed part of the evidence in its "
    "favor, and the corrected criteria and calibrated tests studied here cannot recover "
    "it; the relevant statistics shrink by factors we predict, and the remaining "
    "shortfall is information loss rather than a fixable calibration error. Corrected "
    "criteria are honest, not clairvoyant. Less information means less power, and the "
    "third level is met to the extent the data permit."
)

# ---------------------------------------- S1-P6 (register + R11 rescope #2)
OLD_P6 = (
    "These results stand upstream of the test-calibration literature and beside the "
    "model-selection one. The calibration line runs from "
    "@mengPerformingLikelihoodRatio1992b through @chanMultipleImprovementsMultiple2022 "
    "to @chanGeneralFeasibleTests2022, and it calibrates the reference distribution of "
    "an MI test statistic while taking the statistic's numerator as given. We derive "
    "the bias of that numerator, so the two are complementary. Calibration makes the "
    "reference distribution right, while the present correction makes the statistic "
    "referred to it centered. As a penalty, the correction is precedented, because it "
    "reproduces $\\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017. That "
    "criterion halved the missing-data surcharge of the earlier "
    "complete-data-discrepancy criteria [@cavanaughAkaikeInformationCriterion1998a]. "
    "All of those criteria were derived for deterministic EM estimation under a fixed "
    "missingness pattern. Two other routes stand nearby. The missing-covariate criteria "
    "of @claeskensconsentinoVariableSelectionIncomplete2008 target a different, "
    "Takeuchi-type discrepancy. The reweighting route of @hensModelSelectionIncomplete2006a "
    "reaches the complete-data target through inverse-probability weights, but it "
    "explicitly leaves an imputation-based criterion open. Five things here are new. "
    "First, the decomposition of the bias into an imputation-bias part and an "
    "estimation-mismatch part, with its estimated-scale scope condition. Second, the "
    "design-imbalance term $(A)+(C)$ under MAR, which lies beyond Shimodaira's "
    "fixed-pattern setting. His concluding section names the combination of missingness "
    "with other sampling mechanisms, such as covariate shift "
    "[@shimodairahidetoshiImprovingPredictiveInference2000], as future work. Third, the "
    "extension from the deterministic EM Q-function to proper multiple imputation. "
    "Fourth, the exact differential bias of the likelihood-ratio numerator at the null "
    "in the complete-data metric. Fifth, the replication principle itself, with the "
    "null/noncentral characterization of its third level. Congeniality is assumed "
    "throughout [@mengMultipleImputationInferencesUncongenial1994a]. The bias derived "
    "here is what remains after the imputer and the analyst agree."
)
NEW_P6 = (
    "These results stand upstream of the test-calibration literature and beside the "
    "model-selection one. The calibration line, which runs from "
    "@mengPerformingLikelihoodRatio1992b through @chanMultipleImprovementsMultiple2022 "
    "to @chanGeneralFeasibleTests2022, calibrates the reference distribution of an MI "
    "test statistic while taking the statistic's numerator as given; we derive the bias "
    "of that numerator, so the two are complementary, with calibration making the "
    "reference distribution right and the present correction making the statistic "
    "referred to it centered. As a penalty the correction is precedented, because it "
    "reproduces $\\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017, the "
    "criterion that halved the missing-data surcharge of the earlier "
    "complete-data-discrepancy criteria [@cavanaughAkaikeInformationCriterion1998a]; "
    "all of those criteria were derived for deterministic EM estimation under a fixed "
    "missingness pattern. Two other routes deserve mention: the missing-covariate "
    "criteria of @claeskensconsentinoVariableSelectionIncomplete2008 target a "
    "different, Takeuchi-type discrepancy, and the reweighting route of "
    "@hensModelSelectionIncomplete2006a reaches the complete-data target through "
    "inverse-probability weights but explicitly leaves an imputation-based criterion "
    "open. Five elements here are new. First is the decomposition of the bias into an "
    "imputation-bias part and an estimation-mismatch part, with its estimated-scale "
    "scope condition. Second is the design-imbalance term $(A)+(C)$ under MAR, which "
    "lies beyond Shimodaira's fixed-pattern setting (his concluding section names the "
    "combination of missingness with other sampling mechanisms, such as covariate shift "
    "[@shimodairahidetoshiImprovingPredictiveInference2000], as future work). Third is "
    "the extension from the deterministic EM Q-function to proper multiple imputation. "
    "Fourth is the closed-form leading-order differential bias of the likelihood-ratio "
    "numerator at the null in the complete-data metric. Fifth is the replication "
    "principle itself, with the null/noncentral characterization of its third level. "
    "Congeniality is assumed throughout [@mengMultipleImputationInferencesUncongenial1994a], "
    "and the bias derived here is what remains after the imputer and the analyst agree."
)

# ---------------------------------------------------------- S1B-P1 (partial, R10)
OLD_P1B_SUB = (
    "The division of labor is simple to state. The human author set the direction, "
    "fixed the standards, supplied field knowledge, and accepted or rejected each "
    "result; the AI system produced the derivations, the drafts, and the computations."
)
NEW_P1B_SUB = (
    "The division of labor is as follows: the human author set the direction, fixed "
    "the standards, supplied field knowledge, and accepted or rejected each result, "
    "while the AI system produced the derivations, the drafts, and the computations."
)

REPLACEMENTS = [
    ("S1-P1", OLD_P1, NEW_P1, "full"),
    ("S1-P2", OLD_P2, NEW_P2, "full"),
    ("S1-P3", OLD_P3, NEW_P3, "full"),
    ("S1-P4", OLD_P4, NEW_P4, "full"),
    ("S1-P5", OLD_P5, NEW_P5, "full"),
    ("S1-P6", OLD_P6, NEW_P6, "full"),
    ("S1B-P1", OLD_P1B_SUB, NEW_P1B_SUB, "sub"),
]

for pid, old, new, mode in REPLACEMENTS:
    p = para[pid]
    cur = p["draft_prose"]
    if mode == "full":
        if cur != old:
            raise SystemExit(f"{pid}: current draft_prose does not match the gated "
                             f"Current text -- aborting (no writes made).")
        p["draft_prose"] = new
    else:
        if old not in cur:
            raise SystemExit(f"{pid}: expected substring not found -- aborting.")
        if cur.count(old) != 1:
            raise SystemExit(f"{pid}: substring not unique -- aborting.")
        p["draft_prose"] = cur.replace(old, new)
    print(f"{pid}: replaced ({mode}).")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("batch 1 applied: 7 units rewritten; abstract/S1-P6b/S1-P7/S1B-P2 untouched.")
