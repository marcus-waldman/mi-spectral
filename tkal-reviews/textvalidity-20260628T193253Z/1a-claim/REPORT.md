# Text-validity 1a — claim support (does the prose earn each claim?) -- delphi (pool) result

## Round log

- **R1** (nominate): pool=36, slate=20; not stable -- nomination round (no prior to compare)
- **R2** (iterate): pool=36, slate=20; not stable -- votes moved: claude, gemini, openai; membership changed
- **R3** (iterate): pool=36, slate=20; not stable -- votes moved: claude, gemini, openai; membership changed
- **R4** (iterate): pool=36, slate=20; not stable -- votes moved: claude, openai

## Final set (harness output -- the owner ratifies)

Hit the 4-round cap without stability; the arbiter issued the final ruling on residual contested items.

| rank | K-id | item | category | incl | source |
|---|---|---|---|---|---|
| 1 | K01 | ABSTRACT -- [ABSTRACT] "Adding one trace term per candidate removes the bias and restores complete-data-equivalent selection." — trace correction overstates decisions | overclaim | 3 | consensus |
| 2 | K25 | ABSTRACT -- [ABSTRACT] "Model selection on multiply imputed data is biased toward more complex models, because their larger relative increase in variance makes the fit look better than it is." — model-selection scope too broad | overclaim | 3 | consensus |
| 3 | K24 | S1-P4 -- [S1-P4] "The practical consequence is that, for such a model, every deviance and every information criterion computed from multiply imputed data is too optimistic." — every-criterion sign overclaim | overclaim | 3 | consensus |
| 4 | K11 | S1-P6b -- [S1-P6b] "Adding one term per candidate, the trace of its relative-increase-in-variance matrix, removes the bias and substantially restores the ranking that complete data would have given." — trace-only removal overclaim | overclaim | 3 | consensus |
| 5 | K05 | S1-P5 -- [S1-P5] "The missing data have then destroyed part of the evidence in its favor, and we show that no transformation of the observed data can recover it." — unearned impossibility claim | overclaim | 3 | consensus |
| 6 | K04 | S1-P5 -- [S1-P5] "Correction then restores complete-data behavior entirely." — entirely too strong | overclaim | 3 | consensus |
| 7 | K17 | S6-P7 -- [S6-P7] "No transformation of the observed data manufactures the lost evidence back." — restates disclaimed impossibility | overclaim | 3 | consensus |
| 8 | K22 | S6-P1 -- [S6-P1] "The bias exists only when the fit estimates a scale or covariance." — contradicted by known-scale MI | overclaim | 3 | consensus |
| 9 | K23 | S6-P7 -- [S6-P7] "Corrected selection and calibrated tests behave as they would have with complete data." — decision equivalence too broad | overclaim | 3 | consensus |
| 10 | K21 | S6-P7b -- [S6-P7b] "When the aim is to rank models or to compare nested models on imputed data, and no calibrated reference distribution already absorbs the bias, add the per-candidate trace correction before reading off the result." — nested-test correction conflation | overclaim | 3 | consensus |
| 11 | K27 | S1-P4 -- [S1-P4] "A model-comparison table built on imputed data therefore favors the candidates with the most missing information." — deterministic ranking overclaim | overclaim | 3 | consensus |
| 12 | K18 | S6-P7 -- [S6-P7] "Then trust the result the way complete-data results are trusted." — applied trust too broad | overclaim | 3 | consensus |
| 13 | K29 | S5-P22 -- [S5-P22] "The bootstrap imputation sampler reproduces the analytic results on the most demanding cells, which bounds the cost of not running data augmentation." — empirical check not a bound | overclaim | 3 | consensus |
| 14 | K02 | S1-P4 -- [S1-P4] "In our pre-registered study, every misclassification by uncorrected MI-AIC chose the candidate with the largest RIV." | overclaim | 3 | consensus |
| 15 | K28 | S5-P17 -- [S5-P17] "This is a registered directional prediction, and it held across all sixty cells." — cell scope unclear | unsupported-as-written | 3 | consensus |
| 16 | K15 | S3-P6 -- [S3-P6] "A derivation produced and checked within a single model family would likely have shipped one sign without noticing that there was a choice." — counterfactual workflow claim | speculation | 3 | consensus |
| 17 | K33 | S1-P3 -- [S1-P3] "The open questions above are open because the second and third levels had not been posed." — speculates on field history | speculation | 3 | consensus |
| 18 | K36 | S1-P2 -- [S1-P2] "Only one information criterion has been proposed for multiply imputed data." — ignores other cited criteria | overclaim | 3 | consensus |
| 19 | K34 | S5-P6 -- [S5-P6] "By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic referred to $\chi^2_1$." — missing test citation | missing-citation | 3 | consensus |
| 20 | K35 | S6-P6 -- [S6-P6] "De-shrinkage of estimated noncentrality and joint calibration of score vectors across candidates are developed separately." — points to missing reference | missing-citation | 3 | consensus |

**Arbiter ruling rationale:** The consensus set of 20 items already maxes out the open slots and represents a comprehensive list of overclaims, missing citations, and speculations. There are no residual items to review. I have finalized the ranking with the most impactful structural overclaims at the top.