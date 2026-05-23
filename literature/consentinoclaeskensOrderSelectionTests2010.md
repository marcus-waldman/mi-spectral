---
citekey: consentinoclaeskensOrderSelectionTests2010
item_type: article
authors: 'Consentino, Fabrizio and Claeskens, Gerda'
year: 2010
title: Order Selection Tests with Multiply Imputed Data
venue: 'Computational Statistics \&amp; Data Analysis'
volume: 54
issue: 10
pages: 2284--2295
doi: 10.1016/j.csda.2010.04.009
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\consentino_order_selection_tests_2010.pdf'
pdf_sha256: 5604c4a41725f962cccfb89826418e1af436036e764da76ac4b754e9067b83b2
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-23T00:46:05Z
---
# Order selection tests with multiply imputed data 

Fabrizio Consentino, Gerda Claeskens*<br>ORSTAT and Leuven Statistics Research Center, K.U. Leuven, 3000 Leuven, Belgium

## ARTICLE INFO

## Article history:

Received 2 April 2009
Received in revised form 8 April 2010
Accepted 8 April 2010
Available online 21 April 2010

## Keywords:

Akaike information criterion
Hypothesis test
Multiple imputation
Lack-of-fit test
Missing data
Omnibus test
Order selection


#### Abstract

Nonparametric tests for the null hypothesis that a function has a prescribed form are developed and applied to data sets with missing observations. Omnibus nonparametric tests such as the order selection tests, do not need to specify a particular alternative parametric form, and have power against a large range of alternatives. More specifically, likelihood-based order selection tests are defined that can be used for multiply imputed data when the data are missing-at-random. A simulation study and data analysis illustrate the performance of the tests. In addition, an Akaike information criterion for model selection is presented that can be used with multiply imputed datasets.


© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Testing the lack-of-fit of a parametric function is well-studied. Several types of tests exist, ranging from fully parametric tests, to semiparametric and nonparametric omnibus tests. For an overview of nonparametric tests, see Hart (1997). In settings with missing data, testing for lack-of-fit is more complicated. González-Manteiga and Pérez-González (2006) developed a test based on local linear estimators for a linear regression model with missing response values but a completely observed covariate. We address in particular lack-of-fit tests for missing data situations where multiple imputation is applied. We will focus on a class of smoothing-based tests that use the idea of order selection. Our tests are applicable in parametric likelihood models and are not restricted to linear models.

Eubank and Hart (1992) introduced the order selection test in linear regression models. The idea is to test the shape of a parametric function, most often the mean of the response, by considering not a single one, but a sequence of alternative models. These alternative models are constructed by means of a series expansion of the function of interest around the hypothesized null model. A data-driven method is then applied to select the "order" of the alternative model. That is, in the sequence of alternative models, a method such as Akaike's information criterion AIC (Akaike, 1973) will select the most appropriate one. If the selected model coincides with the null model, the test does not reject the null hypothesis. However, if a model different from the null model is selected, the test will reject the null hypothesis. In those instances, the order of the chosen model, that is, the number of parameters in the model, exceeds that of the null model. Written in another way, this test statistic takes the form of a maximum of weighted likelihood ratio statistics, which clearly indicates the omnibus, or nonparametric nature of the test.

By using such a series expansion the class of alternative models is large and is not restricted to a single specified alternative. For example, if we would just test a linear versus a quadratic fit we would miss out on high frequency alternatives for which the quadratic term happens to be zero. Instead, we are interested in the development of tests that are sensitive to essentially any departure from the null hypothesis.

[^0]The original order selection tests are extended towards testing in general likelihood models by Aerts et al. (1999) and to multiple regression models by Aerts et al. (2000). Recently, these tests have been studied for inverse regression problems by Bissantz et al. (2009). Test statistics can be based on likelihood ratio, Wald statistics, or score statistics. All of these methods are based on completely observed data.

In practice, many data sets contain one or more missing observations. We refer to Little and Rubin (2002) for an overview of methods to deal with such data. Throughout the paper we make the assumption that the data are missing-at-random; this means that the missingness depends only on the observed data. Most research focuses on the estimation under missingness. Multiple imputation methods are particularly attractive since once values are imputed, traditional, complete case methods can be applied to filled-in data sets. Single imputation, where unknown observations are each replaced by a single value, risks understating uncertainty. Inference is generally improved by imputing values several, say $m$ times, creating $m$ complete data sets, with $m=5$ a typical choice based on coverage properties seen in simulation studies. Li et al. (1991a) considered hypothesis testing in this setting. In particular, for a parametric null hypothesis of the form $\theta=\theta_{0}$, with an alternative of the form $\theta \neq \theta_{0}$, they construct a Wald test by combining the results of $m$ Wald tests, one for each of the $m$ imputed data sets. They show that the distribution of such a test statistic can be approximated by that of an $F$-distribution with degrees of freedom that depend on the fraction of missing information. Meng and Rubin (1992) extend this idea to combining $m$ likelihood ratio tests. Recently, Reiter (2007) obtained an alternative approximation to the degrees of freedom for such combined Wald test statistics that should work better for small samples.

The main idea of this paper is to use the combined likelihood ratio tests for the $m$ imputed data sets to perform order selection. In this way, we enlarge the testing power by not considering a single parametric test, since order selection tests are constructed to be powerful against a wide range of alternative models. This creates a straightforward to use lack-of-fit test in the setting of missing data.

Section 2 defines the order selection test first for complete data, and then proposes the new test for the case of multiply imputed data sets. Sections 3 and 4 apply the test to a data example and in a simulation study. A version of Akaike's information criterion that works with multiply imputed datasets is obtained in Section 5 . Section 6 presents some extensions of the proposed method.

## 2. The order selection test

### 2.1. A model sequence for order selection

We consider a set of data $\boldsymbol{Z}_{i}=\left(Y_{i}, x_{i}\right), i=1, \ldots, n$ with joint density depending on a function $\gamma(\cdot)$ of interest (most often this is the mean response, conditional on covariates) and on some other nuisance parameters $\boldsymbol{\eta}$ (such as an unknown variance). We wish to test the hypothesis

$$
H_{0}: \gamma(\cdot) \in \mathcal{G}=\left\{\gamma\left(\cdot, \boldsymbol{\beta}_{p}\right): \boldsymbol{\beta}_{p}=\left(\beta_{0}, \ldots, \beta_{p}\right) \in \Theta\right\},
$$

where the parameter space $\Theta \subset \mathbb{R}^{p+1}$. A simple example is to test for linearity of the mean response, that is, $E(Y \mid x)= \gamma\left(x, \boldsymbol{\beta}_{1}\right)=\beta_{0}+\beta_{1} x$. In a parametric hypothesis testing procedure, a specific parametric model would be stated for the alternative hypothesis. In nonparametric or omnibus testing, this is avoided by constructing a sequence of alternative models. These alternatives could be quite general. For regression models, following the approach of Aerts et al. (1999), we focus on additive series expansions of the true underlying function $\gamma(\cdot)$ around the null model. For convenience, we use $r=0$ to index the null model in (1), and we define for $r=0,1,2, \ldots$,

$$
\gamma\left(x ; \beta_{0}, \ldots, \beta_{p+r}\right)=\gamma\left(x ; \beta_{0}, \ldots, \beta_{p}\right)+\sum_{j=1}^{r} \beta_{p+j} \psi_{j}(x),
$$

where the basis functions $\psi_{j}(\cdot)$ are known functions. Most often these functions are taken to be (orthogonalized) polynomials, Legendre polynomials, cosine functions or wavelet functions. For all further analysis, we consider functions $\psi_{j}$ that are not already used in the null model. For example, a polynomial expansion to test whether the mean $E(Y \mid X= x)=\beta_{0}+\beta_{1} x$, will take for $\psi_{1}(x)$ an (orthogonalized) quadratic function, for $\psi_{2}(x)$ a cubic function, etc. The reason for starting with a quadratic function is that the constant and linear function are already included in the null model.

In practice it is not possible to include an infinite number of terms in the series expansion in (2). The series will be truncated at a value $R_{n}$ that might depend on the size of the dataset, in particular it always holds that $R_{n}$ should not exceed $n$. The order selection test actively uses a model selection criterion to perform the test. For each $r=0,1,2, \ldots, R_{n}$ a model with function $\gamma\left(\cdot ; \beta_{0}, \ldots, \beta_{p+r}\right)$ is fit to the data. This results in a sequence of $R_{n}+1$ fitted models. A model selection criterion such as the AIC (Akaike, 1973) is applied to select one of these models. If a model different from the null model is selected, in other words, when the selected order $\hat{r}>0$, then the null hypothesis (1) is rejected. When the selected order $\hat{r}=0$, the null model cannot be rejected.

Asymptotic distribution theory was developed by Eubank and Hart (1992) for linear regression models. Aerts et al. (1999, 2000) extended this to likelihood-based regression models, and related the order selection test statistic to a test statistic that is the supremum of a set of weighted likelihood ratio statistics. Specifically, the null hypothesis (1) is rejected when an AIC-type criterion of the form

$$
\operatorname{aic}\left(r, C_{n}\right)=2\left\{\log L\left(\hat{\boldsymbol{\eta}}, \hat{\beta}_{0}, \ldots, \hat{\beta}_{p+r}\right)-\log L\left(\hat{\boldsymbol{\eta}}, \hat{\beta}_{0}, \ldots, \hat{\beta}_{p}\right)\right\}-C_{n} r, \quad r=0,1,2, \ldots, R_{n},
$$

selects $\hat{r}=\arg \max _{r=0,1,2, \ldots, R_{n}} \operatorname{aic}\left(r, C_{n}\right)>0$. Note that aic $\left(r, C_{n}\right)$ is twice the difference of the maximized log-likelihood value at the model with $r$ additional terms in the series expansion and the corresponding value at the null model, with penalty $C_{n}$ times the number of additional terms $r$. The difference with a traditional AIC difference is that the penalty constant 2 for the AIC is here replaced by a value $C_{n}$, which will determine the level of the test. This can be understood as follows. The above testing approach is equivalent to rejecting the hypothesis (1) when the order selection statistic

$$
T_{O S}=\max _{r=1, \ldots, R_{n}} \frac{2\left(\mathcal{L}_{r}-\mathcal{L}_{0}\right)}{r}>C_{n},
$$

where $\mathscr{L}_{r}=\log L\left(\hat{\boldsymbol{\eta}}_{p+r}, \hat{\boldsymbol{\beta}}_{p+r}\right)$. The value $C_{n}$ is a quantile of the test statistic's distribution, which can be chosen to obtain a certain level for the test. Note that the dimension of the nuisance parameter $\boldsymbol{\eta}$ stays the same in all models, though the value of the estimator might be different when different approximations of $\gamma$ are used. This is indicated in the notation by adding a subscript to the estimator. In the setting of completely observed data, asymptotic distribution theory (see Aerts et al., 1999) provides a method to compute $P$-values of the test. The idea that we work with in this paper is to use similar likelihood ratio based test statistics for the data sets after multiple imputation.

### 2.2. Likelihood ratio tests after multiple imputation

Multiple imputation inserts values for the missing observations in order to create complete sets of data to which standard methods can be applied. The insertion of values is typically repeated a small number of times $m$ (say $3-10$ ) in order to create $m$ sets of completed data. The insertion of multiple values should help to correct the standard errors of estimators for the additional uncertainty introduced by replacing the unknown values by numbers. Indeed, pretending the inserted values to be the true values of the variables would lead to inferences that are too optimistic. In the context of hypothesis testing, with the availability of $m$ completed sets of data, one could perform $m$ separate tests to test hypothesis (1). Meng and Rubin (1992) proposed a method to combine the $m$ separate likelihood ratio values into one single test statistic with an approximate $F$-distribution. This idea builds on a similar combined testing procedure using Wald statistics instead of likelihood ratio statistics, see Li et al. (1991b).

To introduce the notation, fix a value $r>0$ and consider first the parametric testing problem of the null hypothesis (1) against the parametric alternative hypothesis (with a certain fixed value of $r$ )

$$
H_{a, r}: \gamma(\cdot) \in \mathscr{G}_{r}=\left\{\gamma\left(\cdot, \boldsymbol{\beta}_{p+r}\right): \boldsymbol{\beta}_{p+r}=\left(\beta_{0}, \ldots, \beta_{p+r}\right) \in \Theta_{r}\right\},
$$

where the parameter space $\Theta_{r} \subset \mathbb{R}^{p+r+1}$. As a concrete example we could be interested in testing whether $H_{0}: E(Y \mid x)= \beta_{0}+\beta_{1} x$ versus $H_{a, 1}: E(Y \mid x)=\beta_{0}+\beta_{1} x+\beta_{2} x^{2}$, which in this case is equivalent to testing whether $\beta_{2}=0$ in the quadratic model for the mean. In the next section we will relax this particular form of the alternative hypothesis to allow for omnibus testing.

Denote $\mathscr{L}_{r, \ell}$ the log-likelihood ratio statistic for testing hypothesis (1) against the specific alternative (4) with $r$ additional parameters for the $\ell$ th imputed set of data, with $\ell=1, \ldots, m$. We denote the average of these test statistics as $\overline{\mathcal{L}}_{r, \bullet}= m^{-1} \sum_{\ell=1}^{m} \mathscr{L}_{r, \ell}$.

We denote the parameter estimators for the $\ell$ th imputed data set by ( $\hat{\boldsymbol{\eta}}_{p+r, \ell}, \hat{\boldsymbol{\beta}}_{p+r, \ell}$ ). The average of these $m$ parameter estimators is denoted by ( $\overline{\boldsymbol{\eta}}_{p+r, \bullet}, \overline{\boldsymbol{\beta}}_{p+r, \bullet}$ ) under the alternative model and by ( $\overline{\boldsymbol{\eta}}_{p, \bullet,} \overline{\boldsymbol{\beta}}_{p, \bullet}$ ) under the null model. We now define a 'log-likelihood ratio' value for each of the $m$ imputed data sets that is based on the average parameter value over the $m$ sets of completed data, but using the completed data $\boldsymbol{Z}_{i, \ell}, i=1, \ldots, n$ for the $\ell$ th round of imputation. This leads to $\tilde{\mathscr{L}}_{r, \ell}=\log L\left(\overline{\boldsymbol{\eta}}_{p+r, \bullet}, \overline{\boldsymbol{\beta}}_{p+r, \bullet} ; Z_{1, \ell}, \ldots, Z_{n, \ell}\right)$, and their average $\widetilde{\mathscr{L}}_{r, \bullet}=\frac{1}{m} \sum_{\ell=1}^{m} \tilde{\mathscr{L}}_{r, \ell}$. Meng and Rubin (1992) define the combined test statistic for a parametric testing problem

$$
D_{r}=\frac{\widetilde{\mathcal{L}}_{r, \bullet}}{r\left\{1+\frac{m+1}{r(m-1)}\left(\overline{\mathcal{L}}_{r, \bullet}-\widetilde{\mathcal{L}}_{r, \bullet)}\right\}\right.},
$$

and argue that this statistic has an approximate $F$ distribution with degrees of freedom $r$ and $v$ where

$$
v= \begin{cases}4+(t-4)\left\{1+\left(1-2 t^{-1}\right) D^{-1}\right\}^{2} & \text { if } t=r(m-1)>4, \\ t\left(1+r^{-1}\right)\left(1+D^{-1}\right)^{2} / 2 & \text { otherwise },\end{cases}
$$

with $D=\frac{m+1}{r(m-1)}\left(\overline{\mathcal{L}}_{r, \bullet}-\widetilde{\mathcal{L}}_{r, \bullet}\right)$. We refer to Reiter (2007) for an alternative approximation to the denominator degrees of freedom that should work better for small sample sizes and is defined to not exceed the denominator degrees of freedom for the complete data.

### 2.3. Combining the test statistics

Instead of assuming a particular alternative model such as in the alternative hypothesis (4), we construct an order selection test to test $H_{0}$ against a broad class of alternative models, similar to the order selection idea in complete data cases as described in Section 2.1. Again we consider a sequence of approximations to the function of interest $\gamma(\cdot)$ as in (2). Each such approximation leads to a maximized log-likelihood value, and to a statistic $D_{r}$ as in (5). Similar to combining the

Table 1
Simulated critical values $C_{n}$ using the distribution in (10), for various values of the second degree of freedom (DF) of the $F$ distributions, for a given nominal level $\alpha$ and for $R_{n}=200$.
| DF $\nu$ | $\alpha=0.01$ | 0.05 | 0.10 | DF $\nu$ | $\alpha=0.01$ | 0.05 | 0.10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 6 | 17.7592 | 8.8685 | 6.3072 | 90 | 7.0759 | 4.3443 | 3.3418 |
| 7 | 14.9495 | 7.8246 | 5.6748 | 100 | 7.0414 | 4.3272 | 3.3292 |
| 8 | 13.2251 | 7.1435 | 5.2499 | 200 | 6.8900 | 4.2519 | 3.2740 |
| 9 | 12.0745 | 6.6676 | 4.9460 | 300 | 6.8408 | 4.2274 | 3.2560 |
| 10 | 11.2590 | 6.3180 | 4.7186 | 400 | 6.8164 | 4.2153 | 3.2471 |
| 20 | 8.5020 | 5.0560 | 3.8790 | 500 | 6.8019 | 4.2081 | 3.2418 |
| 30 | 7.8327 | 4.7200 | 3.6217 | 600 | 6.7922 | 4.2032 | 3.2383 |
| 40 | 7.5327 | 4.5710 | 3.5096 | 700 | 6.7853 | 4.1998 | 3.2358 |
| 50 | 7.3624 | 4.4865 | 3.4467 | 800 | 6.7801 | 4.1972 | 3.2339 |
| 60 | 7.2526 | 4.4320 | 3.4064 | 900 | 6.7761 | 4.1952 | 3.2325 |
| 70 | 7.1759 | 4.3940 | 3.3783 | 1000 | 6.7729 | 4.1936 | 3.2313 |
| 80 | 7.1193 | 4.3659 | 3.3577 | $\infty$ | 6.7442 | 4.1793 | 3.2208 |


log-likelihood ratio test statistics $2\left(\mathscr{L}_{r}-\mathscr{L}_{0}\right)$ in the order selection statistic $T_{\text {OS }}$ in (3), our new test statistic combines the log-likelihood ratio statistics $D_{r}$ that are obtained after multiple imputation. We define

$$
D_{O S}=\max _{r=1, \ldots, R_{n}} D_{r} .
$$

Note that the statistic $D_{r}$ already contains the number of additional parameters $r$ in its denominator. In the complete data case the likelihood ratio statistic $2\left(\mathscr{L}_{r}-\mathscr{L}_{0}\right)$ has asymptotically a $\chi_{r}^{2}$ distribution, and under some assumptions on the likelihood, Aerts et al. (1999) obtained that the asymptotic distribution of $T_{O S}$ is given by

$$
P\left(T_{O S} \leq x\right)=\exp \left[-\sum_{r=1}^{\infty} \frac{P\left(\chi_{r}^{2}>r x\right)}{r}\right] .
$$

Since for the case of missing data $D_{r}$ follows only an approximate asymptotic distribution that is $F_{r, v}$, with $v$ depending on the data (Meng and Rubin, 1992), we do not obtain the limiting distribution for $D_{O S}$. However, we investigate by simulation whether the approximation

$$
P\left(D_{O S} \leq x\right) \approx \exp \left[-\sum_{r=1}^{\infty} \frac{P\left(F_{r, v}>x\right)}{r}\right]
$$

holds in practice. This limiting distribution can be used to obtain approximate $P$-values, as well as to define the appropriate critical value $C_{n}$ for a given level for the test. Following the same idea of the order selection test when complete data are exploited, the test rejects the hypothesis (1) when the order selection statistic

$$
D_{O S}=\max _{r=1, \ldots, R_{n}} D_{r}>C_{n} .
$$

To obtain simulated critical values or $P$-values, we approximate the infinite series in (8) by a finite sum

$$
P\left(D_{O S} \leq x\right) \approx \exp \left[-\sum_{r=1}^{R_{n}} \frac{P\left(F_{r, v}>x\right)}{r}\right],
$$

for a large value of $R_{n}$, see Table 1 for values of $C_{n}$ for several choices of $v$.
As an alternative to using this approximation one could use a bootstrap approach. One then generates a large number, say $B$, of datasets. For each dataset the test statistic $D_{O S}$ is computed. An approximation to the $P$-value of the order selection test is obtained by computing the percentage of times that the bootstrap values of $D_{O S}$ are larger than the value of $D_{O S}$ for the original data. For the bootstrap to be valid for hypothesis testing, the bootstrap data should be generated under the null hypothesis (see Hall and Wilson, 1991, for more details).

Note that for $\nu$ tending to infinity, it holds that for $F_{r, \nu}$ following a $F$ distribution with $r$ and $\nu$ degrees of freedom, $\lim _{v \rightarrow \infty} r F_{r, v} \sim \chi_{r}^{2}$. Therefore, for $v$ large, $P\left(F_{r, v}>x\right) \approx P\left(\chi_{r}^{2}>r x\right)$. Hence, for $v$ large, the distribution in (8) can be further well approximated by the standard distribution (7) for order selection tests in complete data.

## 3. Simulations

### 3.1. Simulation settings and methods

We investigate the quality of the approximation to the asymptotic distribution by means of a simulation study. All calculations have been performed using the statistical software package R.

We work with a linear model where we simulated independent normally distributed response variables $Y_{i}, i=1, \ldots, n$ with mean $\mu=1$, standard deviation $\sigma=1$, and a covariate $X_{i}$ that is equally spaced in [ 0,1 ]. We test the 'no effect' null hypothesis $H_{0}: E(Y \mid X)=\beta_{0}$.

We consider two main simulation settings (A) where the response contains missing values but the covariates are completely observed, and (B) where the response is completely observed, but there are missing values in the covariates. In both settings, the values are set missing according to a missing-at-random procedure. For setting (A), missing values in the response variables are introduced by generating a missing data mechanism that depends on the fully observed variable $X_{i}$, obeying the MAR condition, in which the missingness depends only on the observed part of the data. In particular, independent standard normal errors $\epsilon_{i j}$ are generated, and a data value $y_{i}$ is set to be missing when $a\left(x_{i}-\bar{x}_{\bullet}\right)+\epsilon_{i j} \leq z_{\tau}$ where $\bar{x}_{\bullet}$ is the sample mean of $\left(x_{1}, \ldots, x_{n}\right)$ and $z_{\tau}$ is the $(1-\tau)$-quantile of $N\left(0, a^{2} / 12+1\right)$ with $\tau$ the chosen percentage of missingness and $a=-1$. For setting (B), missing values in the covariate values are introduced according to the MAR condition, quite in the same way as for setting (A) though now setting a value missing when $a\left(y_{i}-\bar{y}_{\bullet}\right)+\epsilon_{i j} \leq z_{\tau}$ where $\bar{y}_{\bullet}$ is the sample mean of $\left(y_{1}, \ldots, y_{n}\right)$ and $z_{\tau}$ is the $(1-\tau)$-quantile of $N\left(0, a^{2}+1\right)$.

For each of the settings (A) and (B) we consider (i) different sample sizes, $n=30$ and $n=50$ for setting (A) and $n=60$ and $n=100$ for setting (B); (ii) three different percentages of missingness $5 \%, 15 \%$, and $30 \%$; (iii) two types of series expansions, using either orthogonal polynomials (using the function poly in R ) or a cosine basis with $\psi_{j}(x)=\cos (j \pi x)$ with $j=1, \ldots, R_{n}=15$; (iv) two types of alternative models: a linear one where $E(Y \mid X)=1+\beta_{1} X$ and $\beta_{1}$ ranges between 0 and 2 , and an exponential alternative where $E(Y \mid X)=\exp \left(-2+\beta_{1} X\right)$ with $\beta_{1}$ ranging between 0 and 5 , and (v) two different imputation methods, one parametric and the other nonparametric, with more details below.

For each setting we run 2000 simulations. For the order selection test we take an orthogonal series expansion with $R_{n}=15$ terms. We have tried with different orders, but this did not qualitatively change the results. The number of imputations is equal to $m=5$ for each situation.

For the parametric imputation method we have used a method that is available in the R library mice, short for "multiple imputation by chained equations". In particular, we have used a regression method (norm) where the variables with missing data are regressed on the complete data variables in order to estimate the unknown parameters. Values are then drawn from the posterior distribution of the parameters after which these values are used as parameters in a linear regression model. This latter model is used to obtain fitted values for the variable with missing values. Those values serve as imputations for the missing observations. More information on this procedure can be obtained from the help files in $R$ and the references therein. An overview of imputation methods and available software for multiple imputation is given by Horton and Lipsitz (2001) and Horton and Kleinman (2007).

The nonparametric imputation method does not assume a parametric model for the regression of the variable with missing observations on the observed variables. Instead, the R function gam is used (short for generalized additive model) of library mgcv. For this method we regress the covariate with missing values on the observed variables assuming a nonparametric additive model, that is, a model of the form $X_{\text {mis }}=s_{1}\left(X_{\text {obs }}\right)+s_{2}(Y)+\varepsilon$, for the case of a covariate with missing values and a completely observed response vector $Y$ and other covariate $X_{\text {obs }}$. We used the default settings in R with penalized regression splines and automatic smoothing parameter selection. This generates a prediction of the covariate values at the places where it is missing, see also Schomaker et al. (in press) for an imputation scheme using 'gam'. In order to obtain multiple imputations instead of just a single imputation, we further generate $m$ values (the number of wanted imputations) from a normal distribution that is centered at the predicted value, with standard deviation the estimated standard deviation by 'gam'. These generated values are then inserted in the dataset, resulting in $m$ completed datasets for which we apply the described testing procedure.

### 3.2. Critical values and the null distribution of the test

We calculate the theoretical values of the critical point $C_{n}$ for various values of the type I error $\alpha$ of the test, under the approximate asymptotic distribution in (8). Table 1 shows these values when the second degree of freedom $v$ increases from 6 to infinity when using $R_{n}=200$. We want to stress that changes in the upper bound for the first degree of freedom do not affect the values of $C_{n}$, when the second degree of freedom is bigger than 20. For instance for $\alpha=0.01$, when the second degree of freedom is equal to 20 and the first degree of freedom ranges from 1 to $R_{n}=20$ the cut-off point remains equal to 8.502. If the second degree of freedom is between 6 and 20 small differences can be found. For example, for $\alpha=0.01$, when the second degree of freedom is equal to 6 and the first degree of freedom ranges from 1 to $R_{n}=20$, the critical value $C_{n}$ is 17.7591, which is slightly smaller than the value in Table 1. Furthermore, values of the critical value $C_{n}$ are not calculated when the second degree of freedom $\nu$ is below 6 because such values have never occurred in any of our simulation studies. The critical values decrease when the second degree of freedom increases; for $\alpha=0.01$ the drop of $C_{n}$ is more sensitive than for the other selected $\alpha$ 's, which show more stable values. For all the chosen nominal levels $\alpha$ it holds that the higher the degree of freedom the more stable are the values of $C_{n}$. Furthermore when the second degree of freedom is close to infinity the critical values are similar to the ones computed using the $\chi^{2}$ distribution. For the theoretical values of $C_{n}$ for fully observed data we refer to Hart (1997).

The theoretical values of $C_{n}$ are used to obtain the simulation results shown in Table 2, using test (9), rejecting the null hypothesis when the observed value of $D_{\mathrm{OS}}>C_{n}$. We here test the null hypothesis $H_{0}: E(Y \mid X)=\beta_{0}$ under simulation setting (A). The table shows the simulated significance level of the test, under different choices of $\alpha$ and different bases, for the parametric imputation method, as well as the setting where all observations with missing cases are omitted for the analysis. We observe that the test performs well, with the significance levels close to the nominal levels, when the data

Table 2
Results of a simulation study under setting (A). The table shows, based on cosine and polynomial basis, simulated significance levels of the test $D_{O S}$ when the theoretical critical values $C_{n}$ are used, for different values of the nominal level $\alpha$. The imputation methods is 'norm', also a complete case analysis (CC) using $T_{O S}$ is performed. The original data analysis (before introducing missingness) is shown in the last line.
| \% missing | Method | $n=30$ |  |  | $n=50$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | $\alpha=0.01$ | 0.05 | 0.10 | $\alpha=0.01$ | 0.05 | 0.10 |
| 5\% | $\mathrm{Mis}_{\text {norm }}$ | Cosine basis |  |  |  |  |  |
|  |  | 0.0115 | 0.0545 | 0.0985 | 0.0090 | 0.0430 | 0.0920 |
|  | CC | 0.0175 | 0.0810 | 0.1630 | 0.0135 | 0.0565 | 0.1195 |
| 15\% | Mis $_{\text {norm }}$ | 0.0065 | 0.0305 | 0.0660 | 0.0055 | 0.0400 | 0.0820 |
|  | CC | 0.0215 | 0.0940 | 0.1900 | 0.0105 | 0.0585 | 0.1210 |
| 30\% | Mis $_{\text {norm }}$ | 0.0055 | 0.0335 | 0.0585 | 0.0090 | 0.0535 | 0.0875 |
|  | CC | 0.0790 | 0.1905 | 0.3470 | 0.0165 | 0.0645 | 0.1365 |
|  | Orig | 0.0135 | 0.0835 | 0.1655 | 0.0150 | 0.0595 | 0.1285 |
| 5\% | Mis $_{\text {norm }}$ CC | Polynomial basis |  |  |  |  |  |
|  |  | 0.0130 | 0.0540 | 0.1040 | 0.0090 | 0.0460 | 0.0995 |
|  |  | 0.0160 | 0.0795 | 0.1585 | 0.0115 | 0.0595 | 0.1260 |
| 15\% |  | 0.0140 | 0.0475 | 0.0900 | 0.0085 | 0.0450 | 0.0915 |
|  | CC | 0.0195 | 0.0880 | 0.1885 | 0.0105 | 0.0590 | 0.1150 |
| 30\% | $\mathrm{Mis}_{\text {norm }}$ | 0.0165 | 0.0575 | 0.1000 | 0.0105 | 0.0470 | 0.0765 |
|  | CC | 0.0600 | 0.1685 | 0.3260 | 0.0160 | 0.0650 | 0.1385 |
|  | Orig | 0.0140 | 0.0790 | 0.1610 | 0.0130 | 0.0620 | 0.1295 |


Table 3
Simulated levels using asymptotic approximations with $F$ distributions as in (8) or with $\chi^{2}$ distributions as in (7).
| $n$ | \% miss | Approx | $\alpha=1 \%$ | 5\% | 10\% |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 60 | 5 | $F$ | 0.0080 | 0.0385 | 0.0710 |
|  |  | $\chi^{2}$ | 0.0095 | 0.0445 | 0.0805 |
|  | 15 | $F$ | 0.0105 | 0.0400 | 0.0795 |
|  |  | $\chi^{2}$ | 0.0190 | 0.0615 | 0.1115 |
|  | 30 | $F$ | 0.0195 | 0.0535 | 0.0935 |
|  |  | $\chi^{2}$ | 0.0295 | 0.0850 | 0.1310 |
| 100 | 5 | $F$ | 0.0045 | 0.0330 | 0.0660 |
|  |  | $\chi^{2}$ | 0.0055 | 0.0400 | 0.0765 |
|  | 15 | $F$ | 0.0040 | 0.0340 | 0.0570 |
|  |  | $\chi^{2}$ | 0.0090 | 0.0470 | 0.0825 |
|  | 30 | $F$ | 0.0075 | 0.0365 | 0.0675 |
|  |  | $\chi^{2}$ | 0.0190 | 0.0645 | 0.1040 |


are imputed using the regression method (norm), this for both sample sizes 30 and 50 and for all the different percentages of missingness. The results in the table also show that the complete case method, where cases with missing observations are completely left out for performing the test, performs badly, especially for a small sample size, independently of the percentage of missingness, resulting in a too large simulated value for the significance level of the test. For instance when sample size equals 30 and the percentage of missingness is 30 , at the nominal level of $\alpha=0.05$, the simulated significance level for the test we propose is 0.0575 , while using complete cases the level is 0.1685 . There is, however, an improvement when the sample size increases to 50 .

In addition to the previous analyses we investigate the approximation of the asymptotic distribution of $D_{O S}$ by using the bootstrap, as in (8). For a further discussion on the bootstrap for missing data, see Efron (1994), and the discussion on this paper by Rubin (1994). We consider $B=1000$ bootstrap replicates by resampling with replacement the pairs ( $Y_{i}, X_{i}$ ), for data sets with sample size $n=30$ and percentage of missingness equal to $30 \%$. Note that the bootstrap data might contain a different percentage of missingness due to the resampling. For each of the $B$ bootstrap data sets, we compute the test statistic $D_{O S}$ in precisely the same way as for the original data. Those 1000 bootstrap values of $D_{O S}$ are used to construct a bootstrap density plot. We also generate data from the approximate asymptotic distribution (10) using, as second degree of freedom in the $F$-distributions, the degree obtained by performing the order selection test to the original dataset. Fig. 1 displays the bootstrap density function of $D_{\mathrm{OS}}$ and the density of the distribution of (10) for the different settings. The shapes of the distributions are quite similar, even with large percentages of missing values.

We investigated the approximation of the asymptotic distributions (8) and (7) using, respectively, $F$ and $\chi^{2}$ distributions. Table 3 gives the simulated levels of the test for setting (B) with missing covariate values. The main observation from this table is that the easier approximation (7) works quite fine, especially for the larger sample size $n=100$. However, for the smaller sample size and large percentages of missingness, the use of $F$-distributions as in (8) is more precise.

![](https://cdn.mathpix.com/cropped/e237c1f9-3212-4cb6-9e75-9ef1551ae831-07.jpg?height=627&width=1502&top_left_y=173&top_left_x=197)
Fig. 1. Density plots under $H_{0}$ of $D_{O S}$ for testing the no effect null hypothesis for a data set with missing observations for the responses and sample size equal to 30 . The density obtained by bootstrap resampling is shown with the solid line, while the dashed line displays the density when data are simulated from the approximate asymptotic distribution (10). Plot (a) displays the distribution under cosine basis, while (b) uses a polynomial basis, with percentage of missingness equal to $30 \%$.

![](https://cdn.mathpix.com/cropped/e237c1f9-3212-4cb6-9e75-9ef1551ae831-07.jpg?height=641&width=1442&top_left_y=959&top_left_x=229)
Fig. 2. Power curves for testing no effect at the $5 \%$ level for a setting with missing covariates. (a) Comparing imputation by 'gam' and 'mice'. The true model is linear, we use a polynomial basis, $5 \%$ missingness in the covariate, $n=60$ and 'gam' (solid), 'mice' (dotted), $n=100$ and 'gam' (dash-dotted), 'mice' (dashed). (b) The true model is exponential, $n=60$ and $30 \%$ missingness in the covariate, 'mice' with a polynomial basis (short dashed), cosine basis (long dashed), 'gam' with a polynomial basis (solid), and with a cosine basis (dash-dotted). Results of a test based on complete cases only are shown with the dotted line.

### 3.3. Simulated power of the tests

We investigate the power of the order selection test using multiple imputation under the alternative models specified in Section 3.1.

To investigate whether the model assumed for imputation has an effect on the result of the test, we used imputation by means of the R program 'mice' (with option 'norm'), which is a parametric imputation method, and compared that to a completely nonparametric imputation method using 'gam'. For this method we regress the covariate with missing values on the observed variables assuming a nonparametric additive model, hence we do not make parametric assumptions on the form of this regression model.

Fig. 2(a) shows the results of the simulation for the linear alternative model where a polynomial basis is used in the test and there is $5 \%$ missingness in the covariate (setting B). Results for both sample sizes $n=60$ and 100 are given. All four tests achieve the right level. There is, at least for this setting, a striking difference between the tests using nonparametric imputation and those using parametric imputation, the latter case having considerably less power. This observation holds for both sample sizes.

A further comparison is given in Fig. 2(b) where we now show the results for the exponential alternative, for sample size $n=60$ and with a large percentage of missing values in the covariate ( $30 \%$ ). For this setting we show the results of using either a polynomial expansion for the test statistic, or an expansion using cosine functions. The results of a complete case

Table 4
Results of a simulation study for setting (A). The table shows, based on polynomial basis, simulated significance levels of the test $D_{O S}$ when the theoretical critical values $C_{n}$ are used, for different values of the nominal level $\alpha$, performing a sensitivity analysis. The imputation methods is 'norm' and we test $H_{0}: E(Y \mid X)=\beta_{0}$. Different variable transformations have been used for imputation.
| Var in imputed model | \% missing | $n=30$ |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  |  | $\alpha=0.01$ | 0.05 | 0.10 |
|  |  | Polynomial basis |  |  |
|  | 5\% | 0.0135 | 0.0555 | 0.1070 |
| $\log (X+10)$ | 15\% | 0.0110 | 0.0460 | 0.0880 |
|  | 30\% | 0.0110 | 0.0435 | 0.0755 |
|  | 5\% | 0.0135 | 0.0535 | 0.1060 |
|  | 15\% | 0.0125 | 0.0430 | 0.0850 |
|  | 30\% | 0.0155 | 0.0610 | 0.1045 |
|  | 5\% | 0.0060 | 0.0370 | 0.0775 |
| $\cos (6 \pi X)$ | 15\% | 0.0015 | 0.0090 | 0.0285 |
|  | 30\% | 0.0000 | 0.0025 | 0.0110 |
|  | 5\% | 0.0110 | 0.0530 | 0.1095 |
| poly(X, degree=5) <br> poly(X, degree=5) | 15\% | 0.0100 | 0.0445 | 0.0910 |
|  | 30\% | 0.0065 | 0.0520 | 0.0960 |


analysis are shown by the dotted line. Considering first the level, we observe that parametric imputation methods result in a test with a too large level (both long and short dashed lines), at least for this setting with a high percentage of missingness in the covariate. The observed level of the tests was better for situations with less missing covariates (plots not shown). The test with the highest power for the exponential alternative model is the test using a polynomial series expansion in combination with nonparametric imputation using the function 'gam'. The use of the cosine series expansion results here in a test with the lowest power amongst the considered tests. It should be said that there exist alternatives (for example alternatives consisting of cosine functions) where a cosine based test will be more powerful than a test using polynomial expansions. The choice of basis is not that crucial for the test to have power against a wide range of alternatives, though a well chosen choice of basis might help to increase the power for particular situations. For this particular setting, the test based on the complete cases achieves reasonably good power, though less than that of the tests using multiple imputation, both by using parametric imputation by means of 'mice', as by using nonparametric imputation, using the polynomial basis expansion. There is a clear gain in power when dealing with the missingness by means of multiple imputation.

### 3.4. Sensitivity analysis

The above sections showed that the order selection test when missing data are present works quite well; which means that the imputation is done properly as well. In this section we want to perform a sensitivity analysis in order to verify whether a misspecification problem could arise in the multiple imputation method when using the parametric imputation method 'mice'. We start by considering the same simulation setting (A) as described in Section 3.1, where the covariate is fully observed, while the response vector $Y=\left(Y_{1}, \ldots, Y_{n}\right)$ contains missing observations. We test the null hypothesis $H_{0}: E(Y \mid X)=\beta_{0}$, and use an orthogonal polynomial expansion. The model used for the multiple imputation is different from that in the above sections. There we used $X_{i}$ as a variable in a linear regression model to perform the imputation, here we consider a variable transformation and use for imputation a mean model of the form $\beta_{0}+\beta_{1} g(X)$, where $g(X)$ is one of the functions given in the first column of Table 4. Note that poly ( X , degree $=5$ ) stands for orthogonalized polynomials of degree 5 . Hence this last model is the only one that contains variables that also occur when fitting the alternative models for the construction of the order selection test.

Table 4 displays some nice results about the sensitivity of the imputation model. The order selection test is working fine for all the settings except for the high frequency cosine function which results in too small simulated type I errors when the percentage of missingness is large.

We deepen the question by analyzing a different setting; $Y_{i}, i=1, \ldots, n$ are independent normally distributed response variables with mean $\mu=E(Y \mid X)$ as specified below, standard deviation $\sigma=1$, and a covariate $X_{i}$ that is equally spaced in $[0,1]$. The covariate is fully observed, while the response vector $Y=\left(Y_{1}, \ldots, Y_{n}\right)$ contains missing observations. We test the null hypothesis $H_{0}: E(Y \mid X)=\beta_{0}+\beta_{1} X$, and use an orthogonal polynomial expansion. The model used for the multiple imputation is summarized in Table 5, by showing the variable $g(X)$ that is used in a model for the mean of the form $\beta_{0}+\beta_{1} g(X)$. Unlike the previous setting where all models contained the model under the null hypothesis (which was there a constant function), in this setting this is only true for the first two models. The first setting gives the correct imputation model (a linear model for the mean), in the second setting, the model used for imputation is richer than necessary (it contains a fifth degree orthogonal polynomial in $X$ ). We see that this only slightly reduces the observed significance levels in our simulation study. For the other three models, the model that is used for imputation does not contain the null model, and is hence misspecified. For a small percentage of missingness, all imputation methods still perform reasonably well, even the high frequency cosine model. When the missingness increases, this particular model has problems in keeping the level, but the other misspecified imputation models still give reasonable results.

Table 5
Results of a simulation study. The table shows, based on polynomial basis, simulated significance levels of the test $D_{O S}$ when the theoretical critical values $C_{n}$ are used, for different values of the nominal level $\alpha$, performing a sensitivity analysis. The imputation methods is 'norm'. The null hypothesis is $H_{0}: E(Y \mid X)=\beta_{0}+\beta_{1} X$, with $\beta_{0}=1$ and $\beta_{1}=2$.
| Var in imputed model | \% missing | $n=30$ |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  |  | $\alpha=0.01$ | 0.05 | 0.10 |
| X |  | Polynomial basis |  |  |
|  | 5\% | 0.0080 | 0.0470 | 0.0945 |
|  | 15\% | 0.0080 | 0.0370 | 0.0680 |
|  | 30\% | 0.0090 | 0.0400 | 0.0700 |
|  | 5\% | 0.0065 | 0.0440 | 0.0835 |
| poly(X, degree=5) | 15\% | 0.0050 | 0.0285 | 0.0545 |
|  | 30\% | 0.0030 | 0.0320 | 0.0605 |
|  | 5\% | 0.0070 | 0.0435 | 0.0940 |
| $\log (X+10)$ | 15\% | 0.0060 | 0.0285 | 0.0685 |
|  | 30\% | 0.0025 | 0.0300 | 0.0600 |
| $X^{2}$ | 5\% | 0.0055 | 0.0385 | 0.0805 |
|  | 15\% | 0.0025 | 0.0160 | 0.0445 |
|  | 30\% | 0.0020 | 0.0170 | 0.0390 |
| $\cos (6 \pi X)$ | 5\% | 0.0050 | 0.0335 | 0.0780 |
|  | 15\% | 0.0015 | 0.0130 | 0.0345 |
|  | 30\% | 0.0000 | 0.0080 | 0.0270 |


Table 6
Results for the climate data. The table shows critical values $C_{n}$ of the test $D_{O S}$ at the $10 \%$ level, the $P$-value and, for the missing data approach, the second degree of freedom used to calculate the corresponding $P$-value.
| Method | Cosine basis |  |  | Polynomial basis |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $C_{n}$ | $P$-value | df $v$ | $C_{n}$ | $P$-value | df $v$ |
| $\mu$ constant |  |  |  |  |  |  |
| Missing | 3.943 | 0.061 | 300.92 | 3.353 | 0.083 | 138.24 |
| CC | 4.159 | 0.051 | - | 4.329 | 0.045 | - |
| $\mu$ linear |  |  |  |  |  |  |
| Missing | 0.826 | 0.797 | 197.20 | 0.898 | 0.767 | 243.24 |
| CC | 1.874 | 0.323 | - | 1.916 | 0.310 | - |


While these simulation results show that it is not really crucial to know the correct model for imputations, it is still advised to pay attention to this part of the modeling process, and to use a procedure with enough flexibility to reflect salient features of the data.

## 4. Data analysis

Agriculture is one of the economic sectors that is highly sensitive to climate change, because its activities depend directly on climate conditions, and because of its greenhouse gas releases. Crop and meat production, milk products, livestock, are some of the agricultural activities that contribute to global warming.

We want to investigate the relationship between the emission of greenhouse gasses and the production of wheat. The data come from Eurostat, the Statistical Office of the European Communities, which gathers and analyses figures from the national statistical offices across Europe and provides statistical information. Data to be analyzed are $\left(Y_{i}, X_{i}\right), i=1, \ldots, 33$, where the response variable $Y_{i}$ is the total greenhouse gas (GHG) emissions in thousands of tons, for the agricultural sector, and $X_{i}$ is the yield ( $100 \mathrm{~kg} / \mathrm{ha}$ ) of wheat in 33 European countries for the year 2006; the response variable contains 7 missing observations. For the analysis we rescale the explicative variable to the interval $[0,1]$. We want to analyze the relationship between the yield and the emission of greenhouse gas; we consider a linear regression model. We test two different null hypotheses

$$
H_{0}: E(Y \mid X)=\beta_{0}
$$

and

$$
H_{0}: E(Y \mid X)=\beta_{0}+\beta_{1} X .
$$

We consider again the polynomial and the cosine bases used in the simulation study, with $R_{n}=15$.
Table 6 displays the results when the order selection test is performed. At the $10 \%$ level, the test $D_{\text {OS }}$ rejects the null hypothesis that the expected value of the conditional distribution of $Y$ given $X$ is constant. This data set provides evidence (at the $10 \%$ level) that wheat production has an impact on the total emission of greenhouse gases. With the small sample of

![](https://cdn.mathpix.com/cropped/e237c1f9-3212-4cb6-9e75-9ef1551ae831-10.jpg?height=613&width=1484&top_left_y=171&top_left_x=197)
Fig. 3. Density plots of $D_{O S}$ for testing the null hypothesis of linearity for the data set. The density obtained by bootstrap resampling is shown with the solid line, while the dashed line displays the density when data are simulated from the approximate asymptotic distribution (10). Plot (a) displays the distribution using a cosine basis, while for (b) a polynomial basis is used.

data for 33 countries, the test could not reject the null hypothesis that the expected value of ( $Y \mid X$ ) is linear, at the $10 \%$ level. For these data, the linear model seems appropriate.

Furthermore we want to check whether the distribution of the test $D_{O S}$, applied to the dataset resembles the asymptotic distribution of (10). We drew 2000 bootstrap for the dataset, using the cosine and the polynomial bases, to estimate the distribution. We carried out the analysis testing the null hypothesis $H_{0}: E(Y \mid X)=\beta_{0}+\beta_{1} X$. To approximate the asymptotic distribution (10) we use as second degree of freedom $\nu=197.20$ for the test with cosine basis and $\nu=243.24$ when using an orthogonal polynomial basis. Fig. 3 displays the result, where we can see that the shape of the bootstrap distribution is quite similar to the approximated asymptotic distribution.

## 5. Model selection via AIC for multiply imputed data

### 5.1. Definition of the AIC

In the previous sections we discussed a nonparametric testing method that works with missing data. We here use the obtained results to develop a version of Akaike's information criterion to handle multiple imputations. While it is straightforward to apply any traditional variable selection criterion such as the AIC to the separate imputed sets of data, the biggest question is how the results of those separate AIC selections should be combined? In a Bayesian setting Yang et al. (2005) compute for each imputed dataset separately the posterior for each of the candidate models and then take for each model separately the average of the posterior probabilities over the different imputed data sets. Schomaker et al. (2007) work with the AIC and imputation. They mention two approaches. A first one is to compute the classical AIC for each imputed dataset separately and then compute the average of the AIC values to make a ranking of the candidate models. Their second method is the one that they actually apply in their paper. This consists of computing an averaged dataset that consists of the average of each data value after imputation. Now they have a single dataset to which the classical AIC can be applied. We here propose a theoretically solid version of the AIC that is related though different from the two mentioned proposals. We will see that actually a combination of the two proposals is required.

Multiple imputation for a model $S$ leads to $m$ different datasets, each with its own maximized log-likelihood function. Often the candidate models are nested, in which case we denote by $S_{0}$ the smallest model under consideration. If we were in a testing setting to compare a model $S$ (under the alternative hypothesis) with a simpler model $S_{0}$ (under the null hypothesis) we could apply the results of Meng and Rubin (1992) who proposed to combine the $m$ separate likelihood ratio values into one single test statistic with an approximate $F$-distribution, as in Section 2.2. Denote the number of parameters in model $S$ by $|S|$, and the difference in numbers of parameters of the two models by $p_{S}=|S|-\left|S_{0}\right|$. By the results in Meng and Rubin (1992), we obtain that the combined test statistic for testing model $S_{0}$ versus model $S$ is

$$
\frac{\tilde{D}_{S}}{p_{S}}=\frac{\tilde{\mathscr{L}}_{S, \bullet}}{p_{S}\left\{1+\frac{m+1}{p_{S}(m-1)}\left(\overline{\mathscr{L}}_{S, \bullet}-\widetilde{\mathscr{L}}_{S, \bullet)}\right)\right.} .
$$

This statistic has an approximate $F$ distribution with degrees of freedom $p_{S}$ and $v$ where $v$ is as in (6). The second degree of freedom $\nu$ is expected to be large under a good imputation scheme where $D$ will be small. Therefore we can work with $p_{s}$ only as a penalty term in the AIC difference for model $S$ compared to model $S_{0}$, see also Section 2.3. Thus we arrive at the definition of the AIC difference for model $S$ compared to model $S_{0}$ as

$$
\operatorname{aic}\left(S, S_{0}\right)=\tilde{D}_{S}-2 p_{S} .
$$

Table 7
AIC model selection on multiple imputed datasets. The table shows for a normal regression model with four covariates of which two are relevant, the results of the variable selection search by aic ${ }_{D}$, AIC and $\overline{\text { AIC. The results of a complete case analysis are indicated with } \text { AIC }_{C C} \text {, and those of the original data }}$ before introducing missingness by $\mathrm{AIC}_{\text {orig }}$.
| Method | $n=100$ |  | $n=200$ |  |
| :--- | :--- | :--- | :--- | :--- |
|  | Correct | Overfit | Correct | Overfit |
| $\mathrm{aic}_{D}$ | 0.541 | 0.459 | 0.594 | 0.406 |
| AIC. | 0.540 | 0.460 | 0.574 | 0.426 |
| $\overline{\text { AIC }}$ | 0.540 | 0.460 | 0.574 | 0.426 |
| $\mathrm{AIC}_{\mathrm{CC}}$ | 0 | 1 | 0 | 1 |
| $\mathrm{AIC}_{\text {orig }}$ | 0.731 | 0.269 | 0.722 | 0.278 |


Note that the constant 2 is already absorbed in the notation for the log-likelihood ratio statistics. These differences can be computed for all models $S$ under consideration, with aic $\left(S_{0}, S_{0}\right)=0$. The model with the largest AIC difference is considered the best one. Criterion (11) is generally applicable for use with multiple imputation for likelihood models.

### 5.2. Simulation study

The proposed AIC is compared in a simulation study to two versions of AIC that are recently proposed by Schomaker et al. (2007). Their first suggestion is to use imputations to create $m$ datasets, to each of which the traditional AIC can be applied. For each considered model you then get $m$ AIC values, the 'final' AIC is the average of the $m$ separate AIC values, denote this by $\overline{\text { AIC }}$. A second approach, and this is what is actually used in their paper, is to make $m$ completed datasets, construct an averaged dataset by computing the average of each data value, and then apply AIC to this averaged dataset, we denote this by AIC. The method in (11) is denoted by aic ${ }_{D}$ (to stress its dependence on the statistic $D$ ).

The model that we generate is the following. We generate $X_{1} \sim N(0,1), X_{2} \sim \operatorname{Unif}(0,4),\left(X_{3}, X_{4}\right) \sim N_{2}\left(\binom{0}{5},\left(\begin{array}{cc}1 & 0.3 \\ 0.3 & 1\end{array}\right)\right)$, all independent. We further generate $\epsilon \sim N(0,4)$ and generate normal random variables with $Y=30+3 X_{1}-20 X_{2}+\epsilon$. Values of $X_{1}$ are set missing by generating a Bernoulli variable $R$ with probability $H\left(\left(X_{3}-5\right)^{2}-39\right)$, where $H$ is the inverse logit function $H(x)=e^{x} /\left(1+e^{x}\right)$, resulting in about $11 \%$ missing values. The number of simulations is 1000 . Two sample sizes are taken, $n=100$ and $n=200$.

Simulation results have illustrated that for the purpose of model selection, the randomness that is introduced by generating values to serve as imputation is too large when we generate $m$ values from a normal distribution with mean the predicted value from a nonparametric additive model on the observed variables, and with standard deviation the estimated standard deviation from this estimation method. The model selection method leads in this case to models that tend to overfit, that is, models that include too many variables. A simple remedy is to reduce the variability for the imputations by dividing the standard deviation by a factor when generating the imputations. For the cases that we tried, a factor of 15 seems to produce reasonable results.

Table 7 shows the percentage of times that the correct model is selected by the information criterion, as well as the percentage of times that a model with too many variables is selected. In this simulation study underfitting, that is, including too few variables, did not occur. This is a typical behaviour for AIC methods. A complete case model search is also performed, and the results of the original data analysis (before introducing the missingness) are also shown. It turns out that all three AIC methods are comparable in this situation, with the averaging methods leading to identical results for this case. While the emphasis of this paper is mostly on the testing method, the connected AIC method seems worthwhile to be further investigated, both theoretically as well as in practical situations. This, however, extends the scope of the current paper.

## 6. Discussion and extensions

We introduced an order selection test to apply to data with missing observations. In the simulations we have considered the situation of a missing response variable with a completely observed covariate. Since the likelihood ratio test on which the order selection test is based, can also be applied to data sets with missing covariates, the tests are equally well applicable to data with missing covariates. One requirement is that a proper imputation method should be used to lead to a valid asymptotic distribution of the, for imputation combined, likelihood ratio test. In cases where the approximate asymptotic distribution is not expected to work well, a bootstrap procedure can be used to provide $P$-values.

While the illustrations in this paper are restricted to the case of a simple regression model, the order selection testing idea is readily extended to be applicable to multiple regression. We refer to Aerts et al. (2000) and Bissantz et al. (2009) for examples and the construction of a series expansion in more than one variable.

Since the Wald test is asymptotically equivalent to the likelihood ratio test, one could modify the proposed test statistic $D_{\text {OS }}$ to use the Wald statistics instead of the likelihood ratio statistics. This test is expected to have similar power behaviour. One other related construction that could be of particular interest would be to combine score statistics instead. However, we are not aware of results on the construction and asymptotic distribution of score tests, combined after multiple imputation. This seems an interesting topic for further research since such score tests could be applied to models that are not
likelihood-based (for example based on generalized estimating equations, or quasi-likelihood), and can be made robust for model misspecification.

Other related test statistics following the order selection idea could be constructed for the situation of missing data, following their equivalent ideas for complete sets of data. In particular, one could consider the Bayesian information criterion BIC for order selection, hereby leaving out the order zero as a possibility, due to the consistency of the BIC as a model selection method. Such test was first considered for goodness-of-fit testing by Ledwina (1994). Claeskens and Hjort (2004) discuss some alternative schemes based on both BIC and AIC that have better power properties. Such tests could be of interest to investigate in the missing data setting as well.

A further direction for related research is to consider the distribution of the test statistic in more detail. In particular, instead of starting from the approximation to a $F$ distribution of the Meng and Rubin (1992) statistic, one could try to find the limiting distribution and use that as information to build the order selection statistic. Such a theoretical approach can then shed light on the effect of the missing data in the distribution of the test statistic.

## References

Aerts, M., Claeskens, G., Hart, J.D., 1999. Testing the fit of a parametric function. Journal of the American Statistical Association 94, 869-879.
Aerts, M., Claeskens, G., Hart, J.D., 2000. Testing lack of fit in multiple regression. Biometrika 87, 405-424.
Akaike, H., 1973. Information theory and an extension of the maximum likelihood principle. In: Petrov, B., Csáki, F. (Eds.), Second International Symposium on Information Theory. Akadémiai Kiadó, Budapest, pp. 267-281.
Bissantz, N., Claeskens, G., Holzmann, H., Munk, A., 2009. Testing for lack of fit in inverse regression - with applications to biophotonic imaging. Journal of the Royal Statistical Society, Series B 71 (1), 25-48.
Claeskens, G., Hjort, N.L., 2004. Goodness of fit via nonparametric likelihood ratios. Scandinavian Journal of Statistics 31, 487-513.
Efron, B., 1994. Missing data, imputation, and the bootstrap. Journal of the American Statistical Association 89 (426), 463-479.
Eubank, R.L., Hart, J.D., 1992. Testing goodness-of-fit in regression via order selection criteria. The Annals of Statistics 20, 1412-1425.
González-Manteiga, W., Pérez-González, A., 2006. Goodness-of-fit tests for linear regression models with missing response data. The Canadian Journal of Statistics 34 (1), 149-170.
Hall, P., Wilson, S.R., 1991. Two guidelines for bootstrap hypothesis testing. Biometrics 47 (2), 757-762.
Hart, J.D., 1997. Nonparametric Smoothing and Lack-of-fit Tests. Springer-Verlag, New York.
Horton, N.J., Kleinman, K.P., 2007. Much ado about nothing: a comparison of missing data methods and software to fit incomplete data regression models. The American Statistician 61 (1), 79-90.
Horton, N.J., Lipsitz, S.R., 2001. Multiple imputation in practice: comparison of software packages for regression models with missing variables. The American Statistician 55 (3), 244-254.
Ledwina, T., 1994. Data-driven version of Neyman's smooth test of fit. Journal of the American Statistical Association 89, 1000-1005.
Li, K.H., Meng, X.-L., Raghunathan, T.E., Rubin, D.B., 1991a. Significance levels from repeated p-values with multiply-imputed data. Statistica Sinica 1 (1), 65-92.
Li, K.H., Raghunathan, T.E., Rubin, D.B., 1991b. Large-sample significance levels from multiply imputed data using moment-based statistics and an $F$ reference distribution. Journal of the American Statistical Association 86 (416), 1065-1073.
Little, R.J.A., Rubin, D.B., 2002. Statistical Analysis with Missing Data, second ed. In: Wiley Series in Probability and Statistics, Wiley-Interscience [John Wiley \& Sons], Hoboken, NJ.
Meng, X.-L., Rubin, D.B., 1992. Performing likelihood ratio tests with multiply-imputed data sets. Biometrika 79 (1), 103-111.
Reiter, J.P., 2007. Small-sample degrees of freedom for multi-component significance tests for multiple imputation for missing data. Biometrika 94 (2), 502-508.
Rubin, D.B., 1994. Missing data, imputation, and the bootstrap: comment. Journal of the American Statistical Association 89 (426), 475-478.
Schomaker, M., Heumann, C., Toutenburg, H., 2007. New approaches for model selection under missing data, Technical Report, Department of Statistics, Ludwig-Maximilians-Universität München.
Schomaker, M., Wan, A.T., Heumann, C., 2010. Frequentist model averaging with missing observations, Computational Statistics and Data Analysis $\mathrm{x}(\mathrm{x})$, in press (doi:10.1016/j.csda.2009.07.023).
Yang, X., Belin, T.R., Boscardin, W.J., 2005. Imputation and variable selection in linear regression models with missing covariates. Biometrics 61(2), 498-506.


[^0]:    * Corresponding author. Tel.: +32 16 326993; fax: +32 16326624.

    E-mail address: Gerda.Claeskens@econ.kuleuven.be (G. Claeskens).

