---
citekey: patriotaBiasCorrectionMultivariate2009
item_type: article
authors: 'Patriota, Alexandre G. and Lemonte, Artur J.'
year: 2009
title: Bias Correction in a Multivariate Normal Regression Model with General Parameterization
venue: 'Statistics \& Probability Letters'
volume: 79
issue: 15
pages: 1655--1662
doi: 10.1016/j.spl.2009.04.018
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\patriota_bias_correction_multivariate_2009.pdf'
pdf_sha256: 5a58193d684d43f939791974b6089f61f11e053a91f9cf2d0eda570c736bac33
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T23:14:22Z
---
# Bias correction in a multivariate normal regression model with general parameterization 

Alexandre G. Patriota, Artur J. Lemonte<br>Departamento de Estatística, Universidade de São Paulo, Rua do Matão, 1010, São Paulo/SP, 05508-090, Brazil


#### Abstract

This paper develops a bias correction scheme for a multivariate normal model under a general parameterization. In the model, the mean vector and the covariance matrix share the same parameters. It includes many important regression models available in the literature as special cases, such as (non)linear regression, errors-in-variables models, and so forth. Moreover, heteroscedastic situations may also be studied within our framework. We derive a general expression for the second-order biases of maximum likelihood estimates of the model parameters and show that it is always possible to obtain the second order bias by means of ordinary weighted lest-squares regressions. We enlighten such general expression with an errors-in-variables model and also conduct some simulations in order to verify the performance of the corrected estimates. The simulation results show that the bias correction scheme yields nearly unbiased estimators. We also present an empirical ilustration.


Key Words: Bias correction, errors-in-variables model, maximum likelihood estimation, multivariate regression.

## 1 Introduction

Applications of multivariate normal models are commonly found in the literature. There are simple models that do not require asymptotic approximations for the maximum likelihood estimators. Nevertheless, in the majority of problems, the estimation procedure in such multivariate normal models embrace on the asymptotic theory. For instance, it is hard to compute the exact distribution of maximum likelihood estimators (MLEs) for nonlinear multivariate regressions, errors-in-variables models and many others when the sample size is finite (practical situations). Then, in the practical applications, the asymptotic distribution of the MLE is used as an approximation to its exact distribution. It considerable simplifies the inferential process. In general, under some regularity conditions, the MLEs are consistent and efficient, i.e., asymptotically, their biases converge to zero and their variancecovariance matrices approach the inverse of the Fisher information. Moreover, under
such regularity conditions, the MLEs are asymptotically normally distributed. Although the MLEs have these important features, they may be strongly biased for small or even moderate samples sizes when more complex models are considered. Thus, a bias correction can play an important role to improve the estimation of the model parameters.

An important area of research in statistics is the study of the finite-sample behavior of MLEs. It is well konwn that MLEs are oftentimes biased, thus displaying systematic error. This is not a serious problem for relatively large sample sizes, since the bias is typically of order $\mathcal{O}\left(n^{-1}\right)$, whereas the asymptotic standard errors are of order $\mathcal{O}\left(n^{-1 / 2}\right)$. However, for small or even moderate values of the sample size $n$, bias can constitute a problem. Thus, availability of formulae for its approximate computation is important for accurate estimation of many models that are used in a number of applications. Bias correction of MLEs is particularly important when the sample size, or the total information, is small (Vasconcellos and Cribari-Neto, 2005).

Bias adjustment has been extensively studied in the statistical literature. Box (1971) gives a general expression for the $n^{-1}$ bias in multivariate nonlinear models where covariance matrices are known. For nonlinear regression models, Cook et al. (1986) relate bias to the position of the explanatory variables in the sample space. Cordeiro and McCullagh (1991) give general matrix formulae for bias correction in generalized linear models. Cordeiro and Vasconcellos (1997) obtained general matrix formulae for bias correction in multivariate nonlinear regression models with normal errors, while Vasconcellos and Cordeiro (1997) obtained general formulae for bias in multivariate nonlinear heteroscedastic regression. Also, Cordeiro and Vasconcellos (1999) obtained second order biases of the maximum likelihood estimators in von Mises regression models, while Cordeiro et al. (2000) obtained bias correction for symmetric nonlinear regression models. Vasconcellos and Cordeiro (2000) obtained bias correction for multivariate nonlinear Student $t$ regression models. More recently, Vasconcellos and Cribari-Neto (2005) obtained bias correction in a new class of beta regressions. Cordeiro and Demétrio (2008) derive formulae for the second-order biases of the quasi-maximum likelihood estimators, while Cordeiro and Toyama (2008) derive general formulae for the second-order biases in generalized nonlinear models with dispersion covariates.

In this paper we study a multivariate normal model with general parameterization and derive the second-order biases of the maximum likelihood estimates. Here, the general parameterization means a sort of unification of several important models which can be constructed using the multivariate normal model. For instance, the multivariate nonlinear regressions studied by Cordeiro and Vasconcellos (1997) and their heteroscedastic version (Vasconcellos and Cordeiro, 1997) are just particular cases of our proposal. In this paper we propose a model in which the mean $\boldsymbol{\mu}$ and the variance $\boldsymbol{\Sigma}$ of the observed variables are indexed by the same vector of parameters, say $\boldsymbol{\theta}$. The existing works on bias correction assume that the mean and variance do not share any parameters, however, in errors-in-variables models, for example, this assumption is not realistic. Indeed, that assumption makes the computation of the bias formulae less complicated, but it restricts the applicability of the approach to a special class of models. In view of that, the main goal of this article is to extend
the bias correction to a wide class of multivariate models which has not yet been considered in the statistical literature.

The outline of the paper is as follows. Section 2 presents the main model and computes the first three derivatives of the log-likelihood function and their expectations. In Section 3, we present matrix formulae for the second-order biases of the MLEs for the general model. In Section 4, we present some useful examples of the proposed formulation. Monte Carlo simulation results are presented and discussed in Section 5. The numerical results show that the bias correction we derive is effective in small samples; it delivers estimators that are nearly unbiased and display superior finite-sample behavior. Section 6 contains an empirical ilustration. Finally, Section 7 concludes the paper.

## 2 Model specification

We consider the situation in which $n$ independent multivariate random variables $\boldsymbol{Y}_{1}, \ldots, \boldsymbol{Y}_{n}$ are observed and the number of responses measured in each observation is $q$. We also admit that auxiliary covariates can be observed, say $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{n}$. The multivariate regression model can then be represented as

$$
\boldsymbol{Y}_{i}=\boldsymbol{\mu}_{i}(\boldsymbol{\theta})+\boldsymbol{u}_{i}, \quad i=1,2, \ldots, n
$$

where $\boldsymbol{Y}_{i}$ is a $q \times 1$ vector of dependent variables, $\boldsymbol{\mu}_{i}(\boldsymbol{\theta}) \equiv \boldsymbol{\mu}_{i}\left(\boldsymbol{\theta}, \boldsymbol{X}_{i}\right)$ is a mean function (the shape is assumed known) which is three times continuously differentiable with respect to each element of $\boldsymbol{\theta}$ and $\boldsymbol{X}_{i}$ is an $m \times 1$ vector of known explanatory variables associated with the $i^{\text {th }}$ observed response $\boldsymbol{Y}_{i}$. Also, $\boldsymbol{\theta}$ is a $p \times 1$ vector of unknown parameters of interest. Additionally, as the foundation for estimation by maximum likelihood and hypothesis testing, we assume that the independent random errors $\boldsymbol{u}_{i}$ 's follow a multivariate normal $\mathcal{N}_{q}\left(\mathbf{0}, \boldsymbol{\Sigma}_{i}(\boldsymbol{\theta})\right)$ distribution, where $\boldsymbol{\Sigma}_{i}(\boldsymbol{\theta})$ is a $q \times q$ nonsingular covariance matrix and the entries of $\boldsymbol{\Sigma}_{i}(\boldsymbol{\theta})$ are assumed three times continuously differentiable in each element of $\boldsymbol{\theta}$. We are assuming, in addition, that the functions $\boldsymbol{\mu}_{i}(\boldsymbol{\theta})$ and $\boldsymbol{\Sigma}_{i}(\boldsymbol{\theta})$ are defined in a convenient way since $\boldsymbol{\theta}$ must be identifiable in model (1).

The class of models presented above is very rich and includes many important regression models. For example, in an errors-in-variables model we observe two variables, namely $Y_{i}$ and $X_{i}$ whose relationship is given by

$$
Y_{i}=\alpha+\beta x_{i}+e_{i} \quad \text { and } \quad X_{i}=x_{i}+u_{i}
$$

where $x_{i} \sim \mathcal{N}\left(\mu_{x}, \sigma_{x}^{2}\right), e_{i} \sim \mathcal{N}\left(0, \sigma^{2}\right)$ and $u_{i} \sim \mathcal{N}\left(0, \sigma_{u}^{2}\right)$, with $\sigma_{u}^{2}$ known and, additionally, $x_{i}, e_{i}$ and $u_{i}$ are mutually uncorrelated. Then, denoting $\boldsymbol{Y}_{i}=\left(Y_{i}, X_{i}\right)^{\top}$ and $\boldsymbol{\theta}=\left(\alpha, \beta, \mu_{x}, \sigma_{x}^{2}, \sigma^{2}\right)^{\top}$ we have that $\boldsymbol{Y}_{i} \sim \mathcal{N}_{2}(\boldsymbol{\mu}(\boldsymbol{\theta}), \boldsymbol{\Sigma}(\boldsymbol{\theta}))$, where

$$
\boldsymbol{\mu}(\boldsymbol{\theta})=\binom{\alpha+\beta \mu_{x}}{\mu_{x}} \quad \text { and } \quad \boldsymbol{\Sigma}(\boldsymbol{\theta})=\left(\begin{array}{cc}
\beta^{2} \sigma_{x}^{2}+\sigma^{2} & \beta \sigma_{x}^{2} \\
\beta \sigma_{x}^{2} & \sigma_{x}^{2}+\sigma_{u}^{2}
\end{array}\right) .
$$

This is a simple linear regression in which the covariate is subject to measurement errors. This is a good example where the usual approach (assuming that $\boldsymbol{\Sigma}$
and $\boldsymbol{\mu}$ do not share any parameter) is not applicable. Measurement error models have been largely used in epidemiology (Kulathinal et al., 2002; de Castro et al., 2008), astrophysics (Akritas and Bershady, 1996; Kelly, 2007; Kelly et al., 2008) and analytical chemistry (Cheng and Riu, 2006) to avoid inconsistent estimators (see Fuller, 1987, for further details). Other special cases of model (1) are: multivariate heteroscedastic nonlinear errors-in-variables models, multivariate nonlinear heteroscedastic models, univariate nonlinear models, factor analysis, mixed models and so on. As can be seen, model (1) can encompass a wide class of models.

To simplify the notation, define $\boldsymbol{Y}=\operatorname{vec}\left(\boldsymbol{Y}_{1}, \boldsymbol{Y}_{2}, \ldots, \boldsymbol{Y}_{n}\right), \boldsymbol{\mu}=\operatorname{vec}\left(\boldsymbol{\mu}_{1}(\boldsymbol{\theta}), \ldots, \boldsymbol{\mu}_{n}(\boldsymbol{\theta})\right)$, $\boldsymbol{\Sigma}=\operatorname{diag}\left\{\boldsymbol{\Sigma}_{1}(\boldsymbol{\theta}), \ldots, \boldsymbol{\Sigma}_{n}(\boldsymbol{\theta})\right\}$ and $\boldsymbol{u}=\boldsymbol{Y}-\boldsymbol{\mu}$, where vec $(\cdot)$ is the vec operator, which transforms a matrix into a vector by stacking the columns of the matrix one underneath the other. Then, the log-likelihood associated with (1), apart from an unimportant constant, is

$$
\ell(\boldsymbol{\theta}) \propto-\frac{1}{2} \log |\boldsymbol{\Sigma}|-\frac{1}{2} \operatorname{tr}\left\{\boldsymbol{\Sigma}^{-1} \boldsymbol{u} \boldsymbol{u}^{\top}\right\} .
$$

We make some assumptions (Cox and Hinkley, 1974, Ch. 9) on the behavior of $\ell(\boldsymbol{\theta})$ as the sample size $n$ approaches infinity, such as the regularity of the first three derivatives of $\ell(\boldsymbol{\theta})$ with respect to $\boldsymbol{\theta}$ and the uniqueness of the MLE of $\boldsymbol{\theta}$, $\widehat{\boldsymbol{\theta}}$. We now introduce the following total log-likelihood derivatives, in which the indices $r, s$ and $t$ range from 1 to $p$. Let $U_{r}=\partial \ell(\boldsymbol{\theta}) / \partial \theta_{r}, U_{s r}=\partial^{2} \ell(\boldsymbol{\theta}) / \partial \theta_{s} \partial \theta_{r}$ and $U_{t s r}=\partial^{3} \ell(\boldsymbol{\theta}) / \partial \theta_{t} \partial \theta_{s} \partial \theta_{r}$ be the first three derivatives of $\ell(\boldsymbol{\theta})$. The standard notation for the moments of those log-likelihood derivatives is used (Lawley, 1956), namely: $\kappa_{s r}=\mathbb{E}\left(U_{s r}\right), \kappa_{s, r}=\mathbb{E}\left(U_{s} U_{r}\right), \kappa_{t s r}=\mathbb{E}\left(U_{t s r}\right)$ and so on. Furthermore, we define the derivative of $\kappa_{s r}$ with respect to $\theta_{t}$ as $\kappa_{s r}^{(t)}=\partial \kappa_{s r} / \partial \theta_{t}$. Not all $\kappa$ 's are functionally independent; e.g., $\kappa_{s, r}=-\kappa_{s r}$, which is the typical element of the information matrix $\boldsymbol{K}_{\boldsymbol{\theta}}$, assumed to be nonsingular. All $\kappa$ 's refer to a total over the sample and are, in general, of order $n$. Finally, let $\kappa^{s, r}$ denote the corresponding element of $\boldsymbol{K}_{\boldsymbol{\theta}}^{-1}$.

Define the following quantities:

$$
\begin{gathered}
\boldsymbol{a}_{r}=\frac{\partial \boldsymbol{\mu}}{\partial \theta_{r}}, \quad \boldsymbol{a}_{s r}=\frac{\partial^{2} \boldsymbol{\mu}}{\partial \theta_{s} \partial \theta_{r}}, \quad \boldsymbol{a}_{t s r}=\frac{\partial^{3} \boldsymbol{\mu}}{\partial \theta_{t} \partial \theta_{s} \partial \theta_{r}}, \quad \boldsymbol{C}_{r}=\frac{\partial \boldsymbol{\Sigma}}{\partial \theta_{r}}, \quad \boldsymbol{C}_{s r}=\frac{\partial^{2} \boldsymbol{\Sigma}}{\partial \theta_{s} \partial \theta_{r}} \\
\boldsymbol{C}_{t s r}=\frac{\partial^{3} \boldsymbol{\Sigma}}{\partial \theta_{t} \partial \theta_{s} \partial \theta_{r}}, \quad \boldsymbol{A}_{r}=\frac{\partial \boldsymbol{\Sigma}^{-1}}{\partial \theta_{r}}=-\boldsymbol{\Sigma}^{-1} \boldsymbol{C}_{r} \boldsymbol{\Sigma}^{-1} \quad \text { and } \quad \boldsymbol{A}_{s r}=\frac{\partial \boldsymbol{A}_{r}}{\partial \theta_{s}}
\end{gathered}
$$

where $r, s, t=1,2, \ldots, p$. We assume that these derivatives do exist. To compute the derivatives of $\ell(\boldsymbol{\theta})$ we make use of methods in matrix differential calculus, as describe in Magnus and Neudecker (1988). Thus, the first derivative of (3) with respect to the $r^{\text {th }}$ element of $\boldsymbol{\theta}$ is

$$
U_{r}=\frac{1}{2} \operatorname{tr}\left\{\boldsymbol{A}_{r}\left(\boldsymbol{\Sigma}-\boldsymbol{u} \boldsymbol{u}^{\top}\right)\right\}+\operatorname{tr}\left\{\boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{r} \boldsymbol{u}^{\top}\right\} .
$$

By using some simple matrix properties, the score function for $\boldsymbol{\theta}$ can be written in matrix form as

$$
\boldsymbol{U}_{\boldsymbol{\theta}} \equiv \boldsymbol{U}_{\boldsymbol{\theta}}(\boldsymbol{\theta})=\widetilde{\boldsymbol{D}}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{u}-\frac{1}{2} \widetilde{\boldsymbol{V}}^{\top} \widetilde{\boldsymbol{\Sigma}}^{-1} \operatorname{vec}\left(\boldsymbol{\Sigma}-\boldsymbol{u} \boldsymbol{u}^{\top}\right)
$$

where $\widetilde{\boldsymbol{D}}=\left(\boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{p}\right), \widetilde{\boldsymbol{V}}=\left(\operatorname{vec}\left(\boldsymbol{C}_{1}\right), \ldots, \operatorname{vec}\left(\boldsymbol{C}_{p}\right)\right), \widetilde{\boldsymbol{\Sigma}}=\boldsymbol{\Sigma} \otimes \boldsymbol{\Sigma}$ and $\otimes$ is the Kronecker product. Let

$$
\widetilde{\boldsymbol{F}}=\binom{\widetilde{\boldsymbol{D}}}{\widetilde{\boldsymbol{V}}}, \quad \widetilde{\boldsymbol{H}}=\left(\begin{array}{cc}
\boldsymbol{\Sigma} & \mathbf{0} \\
\mathbf{0} & 2 \widetilde{\boldsymbol{\Sigma}}
\end{array}\right)^{-1} \quad \text { and } \quad \widetilde{\boldsymbol{u}}=\binom{\boldsymbol{u}}{-\operatorname{vec}\left(\boldsymbol{\Sigma}-\boldsymbol{u} \boldsymbol{u}^{\top}\right)}
$$

Then, note that the score function can be written as

$$
\boldsymbol{U}_{\boldsymbol{\theta}}=\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{u}}
$$

The second and third derivatives are given, respectively, by

$$
\begin{aligned}
U_{s r}= & \frac{1}{2} \operatorname{tr}\left\{\left(\boldsymbol{A}_{s} \boldsymbol{\Sigma} \boldsymbol{A}_{r}+\boldsymbol{A}_{r} \boldsymbol{\Sigma} \boldsymbol{A}_{s}-\boldsymbol{\Sigma}^{-1} \boldsymbol{C}_{s r} \boldsymbol{\Sigma}^{-1}\right)\left(\boldsymbol{\Sigma}-\boldsymbol{u} \boldsymbol{u}^{\top}\right)\right\} \\
& +\frac{1}{2} \operatorname{tr}\left\{\boldsymbol{A}_{r}\left(\boldsymbol{C}_{s}+\boldsymbol{a}_{s} \boldsymbol{u}^{\top}+\boldsymbol{u} \boldsymbol{a}_{s}^{\top}\right)\right\}+\operatorname{tr}\left\{\left(\boldsymbol{A}_{s} \boldsymbol{a}_{r}+\boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s r}\right) \boldsymbol{u}^{\top}-\boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{r} \boldsymbol{a}_{s}^{\top}\right\}
\end{aligned}
$$

and

$$
U_{t s r}=U_{t s r}^{(1)}+U_{t s r}^{(2)}+U_{t s r}^{(3)}+U_{t s r}^{(4)}
$$

where

$$
\begin{aligned}
& U_{t s r}^{(1)}=-\frac{1}{2} \operatorname{tr}\left\{\left(\boldsymbol{\Sigma}^{-1} \boldsymbol{C}_{t s r} \boldsymbol{\Sigma}^{-1}+\boldsymbol{\Sigma}^{-1} \boldsymbol{C}_{r s} \boldsymbol{A}_{t}+\boldsymbol{A}_{t} \boldsymbol{C}_{s r} \boldsymbol{\Sigma}^{-1}\right)\left(\boldsymbol{\Sigma}-\boldsymbol{u} \boldsymbol{u}^{\top}\right)\right. \\
&\left.+\boldsymbol{\Sigma}^{-1} \boldsymbol{C}_{s r} \boldsymbol{\Sigma}^{-1} \boldsymbol{C}_{t}+\boldsymbol{\Sigma}^{-1} \boldsymbol{C}_{s r} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{a}_{t} \boldsymbol{u}^{\top}+\boldsymbol{u} \boldsymbol{a}_{t}^{\top}\right)\right\} \\
& U_{t s r}^{(2)}= \frac{1}{2} \operatorname{tr}\left\{\left(\boldsymbol{A}_{s t} \boldsymbol{\Sigma} \boldsymbol{A}_{r}+\boldsymbol{A}_{s}\left(\boldsymbol{C}_{t} \boldsymbol{A}_{r}+\boldsymbol{\Sigma} \boldsymbol{A}_{r t}\right)\right)\left(\boldsymbol{\Sigma}-\boldsymbol{u} \boldsymbol{u}^{\top}\right)\right. \\
&+\left(\boldsymbol{A}_{r t} \boldsymbol{\Sigma} \boldsymbol{A}_{s}+\boldsymbol{A}_{r}\left(\boldsymbol{C}_{t} \boldsymbol{A}_{s}+\boldsymbol{\Sigma} \boldsymbol{A}_{s t}\right)\right)\left(\boldsymbol{\Sigma}-\boldsymbol{u} \boldsymbol{u}^{\top}\right) \\
&\left.+\left(\boldsymbol{A}_{s} \boldsymbol{\Sigma} \boldsymbol{A}_{r}+\boldsymbol{A}_{r} \boldsymbol{\Sigma} \boldsymbol{A}_{s}\right)\left(\boldsymbol{C}_{t}+\boldsymbol{a}_{t} \boldsymbol{u}^{\top}+\boldsymbol{u} \boldsymbol{a}_{t}^{\top}\right)\right\} \\
& U_{t s r}^{(3)}=\frac{1}{2} \operatorname{tr}\left\{\boldsymbol{A}_{r t}\left(\boldsymbol{C}_{s}+\boldsymbol{a}_{s} \boldsymbol{u}^{\top}+\boldsymbol{u} \boldsymbol{a}_{s}^{\top}\right)+\boldsymbol{A}_{r}\left(\boldsymbol{C}_{t s}+\boldsymbol{a}_{t s} \boldsymbol{u}^{\top}-\boldsymbol{a}_{s} \boldsymbol{a}_{t}^{\top}+\boldsymbol{a}_{t} \boldsymbol{a}_{s}^{\top}+\boldsymbol{u} \boldsymbol{a}_{t s}^{\top}\right)\right\}
\end{aligned}
$$

and

$$
\begin{aligned}
U_{t s r}^{(4)}= & \operatorname{tr}\left\{\left(\boldsymbol{A}_{s t} \boldsymbol{a}_{r}+\boldsymbol{A}_{s} \boldsymbol{a}_{r t}+\boldsymbol{A}_{t} \boldsymbol{a}_{s r}+\boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s r t}\right) \boldsymbol{u}^{\top}-\left(\boldsymbol{A}_{s} \boldsymbol{a}_{r}+\boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s r}\right) \boldsymbol{a}_{t}^{\top}\right\} \\
& -\operatorname{tr}\left\{\boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{r} \boldsymbol{a}_{t s}^{\top}+\boldsymbol{A}_{t} \boldsymbol{a}_{r} \boldsymbol{a}_{s}^{\top}+\boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s} \boldsymbol{a}_{t r}^{\top}\right\}
\end{aligned}
$$

Note that $\mathbb{E}(\boldsymbol{u})=\mathbf{0}$ and $\mathbb{E}\left(\boldsymbol{u} \boldsymbol{u}^{\top}\right)=\boldsymbol{\Sigma}$. Knowing these properties, the expectation of $U_{r}, U_{s r}$ and $U_{t s r}$ are easily obtained. The quantities $\kappa_{s r}, \kappa_{t s r}$ and $\kappa_{t s}^{(r)}(r, s, t= 1,2, \ldots, p$ ) are given, respectively, by

$$
\begin{gathered}
\kappa_{s r}=\frac{1}{2} \operatorname{tr}\left\{\boldsymbol{A}_{r} \boldsymbol{C}_{s}\right\}-\boldsymbol{a}_{s}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{r}, \\
\kappa_{t s r}=\operatorname{tr}\left\{\left(\boldsymbol{A}_{r} \boldsymbol{\Sigma} \boldsymbol{A}_{s}+\boldsymbol{A}_{s} \boldsymbol{\Sigma} \boldsymbol{A}_{r}\right) \boldsymbol{C}_{t}\right\}+\frac{1}{2} \operatorname{tr}\left\{\boldsymbol{A}_{s} \boldsymbol{C}_{t r}+\boldsymbol{A}_{r} \boldsymbol{C}_{t s}+\boldsymbol{A}_{t} \boldsymbol{C}_{s r}\right\} \\
-\left(\boldsymbol{a}_{t}^{\top} \boldsymbol{A}_{s} \boldsymbol{a}_{r}+\boldsymbol{a}_{s}^{\top} \boldsymbol{A}_{t} \boldsymbol{a}_{r}+\boldsymbol{a}_{s}^{\top} \boldsymbol{A}_{r} \boldsymbol{a}_{t}+\boldsymbol{a}_{t}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s r}+\boldsymbol{a}_{t s}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{r}+\boldsymbol{a}_{s}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{t r}\right)
\end{gathered}
$$

and

$$
\begin{aligned}
\kappa_{t s}^{(r)}= & \frac{1}{2} \operatorname{tr}\left\{\left(\boldsymbol{A}_{r} \boldsymbol{\Sigma} \boldsymbol{A}_{s}+\boldsymbol{A}_{s} \boldsymbol{\Sigma} \boldsymbol{A}_{r}\right) \boldsymbol{C}_{t}+\boldsymbol{A}_{t} \boldsymbol{C}_{r s}+\boldsymbol{A}_{s} \boldsymbol{C}_{r t}\right\} \\
& -\left(\boldsymbol{a}_{r t}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s}+\boldsymbol{a}_{t}^{\top} \boldsymbol{A}_{r} \boldsymbol{a}_{s}+\boldsymbol{a}_{t}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{r s}\right)
\end{aligned}
$$

Again, by using some matrix properties on expression (5), we can written the expected Fisher information as

$$
\boldsymbol{K}_{\boldsymbol{\theta}} \equiv \boldsymbol{K}_{\boldsymbol{\theta}}(\boldsymbol{\theta})=\widetilde{\boldsymbol{D}}^{\top} \boldsymbol{\Sigma}^{-1} \widetilde{\boldsymbol{D}}+\frac{1}{2} \widetilde{\boldsymbol{V}}^{\top} \widetilde{\boldsymbol{\Sigma}}^{-1} \widetilde{\boldsymbol{V}}
$$

Using $\widetilde{\boldsymbol{F}}$ and $\widetilde{\boldsymbol{H}}$ given in (4), we can write $\boldsymbol{K}_{\boldsymbol{\theta}}$ in the form

$$
\boldsymbol{K}_{\boldsymbol{\theta}}=\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{F}} .
$$

The MLE $\widehat{\boldsymbol{\theta}}$ satisfy the equation $\boldsymbol{U}_{\boldsymbol{\theta}}=\mathbf{0}$. After some matrix manipulations, the Fisher scoring method can be used to estimate $\boldsymbol{\theta}$ by iteratively solving the equation

$$
\left(\widetilde{\boldsymbol{F}}^{(m)^{\top}} \widetilde{\boldsymbol{H}}^{(m)} \widetilde{\boldsymbol{F}}^{(m)}\right) \boldsymbol{\theta}^{(m+1)}=\widetilde{\boldsymbol{F}}^{(m)^{\top}} \widetilde{\boldsymbol{H}}^{(m)} \widetilde{\boldsymbol{u}}^{*(m)}, \quad m=0,1,2, \ldots,
$$

where $\widetilde{\boldsymbol{u}}^{*(m)}=\widetilde{\boldsymbol{F}}^{(m)} \boldsymbol{\theta}^{(m)}+\widetilde{\boldsymbol{u}}^{(m)}$. Each loop, through the iterative scheme (9), consists of an iterative re-weighted least squares algorithm to optimize the log-likelihood (3). Using equation (9) and any software (MAPLE, MATLAB, Ox, R, SAS) with a weighted linear regression routine one can compute the MLE $\widehat{\boldsymbol{\theta}}$ iteratively. It is also noteworthy that the MLE in even much complex models, such as multivariate heteroscedastic nonlinear errors-in-variables models, may be attained via iterative formula (9).

It is well known that MLEs are consistent, asymptotically efficient and asymptotically normal distributed. We can write $\widehat{\boldsymbol{\theta}} \stackrel{a}{\sim} \mathcal{N}_{p}\left(\boldsymbol{\theta}, \boldsymbol{K}_{\boldsymbol{\theta}}^{-1}\right)$, when $n$ is large, $\stackrel{a}{\sim}$ denoting approximately distributed. Hence, hypotheses testing can be carried out using this asymptotic distribution.

## 3 Biases of estimates of $\boldsymbol{\theta}$

In this section we compute the biases of ML estimates of $\boldsymbol{\theta}$ for models defined by (1). Let $B\left(\widehat{\theta}_{a}\right)$ be the $n^{-1}$ bias of $\widehat{\theta}_{a}, a=1,2, \ldots, p$. It follows from the general expression for the multiparameter $n^{-1}$ biases of MLEs given by Cox and Snell (1968) that

$$
B\left(\widehat{\theta}_{a}\right)=\sum_{t, s, r}^{\prime} \kappa^{a, t} \kappa^{s, r}\left\{\frac{1}{2} \kappa_{t s r}-\kappa_{t s, r}\right\}
$$

where $\sum^{\prime}$ denotes the summation over all combinations of the parameters $\theta_{1}, \ldots, \theta_{p}$. Following Cordeiro and Klein (1994), we write the above equation in matrix notation to obtain $n^{-1}$ bias vector $\boldsymbol{B}(\widehat{\boldsymbol{\theta}})$ of $\widehat{\boldsymbol{\theta}}$ in the form

$$
\boldsymbol{B}(\widehat{\boldsymbol{\theta}})=\boldsymbol{K}_{\boldsymbol{\theta}}^{-1} \boldsymbol{W} \operatorname{vec}\left(\boldsymbol{K}_{\boldsymbol{\theta}}^{-1}\right)
$$

where $\boldsymbol{W}=\left(\boldsymbol{W}^{(1)}, \ldots, \boldsymbol{W}^{(p)}\right)$ is a $p \times p^{2}$ partitioned matrix, each $\boldsymbol{W}^{(r)}$ referring to the $r^{\text {th }}$ component of $\boldsymbol{\theta}$ being a $p \times p$ matrix with typical $(t, s)$ th element given by $w_{t s}^{(r)}=\frac{1}{2} \kappa_{t s r}+\kappa_{t s, r}=\kappa_{t s}^{(r)}-\frac{1}{2} \kappa_{t s r}$. Notice that from (6) and (7) we have that

$$
\begin{aligned}
w_{t s}^{(r)}= & \frac{1}{4} \operatorname{tr}\left\{\boldsymbol{A}_{t} \boldsymbol{C}_{s r}+\boldsymbol{A}_{s} \boldsymbol{C}_{t r}-\boldsymbol{A}_{r} \boldsymbol{C}_{t s}\right\} \\
& -\frac{1}{2}\left(\boldsymbol{a}_{t}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s r}+\boldsymbol{a}_{s}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{t r}-\boldsymbol{a}_{r}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{t s}\right) \\
& +\frac{1}{2}\left(\boldsymbol{a}_{s}^{\top} \boldsymbol{A}_{t} \boldsymbol{a}_{r}+\boldsymbol{a}_{t}^{\top} \boldsymbol{A}_{s} \boldsymbol{a}_{r}-\boldsymbol{a}_{t}^{\top} \boldsymbol{A}_{r} \boldsymbol{a}_{s}\right)
\end{aligned}
$$

Since $\boldsymbol{K}_{\boldsymbol{\theta}}$ is a symmetric matrix and we are interested in the multiplication result of $\boldsymbol{W} \operatorname{vec}\left(\boldsymbol{K}_{\boldsymbol{\theta}}^{-1}\right)$, many terms of (10) cancel. Indeed, note that the $t^{\text {th }}$ element of $\boldsymbol{W} \operatorname{vec}\left(\boldsymbol{K}_{\boldsymbol{\theta}}^{-1}\right)$ is given by $w_{t 1}^{(1)} \kappa^{1,1}+\left(w_{t 2}^{(1)}+w_{t 1}^{(2)}\right) \kappa^{1,2}+\cdots+\left(w_{t r}^{(s)}+w_{t s}^{(r)}\right) \kappa^{s, r}+\cdots+ \left(w_{t p}^{(p-1)}+w_{t(p-1)}^{(p)}\right) \kappa^{p-1, p}+w_{t p}^{(p)} \kappa^{p, p}$ and $w_{t r}^{(s)}+w_{t s}^{(r)}=\frac{1}{2} \operatorname{tr}\left(\boldsymbol{A}_{t} \boldsymbol{C}_{s r}\right)-\boldsymbol{a}_{t}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s r}+\boldsymbol{a}_{s}^{\top} \boldsymbol{A}_{t} \boldsymbol{a}_{r}$. Therefore, we can replace the element $w_{t s}^{(r)}$ by $\frac{1}{4} \operatorname{tr}\left(\boldsymbol{A}_{t} \boldsymbol{C}_{s r}\right)-\frac{1}{2} \boldsymbol{a}_{t}^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{a}_{s r}+\frac{1}{2} \boldsymbol{a}_{s}^{\top} \boldsymbol{A}_{t} \boldsymbol{a}_{r}$ and $\boldsymbol{W}^{(r)}$ may be written in an equivalent way as $\boldsymbol{W}^{(r)}=\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \boldsymbol{\Phi}_{r}, r=1, \ldots, p$, where $\boldsymbol{\Phi}_{r}=-\frac{1}{2}\left(\boldsymbol{G}_{r}+\boldsymbol{J}_{r}\right)$ with

$$
\boldsymbol{G}_{r}=\left[\begin{array}{ccc}
\boldsymbol{a}_{1 r} & \cdots & \boldsymbol{a}_{p r} \\
\operatorname{vec}\left(\boldsymbol{C}_{1 r}\right) & \cdots & \operatorname{vec}\left(\boldsymbol{C}_{p r}\right)
\end{array}\right] \quad \text { and } \quad \boldsymbol{J}_{r}=\left[\begin{array}{c}
\mathbf{0} \\
2\left(\boldsymbol{I}_{n q} \otimes \boldsymbol{a}_{r}\right) \widetilde{\boldsymbol{D}}
\end{array}\right]
$$

where $\boldsymbol{I}_{m}$ denotes an $m \times m$ identity matrix. That is, the matrix $\boldsymbol{W}$ can be written as $\boldsymbol{W}=\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}}\left(\boldsymbol{\Phi}_{1}, \ldots, \boldsymbol{\Phi}_{p}\right)$. Then, we arrive at the following theorem.

Theorem. The $n^{-1}$ bias vector $\boldsymbol{B}(\widehat{\boldsymbol{\theta}})$ of $\widehat{\boldsymbol{\theta}}$ is given by

$$
\boldsymbol{B}(\widehat{\boldsymbol{\theta}})=\left(\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{F}}\right)^{-1} \widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{\xi}}
$$

where $\widetilde{\boldsymbol{\xi}}=\left(\boldsymbol{\Phi}_{1}, \ldots, \boldsymbol{\Phi}_{p}\right) \operatorname{vec}\left(\left(\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{F}}\right)^{-1}\right)$.
In order to interpret formulae (11) it is helpful to exploit the relationship between the $n^{-1}$ bias of $\widehat{\boldsymbol{\theta}}$ and a linear regression. The bias vector $\boldsymbol{B}(\widehat{\boldsymbol{\theta}})$ is simply the set coefficients from the ordinary weighted lest-squares regression of $\widetilde{\boldsymbol{\xi}}$ on the columns of $\widetilde{\boldsymbol{F}}$, using weights in $\widetilde{\boldsymbol{H}}$. As expression (11) makes clear, for any particular model of the class of models presented in Section 2, it is always possible to express the bias of $\widehat{\boldsymbol{\theta}}$ as the solution of an ordinary weighted lest-squares regression. Equation (11) is easily handled algebraically for any type of nonlinear model, since it only involves simple operations on matrices and vectors. This equation, in conjunction with a computer algebra system such as MAPLE (Abell and Braselton, 1994), will yield $\boldsymbol{B}(\widehat{\boldsymbol{\theta}})$ algebraically with minimal effort. Also, we can compute the bias $\boldsymbol{B}(\widehat{\boldsymbol{\theta}})$ numerically via software with numerical linear algebra facilities such as Ox (Doornik, 2006) and R (R Development Core Team, 2006). [Note that we have described a procedure to attain a corrected estimator in a general formulation that covers a wide class of models. In the next section we shall present some special cases to shed light on the applicability of our general formulation.]

Therefore, we are able to compute the $n^{-1}$ biases of the MLEs for the general model (1) using formula (11). On the right-hand side of expression (11), which is
of order $n^{-1}$, consistent estimates of the parameter $\boldsymbol{\theta}$ can be inserted to define the corrected MLE $\widetilde{\boldsymbol{\theta}}=\widehat{\boldsymbol{\theta}}-\widehat{\boldsymbol{B}}(\widehat{\boldsymbol{\theta}})$, where $\widehat{\boldsymbol{B}}(\cdot)$ denotes the value of $\boldsymbol{B}(\cdot)$ at $\widehat{\boldsymbol{\theta}}$. The bias-corrected estimate $\widetilde{\boldsymbol{\theta}}$ is expected to have better sampling properties than the uncorrected estimator, $\widehat{\boldsymbol{\theta}}$. In fact, we present some simulations in Section 5 that indicate that $\widetilde{\boldsymbol{\theta}}$ has smaller bias than its corresponding MLE, thus suggesting that the bias corrections above have the effect of shrinking the modified estimates toward to the true parameter values.

Following Cordeiro (2008), it is worth emphasizing that there are other methods to bias-correcting MLEs. In regular parametric problems, Firth (1993) developed the so-called "preventive" method, which also allows for the removal of the secondorder biases. His method consists of modifying the original score function to remove the first-order term from the asymptotic bias of these estimates. In exponential families with canonical parameterization his correction scheme consists in penalizing the likelihood by the Jeffreys invariant prior. This is a preventive approach to bias adjustment which has its merits, but the connections between our results and his work are not pursued in this paper since they will be developed in future research. Additionally, we should also stress that it is possible to avoid cumbersome and tedious algebra on cumulant calculations by using Efron's bootstrap (Efron and Tibshirani, 1993). We use the analytical approach here since it leads to a closed-form solution and we do not need to run extensive numerical resamples. Moreover, the application of the analytical bias seems to generally be the most feasible procedure to use and it continues to receive attention in the literature.

## 4 Special models

It is useful to consider some examples to illustrate the applicability of the results in the previous section and clarify the notation used. Other important special models could also be easily handled since formula (11) only requires simple operations on matrices and vectors.

First, consider a univariate nonlinear model ( $q=1$ ) in which $\boldsymbol{\Sigma}=\sigma^{2} \boldsymbol{I}_{n}$. Note that this model is a particular case of model (1) with $\boldsymbol{\theta}=\left(\boldsymbol{\beta}^{\top}, \sigma^{2}\right)^{\top}$ and $\boldsymbol{\mu}= \left(\mu_{1}(\boldsymbol{\beta}), \ldots, \mu_{n}(\boldsymbol{\beta})\right)^{\top}$, where the components of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are unrelated and vary independently. Let $p-1$ be the dimension of $\boldsymbol{\beta}$. Here, $\widetilde{\boldsymbol{D}}=\left(\boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{p-1}, \mathbf{0}\right)$ and $\widetilde{\boldsymbol{V}}=\left(\mathbf{0}, \operatorname{vec}\left(\boldsymbol{C}_{p}\right)\right)$. Also, $\widetilde{\boldsymbol{F}}=\operatorname{diag}\left\{\widetilde{\boldsymbol{D}}^{(1)}, \widetilde{\boldsymbol{V}}^{(2)}\right\}$, where $\widetilde{\boldsymbol{D}}^{(1)}=\left(\boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{p-1}\right)$ and $\tilde{\boldsymbol{V}}^{(2)}=\operatorname{vec}\left(\boldsymbol{C}_{p}\right)$. Then, from (8), the expected Fisher information for $\boldsymbol{\theta}$ can be written as $\boldsymbol{K}_{\boldsymbol{\theta}}=\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{F}}=\operatorname{diag}\left\{\boldsymbol{K}_{\boldsymbol{\beta}}, K_{\sigma^{2}}\right\}$, where $\boldsymbol{K}_{\boldsymbol{\beta}}=\widetilde{\boldsymbol{D}}^{(1) \top} \widetilde{\boldsymbol{D}}^{(1)} / \sigma^{2}$ is Fisher's information for $\boldsymbol{\beta}$ and $K_{\sigma^{2}}=n / 2 \sigma^{4}$ is the information relative to $\sigma^{2}$. Since $\boldsymbol{K}_{\boldsymbol{\theta}}$ is block-diagonal, $\boldsymbol{\beta}$ and $\sigma$ are globally orthogonal (Cox and Reid, 1987). From (11), note that

$$
\left(\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{F}}\right)^{-1} \widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}}=\left[\begin{array}{cc}
\left(\widetilde{\boldsymbol{D}}^{(1)^{\top}} \widetilde{\boldsymbol{D}}^{(1)}\right)^{-1} \widetilde{\boldsymbol{D}}^{(1) \top} & \mathbf{0} \\
\mathbf{0} & \frac{1}{n} \widetilde{\boldsymbol{V}}^{(2) \top}\left(\boldsymbol{I}_{n} \otimes \boldsymbol{I}_{n}\right)
\end{array}\right] .
$$

Also,

$$
\widetilde{\boldsymbol{\xi}}=\binom{\widetilde{\boldsymbol{\xi}}_{1}}{\widetilde{\boldsymbol{\xi}}_{2}}=\left[\begin{array}{l}
-\frac{\sigma^{2}}{2} \ddot{\boldsymbol{G}} \operatorname{vec}\left\{\left(\widetilde{\boldsymbol{D}}^{(1)^{\top}} \widetilde{\boldsymbol{D}}^{(1)}\right)^{-1}\right\} \\
-\sum_{k=1}^{p-1}\left(\boldsymbol{I}_{n} \otimes \boldsymbol{a}_{k}\right) \widetilde{\boldsymbol{D}}^{(1)} \boldsymbol{K}_{\boldsymbol{\beta} k}^{-1}
\end{array}\right],
$$

where $\ddot{\boldsymbol{G}}=\left(\boldsymbol{a}_{\boldsymbol{\beta} 1}, \ldots, \boldsymbol{a}_{\boldsymbol{\beta}(p-1)}\right)$ with $\boldsymbol{a}_{\boldsymbol{\beta} k}=\left(\boldsymbol{a}_{1 k}, \ldots, \boldsymbol{a}_{(p-1) k}\right)$ and $\boldsymbol{K}_{\boldsymbol{\beta} k}^{-1}$ is the $k^{t h}$ column of $\boldsymbol{K}_{\boldsymbol{\beta}}^{-1}$. Then,

$$
\boldsymbol{B}(\widehat{\boldsymbol{\theta}})=\binom{\boldsymbol{B}(\widehat{\boldsymbol{\beta}})}{B\left(\widehat{\sigma}^{2}\right)}=\left[\begin{array}{c}
\left(\widetilde{\boldsymbol{D}}^{(1)^{\top}} \widetilde{\boldsymbol{D}}^{(1)}\right)^{-1} \widetilde{\boldsymbol{D}}^{(1) \top} \widetilde{\boldsymbol{\xi}}_{1} \\
\frac{1}{n} \widetilde{\boldsymbol{V}}^{(2)^{\top}}\left(\boldsymbol{I}_{n} \otimes \boldsymbol{I}_{n}\right) \widetilde{\boldsymbol{\xi}}_{2}
\end{array}\right]
$$

Note that $\boldsymbol{B}(\widehat{\boldsymbol{\beta}})=\left(\widetilde{\boldsymbol{D}}^{(1)^{\top}} \widetilde{\boldsymbol{D}}^{(1)}\right)^{-1} \widetilde{\boldsymbol{D}}^{(1) \top} \widetilde{\boldsymbol{\xi}}_{1}$ agrees with the result due to Cook et al. (1986, Equation (3)). Additionally, we obtain the following simple form originally first given be Beale (1960): $B\left(\widehat{\sigma}^{2}\right)=-(p-1) \sigma^{2} / n$; note that

$$
\begin{aligned}
\widetilde{\boldsymbol{V}}^{(2) \top}\left(\boldsymbol{I}_{n} \otimes \boldsymbol{I}_{n}\right) & \sum_{k=1}^{p-1}\left(\boldsymbol{I}_{n} \otimes \boldsymbol{a}_{k}\right) \widetilde{\boldsymbol{D}}^{(1)} \boldsymbol{K}_{\boldsymbol{\beta} k}^{-1}=\sum_{k=1}^{p-1} \operatorname{vec}\left(\boldsymbol{C}_{p}\right)^{\top}\left(\boldsymbol{I}_{n} \otimes \boldsymbol{a}_{k}\right) \widetilde{\boldsymbol{D}}^{(1)} \boldsymbol{K}_{\boldsymbol{\beta} k}^{-1} \\
= & \sum_{k=1}^{p-1} \operatorname{tr}\left\{\boldsymbol{a}_{k} \boldsymbol{K}_{\boldsymbol{\beta} k}^{-1} \widetilde{\boldsymbol{D}}^{(1) \top}\right\}=\operatorname{tr}\left\{\widetilde{\boldsymbol{D}}^{(1)} \boldsymbol{K}_{\boldsymbol{\beta}}^{-1} \widetilde{\boldsymbol{D}}^{(1) \top}\right\}=(p-1) \sigma^{2}
\end{aligned}
$$

As a second application, consider the multivariate nonlinear heteroscedastic regression model studied by Vasconcellos and Cordeiro (1997). Note that this model is a particular case of model (1), with $\boldsymbol{\theta}=\left(\boldsymbol{\beta}^{\top}, \boldsymbol{\sigma}^{\top}\right)^{\top}, \boldsymbol{\mu}=\operatorname{vec}\left(\boldsymbol{\mu}_{1}(\boldsymbol{\beta}), \ldots, \boldsymbol{\mu}_{n}(\boldsymbol{\beta})\right)$ and $\boldsymbol{\Sigma}=\operatorname{diag}\left\{\boldsymbol{\Sigma}_{1}(\boldsymbol{\sigma}), \ldots, \boldsymbol{\Sigma}_{n}(\boldsymbol{\sigma})\right\}$. Therefore, the components of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are unrelated and vary independently. Let $p_{1}$ and $p_{2}=p-p_{1}$ be the dimensions of $\boldsymbol{\beta}$ and $\boldsymbol{\sigma}$, respectively. Here, $\widetilde{\boldsymbol{D}}=\left(\boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{p_{1}}, \mathbf{0}\right)$ and $\widetilde{\boldsymbol{V}}=\left(\mathbf{0}, \operatorname{vec}\left(\boldsymbol{C}_{p_{1}+1}\right), \ldots, \operatorname{vec}\left(\boldsymbol{C}_{p}\right)\right)$. Let $\widetilde{\boldsymbol{D}}^{(1)}=\left(\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \ldots, \boldsymbol{a}_{p_{1}}\right)$ and $\tilde{\boldsymbol{V}}^{(2)}=\left(\operatorname{vec}\left(\boldsymbol{C}_{p_{1}+1}\right), \operatorname{vec}\left(\boldsymbol{C}_{p_{1}+2}\right) \ldots, \operatorname{vec}\left(\boldsymbol{C}_{p}\right)\right)$, then $\widetilde{\boldsymbol{F}}=\operatorname{diag}\left\{\widetilde{\boldsymbol{D}}^{(1)}, \widetilde{\boldsymbol{V}}^{(2)}\right\}$. From (8), the expected Fisher information for $\boldsymbol{\theta}$ can be written as $\boldsymbol{K}_{\boldsymbol{\theta}}=\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{F}}=\operatorname{diag}\left\{\boldsymbol{K}_{\boldsymbol{\beta}}, \boldsymbol{K}_{\boldsymbol{\sigma}}\right\}$, where $\boldsymbol{K}_{\boldsymbol{\beta}}=\widetilde{\boldsymbol{D}}^{(1)^{\top}} \boldsymbol{\Sigma}^{-1} \widetilde{\boldsymbol{D}}^{(1)}$ is Fisher's information for $\boldsymbol{\beta}$ and $\boldsymbol{K}_{\boldsymbol{\sigma}}=\frac{1}{2} \tilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \widetilde{\boldsymbol{V}}^{(2)}$ is the information relative to $\boldsymbol{\sigma}$. Since $\boldsymbol{K}_{\boldsymbol{\theta}}$ is block-diagonal, $\boldsymbol{\beta}$ and $\boldsymbol{\sigma}$ are globally orthogonal. From (11), it follows that

$$
\left(\widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}} \widetilde{\boldsymbol{F}}\right)^{-1} \widetilde{\boldsymbol{F}}^{\top} \widetilde{\boldsymbol{H}}=\left[\begin{array}{cc}
\left(\widetilde{\boldsymbol{D}}^{(1) \top} \boldsymbol{\Sigma}^{-1} \widetilde{\boldsymbol{D}}^{(1)}\right)^{-1} \widetilde{\boldsymbol{D}}^{(1) \top} \boldsymbol{\Sigma}^{-1} & \mathbf{0} \\
\mathbf{0} & \left(\widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \widetilde{\boldsymbol{V}}^{(2)}\right)^{-1} \widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\Sigma}^{-1}
\end{array}\right]
$$

Also,

$$
\widetilde{\boldsymbol{\xi}}=\binom{\widetilde{\boldsymbol{\xi}}_{1}}{\widetilde{\boldsymbol{\xi}}_{2}}=\left[\begin{array}{c}
-\frac{1}{2} \ddot{\boldsymbol{G}} \operatorname{vec}\left\{\left(\widetilde{\boldsymbol{D}}^{(1) \top} \boldsymbol{\Sigma}^{-1} \widetilde{\boldsymbol{D}}^{(1)}\right)^{-1}\right\} \\
-\left(\ddot{\boldsymbol{W}} \operatorname{vec}\left\{\left(\widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \widetilde{\boldsymbol{V}}^{(2)}\right)^{-1}\right\}+\sum_{k=1}^{p_{1}}\left(\boldsymbol{I}_{n q} \otimes \boldsymbol{a}_{k}\right) \widetilde{\boldsymbol{D}}^{(1)} \boldsymbol{K}_{\boldsymbol{\beta} k}^{-1}\right)
\end{array}\right],
$$

where $\ddot{\boldsymbol{G}}=\left(\boldsymbol{a}_{\boldsymbol{\beta} 1}, \ldots, \boldsymbol{a}_{\boldsymbol{\beta} p_{1}}\right)$ with $\boldsymbol{a}_{\boldsymbol{\beta} k}=\left(\boldsymbol{a}_{1 k}, \ldots, \boldsymbol{a}_{p_{1} k}\right)$ and $\ddot{\boldsymbol{W}}=\left(\boldsymbol{v}_{\boldsymbol{\sigma}\left(p_{1}+1\right)}, \ldots, \boldsymbol{v}_{\boldsymbol{\sigma} p}\right)$ with $\boldsymbol{v}_{\boldsymbol{\sigma} k}=\left(\operatorname{vec}\left(\boldsymbol{C}_{\left(p_{1}+1\right) k}\right), \ldots, \operatorname{vec}\left(\boldsymbol{C}_{p k}\right)\right)$ and $\boldsymbol{K}_{\boldsymbol{\beta} k}^{-1}$ is the $k^{t h}$ column of $\boldsymbol{K}_{\boldsymbol{\beta}}^{-1}$. Therefore,

$$
\boldsymbol{B}(\widehat{\boldsymbol{\theta}})=\binom{\boldsymbol{B}(\widehat{\boldsymbol{\beta}})}{\boldsymbol{B}(\widehat{\boldsymbol{\sigma}})}=\left[\begin{array}{l}
\left(\widetilde{\boldsymbol{D}}^{(1)^{\top}} \boldsymbol{\Sigma}^{-1} \widetilde{\boldsymbol{D}}^{(1)}\right)^{-1} \widetilde{\boldsymbol{D}}^{(1) \top} \boldsymbol{\Sigma}^{-1} \widetilde{\boldsymbol{\xi}}_{1} \\
\left(\widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \widetilde{\boldsymbol{V}}^{(2)}\right)^{-1} \widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \widetilde{\boldsymbol{\xi}}_{2}
\end{array}\right]
$$

Note that $\boldsymbol{B}(\widehat{\boldsymbol{\beta}})=\left(\widetilde{\boldsymbol{D}}^{(1) \top} \boldsymbol{\Sigma}^{-1} \widetilde{\boldsymbol{D}}^{(1)}\right)^{-1} \widetilde{\boldsymbol{D}}^{(1) \top} \boldsymbol{\Sigma}^{-1} \widetilde{\boldsymbol{\xi}}_{1}$ agrees with the result due to Vasconcellos and Cordeiro (1997, Equation (3.2)). Additionally, note that $\boldsymbol{B}(\widehat{\boldsymbol{\sigma}})=$
$\left(\widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \widetilde{\boldsymbol{V}}^{(2)}\right)^{-1} \widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \widetilde{\boldsymbol{\xi}}_{2}$ also reduces to Vasconcellos and Cordeiro's (1997) Eq. (3.8), since

$$
\widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \sum_{k=1}^{p_{1}}\left(\boldsymbol{I}_{n q} \otimes \boldsymbol{a}_{k}\right) \widetilde{\boldsymbol{D}}^{(1)} \boldsymbol{K}_{\boldsymbol{\beta} k}^{-1}=\widetilde{\boldsymbol{V}}^{(2) \top} \widetilde{\boldsymbol{\Sigma}}^{-1} \operatorname{vec}\left(\boldsymbol{\Delta}_{*}\right)
$$

where $\boldsymbol{\Delta}_{*}$ is as defined by Vasconcellos and Cordeiro (1997, p. 148).
Next, unlike the two models discussed previously, we consider a model where the elements of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are related and do not vary independently. Consider the nonlinear heteroscedastic errors-in-variables model

$$
Y_{i}=\alpha+\beta x_{i}+\exp \left(\gamma z_{i}\right)+e_{i} \quad \text { and } \quad X_{i}=x_{i}+u_{i}
$$

where $x_{i} \sim \mathcal{N}\left(\mu_{x}, \sigma_{x}^{2}\right)$ and $u_{i} \sim \mathcal{N}\left(0, \sigma_{u}^{2}\right)$ are the measurement errors with $\sigma_{u}^{2}$ known and $e_{i} \sim \mathcal{N}\left(0, \sigma^{2} \exp \left\{\eta z_{i}\right\}\right)$. The covariate $z_{i}$ is known. In this example, the vector of parameters is $\boldsymbol{\theta}=\left(\alpha, \beta, \gamma, \mu_{x}, \sigma_{x}^{2}, \sigma^{2}, \eta\right)^{\top}$ and the mean and variance functions for the $i^{\text {th }}$ observation ( $Y_{i}, X_{i}$ ) are given by

$$
\boldsymbol{\mu}_{i}=\binom{\alpha+\beta \mu_{x}+\exp \left(\gamma z_{i}\right)}{\mu_{x}} \quad \text { and } \quad \boldsymbol{\Sigma}_{i}=\left(\begin{array}{cc}
\beta^{2} \sigma_{x}^{2}+\sigma^{2} \exp \left(\eta z_{i}\right) & \beta \sigma_{x}^{2} \\
\beta \sigma_{x}^{2} & \sigma_{x}^{2}+\sigma_{u}^{2}
\end{array}\right) .
$$

Then,

$$
\begin{gathered}
\boldsymbol{a}_{1}=\mathbf{1}_{n} \otimes\binom{1}{0}, \quad \boldsymbol{a}_{2}=\mathbf{1}_{n} \otimes\binom{\mu_{x}}{0}, \quad \boldsymbol{a}_{3}=\operatorname{vec}\left\{\binom{z_{1} \exp \left(\gamma z_{1}\right)}{0} \cdots\binom{z_{n} \exp \left(\gamma z_{n}\right)}{0}\right\}, \\
\boldsymbol{a}_{4}=\mathbf{1}_{n} \otimes\binom{\beta}{1} \quad \text { and } \quad \boldsymbol{a}_{5}=\boldsymbol{a}_{6}=\boldsymbol{a}_{7}=\mathbf{0},
\end{gathered}
$$

where $\mathbf{1}_{n}$ denotes an $n \times 1$ vector of ones. Also, $\boldsymbol{a}_{r s}=\mathbf{0}$ for all $r, s$ except for

$$
\boldsymbol{a}_{24}=\boldsymbol{a}_{42}=\mathbf{1}_{n} \otimes\binom{1}{0} \quad \text { and } \quad \boldsymbol{a}_{33}=\operatorname{vec}\left\{\binom{z_{1}^{2} \exp \left(\gamma z_{1}\right)}{0} \cdots\binom{z_{n}^{2} \exp \left(\gamma z_{n}\right)}{0}\right\} .
$$

Also, $\boldsymbol{C}_{r}=\mathbf{0}$ for all $r$ except for

$$
\left.\boldsymbol{C}_{2}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
2 \beta \sigma_{x}^{2} & \sigma_{x}^{2} \\
\sigma_{x}^{2} & 0
\end{array}\right), \quad \boldsymbol{C}_{5}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
\beta^{2} & \beta \\
\beta & 1
\end{array}\right), \quad \boldsymbol{C}_{6}=\stackrel{n}{i=1}^{\exp \left(\eta z_{i}\right)} 00\right)
$$

and

$$
\boldsymbol{C}_{7}=\underset{i=1}{\stackrel{n}{\oplus}}\left(\begin{array}{cc}
z_{i} \sigma^{2} \exp \left(\eta z_{i}\right) & 0 \\
0 & 0
\end{array}\right)
$$

where $\oplus$ is the direct sum of matrices. Additionally, $\boldsymbol{C}_{r s}=\mathbf{0}$ for all $r, s$ except for

$$
\begin{aligned}
\boldsymbol{C}_{22}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
2 \sigma_{x}^{2} & 0 \\
0 & 0
\end{array}\right), \quad \boldsymbol{C}_{25}=\boldsymbol{C}_{52}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
2 \beta & 1 \\
1 & 0
\end{array}\right) \\
\boldsymbol{C}_{67}=\boldsymbol{C}_{76}=\underset{i=1}{\stackrel{n}{\oplus}}\left(\begin{array}{cc}
z_{i} \exp \left(\eta z_{i}\right) & 0 \\
0 & 0
\end{array}\right) \quad \text { and } \quad \boldsymbol{C}_{77}=\underset{i=1}{\stackrel{n}{\oplus}}\left(\begin{array}{cc}
z_{i}^{2} \sigma^{2} \exp \left(\eta z_{i}\right) & 0 \\
0 & 0
\end{array}\right) .
\end{aligned}
$$

Thus, $\widetilde{\boldsymbol{D}}=\left(\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \boldsymbol{a}_{3}, \boldsymbol{a}_{4}, \mathbf{0}, \mathbf{0}, \mathbf{0}\right), \widetilde{\boldsymbol{V}}=\left(\mathbf{0}, \operatorname{vec}\left(\boldsymbol{C}_{2}\right), \mathbf{0}, \mathbf{0}, \operatorname{vec}\left(\boldsymbol{C}_{5}\right), \operatorname{vec}\left(\boldsymbol{C}_{6}\right), \operatorname{vec}\left(\boldsymbol{C}_{7}\right)\right)$ and the matrix formula (11) can be used to compute the second-order bias for this model. Notice that, as $\operatorname{vec}\left(\boldsymbol{C}_{2}\right)$ is not equal to zero, the derivation of algebraic expression using matrix formula (11) becomes very tedious, since the structure of $\boldsymbol{K}_{\boldsymbol{\theta}}$ is not block-diagonal unlike the two previous examples. However, using MAPLE, for example, the derivation can be easily done. Also, the $n^{-1}$ bias vector $\boldsymbol{B}(\widehat{\boldsymbol{\theta}})$ can be obtained numerically via software with numerical linear algebra facilities with minimal effort such as R and Ox .

## 5 Simulation study

We recall that, for large samples the biases of the MLEs are neglible. However, for small and moderate sample sizes the second-order biases may be large and can be used to improve the estimation. We shall use Monte Carlo simulation to evaluate the finite sample performance of the original MLEs and their corrected versions. All simulations were performed using $R$ ( $R$ Development Core Team, 2006). The sample sizes considered were $n=15,25,35,50$ and 100, the number of Monte Carlo replications was 5,000.

We consider the simple errors-in-variables model as described in Fuller (1987):

$$
Y_{i}=\alpha+\beta x_{i}+e_{i} \quad \text { and } \quad X_{i}=x_{i}+u_{i}
$$

where $x_{i} \sim \mathcal{N}\left(\mu_{x}, \sigma_{x}^{2}\right)$ and $u_{i} \sim \mathcal{N}\left(0, \sigma_{u}^{2}\right)$ are the measurement errors with $\sigma_{u}^{2}$ known and $e_{i} \sim \mathcal{N}\left(0, \sigma^{2}\right)$, with $i=1,2, \ldots, n$. Here, $\boldsymbol{\theta}=\left(\alpha, \beta, \mu_{x}, \sigma_{x}^{2}, \sigma^{2}\right)^{\top}$ and

$$
\boldsymbol{\mu}=\mathbf{1}_{n} \otimes\binom{\alpha+\beta \mu_{x}}{\mu_{x}} \quad \text { and } \quad \boldsymbol{\Sigma}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
\beta^{2} \sigma_{x}^{2}+\sigma^{2} & \beta \sigma_{x}^{2} \\
\beta \sigma_{x}^{2} & \sigma_{x}^{2}+\sigma_{u}^{2}
\end{array}\right) .
$$

From the previous expressions, we have immediately that

$$
\boldsymbol{a}_{1}=\mathbf{1}_{n} \otimes\binom{1}{0}, \quad \boldsymbol{a}_{2}=\mathbf{1}_{n} \otimes\binom{\mu_{x}}{0}, \quad \boldsymbol{a}_{3}=\mathbf{1}_{n} \otimes\binom{\beta}{1}, \quad \boldsymbol{a}_{4}=\boldsymbol{a}_{5}=\mathbf{0}
$$

and $\boldsymbol{a}_{r s}=\mathbf{0}$ for all $r, s$ except for

$$
\boldsymbol{a}_{23}=\boldsymbol{a}_{32}=\mathbf{1}_{n} \otimes\binom{1}{0}
$$

Also, $\boldsymbol{C}_{r}=\mathbf{0}$ for all $r$ except for

$$
\boldsymbol{C}_{2}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
2 \beta \sigma_{x}^{2} & \sigma_{x}^{2} \\
\sigma_{x}^{2} & 0
\end{array}\right), \boldsymbol{C}_{4}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
\beta^{2} & \beta \\
\beta & 1
\end{array}\right) \quad \text { and } \quad \boldsymbol{C}_{5}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
1 & 0 \\
0 & 0
\end{array}\right) .
$$

Additionally, $\boldsymbol{C}_{r s}=\mathbf{0}$ for all $r, s$ except for

$$
\boldsymbol{C}_{22}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
2 \sigma_{x}^{2} & 0 \\
0 & 0
\end{array}\right) \text { and } \boldsymbol{C}_{24}=\boldsymbol{C}_{42}=\boldsymbol{I}_{n} \otimes\left(\begin{array}{cc}
2 \beta & 1 \\
1 & 0
\end{array}\right)
$$

Thus, $\widetilde{\boldsymbol{D}}=\left(\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \boldsymbol{a}_{3}, \mathbf{0}, \mathbf{0}\right)$ and $\tilde{\boldsymbol{V}}=\left(\mathbf{0}, \operatorname{vec}\left(\boldsymbol{C}_{2}\right), \mathbf{0}, \operatorname{vec}\left(\boldsymbol{C}_{4}\right), \operatorname{vec}\left(\boldsymbol{C}_{5}\right)\right)$. Therefore, all the quantities necessary to calculate $\boldsymbol{B}(\widehat{\boldsymbol{\theta}})$ using expression (11) are given.

In order to analyze the point estimation results, we computed, for each sample size and for each estimator: the relative bias (the relative bias of an estimator $\widehat{\theta}$ is defined as $\{\mathbb{E}(\widehat{\theta})-\theta\} / \theta$, its estimate being obtained by estimating $\mathbb{E}(\widehat{\theta})$ by Monte Carlo) and the root mean square error, i.e., $\sqrt{\mathrm{MSE}}$, where MSE is the mean squared error estimated from the 5,000 Monte Carlo replications. Without loss of generality, the true values of the regression parameters were set at $\alpha=67, \beta=0.42, \mu_{x}=70$, $\sigma_{x}^{2}=247$ and $\sigma^{2}=43$. The parameter setting were choosen in order to represent the dataset (yields of corn on Marshall soil in Iowa) presented in Fuller (1987, p. 18). The known measurement error variance is $\sigma_{u}^{2}=57$ (which was attained through a previous experiment).

Table 1 gives the relative biases and $\sqrt{\mathrm{MSE}}$ of both uncorrected and corrected estimates. The figures in this table confirm that the bias-corrected estimates are generally closer to the true parameter values than the unadjusted estimates. We observe that, in absolute value, the estimated relative biases of the bias-corrected estimator were smaller than that of the original MLE for all sample sizes considered, thus showing the effectiveness of the bias correction schemes used in the definition of these estimators.

For instance, when $n=15$, the estimated relative bias of the estimators of $\alpha$, $\beta, \mu_{x}, \sigma_{x}^{2}$ and $\sigma^{2}$ average -0.0518 whereas the biases of the five corresponding biasadjusted estimators average -0.0056 ; that is, the average bias (in value absolute) of the MLEs is almost ten times larger than that of the bias-corrected estimators. This suggests that the second-order bias of MLEs should not be ignored in samples of small to moderate sizes since they can be nonnegligible.

We can readily see that the MLEs of $\sigma_{x}^{2}$ and $\sigma^{2}$ are on average far from the true parameter value, thus displaying large bias, for the different sample sizes considered, even when $n=100$. This stresses the importance of using a bias correction. For instance, when $n=50$, the relative biases of $\widehat{\sigma}_{x}^{2}$ and $\widehat{\sigma}^{2}$ (MLEs) were -0.0226 and -0.0563 , respectively, while the relative biases of $\widetilde{\sigma}_{x}^{2}$ and $\widetilde{\sigma}^{2}$ (BCEs) were 0.0016 (sixteen times lesser) and -0.0011 (fifty times lesser), respectively. Observe that the MLEs are always underestimating the true values of $\sigma_{x}^{2}$ and $\sigma^{2}$, since their biases are always negatives. Note also that root mean square error decrease with $n$, as expected. Additionally, we note that all estimators have similar root mean squared errors.

## 6 An empirical ilustration

Next, as an empirical ilustration, consider a small data set given by Fuller (1987, p. 18). The data set is presented in Table 2. The data are yields of corn and determinations of available soil nitrogen collected at 11 sites on Marshall soil in Iowa. Following Fuller (1987, p. 18), we assume that the estimates of soil nitrogen contain measurement erros arise from two sources. First, only a small sample of soil is selected from each plot and, as a result, there is the sampling error associated with the use of sample to represent the whole. Second, there is a measurement error associated with the chemical analysis used to determined the level of nitrogen in the soil sample. The variance arising from these two sources is $\sigma_{u}^{2}=57$. According to

Table 1: Relative biases and $\sqrt{\text { MSE }}$ of uncorrected and corrected estimates for an errors-in-variables model.
| $n$ | $\theta$ | MLE |  | BCE |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | Rel. bias | $\sqrt{\text { MSE }}$ | Rel. bias | $\sqrt{\mathrm{MSE}}$ |
| 15 | $\alpha$ | -0.0240 | 12.46 | 0.0232 | 11.29 |
|  | $\beta$ | 0.0547 | 0.17 | -0.0526 | 0.16 |
|  | $\mu_{x}$ | 0.0014 | 4.48 | 0.0014 | 4.48 |
|  | $\sigma_{x}^{2}$ | -0.0796 | 108.49 | -0.0029 | 113.81 |
|  | $\sigma^{2}$ | -0.1807 | 19.52 | 0.0031 | 20.38 |
| 25 | $\alpha$ | -0.0198 | 9.05 | 0.0009 | 8.14 |
|  | $\beta$ | 0.0440 | 0.13 | -0.0029 | 0.11 |
|  | $\mu_{x}$ | 0.0004 | 3.43 | 0.0004 | 3.43 |
|  | $\sigma_{x}^{2}$ | -0.0553 | 85.73 | -0.0082 | 88.05 |
|  | $\sigma^{2}$ | -0.1198 | 15.48 | -0.0104 | 15.73 |
| 35 | $\alpha$ | -0.0117 | 7.05 | 0.0010 | 6.68 |
|  | $\beta$ | 0.0267 | 0.10 | -0.0023 | 0.09 |
|  | $\mu_{x}$ | -0.0001 | 2.96 | -0.0001 | 2.96 |
|  | $\sigma_{x}^{2}$ | -0.0424 | 71.36 | -0.0084 | 72.64 |
|  | $\sigma^{2}$ | -0.0799 | 12.83 | -0.0014 | 13.04 |
| 50 | $\alpha$ | -0.0080 | 5.69 | 0.0002 | 5.50 |
|  | $\beta$ | 0.0190 | 0.08 | 0.0005 | 0.08 |
|  | $\mu_{x}$ | -0.0007 | 2.45 | -0.0007 | 2.45 |
|  | $\sigma_{x}^{2}$ | -0.0226 | 60.76 | 0.0016 | 61.71 |
|  | $\sigma^{2}$ | -0.0563 | 10.75 | -0.0011 | 10.89 |
| 100 | $\alpha$ | -0.0025 | 3.83 | 0.0013 | 3.78 |
|  | $\beta$ | 0.0057 | 0.05 | -0.0029 | 0.05 |
|  | $\mu_{x}$ | 0.0002 | 1.72 | 0.0002 | 1.72 |
|  | $\sigma_{x}^{2}$ | -0.0131 | 42.24 | -0.0009 | 42.54 |
|  | $\sigma^{2}$ | -0.0298 | 7.63 | -0.0021 | 7.67 |


BCE : bias-corrected estimator.

Fuller (1987, p. 18), model (2) is a valid representation to these data.

Table 2: Yields of corn on Marshall soil in Iowa.
|  | Yield <br> $(Y)$ | Soil <br> Nitrogen <br> $(X)$ | Site | Yield <br> $(Y)$ | Soil <br> Nitrogen <br> $(X)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 86 | 70 | 7 | 99 | 50 |
| 2 | 115 | 97 | 8 | 96 | 70 |
| 3 | 90 | 53 | 9 | 99 | 94 |
| 4 | 86 | 64 | 10 | 104 | 69 |
| 5 | 110 | 95 | 11 | 96 | 51 |
| 6 | 91 | 64 |  |  |  |


The MLEs, the large-sample estimates of the corresponding standard errors, the biases and the bias-corrected estimates are given Table 3. These estimates were obtained using R. The figures in this table show that the biases of the estimates of $\alpha$ and $\beta$ are much less than standard errors of the corresponding estimates. In cases of marginal statistical significance, biases of this maginitude could have a small effect on the conclusions. However, note that the MLEs of $\sigma_{x}^{2}$ and $\sigma^{2}$ are strongly biased, as evidenced by our simulations studies, i.e., they underestimate the model variances. Therefore, the bias-corrected estimates may be used instead of the MLEs to make point inferences.

Table 3: MLEs and bias-corrected estimatives.
| Parameter | MLEs | S.E. | Bias | BCEs |
| :---: | ---: | ---: | ---: | ---: |
| $\alpha$ | 66.8606 | 11.7272 | -2.5334 | 69.3939 |
| $\beta$ | 0.4331 | 0.1633 | 0.0359 | 0.3973 |
| $\mu_{x}$ | 70.6364 | 5.0194 | 0.0000 | 70.6364 |
| $\sigma_{x}^{2}$ | 220.1405 | 118.1731 | -25.1946 | 245.3351 |
| $\sigma^{2}$ | 38.4058 | 20.9357 | -10.3344 | 48.7402 |


BCE: bias-corrected estimate.

Figure 1 presents the scatterplot of the data together with the fitted lines obtained using the MLEs and BCEs. Notice that the line produced by the bias correction scheme the inclination slightly attenuated and intercept increased relative to the non-corrected one.

## 7 Conclusions

This paper proposed a bias correction for a multivariate normal model with a quite general parameterization. The main result centers on models where the mean and the variance share the same vector of parameters. Many models are particular cases of the proposed model such as (non)linear regressions, errors-in-variables models,

![](https://cdn.mathpix.com/cropped/780c7c94-6353-4780-bab4-30d6772a71ee-15.jpg?height=723&width=1090&top_left_y=388&top_left_x=502)
Figure 1: Scatterplot for the data set together with the fitted lines.

mixed models, factor analysis and so forth. We have shown that it is always possible to express the second order bias vector of the maximum likelihood estimates as an ordinary weighted least-squares regression. Moreover, we derived a bias-adjustment scheme that nearly eliminates the bias of the maximum likelihood estimator in small and moderate samples. Our simulation results suggest that the bias correction we have derived is very effective, even when the sample size is small. Indeed, the bias correction mechanism proposed in this paper yields modified maximum likelihood estimators that are nearly unbiased. We also presented an empirical ilustration that illustrates the proposed bias-adjustment scheme.

## Acknowledgments

We gratefully acknowledge grants from FAPESP. We wish to thank Francisco CribariNeto for valuable comments on this manuscript.

## References

Abell, M.L., Braselton, J.P. (1994). The Maple V Handbook. AP Professional, New York.
Akritas, M.G., Bershady, M.A. (1996). Linear regression for astronomical data with measurement errors and intrinsic scatter. The Astrophysical Journal. 470:706-714.

Beale, E.M.L. (1960). Confidence regions in non-linear estimation (with discussion). Journal of the Royal Statistical Societ B. 22:41-88.

Box, M.J. (1971). Bias in nonlinear estimation (with discussion). Journal of the Royal Statistical Societ B. 33:171-201.

Cheng, C.L., Riu J. (2006). On estimating linear relationships when both variables are subject to heteroscedastic measurement errors. Technometrics. 48:511-519.

Cook, R.D., Tsai, C., Wei, B.(1986). Bias in nonlinear regression. Biometrika. 73:615-623.
Cordeiro, G.M. (2008). Corrected maximum likelihood estimators in linear heteroskedastic regression models. Brazilian Review of Econometrics. 28:53-67.

Cordeiro, G.M., Demétrio, C.G.B. (2008). Corrected estimators in extended quasilikelihood models. Communications in Statistics, Theory and Methods. 37:873-880.

Cordeiro, G.M., Ferrari, S.L.P., Uribe-Opazo, M.A., Vasconcellos, K.L.P. (2000). Corrected maximum-likelihood estimation in a class of symmetric nonlinear regression models. Statistics and Probability Letters. 46:317-328.

Cordeiro, G.M., Klein, R. (1994). Bias correction in ARMA models. Statistics and Probability Letters. 19:169-176.

Cordeiro, G.M., McCullagh, P. (1991). Bias correction in generalized linear models. Journal of the Royal Statistical Society B. 53:629-643.

Cordeiro, G.M., Vasconcellos, K.L.P. (1997). Bias correction for a class of multivariate nonlinear regression models. Statistics and Probability Letters. 35:155-164.

Cordeiro, G.M., Vasconcellos, K.L.P. (1999). Second-order biases of the maximum likelihood estimates in von Mises regression models. Australian and New Zealand Journal of Statistics. 41:901-910.

Cordeiro, G.M., Toyama, M.C. (2008). Bias correction in generalized nonlinear models with dispersion covariates. Communications in Statistics, Theory and Methods. 37:2219-2225.

Cox, D.R., Hinkley, D.V. (1974). Theoretical Statistics. London: Chapman and Hall.
Cox, D.R., Reid, N. (1987). Parameter orthogonality and approximate conditional inference (with discussion). Journal of the Royal Statistical Society B. 40:1-39.

Cox, D.R., Snell, E. (1968). A general definition of residuals (with discussion). Journal of the Royal Statistical Society. 30:248-275.
de Castro, M., Galea, M., Bolfarine, H. (2008). Hypothesis testing in an errors-in-variables model with heteroscedastic measurement errors. Statistics in Medicine. 27:5217-5234.

Doornik, J.A. (2006). An Object-Oriented Matrix Language - Ox 4. Timberlake Consultants Press, London. 5th ed.

Efron, B., Tibshirani, R.J. (1993). An introduction to the bootstrap. Chapman and Hall, New York.

Firth, D. (1993). Bias reduction of maximum likelihood estimates. Biometrika. 80:27-38.
Fuller, W. (1987). Measurement Error Models. Wiley: Chichester.

Kelly, B.C. (2007). Some aspects of measurement error in linear regression of astronomical data. The Astrophysical Journal. 665:1489-1506.

Kelly, B.C., Bechtold, J., Trump, J.R., Vertergaard, M., Siemiginowska, A. (2008). Observational constraints on the dependence of ratio-quiet quasar X-ray emission on black hole mass and accretion rate. Astrophysical Journal Supplement Series. 176(2): 355373.

Kulathinal, S.B., Kuulasmaa, K., Gasbarra, D. (2002). Estimation of an errors-in-variables regression model when the variances of the measurement error vary between the observations. Statistics in Medicine. 21:1089-1101.

Lawley, D.N. (1956). A general method for approximating to the distribution of likelihood ratio criteria. Biometrika. 43:295-303.

Magnus, J.R., Neudecker, H. (1988). Matrix differential calculus. Wiley: New York.
R Development Core Team (2006). R: A Language and Environment for Statistical Computing. Vienna, Austria. ISBN 3-900051-07-0. http://www.R-project.org.

Vasconcellos, K.L.P., Cordeiro, G.M. (1997). Approximate bias for multivariate nonlinear heteroscedastic regressions. Brazilian Journal of Probability and Statistics. 11:141-159.

Vasconcellos, K.L.P., Cordeiro, G.M. (2000). Bias corrected estimates in multivariate Student $t$ regression models. Communications in Statistics, Theory and Methods. 29:797822.

Vasconcellos, K.L.P., Cribari-Neto, F. (2005). Improved maximum likelihood estimation in a new class of beta regression models. Brazilian Journal of Probability and Statistics. 19:13-31.

