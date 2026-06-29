# todo/039 — Citation-audit to-do list (citation ↔ claim fit)

_Generated from `manuscript/plan/level3-paragraphs.json` (the prose source of truth) on branch `contributions-delphi-todo035`. **35 distinct sources / 69 attachments**; literature coverage complete (0 missing)._

**Goal (per todo/039):** confirm every citation is (a) **valid** — the key resolves to the correct real work — and (b) **appropriate as used** — the source actually supports the specific claim it is attached to, at the claimed strength and scope. Flag: `overstates` (source weaker/narrower than claim) · `misattributed` (claim not in this source) · `wrong-work` (a different reference is correct) · `partial` (supports part) · `unsupported`. Default verdict when the source backs the claim: `supports`.

**Retrieval method per item (“using RAG”):**

1. **Primary — repo-grounded (file-RAG, the ground truth we own):** read `literature/<key>.md` (the verbatim Mathpix source) and locate the exact passage that does or does not establish the attached claim. todo/039 mandates this as the arbiter.

2. **Supplement — vector-RAG over the indexed corpus:** `ask_papers("Does <key> establish <claim>?")` / `search_papers(<claim>)` scoped to project `MI-SPECTRAL`. **Currently DOWN** (litrev MotherDuck/DuckDB backend unreachable as of this session); use once it reconnects to cross-check the file-RAG read, especially for the load-bearing attributions.

**Self-rubber-stamp guard:** every `flagged` or borderline attachment escalates to an independent check (a cold-read Agent on source+claim, or a `tkal-in-ket:quorum` for a contested batch) before it enters the edit list.

**Gates (do NOT edit level3 during the audit):** (1) Marcus signs off this map before auditing → (2) show the flagged set with source passages → (3) show the edit list → apply via an update script under `manuscript/plan/updates/` run through Bash, keep check_plan green, render + commit + push.


---


## Part A · read each source, then judge its attachments (35 sources, load-bearing first)

Each source block: one box to read+characterize the source, then one box per attachment to rule. `LB` = load-bearing (scrutinize hardest).


### 1. `@chanGeneralFeasibleTests2022` `LB` — 5 attachment(s) · S1, S2, S4
> ⚠ AoS 2022 (SMI, drops EFMI, full spectrum). KEEP RESULTS STRAIGHT vs the Stat-Sinica Chan&Meng work.
- [ ] **Read** `literature/chanGeneralFeasibleTests2022.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P2]** + co-cited: `@chanMultipleImprovementsMultiple2022` — verdict: `____`
        claim: “Its modern repairs give tests with accurate size [@chanMultipleImprovementsMultiple2022; @chanGeneralFeasibleTests2022].”
  - [ ] **[S1/S1-P5]** — verdict: `____`
        claim: “Calibrated tests reject at the complete-data rate [@chanGeneralFeasibleTests2022].”
  - [ ] **[S1/S1-P6]** + co-cited: `@chanMultipleImprovementsMultiple2022`, `@mengPerformingLikelihoodRatio1992b` — verdict: `____`
        claim: “The calibration line runs from @mengPerformingLikelihoodRatio1992b through @chanMultipleImprovementsMultiple2022 to @chanGeneralFeasibleTests2022, and it calibrates the reference distribution of an MI test statistic while taking the statistic's numerator as given.”
  - [ ] **[S2/S2-P13]** — verdict: `____`
        claim: “The second strand is the reference distribution. @chanGeneralFeasibleTests2022 drops the equal-fractions assumption entirely.”
  - [ ] **[S4/S4-P14]** — verdict: `____`
        claim: “The limiting law of $\hat d_L$ is the weighted sum $\sum_{j} \lambda_j \chi^2_1$ with $\lambda_j = 1 + r_{\perp,j}$ [@chanGeneralFeasibleTests2022].”

### 2. `@mengMultipleImputationInferencesUncongenial1994a` `LB` — 5 attachment(s) · S1, S2, S4, S6
- [ ] **Read** `literature/mengMultipleImputationInferencesUncongenial1994a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P6]** — verdict: `____`
        claim: “Congeniality is assumed throughout [@mengMultipleImputationInferencesUncongenial1994a].”
  - [ ] **[S2/S2-P7]** + co-cited: `@nielsenProperImproperMultiple2003` — verdict: `____`
        claim: “This paper's analyst always uses the complete-data MLE, which is the case where congeniality implies properness [@mengMultipleImputationInferencesUncongenial1994a; @nielsenProperImproperMultiple2003].”
  - [ ] **[S2/S2-P9]** — verdict: `____`
        claim: “**Congeniality.** The second standing assumption is congeniality, which requires the imputer and the analyst to agree. @mengMultipleImputationInferencesUncongenial1994a formalizes that agreement.”
  - [ ] **[S4/S4-P5]** + co-cited: `@rubinInferenceMissingData1976b`, `@rubinMultipleImputationNonresponse1987`, `@vaartAsymptoticStatistics1998a` — verdict: `____`
        claim: “R1 and R2 are smoothness and positive-definite information [@vaartAsymptoticStatistics1998a], R3 is ignorability [@rubinInferenceMissingData1976b], and R4 through R6 are congeniality, properness, and self-efficiency [@mengMultipleImputationInferencesUncongenial1994a; @rubinMultipleImputationNonresponse1987].”
  - [ ] **[S6/S6-P1]** — verdict: `____`
        claim: “What the bias becomes without it [@mengMultipleImputationInferencesUncongenial1994a] is a separate question.”

### 3. `@chanMultipleImprovementsMultiple2022` `LB` — 4 attachment(s) · S1, S2, S4
> ⚠ Stat Sinica 2022 (stacked-data LRT + EFMI). KEEP RESULTS STRAIGHT vs the AoS Chan work.
- [ ] **Read** `literature/chanMultipleImprovementsMultiple2022.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P2]** + co-cited: `@chanGeneralFeasibleTests2022` — verdict: `____`
        claim: “Its modern repairs give tests with accurate size [@chanMultipleImprovementsMultiple2022; @chanGeneralFeasibleTests2022].”
  - [ ] **[S1/S1-P6]** + co-cited: `@chanGeneralFeasibleTests2022`, `@mengPerformingLikelihoodRatio1992b` — verdict: `____`
        claim: “The calibration line runs from @mengPerformingLikelihoodRatio1992b through @chanMultipleImprovementsMultiple2022 to @chanGeneralFeasibleTests2022, and it calibrates the reference distribution of an MI test statistic while taking the statistic's numerator as given.”
  - [ ] **[S2/S2-P13]** + co-cited: `@mengPerformingLikelihoodRatio1992b` — verdict: `____`
        claim: “The first strand is the combining rule. @mengPerformingLikelihoodRatio1992b combine complete-data likelihood-ratio statistics across imputations into a single test statistic, then calibrate it against an $F$ reference under an equal-fractions assumption. @chanMultipleImprovementsMultiple2022 repair the procedure's known defects by switching the order of operations.”
  - [ ] **[S4/S4-P9]** — verdict: `____`
        claim: “Both models are fit to the same imputations, and the numerator is $$ \hat d_L \;=\; 2\big[\bar Q_\infty(\hat\psi^{*}) - \bar Q_\infty(\hat\psi_0^{*})\big], $$ {#eq-dl} the infinite-$m$ limit of the maximize-then-average statistic of @chanMultipleImprovementsMultiple2022 restated in @sec-background.”

### 4. `@rubinMultipleImputationNonresponse1987` `LB` — 4 attachment(s) · S1, S2, S4
- [ ] **Read** `literature/rubinMultipleImputationNonresponse1987.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P1]** — verdict: `____`
        claim: “An analyst then fits the model of substantive interest to each completed data set, and simple rules combine the results [@rubinMultipleImputationNonresponse1987].”
  - [ ] **[S2/S2-P7]** — verdict: `____`
        claim: “Chapter 4 of @rubinMultipleImputationNonresponse1987 states the validity conditions and gives the fully normal Bayesian scheme as the canonical example.”
  - [ ] **[S2/S2-P8]** — verdict: `____`
        claim: “Result 3.2 of @rubinMultipleImputationNonresponse1987 shows two things.”
  - [ ] **[S4/S4-P5]** + co-cited: `@mengMultipleImputationInferencesUncongenial1994a`, `@rubinInferenceMissingData1976b`, `@vaartAsymptoticStatistics1998a` — verdict: `____`
        claim: “R1 and R2 are smoothness and positive-definite information [@vaartAsymptoticStatistics1998a], R3 is ignorability [@rubinInferenceMissingData1976b], and R4 through R6 are congeniality, properness, and self-efficiency [@mengMultipleImputationInferencesUncongenial1994a; @rubinMultipleImputationNonresponse1987].”

### 5. `@shimodairaInformationCriterionModel2017` `LB` — 4 attachment(s) · S1, S2, S4, S6
- [ ] **Read** `literature/shimodairaInformationCriterionModel2017.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P6]** — verdict: `____`
        claim: “As a penalty, the correction is precedented, because it reproduces $\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017.”
  - [ ] **[S2/S2-P7]** + co-cited: `@cavanaughAkaikeInformationCriterion1998a` — verdict: `____`
        claim: “The Monte Carlo E-step of the previous paragraph is improper by construction, and so is the entire deterministic-EM line of work in which the earlier missing-data criteria were derived [@cavanaughAkaikeInformationCriterion1998a; @shimodairaInformationCriterionModel2017].”
  - [ ] **[S4/S4-P16]** + co-cited: `@cavanaughAkaikeInformationCriterion1998a` — verdict: `____`
        claim: “$$ {#eq-ic-corrected} This penalty reproduces $\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017, and its missing-data surcharge is exactly half that of the earlier complete-data-discrepancy criteria [@cavanaughAkaikeInformationCriterion1998a].”
  - [ ] **[S6/S6-P6]** — verdict: `____`
        claim: “The concluding section of @shimodairaInformationCriterionModel2017 names the combination of a missing mechanism with other sampling mechanisms as future work.”

### 6. `@cavanaughAkaikeInformationCriterion1998a` `LB` — 3 attachment(s) · S1, S2, S4
> ⚠ AICcd = EM observed-data MLE — a PARALLEL universe, NOT this paper's target. Check it is positioned as parallel, not competing.
- [ ] **Read** `literature/cavanaughAkaikeInformationCriterion1998a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P6]** — verdict: `____`
        claim: “That criterion halved the missing-data surcharge of the earlier complete-data-discrepancy criteria [@cavanaughAkaikeInformationCriterion1998a].”
  - [ ] **[S2/S2-P7]** + co-cited: `@shimodairaInformationCriterionModel2017` — verdict: `____`
        claim: “The Monte Carlo E-step of the previous paragraph is improper by construction, and so is the entire deterministic-EM line of work in which the earlier missing-data criteria were derived [@cavanaughAkaikeInformationCriterion1998a; @shimodairaInformationCriterionModel2017].”
  - [ ] **[S4/S4-P16]** + co-cited: `@shimodairaInformationCriterionModel2017` — verdict: `____`
        claim: “$$ {#eq-ic-corrected} This penalty reproduces $\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017, and its missing-data surcharge is exactly half that of the earlier complete-data-discrepancy criteria [@cavanaughAkaikeInformationCriterion1998a].”

### 7. `@consentinoclaeskensOrderSelectionTests2010` `LB` — 3 attachment(s) · S1, S2
> ⚠ The MI averaged-criterion proposal. DIFFERENT work from the 2008 missing-covariate paper.
- [ ] **Read** `literature/consentinoclaeskensOrderSelectionTests2010.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P2]** — verdict: `____`
        claim: “Its authors call for further theoretical and practical study of the method and place that work beyond their own scope [@consentinoclaeskensOrderSelectionTests2010].”
  - [ ] **[S1/S1-P3]** + co-cited: `@woodHowShouldVariable2008a` — verdict: `____`
        claim: “Simulation comparisons of that kind appear in @woodHowShouldVariable2008a and @consentinoclaeskensOrderSelectionTests2010.”
  - [ ] **[S2/S2-P13]** — verdict: `____`
        claim: “The third strand is the criterion. @consentinoclaeskensOrderSelectionTests2010 propose an AIC for multiply imputed data by attaching the Meng-Rubin combined statistic to the standard penalty.”

### 8. `@mengPerformingLikelihoodRatio1992b` `LB` — 3 attachment(s) · S1, S2
- [ ] **Read** `literature/mengPerformingLikelihoodRatio1992b.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P2]** — verdict: `____`
        claim: “For likelihood-ratio tests, a combining rule has existed since @mengPerformingLikelihoodRatio1992b.”
  - [ ] **[S1/S1-P6]** + co-cited: `@chanGeneralFeasibleTests2022`, `@chanMultipleImprovementsMultiple2022` — verdict: `____`
        claim: “The calibration line runs from @mengPerformingLikelihoodRatio1992b through @chanMultipleImprovementsMultiple2022 to @chanGeneralFeasibleTests2022, and it calibrates the reference distribution of an MI test statistic while taking the statistic's numerator as given.”
  - [ ] **[S2/S2-P13]** + co-cited: `@chanMultipleImprovementsMultiple2022` — verdict: `____`
        claim: “The first strand is the combining rule. @mengPerformingLikelihoodRatio1992b combine complete-data likelihood-ratio statistics across imputations into a single test statistic, then calibrate it against an $F$ reference under an equal-fractions assumption. @chanMultipleImprovementsMultiple2022 repair the procedure's known defects by switching the order of operations.”

### 9. `@asparouhovRobustChiSquare2006` `LB` — 2 attachment(s) · S4, S5
> ⚠ Robust chi-square / scaled-shifted. Added to S5-P6 by the 1a pass — verify the new attachment.
- [ ] **Read** `literature/asparouhovRobustChiSquare2006.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S4/S4-P20]** + co-cited: `@satorraEnsuringPositivenessScaled2010` — verdict: `____`
        claim: “The Satorra-Bentler scaled difference statistic matches the mean [@satorraEnsuringPositivenessScaled2010], while the mean-and-variance-adjusted statistics match both from the same moment inputs $\operatorname{tr}(M)$ and $\operatorname{tr}(M^2)$ [@asparouhovRobustChiSquare2006].”
  - [ ] **[S5/S5-P6]** + co-cited: `@satorraEnsuringPositivenessScaled2010` — verdict: `____`
        claim: “By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006] referred to $\chi^2_1$.”

### 10. `@kenwardLikelihoodBasedFrequentist1998` `LB` — 2 attachment(s) · S2, S4
> ⚠ Observed-vs-expected information convention (K&M). Verify it backs the specific convention choice.
- [ ] **Read** `literature/kenwardLikelihoodBasedFrequentist1998.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P12]** — verdict: `____`
        claim: “**Observed versus expected information under MAR.** One convention must be fixed before any trace in this paper is computed, namely which information matrix to use under MAR. @kenwardLikelihoodBasedFrequentist1998 settle the question.”
  - [ ] **[S4/S4-P3]** — verdict: `____`
        claim: “Under MAR the expectation defining $I_{\text{obs}}$ is taken jointly over data and pattern, without conditioning, as @kenwardLikelihoodBasedFrequentist1998 require, and the resulting information carries their mean-covariance cross term.”

### 11. `@nielsenProperImproperMultiple2003` `LB` — 2 attachment(s) · S2
- [ ] **Read** `literature/nielsenProperImproperMultiple2003.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P7]** — verdict: `____`
        claim: “Properness is also not absolute. @nielsenProperImproperMultiple2003 shows that Bayesian imputations are proper when the analyst's complete-data estimator is the maximum likelihood estimator, but the same imputations can fail to be proper for a different estimator.”
  - [ ] **[S2/S2-P7]** + co-cited: `@mengMultipleImputationInferencesUncongenial1994a` — verdict: `____`
        claim: “This paper's analyst always uses the complete-data MLE, which is the case where congeniality implies properness [@mengMultipleImputationInferencesUncongenial1994a; @nielsenProperImproperMultiple2003].”

### 12. `@rubinInferenceMissingData1976b` `LB` — 2 attachment(s) · S2, S4
- [ ] **Read** `literature/rubinInferenceMissingData1976b.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P3]** — verdict: `____`
        claim: “**Ignorability.** This paper assumes throughout that the missingness mechanism is ignorable, in the sense and under the conditions set out by Rubin [@rubinInferenceMissingData1976b].”
  - [ ] **[S4/S4-P5]** + co-cited: `@mengMultipleImputationInferencesUncongenial1994a`, `@rubinMultipleImputationNonresponse1987`, `@vaartAsymptoticStatistics1998a` — verdict: `____`
        claim: “R1 and R2 are smoothness and positive-definite information [@vaartAsymptoticStatistics1998a], R3 is ignorability [@rubinInferenceMissingData1976b], and R4 through R6 are congeniality, properness, and self-efficiency [@mengMultipleImputationInferencesUncongenial1994a; @rubinMultipleImputationNonresponse1987].”

### 13. `@satorraEnsuringPositivenessScaled2010` `LB` — 2 attachment(s) · S4, S5
> ⚠ Scaled-shifted positivity. Added to S5-P6 by the 1a pass — verify the new attachment.
- [ ] **Read** `literature/satorraEnsuringPositivenessScaled2010.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S4/S4-P20]** + co-cited: `@asparouhovRobustChiSquare2006` — verdict: `____`
        claim: “The Satorra-Bentler scaled difference statistic matches the mean [@satorraEnsuringPositivenessScaled2010], while the mean-and-variance-adjusted statistics match both from the same moment inputs $\operatorname{tr}(M)$ and $\operatorname{tr}(M^2)$ [@asparouhovRobustChiSquare2006].”
  - [ ] **[S5/S5-P6]** + co-cited: `@asparouhovRobustChiSquare2006` — verdict: `____`
        claim: “By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006] referred to $\chi^2_1$.”

### 14. `@claeskensconsentinoVariableSelectionIncomplete2008` `LB` — 1 attachment(s) · S1
> ⚠ Missing-COVARIATE, Takeuchi-type discrepancy — DIFFERENT from the MI averaged-criterion 2010 work. Do not conflate the two C-C papers.
- [ ] **Read** `literature/claeskensconsentinoVariableSelectionIncomplete2008.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P6]** — verdict: `____`
        claim: “The missing-covariate criteria of @claeskensconsentinoVariableSelectionIncomplete2008 target a different, Takeuchi-type discrepancy.”

### 15. `@daviesAlgorithm155Distribution1980` `LB` — 1 attachment(s) · S4
> ⚠ Quadratic-form distribution algorithm. §4 — numerical-method attribution.
- [ ] **Read** `literature/daviesAlgorithm155Distribution1980.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S4/S4-P20]** + co-cited: `@imhofComputingDistributionQuadratic1961` — verdict: `____`
        claim: “The weighted-$\chi^2$ distribution function is evaluated by numerical inversion of the characteristic function [@imhofComputingDistributionQuadratic1961; @daviesAlgorithm155Distribution1980].”

### 16. `@hensModelSelectionIncomplete2006a` `LB` — 1 attachment(s) · S1
- [ ] **Read** `literature/hensModelSelectionIncomplete2006a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P6]** — verdict: `____`
        claim: “The reweighting route of @hensModelSelectionIncomplete2006a reaches the complete-data target through inverse-probability weights, but it explicitly leaves an imputation-based criterion open.”

### 17. `@imhofComputingDistributionQuadratic1961` `LB` — 1 attachment(s) · S4
> ⚠ Quadratic-form distribution. §4 — numerical-method attribution.
- [ ] **Read** `literature/imhofComputingDistributionQuadratic1961.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S4/S4-P20]** + co-cited: `@daviesAlgorithm155Distribution1980` — verdict: `____`
        claim: “The weighted-$\chi^2$ distribution function is evaluated by numerical inversion of the characteristic function [@imhofComputingDistributionQuadratic1961; @daviesAlgorithm155Distribution1980].”

### 18. `@kolenTestEquatingScaling2014` `LB` — 1 attachment(s) · S4
- [ ] **Read** `literature/kolenTestEquatingScaling2014.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S4/S4-P20]** — verdict: `____`
        claim: “$$ \begin{aligned} \hat d^{(3)}_k &\;=\; F^{-1}_{\chi^2_{q_{d,k}}}\big(F_{W_k}(\hat d_k)\big), \\ W_k &= \textstyle\sum_j \lambda_{k,j} \chi^2_1, \end{aligned} $$ The equating function from observed-score test equating is $e_Y(x) = G^{-1}[F(x)]$ [@kolenTestEquatingScaling2014].”

### 19. `@vuongLikelihoodRatioTests1989` `LB` — 1 attachment(s) · S4
> ⚠ Non-nested LRT. §4 — verify it backs the non-nested regime claim only.
- [ ] **Read** `literature/vuongLikelihoodRatioTests1989.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S4/S4-P13]** — verdict: `____`
        claim: “That last case is the regime of @vuongLikelihoodRatioTests1989. :::”

### 20. `@weiMonteCarloImplementation1990` `LB` — 1 attachment(s) · S2
- [ ] **Read** `literature/weiMonteCarloImplementation1990.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P6]** — verdict: `____`
        claim: “**Imputation is Monte Carlo integration of the E-step.** The averaged log-likelihood over imputations is itself a Q-function, computed by Monte Carlo. @weiMonteCarloImplementation1990 implement the E-step by simulation, drawing $z^{(1)},\dots,z^{(m)}$ from the conditional predictive distribution of the missing data.”

### 21. `@woodburyMissingInformationPrinciple1972` `LB` — 1 attachment(s) · S2
- [ ] **Read** `literature/woodburyMissingInformationPrinciple1972.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P4]** — verdict: `____`
        claim: “**The missing-information principle and the RIV.** The paper's central matrix is the relative-increase-in-variance matrix, and it comes from the missing-information principle. @woodburyMissingInformationPrinciple1972 decompose the information in the complete data into the observed-data information plus what they call the lost information.”

### 22. `@Meng01121991` — 2 attachment(s) · S2
> ⚠ Odd citekey (Zotero-style, not BBT). Verify identity (Meng & Rubin 1991, score/info decomposition?) and that the key resolves to the right work.
- [ ] **Read** `literature/Meng01121991.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P4]** — verdict: `____`
        claim: “They state this decomposition together with a score identity, in which the observed-data score is the conditional expectation of the complete-data score. @Meng01121991 state the same principle in the form used throughout this paper: $$ I_{\text{obs}} \;=\; I_{\text{com}} - I_{\text{mis}\mid\text{obs}}, $$ {#eq-bg-mip} In words, observed information equals complete information $-$ missing information.”
  - [ ] **[S2/S2-P4]** + co-cited: `@dempsterMaximumLikelihoodIncomplete1977a` — verdict: `____`
        claim: “One warning is needed here, because the EM literature works with a different normalization of the same ingredients, namely the EM rate matrix $DM = I_{\text{mis}\mid\text{obs}}\, I_{\text{com}}^{-1}$ of @dempsterMaximumLikelihoodIncomplete1977a and @Meng01121991.”

### 23. `@dempsterMaximumLikelihoodIncomplete1977a` — 2 attachment(s) · S2
- [ ] **Read** `literature/dempsterMaximumLikelihoodIncomplete1977a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P4]** + co-cited: `@Meng01121991` — verdict: `____`
        claim: “One warning is needed here, because the EM literature works with a different normalization of the same ingredients, namely the EM rate matrix $DM = I_{\text{mis}\mid\text{obs}}\, I_{\text{com}}^{-1}$ of @dempsterMaximumLikelihoodIncomplete1977a and @Meng01121991.”
  - [ ] **[S2/S2-P5]** — verdict: `____`
        claim: “So its definition and one geometric fact about it are needed. @dempsterMaximumLikelihoodIncomplete1977a define $$ Q(\phi' \mid \phi) \;=\; E\big(\log f(\mathbf{x} \mid \phi') \,\big|\, \mathbf{y}, \phi\big), $$ {#eq-bg-q} the expected complete-data log-likelihood given the observed data.”

### 24. `@endersMissingDataUpdate2025` — 2 attachment(s) · S1
- [ ] **Read** `literature/endersMissingDataUpdate2025.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P1]** + co-cited: `@schaferMissingDataOur2002a` — verdict: `____`
        claim: “The field's own accounts of its state of the art describe a mature methodology [@schaferMissingDataOur2002a; @endersMissingDataUpdate2025].”
  - [ ] **[S1/S1-P2]** — verdict: `____`
        claim: “Neither does the current state-of-the-art review [@endersMissingDataUpdate2025].”

### 25. `@schaferAnalysisIncompleteMultivariate1997` — 2 attachment(s) · S4
- [ ] **Read** `literature/schaferAnalysisIncompleteMultivariate1997.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S4/S4-P2]** — verdict: `____`
        claim: “The other is the observed-data maximizer $\hat\theta_{\text{obs}}$, which sums each row's marginal density over its observed coordinates [@schaferAnalysisIncompleteMultivariate1997] and is the best available from the data at hand.”
  - [ ] **[S4/S4-P3]** — verdict: `____`
        claim: “Here the fraction-of-missing-information matrix $D = I_{\text{com}}^{-1} I_{\text{mis}\mid\text{obs}}$ [@schaferAnalysisIncompleteMultivariate1997] has the same trace ingredients but the other normalization, and the two relate by $D = (I_k + \mathrm{RIV})^{-1}\mathrm{RIV}$.”

### 26. `@shimodairahidetoshiImprovingPredictiveInference2000` — 2 attachment(s) · S1, S6
- [ ] **Read** `literature/shimodairahidetoshiImprovingPredictiveInference2000.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P6]** — verdict: `____`
        claim: “His concluding section names the combination of missingness with other sampling mechanisms, such as covariate shift [@shimodairahidetoshiImprovingPredictiveInference2000], as future work.”
  - [ ] **[S6/S6-P6]** — verdict: `____`
        claim: “The weighting machinery exists [@shimodairahidetoshiImprovingPredictiveInference2000].”

### 27. `@woodHowShouldVariable2008a` — 2 attachment(s) · S1
- [ ] **Read** `literature/woodHowShouldVariable2008a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P2]** — verdict: `____`
        claim: “A dedicated study of variable selection with multiply imputed data reports that no guidelines yet exist [@woodHowShouldVariable2008a].”
  - [ ] **[S1/S1-P3]** + co-cited: `@consentinoclaeskensOrderSelectionTests2010` — verdict: `____`
        claim: “Simulation comparisons of that kind appear in @woodHowShouldVariable2008a and @consentinoclaeskensOrderSelectionTests2010.”

### 28. `@Tierney01031986` — 1 attachment(s) · S2
> ⚠ Odd citekey (Zotero-style, not BBT). Verify identity (Tierney & Kadane 1986, Laplace approximation?).
- [ ] **Read** `literature/Tierney01031986.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P8]** — verdict: `____`
        claim: “One approximation separates the exact identities from usable inference, namely the usual treatment of the posterior distribution as approximately normal, a Laplace-type approximation [@Tierney01031986].”

### 29. `@akaikeNewLookStatistical1974a` — 1 attachment(s) · S2
- [ ] **Read** `literature/akaikeNewLookStatistical1974a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P10]** — verdict: `____`
        claim: “**AIC is a bias-corrected plug-in estimate.** The model-selection application corrects AIC, so AIC's own logic is needed first. @akaikeNewLookStatistical1974a evaluates a fitted model by its mean log-likelihood against the true distribution.”

### 30. `@honakerAmeliaIIProgram2011` — 1 attachment(s) · S5
- [ ] **Read** `literature/honakerAmeliaIIProgram2011.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S5/S5-P2]** — verdict: `____`
        claim: “The proper arm draws imputations by expectation-maximization with bootstrapping, as implemented in Amelia [@honakerAmeliaIIProgram2011].”

### 31. `@schaferMissingDataOur2002a` — 1 attachment(s) · S1
- [ ] **Read** `literature/schaferMissingDataOur2002a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P1]** + co-cited: `@endersMissingDataUpdate2025` — verdict: `____`
        claim: “The field's own accounts of its state of the art describe a mature methodology [@schaferMissingDataOur2002a; @endersMissingDataUpdate2025].”

### 32. `@schomakerModelSelectionModel2014a` — 1 attachment(s) · S1
- [ ] **Read** `literature/schomakerModelSelectionModel2014a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P2]** — verdict: `____`
        claim: “The first comprehensive study of model selection after multiple imputation describes the available literature as unexpectedly thin [@schomakerModelSelectionModel2014a].”

### 33. `@vaartAsymptoticStatistics1998a` — 1 attachment(s) · S4
- [ ] **Read** `literature/vaartAsymptoticStatistics1998a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S4/S4-P5]** + co-cited: `@mengMultipleImputationInferencesUncongenial1994a`, `@rubinInferenceMissingData1976b`, `@rubinMultipleImputationNonresponse1987` — verdict: `____`
        claim: “R1 and R2 are smoothness and positive-definite information [@vaartAsymptoticStatistics1998a], R3 is ignorability [@rubinInferenceMissingData1976b], and R4 through R6 are congeniality, properness, and self-efficiency [@mengMultipleImputationInferencesUncongenial1994a; @rubinMultipleImputationNonresponse1987].”

### 34. `@vanbuurenFlexibleImputationMissing2018a` — 1 attachment(s) · S1
- [ ] **Read** `literature/vanbuurenFlexibleImputationMissing2018a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S1/S1-P2]** — verdict: `____`
        claim: “The standard book-length treatment does not treat information criteria for multiply imputed data at all [@vanbuurenFlexibleImputationMissing2018a].”

### 35. `@wilksLargeSampleDistributionLikelihood1938a` — 1 attachment(s) · S2
- [ ] **Read** `literature/wilksLargeSampleDistributionLikelihood1938a.md` — record what it actually establishes (claim, scope, strength, setting); confirm the key resolves to the right work.
  - [ ] **[S2/S2-P11]** — verdict: `____`
        claim: “For this case @wilksLargeSampleDistributionLikelihood1938a shows that $-2\log\lambda$ is distributed as $\chi^2_{h-m}$ in large samples, so this distribution is the reference against which every multiply imputed deviance in this paper is ultimately compared.”

---


## Part B · wrap-up
- [ ] Compile all non-`supports` verdicts → flagged set (with the exact source passage per flag).
- [ ] Independent cold-read / quorum on the flagged + borderline set (self-rubber-stamp guard).
- [ ] Show Marcus the flagged set; build the edit list (fix attribution / soften to what the source supports / swap to correct work / add a better source / move-or-remove).
- [ ] Apply via `manuscript/plan/updates/update-citation-audit-039-<date>.py` (Bash); check_plan green; render (APA preview, expect 85 ¶); commit + push.
- [ ] Fold in the S4-P22 consistency item (“developed separately” → “left to future work”, mirroring the S6-P6 1a fix) if wanted here.
