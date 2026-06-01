---
citekey: shimodairahidetoshiImprovingPredictiveInference2000
item_type: article
authors: 'Shimodaira, Hidetoshi'
year: 2000
title: Improving Predictive Inference under Covariate Shift by Weighting the Log-Likelihood Function
venue: Journal of Statistical Planning and Inference
volume: 90
issue: 2
pages: 227--244
doi: 10.1016/s0378-3758(00)00115-4
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\shimodaira_improving_predictive_inference_2000.pdf'
pdf_sha256: 5ae4df2da9b40a3239c7abb4bb4f321985680c7a4a6bf5a8b6472853f01c36e9
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T13:50:44Z
---
# Improving predictive inference under covariate shift by weighting the log-likelihood function 

Hidetoshi Shimodaira*<br>The Institute of Statistical Mathematics, 4-6-7 Minami-Azabu, Minato-ku, Tokyo 106-8569, Japan

Received 17 December 1998; received in revised form 21 January; accepted 25 February 2000


#### Abstract

A class of predictive densities is derived by weighting the observed samples in maximizing the log-likelihood function. This approach is effective in cases such as sample surveys or design of experiments, where the observed covariate follows a different distribution than that in the whole population. Under misspecification of the parametric model, the optimal choice of the weight function is asymptotically shown to be the ratio of the density function of the covariate in the population to that in the observations. This is the pseudo-maximum likelihood estimation of sample surveys. The optimality is defined by the expected Kullback-Leibler loss, and the optimal weight is obtained by considering the importance sampling identity. Under correct specification of the model, however, the ordinary maximum likelihood estimate (i.e. the uniform weight) is shown to be optimal asymptotically. For moderate sample size, the situation is in between the two extreme cases, and the weight function is selected by minimizing a variant of the information criterion derived as an estimate of the expected loss. The method is also applied to a weighted version of the Bayesian predictive density. Numerical examples as well as Monte-Carlo simulations are shown for polynomial regression. A connection with the robust parametric estimation is discussed. (c) 2000 Elsevier Science B.V. All rights reserved.


MSC: 62B10; 62D05
Keywords: Akaike information criterion; Design of experiments; Importance sampling;
Kullback-Leibler divergence; Misspecification; Sample surveys; Weighted least squares

## 1. Introduction

Let $x$ be the explanatory variable or the covariate, and $y$ be the response variable. In predictive inference with the regression analysis, we are interested in estimating the conditional density $q(y \mid x)$ of $y$ given $x$, using a parametric model. Let $p(y \mid x, \theta)$ be the model of the conditional density which is parameterized by $\theta=\left(\theta^{1}, \ldots, \theta^{m}\right)^{\prime} \in \Theta \subset \mathscr{R}^{m}$.

[^0]Having observed i.i.d. samples of size $n$, denoted by $\left(x^{(n)}, y^{(n)}\right)=\left(\left(x_{t}, y_{t}\right): t=1, \ldots, n\right)$, we obtain a predictive density $p(y \mid x, \hat{\theta})$ by giving an estimate $\hat{\theta}=\hat{\theta}\left(x^{(n)}, y^{(n)}\right)$. In this paper, we discuss improvement of the maximum likelihood estimate (MLE) under both (i) covariate shift in distribution and (ii) misspecification of the model as explained below.

Let $q_{1}(x)$ be the density of $x$ for evaluation of the predictive performance, while $q_{0}(x)$ be the density of $x$ in the observed data. We consider the Kullback-Leibler loss function

$$
\operatorname{loss}_{i}(\theta):=-\int q_{i}(x) \int q(y \mid x) \log p(y \mid x, \theta) \mathrm{d} y \mathrm{~d} x
$$

for $i=0,1$, and then employ $\operatorname{loss}_{1}(\hat{\theta})$ for evaluation of $\hat{\theta}$, rather than the usual $\operatorname{loss}_{0}(\hat{\theta})$. The situation $q_{0}(x) \neq q_{1}(x)$ will be called covariate shift in distribution, which is one of the premises of this paper.

This situation is not so odd as it might look at first. In fact, it is seen in various fields as follows. In sample surveys, $q_{0}(x)$ is determined by the sampling scheme, while $q_{1}(x)$ is determined by the population. In regression analysis, covariate shift often happens because of the limitation of resources, or the design of experiments. In artificial neural networks literature, "active learning" is the typical situation where we control $q_{0}(x)$ for better prediction. We could say that the distribution of $x$ in future observations is different from that of the past observations; $x$ is not necessarily distributed as $q_{1}(x)$ in future, but we can give imaginary $q_{1}(x)$ to specify the region of $x$ where the prediction accuracy should be controlled. Note that $q_{0}(x)$ and/or $q_{1}(x)$ are often estimated from data, but we assume they are known or estimated reasonably in advance.

The second premise of this paper is misspecification of the model. Let $\hat{\theta}_{0}$ be the MLE of $\theta$, and $\theta_{0}^{*}$ be the asymptotic limit of $\hat{\theta}_{0}$ as $n \rightarrow \infty$. Under certain regularity conditions, MLE is consistent and $p\left(y \mid x, \theta_{0}^{*}\right)=q(y \mid x)$ provided that the model is correctly specified. In practice, however, $p\left(y \mid x, \theta_{0}^{*}\right)$ deviates more or less from $q(y \mid x)$.

Under both the covariate shift and the misspecification, MLE does not necessarily provide a good inference. We will show that MLE is improved by giving a weight function $w(x)$ of the covariate in the log-likelihood function

$$
L_{w}\left(\theta \mid x^{(n)}, y^{(n)}\right):=-\sum_{t=1}^{n} l_{w}\left(x_{t}, y_{t} \mid \theta\right),
$$

where $l_{w}(x, y \mid \theta)=-w(x) \log p(y \mid x, \theta)$. Then the maximum weighted log-likelihood estimate (MWLE), denoted by $\hat{\theta}_{w}$, is obtained by maximizing (1.1) over $\Theta$. It will be seen that the weight function $w(x)=q_{1}(x) / q_{0}(x)$ is the optimal choice for sufficiently large $n$ in terms of the expected loss with respect to $q_{1}(x)$. We denote MWLE with this weight function by $\hat{\theta}_{1}$. A comparison between $\hat{\theta}_{0}$ and $\hat{\theta}_{1}$ is made in the numerical example of polynomial regression of Section 2, and the asymptotic optimality of $\hat{\theta}_{1}$ is shown in Section 3. Note that MWLE turns out to be downweighting the observed samples which are not important in fitting the model with respect to the population. An interpretation of MWLE as one of the robust estimation techniques is given in Section 9.

This type of estimation is not new in statistics. Actually, $\hat{\theta}_{1}$ is regarded as a generalization of the pseudo-maximum likelihood estimation in sample surveys (Skinner et al., 1989, p. 80; Pfeffermann et al., 1998); the log likelihood is weighted inversely proportional to $q_{0}(x)$, the probability of selecting unit $x$, while $q_{1}(x)$ is equal probability for all possible values of $x$. The same idea is also seen in Rao (1991), where weighted maximum likelihood estimation is considered for unequally spaced time-series data.

The local likelihoods or the weighted likelihoods formally similar to (1.1) are found in the literature for semi-parametric inference. However, $\hat{\theta}_{w}$ is estimated using a weight function concentrated locally around each $x$ or $(x, y)$ in the semi-parametric approach; thus $\hat{\theta}_{w}$ in $p\left(y \mid x, \hat{\theta}_{w}\right)$ will depend on $(x, y)$ as well as the data $\left(x^{(n)}, y^{(n)}\right)$. On the other hand, we restrict our attention to a rather conventional parametric modeling approach here, and $\hat{\theta}_{w}$ depends only on the data.

In spite of the asymptotic optimality of $w(x)=q_{1}(x) / q_{0}(x)$ mentioned above, another choice of the weight function can improve the expected loss for moderate sample size by compromising the bias and the variance of $\hat{\theta}_{w}$. We develop a practical method for this improvement in Section 4-7. The asymptotic expansion of the expected loss is given in Section 4, and a variant of the information criterion is derived as an estimate of the expected loss in Section 5. This new criterion is used to find a good $w(x)$ as well as a good form of $p(y \mid x, \theta)$. The numerical example is revisited in Section 6, and a simulation study is given in Section 7.

In Section 8, we show the Bayesian predictive density is also improved by considering the weight function. Finally, concluding remarks are given in Section 9. All the proofs are deferred to the appendix.

## 2. Illustrative example in regression

Here we consider the normal regression to predict the response $y \in \mathscr{R}$ using a polynomial function of $x \in \mathscr{R}$. Let the model $p(y \mid x, \theta)$ be the polynomial regression

$$
y=\beta_{0}+\beta_{1} x+\cdots+\beta_{d} x^{d}+\varepsilon, \quad \varepsilon \sim \mathrm{N}\left(0, \sigma^{2}\right),
$$

where $\theta=\left(\beta_{0}, \ldots, \beta_{d}, \sigma\right)$ and $\mathrm{N}(a, b)$ denotes the normal distribution with mean $a$ and variance $b$. In the numerical example below, we assume the true $q(y \mid x)$ is also given by (2.1) with $d=3$ :

$$
y=-x+x^{3}+\varepsilon, \quad \varepsilon \sim \mathrm{N}\left(0,0.3^{2}\right) .
$$

The density $q_{0}(x)$ of the covariate $x$ is

$$
x \sim \mathrm{~N}\left(\mu_{0}, \tau_{0}^{2}\right)
$$

where $\mu_{0}=0.5, \tau_{0}^{2}=0.5^{2}$. This corresponds to the sampling scheme of $x$ or the design of experiments. A dataset $\left(x^{(n)}, y^{(n)}\right)$ of size $n=100$ is generated from (2.2) and (2.3), and plotted by circles in Fig. 1a. MLE $\hat{\theta}_{0}$ is obtained by the ordinary least squares (OLS) for the normal regression; we consider a model of the form (2.1) with $d=1$, and the regression line fitted by OLS is drawn in solid line in Fig. 1a.

![](https://cdn.mathpix.com/cropped/9d044cef-46c9-4817-b90e-7c28eee2c697-04.jpg?height=633&width=1265&top_left_y=159&top_left_x=78)
Fig. 1. Fitting of polynomial regression with degree $d=1$. (a) Samples $\left(x_{t}, y_{t}\right)$ of size $n=100$ are generated from $q(y \mid x) q_{0}(x)$ and plotted as circles, where the underlying true curve is indicated by the thin dotted line. The solid line is obtained by OLS, and the dotted line is WLS with weight $q_{1}(x) / q_{0}(x)$. (b) Samples of $n=100$ are generated from $q(y \mid x) q_{1}(x)$, and the regression line is obtained by OLS.

On the other hand, MWLE $\hat{\theta}_{w}$ is obtained by weighted least squares (WLS) with weights $w\left(x_{t}\right)$ for the normal regression. We again consider the model with $d=1$, and the regression line fitted by WLS with $w(x)=q_{1}(x) / q_{0}(x)$ is drawn in dotted line in Fig. 1a. Here, the density $q_{1}(x)$ for imaginary "future" observations or that for the whole population in sample surveys is specified in advance by

$$
x \sim \mathrm{~N}\left(\mu_{1}, \tau_{1}^{2}\right),
$$

where $\mu_{1}=0.0, \tau_{1}^{2}=0.3^{2}$. The ratio of $q_{1}(x)$ to $q_{0}(x)$ is

$$
\frac{q_{1}(x)}{q_{0}(x)}=\frac{\exp \left(-\left(x-\mu_{1}\right)^{2} / 2 \tau_{1}^{2}\right) / \tau_{1}}{\exp \left(-\left(x-\mu_{0}\right)^{2} / 2 \tau_{0}^{2}\right) / \tau_{0}} \propto \exp \left(-\frac{(x-\bar{\mu})^{2}}{2 \bar{\tau}^{2}}\right),
$$

where $\bar{\tau}^{2}=\left(\tau_{1}^{-2}-\tau_{0}^{-2}\right)^{-1}=0.38^{2}$, and $\bar{\mu}=\bar{\tau}^{2}\left(\tau_{1}^{-2} \mu_{1}-\tau_{0}^{-2} \mu_{0}\right)=-0.28$.
The obtained lines in Fig. 1a are very different for OLS and WLS. The question is: which is better than the other? It is known that OLS is the best linear unbiased estimate and makes small mean squared error of prediction in terms of $q(y \mid x) q_{0}(x)$ which generated the data. On the other hand, WLS with weight (2.5) makes small prediction error in terms of $q(y \mid x) q_{1}(x)$ which will generate future observations, and thus WLS is better than OLS here. To confirm this, a dataset of size $n=100$ is generated from $q(y \mid x) q_{1}(x)$ specified by (2.2) and (2.4). The regression line of $d=1$ fitted by OLS is shown in Fig. 1b, which is considered to have small prediction error for the "future" data. The regression line of WLS fitted to the past data in Fig. 1a is quite similar to the line of OLS fitted to the future data in Fig. 1b. In practice, only the past data is available. The WLS gave almost the equivalent result to the future OLS by using only the past data.

The underlying true curve is the polynomial with $d=3$, and thus the regression line of $d=1$ cannot be fitted to it nicely over all the region of $x$. However, the true curve is almost linear in the region of $\mu_{1} \pm 2 \tau_{1}$, and the nice fit of the WLS in this region is obtained by throwing away the observed samples which are outside of this region. The "effective sample size" may be defined in terms of the entropy by $n_{\mathrm{e}}=\exp \left(-\sum_{t=1}^{n} p_{t} \log p_{t}\right)$, where $p_{t}=w\left(x_{t}\right) / \sum_{t^{\prime}=1}^{n} w\left(x_{t^{\prime}}\right)$. In the WLS above, $n_{\mathrm{e}}=49.3$, which is about the half of the original sample size $n=100$, and then increases the variance of the WLS. This is discussed later in detail.

## 3. Asymptotic properties of MWLE

Let $E_{i}(\cdot)$ denote the expectation with respect to $q(y \mid x) q_{i}(x)$ for $i=0,1$. Considering $-L_{w}(\theta)$ as the summation of i.i.d. random variables $l_{w}\left(x_{t}, y_{t} \mid \theta\right)$, it follows from the law of large numbers that $-L_{w}(\theta) / n \rightarrow E_{0}\left(l_{w}(x, y \mid \theta)\right)$ as $n$ grows to infinity. Then we have $\hat{\theta}_{w} \rightarrow \theta_{w}^{*}$ in probability as $n \rightarrow \infty$, where $\theta_{w}^{*}$ is the minimizer of $E_{0}\left(l_{w}(x, y \mid \theta)\right)$ over $\theta \in \Theta$. Hereafter, we restrict our attention to proper $w(x)$ such that $E_{0}\left(l_{w}(x, y \mid \theta)\right)$ exists for all $\theta \in \Theta$ and that the Hessian of $E_{0}\left(l_{w}(x, y \mid \theta)\right)$ is non-singular at $\theta_{w}^{*}$, which is uniquely determined and interior to $\Theta$.

If the above result is applied to $w(x)=q_{1}(x) / q_{0}(x)$, we find that $\hat{\theta}_{1}$ converges in probability to the minimizer of $\operatorname{loss}_{1}(\theta)$ over $\theta \in \Theta$, which we denote $\theta_{1}^{*}$. Here the key idea is the importance sampling identity:

$$
\begin{aligned}
E_{0}\left\{\frac{q_{1}(x)}{q_{0}(x)} \log p(y \mid x, \theta)\right\} & =\int q(y \mid x) q_{0}(x) \frac{q_{1}(x)}{q_{0}(x)} \log p(y \mid x, \theta) \mathrm{d} x \mathrm{~d} y \\
& =E_{1}(\log p(y \mid x, \theta))
\end{aligned}
$$

which implies $E_{0}\left(l_{w}(x, y \mid \theta)\right) \equiv \operatorname{loss}_{1}(\theta)$ and $\theta_{w}^{*}=\theta_{1}^{*}$ when $w(x)=q_{1}(x) / q_{0}(x)$.
Except for the equivalent weight $w(x) \propto q_{1}(x) / q_{0}(x)$, we have $\theta_{w}^{*} \neq \theta_{1}^{*}$ under misspecification in general. From the definition of $\theta_{1}^{*}$, therefore, $\operatorname{loss}_{1}\left(\theta_{w}^{*}\right)>\operatorname{loss}_{1}\left(\theta_{1}^{*}\right)$. This immediately implies the asymptotic optimality of the weight $w(x)=q_{1}(x) / q_{0}(x)$, because $\hat{\theta}_{w} \rightarrow \theta_{w}^{*}$ and $\hat{\theta}_{1} \rightarrow \theta_{1}^{*}$ and thus $\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)>\operatorname{loss}_{1}\left(\hat{\theta}_{1}\right)$ for sufficiently large $n$.
$\hat{\theta}_{1}$ has consistency in a sense that it converges to the optimal parameter value. However, $\hat{\theta}_{0}$ is more efficient than $\hat{\theta}_{1}$ in terms of the asymptotic variance. This will be important for moderate sample size, where $n$ is large enough for the asymptotic expansions to be allowed, but not enough for the optimality of $\hat{\theta}_{1}$ to hold. The following lemma, which is used in the subsequent sections, gives the asymptotic distribution of $\hat{\theta}_{w}$. The derivation is parallel to that of MLE under misspecification given in White (1982); we replace $\log p(y \mid x, \theta) q_{0}(x)$ of MLE with $w(x) \log p(y \mid x, \theta) q_{0}(x)$ of MWLE.

Lemma 1. Assume the regularity conditions similar to those of White (1982), i.e., the model is sufficiently smooth and the support of $p(y \mid x, \theta)$ is the same as that of $q(y \mid x)$ for all $\theta \in \Theta$. Also assume $\theta_{w}^{*}$ is an interior point of $\Theta$. Then, $n^{1 / 2}\left(\hat{\theta}_{w}-\theta_{w}^{*}\right)$
is asymptotically normally distributed as $\mathrm{N}\left(0, H_{w}^{-1} G_{w} H_{w}^{-1}\right)$, where $G_{w}$ and $H_{w}$ are $m \times m$ matrices defined by

$$
G_{w}=E_{0}\left\{\left.\left.\frac{\partial l_{w}(x, y \mid \theta)}{\partial \theta}\right|_{\theta_{w}^{*}} \frac{\partial l_{w}(x, y \mid \theta)}{\partial \theta^{\prime}}\right|_{\theta_{w}^{*}}\right\}, \quad H_{w}=E_{0}\left\{\left.\frac{\partial^{2} l_{w}(x, y \mid \theta)}{\partial \theta \partial \theta^{\prime}}\right|_{\theta_{w}^{*}}\right\},
$$

which are assumed to be non-singular.

## 4. Expected loss

In the previous section, optimal choice of $w(x)$ was discussed in terms of the asymptotic bias $\theta_{w}^{*}-\theta_{1}^{*}$. For moderate sample size, however, the variance of $\hat{\theta}_{w}$ due to the sampling error should be considered. In order to take account of both the bias and the variance, we employ the expected loss $E_{0}^{(n)}\left(\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)\right)$ to determine the optimal weight; $E_{0}^{(n)}(\cdot)$ denotes the expectation with respect to $\left(x^{(n)}, y^{(n)}\right)$ which follows $\prod_{t=1}^{n} q\left(y_{t} \mid x_{t}\right) q_{0}\left(x_{t}\right)$.

Lemma 2. The expected loss is asymptotically expanded as

$$
E_{0}^{(n)}\left(\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)\right)=\operatorname{loss}_{1}\left(\theta_{w}^{*}\right)+\frac{1}{n}\left\{K_{w}^{[1] \prime} b_{w}+\frac{1}{2} \operatorname{tr}\left(K_{w}^{[2]} H_{w}^{-1} G_{w} H_{w}^{-1}\right)\right\}+\mathrm{o}\left(n^{-1}\right)
$$

where the elements of $K_{w}^{[1]}$ and $K_{w}^{[2]}$ are defined by

$$
\left(K_{w}^{[k]}\right)_{i_{1} \cdots i_{k}}=-E_{0}\left\{\left.\frac{q_{1}(x)}{q_{0}(x)} \frac{\partial^{k} \log p(y \mid x, \theta)}{\partial \theta^{i_{1}} \cdots \partial \theta^{i_{k}}}\right|_{\theta_{w}^{*}}\right\}
$$

and $b_{w}$ is the asymptotic limit of $n E_{0}^{(n)}\left(\hat{\theta}_{w}-\theta_{w}^{*}\right)$, which is of order $\mathrm{O}(1)$.
The expression for $b_{w}$ is given in the following lemma. We use the summation convention $A_{i} B^{i}=\sum_{i=1}^{m} A_{i} B^{i}$ in the formula.

Lemma 3. The elements of $b_{w}=\lim _{n \rightarrow \infty} n E_{0}^{(n)}\left(\hat{\theta}_{w}-\theta_{w}^{*}\right)$ are given by

$$
b_{w}^{i_{1}}:=H_{w}^{i_{1} i_{2}} H_{w}^{j_{1} j_{2}}\left\{\left(H_{w}^{[2 \cdot 1]}\right)_{i_{2} j_{1} \cdot j_{2}}-\frac{1}{2}\left(H_{w}^{[3]}\right)_{i_{2} j_{1} k_{1}} H_{w}^{k_{1} k_{2}}\left(H_{w}^{[1 \cdot 1]}\right)_{k_{2} \cdot j_{2}}\right\},
$$

where $H_{w}^{i j}$ denotes the $(i, j)$ element of $H_{w}^{-1}$, and

$$
\begin{aligned}
& \left(H_{w}^{[k]}\right)_{i_{1} \cdots i_{k}}=E_{0}\left\{\left.\frac{\partial^{k} l_{w}(x, y \mid \theta)}{\partial \theta^{i_{1}} \cdots \partial \theta^{i_{k}}}\right|_{\theta_{w}^{*}}\right\}, \\
& \left(H_{w}^{[k \cdot l]}\right)_{i_{1} \cdots i_{k} \cdot j_{1} \cdots j_{l}}=E_{0}\left\{\left.\left.\frac{\partial^{k} l_{w}(x, y \mid \theta)}{\partial \theta^{i_{1}} \cdots \partial \theta^{i_{k}}}\right|_{\theta_{w}^{*}} \frac{\partial^{l} l_{w}(x, y \mid \theta)}{\partial \theta^{j_{1}} \cdots \partial \theta^{j_{l}}}\right|_{\theta_{w}^{*}}\right\} .
\end{aligned}
$$

Note that the matrices defined in (3.2) are written as $G_{w}=H_{w}^{[1 \cdot 1]}$ and $H_{w}=H_{w}^{[2]}$.

For sufficiently large $n, \operatorname{loss}_{1}\left(\theta_{w}^{*}\right)$ is the dominant term on the right-hand side of (4.1), and the optimal weight is $w(x)=q_{1}(x) / q_{0}(x)$ as seen in Section 3. If $n$ is not large enough compared with the extent of the misspecification, the $\mathrm{O}\left(n^{-1}\right)$ terms related to the first and second moments of $\hat{\theta}_{w}-\theta_{w}^{*}$ cannot be ignored in (4.1), and the optimal weight changes. In an extreme case where the model is correctly specified, we only have to look at the $\mathrm{O}\left(n^{-1}\right)$ terms as shown in the following lemma.

Lemma 4. Assume there exists $\theta^{*} \in \Theta$ such that $q(y \mid x)=p\left(y \mid x, \theta^{*}\right)$. Then, $\theta_{w}^{*}=\theta^{*}$ and $q(y \mid x)=p\left(y \mid x, \theta_{w}^{*}\right)$ for all proper $w(x)$. The expected loss $E_{0}^{(n)}\left(\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)\right)$ is minimized when $w(x) \equiv 1$ for sufficiently large $n$.

## 5. Information criterion

The performance of MWLE for a specified $w(x)$ is given by (4.1). However, we cannot calculate the value of the expected loss from it in practice, because $q(y \mid x)$ is unknown. We provide a variant of the information criterion as an estimate of (4.1).

Theorem 1. Let the information criterion for $M W L E$ be

$$
\mathrm{IC}_{w}:=-2 L_{1}\left(\hat{\theta}_{w}\right)+2 \operatorname{tr}\left(J_{w} H_{w}^{-1}\right)
$$

where

$$
\begin{aligned}
& L_{1}(\theta)=\sum_{t=1}^{n} \frac{q_{1}(x)}{q_{0}(x)} \log p\left(y_{t} \mid x_{t}, \theta\right) \\
& J_{w}=-E_{0}\left\{\left.\left.\frac{q_{1}(x)}{q_{0}(x)} \frac{\partial \log p(y \mid x, \theta)}{\partial \theta}\right|_{\theta_{w}^{*}} \frac{\partial l_{w}(x, y \mid \theta)}{\partial \theta^{\prime}}\right|_{\theta_{w}^{*}}\right\} .
\end{aligned}
$$

The matrices $J_{w}$ and $H_{w}$ may be replaced by their consistent estimates

$$
\begin{aligned}
& \hat{J}_{w}=-\left.\left.\frac{1}{n} \sum_{t=1}^{n} \frac{q_{1}\left(x_{t}\right)}{q_{0}\left(x_{t}\right)} \frac{\partial \log p\left(y_{t} \mid x_{t}, \theta\right)}{\partial \theta}\right|_{\hat{\theta}_{w}} \frac{\partial l_{w}\left(x_{t}, y_{t} \mid \theta\right)}{\partial \theta^{\prime}}\right|_{\hat{\theta}_{w}}, \\
& \hat{H}_{w}=\left.\frac{1}{n} \sum_{t=1}^{n} \frac{\partial^{2} l_{w}\left(x_{t}, y_{t} \mid \theta\right)}{\partial \theta \partial \theta^{\prime}}\right|_{\hat{\theta}_{w}} .
\end{aligned}
$$

Then, $\mathrm{IC}_{w} / 2 n$ is an estimate of the expected loss unbiased up to $\mathrm{O}\left(n^{-1}\right)$ term:

$$
E_{0}^{(n)}\left(\mathrm{IC}_{w} / 2 n\right)=E_{0}^{(n)}\left(\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)\right)+\mathrm{o}\left(n^{-1}\right)
$$

Fortunately, expression (5.1) turns out to be rather simpler than that of (4.1), and we do not have to worry about the calculation of the third derivatives appeared in (4.2). The explicit form of (5.1) for the normal regression is given in (6.1) and (6.2).

Given the model $p(y \mid x, \theta)$ and the data $\left(x^{(n)}, y^{(n)}\right)$, we choose a weight function $w(x)$ which attains the minimum of $\mathrm{IC}_{w}$ over a certain class of weights. This is selection of the weight rather than model selection. Searching the optimal weight over all the
possible forms of $w(x)$ is equivalent to $n$-dimensional optimization problem with respect to $\left(w\left(x_{t}\right): t=1, \ldots, n\right)$. But we do not take this line here, because of the computational cost as well as a conceptual difficulty which will be mentioned in Section 9. Rather than the global search, we shall pick a better one from the two extreme cases of $w(x) \equiv 1$ and $w(x)=q_{1}(x) / q_{0}(x)$, or consider a class of weights by connecting the two extremes continuously:

$$
w(x)=\left(\frac{q_{1}(x)}{q_{0}(x)}\right)^{\lambda}, \quad \lambda \in[0,1]
$$

where $\lambda=0$ corresponds to $\hat{\theta}_{0}$ and $\lambda=1$ corresponds to $\hat{\theta}_{1}$. In the next section, we numerically find $\hat{\lambda}$ which minimizes $\mathrm{IC}_{w}$ by searching over $\lambda \in[0,1]$. Note that (5.3) is proportional to $\mathrm{N}\left(\bar{\mu}, \bar{\tau}^{2} / \lambda\right)$ in the case of (2.5), and $\lambda^{-1 / 2}$ is the window scale parameter.

When we have several candidate forms of $p(y \mid x, \theta)$, the model and the weight are selected simultaneously by minimizing $\mathrm{IC}_{w}$. A similar idea of the simultaneous selection is found in Shibata (1989), where an information criterion RIC is derived for the penalized likelihood. A crucial distinction, however, is that the weight for $\theta$ is selected in RIC, whereas the weight for $x$ is selected in $\mathrm{IC}_{w}$. Another distinction is that the weight is additive to the log likelihood in RIC, while it is multiplicative in IC ${ }_{w}$.

Akaike (1974) gave an information criterion

$$
\mathrm{AIC}=-2 L_{0}\left(\hat{\theta}_{0}\right)+2 \operatorname{dim} \theta,
$$

where $L_{0}(\theta)$ is the log-likelihood function. AIC is intended for MLE, and it is obtained as a special case of $\mathrm{IC}_{w}$. When $q_{1}(x)=q_{0}(x)$ and $w(x) \equiv 1, \mathrm{IC}_{w}$ reduces to

$$
\mathrm{TIC}=-2 L_{0}\left(\hat{\theta}_{0}\right)+2 \operatorname{tr}\left(G_{0} H_{0}^{-1}\right),
$$

where $G_{0}=G_{w}$ and $H_{0}=H_{w}$ when $w(x) \equiv 1$. TIC is derived by Takeuchi (1976) as a precise version of AIC, and it is equivalent to the criterion of Linhart and Zucchini (1986). If $p\left(y \mid x, \theta_{0}^{*}\right)$ is sufficiently close to $q(y \mid x), \operatorname{tr}\left(G_{0} H_{0}^{-1}\right) \approx \operatorname{dim} \theta$ and TIC reduces to AIC.

## 6. Numerical example revisited

For the normal linear regression, such as the polynomial regression given in (2.1), $\beta$-components of $\hat{\theta}_{w}$ are obtained by WLS with weights $w\left(x_{t}\right)$. $\sigma$-component of $\hat{\theta}_{w}$ is then given by $\hat{\sigma}^{2}=\sum_{t=1}^{n} w\left(x_{t}\right) \hat{\varepsilon}_{t}^{2} / \hat{c}_{w}$, where $\hat{c}_{w}=\sum_{t=1}^{n} w\left(x_{t}\right)$ and $\hat{\varepsilon}_{t}$ is the residual. Letting $\hat{h}_{t}, t=1, \ldots, n$ be the diagonal elements of the hat matrix used in the WLS, the information criterion (5.1) is calculated from

$$
-L_{1}\left(\hat{\theta}_{w}\right)=\frac{1}{2} \sum_{t=1}^{n} \frac{q_{1}\left(x_{t}\right)}{q_{0}\left(x_{t}\right)}\left\{\frac{\hat{\varepsilon}_{t}^{2}}{\hat{\sigma}^{2}}+\log \left(2 \pi \hat{\sigma}^{2}\right)\right\},
$$

![](https://cdn.mathpix.com/cropped/9d044cef-46c9-4817-b90e-7c28eee2c697-09.jpg?height=614&width=1276&top_left_y=171&top_left_x=73)
Fig. 2. (a) Curve of $\mathrm{IC}_{w}$ versus $\lambda \in[0,1]$ for the model of Section 2 with $d=2$. The weight function (5.3) connecting from $w(x) \equiv 1$ (i.e. $\lambda=0$ ) to $w(x)=q_{1}(x) / q_{0}(x)$ (i.e. $\lambda=1$ ) was used. Also shown are $-2 L_{1}\left(\hat{\theta}_{w}\right)$ in dotted lines, and $2 \operatorname{tr}\left(J_{w} H_{w}^{-1}\right)$ in broken lines. (b) The regression curves for $d=2$. The WLS curve with the optimal $\hat{\lambda}$ as well as those for OLS $(\lambda=0)$ and WLS $(\lambda=1)$ are drawn.

Table 1
$\mathrm{IC}_{w}$ values with weight (5.3) for $\lambda=0, \lambda=1$, and $\lambda=\hat{\lambda}$. Also shown is $\hat{\lambda}$ value. Calculated for the polynomial regression example of Section 2 with $d=0, \ldots, 4$
|  | $d=0$ | $d=1$ | $d=2$ | $d=3$ | $d=4$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\lambda=0$ | 138.72 | 174.02 | 63.59 | 28.97 | 31.75 |
| $\lambda=1$ | 73.96 | 33.23 | 33.64 | 34.80 | 34.98 |
| $\lambda=\hat{\lambda}$ | 73.92 | 32.68 | 32.62 | 28.96 | 31.75 |
| $\hat{\lambda}$ | 0.95 | 0.77 | 0.56 | 0.01 | 0.00 |


$$
\operatorname{tr}\left(\hat{J}_{w} \hat{H}_{w}^{-1}\right)=\sum_{t=1}^{n} \frac{q_{1}\left(x_{t}\right)}{q_{0}\left(x_{t}\right)}\left\{\frac{\hat{\varepsilon}_{t}^{2}}{\hat{\sigma}^{2}} \hat{h}_{t}+\frac{w\left(x_{t}\right)}{2 \hat{c}_{w}}\left(\frac{\hat{\varepsilon}_{t}^{2}}{\hat{\sigma}^{2}}-1\right)^{2}\right\} .
$$

We apply the above formulas to the data generated from (2.2) and (2.3) in Section 2. Fig. 2a shows the plot of the information criterion and its two components for $d=2$. By increasing $\lambda$ from 0 to 1 , the first term of (5.1) decreases while the second term increases in general. We numerically find $\hat{\lambda}$ so that the two terms balance. For $d=2$, $\mathrm{IC}_{w}$ takes the minimum 32.62 at $\hat{\lambda}=0.56$. The regression curves obtained by this method are shown in Fig. 2b.

Table 1 shows $\mathrm{IC}_{w}$ values for $d=0, \ldots, 4$. For each $d, \mathrm{IC}_{w}$ is minimized at $\lambda=\hat{\lambda}$. Then, $\mathrm{IC}_{w}$ of $\hat{\lambda}$ is minimized at the model $d=3$. By minimizing $\mathrm{IC}_{w}, \lambda$ and $d$ are simultaneously selected. For $d=3$, it turns out that $\hat{\lambda}=0.01 \approx 0$. In fact, the model of $d=3$ is correctly specified in this dataset, and it follows from Lemma 4 that $\hat{\theta}_{0}$ is optimal for $d \geqslant 3$. Even in such a situation, the appropriate $\hat{\lambda}$ is selected by minimizing IC ${ }_{w}$.

Table 2
Asymptotic convergence of the second term of (4.1). $2 n$ times of $\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)-\operatorname{loss}_{1}\left(\theta_{w}^{*}\right)$ is calculated for the Monte-Carlo replicates, and its average is tabulated. For every simulation ( $d=0,1,2$ and $\lambda=0,1$ ), the values are showing a good convergence as $n \rightarrow \infty$
| $n$ | $d=0$ |  | $d=1$ |  | $d=2$ |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $\lambda=0$ | $\lambda=1$ | $\lambda=0$ | $\lambda=1$ | $\lambda=0$ | $\lambda=1$ |
| 50 | -3.9 | 5.5 | -2.0 | 8.9 | 19.0 | 15.9 |
| 100 | -5.1 | 4.8 | -3.1 | 7.6 | 17.7 | 11.3 |
| 300 | -7.0 | 4.5 | -4.5 | 6.8 | 17.7 | 9.0 |
| 1000 | -8.0 | 4.4 | -4.9 | 6.6 | 19.3 | 8.5 |


Table 3
Asymptotic convergence of (5.2). $2 n \operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)+2 L_{1}\left(\hat{\theta}_{w}\right)$ is calculated for the Monte-Carlo replicates, and its average is tabulated in the left columns. For $n \geqslant 300$, this agrees very well with the average of $2 \operatorname{tr}\left(\hat{J}_{w} \hat{H}_{w}^{-1}\right)$ tabulated in the right columns. $2 \operatorname{tr}\left(J_{w} H_{w}^{-1}\right)$ is shown in the $n=\infty$ row
| $n$ | $d=0$ |  |  |  | $d=1$ |  |  |  | $d=2$ |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $\lambda=0$ |  | $\lambda=1$ |  | $\lambda=0$ |  | $\lambda=1$ |  | $\lambda=0$ |  | $\lambda=1$ |  |
| 50 | 1.8 | 1.7 | 9.9 | 7.7 | 6.8 | 6.1 | 15.7 | 11.1 | 26.4 | 13.1 | 24.8 | 13.4 |
| 100 | 1.5 | 1.4 | 9.2 | 8.1 | 6.0 | 5.7 | 14.2 | 12.0 | 22.6 | 14.9 | 19.8 | 14.9 |
| 300 | 1.3 | 1.3 | 8.8 | 8.4 | 5.4 | 5.3 | 13.3 | 12.6 | 18.5 | 15.7 | 17.3 | 16.0 |
| 1000 | 1.2 | 1.2 | 8.7 | 8.6 | 5.1 | 5.1 | 13.1 | 12.9 | 16.2 | 15.4 | 16.7 | 16.3 |
| $\infty$ |  | 1.2 |  | 8.6 |  | 5.0 |  | 13.0 |  | 14.9 |  | 16.4 |


In practical data analysis, it would be rare to have correctly specified models at hand. Therefore, we exclude $d \geqslant 3$ from the above example, and restrict the candidates to $d<3$. Then, $d=2$ is selected, and $d=1$ has almost the same $\mathrm{IC}_{w}$ value, while $d=0$ has significantly larger $\mathrm{IC}_{w}$ value. This agrees with the asymptotic result verified by extensive Monte-Carlo simulations in Shimodaira (1997) that (4.1) is minimized when $\lambda=1$ and $d=1$ over $d \in\{0,1,2\}$, for sufficiently large $n$.

## 7. Simulation study

First we show simulation results in Tables 1-3 which confirm the theory of Sections 4 and 5. A large number $N$ of replicates of the dataset of size $n$ are generated from (2.2) and (2.3). We used (2.4) as $q_{1}(x)$. Four simulations of $n=50,100,300$, and 1000 are done with $N=10^{5}$ for $n=50-300$ and $N=10^{6}$ for $n=1000$. For each replicate of the dataset, $\hat{\theta}_{w}$ is calculated for $\lambda=0,1$ and $d=0,1,2$. Then, $\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)$, $L_{1}\left(\hat{\theta}_{w}\right)$, and $\operatorname{tr}\left(\hat{J}_{w} \hat{H}_{w}^{-1}\right)$ are calculated, and their averages over the $N$ replicates are obtained for each simulation. The tables show nice agreement between the simulations and the theory.

Next, we show the results of another set of simulations in Table 4 which confirms the practical performance of the weight selection procedure. We used (2.3) and (2.4) as before, but (2.2) is replaced by $y=-x+\beta_{3} x^{3}+\varepsilon$ for generating replicates of the

Table 4
The expected loss for the selected weight and the selected model. $2 n$ times of $\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)+E_{1}(\log q(y \mid x))$ is calculated for the replicates, and its average is tabulated in the columns of $\lambda=0,1$ for $d=0,1,2$. The average of the loss of the selected weight is shown in the columns of $\hat{\lambda}$. The right most columns show the average of the loss of the selected model
| $\beta_{3}$ | $d=0$ |  |  | $d=1$ |  |  | $d=2$ |  |  | $\hat{d}$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | 0 | 1 | $\hat{\lambda}$ | 0 | 1 | $\hat{\lambda}$ | 0 | 1 | $\hat{\lambda}$ | 0 | 1 | $\hat{\lambda}$ |
| 1.0 | 98.0 | 50.7 | 50.9 | 123.8 | 12.3 | 11.9 | 71.7 | 16.0 | 16.7 | 73.2 | 15.0 | 15.3 |
| 0.5 | 96.0 | 61.1 | 61.1 | 49.9 | 9.0 | 8.2 | 25.6 | 11.8 | 11.5 | 26.9 | 11.0 | 10.8 |
| 0.2 | 142.2 | 68.4 | 68.4 | 12.6 | 7.8 | 6.4 | 8.5 | 10.4 | 8.1 | 10.1 | 9.6 | 7.9 |
| 0.1 | 152.8 | 71.1 | 71.0 | 6.0 | 7.8 | 5.7 | 5.9 | 10.4 | 7.2 | 6.3 | 9.6 | 6.9 |
| 0.0 | 162.2 | 73.8 | 73.7 | 3.6 | 7.7 | 4.8 | 5.0 | 10.2 | 6.6 | 4.4 | 9.5 | 6.0 |


dataset of size $n=100$. Five simulations of $\beta_{3}=1.0,0.5,0.2,0.1$, and 0.0 are done with $N=10^{4}$. In the table, $E_{1}(-\log q(y \mid x))$ is subtracted from the loss to make comparisons easier.

The expected loss of MLE ( $\lambda=0$ ) is 123.8 for $\beta_{3}=1.0, d=1$, while that of MWLE $(\lambda=1)$ is 12.3 , showing a great improvement as we have observed in the numerical example. The expected loss of MWLE with the selected weight $(\hat{\lambda})$ is 11.9 , which is not significantly different from that of $\lambda=1$. This is a consequence of the large sample size $n=100$, where the first term of (4.1) or (5.1) is dominant. The same observation holds for $\beta_{3}=1.0-0.0, d=0$, and $\beta_{3}=1.0,0.5, d=1,2$.

On the other hand, $\lambda=0$ is significantly better than $\lambda=1$ for $\beta_{3}=0.0, d=1,2$, where the model is correctly specified. In this case the second term of (4.1) is dominant and $\lambda=0$ is the optimal choice as mentioned in Lemma 4. The selected weight $\hat{\lambda}$ performs close to $\lambda=0$, but with slightly larger expected loss. This difference is the price we pay for the weight selection using (5.1) which is an estimate of (4.1), not the true value of (4.1).

For all the cases of $\beta_{3}=1.0-0.0, d=0,1,2$, the weight selection procedure gives the expected loss close to the optimal choice. Fixing $\lambda$ to either of 0 or 1 can lead to very poor performance. The same observation holds for the model selection as shown in the columns of $\hat{d}$.

## 8. Bayesian inference

We have been working on the predictive density

$$
p\left(y \mid x, \hat{\theta}_{w}\right),
$$

which is based on MWLE $\hat{\theta}_{w}$. This type of predictive density is occasionally called as an estimative density in the literature. Another possibility is the Bayesian predictive density. Here we consider a weighted version of it, and examine its performance in prediction.

Let $p(\theta)$ be the prior density of $\theta$. Given the data $\left(x^{(n)}, y^{(n)}\right)$, we shall define the weighted posterior density by

$$
p_{w}\left(\theta \mid x^{(n)}, y^{(n)}\right) \propto p(\theta) \exp L_{w}\left(\theta \mid x^{(n)}, y^{(n)}\right) .
$$

Then the predictive density will be

$$
p_{w}\left(y \mid x, x^{(n)}, y^{(n)}\right)=\int p(y \mid x, \theta) p_{w}\left(\theta \mid x^{(n)}, y^{(n)}\right) \mathrm{d} \theta
$$

In the case of $w(x) \equiv 1$, (8.2) reduces to the ordinary posterior density, and (8.3) reduces to the ordinary Bayesian predictive density.

The Kullback-Leibler loss of (8.3) with respect to $q(y \mid x) q_{1}(x)$ is

$$
-\int q_{1}(x) \int q(y \mid x) \log p_{w}\left(y \mid x, x^{(n)}, y^{(n)}\right) \mathrm{d} y \mathrm{~d} x
$$

and thus the expected loss is given by

$$
E_{0}^{(n)}\left(E_{1}\left(-\log p_{w}\left(y \mid x, x^{(n)}, y^{(n)}\right)\right)\right) .
$$

Lemma 5. For sufficiently large $n$, (8.4) is asymptotically expanded as

$$
E_{0}^{(n)}\left(\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)\right)+\frac{1}{n}\left\{K_{w}^{[1] \prime} a_{w}-\frac{1}{2} \operatorname{tr}\left(\left(K_{w}^{[1 \cdot 1]}-K_{w}^{[2]}\right) H_{w}^{-1}\right)\right\}+\mathrm{o}\left(n^{-1}\right),
$$

where

$$
K_{w}^{[1 \cdot 1]}=E_{0}\left\{\left.\left.\frac{q_{1}(x)}{q_{0}(x)} \frac{\partial \log p(y \mid x, \theta)}{\partial \theta}\right|_{\theta_{w}^{*}} \frac{\partial \log p(y \mid x, \theta)}{\partial \theta^{\prime}}\right|_{\theta_{w}^{*}}\right\}
$$

and $a_{w}=\operatorname{plim}_{n \rightarrow \infty} \hat{a}_{w}$ is the probability limit of

$$
\hat{a}_{w}=n \int\left(\theta-\hat{\theta}_{w}\right) p_{w}\left(\theta \mid x^{(n)}, y^{(n)}\right) \mathrm{d} \theta
$$

Furthermore, (8.4) is estimated by an information criterion

$$
-2 \sum_{t=1}^{n} \frac{q_{1}\left(x_{t}\right)}{q_{0}\left(x_{t}\right)} \log p_{w}\left(y_{t} \mid x_{t}, x^{(n)}, y^{(n)}\right)+2 \operatorname{tr}\left(J_{w} H_{w}^{-1}\right) .
$$

In fact, the expectation of (8.6), if divided by $2 n$, is equal to (8.5) up to $\mathrm{O}\left(n^{-1}\right)$ terms.

When $q_{1}(x)=q_{0}(x)$ and $w(x) \equiv 1$, (8.6) reduces to the information criterion for the Bayesian predictive density given in Konishi and Kitagawa (1996). Selection of $w(x)$ as well as selection of $p(\theta)$ and $p(y \mid x, \theta)$ becomes possible by minimizing (8.6). Comparing the values of (5.1) and (8.6), we can also choose which to use from (8.1) and (8.3).

The decrease of the expected loss of (8.3) from that of (8.1) is of order $\mathrm{O}\left(n^{-1}\right)$ as shown in (8.5), which can be positive or negative depending on $q(y \mid x)$. For brevity sake, we assume $q_{1}(x)=q_{0}(x)$ and $w(x) \equiv 1$ below. Then the decrease in the expected loss is $\Delta / 2 n+\mathrm{o}\left(n^{-1}\right)$, where $\Delta=\left(\operatorname{tr}\left(G_{0} H_{0}^{-1}\right)-\operatorname{dim} \theta\right) . G_{0}-H_{0} \neq 0$ and $\Delta \neq 0$ under

![](https://cdn.mathpix.com/cropped/9d044cef-46c9-4817-b90e-7c28eee2c697-13.jpg?height=384&width=585&top_left_y=168&top_left_x=424)
Fig. 3. The curvature of the model in relation to the location of the true density $q$. On the parametric model denoted by $p(\cdot)$, we have $\Delta=0$, and $|\Delta|$ increases as $q$ deviates from $p(\cdot)$. The region of $\Delta>0$ is in the inside direction of the model, and $\Delta<0$ is in the outside direction of the model. $\hat{q}$ denotes the empirical distribution, and the projection of $\hat{q}$ to the model is the estimative density $\hat{p}=p\left(y \mid x, \hat{\theta}_{0}\right) . \hat{p}_{\mathrm{B}}$ denotes the Bayesian predictive density.

misspecification in general, which is utilized in the information matrix tests (White, 1982) for detecting the misspecification.

An enlightening interpretation of $\Delta$ may be possible by the following geometric argument using the terminology of Efron (1978) and Amari (1985). Fig. 3 shows the space of all conditional densities. $\Delta$ is determined by the extent of the misspecification multiplied by the "embedding mixture curvature" of the model ( S . Amari, personal communication). Bayesian predictive density $\hat{p}_{\mathrm{B}}$ is a mixture of $p(y \mid x, \theta)$ around $\hat{\theta}_{0}$, and thus it is located in the inside of the model because of the curvature; $\hat{p}_{\mathrm{B}}$ deviates from $\hat{p}$ of order $\mathrm{O}\left(n^{-1}\right)$ as shown in Davison (1986). Therefore, $\hat{p}_{\mathrm{B}}$ has larger expected loss than $\hat{p}$ if $q(y \mid x)$ is located in the outside of the model (i.e. $\Delta<0$ ), because $\hat{p}_{\mathrm{B}}$ is located in the opposite side of $q$. This does not contradict the classical result that the expected loss of $\hat{p}_{\mathrm{B}}$ is asymptotically smaller than that of $\hat{p}$ for some prior. In Bayesian literature, the case of correct specification (i.e. $\Delta=0$ ) is discussed and the difference of the expected loss is of order $\mathrm{O}\left(n^{-2}\right)$ as seen in Komaki (1996). Note that the quadratic form of $\Delta$ is relevant when the curvature vanishes, and $\Delta \geqslant 0$ if all the eigenvalues are non-negative; see Shimodaira (1997) for details.

## 9. Concluding remarks

Although the ratio $q_{1}(x) / q_{0}(x)$ has been assumed to be known, it is often estimated from data in practice. Assuming $q_{1}(x)$ is known, we tried three possibilities in the numerical example of Section 2: (i) $q_{0}(x)$ is specified correctly without unknown parameters. (ii) Assuming the normality of $q_{0}(x)$, the unknown $\mu_{0}$ and $\tau_{0}$ are estimated. (iii) Non-parametric kernel density estimation is applied to $q_{0}(x)$. Then, it turns out that MWLE is robust against the estimation of $q_{1}(x) / q_{0}(x)$ and the results are almost identical in the three cases. This may be because the form of $q_{0}(x)$ is quite simple and the sample size $n=100$ is rather large.

A parametric approach to take account of estimation of $q_{1}(x) / q_{0}(x)$ is considered as follows. Let the observed data $z_{t}, t=1, \ldots, n$, follow $p_{0}(z \mid \theta)$, while future observations will follow $p_{1}(z \mid \theta)$. Then a possible estimating equation will be

$$
\sum_{t=1}^{n} w\left(z_{t} \mid \theta\right) \frac{\partial \log p_{1}\left(z_{t} \mid \theta\right)}{\partial \theta}=0
$$

where $w(z \mid \theta)=\left(p_{1}(z \mid \theta) / p_{0}(z \mid \theta)\right)^{\lambda}$. The solution of (9.1) reduces to the MWLE discussed in this paper by letting $z=(x, y), p_{0}(z \mid \theta)=p(y \mid x, \theta) q_{0}(x)$, and $p_{1}(z \mid \theta)= p(y \mid x, \theta) q_{1}(x)$.

The estimating equation (9.1) is often seen in the literature of the robust parametric estimation; e.g., Green (1984), Hampel et al. (1986), Lindsay (1994), Basu and Lindsay (1994), Field and Smith (1994) and Windham (1995). In this context, the samples which are not concordant to the model $p_{1}(z \mid \theta)$ will be regarded as "outliers" and downweighted to reduce the impact on the parameter estimation. The specification of the weight function is thus the focal point of the argument. Although the covariate shift is a mechanism different from the outliers, an interpretation of MWLE in terms of the robust estimation can be given as follows. For simplicity, let $z$ be a discrete random variable and $\hat{p}_{0}(z)$ be the observed relative frequency which estimates the contaminated distribution $p_{0}(z)$ consistently. The weight $\left(p_{1}(z \mid \theta) / \hat{p}_{0}(z)\right)^{\lambda}$ in (9.1) then leads to the minimum disparity estimator obtained by minimizing the power divergence

$$
2 n I^{-\lambda}=\frac{2}{\lambda(\lambda-1)} \sum_{z} \hat{p}_{0}(z)\left\{\left(\frac{\hat{p}_{0}(z)}{p_{1}(z \mid \theta)}\right)^{-\lambda}-1\right\}
$$

(Cressie and Read, 1984; Lindsay, 1994). The uniform weight $\lambda=0$ is sensitive to outliers, and a positive value $\lambda=0.5$, say, improves the robustness. In the regression analysis, the deviation of $p_{0}(z)$ from $p_{1}(z)$ is decomposed into two parts: the misspecification of $p(y \mid x, \theta)$ and the covariate shift. MWLE is obtained by applying the power weighting scheme to the second part where $\lambda=1$ is asymptotically optimal. It may be interesting to consider a robust version of MWLE by applying the weight, say $\left(p_{1}(y \mid x, \theta) / \hat{p}_{0}(y \mid x)\right)^{v}$ with $v=0.5$, to the first part as well.

A numerical example of simultaneous selection of the weight and the model by the information criterion is shown in Section 6. The information criterion takes account of the selection bias caused by estimation of the parameter, but it does not take account the bias caused by the selection of the weight and the model. It is important to evaluate the expected loss of the predictive density obtained after these selection. The simulation study of Section 7 indicates that the method presented in this paper is effective, and the final expected loss of the selected weight and/or model is reasonably small.

Although we have employed a specific type of one-parameter connection in (5.3), other types of connection may work similarly. However, increasing the number of connection parameters will increase the final expected loss because of the sampling error of (5.1) as an estimator of (4.1). We observed the slight increase of the expected loss of $\hat{\lambda}$ in Table 4, and this increase can be much larger for multi-parameter connections.

We derived a variant of AIC for MWLE under covariate shift. On the other hand, Shimodaira (1994) and Cavanaugh and Shumway (1998) discussed variants of AIC for MLE in the presence of incomplete data. Information criteria have to be tailored for different styles of sampling scheme, and the unified approach for them is left as a future work.

A software for calculating $\mathrm{IC}_{w}$ and $\hat{\lambda}$ of normal regression will be available in S language at http://www.ism.ac.jp/shimo/.

## Acknowledgements

I would like to thank John Copas, Tony Hayter, Motoaki Kawanabe, Shinto Eguchi, and the reviewers for helpful comments and suggestions.

## Appendix A.

Proof of Lemma 1. Since $\theta_{w}^{*}$ is interior to $\Theta$, so is $\hat{\theta}_{w}$ for sufficiently large $n$. Then, $\hat{\theta}_{w}$ is obtained as a solution of the estimating equation

$$
\left.\sum_{t=1}^{n} \frac{\partial l_{w}\left(x_{t}, y_{t} \mid \theta\right)}{\partial \theta}\right|_{\hat{\theta}_{w}}=0 .
$$

The Taylor expansion of (A.1) leads to

$$
\left.n^{-1} \sum_{t=1}^{n} \frac{\partial^{2} l_{w}\left(x_{t}, y_{t} \mid \theta\right)}{\partial \theta \partial \theta^{\prime}}\right|_{\theta_{w}^{*}} n^{1 / 2}\left(\hat{\theta}_{w}-\theta_{w}^{*}\right)=-\left.n^{-1 / 2} \sum_{t=1}^{n} \frac{\partial l_{w}\left(x_{t}, y_{t} \mid \theta\right)}{\partial \theta}\right|_{\theta_{w}^{*}}+\mathrm{O}_{\mathrm{p}}\left(n^{-1 / 2}\right)
$$

It follows from the central limit theorem that the right-hand side is asymptotically distributed as $\mathrm{N}\left(0, G_{w}\right)$, while the left-hand side converges to $H_{w} n^{1 / 2}\left(\hat{\theta}_{w}-\theta_{w}^{*}\right)$. Thus we obtained the desired result.

Proof of Lemma 2. The Taylor expansion of $\operatorname{loss}_{1}\left(\hat{\theta}_{w}\right)$ around $\theta_{w}^{*}$ is

$$
\operatorname{loss}_{1}\left(\theta_{w}^{*}\right)+\frac{1}{n}\left\{\left(K_{w}^{[1]}\right)_{i} n^{1 / 2} \dot{\theta}_{w}^{i}+\frac{1}{2}\left(K_{w}^{[2]}\right)_{i j} \dot{\theta}_{w}^{i} \dot{\theta}_{w}^{j}\right\}+\mathrm{O}_{\mathrm{p}}\left(n^{-3 / 2}\right)
$$

where $\dot{\theta}_{w}=n^{1 / 2}\left(\hat{\theta}_{w}-\theta_{w}^{*}\right)$, and the summation convention $A_{i} B^{i}=\sum_{i=1}^{m} A_{i} B^{i}$ is used. Considering Lemma 1, the expectation of (A.3) gives (4.1). By taking expectation of (A.2), we observe $b_{w}=\mathrm{O}(1)$.

Proof of Lemma 3. Considering the $\mathrm{O}_{\mathrm{p}}\left(n^{-1 / 2}\right)$ term in (A.2) explicitly, the Taylor expansion of (A.1) gives

$$
\hat{H}_{w}^{*} \dot{\theta}_{w}=-\left.n^{-1 / 2} \sum_{t=1}^{n} \frac{\partial l_{w}\left(x_{t}, y_{t} \mid \theta\right)}{\partial \theta}\right|_{\theta_{w}^{*}}+n^{-1 / 2} e_{w},
$$

where

$$
\hat{H}_{w}^{*}=\left.\frac{1}{n} \sum_{t=1}^{n} \frac{\partial^{2} l_{w}\left(x_{t}, y_{t} \mid \theta\right)}{\partial \theta \partial \theta^{\prime}}\right|_{\theta_{w}^{*}}, \quad\left(e_{w}\right)_{i}=-\frac{1}{2}\left(H_{w}^{[3]}\right)_{i j k} \dot{\theta}_{w}^{j} \dot{\theta}_{w}^{k}+\mathrm{O}_{\mathrm{p}}\left(n^{-1 / 2}\right) .
$$

Noting $\hat{H}_{w}^{*-1}=H_{w}^{-1}-H_{w}^{-1}\left(\hat{H}_{w}^{*}-H_{w}\right) H_{w}^{-1}+\mathrm{O}_{\mathrm{p}}\left(n^{-1}\right), n^{1 / 2} E_{0}^{(n)}\left(\dot{\theta}_{w}\right)$ is written as

$$
E_{0}\left\{\left.\left.H_{w}^{-1} \frac{\partial^{2} l_{w}(x, y \mid \theta)}{\partial \theta \partial \theta^{\prime}}\right|_{\theta^{*}} H_{w}^{-1} \frac{\partial l_{w}(x, y \mid \theta)}{\partial \theta}\right|_{\theta^{*}}\right\}+H_{w}^{-1} E_{0}^{(n)}\left(e_{w}\right)+\mathrm{O}\left(n^{-1 / 2}\right),
$$

which immediately implies (4.2).
Proof of Lemma 4. For any $x$, the conditional Kullback-Leibler loss

$$
\operatorname{loss}(\theta \mid x)=-\int q(y \mid x) \log p(y \mid x, \theta) \mathrm{d} y
$$

is minimized at $\theta^{*}$ if $q(y \mid x)=p\left(y \mid x, \theta^{*}\right)$. Then $\theta_{w}^{*}=\theta^{*}$ for any $w(x)$, because $E_{0}\left(l_{w}(x, y \mid \theta)\right)=\int q(x) w(x) \operatorname{loss}(\theta \mid x) \mathrm{d} x$. Thus $\operatorname{loss}_{1}\left(\theta_{w}^{*}\right)$ in (4.1) is equal for any $w(x)$.

Considering $K_{w}^{[1]}=0$, the second term in (4.1) is written as

$$
n^{-1} \operatorname{tr}\left(K_{w}^{[2]} Q(w)^{-1} Q\left(w^{2}\right) Q(w)^{-1}\right),
$$

where $K_{w}^{[2]}=Q\left(q_{1} / q_{0}\right)$ and $Q(a)$ is defined for any $a(x)$ by

$$
Q(a)=E_{0}\left\{\left.\left.a(x) \frac{\partial \log p(y \mid x, \theta)}{\partial \theta}\right|_{\theta^{*}} \frac{\partial \log p(y \mid x, \theta)}{\partial \theta^{\prime}}\right|_{\theta^{*}}\right\} .
$$

It it easy to verify that $Q(w)^{-1} Q\left(w^{2}\right) Q(w)^{-1}-Q(1)^{-1}$ is non-negative definite for any $w(x)$, and so (A.4) is minimized when $w(x) \equiv 1$.

Proof of Theorem 1. The Taylor expansion of $\log p\left(y \mid x, \hat{\theta}_{w}\right)$ around $\theta_{w}^{*}$ gives

$$
L_{1}\left(\hat{\theta}_{w}\right)=L_{1}\left(\theta_{w}^{*}\right)+\frac{1}{n}\left\{\left.\frac{\partial L_{1}(\theta)}{\partial \theta^{\prime}}\right|_{\theta_{w}^{*}} n^{1 / 2} \dot{\theta}_{w}+\left.\frac{1}{2} \frac{\partial^{2} L_{1}(\theta)}{\partial \theta^{i} \partial \theta^{j}}\right|_{\theta_{w}^{*}} \dot{\theta}_{w}^{i} \dot{\theta}_{w}^{j}\right\}+\mathrm{O}_{\mathrm{p}}\left(n^{-1 / 2}\right)
$$

and thus $E_{0}^{(n)}\left(-L_{1}\left(\hat{\theta}_{w}\right) / n\right)$ is expanded as

$$
\operatorname{loss}_{1}\left(\theta_{w}^{*}\right)-\frac{1}{n} E_{0}^{(n)}\left\{\left.\frac{1}{n} \frac{\partial L_{1}(\theta)}{\partial \theta^{\prime}}\right|_{\theta_{w}^{*}} n^{1 / 2} \dot{\theta}_{w}\right\}+\frac{1}{2 n} \operatorname{tr}\left(K_{w}^{[2]} H_{w}^{-1} G_{w} H_{w}^{-1}\right)+\mathrm{O}\left(n^{-3 / 2}\right) .
$$

Considering $-n^{-1} \partial L_{1}(\theta) /\left.\partial \theta\right|_{\theta_{w}^{*}}=K_{w}^{[1]}+\mathrm{O}_{\mathrm{p}}\left(n^{-1 / 2}\right)$, the second term of (A.5) becomes

$$
\begin{aligned}
& \frac{1}{n} K_{w}^{[1] \prime} b_{w}+\frac{1}{n} E_{0}^{(n)}\left\{n^{1 / 2}\left(-\left.\frac{1}{n} \frac{\partial L_{1}(\theta)}{\partial \theta^{i}}\right|_{\theta_{w}^{*}}-\left(K_{w}^{[1]}\right)_{i}\right)\right. \\
& \left.\quad \times H_{w}^{i j}\left(\left.n^{-1 / 2} \frac{\partial L_{w}(\theta)}{\partial \theta^{j}}\right|_{\theta_{w}^{*}}+\mathrm{O}_{\mathrm{p}}\left(n^{-1 / 2}\right)\right)\right\} \\
& =\frac{1}{n} K_{w}^{[1] \prime} b_{w}-\frac{1}{n} H_{w}^{i j}\left(J_{w}\right)_{i j}+\mathrm{O}\left(n^{-3 / 2}\right)
\end{aligned}
$$

Combining this with (A.5) and (4.1) completes the proof.

Proof of Lemma 5. Assuming certain regularity conditions similar to those of Johnson (1970), we have the asymptotic limit of (8.2) is normal with mean $\hat{\theta}_{w}$ and covariance matrix $\hat{H}_{w}^{-1} / n$, since $\log p_{w}\left(\theta \mid x^{(n)}, y^{(n)}\right)$ is expanded as

$$
-\frac{1}{2} n^{1 / 2}\left(\theta-\hat{\theta}_{w}\right)^{\prime} \hat{H}_{w} n^{1 / 2}\left(\theta-\hat{\theta}_{w}\right)+\mathrm{O}_{\mathrm{p}}\left(n^{-1 / 2}\right),
$$

where the terms independent of $\theta$ are omitted. Then, (8.3) is asymptotically expanded as

$$
p\left(y \mid x, \hat{\theta}_{w}\right)+\left.\frac{1}{n} \frac{\partial p(y \mid x, \theta)}{\partial \theta^{\prime}}\right|_{\hat{\theta}_{w}} \hat{a}_{w}+\frac{1}{2 n} \operatorname{tr}\left(\left.\frac{\partial^{2} p(y \mid x, \theta)}{\partial \theta \partial \theta^{\prime}}\right|_{\hat{\theta}_{w}} \hat{H}_{w}^{-1}\right)+\mathrm{o}_{\mathrm{p}}\left(n^{-1}\right) .
$$

Note that Dunsmore (1976) gave the unweighted version of (A.6) when the model specification is correct, but the term of $\hat{a}_{w}$ was missing as indicated by Komaki (1996). Applying the identity

$$
\frac{1}{p} \frac{\partial^{2} p}{\partial \theta \partial \theta^{\prime}}=\frac{\partial \log p}{\partial \theta} \frac{\partial \log p}{\partial \theta^{\prime}}+\frac{\partial^{2} \log p}{\partial \theta \partial \theta^{\prime}}
$$

to the third term of (A.6), we obtain

$$
\begin{aligned}
& \log p_{w}\left(y \mid x, x^{(n)}, y^{(n)}\right) \\
& \quad=\log p\left(y \mid x, \hat{\theta}_{w}\right)+\left.\frac{1}{n} \frac{\partial \log p(y \mid x, \theta)}{\partial \theta^{\prime}}\right|_{\theta_{w}^{*}} a_{w}+\frac{1}{2 n} \operatorname{tr}\left\{\left(\left.\frac{\partial \log p(y \mid x, \theta)}{\partial \theta}\right|_{\theta_{w}^{*}}\right.\right. \\
& \left.\left.\quad \quad \times\left.\frac{\partial \log p(y \mid x, \theta)}{\partial \theta^{\prime}}\right|_{\theta_{w}^{*}}+\left.\frac{\partial^{2} \log p(y \mid x, \theta)}{\partial \theta \partial \theta^{\prime}}\right|_{\theta_{w}^{*}}\right) H_{w}^{-1}\right\}+\mathrm{o}_{\mathrm{p}}\left(n^{-1}\right)
\end{aligned}
$$

Thus (8.5) immediately follows from (A.7). The last statement of the lemma is verified by combining (A.7) with Theorem 1.

## References

Akaike, H., 1974. A new look at the statistical model identification. IEEE Trans. Automat. Control 19, 716-723.
Amari, S., 1985. Differential-Geometrical Methods in Statistics. Lecture Notes in Statistics, Vol. 28. Springer, Berlin.
Basu, A., Lindsay, B.G., 1994. Minimum disparity estimation for continuous models: efficiency, distributions and robustness. Ann. Inst. Statist. Math. 46, 683-705.
Cavanaugh, J.E., Shumway, R.H., 1998. An Akaike information criterion for model selection in the presence of incomplete data. J. Statist. Plann. Infererence 67, 45-65.
Cressie, N., Read, T.R.C., 1984. Multinomial goodness-of-fit tests. J. Roy. Statist. Soc. Ser. B 46, 440-464.
Davison, A.C., 1986. Approximate predictive likelihood. Biometrika 73, 323-332.
Dunsmore, I.R., 1976. Asymptotic prediction analysis. Biometrika 63, 627-630.
Efron, B., 1978. The geometry of exponential families. Ann. Statist. 6, 362-376.
Field, C., Smith, B., 1994. Robust estimation - a weighted maximum likelihood approach. Internat. Statist. Rev. 62, 405-424.
Green, P.J., 1984. Iteratively reweighted least squares for maximum likelihood estimation, and some robust and resistant alternatives (with discussion). J. Roy. Statist. Soc. Ser. B 46, 149-192.
Hampel, F.R., Ronchetti, E.M., Rousseeuw, P.J., Stahel, W.A., 1986. Robust Statistics: The Approach Based on Influence Functions. Wiley, New York.

Johnson, R.A., 1970. Asymptotic expansions associated with posterior distributions. Ann. Math. Statist. 41, 851-864.
Komaki, F., 1996. On asymptotic properties of predictive distributions. Biometrika 83, 299-313.
Konishi, S., Kitagawa, G., 1996. Generalised information criteria in model selection. Biometrika 83, 875-890.
Lindsay, B.G., 1994. Efficiency versus robustness: the case for minimum Hellinger distance and related methods. Ann. Statist. 22, 1081-1114.
Linhart, H., Zucchini, W., 1986. Model Selection. Wiley, New York.
Pfeffermann, D., Skinner, C.J., Holmes, D.J., Goldstein, H., Rasbash, J., 1998. Weighting for unequal selection probabilities in multilevel models. J. Roy. Statist. Soc. Ser. B 60, 23-56.
Shibata, R., 1989. Statistical aspects of model selection. In: Willems, J.C. (Ed.), From Data to Model. Springer, Berlin, pp. 215-240.
Shimodaira, H., 1994. A new criterion for selecting models from partially observed data. In: Cheeseman, P., Oldford, R.W. (Eds.), Selecting Models from Data: AI and Statistics IV. Springer, Berlin, pp. 21-30 (Chapter 3).
Shimodaira, H., 1997. Predictive inference under misspecification and its model selection. Research Memorandum 642, The Institute of Statistical Mathematics, Tokyo, Japan.
Skinner, C.J., Holt, D., Smith, T.M.F., 1989. Analysis of Complex Surveys. Wiley, New York.
Takeuchi, K., 1976. Distribution of information statistics and criteria for adequacy of models. Math. Sci. (153), 12-18 (in Japanese).

White, H., 1982. Maximum likelihood estimation of misspecified models. Econometrica 50, 1-26.
Windham, M.P., 1995. Robustifying model fitting. J. Roy. Statist. Soc. Ser. B 57, 599-609.


[^0]:    *Correspondence address: Department of Statistics, Sequoia Hall, 390 Serra Mall, Stanford University, Stanford, CA 94305-4065, USA.
    E-mail address: shimo@ism.ac.jp (H. Shimodaira).

