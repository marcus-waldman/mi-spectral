# mi-spectral contributions (pool) -- delphi (pool) result

## Round log

- **R1** (nominate): pool=23, slate=8; not stable -- nomination round (no prior to compare)
- **R2** (iterate): pool=23, slate=8; not stable -- votes moved: claude, gemini; membership changed
- **R3** (iterate): pool=23, slate=8; not stable -- votes moved: claude, gemini, openai; membership changed
- **R4** (iterate): pool=23, slate=8; not stable -- votes moved: claude
- **R5** (iterate): pool=23, slate=8; STABLE -- no vote moved and membership unchanged

## Final set (harness output -- the owner ratifies)

Converged STABLE at round 5.

| rank | K-id | item | category | incl | source |
|---|---|---|---|---|---|
| 1 | K11 | Under congenial proper MI with an estimated scale and complete-data MLE target, the averaged imputation log-likelihood overstates the complete-data log-likelihood by +1/2 tr(RIV) plus a MAR design-imbalance term that vanishes under MCAR. | theory | 3 | consensus |
| 2 | K09 | Applied MI model-selection tables should add a per-candidate tr(RIV_k) correction to AIC/BIC when the target is complete-data-equivalent selection, because uncorrected criteria tilt toward models with more missing information. | applied-implication | 3 | consensus |
| 3 | K03 | For information-criterion selection there is no protective reference distribution, so the per-model correction tr(RIV_k) must be applied to restore complete-data-equivalent ranking; for a calibrated likelihood-ratio test (Chan 2022) the mean is already absorbed and the correction must not be applied a second time. | applied-implication | 3 | consensus |
| 4 | K12 | The MI information-criterion bias is model-specific: candidate models can have different RIV traces, so adding tr(RIV_k) supplies the theoretical centering correction for MI-AIC and MI-BIC under the stated target. | IC-application | 3 | consensus |
| 5 | K10 | We make the structured AI-human workflow a first-class contribution by documenting, for this study, transparent provenance and auditable gates for sourced citations, human acceptance, dual computer-algebra verification, preregistered simulations, adversarial rederivation, and full reproducibility. | methodology-workflow | 3 | consensus |
| 6 | K14 | For nested MI likelihood-ratio comparisons at the null, the numerator's differential bias is tr(RIV_perp), the missing information in the tested directions projected in the complete-data information metric, not tr(RIV_full)-tr(RIV_0). | LRT-application | 3 | consensus |
| 7 | K16 | Applied teams evaluating AI-assisted statistical derivations should require auditable evidence of the same kind used here: sourced citations, independent symbolic checks, preregistered numerical criteria with reported failures, adversarial review, and reproducibility records. | applied-implication | 3 | consensus |
| 8 | K15 | Nested MI likelihood-ratio comparisons should reuse the same imputations for the competing fits, since pairing reduces null and local-alternative Monte Carlo noise from order sqrt(n) to order one. | LRT-application | 3 | consensus |