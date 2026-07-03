# Text-validity 1a — adjudicated edit list (quorum determination: AMENDED)

Quorum: in-session Claude (advocate) vs GPT-5.5 (lead) + Gemini-via-DeepInfra.
True determination **AMENDED** (both peers; all 4 bars holds-as-amended; all 13 objections
withdrawn; R3 consensus). The tool printed "REFUTED" as a known aggregation artifact
(`collect_sustained_objections` OR's the probe-time `is_inaccuracy` flag of OBJ-01/09/10,
which the lead re-listed only as the edit list with `is_inaccuracy:false`). No result was
retracted; every fix below is a bounded wording / citation change, lead-ratified.

19 of the 20 ratified issues were adjudicated (all → amend). TV-06 was not pressed by the
quorum (see note). Two items carry a verification flag for the annotation pass.

---

## ABSTRACT
- **TV-01** (scope): "Adding one trace term per candidate removes the bias and restores complete-data-equivalent selection."
  → "Adding one trace term per candidate removes the deviance bias in expectation and substantially restores complete-data model selection."
- **TV-02** (scope): "...biased toward more complex models, because their larger relative increase in variance makes the fit look better than it is."
  → "...biased toward the candidates with more missing information, which in the nested families studied are the more complex models, because their larger relative increase in variance makes the fit look better than it is."

## S1-P2
- **TV-18** (citation/scope): "Only one information criterion has been proposed for multiply imputed data."
  → "Only one information criterion has been proposed specifically for averaging over multiply imputed data." (keeps the existing @consentinoclaeskensOrderSelectionTests2010 cite; the routes named later in S1-P6 target a different discrepancy or leave an imputation criterion open)

## S1-P3
- **TV-17** (speculation): "The open questions above are open because the second and third levels had not been posed."
  → "Posing the second and third levels reframes these open questions, which had been posed only at the first level."

## S1-P4
- **TV-03** (scope): "for such a model, every deviance and every information criterion computed from multiply imputed data is too optimistic."
  → "for such a model, every deviance and information criterion built on the averaged log-likelihood across imputations is, in expectation, too optimistic."
- **TV-11** (scope): "A model-comparison table built on imputed data therefore favors the candidates with the most missing information."
  → "A model-comparison table built on imputed data therefore tends, all else equal, to favor the candidates with the most missing information."
- **TV-14** (scope/consistency): "In our pre-registered study, every misclassification by uncorrected MI-AIC chose the candidate with the largest RIV."
  → "In our pre-registered congenial cells, every misclassification by uncorrected MI-AIC chose the candidate with the largest RIV." [VERIFY exact cell-scope vs the W3 results table]

## S1-P5
- **TV-05** (consistency vs G4): "...and we show that no transformation of the observed data can recover it."
  → "...and the corrected criteria and calibrated tests studied here cannot recover it."
- **TV-06** (NOT pressed by the quorum): "Correction then restores complete-data behavior entirely." — neither peer raised it. It is defensible in its null-case context (the next sentence: "Calibrated tests reject at the complete-data rate"; matched selection "indistinguishable from complete-data AIC"). OPTIONAL light scope for consistency with TV-01, e.g. "Correction then restores complete-data behavior in this equal-fit case." Marcus's call.

## S1-P6b
- **TV-04** (scope): "Adding one term per candidate, the trace of its relative-increase-in-variance matrix, removes the bias and substantially restores the ranking that complete data would have given."
  → "...removes the trace component of the bias and substantially restores the ranking that complete data would have given."

## S3-P6
- **TV-16** (speculation): "A derivation produced and checked within a single model family would likely have shipped one sign without noticing that there was a choice."
  → "A less diverse, single-family check could have missed that the sign turned on a conditioning choice." (recast as interpretation of the already-stated 8-of-9 result; do not re-state the 8/9)

## S5-P6
- **TV-19** (citation): "By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic referred to $\chi^2_1$."
  → add citation: "...a scaled-and-shifted statistic [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006] referred to $\chi^2_1$." (or a cross-reference to @sec-derivations)

## S5-P17
- **TV-15** (scope/consistency): "This is a registered directional prediction, and it held across all sixty cells." — KEEP (the directional prediction is pre-registered and held across all 60). Ensure the preceding "In every congenial cell, all of the uncorrected criterion's errors land on the saturated... candidate" reads clearly as the congenial-cell pattern, distinct from the 60-cell directional prediction. [VERIFY exact cell-scope vs the W3 results table]

## S5-P22
- **TV-13** (claim_support): "The bootstrap imputation sampler reproduces the analytic results on the most demanding cells, which bounds the cost of not running data augmentation."
  → "...which indicates the cost of not running data augmentation is small on these designs." (retain the conservative-sampler caveat)

## S6-P1
- **TV-08** (consistency/scope): "The bias exists only when the fit estimates a scale or covariance."
  → "The deviance optimism that inflates the criteria exists only when the fit estimates a scale or covariance." (distinguishes it from the known-scale proper-MI $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ term named in the same paragraph)

## S6-P6
- **TV-20** (citation): "De-shrinkage of estimated noncentrality and joint calibration of score vectors across candidates are developed separately."
  → "...are left to future work." (or cite a companion preprint if/when one exists) [VERIFY whether a citeable companion exists]

## S6-P7
- **TV-07** (consistency vs G4): "No transformation of the observed data manufactures the lost evidence back."
  → "No correction studied here manufactures the lost evidence back."
- **TV-09** (scope): "Corrected selection and calibrated tests behave as they would have with complete data."
  → "When the competing models fit alike, corrected selection and calibrated tests behave as they would have with complete data."
- **TV-12** (scope): "Then trust the result the way complete-data results are trusted."
  → "Then trust the result the way complete-data results are trusted, subject to the stated conditions and the close-comparison exception below."

## S6-P7b
- **TV-10** (consistency vs LRT result): "When the aim is to rank models or to compare nested models on imputed data, and no calibrated reference distribution already absorbs the bias, add the per-candidate trace correction before reading off the result."
  → split the rule: "For information-criterion ranking on imputed data, add each candidate's trace correction before reading off the result. For a nested comparison, prefer a calibrated likelihood-ratio test, whose reference distribution already carries the null mean, so no numerator correction is added; where no calibrated reference is available, the relevant bias is the missing information in the tested directions, $\operatorname{tr}(\mathrm{RIV}_\perp)$, not the difference of the candidates' separate trace corrections."

---

## Verification flags for the annotation pass
1. **TV-14 / TV-15** — confirm against the W3 results whether the *all-errors-on-the-saturated-candidate* (100%) pattern held across all 60 cells or only the congenial subset; set the wording to match. (The *directional* prediction held across all 60 — firm.)
2. **TV-20** — confirm no citeable companion preprint exists; if one does, cite it instead of "future work."
