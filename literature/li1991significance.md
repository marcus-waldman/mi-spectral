---
citekey: li1991significance
authors: 'Li, Kim-Hung; Meng, Xiao-Li; Raghunathan, Trivellore E; Rubin, Donald B'
year: 1991
title: Significance levels from repeated p-values with multiply-imputed data
venue: Statistica Sinica
pages: 65–92
zotero_key: QKXBIDFT
item_type: journalArticle
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\li1991significance.pdf'
pdf_sha256: 5cf27bd17538c779ea5338b2c94c407ee90c8097a58dca8eb08a500d8e347331
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T22:52:25Z
---
# SIGNIFICANCE LEVELS FROM REPEATED p-VALUES WITH MULTIPLY-IMPUTED DATA 

Author(s): Kim-Hung Li, Xiao-Li Meng, T. E. Raghunathan and Donald B. Rubin

Source: Statistica Sinica, January 1991, Vol. 1, No. 1 (Tanuary 1991), pp. 65-92
Published by: Institute of Statistical Science, Academia Sinica
Stable URL: https://www.jstor.org/stable/24303994

## REFERENCES

Linked references are available on JSTOR for this article:
https://www.jstor.org/stable/24303994?seq=1\&cid=pdfreference\#references_tab_contents
You may need to log in to JSTOR to access the linked references.

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms \& Conditions of Use, available at https://about.jstor.org/terms
is collaborating with JSTOR to digitize, preserve and extend access to Statistica Sinica

# SIGNIFICANCE LEVELS FROM REPEATED $\boldsymbol{p}$-VALUES WITH MULTIPLY-IMPUTED DATA 

Kim-Hung Li, Xiao-Li Meng, T. E. Raghunathan and Donald B. Rubin<br>Chinese University of Hong Kong, Harvard University, University of Washington and Harvard University


#### Abstract

Multiple imputation is becoming a standard tool for handling nonresponse in sample surveys. A difficult problem in the analysis of a multiply-imputed data set concerns how to combine repeated $p$-values efficiently to create a valid significance level. Here we propose, justify, and evaluate the validity of a new procedure, which is superior to the current standard. This problem is inherently difficult when the number of multiple imputations is small, as it must be in common practice, as made clear by its close relationship to a multivariate version of the classic Behrens-Fisher problem with small degrees of freedom.


Key words and phrases: Multiple imputation, missing data, nonresponse, surveys, Bayesian inference, Behrens-Fisher problem, incomplete data, hypothesis testing.

## 1. Introduction and Background

Multiple imputation, first proposed in Rubin (1978), is a general statistical technique for handling missing data. It is particularly suited to handling nonresponse in large sample surveys, especially those surveys that are designed to produce public-use data bases to be shared by many users. In such surveys, it is tempting to impute (or fill in) the missing values due to nonresponse so that all users can work with a complete data base. The key idea of multiple imputation, in contrast to single imputation, is to replace the set of missing values with $m(\geq 2)$ sets of plausible values. Each of these $m$ resulting completed data sets is then analyzed using standard complete-data methods. These analyses are combined to create one repeated-imputation inference, which takes proper account of the uncertainty due to missing data. In this and other ways multiple imputation retains the major advantages and rectifies the major disadvantages inherent in single imputation. For a comprehensive treatment of multiple imputation and comparisons with single imputation, readers are referred to Rubin (1987), and specifically for comparisons of $p$-values using single and multiple imputation, to Li, Raghunathan and Rubin (1990).

All of the multiple imputation procedures described there perform much better than single imputation procedures. Of these procedures, the least successful, although adequate in most situations, is the one for combining $m p$-values (or $\chi^{2}$ test statistics) to obtain one valid significance level. To illustrate, suppose we wish to test a ten-component regression coefficient when there is $30 \%$ missing information (defined precisely in Section 1.4). Using single imputation, the rejection rate of a nominal $5 \%$ test is approximately $45 \%$ whereas the rejection rate of the current standard procedure is $10 \%$-not perfect but clearly an improvement over single imputation.

Here we derive and describe a new way to combine $p$-values that is as simple yet better than the previous standard. In particular, in the illustrative example just discussed, the rejection rate is $6 \%$. Related improvements for obtaining $p$-values from repeated estimates and variance-covariance matrices are more straightforward and are reported in Li, Raghunathan and Rubin (1990). In the remainder of Section 1, we provide the necessary background material and notation, including discussion of the inherent difficulty of this problem and its relationship with the well-known Behrens-Fisher problem. Section 2 presents our procedure, and gives its theoretical justification. Section 3 evaluates its validity. Finally, in Section 4 we discuss other approaches to this problem, and summarize our conclusion that the new procedure has the simplest form among all previous procedures that give accurate levels. We also provide practical advice on its use, and discuss related research.

### 1.1. The complete-data case

Let $X=\left[x_{1}, \ldots, x_{n}\right]^{t}$ be the $n \times p$ complete-data matrix, with the associated density $f(x \mid \theta)$, where the parameter $\theta$ is a $k$-dimensional vector. Assume that with the complete data the asymptotically valid and efficient inference for $\theta$ would be based on the statement

$$
U^{-1 / 2}(\hat{\theta}-\theta) \sim N(0, I)
$$

where $\hat{\theta}=\hat{\theta}(X)$ is an efficient estimate of $\theta$ and $U=U(X)$ is the associated variance-covariance matrix. For example, in a frequentist analysis, one may take $\hat{\theta}$ to be the maximum likelihood estimate of $\theta$ and $U$ to be the inverse of the observed information matrix. Then (1.1) can be interpreted as asserting that the sampling distribution of $\hat{\theta}$ is approximately normal with mean $\theta$ and variancecovariance $U$. In contrast, in Bayesian analysis, $\hat{\theta}$ and $U$ are the posterior mean and variance-covariance of $\theta$, respectively, where (1.1) is the large sample normal approximation to the posterior distribution of $\theta$. Thus, approximation (1.1) is commonly acceptable to both frequentists and Bayesians.

In practice, especially in multiparameter cases, the evidence about the likely values of $\theta$ is often summarized by a $p$-value for a specified "null" value of $\theta$, say $\theta_{0}$. As a direct consequence of approximation (1.1), this $p$-value can be calculated as

$$
P_{x}=\operatorname{Pr}\left[\chi_{k}^{2}>k D_{x}\right],
$$

where $\chi_{k}^{2}$ is a chi-square random variable with $k$ degrees of freedom, and $D_{x}$ is the observed value of the quadratic form

$$
D(X)=\left(\theta_{0}-\hat{\theta}\right)^{t} U^{-1}\left(\theta_{0}-\hat{\theta}\right) / k
$$

which is proportional to the Wald test statistic. Again, this $p$-value has both frequentist and Bayesian interpretations. A frequentist would interpret it as the probability of observing $D_{x}$ or more extreme values of $D(X)$ when $\theta=\theta_{0}$, in an imagined long sequence of identical experiments that produce new values of $\hat{\theta}$ and $U$. It is also a Bayesian $p$-value in the sense that the $(1-p) 100 \% \mathrm{HPD}$ (highest posterior density) region will just include $\theta_{0}$.

The use of $p$-values rather than interval estimates is especially useful and common in highly multiparameter models, such as large log-linear models for contingency tables, where the parameter $\theta$ consists of all high-dimensional interactions, and the $p$-value summarizes evidence about the acceptability of a parsimonious model that includes, for example, only main effects and two-way interactions. In such cases, the dimensionality of $\theta, k$, can be in the hundreds.

An important point is that whenever the complete-data likelihood ratio test has the form of (1.2), our approach can be used. Therefore, even if the test is not against a single null value of $\theta$, but rather against a collection of null values, as with a composite hypothesis, our method of combining significance levels still can be applied. The reason is that the only distributional results explicitly used are the $\chi_{k}^{2}$ reference distributions.

### 1.2. The incomplete-data case

In common survey practice, it is very likely that we can only observe part of the complete data $X$ for various reasons (see, for example, Rubin (1987), Chapter 1 ). Denote this observed part by $X_{\mathrm{obs}}=\left\{X_{i j} \mid R_{i j}=1\right\}$, where $R_{i j}=1$ if the $(i, j)$ th element of $X$ is observed, and zero otherwise. We also assume that the missing data mechanism is ignorable:

$$
\operatorname{Pr}(R \mid X)=\operatorname{Pr}\left(R \mid X_{\text {obs }}\right),
$$

where we suppress possible dependence of this distribution on unknown parameters distinct from $\theta$.

This ignorability assumption is not strictly necessary (Rubin (1987), Chapter 4), but for simplicity of presentation, we will assume it. Thus, the relevant likelihood function for drawing inferences about $\theta$ is

$$
L\left(\theta \mid X_{\mathrm{obs}}\right) \propto \int f(X \mid \theta) d X_{\mathrm{mis}}
$$

where $X_{\text {mis }}=\left\{X_{i j} \mid R_{i j}=0\right\}$ is the collection of missing values.
In analogy with the complete-data inference (1.1), we assume the following large-sample approximation holds

$$
T^{-1 / 2}\left(\hat{\theta}_{\mathrm{obs}}-\theta\right) \sim N(0, I)
$$

where $\hat{\theta}_{\text {obs }}=\hat{\theta}\left(X_{\text {obs }}\right)$ is an efficient estimate of $\theta$ based on the observed data (e.g., observed-data MLE or posterior mean), and $T=T\left(X_{\text {obs }}\right)$ is the associated variance-covariance matrix (e.g., inverse of the observed-data information matrix or the posterior variance of $\theta$ ). Consequently, the $p$-value for summarizing evidence about a null value $\theta_{0}$ can be calculated as

$$
P_{\mathrm{obs}}=\operatorname{Pr}\left[\chi_{k}^{2}>k D_{\mathrm{obs}}\right],
$$

where

$$
D_{\mathrm{obs}}=\left(\hat{\theta}_{\mathrm{obs}}-\theta_{0}\right)^{t} T^{-1}\left(\hat{\theta}_{\mathrm{obs}}-\theta_{0}\right) / k
$$

is proportional to the observed value of the Wald test statistic based on the observed data.

With the complete data $X$, the computation of $\hat{\theta}(X)$ and $U(X)$ usually is straightforward, either analytically or numerically. But with the incomplete data, it can become troublesome and even intractable, which is especially burdensome in contexts of public-use files.

### 1.3. Basic distributional results for multiple imputation

Multiple imputation is an efficient and valid way of handling incomplete data problems using only standard complete-data techniques once data are imputed. More specifically, $m$ imputations for the missing values $X_{\text {mis }}$ are created, $X_{* \text { mis }}^{(\ell)}, \ell=1, \ldots, m$, and these are used by the data analyst to create $m$ corresponding completed data sets

$$
\left\{X_{*}^{(\ell)} ; \ell=1, \ldots, m\right\}=\left\{\left(X_{\text {obs }}, X_{* \text { mis }}^{(\ell)}\right) ; \ell=1, \ldots, m\right\} .
$$

The data analyst then conducts $m$ standard complete-data analyses to compute the corresponding values for $\hat{\theta}=\hat{\theta}(X)$ and $U=U(X): \hat{\theta}_{* \ell}=\hat{\theta}\left(X_{*}^{(\ell)}\right)$ and $U_{* \ell}=U\left(X_{*}^{(\ell)}\right)(\ell=1, \ldots, m)$. Letting the set of completed-data moments be

$$
S_{m}=\left\{\left(\hat{\theta}_{* \ell}, U_{* \ell}\right) ; \ell=1, \ldots, m\right\}
$$

the data analyst can combine the statistics in the set $S_{m}$ to obtain one inference for $\theta$.

When using "proper" imputation methods (for the definition of "proper", see Rubin (1987), Chapter 4), the following approximations concerning the distribution of $\left(\hat{\theta}_{* \ell}, U_{* \ell}\right)(l=1, \ldots, m)$ are justifiable (Rubin (1987, Chapter 4), Raghunathan (1987), and Schenker and Welsh (1988)):

$$
\hat{\theta}_{* \ell} \mid X_{\mathrm{obs}}, \theta \sim \text { i.i.d. } N\left(\hat{\theta}_{\mathrm{obs}}, B\right)
$$

and

$$
U_{* \ell} \mid X_{\mathrm{obs}}, \theta \approx \bar{U}
$$

where

$$
\begin{aligned}
B & =B\left(X_{\mathrm{obs}}\right)=V\left[\hat{\theta}(X) \mid X_{\mathrm{obs}}, \theta\right] \\
\bar{U} & =\bar{U}\left(X_{\mathrm{obs}}\right)=E\left[U(X) \mid X_{\mathrm{obs}}, \theta\right]
\end{aligned}
$$

and $\approx$ in (1.8) means equal in the sense of lower order variability. Thus, in view of (1.4), (1.7), and (1.8), the sufficient statistics for inference about $\theta$ are

$$
\begin{gathered}
\bar{\theta}_{m}=\frac{1}{m} \sum_{\ell=1}^{m} \hat{\theta}_{* \ell}, \\
B_{m}=\frac{1}{m-1} \sum_{\ell=1}^{m}\left(\hat{\theta}_{* \ell}-\bar{\theta}_{m}\right)\left(\hat{\theta}_{* \ell}-\bar{\theta}_{m}\right)^{t}
\end{gathered}
$$

and

$$
\bar{U}_{m}=\frac{1}{m} \sum_{\ell=1}^{m} U_{* \ell}
$$

Here $B_{m}$ measures "between imputation" variability and $\bar{U}_{m}$ measures "within imputation" variability. Bayesian justification for these statistics can be found in Rubin (1987, Chapter 3).

### 1.4. Fractions of missing information

The crucial measure of the extent to which inference is hindered by the occurrence of missing data is the fraction of missing information, which is the proportionate increase in variance due to missing values. It is especially easy to make this idea clear from a Bayesian perspective. Specifically, the posterior variance of $\theta$ based on the observed data, $X_{\text {obs }}$, can be written as

$$
V\left(\theta \mid X_{\mathrm{obs}}\right)=E\left[V(\theta \mid X) \mid X_{\mathrm{obs}}\right]+V\left[E(\theta \mid X) \mid X_{\mathrm{obs}}\right],
$$

where the first term on the right hand side is the expected posterior variance of $\theta$ when there are no missing data, equal asymptotically to $E\left(U \mid X_{\text {obs }}\right)$, and the second term on the right hand side is the expected increase in posterior variance due to missingness. Hence, the eigenvalues of $V\left[E(\theta \mid X) \mid X_{\text {obs }}\right]$ relative to $V\left(\theta \mid X_{\text {obs }}\right)$ can be interpreted as measuring the increases in posterior variance due to missing data - the fractions of missing information. Small values of these eigenvalues imply less loss of precision. In particular, in the scalar case, the fraction of missing information is simply the ratio of $V\left[E(\theta \mid X) \mid X_{\text {obs }}\right]$ to $V\left(\theta \mid X_{\text {obs }}\right)$.

In large samples, the posterior variance $V\left(\theta \mid X_{\text {obs }}\right)$ will equal the inverse of the negative second derivative of the observed-data log-likelihood, defined in (1.4) to be $T=T\left(X_{\text {obs }}\right)$. Similarly, the complete-data posterior variance $V(\theta \mid X)$ will equal the inverse of the negative second derivative of the complete-data loglikelihood, defined in (1.1) to be $U=U(X)$. Thus, the first term on the right hand side of (1.14) is asymptotically equal to $\bar{U}$ defined in (1.10).

From the frequentist perspective with $\theta_{t}$ equal to the true value of $\theta$, asymptotically we have

$$
\left(\bar{U} \mid \theta=\theta_{t}\right) \approx U_{t}
$$

where

$$
U_{t}=V\left(\hat{\theta} \mid \theta=\theta_{t}\right) .
$$

Finally, the second term on the right hand side of (1.14) is approximately $B$ defined in (1.9); in large samples

$$
\left(B \mid \theta=\theta_{t}\right) \approx B_{t},
$$

where

$$
B_{t}=T_{t}-U_{t}
$$

with

$$
T_{t}=V\left(\hat{\theta}_{\mathrm{obs}} \mid \theta=\theta_{t}\right) .
$$

The eigenvalues of $B_{t}$ relative to $T_{t}$ give the population fractions of missing information, which we denote by $\gamma=\left(\gamma_{1}, \ldots, \gamma_{k}\right) \in[0,1)^{k}$. Thus, $\gamma$ gives the increases in variance of parameter estimates due to missing data when $\theta=\theta_{t}$. Because of the lower order variability of $B$ and $\bar{U}, \gamma$ may also be taken to be the eigenvalues of $B$ with respect to $T=(\bar{U}+B)$, with average fraction of missing information $\bar{\gamma}=\sum_{j} \gamma_{j} / k$. Notationally, we also let $\lambda_{j}=\gamma_{j} /\left(1-\gamma_{j}\right)$, $j=1, \ldots, k$, be the eigenvalues of $B_{t}$ (or $B$ ) relative to $U_{t}$ (or $\bar{U}$ ), where $\lambda= \left(\lambda_{1}, \ldots, \lambda_{k}\right)$ and $\bar{\lambda}=\sum_{j} \lambda_{j} / k$. A final set of measures are the ratios of complete to observed information, that is, $\xi_{i}=1+\lambda_{i}=\left(1-\gamma_{i}\right)^{-1}$, with $\xi=\left(\xi_{1}, \ldots, \xi_{k}\right)$ and $\bar{\xi}=\sum_{j} \xi_{j} / k$.

## 1.5. $p$-values based on $S_{m}$

Having obtained the collection of completed-data moments $S_{m}=\left\{\left(\hat{\theta}_{* \ell}, U_{* \ell}\right)\right.$, $\ell=1, \ldots, m\}$, we can obtain a $p$-value for $\theta=\theta_{0}$,

$$
P_{m}=\operatorname{Pr}\left(F_{k, w}>D_{m}\right)
$$

where the test statistic $D_{m}$ is a scaled distance between the estimate $\bar{\theta}_{m}$ of the parameter $\theta$ and the hypothesized value, $\theta_{0}$, based on the sufficient statistics (1.11-1.13), and $F_{k, w}$ is an $F$ reference distribution with $k$ and $w$ degrees of freedom, with $w \rightarrow \infty$ as $m \rightarrow \infty$. An excellent choice for $D_{m}$, which works well for all values of $m$, is

$$
D_{m}=\left(\bar{\theta}_{m}-\theta_{0}\right)^{t} \bar{U}_{m}^{-1}\left(\bar{\theta}_{m}-\theta_{0}\right) /\left[k\left(1+r_{m}\right)\right]
$$

where

$$
r_{m}=\left(1+m^{-1}\right) \operatorname{tr}\left(B_{m} \bar{U}_{m}^{-1}\right) / k
$$

The $F$ reference distribution can be justified from both the frequentist and Bayesian perspectives, and various specific choices of denominator degrees of freedom, $w$, have been proposed (Li (1985), Rubin (1987) and Raghunathan (1987)). Among them, the best one so far is proposed in Li, Raghunathan and Rubin (1990):

$$
w=4+(\nu-4)\left[1+\left(1-\frac{2}{\nu}\right) / r_{m}\right]^{2}
$$

where $\nu=k(m-1)$.
Notice that this procedure requires $\nu>4$. When $\nu \leq 4$, an alternative denominator degrees of freedom $(m-1)(k+1)\left(1+r_{m}^{-1}\right)^{2} / 2$, proposed by Rubin (1987), can be used. The major conclusion of Li, Raghunathan and Rubin (1990) is that this procedure is very well calibrated for all $m \geq 3$ in cases of practical interest, and the loss of power due to finite $m$ is quite modest in cases likely to occur in practice.

When $m \rightarrow \infty, D_{m}$ given by (1.17) tends to

$$
D_{m}^{\infty}=\left(\hat{\theta}_{\mathrm{obs}}-\theta_{0}\right)^{t} \bar{U}^{-1}\left(\bar{\theta}_{\mathrm{obs}}-\theta_{0}\right) /(k \bar{\xi})
$$

When all $\xi_{i}=\bar{\xi}=1+\bar{\lambda}$, it is easy to show that $D_{m}^{\infty}=D_{\text {obs }}$, the ideal test statistic. When the $\xi_{i}$ vary, Li , Raghunathan and Rubin (1990) show that $D_{m}^{\infty}$ is very close to $D_{\text {obs }}$ under most practical circumstances, the difference being governed essentially by the coefficient of variation of the $\xi_{i}$, that is, the coefficient of variation of the ratios of the complete to observed information.

## 1.6. $p$-values based on $S_{d}$

Clearly, the procedures given in Section 1.5 require access to the collection of completed-data moments $S_{m}=\left\{\left(\hat{\theta}_{* \ell}, U_{* \ell}\right), \ell=1, \ldots, m\right\}$. In practice, the dimension $k$ is often large, as when social scientists attempt to find parsimonious models from public-use data bases with hundreds of variables and thousands of sampling units. In such cases, the standard complete-data analysis may only provide the collection of completed-data $\chi^{2}$ statistics (or distances) $S_{d}=\left\{d_{* 1}, \ldots, d_{* m}\right\}$, where, asymptotically,

$$
d_{* \ell}=\left(\theta_{0}-\hat{\theta}_{* \ell}\right)^{t} U_{* \ell}^{-1}\left(\theta_{0}-\hat{\theta}_{* \ell}\right) ;
$$

the corresponding $p$-value in the $\ell$ th complete-data set is $\operatorname{Pr}\left(\chi_{k}^{2} \geq d_{* \ell}\right)(\ell= 1, \ldots, m)$. Consequently, finding the $p$-value for the null value $\theta_{0}$ given $S_{d}$ rather than $S_{m}$ is an important practical problem.

The problem of directly combining $\left\{d_{* \ell}, \ell=1, \ldots, m\right\}$ is tricky since each $d_{* \ell}$ typically leads to a too significant $p$-value because the $U_{* \ell}$ tends to underestimate the total variability $T$ in equation (1.4). The representation of $D_{m}$ that makes progress possible (Rubin (1987)) is to note that (1.8) implies

$$
D_{m} \approx \hat{D}_{m}=\frac{\bar{d}_{m} k^{-1}-\left(\frac{m-1}{m+1}\right) r_{m}}{1+r_{m}}
$$

where $\bar{d}_{m}$ is the sample mean of $\left\{d_{* \ell}, \ell=1, \ldots, m\right\}$ and $r_{m}$ is given by (1.18).
Two penalties for the overestimation inherent in the $d_{* \ell}$ exist in (1.22). First, a positive quantity is subtracted from $\bar{d}_{m} k^{-1}$ (the extra factor $k^{-1}$ is due to our using a mean square, rather than a chi-square as reference distribution), and then the result is divided by a quantity that is larger than 1 ; both penalties are monotone increasing functions of $r_{m}$.

Replacing $r_{m}$ in $\hat{D}_{m}$ with estimates obtained from the set $S_{d}$ yields procedures for calculating $p$-values when only $S_{d}$ is available. For example, the existing standard procedure, as described in Rubin (1987), is to replace $r_{m}$ by a method of moments estimate

$$
\hat{r}_{m}=\left(1+\frac{1}{m}\right) s_{d}^{2} /\left\{2 \bar{d}_{m}+\left[4 \bar{d}_{m}^{2}-2 k s_{d}^{2}\right]_{+}^{1 / 2}\right\}
$$

where $s_{d}^{2}$ is the sample variance of the $d_{* \ell}$ and $[a]_{+}=\max \{a, 0\}$. The resulting procedure for calculating the $p$-value is

$$
\hat{P}_{m}=\operatorname{Pr}\left\{F_{k, a_{k} \hat{\zeta}} \geq \hat{\hat{D}}_{m}\right\}
$$

where

$$
\begin{aligned}
\hat{\hat{D}}_{m} & =\frac{\bar{d}_{m} k^{-1}-\left(\frac{m-1}{m+1}\right) \hat{r}_{m}}{1+\hat{r}_{m}} \\
\hat{\zeta} & =(m-1)\left(1+\hat{r}_{m}^{-1}\right)^{2}
\end{aligned}
$$

and

$$
a_{k}=\left(1+k^{-1}\right) / 2 .
$$

Evaluations of this procedure are summarized in Rubin (1987) as well as in Li (1985); Raghunathan (1987); Weld (1987); Treiman, Bielby and Cheng (1988); and Schenker, Treiman and Weidman (1988). These results suggest that whenever the fractions of missing information are small, or modest but $m \geq k$, it provides reasonably accurate levels. In other cases, an improved procedure is needed, especially when both the fractions of missing information and $k$ are large.

### 1.7. Relationship with classic Behrens-Fisher problem

Our problem is closely related to the multivariate version $(k>1)$ of the Behrens-Fisher problem. In particular, when all $\lambda_{j}$ equal $\bar{\lambda}$, the numerator of $D_{m}$ on the right hand side of (1.17) is distributed proportional to a $\chi_{k}^{2}$ random variable, and the denominator as a positive affine transformation of an independent $\chi_{k(m-1)}^{2}$ random variable. In this case, $D_{m}$ is distributed as the square of a $k$-variate Behrens-Fisher random variable with $\infty$ and $k(m-1)$ degrees of freedom, where $r_{m}$ can be used to estimate the nuisance parameter $\bar{\lambda}$ with $k(m-1)$ degrees of freedom.

In traditional applications of the Behrens-Fisher problem, the two degrees of freedom are typically modest and relatively similar (e.g., 8 and 12), rather than $\infty$ and $k(m-1)$ where $m$ is small (e.g., 3). In traditional cases, simple approximations often work well because the nuisance parameter, $\bar{\lambda}$, although not known precisely, is well-enough known. References include: Aspin (1948), Cochran (1964), Jeffreys (1940), Johnson and Neyman (1936), Robinson (1976), Smith (1936), Wallace (1978), and Welch (1937, 1947). Although the distribution of $D_{m}$ becomes more complicated when the $\lambda_{j}$ vary, $r_{m}$ is still unbiased for $\bar{\lambda}$. It is thus not too surprising that for modest $k(m-1)$, a satisfactory reference distribution can be found for $D_{m}$, as in Li , Raghunathan and Rubin (1990).

The situation changes rather dramatically, however, when $r_{m}$ is not available and must be estimated - the case that occurs when inference must be based on the set $S_{d}$ rather than the set $S_{m}$. Although $\hat{D}_{m}$ given by (1.22) is asymptotically equivalent to $D_{m}$, when $r_{m}$ is replaced by an estimate from $S_{d}$, three things happen. First, the numerator and denominator of the resulting estimate of $\hat{D}_{m}$



are no longer independent; second, the degrees of freedom available to estimate $\bar{\lambda}$ are reduced from $k(m-1)$ to at most $(m-1)$, at most because the $d_{* \ell}$ only provide an absolute magnitude of the difference between $\theta_{0}$ and $\hat{\theta}_{* \ell}$ and not the direction of that difference as with $\hat{\theta}_{* \ell}-\theta_{0}$; and third, it is not obvious how to combine the ( $m-1$ ) apparent degrees of freedom in $S_{d}$ to estimate $\bar{\lambda}$.

Clearly with small $m$ (e.g., 3), inferences will be sensitive to values of the nuisance parameter $\bar{\lambda}$. Because in practice $m$ is modest, we are dealing with a situation where theoretical small samples issues in the Behrens-Fisher problem are practically important.

## 2. The Proposed Procedure

### 2.1. The test statistic $\hat{D}_{\boldsymbol{d}}$

The proposed test statistic is of the form $D_{m}$ with $r_{m}$ replaced by an estimate $\hat{r}_{d}$, as with $\hat{\hat{D}}_{m}$. Specifically, we propose

$$
\hat{D}_{d}=\frac{\bar{d}_{m} k^{-1}-\left(\frac{m+1}{m-1}\right) \hat{r}_{d}}{1+\hat{r}_{d}}
$$

where

$$
\hat{r}_{d}=\left(1+\frac{1}{m}\right)\left[\frac{1}{m-1} \sum_{\ell=1}^{m}\left(\sqrt{d_{* \ell}}-\overline{\sqrt{d}}\right)^{2}\right]
$$

is the sample variance of $\sqrt{d_{* 1}}, \ldots, \sqrt{d_{* m}}$ times ( $1+m^{-1}$ ). This estimate of $r_{m}$ makes intuitive sense because the smaller the fraction of missing information $\gamma$, the closer each of the $d_{* \ell}(\ell=1, \ldots, m)$ should be to the ideal test statistic and thus to each other. For example, in the extreme case when there is no missing information, all $d_{* \ell}$ 's must be equal to the ideal test statistic, and hence $\hat{r}_{d}=0$; then the corresponding $\hat{D}_{d}$ is also equal to the ideal test statistic.

### 2.2. The derivation of $\hat{D}_{d}$ assuming equal eigenvalues

The main difficulty in deriving a replacement for $r_{m}$ based on the set $S_{d}$ is that the joint distribution of $\left(d_{* 1}, \ldots, d_{* m}\right)$ is very complicated - a product of $m$ Bessel functions (Raghunathan (1987), Meng (1988)). Various estimates have been proposed in the literature. Under the equal eigenvalue assumption, Li (1985) and Rubin (1987) derived the method of moments estimates given in (1.23); Raghunathan (1987) gave an approximate MLE using a simple approximation to the Bessel function; and Meng (1988) showed how to obtain the exact MLE by applying the EM algorithm. But none of these estimates are in simple form, and the corresponding distributions of the approximations are not. tractable.

Here, we adopt a different approach. We first simplify the distribution of $d_{* \ell}$ using a normal approximation to $\sqrt{d_{* \ell}}(\ell=1, \ldots, m)$, and then obtain a simple estimate of $\bar{\lambda}$ by a further approximation. Although we derive $\hat{D}_{d}$ under the equal eigenvalue assumption, we show in Section 2.5 that $\hat{D}_{d}$ can be motivated without this restriction.

From (1.7)-(1.8), one can show, for all $\theta$ and $\theta_{0}$, that

$$
d_{* \ell} \mid X_{\text {obs }}, \theta \sim \text { i.i.d. } \bar{\lambda} \chi_{k, \delta / \bar{\lambda}}^{2}
$$

where the noncentrality parameter of the $\chi^{2}$ random variable is $\delta / \bar{\lambda}$ with

$$
\delta=\left(\hat{\theta}_{\mathrm{obs}}-\theta_{0}\right)^{t} \bar{U}^{-1}\left(\hat{\theta}_{\mathrm{obs}}-\theta_{0}\right)
$$

Using a normal approximation to the non-central chi random variable (Patnaik (1949)), we obtain

$$
\sqrt{d_{* \ell}} \mid X_{\mathrm{obs}}, \theta \sim \text { i.i.d. } N\left(\mu, \sigma^{2}\right),
$$

where

$$
\begin{gathered}
\mu=\{(k-1) \bar{\lambda}+\delta+\tau\}^{1 / 2} \\
\sigma^{2}=\bar{\lambda}-\tau
\end{gathered}
$$

and

$$
\tau=\frac{\bar{\lambda}^{2}}{2(\bar{\lambda}+\delta / k)}=\frac{\bar{\lambda}^{2}}{2\left(\bar{\lambda}+(1+\bar{\lambda}) D_{m}^{\infty}\right)}
$$

where the last step follows because $D_{m}^{\infty}=\delta /[k(1+\bar{\lambda})]$, as given in (1.20). Thus for large $k$ and small $\bar{\lambda}$, the sample mean and sample variance of the $\sqrt{d_{* \ell}}$ are sufficient statistics for $\mu$ and $\sigma^{2}$.

From (2.8), $\tau$ is relatively small compared to $\bar{\lambda}$ in most the cases of importance because (i) in common practice, $\bar{\lambda}$ is less than 1 (corresponding to a maximum of $50 \%$ missing information), and (ii) $D_{m}^{\infty}$ is large when the ideal test statistic is close to traditional values for significance. In fact one can easily show that $\tau / \bar{\lambda}<\bar{\lambda} /(2(1+2 \bar{\lambda}))<1 / 6$ when $\bar{\lambda} \leq 1$ and $D_{m}^{\infty} \geq 1$. If we set $\tau$ to zero, as we shall further justify in the next section, then by (2.5) - (2.7), we obtain

$$
\sqrt{d_{* \ell}} \mid X_{\mathrm{obs}}, \theta \sim \text { i.i.d. } N\left([(k-1) \bar{\lambda}+\delta]^{1 / 2}, \bar{\lambda}\right)
$$

which provides the very simple estimate of $\left(1+m^{-1}\right) \bar{\lambda}$ given by $\hat{r}_{d}$ in (2.2). Replacing $r_{m}$ in (1.22) by $\hat{r}_{d}$ gives $\hat{D}_{d}$ in (2.1).

### 2.3. Behavior of $\hat{D}_{d}$ when $m \rightarrow \infty$ - Theory with equal eigenvalues

Although the case of $m=\infty$ is of no practical interest, it can be used to ascertain the degradation in performance of a procedure with finite $m$. Also, theoretically, the consistency of a general test procedure is desirable, in the sense that $\hat{D}_{d}$ should ideally be close to $D_{\text {obs }}$ when $m=\infty$. We will show that $D_{d}^{\infty}$ is very close to $D_{m}^{\infty}$ and hence, as discussed in Section 1.5, very close to $D_{\text {obs }}$.

From (1.7), (1.8) and (1.21), one can show that

$$
E\left(d_{* \ell} \mid X_{\mathrm{obs}}, \theta\right)=\bar{\lambda}(k+\delta / \bar{\lambda})=k\left(\bar{\lambda}+(1+\bar{\lambda}) D_{m}^{\infty}\right) .
$$

Thus, when $m \rightarrow \infty$, from the strong law of large numbers, $\hat{D}_{d}$ converges almost surely to (conditional on $X_{\text {obs }}$ and $\theta$ )

$$
\begin{aligned}
D_{d}^{\infty} & =\frac{\frac{1}{k} E\left(d_{* \ell} \mid X_{\mathrm{obs}}, \theta\right)-\operatorname{Var}\left(\sqrt{d_{* \ell}} \mid X_{\mathrm{obs}}, \theta\right)}{1+\operatorname{Var}\left(\sqrt{d_{* \ell}} \mid X_{\mathrm{obs}}, \theta\right)} \\
& =D_{m}^{\infty}+R
\end{aligned}
$$

where

$$
R=\frac{\left(\bar{\lambda}-\operatorname{Var}\left(\sqrt{d_{* \ell}} \mid X_{\mathrm{obs}}, \theta\right)\right)\left(1+D_{m}^{\infty}\right)}{1+\operatorname{Var}\left(\sqrt{d_{* \ell}} \mid X_{\mathrm{obs}}, \theta\right)}
$$

From equations (2.11) and (2.12) it is clear that if $R$ is small, then $D_{m}^{\infty}$ will be close to $D_{m}^{\infty}$ and hence close to $D_{\text {obs }}$. We now show that $R$ is indeed negligible in most cases of practical importance.

Approximation (2.7) gives $\operatorname{Var}\left(\sqrt{d_{* \ell}} \mid X_{\text {obs }}, \theta\right)=\bar{\lambda}-\tau$, where $\tau$ is given in (2.8). Thus, from (2.12), straightforward algebra shows

$$
R \approx \frac{\bar{\gamma}^{2}\left(1+D_{m}^{\infty}\right)}{2 D_{m}^{\infty}+1-(1-\bar{\gamma})^{2}}
$$

where $\bar{\gamma}=\bar{\lambda} /(1+\bar{\lambda})$ is the average fraction of missing information. When $D_{m}^{\infty}$ is equal to or larger than its expectation under the null hypothesis (i.e., 1 ), which is certainly true when the ideal test provides any evidence that $\theta \neq \theta_{0}$, it follows that

$$
R \leq \frac{2 \bar{\gamma}^{2}}{3-(1-\bar{\gamma})^{2}} \equiv B(\bar{\gamma}) \quad(\text { say })
$$

Notice that $B(\bar{\gamma})$ is a monotone increasing function with maximal value $B(1)= 2 / 3$. In common practice, $B(\bar{\gamma})$ usually is very small because $\bar{\gamma}$ is typically less than $30 \%$. In fact, $B(0.3)=0.07$, which is clearly negligible compared to $D_{m}^{\infty}$.

### 2.4. Checking the theoretical approximation with $m=\infty$ using Monte Carlo

The actual level of a nominal $\alpha$ test based on $D_{d}^{\infty}$ with the $\chi_{k}^{2} / k$ reference distribution is

$$
\operatorname{Pr}\left\{k D_{d}^{\infty}>\chi_{k}^{2}(1-\alpha) \mid \theta=\theta_{0}\right\}
$$

where $\chi_{k}^{2}(1-\alpha)$ is the $100(1-\alpha)$ percentage point of the chi-square distribution with $k$ degrees of freedom. Now, under the null hypothesis $\theta=\theta_{0}$, and assuming $\lambda_{j}=\bar{\lambda}$,

$$
\left(\delta \mid \theta=\theta_{0}, \lambda_{j}=\bar{\lambda}\right) \sim(1+\bar{\lambda}) \chi_{k}^{2} .
$$

Hence, the probability (2.14) can be evaluated numerically for any fixed $\bar{\lambda}$ or equivalently fixed $\gamma_{j}=\bar{\gamma}$.

Table 1 provides the actual level when $\lambda_{j}=\bar{\lambda}$ for nominal $1 \%, 5 \%$ and $10 \%$ tests for various combinations of $\bar{\gamma}$ and $k$ obtained by numerically evaluating (2.14) using Monte Carlo techniques. To accomplish this, we generated $\delta$ from $(1+\bar{\lambda}) \chi_{k}^{2}$ and computed $D_{d}^{\infty}$ and $D_{\text {obs }}$ (which equals to $D_{m}^{\infty}$ under the equal eigenvalue assumption) for 10,000 draws of $\delta$ for each choice of $\bar{\gamma}=0.1,0.2,0.3$ and 0.5 and $k=2,3,5,7,10,15,20$ and 25 . Overall, the levels seem to be well calibrated, although slightly on the conservative side for small $\bar{\gamma}$ and anticonservative for large $k$ and large $\bar{\gamma}$. Table 2 provides correlation coefficients between $D_{\text {obs }}$ and $D_{d}^{\infty}$ for various choices of $\bar{\gamma}$ and $k$. Overall, it seems that the correlations are high for small $k$ and decrease as $k$ increases.

### 2.5. Extensions to unequal eigenvalue cases

Equations (2.10) - (2.12) are valid even when the fractions of missing information are not equal, since they are derived directly from the general distributional assumptions (1.7) and (1.8) of Section 1.3. An analogue of (2.13) can be obtained by the delta method (or by applying Patnaik's (1949) technique) as follows. Using the notation of Section 1.3, let $\Gamma$ be an orthogonal transformation matrix such that $\Gamma \bar{U}^{-1 / 2} B \bar{U}^{-1 / 2} \Gamma^{\prime}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{k}\right)$, and $\Delta \equiv \Gamma \bar{U}^{-1 / 2}\left(\hat{\theta}_{\text {obs }}-\theta_{0}\right)$, a function of $X_{\text {obs }}$. Let $\beta_{\Delta, \lambda}$ be the slope of the regression of $\Delta$ on $\lambda$ and $C V_{\xi}$ be the coefficient of variation of the $\xi$. Then we have

$$
\operatorname{Var}\left(\sqrt{d_{* \ell}} \mid X_{\text {obs }}, \theta\right) \approx \bar{\lambda}-\tau^{*},
$$

where

$$
\tau^{*}=\frac{\bar{\lambda}^{2}-(1+\bar{\lambda})^{2}\left(1+2 \beta_{\Delta, \lambda}\right) C V_{\xi}^{2}}{2\left(\bar{\lambda}+(1+\bar{\lambda}) D_{m}^{\infty}\right)},
$$

which reduces to $\tau$ of (2.8) when all $\lambda_{i}=\bar{\lambda}$. Substituting these two expressions into (2.12), we obtain

$$
R \approx \frac{\left[\bar{\gamma}^{2}-\left(1+2 \beta_{\Delta, \lambda}\right) C V_{\xi}^{2}\right]\left(1+D_{m}^{\infty}\right)}{2 D_{m}^{\infty}+1-(1-\bar{\gamma})^{2}+\left(1+2 \beta_{\Delta, \lambda}\right) C V_{\xi}^{2}}
$$

This expression indicates that $R$ is still negligible under the null hypothesis, because $E\left(\beta_{\Delta, \lambda} \mid \theta=\theta_{0}\right)=0$, and $C V_{\xi}^{2}$ typically is small. In fact one can show that $C V_{\xi}^{2} \leq \bar{\gamma}-2 \bar{\gamma}^{2}$ when all $\lambda_{i}$ are less than 1 . Assuming $\beta_{\Delta, \lambda}=0$ and $D_{m}^{\infty} \geq 1$, we obtain from (2.15) that

$$
|R| \leq \frac{\left|\bar{\gamma}^{2}-C V_{\xi}^{2}\right|}{3-(1-\bar{\gamma})^{2}+C V_{\xi}^{2}} \equiv \tilde{B}\left(\bar{\gamma}, C V_{\xi}^{2}\right) \quad \text { (say) }
$$

It is interesting to notice that $\tilde{B}\left(\bar{\gamma}, C V_{\xi}^{2}\right)$ is usually smaller than $B(\bar{\gamma})(= \tilde{B}(\bar{\gamma}, 0)$ ), since $C V_{\xi}^{2}$ is positive and small. When $\bar{\gamma} \leq 30 \%$, using the facts $B(\bar{\gamma}) \leq 0.07$ and $C V_{\xi}^{2} \leq \bar{\gamma}-2 \bar{\gamma}^{2}$, one can show that $\tilde{B}\left(\bar{\gamma}, C V_{\xi}^{2}\right) \leq 0.07$, that is the same bound holds for $\tilde{B}$ as for $B$. This result suggests that the approximation in (2.15) is often more accurate than the approximation in (2.13).

Monte Carlo simulations are difficult to perform with unequal eigenvalues because $E\left(\sqrt{d_{* \ell}} \mid X_{\text {obs }}, \theta\right)$ is hard to evaluate. It is not clear, however, whether performing such computationally arduous comparisons of $D_{d}^{\infty}$ and $D_{\text {obs }}$ when the eigenvalues are unequal is worthwhile since $D_{d}^{\infty}$ is primarily of interest as a theoretical procedure, and modest values of $m$ must usually be used in practice. Therefore, we move on to our comparison of $\hat{D}_{d}$ and $D_{\text {obs }}$ for the cases of practical importance with modest $m$ and both equal and unequal eigenvalues.

### 2.6. The reference distribution for $\hat{D}_{d}$ with small $m$

When $m \rightarrow \infty$, the obvious reference distribution is $\chi_{k}^{2} / k$ since it is the correct reference distribution for the ideal test statistic, $D_{\text {obs }}$. For small $m$, some approximations are inevitable, since the exact distribution is intractable and even if it were available, it would depend on nuisance parameters $\left(\lambda_{1}, \ldots, \lambda_{k}\right)$. The reference distribution we use here is an $F$ distribution on $k$ and $a_{k, m} \cdot w_{s}$ degrees of freedom, where

$$
w_{s}=(m-1)\left\{1+\hat{r}_{d}^{-1}\right\}^{2}
$$

and

$$
a_{k, m}=k^{-3 / m}
$$

This form for $w_{s}$ is obtained by replacing $r_{m}$ in $(m-1)\left\{1+r_{m}^{-1}\right\}^{2}$, which is the denominator degrees of freedom of an $F$ reference distribution for $D_{m}$ (Rubin
(1987)), with $\hat{r}_{d}$, in the same way as we did for obtaining $\hat{D}_{d}$; analogous substitution for $r_{m}$ in $w$ given by equation (1.19) leads to essentially the same Monte Carlo results. The extra adjustment factor $a_{k, m}$ is obtained through simulation, and essentially reflects the loss of degrees of freedom due to the fact that we are using a scalar quantity instead of a $k$-dimensional quantity to estimate $\bar{\lambda} ; a_{k, m}$ was chosen to be especially good when $m=3$, since this appears to be the most common value in current practice. Notice that, as $m \rightarrow \infty, a_{k, m} \rightarrow 1$, and for $m \geq 3$

$$
k^{-1} \leq a_{k, m} \leq 1
$$

That is, the adjusted number of degrees of freedom is between the minimum and maximum denominator degrees of freedom.

## 3. Evaluation of Our Procedure for Finite $m$

### 3.1. The level of $\hat{D}_{d}$

The actual level of a nominal $\alpha$ level test based on our procedure is

$$
\operatorname{Pr}\left\{\hat{D}_{d}>F_{k, \eta}(1-\alpha) \mid \theta=\theta_{0}\right\}
$$

where $\eta=a_{k, m} w_{s}$, and $F_{k, \eta}(1-\alpha)$ is the $100(1-\alpha)$ percentage point of the $F_{k, \eta}$ distribution. The procedure is said to have the correct level $\alpha$ if the probability in (3.1) is equal to $\alpha$. Ideally one would hope this is true for every $\alpha$ between 0 and 1 , or at least for common values of $\alpha$ such as $10 \%, 5 \%$ and $1 \%$. From the nature of our procedure, it should be apparent that it will be exceedingly difficult to evaluate (3.1) analytically. Therefore, we use Monte Carlo simulation to evaluate (3.1).

### 3.2. Monte Carlo conditions

Note that without loss of generality, we can let $\theta_{0}=0, \bar{U}=I$ and $B=\operatorname{diag}(\lambda)$. As in Section 2.4, we consider average fractions of missing information, $\bar{\gamma}$, equal to $0.1,0.2,0.3$ and 0.5 , where $50 \%$ missing information represents an extreme case for multiple imputation. We also consider equal and unequal eigenvalues, the latter chosen so that for each value of $k$ considered $(2,3,5,7$, $10,15,20,25)$, the standard deviations of the $\gamma_{i}$ nearly equal $0.12(\min =0.099$, $\max =0.124$ ). Specifically, in the unequal case,

$$
\gamma_{i}=(\bar{\gamma}-0.1)+\gamma_{i}^{*}, \quad i=1, \ldots, k
$$

where the $\gamma_{i}^{*}$ are given in sequence by

| 0.010 | 0.190 | 0.102 | 0.181 | 0.021 | 0.174 | 0.032 | 0.024 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0.250 | 0.031 | 0.056 | 0.032 | 0.351 | 0.021 | 0.052 | 0.203 |
| 0.053 | 0.071 | 0.182 | 0.051 | 0.052 | 0.103 | 0.024 | 0.305 |
| 0.036. |  |  |  |  |  |  |  |

Although the standard deviation of 0.12 may appear modest, especially for large $\bar{\gamma}$, our selection of the $\gamma_{1}, \ldots, \gamma_{k}$ represents extreme situations. For example, when $k=15$ and $\bar{\gamma}=0.5$, the minimum and maximum fractions of missing information are $41 \%$ and $75 \%$ respectively. Some limited experience with real data (e.g., Rubin and Schenker (1987), Treiman, Bielby and Cheng (1987), Heitjan and Rubin (1990), Heitjan and Little (1991)) suggests that with real data, most fractions of missing information are less than $30 \%$. The values of $m$ are $2,3,5$ and 10 , which cover all values likely to be used in practice, and let $\alpha=10 \%, 5 \%$ and $1 \%$.

### 3.3. Steps of the simulation

The basic setup for the simulation is as follows:
Step 1. Generate $\hat{\theta}_{\text {obs }}$ from a normal distribution with mean zero and covariance matrix $I+B=T$. Compute $\operatorname{Pr}\left(\chi_{k}^{2}>D_{\text {obs }}\right)$, the ideal $p$-value, where $D_{\text {obs }}=\hat{\theta}_{\text {obs }}^{t} T^{-1} \theta_{\text {obs }}$. This mimics the situation where our analysis based upon the observed data, $X_{\text {obs }}$, results in ( $\hat{\theta}_{\text {obs }}, T$ ) and the subsequent computation of the ideal $p$-value; $P_{\text {obs }}$ from $D_{\text {obs }}$. This is used as a simulation covariate.
Step 2. Generate $d_{* \ell}$ from its repeated imputation distribution described in Sections 1.3 and 1.6 , where $U_{* \ell}$ is fixed at $I$. This mimics the situation where we have used the complete-data analysis on $m$ completed data sets resulting in chi-square or Wald statistics, $d_{* \ell}, \ell=1, \ldots, m$.
Step 3. Compute the $p$-value, $P_{d}$, based upon $\hat{D}_{d}, \operatorname{Pr}\left\{F_{k, \eta}>\hat{D}_{d}\right\}$, where $\eta$ is given in Section 3.1.
Step 4. Record the $p$-values, ( $P_{\mathrm{obs}}, P_{d}$ ) obtained in Steps 1 and 3.
Step 5. Repeat Steps 1 through $4 N$ times and estimate (3.1) for $\alpha=10 \%, 5 \%$ and $1 \%$.

The simulation was done for $N=5,000$ repetitions with both equal and unequal fractions of missing information. The results of our simulation are described in Tables 3 and 4, which provide the actual levels for various situations when the fractions of missing information are equal and unequal respectively.

### 3.4. Results of the simulation

In general, the exact levels in Tables 3 and 4 suggest that $\hat{D}_{d}$ tends to be conservative for both equal and unequal fractions of missing information. This is more pronounced for $\bar{\gamma}=0.1$ and large $k(\geq 10)$. Furthermore, the extent of conservativeness seems to be a function of the nominal level. For example, for the nominal $5 \%$ tests, the exact levels for $k=10$ range from $3.3 \%$ to $4.3 \%$ when $m$ changes from 2 to 10 , whereas for the nominal $10 \%$ tests, the levels range from $6.9 \%$ to $9.1 \%$. By the results in Section 2, the levels will approach the nominal levels as $m$ increases; however, our results seem to be best when $m=3$, which is as anticipated, since the adjustment factor $a_{k, m}$ was chosen with particular attention to the case $m=3$.

For $\bar{\gamma}=0.2$, the test seems to be somewhat anticonservative for the $1 \%$ nominal level and conservative for the $10 \%$ nominal level with $5 \%$ in between. For $\bar{\gamma}=0.3$ and 0.5 , the test is anticonservative, especially for large $k$. For example when $k=25, m=2$ and $\bar{\gamma}=0.5$, the nominal $1 \%$ test corresponds to an exact $5.2 \%$ test, whereas the nominal $5 \%$ test corresponds to an exact $7.6 \%$ test. There is some nonmonotonicity in the exact levels as $m$ increases, especially for $5 \%$ and $10 \%$ nominal levels. Nevertheless, the performance of $\hat{D}_{d}$ is distinctly superior to the current standard.

To help assess the effect of the various factors on the difference between the nominal and exact levels, we constructed an ANOVA in Table 5 for the $8 \times 4 \times 4 \times 3 \times 2$ factorial design. To measure the difference between the exact and nominal levels we consider

$$
\frac{[z \text { score for the exact level }]-[z \text { score for the nominal level }]}{z \text { score for the nominal level }},
$$

where the $z$ score is the standard normal deviate corresponding to the $p$-value. Since the total sum of squares is small (6.05) relative to the number of differences (768), the variability in differences between the exact and nominal levels is relatively small. The effect of various factors on the differences can be ascertained by the sum of squares associated with various assignable sources.

The results in Table 5 suggest that the major source of differences between the exact and nominal levels is $\bar{\gamma}$, for it explains $58 \%$ of the total variability. The next most important main effect is $\alpha$, closely followed by $m$. Sums of squares associated with various interactions involving $\operatorname{Var}(\gamma)$ also suggest that the test $\hat{D}_{d}$ is somewhat sensitive to the equal eigenvalue assumption, although these interactions are dwarfed by the main effect due to $\bar{\gamma}$.

Correlations between $\hat{D}_{d}$ and both $D_{m}$ and $D_{\text {obs }}$ were examined, and, not surprisingly, are quite low, indicating a substantial loss of power when using
$\hat{D}_{d}$ rather than $D_{m}$. This issue is explored next by examining the conditional performance of $\hat{D}_{d}$ relative to $D_{m}$.

### 3.5. Some evaluations of conditional performance

Despite the approximate attainment of nominal level, our procedure leaves much to be desired because the set $S_{d}$ of $p$-values has so much less information than the set of moments, $S_{m}$. From the frequentist perspective, there will be a substantial loss of power when using $S_{d}$ rather than $S_{m}$, and from the Bayesian perspective, results will be quite sensitive to prior assumptions. The consequences with our procedure, which are visible from our simulations, are that it is poorly calibrated conditionally. In particular, consider any fixed $\lambda$ and repeated samples with (a) estimated fractions of missing information indexed by $\operatorname{Var}\left(\sqrt{d_{* \ell}}\right)$ and (b) $p$-values $P_{m}$ and $P_{d}$. Assuming $P_{d}$ attains nominal levels (unconditionally), when $\operatorname{Var}\left(\sqrt{d_{* \ell}}\right)$ is small, we expect to see too liberal $p$-values from $P_{d}$ relative to $P_{m}$, whereas when $\operatorname{Var}\left(\sqrt{d_{* \ell}}\right)$ is large, we expect to see too conservative $p$-values relative to $P_{m}$. When considering a variety of values of $\lambda$, we expect to see a similar trend.

Figures 1a and 1b display the difference between $P_{d}$ and $P_{m}$ for all $\bar{\lambda}$ values from our simulation with $m=3$ (which is approximately calibrated unconditionally), for $k=5$ and 20 , respectively. Attempts can be made to adjust these results to create a conditionally conservatively calibrated procedure, but such attempts typically lead to worse calibration unconditionally, as with the fiducial solution to the Behrens-Fisher problem.

The real culprit is the extreme loss of information when going from $S_{m}$ to $S_{d}$, and some remedies are suggested in the next and final section.

## 4. Discussion

### 4.1. Conclusions and practical guidance on the use of our procedure

We have described a procedure for computing the $p$-value when only comp-leted-data test statistics, $\left\{d_{* \ell}, \ell=1, \ldots, m\right\}$, are available. The procedure is simple and performs reasonably well for a variety of situations described by the values of $m$, the number of imputations, $k$, the dimensionality of the parameter, and $\bar{\gamma}$, the average fraction of missing information, and for both equal and unequal fractions of missing information. The simulation study shows that the fraction of missing information is the most important factor in the performance of this procedure.

Our procedure is, nevertheless, far from what might be hoped for. Its calibration is only approximate, and moreover, not ideal conditionally given the estimated fraction of missing information. Also, because of its noisy relation
with $D_{m}$, the moment-based procedure, we know there will be a substantial power loss compared with $D_{m}$. As a result, we recommend that $\hat{D}_{d}$ be used primarily as a screening test statistic, thinking of it as providing a range of $p$-values between one-half and twice the observed $P_{d}$. If this range is not sharp enough, then ideally the researcher should use a more accurate procedure, for example $D_{m}$ based on $S_{m}$, the set of moments. If $S_{m}$ is not available, but only $S_{d}$, other work reported in Section 4.2 suggests that extensive efforts may be required to do much better than our procedure - the loss of information going from $S_{m}$ to $S_{d}$ is great. Of these, a fully Bayesian procedure is the most theoretically satisfactory (e.g., Raghunathan (1987)).

Another class of methods is based on obtaining information in addition to $S_{d}$ but short of $S_{m}$. These methods are briefly discussed in Section 4.3 and have promise.

### 4.2. Other methods based on $\boldsymbol{S}_{\boldsymbol{d}}$

Li (1985) describes other procedures primarily motivated by the frequentist perspective. Note that when the fractions of missing information are equal, the ideal $p$-value is

$$
P_{\mathrm{obs}}=\operatorname{Pr}\left(\chi_{k}^{2}>\delta(1-\bar{\gamma})\right)
$$

where $\delta=\left(\hat{\theta}_{\text {obs }}-\theta_{0}\right)^{t} U^{-1}\left(\hat{\theta}_{\text {obs }}-\theta_{0}\right)$ and $\bar{\gamma}$ is the common fraction of missing information. Hence, a version of $P_{\text {obs }}$ based only on $\left\{d_{* \ell}, \ell=1, \ldots, m\right\}$ can be obtained by first obtaining estimates of $\delta$ and $\bar{\gamma}$ and then substituting these estimates in (4.1). Li (1985) provides several estimates of $\delta$ and $\bar{\gamma}$, none of which are superior to the procedure described in Section 2; in some regions of the space formed by values of $(k, m, \bar{\gamma})$, they are overly conservative or overly liberal. A main reason for the poor performance of such methods is their failure to account for the uncertainty introduced by the substitution of estimates for $\delta$ and $\bar{\gamma}$. The procedure described in this paper corrects this by considering an $F$ distribution rather than a chi-square distribution.

Raghunathan (1987) provides procedures motivated by the Bayesian perspective. The posterior density of $(\delta, \bar{\gamma})$, for a uniform prior, can be shown to be

$$
\begin{aligned}
P\left(\delta, \bar{\gamma} \mid S_{d}\right) \propto\left(\bar{\gamma}^{-1}-1\right)^{m / 2} \delta^{-m(k-2) / 4} & \exp \left\{-\frac{1}{2}\left(\bar{\gamma}^{-1}-1\right)\left(\bar{d}_{m}+\delta\right)\right\} \\
& \cdot \prod_{i=1}^{m} I_{(k-2) / 2}\left[\sqrt{d_{* \ell} \delta}\left(\bar{\gamma}^{-1}-1\right)\right]
\end{aligned}
$$

where

$$
I_{q}(x)=\sum_{j=0}^{\infty} \frac{(x / 2)^{q+2 j}}{\Gamma(j+1) \Gamma(j+q+1)}
$$



is the modified Bessel function of the first kind. The Bayesian $p$-value based on $S_{d}$ is obtained as

$$
\int \operatorname{Pr}\left(\chi_{k}^{2}>\delta(1-\bar{\gamma})\right) \cdot \operatorname{Pr}\left(\delta, \bar{\gamma} \mid S_{d}\right) d \delta d \bar{\gamma}
$$

Numerical integration techniques can be used to evaluate the above integral. Raghunathan (1987) develops various approximations to the above integral and investigates their frequency properties. Overall, they tend to be conservative for large $k$ and liberal for small $k$. A serious disadvantage of this approach is its sensitivity to the prior specifications for $(\delta, \bar{\gamma})$. Since usually the number of imputations $m$ is small, say less than 5 , the prior distribution for $(\delta, \bar{\gamma})$ plays a very prominent role and can drastically alter the performance in terms of frequency properties for a slight change in the prior specifications.

An easily implemented Monte Carlo algorithm is described in Meng (1988) for approximating the above integral. It is derived based upon the decomposition of $d_{* \ell}, \ell=1, \ldots, m$, with $\bar{\lambda}=\bar{\gamma} /(1-\bar{\gamma})$,

$$
d_{* \ell}=\bar{\lambda} \chi_{k-1}^{2}+[N(\sqrt{\delta}, \bar{\lambda})]^{2} .
$$

It is also shown that its frequency properties are sensitive to the choice of prior for $\bar{\gamma}$. Meng (1988) also discusses several approximations based on the maximum likelihood estimate of $\delta$ and $\bar{\lambda}$ (obtained using the EM algorithm) and the associated observed Fisher information matrix. Bayesian versions are also considered. These procedures work well for not too small $m$.

Meng (1988) also proposes a translated $F$ reference distribution for $\hat{D}_{d}$, derived using the same normal approximation for the distribution of $\sqrt{d_{* \ell}}$. This reference distribution is more accurate than the $F$ reference distribution given here for large values of $\bar{\gamma}$. Unfortunately, this reference distribution does not converge to the ideal reference distribution when $m \rightarrow \infty$, although they are quite close.

### 4.3. Methods based on more information than $S_{d}$ but less than $S_{m}$

As we mentioned before, the loss of information from $S_{m}$ to $S_{d}$ is extreme, especially when $k$ is large and $m$ is small. This should be clear since $S_{m}$ contains all $k$-dimensional vectors and their normalizing matrices, whereas $S_{d}$ consists of only the normalized scalar distances of these vectors from $\theta_{0}$. This severe loss of information is responsible for the poor performance of the existing procedures, including $\hat{D}_{d}$, and makes the problem a very difficult one.

Clearly, the only way to overcome this inherent difficulty is to obtain more information. Ideally, of course, we would have the collection of the moments,
$S_{m}$, but this is impossible in cases when the covariance matrices are not available. Fortunately, however, it is possible in some cases of practical importance to obtain some extra information, which is less than $S_{m}$, but is enough to approximate $D_{m}$ well. The key idea is that all we want is the scalar test statistic $D_{m}$ of (1.22), and the only quantity there that is not directly obtainable form $S_{d}$ is $r_{m}$ of (1.18).

One such kind of procedure has been proposed recently in Meng and Rubin (1990). The basic requirement of this new procedure is that besides $S_{d}$, one also has (i) the collection of the $m$ estimates $\hat{\theta}_{* \ell}$ and (ii) computer code for evaluating the complete-data likelihood ratio test statistic as a function of parameter estimates. This is often feasible in practice since all it requires is the completedata computations for scalar quantities. It is shown in Meng and Rubin (1990) that in large samples, the $r_{m}$ of (1.18) is proportional to the difference between the average of $m$ complete-data log-likelihood ratios, $\bar{d}_{m}$, and the average of $m$ complete-data log-likelihood ratios, each evaluated at the average of $m$ estimates, where the proportionality constant is a simple function of $k$ and $m$. Based on this result, an approximate likelihood ratio test is constructed, and it is shown to be asymptotically equivalent to $D_{m}$ for any number of multiple imputations.

A common situation in practice is that the standard complete-data analyses provide not only the significance levels, but also the estimates $\hat{\theta}_{* \ell}$ and their standard errors (the diagonal elements of $U_{* \ell}$ ), but neither the entire covariance matrix $U_{* \ell}$ nor the code for evaluating the complete-data likelihood ratio test statistic as a function of parameter estimates. These estimates and standard errors certainly provide more information than does $S_{d}$ alone, and one would expect, therefore, to be able to obtain better test procedures using them. The construction of such test procedures and their evaluation are still open questions, although they are under current investigation.

## Acknowledgements

We wish to thank the reviewers for exceptionally helpful comments on an earlier draft of this paper. This work was partially supported by U.S. N.S.F. grants SES-83-11428 and SES-880543, and partially by Joint Statistical Agreements 87-07, 88-02, 89-08, and 90-23 between the U.S. Bureau of the Census and Harvard University.

Table 1. Levels of $\hat{D}_{d}$ when $m=\infty$ as a function of the nominal level, $\alpha$; the dimension, $k$; and the fraction of missing information $\bar{\gamma}$. (Based on 10,000 draws of $\delta$.) Equal fractions of missing information.
| $\alpha$ | $\boldsymbol{k} \boldsymbol{\gamma}$ | 0.1 | 0.2 | 0.3 | 0.5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1\% | 2 | 0.9 | 0.9 | 0.8 | 1.0 |
|  | 3 | 0.9 | 0.9 | 0.9 | 1.1 |
|  | 5 | 1.0 | 1.0 | 0.9 | 1.2 |
|  | 7 | 1.0 | 1.0 | 0.9 | 1.0 |
|  | 10 | 1.0 | 1.0 | 1.0 | 1.3 |
|  | 15 | 1.0 | 1.0 | 1.0 | 1.0 |
|  | 20 | 1.0 | 1.0 | 1.0 | 1.4 |
|  | 25 | 1.0 | 1.0 | 1.0 | 1.5 |
| 5\% | 2 | 4.8 | 4.8 | 4.8 | 5.6 |
|  | 3 | 5.2 | 4.8 | 4.8 | 5.8 |
|  | 5 | 5.1 | 4.8 | 5.0 | 5.9 |
|  | 7 | 5.1 | 5.0 | 5.1 | 6.1 |
|  | 10 | 5.0 | 5.0 | 4.9 | 5.8 |
|  | 15 | 5.0 | 5.0 | 4.9 | 6.1 |
|  | 20 | 5.0 | 5.0 | 4.9 | 6.1 |
|  | 25 | 5.0 | 5.0 | 4.8 | 6.1 |
| 10\% | 2 | 9.8 | 9.8 | 10.0 | 10.8 |
|  | 3 | 9.9 | 9.8 | 10.2 | 11.2 |
|  | 5 | 9.8 | 9.8 | 10.3 | 11.3 |
|  | 7 | 9.7 | 9.9 | 10.4 | 11.4 |
|  | 10 | 9.6 | 9.8 | 10.3 | 11.8 |
|  | 15 | 9.5 | 9.7 | 10.4 | 11.8 |
|  | 20 | 9.5 | 9.6 | 10.8 | 11.7 |
|  | 25 | 9.4 | 9.6 | 10.9 | 11.1 |


Table 2. Correlation coefficients between $D_{\text {obs }}$ and $\hat{D}_{d}$ when $m=\infty$ as a function of the dimension $k$ and the fraction of missing information, $\bar{\gamma}$. Equal fractions of missing information.
| $k>\bar{\gamma}$ | 0.1 | 0.2 | 0.3 | 0.5 |
| :---: | :---: | :---: | :---: | :---: |
| 2 | 0.998 | 0.998 | 0.998 | 0.997 |
| 3 | 0.971 | 0.981 | 0.998 | 0.921 |
| 5 | 0.962 | 0.988 | 0.996 | 0.905 |
| 7 | 0.892 | 0.976 | 0.988 | 0.896 |
| 10 | 0.891 | 0.892 | 0.921 | 0.821 |
| 15 | 0.876 | 0.872 | 0.904 | 0.831 |
| 20 | 0.772 | 0.802 | 0.872 | 0.781 |
| 25 | 0.792 | 0.821 | 0.872 | 0.761 |


Table 3. Level (in \%) of $\hat{D}_{d}$ with $F$ reference distribution as a function of the nominal level, $\alpha$; the dimension, $k$; the number of imputations, $m$; and the fraction of missing information, $\bar{\gamma}$. Equal fractions of missing information.
| $m=2$ |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | $\boldsymbol{k}$ | 0.1 | 0.2 | 0.3 | 0.5 |
| 1\% | 2 | 0.9 | 1.4 | 1.7 | 2.4 |
|  | 3 | 0.7 | 1.4 | 1.8 | 2.8 |
|  | 5 | 0.8 | 1.2 | 1.8 | 3.4 |
|  | 7 | 0.8 | 1.1 | 2.1 | 4.0 |
|  | 10 | 0.7 | 1.3 | 2.3 | 4.9 |
|  | 15 | 0.7 | 1.3 | 2.3 | 5.4 |
|  | 20 | 0.7 | 1.7 | 2.7 | 5.3 |
|  | 25 | 0.6 | 1.9 | 3.5 | 5.5 |
| 5\% | 2 | 5.1 | 5.1 | 5.7 | 6.5 |
|  | 3 | 4.5 | 5.4 | 5.8 | 8.0 |
|  | 5 | 4.4 | 4.9 | 6.0 | 7.9 |
|  | 7 | 4.3 | 4.8 | 6.5 | 8.6 |
|  | 10 | 3.7 | 5.1 | 6.9 | 9.1 |
|  | 15 | 3.6 | 5.1 | 6.1 | 9.1 |
|  | 20 | 3.2 | 5.4 | 6.5 | 8.0 |
|  | 25 | 3.0 | 5.0 | 7.3 | 8.0 |
| 10\% | 2 | 10.3 | 9.8 | 10.9 | 11.5 |
|  | 3 | 9.3 | 10.1 | 11.1 | 12.2 |
|  | 5 | 9.1 | 9.6 | 10.7 | 12.6 |
|  | 7 | 8.2 | 9.5 | 10.9 | 12.7 |
|  | 10 | 7.9 | 9.4 | 11.3 | 12.8 |
|  | 15 | 7.8 | 8.9 | 9.9 | 12.0 |
|  | 20 | 6.5 | 8.5 | 9.5 | 10.3 |
|  | 25 | 6.0 | 8.5 | 10.4 | 10.3 |


Table 3. Level (in \%) of $\hat{D}_{d}$ with $F$ reference distribution as a function of the nominal level, $\alpha$; the dimension, $k$; the number of imputations, $m$; and the fraction of missing information, $\bar{\gamma}$. Equal fractions of missing information.
| $m=3$ |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | $\boldsymbol{k}$ | 0.1 | 0.2 | 0.3 | 0.5 |
| 1\% | 2 | 0.9 | 1.4 | 1.6 | 1.5 |
|  | 3 | 0.7 | 1.3 | 1.5 | 1.9 |
|  | 5 | 0.8 | 1.5 | 1.7 | 2.4 |
|  | 7 | 0.8 | 1.1 | 2.0 | 3.0 |
|  | 10 | 0.7 | 1.3 | 1.9 | 4.2 |
|  | 15 | 0.8 | 1.2 | 2.1 | 4.5 |
|  | 20 | 0.8 | 1.4 | 2.5 | 4.2 |
|  | 25 | 0.8 | 1.7 | 2.5 | 4.3 |
| 5\% | 2 | 5.4 | 5.2 | 5.6 | 6.1 |
|  | 3 | 5.1 | 5.5 | 6.1 | 6.7 |
|  | 5 | 4.6 | 5.2 | 5.9 | 7.4 |
|  | 7 | 4.4 | 5.2 | 6.2 | 7.4 |
|  | 10 | 4.4 | 4.9 | 6.2 | 8.7 |
|  | 15 | 3.8 | 4.8 | 5.9 | 8.7 |
|  | 20 | 3.6 | 5.1 | 6.6 | 8.1 |
|  | 25 | 3.4 | 4.9 | 6.7 | 7.5 |
| 10\% | 2 | 10.6 | 10.2 | 11.4 | 11.4 |
|  | 3 | 10.1 | 10.1 | 11.3 | 12.4 |
|  | 5 | 9.6 | 9.8 | 11.4 | 12.4 |
|  | 7 | 9.1 | 10.1 | 11.0 | 12.0 |
|  | 10 | 9.2 | 9.4 | 10.8 | 12.5 |
|  | 15 | 8.9 | 9.5 | 10.0 | 12.3 |
|  | 20 | 7.7 | 8.7 | 10.5 | 11.8 |
|  | 25 | 7.4 | 8.7 | 10.6 | 10.6 |


| $m=5$ |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | $\boldsymbol{k}$ | 0.1 | 0.2 | 0.3 | 0.5 |
| 1\% | 2 | 0.8 | 1.2 | 1.3 | 1.6 |
|  | 3 | 0.8 | 1.2 | 1.3 | 2.8 |
|  | 3 | 0.9 | 1.4 | 1.6 | 2.3 |
|  | 7 | 0.8 | 1.2 | 1.7 | 2.2 |
|  | 10 | 0.9 | 1.2 | 2.0 | 3.3 |
|  | 15 | 0.8 | 1.1 | 1.9 | 4.0 |
|  | 20 | 0.8 | 1.4 | 2.2 | 4.2 |
|  | 25 | 0.7 | 1.4 | 2.4 | 4.1 |
| 5\% | 2 | 5.2 | 5.5 | 5.5 | 5.8 |
|  | 3 | 5.1 | 5.7 | 6.2 | 6.7 |
|  | 5 | 4.9 | 5.0 | 5.8 | 7.1 |
|  | 7 | 4.7 | 5.3 | 6.3 | 7.5 |
|  | 10 | 4.5 | 5.4 | 6.4 | 8.0 |
|  | 15 | 4.3 | 5.1 | 7.0 | 8.7 |
|  | 20 | 4.2 | 5.3 | 7.0 | 9.1 |
|  | 25 | 4.2 | 5.3 | 6.8 | 8.5 |
| 10\% | 2 | 10.8 | 10.5 | 11.2 | 10.9 |
|  | 3 | 10.3 | 11.0 | 11.4 | 12.8 |
|  | 5 | 9.8 | 10.6 | 11.4 | 13.2 |
|  | 7 | 9.6 | 10.7 | 11.5 | 13.1 |
|  | 10 | 9.6 | 10.4 | 11.5 | 12.8 |
|  | 15 | 9.4 | 10.8 | 12.1 | 13.1 |
|  | 20 | 9.0 | 10.3 | 11.4 | 13.5 |
|  | 25 | 8.5 | 10.3 | 11.7 | 12.5 |

![](https://cdn.mathpix.com/cropped/f3b70dab-b337-44ba-a6a7-cf92568afecc-24.jpg?height=861&width=532&top_left_y=1330&top_left_x=1009)

Table 4. Level (in \%) of $\hat{D}_{d}$ with $F$ reference distribution as a function of the nominal level, $\alpha$; the dimension, $k$; the number of imputations, $m$; and the average fraction of missing information, $\bar{\gamma}$. Unequal fractions of missing information.
| $m=2$ |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | $\boldsymbol{k}$ | 0.1 | 0.2 | 0.3 | 0.5 |
| 1\% | 2 | 1.0 | 1.1 | 1.3 | 2.6 |
|  | 3 | 0.7 | 1.1 | 1.5 | 3.1 |
|  | 5 | 0.7 | 1.3 | 1.4 | 3.7 |
|  | 7 | 0.8 | 1.2 | 2.1 | 4.2 |
|  | 10 | 0.6 | 1.4 | 2.1 | 4.5 |
|  | 15 | 0.6 | 1.6 | 2.4 | 5.0 |
|  | 20 | 0.7 | 1.4 | 2.8 | 5.1 |
|  | 25 | 0.6 | 1.9 | 3.2 | 5.2 |
| 5\% | 2 | 5.0 | 4.8 | 5.3 | 7.1 |
|  | 3 | 4.7 | 5.0 | 5.5 | 7.7 |
|  | 5 | 3.7 | 4.7 | 5.6 | 8.1 |
|  | 7 | 3.9 | 5.0 | 6.2 | 9.3 |
|  | 10 | 3.3 | 4.6 | 6.9 | 8.9 |
|  | 15 | 3.5 | 4.8 | 6.3 | 8.0 |
|  | 20 | 2.8 | 4.8 | 6.7 | 7.4 |
|  | 25 | 2.8 | 5.2 | 6.4 | 7.6 |
| 10\% | 2 | 10.3 | 9.4 | 9.9 | 12.3 |
|  | 3 | 9.3 | 9.6 | 9.9 | 12.5 |
|  | 5 | 8.1 | 9.5 | 10.1 | 13.3 |
|  | 7 | 7.7 | 8.9 | 10.1 | 13.3 |
|  | 10 | 6.9 | 8.1 | 10.9 | 12.3 |
|  | 15 | 6.8 | 8.1 | 9.7 | 10.5 |
|  | 20 | 5.8 | 8.2 | 9.6 | 9.5 |
|  | 25 | 5.3 | 8.2 | 9.3 | 9.2 |


Table 4. Level (in \%) of $\hat{D}_{d}$ with $F$ reference distribution as a function of the nominal level, $\alpha$; the dimension, $k$; the number of imputations, $m$; and the average fraction of missing information, $\bar{\gamma}$. Unequal fractions of missing information.
| $m=3$ |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | $\boldsymbol{k} \boldsymbol{\gamma}^{\bar{\gamma}}$ | 0.1 | 0.2 | 0.3 | 0.5 |
| 1\% | 2 | 0.9 | 0.9 | 1.1 | 1.9 |
|  | 3 | 0.8 | 1.2 | 1.2 | 2.4 |
|  | 5 | 0.7 | 1.1 | 1.0 | 2.6 |
|  | 7 | 0.8 | 1.3 | 1.6 | 3.1 |
|  | 10 | 0.7 | 1.0 | 1.8 | 3.5 |
|  | 15 | 0.8 | 1.2 | 1.8 | 3.5 |
|  | 20 | 0.6 | 1.2 | 2.3 | 3.7 |
|  | 25 | 0.5 | 1.6 | 2.7 | 3.9 |
| 5\% | 2 | 5.1 | 4.9 | 5.0 | 6.3 |
|  | 3 | 4.7 | 5.2 | 5.0 | 6.9 |
|  | 5 | 4.1 | 4.9 | 5.3 | 7.2 |
|  | 7 | 4.5 | 5.4 | 5.4 | 8.1 |
|  | 10 | 3.6 | 4.9 | 5.6 | 8.0 |
|  | 15 | 3.6 | 4.2 | 5.8 | 7.0 |
|  | 20 | 3.5 | 4.7 | 6.4 | 6.6 |
|  | 25 | 2.8 | 4.8 | 6.3 | 6.5 |
| 10\% | 2 | 10.6 | 9.8 | 9.9 | 11.2 |
|  | 3 | 9.7 | 9.7 | 10.2 | 12.3 |
|  | 5 | 9.1 | 9.6 | 10.2 | 12.6 |
|  | 7 | 8.5 | 9.6 | 10.2 | 12.9 |
|  | 10 | 7.9 | 8.9 | 10.0 | 12.0 |
|  | 15 | 7.6 | 8.2 | 9.2 | 10.0 |
|  | 20 | 6.9 | 8.3 | 10.2 | 9.5 |
|  | 25 | 6.3 | 8.6 | 10.0 | 8.6 |


| $m=5$ |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | $k$ | 0.1 | 0.2 | 0.3 | 0.5 |
| 1\% | 2 | 0.9 | 1.0 | 1.0 | 1.6 |
|  | 3 | 0.8 | 1.0 | 1.0 | 2.0 |
|  | 5 | 0.8 | 1.1 | 1.2 | 2.2 |
|  | 7 | 0.7 | 1.2 | 1.5 | 2.7 |
|  | 10 | 0.7 | 1.0 | 1.7 | 3.1 |
|  | 15 | 0.8 | 0.9 | 1.4 | 2.9 |
|  | 20 | 0.6 | 0.9 | 2.2 | 3.2 |
|  | 25 | 0.6 | 1.5 | 2.3 | 3.2 |
| 5\% | 2 | 5.2 | 4.8 | 4.9 | 6.2 |
|  | 3 | 4.7 | 5.2 | 5.1 | 6.3 |
|  | 5 | 4.5 | 4.6 | 5.4 | 7.0 |
|  | 7 | 4.5 | 5.2 | 5.7 | 7.9 |
|  | 10 | 4.1 | 4.8 | 5.6 | 8.0 |
|  | 15 | 4.0 | 4.3 | 5.5 | 7.0 |
|  | 20 | 3.9 | 4.6 | 6.2 | 6.9 |
|  | 25 | 3.4 | 4.8 | 6.1 | 6.5 |
| 10\% | 2 | 10.3 | 9.5 | 9.6 | 11.4 |
|  | 3 | 9.9 | 10.1 | 10.1 | 12.6 |
|  | 5 | 9.0 | 9.7 | 10.8 | 12.5 |
|  | 7 | 9.0 | 9.6 | 11.1 | 13.2 |
|  | 10 | 8.5 | 9.8 | 10.1 | 12.9 |
|  | 15 | 8.5 | 9.1 | 9.8 | 10.7 |
|  | 20 | 8.2 | 8.2 | 10.1 | 10.9 |
|  | 25 | 7.4 | 8.7 | 10.2 | 9.3 |


| $m=10$ |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | $\boldsymbol{k} \boldsymbol{\gamma}$ | 0.1 | 0.2 | 0.3 | 0.5 |
| 1\% | 2 | 0.9 | 1.0 | 1.1 | 1.1 |
|  | 3 | 0.7 | 1.0 | 1.1 | 1.1 |
|  | 5 | 0.8 | 0.8 | 1.0 | 1.3 |
|  | 7 | 0.9 | 1.0 | 1.2 | 1.7 |
|  | 10 | 0.7 | 1.0 | 1.1 | 2.6 |
|  | 15 | 0.8 | 0.8 | 1.3 | 2.3 |
|  | 20 | 0.7 | 0.9 | 1.6 | 3.0 |
|  | 25 | 0.7 | 1.1 | 1.8 | 3.0 |
| 5\% | 2 | 5.2 | 4.9 | 5.2 | 5.5 |
|  | 3 | 5.1 | 5.3 | 5.6 | 6.0 |
|  | 5 | 4.5 | 5.4 | 5.7 | 6.7 |
|  | 7 | 4.7 | 5.6 | 5.9 | 8.1 |
|  | 10 | 4.3 | 5.4 | 5.7 | 8.9 |
|  | 15 | 4.5 | 5.3 | 5.5 | 8.4 |
|  | 20 | 4.4 | 5.6 | 6.3 | 9.1 |
|  | 25 | 4.4 | 5.3 | 6.7 | 8.7 |
| 10\% | 2 | 10.7 | 9.8 | 9.9 | 11.0 |
|  | 3 | 10.2 | 10.6 | 11.1 | 11.7 |
|  | 5 | 9.7 | 10.6 | 10.9 | 13.5 |
|  | 7 | 9.5 | 10.8 | 11.4 | 14.7 |
|  | 10 | 9.1 | 11.0 | 11.5 | 15.8 |
|  | 15 | 8.8 | 10.0 | 11.1 | 15.2 |
|  | 20 | 8.9 | 10.7 | 11.8 | 15.0 |
|  | 25 | 9.2 | 10.6 | 12.6 | 14.8 |


Table 5. Analysis of variance table for the relative differences between the exact and nominal levels on the $z$ score.
| Factor | Degrees of freedom | \% of total sum of squares | Ratio of mean square to residual mean square |
| :--- | :--- | :--- | :--- |
| $\boldsymbol{k}$ | 7 | 0.6 | 9 |
| $m$ | 3 | 3.0 | 98 |
| $\bar{\gamma}$ | 3 | 58.1 | 1880 |
| Levels | 2 | 4.7 | 228 |
| Var( $\boldsymbol{\gamma}$ ) | 1 | 0.7 | 73 |
| $\boldsymbol{k} \times \boldsymbol{m}$ | 21 | 1.3 | 6 |
| $\boldsymbol{k} \times \bar{\gamma}$ | 21 | 8.2 | 38 |
| $m \times \bar{\gamma}$ | 9 | 0.6 | 7 |
| $\boldsymbol{k} \times$ Levels | 14 | 3.6 | 25 |
| $m \times$ Levels | 6 | 1.8 | 29 |
| $\bar{\gamma} \times$ Levels | 6 | 1.4 | 23 |
| $\boldsymbol{k} \times \operatorname{Var}(\boldsymbol{\gamma})$ | 7 | 1.5 | 21 |
| $m \times \operatorname{Var}(\gamma)$ | 3 | 0.9 | 28 |
| $\overline{\boldsymbol{\gamma}} \times \operatorname{Var}(\boldsymbol{\gamma})$ | 3 | 1.1 | 36 |
| Levels × $\operatorname{Var}(\boldsymbol{\gamma})$ | 2 | 4.6 | 226 |
| $\boldsymbol{k} \times \boldsymbol{m} \times \bar{\gamma}$ | 63 | 1.2 | 2 |
| $m \times \bar{\gamma} \times$ Levels | 18 | 0.4 | 2 |
| $\boldsymbol{k} \times \bar{\gamma} \times$ Levels | 42 | 0.6 | 1 |
| $\boldsymbol{k} \times \boldsymbol{m} \times$ Levels | 42 | 0.4 | 1 |
| Residual | 494 | 5.3 | 1 |
| Total | 767 |  |  |


![](https://cdn.mathpix.com/cropped/f3b70dab-b337-44ba-a6a7-cf92568afecc-27.jpg?height=783&width=1114&top_left_y=312&top_left_x=344)
Figure 1a. Plot of $P_{d}-P_{m}$ vs $\operatorname{Var}\left(\sqrt{d_{* \ell}}\right)$ for $k=5$.

![](https://cdn.mathpix.com/cropped/f3b70dab-b337-44ba-a6a7-cf92568afecc-27.jpg?height=762&width=1114&top_left_y=1313&top_left_x=346)
Figure 1b. Plot of $P_{d}-P_{m}$ vs $\operatorname{Var}\left(\sqrt{d_{* \ell}}\right)$ for $k=20$.

## References

Aspin, A. A. (1948). An examination and further development of a formula arising in the problem of comparing two mean values. Biometrika 35, 88-96.
Cochran, W. G. (1964). Approximate significance levels of the Behrens-Fisher test. Biometrics 20, 191-195.
Heitjan, D. F. and Little, R. J. A. (1991). Multiple imputation for the fatal accident reporting system. To appear in Applied Statistics.
Heitjan, D. F. and Rubin, D. B. (1990). Inference from coarse data via multiple imputation with application to age heaping. J. Amer. Statist. Assoc. 85, 304-314.
Jeffreys, H. (1940). Note on the Behrens-Fisher formula. Ann. Eugen. 10, 48-51.
Johnson, Palmer O. and Neyman, J. (1936). Tests of certain linear hypotheses and their application to some educational problems. Statistical Research Memoirs 1, 57-93.
Li, K. H. (1985). Hypothesis testing in multiple imputation - with emphasis on mixed-up frequencies in contingency tables. Ph.D. Thesis, Department of Statistics, University of Chicago.
Li, K. H., Raghunathan, T. E. and Rubin, D. B. (1990). Large sample significance levels from multiply-imputed data using moment-based statistics and an $F$ reference distribution. Research Report, Department of Statistics, Harvard University.
Meng, X. L. (1988). Significance levels from repeated significance levels in multiple imputation. Ph.D. Qualifying paper, Department of Statistics, Harvard University.
Meng, X. L. and Rubin, D. B. (1990). Likelihood ratio tests with multiply-imputed data sets. Proceeding of the Statistical Computing Section of the American Statistical Association. To appear.
Patnaik, P. B. (1949). The non-central $\chi^{2}$ - and $F$-distributions and their applications. Biometrika 36, 202-232.
Raghunathan, T. E. (1987). Large sample significance levels from multiply-imputed data. Ph.D. Thesis, Department of Statistics, Harvard University.
Robinson, G. K. (1976). Properties of Student's $t$ and of the Behrens-Fisher solution to the two means problem. Ann. Statist. 4, 963-971.
Rubin, D. B. (1978). Multiple imputations in sample surveys - a phenomenological Bayesian approach to nonresponse. Proceedings of the Survey Research Methods Section of the American Statistical Association, 20-34. Also in Imputation and Editing of Faulty or Missing Survey Data. U.S. Dept. of commerce, Bureau of the Census, 1-23.
Rubin, D. B. (1987). Multiple Imputation for Nonresponse in Surveys. John Wiley, New York.
Rubin, D. B. and Schenker, N. (1987). Interval estimation from multiply-imputed data: a case study using census agriculture industry codes. J. Official Statist. 3, 375-387.
Schenker, N., Treiman, D. J. and Weidman, L. (1988). Evaluation of multiply-imputed publicuse tapes. Proceedings of the American Statistical Association Survey Research Methods Section Annual Meetings, 85-92.
Schenker, N. and Welsh, A. H. (1988). Asymptotic results for multiple imputation. Ann. Statist. 16, 1550-1566.
Smith, H. F. (1936). The problem of comparing the results of two experiments with unequal errors. Council of Scientific and Industrial Research (Australia), Journal 9, 211-212.
Treiman, D. J., Bielby, W. and Cheng, M. (1988). Evaluating a multiple-imputation method for recalibrating 1970 U.S. Census detailed industry codes to the 1980 standard. Sociological

Methodology 18, 309-345.
Wallace, D. L. (1978). The Behrens-Fisher and Feiller-Creasy Problems. An Appreciation of Fisher (Edited by S. F. Fienberg and D. V. Hinkley), 119-147.
Welch, B. L. (1937). The significance of the difference between two means when the population variances are unequal. Biometrika 29, 350-362.
Welch, B. L. (1947). The generalization of "Student's" problem when several different population variances are involved. Biometrika 34, 28-35.
Weld, L. H. (1987). Significance levels for public-use data with multiply-imputed industry codes. Ph.D. dissertation, Department of Statistics, Harvard University.

Department of Statistics, Chinese University of Hong Kong, New Territories, Shatin, Hong Kong.
Department of Statistics, Harvard University, Cambridge, MA 02138, U.S.A.
Department of Biostatistics, University of Washington, Seattle, WA 98195, U.S.A.
Department of Statistics, Harvard University, Cambridge, MA 02138, U.S.A.
(Received October 1989; accepted June 1990)

