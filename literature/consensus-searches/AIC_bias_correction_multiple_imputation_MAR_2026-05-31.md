# **Akaike Information Criterion, Bias Correction, and Multiple Imputation:** Key Links

Akaike’s Information Criterion (AIC) estimates **expected out‑of‑sample (predictive) log‑likelihood** by bias‑correcting the maximized log‑likelihood. With missing data handled via multiple imputation or likelihood methods, both the AIC target and its bias correction become more delicate.

## Mechanisms: AIC, Expected Log‑Likelihood, and Bias

**AIC as bias‑corrected expected log‑likelihood**

- AIC uses the maximized log‑likelihood plus a penalty for the number of parameters to correct bias in estimating **expected log‑likelihood / Kullback–Leibler information**  (Burnham & Anderson, 2003; Cavanaugh & Neath, 2019; Gelman et al., 2013).  
- Bias arises because the same data are used both to fit and to evaluate the model; the penalty term aims to cancel this optimism  (Beesley et al., 2021; Bengtsson & Cavanaugh, 2006; Gelman et al., 2013).  

**Bias corrections and refinements**

- Higher‑order bias corrections to AIC are derived via expansions in log‑likelihood derivatives, giving improved approximations when asymptotic assumptions are weak  (Ogasawara, 2016).  
- For linear mixed‑effects models, marginal AIC can be **positively biased** for −2×expected log‑likelihood when random‑effect structures are over‑specified; Monte‑Carlo‑based bias‑reduced AIC variants reduce this bias and wrong selection of smaller models  (Beesley et al., 2021).  
- Similar bias‑corrected AIC forms are developed for factor analysis and multinomial logistic regression, improving model selection performance over crude AIC  (Ogasawara, 2016; Yanagihara et al., 2012).  

### Different Bias Corrections and Their Targets

| Setting / method                         | Target quantity                          | Bias issue & correction                     | Citations |
|-----------------------------------------|------------------------------------------|---------------------------------------------|-----------|
| Classical AIC                           | Expected log‑likelihood / KL divergence  | k‑penalty corrects first‑order bias         |  (Burnham & Anderson, 2003; Cavanaugh & Neath, 2019; Gelman et al., 2013)|
| LME marginal AIC                        | −2×expected log‑likelihood               | Positive bias when random effects overfit   |  (Beesley et al., 2021)|
| State‑space AICi                        | KL info between fitted and true models   | Monte‑Carlo adjustment reduces bias         |  (Bengtsson & Cavanaugh, 2006)|
| Factor / multinomial models             | Same as AIC                              | Higher‑order analytic bias corrections      |  (Ogasawara, 2016; Yanagihara et al., 2012; Ogasawara, 2016)|

**Figure 1:** Targets and bias corrections for AIC variants

## Multiple Imputation, Missing at Random, and AIC/BIC

**Using AIC/BIC to choose imputation models**

- Multiple imputation (MI) can be viewed as a stochastic EM approximation to the likelihood, so **standard likelihood‑based criteria (AIC, BIC)** can be applied to select the imputation model  (Noghrehchi et al., 2021; Chaurasia & Harel, 2012).  
- Poor or overly complex imputation models can **bias parameter estimates**; simulation shows that model selection via AIC/BIC reduces bias and inefficiency, and BIC can be consistent even with missing not at random mechanisms  (Noghrehchi et al., 2021).  
- AIC‑based selection rules have been adapted for multiply imputed regression, by combining AIC values across imputations (e.g., via arithmetic or geometric means) to choose among candidate models  (Chaurasia & Harel, 2012).  

**Effect of imputation method on AIC/BIC accuracy**

- When missingness is small (≈10%), AIC and BIC are most accurate if missing data are handled by full information maximum likelihood; EM can yield the least accurate criteria  (Montshiwa et al., 2018).  
- At higher missingness, MI algorithms (FCS, MCMC) improve AIC/BIC accuracy relative to some ML methods  (Montshiwa et al., 2018).  
- Model averaging and AIC‑based inference are sensitive to missing data; MI can recover accurate AIC values and Akaike weights compared with complete‑case analysis  (Nakagawa & Freckleton, 2010).  

## Missingness Mechanisms and Model‑Selection Implications

- Many MI implementations assume **missing at random (MAR)**; misspecified imputation under MAR or MNAR can still bias analysis, underscoring the need for careful model choice and sensitivity analysis  (Susko & Roger, 2020; Jakobsen et al., 2017; Madley-Dowd et al., 2019; Pedersen et al., 2017).  
- Modified MI procedures including missingness indicators or offsets can substantially **reduce bias under MNAR** compared to standard MI  (Susko & Roger, 2020).  
- Even with large proportions of missingness, valid MI under MAR reduces bias versus complete‑case analysis; efficiency is better described by the **fraction of missing information** than by simple missingness proportion  (Madley-Dowd et al., 2019).  

## Summary

AIC is fundamentally a **bias‑corrected estimator of expected log‑likelihood / KL divergence**, and numerous refinements adjust this bias in complex or small‑sample settings. When data are incomplete, using MI or maximum likelihood together with AIC/BIC requires attention to the imputation model: both under‑ and over‑fitting of the imputation model can bias downstream inference, but AIC/BIC applied correctly to the observed‑data likelihood or MI‑based likelihood approximations can help select better models. Bias‑corrected or specialized AIC variants further improve estimation of expected log‑likelihood in mixed, state‑space, and multivariate models.
 
_These search results were found and analyzed using Consensus, an AI-powered search engine for research. Try it at https://consensus.app. © 2026 Consensus NLP, Inc. Personal, non-commercial use only; redistribution requires copyright holders’ consent._
 
## References
 
Beesley, L., Bondarenko, I., Elliot, M., Kurian, A., Katz, S., & Taylor, J. (2021). Multiple imputation with missing data indicators. *Statistical Methods in Medical Research, 30*, 2685 - 2700. https://doi.org/10.1177/09622802211047346
 
Bengtsson, T., & Cavanaugh, J. (2006). An improved Akaike information criterion for state-space model selection. *Comput. Stat. Data Anal., 50*, 2635-2654. https://doi.org/10.1016/j.csda.2005.05.003
 
Burnham, K., & Anderson, D. (2003). Model selection and multimodel inference : a practical information-theoretic approach. *Journal of Wildlife Management, 67*, 655. https://doi.org/10.2307/3802723
 
Cavanaugh, J., & Neath, A. (2019). The Akaike information criterion: Background, derivation, properties, application, interpretation, and refinements. *Wiley Interdisciplinary Reviews: Computational Statistics, 11*. https://doi.org/10.1002/wics.1460
 
Chaurasia, A., & Harel, O. (2012). Using AIC in multiple linear regression framework with multiply imputed data. *Health Services and Outcomes Research Methodology, 12*, 219-233. https://doi.org/10.1007/s10742-012-0088-8
 
Gelman, A., Hwang, J., & Vehtari, A. (2013). Understanding predictive information criteria for Bayesian models. *Statistics and Computing, 24*, 997 - 1016. https://doi.org/10.1007/s11222-013-9416-2
 
Jakobsen, J., Gluud, C., Wetterslev, J., & Winkel, P. (2017). When and how should multiple imputation be used for handling missing data in randomised clinical trials – a practical guide with flowcharts. *BMC Medical Research Methodology, 17*. https://doi.org/10.1186/s12874-017-0442-1
 
Madley-Dowd, P., Hughes, R., Tilling, K., & Heron, J. (2019). The proportion of missing data should not be used to guide decisions on multiple imputation. *Journal of Clinical Epidemiology, 110*, 63 - 73. https://doi.org/10.1016/j.jclinepi.2019.02.016
 
Montshiwa, T., Moroke, N., & Munapo, E. (2018). The efficiency of multiple imputation and maximum likelihood methods for estimating missing values. *Indian journal of science and technology, 11*, 1-11. https://doi.org/10.17485/ijst/2018/v11i16/118701
 
Nakagawa, S., & Freckleton, R. (2010). Model averaging, missing data and multiple imputation: a case study for behavioural ecology. *Behavioral Ecology and Sociobiology, 65*, 103-116. https://doi.org/10.1007/s00265-010-1044-7
 
Noghrehchi, F., Stoklosa, J., Penev, S., & Warton, D. (2021). Selecting the model for multiple imputation of missing data: Just use an IC!. *Statistics in Medicine, 40*, 2467 - 2497. https://doi.org/10.1002/sim.8915
 
Ogasawara, H. (2016). Bias correction of the Akaike information criterion in factor analysis. *J. Multivar. Anal., 149*, 144-159. https://doi.org/10.1016/j.jmva.2016.04.003
 
Ogasawara, H. (2016). Asymptotic cumulants of some information criteria. *Journal of the Japanese Society of Computational Statistics, 170*, 1-41. https://doi.org/10.5183/jjscs.1512001_225
 
Pedersen, A., Mikkelsen, E., Cronin-Fenton, D., Kristensen, N., Pham, T., Pedersen, L., & Petersen, I. (2017). Missing data and multiple imputation in clinical epidemiological research. *Clinical Epidemiology, 9*, 157 - 166. https://doi.org/10.2147/clep.s129785
 
Susko, E., & Roger, A. (2020). On the Use of Information Criteria for Model Selection in Phylogenetics.. *Molecular biology and evolution*. https://doi.org/10.1093/molbev/msz228
 
Yanagihara, H., Kamo, K., Imori, S., & Satoh, K. (2012). Bias-corrected AIC for selecting variables in multinomial logistic regression models☆. *Linear Algebra and its Applications, 436*, 4329-4341. https://doi.org/10.1016/j.laa.2012.01.018
