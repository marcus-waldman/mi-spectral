---
citekey: shimodairaInformationCriterionModel2017
item_type: article
authors: 'Shimodaira, Hidetoshi and Maeda, Haruyoshi'
year: 2018
title: An Information Criterion for Model Selection with Missing Data via Complete-Data Divergence
venue: Annals of the Institute of Statistical Mathematics
volume: 70
issue: 2
pages: 421--438
doi: 10.1007/s10463-016-0592-7
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\shimodaira_information_criterion_model_2017.pdf'
pdf_sha256: 0f8c796463fcbca638ad0966e0758e6293323d1dceec42972e6c2066909631f9
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T13:50:44Z
---
# An information criterion for model selection with missing data via complete-data divergence 

Hidetoshi Shimodaira ${ }^{1,2}$. Haruyoshi Maeda ${ }^{1,3}$

Received: 26 September 2015 / Revised: 4 November 2016 / Published online: 21 January 2017
© The Institute of Statistical Mathematics, Tokyo 2017


#### Abstract

We derive an information criterion to select a parametric model of completedata distribution when only incomplete or partially observed data are available. Compared with AIC, our new criterion has an additional penalty term for missing data, which is expressed by the Fisher information matrices of complete data and incomplete data. We prove that our criterion is an asymptotically unbiased estimator of complete-data divergence, namely the expected Kullback-Leibler divergence between the true distribution and the estimated distribution for complete data, whereas AIC is that for the incomplete data. The additional penalty term of our criterion for missing data turns out to be only half the value of that in previously proposed information criteria PDIO and AICcd. The difference in the penalty term is attributed to the fact that our criterion is derived under a weaker assumption. A simulation study with the weaker assumption shows that our criterion is unbiased while the other two criteria are biased. In addition, we review the geometrical view of alternating minimizations of the EM algorithm. This geometrical view plays an important role in deriving our new criterion.


[^0]Keywords Akaike information criterion • Alternating projections • Data manifold • EM algorithm • Fisher information matrix • Incomplete data • Kullback-Leibler divergence • Misspecification • Takeuchi information criterion

## 1 Introduction

Modeling complete data $X=(Y, Z)$ is often preferable to modeling incomplete or partially observed data $Y$ when missing data $Z$ are not observed. The expectationmaximization (EM) algorithm (Dempster et al. 1977) computes the maximum likelihood estimate of parameter vector $\boldsymbol{\theta}$ for a parametric model of the probability distribution of $X$. In this research, we consider the problem of model selection in such situations. For mathematical simplicity, we assume that $X$ consists of independent and identically distributed random vectors. More specifically, $X=\left(\boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \ldots, \boldsymbol{x}_{n}\right)$, and the complete-data distribution is modeled as $\boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \ldots, \boldsymbol{x}_{n} \sim p_{x}(\boldsymbol{x} ; \boldsymbol{\theta})$. Each vector is decomposed as $\boldsymbol{x}^{T}=\left(\boldsymbol{y}^{T}, \boldsymbol{z}^{T}\right)$, and the marginal distribution is expressed as $p_{y}(\boldsymbol{y} ; \boldsymbol{\theta})=\int p_{x}(\boldsymbol{y}, \boldsymbol{z} ; \boldsymbol{\theta}) d \boldsymbol{z}$, where $T$ denotes the matrix transpose and the integration is over all possible values of $\boldsymbol{z}$. We formally treat $\boldsymbol{y}, \boldsymbol{z}$ as continuous random variables with the joint density function $p_{x}$. However, when they are discrete random variables, the integration should be replaced with a summation of the probability functions. We use symbols such as $p_{x}$ and $p_{y}$ for both the continuous and discrete cases, and simply refer to them as distributions.

The log-likelihood function is $\ell_{y}(\boldsymbol{\theta})=\sum_{t=1}^{n} \log p_{y}\left(\boldsymbol{y}_{t} ; \boldsymbol{\theta}\right)$ with the parameter vector $\boldsymbol{\theta}=\left(\theta_{1}, \ldots, \theta_{d}\right)^{T} \in \mathbb{R}^{d}$. We assume that the model is identifiable, and the parameter is restricted to $\Theta \subset \mathbb{R}^{d}$. Then, the maximum likelihood estimator (MLE) of $\boldsymbol{\theta}$ is defined by $\hat{\boldsymbol{\theta}}_{y}=\arg \max _{\boldsymbol{\theta} \in \Theta} \ell_{y}(\boldsymbol{\theta})$. The dependence of $\ell_{y}(\boldsymbol{\theta})$ and $\hat{\boldsymbol{\theta}}_{y}$ on $Y= \left(\boldsymbol{y}_{1}, \ldots, \boldsymbol{y}_{n}\right)$ is suppressed in the notation. Akaike (1974) proposed the information criterion

$$
\mathrm{AIC}=-2 \ell_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)+2 d
$$

for model selection. The first term measures the goodness of fit, whereas the second term is interpreted as a penalty for model complexity. The AIC values for candidate models are computed, and then the model that minimizes AIC is selected. This information criterion estimates the expected discrepancy between the unknown true distribution of $\boldsymbol{y}$, which is denoted as $q_{y}$, and the estimated distribution $p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)$. This discrepancy is measured by the incomplete-data Kullback-Leibler divergence.

In this study, we work on the complete-data Kullback-Leibler divergence instead of the incomplete-data counterpart. An information criterion to estimate the expected discrepancy between the unknown true distribution of $\boldsymbol{x}$, which is denoted as $q_{x}$, and the estimated distribution $p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)$ is derived. This approach makes sense when modeling complete data more precisely describes the part being examined. Similar attempts are found in the literature. Shimodaira (1994) proposed the information criterion PDIO (predictive divergence for incomplete observation models)

$$
\mathrm{PDIO}=-2 \ell_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)+2 \operatorname{tr}\left(I_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right) I_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)^{-1}\right) .
$$

The two matrices in the penalty term are the Fisher information matrices for complete data and incomplete data. They are defined by

$$
\begin{aligned}
I_{x}(\boldsymbol{\theta}) & =-\int p_{x}(\boldsymbol{x} ; \boldsymbol{\theta}) \frac{\partial^{2} \log p_{x}(\boldsymbol{x} ; \boldsymbol{\theta})}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{T}} \mathrm{~d} \boldsymbol{x} \\
I_{y}(\boldsymbol{\theta}) & =-\int p_{y}(\boldsymbol{y} ; \boldsymbol{\theta}) \frac{\partial^{2} \log p_{y}(\boldsymbol{y} ; \boldsymbol{\theta})}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{T}} \mathrm{~d} \boldsymbol{y} .
\end{aligned}
$$

Let $p_{z \mid y}(z \mid \boldsymbol{y} ; \boldsymbol{\theta})=p_{x}(\boldsymbol{y}, \boldsymbol{z} ; \boldsymbol{\theta}) / p_{y}(\boldsymbol{y} ; \boldsymbol{\theta})$ be the conditional distribution of $\boldsymbol{z}$ given $\boldsymbol{y}$, and $I_{z \mid y}(\boldsymbol{\theta})=I_{x}(\boldsymbol{\theta})-I_{y}(\boldsymbol{\theta})$ be the Fisher information matrix for $p_{z \mid y}$. Since $I_{z \mid y}(\boldsymbol{\theta})$ is nonnegative definite, we have $\operatorname{tr}\left(I_{x}(\boldsymbol{\theta}) I_{y}(\boldsymbol{\theta})^{-1}\right)=\operatorname{tr}\left(\left(I_{y}(\boldsymbol{\theta})+I_{z \mid y}(\boldsymbol{\theta})\right) I_{y}(\boldsymbol{\theta})^{-1}\right)= d+\operatorname{tr}\left(I_{z \mid y}(\boldsymbol{\theta}) I_{y}(\boldsymbol{\theta})^{-1}\right) \geq d$. Thus, the nonnegative difference

$$
\mathrm{PDIO}-\mathrm{AIC}=2 \operatorname{tr}\left(I_{z \mid y}\left(\hat{\boldsymbol{\theta}}_{y}\right) I_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)^{-1}\right)
$$

is interpreted as the additional penalty for missing data. There are similar attempts in the literature (Cavanaugh and Shumway 1998; Seghouane et al. 2005; Claeskens and Consentino 2008; Yamazaki 2014). In particular, Cavanaugh and Shumway (1998) proposed another information criterion

$$
\mathrm{AIC}_{c d}=-2 Q\left(\hat{\boldsymbol{\theta}}_{y} ; \hat{\boldsymbol{\theta}}_{y}\right)+2 \operatorname{tr}\left(I_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right) I_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)^{-1}\right)
$$

by replacing $\ell_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)$ in PDIO with $Q\left(\hat{\boldsymbol{\theta}}_{y} ; \hat{\boldsymbol{\theta}}_{y}\right)$ to measure the goodness of fit. It should be noted that cd stands for complete data. This is the function introduced in Dempster et al. (1977) for the EM algorithm, and is defined by

$$
Q\left(\boldsymbol{\theta}_{2} ; \boldsymbol{\theta}_{1}\right)=\sum_{t=1}^{n} \int p_{z \mid y}\left(z \mid \boldsymbol{y}_{t} ; \boldsymbol{\theta}_{1}\right) \log p_{x}\left(\boldsymbol{y}_{t}, z ; \boldsymbol{\theta}_{2}\right) \mathrm{d} z
$$

We recently found that the assumption in Shimodaira (1994) to derive PDIO is unnecessarily strong. Additionally, the same assumption explains the derivation of $\mathrm{AIC}_{c d}$. In this paper, we derive a new information criterion under a weaker assumption. The updated version of PDIO is

$$
\operatorname{AIC}_{x ; y}=-2 \ell_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)+d+\operatorname{tr}\left(I_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right) I_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)^{-1}\right)
$$

The first suffix $\boldsymbol{x}$ indicates that a random variable is used to measure the discrepancy, while the second suffix $\boldsymbol{y}$ indicates a random variable is used for the observation. Then, the additional penalty for missing data becomes

$$
\operatorname{AIC}_{x ; y}-\mathrm{AIC}=\operatorname{tr}\left(I_{z \mid y}\left(\hat{\boldsymbol{\theta}}_{y}\right) I_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)^{-1}\right)
$$

The additional penalty is only half the value of that in PDIO. In practice, the computation of $\mathrm{AIC}_{x ; y}$ as well as the related criteria PDIO and AIC ${ }_{c d}$ is not very difficult. The SEM algorithm of Meng and Rubin (1991) provides a shortcut to compute the penalty term $\operatorname{tr}\left(I_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right) I_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)^{-1}\right)$ without computing the two Fisher information matrices as described in Shimodaira (1994) and Cavanaugh and Shumway (1998).

To derive $\mathrm{AIC}_{x ; y}$, we first review the basic properties of Kullback-Leibler divergence for incomplete data in Sect. 2. Section 3 considers those for complete data. Although these results are not new, they are crucial for the argument in later sections. In particular, the geometrical view of alternating minimizations (Csiszár and Tusnády, 1984; Amari, 1995) in Sect. 3.3 is important to understand why the goodness of fit term of AIC $x ; y$ is expressed by the incomplete-data likelihood function instead of the complete-data counterpart.

Section 4, which begins the argument of model selection, discusses what the information criteria should estimate. In general, parametric models are misspecified, and we do not assume that the true distribution is expressed as $q_{x}=p_{x}\left(\boldsymbol{\theta}_{0}\right)$ using the "true" parameter value $\boldsymbol{\theta}_{0}$. However, the unbiasedness of $\mathrm{AIC}_{x ; y}$ is based on the assumption that $p_{z \mid y}(\boldsymbol{\theta})$ is correctly specified for $q_{z \mid y}$. In Sect. 5, we derive our new information criterion. The argument is very straightforward; it simply follows the argument for the robust version of AIC, which is also known as the Takeuchi information criterion (TIC) that is described in Burnham and Anderson (2002) and Konishi and Kitagawa (2008). Section 6 compares the assumptions used to derive PDIO and AIC ${ }_{c d}$ to those of $\mathrm{AIC}_{x ; y}$. Section 7 presents a simulation study to verify the theory. Finally, Sect. 8 contains some concluding remarks. Proofs are deferred to the Appendix.

## 2 Incomplete-data divergence

Here, we review Kullback-Leibler divergence and the asymptotic distribution of MLE under model misspecification (White 1982). Let $g_{y}$ and $f_{y}$ be the arbitrary probability distributions of incomplete data. The incomplete-data Kullback-Leibler divergence from $g_{y}$ to $f_{y}$ is

$$
D_{y}\left(g_{y} ; f_{y}\right)=-\int g_{y}(\boldsymbol{y})\left(\log f_{y}(\boldsymbol{y})-\log g_{y}(\boldsymbol{y})\right) \mathrm{d} \boldsymbol{y}
$$

where $D_{y}\left(g_{y} ; f_{y}\right) \geq 0$ and the equality holds for $g_{y}=f_{y}$ (Csiszár 1975; Amari and Nagaoka 2007). The cross-entropy is

$$
L_{y}\left(g_{y} ; f_{y}\right)=-\int g_{y}(\boldsymbol{y}) \log f_{y}(\boldsymbol{y}) \mathrm{d} \boldsymbol{y}
$$

and the entropy is $L_{y}\left(g_{y}\right)=L_{y}\left(g_{y} ; g_{y}\right)$. Instead of minimizing $D_{y}\left(g_{y} ; f_{y}\right)= L_{y}\left(g_{y} ; f_{y}\right)-L_{y}\left(g_{y}\right)$ with respect to $f_{y}$, we minimize $L_{y}\left(g_{y} ; f_{y}\right)$, because $L_{y}\left(g_{y}\right)$ is independent of $f_{y}$.

For the true distribution $q_{y}$ and the parametric model $p_{y}(\boldsymbol{\theta})$, we consider the minimization of $D_{y}\left(q_{y} ; p_{y}(\boldsymbol{\theta})\right)$ with respect to $\boldsymbol{\theta}$. The optimal parameter value is defined by

$$
\overline{\boldsymbol{\theta}}_{y}=\arg \min _{\boldsymbol{\theta} \in \Theta} L_{y}\left(q_{y} ; p_{y}(\boldsymbol{\theta})\right)
$$

This minimization is interpreted geometrically as a "projection" of $q_{y}$ to the model manifold $M_{y}\left(p_{y}\right)$ as illustrated in Fig. 1a. Let $M_{y}\left(p_{y}\right)=\left\{p_{y}(\boldsymbol{\theta}): \forall \boldsymbol{\theta} \in \Theta\right\}$ be the set of $p_{y}(\boldsymbol{\theta})$ with all possible parameter values. Then, the projection is defined as:

$$
\min _{f_{y} \in M_{y}\left(p_{y}\right)} D_{y}\left(q_{y} ; f_{y}\right)=D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right) .
$$

The projection $p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ is the best approximation of $q_{y}$ in $M_{y}\left(p_{y}\right)$ when the discrepancy is measured by the Kullback-Leibler divergence. We assume that the parametric model is generally misspecified and $q_{y} \notin M_{y}\left(p_{y}\right)$. Later, we also consider the situation where the parametric model is correctly specified and $q_{y} \in M_{y}\left(p_{y}\right)$. In the correctly specified case, $\overline{\boldsymbol{\theta}}_{y}$ is the true parameter value in the sense that $q_{y}=p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$.

Similar to the optimal parameter value, the maximum likelihood estimator is interpreted as a projection of $\hat{q}_{y}$ to $M_{y}\left(p_{y}\right)$. Let $\hat{q}_{y}(\boldsymbol{y})=\frac{1}{n} \sum_{t=1}^{n} \delta\left(\boldsymbol{y}-\boldsymbol{y}_{t}\right)$ be the empirical distribution of $\boldsymbol{y}$ for the observed incomplete data $\boldsymbol{y}_{1}, \ldots, \boldsymbol{y}_{n}$. Here, $\delta(\cdot)$ denotes the Dirac delta function for continuous random variables, or is simply the indicator function for discrete random variables such that $\delta\left(\boldsymbol{y}-\boldsymbol{y}_{t}\right)=1$ for $\boldsymbol{y}=\boldsymbol{y}_{t}$ and $\delta\left(\boldsymbol{y}-\boldsymbol{y}_{t}\right)=0$ otherwise. Then, we can write $\ell_{y}(\boldsymbol{\theta})=-n L_{y}\left(\hat{q}_{y} ; p_{y}(\boldsymbol{\theta})\right)$. Thus,

$$
\hat{\boldsymbol{\theta}}_{y}=\arg \min _{\boldsymbol{\theta} \in \Theta} L_{y}\left(\hat{q}_{y} ; p_{y}(\boldsymbol{\theta})\right) .
$$

We assume the regularity conditions of White (1982) for consistency and asymptotic normality of $\hat{\boldsymbol{\theta}}_{y}$. More specifically, we assume all the regularity conditions (A1) to (A6) for the true distribution $q_{y}$ and the model distribution $p_{y}(\boldsymbol{\theta})$. In particular, $\overline{\boldsymbol{\theta}}_{y}$ is determined uniquely (i.e., identifiable) and is interior to the parameter space $\Theta$. We assume that $I_{y}(\boldsymbol{\theta}), G_{y}\left(q_{y} ; \boldsymbol{\theta}\right)$ and $H_{y}\left(q_{y} ; \boldsymbol{\theta}\right)$ defined below are nonsingular in the neighborhood of $\overline{\boldsymbol{\theta}}_{y}$. Then, White (1982) showed that, as $n \rightarrow \infty$ asymptotically, $\hat{\boldsymbol{\theta}}_{y} \xrightarrow{\text { a.s. }} \overline{\boldsymbol{\theta}}_{y}$ and

$$
\sqrt{n}\left(\hat{\boldsymbol{\theta}}_{y}-\overline{\boldsymbol{\theta}}_{y}\right) \xrightarrow{d} N\left(\mathbf{0}, H_{y}^{-1} G_{y} H_{y}^{-1}\right) .
$$

The matrices are defined as $G_{y}=G_{y}\left(q_{y} ; \overline{\boldsymbol{\theta}}_{y}\right)$ and $H_{y}=H_{y}\left(q_{y} ; \overline{\boldsymbol{\theta}}_{y}\right)$, where

$$
\begin{aligned}
G_{y}\left(g_{y} ; \boldsymbol{\theta}\right) & =\int g_{y}(\boldsymbol{y}) \frac{\partial \log p_{y}(\boldsymbol{y} ; \boldsymbol{\theta})}{\partial \boldsymbol{\theta}} \frac{\partial \log p_{y}(\boldsymbol{y} ; \boldsymbol{\theta})}{\partial \boldsymbol{\theta}^{T}} \mathrm{~d} \boldsymbol{y} \\
H_{y}\left(g_{y} ; \boldsymbol{\theta}\right) & =-\int g_{y}(\boldsymbol{y}) \frac{\partial^{2} \log p_{y}(\boldsymbol{y} ; \boldsymbol{\theta})}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{T}} \mathrm{~d} \boldsymbol{y}
\end{aligned}
$$

In the case of the correct specification $q_{y}=p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$, the matrices become $G_{y}=H_{y}= I_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$.

## 3 Complete-data divergence

Here, we review Kullback-Leibler divergence for complete data when only incomplete data can be observed (Csiszár and Tusnády 1984; Amari 1995).

### 3.1 Projection to the model manifold

Let $g_{x}$ and $f_{x}$ be the arbitrary probability distributions of complete data. The completedata Kullback-Leibler divergence from $g_{x}$ to $f_{x}$ is

$$
D_{x}\left(g_{x} ; f_{x}\right)=-\int g_{x}(\boldsymbol{x})\left(\log f_{x}(\boldsymbol{x})-\log g_{x}(\boldsymbol{x})\right) \mathrm{d} \boldsymbol{x}
$$

All the arguments of incomplete data in Sect. 2 apply to complete data by replacing $\boldsymbol{y}$ with $\boldsymbol{x}$ in the notation. For example, we write $D_{x}\left(g_{x} ; f_{x}\right)=L_{x}\left(g_{x} ; f_{x}\right)-L_{x}\left(g_{x}\right)$ with $L_{x}\left(g_{x} ; f_{x}\right)=-\int g_{x}(\boldsymbol{x}) \log f_{x}(\boldsymbol{x}) d \boldsymbol{x}$ and $L_{x}\left(g_{x}\right)=L_{x}\left(g_{x} ; g_{x}\right)$. The projection of $q_{x}$ to the model manifold $M_{x}\left(p_{x}\right)=\left\{p_{x}(\boldsymbol{\theta}): \forall \boldsymbol{\theta} \in \Theta\right\}$ is defined as:

$$
\min _{f_{x} \in M_{x}\left(p_{x}\right)} D_{x}\left(q_{x} ; f_{x}\right)=D_{x}\left(q_{x} ; p_{x}\left(\overline{\boldsymbol{\theta}}_{x}\right)\right)
$$

with $\overline{\boldsymbol{\theta}}_{x}=\arg \min _{\boldsymbol{\theta}} L_{x}\left(q_{x} ; p_{x}(\boldsymbol{\theta})\right)$. Figure 1 b shows a geometric illustration. Note that $\overline{\boldsymbol{\theta}}_{x} \neq \overline{\boldsymbol{\theta}}_{y}$ and $p_{x}\left(\overline{\boldsymbol{\theta}}_{x}\right) \neq p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ in general.

![](https://cdn.mathpix.com/cropped/e2300c0f-f565-4335-84c8-1adaece49016-06.jpg?height=603&width=1188&top_left_y=1214&top_left_x=166)
Fig. 1 a Space of incomplete-data probability distributions. Projection from $q_{y}$ to the model manifold $M_{y}\left(p_{y}\right)$ (arrow with a solid line), and that from $\hat{q}_{y}$ (arrow with a broken line) using Eqs. (2) and (3) in Sect. 2, respectively. The dotted line indicates $D_{y}\left(q_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)$, which is the loss function for risk ${ }_{y ; y}$. b Space of complete-data probability distributions. Projection from $q_{x}$ to the model manifold $M_{x}\left(p_{x}\right)$ using Eq. (5) in Sect. 3.1. Projection from $p_{x}(\boldsymbol{\theta})$ to the data manifold $S_{x}\left(q_{y}\right)$ using Eq. (9) in Sect. 3.2. Alternating projections between the two manifolds using Eq. (10) in Sect. 3.3. The dotted line indicates $D_{x}\left(q_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)$, which is the loss function for $\operatorname{risk}_{x ; y}$. The bold segment indicates $D_{x}\left(q_{x} ; p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}\right)$, which is assumed to be zero in (15).

### 3.2 Projection to the data manifold

The following simple lemma helps understand how the incomplete-data divergence and the complete-data divergence are related.

Lemma 1 For two distributions $g_{x}(\boldsymbol{x})$ and $f_{x}(\boldsymbol{x})$, we have

$$
D_{x}\left(g_{x} ; f_{x}\right)=D_{x}\left(g_{x} ; f_{z \mid y} g_{y}\right)+D_{y}\left(g_{y} ; f_{y}\right)
$$

where $f_{z \mid y} g_{y}$ represents the distribution $f_{z \mid y}(\boldsymbol{z} \mid \boldsymbol{y}) g_{y}(\boldsymbol{y})$. Therefore, the difference of the two divergences is $D_{x}\left(g_{x} ; f_{x}\right)-D_{y}\left(g_{y} ; f_{y}\right)=D_{x}\left(g_{x} ; f_{z \mid y} g_{y}\right)$, which is zero if $g_{z \mid y}=f_{z \mid y}$. For an arbitrary distribution $h_{x}(\boldsymbol{x})$, the last term in (6) is expressed as:

$$
D_{y}\left(g_{y} ; f_{y}\right)=D_{x}\left(h_{z \mid y} g_{y} ; h_{z \mid y} f_{y}\right)
$$

In particular, choosing $h_{x}=f_{x}$ gives $D_{y}\left(g_{y} ; f_{y}\right)=D_{x}\left(f_{z \mid y} g_{y} ; f_{x}\right)$, and

$$
D_{x}\left(g_{x} ; f_{x}\right)=D_{x}\left(g_{x} ; f_{z \mid y} g_{y}\right)+D_{x}\left(f_{z \mid y} g_{y} ; f_{x}\right) .
$$

We consider the set of all probability distributions $g_{x}$ with the same marginal distribution $g_{y}=q_{y}$ for a specified $q_{y}$. This set is denoted as $S_{x}\left(q_{y}\right)=\left\{g_{z \mid y} q_{y}\right.$ : $\left.\forall g_{z \mid y}\right\}$. Note that the elements of $S_{x}\left(q_{y}\right)$ are written as $g_{z \mid y} q_{y}$ with arbitrary $g_{z \mid y}$ because $\int g_{z \mid y}(\boldsymbol{z} \mid \boldsymbol{y}) q_{y}(\boldsymbol{y}) d \boldsymbol{z}=q_{y}(\boldsymbol{y})$. Equations (88) and (57) in Amari (1995) are $S_{x}\left(\hat{q}_{y}\right)$ and its restriction to a finite dimensional model, respectively, and are called the observed data (sub)manifold there. Here, we call $S_{x}\left(q_{y}\right)$ the expected data manifold and $S_{x}\left(\hat{q}_{y}\right)$ the observed data manifold, although it may be abuse of the word "manifold" for subsets with infinite dimensions.

The projection of $p_{x}(\boldsymbol{\theta})$ to $S_{x}\left(q_{y}\right)$ should be defined to minimize the complete-data divergence over $S_{x}\left(q_{y}\right)$, but the roles of $g_{x}$ and $f_{x}$ in $D_{x}\left(g_{x} ; f_{x}\right)$ are exchanged from those of (5). We minimize $D_{x}\left(g_{x} ; p_{x}(\boldsymbol{\theta})\right)$ over $g_{x} \in S_{x}\left(q_{y}\right)$. By letting $g_{x} \in S_{x}\left(q_{y}\right)$ and $f_{x}=p_{x}(\boldsymbol{\theta})$ in (6),

$$
D_{x}\left(g_{x} ; p_{x}(\boldsymbol{\theta})\right)=D_{x}\left(g_{z \mid y} q_{y} ; p_{z \mid y}(\boldsymbol{\theta}) q_{y}\right)+D_{y}\left(q_{y} ; p_{y}(\boldsymbol{\theta})\right),
$$

which is minimized when $g_{z \mid y}=p_{z \mid y}(\boldsymbol{\theta})$. Therefore, the projection gives the minimum value as:

$$
\min _{g_{x} \in S_{x}\left(q_{y}\right)} D_{x}\left(g_{x} ; p_{x}(\boldsymbol{\theta})\right)=D_{y}\left(q_{y} ; p_{y}(\boldsymbol{\theta})\right) .
$$

Using (8), the minimum value can also be written as $D_{y}\left(q_{y} ; p_{y}(\boldsymbol{\theta})\right)=D_{x}\left(p_{z \mid y}(\boldsymbol{\theta}) q_{y}\right.$; $p_{x}(\boldsymbol{\theta})$ ).

### 3.3 Alternating projections between the two manifolds

The optimal parameter $\overline{\boldsymbol{\theta}}_{y}$ of the incomplete data is interpreted as a dual or alternate minimization problem of complete-data divergence. By minimizing (9) over $\boldsymbol{\theta} \in \Theta$, we define the alternating projections between $S_{x}\left(q_{y}\right)$ and $M_{x}\left(p_{x}\right)$ as:

$$
\min _{f_{x} \in M_{x}\left(p_{x}\right)} \min _{g_{x} \in S_{x}\left(q_{y}\right)} D_{x}\left(g_{x} ; f_{x}\right)=D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right),
$$

where the minimum is attained by $g_{x}=p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}$ and $f_{x}=p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)$. See Eq. (65) in Amari (1995). This implies that $p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}$ is the best approximation of $q_{x}$ when the two manifolds $S_{x}\left(q_{y}\right)$ and $M_{x}\left(p_{x}\right)$ are known, while $p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ is the best approximation of $q_{x}$ in $M_{x}\left(p_{x}\right)$. This interpretation is the key to understanding our problem.

The above-mentioned geometrical interpretation corresponds to the well-known fact that the EM algorithm of Dempster et al. (1977) is alternating projections between $S_{x}\left(\hat{q}_{y}\right)$ and $M_{x}\left(p_{x}\right)$. See Csiszár and Tusnády (1984), Byrne (1992), Amari (1995), and Ip and Lalwani (2000). Starting from the initial value $\boldsymbol{\theta}^{(1)}$, the EM algorithm computes a sequence of the parameter values $\left\{\boldsymbol{\theta}^{(s)} ; s=1,2 \ldots\right\}$ by the updating formula $\boldsymbol{\theta}^{(s+1)}=\arg \max _{\boldsymbol{\theta} \in \Theta} Q\left(\boldsymbol{\theta} ; \boldsymbol{\theta}^{(s)}\right)$. It follows from $L_{x}\left(p_{z \mid y}\left(\boldsymbol{\theta}_{1}\right) \hat{q}_{y} ; p_{x}\left(\boldsymbol{\theta}_{2}\right)\right)= -Q\left(\boldsymbol{\theta}_{2} ; \boldsymbol{\theta}_{1}\right) / n$ that

$$
\boldsymbol{\theta}^{(s+1)}=\arg \min _{\boldsymbol{\theta} \in \Theta} L_{x}\left(p_{z \mid y}\left(\boldsymbol{\theta}^{(s)}\right) \hat{q}_{y} ; p_{x}(\boldsymbol{\theta})\right),
$$

meaning $p_{x}\left(\boldsymbol{\theta}^{(s+1)}\right)$ is the projection from $p_{z \mid y}\left(\boldsymbol{\theta}^{(s)}\right) \hat{q}_{y}$ to $M_{x}\left(p_{x}\right)$. Alternatively, $p_{z \mid y}\left(\boldsymbol{\theta}^{(s)}\right) \hat{q}_{y}$ is the projection from $p_{x}\left(\boldsymbol{\theta}^{(s)}\right)$ to $S_{x}\left(\hat{q}_{y}\right)$. Thus, the converging point of the alternating projections satisfies

$$
\hat{\boldsymbol{\theta}}_{y}=\arg \min _{\boldsymbol{\theta} \in \Theta} L_{x}\left(p_{z \mid y}\left(\hat{\boldsymbol{\theta}}_{y}\right) \hat{q}_{y} ; p_{x}(\boldsymbol{\theta})\right)
$$

## 4 Risk functions for model selection

By looking at the incomplete-data distributions, the discrepancy between the true distribution $q_{y}$ and our estimation $p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)$ is measured by the incomplete-data divergence $D_{y}\left(q_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)$. If we take it as the loss function, the expected loss-function, or the risk function, will measure the discrepancy in the long run. Then, AIC and its variants are derived as estimators of

$$
\operatorname{risk}_{y ; y}=E\left\{D_{y}\left(q_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)\right\} .
$$

The expectation is evaluated with respect to $q_{x}$, although it involves only $q_{y}$ here. This is the standard approach in the literature (Akaike 1974; Bozdogan 1987; Burnham and Anderson 2002; Konishi and Kitagawa 2008).

Shimodaira (1994) and Cavanaugh and Shumway (1998) proposed another approach, which employs the complete-data divergence $D_{x}\left(q_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)$ to measure the discrepancy between the complete-data distributions $q_{x}$ and $p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)$. Using the complete-data divergence as the loss function, the risk function becomes

$$
\operatorname{risk}_{x ; y}=E\left\{D_{x}\left(q_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)\right\} .
$$

The first suffix $\boldsymbol{x}$ indicates the random variable for the loss function, while the second suffix $\boldsymbol{y}$ indicates the random variable for the observation.

However, estimating (13) is difficult. The complete-data empirical distribution $\hat{q}_{x}(\boldsymbol{x})=\frac{1}{n} \sum_{t=1}^{n} \delta\left(\boldsymbol{x}-\boldsymbol{x}_{t}\right)$ is unknown; we only know that $\hat{q}_{x}$ is somewhere in the observed data manifold $S_{x}\left(\hat{q}_{y}\right)$. Considering the limiting situation of $n \rightarrow \infty$, we may only know that the true distribution is somewhere in the expected data manifold: $q_{x} \in S_{x}\left(q_{y}\right)$. Then, the best substitute for $q_{x}$ is

$$
q_{x}=p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}
$$

as suggested by (10) from the viewpoint of the alternating projections in Sect. 3.3. To estimate (13), we assume that (14) holds in this paper. This assumption is rephrased as:

$$
D_{x}\left(q_{x} ; p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}\right)=0
$$

or equivalently

$$
q_{z \mid y}=p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right)
$$

implying that $p_{z \mid y}(\boldsymbol{\theta})$ is correctly specified for $q_{z \mid y}$ and that $\overline{\boldsymbol{\theta}}_{x}=\overline{\boldsymbol{\theta}}_{y}$, because the two projections from $q_{x}$ and $p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}$ to $M_{x}\left(p_{x}\right)$ become identical as illustrated in Fig. 1b. Because it is impossible to know how much $q_{z \mid y}$ actually deviates from $p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ when $Z=\left(\boldsymbol{z}_{1}, \ldots, \boldsymbol{z}_{n}\right)$ is missing completely, we assume (15) in the following argument to derive $\mathrm{AIC}_{x ; y}$. Note that assumption (15) holds with $\overline{\boldsymbol{\theta}}_{x}=\overline{\boldsymbol{\theta}}_{y}=\boldsymbol{\theta}_{0}$ in the case of the correct specification where $q_{x}=p_{x}\left(\boldsymbol{\theta}_{0}\right)$.

We are now ready to derive $\mathrm{AIC}_{x ; y}$ as an estimator of $2 n$ risk $_{x ; y}$. The arguments in Lemma 2 and Theorem 1 almost duplicate that used to derive TIC mentioned in Burnham and Anderson (2002) and Konishi and Kitagawa (2008). However, it should be noted that in Lemma 2 the first term of risk ${ }_{x ; y}$ is expressed by the incomplete-data divergence instead of the complete-data divergence. A point for proving the lemma is that

$$
D_{x}\left(q_{x} ; p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)=D_{x}\left(q_{x} ; p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}\right)+D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)=D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)
$$

which follows from Lemma 1 and the assumption (15). $D_{x}\left(q_{x} ; p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)$ on the lefthand side is the amount of misspecification of $p_{x}(\boldsymbol{\theta})$, and can be decomposed into two parts: $D_{x}\left(q_{x} ; p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}\right)$ and $D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)$, which are the contribution of $p_{z \mid y}(\boldsymbol{\theta})$ and $p_{y}(\boldsymbol{\theta})$, respectively. To estimate (13), instead of estimating $D_{x}\left(q_{x} ; p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}\right)$, we ignore it.

Lemma 2 Assume the regularity conditions of White (1982) mentioned in Sect. 2, and also assume that (15) holds. Then, the expected loss is asymptotically expanded as:

$$
\operatorname{risk}_{x ; y}=D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)+\frac{1}{2 n} \operatorname{tr}\left(H_{x} H_{y}^{-1} G_{y} H_{y}^{-1}\right)+O\left(n^{-3 / 2}\right) .
$$

The matrices $G_{y}$ and $H_{y}$ are those defined in Sect. 2, and $H_{x}=H_{x}\left(p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y} ; \overline{\boldsymbol{\theta}}_{y}\right)$ with

$$
H_{x}\left(g_{x} ; \boldsymbol{\theta}\right)=-\int g_{x}(\boldsymbol{x}) \frac{\partial^{2} \log p_{x}(\boldsymbol{x} ; \boldsymbol{\theta})}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{T}} d \boldsymbol{x}
$$

The dominant term in (17) is also expressed as $D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)=L_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)- L_{y}\left(q_{y}\right)$ using the cross-entropy.

## 5 Information criteria

Let us define an information criterion as an estimator of $\operatorname{risk}_{x ; y}$.

$$
\widehat{\operatorname{risk}}_{x ; y}=L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)-L_{y}\left(q_{y}\right)+\frac{1}{2 n} \operatorname{tr}\left(G_{y} H_{y}^{-1}\right)+\frac{1}{2 n} \operatorname{tr}\left(H_{x} H_{y}^{-1} G_{y} H_{y}^{-1}\right),
$$

where the matrices $G_{y}, H_{y}$ and $H_{x}$ may be replaced by their consistent estimators with error $O_{p}\left(n^{-1 / 2}\right)$. When $\boldsymbol{x} \equiv \boldsymbol{y}$, (18) reduces to

$$
\widehat{\operatorname{risk}}_{y ; y}=L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)-L_{y}\left(q_{y}\right)+\frac{1}{n} \operatorname{tr}\left(G_{y} H_{y}^{-1}\right),
$$

which corresponds to the Takeuchi information criterion (TIC) for estimating risk ${ }_{y ; y}$ mentioned in Burnham and Anderson (2002) and Konishi and Kitagawa (2008). In model selection, we ignore $L_{y}\left(q_{y}\right)$, because all candidate models have the same value. The first term $L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)=-\ell_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right) / n$ of order $O_{p}(1)$ measures the goodness of fit, while the last two terms of order $O\left(n^{-1}\right)$ are interpreted as the penalty of model complexity. Our estimator is justified by the following theorem.

Theorem 1 Assume the regularity conditions of White (1982) mentioned in Sect. 2, and also assume that (15) holds. Then, we have

$$
L_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)=E\left\{L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)\right\}+\frac{1}{2 n} \operatorname{tr}\left(G_{y} H_{y}^{-1}\right)+O\left(n^{-3 / 2}\right),
$$

and therefore

$$
\left.E \widehat{\operatorname{risk}}_{x ; y}\right\}=\operatorname{risk}_{x ; y}+O\left(n^{-3 / 2}\right) .
$$

Thus, the estimator is unbiased asymptotically up to terms of order $O\left(n^{-1}\right)$.
In the case of the correct specification where $q_{y}=p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ for the incomplete-data distribution, we have $G_{y}=H_{y}=I_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$, and the information matrix is consistently estimated by $\boldsymbol{I}_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)$. Assuming (15), this implies that $q_{x}=p_{x}\left(\overline{\boldsymbol{\theta}}_{x}\right)$ is correctly specified for the complete-data distribution. Hence, $H_{x}=I_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ is consistently estimated by $I_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)$. For model selection, we assume that $p_{y}(\boldsymbol{\theta})$ is misspecified for $q_{y}$ in general. However, these equations may approximately hold if $p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ is a good approximation
of $q_{y}$. By substituting $G_{y} \approx H_{y} \approx I_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ and $H_{x} \approx I_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ into (18) and (19), we have

$$
\widehat{\operatorname{risk}}_{x ; y} \approx L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)-L_{y}\left(q_{y}\right)+\frac{d}{2 n}+\frac{1}{2 n} \operatorname{tr}\left(I_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right) I_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)^{-1}\right),
$$

and

$$
\widehat{\operatorname{risk}}_{y ; y} \approx L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)-L_{y}\left(q_{y}\right)+\frac{d}{n}
$$

where $L_{y}\left(q_{y}\right)$ is ignored for model selection. Multiplying by $2 n$ converts these approximations to $\mathrm{AIC}_{x ; y}$ and AIC, respectively.

## 6 PDIO and AICcd

The idea behind the derivation of PDIO and AIC ${ }_{c d}$ is to replace $\hat{q}_{x}$ by

$$
\hat{q}_{x}=p_{z \mid y}\left(\hat{\boldsymbol{\theta}}_{y}\right) \hat{q}_{y}
$$

This implies (14) by considering the limiting situation of $n \rightarrow \infty$. Thus, the assumption for PDIO and $\mathrm{AIC}_{c d}$ is stronger than the assumption for $\mathrm{AIC}_{x ; y}$. Substituting (22) into the complete-data MLE gives

$$
\hat{\boldsymbol{\theta}}_{x}=\arg \min _{\boldsymbol{\theta} \in \Theta} L_{x}\left(\hat{q}_{x} ; p_{x}(\boldsymbol{\theta})\right)
$$

Comparing (23) with (11) gives $\hat{\boldsymbol{\theta}}_{x}=\hat{\boldsymbol{\theta}}_{y}$. Therefore, there should not be any missing data, or at least $p_{z \mid y}(\boldsymbol{\theta})$ should not involve the parameter $\boldsymbol{\theta}$. Consequently, AIC, PDIO, $\mathrm{AIC}_{c d}$, and $\mathrm{AIC}_{x ; y}$ are equivalent when PDIO and $\mathrm{AIC}_{c d}$ are justified under (22).

Although assumption (22) is too strong to work with, it is interesting to see how PDIO and AIC ${ }_{c d}$ would be derived if (22) is formally accepted. The argument below to derive PDIO and $\mathrm{AIC}_{c d}$ is rather confusing because $\hat{q}_{x}$ is interpreted interchangeably as the complete-data empirical distribution or the right-hand side of (22).

By a similar argument to the proof of Theorem 1, the Taylor expansion of $L_{x}\left(\hat{q}_{x} ; p_{x}(\boldsymbol{\theta})\right)$ around $\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}_{y}$ is

$$
L_{x}\left(\hat{q}_{x} ; p_{x}(\boldsymbol{\theta})\right)=L_{x}\left(\hat{q}_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)+\frac{1}{2}\left(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}}_{y}\right)^{T} \hat{H}_{x}\left(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}}_{y}\right)+O_{p}\left(n^{-3 / 2}\right)
$$

with $\hat{H}_{x}=H_{x}\left(\hat{q}_{x} ; \hat{\boldsymbol{\theta}}_{y}\right)$. Its expectation with $\boldsymbol{\theta}=\overline{\boldsymbol{\theta}}_{y}$ gives

$$
L_{x}\left(q_{x} ; p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)=E\left\{L_{x}\left(\hat{q}_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)\right\}+\frac{1}{2 n} \operatorname{tr}\left(H_{x} H_{y}^{-1} G_{y} H_{y}^{-1}\right)+O\left(n^{-3 / 2}\right)
$$

This corresponds to (20) of Theorem 1. Noticing (16) and thus, $D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)= L_{x}\left(q_{x} ; p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)-L_{x}\left(q_{x}\right)$, and then substituting (25) into (17) gives the estimator of risk $_{x ; y}$ unbiased up to $O\left(n^{-1}\right)$ under (22) as:

$$
\widehat{\operatorname{risk}}_{x ; y}=L_{x}\left(\hat{q}_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)-L_{x}\left(q_{x}\right)+\frac{1}{n} \operatorname{tr}\left(H_{x} H_{y}^{-1} G_{y} H_{y}^{-1}\right) .
$$

The goodness of fit term is $L_{x}\left(p_{z \mid y}\left(\hat{\boldsymbol{\theta}}_{y}\right) \hat{q}_{y} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)=-Q\left(\hat{\boldsymbol{\theta}}_{y} ; \hat{\boldsymbol{\theta}}_{y}\right) / n$ under (22). Therefore, (26) gives $\mathrm{AIC}_{c d}$ by the same approximation used to derive $\mathrm{AIC}_{x ; y}$.

In Cavanaugh and Shumway (1998), for evaluating (3.15) there, they assumed that $E\left\{Q\left(\boldsymbol{\theta}_{0} ; \hat{\boldsymbol{\theta}}_{y}\right)\right\} \approx E\left\{Q\left(\boldsymbol{\theta}_{0} ; \boldsymbol{\theta}_{0}\right)\right\}$ or $E\left(L_{x}\left(p_{z \mid y}\left(\hat{\boldsymbol{\theta}}_{y}\right) \hat{q}_{y} ; p_{x}\left(\boldsymbol{\theta}_{0}\right)\right)\right) \approx L_{x}\left(p_{z \mid y}\left(\boldsymbol{\theta}_{0}\right) q_{y} ;\right. p_{x}\left(\boldsymbol{\theta}_{0}\right)$ ) under the correct specification $q_{x}=p_{x}\left(\boldsymbol{\theta}_{0}\right)$. The equality holds exactly under (22) because $E\left(L_{x}\left(\hat{q}_{x} ; p_{x}\left(\boldsymbol{\theta}_{0}\right)\right)\right)=L_{x}\left(q_{x} ; p_{x}\left(\boldsymbol{\theta}_{0}\right)\right)$ if $\hat{q}_{x}$ is interpreted as the empirical distribution. Unfortunately, the difference is $E\left\{Q\left(\boldsymbol{\theta}_{0} ; \hat{\boldsymbol{\theta}}_{y}\right)\right\}-E\left\{Q\left(\boldsymbol{\theta}_{0} ; \boldsymbol{\theta}_{0}\right)\right\}=O(1)$ in general without assuming (22), leading to the bias of $\mathrm{AIC}_{c d}$ even when (15) holds.

In Shimodaira (1994), (3.5) corresponds to our (24), where $\hat{\boldsymbol{\theta}}_{x}=\hat{\boldsymbol{\theta}}_{y}$ is assumed implicitly to ignore the first derivative. Although $L_{x}\left(\hat{q}_{x}\right)$ diverges for continuous random variable $\boldsymbol{x}, D_{x}\left(\hat{q}_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)=L_{x}\left(\hat{q}_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)-L_{x}\left(\hat{q}_{x}\right)$ is formally considered. Similar to (16), we then have $D_{x}\left(\hat{q}_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)=D_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)$ in (3.6) there. From this argument, the goodness of fit term of (26) is $L_{x}\left(\hat{q}_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)= L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)+L_{x}\left(\hat{q}_{x}\right)-L_{y}\left(\hat{q}_{y}\right)$, where $L_{x}\left(\hat{q}_{x}\right)-L_{y}\left(\hat{q}_{y}\right)$ is independent of the model specification if $\hat{q}_{x}$ is interpreted as the empirical distribution. Therefore, (26) gives PDIO because $L_{x}\left(\hat{q}_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)$ can be replaced with $L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)$ for model selection.

## 7 Simulation study

### 7.1 Simulation 1

To verify Theorem 1, we performed a simulation study of the two-component normal mixture model defined as follows. Let $z \in\{1,2\}$ be a discrete random variable for the component label, and $y \in \mathbb{R}$ be a continuous random variable for the observation. The distribution of $z$ is $P(z=i)=\pi_{i}$ and the conditional distribution of $y$ given $z=i$ is the normal distribution with mean $\mu_{i}$ and variance $\sigma_{i}^{2}$. The true parameter for data generation is specified as $\boldsymbol{\theta}_{0}^{T}=\left(\pi_{1}, \mu_{1}, \mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}\right)=\left(0.6,-1,1,0.7^{2}, 0.7^{2}\right)$. We consider two candidate models for selection. Model 1 is a two-component normal mixture model with a constraint $\sigma_{1}^{2}=\sigma_{2}^{2}(d=4)$, whereas Model 2 is the same model without the constraint $(d=5)$. Because these two models are correctly specified, (15) holds. However, (22) obviously does not.

We generated $B=4000$ datasets with sample size $n=100,200,500,1000,2000$, 5000,10000 . They are denoted as $X^{(b)}=\left(\boldsymbol{x}_{1}^{(b)}, \ldots, \boldsymbol{x}_{n}^{(b)}\right), b=1, \ldots, B$. We also generated datasets of sample size $\tilde{n}=15000$, which are denoted as $\tilde{X}^{(b)}=\left(\tilde{\boldsymbol{x}}_{1}^{(b)}, \ldots, \tilde{\boldsymbol{x}}_{\tilde{n}}^{(b)}\right)$ for computing the loss functions. For each $X^{(b)}= \left(Y^{(b)}, Z^{(b)}\right)$ and Model $k, k=1,2$, we computed the information criteria $\operatorname{AIC}\left(Y^{(b)}, k\right), \operatorname{PDIO}\left(Y^{(b)}, k\right), \operatorname{AIC}_{c d}\left(Y^{(b)}, k\right), \operatorname{AIC}_{x ; y}\left(Y^{(b)}, k\right)$, and the loss functions $\operatorname{loss}_{y ; y}\left(Y^{(b)}, k\right)=L_{y}\left(q_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}^{(b)}\right)\right), \operatorname{loss}_{x ; y}\left(X^{(b)}, k\right)=L_{x}\left(q_{x} ; p_{x}\left(\hat{\boldsymbol{\theta}}_{y}^{(b)}\right)\right)$, where $\hat{\boldsymbol{\theta}}_{y}^{(b)}$ is computed from $Y^{(b)}$. In the formulas below, $: \approx$ denotes that the expectation on the
left-hand side is computed numerically by the simulation on the right-hand side. The loss functions are computed numerically by

$$
\begin{aligned}
& \operatorname{loss}_{y ; y}\left(Y^{(b)}, k\right): \approx-\frac{1}{\tilde{n}} \sum_{t=1}^{\tilde{n}} \log p_{y}\left(\tilde{\boldsymbol{y}}_{t}^{(b)} ; \hat{\boldsymbol{\theta}}_{y}^{(b)}\right), \\
& \operatorname{loss}_{x ; y}\left(X^{(b)}, k\right): \approx-\frac{1}{\tilde{n}} \sum_{t=1}^{\tilde{n}} \log p_{x}\left(\tilde{\boldsymbol{x}}_{t}^{(b)} ; \hat{\boldsymbol{\theta}}_{y}^{(b)}\right),
\end{aligned}
$$

where $p_{x}, p_{y}$, and $\hat{\boldsymbol{\theta}}_{y}^{(b)}$ are for Model $k$. Then, the expectation with respect to $q_{x}= p_{x}\left(\boldsymbol{\theta}_{0}\right)$ is computed by the simulation average. For example,

$$
\begin{gathered}
E(\Delta \mathrm{AIC}): \approx \frac{1}{B} \sum_{b=1}^{B}\left(\operatorname{AIC}\left(Y^{(b)}, 1\right)-\operatorname{AIC}\left(Y^{(b)}, 2\right)\right), \\
\Delta \operatorname{risk}_{x ; y}: \approx \frac{1}{B} \sum_{b=1}^{B}\left(\operatorname{loss}_{x ; y}\left(X^{(b)}, 1\right)-\operatorname{loss}_{x ; y}\left(X^{(b)}, 2\right)\right) .
\end{gathered}
$$

This Monte Carlo method calculates the expectation accurately for sufficiently large $\tilde{n}$ and $B$.

The result shown in Table 1 verifies Theorem 1. For sufficiently large $n, E(\Delta \mathrm{AIC})= 2 n \Delta \operatorname{risk}_{y ; y}$ and $E\left(\Delta \operatorname{AIC}_{x ; y}\right)=2 n \Delta \operatorname{risk}_{x ; y}$ hold very well. On the other hand, $E(\Delta \mathrm{PDIO})$ differs significantly from $2 n \Delta \mathrm{risk}_{y ; y}$ and $2 n \Delta \mathrm{risk}_{x ; y}$. Thus, PDIO is not a good estimator of either of these risk functions. In addition, the expected value of $\mathrm{AIC}_{c d}$ is similar to that of PDIO, but its variation is larger than PDIO, as seen in the standard errors.

Let us consider the difference PDIO - $\mathrm{AIC}_{c d}$
$\operatorname{diff}\left(Y, \hat{\boldsymbol{\theta}}_{y}\right)=2 Q\left(\hat{\boldsymbol{\theta}}_{y} ; \hat{\boldsymbol{\theta}}_{y}\right)-2 \ell_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)=2 \sum_{t=1}^{n} \int p_{z \mid y}\left(\boldsymbol{z} \mid \boldsymbol{y}_{t} ; \hat{\boldsymbol{\theta}}_{y}\right) \log p_{z \mid y}\left(\boldsymbol{z} \mid \boldsymbol{y}_{t} ; \hat{\boldsymbol{\theta}}_{y}\right) d \boldsymbol{z}$,
and its difference between the two models, which is denoted as $\Delta \operatorname{diff}\left(Y, \hat{\boldsymbol{\theta}}_{y}\right)= \Delta \mathrm{PDIO}-\Delta \operatorname{AIC}_{c d} . \Delta \operatorname{diff}\left(Y, \hat{\boldsymbol{\theta}}_{y}\right)$ and $E\left(\Delta \operatorname{diff}\left(Y, \hat{\boldsymbol{\theta}}_{y}\right)\right)$ can be very large, and they are $O(n)$ under model misspecification. If (15) holds, as is the case of Table 1, $E\left(\operatorname{diff}\left(Y, \overline{\boldsymbol{\theta}}_{y}\right)\right)=2 n \int q_{x}(x) \log q_{z \mid y}(z \mid y) d x$ is independent of the model. Therefore, the difference becomes smaller; $\Delta \operatorname{diff}\left(Y, \hat{\boldsymbol{\theta}}_{y}\right)=O_{p}(\sqrt{n})$ and $E\left(\Delta \operatorname{diff}\left(Y, \hat{\boldsymbol{\theta}}_{y}\right)\right)= O(1)$.

### 7.2 Simulation 2

We next performed a simulation study on the three-component normal mixture model to examine how well the information criteria work for model selection

Table 1 Expected values of the information criteria and the risk functions in Simulation 1
| $n$ | 100 | 200 | 500 | 1000 | 2000 | 5000 | 10000 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $E(\triangle \mathrm{AIC})$ | 0.810 | 0.898 | 0.982 | 0.978 | 0.986 | 0.982 | 1.04 |
|  | (0.027) | (0.025) | (0.023) | (0.023) | (0.023) | (0.023) | (0.022) |
| $E(\triangle \mathrm{PDIO})$ | 43.5 | 41.1 | 37.0 | 36.0 | 34.9 | 34.4 | 34.2 |
|  | (1.64) | (0.716) | (0.344) | (0.220) | (0.141) | (0.088) | (0.064) |
| $E\left(\Delta \mathrm{AIC}_{c d}\right)$ | 42.3 | 41.0 | 37.2 | 36.6 | 35.2 | 35.5 | 33.5 |
|  | (1.67) | (0.793) | (0.518) | (0.494) | (0.573) | (0.812) | (1.08) |
| $E\left(\Delta \mathrm{AIC}_{x ; y}\right)$ | 22.1 | 21.0 | 19.0 | 18.5 | 18.0 | 17.7 | 17.6 |
|  | (0.821) | (0.361) | (0.174) | (0.113) | (0.074) | (0.049) | (0.037) |
| $2 n \Delta$ risk $_{y ; y}$ | 1.83 | 1.47 | 1.15 | 1.08 | 1.03 | 1.02 | 0.967 |
|  | (0.052) | (0.040) | (0.030) | (0.027) | (0.026) | (0.030) | (0.033) |
| $2 n \Delta$ risk $_{x ; y}$ | 100.9 | 28.9 | 20.3 | 18.6 | 18.2 | 17.5 | 17.0 |
|  | (40.3) | (1.39) | (0.620) | (0.487) | (0.456) | (0.464) | (0.430) |


These values are differences between the two models with standard errors in parentheses

Table 2 Frequency of model selection in Simulation 2
|  | Model 1 ( $d=6$ ) | Model 2 ( $d=7$ ) | Model 3 ( $d=7$ ) | Model $4{ }^{\text {a }}$ ( $d=7$ ) | Model $5{ }^{\text {a }}$ ( $d=8$ ) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| AIC | 881 | 2419 | 262 | 5600 | 838 |
| PDIO | 5442 | 16 | 4 | 4534 | 4 |
| $\mathrm{AIC}_{c d}$ | 2063 | 2 | 974 | 6551 | 410 |
| $\mathrm{AIC}_{x ; y}$ | 3704 | 65 | 15 | 6190 | 26 |


${ }^{\mathrm{a}}$ Correctly specified model
in a practical situation where some candidate models do not satisfy assumption (15). The true parameter value is $\boldsymbol{\theta}_{0}^{T}=\left(\pi_{1}, \pi_{2}, \mu_{1}, \mu_{2}, \mu_{3}, \sigma_{1}^{2}, \sigma_{2}^{2}, \sigma_{3}^{2}\right)= \left(0.5,0.3,-2,0,3,0.7^{2}, 0.7^{2}, 1^{2}\right)$. We consider five candidates with the following constraints. Model 1 is $\sigma_{1}^{2}=\sigma_{2}^{2}=\sigma_{3}^{2}(d=6)$. Model 2 is $\sigma_{2}^{2}=\sigma_{3}^{2}(d=7)$. Model 3 is $\sigma_{1}^{2}=\sigma_{3}^{2}(d=7)$. Model 4 is $\sigma_{1}^{2}=\sigma_{2}^{2}(d=7)$, and Model 5 has no constraint ( $d=8$ ). Models 1, 2 and 3 are misspecified and do not satisfy (15). Models 4 and 5 are correctly specified and satisfy (15). None of the models satisfy (22). We have generated $B=10000$ datasets of $n=500$ and $\tilde{n}=2000$.

Table 2 shows the model selection results. Model 4 is the best model in the sense that it minimizes both risk $_{y ; y}$ and risk ${ }_{x ; y}$ (Table 3). All the information criteria tend to select Model 4. AIC tends to choose a more complex model (i.e., Model 2 or Model 5) than the other criteria, indicating a smaller penalty for model complexity. PDIO tends to choose a simpler model (i.e., Model 1), implying a larger penalty for model complexity.

To compare candidate models in the long run, the expected loss of each Model $k$ relative to that of Model 4 is computed by

Table 3 Risk functions for models and those for information criteria in Simulation 2
|  | $2 n \Delta$ risk $_{y ; y}$ |  | $2 n \Delta$ risk $_{x ; y}$ |  |
| :--- | :--- | :--- | :--- | :--- |
| Model 1 | 6.60 | (0.04) | 33.2 | (0.21) |
| Model 2 | 1.40 | (0.02) | 59.2 | (0.71) |
| Model 3 | 7.86 | (0.04) | 80.7 | (0.80) |
| Model $4{ }^{\text {a }}$ | 0 | (0.00) | 0 | (0.00) |
| Model $5{ }^{\text {a }}$ | 1.32 | (0.02) | 45.6 | (0.87) |
| AIC | 1.44 | (0.03) | 39.6 | (0.91) |
| PDIO | 3.57 | (0.04) | 19.6 | (0.30) |
| $\mathrm{AIC}_{c d}$ | 2.33 | (0.04) | 28.2 | (0.72) |
| $\mathrm{AIC}_{x ; y}$ | 2.36 | (0.04) | 14.8 | (0.43) |


$$
\Delta \operatorname{risk}_{x ; y}(k): \approx \frac{1}{B} \sum_{b=1}^{B}\left(\operatorname{loss}_{x ; y}\left(X^{(b)}, k\right)-\operatorname{loss}_{x ; y}\left(X^{(b)}, 4\right)\right) .
$$

Table 3 (upper) shows the results. The most complex model (Model 5) is the second best in terms of risk ${ }_{y ; y}$, but the simplest model (Model 1) is the second best in terms of risk ${ }_{x ; y}$, indicating a large contribution of $p_{z \mid y}(\boldsymbol{\theta})$ to the second term of (17).

The information criterion performance is measured by the expected loss of the selected model. For example, the performance of AIC in terms of complete data is measured by

$$
\Delta \operatorname{risk}_{x ; y}(\mathrm{AIC}): \approx \frac{1}{B} \sum_{b=1}^{B}\left(\operatorname{loss}_{x ; y}\left(X^{(b)}, \hat{k}^{(b)}\right)-\operatorname{loss}_{x ; y}\left(X^{(b)}, 4\right)\right),
$$

where $\hat{k}^{(b)}$ is the minimum AIC model computed from $Y^{(b)}$. Table 3 (lower) shows the results, where the value in bold denotes the minimum value of each column. AIC outperforms the other criteria in terms of risk ${ }_{y ; y}$, and $\mathrm{AIC}_{x ; y}$ outperforms the other criteria in terms of risk $\mathrm{x}_{x ; y}$. In this example, some models do not satisfy assumption (15), but AIC and AIC $x ; y$ work very well as expected.

## 8 Concluding remarks

We derived $\mathrm{AIC}_{x ; y}$ as an unbiased estimator of the expected Kullback-Leibler divergence between the true distribution and the estimated distribution of complete data when only incomplete data are available. In Simulation 1, AIC $_{x ; y}$ and AIC are unbiased up to the penalty terms, whereas PDIO and AIC ${ }_{c d}$ are not.

To derive $\mathrm{AIC}_{x ; y}$, we assumed (15), meaning that the conditional distribution $p_{z \mid y}(\boldsymbol{\theta})$ of the missing data given the incomplete data is correctly specified, while the marginal distribution $p_{y}(\boldsymbol{\theta})$ of the incomplete data is misspecified in general. However, the conditional distribution is misspecified in practice. In Simulation 2, we observed that $\mathrm{AIC}_{x ; y}$ and AIC perform better than the other criteria even if some
models are misspecified. Without assumption (15), the dominant term in (17) is $D_{x}\left(q_{x} ; p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)=D_{x}\left(q_{x} ; p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}\right)+D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right) \geq D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)$. Thus, $\mathrm{AIC}_{x ; y}$ estimates the lower bound of $2 n \mathrm{risk}_{x ; y}$. It is impossible to reasonably estimate the ignored term $D_{x}\left(q_{x} ; p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}\right)$ in our setting where $z_{1}, \ldots, z_{n}$ are missing completely.

Although we assume that $p_{z \mid y}(\boldsymbol{\theta})$ is correctly specified, it is beneficial to include $p_{z \mid y}(\boldsymbol{\theta})$ as a part of $p_{x}(\boldsymbol{\theta})=p_{z \mid y}(\boldsymbol{\theta}) p_{y}(\boldsymbol{\theta})$ for model selection. The variance of $\hat{\boldsymbol{\theta}}_{y}$ causes $p_{z \mid y}\left(\hat{\boldsymbol{\theta}}_{y}\right)$ to fluctuate even if $p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right)=q_{z \mid y}$. The amount of this random variation is measured by the additional penalty term (1) in $\mathrm{AIC}_{x ; y}$.

In the future, we plan to work on more complicated missing mechanisms or combine a missing mechanism with other sampling mechanisms, such as the covariate-shift (Shimodaira 2000) problem. One important extension is semi-supervised learning (Chapelle et al. 2006; Kawakita and Takeuchi 2014), where the log-likelihood function is

$$
\ell(\boldsymbol{\theta})=\sum_{t=1}^{n} \log p_{y}\left(\boldsymbol{y}_{t} ; \boldsymbol{\theta}\right)+\sum_{t=n+1}^{n+n^{\prime}} \log p_{x}\left(\boldsymbol{x}_{t} ; \boldsymbol{\theta}\right) .
$$

In this case, the additional complete data $\boldsymbol{x}_{n+1}, \ldots, \boldsymbol{x}_{n+n^{\prime}}$ help estimate conditional distribution $q_{z \mid y}$. We may reasonably estimate $D_{x}\left(q_{x} ; p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right) q_{y}\right)$ without assuming (15), leading to a new information criterion, which will be the subject in future research.

Acknowledgements We would like to thank the reviewers for their comments to improve the manuscript. We appreciate Kei Hirose and Shinpei Imori for their suggestions and comments. While preparing an earlier version of the manuscript, which was published as Shimodaira (1994), Hidetoshi Shimodaira is indebted to Shun-ichi Amari for the geometrical view of the EM algorithm and to Noboru Murata for the derivation of the Takeuchi information criterion.

## Appendix A: Technical details

## A. 1 Proof of Lemma 1

For brevity, we omit $(\boldsymbol{y}, \boldsymbol{z})$ of $f_{x}(\boldsymbol{y}, \boldsymbol{z})$ in the integrals below. $D_{x}\left(g_{x} ; f_{x}\right)= \iint g_{z \mid y} g_{y}\left(\log g_{z \mid y}+\log g_{y}-\log f_{z \mid y}-\log f_{y}\right) d z d \boldsymbol{y}=\int g_{y} \int g_{z \mid y}\left(\log g_{z \mid y}-\right. \left.\log f_{z \mid y}\right) d z d \boldsymbol{y}+\int g_{y}\left(\int g_{z \mid y} d z\right)\left(\log g_{y}-\log f_{y}\right) d \boldsymbol{y}=\int g_{y} \int g_{z \mid y}\left(\log g_{z \mid y} g_{y}-\right. \left.\log f_{z \mid y} g_{y}\right) d z d \boldsymbol{y}+\int g_{y}\left(\log g_{y}-\log f_{y}\right) d \boldsymbol{y}=D_{x}\left(g_{z \mid y} g_{y} ; f_{z \mid y} g_{y}\right)+D_{y}\left(g_{y} ; f_{y}\right)$, thus showing (6). $D_{y}\left(g_{y} ; f_{y}\right)=\iint h_{z \mid y} g_{y}\left(\log g_{y}-\log f_{y}+\log h_{z \mid y}-\log h_{z \mid y}\right) d z d \boldsymbol{y}= D_{x}\left(h_{z \mid y} g_{y} ; h_{z \mid y} f_{y}\right)$, which shows (7).

## A. 2 Proof of Lemma 2

We assume $q_{z \mid y}=p_{z \mid y}\left(\overline{\boldsymbol{\theta}}_{y}\right)$ and $\overline{\boldsymbol{\theta}}_{x}=\overline{\boldsymbol{\theta}}_{y}$. From the definitions of $\overline{\boldsymbol{\theta}}_{x}$ and $H_{x}$, we have

$$
\left.\frac{\partial D_{x}\left(q_{x} ; p_{x}(\boldsymbol{\theta})\right)}{\partial \boldsymbol{\theta}}\right|_{\overline{\boldsymbol{\theta}}_{y}}=0,\left.\quad \frac{\partial^{2} D_{x}\left(q_{x} ; p_{x}(\boldsymbol{\theta})\right)}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{T}}\right|_{\overline{\boldsymbol{\theta}}_{y}}=H_{x} .
$$

Hence, the Taylor expansion of $D_{x}\left(q_{x} ; p_{x}(\boldsymbol{\theta})\right)$ around $\boldsymbol{\theta}=\overline{\boldsymbol{\theta}}_{y}$ is

$$
D_{x}\left(q_{x} ; p_{x}(\boldsymbol{\theta})\right)=D_{x}\left(q_{x} ; p_{x}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)+\frac{1}{2}\left(\boldsymbol{\theta}-\overline{\boldsymbol{\theta}}_{y}\right)^{T} H_{x}\left(\boldsymbol{\theta}-\overline{\boldsymbol{\theta}}_{y}\right)+O\left(n^{-3 / 2}\right)
$$

for $\boldsymbol{\theta}-\overline{\boldsymbol{\theta}}_{y}=O\left(n^{-1 / 2}\right)$. The first term on the right-hand side is $D_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)$ as shown in (16). Substituting $\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}_{y}$ in $D_{x}\left(q_{x} ; p_{x}(\boldsymbol{\theta})\right)$ and taking its expectation gives (17) by noting

$$
E\left\{\left(\hat{\boldsymbol{\theta}}_{y}-\overline{\boldsymbol{\theta}}_{y}\right)^{T} H_{x}\left(\hat{\boldsymbol{\theta}}_{y}-\overline{\boldsymbol{\theta}}_{y}\right)\right\}=\operatorname{tr}\left(H_{x} E\left\{\left(\hat{\boldsymbol{\theta}}_{y}-\overline{\boldsymbol{\theta}}_{y}\right)\left(\hat{\boldsymbol{\theta}}_{y}-\overline{\boldsymbol{\theta}}_{y}\right)^{T}\right\}\right)
$$

which becomes $\operatorname{tr}\left(H_{x} H_{y}^{-1} G_{y} H_{y}^{-1}\right) / n+O\left(n^{-2}\right)$ from (4).

## A. 3 Proof of Theorem 1

From the definitions of $\hat{\boldsymbol{\theta}}_{y}$ and $\hat{H}_{y}=H_{y}\left(\hat{q}_{y} ; \hat{\boldsymbol{\theta}}_{y}\right)$, we have

$$
\left.\frac{\partial L_{y}\left(\hat{q}_{y} ; p_{y}(\boldsymbol{\theta})\right)}{\partial \boldsymbol{\theta}}\right|_{\hat{\boldsymbol{\theta}}_{y}}=0,\left.\quad \frac{\partial^{2} L_{y}\left(\hat{q}_{y} ; p_{y}(\boldsymbol{\theta})\right)}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{T}}\right|_{\hat{\boldsymbol{\theta}}_{y}}=\hat{H}_{y} .
$$

Hence, the Taylor expansion of $L_{y}\left(\hat{q}_{y} ; p_{y}(\boldsymbol{\theta})\right)$ around $\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}_{y}$ is

$$
L_{y}\left(\hat{q}_{y} ; p_{y}(\boldsymbol{\theta})\right)=L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)+\frac{1}{2}\left(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}}_{y}\right)^{T} \hat{H}_{y}\left(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}}_{y}\right)+O_{p}\left(n^{-3 / 2}\right)
$$

for $\boldsymbol{\theta}-\hat{\boldsymbol{\theta}}_{y}=O_{p}\left(n^{-1 / 2}\right)$. Substituting $\boldsymbol{\theta}=\overline{\boldsymbol{\theta}}_{y}$ in $L_{y}\left(\hat{q}_{y} ; p_{y}(\boldsymbol{\theta})\right)$, we take its expectation below. By noting $\hat{H}_{y}=H_{y}+O_{p}\left(n^{-1 / 2}\right)$, we have

$$
E\left\{\left(\overline{\boldsymbol{\theta}}_{y}-\hat{\boldsymbol{\theta}}_{y}\right)^{T} \hat{H}_{y}\left(\overline{\boldsymbol{\theta}}_{y}-\hat{\boldsymbol{\theta}}_{y}\right)\right\}=\operatorname{tr}\left(H_{y} E\left\{\left(\hat{\boldsymbol{\theta}}_{y}-\overline{\boldsymbol{\theta}}_{y}\right)\left(\hat{\boldsymbol{\theta}}_{y}-\overline{\boldsymbol{\theta}}_{y}\right)^{T}\right\}\right)+O\left(n^{-3 / 2}\right)
$$

which becomes $\operatorname{tr}\left(H_{y} H_{y}^{-1} G_{y} H_{y}^{-1}\right) / n+O\left(n^{-3 / 2}\right)$ from (4). This proves (20) because

$$
E\left\{L_{y}\left(\hat{q}_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)\right\}=E\left\{L_{y}\left(\hat{q}_{y} ; p_{y}\left(\hat{\boldsymbol{\theta}}_{y}\right)\right)\right\}+\frac{1}{2 n} \operatorname{tr}\left(G_{y} H_{y}^{-1}\right)+O\left(n^{-3 / 2}\right),
$$

and $E\left\{L_{y}\left(\hat{q}_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)\right\}=L_{y}\left(q_{y} ; p_{y}\left(\overline{\boldsymbol{\theta}}_{y}\right)\right)$. Substituting (20) into (17) and comparing it with (18) yields (21).

## References

Akaike, H. (1974). A new look at the statistical model identification. IEEE Transactions on Automatic Control, 19, 716-723.
Amari, S. (1995). Information geometry of the EM and em algorithms for neural networks. Neural Networks, 8, 1379-1408.
Amari, S., Nagaoka, H. (2007). Methods of information geometry 191. Providence, RI: American Mathematical Society.
Bozdogan, H. (1987). Model selection and Akaike's information criterion (AIC): The general theory and its analytical extensions. Psychometrika, 52, 345-370.
Burnham, K. P., Anderson, D. R. (2002). Model selection and multimodel inference: A practical informationtheoretic approach. New York: Springer.
Byrne, W. (1992). Alternating minimization and Boltzmann machine learning. IEEE Transactions on Neural Networks, 3, 612-620.
Cavanaugh, J. E., Shumway, R. H. (1998). An Akaike information criterion for model selection in the presence of incomplete data. Journal of Statistical Planning and Inference, 67, 45-65.
Chapelle, O., Schölkopf, B., Zien, A. (2006). Semi-supervised learning. Cambridge: The MIT Press.
Claeskens, G., Consentino, F. (2008). Variable selection with incomplete covariate data. Biometrics, 64, 1062-1069.
Csiszár, I. (1975). I-divergence geometry of probability distributions and minimization problems. The Annals of Probability, 3, 146-158.
Csiszár, I., Tusnády, G. (1984). Information geometry and alternating minimization procedures. Statistics and decisions, Supplement Issue, 1, 205-237.
Dempster, A. P., Laird, N. M., Rubin, D. B. (1977). Maximum likelihood from incomplete data via the EM algorithm. Journal of the Royal Statistical Society Series B (Methodological), 39, 1-38.
Ip, E. H., Lalwani, N. (2000). A note on the geometric interpretation of the EM algorithm in estimating item characteristics and student abilities. Psychometrika, 65, 533-537.
Kawakita, M., Takeuchi, J. (2014). Safe semi-supervised learning based on weighted likelihood. Neural Networks, 53, 146-164.
Konishi, S., Kitagawa, G. (2008). Information criteria and statistical modeling. New York: Springer.
Meng, X.-L., Rubin, D. B. (1991). Using EM to obtain asymptotic variance-covariance matrices: The SEM algorithm. Journal of the American Statistical Association, 86, 899-909.
Seghouane, A. K., Bekara, M., Fleury, G. (2005). A criterion for model selection in the presence of incomplete data based on Kullback's symmetric divergence. Signal Processing, 85, 1405-1417.
Shimodaira, H. (1994). A new criterion for selecting models from partially observed data. Selecting Models from Data (pp. 21-29). New York: Springer.
Shimodaira, H. (2000). Improving predictive inference under covariate shift by weighting the log-likelihood function. Journal of Statistical Planning and Inference, 90, 227-244.
White, H. (1982). Maximum likelihood estimation of misspecified models. Econometrica, 50, 1-25.
Yamazaki, K. (2014). Asymptotic accuracy of distribution-based estimation of latent variables. The Journal of Machine Learning Research, 15, 3541-3562.


[^0]:    The research was supported in part by JSPS KAKENHI Grant (24300106, 16H02789).
    Hidetoshi Shimodaira
    shimo@sigmath.es.osaka-u.ac.jp
    1 Division of Mathematical Science, Graduate School of Engineering Science, Osaka University, 1-3 Machikaneyama-cho, Toyonaka, Osaka 560-8531, Japan
    2 RIKEN Center for Advanced Intelligence Project, 1-4-1 Nihonbashi, Chuo-ku, Tokyo 103-0027, Japan
    3 Present Address: Kawasaki Heavy Industries, Ltd., 1-1 Kawasaki-cho, Akashi, Hyogo 673-8666, Japan

