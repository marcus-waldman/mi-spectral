---
citekey: vuongLikelihoodRatioTests1989
item_type: article
authors: 'Vuong, Quang H.'
year: 1989
title: 'Likelihood {Ratio Tests} for {Model Selection} and {Non-Nested Hypotheses}'
venue: Econometrica
volume: 57
issue: 2
pages: 307
doi: 10.2307/1912557
eprint: 1912557
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\vuong_likelihood_ratio_tests_1989.pdf'
pdf_sha256: 31cf275a05222d264550deadc592894b773689dadc13069ab926911fbce863d7
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-04T16:25:21Z
---
# Likelihood Ratio Tests for Model Selection and Non-Nested Hypotheses 

Author(s): Quang H. Vuong
Source: Econometrica, Mar., 1989, Vol. 57, No. 2 (Mar., 1989), pp. 307-333
Published by: The Econometric Society
Stable URL: https://www.jstor.org/stable/1912557

## Accessibility support:

If you experience accessibility issues with this file, report them here

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and .facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org

Your use of the TSTOR archive indicates your acceptance of the Terms \& Conditions of Use, available at https://about.jstor.org/terms

# LIKELIHOOD RATIO TESTS FOR MODEL SELECTION AND NON-NESTED HYPOTHESES ${ }^{1}$ 

By Quang H. Vuong


#### Abstract

In this paper, we develop a classical approach to model selection. Using the KullbackLeibler Information Criterion to measure the closeness of a model to the truth, we propose simple likelihood-ratio based statistics for testing the null hypothesis that the competing models are equally close to the true data generating process against the alternative hypothesis that one model is closer. The tests are directional and are derived successively for the cases where the competing models are non-nested, overlapping, or nested and whether both, one, or neither is misspecified. As a prerequisite, we fully characterize the asymptotic distribution of the likelihood ratio statistic under the most general conditions. We show that it is a weighted sum of chi-square distribution or a normal distribution depending on whether the distributions in the competing models closest to the truth are observationally identical. We also propose a test of this latter condition.


Keywords: Likelihood ratio tests, model selection, non-nested hypotheses, misspecified models, weighted sums of chi-squares.

## 1. INTRODUCTION

The main purpose of this paper is to propose some new tests for model selection and non-nested hypotheses. Since all our tests are based on the likelihood ratio principle, as a prerequisite, we shall completely characterize the asymptotic distribution of the likelihood ratio statistic under general conditions. By general conditions we mean that the models may be nested, non-nested, or overlapping, and that both, only one, or neither of the competing models may contain the true law generating the observations.

Unlike most previous work on model selection (see, e.g., Chow (1983, Ch. 9), Judge et al. (1985, Ch. 21)), we adopt the classical hypothesis testing framework and propose some directional and symmetric tests for choosing between models. This approach, which has not attracted a lot of attention, dates back to Hotelling (1940). See also Chow (1980). A notable and recent exception is White and Olson (1979) where competing models are evaluated according to their mean-square error of prediction. In this paper, we follow Akaike $(1973,1974)$ and consider the Kullback-Leibler (1951) Information Criterion (KLIC) which measures the distance between a given distribution and the true distribution. If the distance between a specified model and the true distribution is defined as the minimum of

[^0]the KLIC over the distributions in the model, then it is natural to define the "best" model among a collection of competing models to be the model that is closest to the true distribution (see also Sawa (1978, Rule 2.1)).

We consider conditional models so as to allow for explanatory variables. Then, if $\boldsymbol{F}_{\theta}=\{f(y \mid z ; \theta) ; \theta \in \Theta\}$ is a conditional model, its distance from the true conditional density $h^{0}(y \mid z)$, as measured by the minimum KLIC, is $E^{0}\left[\log h^{0}(y \mid z)\right]-E^{0}\left[\log f\left(y \mid z ; \theta_{*}\right)\right]$ where $E^{0}[\cdot]$ denotes the expectation with respect to the true joint distribution of $(y, z)$ and $\theta_{*}$ is the pseudo-true value of $\theta$ (see, e.g., Sawa (1978), White (1982a)). Thus, an equivalent selection criterion can be based on the quantity $E^{0}\left[\log f\left(y \mid z ; \theta_{*}\right)\right]$, the "best" model being the one for which this quantity is the largest.

Given two conditional models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}=\{g(y \mid z ; \gamma) ; \gamma \in \Gamma\}$, which may be nested, non-nested, or overlapping, we propose tests of the null hypothesis that $E^{0}\left[\log f\left(y \mid z ; \theta_{*}\right)\right]=E^{0}\left[\log g\left(y \mid z ; \gamma_{*}\right)\right]$ meaning that the two models are equivalent, against $E^{0}\left[\log f\left(y \mid z ; \theta_{*}\right)\right]>E^{0}\left[\log g\left(y \mid z ; \gamma_{*}\right)\right]$ meaning that $\boldsymbol{F}_{\theta}$ is better than $\boldsymbol{G}_{\gamma}$ or against $E^{0}\left[\log f\left(y \mid z ; \theta_{*}\right)\right]<E^{0}\left[\log g\left(y \mid z ; \gamma_{*}\right)\right]$ meaning that $\boldsymbol{G}_{\gamma}$ is better than $\boldsymbol{F}_{\boldsymbol{\theta}}$. Tests of such hypotheses are called tests for model selection. Since the true density $h^{0}(y \mid z)$ is not restricted a priori to belong to either one of the models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$, by necessity, the concern of this paper is with asymptotic results.

The quantity $E^{0}\left[\log f\left(y \mid z ; \theta_{*}\right)\right]$ is unknown. It can nevertheless be consistently estimated, under some regularity conditions, by ( $1 / n$ ) times the log-likelihood evaluated at the pseudo or quasi maximum likelihood estimator (MLE) (see, e.g., White (1982a), Gourieroux, Monfort, and Trognon (1984)). Hence ( $1 / n$ ) times the log-likelihood ratio (LR) statistic is a consistent estimator of the quantity $E^{0}\left[\log f\left(y \mid z ; \theta_{*}\right)\right]-E^{0}\left[\log g\left(y \mid z ; \gamma_{*}\right)\right]$. Given the above definition of a "best" model, it is natural to consider the LR statistic as a basis for constructing tests for model selection. Since the two competing models may be nested, non-nested, or overlapping, and since both, only one, or neither of the two models may be correctly specified, it is necessary to obtain the asymptotic distribution of the LR statistic under the most general conditions. To do so, we use the framework of White (1982a) in order to handle the possibly misspecified case.

Since Neyman and Pearson (1928) advocated the LR test, it has become one of the most popular methods for testing restrictions on the parameters of a statistical model. It is well-known that minus twice the LR statistic has a limiting central chi-square distribution under the null hypothesis (Wilks (1938)), and a limiting noncentral chi-square distribution under sequences of local alternatives (Wald (1943)). However, as Foutz and Srivastava (1977), Kent (1982), and White (1982a) pointed out, when the largest model is misspecified, the LR statistic is no longer necessarily chi-square distributed under the null hypothesis, where the null hypothesis must be redefined in terms of the pseudo-true values satisfying the specified restrictions. Parallel to this literature on hypothesis testing, the LR statistic has also been advocated as a basis for testing non-nested models (Cox (1961, 1962)). In particular Cox $(1961,1962)$ and White $(1982 b)$ showed that, if $n$ denotes the sample size, then $n^{-1 / 2}$ times the LR statistic properly centered and
normalized has a limiting standard normal distribution under the hypothesis that one of the competing models is correctly specified. These results suggest that the asymptotic distribution of the LR statistic as well as the speed at which it converges to that distribution depend on whether the models are nested or correctly specified. In the first part of this paper, we completely characterize the asymptotic distribution of the LR statistic under the most general conditions.

The paper is organized as follows. In Section 2, we present the basic framework. In Section 3, we derive the asymptotic distribution of the LR statistic whether or not the models are nested or misspecified. We show that it depends on the condition $f\left(y \mid z ; \theta_{*}\right)=g\left(y \mid z ; \gamma_{*}\right)$ for almost all $(y, z)$. In Section 4, we show that $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ is equivalent to the hypothesis that a variance $\omega_{*}^{2}$ is zero. This allows us to construct a test of $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ based on a consistent estimator $\hat{\omega}_{n}^{2}$ of $\omega_{*}^{2}$. In the next three sections, we apply the previous results to derive new and directional LR based tests for model selection in all possible situations. In Sections 5, 6, and 7, we consider successively the cases where the competing models are (strictly) non-nested, overlapping, and nested. We also briefly compare our approaches to that of Akaike $(1973,1974)$ and Cox (1961, 1962). Section 8 summarizes our results and suggests some directions for further research. All the proofs are collected in the Appendix.

## 2. BASIC FRAMEWORK

Let $X_{t}$ be a $m \times 1$ observed random vector taking its values in a Polish space $\boldsymbol{X}$, i.e., a complete separable metric space. For instance, in the case of a real random vector, $\boldsymbol{X}$ is the Euclidean space $\mathbb{R}^{m}$. Let $\sigma_{X}$ be the Borel $\sigma$-algebra on $\boldsymbol{X}$. The vector $X_{t}$ is partitioned into $X_{t}=\left(Y_{t}, Z_{t}\right)$ where $Y_{t}$ and $Z_{t}$ are respectively $l$ and $k$ dimensional vectors with $m=l+k$. Let $\left(\boldsymbol{Y}, \boldsymbol{\sigma}_{Y}\right)$ and $\left(\boldsymbol{Z}, \boldsymbol{\sigma}_{Z}\right)$ be the measurable spaces associated with $Y_{t}$ and $Z_{t}$. Let $H_{X}^{0}$ be the true joint distribution of $X_{t}$. We shall be interested in the true conditional distribution $H_{Y \mid Z}^{0}(\cdot \mid \cdot)$ of $Y_{t}$ given $Z_{t}$, which exists by Jirina's Theorem (see, e.g., Bauer (1972, p. 319), Monfort (1980, p. 93)). We can think of $Y_{t}$ as being the endogenous variables, and of $Z_{t}$ as being the exogenous variables.

The process generating the observations $X_{t}, t=1,2, \ldots$, satisfies the next assumption. Let $H_{Z}^{0}$ be the true marginal distribution of $Z_{t}$, and $\nu_{Y}$ be a $\sigma$-finite measure on $\left(\boldsymbol{Y}, \boldsymbol{\sigma}_{\boldsymbol{Y}}\right)$.

Assumption A1: (a) The random vectors $X_{t}, t=1,2, \ldots$, are independent and identically distributed (i.i.d.) with common true distribution $H_{X}^{0}$ on ( $\boldsymbol{X}, \boldsymbol{\sigma}_{X}$ ). (b) For $H_{Z}^{0}$-almost all $z, H_{Y \mid Z}^{0}(\cdot \mid z)$ has a Radon-Nikodym density $h^{0}(\cdot \mid z)$ relative to $\nu_{Y}$, which is strictly positive for $\nu_{Y}$-almost all $y$.

Assumption A1-(a) is more suitable for cross-section than time-series data. Some of our results can be generalized to more general data generating processes such as those considered by Burguette, Gallant, and Souza (1982), and White and Domowitz (1984). An assumption equivalent to Assumption A1-(b) is that
$H_{Y \mid Z}^{0}(\cdot \mid z)$ and $\nu_{Y}$ are, for $H_{Z}^{0}$-almost all $z$, absolutely continuous relative to each other (see, e.g., Bauer (1972, p. 901)). Since a similar remark applies to Assumption A2-(a) below, it follows that the measures $H_{Y \mid Z}^{0}(\cdot \mid z), F_{Y \mid Z}(\cdot \mid z ; \theta)$, and $\nu_{Y}$ are absolutely continuous relative to each other, and hence have the same negligible sets. As a consequence of these assumptions, the true conditional distribution $H_{Y \mid Z}^{0}(\cdot \mid \cdot)$ and the competing conditional models have the same support. ${ }^{2}$

We now consider two competing parametric families of conditional distributions defined on $\sigma_{Y} \times \boldsymbol{Z}$ for $Y_{t}$ given $Z_{t}: \boldsymbol{F}_{\theta} \equiv\left\{F_{Y \mid Z}(\cdot \mid \cdot ; \theta) ; \theta \in \Theta \subset \mathbb{R}^{p}\right\}$ and $G_{\gamma} \equiv\left\{G_{Y \mid Z}(\cdot \mid \cdot ; \gamma) ; \gamma \in \Gamma \subset \mathbb{R}^{q}\right\}$. No assumption is here made on the relationship between the two competing conditional models $\boldsymbol{F}_{\boldsymbol{\theta}}$ and $\boldsymbol{G}_{\boldsymbol{\gamma}}$ in the sense that they may be nested, overlapping, or non-nested. Moreover, both, only one, or neither may be correctly specified, i.e., may contain the true conditional distribution for $Y_{t}$ given $Z_{t}$. Each conditional model satisfies the following regularity conditions (Vuong (1983)) which are similar to those of White (1982a, Assumptions A2-A6) with the exception that they bear on conditional models. These regularity conditions are presented without discussion. They are stated in terms of $\boldsymbol{F}_{\boldsymbol{\theta}}$. It is understood that similar assumptions are made on $\boldsymbol{G}_{\gamma}$.

Assumption A2: (a) For every $\theta$ in $\Theta$ and for $H_{Z}^{0}$-almost all $z$ the conditional distribution $F_{Y \mid Z}(\cdot \mid z, \theta)$ has a Radon-Nikodym density $f(\cdot \mid z ; \theta)$ relative to $\nu_{Y}$, which is strictly positive for $\nu_{Y}$-almost all $y$. (b) $\Theta$ is a compact subset of $\mathbb{R}^{p}$, and the conditional density $f(y \mid z ; \theta)$ is continuous in $\theta$ for $H_{X}^{0}$-almost all $(y, z)$.

Assumption A3: (a) For $H_{X}^{0}$-almost all $(y, z),|\log f(y \mid z ; \cdot)|$ is dominated by an $H_{X}^{0}$-integrable function independent of $\theta$. (b) The function $z_{f}(\theta) \equiv \int \log f(y \mid z ; \theta) H_{X}^{0}(d x)$ has a unique maximum on $\Theta$ at $\theta_{*}$.

The value $\theta_{*}$ is called the pseudo-true value of $\theta$ for the conditional model $\boldsymbol{F}_{\theta}$ (see, e.g., Sawa (1978)). Similarly, $\gamma_{*}$ denotes the pseudo-true value of $\gamma$ for the conditional model $\boldsymbol{G}_{\gamma}$.

Assumption A4: (a) For $H_{X}^{0}$-almost all $(y, z), \log f(y \mid z ; \cdot)$ is twice continuously differentiable on $\Theta$. (b) For $H_{X}^{0}$-almost all $(y, z), \mid \partial \log f(y \mid z ; \cdot) / \partial \theta$. $\partial \log f(y \mid z ; \cdot) / \partial \boldsymbol{\theta}^{\prime} \mid$ and $\left|\partial^{2} \log f(y \mid z ; \cdot) / \partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{\prime}\right|$ are dominated by $H_{X}^{0}$-integrable functions independent on $\theta$.

[^1]This ensures the existence of the usual matrices:

$$
\begin{aligned}
& A_{f}(\theta) \equiv E^{0}\left[\frac{\partial^{2} \log f\left(Y_{t} \mid Z_{t} ; \theta\right)}{\partial \theta \partial \theta^{\prime}}\right] \\
& B_{f}(\theta) \equiv E^{0}\left[\frac{\partial \log f\left(Y_{t} \mid Z_{t} ; \theta\right)}{\partial \theta} \cdot \frac{\partial \log f\left(Y_{t} \mid Z_{t} ; \theta\right)}{\partial \theta^{\prime}}\right]
\end{aligned}
$$

where $E^{0}[\cdot]$ denotes the expectation with respect to the true joint distribution of $X_{t}=\left(Y_{t}, Z_{t}\right)$. Similar matrices $A_{g}(\gamma)$ and $B_{g}(\gamma)$ are defined for the conditional model $\boldsymbol{G}_{\gamma}$. Moreover, since Assumption A4 holds for both models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$, then for $H_{X}^{0}$-almost all $(y, z),\left|\partial \log f(y \mid z ; \cdot) / \partial \theta \cdot \partial \log g(y \mid z ; \cdot) / \partial y^{\prime}\right|$ is dominated by an $H_{X}^{0}$-integrable function independent of $\theta$ and $\gamma$. This ensures the existence of the $p \times q$ matrix:

$$
B_{f g}(\theta, \gamma)=B_{g f}^{\prime}(\gamma, \theta) \equiv E^{0}\left[\frac{\partial \log f\left(Y_{t} \mid Z_{t} ; \theta\right)}{\partial \theta} \cdot \frac{\partial \log g\left(Y_{t} \mid Z_{t} ; \gamma\right)}{\partial \gamma^{\prime}}\right] .
$$

Assumption A5: (a) $\boldsymbol{\theta}_{*}$ is an interior point of $\boldsymbol{\Theta}$. (b) $\boldsymbol{\theta}_{*}$ is a regular point of $A_{f}(\theta)$.

Let $\sigma_{X}^{n}$ be the $n$-product of $\sigma_{X}$. The (quasi) maximum likelihood (ML) estimator $\hat{\theta}_{n}$ for the conditional model $\boldsymbol{F}_{\theta}$ is a $\sigma_{X}^{n}$ measurable function of ( $X_{1}, \ldots, X_{n}$ ) such that

$$
L_{n}^{f}\left(\hat{\theta_{n}}\right)=\sup _{\theta \in \Theta} L_{n}^{f}(\theta)
$$

where $L_{n}^{f}(\theta)$ is the conditional $\log$-likelihood function for the model $\boldsymbol{F}_{\theta}$ :

$$
L_{n}^{f}(\theta) \equiv \sum_{t=1}^{n} \log f\left(Y_{t} \mid Z_{t} ; \theta\right)
$$

A similar definition applies to the ML estimator $\hat{\gamma}_{n}$ for the conditional model $\boldsymbol{G}_{\gamma}$ with respect to the conditional log-likelihood function:

$$
L_{n}^{g}(\gamma) \equiv \sum_{t=1}^{n} \log g\left(Y_{t} \mid Z_{t} ; \gamma\right)
$$

Given Assumptions A1-A5, it follows from White (1982a) among others that the ML estimator $\hat{\theta}_{n}$ exists, is consistent for $\theta_{*}$, and is asymptotically normally distributed with asymptotic covariance matrix $A_{f}^{-1}\left(\theta_{*}\right) B_{f}\left(\theta_{*}\right) A_{f}^{-1}\left(\theta_{*}\right)$. Similar properties hold for the ML estimator $\hat{\gamma}_{n}$ of $\gamma_{*}$. As a matter of fact, $\hat{\theta}_{n}$ and $\hat{\gamma}_{n}$ are jointly asymptotically normal (see Lemma A in the Appendix) with asymptotic covariance matrix that can be consistently estimated using the sample analogs of $A_{s}(\theta), B_{s}(\theta)$, and $B_{f g}(\theta, \gamma), s=f, g$, evaluated at $\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)$. For instance, $B_{f g}\left(\theta_{*}, \gamma_{*}\right)$
is consistently estimated by:

$$
B_{f g n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)=\frac{1}{n} \sum_{t=1}^{n} \frac{\partial \log f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right)}{\partial \theta} \cdot \frac{\partial \log g\left(Y_{t} \mid Z_{t} ; \hat{\gamma}_{n}\right)}{\partial \gamma^{\prime}} .
$$

## 3. THE LIKELIHOOD RATIO STATISTIC

All our tests for model selection are based on the likelihood ratio (LR) statistic. In this section, we obtain the asymptotic distribution of the LR statistic under the most general conditions. The LR statistic for the model $\boldsymbol{F}_{\theta}$ against the model $\boldsymbol{G}_{\gamma}$ is:

$$
L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) \equiv L_{n}^{f}\left(\hat{\theta}_{n}\right)-L_{n}^{g}\left(\hat{\gamma}_{n}\right)=\sum_{t=1}^{n} \log \frac{f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right)}{g\left(Y_{t} \mid Z_{t} ; \hat{\gamma}_{n}\right)},
$$

where $\hat{\theta}_{n}$ and $\hat{\gamma}_{n}$ are the ML estimators of $\theta_{*}$ and $\gamma_{*}$.
Lemma 3.1: Given Assumptions A1-A3:

$$
\frac{1}{n} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) \xrightarrow{\text { a.s. }} E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right] .
$$

This result is important because it motivates our LR-based tests for model selection. To derive the asymptotic distribution of the LR statistic, we consider distributions of quadratic forms in normal random variables. Such distributions have been studied by, e.g., Johnson and Kotz (1970, Chapter 29). We call such distributions weighted sums of (independent) chi-square distributions, for which we give the following definition.

Definition 1 (Weighted Sums of Chi-Square Distributions): Let $Z= \left(Z_{1}, \ldots, Z_{m}\right)^{\prime}$ be a vector of $m$ independent standard normal variables, and let $\lambda=\left(\lambda_{1}, \ldots, \lambda_{m}\right)^{\prime}$ be a vector of $m$ real numbers. Then, the random variable $\sum_{i=1}^{m} \lambda_{i} Z_{i}^{2}$ is distributed as a weighted sum of chi-squares with parameters ( $m, \lambda$ ). Its cumulative distribution function (c.d.f.) is denoted by $M_{m}(\cdot ; \lambda)$.

The next lemma shows that any quadratic form in $m$ random variables that are jointly normally distributed with zero means and some covariance matrix $\Omega$ is distributed as a weighted sum of chi-squares with some parameters $m$ and $\lambda$. This result allows $\Omega$ to be singular, and slightly differs from Moore (1978, Theorem 1).

Lemma 3.2: Let $Y$ be a vector of $m$ random variables distributed as $N(0, \Omega)$ with rank $\Omega \leqslant m$. Let $Q$ be a $m \times m$ real symmetric matrix. Then

$$
Y^{\prime} Q Y \sim M_{m}(\cdot ; \lambda)
$$

where $\lambda$ is the vector of eigenvalues of $Q \Omega$. Moreover, the eigenvalues are all real, and they are all nonnegative if $Q$ is positive semi-definite.

We can now readily obtain the asymptotic distribution of the LR statistic under general conditions. Let $\omega_{*}^{2}$ denote the variance of $\log \left[f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right) /\right. \left.g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)\right]$, where the variance is computed with respect to the true joint distribution $H_{X}^{0}$ of ( $Y_{t}, Z_{t}$ ). That is:

$$
\begin{aligned}
\omega_{*}^{2} & \equiv \operatorname{var}^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right] \\
& =E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right]^{2}-\left[E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right]\right]^{2}
\end{aligned}
$$

To ensure that such a variance exists, we make the following assumption.
Assumption A6: For $H_{X}^{0}$-almost all $(y, z)$ the functions $|\log f(y \mid z ; \cdot)|^{2}$ and $|\log g(y \mid z ; \cdot)|^{2}$ are dominated by $H_{X}^{0}$-integrable functions independent of $\theta$ and $\gamma$.

Theorem 3.3 (Asymptotic Distribution of the LR Statistic): Given Assumptions A1-A5:
(i) if $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$, then

$$
2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) \xrightarrow{D} M_{p+q}\left(\cdot ; \lambda_{*}\right),
$$

where $\lambda_{*}$ is the vector of $p+q$ (possibly negative) eigenvalues of

$$
W=\left[\begin{array}{cc}
-B_{f}\left(\theta_{*}\right) A_{f}^{-1}\left(\theta_{*}\right) ; & -B_{f g}\left(\theta_{*}, \gamma_{*}\right) A_{g}^{-1}\left(\gamma_{*}\right) \\
B_{g f}\left(\gamma_{*}, \theta_{*}\right) A_{f}^{-1}\left(\theta_{*}\right) ; & B_{g}\left(\gamma_{*}\right) A_{g}^{-1}\left(\gamma_{*}\right)
\end{array}\right],
$$

(ii) if $f\left(\cdot \mid \cdot ; \theta_{*}\right) \neq g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ and Assumption A6 holds, then

$$
n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)-n^{1 / 2} E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right] \xrightarrow{D} N\left(0, \omega_{*}^{2}\right) .
$$

Throughout, the condition $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ is to be understood as holding for $H_{X}^{0}$-almost all $(y, z)$, i.e., as $H_{X}^{0}\left[(y, z): f\left(y \mid z ; \theta_{*}\right)=g\left(y \mid z ; \gamma_{*}\right)\right]=1$. Its interpretation is that the distributions in $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ that are closest to the true conditional distribution $H_{Y \mid Z}^{0}(\cdot \mid \cdot)$ are observationally identical under $H_{X}^{0}$. Theorem 3.3 characterizes the asymptotic distribution of the LR statistic under general conditions. It shows that the asymptotic distribution of the LR statistic as well as the rate of convergence to that distribution depends on whether or not $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$.

The limiting weighted sum of chi-square distributions that arises when $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ is somewhat unusual. It is useful to characterize the conditions under which this limiting distribution reduces to the familiar chi-square distribution. This is the purpose of the next result. For this result, we assume that the information matrix equivalence holds for both $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$, i.e.:

$$
A_{f}\left(\theta_{*}\right)+B_{f}\left(\theta_{*}\right)=0 \quad \text { and } \quad A_{g}\left(\gamma_{*}\right)+B_{g}\left(\gamma_{*}\right)=0
$$

As shown in White (1982a, Theorem 3.3), the information matrix equivalences hold under correct specification of the conditional models given mild additional assumptions.

Corollary 3.4 (Asymptotic Chi-Square Distribution of the LR Statistic given Information Matrix Equivalences): Given Assumptions A1-A5, suppose that (3.8) holds. If $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$, then $2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)$ converges to a central chisquare distribution if and only if:

$$
B_{g}\left(\gamma_{*}\right)-B_{g f}\left(\gamma_{*}, \theta_{*}\right) B_{f}^{-1}\left(\theta_{*}\right) B_{f g}\left(\theta_{*}, \gamma_{*}\right)=0
$$

in which case the number of degrees of freedom is $p-q$.
As seen in Section 7, (3.9) is satisfied when $\boldsymbol{G}_{\gamma}$ is nested in $\boldsymbol{F}_{\theta}$.

## 4. THE VARIANCE STATISTIC

In the previous section, we show that whether the LR statistic is asymptotically distributed as a normal or a weighted sum of chi-squares depends on whether $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$. Such a condition may hold when the conditional models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are nested or overlapping. It is therefore important to know if it is satisfied. Since $\theta_{*}$ and $\gamma_{*}$ are unknown, we propose in this section a test of such a condition. The proposed test is based on the following property.

Lemma 4.1: Given Assumptions $A 1-(b), A 2, A 3$, and $A 6, f\left(\cdot \mid \cdot ; \theta_{*}\right)= g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ if and only if $\omega_{*}^{2}=0$.

Thus, to test the crucial condition $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ one can equivalently test that the variance $\omega_{*}^{2}$ is equal to zero. We define the following null and alternative hypotheses:

$$
H_{0}^{\omega}: \omega_{*}^{2}=0 \quad \text { vs. } \quad H_{A}^{\omega}: \omega_{*}^{2} \neq 0
$$

A natural statistic that we can use to test $H_{0}^{\omega}$ against $H_{A}^{\omega}$ is the sample analog:

$$
\hat{\omega}_{n}^{2} \equiv \frac{1}{n} \sum_{t=1}^{n}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right)}{g\left(Y_{t} \mid Z_{t} ; \hat{\gamma}_{n}\right)}\right]^{2}-\left[\frac{1}{n} \sum_{t=1}^{n} \log \frac{f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right)}{g\left(Y_{t} \mid Z_{t} ; \hat{\gamma}_{n}\right)}\right]^{2} .
$$

Note that $\omega_{*}^{2}$ is the variance of the limiting normal distribution of the LR statistic (Theorem 3.3-(ii)). Thus the variance statistic $\hat{\omega}_{n}^{2}$ plays two roles: first, to be a basis for a test of $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$; second, to be an estimator of the asymptotic variance of the LR statistic when $f\left(\cdot \mid \cdot ; \theta_{*}\right) \neq g\left(\cdot \mid \cdot ; \gamma_{*}\right)$.

An alternative statistic is

$$
\tilde{\omega}_{n}^{2} \equiv \frac{1}{n} \sum_{t=1}^{n}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right)}{g\left(Y_{t} \mid Z_{t} ; \hat{\gamma}_{n}\right)}\right]^{2}=\hat{\omega}_{n}^{2}+\left(\frac{1}{n} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)\right)^{2} .
$$

The next lemma states that these statistics are strongly consistent estimators of their population analogs.

Lemma 4.2: Given Assumptions $A 1-A 3$, and A6:
(i) $\hat{\omega}_{n}^{2} \xrightarrow{\text { a.s. }} \omega_{*}^{2}$,
(ii) $\tilde{\omega}_{n}^{2} \xrightarrow{\text { a.s. }} \omega_{*}^{2}+\left[E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right]\right]^{2}$.

To construct a test of $H_{0}^{\omega}$ against $H_{A}^{\omega}$, it is necessary to derive the asymptotic distribution of the variance statistic $\hat{\omega}_{n}^{2}$ or $\tilde{\omega}_{n}^{2}$. We make the following assumption.

Assumption a7: For $H_{X}^{0}$-almost all $(y, z)$ the functions $\mid \log [f(y \mid z ; \cdot) / g(y \mid z ; \cdot)] \cdot \partial^{2} \log f(y \mid z ; \cdot) / \partial \theta \partial \theta^{\prime} \mid$ and $\mid \log [f(y \mid z ; \cdot) / g(y \mid z ; \cdot)] \cdot \partial^{2} \log g(y \mid z ; \cdot) / \partial \gamma \partial \gamma^{\prime} \mid$ are dominated by $H_{X}^{0}$-integrable functions independent of $\theta$ and $\gamma$.

Theorem 4.3 (Asymptotic Distribution of the Variance Statistics given $\omega^{2}=0$ ): Given Assumptions A1-A7, under $H_{0}^{\omega}$ :

$$
n \hat{\omega}_{n}^{2}=n \tilde{\omega}_{n}^{2}+o_{p}(1) \xrightarrow{D} M_{p+q}\left(\cdot ; \lambda_{*}^{2}\right)
$$

where $\lambda_{*}^{2}$ is the vector of squares of the $p+q$ eigenvalues $\lambda_{*}$ of $W$.
Theorem 4.3 says that, under the null hypotheses $H_{0}^{\omega}$, the two statistics $n \hat{\omega}_{n}^{2}$ and $n \tilde{\omega}_{n}^{2}$ are asymptotically equivalent, and have a limiting distribution which is again a weighted sum of chi-squares. The parameters $\lambda_{*}^{2}$ are, as expected, all nonnegative.

As for the LR statistic, it is of interest to know when the limiting weighted sum of chi-square distribution of the variance statistics reduces to the familiar central chi-square distribution. The next result characterizes this situation. As for Theorem 3.6, we assume that the information matrix equivalences (3.8) hold.

Corollary 4.4 (Asymptotic Chi-Square Distribution of the Variance Statistics Given Information Matrix Equivalences and $\omega_{*}^{2}=0$ ): Given Assumptions A1-A7, suppose that (3.8) holds. Then, under $H_{0}^{\omega}: \omega_{*}^{2}=0$, the following statements are equivalent: (i) $n \hat{\omega}_{n}^{2}$ converges in distribution to a chi-square, (ii) $n \tilde{\omega}_{n}^{2}$ converges in distribution to a chi-square, (iii) $B_{f g}\left(\theta_{*}, \gamma_{*}\right) B_{g}^{-1}\left(\gamma_{*}\right) B_{g f}\left(\gamma_{*}, \theta_{*}\right) B_{f}^{-1}\left(\theta_{*}\right)$ is idempotent, (iv) $B_{g f}\left(\gamma_{*}, \theta_{*}\right) B_{f}^{-1}\left(\theta_{*}\right) B_{f g}\left(\theta_{*}, \gamma_{*}\right) B_{g}^{-1}\left(\gamma_{*}\right)$ is idempotent; in which case the number of degrees of freedom is $p+q-2 \operatorname{rank} B_{f g}\left(\theta_{*}, \gamma_{*}\right)$.

As shown in Section 7, conditions (iii) or (iv) are satisfied if $\boldsymbol{G}_{\gamma}$ is nested in $\boldsymbol{F}_{\boldsymbol{\theta}}$ or if $\boldsymbol{F}_{\theta}$ is nested in $\boldsymbol{G}_{\gamma}$. Conditions (iii) and (iv) can also be satisfied when the models are non-nested or overlapping. In particular, they are satisfied when the conditional models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are asymptotically orthogonal as defined by


[^0]:    ${ }^{1}$ This research was supported by National Science Foundation Grant SES-8410593. An early version was presented at the North American Econometric Society meeting, New Orleans, 1986. I am indebted to P. Bjorn, D. Lien, D. Rivers, the co-editor, two referees, and seminar participants at the University of Southern California, University of California-Berkeley, Stanford University, University of Minnesota, University of Wisconsin, Yale University, MIT/Harvard University, University of Pennsylvania, University of Florida-Gainesville, North Carolina State/Duke University, Indiana University, and University of California-Irvine. I would like to thank especially H. White whose comments much improved this paper. I am grateful to C. R. Jackson and to L. Donnelly for stimulating thoughts. Remaining errors are mine. This paper is dedicated to some of my former colleagues at Caltech.

[^1]:    ${ }^{2}$ Most of the results of this paper hold under the weaker assumption that $\nu_{Y}$ is absolutely continuous relative to $H_{Y \mid Z}^{0}(\cdot \mid z)$ for $H_{Z}^{0}$-almost all $z$. This latter assumption says that the non-negligible sets relative to $\nu_{Y}$ are also non-negligible relative to $H_{Y \mid Z}^{0}(\cdot \mid z)$. It does not require that $H_{Y \mid Z}^{0}(\cdot \mid z)$ have a density relative to $\nu_{Y}$.



Gourieroux, Monfort, and Trognon (1983), i.e., when:

$$
B_{f g}\left(\theta_{*}, \gamma_{*}\right)=0
$$

in which case the number of degrees of freedom is $p+q$.

## 5. STRICTLY NON-NESTED MODELS

In Section 1, we suggested a classical approach for selecting among competing models. In this section, we shall discuss this approach in more detail. In particular, using the results of Sections 3 and 4, we shall obtain very simple tests for selecting among two competing models whether they are nested or misspecified. Following Akaike (1973, 1974), Sawa (1978), and Chow (1981), our approach is based on the minimum KLIC which measures the distance between the true distribution and a specified model. For the conditional model $\boldsymbol{F}_{\theta}$, this measure gives:

$$
K L I C\left(H_{Y \mid Z}^{0} ; \boldsymbol{F}_{\theta}\right) \equiv E^{0}\left[\log h^{0}\left(Y_{t} \mid Z_{t}\right)\right]-E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)\right],
$$

where $h^{0}(\cdot \mid \cdot)$ is the true conditional density of $Y_{t}$ given $Z_{t}$, and $\theta_{*}$ are the pseudo-true values of $\theta$. From Jensen's inequality, the measure (5.1) is always nonnegative and is equal to zero if and only if $h^{0}(\cdot \mid \cdot)=f\left(\cdot \mid \cdot ; \theta_{*}\right) H_{X}^{0}$-almost surely, i.e., if and only if $\boldsymbol{F}_{\theta}$ is correctly specified. Moreover, since the first term in the right-hand side of (5.1) does not depend on $\boldsymbol{F}_{\theta}$, then an equivalent measure is $E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)\right]$.

Given a pair of competing conditional models, it is natural to select the model that is closest to the true conditional distribution. Given the above measure of distance, we consider the following hypotheses and definitions:

$$
H_{0}: E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right]=0
$$

meaning that $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are equivalent, against

$$
H_{f}: E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right]>0
$$

meaning that $\boldsymbol{F}_{\boldsymbol{\theta}}$ is better than $\boldsymbol{G}_{\gamma}$, or

$$
H_{g}: E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right]<0
$$

meaning that $\boldsymbol{F}_{\theta}$ is worse than $\boldsymbol{G}_{\gamma}$. These definitions have the desirable property that a correctly specified model must be at least as good as any other model. ${ }^{3}$ Thus, if one rejects $H_{0}$ in favor of $H_{f}$, say, then $\boldsymbol{G}_{\gamma}$ must be misspecified.

[^0]Another property is that the null hypothesis $H_{0}$ does not require that either of the competing models be correctly specified. As a matter of fact, from Lemma 6.2 below, both models must be misspecified under $H_{0}$ if $f\left(\cdot \mid \cdot ; \theta_{*}\right) \neq g\left(\cdot \mid \cdot ; \gamma_{*}\right)$.

The indicator $E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)\right]-E^{0}\left[\log g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)\right]$ is, however, unknown. But we can consistently estimate this indicator by $(1 / n)$ times the LR statistic under general conditions (Lemma 3.1). Thus the LR statistic is a natural statistic for discriminating between two models. Tests of $H_{0}$ against $H_{f}$ or $H_{g}$ will be called tests for model selection.

Since Cox's $(1961,1962)$ initial work, non-nested models have attracted a lot of interest (see, e.g., Mackinnon's (1983) recent survey and the special issue of the Journal of Econometrics edited by White (1983)). For a long time, non-nested hypotheses were defined as hypotheses that cannot be obtained from each other by a suitable limiting approximation (Cox (1961, 1962)). Noting that there were no satisfactory definitions, Pesaran (1987) recently proposed definitions of globally non-nested, partially non-nested, and nested hypotheses. It can be shown that Pesaran's definitions are equivalent to our Definitions 2, 3, and 4 below. Our definitions are more intuitive.

In this section, we consider the case where the models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are (strictly) non-nested. We give the following formal definition.

Definition 2 (Strictly Non-Nested Models): Two conditional models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are strictly non-nested if and only if:

$$
\boldsymbol{F}_{\theta} \cap \boldsymbol{G}_{\gamma}=\phi
$$

Since conditional distributions for $Y_{t}$ given $Z_{t}$ are defined on $\sigma_{Y} \times \boldsymbol{Z}$, and since some values of $z$ may not be observed, condition (5.5) is to be understood as meaning that there is no conditional distribution for $Y_{t}$ given $Z_{t}$ which is equal to an element of $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ for $H_{Z}^{0}$-almost all $z$. A similar remark applies to Definitions 3 and 4 below. Condition (5.5) is satisfied when $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are standard linear regression models with different distributional assumptions on the errors, say normally or logistic distributed. Alternatively, the competing regression models may have the same distributional assumption but different functional forms such as $Y_{t}=\theta_{1}+\theta_{2}^{\prime} Z_{t}+e_{f t}$ and $Y_{t}=\exp \left(\gamma_{1}+\gamma_{2}^{\prime} Z_{t}\right)+e_{g t}$ where $\theta_{2} \neq 0, \gamma_{2} \neq 0$, and $Z_{t}$ is a nondegenerate real random vector.

Since the conditional models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ do not have any conditional distribution in common, it must be the case that $f\left(\cdot \mid \cdot ; \theta_{*}\right) \neq g\left(\cdot \mid \cdot ; \gamma_{*}\right) .^{4}$ It follows that the second part of Theorem 3.3 applies. Moreover, from Lemma 4.2, the asymptotic variance $\omega_{*}^{2}$ can be consistently estimated by $\hat{\omega}_{n}^{2}$ or by $\tilde{\omega}_{n}^{2}$ under $H_{0}$. Thus we have the following straightforward model selection test. Let $\hat{\omega}_{n}$ and $\tilde{\omega}_{n}$ be the positive square roots of $\hat{\omega}_{n}^{2}$ and $\tilde{\omega}_{n}^{2}$ respectively.

[^1]Theorem 5.1 (Model Selection Tests for Strictly Non-Nested Models): Given Assumptions A1-A6, if $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are strictly non-nested, then
(i) under $H_{0}: n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n} \xrightarrow{D} N(0,1)$,
(ii) under $H_{f}: n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n} \xrightarrow{\text { a.s. }}+\infty$,
(iii) under $H_{g}: n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n} \xrightarrow{\text { a.s. }}-\infty$,
(iv) properties (i)-(iii) hold if $\hat{\omega}_{n}$ is replaced by $\tilde{\omega}_{n}$.

Theorem 5.2 provides very simple directional tests for model selection. Specifically, one chooses a critical value $c$ from the standard normal distribution for some significance level. If the value of the statistic $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}$ is higher than $c$ then one rejects the null hypothesis that the models are equivalent in favor of $\boldsymbol{F}_{\theta}$ being better than $\boldsymbol{G}_{\gamma}$. If $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}$ is smaller than $-c$ then one rejects the null hypothesis in favor of $\boldsymbol{G}_{\gamma}$ being better than $\boldsymbol{F}_{\theta}$. Finally if $\left|n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}\right| \leqslant c$, then one cannot discriminate between the two competing models given the data. Similar inferences can be based on the other statistic $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \tilde{\omega}_{n}$.

Both statistics are easy to compute. Each one is equal to the difference in the maximum log-likelihood values for the two models suitably normalized. The normalization $n^{1 / 2} \tilde{\omega}_{n}$ is obtained from the sum of squares of $m_{t} \equiv \log \left[f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right) / g\left(Y_{t} \mid Z_{t} ; \hat{\gamma}_{n}\right)\right]$, while the normalization $n^{1 / 2} \hat{\omega}_{n}$ is obtained from the sum of squared deviations of $m_{t}$ from its sample mean which is equal to $(1 / n) L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)$. See (4.2)-(4.3). Alternatively, these statistics can be readily obtained from an additional linear regression. For instance, it can be shown that $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}$ is numerically equal to $[(n-1) / n]^{1 / 2}$ times either the usual $t$ statistic on the constant term in a linear regression of $m_{t}$ on only the constant term, or the usual $t$ statistic on the coefficient of $m_{t}$ in a linear regression of 1 on $m_{t}{ }^{5}$

The previous tests are based on the unadjusted LR statistic. There are, however, many equivalent statistics that can be used to form a model selection test. For instance, we may consider the following adjusted LR statistic:

$$
L \tilde{R}_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) \equiv L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)-K_{n}\left(\boldsymbol{F}_{\theta}, \boldsymbol{G}_{\gamma}\right),
$$

where $K_{n}\left(\boldsymbol{F}_{\theta}, \boldsymbol{G}_{\gamma}\right)$ is a correction factor depending on the characteristics of the competing models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ such as their number of parameters. Suppose that:

$$
n^{-1 / 2} K_{n}\left(\boldsymbol{F}_{\theta}, \boldsymbol{G}_{\gamma}\right)=o_{p}(1) .
$$

Examples of correction factors that satisfy (5.10) are $K_{n}\left(\boldsymbol{F}_{\theta}, \boldsymbol{G}_{\gamma}\right)=p-q$ and $K_{n}\left(\boldsymbol{F}_{\theta}, \boldsymbol{G}_{\gamma}\right)=(p / 2) \log n-(q / 2) \log n$, which correspond to Akaike (1973) and Schwarz (1978) information criteria. It is clear that $n^{-1 / 2} L \tilde{R}_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}$ has the same asymptotic properties as $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}$. Hence, we can use the adjusted log-likelihood ratio $L \tilde{R}_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)$ as a basis for a model selection test. In

[^2]terms of the unadjusted LR statistic, we would accept $H_{0}$ whenever
$$
\begin{aligned}
-c+n^{-1 / 2} K_{n}\left(\boldsymbol{F}_{\theta}, \boldsymbol{G}_{\gamma}\right) / \hat{\omega}_{n} \leqslant n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n} \leqslant c+ \\
n^{-1 / 2} K_{n}\left(\boldsymbol{F}_{\theta}, \boldsymbol{G}_{\gamma}\right) / \hat{\omega}_{n}
\end{aligned}
$$
where $c$ is obtained from the standard normal distribution. Thus the main effect of the correction factor $K_{n}\left(\boldsymbol{F}_{\boldsymbol{\theta}}, \boldsymbol{G}_{\boldsymbol{\gamma}}\right)$ is to translate the critical region ( $-c,+c$ ) in the appropriate direction. Which correction factor is preferable depends on how well the exact small sample distribution of $n^{-1 / 2} L \tilde{R}_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}$ is approximated under $H_{0}$ by the asymptotic $N(0,1)$ distribution. In the next sections on overlapping models and nested models, we shall not discuss possible adjustments to the LR statistic. Similar results can clearly be established.

We now contrast our approach to those initiated by Akaike $(1973,1974)$ on model selection and Cox $(1961,1962)$ on non-nested hypothesis testing. First, the difference between Akaike's and our approach is that ours is probabilistic. Though Amemiya (1980) and McAleer and Bera (1983) have argued that an important difference between non-nested hypothesis testing and model selection is that the former framework allows "a probabilistic statement to be made regarding model selection," while the second does not, this criticism no longer applies to our approach which puts model selection in a significance testing situation. As in the classical testing situation, our distributional results are used to indicate the strength of the evidence in favor of either model whether it is based on the adjusted or unadjusted LR statistic. As a consequence we do not have to choose a "best" model if the competing models are statistically equivalent.

Second, the difference between Cox's and our approach lies in the null hypotheses under test. In Cox's approach, the implicit null hypothesis when testing $\boldsymbol{F}_{\boldsymbol{\theta}}$ using the evidence providing by $\boldsymbol{G}_{\gamma}$, say, is:

$$
\begin{aligned}
H_{0}^{f}: & E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right] \\
& =\int_{Z} \int_{Y} \log \frac{f\left(y \mid z ; \theta_{*}\right)}{g\left(y \mid z ; \gamma_{*}\right)} f\left(y \mid z ; \theta_{*}\right) v_{Y}(d y) H_{Z}^{0}(d z)
\end{aligned}
$$

(see Aguirre-Torres and Gallant (1983), White (1982b)). Hence $H_{0}^{f}$ and $H_{0}$ are in general different. As a matter of fact, these null hypotheses are identical if and only if $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid ; \gamma_{*}\right)$, which cannot hold when the models are strictly non-nested. Moreover, it is well-known that $H_{0}^{f}$ holds if $\boldsymbol{F}_{\theta}$ is correctly specified. On the other hand, as noticed earlier, when the competing models are strictly non-nested, both models must be misspecified under our null hypothesis $H_{0}$.

## 6. OVERLAPPING MODELS

In this section, we consider the case where the two competing models are overlapping. A simple example of two overlapping models is that of two standard
linear regression models with some common explanatory variables. We first give a formal definition of overlapping models.

Definition 3 (Overlapping Models): Two conditional models $\boldsymbol{F}_{\boldsymbol{\theta}}$ and $\boldsymbol{G}_{\gamma}$ are overlapping if and only if:

$$
\text { (i) } \boldsymbol{F}_{\theta} \cap \boldsymbol{G}_{\gamma} \neq \phi \text {, }
$$

$$
\text { (ii) } \boldsymbol{F}_{\theta} \not \subset \boldsymbol{G}_{\gamma} \text { and } \boldsymbol{G}_{\gamma} \subset \boldsymbol{F}_{\theta} \text {. }
$$

Condition (i) says that $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ have some common conditional distributions for $Y_{t}$ given $Z_{t}$ for $H_{Z}^{0}$-almost all $z$, while condition (ii) says that neither model is nested in the other.

As in the previous section, our objective is to construct tests of $H_{0}$ against $H_{f}$ or $H_{g}$. Given the definitions (5.2)-(5.4) of these hypotheses, a natural test statistic is again the LR statistic. The overlapping case is, however, more difficult than the strictly non-nested case for the following reason. Since $\boldsymbol{F}_{\boldsymbol{\theta}} \cap \boldsymbol{G}_{\boldsymbol{\gamma}} \neq \phi$, then one may have $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$. From Theorem 3.3, it follows that under the null hypothesis $H_{0}$ :

$$
\text { (i) if } f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right), 2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) \xrightarrow{D} M_{p+q}\left(\cdot, \lambda_{*}\right) \text {, }
$$

$$
\text { (ii) if } f\left(\cdot \mid \cdot ; \theta_{*}\right) \neq g\left(\cdot \mid \cdot ; \gamma_{*}\right), n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) \xrightarrow{D} N\left(0, \omega_{*}^{2}\right) \text {. }
$$

For instance, in the normal linear regression case with some common explanatory variables, (i) occurs if and only if the pseudo-true parameters associated with the variables specific to each regression are simultaneously null (see Lien and Vuong (1987)). A stronger condition is that $H_{Y \mid Z}^{0}(\cdot \mid \cdot)$ is common to the two competing linear models, or equivalently that both linear models are correctly specified. Since one does not know a priori if $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ holds, i.e., if the distributions in $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ that are closest to $H_{Y \mid Z}^{0}(\cdot \mid \cdot)$ are observationally identical, one does not know the form of the asymptotic distribution of the LR statistic under the null hypothesis $H_{0}$. We distinguish two cases: the general case and the case where one knows a priori that at least one model is correctly specified.

For the general case we propose a sequential procedure which consists in testing first whether $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ and then in using the appropriate null distribution of the LR statistic to construct a model selection test. From Lemma 4.1, we know that $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ if and only if $\omega_{*}^{2}=0$. Thus, for the first step, a natural test can be based on the variance statistics $\hat{\omega}_{n}^{2}$ and $\tilde{\omega}_{n}^{2}{ }^{6}$ Such a test is called the variance test. Once it is known whether $\omega_{*}^{2}=0$, one can use the appropriate null distribution of the LR statistic to test $H_{0}$ against $H_{f}$ or $H_{g}$. The second step simplifies since one need not carry out a test of $H_{0}$ against $H_{f}$ or $H_{g}$ when $\omega_{*}^{2}=0$. Indeed $H_{0}^{\omega}$ is clearly included in $H_{0}$ so that $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$

[^3]must necessarily be equivalent when $\omega_{*}^{2}=0$. On the other hand, when $\omega_{*}^{2} \neq 0$, one may have $E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)\right]=E^{0}\left[\log g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)\right]$ so that a test of $H_{0}$ against $H_{f}$ or $H_{g}$ must still be carried out. But, when $\omega_{*}^{2} \neq 0$, (6.4) holds so that the simple normal test based on $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}$ or $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \tilde{\omega}_{n}$ discussed in Section 5 applies.

To summarize, the sequential procedure is: (i) Test $H_{0}^{\omega}$ against $H_{A}^{\omega}$ using the variance test based on $n \hat{\omega}_{n}^{2}$ or $n \tilde{\omega}_{n}^{2}$. If $H_{0}^{\omega}$ is not rejected, conclude that $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ cannot be discriminated given the data. If $H_{0}^{\omega}$ is rejected, (ii) test $H_{0}$ against $H_{f}$ or $H_{g}$ using the normal model selection test based on $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}$ or $n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \tilde{\omega}_{n}$ as discussed in Section 5.

As a test of the null hypothesis of interest $H_{0}$ that the models are equivalent, this sequential procedure has a significance level which is asymptotically bounded above by the maximum of the asymptotic significance levels $\alpha_{1}$ and $\alpha_{2}$ used for the variance test and the normal LR-test. To see this, note that $H_{0}$ is a composite of $H_{0}^{\omega}$ and $H_{0}-H_{0}^{\omega}$. Let $A \equiv\left\{n \hat{\omega}_{n}^{2}>c_{1}\right\}$ and $B \equiv\left\{\left|n^{-1 / 2} L R\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) / \hat{\omega}_{n}\right|>c_{2}\right\}$. Then $\operatorname{Pr}\left[\right.$ reject $\left.H_{0} \mid H_{0}\right]=\operatorname{Pr}\left[A \cap B \mid H_{0}\right] \leqslant \max \left\{\operatorname{Pr}\left(A \cap B \mid H_{0}^{\omega}\right), \operatorname{Pr}(A \cap B \mid\right. \left.\left.H_{0}-H_{0}^{\omega}\right)\right\} \leqslant \max \left\{\operatorname{Pr}\left(A \mid H_{0}^{\omega}\right), \operatorname{Pr}\left(B \mid H_{0}-H_{0}^{\omega}\right)\right\}$. But from Theorems 5.1 and 6.1 below, $\operatorname{Pr}\left(A \mid H_{0}^{\omega}\right) \rightarrow \alpha_{1}$ and $\operatorname{Pr}\left(B \mid H_{0}-H_{0}^{\omega}\right) \rightarrow \alpha_{2}$. Thus if $\alpha_{1}=\alpha_{2}=.10$, the significance level of the procedure, as a test of $H_{0}$, is asymptotically no larger than $10 \%$.

We now consider in more detail the variance test to be used in the first step. Let $\hat{\lambda}_{n}$ be the vector of $p+q$ eigenvalues of $\hat{W}_{n}$, where $\hat{W}_{n}$ is the sample analog of $W$ as defined in (3.6). For instance, $\hat{W}_{n}$ is obtained by replacing in (3.6) the matrix $B_{f g}\left(\theta_{*}, \gamma_{*}\right)$, say, by its sample analog $B_{f g n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)$ defined in (2.7). Let $\hat{\lambda}_{n}^{2}$ be the vector of squares of $\hat{\lambda}_{n}$.

Theorem 6.1 (Variance Tests for Discrimination): Given Assumptions A1-A7,
(i) under $H_{0}^{\omega}$, for any $x \geqslant 0, \operatorname{Pr}\left(n \hat{\omega}_{n}^{2} \leqslant x\right)-M_{p+q}\left(x ; \hat{\lambda}_{n}^{2}\right) \xrightarrow{\text { a.s. }} 0$,
(ii) under $H_{A}^{\omega}, n \hat{\omega}_{n}^{2} \xrightarrow{\text { a.s. }}+\infty$,
(iii) properties (i) and (ii) hold for $n \tilde{\omega}_{n}^{2}$.

The variance test consists in choosing a critical value $x$ so that $M_{p+q}\left(x ; \hat{\lambda}_{n}^{2}\right)= 1-\alpha \%$ for some significance level $\alpha$, and in rejecting $H_{0}^{\omega}$ if $n \hat{\omega}_{n}^{2}>x$. ${ }^{7}$ Part (i) ensures that the asymptotic size is $\alpha$, while (ii) says that the test is consistent. Similar conclusions apply to the test based on $n \tilde{\omega}_{n}^{2}$. Computation of the statistic $n \hat{\omega}_{n}^{2}$ and $n \tilde{\omega}_{n}^{2}$ is straightforward. The test also requires the computation of the eigenvalues $\hat{\lambda}_{n}$. The eigenvalues need not, however, be computed when rank $B_{f g}\left(\theta_{*}, \gamma_{*}\right)$ is known and condition (iii) or (iv) of Corollary 4.4. holds. (Orthogonal models fullfill such requirements.) In this case, both $n \hat{\omega}_{n}^{2}$ and $n \tilde{\omega}_{n}^{2}$ converge, under $H_{0}^{\omega}$, to a chi-square distribution with degrees of freedom equal to $p+q-$ 2 rank $B_{f g}\left(\theta_{*}, \gamma_{*}\right)$.

[^4]As pointed our earlier, the difficulty in selecting among overlapping models arises from the fact that $f\left(\cdot \mid \cdot ; \theta_{*}\right)$ may or may not be equal to $g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ under the null hypothesis of interest $H_{0}$ so that the form of the asymptotic null distribution of the LR statistic is a priori unknown. This is not the case if one knows that at least one of the two overlapping models is correctly specified, a frequent assumption in the model selection literature. We say that the conditional model $\boldsymbol{F}_{\theta}$, for instance, is correctly specified if $H_{Y \mid Z}^{0}(\cdot \mid \cdot) \in \boldsymbol{F}_{\theta}$, i.e., if there exists a $\theta_{o}$ in $\Theta$ such that $H_{Y \mid Z}^{0}(\cdot \mid z)=F_{Y \mid Z}\left(\cdot \mid z ; \theta_{o}\right)$ for $H_{Z}^{0}$-almost all $z$.

Lemma 6.2: Given Assumptions A1-(b), A2 and A3, suppose that $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are overlapping and at least one model is correctly specified. Then the following statements are equivalent:
(i) $H_{Y \mid Z}^{0}(\cdot \mid \cdot) \in \boldsymbol{F}_{\theta} \cap \boldsymbol{G}_{\gamma}$,
(ii) $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$,
(iii) $E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)\right]=E^{0}\left[\log g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)\right]$.

From (i) and (iii) it follows that, when at least one model is correctly specified, then the models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are equivalent if and only if the other model is correctly specified. From (ii) and (iii) we have that the models $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are equivalent if and only if $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$. The importance of this second equivalence is that under $H_{0}$, we now always have $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ so that the asymptotic distribution of the LR statistic is given by the weighted sum of chi-squares obtained in Theorem 3.3-(i). Thus in this case we can bypass the above sequential procedure, and directly construct a model selection test based on the LR statistic.

Theorem 6.3 (Model Selection Test for Overlapping Models): Given Assumptions $A 1-A 5$, if $\boldsymbol{F}_{\theta}$ and $\boldsymbol{G}_{\gamma}$ are overlapping and at least one model is correctly specified, then:
(i) under $H_{0}$, for any $x \geqslant 0, \operatorname{Pr}\left(2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) \leqslant x\right)-M_{p+q}\left(x ; \hat{\lambda}_{n}\right) \xrightarrow{\text { a.s. }} 0$,
(ii) under $H_{f}: 2 L R_{n}\left(\hat{\theta}, \hat{\gamma}_{n}\right) \xrightarrow[a]{\text { a.s. }}+\infty$,
(iii) under $H_{g}: 2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right) \xrightarrow{\text { a.s. }}-\infty$.

The LR-based test is carried out by choosing critical values from the weighted sum of chi-squares $M_{p+q}\left(\cdot ; \hat{\lambda}_{n}\right)$. Since the LR-based test is two-sided, two critical values $c_{1}$ and $c_{2}$ are chosen, one from the upper-tail and one from the lower-tail of this distribution. As for the normal LR-based test of Section 5, the test is directional in the sense that $H_{0}$ is rejected in favor of $H_{f}$ or $H_{g}$ according to whether $2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)>c_{1}$ or $2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)<c_{2}$ respectively. Since at least one model is assumed to be correctly specified, then rejection of $H_{0}$ in favor of $H_{f}$, say, implies that $\boldsymbol{F}_{\theta}$ is correctly specified and $\boldsymbol{G}_{\gamma}$ is misspecified. The test requires consistent estimators $\hat{\lambda}_{n}$ of $\lambda_{*}$. If the competing models are asymptotically orthogonal, it can readily be shown from (3.6) that $\lambda_{*}$ is equal to a vector of $p$ ones and $q$ minus ones so that the limiting distribution reduces to that of a difference between two independent chi-squares with $p$ and $q$ degrees of freedom.

## 7. NESTED MODELS

We now consider the more familiar case of nested models. We first relate our probabilistic model selection approach to the classical nested-hypothesis testing situation. Then we propose a LR-based test for selecting between two nested models. This test reduces to the classical Neyman-Pearson (1928) LR test when the largest model is correctly specified. We also propose a new test for nested hypotheses based on the variance statistics of Section 3.

A formal definition of nested models is:

Definition 4 (Nested Models): The conditional model $\boldsymbol{G}_{\gamma}$ is nested in $\boldsymbol{F}_{\theta}$ if and only if:

$$
\boldsymbol{G}_{\gamma} \subset \boldsymbol{F}_{\theta} .
$$

As before, condition (7.1) means that any conditional distribution in $\boldsymbol{G}_{\gamma}$ is equal to a conditional distribution in $\boldsymbol{F}_{\theta}$ for $H_{Z}^{0}$-almost all $z$. We make the following regularity assumption on the parameterizations $\theta$ and $\gamma$.

Assumption A8: There exists a $C^{2}$-function $\phi(\cdot)$ from $\Gamma$ to $\Theta$ such that for any $\gamma$ in $\Gamma$ :

$$
g(\cdot \mid \cdot ; \gamma)=f(\cdot \mid \cdot ; \phi(\gamma)) \quad \text { for }\left(\nu_{Y} \times H_{Z}^{0}\right) \text {-almost } \forall(y, z) \text {. }
$$

Assumption A8 states that any conditional density $g(\cdot \mid \cdot ; \gamma)$ is also a conditional density $f(\cdot \mid \cdot ; \theta)$ for some $\theta$ in $\Theta$. Since $\phi(\Gamma)$ is included in $\Theta$, (7.1) holds so that $\boldsymbol{G}_{\gamma}$ is nested in $\boldsymbol{F}_{\boldsymbol{\theta}}$.

The pseudo-true parameter $\theta_{*}$ is not necessarily equal to $\phi\left(\gamma_{*}\right)$ since $\theta_{*}$ may not belong to $\phi(\Gamma)$. The next result relates the condition $\theta_{*} \in \phi(\Gamma)$ to the condition that $\boldsymbol{F}_{\boldsymbol{\theta}}$ and $\boldsymbol{G}_{\boldsymbol{\gamma}}$ are equivalent, and to the condition that $f\left(\cdot \mid \cdot ; \boldsymbol{\theta}_{\boldsymbol{*}}\right)= g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ for $H_{X}^{0}$-almost all $(y, z)$.

Lemma 7.1: Given Assumptions A1-(b), A2-A3, and A8, the following statements are equivalent:
(i) $\theta_{*}=\phi\left(\gamma_{*}\right)$,
(ii) $\theta_{*} \in \phi(\Gamma)$,
(iii) $E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)\right]=E^{0}\left[\log g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)\right]$,
(iv) $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$.

Lemma 7.1 shows that our model selection approach coincides with the classical testing approach when the models are nested. For, the condition $H_{0}^{\theta}$ : $\boldsymbol{\theta}_{\boldsymbol{*}} \in \phi(\Gamma)$ can be interpreted as the condition that $\boldsymbol{\theta}_{\boldsymbol{*}}$ satisfies some restrictions, and thus corresponds to the parametric null hypothesis of the classical testing framework. On the other hand, the null hypothesis in our model selection approach is $H_{0}$. From (ii) and (iii), we have that $H_{0}^{\theta}$ and $H_{0}$ are equivalent, as must be their respective alternatives $H_{A}^{\theta}: \theta_{*} \notin \phi(\Gamma)$ and $H_{f} \cup H_{g}$. As a matter of fact, the alternative to the null hypothesis $H_{0}$ is $H_{f}$ since $H_{g}$ can never occur
because $\boldsymbol{G}_{\gamma}$ can never be better than $\boldsymbol{F}_{\theta}$. Hence, Lemma 7.1 says that testing whether or not $\theta_{*}$ satisfies some restrictions is equivalent to testing whether the smaller model is equivalent to or worse than the larger model.

As argued earlier, the LR statistic is a natural statistic for selecting among models. Thus, we shall consider a LR-based test of $H_{0}$ against $H_{f}$ or equivalently of $H_{0}^{\theta}$ against $H_{A}^{\theta}$. From Lemma 7.1, we always have $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ under the null hypothesis $H_{0}$. Hence, there is no ambiguity as to the asymptotic distribution of the LR statistic which is the weighted sum of chi-squares obtained in Theorem 3.3-(i). It is convenient to define $\tilde{\theta}_{n} \equiv \phi\left(\hat{\gamma}_{n}\right) ; \tilde{\theta}_{n}$ is nothing else than the constrained (quasi) maximum likelihood estimator of $\boldsymbol{\theta}_{\boldsymbol{*}}$ subject to the constraints that $\theta$ belongs to $\phi(\Gamma)$. Then the usual LR statistic of the unconstrained vs. the constrained model is:

$$
L R_{n} \equiv \sum_{t=1}^{n} \log \frac{f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right)}{f\left(Y_{t} \mid Z_{t} ; \tilde{\theta}_{n}\right)}=L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)
$$

where the second equality follows from Assumption A8 and the definition of $\tilde{\theta}_{n}$.
The next result is similar to Kent's (1982) Theorem 3.1, and gives the properties of the model selection or nested hypothesis test based on the LR statistic. It simplifies the computation of the nonzero eigenvalues of $W$ by replacing $W$ by a matrix $\underline{W}$ of lower dimension. Let:

$$
\underline{W}=B_{f}\left(\theta_{*}\right)\left[\frac{\partial \phi\left(\gamma_{*}\right)}{\partial \gamma^{\prime}} A_{g}^{-1}\left(\gamma_{*}\right) \frac{\partial \phi^{\prime}\left(\gamma_{*}\right)}{\partial \gamma}-A_{f}^{-1}\left(\theta_{*}\right)\right],
$$

and let $\underline{\hat{\lambda}}_{n}$ be the vector of $p$ eigenvalues of the sample analog $\underline{W}_{n}$ of $\underline{W}$.
Theorem 7.2 (LR Tests for Nested Models): Given Assumptions A1-A5 and A8, the eigenvalues $\hat{\underline{\hat{x}}}_{n}$ are almost surely all real nonnegative and:
(i) under $H_{0}^{\theta}$, for any $x \geqslant 0, \operatorname{Pr}\left(2 L R_{n} \leqslant x\right)-M_{p}\left(x ; \underline{\hat{\lambda}}_{n}\right) \xrightarrow{\text { a.s. }} 0$,
(ii) under $H_{A}^{\theta}, 2 L R_{n} \xrightarrow{\text { a.s. }}+\infty$.

The test is one sided. It is carried out by choosing a critical value from $M_{p}\left(\cdot ; \underline{\hat{\lambda}}_{n}\right)$ and by rejecting the hypothesis that the models are equivalent or that $\boldsymbol{\theta}^{*}$ belongs to $\phi(\Gamma)$ if twice the LR statistic is greater than this critical value. The test applies whether or not the larger model is correctly specified.

As noted by White (1982a), if the information matrix equivalence holds for the larger model, one has the following corollary.

Corollary 7.3 (LR Tests for Nested Models Given Information Matrix Equivalence): Given Assumptions A1-A5, A8 suppose that $A_{f}\left(\theta_{*}\right)+B_{f}\left(\theta_{*}\right)=0$ :
(i) under $H_{0}^{\theta}, 2 L R_{n} \xrightarrow[a . s .]{D} \chi_{p-q}^{2}$,
(ii) under $H_{A}^{\theta}, 2 L R_{n} \xrightarrow{\text { a.s. }}+\infty$.

The well-known Wilks (1938) result follows since the information matrix equivalence holds if the larger model is correctly specified.

Using the equivalence between $H_{0}^{\theta}$ and $H_{0}$, we have motivated the LR statistic as a basis for a test of $H_{0}^{\theta}$ against $H_{A}^{\theta}$ under general conditions. From Lemmas 7.1 and 4.1, we also have the equivalence between $H_{0}^{\theta}$ and $H_{0}^{\omega}: \omega_{*}^{2}=0$. This suggests testing the parametric hypothesis $H_{0}^{\theta}$ against $H_{A}^{\theta}$ by testing $H_{0}^{\omega}$ against $H_{A}^{\omega}$. Thus, we have a new test for nested hypotheses based on the variance statistics $\hat{\omega}_{n}^{2}$ and $\tilde{\omega}_{n}^{2}$. Let $\hat{\lambda}_{n}^{2}$ be the squares of the eigenvalues $\hat{\lambda}_{n}$.

Theorem 7.4 (Variance Tests for Nested Models): Given Assumptions A1-A8:
(i) under $H_{0}^{\theta}$, for any $x \geqslant 0, \operatorname{Pr}\left(n \hat{\omega}_{n}^{2} \leqslant x\right)-M_{p}\left(x ; \hat{\hat{\lambda}}_{n}^{2}\right) \xrightarrow{\text { a.s. }} 0$,
(ii) under $H_{A}^{\theta}, n \hat{\omega}_{n}^{2} \xrightarrow{\text { a.s. }}+\infty$,
(iii) properties (i) and (ii) hold for $n \tilde{\omega}_{n}^{2}$.

As for the LR test of Theorem 7.4, variance tests are one-sided. They are carried out by choosing a critical value from $M_{p}\left(\cdot ; \underline{\hat{\lambda}}_{n}^{2}\right)$ and by rejecting the hypothesis that $\theta_{*}$ belongs to $\phi(\Gamma)$ if $n \hat{\omega}_{n}^{2}$ or $n \tilde{\omega}_{n}^{2}$ is larger than this critical value. These statistics $n \hat{\omega}_{n}^{2}$ and $n \tilde{\omega}_{n}^{2}$ are readily computed:

$$
\begin{aligned}
& n \hat{\omega}_{n}^{2}=\sum_{t=1}^{n}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right)}{f\left(Y_{t} \mid Z_{t} ; \tilde{\theta}_{n}\right)}\right]^{2}-\frac{1}{n} L R_{n}^{2}, \\
& n \tilde{\omega}_{n}^{2}=\sum_{t=1}^{n}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right)}{f\left(Y_{t} \mid Z_{t} ; \tilde{\theta}_{n}\right)}\right]^{2} .
\end{aligned}
$$

Thus $n \hat{\omega}_{n}^{2}$ is the sum of squared residuals in a linear regression of

$$
m_{t} \equiv \log \left[f\left(Y_{t} \mid Z_{t} ; \hat{\theta}_{n}\right) / f\left(Y_{t} \mid Z_{t} ; \tilde{\theta}_{n}\right)\right]
$$

on the constant term. The variance tests are not asymptotically equivalent to the LR tests, and require more assumptions than the LR test. In normal linear regressions, these additional assumptions bear on the fourth moments of the residuals. Thus it is expected that the variance statistics would be less stable than the LR statistic. ${ }^{8}$

If the larger model is correctly specified, then the limiting distribution reduces to the central chi-square distribution with $p-q$ degrees of freedom, as other classical statistics.

Corollary 7.5 (Variance Tests for Nested Models Given Information Matrix Equivalence): Given Assumptions A1-A8, suppose that $A_{f}\left(\boldsymbol{\theta}_{\boldsymbol{*}}\right)+B_{f}\left(\boldsymbol{\theta}_{\boldsymbol{*}}\right)=0$ :
(i) under $H_{0}^{\theta}, n \hat{\omega}_{n}^{2} \xrightarrow[a s]{D} \chi_{p-q}^{2}$,
(ii) under $H_{A}^{\theta}, n \hat{\omega}_{n}^{2} \xrightarrow{\text { a.s. }}+\infty$,
(iii) properties (i) and (ii) hold for $n \tilde{\omega}_{n}^{2}$.

[^5]
[^0]:    ${ }^{3}$ There are alternative definitions. For instance, one can use the mean-square error of prediction (see White and Olson (1979)). To take into account the parsimonious nature of a model, one may also adjust the above definitions by a correction factor $k(p, q)$ (see Vuong (1986, Theorem 5.4)). In this latter case, a correctly specified model is no longer necessarily best.

[^1]:    ${ }^{4}$ For, if $f\left(y \mid z ; \theta_{*}\right)=g\left(y \mid z ; \gamma_{*}\right)$ holds for $H_{X}^{0}$-almost all $(y, z)$, then from Assumption A1-(b) this must also hold for $\left(\nu_{Y} \times H_{Z}^{0}\right)$-almost all $(y, z)$. Hence $F_{Y \mid Z}\left(\cdot \mid z ; \theta_{*}\right)=G_{Y \mid Z}\left(\cdot \mid z ; \gamma_{*}\right)$ for $H_{Z}^{0}$-almost all $z$, which implies a contradiction.

[^2]:    ${ }^{5}$ I owe this point to Hal White.

[^3]:    ${ }^{6}$ An alternative to the variance test is to characterize and test the conditions that $\theta_{*}$ and $\gamma_{*}$ must satisfy for $f\left(\cdot \mid \cdot ; \theta_{*}\right)$ to be equal to $g\left(\cdot \mid \cdot ; \gamma_{*}\right)$. See Lien and Vuong (1987) for an illustration. In general, tests of these conditions are easier to perform and can be done using $\hat{\theta}_{n}$ and $\hat{\gamma}_{n}$.

[^4]:    ${ }^{7}$ Johnson and Kotz (1969) give values of $M_{m}(x ; \lambda)$ for $m=4$ and some values of $x$ and $\lambda$ with a Fortran IV program for calculating $M_{m}(x ; \lambda)$. Dubin and Rivers (1986) also have an efficient and flexible subroutine for computing $M_{m}(x ; \lambda)$.

[^5]:    ${ }^{8}$ The variance tests are neither asymptotically equivalent under $H_{0}^{\theta}$ to the robust Wald and LM tests proposed by White (1982a). The asymptotic power properties of the variance tests in the misspecified case are left for future research.



As mentioned earlier, the information matrix equivalence $A_{f}\left(\theta_{*}\right)+B_{f}\left(\theta_{*}\right)=0$ holds if the larger model is correctly specified.

## 8. CONCLUSION

In this paper, we have proposed a new and general approach to model selection whether the competing models are nested, overlapping, or non-nested, and whether the models are correctly specified. The approach has the desirable property that it coincides with the usual classical testing approach when the models are nested. It is probabilistic and is based on testing if the competing models are as close to the true distribution against the hypothesis that one model is closer than the other. Since the maximum log-likelihood of a model is a natural estimator of the distance between the model and the true distribution as measured by the KLIC, all our model selection tests are based on the LR statistic. As a prerequisite, we have fully characterized the asymptotic distribution of the LR statistic under the most general conditions.

Much work remains to be done. First, one could relax Assumption A1-(a) so as to extend our results to time-series models. Second, we have mentioned that our LR-based tests for model selection could be adjusted for the number of parameters. A theoretical and Monte Carlo study would shed some light on the most adequate adjustment to the LR statistic in small samples for some particular cases. Third, a thorough comparison between our model selection tests and the available Cox-type tests as considered by Davidson and McKinnon (1981), Pesaran (1974), and Pesaran and Deaton (1978), among others, would be useful. In the same line, it would be useful to compare our approach to the comprehensive approach advocated by Atkinson (1969, 1970), which requires nesting the competing models in a larger model. Fourth, it would be interesting to compare the performance of our model selection tests to the tests using the encompassing principle as advocated by Hendry (1983), and Mizon and Richard (1986). Fifth, the above model selection tests have been obtained under the assumption that there are only two competing models. It is important to generalize our procedures to the case where there are many competing models.

Department of Economics, University of Southern California, Los Angeles, CA 90089, U.S.A.

Manuscript received March, 1986; revision received January, 1988.


#### Abstract

APPENDIX Except when explicitly mentioned, all the matrices $A_{f}, B_{f}, A_{g}, B_{g}$, and $B_{f g}$ are evaluated at the pseudo-true values $\theta_{*}$ and $\gamma_{*}$. The notation $o_{p}(1)$ indicates a quantity that converges in probability to zero, while the notation $O_{p}(1)$ indicates a quantity that is bounded in probability as $n$ goes to infinity. The following lemma is useful.


Lemma A: Given Assumptions A1-A5:

$$
n^{1 / 2}\left[\begin{array}{l}
\hat{\theta}_{n}-\theta_{*} \\
\hat{\gamma}_{n}-\gamma_{*}
\end{array}\right] \xrightarrow{D} N(0, \Sigma), \quad \text { where } \quad \Sigma=\left[\begin{array}{ll}
A_{f}^{-1} B_{f} A_{f}^{-1} ; & A_{f}^{-1} B_{f g} A_{g}^{-1} \\
A_{g}^{-1} B_{g f} A_{f}^{-1} ; & A_{g}^{-1} B_{g} A_{g}^{-1}
\end{array}\right] .
$$

Moreover, the asymptotic covariance matrix $\Sigma$ can be consistently estimated by $\hat{\Sigma}_{n}$ which is defined as in (A.1) where $A_{s}, B_{s}, B_{f g}, s=f, g$, are replaced by their sample analogs evaluated at the $M L$ estimators $\hat{\theta}_{n}$ and $\hat{\gamma}_{n}$.

Proof of Lemma A: Given Assumptions A1-A5, we obtain using the Taylor expansions of the normal equations:

$$
\begin{aligned}
& 0=n^{-1 / 2} \frac{\partial L_{n}^{f}\left(\theta_{*}\right)}{\partial \theta}+A_{f} \cdot n^{1 / 2}\left(\hat{\theta}_{n}-\theta_{*}\right)+o_{p}(1) \\
& 0=n^{-1 / 2} \frac{\partial L_{n}^{g}\left(\gamma_{*}\right)}{\partial \gamma}+A_{g} \cdot n^{1 / 2}\left(\hat{\gamma}_{n}-\gamma_{*}\right)+o_{p}(1)
\end{aligned}
$$

On the other hand from the multivariate Central Limit Theorem (see, e.g., Rao (1973)):

$$
n^{-1 / 2}\left[\begin{array}{l}
\partial L_{n}^{f}\left(\theta_{*}\right) / \partial \theta \\
\partial L_{n}^{g}\left(\gamma_{*}\right) / \partial \gamma
\end{array}\right] \xrightarrow{D} N\left(0,\left[\begin{array}{c}
B_{f} ; B_{f g} \\
B_{g f} ; B_{g}
\end{array}\right]\right)
$$

The desired result follows since $A_{f}$ and $A_{g}$ are nonsingular (White (1982a, Theorem 3.1)).
Proof of Lemma 3.1: Obvious from, e.g., Vuong (1983, Theorem 1).
Proof of Lemma 3.2: From Moore (1978, Theorem 1), we know that $Y^{\prime} Q Y \sim M_{m}(\cdot ; \lambda)$ where $\lambda$ are the eigenvalues of $\Omega^{1 / 2} Q \Omega^{1 / 2}$ and $\Omega^{1 / 2}$ is the (unique) square root of $\Omega$. Using Theorem 1.3.20 in Horn and Johnson (1985) it follows that the eigenvalues of $\Omega^{1 / 2} Q \Omega^{1 / 2}$ are the eigenvalues of $Q \Omega$.

Proof of Theorem 3.3: From a Taylor expansion of $L_{n}^{f}\left(\theta_{*}\right)$ around $\hat{\theta}_{n}$, we obtain:

$$
L_{n}^{f}\left(\theta_{*}\right)=L_{n}^{f}\left(\hat{\theta}_{n}\right)+\frac{n}{2}\left(\hat{\theta}_{n}-\theta_{*}\right)^{\prime} A_{f}\left(\hat{\theta}_{n}-\theta_{*}\right)+o_{p}(1)
$$

Similarly, we have:

$$
L_{n}^{g}\left(\gamma_{*}\right)=L_{n}^{g}\left(\hat{\gamma}_{n}\right)+\frac{n}{2}\left(\hat{\gamma}_{n}-\gamma_{*}\right)^{\prime} A_{g}\left(\hat{\gamma}_{n}-\gamma_{*}\right)+o_{p}(1) .
$$

Since $L R_{n}\left(\theta_{*}, \gamma_{*}\right)=L_{n}^{f}\left(\theta_{*}\right)-L_{n}^{g}\left(\gamma_{*}\right)$, we obtain:

$$
\begin{aligned}
L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)= & L R_{n}\left(\theta_{*}, \gamma_{*}\right)-\frac{n}{2}\left(\hat{\theta}_{n}-\theta_{*}\right)^{\prime} A_{f}\left(\hat{\theta}_{n}-\theta_{*}\right) \\
& +\frac{n}{2}\left(\hat{\gamma}_{n}-\gamma_{*}\right)^{\prime} A_{g}\left(\hat{\gamma}_{n}-\gamma_{*}\right)+o_{p}(1)
\end{aligned}
$$

To prove (i), we note that $L R_{n}\left(\theta_{*}, \gamma_{*}\right)=0$ if $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$. Part (i) follows from Lemma A and Lemma 3.2 by considering the quadratic form associated with the block-diagonal matrix:

$$
Q=\left[\begin{array}{cc}
-A_{f} & 0 \\
0 & A_{g}
\end{array}\right]
$$

Then, one can check that $Q \Sigma$ is equal to $W$ as given in (3.6). To prove (ii), we note that $n^{1 / 2}\left(\hat{\theta}_{n}-\theta_{*}\right)$ and $n^{1 / 2}\left(\hat{\gamma}_{n}-\gamma_{*}\right)$ are $O_{p}(1)$. Thus, from (A.7) we obtain:

$$
\begin{aligned}
& n^{-1 / 2} L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)-n^{1 / 2} E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right] \\
& \quad=n^{1 / 2}\left[\frac{1}{n} L R_{n}\left(\theta_{*}, \gamma_{*}\right)-E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)}\right]\right]+o_{p}(1)
\end{aligned}
$$

But from the multivariate Central Limit Theorem, the first term in the right-hand side converges in distribution to $N\left(0, \omega_{*}^{2}\right)$ where $\omega_{*}^{2}$ is the variance defined in (3.4). This variance is finite given Assumption A6 and the Cauchy-Schwartz inequality. Part (ii) follows.

Proof of Corollary 3.4: From the proof of Theorem 3.3-(i), $2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)$ is asymptotically distributed as a quadratic form in $n^{1 / 2}\left(\hat{\theta}_{n}^{\prime}-\theta_{*}^{\prime}, \hat{\gamma}_{n}^{\prime}-\gamma_{*}^{\prime}\right)^{\prime}$ which is asymptotically normal $N(0, \Sigma)$ (Lemma A). Thus, from Rao and Mitra (1971, Theorem 9.2.1), $2 L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)$ is asymptotically distributed as a (central) chi-square if and only if $\Sigma Q \Sigma Q \Sigma=\Sigma Q \Sigma$, where $Q$ is given in (A.8), in which case the number of degrees of freedom is $\operatorname{tr} Q \Sigma$. But $\Sigma=A^{-1} B A^{-1}$, where

$$
B=\left[\begin{array}{cc}
B_{f} & B_{f g} \\
B_{g f} & B_{g}
\end{array}\right] ; \quad A=\left[\begin{array}{cc}
A_{f} & 0 \\
0 & A_{g}
\end{array}\right] .
$$

Noticing that $A^{-1} Q A^{-1}=Q^{-1}$, the necessary and sufficient condition $\Sigma Q \Sigma Q \Sigma=\Sigma Q \Sigma$ becomes:

$$
B Q^{-1} B Q^{-1} B=B Q^{-1} B
$$

Using (3.8), we obtain that (A.11) is equivalent to:

$$
\begin{gathered}
{\left[\begin{array}{cc}
B_{f}-B_{f g} B_{g}^{-1} B_{g f} ; & B_{f g} B_{g}^{-1}\left(B_{g}-B_{g f} B_{f}^{-1} B_{f g}\right) \\
\left(B_{g}-B_{g f} B_{f}^{-1} B_{f g}\right) B_{g}^{-1} B_{g f} ; & B_{g}-B_{g f} B_{f}^{-1} B_{f g}
\end{array}\right]} \\
=\left[\begin{array}{cc}
B_{f}-B_{f g} B_{g}^{-1} B_{g f} ; & 0 \\
0 ; & -B_{g}+B_{g f} B_{f}^{-1} B_{f g}
\end{array}\right]
\end{gathered}
$$

which is equivalent to (3.9). Then, the number of degrees of freedom is:

$$
\operatorname{tr} Q \Sigma=\operatorname{tr}\left[\begin{array}{cc}
I_{p} ; & B_{f g} B_{g}^{-1} \\
-B_{g f} B_{f}^{-1} ; & -I_{q}
\end{array}\right]=p-q .
$$

Proof of Lemma 4.1: From (3.4) it follows that $\omega_{*}^{2}=0$ if and only if $f\left(\cdot \mid \cdot ; \theta_{*}\right)=K g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ for some constant $K, H_{X}^{0}$-almost surely. It remains to show that $K=1$. From Assumption A1-(b), it follows that $f\left(y \mid z ; \theta_{*}\right)=K g\left(y \mid z ; \gamma_{*}\right)$ for $\left(\nu_{Y} \times H_{Z}^{0}\right)$-almost all $(y, z)$. Integrating this equality with respect to ( $\nu_{Y} \times H_{Z}^{0}$ ) gives $1=K$.

Proof of Lemma 4.2: Given Assumptions A1-A3, and A6, it follows from the Cauchy-Schwartz inequality and Jennrich's uniform Strong Law of Large Numbers (1969, Theorem 2) that

$$
\frac{1}{n} \sum_{t=1}^{n}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma\right)}\right]^{2} \xrightarrow{\text { a.s. }} E^{0}\left[\log \frac{f\left(Y_{t} \mid Z_{t} ; \theta\right)}{g\left(Y_{t} \mid Z_{t} ; \gamma\right)}\right]^{2}
$$

uniformly in $(\theta, \gamma)$ on $\Theta \times \Gamma$. The result follows from Lemma 3.1 and the strong consistency of $\hat{\theta}_{n}$ and $\hat{\gamma}_{n}$ to $\theta_{*}$ and $\gamma_{*}$.

Proof of Theorem 4.3: Since $\omega_{*}^{2}=0$ is equivalent to $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ (Lemma 4.1), it follows from Theorem 3.3-(i) that $L R_{n}\left(\hat{\theta}_{n}, \hat{\gamma}_{n}\right)=O_{p}(1)$. Thus, from (4.3), the equality in (4.6) follows. Hence, we need only to study the null asymptotic distribution of $n \tilde{\omega}_{n}^{2}$. Using a Taylor expansion around ( $\theta_{*}, \gamma_{*}$ ), we obtain:

$$
\begin{aligned}
\tilde{\omega}_{n}^{2}= & \frac{1}{n} \sum_{t=1}^{n}\left[\log \frac{f_{t}\left(\theta_{*}\right)}{g_{t}\left(\gamma_{*}\right)}\right]^{2}+2\left[\frac{1}{n} \sum_{t=1}^{n}\left[\log \frac{f_{t}\left(\theta_{*}\right)}{g_{t}\left(\gamma_{*}\right)}\right] \frac{\partial \log f_{t}\left(\theta_{*}\right)}{\partial \theta^{\prime}}\right]\left(\hat{\theta}_{n}-\theta_{*}\right) \\
& -2\left[\frac{1}{n} \sum_{t=1}^{n}\left[\log \frac{f_{t}\left(\theta_{*}\right)}{g_{t}\left(\gamma_{*}\right)}\right] \frac{\partial \log g_{t}\left(\gamma_{*}\right)}{\partial \gamma^{\prime}}\right]\left(\hat{\gamma}_{n}-\gamma_{*}\right) \\
& +\left(\hat{\theta}_{n}^{\prime}-\theta_{*}^{\prime}, \hat{\gamma}_{n}^{\prime}-\gamma_{*}^{\prime}\right) \bar{V}_{n}\left(\hat{\theta}_{n}^{\prime}-\theta_{*}^{\prime}, \hat{\gamma}_{n}^{\prime}-\gamma_{*}^{\prime}\right)^{\prime}
\end{aligned}
$$

where we have used $f_{t}\left(\theta_{*}\right)$ and $g_{t}\left(\gamma_{*}\right)$ for $f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)$ and $g\left(Y_{t} \mid Z_{t} ; \gamma_{*}\right)$ respectively, and

$$
\begin{aligned}
& \bar{V}_{n}=\left[\begin{array}{cc}
\bar{V}_{\theta \theta n} ; & \bar{V}_{\theta \gamma n} \\
\bar{V}_{\gamma \theta n} ; & \bar{V}_{\gamma \gamma n}
\end{array}\right] \\
& \bar{V}_{\theta \theta n}=\frac{1}{n} \sum_{t=1}^{n} \frac{\partial \log f_{t}\left(\bar{\theta}_{n}\right)}{\partial \theta} \cdot \frac{\partial \log f_{t}\left(\bar{\theta}_{n}\right)}{\partial \theta^{\prime}}+\frac{1}{n} \sum_{t=1}^{n}\left[\log \frac{f_{t}\left(\bar{\theta}_{n}\right)}{g_{t}\left(\bar{\gamma}_{n}\right)}\right] \frac{\partial^{2} \log f_{t}\left(\bar{\theta}_{n}\right)}{\partial \theta \partial \theta^{\prime}} \\
& \bar{V}_{\theta \gamma n}=\bar{V}_{\gamma^{\prime} \theta n}^{\prime}=-\frac{1}{n} \sum_{t=1}^{n} \frac{\partial \log f_{t}\left(\bar{\theta}_{n}\right)}{\partial \theta} \cdot \frac{\partial \log g_{t}\left(\bar{\gamma}_{n}\right)}{\partial \gamma^{\prime}} \\
& \bar{V}_{\gamma \gamma n}=\frac{1}{n} \sum_{t=1}^{n} \frac{\partial \log g_{t}\left(\bar{\gamma}_{n}\right)}{\partial \gamma} \cdot \frac{\partial \log g_{t}\left(\bar{\gamma}_{n}\right)}{\partial \gamma^{\prime}}-\frac{1}{n} \sum_{t=1}^{n}\left[\log \frac{f_{t}\left(\bar{\theta}_{n}\right)}{g_{t}\left(\bar{\gamma}_{n}\right)}\right] \frac{\partial^{2} \log g_{t}\left(\bar{\gamma}_{n}\right)}{\partial \gamma \partial \gamma^{\prime}}
\end{aligned}
$$

for some $\bar{\theta}_{n}$ and $\bar{\gamma}_{n}$ in the segments $\left[\theta_{*}, \hat{\theta}_{n}\right]$ and $\left[\gamma_{*}, \hat{\gamma}_{n}\right]$ respectively. But, $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ under $H_{0}^{\omega}$ (Lemma 4.1) so that the first three terms in (A.15) are null. Moreover, given Assumptions A1-A7, Jennrich's uniform Strong Law of Large Numbers, the second term in $\bar{V}_{\theta \theta n}$ (or $\bar{V}_{\gamma \gamma n}$ ) goes almost surely to zero since $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ under $H_{0}^{\omega}$. Hence $\bar{V}_{\theta \theta n}=B_{f}+o_{p}(1), \bar{V}_{\gamma \gamma n}=B_{g}+ o_{p}(1), \bar{V}_{\theta \gamma n}=\bar{V}_{\gamma \theta n}^{\prime}=-B_{f g}+o_{p}(1)$. Since $n^{1 / 2}\left(\hat{\theta}_{n}-\theta_{*}\right)$ and $n^{1 / 2}\left(\hat{\gamma}_{n}-\gamma_{*}\right)$ are both $O_{p}(1)$, we obtain from (A.15):

$$
n \tilde{\omega}_{n}^{2}=n\left(\hat{\theta}_{n}^{\prime}-\theta_{*}^{\prime}, \hat{\gamma}_{n}-\gamma_{*}^{\prime}\right) V\left(\hat{\theta}_{n}^{\prime}-\theta_{*}^{\prime}, \hat{\gamma}_{n}^{\prime}-\gamma_{*}^{\prime}\right)+o_{p}(1)
$$

where

$$
V=\left[\begin{array}{cc}
B_{f} & -B_{f g} \\
-B_{g f} & B_{g}
\end{array}\right]
$$

From Lemma A and Lemma 3.2, it remains to show that the eigenvalues of $V \Sigma$ are equal to the squares of the eigenvalues of $W=Q \Sigma$ where $Q$ is defined in (A.8). It is easy to check that $V=Q \Sigma Q$. Thus $V \Sigma=(Q \Sigma)^{2}$. This completes the proof.

Proof of Corollary 4.4: From Lemma A, (A.20), and Rao and Mitra (1971, Theorem 9.2.1), it follows that $n \hat{\omega}_{n}^{2}$ (or $n \tilde{\omega}_{n}^{2}$ ) has a limiting (central) chi-square distribution if and only if $\sum V \Sigma V \Sigma=\Sigma V \Sigma$ in which case the number of degrees of freedom is $\operatorname{tr} V \Sigma$. Using (3.8) we have:

$$
\begin{aligned}
& V \Sigma=\left[\begin{array}{cc}
I_{p}-B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1} ; & 0 \\
0 ; & I_{q}-B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}
\end{array}\right], \\
& \Sigma V \Sigma=\left[\begin{array}{cc}
B_{f}^{-1}\left(I_{p}-B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}\right) ; & B_{f}^{-1} B_{f g} B_{g}^{-1}\left(I_{q}-B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}\right) \\
B_{g}^{-1} B_{g f} B_{f}^{-1}\left(I_{p}-B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}\right) ; & B_{g}^{-1}\left(I_{q}-B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}\right)
\end{array}\right], \\
& \Sigma V \Sigma V \Sigma=\left[\begin{array}{cc}
B_{f}^{-1}\left(I_{p}-B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}\right)^{2} ; & B_{f}^{-1} B_{f g} B_{g}^{-1}\left(I_{q}-B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}\right)^{2} \\
B_{g}^{-1} B_{g f} B_{f}^{-1}\left(I_{p}-B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}\right)^{2} ; & B_{g}^{-1}\left(I_{q}-B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}\right)^{2}
\end{array}\right] .
\end{aligned}
$$

Hence $\sum V \Sigma V \Sigma=\Sigma V \Sigma$ if and only if $I_{p}-B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}$ and $I_{q}-B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}$ are both idempotent, i.e., if and only if $B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}$ and $B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}$ are both idempotent.

But, $B_{f g} B_{g}^{-1} B_{g f} B_{j}^{-1}$ is idempotent if and only if $B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}$ is idempotent. Indeed, $\operatorname{rank}\left(B_{f g} B_{g}^{-1}\right)\left(B_{g f} B_{f}^{-1}\right)=\operatorname{rank} B_{f g} B_{g}^{-1} B_{g f}=\operatorname{rank} B_{f g}=\operatorname{rank} B_{f g} B_{g}^{-1}$. Thus, from Rao and Mitra (1971, Lemma 2.2.7), if $\left(B_{f g} B_{g}^{-1}\right)\left(B_{g f} B_{f}^{-1}\right)$ is idempotent, then $\left(B_{g f} B_{f}^{-1}\right)\left(B_{f g} B_{g}^{-1}\right)$ is also idempotent. By the same argument, if $B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}$ is idempotent, then $B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}$ is also idempotent.

This establishes the equivalences between (i), (ii), (iii), and (iv). Finally, from (A.19):

$$
\begin{aligned}
\operatorname{tr} V \Sigma & =p+q-\operatorname{tr}\left(B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}\right)-\operatorname{tr}\left(B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}\right) \\
& =p+q-2 \operatorname{tr}\left(B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}\right) .
\end{aligned}
$$

Since $B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}$ must be idempotent for $n \hat{\omega}_{n}^{2}$ to be chi-square distributed asymptotically, then $\operatorname{tr}\left(B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}\right)=\operatorname{rank}\left(B_{f g} B_{g}^{-1} B_{g f} B_{f}^{-1}\right)=\operatorname{rank} B_{g f}$. This completes the proof.

Proof of Theorem 5.1: Straightforward from Theorem 3.3-(ii), and Lemma 4.2 since $f\left(\cdot \mid \cdot ; \theta_{*}\right) \neq g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ (footnote 3) and $\omega_{*}^{2}>0$ (Lemma 4.1).

Proof of Theorem 6.1: Since $\hat{W}_{n}$ converges almost surely to $W$ and since the eigenvalues of a matrix are continuous in the elements of the matrix (see, e.g., Horn and Johnson (1985, p. 540)), then the eigenvalues $\hat{\lambda}_{n}$ converge almost surely to $\lambda_{*}$. Part (i) follows from Theorem 4.3, since $M_{p+q}(x ; \lambda)$ is continuous in $\lambda$. Part (ii) follows from Lemma 4.2-(i). Part (iii) is proved similarly.

Proof of Lemma 6.2: We shall prove that (ii) ⇒ (i) $\Rightarrow$ (iii) $\Rightarrow$ (ii). We shall also freely switch between the measures ( $\nu_{Y} \times H_{Z}^{0}$ ) and $H_{X}^{0}$ because they are equivalent by Assumption A1-(b). Without loss of generality, we assume that $H_{Y \mid Z}^{0}(\cdot \mid \cdot) \in \boldsymbol{F}_{\theta}$, which is equivalent to $h^{0}(\cdot \mid \cdot)=f\left(\cdot \mid \cdot ; \theta_{o}\right)$ for some $\theta_{o}$ in $\Theta$. It follows from Assumption A3-(b) and Jensen's inequality that $\theta_{*}=\theta_{o}$. Thus $h^{0}(\cdot \mid \cdot)=f\left(\cdot \mid \cdot ; \theta_{*}\right)$.
(ii) ⇒ (i): Since $h^{0}(\cdot \mid \cdot)=f\left(\cdot \mid \cdot ; \theta_{*}\right)$, then $h^{0}(\cdot \mid \cdot)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$, so that $H_{Y \mid Z}^{0}(\cdot \mid \cdot) \in \boldsymbol{G}_{\gamma}$.
(i) ⇒ (iii): Since $H_{Y \mid Z}^{0}(\cdot \mid \cdot) \in \boldsymbol{G}_{\gamma}$, then $h^{0}(\cdot \mid \cdot)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ as above. Since $h^{0}(\cdot \mid \cdot)=f\left(\cdot \mid \cdot ; \theta_{*}\right)$, then $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ for $H_{X}^{0}$-almost all $(y, z)$, which implies (iii).
(iii) ⇒ (ii): Since $h^{0}(\cdot \mid \cdot)=f\left(\cdot \mid \cdot ; \theta_{*}\right)$ for ( $\nu_{Y} \times H_{Z}^{0}$ ) almost all ( $y, z$ ), (iii) implies:

$$
\int_{Z}\left\{\int_{Y} \log \frac{f\left(y \mid z ; \theta_{*}\right)}{g\left(y \mid z ; \gamma_{*}\right)} f\left(y \mid z ; \theta_{*}\right) \nu_{Y}(d y)\right\} H_{Z}^{0}(d z)=0 .
$$

Then (ii) follows from Jensen's inequality and $H_{X}^{0}=F_{Y \mid Z}\left(\cdot \mid \cdot ; \theta_{*}\right) H_{Z}^{0}(\cdot)$.
Proof of Theorem 6.3: Under $H_{0}$, it follows from Lemma 6.2 that $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$. Then, Part (i) follows from Theorem 3.3-(i), the continuity of $M_{p+q}(x ; \lambda)$ in $\lambda$, and the strong convergence of $\hat{\lambda}_{n}$ to the eigenvalues $\lambda_{*}$ of $W$. Parts (ii) and (iii) follow from Lemma 3.1.

Proof of Lemma 7.1: We shall prove that (ii) ⇒ (i) $\Rightarrow$ (iv) $\Rightarrow$ (iii) $\Rightarrow$ (ii).
(ii) ⇒ (i): Since $\theta_{*} \in \phi(\Gamma), \exists \tilde{\gamma} \in \Gamma$ such that $\theta_{*}=\phi(\tilde{\gamma})$. Thus, from Assumptions A1-(b) and A8, $g(\cdot \mid \cdot ; \tilde{\gamma})=f\left(\cdot \mid \cdot ; \theta_{*}\right)$ for $H_{X}^{0}$-almost all $(y, z)$, which implies $E^{0}\left[\log g\left(Y_{t} \mid Z_{t} ; \tilde{\gamma}\right)\right] \geqslant E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \theta\right)\right]$ for any $\theta$ in $\Theta$ and, in particular for any $\theta=\phi(\gamma)$ for $\gamma \in \Gamma$. Using again Assumption A8, we have $E^{0}\left[\log g\left(Y_{t} \mid Z_{t} ; \tilde{\gamma}\right)\right] \geqslant E^{0}\left[\log g\left(Y_{t} \mid Z_{t} ; \gamma\right)\right]$ for any $\gamma \in \Gamma$, which implies that $\tilde{\gamma}=\gamma_{*}$ from Assumption A3-(b), and hence that $\theta_{*}=\phi\left(\gamma_{*}\right)$.
(i) ⇒ (iv): Obvious given Assumptions A1-(b) and A8.
(iv) ⇒ (iii): Obvious.
(iii) ⇒ (ii): Suppose that $\theta_{*} \notin \phi(\Gamma)$; then $\theta_{*} \neq \tilde{\theta} \equiv \phi\left(\gamma_{*}\right)$. From (iii), Assumptions A1-(b) and A8, we have $E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right)\right]=E^{0}\left[\log f\left(Y_{t} \mid Z_{t} ; \tilde{\theta}\right)\right]$, which contradicts the uniqueness of $\theta_{*}$.

Lemma B: Given Assumptions A1-(b), A2-A5 and A8, we have under $H_{0}^{\theta}$ :

$$
B_{g}\left(\gamma_{*}\right)=\frac{\partial \phi^{\prime}\left(\gamma_{*}\right)}{\partial \gamma} B_{f}\left(\theta_{*}\right) \frac{\partial \phi\left(\gamma_{*}\right)}{\partial \gamma^{\prime}} ; \quad A_{g}\left(\gamma_{*}\right)=\frac{\partial \phi^{\prime}\left(\gamma_{*}\right)}{\partial \gamma} A_{f}\left(\theta_{*}\right) \frac{\partial \phi\left(\gamma_{*}\right)}{\partial \gamma^{\prime}},
$$

(ii)

$$
B_{g f}\left(\gamma_{*}, \theta_{*}\right)=\frac{\partial \phi^{\prime}\left(\gamma_{*}\right)}{\partial \gamma} B_{f}\left(\theta_{*}\right),
$$

(iii)

$$
q \leqslant p, \quad \operatorname{rank} \frac{\partial \phi^{\prime}\left(\gamma_{*}\right)}{\partial \gamma}=q .
$$

Proof of Lemma B: Under Assumptions A1-(b) and A8, $\partial \log g(\cdot \mid \cdot ; \gamma) / \partial \gamma=\partial \phi^{\prime} / \partial \gamma$. $\partial \log f(\cdot \mid \cdot ; \phi(\gamma)) / \partial \theta H_{X}^{0}$-almost surely. But under $H_{0}^{\theta}$, we have $\theta_{*}=\phi\left(\gamma_{*}\right)$ (Lemma 7.1), which establishes (ii) and the first equality of (i) using the definitions of $B_{g}, B_{f}$, and $B_{g f}$. In addition:

$$
\frac{\partial^{2} \log g}{\partial \gamma \partial \gamma^{\prime}}=\frac{\partial \phi^{\prime}}{\partial \gamma} \cdot \frac{\partial^{2} \log f}{\partial \theta \partial \theta^{\prime}} \cdot \frac{\partial \phi}{\partial \gamma^{\prime}}+\sum_{k} \frac{\partial \phi_{k}}{\partial \gamma \partial \gamma^{\prime}} \frac{\partial \log f}{\partial \theta_{k}},
$$

$H_{X}^{0}$-almost surely, where we have omitted the arguments of the functions, and where $\phi_{k}$ is the $k$ th component of $\phi$. Since $E^{0}\left[\partial \log f\left(Y_{t} \mid Z_{t} ; \theta_{*}\right) / \partial \theta\right]=0$ and since $\theta_{*}=\phi\left(\gamma_{*}\right)$, the second equality of (i) follows. Finally, (iii) follows from this equality and the fact that $A_{f}\left(\theta_{*}\right)$ and $A_{g}\left(\gamma_{*}\right)$ are nonsingular matrices (see, White (1982a), Theorem 3.1)).

Proof of Theorem 7.2: Since under $H_{0}^{\theta}$, we have $f\left(\cdot \mid \cdot ; \theta_{*}\right)=g\left(\cdot \mid \cdot ; \gamma_{*}\right)$ (Lemma 7.1), then (i) follows from (7.3) and Theorem 3.3-(i) if we show that the nonzero eigenvalues $\lambda_{*}$ of $W$ are the nonzero eigenvalues of $W$. But, using Lemma B, the eigenvalues of $W$ solve:

$$
\begin{aligned}
0 & =\operatorname{det}\left[\begin{array}{cc}
-B_{f} A_{f}^{-1}-\lambda I_{p} ; & -B_{f} \frac{\partial \phi}{\partial \gamma^{\prime}} A_{g}^{-1} \\
\frac{\partial \phi^{\prime}}{\partial \gamma} B_{f} A_{f}^{-1} ; & \frac{\partial \phi^{\prime}}{\partial \gamma} B_{f} \frac{\partial \phi}{\partial \gamma^{\prime}} A_{g}^{-1}-\lambda I_{q}
\end{array}\right] \\
& =\operatorname{det}\left[\begin{array}{cc}
-B_{f} A_{f}^{-1}-\lambda I_{p} ; & -B_{f} \frac{\partial \phi}{\partial \gamma^{\prime}} A_{g}^{-1} \\
-\lambda \frac{\partial \phi^{\prime}}{\partial \gamma} ; & -\lambda I_{q}
\end{array}\right] \\
& =\operatorname{det}\left[\begin{array}{cc}
-B_{f} A_{f}^{-1}-\lambda I_{p}+B_{f} \frac{\partial \phi}{\partial \gamma^{\prime}} A_{g}^{-1} \frac{\partial \phi^{\prime}}{\partial \gamma} ; & -B_{f} \frac{\partial \phi}{\partial \gamma^{\prime}} A_{g}^{-1} \\
0 ; & -\lambda I_{q}
\end{array}\right],
\end{aligned}
$$

where the second equation follows from the first equation by adding to the second-row matrices the first-row matrices premultiplied by the full row-rank matrix $\partial \phi^{\prime} / \partial \gamma$ (Lemma B-(iii)), and where the third equation follows from the second equation by adding to the first-column matrices the second-column matrices postmultiplied by $-\partial \phi^{\prime} / \partial \gamma$. Hence, the eigenvalues of $W$ solve:

$$
0=\lambda^{q} \operatorname{det}\left\{-B_{f} A_{f}^{-1}+B_{f} \frac{\partial \phi}{\partial \gamma^{\prime}} A_{g}^{-1} \frac{\partial \phi^{\prime}}{\partial \gamma}-\lambda I_{p}\right\},
$$

which establishes that the nonzero eigenvalues of $W$ are the nonzero eigenvalues of $\underline{W}$ as defined by (7.4). Equation (A.23) also shows that the eigenvalues of $\underline{W}$ are all real and nonnegative since $A_{f}^{-1}-\left[\partial \phi / \partial \gamma^{\prime}\right] A_{g}^{-1}\left[\partial \phi^{\prime} / \partial \gamma\right]=A_{f}^{-1}-\left[\partial \phi / \partial \gamma^{\prime}\right]\left(\left[\partial \phi^{\prime} / \partial \gamma\right] A_{f}\left[\partial \phi / \partial \gamma^{\prime}\right]\right)^{-1}\left[\partial \phi^{\prime} / \partial \gamma\right]$ which is n.s.d. Part (ii) follows from Lemma 3.1 and $H_{A}^{\theta}=H_{f}$.

Proof of Corollary 7.3: If $A_{f}+B_{f}=0$, then it follows from Lemma B-(i) that under $H_{0}^{\theta}$, $A_{g}+B_{g}=0$. Part (i) follows from Corollary 3.4. Part (ii) is identical to Theorem 7.2-(ii).

Proof of Theorem 7.4: Since $H_{0}^{\theta}=H_{0}^{\omega}$, (i) follows from Theorem 4.3 since the nonzero eigenvalues of $W$ are the eigenvalues of $\underline{W}$. Part (ii) follows from Lemma 4.2 since $H_{A}^{\theta}$ is equivalent to $H_{A}^{\omega}$. Part (iii) is proved similarly.

Proof of Corollary 7.5: As noticed in the proof of Corollary 7.3, both information matrix equivalences hold under $H_{0}^{\theta}$. Then (i) follows from Corollary 4.4-(iv) since $B_{g f} B_{f}^{-1} B_{f g} B_{g}^{-1}$ is equal to $I_{q}$ (using Lemma B). Parts (ii) and (iii) are identical to Theorem 7.4-(ii) and (iii).

## REFERENCES

Aguirre-Torres, V., and A. R. Gallant (1983): "The Null and Non-Null Asymptotic Distribution of the Cox Test for Multivariate Nonlinear Regression: Alternatives and a New Distribution-Free Cox Test," Journal of Econometrics, 21, 5-33.
Akaike, H. (1973): "Information Theory and an Extension of the Likelihood Ratio Principle," Proceedings of the Second International Symposium of Information Theory, ed. by B. N. Petrov and F. Csaki. Budapest: Akademiai Kiado, 257-281.
(1974): "A New Look at the Statistical Model Identification," IEEE Transactions on Automatic Control, AC-19, 716-723.
Amemiya, T. (1980): "Selection of Regressors," International Economic Review, 21, 331-354.
Atkinson, A. C. (1969): "A Test for Discriminating between Models," Biometrika, 56, 337-347.

- (1970): "A Method for Discriminating between Models," Journal of the Royal Statistical Society, Series B, 32, 323-353.
Bauer, H. (1972): Probability Theory and Elements of Measure Theory. New York: Holt, Rinehart, and Winston.
Burguette, J., A. R. Gallant, and G. Souza (1982): "On the Unification of the Asymptotic Theory of Nonlinear Econometric Models," Econometric Reviews, 1, 151-190.
Chow, G. (1980): "The Selection of Variables for Use in Prediction: A Generalization of Hotelling's Solution," Quantitative Econometrics and Development, ed. by L. N. Klein, M. Nerlove, and S. C. Tiang. New York: Academic Press.
- (1981): "Selection of Econometric Models by the Information Criterion," Proceedings of the Econometric Society European Meeting, ed. E. G. Charatsis. Amsterdam: North Holland.
_ (1983): Econometrics. New York: McGraw-Hill, 1983.
Cox, D. R. (1961): "Tests of Separate Families of Hypotheses," Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability, 1, 105-123.
- (1962): "Further Results on Tests of Separate Families of Hypotheses," Journal of the Royal Statistical Society, Series B, 24, 406-424.
Davidson, R., and J. G. MacKinnon (1981): "Several Tests for Model Specification in the Presence of Alternative Hypotheses," Econometrica, 49, 781-793.
Dubin, J., and D. Rivers (1986): Statistical Software Tools. Pasadena: California Institute of Technology.
Foutz, R. V., and R. C. Srivastava (1977): "The Performance of the Likelihood Ratio Test When the Model is Incorrect," Annals of Statistics, 5, 1183-1194.
Gourieroux, C., A. Monfort, and A. Trognon (1983): "Testing Nested or Non-Nested Hypotheses," Journal of Econometrics, 21, 83-115.
- (1984): "Pseudo Maximum Likelihood Method: Theory," Econometrica, 52, 681-700.

Hendry, D. F. (1983): "Comment," Econometric Reviews, 2, 111-114.
Horn, R. G., and C. A. Johnson (1985): Matrix Analysis. Cambridge: Cambridge University Press.
Hotelling, H. (1940): "The Selection of Variables for Use in Prediction with Some Comments on the Problem of Nuisance Parameters," Annals of Mathematical Statistics, 11, 271-283.
Jennrich, R. I. (1969): "Asymptotic Properties of Non-Linear Least Squares Estimators," Annals of Mathematical Statistics, 40, 633-643.
Johnson, N. L., and S. Kotz (1969): "Tables of Distributions of Positive Definite Quadratic Forms in Central Normal Variables," Sankhya, Series B, 303-314.

- (1970): Continuous Univariate Distributions-2. New York: John Wiley and Sons.

Judge, G. G., W. E. Griffiths, R. C. Hill, H. Lutkepohl, and T. C. Lee (1985): The Theory and Practice of Econometrics. New York: John Wiley and Sons, Second edition.
Kent, J. T. (1982): "Robust Properties of Likelihood Ratio Tests," Biometrika, 69, 19-27.
Kullback, S., and R. A. Leibler (1951): "On Information and Sufficiency," Annals of Mathematical Statistics, 22, 79-86.
Lien, D., and Q. H. Vuong (1987): "Selecting the Best Linear Regression Model: A Classical Approach," Journal of Econometrics, Annals, 35, 3-23.
MacKinnon, J. G. (1983): "Model Specification Tests against Non-Nested Alternatives," Econometric Reviews, 2, 85-110.
McAleer, M., and A. Bera (1983): "Comment," Econometric Reviews, 2, 121-130.
Mizon, G., and J. F. Richard (1986): "The Encompassing Principle and its Application to Non-Nested Hypotheses," Econometrica, 54, 657-678.
Monfort, A. (1980): Cours de Probabilites. Paris: Economica.

Moore, D. S. (1978): "Chi-Square Tests," in Studies in Statistics, ed. by R. V. Hogg. Volume 19, The Mathematical Association of America.
Neyman, J., and E. S. Pearson (1928): "On the Use and Interpretation of Certain Test Criteria for Purposes of Statistical Inference," Biometrika, 20A, 175-240.
Pesaran, M. H. (1974): "On the General Problem of Model Selection," Review of Economic Studies," 41, 153-171.

- (1987): "Global and Partial Non-Nested Hypotheses and Asymptotic Local Power," Econometric Theory, 3, 69-97.
Pesaran, M. H., and A. S. Deaton (1978): "Testing Non-Nested Nonlinear Regression Models," Econometrica, 46, 677-694.
Rao, C. R. (1973): Linear Statistical Inference and its Applications. New York: John Wiley and Sons.
Rao, C. R., and S. K. Mitra (1971): Generalized Inverse of Matrices and its Applications. New York: John Wiley and Sons.
Sawa, T. (1978): "Information Criteria for Discriminating among Alternative Regression Models," Econometrica, 46, 1273-1291.
Schwarz, G. (1978): "Estimating the Dimension of a Model," Annals of Statistics, 6, 461-464.
Vuong, Q. H. (1983): "Misspecification and Conditional Maximum Likelihood Estimation," Social Science Working Paper, No. 503. Pasadena: California Institute of Technology.
- (1986): "Likelihood Ratio Tests for Model Selection and Non-Nested Hypotheses," Social Science Working Paper, No. 605. Pasadena: California Institute of Technology.
Wald, A. (1943): "Tests of Statistical Hypotheses Concerning Several Parameters when the Number of Observations is Large," Transaction of the American Mathematical Society, 54, 426-482.
White, H. (1982): "Maximum Likelihood Estimation of Misspecified Models," Econometrica, 50, 1-25.
- (1982): "Regularity Conditions for Cox's Test of Non-Nested Hypotheses," Journal of Econometrics, 19, 301-318.
- (1983): "Editor's Introduction," Journal of Econometrics, 21, 1-3.

White, H., and I. Domowitz (1984): "Non-linear Regression with Dependent Observations," Econometrica, 52, 143-161.
White, H., and L. Olson (1979): "Determinants of Wage Change on the Job: A Symmetric Test of Non-Nested Hypotheses," mimeo, University of Rochester.
Wilks, S. S. (1938): "The Large Sample Distribution of the Likelihood Ratio for Testing Composite Hypotheses," Annals of Mathematical Statistics, 9, 60-62.

