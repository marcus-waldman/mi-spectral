---
citekey: cavanaughAkaikeInformationCriterion1998a
item_type: article
authors: 'Cavanaugh, Joseph E. and Shumway, Robert H.'
year: 1998
title: 'An {Akaike} Information Criterion for Model Selection in the Presence of Incomplete Data'
venue: Journal of Statistical Planning and Inference
volume: 67
issue: 1
pages: 45--65
doi: 10.1016/S0378-3758(97)00115-8
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\cavanaugh_akaike_information_criterion_1998.pdf'
pdf_sha256: b59377318d265956080ab494a67ad3ed49ff96a6d3ac051a323ce17c7064f086
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T23:01:52Z
---
# An Akaike information criterion for model selection in the presence of incomplete data 

Joseph E. Cavanaugh ${ }^{\mathrm{a}, *}$, Robert H. Shumway ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}}$ Department of Statistics, University of Missouri, Columbia, MO 65211, USA<br>${ }^{\mathrm{b}}$ Division of Statistics, University of California, Davis, CA 95616, USA

Received 24 March 1995; received in revised form 9 June 1997


#### Abstract

We derive and investigate a variant of AIC, the Akaike information criterion, for model selection in settings where the observed data is incomplete. Our variant is based on the motivation provided for the PDIO ('predictive divergence for incomplete observation models') criterion of Shimodaira (1994, in: Selecting Models from Data: Artificial Intelligence and Statistics IV, Lecture Notes in Statistics, vol. 89, Springer, New York, pp. 21-29). However, our variant differs from PDIO in its 'goodness-of-fit' term. Unlike AIC and PDIO, which require the computation of the observed-data empirical log-likelihood, our criterion can be evaluated using only complete-data tools, readily available through the EM algorithm and the SEM ('supplemented' EM) algorithm of Meng and Rubin (Journal of the American Statistical Association 86 (1991) 899-909). We compare the performance of our AIC variant to that of both AIC and PDIO in simulations where the data being modeled contains missing values. The results indicate that our criterion is less prone to overfitting than AIC and less prone to underfitting than PDIO. © 1998 Elsevier Science B.V. All rights reserved.


AMS classification: 62B10; 94A17; 62E25
Keywords: AIC; EM algorithm; Information theory; Kullback-Leibler information; Model selection criteria; PDIO criterion; SEM algorithm

## 1. Introduction

Modeling in the presence of incomplete or partially observed data arises in a large variety of practical problems, including applications involving ANOVA and regression models (Rubin, 1976; Little, 1979), state-space models (Shumway and Stoffer, 1982), latent class models (Goodman, 1974), and mixture models (Titterington et al., 1985). In such settings, we generally view the observed, incomplete data $\boldsymbol{Y}_{\text {obs }}$ together with unobserved, missing data $\boldsymbol{Y}_{\text {mis }}$ as comprising the complete data $\boldsymbol{Y}$. A parametric family of

[^0]models $f(\boldsymbol{Y} \mid \boldsymbol{\theta})$ is postulated for the complete data $\boldsymbol{Y}$, where the size of the parameter vector $\boldsymbol{\theta}$ dictates the complexity of the corresponding model. The complete-data model $f(\boldsymbol{Y} \mid \boldsymbol{\theta})$ implies a model for the incomplete data, $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}\right)$, although the latter is often more difficult to represent or to work with than the former. In many frameworks, a fitted model for the complete data $f(\boldsymbol{Y} \mid \hat{\boldsymbol{\theta}})$ can be conveniently found through utilizing the well-known EM (expectation/maximization) algorithm (Dempster et al., 1977).

In most applications, finding a suitable dimension for the parameter vector $\boldsymbol{\theta}$ is an important component of the modeling problem. A common approach is to choose several different dimensions for $\boldsymbol{\theta}$, find the fitted models corresponding to these choices, compute a model selection criterion for each of the fitted candidate models, and determine the dimension of $\theta$ for the final model based on the values of the criterion. The Akaike information criterion (Akaike, 1973, 1974), or AIC, is the most widely known and used of the criteria which have been proposed for this purpose.

In the present context, AIC can be interpreted as a measure of separation between the fitted model for the incomplete data, $f\left(\boldsymbol{Y}_{\text {obs }} \mid \hat{\boldsymbol{\theta}}\right)$, and the 'true' or generating model which presumably gave rise to the incomplete data, say $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}_{o}\right)$. Yet as indicated by Shimodaira (1994), in many applications it may be more natural or desirable to use a criterion based on the complete data, which assesses the separation between the fitted model $f(\boldsymbol{Y} \mid \hat{\boldsymbol{\theta}})$ and the generating model $f\left(\boldsymbol{Y} \mid \boldsymbol{\theta}_{o}\right)$. There are several arguments to be made in defense of this idea. First of all, the implementation of the EM algorithm is based on the premise that a convenient class of models can be specified for the complete data $\boldsymbol{Y}$, whereas the corresponding class of models for the incomplete data $\boldsymbol{Y}_{\text {obs }}$ may be difficult to exhibit or to work with. Since it is the complete data for which the investigator postulates the family of 1.10dels, it seems reasonable to base model selection on measures which assess the propriety of fitted candidate models within this family. Secondly, as pointed out by Meng and Rubin (1991, p. 899), the EM algorithm essentially involves 'capitalizing on computing power and complete-data tools to handle missing-data problems'. Because the EM algorithm utilizes completedata tools, it may be more computationally convenient to calculate a selection criterion based on these quantities rather than analogous incomplete-data quantities. And finally, the complete-data density $f(\boldsymbol{Y} \mid \boldsymbol{\theta})$ is composed of the product of the incompletedata density $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}\right)$ and the conditional density of the missing data $\boldsymbol{Y}_{\text {mis }}$ given the incomplete data $\boldsymbol{Y}_{\text {obs }}$; i.e.,

$$
f(\boldsymbol{Y} \mid \boldsymbol{\theta})=f\left(\boldsymbol{Y}_{\mathrm{obs}} \mid \boldsymbol{\theta}\right) f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}\right) .
$$

Suppose that the density $f\left(\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}, \boldsymbol{\theta}\right)$ is substantially affected by deviations of $\boldsymbol{\theta}$ from the 'true' parameter vector $\boldsymbol{\theta}_{o}$. Model selection based on the discrepancy between $f(\boldsymbol{Y} \mid \hat{\boldsymbol{\theta}})$ and $f\left(\boldsymbol{Y} \mid \boldsymbol{\theta}_{o}\right)$ would incorporate this information; it is not clear that model selection based on the discrepancy between $f\left(\boldsymbol{Y}_{\text {obs }} \mid \hat{\boldsymbol{\theta}}\right)$ and $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}_{o}\right)$ would do the same.

The last of the aforementioned arguments is further explored in the next section. In Section 3, we present an informal derivation of a model selection criterion which is analogous to AIC, yet is based on complete-data rather than incomplete-data concepts
and tools. We call this criterion AICcd, where the notation 'cd' stands for 'complete data'. Our criterion is motivated by the same principle as the PDIO ('predictive divergence for incomplete observation models') criterion introduced by Shimodaira (1994), yet differs from PDIO in its goodness-of-fit term.

In Section 4, we describe the evaluation of AICcd, and indicate the computational advantage the criterion holds over PDIO and AIC. We contrast the forms of AICcd, PDIO, and AIC in Section 5, and discuss several key principles related to the behavior of these criteria. These principles are illustrated by the simulation sets presented in Sections 6 and 7. In these simulations, we compare the effectiveness of AICcd, PDIO, and AIC at selecting a model of correct dimension within a candidate class, where the data being modeled contains various degrees of missing values. Our results demonstrate that AICcd is generally less prone to underfitting than PDIO and less prone to overfitting than AIC. The simulations in Section 6 involve modeling bivariate normal data whereas the simulations in Section 7 are based on multivariate regression models. Section 8 concludes.

## 2. Complete-data versus incomplete-data Kullback-Leibler discrepancy

Let $f(\boldsymbol{Y} \mid \boldsymbol{\theta})$ and $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}\right)$ respectively denote parametric densities for the complete data $\boldsymbol{Y}$ and the incomplete data $\boldsymbol{Y}_{\text {obs }}$. Assume that the parameter vector $\boldsymbol{\theta}$ is $d$-dimensional. Let $\boldsymbol{\theta}_{o}$ denote the 'true' parameter vector, so that $f\left(\boldsymbol{Y} \mid \boldsymbol{\theta}_{o}\right)$ and $f\left(Y_{\text {obs }} \mid \theta_{o}\right)$ respectively represent the generating densities for the complete and the incomplete data.

A well-known measure of separation between two models is given by the nonnormalized Kullback-Leibler information (Kullback, 1968), also known as the cross entropy or discrepancy. The complete-data Kullback-Leibler discrepancy between a candidate model $f(\boldsymbol{Y} \mid \boldsymbol{\theta})$ and the generating model $f\left(\boldsymbol{Y} \mid \boldsymbol{\theta}_{o}\right)$ is defined by

$$
D_{Y}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)=E_{Y}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}
$$

where $E_{\boldsymbol{Y}}$ denotes the expected value with respect to the density $f\left(\boldsymbol{Y} \mid \boldsymbol{\theta}_{o}\right)$. Similarly, the incomplete-data Kullback-Leibler discrepancy between a candidate model $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}\right)$ and the generating model $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}_{o}\right)$ is defined by

$$
D_{\boldsymbol{Y}_{\mathrm{obs}}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)=E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{obs}} \mid \boldsymbol{\theta}\right)\right\},
$$

where $E_{\boldsymbol{Y}_{\text {obs }}}$ denotes the expected value with respect to the density $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}_{0}\right)$. Since the evaluation of (2.1) and (2.2) requires knowledge of $\boldsymbol{\theta}_{o}$, these quantities are not directly accessible. Thus, it is not possible to assess the exact discrepancy between a fitted candidate model, parameterized by $\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}$, and the corresponding generating model.

An important contribution of Akaike $(1973,1974)$ was in showing that in certain large-sample settings, the expected value of

$$
D_{\boldsymbol{Y}_{\mathrm{obs}}}\left(\hat{\boldsymbol{\theta}}, \boldsymbol{\theta}_{o}\right)=\left.E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{obs}} \mid \boldsymbol{\theta}\right)\right\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}
$$

(with respect to $\left.f\left(Y_{\text {obs }} \mid \theta_{o}\right)\right)$ is approximately the same as the expected value of

$$
\mathrm{AIC}=-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)+2 d,
$$

where $L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$ denotes the incomplete-data empirical likelihood. In other words, AIC serves as an approximately unbiased estimator of the expected incomplete-data discrepancy

$$
\Delta_{\boldsymbol{Y}_{\mathrm{obs}}}\left(d, \boldsymbol{\theta}_{o}\right)=E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\left.E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{obs}} \mid \boldsymbol{\theta}\right)\right\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}\right\} .
$$

The terms $-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$ and $2 d$ in AIC are commonly referred to as the 'goodness-of-fit' and 'penalty' terms, respectively.

Our objective is to propose a version of AIC that will have an expected value (with respect to $\left.f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}_{o}\right)\right)$ which, in large-sample settings, is approximately the same as the expected value of

$$
D_{Y}\left(\hat{\boldsymbol{\theta}}, \boldsymbol{\theta}_{o}\right)=\left.E_{Y}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}\right|_{\theta=\hat{\boldsymbol{\theta}}}
$$

(Note that (2.6) is a function of $\boldsymbol{Y}_{\text {obs }}$ through its dependence on $\hat{\boldsymbol{\theta}}$, yet does not involve the missing data $\boldsymbol{Y}_{\text {mis }}$.) Equivalently, we wish to propose an approximately unbiased estimator of the expected complete-data discrepancy

$$
\Delta_{Y}\left(d, \theta_{o}\right)=E_{Y_{\mathrm{obs}}}\left\{\left.E_{Y}\{-2 \ln f(\boldsymbol{Y} \mid \theta)\}\right|_{\theta=\hat{\theta}}\right\} .
$$

The relationship between (2.1) and (2.2) provides an important insight into why it may be preferable to base model selection on the former as opposed to the latter. To establish this relationship, recall that

$$
f(\boldsymbol{Y} \mid \boldsymbol{\theta})=f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}\right) f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\text {obs }}, \boldsymbol{\theta}\right),
$$

meaning

$$
E_{Y}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}=E_{Y}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{obs}} \mid \boldsymbol{\theta}\right)\right\}+E_{\boldsymbol{Y}}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}\right)\right\} .
$$

Using (2.8), it is easily shown that

$$
E_{Y}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{obs}} \mid \boldsymbol{\theta}\right)\right\}=D_{\boldsymbol{Y}_{\mathrm{obs}}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right),
$$

meaning that (2.9) can be written as

$$
D_{\boldsymbol{Y}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)=D_{\boldsymbol{Y}_{\mathrm{obs}}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)+E_{\boldsymbol{Y}}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}\right)\right\} .
$$

Now consider the second of the two terms on the right-hand side of (2.10). Define

$$
D_{\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)=E_{\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}\right)\right\},
$$

where $E_{\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}}$ denotes the expected value with respect to the density $f\left(\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}, \boldsymbol{\theta}_{o}\right)$. We will refer to (2.11) as the conditional missing-data discrepancy. Using (2.8), it is easily shown that

$$
E_{\boldsymbol{Y}}\left\{-2 \ln f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}\right)\right\}=E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{D_{\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\},
$$

meaning that (2.10) can be written as

$$
D_{\boldsymbol{Y}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)=D_{\boldsymbol{Y}_{\mathrm{obs}}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)+E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{D_{\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\} .
$$

Now one can easily establish using Jensen's inequality that for any $\boldsymbol{Y}_{\text {obs }}$ and any $\boldsymbol{\theta}$,

$$
D_{\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\text {obs }}\right) \geqslant D_{\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}}\left(\boldsymbol{\theta}_{o}, \boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\text {obs }}\right) .
$$

If we then define $k\left(\boldsymbol{\theta}_{o}\right) \equiv E_{\boldsymbol{Y}_{\text {obs }}}\left\{D_{\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}}\left(\boldsymbol{\theta}_{o}, \boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\text {obs }}\right)\right\}$, by (2.12) and (2.13), we have for any $\boldsymbol{\theta}$

$$
D_{\boldsymbol{Y}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right) \geqslant D_{\boldsymbol{Y}_{\mathrm{obs}}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)+k\left(\boldsymbol{\theta}_{o}\right) .
$$

Thus as a function of $\boldsymbol{\theta}$, the complete-data discrepancy $D_{Y}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)$ is always at least as great as the incomplete-data discrepancy $D_{Y_{\text {obs }}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)$, adjusted by the constant $k\left(\boldsymbol{\theta}_{o}\right)$.

From (2.12) and (2.14), we can infer that the complete-data discrepancy is potentially more sensitive than the incomplete-data discrepancy to deviations of $\boldsymbol{\theta}$ from $\boldsymbol{\theta}_{o}$ which affect the conditional missing-data discrepancy (2.11). This implies that in the presence of missing data, $D_{Y}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)$ may be preferable to $D_{Y_{\text {obs }}}\left(\boldsymbol{\theta}, \boldsymbol{\theta}_{o}\right)$ for assessing the separation between a model parameterized by $\boldsymbol{\theta}$ and one parameterized by $\boldsymbol{\theta}_{o}$. As a consequence, an estimator of $\Delta_{Y}\left(d, \theta_{o}\right)$ may be preferable to an estimator of $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$ as a model selection criterion, provided of course that the former is accurate enough to sufficiently reflect the sensitivity of $\Delta_{Y}\left(d, \theta_{o}\right)$.

In the next section, we introduce and derive the AICcd statistic, which in largesample settings, serves as an approximately unbiased estimator of $\Delta_{Y}\left(d, \theta_{o}\right)$. This criterion has different goodness-of-fit and penalty terms than AIC, yet both terms reduce to their AIC counterparts when $\boldsymbol{Y}=\boldsymbol{Y}_{\text {obs }}$. The criterion shares the penalty term of Shimodaira's (1994) PDIO, yet differs in the goodness-of-fit term, where PDIO and AIC agree.

## 3. Derivation of AICed

We seek an approximately unbiased estimator of $\Delta_{Y}\left(d, \theta_{o}\right)$. We will require that the parameter space for the candidate model under consideration includes $\theta_{o}$ as an interior point. (This strong assumption is also used in the derivation of AIC. See Linhart and Zucchini, 1986, p. 245.) We will assume that the fitted parameter vector $\hat{\boldsymbol{\theta}}$ is obtained using the EM algorithm, making $\hat{\boldsymbol{\theta}}$ a maximum likelihood estimator of $\boldsymbol{\theta}_{o}$. We will require the usual regularity conditions needed to ensure the consistency and asymptotic normality of $\hat{\boldsymbol{\theta}}$.

Following conventions similar to those of Meng and Rubin (1991), let

$$
\begin{aligned}
& Q\left(\boldsymbol{\theta}_{1} \mid \boldsymbol{\theta}_{2}\right)=\int_{\boldsymbol{Y}_{\mathrm{mis}}}\left\{\ln f\left(\boldsymbol{Y} \mid \boldsymbol{\theta}_{1}\right)\right\} f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}_{2}\right) \mathrm{d} \boldsymbol{Y}_{\mathrm{mis}} \\
& \boldsymbol{I}_{o}(\boldsymbol{\theta} \mid \boldsymbol{Y})=-\frac{\partial^{2} \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{\prime}}
\end{aligned}
$$

$$
\begin{aligned}
& \boldsymbol{I}_{o}\left(\boldsymbol{\theta} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)=-\frac{\partial^{2} \ln f\left(\boldsymbol{Y}_{\mathrm{obs}} \mid \boldsymbol{\theta}\right)}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{\prime}} \\
& \boldsymbol{I}_{o c}\left(\boldsymbol{\theta} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)=\int_{\boldsymbol{Y}_{\mathrm{mis}}}\left\{-\frac{\partial^{2} \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{\prime}}\right\} f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}\right) \mathrm{d} \boldsymbol{Y}_{\mathrm{mis}}
\end{aligned}
$$

To begin, expand $\left.E_{\boldsymbol{Y}}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}$ about $\boldsymbol{\theta}_{o}$ to obtain

$$
\begin{aligned}
& \left.E_{\boldsymbol{Y}}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}\right|_{\boldsymbol{\theta}=\hat{\theta}} \\
& \quad \approx E_{\boldsymbol{Y}}\left\{-2 \ln f\left(\boldsymbol{Y} \mid \boldsymbol{\theta}_{o}\right)\right\}+\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{Y}\left\{\boldsymbol{I}_{o}\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{Y}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)
\end{aligned}
$$

Now using (2.8), one can show that

$$
E_{Y}\left\{-2 \ln f\left(\boldsymbol{Y} \mid \boldsymbol{\theta}_{o}\right)\right\}=E_{Y_{\mathrm{obs}}}\left\{-2 Q\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{\theta}_{o}\right)\right\},
$$

and that

$$
E_{Y}\left\{\boldsymbol{I}_{o}\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{Y}\right)\right\}=E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\} .
$$

Substituting (3.6) and (3.7) into (3.5), we obtain

$$
\begin{aligned}
& \left.E_{Y}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}} \\
& \quad \approx E_{\boldsymbol{V}_{\mathrm{obs}}}\left\{-2 Q\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{\theta}_{o}\right)\right\}+\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)
\end{aligned}
$$

Yet for large $n$, it is justifiable to replace $\boldsymbol{I}_{o c}\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{Y}_{\text {obs }}\right)$ in (3.8) with $\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$. This leads to the large-sample approximation

$$
\begin{aligned}
& \left.E_{\boldsymbol{Y}}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}} \\
& \quad \approx E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{-2 Q\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{\theta}_{o}\right)\right\}+\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)
\end{aligned}
$$

Next, expand the first argument of $-2 Q\left(\boldsymbol{\theta}_{o} \mid \hat{\boldsymbol{\theta}}\right)$ about $\hat{\boldsymbol{\theta}}$ to obtain

$$
\begin{aligned}
-2 Q\left(\boldsymbol{\theta}_{o} \mid \hat{\boldsymbol{\theta}}\right) \approx & -2 Q(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})-2\left(\boldsymbol{\theta}_{o}-\hat{\boldsymbol{\theta}}\right)^{\prime}\left\{\left.\left\{\frac{\partial Q(\boldsymbol{\theta} \mid \hat{\boldsymbol{\theta}})}{\partial \boldsymbol{\theta}}\right\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}\right\} \\
& +\left(\boldsymbol{\theta}_{o}-\hat{\boldsymbol{\theta}}\right)^{\prime}\left\{\left.\left\{-\frac{\partial^{2} Q(\boldsymbol{\theta} \mid \hat{\boldsymbol{\theta}})}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{\prime}}\right\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}\right\}\left(\boldsymbol{\theta}_{o}-\hat{\boldsymbol{\theta}}\right)
\end{aligned}
$$

Now on the right-hand side of (3.10), the second of the three terms is zero, since

$$
\left.\frac{\partial Q(\boldsymbol{\theta} \mid \hat{\boldsymbol{\theta}})}{\partial \boldsymbol{\theta}}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}=\mathbf{0} .
$$

(In the EM algorithm, the point of convergence $\hat{\boldsymbol{\theta}}$ provides a solution to the equation $(\partial Q(\boldsymbol{\theta} \mid \hat{\boldsymbol{\theta}})) /(\partial \boldsymbol{\theta})=\mathbf{0}$.) We can rewrite the third of these three terms by noting that

$$
-\left.\frac{\partial^{2} Q(\boldsymbol{\theta} \mid \hat{\boldsymbol{\theta}})}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{\prime}}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}=\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right) .
$$

Using (3.11) and (3.12), we can express (3.10) as

$$
-2 Q\left(\boldsymbol{\theta}_{o} \mid \hat{\boldsymbol{\theta}}\right) \approx-2 Q(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})+\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} \boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)
$$

Yet for large $n$, it is justifiable to replace $\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$ in (3.13) by $E_{\boldsymbol{Y}_{\text {obs }}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)\right\}$. This leads to the large-sample approximation

$$
-2 Q\left(\boldsymbol{\theta}_{o} \mid \hat{\boldsymbol{\theta}}\right) \approx-2 Q(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})+\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{Y_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)
$$

Now consider using $Q\left(\boldsymbol{\theta}_{o} \mid \hat{\boldsymbol{\theta}}\right)$ as an approximation to $Q\left(\boldsymbol{\theta}_{o} \mid \boldsymbol{\theta}_{o}\right)$ in (3.9). We obtain

$$
\begin{aligned}
& \left.E_{\boldsymbol{Y}}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}} \\
& \quad \approx E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{-2 Q\left(\boldsymbol{\theta}_{o} \mid \hat{\boldsymbol{\theta}}\right)\right\}+\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)
\end{aligned}
$$

If we then substitute the right-hand side of (3.14) for $-2 Q\left(\boldsymbol{\theta}_{o} \mid \hat{\boldsymbol{\theta}}\right)$ in (3.15), we have

$$
\begin{aligned}
E_{\boldsymbol{Y}}\{ & -2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}\left.\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}} \\
\approx E_{\boldsymbol{Y}_{\mathrm{obs}}}\{ & -2 Q(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})\}+E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)\right\} \\
& +\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)
\end{aligned}
$$

Taking expectations of both sides of (3.16) with respect to $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}_{o}\right)$ yields the following useful large-sample approximation for $\Delta_{Y}\left(d, \theta_{o}\right)$ :

$$
\begin{aligned}
\Delta_{\boldsymbol{Y}}\left(d, \boldsymbol{\theta}_{o}\right) & =E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\left.E_{\boldsymbol{Y}}\{-2 \ln f(\boldsymbol{Y} \mid \boldsymbol{\theta})\}\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}\right\} \\
& \approx E_{\boldsymbol{Y}_{\mathrm{obs}}}\{-2 Q(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})\}+2 E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{Y_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)\right\}
\end{aligned}
$$

Consider the estimation of the two terms on the right-hand side of (3.17). The first of these terms can be estimated by $-2 Q(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$, which is easily evaluated after the last iteration of the EM algorithm. For the second of these terms, we will use the wellknown fact that the large-sample variance/covariance matrix of ( $\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}$ ) is approximated by $\boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$. Thus, we can write

$$
\begin{aligned}
& 2 E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime} E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)\right\} \\
& \quad=2 \operatorname{trace}\left\{E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\} E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)\left(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}\right)^{\prime}\right\}\right\} \\
& \quad \approx 2 \operatorname{trace}\left\{E_{\boldsymbol{Y}_{\mathrm{obs}}}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\} \boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}
\end{aligned}
$$

A natural estimator for (3.18) is given by

$$
2 \operatorname{trace}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right) \boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)\right\}
$$

Using $-2 Q(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$ and (3.19) to approximate the terms on the right-hand side of (3.17) suggests the following large-sample estimator for $\boldsymbol{\Delta}_{Y}\left(d, \boldsymbol{\theta}_{o}\right)$ :

$$
\mathrm{AICcd}=-2 Q(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})+2 \operatorname{trace}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right) \boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\}
$$

Shimodaira's (1994) PDIO criterion, written in the present notation, has the form

$$
\mathrm{PDIO}=-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)+2 \operatorname{trace}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right) \boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\right\} .
$$

Our derivation of AICcd is similar to Shimodaira's derivation of PDIO, yet differs in several key aspects: most noticeably in the development of the goodness-of-fit term. The difference between these terms in AICcd and PDIO causes the criteria to behave quite differently, as the discussion in Section 5 and the simulations in Sections 6 and 7 will indicate.

## 4. Evaluating AICcd

The penalty term (3.19) of AICcd and PDIO involves the information matrix $\boldsymbol{I}_{o}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$. An explicit expression for $\boldsymbol{I}_{o}\left(\boldsymbol{\theta} \mid \boldsymbol{Y}_{\text {obs }}\right)$ via (3.3) can be difficult to obtain directly, since $f\left(\boldsymbol{Y}_{\text {obs }} \mid \boldsymbol{\theta}\right)$ is often inaccessible or cumbersome to work with. Fortunately, the 'supplemented' EM or SEM algorithm of Meng and Rubin (1991) provides a convenient mechanism for evaluating both $\boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$ and the penalty term (3.19) without the need for such an expression. (Evaluating $\boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)$, the approximate large-sample variance/covariance matrix of $\hat{\boldsymbol{\theta}}$, is the motivation behind the SEM algorithm. The EM algorithm alone does not provide this matrix.)

Let $\hat{\boldsymbol{\theta}}^{(t)}$ denote the estimate of $\boldsymbol{\theta}_{o}$ obtained on the $t$ th iteration of the EM algorithm. As indicated by Meng and Rubin (1991), the EM algorithm defines a mapping $\boldsymbol{M}(\boldsymbol{\theta})=\left(M_{1}(\boldsymbol{\theta}), \ldots, M_{d}(\boldsymbol{\theta})\right)^{\prime}$ such that $\hat{\boldsymbol{\theta}}^{(t+1)}=\boldsymbol{M}\left(\hat{\boldsymbol{\theta}}^{(t)}\right)$ for $t=0,1, \ldots$. If $\hat{\boldsymbol{\theta}}^{(t)}$ converges to $\hat{\theta}$ (and $\boldsymbol{M}(\theta)$ is continuous), we must have $\hat{\theta}=\boldsymbol{M}(\hat{\theta})$. A first-order expansion of $\boldsymbol{M}\left(\hat{\boldsymbol{\theta}}^{(t)}\right)$ about $\hat{\boldsymbol{\theta}}$ leads to the approximation

$$
\left(\hat{\boldsymbol{\theta}}^{(t+1)}-\hat{\boldsymbol{\theta}}\right)^{\prime} \approx\left(\hat{\boldsymbol{\theta}}^{(t)}-\hat{\boldsymbol{\theta}}\right)^{\prime} \boldsymbol{D} \boldsymbol{M},
$$

where $\boldsymbol{D} \boldsymbol{M}$ is a $d \times d$ matrix having $\left.\left\{\left(\partial M_{j}(\theta)\right) /\left(\partial \theta_{i}\right)\right\}\right|_{\boldsymbol{\theta}=\hat{\theta}}$ in row $i$ and column $j$; i.e.,

$$
\boldsymbol{D} \boldsymbol{M}=\left.\left[\frac{\partial M_{j}(\boldsymbol{\theta})}{\partial \theta_{i}}\right]\right|_{\boldsymbol{\theta}=\hat{\boldsymbol{\theta}}}, \quad 1 \leqslant i, j \leqslant d .
$$

Thus, as Meng and Rubin (1991, p. 901) state, in a neighborhood of $\hat{\theta}$, 'the EM algorithm is essentially a linear iteration with rate matrix $\boldsymbol{D} \boldsymbol{M}$, since $\boldsymbol{D} \boldsymbol{M}$ is typically nonzero'.

Meng and Rubin (1991) go on to show

$$
\boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)=\boldsymbol{I}_{o c}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}
$$

and

$$
\boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)=\boldsymbol{I}_{o c}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)+\boldsymbol{I}_{o c}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right) \boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1} .
$$

(See Meng and Rubin, 1991, p. 901, Eqs. (2.3.1), (2.3.4), (2.4.6), and (2.4.7).) This means that the penalty term (3.19) can be written using (4.1) as

$$
2 \text { trace }\left\{(I-D M)^{-1}\right\}
$$

or written using (4.2) as

$$
\begin{aligned}
2 d & +2 \operatorname{trace}\left\{\boldsymbol{I}_{o c}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)\left\{\boldsymbol{I}_{o c}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right) \boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}\right\}\right\} \\
& =2 d+2 \operatorname{trace}\left\{\boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}\right\} .
\end{aligned}
$$

The computation of $\boldsymbol{D} \boldsymbol{M}$ is discussed in Section 3.3 of Meng and Rubin (1991). Once $\boldsymbol{D} \boldsymbol{M}$ is obtained, the penalty term of AICcd and PDIO can be easily evaluated using (4.3). ( $\boldsymbol{I}_{o}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$ is typically computed using (4.2).)

Expression (4.4) is useful for the purpose of comparing the penalty term of AIC ( $2 d$ ) to the penalty term of AICcd and PDIO. The matrix $\boldsymbol{I}_{o c}^{-1}\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right) \boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}$ is described by Meng and Rubin (1991, p. 901) as representing 'the increase in variance [of $\hat{\theta}$ ] due to missing information'. Thus, the trace term in (4.4) can be conveniently viewed as a measure of the amount of data which is missing in $\boldsymbol{Y}$; or more precisely, as a measure of the extent to which the missing data $\boldsymbol{Y}_{\text {mis }}$ affects the fitted model. If $\boldsymbol{Y}=\boldsymbol{Y}_{\text {obs }}$, this trace term will be zero (since $\mathbf{D M}=\mathbf{0}$ ); otherwise, it will be positive. Moreover, this term will be substantial in settings where the amount of missing data is large relative to the complexity of the fitted model. Thus, (4.4) implies that the penalty term of AICcd and PDIO is composed of the penalty term of AIC together with a term which assesses an additional penalty in accordance to the impact of the missing data on the fitted model.

In discussing the evaluation of AICcd, it is important to note that its goodness-of-fit term is based on the complete-data function $Q(\boldsymbol{\theta} \mid \boldsymbol{\theta})$, which is the principal tool used by the EM algorithm. The evaluation of this term should always be straightforward. The same cannot be said of the goodness-of-fit term of AIC and PDIO, which is based on the incomplete-data $\log$-likelihood $\ln L\left(\boldsymbol{\theta} \mid \boldsymbol{Y}_{\text {obs }}\right)$. We feel that one of the most compelling features of AICcd is that its computation involves only complete-data quantities which arise naturally in the execution of the EM and SEM algorithms. It is therefore readily accessible in any of the wide variety of incomplete-data problems for which the EM algorithm has been proposed.

## 5. Contrasting AICcd, PDIO, and AIC

An evaluation of comparable expressions for AICcd, PDIO, and AIC can serve as a starting point to an investigation of the behavior of these criteria. A convenient representation for the goodness-of-fit term of AICcd is obtained by defining

$$
H\left(\boldsymbol{\theta}_{1} \mid \boldsymbol{\theta}_{2}\right)=\int_{\boldsymbol{Y}_{\mathrm{mis}}}\left\{\ln f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}_{1}\right)\right\} f\left(\boldsymbol{Y}_{\mathrm{mis}} \mid \boldsymbol{Y}_{\mathrm{obs}}, \boldsymbol{\theta}_{2}\right) \mathrm{d} \boldsymbol{Y}_{\mathrm{mis}}
$$

and by utilizing (3.1) and (2.8) to show that

$$
-2 Q\left(\boldsymbol{\theta}_{1} \mid \boldsymbol{\theta}_{2}\right)=-2 H\left(\boldsymbol{\theta}_{1} \mid \boldsymbol{\theta}_{2}\right)+\left\{-2 \ln f\left(Y_{\text {obs }} \mid \boldsymbol{\theta}_{1}\right)\right\} .
$$

By (3.20), (3.21), and (2.4), along with (5.1) and representation (4.5) for (3.19), we have

$$
\begin{aligned}
& \mathrm{AICcd}=\left\{-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)+\{-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})\}\right\}+\{2 d+2 \operatorname{trace}\{\boldsymbol{D} \\
& \mathrm{PDIO}=-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)+\left\{2 d+2 \text { trace }\left\{\boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}\right\}\right\}, \\
& \mathrm{AIC}=-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\mathrm{obs}}\right)+2 d .
\end{aligned}
$$

Each of the preceding criteria is comprised of the sum of a goodness-of-fit term and a penalty term. As the fitted model becomes more complex, the penalty term increases, whereas the goodness-of-fit term tends to decrease. (The latter behavior is a reflection of the improvement in fit which results from using larger, more flexible models.) Ideally, the fitted model which provides the optimal balance between fidelity to the data and parsimony is identified by the minimum criterion value.

The goodness-of-fit term of AIC and PDIO, $-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$, measures the conformity of the observed data $\boldsymbol{Y}_{\text {obs }}$ to the fitted model $f\left(\boldsymbol{Y}_{\text {obs }} \mid \hat{\boldsymbol{\theta}}\right)$. This term as well as the additional component $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$ comprise the goodness-of-fit term of AICcd. The component $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$ measures the conformity of the missing data $\boldsymbol{Y}_{\text {mis }}$ to the fitted model $f\left(\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}, \hat{\boldsymbol{\theta}}\right)$ in the following sense: if many realizations of $\boldsymbol{Y}_{\text {mis }}$ were generated according to the density $f\left(\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}, \hat{\boldsymbol{\theta}}\right)$, and the goodness-of-fit measure $-2 \ln f\left(\boldsymbol{Y}_{\text {mis }} \mid \boldsymbol{Y}_{\text {obs }}, \hat{\boldsymbol{\theta}}\right)$ was averaged over these realizations, this average would approximate $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$.

First, we consider the relative behavior of PDIO and AIC. These criteria share the same goodness-of-fit term, yet a comparison of (5.3) and (5.4) indicates that the penalty term of PDIO is always at least as large as the penalty term of AIC. (Recall from the discussion in Section 4 that trace $\left\{\boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}\right\}$ is always nonnegative, and is positive when $\boldsymbol{Y} \neq \boldsymbol{Y}_{\text {obs }}$.) Thus, PDIO will always choose a fitted model in a candidate class which is no larger than the model chosen by AIC. This implies that PDIO is more prone than AIC to underfitting (i.e., to choosing a model of lower dimension than the generating model), whereas AIC is more prone than PDIO to overfitting (i.e., to choosing a model of higher dimension than the generating model). These tendencies become more extreme as the amount of missing data increases, since the trace component in the penalty term of PDIO grows in relation to the amount of missing information.

We next consider the relative behavior of AICcd and PDIO. These criteria share the same penalty term, but an inspection of (5.2) and (5.3) reveals that the goodness-of-fit terms differ by the component $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$. In applications where the degree of missing information is large relative to the degree of complete information, the penalty term of PDIO often dominates its goodness-of-fit term; as a result, the criterion may tend to underfit excessively. (This behavior is exhibited in the simulations reported by

Shimodaira, 1994.) The additional component $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$ in the goodness-of-fit term of AICcd counteracts this underfitting tendency, thus providing AICcd with a certain level of protection against choosing models which are too small. This tendency will be illustrated by the simulations which follow in Sections 6 and 7.

Finally, we consider the relative behavior of AICcd and AIC. By comparing (5.2) and (5.4), we note that AICed contains extra components in both the goodness-offit term and the penalty term, each of which involve the missing information. Note that the component $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$ provides a missing-data supplement to the goodness-of-fit term of AIC in the same way that the component 2 trace $\left\{\boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}\right\}$ provides a missing-data supplement to the penalty term of AIC. It would be difficult to give a general characterization of the contribution made by the sum of these components to AICcd. However, extensive simulation results (including those which follow) indicate that in settings where the criteria do not exhibit similar selection behavior, AICcd generally tends to overfit to a lesser degree than AIC. In such instances, AICcd may tend to underfit more frequently than AIC, yet rarely to the same extent as PDIO.

To summarize, the additional penalty term which AICcd and PDIO share over AIC, 2 trace $\left\{\boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}\right\}$, penalizes a fitted model in accordance to the impact the missing data has on the model. Thus, in applications where the observed data is incomplete, AICcd and PDIO often favor lower-dimensional models than AIC. Yet unlike AICcd, PDIO does not contain the additional goodness-of-fit term $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$. The inclusion of this term attenuates the effect of the extra penalty term, and protects AICcd from the type of excessive underfitting which PDIO may exhibit when there exists a significant amount of missing information.

## 6. Simulations: Modeling bivariate normal data

Let $\mu_{1}, \mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}$, and $\sigma_{12}$ denote, respectively, the two means, two variances, and covariance for a general bivariate normal model.

Suppose we collect a data set consisting of observations on a pair of random variables $\left(y_{1}, y_{2}\right)$. To model this data, we consider a candidate class consisting of four types of bivariate normal models corresponding to certain parameter constraints. The constraints, along with the implied dimensions and estimation requirements of the associated models, are as follows:

| Dimension | Parameter constraints | Parameters to be estimated |
| :--- | :--- | :--- |
| 5 | None | $\mu_{1}, \mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}, \sigma_{12}$ |
| 4 | $\sigma_{1}^{2}=\sigma_{2}^{2} \equiv \sigma^{2}$ | $\mu_{1}, \mu_{2}, \sigma^{2}, \sigma_{12}$ |
| 3 | $\sigma_{1}^{2}=\sigma_{2}^{2} \equiv \sigma^{2}, \mu_{1}=\mu_{2} \equiv \mu$ | $\mu, \sigma^{2}, \sigma_{12}$ |
| 2 | $\sigma_{1}^{2}=\sigma_{2}^{2} \equiv \sigma^{2}, \mu_{1}=\mu_{2} \equiv \mu, \sigma_{12}=0$ | $\mu, \sigma^{2}$ |


Table 1
Dimension selections for bivariate normal simulations
|  | True dim. | $\operatorname{Pr}\left(y_{1} \mathrm{mis}\right)$, $\operatorname{Pr}\left(y_{2} \mathrm{mis}\right)$ | Dimension selections |  |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | AIC |  |  |  | PDIO |  |  |  | AICcd |  |  |  |
|  |  |  | 2 | 3 | 4 | 5 | 2 | 3 | 4 | 5 | 2 | 3 | 4 | 5 |
| 1 | 3 | 0.00, 0.00 | 1 | 799 | 118 | 82 | 1 | 799 | 118 | 82 | 1 | 799 | 118 | 82 |
| 2 | 3 | 0.15, 0.15 | 10 | 776 | 123 | 91 | 18 | 849 | 84 | 49 | 11 | 783 | 119 | 87 |
| 3 | 3 | 0.30, 0.30 | 51 | 718 | 129 | 102 | 213 | 730 | 35 | 22 | 54 | 714 | 127 | 105 |
| 4 | 3 | 0.40, 0.40 | 207 | 573 | 119 | 101 | 739 | 252 | 5 | 4 | 193 | 605 | 109 | 93 |
| 5 | 3 | 0.00, 0.00 | 0 | 813 | 122 | 65 | 0 | 813 | 122 | 65 | 0 | 813 | 122 | 65 |
| 6 | 3 | 0.15, 0.15 | 0 | 800 | 130 | 70 | 0 | 891 | 77 | 32 | 0 | 797 | 129 | 74 |
| 7 | 3 | 0.30, 0.30 | 0 | 791 | 131 | 78 | 11 | 942 | 38 | 9 | 0 | 783 | 139 | 78 |
| 8 | 3 | 0.40, 0.40 | 16 | 735 | 143 | 106 | 389 | 600 | 10 | 1 | 15 | 738 | 149 | 98 |
| 9 | 4 | 0.00, 0.00 | 0 | 0 | 850 | 150 | 0 | 0 | 850 | 150 | 0 | 0 | 850 | 150 |
| 10 | 4 | 0.15, 0.15 | 1 | 0 | 844 | 155 | 1 | 3 | 882 | 114 | 1 | 2 | 846 | 151 |
| 11 | 4 | 0.30, 0.30 | 8 | 11 | 830 | 151 | 108 | 39 | 794 | 59 | 17 | 13 | 812 | 158 |
| 12 | 4 | 0.40, 0.40 | 56 | 32 | 738 | 174 | 672 | 38 | 277 | 13 | 105 | 85 | 660 | 150 |
| 13 | 4 | 0.00, 0.00 | 0 | 0 | 860 | 140 | 0 | 0 | 860 | 140 | 0 | 0 | 860 | 140 |
| 14 | 4 | 0.15, 0.15 | 0 | 0 | 852 | 148 | 0 | 0 | 905 | 95 | 0 | 0 | 863 | 137 |
| 15 | 4 | 0.30, 0.30 | 0 | 0 | 829 | 171 | 10 | 9 | 934 | 47 | 0 | 0 | 835 | 165 |
| 16 | 4 | 0.40, 0.40 | 6 | 7 | 807 | 180 | 461 | 65 | 465 | 9 | 11 | 30 | 789 | 170 |


In each of our simulation sets, 1000 samples of size 50 are generated using a known bivariate normal model in the preceding candidate class. In some sets, certain data pairs within each sample are made incomplete by eliminating either the first or the second observation. Whether a data pair is made incomplete is determined at random according to specified discard probabilities. We will use $\operatorname{Pr}\left(y_{1} \mathrm{mis}\right)$ to denote the probability that the first observation is discarded and the second is retained, and $\operatorname{Pr}\left(y_{2}\right.$ mis $)$ to denote the probability that the second observation is discarded and the first is retained. (Thus, in a simulation set where $\operatorname{Pr}\left(y_{1}\right.$ mis $)$ and $\operatorname{Pr}\left(y_{2}\right.$ mis $)$ are both set at 0.30 , for each sample of size 50 , one would expect roughly 15 pairs where $y_{1}$ is missing but $y_{2}$ is observed, 15 pairs where $y_{1}$ is observed but $y_{2}$ is missing, and 20 pairs where $y_{1}$ and $y_{2}$ are both observed.)

For each of the 1000 samples in a set, all four models in the candidate class are fit to the data using the SEM algorithm; the criteria AIC, PDIO, and AICcd are evaluated using (2.4), (3.21), and (3.20); and the candidate model selected by each criterion is determined. The distribution of selections by each criterion is recorded for the 1000 samples and presented in Table 1. In this table, the dimension of the generating model is listed in the second column, and the discard probabilities are listed in the third column.

We include four simulation sets for each of the following generating models:

| Set numbers | True dimension | True parameter values |  |  |
| :---: | :--- | :--- | :--- | :--- |
| $1-4$ | 3 | $\mu_{1}=\mu_{2} \equiv \mu=0$, | $\sigma_{1}^{2}=\sigma_{2}^{2} \equiv \sigma^{2}=10$, | $\sigma_{12}=6$ |
| $5-8$ | 3 | $\mu_{1}=\mu_{2} \equiv \mu=0$, | $\sigma_{1}^{2}=\sigma_{2}^{2} \equiv \sigma^{2}=10$, | $\sigma_{12}=8$ |
| $9-12$ | 4 | $\mu_{1}=0, \mu_{2}=2$, | $\sigma_{1}^{2}=\sigma_{2}^{2} \equiv \sigma^{2}=10$, | $\sigma_{12}=6$ |
| $13-16$ | 4 | $\mu_{1}=0, \mu_{2}=2$, | $\sigma_{1}^{2}=\sigma_{2}^{2} \equiv \sigma^{2}=10$, | $\sigma_{12}=8$ |

For the first of the four sets corresponding to a generating model, none of the data is discarded. For the second, third, and fourth sets, the discard probabilities $\operatorname{Pr}\left(y_{1} \mathrm{mis}\right)$ and $\operatorname{Pr}\left(y_{2} \mathrm{mis}\right)$ are both set at $0.15,0.30$, and 0.40 , respectively.

When none of the data is missing, AIC, PDIO and AICcd are all equivalent, and therefore all yield the same selection results. As the discard probabilities are increased, differences in the behavior of the criteria become more apparent. The simulation results support the following conclusions.
(i) The selection performance of the criteria improves as the correlation between $y_{1}$ and $y_{2}$ is increased. Each criterion performs more effectively in sets $5-8$ than in sets 1-4, and more effectively in sets 13-16 than in sets 9-12. In the sets where data is discarded, this behavior can be easily explained. When the correlation is high, incomplete data pairs are less costly since it is possible to accurately impute the missing elements. All criteria should benefit in such a setting.
(ii) In every simulation set where data is discarded, AICcd underfits to a lesser degree than PDIO, and overfits to a comparable or to a slightly lesser degree than AIC.
(iii) As the discard probabilities are increased, PDIO becomes more prone towards selecting lower dimensional models, which results in excessive underfitting in sets 4, 8, 12, and 16. AICcd exhibits this propensity to a much lesser extent.

As mentioned in Section 5, as the discard probabilities are increased, the trace component 2 trace $\left\{\boldsymbol{D} \boldsymbol{M}(\boldsymbol{I}-\boldsymbol{D} \boldsymbol{M})^{-1}\right\}$ in the penalty term (4.5) tends to increase. The goodness-of-fit term of PDIO, $-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$, does not compensate for this behavior and as a result, becomes increasingly less competitive with the penalty term. This causes PDIO to become more prone towards selecting lower dimensional models, which results in excessive underfitting in sets $4,8,12$, and 16 . The additional goodness-of-fit component in AICcd, $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$, provides protection against this tendency.
Figs. 1-5 provide some insight into the nature of the expected complete-data discrepancy $\Delta_{Y}\left(d, \theta_{o}\right)$, the expected incomplete-data discrepancy $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$, and the estimators of these quantities provided by AICcd, PDIO, and AIC.

Figs. 1-3 illustrate the changes which occur in $\Delta_{Y}\left(d, \theta_{o}\right)$ and $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$ as the discard probabilities are increased. The samples from sets $1-4$ are used in simulating the

![](https://cdn.mathpix.com/cropped/7951e704-9b21-4411-8e2c-fdcb3acdf73d-14.jpg?height=921&width=1005&top_left_y=235&top_left_x=350)
Fig. 1. Simulated $\Delta_{Y}\left(d, \theta_{o}\right)$ and $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$ curves (bivariate normal simulation sets 1, 2).

expected discrepancies. To serve as a reference in each figure, the simulated $\Lambda_{Y}\left(d, \theta_{o}\right)$ curve from set 1 (based on no missing data) is plotted against the candidate model dimensions $d=2,3,4,5$. The simulated $\Delta_{Y}\left(d, \theta_{o}\right)$ and $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$ curves from sets 2 , 3, and 4 are overlaid in Figs. 1, 2, and 3, respectively. (For comparison purposes, each curve is translated so that its minimum at $d=3$ is set at zero. The curves are then scaled by dividing each value by the difference between the maximum and the minimum of the reference curve, $\Delta_{Y}\left(d, \theta_{o}\right)$ from set 1.)

As the discard probabilities are increased, the values of $\Delta_{Y}\left(d, \boldsymbol{\theta}_{o}\right)$ and $\Delta_{Y_{\text {obs }}}\left(d, \boldsymbol{\theta}_{o}\right)$ decrease for $d=2$ and increase for $d=4,5$. However, $\Delta_{Y}\left(d, \theta_{o}\right)$ decreases to a lesser extent than $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$ for $d=2$, and increases to a greater extent for $d=4,5$. Note that as a result, the minimum of the $\Delta_{Y}\left(d, \theta_{o}\right)$ curve becomes sharper and better defined, whereas the minimum of the $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$ curve becomes less pronounced. This phenomenon suggests that in the presence of incomplete data, an estimator of $\Delta_{Y}\left(d, \theta_{o}\right)$ may be preferable to an estimator of $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$ for the purpose of model selection, provided that the former adequately reflects the discriminatory behavior of $\Delta_{Y}\left(d, \theta_{o}\right)$.

Fig. 4 illustrates how effectively AICcd and PDIO serve as approximately unbiased estimators of $\Delta_{Y}\left(d, \theta_{o}\right)$, and Fig. 5 illustrates how effectively AIC serves as an approximately unbiased estimator of $\Delta_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$. Fig. 4 features the simulated $\Delta_{Y}\left(d, \theta_{o}\right)$ curve for simulation set 3 plotted for $d=2,3,4,5$ along with the curves which represent the

![](https://cdn.mathpix.com/cropped/7951e704-9b21-4411-8e2c-fdcb3acdf73d-15.jpg?height=926&width=1008&top_left_y=233&top_left_x=339)
Fig. 2. Simulated $\Delta_{Y}\left(d, \theta_{o}\right)$ and $\Delta_{Y_{\mathrm{obs}}}\left(d, \theta_{o}\right)$ curves (bivariate normal simulation sets 1, 3).

average values of AICcd and PDIO. In Fig. 5, the simulated $\Delta_{Y_{\text {obs }}}\left(d, \boldsymbol{\theta}_{o}\right)$ curve for set 3 is plotted for $d=2,3,4,5$ along with the curve which represents the average values of AIC. (Each curve has been translated so that its minimum at $d=3$ is set at zero. The curves in Fig. 4 are then scaled by dividing each value by the difference between the maximum and the minimum of the reference $A_{Y}\left(d, \theta_{o}\right)$ curve. The curves in Fig. 5 are similarly scaled using the reference $A_{Y_{\text {obs }}}\left(d, \theta_{o}\right)$ curve.)

Note that the average AICcd and AIC curves respectively follow the simulated $\Delta_{Y}\left(d, \theta_{o}\right)$ and $\Delta_{Y_{\mathrm{obs}}}\left(d, \theta_{o}\right)$ curves to a comparable degree. Both the AICcd and AIC curves exhibit a more gradual slope than the corresponding expected discrepancy curves over $d=3,4,5$. The average PDIO curve tracks $\Delta_{Y}\left(d, \theta_{o}\right)$ more effectively than the AICcd curve over these dimensions, yet assumes a value at $d=2$ which is much lower than $\Delta_{Y}\left(d, \theta_{o}\right)$. This type of behavior is more pronounced in simulation sets with higher discard probabilities, and helps to illustrate why the PDIO criterion is often prone to underfitting.

The preceding section of simulations considers the performance of the criteria in a simplistic, illustrative setting, albeit one where the use of model selection criteria would not be typically employed. In the next section, we consider the behavior of the criteria in a more practical, traditional framework.

![](https://cdn.mathpix.com/cropped/7951e704-9b21-4411-8e2c-fdcb3acdf73d-16.jpg?height=928&width=1005&top_left_y=233&top_left_x=346)
Fig. 3. Simulated $A_{Y}\left(d, \theta_{o}\right)$ and $\Delta_{Y_{\mathrm{obs}}}\left(d, \theta_{o}\right)$ curves (bivariate normal simulation sets 1,4 ).

## 7. Simulations: Multivariate regression modeling

Consider the multivariate regression model

$$
\boldsymbol{Y}=\boldsymbol{X} \boldsymbol{\beta}+\boldsymbol{U},
$$

where the $n \times p$ matrix $\boldsymbol{Y}$ consists of rows which are independent, $p$-dimensional random vectors, the $n \times m$ matrix $X$ is a known design matrix of covariate values, and the $m \times p$ matrix $\boldsymbol{\beta}$ is an unknown matrix of regression parameters. The $n \times p$ matrix $\boldsymbol{U}$ is comprised of rows which are independent $p$-variate normal random vectors, each with a mean vector of zero and a variance/covariance matrix $\boldsymbol{\Sigma}$.

One of the most important problems in regression modeling is that of choosing the number of predictors to include in the model; i.e., of determining the size of the design matrix $X$. If $m$ regressors are retained for a candidate regression model, the overall dimension of the model is given by $d=m p+p(p+1) / 2$.

We consider a setting where $p=2$, so that the rows of $\boldsymbol{Y}$ represent bivariate data pairs. The design matrices $\boldsymbol{X}$ for our class of candidate models range in size from $m=1$ column to $m=8$ columns, representing models of dimension $d=5$ through $d=19$. We assume that the candidate models are nested; i.e., if $\boldsymbol{X}_{1}$ has $m_{1}$ columns and $\boldsymbol{X}_{2}$ has $m_{2}$ columns where $m_{1}<m_{2}$, the columns of $\boldsymbol{X}_{1}$ comprise the first $m_{1}$ columns of $\boldsymbol{X}_{2}$.

![](https://cdn.mathpix.com/cropped/7951e704-9b21-4411-8e2c-fdcb3acdf73d-17.jpg?height=921&width=1008&top_left_y=231&top_left_x=339)
Fig. 4. Simulated $\Delta_{Y}\left(d, \theta_{o}\right)$ curve and average AICcd, PDIO curves (bivariate normal simulation set 3).

The first column of each $\boldsymbol{X}$ is taken to be a vector of ones. The covariate values are generated by taking independent measurements on a random variable having a uniform distribution on the interval $(0,5)$. Setting up the design matrices in this simplistic fashion ensures that the simulation results are not unduly influenced by such factors as multicollinearity and high-leverage cases.

For each simulation set, 1000 response matrices $\boldsymbol{Y}$ of dimension $50 \times 2$ are generated from a model having the form

$$
\boldsymbol{Y}=\boldsymbol{X}_{o} \boldsymbol{\beta}_{o}+\boldsymbol{U} \quad \text { where } \boldsymbol{\Sigma}=\left[\begin{array}{rr}
4 & 7 \\
7 & 16
\end{array}\right]
$$

Thus, the response variable represented in the first column of $\boldsymbol{Y}, y_{1}$, is much less variable than the response variable represented in the second column of $\boldsymbol{Y}, y_{2}$.

Three different parameter matrices $\boldsymbol{\beta}_{o}$ are used. For each $\boldsymbol{\beta}_{o}$, a collection of five simulation sets are run with the pair of discard probabilities ( $\operatorname{Pr}\left(y_{1}\right.$ mis), $\operatorname{Pr}\left(y_{2}\right.$ mis $\left.)\right)$ set at $(0.00,0.00),(0.00,0.60),(0.20,0.40),(0.40,0.20)$, and $(0.60,0.00)$. The $m_{o} \times 2$ parameter matrices $\boldsymbol{\beta}_{o}$ have all elements set equal to 1 , and have sizes determined by $m_{o}=3\left(d_{o}=9\right), m_{o}=5\left(d_{o}=13\right)$, and $m_{o}=7\left(d_{o}=17\right)$. The fifteen sets corresponding to these three $\boldsymbol{\beta}_{o}$ are labeled 1-5, 6-10, and 11-15, respectively.

For each of the 1000 samples in a set, all 8 models in the candidate class are fit to the data using the SEM algorithm; the criteria AIC, PDIO, and AICcd are evaluated

![](https://cdn.mathpix.com/cropped/7951e704-9b21-4411-8e2c-fdcb3acdf73d-18.jpg?height=919&width=1003&top_left_y=233&top_left_x=342)
Fig. 5. Simulated $\Delta_{Y_{\text {obs }}}\left(d, \boldsymbol{\theta}_{o}\right)$ curve and average AIC curve (bivariate normal simulation set 3).

using (2.4), (3.21), and (3.20); and the candidate model selected by each criterion is determined. The distribution of selections by each criterion is recorded for the 1000 samples and presented in Table 2. In this table, the dimension of the generating model $d_{o}$ is listed in the second column, and the discard probabilities for the samples are listed in the third column. For brevity, we group the dimension selections into three categories: ' $<d_{o}$ ' (underfitting), ' $d_{o}$ ' (correct dimension), and ' $>d_{o}$ ' (overfitting).

The results of the simulations support the following conclusions.
(i) As the dimension of the generating model $d_{o}$ is increased, each criterion tends to become more prone towards underfitting and less prone towards overfitting.
(ii) In every simulation set where data is discarded, AICcd overfits to a lesser degree than AIC and underfits to a lesser degree than PDIO. Moreover, although PDIO often obtains more correct dimension selections than AICcd, AICcd maintains the greatest level of consistency as a selection criterion. In sets where AIC demonstrates a strong propensity towards overfitting (e.g., 7), and in sets where PDIO demonstrates a strong propensity towards underfitting (e.g., 15), AICcd exhibits these tendencies to a much lesser extent.
(iii) In the simulation sets where data is discarded, $\operatorname{Pr}\left(y_{1} \mathrm{mis}\right)+\operatorname{Pr}\left(y_{2} \mathrm{mis}\right)$ is held constant at 0.60 . Yet as $\operatorname{Pr}\left(y_{1} \mathrm{mis}\right)$ is increased and $\operatorname{Pr}\left(y_{2} \mathrm{mis}\right)$ is decreased, PDIO becomes more prone towards selecting lower dimensional models; this results in

Table 2
Dimension selections for multivariate regression simulations
| Set | True $\operatorname{dim} .: d_{o}$ | $\operatorname{Pr}\left(y_{1} \mathrm{mis}\right)$, $\operatorname{Pr}\left(y_{2} \mathrm{mis}\right)$ | Dimension selections |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | AIC |  |  | PDIO |  |  | AICcd |  |  |
|  |  |  | $<d_{o}$ | $d_{o}$ | $>d_{o}$ | $<d_{o}$ | $d_{o}$ | $>d_{o}$ | $<d_{o}$ | $d_{o}$ | $>d_{o}$ |
| 1 | 9 | 0.00, 0.00 | 0 | 713 | 287 | 0 | 713 | 287 | 0 | 713 | 287 |
| 2 | 9 | 0.00, 0.60 | 1 | 606 | 393 | 31 | 912 | 57 | 13 | 722 | 265 |
| 3 | 9 | 0.20, 0.40 | 3 | 618 | 379 | 41 | 904 | 55 | 13 | 724 | 263 |
| 4 | 9 | 0.40, 0.20 | 2 | 636 | 362 | 76 | 874 | 50 | 21 | 739 | 240 |
| 5 | 9 | 0.60, 0.00 | 9 | 611 | 380 | 188 | 768 | 44 | 45 | 697 | 258 |
| 6 | 13 | 0.00, 0.00 | 0 | 710 | 290 | 0 | 710 | 290 | 0 | 710 | 290 |
| 7 | 13 | 0.00, 0.60 | 0 | 598 | 402 | 72 | 885 | 43 | 31 | 759 | 210 |
| 8 | 13 | 0.20, 0.40 | 0 | 628 | 372 | 85 | 862 | 53 | 27 | 758 | 215 |
| 9 | 13 | 0.40, 0.20 | 3 | 636 | 361 | 112 | 837 | 51 | 23 | 771 | 206 |
| 10 | 13 | 0.60, 0.00 | 8 | 598 | 394 | 305 | 660 | 35 | 84 | 709 | 207 |
| 11 | 17 | 0.00, 0.00 | 0 | 792 | 208 | 0 | 792 | 208 | 0 | 792 | 208 |
| 12 | 17 | 0.00, 0.60 | 0 | 697 | 303 | 219 | 760 | 21 | 127 | 725 | 148 |
| 13 | 17 | 0.20, 0.40 | 0 | 731 | 269 | 177 | 782 | 41 | 73 | 778 | 149 |
| 14 | 17 | 0.40, 0.20 | 9 | 726 | 265 | 289 | 680 | 31 | 89 | 778 | 133 |
| 15 | 17 | 0.60, 0.00 | 17 | 685 | 298 | 462 | 509 | 29 | 157 | 704 | 139 |


excessive underfitting in sets such as 5, 10, and 15. AICcd exhibits this tendency to a much lesser extent.

Since $\operatorname{Var}\left(y_{1}\right)=4$ and $\operatorname{Var}\left(y_{2}\right)=16$, increasing $\operatorname{Pr}\left(y_{1}\right.$ mis) and decreasing $\operatorname{Pr}\left(y_{2} \mathrm{mis}\right)$ results in discarding a larger percentage of the less variable data and retaining a higher percentage of the noisier data. This causes the goodness-of-fit term of PDIO, $-2 \ln L\left(\hat{\boldsymbol{\theta}} \mid \boldsymbol{Y}_{\text {obs }}\right)$, to become less effective against its penalty term, which will be large since $\operatorname{Pr}\left(y_{1} \mathrm{mis}\right)+\operatorname{Pr}\left(y_{2} \mathrm{mis}\right)$ is substantial. As a result, PDIO increasingly favors lower dimensional models. In sets such as 5,10 , and 15, this tendency results in PDIO underfitting to an excessive degree. Here again, the additional goodness-of-fit component in AICcd, $-2 H(\hat{\boldsymbol{\theta}} \mid \hat{\boldsymbol{\theta}})$, provides protection against this behavior.

## 8. Conclusion

In Sections 2-5, we derived and discussed an analogue of AIC for model selection in applications where the observed data is incomplete. Our criterion estimates the expected complete-data Kullback-Leibler discrepancy in the same manner that Akaike's (1973, 1974) AIC estimates the expected incomplete-data discrepancy.

AIC lacks the property of consistency, but is asymptotically efficient in the sense of Shibata (1980), which is arguably a property of greater practical value. (See, for
example, Hurvich and Tsai, 1989; Bhansali, 1993.) AICcd should possess the same asymptotic properties as AIC under the assumption that the proportion of missing information to complete information tends to zero as the degree of complete information (i.e., the overall sample size) tends to infinity. Establishing the properties of AICcd when this assumption is not met is a topic for future investigation.

As a model selection criterion, AIC performs effectively in a large variety of applications. However, recent work has shown that in settings where the sample size is small relative to the dimension of the largest model in the candidate class, AIC provides an estimator of the expected discrepancy which is significantly negatively biased. 'Corrected' variants of AIC which compensate for this small-sample bias have been developed for such applications: see Hurvich and Tsai (1989), Hurvich et al. (1990), and Bedrick and Tsai (1994). In future work, we hope to develop analogous 'corrected' variants of AICcd, since AICcd itself will exhibit substantial negative bias in the type of settings previously mentioned.

Our simulations in Sections 6 and 7 indicate that in the presence of incomplete data, AICcd tends to underfit to a lesser degree than PDIO, and tends to overfit to a lesser degree than AIC. AICcd achieves the latter by incorporating a penalization for missing information which is lacking in AIC; it achieves the former by incorporating a goodness-of-fit term for missing information which is lacking in PDIO.

AICcd is based entirely on complete-data tools. Unlike AIC and PDIO, it does not require the evaluation of the observed-data empirical log-likelihood, which may be problematic or burdensome to compute. Thus, AICcd can be easily evaluated in the framework of the SEM algorithm without any additional programming. This important property of AICcd, along with its promising performance in our simulation sets, will hopefully encourage the usage and further investigation of this criterion as well as others based on complete-data tools and principles.

## Acknowledgements

We wish to extend our sincere appreciation to an associate editor and a referee for carefully reading the original version of this manuscript, and for preparing helpful and constructive critiques which served to greatly improve the exposition and content. We also extend our thanks to the editor.

The work of the first author was supported by grants from the Research Board of the University of Missouri and the Research Council of the University of MissouriColumbia.

## References

Akaike, H., 1973. Information theory and an extension of the maximum likelihood principle. In: Petrov, B.N., Csaki, F. (Eds.), Proc. 2nd Internat. Symp. on Inform. Theory. Akademia Kiado, Budapest, pp. 267-281. Akaike, H., 1974. A new look at the statistical model identification. IEEE Trans. Automat. Control AC-19, 716-723.

Bedrick, E.J., Tsai, C.L., 1994. Model selection for multivariate regression in small samples. Biometrics 50, 226-231.
Bhansali, R.J., 1993. Order selection for linear time series models: A review. In: Rao, T.S. (Ed.), Developments in Time Series Analysis. Chapman \& Hall, London, pp. 50-66.
Dempster, A.P., Laird, N.M., Rubin, D.B., 1977. Maximum likelihood estimation from incomplete data via the EM algorithm (with discussion). J. Roy. Statist. Soc. Ser. B 39, 1-38.
Goodman, L.A., 1974. Exploratory latent structure models using both identifiable and unidentifiable models. Biometrika 61, 315-331.
Hurvich, C.M., Shumway, R.H., Tsai, C.L., 1990. Improved estimators of Kullback-Leibler information for autoregressive model selection in small samples. Biometrika 77, 709-719.
Hurvich, C.M., Tsai, C.L., 1989. Regression and time series model selection in small samples. Biometrika 76, 297-307.
Kullback, S., 1968. Information Theory and Statistics. Dover, New York.
Linhart, H., Zucchini, W., 1986. Model Selection. Wiley, New York.
Little, R.J.A., 1979. Maximum likelihood inference for multiple regression with missing values: A simulation study. J. Roy. Statist. Soc. Ser. B 41, 76-87.
Little, R.J.A., Rubin, D.B., 1987. Statistical Analysis with Missing Data. Wiley, New York.
Meng, X.L., Rubin, D.B., 1991. Using EM to obtain asymptotic variance-covariance matrices: The SEM algorithm. J. Amer. Statist. Assoc. 86, 899-909.
Rubin, D.B., 1976. Noniterative least squares estimates, standard errors and $F$-tests for any analysis of variance with missing data. J. Roy. Statist. Soc. Ser. B 38, 270-274.
Shibata, R., 1980. Asymptotically efficient selection of the order of the model for estimating parameters of a linear process. Ann. Statist. 80, 147-164.
Shimodaira, H., 1994. A new criterion for selecting models from partially observed data. In: Cheeseman, P., Oldford, R.W. (Eds.), Selecting Models from Data: Artificial Intelligence and Statistics IV, Lecture Notes in Statistics, vol. 89. Springer, New York, pp. 21-29.
Shumway, R.H., Stoffer, D.S., 1982. An approach to time series smoothing and forecasting using the EM algorithm. J. Time Series Anal. 3, 253-264.
Titterington, D.M., Smith, A.F.M., Makov, U.E., 1985. Statistical Analysis of Finite Mixture Distributions. Wiley, New York.


[^0]:    *Corresponding author.

