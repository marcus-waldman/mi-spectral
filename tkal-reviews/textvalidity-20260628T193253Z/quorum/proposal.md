POSITION UNDER DEFENSE — text-validity of the manuscript's claims (claim-support, 1a)

The manuscript is a statistics methods paper: a deviance-bias correction for the averaged log-likelihood (Q-function) under congenial proper multiple imputation, with two applications — information-criterion model selection and likelihood-ratio model comparison. Its theorem and simulation RESULTS are correct and were already validated by a separate adversarial cross-family review; they are off-limits here.

THE POSITION: the in-scope prose is faithful to what the paper establishes. Each of the 20 sentences flagged below is either (a) earned as written from the paper's own derivation, figure, or pre-registration, or (b) where the wording could be read as stronger or broader than the established result, the underlying claim is still correct and the remedy is a bounded WORDING amendment that re-scopes the sentence to what is proved/measured — not a retraction of any result. The defense will, per item, point to the paper's own basis (section / figure / pre-registration) or to the cited source; it concedes a wording fix where a careful reader could read more than the result shows, and it never concedes a result.

What the paper actually establishes (the basis the defense draws on):
- HEADLINE BIAS. For a model that estimates a scale/covariance, fit to congenially imputed data, the averaged log-likelihood overstates its complete-data counterpart by 1/2 tr(RIV) + (A)+(C), where (A)+(C) is a design-imbalance term that vanishes under MCAR (S1-P4). The +1/2 tr(RIV) holds for the FITTED-imputation Q-function; a known-scale, location-only fit has no bias under deterministic FIML and -1/2 tr(RIV) under proper MI (S6-P1).
- IC CORRECTION (second level of the replication principle). Adding each candidate's own tr(RIV) makes the corrected criterion recover its complete-data EXPECTATION at any signal strength (S1-P4, proved). Selection RATE recovery is "substantial but visibly short of the complete-data benchmark": at N=500 the benchmark selects the true model at 0.90, uncorrected 0.67, corrected 0.82 (S5-P17); a weak-signal floor remains (G4, S6-P3).
- THIRD LEVEL (decision rates) SPLITS. When the smaller model is true, calibrated tests reject at the complete-data rate and matched selection is indistinguishable from complete-data AIC (S1-P5). When one model genuinely fits better, statistics shrink by predicted factors and the residual shortfall is information loss "as measured through these corrections"; G4 states explicitly that no argument here shows no estimator from the same observed data could do better (S6-P3).
- LRT NUMERATOR. The bias of a nested comparison at the null is the missing information in the tested directions alone, in the complete-data metric (tr(RIV_perp)); the difference of the two models' separate corrections ALWAYS OVERSTATES it (S1-P6b item 3). A calibrated reference distribution already carries the null mean, so a numerator correction on top would double-count (S6-P7b).
- PRE-REGISTERED SELECTION RESULT. In every congenial cell, all uncorrected-criterion errors land on the saturated, largest-missing-information candidate (registered directional prediction; W3-C = 1.000). Because candidates are nested and ordered by missing information, this confirms the bias DIRECTION but does not discriminate the decomposition (S5-P17).
- WORKFLOW. Eight of nine blind cross-family re-derivations produced the opposite sign because a true-model conditioning was silently substituted; the fork is now stated where the theorem is set up (S3-P6).
- LINEAGE. The correction reproduces Shimodaira's AIC_{x;y} as a penalty; the Claeskens-Consentino (2008) missing-covariate criteria target a different (Takeuchi-type) discrepancy and the Hens et al. (2006) reweighting route explicitly leaves an imputation-based criterion open (S1-P6). The "one information criterion proposed for MI" refers to Consentino-Claeskens (2010), whose authors place further study beyond their scope (S1-P2).

THE 20 FLAGGED CLAIMS, EACH WITH ITS CONTEXT (the challenge per item is in the attack surface):

TV-01 [ABSTRACT] "Adding one trace term per candidate removes the bias and restores complete-data-equivalent selection."
  Context: the body states the correction removes the bias IN EXPECTATION (S1-P4) and "substantially restores the ranking" (S1-P6b); S5-P17 reports recovery 0.67->0.82 vs benchmark 0.90, "substantial but visibly short."

TV-02 [ABSTRACT] "Model selection on multiply imputed data is biased toward more complex models, because their larger relative increase in variance makes the fit look better than it is."
  Context: the proved driver is per-candidate tr(RIV) (missing information); in the nested families studied the higher-RIV candidate is the more complex one (S5-P17), but complexity=>higher RIV is not proved in general.

TV-03 [S1-P4] "for such a model, every deviance and every information criterion computed from multiply imputed data is too optimistic."
  Context: "for such a model" = a model estimating a scale/covariance under congenial MI; the bias is +1/2 tr(RIV)+(A)+(C). Known-scale location-only fits are exempt/opposite-signed (S6-P1).

TV-04 [S1-P6b] "Adding one term per candidate, the trace of its relative-increase-in-variance matrix, removes the bias and substantially restores the ranking that complete data would have given."
  Context: the trace removes the +1/2 tr(RIV) part; the design-imbalance (A)+(C) is separate and small (zero under MCAR); ranking recovery is the measured 0.82 vs 0.90 with a residual gap (S5-P17, G4).

TV-05 [S1-P5] "The missing data have then destroyed part of the evidence in its favor, and we show that no transformation of the observed data can recover it."
  Context: paired against G4 (S6-P3): "No argument here shows that no estimator built from the same observed data could do better." The measured object is the shortfall "as measured through these corrections."

TV-06 [S1-P5] "Correction then restores complete-data behavior entirely."
  Context: this is the FIRST case (smaller model true / null): "Calibrated tests reject at the complete-data rate" and matched selection is "indistinguishable from complete-data AIC in our pre-registered design" (S1-P5). The weak-signal floor belongs to the SECOND case.

TV-07 [S6-P7] "No transformation of the observed data manufactures the lost evidence back."
  Context: the conclusion's restatement of the third-level "no" case; pair against G4 (S6-P3) as for TV-05.

TV-08 [S6-P1] "The bias exists only when the fit estimates a scale or covariance."
  Context: next sentences: "In that case the conditional missing-data entropy depends on the estimated parameters. A known-scale, location-only fit has no such bias under deterministic FIML and only -1/2 tr(RIV) under proper MI." "The bias" = the deviance optimism (the +1/2 tr(RIV) entropy bias); the -1/2 tr(RIV) under known-scale proper MI is the estimation-mismatch term.

TV-09 [S6-P7] "Corrected selection and calibrated tests behave as they would have with complete data."
  Context: this is the SECOND part of the three-part answer — "decisions when the competing models fit alike" (the null/equal-fit case), where calibrated tests reject at the complete-data rate (S1-P5, S6-P7). The third part (one model fits better) is explicitly answered "no" in the very next sentences.

TV-10 [S6-P7b] "...add the per-candidate trace correction before reading off the result." (for ranking OR nested comparison)
  Context: the sentence's own next clause: "Information-criterion selection is the main such case. The exception is a calibrated likelihood-ratio test, where the reference distribution already carries the null mean, so a numerator correction applied on top would double-count and should be left out." The LRT bias object is tr(RIV_perp), not the difference of per-candidate corrections (S1-P6b item 3).

TV-11 [S1-P4] "A model-comparison table built on imputed data therefore favors the candidates with the most missing information."
  Context: follows from "Each candidate's criterion is inflated in proportion to that candidate's own missing information." The pre-registered result: in every congenial cell all uncorrected errors land on the largest-RIV candidate (S5-P17).

TV-12 [S6-P7] "Then trust the result the way complete-data results are trusted."
  Context: the applied summary, preceded by "Correct the criterion, or match its null distribution," and followed by "The one exception is where the comparison was close enough that the missing data could have decided it. There, the honest answer is that the data no longer say." Scope limits (estimated-scale, congeniality, weak-signal floor, normal-family) are stated across S6-P1..P3.

TV-13 [S5-P22] "...which bounds the cost of not running data augmentation."
  Context: the engine-sensitivity study: sample tr(RIV) matches the observed-data value within 2-3% and selection agrees within 0.011 on the recovery gap, on the studied designs; "This robustness is empirical and scoped to the designs studied," and a fully Bayesian sampler "remains the conservative choice when the fraction of missing information is large."

TV-14 [S1-P4] "In our pre-registered study, every misclassification by uncorrected MI-AIC chose the candidate with the largest RIV."
  Context: the results section states it precisely: "In every congenial cell, all of the uncorrected criterion's errors land on the saturated, largest-missing-information candidate" (S5-P17). W3-C = 1.000 is the congenial-cell result.

TV-15 [S5-P17] "This is a registered directional prediction, and it held across all sixty cells."
  Context: the preceding sentence restricts the pattern to congenial cells ("In every congenial cell ..."); the comprehensive sweep is 60 cells; uncongenial overshoot is disclosed in the discussion (G7 congeniality limit).

TV-16 [S3-P6] "A derivation produced and checked within a single model family would likely have shipped one sign without noticing that there was a choice."
  Context: the worked example: 8 of 9 BLIND cross-family re-derivations produced the opposite sign via a silent true-model conditioning; "The check's limit is the mirror of its strength ... An error common to the corpus can survive both" (S3-P6).

TV-17 [S1-P3] "The open questions above are open because the second and third levels had not been posed."
  Context: the replication principle's three levels; S1-P2 documents that the field's own accounts call MI model selection open/thin. The paper documents the openness; this sentence assigns it a cause.

TV-18 [S1-P2] "Only one information criterion has been proposed for multiply imputed data."
  Context: S1-P6 later names two adjacent routes: the Claeskens-Consentino (2008) missing-covariate criteria (a different, Takeuchi-type discrepancy) and the Hens et al. (2006) reweighting route (which "explicitly leaves an imputation-based criterion open"). The "one" refers to Consentino-Claeskens (2010), an averaged-criterion proposal for MI.

TV-19 [S5-P6] "...the Satorra-Bentler arm applies a scaled-and-shifted statistic referred to chi-square_1."
  Context: introduced in the likelihood-ratio simulation design as one of four references; the manuscript cites the scaled-shifted correction literature (Satorra-Bentler; Asparouhov-Muthen 2006; Satorra 2010) in the derivations section (S4) but not at this S5 mention.

TV-20 [S6-P6] "De-shrinkage of estimated noncentrality and joint calibration of score vectors across candidates are developed separately."
  Context: a future-directions sentence; "developed separately" refers to companion/sequel work that is not cited or cross-referenced at this point.
