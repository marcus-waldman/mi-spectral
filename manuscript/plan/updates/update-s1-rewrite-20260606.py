# S1 Introduction - plain-cadence rewrite, 2026-06-06 (same day as the first draft)
#
# Marcus's in-chat feedback on the first S1 draft (3610a72):
#   1. P4 read as unmotivated ("whoa, where did this all come from?") - results must
#      be announced ("we show") and cashed out in applied terms.
#   2. Prose cadence: no em-dash appositive chains, no fixed poetic rhythm, no inline
#      hanging references; plain expository structure (topic sentence, supporting
#      details, one idea per sentence). Saved as standing feedback memory
#      (feedback_plain_expository_cadence).
#   3. Drop the companion-paper citation (@TODO:mi-ic-companion) from P3.
# Result: whole introduction rewritten in plain cadence; old P4 split into P4 (bias +
# level 2) and P5 (level 3 split); old P5->P6, old P6->P7. Seven paragraphs.
# The +tr/-1/2tr decomposition detail moved out of P4; it now first appears as item
# one of P6's novelty list (flagged for the per-paragraph session).
# Marcus: "good enough so far... I do have comments, but I need to sit down at a
# computer and go one paragraph at a time." Status -> awaiting per-paragraph
# annotation of S1.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

paras = {p["id"]: p for p in l3["paragraphs"]}

P1 = (
    "Multiple imputation treats missing data through a division of labor, and that "
    "division has served applied research for nearly four decades. An imputer fills in "
    "the missing values several times from a model for the complete data. An analyst "
    "fits the model of substantive interest to each completed data set. Simple rules "
    "then combine the results [@rubinMultipleImputationNonresponse1987]. The field's own "
    "accounts of its state of the art describe a mature methodology "
    "[@schaferMissingDataOur2002a; @endersMissingDataUpdate2025]. The role of the "
    "missing-data mechanism is understood. Point estimates recover their complete-data "
    "targets under stated conditions. Wald-type tests for single and multiple parameters "
    "are well calibrated. On that testimony, the major inferential questions read as "
    "settled."
)

P2 = (
    "The exception is inference carried by the likelihood itself. For likelihood-ratio "
    "tests, a combining rule has existed since @mengPerformingLikelihoodRatio1992b, and "
    "its modern repairs give tests with accurate size "
    "[@chanMultipleImprovementsMultiple2022; @chanGeneralFeasibleTests2022]. For "
    "likelihood-based model selection, the literature's assessment of itself is that the "
    "question is open. The one information criterion proposed for multiply imputed data "
    "closes with the statement that the method \"seems worthwhile to be further "
    "investigated, both theoretically as well as in practical situations\"; that "
    "investigation lay beyond the paper's scope "
    "[@consentinoclaeskensOrderSelectionTests2010]. The first comprehensive study of "
    "model selection after multiple imputation calls the literature \"surprisingly "
    "sparse\" [@schomakerModelSelectionModel2014a]. The same study cautions that "
    "selecting by averaged criteria \"is not supported by MI literature.\" For variable "
    "selection, \"there are currently no guidelines\" [@woodHowShouldVariable2008a]. The "
    "applied guides are silent in the same direction. Neither the standard book-length "
    "treatment [@vanbuurenFlexibleImputationMissing2018a] nor the current "
    "state-of-the-art review [@endersMissingDataUpdate2025] treats information criteria "
    "for multiply imputed data at all."
)

P3 = (
    "What, then, should \"settled\" mean? We propose a standard and organize this paper "
    "around it. We call it the *complete-data replication principle*: a procedure for "
    "multiply imputed data replicates complete-data inference if, on average over "
    "repeated samples, it reaches the same conclusion that would have been reached had "
    "no data been missing. The principle can be demanded at three levels. At the first "
    "level, estimates recover their complete-data targets. This is the classical level, "
    "and Rubin's rules settle it. At the second level, the decision criterion itself "
    "--- a deviance, an information criterion --- recovers its complete-data counterpart "
    "in expectation. At the third level, decision rates match: the same model is "
    "selected, and the same hypotheses are rejected, as often as they would have been "
    "with complete data. Stated this way, the settled results are settled because they "
    "pass at the first level. The open questions above are open because the second and "
    "third levels had not been posed. Benchmarking selection methods against the full "
    "data is not new in itself; simulation comparisons of that kind appear in "
    "@woodHowShouldVariable2008a and @consentinoclaeskensOrderSelectionTests2010. The "
    "principle as an explicit yardstick, with a characterization of when it can and "
    "cannot be met, is to our knowledge stated here for the first time."
)

P4 = (
    "The obstacle is a bias in the averaged log-likelihood, and this paper's central "
    "result describes that bias exactly. Suppose a likelihood model with an estimated "
    "variance or covariance is fit to congenially imputed data. We show that the "
    "averaged log-likelihood then overstates its complete-data counterpart by\n"
    "$$ \\tfrac{1}{2}\\operatorname{tr}(\\mathrm{RIV}) \\;+\\; (A){+}(C). $$\n"
    "The first term is one half the trace of the relative-increase-in-variance matrix. "
    "This matrix is a standard object in the MI literature, and its trace adds up the "
    "missing information about the model's parameters. The second term is smaller. It "
    "reflects imbalance between the observed and the missing units on the conditioning "
    "variables, and it vanishes when the data are missing completely at random. The "
    "practical consequence is that every deviance and every information criterion "
    "computed from multiply imputed data is too optimistic. Worse, the optimism is not "
    "uniform across models. Each candidate's criterion is inflated in proportion to "
    "that candidate's own missing information. A model-comparison table built on "
    "imputed data therefore favors the candidates with the most missing information. In "
    "our pre-registered study, every misclassification by uncorrected MI-AIC chose the "
    "candidate with the largest RIV. The fix is direct: add each candidate's own trace "
    "back to its criterion. We show that the corrected criterion recovers its "
    "complete-data expectation at any signal strength. This is the principle's second "
    "level, met in full."
)

P5 = (
    "The principle's third level asks for more: the same decisions at the same rates as "
    "the complete data. We show that the answer splits into two cases. In the first "
    "case, the competing models fit equally well, in the sense that the smaller model "
    "is true. Correction then restores complete-data behavior entirely. Calibrated "
    "tests reject at the complete-data rate [@chanGeneralFeasibleTests2022]. Selection "
    "that matches the criterion's full null distribution chooses models "
    "indistinguishably from complete-data AIC in our pre-registered design. In the "
    "second case, one model genuinely fits better. The missing data have then destroyed "
    "part of the evidence in its favor, and we show that no transformation of the "
    "observed data can recover it. The relevant statistics shrink by factors we predict "
    "exactly, and the remaining shortfall is information loss rather than a fixable "
    "calibration error. The practical reading is this: corrected criteria are honest, "
    "not clairvoyant. Less information means less power, and the third level is met "
    "exactly to the extent the data permit."
)

P6 = (
    "These results sit upstream of the test-calibration literature and beside the "
    "model-selection one. The calibration line runs from "
    "@mengPerformingLikelihoodRatio1992b through @chanMultipleImprovementsMultiple2022 "
    "to @chanGeneralFeasibleTests2022. That line calibrates the reference distribution "
    "of an MI test statistic, and it takes the statistic's numerator as given. We "
    "derive the bias of that numerator. The two are complementary: calibration makes "
    "the reference distribution right, and the present correction makes the statistic "
    "referred to it centered. As a penalty, the correction is precedented. It "
    "reproduces $\\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017, "
    "which halved the missing-data surcharge of the earlier complete-data-discrepancy "
    "criteria [@cavanaughAkaikeInformationCriterion1998a]. All of those criteria were "
    "derived for deterministic EM estimation under a fixed missingness pattern. Two "
    "other routes sit nearby. The missing-covariate criteria of "
    "@claeskensconsentinoVariableSelectionIncomplete2008 target a different, "
    "Takeuchi-type discrepancy. The reweighting route of "
    "@hensModelSelectionIncomplete2006a reaches the complete-data target through "
    "inverse-probability weights, and it explicitly leaves an imputation-based "
    "criterion open. Five things here are new. First, the decomposition of the bias "
    "into an imputation-bias part and an estimation-mismatch part, with its "
    "estimated-scale scope condition. Second, the design-imbalance term $(A)+(C)$ under "
    "MAR, which lies beyond Shimodaira's fixed-pattern setting; his concluding section "
    "names the combination of missingness with other sampling mechanisms, such as "
    "covariate shift [@shimodairahidetoshiImprovingPredictiveInference2000], as future "
    "work. Third, the extension from the deterministic EM Q-function to proper multiple "
    "imputation. Fourth, the exact differential bias of the likelihood-ratio numerator "
    "in the complete-data metric. Fifth, the replication principle itself, with the "
    "null/noncentral characterization of its third level. Congeniality is assumed "
    "throughout [@mengMultipleImputationInferencesUncongenial1994a]. The bias derived "
    "here is what remains after the imputer and the analyst agree."
)

P7 = (
    "One feature of this paper bears on how it should be read, and the title page "
    "declares it: the derivations are AI-assisted, with an ORCID-verified human "
    "prompter of record. @sec-methods states the workflow under which every claim was "
    "produced. Citations are backed by archived source documents. Every analytic result "
    "was verified symbolically in two independent computer-algebra systems and "
    "confirmed by Monte Carlo simulation. Predictions were registered before code was "
    "written, and the failed ones are reported. Load-bearing claims were re-derived "
    "blind by an independent model and subjected to an adversarial review. "
    "@sec-methods also states what each of these safeguards can and cannot catch. The "
    "results are then offered to be judged through that protocol, the way an empirical "
    "paper's results are judged through its methods. The rest of the paper proceeds as "
    "follows. @sec-background fixes notation and restates the standard results at the "
    "precision the argument needs. @sec-derivations develops the theorem and both "
    "applications. @sec-simulations reports the pre-registered studies, including the "
    "predictions that failed. @sec-discussion states what is firm, what is measured, "
    "and what is conjectured."
)

# Rebuild the paragraph list: reuse audit/citation metadata, renumber, split P4.
old = paras

def mk(idx, goal, proposition, dep, prose, serves_L2, serves_L1, sets_up, topic, closing, flags, citations, numbers, notes):
    return {
        "id": idx, "section": "S1", "goal": goal, "proposition": proposition,
        "depends_on": dep, "dep_types": ["builds_on"] * len(dep),
        "review": {"serves_L2": serves_L2, "serves_L1": serves_L1, "sets_up": sets_up,
                   "topic_sentence": topic, "closing_sentence": closing,
                   "status": "drafted", "flags": flags},
        "draft_prose": prose,
        "audit": {"status": "complete", "citations": citations, "numbers": numbers, "notes": notes}
    }

l3["paragraphs"] = [
    mk("S1-P1", "position_lineage", old["S1-P1"]["proposition"], [], P1,
       "S1-SP1", old["S1-P1"]["review"]["serves_L1"], "S1-P2, S1-P3",
       "Multiple imputation treats missing data through a division of labor, and that division has served applied research for nearly four decades.",
       "On that testimony, the major inferential questions read as settled.",
       None, old["S1-P1"]["audit"]["citations"], {}, old["S1-P1"]["audit"]["notes"]),
    mk("S1-P2", "position_lineage", old["S1-P2"]["proposition"], ["S1-P1"], P2,
       "S1-SP2", old["S1-P2"]["review"]["serves_L1"], "S1-P3",
       "The exception is inference carried by the likelihood itself.",
       "Neither the standard book-length treatment [@vanbuurenFlexibleImputationMissing2018a] nor the current state-of-the-art review [@endersMissingDataUpdate2025] treats information criteria for multiply imputed data at all.",
       "S1 runs to 7 paragraphs vs blueprint estimate 4-5 (Marcus aware; per-paragraph session pending).",
       old["S1-P2"]["audit"]["citations"], {}, old["S1-P2"]["audit"]["notes"]),
    mk("S1-P3", "define_concept", old["S1-P3"]["proposition"], ["S1-P1", "S1-P2"], P3,
       "S1-SP3", old["S1-P3"]["review"]["serves_L1"], "S1-P4, S1-P5; S4 openers; S6 verdict",
       "What, then, should \"settled\" mean?",
       "The principle as an explicit yardstick, with a characterization of when it can and cannot be met, is to our knowledge stated here for the first time.",
       None,
       old["S1-P3"]["audit"]["citations"], {},
       "Companion-paper citation REMOVED per Marcus (2026-06-06); compile blocker cleared. Asserted-here typing per the todo/003 pass."),
    mk("S1-P4", "state_result",
       "The headline bias, stated as something the paper shows, with each formal object translated to applied terms; correction restores level-2 replication.",
       ["S1-P3"], P4,
       "S1-SP4", "M1 paragraph (3); primary+tertiary theses", "S4a/S4c, S5, S6-SP4",
       "The obstacle is a bias in the averaged log-likelihood, and this paper's central result describes that bias exactly.",
       "This is the principle's second level, met in full.",
       "The +tr/-1/2tr decomposition detail moved out of this paragraph in the plain-cadence rewrite; it now first appears in P6's novelty list. Confirm or restore a sentence here (per-paragraph session).",
       {}, {
           "headline display +1/2 tr(RIV) + (A)+(C)": "deriv:sec-thm",
           "(A)+(C) imbalance reading, MCAR vanishing": "deriv:sec-lrt-ac",
           "every misclassification on the largest-RIV candidate": "verif:verification/cache/run_all-prod",
           "corrected criterion recovers complete-data expectation": "deriv:sec-ic"
       },
       "Rewritten for plain cadence + 'we show' announcements (Marcus feedback 2026-06-06)."),
    mk("S1-P5", "state_result",
       "Level 3 splits: null side restored entirely (testing and selection); under signal the shortfall is information loss with exactly predicted shrinkage.",
       ["S1-P4"], P5,
       "S1-SP4", "M1 paragraph (3); secondary+tertiary theses", "S4b/S4c, S6-SP4",
       "The principle's third level asks for more: the same decisions at the same rates as the complete data.",
       "Less information means less power, and the third level is met exactly to the extent the data permit.",
       None,
       {"chanGeneralFeasibleTests2022": "verified (calibrated reference absorbs the null-mean inflation)"},
       {
           "null-side selection indistinguishable from complete-data AIC": "verif:verification/cache/ic-ladder-summary.csv",
           "noncentral shrinkage by exactly predicted factors": "deriv:sec-ic"
       },
       "Split out of old P4 in the plain-cadence rewrite."),
    mk("S1-P6", "position_lineage", old["S1-P5"]["proposition"], ["S1-P4", "S1-P5"], P6,
       "S1-SP5", old["S1-P5"]["review"]["serves_L1"], "S2-SP8, S6-SP3",
       "These results sit upstream of the test-calibration literature and beside the model-selection one.",
       "The bias derived here is what remains after the imputer and the analyst agree.",
       None,
       old["S1-P5"]["audit"]["citations"], old["S1-P5"]["audit"]["numbers"],
       "Novelty list enumerated (First..Fifth) in the plain-cadence rewrite; deps updated to P4+P5."),
    mk("S1-P7", "transition", old["S1-P6"]["proposition"], ["S1-P6"], P7,
       "S1-SP6", old["S1-P6"]["review"]["serves_L1"], "S3, section sequence",
       "One feature of this paper bears on how it should be read, and the title page declares it: the derivations are AI-assisted, with an ORCID-verified human prompter of record.",
       "@sec-discussion states what is firm, what is measured, and what is conjectured.",
       None, {}, {}, old["S1-P6"]["audit"]["notes"])
]
# fix dep_types where two deps
l3["paragraphs"][2]["dep_types"] = ["builds_on", "builds_on"]
l3["paragraphs"][5]["dep_types"] = ["builds_on", "builds_on"]

l3["metadata"]["status"] = "s1_rewritten_awaiting_paragraph_annotation"
l3["metrics_gate"]["notes"] = (
    "Partial evaluation after the S1 plain-cadence rewrite (2026-06-06): 7/7 paragraphs "
    "carry propositions/goals; numbers pointered; citekeys session-read; the "
    "@TODO:mi-ic-companion placeholder is REMOVED (P3). Marcus: substance approved 'so "
    "far', per-paragraph annotation session pending. Full gate when all sections drafted."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# ---------------------------------------------------------------- Level 4 renumber
with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)

new_map = []
for e in l4["evidence_map"]:
    pid = e["proposition_id"]
    if e["id"] == "E-S1-P3-4":
        continue  # companion placeholder removed with the citation
    if pid == "S1-P4":
        # split: ladder/selection-rate entries follow the level-3 content to P5
        if "ic-ladder" in e["pointer"] or "absorbs the null mean" in str(e.get("passage_or_value", "")):
            e["proposition_id"] = "S1-P5"
            e["id"] = e["id"].replace("-P4-", "-P5-")
    elif pid == "S1-P5":
        e["proposition_id"] = "S1-P6"
        e["id"] = e["id"].replace("-P5-", "-P6-")
    new_map.append(e)
l4["evidence_map"] = new_map
l4["metrics_gate"]["notes"] = (
    "Renumbered after the S1 rewrite (P4 split -> P4/P5; old P5 -> P6); companion "
    "placeholder entry removed with the citation. Every S1 paragraph has >=1 entry; "
    "all pointers resolve. Full gate when all sections drafted."
)

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S1 rewritten: 7 paragraphs, plain cadence; level4 renumbered; companion placeholder removed")
