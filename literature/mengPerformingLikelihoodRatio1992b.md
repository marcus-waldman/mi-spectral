---
citekey: mengPerformingLikelihoodRatio1992b
item_type: article
authors: 'Meng, Xiao-Li and Rubin, Donald B.'
year: 1992
title: Performing Likelihood Ratio Tests with Multiply-Imputed Data Sets
venue: Biometrika
volume: 79
issue: 1
pages: 103--111
doi: 10.1093/biomet/79.1.103
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\meng_performing_likelihood_ratio_1992.pdf'
pdf_sha256: c23fff42e15eaf4d46d8e9b117a9b2e9972ce4c62503c2105496a09fdac10a89
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T23:01:52Z
---
## OXFORD JOURNALS

## OXFORD UNIVERSITY PRESS

Performing Likelihood Ratio Tests with Multiply-Imputed Data Sets
Author(s): Xiao-Li Meng and Donald B. Rubin
Source: Biometrika, Mar., 1992, Vol. 79, No. 1 (Mar., 1992), pp. 103-111
Published by: Oxford University Press on behalf of Biometrika Trust
Stable URL: https://www.jstor.org/stable/2337151

## REFERENCES

Linked references are available on JSTOR for this article:
https://www.jstor.org/stable/2337151?seq=1\&cid=pdf-
reference\#references_tab_contents
You may need to log in to JSTOR to access the linked references.

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about TSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms \& Conditions of Use, available at https://about.jstor.org/terms

# Performing likelihood ratio tests with multiply-imputed data sets 

By XIAO-LI MENG<br>Department of Statistics, University of Chicago, Chicago, Illinois 60637, U.S.A.<br>AND DONALD B. RUBIN<br>Department of Statistics, Harvard University, Cambridge, Massachusetts 02138, U.S.A.


#### Abstract

Summary Existing procedures for obtaining significance levels from multiply-imputed data either (i) require access to the completed-data point estimates and variance-covariance matrices, which may not be available in practice when the dimensionality of the estimand is high, or (ii) directly combine $p$-values with less satisfactory results. Taking advantage of the well-known relationship between the Wald and log likelihood ratio test statistics, we propose a complete-data log likelihood ratio based procedure. It is shown that, for any number of multiple imputations, the proposed procedure is equivalent in large samples to the existing procedure based on the point estimates and the variance-covariance matrices, yet it only requires the point estimates and evaluations of the complete-data log likelihood ratio statistic as a function of these estimates and the completed data. The proposed procedure, therefore, is especially attractive with highly multiparameter incom-plete-data problems since it does not involve the computation of any matrices.


Some key words: Hypothesis testing; Incomplete data; Missing data; $p$-values; Significance levels; Wald test statistic.

## 1. Introduction

Multiple imputation, first proposed by Rubin (1978) and expounded upon by Rubin (1987), is a general statistical technique for handling missing data. It is particularly suited for handling nonresponse in large public-use sample surveys. The key idea, in contrast to single imputation, is to replace each missing value with a set of plausible values, thereby creating multiple completed data sets. Each of these resulting completed data sets is then analyzed using standard complete-data methods. The repeated analyses corresponding to one model for the missing data are combined to create one repeatedimputation inference, which takes proper account of the uncertainty due to missing data under that model. Repeated-imputation inferences across different models are contrasted to reveal sensitivity of inference to posited reasons for the missing data. In this and other ways, multiple imputation retains the major advantages yet rectifies the major disadvantages inherent in single imputation.

Combining the complete-data analyses within a model is usually straightforward. For example, the combined estimate is simply the average of the completed-data estimates. The variability associated with this combined estimate is the sum of two components: the within-imputation variance, i.e. the average of completed-data variance estimates, and the between-imputation component, i.e. the sample variance of the completed-data
estimates. Significance levels can be obtained by computing a modified Wald test statistic from the quantities mentioned above, which is then referred to an $F$ distribution. This procedure has been recently evaluated comprehensively in large samples by Li , Raghunathan \& Rubin (1991), with the conclusion that it is essentially calibrated and the loss of power due to a finite number of imputations is quite modest in cases likely to occur in practice. A brief summary of these standard multiple imputation results is presented in § 2.

The procedure studied by Li et al. (1991) requires access to the completed-data estimates and their covariance matrices, and the latter may not be available in practice with standard computer packages, especially when the dimensionality of the estimand is high, such as can occur with partially classified multidimensional contingency tables. Motivated by the well-known relationship between the Wald test statistic and the log likelihood ratio test statistic, we propose a complete-data log likelihood ratio based procedure in § 3. The proposed procedure is equivalent in large samples to the previous one, yet it only requires evaluations of the complete-data log likelihood ratio statistic as a function of parameter estimates for each data set completed by multiple imputation. The computer code for complete-data log likelihood ratio statistics is part of many standard completedata routines. A numerical example is presented in § 4 to illustrate the implementation of the new procedure. Unless otherwise noted, the appropriate reference for definitions and concepts is Rubin (1987), primarily Chapters 3 and 4.

## 2. Notation and background

## 2-1. Large-sample hypothesis testing with complete data

Let $X$ be the $n \times p$ complete-data matrix, with associated density $f(X \mid \psi)$ indexed by the $h$-dimensional vector parameter $\psi$. Suppose in a particular analysis the parameter of primary interest, $\theta$, is a $k$-dimensional vector function of $\psi$. Let $\hat{\psi}=\hat{\psi}(X)$ be an efficient estimate, e.g. maximum likelihood estimate, of $\psi$ and let $\hat{\theta}=\hat{\theta}(X)$ be an efficient estimate of $\theta$ with $U=U(X)$ as the associated covariance matrix. With large samples, a common approximation that is acceptable to both Bayesians and frequentists is

$$
U^{-\frac{1}{2}}(\hat{\theta}-\theta) \sim N(0, I),
$$

where the sampling distribution of $U$ has lower-order variability than that of $\hat{\theta}$. Consequently, a $p$-value for the null value of $\theta$, which without loss of generality we take to be zero, can be obtained as $p=\operatorname{pr}\left(\chi_{k}^{2}>d\right)$, where

$$
d=d(\hat{\theta}, U)=\hat{\theta}^{\mathrm{T}} U^{-1} \hat{\theta}
$$

is known as the Wald $\chi^{2}$ test statistic.
It is well known that, under standard regularity conditions, $d$ is asymptotically equivalent to the log likelihood ratio statistic $d^{\prime}$, which can be written as

$$
d^{\prime}=d^{\prime}\left(\hat{\psi}_{0}, \hat{\psi} \mid X\right)=2 \log \frac{f(X \mid \hat{\psi})}{f\left(X \mid \hat{\psi}_{0}\right)}
$$

where $\hat{\psi}_{0}=\hat{\psi}_{0}(X)$ is an efficient estimate of $\psi$ under $f(X \mid \psi ; \theta=0)$, that is, with $\psi$ restricted to lie in the $h-k$ dimensional subspace defined by $\theta=0$. The basis of this equivalence is the $h$ dimensional asymptotic normality of $(\psi-\hat{\psi})$, which we assume in addition to (2/1).

### 2.2. Hypothesis testing with multiply-imputed data based on moments

With incomplete data, write $X=\left(X_{\text {obs }}, X_{\text {mis }}\right)$, where $X_{\text {obs }}$ is the observed part of $X$ and $X_{\text {mis }}$ is the missing part. Using proper imputation methods, such as using independent draws from the posterior predictive distribution $f\left(X_{\text {mis }} \mid X_{\text {obs }}\right)$, one can create $m$ imputations, $X_{* \text { mis }}^{(l)}(l=1, \ldots, m)$ for the missing values $X_{\text {mis }}$, and thereby create $m$ corresponding completed data sets

$$
\left\{X_{*}^{(l)} ; l=1, \ldots, m\right\}=\left\{\left(X_{\mathrm{obs}}, X_{* \mathrm{mis}}^{(l)}\right) ; l=1, \ldots, m\right\} .
$$

Standard complete-data methods then can be applied to compute the set of complete-data moments, i.e. estimates and covariance matrices:

$$
S_{m}=\left\{\hat{\theta}_{* l} \equiv \hat{\theta}\left(X_{*}^{(l)}\right), U_{* l} \equiv U\left(X_{*}^{(l)}\right) ; l=1, \ldots, m\right\}
$$

The resulting estimate of $\theta$ is

$$
\bar{\theta}_{m}=\frac{1}{m} \sum_{l=1}^{m} \hat{\theta}_{* l}
$$

with associated variability

$$
T_{m}=\bar{U}_{m}+\left(1+m^{-1}\right) B_{m},
$$

where

$$
\bar{U}_{m}=\frac{1}{m} \sum_{l=1}^{m} U_{* l}
$$

measures the within imputation variability, and

$$
B_{m}=\frac{1}{m-1} \sum_{l=1}^{m}\left(\hat{\theta}_{* l}-\bar{\theta}_{m}\right)\left(\hat{\theta}_{* l}-\bar{\theta}_{m}\right)^{\mathrm{T}}
$$

measures the between imputation variability.
Although hypothesis testing based on $S_{m}$ can be accomplished directly by forming a Wald type statistic using $\bar{\theta}_{m}$ and $T_{m}$, such a procedure does not provide satisfactory results when the dimensionality of $\theta$ is substantially larger than the number of multiple imputations because of the deficient rank of $B_{m}$. One way to avoid this problem, which typically occurs in practice, is to assume equal fractions of missing information, that is, to assume that the proportional loss of information is the same for all components of $\theta$. Under this assumption, the Wald type statistic is proportional to

$$
D_{m}=\frac{\bar{\theta}_{m}^{\mathrm{T}} \bar{U}_{m}^{-1} \bar{\theta}_{m}}{k\left(1+r_{m}\right)}
$$

where

$$
r_{m}=\left(1+m^{-1}\right) \operatorname{tr}\left(B_{m} \bar{U}_{m}^{-1}\right) / k
$$

is the estimated average odds ratio of the fractions of missing information. The exact distribution of $D_{m}$ is intractable, but it can be approximated well by an $F$ distribution on $k$ and $w$ degrees of freedom, where the best choice of $w$ thus far is given by Li et al. (1991):

$$
w=w\left(r_{m}\right)= \begin{cases}4+(v-4)\left\{1+\left(1-\frac{1}{2} v\right) r_{m}^{-1}\right\}^{2} & \text { if } v=k(m-1)>4, \\ \frac{1}{2} v(1+1 / k)\left(1+r_{m}^{-1}\right)^{2} & \text { otherwise. }\end{cases}
$$

Major conclusions of Li et al. (1991) are that, in cases of practical interest, this procedure with $m \geqslant 3$ is insensitive to the assumption of equal fractions of missing information, is well calibrated, and suffers only modest loss of power relative to the ideal likelihood ratio test based directly on $X_{\text {obs }}$.

### 2.3. Hypothesis testing with multiply-imputed data based on $\chi^{2}$ statistics

The use of significance levels rather than interval estimates is especially useful and common in models with many parameters. In these cases, however, a standard completedata analysis often does not provide the entire $k \times k$ variance-covariance matrix $U(X)$, but rather a scalar $p$-value, or equivalently, the $\chi^{2}$ statistic, for the null value of $\theta$. Thus, the repeated complete-data computations may not provide the set of the completed-data moments $S_{m}$ defined in (2•4), but instead, the set of the completed-data Wald $\chi^{2}$ statistics

$$
S_{d}=\left\{d_{* l} \equiv d\left(\hat{\theta}_{* l}, U_{* l}\right) ; l=1, \ldots, m\right\}
$$

where the function $d$ is defined in (2.2), or equivalenty the set of the completed-data log likelihood ratio statistics

$$
S_{d^{\prime}}=\left\{d_{* l}^{\prime} \equiv d^{\prime}\left(\hat{\psi}_{0 * l}, \hat{\psi}_{* l} \mid X_{*}^{(l)}\right) ; l=1, \ldots, m\right\}
$$

where the $d^{\prime}$ function is defined in (2•3), $\hat{\psi}_{0 * l}=\hat{\psi}_{0}\left(X_{*}^{(l)}\right)$ and $\hat{\psi}_{* l}=\hat{\psi}\left(X_{*}^{(l)}\right)$. Clearly, in these cases, the procedure given by $(2 \cdot 5)-(2 \cdot 7)$ cannot be applied directly to obtain significance levels.

A key representation in developing procedures for obtaining significance levels based on $S_{d}$ or $S_{d^{\prime}}$ is

$$
D_{m} \bumpeq \hat{D}_{m} \equiv\left(\frac{\bar{d}_{m}}{k}-\frac{m-1}{m+1} r_{m}\right) /\left(1+r_{m}\right)
$$

where $\bar{d}_{m}$ is the average of $\left\{d_{* l} ; l=1, \ldots, m\right\}$, and $A \bumpeq B$ means $A=B+o(1)$ almost surely. Thus, since $d_{* l} \bumpeq d_{* l}^{\prime}$, asymptotically,

$$
D_{m} \bumpeq \hat{D}_{m}^{\prime} \equiv\left(\frac{\bar{d}_{m}^{\prime}}{k}-\frac{m-1}{m+1} r_{m}\right) /\left(1+r_{m}\right)
$$

where $\bar{d}_{m}^{\prime}$ is the average of $\left\{d_{* l}^{\prime} ; l=1, \ldots, m\right\}$. Notice that the only quantity in(2•8) or (2.9) that is not directly obtainable from $S_{d}$ or $S_{d^{\prime}}$ is $r_{m}$ of (2.6). Replacing $r_{m}$ with estimates based on $S_{d}$ or $S_{d^{\prime}}$ gives a set of procedures for computing $p$-values when only $S_{d}$ or $S_{d^{\prime}}$ is available. The simplest and best replacement so far is given by Li , Meng, Raghunathan \& Rubin (1991),

$$
\hat{r}_{d}=\left(1+m^{-1}\right)\left\{\sum_{l=1}^{m} d_{* l}-\left(\sum_{l=1}^{m} d_{* l}^{\frac{1}{2}}\right)^{2} / m\right\} /(m-1)
$$

with corresponding test statistic

$$
\hat{D}_{d}=\left(\frac{\bar{d}_{m}}{k}-\frac{m-1}{m+1} \hat{r}_{d}\right) /\left(1+\hat{r}_{d}\right)
$$

which is then referred to the distribution $F_{k, a w_{s}}$, where $w_{s}=(m-1)\left(1+\hat{r}_{d}^{-1}\right)^{2}$ and $a=k^{-3 / m}$. The analogue $\hat{D}_{d^{\prime}}$ replaces $d_{* l}$ with $d_{* l}^{\prime}$ wherever applicable, and thus $\hat{D}_{d^{\prime}} \bumpeq \hat{D}_{d}$.

Although the procedures based on $S_{d}$ or $S_{d^{\prime}}$ are calibrated reasonably well in many cases of practical importance, they are distinctly inferior to procedures based on $S_{m}$, and the loss of power can be severe, especially when $k$ is large and $m$ is small. This degradation in performance is not surprising and will occur for any procedure based only on $S_{d}$ or $S_{d^{\prime}}$, because of the extreme loss of information when going from $S_{m}$ to $S_{d}$ or $S_{d^{\prime}}$. Clearly, the only way to overcome this inherent difficulty is to obtain more information. In the next section we show how to combine $S_{d}$ or $S_{d^{\prime}}$ with the set of estimates

$$
S_{e}=\left\{\left(\hat{\psi}_{* l}, \hat{\psi}_{0 * l}\right) ; l=1, \ldots, m\right\}
$$

to obtain a valid $p$-value, assuming access to the computer code that calculates the complete-data log likelihood ratio statistic as a function of the parameter estimates at each completed-data set. The new test statistic is not only asymptotically equivalent to the practically satisfactory statistic $D_{m}$ for any $m \geqslant 2$, but also can require much less computation because it calculates neither the complete-data variance-covariance matrices $U_{* l}(l=1, \ldots, m)$ nor the between covariance matrix $B_{m}$.

## 3. Complete-data log likelihood ratio based procedure

## 3•1. An intermediate procedure

Because the numerator of $D_{m}$ in (2.5) is the simple quadratic form $\bar{d}\left(\bar{\theta}_{m}, \bar{U}_{m}\right)= \bar{\theta}_{m}^{\mathrm{T}} \bar{U}_{m}^{-1} \bar{\theta}_{m}$, from (2•5), (2•8) and (2•9), we have

$$
r_{m} \bumpeq \frac{m+1}{k(m-1)}\left\{\bar{d}_{m}-d\left(\bar{\theta}_{m}, \bar{U}_{m}\right)\right\} \bumpeq \frac{m+1}{k(m-1)}\left\{\bar{d}_{m}^{\prime}-d\left(\bar{\theta}_{m}, \bar{U}_{m}\right)\right\} .
$$

Since $r_{m}$ is the only quantity needed for computing the denominator of $D_{m}$, we can obtain $D_{m}$ from the scalar $\bar{d}_{m}$ or $\bar{d}_{m}^{\prime}$ and the scalar distance $d\left(\bar{\theta}_{m}, \bar{U}_{m}\right)$.

Under the lower order variability assumption of $U, \bar{U}_{m} \bumpeq U_{* l}$ for any $l$. Thus, if we have access to the Wald test statistic $d\left(\theta_{* l}, U_{* l}\right)$ as a function of $\theta_{* l}$ at any completed data set, we can replace $d\left(\bar{\theta}_{m}, \bar{U}_{m}\right)$ in (3•1) by any $d\left(\bar{\theta}_{m}, U_{* l}\right)$, or more efficiently by their average

$$
\bar{d}_{w}=\frac{1}{m} \sum_{l=1}^{m} d\left(\bar{\theta}_{m}, U_{* l}\right)
$$

The corresponding test statistic then can be constructed as

$$
D_{w}=\frac{\bar{d}_{w}}{k\left(1+r_{w}\right)} \bumpeq D_{m},
$$

where

$$
r_{w}=\frac{m+1}{k(m-1)}\left(\bar{d}_{m}-\bar{d}_{w}\right)
$$

### 3.2. Motivation for the new procedure

The calculation of $\bar{d}_{w}$ in (3.2) requires access to the Wald test statistic in each completed-data set as a function of the estimate of $\theta$, but the well-known asymptotic equivalence between the Wald and log likelihood ratio test statistics suggests that we can compute $d\left(\bar{\theta}_{m}, \bar{U}_{m}\right)$ assuming access to the function $d^{\prime}\left(\hat{\psi}_{0}, \psi \mid X\right)$, defined in (2•3). An important but subtle distinction, however, is that although with the Wald test statistic
we can replace $d\left(\bar{\theta}_{m}, \bar{U}_{m}\right)$ by any $d\left(\bar{\theta}_{m}, U_{* l}\right)$, with the log likelihood ratio test statistic, we must average all $m$ values. That is, even though $d^{\prime}\left(\hat{\psi}_{0 * l}, \hat{\psi}_{* l} \mid X_{*}^{(l)}\right) \bumpeq d\left(\hat{\theta}_{* l}, U_{* l}\right)$ for each $l$, the analogous replacement of average estimates in $d^{\prime}$ does not work:

$$
d^{\prime}\left(\bar{\psi}_{0 m}, \bar{\psi}_{m} \mid X_{*}^{(l)}\right) \neq d\left(\bar{\theta}_{m}, U_{* l}\right)
$$

for any $l$, where $\bar{\psi}_{0 m}$ and $\bar{\psi}_{m}$ are the averages of $\left\{\hat{\psi}_{0 * l} ; l=1, \ldots, m\right\}$ and $\left\{\hat{\psi}_{* l} ; l=1, \ldots, m\right\}$, respectively. Rather, asymptotically, with a quadratic complete-data log likelihood function,

$$
d^{\prime}\left(\bar{\psi}_{0 m}, \bar{\psi}_{m} \mid X_{*}^{(l)}\right)=d\left(\hat{\theta}_{* l}, U_{* l}\right)-d\left(\hat{\theta}_{* l}-\bar{\theta}_{m}, U_{* l}\right)
$$

which generally does not equal $d\left(\bar{\theta}_{m}, U_{* l}\right)$ unless there is no missing information. Their average, however, does equal $\bar{d}_{w}$ asymptotically because

$$
\bar{d}_{L} \equiv \frac{1}{m} \sum_{l=1}^{m} d^{\prime}\left(\bar{\psi}_{0 m}, \bar{\psi}_{m} \mid X_{*}^{(l)}\right) \bumpeq d\left(\bar{\theta}_{m}, \bar{U}_{m}\right)
$$

Equation (3•5) follows from viewing the log likelihood ratio $d^{\prime}\left(\bar{\psi}_{0 m}, \bar{\psi}_{m} \mid X_{*}^{(l)}\right)$ as the log ratio of an $h$-variate normal density with mean $\hat{\psi}_{* l}$, where the numerator is evaluated at $\bar{\psi}_{0 m}$ and the denominator at $\bar{\psi}_{m}$. The key observation is that, without loss of generality, $\psi$ can be taken such that $\hat{\psi}_{* l}-\hat{\psi}_{0 * l}=\left(\hat{\theta}_{* l}, 0\right)^{\mathrm{T}}$, where the two components of $\psi$ are orthogonal, and the first component, $\theta$, has covariance $U_{* l}$ and $\hat{\theta}_{0 * l}=0$. The right-hand side of (3.6) follows from (3.5) by viewing $\Sigma d\left(\hat{\theta}_{* l}, U_{* l}\right) \bumpeq \Sigma d\left(\hat{\theta}_{* l}, \bar{U}_{m}\right)$ as a total sum of squares decomposed into an $m-1$ degrees of freedom sum of squares about the mean, $\Sigma d\left(\hat{\theta}_{* 1}-\bar{\theta}_{m}, \bar{U}_{m}\right)$, and a one degree of freedom sum of squares for the mean, $d\left(\bar{\theta}_{m}, \bar{U}_{m}\right)$.

### 3.3. Definition and computation of the new procedure

Because $\bar{d}_{L} \bumpeq \bar{d}_{w}$, in view of (3•3) and (3•4), we define our new test statistic as

$$
D_{L}=\frac{\bar{d}_{L}}{k\left(1+r_{L}\right)},
$$

where

$$
r_{L}=\frac{m+1}{k(m-1)}\left(\bar{d}_{m}^{\prime}-\bar{d}_{L}\right)
$$

Since for any $m \geqslant 2, D_{L} \bumpeq D_{m}$ and $r_{L} \bumpeq r_{m}$, an obvious approximate reference distribution for $D_{L}$ is $F_{k, w\left(r_{L}\right)}$, where the $w(r)$ function is defined in (2•7).

To compute $D_{L}$, first assume we have $S_{e}$ and $S_{d^{\prime}}$, as well as access to the complete-data $\log$ likelihood ratio function $d^{\prime}$ used to compute $d_{* l}^{\prime}(l=1, \ldots, m)$. From $S_{e}$ we calculate the average estimates $\bar{\psi}_{0 m}$ and $\bar{\psi}_{m}$, and from $S_{d^{\prime}}$ we calculate $\bar{d}_{m}^{\prime}$, the average of $\left\{d_{* l}^{\prime} ; l=1, \ldots, m\right\}$. Then, we make a second pass through the completed data, using $\bar{\psi}_{0 m}$ and $\bar{\psi}_{m}$ to calculate the $m$ scalar quantities $d^{\prime}\left(\bar{\psi}_{0 m}, \bar{\psi}_{m} \mid X_{*}^{(l)}\right)$, and their average, $\bar{d}_{L}$, defined in (3.6). In most practical applications, the complete-data density $f(X \mid \psi)$ is from an exponential family so that $d^{\prime}\left(\psi_{0}, \psi \mid X\right)$ is linear in the complete-data sufficient statistics, and thus $\bar{d}_{L}$ is the complete-data log likelihood ratio statistic evaluated at the average parameter estimates ( $\bar{\psi}_{0 m}, \bar{\psi}_{m}$ ) and at the average completed-data sufficient statistics. Having obtained $\bar{d}_{m}^{\prime}$ and $\bar{d}_{L}$, we apply (3.8) to compute $r_{L}$, and then apply
(2•7) and (3•7) to compute $w\left(r_{L}\right)$ and $D_{L}$, respectively. Finally, we obtain the significance level $p=\operatorname{pr}\left\{F_{k, w\left(r_{L}\right)}>D_{L}\right\}$.

## 4. Example

## 4•1. Likelihood ratio tests for complete contingency tables

In the analysis of contingency tables, it is very common to test whether the cell probabilities $\left\{\pi_{i j k . . t}\right\}$ have a special structure corresponding to a parsimonious model. For example, such null models often specify conditional independence of some factors given other factors. With complete data, that is, when each case can be classified into one cell, performing the likelihood ratio test is straightforward. Let $\hat{\pi}_{c}$ and $\hat{\pi}_{0 c}$ be the maximum likelihood estimates of the cell probability for cell $c$ under the saturated and null models, respectively. Then the log likelihood ratio statistic is

$$
d^{\prime}=2 \sum_{c} n_{c} \log \left(\hat{\pi}_{c} / \hat{\pi}_{0 c}\right),
$$

where the summation is over all the cells $c$ in the table, $n_{c}=N \hat{\pi}_{c}$ is the observed count in cell $c$, and $N=\Sigma_{c} n_{c}$ is the total count. When the null model is true, $d^{\prime}$ is distributed asymptotically as a chi-squared random variable with degrees of freedom equal to the number of independent restrictions on the cell probabilities under the null model (Bishop, Fienberg \& Holland, 1975, p. 114).

## 4•2. Creating multiple imputations for a partially classified table

In the presence of missing data, some cases are only partially classified, as illustrated in Table 1 taken from Little \& Rubin (1987, Table 9.8). Applying the em algorithm to find the maximum likelihood estimates for the cell probabilities under the null model and then performing likelihood ratio tests, Little \& Rubin (1987, p. 192) considered several models for these data in Table 1 assuming the missing data are missing at random (Rubin, 1976). As an alternative approach, we can use multiple imputation and then apply our new procedure $D_{L}$ to find the significance level without the need for a covariance matrix for the parameters, as with the moment-based procedure $D_{m}$.

The implementation of multiple imputation is particularly simple with a saturated model for a table having a monotone missing data pattern; even for nonmonotone patterns, data augmentation (Tanner \& Wong, 1987) makes such multiple imputation

Table 1. A $2^{3}$ contingency table with partially classified observations
| (a) Completely classified cases |  |  |  |  |
| :---: | :---: | :---: | :---: | :--- |
|  | Survival, $j$ |  |  |  |
| Clinic, $k$ | Prenatal care, $i$ | Died | Survived |  |
| A | Less | 3 | 176 |  |
|  | More | 4 | 293 |  |
| B | Less | 17 | 197 |  |
|  | More | 2 | 23 | $N^{(a)}=715$ cases |


(b) Partially classified cases, clinic missing
|  | Survival, $j$ |  |  |  |
| :---: | :---: | :---: | :---: | :--- |
| Clinic, $k$ | Prenatal care, $i$ | Died | Survived |  |
| $?$ | Less | 10 | 150 |  |
|  | More | 5 | 90 | $N^{(b)}=255$ cases |


straightforward though iterative. For example, for the data set in Table 1, under the noninformative Beta $(1, \ldots, 1)$ prior for the cell probabilities $\left\{\pi_{i j k}\right\}$, the $l$ th $(l=1, \ldots, m)$ imputation of the cell counts can be obtained as follows:

Step 1: Draw the conditional cell probabilities $\pi_{1 . i j}$ from Beta $\left(n_{i j 1}^{(a)}+1, n_{i j 2}^{(a)}+1\right) (i, j=1,2)$, where $n_{i j k}^{(a)}$ is the observed cell count in cell $(i, j, k)$ of the completely classified Table 1(a).
Step 2: Given the conditional probabilities $\pi_{1 . i j}(i, j=1,2)$ drawn in Step 1, draw $n_{i j 1}^{(b)}$ from Binomial ( $n_{i j+}^{(b)}, \pi_{1 \cdot i j}$ ), where $n_{i j+}^{(b)}$ is the observed counts in the marginal cell ( $i, j$ ) of the partially classified Table 1(b); let $n_{i j 2}^{(b)}=n_{i j+}^{(b)}-n_{i j 1}^{(b)}$.
Step 3: Calculate the $l$ th imputed cell count for cell $(i, j, k)$ as $n_{i j k}^{(l)}=n_{i j k}^{(a)}+n_{i j k}^{(b)} (i, j, k=1,2)$.

## 4•3. Testing null models using our new procedure

Once these $m$ completed tables are created, one can treat each as if it were the complete data, and use formula (4•1) to compute $m$ completed-data log likelihood ratio test statistics

$$
d_{* l}^{\prime}=2 \sum_{c} n_{c}^{(l)} \log \left(\hat{\pi}_{c}^{(l)} / \hat{\pi}_{0 c}^{(l)}\right) \quad(l=1, \ldots, m) .
$$

The computation of $\bar{d}_{L}$ of (3.6) involves evaluating the log likelihood ratio function at $\bar{\psi}_{m}$ and $\bar{\psi}_{0 m}$, where $\psi$ is a vector parameter providing the cell probabilities. For simplicity, we take $\psi$ to be the cell probabilities, whence $\bar{\psi}_{m}$ and $\bar{\psi}_{0 m}$ are simply the averages of cell probabilities under the saturated and null models, respectively, across the imputations. Thus, letting $\bar{\pi}_{c}$ and $\bar{\pi}_{0 c}$ be the averages of the estimated cell probabilities across imputations for cell $c$ under the saturated and null models, respectively, by (4•1),

$$
d^{\prime}\left(\bar{\psi}_{0 m}, \bar{\psi}_{m} \mid X_{*}^{(l)}\right)=2 \sum_{c} n_{c}^{(l)} \log \left(\bar{\pi}_{c} / \bar{\pi}_{0 c}\right) \quad(l=1, \ldots, m),
$$

whose average is equal to

$$
\bar{d}_{L}=2 \sum_{c} \bar{n}_{c} \log \left(\bar{\pi}_{c} / \bar{\pi}_{0 c}\right)=2 \sum_{c} \bar{n}_{c} \log \left(\bar{n}_{c} / \bar{n}_{0 c}\right),
$$

where $\bar{n}_{c}=N \bar{\pi}_{c}$ and $\bar{n}_{0 c}=N \bar{\pi}_{0 c}$.
Table 2 presents the results for testing two different null models with several choices of $m$. The conditional independence model asserts that conditional on clinic, survival and prenatal care are independent, which was Little \& Rubin's (1987) preferred parsimonious model based on their tests. The full independence model has all three factors mutually independent, and is included here for comparison. The second column gives $r_{L}$ of (3•8), the estimated average odds ratio of the fractions of missing information,

Table 2. Testing null models using $D_{L}$
|  | Conditional independence |  |  | Full independence |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $m$ | $r_{L}$ | $\boldsymbol{D}_{\boldsymbol{L}}$ | $\boldsymbol{p}$ | $r_{L}$ | $\boldsymbol{D}_{\boldsymbol{L}}$ | $\boldsymbol{p}$ |
| 2 | 0.46 | 0.06 | 0.938 | 0.70 | 41.86 | 0.000 |
| 3 | 0.32 | 0.08 | 0.927 | 0.41 | 51.12 | 0.000 |
| 5 | 0.28 | 0.02 | 0.980 | 0.26 | 56.36 | 0.000 |
| 7 | 0.26 | 0.03 | 0.966 | 0.29 | 54.35 | 0.000 |
| 10 | 0.30 | 0.08 | 0.928 | 0.34 | 52.33 | 0.000 |
| 25 | 0.32 | 0.10 | 0.905 | 0.36 | 51.97 | 0.000 |
| 50 | 0.30 | 0.09 | 0.919 | 0.37 | 50.98 | 0.000 |
| Ideal |  | 0.10 | 0.904 |  | 52.67 | 0.000 |


which, except for $m=2$, is relatively stable as $m$ increases, as we expected. The third column gives the value of the new test statistic $D_{L}$, and the fourth column gives the corresponding $p$-value using the $F$ reference distribution. The last three columns are the counterparts for the full independence model. For comparison, we include in the last row the corresponding results using the ideal likelihood ratio test based directly on the data in Table 1. It is clear from Table 2 that the tests based on $D_{L}$ reach essentially the same practical conclusions as the ideal test, even for small $m$. The satisfactory performance of these tests based on small numbers of multiple imputations is especially encouraging, because small $m$ is common in practice.

## Acknowledgements

Some of this research was done when the first author was a graduate student at Harvard University, and was supported in part by an SES NSF grant and in part by Joint Statistical Agreements between the U.S. Bureau of the Census and Harvard University. The manuscript was prepared using computer facilities supported in part by NSF grants awarded to the Department of Statistics at The University of Chicago, and by The University of Chicago Block Fund. The authors wish to thank the Editor and anonymous reviewers for helpful comments.

## References

Bishop, Y. M. M., Fienberg, S. E. \& Holland, P. W. (1975). Discrete Multivariate Analysis: Theory and Practice. Cambridge, MA: MIT Press.
Li, K. H., Meng, X. L., Raghunathan, T. E. \& Rubin, D. B. (1991). Significance levels from repeated $p$-values with multiply-imputed data. Statistica Sinica 1, 65-92.
Li, K. H., Raghunathan, T. E. \& Rubin, D. B. (1991). Large sample significance levels from multiplyimputed data using moment-based statistics and an $F$ reference distribution. J. Am. Statist. Assoc. 86, 1065-73.
Little, R. J. A. \& Rubin, D. B. (1987). Statistical Analysis with Missing Data. New York: Wiley.
Rubin, D. B. (1976). Inference and missing data. Biometrika 63, 581-92.
Rubin, D. B. (1978). Multiple imputations in sample surveys-a phenomenological Bayesian approach to nonresponse. In Proc. Survey Res. Meth. Sect., Am. Statist. Assoc., pp. 20-34. Also in Imputation and Editing of Faulty or Missing Survey Data, pp. 1-23. U.S. Dept. of Commerce, Bureau of the Census.
Rubin, D. B. (1987). Multiple Imputation for Nonresponse in Sample Surveys. New York: Wiley.
Tanner, M. A. \& Wong, W. H. (1987). The calculation of posterior distributions by data augmentation. J. Am. Statist. Assoc. 82, 805-11.
[Received October 1990. Revised August 1991]

