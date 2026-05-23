---
citekey: li1991large
authors: 'Li, Kim-Hung; Raghunathan, Trivellore E; Rubin, Donald B'
year: 1991
title: Large-sample significance levels from multiply imputed data using moment-based statistics and an F reference distribution
venue: Journal of the American Statistical Association
volume: 86
issue: 416
pages: 1065–1073
zotero_key: GKW89J7E
item_type: journalArticle
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\li1991large.pdf'
pdf_sha256: e065908d517211f33b92fe65f7ee9c9beb6723f4e96b8b85acbe704045ccb7db
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T22:51:10Z
---
# Large-Sample Significance Levels from Multiply Imputed Data Using Moment-Based Statistics and an F Reference Distribution 

Author(s): K. H. Li, T. E. Raghunathan and D. B. Rubin

Source: Journal of the American Statistical Association, Vol. 86, No. 416 (Dec., 1991), pp. 1065-1073

## Published by: Taylor \& Francis on behalf of the American Statistical Association <br> Stable URL: https://www.jstor.org/stable/2290525

Accessed: 22-05-2026 20:46 UTC

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about TSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms \& Conditions of Use, available at https://about.jstor.org/terms

# Large-Sample Significance Levels From Multiply Imputed Data Using Moment-Based Statistics and an $F$ Reference Distribution 

K. H. LI, T. E. RAGHUNATHAN, and D. B. RUBIN*


#### Abstract

We present a procedure for computing significance levels from data sets whose missing values have been multiply imputed data. This procedure uses moment-based statistics, $m \geq 3$ repeated imputations, and an $F$ reference distribution. When $m=\infty$, we show first that our procedure is essentially the same as the ideal procedure in cases of practical importance and, second, that its deviations from the ideal are basically a function of the coefficient of variation of the canonical ratios of complete to observed information. For small $m$ our procedure's performance is largely governed by this coefficient of variation and the mean of these ratios. Using simulation techniques with small $m$, we compare our procedure's actual and nominal large-sample significance levels and conclude that it is essentially calibrated and thus represents a definite improvement over previously available procedures. Furthermore, we compare the large-sample power of the procedure as a function of $m$ and other factors, such as the dimensionality of the estimand and fraction of missing information, to provide guidance on the choice of the number of imputations; generally, we find the loss of power due to small $m$ to be quite modest in cases likely to occur in practice.


KEY WORDS: Imputation; Missing data; Nonresponse; Tests of significance.

## 1. INTRODUCTION

### 1.1 Background

Missing data are a pervasive problem in statistics with many possible approaches, as discussed, for example, by Little and Rubin (1987). One approach that is especially appropriate with complicated public-use data sets is multiple imputation (Rubin 1978, 1987), which replaces the set of missing values with $m \geq 2$ sets of plausible values. The observed data set supplemented with the $m$ sets of imputations is called a multiply imputed data set and can be used to create $m$ completed data sets. The first set of imputed values together with the observed data forms the first completed data set, the second set of imputed values together with the observed data forms the second completed data set, and so on. Each completed data set can be treated as a standard complete data set and thus can be analyzed using techniques that are appropriate when there are no missing values. For example, using standard complete-data methods, we can obtain $m$ estimates and their variancecovariance matrices or $p$ values, which can be combined to form a single inference under the model used to impute the missing values.

The practical payoffs from using multiple imputation are that (1) only standard complete-data methods of analysis need to be used to analyze each completed data set and (2) satisfactory multiple imputations can often be created relatively easily. A fairly substantial literature, both theoretical and applied, now supports the efficacy of multiple imputation. Rubin (1980), Herzog and Rubin (1983), Heitjan and Rubin (1986), Schenker (1985), Rubin and Schenker (1986, 1987), and Glynn, Laird, and Rubin $(1986,1991)$

[^0]develop, illustrate, and evaluate procedures for scalar parameters. Li (1985), Rubin (1987), Raghunathan (1987), Weld (1987), Treiman, Bielby, and Cheng (1988), and Schenker, Treiman, and Weidman (1988) consider multiparameter situations.

Generally, the conclusions of these investigations are that (1) existing procedures for combining scalar complete-data analyses based on estimates and standard errors work very well, (2) existing procedures for combining $k$-parameter ( $k >1)$ complete-data estimates and variance-covariance matrices to produce $p$ values typically work well for modest $k$ but can use improvement for larger $k$, and (3) existing procedures for directly combining complete-data $p$ values typically work well only for relatively small $k$. Here we focus on the second point; the third point is addressed directly in Li, Meng, Raghunathan, and Rubin (1991) and indirectly in Meng and Rubin (in press).

Our theoretical and simulation investigations show that the parameters that govern the performance of standard multiparameter multiple-imputation test statistics are the $k$ canonical ratios of complete to observed information, where complete information is observed plus missing information. With a large number of imputations, the coefficient of variation of these ratios governs the performance of test statistics, and with a modest number of imputations, the mean of these ratios is also relevant. These facts allow a clearer representation of previous and current results.

### 1.2 Illustrating the Results of Single and Multiple Imputation

To motivate our procedure, consider an $n \times p$ data set with missing values, which is going to be used for many analyses, including, for example, a least squares regression of a dependent variable on a set of independent variables to estimate the $k$-component regression coefficient vector $\theta$. If there were no missing data, the least squares estimate

[^1]would be $\hat{\theta}$ with associated variance-covariance matrix $U$ as produced by a standard least squares regression program; for simplicity we assume that $n$ is large so that $U$ can be regarded as known. The large-sample $p$ value associated with the null value $\theta=\theta_{0}$ would be
$$
P=\operatorname{Pr}\left[\chi_{k}^{2}>\left(\hat{\theta}-\theta_{0}\right)^{t} U^{-1}\left(\hat{\theta}-\theta_{0}\right)\right],
$$
where $\chi_{k}^{2}$ is a $\chi^{2}$ random variable on $k \mathrm{df}$.
Because of missing values in the dependent and independent variables, the complete-data statistics $\hat{\theta}, U$, and $P$ cannot be calculated. A common applied practice is to fill in the missing values, that is, singly impute them, and proceed as if there were no missing data. Such single-imputation techniques can have very poor repeated sampling properties [see Rubin and Schenker (1986) and Rubin (1987, table 4.7)]. In particular, suppose that single imputations are created as well as possible by drawing from the posterior predictive distribution of the missing values, and then (1.1) is applied to the completed data, treating the imputed data as if they were true data. Table 1 provides the actual levels of tests based on (1.1) with such imputed data as a function of (i) the number of components being tested, $k$, (ii) the average ratio of complete information to observed information, $\bar{\xi}$, defined precisely in Section 2, (iii) the coefficient of variation of these ratios across the components of $\theta, C_{\xi}$, and (iv) the nominal level $\alpha$.

Some limited experience suggests that an average ratio of complete to observed information equal to 1.5 , corresponding to $33 \%$ missing information, is relatively unusual,
and that a ratio close to 2 , corresponding to $50 \%$ missing information, is extreme for any real problem of survey nonresponse. Certainly, multiple imputation with modest $m$ (for example, $\leq 5$ ) is not designed to handle more extreme cases. Our choices of variation in ratios of missing information, described in Section 3, include relatively extreme variation based on a range of practical cases. In particular, in our experience with actual data sets that might be addressed using multiple imputation with modest $m$, multicomponent estimands typically have most components exhibiting no missing information and essentially never have any components exhibiting more than $75 \%$ missing information. Suppose that the fractions of missing information are uniform on ( $0, a$ ); then $\bar{\xi}$ is $-\ln (1-a) / a$ and $C_{\xi}$ is ( $a^{2} /(1-$ a) $\left.(\ln (1-a))^{2}-1\right)^{1 / 2}$. The extreme choice of $a=.75$ yields $\bar{\xi}=1.9$ and $C_{\xi}=41.3 \%$; the more modest but still fairly extreme choice of $a=.5$ yields $\bar{\xi}=1.4$ and $C_{\xi}= 20.0 \%$, and $a=.3$ gives $\bar{\xi}=1.2$ and $C_{\xi}=10.3 \%$. Our values of $\bar{\xi}$ and $C_{\xi}$ cover this range of practically important values.

From Table 1 it is clear that even for modest amounts of missing information, the use of single imputation is a prescription for disaster. The reason for the poor performance of single imputation is the underestimation of the variability: the uncertainty in not knowing the missing values is not incorporated. Multiple imputation remedies this by allowing the measurement of the extra component of variability, resulting in a well-calibrated test procedure.

Specifically, suppose that $m$ imputations had been taken

Table 1. Large-Sample Level (in \%) of Single Imputation Methodology as a Function of Nominal Level, $\alpha$; Number of Components Being Tested, $k$; the Average Ratio of Complete to Observed Information, $\xi$; and the Coefficient of Variation of the Ratios, $C_{\xi}$
|  | $\bar{\xi}$ | $\alpha=1 \%$ |  |  | $\alpha=5 \%$ |  |  | $\alpha=10 \%$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 1.2 | 1.5 | 2.0 | 1.2 | 1.5 | 2.0 | 1.2 | 1.5 | 2.0 |
| $C_{\xi}=0 \%$ |  |  |  |  |  |  |  |  |  |  |
| $\boldsymbol{k}$ | 2 | 2.3 | 4.7 | 21.5 | 8.6 | 13.8 | 36.8 | 15.2 | 24.2 | 46.4 |
|  | 5 | 2.7 | 7.4 | 41.2 | 10.7 | 19.2 | 59.8 | 18.2 | 29.2 | 68.9 |
|  | 10 | 4.0 | 11.6 | 65.5 | 13.2 | 28.1 | 80.1 | 22.3 | 39.2 | 86.7 |
|  | 20 | 6.2 | 20.7 | 89.7 | 17.5 | 41.2 | 95.9 | 28.8 | 60.7 | 97.8 |
|  | 35 | 8.8 | 25.1 | 95.7 | 23.5 | 51.6 | 99.2 | 34.3 | 68.8 | 99.2 |
| $C_{\xi}=10 \%$ |  |  |  |  |  |  |  |  |  |  |
| $\boldsymbol{k}$ | 2 | 2.6 | 6.1 | 22.8 | 9.2 | 16.2 | 37.9 | 15.8 | 25.3 | 47.1 |
|  | 5 | 3.4 | 8.4 | 42.8 | 11.4 | 22.3 | 60.7 | 18.9 | 31.2 | 69.9 |
|  | 10 | 4.9 | 13.4 | 67.8 | 15.1 | 31.6 | 83.6 | 21.9 | 39.9 | 87.1 |
|  | 20 | 7.5 | 26.7 | 91.8 | 20.4 | 43.8 | 97.8 | 30.8 | 61.8 | 98.3 |
|  | 35 | 9.4 | 29.4 | 97.2 | 23.8 | 52.3 | 99.2 | 34.9 | 69.9 | 99.9 |
| $C_{\xi}=20 \%$ |  |  |  |  |  |  |  |  |  |  |
| $\boldsymbol{k}$ | 2 | 2.8 | 6.8 | 23.9 | 9.8 | 16.2 | 38.2 | 16.1 | 25.4 | 48.1 |
|  | 5 | 3.5 | 9.2 | 46.4 | 12.3 | 24.3 | 61.8 | 19.2 | 32.3 | 71.2 |
|  | 10 | 5.2 | 14.5 | 71.8 | 17.2 | 33.5 | 84.6 | 23.1 | 40.1 | 89.3 |
|  | 20 | 8.1 | 29.6 | 92.9 | 21.5 | 48.9 | 98.9 | 31.2 | 62.8 | 99.3 |
|  | 35 | 12.3 | 32.3 | 99.2 | 25.6 | 61.4 | 99.2 | 35.6 | 71.1 | 99.9 |
| $C_{\xi}=40 \%$ |  |  |  |  |  |  |  |  |  |  |
| $\boldsymbol{k}$ | 2 | 3.2 | 7.2 | 31.2 | 11.2 | 19.2 | 42.2 | 18.9 | 29.5 | 57.1 |
|  | 5 | 3.7 | 10.3 | 52.3 | 14.4 | 32.4 | 68.8 | 22.3 | 38.4 | 82.2 |
|  | 10 | 5.8 | 16.5 | 80.3 | 21.3 | 43.4 | 91.5 | 28.7 | 49.5 | 99.9 |
|  | 20 | 9.5 | 33.4 | 99.9 | 31.4 | 56.3 | 99.0 | 36.3 | 78.6 | 100.0 |
|  | 35 | 15.3 | 38.9 | 99.9 | 38.6 | 68.4 | 100.0 | 42.2 | 82.6 | 100.0 |


[^2]from the posterior predictive distribution of the missing data to produce $m$ completed data sets and thus $m$ values for $\hat{\theta}$, $\hat{\theta}_{*_{1}}, \ldots, \hat{\theta}_{*_{m}}$ and $m$ associated variance-covariance matrices, $U_{*_{1}}, \ldots, U_{*_{m}}$. Our procedure uses the test statistic
$$
D_{m}=\left(\bar{\theta}_{m}-\theta_{0}\right)^{t} \bar{U}_{m}^{-1}\left(\bar{\theta}_{m}-\theta_{0}\right) /\left[k\left(1+r_{m}\right)\right],
$$
where
$$
\begin{aligned}
\bar{\theta}_{m} & =\sum_{l=1}^{m} \hat{\theta}_{* l} / m, \\
\bar{U}_{m} & =\sum_{l=1}^{m} U_{* l} / m,
\end{aligned}
$$
and
$$
r_{m}=\left(1+m^{-1}\right) \operatorname{tr}\left(B_{m} \bar{U}_{m}^{-1}\right) / k
$$
with
$$
B_{m}=\sum_{l=1}^{m}\left(\hat{\theta}_{*_{l}}-\bar{\theta}_{m}\right)\left(\hat{\theta}_{*_{l}}-\bar{\theta}_{m}\right)^{t} /(m-1) .
$$

The $p$ value associated with $D_{m}$ is

$$
P_{m}=\operatorname{Pr}\left[F_{k, w}>D_{m}\right]
$$

where $F_{k, w}$ is an $F$ random variable on $k$ and $w \mathrm{df}$, where

$$
w=4+(t-4)\left[1+\left(1-2 t^{-1}\right) / r_{m}\right]^{2}
$$

with

$$
t=k(m-1) .
$$

Table 2 presents levels for our procedure, obtained by the simulation described in Section 4, for the exact same
conditions as in Table 1. The contrast is dramatic: our procedure with only $m=3$ is very well calibrated, essentially always within $\pm 1 \%$ of the nominal level. The previous standard for this problem, presented in Rubin (1987), is the statistic $D_{m}$ with $w$ in the reference distribution replaced by

$$
w^{\prime}=(m-1)\left(\frac{k+1}{2}\right)\left(1+1 / r_{m}\right)^{2} .
$$

The use of $w$ rather than $w^{\prime}$ leads to distinctly better results for large $k$. For example, when $m=3, k=35, \bar{\xi}=1.2$, and $C_{\xi}=20 \%$, using $w^{\prime}$ gives a rejection rate of $2.1 \%$ versus $1.4 \%$ when $\alpha=1 \%$, and $7.8 \%$ versus $5.9 \%$ when $\alpha=5 \%$.

### 1.3 Outline

Section 2 presents necessary notation and definitions and derives the procedure introduced in Section 1.2, in particular the new degrees of freedom $w$. Section 3 presents new infinite $m$ properties of $D_{m}$ and shows that in this case it is essentially equal to the ideal procedure with its deviations from this ideal governed by $C_{\xi}$. Section 4 then summarizes Monte Carlo results for finite $m \geq 3$ that show the new procedure to be very well calibrated in cases of practical interest. We also compare the power of the test with that of the ideal test and conclude that usually the loss of power is quite modest.

Table 2. Large-Sample Level (in \%) of Multiple Imputation Methodology Using $D_{m}(m=3)$ With $F$ Reference Distribution as a Function of Nominal Level, $\alpha$; Number of Components Being Tested, $k$; the Average Ratio of Complete to Observed Information, $\bar{\xi}$; and the Coefficient of Variation of the Ratios, $C_{\xi}$
|  | $\bar{\xi}$ | $\alpha=1 \%$ |  |  | $\alpha=5 \%$ |  |  | $\alpha=10 \%$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 1.2 | 1.5 | 2.0 | 1.2 | 1.5 | 2.0 | 1.2 | 1.5 | 2.0 |
| $C_{\xi}=0 \%$ |  |  |  |  |  |  |  |  |  |  |
| $k$ | 2 | 1.1 | 1.2 | 1.5 | 4.7 | 5.1 | 5.6 | 9.7 | 9.9 | 10.4 |
|  | 5 | 1.0 | . 9 | . 8 | 4.4 | 4.5 | 4.1 | 9.4 | 9.4 | 9.0 |
|  | 10 | 1.0 | . 8 | 1.0 | 4.8 | 4.7 | 4.5 | 9.8 | 9.5 | 9.7 |
|  | 20 | 1.1 | 1.1 | 1.0 | 5.2 | 5.2 | 4.9 | 9.7 | 9.7 | 10.1 |
|  | 35 | 1.0 | 1.1 | 1.1 | 5.1 | 4.8 | 5.3 | 9.9 | 9.8 | 9.9 |
| $C_{\xi}=10 \%$ |  |  |  |  |  |  |  |  |  |  |
| $k$ | 2 | . 8 | 1.0 | 1.2 | 4.6 | 4.4 | 5.6 | 9.3 | 9.0 | 10.6 |
|  | 5 | 1.0 | . 8 | 1.2 | 4.7 | 4.4 | 5.2 | 9.3 | 9.2 | 10.1 |
|  | 10 | 1.1 | 1.1 | 1.1 | 5.2 | 4.6 | 5.4 | 10.2 | 9.3 | 10.1 |
|  | 20 | 1.2 | 1.1 | 1.1 | 5.0 | 5.2 | 5.1 | 10.2 | 10.3 | 10.0 |
|  | 35 | . 9 | 1.1 | 1.1 | 5.2 | 4.9 | 5.1 | 9.8 | 9.9 | 10.2 |
| $C_{\xi}=20 \%$ |  |  |  |  |  |  |  |  |  |  |
| $k$ | 2 | 9 | 1.2 | 1.3 | 4.8 | 4.9 | 5.4 | 9.5 | 9.6 | 10.2 |
|  | 5 | 1.2 | 1.0 | . 8 | 5.3 | 5.1 | 4.5 | 10.3 | 9.6 | 9.5 |
|  | 10 | 1.5 | 1.1 | 1.2 | 5.5 | 5.5 | 5.3 | 10.7 | 10.4 | 10.2 |
|  | 20 | 1.3 | 1.3 | 1.2 | 5.9 | 5.4 | 5.4 | 11.2 | 10.6 | 10.7 |
|  | 35 | 1.4 | 1.2 | 1.1 | 5.9 | 5.8 | 5.3 | 11.1 | 10.7 | 10.5 |
| $C_{\xi}=40 \%$ |  |  |  |  |  |  |  |  |  |  |
| $k$ | 2 | 1.3 | 1.6 | 1.6 | 5.1 | 5.0 | 6.7 | 10.3 | 10.0 | 12.0 |
|  | 5 | 1.7 | 1.7 | 1.3 | 6.1 | 5.5 | 5.5 | 10.9 | 10.0 | 11.1 |
|  | 10 | 1.8 | 2.0 | 1.8 | 6.6 | 6.3 | 6.8 | 11.2 | 11.1 | 12.0 |
|  | 20 | 2.1 | 2.1 | 1.9 | 7.4 | 7.7 | 6.9 | 12.9 | 13.0 | 12.1 |
|  | 35 | 2.5 | 2.1 | 2.1 | 7.3 | 7.3 | 7.4 | 12.6 | 12.9 | 12.9 |


NOTE: Based on 10,000 independent Monte Carlo draws for each combination of $k, \bar{\xi}$, and $C_{\xi}$.

## 2. DISTRIBUTIONAL CONSIDERATIONS

### 2.1 The Complete-Data Case

Let $X$ be an $n \times p$ data matrix with distribution governed by an unknown $k$-component parameter $\theta$. We assume throughout that $n$ is large enough to justify standard largesample approximations. In particular, letting $\hat{\theta}=\hat{\theta}(X)$ be the complete-data maximum likelihood (ML) estimate of $\theta$ with associated complete-data variance-covariance matrix $U=U(X)$ (for example, the inverse of the observed com-plete-data information), we assume that the complete-data inference based on $\hat{\theta}$ and $U$ is valid in the sense that

$$
\left(\hat{\theta} \mid \theta=\theta_{t}\right) \sim N\left(\theta_{t}, U_{t}\right)
$$

and

$$
\left(U \mid \theta=\theta_{t}\right) \approx U_{t},
$$

where $\approx$ means equal in the sense of lower-order variability, and the subscripts $t$ on $\theta$ and $U$ designate the true values of $\theta$ and $V\left(\hat{\theta} \mid \theta=\theta_{t}\right)$, respectively; $U_{t}^{-1}$ is the completedata information. The $p$ value associated with the null value of $\theta, \theta_{0}$, can be calculated as

$$
P=\operatorname{Pr}\left[\chi_{k}^{2} / k>D(X)\right],
$$

where the quadratic form

$$
D=D(X)=\left(\hat{\theta}-\theta_{0}\right)^{t} U^{-1}\left(\hat{\theta}-\theta_{0}\right) / k
$$

is proportional to the Wald test statistic. All of our results apply to inference for a subvector of $\theta$, but the additional notation needed to represent this case clutters expressions with no new insight.

### 2.2 The Incomplete-Data Case

When some components of $X$ are missing, none of the complete-data statistics, $\hat{\theta}, U, D$, or $P$, can be calculated. Suppose that based on the observed data, $X_{\text {obs }}$, the ML estimate of $\theta$ is $\hat{\theta}_{\text {obs }}$, with associated variance-covariance matrix $T=T\left(X_{\text {obs }}\right)$ (for example, the negative second derivative of the observed-data log-likelihood at $\hat{\theta}_{\text {obs }}$ ). Applying standard asymptotic results we have

$$
\left(\hat{\theta}_{\mathrm{obs}} \mid \theta=\theta_{t}\right) \sim N\left(\theta_{t}, T_{t}\right)
$$

and

$$
\left(T \mid \theta=\theta_{t}\right) \approx T_{t},
$$

where

$$
T_{t}=V\left(\hat{\theta}_{\mathrm{obs}} \mid \theta=\theta_{t}\right)
$$

and $T_{t}^{-1}$ is the observed information or, more precisely, the expected observed-data information.

From (2.5) and (2.6), the $p$ value associated with $\theta=\theta_{0}$ based on the observed data, $X_{\text {obs }}$, is

$$
P_{\mathrm{obs}}=\operatorname{Pr}\left[\chi_{k}^{2} / k>D_{\mathrm{obs}}\right],
$$

where

$$
D_{\mathrm{obs}}=\left(\hat{\theta}_{\mathrm{obs}}-\theta_{0}\right)^{t} T^{-1}\left(\hat{\theta}_{\mathrm{obs}}-\theta_{0}\right) / k .
$$

This procedure leading to $P_{\text {obs }}$, although ideal in the sense that it is optimal in large samples, is often difficult to implement in practice, especially in the context of large pub-lic-use data bases. This fact is documented in many of the references mentioned in Section 1.

The comparison of (2.1) and (2.5) shows that the increase in variance due to missing data is

$$
B_{t}=T_{t}-U_{t}
$$

and that the missing information is $U_{t}^{-1}-T_{t}^{-1}$. Thus the canonical ratios of missing to observed information are given by the eigenvalues of $\left(U_{t}^{-1}-T_{t}^{-1}\right) T_{t}$ or, from (2.9) and simple matrix algebra, by the eigenvalues of $B_{t}$ relative to $U_{t}$, which we label $\left(\lambda_{1}, \ldots, \lambda_{k}\right) \in[0, \infty)^{k}$. Since complete information is observed information plus missing information, the canonical ratios of complete to observed information are given by the $\xi_{i}=\left(1+\lambda_{i}\right), i=1, \ldots, k$.

### 2.3 Multiple Imputation and the Completed Data Statistics

Suppose that the missing data, $X_{\text {mis }}$, are multiply imputed with $X{ }_{*_{\text {mis }}}^{(l)}, l=1, \ldots, m$, where the resulting $m$ completed data sets can be represented as

$$
\left\{X_{*}^{(l)} ; l=1, \ldots, m\right\}=\left\{\left(X_{\mathrm{obs}}, X_{*_{\mathrm{mis}}}^{(l)}\right) ; l=1, \ldots, m\right\}
$$

and the resulting complete-data statistics $\hat{\theta}$ and $U$ calculated on the $X_{*}^{(l)}$ are written as $\hat{\theta}_{*_{1}}, \ldots, \hat{\theta}_{*_{1}}$ and $U_{*_{1}}, \ldots, U_{*_{m}}$. Assuming that the multiple imputations are proper, as defined and illustrated in Rubin (1987, chap. 4), and that the samples are large, it follows that for $l=1, \ldots, m$,

$$
\left(\hat{\theta}_{* l} \mid \theta=\theta_{t}, X_{\mathrm{obs}}\right) \sim \operatorname{iid} N\left(\hat{\theta}_{\mathrm{obs}}, B_{t}\right),
$$

and

$$
\left(U_{* l} \mid \theta=\theta_{t}, X_{\mathrm{obs}}\right) \approx U_{t} .
$$

The theoretically most straightforward way to create proper multiple imputations is to draw $X_{\text {mis }}$ from its posterior predictive distribution under an appropriate Bayesian model specification, but other imputation methods can also be proper. Work justifying (2.10) and (2.11) for broad classes of imputation methods can be found in Rubin (1987, chap. 4), Raghunathan (1987), and Schenker and Welsh (1988)in order of decreasing generality and increasing mathematical rigor.

Our objective is to combine the statistics $\left\{\hat{\theta}_{*_{l}}, U_{*_{l}}, l=\right. 1, \ldots, m\}$ to obtain a valid inference for $\theta$, in particular, a $p$ value for $\theta=\theta_{0}$. An obvious result from (2.10)-(2.11) is that

$$
\left(\bar{\theta}_{m} \mid \theta=\theta_{t}, X_{\mathrm{obs}}\right) \sim N\left(\hat{\theta}_{\mathrm{obs}}, B_{t} / m\right),
$$

and independently,
$\left(B_{t}^{-1 / 2} B_{m} B_{t}^{-1 / 2} \mid \theta=\theta_{t}, X_{\text {obs }}\right)$
$\sim$ Wishart with $k$ components and $m-1 \mathrm{df}$,
where the between-imputation component, $\boldsymbol{B}_{m}$, is defined in Equation (1.6).

### 2.4 The Test Statistic $D_{m}$

If $B_{t}$ and $T_{t}=B_{t}+U_{t}$ were known, an efficient procedure would be based on the fact that from (2.5), (2.6), and (2.12)

$$
\left(\bar{\theta}_{m} \mid \theta=\theta_{t}\right) \sim N\left(\theta_{t}, U_{t}+\left(1+m^{-1}\right) B_{t}\right) .
$$

By (2.11), $\bar{U}_{m}$, defined in (1.4), essentially equals $U_{t}$, but $B_{t}$ must be estimated from $\left\{\hat{\theta}_{* l}, U_{* l}, l=1, \ldots, m\right\}$. From (2.13), a conditionally unbiased estimate of $B_{t}$ is $B_{m}$, which, although an efficient estimate of $B_{t}$ with large $m$ and no restrictions on $B_{t}$, with smaller $m$ and larger $k$ can nevertheless be a relatively poor estimate. In fact, procedures based on substituting $B_{m}$ for $B_{t}$ have been studied in Li (1985), Rubin (1987), and Raghunathan (1987), are usually inferior to procedures based on the assumption that $B_{t} \propto U_{t}$, corresponding to equal ratios of missing to observed information. When all ratios of missing to observed information are equal (all $\lambda_{i}=\bar{\lambda}$ ), $B_{t}=\bar{\lambda} U_{t}$, and then if $\bar{\lambda}$ were known, the $p$ value for $\theta=\theta_{0}$ would be based on the test statistic

$$
\begin{aligned}
& \left(\bar{\theta}_{m}-\theta_{0}\right)^{t}\left[U_{t}+\bar{\lambda}\left(1+m^{-1}\right) U_{t}\right]^{-1}\left(\bar{\theta}_{m}-\theta_{0}\right) / k \\
& \quad=\left(\bar{\theta}_{m}-\theta_{0}\right)^{t} U_{t}^{-1}\left(\bar{\theta}_{m}-\theta_{0}\right) /\left[k\left(1+\bar{\lambda}\left(1+m^{-1}\right)\right)\right]
\end{aligned}
$$

Thus a natural choice for a test statistic, at least assuming that $B_{t} \propto U_{t}$, is (2.15) with $\bar{\lambda}$ replaced by an efficient estimate obtained from $\left\{\hat{\theta}_{* l}, U_{* l} ; l=1, \ldots, m\right\}$, specifically, $D_{m}$ defined by Equation (1.2), where $r_{m}$ [defined in (1.5)] is, from (2.11) and (2.13), an unbiased and efficient estimate of $\left(1+m^{-1}\right) \bar{\lambda}$ under the assumption that all $\lambda_{i}=\bar{\lambda}$ [see, for example, Johnson and Kotz (1973)].

### 2.5 The Sampling Distribution of $D_{m}$

The sampling distribution of $D_{m}$ can be easily derived after first observing that from (2.11) $\bar{U}_{m}$ can be replaced by $U_{t}$, and second observing that from the affine invariance of $D_{m}$ we can set, with no loss of generality, $\theta_{0}=0, U_{t}=I$, and $B_{t}=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{k}\right)$. Then, from (1.2) and (1.5),

$$
D_{m}=\frac{\sum_{i=1}^{k} \bar{\theta}_{m, i}^{2} / k}{1+r_{m}}
$$

and

$$
r_{m}=\left(1+m^{-1}\right) \sum_{i=1}^{k} \sum_{l=1}^{m}\left(\hat{\theta}_{* l}-\bar{\theta}_{m}\right)_{i}^{2} / k(m-1),
$$

where the subscript $i$ indexes the $i$ th components of $\bar{\theta}_{m}$ and ( $\hat{\theta}_{*_{l}}-\bar{\theta}_{m}$ ). From (2.12) and (2.13), the numerator and denominator of $D_{m}$ are independently distributed with

$$
\bar{\theta}_{m, i} \mid \theta=\theta_{t} \stackrel{\text { md }}{\sim} N\left(\theta_{t, i}, 1+\left(1+m^{-1}\right) \lambda_{i}\right),
$$

$$
i=1, \ldots, k
$$

and

$$
\sum_{l=1}^{m}\left(\hat{\theta}_{* l}-\bar{\theta}_{m}\right)_{i}^{2} \mid \theta=\theta_{t} \stackrel{\mathrm{md}}{\sim} \lambda_{i} \chi_{m-1}^{2}, \quad i=1, \ldots, k,
$$

where (2.18) holds also conditionally given both $\theta=\theta_{t}$ and $X_{\mathrm{obs}}$. When $\theta=\theta_{0}$ (i.e., when all $\theta_{t, i}=0$ in canonical form) and all ratios of missing to observed information are equal (i.e., when all $\lambda_{i}=\bar{\lambda}$ ), then (2.16)-(2.18) imply that the distribution of $D_{m}$ can be represented as

$$
D_{m} \sim \frac{\chi_{k}^{2} / k}{\left(1+a \chi_{t}^{2} / t\right) /(1+a)},
$$

where $t=k(m-1)$ and $a=\left(1+m^{-1}\right) \bar{\lambda}$, and where $\chi_{k}^{2}$
and $\chi_{t}^{2}$ are independent $\chi^{2}$ random variables on $k$ and $t \mathrm{df}$, respectively.

### 2.6 Approximating the Sampling Distribution of $D_{m}$ When $\theta=\theta_{0}$ and the Fractions of Missing Information Are Equal

Li (1985), Rubin (1987), and Raghunathan (1987) all arrive at the test statistic $D_{m}$ and its distribution given by (2.16)(2.19), but none of their approximations to (2.19) result in fully satisfactory levels, especially for larger $k$ and $\bar{\lambda}$. We approximate distribution (2.19) by a multiple of an $F$ random variable, $\delta F_{k, w}$, where $\delta$ and $w$ are obtained by matching the first two central moments of $D_{m}$, approximated by expanding (2.19) in $1 / \chi_{t}^{2}$ around its expectation, $1 /(t-$ 2 ). This process gives

$$
\delta=(1-2 / w)[1+a t /(t-2)] /(1+a)
$$

and

$$
w=4+(t-4)\left[1+\left(1-2 t^{-1}\right) / a\right]^{2},
$$

provided that $t$ is greater than 4 . Note that, for modest values of $a, \delta$ is close to 1 . Fixing $\delta=1$ and substituting the estimate $r_{m}$ for $a$ in $w$ leads to our procedure given by (1.7)(1.8). When $k=2$ and $m=3$, we obtain $t=4$, which implies that the second moment of the approximating sampling distribution of $D_{m}$ does not exist. Hence, in that case, $\delta$ and $w$ defined by (2.20) and (2.21) cannot be calculated, and so we use the degrees of freedom given by (1.9).

## 3. BEHAVIOR OF $D_{m}$ WHEN $m$ IS LARGE

### 3.1 General Results

As $m \rightarrow \infty$, our suggested reference distribution, as well as those proposed earlier, equal $F_{k, \infty}=\chi_{k}^{2} / k$. Even though the case of $m \rightarrow \infty$ may appear to be of no direct practical interest, it turns out to be of practical importance as a baseline for comparing results with finite $m$ and for suggesting the relevant functions of the $\lambda_{i}$ that govern the performance of procedures based on $D_{m}$. Also, theoretically, the consistency of general test procedures is desirable, suggesting that we hope $D_{\infty}$ is close to $D_{\text {obs }}$. For notational simplicity, we continue to use the canonical form with $\theta_{0}=0, U_{t}= I, B_{t}=\operatorname{diag}\left(\lambda_{i}\right)$, and $T_{t}=\operatorname{diag}\left(\xi_{i}\right)$, where $\xi_{i}=1+\lambda_{i}$. As $m \rightarrow \infty$ and given $\theta=\theta_{t}$ and $X_{\text {obs }}$, from the strong law of large numbers, (2.10) implies that $\bar{\theta}_{m, i} \rightarrow \hat{\theta}_{\text {obs }, i}$, and thus (2.16) and (2.18) imply that

$$
D_{m} \rightarrow D_{\infty}=\frac{1}{k} \sum_{i=1}^{k} \hat{\theta}_{\mathrm{obs}, i}^{2} / \bar{\xi}
$$

In addition, from (2.6) and (2.8), using this canonical notation,

$$
D_{\mathrm{obs}}=\frac{1}{k} \sum_{i=1}^{k} \hat{\theta}_{\mathrm{obs}, i}^{2} / \xi_{i} .
$$

When all $\xi_{i}=\bar{\xi}, D_{\infty}=D_{\text {obs }}$. Consequently, with equal ratios of complete to observed information, our procedure with large $m$ essentially equals the ideal procedure. When the $\xi_{i}$
vary, $D_{\infty}$ and $D_{\text {obs }}$ can be compared by noting that from (2.17)

$$
\left(\hat{\theta}_{\mathrm{obs}, i}^{2} \mid \theta=\theta_{t}\right) \stackrel{\mathrm{md}}{\sim} N\left(\theta_{t, i}, \xi_{i}\right)^{2}, \quad i=1, \ldots, k,
$$

where $N\left(\theta_{t, i}, \xi_{i}\right)^{2}$ is the square of a normal deviate with mean $\theta_{t, i}$ and variance $\xi_{i}$.

### 3.2 Level of $D_{\infty}$ With Unequal Ratios of Complete to Observed Information

Under the null hypothesis that $\theta_{t, i}=0$ for all $i$, from (3.1)-(3.3) both $D_{\infty}$ and $D_{\text {obs }}$ have expectation 1 ,

$$
E\left(D_{\infty} \mid \theta_{t}=\theta_{0}\right)=E\left(D_{\text {obs }} \mid \theta_{t}=\theta_{0}\right)=1,
$$

but $D_{\infty}$ has larger variance,

$$
V\left(D_{\infty} \mid \theta_{t}=\theta_{0}\right)=V\left(D_{\text {obs }} \mid \theta_{t}=\theta_{0}\right)\left(1+C_{\xi}^{2}\right),
$$

where $\dot{C}_{\xi}$ is the coefficient of variation of the $\xi_{i}$,

$$
1+C_{\xi}^{2}=\frac{1}{k} \sum\left(\xi_{i} / \bar{\xi}\right)^{2}
$$

Expression (3.4) suggests that $D_{\infty}$ will be too liberal when the fractions of information vary, essentially as a monotone function of the coefficient of variation of the ratio of complete to observed information. The correlation between $D_{\infty}$ and $D_{\text {obs }}$ under the null hypothesis is also governed solely by $C_{\xi}^{2}$ :

$$
\operatorname{corr}\left(D_{\infty}, D_{\text {obs }} \mid \theta_{t}=\theta_{0}\right)=\left(1+C_{\xi}^{2}\right)^{-1 / 2} .
$$

These results in (3.4) and (3.6) support the conclusion that $D_{\infty}$ and $D_{\text {obs }}$ should behave similarly whenever the $\xi_{i}$ vary only modestly, that is, when $C_{\xi}^{2}$ is modest relative to 1 . Previous work has indexed the performance of $D_{m}$ by the variance in the fractions of missing information, $\gamma_{i}=1- \xi_{i}^{-1}$, which leads to less crisp conclusions than are given here.

The actual level of a nominal level- $\alpha$ test based on $D_{\infty}$ referenced to a $\chi_{k}^{2} / k$ distribution is, from (3.1) and (3.3),

$$
\operatorname{Pr}\left[\sum \frac{\xi_{i}}{\bar{\xi}} \chi_{1, i}^{2}>\chi_{k}^{2}(\alpha)\right],
$$

where $\chi_{1, i}^{2}$ are independent $\chi^{2}$ random variables on 1 df and $\chi_{k}^{2}(\alpha)$ is the $\alpha$ percent point of the $\chi_{k}^{2}$ distribution. Table 3 gives exact levels of $D_{\infty}$ corresponding to the conditions in Tables 1 and 2, obtained using a modification of the method of Imhof (1961) to evaluate (3.7). For all conditions with $C_{\xi} \leq 20 \%$ and most conditions with $C_{\xi}=40 \%$,
nominal level $\leq$ actual level of $D_{\infty} \leq 1.1 \times$ nominal level, so that even when the fractions of missing information vary, $D_{\infty}$ referenced to $\chi_{k}^{2} / k$ very nearly has the correct level. In Tables 1-3, for each combination of $k, \bar{\xi}$, and $C_{\xi}$, the $k$ values of $\xi_{i}$ were selected to have mean $\bar{\xi}$ and coefficient of variation $C_{\xi}$ by drawing $k$ values of $\lambda_{i}=\xi_{i}-1$ from a gamma distribution.

Our conclusion is that for all practical purposes $D_{\infty}$ is asymptotically calibrated-it has exactly the correct largesample level with equal fractions of missing information
and essentially the correct large-sample level unless the fractions vary substantially.

### 3.3 Power Loss of $D_{\infty}$ With Unequal Fractions of Missing Information

Under the alternative hypothesis, $\theta=\theta_{t}$, let $a_{i}=\theta_{t, i}^{2} / \xi_{i}$; it is then easy to show from (3.1) and (3.2) that

$$
\begin{gathered}
E\left(D_{\infty} \mid \theta=\theta_{t}\right)=1+\frac{1}{k} \sum a_{i}\left(\xi_{i} / \bar{\xi}\right), \\
E\left(D_{\mathrm{obs}} \mid \theta=\theta_{t}\right)=1+\frac{1}{k} \sum a_{i},
\end{gathered}
$$

$$
\begin{gathered}
\operatorname{var}\left(D_{\infty} \mid \theta=\theta_{t}\right)=\frac{2}{k}\left[1+C_{\xi}^{2}+\frac{2}{k} \sum a_{i}\left(\xi_{i} / \bar{\xi}\right)^{2}\right], \\
\operatorname{var}\left(D_{\text {obs }} \mid \theta=\theta_{t}\right)=\frac{2}{k}\left[1+\frac{2}{k} \sum a_{i}\right],
\end{gathered}
$$

and

$$
\operatorname{cov}\left(D_{\infty}, D_{\mathrm{obs}} \mid \theta=\theta_{t}\right)=\frac{2}{k}\left[1+\frac{2}{k} \sum a_{i}\left(\xi_{i} / \bar{\xi}\right)\right] .
$$

From these expressions it is clear that the power loss is related not only to the variability of the $\xi_{i}$ but also to the relationship between the $\xi_{i}$ and the $a_{i}=\theta_{t, i}^{2} / \xi_{i}$. Generally, the impression is that for many cases $D_{\infty}$ and $D_{\text {obs }}$ have similar first and second moments. To explore this situation further, we obtained some numerical results, which were quite encouraging. Again, the modified results of Imhof (1961) were used to evaluate the probabilities of rejection as a function of the values of $k, \bar{\xi}, C_{\xi}, \alpha$ used in Tables 13 , and now $\theta_{t} \neq \theta_{0}$. For our evaluations, the values of $k$ dimensional $\theta_{t}$ were indexed by the scalar

$$
\Delta=\sum_{i=1}^{k} \theta_{t, i}^{2} / k
$$

the average squared distance between the null and alternative values. For each alternative indexed by $\Delta$, we randomly selected a value $\theta_{t}$ on the surface of the $k$-dimensional hypersphere with center $\theta_{0}$ and radius $\Delta^{1 / 2}$. Although there is some loss of generality in this method of setting alternatives, it allows us to investigate easily a wide range of alternatives with varying $k$. We chose $\Delta=.25, .50, .75$, and 1.75, and calculated relative power losses for each case of Table 3. Relative power loss is defined as

$$
\left(P_{\infty}^{t}-P_{\mathrm{obs}}^{t}\right) / P_{\mathrm{obs}}^{t},
$$

where $P_{\text {obs }}^{t}=$ probability of rejection using the ideal procedure based on $D_{\text {obs }}$, and $P_{\infty}^{t}=$ probability of rejection using $D_{\infty}$ when $\theta=\theta_{t}$.

Across the conditions with $C_{\xi} \leq 20 \%$, the maximum relative loss of power was $6 \%$, with a typical relative loss of power between $2 \%$ and $3 \%$; the relative power losses were greatest when $\alpha=1 \%, C_{\xi}=20 \%, \bar{\xi}=2$, and $k=35$. When $C_{\xi}=40 \%$, the maximum relative loss of power was $12 \%$, with a typical relative loss of power between $3 \%$ and $5 \%$. The relative power losses were greatest when $\alpha=1 \%$,

Table 3. Exact Levels for $D_{\infty}$ [from (3.7)] With Unequal Fractions of Missing Information as a Function of Nominal Level, $\alpha$; Number of Components Being Tested, $k$; the Average Ratio of Complete to Observed Information, $\xi$; and the Coefficient of Variation of the Ratios, $C_{\xi}$
|  | $\bar{\xi}$ | $\alpha=1 \%$ |  |  | $\alpha=5 \%$ |  |  | $\alpha=10 \%$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 1.1 | 1.5 | 2.0 | 1.1 | 1.5 | 2.0 | 1.1 | 1.5 | 2.0 |
| $C_{\xi}=10 \%$ |  |  |  |  |  |  |  |  |  |  |
| $k$ | 2 | 1.0 | 1.1 | 1.1 | 5.1 | 5.1 | 5.1 | 10.0 | 10.0 | 10.0 |
|  | 5 | 1.0 | 1.0 | 1.1 | 5.0 | 5.0 | 5.1 | 10.0 | 10.0 | 10.1 |
|  | 10 | 1.0 | 1.0 | 1.0 | 5.0 | 5.1 | 5.0 | 10.0 | 10.1 | 10.1 |
|  | 20 | 1.0 | 1.0 | 1.0 | 5.0 | 5.1 | 5.1 | 10.1 | 10.1 | 10.1 |
|  | 35 | 1.0 | 1.0 | 1.0 | 5.0 | 5.0 | 5.0 | 10.1 | 10.1 | 10.1 |
| $C_{\xi}=20 \%$ |  |  |  |  |  |  |  |  |  |  |
| $\boldsymbol{k}$ | 2 | 1.1 | 1.1 | 1.1 | 5.1 | 5.1 | 5.1 | 10.0 | 10.0 | 10.1 |
|  | 5 | 1.0 | 1.0 | 1.1 | 5.1 | 5.0 | 5.1 | 10.1 | 10.1 | 10.1 |
|  | 10 | 1.0 | 1.0 | 1.1 | 5.0 | 5.1 | 5.2 | 10.1 | 10.2 | 10.2 |
|  | 20 | 1.0 | 1.0 | 1.0 | 5.0 | 5.1 | 5.2 | 10.1 | 10.2 | 10.2 |
|  | 35 | 1.0 | 1.0 | 1.1 | 5.0 | 5.2 | 5.2 | 10.2 | 10.2 | 10.2 |
| $C_{\xi}=40 \%$ |  |  |  |  |  |  |  |  |  |  |
| $k$ | 2 | 1.2 | 1.2 | 1.3 | 5.3 | 5.4 | 5.5 | 10.2 | 10.3 | 11.0 |
|  | 5 | 1.2 | 1.2 | 1.3 | 5.3 | 5.4 | 5.5 | 10.2 | 10.3 | 10.9 |
|  | 10 | 1.0 | 1.1 | 1.3 | 5.3 | 5.4 | 5.6 | 10.0 | 10.3 | 10.5 |
|  | 20 | 1.0 | 1.1 | 1.2 | 5.2 | 5.2 | 5.2 | 10.0 | 10.1 | 10.2 |
|  | 35 | 1.0 | 1.1 | 1.2 | 5.2 | 5.1 | 5.1 | 10.0 | 10.1 | 10.2 |


NOTE: When $C_{\xi}=0 \%$, exact level $\equiv$ nominal level.
$C_{\xi}=40 \%, \bar{\xi}=2$, and $k=35$. Of course, some fraction of the rejections are due to the slightly liberal level of $D_{\infty}$, especially with $C_{\xi}=40 \%$, so the conclusions on power loss are somewhat optimistic, especially in cases with large $C_{\xi}$. Nevertheless, the overall conclusion is that the power curve of $D_{\infty}$ is quite similar to that of the ideal statistic $D_{\text {obs }}$ for practical values of $C_{\xi}$.

## 4. MONTE CARLO RESULTS WITH FINITE $m$

### 4.1 Comparison of Levels

The exact sampling distribution of $D_{m}$, even with large samples and under the null hypothesis, is analytically unpleasant, and, therefore, we retreat from analytical comparisons and instead use simulation techniques. The basic setup uses the distribution of $D_{m}$ defined by (2.16)-(2.18) with the $F_{k, w}$ reference distribution given by (1.7)-(1.8). The simulation was done for $N=10,000$ repetitions for the conditions of Tables $1-3$ with $m=3,4,5,10$.

Thus, our simulation experiment can be described as a $3^{3} \times 5 \times 4$ factorial experiment with the following: Three levels of the nominal level, $\alpha$; three levels of the average complete to observed information, $\bar{\xi}$; three levels of variation among components of $\theta$ in the complete to observed information, $C_{\xi}$; five levels of dimensionality, $k$; and four levels of $m$, the number of imputations. From the results presented in Table 2 for $m=3$ and Table 3 for $m=\infty$, we expect our procedure to have nearly the correct level for all cases under study. In fact, the results of our simulation can be accurately summarized by linearly interpolating in $[k(m-1)-2]^{-1}$ between the corresponding values in the tables. The residual sum of squares when using this interpolation is only $4.1 \%$ of the total sum of squares across all Monte Carlo conditions (and only $3.2 \%$ for those cases with $C_{\xi} \leq 20 \%$ ). Also, the largest residual is only $.12 \%$
(and $.08 \%$ when $C_{\xi} \leq 20 \%$ ). Consequently, Tables 2 and 3 can be used to summarize accurately results for all values of $m$.

### 4.2 Power Comparison of Procedures $D_{m}$ and $D_{\infty}$

We focus on $5 \%$ nominal tests and $C_{\xi} \leq 20 \%$ for investigating the relative power of the procedures $D_{m}$ and $D_{\infty}$. We restrict attention to these cases for two reasons-first, to limit the number of expensive simulations, and second, to focus on cases where the level of $D_{m}$ is essentially correct so that the rejection rates really reflect power. As in Section 3.3, we generated $\theta_{t}$ values to obtain powers under alternative distributions. The power of the nominal $\alpha$-level test based on $D_{m}$ is given by

$$
P_{m}^{t}=\operatorname{Pr}\left(D_{m}>F_{k, w}(\alpha) \mid \theta=\theta_{t}\right),
$$

where $F_{k, w}(\alpha)$ is the upper $\alpha$ percentile of an $F$ distribution with $k$ and $w \mathrm{df}$. To measure the loss of power due to finite $m$, we use

$$
\left(P_{m}^{t}-P_{\infty}^{t}\right) / P_{\infty}^{t},
$$

the relative loss of power due to the use of a finite number of multiple imputations.

The total sum of squares is 4.6393 with 719 df , with the average relative power loss of $10 \%$. This suggests relatively small losses in power in general. The major power losses are when $m=3$ and $k$ is large ( $\geq 15$ ) and $C_{\xi}$ and $\bar{\xi}$ are large. The typical loss of power is $12 \%$ but can be as large as $40 \%$ for extreme cases. Most of the total variation can be explained by the factors $\Delta, k, m, \bar{\xi}$, and $k * m$. These five factors explain roughly $70 \%$ of the total variability.

Further investigation of the interactions suggests that the loss of power when $m \geq 4$ and $\bar{\xi} \leq 1.5$ and $C_{\xi} \leq 20 \%$ is modest-the maximum loss across these situations is only

Table 4. Large-Sample Power (in \%) of $D_{m}$ With $F_{k, w}$ Reference Distribution as a Function of $\Delta, \bar{\xi}, C_{\xi}$, and $k$, With $m=\infty(m=4)$
|  | $\boldsymbol{k}$ | $\Delta=.25$ |  | $\Delta=.50$ |  | $\Delta=.75$ |  | $\Delta=1.75$ |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $C_{\xi}=0 \%$ |  |  |  |  |  |  |  |  |  |
| $\bar{\xi}=1.2$ | 2 | 7.9 | (6.7) | 11.8 | (10.0) | 19.1 | (15.8) | 31.3 | (26.6) |
|  | 5 | 9.8 | (9.6) | 16.8 | (15.7) | 29.9 | (28.3) | 52.5 | (49.3) |
|  | 10 | 12.4 | (11.9) | 22.2 | (21.0) | 44.8 | (42.2) | 76.2 | (71.5) |
|  | 20 | 16.0 | (15.2) | 32.3 | (30.5) | 66.3 | (63.5) | 93.2 | (91.7) |
|  | 35 | 20.8 | (20.1) | 46.0 | (43.4) | 85.5 | (82.9) | 99.2 | (99.0) |
| $\bar{\xi}=1.5$ | 2 | 7.7 | (5.6) | 10.1 | (6.9) | 16.3 | (10.9) | 25.4 | (18.4) |
|  | 5 | 9.1 | (8.0) | 13.7 | (11.5) | 24.9 | (20.8) | 41.5 | (35.7) |
|  | 10 | 11.2 | (10.3) | 17.9 | (15.6) | 36.3 | (32.0) | 62.2 | (55.3) |
|  | 20 | 13.6 | (12.3) | 25.9 | (22.4) | 54.5 | (48.0) | 85.3 | (79.2) |
|  | 35 | 17.7 | (15.4) | 36.0 | (31.2) | 72.5 | (67.3) | 96.8 | (93.9) |
| $\bar{\xi}=2.0$ | 2 | 6.8 | (4.8) | 9.1 | (5.8) | 13.1 | (8.1) | 20.3 | (12.2) |
|  | 5 | 8.0 | (7.0) | 11.4 | (9.8) | 19.2 | (15.4) | 31.9 | (24.9) |
|  | 10 | 9.1 | (8.4) | 14.9 | (12.5) | 27.6 | (22.2) | 48.5 | (38.2) |
|  | 20 | 11.2 | (9.9) | 19.7 | (16.2) | 40.3 | (32.7) | 71.1 | (59.3) |
|  | 35 | 14.3 | (12.1) | 26.6 | (21.1) | 56.4 | (46.1) | 88.5 | (78.8) |
| $C_{\xi}=10 \%$ |  |  |  |  |  |  |  |  |  |
| $\bar{\xi}=1.2$ | 2 | 8.4 | (7.3) | 11.5 | (9.9) | 19.3 | (15.9) | 31.3 | (26.6) |
|  | 5 | 9.9 | (9.2) | 16.5 | (15.2) | 30.5 | (27.6) | 51.8 | (48.5) |
|  | 10 | 12.4 | (11.5) | 22.0 | (20.7) | 45.1 | (41.7) | 74.5 | (70.1) |
|  | 20 | 15.8 | (15.4) | 32.9 | (31.4) | 66.8 | (63.1) | 93.4 | (91.5) |
|  | 35 | 21.2 | (20.4) | 45.8 | (43.6) | 85.5 | (82.2) | 99.4 | (98.8) |
| $\bar{\xi}=1.5$ | 2 | 7.7 | (5.5) | 10.4 | (7.3) | 16.0 | (11.4) | 25.4 | (17.5) |
|  | 5 | 9.1 | (8.4) | 13.3 | (11.7) | 24.9 | (21.3) | 41.5 | (35.2) |
|  | 10 | 11.0 | (10.0) | 17.9 | (16.1) | 36.3 | (31.7) | 62.6 | (55.9) |
|  | 20 | 14.1 | (12.6) | 26.0 | (22.4) | 55.4 | (48.3) | 85.4 | (79.0) |
|  | 35 | 18.0 | (15.9) | 36.7 | (32.0) | 74.1 | (67.2) | 96.6 | (93.7) |
| $\bar{\xi}=2.0$ | 2 | 5.5 | (4.6) | 5.7 | (4.7) | 6.4 | (5.4) | 7.7 | (5.6) |
|  | 5 | 5.3 | (5.1) | 6.3 | (5.8) | 7.5 | (6.1) | 8.9 | (7.3) |
|  | 10 | 5.7 | (5.7) | 6.4 | (6.3) | 8.3 | (7.5) | 10.9 | (8.4) |
|  | 20 | 5.6 | (5.5) | 7.0 | (6.8) | 9.5 | (8.2) | 19.5 | (9.8) |
|  | 35 | 5.8 | (5.4) | 7.4 | (7.0) | 11.2 | (9.1) | 17.8 | (13.4) |
|  |  |  |  | $C_{\xi}=20 \%$ |  |  |  |  |  |
| $\bar{\xi}=1.2$ | 2 | 8.2 | (6.9) | 11.8 | (10.0) | 19.3 | (16.0) | 30.1 | (25.4) |
|  | 5 | 10.4 | (10.0) | 16.0 | (14.5) | 29.2 | (26.6) | 50.3 | (45.0) |
|  | 10 | 12.1 | (11.7) | 20.9 | (19.8) | 43.9 | (39.1) | 72.6 | (66.6) |
|  | 20 | 16.1 | (15.3) | 31.4 | (28.4) | 65.8 | (59.4) | 92.3 | (86.0) |
|  | 35 | 20.5 | (19.6) | 43.5 | (38.9) | 83.9 | (77.4) | 98.9 | (97.7) |
| $\bar{\xi}=1.5$ | 2 | 7.5 | (5.5) | 11.3 | (8.1) | 16.1 | (11.3) | 25.7 | (17.9) |
|  | 5 | 8.6 | (8.1) | 14.1 | (12.6) | 26.6 | (20.4) | 41.9 | (34.1) |
|  | 10 | 10.3 | (9.8) | 18.4 | (16.5) | 36.5 | (30.7) | 62.7 | (53.1) |
|  | 20 | 13.4 | (12.3) | 26.6 | (22.5) | 55.2 | (46.6) | 85.5 | (76.9) |
|  | 35 | 17.1 | (15.4) | 37.1 | (30.9) | 74.2 | (64.3) | 96.8 | (92.7) |
| $\bar{\xi}=2.0$ | 2 | 6.4 | (4.7) | 9.1 | (6.4) | 13.4 | (8.3) | 21.2 | (12.6) |
|  | 5 | 8.1 | (7.1) | 11.9 | (10.3) | 19.0 | (14.7) | 32.5 | (24.4) |
|  | 10 | 9.3 | (9.0) | 15.0 | (12.8) | 26.9 | (21.4) | 48.3 | (36.9) |
|  | 20 | 11.1 | (10.4) | 20.0 | (16.4) | 40.8 | (32.2) | 70.9 | (56.6) |
|  | 35 | 13.8 | (12.5) | 26.8 | (21.3) | 57.7 | (44.4) | 88.9 | (76.5) |


$17 \%$. Hence, in the cases of most practical importance, using $m=4$ should lead to only a slight loss of power. Table 4 provides the powers of $D_{\infty}$ and $D_{m}$ with $m=4$ as a function of $\bar{\xi}, C_{\xi}$, and $k$ for alternatives indexed by $\Delta$. Twodimensional linear interpolation in $(t-2)^{-1}$ and $\Delta^{-1}$ between the power using $D_{\infty}$ and $D_{m}$ with $m=4$ provides accurate predictions; the residual sum of squares is $6.4 \%$ of the total sum of squares across all Monte Carlo conditions, with a largest residual of only $2.9 \%$.

### 4.4 Conclusions From Simulations

The results of the simulation indicate that our procedure based on $D_{m}$ is well calibrated and there is no substantial loss of power except in relatively extreme circumstances. Further, with $m=4$ imputations, our procedure is comparable to the ideal one $D_{\text {obs }}$ in terms of level and power even in relatively extreme circumstances. Summary advice is that if fractions of missing information are likely to be
modest (for example, $\leq 20 \%$ ) or even moderately large (for example, $30 \%$ ), $m=3$ imputations should be adequate. Even when half the information is missing, $m=4$ or 5 imputations results in well-calibrated procedures with relatively modest power losses except when the variation in the fractions of missing information is extreme.

## 5. CONCLUSIONS

We have described a procedure for computing significance levels from multiply imputed data using the statistic $D_{m}$ and an $F_{k, w}$ reference distribution, which requires a point estimate and its variance-covariance matrix in each completed data set. All of our results are for large samples. Single imputation, even well done, can be a total disaster. For example, with $30 \%$ missing information, a 25 -component parameter, and a nominal 5\% test, the actual level is more than $76 \%$.

We first show that for $m \rightarrow \infty, D_{m}$ is essentially the same, with respect to both power and level, as the ideal procedure, the likelihood ratio test based directly on the observed data. Only for very large and variable fractions of missing information are there discernable differences.

Then, using simulation techniques, we show that with $m =3,4,5$, and 10 , the level of our procedure is very close to the nominal level in almost all cases of practical interest, and that the power losses are usually modest (approximately $10 \%$ ) unless fractions of missing information are large and variable, and even then, the power losses are not disastrous, even for $m=3$. The method of this article works well with $m=2$ when $k$ is large, but neither ours nor the one in Rubin (1987, chap. 3) works especially well when $m=2, k$ is small, and fractions of missing information are large and variable [see Rubin (1987, chap. 4) for results on level].
[Received March 1989. Revised February 1991.]

## REFERENCES

Glynn, R., Laird, N., and Rubin, D. B. (1986), "Selection Modelling Versus Mixture Modelling With Nonignorable Nonresponse," in Drawing Inferences from Self-Selected Samples, ed. H. Wainer, New York: Springer-Verlag, pp. 119-146.

- (1991), "The Performance of Mixture Models for Nonignorable Nonresponse With Follow Ups," Technical Report, Harvard University, Dept. of Statistics.

Heitjan, D. F., and Rubin, D. B. (1986), "Inference From Coarse Data Using Multiple Imputation," in Proceedings of the 18th Symposium on the Interface of Computer Science and Statistics, ed. T. Boardman, Washington, DC: American Statistical Association, pp. 138-143.
Herzog, T. N., and Rubin, D. B. (1983), "Using Multiple Imputations to Handle Nonresponse in Sample Surveys," in Incomplete Data in Sample Surveys, Volume 2, Theory and Bibliographies, eds. W. G. Madow, I. Olkin, and D. B. Rubin, New York: Academic Press, pp. 209-245.
Imhof, J. P. (1961), "Computing the Distribution of Quadratic Forms in Normal Variables," Biometrika, 48, 419-426.
Johnson, N. L., and Kotz, S. (1973), Continuous Univariate Distribu-tions-2, New York: John Wiley.
Li, K. H. (1985), "Hypothesis Testing in Multiple Imputation-With Emphasis on Mixed-up Frequencies in Contingency Tables," unpublished Ph.D. thesis, University of Chicago, Dept. of Statistics.
Li, K. H., Meng, X. L., Raghunathan, T. E., and Rubin, D. B. (1991), "Significance Levels From Repeated $p$-Values With Multiply-Imputed Data," Statistica Sinia, 1, pp. 65-92.
Little, R. J. A., and Rubin, D. B. (1987), Statistical Analysis With Missing Data, New York: John Wiley.
Meng, X. L., and Rubin, D. B. (in press), "Performing Likelihood-Ratio Tests with Multiply-Imputated Data Sets," Biometrika.
Raghunathan, T. E. (1987), "Large Sample Significance Levels from Multiply-Imputed Data," unpublished Ph.D. thesis, Harvard University, Dept. of Statistics.
Rubin, D. B. (1978), "Multiple Imputations in Sample Surveys-A Phenomenological Bayesian Approach to Nonresponse," in Proceedings of the Survey Research Methods Section, American Statistical Association, pp. 20-34. Also in Imputation and Editing of Faulty or Missing Survey Data, U.S. Dept. of Commerce, Bureau of the Census, pp. 1-23.
(1980), "Illustrating the Use of Multiple Imputations to Handle Nonresponse in Sample Surveys," in 42nd Session of the International Statistical Institute, 1979, Book 2, pp. 517-532.

- (1987), Multiple Imputation for Nonresponse in Surveys, New York: John Wiley.
Rubin, D. B., and Schenker, N. (1986), "Multiple Imputation for Interval Estimation From Simple Random Samples With Ignorable Nonresponse," Journal of the American Statistical Association, 81, pp. 366374.
(1987), "Interval Estimation From Multiply-Imputed Data: A Case Study Using Census Agriculture Industry Codes," Journal of Official Statistics, 3, pp. 375-387.
Schenker, N. (1985), "Multiple Imputation for Interval Estimation From Surveys With Ignorable Nonresponse," unpublished Ph.D. dissertation, University of Chicago, Dept. of Statistics.
Schenker, N., and Welsh, A. H. (1988), "Asymptotic Results From Multiple Imputation," The Annals of Statistics, 16, pp. 1550-1566.
Schenker, N., Treiman, D. J., and Weidman, L. (1988), "Evaluation of Multiply-Imputed Public-Use Tapes," in Proceedings of the Survey Research Methods Section, American Statistical Association, pp. 85-92.
Treiman, D. J., Bielby, W., and Cheng, M. (1988), "Evaluating a Mul-tiple-Imputation Method for Recalibrating 1970 Census Detailed Industry Codes to the 1980 Standard," Sociological Methodology, 18, pp. 309-345.
Weld, L. H. (1987), "Significance Levels From Public-Use Data With Multiply-Imputed Industry Codes," unpublished Ph.D. dissertation, Harvard University, Dept. of Statistics.


[^0]:    * K. H. Li is Lecturer, Department of Statistics, Chinese University of Hong Kong, Shatin, Hong Kong. T. E. Raghunathan is Assistant Professor, Department of Biostatistics, University of Washington, Seattle, WA 98195. D. B. Rubin is Professor and Chairman, Department of Statistics, Harvard University, Cambridge, MA 02138. This work was supported in part by National Science Foundation Grants SES-83-11428 and SES-88-05433 and in part by Joint Statistical Agreements with the United States Census Bureau JSA-86-8, JSA-87-7, JSA-88-3, JSA-89-08, and JSA-90-23.

[^1]:    © 1991 American Statistical Association
    Journal of the American Statistical Association December 1991, Vol. 86, No. 416, Theory and Methods

[^2]:    NOTE: Based on 10,000 independent Monte Carlo draws for each combination of $k, \bar{\xi}$, and $C_{\xi}$.

