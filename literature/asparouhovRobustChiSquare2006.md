---
citekey: asparouhovRobustChiSquare2006
item_type: book
authors: 'Asparouhov, Tihomir and Muth\''en, Bengt'
year: 2006
title: 'Robust {Chi Square Difference Testing} with {Mean} and {Variance Adjusted Test Statistics}: {Webnote} 10'
issue: 10
doi: 'http://www.statmodel.com/examples/webnotes/webnote10.pdf'
series: 'Mplus {Web Notes}'
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\asparouhov_robust_chi_square_2006.pdf'
pdf_sha256: 94a8132cdd0d724dc2b4c6602786109b39abf1bfbf47a7056b5f03ab1a9a10af
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T23:15:22Z
---
# Robust Chi Square Difference Testing with Mean and Variance Adjusted Test Statistics 

Tihomir Asparouhov<br>Muthen \& Muthen<br>Bengt Muthen<br>UCLA<br>Mplus Web Notes: No. 10

May 26, 2006

## 1 Preliminaries

In this note we describe the DIFFTEST command implemented in Mplus for testing nested models with a mean and variance adjusted chi-square statistics. The DIFFTEST command is available for both the MLMV and the WLSMV estimators. In this note we will discuss the implementation only for the WLSMV estimator, but the MLMV implementation is similar. Suppose that there are two nested SEM models $H_{0}$ and $H_{1}$ where the parameters in each of the models are $\theta_{0}$ and $\theta_{1}$. Let $d_{i}$ be the number of parameters in model $H_{i}$. Let's assume that $H_{0}$ is nested in $H_{1}$. We want to test the hypothesis that $\theta_{1}=f\left(\theta_{0}\right)$. The WLSMV estimates are obtained by minimizing the fit functions

$$
\begin{aligned}
& T_{0}=\left(\sigma\left(\theta_{0}\right)-s\right)^{\prime} W^{-1}\left(\sigma\left(\theta_{0}\right)-s\right) \\
& T_{1}=\left(\sigma\left(\theta_{1}\right)-s\right)^{\prime} W^{-1}\left(\sigma\left(\theta_{1}\right)-s\right)
\end{aligned}
$$

where $s$ represents all sample statistics in the unrestricted model and $\sigma\left(\theta_{i}\right)$ are the $H_{i}$ model estimated sample statistics, see Muthen (1998-2004). Let $\Gamma$ be an estimate of the variance covariance matrix of the sample statistics $s$. Define also the following matrices

$$
\begin{gathered}
\frac{\partial \sigma\left(\theta_{i}\right)}{\partial \theta_{i}}=\Delta_{i} \\
P_{i}=\Delta_{i}^{\prime} W^{-1} \Delta_{i} \\
V_{i}=P_{i}^{-1} \Delta_{i}^{\prime} W^{-1} \Gamma W^{-1} \Delta_{i} P_{i}^{-1} .
\end{gathered}
$$

The matrix $V_{i}$ is actually the asymptotic variance covariance matrix for the parameter estimates $\theta_{i}$. Let also

$$
H=\frac{\partial \theta_{1}}{\partial \theta_{0}}
$$

To test the hypothesis $\theta_{1}=f\left(\theta_{0}\right)$ we will use the test statistic $T=T_{0}-T_{1}$. The mean and variance adjustment for $T$ is derived by the last two formulas in Section 3 of Satorra (2000), and the second to last formula on page 6 in Satorra-Bentler (1999)

$$
\bar{T}=\frac{d}{\operatorname{tr}(M)} T
$$

where

$$
d=d_{1}-d_{0}
$$

$$
M=W^{-1} \Delta_{1}^{\prime}\left(p_{1}^{-1}-H\left(H^{\prime} P H\right)^{-1} H^{\prime}\right) \Delta_{1} W^{-1} \Gamma .
$$

The distribution of $\bar{T}$ is approximately a chi-square distribution with $d^{\prime}$ degrees of freedom where $d^{\prime}$ is the integer nearest to

$$
\frac{(\operatorname{tr}(M))^{2}}{\operatorname{tr}\left(M^{2}\right)}
$$

Thus we estimate the degrees of freedom just as this is done for the test of fit with the WLSMV estimator.

## 2 Alternative Formula

In this section we derive an alternative formula for computing the mean and variance adjustment for $T$. Let

$$
M_{1}=\left(P_{1}-P_{1} H\left(H^{\prime} P_{1} H\right)^{-1} H^{\prime} P_{1}\right) V_{1}
$$

We will show below that $\operatorname{tr}\left(M_{1}\right)=\operatorname{tr}(M)$ and $\operatorname{tr}\left(M_{1}^{2}\right)=\operatorname{tr}\left(M^{2}\right)$. Thus in equations (7) and (10) we can use the matrix $M_{1}$ instead of the matrix $M$. The matrix $M_{1}$ has the advantage that it doesn't depend on the large matrix $\Gamma$.

It is easy to see that $M=N_{1} N_{2}$ and $M_{1}=N_{2} N_{1}$, where

$$
\begin{gathered}
N_{1}=W^{-1} \Delta_{1} P_{1}^{-1} \\
N_{2}=\left(P_{1}-P_{1} H\left(H^{\prime} P_{1} H\right)^{-1} H^{\prime} P_{1}\right) W^{-1} \Delta_{1}^{\prime} P_{1}^{-1} \Gamma .
\end{gathered}
$$

The commutative property of the trace now implies that $\operatorname{tr}\left(M_{1}\right)=\operatorname{tr}(M)$ and $\operatorname{tr}\left(M_{1}^{2}\right)=\operatorname{tr}\left(M^{2}\right)$.

Mplus implementation computes $\operatorname{tr}\left(M_{1}\right)$ and $\operatorname{tr}\left(M_{1}^{2}\right)$ to obtain the mean and variance adjustment for $T$. First Mplus estimates the $H_{1}$ model and store the matrices $\Delta_{1}, P_{1}$ and $V_{1}$ in the DIFFTEST file. During the $H_{0}$ model estimation these matrices are used together with the matrix $H$ to obtain $M_{1}$. The DIFFTEST file also contains also $T_{1}, d_{1}$, the number of sample statistics, and the number of groups in the analysis. These numbers are at the top of the file.

## 3 Simulation Study

A key application of the DIFFTEST construction is the test of measurement invariance of categorical outcomes as described on page 346, Muthen and Muthen (1998-2006). We use a simple two-group factor analysis model with 6 polytomous indicators with 3 categories each. Let $u_{i j g}$ be the $j$-th observed indicator for the $i$-th individual in group $g$ and $u_{i j g}^{*}$ be the underlying normal variable. The model is described by

$$
u_{i j g}^{*}=\Delta_{j g}\left(\lambda_{j g} f_{i g}+\varepsilon_{i j g}\right) .
$$

where $f_{i g}$ is the factor with mean $\mu_{g}$ and variance $\psi_{g}$ and $\varepsilon_{i j g}$ are normal residuals with variance $\theta_{j g}$. The above parameters are constrained by the following equation which standardizes the variance of $u_{i j g}^{*}$ to 1

$$
\Delta_{j g}=1 / \sqrt{\lambda_{j g}^{2} \psi_{g}+\theta_{j g}}
$$

The threshold parameters are denoted by $\tau_{j k g}$ where $k=1$ or 2 and indicates the first and the second threshold. The thresholds are used to cut $u_{i j g}^{*}$ into categories. We generate the data with the following set of parameters: $\tau_{j 1 g}= -1, \tau_{j 1 g}=\lambda_{j g}=\Delta_{j g}=1, \mu_{g}=0, \psi_{g}=0.49, \theta_{1}=.51$ and $\theta_{2}=3.51$.

In the estimation we use the delta parameterizations, thus allowing the $\Delta_{j g}$ parameter to be free while $\theta_{j g}$ to be a dependent parameter constraint by equation (12). We test the following two models.
$H_{0}$ model: Thresholds and factor loadings constrained to be equal across groups; scale factors fixed to one in one group and free in the others; factor means fixed to zero in one group and free in the others (the Mplus default). This model has 26 parameters and is correct for these data with $\Delta_{2}=0.5$.
$H_{1}$ model: Thresholds and factor loadings free across groups; scale factors fixed to one in all groups; factor means fixed to zero in all groups. This model has 36 parameters and is nested above the $H_{0}$ model.

We use DIFFTEST to test $H_{0}$ against $H_{1}$ in a simulation study with 500 replications. We performed the simulation study with two different sample sizes 1100 ( 500 in group 1 and 600 in group 2) and 2200 ( 1000 in group 1 and 1200 in group 2). The result of the simulation study is that the for sample size 1100 the $H_{0}$ was rejected $6 \%$ of the time and for sample size 2200 the
$H_{0}$ model was rejected $4.4 \%$ of the time. Both rates are sufficiently close to the nominal rejection rate of $5 \%$ and thus we conclude that the DIFFTEST as implemented in Mplus performs correctly.

## 4 References

Muthen, B.O. (1998-2004). Mplus Technical Appendices. Los Angeles, CA: Muthen \& Muthen.
http://statmodel.com/download/techappen.pdf

Muthen, L.K. and Muthen, B.O. (1998-2006). Mplus Users Guide. Fourth Edition. Los Angeles, CA: Muthen \& Muthen
http://statmodel.com/download/usersguide/Mplus\ Users\ Guide\ v41.pdf
Satorra, A. (2000). Scaled and adjusted restricted tests in multi-sample analysis of moment structures. In Innovations in Multivariate Statistical Analysis: A Festschrift for Heinz Neudecker. Heijmans, D.D.H., Pollock, D.S.G. and Satorra, A. (edts.), pp. 233-247, Kluwer Academic Publishers, Dordrecht.
http://www.econ.upf.edu/docs/papers/downloads/395.pdf

Satorra, A. and Bentler, P. (1999) A Scaled Difference Chi-square Test Statistic for Moment Structure Analysis. Technical Report University of California, Los Angeles.
http://preprints.stat.ucla.edu/260/chisquare.pdf

