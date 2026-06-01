---
citekey: wangLargesampleTheoryParametric1998
item_type: article
authors: 'Wang, N'
year: 1998
title: Large-Sample Theory for Parametric Multiple Imputation Procedures
venue: Biometrika
volume: 85
issue: 4
pages: 935--948
doi: 10.1093/biomet/85.4.935
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\wang_large_sample_theory_1998.pdf'
pdf_sha256: 98502808ede602577e1cac11eaa92467ff17eede04514c46c204d1f1b383a415
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T15:21:35Z
---
# Large-sample theory for parametric multiple imputation procedures 

By NAISYIN WANG<br>Department of Statistics, Texas A\&M University, College Station, Texas 77843, U.S.A.<br>nwang@picard.tamu.edu

and JAMES M. ROBINS<br>Department of Epidemiology, Harvard School of Public Health, 677 Huntington Avenue, Boston, Massachusetts 02115, U.S.A.<br>robins@episun1.harvard.edu


#### Abstract

Summary We consider the asymptotic behaviour of various parametric multiple imputation procedures which include but are not restricted to the 'proper' imputation procedures proposed by Rubin (1978). The asymptotic variance structure of the resulting estimators is provided. This result is used to compare the relative efficiencies of different imputation procedures. It also provides a basis to understand the behaviour of two Monte Carlo iterative estimators, stochastic em (Celeux \& Diebolt, 1985; Wei \& Tanner, 1990) and simulated em (Ruud, 1991). We further develop properties of these estimators when they stop at iteration $K$ with imputation size $m$. An application to a measurement error problem is used to illustrate the results.


Some key words: Asymptotic distribution; EM algorithm; Loglikelihood score; Measurement error model; Missing data.

## 1. Introduction

In observational studies, data are often missing either by chance or design. A number of statistical procedures have been proposed that first use multiple imputation methods repeatedly to fill in the missing data and then use standard complete data methods to analyse the 'completed' data. Different multiple imputation methods have been proposed in the context of different statistical models: parametric (Ruud, 1991; Celeux \& Diebolt, 1985), non- or semiparametric (Reilly, 1993), randomisation (Rubin, 1987, Ch. 4; Fay, 1996) and fully Bayesian models (Rubin, 1978, 1987, Ch. 3). They serve different purposes such as the 'completion' of public-use data tapes with missing values (Rubin, 1978, 1987, 1996; Fay, 1996; Meng, 1994), or to substitute for a computationally difficult or intractable expectation step in the em algorithm (Celeux \& Diebolt, 1985; Diebolt \& Celeux, 1993; Diebolt \& Ip, 1996; Tanner, 1993; Wei \& Tanner, 1990; Ruud, 1991; McFadden \& Ruud, 1994; Robins \& Gill, 1997; Deltour, Richardson \& Le Hesran, 1999).

The interrelationships between these multiple imputation methods have not been studied. Consequently, the performance of various methods as statistical estimation procedures has not been compared. It is the goal of this paper to provide an asymptotic theory for multiple imputation estimators of the parameter $\theta$ of a correctly specified regular para-
metric model. Generalisations of our results to semiparametric or misspecified parametric models and to settings, like those considered in Meng (1994), Rubin (1996) and Fay (1996), in which the parametric model used to produce imputations for public-use data tapes differs from the consumers' analysis model will be the subjects of later reports.

The multiple imputation method proposed by Rubin (1978, 1987), working in a Bayesian context, is one of the most popular among applied scientists who rely on simple complete data procedures for data analysis. Rubin's original goal was to impute $m$ completed data sets for public usage in the context of public surveys in which a response rate of less than $60 \%$ for any variable was rare. However, because of its ease of implementation and increasing familiarity, Rubin's method is recently being used outside this context, for example as the primary analytical method for 'two-stage' studies in which response rates are as low as $0 \cdot 1$ to $1 \%$ (Greenland \& Finkle, 1995). To reduce data storage costs, it may be desirable for the number of imputed datasets, $m$, to be as small as two or three.

Wei \& Tanner (1990) obviated a full Bayesian formulation by suggesting that one imputed missing values from the conditional distribution of the missing data given the observed evaluated at the maximum likelihood estimate. Their method belongs to a class referred to as 'improper' by Rubin (1987, Ch. 3) in contrast to his class of 'proper' procedures. When one's goal is to create public-use data tapes, Rubin states a preference for proper imputation methods based on certain inferential concerns and the availability of a computationally convenient variance estimator that may remain useful even when the parametric model used to produce the imputations differs from the consumer's analysis model. However, when, as in this paper, one's concern is with estimation efficiency in a correctly specified parametric model, we show that the improper procedure of Wei \& Tanner is always to be preferred to that of Rubin for finite $m$, because of its strictly smaller asymptotic variance. The asymptotic properties of these two types of non-iterative multiple imputation procedure and theoretical and numerical comparisons of their efficiencies are given in § 3. We find that the efficiency of the proper estimator relative to the improper may be as low as $60 \%$ when $m$ is small and the response rate is low.

In this setting, the inefficiency of Rubin's procedure is even more striking when we turn our attention from point to interval estimation. Specifically, we derive a consistent estimator for the asymptotic variance of the 'improper' estimator and use it to construct a Wald-type interval estimator. In § 3, we show that, even when the efficiency of the proper point estimator relative to the improper is nearly $90 \%$, nonetheless the median length of Rubin's interval estimator is a striking 1.9 times that of the Wald intervals. This poor performance arises because Rubin's variance estimator, although unbiased, is not consistent. As a result, $t$-intervals, which have a fairly large expected length, are used rather than the standard $z$-intervals in order to attain nominal coverage rates. Thus, the improper point and Wald interval estimates, though computationally more complicated, are clearly preferable in terms of efficiency when $m$ is small and the fraction of missing data is at least moderate.

An entirely different use for multiple imputation is to substitute for an intractable E -step in the em algorithm. Both the stochastic (Celeux \& Diebolt, 1985) and simulated (Ruud, 1991) em algorithms are 'iterative' imputation procedures. In general, for the simulated or stochastic em estimator to be consistent, iteration must continue to convergence or stationarity; see §4. This may require excessive computation time, especially when $m$ is large and the convergence of the algorithms is mainly decided by the linear convergence rate of em-like algorithms. However, in settings in which one has an inefficient but easily computed and consistent asymptotically linear initial estimate of $\theta$, one may want to stop
the iteration when the relative efficiency reaches a desired level as each iterate is itself consistent asymptotically normal. For inference, one then only requires the asymptotic distribution of the $k$ th iterate. Therefore, in § 4, we derive the asymptotic variances of the simulated and stochastic em estimators when stopped after $k$ iterations with $m$ imputations per iteration. We show that the asymptotic variance of the stochastic em estimator is less than that of the simulated em and that, for the simulated em estimator, it may be more efficient to stop after $k$ iterations than to iterate to convergence.

Finally, we analyse a parametric measurement error problem with a validation sample and a dichotomous outcome using the stochastic and simulated em. This model is a natural one for our approach since an inefficient complete-case estimator based on the validation sample is easily computed, the e-step of the em algorithm is computationally burdensome, but it is easy to draw from the conditional law of the missing data given the observed data by rejection sampling.

## 2. The model

We shall study the following statistical model. The complete data $Y=\left(Y_{1}, \ldots, Y_{p}\right)^{\prime}$, of dimension $p \times 1$, is randomly drawn from a population whose density is $f\left(Y ; \theta_{0}\right)$, a regular parametric family, $\left\{f(Y ; \theta) ; \theta \in \Theta \subset R^{q}\right\}$, with respect to a dominating measure $\mu$, where $\theta_{0}$ is an unknown parameter to be estimated. Let $R_{k}$ be the indicator of whether or not the $k$ th component of $Y$ was observed and let $R=\left(R_{1}, \ldots, R_{p}\right)^{\prime}$. We also denote the observed and unobserved components of $Y$ by $Y_{R}$ and $Y_{\bar{R}}$, respectively. Rubin refers to $Y_{R}$ and $Y_{\bar{R}}$ as $Y_{\text {obs }}$ and $Y_{\text {mis }}$. Throughout, we assume that the data are missing at random; that is, the probability that $R=r$ given $Y$ does not depend on the unobserved component $Y_{\bar{R}}$ of $Y$. We observe $n$ independent and identically distributed realisations $Z=\left\{R^{i}, Y_{R}^{i} ; i=1, \ldots, n\right\}$ of $\left(R, Y_{R}\right)$. To avoid extraneous issues, we assume
(i) that the complete-data maximum likelihood estimator, $\hat{\theta}_{c}$, and the observed-data maximum likelihood estimator, $\hat{\theta}_{\text {MLE }}$, are, respectively, the unique solutions to the complete-data score equation $\sum S_{i}(\theta)=0$ and the observed-data score equation $\sum S_{i}^{\text {obs }}(\theta)=0$, where $S(\theta)=S(Y ; \theta)=\partial \log f(Y ; \theta) / \partial \theta$ is the loglikelihood score if the data were completely observed and $S^{\text {obs }}(\theta)=E_{\theta}\left\{S(\theta) \mid Y_{R}\right\}$ is the score function of the observed-data loglikelihood; and
(ii) $\hat{\theta}_{c}$ and $\hat{\theta}_{\text {MLE }}$ are consistent asymptotically linear estimators of $\theta_{0}$ with influence functions $I_{c}^{-1} S\left(\theta_{0}\right)$ and $I_{\text {obs }}^{-1} S^{\text {obs }}\left(\theta_{0}\right)$, where $I_{c}=E_{0_{0}}\left\{S\left(\theta_{0}\right)^{\otimes 2}\right\}$ and $I_{\text {obs }}= E_{\theta_{0}}\left\{S^{\text {obs }}\left(\theta_{0}\right)^{\otimes 2}\right\}$ are the full- and observed-data information matrices and $A^{\otimes 2}=A A^{\prime}$.
An estimator $\theta$ of $\theta_{0}$ is consistent asymptotically linear with influence function $D$ if $n^{\frac{1}{2}}\left(\hat{\theta}-\theta_{0}\right)=n^{-\frac{1}{2}} \sum D_{i}+o_{p}(1)$, where $D$ has a zero mean and a finite covariance matrix and $o_{p}(1)$ denotes a random variable converging to zero in probability. Consequently, $n^{\frac{1}{2}}\left(\hat{\theta}-\theta_{0}\right)$ is asymptotically normal with mean zero and variance $E\left[D^{\otimes 2}\right]$. For example, $\hat{\theta}_{c}$ and $\hat{\theta}_{\mathrm{MLE}}$ have asymptotic variances $I_{c}^{-1}$ and $I_{\mathrm{obs}}^{-1}$, respectively.

## 3. Asymptotic properties of non-iterative multiple imputation estimators

### 3.1. Definition of the estimators

We shall study two types of non-iterative multiple imputation estimator, type A and type B. In Rubin's nomenclature, type A estimators use a proper and type B estimators use an improper imputation method. For $i=1, \ldots, n$, let $Y_{R}^{i j}\left(\tilde{\theta}_{j}\right)(j=1, \ldots, m)$ be $m$
imputed copies of subject $i$ 's missing data; each $Y_{R}^{i j}\left(\tilde{\theta}_{j}\right)$ is drawn independently from $f\left(Y_{\bar{R}} \mid Y_{R}^{i} ; \tilde{\theta}_{j}\right)$. For type $\mathrm{B}, \tilde{\theta}_{j}=\hat{\theta}_{P}$ is a preliminary consistent asymptotically linear estimate of $\theta_{0}$ computed from the observed data $Z$. For type $\mathrm{A}, \tilde{\theta}_{j}$ is a single independent draw from the posterior density $f(\theta \mid Z)$ of $\theta$ under a Bayesian model. Let $S_{i j}\left(\theta, \tilde{\theta}_{j}\right)=S\left[\left\{Y_{R}^{i}, Y_{R}^{i j}\left(\tilde{\theta}_{j}\right)\right\} ; \theta\right]$ be the completed data score contributed by subject $i$ in the $j$ th completed dataset. Then the $j$ th completed dataset maximum likelihood estimator of $\theta_{0}, \hat{\theta}_{j} \equiv \hat{\theta}_{j}\left(\tilde{\theta}_{j}\right)$, solves $n^{-\frac{1}{2}} \sum_{i} S_{i j}\left(\theta, \tilde{\theta}_{j}\right)=0$. Rubin suggests a final inference based on $\bar{\theta}=\sum \hat{\theta}_{j} / m$. As an alternative to solving $m$ separate score equations to obtain $\hat{\theta}_{1}, \ldots, \hat{\theta}_{m}$ and then averaging, one could use the estimator $\hat{\theta}$ that solves the single 'clustered data' estimating equation $0=m^{-1} \sum \sum S_{i j}\left(\theta, \tilde{\theta}_{j}\right)$ (Fay, 1996). The following lemma, which follows from simple algebraic arguments and Slutsky's theorem (Billingsley, 1968, § 1.5), implies that the two estimators have the same asymptotic distributions. We shall therefore treat the estimators $\hat{\theta}$ and $\bar{\theta}$ interchangeably in the sequel.

Lemma 1. Estimators $\hat{\theta}$ and $\bar{\theta}$ are asymptotically equivalent, that is, $n^{\frac{1}{2}}(\hat{\theta}-\bar{\theta})$ converges to zero in probability.

### 3.2. Asymptotic distribution of the type B estimator

Write $\hat{\theta}_{B}$ to denote a type B estimator $\hat{\theta}$ based on a preliminary asymptotically linear estimator $\hat{\theta}_{\boldsymbol{P}}$ with asymptotic variance $B$. The following theorem, proved in the Appendix, gives the asymptotic distribution of $\hat{\theta}_{B}$. Let $I_{\text {mis }} \equiv I_{c}-I_{\text {obs }}$ be the missing information matrix. Then $J=I_{\text {mis }} I_{c}^{-1}$ is the 'fraction' of missing information matrix (Rubin, 1987, Ch. 4). Let $\Delta(B)=B-I_{\text {obs }}^{-1}$ be the nonnegative definite difference between the asymptotic variance matrix of $\hat{\theta}_{P}$ and $\hat{\theta}_{\text {MLE }}$.

Theorem 1. Under the regularity conditions in the Appendix, $n^{\frac{1}{2}}\left\{\hat{\theta}_{B}-\theta_{0}\right\}$ is asymptotically normal with mean zero and variance

$$
V_{B} \equiv I_{\mathrm{obs}}^{-1}+J^{\prime} \Delta(B) J+m^{-1} I_{c}^{-1} J .
$$

Corollary 1. If $\hat{\theta}_{P}=\hat{\theta}_{\mathrm{MLE}}$, the asymptotic variance of $\hat{\theta}_{B}$ is $V_{B}=I_{\mathrm{ob} 3}^{-1}+m^{-1} I_{c}^{-1} J$.
Theorem 1 and its corollary show that the asymptotic variance $I_{\text {obs }}^{-1}$ of $\hat{\theta}_{\text {MLE }}$ differs from that of $\hat{\theta}_{B}$ by two positive semidefinite terms. The third term, $m^{-1} I_{c}^{-1} J$, in (1) is attributable to the additional variability resulting from the finite number of imputations $m$. This term, which does not depend on the initial estimator $\hat{\theta}_{P}$, increases with the fraction of missing information $J$ and goes to zero as $m \rightarrow \infty$. The second term, $J^{\prime} \Delta(B) J$, is attributable to the inefficiency of $\hat{\theta}_{P}$, and does not depend on the number of imputations $m$. Since, when $\hat{\theta}_{P}$ is inefficient, $B-\left\{I_{\text {obs }}^{-1}+J^{\prime} \Delta(B) J\right\}$ is positive definite, $\hat{\theta}_{B}$ will always be more efficient than $\hat{\theta}_{P}$ when $m=\infty$. In fact, with $m=\infty, \hat{\theta}_{B}$ is exactly a one-step update of $\hat{\theta}_{P}$ using the EM algorithm. When $m$ is finite and $\hat{\theta}_{P}$ is inefficient, $\hat{\theta}_{B}$ may or may not be more efficient than $\hat{\theta}_{P}$ depending on the relative sizes of the terms in (1).

### 3.3. Asymptotic distribution of type A estimators

Assume the standard regularity conditions hold for the model and the prior which guarantee that the posterior distribution of $\theta$ given the observed data $Z$ is asymptotically normal with mean $\hat{\theta}_{\text {MLE }}$ and variance matrix $\left\{-\sum \partial S_{i}^{\text {obs }}\left(\hat{\theta}_{\text {MLE }}\right) / \partial \theta^{\prime}\right\}^{-1}$ almost surely on $Z$. The validity of $z$ and $t$ inference procedures proposed by Rubin (1987, Ch. 3) require this assumption. The following theorem then characterises the asymptotic distribution of the type A multiple imputation estimator $\hat{\theta}_{A}$.

Theorem 2. Under the regularity conditions in the Appendix, $n^{\frac{1}{2}}\left(\hat{\theta}_{A}-\theta_{0}\right)$ is asymptotically normal with mean zero and variance

$$
V_{A}=I_{\mathrm{obs}}^{-1}+m^{-1} J_{c}^{-1} J+m^{-1} J^{\prime} I_{\mathrm{obs}}^{-1} J .
$$

The proof of Theorem 2 is outlined in the Appendix. It follows that the inflation, $m^{-1} J^{\prime} I_{\text {obs }}^{-1} J$, of the type A asymptotic variance over that of a type B estimator with the preliminary estimate $\hat{\theta}_{P}=\hat{\theta}_{\text {MLE }}$, goes to zero as $m \rightarrow \infty$ and increases with the fraction of missing information. This suggests that, when $m$ is small and the fraction of missing data large, the type B, improper estimator could be significantly more efficient than the type A, proper estimator. We use Example (2.1) of Rubin (1987) to illustrate this result.

Example 1. Suppose $Y$ is $N\left(\mu, \sigma^{2}\right)$ when $\theta=\left(\mu, \sigma^{2}\right)^{\prime}$. Let $\pi=\operatorname{pr}(R=1 \mid Y)=\operatorname{pr}(R=1)$ be the probability that $Y$ is observed. Then $\hat{\theta}_{\text {MLE }}^{\prime}=\left(\hat{\mu}_{\text {MLE }}, \sigma_{\text {MLE }}^{2}\right)$ is the sample mean and variance of $Y$ calculated from the $N_{\text {obs }}$ of the $n$ subjects with $Y$ observed. The type B estimator with $\hat{\theta}_{P}=\hat{\theta}_{\text {MLE }}$ imputes independent replications for each subject with missing data from a $N\left(\hat{\mu}_{\text {MLE }}, \hat{\sigma}_{\text {MLE }}^{2}\right)$ distribution. For the type A estimator, Rubin shows that, with standard non-informative priors, the $j$ th imputed value of $Y^{i j}$ for a subject $i$ with missing data is obtained as follows:
(i) draw a random variable $v_{1 j}$, from a $\chi^{2}$ distribution with $N_{\text {obs }}-1$ degrees of freedom, and let $\gamma_{j}^{2}=\hat{\sigma}_{\text {MLE }}^{2}\left(N_{\text {obs }}-1\right) / v_{i j}$;
(ii) draw $\tilde{\mu}_{j}$ from a $N\left(\hat{\mu}_{\text {MLE }}, N_{\text {obs }}^{-1} \tilde{\sigma}_{j}^{2}\right)$ distribution;
(iii) draw $Y^{i j}$ from a $N\left(\tilde{\mu}_{j}, \tilde{\sigma}_{j}^{2}\right)$ distribution.

For various choices of $\pi$ and $m$, we evaluated the relative efficiency of the type A estimator compared to the type B. The results are summarised in Fig. 1. The relative efficiency drops to nearly $60 \%$ when $m=2$ and $\pi=0 \cdot 1$, but increases rapidly when either $\pi$ or $m$ is increased.

![](https://cdn.mathpix.com/cropped/93183a7d-de35-4baa-8773-1d02e3b13fd7-05.jpg?height=702&width=654&top_left_y=1472&top_left_x=575)
Fig. 1. Example 1. The relative efficiency of the type $A$ estimator with respect to the corresponding type B estimator versus the proportion of observed data, $\pi$. Five curves, from bottom to top, correspond to imputation size $m=2,3,5,10$ and 20 , respectively.

### 3.4. Variance estimation

The asymptotic variances $V_{B}$ and $V_{A}$ of $\hat{\theta}_{B}$ and $\hat{\theta}_{A}$ depend on $I_{\text {obs }}, I_{c}$ and the asymptotic variance $B$ of $\hat{\theta}_{P}$. Usually, as in the measurement error example in § 4.3, a consistent estimator $\hat{B}$ of $B$ can be easily computed. It therefore remains to find consistent estimators of $I_{c}$ and $I_{\text {obs }}$. A consistent estimator for $I_{c}$ is $\hat{I}_{c}=m^{-1} \sum \hat{I}_{c, j}$, where $\hat{I}_{c, j}= -n^{-1} \sum \partial S_{i j}(\theta, \tilde{\theta}) /\left.\partial \theta^{\prime}\right|_{\theta=\hat{\theta}}$ is the usual observed information for the $j$ th completed dataset given by off-the-shelf software packages. A consistent estimator for $I_{\text {obs }}$ is motivated by the following lemma by Robins \& Gill (1997), which states that the expected outer product of the completed data scores for two different completed datasets equals $I_{\text {obs }}$.

Lemma 2. For $j \neq j^{*}, E\left\{S_{i j}\left(\theta_{0}, \theta_{0}\right) S_{i j^{*}}^{\prime}\left(\theta_{0}, \theta_{0}\right)\right\}=E\left\{S_{\text {obs }}^{\otimes 2}\left(\theta_{0}\right)\right\} \equiv I_{\text {obs }}$.
A symmetrised positive definite consistent estimator of $I_{\text {obs }}$ is

$$
\hat{I}_{\text {obs }}=\frac{1}{2 n m(m-1)} \sum_{i} \sum_{j \neq j^{*}}\left\{S_{i j}\left(\hat{\theta}, \tilde{\theta}_{j}\right) S_{i j^{*}}\left(\hat{\theta}, \tilde{\theta}_{j^{*}}\right)^{\prime}+S_{i j^{*}}\left(\hat{\theta}, \tilde{\theta}_{j^{*}}\right) S_{i j}\left(\hat{\theta}, \tilde{\theta}_{j}\right)^{\prime}\right\}
$$

Let $\hat{V}_{B}$ and $\hat{V}_{A}$ be $V_{B}$ and $V_{A}$ in (1) and (2), with $\hat{I}_{c}, \hat{I}_{\text {obs }}, \hat{J}=I-\hat{I}_{\text {obs }} \hat{I}_{c}^{-1}$ and $\hat{B}$ replacing $I_{c}, I_{\text {obs }}, J$ and $B$, where $I$ denotes the $q \times q$ identity matrix. Then $\hat{V}_{B}$ and $\hat{V}_{A}$ are consistent for $V_{B}$ and $V_{A}$. Furthermore, by Slutsky's theorem, $n^{\frac{1}{2}} V_{t}^{-\frac{1}{2}}\left(\hat{\theta}_{t}-\theta_{0}\right), t$ in $\{A, B\}$, are asymptotically standard normal. Thus, Wald-type inferences can be directly applied.

### 3.5. Comparison with inference based on Rubin's variance estimators

Rubin (1987, Ch. 3, 4) proposed to use $\tilde{V}_{A}$, which does not require explicit estimation of $I_{\text {obs }}$, to estimate $V_{A}$, where

$$
\tilde{V}_{A}=\hat{I}_{c}^{-1}+\left(1+m^{-1}\right) \tilde{Q}_{A}, \quad \tilde{Q}_{A}=n(m-1)^{-1} \sum\left(\hat{\theta}_{A j}-\bar{\theta}_{A}\right)^{\otimes 2}
$$

Recall that $\hat{\theta}_{A j}$ is the estimate based on the $j$ th completed dataset using the type A imputation. In the above formula for $\tilde{Q}_{A}$, the empirical between-imputation variance of $\hat{\theta}_{A j}$ is multiplied by the sample size $n$ to make $\tilde{Q}_{A}$, the empirical between-imputation variance of $\hat{\theta}_{A j}$ is multiplied by the sample size $n$ to make $\tilde{Q}_{A}$ an $O_{p}(1)$ random variable, where a random variable is $O_{p}(1)$ if it is bounded in probability.

As in Rubin (1987, Ch. 3, 4), we concentrate on the cases where $\operatorname{var}\left\{\left.n^{\frac{1}{2}}\left(\hat{\theta}_{A j}-\theta_{0}\right) \right\rvert\, Z\right\}$ is finite with probability one; when this condition fails, $\widetilde{V}_{A}$ might need to be robustified in some suitable fashion to control the influence of the heavy tails of $\hat{\theta}_{A j}$. In §§4.1 and $4 \cdot 2$ below, we will use the following identities, proved in the Appendix,

$$
\begin{aligned}
& V_{A}=I_{c}^{-1}+\left(1+m^{-1}\right)\left(I_{\text {obs }}^{-1}-I_{c}^{-1}\right), \\
& E\left\{E\left(\tilde{Q}_{A} \mid Z\right)\right\}=I_{\text {obs }}^{-1}-I_{c}^{-1}+o(1),
\end{aligned}
$$

to study the properties of $\widetilde{V}_{A}$ in the $m$-infinite and $m$-finite settings. Throughout $\S \S 4 \cdot 1$ and 4.2 references to $\hat{\theta}_{B}$ or $V_{B}$ refer to the case in which $\hat{\theta}_{P}=\hat{\theta}_{\text {MLE }}$. Also, for any two matrices $M_{A}$ and $M_{B}, M_{A} \geqslant M_{B}$ indicates that $M_{A}-M_{B}$ is positive semidefinite, whereas the strict inequality implies that $M_{A}-M_{B}$ is positive definite.

Case I (infinite m). If both $m$ and $n \rightarrow \infty$, then (i) $\hat{\theta}_{A}$ and $\hat{\theta}_{B}$ will have the same limiting distribution, and (ii), by (3) and (4), $\widetilde{V}_{A}$ will consistently estimate $V_{A}=V_{B}=I_{\text {obs }}^{-1}$, since $\widetilde{Q}_{A}$ will be consistent for $I_{\text {obs }}^{-1}-I_{c}^{-1}$. Thus, by Slutsky's theorem, the Wald intervals using $\tilde{V}_{A}$ will cover $\theta_{0}$ at their nominal confidence level for large samples. However, as noted by Rubin (1987), such intervals with $\hat{\theta}_{B j}$ substituted for $\hat{\theta}_{A j}$ will under-cover. Define $\tilde{V}_{B}$ and
$\tilde{Q}_{B}$ by analogy with the type A estimators; it is easy to see that $\tilde{Q}_{B}$ converges to $I_{c}^{-1} I_{\text {mis }} I_{c}^{-1}$, which is smaller than or equal to $I_{\text {obs }}^{-1}-I_{c}^{-1}$. This result explains why, from a frequentist perspective, Rubin (1987, Ch. 4) suggested using a type A, proper, rather than a type B , improper estimator even though $\bar{\theta}_{A}$ and $\bar{\theta}_{B}$ have the same limiting distribution. Note that, when $m$ goes to infinity, both $\widehat{V}_{A}$ and $\widehat{V}_{B}$ of § $3 \cdot 4$ converge in probability to the same and correct limit. The comparison between two types of variance estimator becomes much more important when we consider the finite $m$ case where $V_{A} \neq V_{B}$.

Case II (finite $m$ ). When $m$ is finite, as noted by Rubin (1987), $\widetilde{V}_{A}$ has a nondegenerate limiting distribution and thus does not converge to the constant $I_{\text {obs }}^{-1}-I_{c}^{-1}$. Nonetheless, the asymptotic means of $\tilde{Q}_{A}$ and $\tilde{V}_{A}$ equal $I_{\text {obs }}^{-1}-I_{c}^{-1}$ and $V_{A}$. Hence $\tilde{V}_{A}$ remains a sensible estimator of $V_{A}$. Since the asymptotic normality for $n^{\frac{1}{2}} \tilde{V}_{A}^{-\frac{1}{2}}\left(\hat{\theta}_{A}-\theta_{0}\right)$ no longer holds, Rubin suggests replacing a $z$-critical value by a $t$-critical value with an approximated degree of freedom (Rubin, 1987, p. 77). However, these $t$ intervals will cover $\theta_{0}$ at their nominal rate at the cost of a rather large expected confidence interval length due to the heavy $t$ tails. This unfortunate trade-off can be bypassed by replacing $\widetilde{V}_{A}$ by $\hat{V}_{A}$ since it is consistent for $V_{A}$. An even better strategy is to use the type B , improper, Wald interval based on the estimator $\hat{\theta}_{B}$ and the estimated variance $\hat{V}_{B}$, which, for finite $m$, will (i) have a shorter expected length than the corresponding $A$ intervals, since $V_{B}<V_{A}$, and (ii) still cover $\theta_{0}$ at the nominal confidence level in large samples. This point is illustrated in the following simulation study.

Example 1 (cont.). In the setting of Example 1, we conducted a small simulation study with sample size $n=50$, the number of imputations $m=3$ and the response rate, $\pi$, equal to $0.9,0.5$ and 0.25 , respectively. One thousand datasets were generated for each of the three scenarios. In Table 1, we report the Monte Carlo means and variances of $\hat{\theta}_{A}$ and $\hat{\theta}_{B}$, with the preliminary estimator $\hat{\theta}_{P}$ being the observed-data maximum likelihood estimator, that is, the sample mean of the observed data. The relative efficiency of $\hat{\theta}_{A}$ compared to $\hat{\theta}_{B}$ is never less than $0.86=0.8784 / 1.093$ since $\pi$ was not very small. We also report the actual coverage rates of nominal $95 \%$ confidence intervals. For the type B estimator $\hat{\theta}_{B}$, we report the Wald $z$-interval based on $\hat{V}_{B}$. For $\hat{\theta}_{A}$, we report (i) the $z$-interval based on $\tilde{V}_{A}$, (ii) the $t$-interval based on $\tilde{V}_{A}$, and (iii) the Wald $z$-interval based on $\hat{V}_{A}$. We also report the Monte Carlo median of the ratios of the lengths of the type A intervals to those of

Table 1. Example 1 (cont.). Results based on 1000 simulations, $m=3$, summary statistics of estimated $\mu$ for a normal mean problem with the true $\mu=0$. Entries reading from left to right in each row are sample mean $\times 10$, sample variance $\times 10$, coverage probability for 95\% confidence intervals and median ratio of the length of each confidence interval over that of type $\mathrm{B} z$-interval. Results for three different type A intervals are reported, (i) z-interval using $\widetilde{V}_{A}$, (ii) $t$-interval using $\widetilde{V}_{A}$ and (iii) $z$-interval using $\hat{V}_{A}$; first and second entries inside parentheses are for (ii) and (iii), respectively
|  | $\pi$ | Sample mean | Sample var. | Coverage prob. | Median length ratio |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Type B | 0.9 | 0.1571 | 0-2207 | 0.961 | 1.00 |
| Type A |  | 0.1713 | 0-2250 | 0933 (0-950, 0-958) | 0.929 (0.992, 1.002) |
| Type B | 0.5 | 0.3411 | 0.4160 | 0965 | 1.00 |
| Type A |  | $0 \cdot 2472$ | 04654 | 0.887 (0.943, 0.966) | 0.776 (1.516, 1.033) |
| Type B | 0.25 | 0.3552 | 0.8784 | 0.978 | 1.00 |
| Type A |  | 03206 | 1.0930 | 0.889 (0-980, 0-973) | 0852 (1.871, 1.069) |


the type B intervals. As predicted by the theory, when $\pi$ is small, the $z$-interval based on $\tilde{V}_{A}$ under-covers and the $t$-interval has median length 1.87 times that of the type $\mathrm{B} z$-interval and $1 \cdot 8=1 \cdot 87 / 1 \cdot 069$ times that of the type $\mathrm{A} z$-interval based on $\hat{V}_{A}$.

In practice when, as in Example 1, an efficient and easily computed estimator of $\theta$ is available, there is no reason to use a multiple imputation estimator. Rather, the purpose of Example 1 was to compare, in a simple tractable setting, the performance of alternative imputation procedures. Fitting parametric models by multiple imputation methods will be of practical importance for those models with a computationally difficult or intractable expectation step in the EM algorithm; see § 4 for examples.

## 4. Iterative multiple imputation estimators

### 4.1. The stochastic em and simulated em algorithms

Iterative versions of the type B estimator $\hat{\theta}_{B}$ have been proposed to substitute for a computationally difficult or intractable e-step in the em algorithm. Both the stochastic em algorithm (Celeux \& Diebolt, 1985; Tanner, 1993) and the simulated em algorithm (Ruud, 1991) start from an initial $\hat{\theta}_{P}$ and compute $\hat{\theta}_{B}^{(1)}=\hat{\theta}_{B}$ and then iterate by regarding the current estimate $\hat{\theta}_{B}^{(k)}$ as $\hat{\theta}_{P}$ and updating to $\hat{\theta}_{B}^{(k+1)}=\hat{\theta}_{B}$. In the simulated EM algorithm, the same pseudo-random numbers drawn in the first iteration are reused to draw the imputations in subsequent iterations. In the stochastic em algorithm, an independent set of pseudo-random numbers is used in each iteration. As a consequence, the stochastic em algorithm is computationally more intensive than the simulated em algorithm, especially if it is computationally demanding to draw from $f\left\{Y_{R} \mid Y_{R}^{i} ; \hat{\theta}_{B}^{(k-1)}\right\}$. Ruud (1991) did not require the starting value $\hat{\theta}_{P}$ to be a consistent, asymptotically linear estimator of $\theta_{0}$. Consequently, to ensure consistency he required the simulated em algorithm to be iterated until convergence. McFadden \& Ruud (1994) prove that, under regularity conditions, as $K \rightarrow \infty$, the iterative simulated em estimates, $\hat{\theta}_{\text {sim }, K}=\hat{\theta}_{B}^{(K)}$ converge to a consistent, asymptotically linear limit, $\hat{\theta}_{\text {sim }}$, with the variance

$$
V_{\min }=I_{\mathrm{obs}}^{-1}+m^{-1} I_{\mathrm{obs}}^{-1} I_{\mathrm{mis}} I_{\mathrm{obs}}^{-1} .
$$

Although the iterates $\hat{\theta}_{\text {sto, } K}$ of the stochastic EM algorithm do not converge point-wise for finite $m$, nonetheless they do converge to a stationary distribution under regularity conditions (Diebolt \& Celeux, 1993). These authors further show that, as $K \rightarrow \infty, \bar{\theta}_{\text {sto, } K}$, the average of the first $K$ iterates after the algorithm converges, goes to a consistent, asymptotically linear limit $\bar{\theta}_{\text {sto }}$ which is efficient for $\theta_{0}$. However, the computation time necessary to reach convergence or stationarity could be excessive for both algorithms, especially when $m$ and the fraction of missing data are large.

### 4.2. Properties of $\hat{\theta}_{\text {sto }, K}$ and $\hat{\theta}_{\text {sim }, K}$ for finite $m$ and $K$

If, as in the measurement error example of § $4 \cdot 3$, one has an initial inefficient consistent asymptotically linear estimator of $\theta_{0}$, then each iterate is itself consistent asymptotically linear so one needs not iterate until convergence or stationarity. Note that, even though these estimators may not be efficient especially when $m$ is small, one can easily obtain the estimated relative efficiency at each iteration. If, as in the example in § $4 \cdot 3$, after several iterations the asymptotic relative efficiency of the iterate is already near 1 , then one may choose to stop the iteration at that point. The following theorems provide the asymptotic distribution of $\hat{\theta}_{\text {sto, } K}$ and $\hat{\theta}_{\text {sim, } K}$ when $\hat{\theta}_{P}$ is a consistent asymptotically linear estimate of $\theta_{0}$ with asymptotic variance $B$.

Theorem 3. Under the regularity conditions in the Appendix, $n^{\frac{1}{2}}\left(\hat{\theta}_{\text {sim }, K}-\theta_{0}\right)(K \geqslant 1)$ is asymptotically normal with mean 0 and variance

$$
V_{\text {sim }, K}=I_{\text {obs }}^{-1}+\Sigma_{P}^{(K)}+\Sigma_{\text {imp }, \text { sim }}^{(K)},
$$

where $\Sigma_{P}^{(K)}=\left(J^{K}\right)^{\prime} \Delta(B) J^{K}$ and

$$
\Sigma_{\text {imp.sim }}^{(K)}=m^{-1} I_{c}^{-1}\left(\sum_{k=1}^{K} J^{K-k}\right) I_{\text {mis }}\left(\sum_{k=1}^{K} J^{K-k}\right)^{\prime} I_{c}^{-1} .
$$

Theorem 4. Under regularity conditions, $n^{\frac{1}{2}}\left(\hat{\theta}_{\text {sto }, K}-\theta_{0}\right)(K \geqslant 1)$ is asymptotically normal with mean 0 and asymptotic variance $V_{\text {sto }, K}=I_{\text {obs }}^{-1}+\Sigma_{p}^{(K)}+\Sigma_{\text {imp, sto, }}^{(K)}$, where

$$
\Sigma_{\mathrm{imp}, \mathrm{sto}}^{(K)}=\sum_{k=1}^{K} m_{k}^{-1} I_{c}^{-1} J^{K-k} I_{\mathrm{mis}}\left(J^{K-k}\right)^{\prime} I_{c}^{-1}
$$

and where $m_{k}(k=1, \ldots, K)$ is the number of imputations used in the $k$ th iteration.
Both theorems can be obtained through simple algebraic derivations following the asymptotic expansions for $\hat{\theta}_{\text {sto }, K}$ and $\hat{\theta}_{\text {sim }, K}$ given in (A5) and (A6), respectively. In the Appendix we prove the following corollary.

Corollary 2. Suppose for the stochastic em algorithm $m_{k}=m$ for $k=1, \ldots, K$. Then $V_{\text {sim }, K}-V_{\text {sto }, K}$ is positive semidefinite. Further, as $K \rightarrow \infty$,
(i) $V_{\text {sim }, K} \rightarrow V_{\text {sim }}$ given by (5), and
(ii) $V_{\text {sto }, K} \rightarrow V_{\text {sto }} \equiv I_{\text {obs }}^{-1}+m^{-1} I_{c}^{-1} I_{\text {mis }} I_{c}^{-1}\left(I-J^{2}\right)^{-1}$.

The two theorems and Corollary 2 above provide insight about the behaviour of $\hat{\theta}_{\text {sim }, K}$ and $\hat{\theta}_{\text {sto }, K}$. We summarise them in the following remarks. To simplify the notation in the presentation, unless otherwise we consider $m_{k} \equiv m$ in $\hat{\theta}_{\text {sto }, K}$.

Remark 1. The matrices $\Sigma_{\text {imp }}^{(K)}$ and $\Sigma_{P}^{(K)}$ correspond to the extra variation caused by the imputations and by the inefficient preliminary estimator respectively. We prove in Lemma A1 in the Appendix that the matrix norm $\left\|J^{K}\right\|$ goes to zero as $K$ increases. As a consequence, as indicated in Corollary 2, the effect of the initial inefficiency in $\hat{\theta}_{P}$ is eliminated as $K \rightarrow \infty$. On the other hand, $\Sigma_{\text {imp, sim }}^{(K)}$ and $\Sigma_{\text {imp, sto }}^{(K)}$ both increase with $K$ and decrease with $m$.

Remark 2. By Corollary 2, it is obvious that $V_{\text {sim }}$ and $V_{\text {sto }}$ need not be smaller than the asymptotic variance $B$ of the initial estimator $\hat{\theta}_{P}$. An extreme example is when $\hat{\theta}_{P}=\hat{\theta}_{\text {MLE }}$ and $B=I_{\text {obs }}^{-1}$. However, it can be easily shown that, for the stochastic em algorithm, if, for the given imputation size, $m$, and the initial variance $B$, there is an improvement in efficiency after the first iteration, then there is an improvement in each iteration; that is, if $V_{\text {sto, } 1}-B$ is nonpositive definite then so is $V_{\text {sto, } k}-V_{\text {sto, } k-1}$. This result does not hold for the simulated EM algorithm, however, where the optimal estimates in the class may not be attained in the limit as $K \rightarrow \infty$.

Remark 3. Define $\bar{\theta}_{\text {sto, } K}$ to be the average of the first $K$ iterates in a stochastic em. We obtain the asymptotic expression of $n^{\frac{1}{2}}\left(\bar{\theta}_{\text {sto }, K}-\theta_{0}\right)$ in (A7) when we start with a consistent asymptotic linear $\hat{\theta}_{\boldsymbol{P}}$. As pointed out in the Appendix, the asymptotic variance of $n^{\frac{1}{2}}\left(\bar{\theta}_{\text {sto, } K}-\theta_{0}\right) \rightarrow I_{\text {obs }}^{-1}$ as $n$ and $K \rightarrow \infty$. Equivalent results have been obtained earlier by Diebolt \& Celeux (1993) for $m=1$. For finite $K$, there is no guarantee that $\bar{\theta}_{\text {sto }, K}$ is more efficient than $\hat{\theta}_{\text {sto }, K}$. For both the stochastic and simulated EM algorithms, even greater efficiency can, in principle, be obtained by taking 'optimal' linear combinations of the first $K$ iterates rather than using the $K$ th iterate or the unweighted average.



Remark 4. Tanner (1993, p. 75) suggested starting a stochastic EM algorithm with a small number of imputations, and then increasing the imputation size at a later stage. Our Theorem 4 supports this suggestion by noting that, in $\Sigma_{\text {imp, sto }}^{(K)}$, the contribution of the $k$ th iteration is relatively small for small $k$ since $\left\|J^{K-k}\right\|$ is small. Therefore, for a fixed number of iterations, to improve the efficiency without performing extra imputations one should allocate more imputations to the later iterations. How to allocate the imputation resources efficiently is currently under investigation.

### 4.3. A measurement error example

To demonstrate properties of the stochastic and simulated EM, we study a simple logistic normal measurement error example, in which the true covariate $X$ is $N\left(\mu_{x}, \sigma_{x}^{2}\right)$ distributed; the surrogate $W$ equals $X+U$ with $U$ distributed as $N\left(0, \sigma_{u}^{2}\right)$, independent of $X$; the dichotomous response $D$ follows a logistic model with $E(D \mid X)=H\left(\beta_{0}+\beta_{1} X\right)$ and $H(v)= \{1+\exp (-v)\}^{-1} ; D$ and $W$ are always observed. Subjects are randomly selected into a validation sample with probability $\pi$. The variable $X$ is only observed in the validation sample. For more details about measurement error problems with this data structure, see Carroll, Ruppert \& Stefanski (1995, Ch. 13). The parameter $\theta=\left(\beta_{0}, \beta_{1}, \mu_{x}, \sigma_{x}^{2}, \sigma_{u}^{2}\right)^{\prime}$ is $(0,1,0,1,0 \cdot 5)$, implying a reliability ratio of $66.7 \%$. By using the results in § 4.2, we calculated the asymptotic

![](https://cdn.mathpix.com/cropped/64b5df44-a34d-4975-a559-cb1c5ec9fd60-10.jpg?height=915&width=1016&top_left_y=1135&top_left_x=473)
Fig. 2. Measurement error example. Asymptotic relative efficiencies, are, of $\hat{\beta}_{1}^{(k)}$ with respect to the observed-data maximum likelihood estimator versus the number of iterations $k$. The solid curves and the dashed curves in all plots correspond to the stochastic em estimates with $m=5$ and 10 , respectively; the dotted curves correspond to the simulated em estimates with $m=10$. (a) $\pi=0.25$; (b) as in (a), but replacing the variances in the asymptotic relative efficiency with the sample variances of the estimates in a simulation study, with $n=250$; (c) and (d), as in (a) but with $\pi=0.5$ and 0.1 , respectively.

relative efficiency of $\hat{\beta}_{1}^{(K)}$ with respect to the observed-data maximum likelihood estimator when the initial estimate was the maximum likelihood estimator calculated from the completely observed data in the validation sample. The results are shown in Fig. 2. Note that, if $\pi$ is a known function of the always observed data, $Z=(D, W)$, and it is bounded away from zero, the Horvitz-Thompson estimate (Horvitz \& Thompson, 1952) calculated from the validation sample data could be used as the initial estimate. In Fig. 2, we plot the asymptotic relative efficiency of $\hat{\beta}_{1}^{(K)}$ versus the number of iterations, $K$. The three curves in each plot, from bottom to top, respectively, correspond to the stochastic em with $m=5$, solid curve, the simulated em with $m=10$, dotted curve, and the stochastic em with $m=10$, dashed curve. Figures 2(a), (c) and (d) correspond to the cases where $\pi=0 \cdot 25,0 \cdot 5$ and $0 \cdot 1$, respectively. For this example, our calculations indicate the following: (i) most of the improvement in efficiency is gained in the early iterations; (ii) even with a small number of imputations, $m=5$ or 10 , and a relatively small validation proportion, $\pi=0.1$, the asymptotic relative efficiencies of both estimator are still quite good, that is, above $90 \%$; (iii) although not quite visible in Fig. 2, the maximum asymptotic relative efficiency for the simulated em occurred from the third to the fifth iterations, but nonetheless there is little difference between these maxima and the asymptotic relative efficiencies at the later iterations. We also conducted a small simulation study for $n=250, m=5$ and $10, \pi=0 \cdot 25$, based on 1000 iterations. Estimated asymptotic relative efficiencies, with the calculated variances now replaced by the simulation sample variances, are presented in Fig. 2(b). The simulation result is close to what is suggested by the theory, except that the estimated asymptotic relative efficiency of the simulated em is slightly lower than predicted by our asymptotic theory. Using the completely observed cases only results in a preliminary estimate with $39 \%$ estimated asymptotic relative efficiency. The improvement resulting from even a small number of iterations is obvious.

## Acknowledgement

This research was supported by grants from the National Science Foundation, National Institutes of Health and the Texas Advanced Research program. We thank the editor and two referees, whose comments greatly improved the presentation of the paper.

## Appendix

## Assumptions and proofs

We consider a regular parametric family $\{f(Y ; \theta): \theta \in \Theta\}$, where $\Theta$ is in a finite dimensional Euclidean space. Besides the regularity assumptions we mentioned in the text, we further assume that Assumptions (S1) and (S2) hold for $\theta$ in a neighbourhood of $\theta_{0}$ throughout the proofs.

Assumption (S1). The partial derivative $\partial \log f\left(Y_{R} \mid Y_{R}, \theta\right) / \partial \theta^{\prime}$ exists and is bounded in $L^{2}$.
Assumption (S2). Let $\lambda(\theta, \eta)$ be $E_{\theta}\left[E\left\{S\left(Y_{R}, Y_{R}, \theta\right) \mid Y_{R}, \eta\right\}\right]$, where $E\left(. \mid Y_{R}, \eta\right)$ is the conditional mean given the observed data when the conditional distribution of $Y_{R}$ is $f\left(. \mid Y_{R}, \eta\right)$, and let

$$
\mathscr{T}_{n, \theta}(\tau, \eta)=n^{-\frac{1}{2}}\left|\sum S(\theta, \eta)-\sum S(\theta, \tau)-\lambda(\theta, \eta)+\lambda(\theta, \tau)\right|,
$$

where $S(\theta, \eta)$ is $S\left\{Y_{R}, Y_{R}(\eta) ; \theta\right\}$ defined in § 3. We assume that there exists a positive $d$ such that, for $\theta, \eta$ and $\tau$ in a neighbourhood of $\theta_{0}$, sup ${ }_{|\eta-\tau|<d} \mathscr{R}_{n, \theta}(\tau, \eta) \rightarrow 0$ uniformly in $\theta$ as $n$ goes to $\infty$. We also assume that $(\partial / \partial \eta) \lambda(\theta, \eta)$ exists.

Note that Assumption ( $\mathbf{S} \mathbf{2}$ ) provides a continuity condition which is equivalent to what is assumed in § 4 of Huber (1967). We will now provide sketches of the following proofs.

Proof of Theorem 1. Define $S_{i}(\theta, \tilde{\theta})=m^{-1} \sum_{j} S_{i j}(\theta, \tilde{\theta})$. Then $\hat{\theta}_{B}$ solves $n^{-\frac{1}{2}} \sum S_{i}\left(\theta, \hat{\theta}_{P}\right)=0$. Let $\psi$ be the influence function of $\hat{\theta}_{P}$, that is, $n^{\frac{1}{2}}\left(\hat{\theta}_{P}-\theta_{0}\right)=\sum_{i} n^{-\frac{1}{2}} \psi\left(Y_{R}^{i}, \theta_{0}\right)+o_{p}(1)$. The standard $M$-estimator arguments lead to

$$
n^{\frac{1}{1}}\left(\hat{\theta}_{B}-\theta_{0}\right)=n^{-\frac{1}{2}} \sum_{i=1}^{n}\left[I_{c}^{-1}\left\{S_{i}\left(\theta_{0}, \theta_{0}\right)+\lambda_{2}\left(\theta_{0}, \theta_{0}\right) \psi\left(Y_{R}^{i}, \theta_{0}\right)\right\}\right]+o_{p}(1),
$$

where by Assumption (S2) and similar derivations in Huber (1967), $\lambda_{2}$ is the partial derivative of $\lambda$ with respect to its second argument. Define $S^{\text {mis }}(\theta, \eta)=S(\theta, \eta)-S^{\text {obs }}(\theta)$. By (2.4.1) of Meng \& Rubin (1991), we obtain $S^{\text {mis }}(\theta, \theta)=(\partial / \partial \theta) \log f\left(Y_{R} \mid Y_{R}, \theta\right)$. Therefore, we can write $\lambda_{2}\left(\theta_{0}, \theta_{0}\right)$ as

$$
\left.\int S\left(\theta_{0}, \theta_{0}\right)\left\{(\partial / \partial \eta) f\left(y_{R} \mid Y_{R}, \eta\right) / f\left(y_{R} \mid Y_{R}, \eta\right)\right\} d F\left(y_{R} \mid Y_{R}, \eta\right)\right|_{\eta=\theta_{0}}
$$

which, upon dropping the obvious arguments, is $E\left\{S\left(S^{\text {mis }}\right)^{\prime} \mid Y_{R}\right\}$. The fact that $E\left\{S^{\text {obs }}\left(S^{\text {mis }}\right)^{\prime}\right\}= E\left[E\left\{S^{\text {obs }}\left(S-S^{\text {obs }}\right)^{\prime}\right\} \mid Y_{R}\right]=0$, with some simple derivations implies that $\lambda_{2}\left(\theta_{0}, \theta_{0}\right)=I_{\text {mis }}$. Write $S_{i}=S_{i}^{\text {obs }}+S_{i}^{\text {mis }}$ and define $\rho_{i}$ to be $\psi\left(Y_{R}^{i}, \theta_{0}\right)-I_{\text {obs }}^{-1} S_{i}^{\text {obs }}$. The influence function of $\hat{\theta}_{B}$ in (A1) can be written as $I_{c}^{-1}\left(I+I_{\text {mis }} I_{\text {obs }}^{-1}\right) S_{i}^{\text {obs }}+I_{c}^{-1} S_{i}^{\text {mis }}+J^{\prime} \rho_{i} ; I$ is the identity matrix. The fact that $S^{\text {obs }}, S^{\text {mis }}$ and $\rho$ are mutually orthogonal, and the equality

$$
I+I_{\mathrm{mis}} I_{\mathrm{obs}}^{-1}=I_{c} I_{\mathrm{obs}}^{-1}
$$

imply the resulting variance in (1).
Proof of Theorem 2. By similar derivations to those leading to Theorem 1, we obtain

$$
n^{\frac{1}{2}}\left(\hat{\theta}_{A}-\theta_{0}\right)=n^{-\frac{1}{2}} \sum_{i=1}^{n} I_{\mathrm{ob} i}^{-1} S_{i}^{\mathrm{obs}}+m^{-1} \sum_{j=1}^{m}\left(n^{-\frac{1}{1}} \sum_{i=1}^{n} I_{c}^{-1} S_{i j}^{\mathrm{mis}}\right)+m^{-1} \sum_{j=1}^{m}\left(n^{\frac{1}{2}} J^{\prime} V_{j}\right)+o_{p}(1)
$$

where $S_{i j}^{\mathrm{mis}}=S_{i j}-S_{i j}^{\mathrm{obs}} ; V_{j}=\tilde{\theta}_{j}-\hat{\theta}_{\mathrm{MLE}}$; and $\tilde{\theta}_{j}$, as defined in § 3, are independent draws from the posterior density of $\theta$ given the observed $Z$. Under the standard regularity conditions in § 3.2, given $Z, m^{-1} \sum\left(n^{\frac{1}{2}} J^{\prime} V_{j}\right)$ converges, almost surely on $Z$, to an asymptotic normal with mean zero and variance $m^{-1} J^{\prime} I_{\text {obs }}^{-1} J$. The sum of the first two terms in (A3) converges unconditionally to an asymptotic normal with mean zero and variance $I_{\mathrm{obs}}^{-1}+m^{-1} I_{c}^{-1} J$. Theorem 2 thus follows from Lemma 1 of Schenker \& Welsh (1988), which implies that the asymptotic distribution of $n^{\frac{1}{2}}\left(\hat{\theta}_{A}-\theta_{0}\right)$ is the convolution of the two normal distributions above. $\square$

Proof of (3) and (4). To prove (3), it is sufficient to show that $I_{\text {obs }}^{-1}-I_{c}^{-1}=I_{c}^{-1} J+J^{\prime} I_{\text {obs }}^{-1} J$. The right-hand side of the equation equals $I_{c}^{-1}\left(I+I_{\text {mis }} I_{\text {obs }}^{-1}\right) I_{\text {mis }} I_{c}^{-1}$, which by (A2) is $I_{\mathrm{obs}}^{-1}\left(I_{c}-I_{\mathrm{obs}}\right) I_{c}^{-1}$; we thus obtain (3). To prove (4), by the law of large numbers it is sufficient to show that, when $m \rightarrow \infty, \tilde{Q}_{A}$ converges to $I_{c}^{-1} J+J^{\prime} I_{\text {obs }}^{-1} J$. Write $\tilde{Q}_{A}$ as

$$
(m-1)^{-1} \sum_{j}\left[n^{\frac{1}{2}}\left\{\left(\hat{\theta}_{A j}-\theta_{0}\right)-\left(\bar{\theta}_{A}-\theta_{0}\right)\right\}\right]^{\otimes 2}
$$

Straightforward derivations further show that

$$
\tilde{Q}_{A}=(m-1) \sum\left\{n^{\frac{1}{2}} J^{\prime}\left(V_{j}-\bar{V}\right)\right\}^{\otimes 2}+\{n(m-1)\}^{-1} \sum \sum\left\{I_{c}^{-1}\left(S_{i j}^{\mathrm{mis}}-\bar{S}_{i}^{\mathrm{mis}}\right)\right\}^{\otimes 2}+o_{p}(1),
$$

where $V_{j}$ is defined at (A3); $\bar{V}$ is the average of the $m V_{j}$ 's and $\bar{S}_{i}^{\mathrm{mis}}$ is defined analogously. When both $n$ and $m$ go to infinity, it is easy to show that the first term above converges to $J^{\prime} I_{\text {obs }}^{-1} J$ while the second term converges to $I_{c}^{-1} J$. $\square$

Influence function for $\hat{\theta}_{\text {sto }, K}$ and $\hat{\theta}_{\text {sim }, K}$. Note that, with $J^{0}=I$,

$$
\sum_{k=1}^{K} J^{k-1}+I_{c}\left(J^{K}\right)^{\prime} I_{\mathrm{obs}}^{-1} \equiv I_{c} I_{\mathrm{obs}}^{-1}
$$

which can be proved easily by induction on $K$. By iterative substitutions into (A1) and by applying (A4), we have

$$
n^{\frac{1}{2}}\left(\hat{\theta}_{\mathrm{sto}, K}-\theta_{0}\right)=n^{-\frac{1}{2}} \sum_{i=1}^{n} I_{\mathrm{obs}}^{-1} S_{i}^{\mathrm{obs}}+n^{-\frac{1}{2}} \sum_{i=1}^{n}\left(\sum_{k=1}^{K} m_{k}^{-1} I_{c}^{-1} J^{K-k} S_{l}^{\mathrm{mis},(k)}\right)+n^{-\frac{1}{2}} \sum_{i=1}^{n}\left(J^{K}\right)^{\prime} \rho_{i}+o_{p}(1),
$$

where $S^{\mathrm{mis},(k)}$ is the $S^{\mathrm{mis}}$ component of the $k$ th iterate, and $\rho_{i}$ is defined in the proof of Theorem 1. Similarly,

$$
n^{\frac{1}{2}}\left(\hat{\theta}_{\operatorname{sim}, K}-\theta_{0}\right)=n^{-\frac{1}{2}} \sum_{i=1}^{n} I_{\mathrm{obs}}^{-1} S_{i}^{\mathrm{obs}}+n^{-\frac{1}{2}} \sum_{i=1}^{n} m^{-1} I_{c}^{-1}\left(\sum_{k=1}^{K} J^{K-k}\right) S_{i}^{\mathrm{mis},(1)}+n^{-\frac{1}{2}} \sum_{i=1}^{n}\left(J^{K}\right)^{\prime} \rho_{i}+o_{p}(1) .
$$

Proof of Corollary 2. To show that $V_{\text {sim }, K}-V_{\text {sto }, K}$ is positive semidefinite, we only need to show that $\Sigma_{\text {imp, sim }}^{(K)}-\Sigma_{\text {imp, ato }}^{(K)}$ is positive semidefinite, which, by using the fact that $J^{k_{1}} I_{\text {mis }}\left(J^{k_{2}}\right)^{\prime}$ is positive semidefinite for any two nonnegative integers $k_{1}$ and $k_{2}$ can be easily obtained by induction. Note that $J^{k_{1}} I_{\text {mis }}\left(J^{k_{2}}\right)^{\prime}$ equals $M I_{c}^{-1} M^{\prime}$ for some matrix $M$ when $k_{1}+k_{2}$ is odd, and equals $M I_{\text {mis }} M^{\prime}$ when $k_{1}+k_{2}$ is even, which implies that it is always positive semidefinite.

To show (i) and (ii) in Corollary 2, we need the following lemma, which we state first and prove afterwards.

Lemma A1. Consider the norm of a matrix to be the largest absolute value of all elements in the matrix. Then, when $k$ goes to $\infty,\left\|J^{k}\right\| \rightarrow 0$.

Proof. Since $I_{c}$ and $I_{\text {mis }}$ are real symmetric matrices and $I_{c}$ is positive definite, there exists a nonsingular matrix $R$ such that $I_{\text {mis }}=R^{\prime} \Lambda R$ and $I_{c}=R^{\prime} R$, where $\Lambda$ is a diagonal matrix with $i$ th diagonal element $\lambda_{i}$ (Rao, 1985, p. 41). Since $I_{\text {obs }}=I_{c}-I_{\text {mis }}$ is positive definite, it implies that the $\lambda_{i}$ 's are all less than 1 . The result follows since $J^{K}=\left(I_{\text {mix }} I_{c}^{-1}\right)^{K}=R^{\prime}(\Lambda)^{K}\left(R^{-1}\right)^{\prime}$.

By Lemma A1, $\left\|\Sigma_{p}^{(\boldsymbol{K})}\right\|$ goes to zero. To find the limit of $V_{\text {sim }, \boldsymbol{K}}$ and $V_{\text {sto, } \boldsymbol{K}}$, we only need to find the limit of $\Sigma_{\text {imp, sim }}^{(K)}$ and $\Sigma_{\text {imp, sto }}^{(K)}$. The results claimed in Corollary 2 can be easily obtained by noting that $I-J=I_{\mathrm{obs}} I_{c}^{-1}$, and that

$$
\left(\sum_{k=1}^{K} J^{K-k}\right)(I-J)=I-J^{K}, \quad \sum_{k=1}^{K}\left\{I_{c}^{-1} J^{K-k} I_{\mathrm{mis}}\left(J^{K-k}\right)^{\prime} I_{c}^{-1}\right\}\left(I-J^{2}\right)=I_{c}^{-1} I_{\mathrm{mis}} I_{c}^{-1}-I_{c}^{-1} K^{2 K+1}
$$

Influence function for $\bar{\theta}_{\text {sto, } \boldsymbol{K}}$. By (A5), we have

$$
\begin{aligned}
n^{\frac{1}{2}}\left(\bar{\theta}_{\mathrm{sto}, K}-\theta_{0}\right)= & n^{-\frac{1}{2}} \sum_{i=1}^{n} I_{\mathrm{ob} z}^{-1} S_{i}^{\mathrm{ob} z}+n^{-\frac{1}{2}} \sum_{i=1}^{n}(m K)^{-1} I_{c}^{-1}\left\{\sum_{k=1}^{K}\left(\sum_{l=0}^{K-k} J^{l}\right) S_{i}^{\mathrm{mis},(k)}\right\} \\
& +n^{-\frac{1}{2}} \sum_{i=1}^{n}\left\{K^{-1} \sum_{k=1}^{K}\left(J^{k}\right)^{\prime}\right\} \rho_{i}+o_{p}(1)
\end{aligned}
$$

Straightforward calculations imply that, when $n$ and $K \rightarrow \infty$, the variances of the second and third terms in (A7) go to 0 , that is the asymptotic variance of $n^{\frac{1}{2}}\left(\bar{\theta}_{\text {sto }, K}-\theta_{0}\right) \rightarrow I_{\text {obs }}^{-1}$.

## References

Billingsley, P. (1968). Convergence of Probability Measures. New York: Wiley.
Carroll, R. J., Ruppert, D. \& Stefanski, L. A. (1995). Measurement Error in Non-linear Models. London: Chapman and Hall.
Celeux, G. \& Diebolt, J. (1985). The sem algorithm: a probabilistic teacher algorithm derived from the em algorithm for the mixture problem. Comp. Statist. Quart. 2, 73-82.
Deltour, I., Richardson, S. \& Le Hesran, J. L. (1999). Stochastic algorithms for Markov models estimation with intermittent missing data. Biometrics. To appear.
Diebolt, J. \& Celeux, G. (1993). Asymptotic properties of a stochastic em algorithm for estimating mixing proportions. Commun. Statist. B 9, 599-613.
Diebolt, J. \& Ip, E. H. S. (1996). Stochastic em: method and application. In Markov Chain Monte Carlo in Practice, Ed. W. R. Gilks, S. Richardson and D. J. Spiegelhalter, pp. 259-68. New York: Springer-Verlag.
Fay, R. (1996). Alternative paradigms for the analysis of imputed survey data. J. Am. Statist. Assoc. 91, 490-8.
Greenland, S. \& Finkle, W. D. (1995). A critical look at basic methods for handling missing covariates in epidemiologic regression analyses. Am. J. Epidem. 142, 1255-64.

Horvitz, D. G. \& Thompson, D. J. (1952). A generalization of sampling without replacement from a finite universe. J. Am. Statist. Assoc. 47, 663-85.
Huber, P. J. (1967). The behavior of maximum likelihood estimates under nonstandard conditions. In Proc. 5th Berkeley Symp. Math. Statist. Prob., 1, pp. 221-33.
McFadden, D. \& Rudd, P. A. (1994). Estimation by simulation. Rev. Econ. Statist. 76, 591-608.
Meng, X. L. (1994). Multiple imputation inferences with uncongenial sources of input. Statist. Sci. 9, 538-58.
Meng, X. L. \& Rubin, D. B. (1991). Using em to obtain asymptotic variance-covariance matrices: the sem algorithm. J. Am. Statist. Assoc. 86, 899-909.
Rao, C. R. (1985). Linear Statistical Inference and its Applications, 2nd ed. New York: Wiley.
Reilly, M. (1993). Data analysis using hot-deck multiple imputation. Statistician 42, 307-13.
Robins, J. M. \& Gill, R. D. (1997). Non-response models for the analysis of non-monotone ignorable missing data. Statist. Med. 16, 39-56.
Rubin, D. B. (1978). Multiple imputation in sample surveys-a phenomenological Bayesian approach to nonresponse. In Proc. Survey Res. Meth. Sect., Am. Statist. Assoc. pp. 20-34. Washington, DC: American Statistical Association.
Rubin, D. B. (1987). Multiple Imputation for Nonresponse in Surveys. New York: Wiley.
Rubin, D. B. (1996). Multiple imputation after 18 years. J. Am. Statist. Assoc. 91, 473-90.
Ruud, P. A. (1991). Extensions of estimation methods using the em algorithm. J. Economet. 49, 305-41.
Schenker, N. \& Welsh, A. H. (1988). Asymptotic results for multiple imputation. Ann. Statist. 16, 1550-66.
Tanner, M. A. (1993). Tools for Statistical Inference. New York: Springer-Verlag.
Wei, G. C. G. \& Tanner, M. A. (1990). A Monte Carlo implementation of the em algorithm and the poor man's data augmentation algorithms. J. Am. Statist. Assoc. 85, 699-704.
[Received March 1997. Revised January 1998]

