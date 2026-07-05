# Sweep batch 1 proposal: abstract + S1 + S1B (D-26 register, for Marcus's gate)

**Date: 2026-07-05. GATE DOCUMENT — nothing applied to level3 until Marcus approves this
batch.** On approval it becomes one atomic script under `manuscript/plan/updates/`, then
check_plan → rebuild → render → scouts, per D-26. Register changes and R11 (precision)
changes are labeled separately. Units marked NO CHANGE are proposed to pass untouched
(final texture falls to the closing whole-document read).

## Batch summary

| unit | action |
|---|---|
| abstract | NO CHANGE (Phase B: largely conformant; longest-sentence prose in the paper) |
| S1-P1 | ratified Demo 1, verbatim |
| S1-P2 | register rewrite (subordination, C7 attribution repair) |
| S1-P3 | register rewrite (subordination; the organizing question kept) |
| S1-P4 | ratified Demo 2 + the authorized R11 rescope #1 |
| S1-P5 | register rewrite + Bucket-2 "genuinely"→"truly" + E3 thin + R10 formula retired; signature sentence KEPT |
| S1-P6 | register rewrite + the authorized R11 rescope #2 |
| S1-P6b | NO CHANGE (contributions list conforms, R7) |
| S1-P7 | NO CHANGE (roadmap conforms, R7) |
| S1B-P1 | one-sentence fix (retired "is simple to state" formula) |
| S1B-P2 | NO CHANGE (First/.../Fifth structure is register-native) |

---

## S1-P1 — ratified Demo 1 (restated for the script)

> Multiple imputation treats missing data through a division of labor that has served
> applied research for nearly four decades: an imputer fills in the missing values several
> times from a model for the complete data, an analyst fits the model of substantive
> interest to each completed data set, and simple rules combine the results
> [@rubinMultipleImputationNonresponse1987]. Reviews of the field's state of the art
> describe a mature methodology [@schaferMissingDataOur2002a; @endersMissingDataUpdate2025],
> in which the role of the missing-data mechanism is understood, point estimates recover
> their complete-data targets under stated conditions, and Wald-type tests for single and
> multiple parameters are well calibrated. On these accounts, the major inferential
> questions appear settled.

Invariance: as certified in `demonstrations-2026-07-05.md`, Demo 1.

---

## S1-P2 — register rewrite

### Current

> The exception is inference carried by the likelihood itself. For likelihood-ratio tests,
> a combining rule has existed since @mengPerformingLikelihoodRatio1992b. Its modern
> repairs give tests with accurate size [@chanMultipleImprovementsMultiple2022;
> @chanGeneralFeasibleTests2022]. For likelihood-based model selection, the picture is
> different. Here the literature's assessment of itself is that the question is open. Only
> one information criterion has been proposed specifically for averaging over multiply
> imputed data. Its authors call for further theoretical and practical study of the method
> and place that work beyond their own scope [@consentinoclaeskensOrderSelectionTests2010].
> The first comprehensive study of model selection after multiple imputation describes the
> available literature as unexpectedly thin [@schomakerModelSelectionModel2014a]. That
> study also cautions that selecting models by averaged criteria has no support in the
> multiple-imputation literature. A dedicated study of variable selection with multiply
> imputed data reports that no guidelines yet exist [@woodHowShouldVariable2008a]. The
> applied guides are silent in the same direction. The standard book-length treatment does
> not treat information criteria for multiply imputed data at all
> [@vanbuurenFlexibleImputationMissing2018a]. Neither does the current state-of-the-art
> review [@endersMissingDataUpdate2025].

### Proposed

> The exception is inference carried by the likelihood itself. For likelihood-ratio tests,
> a combining rule has existed since @mengPerformingLikelihoodRatio1992b, and its modern
> repairs give tests with accurate size [@chanMultipleImprovementsMultiple2022;
> @chanGeneralFeasibleTests2022]. For likelihood-based model selection the picture is
> different, because here the literature assesses the question as open. Only one
> information criterion has been proposed specifically for averaging over multiply imputed
> data, and its authors call for further theoretical and practical study of the method
> while placing that work beyond their own scope
> [@consentinoclaeskensOrderSelectionTests2010]. The first comprehensive study of model
> selection after multiple imputation describes the available literature as unexpectedly
> thin [@schomakerModelSelectionModel2014a], and it cautions that selecting models by
> averaged criteria has no support in the multiple-imputation literature; a dedicated
> study of variable selection with multiply imputed data likewise reports that no
> guidelines yet exist [@woodHowShouldVariable2008a]. The applied guides are silent on the
> same question: the standard book-length treatment does not treat information criteria
> for multiply imputed data at all [@vanbuurenFlexibleImputationMissing2018a], and neither
> does the current state-of-the-art review [@endersMissingDataUpdate2025].

Register: twelve sentences → six (R1); the C7 scaffold "the literature's assessment of
itself is that" becomes "the literature assesses the question as open" (attribution
kept); "silent in the same direction" (figurative) → "silent on the same question".
Invariance: all seven citekeys at the same attachment points; every documented-open claim
still attributed to its stating source (T-06); no number, no hedge changed.

---

## S1-P3 — register rewrite

### Current

> What, then, should "settled" mean? We propose a standard and organize this paper around
> it. We call it the *complete-data replication principle*. A procedure for multiply
> imputed data replicates complete-data inference under one condition. On average over
> repeated samples, it must reach the same conclusion that would have been reached had no
> data been missing. The principle can be demanded at three levels. At the first level,
> estimates recover their complete-data targets. This is the classical level, and Rubin's
> rules settle it. At the second level, the decision criterion itself recovers its
> complete-data counterpart in expectation. This criterion is a deviance or an information
> criterion. At the third level, decision rates match. The same model is selected, and the
> same hypotheses are rejected, as often as they would have been with complete data.
> Stated this way, the settled results are settled because they pass at the first level.
> Posing the second and third levels reframes these open questions, which had been posed
> only at the first level. Benchmarking selection methods against the full data is not new
> in itself. Simulation comparisons of that kind appear in @woodHowShouldVariable2008a and
> @consentinoclaeskensOrderSelectionTests2010. The principle as an explicit yardstick is,
> to our knowledge, stated here for the first time. We add a characterization of when it
> can and cannot be met.

### Proposed

> What, then, should "settled" mean? We propose a standard, the *complete-data replication
> principle*, and organize this paper around it: a procedure for multiply imputed data
> replicates complete-data inference when, on average over repeated samples, it reaches
> the same conclusion that would have been reached had no data been missing. The principle
> can be demanded at three levels. At the first level, estimates recover their
> complete-data targets; this is the classical level, and Rubin's rules settle it. At the
> second level, the decision criterion itself (a deviance or an information criterion)
> recovers its complete-data counterpart in expectation. At the third level, decision
> rates match: the same model is selected, and the same hypotheses are rejected, as often
> as they would have been with complete data. Stated this way, the settled results are
> settled because they pass at the first level, and posing the second and third levels
> reframes the open questions, which had been posed only at the first level. Benchmarking
> selection methods against the full data is not new in itself, because simulation
> comparisons of that kind appear in @woodHowShouldVariable2008a and
> @consentinoclaeskensOrderSelectionTests2010; the principle as an explicit yardstick is,
> to our knowledge, stated here for the first time, and we add a characterization of when
> it can and cannot be met.

Register: seventeen sentences → eight (R1); the criterion gloss becomes a parenthesis
(R2); the organizing question and the three-level structure are untouched (R7).
Invariance: the definition's condition ("on average over repeated samples ... same
conclusion") verbatim; "to our knowledge" hedge verbatim; both citekeys kept; the
novelty claim's scope ("as an explicit yardstick ... for the first time") unchanged.

---

## S1-P4 — ratified Demo 2 + authorized R11 rescope #1

As Demo 2's proposed text, with one authorized precision change (addendum item #1):
the opening becomes

> The obstacle is a bias in the averaged log-likelihood, and this paper's central result
> describes the leading term of that bias exactly. When a likelihood model with an
> estimated variance or covariance is fit to congenially imputed data, we show that the
> averaged log-likelihood overstates its complete-data counterpart by [display unchanged] ...

and the remainder follows Demo 2 verbatim. Labels in the update script: register (Demo 2)
vs precision (R11 #1) separately.

---

## S1-P5 — register rewrite + authorized vocabulary/precision items

### Current

> The principle's third level asks for more. It asks for the same decisions at the same
> rates as the complete data. We show that the answer splits into two cases. In the first
> case, the competing models fit equally well, in the sense that the smaller model is
> true. Correction then restores complete-data behavior in this case. Calibrated tests
> reject at the complete-data rate [@chanGeneralFeasibleTests2022]. Selection that matches
> the criterion's full null distribution chooses models indistinguishably from
> complete-data AIC in our pre-registered design. In the second case, one model genuinely
> fits better. The missing data have then destroyed part of the evidence in its favor, and
> the corrected criteria and calibrated tests studied here cannot recover it. The relevant
> statistics shrink by factors we predict, and the remaining shortfall is information loss
> rather than a fixable calibration error. The practical reading is this. Corrected
> criteria are honest, not clairvoyant. Less information means less power, and the third
> level is met exactly to the extent the data permit.

### Proposed

> The principle's third level asks for more: the same decisions at the same rates as the
> complete data. The answer, we show, splits into two cases. In the first, the competing
> models fit equally well, in the sense that the smaller model is true, and correction
> then restores complete-data behavior: calibrated tests reject at the complete-data rate
> [@chanGeneralFeasibleTests2022], and selection that matches the criterion's full null
> distribution chooses models indistinguishably from complete-data AIC in our
> pre-registered design. In the second, one model truly fits better. The missing data have
> then destroyed part of the evidence in its favor, and the corrected criteria and
> calibrated tests studied here cannot recover it; the relevant statistics shrink by
> factors we predict, and the remaining shortfall is information loss rather than a
> fixable calibration error. Corrected criteria are honest, not clairvoyant. Less
> information means less power, and the third level is met to the extent the data permit.

Register: "The practical reading is this." retired (R10); sentences subordinated (R1).
Vocabulary: "genuinely" → "truly" (Bucket 2, authorized). Precision: "met exactly to the
extent" → "met to the extent" (E3 thin, authorized). The signature sentence "Corrected
criteria are honest, not clairvoyant." is KEPT verbatim per D-26.
Invariance: the two-case split, the smaller-model-true sense clause, "factors we
predict", "information loss rather than a fixable calibration error", the citekey — all
verbatim; no claim strength changed ("truly" = "genuinely").

---

## S1-P6 — register rewrite + authorized R11 rescope #2

### Current

> These results stand upstream of the test-calibration literature and beside the
> model-selection one. The calibration line runs from @mengPerformingLikelihoodRatio1992b
> through @chanMultipleImprovementsMultiple2022 to @chanGeneralFeasibleTests2022, and it
> calibrates the reference distribution of an MI test statistic while taking the
> statistic's numerator as given. We derive the bias of that numerator, so the two are
> complementary. Calibration makes the reference distribution right, while the present
> correction makes the statistic referred to it centered. As a penalty, the correction is
> precedented, because it reproduces $\mathrm{AIC}_{x;y}$ of
> @shimodairaInformationCriterionModel2017. That criterion halved the missing-data
> surcharge of the earlier complete-data-discrepancy criteria
> [@cavanaughAkaikeInformationCriterion1998a]. All of those criteria were derived for
> deterministic EM estimation under a fixed missingness pattern. Two other routes stand
> nearby. The missing-covariate criteria of @claeskensconsentinoVariableSelectionIncomplete2008
> target a different, Takeuchi-type discrepancy. The reweighting route of
> @hensModelSelectionIncomplete2006a reaches the complete-data target through
> inverse-probability weights, but it explicitly leaves an imputation-based criterion
> open. Five things here are new. First, the decomposition of the bias into an
> imputation-bias part and an estimation-mismatch part, with its estimated-scale scope
> condition. Second, the design-imbalance term $(A)+(C)$ under MAR, which lies beyond
> Shimodaira's fixed-pattern setting. His concluding section names the combination of
> missingness with other sampling mechanisms, such as covariate shift
> [@shimodairahidetoshiImprovingPredictiveInference2000], as future work. Third, the
> extension from the deterministic EM Q-function to proper multiple imputation. Fourth,
> the exact differential bias of the likelihood-ratio numerator at the null in the
> complete-data metric. Fifth, the replication principle itself, with the null/noncentral
> characterization of its third level. Congeniality is assumed throughout
> [@mengMultipleImputationInferencesUncongenial1994a]. The bias derived here is what
> remains after the imputer and the analyst agree.

### Proposed

> These results stand upstream of the test-calibration literature and beside the
> model-selection one. The calibration line, which runs from
> @mengPerformingLikelihoodRatio1992b through @chanMultipleImprovementsMultiple2022 to
> @chanGeneralFeasibleTests2022, calibrates the reference distribution of an MI test
> statistic while taking the statistic's numerator as given; we derive the bias of that
> numerator, so the two are complementary, with calibration making the reference
> distribution right and the present correction making the statistic referred to it
> centered. As a penalty the correction is precedented, because it reproduces
> $\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017, the criterion that
> halved the missing-data surcharge of the earlier complete-data-discrepancy criteria
> [@cavanaughAkaikeInformationCriterion1998a]; all of those criteria were derived for
> deterministic EM estimation under a fixed missingness pattern. Two other routes deserve
> mention: the missing-covariate criteria of
> @claeskensconsentinoVariableSelectionIncomplete2008 target a different, Takeuchi-type
> discrepancy, and the reweighting route of @hensModelSelectionIncomplete2006a reaches the
> complete-data target through inverse-probability weights but explicitly leaves an
> imputation-based criterion open. Five elements here are new. First is the decomposition
> of the bias into an imputation-bias part and an estimation-mismatch part, with its
> estimated-scale scope condition. Second is the design-imbalance term $(A)+(C)$ under
> MAR, which lies beyond Shimodaira's fixed-pattern setting (his concluding section names
> the combination of missingness with other sampling mechanisms, such as covariate shift
> [@shimodairahidetoshiImprovingPredictiveInference2000], as future work). Third is the
> extension from the deterministic EM Q-function to proper multiple imputation. Fourth is
> the closed-form leading-order differential bias of the likelihood-ratio numerator at the
> null in the complete-data metric. Fifth is the replication principle itself, with the
> null/noncentral characterization of its third level. Congeniality is assumed throughout
> [@mengMultipleImputationInferencesUncongenial1994a], and the bias derived here is what
> remains after the imputer and the analyst agree.

Register: subordination + a which-clause and a parenthesis (R1/R2); "Two other routes
stand nearby" (spatial) → "deserve mention"; "Five things here are new" → "Five elements
here are new" with "First is ..." parallel members. Precision (R11 rescope #2,
authorized): "the exact differential bias" → "the closed-form leading-order differential
bias". Invariance: all eight citekeys at the same attachment points; the five novelty
items unchanged in content and order; "As a penalty the correction is precedented"
(precedent acknowledgment) kept; semicolon count 3 (at the v3 cap).

---

## S1B-P1 — one-sentence fix

Replace only

> The division of labor is simple to state. The human author set the direction, fixed the
> standards, supplied field knowledge, and accepted or rejected each result; the AI system
> produced the derivations, the drafts, and the computations.

with

> The division of labor is as follows: the human author set the direction, fixed the
> standards, supplied field knowledge, and accepted or rejected each result, while the AI
> system produced the derivations, the drafts, and the computations.

("is simple to state" is the retired R10 formula family; roles verbatim.)

---

## NO CHANGE justifications

- **Abstract:** already the paper's most subordinated prose; Phase B graded it largely
  conformant; every sentence carries riders. Touching it buys nothing.
- **S1-P6b:** the numbered contributions list matches
  `rubinMultipleImputationNonresponse1987:536` ("In this text we will: 1. ..."); internal
  texture deferred to the closing read.
- **S1-P7:** the roadmap matches `rubinInferenceMissingData1976b:57-71`; register-native
  as separate sentences.
- **S1B-P2:** the measured Five-patterns paragraph mirrors
  `rubinMultipleImputationNonresponse1987:557`'s First/.../Fourth structure; conformant.

## Gate

Approve / amend per unit. On approval: one atomic update script
(`manuscript/plan/updates/update-batch-s1-register-YYYYMMDD.py`, register and R11 changes
labeled separately) → `py scripts/check_plan.py` → `py scripts/build_manuscript_apa.py` →
`quarto render manuscript/mi-spectral-apa.qmd` → scouts. Expected gate movement: the
S1-P5 "genuinely" vocabulary warning clears; S4/S5/S6 warnings remain until their batches.
