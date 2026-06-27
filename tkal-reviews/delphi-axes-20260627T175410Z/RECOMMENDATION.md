# mi-spectral contributions (axes ratification) -- consensus recommendation for the owner

- Date: 2026-06-27
- Panel: Claude/Opus 4.8 (`claude-opus-4-8`), GPT-5.5 (`gpt-5.5-pro-2026-04-23`), Gemini (`models/gemini-3.1-pro-preview`), anonymized B/A/C.
- Convergence: **5 unanimous, 7 majority, 0 split** of 12 axes. Agreement tallied in CODE from discrete endorsement votes; multi-model consensus is a strong signal, NOT ground truth -- **the owner ratifies.**

> Every row below is a RECOMMENDATION. The cardinal control is human ratification; the panel proposes, the owner authorizes.

## The recommendation, per axis

### Ratify item 1 (theory)  — **MAJORITY**
_Axis `ratify-1`. Votes: B×1, MERGE×2._

**Recommended disposition:** KEEP-WITH-REVISION. Exact revised sentence: Under congenial proper MI with an estimated scale and the complete-data MLE target, the averaged log-likelihood across imputations overstates the complete-data log-likelihood by +1/2 tr(RIV) plus a MAR design-imbalance term that vanishes exactly under MCAR; the proper-MI proof and the MAR design-imbalance term are the novel parts, while the trace magnitude coincides with Shimodaira's AIC_{x;y} penalty. The revision fixes novelty scoping; real, applied importance, and technical scope otherwise pass.

### Ratify item 2 (applied-implication: add tr(RIV_k))  — **MAJORITY**
_Axis `ratify-2`. Votes: A×1, MERGE×2._

**Recommended disposition:** KEEP-WITH-REVISION. The directive is the single most actionable takeaway and follows from the firm model-specific bias result, but the scope should make the scale explicit. Revised: 'Under the paper's proper-MI conditions, applied MI AIC/BIC tables targeting complete-data-equivalent selection should add a per-candidate tr(RIV_k) to each criterion (on the -2 log-likelihood scale), because uncorrected criteria tilt toward models with more missing information.'

### Ratify item 3 (applied-implication: where it applies / do not double-apply)  — **UNANIMOUS**
_Axis `ratify-3`. Votes: A×3._

**Recommended disposition:** KEEP-WITH-REVISION. Revised: 'For information-criterion ranking, where no calibrated reference distribution absorbs the mean, use the per-candidate tr(RIV_k) centering correction for complete-data-equivalent selection; for a Chan-style calibrated nested likelihood-ratio test, do not add a separate numerator mean correction because the null mean is already absorbed by the reference distribution.' This limits the LRT warning to calibrated nested tests and avoids the overstrong 'must restore ranking' wording.

### Ratify item 4 (IC-application: model-specific bias)  — **UNANIMOUS**
_Axis `ratify-4`. Votes: A×3._

**Recommended disposition:** KEEP-WITH-REVISION. Revised: 'The MI information-criterion bias is model-specific: candidate models can have different RIV traces, so on the usual -2 log-likelihood scale adding tr(RIV_k) supplies the theoretical centering correction for MI-AIC and MI-BIC under the complete-data-equivalent target.' The revision specifies criterion scale and target instead of relying on the vague 'stated target.'

### Ratify item 5 (methodology-workflow, first-class)  — **MAJORITY**
_Axis `ratify-5`. Votes: A×1, MERGE×2._

**Recommended disposition:** KEEP-WITH-REVISION. The documented facts are firm but 'first-class contribution' must carry the self-coding limit it currently omits. Revised: 'We treat the structured AI-human workflow as a first-class methodological contribution by documenting, for this study, ORCID-verified human provenance and auditable gates -- sourced citations, human acceptance of every result, dual computer-algebra verification, preregistered simulations with reported failures, adversarial rederivation (which caught an 8-of-9 sign error), and full reproducibility -- where the verifiable records are mechanically checked, while the qualitative session-coding frequencies are model judgments produced by the same lineage analyzed, without a human second coder.'

### Ratify item 6 (LRT-application: tr(RIV_perp))  — **MAJORITY**
_Axis `ratify-6`. Votes: A×1, MERGE×2._

**Recommended disposition:** KEEP-WITH-REVISION. Exact revised sentence: For nested MI likelihood-ratio comparisons at the null, the numerator's differential deviance bias is tr(RIV_perp), the missing information in the tested directions projected in the complete-data information metric, not tr(RIV_full) minus tr(RIV_0). The revision fixes wording and deviance-scale precision; real, novelty, applied importance, and scope pass.

### Ratify item 7 (applied-implication: demand auditable evidence)  — **UNANIMOUS**
_Axis `ratify-7`. Votes: A×3._

**Recommended disposition:** KEEP-WITH-REVISION. Revised: 'Applied teams evaluating AI-assisted statistical derivations should ask for commensurate auditable evidence before relying on the results: sourced citations, independent symbolic checks where applicable, preregistered numerical criteria with reported failures, adversarial review, and reproducibility records.' The revision frames this as a reliance standard rather than a universal proof of correctness or a rigid recipe.

### Ratify item 8 (LRT-application: reuse imputations / pairing)  — **UNANIMOUS**
_Axis `ratify-8`. Votes: A×3._

**Recommended disposition:** KEEP-WITH-REVISION. Revised: 'For nested MI likelihood-ratio comparisons at the null or local alternatives, fit the competing models to the same imputed data sets whenever possible, because this pairing reduces Monte Carlo noise from order sqrt(n) to order one.' Novelty is the MI-LRT-specific order result rather than the generic common-random-numbers idea; the revision tightens the scope.

### Consolidate the three overlapping IC / tr(RIV_k) items (ranks 2, 3, 4)  — **UNANIMOUS**
_Axis `consolidate`. Votes: MERGE×3._

**Recommended disposition:** CONSOLIDATE TO TWO. Introduction contributions list (the result, merging item 4 and the directive of item 2): 'For information-criterion selection after proper MI, the deviance bias is model-specific -- candidate models can have different RIV traces, so uncorrected AIC/BIC tilt toward higher-missing-information candidates -- and adding tr(RIV_k) to each criterion gives the centering correction for complete-data-equivalent selection.' Discussion applied-implications passage (the scope guard, item 3): 'In practice, use the per-candidate tr(RIV_k) correction for IC ranking and other uses where no calibrated reference distribution absorbs the mean; do not add a separate numerator correction to a Chan-style calibrated nested likelihood-ratio test, where the null mean is already built into the reference distribution.'

### Anything missing from the set  — **MAJORITY + caveat**
_Axis `completeness`. Votes: A×1, MERGE×2._

**Recommended disposition:** COMPLETE. The eight-item set is sufficient for the skim layer. The W3-C=1.000 finding, the calibration ladder, and the Shimodaira reproduction are strong supporting evidence but belong inside the IC-application section as proof/validation, not as separate headline contributions; promoting any of them would dilute the single actionable message (add tr(RIV_k)) with detail a skimming applied reader does not need to act on. The 100%-on-largest-RIV result should appear prominently as the empirical confirmation of the tilt within the IC section, but as evidence rather than as a ninth contribution bullet.

**Residual dissent / caveats:**
- [B] C preferred adding the 100%-largest-RIV finding to the Introduction list; I concede it should be reported prominently as supporting evidence but not as a separate skim-layer contribution, since it is a validation of the already-ratified result rather than an independent applied action.

### Lead contribution + abstract hook  — **MAJORITY**
_Axis `lead-hook`. Votes: A×1, MERGE×2._

**Recommended disposition:** Lead with item 2 (the applied tr(RIV_k) directive), placing the general theorem immediately after so the applied claim is visibly grounded. Abstract hook: 'Model-selection tables built on multiply-imputed data are systematically biased toward models with more missing information; we prove the bias is one trace term per candidate, tr(RIV_k), give the one-line correction that restores complete-data-equivalent selection, and show exactly where it must -- and must not -- be applied.'

### Workflow framing and credit  — **MAJORITY + caveat**
_Axis `workflow-framing`. Votes: A×1, MERGE×2._

**Recommended disposition:** FIRST-CLASS, but framed so the self-coding limit is carried in the same sentence. Framing: 'We treat the AI-human workflow as a first-class methodological contribution, co-equal with the technical results, because this study pairs mechanically checkable provenance and verification gates -- sourced citations, dual computer-algebra checks, preregistration with reported failures, and an adversarial rederivation that caught an 8-of-9 sign error -- with a transparent audit trail, while reporting the same-lineage session-coding frequencies as model judgments rather than independently human-coded measurements.'

**Residual dissent / caveats:**
- [B] B preferred ranking the workflow as SUPPORTING given the self-coding limit; I judge first-class defensible because the load-bearing records are mechanically verified and only the qualitative frequencies are model judgments, which the framing explicitly discloses.
- [A] Minority concern remains that the absence of a human second coder could justify ranking the workflow as supporting rather than co-equal; the first-class framing should be ratified only if the caveat is carried prominently.

## Residual SPLITS for the owner

- (none — every axis reached unanimous or majority consensus)