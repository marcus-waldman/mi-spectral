---
citekey: efronAssessingAccuracyMaximum1978
item_type: article
authors: 'Efron, Bradley and Hinkley, David V.'
year: 1978
title: 'Assessing the Accuracy of the Maximum Likelihood Estimator: {Observed} versus Expected {Fisher} Information'
venue: Biometrika
volume: 65
issue: 3
pages: 457--483
doi: 10.1093/biomet/65.3.457
eprint: 'https://academic.oup.com/biomet/article-pdf/65/3/457/636067/65-3-457.pdf'
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\efronAssessingAccuracyMaximum1978.pdf'
pdf_sha256: c46336119a4041fc7d9497da17e6b3f6343767fe7e250075f37f58b8b8db24c0
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-31T18:19:00Z
---
## Biometrika Trust

Assessing the Accuracy of the Maximum Likelihood Estimator: Observed Versus Expected Fisher Information
Author(s): Bradley Efron and David V. Hinkley
Source: Biometrika, Vol. 65, No. 3 (Dec., 1978), pp. 457-482
Published by: Oxford University Press on behalf of Biometrika Trust
Stable URL: https://www.jstor.org/stable/2335893
Accessed: 31-05-2026 16:31 UTC

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about TSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms \& Conditions of Use, available at https://about.jstor.org/terms

# Assessing the accuracy of the maximum likelihood estimator: Observed versus expected Fisher information 

By BRADLEY EFRON<br>Department of Statistics, Stanford University, California<br>and DAVID V. HINKLEY<br>School of Statistics, University of Minnesota, Minneapolis


#### Abstract

Summary This paper concerns normal approximations to the distribution of the maximum likelihood estimator in one-parameter families. The traditional variance approximation is $1 / \mathscr{I}_{\hat{\theta}}$, where $\hat{\theta}$ is the maximum likelihood estimator and $\mathscr{I}_{\theta}$ is the expected total Fisher information. Many writers, including R. A. Fisher, have argued in favour of the variance estimate $1 / I(x)$, where $I(x)$ is the observed information, i.e. minus the second derivative of the log likelihood function at $\hat{\theta}$ given data $x$. We give a frequentist justification for preferring $1 / I(x)$ to $1 / \mathscr{I}_{\hat{\theta}}$. The former is shown to approximate the conditional variance of $\hat{\theta}$ given an appropriate ancillary statistic which to a first approximation is $I(x)$. The theory may be seen to flow naturally from Fisher's pioneering papers on likelihood estimation. A large number of examples are used to supplement a small amount of theory. Our evidence indicates preference for the likelihood ratio method of obtaining confidence limits.


Some key words : Ancillary; Asymptotics; Cauchy distribution; Conditional inference; Confidence limits; Curved exponential family; Fisher information; Likelihood ratio; Location parameter; Statistical curvature.

## 1. Introduction

In 1934, Sir Ronald Fisher's work on likelihood reached its peak. He had earlier advocated the maximum likelihood estimator as a statistic with least large sample information loss, and had computed the approximate loss. Now, in 1934, Fisher showed that in certain special cases, namely the location and scale models, all of the information in the sample is recoverable by using an appropriately conditioned sampling distribution for the maximum likelihood estimator. This marks the beginning of exact conditional inference based on exact ancillary statistics, although the notion of ancillary statistics had appeared in Fisher's 1925 paper on statistical estimation.

Beyond the explicit details of exact conditional distributions for special cases, the 1934 paper contains on p. 300 the following intriguing claim about the general case
When these [log likelihood] functions are differentiable successive portions of the [information] loss may be recovered by using as ancillary statistics, in addition to the maximum likelihood estimate, the second and higher differential coefficients at the maximum.
To this may be coupled an earlier statement (Fisher, 1925, p. 724)
The function of the ancillary statistic is analogous to providing a true, in place of an approximate, weight for the value of the estimate.

There are no direct calculations by Fisher to clarify the above remarks, other than calculations of information loss. But one may infer that approximate conditional inference based on the maximum likelihood estimate is claimed to be possible using observed properties
of the likelihood function. To be specific, if we take for granted that inference is accomplished by attaching a standard error to the maximum likelihood estimate, then Fisher's remarks suggest that we use a conditional variance approximation based on the observed second derivative of the log likelihood function, as opposed to the usual unconditional variance approximation, the reciprocal of the Fisher information. Our main topics in this paper are (i) the appropriateness and easy calculation of such a conditional variance approximation and (ii) the ramifications of this for statistical inference in the single parameter case.

We begin with a simple illustrative example borrowed from Cox (1958). An experiment is conducted to measure a constant $\theta$. Independent unbiased measurements $y$ of $\theta$ can be made with either of two instruments, both of which measure with normal error: instrument $k$ produces independent errors with a $N\left(0, \sigma_{k}^{2}\right)$ distribution ( $k=0,1$ ), where $\sigma_{0}^{2}$ and $\sigma_{1}^{2}$ are known and unequal. When a measurement $y$ is obtained, a record is also kept of the instrument used, so that after a series of $n$ measurements the experimental results are of the form $\left(a_{1}, y_{1}\right), \ldots,\left(a_{n}, y_{n}\right)$, where $a_{j}=k$ if $y_{j}$ is obtained using instrument $k$. The choice between instruments for the $j$ th measurement is made at random by the toss of a fair coin,

$$
\operatorname{pr}\left(a_{j}=0\right)=\operatorname{pr}\left(a_{j}=1\right)=\frac{1}{2}
$$

Throughout this paper, $x$ will denote the entire set of experimental results available to the statistician, in this case $\left(a_{1}, y_{1}\right), \ldots,\left(a_{n}, y_{n}\right)$.

The log likelihood function $l_{\theta}(x), l_{\theta}$ for short, is the log of the density function, thought of as a function of $\theta$. In this example

$$
l_{\theta}(x)=\text { const }-\sum_{j=1}^{n} \log \sigma_{a_{j}}-\frac{1}{2} \sum_{j=1}^{n}\left(y_{j}-\theta\right)^{2} / \sigma_{a_{j}}^{2}
$$

from which we obtain the maximum likelihood estimator as the weighted mean

$$
\hat{\theta}=\left(\Sigma y_{j} / \sigma_{a_{j}}^{2}\right)\left(\Sigma 1 / \sigma_{a_{j}}^{2}\right)^{-1}
$$

If we denote first and second derivatives of $l_{\theta}(x)$ with respect to $\theta$ by $l_{\theta}(x)$ and $\ddot{l}_{\theta}(x), i_{\theta}$ and $\ddot{l}_{\theta}$ for short, then the total Fisher information for this experiment is

$$
\mathscr{I}_{\theta}=\operatorname{var}\left\{i_{\theta}(x)\right\}=E\left\{-\ddot{l}_{\theta}(x)\right\}=\frac{1}{2} n\left(1 / \sigma_{0}^{2}+1 / \sigma_{1}^{2}\right)
$$

Standard theory shows that $\hat{\theta}$ is asymptotically normally distributed with mean $\theta$ and variance

$$
\operatorname{var}(\hat{\theta}) \bumpeq 1 / \mathscr{I}_{\theta} .
$$

In this particular example $\mathscr{I}_{\theta}$ does not depend on $\theta$, so that the variance approximation $(1 \cdot 2)$ is known. If this were not so we would use one of the two approximations (Cox \& Hinkley, 1974, p. 302)

$$
1 / \mathscr{I}_{\hat{\theta}}, \quad 1 / I(x)
$$

where

$$
I(x)=-\ddot{l}_{\hat{\theta}}=\left[-\frac{\partial^{2} l_{\theta}(x)}{\partial \theta^{2}}\right]_{\theta=\hat{\theta}(x)}
$$

The quantity $I(x)$ is aptly called the observed Fisher information by some writers, as distinguished from $\mathscr{I}_{\theta}$, the expected Fisher information. This last name is useful even though $E\left(\mathscr{J}_{\theta}\right) \neq \mathscr{I}_{\theta}$ in general. In the example above

$$
I(x)=a / \sigma_{1}^{2}+(n-a) / \sigma_{0}^{2}
$$

where $a=\Sigma a_{j}$, the number of times instrument 1 was used.

Approximation (1•2), one over the expected Fisher information, would presumably never be applied in practice, because after the experiment is carried out it is known that instrument 1 was used $a$ times and that instrument 0 was used $n-a$ times. With the ancillary statistic $a$ fixed at its observed value, $\hat{\theta}$ is normally distributed with mean $\theta$ and variance

$$
\operatorname{var}(\hat{\theta} \mid a)=\left\{a / \sigma_{1}^{2}+(n-a) / \sigma_{0}^{2}\right\}^{-1}
$$

not (1.2). But now notice that, whereas (1.2) involves an average property of the likelihood, the conditional variance $(1 \cdot 4)$ is a corresponding property of the observed likelihood: $(1 \cdot 4)$ is equal to the reciprocal of the observed Fisher information $I(x)$.

It is clear here that the conditional variance $\operatorname{var}(\hat{\theta} \mid a)$ is more meaningful than $\operatorname{var}(\hat{\theta})$ in assessing the precision of the calculated value $\hat{\theta}$ as an estimator of $\theta$, and that the two variances may be quite different in extreme situations.

This example is misleadingly neat in that $\operatorname{var}(\hat{\theta} \mid a)$ exactly equals $1 / I(x)$. Nevertheless, a version of this relationship applies, as an approximation, to general one parameter estimation problems. A central topic of this paper is the accuracy of the approximation

$$
\operatorname{var}(\hat{\theta} \mid a) \bumpeq 1 / I(x),
$$

where $a$ is an ancillary or approximately ancillary statistic which affects the precision of $\hat{\theta}$ as an estimator of $\theta$. To a first approximation, $a$ will be equivalent to $I(x)$ itself. It is exactly so in Cox's example. The approximation ( $1 \cdot 5$ ) was suggested, never too explicitly, by Fisher in his fundamental papers on ancillarity and estimation. In complicated situations, such as that considered by Cox (1958), it is a good deal easier to compute $I(x)$ than $\mathscr{I}_{\theta}$. There are also philosophical advantages to ( 1.5 ). It is 'closer to the data' than $1 / \mathscr{I}_{\theta}$, and tends to agree more closely with Bayesian and fiducial analyses. In Cox's example of the two measuring instruments, for instance, an improper uniform prior for $\theta$ on $(-\infty, \infty)$ gives var $(\theta \mid x)=1!I(x)$, in agreement with ( $1 \cdot 5$ ).

To demonstrate that ( $1 \cdot 5$ ) has validity in more realistic contexts, consider the estimation of the centre $\theta$ of a standard Cauchy translation family. For random samples of size $n$ the Fisher information is $\mathscr{I}_{\theta}=\frac{1}{2} n$. When $n=20$, then $\hat{\theta}$ has approximate variance $0 \cdot 1$, in accordance with (1.2); the exact variance is about 0.115 according to Efron (1975, p. 1210). In a Monte Carlo experiment 14,048 Cauchy samples of size 20 , with $\theta=0$, were obtained, and Fig. 1 plots the resulting estimated conditional variances of $\hat{\theta}$ given $I(x)$ versus $1 / I(x)$. Samples were grouped according to interval values of $1 / I(x)$. For example, 224 of the 14,048 samples had $1 / I(x)$ in the range $0 \cdot 170-0 \cdot 180$, averaging $0 \cdot 175$, and the 224 values of $\hat{\theta}^{2}$ had mean 0.201 and standard error 0.023 . This gives the estimate

$$
\operatorname{var}\{\hat{\theta} \mid 1 / I(x)=0.175\}=0.201 \pm 0.023
$$

plotted in Fig. 1, since we know $E\{\hat{\theta} \mid I(x)\}=0$ by symmetry.
Figure 1 strongly suggests the relationship

$$
\operatorname{var}\{\hat{\theta} \mid I(x)\} \bumpeq 1 / I(x) .
$$

This is a weakened version of (1•5). In translation families $I(x)$ is ancillary, but it is only a function of the maximal ancillary $a$, the configuration statistic, i.e. the $n-1$ spacings between the ordered values $x_{(1)}<\ldots<x_{(n)}$. The stronger statement ( $1 \cdot 5$ ) is verified for translation families in §§ 2 and 8 . We prefer ( $1 \cdot 5$ ) to ( $1 \cdot 6$ ) because $\operatorname{var}(\hat{\theta} \mid a)$ is more relevant than $\operatorname{var}\{\hat{\theta} \mid I(x)\}$ as a measure of precision for $\hat{\theta}$; in principle (Fisher, 1934) inference about $\theta$ is conditional on $a$.

The implications of $(1 \cdot 5)$ are considerable. If $I(x)=15$ in the Cauchy example, a not very remarkable event since $\operatorname{pr}\{I(x)>15\} \bumpeq 0 \cdot 05$, then the approximate $95 \%$ confidence interval for $\theta$ is

$$
\hat{\theta} \pm 1 \cdot 96 / \sqrt{ } 15,
$$

rather than

$$
\hat{\theta} \pm 1 \cdot 96 / \sqrt{ } 10
$$

as suggested by (1.2). The latter interval is too wide, having conditional coverage probability of $98 \%$ rather than the normal $95 \%$. Given the equally unremarkable event $I(x)=6$, interval (1.8) is too narrow, having conditional coverage probability of only $87 \%$. These numerical comparisons presuppose accuracy of normal approximations, which is justified in §4.

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-05.jpg?height=1142&width=1065&top_left_y=699&top_left_x=288)
Fig. 1. Cauchy location $\theta$. Monte Carlo estimates of conditional variance of maximum likelihood estimate $\hat{\theta}$ given the observed information $I(x)$. Sample size $n=20 ; 14,048$ samples.

The purpose of this paper is to justify ( $1 \cdot 5$ ) for a wide variety of one-parameter problems. The justification consists of detailed numerical results for several special examples involving moderate sample sizes, in addition to the general asymptotic theory. The results are presented in the following order: § 2 gives an outline of the theory for translation families; § 3 contains two detailed examples of this theory; §4 deals with confidence interval interpretations for the results of §2; §5 outlines the more complicated theory appropriate for nontranslation problems; § 6 follows with an example; §§ 7 and 8 present details of the asymptotic theory; § 9 contains brief concluding remarks, together with some further references and historical notes.

## 2. Translation families

## $2 \cdot 1$. Conditional variance approximations

The theory of ancillarity and conditional inference for translation families was developed by Fisher (1934). Here we will use Fisher's theory to justify (1.5), and its higher order corrections, in translation families. Section 4 contains the analogous results for approximate normal confidence limits based on ( $1 \cdot 5$ ). In § 5 the general one-parameter problem is reduced to approximate translation form by a transformation argument. The treatment in this section is presented in outline form, more careful calculations being reserved for §8.

Suppose then that $x_{1}, \ldots, x_{n}$ are independent and identically distributed with density $f_{\theta}\left(x_{1}\right)=f_{0}\left(x_{1}-\theta\right)$. The data vector $x$ can be reduced to the sufficient statistic ( $\hat{\theta}, a$ ), where $\hat{\theta}(x)$ is the maximum likelihood estimator and $a(x)$ is the ancillary configuration statistic, representable as the spacings between successive order statistics, $x_{(2)}-x_{(1)}, \ldots, x_{(n)}-x_{(n-1)}$.

Because $a$ is ancillary, its density $g(a)$ does not depend on $\theta$. The conditional density, with respect to Lebesgue measure, of $\hat{\theta}$ given $a$ is of the translation form

$$
f_{\theta}(\hat{\theta} \mid a)=h_{a}(\hat{\theta}-\theta) .
$$

The Jacobian of the transformation from the ordered $x_{i}$ values to $(\hat{\theta}, a)$ is a constant not depending on $x$, which implies that the density of $x$ can be written

$$
f_{\theta}(x)=c g(a) h_{a}(\hat{\theta}-\theta)
$$

for some constant $c$.
The likelihood function $\operatorname{lik}_{x}(\theta)$ is $f_{\theta}(x)$ thought of as a function of $\theta$, with $x$ fixed at its observed value. Fisher's (1934) main result relates $f_{\theta}(\hat{\theta} \mid a)=h_{a}(\hat{\theta}-\theta)$ to $\operatorname{lik}_{x}(\theta)$ : for any value of $t=\hat{\theta}(x)-\theta$,

$$
\frac{h_{a}(t)}{h_{a}(0)}=\frac{\operatorname{lik}_{x}\{\hat{\theta}(x)-t\}}{\operatorname{lik}_{x}\{\hat{\theta}(x)\}}
$$

This result, which is derived immediately from (2.2), looks simple but is in fact a powerful computational tool. Given the data vector $x$, it is computationally easy to plot the shape of the likelihood function $\operatorname{lik}_{x}(\theta)$. Reflection of this curve about its maximum point $\hat{\theta}(x)$ then gives the conditional sampling density $f_{\theta}(\hat{\theta} \mid a)$, which might otherwise be thought difficult to compute. The word 'shape' is necessary here since $(2 \cdot 3)$ determines $h_{a}(t)$ only relative to its maximum $h_{a}(0)$. Integration is necessary to determine the correct multiple, that which integrates to one. Fisher's tour de force was completed by noting that fully informative frequentist inferences about $\theta$ should certainly be made conditional on the ancillary $a$, so that the likelihood theory leads easily and naturally to the appropriate frequentist theory.

To see how ( $2 \cdot 3$ ) applies to the phenomenon pictured in Fig. 1 suppose, for the moment, that $\operatorname{lik}_{x}(\theta)$ happens to be perfectly normal shaped; that is,

$$
\frac{\operatorname{lik}_{x}(\theta)}{\operatorname{lik}_{x}\{\hat{\theta}(x)\}}=\exp \left[-\frac{1}{2} c_{2}\{\theta-\hat{\theta}(x)\}^{2}\right]
$$

for some positive constant $c_{2}$. Then (2•4) and (2•3) quickly give

$$
f_{\theta}(\hat{\theta} \mid a)=h_{u}(\hat{\theta}-\theta)=\left(2 \pi / c_{2}\right)^{-\frac{1}{2}} \exp \left\{-\frac{1}{2} c_{2}(\hat{\theta}-\theta)^{2}\right\} .
$$

In other words, a normal-shaped likelihood function implies that, conditional on $a, \hat{\theta}$ is normally distributed with mean $\theta$ and variance

$$
\operatorname{var}(\hat{\theta} \mid a)=1 / c_{2} .
$$

In the notation of § 1 , where $l_{\theta}(x)$ is the $\log$ likelihood function $\log \operatorname{lik}_{x}(\theta)$, and dots indicate differentiation with respect to $\theta$, (2.4) gives $c_{2}=-l_{\theta}=I(x)$, so that (2.5) is an exact form of ( $1 \cdot 5$ ),

$$
\operatorname{var}(\hat{\theta} \mid a)=1 / I(x) .
$$

What if the likelihood function is not perfectly normal shaped? As $n$ gets large the likelihood will approach normality, assuming some mild regularity conditions on the form of $f_{\theta}(x)$, and we can use this fact to obtain asymptotic expansions for the conditional mean and variance of $\hat{\theta}$ given $a$. These expansions involve the higher derivatives of the log likelihood function, say for $j=3,4, \ldots$

$$
l_{\theta}^{(\cdot j)}=\left[\frac{\partial^{j} l_{\theta}(x)}{\partial \theta^{j}}\right]_{\theta=\theta(x)}
$$

all of which are zero in the normal case (2.4). We also use the notation $l_{\theta}^{(\cdot 2)}=l_{\theta}$ where convenient. Notice that ( $2 \cdot 2$ ) implies

$$
l_{\hat{\theta}}^{(\cdot j)}=\left[\frac{\partial^{j} \log h_{a}(\hat{\theta}-\theta)}{\partial \theta^{j}}\right]_{\theta=\theta}=(-1)^{j}\left[\frac{\partial^{j} \log h_{a}(t)}{\partial t^{j}}\right]_{t=0},
$$

which says that the $l_{\dot{\theta}}^{(\cdot j)}$ are functions of $x$ only through $a$ and are themselves ancillary statistics. This same statement applies to the observed Fisher information $I(x)=-\ddot{l}_{\theta}$.

Lemma 1. In translation families satisfying the regularity conditions stated in §8,

$$
\begin{gathered}
\operatorname{var}(\hat{\theta} \mid a)=I^{-1}\left\{1+\left(J^{2} / I^{3}-\frac{1}{2} K / I^{2}\right)+o_{p}\left(n^{-1}\right)\right\}, \quad E(\hat{\theta} \mid a)=\theta-\frac{1}{2} J / I^{2}+o_{p}\left(n^{-1}\right), \\
E\left\{(\hat{\theta}-\theta)^{2} \mid a\right\}=\frac{1}{I}\left\{1+\left(\frac{5}{4} \frac{J^{2}}{I^{3}}-\frac{1}{2} \frac{K}{I^{2}}\right)+o_{p}\left(n^{-1}\right)\right\},
\end{gathered}
$$

where

$$
I=I(x)=-l_{\theta}(x), \quad J=l_{\theta}^{(\cdot 3)}(x), \quad K=-l_{\theta}^{(\cdot 4)}(x) .
$$

The proof of Lemma 1, which is an elaboration of the argument leading from a normalshaped likelihood to ( $2 \cdot 6$ ), is given in §8, along with appropriate regularity conditions.

The terms in round brackets in (2.7)-(2.8) are of order $O_{p}\left(n^{-1}\right)$ or smaller. In particular $\operatorname{var}(\hat{\theta} \mid a)$ in (2•7) can be written

$$
\operatorname{var}(\hat{\theta} \mid a)=I^{-1}\left\{1+O_{p}\left(n^{-1}\right)\right\},
$$

which verifies ( $1 \cdot 5$ ). Lemma 2 , in § $2 \cdot 2$, provides the final justification for ( $1 \cdot 5$ ) being an improvement over $1 / \mathscr{I}_{\theta}$. The approximate normality of the likelihood function, which is used to prove Lemma 1, also ensures that the conditional distribution of $\hat{\theta}$ is approximately normal, given Fisher's result ( $2 \cdot 3$ ). Results directly related to conditional confidence intervals for $\theta$ are described in §4.

In special cases the higher order terms in the left-hand side of ( $2 \cdot 7$ ) can be evaluated, giving expressions for $\operatorname{var}(\hat{\theta} \mid a)$ more accurate than $(1 \cdot 5)$. This is demonstrated by the two examples of §3 and the brief discussion of the Cauchy translation problem in §8.

Even though the maximal ancillary $a$ consists of $I(x)$ plus the higher order derivatives $l_{\theta}^{(\cdot j)}(j=3,4, \ldots)$, the conditional variance $\operatorname{var}(\hat{\theta} \mid a)$ is asymptotically equivalent, to within terms of order $n^{-2}$, to a function of just $I(x)$, namely $1 / I(x)$. To put it another way, $I(x)=-\ddot{l}_{\theta}$ recaptures most of the information lost by considering only $\hat{\theta}(x)$ instead of the full sample $x$. Some informal calculations to this effect were carried out by Fisher (1925). Roughly speaking, the pair ( $\hat{\theta}, Z_{\theta}$ ) is the sufficient statistic for the two-parameter exponential family which best approximates the family $f_{\theta}(x)$ near the true value of $\theta$; see § 7 below.

### 2.2. Statistical curvature and comparison of variance approximations

How different, numerically, is the conditional variance approximation $1 / I(x)$ from the unconditional approximation $1 / \mathscr{I}_{\theta}$ ? An asymptotic answer can be given in terms of the statistical curvature $\gamma_{\theta}$, as defined by Efron (1975, §§ 3, 5). Suppose that each $x_{i}$ has density function $f_{\theta}\left(x_{1}\right)$, not necessarily of translation form, and define for $j, k=1,2$ the moments

$$
v_{j k}(\theta)=E\left(\left\{\frac{\partial \log f\left(x_{1}\right)}{\partial \theta}\right\}^{j}\left[\frac{\partial^{2} \log f_{\theta}\left(x_{1}\right)}{\partial \theta^{2}}+E\left\{\frac{\partial \log f_{\theta}\left(x_{1}\right)}{\partial \theta}\right\}^{2}\right]^{k}\right),
$$

assuming these exist. Then the statistical curvature of $f_{\theta}\left(x_{1}\right)$ is

$$
\gamma_{\theta}=\left(\nu_{02} \nu_{20}-\nu_{11}^{2}\right)^{1 / 2} / \nu_{20}^{3 / 2} .
$$

This curvature is a measure of the deviation of $f_{\theta}\left(x_{1}\right)$ from exponential family form and is invariant under monotone reparameterization. One interpretation is that $\gamma_{\theta}^{2} \mathscr{I}_{\theta}^{2}$ is the residual variation in $\ddot{l}_{\theta}$ after linear regression on $\dot{l}_{\theta}$. For one-parameter exponential families $\gamma_{\theta}=0$, and in such families $I(x)=\mathscr{I}_{\theta}$, so that the two variance approximations being considered are equal. The statistical curvature of $l_{\theta}\left(x_{1}, \ldots, x_{n}\right)$ is $\gamma_{\theta} / \sqrt{ } n$.

The relationship between $\gamma_{\theta}$ and the variance approximations is given by the following result.

Lemma 2. If $x_{1}, \ldots, x_{n}$ are independent and identically distributed with density function $f_{\theta}\left(x_{1}\right)$ satisfying the regularity conditions stated in § 8, then as $n \rightarrow \infty$

$$
\sqrt{ } n\left\{I(x) \mid \mathscr{I}_{\theta}-1\right\} \sim N\left(0, \gamma_{\theta}^{2}\right) .
$$

A proof is given in §8. Fisher (1925) indirectly suggests (2.12).
In a translation family $\mathscr{I}_{\theta}=\mathscr{I}$ and $\gamma_{\theta}=\gamma$ are constants, so that (2.12) can then be written as $I(x) \left\lvert\, \mathscr{I}_{\theta}=1+O_{p}\left(n^{-\frac{1}{2}}\right)\right.$. Combined with (2•10), this easily leads to

$$
\frac{\operatorname{var}(\hat{\theta} \mid a)-1 / I(x)}{\operatorname{var}(\hat{\theta} \mid a)-1 / \mathscr{I}}=O_{p}\left(n^{-\frac{1}{2}}\right)
$$

which shows that ( $1 \cdot 5$ ) is a valid and useful asymptotic approximation. Granting that $\operatorname{var}(\hat{\theta} \mid a)$ is a more meaningful measure of variance than $\operatorname{var}(\hat{\theta})$, we see that $1 / I(x)$ is a better variance approximation than $1 / \mathscr{I}$ by a half order of magnitude, in the usual exaggerated sense of asymptotic comparisons. The numerical results for the Cauchy translation problem in § 1 and the two examples in § 3 show that the improvement can be substantial even for moderate sample sizes.

Suppose that we are interested in estimating a monotone function of $\theta$, say $\sigma=\sigma(\theta)$, rather than $\theta$ itself. It is easy to verify that the observed Fisher information for $\sigma$, say $I^{(\sigma)}(x)$, is related to that for $\theta$ by

$$
I^{(\sigma)}(x)=I(x)(d \hat{\theta} / d \hat{\sigma})^{2}
$$

The expected Fisher information transforms in the same way. Since the maximum likelihood estimator maps the same way as does the parameter, $\hat{\sigma}=\sigma(\hat{\theta})$, the notation $d \hat{\theta} / d \hat{\sigma}$ is unambiguous, and equals $[d \theta / d \sigma]_{\sigma=\varnothing}$. A standard expansion argument proceeding from Lemmas 1 and 2 shows that ( $1 \cdot 5$ ) is valid for $\hat{\sigma}$, in the sense of ( $2 \cdot 13$ ), that is

$$
\frac{\operatorname{var}(\hat{\sigma} \mid a)-1 / I^{(\sigma)}(x)}{\operatorname{var}(\hat{\sigma} \mid a)-1 / \mathscr{I}_{\partial}^{(\sigma)}}=O_{p}\left(n^{-\frac{1}{2}}\right)
$$

If we wish to compare confidence intervals for $\hat{\theta}$, conditional versus unconditional as at (1.7) and (1.8), the ratio of the lengths of conditional and unconditional intervals is

$$
\left\{I(x) \mid \mathscr{I}_{\theta}\right\}^{\frac{1}{2}} .
$$

Lemma 2 implies that $\left\{I(x) \mid \mathscr{I}_{\theta}\right\}^{\frac{1}{2}}$ has, asymptotically, a normal distribution with mean 1 and standard deviation $\gamma_{\theta} /(2 \sqrt{ } n)$. For the Cauchy translation family $\gamma_{\theta}^{2}=2 \cdot 5$, so that with $n=20$ the standard deviation of $\left\{I(x) / \mathscr{I}_{\theta}\right\}^{\frac{1}{2}}$ is approximately $0 \cdot 18$. We expect large variability in $\left\{I(x) \mid \mathscr{I}_{\theta}\right\}^{\frac{1}{2}}$ in this situation, which is indeed the case. Increasing $n$ to 80 in the Cauchy problem reduces the standard deviation of $\left\{I(x) \mid \mathscr{I}_{\theta}\right\}^{\frac{1}{1}}$ to 0.09 , so that conditioning effects become considerably less important.

## 3. Examples of translation families

We illustrate the theory of the preceding section using two particularly simple examples of symmetric translation families due to Fisher.

Example 3.1: Fisher's normal circle. The first example is the circle model (Fisher, 1974, p. 138), where the data consist of a two-dimensional normally distributed vector $x$, covariance matrix the identity, whose mean vector is known to lie on a circle of known radius $\rho_{0}$ centred at the origin. That is,

$$
E\left(x^{T}\right)=\rho_{0}(\cos \theta, \sin \theta) .
$$

Having observed $x$, we wish to estimate the unknown $\theta$. Note that given $n$ independent observations $x_{1}, \ldots, x_{n}$ on this model the sufficient statistic $x=\Sigma x_{i} / \sqrt{ } n$ satisfies (3.1) with $\rho_{0} \sqrt{ } n$ in place of $\rho_{0}$.

If the data vector $x$ has polar coordinates $\left(\hat{\theta}, r \rho_{0}\right)$ then $\hat{\theta}$ is the maximum likelihood estimate of $\theta$, and $r=\|x\| / \rho_{0}$ is ancillary. The density is of the form (2.2), with $a$ replaced by $r$, so that we can apply the theory of § 2, even though (3•1) does not look like a standard translation problem. The density $g(r)$ is noncentral chi, while the conditional density

$$
f_{\theta}(\hat{\theta} \mid r)=h_{r}(\hat{\theta}-\theta)
$$

is the 'circular normal',

$$
c^{-1} \exp \left\{\rho_{0}^{2} r \cos (\hat{\theta}-\theta)\right\} .
$$

Here we are assuming that $\hat{\theta}$ given $\theta$ ranges from $\theta-\pi$ to $\theta+\pi$, for the sake of symmetric definition. The constant $c$ equals $2 \pi I_{0}\left(\rho_{0}^{2} r\right)$, in the standard Bessel function notation.

Now we can apply Lemma 1 of §2. From (3.2) we calculate

$$
l_{\ddot{\theta}}^{(\cdot . j)}=(-1)^{\ddagger j} \rho_{0}^{2} r \quad(j=2,4, \ldots)
$$

and $l_{\ddot{\theta}}^{(\cdot j)}=0$ for $j$ odd. The Fisher information $\mathscr{J}_{\theta}$ is constant,

$$
\mathscr{I}_{\theta}=\mathscr{I}=\rho_{0}^{2}
$$

Using $I(x)=-l_{\theta}=r \mathscr{I}, l_{\theta}^{(\cdot 3)}=0, l_{\theta}^{(\cdot 4)}=r \mathscr{I}$, from (3•3) and (3•4), (2•7) can be written

$$
\operatorname{var}(\hat{\theta} \mid r) \bumpeq \frac{1}{r \mathscr{I}}\{1+1 /(2 r \mathscr{I})\} .
$$

The exact conditional variance of $\hat{\theta}$ given the ancillary statistic $r$ is calculated from (3.2) to be

$$
\operatorname{var}(\hat{\theta} \mid r)=\left\{\int_{-\pi}^{\pi} t^{2} \exp (r \mathscr{I} \cos t) d t\right\} /\left\{\int_{-\pi}^{\pi} \exp (r \mathscr{I} \cos t) d t\right\}
$$

Figure 2 compares (3.6) with (3.5). For values of $\rho_{0}^{2}=\mathscr{I} \geqslant 8$ it can be shown that at least $95 \%$ of the realizations of $r \mathscr{I}=I(x)$ will be greater than 4 . We see that approximation ( 1.5 ), $\operatorname{var}(\hat{\theta} \mid r) \bumpeq 1 /(r \mathscr{I})$, is quite acceptable in the range $1 /(r \mathscr{I}) \leqslant 0 \cdot 25$, and that the improved approximation (3.5) derived from Lemma 1 is very accurate.

The exact variance (3.6) can be expressed in terms of Bessel functions, whose expansions lead to $(3 \cdot 5)$.

Example 3.2: Fisher's gamma hyperbola. Fisher's hyperbola model, introduced in connexion with his famous 'problem of the Nile' (Fisher, 1974, p. 169), involves two independent scaled gamma variables whose means are restricted to lie on an hyperbola. Thus we observe $x=\left(x_{1}, x_{2}\right)$ such that $x_{1}=e^{\theta} G_{m 1}$ and $x_{2}=e^{-\theta} G_{m 2}$, where $G_{m i}$ indicates a variable with density $x^{m-1} e^{-x} / \Gamma(m)$ on ( $0, \infty$ ). The Fisher information for $\theta$ is $\mathscr{I}=2 m$. The maximum likelihood estimate of $\theta$ is $\hat{\theta}=\frac{1}{2} \log \left(x_{1} / x_{2}\right)$. This is illustrated in Fig. 3.

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-10.jpg?height=812&width=730&top_left_y=780&top_left_x=102)
Fig. 2 (left). Exact conditional variances, circles, of $\hat{\theta}$ given $r$ compared with approximations $(2 \cdot 7)$, curves, for the circle and hyperbola models. Dotted line, approximation ( $1 \cdot 5$ ).

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-10.jpg?height=669&width=706&top_left_y=892&top_left_x=918)
Fig. 3 (right). Fisher's gamma hyperbola model. $x=\left(x_{1}, x_{2}\right)$, a pair of independent gamma variables with index $m$, whose means lie on solid curve. Broken curve, one orbit hyperbola for ancillary statistic $r$.

The ancillary statistic in the hyperbola model is $r=\sqrt{ }\left(x_{1} x_{2}\right) / m$, the level curves of which are hyperbolae 'parallel' to the curve of possible mean vectors, as shown in Fig. 3. It has density

$$
g(r)=\frac{2 m^{2 m}}{\{\Gamma(m)\}^{2}} r^{2 m-1} \int_{-\infty}^{\infty} \exp \{-2 m r \cosh (t)\} d t
$$

the conditional density of $\hat{\theta}$ given $r$ being

$$
f_{\theta}(\hat{\theta} \mid r)=\exp \{-2 m r \cosh (\hat{\theta}-\theta)\} / \int_{-\infty}^{\infty} \exp \{-2 m r \cosh (t)\} d t
$$

In other words, this is another nonobvious example of form (2.2).

The log likelihood derivatives, from (3•7), are

$$
l_{\theta}^{(\cdot j)}=-2 m r=-r \mathscr{I} \quad(j=2,4, \ldots)
$$

$l_{\partial}^{(\cdot j)}=0$ for $j$ odd, so that $I(x)=r \mathscr{I}$ as in the circle model, and (2•7) gives

$$
\operatorname{var}(\hat{\theta} \mid r) \bumpeq \frac{1}{r \mathscr{I}}\{1-1 /(2 r \mathscr{\mathscr { I }})\} .
$$

This differs only in the sign of the second term from the corresponding formula ( $3 \cdot 5$ ) for the circle model. The actual conditional variance $\operatorname{var}(\hat{\theta} \mid r)$, obtained by integrating (3.7), can also be expressed as a function of $r \mathscr{I}$. The comparison of (3.9) with the actual conditional variance, Fig. 2, is almost exactly the same as for the circle model, except that here the deviations from the line $\operatorname{var}(\hat{\theta} \mid r)=1 / I(x)=1 /(r \mathscr{I})$ go in the opposite direction.

## 4. Conditional confidence intervals for the location parameter

Our results so far have been presented mainly in terms of variances, it being understood that these are of most interest in conjunction with a normal approximation for $\hat{\theta}-\theta$. The expansion theory of § 2 can be expressed directly in terms of conditional confidence intervals, an idea we now pursue explicitly.

As before, consider first the situation where $\operatorname{lik}_{x}(\theta)$ happens to be perfectly normal shaped, so that (2-4) holds with $c_{2}=I(x)$. There are two consequences of this relating to standard confidence interval methods. First, $\hat{\theta}$ has an exact normal distribution conditional on $a$, so that

$$
u(x)=I(x)(\hat{\theta}-\theta)^{2}
$$

is exactly a $\chi_{1}^{2}$ variable conditional on $a$. If the upper $p$ point of $\chi_{1}^{2}$ is denoted $\chi_{1}^{2}(p)$, then level $p$ conditional limits on $\theta$ are $\hat{\theta} \pm\left\{\chi_{1}^{2}(p) / I(x)\right\}^{\frac{1}{2}}$. The other standard method of setting confidence limits is based on

$$
v(x)=2\left\{l_{\theta(x)}(x)-l_{\theta}(x)\right\}
$$

which also has an exact $\chi_{1}^{2}$ distribution conditional on $a$.
Although in general the likelihood function is not exactly normal shaped, it is approximately so for large $n$, and the same expansion methods used to confirm ( $1 \cdot 5$ ) also show that $u(x)$ and $v(x)$ defined above are asymptotically $\chi_{1}^{2}$ conditional on $a$. More formally, we have the following result, proved in §8.

Lemma 3. For translation families satisfying the regularity conditions in §8, the statistics $u(x)$ and $v(x)$ defined by (4•1) and (4•2) satisfy

$$
\begin{aligned}
& \operatorname{pr}\left\{u(x) \geqslant u_{0} \mid a\right\}=\left(1-d_{1}-d_{2}\right) \operatorname{pr}\left(\chi_{1}^{2} \geqslant u_{0}\right)+d_{1} \operatorname{pr}\left(\chi_{5}^{2} \geqslant u_{0}\right)+d_{2} \operatorname{pr}\left(\chi_{7}^{2} \geqslant u_{0}\right)+o_{p}\left(n^{-1}\right), \\
& \operatorname{pr}\left\{v(x) \geqslant u_{0} \mid a\right\}=\left(1-d_{1}-d_{2}\right) \operatorname{pr}\left(\chi_{1}^{2} \geqslant u_{0}\right)+\left(d_{2}+d_{1}\right) \operatorname{pr}\left(\chi_{3}^{2} \geqslant u_{0}\right)+o_{p}\left(n^{-1}\right),
\end{aligned}
$$

where $d_{1}=-K /\left(8 I^{2}\right)$ and $d_{2}=\left(5 J^{2}\right) /\left(24 I^{3}\right)$, with $I, J$ and $K$ as defined in (2.9).
Because $d_{1}$ and $d_{2}$ are both $O_{p}\left(n^{-1}\right)$, (4.3) and (4.4) imply

$$
I(x)(\hat{\theta}-\theta)^{2}\left|a=\chi_{1}^{2}+O_{p}\left(n^{-1}\right), \quad 2\left(l_{\theta}-l_{\theta}\right)\right| a=\chi_{1}^{2}+O_{p}\left(n^{-1}\right)
$$

Note that the latter result is a conditional version of Wilks's famous theorem, and establishes that a standard method has the correct conditional properties.

The results ( $4 \cdot 5$ ) are superior to the unconditional result

$$
\mathscr{I}_{\theta}(\hat{\theta}-\theta)^{2}=\chi_{1}^{2}+O_{p}\left(n^{-1}\right)
$$

in a sense similar to $(2 \cdot 13)$. As we pointed out in § $2 \cdot 2$, the degree of superiority is determined by the curvature.

To investigate the practical validity of $(4 \cdot 5)$, we return to the Cauchy translation problem discussed in § 1 . We have generated 20,000 samples of size $n=20$ and computed the empirical frequencies with which $\mathscr{I}_{\theta}(\hat{\theta}-\theta)^{2}, I(x)(\hat{\theta}-\theta)^{2}$ and $2\left(l_{\theta}-l_{\theta}\right)$ exceeded $\chi_{1}^{2}(p)$ for $p=0.05$ and 0.01 , broken down by interval values of $I(x)$. Figure 4 graphs the results which show convincing evidence in support of (4.5) and dramatic conditional effects on the unconditional statistic (4.6). Note that the likelihood ratio method agrees better numerically with the chi-squared approximation than does the method based on $\hat{\theta}$. The expansions ( $4 \cdot 3$ ) and ( $4 \cdot 4$ ) indicate that this may be true in general, since $\operatorname{pr}\left(\chi_{q}^{2} \geqslant u_{0}\right)$ is an increasing function of $q$.

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-12.jpg?height=1066&width=1581&top_left_y=870&top_left_x=69)
Fig. 4. Monte Carlo estimates of pr (statistic $\geqslant c \mid I$ ) with $c=3.84$, shown by closed circles, and $c=5 \cdot 99$, open circles, for three likelihood statistics in the Cauchy location model, $n=20$. Statistics: $2\left(l_{\hat{\theta}}-l_{\theta}\right)$ shown by solid curve; $I(\hat{\theta}-\theta)^{2}$, dashed curve; $\mathscr{I}(\hat{\theta}-\theta)^{2}$, dotted curve. Estimates from 20,000 samples.

## 5. Nontranslation families

This section discusses an example of a nontranslation problem in which a version of (1.5) can be seen to hold. We will use this example to introduce definitions appropriate for general nontranslation problems. The example is totally artificial, being in fact a simple variant of

Fisher's circle model, but furnishes a useful starting point because of its simplicity. A nontranslation problem of a more realistic nature is discussed in §6, again showing ( $1 \cdot 5$ ) at work.

We have not been able to provide a theoretical justification for these results in general, and pathological counterexamples are easy to construct, but nevertheless the examples suggest that $(1 \cdot 5)$, suitably interpreted, has wide validity.

Figure 5 illustrates a model in which the data vector is bivariate normal, covariance matrix the identity, and with mean vector constrained to lie on a spiral, instead of Fisher's circle; that is

$$
E(x)=\beta_{\theta}=\left[\begin{array}{l}
\cos \theta-\rho_{\theta} \sin \theta \\
\sin \theta+\rho_{\theta} \cos \theta
\end{array}\right], \quad \rho_{\theta}=\rho_{0}-\theta, \quad \theta \leqslant \rho_{0} .
$$

The spiral is generated by the end of a thread unwinding from a circular spool of unit radius. By definition the thread has length $\rho_{0}$ at $\theta=0$, which implies that it has length $\rho_{\theta}=\rho_{0}-\theta$ at $\theta$. At $\theta=+\rho_{0}$, we have $\rho_{\theta}=0$, which accounts for the restriction in (5.1). We wish to assign some measure of accuracy to the maximum likelihood estimate $\hat{\theta}$ on the basis of the observed $x$. The sample size here is $n=1$, but under repeated sampling essentially the same model holds with $x$ replaced by $\bar{x}=\Sigma x_{i} / n$.

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-13.jpg?height=1001&width=939&top_left_y=965&top_left_x=395)
Fig. 5. Spiral model. $x=\left(x_{1}, x_{2}\right)$, bivariate normal with identity covariance matrix and mean $\beta_{\theta}$ on a logarithmic spiral shown by solid curve. Maximum likelihood estimate $\hat{\theta}$ is angular coordinate of straight thread on which $x$ lies. Ancillary statistic has constant value $q$ on parallel spiral through $x$, dashed curve.

It is easy to calculate that the Fisher information and curvature for the spiral model are $\mathscr{I}_{\theta}=\rho_{\theta}^{2}$ and $\gamma_{\theta}=1 / \rho_{\theta}$, and that having observed $x$, the maximum likelihood estimate $\hat{\theta}(x)$ is the angular coordinate of the thread upon which $x$ lies. The vector $\beta_{\theta}$ is the closest point to $x$ on the spiral of possible mean vectors. When $\rho_{\theta}$ is large the curvature is small, and we expect small conditioning effects, the reverse being true when $\rho_{\theta}$ is small.

The geometry of Fig. 5 and familiarity with the bivariate normal distribution suggest that $Q(x)$, the signed distance of $x$ from $\beta_{\theta}$, should be approximately ancillary, with a limiting $N(0,1)$ distribution as $\rho_{\theta}$ gets large. We take the sign of $Q(x)$ positive if $x$ is closer to the spool than $\beta_{\theta}$, and negative if it is farther from the spool. Figure 5 shows that the level curve $Q(x)=q$ is a parallel spiral having thread everywhere $q$ units shorter than that for the mean vector.

We intend to use $Q(x)$ as an approximate ancillary, conditioning upon the observed value of $Q$ as we did upon $a$ in the translation case. Both D. A. Pierce and D. R. Cox suggest this use of $Q$ in the discussion following Efron (1975). Table 1 displays the marginal density of $Q(x)$ for four values of $\theta$ and eight values of $Q=q$. The four $\theta$ values are chosen such that $\rho_{\theta}=\rho_{0}-\theta=\sqrt{ } 8, \sqrt{ } 16, \sqrt{ } 32, \sqrt{ } 64$; it is irrelevant which combinations of $\rho_{0}$ and $\theta$ are used to get these values of $\rho_{\theta}$. The density would be constant across rows if $Q(x)$ were a genuine ancillary. We see that it is nearly constant, tending toward the $N(0,1)$ density as $\rho_{\theta} \rightarrow \infty$.

The marginal densities in Table 1 were obtained by numerical integration of the bivariate normal density along the spiral $Q(x)=q$. To avoid certain problems of definition, for each $\rho_{\theta}$ the integration was restricted to points on this spiral with angular coordinate in the interval $\theta \pm \pi$. Notice that if $\rho_{\theta}-q<\pi$, then the spiral runs into the central spool before the lower limit $\theta-\pi$ is reached. This end effect seriously distorts a few of the more extreme calculations, as indicated in the tables.

$$
\rho_{\theta}=\sqrt{ } 8, \sqrt{ } 16, \sqrt{ } 32, \sqrt{ } 64
$$

Table 1. Exact marginal density of asymptotic ancillary statistic $Q(x)$ at $q$ for
| $Q=q$ | $\rho_{\theta}=\sqrt{ } 8$ | $\rho_{\theta}=\sqrt{ } 16$ | $\rho_{\theta}=\sqrt{ } 32$ | $\rho_{\theta}=\sqrt{ } 64$ | $N(0,1)$ density |
| :--- | :--- | :--- | :--- | :--- | :--- |
| -2 | 0.07 | 0.07 | 0.06 | 0.06 | 0.05 |
| $-1.5$ | 0.16 | 0.15 | $0 \cdot 15$ | 0.14 | 0.13 |
| -1 | 0.29 | 0.27 | 0.26 | 0.26 | 0.24 |
| -0.5 | $0 \cdot 39$ | 0.38 | 0.37 | 0.36 | 0.35 |
| 0 | 0.41 | 0.40 | $0 \cdot 40$ | 0.40 | 0.40 |
| 1 | 0.19 | 0.21 | 0.22 | 0.23 | $0 \cdot 24$ |
| 1.5 | 0.08* | $0 \cdot 10$ | 0.11 | 0.12 | 0.13 |
| 2 | 0.02* | 0.04 | 0.04 | 0.05 | 0.05 |


Last column gives the $N(0,1)$ density, corresponding to the limiting case $\rho_{\theta} \rightarrow \infty$. *: substantial distortion by end effects.

The observed Fisher information $I(x)$ is

$$
I(x)=\left\{1-\gamma_{\theta} Q(x)\right\} \mathscr{I}_{\theta}=\rho_{\theta}\left(\rho_{\theta}-q\right),
$$

where $\hat{\theta}=\hat{\theta}(x)$ and $q=Q(x)$. We will also use the notation $I(q, \hat{\theta})=I(x)$ to emphasize the partition of $x$ into the approximate ancillary $Q(x)=q$ and the estimate $\hat{\theta}$. Rather than directly verifying that $\operatorname{var}(\hat{\theta} \mid q) \sim 1 / I(q, \theta)$, which is in fact true, we will first make a 'variance stabilizing' transformation of parameter, to put the problem in an approximate translation form, where we can expect our approximation theory to work better. Fraser (1964) makes a similar effort using a different technique.

For a fixed value of $q$ consider the transformation $\theta \rightarrow \phi_{q}$ defined by

$$
\frac{d \phi_{q}}{d \theta}=\sqrt{ }|I(q, \theta)|=\sqrt{ }\left\{\rho_{\theta}\left(\rho_{\theta}-q\right)\right\} .
$$

Equation (2-14) shows that

$$
I^{\left(\phi_{\theta}\right)}(x)=I(x) /\left\{\rho_{\theta}\left(\rho_{\theta}-q\right)\right\}
$$

for $Q(x)=q$. In terms of the new parameter $\phi_{q}$, the observed Fisher information is one for every $x$ on the level curve $Q(x)=q$. Since we intend to make conditional statements given $Q(x)=q$, it causes no trouble to use a different transformation for each value of $q$. Relation $(1 \cdot 5)$ then becomes simply $\operatorname{var}\left(\hat{\phi}_{q} \mid q\right) \sim 1$. Notice that if this is true, then transforming back to $\hat{\theta}$ gives

$$
\operatorname{var}(\hat{\theta} \mid q) \sim \operatorname{var}\left(\hat{\phi}_{q} \mid q\right)\left(\frac{d \hat{\theta}}{d \hat{\phi}_{q}}\right)^{2} \sim\left(\frac{d \hat{\theta}}{d \hat{\phi}_{q}}\right)^{2}=\frac{1}{I(x)},
$$

which is ( $1 \cdot 5$ ). There is one more level of approximation in (5.5) than in $\operatorname{var}\left(\hat{\phi}_{q} \mid q\right) \sim 1$ which, to reiterate, is one reason for making the transformation (5.3).

Table 2 shows that the quantity $\hat{\phi}_{q}-\phi_{q}$ does indeed have nearly the right mean and variance, 0 and 1 respectively, for the cases considered. The worst case is $q=0, \rho_{\theta}=\sqrt{ } 8$, for which the variance is $1 \cdot 10$. The case $q=2$ with $\rho_{\theta}=\sqrt{ } 8$ looks terrible, but that is due to the end effect previously mentioned.

Table 2. Mean and variance of $\hat{\phi}_{q}-\phi_{q}$ for $\rho_{\theta}=\sqrt{ } 8, \sqrt{ } 16, \sqrt{ } 32, \sqrt{ } 64$.
| $q$ | $\rho_{\theta}=\sqrt{ } 8$ |  | $\rho_{\theta}=\sqrt{ } 16$ |  | $\rho_{\theta}=\sqrt{ } 32$ |  | $\rho_{\theta}=\sqrt{ } 64$ |  |
| ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| -2 | -0.02 | 1.04 | -0.01 | 1.02 | -0.00 | 1.01 | -0.00 | 1.01 |
| -1 | -0.02 | 1.06 | -0.01 | 1.03 | -0.00 | 1.01 | -0.00 | 1.01 |
| 0 | -0.02 | 1.10 | -0.01 | 1.04 | -0.00 | 1.02 | -0.00 | 1.01 |
| 1 | $0.05^{*}$ | $0.99^{*}$ | -0.01 | 1.05 | -0.00 | 1.02 | -0.00 | 1.01 |
| 2 | $0.49^{*}$ | $0.58^{*}$ | -0.00 | 1.06 | -0.00 | 1.03 | -0.00 | 1.01 |


*: substantial distortion by end effects.
Other moments of $\hat{\phi}_{q}-\phi_{q}$ were calculated, all of which indicated good agreement with a standard normal distribution. For example, $E\left(\left|\hat{\phi}_{q}-\phi_{q}\right|\right)$ was within $4 \%$, the worst case again being $q=0, \rho_{\theta}=\sqrt{ } 8$. Another advantage of variance stabilizing transformations is that they tend to improve normality. In our two examples, $\hat{\phi}_{q}-\phi_{q}$ was more nearly normal than $\hat{\theta}-\theta$. This suggests forming conditional confidence intervals for $\theta$ by computing $\hat{\phi}_{q} \pm z_{\frac{1}{2}}$, where $z_{\frac{1}{2} p}$ is the upper $\frac{1}{2} p$ point for $N(0,1)$, and transforming back to the $\theta$ scale. This method agrees with $\hat{\theta} \pm z_{t p} p\{I(x)\}^{\frac{1}{2}}$ to first order, but can give quite different results for small sample sizes.

To summarize the results for the spiral model, $Q(x)$ contains very little direct information about $\theta$, but its observed value considerably influences the variance of $\hat{\theta}$. For example, (5•2) shows that if $\rho_{\theta}=\sqrt{ } 16$, then $I(q, \hat{\theta})$ varies from 24 to 8 as $q$ varies from -2 to 2 , causing a threefold change in the variance approximation $1 / I(x)$ for $\hat{\theta}$. In other words, $Q(x)$ acts as an effective ancillary statistic.

We now extend the definitions of $Q(x)$ and $\phi_{q}$ to an arbitrary one parameter family, say $\mathscr{F}=\left\{f_{\theta}(x), \theta \in \Theta\right\}, \Theta$ an interval of $R^{1}$, satisfying the regularity conditions of §8.

Define

$$
Q(x)=\frac{1-I(x) \mid \mathscr{I}_{\theta}}{\gamma_{\theta}},
$$

which agrees with (5•2). Lemma 2 shows that $\sqrt{ } n Q(x) \rightarrow N(0,1)$ as $n \rightarrow \infty$, assuming that $\gamma_{\theta}$ is a continuous function of $\theta$, that is $Q(x)$ is asymptotically ancillary. We have already mentioned that $\left(\hat{\theta}, \ddot{l}_{\theta}\right)$ acts like the sufficient statistic for the two parameter exponential family which best approximates $\mathscr{F}$ near any given point $\theta$ in $\Theta$. The statistic $Q(x)$ is the function of $\left(\hat{\theta}, \ddot{l}_{\theta}\right)$ linear in $\ddot{l}_{\theta}$, for $\hat{\theta}$ fixed, which is asymptotically ancillary. The definition
of $Q(x)$ is also motivated by the obvious geometrical considerations of Fig. 5, generalized in §7.

From (5.6) we can write $I(x)=I(q, \hat{\theta})=\left(1-\gamma_{\theta} q\right) \mathscr{I}_{\theta}$ as before, since $I(x)$ is a function of $\hat{\theta}$ and the observed value $q=Q(x)$.

The general definition we will use for $\phi_{q}$ is

$$
\frac{d \phi_{q}}{d \theta}=\left(\frac{|I(q, \theta)|}{n}\right)^{\ddagger}
$$

where $n$ is the sample size of a random sample $x_{1}, \ldots, x_{n}$ from some member of $\mathscr{F}$. In making this definition, $q$ is considered fixed and $\theta$ variable. The mapping $\theta \rightarrow \phi_{q}$ is monotonic over intervals of $\Theta$ where $I(q, \theta)$ does not change sign. The possible difficulties of definition at points where $I(q, \theta)=0$ do not cause trouble in our examples. A discussion of the special nature of such points is given in §5 of Efron (1978).

In a translation family definition (5.7) automatically produces a linear function of the translation parameter, $\phi_{q}=c_{q}+d_{q} \theta$, if the original $\theta$ is any smooth monotonic function of the translation parameter.

By (2.14) and (5.7), the observed Fisher information for $\phi_{q}$ is

$$
I^{\left(\phi_{Q}\right)}(x)=n I(x) / I(q, \hat{\theta})
$$

and is $n$ for $Q(x)=q$. That is, $I^{\left(\phi_{q}\right)}(x)$ is constant on the level surface $Q(x)=q$. The choice of the constant equal to $n$ keeps $\phi_{q}$ and $\theta$ the same order of magnitude. In the example of §6, as in the spiral example, we verify that $Q(x)$ is close to ancillary, and that $\operatorname{var}\left(\hat{\phi}_{q} \mid q\right) \sim 1 / n$ in accordance with ( $1 \cdot 5$ ).

The transformation $\theta \rightarrow \phi_{q}$ defined by (5.7) is mainly of theoretical and conceptual convenience. Practical evidence certainly suggests that the likelihood is often more normal on the $\phi_{q}$ scale. But the derivation of $\phi_{q}$ is often difficult and usually requires approximation; see §6. Moreover, if, as we believe, the results of §4 generalize, then

$$
2\left(l_{\theta}-l_{\theta}\right)\left|q=2\left(l_{\hat{\phi}_{q}}-l_{\phi_{q}}\right)\right| q=\chi_{1}^{2}+O_{p}\left(n^{-1}\right)
$$

so that confidence limits for $\theta$ can be derived directly from $l_{\theta}(x)$. We emphasize that (5.9) has not been proved for the general case. Confidence limits for $\theta$ can also be determined by taking the quadratic approximation in $(\hat{\theta}-\theta)$ to

$$
n^{\frac{1}{\mathrm{t}}}\left(\hat{\phi}_{q}-\phi_{q}\right)=\int_{\theta}^{\theta} \sqrt{ }|I(q, t)| d t
$$

The numerical results of §6 suggest that the direct likelihood method based on (5.9) is preferable.

A corresponding treatment of locally most powerful tests of $H_{0}: \theta=\theta_{0}$ indicates that the appropriate standardized form of the score statistic is $l_{\theta_{0}} \left\lvert\,\{I(x)\}^{\frac{1}{2}}\right.$, which is approximately $N(0,1)$ conditional on $Q=q$. In this form the score statistic is no more convenient than its asymptotic equivalents, since $\hat{\theta}$ must be computed; for an example, see Hinkley (1977).

What happens when we have $r$ independent sets of samples from the same model? How would we compare the estimates? How would we pool the estimates? Answers to these questions are essentially given by Fisher (1925). Suppose that we have only ( $\hat{\theta}_{j}, I_{j}$ ) for $j=1, \ldots, r$. Then the appropriate pooled statistic is ( $\hat{\theta}_{.}, I_{.}$), say, where $\hat{\theta}_{.}=\Sigma I_{j} \hat{\theta}_{j} / \Sigma I_{j}$ and $I=\Sigma I_{j} ; \hat{\theta}$. is second-order efficient according to Fisher's informal argument. The effective part of $\left(Q_{1}, \ldots, Q_{r}\right)$, to first order, is presumably $Q .=(1+I . \mid \mathscr{I}.) \gamma_{\theta}^{-1}$, where $\mathscr{I}$. is the grand
total Fisher information. A reasonable conjecture is that ( $\hat{\theta}, Q$. ) is equivalent, to second order, to the statistics $(\hat{\theta}, Q)$ computed from the pooled likelihood function. Comparisons of the $\hat{\theta}_{j}$ would be made conditional on $\left(Q_{1}, \ldots, Q_{r}\right)$, and would be asymptotically equivalent to normal-theory comparisons with sample weights $I_{j}$. For example, in testing the equality of parameter values, the likelihood ratio statistic is

$$
W=2 \sum_{j=1}^{r}\left(l_{j, \theta_{j}}-l_{j, \theta}\right) \sim 2 \sum_{j=1}^{r}\left(l_{j, \theta_{j}}-l_{j, \theta .}\right) \sim \sum_{j=1}^{r} I_{j}\left(\hat{\theta}_{j}-\hat{\theta}_{.}\right)^{2}
$$

under the hypothesis of equality. But the right-hand side is

$$
\Sigma I_{j}\left(\hat{\theta}_{j}-\theta\right)^{2}-I_{.}\left(\hat{\theta}_{.}-\theta\right)^{2},
$$

which by extension of earlier arguments is approximately $\chi_{r-1}^{2}$ conditional on

$$
\left(Q_{1}, \ldots, Q_{r}\right)=\left(q_{1}, \ldots, q_{r}\right) .
$$

## 6. Example of a nontranslation family

We illustrate the theory of §5 for a simple nontranslation example, using Monte Carlo methods to estimate the conditional properties of the maximum likelihood estimate.

Let $x_{i}=\left(x_{1 i}, x_{2 i}\right)$ for $i=1, \ldots, n$ be independent bivariate normal pairs with zero mean, unit variances and correlation $\theta$. The two-dimensional sufficient statistic is

$$
s_{1}=\sum_{i=1}^{n} x_{1 i} x_{2 i}, \quad s_{2}=\sum_{i=1}^{n}\left(x_{1 i}^{2}+x_{2 i}^{2}\right),
$$

and the first derivative of the log likelihood function is

$$
l_{\theta}=\frac{n \theta\left(1-\theta^{2}\right)-\theta s_{2}+\left(1+\theta^{2}\right) s_{1}}{\left(1-\theta^{2}\right)^{2}} .
$$

Calculations for the Fisher information and curvature (2-11) are straightforward, yielding

$$
\mathscr{I}_{\theta}=n\left(1+\theta^{2}\right) /\left(1-\theta^{2}\right)^{2}, \quad \gamma_{\theta}^{2}=4\left(1-\theta^{2}\right)^{2} /\left(1+\theta^{2}\right)^{3} .
$$

Some numerical values of both $\mathscr{I}_{\theta}$ and $\gamma_{\theta}^{2}$ are given in Table 3. A qualitative interpretation of the curvature values is that our two-dimensional exponential family model is highly nonlinear for small $|\theta|$, but nearly linear as $\theta \rightarrow \pm 1$. The effect of replacing $\mathscr{I}_{\theta}$ by $I(x)$ is potentially large for small $|\theta|$.

Table 3. Information, curvature, and parameter $\phi_{\theta}$ for special bivariate model
| $\|\theta\|$ | 0 | 0.1 | 0.2 | 0.4 | 0.6 | 0.8 | 0.9 | 0.95 | 1 |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| $\boldsymbol{S}_{\theta} / n$ | 1 | 1.03 | 1.13 | 1.64 | 3.32 | 12.65 | 50.14 | 200 | $\infty$ |
| $\gamma_{\theta}^{2}$ | 4.00 | 3.81 | 3.28 | 1.81 | 0.65 | 0.12 | 0.024 | 0.0055 | 0 |
| $\boldsymbol{\phi}_{0}$ | 0 | 0.100 | 0.204 | 0.435 | 0.737 | 1.235 | 1.727 | 2.217 | $\infty$ |


The variance stabilizing transformation $\theta \rightarrow \phi_{q}$ defined by (5.7) is equivalent to

$$
\phi_{q}=n^{-\frac{1}{2}} \int^{\theta} \mathscr{I}_{t}^{\frac{1}{2}}\left(1-q \gamma_{t}\right)^{\frac{1}{2}} d t .
$$

As in many examples it is difficult to evaluate this transformation exactly, but a good approximation can be obtained by substituting $\left(1-q \gamma_{t}\right)^{\frac{1}{2}} \bumpeq 1-\frac{1}{2} q \gamma_{t}$; recall that $q$ is $O\left(n^{-\frac{1}{2}}\right)$.

In the present case this substitution leads simply to

$$
\phi_{q} \bumpeq \phi_{0}-q \tan ^{-1} \theta,
$$

where

$$
\phi_{0}=2^{\frac{1}{2}} \tanh ^{-1}\left(\xi_{\theta} 2^{\frac{1}{2}}\right)-\tanh ^{-1}\left(\xi_{\theta}\right), \quad \xi_{\theta}=\theta\left(1+\theta^{2}\right)^{-\frac{1}{2}} .
$$

The normalizing effect of the transformation $\theta \rightarrow \phi_{q}$ is illustrated by plots of likelihoods and their normal approximations in Fig. 6 for a small data set with $n=20, s_{1}=12, s_{2}=35$. In each case the likelihood is graphed relative to its maximum. The observed informations, respectively $I(x)$ and $n$, are used as variance inverses in the normal approximations, which are centred on the maximum likelihood estimates.

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-18.jpg?height=722&width=1440&top_left_y=671&top_left_x=144)
Fig. 6. Relative likelihood functions shown by solid curves, and normal approximations, dotted curves, for correlation $\theta$ and transformed parameter $\phi_{a}$ for bivariate normal sample with known $N(0,1)$ marginal distributions. Data: $n=20, s_{1}=12, s_{2}=35, \hat{\theta}=0 \cdot 7185, I(x)=122 \cdot 77$,
$$
q=0.101, \hat{\phi}_{q}=0.928 .
$$

Our interest is in whether $Q(x)$ defined by (5.2) is approximately ancillary, and whether $\operatorname{var}\left(\hat{\phi}_{q} \mid q\right) \sim 1 / n$ is accurate. Notice that $\phi_{0}$ is the transformation which makes $\mathscr{I}_{\theta}=n$, so that the superiority of $I(x)$ over $\mathscr{I}_{\theta}$ as a measure of precision conditional on $Q(x)=q$ may be judged by comparing the conditional variances of $\hat{\phi}_{q}$ and $\hat{\phi}_{0}$. The preceding theory would indicate that conditional on $q$

$$
\frac{\operatorname{var}\left(\hat{\phi}_{q} \mid q\right)-1 / n}{\operatorname{var}\left(\hat{\phi}_{0} \mid q\right)-1 / n}=O_{p}\left(n^{-\frac{1}{2}}\right),
$$

but we have not proved this.
The likelihood equation $l_{\theta}=0$ has three solutions, two of which may be complex; the frequency of multiple real zeros increases with curvature and with $q$. We computed $\hat{\theta}$ as a solution to the likelihood equation by iterating from an efficient estimate of $\theta$, not the sample correlation. We simulated samples for $n$ between 15 and 40 , with $\theta$ ranging between 0 and 0.9 . The numbers of samples were $10,000,50,000$ and 10,000 for $n=15,25$ and 40 respectively. In each case results were recorded for twenty interval values of $q$ in the $99 \%$ range $-2 \leqslant q \leqslant+2$, there being approximately the same number of samples for each $q$ interval.
From the simulation results it was quickly apparent that the range of values of $\theta$ for which the approximate theory of §5 is accurate depends markedly on sample size. For that

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-19.jpg?height=487&width=1480&top_left_y=284&top_left_x=120)
Fig. 7. Empirical cumulative probabilities of approximate ancillary $Q$ in correlation model against $N(0,1)$ cumulative probabilities. (a) $n=15, \theta=0,0 \cdot 3$; (b) $n=25, \theta=0,0 \cdot 3,0 \cdot 5$, shown by closed circles, and $\theta=0 \cdot 6$, open circles; (c) $n=40, \theta=0 \cdot 7$, closed circles, and $\theta=0 \cdot 9$, open circles. Numbers of samples exceed 10,000 .

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-19.jpg?height=1176&width=1494&top_left_y=1048&top_left_x=114)
Fig. 8. Monte Carlo estimates of conditional variances of $\hat{\phi}_{q}$, shown by closed circles, and of $\hat{\phi}_{0}$, open circles, given $Q=q$ in correlation model. Dashed line, theoretical approximation, $1 / n$. Numbers of samples exceed 10,000 .

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-20.jpg?height=722&width=883&top_left_y=254&top_left_x=395)
Fig. 9. Monte Carlo estimates of conditional mean of $\hat{\phi}_{q}$, circles, given $Q=q$, and theoretical approximation, dashed line, in the correlation model with $n=25, \theta=0.5$, Estimates from 50,000 samples.

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-20.jpg?height=993&width=1184&top_left_y=1210&top_left_x=244)
Fig. 10. Monte Carlo estimates of pr (statistic $\geqslant 3.84 \mid Q=q$ ) for three likelihood statistics in correlation model with $n=25, \theta=0.3$. Statistics: $2\left(l_{\hat{\theta}}-l_{\theta}\right)$, shown by solid curve; $n\left(\hat{\phi}_{\theta}-\phi_{\theta}\right)^{2}$, dashed curve; $n\left(\hat{\phi}_{0}-\phi_{0}\right)^{2}$, dotted curve. Estimates from 50,000 samples.

reason we give a comprehensive set of illustrations here. First, Fig. 7 contains normal plots of the empirical distributions of $Q(x)$, a separate graph for each sample size. Several $\theta$ cases are indistinguishable, but clearly as $|\theta| \rightarrow 1$ the approximate ancillarity of $Q(x)$ breaks down.

Figure 8 contains plots of empirical conditional variances of both $\hat{\phi}_{q}$ and $\hat{\phi}_{0}$ for six representative cases. Standard errors for the estimated variances are indicated. These graphs confirm the theory to a remarkable degree. Particularly striking are the deviations from $n^{-1}$ of the conditional variances of $\hat{\phi}_{0}$.

The approximation (6.2) is remarkably accurate for the conditional mean of $\hat{\phi}_{q}$, which implies that the conditional mean of $\hat{\phi}_{0}$ deviates from $\phi_{0}$. Figure 9 illustrates a typical case.

The final numerical results are concerned with approximate methods for obtaining confidence limits for $\theta$. According to our theory, both $n\left(\hat{\phi}_{q}-\phi_{q}\right)^{2}$ and $2\left(l_{\theta}-l_{\theta}\right)$ are approximate $\chi_{1}^{2}$ variables conditional on $q$. In contrast $n\left(\hat{\phi}_{0}-\phi_{0}\right)^{2}$, which is an approximate $\chi_{1}^{2}$ variable unconditionally, does not have this property conditionally. Figure 10 contains empirical conditional tail probabilities for all three of these statistics corresponding to the value $3 \cdot 84$, nominal 0.05 probability, for the case $n=25, \theta=0.3$. Our speculative theory is nicely confirmed by these and similar results. As in the Cauchy case, §4, the likelihood ratio method gives the best agreement with the chi-squared approximation.

Note that even for $n=40$ conditioning on $q$ is likely to have an appreciable effect, because the coefficient of variation of $I(x)$ is as high as $0 \cdot 3$, its value at $\theta=0$. Thus at $n=40$ the unconditional variance approximation $1 / \mathscr{I}_{\theta}$ can easily depart by a factor of two from the conditional variance approximation.

## 7. Curved exponential families

The definition of the asymptotic ancillary statistic $Q(x)$ at (5.6) is motivated by the geometry of curved exponential families. This section gives a brief description of the geometry involved. More details are given by Efron (1975, 1978).

We begin with a $k$-dimensional exponential family $\mathscr{G}$, with density functions of the form

$$
g_{\alpha}(x)=\exp \left\{\alpha^{\mathrm{T}} x-\psi(\alpha)\right\} \quad(\alpha \in A, x \in \mathscr{X}),
$$

$\psi(\alpha)$ being a normalizing constant. The natural parameter space $A$ and the sample space $\mathscr{X}$ are both subsets of $R^{k}, A$ being convex. Corresponding to each $\alpha$ is the mean vector and covariance matrix of $x$,

$$
\beta=E_{\alpha}(x), \quad \Omega_{\alpha}=\operatorname{cov}_{\alpha}(x) .
$$

The mapping from $\alpha$ to $\beta$ is one to one, so $\mathscr{G}$ can just as well be indexed by $\beta$ as by $\alpha$. The space $B=\{\beta(\alpha): \alpha \in A\}$ is not necessarily convex.

A curved exponential family $\mathscr{F}$ is a one parameter subset of $\mathscr{G}$, with typical density function say

$$
f_{\theta}(x)=\exp \left(\alpha_{\theta}^{\mathrm{T}} x-\psi_{\theta}\right), \quad \psi_{\theta}=\psi\left(\alpha_{\theta}\right)
$$

Here $\theta$ is a real parameter contained in $\Theta$, an interval of $R^{1}$, and the mapping $\theta \rightarrow \alpha_{\theta}$ is assumed to be continuously twice differentiable; $\mathscr{F}$ is fully described by the curve $\mathscr{F}_{A}=\left\{\alpha_{\theta}: \theta \in \Theta\right\}$ through $A$, or equivalently by the curve $\mathscr{F}_{B}=\left\{\beta_{\theta}=\beta\left(\alpha_{\theta}\right): \theta \in \Theta\right\}$ through $B$. All of our examples, except for those in § 1, involve curved exponential families.

If $\mathscr{G}$ is two-dimensional, as in Figs 3 and 5, then for a given $\hat{\theta}$, the set $Q(x)=q$ is a single vector. It is shown in §5 of Efron (1975) that this vector $v$ has squared Mahalanobis distance $q^{2}$ from $\mathscr{F}_{B}$ in the inner product $\Omega_{\theta}^{-1}:\left(v-\beta_{\theta}\right)^{\mathrm{T}} \Omega_{\theta}^{-1}\left(v-\beta_{\theta}\right)=q^{2}$. This generalizes the geometric description of $Q(x)$ given in Fig. 5, where $\Omega_{\theta}$ is the identity. A similar interpretation holds
for higher dimensional families $\mathscr{G}$. The Cauchy translation problem may be thought of as a limiting case of a curved exponential family, as remarked at the end of § 5 of Efron (1975).

We use the notation $\Omega_{\theta}=\Omega_{\alpha_{\theta}}$, and also $\dot{\alpha}_{\theta}=d \alpha_{\theta} / d \theta, \ddot{\alpha}_{\theta}=d^{2} \alpha_{\theta} / d \theta^{2}$.
Suppose $x_{1}, \ldots, x_{n}$ is a random sample from some member $f_{\theta}$ of $\mathscr{F}$. The average vector $\bar{x}=\Sigma x_{i} / n$ is a sufficient statistic for $\theta$, and it is easy to verify that the derivatives of the log likelihood function are

$$
l_{\theta}(\bar{x})=n \dot{\alpha}_{\theta}^{\mathrm{T}}\left(\bar{x}-\beta_{\theta}\right), \quad l_{\theta}(\bar{x})=n \ddot{\alpha}_{\theta}^{\mathrm{T}}\left(\bar{x}-\beta_{\theta}\right)-\mathscr{I}_{\theta},
$$

where $\mathscr{I}_{\theta}=n \dot{\alpha}_{\theta}^{\mathrm{T}} \Omega_{\theta} \dot{\alpha}_{\theta}$ is the Fisher information.
Figure 11 illustrates two useful facts about solutions to the maximum likelihood equation $l_{\theta}(\bar{x})=0$, both of which follow from (7.4).
(i) Given $\hat{\theta}$, the set of $\bar{x}$ vectors for which $l_{\theta}(\bar{x})=0$, that is for which $\hat{\theta}$ is a solution to the likelihood equations, is the $k-1$-dimensional hyperplane through $\beta_{\theta}$ orthogonal to $\dot{\alpha}_{\theta}$, say

$$
\mathscr{L}_{\theta}=\left\{\bar{x}: \dot{\alpha}_{\theta}^{\mathrm{T}}\left(\bar{x}-\beta_{\theta}\right)=0\right\} .
$$

(ii) From (5•6) and (7•4),

$$
Q(x)=n \ddot{\alpha}_{\theta}^{\mathrm{T}}\left(\bar{x}-\beta_{\theta}\right) /\left(\gamma_{\theta} \mathscr{I}_{\theta}\right) .
$$

Therefore for a given $\hat{\theta}$, the set of $\bar{x}$ vectors for which $Q(x)=q$ is the $k-2$-dimensional hyperplane contained in $\mathscr{L}_{\theta}$ and orthogonal to $\delta_{\theta}$, the projection of $\ddot{\alpha}_{\theta}$ into $\mathscr{L}_{\theta}$.

![](https://cdn.mathpix.com/cropped/729c1a90-112b-4445-856c-adc9f726c2b3-22.jpg?height=765&width=1160&top_left_y=1153&top_left_x=288)
Fig. 11. Geometry of maximum likelihood estimation in a three-dimensional curved exponential family. Curve $\mathscr{F}_{B}$, values of $\beta_{\theta}=E_{\theta}(\bar{x})$; plane $\mathscr{L}_{t}$ orthogonal to $\dot{\alpha}_{t}$, vectors $x$ for which $\hat{\theta}=t$; vector $\delta_{t}$, projection of $\ddot{\alpha}_{t}$ in $\mathscr{L}_{t}$, is $q$ axis when $\hat{\theta}=t$.

So far we have discussed two 'coordinates' of $\bar{x}$ of particular interest, namely $\hat{\theta}$ and $q$. The remaining $k-2$ coordinates necessary to specify $\bar{x}$ completely are higher order ancillaries, corresponding to the $l_{\theta}^{(\cdot j)}$ for the translation problem. We can replace $\bar{x}$ by the sufficient statistic ( $\hat{\theta}, a$ ), where $a$ represents the $k-1$ coordinates which locate $\bar{x}$ in $\mathscr{L}_{\theta}$. The coordinate system for $a$ rotates with $\mathscr{L}_{\theta}$, so that the first coordinate of $a$ always corresponds to $Q(x)$. The second coordinate of $a$ is essentially the component of $\bar{x}$ along that part of $\alpha_{\dot{\theta}}^{(.3)}$ orthogonal
to $\dot{\alpha}_{\theta}$ and $\ddot{\alpha}_{\theta}$, orthogonal being defined with respect to the inner product $\Omega_{\theta}$. This process of definition can be continued so that each successive component of $a$ is less important in describing local behaviour of the likelihood function near $\hat{\theta}$, and so that $a \sqrt{ } n \rightarrow N_{k-1}\left(0, V_{a}\right)$ as $n \rightarrow \infty$. In other words, $a$ is asymptotically ancillary. In curved exponential families, Lemma 2 can be extended to give this stronger result.

## 8. Details of theoretical results

We describe here proofs of Lemmas 1 and 2 of § 2, and Lemma 3 of § 4, together with some incidental remarks about the Cauchy location example discussed in §§ 1 and 4.

Lemmas 1 and 3 relate to expansions for conditional expectations of the form $E\{k(t) \mid a\}$, where the conditional density of $t=\hat{\theta}-\theta$ is given by (2•1) and (2•3). These expansions are deterministic numerical approximations of the form

$$
E\{k(t) \mid a\}=v(a)+r(a)
$$

where for a given $s$ and any $\varepsilon>0$

$$
\lim _{n \rightarrow \infty} \operatorname{pr}_{\theta}\left\{\left|n^{8} r(a)\right|<\varepsilon\right\}=0
$$

We write $r(a)=o_{p}\left(n^{-8}\right)$ to express this. Most of the theory relies on standard asymptotic results for regular likelihoods, a particularly useful reference being Walker (1969). Sufficient conditions for each result are given at the end of the proof.

For Lemma 1, consider the conditional mean squared error of $t=\hat{\theta}-\theta$. By (2•1) and (2•3) we may write

$$
E\left(t^{2} \mid a\right)=\int_{-\infty}^{\infty} t^{2} h_{a}(t) d t / \int_{-\infty}^{\infty} h_{a}(t) d t=\int_{-\infty}^{\infty} t^{2} \exp \left(l_{\theta-t}-l_{\theta}\right) d t / \int_{-\infty}^{\infty} \exp \left(l_{\theta-t}-l_{\theta}\right) d t
$$

where $l_{\theta}=l_{\theta(x)}(x)$. If both integrals here are finite, as we assume, then they may be approximated arbitrarily closely by the corresponding integrals truncated at $t= \pm b(a)$ for suitably large finite $b(a)$. We choose $b(a)$ so that the error incurred in (8.1) is $o_{p}\left(n^{-2}\right)$.

The next simplification follows from the fact that for arbitrary $\delta>0$ there is a $c_{\delta}>0$ such that

$$
\lim _{n \rightarrow \infty} \operatorname{pr}_{\theta}\left\{\sup _{|1|>\delta} n^{-1}\left(l_{\theta-t}-l_{\theta}\right)<-c_{\delta}\right\}=1,
$$

a result essentially given by Walker (1969, §3). This result implies that the contributions to the integrals in $(8 \cdot 1)$ from $\delta<|t| \leqslant b(a)$ are $O_{p}\left(e^{-n c 8}\right)$, certainly $o_{p}\left(n^{-k}\right)$ for all $k$, for all $\delta>0$. Our problem then reduces to computing for arbitrarily small $\delta$ the truncated integrals

$$
N(\delta, a)=\int_{-\delta}^{\delta} t^{2} \exp \left(l_{\theta-t}-l_{\theta}\right) d t, \quad D(\delta, a)=\int_{-\delta}^{\delta} \exp \left(l_{\theta-t}-l_{\theta}\right) d t
$$

It will be convenient to write $c_{j}=(-1)^{j+1} l_{\theta}^{(\cdot j)}$ for $j=1,2, \ldots$, where $c_{2}=I(x)$ and $c_{1}=0$, assuming $\hat{\theta}$ to be a stationary point of $l_{\theta}$. Then we have the Taylor expansion

$$
l_{\theta-1}-l_{\theta}=-\frac{1}{2} c_{2} t^{2}-\frac{1}{6} c_{3} t^{3}-\frac{1}{24} c_{4} t^{4}\left(1+\varepsilon_{n}\right),
$$

where

$$
\varepsilon_{n}=\left(l_{\hat{\theta}_{1}}^{(\cdot 4)}-l_{\hat{\theta}}^{(\cdot 4)}\right) / c_{4}, \quad \hat{\theta_{1}} \in(\hat{\theta}-t, \hat{\theta}) .
$$

Under a continuity condition on $l_{\theta}^{(\cdot 4)}, \varepsilon_{n}$ will be $o_{p}(1)$. We now use (8.3) to expand the integrals in ( $8 \cdot 2$ ) about the leading normal density term. To do this, let

$$
z=t \sqrt{ } c_{2}, \quad w=w(z)=\frac{1}{6} c_{3} t^{3}+\frac{1}{24} c_{4} t^{4}\left(1+\varepsilon_{n}\right)
$$

and note that

$$
1-w+\frac{1}{2} w^{2}-\frac{1}{6}|w|^{3} \leqslant e^{-w} \leqslant 1-w+\frac{1}{2} w^{2}+\frac{1}{6}|w|^{3} .
$$

Substitution of (8.5) and use of (8.6) for the first integral in (8.2) gives

$$
\begin{aligned}
\int_{-\delta \sqrt{ } c_{2}}^{\delta \sqrt{ } c_{2}} z^{2}\left(1-w+\frac{1}{2} w^{2}-\frac{1}{6}|w|^{3}\right) \phi(z) d z & \leqslant c_{2}^{3 / 2} N(\delta, a) /(2 \pi)^{\frac{1}{2}} \\
& \leqslant \int_{-\delta \sqrt{ } c_{2}}^{\delta \sqrt{ } c_{2}} z^{2}\left(1-w+\frac{1}{2} w^{2}+\frac{1}{6}|w|^{3}\right) \phi(z) d z
\end{aligned}
$$

where $\phi(z)$ is the $N(0,1)$ density. Next replace the integration limits $\pm \delta \sqrt{ } c_{2}$ by $\pm \infty$, which incurs an error of $O_{p}\left(e^{-n}\right)$ because $c_{2}^{-1}=O_{p}\left(n^{-1}\right)$. Then the integrals in (8.7) simply involve the first twelve moments of the $N(0,1)$ distribution. Using the fact that $c_{j} / c_{2}^{s}=O_{p}\left(n^{1-s}\right)$, calculation of the bounds in (8.7) immediately leads to

$$
N(\delta, a)=\frac{(2 \pi)^{\frac{1}{2}}}{c_{2}^{3 / 2}}\left\{1-\frac{15}{24} \frac{c_{4}}{c_{2}^{2}}+\frac{105}{72} \frac{c_{3}^{2}}{c_{2}^{3}}+O_{p}\left(n^{-2}\right)+O_{p}\left(n^{-1} \varepsilon_{n}\right)\right\} .
$$

The corresponding evaluation of the second integral in (8.2) gives

$$
D(\delta, a)=\frac{(2 \pi)^{\frac{1}{2}}}{c_{2}^{\frac{1}{2}}}\left\{1-\frac{3}{24} \frac{c_{4}}{c_{2}^{2}}+\frac{5}{4} \frac{c_{3}^{2}}{c_{2}^{3}}+O_{p}\left(n^{-2}\right)+O_{p}\left(n^{-1} \varepsilon_{n}\right)\right\} .
$$

Finally, noting that the magnitudes of earlier truncation errors are smaller than those in (8.8) and (8.9), and that $\varepsilon_{n}=o_{p}(1)$, we substitute for numerator and denominator in (8.1) and simplify to obtain ( $2 \cdot 8$ ).

The corresponding calculation for $E(t \mid a)$ is very similar and need not be given here. The conditional variance (2•7) is simply $E\left(t^{2} \mid a\right)-\{E(t \mid a)\}^{2}$.

The essential conditions for these results to hold are, first, that $E\left\{(\hat{\theta}-\theta)^{2}\right\}<\infty$, so that the integrals in (8.1) exist. Secondly, the first four derivatives of $\log f_{\theta}(x)$ with respect to $\theta$ exist in an open neighbourhood of the true $\theta$ and have finite expectations; the second derivative has strictly negative expectation, $\mathscr{I}>0$. Also we require a condition on $l_{\theta}^{(\cdot 4)}(x)$ to ensure that $\varepsilon_{n}$ in (8.4) is $o_{p}(1)$. Since in (8.4) we have $\left|\hat{\theta}_{1}-\hat{\theta}\right|<\delta$, and $|\theta-\hat{\theta}|<\delta$ for suitably large $n$, it is sufficient to assume that for $\left|\theta_{0}-\theta\right|<\delta$

$$
\left|l_{\theta_{0}}^{(.4)}\left(x_{1}\right)-l_{\theta}^{(.4)}\left(x_{1}\right)\right|<M_{\delta}\left(x_{1}, \theta\right), \quad \lim _{\delta \rightarrow 0} E_{\theta} M_{\delta}\left(x_{1}, \theta\right) \rightarrow 0
$$

A similar condition was used by Walker (1969).
Under stronger regularity conditions the remainder terms in (2.7)-(2.8) can be shown to be $O_{p}\left(n^{-2}\right)$ rather than $o_{p}\left(n^{-1}\right)$.

Lemma 3 is proved in much the same way as Lemma 1, using Laplace transforms. Because of the very similar natures of ( $4 \cdot 3$ ) and ( $4 \cdot 4$ ), we discuss only the latter.

Consider, then, the log likelihood ratio statistic $v(x)=2\left(l_{\theta}-l_{\theta}\right)=2\left(l_{\theta}-l_{\theta-1}\right)$. The conditional moment generating function of $v(x)$ is, by (2•1) and (2•3),

$$
E\left(e^{s v(x)} \mid a\right)=\int_{-\infty}^{\infty} \exp \left\{(1-2 s)\left(l_{\theta-t}-l_{\theta}\right)\right\} d t / \int_{-\infty}^{\infty} \exp \left(l_{\theta-t}-l_{\theta}\right) d t
$$

We assume that $s<\frac{1}{2}$. Approximation to both integrals is accomplished just as in Lemma 1, after which (8.3) is used for $|t|<\delta$ with $\varepsilon_{n}$ as in (8.4). A calculation parallel to that leading from ( $8 \cdot 2$ ) to ( $8 \cdot 8$ ) gives

$$
\int_{-\delta}^{\delta} \exp \left\{(1-2 s)\left(l_{\theta-t}-l_{\theta}\right)\right\} d t=\left(\frac{2 \pi}{c_{2}}\right)^{\frac{1}{2}} \frac{1}{(1-2 s)^{\frac{1}{3}}}\left\{1-\left(\frac{1}{8} \frac{c_{4}}{c_{2}^{2}}-\frac{5}{24} \frac{c_{3}^{2}}{c_{2}^{3}}\right)\left(\frac{1}{1-2 s}\right)+O_{p}\left(n^{-1} \varepsilon_{n}\right)\right\},
$$

with the $c_{j}$ as in Lemma 1. Substitution of (8.11) in the numerator and denominator $(s=0)$ of (8.10) gives

$$
E\left(e^{s v(x)} \mid a\right)=\frac{1}{(1-2 s)^{\frac{1}{2}}}\left\{1+\frac{1}{8} \frac{c_{4}}{c_{2}^{2}}-\frac{5}{24} \frac{c_{3}^{2}}{c_{2}^{3}}-\left(\frac{1}{8} \frac{c_{4}}{c_{2}^{2}}-\frac{5}{24} \frac{c_{3}^{2}}{c_{2}^{3}}\right)\left(\frac{1}{1-2 s}\right)+o_{p}\left(n^{-1}\right)\right\}
$$

for $s<\frac{1}{2}$; the $o_{p}\left(n^{-1}\right)$ term is a bounded function of $s$ for $s \leqslant \frac{1}{2}-\eta, \eta>0$.
Formal inversion of (8.12) gives the result (4.4). The necessary regularity conditions are clearly the same as those given for Lemma 1, and in addition we assume that $E_{\theta}[\exp \{s v(x)\}]<\infty$ for $s<\frac{1}{2}$.

The $o_{p}\left(n^{-1}\right)$ terms in (4-3) and (4-4) will be $O_{p}\left(n^{-2}\right)$ under stronger regularity conditions.
The second-order expansions in Lemmas 1 and 3 help to explain the deviations from firstorder approximations apparent in Figs 1 and 4 for the Cauchy case. To show this informally we argue as follows. By symmetry $E_{\theta}\left\{l_{\dot{\theta}}^{(\cdot 3)} \mid I(x)\right\}=0$, so that $\left(l_{\dot{\theta}}^{(\cdot 3)}\right)^{2} \mid I(x)=O_{p}(n)$. Therefore, taking expectations with respect to $a$ conditional on $I(x)$ in Lemmas 1 and 3, we have that

$$
\begin{aligned}
\operatorname{var}(\hat{\theta} \mid I) & \sim \frac{1}{I}\left\{1+\frac{I}{2} \frac{K(I)}{I^{2}}\right\} \\
\operatorname{pr}\{u(x) \leqslant c \mid I(x)\} & \sim\left\{1+\frac{1}{8} \frac{K(I)}{I^{2}}\right\} \operatorname{pr}\left(\chi_{1}^{2} \leqslant c\right)+\frac{1}{8} \frac{K(I)}{I^{2}} \operatorname{pr}\left(\chi_{5}^{2} \leqslant c\right) \\
\operatorname{pr}\{v(x) \leqslant c \mid I(x)\} & \sim\left\{1+\frac{1}{8} \frac{K(I)}{I^{2}}\right\} \operatorname{pr}\left(\chi_{1}^{2} \leqslant c\right)+\frac{1}{8} \frac{K(I)}{I^{2}} \operatorname{pr}\left(\chi_{3}^{2} \leqslant c\right)
\end{aligned}
$$

where $K(I)=E\left\{l_{\theta}^{\cdot 4)} \mid I(x)\right\}$.
Now suppose that $K(I) \sim b_{1} n+b_{2} I$, so that

$$
E\left\{l_{\theta}^{(\cdot 4)}\right\}=E\{K(I)\} \sim b_{1} n+b_{2} E\{I(x)\} \sim b_{1} n+b_{2} \mathscr{I} .
$$

For the Cauchy distribution $E\left\{l_{\theta}^{(\cdot 4)}\right\}=\mathscr{I}$, so that $b_{1} \sim 0$ and $b_{2} \sim 1$. The implied form of (8.13) is $\operatorname{var}(\hat{\theta} \mid I) \sim I^{-1}\{1+1 /(2 I)\}$, which is a very good approximation to the empirical variances in Fig. 1, and is for the majority of cases at $n=10$. The implied forms of (8.14) are also very accurate. Note that (8.14) also explains the tendency for $v(x)$ to be closer to $\chi_{1}^{2}$ than is $u(x)$, because $\chi_{3}^{2}$ is stochastically smaller than $\chi_{5}^{2}$.

For Lemma 2 sufficient regularity conditions are stated in the last paragraph, following the formal derivation. First notice that since $I(x) / \mathscr{J}_{\theta}$ is invariant under monotone reparameterizations, by (2-14), we can change to the parameter $\sigma$ defined by $d \sigma / d \theta=\mathscr{I}_{\theta} / n$, for which $\mathscr{I}^{(\sigma)}=n$. We might as well assume this parameterization to begin with, so $\mathscr{I}_{\theta}=n$ for all $\theta$. This implies $\nu_{20}(\theta)=1$ since, by definition, $\nu_{20}(\theta)$ is the Fisher information in a single observation. For notational convenience, let $\theta=0$ be the true value of the parameter. Then we wish to show that

$$
\sqrt{ } n\left(\frac{I(x)}{n}-1\right)=\frac{I(x)-n}{\sqrt{ } n} \rightarrow N\left(0, \gamma_{0}^{2}\right)
$$

under independent sampling from $f_{0}(x)$.

Let $S(x)=\left\{-\ddot{l}_{0}(x)-n-\nu_{11}(0) \dot{l}_{0}(x)\right\} / \sqrt{ } n$. Because $\nu_{11}(0)$ is the regression coefficient of $-\ddot{l}_{0}$ on $l_{0}$, and by definition (2.11) and the preceding definitions, it is easy to see that $S(x) \rightarrow N\left(0, \gamma_{0}^{2}\right)$. The proof is completed by showing that $S(x)$ is asymptotically equivalent to $\{I(x)-n\} / \sqrt{ } n$.

Notice that by differentiating $\nu_{20}(\theta)=1=E_{\theta}\left\{-l_{\theta}(x)\right\}$ with respect to $\theta$ we get that

$$
E_{\theta}\left\{-l_{\theta}^{(\cdot .3)}(x)\right\}=\nu_{11}(\theta)
$$

The strong law of large numbers then implies that $-l_{\theta}^{(.3)}(x) / n=\nu_{11}(\theta)\left(1+\varepsilon_{n}\right)$, where $\varepsilon_{n} \rightarrow 0$ almost everywhere. In what follows, $\varepsilon_{n}$ will stand for any sequence of random variables converging to zero almost everywhere. The standard proof for the asymptotic normality of $\hat{\theta}$, as in Rao (1973,§5f), shows that $\hat{\theta}=\left\{l_{0}(x) / n\right\}\left(1+\varepsilon_{n}\right)$. These results imply that the expansion $l_{\theta}(x)=l_{0}(x)+\hat{\theta} l_{0}^{(.3)}(x)+\frac{1}{2} \hat{\theta}^{2} l_{\theta_{1}}^{(.4)}(x), \hat{\theta}_{1} \in(0, \hat{\theta})$, can be rewritten as

$$
\frac{-l_{\theta}(x)-n}{\sqrt{ } n}=S(x)-\varepsilon_{n} \nu_{11}(0) \frac{l_{0}(x)}{\sqrt{ } n}-\hat{\theta}^{2} \sqrt{ } n \frac{l_{\theta_{1}}^{(\cdot 4)}(x)}{2 n} .
$$

Since $l_{0}(x) / \sqrt{ } n \rightarrow N(0,1)$, the term $\varepsilon_{n} \nu_{11} l_{0}(x) / \sqrt{ } n \rightarrow 0$. The last term in (8.17) is also negligible under a boundedness condition on $l_{\theta}^{(\cdot 4)}(x)$, completing the proof of (8.15).

The regularity conditions needed in this proof are (i) the usual conditions for the asymptotic normality of the maximum likelihood estimate, see Rao (1973, §5f); (ii) equality (8.16), or any regularity conditions justifying the differentiation under the integral sign leading to (8.16); (iii) $\left|l_{\theta_{1}}^{(\cdot 4)}(x)\right|<M(x)$ for $\theta_{1}$ in a neighbourhood of 0 , where $E_{0} M(x)<\infty$. Then $\left|l_{\theta_{1}}^{(.4)}(x) / n\right|<\Sigma M(x) / n \rightarrow E_{0}\{M(x)\}$ justifying the last step in the proof. We remark that these conditions are always satisfied in curved exponential families. Less stringent conditions are required for (2/14).

## 9. Concluding remarks

The thrust of this paper has been to offer what we believe to be convincing evidence that there is a meaningful approximate conditional inference for single parameters based on the maximum likelihood estimate $\hat{\theta}$ and the observed information $I(x)$. For the most part the evidence has been empirical, although in the location case the theory flows directly from Fisher's exact calculations. In the nonlocation case the discussions of §§ 5 and 7 demonstrate the existence of a dominant approximate ancillary, together with a convenient framework of curved exponential families for further work. We have not obtained a formal proof generalizing the results of §§ 2 and 4 , although we do not doubt that this is possible.

A careful reading of Fisher's work on likelihood estimation suggests that the emphasis on $\mathscr{I}_{\theta}$ is due to the emphasis on a priori comparisons among estimators. The use of $I(x)$ in the interpretation of given data sets is recommended, and some readers of Fisher's work have inferred ( 1.5 ); see, for example, the biography by Yates \& Mather (1963, p. 100). Relevant work in the context of nonlinear regression may be found in papers be Beale (1960) and Bliss \& James (1966), both of which mention some of the geometric ideas underlying our own approach in §§ 5 and 7. A different approach to the problem is due to Fraser (1964). A useful general article on likelihood inference is by Sprott (1975), which summarizes much of the work by G. A. Barnard, J. D. Kalbfleisch, Sprott himself and others.

Not all of the examples that we considered have been included here. We also looked at the $N\left(\theta, c \theta^{2}\right)$ case discussed by Hinkley (1977); a two-parameter linear model version of Fisher's hyperbola; and the double-exponential location model, where the theory of § 2 must fail, but does so in an intriguing manner.

We have not attempted to discuss the case of several parameters, which raises certain problems of definition. However, the extension of our results to the case of the general regular location-scale model is straightforward, again because of duality between conditional distribution and likelihood (Hinkley, 1978).

## References

Beale, E. M. L. (1960). Confidence regions in non-linear estimation (with discussion). J. R. Statist. Soc. B 22, 41-88.
Bliss, C. I. \& James, A. T. (1966). Fitting the rectangular hyperbola. Biometrics 22, 573-602.
Cox, D. R. (1958). Some problems connected with statistical inference. Ann. Math. Statist. 29, 357-72.
Cox, D. R. \& Hinkley, D. V. (1974). Theoretical Statistics. London: Chapman and Hall.
Efron, B. (1975). Defining the curvature of a statistical problem (with applications to second order efficiency) (with discussion). Ann. Statist. 3, 1189-242.
Efron, B. (1978). The geometry of exponential families. Ann. Statist. 6, 362-76.
Fisher, R. A. (1925). Theory of statistical estimation. Proc. Camb. Phil. Soc. 22, 700-25.
Fisher, R. A. (1934). Two new properties of mathematical likelihood. Proc. R. Soc. A 144, 285-307.
Fisher, R. A. (1974). Statistical Methods and Scientific Inference, 3rd edition. Edinburgh: Oliver \& Boyd.
Fraser, D. A. S. (1964). Local conditional sufficiency. J. R. Statist. Soc. B 26, 52-62.
Hinkley, D. V. (1977). Conditional inference about a normal mean with known coefficient of variation. Biometrika 64, 105-8.
Hinkley, D. V. (1978). Likelihood inference about location and scale parameters. Biometrika 65, 253-61.
Rao, C. R. (1973). Linear Statistical Inference and its Applications, 2nd edition. New York: Wiley.
Sprott, D. A. (1975). Application of maximum likelihood methods to finite samples. Sankhyā 37 B, 259-70.
Walker, A. M. (1969). On the asymptotic behaviour of posterior distributions. J. R. Statist. Soc. B 31, 80-8.
Yates, F. \& Mather, K. (1963). Ronald Aylmer Fisher 1890-1962. Biog. Mem. Fellows R. Soc., London 9, 91-120.
[Received February 1978. Revised June 1978]

## Comments on paper by B. Efron and D. V. Hinkley

## By OLE BARNDORFF-NIELSEN

## Department of Theoretical Statistics, Aarhus University

Ever since Fisher's (1925) first discussion of ancillarity it has been a reigning impression that the observed information $I(x)$ is, in general, an approximate ancillary statistic. Parts of Efron \& Hinkley's (1978) paper seem prone to perpetuate this impression; see the remarks immediately after formulae (1•5) and (1•6). It is, however, false. The statistic $I(x)$ may be ancillary and may capture most or all of the relevant ancillary information available for inference on $\theta$, such as is the case in the Cauchy example and for Fisher's circle and hyperbola models. Note that the possible ancillarity properties of $I(x)$ depend on the parameterization chosen. Thus in Fisher's hyperbola model the observed information relative to the parameter $e^{\theta}$, which was the original parameter in Fisher's discussion, is not ancillary. At the other extreme, $I(x)$ may be a minimal sufficient statistic and this is often the case for linear exponential families; the $\sigma^{2} \chi^{2}$ distribution affords an example of this. In relation to this latter example, note that if $x_{1}, \ldots, x_{n}$ is a sample from the $\sigma^{2} \chi^{2}$ distribution with one degree of freedom, then $I\left(x_{1}, \ldots, x_{n}\right)$ is minimal sufficient for any sample size even though the distribution sampled is, in effect, a translation family. It can also happen that $I(x)$ is constant while there exists a simple and significant ancillary statistic. This can be illustrated for instance by means of the hyperbolic distribution (Barndorff-Nielsen, 1977, 1978).

