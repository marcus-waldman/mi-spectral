# todo/039 — Citation Audit Results

Branch: `contributions-delphi-todo035`

This is an audit artifact (not the manuscript), so verbatim quotation of `literature/` sources is permitted here per todo/039 / D-17.

## Summary

- Audited: **69 citation attachments** across **35 sources**.
- Independently verified (second adversarial pass): **3**.
- Flagged (final verdict not `supports`): **3**.
- First-pass vs independent disagreements: **1**.
- Source-identity confirmations: **35 / 35 OK**.

Counts by final verdict:

| Final verdict | Count |
|---|---|
| supports | 66 |
| misattributed | 1 |
| partial | 2 |
| **Total** | **69** |

All three non-`supports` verdicts were independently verified. The only first-pass/independent disagreement is the one source that ended at `misattributed` (first pass had it as `partial`).

## Flagged — needs an edit decision

Three attachments did not clear as `supports`. All three are load-bearing. One is a `misattributed` (the directional implication is pinned on the wrong co-citation); the other two are the same compound `scaled-and-shifted` claim split across two SEM references, each only `partial`.

### 1. `mengMultipleImputationInferencesUncongenial1994a` — S2/S2-P7 (load-bearing)

- Verdict: **partial (first pass) -> misattributed (independent)**. FINAL: **misattributed**.
- Confidence (first pass): medium. Independently verified: yes.

Claim:

> This paper's analyst always uses the complete-data MLE, which is the case where congeniality implies properness [@mengMultipleImputationInferencesUncongenial1994a; @nielsenProperImproperMultiple2003].

Evidence passage (first-pass and independent cite the same line):

> We emphasize that the concept of second-moment proper is only with respect to the analyst's complete-data procedure, in contrast to the concept of congeniality, which is with respect to the analyst's complete-data and incomplete-data procedures. An imputation model, therefore, can be second-moment proper but still uncongenial to the analysis procedure.

First-pass rationale (partial): Meng supplies the two concepts the claim uses: congeniality (Def 1-2) and second-moment proper, explicitly defined 'with respect to the analyst's complete-data procedure' (Def 3), which matches the complete-data-procedure framing. But Meng never mentions the MLE/maximum likelihood (0 occurrences in the paper), and never states the asserted direction 'congeniality implies properness'; the only proper-vs-congenial directional statement in Meng is the CONVERSE non-implication (proper does not imply congenial, line quoted). Meng's 'Main result' even lists self-efficiency and second-moment properness as separate conditions rather than deriving one from congeniality. The load-bearing directional implication, and the efficient/complete-data-estimator (MLE) framing, are carried by the co-cited Nielsen (2003), not by Meng. So Meng backs the vocabulary/framework (part of the claim) but not the implication itself.

Independent (verifier) rationale (misattributed): The claim credits Meng (1994) with the directional implication "congeniality implies properness" (in the complete-data-MLE case). Meng establishes no such implication. He defines congeniality (Def. 1-2) and second-moment proper (Def. 3) as DISTINCT concepts on different axes: congeniality is a conditional Bayesian-matching property w.r.t. BOTH the analyst's incomplete- and complete-data procedures; properness is a randomization-averaged property w.r.t. ONLY the complete-data procedure. The single explicit statement linking them (line 371) asserts the REVERSE non-implication: a model "can be second-moment proper but still uncongenial." In his Main result (lines 503-514), properness is an INDEPENDENT condition (c), not a consequence of congeniality (which is not even among the conditions) — indeed Meng's entire purpose is to make properness usable WITHOUT congeniality. He also never singles out the MLE case for this relationship; his analyst-side condition is self-efficiency (Def. 5), not the MLE. So the specific load-bearing proposition ("congeniality implies properness") is not in Meng at any strength, and the relationship he does state runs against treating the two as nested in the claimed direction. The proposition may be true and supported elsewhere (plausibly the co-cited Nielsen 2003, or Rubin 1987), but pinning it on Meng (1994) misattributes a directional implication the source does not make. Not "overstates," because there is no weaker version of this implication in Meng to inflate; not "wrong-work," because Meng is the foundational congeniality source and thus the right neighborhood.

Edit-decision note: the co-cited `@nielsenProperImproperMultiple2003` does carry "congeniality implies properness" with the MLE framing (its own S2/S2-P7 attachments both verify `supports`). The minimal fix is to attribute the directional implication to Nielsen and keep Meng for the vocabulary/framework only. No `correct_work_if_wrong` was recorded (the right work is already co-cited).

### 2. `asparouhovRobustChiSquare2006` — S5/S5-P6 (load-bearing)

- Verdict: **partial (first pass) -> partial (independent)**. FINAL: **partial**.
- Confidence (first pass): medium. Independently verified: yes.

Claim:

> By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006] referred to $\chi^2_1$.

Evidence passage (first pass):

> $$\bar{T}=\frac{d}{\operatorname{tr}(M)} T$$ ... The distribution of $\bar{T}$ is approximately a chi-square distribution with $d^{\prime}$ degrees of freedom where $d^{\prime}$ is the integer nearest to $$\frac{(\operatorname{tr}(M))^{2}}{\operatorname{tr}\left(M^{2}\right)}$$

Evidence passage (independent):

> $$\bar{T}=\frac{d}{\operatorname{tr}(M)} T$$ ... "The distribution of $\bar{T}$ is approximately a chi-square distribution with $d^{\prime}$ degrees of freedom where $d^{\prime}$ is the integer nearest to $\frac{(\operatorname{tr}(M))^{2}}{\operatorname{tr}\left(M^{2}\right)}$" (with title/Sec.1: "mean and variance adjusted test statistics" / "mean and variance adjusted chi-square statistics")

First-pass rationale (partial): This source supports part of the claim but not the load-bearing descriptor. It does establish a robust scaled chi-square difference statistic for a single tested direction referred to chi-square: for a 1-df difference (d = d1 - d0 = 1) the rank-1 matrix M gives d' = lambda^2/lambda^2 = 1, so T-bar is referred to chi^2_1 -- consistent with 'referred to $\chi^2_1$.' However, the method described here is scale + DEGREES-OF-FREEDOM adjustment (Satterthwaite-type), NOT a 'scaled-AND-shifted' statistic. There is no additive shift term anywhere in the note; for the 1-df case the statistic reduces to pure scaling (d'=d=1), so a shift is not even present. 'Scaled-and-shifted' is a distinct, later named robust statistic (scale + additive shift with the nominal df held fixed), which this 2006 DIFFTEST webnote does not describe. So the source backs the 'robust difference statistic referred to chi^2_1' content but contradicts/does not support the specific 'scaled-and-shifted' mechanism; a literal scaled-and-shifted attribution would need a different Asparouhov-Muthen reference. Flagged per the special note that this S5 attachment was newly added.

Independent (verifier) rationale (partial): The claim attributes a "scaled-and-shifted statistic referred to chi^2_1" jointly to @satorraEnsuringPositivenessScaled2010 and this source. This source (Asparouhov & Muthen 2006, Mplus Web Note 10) describes a DIFFERENT, sibling statistic: the title and Sec.1 call it the "mean and variance adjusted" test statistic, and the actual adjustment is a PURE SCALING with ESTIMATED (Satterthwaite) degrees of freedom, not a scale-plus-shift with fixed/original df. The statistic is T-bar = (d/tr(M))*T (scale only, no additive shift constant), referred to "a chi-square distribution with d' degrees of freedom where d' is the integer nearest to (tr M)^2/tr(M^2)" (estimated df, generally not 1). Thus the two specific qualifiers in the claim are not established here: (1) "shifted" -- the webnote has no shift term; the scaled-and-shifted (T_ss = aT + b, original df) form is the Satorra-Bentler 2010 object, properly carried by the co-cited reference, not by this webnote; (2) "referred to chi^2_1" -- the webnote refers to chi^2_{d'} with re-estimated df, not to chi^2 with a preserved df=1. What IS supported: the source is squarely in the right family -- a robust, scaled chi-square difference statistic for nested SEM models referred to a chi-square distribution -- so it is a legitimate on-topic companion/implementation citation for the "Satorra-Bentler arm." Part of the compound claim is backed (robust scaled difference statistic referred to chi-square); the precise form named ("scaled-and-shifted", chi^2_1) is not, and is in fact a technically distinct variant from what this source describes. Hence partial rather than supports/misattributed.

Edit-decision note: no `correct_work_if_wrong` recorded. The descriptor "scaled-and-shifted" is the sticking point on both S5/S5-P6 references; see the shared note under item 3.

### 3. `satorraEnsuringPositivenessScaled2010` — S5/S5-P6 (load-bearing)

- Verdict: **partial (first pass) -> partial (independent)**. FINAL: **partial**.
- Confidence (first pass): medium. Independently verified: yes.

Claim:

> By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006] referred to chi^2_1.

Evidence passage (first pass):

> we can compute the proposed new SB corrected chi-square statistic as $$\bar{T}_{d}=\bar{T}_{d}^{(10)}=\left(T_{0}-T_{1}\right) / \hat{c}_{d}^{(10)}=(139.495-107.398) / 1.10=29.179$$ which can be referred to a $\chi_{1}^{2}$ variate for evaluation.

Evidence passage (independent):

> "...we can compute the proposed new SB corrected chi-square statistic as $\bar{T}_{d}=\bar{T}_{d}^{(10)}=(T_{0}-T_{1})/\hat{c}_{d}^{(10)}=(139.495-107.398)/1.10=29.179$ which can be referred to a $\chi_{1}^{2}$ variate for evaluation." [supports scaled + chi^2_1] // Footnote 2: "Satorra (2000) provides also Monte Carlo evidence...of the superiority of the scaling correction over other alternatives such as the adjusted (mean and variance corrected) statistic." [shows the mean-and-variance 'shifted' statistic is a rival, not what this paper applies]

First-pass rationale (partial): Special-note attachment, scrutinized hardest. This source supports two of the three components: the statistic is SCALED (a pure division T_d / c_hat_d, here divided by 1.10) and it is explicitly 'referred to a chi-square_1 variate.' But it does NOT support 'shifted': the paper's statistic has no additive shift anywhere — it is a scaled (mean-only) difference statistic. Footnote 2 distinguishes 'the scaling correction' from 'the adjusted (mean and variance corrected) statistic,' the latter being only a competing alternative, not this paper's method. The 'scaled-AND-shifted' (mean-and-variance) form is the contribution of the co-cited @asparouhovRobustChiSquare2006, not of this Satorra-Bentler 2010 note. So this source backs the 'scaled ... referred to chi-square_1' portion of the claim, while the 'shifted' descriptor is carried by the co-citation.

Independent (verifier) rationale (partial): The claim's compound predicate ("scaled-and-shifted statistic ... referred to chi^2_1") is only partly established by this source. SUPPORTED: the paper is entirely about a SCALED difference chi-square statistic of the form T_d/c_d, and the worked 1-df illustration explicitly states the result "can be referred to a chi^2_1 variate for evaluation" (line 177). So "scaled ... referred to chi^2_1" is fully backed. NOT SUPPORTED: the "shifted" qualifier. Every statistic in this paper is a pure multiplicative scaling (mean) correction with no additive shift term; the title is "Ensuring Positiveness of the SCALED Difference Chi-square Test Statistic." The mean-and-variance-adjusted (i.e., scaled-and-shifted, second-order) statistic appears only in footnote 2, where it is named as a RIVAL alternative the paper's scaling correction is claimed to beat ("the superiority of the scaling correction over other alternatives such as the adjusted (mean and variance corrected) statistic"). In SEM terms, scaled (T/c) and scaled-and-shifted (aT+b) are technically distinct corrections; this paper is the former and explicitly distinguishes itself from the latter. Because this is a joint citation, the "shifted" component may be intended to rest on the Asparouhov co-citation, but as to THIS source the "shifted" descriptor is unsupported and mildly contradicted, while the scaled/chi^2_1 core is strongly supported — hence partial.

Edit-decision note (shared with item 2): both S5/S5-P6 references back "scaled ... referred to chi^2_1" but neither backs "shifted." Satorra-Bentler (2010) is a pure scaling (mean-only) correction that explicitly distinguishes itself from the mean-and-variance ("adjusted") statistic; Asparouhov-Muthen (2006) is the mean-and-variance ("adjusted") statistic but implemented as scale + estimated (Satterthwaite) df, not as scale + additive shift. So as written, neither co-citation supplies a literal "scaled-AND-shifted" (a·T + b, df held fixed) statistic. The fix is to drop "shifted" (call it the scaled SB difference statistic) or substitute a reference that actually describes the additive-shift form. No `correct_work_if_wrong` was recorded for either reference.

## Disagreements (first-pass vs independent)

One attachment changed verdict between the first pass and the independent verification.

| Source | Tag | First-pass | Independent (final) | Whom to trust per the evidence |
|---|---|---|---|---|
| `mengMultipleImputationInferencesUncongenial1994a` | S2/S2-P7 | partial | misattributed | Independent (`misattributed`). The cited Meng line states only the REVERSE non-implication ("a model can be second-moment proper but still uncongenial"); Meng never states "congeniality implies properness" and never invokes the MLE. The directional implication and MLE framing are carried by the co-cited Nielsen (2003), not Meng — so the implication is misattributed to Meng, not merely partially supported by it. |

## Identity confirmations

Every source resolves to the correct real work: **35 / 35 OK**. Two citekeys are odd (Zotero numeric-style rather than the usual BBT `firstauthorShortTitleYEAR`) and are called out explicitly below; both resolve correctly.

- `chanGeneralFeasibleTests2022` — OK — Single-author Kin Wai Chan, "General and Feasible Tests with Multiply-Imputed Datasets," The Annals of Statistics 2022, vol. 50(2), DOI 10.1214/21-AOS2132. This is the AoS "stacked multiple imputation" (SMI) paper that drops EOMI/EFMI and uses a Monte Carlo reference null distribution over the full OMI eigenvalue spectrum. Correctly distinct from the Stat Sinica Chan & Meng work, which the paper itself cites as a predecessor "Chan and Meng (2021+)" that "assumes equal OMI and is restricted to LR tests" (line 128). Identity check passes.
- `mengMultipleImputationInferencesUncongenial1994a` — OK — Source resolves correctly. YAML + title block: Meng, Xiao-Li (1994), "Multiple-Imputation Inferences with Uncongenial Sources of Input," Statistical Science, vol. 9, issue 4, DOI 10.1214/ss/1177010269. This is the canonical congeniality paper; keywords include "Congeniality, self-efficiency." Author affiliation given as Assistant Professor, Department of Statistics, University of Chicago.
- `chanMultipleImprovementsMultiple2022` — OK — Frontmatter and title confirm: "Multiple Improvements of Multiple Imputation Likelihood Ratio Tests," Kin Wai Chan (CUHK) and Xiao-Li Meng (Harvard), 2022, Statistica Sinica, DOI 10.5705/ss.202019.0314. Matches the task's special note (Statistica Sinica 2022; stacked-data LRT; EFMI; maximize-the-average). This is the Stat Sinica Chan-Meng paper, correctly distinct from the AoS "general feasible tests" Chan paper (chanGeneralFeasibleTests2022).
- `rubinMultipleImputationNonresponse1987` — OK — Frontmatter and title pages confirm: Donald B. Rubin, "Multiple Imputation for Nonresponse in Surveys," John Wiley & Sons, 1987 (Wiley Series in Probability and Mathematical Statistics; ISBN 0-471-08705-X). This is the canonical MI monograph and is the correct work for the citekey.
- `shimodairaInformationCriterionModel2017` — OK — Title "An Information Criterion for Model Selection with Missing Data via Complete-Data Divergence", by Hidetoshi Shimodaira and Haruyoshi Maeda, Annals of the Institute of Statistical Mathematics 70(2):421-438, DOI 10.1007/s10463-016-0592-7 (received 2015, revised 2016, published online 21 Jan 2017; frontmatter year field 2018 reflects the print issue). Citekey resolves to the correct real work.
- `cavanaughAkaikeInformationCriterion1998a` — OK — Cavanaugh, Joseph E. and Shumway, Robert H. (1998), "An Akaike Information Criterion for Model Selection in the Presence of Incomplete Data," Journal of Statistical Planning and Inference 67(1):45-65. Confirmed correct work. Introduces AICcd ('cd' = complete data), an AIC variant estimating the expected complete-data Kullback-Leibler discrepancy, derived from deterministic EM/SEM machinery with the EM-based observed-data MLE plugged in — the parallel/precedent line the special note flags, distinct from this paper's congenial-MI target.
- `consentinoclaeskensOrderSelectionTests2010` — OK — Title "Order selection tests with multiply imputed data"; authors Fabrizio Consentino and Gerda Claeskens (ORSTAT/Leuven Statistics Research Center, K.U. Leuven); year 2010; venue Computational Statistics & Data Analysis 54(10):2284-2295; doi 10.1016/j.csda.2010.04.009. This is the MI order-selection / averaged-criterion proposal (Meng-Rubin combined statistic + standard penalty), distinct from the 2008 missing-covariate paper, exactly as the special note requires.
- `mengPerformingLikelihoodRatio1992b` — OK — Source front matter and title page confirm: Meng, Xiao-Li and Rubin, Donald B. (1992), "Performing Likelihood Ratio Tests with Multiply-Imputed Data Sets," Biometrika, Vol. 79, No. 1, pp. 103-111, DOI 10.1093/biomet/79.1.103 (JSTOR 2337151). The citekey resolves exactly to this work; the "b" is a Better BibTeX disambiguation suffix.
- `asparouhovRobustChiSquare2006` — OK — Asparouhov, T. & Muthén, B. (2006), "Robust Chi Square Difference Testing with Mean and Variance Adjusted Test Statistics," Mplus Web Notes No. 10 (dated May 26, 2006). YAML frontmatter and title heading both confirm this. It documents the Mplus DIFFTEST command for nested SEM chi-square difference testing under WLSMV/MLMV. Matches the citekey.
- `kenwardLikelihoodBasedFrequentist1998` — OK — Source frontmatter and title page confirm: M. G. Kenward and G. Molenberghs, "Likelihood Based Frequentist Inference When Data Are Missing at Random," Statistical Science, Vol. 13, No. 3 (Aug. 1998), pp. 236-247, Institute of Mathematical Statistics. Citekey resolves correctly to the K&M 1998 Statistical Science paper.
- `nielsenProperImproperMultiple2003` — OK — Frontmatter and header confirm: Søren Feodor Nielsen (2003), "Proper and Improper Multiple Imputation," International Statistical Review 71(3):593–607, DOI 10.1111/j.1751-5823.2003.tb00214.x. Citekey nielsenProperImproperMultiple2003 resolves exactly (author=nielsen, ProperImproperMultiple, year=2003).
- `rubinInferenceMissingData1976b` — OK — Rubin, Donald B. (1976), "Inference and Missing Data," Biometrika, Vol. 63, No. 3, pp. 581-592, doi:10.1093/biomet/63.3.581 (Oxford University Press / Biometrika Trust). The markdown also includes R. J. A. Little's published comments and Rubin's reply. This is the canonical foundational paper on ignorability of the missing-data mechanism; the citekey resolves to the correct real work.
- `satorraEnsuringPositivenessScaled2010` — OK — Satorra, Albert & Bentler, Peter M. (2010), "Ensuring Positiveness of the Scaled Difference Chi-square Test Statistic," Psychometrika 75(2):243-248, doi:10.1007/s11336-009-9135-y. A short note that uses the implicit function theorem to develop a guaranteed-positive computation of the Satorra-Bentler scaled chi-square DIFFERENCE test statistic for SEM/moment structures. Citekey resolves correctly.
- `claeskensconsentinoVariableSelectionIncomplete2008` — OK — Source is Claeskens, Gerda and Consentino, Fabrizio (2008), "Variable Selection with Incomplete Covariate Data," Biometrics 64(4):1062-1069, DOI 10.1111/j.1541-0420.2008.01003.x (K.U. Leuven). This is the missing-COVARIATE selection paper (response fully observed, some covariates incomplete), explicitly distinct from the 2010 order-selection work flagged in the task note. Citekey resolves to the correct real work.
- `daviesAlgorithm155Distribution1980` — OK — Davies, Robert B. (1980), "Algorithm AS 155: The Distribution of a Linear Combination of $\chi^2$ Random Variables," Applied Statistics (Journal of the Royal Statistical Society, Series C), Vol. 29, No. 3, pp. 323-333. Confirmed by both YAML frontmatter and article header/source line in the markdown. Correctly identified canonical AS 155 algorithm (Algol 60).
- `hensModelSelectionIncomplete2006a` — OK — Title "Model Selection for Incomplete and Design-Based Samples"; authors Hens, N., Aerts, M., Molenberghs, G.; 2006; Statistics in Medicine, vol 25, issue 14, pp 2502-2520; doi 10.1002/sim.2559. Citekey hensModelSelectionIncomplete2006a resolves correctly to this work.
- `imhofComputingDistributionQuadratic1961` — OK — Imhof, J. P. (Jean-Pierre Imhof), "Computing the Distribution of Quadratic Forms in Normal Variables," Biometrika 1961, vol. 48, no. 3-4, pp. 419-426, doi:10.1093/biomet/48.3-4.419 (University of Geneva). Title, author, year, and venue in the source markdown match the citekey exactly.
- `kolenTestEquatingScaling2014` — OK — Kolen, Michael J. and Brennan, Robert L. (2014). "Test Equating, Scaling, and Linking: Methods and Practices", Third Edition. Springer (Statistics for Social and Behavioral Sciences series). ISBN 978-1-4939-0316-0; DOI 10.1007/978-1-4939-0317-7. Identity confirmed from the YAML frontmatter and title pages (lines 1-50). Correct, real work.
- `vuongLikelihoodRatioTests1989` — OK — Verified from source YAML and title pages: Quang H. Vuong (1989), "Likelihood Ratio Tests for Model Selection and Non-Nested Hypotheses," Econometrica, Vol. 57, No. 2 (Mar. 1989), pp. 307-333, The Econometric Society (JSTOR 1912557, doi 10.2307/1912557). This is the canonical Vuong non-nested model-selection LRT paper; citekey resolves correctly.
- `weiMonteCarloImplementation1990` — OK — Source frontmatter and body both confirm: Greg C. G. Wei and Martin A. Tanner (1990), "A Monte Carlo Implementation of the EM Algorithm and the Poor Man's Data Augmentation Algorithms," Journal of the American Statistical Association, Vol. 85, No. 411 (Sep. 1990), pp. 699-704; DOI 10.1080/01621459.1990.10474930. This is the canonical MCEM paper and the correct work for the cited claim.
- `woodburyMissingInformationPrinciple1972` — OK — Title "A Missing Information Principle: Theory and Applications"; authors Terence Orchard and Max A. Woodbury (Duke University Medical Center); year 1972; frontmatter item_type techreport (the Berkeley-Symposium proceedings paper). NOTE: the citekey uses the SECOND author's surname (Woodbury); the first author is Orchard. Despite the naming quirk, the markdown is the canonical missing-information-principle paper and is the correct target for the cited decomposition.
- **`Meng01121991` (odd Zotero-style citekey)** — OK — Confirmed correct work. Frontmatter and JSTOR header give: Xiao-Li Meng and Donald B. Rubin (1991), "Using EM to Obtain Asymptotic Variance-Covariance Matrices: The SEM Algorithm," Journal of the American Statistical Association, Vol. 86, No. 416 (Dec. 1991), pp. 899-909, DOI 10.1080/01621459.1991.10475130. The Zotero-style citekey Meng01121991 resolves to the expected Meng & Rubin 1991 SEM paper containing the score/information decomposition, as flagged in the task identity check.
- `dempsterMaximumLikelihoodIncomplete1977a` — OK — Source is Dempster, A. P.; Laird, N. M.; Rubin, D. B. (1977), "Maximum Likelihood from Incomplete Data via the EM Algorithm," Journal of the Royal Statistical Society Series B, vol. 39, issue 1, pp. 1-22 (DOI 10.1111/j.2517-6161.1977.tb01600.x). This is the canonical DLR EM-algorithm paper. Title/authors/year/venue all visible in the YAML frontmatter and on the title line. Correct work.
- `endersMissingDataUpdate2025` — OK — Source frontmatter and body confirm: Enders, Craig K. (2025), "Missing Data: An Update on the State of the Art," Psychological Methods, vol. 30, issue 2, pp. 322-339, DOI 10.1037/met0000563. Single-author review (UCLA). Explicitly framed as the 20th-anniversary update of Schafer & Graham (2002, "Missing data: Our view of the state of the art"), cataloging two decades of missing-data methodology. Citekey resolves to the correct work.
- `schaferAnalysisIncompleteMultivariate1997` — OK — Source frontmatter and title page confirm: Schafer, J. L. (1997), "Analysis of Incomplete Multivariate Data," Chapman & Hall/CRC (1st ed., 1997; ISBN 0-412-04061-1 / 978-1-4398-2186-2), Department of Statistics, The Pennsylvania State University. item_type: book. Citekey resolves to the correct real work.
- `shimodairahidetoshiImprovingPredictiveInference2000` — OK — Source is Hidetoshi Shimodaira (2000), "Improving predictive inference under covariate shift by weighting the log-likelihood function," Journal of Statistical Planning and Inference, vol. 90(2), pp. 227-244, doi 10.1016/s0378-3758(00)00115-4. Title, single author (Shimodaira, Hidetoshi), year, and venue all match the citekey exactly. resolves_to_correct_work = true.
- `woodHowShouldVariable2008a` — OK — Source frontmatter and title block identify the work as Wood, Angela M.; White, Ian R.; Royston, Patrick (2008), "How should variable selection be performed with multiply imputed data?", Statistics in Medicine 27(17):3227-3246, doi:10.1002/sim.3177. This matches the citekey @woodHowShouldVariable2008a exactly.
- **`Tierney01031986` (odd Zotero-style citekey)** — OK — Source is Tierney, Luke and Kadane, Joseph B. (1986), "Accurate Approximations for Posterior Moments and Marginal Densities," Journal of the American Statistical Association, Vol. 81, No. 393 (Mar. 1986), pp. 82-86 (DOI 10.1080/01621459.1986.10478240). This matches the expected Tierney & Kadane 1986 Laplace-approximation paper. Despite the Zotero-style citekey (Tierney01031986), it resolves to the correct real work.
- `akaikeNewLookStatistical1974a` — OK — Frontmatter and body both confirm: "A New Look at the Statistical Model Identification," HIROTUGU AKAIKE, 1974, IEEE Transactions on Automatic Control, vol. 19, issue 6, pp. 716-723, DOI 10.1109/TAC.1974.1100705. Citekey akaikeNewLookStatistical1974a correctly resolves to the canonical Akaike AIC paper. Note: the markdown file also contains a trailing OCR of a separate paper, Parzen, "Some Recent Advances in Time Series Modeling" (next article in the same IEEE issue); it is appended noise, not the cited work, and does not affect the identity.
- `honakerAmeliaIIProgram2011` — OK — Source is "Amelia II: A Program for Missing Data" by James Honaker, Gary King, and Matthew Blackwell (2011), Journal of Statistical Software, vol. 45, issue 7, DOI 10.18637/jss.v045.i07. This matches the citekey honakerAmeliaIIProgram2011 exactly (correct authors, year, title, venue).
- `schaferMissingDataOur2002a` — OK — Schafer, Joseph L. and Graham, John W. (2002). "Missing Data: Our View of the State of the Art." Psychological Methods, 7(2), 147-177. doi:10.1037/1082-989X.7.2.147. Front-matter and article title in the source confirm the citekey resolves to the correct work — the canonical "state of the art" review of missing-data methodology.
- `schomakerModelSelectionModel2014a` — OK — Schomaker, Michael and Heumann, Christian (2014). "Model Selection and Model Averaging after Multiple Imputation." Computational Statistics & Data Analysis, vol. 71, pp. 758–770. DOI 10.1016/j.csda.2013.02.017. Frontmatter and title header match the citekey exactly.
- `vaartAsymptoticStatistics1998a` — OK — Source frontmatter and title pages confirm: "Asymptotic Statistics" by A.W. van der Vaart (1998), Cambridge University Press (Cambridge Series in Statistical and Probabilistic Mathematics), DOI 10.1017/CBO9780511802256. This is the canonical graduate textbook on asymptotic statistics. Matches the citekey/year/venue exactly.
- `vanbuurenFlexibleImputationMissing2018a` — OK — Confirmed correct work. Frontmatter and body identify it as "Flexible Imputation of Missing Data, Second Edition" by Stef Van Buuren, 2018, Chapman and Hall/CRC (DOI 10.1201/9780429492259; ISBN 978-0-429-49225-9). This is the standard practitioner book-length treatment of multiple imputation; Van Buuren is the author of the mice R package (the book serves as "an extended tutorial on the practical application of mice"). The markdown is a partial extraction: frontmatter states chapters_included = '1 (Introduction), 5 (Analysis of imputed data)', with remaining chapters available at the source repo.
- `wilksLargeSampleDistributionLikelihood1938a` — OK — Source is Wilks, S. S. (1938), "The Large-Sample Distribution of the Likelihood Ratio for Testing Composite Hypotheses," The Annals of Mathematical Statistics, vol. 9, issue 1, pp. 60–62 (DOI 10.1214/aoms/1177732360). This is the canonical Wilks' theorem paper; the citekey resolves correctly.

## Full verdict map

Per source, ordered load-bearing first. Non-`supports` verdicts are bolded.

### Load-bearing sources

#### `chanGeneralFeasibleTests2022`

Chan (2022, AoS) proposes a general, feasible MI testing procedure (SMI) that performs Wald, LR, and Rao score tests with a unified algorithm requiring only the complete-data testing device d(·). It derives the limiting null distribution D of MI test statistics as a function of the odds-of-missing-information eigenvalues r_j = f_j/(1−f_j) of F = I_mis·I_com^{-1}; under m→∞ this reduces to the weighted chi-square mixture D_∞ = (1/(k(1+μ_r)))·Σ(1+r_j)G_j, G_j~χ²₁. The proposal requires neither EOMI/EFMI nor m→∞, computes the reference via Monte Carlo (Algorithm 2.1), and is shown to control test size substantially more accurately than competitors (Fig. 2).

- S1/S1-P2: supports
- S1/S1-P5: supports
- S1/S1-P6: supports
- S2/S2-P13: supports
- S4/S4-P14: supports

#### `mengMultipleImputationInferencesUncongenial1994a`

Meng (1994) introduces and formally defines congeniality between an analyst's procedure and an imputation model (Definitions 1-2), defines "second-moment proper" imputation with respect to the analyst's complete-data procedure (Definition 3, a weaker version of Rubin 1987's proper), and defines self-efficiency (Definition 5). It analyzes the consequences of UNcongeniality for repeated-imputation inference (the Fay/Kott variance discrepancy) and gives a frequentist "Main result" on validity under separate conditions (self-efficiency, information-regularity, second-moment properness, "better" model). The paper never mentions the MLE; the only proper-vs-congenial directional statement is that a model can be second-moment proper yet still uncongenial.

- S1/S1-P6: supports
- S2/S2-P7: **misattributed**
- S2/S2-P9: supports
- S4/S4-P5: supports
- S6/S6-P1: supports

#### `chanMultipleImprovementsMultiple2022`

Chan & Meng (2022, Stat Sinica) fix four known defects of the Meng-Rubin (1992) combined MI likelihood-ratio test by switching the order of two operations in the combining rule: maximize the average of the m completed-data log-likelihoods (yielding common maximizers psi-hat* and psi-hat_0*) instead of averaging the per-imputation maximizers. The resulting statistic d_L-hat = 2{Lbar(psi-hat*) - Lbar(psi-hat_0*)} is non-negative, parametrization-invariant, and feasible from a standard complete-data LRT subroutine (stacked-data version); a new consistent FMI estimator restores monotone power, and the test is referred to an improved F reference null distribution F_{k, df-hat(r_m, h)} under EFMI. Simulations show the recommended test (LRT-3) attains accurate empirical size.

- S1/S1-P2: supports
- S1/S1-P6: supports
- S2/S2-P13: supports
- S4/S4-P9: supports

#### `rubinMultipleImputationNonresponse1987`

The foundational monograph on multiple imputation. It establishes the MI workflow (fill in missing values m times under a model, analyze each completed data set by standard complete-data methods, combine via simple rules), the exact posterior-moment identities for an estimand Q (Result 3.2: posterior mean = average of completed-data means; posterior variance = average within-imputation variance + between-imputation variance), the relative increase in variance r_inf = B/U-bar (eq. 3.1.7), and Chapter 4's randomization-validity conditions together with the formal Definition of "proper" multiple-imputation methods, illustrated by the fully normal Bayesian scheme (Example 4.2). The terms "congenial" and "self-efficiency" do not appear anywhere in the book (those are Meng 1994's).

- S1/S1-P1: supports
- S2/S2-P7: supports
- S2/S2-P8: supports
- S4/S4-P5: supports

#### `shimodairaInformationCriterionModel2017`

Shimodaira & Maeda derive AIC_{x;y}, an information criterion for model selection with missing data that is an asymptotically unbiased estimator of complete-data (rather than incomplete-data) Kullback-Leibler divergence. Relative to AIC it adds a missing-data penalty tr(I_{z|y}(theta_y) I_y(theta_y)^{-1}), i.e. tr(RIV), derived via the EM algorithm's alternating-minimization geometry under a weaker assumption than the earlier PDIO and AICcd criteria; the abstract and body state this penalty is exactly half the value of the PDIO/AICcd penalty. Section 8 names combining a missing mechanism with other sampling mechanisms as future work.

- S1/S1-P6: supports
- S2/S2-P7: supports
- S4/S4-P16: supports
- S6/S6-P6: supports

#### `cavanaughAkaikeInformationCriterion1998a`

The paper derives AICcd, an AIC variant for incomplete data that estimates the expected complete-data K-L discrepancy using only complete-data (EM/SEM) tools. Its penalty equals 2 trace{I_oc I_o^{-1}} = 2d + 2 trace{DM(I-DM)^{-1}}, where the "2 trace{DM(I-DM)^{-1}}" term is explicitly a missing-data supplement over plain AIC's 2d penalty; AICcd shares this penalty with Shimodaira's (1994) PDIO but adds a goodness-of-fit component -2H(θ̂|θ̂). The estimate θ̂ is the EM convergence point (observed-data MLE), and the whole development is deterministic EM/SEM, never stochastic/Monte-Carlo imputation.

- S1/S1-P6: supports
- S2/S2-P7: supports
- S4/S4-P16: supports

#### `consentinoclaeskensOrderSelectionTests2010`

The paper develops likelihood-based order selection (omnibus lack-of-fit) tests for multiply imputed data under MAR, using Meng-Rubin (1992) combined likelihood-ratio statistics. Section 5 additionally proposes an AIC for multiply imputed data, aic(S,S0) = D̃_S − 2 p_S, i.e., the Meng-Rubin combined statistic minus the standard two-per-parameter penalty, and benchmarks it in a simulation (Table 7) against Schomaker's averaging methods, complete-case analysis, and the original full-data analysis (AIC_orig). The authors state that the connected AIC merits further theoretical and practical investigation, which extends the scope of the current paper.

- S1/S1-P2: supports
- S1/S1-P3: supports
- S2/S2-P13: supports

#### `mengPerformingLikelihoodRatio1992b`

Meng & Rubin (1992, Biometrika) propose a likelihood-ratio-based procedure for significance testing with multiply-imputed data. They combine the m complete-data log likelihood ratio statistics across imputations into a single pooled statistic (D_L, built from the deviance evaluated at averaged parameter estimates) and refer it to an F reference distribution on k and w(r_L) degrees of freedom. The construction rests on the equal-fractions-of-missing-information assumption (inherited from the moment-based D_m, to which D_L is asymptotically equivalent) and avoids computing complete-data covariance matrices.

- S1/S1-P2: supports
- S1/S1-P6: supports
- S2/S2-P13: supports

#### `asparouhovRobustChiSquare2006`

Mplus Web Note No. 10 deriving the DIFFTEST mean-and-variance adjusted chi-square difference statistic for nested SEM models under WLSMV/MLMV. The adjusted statistic is T-bar = (d / tr(M)) T, referred to a chi-square with d' degrees of freedom where d' is the integer nearest to (tr(M))^2 / tr(M^2). Section 2 gives an algebraically equivalent cheaper formula M_1 (same tr and tr-of-square as M) avoiding the large Gamma matrix; Section 3 is a small measurement-invariance simulation. The method matches the first two moments via scaling plus a degrees-of-freedom adjustment; there is no additive shift term anywhere in the note.

- S4/S4-P20: supports
- S5/S5-P6: **partial**

#### `kenwardLikelihoodBasedFrequentist1998`

An exposition of likelihood-based frequentist inference under MAR. The paper shows the classical (naive/MCAR) expected information matrix is biased under MAR and recommends using the observed information matrix, with the "unconditional" expected information (expectation taken over the joint (Y,R) sampling distribution) as the valid theoretical alternative; the naive expected information conditioning on the realized pattern is inconsistent. In the bivariate Gaussian example (§3.2) it derives that under MAR the unconditional information carries non-zero cross-terms linking the mean and variance-covariance parameters that vanish under the naive framework, breaking mean/covariance orthogonality.

- S2/S2-P12: supports
- S4/S4-P3: supports

#### `nielsenProperImproperMultiple2003`

Nielsen develops frequentist large-sample theory for Bayesian multiple imputation and shows it is NOT generally proper. Section 2 proves Bayesian MI is proper when the complete-data estimator is the complete-data MLE; Section 3 gives counterexamples where the same Bayesian imputations are improper under inefficient (non-MLE) complete-data estimators. Section 4 restates Meng (1994)'s result that congeniality implies properness and proves (Result 1) that congeniality holds iff the complete- and observed-data estimators are efficient (maximum likelihood) with inverse-Fisher-information variance estimators.

- S2/S2-P7 (properness is not absolute): supports
- S2/S2-P7 (analyst uses complete-data MLE; congeniality ⇒ properness): supports

#### `rubinInferenceMissingData1976b`

The paper derives the weakest general conditions under which the process that causes missing data can be ignored when making inferences about the data parameter theta. It defines three conditions — missing at random (Definition 1), observed at random (Definition 2), and distinctness of the missing-data parameter phi from theta (Definition 3) — and proves that ignoring the mechanism is valid for direct-likelihood and Bayesian inference under MAR + distinctness (Theorems 7.1, 8.1), and for sampling-distribution inference under MAR + OAR (Theorem 6.1). These are stated to be the weakest simple/general conditions for which ignoring the mechanism always yields correct inferences.

- S2/S2-P3: supports
- S4/S4-P5: supports

#### `satorraEnsuringPositivenessScaled2010`

The paper develops a new hand-computable, guaranteed-positive version of the Satorra-Bentler SCALED chi-square difference statistic for nested SEM models under nonnormality. The scaled difference statistic is defined as a pure division T_d-bar = T_d / c_hat_d with scaling correction c_d = (1/m) tr{U_d Gamma} — a mean (first-moment) correction — referred to a chi-square_m reference (chi-square_1 in the worked illustration). It is explicitly a SCALED (mean-only) statistic; there is no additive shift. The "adjusted (mean and variance corrected) statistic" is mentioned only as a competing alternative (footnote 2), not as the paper's method.

- S4/S4-P20: supports
- S5/S5-P6: **partial**

#### `claeskensconsentinoVariableSelectionIncomplete2008`

The paper proposes AIC- and TIC-type model selection criteria for parametric regression (incl. GLMs, logistic) when covariates are missing (response fully observed), derived from the EM Q-function via the methods-of-weights of Ibrahim et al. The criteria are bias-corrected estimators of the expected Kullback-Leibler discrepancy K_n between the unknown true data-generating mechanism g and the (possibly misspecified) likelihood model; the headline "model-robust" version uses the Takeuchi tr{J I^{-1}} penalty (Theorem 1: E_g(K-hat_n - K_n) = tr{I^{-1} J}/n + o(1/n)), reducing to an AIC penalty only when the model is correct (I = J).

- S1/S1-P6: supports

#### `daviesAlgorithm155Distribution1980`

Davies (1980) presents Algorithm AS 155 to compute pr(Q<c) for Q = sum_j lambda_j X_j + sigma X_0, a linear combination (weighted sum) of independent non-central chi-squared variables plus an optional normal term. The algorithm computes this distribution function by numerical inversion of the characteristic function (based on Davies 1973), with explicit integration- and truncation-error bounds. It also covers any quadratic form in normal variables and ratios of quadratic forms.

- S4/S4-P20: supports

#### `hensModelSelectionIncomplete2006a`

Hens, Aerts & Molenberghs (2006, Statistics in Medicine) propose a weighted AIC (AIC_W) using inverse selection/missingness-probability weights w_i = delta_i/pi_i (Horvitz-Thompson style) to correct AIC-based model selection for incomplete (MAR) and design-based samples; the stated aim is to select the model that best describes the hypothetically complete data. The Discussion explicitly raises an "explicit imputation-based AIC" as an obvious alternative, runs only a small pilot simulation of it, and defers a detailed study to "current research."

- S1/S1-P6: supports

#### `imhofComputingDistributionQuadratic1961`

Imhof (1961) gives exact and numerical methods for the distribution P{Q>x} of a quadratic form in normal variables, written as a linear combination of independent (possibly non-central) chi-square variables Q = sum_r lambda_r * chi^2_{h_r; delta_r^2} (eq. 1.1), where the lambda_r are the weights. Section 3, "Numerical inversion of the characteristic function," derives a method that evaluates the CDF F(x) by numerically integrating the Gil-Pelaez inversion formula (3.1)/(3.2) applied to the characteristic function phi(t) of Q.

- S4/S4-P20: supports

#### `kolenTestEquatingScaling2014`

A graduate textbook on test equating. It defines equipercentile (observed-score) equating: in Section 1.3.4 "Observed Score Equating Properties" the equipercentile equating function e_Y converts Form X scores so their distribution matches Form Y; in Section 2.x it gives the closed-form continuous equating function e_Y(x) = G^{-1}[F(x)] (attributed to Braun and Holland 1982), where F and G are the CDFs of the two forms and G^{-1} is the inverse CDF.

- S4/S4-P20: supports

#### `vuongLikelihoodRatioTests1989`

Vuong (1989) develops a classical (significance-testing) approach to model selection among competing, possibly misspecified parametric models, using the Kullback-Leibler distance to the truth and working in pseudo-true values. It characterizes the asymptotic distribution of the log-likelihood-ratio statistic for nested, non-nested, and overlapping competing models. For strictly non-nested models (Theorem 5.1), the n^{-1/2}-scaled LR statistic is asymptotically N(0,1) under the equivalence null E0[log(f/g)]=0 and diverges to +/-infinity under the alternatives where one model is strictly closer to the truth.

- S4/S4-P13: supports

#### `weiMonteCarloImplementation1990`

Wei & Tanner (1990, JASA 85(411):699-704), "A Monte Carlo Implementation of the EM Algorithm and the Poor Man's Data Augmentation Algorithms." Introduces the MCEM algorithm: the E-step integral defining the Q-function is approximated by Monte Carlo, drawing latent-data samples z^(1),...,z^(m) from the conditional predictive distribution p(z|theta^(i),y) and forming the Q-function as the average of augmented log-posteriors over those draws. Also relates MCEM to data augmentation and introduces two PMDA approximations.

- S2/S2-P6: supports

#### `woodburyMissingInformationPrinciple1972`

Orchard & Woodbury (1972), "A Missing Information Principle: Theory and Applications." Establishes the missing information principle: the complete-data information J_X decomposes as J_X = J_Y + J_{X/Y}, where Y is the observable "image" of the complete data X, J_Y is the observed-data information, and J_{X/Y} is explicitly termed "the lost information." It then relates the lost information to the increase in parameter-estimate variance (the "hidden variance"), with worked examples (linear model, MVN with missing components, mixtures).

- S2/S2-P4: supports

### Background (non-load-bearing) sources

#### `Meng01121991` (odd Zotero-style citekey)

Meng & Rubin (1991) introduce the Supplemented EM (SEM) algorithm for obtaining asymptotic variance-covariance matrices from EM output. Section 2.4 derives, from the log-likelihood factorization L(theta|Y_obs)=L(theta|Y)-log f(Y_mis|Y_obs,theta), the information decomposition I_o(theta*|Y_obs)=I_oc - I_om (eq. 2.4.2), stated in words as "observed information = complete information - missing information" (the "missing information principle," whose name they attribute to Orchard and Woodbury 1972). They then state the EM rate matrix DM = I_om I_oc^{-1} (eq. 2.4.5), crediting DLR (Dempster, Laird & Rubin 1977) for showing it, and use it to write V = I_oc^{-1} + DeltaV.

- S2/S2-P4 (observed = complete − missing decomposition): supports
- S2/S2-P4 (EM rate matrix DM normalization): supports

#### `dempsterMaximumLikelihoodIncomplete1977a`

The foundational EM-algorithm paper. It defines the Q-function as the conditional expectation of the complete-data log-likelihood given the observed data (eq. at lines 252-254), establishes the monotone-likelihood / GEM convergence theory, and derives the EM rate-of-convergence matrix DM(phi*) = D^{20}H(phi*|phi*)[D^{20}Q(phi*|phi*)]^{-1}. It identifies -D^{20}H as the Fisher information in the unobserved part of x (missing information) and, via Q = L + H, -D^{20}Q as the complete-data information; the largest eigenvalue of DM gives the rate of convergence.

- S2/S2-P4 (EM rate matrix DM): supports
- S2/S2-P5 (Q-function definition): supports

#### `endersMissingDataUpdate2025`

A single-author state-of-the-art review of missing-data methodology, written as a 20-year update to Schafer & Graham (2002). It catalogs innovations across missing-data theory, factored regression, FIML, Bayesian estimation, multiple imputation, MNAR processes, composite scores, multilevel models, and software. Its inference coverage (the "Multiple Imputation Inference" section) is confined to Wald and likelihood-ratio tests, degrees-of-freedom corrections, the Chan & Meng D4 test, and SEM fit indices; it contains no treatment of information criteria, AIC/BIC, or likelihood-based model selection for multiply imputed data.

- S1/S1-P1: supports
- S1/S1-P2: supports

#### `schaferAnalysisIncompleteMultivariate1997`

Schafer's monograph on likelihood and Bayesian analysis of incomplete multivariate data under ignorability. Section 2.3 defines the observed-data likelihood as proportional to the marginal distribution of the observed data, L(theta|Y_obs) ~ P(Y_obs|theta) (eq 2.5), obtained by integrating out Y_mis; for arbitrary MVN missingness patterns it is written (eq 2.10) as a product over patterns s and rows i of each unit's observed-coordinate normal density |Sigma_s*|^(1/2) exp{...}, with y_i* the observed part of row i and mu_s*, Sigma_s* the observed-variable mean subvector / covariance submatrix; the observed-data loglikelihood is the sum of these per-pattern contributions, and theta-hat is its maximizer. Section 3 ("missing information principle") establishes I_c = I_o + I_m (Orchard-Woodbury) and the EM asymptotic rate matrix D = I_c^{-1} I_m (eq 3.21), which it names the matrix fraction of missing information.

- S4/S4-P2: supports
- S4/S4-P3: supports

#### `shimodairahidetoshiImprovingPredictiveInference2000`

Shimodaira (2000) develops the maximum weighted log-likelihood estimate (MWLE): under covariate shift (observed-covariate density q0 differs from population/target density q1) plus model misspecification, weighting the log-likelihood by w(x)=q1(x)/q0(x) is asymptotically optimal under expected Kullback-Leibler loss, with a variant of AIC (IC_w) used to select the weight at moderate sample sizes. The Section 9 "Concluding remarks" observe that information criteria must be tailored to different sampling schemes — covariate shift (this paper) versus incomplete data (Shimodaira 1994; Cavanaugh-Shumway 1998) — and leave "the unified approach for them" as future work.

- S1/S1-P6: supports
- S6/S6-P6: supports

#### `woodHowShouldVariable2008a`

A dedicated methodological study of how variable (backward-stepwise) selection should be performed with multiply imputed data. It states that no guidelines currently exist, then compares complete-case selection, repeated Rubin's rules (RR), stacked/weighted approaches, and other variants through seven simulation scenarios based on the UK700 psychiatry trial, explicitly benchmarking each selection method against model selection on the full pre-missingness data, and recommends RR because it preserves type 1 error.

- S1/S1-P2: supports
- S1/S1-P3: supports

#### `Tierney01031986` (odd Zotero-style citekey)

The paper develops Laplace-method approximations to posterior means, variances, and marginal densities of functions of a parameter, requiring only maximization of slightly modified likelihoods plus the observed information at the maxima. Its introduction explicitly frames the standard normal approximation to the posterior (a normal curve centered at the posterior mode with variance equal to minus the inverse second derivative of the log posterior) as an application of Laplace's method for integrals; the paper's own contribution is a more accurate ratio ("fully exponential") form with O(n^-2) error.

- S2/S2-P8: supports

#### `akaikeNewLookStatistical1974a`

Akaike, H. (1974), "A New Look at the Statistical Model Identification," IEEE Transactions on Automatic Control, 19(6), 716-723. Introduces AIC and the MAICE procedure: a fitted model's quality is measured by its mean (expected) log-likelihood under the true density g, S(g; f(·|θ)) = ∫ g(x) log f(x|θ) dx (Section IV, "Mean Log-Likelihood as a Measure of Fit"); -2 log(maximum likelihood) is a downward-biased plug-in estimate of -2N·E·S, and adding +2k corrects that bias, yielding AIC = (-2)log(maximum likelihood) + 2k. (A second, unrelated paper by Parzen is OCR-appended to the same markdown file but is not the cited work.)

- S2/S2-P10: supports

#### `honakerAmeliaIIProgram2011`

The paper documents the Amelia II R package for multiple imputation of missing data. Its stated method is the EMB (expectation-maximization with bootstrapping) algorithm: it runs EM on multiple bootstrapped samples of the incomplete data to draw complete-data parameters, then draws imputed values from each bootstrapped parameter set. The model assumes multivariate normality and MAR.

- S5/S5-P2: supports

#### `schaferMissingDataOur2002a`

A widely cited review article that frames the missing-data problem, dismisses older ad hoc procedures, and presents maximum likelihood (ML) and Bayesian multiple imputation (MI) as the two highly recommended, "state of the art" approaches under MAR. It explicitly characterizes these methods as vastly improved over prior practice and "becoming standard" due to software availability, while also flagging remaining misconceptions and unresolved issues (notably non-MAR/nonignorable settings).

- S1/S1-P1: supports

#### `schomakerModelSelectionModel2014a`

The paper proposes a general framework for model selection and model averaging under missing data, with multiple imputation as the missingness strategy, combined with model averaging and bootstrapping; it is evaluated via Monte Carlo simulation (linear regression) and a pulmonary-TB survival application. Its introduction explicitly states that the literature on model selection/averaging in the presence of missing data is surprisingly sparse, and that prior suggestions (Hens et al. 2006, Wood et al. 2008, May et al. 2010) do not provide a general, overall valid framework.

- S1/S1-P2: supports

#### `vaartAsymptoticStatistics1998a`

A graduate textbook covering likelihood inference, M-/Z-estimation, and asymptotic efficiency. It establishes the standard regularity conditions for asymptotic normality of the MLE/M-estimator: a smoothness condition (Theorem 5.39 "differentiable in quadratic mean" plus a Lipschitz bound on the log-density; Section 5.6 "Classical Conditions" / Theorem 5.41 requiring the criterion to be twice continuously differentiable with dominated derivatives) and a nonsingular Fisher information condition (Theorem 5.39: "If the Fisher information matrix I_{theta_0} is nonsingular"; Theorem 5.41: "the matrix P psi-dot_{theta_0} exists and is nonsingular"). These two conditions recur throughout Chapters 5, 7, 8, 10, 15, 16.

- S4/S4-P5: supports

#### `vanbuurenFlexibleImputationMissing2018a`

A partial extraction (Chapters 1 and 5) of Van Buuren's standard MI textbook. Chapter 5, "Analysis of imputed data," is the natural home for any model-selection/model-evaluation material under MI. It covers parameter pooling (Rubin's rules), multi-parameter inference via Wald (D1), combining test statistics (D2), and likelihood-ratio (D3) tests, plus "Stepwise model selection" (variable selection via majority/stack/Wald methods, Bayesian model averaging, LASSO) and "Model optimism" (bootstrap-based optimism correction). No information criterion (AIC/BIC) appears anywhere in the included text.

- S1/S1-P2: supports

#### `wilksLargeSampleDistributionLikelihood1938a`

A 3-page note deriving the asymptotic (large-sample) distribution of the likelihood-ratio statistic for testing composite hypotheses. Under the Neyman-Pearson likelihood-ratio setup with a full parameter space of dimension h and a constrained subspace fixing h-m parameters, Wilks shows via a characteristic-function argument that, when the null hypothesis H is true, -2 log lambda is distributed (except for terms of order 1/sqrt(n)) as chi-square with h-m degrees of freedom.

- S2/S2-P11: supports
