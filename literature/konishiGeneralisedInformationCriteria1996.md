---
citekey: konishiGeneralisedInformationCriteria1996
item_type: article
authors: 'Konishi, Sadanori and Kitagawa, Genshiro'
year: 1996
title: Generalised Information Criteria in Model Selection
venue: Biometrika
volume: 83
issue: 4
pages: 875--890
doi: 10.1093/biomet/83.4.875
eprint: 'https://academic.oup.com/biomet/article-pdf/83/4/875/703557/83-4-875.pdf'
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\konishiGeneralisedInformationCriteria1996.pdf'
pdf_sha256: 44df10d831119aeeafacb152e9e13c3c618c66e01ca2a82f2f938d337dadde2f
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-31T18:19:00Z
---
# Generalised information criteria in model selection 

By SADANORI KONISHI<br>Graduate School of Mathematics, Kyushu University, 6-10-1 Hakozaki, Higashi-ku, Fukuoka 812, Japan

and GENSHIRO KITAGAWA<br>The Institute of Statistical Mathematics, 4-6-7 Minami-Azabu, Minato-ku, Tokyo 106, Japan


#### Abstract

Summary The problem of evaluating the goodness of statistical models is investigated from an information-theoretic point of view. Information criteria are proposed for evaluating models constructed by various estimation procedures when the specified family of probability distributions does not contain the distribution generating the data. The proposed criteria are applied to the evaluation of models estimated by maximum likelihood, robust, penalised likelihood, Bayes procedures, etc. We also discuss the use of the bootstrap in model evaluation problems and present a variance reduction technique in the bootstrap simulation.


Some key words: AIC; Bayes approach; Efficient bootstrap simulation; Information criterion; M-estimators; Penalised likelihood; Predictive distribution; Statistical functional.

## 1. Introduction

Akaike's information criterion AIC (Akaike, 1973, 1974) is a model evaluation and selection tool which can be thought of in terms of estimating the Kullback \& Leibler (1951) information of the true model with respect to the fitted model. It can be derived under the assumptions that
(i) estimation is by maximum likelihood, and
(ii) this is carried out in a parametric family of distributions including the true model.

We introduce criteria which estimate the same Kullback-Leibler information as does the aIC, relaxing both the assumptions (i) and (ii). The essential point, in our work and Akaike's, is to approximate the bias in a very simple but clearly deficient estimate of the Kullback-Leibler information in question. In § 2 we develop the general theory, using functional-type estimators, and show the simplifications resulting from assumption (i) alone, and then from both (i) and (ii). In § 3 the information criteria proposed are applied to the evaluation of the various types of models based on robust, penalised likelihood and Bayes estimation procedures. In §4 the variance reduction technique in the bootstrap simulation is investigated, and it is shown that the variance of the bootstrap estimates caused by simulation can be reduced without any analytical derivations. The derivation of the proposed criteria is given in the Appendix.

## 2. Generalised information criteria

Suppose that $X_{n}$ is a random sample of size $n$ from an unknown distribution $G(x)$ having probability density function $g(x)$. Estimation is done within a parametric family
of distributions with densities $\{f(x \mid \theta) ; \theta \in \Theta\}$, which may or may not contain $g$. Here $\theta$ is a $p$-dimensional vector of unknown parameters. The predictive density function $f(z \mid \hat{\theta})$ for a future observation $z$ can be constructed by replacing the unknown parameter vector $\theta$ by some efficient estimate $\hat{\theta}$, for which maximum likelihood, robust or penalised likelihood procedures are used for parameter estimation. The development in terms of this simple predictive density will also apply, with some modification, to the Bayesian one.

Model selection can be approached by trying to make small the Kullback-Leibler information (Kullback \& Leibler, 1951)

$$
I\{g(z) ; f(z \mid \hat{\theta})\}:=\int g(z) \log g(z) d z-\int g(z) \log f(z \mid \hat{\theta}) d z
$$

which is a measure of the divergence of $g(z)$ relative to $f(z \mid \hat{\theta})$. The first term on the righthand side of (1) does not depend on the model and only the second term, the expected log likelihood,

$$
\eta\left(X_{n} ; G\right):=\int g(z) \log f(z \mid \hat{\theta}) d z=\int \log f(z \mid \hat{\theta}) d G(z)
$$

is relevant.
A simple estimator of $\eta\left(X_{n} ; G\right)$ is given by substituting for $G$ the empirical distribution $\hat{G}$, yielding the log likelihood

$$
\eta\left(X_{n} ; \hat{G}\right)=\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}\right)
$$

Ordinarily this provides an overestimate of the expected $\log$ likelihood, since $\hat{G}$ corresponds more closely to $\hat{\theta}$ than does the true $G$. Writing the bias as

$$
b(G):=E_{G}\left\{\eta\left(X_{n} ; \widehat{G}\right)-\eta\left(X_{n} ; G\right)\right\},
$$

we define an information criterion based on the bias-corrected log likelihood as

$$
\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}\right)-b(\widehat{G}) .
$$

Akaike (1973) showed that $b(G)$ is asymptotically $p / n$ under the assumptions that estimation is by maximum likelihood and the specified parametric model contains the true distribution $g$. Hence the AIC can be considered as a criterion obtained by correcting the asymptotic bias of the log likelihood of the estimated model.

In order to remove both of the assumptions imposed on AIC, we first consider bias correction of the log likelihood when $\hat{\theta}$ is a functional estimator, namely when $\hat{\theta}$ is defined by $\hat{\theta}=T(\hat{G})$ with $T$ being a suitably defined $p$-dimensional regular functional. It is assumed that the functional under consideration is Fisher consistent, that is $T\left(F_{\theta}\right)=\theta$ for all $\theta \in \Theta$, where $F_{\theta}$ is the distribution function of the specified probability density $f(x \mid \theta)$. Then the bias of the log likelihood is given in the following theorem.

Theorem 2.1. Let $\eta\left(X_{n} ; G\right)$ and $\eta\left(X_{n} ; \widehat{G}\right)$ be the expected log likelihood in (2) and the log likelihood in (3), respectively. Suppose that the parametric family of distributions does not necessarily contain the true distribution and that the statistical functional T(.) is secondorder compact differentiable at $G$. Then the asymptotic bias of the log likelihood in the
estimation of the expected log likelihood is given by

$$
E_{G}\left\{\eta\left(X_{n} ; \hat{G}\right)-\eta\left(X_{n} ; G\right)\right\}=\frac{1}{n} b_{1}(G)+o\left(\frac{1}{n}\right),
$$

where

$$
b_{1}(G)=\operatorname{tr}\left\{\left.\int T^{(1)}(z ; G) \frac{\partial \log f(z \mid \theta)}{\partial \theta^{\prime}}\right|_{T(G)} d G(z)\right\},
$$

and $T^{(1)}(z ; G)=\left(T_{1}^{(1)}(z ; G), \ldots, T_{p}^{(1)}(z ; G)\right)^{\prime}$ is the influence function of a $p$-dimensional functional $T(G)$ at the distribution $G$.

The derivation is given in the Appendix.
Let $b_{1}(\widehat{G})$ be a bias estimate obtained by replacing the unknown distribution $G$ by the empirical distribution $\hat{G}$. Then we have an information criterion based on the bias corrected log likelihood as follows:

$$
\begin{aligned}
\operatorname{GIC}\left(X_{n} ; \hat{G}\right) & :=-2 n\left\{\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}\right)-\frac{1}{n} b_{1}(\hat{G})\right\} \\
& =-2 \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}\right)+\frac{2}{n} \sum_{\alpha=1}^{n} \operatorname{tr}\left\{\left.T^{(1)}\left(X_{\alpha} ; \hat{G}\right) \frac{\partial \log f\left(X_{\alpha} \mid \theta\right)}{\partial \theta^{\prime}}\right|_{\hat{\theta}}\right\},
\end{aligned}
$$

where $T^{(1)}\left(X_{\alpha} ; \widehat{G}\right)=\left(T_{1}^{(1)}\left(X_{\alpha} ; \widehat{G}\right), \ldots, T_{p}^{(1)}\left(X_{\alpha} ; \widehat{G}\right)\right)^{\prime}$ is the $p$-dimensional empirical influence function defined by

$$
T_{i}^{(1)}\left(X_{\alpha} ; \hat{G}\right)=\lim _{\epsilon \rightarrow 0}\left[T_{i}\left\{(1-\varepsilon) \hat{G}+\varepsilon \delta\left(X_{\alpha}\right)\right\}-T_{i}(\hat{G})\right] / \varepsilon,
$$

with $\delta\left(X_{\alpha}\right)$ being the point mass at $X_{\alpha}$. The influence function $T^{1)}(z ; G)$ and its estimate $T^{(1)}\left(X_{\alpha} ; \hat{G}\right)$ are respectively the derivatives of $T(G)$ and $T(\hat{G})$ with respect to the probability measures $\delta(z)$ and $\delta\left(X_{\alpha}\right)$. For the problem of choosing among different models, we select the model for which the value of the information criterion GIC ( $X_{n} ; \widehat{G}$ ) is smallest.

Theorem $2 \cdot 1$ produces in a simple way criteria for evaluating the models estimated by various types of procedures. We now show how the results simplify for the case of maximum likelihood estimation.

The maximum likelihood estimator, $\hat{\theta}_{\mathrm{ML}}$, can be expressed as $\hat{\theta}_{\mathrm{ML}}=T_{\mathrm{ML}}(\hat{G})$, where $T_{\mathrm{ML}}$ is the $p$-dimensional functional given as a solution of the implicit equation

$$
\left.\int \frac{\partial}{\partial \theta} \log f(z \mid \theta)\right|_{T_{\mathrm{ML}(G)}} d G(z)=0
$$

Replacing $G$ by $(1-\varepsilon) G+\varepsilon \delta(z)$ in the above equation and differentiating with respect to $\varepsilon$, we have the $p$-dimensional influence function of $\hat{\theta}_{\mathrm{ML}}=T_{\mathrm{ML}}(\hat{G})$ in the form

$$
T_{\mathrm{ML}}^{(1)}(z ; G)=\left.J(G)^{-1} \frac{\partial \log f(z \mid \theta)}{\partial \theta}\right|_{T_{\mathrm{ML}}(G)}
$$

where

$$
J(G)=-\left.\int \frac{\partial^{2} \log f(z \mid \theta)}{\partial \theta \partial \theta^{\prime}}\right|_{T_{M L}(G)} d G(z)
$$

Substituting the influence function $T_{\mathrm{ML}}^{(1)}$ given by (7) in the result (5) yields the asymptotic bias $\operatorname{tr}\left\{J(G)^{-1} I(G)\right\}$, where

$$
I(G)=\left.\int \frac{\partial \log f(z \mid \theta)}{\partial \theta} \frac{\partial \log f(z \mid \theta)}{\partial \theta^{\prime}}\right|_{T_{\mathrm{ML}}(G)} d G(z)
$$

Thus for the case of maximum likelihood estimation the information criterion GIC defined by (6) reduces to

$$
\operatorname{TIC}\left(X_{n} ; \hat{G}\right):=-2 \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}_{\mathrm{ML}}\right)+2 \operatorname{tr}\left\{J(\hat{G})^{-1} I(\hat{G})\right\}
$$

where $J(G)$ and $I(G)$ are respectively given by (8) and (9). This criterion was originally introduced by Takeuchi (1976) and discussed by Stone (1977) and Shibata (1989).

If the specified parametric family of densities contains the true distribution, that is $g(z)= f\left(z \mid \theta_{0}\right)$, or $G=F_{\theta_{0}}$, for some $\theta_{0}$ in $\Theta$, then we see that $\operatorname{tr}\left\{J\left(F_{\theta_{0}}\right)^{-1} I\left(F_{\theta_{0}}\right)\right\}=p$, noting the well-known identity $I\left(F_{\theta_{0}}\right)=J\left(F_{\theta_{0}}\right)$. Hence TIC in (10) is further reduced to

$$
\mathrm{AIC}=-2 \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}_{\mathrm{ML}}\right)+2 p
$$

the criterion proposed by Akaike (1973, 1974). Stone (1977) showed that AIC is asymptotically equivalent to the cross-validation which is a naive method for estimating prediction error.

We have so far concentrated on deriving information criteria for the fitted densities in the context of functional statistics. The generalised information criterion given by (6) may not directly be applied to the evaluation of the models with the Bayes and nonfunctional estimators. However, if the Bayesian predictive density, $h\left(z \mid X_{n}\right)$, and the model $f\left(z \mid \hat{\theta}_{U}\right)$ with nonfunctional estimator $\hat{\theta}_{U}$ may be approximated by $f(z \mid \hat{\theta})+O_{p}\left(n^{-1}\right)$ with functional statistic $\hat{\theta}=T(\hat{G})$, then an information criterion similar to GIC in (6) can be obtained as follows.

Theorem 2.2. Let $h\left(z \mid X_{n}\right)$ be a model fitted to the data $X_{n}$ drawn from the distribution $G(x)$. Assume that the fitted model can be expressed as $h\left(z \mid X_{n}\right)=f(z \mid \hat{\theta})+O_{p}\left(n^{-1}\right)$, where $\hat{\theta}=T(\hat{G})$ is a functional statistic for functional $T(G)=\left(T_{1}(G), \ldots, T_{p}(G)\right)^{\prime}$. Then an information criterion for the evaluation of the model $h\left(z \mid X_{n}\right)$ is given by

$$
-2 \sum_{\alpha=1}^{n} \log h\left(X_{\alpha} \mid X_{n}\right)+\frac{2}{n} \sum_{\alpha=1}^{n} \operatorname{tr}\left\{\left.T^{(1)}\left(X_{\alpha} ; \hat{G}\right) \frac{\partial \log f\left(X_{\alpha} \mid \theta\right)}{\partial \theta^{\prime}}\right|_{\hat{\theta}}\right\},
$$

where $T^{(1)}\left(X_{\alpha} ; \hat{G}\right)=\left(T_{1}^{(1)}\left(X_{\alpha} ; \hat{G}\right), \ldots, T_{p}^{(1)}\left(X_{\alpha} ; \hat{G}\right)\right)^{\prime}$ is the empirical influence function of $\hat{\theta}=T(\hat{G})$.

If the estimator $\hat{\theta}_{U}$ differs from a functional statistic $\hat{\theta}$ by an error of order $O_{p}\left(n^{-1}\right)$, then $f\left(z \mid \hat{\theta}_{U}\right)=f(z \mid \hat{\theta})+O_{p}\left(n^{-1}\right)$, so that Theorem $2 \cdot 2$ can be directly applied to the evaluation of $f\left(z \mid \hat{\theta}_{U}\right)$. For example, the usual unbiased variance estimator may be expressed as

$$
T(\hat{G})\left\{1+n^{-1}+O_{p}\left(n^{-2}\right)\right\}
$$

where $T(G)=2^{-1} \iint(x-y)^{2} d G(x) d G(y)$. We note that GIC defined by (6) is still valid with the log likelihood of a fitted model $h\left(z \mid X_{n}\right)$ if this predictive distribution can be approximated as $f(z \mid \hat{\theta})+O_{p}\left(n^{-1}\right)$ with functional statistic $\hat{\theta}=T(\hat{G})$.

The criterion AIC given by(11) has some attractive properties in practical applications;
the bias correction term does not require any analytical derivation, and it can be applied in an automatic way in various situations (Kitagawa, 1987). A number of successful applications of AIC in statistical data analysis have been reported; see, e.g., Bozdogan (1994), Sakamoto, Ishiguro \& Kitagawa (1986). The problem is whether the bias of the log likelihood of a fitted model is well approximated by the number of parameters when a specified model deviates from the true distribution.

Figure 1 plots the true bias $n b(G)$ and the estimated bias $\operatorname{tr}\left\{J(\widehat{G})^{-1} I(\widehat{G})\right\}$, with standard errors, in addition to the asymptotic bias $\operatorname{tr}\left\{J(G)^{-1} I(G)\right\}$, for sample sizes $n=25,100$, 400 and 1600 . The true density function $g(x)$ and the model $f(z \mid \theta)$ are respectively assumed to be

$$
g(x)=(1-\varepsilon) \phi(x \mid 0,1)+\varepsilon \phi\left(x \mid 0, d^{2}\right) \quad(d \gg 1), \quad f(x \mid \theta)=\phi\left(x \mid \mu, \sigma^{2}\right),
$$

where $\theta=\left(\mu, \sigma^{2}\right)$, and $\phi\left(x \mid \mu, \sigma^{2}\right)$ denotes the density function of the normal distribution with mean $\mu$ and variance $\sigma^{2}$. The variance $d^{2}$ is arbitrarily set to 10 . For this situation the values of biases are plotted for mixing proportion $\varepsilon$ ranging from 0 to $0 \cdot 2$, in which the

![](https://cdn.mathpix.com/cropped/9878ee9d-119b-4ae7-adaa-805b8142f692-05.jpg?height=1277&width=1489&top_left_y=990&top_left_x=160)
Fig. 1. Comparison of the true bias $n \times b(G)(\rightarrow)$, the asymptotic bias $\operatorname{tr}\left\{J(G)^{-1} I(G)\right\}(---)$ and the estimated asymptotic bias $\operatorname{tr}\left\{J(\hat{G})^{-1} I(\hat{G})\right\}$ (—) with standard errors ( $\cdots \cdots$ ) for the sample sizes $n=25,100,400$ and 1600.

quantities other than the asymptotic bias are evaluated by a Monte Carlo simulation with 100000 repetitions.

It may be seen from Fig. 1 that the log likelihood of a fitted model has a significant bias as an estimate of the expected log likelihood and that the bias is significantly larger than 2 , the approximation by AIC, if the mixing proportion $\varepsilon$ is around 0.07 . It should be noticed here that the amount of contamination in the observed data is often between $5 \%$ and $7 \%$ and this is the region where the bias is large. We observe that for large sample sizes the true bias, the asymptotic bias and the estimated asymptotic bias coincide quite well. On the other hand, for smaller sample sizes such as $n=25$, the estimated asymptotic bias underestimates the true asymptotic bias and the true bias.

## 3. Criteria for evaluating various statistical models <br> 3.1. General

This section gives criteria to evaluate the goodness of the models estimated by robust and penalised maximum likelihood procedures. We also consider an information criterion for the predictive densities of Bayesian methods.

## 3•2. Robust estimation

Let $f\left(x \mid \hat{\theta}_{M}\right)$ be the fitted model to the data $X_{n}$ from the true distribution $G(x)$, where $\hat{\theta}_{M}$ is an $M$-estimator defined as the solution of the implicit equations

$$
\sum_{\alpha=1}^{n} \psi_{i}\left(X_{\alpha}, \hat{\theta}_{M}\right)=0 \quad(i=1, \ldots, p)
$$

with $\psi_{i}$ a function on $\mathscr{X} \times \Theta\left(\Theta \subset R^{p}\right)$ (Huber, 1981). The solution $\hat{\theta}_{M}$ can be written as $T_{M}(\hat{G})$ for the functional given by

$$
\int \psi_{i}\left\{z, T_{M}(G)\right\} d G(z)=0 \quad(i=1, \ldots, p)
$$

It is known, see e.g. Hampel et al. (1986, p. 230), that the influence function of the $M$-estimator is

$$
T_{M}^{(1)}(z ; G)=M(\psi, G)^{-1} \psi\left\{z, T_{M}(G)\right\}
$$

where $\psi=\left(\psi_{1}, \ldots, \psi_{p}\right)^{\prime}$ and the $p \times p$ matrix $M(\psi, G)$ is given by

$$
M(\psi, G)^{\prime}=-\left.\int \frac{\partial \psi(z, \theta)^{\prime}}{\partial \theta}\right|_{T_{M}(G)} d G(z),
$$

under the assumption that the matrix $M$ is nonsingular. Then it follows from Theorem $2 \cdot 1$ that the asymptotic bias of the $\log$ likelihood $n^{-1} \sum \log f\left(X_{\alpha} \mid \hat{\theta}_{M}\right)$ in the estimation of the expected log likelihood (2) with $\hat{\theta}_{M}$ is

$$
b_{M}^{(1)}(G)=\operatorname{tr}\left[\left.M(\psi, G)^{-1} \int \psi\{z, T(G)\} \frac{\partial \log f(z \mid \theta)}{\partial \theta^{\prime}}\right|_{T_{M}(G)} d G(z)\right],
$$

which is estimated by $b_{M}^{(1)}(\hat{G})$.
Let us now consider the situation that the parametric family of densities $\left\{f(x \mid \theta) ; \theta \in \Theta \subset R^{p}\right\}$ contains the true density, that is $g(x)=f\left(x \mid \theta_{0}\right)$ for some $\theta_{0}$ in $\Theta$.

Assume that the functional $T_{M}$ is Fisher consistent. Then the matrix $M$ in (15) can be expressed as

$$
M\left(\psi, F_{\theta}\right)=\int \psi(z, \theta) \frac{\partial \log f(z \mid \theta)}{\partial \theta^{\prime}} d F_{\theta}(z)
$$

where $F_{\theta}(x)$ is the distribution function of $f(x \mid \theta)$ (Hampel et al., 1986, p. 231). By replacing $M(\psi, G)$ in (16) by $M\left(\psi, F_{\theta}\right)$, we have $b_{M}^{(1)}\left(F_{\theta}\right)=p$, which does not depend on unknown parameters. The results on information criteria for $M$-estimator are summarised in the following theorem.

Theorem 3.1. Let $f\left(x \mid \hat{\theta}_{M}\right)$ be the estimated model based on the M-estimator $\hat{\theta}_{M}$ defined by (13). Then an information criterion for $f\left(x \mid \hat{\theta}_{M}\right)$ is

$$
\mathrm{IC}_{M}\left(X_{n} ; \hat{G}\right):=-2 \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}_{M}\right)+2 b_{M}^{(1)}(\hat{G})
$$

where $b_{M}^{(1)}(G)$ is given by (16). If the specified model contains the true distribution and the functional $T_{M}$ defined by (14) is Fisher consistent, then the information criterion (17) can be reduced to

$$
-2 \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}_{M}\right)+2 p
$$

where $p$ is the number of parameters within the model $f(x \mid \theta)$.
It might be noted that the maximum likelihood estimator is an $M$-estimator, corresponding to

$$
\psi\left\{x, T_{M}(G)\right\}=\partial \log f(x \mid \theta) /\left.\partial \theta\right|_{T_{M}(G)}
$$

Hence tic given by (10) can be also obtained by taking this $\psi\left\{x, T_{M}(G)\right\}$ in Theorem 3.1. The use of Theorem $3 \cdot 1$ is illustrated through the following examples.

Example 3.1. Let $\left\{\left(y_{i}, x_{i}\right) ; i=1, \ldots, n\right\}\left(y_{i} \in R, x_{i} \in R^{p}\right)$ be a sample of independent, identically distributed random variables with common distribution $G(y, x)$ having density $g(y, x)$. Consider the linear model

$$
y_{i}=x_{i}^{\prime} \theta+\varepsilon_{i} \quad(i=1, \ldots, n),
$$

where $\theta$ is a $p$-dimensional parameter vector. Let $F(y, x \mid \theta)$ be a model distribution with density $f(y, x \mid \theta)=f_{1}\left(y-x^{\prime} \theta\right) f_{2}(x)$, in which the error $\varepsilon_{i}$ is assumed to be independent of $x_{i}$ and a scale parameter is ignored. In the linear model (18), the $M$-estimator is given as the solution of the system of equations

$$
\sum_{i=1}^{n} \psi\left(y_{i}-x_{i}^{\prime} \hat{\theta}_{R}\right) x_{i}=0
$$

The influence function of the $M$-estimator defined by (19) at the distribution $G$ is

$$
T_{R}^{(1)}(G)=\left[\int \psi^{\prime}\left\{y-x^{\prime} T_{R}(G)\right\} x x^{\prime} d G\right]^{-1} \psi\left\{y-x^{\prime} T_{R}(G)\right\} x
$$

where $\psi^{\prime}(z)=\partial \psi(z) / \partial z$ and $T_{R}(G)$ is the functional given by

$$
\int \psi\left\{y-x^{\prime} T_{R}(G)\right\} x d G=0
$$

Then it follows from Theorem $3 \cdot 1$ that the asymptotic bias of the log likelihood of $f\left(y, x \mid \hat{\theta}_{R}\right)$ is

$$
b_{R}^{(1)}(G)=\operatorname{tr}\left(\left.\left[\int \psi^{\prime}\left\{y-x^{\prime} T_{R}(G)\right\} x x^{\prime} d G\right]^{-1} \int \psi\left\{y-x^{\prime} T_{R}(G)\right\} x \frac{\partial \log f(y, x \mid \theta)}{\partial \theta^{\prime}}\right|_{T_{R}(G)} d G\right)
$$

Suppose that the true density $g$ can be written in the form $g(y, x)=g_{1}\left(y-x^{\prime} \theta\right) g_{2}(x)$, and that the $M$-estimator defined by (19) is the maximum likelihood estimator for the model $f(y, x \mid \theta)$, that is $\partial \log f(y, x \mid \theta) / \partial \theta=\psi\left(y-x^{\prime} \theta\right) x$. Then the asymptotic bias $b_{R}^{(1)}(G)$ in (20) can be reduced to $E_{g_{1}}\left(\psi^{\prime}\right)^{-1} E_{g_{1}}\left(\psi^{2}\right) p$, which agrees with the result given by Ronchetti (1985, p. 23).

For an ordinary Gaussian linear regression model, Sugiura (1978) obtained the bias of a log likelihood in closed form when the specified model includes the true one, and Hurvich \& Tsai (1991) considered this problem under the assumption that the candidate models do not include the true model. In regression Mallow's (1973) $C_{p}$ is a classical model selection procedure and equivalent to AIC. A robust version of Mallow's $C_{p}$ was presented by Ronchetti \& Staudte (1994).

Example 3•2: Numerical result. Consider the parametric model $F_{\theta}(x)=\Phi\{(x-\mu) / \sigma\}$, where $\Phi$ is the standard normal distribution function. It is assumed that the parametric family of distributions $\left\{F_{\theta}(x) ; \theta \in \Theta \subset R^{2}\right\}$ contains the true distribution generating the data $X_{n}$. The location and scale parameters are respectively estimated by the median, $\hat{\mu}_{m}=\operatorname{med}_{i}\left\{X_{i}\right\}$, and the median absolute deviation, $\hat{\sigma}_{m}=(1 / c) \operatorname{med}_{i}\left\{\left|X_{i}-\operatorname{med}_{j}\left(X_{j}\right)\right|\right\}$, where $c=\Phi^{-1}(0.75)$ is chosen to make $\hat{\sigma}_{m}$ Fisher consistent for $\Phi$.

Table 1. Estimates of the biases for the M-estimator and the maximum likelihood estimator obtained by a Monte Carlo simulation
|  | $n=25$ | $n=50$ | $n=100$ | $n=200$ | $n=400$ | $n=800$ | $n=1600$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Robust | $3 \cdot 839$ | $2 \cdot 569$ | $2 \cdot 250$ | $2 \cdot 125$ | $2 \cdot 056$ | $2 \cdot 029$ | $2 \cdot 013$ |
| MLE | $2 \cdot 229$ | $2 \cdot 079$ | $2 \cdot 047$ | $2 \cdot 032$ | $2 \cdot 014$ | $2 \cdot 002$ | $2 \cdot 003$ |


Table 1 compares the biases ( $\times n$ ) of the log likelihoods for the $M$-estimator ( $\hat{\mu}_{m}, \hat{\partial}_{m}$ ) and the maximum likelihood estimator ( $\hat{\mu}, \hat{\sigma}^{2}$ ) obtained by averaging over 100000 repeated Monte Carlo trials. Note that the bias for the maximum likelihood estimator is analytically given by $n b(G)=2 n /(n-3)$. From the table it may be observed that both of the biases actually converge to the asymptotic bias, 2 , as the sample size $n$ gets larger and that the convergence of the bias for the robust estimator is slower than that for the maximum likelihood estimator.

### 3.3. Penalised likelihood estimation

We consider a criterion for models estimated by procedures based on penalised likelihoods (Good \& Gaskins, 1971) in the context of $M$-estimators. Let $T_{\lambda}$ be the $p$-dimensional statistical functional determined by the system of equations

$$
\left.\int \frac{\partial}{\partial \theta}\{\log f(z \mid \theta)-\lambda k(\theta)\}\right|_{T_{\lambda}(G)} d G(z)=0
$$

where the penalty function $k(\theta)$ is assumed to be twice continuously differentiable. Then the estimate $\hat{\theta}_{\lambda}=T_{\lambda}(\hat{G})$ is a maximum penalised likelihood estimate defined by the functional $T_{\lambda}$.

Taking

$$
\psi\left\{z, T_{\lambda}(G)\right\}=\partial\{\log f(z \mid \theta)-\lambda k(\theta)\} / \partial \theta
$$

at $\theta=T_{\lambda}(G)$ in the formula (16) and replacing $G$ by the empirical distribution function $\hat{G}$ give the information criterion for the model $f\left(x \mid \hat{\theta}_{\lambda}\right)$ as

$$
\mathrm{IC}_{P}\left(X_{n} ; \hat{G}\right)=-2 \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}_{\lambda}\right)+2 \operatorname{tr}\left\{J_{\lambda}(\hat{G})^{-1} I_{\lambda}(\hat{G})\right\}
$$

where

$$
I_{\lambda}(\hat{G})=\left.\frac{1}{n} \sum_{\alpha=1}^{n} \psi\left(X_{\alpha}, \hat{\theta}_{\lambda}\right) \frac{\partial \log f\left(X_{\alpha} \mid \theta\right)}{\partial \theta^{\prime}}\right|_{\hat{\theta}_{\lambda}}, \quad J_{\lambda}(\hat{G})=-\left.\frac{1}{n} \sum_{\alpha=1}^{n} \frac{\partial \psi\left(X_{\alpha}, \theta\right)^{\prime}}{\partial \theta}\right|_{\hat{\theta}_{\lambda}} .
$$

An optimal value of $\lambda$ is chosen such that the information criterion IC $_{P}$ in (21) is minimal. If the penalty function $k(\theta)$ does not depend on the distribution $G$, then $\int \psi\left\{z, T_{\lambda}(G)\right\} \partial k(\theta) / \partial \theta^{\prime} d G(z)=0$, so that the information criterion (21) agrees with the result obtained by Shibata (1989). Green (1987) examined penalised likelihood estimation in the context of general regression models and introduced various types of roughness penalties.

### 3.4. Predictive distributions

The predictive density function in the Bayesian framework is defined by

$$
h\left(z \mid X_{n}\right)=\int f(z \mid \theta) \pi\left(\theta \mid X_{n}\right) d \theta
$$

where $\pi\left(\theta \mid X_{n}\right)$ is the posterior density function for $\theta$ based on a prior $\pi(\theta)$ and the data $X_{n}$. It is required to approximate the predictive density with an error of order at least $O_{p}\left(n^{-1}\right)$, for which we use Laplace's methods for integrals in the Bayesian framework developed by Tierney \& Kadane (1986) and Davison (1986). The predictive density may be expressed as

$$
\begin{aligned}
h\left(z \mid X_{n}\right) & =\int f(z \mid \theta) \prod_{\alpha=1}^{n} f\left(X_{\alpha} \mid \theta\right) \pi(\theta) d \theta / \int \prod_{\alpha=1}^{n} f\left(X_{\alpha} \mid \theta\right) \pi(\theta) d \theta \\
& =\int \exp \left\{q\left(\theta \mid X_{n}\right)+\log f(z \mid \theta)\right\} d \theta / \int \exp \left\{q\left(\theta \mid X_{n}\right)\right\} d \theta
\end{aligned}
$$

where $q\left(\theta \mid X_{n}\right)=\sum \log f\left(X_{\alpha} \mid \theta\right)+\log \pi(\theta)$.
Let $\hat{\theta}_{\pi}$ and $\hat{\theta}_{\pi}(z)$ be the solutions of the equations

$$
\partial\left\{q\left(\theta \mid X_{n}\right)\right\} / \partial \theta=0, \quad \partial\left\{q\left(\theta \mid X_{n}\right)+\log f(z \mid \theta)\right\} / \partial \theta=0
$$

respectively. Then it follows from the expression given by Davison (1986, p. 325) that the Laplace approximation to the predictive density is

$$
h\left(z \mid X_{n}\right)=\left\{\left|J_{q}\right| /\left|J_{q}(z)\right|\right\}^{\frac{1}{2}} \exp \left[q\left\{\hat{\theta}_{\pi}(z) \mid X_{n}\right\}-q\left(\hat{\theta}_{\pi} \mid X_{n}\right)+\log f\left\{z \mid \hat{\theta}_{\pi}(z)\right\}\right]\left\{1+O_{p}\left(n^{-2}\right)\right\}
$$

where

$$
J_{q}=-\partial^{2}\left\{q\left(\theta \mid X_{n}\right)\right\} /\left.\partial \theta \partial \theta^{\prime}\right|_{\hat{\theta}_{x}}, \quad J_{q}(z)=-\partial^{2}\left\{q\left(\theta \mid X_{n}\right)+\log f(z \mid \theta)\right\} /\left.\partial \theta \partial \theta^{\prime}\right|_{\hat{\theta}_{x}(z)} .
$$

Noting that $\hat{\theta}_{\pi}-\hat{\theta}_{\mathrm{ML}}=O_{p}\left(n^{-1}\right)$ and $\hat{\theta}_{\pi}(z)-\hat{\theta}_{\mathrm{ML}}=O_{p}\left(n^{-1}\right)$ for the maximum likelihood estimator $\hat{\theta}_{\text {ML }}$, and using the result $\left|J_{q}\right| /\left|J_{q}(z)\right|=1+O_{p}\left(n^{-1}\right)$ produce the approximation $h\left(z \mid X_{n}\right)=f\left(z \mid \hat{\theta}_{\mathrm{ML}}\right)+O_{p}\left(n^{-1}\right)$.

Hence it follows from Theorem $2 \cdot 2$ that a criterion for the evaluation of the predictive density $h\left(z \mid X_{n}\right)$ is given by

$$
-2 \sum_{\alpha=1}^{n} \log h\left(X_{\alpha} \mid X_{n}\right)+2 \operatorname{tr}\left\{J(\widehat{G})^{-1} I(\widehat{G})\right\}
$$

where $J(G)$ and $I(G)$ are defined by (8) and (9), respectively.

## 4. Numerical approach

## 4•1. General objectives

It may be seen that the bias correction for the log likelihood of a predictive density in the estimation of the expected log likelihood is essential to construct an information criterion. The bootstrap methods (Efron, 1979) offer an alternative approach to estimate the bias of the log likelihood numerically. The use of the bootstrap in a simple situation was introduced by Efron (1986, p. 467). Ishiguro, Sakamoto \& Kitagawa (1996) examined through numerical examples the performance of the bootstrap bias corrected information criterion called eic. This section discusses the use of the bootstrap in statistical model evaluation problems and introduces the variance reduction procedure in bootstrap simulation.

### 4.2. Bootstrap bias estimates

Let $h\left(z \mid X_{n}\right)$ be a model fitted to the data $X_{n}$ drawn from the true distribution $G(x)$. The model $h\left(z \mid X_{n}\right)$ may be constructed in various ways based on the specified parametric family of densities $\{f(x \mid \theta) ; \theta \in \Theta\}$. Conditional on the observed data $X_{n}$, let $X_{n}^{*}$ be the bootstrap sample generated according to the empirical distribution $\hat{G}$ of $X_{n}$. The bootstrap analogue of the expected log likelihood of $h\left(z \mid X_{n}\right)$ defined by (2) is

$$
\eta\left(X_{n}^{*} ; \hat{G}\right):=\int \log h\left(z \mid X_{n}^{*}\right) d \hat{G}(z)=\frac{1}{n} \sum_{\alpha=1}^{n} \log h\left(X_{\alpha} \mid X_{n}^{*}\right) .
$$

By noting that the same sample $X_{n}^{*}$ is used to estimate $\eta\left(X_{n}^{*} ; \hat{G}\right)$, the log likelihood of $h\left(z \mid X_{n}^{*}\right)$ is constructed as

$$
\eta\left(X_{n}^{*} ; \hat{G}^{*}\right):=\int \log h\left(z \mid X_{n}^{*}\right) d \hat{G}^{*}(z)=\frac{1}{n} \sum_{\alpha=1}^{n} \log h\left(X_{\alpha}^{*} \mid X_{n}^{*}\right),
$$

where $\hat{G}^{*}$ is the empirical distribution function of the bootstrap sample $X_{n}^{*}$. Then the bootstrap bias of the log likelihood is given by $\hat{b}_{B}(\hat{G}):=E_{\vec{G}}\left\{\eta\left(X_{n}^{*} ; \hat{G}^{*}\right)-\eta\left(X_{n}^{*} ; \hat{G}\right)\right\}$, the bootstrap estimate of $b(G):=E_{G}\left\{\eta\left(X_{n} ; \widehat{G}\right)-\eta\left(X_{n} ; G\right)\right\}$.

The bias $\hat{b}_{B}(\widehat{G})$ is approximated by averaging $\eta\left(X_{n}^{*} ; \hat{G}^{*}\right)-\eta\left(X_{n}^{*} ; \hat{G}\right)$ over a large number of repeated bootstrap samples. By subtracting the bootstrap bias estimate from the log likelihood, we have

$$
\operatorname{EIC}\left(X_{n} ; \hat{G}\right):=-2 \sum_{\alpha=1}^{n} \log h\left(X_{\alpha} \mid X_{n}\right)+2 n \hat{b}_{B}(\hat{G}) .
$$

Suppose the fitted model may be expressed as $h\left(z \mid X_{n}\right)=f(z \mid \hat{\theta})+O_{p}\left(n^{-1}\right)$, where $\hat{\theta}$ is a

![](https://cdn.mathpix.com/cropped/9878ee9d-119b-4ae7-adaa-805b8142f692-11.jpg?height=1275&width=1480&top_left_y=234&top_left_x=188)
Fig. 2. Comparison of the true bias $n \times b(G)(\cdot \cdot)$, the asymptotic bias $\operatorname{tr}\left\{J(G)^{-1} I(G)\right\}(\cdots-)$ and the bootstrap estimate of the bias $n \times b_{B}(\hat{G})(-)$ with standard errors $(\cdots \cdots)$ for the sample sizes $n=25,100,400$ and 1600.

functional statistic. Then it follows from the expressions (4) and (5) in Theorem $2 \cdot 1$ that the bootstrap bias estimate $n \hat{b}_{B}(\hat{G})$ converges in probability to $b_{1}(G)$ in (4) as $n$ tends to infinity.

Figure 2 shows the bootstrap estimates $(x n)$ of the biases of the log likelihood for the cases given in Fig. 1. In Monte Carlo experiments, 1000 repeated random samples were generated from a mixture of two normal populations in (12) for the sample sizes $n=25$, 100,400 and 1600 , and 1000 bootstrap replications were taken for each trial. From Fig. 2 we see that the means of the bootstrap estimates are close to the true biases $n b(G)$, for large sample sizes. It may be seen from Figs 1 and 2 that the standard deviations of the bootstrap estimates are comparable to those of $\operatorname{tr}\left\{J(\hat{G})^{-1} I(\hat{G})\right\}$ for $n=100$ and 400 , but are larger than those for $n=25$ and 1600. The reason for the increase of variance in large sample case and the reduction of variance in the bootstrap simulation are discussed in §4.3.

### 4.3. Variance reduction in bootstrap simulation

The bootstrap bias estimates are usually approximated by a Monte Carlo simulation. The bias estimates obtained numerically include both the randomness of the observed
data and simulation error which decreases as the number of bootstrap replication increases. It will be shown that the variance associated with a Monte Carlo simulation can be reduced automatically without any analytical argument.

Let $T\left(X_{n} ; G\right)=\eta\left(X_{n} ; \hat{G}\right)-\eta\left(X_{n} ; G\right)$ for the log likelihood of $f(z \mid \hat{\theta})$ in (3) and the expected $\log$ likelihood in (2). Then the bias of the $\log$ likelihood $\eta\left(X_{n} ; \hat{G}\right)$ or equivalently the expectation of $T\left(X_{n} ; G\right)$ may be decomposed into three parts

$$
E_{G}\left\{T\left(X_{n} ; G\right)\right\}=E_{G}\left\{T_{1}\left(X_{n} ; G\right)+T_{2}\left(X_{n} ; G\right)+T_{3}\left(X_{n} ; G\right)\right\},
$$

where

$$
\begin{aligned}
& T_{1}\left(X_{n} ; G\right)=\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}\right)-\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left\{X_{\alpha} \mid T(G)\right\} \\
& T_{2}\left(X_{n} ; G\right)=\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left\{X_{\alpha} \mid T(G)\right\}-\int g(z) \log f\{z \mid T(G)\} d z \\
& T_{3}\left(X_{n} ; G\right)=\int g(z) \log f\{z \mid T(G)\} d z-\int g(z) \log f(z \mid \hat{\theta}) d z
\end{aligned}
$$

We examined the bootstrap estimates of

$$
n E_{G}\left\{T_{1}\left(X_{n} ; G\right)\right\}, \quad n E_{G}\left\{T_{2}\left(X_{n} ; G\right)\right\}, \quad n E_{G}\left\{T_{3}\left(X_{n} ; G\right)\right\}
$$

and their variances in the bootstrap simulation through Monte Carlo experiments. It is assumed that the true distribution and the specified model are both normal, and the model is estimated by the maximum likelihood methods. The simulation results were obtained by averaging over 1000 repeated Monte Carlo trials. For each Monte Carlo trial $B=100$ bootstrap samples are taken and variances are calculated based on 100 bootstrap bias estimates. Table 2 shows the bootstrap estimates and variances for sample sizes $n=25$, 100,400 and 1600 , in which the notation $\mathbf{B T}_{1}, \mathbf{B T}_{2}, \mathbf{B T}_{3}, \mathbf{B T}$ and $\mathbf{B T}_{13}$ refers to the simulation results for $n E_{G}\left\{T_{1}\left(X_{n} ; G\right)\right\}, n E_{G}\left\{T_{2}\left(X_{n} ; G\right)\right\}, n E_{G}\left\{T_{3}\left(X_{n} ; G\right)\right\}, n E_{G}\left\{T\left(X_{n} ; G\right)\right\}$ and $n E_{G}\left\{T_{1}\left(X_{n} ; G\right)+T_{3}\left(X_{n} ; G\right)\right\}$, respectively.

We observe from the experiment that the bootstrap estimate of the second term $\mathbf{B T}_{\mathbf{2}}$ is almost zero and does not affect the estimate of the total expected value in (22) for each case, but its variance is extremely large, especially for $n=400$ or $n=1600$. In contrast the bootstrap estimates $\mathrm{BT}_{1}$ and $\mathrm{BT}_{3}$ have much smaller variances. This clearly shows the reason for the increase of variances of the bootstrap estimates in large sample cases.

The simulation results suggest eliminating the second term $T_{2}\left(X_{n} ; G\right)$ and applying the

Table 2. Simulation results: The bootstrap estimates, bse, and variances, Var, for $\mathbf{B T}_{1}=n E_{G}\left\{T_{1}\left(X_{n} ; G\right)\right\}, \quad \mathbf{B T}_{2}=n E_{G}\left\{T_{2}\left(X_{n} ; G\right)\right\}, \quad \mathbf{B T}_{3}=n E_{G}\left\{T_{3}\left(X_{n} ; G\right)\right\}, \quad \mathbf{B T}= n E_{G}\left\{T\left(X_{n} ; G\right)\right\}$ and $\mathrm{BT}_{13}=n E_{\mathrm{G}}\left\{T_{1}\left(X_{n} ; G\right)+T_{3}\left(X_{n} ; G\right)\right\}$
|  | $n=25$ |  | $n=100$ |  | $n=400$ |  | $n=1600$ |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | BSE | Var | BSE | Var | BSE | Var | BSE | Var |
| $\mathbf{B T}_{\mathbf{1}}$ | 1.230 | 0.036 | 1.041 | 0013 | 1.009 | 0011 | 1.003 | 0010 |
| $\mathrm{BT}_{2}$ | -0-001 | 0.110 | 0-002 | 0480 | 0011 | 1.962 | 0.008 | 7.904 |
| $\mathrm{BT}_{3}$ | 1.002 | 0012 | 0.995 | 0.010 | 0.999 | 0010 | 1.000 | 0.010 |
| BT | 2.232 | 0.242 | 2.038 | 0.564 | 2019 | 2034 | $2 \cdot 010$ | 7.974 |
| $\mathbf{B T}_{\mathbf{1 3}}$ | 2.232 | 0086 | 2.036 | 0.047 | 2.008 | 0.041 | 2.003 | 0040 |


bootstrap to approximate the bias $E_{\mathrm{G}}\left\{T\left(X_{n} ; G\right)\right\}$ in (22). Then the bootstrap estimate of $E_{G}\left\{T_{1}\left(X_{n} ; G\right)+T_{3}\left(X_{n} ; G\right)\right\}$ is the same as that of $E_{\mathrm{G}}\left\{T\left(X_{n} ; G\right)\right\}$, but the variance is much smaller. This implies that, if the bootstrap technique is applied to the modified formula, the number of bootstrap replications may be greatly reduced.

The theoretical justification for use of the simple variance reduction technique mentioned above is as follows. By an argument similar to that in Appendix, $T\left(X_{n} ; G\right)$ in (22) can be expanded as

$$
T\left(X_{n} ; G\right)=\frac{1}{n} \sum_{\alpha=1}^{n} \operatorname{IF}\left(X_{\alpha} ; G\right)+O_{p}\left(\frac{1}{n}\right),
$$

where

$$
\operatorname{IF}\left(X_{\alpha} ; G\right):=\log f\left\{X_{\alpha} \mid T(G)\right\}-\int g(z) \log f\{z \mid T(G)\} d z
$$

the influence function of $T\left(X_{n} ; G\right)$. Noting that $n^{-1} \sum_{\operatorname{IF}}\left(X_{\alpha} ; G\right)=T_{2}\left(X_{n} ; G\right)$ in (23) and $E_{G}\left\{\mathrm{IF}\left(X_{\alpha} ; G\right)\right\}=0$, the bootstrap estimate of the bias (22) can be rewritten as

$$
\begin{aligned}
E_{\hat{G}}\left\{T\left(X_{n}^{*} ; \hat{G}\right)\right\}= & E_{\hat{G}}\left\{T\left(X_{n}^{*} ; \hat{G}\right)-\frac{1}{n} \sum_{\alpha=1}^{n} \operatorname{IF}\left(X_{\alpha}^{*} ; \hat{G}\right)\right\} \\
= & E_{\hat{G}}\left\{\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left(X_{\alpha}^{*} \mid \hat{\theta}^{*}\right)-\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left(X_{\alpha}^{*} \mid \hat{\theta}\right)\right. \\
& \left.+\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}\right)-\frac{1}{n} \sum_{\alpha=1}^{n} \log f\left(X_{\alpha} \mid \hat{\theta}^{*}\right)\right\},
\end{aligned}
$$

where $\hat{\theta}^{*}=T\left(\hat{G}^{*}\right)$ for the empirical distribution function $\hat{G}^{*}$ of $X_{n}^{*}$.
It can be easily shown that the asymptotic conditional variances of

$$
B^{-1} \sum T\left(X_{n}^{*} ; \hat{G}\right), \quad B^{-1} \sum\left\{T\left(X_{n}^{*} ; \hat{G}\right)-n^{-1} \sum \operatorname{If}\left(X_{\alpha}^{*} ; \hat{G}\right)\right\}
$$

are of order $B^{-1} n^{-1}$ and $B^{-1} n^{-2}$, respectively, where $B$ is the number of bootstrap replications. This implies that the use of the decomposition in (24) is superior to the ordinary bootstrap bias estimate in the sense that the simulation error is of smaller order.
The method discussed above is essentially the same as the linear approximation method investigated by Davison, Hinkley \& Schechtman (1986). The advantage in the proposed variance reduction method is that it can be applied automatically in a wide variety of situations without any knowledge of influence functions for estimators, whereas the linear approximation method requires formulae for linear terms.

## 5. Discussion

The main aim of this paper was to provide criteria which enable us to evaluate various types of statistical models. We derived the criteria from the information-theoretic point of view in the context of functional statistics without the assumption that the specified family of probability distributions contains the true structure generating the data. An advantage of the criteria proposed is that they are not restricted to maximum likelihood estimation but may be applied to the evaluation of models constructed by a variety of procedures as discussed in § 3. It might be noted that the existing model evaluation criteria
such as AIC, TIC in (10) and Schwarz's (1978) Bayes information criterion cover only models estimated by the maximum likelihood methods.

The criteria obtained in this paper were constructed by correcting the bias of a log likelihood in the estimation of the expected log likelihood of a fitted density. Ideally we would like to obtain a criterion, ic ( $X_{n} ; \widehat{G}$ ), which satisfies the condition that

$$
E_{G}\left\{\operatorname{IC}\left(X_{n} ; \hat{G}\right)-\eta\left(X_{n} ; G\right)\right\}=O\left(n^{-j}\right)
$$

for larger values of $j$, where $\eta\left(X_{n} ; G\right)$ is the expected log likelihood given by (2). The biascorrected version of the log likelihood is second-order correct or accurate for $\eta\left(X_{n} ; G\right)$ in the sense that the remainder is of order $O\left(n^{-2}\right)$ in the above condition. We obtained a criterion which achieves third-order accuracy in the context of functional statistics. The result is however very lengthy and seems to be of no practical use. By bootstrapping the bias-corrected log likelihood, we may obtain a criterion with third-order accuracy. The large variances of bootstrap estimates should however be examined carefully. Further work remains to be done towards constructing more refined results, especially for small sample sizes.

## Acknowledgement

The authors would like to thank the Editor, Professor Dawid, the Associate Editor and a referee for their helpful comments and suggestions which improved the quality of this paper considerably.

## Appendix

## Derivation of Theorem 2-1

We recall that an estimator $\hat{\theta}=\left(\hat{\theta}_{1}, \ldots, \hat{\theta}_{p}\right)^{\prime}$ is a functional, for which there exists a $p$-dimensional functional $T$ such that $\hat{\theta}=T(\hat{G})=\left(T_{1}(\hat{G}), \ldots, T_{p}(\hat{G})\right)^{\prime}$. Suppose that $T_{i}$ is second-order compact differentiable at $G$ for $i=1, \ldots, p$. Then the functional Taylor series expansion for $\hat{\theta}_{i}=T_{i}(\hat{G})$ is, up to order $n^{-1}$,

$$
\hat{\theta}_{i}=T_{i}(G)+\frac{1}{n} \sum_{\alpha=1}^{n} T^{1)}\left(X_{\alpha} ; G\right)+\frac{1}{n^{2}} \frac{1}{2} \sum_{\alpha=1}^{n} \sum_{\beta=1}^{n} T_{i}^{(2)}\left(X_{\alpha}, X_{\beta} ; G\right)+o_{p}\left(n^{-1}\right),
$$

where $T_{i}^{(\alpha)}$ are defined as symmetric functions such that, for an arbitrary distribution $H$,

$$
\frac{d^{\alpha}}{d \varepsilon^{\alpha}} T_{i}\{(1-\varepsilon) G+\varepsilon H\}=\int \ldots \int T^{(\alpha)}\left(x_{1}, \ldots, x_{\alpha} ; G\right) \prod_{j=1}^{\alpha} d\left\{H\left(x_{j}\right)-G\left(x_{j}\right)\right\}
$$

at $\varepsilon=0$ and

$$
\int T^{(\alpha)}\left(x_{1}, \ldots, x_{a} ; G\right) d G\left(x_{j}\right)=0 \quad(1 \leqslant j \leqslant \alpha) .
$$

Then it may be seen that, as $n \rightarrow+\infty, n^{\frac{1}{2}}\{\hat{\theta}-T(G)\}$ is asymptotically normally distributed with mean vector 0 and covariance matrix $\Sigma=\left(\sigma_{i j}\right)$, where

$$
\sigma_{i j}=\int T_{1}^{11}(z ; G) T_{j}^{(1)}(z ; G) d G(z)
$$

Also it can be readily shown that the asymptotic bias of $\hat{\theta}$ for $T(G)$ is $E_{G}\{\hat{\theta}-T(G)\}=b / n+o\left(n^{-1}\right)$, where $b=\left(b_{1}, \ldots, b_{p}\right)^{\prime}$ with

$$
b_{i}=\frac{1}{2} \int T_{i}^{(2)}(z, z ; G) d G(z)
$$

Expanding $\log f(z \mid \hat{\theta})$ in a Taylor series around $\hat{\theta}=T(G)$ and substituting (A1) in the resulting expansion, we have stochastic expansions for the expected log likelihood $\eta\left(X_{n}, G\right)= \int g(z) \log f(z \mid \hat{\theta}) d z$ and the $\log$ likelihood $\eta\left(X_{n} ; \hat{G}\right)=(1 / n) \sum \log f\left(X_{\alpha} \mid \hat{\theta}\right)$ as follows:

$$
\begin{aligned}
\eta\left(X_{n} ; G\right)= & \int g(z) \log f\{z \mid T(G)\} d z+\left.\frac{1}{n} \sum_{i=1}^{p} \sum_{\alpha=1}^{n} T^{(1)}\left(X_{\alpha} ; G\right) \int g(z) \frac{\partial \log f(z \mid \theta)}{\partial \theta_{i}}\right|_{T(G)} d z \\
& +\frac{1}{2 n^{2}} \sum_{\alpha=1}^{n} \sum_{\beta=1}^{n}\left\{\left.\sum_{i=1}^{p} T^{(2)}\left(X_{\alpha}, X_{\beta} ; G\right) \int g(z) \frac{\partial \log f(z \mid \theta)}{\partial \theta_{i}}\right|_{T(G)} d z\right. \\
& \left.+\left.\sum_{i=1}^{p} \sum_{j=1}^{p} T_{i}^{(1)}\left(X_{\alpha} ; G\right) T_{j}^{(1)}\left(X_{\beta} ; G\right) \int g(z) \frac{\partial^{2} \log f(z \mid \theta)}{\partial \theta_{i} \partial \theta_{j}}\right|_{T(G)} d z\right\}+o_{p}\left(\frac{1}{n}\right) \\
\eta\left(X_{n} ; \hat{G}\right)= & \frac{1}{n} \sum_{\alpha=1}^{n} \log f\left\{X_{\alpha} \mid T(G)\right\}+\left.\frac{1}{n^{2}} \sum_{i=1}^{p} \sum_{\alpha=1}^{n} \sum_{\beta=1}^{n} T_{i}^{(1)}\left(X_{\alpha} ; G\right) \frac{\partial \log f\left(X_{\beta} \mid \theta\right)}{\partial \theta_{i}}\right|_{T(G)} \\
& +\frac{1}{2 n^{3}} \sum_{\alpha=1}^{n} \sum_{\beta=1}^{n} \sum_{\gamma=1}^{n}\left\{\left.\sum_{i=1}^{p} T_{i}^{(2)}\left(X_{\alpha}, X_{\beta} ; G\right) \frac{\partial \log f\left(X_{\gamma} \mid \theta\right)}{\partial \theta_{i}}\right|_{T(G)}\right. \\
& \left.+\left.\sum_{i=1}^{p} \sum_{j=1}^{p} T_{i}^{(1)}\left(X_{\alpha} ; G\right) T_{j}^{(1)}\left(X_{\beta} ; G\right) \frac{\partial^{2} \log f\left(X_{\gamma} \mid \theta\right)}{\partial \theta_{i} \partial \theta_{j}}\right|_{T(G)}\right\}+o_{p}\left(\frac{1}{n}\right)
\end{aligned}
$$

Taking expectations term by term yields

$$
\begin{aligned}
E_{G}\left\{\eta\left(X_{n} ; G\right)\right\}= & \int g(z) \log f\{z \mid T(G)\} d z+\frac{1}{n}\left[b^{\prime} \kappa-\frac{1}{2} \operatorname{tr}\{\Sigma(G) J(G)\}\right]+o\left(\frac{1}{n}\right), \\
E_{G}\left\{\eta\left(X_{n} ; \hat{G}\right)\right\}= & \int g(z) \log f\{z \mid T(G)\} d z+\left.\frac{1}{n}\left[\sum_{i=1}^{p} \int T\right\rangle^{(1)}(z ; G) \frac{\partial \log f(z \mid \theta)}{\partial \theta_{i}}\right|_{T(G)} d G(z) \\
& \left.+b^{\prime} \kappa-\frac{1}{2} \operatorname{tr}\{\Sigma(G) J(G)\}\right]+o\left(\frac{1}{n}\right),
\end{aligned}
$$

where $\kappa$ and $J(G)$ are given by

$$
\kappa=\left.\int \frac{\partial \log f(z \mid \theta)}{\partial \theta}\right|_{T(G)} d G(z), \quad J(G)=-\left.\int \frac{\partial^{2} \log f(z \mid \theta)}{\partial \theta \partial \theta^{\prime}}\right|_{T(G)} d G(z)
$$

This shows immediately that the asymptotic bias of the log likelihood is given by the result (5) in Theorem $2 \cdot 1$. By an argument similar to that discussed above, we have the result given in Theorem 2/2.

We have derived the terms of order $1 / n^{2}$ in (A2) and (A3) under the fourth-order compact differentiability condition on $T$. The results are, however, very lengthy and are omitted. For theoretical work on the functional Taylor series expansion, we refer to von Mises (1947), Withers (1983) and Konishi (1991).

## References

Akaike, H. (1973). Information theory and an extension of the maximum likelihood principle. In 2nd International Symposium on Information Theory, Ed. B. N. Petrov and F. Csaki, pp. 267-81. Budapest: Akademiai Kiado. (Reproduced (1992) in Breakthroughs in Statistics 1, Ed. S. Kotz and N. L. Johnson, pp. 610-24. New York: Springer-Verlag.)
Akaike, H. (1974). A new look at the statistical model identification. IEEE Trans. Auto. Control AC-19, 716-23.
Bozdogan, H. (Ed.) (1994). Proceedings of the First US/Japan Conference on the Frontiers of Statistical Modelling: An Informational Approach. Netherlands: Kluwer Academic.

Davison, A. C. (1986). Approximate predictive likelihood. Biometrika 73, 323-32.
Davison, A. C., Hinkley, D. V. \& Schechtman, E. (1986). Efficient bootstrap simulation. Biometrika 73, 555-66.
Efron, B. (1979). Bootstrap methods: another look at the jackknife. Ann. Statist. 7, 1-26.
Efron, B. (1986). How biased is the apparent error rate of a prediction rule? J. Am. Statist. Assoc. 81, 461-70.
Good, I. J. \& Gaskins, R. A. (1971). Nonparametric roughness penalties for probability densities. Biometrika 58, 255-77.
Green, P. J. (1987). Penalized likelihood for general semi-parametric regression models. Int. Statist. Rev. 55, 245-59.
Hampel, F. R., Ronchetti, E. M., Rousseeuw, P. J. \& Stahel, W. A. (1986). Robust Statistics. The Approach Based on Influence Functions. New York: Wiley.
Huber, P. J. (1981). Robust Statistics. New York: Wiley.
Hurvich, C. M. \& Tsai, C.-L. (1991). Bias of the corrected aic criterion for underfitted regression and time series models. Biometrika 78, 499-509.
Ishiguro, M., Sakamoto, Y. \& Kitagawa, G. (1996). Bootstrapping log-likelihood and eic, an extension of aic. Ann. Inst. Statist. Math. To appear.
Kitagawa, G. (1987). Non-Gaussian state-space modeling of nonstationary time series (with Discussion). J. Am. Statist. Assoc. 82, 1032-63.

Konishi, S. (1991). Normalizing transformations and bootstrap confidence intervals. Ann. Statist. 19, 2209-25.
Kullback, S. \& Leibler, R. A. (1951). On information and sufficiency. Ann. Math. Statist. 22, 79-86.
Mallows, C. L. (1973). Some comments on $C_{p}$. Technometrics 15, 661-75.
Ronchetti, E. (1985). Robust model selection in regression. Statist. Prob. Lett. 3, 21-3.
Ronchetti, E. \& Staudte, R. G. (1994). A robust version of Mallows's $C_{p}$. J. Am. Statist. Assoc. 89, 550-9.
Sakamoto, Y., Ishiguro, M. \& Kitagawa, G. (1986). Akaike Information Criterion Statistics. Tokyo: D. Reidel.
Schwarz, G. (1978). Estimating the dimension of a model. Ann. Statist. 6, 461-4.
Shirata, R. (1989). Statistical aspects of model selection. In From Data to Model, Ed. J. C. Willems, pp. 215-40. New York: Springer-Verlag.
Stone, M. (1977). An asymptotic equivalence of choice of model by cross-validation and Akaike's criterion. J. R. Statist. Soc. B 39, 44-7.

Sugiura, N. (1978). Further analysis of the data by Akaike's information criterion and the finite corrections. Commun. Statist. A 7, 13-26.
Takeuchi, K. (1976). Distribution of information statistics and criteria for adequacy of models. Mathematical Sciences, No. 153, pp. 12-8 (in Japanese).
Tierney, L. \& Kadane, J. B. (1986). Accurate approximations for posterior moments and marginal densities. J. Am. Statist. Assoc. 81, 82-6.
von Mises, R. (1947). On the asymptotic distribution of differentiable statistical functions. Ann. Math. Statist. 18, 309-48.
Withers, C. S. (1983). Expansions for the distribution and quantiles of a regular functional of the empirical distribution with applications to nonparametric confidence intervals. Ann. Statist. 11, 577-87.
[Received July 1995. Revised March 1996]

