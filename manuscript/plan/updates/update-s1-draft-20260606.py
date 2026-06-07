# S1 Introduction - from-scratch draft (D-12), 2026-06-06
#
# First Level-3 drafting cycle under the approved Level-2 blueprint (a21120a).
# Six paragraphs S1-P1..S1-P6 delivering S1-SP1..SP6 in order:
#   P1 maturity, ATTRIBUTED to the field's accounts (SP1)
#   P2 LRT/IC documented-open, quotes pinned to read sources (SP2, T-06)
#   P3 the complete-data replication principle, three levels, asserted-here with
#      the precedent scoping (SP3, D-10); @TODO:mi-ic-companion placeholder
#   P4 the theorem + both applications organized by principle level (SP4)
#   P5 positioning + what-is-new, incl. C-C 2010 prior MI-AIC in the lineage (SP5)
#   P6 meta layer + roadmap, title-page declaration referenced (SP6, D-11)
# Quarried from 180e2b5 sec-intro: the headline display, the decomposition
# sentences, the Chan-complementarity formulation, the Shimodaira/Cavanaugh
# lineage sentences, the congeniality scope sentence - all citation-verified
# passages; reframed around the principle.
# Also: sections_order updated to the ratified 6-section set (+ title-page
# declaration note); level4 evidence_map populated for S1.
# NOTE: estimated_paragraphs in the L2 blueprint was 4-5; the draft runs to 6
# (typing quotes in P2 and the principle in P3 each need their own paragraph).
# Flagged for Marcus in S1-P2.review.flags.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

# ---------------------------------------------------------------- sections_order
l3["sections_order"] = [
    {"id": "FRONT", "anchor": "title-page", "title": "Title page incl. authorship and provenance declaration (D-11)"},
    {"id": "S1", "anchor": "sec-intro", "title": "Introduction"},
    {"id": "S2", "anchor": "sec-background", "title": "Background and notation"},
    {"id": "S3", "anchor": "sec-methods", "title": "Methods: the derivation and verification workflow"},
    {"id": "S4", "anchor": "sec-derivations", "title": "Derivations"},
    {"id": "S5", "anchor": "sec-simulations", "title": "Simulation studies"},
    {"id": "S6", "anchor": "sec-discussion", "title": "Discussion"}
]
l3["metadata"]["status"] = "drafting_s1_complete"
l3["metadata"]["compile_note"] = (
    "compile_enabled stays false until all six sections are drafted and reviewed "
    "(D-12: from-scratch drafting, 180e2b5 as quarry; the decomposition route is "
    "retired). mi-spectral.qmd remains frozen at 180e2b5 until the first compile."
)

P1 = (
    "Multiple imputation treats missing data through a division of labor that has served "
    "applied research for nearly four decades: an imputer fills in the missing values "
    "several times from a model for the complete data, an analyst fits the model of "
    "substantive interest to each completed data set, and simple rules combine the results "
    "[@rubinMultipleImputationNonresponse1987]. The field's own accounts of its state of "
    "the art --- @schaferMissingDataOur2002a and the twentieth-anniversary update of "
    "@endersMissingDataUpdate2025 --- describe a mature methodology: the role of the "
    "missing-data mechanism is understood, point estimates recover their complete-data "
    "targets under stated conditions, and Wald-type tests for single and multiple "
    "parameters are well calibrated. On that testimony, the major inferential questions "
    "read as settled."
)

P2 = (
    "The exception is inference carried by the likelihood itself. A combining rule for "
    "likelihood-ratio tests has existed since @mengPerformingLikelihoodRatio1992b, and its "
    "modern repairs [@chanMultipleImprovementsMultiple2022; @chanGeneralFeasibleTests2022] "
    "give tests with accurate size; but on likelihood-based *model selection* after "
    "multiple imputation the literature's assessment of itself is that the question is "
    "open. The one information criterion proposed for multiply imputed data closes with "
    "the statement that the method \"seems worthwhile to be further investigated, both "
    "theoretically as well as in practical situations,\" the investigation lying beyond "
    "that paper's scope [@consentinoclaeskensOrderSelectionTests2010]. The first "
    "comprehensive study of model selection and model averaging after multiple imputation "
    "calls the literature \"surprisingly sparse\" and cautions that selecting by averaged "
    "criteria \"is not supported by MI literature\" [@schomakerModelSelectionModel2014a]. "
    "For variable selection, \"there are currently no guidelines\" "
    "[@woodHowShouldVariable2008a]. The applied guides are silent in the same direction: "
    "neither the standard book-length treatment [@vanbuurenFlexibleImputationMissing2018a] "
    "nor the current state-of-the-art review [@endersMissingDataUpdate2025] treats "
    "information criteria for multiply imputed data at all."
)

P3 = (
    "What, then, should \"settled\" mean? We propose a standard and organize this paper "
    "around it. Call it the *complete-data replication principle*: a procedure for "
    "multiply imputed data replicates complete-data inference if, on average over "
    "repeated samples, it reaches the same conclusion that would have been reached had no "
    "data been missing. The principle can be demanded at three levels: that *estimates* "
    "recover their complete-data targets --- the classical level, settled by Rubin's "
    "rules; that the decision *criterion* --- a deviance, an information criterion --- "
    "recover its complete-data counterpart in expectation; and that *decision rates* --- "
    "which model is selected, whether a hypothesis is rejected, how often --- match those "
    "of the complete-data analysis. Stated this way, the settled results are settled "
    "because they pass at the first level, and the open questions above are open "
    "precisely because the second and third levels had not been posed. Benchmarking "
    "selection methods against the full data is not new in itself --- simulation "
    "comparisons of that kind appear in @woodHowShouldVariable2008a and "
    "@consentinoclaeskensOrderSelectionTests2010 --- but the principle as an explicit "
    "yardstick, with a characterization of when it can and cannot be met, is to our "
    "knowledge stated here for the first time, jointly with a companion applied paper "
    "(@TODO:mi-ic-companion)."
)

P4 = (
    "This paper answers the principle's second level completely and locates the exact "
    "boundary of its third. The obstruction is a bias. For a regular likelihood model fit "
    "to congenially imputed data, with an estimated scale or covariance, the averaged "
    "log-likelihood across imputations --- the Q-function of the EM algorithm in its "
    "infinite-imputation limit --- overstates its complete-data target at the "
    "observed-data maximum likelihood estimate by\n"
    "$$ \\tfrac{1}{2}\\operatorname{tr}(\\mathrm{RIV}) \\;+\\; (A){+}(C), $$\n"
    "where $\\operatorname{tr}(\\mathrm{RIV})$ is the trace of the "
    "relative-increase-in-variance matrix --- the total odds of missing information about "
    "the model's parameters --- and $(A)+(C)$ is an $O(1)$ design-imbalance term that "
    "vanishes under MCAR. The half-trace decomposes into an *imputation-bias* term "
    "$+\\operatorname{tr}(\\mathrm{RIV})$ --- completions drawn from the fitted imputation "
    "model inflate the apparent fit of that same model --- and an *estimation-mismatch* "
    "term $-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ --- the MI fit targets the "
    "complete-data maximizer, which is not the observed-data one. Because the bias is "
    "model-specific --- each candidate's criterion is too small by its own "
    "$\\operatorname{tr}(\\mathrm{RIV}_k)$ --- uncorrected comparisons systematically "
    "favor the candidates with the most missing information; adding the trace back "
    "restores the criterion's complete-data expectation at any signal strength, and with "
    "it the principle's second level. The third level splits. At the null, corrected "
    "procedures replicate complete-data decisions completely: for testing, because a "
    "correctly calibrated reference distribution absorbs exactly the corresponding "
    "differential bias [@chanGeneralFeasibleTests2022]; for selection, because matching "
    "the criterion's null distribution makes model choice indistinguishable from "
    "complete-data AIC in our pre-registered design. Under signal, no transform built "
    "from the observed data restores the evidence the missing data destroyed: noncentral "
    "statistics shrink by exactly predictable factors, and the residual is information "
    "loss, not calibration error. Less information means less power, and the third level "
    "is met exactly to the extent the data permit."
)

P5 = (
    "These results sit upstream of the test-calibration literature and beside the "
    "model-selection one. The combining-rule line from @mengPerformingLikelihoodRatio1992b "
    "through @chanMultipleImprovementsMultiple2022 to @chanGeneralFeasibleTests2022 "
    "calibrates the *reference distribution* of an MI test statistic, taking the "
    "statistic's numerator as given; we derive the bias of that numerator. The two are "
    "complementary: calibration makes the reference distribution right, and the present "
    "correction makes the statistic referred to it centered. As a penalty, the correction "
    "is precedented: it reproduces $\\mathrm{AIC}_{x;y}$ of "
    "@shimodairaInformationCriterionModel2017, which halved the missing-data surcharge of "
    "the complete-data-discrepancy criteria PDIO and $\\mathrm{AIC}_{cd}$ "
    "[@cavanaughAkaikeInformationCriterion1998a] --- all derived for deterministic EM "
    "estimation under a fixed missingness pattern. The missing-covariate criteria of "
    "@claeskensconsentinoVariableSelectionIncomplete2008 target a different, "
    "Takeuchi-type discrepancy and sit outside this line, and the "
    "inverse-probability-reweighting route of @hensModelSelectionIncomplete2006a reaches "
    "the complete-data target while explicitly leaving an imputation-based criterion "
    "open. What is new here: the decomposition of the bias into imputation bias and "
    "estimation mismatch, with its estimated-scale scope condition; the MAR "
    "design-imbalance term $(A)+(C)$, which lies beyond Shimodaira's fixed-pattern "
    "setting --- his concluding section names the combination of missingness with other "
    "sampling mechanisms, such as covariate shift "
    "[@shimodairahidetoshiImprovingPredictiveInference2000], as future work; the "
    "extension from the deterministic EM Q-function to proper multiple imputation; the "
    "exact differential bias of the likelihood-ratio numerator in the complete-data "
    "metric; and the replication principle itself, with the null/noncentral "
    "characterization of its third level. Congeniality is assumed throughout "
    "[@mengMultipleImputationInferencesUncongenial1994a]: the bias derived here is what "
    "remains after the imputer and the analyst agree."
)

P6 = (
    "One feature of this paper bears on how it should be read, and the title page "
    "declares it: the derivations are AI-assisted, with an ORCID-verified human prompter "
    "of record. @sec-methods states the workflow under which every claim was produced "
    "--- citations backed by archived source documents, symbolic verification in two "
    "independent computer-algebra systems with Monte Carlo confirmation, preregistration "
    "with failed predictions reported, and adversarial re-derivation by an independent "
    "model --- together with what each safeguard can and cannot catch. The results are "
    "then offered to be judged through that protocol, as the results of an empirical "
    "paper are judged through its methods. @sec-background fixes notation and restates "
    "the standard results at the precision the argument needs. @sec-derivations develops "
    "the theorem and both applications; @sec-simulations reports the pre-registered "
    "studies, including the predictions that failed; @sec-discussion states what is "
    "firm, what is measured, and what is conjectured."
)

paragraphs = [
    {
        "id": "S1-P1",
        "section": "S1",
        "goal": "position_lineage",
        "proposition": "The field's own state-of-the-art accounts treat MI's core inferential machinery as settled; the maturity claim is reported as theirs.",
        "depends_on": [],
        "dep_types": [],
        "review": {
            "serves_L2": "S1-SP1",
            "serves_L1": "M1 paragraph (1) of the funnel; primary thesis via setup",
            "sets_up": "S1-P2 (the exception), S1-P3 (the criterion question)",
            "topic_sentence": "Multiple imputation treats missing data through a division of labor that has served applied research for nearly four decades: an imputer fills in the missing values several times from a model for the complete data, an analyst fits the model of substantive interest to each completed data set, and simple rules combine the results [@rubinMultipleImputationNonresponse1987].",
            "closing_sentence": "On that testimony, the major inferential questions read as settled.",
            "status": "drafted",
            "flags": None
        },
        "draft_prose": P1,
        "audit": {
            "status": "complete",
            "citations": {
                "rubinMultipleImputationNonresponse1987": "verified (read in-session 2026-06-06; division-of-labor framing per the book's stated program)",
                "schaferMissingDataOur2002a": "verified (read in-session 2026-06-06; abstract: ML and MI 'currently represent the state of the art')",
                "endersMissingDataUpdate2025": "verified (read in-session 2026-06-06; explicit 20th-anniversary update of SG2002, catalogs the settled landscape)"
            },
            "numbers": {},
            "notes": "No quantitative claims. 'Nearly four decades' anchored to Rubin 1987."
        }
    },
    {
        "id": "S1-P2",
        "section": "S1",
        "goal": "position_lineage",
        "proposition": "LRT/IC after MI are documented-open, in the literature's own words (four direct quotes + two documented absences).",
        "depends_on": ["S1-P1"],
        "dep_types": ["builds_on"],
        "review": {
            "serves_L2": "S1-SP2",
            "serves_L1": "M1 paragraph (2); T-06 documented-open typing",
            "sets_up": "S1-P3 (the principle that explains WHY these are open)",
            "topic_sentence": "The exception is inference carried by the likelihood itself.",
            "closing_sentence": "The applied guides are silent in the same direction: neither the standard book-length treatment [@vanbuurenFlexibleImputationMissing2018a] nor the current state-of-the-art review [@endersMissingDataUpdate2025] treats information criteria for multiply imputed data at all.",
            "status": "drafted",
            "flags": "Draft runs S1 to 6 paragraphs vs the blueprint's estimated 4-5; P2 (quotes) and P3 (principle) each need their own paragraph. For Marcus to confirm or compress."
        },
        "draft_prose": P2,
        "audit": {
            "status": "complete",
            "citations": {
                "mengPerformingLikelihoodRatio1992b": "verified (read in-session 2026-06-06; D_L construction, SS3)",
                "chanMultipleImprovementsMultiple2022": "verified (read in-session 2026-06-06; D4/stacked improvements)",
                "chanGeneralFeasibleTests2022": "verified (read in-session 2026-06-06; general feasible calibration)",
                "consentinoclaeskensOrderSelectionTests2010": "verified (read in-session 2026-06-06; SS5 closing quote verbatim at :404)",
                "schomakerModelSelectionModel2014a": "verified (read in-session 2026-06-06; 'surprisingly sparse' SS1 :54, 'not supported by MI literature' SS2.1 :123)",
                "woodHowShouldVariable2008a": "verified (read in-session 2026-06-06; 'currently no guidelines' abstract :24)",
                "vanbuurenFlexibleImputationMissing2018a": "verified (read in-session 2026-06-06; ch.5 has no IC-after-MI treatment - documented by absence)",
                "endersMissingDataUpdate2025": "verified (read in-session 2026-06-06; MI-inference section is testing-only)"
            },
            "numbers": {},
            "notes": "All four quotes checked verbatim against the literature files this session; absences documented in todo/003 typing pass."
        }
    },
    {
        "id": "S1-P3",
        "section": "S1",
        "goal": "define_concept",
        "proposition": "The complete-data replication principle, posed at three levels, supplies the missing criterion of settledness; asserted-here with the benchmark-practice precedent scoped honestly.",
        "depends_on": ["S1-P1", "S1-P2"],
        "dep_types": ["builds_on", "builds_on"],
        "review": {
            "serves_L2": "S1-SP3",
            "serves_L1": "M1 paragraph (2)-(3) hinge; D-10",
            "sets_up": "S1-P4 (the answers, level by level); S4 subsection openers; S6 verdict",
            "topic_sentence": "What, then, should \"settled\" mean?",
            "closing_sentence": "...but the principle as an explicit yardstick, with a characterization of when it can and cannot be met, is to our knowledge stated here for the first time, jointly with a companion applied paper (@TODO:mi-ic-companion).",
            "status": "drafted",
            "flags": "@TODO:mi-ic-companion placeholder - the MI-IC companion needs a citable form (preprint DOI or in-prep entry) before compile."
        },
        "draft_prose": P3,
        "audit": {
            "status": "complete",
            "citations": {
                "woodHowShouldVariable2008a": "verified (full-data benchmark practice, SS4 :279)",
                "consentinoclaeskensOrderSelectionTests2010": "verified (Table 7 AIC_orig row :383-391)"
            },
            "numbers": {},
            "notes": "Asserted-here typing per the todo/003 pass (2026-06-06): the principle confirmed unposed in Meng-Rubin 1992, both Chan papers, C-C 2008/2010, Schomaker-Heumann 2014; novelty scoped to the PRINCIPLE, not the benchmark practice. The @TODO:mi-ic-companion placeholder is mirrored as a 'proposed' entry in level4 (E-S1-P3-4) and in todo/003."
        }
    },
    {
        "id": "S1-P4",
        "section": "S1",
        "goal": "state_result",
        "proposition": "The headline bias and its decomposition restore level-2 replication everywhere; level 3 splits along the null/noncentral axis identically for testing and selection.",
        "depends_on": ["S1-P3"],
        "dep_types": ["builds_on"],
        "review": {
            "serves_L2": "S1-SP4",
            "serves_L1": "M1 paragraph (3); primary+secondary+tertiary theses",
            "sets_up": "S4 (all three subsections), S5 (the preregistered grading), S6-SP4 (the verdict)",
            "topic_sentence": "This paper answers the principle's second level completely and locates the exact boundary of its third.",
            "closing_sentence": "Less information means less power, and the third level is met exactly to the extent the data permit.",
            "status": "drafted",
            "flags": None
        },
        "draft_prose": P4,
        "audit": {
            "status": "complete",
            "citations": {
                "chanGeneralFeasibleTests2022": "verified (calibrated reference absorbs the null-mean inflation; eq. 1.10 spectrum)"
            },
            "numbers": {
                "headline display +1/2 tr(RIV) + (A)+(C)": "deriv:sec-thm",
                "decomposition +tr(RIV) / -1/2 tr(RIV)": "deriv:sec-thm",
                "(A)+(C) O(1), vanishes under MCAR": "deriv:sec-lrt-ac",
                "model-specific bias tr(RIV_k); uncorrected favors high-RIV": "deriv:sec-ic",
                "null-side selection indistinguishable from complete-data AIC": "verif:verification/cache/ic-ladder-summary.csv",
                "noncentral shrinkage by predictable factors; information loss not calibration error": "deriv:sec-ic"
            },
            "notes": "Display and decomposition sentences quarried from 180e2b5 P2 (citation-verified there); numbers kept qualitative in the intro per D-03 (exact values land inline in S4)."
        }
    },
    {
        "id": "S1-P5",
        "section": "S1",
        "goal": "position_lineage",
        "proposition": "Upstream of calibration (complementary), beside the model-selection lineage (penalty precedented); the five claimed novelties named; congeniality scoped.",
        "depends_on": ["S1-P4"],
        "dep_types": ["builds_on"],
        "review": {
            "serves_L2": "S1-SP5",
            "serves_L1": "M1 paragraph (3) positioning; honest-novelty posture (T-06)",
            "sets_up": "S2-SP8 (lineage restatement), S6-SP3 (future directions)",
            "topic_sentence": "These results sit upstream of the test-calibration literature and beside the model-selection one.",
            "closing_sentence": "Congeniality is assumed throughout [@mengMultipleImputationInferencesUncongenial1994a]: the bias derived here is what remains after the imputer and the analyst agree.",
            "status": "drafted",
            "flags": None
        },
        "draft_prose": P5,
        "audit": {
            "status": "complete",
            "citations": {
                "mengPerformingLikelihoodRatio1992b": "verified (combining rule; calibration universe)",
                "chanMultipleImprovementsMultiple2022": "verified (D4)",
                "chanGeneralFeasibleTests2022": "verified (general calibration)",
                "shimodairaInformationCriterionModel2017": "verified (read in-session 2026-06-06; AIC_{x;y} = -2l_y + d + tr(I_x I_y^{-1}), 'only half the value' of PDIO's surcharge, :77-89; SS8 future work)",
                "cavanaughAkaikeInformationCriterion1998a": "verified (read in-session 2026-06-06; AICcd abstract + complete-data discrepancy motivation)",
                "claeskensconsentinoVariableSelectionIncomplete2008": "verified (read in-session 2026-06-06; TIC-style criterion, missing covariates, KL on Q)",
                "hensModelSelectionIncomplete2006a": "verified (read in-session 2026-06-06; weighted-AIC Horvitz-Thompson route, abstract)",
                "shimodairahidetoshiImprovingPredictiveInference2000": "verified (read in-session 2026-06-06; covariate-shift weighting, abstract)",
                "mengMultipleImputationInferencesUncongenial1994a": "verified (read in-session 2026-06-06; congeniality definition, abstract)"
            },
            "numbers": {
                "AIC_{x;y} halves the PDIO/AICcd surcharge": "lit:shimodairaInformationCriterionModel2017"
            },
            "notes": "Lineage sentences quarried from 180e2b5 P5-P6 and reframed; the five-item novelty list adds the replication principle (D-10) to 180e2b5's three-item list."
        }
    },
    {
        "id": "S1-P6",
        "section": "S1",
        "goal": "transition",
        "proposition": "The meta layer, last: title-page declaration referenced, Methods as the reading protocol, roadmap.",
        "depends_on": ["S1-P5"],
        "dep_types": ["builds_on"],
        "review": {
            "serves_L2": "S1-SP6",
            "serves_L1": "M1 paragraph (4); methodological thesis; D-11",
            "sets_up": "S3 (Methods), the section sequence",
            "topic_sentence": "One feature of this paper bears on how it should be read, and the title page declares it: the derivations are AI-assisted, with an ORCID-verified human prompter of record.",
            "closing_sentence": "@sec-discussion states what is firm, what is measured, and what is conjectured.",
            "status": "drafted",
            "flags": None
        },
        "draft_prose": P6,
        "audit": {
            "status": "complete",
            "citations": {},
            "numbers": {},
            "notes": "Rhetorical/transition paragraph; cross-references only. T-03 vocabulary check passed (no banned terms)."
        }
    }
]

l3["paragraphs"] = paragraphs

l3["metrics_gate"]["notes"] = (
    "Partial evaluation at S1 drafting (2026-06-06): 6/6 paragraphs carry a proposition "
    "or declared rhetorical goal; every number in S1 has a deriv:/verif: pointer in its "
    "audit object; every citekey backed by literature/<citekey>.md read in-session "
    "2026-06-06 (@TODO:mi-ic-companion is the one declared placeholder); review objects "
    "complete; dependency chain P1->P6 acyclic. Full gate evaluation deferred until all "
    "six sections are drafted (D-12)."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# ---------------------------------------------------------------- Level 4
with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)

l4["metadata"]["status"] = "populating_with_level3_drafting"
l4["evidence_map"] = [
    {"id": "E-S1-P1-1", "proposition_id": "S1-P1", "pointer": "lit:schaferMissingDataOur2002a", "evidence_status": "verified", "passage_or_value": "Abstract: ML and Bayesian MI 'currently represent the state of the art.'", "note": "Field's own maturity testimony, 2002 anchor."},
    {"id": "E-S1-P1-2", "proposition_id": "S1-P1", "pointer": "lit:endersMissingDataUpdate2025", "evidence_status": "verified", "passage_or_value": "20th-anniversary update framing; catalogs settled landscape (mechanisms, FIML, Bayes, MI, MNAR, multilevel).", "note": "Maturity testimony, current anchor."},
    {"id": "E-S1-P1-3", "proposition_id": "S1-P1", "pointer": "lit:rubinMultipleImputationNonresponse1987", "evidence_status": "verified", "passage_or_value": "The MI program: impute m times, analyze, combine.", "note": "Division-of-labor sentence."},
    {"id": "E-S1-P2-1", "proposition_id": "S1-P2", "pointer": "lit:consentinoclaeskensOrderSelectionTests2010", "evidence_status": "verified", "passage_or_value": "SS5 :404: 'the connected AIC method seems worthwhile to be further investigated, both theoretically as well as in practical situations. This, however, extends the scope of the current paper.'", "note": "Prior MI-AIC's own open-theory statement; quote used in P2."},
    {"id": "E-S1-P2-2", "proposition_id": "S1-P2", "pointer": "lit:schomakerModelSelectionModel2014a", "evidence_status": "verified", "passage_or_value": "SS1 :54 'surprisingly sparse'; SS2.1 :123 averaged criteria 'not supported by MI literature' (citing White et al. 2011 p.389).", "note": "Both quotes used in P2."},
    {"id": "E-S1-P2-3", "proposition_id": "S1-P2", "pointer": "lit:woodHowShouldVariable2008a", "evidence_status": "verified", "passage_or_value": "Abstract :24: 'there are currently no guidelines for variable selection in multiply imputed data sets.'", "note": "Quote used in P2."},
    {"id": "E-S1-P2-4", "proposition_id": "S1-P2", "pointer": "lit:vanbuurenFlexibleImputationMissing2018a", "evidence_status": "verified", "passage_or_value": "Ch.5: D1/D2/D3 testing + Wald-based stepwise + LASSO variants; no IC-after-MI treatment.", "note": "Documented-by-absence claim."},
    {"id": "E-S1-P2-5", "proposition_id": "S1-P2", "pointer": "lit:endersMissingDataUpdate2025", "evidence_status": "verified", "passage_or_value": "MI-inference section covers Wald/LRT pooling + SEM fit only.", "note": "Documented-by-absence claim, current anchor."},
    {"id": "E-S1-P3-1", "proposition_id": "S1-P3", "pointer": "verif:todo/003-references-to-acquire.md", "evidence_status": "verified", "passage_or_value": "M1 typing pass section (2026-06-06): centering question + replication principle confirmed unposed across the theory line.", "note": "Backs the asserted-here typing of the principle."},
    {"id": "E-S1-P3-2", "proposition_id": "S1-P3", "pointer": "lit:woodHowShouldVariable2008a", "evidence_status": "verified", "passage_or_value": "SS4 :279: 'A good method should have type 1 error close to that observed using the full data.'", "note": "The precedented benchmark practice the novelty claim is scoped against."},
    {"id": "E-S1-P3-3", "proposition_id": "S1-P3", "pointer": "lit:consentinoclaeskensOrderSelectionTests2010", "evidence_status": "verified", "passage_or_value": "Table 7: AIC_orig 0.731/0.722 vs MI methods 0.540-0.594.", "note": "Displays the replication gap without framing it - second precedent for the benchmark practice."},
    {"id": "E-S1-P3-4", "proposition_id": "S1-P3", "pointer": "verif:todo/003-references-to-acquire.md", "evidence_status": "proposed", "passage_or_value": "MI-IC companion paper (Waldman, in preparation): complete-data replication framing at MI-IC/manuscript/mi-ic-article.qmd:136.", "note": "PLACEHOLDER for the @TODO:mi-ic-companion citation in S1-P3 prose - the companion needs a citable form (preprint/DOI or in-prep bib entry) before compile. Logged in todo/003."},
    {"id": "E-S1-P4-1", "proposition_id": "S1-P4", "pointer": "deriv:sec-thm", "evidence_status": "verified", "passage_or_value": "+1/2 tr(RIV) + (A)+(C) and the +tr/-1/2tr decomposition.", "note": "Headline display and decomposition sentences."},
    {"id": "E-S1-P4-2", "proposition_id": "S1-P4", "pointer": "deriv:sec-lrt-ac", "evidence_status": "verified", "passage_or_value": "(A)+(C): O(1), MCAR vanishing.", "note": "Design-imbalance clause."},
    {"id": "E-S1-P4-3", "proposition_id": "S1-P4", "pointer": "deriv:sec-ic", "evidence_status": "verified", "passage_or_value": "Model-specific bias; corrected criterion; noncentral shrinkage factors.", "note": "Selection clauses."},
    {"id": "E-S1-P4-4", "proposition_id": "S1-P4", "pointer": "verif:verification/cache/ic-ladder-summary.csv", "evidence_status": "verified", "passage_or_value": "Null-side rungs 2-3: 0.904/0.903 vs oracle 0.899 (exact values quoted in S4, qualitative here).", "note": "'Indistinguishable from complete-data AIC' clause."},
    {"id": "E-S1-P4-5", "proposition_id": "S1-P4", "pointer": "lit:chanGeneralFeasibleTests2022", "evidence_status": "verified", "passage_or_value": "Calibrated reference absorbs the null mean (eq. 1.10 spectrum).", "note": "Testing side of the null-replication claim."},
    {"id": "E-S1-P5-1", "proposition_id": "S1-P5", "pointer": "lit:shimodairaInformationCriterionModel2017", "evidence_status": "verified", "passage_or_value": ":77-89: AIC_{x;y} penalty d + tr(I_x I_y^{-1}); 'The additional penalty is only half the value of that in PDIO'; SS8 names mechanism combinations as future work.", "note": "Penalty precedent + future-work hook."},
    {"id": "E-S1-P5-2", "proposition_id": "S1-P5", "pointer": "lit:cavanaughAkaikeInformationCriterion1998a", "evidence_status": "verified", "passage_or_value": "AICcd = -2Q + 2tr(I_x I_y^{-1}); complete-data discrepancy motivation.", "note": "The doubled-penalty lineage."},
    {"id": "E-S1-P5-3", "proposition_id": "S1-P5", "pointer": "lit:claeskensconsentinoVariableSelectionIncomplete2008", "evidence_status": "verified", "passage_or_value": "TIC-style criterion on the EM Q-function for missing covariates ('best approximating' values; no correct-specification assumption).", "note": "'Different discrepancy, outside this line' sentence."},
    {"id": "E-S1-P5-4", "proposition_id": "S1-P5", "pointer": "lit:hensModelSelectionIncomplete2006a", "evidence_status": "verified", "passage_or_value": "Weighted (Horvitz-Thompson) AIC for incomplete/design-based samples.", "note": "Reweighting route; leaves imputation-based criterion open."},
    {"id": "E-S1-P5-5", "proposition_id": "S1-P5", "pointer": "lit:shimodairahidetoshiImprovingPredictiveInference2000", "evidence_status": "verified", "passage_or_value": "Covariate-shift weighting of the log-likelihood.", "note": "Named in the future-work clause."},
    {"id": "E-S1-P5-6", "proposition_id": "S1-P5", "pointer": "lit:mengMultipleImputationInferencesUncongenial1994a", "evidence_status": "verified", "passage_or_value": "Congeniality definition and the uncongenial controversy.", "note": "Scope sentence."}
]
l4["metrics_gate"]["notes"] = (
    "Partial evaluation at S1 drafting (2026-06-06): every S1 paragraph proposition has "
    ">=1 entry; all pointers resolve; the one 'proposed' entry (E-S1-P3-4) is the "
    "declared @TODO:mi-ic-companion placeholder. Full gate when all sections drafted."
)

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S1 drafted: 6 paragraphs into level3, 22 evidence entries into level4")
