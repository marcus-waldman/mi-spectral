---
citekey: satorraEnsuringPositivenessScaled2010
item_type: article
authors: 'Satorra, Albert and Bentler, Peter M.'
year: 2010
title: 'Ensuring {Positiveness} of the {Scaled Difference Chi-square Test Statistic}'
venue: Psychometrika
volume: 75
issue: 2
pages: 243--248
doi: 10.1007/s11336-009-9135-y
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\satorra_ensuring_positiveness_scaled_2010.pdf'
pdf_sha256: ce306d73175d9e05eb1346df39179958f49e67c7c89b18b8bb0ea862934a4029
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T23:01:52Z
---
# ENSURING POSITIVENESS OF THE SCALED DIFFERENCE CHI-SQUARE TEST STATISTIC 

Albert Satorra<br>UNIVERSITAT POMPEU FABRA<br>Peter M. Bentler<br>UNIVERSITY OF CALIFORNIA


#### Abstract

A scaled difference test statistic $\tilde{T}_{d}$ that can be computed from standard software of structural equation models (SEM) by hand calculations was proposed in Satorra and Bentler (Psychometrika 66:507-514, 2001). The statistic $\tilde{T}_{d}$ is asymptotically equivalent to the scaled difference test statistic $\bar{T}_{d}$ introduced in Satorra (Innovations in Multivariate Statistical Analysis: A Festschrift for Heinz Neudecker, pp. 233-247, 2000), which requires more involved computations beyond standard output of SEM software. The test statistic $\tilde{T}_{d}$ has been widely used in practice, but in some applications it is negative due to negativity of its associated scaling correction. Using the implicit function theorem, this note develops an improved scaling correction leading to a new scaled difference statistic $\bar{T}_{d}$ that avoids negative chi-square values.


Key words: moment-structures, goodness-of-fit test, chi-square difference test statistic, chi-square distribution, nonnormality.

## 1. Introduction

Moment structure analysis is widely used in behavioral, social, and economic studies to analyze structural relations between variables, some of which may be latent; see, e.g., Bollen and Curran (2006), Grace (2006), Yuan and Bentler (2007), and references therein. In such analyses, it frequently happens that two nested models $M_{0}$ and $M_{1}$, are compared using estimation methods that are nonoptimal (asymptotically) given the distribution of the data; e.g., maximum likelihood (ML) estimation is used when the data are not multivariate normal. In those circumstances, the usual chi-square difference test $T_{d}=T_{0}-T_{1}$, based on the separate models' goodness of fit test statistics, is not $\chi^{2}$ distributed. A correction to $T_{d}$ by a scaling factor was proposed by Satorra (2000) and Satorra and Bentler (2001) to improve the chi-square approximation. The latter is the focus of this paper.

Satorra and Bentler's (2001) correction provided a simple procedure to obtain an approximate scaled chi-square statistic using hand calculations on regular output of structural equation modeling (SEM) analysis; it has the drawback, however, that a positive value for the scaling correction is not assured. The present paper develops a simple procedure by which a researcher can compute the exact scaling correction of difference test statistic based only on output from standard SEM programs.

[^0]
## 2. Setup and Notation

Throughout we adhere to the notation and results of Satorra and Bentler (2001). Let $\sigma$ and $s$ be $p$-dimensional vectors of population and sample moments, respectively, where $s$ tends in probability to $\sigma$ as sample size $n \rightarrow+\infty$. Let $\sqrt{n}(s-\sigma)$ be asymptotically normally distributed with a finite asymptotic variance matrix $\Gamma(p \times p)$. Consider the model $M_{0}: \sigma=\sigma(\theta)$ for the moment vector $\sigma$, where $\sigma(\cdot)$ is a twice-continuously differentiable vector-valued function of $\theta$, a $q$-dimensional parameter vector. Consider a discrepancy function $F=F(s, \sigma)$ in the sense of Browne (1984), and the estimator $\hat{\theta}$ based on $F$ or on an (asymptotically equivalent) weighted least squares (WLS) analysis with weight matrix $V=\frac{1}{2} \partial^{2} F(s, \sigma) / \partial \sigma \partial \sigma^{\prime}$ evaluated at $\sigma=s$.

Let $M_{0}: \sigma=\sigma^{\star}(\delta), a(\delta)=0$, and $M_{1}: \sigma=\sigma^{\star}(\delta)$ be two nested models for $\sigma$. Here, $\delta$ is a $(q+m)$-dimensional vector of parameters, and $\sigma^{\star}($.$) and a($.$) (an m$-valued function) are twicecontinuously differentiable vector-valued functions of $\delta \in \Theta_{1}$, a compact subset of $R^{q+m}$. Our interest is in the test of a null hypothesis $H_{0}: a(\delta)=0$ against the alternative $H_{1}: a(\delta) \neq 0$.

For the developments that follow, we require the Jacobian matrices $\Pi(p \times(q+m)):= \partial \sigma^{\star}(\delta) / \partial \delta^{\prime}$ and $A(m \times(q+m)):=\partial a(\delta) / \partial \delta^{\prime}$, which we assume to be regular at the true value of $\delta$, say $\delta_{0}$. We also assume that $A$ is of full row rank. By using the implicit function theorem, associated to $M_{0}$ (more specifically, to the restrictions $a(\delta)=0$ ), there exists (locally in a neighborhood of $\delta_{0}$ ) a one-to-one function $\delta=\delta(\theta)$ defined in an open and compact subset S of $R^{q}$, and a $\theta_{0}$ in the interior of S such that $\delta\left(\theta_{0}\right)=\delta_{0}$ and $\sigma(\delta(\theta))$ satisfies the model $M_{0}$. Let $H=\partial \delta(\theta) / \partial \theta^{\prime}((q+m) \times q)$ be the corresponding Jacobian matrix evaluated at $\theta_{0}$. Hence, by the chain rule of differentiation, $\Delta=\partial \sigma / \partial \theta^{\prime}=\left(\partial \sigma(\delta) / \partial \delta^{\prime}\right)\left(\partial \delta(\theta) / \partial \theta^{\prime}\right)=\Pi H$. Since $a(\delta(\theta))=0$, it holds that with $A$ evaluated at $\delta_{0}, A H=0$ with $r(A)+r(H)=q+m$, and $r$ (.) denoting the rank of a matrix. Thus, $H$ is an orthogonal complement of $A^{\prime}$. Let $P((q+m) \times(q+m)):=\Pi^{\prime} V \Pi$. Associated to $M_{1}$, the less restricted model $\sigma=\sigma^{\star}(\delta)$, the goodness-of-fit test statistic is $T_{1}=n F(s, \tilde{\sigma})$, where $\tilde{\sigma}$ is the fitted moment vector in model $M_{1}$ with associated degrees of freedom $r_{1}=r_{0}-m$ and scaling factor $c_{1}$ given by

$$
c_{1}:=\frac{1}{r_{1}} \operatorname{tr}\left\{U_{1} \Gamma\right\}=\frac{1}{r_{1}} \operatorname{tr}\{V \Gamma\}-\frac{1}{r_{1}} \operatorname{tr}\left\{P^{-1} \Pi^{\prime} V \Gamma V \Pi\right\},
$$

where

$$
U_{1}:=V-V \Pi P^{-1} \Pi^{\prime} V
$$

We refer to Satorra and Bentler (2001) for further details.

## 3. Scaling Correction for the Difference Test

When both models $M_{0}$ and $M_{1}$ are fitted, for example, by ML, then we can test the restriction $a(\delta)=0$, assuming $M_{1}$ holds, using the chi-square difference test statistic $T_{d}:=T_{0}-T_{1}$. Under the null hypothesis, we would like $T_{d}$ to have a $\chi^{2}$ distribution with degrees of freedom $m= r_{0}-r_{1}$. This is the restricted test of $M_{0}$ within $M_{1}$. For general distributions of the data, the asymptotic chi-square approximation may not hold. To improve on the chi-square approximation, Satorra (2000) gave explicit formulae that extend the scaling corrections proposed by Satorra and Bentler (1994) to the case of difference, Wald, and score types of test statistics. General expressions for those corrections were also put forward in Satorra (1989, p. 146). Specifically, for the test statistic $T_{d}$ we are considering, Satorra (2000, p. 241) proposed the following scaled test statistic:

$$
\bar{T}_{d}:=T_{d} / \hat{c}_{d}, \quad \text { where } c_{d}:=\frac{1}{m} \operatorname{tr}\left\{U_{d} \Gamma\right\}
$$

with

$$
U_{d}=V \Pi P^{-1} A^{\prime}\left(A P^{-1} A^{\prime}\right)^{-1} A P^{-1} \Pi^{\prime} V
$$

Here, $\hat{c}_{d}$ denotes $c_{d}$ after substituting consistent estimates of $V$ and $\Gamma$, and evaluating the Jacobians $A$ and $\Pi$ at the estimate $\hat{\delta}_{0}$ when fitting $M_{0}$ (or $M_{1}$ ). Since $\operatorname{tr}\left\{U_{d} \Gamma\right\}$ can be expressed as the trace of the product of two positive definite matrices, $\operatorname{tr}\left\{U_{d} \Gamma\right\}>0$, and thus $c_{d}>0$; the same for $\hat{c}_{d}>0$. Consequently, $\bar{T}_{d}$ is ensured to be a nonnegative number.

A practical problem with the statistic $\bar{T}_{d}$ is that it requires computations that are outside the standard output of current SEM programs. Furthermore, difference tests are usually hand computed from different modeling runs. Satorra and Bentler (2001) proposed a procedure to combine the estimates of the scaling corrections $c_{0}$ and $c_{1}$ associated to the chi-square goodness-of-fit test for the two fitted models $M_{0}$ and $M_{1}$ in order to compute a consistent estimate of the scaling correction $c_{d}$ for the difference test statistic. A modified (easy to compute) scaled test statistic $\tilde{T}_{d}$ with the same asymptotic distribution as $\bar{T}_{d}$ was proposed. Both statistics were shown to be asymptotically equivalent under a sequence of local alternatives (so they have the same asymptotic local power). Their procedure to compute $\tilde{T}_{d}$ is as follows (see Satorra and Bentler, 2001, p. 511).

1. Obtain the unscaled and scaled goodness-of-fit tests when fitting $M_{0}$ and $M_{1}$, respectively; that is, $T_{0}$ and $\bar{T}_{0}$ when fitting $M_{0}$, and $T_{1}$ and $\bar{T}_{1}$ when fitting $M_{1}$;
2. Compute the scaling corrections $\hat{c}_{0}=T_{0} / \bar{T}_{0}, \hat{c}_{1}=T_{1} / \bar{T}_{1}$, and the unscaled chi-square difference $T_{d}=T_{0}-T_{1}$ and its degrees of freedom $m=r_{0}-r_{1}$;
3. Compute the scaled difference test statistic as

$$
\tilde{T}_{d}:=T_{d} / \tilde{c}_{d} \quad \text { with } \tilde{c}_{d}=\left(r_{0} \hat{c}_{0}-r_{1} \hat{c}_{1}\right) / m
$$

Here, $r_{0}$ and $r_{1}$ are the respective degrees of freedom of the models $M_{0}$ and $M_{1}$.
The basis for computing the scaling correction for the difference test statistic is the following alternative expression for $U_{d}$ of (4) (see Satorra and Bentler, 2001, p. 510)

$$
U_{d}=U_{0}-U_{1}
$$

where $U_{1}$ is given in (2) and $U_{0}:=V-V \Pi H\left(H^{\prime} \Pi^{\prime} V \Pi H\right)^{-1} H^{\prime} \Pi^{\prime} V$. Since (5) implies

$$
m c_{d}=\operatorname{tr}\left\{U_{d} \Gamma\right\}=\operatorname{tr}\left\{\left(U_{0}-U_{1}\right) \Gamma\right\}=r_{0} c_{0}-r_{1} c_{1}
$$

it follows that $c_{d}=\left(r_{0} c_{0}-r_{1} c_{1}\right) / m$. This is the theoretical basis for Satorra and Bentler's (2001) proposal as given in steps $1-3$ above.

## 4. Problem with the Current Scaled Difference Test

For an arbitrary matrix $V>0$, (5) and (6) are exact equalities when the matrices $U_{d}, U_{0}$ and $U_{1}$ are evaluated at a common value $\delta$ (as, e.g., the fitted value under model $M_{0}$ or under $\left.M_{1}\right)$; however, they are just asymptotic equalities when $U_{d}, U_{0}$ and $U_{1}$ are evaluated at different estimates that converge to the same true value under the null hypothesis. Under Satorra and Bentler's (2001) proposal, $\tilde{c}_{d}$ evaluates $U_{0}$ and $U_{1}$ at the estimates $\hat{\delta}_{0}$ and $\hat{\delta}_{1}$, respectively. Since $\hat{\delta}_{1}$ will in general not satisfy the null model $M_{0}$ (i.e., it will not be of the form $\delta=\delta(\theta)$ for the function implied by the implicit function theorem), when it deviates highly from $M_{0}$, the estimated difference $\tilde{c}_{d}=\left(r_{0} \hat{c}_{0}-r_{1} \hat{c}_{1}\right) / m$ may turn out to be negative. This may happen in small samples, or when $M_{0}$ is highly incorrect; a result can be an improper value for $\tilde{T}_{d}$. Satorra and Bentler (2001, p. 511) warned on the possibility that an improper value of $\tilde{T}_{d}$ could arise.

In order to be sure to avoid a negative value for $\tilde{c}_{d}$, and hence $\tilde{T}_{d}$, currently one would need to resort to computing $\bar{T}_{d}$ using (3). Unfortunately, this is impractical or impossible for most applied researchers who only have access to standard SEM software.

Fortunately, as we show next, the exact value of $\bar{T}_{d}$ can also be obtained from the standard output of SEM software, using a new hand computation.

## 5. A New Scaled Test Statistic $\bar{T}_{d}$

Denote by $M_{10}$ the fit of model $M_{1}$ to a model setup with starting values taken as the final estimates obtained from model $M_{0}$, and with number of iterations set to 0 . Consider $\hat{c}_{1}{ }^{(10)}:= T_{1}{ }^{(10)} / \bar{T}_{1}{ }^{(10)}$, where $T_{1}{ }^{(10)}$ and $\bar{T}_{1}{ }^{(10)}$ are the standard unscaled and scaled test statistic of this additional run. Note that the estimate $\hat{c}_{1}{ }^{(10)}$ uses model $M_{1}$ but the matrices $\Pi$ and $A$ are now evaluated at $\hat{\delta}_{0}:=\delta(\hat{\theta})$, where $\hat{\theta}$ is the estimate under $M_{0}$. Since now all the matrices involved in (5) are evaluated at $\hat{\delta}_{0}$, the equality (6) holds exactly, and not only asymptotically, as when $U_{0}$ is evaluated at $\hat{\delta}_{0}$ and $U_{1}$ at $\hat{\delta}_{1}$. The scaling correction that is now computed is

$$
\hat{c}_{d}^{(10)}:=\left(r_{0} \hat{c}_{0}-r_{1} \hat{c}_{1}^{(10)}\right) / m
$$

which, in view of (6), is the scaling correction of (3) when $U_{d}$ is evaluated at the estimate $\hat{\delta}_{0}$ when fitting $M_{0}$, and thus it is a positive number. The new scaled difference statistic is thus defined as

$$
\bar{T}_{d}^{(10)}:=\left(T_{0}-T_{1}\right) / \hat{c}_{d}^{(10)}
$$

Clearly, $\bar{T}_{d}^{(10)}=\bar{T}_{d}$; that is, $\bar{T}_{d}^{(10)}$ coincides numerically with the scaled statistic (3) proposed in Satorra (2000).

## 6. An Illustration

We use these data just for illustrative purposes, and because they provide an example where the standard scaling correction fails to be positive. We use a latent variable model discussed for data by Bentler, Satorra, and Yuan (2009). The Bonett-Woodward-Randall (2002) test shows that these data have significant excess kurtosis indicative of nonnormality at a one-tail 0.05 level, so test statistics derived from ML estimation may not be appropriate and we do the scaling corrections.

The model considered is a structured means model, with the mean cigarette sales indirectly affecting the mean rates of the various cancers. The specified model is

$$
V_{j}=\lambda_{j} F+E_{j}, \quad j=2, \ldots, 5, \quad F=\beta V_{1}+D_{1}, \quad V_{1}=\mu+E_{1},
$$

where the $V_{j}$ 's denote observed variables; $F, D_{1}$, and $E_{j}$ are the common, residual common, and unique factors, respectively; $\lambda_{j}$ denotes a factor loading parameter, $\beta$ is the effect of cigarette smoking on the cancer factor, and $\mu$ is the mean parameter for rates of smoking. The units of measurement for the factor were tied to $V_{2}$, with $\lambda_{2}=1$. The following values for the ML and Satorra-Bentler (1994) (SB) scaled chi-square statistics are obtained

$$
T_{1}=107.398, \quad \bar{T}_{1}=65.3524, \quad r_{1}=9, \quad \hat{c}_{1}=1.6434
$$

along with the degrees of freedom $r_{1}$ and the scaling correction $\hat{c}_{1}$. The model does not fit, though for the sake of the illustration we are aiming for, this is not of concern to us.

Restricted Model $M_{0}$ The same model is now fitted with the added restriction that the error variances of the kidney and leukemia cancers, $E_{4}$ and $E_{5}$, are equal. This model gives the following statistics

$$
T_{0}=139.495, \quad \bar{T}_{0}=97.4034, \quad r_{0}=10, \quad \hat{c}_{0}=1.4322 .
$$

Difference Test Our main interest lies in testing the difference between $M_{0}$ and $M_{1}$, which we do with the chi-square difference test. The ML difference statistic is

$$
T_{d}=139.495-107.398=32.097
$$

which, with 1 degree of freedom ( $m$ ), rejects the null hypothesis that the error variances for E 4 and E5 are equal. Since the data are not normal, we compute the SB (2001) $\tilde{T}_{d}$ scaled difference statistic. This requires computing the scaling factor $\tilde{c}_{d}=\left(r_{0} \hat{c}_{0}-r_{1} \hat{c}_{1}\right) / m$ given by

$$
[10(1.4322)-9(1.6434)] / 1=14.322-14.7906=-0.4686
$$

The scaling factor $\tilde{c}_{d}$ is negative, so the SB difference test cannot be carried out; or if carried out, it results in an improper negative chi-square value.

New Scaled Difference Test As described above, to compute the scaled statistic $\bar{T}_{d}$, we implement (7) and (8). The output that is missing in the prior runs is $\bar{T}_{1}^{(10)}$ the value of the SB statistic obtained at the final parameter estimates for model $M_{0}$ when model $M_{1}$ is evaluated. This can be obtained by creating a model setup $M_{10}$ that contains the parameterization of $M_{1}$ with start values taken from the output of model $M_{0}$. Model $M_{10}$ is run with zero iterations, so that the parameter values do not change before output including test statistics is produced. ${ }^{1}$ The new result gives

$$
T_{1}^{(10)}=139.495, \quad \bar{T}_{1}^{(10)}=94.9551, \quad r_{1}=9, \quad \hat{c}^{(10)}=1.4691,
$$

where as expected, $T_{1}^{(10)}=T_{0}$ as reported above (i.e., the ML statistics are identical), and the value $\hat{c}^{10}$ is hand computed. As a result, we can compute

$$
\hat{c}_{d}^{(10)}=\left(r_{0} \hat{c}_{0}-r_{1} \hat{c}_{1}^{(10)}\right) / m=[(10)(1.4322)-(9)(1.4691)]=1.10,
$$

which, in contrast to the SB (2001) $\tilde{c}_{d}$ computations, is positive. Finally, we can compute the proposed new SB corrected chi-square statistic as

$$
\bar{T}_{d}=\bar{T}_{d}^{(10)}=\left(T_{0}-T_{1}\right) / \hat{c}_{d}^{(10)}=(139.495-107.398) / 1.10=29.179
$$

which can be referred to a $\chi_{1}^{2}$ variate for evaluation.

## 7. Discussion

The implicit function theorem was used to provide a theoretical basis for the development of a practical version of the computationally more difficult scaled difference statistic proposed by

[^1]Satorra (2000). ${ }^{2}$ The proposed method is only marginally more difficult to compute than that of Satorra and Bentler (2001) and solves the problem of an uninterpretable negative $\chi^{2}$ difference test that applied researchers have complained about for some time.

Like the method it is replacing, the proposed procedure applies to a general modeling setting. The vector of parameters $\sigma$ to be modeled may contain various types of moments: means, product-moments, frequencies (proportions), and so forth. Thus, this scaled difference test applies to methods such as factor analysis, simultaneous equations for continuous variables, loglinear multinomial parametric models, etc. It can easily be seen that the procedure applies also in the case where the matrix $\Gamma$ is singular, when the data is composed of various samples, as in multisample analysis, and to other estimation methods. It applies also to the case where the estimate of $\Gamma$ reflects the fact that we have intraclass correlation among observations, as in complex samples. Hence, this new statistic should be useful in a variety of applied modeling contexts. Simulation work will be needed to understand its virtues and limitations, relative to other alternatives, in such contexts.

## References

Bentler, P.M. (2008). EQS 6 structural equations program manual. Encino: Multivariate Software.
Bentler, P.M., Satorra, A., \& Yuan, K.-H. (2009). Smoking and cancers: case-robust analysis of a classic data set. Structural Equation Modeling, 16, 382-390.
Bollen, K.A., \& Curran, P.J. (2006). Latent curve models: a structural equation perspective. New York: Wiley.
Bonett, D.G., Woodward, J.A., \& Randall, R.L. (2002). Estimating p-values for Mardia's coefficients of multivariate skewness and kurtosis. Computational Statistics, 17, 117-122.
Browne, M.W. (1984). Asymptotically distribution-free methods for the analysis of covariance structures. British Journal of Mathematical and Statistical Psychology, 37, 62-83.
Grace, J.B. (2006). Structural equation modeling and natural systems. New York: Cambridge University Press.
Satorra, A. (1989). Alternative test criteria in covariance structure analysis: a unified approach. Psychometrika, 54, 131151.

Satorra, A. (2000). Scaled and adjusted restricted tests in multi-sample analysis of moment structures. In D.D.H. Heijmans \& D.S.G. Pollock, A. Satorra (Eds.), Innovations in multivariate statistical analysis: a festschrift for Heinz Neudecker (pp. 233-247). Dordrecht: Kluwer Academic.
Satorra, A., \& Bentler, P.M. (1994). Corrections to test statistics and standard errors in covariance structure analysis. In A. von Eye \& C.C. Clogg (Eds.) Latent variables analysis: applications for developmental research (pp. 399-419). Thousand Oaks: Sage.
Satorra, A., \& Bentler, P.M. (2001). A scaled difference chi-square test statistic for moment structure analysis. Psychometrika, 66, 507-514.
Satorra, A., \& Bentler, P.M. (2008). Ensuring positiveness of the scaled difference chi-square test statistic. Department of Statistics, UCLA Department of Statistics Preprint. http://repositories.cdlib.org/uclastat/papers/2008010905.
Yuan, K.-H., \& Bentler, P.M. (2007). Structural equation modeling. In C.R. Rao \& S. Sinharay (Eds.) Handbook of statistics 26: Psychometrics (pp. 297-358). Amsterdam: North-Holland.

Manuscript Received: 4 JUN 2008
Final Version Received: 25 MAY 2009
Published Online Date: 20 JUN 2009

[^2]
[^0]:    *Research supported by grants SEJ2006-13537 and PR2007-0221 from the Spanish Ministry of Science and Technology and by USPHS grants DA00017 and DA01070.

    Requests for reprints should be sent to Albert Satorra, Department of Economics and Business, Universitat Pompeu Fabra, Ramon Trias Fargas 25-27, Barcelona, Spain. E-mail: albert.satorra@upf.edu

[^1]:    ${ }^{1}$ For this particular example, the Appendix of Satorra and Bentler (2008) illustrates this procedure with EQS (Bentler, 2008). In the same reference, there is a second illustration with a larger degree of freedom.

[^2]:    ${ }^{2}$ Satorra (2000) provides also Monte Carlo evidence-on a specific model context and various sample sizes-of the superiority of the scaling correction over other alternatives such as the adjusted (mean and variance corrected) statistic.

