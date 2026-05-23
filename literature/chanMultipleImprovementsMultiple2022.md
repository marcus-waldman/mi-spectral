---
citekey: chanMultipleImprovementsMultiple2022
item_type: article
authors: 'Chan, Kin Wai and Meng, Xiao-Li'
year: 2022
title: 'Multiple {Improvements} of {Multiple Imputation Likelihood Ratio Tests}'
venue: Statistica Sinica
doi: 10.5705/ss.202019.0314
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\chan_multiple_improvements_multiple_2022.pdf'
pdf_sha256: d433adb7f785f43ce8df26a39d7870cecbfd2591a21a8c964b5889d61b8c33d6
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-23T01:38:31Z
---
# MULTIPLE IMPROVEMENTS OF MULTIPLE IMPUTATION LIKELIHOOD RATIO TESTS 

Kin Wai Chan ${ }^{1}$ and Xiao-Li Meng ${ }^{2}$<br>Department of Statistics, The Chinese University of Hong Kong ${ }^{1}$<br>Department of Statistics, Harvard University ${ }^{2}$


#### Abstract

Multiple imputation (MI) inference handles missing data by imputing the missing values $m$ times, and then combining the results from the $m$ completedata analyses. However, the existing method for combining likelihood ratio tests (LRTs) has multiple defects: (i) the combined test statistic can be negative, but its null distribution is approximated by an $F$-distribution; (ii) it is not invariant to re-parametrization; (iii) it fails to ensure monotonic power owing to its use of an inconsistent estimator of the fraction of missing information (FMI) under the alternative hypothesis; and (iv) it requires nontrivial access to the LRT statistic as a function of parameters instead of data sets. We show, using both theoretical derivations and empirical investigations, that essentially all of these problems can be straightforwardly addressed if we are willing to perform an additional LRT by stacking the $m$ completed data sets as one big completed data set. This enables users to implement the MI LRT without modifying the complete-data procedure. A particularly intriguing finding is that the FMI can be estimated consistently by an LRT statistic for testing whether the $m$ completed data sets can be regarded effectively as samples coming from a common model. Practical guidelines are provided based on an extensive comparison of existing MI tests. Issues related to nuisance parameters are also discussed.


Key words and phrases: Fraction of missing information, missing data, invariant test, monotonic power, robust estimation.

## 1. Historical Successes and Failures

### 1.1 The Need for Multiple Imputation Likelihood-Ratio Tests

Missing-data problems are ubiquitous in practice, to the extent that the absence of any missingness is often a strong indication that the data have been pre-processed or manipulated in some way (e.g., Blocker and Meng, 2013). Multiple imputation (MI) Rubin, 1978, 2004) has been a preferred method, especially by those who are ill-equipped to handle missingness on their own, owing to a lack of information or skills or resources. MI relies on the data collector (e.g., a census bureau) building a reliable imputation model to fill in the missing data $m(\geqslant 2)$ times. In this way, users can apply their preferred software or procedures designed for complete data, and do so $m$ times. MI inference is then performed by appropriately combining these $m$
complete-data results. Note that in a typical analysis of public MI data, the analyst has no control over or understanding of how the imputation was done, including the choice of the model and $m$, which is often small in reality (e.g., $3 \leqslant m \leqslant 10$ ). The analyst's job is to analyze the given $m$ completed data sets as appropriately as possible, but only using complete-data procedures or software routines.

Although MI was designed initially for public-use data sets, over the years, it has become a method of choice in general, because it separates handling the missingness from the analysis (e.g., Tu et al., 1993; Rubin, 1996, 2004; Schafer, 1999; King et al., 2001; Peugh and Enders, 2004; Kenward and Carpenter, 2007. Rose and Fraser, 2008, Holan et al., 2010, Kim and Yang, 2017). Software routines for performing MI are now available in R (Su et al., 2011), Stata (Royston and White, 2011), SAS (Berglund and Heeringa, 2014), and SPSS; see Harel and Zhou (2007) and Horton and Kleinman (2007) for summaries.

This convenient separation, however, creates an issue of uncongeniality, that is, an incompatibility between the imputation model and the subsequent analysis procedures (Meng, 1994a). This issue is examined in detail by Xie and Meng (2017), who show that uncongeniality is easiest to deal with when the imputer's model is more saturated than the user's model/procedure, and when the user is conducting an efficient analysis, such as a likelihood inference. Therefore, this study focuses on conducting MI likelihood ratio tests (LRTs), assuming the imputation model is sufficiently saturated to render the common assumptions made in the literature about conducting LRTs with MI valid.

Like many hypothesis testing procedures in common practice, the exact null distributions of various MI test statistics, LRTs or not, are intractable. This intractability is not computational, but rather statistical, owing to the well-known issue of a nuisance parameter, that is, the lack of a pivotal quantity, as highlighted by the Behrens-Fisher problem (Wallace, 1980). Indeed, the nuisance parameter in the MI context is the so-called "fraction of missing information" (FMI), which is determined by the ratio of the between-imputation variance to the within-imputation variance (and its multi-variate counterparts). Hence, the challenge we face is almost identical to the one faced by the Behrens-Fisher problem, as shown in Meng (1994b). Currently the most successful strategy has been to reduce the number of nuisance parameters to one by assuming an equal fraction of missing information (EFMI), a strategy we follow as well because our simulation study indicates that it achieves a better compromise between type-I and type-II errors than other strategies we (and others) have tried.

An added challenge in the MI context is that the user's complete-data procedures can be very restrictive. Please update as follows: What is available to the user could vary from the entire likelihood function to point estimators (such as the MLE and Fisher information) and to a single $p$-value. Therefore, there have been a
variety of procedures proposed in the literature, depending on what quantities we assume the user has access to, as we review shortly.

Among them, a promising idea is to directly combine LRT statistics. However, the current execution of this idea (Meng and Rubin, 1992) relies too heavily on the asymptotic equivalence (in terms of the data size, not the number of imputations, $m$ ) between the LRT and Wald test under the null. Its asymptotic validity, unfortunately, does not protect it from quick deterioration for small data sizes, such as delivering a negative " $F$ test statistic" or FMI. Worst of all, the test can have essentially zero power because the estimator of the FMI can be badly inconsistent under some alternative hypotheses. The combining rule of Meng and Rubin (1992) also requires access to the LRT as a function of parameter values, not just as a function of the data. The former is often unavailable from standard software packages. This defective MI LRT, however, has been adopted by textbooks (e.g., van Buuren S, 2012, Kim and Shao, 2013) and popular software, for example, the function pool.compare in the R package mice van Buuren and Groothuis-Oudshoorn, 2011), the function testModels in the R package mitml (Grund et al., 2017), and the function milrtest (Medeiros, 2008) in the Stata module mim (Carlin et al., 2008).

To minimize the negative impact of this defective LRT test, this study derives MI LRTs that are free of these defects, as detailed in Section 1.5. We achieve this mainly by switching the order of two main operators in the combining rule of Meng and Rubin (1992): we maximize the average of the $m$ log-likelihoods instead of averaging their maximizers. This switch, guided by the likelihood principle, renders positivity, invariance, and monotonic power. Other judicious uses of the likelihood functions permit us to overcome the remaining defects.

### 1.2 Summary of the Major Findings

Our major contributions are four-fold:

- In terms of statistical principles, we propose switching the order of two operations, namely maximization and averaging, in the existing MI LRT statistic, as suggested by the likelihood principle. This operation retrieves the nonnegativity and invariance to the re-parametrization of the MI statistic.
- In terms of theoretical properties, a new estimator of the fraction of missing information is proposed. It is consistent, regardless of the validity of the null hypothesis, so that the proposed test is monotonically powerful with respect to the discrepancy between the null and alternative hypotheses.
- In terms of computational properties, the proposed test only requires that users have a standard subroutine for performing a complete-data LRT. Thus,
unlike the existing MI LRT, users do not need to modify the subroutine in order to evaluate the likelihood function at arbitrary parameter values.
- In terms of practical impact, the proposed test can be implemented easily to replace the flawed MI LRT procedures in the aforementioned software packages and beyond. It immediately resolves the issue of returning a negative $F$-test value. In addition, the power loss due to the flaws in the MI LRT procedure can be retrieved.

The remainder of Section 1 provides background and notation. Section 2 discusses the defects of the existing MI LRT and our remedies. Section 3 investigates the computational requirements, including theoretical considerations and comparisons. In particular, Algorithm 1 of Section 3.1 computes our most recommended test. Section 4 provides empirical evidence. Section 5 concludes the paper. Appendices A and B provide additional investigations, real-life data examples, and proofs.

### 1.3 Notation and Complete-Data Tests

Let $X_{\text {obs }}$ and $X_{\text {mis }}$ be, respectively, the observed and missing parts of an intended complete data set $X=X_{\text {com }}=\left\{X_{\text {obs }}, X_{\text {mis }}\right\}$ consisting of $n$ observations. Denote the sampling model - probability or density, depending on the data type - of $X$ by $f(\cdot \mid \psi)$, where $\psi \in \Psi \subseteq \mathbb{R}^{h}$ is a vector of parameters. Suppose that we are interested in inferring $\theta=\theta(\psi) \in \Theta \subseteq \mathbb{R}^{k}$, which is expressed as a function of $\psi$. This definition of $\theta$ is very general. For example, $\theta$ can be a sub-vector of $\psi=\left(\theta^{\boldsymbol{\top}}, \eta^{\boldsymbol{\top}}\right)^{\boldsymbol{\top}}$, or a transformation (not necessarily one-to-one) of $\psi$; see Section 4.4 of Serfling (2001) and Section 6.4.2 of Shao (1998).

The goal is to test $H_{0}: \theta=\theta_{0}$ when only $X_{\text {obs }}$ is available, where $\theta_{0}$ is a specified vector. For example, if $H_{0}$ puts a $k$-dimensional restriction $R(\psi)=\mathbf{0}$ on the model parameter $\psi$, then $\theta=R(\psi)$ and $\theta_{0}=\mathbf{0}$. For simplicity, we focus on a two-sided alternative, but our approach adapts to general LRTs. Here, we assume $X_{\text {obs }}$ is rich enough that the missing data mechanism is ignorable Rubin, 1976), or it has been properly incorporated by the imputer, who may have access to additional confidential data.

Let $\hat{\theta}=\hat{\theta}(X), \hat{\psi}=\hat{\psi}(X)$, and $\hat{\psi}_{0}=\hat{\psi}_{0}(X)$ be the complete-data MLE of $\theta$, complete-data MLE of $\psi$, and $H_{0}$-constrained complete-data MLE of $\psi$, respectively. Furthermore, let $U=U_{\theta}=U_{\theta}(X)$ and $U_{\psi}=U_{\psi}(X)$ be efficient estimators of $\operatorname{Var}(\widehat{\theta})$ and $\operatorname{Var}(\widehat{\psi})$, respectively, for example, the inverse of the observed Fisher information. Common test statistics for $H_{0}$ include the Wald statistic
$D_{\mathrm{W}}=d_{\mathrm{W}}(\hat{\theta}, U) / k$ and the LRT statistic $D_{\mathrm{L}}=d_{\mathrm{L}}\left(\hat{\psi}_{0}, \hat{\psi} \mid X\right) / k$, where

$$
d_{\mathrm{W}}(\hat{\theta}, U)=\left(\hat{\theta}-\theta_{0}\right)^{\top} U^{-1}\left(\hat{\theta}-\theta_{0}\right), \quad d_{\mathrm{L}}\left(\hat{\psi}_{0}, \hat{\psi} \mid X\right)=2 \log \frac{f(X \mid \hat{\psi})}{f\left(X \mid \hat{\psi}_{0}\right)}
$$

Under regularity conditions, such as those in Section 4.2.2 and Section 4.4.2 of Serfling (2001), we have the following classical results.

Property 1. Under $H_{0}$, (i) $D_{\mathrm{W}} \Rightarrow \chi_{k}^{2} / k$ and $D_{\mathrm{L}} \Rightarrow \chi_{k}^{2} / k$; and (ii) $n\left(D_{\mathrm{W}}-\right. \left.D_{\mathrm{L}}\right) \xrightarrow{\mathrm{pr}} 0$ as $n \rightarrow \infty$, where " ⇒ " and $\xrightarrow{\mathrm{pr}}$ " denote convergence in distribution and in probability, respectively.

Testing $H_{0}$ based on $X_{\text {obs }}$ is more involved. For MI, let $X^{(\ell)}=\left\{X_{\text {obs }}, X_{\text {mis }}^{(\ell)}\right\}$, for $\ell=1, \ldots, m$, be the $m$ completed data sets, where $X_{\text {mis }}^{(\ell)}$ are drawn from a proper imputation model (Rubin, 2004). We then carry out a complete-data estimation or testing procedure on $X^{(\ell)}$, for $\ell=1, \ldots, m$, resulting in a set of $m$ quantities. The so-called MI inference combines them to obtain a single answer. Note that the setting of MI is such that the user is unable or unwilling to carry out the test based directly on the observed data $X_{\text {obs }}$.

### 1.4 MI Wald Test and Fraction of Missing Information

Let $d_{\mathrm{W}}^{(\ell)}=d_{\mathrm{W}}\left(\hat{\theta}^{(\ell)}, U^{(\ell)}\right), \hat{\theta}^{(\ell)}=\hat{\theta}\left(X^{(\ell)}\right)$, and $U^{(\ell)}=U\left(X^{(\ell)}\right)$ be the imputed counterparts of $d_{\mathrm{W}}(\hat{\theta}, U), \hat{\theta}$, and $U$, respectively, for each $\ell$. In addition, let

$$
\bar{d}_{\mathrm{W}}=\frac{1}{m} \sum_{\ell=1}^{m} d_{\mathrm{W}}^{(\ell)}, \quad \bar{\theta}=\frac{1}{m} \sum_{\ell=1}^{m} \hat{\theta}^{(\ell)}, \quad \bar{U}=\frac{1}{m} \sum_{\ell=1}^{m} U^{(\ell)}
$$

Under congeniality (Meng, 1994a), one can show that asymptotically Rubin and Schenker, 1986) $\operatorname{Var}(\bar{\theta})$ can be consistently estimated by

$$
T=\bar{U}+(1+1 / m) B, \quad \text { where } \quad B=\frac{1}{m-1} \sum_{\ell=1}^{m}\left(\hat{\theta}^{(\ell)}-\bar{\theta}\right)\left(\hat{\theta}^{(\ell)}-\bar{\theta}\right)^{\top}
$$

is known as the between-imputation variance, in contrast to $\bar{U}$ in (1.1), which measures the within-imputation variance. Intriguingly, $2 T$ serves as a universal (estimated) upper bound of $\operatorname{Var}(\bar{\theta})$ under uncongeniality (Xie and Meng, 2017). Under regularity conditions, we have that, as $m, n \rightarrow \infty$,

$$
n\left(\bar{U}-\mathscr{U}_{\theta}\right) \xrightarrow{\mathrm{pr}} \mathbf{0}, \quad n\left(T-\mathscr{T}_{\theta}\right) \xrightarrow{\mathrm{pr}} \mathbf{0}, \quad n\left(B-\mathscr{B}_{\theta}\right) \xrightarrow{\mathrm{pr}} \mathbf{0}
$$

for some deterministic matrices $\mathscr{U}_{\theta}, \mathscr{T}_{\theta}$, and $\mathscr{B}_{\theta}=\mathscr{T}_{\theta}-\mathscr{U}_{\theta}$, where $\mathbf{0}$ denotes a matrix of zeros, and the subscript $\theta$ highlights that these matrices are for estimating
$\theta$, because there are also corresponding $\mathscr{T}_{\psi}, \mathscr{B}_{\psi}$, and $\mathscr{U}_{\psi}$ for the entire parameter $\psi$. Similar to $\bar{U}, T$, and $B$, we define $\bar{U}_{\psi}, T_{\psi}$, and $B_{\psi}$ for the parameter $\psi$. If $\widehat{\theta}_{\text {com }}$ and $\widehat{\theta}_{\text {obs }}$ are the MLEs of $\theta$ based on $X_{\text {com }}$ and $X_{\text {obs }}$ (under congeniality), respectively, then $\mathscr{U}_{\theta} \bumpeq \operatorname{Var}\left(\widehat{\theta}_{\text {com }}\right)$ and $\mathscr{T}_{\theta} \bumpeq \operatorname{Var}\left(\widehat{\theta}_{\text {obs }}\right)$ as $n \rightarrow \infty$, where $A_{n} \bumpeq B_{n}$ means that $A_{n}-B_{n}=o_{p}\left\{\min \left(A_{n}, B_{n}\right)\right\}$. Note that the relation $A_{n} \bumpeq B_{n}$ means that the difference between $A_{n}$ and $B_{n}$ is of a smaller order than $A_{n}$ or $B_{n}$, when both $A_{n} \geqslant 0$ and $B_{n} \geqslant 0$ approach zero. This notation (or its variants) is also used in, for example, Meng and Rubin (1992), Li et al. (1991b), and Kim and Shao (2013).

The straightforward MI Wald test $D_{\mathrm{W}}(T)=d_{\mathrm{W}}(\bar{\theta}, T) / k$ is not practical because $T$ is singular when $m<k$ (usually $3 \leqslant m \leqslant 10$ ). Even when it is not singular, it is usually not a very stable estimator of $\mathscr{T}_{\theta}$ because $m$ is small. To circumvent this problem, Rubin (1978) adopted the following assumption of an EFMI.

Assumption 1 (EFMI of $\theta$ ). There is $\mathcal{r} \geqslant 0$ such that $\mathscr{T}_{\theta}=(1+\mathcal{r}) \mathscr{U}_{\theta}$.
EFMI is a strong assumption, implying that the missing data have caused an equal loss of information for estimating every component of $\theta$. However, as we shall see shortly, adopting this assumption for the purpose of hypothesis testing is essentially the same as summarizing the impact of (at least) $k$ nuisance parameters due to FMI by a single nuisance parameter, this is, the average FMI across different components. How well this reduction strategy works has a greater effect on the power of the test than on its validity, as long as we can construct an approximate null distribution that is more robust to the EFMI assumption. The issue of power turns out to be a rather tricky one, because without the reduction strategy, we also lose power when $m / k$ is small or even modest. This is because we simply do not have enough degrees of freedom to estimate all the nuisance parameters well or at all. We illustrate this point in Section 4.2. (To clarify some confusion in literature, $\boldsymbol{r}$ in Assumption 1 is the odds of the missing information, not the FMI, which is $f=r /(1+r)$.) We also denote $r_{m}=(1+1 / m) r$ as the finite- $m$ adjusted value of r.

Under EFMI, Rubin (2004) replaced $T$ by $\left(1+\widetilde{r}_{\mathrm{W}}^{\prime}\right) \bar{U}$, where

$$
\tilde{r}_{\mathrm{W}}^{\prime}=\frac{(m+1)}{k(m-1)}\left(\bar{d}_{\mathrm{W}}^{\prime}-\widetilde{d}_{\mathrm{W}}^{\prime}\right), \quad \bar{d}_{\mathrm{W}}^{\prime}=\frac{1}{m} \sum_{\ell=1}^{m} d_{\mathrm{W}}\left(\hat{\theta}^{(\ell)}, \bar{U}\right)
$$

$\widetilde{d}_{\mathrm{W}}^{\prime}=d_{\mathrm{W}}(\bar{\theta}, \bar{U})$, and the prime "$"$ " indicates that $\bar{U}$ is used instead of individual $\left\{U^{(\ell)}\right\}_{\ell=1}^{m}$. Then, a simple MI Wald test statistic Rubin, 2004) is

$$
\widetilde{D}_{\mathrm{W}}^{\prime}=\frac{\widetilde{d}_{\mathrm{W}}^{\prime}}{k\left(1+\widetilde{r}_{\mathrm{W}}^{\prime}\right)}
$$

The intuition behind (1.3)-(1.4) is important because it forms the building blocks for virtually all the subsequent developments. The "obvious" Wald statistic $\widetilde{d}_{\mathrm{W}}^{\prime} / k$ is too large (compared to the usual $\chi_{k}^{2} / k$ ), because it fails to take into account the missing information. The $\left(1+\widetilde{r}_{\mathrm{W}}^{\prime}\right)$ factor attempts to correct this, with the amount of correction determined by the amount of between-imputation variance relative to the within-imputation variance. This relative amount can be estimated by contrasting the average of individual Wald statistics and the Wald statistic based on an average of individual estimates, as in (1.3). Using the difference between the "average of functions" and the "function of average," namely,

$$
\operatorname{Ave}\{G(x)\}-G(\operatorname{Ave}\{x\})
$$

is a common practice, for example, $G(x)=x^{2}$ for variance; see Meng (2002).
Because the exact null distribution of $\widetilde{D}_{\mathrm{W}}^{\prime}$ is intractable, Li et al. (1991b) proposed approximating it by $F_{k, \widetilde{\mathrm{~d}}\left(\widetilde{r}_{\mathrm{w}}^{\prime}, k\right)}$, the $F$ distribution with degrees of freedom $k$ and $\widetilde{\mathrm{df}}\left(\widetilde{r}_{\mathrm{W}}^{\prime}, k\right)$, where, denoting $K_{m}=k(m-1)$,

$$
\widetilde{\operatorname{df}}\left(r_{m}, k\right)= \begin{cases}4+\left(K_{m}-4\right)\left\{1+\left(1-2 / K_{m}\right) / r_{m}\right\}^{2}, & \text { if } K_{m}>4 \\ (m-1)\left(1+1 / r_{m}\right)^{2}(k+1) / 2, & \text { otherwise }\end{cases}
$$

In (1.6), $n$ is assumed to be sufficiently large so that the asymptotic $\chi^{2}$ distribution in Property 1 can be used. If $n$ is small, the small sample degree of freedom in Barnard and Rubin (1999) should be used.

### 1.5 The Current MI Likelihood Ratio Test and Its Defect

Let $d_{\mathrm{L}}^{(\ell)}=d_{\mathrm{L}}\left(\widehat{\psi}_{0}^{(\ell)}, \widehat{\psi}^{(\ell)} \mid X^{(\ell)}\right), \widehat{\psi}_{0}^{(\ell)}=\widehat{\psi}_{0}\left(X^{(\ell)}\right)$ and $\widehat{\psi}^{(\ell)}=\widehat{\psi}\left(X^{(\ell)}\right)$ be the imputed counterparts of $d_{\mathrm{L}}\left(\widehat{\psi}_{0}, \widehat{\psi} \mid X\right), \widehat{\psi}_{0}$ and $\widehat{\psi}$, respectively, for each $\ell$. Define

$$
\bar{d}_{\mathrm{L}}=\frac{1}{m} \sum_{\ell=1}^{m} d_{\mathrm{L}}^{(\ell)}, \quad \bar{\psi}_{0}=\frac{1}{m} \sum_{\ell=1}^{m} \widehat{\psi}_{0}^{(\ell)}, \quad \bar{\psi}=\frac{1}{m} \sum_{\ell=1}^{m} \widehat{\psi}^{(\ell)}
$$

Similar to $\widetilde{r}_{\mathrm{W}}^{\prime}$, Meng and Rubin (1992) proposed estimating $\mathscr{F}_{m}$ by

$$
\tilde{r}_{\mathrm{L}}=\frac{m+1}{k(m-1)}\left(\bar{d}_{\mathrm{L}}-\tilde{d}_{\mathrm{L}}\right), \quad \text { where } \quad \tilde{d}_{\mathrm{L}}=\frac{1}{m} \sum_{\ell=1}^{m} d_{\mathrm{L}}\left(\bar{\psi}_{0}, \bar{\psi} \mid X^{(\ell)}\right)
$$

and hence it is again in the form of (1.5). The computation of $\widetilde{r}_{\mathrm{L}}$ requires that users have access to (i) a subroutine for $\left(X, \psi_{0}, \psi\right) \mapsto d_{\mathrm{L}}\left(\psi_{0}, \psi \mid X\right)$, and (ii) the estimates $\widehat{\psi}_{0}^{(\ell)}$ and $\widehat{\psi}^{(\ell)}$, rather than the matrices $\bar{U}$ and $B$. Therefore, computing $\widetilde{r}_{\mathrm{L}}$ is easier than computing $\widetilde{r}_{\mathrm{W}}^{\prime}$. The resulting MI LRT is

$$
\widetilde{D}_{\mathrm{L}}=\frac{\widetilde{d}_{\mathrm{L}}}{k\left(1+\widetilde{r}_{\mathrm{L}}\right)}
$$

the null distribution of which can be approximated by $F_{k, \widetilde{\mathrm{~d}}\left(\widetilde{r}_{\mathrm{L}}, k\right)}$. Its main theoretical justification (and motivation) is the asymptotic equivalence between the complete-data Wald test statistic and the LRT statistic under the null, as stated in Property 1. This equivalence permitted the replacement of $\bar{d}_{\mathrm{W}}^{\prime}$ and $\widetilde{d}_{\mathrm{W}}^{\prime}$ in (1.3) by $\bar{d}_{\mathrm{L}}$ and $\widetilde{d}_{\mathrm{L}}$, respectively, in (1.8). However, this is also where the problems lie.

First, with finite samples, $0 \leqslant \widetilde{d}_{\mathrm{L}} \leqslant \bar{d}_{\mathrm{L}}$ is not guaranteed; consequently, nor is $\widetilde{D}_{\mathrm{L}} \geqslant 0$ or $\widetilde{r}_{\mathrm{L}} \geqslant 0$. Because $\widetilde{D}_{\mathrm{L}}$ is referred to as an $F$ distribution and $\widetilde{r}_{\mathrm{L}}$ estimates $r_{m} \geqslant 0$, clearly, negative values of $\widetilde{D}_{\mathrm{L}}$ or $\widetilde{r}_{\mathrm{L}}$ will cause trouble. Second, the MI LRT statistic $\widetilde{D}_{\mathrm{L}}$ is not invariant to re-parameterization of $\psi$, although invariance is a natural property of the standard LRT; see, for example, Dagenais and Dufour (1991). This invariance principle is an appealing property because it requires that problems with the same formal structure should produce the same statistical results; see Chapter 6 of Berger (1985) and Chapter 3.2 of Lehmann and Casella (1998). Formally, we say that $\varphi=g(\psi)$ is a re-parametrization of $\psi$ if $g$ is a bijective map. The classical LRT statistic is invariant to re-parametrization because

$$
d_{\mathrm{L}}\left(\hat{\psi}_{0}, \hat{\psi} \mid X\right)=d_{\mathrm{L}}\left(g^{-1}\left(\hat{\varphi}_{0}\right), g^{-1}(\hat{\varphi}) \mid X\right)
$$

where $\hat{\varphi}_{0}$ and $\hat{\varphi}$ are the constrained and unconstrained MLEs, respectively, of $\varphi$ based on $X$. However, the MI (pooled) LRT statistic $\widetilde{d}_{\mathrm{L}}$ no longer has this property because

$$
\sum_{\ell=1}^{m} d_{\mathrm{L}}\left(\bar{\psi}_{0}, \bar{\psi} \mid X^{(\ell)}\right) \neq \sum_{\ell=1}^{m} d_{\mathrm{L}}\left(g^{-1}\left(\bar{\varphi}_{0}\right), g^{-1}(\bar{\varphi}) \mid X^{(\ell)}\right)
$$

in general, where $\hat{\varphi}_{0}^{(\ell)}$ and $\hat{\varphi}^{(\ell)}$ are the constrained and unconstrained MLEs, respectively, of $\varphi$ based on $X^{(\ell)}$, and $\bar{\varphi}_{0}=m^{-1} \sum_{\ell=1}^{m} \hat{\varphi}_{0}^{(\ell)}$ and $\bar{\varphi}=m^{-1} \sum_{\ell=1}^{m} \hat{\varphi}^{(\ell)}$. Section 4 shows how the MI LRT results vary dramatically with parametrizations in finite samples.

Third, the estimator $\tilde{r}_{\mathrm{L}}$ involves the estimators of $\psi$ under $H_{0}$, this is, $\widehat{\psi}_{0}^{(\ell)}$ and $\bar{\psi}_{0}$. When $H_{0}$ fails, they may be inconsistent for $\psi$. Thus, $\widetilde{r}_{\mathrm{L}}$ is no longer consistent for $\mathcal{r}_{m}$. A serious consequence is that the power of the test statistic $\widetilde{D}_{\mathrm{L}}$ is not guaranteed to monotonically increase as $H_{1}$ moves away from $H_{0}$. Indeed, our simulations (see Section 3.2) show that under certain parametrizations, the power may nearly vanish for obviously false $H_{0}$. Fourth, computing $\widetilde{d}_{\mathrm{L}}$ in (1.8) requires that users have access to $\widetilde{\mathscr{D}}_{\mathrm{L}}$, a function of both data and parameters. However, in most software, the available function is $\mathscr{D}_{\mathrm{L}}$, a function of data only; that is,

$$
\tilde{\mathscr{D}}_{\mathrm{L}}:\left(X, \psi_{0}, \psi\right) \mapsto d_{\mathrm{L}}\left(\psi_{0}, \psi \mid X\right), \quad \mathscr{D}_{\mathrm{L}}: X \mapsto d_{\mathrm{L}}\left(\hat{\psi}_{0}(X), \hat{\psi}(X) \mid X\right)
$$

It is not always feasible for users to write themselves a subroutine for computing $\widetilde{\mathscr{D}}_{L}$.

In short, four problems need to be resolved: (i) the lack of non-negativity, (ii) the lack of invariance, (iii) the lack of consistency and power, and (iv) the lack of a feasible algorithm. Problems (i)-(iii) are resolved in Section 2; (iv) is resolved in Section 3.

## 2. Improved MI Likelihood Ratio Tests

### 2.1 Invariant Combining Rule and Estimator of $\varkappa_{m}$

To derive a parametrization-invariant MI LRT, we replace $\widetilde{d}_{\mathrm{L}}$ by an asymptotically equivalent version that behaves like a standard LRT statistic. Let

$$
\bar{L}(\psi)=\frac{1}{m} \sum_{\ell=1}^{m} L^{(\ell)}(\psi), \quad \text { where } \quad L^{(\ell)}(\psi)=\log f\left(X^{(\ell)} \mid \psi\right) .
$$

Here, $\bar{L}(\psi)$ is not a real log-likelihood, because it does not properly model the completed data sets: $\mathbb{X}=\left\{X^{1}, \ldots, X^{m}\right\}$ (e.g., all $X^{\ell}$ share the same $X_{\text {obs }}$ ). Nevertheless, $\bar{L}(\psi)$ can be treated as a log-likelihood for computational purposes. In particular, we can maximize it to obtain

$$
\widehat{\psi}_{0}^{*}=\widehat{\psi}_{0}^{*}(\mathbb{X})=\underset{\psi \in \Psi: \theta(\psi)=\theta_{0}}{\arg \max } \bar{L}(\psi), \quad \widehat{\psi}^{*}=\widehat{\psi}^{*}(\mathbb{X})=\underset{\psi \in \Psi}{\arg \max } \bar{L}(\psi)
$$

The corresponding log-likelihood ratio test statistic is given by

$$
\hat{d}_{\mathrm{L}}=2\left\{\bar{L}\left(\widehat{\psi}^{*}\right)-\bar{L}\left(\widehat{\psi}_{0}^{*}\right)\right\}=\frac{1}{m} \sum_{\ell=1}^{m} d_{\mathrm{L}}\left(\widehat{\psi}_{0}^{*}, \widehat{\psi}^{*} \mid X^{(\ell)}\right)
$$

Thus, in contrast to $\widetilde{d}_{\mathrm{L}}$ of (1.8), $\widehat{d}_{\mathrm{L}}$ aggregates MI data sets by averaging the MI LRT functions, as in (2.1), rather than averaging the MI test statistics and moments, as in (1.7). Although $\sqrt{n}\left(\widehat{\psi}_{0}^{*}-\bar{\psi}_{0}\right) \xrightarrow{\mathrm{pr}} \mathbf{0}$ and $\sqrt{n}\left(\widehat{\psi}^{*}-\bar{\psi}\right) \xrightarrow{\mathrm{pr}} \mathbf{0}$ as $n \rightarrow \infty$ for each $m$, only $\hat{d}_{\mathrm{L}}$, not $\widetilde{d}_{\mathrm{L}}$, is guaranteed to be non-negative and invariant to parametrization of $\psi$ for all $m, n$. Indeed, the likelihood principle guides us to consider averaging individual log-likelihoods rather than individual MLEs, because the former has a much better chance of capturing the functional features of the real log-likelihood than any of their (local) maximizers can.

To derive the properties of $\hat{d}_{\mathrm{L}}$, we need the usual regularity conditions on the MLE and MI.

Assumption 2. The sampling model $f(X \mid \psi)$ satisfies the following:
(a) The map $\psi \mapsto \underline{L}(\psi)=n^{-1} \log f(X \mid \psi)$ is twice continuously differentiable.
(b) The complete-data MLE $\widehat{\psi}(X)$ is the unique solution of $\partial \underline{L}(\psi) / \partial \psi=\mathbf{0}$.
(c) Let $\underline{I}(\psi)=-\partial^{2} \underline{L}(\psi) / \partial \psi \partial \psi^{\boldsymbol{\top}}$; then, for each $\psi$, there exists a positive-definite matrix $\underline{\mathscr{I}}(\psi)=\mathscr{U}_{\psi}^{-1}$ such that $\underline{I}(\psi) \xrightarrow{\text { pr }} \underline{\mathscr{I}}(\psi)$ as $n \rightarrow \infty$.
(d) The observed-data MLE $\widehat{\psi}_{\mathrm{obs}}$ of $\psi$ obeys

$$
\left[\mathscr{T}_{\psi}^{-1 / 2}\left(\widehat{\psi}_{\mathrm{obs}}-\psi\right) \mid \psi\right] \Rightarrow \mathscr{N}_{h}\left(\mathbf{0}, I_{h}\right)
$$

as $n \rightarrow \infty$, where $I_{h}$ is the $h \times h$ identity matrix.
Assumption 3. The imputation model is proper (Rubin, 2004):

$$
\begin{gathered}
{\left[\mathscr{B}_{\psi}^{-1 / 2}\left(\widehat{\psi}^{(\ell)}-\widehat{\psi}_{\mathrm{obs}}\right) \mid X_{\mathrm{obs}}\right] \Rightarrow \mathcal{N}_{h}\left(\mathbf{0}, I_{h}\right),} \\
{\left[\mathscr{T}_{\psi}^{-1}\left(U_{\psi}^{(\ell)}-\mathcal{U}_{\psi}\right) \mid X_{\mathrm{obs}}\right] \xrightarrow{\mathrm{pr}} \mathbf{0}, \quad\left[\mathscr{T}_{\psi}^{-1}\left(B_{\psi}-\mathscr{B}_{\psi}\right) \mid X_{\mathrm{obs}}\right] \xrightarrow{\mathrm{pr}} \mathbf{0}}
\end{gathered}
$$

independently for each $\ell$, as $n \rightarrow \infty$, provided that $\mathscr{B}_{\psi}^{-1}$ is well defined.
Assumption 2 holds under the usual regularity conditions that guarantee the normality and consistency of MLEs. When $X_{\text {mis }}^{(1)}, \ldots, X_{\text {mis }}^{(m)}$ are drawn independently from a (correctly specified) posterior predictive distribution $f\left(X_{\text {mis }} \mid X_{\text {obs }}\right)$, Assumption 3 is typically satisfied. Clearly, we can replace $\psi$ by its sub-vector $\theta$ in Assumptions 2 and 3. These $\theta$-version assumptions are sufficient to guarantee the validity of Theorem 2 and Corollary 1. For simplicity, Assumption 1, the $\theta$-version of Assumptions 2 and 3, and the conditions that guarantees Property 1 are collectively written as $\mathrm{RC}_{\theta}$ ( RC denotes "regularity conditions"), which are commonly assumed for MI inference.

Theorem 1. Assume $\mathrm{RC}_{\theta}$. Under $H_{0}$, we have (i) $\widehat{d}_{\mathrm{L}} \geqslant 0$ for all $m$, $n$; (ii) $\widehat{d}_{\mathrm{L}}$ is invariant to parametrization of $\psi$ for all $m, n$; and (iii) $\widehat{d}_{\mathrm{L}} \bumpeq \widetilde{d}_{\mathrm{L}}$ as $n \rightarrow \infty$ for each $m$.

Consequently, an improved combining rule is defined as

$$
\hat{D}_{\mathrm{L}}\left(r_{m}\right)=\frac{\hat{d}_{\mathrm{L}}}{k\left(1+r_{m}\right)}
$$

for a given value of $r_{m}$. The forms of 1.4 and 1.9 follow. Using $\hat{d}_{\mathrm{L}}$ in (2.3), we can modify $\widetilde{r}_{\mathrm{L}}$ in (1.8) to provide a potentially better estimator:

$$
\widehat{r}_{\mathrm{L}}=\frac{m+1}{k(m-1)}\left(\bar{d}_{\mathrm{L}}-\hat{d}_{\mathrm{L}}\right)
$$

Although $\hat{d}_{\mathrm{L}} \geqslant 0$ is guaranteed by our construction, $\hat{r}_{\mathrm{L}} \geqslant 0$ does not hold in general for a finite $m$. However, it is guaranteed in the following situation.

Proposition 1. Write $\psi=\left(\theta^{\boldsymbol{\top}}, \eta^{\boldsymbol{\top}}\right)^{\boldsymbol{\top}}$, where $\eta$ represents a nuisance parameter that is distinct from $\theta$. If there exist functions $L_{\dagger}$ and $L_{\ddagger}$ such that, for all $X$, the log-likelihood function $L(\psi \mid X)=\log f(X \mid \psi)$ is of the form $L(\psi \mid X)=L_{\dagger}(\theta \mid X)+L_{\ddagger}(\eta \mid X)$, then $\widehat{r}_{\mathrm{L}} \geqslant 0$ for all $m, n$.

The condition in Proposition 1 means that the likelihood function of $\psi$ is separable, which ensures that the profile likelihood estimator of $\eta$ given $\theta$, this is, $\widehat{\eta}_{\theta}=\arg \max _{\eta} L(\theta, \eta \mid X)$, is free of $\theta$. Clearly, in the absence of the nuisance parameter $\eta$, the separation condition holds trivially. More generally, we have the following.

Corollary 1. Assume $\mathrm{RC}_{\theta}$. We have (i) under $H_{0}, \widehat{r}_{\mathrm{L}} \xrightarrow{\mathrm{pr}} r$ as $m, n \rightarrow \infty$; and (ii) under $H_{1}, \hat{r}_{\mathrm{L}} \xrightarrow{\mathrm{pr}} \mathcal{r}_{0}$ as $m, n \rightarrow \infty$, where $\mathcal{r}_{0} \geqslant 0$ is some finite value depending on $\theta_{0}$ and the true value of $\theta$.

Corollary 1 ensures that, under $H_{0}, \widehat{r}_{\mathrm{L}}$ is non-negative asymptotically and converges in probability to the true $\mathcal{r}$. However, it also reveals another fundamental defect of $\widehat{r}_{L}$ : under $H_{1}$, the limit $\varkappa_{0}$ may not equal $r$, a problem we address in Section 2.2. Fortunately, because $\hat{d}_{\mathrm{L}} \xrightarrow{\mathrm{pr}} \infty$ under $H_{1}$, the LRT statistic $\hat{D}_{\mathrm{L}}\left(\hat{r}_{\mathrm{L}}\right)$ is still powerful, albeit the power may be reduced. Similarly, $\widetilde{r}_{\mathrm{L}}$ of 1.8 has the same asymptotic properties and defects, but $\widehat{r}_{\mathrm{L}}$ behaves more nicely than $\widetilde{r}_{\mathrm{L}}$ for finite $m$. This hinges closely on the high sensitivity of $\widetilde{r}_{\mathrm{L}}$ to the parametrization of $\psi$; for example, $\widetilde{r}_{\mathrm{L}}$ may become more negative as $H_{1}$ moves away from $H_{0}$; see Section 4.1.

Whereas we can fix the occasional negativeness of $\hat{r}_{\mathrm{L}}$ by using $\hat{r}_{\mathrm{L}}^{+}=\max \left(0, \hat{r}_{\mathrm{L}}\right)$, such an ad hoc fix misses the opportunity to improve upon $\widehat{r}_{\mathrm{L}}$, and indeed it cannot fix the inconsistency of $\hat{r}_{\mathrm{L}}$ under $H_{1}$.

### 2.2 A Consistent and Non-Negative Estimator of $\varkappa_{m}$

Proposition 1 already hinted that the source of the negativity and inconsistency of $\widehat{r}_{\mathrm{L}}$ is related to the existence of the nuisance parameter $\eta$. By definition, $\bar{d}_{\mathrm{L}}$ and $\widehat{d}_{\mathrm{L}}$ depend on the specification of $\theta_{0}$. In general, the effect of $\theta_{0}$ may not be cancelled out by their difference $\bar{d}_{\mathrm{L}}-\hat{d}_{\mathrm{L}}$, unless a certain type of orthogonality assumption is made on $\eta$ and $\theta$; see Proposition 1 for an example. Consequently, the validity of the estimator $\hat{r}_{\mathrm{L}}$ depends on the correctness of $H_{0}$. A more elaborate discussion can be found in Appendix A.1. In order to principally resolve the aforementioned problem, we need to eliminate the dependence on $\theta_{0}$ in our estimator for the odds of missing information, $\mathscr{r}_{m}$. We achieve this goal by estimating these odds for the
entire $\psi$, resulting in the following estimator for $\varkappa_{m}$ :

$$
\begin{gathered}
\widehat{r}_{\mathrm{L}}^{\diamond}=\frac{m+1}{h(m-1)}\left(\bar{\delta}_{\mathrm{L}}-\widehat{\delta}_{\mathrm{L}}\right), \quad \text { where } \\
\bar{\delta}_{\mathrm{L}}=2 \bar{L}\left(\widehat{\psi}^{(1)}, \ldots, \widehat{\psi}^{(m)}\right), \quad \widehat{\delta}_{\mathrm{L}}=2 \bar{L}\left(\widehat{\psi}^{*}, \ldots, \widehat{\psi}^{*}\right),
\end{gathered}
$$

and $h$ is the dimension of $\psi$. In (2.10), the rhombus " ◇" symbolizes a robust estimator. It is robust because it is consistent under either $H_{0}$ or $H_{1}$, as long as we are willing to impose the EFMI assumption on $\psi$, this is, Assumption 4 . This expansion from $\theta$ to $\psi$ is inevitable because the LRT must handle the entire $\psi$, not just $\theta$. The collection of Assumptions 24 are referred to as $\mathrm{RC}_{\psi}$.

Assumption 4 (EFMI of $\psi$ ). There is $\mathfrak{r} \geqslant 0$ such that $\mathscr{T}_{\psi}=(1+\mathfrak{r}) \mathscr{U}_{\psi}$.
Theorem 2. Assume $\mathrm{RC}_{\psi}$. For any value of $\psi$, we have (i) $\widehat{r}_{\mathrm{L}}^{\diamond} \geqslant 0$ for all $m, n$; (ii) $\widehat{r}_{\mathrm{L}}^{\diamond}$ is invariant to parametrization of $\psi$ for all $m, n$; and (iii) $\widehat{r}_{\mathrm{L}}^{\diamond} \xrightarrow{\mathrm{pr}} r$ as $m, n \rightarrow \infty$, where $r$ is given in Assumption 4 .

With the improved combining rule $\hat{D}_{\mathrm{L}}\left(\mathcal{F}_{m}\right)$ of 2.7 and improved estimators for $\mathfrak{r}_{m}$, we are ready to propose two MI LRT statistics:

$$
\hat{D}_{\mathrm{L}}^{+}=\hat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}^{+}\right) \quad \text { and } \quad \hat{D}_{\mathrm{L}}^{\diamond}=\hat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right)
$$

For comparison, we also study the test statistic $\widehat{D}_{\mathrm{L}}=\widehat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}\right)$.

### 2.3 Reference Null Distributions

The estimators $\widehat{r}_{\mathrm{L}}^{+}$and $\widetilde{r}_{\mathrm{L}}$ have the same functional form asymptotically ( $n \rightarrow \infty$ ). Hence, they have the same asymptotic distribution.

Lemma 1. Suppose $\mathrm{RC}_{\theta}$ and $m>1$. Under $H_{0}$, we have, jointly,

$$
\frac{\hat{r}_{\mathrm{L}}^{+}}{r_{m}} \Rightarrow M_{2} \quad \text { and } \quad \hat{D}_{\mathrm{L}}^{+} \Rightarrow \frac{\left(1+r_{m}\right) M_{1}}{1+r_{m} M_{2}}
$$

as $n \rightarrow \infty$, where $M_{1} \sim \chi_{k}^{2} / k$ and $M_{2} \sim \chi_{k(m-1)}^{2} /\{k(m-1)\}$ are independent.
Consequently, $\hat{D}_{\mathrm{L}}^{+}=\hat{D}_{\mathrm{L}}\left(\hat{r}_{\mathrm{L}}^{+}\right)$approximately follows $F_{k, \widetilde{\mathrm{df}}\left(\hat{r}_{\mathrm{L}}^{+}, k\right)}$ under $H_{0}$, but a better approximation is provided shortly. For the other proposal, although $\hat{r}_{\mathrm{L}}^{+}- \widehat{r}_{\mathrm{L}}^{\vee} \xrightarrow{\mathrm{pr}} 0$ as $n \rightarrow \infty$ under $H_{0}$, their non-degenerated limiting distributions are different because $\widehat{r}_{\mathrm{L}}^{\diamond}$ and $\widehat{r}_{\mathrm{L}}^{+}$rely on an average FMI in $\psi$ and $\theta$, respectively.

Theorem 3. Suppose $\mathrm{RC}_{\psi}$ and $m>1$. Then, for any value of $\psi$,

$$
\frac{\widehat{r}_{\mathrm{L}}^{\diamond}}{r_{m}} \Rightarrow M_{3} \sim \frac{\chi_{h(m-1)}^{2}}{h(m-1)}
$$

as $n \rightarrow \infty$, where $M_{3}$ is independent of the $M_{1}$ defined in (2.12).
Theorem 3 implies that, if $n$ can be regarded as infinity and $\widehat{r}_{\mathrm{L}}^{\diamond}$ is uniformly integrable in $\mathscr{L}^{2}$, then $\operatorname{Bias}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right)=\mathrm{E}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right)-\mathcal{r}_{m}=0$ and $\operatorname{Var}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right)=2 \varkappa_{m}^{2} /\{h(m-1)\}=O\left(m^{-1}\right)$ as $m \rightarrow \infty$. Hence, $\widehat{r}_{\mathrm{L}}^{\diamond}$ is a $\sqrt{m}$-consistent estimator of $r$ in $\mathscr{L}^{2}$. Moreover, for each $m>1$ and as $n \rightarrow \infty$, we have $\operatorname{Bias}\left(\widehat{r}_{\mathrm{L}}^{+}\right) / \operatorname{Bias}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right) \rightarrow 1$ and $\operatorname{Var}\left(\widehat{r}_{\mathrm{L}}^{+}\right) / \operatorname{Var}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right) \rightarrow h / k \geqslant 1$, which imply that $\widehat{r}_{\mathrm{L}}^{\diamond}$ is no less efficient than $\widehat{r}_{\mathrm{L}}^{+}$when $\mathrm{RC}_{\psi}$ holds. This is not surprising because of the extra information brought in by the stronger Assumption 4. Result (2.13) also gives us the exact (i.e., for any $m>1$, but assuming $n \rightarrow \infty$ ) reference null distribution of $\widehat{D}_{\mathrm{L}}^{\diamond}$, as given below.

Theorem 4. Assume $\mathrm{RC}_{\psi}$ and $m>1$. Under $H_{0}$, we have

$$
\hat{D}_{\mathrm{L}}^{\diamond} \Rightarrow \frac{\left(1+r_{m}\right) M_{1}}{1+r_{m} M_{3}} \equiv D
$$

as $n \rightarrow \infty$, where $M_{1} \sim \chi_{k}^{2} / k$ and $M_{3} \sim \chi_{h(m-1)}^{2} /\{h(m-1)\}$ are independent.
The impact of the nuisance parameter $\varkappa_{m}$ on $D$ diminishes with $m$ because $\hat{D}_{\mathrm{L}}^{\diamond}$ and $\widehat{D}_{\mathrm{L}}^{+}$converge in distribution to $M_{1}=\chi_{k}^{2} / k$ as $m, n \rightarrow \infty$. Because $M_{3} \xrightarrow{\mathrm{pr}} 1$ faster than $M_{2} \xrightarrow{\mathrm{pr}} 1, \widehat{D}_{\mathrm{L}}^{\diamond}$ is expected to be more robust to $r_{m}$. Nevertheless, $m$ typically is small in practice (e.g., $m \leqslant 10$ ), so we cannot ignore the impact of $r_{m}$. This issue has been largely dealt with in the literature by seeking an $F_{k, \mathrm{df}}$ distribution to approximate $D$, as in Li et al. (1991b). However, directly adopting their $\widetilde{\mathrm{df}}$ of 1.6 leads to a poorer approximation for our purposes; see below. A better approximation is to match the first two moments of the denominator of (2.14, $1+r_{m} M_{3}$, with that of a scaled $\chi^{2}: a \chi_{b}^{2} / b$. This yields $a=1+r_{m}$ and $b=\left(1+r_{m}^{-1}\right)^{2} h(m-1)$, and the approximated $F_{k, \hat{\mathrm{df}}\left(r_{m}, h\right)}$, where

$$
\widehat{\mathrm{df}}\left(r_{m}, h\right)=\left\{\frac{1+r_{m}}{r_{m}}\right\}^{2} h(m-1)=\frac{h(m-1)}{f_{m}^{2}}
$$

which is appealing because it simply inflates the denominator degrees of freedom $h(m-1)$ by dividing it by the square of the finite- $m$ corrected FMI $f_{m}=r_{m} /(1+ \left.r_{m}\right)$. The less missing information, the closer $F_{k, \widehat{\mathrm{df}}\left(r_{m}, h\right)}$ is to $\chi_{k}^{2} / k$, the usual large- $n \chi^{2}$ test; as mentioned earlier, for small $n$, see Barnard and Rubin (1999).

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-14.jpg?height=802&width=1286&top_left_y=421&top_left_x=330)
Figure 1: The performance of two approximated null distributions when the nominal size is $\alpha=0.5 \%$. The vertical axis denotes $\widehat{\alpha}$ or $\widetilde{\alpha}$, and the horizontal axis denotes the value of $f_{m}$. The number attached to each line denotes the value of $\tau=h / k$.

To compare the performance of $F_{k, \widehat{\mathrm{df}}\left(\boldsymbol{r}_{m}, h\right)}$ in 2.15 with the existing best approximation $F_{k, \widetilde{\mathrm{df}}\left(r_{m}, h\right)}$, as approximations to the limiting distribution of $D$ given in (2.14), we compute via simulations

$$
\widetilde{\alpha}=\mathrm{P}\left\{D>F_{k, \widetilde{\mathrm{~d}}\left(\varkappa_{m}, h\right)}^{-1}(1-\alpha)\right\} \quad \text { and } \quad \hat{\alpha}=\mathrm{P}\left\{D>F_{k, \widehat{\mathrm{~d}}\left(\varkappa_{m}, h\right)}^{-1}(1-\alpha)\right\},
$$

where $F_{k, \text { df }}^{-1}(q)$ denotes the $q$-quantile of $F_{k, \text { df }}$. Note that the experiments assess solely the performance of the finite- $m$ approximation instead of the performance of the large- $n \chi^{2}$-approximation of the asymptotic LRT statistics. We draw $N= 2^{18}$ independent copies $D$ for each of the following possible combinations: $m \in \{3,5,7\}, k \in\{1,2,4,8\}, \tau=h / k \in\{1,2,3\}, f_{m} \in\{0,0.1, \ldots, 0.9\}$, and following the recommendation of Benjamin et al. (2018), we use both $\alpha \in\{0.5 \%, 5 \%\}$. The results for $\alpha=0.5 \%$ and $\alpha=5 \%$ are shown in Figure 1 and Figure 6 of the Appendix, respectively. In general, $\widehat{\alpha}$ approximates $\alpha$ much better than $\widetilde{\alpha}$ does, especially when $m, k, h$ are small. When $m, h$ are larger, they perform similarly because both $F_{k, \widetilde{\mathrm{~d}}\left(r_{m}, h\right)}$ and $F_{k, \hat{\mathrm{~d}}\left(r_{m}, h\right)}$ get closer to $\chi_{k}^{2} / k$. However, the performance of $\widetilde{\alpha}$ and
$\widehat{\alpha}$ is not monotonic in $f_{m}$. The performance of $F_{k, \widehat{\mathrm{df}}\left(r_{m}, h\right)}$ is particularly good for $0 \% \lesssim f_{m} \lesssim 30 \%$. Consequently, we recommend using $F_{k, \widehat{\mathrm{df}}\left(\widehat{\mathrm{r}}_{\mathrm{L}}^{\diamond}, h\right)}$ as an approximate null distribution for $\widehat{D}_{\mathrm{L}}^{\diamond}$, and $F_{k, \widehat{\mathrm{df}}^{\mathrm{f}}\left(\widehat{r}_{\mathrm{L}}^{+}, k\right)}$ for $\widehat{D}_{\mathrm{L}}^{+}$, as employed in the rest of this paper. However, these approximations obviously suffer from the usual "plug-in problem" by ignoring the uncertainty in estimating $\varkappa_{m}$. Because $F_{k, \text { df }}$ is not too sensitive to the value of df once it is reasonably large ( $\mathrm{df} \geqslant 20$ ), the "plug-in problem" is less an issue here than in many other contexts, leading to acceptable approximations, as empirically demonstrated in Section 4. Nevertheless, further improvements should be sought, especially for dealing with the violation of the EFMI assumption, which would likely make the performance of our tests deteriorate with large $k$ or $h$, in contrast to the results shown in Figure 1, see Chan 2021) for a possible remedy.

## 3. Computational Considerations and Comparisons

### 3.1 Computationally Feasible Combining Rule

For many real-world data sets, $X$ is an $n \times p$ matrix, with rows indicating subjects and columns indicating attributes. We write $X=\left(X_{1}, \ldots, X_{n}\right)^{\top}$, and its sampling model by $f_{n}(X \mid \psi)$. Correspondingly, the $\ell$ th imputed data set is $X^{(\ell)}= \left(X_{1}^{(\ell)}, \ldots, X_{n}^{(\ell)}\right)^{\top}$. Define the stacked data set by $X^{(1: m)}=\left[\left(X^{(1)}\right)^{\top}, \ldots,\left(X^{(m)}\right)^{\top}\right]^{\top}$, a $m n \times p$ matrix, which is conceptually different from the collection of data sets $\left\{X^{(1)}, \ldots, X^{(m)}\right\}$. Assuming that the rows of $X$ are independent, we can compute (2.1) as

$$
\bar{L}(\psi)=\frac{1}{m} \log f_{m n}\left(X^{(1: m)} \mid \psi\right)
$$

Consequently, as long as the user's complete-data procedures can handle size $m n$ instead of $n$, the user can apply them to $X^{(1: m)}$ to obtain $\widehat{D}_{\mathrm{L}}^{+}$and $\widehat{D}_{\mathrm{L}}^{\diamond}$ in (2.11).

In many applications, the rows correspond to individual subjects. Thus, the row-independence assumption typically holds for arbitrary $n$. Hence, we can extend from $n$ to $m n$, assuming the user's complete-data procedure is not size-limited. Even if this is not true, A.5 can still hold approximately under some regularity conditions; see Appendix A, where we also reveal a subtle, but important difference between the computation formulae (2.1) and A.5).

Similar to $\mathscr{D}_{\mathrm{L}}$ in 1.10, we define complete-data functions

$$
\mathscr{D}_{\mathrm{L}, 0}(X)=2 \log f\left(X \mid \hat{\psi}_{0}(X)\right), \quad \mathscr{D}_{\mathrm{L}, 1}(X)=2 \log f(X \mid \hat{\psi}(X))
$$

the only input of which is the data set $X$. Clearly, $\mathscr{D}_{\mathrm{L}}(X)=\mathscr{D}_{\mathrm{L}, 1}(X)-\mathscr{D}_{\mathrm{L}, 0}(X)$. The subroutine for evaluating the complete-data LRT function $X \mapsto \mathscr{D}_{\mathrm{L}}(X)$ is usually available, as is the subroutine for $X \mapsto \mathscr{D}_{\mathrm{L}, 1}(X)$, for example, the function

```
Algorithm 1: (Robust) MI LRT statistic $\widehat{D}_{\mathrm{L}}^{\diamond}$
    Input: Data sets $X^{(1)}, \ldots, X^{(m)} ; h, k$; functions $\mathscr{D}_{\mathrm{L}, 1}, \mathscr{D}_{\mathrm{L}}$ in (3.2), (1.10).
    begin
        Stack the data sets to form $X^{(1: m)}=\left[\left(X^{(1)}\right)^{\top}, \ldots,\left(X^{(m)}\right)^{\top}\right]^{\top}$.
        Find $\bar{\delta}_{\mathrm{L}}=\sum_{\ell=1}^{m} \mathscr{D}_{\mathrm{L}, 1}\left(X^{(\ell)}\right) / m, \widehat{\delta}_{\mathrm{L}}=\mathscr{D}_{\mathrm{L}, 1}\left(X^{(1: m)}\right) / m$,
            $\hat{d}_{\mathrm{L}}=\mathscr{D}_{\mathrm{L}}\left(X^{(1: m)}\right) / m$.
        Calculate $\widehat{r}_{\mathrm{L}}^{\diamond}$ according to 2.9, and $\widehat{D}_{\mathrm{L}}^{\diamond}$ according to 2.7 and 2.11.
        Calculate $\widehat{\mathrm{df}}\left(\widehat{r}_{\mathrm{L}}, h\right)$ according to 2.15 .
        Compute the $p$-value as $1-F_{k, \widehat{\mathrm{df}}\left(\widehat{r}_{\mathrm{L}}^{\diamond}, h\right)}\left(\widehat{D}_{\mathrm{L}}^{\diamond}\right)$.
```

```
Algorithm 2: MI LRT statistic $\widehat{D}_{\mathrm{L}}^{+}$
    Input: Data sets $X^{(1)}, \ldots, X^{(m)} ; k$; function $\mathscr{D}_{\mathrm{L}}$ in 1.10.
    begin
        Stack the data sets to form $X^{(1: m)}=\left[\left(X^{(1)}\right)^{\top}, \ldots,\left(X^{(m)}\right)^{\top}\right]^{\top}$.
        Find $\bar{d}_{\mathrm{L}}=\sum_{\ell=1}^{m} \mathscr{D}_{\mathrm{L}}\left(X^{(\ell)}\right) / m$ and $\hat{d}_{\mathrm{L}}=m^{-1} \mathscr{D}_{\mathrm{L}}\left(X^{(1: m)}\right)$.
        Calculate $\hat{r}_{\mathrm{L}}^{+}$according to 2.8, and $\hat{D}_{\mathrm{L}}^{+}$according to 2.7 and 2.11.
        Calculate $\widehat{\mathrm{df}}\left(\widehat{r}_{\mathrm{L}}^{+}, k\right)$ according to 2.15 .
        Compute the $p$-value as $1-F_{k, \hat{\mathrm{df}}\left(\hat{r}_{\mathrm{L}}^{+}, k\right)}\left(\hat{D}_{\mathrm{L}}^{+}\right)$.
```

logLik in R extracts the maximum of the complete data log-likelihood for objects belonging to classes "glm", "lm", "nls", and "Arima".

Algorithms 1 and 2 compute $\widehat{D}_{\mathrm{L}}^{\diamond}$ and $\widehat{D}_{\mathrm{L}}^{+}$, respectively. We recommend using the robust MI LRT in Algorithm 1, because it has the best theoretical guarantee. The second test can be useful when $\mathscr{D}_{\mathrm{L}}$ is available but $\mathscr{D}_{\mathrm{L}, 1}$ is not.

### 3.2 Computational Comparison with Existing Tests

Different MI tests require different computing subroutines, for example, $\mathscr{D}_{\mathrm{L}}, \widetilde{\mathscr{D}}_{\mathrm{L}}$, $\mathscr{D}_{\mathrm{L}, 1}$,

$$
\mathscr{M}_{\mathrm{W}}(X)=\{\hat{\theta}(X), U(X)\} \quad \text { and } \quad \mathscr{M}_{\mathrm{L}}(X)=\left\{\hat{\psi}(X), \hat{\psi}_{0}(X)\right\},
$$

where the unnormalized density can be used in $\mathscr{D}_{\mathrm{L}, 1}$. We summarize the computing requirement in Table1. We also compare the following statistical and computational properties of various MI test statistics and various estimators of $\mathcal{r}_{m}$ :

- (Inv) The MI test is invariant to re-parametrization of $\psi$.

Table 1: Computational requirements and statistical properties of MI tests. The symbol "+" (resp. "-") means that a test has (resp. does not have) the indicated property; see Section 3.2 for detailed descriptions. WT-1 Rubin, 2004, Li et al., 1991a) and LRT-1 (Meng and Rubin, 1992) are existing tests. LRT-2 and LRT-3 are the proposed tests, which can be computed by Algorithms 2 and 1 , respectively. LRT-3 is recommended.
|  |  |  |  | Properties |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Test | Statistic | Distribution | Routine | Inv | Con | $\geqslant$ | 0 | Pow | Def | Sca | EFMI |
| WT-1 | $D_{\mathrm{W}}(T)$ | $\approx F_{k, \widetilde{\mathrm{~d}}_{\mathrm{f}}\left(r_{\mathrm{W}}^{\prime}, k\right)}$ | $\mathscr{M}_{\mathrm{W}}$ | - | + | + | - | - | - | $\theta$ |  |
| LRT-1 | $\widetilde{D}_{\mathrm{L}}\left(\widetilde{r}_{\mathrm{L}}\right)$ | $\approx F_{k, \widetilde{\mathrm{~d}}_{\mathrm{f}}\left(\widetilde{r}_{\mathrm{L}}, k\right)}$ | $\mathscr{M}_{\mathrm{L}}, \widetilde{\mathscr{D}}_{\mathrm{L}}$ | - | - | - | - | + | - | $\theta$ |  |
| LRT-2 | $\hat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}^{+}\right)$ | $\approx F_{k, \hat{\mathrm{~d}} \mathrm{f}\left(\hat{r}_{\mathrm{L}}^{+}, k\right)}$ | $\mathscr{D}_{\mathrm{L}}$ | + | - | + | - | + | + | $\theta$ |  |
| LRT-3 | $\hat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}^{\mathrm{v}}\right)$ | $\approx F_{k, \hat{\mathrm{~d}} \mathrm{f}\left(\widehat{r}_{\mathrm{L}}, k\right)}$ | $\mathscr{D}_{\mathrm{L}}, \mathscr{D}_{\mathrm{L}, 1}$ | + | + | + | + | + | + | $\psi$ |  |


- (Con) The estimator of $\varkappa_{m}$ is consistent, regardless of whether or not $H_{0}$ is true.
- ( $\geqslant 0$ ) The test statistic and estimator of $\varkappa_{m}$ are always non-negative.
- (Pow) The MI test has high power to reject $H_{0}$ under $H_{1}$.
- (Def) The MI test statistic is well defined and numerically well conditioned.
- (Sca) The MI procedure requires that users deal with scalars only.
- (EFMI) Whether EFMI is assumed for $\theta$ or for $\psi$.

In summary, our proposed LRT-2 is the most attractive computationally. If the user is willing to make stronger assumptions, our proposed LRT-3 has better statistical properties, and is still computationally feasible. In practice, we recommend using LRT-3. We also present other existing MI tests and compare our proposals with them in Appendix A.5.

### 3.3 Summary of Notation

For ease of referencing, we summarize all major notation used in the paper. Recall that $\psi \in \mathbb{R}^{h}$ is the model parameter, and $\theta$ is the parameter of interest. We would like to test $H_{0}: \theta=\theta_{0}$ against $H_{1}: \theta \neq \theta_{0}$.

- Complete-data Estimators and Test Statistics:
$-\hat{\theta}(X)$ and $U(X)$ : MLE of $\theta$ and its variance estimator.
$-\widehat{\psi}(X)$ and $\widehat{\psi}_{0}(X)$ : the unrestricted and $H_{0}$-restricted MLEs of $\psi$.
$-d_{\mathrm{W}}(\hat{\theta}, U)=\left(\hat{\theta}-\theta_{0}\right)^{\top} U^{-1}\left(\hat{\theta}-\theta_{0}\right)$ : the Wald test statistic.
$-d_{\mathrm{L}}\left(\hat{\psi}_{0}, \hat{\psi} \mid X\right)=2 \log \left\{f(X \mid \hat{\psi}) / f\left(X \mid \hat{\psi}_{0}\right)\right\}$ : the LRT statistic.
- Complete-data Functions (or Software Routines):
$-\mathscr{M}_{\mathrm{W}}(X)=\{\hat{\theta}(X), U(X)\}$ and $\mathscr{M}_{\mathrm{L}}(X)=\left\{\widehat{\psi}(X), \hat{\psi}_{0}(X)\right\}$.
$-\widetilde{\mathscr{D}}_{\mathrm{L}}\left(X, \psi_{0}, \psi\right)=d_{\mathrm{L}}\left(\psi_{0}, \psi \mid X\right)$ : a nonstandard LRT function/routine.
$-\mathscr{D}_{\mathrm{L}}(X)=d_{\mathrm{L}}\left(\hat{\psi}_{0}(X), \hat{\psi}(X) \mid X\right)$ : the standard LRT function/routine.
- $\mathscr{D}_{\mathrm{L}, 1}(X)=2 \log f(X \mid \hat{\psi}(X))$ : the (scaled) maximum log-likelihood.
- MI Statistics:
$-\hat{\theta}^{(\ell)}, U^{(\ell)}, \hat{\psi}_{0}^{(\ell)}, \hat{\psi}^{(\ell)}, d_{\mathrm{W}}^{(\ell)}, d_{\mathrm{L}}^{(\ell)}$ : the imputed values of $\hat{\theta}, U, \hat{\psi}_{0}, \hat{\psi}$, $d_{\mathrm{W}}(\widehat{\theta}, U), d_{\mathrm{L}}\left(\widehat{\psi}_{0}, \widehat{\psi} \mid X\right)$ using the imputed data set $X^{(\ell)}$ for each $\ell$.
$-\bar{\theta}, \bar{U}, \bar{\psi}_{0}, \bar{\psi}, \bar{d}_{\mathrm{W}}, \bar{d}_{\mathrm{L}}:$ the averages (over $\ell$ ) of $\hat{\theta}^{(\ell)}, U^{(\ell)}, \widehat{\psi}_{0}^{(\ell)}, \widehat{\psi}^{(\ell)}, d_{\mathrm{W}}^{(\ell)}$, $d_{\mathrm{L}}^{(\ell)}$.
$-T=\bar{U}+(1+1 / m) B$, where $B=\sum_{\ell=1}^{m}\left(\widehat{\theta}^{(\ell)}-\bar{\theta}\right)\left(\widehat{\theta}^{(\ell)}-\bar{\theta}\right)^{\top} /(m-1)$.
$-\bar{d}_{\mathrm{W}}^{\prime}=\sum_{\ell=1}^{m} d_{\mathrm{W}}\left(\widehat{\theta}^{(\ell)}, \bar{U}\right) / m$ and $\widetilde{d}_{\mathrm{W}}^{\prime}=d_{\mathrm{W}}(\bar{\theta}, \bar{U})$.
$-\widetilde{d}_{\mathrm{L}}=\sum_{\ell=1}^{m} \widetilde{\mathscr{D}}_{\mathrm{L}}\left(X^{(\ell)}, \bar{\psi}_{0}, \bar{\psi}\right) / m$ : an existing pooled LRT statistic.
$-\widehat{d}_{\mathrm{L}}=\mathscr{D}_{\mathrm{L}}\left(X^{(1: m)}\right) / m$ : the proposed pooled LRT statistic.
$-\bar{\delta}_{\mathrm{L}}=\sum_{\ell=1}^{m} \mathscr{D}_{\mathrm{L}, 1}\left(X^{(\ell)}\right) / m$ and $\widehat{\delta}_{\mathrm{L}}=\mathscr{D}_{\mathrm{L}, 1}\left(X^{(1: m)}\right) / m$ : two proposed ways for pooling maximized log-likelihood.
- Estimators of $r_{m}$ :
$-\widetilde{r}_{\mathrm{W}}^{\prime}=(m+1)\left(\bar{d}_{\mathrm{W}}^{\prime}-\widetilde{d}_{\mathrm{W}}^{\prime}\right) /\{k(m-1)\}$ (Rubin, 2004).
$-\widetilde{r}_{\mathrm{L}}=(m+1)\left(\bar{d}_{\mathrm{L}}-\widetilde{d}_{\mathrm{L}}\right) /\{k(m-1)\}$ (Meng and Rubin, 1992).
$-\hat{r}_{\mathrm{L}}^{+}=\max \left[0,(m+1)\left(\bar{d}_{\mathrm{L}}-\widehat{d}_{\mathrm{L}}\right) /\{k(m-1)\}\right]$ : our first proposal.
$-\widehat{r}_{\mathrm{L}}^{\diamond}=(m+1)\left(\bar{\delta}_{\mathrm{L}}-\widehat{\delta}_{\mathrm{L}}\right) /\{h(m-1)\}$ : our second proposal.
- MI Test Statistics for Testing $H_{0}$ against $H_{1}$ :
$-($ WT-1 $) D_{\mathrm{W}}(T)=d_{\mathrm{W}}(\bar{\theta}, T) / k$ : the classical MI Wald test.
$-(\mathrm{LRT}-1) \widetilde{D}_{\mathrm{L}}\left(\widetilde{r}_{\mathrm{L}}\right)=\widetilde{d}_{\mathrm{L}} /\left\{k\left(1+\widetilde{r}_{\mathrm{L}}\right)\right\}$ : the existing MI LRT.
- (LRT-2) $\hat{D}_{\mathrm{L}}\left(\hat{r}_{\mathrm{L}}^{+}\right)=\hat{d}_{\mathrm{L}} /\left\{k\left(1+\hat{r}_{\mathrm{L}}^{+}\right)\right\}$: our first proposal.
$-($ LRT-3 $) \widehat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right)=\widehat{d}_{\mathrm{L}} /\left\{k\left(1+\widehat{r}_{\mathrm{L}}^{\diamond}\right)\right\}$ : our second proposal.


## 4. Empirical Investigation and Findings

### 4.1 Monte Carlo Experiments With EFMI

Let $X_{1}, \ldots, X_{n} \sim \mathcal{N}_{p}(\mu, \Sigma)$ independently, where $\mu=\left(\mu_{1}, \ldots, \mu_{p}\right)^{\top}$. Assume that only $n_{\text {obs }}=\lfloor(1-f) n\rfloor$ data points are observed. Let $X_{\text {obs }}=\left\{X_{i}: i=1, \ldots, n_{\text {obs }}\right\}$ and $X_{\text {mis }}=\left\{X_{i}: i=n_{\text {obs }}+1, \ldots, n\right\}$. We want to test $H_{0}: \mu_{1}=\cdots=\mu_{p}$.

Obviously, one may directly use the observed data set to construct the LRT statistic $D_{\mathrm{L}}$ without MI. Thus, it is regarded as a benchmark (denoted by LRT0 ). The tests WT-1 and LRT-1,2,3 listed in Table 1 are investigated. We perform MI using a Bayesian model with a multivariate Jeffreys prior on ( $\mu, \Sigma$ ), this is, $f(\mu, \Sigma) \propto|\Sigma|^{-(p+1) / 2}$. The imputation procedure is detailed in Appendix A.6. We study the impact of the parametrization on different test statistics.

- Parametrizations of $\theta$ for the Wald tests: (i) $\theta=\left(\mu_{2}-\mu_{1}, \ldots, \mu_{p}-\mu_{p-1}\right)^{\top}$; (ii) $\theta=\left(\mu_{2} / \mu_{1}-1, \ldots, \mu_{p} / \mu_{p-1}-1\right)^{\top}$; and (iii) $\theta=\left(\mu_{2}^{3}-\mu_{1}^{3}, \ldots, \mu_{p}^{3}-\mu_{p-1}^{3}\right)^{\top}$. For any case above, $H_{0}$ can be expressed as $\theta=(0, \ldots, 0)^{\top}$.
- Parametrizations of $\psi$ for LRTs: (i) $\psi=\{\mu$; $\Sigma\}$; (ii) $\psi=\left\{\sqrt{\sigma_{i i}} / \mu_{i}, 1 \leqslant i \leqslant\right. p ; \Sigma\}$; and (iii) $\psi=\left\{\mu^{\top} \Sigma^{-1 / 2} ; \Sigma^{-1}\right\}$, where $\Sigma=\left(\sigma_{i j}\right)$ and $\Sigma^{1 / 2}$ is the square root of $\Sigma$ via the spectral method. The dimension of $\psi$ is $h=\left(p^{2}+3 p\right) / 2$.

We set $\Sigma=\sigma^{2}\left\{(1-\rho) I_{p}+\rho \mathbf{1}_{p} \mathbf{1}_{p}^{\top}\right\}, \mathcal{f}=0.5, p=2, \rho=0.8, \sigma^{2}=5$, and $\mu= (-2+\delta,-2+2 \delta)^{\top}$ for different values of $m \in\{3,10,30\}, n \in\{100,400,1600\}$, and $\delta=\mu_{2}-\mu_{1} \in[0,4]$. All simulations are repeated $2^{12}$ times. The empirical power functions for $\alpha=0.5 \%$ tests are plotted in Figure 2. The results for $\alpha=5 \%$ tests are deferred to Table 10 of the Appendix.

In general, WT-1 exhibits monotonically increasing power as $\delta$ increases, and its performance is affected significantly by parametrization. Indeed, the power can be as low as zero when $1 \lesssim \delta \lesssim 2$ under parametrizations (ii) and (iii). Under parametrization (ii), LRT-1 is not powerful, even for large $\delta$. On the other hand, our first proposed test statistic LRT-2 performs better than LRT-1, at least for large $m$; however, they also lose a significant amount of power when $m$ is small. Our recommended proposal LRT-3 performs best in all cases. The superiority of LRT-3 is particularly striking when $m$ is small, this is, $m=3$.

We also investigate (a) the distribution of the $p$-value, (b) the empirical size $\widehat{\alpha}$ in comparison to the nominal type-I error $\alpha$, (c) the empirical size-adjusted power (Bayarri et al., 2016), (d) the robustness of our proposed estimators of $\mathscr{r}_{m}$, and (e) the performance of other existing MI tests. The results are shown in Appendix A.6. all of which indicate that our proposed tests perform best.

### 4.2 Monte Carlo Experiments Without EFMI

To check how robust various tests are to the assumption of EFMI, we simulate $X_{i}=\left(X_{i 1}, \ldots, X_{i p}\right)^{\top} \sim \mathcal{N}_{p}(\mu, \Sigma)$ independently for $i=1, \ldots, n$. Let $R_{i j}$ be defined by $R_{i j}=1$ if $X_{i j}$ is observed, and $R_{i j}=0$ otherwise. Suppose that the first variable $X_{.1}$ is always observed, and the rest form a monotone missing pattern, as defined by a logistic model on the missing propensity: $\mathrm{P}\left(R_{i j}=0 \mid R_{i, j-1}=a\right)= \left[1+\exp \left(\alpha_{0}+\alpha_{1} X_{i, j-1}\right)\right]^{-1}$ (for $j=2, \ldots, p$ ) when $a=1$. This probability is zero

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-20.jpg?height=1656&width=1255&top_left_y=433&top_left_x=335)
Figure 2: The power curves under nominal size $\alpha=0.5 \%$. In each plot, the vertical axis denotes the power, and the horizontal axis denotes the value of $\delta=\mu_{2}-\mu_{1}$.

when $a=0$ (i.e., nothing is missing). If $\alpha_{1}=0$, the data are missing completely at random (MCAR); otherwise they are missing at random (MAR); see Rubin (1976). The imputation procedure is given in Appendix A.7.

We test $H_{0}: \mu=\mathbf{0}_{p}$ against $H_{1}: \mu \neq \mathbf{0}_{p}$. We set $\mu=\delta \mathbf{1}_{p}$, where $\delta \in[0,0.6] ; \Sigma_{i j}=0.5^{|i-j|}$, for $i, j=1, \ldots, p ; n=500 ; m \in\{3,5\} ; p=5 ;$ and $\left(\alpha_{0}, \alpha_{1}\right) \in \{(2,-1),(1,0)\}$. Our model treats $\Sigma$ as unknown, and hence $k=p$ and $h= \left(3 p+p^{2}\right) / 2$. Under $H_{0}$ and MAR, the FMI, i.e., the eigenvalues of $\mathscr{B}_{\theta} \mathscr{T}_{\theta}^{-1}$, are ( $0,19 \%, 34 \%, 45 \%, 55 \%$ ). Thus, the assumption of EFMI does not hold.

In this experiment, we also compare the performance of WT-1 and LRT-1,2,3. For reference, the complete-case (asymptotic) LRT using $\left\{X_{i}: R_{i 1}=\cdots=R_{i p}=1\right\}$, denoted by LRT-0, is also computed. The results are shown in Figure 3. The size of LRT-3 is accurate when the nominal size is small. If the data are MCAR, LRT-0 is valid, but with slightly less power. (LRT-0 is typically invalid without MCAR.) The test LRT-3 has the best power-to-size ratio among all other tests. The power-to-size ratio of LRT-2 and LRT-3 become closer to the nominal value $1 / 0.5 \%=200$ as $m$ increases. These results indicate that our proposed tests perform well and best, despite the serious violation of the EFMI assumption.

## 5. Conclusion, Limitation and Future Work

In addition to conducting a general comparative study of MI tests, we have proposed two particularly promising MI LRTs based on $\widehat{D}_{\mathrm{L}}^{\diamond}=\widehat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right)$ and $\widehat{D}_{\mathrm{L}}^{+}=\widehat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}^{+}\right)$. Both test statistics are non-negative, invariant to parametrizations, and powerful to reject a false $H_{0}$ (at least for large enough $m$ ). The test $\hat{D}_{\mathrm{L}}^{\diamond}$ is the most principled, and has desirable monotonically increasing power as $H_{1}$ departs from $H_{0}$. However, it is derived under the stronger assumption of EFMI for $\psi$, not just for $\theta$. Furthermore, row independence of $X_{\text {com }}$ is needed for ease of computation. (With a slightly more computationally demanding requirement, $\widehat{D}_{\mathrm{L}}\left(\widehat{r}_{\mathrm{L}}^{\diamond}\right)$ can be used without the independence assumption.) The main advantage of $\widehat{D}_{\mathrm{L}}^{+}$is that it is easier to compute, because it requires only standard complete-data computer subroutines for LRTs. One drawback is that the ad hoc fix $\hat{r}_{\mathrm{L}}^{+}=\max \left(0, \hat{r}_{\mathrm{L}}\right)$ is inconsistent, in general. However, the inconsistency does not significantly affect the asymptotic power, at least in our experiments. Although $\widehat{D}_{\mathrm{L}}^{+}$and $\widehat{D}_{\mathrm{L}}^{\diamond}$ offer significant improvements over existing options, more research is needed, for the reasons listed below:

- When the missing-data mechanism is not ignorable, but the imputers fail to fully take that into account, the issue of uncongeniality becomes critical (Meng, 1994a). Xie and Meng (2017) provide theoretical tools to address this issue in the context of estimation, and research is needed to extend their findings to the setting of hypothesis testing.

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-22.jpg?height=982&width=1376&top_left_y=391&top_left_x=281)
Figure 3: The empirical size, empirical power, and their ratio. The first row of plots show the empirical sizes. The size of the complete-case test (C2) under MAR is off the chart (always equal to one) because it is invalid. The second and third rows of plots show the powers and the power-to-size ratios, respectively. The nominal size is $0.5 \%$.

- Violating the EFMI assumption may not invalidate a test, but it will affect its power. Thus, it is desirable to explore MI tests without assuming EFMI.
- The robust $\widehat{D}_{\mathrm{L}}^{\diamond}$ relies on a stronger assumption of EFMI on $\psi$. We can modify it so only EFMI on $\theta$ is required, but the modification may be very difficult to compute, and may require that users have access to nontrivial complete-data procedures. Hence, a computationally feasible robust test that only assumes EFMI on $\theta$ needs to be developed.
- Because the FMI is a fundamental nuisance parameter and there is no (known) pivotal quantity, all MI tests are just approximations. If FMI is large or $m$ is small, they may perform poorly. Thus, seeking powerful MI tests that are least affected by FMI is of both theoretical and practical interest.


## Supplementary Material

Appendix A contains additional theoretical results and details of numerical examples. Appendix B contains proofs of the main results. The R code is provided online.

## Acknowledgments

Meng thanks the NSF and JTF for their partial financial support. He is also grateful for Keith's (Kin Wai's) creativity and diligence, which led to the remedies presented here, and which are also a part of Keith's thesis. Chan thanks the University Grant Committee of HKSAR for its partial financial support.

## References

Barnard, J. and Rubin, D. B. (1999) Small-sample degrees of freedom with multiple imputation. Biometrika, 86, 948-955.
Bayarri, M. J., Benjamin, D. J., Berger, J. O. and Sellke, T. M. (2016) Rejection odds and rejection ratios: A proposal for statistical practice in testing hypotheses. Journal of Mathematical Psychology, 72, 90-103.
Benjamin, D. J., Berger, J. O., Johannesson, M., Nosek, B. A., Wagenmakers, E.-J., Berk, R., Bollen, K. A., Brembs, B., Brown, L., Camerer, C. et al. (2018) Redefine statistical significance. Nature Human Behaviour, 2, 6-10.
Berger, J. O. (1985) Statistical Decision Theory and Bayesian Analysis. Springer-Verlag New York.
Berglund, P. and Heeringa, S. G. (2014) Multiple imputation of missing data using SAS. SAS Institute, Cary.
Blocker, A. W. and Meng, X.-L. (2013) The potential and perils of preprocessing: Building new foundations. Bernoulli, 19, 1176-1211.
Carlin, J. B., Galati, J. C. and Royston, P. (2008) A new framework for managing and analyzing multiply imputed data in stata. The Stata Journal, 8, 49-67.
Chan, K. W. (2021) General and feasible tests with multiply-imputed datasets. Ann. Statist. (to appear).
Cox, D. R. and Reid, N. (1987) Parameter orthogonality and approximate conditional inference. Journal of the Royal Statistical Society B, 49, 1-39.
Dagenais, M. G. and Dufour, J.-M. (1991) Invariance, nonlinear models, and asymptotic tests. Econometrica, 59, 1601-1615.
Grund, S., Robitzsch, A. and Luedtke, O. (2017) Tools for Multiple Imputation in Multilevel Modeling.
Harel, O. and Zhou, X.-H. (2007) Multiple imputation - review of theory, implementation and software. Statistics in medicine, 26, 3057-3077.
Holan, S. H., Toth, D., Ferreira, M. A. R. and Karr, A. F. (2010) Bayesian multiscale multiple imputation with implications for data confidentiality. Journal of the American Statistical Association, 105, 564-577.
Horton, N. and Kleinman, K. P. (2007) Much ado about nothing: A comparison of missing data methods and software to fit incomplete data regression models. The American Statistician, 61, 79-90.

## REFERENCES

Kenward, M. G. and Carpenter, J. R. (2007) Multiple imputation: current perspectives. Statistical Methods in Medical Research, 16, 199-218.
Kim, J. K. and Shao, J. (2013) Statistical Methods for Handling Incomplete Data. Chapman and Hall/CRC, Boca Raton.
Kim, J. K. and Yang, S. (2017) A note on multiple imputation under complex sampling. Biometrika, 104, 221-228.
King, G., Honaker, J., Joseph, A. and Scheve, K. (2001) Analyzing incomplete political science data: An alternative algorithm for multiple imputation. American Political Science Review, 95, 49-69.
Lehmann, E. L. and Casella, G. (1998) Theory of Point Estimation. Springer-Verlag New York.
Li, K. H., Meng, X.-L., Raghunathan, T. E. and Rubin, D. B. (1991a) Significance levels from repeated $p$-values with multiply-imputed data. Statistica Sinica, 1, 65-92.
Li, K. H., Raghunathan, T. E. and Rubin, D. B. (1991b) Large-sample significance levels from multiply imputed data using moment-based statistics and an $F$ reference distribution. Journal of the American Statistical Association, 86, 1065-1073.
Little, R. J. A. and Rubin, D. B. (2002) Statistical analysis with missing data. Wiley, New York.
Medeiros, R. (2008) Likelihood ratio tests for multiply imputed datasets: Introducing milrtest.
Meng, X.-L. (1994a) Multiple-imputation inferences with uncongenial sources of input. Statistical Science, 9, 538-573.
Meng, X.-L. (1994b) Posterior predictive $p$-values. The Annals of Statistics, 22, 1142-1160.
Meng, X.-L. (2002) Discussion of "Bayesian measures of model complexity and fit" by Spiegelhalter, D. J., Best, N. G., Carlin, B. P. and Van Der Linde, A. Journal of the Royal Statistical Society B, 64, 633.
Meng, X.-L. and Rubin, D. B. (1992) Performing likelihood ratio tests with multiplyimputed data sets. Biometrika, 79, 103-111.
Peugh, J. L. and Enders, C. K. (2004) Missing data in educational research: A review of reporting practices and suggestions for improvement. Review of Educational Research, 74, 525-556.
Rose, R. A. and Fraser, M. W. (2008) A simplified framework for using multiple imputation in social work research. Social Work Research, 32, 171-178.
Royston, P. and White, I. R. (2011) Multiple imputation by chained equations (mice): Implementation in stata. Journal of Statistical Software, 45, 1-20.
Rubin, D. B. (1976) Inference and missing data. Biometrika, 63, 581-592.
Rubin, D. B. (1978) Multiple imputations in sample surveys - a phenomenological Bayesian approach to nonresponse. Proceedings of the Survey Research Methods Section of the American Statistical Association, 20-34.
Rubin, D. B. (1996) Multiple imputation after 18+ years. Journal of the American statistical Association, 91, 473-489.
Rubin, D. B. (2004) Multiple Imputation for Nonresponse in Surveys. Wiley, New York.
Rubin, D. B. and Schenker, N. (1986) Multiple imputation for interval estimation from
simple random samples with ignorable nonresponse. Journal of the American Statistical Association, 81, 366-374.
Schafer, J. L. (1999) Multiple imputation: A primer. Statistical Methods in Medical Research, 8, 3-15.
Serfling, R. J. (2001) Approximation Theorems of Mathematical Statistics. Wiley, New York.
Shao, J. (1998) Mathematical Statistics. Springer-Verlag New York.
Su, Y.-S., Gelman, A., Hill, J. and Yajima, M. (2011) Multiple imputation with diagnostics (mi) in R: Opening windows into the black box. Journal of Statistical Software, 45, 1-31.
Tu, X. M., Meng, X.-L. and Pagano, M. (1993) The AIDS epidemic: Estimating survival after AIDS diagnosis from surveillance data. Journal of the American Statistical Association, 88, 26-36.
van Buuren, S. and Groothuis-Oudshoorn, K. (2011) Mice: Multivariate imputation by chained equations in R. Journal of Statistical Software, 45, 1-67.
van Buuren S (2012) Flexible Imputation of Missing Data. Chapman and Hall/CRC.
van der Vaart, A. W. (2000) Asymptotic Statistics. Cambridge University Press, Cambridge.
Wallace, D. L. (1980) The Behrens-Fisher and Fieller-Creasy problems. In R. A. Fisher: An Appreciation (eds. S. E. Fienberg and D. V. Hinkley), 119-147. Springer New York.
Wang, N. and Robins, J. M. (1998) Large-sample theory for parametric multiple imputation procedures. Biometrika, 85, 935-948.
Xie, X. and Meng, X.-L. (2017) Dissecting multiple imputation from a multi-phase inference perspective: What happens when God's, imputer's and analyst's models are uncongenial? (with discussion). Statistica Sinica, 27, 1485-1594.

Department of Statistics, The Chinese University of Hong Kong.
E-mail: kinwaichan@cuhk.edu.hk
Department of Statistics, Harvard University.
E-mail: meng@stat.harvard.edu

## Supplementary Material

## A. Supplementary Results

## A. 1 A Complication Caused by Nuisance Parameter

This section supplement the discussion of Section 2.2 in the main article. Recall that the likelihood function $L^{(\ell)}(\cdot)$ is based on both observed data $X_{\text {obs }}$ and imputed data $X_{\text {mis }}^{(\ell)}$, which varies across $\ell$. Hence, each imputed likelihood $L^{(\ell)}(\cdot)$ is associated with a (imputation-specific) pseudo parameter $\psi^{(\ell)}$, may vary across $\ell=1, \ldots, m$.

To see the source of the negativity of $\widehat{r}_{\mathrm{L}}$, we extend $\bar{L}(\psi)$ in 2.1 to

$$
\bar{L}\left(\psi^{(1)}, \ldots, \psi^{(m)}\right)=\frac{1}{m} \sum_{\ell=1}^{m} L^{(\ell)}\left(\psi^{(\ell)}\right) .
$$

Using the "log-likelihood" $\bar{L}\left(\psi^{(1)}, \ldots, \psi^{(m)}\right)$, we can construct, at least conceptually, four hypotheses $H_{0}^{0}, H_{0}^{1}, H_{1}^{0}, H_{1}^{1}$ defined in Table 2. Each of them consists of zero, one or two of the constraints $\mathscr{C}_{0}: \theta^{(1)}=\cdots=\theta^{(m)}=\theta_{0}$ and $\mathscr{C}^{0}: \psi^{(1)}=\cdots=\psi^{(m)}$, where $\theta^{(\ell)}=\theta\left(\psi^{(\ell)}\right)$ is the interested part of $\psi^{(\ell)}$ for each $\ell$. The constraint $\mathscr{C}_{0}$ is equivalent to $H_{0}$, and the constraint $\mathscr{C}^{0}$ means that all $\psi^{(\ell)}$ s are equal, and hence it is effectively equivalent to $r=0$, i.e., no missing information. The relationships among $H_{0}^{0}, H_{0}^{1}, H_{1}^{0}, H_{1}^{1}$ can be visualized in Figure 5. Define the maximized value of $\bar{L}\left(\psi^{(1)}, \ldots, \psi^{(m)}\right)$ under hypothesis $H \in\left\{H_{0}^{0}, H_{0}^{1}, H_{1}^{0}, H_{1}^{1}\right\}$ by $\mathbb{L}(H)$. Then we can re-express $\left(\bar{d}_{\mathrm{L}}-\widehat{d}_{\mathrm{L}}\right) / 2$ as

$$
\left(\bar{d}_{\mathrm{L}}-\widehat{d}_{\mathrm{L}}\right) / 2=\left\{\mathbb{L}\left(H_{1}^{1}\right)-\mathbb{L}\left(H_{1}^{0}\right)\right\}-\left\{\mathbb{L}\left(H_{0}^{1}\right)-\mathbb{L}\left(H_{0}^{0}\right)\right\}
$$

Whereas the two bracketed terms in A.2 are non-negative as they correspond to two LRT statistics, their difference can be negative.

A simple example illustrates this well. For the regression model $[Y \mid \left.X_{1}, X_{2}\right] \sim \mathcal{N}\left(\beta_{0}+\beta_{1} X_{1}+\beta_{2} X_{2}, \sigma^{2}\right)$, the LRT statistic for testing $H_{1}^{0}: \beta_{1}=$ 0 , $\beta_{2} \in \mathbb{R}$ against $H_{1}^{1}: \beta_{1}, \beta_{2} \in \mathbb{R}$ is not necessarily larger (or smaller) than that for testing $H_{0}^{0}: \beta_{1}=\beta_{2}=0$ against $H_{0}^{1}: \beta_{1} \in \mathbb{R}, \beta_{2}=0$; see Figure 4 for a schematic illustration.

The decomposition (A.2) provides another interpretation of $\widehat{r}_{\mathrm{L}}$. The test statistic $\mathbb{L}\left(H_{1}^{1}\right)-\mathbb{L}\left(H_{1}^{0}\right)$ seeks evidence for detecting the falsity of $\mu=0$ in both $\theta$ and $\eta$, whereas $\mathbb{L}\left(H_{0}^{1}\right)-\mathbb{L}\left(H_{0}^{0}\right)$ seeks evidence only in $\eta$. For cases where $\theta$ and $\eta$ are orthogonal (at least locally), the left-hand side of A.2)

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-27.jpg?height=414&width=753&top_left_y=388&top_left_x=590)
Figure 4: A schematic illustration of the sign of (A.2). The contour lines of $\bar{L}\left(\psi^{(1)}, \ldots, \psi^{(m)}\right)$ are plotted. The two straight lines refer to constraints $\mathscr{C}_{0}$ and $\mathscr{C}^{0}$. Since $\mathbb{L}\left(H_{1}^{1}\right)=0.082, \mathbb{L}\left(H_{0}^{1}\right)=\mathbb{L}\left(H_{1}^{0}\right)=0.08$, and $\mathbb{L}\left(H_{0}^{0}\right)=0.01$, we have $\left\{\mathbb{L}\left(H_{1}^{1}\right)-\mathbb{L}\left(H_{1}^{0}\right)\right\}-\left\{\mathbb{L}\left(H_{0}^{1}\right)-\mathbb{L}\left(H_{0}^{0}\right)\right\}=0.002-0.007<0$. Note that the function $\bar{L}\left(\psi^{(1)}, \ldots, \psi^{(m)}\right)$ in A.1 is at least 4-dimensional (i.e., $\theta^{(1)}, \theta^{(2)}, \eta^{(1)}, \eta^{(2)}$ ) generally, so this illustration in a 2 -dimension space is just conceptual.

Table 2: The definitions of hypotheses $H_{0}^{0}, H_{0}^{1}, H_{1}^{0}, H_{1}^{1}$.
|  | $\mathscr{C}^{0}: \psi^{(1)}=\cdots=\psi^{(m)} \in \Psi$ <br> (i.e., $\boldsymbol{r}=0$ ) | $\begin{gathered} \mathscr{C}^{1}: \psi^{(1)}, \ldots, \psi^{(m)} \in \Psi \\ \text { (i.e., } \boldsymbol{r} \geqslant 0) \end{gathered}$ |
| :--- | :--- | :--- |
| $\mathscr{C}_{0}: \theta^{(1)}=\cdots=\theta^{(m)}=\theta_{0} \in \Theta$ <br> (i.e., $H_{0}$-constrained) | $H_{0}^{0}=\mathscr{C}_{0} \cap \mathscr{C}^{0}$ | $H_{0}^{1}=\mathscr{C}_{0} \cap \mathscr{C}^{1}$ |
| $\mathscr{C}_{1}: \theta^{(1)}, \ldots, \theta^{(m)} \in \Theta$ <br> (i.e., not $H_{0}$-constrained) | $H_{1}^{0}=\mathscr{C}_{1} \cap \mathscr{C}^{0}$ | $H_{1}^{1}=\mathscr{C}_{1} \cap \mathscr{C}^{1}$ |


![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-27.jpg?height=214&width=373&top_left_y=1705&top_left_x=786)
Figure 5: The relationships between the four hypotheses $H_{0}^{0}, H_{0}^{1}, H_{1}^{0}, H_{1}^{1}$. Each arrow denotes an implication, e.g., $H_{0}^{0} \Rightarrow H_{0}^{1}$ means that $H_{0}^{0}$ implies $H_{0}^{1}$.

can be viewed as a measure of evidence against $r=0$ solely from $\theta$; Proposition 1 already hinted this possibility. However, the "test statistic" A.2 has a fatal flaw. Because $\mathscr{C}_{0}$ requires all $\theta^{(\ell)}$ s to coincide with a specific $\theta_{0}, \mathscr{C}_{0}$ is not nested within $\mathscr{C}^{0}$, i.e., $\mathscr{C}^{0} \nRightarrow \mathscr{C}_{0}$. Hence $\hat{r}_{\mathrm{L}}$ is guaranteed to consistently estimate $\mathcal{r}_{m}$ only under $H_{0}$. This explains Corollary 1, and leads to an im-
provement in Section 2.2. In it not hard to see that our new estimator $\widehat{r}_{\mathrm{L}}^{\widehat{ }}$ simply drops the second term in (A.2).

## A. 2 Another Motivation for $\widehat{r_{\mathrm{L}}}$

The definition of $\widehat{r}_{\mathrm{L}}$ can also be motivated by the following observation. First, observe that one simple method to construct an always non-negative estimator of $\varkappa_{m}$ is to perturb $\hat{\psi}_{0}^{*}$ and $\hat{\psi}_{0}^{(\ell)}$ by a suitable amount, say $\Delta$, so that the perturbed version of $\widehat{r}_{\mathrm{L}}$ is always non-negative, and is still asymptotically equivalent to the original $\widehat{r}_{\mathrm{L}}$. We show, in Theorem 5 below, that the right amount of $\Delta$ is $\Delta=\widehat{\psi}^{*}-\widehat{\psi}_{0}^{*}$. Using the perturbed version of $\widehat{r}_{\mathrm{L}}$, we obtain

$$
\widehat{r}_{\mathrm{L}}^{\triangle}=\frac{m+1}{k(m-1)} \widehat{\delta}_{\mathrm{L}}^{\triangle}
$$

where
$\widehat{\delta}_{\mathrm{L}}^{\Delta}=\frac{2}{m} \sum_{\ell=1}^{m} \log \left\{\frac{f\left(X^{(\ell)} \mid \widehat{\psi}^{(\ell)}\right)}{f\left(X^{(\ell)} \mid \widehat{\psi}^{*}\right)} \frac{f\left(X^{(\ell)} \mid \widehat{\psi}_{0}^{*}+\Delta\right)}{f\left(X^{(\ell)} \mid \widehat{\psi}_{0}^{(\ell)}+\Delta\right)}\right\}=\frac{1}{m} \sum_{\ell=1}^{m} d_{\mathrm{L}}\left(\widehat{\psi}_{0}^{(\ell)}+\Delta, \widehat{\psi}^{(\ell)} \mid X^{(\ell)}\right)$.
Then we have the following result.
Theorem 5. Suppose $\mathrm{RC}_{\theta}$. Under $H_{0}$, we have (i) $\widehat{r}_{\mathrm{L}}^{\triangle} \geqslant 0$ for all $m, n$; and (ii) $\widehat{r}_{\mathrm{L}}^{\triangle} \bumpeq \widehat{r}_{\mathrm{L}}$ as $n \rightarrow \infty$ for each $m$.

Although $\widehat{r}_{\mathrm{L}}^{\perp} \geqslant 0$, it is only invariant to affine transformations, and not robust against $\theta_{0}$, and less computational feasible than $\widehat{r}_{\mathrm{L}}$; see Section 3. However, it gives us some insights on how to construct a potentially better estimator. Note that, in (A.3), the constrained MLE is not used in $d_{\mathrm{L}}\left(\cdot, \cdot \mid X^{(\ell)}\right)$, but it is still always non-negative. We call this a "pseudo" LRT statistics. Then, $\widehat{\delta}_{\mathrm{L}}^{\triangle}$ is just a multiple of an average of many "pseudo" LRT statistics. In order to find a good estimator of $\varkappa_{m}$, we may seek for an estimator which admits this form. Indeed, our estimator $\widehat{r}_{\mathrm{L}}^{\diamond}$ also takes the same form:

$$
\widehat{r}_{\mathrm{L}}^{\widehat{\mathrm{L}}}=\frac{m+1}{h(m-1)} \frac{1}{m} \sum_{\ell=1}^{m} d_{\mathrm{L}}\left(\widehat{\psi}^{*}, \widehat{\psi}^{(\ell)} \mid X^{(\ell)}\right)
$$

## A. 3 Additional result for Section 2.3

This section presents the additional simulation result for Section 2.3. The performance of different approximations to the reference null distribution when $\alpha=5 \%$ is shown in Figure 6.

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-29.jpg?height=798&width=1284&top_left_y=421&top_left_x=326)
Figure 6: The performance of two approximate null distributions when the nominal size is $\alpha=5 \%$. The vertical axis denotes $\widehat{\alpha}$ or $\widetilde{\alpha}$, and the horizontal axis denotes the value of $f_{m}$. The number attached to each line denotes the value of $\tau=h / k$. The proposed approximation $\hat{\alpha}$ is denoted by thick solid lines with triangles, and the existing approximation $\widetilde{\alpha}$ is denoted by thin dashed lines with circles.

## A. 4 Results for Dependent Data

This is a supplement for Section 3.1. If the data are not independent, then A.5 is no longer true. In other words, $\bar{L}(\psi) \not \equiv \bar{L}^{\mathrm{S}}(\psi)$, where $\bar{L}(\psi)= \sum_{\ell=1}^{m} L^{(\ell)}(\psi) / m$ is defined in (2.1), and

$$
\bar{L}^{\mathrm{S}}(\psi)=\frac{1}{m} \log f_{m n}\left(X^{(1: m)} \mid \psi\right) .
$$

In principle, $\bar{L}(\psi)$ should be used instead of the "stacked version" $\bar{L}^{\mathrm{S}}(\psi)$, however, the stacked one is much easier to compute. Because of this reason, it is of interest to see whether the stacked version can be used generally.

To begin with, we define the stacked version of all MI statistics when
$\bar{L}^{\mathrm{S}}(\psi)$ is used instead of $\bar{L}(\psi)$. Let

$$
\begin{array}{rlrl}
\widehat{\psi}_{0}^{\mathrm{S}} & =\underset{\psi \in \Psi: \theta(\psi)=\theta_{0}}{\arg \max } \bar{L}^{\mathrm{S}}(\psi), & & \widehat{\psi}^{\mathrm{S}}=\underset{\psi \in \Psi}{\arg \max } \bar{L}^{\mathrm{S}}(\psi) ; \\
\widehat{\delta}_{0, \mathrm{~S}} & =2 \bar{L}^{\mathrm{S}}\left(\widehat{\psi}_{0}^{\mathrm{S}}\right), & \widehat{\delta}_{\mathrm{S}}=2 \bar{L}^{\mathrm{S}}\left(\widehat{\psi}^{\mathrm{S}}\right) .
\end{array}
$$

and

$$
\begin{aligned}
\hat{D}_{\mathrm{S}}\left(\varkappa_{m}\right) & =\frac{\hat{d}_{\mathrm{S}}}{k\left(1+\varkappa_{m}\right)}, & & \text { with } \hat{d}_{\mathrm{S}}=\hat{\delta}_{\mathrm{S}}-\hat{\delta}_{0, \mathrm{~S}} \text { of A.5 } \\
\hat{r}_{\mathrm{S}} & =\frac{m+1}{k(m-1)}\left(\bar{d}_{\mathrm{S}}-\hat{d}_{\mathrm{S}}\right), & & \text { with } \bar{d}_{\mathrm{S}}=\bar{d}_{\mathrm{L}} \text { of 1.7); } \\
\widehat{r}_{\mathrm{S}} & =\frac{m+1}{h(m-1)}\left(\bar{\delta}_{\mathrm{S}}-\widehat{\delta}_{\mathrm{S}}\right), & & \text { with } \bar{\delta}_{\mathrm{S}}=\bar{\delta}_{\mathrm{L}} \text { of 2.10; }
\end{aligned}
$$

and $\widehat{r}_{\mathrm{S}}^{+}=\max \left(0, \widehat{r}_{\mathrm{S}}\right)$. The stacked counterparts of $\widehat{D}_{\mathrm{L}}^{\diamond}$ and its existing counterparts $\widehat{D}_{\mathrm{L}}$ and $\widehat{D}_{\mathrm{L}}^{+}$(see 2.11) then are given by

$$
\hat{D}_{\mathrm{S}}^{\diamond}=\hat{D}_{\mathrm{S}}\left(\widehat{r}_{\mathrm{S}}^{\widehat{\mathrm{S}}}\right), \quad \hat{D}_{\mathrm{S}}=\hat{D}_{\mathrm{S}}\left(\hat{r}_{\mathrm{S}}\right), \quad \hat{D}_{\mathrm{S}}^{+}=\hat{D}_{\mathrm{S}}\left(\hat{r}_{\mathrm{S}}^{+}\right)
$$

The approximation $\widehat{d}_{\mathrm{L}} \bumpeq \widehat{d}_{\mathrm{S}}$ is still true under the following conditions.
Assumption 5. (a) Define $R(\psi)=\underline{\bar{L}}^{\mathrm{S}}(\psi)-\underline{\bar{L}}(\psi)$, where

$$
\underline{\bar{L}}(\psi)=(m n)^{-1} \sum_{\ell=1}^{m} \log f\left(X^{(\ell)} \mid \psi\right) \quad \text { and } \quad \underline{\bar{L}}^{\mathrm{S}}(\psi)=(m n)^{-1} \log f\left(X^{\mathrm{S}} \mid \psi\right) .
$$

For each $m$, as $n \rightarrow \infty$,

$$
\sup _{\psi \in \Psi}|R(\psi)|=O_{p}(1 / n), \quad \sup _{\psi \in \Psi}\left|\frac{\partial}{\partial \psi} R(\psi)\right|=O_{p}(1 / n) .
$$

(b) For each $m$, there exists a continuous function $\psi \mapsto \overline{\mathscr{L}}(\psi)$, which is free of $n$ but may depend on $m$, such that, as $n \rightarrow \infty$,

$$
\sup _{\psi \in \Psi}|\underline{\bar{L}}(\psi)-\underline{\overline{\mathscr{L}}}(\psi)|=o_{p}(1)
$$

(c) Let $\psi_{0}^{*}=\arg \max _{\psi \in \Psi: \psi(\theta)=\theta_{0}} \overline{\mathscr{L}}(\psi)$ and $\psi^{*}=\arg \max _{\psi \in \Psi} \overline{\mathscr{L}}(\psi)$. For any fixed $m$, and for all $\varepsilon>0$, there exists $\delta>0$ such that

$$
\sup _{\substack{\psi \in \Psi:\left|\psi_{0}^{*}-\psi\right|>\varepsilon \\ \theta(\psi)=\theta_{0}}}\left\{\overline{\mathscr{L}}\left(\psi_{0}^{*}\right)-\overline{\mathscr{L}}(\psi)\right\} \geqslant \delta, \sup _{\psi \in \Psi:\left|\psi^{*}-\psi\right|>\varepsilon}\left\{\overline{\mathscr{L}}\left(\psi^{*}\right)-\overline{\mathscr{L}}(\psi)\right\} \geqslant \delta .
$$

Conditions (b) and (c) in Assumption 5 are standard RCs that are usually assumed for M-estimators (see Section 5 of van der Vaart (2000)); whereas condition (a) is satisfied by many models (see Example A.1 below).
Theorem 6. Suppose $\mathrm{RC}_{\theta}$ and Assumption 5. Under both $H_{0}$ and $H_{1}$, we have (i) $\hat{d}_{\mathrm{S}}, \hat{r}_{\mathrm{S}} \geqslant 0$ for all $m, n$; (ii) $\hat{d}_{\mathrm{S}}, \hat{r}_{\mathrm{S}}$ are invariant to the parametrization of $\psi$ for all $m, n$; and (iii) $\hat{d}_{\mathrm{L}} \bumpeq \hat{d}_{\mathrm{S}}$ and $\hat{r}_{\mathrm{L}} \bumpeq \hat{r}_{\mathrm{S}}$ as $n \rightarrow \infty$ for each $m$.

Theorem 6 implies that the handy test statistics $\hat{D}_{\mathrm{S}}$ and $\hat{D}_{\mathrm{S}}^{+}$approximate $\widehat{D}_{\mathrm{L}}$ and $\widehat{D}_{\mathrm{L}}^{+}$for dependent data, provided that Assumption 5 holds.
Example A.1. Consider a stationary autoregressive model of order one. Suppose the complete data $X=\left(X_{1}, \ldots, X_{n}\right)^{\top}$ is generated as following: $X_{1} \sim \mathscr{N}\left(0, v^{2}\right)$ and $\left[X_{i} \mid X_{i-1}\right] \sim \mathscr{N}\left(\phi X_{i-1}, \sigma^{2}\right)$ for $i \geqslant 2$, where $v^{2}=\sigma^{2}(1+\phi) /(1-\phi)$. Then $\psi=\left(\phi, \sigma^{2}\right)^{\top}$, and

$$
\begin{aligned}
\underline{\bar{L}}(\psi)= & -\frac{1}{2} \log (2 \pi)-\frac{1}{2 n} \log v^{2}-\frac{1}{m n} \sum_{\ell=1}^{m} \frac{X_{1}^{(\ell)}}{2 v^{2}}-\frac{n-1}{2 n} \log \sigma^{2} \\
& -\frac{1}{m n} \sum_{\ell=1}^{m} \sum_{i=2}^{n} \frac{\left(X_{i}^{(\ell)}-\phi X_{i-1}^{(\ell)}\right)^{2}}{2 \sigma^{2}} \\
\underline{\bar{L}}^{\mathrm{S}}(\psi)= & -\frac{1}{2} \log (2 \pi)-\frac{1}{2 m n} \log v^{2}-\frac{\left(X_{1}^{(1)}\right)^{2}}{2 m n v^{2}}-\frac{m n-1}{2 m n} \log \sigma^{2} \\
& -\frac{1}{m n} \sum_{\ell=1}^{m} \sum_{i=2}^{n} \frac{\left(X_{i}^{(\ell)}-\phi X_{i-1}^{(\ell)}\right)^{2}}{2 \sigma^{2}}-\frac{1}{m n} \sum_{\ell=2}^{m} \frac{\left(X_{1}^{(\ell)}-\phi X_{n}^{(\ell-1)}\right)^{2}}{2 \sigma^{2}} .
\end{aligned}
$$

Then, it is easy to see that condition (a) of Assumption 5 is satisfied.

## A. 5 Other existing MI tests

First, we list some existing estimators of $\varkappa_{m}$. Let $s_{\mathrm{W}, a}^{2}$ be the sample variances of $\left\{\left(d_{\mathrm{W}}^{(\ell)}\right)^{a}\right\}_{\ell=1}^{m}$ for $a>0$. Rubin (2004) and Li et al. (1991a) proposed

$$
\begin{aligned}
\tilde{r}_{\mathrm{W}, 1} & =\frac{(1+1 / m) s_{\mathrm{W}, 1}^{2}}{2 \bar{d}_{\mathrm{W}}+\sqrt{\max \left\{0,4 \bar{d}_{\mathrm{W}}^{2}-2 k s_{\mathrm{W}, 1}^{2}\right\}}} \\
\tilde{r}_{\mathrm{W}, 1 / 2} & =(1+1 / m) s_{\mathrm{W}, 1 / 2}^{2}
\end{aligned}
$$

respectively. When $k$ is large and $m$ is small, using (A.10) or A.11) may lead to power loss. A trivial modification of $\widetilde{r}_{\mathrm{L}}$ of (1.8), i.e., $\widetilde{r}_{\mathrm{L}}^{+}=\max \left(0, \widetilde{r}_{\mathrm{L}}\right)$, is a better alternative.

Second, we list some alternative MI combining rules. Having the above estimators of $\varkappa_{m}$, we can insert them into the following combining rules:

$$
\widetilde{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)=\frac{\widetilde{d}_{\mathrm{W}}^{\prime}}{k\left(1+\varkappa_{m}\right)}, \widetilde{D}_{\mathrm{L}}\left(\varkappa_{m}\right)=\frac{\widetilde{d}_{\mathrm{L}}}{k\left(1+\varkappa_{m}\right)}, \widetilde{D}_{\mathrm{L}}^{+}\left(\varkappa_{m}\right)=\left\{\widetilde{D}_{\mathrm{L}}\left(\varkappa_{m}\right)\right\}^{+}
$$

Using (1.3) and (1.8), we can also define the following combining rules:

$$
\bar{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)=\frac{\bar{d}_{\mathrm{W}}^{\prime}-\frac{k(m-1)}{m+1} \varkappa_{m}}{k\left(1+\varkappa_{m}\right)}, \quad \bar{D}_{\mathrm{L}}\left(\varkappa_{m}\right)=\frac{\bar{d}_{\mathrm{L}}-\frac{k(m-1)}{m+1} \varkappa_{m}}{k\left(1+\varkappa_{m}\right)} ;
$$

see, e.g., Li et al. (1991a). The combining rule $\bar{D}_{\mathrm{W}}^{\prime}\left(v_{m}\right)$ is useful when computing $\bar{d}_{\mathrm{W}}^{\prime}$ and estimating $r_{m}$ are simple, but the resulting power may deteriorate. If $\widetilde{r}_{\mathrm{W}, 1}$ or $\widetilde{r}_{\mathrm{W}, 1 / 2}$ is used for estimating $r_{m}$, the null distribution of A.12 and A.13 can be approximated by $F_{k, \widetilde{\mathrm{df}}^{\prime}\left(r_{m}, k\right)}$, where $\widetilde{\mathrm{df}}^{\prime}\left(r_{m}, k\right)= (m-1)\left(1+\varkappa_{m}^{-1}\right)^{2} k^{-3 / m}$; see Li et al. 1991a).

Next, we introduce and recall some notation: (a) standard complete-data moments estimation ( $\mathscr{M}_{\mathrm{W}}, \mathscr{M}_{\mathrm{L}}$ ) and testing procedures ( $\mathscr{D}_{\mathrm{W}}, \mathscr{D}_{\mathrm{L}}$ ), and (b) non-standard complete-data procedures ( $\widetilde{\mathscr{D}}_{\mathrm{L}}, \overline{\mathscr{D}}_{\mathrm{L}}, \mathscr{D}_{\mathrm{L}, 1}, \overline{\mathscr{D}}_{\mathrm{L}, 1}$ ), where

$$
\begin{gathered}
\mathscr{M}_{\mathrm{W}}(X)=\{\hat{\theta}(X), U(X)\}, \quad \mathscr{M}_{\mathrm{L}}(X)=\left\{\widehat{\psi}(X), \hat{\psi}_{0}(X)\right\} \\
\mathscr{D}_{\mathrm{W}}(X)=d_{\mathrm{W}}(\hat{\theta}(X), U(X)), \quad \overline{\mathscr{D}}_{\mathrm{L}, 1}(\mathbb{X})=\frac{2}{m} \sum_{\ell=1}^{m} \log f\left(X^{(\ell)} \mid \hat{\psi}^{*}(\mathbb{X})\right) \\
\bar{L}(\psi)=\frac{1}{m} \log f_{m n}\left(X^{(1: m)} \mid \psi\right)
\end{gathered}
$$

Table 3 is the full version of Table 1 in the main text. It summarizes the statistical and computational properties of different MI tests; see Section 3.2 for details.

Table 3: Computational requirements and statistical properties of MI test statistics, their associated combining rules and estimators of FMI $r_{m}$. The symbols "+" and "-" mean that the test statistic (or estimator) is equipped and not equipped with the indicated property, respectively; see the end of Section 3.2 for heading descriptions. The reference papers/book are abbreviated as follows: Rubin (2004) (R04), Li et al. (1991a) (LMRR91) and Meng and Rubin (1992) (MR92).
| Test | No. | Combining Rule |  | Estimator of $\varkappa_{m}$ |  | Approx. null distributior ${ }^{a}$ |  | Reference | Properties |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | Formula | Routine | Formula | Routine | Original | Proposed |  | Inv | Con | $\geqslant 0$ | Pow | Def | Sca | EFMI |
| WT | WT-1 | $D_{\mathrm{W}}(T)^{b}$ | $\mathscr{M}_{\mathrm{W}}$ | $\tilde{r}_{\mathrm{W}}^{\prime}$ | $\mathscr{D}_{\mathrm{W}}$ | $F_{k, \widetilde{\mathrm{df}}\left(r_{m}, k\right)}$ | $F_{k, \widehat{\mathrm{df}}\left(r_{m}, k\right)}$ | R04 | - | + | + | - | - | - | $\theta^{c}$ |
|  | WT-2 | $\widetilde{D}_{\mathrm{W}}^{\prime}\left(r_{m}\right)$ | $\mathscr{M}_{\mathrm{W}}$ | $\tilde{r}_{\mathrm{W}}^{\prime}$ | $\mathscr{M}_{\mathrm{W}}$ | $F_{k, \widetilde{\mathrm{df}}\left(r_{m}, k\right)} d$ | $F_{k, \widehat{\mathrm{df}}\left(\mu_{m}, k\right)}$ | R04 | - | $+{ }^{e}$ | + | - | - | - | $\theta$ |
|  | WT-3 | $\tilde{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)^{f}$ | $\mathscr{M}_{\mathrm{W}}$ | $\widetilde{r}_{\mathrm{W}, 1}^{\prime}$ | $\mathscr{D}_{W}$ | $F_{k, \widetilde{\mathrm{df}}^{\prime}\left(r_{m}, k\right)}$ | NA | R04 | - | - | + | - | - | - | $\theta$ |
|  | WT-4 | $\tilde{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)$ | $\mathscr{M}_{\mathrm{W}}$ | $\widetilde{r}_{\mathrm{W}, 1 / 2}^{\prime}$ | $\mathscr{D}_{W}$ | $F_{k, \widetilde{\mathrm{df}}^{\prime}\left(r_{m}, k\right)}$ | NA | LMRR91 | - | - | + | - | - | - | $\theta$ |
|  | WT-5 | $\bar{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)$ | $\mathscr{D}_{W}$ | $\widetilde{r}_{\mathrm{W}, 1}^{\prime}$ | $\mathscr{D}_{\mathrm{W}}$ | $F_{k, \widetilde{\mathrm{df}}^{\prime}\left(r_{m}, k\right)}$ | NA | R04 | - | - | - | - | - | + | $\theta$ |
|  | WT-6 | $\bar{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)$ | $\mathscr{D}_{\mathrm{W}}$ | $\widetilde{r}_{\mathrm{W}, 1 / 2}^{\prime}$ | $\mathscr{D}_{W}$ | $F_{k, \widetilde{\mathrm{df}}^{\prime}\left(r_{m}, k\right)}$ | NA | LMRR91 | - | - | - | - | - | + | $\theta$ |
| LRT | LRT-1 | $\widetilde{D}_{\mathrm{L}}\left(\varkappa_{m}\right)$ | $\mathscr{M}_{\mathrm{L}}, \widetilde{\mathscr{D}}_{\mathrm{L}}$ | $\widetilde{r}_{\mathrm{L}}$ | $\mathscr{M}_{\mathrm{L}}, \widetilde{\mathscr{D}}_{\mathrm{L}}$ | $F_{k, \widetilde{\mathrm{df}}\left(r_{m}, k\right)}$ | $F_{k, \widehat{\mathrm{df}}\left(r_{m}, k\right)}$ | MR92 | - | - | - | - | + | $-^{g}$ | $\theta$ |
|  | LRT-2 | $\widehat{D}_{\mathrm{L}}\left(\varkappa_{m}\right)$ | $\mathscr{D}_{\mathrm{L}}$ | $\hat{r}_{\mathrm{L}}^{+}$ | $\mathscr{D}_{\mathrm{L}}$ | $F_{k, \widetilde{\mathrm{df}}\left(r_{m}, k\right)}$ | $F_{k, \widehat{\mathrm{df}}\left(r_{m}, k\right)}$ | Proposal | + | - | + | - | + | + | $\theta$ |
|  | LRT-3 | $\hat{D}_{\mathrm{L}}\left(\varkappa_{m}\right)$ | $\mathscr{D}_{\mathrm{L}}$ | $\widehat{r}_{\mathrm{L}}^{\diamond}$ | $\mathscr{D}_{\mathrm{L}, 1}$ | $F_{k, \widetilde{\mathrm{df}}\left(r_{m}, h\right)}$ | $F_{k, \widehat{\mathrm{df}}\left(r_{m}, h\right)}$ | Proposal | + | + | + | + | + | + | $\psi$ |
|  | LRT-4 | $\widetilde{D}_{\mathrm{L}}^{+}\left(\varkappa_{m}\right)$ | $\mathscr{M}_{\mathrm{L}}, \widetilde{\mathscr{D}}_{\mathrm{L}}$ | $\widetilde{r}_{\mathrm{L}}^{+}$ | $\mathscr{M}_{\mathrm{L}}, \widetilde{\mathscr{D}}_{\mathrm{L}}$ | $F_{k, \widetilde{\mathrm{df}}\left(r_{m}, k\right)}$ | $F_{k, \widehat{\mathrm{df}}\left(\mu_{m}, k\right)}$ | MR92 ${ }^{h}$ | - | - | + | - | + | - | $\theta$ |
|  | LRT-5 | $\widehat{D}_{\mathrm{L}}\left(\varkappa_{m}\right)$ | $\mathscr{D}_{\mathrm{L}}$ | $\widehat{r}_{\mathrm{L}}$ | $\mathscr{D}_{\mathrm{L}}$ | $F_{k, \widetilde{\mathrm{df}}\left(r_{m}, k\right)}$ | $F_{k, \widehat{\mathrm{df}}\left(r_{m}, k\right)}$ | Proposal | + | - | - | - | + | + | $\theta$ |


[^0]A. 6 Supplement for Section 4.1

Table 4: The values of parameters used in the simulation experiment in Section 4.1.
| Experiment |  |  | Fixed Parameters |  |  |  | Variable Parameter |  |  |  |  |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| No. | Variable Parameter |  | $\rho$ | $p$ | $\boldsymbol{f}$ |  | Case 1 | Case 2 | Case 3 | Case 4 | Case 5 |
| I | Correlation $\rho$ |  | - | 2 | 0.5 |  | -0.8 | -0.4 | 0 | 0.4 | 0.8 |
| II | Dimension $p$ |  | 0.4 | - | 0.5 |  | 2 | 3 | 4 | 5 | 6 |
| III | FMI $\boldsymbol{f}$ |  | 0.4 | 2 | - |  | 0.1 | 0.3 | 0.5 | 0.7 | 0.9 |


## A. 6 Supplement for Section 4.1

Let $\bar{X}_{\text {obs }}$ and $S_{\text {obs }}$ be the sample mean and sample covariance matrix based on $X_{\text {obs }}$. Then, the $\ell$ th imputed missing data set can be produced by the following procedure, for $\ell=1, \ldots, m$.

1. Draw $\left(\Sigma^{(\ell)}\right)^{-1}$ from a Wishart distribution with $\left(n_{\text {obs }}-1\right)$ degrees of freedom and scale matrix $S_{\text {obs }}$.
2. Draw $\mu^{(\ell)}$ from $\mathcal{N}_{p}\left(\bar{X}_{\text {obs }}, \Sigma^{(\ell)} / n_{\text {obs }}\right)$.
3. Draw $\left(n-n_{\text {obs }}\right)$ imputed missing values $\left\{X_{i}^{(\ell)}: i=n_{\text {obs }}+1, \ldots, n\right\}$ from $\mathcal{N}_{p}\left(\mu^{(\ell)}, \Sigma^{(\ell)}\right)$ independently.

Also, denote $X_{i}^{(\ell)}=X_{i}$ for $i=1, \ldots, n_{\text {obs }}$. With the $\ell$ th completed data set, the unconstrained MLEs for $\mu$ and $\Sigma$ are

$$
\widehat{\mu}^{(\ell)}=\frac{1}{n} \sum_{i=1}^{n} X_{i}^{(\ell)}, \quad \widehat{\Sigma}^{(\ell)}=\frac{1}{n} \sum_{i=1}^{n}\left(X_{i}^{(\ell)}-\widehat{\mu}^{(\ell)}\right)\left(X_{i}^{(\ell)}-\widehat{\mu}^{(\ell)}\right)^{\top} .
$$

Whereas we generate data using a covariance matrix with common variance and correlation, our model does not assume any structure for $\Sigma$. The only restriction we can impose is the common-mean assumption under the null, for which the constrained MLEs are

$$
\widehat{\mu}_{0}^{(\ell)}=\left\{\frac{\mathbf{1}_{p}^{\top}\left(\widehat{\Sigma}^{(\ell)}\right)^{-1} \widehat{\mu}^{(\ell)}}{\mathbf{1}_{p}^{\top}\left(\widehat{\Sigma}^{(\ell)}\right)^{-1} \mathbf{1}_{p}}\right\} \mathbf{1}_{p}, \quad \widehat{\Sigma}_{0}^{(\ell)}=\widehat{\Sigma}^{(\ell)}+\left(\widehat{\mu}^{(\ell)}-\widehat{\mu}_{0}^{(\ell)}\right)\left(\widehat{\mu}^{(\ell)}-\widehat{\mu}_{0}^{(\ell)}\right)^{\top}
$$

We first study the distribution of $p$-values of each test under $H_{0}$. We use $n=100, m=3, \sigma^{2}=5$ and $\mu=\mathbf{1}_{p}$, with various values of $\rho, p$ and $\mathcal{f}$ specified in Table 4. The results under parametrizations (i), (ii) and (iii) are shown in Figures 7, 8 and 9, respectively. Note that, for Wald tests under

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-35.jpg?height=716&width=1321&top_left_y=421&top_left_x=302)
Figure 7: The comparison between empirical size and nominal size $\alpha$ under parametrization (ii) for $\alpha \in(0,5 \%]$. Our most recommended proposal is LRT-3, which is highlighted red.

parametrization (ii), the matrix $U^{(\ell)}$ is singular in $0.25 \%$ of the replications, and those cases are removed from the analysis (which should favor the Wald tests).

The empirical sizes (i.e., type-I errors) of the MI Wald tests generally deviate from the nominal size $\alpha$ under parametrization (ii). In contrast, the sizes of all LRTs are closer to $\alpha$. However, the original L-1 and its trivial modification L-2 do not have accurate sizes when $|\rho|$ or $\mathcal{f}$ is large. They can be over-sized or under-sized depending on which parametrization is used. Moreover, the trivial modification L-2 does not help to correct the size, and it may even worsen the test. For our test statistics L-3 and L-4, they are invariant to parametrizations and have quite accurate sizes, although they are under-sized in challenging cases where both $p$ and $\mathcal{f}$ are large. For our recommended statistic L-5, it gives the most satisfactory overall results. It generally has very accurate size, except that it is slightly over-sized for large $p$, a problem that should diminish when we use $m$ beyond the smallest recommended $m=3$.

Interestingly, as seen clearly in Figure 8, the benchmark L-0 performs very badly for large $p$ and $f$. This is because the sample size per parameter, $n / h$,

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-36.jpg?height=716&width=1323&top_left_y=421&top_left_x=300)
Figure 8: The comparison between empirical size and nominal size $\alpha$ under parametrization (i) for $\alpha \in(0,5 \%]$. The legend in Figure 7 also applies here.

is small; for $p \geqslant 4, n / h \leqslant 100 / 14<8$. The asymptotic null distribution $\chi_{k}^{2} / k$ then can fail badly under arbitrary or even all parametrizations; (ii) apparently falls into this category. An $F$ approximation would be more appropriate (see Barnard and Rubin, 1999). But this is exactly what is being used for MI tests, albeit with different choices of the denominator degrees of freedom. Note also that, in some cases, nearly half of the simulated values of $\widetilde{r}_{\mathrm{L}}$ and $\widetilde{D}_{\mathrm{L}}$ are negative; see Table 5. In contrast, $\widehat{r}_{\mathrm{S}}$ is always non-negative in our simulation, despite the fact that it can be negative in theory.

The power curves under nominal size $0.5 \%$ and $5 \%$ are shown in Figure 2 of the main text and Figure 10, respectively. Note that the trivial modifications LRT-2 of LRT-1 cannot retrieve all the power it should have. Tables 6 and 7 show the minimum and maximum of the empirical sizes over the three parametrizations considered in each test - and only one value is needed for those tests that are invariant to parametrization - when the nominal size is $0.5 \%$ and $5 \%$, respectively. We see the deviations from the nominal $\alpha$ can be noticeable, especially when $m=3$. To take that into account, we report the empirical size adjusted power, that is, $O=$ power $/ \widehat{\alpha}$, which also has the interpretation as (an approximated) posterior odds of $H_{1}$ to $H_{0}$ (Bayarri et al., 2016). Figures 11 and 12 plot the result for nominal size $0.5 \%$ and $5 \%$,

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-37.jpg?height=716&width=1318&top_left_y=421&top_left_x=302)
Figure 9: The comparison between empirical size and nominal size $\alpha$ under parametrization (iii) for $\alpha \in(0,5 \%]$. The legend in Figure 8 also applies here.

Table 5: The empirical proportions of negative $\widetilde{r}_{\mathrm{L}}$ and $\widetilde{D}_{\mathrm{L}}$. The results under parametrizations (ii) and (iii) are shown. For parametrization (i), $\widetilde{r}_{\mathrm{L}} \geqslant 0$ and $\widetilde{D}_{\mathrm{L}} \geqslant 0$ in the experiments.
| Experiment | Parametrization | Case |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 1 | 2 | 3 | 4 | 5 | 1 | 2 | 3 | 4 | 5 |
|  |  | \% of $\widetilde{r}_{\mathrm{L}}<0$ |  |  |  |  | \% of $\widetilde{D}_{\mathrm{L}}<0$ |  |  |  |  |
| I | (ii) | 1 | 2 | 3 | 4 | 5 | 26 | 16 | 13 | 12 | 12 |
|  | (iii) | 6 | 6 | 7 | 7 | 7 | 1 | 1 | 1 | 1 | 2 |
| II | (ii) | 4 | 1 | 0 | 0 | 0 | 12 | 5 | 3 | 4 | 3 |
|  | (iii) | 7 | 3 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| III | (ii) | 13 | 6 | 4 | 4 | 3 | 55 | 25 | 12 | 5 | 2 |
|  | (iii) | 18 | 9 | 7 | 5 | 4 | 20 | 5 | 1 | 1 | 0 |


respectively. Compared with the benchmark L-0, the odds $O$ of the proposed

## A. 7 Supplements for Section 4.2

Table 6: The range of empirical size $[\min \hat{\alpha}, \max \hat{\alpha}]$ in percentage, where max and min are taken over the three parametrizations. Only one value is recorded for parametrization-invariant tests. The nominal size is $\alpha=0.5 \%$. The results under nominal size $\alpha=5 \%$ are shown in Figure 7.
| $(n, m)$ | Range of empirical size: $[\min \hat{\alpha}, \max \hat{\alpha}] / \%$ |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  | $(1600,3)$ | $(400,3)$ | $(100,3)$ | $(100,10)$ | $(100,30)$ |
| W-1 | [0.90, 1.05] | [0.76, 1.05] | [0.20, 1.22] | [0.07, 0.56] | [0.02, 0.49] |
| W-2 | [0.90, 1.05] | [0.98, 1.22] | [0.93, 1.25] | [0.32, 0.73] | [0.20, 0.85] |
| W-3 | [0.98, 1.05] | [0.98, 1.25] | [0.90, 1.29] | [0.34, 0.71] | [0.22, 0.73] |
| W-4 | [0.90, 1.05] | [0.76, 1.05] | [0.20, 1.22] | [0.07, 0.56] | [0.02, 0.49] |
| L-1 | [0.90, 1.03] | [1.10, 1.64] | [1.15, 1.49] | [0.37, 1.05] | [0.10, 0.46] |
| L-2 | [0.90, 1.05] | [1.10, 1.76] | [1.15, 2.37] | [0.37, 0.98] | [0.10, 0.49] |
| L-3 | 0.90 | 1.10 | 0.83 | 0.24 | 0.07 |
| L-4 | 0.90 | 1.10 | 0.83 | 0.24 | 0.07 |
| L-5 | 0.46 | 0.44 | 0.68 | 0.46 | 0.42 |
| L-0 | 0.39 | 0.66 | 0.66 | 0.66 | 0.66 |


robust MI test (L-5) is closer to the nominal value $1 / \alpha$ as $\delta \rightarrow \infty$. Nevertheless, the performances of all size $0.5 \%$ tests are less satisfactory than those for size $5 \%$ tests because larger sample sizes $n$ are required to approximate the tail behavior well.

We also compare the performance of estimators of $\varkappa_{m}$ for different $\delta$ and parametrizations. In our experiment, we have $\varkappa_{m}=1+1 / m$ because we have set $\mathfrak{r}=1$. The MSEs of estimators $\hat{f}=\hat{r} /(1+\hat{r})$ of $f_{m}=r_{m} /\left(1+r_{m}\right)$ are shown in Figure 13, in log scale. Clearly, the only estimator that is consistent, invariant to parametrization and robust against $\delta$ is our proposal $\widehat{f}_{\mathrm{L}}^{\diamond}=\widehat{r}_{\mathrm{L}} /\left(1+\widehat{r}_{\mathrm{L}}^{\diamond}\right)$. It concentrates at the true value $f_{m}$ quite closely even for small $m$ and $n$. It verifies why L- 5 has the greatest power. On the other hand, the estimator $\widetilde{f}_{\mathrm{L}}=\widetilde{r}_{\mathrm{L}} /\left(1+\widetilde{r}_{\mathrm{L}}\right)$ has a large MSE when $\delta \neq 0$. It explains why $\mathrm{L}-1$ is not powerful.

## A. 7 Supplements for Section 4.2

Let $n_{j}=\sum_{i=1}^{n} R_{i j}$ be the number of observed $j$ th component. Without loss of generality, assume $X_{\text {obs }}$ is arranged in such a way that $R_{i j} \geqslant R_{i^{\prime} j}$ for all

## A. 7 Supplements for Section 4.2

Table 7: The range of empirical size $[\min \hat{\alpha}, \max \hat{\alpha}]$ in percentage, where max and min are taken over the three parametrizations. Only one value is recorded for parametrization-invariant tests. The nominal size is $\alpha=5 \%$.
| $(n, m)$ | Range of empirical size: $[\min \hat{\alpha}, \max \hat{\alpha}] / \%$ |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  | $(1600,3)$ | $(400,3)$ | $(100,3)$ | $(100,10)$ | $(100,30)$ |
| W-1 | [5.62, 5.71] | [5.30, 6.03] | [3.22, 6.20] | [1.64, 4.81] | [1.37, 5.00] |
| W-2 | [5.93, 6.05] | [6.08, 7.18] | [5.52, 8.69] | [4.42, 8.47] | [4.20, 8.50] |
| W-3 | [5.81, 6.03] | [6.01, 6.98] | [5.37, 8.28] | [4.20, 7.67] | [4.10, 7.50] |
| W-4 | [5.62, 5.71] | [5.30, 6.03] | [3.22, 6.20] | [1.64, 4.81] | [1.37, 5.00] |
| L-1 | [5.57, 6.15] | [6.37, 6.57] | [5.88, 6.47] | [4.39, 5.66] | [4.22, 5.32] |
| L-2 | [5.52, 6.10] | [6.37, 6.52] | [5.88, 7.47] | [4.39, 5.66] | [4.22, 5.32] |
| L-3 | 5.76 | 6.37 | 5.42 | 3.78 | 3.71 |
| L-4 | 5.76 | 6.37 | 5.42 | 3.78 | 3.71 |
| L-5 | 4.96 | 5.32 | 4.93 | 4.79 | 4.54 |
| L-0 | 5.03 | 5.03 | 5.57 | 5.57 | 5.57 |


$i<i^{\prime}$ and $j$. To impute the missing data, it is useful to represent $X_{i}$ by $\left[X_{i 1} \mid \beta_{1}, \tau_{1}^{2}\right] \sim \mathcal{N}\left(\beta_{1}, \tau_{1}^{2}\right) \quad$ and $\quad\left[X_{i j} \mid X_{i, 1:(j-1)}, \beta_{j}, \tau_{j}^{2}\right] \sim \mathcal{N}\left(\beta_{j}^{\top} Z_{i j}, \tau_{j}^{2}\right)$, for $j=2, \ldots, p$ where $\tau_{1}^{2}, \ldots, \tau_{p}^{2} \in \mathbb{R}^{+}, \beta_{j} \in \mathbb{R}^{j}, X_{i, 1:(j-1)}=\left(X_{i 1}, \ldots, X_{i, j-1}\right)^{\top}$ and $Z_{i j}=\left(1, X_{i, 1:(j-1)}^{\top}\right)^{\top}$ for $j \geqslant 2$. Denote the (complete-case) least squares estimators of $\beta_{j}$ and $\tau_{j}^{2}$ respectively by

$$
\widehat{\beta}_{j}=\left(Z_{j}^{\top} Z_{j}\right)^{-1} Z_{j}^{\top} W_{j} \quad \text { and } \quad \hat{\tau}_{j}^{2}=\frac{\left(W_{j}-Z_{j} \hat{\beta}_{j}\right)^{\top}\left(W_{j}-Z_{j} \hat{\beta}_{j}\right)}{n_{j}-j},
$$

where $Z_{j}=\left(Z_{1 j}, \ldots, Z_{n_{j} j}\right)^{\top}$ and $W_{j}=\left(X_{1 j}, \ldots, X_{n_{j} j}\right)^{\top}$.
We assume a Bayesian imputation model with the non-informative prior $f\left(\beta_{1}, \ldots, \beta_{p}, \tau_{1}^{2}, \ldots, \tau_{p}^{2}\right) \propto 1 /\left(\tau_{1}^{2} \cdots \tau_{p}^{2}\right)$. For $\ell=1, \ldots, m$, denote the $\ell$ th imputed data set by $X^{(\ell)}$, whose $(i, j)$ th element is $X_{i j}^{(\ell)}$. If $1 \leqslant j \leqslant p$ and $i \leqslant n_{j}$, then $X_{i j}^{(\ell)}=X_{i j}$, otherwise $X_{i j}^{(\ell)}$ is filled in by recursing the following steps for $j=2, \ldots, p$.

1. Draw a sample $\left(\tau_{j}^{(\ell)}\right)^{2}$ from $\widehat{\tau}_{j}^{2}\left(n_{j}-j\right) / \chi_{n_{j}-j}^{2}$.
2. Draw a sample $\beta_{j}^{(\ell)}$ from $\mathcal{N}_{j}\left(\widehat{\beta}_{j},\left(\tau_{j}^{(\ell)}\right)^{2}\left(Z_{j}^{\top} Z_{j}\right)^{-1}\right)$.
3. Draw a sample $X_{i j}^{(\ell)}$ from $\mathscr{N}\left(\left(\beta_{j}^{(\ell)}\right)^{\top} Z_{i j}^{(\ell)},\left(\tau_{j}^{(\ell)}\right)^{2}\right)$ for $i=n_{j}+1, \ldots, n$, where $Z_{i j}^{(\ell)}=\left(1,\left(X_{i, 1:(j-1)}^{(\ell)}\right)^{\top}\right)^{\top}$.

With the $\ell$ th imputed data set, the $H_{0}$-constrained MLEs of $\mu$ and $\Sigma$ are $\widehat{\mu}_{0}^{(\ell)}=\mathbf{0}_{p}$ and $\widehat{\Sigma}_{0}^{(\ell)}=\left(X^{(\ell)}\right)^{\top}\left(X^{(\ell)}\right) / n$; whereas the unconstrained counterparts are $\widehat{\mu}^{(\ell)}=\mathbf{1}_{n}^{\top} X^{(\ell)} / n$ and $\widehat{\Sigma}^{(\ell)}=\left(X^{(\ell)}-\widehat{\mu}^{(\ell)}\right)^{\top}\left(X^{(\ell)}-\widehat{\mu}^{(\ell)}\right) / n$.

The partial result is shown in Figure 3 of the main text, whereas the full version is shown in Figure 14.

## A. 8 Applications to a Care-Survival Data

Meng and Rubin (1992) considered the data given in Table 8, where $i, j$ and $k$ index, respectively, amount of parental care (less or more, corresponding to $i=1,2$ ), and survival status (died or survived, corresponding to $j=1,2$ ), and clinic ( A or B , corresponding to $k=1,2$ ). The label $k$ is missing for some observations. The missing mechanism was assumed to be ignorable. We consider two null hypotheses: ( $H_{0}$ ) the clinic and parental care are conditionally independent given the survival status, and ( $H_{0}^{\prime}$ ) all three variables are independent. It is remarked that testing the conditional independence model (i.e., $H_{0}$ ) is useful from a modeling perceptive. If $H_{0}$ cannot be rejected, then one may be tempted to adopt the more parsimonious null model (for the cell probabilities). The same model is also suggested in Little and Rubin (2002) and Meng and Rubin (1992).

Our aim is to investigate the impact on $\left\{\widetilde{D}_{\mathrm{S}}, \widehat{D}_{\mathrm{S}}^{+}, \widehat{D}_{\mathrm{S}}^{\diamond}\right\}$ by the parametrization of the cell probabilities

$$
\pi_{i j k}=\mathrm{P}(\text { parental care }=i, \text { survival status }=j, \text { clinic label }=k)
$$

for $i, j, k \in\{1,2\}$; and the impact on $\left\{\widetilde{r}_{\mathrm{L}}, \widehat{r}_{\mathrm{S}}^{+}, \widehat{r}_{\mathrm{S}}\right\}$ under different null hypotheses. Here the full model parameter vector can be expressed as $\psi= \left(\pi_{111}, \pi_{112}, \pi_{121}, \pi_{122}, \pi_{211}, \pi_{212}, \pi_{221}\right)^{\top}$. Since the restrictions imposed by $H_{0}$ are $\pi_{i j k}=\left(\pi_{1 j k}+\pi_{2 j k}\right)\left(\pi_{i j 1}+\pi_{i j 2}\right)$ for $j=1,2$, one may express the parameter of interest as $\theta=\left(\theta_{1}, \theta_{2}\right)^{\top}$, where $\theta_{j}=\pi_{i j k}-\left(\pi_{1 j k}+\pi_{2 j k}\right)\left(\pi_{i j 1}+\pi_{i j 2}\right)$ for $j=1,2$. Then $H_{0}$ can be equivalently stated as $\theta=\theta_{0}$, where $\theta_{0}=(0,0)^{\top}$. Similarly, the parameter of interest under $H_{0}^{\prime}$ can be defined.

The computation of the stacked MI estimators of $\left\{\pi_{i j k}\right\}$ is presented in A. 8 of the Appendix. We consider three parametrizations: (i) $\psi_{i j k}=\pi_{i j k}$; (ii) $\psi_{i j k}=\log \left\{\pi_{i j k} /\left(1-\pi_{i j k}\right)\right\}$; and (iii) $\psi_{i j 1}=\pi_{i j 1}$ and $\psi_{i j 2}=\pi_{i j 2} / \pi_{i j 1}$. Denote the $p$-values of tests $\left\{\widetilde{D}_{\mathrm{L}}, \widehat{D}_{\mathrm{S}}^{+}, \widehat{D}_{\mathrm{S}}^{\diamond}\right\}$ by $\left\{\widetilde{p}_{\mathrm{L}}, \widehat{p}_{\mathrm{S}}^{+}, \widehat{p}_{\mathrm{S}}^{\widehat{ }}\right\}$, respectively. The results are summarized in Table 9. Clearly, only $\widehat{r}_{\mathrm{S}}, \widehat{r}_{\diamond}, \widehat{D}_{\mathrm{S}}^{+}, \widehat{D}_{\mathrm{S}}^{\widehat{S}}$ are always non-negative

Table 8: Data from Meng and Rubin (1992). The notation "?" indicates missing label.
| Parental care $(i)$ |  | Less |  |  | More |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Survival Status $(j)$ | Died | Survived |  | Died | Survived |  |
| Clinic Label $(k)$ | A | 3 | 176 |  | 4 | 293 |
|  | B | 17 | 197 |  | 2 | 23 |
|  | $?$ | 10 | 150 |  | 5 | 90 |


and parametrization-invariant. Some of the values of $\widetilde{r}_{\mathrm{L}}$ and $\widetilde{D}_{\mathrm{L}}$ are negative, leading to the meaningless $\widetilde{p}_{\mathrm{L}}=1$. For testing $H_{0}$, we have $\widehat{D}_{\mathrm{S}}^{+} \approx \widehat{D}_{\mathrm{S}}^{\diamond}$. For testing $H_{0}^{\prime}, \widehat{D}_{\mathrm{S}}^{+}$and $\widehat{D}_{\mathrm{S}}^{\diamond}$ are not very close to each other, but they both lead to essentially zero $p$-value. These results reconfirm the conclusions in Meng and Rubin (1992). Moreover, only $\widehat{r_{\mathrm{S}}}$ does not change under different null hypotheses.

The MI data sets are generated from a Bayesian model in Section 4.2 of Meng and Rubin (1992). The $\ell$ th imputed $\log$-likelihood function is $\log f\left(X^{(\ell)} \mid\right. \pi)=\sum_{c} n_{c}^{(\ell)} \log \pi_{c}$, where $X^{(\ell)}$ are the cell counts $n_{c}^{(\ell)}$ in the $\ell$ th imputed data set. Hence the unconstrained MLE of $\pi_{c}$ is $\widehat{\pi}_{c}^{(\ell)}=n_{c}^{(\ell)} / n_{+}^{(\ell)}$, where $n_{+}^{(\ell)}=\sum_{c} n_{c}^{(\ell)}$. Let $n_{c}^{+}=\sum_{\ell=1}^{m} n_{c}^{(\ell)}$. Consequently, the joint log-likelihood based on the stacked data is

$$
\log f\left(X^{\mathrm{S}} \mid \pi\right)=\sum_{\ell=1}^{m} \sum_{c} n_{c}^{(\ell)} \log \pi_{c}=\sum_{c} n_{c}^{+} \log \pi_{c},
$$

Thus the unconstrained MLE with respect to (A.14) is $\widehat{\pi}_{c}^{\mathrm{S}}=n_{c}^{+} / n_{+}^{+}$, where $n_{+}^{+}=\sum_{c} n_{c}^{+}$. Similarly, we can find the constrained MLEs under a given null.

## B. Proofs

Proof of Theorem 1. (i, ii) From (2.3), we know $\hat{d}_{\mathrm{L}} \geqslant 0$ is invariant to parametrization $\psi$. (iii) Since $\hat{d}_{\mathrm{L}}$ is invariant to transformation of $\psi$, we assume, without loss of generality, that $\psi$ admits a parameterization such that $\operatorname{Cov}\left(\hat{\theta}^{(\ell)}, \hat{\eta}^{(\ell)}\right) \bumpeq \mathbf{0}$ by taking suitable linear transformation of $\psi$. Also write $U_{\eta}^{(\ell)}$ as an efficient estimator of $\operatorname{Var}(\widehat{\eta})$ based on $X^{(\ell)}$; and recall that $U_{\theta}^{(\ell)}=U^{(\ell)}$ is an efficient estimator of $\operatorname{Var}(\widehat{\theta})$ based on $X^{(\ell)}$.

Using Taylor's expansion on $\psi \mapsto \bar{L}(\psi)=m^{-1} \sum_{\ell=1}^{m} \log f\left(X^{(\ell)} \mid \psi\right)$ around

Table 9: The LRTs using $\widetilde{D}_{\mathrm{L}}, \widehat{D}_{\mathrm{S}}^{+}$and $\widehat{D}_{\mathrm{S}}^{\widehat{S}}$ under different parametrizations in Section A.8.
|  | Parametrization (i): identity map |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $H_{0}$ : Conditional independence |  |  | $H_{0}$ : Full independence |  |  |
| $m$ | $\widetilde{r}_{\mathrm{L}}, \widehat{r}_{\mathrm{S}}^{+}, \widehat{r}_{\mathrm{S}}^{\diamond}$ | $\widetilde{D}_{\mathrm{L}}, \widehat{D}_{\mathrm{S}}^{+}, \widehat{D}_{\mathrm{S}}^{\diamond}$ | $\widetilde{p}_{\mathrm{L}}, \widehat{p}_{\mathrm{S}}^{+}, \widehat{p}_{\mathrm{S}}^{\widehat{ }}$ | $\widetilde{r}_{\mathrm{L}}, \widehat{r}_{\mathrm{S}}^{+}, \widehat{r}_{\mathrm{S}}^{\circlearrowright}$ | $\widetilde{D}_{\mathrm{L}}, \hat{D}_{\mathrm{S}}^{+}, \hat{D}_{\mathrm{S}}^{\diamond}$ | $\widetilde{p}_{\mathrm{L}}, \widehat{p}_{\mathrm{S}}^{+}, \widehat{p}_{\mathrm{S}}$ |
| $\overline{2}$ | 0.63, 0.64, 0.83 | 0.14, 0.14, 0.12 | 0.87, 0.87, 0.89 | 0.53, 0.53, 0.83 | 44.4, 44.4, 37.1 | 0, 0, 0 |
| 3 | 0.54, 0.54, 0.38 | 0.08, 0.08, 0.09 | 0.93, 0.93, 0.92 | 0.31, 0.31, 0.38 | 54.2, 54.2, 51.4 | 0, 0, 0 |
| 5 | 0.49, 0.48, 0.89 | 0.12, 0.12, 0.10 | 0.89, 0.89, 0.91 | 0.72, 0.72, 0.89 | 40.8, 40.8, 37.1 | 0, 0, 0 |
| 7 | 0.23, 0.23, 0.47 | 0.06, 0.06, 0.05 | 0.94, 0.94, 0.95 | 0.31, 0.31, 0.47 | 53.2, 53.2, 47.6 | 0, 0, 0 |
| 10 | 0.50, 0.50, 0.70 | 0.14, 0.14, 0.12 | 0.87, 0.87, 0.88 | 0.56, 0.56, 0.70 | 45.4, 45.4, 41.7 | 0, 0, 0 |
| 25 | 0.35, 0.35, 0.47 | 0.06, 0.06, 0.06 | 0.94, 0.94, 0.95 | 0.35, 0.35, 0.47 | 51.4, 51.4, 47.0 | 0, 0, 0 |
| 50 | 0.31, 0.31, 0.45 | 0.11, 0.11, 0.10 | 0.90, 0.90, 0.91 | 0.33, 0.33, 0.45 | 51.5, 51.5, 47.3 | 0, 0, 0 |
| Parametrization (ii): logit transformation |  |  |  |  |  |  |
| $H_{0}$ : Conditional independence |  |  |  | $H_{0}$ : Full independence |  |  |
| $m$ | $\widetilde{r}_{\mathrm{L}}, \widehat{r}_{\mathrm{S}}^{+}, \widehat{r}_{\mathrm{S}}^{>}$ | $\widetilde{D}_{\mathrm{L}}, \widehat{D}_{\mathrm{S}}^{+}, \widehat{D}_{\mathrm{S}}^{\diamond}$ | $\widetilde{p}_{\mathrm{L}}, \widehat{p}_{\mathrm{S}}^{+}, \widehat{p}_{\mathrm{S}}$ | $\widetilde{r}_{\mathrm{L}}, \widehat{r}_{\mathrm{S}}^{+}, \widehat{r}_{\mathrm{S}}^{\top}$ | $\widetilde{D}_{\mathrm{L}}, \hat{D}_{\mathrm{S}}^{+}, \hat{D}_{\mathrm{S}}^{\diamond}$ | $\widetilde{p}_{\mathrm{L}}, \widehat{p}_{\mathrm{S}}^{+}, \widehat{p}_{\mathrm{S}}$ |
| 2 | 1.23, 0.64, 0.83 | 0.01, 0.14, 0.12 | 0.99, 0.87, 0.89 | 0.98, 0.53, 0.83 | 34.2, 44.4, 37.1 | 0, 0, 0 |
| 3 | 1.08, 0.54, 0.38 | -0.07, 0.08, 0.09 | 1.00, 0.93, 0.92 | 0.61, 0.31, 0.38 | 43.9, 54.2, 51.4 | 0, 0, 0 |
| 5 | 1.02, 0.48, 0.89 | -0.09, 0.12, 0.10 | 1.00, 0.89, 0.91 | 1.40, 0.72, 0.89 | 29.0, 40.8, 37.1 | 0, 0, 0 |
| 7 | 0.45, 0.23, 0.47 | -0.07, 0.06, 0.05 | 1.00, 0.94, 0.95 | 0.58, 0.31, 0.47 | 43.9, 53.2, 47.6 | 0, 0, 0 |
| 10 | 0.99, 0.50, 0.70 | -0.10, 0.14, 0.12 | 1.00, 0.87, 0.88 | 1.09, 0.56, 0.70 | 33.7, 45.4, 41.7 | 0, 0, 0 |
| 25 | 0.71, 0.35, 0.47 | -0.14, 0.06, 0.06 | 1.00, 0.94, 0.95 | 0.68, 0.35, 0.47 | 41.0, 51.4, 47.0 | 0, 0, 0 |
| 50 | 0.63, 0.31, 0.45 | -0.10, 0.11, 0.10 | 1.00, 0.90, 0.91 | 0.65, 0.33, 0.45 | 41.3, 51.5, 47.3 | 0, 0, 0 |
| Parametrization (iii): ratios of probabilities |  |  |  |  |  |  |
| $H_{0}$ : Conditional independence |  |  |  | $H_{0}$ : Full independence |  |  |
| $m$ | $\widetilde{r}_{\mathrm{L}}, \widehat{r}_{\mathrm{S}}^{+}, \widehat{r}_{\mathrm{S}}^{\gamma}$ | $\widetilde{D}_{\mathrm{L}}, \widehat{D}_{\mathrm{S}}^{+}, \widehat{D}_{\mathrm{S}}^{\diamond}$ | $\widetilde{p}_{\mathrm{L}}, \widehat{p}_{\mathrm{S}}^{+}, \widehat{p}_{\mathrm{S}}$ | $\widetilde{r}_{\mathrm{L}}, \widehat{r}_{\mathrm{S}}^{+}, \widehat{r}_{\mathrm{S}}^{\top}$ | $\widetilde{D}_{\mathrm{L}}, \widehat{D}_{\mathrm{S}}^{+}, \widehat{D}_{\mathrm{S}}^{\diamond}$ | $\widetilde{p}_{\mathrm{L}}, \widehat{p}_{\mathrm{S}}^{+}, \widehat{p}_{\mathrm{S}}$ |
| 2 | 1.06, 0.64, 0.83 | 0.04, 0.14, 0.12 | 0.96, 0.87, 0.88 | -0.38, 0.53, 0.83 | 109, 44.4, 37.1 | 0, 0, 0 |
| 3 | -2.35, 0.54, 0.38 | -1.16, 0.08, 0.09 | 1.00, 0.93, 0.92 | -1.22, 0.31, 0.38 | -321, 54.2, 51.4 | 1, 0, 0 |
| 5 | -2.64, 0.48, 0.89 | -1.38, 0.12, 0.10 | 1.00, 0.89, 0.91 | -2.24, 0.72, 0.89 | -58, 40.8, 37.1 | 1, 0, 0 |
| 7 | -0.01, 0.23, 0.47 | 0.25, 0.06, 0.05 | 0.78, 0.94, 0.95 | -0.34, 0.31, 0.47 | 107, 53.2, 47.6 | 0, 0, 0 |
| 10 | -2.04, 0.50, 0.70 | -2.20, 0.14, 0.12 | 1.00, 0.87, 0.88 | -1.85, 0.56, 0.70 | -86, 45.4, 41.7 | 1, 0, 0 |
| 25 | -1.39, 0.35, 0.47 | -4.30, 0.06, 0.06 | 1.00, 0.94, 0.95 | -1.12, 0.35, 0.47 | -603, 51.4, 47.0 | 1, 0, 0 |
| 50 | -1.22, 0.31, 0.45 | -7.39, 0.11, 0.10 | 1.00, 0.90, 0.91 | -1.06, 0.33, 0.45 | -1136, 51.5, 47.3 | 1, 0, 0 |


$\widehat{\psi}^{*}=\left(\left(\widehat{\theta}^{*}\right)^{\top},\left(\widehat{\eta}^{*}\right)^{\top}\right)^{\top}$, we know that for $\psi \bumpeq \widehat{\psi}^{*}$,

$$
\bar{L}(\psi) \bumpeq \bar{L}\left(\hat{\psi}^{*}\right)-\frac{1}{2}\left(\psi-\widehat{\psi}^{*}\right)^{\top} \bar{I}\left(\hat{\psi}^{*}\right)\left(\psi-\hat{\psi}^{*}\right)
$$

where $\bar{I}(\psi)=-\partial^{2} \bar{L}(\psi) / \partial \psi \partial \psi^{\top}$, which satisfies

$$
\bar{I}\left(\widehat{\psi}^{*}\right) \bumpeq\left(\begin{array}{cc}
\bar{U}_{\theta}^{-1} & \mathbf{0} \\
\mathbf{0} & \bar{U}_{\eta}^{-1}
\end{array}\right)
$$

with $\bar{U}_{\eta}=m^{-1} \sum_{i=1}^{m} U_{\eta}^{(\ell)}$. Under the null, $\widehat{\psi}^{*} \bumpeq \widehat{\psi}_{0}^{*}$. So, using (B.1), we have

$$
\begin{aligned}
\hat{d}_{\mathrm{L}} & \bumpeq\left(\hat{\psi}_{0}^{*}-\hat{\psi}^{*}\right)^{\top} \bar{I}\left(\hat{\psi}^{*}\right)\left(\hat{\psi}_{0}^{*}-\hat{\psi}^{*}\right) \\
& \bumpeq\binom{\theta_{0}-\hat{\theta}^{*}}{\hat{\eta}\left(\theta_{0}\right)-\hat{\eta}\left(\hat{\theta}^{*}\right)}^{\top}\left(\begin{array}{cc}
\bar{U}_{\theta}^{-1} & \mathbf{0} \\
\mathbf{0} & \bar{U}_{\eta}^{-1}
\end{array}\right)\binom{\theta_{0}-\hat{\theta}^{*}}{\hat{\eta}\left(\theta_{0}\right)-\hat{\eta}\left(\hat{\theta}^{*}\right)} \\
& \bumpeq\left(\bar{\theta}^{\top}-\theta_{0}\right) \bar{U}_{\theta}^{-1}\left(\bar{\theta}^{\top}-\theta_{0}\right)=\widetilde{d}_{\mathrm{W}}^{\prime}
\end{aligned}
$$

where we have used (a) $\hat{\theta}^{*} \bumpeq \bar{\theta}$; see, e.g., Lemma 1 of Wang and Robins (1998), and (b) $\widehat{\eta}\left(\theta_{0}\right)-\widehat{\eta}\left(\widehat{\theta}^{*}\right)=O_{p}(1 / n)$ if $\theta_{0}-\widehat{\theta}^{*}=O_{p}(1 / \sqrt{n})$; see Cox and Reid (1987). Since $\widetilde{d}_{\mathrm{W}}^{\prime} \bumpeq \widetilde{d}_{\mathrm{L}}$ (Meng and Rubin, 1992), we have $\widehat{d}_{\mathrm{L}} \bumpeq \widetilde{d}_{\mathrm{L}}$.

Proof of Proposition 1. The given condition implies that

$$
\begin{array}{cc}
\widehat{\psi}^{(\ell)}=\left(\left(\hat{\theta}^{(\ell)}\right)^{\top},\left(\hat{\eta}^{(\ell)}\right)^{\top}\right)^{\top}, & \hat{\psi}_{0}^{(\ell)}=\left(\theta_{0}^{\top},\left(\hat{\eta}^{(\ell)}\right)^{\top}\right)^{\top} \\
\hat{\psi}^{*}=\left(\left(\hat{\theta}^{*}\right)^{\top},\left(\hat{\eta}^{*}\right)^{\top}\right)^{\top}, & \hat{\psi}_{0}^{*}=\left(\theta_{0}^{\top},\left(\hat{\eta}^{*}\right)^{\top}\right)^{\top}
\end{array}
$$

Clearly, we also have the decomposition: $L^{(\ell)}(\psi)=L_{\dagger}^{(\ell)}(\theta)+L_{\ddagger}^{(\ell)}(\eta)$ for all $\ell$, where $L_{\dagger}^{(\ell)}(\theta)=L_{\dagger}\left(\theta \mid X^{(\ell)}\right)$ and $L_{\ddagger}^{(\ell)}(\eta)=L_{\ddagger}\left(\eta \mid X^{(\ell)}\right)$. Then,

$$
\begin{aligned}
\bar{d}_{\mathrm{L}}-\widehat{d}_{\mathrm{L}} & =\frac{2}{m} \sum_{\ell=1}^{m}\left\{L^{(\ell)}\left(\widehat{\psi}^{(\ell)}\right)-L^{(\ell)}\left(\widehat{\psi}_{0}^{(\ell)}\right)-L^{(\ell)}\left(\widehat{\psi}^{*}\right)+L^{(\ell)}\left(\widehat{\psi}_{0}^{*}\right)\right\} \\
& =\frac{2}{m} \sum_{\ell=1}^{m}\left\{L_{\dagger}^{(\ell)}\left(\widehat{\theta}^{(\ell)}\right)-L_{\dagger}^{(\ell)}\left(\widehat{\theta}^{*}\right)\right\} \geqslant 0
\end{aligned}
$$

since $L_{\dagger}^{(\ell)}\left(\hat{\theta}^{(\ell)}\right) \geqslant L_{\dagger}^{(\ell)}\left(\hat{\theta}^{*}\right)$ for all $\ell$.
Proof of Corollary 1. Applying Taylor's expansion on $\psi \mapsto L^{(\ell)}(\psi)$, we can find $\widetilde{\psi}^{(\ell)}$ lying on the line segment joining $\widehat{\psi}^{(\ell)}$ and $\widehat{\psi}_{0}^{(\ell)}$ such that

$$
L^{(\ell)}\left(\widehat{\psi}_{0}^{(\ell)}\right)=L^{(\ell)}\left(\widehat{\psi}^{(\ell)}\right)-\frac{1}{2}\left(\widehat{\psi}_{0}^{(\ell)}-\widehat{\psi}^{(\ell)}\right)^{\top} I^{(\ell)}\left(\widetilde{\psi}^{(\ell)}\right)\left(\widehat{\psi}_{0}^{(\ell)}-\widehat{\psi}^{(\ell)}\right)
$$

where $I^{(\ell)}(\psi)=-\partial^{2} L^{(\ell)}(\psi) / \partial \psi \partial \psi^{\boldsymbol{\top}}$. By the lower order variability of $I^{(\ell)}\left(\widetilde{\psi}^{(\ell)}\right)$, we can find $\widetilde{\psi}^{*}$ such that $I^{(\ell)}\left(\widetilde{\psi}^{(\ell)}\right) \bumpeq I^{(\ell)}\left(\widetilde{\psi}^{*}\right)$ for all $\ell$. Then, using similar techniques as in (B.2) and (B.3), we have

$$
\begin{aligned}
L^{(\ell)}\left(\widehat{\psi}^{(\ell)}\right)-L^{(\ell)}\left(\widehat{\psi}_{0}^{(\ell)}\right) & \bumpeq \frac{1}{2}\left(\widehat{\psi}_{0}^{(\ell)}-\widehat{\psi}^{(\ell)}\right)^{\top} I^{(\ell)}\left(\breve{\psi}^{*}\right)\left(\widehat{\psi}_{0}^{(\ell)}-\widehat{\psi}^{(\ell)}\right) \\
& \bumpeq \frac{1}{2}\left(\theta_{0}-\widehat{\theta}^{(\ell)}\right)^{\top} \breve{U}^{-1}\left(\theta_{0}-\widehat{\theta}^{(\ell)}\right)
\end{aligned}
$$

for some matrix $\breve{U}$. Similarly, we have

$$
L^{(\ell)}\left(\widehat{\psi}^{*}\right)-L^{(\ell)}\left(\widehat{\psi}_{0}^{*}\right) \bumpeq \frac{1}{2}\left(\theta_{0}-\widehat{\theta}^{*}\right)^{\top} \breve{U}^{-1}\left(\theta_{0}-\widehat{\theta}^{*}\right) .
$$

Write $A^{\otimes 2}=A A^{\top}$ for any appropriate matrix $A$. Using (B.4), B.5 and the cyclic property of trace, we have

$$
\begin{aligned}
\bar{d}_{\mathrm{L}}-\widehat{d}_{\mathrm{L}} & \bumpeq \frac{1}{m} \sum_{\ell=1}^{m}\left\{\left(\theta_{0}-\hat{\theta}^{(\ell)}\right)^{\top} \breve{U}^{-1}\left(\theta_{0}-\hat{\theta}^{(\ell)}\right)-\left(\theta_{0}-\hat{\theta}^{*}\right)^{\top} \breve{U}^{-1}\left(\theta_{0}-\hat{\theta}^{*}\right)\right\} \\
& =\operatorname{tr}\left[\breve{U}^{-1}\left\{\frac{1}{m} \sum_{\ell=1}^{m}\left(\theta_{0}-\hat{\theta}^{(\ell)}\right)^{\otimes 2}-\left(\theta_{0}-\hat{\theta}^{*}\right)^{\otimes 2}\right\}\right] \\
& \bumpeq \operatorname{tr}\left[\breve{U}^{-1} \frac{1}{m} \sum_{\ell=1}^{m}\left\{\left(\hat{\theta}^{(\ell)}\right)^{\otimes 2}-\bar{\theta}^{\otimes 2}\right\}\right] \bumpeq \operatorname{tr}\left(\breve{U}^{-1} B\right) \bumpeq \operatorname{tr}\left(\mathcal{U}_{\theta, 0}^{-1} \mathscr{B}_{\theta}\right)
\end{aligned}
$$

as $m, n \rightarrow \infty$, where $\mathscr{U}_{\theta, 0}$ is a deterministic matrix that depends on both $\theta_{0}$ and the true value of $\theta$, and satisfies $n\left(\breve{U}-\mathscr{U}_{\theta, 0}\right) \xrightarrow{\mathrm{pr}} 0$. Note that $\operatorname{tr}\left(\mathscr{U}_{\theta, 0}^{-1} \mathscr{B}_{\theta}\right)=k \varkappa_{0}$, for some finite $\varkappa_{0}$ by Assumption 2. Then $\widehat{r}_{\mathrm{L}} \xrightarrow{\mathrm{pr}} \varkappa_{0}=\operatorname{tr}\left(U_{\theta, 0}^{-1} \mathscr{B}_{\theta}\right) / k$, proving (ii). (But $\mathscr{U}_{\theta, 0}$ may not equal to $\mathscr{U}_{\theta}$, and hence $\hat{r}_{\mathrm{L}}$ may not be consistent for $r_{m}$.)

If $H_{0}$ is true, then $\bar{\theta} \xrightarrow{\mathrm{pr}} \theta_{0}$ and $\widetilde{U} \bumpeq \bar{U} \bumpeq \mathscr{U}_{\theta}=\mathscr{U}_{\theta, 0}$. Then, $\widehat{r}_{\mathrm{L}} \xrightarrow{\mathrm{pr}} r$ as $m, n \rightarrow \infty$. So, (i) follows.

Proof of Theorem 2. (i, ii) It is trivial by the definition of $\widehat{r}_{\mathrm{L}}$. (iii) Applying Taylor's expansion to $\psi \mapsto L^{(\ell)}(\psi)$ again, we know there is $\widetilde{\psi}^{(\ell)}$ lying on the line segment joining $\widehat{\psi}^{(\ell)}$ and $\widehat{\psi}^{*}$ such that

$$
L^{(\ell)}\left(\widehat{\psi}^{*}\right)=L^{(\ell)}\left(\widehat{\psi}^{(\ell)}\right)-\frac{1}{2}\left(\widehat{\psi}^{*}-\widehat{\psi}^{(\ell)}\right)^{\top} I^{(\ell)}\left(\breve{\psi}^{(\ell)}\right)\left(\widehat{\psi}^{*}-\widehat{\psi}^{(\ell)}\right)
$$

By the lower order variability of $I^{(\ell)}\left(\widetilde{\psi}^{(\ell)}\right)$, we know that $I^{(\ell)}\left(\widetilde{\psi}^{(\ell)}\right) \bumpeq \bar{I}\left(\widehat{\psi}^{*}\right)$ for all $\ell$, where $\bar{I}(\psi)=m^{-1} \sum_{\ell=1}^{m} I^{(\ell)}(\psi)$. We also know that $\widehat{\psi}^{*} \bumpeq \bar{\psi}$. Thus

$$
\begin{aligned}
\bar{\delta}_{\mathrm{L}}-\widehat{\delta}_{\mathrm{L}} & \bumpeq \frac{1}{m} \sum_{\ell=1}^{m}\left(\widehat{\psi}^{*}-\widehat{\psi}^{(\ell)}\right)^{\top} \bar{I}\left(\widehat{\psi}^{*}\right)\left(\widehat{\psi}^{*}-\widehat{\psi}^{(\ell)}\right) \\
& =\operatorname{tr}\left\{\bar{I}\left(\widehat{\psi}^{*}\right) \frac{1}{m} \sum_{\ell=1}^{m}\left(\widehat{\psi}^{*}-\widehat{\psi}^{(\ell)}\right)^{\otimes 2}\right\} \\
& \bumpeq \operatorname{tr}\left\{\bar{I}\left(\widehat{\psi}^{*}\right) \frac{1}{m} \sum_{\ell=1}^{m}\left(\widehat{\psi}^{(\ell)}-\bar{\psi}\right)^{\otimes 2}\right\} \bumpeq \operatorname{tr}\left(\mathscr{U}_{\psi}^{-1} \mathscr{B}_{\psi}\right)
\end{aligned}
$$

as $m, n \rightarrow \infty$. By the assumption of EFMI of $\psi$, we have $\widehat{r}_{\mathrm{L}}^{\widehat{p r}} \xrightarrow{p}$.
Proof of Lemma 1. First, recall that, as $n \rightarrow \infty$, the observed data MLE $\hat{\theta}_{\text {obs }}$ of $\theta$ satisfies (2.4), which can be written as $\left[\hat{\theta}_{\text {obs }} \mid \theta\right] \stackrel{\mathscr{D}}{\approx} \mathscr{N}_{k}\left(\theta, \mathscr{T}_{\theta}\right)$, where $A_{1, n} \stackrel{\mathscr{D}}{\approx} A_{2, n}$ means that $A_{1, n}$ and $A_{2, n}$ have the same asymptotic distribution, i.e., there exist deterministic sequences $\mu_{n}$ and $\Sigma_{n}$ such that $\left(A_{1, n}-\mu_{n}\right) \Sigma_{n}^{-1 / 2} \Rightarrow A$ and $\left(A_{2, n}-\mu_{n}\right) \Sigma_{n}^{-1 / 2} \Rightarrow A$ for some non-degenerate random variable $A$. From Assumption 3, a proper imputation model is used. So, we have (2.5), which is equivalent to say that, as $n \rightarrow \infty$,

$$
\left[\hat{\theta}^{(\ell)} \mid X_{\mathrm{obs}}\right] \stackrel{\mathscr{N}}{\approx} \mathscr{N}_{k}\left(\hat{\theta}_{\mathrm{obs}}, \mathscr{B}_{\theta}\right)
$$

independently for for $\ell=1, \ldots, m$. Therefore we can represent

$$
\begin{aligned}
\hat{\theta}_{\mathrm{obs}} & \stackrel{\mathscr{D}}{\approx} \theta+\mathscr{T}_{\theta}^{1 / 2} W, \\
\hat{\theta}^{(\ell)} & \stackrel{\mathscr{D}}{\approx} \hat{\theta}_{\mathrm{obs}}+\mathscr{B}_{\theta}^{1 / 2} Z_{\ell}, \quad \ell=1, \ldots, m
\end{aligned}
$$

where $Z_{1}, \ldots, Z_{m}, W \stackrel{\mathrm{iid}}{\sim} \mathcal{N}_{k}\left(0, I_{k}\right)$. Also write $Z_{\ell}=\left(Z_{1 \ell}, \ldots, Z_{k \ell}\right)^{\top}$, for $\ell= 1,2, \ldots, m$, and $W=\left(W_{1}, \ldots, W_{k}\right)^{\top}$. Averaging B.10 over $\ell$, we have $\bar{\theta} \mathscr{Z} \hat{\theta}_{\text {obs }}+\mathscr{B}_{\theta}^{1 / 2} \bar{Z}_{\bullet}$, where $\bar{Z}_{\bullet}=m^{-1} \sum_{\ell=1}^{m} Z_{\ell}$. Since $\mathscr{B}_{\theta}=\mathcal{H}_{\theta}$, we have

$$
\begin{aligned}
\mathcal{U}_{\theta}^{-1 / 2}\left(\hat{\theta}^{(\ell)}-\theta\right) & \stackrel{\mathscr{D}}{\approx}\left(1+r^{\circ}\right)^{1 / 2} W+r^{1 / 2} Z_{\ell} \\
\mathcal{U}_{\theta}^{-1 / 2}(\bar{\theta}-\theta) & \stackrel{\mathscr{D}}{\approx}(1+r)^{1 / 2} W+r^{1 / 2} \bar{Z}_{\bullet}
\end{aligned}
$$

Note that 2.6 implies $\mathscr{U}_{\theta} \bumpeq \bar{U}$. Under $H_{0}$, we have $\theta=\theta_{0}$ and

$$
\begin{aligned}
& \bar{d}_{\mathrm{L}} \bumpeq \bar{d}_{\mathrm{W}}^{\prime} \stackrel{\mathscr{D}}{\sim} \sum_{i=1}^{k}\left\{(1+r)^{1 / 2} W_{i}+r^{1 / 2} Z_{i \ell}\right\}^{2} \\
& \hat{d}_{\mathrm{L}} \bumpeq \widetilde{d}_{\mathrm{L}} \bumpeq \widetilde{d}_{\mathrm{W}}^{\prime} \stackrel{\mathscr{D}}{\approx} \sum_{i=1}^{k}\left\{(1+r)^{1 / 2} W_{i}+r^{1 / 2} \bar{Z}_{i}\right\}^{2}
\end{aligned}
$$

After some simple algebra, we obtain

$$
\hat{r}_{\mathrm{L}}^{+} \approx \frac{(m+1) r}{m k} \sum_{i=1}^{k} s_{Z_{i}}^{2} \quad \text { and } \quad \hat{D}_{\mathrm{L}}^{+} \stackrel{\mathscr{D}}{\approx} \frac{m \sum_{i=1}^{k}\left\{(1+r)^{1 / 2} W_{i}+r^{1 / 2} \bar{Z}_{i \bullet}\right\}^{2}}{m k+(m+1) r \sum_{i=1}^{k} s_{Z_{i}}^{2}}
$$

where $s_{Z_{i}}^{2}=(m-1)^{-1} \sum_{\ell=1}^{m}\left(Z_{i \ell}-\bar{Z}_{i \bullet}\right)^{2}$ is the sample variance of $\left\{Z_{i \ell}\right\}_{\ell=1}^{m}$. Since $W_{i}, \bar{Z}_{i \bullet}$ and $s_{Z_{i}}^{2}$ are mutually independent for each fixed $i$, we can simplify the representation of $\widehat{D}_{\mathrm{L}}^{+}$to

$$
\hat{r}_{\mathrm{L}}^{+} \neq \frac{(m+1) r}{m(m-1) k} \sum_{i=1}^{k} H_{i}^{2} \quad \text { and } \quad \hat{D}_{\mathrm{L}}^{+} \neq \frac{\mathscr{D}}{m(m-1)\{m+(m+1) r\} \sum_{i=1}^{k} G_{i}^{2}}
$$

where $G_{i}^{2} \stackrel{\mathrm{iid}}{\sim} \chi_{1}^{2}$ and $H_{i}^{2} \stackrel{\mathrm{iid}}{\sim} \chi_{m-1}^{2}$, for $i=1, \ldots, k$, are all mutually independent. Clearly, they can be further simplified to (2.12).
Proof of Theorem 3. Similar to (B.9) and (B.10), we can have a more general representation:

$$
\hat{\psi}_{\mathrm{obs}} \stackrel{\mathscr{D}}{\approx} \psi+\mathscr{T}_{\psi}^{1 / 2} W ; \quad \hat{\psi}^{(\ell)} \stackrel{\mathscr{D}}{\approx} \hat{\psi}_{\mathrm{obs}}+\mathscr{B}_{\psi}^{1 / 2} Z_{\ell}, \quad \ell=1, \ldots, m
$$

where $Z_{1}, \ldots, Z_{h}, W \stackrel{\mathrm{iid}}{\sim} \mathcal{N}_{h}\left(0, I_{h}\right)$. Also write $Z_{\ell}=\left(Z_{1 \ell}, \ldots, Z_{h \ell}\right)^{\top}$, for $\ell= 1,2, \ldots, m$, and $W=\left(W_{1}, \ldots, W_{h}\right)^{\top}$. Using (B.7), we have

$$
\begin{aligned}
\bar{\delta}_{\mathrm{L}}-\widehat{\delta}_{\mathrm{L}} & \bumpeq \operatorname{tr}\left\{\bar{I}\left(\widehat{\psi}^{*}\right) \frac{1}{m} \sum_{\ell=1}^{m}\left(\widehat{\psi}^{(\ell)}-\bar{\psi}\right)\left(\widehat{\psi}^{(\ell)}-\bar{\psi}\right)^{\top}\right\} \\
& \approx \operatorname{tr}\left\{\mathcal{U}_{\psi}^{-1} \frac{1}{m} \sum_{\ell=1}^{m}\left[\left(\mathscr{T}_{\psi}-\mathscr{U}_{\psi}\right)^{1 / 2}\left(Z_{\ell}-\bar{Z}_{\bullet}\right)\right]^{\otimes 2}\right\} \\
& =\frac{1}{m} \sum_{\ell=1}^{m} \operatorname{tr}\left\{r^{\prime} I_{h}\left(Z_{\ell}-\bar{Z}_{\bullet}\right)^{\otimes 2}\right\}=\frac{r}{m} \sum_{\ell=1}^{m} \sum_{i=1}^{h}\left(Z_{i \ell}-\bar{Z}_{i_{\bullet}}\right)^{2}
\end{aligned}
$$

Equivalently, we can say $\bar{\delta}_{\mathrm{L}}-\widehat{\delta}_{\mathrm{L}} \Rightarrow r^{\prime} \chi_{h(m-1)}^{2} / m$ as $n \rightarrow \infty$. Hence

$$
\widehat{r}_{\mathrm{L}}^{\widehat{ }} \Rightarrow r \cdot \frac{m+1}{h m(m-1)} \cdot \chi_{h(m-1)}^{2}
$$

which is equivalent to (2.13). Note that it is true under both $H_{0}$ and $H_{1}$.
Proof of Theorem 4. From the representations of $\hat{d}_{\mathrm{L}}^{\diamond}$ and $\widehat{r}_{\mathrm{L}}$ in Lemma 1 and Theorem 3, we know that they are asymptotically ( $n \rightarrow \infty$ ) independent. The proof then follows the derivation for Lemma 1 .

Proof of Theorem 5. (i) Using the representation (A.3), we can easily see that $\widehat{r}_{\mathrm{L}}^{\triangle} \geqslant 0$. (ii) It suffices to show

$$
m^{-1} \sum_{\ell=1}^{m} d_{\mathrm{L}}\left(\hat{\psi}_{0}^{(\ell)}+\Delta_{m}, \hat{\psi}^{(\ell)} \mid X^{(\ell)}\right) \bumpeq \bar{d}_{\mathrm{L}}-\widetilde{d}_{\mathrm{L}}
$$

where $\Delta_{m}=\widehat{\psi}^{*}-\widehat{\psi}_{0}^{*}$. Under $H_{0}, \Delta_{m} \bumpeq 0$ and $\widehat{\psi}_{0}^{(\ell)} \bumpeq \widehat{\psi}^{(\ell)}$, so $\widehat{\psi}_{0}^{(\ell)}+\Delta_{m} \bumpeq \widehat{\psi}^{(\ell)}$. Using Taylor's expansion on $\psi \mapsto L^{(\ell)}(\psi)$ around its maximizer $\widehat{\psi}^{(\ell)}$, we have for $\psi \bumpeq \widehat{\psi}^{(\ell)}$ that

$$
L^{(\ell)}(\psi) \bumpeq L^{(\ell)}\left(\widehat{\psi}^{(\ell)}\right)-\frac{1}{2}\left(\psi-\widehat{\psi}^{(\ell)}\right)^{\top} I^{(\ell)}\left(\widehat{\psi}^{(\ell)}\right)\left(\psi-\widehat{\psi}^{(\ell)}\right)
$$

Under the parametrization of $\psi$ in the proof of Theorem 1, we know that the upper $k \times k$ sub-matrix of $I^{(\ell)}\left(\widehat{\psi}^{(\ell)}\right)$ is $\left(U^{(\ell)}\right)^{-1}$. Using the lower order variability of $U^{(\ell)}$, we have $\left(U^{(\ell)}\right)^{-1} \bumpeq \bar{U}^{-1}$ and

$$
\begin{aligned}
\frac{1}{m} \sum_{\ell=1}^{m} d_{\mathrm{L}}\left(\widehat{\psi}_{0}^{(\ell)}+\Delta_{m}, \widehat{\psi}^{(\ell)} \mid X^{(\ell)}\right) & \bumpeq \frac{1}{m} \sum_{\ell=1}^{m}\left(\widehat{\psi}_{0}^{(\ell)}+\Delta_{m}-\widehat{\psi}^{(\ell)}\right)^{\top} I^{(\ell)}\left(\widehat{\psi}^{(\ell)}\right)\left(\widehat{\psi}_{0}^{(\ell)}+\Delta_{m}-\widehat{\psi}^{(\ell)}\right) \\
& \bumpeq \frac{1}{m} \sum_{\ell=1}^{m}\left(\widehat{\theta}^{(\ell)}-\bar{\theta}\right)^{\top} \bar{U}^{-1}\left(\hat{\theta}^{(\ell)}-\bar{\theta}\right)=\bar{d}_{\mathrm{W}}^{\prime}-\widetilde{d}_{\mathrm{W}}^{\prime} \bumpeq \bar{d}_{\mathrm{L}}-\hat{d}_{\mathrm{L}} .
\end{aligned}
$$

Therefore, the desired result follows.
Proof of Theorem 6. Throughout this proof, conditions (a), (b) and (c) refer to the list given in Assumption 5. (i, ii) It trivially follows from the definitions
of $\hat{d}_{\mathrm{S}}$ and $\hat{r}_{\mathrm{S}}$. (iii) First, by the definition of maximizer and condition (a), we have

$$
\begin{aligned}
\underline{\bar{L}}\left(\hat{\psi}^{*}\right)-\underline{\bar{L}}\left(\hat{\psi}^{\mathrm{S}}\right) & =\bar{L}\left(\hat{\psi}^{*}\right)-\underline{\bar{L}}^{\mathrm{S}}\left(\hat{\psi}^{\mathrm{S}}\right)+\underline{\bar{L}}^{\mathrm{S}}\left(\hat{\psi}^{\mathrm{S}}\right)-\underline{\bar{L}}\left(\hat{\psi}^{\mathrm{S}}\right) \\
& \leqslant \bar{L}\left(\hat{\psi}^{*}\right)-\bar{L}^{\mathrm{S}}\left(\hat{\psi}^{*}\right)+\overline{\bar{L}}^{\mathrm{S}}\left(\hat{\psi}^{\mathrm{S}}\right)-\bar{L}\left(\hat{\psi}^{\mathrm{S}}\right) \\
& \leqslant 2 \sup _{\psi \in \Psi}\left|\underline{L}(\psi)-\bar{L}^{\mathrm{S}}(\psi)\right|=O_{p}(1 / n)
\end{aligned}
$$

which, together with condition (b), imply that

$$
\begin{aligned}
\overline{\mathscr{L}}\left(\psi^{*}\right)-\overline{\mathscr{L}}\left(\hat{\psi}^{\mathrm{S}}\right) & =\left\{\overline{\mathscr{L}}\left(\psi^{*}\right)-\bar{L}\left(\psi^{*}\right)\right\}+\left\{\bar{L}\left(\psi^{*}\right)-\underline{L}\left(\hat{\psi}^{\mathrm{S}}\right)\right\}+\left\{\bar{L}\left(\hat{\psi}^{\mathrm{S}}\right)-\overline{\mathscr{L}}\left(\hat{\psi}^{\mathrm{S}}\right)\right\} \\
& \leqslant 2 \sup _{\psi \in \Psi}|\bar{L}(\psi)-\underline{\bar{L}}(\psi)|+\left\{\bar{L}\left(\hat{\psi}^{*}\right)-\bar{L}\left(\hat{\psi}^{\mathrm{S}}\right)\right\}=o_{p}(1)
\end{aligned}
$$

Using (B.11) and (c), we have $\hat{\psi}^{\mathrm{S}} \xrightarrow{\mathrm{pr}} \psi^{*}$. By (b) and (c), we also have $\hat{\psi}^{*} \xrightarrow{\mathrm{pr}} \psi^{*}$. So, $\left|\widehat{\psi}^{\mathrm{S}}-\widehat{\psi}^{*}\right| \xrightarrow{\mathrm{pr}} \mathbf{0}$ as $n \rightarrow \infty$. By the definition of maximizer,

$$
\mathbf{0}=\nabla \underline{\bar{L}}^{\mathrm{S}}\left(\widehat{\psi}^{\mathrm{S}}\right)=\nabla \underline{\bar{L}}\left(\hat{\psi}^{\mathrm{S}}\right)+\nabla R\left(\hat{\psi}^{\mathrm{S}}\right)
$$

where $\nabla g(\psi)=\partial g(\psi) / \partial \psi$ is the gradient of $\psi \mapsto g(\psi)$. By condition (a), we know $\nabla R\left(\widehat{\psi}^{\mathrm{S}}\right)=O_{p}(1 / n)$. Thus, together with B.12, we have $\nabla \underline{\bar{L}}\left(\hat{\psi}^{\mathrm{S}}\right)= O_{p}(1 / n)$. Also, by the definition of MLE, we have $\nabla \overline{\underline{L}}\left(\hat{\psi}^{*}\right)=\mathbf{0}$.

By Taylor's expansion, there exists $\widetilde{\psi}$ such that

$$
\underline{\bar{L}}\left(\widehat{\psi}^{*}\right)-\underline{\bar{L}}\left(\hat{\psi}^{\mathrm{S}}\right)=\{\nabla \underline{\bar{L}}(\widetilde{\psi})\}^{\top}\left(\widehat{\psi}^{*}-\widehat{\psi}^{\mathrm{S}}\right)=o_{p}(1 / n)
$$

where we have used the continuity of $\psi \mapsto \nabla \underline{\bar{L}}(\psi)$ to yield $\nabla \underline{\bar{L}}(\widetilde{\psi})=O_{p}(1 / n)$. Rewriting (B.13), we have

$$
\underline{\bar{L}}\left(\hat{\psi}^{*}\right)-\underline{\bar{L}}^{\mathrm{S}}\left(\widehat{\psi}^{\mathrm{S}}\right)=R\left(\hat{\psi}^{\mathrm{S}}\right)+o_{p}(1 / n)
$$

Similar to (B.14), we have

$$
\underline{\bar{L}}\left(\widehat{\psi}_{0}^{*}\right)-\underline{\bar{L}}^{\mathrm{S}}\left(\widehat{\psi}_{0}^{\mathrm{S}}\right)=R\left(\widehat{\psi}_{0}^{\mathrm{S}}\right)+o_{p}(1 / n)
$$

Then, using (B.14) and (B.15), we have

$$
\begin{aligned}
\left|\hat{d}_{\mathrm{L}}-\hat{d}_{\mathrm{S}}\right| & =2 n\left|\left\{\overline{\underline{L}}\left(\hat{\psi}^{*}\right)-\underline{\underline{L}}^{\mathrm{S}}\left(\hat{\psi}^{\mathrm{S}}\right)\right\}-\left\{\underline{\underline{L}}\left(\hat{\psi}_{0}^{*}\right)-\underline{\underline{L}}^{\mathrm{S}}\left(\hat{\psi}_{0}^{\mathrm{S}}\right)\right\}\right| \\
& =2 n\left|R\left(\hat{\psi}^{\mathrm{S}}\right)-R\left(\hat{\psi}_{0}^{\mathrm{S}}\right)+o_{p}(1 / n)\right|
\end{aligned}
$$

Now consider two cases.
(i) Under $H_{0}$, we have $\widehat{d}_{\mathrm{L}}=O_{p}(1)$ and $\widehat{\psi}_{0}^{\mathrm{S}} \bumpeq \widehat{\psi}^{\mathrm{S}}$. Thus condition (a) implies $R\left(\widehat{\psi}^{\mathrm{S}}\right)-R\left(\hat{\psi}_{0}^{\mathrm{S}}\right)=o_{p}(1 / n)$. Then, we have $\left|\hat{d}_{\mathrm{L}}-\hat{d}_{\mathrm{S}}\right|=o_{p}\left(\hat{d}_{\mathrm{L}}\right)$.
(ii) Under $H_{1}$, we have $\hat{d}_{\mathrm{L}} \xrightarrow{\mathrm{pr}} \infty$. Condition (a) and B.11 imply that $\bar{L}\left(\widehat{\psi}^{*}\right)-\underline{\bar{L}}^{\mathrm{S}}\left(\widehat{\psi}^{\mathrm{S}}\right)=O_{p}(1 / n)$. Similarly, we also have $\underline{\bar{L}}\left(\hat{\psi}_{0}^{*}\right)-\underline{\bar{L}}^{\mathrm{S}}\left(\widehat{\psi}_{0}^{\mathrm{S}}\right)= O_{p}(1 / n)$. Hence $\left|\hat{d}_{\mathrm{L}}-\hat{d}_{\mathrm{S}}\right|=O_{p}(1)$. Thus we have $\left|\hat{d}_{\mathrm{L}}-\hat{d}_{\mathrm{S}}\right|=o_{p}\left(\hat{d}_{\mathrm{L}}\right)$.

Therefore, under either $H_{0}$ or $H_{1}$, we also have $\left|\hat{d}_{\mathrm{L}}-\hat{d}_{\mathrm{S}}\right|=o_{p}\left(\hat{d}_{\mathrm{L}}\right)$. Since $\widehat{d}_{\mathrm{L}} \bumpeq \widehat{d}_{\mathrm{S}}$ and $\bar{d}_{\mathrm{L}}=\bar{d}_{\mathrm{S}}$, we know $\widehat{r}_{\mathrm{L}} \bumpeq \widehat{r}_{\mathrm{S}}$.

Note that, even under the assumption of this theorem, $\widehat{r}_{\mathrm{S}}$ and $\widehat{r}_{\mathrm{S}}$ are not equivalent. From (A.7) and A.8, $\widehat{r}_{\mathrm{S}}$ and $\widehat{r}_{\mathrm{S}}$ are a "difference of difference" estimator and a "difference" estimator, respectively. So, the "bias" of using $\bar{L}^{\mathrm{S}}(\psi)$ cannot be canceled out in $\widehat{r}_{\mathrm{S}}^{\widehat{s}}$.

Nominal size $\alpha=5$ \%

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-50.jpg?height=1703&width=1320&top_left_y=476&top_left_x=309)
Figure 10: The power curves under different parametrizations. The nominal size is $\alpha=5 \%$. In each plot, the vertical axis denotes the power, whereas the horizontal axis denotes the value of $\delta=\mu_{2}-\mu_{1}$. The legend in Figure 8 also applies here.

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-51.jpg?height=1741&width=1313&top_left_y=438&top_left_x=305)
Figure 11: The ratios of empirical power to empirical size under different parametrizations. The nominal size is $\alpha=0.5 \%$. In each plot, the vertical axis denotes the ratio, and the horizontal axis denotes $\delta=\mu_{2}-\mu_{1}$. The legend in Figure 8 also applies here. The results under nominal size $5 \%$ are shown in Figure 12.

Nominal size $\alpha=5$ \%

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-52.jpg?height=1703&width=1309&top_left_y=476&top_left_x=309)
Figure 12: The ratios of empirical power to empirical size under different parametrizations. The nominal size is $\alpha=5 \%$. In each plot, the vertical axis denotes the ratio, whereas the horizontal axis denotes $\delta=\mu_{2}-\mu_{1}$. The legend in Figure 8 also applies here.

Mean-squared error of estimators of FMI

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-53.jpg?height=1703&width=1335&top_left_y=476&top_left_x=305)
Figure 13: The MSEs of estimators of $f_{m}$ used in the test statistics. The vertical axis denotes the log of MSE, whereas the horizontal axis denotes the value of $\delta= \mu_{2}-\mu_{1}$. The legend in Figure 8 also applies here.

![](https://cdn.mathpix.com/cropped/e2ac8ec1-3554-40c7-a37d-ee18810f2b55-54.jpg?height=974&width=1365&top_left_y=730&top_left_x=283)
Figure 14: The empirical size, empirical power, and their ratio. The first row of plots show the empirical sizes. The size of the complete-case test (C2) under MAR is off the chart (always equals to one) because it is invalid. The second and third rows of plots show the powers and the power-to-size ratios, respectively, where the nominal size is $0.5 \%$.


[^0]:    ${ }^{a}$ In actual computation, the $\varkappa_{m}$ in the denominator degree of freedom of $F$ is replaced by its corresponding estimator.
    ${ }^{b}$ Computing the test statistic $D_{\mathrm{W}}(T)=d_{\mathrm{W}}(\bar{\theta}, T) / k$ does not require estimating $r_{m}$.
    ${ }^{c}$ EFMI is not required for the test statistic $D_{\mathrm{W}}(T)$, but it is required for its approximate null distribution.
    ${ }^{d}$ The approximate null distribution documented in Rubin (2004) was modified by Li et al. (1991a). This also applies to WT-2,4,5.
    ${ }^{e}$ The estimator $\widetilde{r}_{\text {W }}^{\prime}$ does not depend on $\theta_{0}$, but its MSE may be inflated under $H_{1}$ if a bad parametrization of $\theta$ is used.
    ${ }^{f}$ The originally proposed combining rule is $\bar{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)$; see A.13). Although $\bar{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)$ is more computational feasible, the power loss is more significant than $\widetilde{D}_{\mathrm{W}}^{\prime}\left(\varkappa_{m}\right)$ after inserting an inefficient estimator $\widetilde{r}_{\mathrm{W}, 1}^{\prime}$ for $\varkappa_{m}$. This footnote also applies to WT-3.
    ${ }^{g}$ Averaging and processing vector estimators of $\psi$, but not their covariance matrixes, is needed. This footnote also applies to LRT-2.
    ${ }^{h}$ It is a trivial modification of the original proposal in MR92 by replacing $\widetilde{r}_{\mathrm{L}}$ with $\widetilde{r}_{\mathrm{L}}^{+}=\max \left\{0, \widetilde{r}_{\mathrm{L}}\right\}$.

