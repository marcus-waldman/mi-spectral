---
citekey: vonhippelNewConfidenceIntervals2016
item_type: article
authors: 'von Hippel, Paul T.'
year: 2016
title: 'New {Confidence Intervals} and {Bias Comparisons Show That Maximum Likelihood Can Beat Multiple Imputation} in {Small Samples}'
venue: Structural equation modeling
publisher: Routledge
volume: 23
issue: 3
pages: 422--437
doi: 10.1080/10705511.2015.1047931
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\vonhippelNewConfidenceIntervals2016.pdf'
pdf_sha256: 305588d477478e001ac1e45eb265658a45177a10628eec1903c0c25c55140d40
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-07-02T21:18:02Z
---
# New Confidence Intervals and Bias Comparisons Show That Maximum Likelihood Can Beat Multiple Imputation in Small Samples 

Paul T. von Hippel

To cite this article: Paul T. von Hippel (2016) New Confidence Intervals and Bias Comparisons Show That Maximum Likelihood Can Beat Multiple Imputation in Small Samples, Structural Equation Modeling: A Multidisciplinary Journal, 23:3, 422-437, DOI: 10.1080/10705511.2015.1047931

To link to this article: https://doi.org/10.1080/10705511.2015.1047931

View supplementary material

Published online: 12 Oct 2015.

Submit your article to this journal

Article views: 1068

View related articles

View Crossmark data

Citing articles: 22 View citing articles

# New Confidence Intervals and Bias Comparisons Show That Maximum Likelihood Can Beat Multiple Imputation in Small Samples 

Paul T. von Hippel<br>University of Texas


#### Abstract

When analyzing incomplete data, is it better to use multiple imputation (MI) or full information maximum likelihood (ML)? In large samples ML is clearly better, but in small samples ML's usefulness has been limited because ML commonly uses normal test statistics and confidence intervals that require large samples. We propose small-sample $t$-based ML confidence intervals that have good coverage and are shorter than $t$-based confidence intervals under MI. We also show that ML point estimates are less biased and more efficient than MI point estimates in small samples of bivariate normal data. With our new confidence intervals, ML should be preferred over MI, even in small samples, whenever both options are available.


Keywords: confidence intervals, finite samples, maximum likelihood, multiple imputation, small samples

Multiple imputation (MI) and full information maximum likelihood (ML) are increasingly popular methods for analyzing data with missing values (Allison, 2002; Little \& Rubin, 2002). MI fills in each missing value with a random sample of plausible imputations, whereas ML integrates the missing values out of the likelihood. The increasing popularity of MI and ML is due in part to their increasing availability in software. For example, the structural equation modeling (SEM) software LISREL, Mplus, AMOS, and SAS PROC CALIS can all use either MI or ML.

When both ML and MI are available, which is better? If the sample is large, the answer is clear: It is better to use ML. One reason for this is that ML is more efficient. In large samples, MI would need an infinite number of imputations to achieve the efficiency of ML (Wang \& Robins, 1998). If the number of imputations is small ( $3-10$ ), as it typically is, MI is just slightly less efficient than ML at producing point estimates (Rubin, 1987), but MI is much less efficient at estimating standard errors, confidence intervals, or the fraction of missing information (Graham, Olchowski, \& Gilreath, 2007). If the fraction of missing information is

[^0]large, standard errors estimated by MI can require 200 to 300 imputed data sets to approach the efficiency of standard errors estimated by ML (Bodner, 2008; Graham et al., 2007). It can be impractical to use so many imputations if the sample is large, or if the analysis runs slowly on each imputed data set.

With large samples, then, ML is better than MI. But what about small samples? One could get the impression that small samples turn the table and give the advantage to MI. Under MI it is common to report hypothesis tests and confidence intervals using a $t$ statistic with degrees of freedom that decrease with the sample size $n$ (Barnard \& Rubin, 1999, developed the most popular choice; for alternatives, see Wagstaff \& Harel, 2011). By contrast, ML confidence intervals commonly rely on asymptotic normality and so require a large sample. Small-sample $t$ intervals have also been proposed for ML, but they are rarely used because they only work for two specific estimands: the mean and the mean difference (Little, 1976, 1988; Morrison, 1973).

This article proposes a more general degrees of freedom formula for $t$ intervals under ML with missing data. We propose two very similar formulas; the more general is

$$
\hat{v}_{M L}=v_{c o m}\left(1-\hat{\gamma}_{M L}\right)\left(\frac{v_{c o m}+1}{v_{c o m}+3}\right) .
$$

Here $\hat{\gamma}_{M L}$ is an estimate of the fraction of missing information $\gamma$. The estimate $\hat{\gamma}_{M L}$ is calculated directly from the incomplete data using ML, and is more precise than the estimate of $\gamma$ that is commonly used under MI (Savalei \& Rhemtulla, 2012). $v_{c o m}$ is the degrees of freedom that would apply if the data were complete-for example, $v_{\text {com }}=n-2$ for a simple regression. (Note that $v_{\text {com }}$ is the error degrees of freedom, which depends on the sample size; it should not be confused with the SEM degrees of freedom, which depends on the number of distinct elements in the covariance matrix.)

The formula for $\hat{v}_{M L}$ makes ML a viable approach even in small samples. In simulations using bivariate normal data, we will show that small-sample $t$ intervals using $\hat{v}_{M L}$ under ML have good coverage and are shorter and more reliable than the small-sample $t$ intervals that are commonly used in MI. We also show that, under both ML and MI, the degrees of freedom estimators perform better if they are constrained to take values no smaller than 3 .

In addition to the new confidence intervals, our simulations also evaluate the point estimates produced by ML and MI in small samples of incomplete normal data. We find that MI point estimates are less efficient than ML point estimates in small samples, just as they are in large samples. The reason for MI's lower efficiency is simple: Random variation in the imputed values contributes excess variation to the MI estimates.

We also confirm that, although both ML and MI can produce biased point estimates, the biases are larger under MI than they are under ML. Some of these biases have been noticed in previous research, but previous results are scattered and no one has pulled them together to tell a coherent story. We offer an intuitive explanation, as well as a closed-form expression for the bias, which shows when it will be smaller or larger. The pattern of bias is fairly simple. Under MI, the variance of the imputed variable is overestimated (cf. Demirtas, Freels, \& Yucel, 2008, Table 2; Yuan, Yang-Wallentin, \& Bentler, 2012, Table 2). When the imputed variable is used as a regressor, the estimated regression slope is attenuated (cf. Hoogendoorn, 2009). When the imputed variable is used as a regressand, the regression slope is unbiased but the residual variance is overestimated (cf. Chen \& Ibrahim, 2013; Kim, 2004). The bias in the residual variance can be eliminated by a change to the Bayesian prior (Kim, 2004; von Hippel, 2013a), but eliminating the other biases is not so easy. Under ML, the biases are similar but considerably smaller.

Overall, with our new confidence intervals, ML estimates can be at least as good as MI in small samples as well as large. As ML is also easier to use than MI, we conclude that ML should be preferred whenever both options are available. However, it is not always the case that both options are available. There are situations when ML is unavailable and MI should be used. We discuss some of those situations in the conclusion.

## INCOMPLETE BIVARIATE NORMAL DATA

In this section we introduce the incomplete bivariate normal data that is used in later calculations and simulations. Data are drawn from an infinite population consisting of standard bivariate normal variables ( $X, Y$ ) with mean and covariance matrix

$$
\begin{aligned}
& \mu_{X Y}=\left[\begin{array}{l}
\mu_{X} \\
\mu_{Y}
\end{array}\right]=\left[\begin{array}{l}
0 \\
0
\end{array}\right] \\
& \Sigma_{X Y}=\left[\begin{array}{cc}
\sigma_{X}^{2} & \\
\sigma_{X Y} & \sigma_{Y}^{2}
\end{array}\right]=\left[\begin{array}{cc}
1 & \\
\rho & 1
\end{array}\right] .
\end{aligned}
$$

Notice that the regression of $Y$ on $X$ has the same parameter values as the regression of $X$ on $Y$. That is, in the following regression equations,

$$
\begin{aligned}
& Y=\alpha_{Y . X}+\beta_{Y . X} X+e_{Y . X}, \text { where } e_{Y . X} \sim N\left(0, \sigma_{Y . X}^{2}\right) \\
& X=\alpha_{X . Y}+\beta_{X . Y} Y+e_{X . Y}, \text { where } e_{X . Y} \sim N\left(0, \sigma_{X . Y}^{2}\right)
\end{aligned}
$$

the parameter values are $\alpha_{Y . X}=\alpha_{X . Y}=0, \beta_{Y . X}=\beta_{X . Y}=\rho$, and $\sigma_{Y . X}^{2}=\sigma_{X . Y}^{2}=1-\rho^{2}$.

We define a dummy variable $M$ to indicate whether the value of $Y$ is missing ( $M=1$ ) or observed ( $M=0$ ). Notice that the mean of $M$ is also the proportion $p$ of $Y$ values that are missing. If the variable $M$ is independent of the variables $X$ and $Y$, then values are said to be missing completely at random (MCAR). If $M$ depends on $X$ but not on $Y$ (net of $X$ ), then values are said to be missing at random (MAR) (Heitjan \& Basu, 1996). There are many ways for values to be MAR. Our simulations focus on the MAR pattern where $Y$ values are missing if $X$ is negative (MXN)-that is, $M=1$ iff $\mathrm{X}<0$. MXN is a simple but challenging MAR pattern that limits statistical information and yields estimates with large bias in small samples. After we develop an understanding of where the bias comes from, it will be easy to anticipate the bias that would result from other MAR patterns.

It will be helpful to know the conditional moments of ( $X, Y$ ) given $M$. Let $\mu_{X Y .0}$ and $\Sigma_{X Y .0}$ be the moments when $M=0$; likewise let $\mu_{X Y .1}$ and $\Sigma_{X Y .1}$ be the moments when $M=1$. If $Y$ values are MCAR, then the conditional moments of ( $X, Y$ ) given $M$ are the same as the unconditional moments-that is, $\mu_{X Y .0}=\mu_{X Y .1}=\mu_{X Y}$ and $\Sigma_{X Y .0}=\Sigma_{X Y .1}=\Sigma_{X Y}$. But if $Y$ values are MXN then the conditional moments of ( $X, Y$ ) given $M$ are the moments of a standard bivariate normal distribution where one variable has been truncated at zero. Those moments are (Rose \& Smith, 2002, p. 226)

$$
\begin{aligned}
& \mu_{X Y .1}=-\mu_{X Y .0}=\sqrt{\frac{2}{\pi}}\left[\begin{array}{l}
1 \\
\rho
\end{array}\right] \\
& \Sigma_{X Y .1}=\Sigma_{X Y .0}=\frac{1}{\pi}\left[\begin{array}{cc}
\pi-2 & \\
(\pi-2) \rho & \pi-2 \rho^{2}
\end{array}\right] .
\end{aligned}
$$

It will also be helpful to know the unconditional moments of $X, Y, M$, and the interaction $X M$. It is straightforward to calculate those moments using the algebra of expectations:

$$
\begin{aligned}
& \mu_{X Y M X M}=E\left[\begin{array}{c}
X \\
Y \\
M \\
X M
\end{array}\right]=\left[\begin{array}{c}
0 \\
0 \\
p \\
p \mu_{X .1}
\end{array}\right] \\
& \Sigma_{X Y M X M}=V\left[\begin{array}{c}
X \\
Y \\
M \\
X M
\end{array}\right] \\
& =\left[\begin{array}{ccc}
1 & 1 & p(1-p) \\
\rho & p \mu_{X .1} \rho & p\left(\sigma_{X .1}^{2}+\mu_{X .1}^{2}(1-p)\right)
\end{array}\right] .
\end{aligned}
$$

In interpreting $\Sigma_{X Y M X M}$, notice that if $Y$ values are MCAR then $M$ is uncorrelated with $X$ because $\mu_{X .1}=0$. On the other hand, if $Y$ values are MXN then $M$ is correlated with $X$.

To illustrate the properties of different estimators, we held $p$ and $\rho$ constant at $1 / 2$, we let $Y$ values be MCAR or MXN, and we simulated samples each containing $n$ cases from the population described above. Of these n cases, $n_{0}$ cases were complete, with $M=0$ and $Y$ observed, and $n_{1}=n-n_{0}$ cases were incomplete, with $M=1$ and $Y$ missing. For purposes of some of the formulas that follow, we suppose that the data are sorted so that the complete cases come first; that is, the observed $Y_{i}$ values are in cases $i=1, \ldots, n_{0}$ and the missing $Y_{i}$ values are in cases $i=n_{0}+1, \ldots, n$.

It remains only to choose values for the sample size n . Although there are old rules of thumb suggesting that structural equation models invariably require 100 to 250 cases, more recent and empirically grounded work shows that the number of cases required depends on the model and data (Hogarty, Hines, Kromrey, Ferron, \& Mumford, 2005; MacCallum, Widaman, Zhang, \& Hong, 1999; Muthén \& Muthén, 2002). In regression analysis, smaller samples can be adequate if the residual variance is small and the collinearity among regressors is low (Kelley \& Maxwell, 2003). In factor analysis, smaller samples can be adequate if the model is simple and the communalities are high (Hogarty et al., 2005; MacCallum et al., 1999). A recent simulation found that, depending on the characteristics of the model and data, the number of cases required to meet certain criteria for power, bias, and solution propriety could be as low as $n=30$ or as high as $n=460$ (Wolf, Harrington, Clark, \& Miller, 2013).

To explore the low end of these recommendations, we let $n$ take values of 25 or 100 . A sample size of $n=25$ is consistent with past studies on the small-sample properties of missing-data estimators, which have most commonly examined sample sizes down to $n=25$ (Lipsitz, Parzen, \& Zhao, 2002; Wagstaff \& Harel, 2011), although two studies went as low as $n=10$ (Barnard \& Rubin, 1999; von Hippel, 2013a)
and two did not go below $n=40$ (Demirtas et al., 2008; Reiter, 2007). Samples of this size are of practical interest in applied settings where the intended model is simple and it is expensive, impractical, or impossible to gather a large sample. For example, in political science, regressions that compare U.S. states cannot have a sample size greater than $n=50$ (Granberg-Rademacker, 2007), and regressions that compare different countries might have $n$ as small as 41 or 46 (Cohen, 2004; Kunovich \& Paxton, 2003). The problems of finite populations is an issue in political research, as there are only 50 states in the United States and 196 countries in the world. But the use of small samples is not limited to fields with small populations. Pilot clinical trials can use as few as $n=20$ patients (Barnes, Lindborg, \& Seaman, 2006), and the median number of subjects in psychology experiments is just $n=18$ (Marszalek, Barber, Kohlhart, \& Holmes, 2011).

To accurately evaluate the properties of the estimators, our research design had many replications for each simulated condition. For conditions with $n=100$, we replicated the simulation 40,000 times; for conditions with $n=25$, we replicated the simulation 160,000 times. The large number of replications ensures that the means and standard deviations of the point estimates, as estimated from the simulation, are usually accurate to two significant digits. To evaluate confidence intervals, we used only 8,000 replications because the calculations were iterative and ran more slowly. With 8,000 replications the mean length of confidence intervals were usually accurate to one decimal place, and the estimated coverage of confidence intervals was accurate to within a standard error of $0.25 \%$.

## MAXIMUM LIKELIHOOD

ML estimation often requires iterative numerical maximization of the likelihood. In bivariate normal data with values MAR, however, ML estimates can be obtained as closed form expressions (Anderson, 1957), which permit us to calculate the biases in closed form as well. Because $X$ is complete, ML estimates for the moments of $X$ are obtained using the usual complete-data ML formulas:

$$
\begin{aligned}
& \hat{\mu}_{X, M L}=\frac{1}{n} \sum_{i=1}^{n} X_{i} \\
& \hat{\sigma}_{X, M L}^{2}=\frac{1}{n} \sum_{i=1}^{n}\left(X_{i}-\hat{\mu}_{X, M L}\right)^{2} .
\end{aligned}
$$

ML estimates for the regression of $Y$ on $X$ can be obtained simply by ignoring the incomplete cases and applying ordinary least squares (OLS) to the $n_{0}$ cases with $Y$ observed (Anderson, 1957; Little, 1992; von Hippel, 2007). The ML slope $\hat{\beta}_{Y . X, M L}$ and intercept $\hat{\alpha}_{Y . X, M L}$ are calculated by the
usual OLS formulas, and the ML residual variance $\hat{\sigma}_{Y . X, M L}^{2}$ is calculated by averaging the squared residuals:

$$
\hat{\sigma}_{Y . X, M L}^{2}=\frac{1}{n} \sum_{i=1}^{n}\left(Y_{i}-\hat{\alpha}_{Y . X, M L}-\hat{\beta}_{Y . X, M L} X_{i}\right)^{2} .
$$

However, ML estimates for other parameters cannot be obtained by ignoring the incomplete cases. Instead, because ML estimates are functionally invariant, ML estimates for other parameters can be obtained by transforming the ML estimates that we have already obtained. For example, the following formulas give ML estimates for the mean and variance of $Y$ and for the covariance of $Y$ with $X$ :

$$
\begin{aligned}
& \hat{\mu}_{Y, M L}=\hat{\alpha}_{Y . X, M L}+\hat{\beta}_{Y . X, M L} \hat{\mu}_{X, M L} \\
& \hat{\sigma}_{X Y, M L}=\hat{\beta}_{Y . X, M L} \hat{\sigma}_{X, M L}^{2} \\
& \hat{\sigma}_{Y, M L}^{2}=\hat{\beta}_{Y . X, M L}^{2} \hat{\sigma}_{X, M L}^{2}+\hat{\sigma}_{Y . X, M L}^{2}
\end{aligned}
$$

(Anderson, 1957). Likewise, the following formulas define ML estimates for the regression of $X$ on $Y$ :

$$
\begin{aligned}
& \hat{\beta}_{X . Y, M L}=\hat{\sigma}_{X Y, M L} / \hat{\sigma}_{Y, M L}^{2} \\
& \hat{\alpha}_{X . Y, M L}=\hat{\mu}_{X, M L}-\hat{\beta}_{X . Y, M L} \hat{\mu}_{Y, M L} \\
& \hat{\sigma}_{X . Y, M L}^{2}=\hat{\sigma}_{X, M L}^{2}-\hat{\beta}_{X . Y, M L}^{2} \hat{\sigma}_{Y, M L}^{2}
\end{aligned}
$$

These estimates follow from the fact that the same formulas define relationships among the parameters.

## Bias

The middle rows of Table 1 give the approximate expectations and standard errors of the ML estimates, calculated by taking the mean and standard deviation of the estimates obtained in our simulation. The estimates $\hat{\mu}_{M L}, \hat{\alpha}_{Y . X, M L}, \hat{\beta}_{Y . X, M L}$ are unbiased, whereas the other estimates have at least slight biases. The biases are worst when the sample is small ( $n=25$ ) and when values are MXN.

The negative biases in the variances $\hat{\sigma}_{X, M L}^{2}$ and $\hat{\sigma}_{Y . X, M L}^{2}$ are familiar, and result from the estimates using formulas that divide by $n$ and $n_{0}$ instead of $n-1$ and $n_{0}-2$. The covariance $\hat{\sigma}_{X, M L}^{2}$ also has a negative bias that it inherits from $\hat{\sigma}_{X, M L}^{2}$ through the formula $\hat{\sigma}_{X Y, M L}=\hat{\beta}_{Y, X, M L} \hat{\sigma}_{X, M L}^{2}$.

Less familiar is the positive bias in $\hat{\sigma}_{Y, M L}^{2}$ that occurs when values are MXN. This has been observed in simulations (Yuan et al., 2012; Table 2), but it has never been explained. To understand the positive bias in $\hat{\sigma}_{Y, M L}^{2}$, consider the definition $\hat{\sigma}_{Y, M L}^{2}=\hat{\beta}_{Y . X, M L}^{2} \hat{\sigma}_{X, M L}^{2}+\hat{\sigma}_{Y . X, M L}^{2}$ and notice that the square $\hat{\beta}_{Y . X, M L}^{2}$ is positively biased, even though $\hat{\beta}_{Y . X, M L}$ itself is unbiased. A simple expression for the bias in $\hat{\beta}_{Y . X, M L}^{2}$ is

$$
\operatorname{Bias}\left(\hat{\beta}_{Y . X, M L}^{2}\right)=E\left(\hat{\beta}_{Y . X, M L}^{2}\right)-\beta_{Y . X}^{2}=V\left(\hat{\beta}_{Y . X, M L}\right),
$$

which follows immediately from the identity $V\left(\hat{\beta}_{Y . X, M L}\right)= E\left(\hat{\beta}_{Y . X, M L}^{2}\right)-\left[E\left(\hat{\beta}_{Y . X, M L}\right)\right]^{2}$. When values are MXN, the positive bias in $\hat{\beta}_{Y . X, M L}^{2}$ outweighs the negative biases in $\hat{\sigma}_{X, M L}^{2}$ and $\hat{\sigma}_{Y, X, M L}^{2}$, so that the net bias in $\hat{\sigma}_{Y, M L}^{2}$ is positive, and large when the sample is small.

Why is the bias in $\hat{\beta}_{Y . X, M L}^{2}$ larger with a small sample size or an MXN pattern? It is because the bias is equal to $V\left(\hat{\beta}_{Y . X, M L}\right)$, which is larger when we reduce the sample size or restrict the range of observed $X$ values that are used in the regression of $Y$ on $X$. The MXN pattern is one way to restrict the range of $X$.

More explicitly, the asymptotic covariance matrix of the regression estimates is

$$
\Sigma_{\hat{\alpha} \hat{\beta}_{Y . X, M L}}=V\binom{\hat{\alpha}_{Y . X, M L}}{\hat{\beta}_{Y . X, M L}}=\frac{\sigma_{Y . X}^{2}}{n_{0}}\left[\begin{array}{cc}
1+\mu_{X .0}^{2} / \sigma_{X .0}^{2} & \\
-\mu_{X .0} / \sigma_{X .0}^{2} & 1 / \sigma_{X .0}^{2}
\end{array}\right]
$$

(Little \& Rubin, 2002), which is larger when values are MXN as the MXN condition implies that $\sigma_{X .0}^{2}$ is small and $\mu_{X .0}^{2}$ is large. More generally, $\operatorname{Bias}\left(\hat{\beta}_{Y . X, M L}^{2}\right)=V\left(\hat{\beta}_{Y . X, M L}\right)$ will be larger under any MAR pattern that yields a small $\sigma_{X .0}^{2}$, whereas the MCAR pattern causes relatively little bias because $\sigma_{X .0}^{2}=\sigma_{X}^{2}$.

We can now understand the potential for bias in the regression of $X$ on $Y$. When $n=25$ and values are MXN, the slope $\hat{\beta}_{X, Y, M L}=\hat{\sigma}_{X Y, M L} / \hat{\sigma}_{Y, M L}^{2}$ has a negative bias as its numerator has a negative bias and its denominator has a positive bias. The bias of the intercept is opposite to that of the slope; this follows from the definition of the intercept as $\hat{\alpha}_{X . Y, M L}=\hat{\mu}_{Y, M L}-\hat{\beta}_{X . Y, M L} \hat{\mu}_{X, M L}$. The residual variance $\hat{\sigma}_{X . Y, M L}^{2}=\hat{\sigma}_{X, M L}^{2}-\hat{\beta}_{X . Y, M L}^{2} \hat{\sigma}_{Y, M L}^{2}$ has a negative bias that comes partly from negative bias in $\hat{\sigma}_{X, M L}^{2}$, but mostly from positive bias in $\hat{\beta}_{X, Y, M L}^{2}$. An argument like that in Equation 10 shows that Bias $\left(\hat{\beta}_{X, Y, M L}^{2}\right)=V\left(\hat{\beta}_{X, Y, M L}\right)$.

## MAXIMUM LIKELIHOOD MULTIPLE IMPUTATION

Values can be imputed conditionally on the ML estimates (Wang \& Robins, 1998), a practice that we call maximum likelihood multiple imputation (MLMI). MLMI is not the most common type of MI, but its simplicity will ease our calculations and serve as a bridge to the more common type of MI.

It is helpful to start with a simplified situation where values are imputed just once-a process that we call maximum

TABLE 1
Expectations and (Standard Errors) of Estimators
| Estimator | $n$ | Pattern | Estimands |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | Regression of $Y$ on $X$ |  |  | Moments of $Y$ |  |  | Regression of $X$ on $Y$ |  |  |
|  |  |  | $\alpha_{Y . X}$ | $\beta_{Y . X}$ | $\sigma_{Y . X}^{2}$ | $\mu_{Y}$ | $\sigma_{Y}^{2}$ | $\sigma_{X Y}$ | $\alpha_{X . Y}$ | $\beta_{X . Y}$ | $\sigma_{X . Y}^{2}$ |
| ML | 25 | MXN | . 00 | . 50 | . 62 | . 00 | 1.09 | . 48 | . 10 | . 41 | . 63 |
|  |  |  | (.46) | (.51) | (.28) | (.50) | (.78) | (.48) | (.26) | (.39) | (.29) |
|  |  | MCAR |  |  |  |  |  |  |  |  | . 65 (.25) |
|  |  |  | . 00 (.27) | . 50 (.29) | . 62 (.28) | . 00 (.28) | . 94 (.41) | . 48 (.30) | . 00 (.22) | . 52 (.29) |  |
|  | 100 | MXN |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.21) | . 50 (.21) | . 72 (.15) | . 00 (.22) | 1.01 (.27) | . 50 (.22) | . 02 (.12) | . 48 (.16) | . 73 (.17) |
|  |  | MCAR |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.12) | . 50 (.13) | . 72 (.15) | . 00 (.13) | . 98 (.20) | . 50 (.14) | . 00 (.10) | . 51 (.12) | . 73 (.13) |
| MLMI | 25 | MXN |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.46) | . 50 (.51) | . 65 (.30) | . 00 (.51) | 1.12 (.81) | . 50 (.50) | . 11 (.26) | . 42 (.40) | . 67 (.31) |
|  |  | MCAR |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.27) | . 50 (.30) | . 65 (.30) | . 00 (.28) | . 96 (.44) | . 50 (.32) | . 00 (.22) | . 53 (.30) | . 70 (.27) |
|  | 100 | MXN |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.21) | . 50 (.21) | . 73 (.15) | . 00 (.22) | 1.02 (.27) | . 50 (.22) | . 02 (.12) | . 48 (.16) | . 74 (.17) |
|  |  | MCAR |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.13) | . 50 (.13) | . 73 (.15) | . 00 (.14) | 99 (.20) | . 50 (.15) | . 00 (.10) | . 51 (.12) | . 74 (.13) |
| PDMI | 25 | MXN |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.51) | . 50 (.56) | . 87 (.84) | . 00 (.56) | 1.58 (1.82) | . 50 (.55) | . 17 (.22) | . 32 (.33) | . 67 (.28) |
|  |  | MCAR |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.29) | . 50 (.32) | . 88 (2.68) | . 00 (.30) | 1.24 (2.98) | . 50 (.34) | . 00 (.21) | . 45 (.27) | . 73 (.26) |
|  | 100 | MXN |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.23) | . 50 (.23) | . 77 (.17) | . 00 (.23) | 1.09 (.30) | . 50 (.24) | . 04 (.12) | . 44 (.16) | . 74 (.17) |
|  |  | MCAR |  |  |  |  |  |  |  |  |  |
|  |  |  | . 00 (.13) | . 50 (.13) | . 77 (.17) | . 00 (.14) | 1.03 (.22) | . 50 (.15) | . 00 (.10) | . 49 (.12) | . 75 (.13) |
| Parameter values |  |  | 0 | . 5 | . 75 | 0 | 1 | . 5 | 0 | . 5 | . 75 |


Note. $\mathrm{ML}=$ maximum likelihood; $\mathrm{MXN}=$ data missing at random pattern where $Y$ values are missing if $X$ is negative; MCAR $=$ data missing completely at random; MLMI $=$ maximum likelihood multiple imputation; PDMI $=$ posterior draw multiple imputation. The PDMI estimates use $\nu_{\text {prior }}=0$.
likelihood single imputation (MLSI). In MLSI, we fill in missing $Y$ values by regression on $X$, where the coefficients of the regression model are ML estimates:

$$
Y_{M L S I, i}=\hat{\alpha}_{Y . X, M L}+\hat{\beta}_{Y . X, M L} X_{i}+e_{M L S I, i}, i=n_{1}+1, \ldots, n
$$

where $e_{M L S I, i} \sim N\left(0, \hat{\sigma}_{Y . X, M L}^{2}\right)$.

The result is a partly observed, partly imputed variable $Y_{\text {obsMLSI }}$ consisting of $n_{0}$ observed values $Y_{\text {obs }}$ drawn from Eqaution 3 and $n_{1}$ imputed values $Y_{\text {MLSI }}$ drawn from Equation 12. MLSI estimates of means, variances, covariances, and regressions are obtained by applying the usual complete-data formulas to the partly imputed data. ${ }^{1}$

In MLMI, the process of imputation and estimation is repeated $D$ times with each repetition yielding a new MLSI estimate-for example, $\hat{\mu}_{\text {MLSI }, d}, d=1, \ldots D$. The MLSI

[^1]estimates are averaged to yield MLMI estimates-for example, $\hat{\mu}_{\text {MLMI }}=D^{-1} \sum_{d=1}^{D} \hat{\mu}_{\text {MLSI, } d}$.

Because averaging does not affect the expectation of an estimator, the bias of the MLMI estimators is the same as the bias of the MLSI estimators. When discussing bias, we focus on the MLSI estimates, which makes the mathematics a little simpler.

## Bias

The middle rows of Table 1 give the expectations and standard errors of the MLMI estimates, as calculated from our simulation with $D=5$ imputations. The standard errors of the MLMI estimates are slightly larger than those of the ML estimates-a result that accords with large-sample theory (Wang \& Robins, 1998).

The biases of the MLMI estimates are also similar to those of the ML estimates, although slightly larger. In particular, when values are MXN, $\hat{\sigma}_{Y, M L S I}^{2}$ has a positive bias that is large when $n=25$. The positive bias in $\hat{\sigma}_{Y, M L S I}^{2}$ is responsible for the negative bias in $\hat{\beta}_{X . Y, M L S I}=\hat{\sigma}_{X Y, M L S I} / \hat{\sigma}_{X, M L S I}^{2}$, which in turn is responsible for the positive bias in $\hat{\alpha}_{X . Y, M L S I}=$

TABLE 2
Expectations (and Standard Errors) of Posterior Draw Multiple Imputation Estimators With Different Values of vprior
| $\nu_{\text {prior }}$ | $N$ | Pattern | Estimands |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | Regression of $Y$ on $X$ |  |  | Moments of $Y$ |  |  | Regression of $X$ on $Y$ |  |  |
|  |  |  | $\alpha_{Y . X}$ | $\beta_{Y . X}$ | $\sigma_{Y . X}^{2}$ | $\mu_{Y}$ | $\sigma_{Y}^{2}$ | $\sigma_{X Y}$ | $\alpha_{X . Y}$ | $\beta_{X . Y}$ | $\sigma_{X . Y}^{2}$ |
| -2 | 25 | MXN | . 00 | . 50 | 4.22 | . 00 | 6.10 | . 50 | . 17 | . 29 | . 68 |
|  |  |  | (.68) | (.82) | (678) | (.93) | (731) | (.72) | (.21) | (.30) | (.27) |
|  |  | MCAR | . 00 | . 50 | $205{ }^{\text {a }}$ | . 00 | $198{ }^{\text {a }}$ | . 50 | . 00 | . 41 | . 75 |
|  |  |  | (1.82) | (.64) | $(76,986){ }^{\mathrm{a}}$ | (1.80) | $(73,830)^{\mathrm{a}}$ | (.64) | (.21) | (.25) | (.26) |
|  | 100 | MXN | . 00 | . 50 | . 79 | . 00 | 1.11 | . 50 | . 04 | . 43 | . 74 |
|  |  |  | (.23) | (.23) | (.17) | (.24) | (.31) | (.24) | (.12) | (.16) | (.17) |
|  |  | MCAR | . 00 | . 50 | . 79 | . 00 | 1.05 | . 50 | . 00 | . 48 | . 75 |
|  |  |  | (.13) | (.13) | (.17) | (.14) | (.22) | (.15) | (.10) | (.12) | (.13) |
| 0 | 25 | MXN | . 00 | . 50 | . 87 | . 00 | 1.58 | . 50 | . 17 | . 32 | . 67 |
|  |  |  | (.51) | (.56) | (.84) | (.56) | (1.82) | (.55) | (.22) | (.33) | (.28) |
|  |  | MCAR | . 00 | . 50 | . 88 | . 00 | 1.24 | . 50 | . 00 | . 45 | . 73 |
|  |  |  | (.29) | (.32) | (2.68) | (.30) | (2.98) | (.34) | (.21) | (.27) | (.26) |
|  | 100 | MXN | . 00 | . 50 | . 77 | . 00 | 1.09 | . 50 | . 04 | . 44 | . 74 |
|  |  |  | (.23) | (.23) | (.17) | (.23) | (.30) | (.24) | (.12) | (.16) | (.17) |
|  |  | MCAR | . 00 | . 50 | . 77 | . 00 | 1.03 | . 50 | . 00 | . 49 | . 75 |
|  |  |  | (.13) | (.13) | (.17) | (.14) | (.22) | (.15) | (.10) | (.12) | (.13) |
| 2 | 25 | MXN | . 00 | . 50 | . 75 | . 00 | 1.40 | . 50 | . 16 | . 35 | . 66 |
|  |  |  | (.49) | (.55) | (.37) | (.54) | (1.03) | (.54) | (.23) | (.35) | (.28) |
|  |  | MCAR | . 00 | . 50 | . 75 | . 00 | 1.09 | . 50 | . 00 | . 48 | . 71 |
|  |  |  | (.28) | (.31) | (.37) | (.29) | (.54) | (.33) | (.22) | (.29) | (.26) |
|  | 100 | MXN | . 00 | . 50 | . 75 | . 00 | 1.07 | . 50 | . 04 | . 45 | . 74 |
|  |  |  | (.23) | (.23) | (.16) | (.24) | (.30) | (.24) | (.12) | (.17) | (.17) |
|  |  | MCAR | . 00 | . 50 | . 75 | . 00 | 1.02 | . 50 | . 00 | . 50 | . 74 |
|  |  |  | (.13) | (.13) | (.16) | (.14) | (.21) | (.15) | (.10) | (.12) | (.13) |
| 7 | 25 | MXN | . 00 | . 50 | . 61 | . 00 | 1.20 | . 50 | . 16 | . 40 | . 64 |
|  |  |  | (.48) | (.53) | (.29) | (.53) | (.92) | (.53) | (.24) | (.39) | (.29) |
|  |  | MCAR | . 00 | . 50 | . 61 | . 00 | . 94 | . 50 | . 00 | . 54 | . 68 |
|  |  |  | (.28) | (.30) | (.28) | (.29) | (.47) | (.32) | (.22) | (.31) | (.26) |
|  | 100 | MXN | . 00 | . 50 | . 71 | . 00 | 1.03 | . 50 | . 04 | . 47 | . 73 |
|  |  |  | (.22) | (.23) | (.15) | (.23) | (.29) | (.24) | (.12) | (.17) | (.17) |
|  |  | MCAR | . 00 | . 50 | . 71 | . 00 | . 98 | . 50 | . 00 | . 51 | . 74 |
|  |  |  | (.13) | (.13) | (.15) | (.14) | (.21) | (.15) | (.10) | (.12) | (.13) |
| Parameter values |  |  | 0 | . 5 | . 75 | 0 | 1 | . 5 | 0 | . 5 | . 75 |


Note. $\mathrm{MXN}=\mathrm{MXN}=$ data missing at random pattern where $Y$ values are missing if $X$ is negative; MCAR = data missing completely at random.
${ }^{\mathrm{a}}$ With $v_{\text {prior }}=-2$, the expectation or standard error of certain estimates can be undefined. When the true expectation is undefined, the expectation and standard error estimated from the simulation tend to be very large.
$\hat{\mu}_{Y, M L S I}-\hat{\beta}_{Y, X, M L S I} \hat{\mu}_{X, M L S I}$. When values are MCAR, on the other hand, the bias of $\hat{\sigma}_{Y, M L S I}^{2}$ turns slightly negative.

To understand the biases of the MLSI estimates, it is helpful to summarize the distribution of $Y_{\text {obsMLSI }}$ in a single equation. Using the following symbols for the errors of the ML estimates,

$$
\begin{aligned}
\Delta \hat{\alpha}_{Y . X, M L} & =\hat{\alpha}_{Y . X, M L}-\alpha_{Y . X} \\
\Delta \hat{\beta}_{Y . X, M L} & =\hat{\beta}_{Y . X, M L}-\beta_{Y . X} \\
\Delta \hat{\sigma}_{Y . X, M L}^{2} & =\hat{\sigma}_{Y . X, M L}^{2}-\sigma_{Y . X}^{2}
\end{aligned}
$$

we can summarize the distribution of $Y_{\text {obsMLSI }}$ using a single regression equation:
$Y_{\text {obs } M L S I}=\alpha+M \Delta \hat{\alpha}_{Y . X, M L}+\beta X+X M \Delta \hat{\beta}_{Y . X, M L}+e_{\text {obsMLSI }}$,
where $e_{\text {obsMLSI }} \sim N\left(0, \sigma_{Y . X}^{2}+M \Delta \hat{\sigma}_{Y . X, M L}^{2}\right)$.

In the fully observed cases, this reduces to the regression in Equation 3. In the imputed cases, it reduces to the regression in Equation 12.

In Equation 14, the regressors $M$ and $X M$ contribute extra variance to $Y$, and that extra variance increases with the coefficients $\Delta \hat{\alpha}_{Y . X, M L}$ and $\Delta \hat{\beta}_{Y . X, M L}$. So when $\Delta \hat{\alpha}_{Y . X, M L}$ and $\Delta \hat{\beta}_{Y . X, M L}$ are large-that is, when $\hat{\alpha}_{Y . X, M L}$ and $\hat{\beta}_{Y . X, M L}$ contain substantial estimation error-the variance of $Y_{\text {obsMLSI }}$ has positive bias even though the bias of $\hat{\sigma}_{Y . X, M L}^{2}$ is negative.

More explicitly, a calculation in the Appendix shows that the bias of $\hat{\sigma}_{Y, M L S I}^{2}$ is approximately

$$
\operatorname{Bias}\left(\hat{\sigma}_{Y, M L S I}^{2}\right)=\operatorname{tr}\left(\Sigma_{M X M} \Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, M L}}\right)+\operatorname{Bias}\left(\hat{\sigma}_{Y, X, M L}^{2}\right) p
$$

where $\Sigma_{M X M}$ is the covariance matrix of ( $M, X M$ )-that is, the lower right corner of the big matrix in Equation 5and $\Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, M L}}$ is the covariance matrix of the ML regression estimates, from Equation 11.

The first component in the bias is positive, but the second component is negative because $\hat{\sigma}_{Y . X, M L}^{2}$ is a negatively biased estimator of $\sigma_{Y . X}^{2}$. When values are MXN, the first bias component is relatively large so the net bias is positive. When values are MCAR, the first bias component is relatively small so the net bias is negative. These patterns are plainly visible in Table 1.

## POSTERIOR DRAW MULTIPLE IMPUTATION

MLMI is not the most popular form of imputation. Instead, the most popular form of imputation fills in missing values with draws from the posterior predictive distribution. Others simply call this MI (Rubin, 1987), but here we call it posterior draw multiple imputation (PDMI) to distinguish it from MLMI.

Again it is helpful to start with a simplified situation where values are imputed just once-that is, posterior draw single imputation (PDSI). Under PDSI, we fill in missing $Y$ values by regression on $X$, much as we do under MLSI:

$$
\begin{aligned}
& Y_{P D S I, i}=\hat{\alpha}_{Y . X, P D}+\hat{\beta}_{Y . X, P D} X_{i}+e_{P D S I, i}, i=n_{1}+1 \ldots n \\
& \text { where } e_{P D S I, i} \sim N\left(0, \hat{\sigma}_{Y . X, P D}^{2}\right) .
\end{aligned}
$$

Under PDMI, however, the estimates $\hat{\alpha}_{Y . X, P D}$, $\hat{\beta}_{Y . X, P D}, \hat{\sigma}_{Y . X, P D}^{2}$ used in the imputation model are not ML estimates but posterior draw (PD) estimates drawn at random from the posterior distribution of the parameters given the observed data.

The PD estimates are obtained as follows (Little \& Rubin, 1989). First, $\hat{\sigma}_{Y . X, P D}^{2}$ is drawn from an inverse chi-square distribution that is scaled by $\hat{\sigma}_{Y . X, M L}^{2}$,

$$
\hat{\sigma}_{Y . X, P D}^{2}=\hat{\sigma}_{Y . X, M L}^{2} \frac{n_{0}}{U}, \text { where } U \sim \chi_{n_{0}-2+v_{\text {prior }}}^{2} .
$$

Here $\nu_{\text {prior }}$ is the prior degrees of freedom (Kim, 2004), which is set in the imputation software. The most widely available choice in software is $v_{\text {prior }}=0$, which corresponds to the Jeffreys prior.

Next, $\hat{\alpha}_{Y . X, P D}, \hat{\beta}_{Y . X, P D}$ are drawn from a bivariate normal distribution whose covariance matrix is just the ML covariance matrix rescaled using $\hat{\sigma}_{Y . X, P D}^{2}$ :

$$
\left[\begin{array}{c}
\hat{\alpha}_{Y . X, P D} \\
\hat{\beta}_{Y . X, P D}
\end{array}\right] \sim N\left(\left[\begin{array}{c}
\hat{\alpha}_{Y . X, M L} \\
\hat{\beta}_{Y . X, M L}
\end{array}\right], \Sigma_{\hat{\alpha} \hat{\beta}_{Y . X, M L}} \frac{\hat{\sigma}_{Y . X, P D}^{2}}{\hat{\sigma}_{Y . X, M L}^{2}}\right) .
$$

Notice that the PD estimates $\hat{\alpha}_{Y . X, P D}, \hat{\beta}_{Y . X, P D}$, although unbiased, are about twice as variable as the ML estimates $\hat{\alpha}_{Y . X, M L}, \hat{\beta}_{Y . X, M L}$. The PD estimates have all the variability of the ML estimates, plus a similar amount of variability that is added by the posterior draws:

$$
\begin{aligned}
\Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, P D}}= & V\left[\begin{array}{c}
\hat{\alpha}_{Y, X, P D} \\
\hat{\beta}_{Y, X, P D}
\end{array}\right]=\Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, M L}}+\Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, M L}} \frac{\hat{\sigma}_{Y . X, P D}^{2}}{\hat{\sigma}_{Y . X, M L}^{2}} \\
& \approx 2 \Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, M L}} .
\end{aligned}
$$

Like MLSI estimates, PDSI estimates are obtained by applying the usual complete-data formulas to the partly imputed data. PDMI estimates are obtained by averaging PDSI estimates across $D$ imputations. More explicitly, in each iteration $d=1, \ldots D$, we draw new parameter estimates $\hat{\alpha}_{Y . X, P D, d}, \hat{\beta}_{Y . X, P D, d}, \hat{\sigma}_{Y . X, P D, d}^{2}$ from the posterior; we reimpute the missing values; and we calculate new PDSI estimatesfor example, $\hat{\mu}_{\text {PDSI }, d}$-from the imputed data. We then average the PDSI estimates to obtain PDMI estimates-for example, $\hat{\mu}_{\text {PDMI }}=D^{-1} \sum_{d=1}^{D} \hat{\mu}_{\text {PDSI }, d}$.

## Bias

Table 1 gives the expectations and standard errors of the PDMI estimates, as calculated from the simulation with $D=5$ imputations. The standard errors of the PDMI estimates are larger than those of the MLMI estimates-a result that accords with large-sample theory (Wang \& Robins, 1998). The biases of PDMI affect the same parameters as the biases of MLMI, but the biases of PDMI are considerably larger. In discussing the biases, we focus on the PDSI estimates, which have the same biases as the PDMI estimates but are mathematically simpler.

A striking difference between the PDSI and MLSI biases is that under PDSI the bias of $\hat{\sigma}_{Y, P D S I}^{2}$ is positive not just when values are MXN but when values are MCAR as well. The positive bias in $\hat{\sigma}_{Y, \text { PDSI }}^{2}$ is responsible for the negative bias in $\hat{\beta}_{X, Y, P D S I}=\hat{\sigma}_{X Y, P D S I} / \hat{\sigma}_{X, P D S I}^{2}$, which in turn is responsible for the positive bias in $\hat{\alpha}_{X . Y, \text { PDSI }}=\hat{\mu}_{Y, \text { PDSI }}-\hat{\beta}_{Y . X, \text { PDSI }} \hat{\mu}_{X, \text { PDSI }}$.

Using the same approximation that we used for MLSI (see Appendix), we get the following expression for the asymptotic bias of $\hat{\sigma}_{Y, P D S I}^{2}$ :

$$
\operatorname{Bias}\left(\hat{\sigma}_{Y, P D S I}^{2}\right)=\operatorname{tr}\left(\Sigma_{M X M} \Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, P D}}\right)+\operatorname{Bias}\left(\hat{\sigma}_{Y . X, P D}^{2}\right) p .
$$

The first component in the bias is positive, and the second component is also positive because the estimate $\hat{\sigma}_{Y . X, P D}^{2}$ has a bias of

$$
\begin{aligned}
& \operatorname{Bias}\left(\hat{\sigma}_{Y . X, P D}^{2}\right)=E\left(\hat{\sigma}_{Y . X, P D}^{2}\right)-\sigma_{Y . X}^{2} \\
& =\frac{2-v_{\text {prior }}}{\left(n_{0}-2\right)-\left(2-v_{\text {prior }}\right)} \sigma_{Y . X}^{2}
\end{aligned}
$$

which is positive under the usual choice $v_{\text {prior }}=0$ (Kim, 2004; von Hippel, 2013a).

Because both components of $\operatorname{Bias}\left(\hat{\sigma}_{Y, \text { PDSI }}^{2}\right)$ are positive, the net bias in $\hat{\sigma}_{Y, P D I}^{2}$ is positive even when values are MCAR. In addition, the first bias component is about twice as large under PDSI as it is under MLSI, because $\Sigma_{\hat{\alpha} \hat{\beta}_{Y, Y, P D}} \approx 2 \Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, M L}}$. That is why the biases of PDSI are worse than they are under MLSI: The variation in the posterior draws inadvertently adds to the variation in $Y$.

## Root Mean Squared Error

Table 3 evaluates the bias-variance trade-off by comparing the estimators with respect to root mean squared errors (RMSEs). For each sample size and pattern, it gives the RMSE of each estimator and ranks the estimators from 1 (smallest RMSE) to 6 (largest RMSE).

Across all the estimands, the smallest RMSEs are typically achieved by the ML estimates, followed by the MLMI estimates and then the PDMI estimates with $v_{\text {prior }}=7$. Exceptions to this pattern can occur when an estimate is biased toward zero. Biasing an estimate toward zero can sometimes produce a favorable bias-variance trade-off, although such a trade-off is by no means guaranteed (Draper \& Nostrand, 1979; Tibshirani, 1996).

For example, in estimating $\sigma_{Y . X}^{2}$, the PDMI estimator with $v_{\text {prior }}=7$ achieves the best RMSE with an estimate that is biased toward zero. Similarly, in estimating $\beta_{X . Y}$, the PDMI estimator with $\nu=-2$ achieves the best RMSE with an estimate that is biased toward zero. Overall, though, it is impossible to recommend the PDMI estimator with $v_{\text {prior }}=-2$ because it has the worst or second-worst RMSE in estimating seven of the nine tabled parameters. Indeed, for some parameters, its RMSE is not just large, but undefined. These undefined RMSEs show up as very large entries in the table. These are not typos.

ML turns in the best RMSEs overall. At $n=25$, ML has the best RMSE for six of the nine estimands. For some estimands where ML does not have the best RMSE, we can see its ranking improve as the sample size increases from $n=25$ to $n=100$. This is not surprising. As the sample size increases, asymptotic theory tells us that all the biases vanish and the smallest RMSE will be achieved by the ML estimates, followed by the MLMI estimates, followed by the PDMI estimates (Wang \& Robins, 1998). In addition, the differences among the PDMI estimators vanish in large samples as the choice of priors become immaterial.

## Bias Reduction

A simple way to reduce the bias of PDMI estimates is to increase $v_{\text {prior }}$. Table 2 illustrates the effect of $v_{\text {prior }}$ on simulated PDMI results with $D=5$ imputations and $v_{\text {prior }}=-2$, 0,2 , or 7 . The choice $v_{\text {prior }}=2$ eliminates the bias in $\hat{\sigma}_{Y . X, P D M I}^{2}$ (Kim, 2004; see also our Equation 21) and reduces bias in other estimates by reducing $\Sigma_{\hat{\alpha} \hat{\beta}_{Y, Y, P D}}$. The choice $\nu_{\text {prior }}=7$ further reduces bias in most estimates by reducing $\Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, P D}}$. Although $v_{\text {prior }}=7$ yields a negatively biased estimate $\hat{\sigma}_{Y . X, P D M I}^{2}$ the bias comes with a greater reduction in variability so that the estimate $\hat{\sigma}_{Y . X, P D M I}^{2}$ has the smallest mean squared error that can be achieved by any choice of $v_{\text {prior }}$ (von Hippel, 2013a).

Unfortunately, the choices $v_{\text {prior }}=2$ and 7 are not available in popular commercial software. Instead, Stata's mi impute command defaults to $v_{\text {prior }}=0$ (the Jeffreys prior) which yields bias, and offers as an alternative $v_{\text {prior }}=-2$ (the uniform prior), which makes the bias worse. $v_{\text {prior }}=$ -2 worsens the bias in two ways-first by increasing the $\operatorname{Bias}\left(\hat{\sigma}_{Y . X, P D}^{2}\right)$ according to Equation 21, and second by increasing $\Sigma_{\hat{\alpha} \hat{\beta}_{Y, X, P D}}$. In fact, with $v_{\text {prior }}=-2$ the bias and standard error of some estimates can be not just large, but undefined. More specifically, with $v_{\text {prior }}=-2, \hat{\sigma}_{Y . X, P D M I}^{2}$ and $\hat{\sigma}_{Y, \text { PDMI }}^{2}$ have undefined standard errors occur when there are $n_{0} \leq 7$ observed values (von Hippel, 2013a), which is a condition that occasionally occurred in the simulation. In the simulation, undefined expectations and standard errors show up as very large values in Table 2. These values are so large that they look like typos, but they are not.

## CONFIDENCE INTERVALS

In analyzing incomplete data, we typically want not just a point estimate but a confidence interval or equivalent hypothesis test. Given the smaller bias and greater precision of ML estimates, there is clear potential for ML confidence intervals to be shorter than PDMI confidence intervals with similar coverage. In small samples, however, confidence intervals have been more fully developed for PDMI than for ML. In this section, we review the commonly used PDMI confidence intervals and then propose new ML confidence intervals to compete with them. (We are pursuing the estimation of MLMI confidence intervals separately and do not discuss them here.)

## PDMI Confidence Intervals

PDMI confidence intervals are typically calculated as

$$
\hat{\theta}_{P D M I} \pm t \hat{V}_{P D M I}^{1 / 2}
$$

where $\hat{\theta}_{\text {PDMI }}$ is a parameter estimate, $\hat{V}_{\text {PDMI }}$ is the estimated variance of the parameter estimate, and $t$ is a quantile from

TABLE 3
Value (and Rank) of Root Mean Square Error for Different Estimators
| Estimator | $\nu_{\text {prior }}$ | $n$ | Pattern | Estimands |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  | Regression of $Y$ on $X$ |  |  | Moments of $Y$ |  |  | Regression of $X$ on $Y$ |  |  |
|  |  |  |  | $\alpha_{Y . X}$ | $\beta_{Y . X}$ | $\sigma_{Y . X}^{2}$ | $\mu_{Y}$ | $\sigma_{Y}^{2}$ | $\sigma_{X Y}$ | $\alpha_{X . Y}$ | $\beta_{X . Y}$ | $\sigma_{X . Y}^{2}$ |
| ML <br> MLMI |  | 25 | MXN | . 457 | . 712 | . 684 | . 503 | 1.335 | . 679 | . 280 | . 565 | . 695 |
|  |  |  |  | (1) | (1) | (2) | (1) | (1) | (1) | (4) | (5) | (1) |
|  |  |  | MCAR | . 266 | . 580 | . 682 | . 278 | 1.025 | . 567 | . 216 | . 594 | . 699 |
|  |  |  |  | (1) | (1) | (2) | (1) | (1) | (1) | (4) | (4) | (1) |
|  |  | 100 | MXN | . 209 | . 543 | . 736 | . 218 | 1.046 | . 542 | . 124 | . 503 | . 746 |
|  |  |  |  | (1) | (1) | (2) | (1) | (1) | (1) | (4) | (5) | (1) |
|  |  |  | MCAR | . 124 | . 516 | . 735 | . 133 | 1.003 | . 516 | . 099 | . 519 | . 740 |
|  |  |  |  | (1) | (1) | (2) | (1) | (2) | (1) | (1) | (4) | (1) |
|  |  | 25 | MXN | . 460 | . 714 | . 716 | . 505 | 1.381 | . 709 | . 285 | . 578 | . 742 |
|  |  |  |  | (2) | (2) | (3) | (2) | (2) | (2) | (5) | (6) | (6) |
|  |  |  | MCAR | . 270 | . 582 | . 715 | . 282 | 1.058 | . 593 | . 220 | . 607 | . 747 |
|  |  |  |  | (2) | (2) | (3) | (2) | (3) | (2) | (5) | (5) | (3) |
|  |  | 100 | MXN | . 211 | . 544 | . 744 | . 220 | 1.054 | . 548 | . 125 | . 506 | . 758 |
|  |  |  | MCAR <br> MCAR | (2) | (2) | (3) | (2) | (2) | (2) | (5) | (6) | (4) |
|  |  |  |  | . 127 | . 517 | . 743 | . 136 | 1.010 | . 522 | . 100 | . 522 | . 752 |
|  |  |  |  | (2) | (2) | (3) | . 926 <br> 926 | (3) | (2) | (4) | (5) | (3) |
| PDMI | -2 | 25 | MXN <br> MXN | . 682 | . 957 | 678 |  | 731 | . 873 | . 266 | . 420 | . 733 |
|  |  |  |  | (6) | (6) | (6) | (6) | (6) <br> $73830{ }^{\text {a }}$ <br> $73830{ }^{\text {a }}$ <br> (6) | (6) | (1) | (1) | (5) |
|  |  |  | MCAR | 1.819 | . 810 | $76986{ }^{\text {a }}$ | 1.801 |  | . 809 | . 207 | . 479 | . 790 |
|  |  | 100 |  | (6) | (6) | (6) | (6) |  | (6) | (1) | (1) | (6) |
|  |  |  | MXN | . 228 | . 551 | . 805 | . 237 | 1.155 <br> (6) <br> 1.155 | . 555 | . 123 | . 462 | . 762 |
|  |  |  |  | (6) | (6) | (6) | (6) |  | (6) | (2) | (1) | (6) |
|  |  | 25 | MCAR | . 131 | . 518 | . 805 | . 139 | 1.076 | . 523 | . 100 | . 494 | . 764 |
|  |  |  |  | (6) | (4) | (6) | (6) | (6) | (4) | (2) | (1) | (6) |
|  |  |  | MCAR | . 682 | . 957 | 678 | . 926 | 731.552 | . 873 | . 266 | . 420 | . 733 |
|  |  |  |  | (6) | (6) | (6) | (6) | (6) | (6) | (1) | (1) | (5) |
| PDMI | 0 | 25 <br> 25 | MXN | . 506 | . 752 | 1.208 | . 559 | 2.414 | . 744 | . 272 | . 461 | . 721 |
|  |  |  | MCAR | (5) | (5) | (5) | (5) | (5) | (5) | (2) | (2) | (4) |
|  |  |  |  | . 286 | . 592 | 2.823 | . 296 | 3.230 | . 602 | . 212 | . 526 | . 770 |
|  |  | 100 |  | (5) | (5) | (5) | (5) | (5) | (5) | (2) | (2) | (5) |
|  |  | 哩的 | MXN <br> MCAR <br> MXN | . 226 | . 550 | . 786 | . 235 | 1.133 | . 554 | . 123 | . 470 | . 759 |
|  |  | 25 <br> 25 |  | (4) | (4) | (5) | (4) | (5) | (4) | (1) | (2) | (5) |
|  |  |  |  |  | . 130 | . 518 | . 785 | . 139 | 1.057 | . 523 | . 100 | . 503 | . 760 |
|  |  |  |  |  | (5) | (6) | (5) | (5) | (5) | (5) | (3) | (2) | (5) |
|  |  |  |  |  | MCAR <br> MCAR | . 286 | . 592 | 2.823 | 296 | 3.230 | . 602 | . 212 | . 526 | . 770 |
|  |  |  |  | (5) |  | (5) | (5) | (5) | (5) | (5) | (2) | (2) | (5) |
| PDMI | 2 | 25 | MXN | . 494 | . 742 | . 835 | . 544 | 1.736 | . 735 | . 277 | . 495 | . 714 |
|  |  |  |  | (4) | (4) | (4) | (4) | (4) | (4) | (3) | (3) | (3) |
|  |  |  | MCAR | . 280 | . 589 | . 832 | 291 | 1.220 | . 599 | . 216 | . 562 | . 755 |
|  |  | 100 |  | (4) | (4) | (4) | (4) | (4) | (4) | (3) | (3) | (4) |
|  |  |  | MXN | . 226 | . 551 | . 768 | . 235 | 1.116 | . 555 | . 124 | . 478 | . 756 |
|  |  |  |  | (5) | (5) | (4) | (5) | (4) | (5) | (3) | (3) | (3) |
|  |  | 25 | MCAR | . 130 | . 518 | . 767 | 138 | 1.039 | . 523 | . 100 | . 511 | . 756 |
|  |  |  |  | (4) | (5) | (4) | (4) | (4) | (6) | (5) | (3) | (4) |
|  |  |  | MCAR | . 494 | . 742 | . 835 | . 544 | 1.736 | . 735 | . 277 | . 495 | . 714 |
|  |  |  |  | (4) | (4) | (4) | (4) | (4) | (4) | (3) | (3) | (3) |
| PDMI | 7 | 25 <br> 25 | MXN | . 481 | . 732 | . 673 | 528 | 1.507 | . 725 | . 289 | . 556 | . 700 |
|  |  |  |  | (3) | (3) | (1) | (3) | (3) | (3) | (6) | (4) | (2) |
|  |  |  | MCAR | . 275 | . 586 | . 672 | 286 | 1.051 | . 596 | . 225 | . 627 | . 729 |
|  |  | 100 |  | (3) | (3) | (1) | (3) | (2) | (3) | (6) | (6) | (2) |
|  |  |  | MXN | . 224 | . 549 | . 731 | . 232 | 1.074 | . 553 | . 125 | . 495 | . 749 |
|  |  |  |  | (3) | (3) | (1) | (3) | (3) | (3) | (6) | (4) | (2) |
|  |  | 25 | MCAR | . 130 | . 517 | . 730 | 138 | 1.001 | . 522 | . 101 | . 528 | . 748 |
|  |  |  |  | (3) | (3) | (1) | (3) | (1) | (3) | (6) | (6) | (2) |
|  |  |  |  | . 481 | . 732 | . 673 | . 528 | 1.507 | . 725 | . 289 | . 556 | . 700 |
|  |  |  |  |  |  | (1) | (3) | (3) | (3) | (6) | (4) | (2) |


Note. $\mathrm{ML}=$ maximum likelihood; $\mathrm{MXN}=$ data missing at random pattern where $Y$ values are missing if $X$ is negative; MCAR $=$ data missing completely at random; MLMI = maximum likelihood multiple imputation; PDMI = posterior draw multiple imputation. For each sample size and pattern, the estimator with the smallest root mean square error is ranked 1 , and the estimator with the largest root mean square error is ranked 6 .

[^2]a $t$ distribution ${ }^{2}$ with $\hat{v}_{\text {PDMI }}$ degrees of freedom. The degrees of freedom are estimated as
$$
\hat{v}_{P D M I}=\left(\frac{1}{\hat{v}_{D}}+\frac{1}{\hat{v}_{o b s}}\right)^{-1}
$$
(Barnard \& Rubin, 1999), where
$$
\hat{v}_{D}=(D-1) \hat{v}_{P D M I}^{-2}
$$
and
$$
\hat{v}_{o b s}=v_{c o m}\left(1-\hat{\gamma}_{P D M I}\right)\left(\frac{v_{c o m}+1}{v_{c o m}+3}\right)
$$
estimate the respective degrees of freedom in the imputations and in the observed data. Here $\hat{\gamma}_{\text {PDMI }}$ is an estimate of the fraction of missing information, and $v_{c o m}$ is the degrees of freedom that would be used if the data were completefor example, $v_{\text {com }}=n-2 \mathrm{f}$ for a simple linear regression. Finally, $\hat{\gamma}_{\text {PDMI }}$ and $\hat{V}_{\text {PDMI }}$ are estimated as follows:
$$
\begin{aligned}
& \hat{V}_{P D M I}=\hat{W}_{P D M I}+\left(1+\frac{1}{D}\right) \hat{B}_{P D M I} \\
& \hat{\gamma}_{P D M I}=\left(1+\frac{1}{D}\right) \frac{\hat{W}_{P D M I}}{\hat{V}_{P D M I}}
\end{aligned}
$$
(Rubin, 1987), where
$$
\begin{aligned}
& \hat{W}_{P D M I}=\frac{1}{D} \sum_{d=1}^{D} \hat{W}_{P D S I, d} \\
& \hat{B}_{P D M I}=\frac{1}{D-1} \sum_{d=1}^{D}\left(\hat{\theta}_{P D S I}-\hat{\theta}_{P D M I}\right)^{2}
\end{aligned}
$$
are the variances within and between the $D$ imputed data sets. More specifically, $\hat{B}_{\text {PDMI }}$ is the variance of $\hat{\theta}_{\text {PDSI, } d}$ from one imputed data set to another, and $\hat{W}_{\text {PDMI }}$ is the average value of the statistic $\hat{W}_{\text {PDSI, } d}$ that would estimate the variance of $\hat{\theta}_{\text {PDSI, } d}$ if the SI data set were complete rather than partly imputed (e.g., $\hat{W}_{\text {PDSI, } d}=\hat{\sigma}_{Y, \text { PDMI }}^{2} / n$ if $\hat{\theta}_{\text {PDSI, } d}=\hat{\mu}_{Y, D M I, d}$ ).

In initial simulations, we found that estimation error in $\hat{v}_{\text {PDMI }}$ could occasionally result in confidence intervals that were orders of magnitude longer than they needed to be to achieve nominal coverage. Because of estimation error, it is quite possible for the estimated degrees of freedom $\hat{v}_{\text {PDMI }}$ to be close to 0 , although it is hard to imagine a realistic

[^3]situation where the true degrees of freedom would be less than 2 or 3 . Small values of $\hat{v}_{\text {PDMI }}$ are a serious problem because as $\hat{v}_{\text {PDMI }}$ approaches zero, the $t$ quantile used in the confidence interval becomes arbitrarily large. For example, if $\hat{v}_{\text {PDMI }}=1$, a $95 \%$ confidence interval has $t \approx 12.7$; if $\hat{v}_{\text {PDMI }}=1 / 2$, a $95 \%$ confidence interval has $t \approx 165$, and if $\hat{v}_{\text {PDMI }}=1 / 4$, a $95 \%$ confidence interval has $t \approx 43,640$. To put this another way, when $\hat{v}_{\text {PDMI }} \leq 2$ the $t$ distribution has such heavy tails that its variance is undefined, and when $\hat{v}_{\text {PDMI }} \leq 1$ the mean of the $t$ distribution is undefined as well. Small $\hat{v}_{\text {PDMI }}$ values occurred with some frequency in our simulation; for example, with $n=25$ and values MXN, about $24 \%$ of $\hat{v}_{\text {PDMI }}$ values were less than $3,11 \%$ were less than 2 , and $2 \%$ were less than 1 .

To ensure against too-small values of $\hat{v}_{P D M I}$, we replaced $\hat{v}_{\text {PDMI }}$ with the bounded estimator

$$
\tilde{v}_{P D M I}=\max \left(3, \hat{v}_{P D M I}\right),
$$

which, as it never goes under 3, can never produce a $t$ statistic with an undefined mean, an undefined variance, or very extreme quantiles. This change will have little impact on coverage if in fact the true degrees of freedom are at least 3-which is almost always a safe bet. If for some reason one believes that the true degrees of freedom are less than 3 , one can use a lower bound of 2 or 2.5, which in our simulation produced similar results.

## ML Confidence Intervals

Under ML, the standard error of a scalar parameter estimate $\hat{\theta}_{M L}$ can be estimated as $\hat{I}_{\text {obs }, i}^{-1 / 2}$, which is the square root of a diagonal element of the inverse of the observed information matrix $\hat{I}_{\text {obs }}$. Then in large samples, a normal confidence interval can be calculated as

$$
\hat{\theta}_{M L} \pm z \hat{I}_{o b s, i}^{-1 / 2}
$$

where $z$ is a quantile from the standard normal distribution.
In small samples, normal confidence intervals are too short to achieve full coverage, and better results can be achieved with an approximate ${ }^{3} t$ interval like

$$
\hat{\theta}_{M L} \pm \hat{t} \hat{I}_{o b s, i}^{-1 / 2}
$$

The only trick is estimating the degrees of freedom for the $t$ quantile. Some degrees of freedom estimators have been proposed, but they are limited to specific estimates such as $\hat{\mu}_{Y, M L}$ or $\hat{\mu}_{Y, M L}-\hat{\mu}_{X, M L}$ (Little, 1976, 1988; Morrison, 1973).

[^4]We now propose a more general estimator for degrees of freedom under ML. There are two ways to reach similar results. For the first approach, consider estimating a regression. In complete data, confidence intervals for the regression slopes and intercept would be calculated using a $t$ distribution with degrees of freedom

$$
v_{c o m}=n-k
$$

where $n$ is the sample size and $k$ is the number of regression parameters (slopes and intercept).

With incomplete data, we can use the same formula but replace $n$ with the effective sample size, by which we mean the sample size that, in complete data, would provide the same amount of information about the parameter as we get from the incomplete data. The effective sample size in incomplete data is estimated by $n\left(1-\hat{\gamma}_{M L}\right)$, which is the sample size reduced by an estimate $\hat{\gamma}_{M L}$ of the fraction of missing information. So the degrees of freedom for a regression parameter is

$$
\hat{v}_{M L}^{*}=n\left(1-\hat{\gamma}_{M L}\right)-k .
$$

This formula can be used whenever we estimate a linear regression. Outside of the regression context, though, it is not always the case that the complete data degrees of freedom $v_{\text {comp }}$ is estimated simply by subtracting the number of parameters from the sample size. We therefore need a more general formula that will apply whenever $v_{\text {comp }}$ is known. To motivate this more general formula, remember that, in large samples, the ML estimator is equivalent to the PDMI estimator with infinite imputations (Wang \& Robins, 1998). This is a large-sample relationship, but it remains useful, if approximate, in small samples as well. Exploiting the relationship, we take the limit of $\hat{v}_{\text {PDMI }}$ as the number of imputations $D$ goes to infinity, and arrive at the following estimate for the degrees of freedom under ML:

$$
\hat{v}_{M L}=v_{c o m}\left(1-\hat{\gamma}_{M L}\right)\left(\frac{v_{c o m}+1}{v_{c o m}+3}\right) .
$$

$\hat{v}_{M L}$ and $\hat{v}_{M L}^{*}$ are not equal but they are very similar. For example, in a simple linear regression with $n=25, k=2$, and $\hat{\gamma}_{M L}=.5$, the two formulas give $\hat{v}_{M L}=10.6$ and $\hat{v}_{M L}^{*}=10.5$.

To calculate $\hat{v}_{M L}$ or $\hat{v}_{M L}^{*}$, we need $\hat{\gamma}_{M L}$, which is an ML estimate of the fraction of missing information. Following Savalei and Rhemtulla (2012) we calculate $\hat{\gamma}_{M L}$ in two steps. First, we enter the incomplete data into ML software to obtain ML point estimates $\hat{\mu}_{X Y, M L}, \hat{\Sigma}_{X Y, M L}$ and an estimate $\hat{I}_{\text {obs }}$ of the observed information. Then we supply the same software with the point estimates $\hat{\mu}_{X Y, M L}, \hat{\Sigma}_{X Y, M L}$ and a sample size $n$ that implies that the data are complete. This tricks the software into calculating $\hat{I}_{\text {com }}$, which estimates the information that would be available if the data were complete.

For each estimand, the fraction of information that is observed is $\hat{I}_{o b s, i}^{-1} \hat{I}_{c o m, i}$, so the fraction of missing information is

$$
\hat{\gamma}_{M L}=1-\hat{I}_{o b s, i}^{-1} \hat{I}_{c o m, i} .
$$

Because of estimation error in $\hat{\gamma}_{M L}$, it is possible although very rare for $\hat{v}_{M L}$ or $\hat{v}_{M L}^{*}$ to take values less than 3, which as discussed earlier will leave the $t$ distribution with an undefined variance and confidence intervals with unnecessary length. To avoid this, we recommend setting a lower bound of 3 on the degrees of freedom-that is, using

$$
\begin{aligned}
& \tilde{v}_{M L}=\max \left(3, \hat{v}_{M L}\right) \\
& \text { or } \tilde{v}_{M L}^{*}=\max \left(3, \hat{v}_{M L}^{*}\right)
\end{aligned}
$$

which mirrors the formula that we offered for $\tilde{v}_{P D M I}$.
In an online Appendix, we illustrate how to calculate $\tilde{v}_{M L}$ and $\hat{\gamma}_{M L}$ using the CALIS procedure in SAS software. Savalei and Rhemtulla (2012) showed how to calculate $\hat{\gamma}_{M L}$ in Mplus, R, and EQS. It would be easy for vendors to modify any of these software packages to provide $\hat{\gamma}_{M L}$ and $\tilde{v}_{M L}$ or $\tilde{v}_{M L}^{*}$ automatically.

## Results

In our simulation, we estimated the mean length and coverage of nominal 95\% confidence intervals. For most of the parameters $\left(\alpha_{Y . X}, \beta_{Y . X}, \mu_{Y}, \alpha_{X . Y}, \beta_{X . Y}, \sigma_{X Y}\right)$ we applied the confidence interval formulas directly to the parameter estimates. For the variance parameters ( $\sigma_{X . Y}^{2}, \sigma_{Y}^{2}, \sigma_{Y . X}^{2}$ ) we used a cuberoot transformation to bring the estimates closer to a normal distribution (Hawkins \& Wixley, 1986). ${ }^{4}$

Table 4 gives the mean length and coverage of confidence intervals using the usual formulas; that is, under ML we used the normal confidence intervals in Equation 28 and under PDMI we used $t$-based confidence intervals with the unbounded degrees of freedom estimator in Equation 23. The results highlight the limitations of the usual formulas. Under ML the confidence intervals are too short and cover the estimands less than $95 \%$ of the time. With $n=100$ the coverage is just $0 \%$ to $3 \%$ under the nominal level, but with $n=25$ it is $5 \%$ to $6 \%$ under the nominal level for the regression intercept and slope, and $8 \%$ to $14 \%$ under

[^5]TABLE 4
Mean Length (and Coverage \%) of Nominal 95\% Confidence Intervals, Using the Usual Formulas
| Estimator | $\nu_{\text {prior }}$ | n | Pattern | Regression of $Y$ on $X$ |  |  | Estimands |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  |  |  | Moments of $Y$ |  |  | Regression of $X$ on $Y$ |  |  |
|  |  |  |  | $\alpha_{Y . X}$ | $\beta_{Y . X}$ | $\sigma_{Y . X}^{2}$ | $\mu_{Y}$ | $\sigma_{Y}^{2}$ | $\sigma_{X Y}$ | $\alpha_{X . Y}$ | $\beta_{X . Y}$ | $\sigma_{X . Y}^{2}$ |
| ML |  | 25 | MXN | 1.5 (89\%) | 1.6 (90\%) | 1.0 (83\%) | 1.7 (91\%) | 2.4 (90\%) | 1.7 (92\%) | 1.1 (90\%) | 1.3 (90\%) | 1.2 (87\%) |
|  |  |  | MCAR | 0.9 (90\%) | 1.0 (89\%) | 1.0 (82\%) | 1.0 (91\%) | 1.5 (87\%) | 1.1 (90\%) | 0.8 (92\%) | 1.0 (90\%) | 0.9 (87\%) |
|  |  | 100 | MXN | 0.8 (94\%) | 0.8 (94\%) | 0.6 (92\%) | 0.8 (94\%) | 1.0 (93\%) | 0.8 (94\%) | 0.5 (94\%) | 0.6 (94\%) | 0.6 (92\%) |
|  |  |  | MCAR | 0.5 (94\%) | 0.5 (94\%) | 0.6 (92\%) | 0.5 (94\%) | 0.8 (93\%) | 0.6 (94\%) | 0.4 (94\%) | 0.4 (94\%) | 0.5 (93\%) |
| PDMI | -2 | 25 | MXN | $1.9 \mathrm{E}+10{ }^{\mathrm{a}}$ (97\%) | $1.3 \mathrm{E}+11{ }^{\text {a }}$ (98\%) | 3.4E+13 ${ }^{\mathrm{a}}$ (97\%) | 60.3 (97\%) | 1.6E+181 ${ }^{\text {a }}$ (98\%) | $4.8 \mathrm{E}+09^{\mathrm{a}}$ (98\%) | 1.6 (95\%) | 3.0E+04 ${ }^{\text {a }}$ (96\%) | 3.3 (96\%) |
|  |  |  | MCAR | 2.4 (97\%) | 65.3 (97\%) | $4.8 \mathrm{E}+16$ (97\%) | 2.2 (97\%) | $2.9 \mathrm{E}+16$ (97\%) | 40.3 (97\%) | 0.9 (96\%) | 1.6 (96\%) | 3.1 (96\%) |
|  |  | 100 | MXN | 1.3 (95\%) | 1.3 (95\%) | 0.8 (95\%) | 1.2 (95\%) | 1.5 (95\%) | 1.2 (95\%) | 0.6 (96\%) | 0.8 (96\%) | 0.8 (94\%) |
|  |  |  | MCAR | 0.6 (95\%) | 0.6 (95\%) | 0.8 (95\%) | 0.6 (95\%) | 1.0 (95\%) | 0.7 (96\%) | 0.4 (96\%) | 0.5 (95\%) | 0.5 (95\%) |
| PDMI | 0 | 25 | MXN | $2.5 \mathrm{E}+10^{\mathrm{a}}$ (97\%) | $2.7 \mathrm{E}+06{ }^{\mathrm{a}}$ (97\%) | 807.5 (94\%) | 9.4 (96\%) | 1.1E+05 ${ }^{\mathrm{a}}$ (97\%) | 4.1 (97\%) | 1.6 (94\%) | 154.8 (96\%) | 2.7 (94\%) |
|  |  |  | MCAR | 1.9 (96\%) | 1.0E+13 ${ }^{\mathrm{a}}$ (95\%) | 3.1E+08 ${ }^{\mathrm{a}}$ (94\%) | 1.7 (96\%) | 1.8E+08 ${ }^{\mathrm{a}}$ (96\%) | 1.8 (96\%) | 0.9 (96\%) | 1.4 (95\%) | 1.4 (94\%) |
|  |  | 100 | MXN | 1.2 (95\%) | 1.3 (95\%) | 0.7 (94\%) | 1.2 (95\%) | 1.5 (94\%) | 1.2 (95\%) | 0.6 (96\%) | 0.8 (96\%) | 0.8 (94\%) |
|  |  |  | MCAR | 0.6 (95\%) | 0.6 (95\%) | 0.7 (94\%) | 0.6 (96\%) | 1.0 (95\%) | 0.6 (95\%) | 0.4 (95\%) | 0.5 (95\%) | 0.5 (95\%) |
| PDMI | 2 | 25 | MXN | $4.4 \mathrm{E}+07{ }^{\mathrm{a}}$ (96\%) | 1.8E+07 ${ }^{\mathrm{a}}$ (96\%) | 9.0E+04 ${ }^{\text {a }}$ (90\%) | 53.7 (95\%) | $3.3 \mathrm{E}+08^{\mathrm{a}}$ (96\%) | 3.6 (96\%) | 1.6 (93\%) | 106.6 (95\%) | 3.7 (93\%) |
|  |  |  | MCAR | 1.5 (95\%) | 60.6 (94\%) | $1.4 \mathrm{E}+10$ (91\%) | 1.4 (95\%) | $9.8 \mathrm{E}+09$ (94\%) | 1.6 (95\%) | 0.9 (95\%) | 1.4 (94\%) | 1.2 (92\%) |
|  |  | 100 | MXN | 1.2 (95\%) | 1.2 (94\%) | 0.7 (93\%) | 1.2 (95\%) | 1.4 (94\%) | 1.2 (95\%) | 0.6 (95\%) | 0.8 (95\%) | 0.8 (94\%) |
|  |  |  | MCAR | 0.6 (95\%) | 0.6 (94\%) | 0.7 (94\%) | 0.6 (95\%) | 0.9 (95\%) | 0.6 (95\%) | 0.4 (95\%) | 0.5 (94\%) | 0.5 (94\%) |
| PDMI | 7 | 25 | MXN | 1.0E+16 ${ }^{\mathrm{a}}$ (94\%) | $7.3 \mathrm{E}+15{ }^{\mathrm{a}}$ (94\%) | 1.3 (79\%) | 4.8 (93\%) | 13.2 (92\%) | 2.8 (95\%) | 1.5 (91\%) | 63.1 (92\%) | 2.0 (90\%) |
|  |  |  | MCAR | 1.2 (92\%) | 58.8 (91\%) | 1.1 (79\%) | 1.2 (93\%) | 2.0 (88\%) | 1.4 (93\%) | 0.9 (94\%) | 1.2 (90\%) | 1.1 (88\%) |
|  |  | 100 | MXN | 1.2 (94\%) | 1.2 (94\%) | 0.6 (91\%) | 1.1 (94\%) | 1.3 (93\%) | 1.1 (94\%) | 0.6 (95\%) | 0.8 (94\%) | 0.8 (93\%) |
|  |  |  | MCAR | 0.6 (94\%) | 0.6 (93\%) | 0.6 (90\%) | 0.6 (95\%) | 0.9 (92\%) | 0.6 (95\%) | 0.4 (95\%) | 0.5 (93\%) | 0.5 (93\%) |


Note. $\mathrm{ML}=$ maximum likelihood; $\mathrm{MXN}=$ data missing at random pattern where $Y$ values are missing if $X$ is negative; MCAR $=$ data missing completely at random; PDMI = posterior draw multiple imputation.
${ }^{\text {a }}$ In some cells, very large estimates for the mean length indicate that the true mean length is undefined.
the nominal level for the residual variance. Under PDMI, the confidence intervals have closer to $95 \%$ coverage but are longer, on average, than they need to be. In fact, with $n=25$, some of the mean lengths estimated from the PDMI simulation are so large-e.g., $2.6 \mathrm{E}+31$-that the true mean length must be not just large, but undefined. An undefined mean length can occur, as noted earlier, if $\hat{v}_{\text {PDMI }} \leq 1$.

Table 5 displays results obtained from our improved confidence intervals. Under PDMI we used $t$-based confidence intervals with $\tilde{v}_{\text {PDMI }}$ degrees of freedom, and
under ML we used $t$-based confidence intervals with $\tilde{v}_{M L}^{*}$ degrees of freedom. (Very similar results, not shown, were obtained with $\tilde{v}_{M L}$.) Remember that $\tilde{v}_{P D M I}, \tilde{v}_{M L}$, and $\tilde{v}_{M L}^{*}$ are all constrained to take values no smaller than 3.

The results highlight our improvements. The PDMI confidence intervals still have close to $95 \%$ coverage but they are shorter than they were before, and they always have defined mean lengths. The fact that the PDMI confidence intervals have close to $95 \%$ coverage is a little surprising in view of the bias in the point estimates. Evidently PDMI confidence

TABLE 5
Mean Length (and Coverage \%) of Nominal 95\% Confidence Intervals, Using Our Improved Formulas
| Estimator | $v_{\text {prior }}$ | $n$ | Pattern | Estimands |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  | Regression of $Y$ on $X$ |  |  | Moments of $Y$ |  |  | Regression of $X$ on $Y$ |  |  |
|  |  |  |  | $\alpha_{Y . X}$ | $\beta_{Y . X}$ | $\sigma_{Y . X}^{2}$ | $\mu_{Y}$ | $\sigma_{Y}^{2}$ | $\sigma_{X Y}$ | $\alpha_{X . Y}$ | $\beta_{X . Y}$ | $\sigma_{X . Y}^{2}$ |
| ML |  | 25 | MXN | 2.4 (98\%) | 2.6 (98\%) | 1.2 (87\%) | 2.4 (97\%) | 3.4 (94\%) | 2.3 (98\%) | 1.4 (93\%) | 1.8 (94\%) | 1.5 (93\%) |
|  |  |  | MCAR | 1.1 (93\%) | 1.2 (93\%) | 1.2 (86\%) | 1.1 (94\%) | 1.8 (91\%) | 1.2 (93\%) | 0.8 (94\%) | 1.1 (93\%) | 1.0 (90\%) |
|  |  | 100 | MXN | 0.9 (96\%) | 0.9 (96\%) | 0.6 (93\%) | 0.9 (96\%) | 1.1 (93\%) | 0.9 (96\%) | 0.5 (95\%) | 0.6 (94\%) | 0.7 (93\%) |
|  |  |  | MCAR | 0.5 (95\%) | 0.5 (94\%) | 0.6 (93\%) | 0.5 (95\%) | 0.8 (94\%) | 0.6 (95\%) | 0.4 (95\%) | 0.5 (94\%) | 0.5 (94\%) |
| PDMI | -2 | 25 | MXN | 3.7 (97\%) | 3.9 (97\%) | 7.0 (96\%) | 4.0 (97\%) | 26.5 (98\%) | 3.9 (98\%) | 1.5 (95\%) | 1.9 (96\%) | 1.7 (96\%) |
|  |  |  | MCAR | 2.0 (97\%) | 2.2 (97\%) | 166.5 (97\%) | 2.0 (97\%) | 403.6 (97\%) | 2.3 (97\%) | 0.9 (96\%) | 1.3 (96\%) | 1.2 (96\%) |
|  |  | 100 | MXN | 1.2 (95\%) | 1.3 (95\%) | 0.8 (95\%) | 1.2 (95\%) | 1.5 (95\%) | 1.2 (95\%) | 0.6 (96\%) | 0.8 (96\%) | 0.8 (94\%) |
|  |  |  | MCAR | 0.6 (95\%) | 0.6 (95\%) | 0.8 (95\%) | 0.6 (95\%) | 1.0 (95\%) | 0.7 (96\%) | 0.4 (96\%) | 0.5 (95\%) | 0.5 (95\%) |
| PDMI | 0 | 25 | MXN | 3.1 (96\%) | 3.3 (96\%) | 2.5 (94\%) | 3.2 (96\%) | 6.4 (97\%) | 3.2 (97\%) | 1.5 (94\%) | 1.9 (95\%) | 1.6 (94\%) |
|  |  |  | MCAR | 1.5 (96\%) | 1.7 (95\%) | 2.6 (94\%) | 1.6 (96\%) | 3.6 (96\%) | 1.7 (96\%) | 0.9 (96\%) | 1.3 (95\%) | 1.2 (94\%) |
|  |  | 100 | MXN | 1.2 (95\%) | 1.2 (95\%) | 0.7 (94\%) | 1.2 (95\%) | 1.5 (94\%) | 1.2 (95\%) | 0.6 (96\%) | 0.8 (96\%) | 0.8 (94\%) |
|  |  |  | MCAR | 0.6 (95\%) | 0.6 (95\%) | 0.7 (94\%) | 0.6 (96\%) | 1.0 (95\%) | 0.6 (95\%) | 0.4 (95\%) | 0.5 (95\%) | 0.5 (95\%) |
| PDMI | 2 | 25 | MXN | 2.8 (95\%) | 2.9 (95\%) | 1.8 (90\%) | 2.9 (95\%) | 5.2 (95\%) | 2.9 (96\%) | 1.4 (93\%) | 1.9 (95\%) | 1.5 (93\%) |
|  |  |  | MCAR | 1.4 (95\%) | 1.5 (94\%) | 1.8 (90\%) | 1.4 (95\%) | 2.7 (94\%) | 1.5 (95\%) | 0.9 (95\%) | 1.3 (94\%) | 1.1 (92\%) |
|  |  | 100 | MXN | 1.2 (95\%) | 1.2 (94\%) | 0.7 (93\%) | 1.2 (95\%) | 1.4 (94\%) | 1.2 (95\%) | 0.6 (95\%) | 0.8 (95\%) | 0.8 (94\%) |
|  |  |  | MCAR | 0.6 (95\%) | 0.6 (94\%) | 0.7 (94\%) | 0.6 (95\%) | 0.9 (95\%) | 0.6 (95\%) | 0.4 (95\%) | 0.5 (94\%) | 0.5 (94\%) |
| PDMI | 7 | 25 | MXN | 2.3 (93\%) | 2.4 (93\%) | 1.1 (79\%) | 2.4 (93\%) | 3.6 (92\%) | 2.4 (95\%) | 1.4 (91\%) | 1.8 (92\%) | 1.4 (89\%) |
|  |  |  | MCAR | 1.1 (91\%) | 1.2 (91\%) | 1.1 (79\%) | 1.2 (93\%) | 1.9 (88\%) | 1.3 (93\%) | 0.9 (94\%) | 1.2 (90\%) | 1.0 (88\%) |
|  |  | 100 | MXN | 1.1 (94\%) | 1.2 (94\%) | 0.6 (91\%) | 1.1 (94\%) | 1.3 (93\%) | 1.1 (94\%) | 0.6 (95\%) | 0.8 (94\%) | 0.8 (93\%) |
|  |  |  | MCAR | 0.6 (94\%) | 0.6 (93\%) | 0.6 (90\%) | 0.6 (95\%) | 0.9 (92\%) | 0.6 (95\%) | 0.4 (95\%) | 0.5 (93\%) | 0.5 (93\%) |


intervals are long enough to cover not just the variability of the point estimate, but to cover some bias as well.

The ML confidence intervals are also improved. They are longer than they were before and the extra length brings them within $2 \%$ of nominal coverage for most parameters. At $n=25$, coverage is a bit lower for the parameters whose point estimates are biased. Evidently the ML confidence intervals are only long enough to cover variability in the point estimate. Unlike the PDMI confidence intervals, the ML confidence intervals are not long enough to cover bias as well.

On the whole, the ML confidence intervals are quite competitive with the PDMI confidence intervals. The ML
confidence intervals have good coverage and are shorter than the PDMI confidence intervals with $v_{\text {prior }}=-2,0$, or 2 . The PDMI confidence intervals with $v_{\text {prior }}=7$ are approximately as short as the ML confidence intervals, but have slightly lower coverage.

## CONCLUSION

With our new confidence intervals, ML performs at least as well as MI in small samples. The new ML confidence intervals have close to nominal coverage and are shorter than MI confidence intervals with the same coverage. Our ML
confidence intervals are easy to implement in SEM software, and we recommend that vendors make them part of the standard output. In addition, our results show that ML point estimates can be less biased and more precise than MI estimates in small samples. Previous results show that ML estimates are more precise than MI estimates in large samples as well (Wang \& Robins, 1998).

The quality of estimates is not the only advantage of ML over MI. ML runs more quickly than MI and, unlike MI, ML does not request the user to store and analyze multiple copies of the data. Storage and runtime are not major concerns in small samples, but can be serious issues in large samples, particularly if the analysis runs slowly on each imputed data set (von Hippel, 2005). In addition, MI often requires the user to specify separate models for the imputation and analysis, and to ensure that assumptions made by the imputation model do not bias the results of the analysis (Meng, 1994; Schafer, 1997). This can be a tricky issue, and can crop up in unexpected ways-for example, when variables interact, or are transformed to reduce skew (von Hippel, 2009, 2013b). Finally, MI sometimes requires the user to make thorny decisions about Markov chain Monte Carlo, an iterative method that is commonly used to generate posterior draws. None of these issues come up with ML.

Our general recommendation is to prefer ML (with the new confidence intervals) over MI whenever both options are available, but this does not mean than MI should never be used. There are common situations when ML is not an option. ML has rather strict requirements. ML requires a parametric model that can be estimated by maximum likelihood and used to derive the parameters of the analytic model. The analytic model need not be identical to the model that is used to maximize the likelihood, but it must be possible to derive the parameters of the analytic model from the parameters of the model that is used to maximize the likelihood (Savalei \& Bentler, 2009; Yuan \& Lu, 2008).

MI is more flexible. Although the most popular flavor of MI has the same requirements as ML (Schafer, 1997), there are flavors of MI that do not require that the parameters of the analytic model can be derived from the parameters of the imputation model. MI can use very different parametric models for imputation and analysis (Raghunathan, Lepkowski, Van Hoewyk, \& Solenberger, 2001; Van Buuren \& Oudshoorn, 1999). MI can also impute values nonparametrically, using a "hot-deck" procedure that replaces the missing values by sampling from the observed values (Andridge \& Little, 2010). The flexibility of MI can have both advantages and disadvantages. The advantage is that the imputed values can look very realistic (Demirtas \& Hedeker, 2008; He \& Raghunathan, 2012). The potential disadvantage is that bias can be introduced by unnoticed conflicts between the assumptions of the imputation model and the assumptions of the analytic model (e.g., von Hippel, 2009, 2013b).

A further advantage of MI is that it can be used when we plan to analyze the data using techniques that are not based on the likelihood, such as quantile regression or
the generalized method of moments. Finally, MI is more widely implemented in software. Users who are not using SEM software-for example, a user running the LOGISTIC procedure in SAS-will often find that MI is available but ML is not.

When MI must be used, our results suggest several ways improve MI estimates. First, Equation 27 offers a way to improve the degrees of freedom estimate that is used for PDMI confidence intervals. In addition, we have shown that PDMI point estimates can be improved by using a Bayesian prior with $2 \leq v_{\text {prior }} \leq 7$ degrees of freedom rather than the usual default of $\nu_{\text {prior }}=0$. Software should permit users to choose options in the range $0 \leq \nu_{\text {prior }} \leq 7$, perhaps with $v_{\text {rior }}=2$ as a default. The option $v_{\text {prior }}=-2$, currently available in Stata, produces such poor estimates that it should never be used.

For simplicity's sake, our presentation focused on bivariate normal data, but some of our conclusions apply more broadly. Our degrees of freedom formula (Equation 31) was derived from general principles and does not assume that the data are normally distributed. The small-sample biases that we observed under PDMI also have a source that will generalize to other settings: Variation in the posterior draws adds to variation in the imputed variable. The biases introduced by this extra variation are not limited to the bivariate normal case. Indeed, similar biases have been observed in a simulation with five multivariate normal variables; that simulation also found that the biases were smaller under ML than under PDMI (Table A10 in Yuan et al., 2012).

In nonnormal data, the biases that we have observed might actually be worse. In normal data, the mean and variance estimates are independent, which is why our simulation found that a mean can be unbiased even if the variance is biased, or a regression slope can be unbiased if the residual variance is biased. Such examples would not be possible in binomial or Poisson data where the mean and variance are not independent parameters. In those settings, if the variance is biased, it seems inevitable that the mean and regression slopes will be biased as well. However, this prediction should be tested in future work.

## SUPPLEMENTAL MATERIAL

Supplemental data for this article can be accessed www.tandfonline.com/hsem.

## REFERENCES

Allison, P. D. (2002). Missing data. Thousand Oaks, CA: Sage.
Anderson, T. W. (1957). Maximum likelihood estimates for a multivariate normal distribution when some observations are missing. Journal of the American Statistical Association, 52, 200-203. doi:10.1080/ 01621459.1957 .10501379

Andridge, R. R., \& Little, R. J. A. (2010). A review of hot deck imputation for survey non-response. International Statistical Review, 78(1), 40-64. doi:10.1111/j.1751-5823.2010.00103.x
Barnard, J., \& Rubin, D. B. (1999). Small-sample degrees of freedom with multiple imputation. Biometrika, 86, 948-955. doi:10.1093/biomet/ 86.4.948

Barnes, S. A., Lindborg, S. R., \& Seaman, J. W. (2006). Multiple imputation techniques in small sample clinical trials. Statistics in Medicine, 25, 233-245. doi:10.1002/sim. 2231
Bodner, T. E. (2008). What improves with increased missing data imputations? Structural Equation Modeling, 15, 651-675. doi:10.1080/ 10705510802339072
Chen, Q., \& Ibrahim, J. G. (2013). A note on the relationships between multiple imputation, maximum likelihood and fully Bayesian methods for missing responses in linear regression models. Statistics and Its Interface, 6, 315-324. doi:10.4310/SII.2013.v6.n3.a2
Cohen, J. E. (2004). Economic perceptions and executive approval in comparative perspective. Political Behavior, 26(1), 27-43.
Demirtas, H., Freels, S. A., \& Yucel, R. M. (2008). Plausibility of multivariate normality assumption when multiply imputing non-Gaussian continuous outcomes: A simulation assessment. Journal of Statistical Computation \& Simulation, 78(1), 69-84. doi:10.1080/1062936060090 3866
Demirtas, H., \& Hedeker, D. (2008). Imputing continuous data under some non-Gaussian distributions. Statistica Neerlandica, 62, 193-205. doi:10.1111/j.1467-9574.2007.00377.x
Draper, N. R., \& Nostrand, R. C. V. (1979). Ridge regression and JamesStein estimation: Review and comments. Technometrics, 21, 451-466. doi:10.1080/00401706.1979.10489815
Graham, J. W., Olchowski, A. E., \& Gilreath, T. D. (2007). How many imputations are really needed? Some practical clarifications of multiple imputation theory. Prevention Science, 8, 206-213. doi:10.1007/ s11121-007-0070-9
Granberg-Rademacker, J. S. (2007). A comparison of three approaches to handling incomplete state-level data. State Politics \& Policy Quarterly, 7(3), 325-338.
Hawkins, D. M., \& Wixley, R. A. J. (1986). A note on the transformation of chi-squared variables to normality. The American Statistician, 40, 296-298. doi:10.2307/2684608
He, Y., \& Raghunathan, T. E. (2012). Multiple imputation using multivariate gh transformations. Journal of Applied Statistics, 39, 2177-2198. doi:10.1080/02664763.2012.702268
Heitjan, D. F., \& Basu, S. (1996). Distinguishing "missing at random" and "missing completely at random". The American Statistician, 50, 207-213. doi:10.2307/2684656
Hogarty, K. Y., Hines, C. V., Kromrey, J. D., Ferron, J. M., \& Mumford, K. R. (2005). The quality of factor solutions in exploratory factor analysis: The influence of sample size, communality, and overdetermination. Educational and Psychological Measurement, 65, 202-226. doi:10.1177/ 0013164404267287
Hoogendoorn, A. (2009, November 18). Mulitple [sic] imputation in a very simple situation: Just two variables. Retrieved from http://www.mailarchive.com/impute@listserv.it.northwestern.edu/msg00455.html
Kelley, K., \& Maxwell, S. E. (2003). Sample size for multiple regression: Obtaining regression coefficients that are accurate, not simply significant. Psychological Methods, 8, 305-321. doi:10.1037/1082-989X. 8.3.305

Kim, J. K. (2004). Finite sample properties of multiple imputation estimators. The Annals of Statistics, 32, 766-783. doi:10.1214/009053 604000000175
Kunovich, S., \& Paxton, P. M. (2003). Women's political representation: The importance of ideology. Social Forces, 82(1), 87-113. doi:10.1353/sof.2003.0105
Lipsitz, S., Parzen, M., \& Zhao, L. P. (2002). A degrees-offreedom approximation in multiple imputation. Journal of Statistical Computation and Simulation, 72, 309-318. doi:10.1080/00949650212 848

Little, R. J. A. (1976). Inference about means from incomplete multivariate data. Biometrika, 63, 593-604. doi:10.1093/biomet/63.3.593
Little, R. J. A. (1988). Approximately calibrated small sample inference about means from bivariate normal data with missing values. Computational Statistics \& Data Analysis, 7, 161-178. doi:10.1016/ 0167-9473(88)90090-4
Little, R. J. A. (1992). Regression with missing X's: A review. Journal of the American Statistical Association, 87, 1227-1237.
Little, R. J. A., \& Rubin, D. B. (1989). The analysis of social science data with missing values. Sociological Methods \& Research, 18, 292-326. doi:10.1177/0049124189018002004
Little, R. J. A., \& Rubin, D. B. (2002). Statistical analysis with missing data. Hoboken, NJ: Wiley.
MacCallum, R. C., Widaman, K. F., Zhang, S., \& Hong, S. (1999). Sample size in factor analysis. Psychological Methods, 4, 84-99. doi:10.1037/ 1082-989X.4.1.84
Marszalek, J. M., Barber, C., Kohlhart, J., \& Holmes, C. B. (2011). Sample size in psychological research over the past 30 years. Perceptual and Motor Skills, 112, 331-348. doi:10.2466/03.11.PMS.112.2.331-348
Meng, X.-L. (1994). Multiple-imputation inferences with uncongenial sources of input. Statistical Science, 9, 538-558.
Morrison, D. F. (1973). A test for equality of means of correlated variates with missing data on one response. Biometrika, 60, 101-105. doi:10.1093/biomet/60.1.101
Muthén, L. K., \& Muthén, B. O. (2002). How to use a Monte Carlo study to decide on sample size and determine power. Structural Equation Modeling, 9, 599-620. doi:10.1207/S15328007SEM0904_8
Raghunathan, T. E., Lepkowski, J. M., Van Hoewyk, J., \& Solenberger, P. W. (2001). A multivariate technique for multiply imputing missing values using a sequence of regression models. Survey Methodology, 27(1), 85-95.
Reiter, J. P. (2007). Small-sample degrees of freedom for multi-component significance tests with multiple imputation for missing data. Biometrika, 94, 502-508. doi:10.1093/biomet/asm028
Rose, C., \& Smith, M. D. (2002). Mathematical statistics with Mathematica. New York, NY: Springer.
Rubin, D. B. (1987). Multiple imputation for nonresponse in surveys. New York, NY: Wiley.
Savalei, V., \& Bentler, P. M. (2009). A two-stage approach to missing data: Theory and application to auxiliary variables. Structural Equation Modeling, 16, 477-497. doi:10.1080/10705510903008238
Savalei, V., \& Rhemtulla, M. (2012). On obtaining estimates of the fraction of missing information from full information maximum likelihood. Structural Equation Modeling, 19, 477-494. doi:10.1080/ 10705511.2012 .687669

Schafer, J. L. (1997). Analysis of incomplete multivariate data. London, UK: Chapman \& Hall.
Seber, G. A. F., \& Lee, A. J. (2003). Linear regression analysis. Hoboken, NJ: Wiley-Interscience.
Tibshirani, R. (1996). Regression shrinkage and selection via the Lasso. Journal of the Royal Statistical Society, Series B (Methodological), 58, 267-288.
Van Buuren, S., \& Oudshoorn, K. (1999). Flexible multivariate imputation by MICE (TNO Report No. PG/VGZ/99.054). Leiden, The Netherlands: TNO Institute of Prevention and Health.
von Hippel, P. T. (2005). Teacher's corner: How many imputations are needed? A comment on Hershberger and Fisher (2003). Structural Equation Modeling, 12, 334-335. doi:10.1207/s15328007sem1202_8
von Hippel, P. T. (2007). Regression with missing Ys: An improved strategy for analyzing multiply imputed data. Sociological Methodology, 37, 83-117. doi:10.1111/j.1467-9531.2007.00180.x
von Hippel, P. T. (2009). How to impute interactions, squares, and other transformed variables. Sociological Methodology, 39, 265-291. doi:10.1111/j.1467-9531.2009.01215.x
von Hippel, P. T. (2013a). The bias and efficiency of incomplete-data estimators in small univariate normal samples. Sociological Methods \& Research, 42, 531-558. doi:10.1177/0049124113494582
von Hippel, P. T. (2013b). Should a normal imputation model be modified to impute skewed variables? Sociological Methods \& Research, 42(1), 105-138. doi:10.1177/0049124112464866
Wagstaff, D. A., \& Harel, O. (2011). A closer examination of three smallsample approximations to the multiple-imputation degrees of freedom. Stata Journal, 11, 403-419.
Wang, N., \& Robins, J. M. (1998). Large-sample theory for parametric multiple imputation procedures. Biometrika, 85, 935-948. doi:10.1093/ biomet/85.4.935
Wolf, E. J., Harrington, K. M., Clark, S. L., \& Miller, M. W. (2013). Sample size requirements for structural equation models: An evaluation of power, bias, and solution propriety. Educational and Psychological Measurement, 73, 913-934. doi:10.1177/0013164413495237
Yuan, K.-H., \& Bentler, P. M. (2007). Structural equation modeling. In C. R. Rao \& S. Sinharay (Eds.), Handbook of statistics: Vol. 26. Psychometrics (pp. 297-358). Boston, MA: North Holland.
Yuan, K.-H., \& Lu, L. (2008). SEM with missing data and unknown population distributions using two-stage ML: Theory and its application. Multivariate Behavioral Research, 43, 621-652. doi:10.1080/ 00273170802490699
Yuan, K.-H., Yang-Wallentin, F., \& Bentler, P. M. (2012). ML versus MI for missing data with violation of distribution conditions. Sociological Methods \& Research, 41, 598-629. doi:10.1177/0049124112460373

## APPENDIX BIAS CALCULATIONS

In this appendix we approximate the bias of $\hat{\sigma}_{Y, M L S I}^{2}$ and $\hat{\sigma}_{Y, P D S I}^{2}$.
Under PDSI or MLSI, the distribution of the partly observed, partly imputed variable $Y_{\text {obsSI }}$ can be written as

$$
\begin{aligned}
& Y_{o b s S I}=\alpha+M \Delta \hat{\alpha}_{Y . X}+\beta X+X M \Delta \hat{\beta}_{Y . X}+e_{o b s S I} \\
& \text { where } e_{o b s S I} \sim N\left(0, \sigma_{Y . X}^{2}+M \Delta \hat{\sigma}_{Y . X}^{2}\right)
\end{aligned}
$$

where $\Delta \hat{\alpha}_{Y . X}, \Delta \hat{\beta}_{Y . X}$, and $\Delta \hat{\sigma}_{Y . X}^{2}$ are the errors of the ML or PD estimates that are used in the imputation model. There are a lot of random variables in this equation, but the situation becomes more tractable if we accept the approximation that $X, M$, and $M X$ are fixed with covariance matrix $\Sigma_{M, X, M X}$.

Then the SI estimator

$$
\hat{\sigma}_{Y, S I}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(Y_{o b s S I, i}-\hat{\mu}_{Y, S I}\right)^{2}
$$

has the conditional expectation

$$
\begin{aligned}
& E\left(\hat{\sigma}_{Y, S I}^{2} \mid \hat{\alpha}_{Y . X}, \hat{\beta}_{Y . X}, \hat{\sigma}_{Y . X}^{2}\right)=V\left(Y_{o b s S I} \mid \hat{\alpha}_{Y . X}, \hat{\beta}_{Y . X}, \hat{\sigma}_{Y . X}^{2}\right) \\
& =\left[\begin{array}{c}
\Delta \hat{\alpha}_{Y . X} \\
\beta \\
\Delta \hat{\beta}_{Y . X}
\end{array}\right]^{T} \Sigma_{M, X, M X}\left[\begin{array}{c}
\Delta \hat{\alpha}_{Y . X} \\
\beta \\
\Delta \hat{\beta}_{Y . X}
\end{array}\right]+\sigma_{Y . X}^{2}+p \Delta \hat{\sigma}_{Y . X}^{2} .
\end{aligned}
$$

Breaking this into components, we see that the first component is a quadratic form whose expectation can be calculated using a matrix identity (Seber \& Lee, 2003, pp. 9-12),

$$
\begin{aligned}
& E\left(\left[\begin{array}{c}
\Delta \hat{\alpha}_{Y . X} \\
\beta \\
\Delta \hat{\beta}_{Y . X}
\end{array}\right]^{T} \Sigma_{M, X, X M}\left[\begin{array}{c}
\Delta \hat{\alpha}_{Y . X} \\
\beta \\
\Delta \hat{\beta}_{Y . X}
\end{array}\right]\right) \\
& =\operatorname{tr}\left(\Sigma_{M, X, X M} V\left[\begin{array}{c}
\Delta \hat{\alpha}_{Y . X} \\
\beta \\
\Delta \hat{\beta}_{Y . X}
\end{array}\right]\right)+\left[\begin{array}{l}
0 \\
\beta \\
0
\end{array}\right] \Sigma_{M, X, X M}\left[\begin{array}{l}
0 \\
\beta \\
0
\end{array}\right]^{T} \\
& =\operatorname{tr}\left(\Sigma_{M X M} \Sigma_{\hat{\alpha} \hat{\beta}_{Y . X}}\right)+\beta^{2} \sigma_{X}^{2}
\end{aligned}
$$

where $\Sigma_{M X M}$ is the covariance matrix of ( $M, X M$ ).
The remaining components have expectation

$$
\begin{aligned}
& \sigma_{Y . X}^{2}+p \Delta \hat{\sigma}_{Y . X}^{2}=\sigma_{Y . X}^{2}+p E\left(\Delta \hat{\sigma}_{Y . X}^{2}\right) \\
& \quad=\sigma_{Y . X}^{2}+p \operatorname{Bias}\left(\hat{\sigma}_{Y . X}^{2}\right)
\end{aligned}
$$

where $\operatorname{Bias}\left(\hat{\sigma}_{Y . X}^{2}\right)$ is the bias of $\hat{\sigma}_{Y . X}^{2}$ as an estimator of $\sigma_{Y . X}^{2}$.
Therefore the unconditional expectation of $\hat{\sigma}_{Y, S I}^{2}$ is

$$
E\left(\hat{\sigma}_{Y, S I}^{2}\right)=\operatorname{tr}\left(\Sigma_{M X M} \Sigma_{\hat{\alpha} \hat{\beta}_{Y . X}}\right)+\beta^{2} \sigma_{X}^{2}+\sigma_{Y . X}^{2}+p \operatorname{Bias}\left(\hat{\sigma}_{Y . X}^{2}\right)
$$

and the bias of $\hat{\sigma}_{Y, S I}^{2}$ as an estimator of $\sigma_{Y . X}^{2}$ is

$$
\begin{gathered}
\operatorname{Bias}\left(\hat{\sigma}_{Y, S I}^{2}\right)=E\left(\hat{\sigma}_{Y, S I}^{2}\right)-\sigma_{Y}^{2}=E\left(\hat{\sigma}_{Y, S I}^{2}\right)-\beta^{2} \sigma_{X}^{2}-\sigma_{Y . X}^{2} \\
=\operatorname{tr}\left(\Sigma_{M X M} \Sigma_{\hat{\alpha} \hat{\beta}_{Y . X}}\right)+\operatorname{pBias}\left(\hat{\sigma}_{Y . X, S I}^{2}\right)
\end{gathered}
$$

This justifies the expressions in Equations 15 and 20.


[^0]:    Correspondence should be addressed to Paul T. von Hippel, LBJ School of Public Affairs, University of Texas, 2315 Red River, Box Y, Austin, TX 78712. E-mail: paulvonhippel.utaustin@gmail.com

[^1]:    ${ }^{1}$ In our simulation we calculated variances and covariances from imputed data by dividing each sum of squares by its degrees of freedom. Other divisors are also possible.

[^2]:    ${ }^{\text {a }}$ With $v_{\text {prior }}=-2$, the expectation or standard error of certain estimates can be undefined. In this table, these undefined values show up as very large numbers.

[^3]:    ${ }^{2}$ The $t$ distribution is just an approximation here. The true small-sample distribution of PDMI estimates is not exactly $t$ (von Hippel, 2013a; Wagstaff \& Harel, 2011).

[^4]:    ${ }^{3}$ Again, the $t$ distribution is just an approximation here. The true smallsample distribution of ML estimates with incomplete data is not exactly $t$ (Little \& Rubin, 2002; von Hippel, 2013a).

[^5]:    ${ }^{4}$ More specifically, for the untransformed parameters we obtained point estimates and standard errors using the usual formulas. We then cube-root transformed the parameter estimates, and used the delta rule to transform the standard error. We calculated confidence intervals using the transformed parameter estimates and standard errors, then applied the inverse transformation (the cube) to the endpoints of the confidence intervals. Note that Little and Rubin (2002) suggested using a log transformation for a similar purpose. However, a log transformation does a relatively poor job of normalizing variance estimates (Hawkins \& Wixley, 1986), and produced poor (unnecessarily long) confidence intervals in our initial simulations.

