---
citekey: nielsenProperImproperMultiple2003
item_type: article
authors: 'Nielsen, S\oren Feodor'
year: 2003
title: 'Proper and {Improper Multiple Imputation}'
venue: International Statistical Review
volume: 71
issue: 3
pages: 593--607
doi: 10.1111/j.1751-5823.2003.tb00214.x
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\nielsen_proper_improper_multiple_2003.pdf'
pdf_sha256: 7e764f466cfdb0fd45721772aa4f5b56a72eb4a3301b7e5ee671c0969c17388c
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T15:21:35Z
---
# Proper and Improper Multiple Imputation 

Søren Feodor Nielsen<br>Department of Applied Mathematics and Statistics, University of Copenhagen, Universitetsparken 5, DK-2100 København Ø, Denmark


#### Abstract

Summary Multiple imputation has become viewed as a general solution to missing data problems in statistics. However, in order to lead to consistent asymptotically normal estimators, correct variance estimators and valid tests, the imputations must be proper. So far it seems that only Bayesian multiple imputation, i.e. using a Bayesian predictive distribution to generate the imputations, or approximately Bayesian multiple imputations has been shown to lead to proper imputations in some settings. In this paper, we shall see that Bayesian multiple imputation does not generally lead to proper multiple imputations. Furthermore, it will be argued that for general statistical use, Bayesian multiple imputation is inefficient even when it is proper.


Key words: Missing data; Multiple imputation; Congeniality; Efficiency.

## 1 Multiple Imputation

Missing-or incomplete-data is a problem to most applications of statistics. It is well-known that we have to be very careful when analysing incomplete data; using ad hoc methods often gives the wrong answer. However, many sophisticated methods for handling missing data correctly exist. Lately, multiple imputation has become viewed as a general answer to missing data problems; see for instance the book by Schafer (1997) or the paper by Rubin (1996).

Multiple imputation was originally introduced as a method for handling missing data in surveys. As many other types of data, survey data is prone to missingness. It differs from most other kinds of data, however, in that it often ends up in large databases, where many different users have access to and analyse the data. Naturally, it would be preferred that different users get the same answer if they perform the same statistical analysis on the data. This is ensured when the missing data is imputed. Furthermore, by performing the imputation "at the data base", the imputer may be able to generate better imputations than the individual user would be able to, using additional information which is not revealed to the public either for confidentiality reasons or simply because it is deemed irrelevant to the user. (Even if irrelevant, it may be very useful for imputing missing data.) Finally, by imputing the missing data, the data base will appear to be complete and allow the users to analyse the data using complete data methods. Unfortunately, analysing imputed data as if it was real data generally leads to variance estimates that are too low, confidence intervals which are too narrow, and wrong tests (real significance level above nominal level). Intuitively, this is due to the fact that imputation does not generate information which is not already present in the data; hence the sample size is the same for the incomplete data and for the imputed ("pseudo-complete") data. Multiple imputation has been suggested as a way of overcoming this problem. By multiply imputing the missing data-i.e. by imputing $m>1$ values for the missing data-the analyser can perform $m$ complete data analyses and use the results to correct for the variability in the imputations, which differs from the variability in the observed data.

The key to the success of multiple imputation is the concept of proper multiple imputation. If the multiple imputations are proper then the average of the estimators is a consistent, asymptotically normal estimator, and an estimator of its asymptotic variance is given by a simple combination of the average of the complete data variance estimators and the empirical variance of the $m$ estimators (the "between imputation variance") according to "Rubin’s rule" (see Section 2). Rubin (1987) gives a precise definition of proper multiple imputation but for practical purposes it suffices to define proper multiple imputation to be multiple imputations for which "Rubin's rule" yields a consistent asymptotically normal estimator of the unknown parameter and a weakly unbiased (see Section 2) estimator of its asymptotic variance in sufficiently regular models. We note that whether or not imputations are proper is related to the frequentist properties of the resulting estimator. Indeed, we shall focus on the frequentist properties of multiple imputation in this paper.

It seems to be generally believed that imputations drawn from a Bayesian predictive distribution are proper when the model used for the imputations and the model used for the analysis are "compatible". In this paper we will show that such Bayesian imputations are not generally proper even if the two models are "the same". Furthermore, we will argue that even when the imputations are proper, multiple imputation is a highly inefficient way of handling missing data outside the world of survey data.

## 2 Large Sample Results

We start by outlining some large sample results for Bayesian multiple imputation in a setting where it is proper. To get the desired asymptotic results we shall use the following result repeatedly:

LEMMA 1. Let $\mathbf{Y}=\left(Y_{n}\right)_{n \in \mathbb{N}}$ be a sequence of random variables. Suppose that for a sequence of functions, $\left(f_{n}\right)_{n \in \mathbb{N}}$ and a sequence of $d$-dimensional real random variables $\left(Z_{n}\right)_{n \in \mathbb{N}}$

$$
\sqrt{n}\left(Z_{n}-f_{n}\left(Y_{1}, \ldots, Y_{n}\right)\right) \xrightarrow{\mathcal{D}} N\left(0, \Sigma_{1}\right) \quad \text { given } \mathbf{Y} \text { for almost every } \mathbf{Y}
$$

and

$$
\sqrt{n}\left(f_{n}\left(Y_{1}, \ldots, Y_{n}\right)-\xi_{n}\right) \xrightarrow{\mathcal{D}} N\left(0, \Sigma_{2}\right)
$$

for some $\xi_{n} \in \mathbb{R}^{d}$ and $d \times d$-matrices $\Sigma_{1}$ and $\Sigma_{2}$. Then

$$
\sqrt{n}\left(Z_{n}-\xi_{n}\right) \xrightarrow{\mathcal{D}} N\left(0, \Sigma_{1}+\Sigma_{2}\right)
$$

Proof. It suffices to show convergence of the characteristic function of $\sqrt{n}\left(Z_{n}-\xi_{n}\right)$. For any $s \in \mathbb{R}^{d}$

$$
\begin{aligned}
& E\left[\exp \left(i s^{t} \sqrt{n}\left(Z_{n}-\xi_{n}\right)\right)\right] \\
& \qquad \begin{array}{l}
=E\left[E \left[\exp \left(i s^{t} \sqrt{n}\left(Z_{n}-f_{n}\left(Y_{1}, \ldots, Y_{n}\right)\right) \mid \mathbf{Y}\right]\right.\right. \\
\left.\quad \cdot \exp \left(i s^{t} \sqrt{n}\left(f_{n}\left(Y_{1}, \ldots, Y_{n}\right)-\xi_{n}\right)\right)\right]
\end{array} \\
& \quad=\exp \left(-s^{t} \Sigma_{1} s\right) E\left[\exp \left(i s^{t} \sqrt{n}\left(f_{n}\left(Y_{1}, \ldots, Y_{n}\right)-\xi_{n}\right)\right)\right] \\
& \quad+E\left[\left(E\left[\exp \left(i s^{t} \sqrt{n}\left(Z_{n}-f_{n}\left(Y_{1}, \ldots, Y_{n}\right)\right) \mid \mathbf{Y}\right]-\exp \left(-s^{t} \Sigma_{1} s\right)\right)\right.\right. \\
& \left.\quad \cdot \exp \left(i s^{t} \sqrt{n}\left(f_{n}\left(Y_{1}, \ldots, Y_{n}\right)-\xi_{n}\right)\right)\right] \\
& \quad \rightarrow \exp \left(-s^{t} \Sigma_{1} s\right) \exp \left(-s^{t} \Sigma_{2} s\right)+0=\exp \left(-s^{t}\left(\Sigma_{1}+\Sigma_{2}\right) s\right) \text { as } n \rightarrow \infty
\end{aligned}
$$

proving the result. $\square$

Remark. Lemma 1 is a special case of (a part of) Lemma 1 in Schenker \& Welsh (1988); the proof is simpler. It is included to make this paper self-contained.

Let $X_{1}, \ldots, X_{n}$ be iid random variables (the complete data) with a distribution depending on an unknown parameter $\theta \subseteq \Theta \in \mathbb{R}^{d}$; the true value is denoted $\theta_{0}$. We let $s_{X}(\theta)$ denote the corresponding score function (the derivative of the log-likelihood) and let $V(\theta)=E\left[s_{X}(\theta)^{\otimes 2}\right]$ denote the expected Fisher information.

Rather than observing $X_{1}, \ldots, X_{n}$ we assume we observe $Y_{1}, \ldots, Y_{n}$. Typically, $Y_{i}$ is $X_{i}$ if $X_{i}$ is observed and an indicator of missingness if $X_{i}$ is missing. More generally, $Y_{i}$ could be a random subset of $X_{i}$ 's sample space, i.e. a coarsening of $X_{i}$ (see Heitjan \& Rubin, 1991; Nielsen, 2000). For instance, with right censored data $Y_{i}$ would be $\left\{X_{i}\right\}$ if $X_{i}$ is observed and $\left[C_{i} ; \infty\left[\right.\right.$ if $X_{i}$ is censored at $C_{i}$. We assume that the $Y_{i} \mathrm{~s}$ are independent, and that the missing data (or coarsening) mechanism does not depend on $\theta$. Hence the distribution (and the likelihood) of the observed data will in general depend on $\theta$ and on an additional (possibly high-dimensional or even non-Euclidean) parameter. Under missing (or coarsening) at random, the observed data likelihood is a product of a factor only dependent on $\theta$ and a factor depending on the parameter of the missing data (or coarsening) mechanism. As a consequence, the score function also has a $\theta$-part and a "non- $\theta$ "-part. Thus for estimating $\theta$ the "non- $\theta$ "-part may be ignored. We let $s_{Y}(\theta)$ denote the $\theta$-part of the score function corresponding to the observed data and $I(\theta)$ the expected Fisher information. Without missing (or coarsening) at random, the "non- $\theta$ "-part cannot be ignored; in this case we let $\theta$ denote the concatenation of the interest parameter (the parameter indicing the distribution of $X_{i}$ ) and the nuisance parameter from the missing data mechanism.

Finally, we let $s_{X \mid Y}(\theta)=s_{X}(\theta)-s_{Y}(\theta)$ and put $I_{Y}(\theta)=E\left[s_{X \mid Y}(\theta)^{\otimes 2} \mid Y\right]$ so that $E I_{Y}(\theta)= V(\theta)-I(\theta)$.

We assume standard regularity assumptions on both the complete data model and the observed data model. In particular, the observed data MLE, $\hat{\theta}_{n}$, is a solution to the likelihood equations, $1 / n \sum_{i=1}^{n} s_{y_{i}}(\theta)=0$, and it is asymptotically normal with mean $\theta_{0}$ and variance $I\left(\theta_{0}\right)^{-1} / n$.

To generate the imputation we shall also need a prior distribution on the parameter set $\Theta$. As we are interested in frequentist properties, the prior is a tool and does not (necessarily) represent degrees of belief in the unknown parameter. Using the density function of the observed data as if it is the conditional distribution of the observed data given the parameters, we can in principle find the posterior distribution of the parameters, i.e. the conditional distribution of the parameters given the observed data, using Bayes formula; in practice this will typically be very difficult and require simulation. Again, since we are interested in frequentist properties, the posterior is a tool and does not represent degrees of belief. By the Bernstein-von Mises theorem, the posterior distribution given the observed data is asymptotically normal with mean equal to the observed data MLE and the inverse Fisher information, $I\left(\theta_{0}\right)^{-1} / n$, as asymptotic variance for any reasonable prior under weak regularity assumptions (see e.g. van der Vaart, 1998, Theorem 10.1). Finally, we shall need the Bayesian predictive distribution. This is the distribution of the missing data given the observed data with the parameters integrated out using the prior distribution. The imputations, we shall consider here, are simulations from this predictive distribution. In principle, these can be simulated by first simulating $\tilde{\theta}_{n j}$ from the posterior distribution and then sampling $\tilde{X}_{i j}$ independently from the distribution $\mathcal{L}_{\tilde{\theta}_{n j}}\left(X_{i} \mid Y_{i}=y_{i}\right)$ for $i=1, \ldots, n, j=1, \ldots, m$. From a purely theoretical point of view we may and will assume that the imputations are generated in this way. In practice, simulating from the predictive distribution is usually very difficult, requiring iterative methods such as Markov chains. We shall return to this point in Section 5.

Now, for $j=1, \ldots, m$, let the imputations $\left(\widetilde{X}_{i j}\right)_{i=1, \ldots, n}$ be drawn from the Bayesian predictive distribution generated as described above by first simulating $\tilde{\theta}_{n j}$ from the posterior distribution and
then simulating from $\widetilde{X}_{i j}$ from $\mathcal{L}_{\tilde{\theta}_{n j}}\left(X_{i} \mid Y_{i}=y_{i}\right)$ for $i=1, \ldots, n$. These $m$ sets of imputations are used to form the $m$ complete data MLEs, $\hat{\theta}_{n j}$, given as the solutions to the $m$ likelihood equations

$$
\frac{1}{n} \sum_{i=1}^{n} s_{\tilde{X}_{i j}}\left(\hat{\theta}_{n j}\right)=0, \quad j=1, \ldots, m
$$

Then Taylor expanding for each $j=1, \ldots, m$

$$
\begin{aligned}
0= & \frac{1}{\sqrt{n}} \sum_{i=1}^{n} s_{\widetilde{X}_{i j}}\left(\hat{\theta}_{n j}\right) \\
= & \frac{1}{\sqrt{n}} \sum_{i=1}^{n} s_{\widetilde{X}_{i j}}\left(\hat{\theta}_{n}\right)+\frac{1}{n} \sum_{i=1}^{n} D_{\theta} s_{\widetilde{X}_{i j}}\left(\hat{\theta}_{n j}^{*}\right) \sqrt{n}\left(\hat{\theta}_{n j}-\hat{\theta}_{n}\right) \\
= & \frac{1}{\sqrt{n}} \sum_{i=1}^{n} s_{\widetilde{X}_{i j} \mid y_{i}}\left(\hat{\theta}_{n}\right)+\frac{1}{\sqrt{n}} \sum_{i=1}^{n} s_{y_{i}}\left(\hat{\theta}_{n}\right) \\
& \quad+\frac{1}{n} \sum_{i=1}^{n} D_{\theta} s_{\widetilde{X}_{i j}}\left(\hat{\theta}_{n j}^{*}\right) \sqrt{n}\left(\hat{\theta}_{n j}-\hat{\theta}_{n}\right) \\
= & \frac{1}{\sqrt{n}} \sum_{i=1}^{n} s_{\widetilde{X}_{i j} \mid y_{i}}\left(\tilde{\theta}_{n j}\right)+\frac{1}{n} \sum_{i=1}^{n} D_{\theta} s_{\widetilde{X}_{i j} \mid y_{i}}\left(\tilde{\theta}_{n j}^{*}\right) \sqrt{n}\left(\hat{\theta}_{n}-\tilde{\theta}_{n j}\right) \\
& \quad+\left(\frac{1}{n} \sum_{i=1}^{n} D_{\theta} s_{\widetilde{X}_{i j} \mid y_{i}}\left(\hat{\theta}_{n j}^{*}\right)+\frac{1}{n} \sum_{i=1}^{n} D_{\theta} s_{y_{i}}\left(\hat{\theta}_{n j}^{*}\right)\right) \sqrt{n}\left(\hat{\theta}_{n j}-\hat{\theta}_{n}\right)
\end{aligned}
$$

where $\hat{\theta}_{n j}^{*}\left(\tilde{\theta}_{n j}^{*}\right)$ is a point on the line from $\hat{\theta}_{n}$ to $\hat{\theta}_{n j}\left(\tilde{\theta}_{n j}\right)$. Here as $n \rightarrow \infty$ (under suitable regularity conditions; see appendix for a discussion)

$$
\begin{aligned}
\frac{1}{n} \sum_{i=1}^{n} D_{\theta} s_{\tilde{X}_{i j} \mid y_{i}}\left(\tilde{\theta}_{n j}^{*}\right) & \rightarrow E I_{Y}\left(\theta_{0}\right) \\
\frac{1}{n} \sum_{i=1}^{n} D_{\theta} s_{\tilde{X}_{i j} \mid y_{i}}\left(\hat{\theta}_{n j}^{*}\right)+\frac{1}{n} \sum_{i=1}^{n} D_{\theta} s_{y_{i}}\left(\hat{\theta}_{n j}^{*}\right) & \rightarrow E I_{Y}\left(\theta_{0}\right)+I\left(\theta_{0}\right)=V\left(\theta_{0}\right)
\end{aligned}
$$

whereas

$$
\frac{1}{\sqrt{n}} \sum_{i=1}^{n} s_{\tilde{X}_{i j} \mid y_{i}}\left(\tilde{\theta}_{n j}\right) \xrightarrow{\mathcal{D}} N\left(0, E I_{Y}\left(\theta_{0}\right)\right)
$$

conditional on the observed data and $\tilde{\theta}_{n j}$.
It now follows that conditional on the observed data and $\tilde{\theta}_{n j}$

$$
\sqrt{n}\left(\hat{\theta}_{n j}-\hat{\theta}_{n}\right)-F\left(\theta_{0}\right)^{t} \sqrt{n}\left(\tilde{\theta}_{n j}-\hat{\theta}_{n}\right) \xrightarrow{\mathcal{D}} N\left(0, V\left(\theta_{0}\right)^{-1} E I_{Y}\left(\theta_{0}\right) V\left(\theta_{0}\right)^{-1}\right)
$$

where $F\left(\theta_{0}\right)=E I_{Y}\left(\theta_{0}\right) V\left(\theta_{0}\right)^{-1}$ for each $j=1, \ldots, m$. Hence, given the observed data only,

$$
\sqrt{n}\left(\hat{\theta}_{n j}-\hat{\theta}_{n}\right) \xrightarrow{\mathcal{D}} N\left(0, F\left(\theta_{0}\right)^{t} I\left(\theta_{0}\right)^{-1} F\left(\theta_{0}\right)+V\left(\theta_{0}\right)^{-1} E I_{Y}\left(\theta_{0}\right) V\left(\theta_{0}\right)^{-1}\right)
$$

by Lemma 1. Moreover, given the observed data, $\hat{\theta}_{n 1}, \ldots, \hat{\theta}_{n m}$ are independent. Straightforward manipulations (multiply by $V\left(\theta_{0}\right)$ from both sides) yield

$$
F\left(\theta_{0}\right)^{t} I\left(\theta_{0}\right)^{-1} F\left(\theta_{0}\right)+V\left(\theta_{0}\right)^{-1} E I_{Y}\left(\theta_{0}\right) V\left(\theta_{0}\right)^{-1}=I\left(\theta_{0}\right)^{-1}-V\left(\theta_{0}\right)^{-1} .
$$

Putting $\bar{\theta}_{n}=\frac{1}{m} \sum_{j=1}^{m} \hat{\theta}_{n j}$, continuous mapping and the partitioning theorem give us (conditional on the observed data)

$$
\sqrt{n}\left(\bar{\theta}_{n}-\hat{\theta}_{n}\right) \xrightarrow{\mathcal{D}} N\left(0, \frac{1}{m}\left(I\left(\theta_{0}\right)^{-1}-V\left(\theta_{0}\right)^{-1}\right)\right)
$$

and

$$
\frac{n}{m-1} \sum_{j=1}^{m}\left(\hat{\theta}_{n j}-\bar{\theta}_{n}\right)^{\otimes 2} \xrightarrow{\mathcal{D}} \text { Wishart }\left(m-1, \frac{1}{m-1}\left(I\left(\theta_{0}\right)^{-1}-V\left(\theta_{0}\right)^{-1}\right)\right)
$$

which are asymptotically independent. Notice also that the asymptotic distribution of $\frac{1}{m-1} \sum_{j=1}^{m} n\left(\hat{\theta}_{n j}-\bar{\theta}_{n}\right)^{\otimes 2}$ does not depend on the observed data. Thus (2) also holds unconditionally. Finally, (1) and Lemma 1 gives us

$$
\sqrt{n}\left(\bar{\theta}_{n}-\theta_{0}\right) \xrightarrow{\mathcal{D}} N\left(0, I\left(\theta_{0}\right)^{-1}+\frac{1}{m}\left(I\left(\theta_{0}\right)^{-1}-V\left(\theta_{0}\right)^{-1}\right)\right) .
$$

Let $\hat{V}_{n}$ be a (consistent) estimator of the complete data Fisher information based on the complete data. Let $\hat{V}_{n j}$ be the same estimator based on the observed data and the $j$ th set of imputations. Then

$$
\begin{aligned}
\hat{\Sigma}_{n} & =\frac{1}{m} \sum_{j=1}^{m} \hat{V}_{n j}^{-1}+\left(1+\frac{1}{m}\right) \frac{n}{m-1} \sum_{j=1}^{m}\left(\hat{\theta}_{n j}-\bar{\theta}_{n}\right)^{\otimes 2} \\
& \leadsto V\left(\theta_{0}\right)^{-1}+\left(1+\frac{1}{m}\right)\left(I\left(\theta_{0}\right)^{-1}-V\left(\theta_{0}\right)^{-1}\right) \text { as } n \rightarrow \infty \\
& =I\left(\theta_{0}\right)^{-1}+\frac{1}{m}\left(I\left(\theta_{0}\right)^{-1}-V\left(\theta_{0}\right)^{-1}\right)
\end{aligned}
$$

estimates the asymptotic variance of $\bar{\theta}_{n}$. The notation " $Z_{n} \leadsto \alpha$ " is used to denote that $Z_{n}$ converges in distribution and that the limiting distribution has mean $\alpha$. We will call such an estimator weakly unbiased for $\alpha$. Indeed it should be noted that $\hat{\Sigma}_{n}$ is not consistent (as $n \rightarrow \infty$ ); rather its asymptotic distribution is the Wishart distribution given in (2) shifted (by $I\left(\theta_{0}\right)^{-1}$ ) so that it has the correct mean. To account for the variability in the variance estimator it is generally recommended that Wald type tests and confidence intervals are based on a $t$ - (or $F$-) distribution with degrees of freedom based on a Satterthwaite approximation (see e.g. Schafer, 1997) rather than a normal distribution. One should be aware that the asymptotic distribution of the Wald test statistic is non-standard and non-similar: As $I\left(\theta_{0}\right) \rightarrow V\left(\theta_{0}\right)$, corresponding to no missing information, the distribution of the Wald test statistic tends to a $\chi^{2}$-distribution.

Basically "Rubin's Rule" boils down to this: Impute $m$ datasets and perform $m$ complete data analyses to get $m$ estimators of $\theta$ and $m$ corresponding variance estimators. Average the estimators of the unknown parameters to get the point estimate (cf. (3)) and estimate the variance matrix by the average of the variance estimators from the complete data analyses and $1+1 / m$ times the empirical variance of the $m$ estimators of $\theta$ (cf. (4)).

If the imputations are proper, then "Rubin's rule" yields a weakly unbiased estimator of the variance. The argument above shows that Bayesian multiple imputations are proper, when the complete data estimator is the complete data MLE.

Remark. The argument given above leading to the frequentist large sample justification of Bayesian multiple imputation may be seen as a more explicit formulation of the argument given by Rubin (1987, Section 4.5). Robins \& Wang (2000) give a more general argument.

In many practical examples, one would be interested in less than the full complete data model. For instance, $X_{i}$ could be both outcome and covariates; here the interest would be in the conditional (regression) model of the outcome given the covariates. If the covariates are missing, we need the full model to impute but in practice we would only estimate in the conditional model. If $\theta$ can be written as $\left(\theta_{1}, \theta_{2}\right)$, where $\theta_{1}$ is the parameter of the conditional model of interest and $\theta_{2}$ the parameter of the marginal model of the covariates, and the parameters are variation independent, i.e. $\left(\theta_{1}, \theta_{2}\right) \in \Theta_{1} \times \Theta_{2}$, then the result above shows that Bayesian multiple imputation are still proper for estimating $\theta_{1}$ (or $\theta_{2}$ ) using a conditional (or a marginal) maximum likelihood estimator. That this is not the case when the parameters are not variation independent will be indicated in Section 3.2 below.

Also it is worth noting that the iid structure assumed above is not necessary (nor used) in the derivations. Thus the result also holds for non-iid observations (given sufficient regularity, of course).

## 3 Counter Examples

If a conclusion is to be drawn from the results in Section 2, clearly it is that multiple imputation works nicely when we stay within a maximum likelihood framework. We do not, however, have to look very far for an example were Bayesian multiple imputations fail at being proper.

### 3.1 First Example

Let $X_{1}, \ldots, X_{n}$ be independent identically Gamma distributed with shape parameter $\lambda$ and intensity (inverse scale) $\theta$. Suppose that $\lambda$ is known and larger than 2 . Each $X_{i}$ is missing completely at random with probability $1-p$; i.e. each $X_{i}$ is observed with probability $p$ independently of $X_{1}, \ldots, X_{n}$. Suppose that only $N$ of the $n X_{i}$ s are observed; without loss of generality we assume it to be the first $N$. Note that $N / n \xrightarrow{P} p$.

The MLE of $\theta$ based on the observed data is $\hat{\theta}_{n}=\lambda / \bar{X}$, where $\bar{X}$ is the average of the observed $X_{i} \mathrm{~s}$. The asymptotic distribution of $\hat{\theta}_{n}$ is $N\left(\theta_{0}, \frac{1}{p n} \frac{\theta_{0}^{2}}{\lambda}\right)$.

Assuming a Gamma prior distribution with parameters $(\alpha, \beta)$, the posterior is again a Gamma distribution with parameters $(\alpha+N \lambda, \beta+N \bar{X})$. We now let $\tilde{\theta}_{n j}, j=1, \ldots, m$ be drawn from the posterior; note that (given the observed data)

$$
\sqrt{n}\left(\tilde{\theta}_{n j}-\hat{\theta}_{n}\right) \xrightarrow{\mathcal{D}} N\left(0, \frac{1}{p} \frac{\theta_{0}^{2}}{\lambda}\right) .
$$

Finally, let for each $j=1, \ldots, m$ the imputations $\widetilde{X}_{i j}$ be drawn independently for $i=N+1, \ldots, n$ from the Gamma distribution with shape $\lambda$ and intensity $\tilde{\theta}_{n j}$.

Suppose now that rather than using the MLE as our complete data estimator we use $1 / n \sum_{i=1}^{n}(\lambda- 1) / X_{i}$. In the complete data model, it is unbiased and asymptotically normal with variance $1 / n$. $\theta_{0}^{2} /(\lambda-2)$. Hence

$$
\theta_{n j}^{*}=\frac{1}{n} \sum_{i=1}^{N}(\lambda-1) / X_{i}+\frac{1}{n} \sum_{i=N+1}^{n}(\lambda-1) / \tilde{X}_{i j} .
$$

Let $\theta_{n}^{*}=1 / N \sum_{i=1}^{N}(\lambda-1) / X_{i}$ be the corresponding estimator based on the observed data only (the complete case estimator). Then

$$
\begin{aligned}
\sqrt{n}\left(\theta_{n j}^{*}-\theta_{n}^{*}\right)= & \frac{1}{\sqrt{n}} \sum_{i=N+1}^{n}\left(\frac{\lambda-1}{\widetilde{X}_{i j}}-\theta_{n}^{*}\right) \\
= & \sqrt{\frac{n-N}{n}} \frac{1}{\sqrt{n-N}} \sum_{i=N+1}^{n}\left(\frac{\lambda-1}{\widetilde{X}_{i j}}-\tilde{\theta}_{n j}\right) \\
& +\frac{n-N}{n} \sqrt{n}\left(\tilde{\theta}_{n j}-\hat{\theta}_{n}\right)+\frac{n-N}{n} \sqrt{n}\left(\hat{\theta}_{n}-\theta_{n}^{*}\right) .
\end{aligned}
$$

Going through arguments similar to those given in Section 2 (using first the Lindeberg central limit theorem conditional on the data and $\tilde{\theta}_{n j}$ and then (5)), we see that

$$
\begin{aligned}
& \sqrt{n}\left(\theta_{n j}^{*}-\hat{\theta}_{n}\right)+\frac{N}{n} \sqrt{n}\left(\hat{\theta}_{n}-\theta_{n}^{*}\right) \\
& =\sqrt{\frac{n-N}{n}} \frac{1}{\sqrt{n-N}} \sum_{i=N+1}^{n}\left(\frac{\lambda-1}{\widetilde{X}_{i j}}-\tilde{\theta}_{n j}\right)+\frac{n-N}{n} \sqrt{n}\left(\tilde{\theta}_{n j}-\hat{\theta}_{n}\right) \\
& \xrightarrow{\mathcal{D}} N\left(0, \frac{(1-p)^{2}}{p} \frac{\theta_{0}^{2}}{\lambda}+(1-p) \frac{\theta_{0}^{2}}{\lambda-2}\right)
\end{aligned}
$$

conditional on the observed data. Using the central limit theorem and the delta method, it is straightforward to show that

$$
\left[\begin{array}{c}
\sqrt{n}\left(\hat{\theta}_{n}-\theta_{0}\right) \\
\sqrt{n}\left(\hat{\theta}_{n}-\theta_{n}^{*}\right)
\end{array}\right] \xrightarrow{\mathcal{D}} N\left(\left[\begin{array}{l}
0 \\
0
\end{array}\right],\left[\begin{array}{cc}
\frac{1}{p} \frac{\theta_{0}^{2}}{\lambda} & 0 \\
0 & \frac{1}{p}\left(\frac{\theta_{0}^{2}}{\lambda-2}-\frac{\theta_{0}^{2}}{\lambda}\right)
\end{array}\right]\right) .
$$

Thus the multiple imputation estimator $\bar{\theta}_{n}=\frac{1}{m} \sum_{j=1}^{m} \theta_{n j}^{*}$ is asymptotically normal with mean $\theta_{0}$ and variance

$$
\frac{1}{n}\left(\frac{1}{p} \frac{\theta_{0}^{2}}{\lambda}+p\left(\frac{\theta_{0}^{2}}{\lambda-2}-\frac{\theta_{0}^{2}}{\lambda}\right)+\frac{1}{m}\left(\frac{(1-p)^{2}}{p} \frac{\theta_{0}^{2}}{\lambda}+(1-p) \frac{\theta_{0}^{2}}{\lambda-2}\right)\right)
$$

The variance estimator is

$$
\begin{aligned}
& \frac{1}{m} \sum_{j=1}^{m} \frac{\theta_{n j}^{* 2}}{\lambda-2}+\left(1+\frac{1}{m}\right) \frac{n}{m-1} \sum_{j=1}^{m}\left(\theta_{n j}^{*}-\bar{\theta}_{n}\right)^{\otimes 2} \\
& \leadsto \frac{\theta_{0}^{2}}{\lambda-2}+\left(1+\frac{1}{m}\right)\left(\frac{(1-p)^{2}}{p} \frac{\theta_{0}^{2}}{\lambda}+(1-p) \frac{\theta_{0}^{2}}{\lambda-2}\right)
\end{aligned}
$$

and the difference between ( $n$ times) (6) and (7) is

$$
2(1-p)\left(\frac{\theta_{0}^{2}}{\lambda-2}-\frac{\theta_{0}^{2}}{\lambda}\right)>0 .
$$

Thus the imputations are not proper in this example. Or rather, they are not proper for this estimator. Clearly, if we had used the complete data MLE as our estimator rather than the inefficient but unbiased estimator, the imputations would have been proper by the results of Section 2. Thus "being proper" is not a property, which is independent of the subsequent analysis.

Though the imputations are improper in the example above, at least the estimator of the variance is larger than the asymptotic variance. Hence Wald-type tests will be conservative, and confidence intervals will be too large, but at least they will be valid. Meng (1994, Main Result) gives sufficient conditions for this to be the case. However, as the following example shows we might as well get a variance estimator, which is too small.

### 3.2 Second Example

Let $Y_{1}, \ldots, Y_{n}$ be a random sample from a Gaussian distribution with mean $\theta$ and variance 1. Suppose that a second sample, $X_{1}, \ldots, X_{n}$ from a Gaussian distribution with the same unknown mean but a different, yet known, variance $\sigma^{2}$ is not observed, but that we (rather foolishly) wish to incorporate it in our estimation of $\theta$. Here our imputations are $\widetilde{X}_{i j}=\tilde{\theta}_{n j}+\sigma \varepsilon_{i j}$ where the $\varepsilon_{i j} \mathrm{~s}$ are iid standard normal random variables and $\tilde{\theta}_{n j}$ are drawn independently for $j=1, \ldots, m$ from a normal distribution with a mean equal to $\sum_{i=1}^{n} Y_{i} /(1+n)$ and variance equal to $1 /(1+n)$; this corresponds to using a standard normal prior for $\theta$. Taking the average of the observed $Y_{i} \mathrm{~s}$ and the imputed $\widetilde{X}_{i j} \mathrm{~s}$ (for each $j=1, \ldots, m$ ) as our estimator, we get

$$
\begin{aligned}
\sqrt{n}\left(\bar{\theta}_{n}-\theta_{0}\right) & \sim N\left(\frac{-\sqrt{n}}{2(n+1)} \theta_{0}, \frac{1}{4}\left(1+\frac{n}{n+1}\right)^{2}+\frac{1}{4 m}\left(\frac{n}{n+1}+\sigma^{2}\right)\right) \\
\xrightarrow{\mathcal{D}} & N\left(0,1+\frac{1}{m} \frac{1+\sigma^{2}}{4}\right) .
\end{aligned}
$$

But the estimator of the variance using "Rubin's rule" has expectation

$$
\frac{1+\sigma^{2}}{4}+\left(1+\frac{1}{m}\right) \frac{1+\sigma^{2}}{4}+O\left(\frac{1}{n}\right),
$$

so that for $n$ large the difference is $\left(1-\sigma^{2}\right) / 2$. In particular, if $\sigma^{2}<1$, then the estimator of the variance is systematically smaller than the true variance. Hence, if $\sigma^{2}<1$, we do not obtain asymptotically valid tests, and our confidence intervals will be too short. For $\sigma^{2}>1$ the variance is overestimated. Only for $\sigma^{2}=1$ do we get a weakly unbiased estimator; of course, in this case our complete data estimator is maximum likelihood.

We get similar results if we use a marginal maximum likelihood estimator, the average of the $X_{i} \mathrm{~s}$, as our complete data estimator, indicating that we cannot extend the large sample results from Section 2 to estimating a sub-parameter which is not variation independent of the rest of $\theta$.

Remark. It is not essential for the result (merely convenient for the calculations) to assume the variances of $X_{i}$ and $Y_{i}$ to be known; we get exactly the same (asymptotic) result if we use, say, independent inverse $\chi^{2}$-priors for the variances. Of course, if the variance of $X_{i}$ is unknown we would be very foolish indeed to try to impute the missing data.

### 3.3 Simulations

To get a slightly more interesting example we generalise the complete data model in Subsection 3.2 to have an unknown variance matrix

$$
\left[\begin{array}{c}
X_{i} \\
Y_{i}
\end{array}\right] \sim N\left(\left[\begin{array}{l}
\theta \\
\theta
\end{array}\right],\left[\begin{array}{cc}
\sigma_{x}^{2} & \rho \\
\rho & \sigma_{y}^{2}
\end{array}\right]\right) .
$$

Thus we have two measurements on each individual with different precision, and we wish to estimate the population mean. Furthermore, we let $X_{i}$ be missing at random, rather than completely missing. Thus whether $X_{i}$ is observed or missing is allowed to depend on $Y_{i}$. If the variance of $Y_{i}$ is large compared to the variance of $X_{i}$ it will be highly relevant to incorporate the observed $X_{i}$ s in the estimation of $\theta$. However, since $X_{i}$ is not missing completely at random we have to do something intelligent. Let us try imputing from a predictive distribution.

To specify a Bayesian imputation model, we re-parametrise $\left(\theta, \sigma_{x}^{2}, \rho, \sigma_{y}^{2}\right)$ to $\left(\theta, \sigma^{2}, \beta, \tau^{2}\right)$ where $\beta=\rho / \sigma_{y}^{2}$ is the regression coefficient in the conditional model of $X_{i}$ given $Y_{i}, \tau^{2}=\sigma_{x}^{2}-\rho^{2} / \sigma_{y}^{2}$ is the conditional variance, and $\sigma^{2}=\sigma_{y}^{2}$. A prior distribution is chosen as standard normals for $\theta$
and $\beta$ and scaled inverse $\chi^{2}$ distributions with parameters (2,3/2) for $\sigma^{2}$ and $\tau^{2}$; all components are a priori independent. The posterior (and hence the predictive distribution) becomes non-standard, so we simulate instead of giving exact results.

For illustration we simulate 5000 data sets of sample size 200 with parameters $\left(\theta, \sigma_{y}^{2}, \rho, \sigma_{x}^{2}\right)= (1,1,0.5,0.5) . X_{i}$ is missing if $Y_{i}>1.84$ so that the proportion of incomplete data is approximately $20 \%$. The imputations are generated by $m=5$ independent Gibbs samplers run for 2000 iterations. The results show that for any practical purpose the multiple imputation estimator is normally distributed with mean 1 and variance 0.00355 ; see Figure 1 . A Kolmogorov-Smirnoff test accepts the hypothesis of normality with a $p$-value of $53.5 \%$.

![](https://cdn.mathpix.com/cropped/ceebf844-e178-4487-bbdb-d014c79653c4-09.jpg?height=618&width=1337&top_left_y=776&top_left_x=333)
Figure 1. Simulated distribution of the MI-estimator.

The variance estimator is however too small as seen from Figure 2: The true variance (indicated by the vertical line in Figure 2) is the $77 \%$ quantile of the (simulated) distribution of the variance estimator.

To be fair it must be added that these results are highly dependent on the chosen values of the parameters. For other parameter values the result is the reverse: The variance estimator overestimates the true variance. Keeping the simple example of Section 3.2 in mind, this is not unexpected. The conclusion from this observation is not heartening though: Since we cannot in general see if the procedure we use over- or under-estimates the variance, we really cannot trust it at all.

It is worth noticing that the confidence intervals based on the variance estimator and the $t$ distribution approximation are surprisingly good in this simulation: A nominal $95 \%$ confidence interval has $93.7 \%$ coverage, whereas a $90 \%$ confidence interval has $88.9 \%$ coverage. This appears to be due to the fact that when the variance is underestimated, the approximate degrees of freedom are underestimated too resulting in longer confidence intervals.

## 4 A Note on Uncongeniality

Meng (1994) discusses a concept he calls "(un-)congeniality". He defines an "analysis procedure" consisting of an estimator of the unknown parameter $\theta$ based on the observed data and an estimator of $\theta$ based on the complete data both with associated variance estimators to be congenial to an imputation procedure if

![](https://cdn.mathpix.com/cropped/ceebf844-e178-4487-bbdb-d014c79653c4-10.jpg?height=759&width=780&top_left_y=413&top_left_x=607)
Figure 2. Simulated distribution of the variance estimator. The true variance is indicated by the vertical line.

1. the imputations come from a Bayesian predictive distribution
2. the observed (complete) data estimator asymptotically equals the posterior mean of $\theta$ given the observed (complete) data and the associated variance estimator asymptotically equals the posterior variance of $\theta$ given the observed (complete) data.

Meng (1994) shows that congeniality implies properness in the sense that the variance estimator derived from "Rubin's rule" is consistent if $m=\infty$. He does not explicitly consider the asymptotic distribution of the estimator, and his treatment of congeniality is restricted to multiple imputation with $m=\infty$.

In order to discuss asymptotic results it seems fruitful to extend the asymptotic equivalence of the estimators of $\theta$ to be such that two estimators $\hat{\theta}_{n}$ and $\tilde{\theta}_{n}$ are asymptotically equal if $\sqrt{n}\left(\hat{\theta}_{n}-\tilde{\theta}_{n}\right) \xrightarrow{P} 0$. Since the posterior mean and variance asymptotically equals the MLE and inverse Fisher information in sufficiently regular models, the argument given in Section 2 actually verifies Meng's (1994) result for fixed finite $m$, if consistency of the variance estimator is replaced by it being weakly unbiased. Moreover, we see that (with our strengthening of Meng's (1994) concept) the following result is true in sufficiently regular models:

Result 1. An analysis procedure is congenial to an imputation procedure if and only if the complete data and observed data estimators are efficient (i.e. maximum likelihood) and their associated variance estimators estimate the corresponding inverse Fisher informations.

Hence, if our complete and observed data estimators are efficient, our Bayesian multiple imputations are proper in the sense adopted for this paper. Of course, they may be proper even if the analysis procedure is not congenial to the imputation procedure. As the asymptotic results of Section 2 show, if the complete data estimator is efficient, the imputations derived from a corresponding Bayesian predictive distribution are proper, regardless of whatever observed data estimator we have
in mind. Meng's (1994) insistence on an observed data estimator seems to be based on his intention of comparing the multiple imputation estimator to an estimator based on the observed data. It makes a further discussion of the results reported in this paper difficult to relate to his concepts. However, we note that in our examples, the analysis procedure is uncongenial to the imputation procedure.

Schenker \& Welsh (1988) discuss multiple imputation in a linear regression setting with missing outcomes. The noise is only restricted to be iid zero mean random variables with finite variance (so that their model is really semi-parametric), but they impute using a Bayesian predictive distribution calculated under the assumption that the noise is indeed normal. Their complete data estimator is the usual least squares estimator. Clearly, the distribution of the noise could be chosen such that the complete data estimator is not efficient but their results indicate that the Bayesian multiple imputations are proper in our sense. Of course, one might argue that since their result is due to the fact that they rely on first and second moments and their calculations are exactly as they would be in the case of Gaussian errors, where the least squares estimator is maximum likelihood, this does not really give much of a counterexample to the need for efficient complete data estimators. Furthermore, if the imputations were made assuming a non-Gaussian distribution of the errors, the variance estimator of the least squares estimator obtained using "Rubin's rule" would typically be wrong. Alternatively, one might argue that their estimator is efficient in the semi-parametric model Schenker \& Welsh (1988) consider, but that would be missing the point: Their imputations are proper even if the errors are assumed to be double exponential as long as we use the least squares estimator and the Gaussian imputation model. We see again that being proper is as much related to the complete data estimator as to the model generating the data.

Though there may be examples-the example considered by Schenker \& Welsh (1988) could be considered one such example-where Bayesian multiple imputations are proper even though the complete data estimator is not efficient, the examples given in Section 3 suggest that this would be the exception rather than the rule. Thus, to be on the safe side we must insist that our complete data estimators are efficient.

## 5 Inefficiency

The insistence on efficiency is sound statistical advice with or without missing data. But a multiple imputation estimator is clearly not efficient: It is a simulation based estimator, and simulation introduces noise. Obviously, there is little point in using a multiple imputation estimator if an efficient estimator (based on the observed data) can be found. Thus criticising multiple imputation estimators for being inefficient when compared to the observed data MLE is hardly fair. Moreover, (3) tells us that we can make the multiple imputation estimator based on the complete data MLE almost efficient by picking $m$ sufficiently large.

However, as Wang \& Robins (1998) discuss in detail, the inconsistent variance estimator leads to much broader confidence intervals (weaker tests) than a consistent variance estimator would do. Thus even though the estimator is almost efficient (for $m$ large), the inference is inefficient. Robins \& Wang (2000) suggest a consistent variance estimator; it is, however, more complicated to calculate than the one obtained from "Rubin's rule". When using the complete data MLE as the complete data estimator, a simple estimator is available (Wang \& Robins, 1998):

$$
\hat{I}=\frac{1}{n} \sum_{i=1}^{n} \frac{1}{2 m(m-1)} \sum_{j, j^{\prime}=1, j \neq j^{\prime}}^{m}\left(s_{\tilde{X}_{i j}}\left(\tilde{\theta}_{n j}\right)^{t} s_{\tilde{X i j}^{\prime}}\left(\tilde{\theta}_{n j^{\prime}}\right)+s_{\tilde{X}_{i j^{\prime}}}\left(\tilde{\theta}_{n j^{\prime}}\right)^{t} s_{\tilde{X}_{i j}}\left(\tilde{\theta}_{n j}\right)\right)
$$

is a consistent estimator of the observed data information (given sufficient regularity), and

$$
\hat{I}^{-1}+\frac{1}{m}\left(\hat{I}^{-1}-\frac{1}{m} \sum_{j=1}^{m} \hat{V}_{n j}^{-1}\right)
$$

is a consistent estimator of the variance of $\bar{\theta}_{n}$ (cf (3)).
In practice the multiple imputation estimator is often inefficient in a much more direct sense. To be able to impute from a Bayesian predictive distribution we-more or less-need to be able to simulate from the posterior distribution of $\theta$. In all but trivial examples, to draw from the posterior we need a Markov chain method such as a Gibbs sampler. In order to get $m$ independent imputations, we need to run our Gibbs sampler $m$ times independently to convergence. However, the average of the last $k$ iterations of the $m$ chains will provide a much better estimator than multiple imputation; here the additional variance due to simulations goes down as $1 /(m k)$. Actually, to find the posterior mean only one chain is necessary, though $m$ independent chains may be useful for checking convergence (Gelman, 1996). This single chain may then be run $m$ times as long making more efficient use of the simulation budget. Alternatively, the simulation noise can be reduced to whatever level desired by running the $m$ chains further (i.e. increasing $k$ ). In practice, this would typically be a limited extension of the simulation budget. To reduce the simulation noise of the multiple imputation estimator, more chains run until convergence are needed. In practical implementation of multiple imputation, one may choose to run just one Markov chain and choose the $\tilde{\theta}_{n j}$ s far apart, so that they are approximately independent. Clearly, a more efficient use of this single chain would be to find the posterior mean, i.e. the average of the chain. Consequently, in most practical examples there will be an estimator more efficient than the multiple imputation estimator which may be obtained by the same amount of simulation (or at worst negligibly more).

If we can draw directly from the posterior distribution, multiple imputation might be quite efficient. If our complete data estimator is maximum likelihood, the multiple imputation estimator will be more efficient than the average of the simulated $\tilde{\theta}_{n j} \mathrm{~s}$, since $1 / m \sum_{j=1}^{m} \tilde{\theta}_{n j}$ is asymptotically normal with mean $\theta_{0}$ and variance $(1+1 / m) I\left(\theta_{0}\right)^{-1} / n$ (use Lemma 1 ), which is larger than the asymptotic variance found in (3). However, if the aim is to reduce the simulation part of the variance, it may well be faster to use the posterior mean estimator (with a slightly larger $m$ ) than to do the extra work necessary to simulate from the predictive distribution and find a complete data estimator, especially if an iterative procedure is needed in order to find this.

The final case, where drawing directly from the predictive distribution is possible, seems to be rare in practice, especially if we rule out examples so simple that we can find an efficient estimator directly. However, if such a problem should occur in practice, multiple imputation may be the solution.

## 6 Practical Implementation

For practical application of the methods discussed in the previous section it is important that software implementing them exist. Indeed, the wealth of free and commercial software available for multiple imputation (see www.multiple - imputation.com for a list) makes multiple imputation easy and tempting to use. Keeping our examples in mind, one should be careful to check when using this software that it actually imputes from the model one intends to analyse. Some of the software only allows a very limited choice of imputation models even if the models offered are flexible. Imputing from an incorrect model will generally lead to wrong (asymptotically biased) estimators: Restricting attention to estimators derived from an estimating equation, we need the imputations to be such that the estimating equation is approximately unbiased to obtain consistent estimators. Of course, as the examples clearly indicate, for the variance estimator to be reasonable, we need much more.

On the other hand, free and flexible software for implementing Bayesian models (BUGS/WinBUGS,
www.mrc - bsu.cam.ac.uk/bugs/) exists making the posterior mean estimator a feasible and attractive alternative in many problems.

## 7 Conclusion

When it comes to the examples given in Section 3, it is important to notice that all the methods used are "correct": The complete data estimators would lead to consistent asymptotically normal estimators with complete data, and the Bayesian models are based on the correct likelihood and sensible priors. Hence, our examples are-unlike most examples on how multiple imputation may fail found in the literature-not examples of the imputer assuming/knowing more or less than the data analyser. Indeed we think of the imputer and the analyser as being the same person as would be common in most statistical applications outside analysis of large public-use databases.

The examples are very simple. Indeed, when it comes to the first two examples the observed data MLE can be written down explicitly and presumably nobody would even consider using multiple imputation or anything else to estimate the unknown parameter. The third example is slightly more complicated. Though a consistent normally distributed estimator-the average of the $Y_{i}$ s-is easily obtained, the facts that only $20 \%$ of the $X_{i} \mathrm{~s}$ are missing and that the $X_{i} \mathrm{~s}$ have smaller variance, make it tempting to improve on the simple but very inefficient estimator. Missing at random rather than completely at random rules out simple solutions such as a complete case analysis. Finally, the unrestricted variance matrix makes exact maximum likelihood difficult both in the observed data case and the complete data case, leading us to an inefficient complete data estimator. This being said, it is not too difficult to guess a better complete data estimator, to find an efficient two-step estimator, or even to find the MLE by iterative means. On the other hand, inefficient estimators are frequently used in practice when models get more complicated than the ones considered in the examples here. Examples include robust estimators, general estimating equations and quasi-likelihood and estimators derived from other optimality considerations than those of (asymptotic) efficiency; in the first example the complete data estimator is the best linear unbiased estimator based on the transformed observations $1 / X_{1}, \ldots, 1 / X_{n}$, whereas the estimators in the other two examples are moment estimators.

Whereas it may be argued that none of the examples are "realistic", the implications of these simple examples cannot be denied: Unless we use an efficient complete data estimator, the variance estimator derived from "Rubin's rule" will be asymptotically biased. Furthermore, the bias may be upwards, leading to inefficient but correct inference, as well as downwards, leading to incorrect inference. Moreover, the third example indicates that in practice it may be impossible to judge whether the bias is upwards or downwards.

As discussed in Section 5, even if we use an efficient complete data estimator, the multiple imputation procedure is inefficient: The inconsistency of the variance estimator leads to weaker tests than a consistent variance estimator (which in principle can be obtained) would. Even though a consistent variance estimator can be constructed, we should keep in mind that a more efficient estimator based on approximately the same amount of (simulation) work can be found.

The discussion so far has been given from a frequentist point of view. From a Bayesian point of view it would seem strange first to find the posterior distribution by simulation and then impute the missing data to find a point estimate and forget about the posterior. Clearly to be able to find the posterior distribution answers any Bayesian need.

The situation is more complicated when it comes to large public-use data bases. Here multiple imputation may be the best strategy: The imputer uses her or his knowledge to create better imputations than the analyser is able to, and an analyser, using a correct model and an efficient complete data estimator, obtains consistent asymptotically normal estimators and-using the variance estimator given by (11)-acceptable confidence intervals and tests. Or the analyser ignores the imputations provided and creates his or her own; multiple imputations (unlike single imputation) makes it obvi-
ous which observations are actually imputed and which are observed. Also the multiple imputations carry a little information on what the imputer thought was important to correct for when creating the imputations even if this information may be difficult to quantify for the analyser. It must also be acknowledged that for public-use data bases imputation is necessary; it cannot be expected that all users are able to treat missing data correctly. Here multiple imputation allows the user to perform correct analyses as long as (s)he stays within certain limits.

The findings discussed above suggest that for general statistical practice multiple imputation is not the solution to missing data problems. Of course, we should keep in mind that we have only considered imputations derived from a Bayesian predictive distribution. Thus there may be other ways of generating proper multiple imputations and some of these may yield more satisfying results. However, so far only Bayesian or approximately (cf Rubin, 1987 p. 124) Bayesian imputation schemes have been shown to be proper in some settings. We close with an example of an approximately Bayesian imputation method: Find the observed data MLE, $\hat{\theta}_{n}$, and a consistent estimator of the Fisher information, $\hat{I}$. Construct multiple imputations by drawing $\widetilde{X}_{i j}$ from the conditional distribution of $X_{i}$ given $Y_{i}$ using $\tilde{\theta}_{n j}$ drawn from $N\left(\hat{\theta}_{n}, \hat{I}^{-1} / n\right)$ as the parameter. The argument given in Section 2 shows that this gives proper imputations when the complete data estimator is the MLE. But would anyone use this estimator instead of the observed data MLE? Hopefully not. Do we?

## Acknowledgement

I am very grateful for the help of Xiao-Li Meng and Martin Romero, whose independent simulations disclosed an error in my original simulations for section 3.3.

## References

Gelman, A. (1996). Inference and monitoring convergence. In Markov chain Monte Carlo in practice, Eds. W.R. Gilks, S. Richardson \& D.J. Spiegelhalter. Chapman \& Hall.

Heitjan, D.F. \& Rubin, D.B. (1991). Ignorability and coarse data. Ann. Statist., 19, 2244-2253.
Meng, X.-L. (1994). Multiple-imputation inferences with uncongenial sources of input. Statist. Sci., 9, 538-558.
Nielsen, S.F. (2000). Relative coarsening at random. Statist. Neerlandica, 54, 79-99.
Robins, J.M. \& Wang, N. (2000). Inference for imputation estimators. Biometrika, 87, 113-124.
Rubin, D.B. (1987). Multiple Imputation for Nonresponse in Surveys. Wiley.
Rubin, D.B. (1996). Multiple imputation after 18+ years. J. Amer. Statist. Assoc., 91, 473-489.
Schafer, J. (1997). Analysis of Incomplete Multivariate Data. Chapman \& Hall.
Schenker, N. \& Welsh, A.H. (1988). Asymptotic results for multiple imputation. Ann. Statist., 16, 1550-1566.
van der Vaart, A.W. (1998). Asymptotic Statistics. Cambridge University Press.
Wang, N. \& Robins, J.M. (1998). Large-sample theory for parametric multiple imputation procedures. Biometrika, 85, 935948.

## Résumé

On a pris l'habitude de considérer l'imputation multiple comme une solution générale au problème des données manquantes en statistique. Cependant, afin d'obtenir des estimateurs cohérents et asymptotiquement normaux, des estimations correctes de la variance et des tests valides, il faut que les imputations soient approprées. Jusqu'alors, il semble que c'est seulement dans le cas de l'imputation multiple bayésienne, c'est-á-dire utilisant une distribution prédictive bayésienne pour générer les imputations, ou de ses approximations, que l'on a montré que l'on obtenait des imputations appropriées dans certains cas particuliers. Dans cet article, on montre qu'en général l'imputation multiples bayésienne ne conduit pas à des imputations multiples appropriées. De plus, on argumente l'idée selon laquelle, de manière générale, l'imputation multiple bayésienne est inefficace même si elle approprée.

## Appendix

## Regularity Assumptions

Regularity assumptions necessary for the calculations given in Section 2 may take many forms. The regularity conditions suggested here are not supposed to be technically exhaustive but merely suggestive of what may be needed:

1. "Standard regularity assumptions" on the complete and observed data models, so that the MLE is asymptotically linear and efficient in both models.
2. The draws from the posterior are asymptotically normal, i.e. given the observed data

$$
\sqrt{n}\left(\tilde{\theta}_{n j}-\hat{\theta}_{n}\right) \xrightarrow{\mathcal{D}} N\left(0, I\left(\theta_{0}\right)^{-1}\right) .
$$

Often this follows from the same regularity conditions used to obtain the asymptotic distribution of the observed data MLE.
3. With $\widetilde{X}_{i} \sim \mathcal{L}_{\theta_{n}}\left(X_{i} \mid Y_{i}=y_{i}\right)$,

$$
\frac{1}{\sqrt{n}} \sum_{i=1}^{n} s_{\tilde{X}_{i} \mid y_{i}}\left(\theta_{n}\right) \xrightarrow{\mathcal{D}} N\left(0, E I_{Y}\left(\theta_{0}\right)^{-1}\right)
$$

for any sequence $\theta_{n}$ with $\sqrt{n}\left(\theta_{n}-\theta_{0}\right)$ bounded and (almost) every sequence of $y_{i}$ s. In practice, a Lindeberg condition should be verified.
4. Uniform laws of large numbers hold for

$$
\frac{1}{n} \sum_{i=1}^{n} D_{\theta} S_{\tilde{X}_{i} \mid y_{i}}(\theta) \quad \text { and } \quad \frac{1}{n} \sum_{i=1}^{n} D_{\theta} S_{Y_{i}}(\theta)
$$

on a compact set of $\theta$ with $\theta_{0}$ as an inner point; here $\tilde{X}_{i} \sim \mathcal{L}_{\theta}\left(X_{i} \mid Y_{i}=y_{i}\right)$. In practice this could be verified from additional smoothness (a Lipschitz condition) or more general empirical process techniques.

# Discussion: Efficiency and Self-efficiency With Multiple Imputation Inference 

Xiao-Li Meng ${ }^{\mathbf{1}}$ and Martin Romero ${ }^{\mathbf{2}}$<br>${ }^{1}$ Harvard University, Cambridge, MA 02138, USA. E-mail: meng@stat.harvard.edu $\quad{ }^{2}$ Instituto Mexicano del Petróleo, Eje Central Lázaro Cárdenas 152, México D.F., C.P. 07730 México

## Summary

By closely examining the examples provided in Nielsen (2003), this paper further explores the relationship between self-efficiency (Meng, 1994) and the validity of Rubin's multiple imputation (RMI) variance combining rule. The RMI variance combining rule is based on the common assumption/intuition that the efficiency of our estimators decreases when we have less data. However, there are estimation procedures

