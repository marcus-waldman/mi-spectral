---
citekey: hensModelSelectionIncomplete2006a
item_type: article
authors: 'Hens, N. and Aerts, M. and Molenberghs, G.'
year: 2006
title: Model Selection for Incomplete and Design-Based Samples
venue: Statistics in Medicine
volume: 25
issue: 14
pages: 2502--2520
doi: 10.1002/sim.2559
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\hens_model_selection_incomplete_2006.pdf'
pdf_sha256: b71bc04fc8834759868993833d6a0c923fb38781c16742e9bb80ddb4c6462602
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T15:21:35Z
---
# Model selection for incomplete and design-based samples 

N. Hens ${ }^{*, \dagger}$, M. Aerts and G. Molenberghs<br>Center for Statistics, Universiteit Hasselt, Campus Diepenbeek, Agoralaan-Gebouw D, B-3590 Diepenbeek, Belgium


#### Abstract

SUMMARY The Akaike information criterion, AIC, is one of the most frequently used methods to select one or a few good, optimal regression models from a set of candidate models. In case the sample is incomplete, the naive use of this criterion on the so-called complete cases can lead to the selection of poor or inappropriate models. A similar problem occurs when a sample based on a design with unequal selection probabilities, is treated as a simple random sample. In this paper, we consider a modification of AIC, based on reweighing the sample in analogy with the weighted Horvitz-Thompson estimates. It is shown that this weighted AIC-criterion provides better model choices for both incomplete and design-based samples. The use of the weighted AIC-criterion is illustrated on data from the Belgian Health Interview Survey, which motivated this research. Simulations show its performance in a variety of settings. Copyright © 2006 John Wiley \& Sons, Ltd.


KEY WORDS: missing data; weighted likelihood; model selection; complex designs; Akaike information criterion

## 1. INTRODUCTION

In a regression analysis, starting from a rich enough family of models and based on the data at hand, one or a few good models can be selected, e.g. using the Akaike information criterion (AIC). In case of missing data, simple deletion of the subsample of incomplete observations and treating the resulting subsample of so-called complete cases (CC) as a simple random sample has been shown to possibly lead to biased estimates, even when using a correct model (see References [1,2]). A similar problem occurs when the observations come from a complex survey design, i.e. when sampling from a finite population with unequal selection probabilities. Indeed, the probability that an observation is incomplete can also be considered

[^0]as a selection probability for that observation to be included in the sample or not. Analysing such design-based data as a simple random sample can also introduce bias [3].

There is a vast literature on parametric and nonparametric models in case of incomplete or design-based samples, but most of it concerns estimation (assuming a correct model) rather than model selection. The naive use of model selection criteria however turns out to be unreliable in case of the aforementioned complications in the data. Indeed, treating the CC or the design-based sample as just a simple random sample can invoke some effects to appear or disappear and thus suggest an other (incorrect) model to be more adequate for the data at hand.

In the context of incomplete data, selection methods like the predictive divergence for incomplete observations (PDIO, [4]) and the complete data AIC (AICcd, [5]) have been proposed. These methods rely on modelling the complete data likelihood, which introduces an additional model selection problem, namely the selection of an appropriate model for the missingness mechanism (if not missing completely at random).

In this paper, we focus on selecting appropriate models for the measurement part, while treating the missingness mechanism as a nuisance. We propose a modification of the AIC for regression models, based on reweighing the CC by their inverse selection probabilities. The latter selection probabilities, if unknown, are preferably estimated non-parametrically (using e.g. splines), in this way avoiding the selection of a parametric model with its assumptions for the missingness process. This weighing of completely observed cases can be seen as an implicit imputation of missing observations and is valid when the probability to be missing depends upon the observed values but not on the unobserved values (MAR in the terminology of Little and Rubin [6]).

For the closely related situation of design-based samples, model selection has not been really investigated. In the next section, the motivating study illustrates both complications of missingness and design-based sampling. In Section 3, the weighted AIC is introduced and discussed, mainly for parametric models, but its applicability is also extended to nonparametric models. Indeed, analogous to the selection of an optimal model from a set of parametric candidate models, one can choose the optimal smoothing parameter in nonparametric regression based on an AIC, as shown by Hurvich et al. [7]. We will modify this criterion to handle incomplete and design-based samples. An application to the cervix cancer screening data is shown in Section 4 while, in Section 5, a simulation study shows the improved performance of the modified AIC. Finally, Section 6 discusses the performance of the weighted AIC, introduces imputation-based model selection for incomplete data and possible avenues of further research.

## 2. THE BELGIAN HEALTH INTERVIEW SURVEY: CERVIX CANCER SCREENING

To outline an evidence-based health policy, one is often interested in the profiles of persons who are at risk to obtain certain diseases and do not respond to prevention programs, e.g. cervix cancer screening. In the Belgian Health Interview Survey (HIS) of 1997, one of the questions investigated is in what respect the group of women, aged $25-64$, not having a smear is different from the group of women that did have a smear taken in the past 3 years. For this purpose discrimination based on civil status (CS), drug consumption (DR), age (Age),

Table I. HIS example: the different candidate models and their (weighted) AIC values.
| Model | AIC | $\mathrm{AIC}_{W_{1}}$ | $\mathrm{AIC}_{W_{2}}$ | $\mathrm{AIC}_{W_{1}, W_{2}}$ |
| :--- | :--- | :--- | :--- | :--- |
| (1) Age + Age ${ }^{2}+\operatorname{log(DR)}+\mathrm{CS}$ | 1489.02(1) | 975.31 | 2607.11(2) | 1463.16 |
| (2) Age $+\mathrm{Age}^{2}+\log (\mathrm{DR})+\mathrm{EL}+\log (\mathrm{DR}) * \mathrm{EL}$ | 1489.68(2) | 967.13 | 2597.37(1) | 1453.83 |
| (3) Age + Age ${ }^{2}+\mathrm{DR}+\mathrm{EL}+\mathrm{DR} * \mathrm{EL}$ | 1490.70(3) | 963.26(2) | 2608.69(3) | 1451.06(3) |
| (4) Age $+\mathrm{Age}^{2}+\operatorname{log(DR)}$ | 1492.39 | 965.66(3) | 2618.32 | 1457.89 |
| (5) Age $+\mathrm{Age}^{2}+\log (\mathrm{DR})+\log ($ Age $)$ | 1494.10 | 967.60 | 2619.77 | 1459.82 |
| (6) Age $+\mathrm{Age}^{2}+\mathrm{DR}$ | 1495.86 | 967.64 | 2624.82 | 1461.28 |
| (7) Age + Age ${ }^{2}+\mathrm{CS}+\mathrm{CS} *$ Age | 1496.19 | 984.37 | 2621.91 | 1474.56 |
| (8) CS + Age + EL + DR + Age * EL | 1496.84 | 961.57(1) | 2609.49 | 1443.00(1) |
| (9) Age + Age ${ }^{2}$ | 1496.97 | 969.54 | 2627.87 | 1463.88 |
| (10) CS + Age + EL + DR + Age * EL + DR * EL | 1502.31 | 967.35 | 2613.19 | 1448.30(2) |
| (11) $\mathrm{FS}+\mathrm{CS}+\mathrm{DR}+$ Age +EL | 1504.01 | 970.94 | 2624.65 | 1458.64 |
| (12) $\mathrm{FS}+\mathrm{CS}+\mathrm{DR}+$ Age + Age $* \mathrm{FS}$ | 1516.75 | 980.92 | 2652.53 | 1476.12 |


Between brackets, the ranks of the three best models.
educational level (EL) and financial status (FS) was of interest. In this particular data set, two complications arise. Firstly, sampling in the HIS was based on a combination of stratification, multistage sampling and clustering [8]. Secondly, about 30 per cent of the 2893 women had one or more missing covariates for the variables of interest. These design issues, together with the likely occurrence of data to be missing, are inherent to surveys and should be taken into account when selecting an optimal model from a candidate set of models.

In Table I, an overview of 12 different models is given together with the original AIC and three weighted versions. The choice of the variables and the particular set of candidate models was partly driven by prior knowledge and expert opinions (for a related data analysis see Reference [9]). The first modification, 'AIC ${ }_{W_{1}}$ ', corrects for the survey design, the second version, 'AIC ${ }_{W_{2}}$ ', corrects for incomplete data and the combination of both can be found in version, ' $\mathrm{AIC}_{W_{1}, W_{2}}$ '.

Table I shows that different models are chosen by the different versions of the AIC; so it indicates that ignoring missingness or ignoring the sampling design can possibly lead to inappropriate model choices. We refer to Section 4 for a more thorough discussion.

Based on a theoretical justification, the weighted AICs are defined in the next section.

## 3. WEIGHTED AIC

Based on observations $\left(\mathbf{x}_{i}, y_{i}\right), i=1, \ldots, n$, consider the regression model

$$
\mathbf{y} \sim f(\mathbf{y} ; \boldsymbol{\theta}, \boldsymbol{\eta})
$$

where

$$
\mathbf{y}=\left(y_{1}, \ldots, y_{n}\right)^{\mathrm{T}}, \quad \boldsymbol{\theta}=\left(\theta\left(\mathbf{x}_{1}\right), \ldots, \theta\left(\mathbf{x}_{n}\right)\right)^{\mathrm{T}}, \quad \boldsymbol{\eta}=\left(\eta\left(\mathbf{x}_{1}\right), \ldots, \eta\left(\mathbf{x}_{n}\right)\right)^{\mathrm{T}}
$$

Here $f$ denotes the joint density of $\mathbf{y}$ (given $\mathbf{x}$ ), $\boldsymbol{\theta}$ the parameter of interest and $\boldsymbol{\eta}$ a nuisance parameter. The aim is to select an optimal or a few good models among a set of candidate
models. Several model selection criteria have been developed, in different settings and with different types of complexities in data and models (see References [10-13]).

Assume we start from a collection of models, in particular we consider models of form (1). The well-known AIC [10]

$$
\mathrm{AIC}=-2 L(\hat{\boldsymbol{\theta}}, \hat{\boldsymbol{\eta}})+2 K
$$

with $L(\boldsymbol{\theta}, \boldsymbol{\eta})$ denoting the loglikelihood of the model and $(\hat{\boldsymbol{\theta}}, \hat{\boldsymbol{\eta}})$ the maximum likelihood (ML) estimator of $(\boldsymbol{\theta}, \boldsymbol{\eta})$, originates from information theory. Here $K$ stands for the total number of estimated parameters, nuisance parameters included. The second term in the AIC formula is often interpreted as a penalization for complexity. The AIC was designed to be an approximately unbiased estimator of the expected Kullback-Leibler information (KL). In general, the KL information between model $f_{0}$ (denoting the 'true' model) and model $f$ (the approximating model (1)) is defined as (ignoring an 'historical' factor 2)

$$
I\left(f_{0}, f\right)=E\left\{\log \left(\frac{f_{0}(\mathbf{y})}{f(\mathbf{y} ; \boldsymbol{\theta}, \boldsymbol{\eta})}\right)\right\}
$$

(expectation with respect to the true model) and can be interpreted as the information loss using $f$ to approximate $f_{0}$, or as the distance from $f_{0}$ to $f$. This KL distance is not a metric, but it has the property that $I\left(f_{0}, f\right) \geqslant 0$ with equality only if $f \equiv f_{0}$.

### 3.1. Missing data

In case of missing data, the naive use of only CC in the definition of $I\left(f_{0}, f\right)$ can lead to serious deficiencies in its applicability to measure the distance between models (and consequently also in the use of its empirical version, the AIC). For simplicity, let us consider classical regression and suppose data are generated by a true model

$$
\mathbf{y} \sim \mathscr{N}_{n}\left(\boldsymbol{\mu}_{0}, \sigma_{0}^{2} I_{n}\right)
$$

where $\boldsymbol{\mu}_{0}=\left(\mu_{0}(1), \ldots, \mu_{0}(n)\right)^{\mathrm{T}}, \mathscr{N}_{n}$ denotes an $n$-variate normal distribution and $I_{n}$ the $n \times n$ identity matrix. Consider the approximating, or candidate, family of models

$$
\mathbf{y} \sim \mathscr{N}_{n}\left(\boldsymbol{\mu}(\boldsymbol{\theta}), \sigma^{2} I_{n}\right)
$$

where $\boldsymbol{\mu}=\left(\mu\left(\mathbf{x}_{1} ; \boldsymbol{\theta}\right), \ldots, \mu\left(\mathbf{x}_{n} ; \boldsymbol{\theta}\right)\right)^{\mathrm{T}}$.
For this setting, $E\{\log f(\mathbf{y} ; \boldsymbol{\theta}, \boldsymbol{\eta})\}$ can be written as ( $f$ now denoting the univariate normal density)

$$
E\left\{\sum_{i=1}^{n} \log f\left(y_{i} ; \mu\left(\mathbf{x}_{i}\right), \sigma^{2}\right)\right\}=-\frac{n}{2} \log \left(2 \pi \sigma^{2}\right)-E\left[\{\mathbf{y}-\boldsymbol{\mu}(\boldsymbol{\theta})\}^{\mathrm{T}}\{\mathbf{y}-\boldsymbol{\mu}(\boldsymbol{\theta})\}\right] /\left(2 \sigma^{2}\right)
$$

Using an analogous expression for $E\left\{\log f_{0}(\mathbf{y})\right\}$, it is easy to verify that

$$
I\left(f_{0}, f\right)=\frac{n}{2} \log \left(\sigma^{2} / \sigma_{0}^{2}\right)+n\left\{\frac{\sigma_{0}^{2}}{\sigma^{2}}-1\right\}+\left\{\boldsymbol{\mu}_{0}-\boldsymbol{\mu}(\boldsymbol{\theta})\right\}^{\mathrm{T}}\left\{\boldsymbol{\mu}_{0}-\boldsymbol{\mu}(\boldsymbol{\theta})\right\} /\left(2 \sigma^{2}\right)
$$

It follows that this measure is minimized as a function of $\sigma^{2}$ and $\boldsymbol{\mu}(\boldsymbol{\theta})$ (and equals 0 ) by taking $\sigma^{2}=\sigma_{0}^{2}$ and $\boldsymbol{\mu}(\boldsymbol{\theta})=\boldsymbol{\mu}_{0}$.

Now, let us introduce the missingness process. For $i=1, \ldots, n$, define the indicator $\delta_{i}=1$ if $\left(\mathbf{x}_{i}, y_{i}\right)$ is fully observed and 0 otherwise. In general it is possible that $\pi_{i}=P\left(\delta_{i}=1\right)=\pi\left(\mathbf{x}_{i}, y_{i}, z_{i}\right)$, so the probability that the $i$ th observation is not fully observed is allowed to depend on $\mathbf{x}_{i}$, $y_{i}$ or even on the value $z_{i}$ of an other, completely ignored, variable. In this paper we restrict attention to the MAR setting, implying that $\pi_{i}$ does not depend on $z_{i}$, that it additionally does not depend on $\mathbf{x}_{i}$ (resp. $y_{i}$ ) in case $\mathbf{x}_{i}$ (resp. $y_{i}$ ) might be missing.

The use of CC only (those for which $\delta_{i}=1$ ) (and hence ignoring the missing data mechanism) is translated in a replacement of (6) by

$$
\begin{aligned}
E\left\{\sum_{i=1}^{n} \delta_{i} \log f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right), \sigma^{2}\right)\right\}= & -\frac{E\{\operatorname{trace}(D)\}}{2} \log \left(2 \pi \sigma^{2}\right) \\
& -E\left[\{\mathbf{y}-\boldsymbol{\mu}(\boldsymbol{\theta})\}^{\mathrm{T}} D\{y-\boldsymbol{\mu}(\boldsymbol{\theta})\}\right] /\left(2 \sigma^{2}\right)
\end{aligned}
$$

where $D=\operatorname{diag}\left(\delta_{1}, \ldots, \delta_{n}\right)$. As a function of $\sigma^{2}$ and $\boldsymbol{\mu}(\boldsymbol{\theta})$, and using a saturated model $\boldsymbol{\mu}(\boldsymbol{\theta})=\boldsymbol{\theta}=\left(\theta_{1}, \ldots, \theta_{n}\right)$ for the mean function, this expression (8) is maximized and the corresponding CC version of the KL distance

$$
\begin{aligned}
I_{\mathrm{CC}}\left(f_{0}, f\right)= & E\left\{\sum_{i=1}^{n} \delta_{i} \log \left[\left(f_{0}\left(y_{i}\right) / f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right), \sigma^{2}\right)\right]\right\}\right. \\
= & \frac{E\{\operatorname{trace}(D)\}}{2} \log \left(\frac{\sigma^{2}}{\sigma_{0}^{2}}\right)+E\left[\left\{\boldsymbol{\mu}_{0}-\boldsymbol{\mu}(\boldsymbol{\theta})\right\}^{\mathrm{T}} D\left\{\boldsymbol{\mu}_{0}-\boldsymbol{\mu}(\boldsymbol{\theta})\right\}\right] /\left(2 \sigma^{2}\right) \\
& +E\left\{\boldsymbol{\zeta}^{\mathrm{T}} D \boldsymbol{\zeta}\right\} \frac{1}{2}\left(\frac{\sigma_{0}^{2}}{\sigma^{2}}-1\right)+E\left\{\boldsymbol{\zeta}^{\mathrm{T}} D\right\}\left(\boldsymbol{\mu}_{0}-\boldsymbol{\mu}(\boldsymbol{\theta})\right)\left(\frac{\sigma_{0}}{\sigma^{2}}\right)
\end{aligned}
$$

(with $\left.\zeta=\left(\mathbf{y}-\boldsymbol{\mu}_{0}\right) / \sigma_{0}\right)$ is minimized at

$$
\tilde{\theta}_{i}=\frac{E\left\{y_{i} \pi_{i}\right\}}{E\left\{\pi_{i}\right\}}=\mu_{0}(i)+\frac{\operatorname{Cov}\left(y_{i}, \pi_{i}\right)}{E\left\{\pi_{i}\right\}}
$$

and

$$
\tilde{\sigma}^{2}=\frac{\sum_{i=1}^{n} E\left[\pi_{i}\left\{y_{i}-\tilde{\theta}_{i}\right\}^{2}\right]}{\sum_{i=1}^{n} E\left\{\pi_{i}\right\}}
$$

In the above expressions and in the what follows, moment-related operators like the expectation $E$ or the covariance (Cov) act on the random variables $y_{i}$ and $\delta_{i}$ and treat $\mathbf{x}_{i}$ as nonrandom.

First of all, under a missing completely at random (MCAR) mechanism, $\pi_{i}=\pi$ and the above solutions simplify and are equal to the 'true' values, $\mu_{0}\left(\mathbf{x}_{i}\right)$ and $\sigma_{0}^{2}$, respectively. The same holds in the MAR case that $y_{i}$ is missing with probability $\pi_{i}=\pi\left(\mathbf{x}_{i}\right)$, only depending on $\mathbf{x}_{i}$. If however $\pi_{i}$ does depend on $y_{i}$ in a way that $\operatorname{Cov}\left(y_{i}, \pi_{i}\right) \neq 0, I_{\mathrm{CC}}\left(f_{0}, f\right)$ reaches a different minimum at (10) and (11). In fact, since by definition $I_{\mathrm{CC}}\left(f_{0}, f_{0}\right)=0$, this minimal value has to be negative (which is undesirable for a distance measure). If e.g. $y_{i}$ and $\pi_{i}$ are positively correlated, then $\tilde{\theta}_{i}>\mu_{0}\left(\mathbf{x}_{i}\right)$. This is to be expected since observations with smaller values of $y_{i}$ are discarded with higher probability. Also for nonsaturated models for $\boldsymbol{\mu}(\boldsymbol{\theta})$, such kind of anomalies can be shown.

AIC (2) based on the CC is given by

$$
\mathrm{AIC}_{\mathrm{CC}}=-2 \sum_{i=1}^{n} \delta_{i} \log \left[f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \hat{\boldsymbol{\theta}}_{\mathrm{CC}}\right), \hat{\sigma}_{\mathrm{CC}}^{2}\right)\right]+2 K
$$

where $\hat{\boldsymbol{\theta}}_{\mathrm{CC}}$ and $\hat{\sigma}_{\mathrm{CC}}^{2}$ are the ML estimators, maximizing the CC-loglikelihood (as described by the first term in (12)). For classical regression and ignoring constants, this can be simplified to

$$
\mathrm{AIC}_{\mathrm{CC}}=\left(\sum_{i=1}^{n} \delta_{i}\right) \log \left(\hat{\sigma}_{\mathrm{CC}}^{2}\right)+2 K
$$

In case of MCAR, criterion (12) or (13) is an approximately unbiased estimate of $I_{\mathrm{CC}}\left(f_{0}, f\right)$ and is expected to behave appropriately (the missingness just results in an implicit sample size reduction). But for the MAR setting with missingness probabilities depending on the response, nothing guarantees that the above AIC criteria will serve any longer as useful model selection criteria.

The shortcomings of a CC approach, as described above, can be circumvented by a simple modification of the KL distance $I_{\mathrm{CC}}\left(f_{0}, f\right)$ and corresponding $\mathrm{AIC}_{\mathrm{CC}}$. This modification is inspired by the technique of weighted estimation. Assuming a correct model is used, Flanders and Greenland [14] and Zhao and Lipsitz [15] showed that the use of weighted estimators, solving the weighted estimating equations (WEE)

$$
\sum_{i=1}^{n} w_{i} \Psi\left(y_{i} ; \boldsymbol{\theta}, \boldsymbol{\eta}\right)=0
$$

with $\Psi$ the derivative of the $\log$ (quasi)likelihood and with weights $w_{i}$ inversely proportional to the missingness probabilities, are consistent and asymptotically unbiased. The idea of WEE was inspired by the Horvitz-Thompson estimator in the closely related setting of design-based samples with unequal selection probabilities (see Reference [3]). In Section 3.2, we further exploit this setting and its similarity with missing data for model selection.

Analogous to (14), a weighted KL distance can be defined as

$$
I\left(f_{0}, f ; w\right)=E\left\{\sum_{i=1}^{n} w_{i} \log \left[\left(f_{0}\left(y_{i}\right) / f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right), \sigma^{2}\right)\right]\right\}\right.
$$

Taking the weights

$$
w_{i}=\delta_{i} / \pi_{i}
$$

the deficient distance $I_{\mathrm{CC}}\left(f_{0}, f\right)$ is rectified and turned into the original data KL distance ('original' referring to the 'full' data, before introducing missingness). Indeed,

$$
E\left\{\sum_{i=1}^{n} \frac{\delta_{i}}{\pi_{i}} \log \left[\left(f_{0}\left(y_{i}\right) / f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right), \sigma^{2}\right)\right]\right\}=\sum_{i=1}^{n} E\left\{\log \left[\left(f_{0}\left(y_{i}\right) / f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right), \sigma^{2}\right)\right]\right\}\right.\right.
$$

In a similar way, the weighted AIC

$$
\mathrm{AIC}_{W}=-2 \sum_{i=1}^{n} w_{i} \log \left[f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \hat{\boldsymbol{\theta}}_{W}\right), \hat{\sigma}_{W}^{2}\right)\right]+2 K
$$

with $w_{i}$ as in (16) and with $\hat{\boldsymbol{\theta}}_{W}$ and $\hat{\sigma}_{W}^{2}$ the weighted ML estimators (maximizing the weighted maximum likelihood), is expected to behave more appropriately, i.e. to correct for the missing data. Indeed, denote $\hat{\boldsymbol{\theta}}_{\mathrm{O}}$ and $\hat{\sigma}_{\mathrm{O}}^{2}$ the ML estimators based on the original data, and consider the Taylor expansion (linear terms cancelling out)

$$
\begin{aligned}
& -2 \sum_{i=1}^{n} w_{i} \log \left[f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \hat{\boldsymbol{\theta}}_{\mathrm{O}}\right), \hat{\sigma}_{\mathrm{O}}^{2}\right)\right] \\
& \quad \approx \mathrm{AIC}_{W}-2\left(\left(\hat{\boldsymbol{\theta}}_{\mathrm{O}}-\hat{\boldsymbol{\theta}}_{W}\right)\left(\hat{\sigma}_{\mathrm{O}}^{2}-\hat{\sigma}_{W}^{2}\right)\right) \mathscr{I}_{n}\left(\hat{\boldsymbol{\theta}}_{W}, \hat{\sigma}_{W}^{2}\right)\left(\left(\hat{\boldsymbol{\theta}}_{\mathrm{O}}-\hat{\boldsymbol{\theta}}_{W}\right)\left(\hat{\sigma}_{\mathrm{O}}^{2}-\hat{\sigma}_{W}^{2}\right)\right)^{\mathrm{T}}
\end{aligned}
$$

where the matrix $\mathscr{I}_{n}$ is the matrix of second derivatives of the weighted log-likelihood, evaluated at ( $\hat{\boldsymbol{\theta}}_{W}, \hat{\sigma}_{W}^{2}$ ). The expected value of the left-hand side equals the expected value of the AIC based on the original data. Since both estimates, the 'original' ( $\hat{\boldsymbol{\theta}}_{\mathrm{O}}, \hat{\sigma}_{\mathrm{O}}^{2}$ ) and the 'weighted' ( $\hat{\boldsymbol{\theta}}_{W}, \hat{\sigma}_{W}^{2}$ ), are estimating the same parameter (being the true value ( $\boldsymbol{\theta}_{0}, \sigma_{0}^{2}$ ) in case the model under consideration is a correct model), the second term on the right-hand side is negligible, at least in a first-order approximation.

For a normal regression model with $\mu\left(\mathbf{x}_{i}, \boldsymbol{\theta}\right)=\mathbf{x}_{i} \boldsymbol{\theta}, i=1, \ldots, n$, where $\mathbf{x}_{i}=\left(\begin{array}{llll}1 & x_{i 1} & \ldots & x_{i p}\end{array}\right)$ and $\boldsymbol{\theta}=\left(\begin{array}{llll}\theta_{0} & \theta_{1} & \ldots & \theta_{p}\end{array}\right)^{\mathrm{T}}$, the weighted AIC can be rewritten in terms of squared residuals

$$
\mathrm{AIC}_{W}=\left(\sum_{i=1}^{n} w_{i}\right) \log \left(\frac{\sum_{i=1}^{n} w_{i} e_{i}^{2}}{\sum_{i=1}^{n} w_{i}}\right)+2(p+2)
$$

where $e_{i}$ are the residuals from the fitted model, using weighted ML. In the context of robust model selection procedures, Agostinelli [16] introduced a robust modification of the AIC, based on the weighted likelihood methodology. He proposed a similar weighted AIC ${ }_{W}$, but with weights downplaying the contribution of highly influential outliers.

Of course, typically the missing probabilities are unknown and have to be estimated, introducing essentially two further complications: (i) finding appropriate estimates $\hat{\pi}_{i}$ which is again a model selection problem and (ii) the effect on the characteristics of $\mathrm{AIC}_{W}$ when using weights

$$
\hat{w}_{i}=\delta_{i} / \hat{\pi}_{i}
$$

Regarding the first complication, we suggest the use of a nonparametric or flexible semiparametric estimator (generalized additive models (gam) or e.g. regression trees for more complicated data structures, as illustrated in Sections 4 and 5). This avoids the need for another model selection step. It is also important to note that, since the estimation of the missingness probabilities is a step prior to the envisaged model selection exercise, and hence is common to all candidate models under consideration, it has no effect on the penalization term in the expression of $\mathrm{AIC}_{W}$. Concerning the second complication: rather than focusing on a theoretical study of the effect of estimating $\pi_{i}$ on the expected value of $\mathrm{AIC}_{W}$ (a Taylor expansion immediately shows highly 'untractable' bias expressions), we opted for examining the finite sample performance of $\mathrm{AIC}_{W}$ with estimated weights by a simulation study (see Section 5).

With or without missing data, the goal of a statistical analysis is to make valid and efficient inferences about a population of interest. Existing methods dealing with missing data often assume a correct model being used. Ignoring missingness in the model selection step
possibly results in the selection of poor and inappropriate models and consequently in invalid inferences. The $\mathrm{AIC}_{W}$ aims to select the model which would best describe the hypothetically complete data. Indeed, in the context of missing data, the use of inverse probability weights (16) can be seen as an (implicit) imputation as explicitly shown by Reilly and Pepe [17] in a simpler setting and one can verify that $\sum_{i=1}^{n} \hat{w}_{i}=\sum_{i=1}^{n} \delta_{i} / \hat{\pi}_{i} \approx n$.

In analogy to its expression based on the original data [18], we define a bias-corrected weighted AIC as

$$
\mathrm{AIC}_{W}^{\mathrm{cor}}=\mathrm{AIC}_{W}+\frac{2 K(K+1)}{\sum_{i=1}^{n} w_{i}-K-1}
$$

This small-sample correction (second-order bias adjustment) has been especially recommended in a setting where there are many parameters in relation to the size of the sample $n$ (for more details see Reference [19]). Its performance in some simulations is briefly discussed in Section 5.1.3.

### 3.2. Design-based samples

Assume a finite population consisting of $N$ units with measurements $\mathscr{M}=\left\{y_{1}, \ldots, y_{N}\right\}$. A particular sampling plan leads to the random variable $\delta_{i}=1$ if the $i$ th unit is included in the sample (and 0 otherwise) with $n=\sum_{i=1}^{N} \delta_{i}$ the total sample size. The selection probabilities are defined as $\pi_{i}=P\left(\delta_{i}=1\right)$, for $i=1, \ldots, N$. The choice $\pi_{i}=n / N$ corresponds to a simple random sample. In this finite population setting, only the $\delta_{i}$ are to be considered as random; the set $\mathscr{M}$ is to be considered as unknown but fixed.

Supposing that the population $\mathbf{y}=\left(y_{1}, \ldots, y_{N}\right)^{\mathrm{T}}$ is a single realization of a true 'superpopulation' model $f_{0}(\cdot)$, using the approximating model $f\left(\cdot ; \mu\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right), \sigma^{2}\right)$ and treating the sample indicated by the $\delta_{i}$ as a random sample, a KL distance similar to the $I_{\mathrm{CC}}\left(f_{0}, f\right)$ measure in (9) can be defined as (with now the expectation $E$ with respect to the $\delta_{i}$ 's, conditional on the 'realized' population)

$$
\begin{aligned}
I_{\mathrm{DB}}\left(f_{0}, f\right) & =E\left\{\sum_{i=1}^{N} \delta_{i} \log \left[\left(f_{0}\left(y_{i}\right) / f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right), \sigma^{2}\right)\right]\right\}\right. \\
& =\sum_{i=1}^{N} \pi_{i} \log \left[\left(f_{0}\left(y_{i}\right) / f\left(y_{i} ; \mu\left(\mathbf{x}_{i} ; \boldsymbol{\theta}\right), \sigma^{2}\right)\right]\right.
\end{aligned}
$$

For true and approximating models as in (4) and (5), with now $\boldsymbol{\mu}=\left(\mu\left(\mathbf{x}_{1} ; \boldsymbol{\theta}\right), \ldots, \mu\left(\mathbf{x}_{N} ; \boldsymbol{\theta}\right)\right)^{\mathrm{T}}$ and $\boldsymbol{\mu}_{0}=\left(\mu_{0}(1), \ldots, \mu_{0}(N)\right)^{\mathrm{T}}$ and with $\boldsymbol{\zeta}=\left(\mathbf{y}-\boldsymbol{\mu}_{0}\right) / \sigma_{0}$ as before, we obtain

$$
\begin{aligned}
I_{\mathrm{DB}}\left(f_{0}, f\right)= & \frac{\operatorname{trace}(\Pi)}{2} \log \left(\frac{\sigma^{2}}{\sigma_{0}^{2}}\right)+\left\{\boldsymbol{\mu}_{0}-\boldsymbol{\mu}(\boldsymbol{\theta})\right\}^{\mathrm{T}} \Pi\left\{\boldsymbol{\mu}_{0}-\boldsymbol{\mu}(\boldsymbol{\theta})\right\} /\left(2 \sigma^{2}\right) \\
& +\zeta^{\mathrm{T}} \Pi \zeta \frac{1}{2}\left(\frac{\sigma_{0}^{2}}{\sigma^{2}}-1\right)+\zeta^{\mathrm{T}} \Pi\left(\boldsymbol{\mu}_{0}-\boldsymbol{\mu}(\boldsymbol{\theta})\right)\left(\frac{\sigma_{0}}{\sigma^{2}}\right)
\end{aligned}
$$

where $\Pi=\operatorname{diag}\left(\pi_{1}, \ldots, \pi_{n}\right)$. As an example, consider a simple two-valued true superpopulation model

$$
\boldsymbol{\mu}_{0}=\left(\mu_{0}(1), \ldots, \mu_{0}\left(N_{1}\right), \mu_{0}\left(N_{1}+1\right), \ldots, \mu_{0}(N)\right)^{\mathrm{T}}=\left(\mu_{1}, \ldots, \mu_{1}, \mu_{2}, \ldots, \mu_{2}\right)^{\mathrm{T}}
$$

with $\mu_{1} \neq \mu_{2}$, and the incorrect constant model $\boldsymbol{\mu}(\theta)=(\theta, \ldots, \theta)^{\mathrm{T}}$. For this incorrect model, the minimal distance $I_{\mathrm{DB}}\left(f_{0}, f\right)$ is at least as small as its value at $\tilde{\sigma}^{2}=\sigma_{0}^{2}$ and

$$
\tilde{\theta}=\frac{\sum_{i=1}^{N} \pi_{i} y_{i}}{n}
$$

Using the correct two-parameter mean model with $\sigma^{2}=\sigma_{0}^{2}, I_{\mathrm{DB}}\left(f_{0}, f\right)$ is minimized at

$$
\tilde{\mu}_{1}=\frac{\sum_{i=1}^{N_{1}} \pi_{i} y_{i}}{n_{1}}, \quad \tilde{\mu}_{2}=\frac{\sum_{i=1}^{N_{2}} \pi_{i} y_{i}}{n_{2}}
$$

where $n_{1}=\sum_{i=1}^{N_{1}} \delta_{i}$ and $n_{2}=\sum_{i=N_{1}+1}^{N} \delta_{i}$. Now, in the particular case that the selection probabilities induce a bias resulting in $\tilde{\mu}_{1}=\tilde{\mu}_{2}$, the KL distance $I_{\mathrm{DB}}\left(f_{0}, f\right)$ is exactly the same for both models and hence the incorrect model is indistinguishable from the correct model.

Identical to the case of missing data, the weighing of the KL distance and corresponding AIC, with weights as in (16), can be used to correct both measures. Note that in general, the selection probabilities can depend on both $\mathbf{x}_{i}$ and $y_{i}$. In most applications the selection probabilities $\pi_{i}$ are determined by the design of the sample and hence are known.

In contrast to the missing data situation, using weights (16) in $\mathrm{AIC}_{W}$ for design-based samples does not reflect an 'implicit imputation'. The idea here is to assign weights to the observations to make the sample representative for the population under consideration. Therefore, the inverse selection probabilities have to be standardized to sum up to the size of the sample.

### 3.3. Design-based samples with missing observations

In typical surveys, as in the cervix cancer screening example introduced in Section 2, both complications occur together. In this case $\delta_{i}$, indicating whether or not the $i$ th unit is in the sample and is fully observed, can be written as

$$
\delta_{i}=\delta_{i}^{D} \delta_{i}^{M}
$$

where $\delta_{i}^{D}=1$ if the $i$ th unit is included in the sample (as in Section 3.2) and $\delta_{i}^{M}=1$ if the $i$ th unit is fully observed (as in Section 3.1). The weighted AIC (17) can now be based on weights $w_{i}=\delta_{i} / \pi_{i}$ where

$$
\pi_{i}=P\left(\delta_{i}=1\right)=P\left(\delta_{i}^{M}=1 \mid \delta_{i}^{D}=1\right) P\left(\delta_{i}^{D}=1\right)
$$

These latter probabilities can be estimated by the product of the (known) probabilities $P\left(\delta_{i}^{D}=1\right)$ and the (nonparametrically) estimated probabilities $P\left(\delta_{i}^{M}=1 \mid \delta_{i}^{D}=1\right)$.

In the next section, we show how the idea of a weighted AIC can be extended to select a smoothing parameter for nonparametric regression.

### 3.4. Smoothing parameter selection using $A I C_{W}$

Assume

$$
y_{i}=\mu_{0}\left(\mathbf{x}_{i}\right)+\varepsilon_{i}, \quad i, \ldots, n
$$

where $\mu_{0}(\cdot)$ is an unknown smooth function and $\varepsilon_{i}, i=1, \ldots, n$, are independent error terms with mean 0 and variance $\sigma_{0}^{2}$. Different linear smoothers for $\mu$ are available: orthogonal series, kernel estimators, splines, ... (see e.g. Reference [20]). The most crucial choice for any smoother is the choice of the smoothing parameter. Hurvich et al. [7] proposed to select this parameter $\alpha$ by minimizing the corrected AIC

$$
\operatorname{AIC}_{\alpha}^{\mathrm{cor}}=n \log \left(\hat{\sigma}^{2}\right)+\frac{n+\operatorname{trace}\left(S_{\alpha}\right)}{1-\left\{\operatorname{trace}\left(S_{\alpha}\right)+2\right\} / n}
$$

where $S_{\alpha}$ is the smoother matrix for which $\hat{\mathbf{y}}=S_{\alpha} \mathbf{y}$.
In case of an incomplete or design-based sample, this criterion can be turned into a weighted version

$$
\mathrm{AIC}_{\alpha, W}^{\mathrm{cor}}=\left(\sum_{i=1}^{n} w_{i}\right) \log \left(\frac{\sum_{i=1}^{n} w_{i} e_{i}^{2}}{\sum_{i=1}^{n} w_{i}}\right)+\frac{\sum_{i=1}^{n} w_{i}+\operatorname{trace}\left(S_{W, \alpha}\right)}{1-\left\{\operatorname{trace}\left(S_{W, \alpha}\right)+2\right\} /\left(\sum_{i=1}^{n} w_{i}\right)}
$$

where $S_{W, \alpha}$ is the smoother matrix from the weighted fit. Taking $S_{W, \alpha}$ the classical regression 'hat matrix', (31) reduces (up to a constant) to (21).

## 4. THE HIS 1997 REVISITED

Since the design of the Health Interview Survey follows a complex multistage probability sampling scheme, it is necessary to incorporate this in the model selection procedure. A second complication is the substantial amount of missing covariate data (about 30 per cent) spread over several covariates. Let us consider the candidate models in Table I. The models are ranked according to their AIC based on the CC (second column). For all other columns, the three models with lowest AIC values are indicated by their ranks.

In the third column, a first weighted version, $\mathrm{AIC}_{W_{1}}$, takes into account the complex design. Individual weights, $W_{1}$, reflecting the stratification at provincial level and the differential selection probabilities within households were available. This results in a somewhat different ordering of the models. The best model now is the model with original rank 8.

Similarly, the fourth column shows the modified AIC value, $\mathrm{AIC}_{W_{2}}$, incorporating missing covariate data (assuming MAR). Because of the high-dimensional covariate space, a classification tree with surrogate splitting was used to obtain estimates of the missingness probabilities and thus the weights $W_{2}$. This leads to only minor changes, as compared to the second column. The best model now is model 2.

In the fifth column, both complications have been taken into account by multiplying both weights in $\mathrm{AIC}_{W_{1}, W_{2}}$. Model 8 showing up again, now having the lowest AIC value, while model 10 is the second best model.

Although essentially the same set of models reappears as the set of best models, this example illustrates that differently weighted AIC criteria can select different models as best ones. Since the choice of the final model or the set of final models used, for e.g. model
averaging is affected by missing data and by the design, we recommend in general the use of the weighted criteria (at least as a sensitivity tool).

To study the effects of weighing more closely, a simulation study in a variety of settings was conducted. The next section summarizes our main findings. All computations were conducted in R 2.0.1 [21].

## 5. SIMULATIONS

In the first scenario, we consider a setting with missing covariate data. The second scenario focuses on design-based samples and the last scenario on the selection of the smoothing parameter in nonparametric regression.

### 5.1. Scenario 1: parametric model selection for incomplete data

In this first scenario, uniform $[0,10] x$ values were generated, together with (independently) Bernoulli(0.5) $z$ values. Given $x$ and $z$, response $y$ values were generated from a normal distribution with mean $\mu_{0}(x, z)$ and variance $\sigma_{0}^{2}$. $x$ observations were then turned missing with conditional probability

$$
\pi(y, z)=1-[1+\exp \{1-0.009(y-300)\}]^{-1}
$$

Not depending on unobserved $x$ values, the missingness process is MAR. Let $n$ denote the total sample size and $n_{c}$ the number of complete observations. We generated 1000 different samples $\left\{\left(x_{i}, z_{i}, y_{i}\right), i=1, \ldots, n\right\}$, with fixed design $\left\{x_{i}, z_{i}, i=1, \ldots, n\right\}$. For each sample, eight different regression models were fit, all submodels of $\mu(x, z)=\beta_{0}+\beta_{1} x+\beta_{2} x^{2}+\beta_{3} z+\beta_{4} x z$.

Four different 'strategies' are compared: (i) AIC on the original data, before introducing missingness (what we would get if no values were missing), (ii) (unweighted) AIC on the CC only (ignoring missingness), (iii) weighted AIC using the true weights (16) and (iv) weighted AIC, using the estimated weights (20). The probabilities (32) are estimated by gam estimates $\hat{\pi}(y, z)$ (using the R package 'mgcv 1.1-8' [22]).

In a first setting, the set of candidate models contains the true model while in a second setting, this is not the case.
5.1.1. A first setting: generating model included. In this first setting, the same with more general setting as above, $y$ values were generated from a normal distribution with mean $\mu_{0}(x, z)=-3+3 x+5 x^{2}$ and variance $\sigma_{0}^{2}=\exp (5)$. This resulted in that on average 35 per cent of the $x$ values were missing. In Figure 1, a typical data set for setting 1 is shown together with the missingness probabilities and the estimated weights. This latter figure shows a double curve, as a consequence of the additive model in $x$ and $z$ (being binary).

The first part of Table II displays the results for $n=50$. Each column (from 2 to 9) corresponds to a particular model and the numbers show how often the respective model has been selected by AIC under the four strategies mentioned above. Models more complex than the true quadratic model $\left\{x, x^{2}\right\}$ can be considered as correct models, the others as incorrect models. The last rightmost column shows the total number of times a correct model was chosen. The table shows that for this setting, the unweighted AIC applied on the CC, very often selects the incorrect simpler model $\{x\}$. This is to be expected since the missingness

![](https://cdn.mathpix.com/cropped/5ee9d466-bcbf-4e65-9392-2e59255eaec0-12.jpg?height=536&width=1428&top_left_y=306&top_left_x=258)
Figure 1. For an arbitrary chosen sample under Scenario 1, setting 1: (a) original sample, CC (white bullets) and unobserved data (black bullets); (b) missingness probabilities; and (c) estimated weights.

Table II. Scenario 1, setting 1: the numbers indicate how often a model has been selected.
|  | 1 | $x$ | $z$ | $x, x^{2}$ | $x, z$ | $x, z$, $x z$ | $x, x^{2}$, $z$ | $x, x^{2}$, $z, x z$ | Correctly classified |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| AIC, $n=50$ |  |  |  |  |  |  |  |  |  |
| Original data | 0 | 272 | 0 | 467 | 55 | 40 | 85 | 81 | 633 |
| CC | 0 | 447 | 0 | 274 | 97 | 53 | 81 | 48 | 403 |
| True weighted | 0 | 271 | 0 | 254 | 125 | 99 | 101 | 150 | 505 |
| Est. weighted | 0 | 329 | 0 | 286 | 100 | 83 | 102 | 106 | 494 |
| AIC, $n=30$ |  |  |  |  |  |  |  |  |  |
| Original data | 0 | 310 | 0 | 392 | 85 | 63 | 82 | 68 | 542 |
| CC | 9 | 436 | 0 | 255 | 121 | 76 | 54 | 49 | 358 |
| True weighted | 4 | 284 | 0 | 228 | 134 | 118 | 96 | 136 | 460 |
| Est. weighted | 7 | 324 | 1 | 253 | 119 | 108 | 91 | 117 | 461 |
| $A I C^{\mathrm{cor}}, n=30$ |  |  |  |  |  |  |  |  |  |
| Original data | 0 | 435 | 0 | 392 | 77 | 31 | 40 | 25 | 457 |
| CC | 16 | 616 | 3 | 217 | 80 | 34 | 26 | 8 | 251 |
| True weights | 6 | 398 | 1 | 260 | 129 | 77 | 61 | 68 | 389 |
| Est. weights | 8 | 442 | 0 | 275 | 122 | 53 | 56 | 63 | 394 |


The last column shows how often a correct model has been chosen, out of 1000 .
is mainly located at the larger $y$ values (which of all response values mostly represent the quadratic effect). The weighted versions correct for that, especially the one with true weights which selects about 10 per cent more often a correct model.

Similar results were obtained for variations on setting 1, such as a larger error variance, less missingness, a smaller quadratic effect and a smaller/larger sample size (not reported here, except for $n=30$, see second part of Table II).

The use of the weighted version improves the performance of the AIC and the version with known weights is consistently choosing more correct models than with estimated weights. On
the other hand, the version with estimated weights constantly performs better than with true weights in selecting the only true model. One might argue that the gain by using the weighted AIC is not so spectacular but rather moderate, that it tends to select more complicated models and that, thinking critically further along these lines, always taking the 'most complex model' (including $x, x^{2}, z$ and $x z$ ) is actually the best criterion (since it leads to a 100 per cent correct classification according to our definition of a correct model). But first of all, we have to realize that correcting for missing information is often a hard exercise, since information in available data might be very scarce. Secondly, the AIC is known to be an inconsistent model selection criterion [23]. And thus the selection of somewhat more complicated models might be justified in this setting and not just arbitrary. Moreover a needless complex model will be accompanied with larger variability in its estimates. To show that the weighted AIC does not just select more complex models in an arbitrary way, but leads to models with an improved accuracy, Table III shows, for setting 1, mean averaged squared errors (together with squared bias and variance decomposition)

$$
\text { MASE }=\frac{1}{1000} \sum_{r=1}^{1000}\left\{\frac{1}{n} \sum_{i=1}^{n}\left(\hat{\mu}^{(r)}\left(x_{i}, z_{i}\right)-\mu_{0}\left(x_{i}, z_{i}\right)\right)^{2}\right\}
$$

for the different AIC selected models together with that of the 'most complex model'. Here, $\hat{\mu}^{(r)}\left(x_{i}, z_{i}\right)$ denotes the fitted value within simulation run $r$. First of all, the numbers emphasized (in italic) in Table III, clearly show the large increase in MASE for the unweighted AIC (MASE $=4918.95$ as compared to 2125.32 for the original data) and the improvement when using the weighted AIC (MASE $=3891.60$ ). This table also shows that choosing the most complex model is not a sensible strategy (as expected) and more importantly that the weighted AIC does lead to a considerable improvement. Just using CC has a disastrous effect on the quality of the selected fits (particularly on the bias), whereas the use of the estimated weighted AIC leads to the best results in terms of MASE. Indeed, the latter reduces bias spectacularly,

Table III. Scenario 1, setting 1: MASE and bias-variance decomposition based for the four strategies from Table II together with the 'most complex model strategy'.
| Model selection | Bias ${ }^{2}$ | Var | MASE |
| :--- | :--- | :--- | :--- |
| Original data |  |  |  |
| Min AIC | 39.26 | 2085.05 | 2124.32 |
| Most complex | 2.25 | 2253.05 | 2255.30 |
| CC |  |  |  |
| Min AIC | 2433.37 | 2485.58 | 4918.95 |
| Most complex | 1986.74 | 2964.73 | 4951.47 |
| True weighted |  |  |  |
| Min $\mathrm{AIC}_{W}$ | 460.62 | 3984.71 | 4445.33 |
| Most complex | 404.51 | 4289.29 | 4693.81 |
| Est. weighted |  |  |  |
| Min $\mathrm{AIC}_{W}$ | 738.53 | 3153.06 | 3891.60 |
| Most complex | 608.09 | 3595.19 | 4203.28 |


at the cost of a moderate increase in variance. That the use of estimated rather than true weights lead to the smallest MASE values is in accordance with known results in related settings (see e.g. Reference [24]).
5.1.2. Nonparametric weighting methods. Different smoothers can be used to estimate the missingness probabilities $\pi(y, z)$. In setting 1, Equation (32) shows that these probabilities only depend on $y$. In Section 5.1.1, these probabilities were estimated with a gam model, as a function of both $y$ and $z$. A gam using $y$ only, a Nadaraya-Watson (NW) kernel estimate using both $y$ and $z$ or $y$ only, with fixed or with data-driven bandwidth (cross-validation) showed that the best results are obtained when using a gam model, but the other techniques provide similar results. Main conclusion is that the choice of smoother and smoothing parameter, although they have a similar behaviour for this setting, is not unimportant. It is also recommendable to examine the missingness process carefully, so that accurate estimation of the probabilities is possible.
5.1.3. Corrected AIC. For small sample sizes, the use of the corrected AIC (21) is recommended. The results in the third part of Table II are based on the corrected AIC for the first setting but now with $n=30$. The improvement of the weighted AIC ${ }^{\text {cor }}$ over the CC AIC ${ }^{\text {cor }}$ is considerable, especially when the weights are estimated. Compared to the AIC ( $n=30$ ), the corrected AIC selects simpler models.
5.1.4. A second setting: generating model not included. We now consider the (more realistic) setting that the set of candidate models does not contain the true model. With the same general settings as above, the response $y$ is now generated from a normal distribution with mean function $\mu_{0}(x, z)=-3-3 \log (x+1)+5 x^{2}$ and variance $\sigma_{0}^{2}=\exp (5)$. The same set of candidate models is considered. Since now direct comparison with the true model, nor a categorization in correct or incorrect models is possible anymore, only MASE values were calculated for the different methods (Table IV). Again, as before, gam was used to estimate the weights. Similar to setting 1, the results show the benefit in using the $\mathrm{AIC}_{W}$.

### 5.2. Scenario 2: model selection for design-based samples

To illustrate the use of the weighted AIC for design-based samples, a population $\left\{y_{1}, \ldots, y_{N}\right\}$ of size $N=1500$ was generated, as a single realization from the superpopulation model $f_{0}$, being a normal distribution with variance $\sigma_{0}^{2}$ and mean $\mu_{0}(i)=\mu_{1}$ for $i=1, \ldots, 500$ (group 1 ), $\mu_{0}(i)=\mu_{2}$ for $i=501, \ldots, 1000$ (group 2), $\mu_{0}(i)=\mu_{3}$ for $i=1001, \ldots, 1500$ (group 3).

One thousand samples were taken by dividing this population into two strata based on the ordered population $y$ values: the 300 largest $y$ values of the third group and the remaining $1200 y$ values. The sample was then taken as follows: a population unit $i$ is selected with probability $p_{1}$ when it belongs to the first stratum and with probability $p_{2}$ when it belongs to the second stratum. If $p_{1}<p_{2}$ this results in an undersampling of units in the third group with the larger $y$ values.

The (single) population was generated with $\mu_{2}=\mu_{3}=\kappa=-\mu_{1}$ with $\kappa>0 .\left\{\kappa, \sigma_{0}\right\}$ was chosen $\{0.5,3\}$ and sampling was done according to different choices of $\left(p_{1}, p_{2}\right)$, ranging from simple random sampling $p_{2} / p_{1}=1$ to highly unequal stratified sampling $p_{2} / p_{1}=11$ as shown in Table V. For each of the samples, five different models were fit: (1) $\mu_{1}=\mu_{2}=\mu_{3}$,

Table IV. Scenario 1, setting 2: MASE and bias-variance decomposition based for the four strategies from Table II together with the 'most complex model strategy'.
| Model selection | Bias ${ }^{2}$ | Var | MASE |
| :--- | :--- | :--- | :--- |
| Original data |  |  |  |
| Min AIC | 41.58 | 2079.93 | 2121.50 |
| Most complex | 2.90 | 2236.82 | 2239.72 |
| $C C$ |  |  |  |
| Min AIC | 2040.05 | 2310.80 | 4350.85 |
| Most complex | 1638.04 | 2750.06 | 4388.10 |
| True weighted |  |  |  |
| Min $\mathrm{AIC}_{W}$ | 382.79 | 3516.66 | 3899.45 |
| Most complex | 307.85 | 3802.61 | 4110.46 |
| Est. weighted |  |  |  |
| Min $\mathrm{AIC}_{W}$ | 439.66 | 3128.05 | 3567.70 |
| Most complex | 374.15 | 3447.90 | 3822.05 |


Table V. Scenario 2: the number of models chosen by AIC and AIC ${ }_{W}$, for different choices of $p_{1}$ and $p_{2}$.
| $p_{1}$ | $p_{2}$ | AIC |  |  |  |  |  | $\mathrm{AIC}_{W}$ |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 1 | 2 | 3 | 4 | 5 | Cor | 1 | 2 | 3 | 4 | 5 | Cor |
| 0.025 | 0.275 | 92 | 120 | 56 | 596 | 136 | 192 | 66 | 175 | 510 | 52 | 197 | 707 |
| 0.050 | 0.250 | 189 | 19 | 392 | 381 | 19 | 411 | 46 | 171 | 590 | 12 | 181 | 771 |
| 0.100 | 0.200 | 126 | 131 | 651 | 31 | 61 | 712 | 60 | 197 | 615 | 7 | 121 | 736 |
| 0.150 | 0.150 | 133 | 108 | 639 | 64 | 56 | 695 | 125 | 108 | 648 | 63 | 56 | 704 |


(2) $\mu_{1}=\mu_{2}$, (3) $\mu_{2}=\mu_{3}$, (4) $\mu_{1}=\mu_{3}$, and (5) no restrictions. Model (3) is the true model, model (5) is another correct model. The other models assume $\mu_{1}=\mu_{2}$ or $\mu_{1}=\mu_{3}$ and are incorrect (for $\kappa \neq 0$ ).

The results in Table V show an improved selection for the $\mathrm{AIC}_{W}$ compared to the AIC. Models (3) and (5) are chosen more frequently by the $\mathrm{AIC}_{W}$.

For different variations of this setting such as a smaller $p_{1}, p_{2}$, a larger $\kappa$ and a larger $\sigma_{0}$, the $\mathrm{AIC}_{W}$ outperforms AIC. One can also observe that the number of times a correct model is selected by the $\mathrm{AIC}_{W}$ is more or less the same for all different choices of ( $p_{1}, p_{2}$ ). When sampling probabilities are equal and thus a simple random sample is taken, the choices made using AIC and AIC ${ }_{W}$ are essentially the same (as expected).

### 5.3. Scenario 3: smoothing parameter selection in nonparametric regression for incomplete data

For this scenario, $n=200 x$ values were generated from uniform $[0,1]$, and corresponding $y$ values from a normal distribution with mean $\mu_{0}(x)=1-48 x+218 x^{2}-315 x^{3}+145 x^{4}$ and

![](https://cdn.mathpix.com/cropped/5ee9d466-bcbf-4e65-9392-2e59255eaec0-16.jpg?height=878&width=1412&top_left_y=308&top_left_x=264)
Figure 2. Average of the fitted values based on the chosen models over simulation runs together with the true function and 95 per cent confidence intervals. From left to right: the original data, the CC and the weighted CC, using either $\hat{\sigma}_{\mathrm{ML}}^{2}$ (upper row) or $\hat{\sigma}_{\mathrm{U}}^{2}$ (lower row).

variance $\sigma_{0}^{2}=8$. This corresponds to one of the simulation settings used in Reference [7]. Next, $x$ observations were turned missing with probability

$$
\pi(y)=\left[1+\exp \left\{2-0.1(y-2)^{2}\right]^{-1}\right.
$$

For each of the 1000 generated samples $\left\{Y_{i}, i=1, \ldots, n\right\}$ with a fixed design $\left\{x_{i}, i=1, \ldots, n\right\}$, a smoothing spline was fitted (using smooth.spline in R ) according to three methods, and with smoothing parameter selected by the corrected AIC (as introduced by Hurvich et al. [7]). The first method is based on the original data, while the second method is based on the CC only and finally the third method weights the CC (at the model selection stage and at the final fitting stage) with $\hat{w}_{i}=1 / \hat{\pi}_{i}$ where $\hat{\pi}_{i}$ is the estimated probability for a CC to be observed. The estimation of $\pi_{i}$ is also based on a smoothing spline with smoothing parameter again determined by the corrected AIC.

In this context, Wahba [25] uses the unbiased variance estimator

$$
\hat{\sigma}_{\mathrm{U}}^{2}=\frac{y^{\mathrm{T}}\left(I-S_{\alpha}\right)^{2} y}{\operatorname{trace}\left(I-S_{\alpha}\right)}
$$

where $S_{\alpha}$ is the smoother matrix. The use of $\hat{\sigma}_{\mathrm{U}}^{2}$ instead of $\hat{\sigma}_{\mathrm{ML}}^{2}$ is equivalent to an extra penalization of $-n \log \left(\operatorname{trace}\left(I-S_{\alpha}\right)\right)$, which corrects for undersmoothing. The simulation
average of the equivalent number of parameters using $\hat{\sigma}_{\text {ML }}^{2}$ equal 8.33, 7.55 and 18.31 for the original data, CC and weighted version, respectively, while for $\hat{\sigma}_{\mathrm{U}}^{2}$, the values 6.99, 6.31 and 9.00 were obtained. The models using the unbiased estimator are generally smoother and this reduction in equivalent number of parameters is very substantial for the weighted analysis. Other simulations confirmed this and therefore we certainly recommend the use of the unbiased estimator $\hat{\sigma}_{\mathrm{U}}^{2}$ for the weighted method.

In Figure 2, the true curve (the solid line) and the simulation average of the fitted curves for all three methods and both variance estimators, together with 95 per cent pointwise confidence intervals, are shown. Again, the beneficial effect on the smoothing when using the unbiased variance estimator is illustrated. The middle panels show that there is substantial bias at both minima, when using the CC without weighting. The weighted AIC ${ }^{\text {cor }}$ does correct for bias, as shown in the right panels.

The simulation MASE was calculated for each method and each variance estimator. MASE values of 13.64, 26.51 and 32.10 were found for the corrected AIC on the original data, the CC and its weighted version using $\hat{\sigma}_{\mathrm{ML}}^{2}$, respectively, while 20.10 was found when using $\hat{\sigma}_{\mathrm{U}}^{2}$.

## 6. DISCUSSION

The naive use of model selection criteria in case of incomplete and design-based samples can lead to the selection of an inappropriate or non-optimal model. In this paper, we introduced a weighted Akaike information criterion. The weights are inversely proportional to the selection probabilities and if unknown, can be estimated nonparametrically. Simulations show that the use of this weighted AIC results in improved model selection for design-based samples. For incomplete data, the model-selection performance of the weighted AIC is somewhat less pronounced. But missing data are more problematic than design-related complications. Various views can be taken. First, one may want to find out which model best describes the observed portion of the data in a pragmatic way. Second, one may desire to know which model would best describe the hypothetically complete data. There are advantages and disadvantages to both methods, and it is most sensible to frame them within the context of a sensitivity analysis, in an effort to assess to what extent incompleteness is able to distort our model choice and, ultimately, associated inferences. Moreover, the simulated MASE results are showing the improved accuracy of the $\mathrm{AIC}_{W}$-selected models. So, in our opinion, it is a worthwhile and relatively simple exercise to complement naive model selection (ignoring missingness or design) with a weighted one.

Next to the AIC, several other model selection criteria have been developed and can be extended to a weighted version to handle incomplete and design-based samples. A small simulation study confirmed the improved performance of Mallows' $C_{p}$ and the Bayesian information criterion (BIC). While the AIC is inconsistent but asymptotically efficient and the gain of using $\mathrm{AIC}_{W}$ was clearly shown by calculating the MASE, the BIC is an asymptotically consistent model selection criterion and the improvements of using a weighted version were more pronounced in the improved selection of the true model.

As mentioned before, the $\mathrm{AIC}_{W}$ for incomplete data can be seen as an implicit imputation approach. An obvious alternative method is the use of an explicit imputation-based AIC. Selection is done by first imputing the missing values and then using the classical AIC on the augmented data. Of course the performance of this method is directly related to the quality of
the imputation model. One option here is to use a flexible nonparametric model, thus avoiding an additional model selection step.

We investigated the performance of this imputation-based approach in a small simulation study for scenario 1. Data were imputed using mean-imputation based on a generalized additive model. The imputation-step is nonparametric in nature and takes place prior to the envisaged model selection, so it is common to all candidate models.

Calculating the MASE for setting 2 using the imputation-based AIC gives a value of 4643.93 of which 151.83 is ascribed to the squared bias and 4492.10 to the variance, as compared to $3567.70,439.66$ and 3128.05 , respectively, for the (estimated) $\mathrm{AIC}_{W}$. Similar results were found for setting 1, i.e. the imputation-based AIC selected the true model 471 times, essentially the same as the original data does, but it selects a 'correct' model 744 times. So, more often the true (and a correct) model is chosen, but the selected models appear to show highly variable fits. Moreover, in situations where $x$ cannot be written as a function $y$ the imputation method suffers from structural defects. A detailed study of this imputation-based method is topic of current research. For the cervix cancer screening data, $\mathrm{AIC}_{W}$, taking into account the design, on an augmented data set, where imputation was done using the random forest methodology of Breiman [26] selected models (2), (3) and (11).

Other options to deal with missingness in the context of model selection are full likelihood methods, that model both measurement and missingness part simultaneously. This is another challenging approach. Because of the similarity between incomplete and design-based samples, we focused on the weighted AIC in this paper.

Next to the performance of imputation-based selection methods, extensions to weighted versions of model selection criteria for generalized estimating equations in the context of clustered data as proposed in References [27,28], are topics of current research. Additional further research includes deriving new lack of fit tests when dealing with incomplete and design-based data (e.g. modifications of Reference [29]), and the use of a weighted likelihood ratio test (see e.g. Reference [30]) in this context.

## ACKNOWLEDGEMENTS

Financial support from the IAP research network No. P5/24 of the Belgian Government (Belgian Science Policy) is gratefully acknowledged. We wish to thank the Editor and two referees for helpful suggestions that have improved the manuscript.

## REFERENCES

1. Little RJA. Regression with missing X's: a review. Journal of the American Statistical Association 1992; 87:1227-1237.
2. Zhao LP, Lipsitz S, Lew D. Regression analysis with missing covariate data using estimating equations. Biometrics 1996; 52:1165-1182.
3. Horvitz DG, Thompson DJ. A generalization of sampling without replacement from a finite universe. Journal of the American Statistical Association 1952; 47:663-685.
4. Shimodaira H. A new criterion for selecting models from partially observed data. In Selecting Models from Data: Artificial Intelligence and Statistics IV. Cheeseman P, Oldford RW (eds), vol. 89. 1994; 21-29.
5. Cavanaugh JE, Shumway RH. An Akaike information criterion for model selection in the presence of incomplete data. Journal of Statistical Planning and Inference 1998; 67:45-65.
6. Little RJA, Rubin DB. Statistical Analysis with Missing Data. Wiley: New York, 1987.
7. Hurvich CM, Simonoff JS, Tsai C-L. Smoothing parameter selection in nonparametric regression using an improved Akaike information criterion. JRSS-B 1998; 60:271-293.
8. Kish L. Survey Sampling. Wiley: New York, 1995.
9. Hens N, Bruckers L, Arbyn M, Aerts M, Molenberghs G. Classification tree analysis of cervix cancer screening in the Belgian health interview survey. Archives of Public Health 2002; 60:275-294.
10. Akaike H. Information theory and an extension of the maximum likelihood principle. In 2nd International Symposium on Information Theory, Csaki F, Petrov BN (eds). Akademia Kiado: Budapest, 1973; 267-281.
11. Takeuchi K. Discussion of informational statistics and a criterion for model fitting. Suri-Kagaku 1976; 153:12-18.
12. Schwarz G. Estimating the dimension of a model. Annals of Statistics 1978; 6:461-464.
13. Spiegelhalter DJ, Best NG, Carlin BP, van der Linde A. Bayesian measures of model complexity and fit. JRSS-B 2002; 64(4):583-639.
14. Flanders WD, Greenland S. Analytic methods for two-stage case-control studies and other stratified designs. Statistics in Medicine 1991; 10:739-747.
15. Zhao LP, Lipsitz S. Design and analysis of two-stage studies. Statistics in Medicine 1992; 11:769-782.
16. Agostinelli C. Robust model selection in regression via weighted likelihood methodology. Statistics and Probability Letters 2002; 56(3):289-300.
17. Reilly M, Pepe M. The relationship between Hot-Deck multiple imputation and weighted likelihood. Statistics in Medicine 1997; 16:5-19.
18. Hurvich CM, Tsai C-L. Regression and time series model selection in small samples. Biometrika 1989; 76:297-307.
19. Burnham KP, Anderson DR. Model Selection and Multimodel Inference: A Practical Information-Theoretic Approach. Springer-Verlag: New York, 2002.
20. Simonoff JS. Smoothing Methods in Statistics. Springer: New York, 1996.
21. R Development Core Team. R: A Language and Environment for Statistical Computing. R Foundation for statistical computing, Vienna, Austria. ISBN 3-900051-00-3, URL http://www.R-project.org, 2004.
22. Wood S. mgcv: Gams and generalized ridge regression for r. R News 2001; 1(2):20-25.
23. Nishii R. Asymptotic properties of criteria for selection of variables in multiple regression. Annals of Statistics 1984; 12:758-765.
24. Rotnitzky A, Robins J. Semiparametric regression estimation in the presence of dependent censoring. Biometrika 1995; 82:805-820.
25. Wahba G. Spline Models for Observational Data. CBMS-NSF Series. SIAM: Philadelphia, PA, 1990.
26. Breiman L. Random forests. Machine Learning 2001; 45(1):5-32.
27. Pan W. Akaike's information criterion in generalized estimating equations. Biometrics 2001; 57:120-125.
28. Pan W. Model selection in estimating equations. Biometrics 2001; 57:529-534.
29. Aerts M, Claeskens G, Hart J. Testing the fit of a parametric function. Journal of the American Statistical Association 1999; 94:869-879.
30. Agostinelli C, Markatou M. Test of hypotheses based on the weighted likelihood methodology. Statistica Sinica 2001; 44:499-514.

[^0]:    *Correspondence to: N. Hens, Center for Statistics, Universiteit Hasselt, Campus Diepenbeek, Agoralaan— Gebouw D, B-3590 Diepenbeek, Belgium.
    ${ }^{\dagger}$ E-mail: niel.hens@uhasselt.be
    Contract/grant sponsor: Belgian Government (Belgian Science Policy); contract/grant number: P5/24

