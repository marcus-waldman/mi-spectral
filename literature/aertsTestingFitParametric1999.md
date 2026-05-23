---
citekey: aertsTestingFitParametric1999
item_type: article
authors: 'Aerts, Marc and Claeskens, Gerda and Hart, Jeffrey D.'
year: 1999
title: 'Testing the {Fit} of a {Parametric Function}'
venue: Journal of the American Statistical Association
volume: 94
issue: 447
pages: 869--879
doi: 10.1080/01621459.1999.10474192
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\aerts_testing_fit_parametric_1999.pdf'
pdf_sha256: 49a3ca2fc00cff51b3960451f15b7c11e5aef8b4909c3fa3be42658d0904551b
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-23T01:22:37Z
---
# Testing the Fit of a Parametric Function 

Marc Aerts, Gerda Claeskens \& Jeffrey D. Hart

To cite this article: Marc Aerts, Gerda Claeskens \& Jeffrey D. Hart (1999) Testing the Fit of a Parametric Function, Journal of the American Statistical Association, 94:447, 869-879, DOI: 10.1080/01621459.1999.10474192

To link to this article: https://doi.org/10.1080/01621459.1999.10474192

Published online: 17 Feb 2012.

Submit your article to this journal

Article views: 212

View related articles

Citing articles: 3 View citing articles

# Testing the Fit of a Parametric Function 

Marc Aerts, Gerda Claeskens, and Jeffrey D. Hart


#### Abstract

General methods for testing the fit of a parametric function are proposed. The idea underlying each method is to "accept" the prescribed parametric model if and only if it is chosen by a model selection criterion. Several different selection criteria are considered, including one based on a modified version of the Akaike information criterion and others based on various score statistics. The tests have a connection with nonparametric smoothing because they use orthogonal series estimators to detect departures from a parametric model. An important aspect of the tests is that they can be applied in a wide variety of settings, including generalized linear models, spectral analysis, the goodness-of-fit problem, and longitudinal data analysis. Implementation using standard statistical software is straightforward. Asymptotic distribution theory for several test statistics is described, and the tests are shown to be consistent against essentially any alternative hypothesis. Simulations and a data example illustrate the usefulness of the tests.


KEY WORDS: Akaike information criterion; Likelihood; Misspecification; Nonparametric series regression; Robust score statistics; Score statistics.

## 1. INTRODUCTION

A fundamental problem in statistics is testing the hypothesis that a function has a prescribed parametric form. This problem arises in a number of different contexts, including regression, spectral analysis, and testing the goodness of fit of a probability distribution. The existing methods for testing such hypotheses fall mainly into two categories: (a) parametric methods designed to detect specific types of departures from the prescribed model, and (b) omnibus nonparametric methods. Tests of the latter type are appealing in that they are consistent against virtually any departure from the hypothesized parametric model. In this article we propose an omnibus method of testing function fit that is generally applicable and easy to implement. In contrast to some other methods, ours does not require specification of a smoothing parameter.

We now introduce the Wisconsin diabetes study (Klein, Klein, Moss, Davis, and DeMets 1984) as an example to motivate the use of lack-of-fit tests in a multiparameter setting. The data considered comprise records from 720 younger-onset diabetic persons. Both eyes of each person were examined for the presence of macular edema. In 29 of the 720 subjects, macular edema was present in only one eye, in 17, it was observed in both eyes; and in the remaining 674, it was completely absent. It is of interest to study the probability of macular edema as a function of systolic blood pressure. In doing so, the clustered nature of the data should be taken into account, because the responses for a person's two eyes are likely to be correlated. A graphical representation of these data can easily yield some idea of

[^0]how the proportion of eyes with macular edema varies with systolic blood pressure (Fig. 1).

Such a graph does not give any information about the correlation between the outcomes of the two eyes, however. Usually, this correlation is assumed to be some constant, which can be estimated from the data. We apply an omnibus lack-of-fit test to investigate the validity of this assumption for these data.

The first two tests that we propose are applicable when the joint density of the data is known up to the function of interest and a finite number of nuisance parameters. The first method makes use of a modified version of the Akaike information criterion (AIC; Akaike 1974) for selecting the dimension of a statistical model. Our second proposed test is a score-statistic analog of the likelihood-based AIC test. In general, the validity of both of these proposed tests depends on correct specification of the likelihood function. To address this problem, we propose a robust version of the score-based test whose asymptotic significance level is correct even when the likelihood is misspecified.

Eubank and Hart (1992) proposed the so-called "order selection" test for checking the fit of a linear model in fixed-design regression. In their test, the difference between the hypothesized linear function and the true regression is expressed as an orthogonal series. This difference can be estimated by an orthogonal series with a finite number of terms, with 0 terms corresponding to the hypothesized linear model. The order selection test proceeds by using a modified Mallows' criterion (1973) to choose the number of terms in the orthogonal series estimate, and rejecting the null hypothesis if and only if the number of terms selected is larger than 0 . The tests that we propose here are analogous to the order selection test of Eubank and Hart (1992) but are applicable to a much wider range of statistical problems. One important area of application is in generalized linear models, where our ideas can be used to check the fit of a linear model for a given link function. Several other applications illustrating the generality of the procedure are

[^1]![](https://cdn.mathpix.com/cropped/5e93efba-443f-49dd-ba57-7002b9959009-03.jpg?height=519&width=886&top_left_y=202&top_left_x=166)
Systolic blood pressure

Figure 1. The Wisconsin Diabetes Data. y values have been jittered.
given as examples in Sections 2 and 3 and in the simulation study in Section 4.

In recent years there has been considerable interest in using smoothing ideas to construct lack-of-fit tests (Hart 1997). Inasmuch as orthogonal series estimators are smoothers, the tests that we propose here may also be regarded as "smoothing based." The existing tests that make use of smoothers are mostly in the regression context and based on squared error discrepancy measures; a number of references to such tests have been given by Eubank, Hart, and LaRiccia (1993) and Hart (1997). In contrast, our tests may be applied in a much wider context than regression and use information divergence (i.e., likelihood) to measure discrepancy between the true and fitted models. Staniswalis and Severini (1991) and Staniswalis, Severini, and Moschopoulos (1993) likewise used likelihood-based diagnostics to assess the fit of regression models.

The rest of the article proceeds as follows. Section 2 describes and analyzes tests that assume a correct specification of the likelihood function. Section 3 proposes tests that retain their validity even when the likelihood is misspecified. Section 4 is devoted to a simulation study, Section 5 to a data example, and Section 6 to conclusions and further research.

## 2. TESTS IN FULL LIKELIHOOD MODELS

In this section we introduce three tests for checking the fit of a parametric function. We begin by laying down some groundwork in Section 2.1. In Sections 2.2 and 2.3 we describe two versions of an AIC-based test that are equivalent and yet have different interpretations. In Sections 2.4 and 2.5 we provide some aymptotic distribution theory for the AIC-based test. Finally, in Section 2.5 we introduce a scorebased test of function fit.

### 2.1 Preliminaries

We suppose that the observed data $\left(\mathbf{Z}_{1}, \ldots, \mathbf{Z}_{n}\right)$ have a joint density of the form $f_{n}\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{n} ; \gamma(\cdot), \boldsymbol{\eta}\right)$, where $f_{n}$ is known up to $\gamma(\cdot)$, the function of interest, and $\boldsymbol{\eta}$, a $k$-dimensional vector of nuisance parameters $(k<\infty)$.

It follows that the log-likelihood function has the form $L(\gamma(\cdot), \boldsymbol{\eta})=\log \left(f_{n}\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{n} ; \gamma(\cdot), \boldsymbol{\eta}\right)\right)$. Our interest is in testing the null hypothesis

$$
H_{0}: \gamma(\cdot) \in \mathcal{G},
$$

where $\mathcal{G}=\left\{\gamma(\cdot ; \boldsymbol{\theta}): \boldsymbol{\theta}=\left(\theta_{1}, \ldots, \theta_{p}\right) \in \Theta\right\}$ and $\Theta$ is a subset of a $p$-dimensional Euclidean space. As alternative models for $\gamma(\cdot)$ we consider sequences of approximators $\left\{\gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+j}\right): j=1,2, \ldots\right\}$, which are assumed to satisfy the following properties:

C0a: For all possible vectors ( $\theta_{1}, \ldots, \theta_{p+j}$ ) and each $j= 0,1, \ldots, \gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+j}\right) \equiv \gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+j}, 0\right)$.
C0b: There exist approximators $\gamma\left(\cdot ; \theta_{1}^{r}, \ldots, \theta_{p+r}^{r}\right), r= 1,2, \ldots$, that converge (in some appropriate sense) to $\gamma(\cdot)$ as $r \rightarrow \infty$.

Condition C 0 a implies that the parametric family $\mathcal{G}$ is nested within the alternative models, which in turn form a sequence of nested models having more and more parameters. The second condition is the first step to ensuring that $\gamma(\cdot)$ may be consistently estimated whether or not it is a member of $\mathcal{G}$. Because we are not primarily interested in function estimation, C 0 b is not necessary for our subsequent results and is included only to suggest a schema by which alternative models may be constructed. (Refer to Efromovich 1996 for more on estimating functions in a quite general setting.)

As just described, the approximators to the underlying function $\gamma(\cdot)$ could be quite general, but we now give a concrete example. Define for $r=1,2, \ldots$, and all $t$ in the domain of $\gamma(\cdot)$,

$$
\gamma\left(t ; \theta_{1}, \ldots, \theta_{p+r}\right)=\gamma\left(t ; \theta_{1}, \ldots, \theta_{p}\right)+\sum_{j=1}^{r} \theta_{p+j} u_{j}(t)
$$

where $u_{1}, u_{2}, \ldots$, are known functions that span some "large" space of functions. If $t$ is real-valued, then possibilities for the $u_{j}$ 's are

- polynomials: $u_{j}(t)=t^{j}, j=1,2, \ldots$
- trigonometric functions: $u_{j}(t)=\cos (A j t), j= 1,2, \ldots$
- linear combinations of polynomials and/or trigonometric functions that are orthogonal in some sense.

It is implicit here that the functions in $\{\gamma(\cdot): \gamma \in \mathcal{G}\}$ are not of the form $\sum_{j=1}^{p} b_{j} u_{i_{j}}(t)$. If this were the case, then we could simply discard $u_{i_{1}}, \ldots, u_{i_{p}}$ from $\sum_{j=1}^{r} \theta_{p+j} u_{j}(t)$. For example, suppose that we wish to test the hypothesis that $\gamma(t)$ has the form $\theta_{1}+\theta_{2} t$ and we want to use polynomial alternatives. Then we could take $u_{j}(t)=t^{j+1}, j=1,2, \ldots$, because there is no point in including 1 or $t$ in our set of alternative models.

### 2.2 An Akaike Information Criterion-Based Test

The basic idea of our tests is to use a data-driven method of selecting a model for $\gamma(\cdot)$, and to reject the null hypothesis (1) if the selected model contains more than $p$ parameters, with $p$ the number of parameters in $H_{0}$. In a likelihood
context, a popular method of model selection is the AIC. Given an approximator $\gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+r}\right)$ of $\gamma(\cdot)$, our $\log$ likelihood is

$$
\begin{aligned}
L_{r}\left(\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}\right) & =\log f_{n}\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{n} ;\right. \\
& \left.\gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+r}\right), \boldsymbol{\eta}\right), \quad r=0,1, \ldots
\end{aligned}
$$

Suppressing the dependence on $k$ and $p$, we write $\mathcal{L}_{r}= \sup _{\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}} L_{r}\left(\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}\right),(r=0,1, \ldots)$. The AIC function is the penalized likelihood $\operatorname{AIC}(r)=\mathcal{L}_{r}-(k+ p+r), r=0,1, \ldots$, in which $r$ is the number of parameters in $\gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+r}\right)$ corresponding to the alternative hypothesis. An estimate of $\gamma(\cdot)$ may be obtained by choosing $r$ to maximize AIC( $r$ ) over some set of the form $\left\{0,1, \ldots, R_{n}\right\}$, where $R_{n}$ could be either fixed or tending to infinity with $n$. For future reference, we note that the maximizer of AIC( $r$ ) is equal to the maximizer of $2\left(\mathcal{L}_{r}-\right. \left.\mathcal{L}_{0}\right)-2 r$.

A possible test of $H_{0}$ against a general alternative is to reject $H_{0}$ if the maximizer, $\hat{r}$, of $\operatorname{AIC}(r)$ is larger than 0 . Under certain regularity conditions (given in Theorem 1 in Sec. 2.4), the limiting level of this test (as $n \rightarrow \infty$ ) is about .29. By most standards, a type I error probability of . 29 is quite high. To obtain control of the test level, we thus propose a modification of AIC that parallels a proposal of Eubank and Hart (1992). Define the modified AIC by

$$
\operatorname{MAIC}\left(r ; C_{n}\right)=2\left(\mathcal{L}_{r}-\mathcal{L}_{0}\right)-C_{n} r, \quad r=0,1, \ldots,
$$

where $C_{n}$ is some constant larger than 1 , and let $\hat{r}_{C_{n}}$ be the maximizer of MAIC $\left(r ; C_{n}\right)$. By appropriate choice of $C_{n}$, the asymptotic type I error probability of the test

$$
\text { reject } H_{0} \text { when } \hat{r}_{C_{n}}>0
$$

can be any number between 0 and 1 . For example, a test of asymptotic level .05 is obtained by using $C_{n}=4.18$. (See Hart 1997, p. 178, for values of $C_{n}$ leading to other test levels.)

### 2.3 An Equivalent Version of the Test

The test just described rejects $H_{0}$ if and only if MAIC $\left(r ; C_{n}\right)$ is larger than 0 for some $r$ in $\left\{1, \ldots, R_{n}\right\}$, which is equivalent to rejecting $H_{0}$ when $T_{n} \geq C_{n}$, with $T_{n}=\max _{1 \leq r \leq R_{n}}\left\{2\left(\mathcal{L}_{r}-\mathcal{L}_{0}\right) / r\right\}$. Hence, in addition to playing the role of penalty constant, $C_{n}$ is a critical value of the statistic $T_{n}$. Using this version of the test, one may approximate the $p$ value corresponding to an observed $T_{n}$ by using either a large-sample distribution or the bootstrap.

The test based on $T_{n}$ has a nice interpretation in terms of likelihood ratio statistics. Notice that $\mathcal{L}_{r}-\mathcal{L}_{0}$ is the log of the likelihood ratio used to test hypothesis (1) against the alternative that $\gamma(\cdot)$ has the form $\gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+r}\right)$. Because our test of $H_{0}$ is omnibus, $T_{n}$ is not a single likelihood ratio but rather the largest of a set of weighted log-likelihood ratio statistics. The largest weights are placed on the models with the fewest parameters. This has an effect similar to
using a prior distribution that places higher probability on alternatives with fewer parameters.

It is worth noting that $T_{n}$ 's limit distribution can be guessed from the fact that $T_{n}$ depends on the data only through $D_{r}=2\left(\mathcal{L}_{r}-\mathcal{L}_{r-1}\right), r=1, \ldots, R_{n}$. Under $H_{0}$ (and the regularity conditions in Theorem 1), the statistics $D_{1}, D_{2}, \ldots$ are asymptotically distributed as independent and identically distributed $\chi_{1}^{2}$ random variables.

### 2.4 Asymptotic Distribution Theory

The data-driven smoothing parameter $\hat{r}_{C_{n}}$ represents the number of basis elements added to the null model parameters. Because we want to use $\hat{r}_{C_{n}}$ as the test statistic, we are interested in its distribution. It turns out that under $H_{0}$, $\hat{r}_{C_{n}}$ has a generalized arc-sine distribution, as described by Woodroofe (1982). Our Theorem 1 is for the most part a consequence of Woodroofe's results. The key distinction between our setting and Woodroofe's is in how these results are applied. We are interested in tests for model fit using series estimators, whereas Woodroofe sought to characterize the number of superfluous parameters chosen by AIC. A novel aspect of Theorem 1 is the penalty constant $C_{n}$ that appears in the definition of the likelihood-based information criterion (MAIC). This constant plays the role of critical value and can be made sample size dependent. Woodroofe's results are based on the traditional AIC, in which $C_{n}=2$ for all $n$.

We need essentially the same assumptions as used by Woodroofe (1982). Let $0_{r}$ be a vector of $r 0$ 's, and let ( $\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}$ ) denote the true parameter under $H_{0}$ and $\mathcal{B}_{r}(\varepsilon)$ the ( $k+p+r$ )-dimensional sphere centered at ( $\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}, \mathbf{0}_{r}$ ) with radius $\varepsilon$. The notation $A^{c}$ indicates complement of the set $A$.
C1: For each $\varepsilon>0$ and all $r=0,1, \ldots$, as $n \rightarrow \infty$, $\sup \left\{\left(L_{r}\left(\boldsymbol{\delta}_{r}\right)-L_{0}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}\right)\right): \boldsymbol{\delta}_{r} \in \mathcal{B}_{r}^{c}(\varepsilon)\right\} \xrightarrow{P}-\infty$.
C2: There exists an $\varepsilon_{0}>0$ such that for all $r \geq 0$, $L_{r}\left(\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}\right)$ is 2 times continuously differentiable in $\mathcal{B}_{r}\left(\varepsilon_{0}\right)$, for all $n$ sufficiently large. Define $\mathbf{U}_{r}\left(\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}\right)$ to be the vector of first partial derivatives and $-\mathbf{A}_{n r}\left(\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}\right)$ to be the matrix of second partial derivatives of the log-likelihood $L_{r}$, where the derivatives are with respect to the parameters ( $\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}$ ).
C3: There exist nonrandom, continuous matrices $\mathbf{A}_{r}$ ( $\boldsymbol{\eta}$, $\left.\theta_{1}, \ldots, \theta_{p+r}\right)$ that are positive definite in $\mathcal{B}_{r}\left(\varepsilon_{1}\right)$, and such that for $r \geq 0, \sup \left\{\left\|\mathbf{A}_{n r}\left(\boldsymbol{\delta}_{r}\right) / n-\mathbf{A}_{r}\left(\boldsymbol{\delta}_{r}\right)\right\|\right.$ : $\left.\boldsymbol{\delta}_{r} \in \mathcal{B}_{r}\left(\varepsilon_{1}\right)\right\} \xrightarrow{P} 0$, as $n \rightarrow \infty$ for some $0<\varepsilon_{1}<\varepsilon_{0}$.
C4: There exist continuous, positive definite, and nonrandom matrices $\mathbf{B}_{r}(\cdot)$ such that for each $r \geq 0, n^{-1 / 2} \mathbf{U}_{r}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}, \mathbf{0}_{r}\right)$ converges in distribution to $\left(\mathcal{Z}_{1}, \ldots, \mathcal{Z}_{k+p+r}\right) \sim \mathcal{N}\left(\mathbf{0}, \mathbf{B}_{r}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}\right)\right)$ as $n \rightarrow \infty$.
C5: The sequence $\left\{C_{n}\right\}$ tends to $C>1$ as $n$ and $R_{n}$ tend to $\infty$, and for every $\varepsilon>0$ there is a positive integer $r_{0}(\varepsilon)=r_{0}$ such that under $H_{0}$,

$$
P\left(\max _{r_{0} \leq r \leq R_{n}}\left[\frac{2\left(\mathcal{L}_{r}-L_{0}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}\right)\right)}{r}\right] \geq \frac{C+1}{2}\right)<\varepsilon,
$$

for all $n$ sufficiently large.

In this section, where we assume the likelihood model to be correctly specified, the matrices $\mathbf{A}_{r}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}, \mathbf{O}_{r}\right)$ and $\mathbf{B}_{r}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}\right)$ are exactly the same by Bartlett's identities.

Theorem 1. Assume that conditons $\mathrm{Cl}-\mathrm{C} 5$ hold. Then, under the null hypothesis (1):
a. The stochastic smoothing parameter $\hat{r}_{C_{n}}$ as defined in Section 2.2 is asymptotically distributed according to a generalized arc-sine distribution; that is, for $P_{0}=1$ and $P_{r}=P\left(S_{1}>0, \ldots, S_{r}>0\right), r=1,2, \ldots$

$$
\lim _{n \rightarrow \infty} P\left(\hat{r}_{C_{n}}=r\right)=P_{r} \exp \left(-\sum_{s=1}^{\infty} \frac{P\left(S_{s}>0\right)}{s}\right)
$$

where $S_{s}=\sum_{j=1}^{s}\left(V_{j}^{2}-C\right), s=1,2, \ldots$, and $V_{1}$, $V_{2}, \ldots$, are independent and identically distributed standard normal random variables.
b. The asymptotic distribution of the test statistic $T_{n}$ is given by

$$
P(T \leq x)=\exp \left[-\sum_{s=1}^{\infty} \frac{P\left(\chi_{s}^{2}>s x\right)}{s}\right],
$$

where $\chi_{s}^{2}$ has the chi-squared distribution with $s \mathrm{df}$.
We omit a proof of Theorem 1, because it would be essentially the same as Woodroofe's proof of his theorems 3 and 4. A few remarks are in order concerning Cl-C5. The condition that $R_{n}$ tend to $\infty$ is not necessary to obtain either a valid or a powerful test. If $R_{n}$ is fixed at $R$, then the limiting null distribution of $T_{n}$ changes somewhat, but for test levels no bigger than .10 , the distribution in part b is still an excellent approximation as long as $R \geq 5$ (Hart 1997, pp. 177-178). As noted by Woodroofe (1982), condition C5 can be replaced in particular cases by restrictions on the rate at which $R_{n}$ tends to $\infty$. The setting of Example 2 in Section 2.5 is one such case. Finally, it is worth noting that for test (4) to have reasonable power, the limiting value of $C_{n}$ should be finite. Indeed, if the sequence $C_{n}$ is unbounded as $n \rightarrow \infty$, it follows that under the null hypothesis, $P\left(\hat{r}_{C_{n}}=0\right)$ converges to 1 , in which case test (4) would not be useful. In the following theorem we establish that the test based on $T_{n}$ is consistent under very general conditions.

Theorem 2. Suppose that the null hypothesis is false in the sense that there exist $r_{a} \geq 1, \boldsymbol{\delta}_{r_{a}}=\left(\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r_{a}}\right)$ and a positive number $\zeta$ for which $\lim _{n \rightarrow \infty} P\left[\left(L_{r_{a}}\left(\boldsymbol{\delta}_{r_{a}}\right)-\right.\right. \left.\left.\mathcal{L}_{0}\right) / n>\zeta\right]=1$. If in addition $R_{n} \rightarrow \infty$ and $C_{n}$ tends to a finite constant, then the test with rejection region $T_{n} \geq C_{n}$ has power tending to 1 as $n \rightarrow \infty$.

Proof. For all $n$ sufficiently large, $R_{n}>r_{a}$, and hence

$$
\begin{aligned}
P\left(T_{n} \geq C_{n}\right) & \geq P\left(\frac{2\left(\mathcal{L}_{r_{a}}-\mathcal{L}_{0}\right)}{r_{a}} \geq C_{n}\right) \\
& \geq P\left(L_{r_{a}}\left(\delta_{r_{a}}\right)-\mathcal{L}_{0} \geq r_{a} C_{n} / 2\right)
\end{aligned}
$$

By assumption, the very last probability tends to 1 as $n \rightarrow \infty$, and so the result is proven.

Consistency of the MAIC test is desirable mainly on the assumption that the likelihood has been correctly specified but $\gamma$ is not in $\mathcal{G}$. Under such a circumstance, the main condition in Theorem 2 is generally a consequence of condition COb . However, as remarked before, COb is not necessary for consistency of the test. Also, the condition $R_{n} \rightarrow \infty$ is not necessary for consistency. Fixing $R_{n}$ at, say, 10 would still yield a test that is consistent against all but rather unusual alternatives.

### 2.5 Tests Based on Score Statistics

Both versions of the proposed AIC-based tests can be written in terms of the likelihood ratio statistic $2\left(\mathcal{L}_{r}-\mathcal{L}_{0}\right)$ for testing hypothesis (1) against the alternative that $\gamma(\cdot)$ has the form $\gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+r}\right)$. The Wald and score test statistics are two computationally attractive quadratic approximations of the likelihood ratio statistic. Either one could be used instead of $2\left(\mathcal{L}_{r}-\mathcal{L}_{0}\right)$. The Wald statistic (Boos 1992) needs the "unrestricted" maximum likelihood estimators (MLE's) whereas the score statistic only requires fitting the null model. The last property is appealing in our setting where one considers a large number of alternative models. We thus focus on score-based tests. A parallel development is possible for Wald statistics, which are, however, known to not be invariant to equivalent reparameterizations of nonlinear restrictions (see, e.g., Phillips and Park 1988).

Analogous to the definition of MAIC, we define the "score-based AIC,"

$$
\operatorname{SAIC}\left(r ; C_{n}\right)=\mathcal{S}_{r}-C_{n} r, \quad r=0,1, \ldots, R_{n}
$$

where

$$
\mathcal{S}_{r}=\left\{\begin{array}{l}
0 \quad \text { if } r=0 \\
\mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)^{T}\left(\mathbf{A}_{n r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)\right)^{-1} \mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right) \\
\quad \text { if } r=1,2, \ldots, R_{n}
\end{array}\right.
$$

$\hat{\boldsymbol{\delta}}_{r 0}=\left(\hat{\boldsymbol{\eta}}_{0}, \hat{\boldsymbol{\theta}}_{0}, \mathbf{O}_{r}\right)$ and ( $\hat{\boldsymbol{\eta}}_{0}, \hat{\boldsymbol{\theta}}_{0}$ ) is the null estimate; that is, the estimate of ( $\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p}$ ) obtained by maximizing the log-likelihood $L_{0}$. An apparently sensible test is that which rejects $H_{0}$ when the maximizer, $\tilde{r}_{C_{n}}$, of $\operatorname{SAIC}\left(r, C_{n}\right)$ is larger than 0 . This test is equivalent to one that rejects $H_{0}$ for $\tilde{T}_{n} \geq C_{n}$, where $\tilde{T}_{n}=\max _{1 \leq r \leq R_{n}}\left\{S_{r} / r\right\}$. The next theorem states that under $H_{0}, \tilde{r}_{C_{n}}$ and $\tilde{T}_{n}$ have the same limiting distributions as $\hat{r}_{C_{n}}$ and $T_{n}$.

Theorem 3. Let conditions $\mathrm{C} 1-\mathrm{C} 4$ hold, and assume that, as $n \rightarrow \infty, C_{n} \rightarrow C>1$ and $R_{n} \rightarrow \infty$. Furthermore, suppose that for every $\varepsilon>0$ there exists a positive integer $r_{0}(\varepsilon)=r_{0}$ such that under $H_{0}$,

$$
P\left(\max _{r_{0} \leq r \leq R_{n}} \frac{\mathcal{S}_{r}}{r} \geq \frac{C+1}{2}\right)<\varepsilon
$$

for all $n$ sufficiently large; we call this condition C6. Then the conclusion of Theorem 1 remains true if $\hat{r}_{C_{n}}$ and $T_{n}$ are replaced by $\tilde{r}_{C_{n}}$ and $\tilde{T}_{n}$.

Proof. A straightforward argument (available from the authors) shows that the desired result is a consequence of condition C6 and convergence in distribution of $\mathcal{S}_{1}, \ldots, \mathcal{S}_{r}$ to $V_{1}^{2}, V_{1}^{2}+V_{2}^{2}, \ldots, V_{1}^{2}+\cdots+V_{r}^{2}$ for each $r$, where $V_{1}, V_{2}, \ldots$ are iid standard normal random variables. The latter result is established as in the proof of Theorem 1 using the fact that, by definition, $\mathcal{S}_{r}$ is a quadratic form in $\mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)_{r}$, the last $r$ components of $\mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)$.

The matrix $\mathbf{A}_{n r}(\cdot)$ in $\mathcal{S}_{r}$ is the observed Fisher information evaluated at the null parameter estimates. In some cases it is possible to obtain explicit expressions for the expected Fisher information. In such cases one could replace $\mathbf{A}_{n r}(\cdot)$ by the expected information evaluated at the null estimates. There is no general consensus in the literature as to which of these two approaches is better (Boos 1992; Efron and Hinkley 1978). Asymptotically, the two versions of $\mathcal{S}_{r}$ are generally equivalent to first order. An appealing aspect of using expected information is that it often leads to simpler and more readily interpretable expressions for $\mathcal{S}_{r}$.

Example 1. Suppose that we have independent observations $X_{1}, \ldots, X_{n}$ with unknown density $f(x)$. Writing $f(x)=C_{\gamma} \exp (\gamma(x))$, we want to test the hypothesis $H_{0}: \gamma(x) \in \mathcal{G}$ for some parametric family of functions $\mathcal{G}=\left\{\gamma\left(x ; \theta_{1}, \ldots, \theta_{p}\right):\left(\theta_{1}, \ldots, \theta_{p}\right) \in \Theta\right\}$. Typical examples are testing for exponentiality or normality. Using an approximator of the form (2), the log-likelihood is

$$
\begin{aligned}
& L_{T}\left(\theta_{1}, \ldots, \theta_{p+r}\right) \\
& =\sum_{i=1}^{n} \gamma\left(X_{i} ; \theta_{1}, \ldots, \theta_{p}\right)+\sum_{i=1}^{n} \sum_{j=1}^{r} \theta_{p+j} u_{j}\left(X_{i}\right) \\
& \quad+n \log C_{\gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+r}\right)} .
\end{aligned}
$$

We may then proceed to test $H_{0}$ using either MAIC or SAIC as described in Section 2. It would be interesting to compare this goodness-of-fit test with the data-driven smooth tests proposed by Kallenberg and Ledwina (1997).

Example 2. Suppose that a regression model is based on a Gaussian likelihood and that we consider testing a null hypothesis about the mean: $H_{0}: \gamma(x)=\sum_{i=1}^{p} \theta_{i} \gamma_{i}(x)$, $0 \leq x \leq 1$, for some set of parameters $\theta_{1}, \ldots, \theta_{p}$. The test based on MAIC rejects $H_{0}$ for large values of $T_{n}=\max _{1 \leq r \leq R_{n}}\left\{n\left(\log \operatorname{SSE}_{p}-\log \operatorname{SSE}_{p+r}\right) / r\right\}$, where $\mathrm{SSE}_{p+r}$ denotes the error sum of squares from the least squares analysis of the linear model $\sum_{j=1}^{p} \theta_{j} \gamma_{j}(x)+ \sum_{j=1}^{r} \theta_{p+j} u_{j}(x)$. Next, consider the SAIC-based test where the expected Fisher information is evaluated at the MLE's under $H_{0}$. This test rejects $H_{0}$ for large values of $\tilde{T}_{n}= n \max _{1 \leq r \leq R_{n}}\left\{\left(\operatorname{SSE}_{p}-\operatorname{SSE}_{p+r}\right) / r\right\} / \operatorname{SSE}_{p}$. This statistic is identical to that proposed by Eubank and Hart (1992). When $H_{0}$ is true, the exact distribution of $\tilde{T}_{n}$ can be obtained for any $n$ (Hart 1997, pp. 177-178).

How do the likelihood and score-based statistics compare in this example? Suppose that $R_{n}$ is arbitrarily large but fixed. Then by using a Taylor series expansion of $\log \left(\operatorname{SSE}_{p+r} / \operatorname{SSE}_{p}\right)$ about 1 , it is easy to see that $T_{n}$ and $\tilde{T}_{n}$ are the same to first order, as $n \rightarrow \infty$. However, when
$R_{n}=n-p-1$, we have $T_{n} \geq n\left\{\log (n-p)+\log \left(\operatorname{SSE}_{p} /\right.\right. \left.(n-p))-\log \operatorname{SSE}_{n-1}\right\} /(n-p-1)$, and in general the last quantity tends to infinity in probability as $n \rightarrow \infty$. Eubank and Hart (1992) showed that in certain cases $\tilde{T}_{n}$ has a proper limiting distribution even if we take $R_{n}=n-p$. The fact that $\tilde{T}_{n}$ is less sensitive than $T_{n}$ to the choice of $R_{n}$ seems to be a clear advantage for the former statistic.

Example 3. Consider a sequence of time-ordered observations $X_{1}, \ldots, X_{n}$, and suppose that we wish to test the hypothesis that these observations are independent; that is, they are a white noise sequence. A quite general model for dependence is that which assumes $\left\{X_{t}\right\}$ to have the linear form $X_{t}=\mu+\sum_{i=0}^{\infty} \xi_{i} \epsilon_{t-i}, t=1,2, \ldots$, where the $\epsilon_{j}$ 's are i.i.d. random variables with mean 0 and finite variance $\sigma^{2}$ and $\sum_{i=0}^{\infty} \xi_{i}^{2}<\infty$. If this model holds, then the process $\left\{X_{t}\right\}$ is covariance stationary in the sense that $\operatorname{cov}\left(X_{i}, X_{i+j}\right)$ depends on $j$ but not $i$. If each $\xi_{i}$ other than $\xi_{0}$ is 0 , then the null hypothesis of independence is true. The model is characterized by the probability distribution of $\epsilon_{i}$ and the power spectrum $\gamma(\omega), 0 \leq \omega \leq 1$. A popular way of approximating such spectra (Newton 1988) is to use autoregressive representations, which imply that the process $\left\{X_{t}\right\}$ has the form $X_{t}-\mu=\sum_{i=1}^{r} \theta_{i}\left(X_{t-i}-\mu\right) +\epsilon_{t}, t=1,2, \ldots$, for some $r \geq 0$, where the $\epsilon_{t}$ 's are iid with mean 0 and finite variance and the 0 's of $1-\theta_{1} z-\cdots-\theta_{r} z^{r}$ are outside the unit circle in the complex plane. The case $r=0$ corresponds to the null hypothesis of independence. Suppose that we entertain the autoregressive model along with the assumption that $\epsilon_{t} \sim \mathcal{N}\left(0, \sigma^{2}\right)$. If we take $X_{i}=\mu$ for $i<1$ (a common practice in time series analysis), then the joint density of the observations can be written as in Section 2.1 with $\boldsymbol{\eta}=\left(\mu, \sigma^{2}\right)$ and $\gamma$ the spectral density of the process $\left\{X_{t}\right\}$. The quantity MAIC in this case has the form MAIC $\left(r ; C_{n}\right)=n\left(\log \hat{\sigma}_{0}^{2}-\log \hat{\sigma}_{r}^{2}\right)-C_{n} r, r= 0,1, \ldots, R_{n}$, where $\hat{\sigma}_{T}^{2}$ denotes the MLE of $\sigma^{2}$ for the order $r$ autoregressive model. In contrast, SAIC, based on expected Fisher information, takes the form SAIC $\left(r ; C_{n}\right)= \left[n \sum_{j=1}^{r} \hat{\rho}_{j}^{2} /(1-j / n)\right]-C_{n} r, r=0,1, \ldots, R_{n}$, where $\hat{\rho}_{j}$ is the usual sample autocorrelation function. It is noteworthy that the limit distribution of each test statistic is invariant under general moment conditions on $X_{1}, \ldots, X_{n}$. Another interesting aspect of this example is that both tests are apparently reasonable tests of white noise, but for different reasons. The quantity MAIC is just a penalty-modified version of Akaike's criterion for selecting autoregressive order. In contrast, SAIC is closely related to criteria for selecting the order of a moving average model for the time series $X_{1}, X_{2}, \ldots$ (Hart 1997, pp. 242-244). One thus anticipates that the power properties of the two tests will be different. The MAIC test would be expected to have better power than the SAIC test against autoregressive alternatives to white noise, whereas SAIC should tend to have better power when the process is of moving average type.

In the following theorem we provide conditions under which the score-based test is consistent. We require the following condition:

C7: There exists $r$ such that $\left\|\mathbf{U}_{r}\left(\hat{\delta}_{r 0}\right)\right\| / n$ is bounded away from 0 and $\infty$ in probability as $n \rightarrow \infty$.

Theorem 4. Suppose that ( $\hat{\boldsymbol{\eta}}_{0}, \hat{\boldsymbol{\theta}}_{0}$ ) converges in probability to some vector $\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}\right)$, let $\mathcal{B}_{r}(\varepsilon)$ be defined as in Section 2.4 in terms of this vector, and assume that conditions C2, C3, and C7 hold. If, in addition, $R_{n} \rightarrow \infty$ and $C_{n} \rightarrow C<\infty$, then the power of the test with rejection region $\left\{\max _{1 \leq j \leq R_{n}}\left\{\mathcal{S}_{j} / j\right\} \geq C_{n}\right\}$ tends to 1 as $n \rightarrow \infty$.

Proof. For all $n$ sufficiently large, we have $R_{n}> r$, and so $P\left(\tilde{T}_{n} \geq C_{n}\right) \geq P\left(\mathcal{S}_{r} \geq r C_{n}\right)$. Defining $\xi_{n}=n^{-2} \mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)^{T} \mathbf{A}_{r}^{-1}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}, \mathbf{0}_{r}\right) \mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)$ and $\Delta_{n}= n^{-2} \mathbf{U}_{r}\left(\hat{\delta}_{r 0}\right)^{T}\left[n \mathbf{A}_{n r}^{-1}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)-\mathbf{A}_{r}^{-1}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}, \mathbf{0}_{r}\right)\right] \mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)$, we have $P\left(\mathcal{S}_{r} \geq r C_{n}\right)=P\left(\xi_{n}+\Delta_{n} \geq r C_{n} / n\right)$. By conditions C3 and C7, it follows that there exists a positive number $a$ such that $P\left(\xi_{n} \geq a\right) \rightarrow 1$ as $n \rightarrow \infty$. Using the consistency of the null MLE for ( $\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}$ ) and conditions C3 and C7, it is easily shown that $\Delta_{n}$ tends to 0 in probability. Together, the last two facts imply that $P\left(\xi_{n}+\Delta_{n} \geq r C_{n} / n\right) \rightarrow 1$ as $n \rightarrow \infty$, and the result follows.

Condition C7 represents the negation of the null hypothesis. Intuitively, this condition will hold as long as there exists an $r$ for which ( $\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}, \mathbf{0}_{r}$ ) is not a local maximum of $\lim _{n \rightarrow \infty} \log$-likelihood $/ n$.

## 3. ROBUST TESTS

Maximum likelihood methods, as described in Section 2 , are very generally applicable. An important assumption, however, is that the true joint probability density function (pdf) $g_{n}\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{n}\right)$ of the observations $\left(\mathbf{Z}_{1}, \ldots, \mathbf{Z}_{n}\right)$ belongs to a family having the form $f_{n}\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{n} ; \gamma(\cdot), \boldsymbol{\eta}\right)$, as specified by (3). In this section we construct lack-of-fit tests for cases where this assumption does not necessarily hold. We first consider the case of a misspecified likelihood, and then discuss a test statistic derived from general estimating equations.

### 3.1 Likelihood Misspecification

When the true data-generating process is not completely described by the assumed likelihood, the likelihood model is misspecified (see White 1994 and references therein). It turns out (see Theorem 5) that the asymptotic distribution of test statistics resulting from MAIC and SAIC can be quite complicated and, more important, can depend on unknown model parameters. Here we propose a robustified score statistic that has the same asymptotic distribution as the statistic appearing in Theorem 1.

As before, our interest is in testing the hypothesis (1), where now the "true parameters" are the best approximating values of $\left(\boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}\right)$ in the Kullback-Leibler sense. In other words, the true parameters minimize the distance $E\left[\log g_{n}\left(\mathbf{Z}_{1}, \ldots, \mathbf{Z}_{n}\right)-\right. \left.\log f_{n}\left(\mathbf{Z}_{n}, \ldots, \mathbf{Z}_{n} ; \gamma\left(\cdot ; \theta_{1}, \ldots, \theta_{p+r}\right), \boldsymbol{\eta}\right)\right]$ between $f_{n}$ and $g_{n}$, where, here and elsewhere, all expectations are with respect to $g_{n}$. If there exists a unique vector $(\boldsymbol{\eta}, \boldsymbol{\theta})$ such that $f_{n}\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{n} ; \gamma(\cdot ; \boldsymbol{\theta}), \boldsymbol{\eta}\right)=g_{n}\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{n}\right)$, then this is also the best approximating parameter obtained by minimizing this distance function.

Theorem 5. Assume conditions $\mathrm{C} 1-\mathrm{C} 4$ and let $R_{n}=R$, a fixed positive integer. The maximizers of MAIC $\left(r ; C_{n}\right)$ and SAIC $\left(r ; C_{n}\right)$ both have the limiting distribution $\mathcal{P}$, given by
$\mathcal{P}(r)=P\left(\tilde{S}_{r}-C r \geq \tilde{S}_{j}-C j, \quad \forall j=0, \ldots, R\right)$,

$$
r=0,1, \ldots, R,
$$

where $\tilde{S}_{j}=\left(\mathbf{0}_{k+p}, \mathcal{Z}_{k+p+1}, \ldots, \mathcal{Z}_{k+p+j}\right) \mathbf{A}_{j}^{-1}\left(\boldsymbol{\eta}^{0}, \boldsymbol{\theta}^{0}, \mathbf{0}_{j}\right) \left(\mathbf{0}_{k+p}, \mathcal{Z}_{1}, \ldots, \mathcal{Z}_{k+p+j}\right)^{T}$, using the notation as in C3 and C 4 .

Proof. If the likelihood model is not the true likelihood of the data, the matrices $\mathbf{A}_{r}$ and $\mathbf{B}_{r}$ as defined in C3 and C4 are in general not the same. Consequently, the asymptotic distribution of $\tilde{\mathcal{S}}_{j}$ is a weighted sum of chi-squared random variables, and in general no further simplification of the limiting distribution is possible.

Note that C3 and C4 imply that for a correctly specified model, Theorem 5 reduces to Theorem 1, because the matrices $\mathbf{A}_{r}$ and $\mathbf{B}_{r}$ are in that case exactly the same.

To overcome the practical problems with the asymptotic distribution in Theorem 5, we define a score statistic in analogy to those of Engle (1984) and Kent (1982). Let $\mathcal{R}_{0}=$ 0 and

$$
\begin{aligned}
\mathcal{R}_{r}= & \mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)_{r}^{T}\left(\mathbf{A}_{n r}^{-1}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)\right)_{r} \\
& \times\left[\left(\mathbf{A}_{n r}^{-1}\left(\hat{\boldsymbol{\delta}}_{r 0}\right) \mathbf{B}_{n r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right) \mathbf{A}_{n r}^{-1}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)\right)_{r}\right]^{-1} \\
& \times\left(\mathbf{A}_{n r}^{-1}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)\right)_{r} \mathbf{U}_{r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)_{r}
\end{aligned}
$$

for $r=1,2, \ldots$, where $\mathbf{B}_{n r}(\cdot)$ is a consistent estimator of $\mathbf{B}_{r}(\cdot), \mathbf{D}_{r}(\cdot)_{r}$ is the lower right ( $r \times r$ ) submatrix of a $(k+p+r)$ dimensional matrix $\mathbf{D}_{r}(\cdot)$, and $\mathbf{U}_{r}(\cdot)_{r}$ are the last $r$ components of the length $k+p+r$ vector $\mathbf{U}_{r}(\cdot)$. Now define $\operatorname{RAIC}\left(r ; C_{n}\right)=\mathcal{R}_{T}-C_{n} r, r=0,1, \ldots, R_{n}$. We may then reject $H_{0}$ whenever the maximizer of $\operatorname{RAIC}\left(r ; C_{n}\right)$ exceeds 0 . This test is equivalent to one that rejects $H_{0}$ whenever $\bar{T}_{n}=\max _{1 \leq r \leq R_{n}}\left\{\mathcal{R}_{r} / r\right\} \geq C_{n}$. Under $H_{0}$ and appropriate regularity conditions, the statistic $\bar{T}_{n}$ will have the same limit distribution as that of $T_{n}$ in Theorem 1. Moreover, this result will not in general depend on a correct specification of the likelihood. Rather than stating a theorem to this effect, we use simulation in Section 4 to investigate the adequacy of the large-sample distribution for finite $n$.

In certain settings where series estimators are used to approximate $\gamma$, the matrices $\mathbf{A}_{n r}\left(\hat{\boldsymbol{\delta}}_{r 0}\right)$ can be greatly simplified by an orthogonalization process, as shown in the next example.

Example 4. Consider the regression model $Y_{i} \sim \mathcal{N}\left(\eta\left(x_{i}\right), \gamma\left(x_{i}\right)\right), i=1, \ldots, n$, where $Y_{1}, \ldots, Y_{n}$ are independent and $x_{1}, \ldots, x_{n}$ are fixed design points on, say, $[0,1]$. The tests based on MAIC and SAIC are in this case tests for homoscedasticity, where now the vector $\boldsymbol{\eta}^{T}=\left(\eta_{1}, \ldots, \eta_{k}\right)$ in the mean function $\eta(x)=\sum_{\ell=1}^{k} \eta_{\ell} \psi_{\ell}(x)$ is considered the nuisance parameter and the function of interest is $\gamma\left(x ; \theta_{1}, \ldots, \theta_{T}\right)=\exp \left\{\theta_{1}+\sum_{j=1}^{r} \theta_{1+j} u_{j}(x)\right\}$. We consider $k$ fixed and assume that the orthogonality property
$\sum_{i=1}^{n} \psi_{j}\left(x_{i}\right) \psi_{\ell}\left(x_{i}\right)=n \delta_{j \ell}$ holds for each $j, \ell=0, \ldots, k$. Next, suppose that the set $\left\{u_{1}, u_{2}, \ldots\right\}$ is complete and orthogonalized such that $\sum_{i=1}^{n} u_{j}\left(x_{i}\right) u_{\ell}\left(x_{i}\right)=n \delta_{j \ell}$, for $j, \ell=0, \ldots, r$ for every $r$, where $u_{0}=1$. The orthogonalization of the $\psi_{j}$ 's and $u_{j}$ 's can be done using the GramSchmidt process (see, e.g., Rao 1973). We focus attention on the SAIC-based test (using expected Fisher information) for the null hypothesis of homoscedasticity; that is, $H_{0}: \gamma(x)=\theta_{1}, \quad 0 \leq x \leq 1$ for some value of $\theta_{1}>0$. Define $\hat{\sigma}_{0}^{2}=\left(\sum_{i=1}^{n} e_{i}^{2}\right) / n$, where $e_{i}$ are the residuals of the ordinary least squares fit; then the SAIC test rejects $H_{0}$ for large values of $\tilde{T}_{n}=\max _{1 \leq r \leq R_{n}}\left\{\sum_{j=1}^{r} \hat{\phi}_{j}^{2} / r\right\} /\left(2 \hat{\sigma}_{0}^{2}\right)$, where $\hat{\phi}_{j}=\left(\sum_{i=1}^{n} e_{i}^{2} u_{j}\left(x_{i}\right)\right) / n$ for $j=1, \ldots, r$. Note that $\tilde{T}_{n}$ uses $2 \hat{\sigma}_{0}^{4}$ to estimate the null variance of $e_{i}^{2}$. This is a consistent estimator when assuming Gaussian errors but not in general, indicating that $\tilde{T}_{n}$ is not robust against nonnormality. However, the RAIC-based statistic is identical to the statistic of Liaw (1997), which he showed to be asymptotically valid even for non-Gaussian errors and $R_{n}=n-k-1$.

Because the statistic $\tilde{T}_{n}$ requires only the score equations, and not knowledge of the likelihood itself, the RAIC test will also be applicable in more general statistical models. We consider these next.

### 3.2 Estimating Equations

Parameter estimators can be obtained by solving more general estimating equations (GEE's) than likelihood equations. If the parameter of interest is the (conditional) mean of the response variables, then the idea of solving a set of score equations $\mathbf{U}_{r}(\cdot)=0$ in likelihood models is generalized to the construction of quasi-likelihood equations (Wedderburn 1974), and to the multivariate version, the GEE's (Liang and Zeger 1986). Other frequently used estimating equations are found in the context of M estimation (Huber 1981), resulting in robust regression models.

In the absence of a likelihood function, it is clear that an MAIC-based test can no longer be constructed. Instead, an RAIC criterion may be defined as follows. Let $\mathbf{Z}_{1}, \ldots, \mathbf{Z}_{n}$ be independent observations, and consider the sets of estimating equations $\sum_{i=1}^{n} \boldsymbol{\psi}_{r}\left(\mathbf{Z}_{i} ; \boldsymbol{\eta}, \theta_{1}, \ldots, \theta_{p+r}\right)=\mathbf{0}_{p+k+r}$, where $\psi_{r}$ is a $p+k+r$ vector of statistics, $r=0,1, \ldots$ Let ( $\hat{\boldsymbol{\eta}}_{0}, \hat{\boldsymbol{\theta}}_{0}$ ) be the solution to the set of equations corresponding to $r=0$, define $\widehat{\boldsymbol{\delta}}_{r 0}=\left(\hat{\boldsymbol{\eta}}_{0}, \hat{\boldsymbol{\theta}}_{0}, \mathbf{O}_{r}\right)$, and take $\boldsymbol{\xi}_{r}$ to be the length $p+k+r$ vector equal to $\sum_{i=1}^{n} \boldsymbol{\psi}_{r}\left(\mathbf{Z}_{i} ; \hat{\boldsymbol{\eta}}_{0}, \hat{\boldsymbol{\theta}}_{0}, \mathbf{O}_{r}\right)$. Now define $\mathcal{R}_{0}=0$ and

$$
\begin{aligned}
\mathcal{R}_{r}= & \left(\boldsymbol{\xi}_{r}\right)_{r}^{T}\left(\tilde{\mathbf{A}}_{n r}^{-1}\left(\widehat{\boldsymbol{\delta}}_{r 0}\right)\right)_{r} \\
& \times\left[\left(\tilde{\mathbf{A}}_{n r}^{-1}\left(\widehat{\boldsymbol{\delta}}_{r 0}\right) \tilde{\mathbf{B}}_{n r}\left(\widehat{\boldsymbol{\delta}}_{r 0}\right) \tilde{\mathbf{A}}_{n r}^{-1}\left(\widehat{\boldsymbol{\delta}}_{r 0}\right)\right)_{r}\right]^{-1} \\
& \times\left(\tilde{\mathbf{A}}_{n r}^{-1}\left(\widehat{\boldsymbol{\delta}}_{r 0}\right)\right)_{r}\left(\boldsymbol{\xi}_{r}\right)_{r}
\end{aligned}
$$

for $r=1,2, \ldots$, where $\tilde{\mathbf{A}}_{n r}(\cdot)$ is a $(p+k+r) \times(p+ k+r$ ) matrix of partial derivatives of $\boldsymbol{\psi}_{r}$ and $\tilde{\mathbf{B}}_{n r}\left(\widehat{\boldsymbol{\delta}}_{r 0}\right)= \sum_{i=1}^{n} \boldsymbol{\psi}_{r}\left(\mathbf{Z}_{i} ; \hat{\boldsymbol{\eta}}_{0}, \hat{\boldsymbol{\theta}}_{0}, \mathbf{0}_{r}\right) \boldsymbol{\psi}_{r}\left(\mathbf{Z}_{i} ; \hat{\boldsymbol{\eta}}_{0}, \hat{\boldsymbol{\theta}}_{0}, \mathbf{0}_{r}\right)^{T}$. We may now define a test statistic based on RAIC as before. Conditions
under which previous theorems remain valid could be stated here, but we do not pursue this any further.

Example 5. Let $\mathbf{Y}_{i}=\left(Y_{i 1}, \ldots, Y_{i n}\right)^{T}$ and $\mathbf{X}_{i}= \left(X_{i 1}, \ldots, X_{i n}\right)^{T}$ denote a vector of $n$ repeated observations and a vector of covariates, measured on the $i$ th subject, $i=1, \ldots, m$. The multivariate Gaussian model for longitudinal data can be extended in different ways to generalized linear models (GLM's) for longitudinal responses (see Diggle, Liang, and Zeger 1994). A so-called marginal approach that does not require specification of the entire likelihood are the GEE's, introduced by Liang and Zeger (1986) and Zeger and Liang (1986). The function of interest is $\gamma(x)=E\left(Y_{i j} \mid X_{i j}=x\right)$ which can be approximated as before by $\gamma\left(x ; \theta_{1}, \ldots, \theta_{p+r}\right)=h^{-1}\left(\sum_{i=1}^{p} \theta_{i} \gamma_{i}(x)+\right. \left.\sum_{j=1}^{r} \theta_{p+j} u_{j}(x)\right)$ for some (specified) link function $h$. A GEE estimator of $\left(\theta_{1}, \ldots, \theta_{p+r}\right)$ is the solution to $\mathbf{U}\left(\theta_{1}, \ldots, \theta_{p+r}\right)=\sum_{i=1}^{m} \mathbf{D}_{i}^{T} \boldsymbol{\Sigma}_{i}^{-1}\left(\mathbf{Y}_{i}-\gamma\left(\mathbf{X}_{i} ; \theta_{1}, \ldots, \theta_{p+r}\right)\right)$ where $\mathbf{D}_{i}=\partial \gamma\left(\mathbf{X}_{i} ; \theta_{1}, \ldots, \theta_{p+r}\right) / \partial\left(\theta_{1}, \ldots, \theta_{p+r}\right), \boldsymbol{\Sigma}_{i}= \mathbf{A}_{i}^{1 / 2} \mathbf{R}_{i} \mathbf{A}_{i}^{1 / 2}, \mathbf{A}_{i}=\operatorname{diag}\left(\operatorname{var}\left(\epsilon_{i 1}\right), \ldots, \operatorname{var}\left(\epsilon_{i n}\right)\right)$, and $\mathbf{R}_{i}$ is an $n \times n$ correlation matrix. It is assumed that $\operatorname{var}\left(\epsilon_{i j}\right)= \nu\left(E\left(Y_{i j}\right)\right) \eta_{1}$, where $\nu$ is a known function and $\eta_{1}$ is a scale parameter. The "working" correlation matrix $\mathbf{R}_{i}$ may also depend on a vector of unknown parameters $\left(\eta_{2}, \ldots, \eta_{k}\right)$.

To obtain a test of the null hypothesis $H_{0}: \gamma(x)= h^{-1}\left(\sum_{i=1}^{p} \theta_{i} \gamma_{i}(x)\right)$, robust score statistics $\mathcal{R}_{r}$ may be constructed and a test statistic defined as $\max _{1 \leq r \leq R_{n}} \mathcal{R}_{r} / r$, the largest of a set of weighted robust score statistics.

## 4. SIMULATION STUDY

This section illustrates certain aspects of the finitesample behavior of our proposed tests. These include level properties of the various tests, a power comparison of the proposed nonparametric tests for correctly specified models, and a power comparison with a classical parametric test.

### 4.1 Type I Error Probabilities

When the assumed likelihood model is incorrect, the distributional properties as formulated in Theorems 1 and 3 are no longer valid. Therefore, it is expected that the MAICand SAIC-based tests will have inaccurate levels, whereas the level of the RAIC-based test should remain close to the nominal value. We illustrate this with simulations for generalized linear models GLM's (see, e.g., McCullagh and Nelder 1989). Gourieroux, Monfort, and Trognon (1984) have shown that when a GLM is used, the mean can still be consistently estimated even if the true pdf does not belong to the specified class of exponential family models.

In our first setting, we generated data from independent, zero-inflated Poisson response variables $Y_{i}=U_{i} \times V_{i}, i= 1, \ldots, n$, where $U_{i} \sim \operatorname{Poisson}\left(\lambda\left(x_{i}\right)\right), \lambda(x)=\exp (2(x+ .2)(x-.3)), V_{i} \sim \operatorname{bin}(1, \pi)$, and $U_{i}$ and $V_{i}$ are independent. The design points $x_{1}, \ldots, x_{n}$ were chosen to be equidistant between 0 and 1 . The null hypothesis $H_{0}: \ln (\lambda(x))=\theta_{0}+ \theta_{1} x+\theta_{2} x^{2}$ is tested at a $5 \%$ significance level. Table 1 shows estimated type I error probabilities (as \%) based on 1,000 simulation runs.

Table 1. Simulation Results for Zero-Inflated Poisson Data
| $n$ | $\pi$ | Polynomial basis |  |  | Cosine basis |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | MAIC | SAIC | RAIC | MAIC | SAIC | RAIC |
| 30 | 1 | 4.2 | 3.8 | 4.4 | 4.2 | 3.6 | 4.8 |
|  | . 9 | 9.5 | 7.7 | 4.4 | 9.1 | 7.8 | 4.4 |
|  | 8 | 15.5 | 12.2 | 5.4 | 14.5 | 11.4 | 5.4 |
|  | . 7 | 22.1 | 15.7 | 5.9 | 21.2 | 15.0 | 6.0 |
|  | . 6 | 32.4 | 20.8 | 5.4 | 30.8 | 19.7 | 5.4 |
| 60 | 1 | 5.4 | 5.1 | 5.8 | 5.6 | 5.4 | 5.7 |
|  | 9 | 11.5 | 10.0 | 6.5 | 10.6 | 9.5 | 6.4 |
|  | 8 | 16.1 | 14.7 | 5.9 | 15.9 | 14.7 | 6.2 |
|  | . 7 | 21.4 | 19.0 | 5.3 | 20.6 | 19.4 | 5.1 |
|  | 6 | 29.8 | 25.3 | 5.5 | 27.6 | 23.9 | 5.3 |


Note first that the case $\pi=1$ corresponds to a correctly specified model. Here each of the three tests maintains the nominal $5 \%$ significance level. As $\pi$ decreases from 1 (i.e., misspecified models), the type I error probabilities of the MAIC and SAIC tests increase. In contrast, the RAIC test nicely holds the prescribed level of $5 \%$.

As a second example, we consider overdispersed binomial data, generated from a beta-binomial model $\mathrm{BB}(N, \pi(x), \rho)$, where $N=13, \ln (\pi(x) /(1-\pi(x)))= -5+5 x$, and $\ln ((1+\rho(x)) /(1-\rho(x)))=c$. Here $\pi(x)$ represents success probability, $\rho(x)$ the intracluster correlation, $N$ the cluster size, and $x$ a covariate. (For more details on the beta-binomial model, see Skellam 1948 and, in a similar setting, Aerts and Claeskens 1997). Using the binomial likelihood in MAIC, SAIC, and RAIC, we tested the hypothesis that the logit of $\pi(x)$ is linear in $x$ at a 5\% significance level. If $\rho \equiv 0$, the beta-binomial model reduces to the binomial model (no overdispersion), but for $\rho>0$, the binomial likelihood is incorrect. Simulated type I error probabilities (as \%) based on 1,000 simulation runs are shown in Table 2.

When the model is correctly specified ( $c=0$ ), both score tests have empirical levels close to the nominal level. However, even a small amount of intracluster correlation causes highly inflated type I error probabilities for the SAIC test. The RAIC test nicely corrects for the model misspecification and has the correct type I error rate. (The MAIC test was not considered in this part of the simulation, because of numerical problems with the MLE's.)

### 4.2 Power Comparisons When Likelihood Is Correctly Specified

Here we address the question "How does the power of an RAIC test compare with that of MAIC and SAIC tests for correctly specified models?" In general, one might expect the RAIC test to have less power, but because there are many ways to specify an alternative model, there is probably no simple answer. To investigate this question, we generated Poisson data $Z_{i}=\left(Y_{i}, x_{i}\right), i=1, \ldots, n=30$, where the $Y_{i}$ 's were independent with $Y_{i} \sim \operatorname{Poisson}\left(\lambda\left(x_{i}\right)\right)$, $\ln (\lambda(x))=-1+4 x^{a}$ and the $x_{i}$ 's were equally spaced in $[0,1]$. We tested the hypothesis $H_{0}: \ln (\lambda(x))=\theta_{0}+\theta_{1} x$ at a 5\% significance level.

Table 3 shows the simulated rejection probabilities (as $\%$ ) based on 1,000 simulation runs. In this example, losses

Table 2. Simulation Results for Beta-Binomial Data
| $n$ | $c$ | Polynomial basis |  | Cosine basis |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | SAIC | RAIC | SAIC | RAIC |
| 30 | 0 | 4.4 | 6.4 | 5.0 | 4.8 |
|  | . 05 | 9.1 | 5.6 | 10.7 | 4.5 |
|  | . 10 | 14.6 | 5.6 | 15.3 | 4.5 |
|  | . 20 | 25.2 | 5.6 | 27.1 | 4.5 |
|  | . 30 | 34.6 | 3.4 | 40.2 | 3.8 |
| 60 | 0 | 5.4 | 6.8 | 6.2 | 5.6 |
|  | . 05 | 8.8 | 5.9 | 10.7 | 5.7 |
|  | . 10 | 14.1 | 5.2 | 14.6 | 4.6 |
|  | . 20 | 23.8 | 4.4 | 28.0 | 4.6 |
|  | . 30 | 35.6 | 4.4 | 39.4 | 5.2 |


in power for the RAIC test are significant, meaning that unnecessary use of the robust procedure is quite costly.

In a second example, we generated data from the alternative $\lambda(x)=\exp (-1+4 x+a \ln (x+1))$, with $n=30$. The simulated rejection probabilities (as \%) over 1,000 simulation runs are shown in Table 4. For this alternative, the RAIC test has either comparable or somewhat higher power than the MAIC and SAIC tests, which are again comparable to each other. Obviously then, one does not always pay a price when using a robust test unnecessarily.

### 4.3 Comparison With a Parametric Test

We now compare the MAIC test with a likelihood ratio test in the context of longitudinal data. One would expect no test to have substantially higher power than the likelihood ratio test based on a correctly specified alternative.

Let $\mathbf{Y}_{i}=\left(Y_{i 1}, \ldots, Y_{i n}\right)^{T}$ and $\mathbf{X}_{i}=\left(X_{i 1}, \ldots, X_{i n}\right)^{T}$ denote a vector of $n$ repeated observations and a vector of covariates, measured on the $i$ th subject, $i=1, \ldots, m$. A possible Gaussian model for longitudinal data is $\mathbf{Y}=\gamma(\mathbf{X} ; \boldsymbol{\theta}) +\epsilon$, where $\mathbf{Y}^{T}=\left(\mathbf{Y}_{1}^{T}, \ldots, \mathbf{Y}_{m}^{T}\right), \mathbf{X}^{T}=\left(\mathbf{X}_{1}^{T}, \ldots, \mathbf{X}_{m}^{T}\right)$, $\gamma(\mathbf{X} ; \boldsymbol{\theta})$ is the $n m$ vector obtained by applying $\gamma(\cdot ; \boldsymbol{\theta})$ elementwise to $X$, and $\epsilon \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma})$, with $\boldsymbol{\Sigma}$ a block-diagonal matrix with $n \times n$ blocks $\Sigma_{i}$ representing the covariance matrix of $\mathbf{Y}_{i}, i=1, \ldots, m$.

In the simulations that follow, we generated Gaussian observations from 15 (independent) experimental units (so $n=15)$ and $m=5$. We took $X_{i j}=j$ for all $i$ and $j=1, \ldots, 5$, which corresponds to using time as the covariate and observing all experimental units at the same time points. We took the mean function to be $\gamma(t)=\beta t^{3}$ for selected values of $\beta$, and for each $i$, the elements of $\Sigma_{i}$ were of the form $\sigma^{2} \exp \left(-\phi(j-k)^{2}\right), j, k=1, \ldots, 5$.

Table 3. Empirical Power for Poisson Model With
$\ln (\lambda(x))=-1+4 x^{a}$
| $a$ | Polynomial basis |  |  | Cosine basis |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | MAIC | SAIC | RAIC | MAIC | SAIC | RAIC |
| 1.0 | 5.5 | 5.4 | 5.1 | 6.0 | 5.5 | 5.4 |
| 1.2 | 9.8 | 10.7 | 6.5 | 6.8 | 8.0 | 6.0 |
| 1.4 | 16.3 | 20.5 | 8.9 | 11.0 | 11.8 | 7.2 |
| 1.6 | 26.4 | 33.6 | 13.0 | 18.1 | 22.4 | 10.4 |
| 1.8 | 39.8 | 45.9 | 19.7 | 29.9 | 34.9 | 15.6 |
| 2.0 | 50.7 | 57.4 | 26.5 | 38.6 | 44.7 | 22.4 |


Table 4. Empirical Power for Poisson Model With
$\lambda(x)=\exp (-1+4 x+a \ln (x+1))$.
| $a$ | Polynomial basis |  |  | Cosine basis |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | MAIC | SAIC | RAIC | MAIC | SAIC | RAIC |
| 0 | 5.5 | 5.4 | 5.1 | 6.0 | 5.5 | 5.4 |
| 1.0 | 4.8 | 3.7 | 6.2 | 4.9 | 4.5 | 4.4 |
| 3.0 | 9.8 | 8.4 | 12.9 | 9.2 | 8.1 | 9.0 |
| 5.0 | 39.1 | 36.4 | 42.6 | 32.9 | 30.8 | 31.2 |
| 7.0 | 93.5 | 92.5 | 92.5 | 86.3 | 85.5 | 84.3 |


Taking $\beta$ equal to $0, .0075$, and .01 , we tested the null hypothesis of linearity $H_{0}: \gamma(t)=\beta_{0}+\beta_{1} t$ at nominal significance level $5 \%$. Let $T_{n}^{P}$ and $T_{n}^{C}$ be the versions of $T_{n}$ (Sec. 2.3) that use polynomial and cosine bases. We then considered four test statistics: $T_{n}^{P}, T_{n}^{C}, \max \left(T_{n}^{P}, T_{n}^{C}\right)$, and a likelihood ratio in which the alternative hypothesis was $H_{1}: \gamma(t)=\beta_{0}+\beta_{1} t+\beta_{3} t^{3}$. Table 5 shows estimated rejection probabilities based on 500 samples. MLE's were computed using the Oswald software in S-PLUS (Smith 1997). Because the true alternative is a polynomial, it is not surprising that the MAIC test based on polynomials performs substantially better than the one based on cosines. In fact, the power of $T_{n}^{P}$ is comparable to that of the parametric likelihood ratio test.

In practice, an optimal choice of basis is not a trivial problem, and hence the results for $T_{n}^{\text {max }}=\max \left(T_{n}^{P}, T_{n}^{C}\right)$ are of interest. We compared this statistic to a critical value of 5.236, the 97.5th percentile of $T_{n}$ 's limit distribution. Bonferroni's inequality implies that the corresponding (asymptotic) level of the $T_{n}^{\text {max }}$-based test is no more than $5 \%$. Interestingly, the empirical power of the "Bonferroni" test is not much lower than that of $T_{n}^{P}$. Note also that the empirical level for $T_{n}^{\text {max }}$ is close to $2.5 \%$, suggesting that proper adjustment of the critical value will make the power of $T_{n}^{\text {max }}$ close to that of $T_{n}^{P}$.

## 5. THE WISCONSIN DIABETES STUDY

Here we apply our proposed tests to a dataset concerning the effect of the systolic blood pressure on the occurrence of macular edema for younger-onset diabetic persons. (See

Table 5. Empirical Powers for Three MAIC-Based Tests and a Likelihood Ratio Test for Longitudinal Data
| $\sigma^{2}, \phi$ | $\beta$ | Order selection tests |  |  | Likelihood-ratio test |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | $T_{n}^{P}$ | $T_{n}^{C}$ | $T_{n}^{\text {max }}$ |  |
| 4, . 1 | 0 | 4.6 | 4.6 | 2.6 | 4.8 |
|  | . 0075 | 36.0 | 9.0 | 25.4 | 38.4 |
|  | 01 | 57.4 | 15.4 | 46.8 | 61.6 |
| 4, . 5 | 0 | 4.8 | 5.2 | 2.4 | 5.2 |
|  | . 0075 | 8.6 | 5.6 | 5.0 | 10.0 |
|  | . 01 | 11.2 | 5.4 | 8.0 | 12.6 |
| .5, . 1 | 0 | 4.6 | 4.6 | 2.6 | 4.8 |
|  | . 0075 | 99.8 | 60.0 | 99.0 | 99.8 |
|  | . 01 | 100 | 83.6 | 99.8 | 100 |
| .5, . 5 | 0 | 4.8 | 5.2 | 2.4 | 5.2 |
|  | . 0075 | 32.8 | 10.0 | 25.4 | 36.4 |
|  | . 01 | 55.6 | 15.8 | 45.6 | 57.6 |


Klein et al. 1984 for more information about these data.) The data to be analyzed are $\left(x_{i}, y_{i}\right), i=1, \ldots, 720$, where $y_{i}$ is the number of eyes infected $(0,1$, or 2$)$ and $x_{i}$ is the systolic blood pressure. Let $\pi(x)$ denote the expected proportion of infected eyes for a diabetic person whose systolic blood pressure is $x$, and let $\rho(x)$ denote the correlation between the outcomes of the left eye and the right eye. We wish to test whether the correlation changes with systolic blood pressure, in which case the null hypothesis is

$$
H_{0}: \rho(x)=\theta, \quad \text { for each } x .
$$

We consider two models for these data, both accounting for the intraperson correlation. The first model is the full likelihood beta-binomial model (Sec. 4.1). The second model uses GEE's (GEE2; Zhao and Prentice 1990) based on the first four moments of the Bahadur (1961) model. We calculate test statistics for hypothesis (5) using both polynomial and cosine alternatives. First, we transform the design points to the interval $(0,1)$. In the notation of Section 2.1, we then consider $u_{j}(x)=x^{j}$ and $u_{j}(x)=\cos (\pi j x)$, $j=1,2, \ldots, 15$. The values of the statistics, in the form $\max _{1 \leq r \leq R_{n}}\left(V_{T} / r\right)$, where $V_{T}$ is either $2\left(\mathcal{L}_{r}-\mathcal{L}_{0}\right), \mathcal{S}_{T}$, or $\mathcal{R}_{r}$, are given in Table 6. Note that for the GEE2 model, only the RAIC criterion yields relevant test statistics and that the MAIC criterion is not defined in this context. The parameters corresponding to $\pi(x)$ are, for present purposes, nuisance parameters. It turns out that for these data, the test results are very similar for a linear or a quadratic form of $\pi(x)$. None of the "naive" score based tests is able to reject the null hypothesis. In the GEE model the $p$ values are slightly smaller than in the full likelihood model, but in both cases the RAIC yields $p$ values that are no larger than $5.5 \%$. These results indicate the necessity of modeling the correlation as a nonconstant function of systolic blood pressure.

Table 6. Test Statistics for the Wisconsin Diabetes Data
|  | Polynomial basis |  |  |  | Cosine basis |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Criterion | Value $\quad \rho$ value $\quad R_{n}$ |  | Value $\quad \rho$ value $\quad R_{n}$ |  |  |  |  |


Beta-Binomial Likelihood Model

Table 6. Test Statistics for the Wisconsin Diabetes Data
| $\pi(x)$ linear |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SAIC | 2.096 | . 262 | 15 | 2.347 | . 207 | 15 |
| RAIC | 4.350 | . 045 | 15 | 4.628 | . 037 | 15 |
| MAIC | 3.522 | . 080 | 4 | 3.453 | . 084 | 4 |
| $\pi(x)$ quadratic |  |  |  |  |  |  |
| SAIC | 2.105 | . 260 | 15 | 2.267 | . 223 | 15 |
| RAIC | 4.045 | . 055 | 15 | 4.315 | . 046 | 15 |
| MAIC | 3.405 | . 087 | 4 | 3.340 | . 091 | 4 |
| GEE2 (Bahadur) Model |  |  |  |  |  |  |
| $\pi(x)$ linear |  |  |  |  |  |  |
| SAIC | 2.293 | . 218 | 15 | 2.578 | . 169 | 15 |
| RAIC | 4.632 | . 037 | 15 | 4.848 | 032 | 15 |
| $\pi(x)$ quadratic |  |  |  |  |  |  |
| SAIC | 2.308 | . 214 | 15 | 2.484 | . 183 | 15 |
| RAIC | 4.381 | . 044 | 15 | 4.376 | . 044 | 15 |


## 6. CONCLUSIONS AND FURTHER RESEARCH

We have proposed a very general means of testing the fit of a parametric function. This method is an extension of the order selection test of Eubank and Hart (1992) and requires specification of a likelihood function or estimating equation that depends on the unknown function of interest and a finite number of nuisance parameters. Alternatives to the null hypothesis are modeled by a sequence of nested orthogonal series or some other appropriate function approximators. The parametric model is rejected if a model selection criterion prefers an alternative to it.

An attractive feature of the proposed tests is their generality. They can be used with discrete or continuous data and can accommodate dependence among observations. The null distribution of statistics based on Gaussian likelihoods is often insensitive to the true probability model. Furthermore, robust versions of the test are proposed that retain their (asymptotic) validity even when the specified likelihood is non-Gaussian and incorrect.

Our simulation study supports the conclusion that test validity is generally well maintained by use of an asymptotic distribution. It also shows that our proposed tests can compare favorably with a "good" parametric test in terms of power. Nonetheless, our simulations are of necessity limited, and much more research is needed to better understand the methods.

In the multivariate case, where the covariates belong to a subset of $\mathbb{R}^{d}(d>1)$, there are many ways to choose a sequence of nested models. Not all of these ways will lead to consistent tests of the null hypothesis. We can get an idea of the problems involved by considering the case $d=2$. Let $\Lambda_{1} \subset \Lambda_{2} \subset \cdots$ be a sequence of subsets of $\{(r, s): r \geq 1, s \geq 1\}$, let $\mathcal{L}_{0}$ be the maximized loglikelihood under $H_{0}$, and let $\mathcal{L}_{\Lambda_{j}}$ be the maximized loglikelihood for an alternative model with coefficients $\theta_{r s}$ such that $(r, s) \in \Lambda_{j}$. Consider test statistics of the form $\max _{1 \leq j \leq m_{n}}\left\{2\left(\mathcal{L}_{\Lambda_{j}}-\mathcal{L}_{0}\right) / N\left(\Lambda_{j}\right)\right\}$, where $m_{n} \rightarrow \infty$ and $N\left(\Lambda_{j}\right)$ is the number of elements in $\Lambda_{j}$. For such a test to be consistent against all smooth alternatives, each ( $r, s$ ) must be an element of $\Lambda_{j}$ for $j$ sufficiently large. At the same time, for the distribution theory of Section 2 to be relevant, we need $N\left(\Lambda_{j+1}\right)-N\left(\Lambda_{j}\right)=1$ for $j=1,2, \ldots$. Although it is easy to define a sequence of sets that satisfies these two conditions, there is apparently no "natural" way to do so; the order in which new coefficients enter is arbitrary, and the power properties of the test will depend on the ordering used. To obtain consistency and a less arbitrary choice of nested models, all $N\left(\Lambda_{j+1}\right)-N\left(\Lambda_{j}\right)$ must not be 1. This means that the distribution theory of Section 2 is no longer correct. This is a topic of current research and has been addressed by Aerts, Claeskens, and Hart (1998).

A number of other interesting questions have arisen during the course of our research. The distribution theory in this article assumes the null hypothesis is parametric and that the number of nuisance parameters is finite. There are important settings where at least one of these assumptions is not true. It is sometimes of interest to test whether a regression curve is additive in certain variables without spec-
ifying parametric models for the additive components. An infinite number of nuisance parameters can arise in cases where the likelihood depends on, say, two functions $\gamma_{1}$ and $\gamma_{2}$. One may wish to test whether $\gamma_{1}$ lies in a parametric family without assuming any sort of parametric model for the function $\gamma_{2}$. Can the methodology in this article be extended to allow for such cases?

Another interesting question concerns the correct specification of the model. It would be worthwhile to develop general methods for testing whether the likelihood itself has been correctly specified.
[Received March 1998. Revised March 1999.]

## REFERENCES

Aerts, M., and Claeskens, G. (1997), "Local Polynomial Estimation in Multiparameter Likelihood Models," Journal of the American Statistical Association, 92, 1536-1545.
Aerts, M., Claeskens, G., and Hart, J. D. (1998), "Testing Lack of Fit in Multiple Regression," technical report, Limburgs Universitair Centrum, Diepenbeek, Belgium.
Akaike, H. (1974), "A New Look at Statistical Model Identification," IEEE Transactions on Automatic Control, 19, 716-723.
Bahadur, R. R. (1961), "A Representation of the Joint Distribution of Responses of $n$ Dichotomous Items," in Studies in Item Analysis and Prediction, ed. H. Solomon, Stanford, CA: Stanford University Press.
Boos, D. D. (1992), "On Generalized Score Tests," The American Statistician, 46, 327-333.
Diggle, P. J., Liang, K-Y., and Zeger, S. L. (1994), Analysis of Longitudinal Data, Oxford, U.K.: Oxford University Press.
Efromovich, S. (1996), "On Nonparametric Regression for iid Observations in a General Setting," The Annals of Statistics, 24, 1126-1144.
Efron, B., and Hinkley, D. V. (1978), "Assessing the Accuracy of the Maximum Likelihood Estimator: Observed Versus Expected Fisher Information," Biometrika, 65, 457-487.
Engle, R. R. (1984), "Wald, Likelihood Ratio and Lagrange Multiplier Tests in Econometrics," in Handbook of Econometrics, Vol. II, eds. Z. Griliches and M. Intriligator, Amsterdam: North-Holland.
Eubank, R. L., and Hart, J. D. (1992), "Testing Goodness of Fit in Regression via Order Selection Criteria," The Annals of Statistics, 20, 14121425.

Eubank, R. L., Hart, J. D., and LaRiccia, V. N. (1993), "Testing Goodness of Fit via Nonparametric Function Estimation Techniques," Communications in Statistics, Part A-Theory and Methods, 22, 3327-3354.
Gourieroux, C., Montfort, A., and Trognon, A. (1984), "Pseudo-Maximum Likelihood Methods: Theory," Econometrica, 52, 681-700.
Hart, J. D. (1997), Nonparametric Smoothing and Lack-of-Fit Tests, New York: Springer-Verlag.
Huber, P. J. (1981), Robust Statistics, New York: Wiley.
Kallenberg, W. C. M., and Ledwina, T. (1997), "Data-Driven Smooth Tests When the Hypothesis is Composite," Journal of the American Statistical Association, 92, 1094-1104.
Kent, J. T. (1982), "Robust Properties of Likelihood Ratio Tests," Biometrika, 69, 19-27.
Klein, R., Klein, B. E. K., Moss, S. E., Davis, M. D., and DeMets, D. L. (1984), "The Wisconsin Epidemiologic Study of Diabetic Retinopathy: II. Prevalence and Risk of Diabetic Retinopathy When Age at Diagnosis is Less Than 30 Years," Archives of Ophthalmology, 102, 520-526.
Liang, K-Y., and Zeger, S. L. (1986), "Longitudinal Data Analysis Using Generalized Linear Models," Biometrika, 73, 13-22.
Liaw, A. (1997), "An Application of Fourier Series Smoothing to a Diagnostic Test of Heteroscedasticity," Ph.D. dissertation, Texas A\&M University, Dept. of Statistics.
Mallows, C. L. (1973), "Some Comments on $C_{p}$," Technometrics, 15, 661675.

McCullagh, P., and Nelder, J. A. (1989), Generalized Linear Models (2nd ed.), London: Chapman and Hall.
Newton, H. J. (1988), Timeslab: A Time Series Analysis Laboratory, Belmont, CA: Wadsworth \& Brooks-Cole.
Phillips, P. C. B., and Park, J. Y. (1988), "On the Formulation of Wald

Tests of Nonlinear Restrictions," Econometrica, 56, 1065-1083.
Rao, C. R. (1973), Linear Statistical Inference and Its Applications, New York: Wiley.
Skellam, J. G. (1948), "A Probability Distribution Derived From the Binomial Distribution by the Probability of Success as Variable Between the Sets of Trials," Journal of the Royal Statistical Society, Ser. B, 10, 257-261.
Smith, D. M. (1997), "Oswald: Object-Oriented Software for the Analysis of Longitudinal Data in S," World Wide Web page http://www.maths.lancs.ac.uk/Software/Oswald/.
Staniswalis, J., and Severini, T. (1991), "Diagnostics for Assessing Regression Models," Journal of the American Statistical Association, 86, 684-692.
Staniswalis, J. G., Severini, T., and Moschopoulos, P. G. (1993), "On a

Data Based Power Transformation for Reducing Skewness With Application to Goodness-of-Fit Testing," Journal of Statistical Computation and Simulation, 46, 91-100.
Wedderburn, R. W. M. (1974), "Quasi-Likelihood Functions, Generalized Linear Models, and the Gauss-Newton Method," Biometrika, 61, 439447.

White, H. (1994), Estimation, Inference and Specification Analysis, New York: Cambridge University Press.
Woodroofe, M. (1982), "On Model Selection and the Arc-Sine Laws," The Annals of Statistics, 10, 1182-1194.
Zeger, S., and Liang, K-Y. (1986), "Longitudinal Data Analysis for Discrete and Continuous Outcomes," Biometrics, 42, 121-130.
Zhao, L. P., and Prentice, R. L. (1990), "Correlated Binary Regression Using a Quadratic Exponential Model," Biometrika, 77, 642-648.


[^0]:    Marc Aerts is Associate Professor and Gerda Claeskens is Research Assistant of the Fund for Scientific Research-Flanders, Belgium (FWO), both at Center for Statistics, Limburgs Universitair Centrum (LUC), Universitaire Campus, B3590 Diepenbeek, Belgium (E-mail: marc.aerts@ luc.ac.be). Jeffrey D. Hart is Professor, Department of Statistics, Texas A\&M University, College Station, TX 77843. Hart's research was conducted while visiting Limburgs Universitair Centrum (LUC) and was supported by LUC grant BOF96K03. He is most grateful to the LUC for their generous support during his visit. The authors thank R. Klein of the University of Wisconsin, Madison, for kindly providing the data used in the example (National Institutes of Health grant EY 03083), and gratefully acknowledge the comments and suggestions of an associate editor and two referees.

[^1]:    1999 American Statistical Association
    Journal of the American Statistical Association September 1999, Vol. 94, No. 447, Theory and Methods

