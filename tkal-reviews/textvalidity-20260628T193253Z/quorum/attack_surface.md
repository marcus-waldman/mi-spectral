PRE-DISCLOSED WEAK POINTS — the 20 issues a cross-family claim-support review (Claude + GPT-5.5 + Gemini, unanimous 3/3) flagged in the manuscript prose. Probe EACH of these first as a distinct objection (tag it with the bar it threatens), then hunt for anything the advocate did NOT disclose. Each item gives the paragraph ID, the VERBATIM sentence/clause challenged, the bar it most threatens, and the reviewers' reason.

TV-01 [ABSTRACT] — bar: scope_calibration
  Claim: "Adding one trace term per candidate removes the bias and restores complete-data-equivalent selection."
  Reason: the body shows bias removal in expectation and selection "substantially" restored with a residual gap / weak-signal floor; "restores complete-data-equivalent selection" reads as full decision-level recovery, stronger than shown.

TV-02 [ABSTRACT] — bar: scope_calibration
  Claim: "Model selection on multiply imputed data is biased toward more complex models, because their larger relative increase in variance makes the fit look better than it is."
  Reason: the result concerns particular likelihood-based criteria under congenial proper MI; more complex models need not always carry the larger missing-information trace, so the complexity framing is broader than the RIV result establishes.

TV-03 [S1-P4] — bar: scope_calibration
  Claim: "for such a model, every deviance and every information criterion computed from multiply imputed data is too optimistic."
  Reason: the derivation is for the averaged log-likelihood/Q-function under stated conditions; "every deviance and every information criterion" universalizes the sign and scope beyond the estimated-scale and design-imbalance qualifications.

TV-04 [S1-P6b] — bar: scope_calibration
  Claim: "Adding one term per candidate, the trace of its relative-increase-in-variance matrix, removes the bias and substantially restores the ranking that complete data would have given."
  Reason: omits the design-imbalance term; ranking restoration is conditional/empirical (a residual gap remains), so "removes the bias and ... restores the ranking" still reads stronger than shown even with "substantially".

TV-05 [S1-P5] — bar: internal_consistency (also claim_support)
  Claim: "The missing data have then destroyed part of the evidence in its favor, and we show that no transformation of the observed data can recover it."
  Reason: a general impossibility claim that contradicts the paper's own limitation G4 (S6-P3): "No argument here shows that no estimator built from the same observed data could do better."

TV-06 [S1-P5] — bar: scope_calibration
  Claim: "Correction then restores complete-data behavior entirely."
  Reason: "entirely" overstates; the ladder/ calibration results reach the benchmark in the strong-signal case but not the weak-signal cell (the floor), so full restoration is not demonstrated in general.

TV-07 [S6-P7] — bar: internal_consistency (also claim_support)
  Claim: "No transformation of the observed data manufactures the lost evidence back."
  Reason: restates the same impossibility the paper explicitly disclaims having proven in G4 — a direct internal contradiction in the conclusion.

TV-08 [S6-P1] — bar: internal_consistency / scope_calibration
  Claim: "The bias exists only when the fit estimates a scale or covariance."
  Reason: the same paragraph then says a known-scale, location-only fit has "-1/2 tr(RIV) under proper MI" — a nonzero bias — so the unqualified "only" appears contradicted by the paper's own next sentence.

TV-09 [S6-P7] — bar: scope_calibration
  Claim: "Corrected selection and calibrated tests behave as they would have with complete data."
  Reason: the simulations show scoped null-side recovery and a weak-signal floor, not a general guarantee that corrected selection and calibrated tests behave like complete-data procedures in all decision settings.

TV-10 [S6-P7b] — bar: internal_consistency
  Claim: "When the aim is to rank models or to compare nested models on imputed data, and no calibrated reference distribution already absorbs the bias, add the per-candidate trace correction before reading off the result."
  Reason: the paper's own likelihood-ratio result says the per-candidate (difference-of-corrections) approach OVERSTATES the nested-comparison bias (the right object is tr(RIV_perp) in the complete-data metric); recommending the per-candidate trace correction for nested comparison conflates IC ranking with the nested-test correction.

TV-11 [S1-P4] — bar: scope_calibration
  Claim: "A model-comparison table built on imputed data therefore favors the candidates with the most missing information."
  Reason: the bias is a directional tendency; realized rankings also depend on fit, penalty, signal strength, and candidate geometry, so "therefore favors" reads deterministic rather than all-else-equal.

TV-12 [S6-P7] — bar: scope_calibration
  Claim: "Then trust the result the way complete-data results are trusted."
  Reason: a blanket applied endorsement that drops the paper's own boundaries stated just above/elsewhere (estimated-scale, congeniality, weak-signal floor, normal-family verification).

TV-13 [S5-P22] — bar: claim_support
  Claim: "The bootstrap imputation sampler reproduces the analytic results on the most demanding cells, which bounds the cost of not running data augmentation."
  Reason: an empirical agreement check in selected cells is not a derived bound on the unrun data-augmentation alternative; "bounds" claims more than an empirical reproduction supports.

TV-14 [S1-P4] — bar: scope_calibration / internal_consistency
  Claim: "In our pre-registered study, every misclassification by uncorrected MI-AIC chose the candidate with the largest RIV."
  Reason: the results section limits this to congenial cells ("In every congenial cell, all of the uncorrected criterion's errors land on the saturated ... candidate"); the unqualified "every misclassification" in the intro drops that qualifier.

TV-15 [S5-P17] — bar: scope_calibration / internal_consistency
  Claim: "This is a registered directional prediction, and it held across all sixty cells."
  Reason: the preceding sentence limits the pattern to congenial cells, while the design includes uncongenial cells with reported overshoot; "all sixty cells" needs a clear pointer to which prediction held in which cells.

TV-16 [S3-P6] — bar: claim_support (speculation)
  Claim: "A derivation produced and checked within a single model family would likely have shipped one sign without noticing that there was a choice."
  Reason: an unsupported counterfactual about an unrun single-family workflow; the observed 8-of-9 figure is cross-family, not a controlled single-family comparison.

TV-17 [S1-P3] — bar: claim_support (speculation)
  Claim: "The open questions above are open because the second and third levels had not been posed."
  Reason: asserts a singular historical cause for the field's open questions; they could be open for other reasons (intractability, shifting focus), and the paper does not establish the causal claim.

TV-18 [S1-P2] — bar: internal_consistency / claim_support
  Claim: "Only one information criterion has been proposed for multiply imputed data."
  Reason: reads as an absolute literature claim that sits awkwardly with the paper's own later mention of the Claeskens-Consentino (2008) missing-covariate criteria and the Hens et al. (2006) reweighting route (S1-P6).

TV-19 [S5-P6] — bar: citation_support
  Claim: "By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic referred to chi-square_1."
  Reason: a named external test correction introduced with no citation or prior setup.

TV-20 [S6-P6] — bar: citation_support
  Claim: "De-shrinkage of estimated noncentrality and joint calibration of score vectors across candidates are developed separately."
  Reason: "developed separately" implies a companion paper or external literature but provides no citation or cross-reference for the reader to follow.
