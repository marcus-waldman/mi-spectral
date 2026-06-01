---
citekey: kandaBasicPropertiesMles1998
item_type: article
authors: 'Kanda, Takashi and Fujikoshi, Yasunori'
year: 1998
title: 'Some {Basic Properties} of the {Mle}''s for a {Multivariate Normal Distribution} with {Monotone Missing Data}'
venue: American Journal of Mathematical and Management Sciences
volume: 18
issue: 1-2
pages: 161--192
doi: 10.1080/01966324.1998.10737458
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\kanda_some_basic_properties_1998.pdf'
pdf_sha256: 2bd68f1bc2d1f744d75775880273619c14aaf47e7d0bd9d14c25ba6cd8039470
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T23:14:22Z
---
# Some Basic Properties of the Mle's for a Multivariate Normal Distribution with Monotone Missing Data 

Takashi Kanda \& Yasunori Fujikoshi

To cite this article: Takashi Kanda \& Yasunori Fujikoshi (1998) Some Basic Properties of the Mle's for a Multivariate Normal Distribution with Monotone Missing Data, American Journal of Mathematical and Management Sciences, 18:1-2, 161-192, DOI: 10.1080/01966324.1998.10737458

To link to this article: https://doi.org/10.1080/01966324.1998.10737458

Published online: 14 Aug 2013.

Submit your article to this journal

Article views: 125

View related articles

Citing articles: 5 View citing articles

# SOME BASIC PROPERTIES OF THE MLE'S FOR A MULTIVARIATE NORMAL DISTRIBUTION WITH MONOTONE MISSING DATA 

Takashi Kanda<br>Hiroshima Institute of Technology<br>Hiroshima 731-5193, Japan

Yasunori Fujikoshi<br>Hiroshima University<br>Higashi-Hiroshima 739-8526, Japan

## SYNOPTIC ABSTRACT

In this paper we study some basic properties of the MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\boldsymbol{\Sigma}}$ for a $p$-variate normal population $N_{p}(\mu, \Sigma)$, based on a $k$-step monotone sample. For $k=2$ and 3 , we obtain the exact means and variances of $\hat{\boldsymbol{\mu}}$ and the exact bias of $\hat{\Sigma}$. Asymptotic expansions of the distributions of these estimators are also obtained in the situation when the sample size is large. For a general $k$, the MLE's of $\boldsymbol{\mu}$ and the usual transformed matrix $\Delta$ of $\Sigma$ are given in explicit forms. Some analogous properties are also obtained.

Key Words and Phrases: multivariate normal distribution; monotone missing data; MLE's; mean and variance; exact distribution; asymptotic distribution.

1998, VOL. 18, NOS. 1 \& 2, 161-190
0196-6324/98/020161-30 \$35.00

## 1. INTRODUCTION

In statistical data analysis we frequently face the situation where there are missing observations. Many statistical methods have been developed for analyzing the data with missing observations (see, e.g., Dempster, Laird and Rubin (1977), Srivastava (1985), Little and Rubin (1987)). However, it has not been sufficiently done to study statistical properties of these methods. This is because for a general missing pattern being not monotone, there are some troublesome problems even in statistical inference for the parameters of a multivariate normal distribution $N_{p}(\mu, \Sigma)$. For example, the parameter $\Sigma$ may or may not be identifiable, conditions for existence and uniqueness of the MLE's of ( $\boldsymbol{\mu}, \Sigma$ ) are not expressible in convenient form, as being pointed by Anderson and Perlman (1991).

In this paper we consider a monotone missing data pattern, which was dealt by Anderson (1957) in the bivariate case, Bhargava (1975), Jinadasa and Tracy (1992) and Fujisawa (1995). Let $\boldsymbol{x}$ be distributed as $N_{p}(\boldsymbol{\mu}, \Sigma)$, and $\boldsymbol{x}^{(i)}$ the vector of the first $q_{i}$ elements of $\boldsymbol{x}$, where $p=q_{1}>q_{2}>\cdots>q_{k}>0$. We partition $\boldsymbol{x}$ as

$$
\boldsymbol{x}=\left(\boldsymbol{x}_{1}^{\prime}, \ldots, \boldsymbol{x}_{\boldsymbol{k}}^{\prime}\right)^{\prime}, \quad \boldsymbol{x}_{i}: p_{i} \times 1,
$$

and $p_{1}+\cdots+p_{i}=q_{k-i+1}$ for $i=1, \ldots, k$. Then

$$
\boldsymbol{x}^{(1)}=\left(\boldsymbol{x}_{1}^{\prime}, \ldots, \boldsymbol{x}_{k}^{\prime}\right)^{\prime}, \boldsymbol{x}^{(2)}=\left(\boldsymbol{x}_{1}^{\prime}, \ldots, \boldsymbol{x}_{k-1}^{\prime}\right)^{\prime}, \ldots, \boldsymbol{x}^{(k)}=\boldsymbol{x}_{1} .
$$

Suppose we have $N_{1}$ observations on $\boldsymbol{x}^{(1)}, N_{2}$ observations on $\boldsymbol{x}^{(2)}$, and so on. Let $\boldsymbol{x}_{j}^{(i)}$ be the $j$ th observation on $\boldsymbol{x}^{(i)}$. Such a sample is called a $k$ step monotone sample (Bhargava (1975), Srivastava and Carter (1983)), or a $k$-step monotone missing data pattern (Little and Rubin (1987)). Here it is assumed that the marginal density function of the observed data set $\left\{\boldsymbol{x}_{1}^{(1)}, \ldots, \boldsymbol{x}_{N_{1}}^{(1)}, \ldots, \boldsymbol{x}_{1}^{(k)}, \ldots, \boldsymbol{x}_{N_{k}}^{(k)}\right\}$ is

$$
\prod_{i=1}^{k} \prod_{j=1}^{N_{i}} f\left(\boldsymbol{x}_{j}^{(i)} ; \boldsymbol{\mu}_{[i]}, \Sigma_{(1, \ldots, i)(1, \ldots, i)}\right),
$$

where $f\left(\boldsymbol{x}_{j}^{(i)} ; \boldsymbol{\mu}_{[i]}, \Sigma_{(1, \ldots, i)(1, \ldots, i)}\right)$ is the density function of
$N_{q_{k-i+1}}\left(\mu_{[i]}, \Sigma_{(1, \ldots, i)(1, \ldots, i)}\right)$ and

$$
\begin{gathered}
\boldsymbol{\mu}_{[i]}=\left(\begin{array}{c}
\boldsymbol{\mu}_{1} \\
\boldsymbol{\mu}_{2} \\
\vdots \\
\boldsymbol{\mu}_{i}
\end{array}\right), \quad \Sigma_{(1, \ldots, i)(1, \ldots, i)}=\left(\begin{array}{cccc}
\Sigma_{11} & \Sigma_{12} & \cdots & \Sigma_{1 i} \\
\Sigma_{21} & \Sigma_{22} & \cdots & \Sigma_{2 i} \\
\vdots & \vdots & \ddots & \vdots \\
\Sigma_{i 1} & \Sigma_{i 2} & \cdots & \Sigma_{i i}
\end{array}\right), \\
\boldsymbol{\mu}_{j}: p_{j} \times 1(j=1, \ldots, i), \quad \Sigma_{j l}: p_{j} \times p_{l}(j, l=1, \ldots, i) .
\end{gathered}
$$

In this paper we consider the likelihood inference based on the density function (1) which is conditional on the observed pattern of missing data. This likelihood inference will be the same as the one based on an appropriate process which causes missing data. For related processes of missing data, see, e.g., Rubin $(1974,1976)$. The MLE's of $\boldsymbol{\mu}$ and $\Sigma$ are defined as the values of $\mu$ and $\Sigma$ maximizing the density function (1). We assume $N_{1}>p$; this is a necessary and sufficient condition for existence and uniqueness of the MLE's of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ (see, Section 4). Anderson (1957) and Anderson and Olkin (1985) considered a 2 -step monotone sample and obtained the MLE's of parameters of a normal distribution.

There are two methods of obtaining the MLE's; one is to use the decomposition of the density into conditional densities, and the other is to use matrix differentiation. The conditional method was used by Anderson (1957) in the case $k=2$, and for a general $k$ Bhargava (1975) have considered the MLE's, relating to three testing problems, but he didn't give them in a closed form. Recently, Fujisawa (1995) has obtained the estimators by the conditional approach. On the other hand, the method of using matrix differentiation was used by Anderson and Olkin (1985) in the case $k=2$. Jinadasa and Tracy (1992) obtained them in a successive representation.

The purpose of this paper is to study some fundamental properties of the MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\boldsymbol{\Sigma}}$ of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$. In general, it becomes difficult to derive the exact properties of these estimators except for some special cases. So we also study the asymptotic properties of these estimators in a situation when

$$
\rho_{i}=n_{i} / n \longrightarrow \text { positive constants }
$$

as $N_{i}$ 's tend to infinity, where $n_{i}=N_{i}-1$ and $n=n_{1}+\cdots+n_{k}$. For $k=2$ and 3, we obtain the exact means and variances of $\hat{\boldsymbol{\mu}}$ and the exact bias of $\hat{\Sigma}$ and its transformed parameter matrix $\hat{\Delta}$. Asymptotic expansions of the distributions
of these estimators are also obtained in the situation when the sample size is large. These results in the cases $k=2$ and 3 are given in Sections 2 and 3, respectively. In Section 4 the MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\Delta}$ are given in explicit forms. Some analogous properties are also obtained.

## 2. 2-STEP MONOTONE MISSING DATA

In this section, we consider the case $k=2$. Let the $p$-dimensional variate $\boldsymbol{x}$ be decomposed as $\left(\boldsymbol{x}_{1}^{\prime}, \boldsymbol{x}_{2}^{\prime}\right)^{\prime}$, where $\boldsymbol{x}_{1}$ and $\boldsymbol{x}_{2}$ are $p_{1}$ and $p_{2}$-dimensional vectors, respectively. Suppose that we have $N_{1}$ observations on the full set of variables, i.e., $\boldsymbol{x}$, and $N_{2}$ observations on $\boldsymbol{x}_{1}$, and these observations are independently distributed. We introduce some notation for the sample means and covariance matrices. Let $\overline{\boldsymbol{x}}^{(1)}$ denote the sample mean of $\boldsymbol{x}$ based on the $N_{1}$ observations, and $\overline{\boldsymbol{x}}^{(1)}=\left(\overline{\boldsymbol{x}}_{1}^{(1)^{\prime}}, \overline{\boldsymbol{x}}_{2}^{(1)^{\prime}}\right)^{\prime}, \overline{\boldsymbol{x}}_{i}^{(1)}: p_{i} \times 1$. Let $\overline{\boldsymbol{x}}^{(2)}$ denote the sample mean for the $p_{1}$-dimensional elements of $\boldsymbol{x}_{1}$ based on the $N_{2}$ observations. Throughout this paper, we use the letter $\alpha$ only as running suffix for sample observations. Then the sample covariance matrices based on the $N_{1}$ and $N_{2}$ observations are expressed as

$$
\begin{aligned}
& S^{(1)}=\frac{1}{n_{1}} \sum_{\alpha=1}^{N_{1}}\left(\boldsymbol{x}_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)\left(\boldsymbol{x}_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)^{\prime}, \\
& S^{(2)}=\frac{1}{n_{2}} \sum_{\alpha=1}^{N_{2}}\left(\boldsymbol{x}_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)\left(\boldsymbol{x}_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)^{\prime},
\end{aligned}
$$

respectively, where $n_{i}=N_{i}-1, i=1,2$.
Let the partitions of $\boldsymbol{\mu}, \Sigma$ and $S^{(1)}$ corresponding to the ones of $\boldsymbol{x}$ be

$$
\boldsymbol{\mu}=\binom{\boldsymbol{\mu}_{1}}{\boldsymbol{\mu}_{2}}, \quad \Sigma=\left(\begin{array}{cc}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{array}\right), \quad S^{(1)}=\left(\begin{array}{cc}
S_{11}^{(1)} & S_{12}^{(1)} \\
S_{21}^{(1)} & S_{22}^{(1)}
\end{array}\right) .
$$

### 2.1. MLE's

Let the MLE's of $\boldsymbol{\mu}$ and $\Sigma$ denote by $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$, which are partitioned in the same way as $\boldsymbol{\mu}$ and $\Sigma$. Then we can write the MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\boldsymbol{\Sigma}}$ (Anderson and Olkin (1985)) as

$$
\hat{\boldsymbol{\mu}}_{1}=\frac{1}{N}\left(N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}^{(2)}\right), \quad \hat{\boldsymbol{\mu}}_{2}=\overline{\boldsymbol{x}}_{2}^{(1)}-\hat{\Sigma}_{21} \hat{\Sigma}_{11}^{-1}\left(\overline{\boldsymbol{x}}_{1}^{(1)}-\hat{\boldsymbol{\mu}}_{1}\right),
$$



$$
\begin{aligned}
& \hat{\Sigma}_{11}=\frac{1}{N}\left(W_{11}^{(1)}+W^{(2)}\right), \quad \hat{\Sigma}_{12}=\hat{\Sigma}_{11}\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}, \\
& \hat{\Sigma}_{22}=\frac{1}{N_{1}} W_{22 \cdot 1}^{(1)}+\hat{\Sigma}_{21} \hat{\Sigma}_{11}^{-1} \hat{\Sigma}_{12},
\end{aligned}
$$

where $N=N_{1}+N_{2}$,

$$
\begin{aligned}
& W^{(1)}=n_{1} S^{(1)}, \quad W^{(2)}=n_{2} S^{(2)}+\frac{N_{1} N_{2}}{N}\left(\overline{\boldsymbol{x}}_{1}^{(1)}-\overline{\boldsymbol{x}}^{(2)}\right)\left(\overline{\boldsymbol{x}}_{1}^{(1)}-\overline{\boldsymbol{x}}^{(2)}\right)^{\prime}, \\
& W^{(1)}=\left(\begin{array}{ll}
W_{11}^{(1)} & W_{12}^{(1)} \\
W_{21}^{(1)} & W_{22}^{(1)}
\end{array}\right), \quad W_{22 \cdot 1}^{(1)}=W_{22}^{(1)}-W_{21}^{(1)}\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)} .
\end{aligned}
$$

In the conditional approach, it is simple to treat the usual transformed parameters defined by

$$
\boldsymbol{\eta}=\binom{\boldsymbol{\eta}_{1}}{\boldsymbol{\eta}_{2}}, \quad \Delta=\left(\begin{array}{ll}
\Delta_{11} & \Delta_{12} \\
\Delta_{21} & \Delta_{22}
\end{array}\right),
$$

where

$$
\begin{gathered}
\boldsymbol{\eta}_{1}=\boldsymbol{\mu}_{1}, \quad \boldsymbol{\eta}_{2}=\boldsymbol{\mu}_{2}-\Delta_{21} \boldsymbol{\mu}_{1} \\
\Delta_{11}=\Sigma_{11}, \quad \Delta_{12}=\Delta_{21}^{\prime}=\Sigma_{11}^{-1} \Sigma_{12}, \quad \Delta_{22}=\Sigma_{22 \cdot 1}=\Sigma_{22}-\Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12},
\end{gathered}
$$

which are one to one correspondence to $(\boldsymbol{\mu}, \Sigma)$.
The MLE's of ( $\boldsymbol{\eta}, \Delta$ ) are expressed as follows:

$$
\begin{gathered}
\hat{\boldsymbol{\eta}}_{1}=\hat{\boldsymbol{\mu}}_{1}, \quad \hat{\boldsymbol{\eta}}_{2}=\overline{\boldsymbol{x}}_{2}^{(1)}-\hat{\Delta}_{21} \overline{\boldsymbol{x}}_{1}^{(1)} \\
\hat{\Delta}_{11}=\hat{\Sigma}_{11}, \quad \hat{\Delta}_{12}=\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}, \quad \hat{\Delta}_{22}=\frac{1}{N_{1}} W_{22 \cdot 1}^{(1)}
\end{gathered}
$$

### 2.2. Means and Variances of $\hat{\mu}$ and $\hat{\Sigma}$

First we prepare a preliminary lemma which is useful in deriving exact means and variances of $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$.

Lemma 2.1. Suppose that $A$ is distributed as a Wishart distribution $W_{p}(\Sigma, n)$ and $n \geq p$, where $A$ is partitioned as in the partition of $\Sigma$, and let $A_{22 \cdot 1}=A_{22}-A_{21} A_{11}^{-1} A_{12}$. Then
(i) $\quad A_{22 \cdot 1} \sim W_{p_{2}}\left(\Sigma_{22 \cdot 1}, n-p_{1}\right)$, and $A_{22 \cdot 1}$ is independent of $A_{11}$ and $A_{12}$,
(ii) The conditional distribution of $\operatorname{Vec}\left(A_{12}\right)$ given $A_{11}$ is $N\left(\operatorname{Vec}\left(A_{11} \Sigma_{11}^{-1} \Sigma_{12}\right), \Sigma_{22 \cdot 1} \otimes A_{11}\right)$, and in particular $\mathrm{E}\left[A_{11}^{-1} A_{12}\right]=\Sigma_{11}^{-1} \Sigma_{12}$, where $\operatorname{Vec}(C)$ denotes the column vector formed by stacking the columns of $C$ under each other,
(iii) $\quad A_{11} \sim W_{p_{1}}\left(\Sigma_{11}, n\right)$,
(iv) if $n-p-1>0, \mathrm{E}\left[A^{-1}\right]=\frac{1}{n-p-1} \Sigma^{-1}$,
(v) if $n-p_{1}-1>0$, $\mathrm{E}\left[A_{21} A_{11}^{-1} C A_{11}^{-1} A_{12}\right]=\mathrm{E}\left[\operatorname{tr} A_{11}^{-1} C\right] \Sigma_{22 \cdot 1}+\Sigma_{21} \Sigma_{11}^{-1} \mathrm{E}[C] \Sigma_{11}^{-1} \Sigma_{12}$,
where $C$ is a random matrix depending on $A_{11}$.
Proof. The results (i) ~ (iv) are well known. For a proof, see Muirhead (1982) and Siotani, Hayakawa and Fujikoshi (1985). The result (v) follows from (ii) and (iv).

Theorem 2.1. Suppose that $N_{1}>p$. Then, the mean vector and the covariance matrix of $\hat{\boldsymbol{\mu}}$ are given by
(i) $\quad \mathrm{E}[\hat{\boldsymbol{\mu}}]=\boldsymbol{\mu}$,
(ii) $\quad \operatorname{Var}[\hat{\boldsymbol{\mu}}]=\left(\begin{array}{cc}\frac{1}{N} \Sigma_{11} & \frac{1}{N} \Sigma_{12} \\ \frac{1}{N} \Sigma_{21} & \operatorname{Var}\left(\hat{\boldsymbol{\mu}}_{2}\right)\end{array}\right),\left(N_{1}>p_{1}+2\right)$,
where

$$
\operatorname{Var}\left(\hat{\boldsymbol{\mu}}_{2}\right)=\frac{1}{N_{1}}\left(\Sigma_{22}-\frac{N_{2}}{N} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right)+\frac{N_{2} p_{1}}{N N_{1}\left(N_{1}-p_{1}-2\right)} \Sigma_{22 \cdot 1} .
$$

Proof. Most results except for $\operatorname{Var}\left(\hat{\boldsymbol{\mu}}_{2}\right)$ are easily derived by using that $\overline{\boldsymbol{x}}^{(1)} \sim N\left(\boldsymbol{\mu}, N_{1}^{-1} \Sigma\right), \overline{\boldsymbol{x}}^{(2)} \sim N\left(\boldsymbol{\mu}_{1}, N_{2}^{-1} \Sigma_{11}\right), \hat{\Sigma}_{21} \hat{\Sigma}_{11}^{-1}=A_{21} A_{11}^{-1}$, where $A_{i j}$ are the same ones as in Lemma 2.1 with $n=n_{1}$, and these are independent. So, we consider $\operatorname{Var}\left[\hat{\boldsymbol{\mu}}_{2}\right]$ only. We can write

$$
\begin{aligned}
\operatorname{Var}\left(\hat{\boldsymbol{\mu}}_{2}\right)= & \mathrm{E}\left[\left(\hat{\boldsymbol{\mu}}_{2}-\boldsymbol{\mu}_{2}\right)\left(\hat{\boldsymbol{\mu}}_{2}-\boldsymbol{\mu}_{2}\right)^{\prime}\right] \\
= & \operatorname{Var}\left(\overline{\boldsymbol{x}}_{2}^{(1)}\right)-\frac{N_{2}}{N} \mathrm{E}\left[A_{21} A_{11}^{-1}\right] \operatorname{Cov}\left(\overline{\boldsymbol{x}}_{1}^{(1)}, \overline{\boldsymbol{x}}_{2}^{(1)}\right) \\
& -\frac{N_{2}}{N} \operatorname{Cov}\left(\overline{\boldsymbol{x}}_{2}^{(1)}, \overline{\boldsymbol{x}}_{1}^{(1)}\right) \mathrm{E}\left[A_{11}^{-1} A_{12}\right] \\
& +\left(\frac{N_{2}}{N}\right)^{2} \mathrm{E}\left[A_{21} A_{11}^{-1} \operatorname{Var}\left(\overline{\boldsymbol{x}}^{(2)}-\overline{\boldsymbol{x}}_{1}^{(1)}\right) A_{11}^{-1} A_{12}\right] .
\end{aligned}
$$

The final result is obtained by using Lemma 2.1 (ii) and (v).
It may be interesting to compare $\hat{\boldsymbol{\mu}}_{2}$ with a simple estimator $\tilde{\boldsymbol{\mu}}_{2}=\overline{\boldsymbol{x}}_{2}^{(1)}$, which is obtained by using the observations of $\boldsymbol{x}_{2}$ only. From Theorem 2.1 we have

$$
\begin{aligned}
\Psi & =\operatorname{Var}\left(\tilde{\boldsymbol{\mu}}_{2}\right)-\operatorname{Var}\left(\hat{\boldsymbol{\mu}}_{2}\right) \\
& =\frac{N_{2}}{N_{1} N}\left\{\Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}-\frac{p_{1}}{N_{1}-p_{1}-2} \Sigma_{22 \cdot 1}\right\}
\end{aligned}
$$

In general, if $\Psi$ is positive definite, i.e., $\Psi>O, \hat{\boldsymbol{\mu}}_{2}$ is better than $\tilde{\boldsymbol{\mu}}_{2}$. Though $\Psi$ is not always positive semidefinite, it is seen that $\Psi$ will be positive semidefinite for large $N_{1}$, since

$$
\Psi=\frac{N_{2}}{N_{1} N}\left\{\Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}+O\left(N_{1}^{-1}\right)\right\}
$$

When $N_{1}$ and $N_{2}$ are large, the asymptotic covariance matrix of $\sqrt{n}(\hat{\boldsymbol{\mu}}- \boldsymbol{\mu})$ under the assumption (2) is given by

$$
D=J_{1}+\frac{1}{\rho_{1}} J_{2}
$$

where

$$
J_{1}=\left(\begin{array}{cc}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}
\end{array}\right), \quad J_{2}=\left(\begin{array}{cc}
O & O \\
O & \Sigma_{22 \cdot 1}
\end{array}\right) .
$$

Next we examine the bias properties of $\hat{\Sigma}$ and $\hat{\Delta}$. The expectations of $\hat{\Sigma}$ and $\hat{\Delta}$ are given in the following theorem.

Theorem 2.2. Suppose that $N_{1}>p$. Then
(i) $\quad \mathrm{E}[\hat{\Sigma}]=\frac{N-1}{N} \Sigma+\left(\begin{array}{cc}O & O \\ O & \frac{b_{0}}{N} \Sigma_{22 \cdot 1}\end{array}\right),\left(N_{1}>p_{1}+2\right)$,
(ii) $\quad \mathrm{E}[\hat{\Delta}]=\Delta-\frac{1}{N}\left(\begin{array}{cc}\Delta_{11} & O \\ O & \frac{\left(p_{1}+1\right) N}{N_{1}} \Delta_{22}\end{array}\right)$,
where

$$
b_{0}=-\frac{N_{2}\left\{N_{1}-\left(p_{1}+1\right)\left(p_{1}+2\right)\right\}}{N_{1}\left(N_{1}-p_{1}-2\right)}
$$

Proof. It is seen that $W^{(1)}$ and $W^{(2)}$ are independently distributed as $W_{p}\left(\Sigma, N_{1}-1\right)$ and $W_{p_{1}}\left(\Sigma_{11}, N_{2}\right)$, respectively. This implies that $\mathrm{E}\left[\hat{\Sigma}_{11}\right]=$
$\frac{N-1}{N} \Sigma_{11}$, and

$$
\begin{aligned}
\mathrm{E}\left[\hat{\Sigma}_{12}\right] & =\frac{1}{N} \cdot \mathrm{E}\left[W_{12}^{(1)}+N_{2} \Sigma_{11}\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}\right] \\
& =\frac{1}{N} \cdot\left\{\left(N_{1}-1\right) \Sigma_{12}+N_{2} \Sigma_{12}\right\} \quad(\text { by Lemma 2.1(ii)) } \\
& =\frac{N-1}{N} \Sigma_{12}
\end{aligned}
$$

Similarly

$$
\begin{aligned}
\mathrm{E}\left[\hat{\Sigma}_{22}\right]= & \frac{1}{N} \cdot\left\{\left(N_{1}-1\right) \Sigma_{22}+\frac{N_{2}}{N_{1}}\left(N_{1}-p_{1}-1\right) \Sigma_{22 \cdot 1}\right. \\
& \left.+N_{2} \mathrm{E}\left[W_{21}^{(1)}\left(W_{11}^{(1)}\right)^{-1} \Sigma_{11}\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}\right]\right\} \\
= & \frac{N-1}{N} \Sigma_{22}+\frac{b_{0}}{N} \Sigma_{22 \cdot 1} \quad(\text { by Lemma } 2.1(\mathrm{v}))
\end{aligned}
$$

The result (ii) is easily obtained, by noting that $W^{(1)} \sim W_{p}\left(\Sigma, N_{1}-1\right)$.
From Theorem 2.2 (i) we can recommend a usual correction

$$
\tilde{\Sigma}=\frac{N}{N-1} \hat{\Sigma}
$$

for an estimator of $\Sigma$. In this case, $\tilde{\Sigma}_{11}$ and $\tilde{\Sigma}_{12}$ are unbiased, but $\tilde{\Sigma}_{22}$ involves the bias term of $O\left(N^{-1}\right)$. On the other hand, from Theorem 2.2 (ii), we can obtain an exact unbiased estimator $\tilde{\Delta}$ for $\Delta$, defined by

$$
\tilde{\Delta}_{11}=\frac{N}{N-1} \hat{\Delta}_{11}, \quad \tilde{\Delta}_{12}=\hat{\Delta}_{12}, \quad \tilde{\Delta}_{22}=\frac{N_{1}}{N_{1}-p_{1}-1} \hat{\Delta}_{22}
$$

In general, the exact variances of $\hat{\Sigma}$ or $\hat{\Delta}$ are complicated, though some marginal results are simple. These are asymptotically obtained in the next subsection.

### 2.3. Asymptotic Expansions of the Distributions of $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$

It is possible to obtain exact distributions of some subvectors of $\hat{\boldsymbol{\mu}}$ or some submatrices of $\hat{\Sigma}$. For example, $\hat{\boldsymbol{\mu}}_{1}$ and $N \hat{\Sigma}_{11}$ are independently distributed as $N_{p_{1}}\left(\boldsymbol{\mu}_{1}, N^{-1} \Sigma_{11}\right)$ and $W_{p_{1}}\left(\Sigma_{11}, N-1\right)$, respectively. However, it is difficult to obtain the exact distribution of $\hat{\boldsymbol{\mu}}$ itself or $\hat{\Sigma}$ itself. So, we consider asymptotic
expansions of the distributions of $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$ when $N_{1}$ and $N_{2}$ are large. In our derivations we consider stochastic expansions of $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$ in terms of

$$
\begin{array}{ccl}
\boldsymbol{z}^{(1)}=\sqrt{n_{1}}\binom{\overline{\boldsymbol{x}}_{1}^{(1)}-\boldsymbol{\mu}_{1}}{\overline{\boldsymbol{x}}_{2}^{(1)}-\boldsymbol{\mu}_{2}}, & \boldsymbol{z}^{(2)}=\sqrt{n_{2}}\left(\overline{\boldsymbol{x}}^{(2)}-\boldsymbol{\mu}_{1}\right), \\
V^{(1)}=\sqrt{n_{1}}\left(S^{(1)}-\Sigma\right), & V^{(2)}=\sqrt{n_{2}}\left(S^{(2)}-\Sigma_{11}\right) .
\end{array}
$$

Here we note that $\boldsymbol{z}^{(1)} \sim N_{p}\left(\mathbf{0},\left(n_{1} / N_{1}\right) \Sigma\right), \boldsymbol{z}^{(2)} \sim N_{p_{1}}\left(\mathbf{0},\left(n_{2} / N_{2}\right) \Sigma_{11}\right)$, and an asymptotic expansion of the density of $V^{(i)}$ is known ( see, e.g., Fujikoshi (1977)). Further, these statistics are independent.

Substituting $\overline{\boldsymbol{x}}_{j}^{(i)}=\boldsymbol{\mu}_{j}+n_{i}^{-1 / 2} \boldsymbol{z}^{(i)}$ and $S^{(1)}=\Sigma+n_{1}^{-1 / 2} V^{(1)}, S^{(2)}=\Sigma_{11}+ n_{2}^{-1 / 2} V^{(2)}$ to $\hat{\boldsymbol{\mu}}$, we can easily obtain a stochastic expansion of $\sqrt{n}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})$ given by

$$
\sqrt{n}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})=\boldsymbol{u}^{[0]}+\frac{1}{\sqrt{n}} \boldsymbol{u}^{[1]}+\frac{1}{n} \boldsymbol{u}^{[2]}+\frac{1}{n \sqrt{n}} \boldsymbol{r}_{1}+O_{p}\left(n^{-2}\right)
$$

where $\boldsymbol{u}^{[i]}=\left(\boldsymbol{u}_{1}^{[i] \prime}, \boldsymbol{u}_{2}^{[i] \prime}\right)^{\prime}, i=0,1,2$,

$$
\begin{aligned}
& \boldsymbol{u}^{[0]}=\binom{\sqrt{\rho_{1}} \boldsymbol{z}_{1}^{(1)}+\sqrt{\rho_{2}} \boldsymbol{z}^{(2)}}{\frac{1}{\sqrt{\rho_{1}}} \boldsymbol{z}_{2}^{(1)}+\rho_{2} \Sigma_{21} \Sigma_{11}^{-1} \boldsymbol{v}}, \\
& \boldsymbol{u}^{[1]}=\binom{O}{\frac{\rho_{2}}{\sqrt{\rho_{1}}}\left(V_{21}^{(1)}-\Sigma_{21} \Sigma_{11}^{-1} V_{11}^{(1)}\right) \Sigma_{11}^{-1} \boldsymbol{v}}, \\
& \boldsymbol{u}^{[2]}=\left\{\left(1-2 \rho_{2}\right)\binom{I_{p_{1}}}{\Sigma_{21} \Sigma_{11}^{-1}}+\frac{\rho_{2}}{\rho_{1}}\binom{O}{\Sigma_{21} \Sigma_{11}^{-1} V_{11}^{(1)}-V_{21}^{(1)}} \Sigma_{11}^{-1} V_{11}^{(1)} \Sigma_{11}^{-1}\right\} \boldsymbol{v}, \\
& \boldsymbol{v}=\frac{1}{\sqrt{\rho_{2}}} \boldsymbol{z}^{(2)}-\frac{1}{\sqrt{\rho_{1}}} \boldsymbol{z}_{1}^{(1)}
\end{aligned}
$$

and the elements of $\boldsymbol{r}_{1}$ are zero or the sums of homogeneous polynomials of degrees 1,3 or 5 in the elements of $\boldsymbol{z}^{(1)}, \boldsymbol{z}^{(2)}, V^{(1)}$ and $V^{(2)}$. Let $c(\boldsymbol{t})$ be the characteristic function of $\sqrt{n}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})$. Using the stochastic expansion, we can write $c(\boldsymbol{t})$ as

$$
\begin{aligned}
c(\boldsymbol{t})= & \mathrm{E}\left[e^{i \boldsymbol{t}^{\prime}} \boldsymbol{u}^{[0]}\left\{1+i\left(\frac{1}{\sqrt{n}} \boldsymbol{t}^{\prime} \boldsymbol{u}^{[1]}+\frac{1}{n} \boldsymbol{t}^{\prime} \boldsymbol{u}^{[2]}\right)+\frac{i^{2}}{2} \cdot \frac{1}{n}\left(\boldsymbol{t}^{\prime} \boldsymbol{u}^{[1]}\right)^{2}+\frac{1}{n \sqrt{n}} \boldsymbol{r}_{2}\right\}\right] \\
& +O\left(n^{-2}\right)
\end{aligned}
$$

where $\boldsymbol{r}_{2}$ is a quantity having the same property as $\boldsymbol{r}_{1}$. The above expectations can be evaluated by using that $\boldsymbol{z}^{(1)} \sim N_{p}\left(\mathbf{0},\left(n_{1} / N_{1}\right) \Sigma\right), \boldsymbol{z}^{(2)} \sim N_{p_{1}}(\mathbf{0}$,



$\left.\left(n_{2} / N_{2}\right) \Sigma_{11}\right), n_{1} S^{(1)} \sim W_{p}\left(\Sigma, n_{1}\right)$ and $n_{2} S^{(2)} \sim W_{p_{1}}\left(\Sigma_{11}, n_{2}\right)$. The result up to the order $n^{-3 / 2}$ is given by

$$
c(\boldsymbol{t})=\exp \left\{\frac{i^{2}}{2} \boldsymbol{t}^{\prime} D \boldsymbol{t}\right\} \cdot\left(1+\frac{i^{2}}{n} \cdot \frac{p_{1} \rho_{2}}{2 \rho_{1}^{2}} \cdot \boldsymbol{t}^{\prime} J_{2} \boldsymbol{t}\right)+O\left(n^{-2}\right)
$$

Therefore the characteristic function of $\sqrt{n} D^{-1 / 2}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})$ is given by

$$
\tilde{c}(\boldsymbol{t})=\exp \left(\frac{i^{2}}{2} \boldsymbol{t}^{\prime} \boldsymbol{t}\right)\left[1+\frac{i^{2}}{2 n} \cdot \frac{p_{1} \rho_{2}}{\rho_{1}^{2}} \cdot \boldsymbol{t}^{\prime} D^{-1 / 2} J_{2} D^{-1 / 2} \boldsymbol{t}\right]+O\left(n^{-2}\right)
$$

The density function $f(\boldsymbol{x})$ of $\sqrt{n} D^{-1 / 2}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})$ is obtained by inverting this characteristic function $\tilde{c}(\boldsymbol{t})$, i.e.,

$$
\begin{aligned}
f(\boldsymbol{x})= & (2 \pi)^{-p} \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \exp \left(-i \boldsymbol{t}^{\prime} \boldsymbol{x}\right) \tilde{c}(\boldsymbol{t}) d t_{1} \ldots d t_{p} \\
= & (2 \pi)^{-p} \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \exp \left(-i \boldsymbol{t}^{\prime} \boldsymbol{x}\right) \exp \left(-\frac{1}{2} \boldsymbol{t}^{\prime} \boldsymbol{t}\right) \\
& \times\left[1+\frac{i^{2}}{2 n} \cdot \frac{p_{1} \rho_{2}}{\rho_{1}^{2}} \cdot \boldsymbol{t}^{\prime} D^{-1 / 2} J_{2} D^{-1 / 2} \boldsymbol{t}\right] d t_{1} \ldots d t_{p}+O\left(n^{-2}\right)
\end{aligned}
$$

Calculating the above integrals, we can obtain the following theorem:
Theorem 2.3. The density function $f(\boldsymbol{x})$ of $\sqrt{n} D^{-1 / 2}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})$ can be expanded as

$$
f(\boldsymbol{x})=\phi(\boldsymbol{x})\left[1+\frac{1}{n} \cdot \frac{p_{1} \rho_{2}}{2 \rho_{1}^{2}}\left\{\boldsymbol{x}^{\prime} D^{-1 / 2} J_{2} D^{-1 / 2} \boldsymbol{x}-\operatorname{tr} J_{2} D^{-1}\right\}\right]+O\left(n^{-2}\right)
$$

for large $N_{i}$ 's, where $D$ is given by (3) and

$$
\phi(\boldsymbol{x})=\left(\frac{1}{2 \pi}\right)^{p / 2} \exp \left(-\frac{1}{2} \boldsymbol{x}^{\prime} \boldsymbol{x}\right)
$$

Now we consider the asymptotic expansions of density functions of MLE's $\hat{\Sigma}$ and $\hat{\Delta}$. For simplicity, we consider the distribution of $\hat{\Delta}$. The result can be used for obtaining an asymptotic expansion of the distribution of $\hat{\Sigma}$. Let $C(T)$ be the characteristic function of $\sqrt{n}(\hat{\Delta}-\Delta)$, where $T=\left[(1 / 2)\left(1+\delta_{i j}\right) t_{i j}\right]$ with $t_{i j}=t_{j i}$, and $T$ is partitioned as in the partition of $\Sigma$. By the same way as in the case $\hat{\boldsymbol{\mu}}$, we can obtain a stochastic expansion of $M=\sqrt{n}(\hat{\Delta}-\Delta)$ as follows:

$$
M=M^{[0]}+\frac{1}{\sqrt{n}} M^{[1]}+O_{p}\left(n^{-1}\right)
$$

where

$$
\begin{aligned}
& M^{[i]}=\left(\begin{array}{ll}
M_{11}^{[i]} & M_{12}^{[i]} \\
M_{21}^{[i]} & M_{22}^{[i]}
\end{array}\right), i=0,1 \\
& M_{11}^{[0]}=\sqrt{\rho_{1}} V_{11}^{(1)}+\sqrt{\rho_{2}} V^{(2)}, \quad M_{12}^{[0]}=\frac{1}{\sqrt{\rho_{1}}} \Delta_{11}^{-1}\left(V_{12}^{(1)}-V_{11}^{(1)} \Delta_{12}\right) \\
& M_{22}^{[0]}=\frac{1}{\sqrt{\rho_{1}}}\left(\Delta_{21} I_{p_{2}}\right) V^{(1)}\left(\Delta_{21} I_{p_{2}}\right)^{\prime} \\
& M_{11}^{[1]}=\rho_{1} \rho_{2} v v^{\prime}-2 \Delta_{11}, \quad M_{12}^{[1]}=\frac{1}{\sqrt{\rho_{1}}} \Delta_{11}^{-1} V_{11}^{(1)} \Delta_{11}^{-1}\left(V_{11}^{(1)} V_{12}^{(1)}\right)\left(\Delta_{21} I_{p_{2}}\right)^{\prime} \\
& M_{22}^{[1]}=-\frac{1}{\rho_{1}}\left[\left(\Delta_{21} V_{11}^{(1)}-V_{21}^{(1)}\right) \Delta_{11}^{-1}\left(\Delta_{21} V_{11}^{(1)}-V_{21}^{(1)}\right)^{\prime}+\Delta_{22}\right]
\end{aligned}
$$

Then the characteristic function of $M$ can be expressed as

$$
\begin{aligned}
C(T)= & \mathrm{E}[\exp \{i \operatorname{tr} T M\}] \\
= & \mathrm{E}\left[\exp \left\{i \operatorname{tr} T_{11} M_{11}^{[0]}+2 i \operatorname{tr} T_{12} M_{12}^{[0]}+i \operatorname{tr} T_{22} M_{22}^{[0]}\right\}\right. \\
& \left.\times\left\{1+\frac{i}{\sqrt{n}}\left(\operatorname{tr} T_{11} M_{11}^{[1]}+2 \operatorname{tr} T_{12} M_{12}^{[1]}+\operatorname{tr} T_{22} M_{22}^{[1]}\right)\right\}\right]+O\left(n^{-1}\right)
\end{aligned}
$$

The above expressions can be evaluated by using an asymptotic expansion of the probability density function of $V^{(i)}$. The final result is given as follows.

$$
\begin{aligned}
C(T)= & \exp \left[-\left\{\operatorname{tr}\left(T_{11} \Delta_{11}\right)^{2}+\frac{2}{\rho_{1}} \operatorname{tr} T_{21} \Delta_{11}^{-1} T_{12} \Delta_{22}+\frac{1}{\rho_{1}} \operatorname{tr}\left(T_{22} \Delta_{22}\right)^{2}\right\}\right] \\
& \times\left[1+\frac{1}{\sqrt{n}}\left\{\frac{4}{3} i^{3} \rho_{2} \operatorname{tr}\left(T_{11} \Delta_{11}\right)^{3}+\frac{4}{3 \sqrt{\rho_{1}}} i^{3}\left(\rho_{1} \sqrt{\rho_{1}} \operatorname{tr}\left(T_{11} \Delta_{11}\right)^{3}\right.\right.\right. \\
& +\frac{3}{\sqrt{\rho_{1}}} \operatorname{tr} T_{21} T_{11} T_{12} \Delta_{22}+\frac{1}{\rho_{1} \sqrt{\rho_{1}}}\left\{3 \operatorname{tr} T_{22} \Delta_{22} T_{21} \Delta_{11}^{-1} T_{12} \Delta_{22}\right. \\
& \left.\left.+\operatorname{tr}\left(T_{22} \Delta_{22}\right)^{3}\right\}\right)-i \operatorname{tr} T_{11} \Delta_{11}+\frac{8 i}{\sqrt{\rho_{1}}} \operatorname{tr} T_{21} T_{11} T_{12} \Delta_{22} \\
& \left.\left.-\frac{i}{\rho_{1}}\left(p_{1}+1\right) \operatorname{tr} T_{22} \Delta_{22}+\frac{4 i}{\rho_{1}^{2}} \operatorname{tr} T_{22} \Delta_{22} T_{21} \Delta_{11}^{-1} T_{12} \Delta_{22}\right\}\right]+O\left(n^{-1}\right)
\end{aligned}
$$

Based on the above result, we normalize $\sqrt{n}(\hat{\Delta}-\Delta)$ as

$$
U=\left(\begin{array}{ll}
U_{11} & U_{12} \\
U_{21} & U_{22}
\end{array}\right)
$$

where

$$
\begin{aligned}
U_{11} & =\sqrt{\frac{n}{2}} \Delta_{11}^{-1 / 2}\left(\hat{\Delta}_{11}-\Delta_{11}\right) \Delta_{11}^{-1 / 2} \\
U_{12} & =\sqrt{\frac{n \rho_{1}}{2}} \Delta_{11}^{1 / 2}\left(\hat{\Delta}_{12}-\Delta_{12}\right) \Delta_{22}^{-1 / 2} \\
U_{22} & =\sqrt{\frac{n \rho_{1}}{2}} \Delta_{22}^{-1 / 2}\left(\hat{\Delta}_{22}-\Delta_{22}\right) \Delta_{22}^{-1 / 2}
\end{aligned}
$$

Then the characteristic function of $U$ can be represented as the following form.

$$
\begin{aligned}
& \exp \left(-\frac{1}{2} \operatorname{tr} T^{2}\right)\left[1+\frac{1}{\sqrt{n}}\left\{\frac{\sqrt{2}}{3} i^{3}\left(\operatorname{tr} T_{11}^{3}+\frac{1}{\sqrt{\rho_{1}}} \operatorname{tr} T_{22}^{3}\right)\right.\right. \\
& \left.\left.+\sqrt{2}\left(1-2 \sqrt{\rho_{1}}\right) i^{3} \operatorname{tr} T_{21} T_{11} T_{12}-\frac{i}{\sqrt{2}}\left(\operatorname{tr} T_{11}+\frac{p_{1}+1}{\sqrt{\rho_{1}}} \operatorname{tr} T_{22}\right)\right\}\right]+O\left(n^{-1}\right)
\end{aligned}
$$

Inverting this characteristic function, we have the following theorem on the distribution of $U$.

Theorem 2.4. Let $U$ be the standardized statistic of $\sqrt{n}(\hat{\Delta}-\Delta)$ defined by (5). Then the probability density function of $U$ can be expanded as

$$
\begin{aligned}
\phi(X) & {\left[1+\frac{1}{\sqrt{n}}\left\{\frac{\sqrt{2}}{3}\left(\operatorname{tr} X_{11}^{3}+\frac{1}{\sqrt{\rho_{1}}} \operatorname{tr} X_{22}^{3}\right)+\sqrt{2}\left(1-2 \sqrt{\rho_{1}}\right) \operatorname{tr} X_{21} X_{11} X_{12}\right.\right.} \\
& \left.\left.-\frac{1}{\sqrt{2}}\left(\left(p+2-2 p_{2} \sqrt{\rho_{1}}\right) \operatorname{tr} X_{11}+\frac{1}{\sqrt{\rho_{1}}}(p+2) \operatorname{tr} X_{22}\right)\right\}\right]+O\left(n^{-1}\right)
\end{aligned}
$$

where $X: p \times p$ is partitioned as in the partition of $U$, and

$$
\phi(X)=\pi^{-p(p+1) / 4} 2^{-p / 2} \exp \left(-\frac{1}{2} \operatorname{tr} X^{2}\right)
$$

This result shows that $U_{11}, U_{12}$ and $U_{22}$ are asymptotically independent, and $\left(U_{11}, U_{12}\right)$ and $U_{22}$ are asymptotically independent up to the order $n^{-1 / 2}$. Theorem 2.4 can be used for deriving asymptotic expansions of $\sqrt{n}(\hat{\Sigma}-\Sigma)$ and its function. The idea is to use stochastic expansions of $\sqrt{n}(\hat{\Sigma}-\Sigma)$ in terms of $U$, which are obtained by using one-to-one correspondence between $\hat{\Sigma}$ and $\hat{\Delta}$. In fact, we can derive the following expansions:

$$
\begin{aligned}
\sqrt{\frac{n}{2}}\left(\hat{\Sigma}_{11}-\Sigma_{11}\right) & =\Sigma_{11}^{1 / 2} U_{11} \Sigma_{11}^{1 / 2} \\
\sqrt{\frac{n \rho_{1}}{2}}\left(\hat{\Sigma}_{12}-\Sigma_{12}\right) & =\Sigma_{11}^{1 / 2}\left\{U_{12} \Sigma_{22 \cdot 1}^{1 / 2}+\sqrt{\rho_{1}} U_{11} \Sigma_{11}^{-1 / 2} \Sigma_{12}+\sqrt{\frac{2}{n}} U_{11} U_{12} \Sigma_{22 \cdot 1}^{-1 / 2}\right\}
\end{aligned}
$$

$$
\begin{aligned}
\sqrt{\frac{n \rho_{1}}{2}}\left(\hat{\Sigma}_{22}-\Sigma_{22}\right)= & \Sigma_{22 \cdot 1}^{1 / 2} U_{22} \Sigma_{22 \cdot 1}^{1 / 2}+\sqrt{\rho_{1}} \Sigma_{21} \Sigma_{11}^{-1 / 2} U_{11} \Sigma_{11}^{-1 / 2} \Sigma_{12} \\
& +\Sigma_{21} \Sigma_{11}^{-1 / 2} U_{12} \Sigma_{22 \cdot 1}^{1 / 2}+\Sigma_{22 \cdot 1}^{1 / 2} U_{21} \Sigma_{11}^{-1 / 2} \Sigma_{12} \\
& +\sqrt{\frac{2}{n}}\left\{\Sigma_{11}^{1 / 2} U_{11} U_{12} \Sigma_{22 \cdot 1}^{1 / 2}+\frac{1}{\sqrt{\rho_{1}}} \Sigma_{11}^{1 / 2} U_{11} U_{12} \Sigma_{22 \cdot 1}^{1 / 2}\right. \\
& \left.+\Sigma_{22 \cdot 1}^{1 / 2} U_{21} U_{11} \Sigma_{11}^{-1 / 2} \Sigma_{12}\right\}+\frac{2}{n} \cdot \frac{1}{\sqrt{\rho_{1}}} \Sigma_{22 \cdot 1}^{1 / 2} U_{21} U_{11} U_{12} \Sigma_{22 \cdot 1}^{1 / 2}
\end{aligned}
$$

Further, letting $\rho_{1}=1$ in the result of Theorem 2.4 we can obtain an asymptotic expansion of the probability density function of $U$ when $N_{1}$ is large and $N_{2}$ is fixed.

## 3. 3-STEP MONOTONE MISSING DATA

In this section, we consider the case $k=3$. As in section 2, we partition $\boldsymbol{x}$ as $\left(\boldsymbol{x}_{1}^{\prime}, \boldsymbol{x}_{2}^{\prime}, \boldsymbol{x}_{3}^{\prime}\right)^{\prime}$ where $\boldsymbol{x}_{1}, \boldsymbol{x}_{2}$ and $\boldsymbol{x}_{3}$ are $p_{1}, p_{2}$ and $p_{3}$-dimensional vectors, respectively. Suppose we have $N_{1}$ observations on $\boldsymbol{x}, N_{2}$ observations on $\left(\boldsymbol{x}_{1}^{\prime}, \boldsymbol{x}_{2}^{\prime}\right)^{\prime}$, and $N_{3}$ observations on $\boldsymbol{x}_{1}$, and these observations are independently distributed. Similarly, let the vector $\overline{\boldsymbol{x}}^{(1)}=\left(\overline{\boldsymbol{x}}_{1}^{(1)^{\prime}}, \overline{\boldsymbol{x}}_{2}^{(1)^{\prime}}, \overline{\boldsymbol{x}}_{3}^{(1) \prime}\right)^{\prime}$ denote the sample mean of $\boldsymbol{x}$ based on $N_{1}$ observations, $\overline{\boldsymbol{x}}^{(2)}=\left(\overline{\boldsymbol{x}}_{1}^{(2) \prime}, \overline{\boldsymbol{x}}_{2}^{(2) \prime}\right)^{\prime}$ denote the sample mean for the first ( $p_{1}+p_{2}$ )-dimensional elements of $\boldsymbol{x}$ based on $N_{2}$ observations, respectively, and $\overline{\boldsymbol{x}}^{(3)}$ denote the sample mean for $p_{1}$-dimensional elements of $\boldsymbol{x}_{1}$ based on $N_{3}$ observations. The corresponding sample covariance matrices are denoted by $S^{(i)}, i=1,2,3$, as follows:

$$
\begin{aligned}
S^{(1)} & =\frac{1}{n_{1}} \sum_{\alpha=1}^{N_{1}}\left(\boldsymbol{x}_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)\left(\boldsymbol{x}_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)^{\prime}, \\
S^{(2)} & =\frac{1}{n_{2}} \sum_{\alpha=1}^{N_{2}}\binom{\boldsymbol{x}_{1 \alpha}^{(2)}-\overline{\boldsymbol{x}}_{1}^{(2)}}{\boldsymbol{x}_{2 \alpha}^{(2)}-\overline{\boldsymbol{x}}_{2}^{(2)}}\binom{\boldsymbol{x}_{1 \alpha}^{(2)}-\overline{\boldsymbol{x}}_{1}^{(2)}}{\boldsymbol{x}_{2 \alpha}^{(2)}-\overline{\boldsymbol{x}}_{2}^{(2)}}^{\prime}, \\
S^{(3)} & =\frac{1}{n_{3}} \sum_{\alpha=1}^{N_{3}}\left(\boldsymbol{x}_{\alpha}^{(3)}-\overline{\boldsymbol{x}}^{(3)}\right)\left(\boldsymbol{x}_{\alpha}^{(3)}-\overline{\boldsymbol{x}}^{(3)}\right)^{\prime},
\end{aligned}
$$

where $n_{i}=N_{i}-1, i=1,2,3, N=N_{1}+N_{2}+N_{3}, n=N-3$.
Let the partitions of $\boldsymbol{\mu}$ and $\Sigma$ corresponding to the ones of $\boldsymbol{x}$ be

$$
\boldsymbol{\mu}=\left(\begin{array}{l}
\boldsymbol{\mu}_{1} \\
\boldsymbol{\mu}_{2} \\
\boldsymbol{\mu}_{3}
\end{array}\right), \quad \Sigma=\left(\begin{array}{ccc}
\Sigma_{11} & \Sigma_{12} & \Sigma_{13} \\
\Sigma_{21} & \Sigma_{22} & \Sigma_{23} \\
\Sigma_{31} & \Sigma_{32} & \Sigma_{33}
\end{array}\right)=\left(\begin{array}{cc}
\Sigma_{(12)(12)} & \Sigma_{(12) 3} \\
\Sigma_{3(12)} & \Sigma_{33}
\end{array}\right) .
$$

Similar partitions and notations are used for $S^{(i)}$ and other matrices.

### 3.1. MLE's

Extending to the conditional approach or using a successive expression by Jinadasa and Tracy (1992), we can express the MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$ as follows:

$$
\begin{aligned}
\hat{\boldsymbol{\mu}}_{1} & =\frac{1}{N}\left(N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{1}^{(2)}+N_{3} \overline{\boldsymbol{x}}^{(3)}\right), \\
\hat{\boldsymbol{\mu}}_{2} & =\frac{1}{N_{1}+N_{2}}\left(N_{1} \overline{\boldsymbol{x}}_{2}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{2}^{(2)}\right)-F^{\prime}\left(\frac{N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{1}^{(2)}}{N_{1}+N_{2}}-\hat{\boldsymbol{\mu}}_{1}\right), \\
\hat{\boldsymbol{\mu}}_{3} & =\overline{\boldsymbol{x}}_{3}^{(1)}-G^{\prime}\binom{\overline{\boldsymbol{x}}_{1}^{(1)}-\hat{\boldsymbol{\mu}}_{1}}{\overline{\boldsymbol{x}}_{2}^{(1)}-\hat{\boldsymbol{\mu}}_{2}}, \\
\hat{\Sigma}_{11} & =\frac{1}{N}\left(W_{11}^{(1)}+W_{11}^{(2)}+W^{(3)}\right), \quad \hat{\Sigma}_{12}=\hat{\Sigma}_{11} F, \\
\hat{\Sigma}_{22} & =\frac{1}{N_{1}+N_{2}}\left(W_{(12)(12)}^{(1)}+W^{(2)}\right)_{22 \cdot 1}+F^{\prime} \hat{\Sigma}_{11} F, \\
\hat{\Sigma}_{(12) 3} & =\hat{\Sigma}_{(12)(12)} G, \quad \hat{\Sigma}_{33}=\frac{1}{N_{1}} W_{33 \cdot 12}^{(1)}+G^{\prime} \hat{\Sigma}_{(12)(12)} G,
\end{aligned}
$$

where

$$
\begin{aligned}
F= & \left(W_{11}^{(1)}+W_{11}^{(2)}\right)^{-1}\left(W_{12}^{(1)}+W_{12}^{(2)}\right), \quad G=\left(W_{(12)(12)}^{(1)}\right)^{-1} W_{(12) 3}^{(1)}, \\
W^{(1)}= & n_{1} S^{(1)}, \\
W^{(2)}= & n_{2} S_{\prime}^{(2)}+\frac{N_{1} N_{2}}{N_{1}+N_{2}}\binom{\overline{\boldsymbol{x}}_{1}^{(1)}-\overline{\boldsymbol{x}}_{1}^{(2)}}{\overline{\boldsymbol{x}}_{2}^{(1)}-\overline{\boldsymbol{x}}_{2}^{(2)}}\binom{\overline{\boldsymbol{x}}_{1}^{(1)}-\overline{\boldsymbol{x}}_{1}^{(2)}}{\overline{\boldsymbol{x}}_{2}^{(1)}-\overline{\boldsymbol{x}}_{2}^{(2)}}^{\prime}, \\
W^{(3)}= & n_{3} S^{(3)}+\frac{\left(N_{1}+N_{2}\right) N_{3}}{N}\left(\overline{\boldsymbol{x}}^{(3)}-\frac{1}{N_{1}+N_{2}}\left(N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{1}^{(2)}\right)\right) \\
& \times\left(\overline{\boldsymbol{x}}^{(3)}-\frac{1}{N_{1}+N_{2}}\left(N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{1}^{(2)}\right)\right)^{\prime}
\end{aligned}
$$

The natural parameters in the conditional approach are defined by

$$
\boldsymbol{\eta}=\left(\begin{array}{l}
\boldsymbol{\eta}_{1} \\
\boldsymbol{\eta}_{2} \\
\boldsymbol{\eta}_{3}
\end{array}\right), \quad \Delta=\left(\begin{array}{lll}
\Delta_{11} & \Delta_{12} & \Delta_{13} \\
\Delta_{21} & \Delta_{22} & \Delta_{23} \\
\Delta_{31} & \Delta_{32} & \Delta_{33}
\end{array}\right),
$$

which are one to one correspondence to $(\boldsymbol{\mu}, \Sigma)$, where

$$
\boldsymbol{\eta}_{1}=\boldsymbol{\mu}_{1}, \quad \boldsymbol{\eta}_{2}=\boldsymbol{\mu}_{2}-\Delta_{21} \boldsymbol{\mu}_{1}, \quad \boldsymbol{\eta}_{3}=\boldsymbol{\mu}_{3}-\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1}\binom{\boldsymbol{\mu}_{1}}{\boldsymbol{\mu}_{2}}
$$



$$
\begin{aligned}
& \Delta_{11}=\Sigma_{11}, \quad \Delta_{12}=\Delta_{21}^{\prime}=\Sigma_{11}^{-1} \Sigma_{12}, \quad \Delta_{22}=\Sigma_{22 \cdot 1}=\Sigma_{22}-\Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12} \\
& \Delta_{(12) 3}=\Delta_{3(12)}^{\prime}=\Sigma_{(12)(12)}^{-1} \Sigma_{(12) 3} \\
& \Delta_{33}=\Sigma_{33 \cdot 12}=\Sigma_{33}-\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1} \Sigma_{(12) 3}
\end{aligned}
$$

The MLE's $(\hat{\boldsymbol{\eta}}, \hat{\Delta})$ of $(\boldsymbol{\eta}, \Delta)$ are expressed as follows:

$$
\begin{aligned}
& \hat{\boldsymbol{\eta}}_{1}=\hat{\boldsymbol{\mu}}_{1}, \quad \hat{\boldsymbol{\eta}}_{2}=\overline{\boldsymbol{x}}_{2}^{(1)}-\hat{\Delta}_{21} \overline{\boldsymbol{x}}_{1}^{(1)}, \quad \hat{\boldsymbol{\eta}}_{3}=\overline{\boldsymbol{x}}_{3}^{(1)}-\hat{\Delta}_{3(12)}\binom{\overline{\boldsymbol{x}}_{1}^{(1)}}{\overline{\boldsymbol{x}}_{2}^{(1)}} \\
& \hat{\Delta}_{11}=\hat{\Sigma}_{11}, \quad \hat{\Delta}_{12}=\hat{\Delta}_{21}^{\prime}=\left(W_{11}^{(1)}+W_{11}^{(2)}\right)^{-1}\left(W_{12}^{(1)}+W_{12}^{(2)}\right) \\
& \hat{\Delta}_{22}=\frac{1}{N_{1}+N_{2}}\left(W_{(12)(12)}^{(1)}+W^{(2)}\right)_{22 \cdot 1} \\
& \hat{\Delta}_{(12) 3}=\left(W_{(12)(12)}^{(1)}\right)^{-1} W_{(12) 3}^{(1)}, \quad \hat{\Delta}_{33}=\frac{1}{N_{1}} W_{33 \cdot 12}^{(1)}
\end{aligned}
$$

### 3.2. Means and Variances of $\hat{\mu}$ and $\hat{\Sigma}$

In addition to the properties of Wishart matrices as in Lemma 2.1, we use the following properties.

Lemma 3.1. Suppose that $A, B$ and $C$ are independently distributed as Wishart distributions $W_{p}\left(\Sigma, n_{1}\right), W_{p}\left(\Sigma, n_{2}\right)$ and $W_{p}\left(\Sigma, n_{3}\right)$, respectively. Let $n=n_{1}+n_{2}+n_{3}$ and let $A, B, C$ and $\Sigma$ be partitioned as in Lemma 2.1. Further, let $L=\left(A_{11}+B_{11}\right)^{-1}\left(A_{12}+B_{12}\right)$ and

$$
D=\left(\begin{array}{ll}
D_{11} & D_{12} \\
D_{21} & D_{22}
\end{array}\right)
$$

where $D_{11}=A_{11}+B_{11}+C_{11}, D_{12}=D_{21}^{\prime}=D_{11} L, D_{22}=\gamma A_{22 \cdot 1}+L^{\prime} D_{11} L$ and $\gamma$ is a constant. Then
(i) $\quad \mathrm{E}\left[D_{11}\right]=n \Sigma_{11}$,
(ii) $\quad \mathrm{E}\left[D_{12}\right]=n \Sigma_{12}$,
(iii) if $n_{1}+n_{2}-p_{1}-1>0$,

$$
\begin{aligned}
\mathrm{E}\left[D_{22}\right]=\gamma\left(n-p_{1}\right) & \Sigma_{22 \cdot 1}+n \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12} \\
& +p_{1}\left\{1+\frac{n_{3}}{n_{1}+n_{2}-p_{1}-1}\right\} \Sigma_{22 \cdot 1}
\end{aligned}
$$

(iv) if $n_{1}-p-1>0$,

$$
\mathrm{E}\left[\operatorname{tr} A^{-1} D\right]=p_{1}+\gamma p_{2}+\frac{\left(n_{2}+n_{3}\right) p_{1}}{n_{1}-p_{1}-1}
$$

$$
+\frac{p_{1} p_{2}}{n_{1}-p-1}\left\{\frac{n_{2}+n_{3}}{n_{1}-p_{1}-1}-\frac{n_{3}}{n_{1}+n_{2}-p_{1}-1}\right\}
$$

(v) if $n_{1}-p-1>0$,

$$
\begin{aligned}
\mathrm{E}\left[\operatorname{tr} A^{-1}\binom{I_{p_{1}}}{L^{\prime}}\right. & \left.\Sigma_{11}\left(I_{p_{1}} L\right)\right]=\frac{p_{1}}{n_{1}-p_{1}-1} \\
& +\frac{p_{1} p_{2}}{n_{1}-p-1}\left\{\frac{1}{n_{1}-p_{1}-1}-\frac{1}{n_{1}+n_{2}-p_{1}-1}\right\}
\end{aligned}
$$

Proof. The results (i), (ii) and (iii) are easily reduced from Lemma 2.1. For a proof of (iv) and (v), we use

$$
A^{-1}=\left(\begin{array}{ll}
A^{11} & A^{12} \\
A^{21} & A^{22}
\end{array}\right)
$$

where $A^{11}=A_{11}^{-1}+A_{11}^{-1} A_{12} A_{22 \cdot 1}^{-1} A_{21} A_{11}^{-1}, A^{12}=\left(A^{21}\right)^{\prime}=-A_{11}^{-1} A_{12} A_{22 \cdot 1}^{-1}$ and $A^{22}=A_{22-1}^{-1}$. The expectation of each term can be evaluated in three steps; (1) $A_{22 \cdot 1},(2) A_{12}, B_{12},(3) A_{11}, B_{11}, C_{11}$ in this order, by using Lemma 2.1. The detail is omitted here.

Clearly $\mathrm{E}\left[\hat{\boldsymbol{\mu}}_{1}\right]=\boldsymbol{\mu}_{1}$. Let

$$
\boldsymbol{y}=\binom{\boldsymbol{y}_{1}}{\boldsymbol{y}_{2}}=\frac{1}{N_{1}+N_{2}}\left\{N_{1}\binom{\overline{\boldsymbol{x}}_{1}^{(1)}}{\overline{\boldsymbol{x}}_{2}^{(1)}}+N_{2}\binom{\overline{\boldsymbol{x}}_{1}^{(2)}}{\overline{\boldsymbol{x}}_{2}^{(2)}}\right\} .
$$

Then, $F$ and $\left\{\boldsymbol{y}, \hat{\boldsymbol{\mu}}_{1}\right\}$ are independent, and hence $\mathrm{E}\left[\hat{\boldsymbol{\mu}}_{2}\right]=\boldsymbol{\mu}_{2}$. Similarly the independence of $G$ and $\left\{\overline{\boldsymbol{x}}^{(1)}, \hat{\boldsymbol{\mu}}_{1}, \hat{\boldsymbol{\mu}}_{2}\right\}$ implies $\mathrm{E}\left[\hat{\boldsymbol{\mu}}_{3}\right]=\boldsymbol{\mu}_{3}$. For deriving the covariance matrix of $\hat{\boldsymbol{\mu}}$, we use the following two expressions:

$$
\begin{aligned}
\hat{\boldsymbol{\mu}} & =\frac{N_{1}}{N} C_{1} \overline{\boldsymbol{x}}^{(1)}+\frac{N_{2}}{N} C_{2} \overline{\boldsymbol{x}}^{(2)}+\frac{N_{3}}{N} C_{3} \overline{\boldsymbol{x}}^{(3)} \\
& =\frac{N_{1}}{N} C_{1}^{*} \overline{\boldsymbol{x}}^{(1)}+\frac{1}{N}\left(N_{1}+N_{2}\right) C_{2} \boldsymbol{y}+\frac{N_{3}}{N} C_{3} \overline{\boldsymbol{x}}^{(3)},
\end{aligned}
$$

where

$$
\begin{aligned}
C_{1} & =\left(\begin{array}{cc}
C & O \\
G^{\prime}\left(C-\frac{N}{N_{1}} I_{p_{1}+p_{2}}\right) & \frac{N}{N_{1}} I_{p_{3}}
\end{array}\right), \quad C_{2}=\binom{I_{p_{1}}}{G^{\prime}} C, \\
C_{3} & =\binom{I_{p_{1}+p_{2}}}{G^{\prime}}\binom{I_{p_{1}}}{F^{\prime}}, \quad C=\left(\begin{array}{c}
I_{p_{1}} \\
-\frac{N_{3}}{N_{1}+N_{2}} F^{\prime} \\
\frac{N}{N_{1}+N_{2}} I_{p_{2}}
\end{array}\right), \\
C_{1}^{*} & =\left(\begin{array}{cc}
O & O \\
-\frac{N}{N_{1}} G^{\prime} & \frac{N}{N_{1}} I_{p_{3}}
\end{array}\right) .
\end{aligned}
$$

Lemma 3.2. The covariance matrix of $\hat{\boldsymbol{\mu}}$ can be expressed as

$$
\operatorname{Var}(\hat{\boldsymbol{\mu}})=\frac{1}{N^{2}} \mathrm{E}\left[N_{1} C_{1} \Sigma C_{1}^{\prime}+N_{2} C_{2} \Sigma_{(12)(12)} C_{2}^{\prime}+N_{3} C_{3} \Sigma_{11} C_{3}^{\prime}\right]
$$

Proof. Using the second expression for $\hat{\boldsymbol{\mu}}$, it can be seen that

$$
\begin{aligned}
\operatorname{Var}(\hat{\boldsymbol{\mu}})= & \frac{1}{N^{2}} \mathrm{E}\left[N_{1} C_{1}^{*} \Sigma C_{1}^{*}+\left(N_{1}+N_{2}\right) C_{2} \Sigma_{(12)(12)} C_{2}^{\prime}\right. \\
& \left.+N_{1}\left(N_{1}+N_{2}\right)\left\{C_{1}^{*} \overline{\boldsymbol{x}}^{(1)} \boldsymbol{y}^{\prime} C_{2}^{\prime}+C_{2} \boldsymbol{y} \overline{\boldsymbol{x}}^{(1) \prime} C_{1}^{*}\right\}+N_{3} C_{3} \Sigma_{11} C_{3}^{\prime}\right]
\end{aligned}
$$

Here, without loss of generality it is assumed that $\boldsymbol{\mu}=\mathbf{0}$. Since $C_{1}=\left[C_{2} O\right]+ C_{1}^{*}$, it is sufficient to show that

$$
\mathrm{E}\left[C_{1}^{*} \overline{\boldsymbol{x}}^{(1)} \boldsymbol{y}^{\prime} C_{2}\right]=\frac{1}{N_{1}+N_{2}} C_{1}^{*} \Sigma\binom{C_{2}^{\prime}}{O}
$$

Noting that

$$
\mathrm{E}\left[\overline{\boldsymbol{x}}_{3}^{(1)} \left\lvert\,\binom{\overline{\boldsymbol{x}}_{1}^{(1)}}{\overline{\boldsymbol{x}}_{2}^{(1)}}\right.\right]=\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1}\binom{\overline{\boldsymbol{x}}_{1}^{(1)}}{\overline{\boldsymbol{x}}_{2}^{(1)}}
$$

we have

$$
\begin{aligned}
\mathrm{E}\left[C_{1}^{*} \overline{\boldsymbol{x}}^{(1)} \boldsymbol{y}^{\prime} C_{2}\right] & =\mathrm{E}\left[C_{1}^{*}\binom{I_{p_{1}+p_{2}}}{\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1}}\binom{\overline{\boldsymbol{x}}_{1}^{(1)}}{\overline{\boldsymbol{x}}_{2}^{(1)}} \boldsymbol{y}^{\prime} C_{2}\right] \\
& =\frac{1}{N_{1}+N_{2}} C_{1}^{*}\binom{\Sigma_{(12)(12)}}{\Sigma_{3(12)}} C_{2}
\end{aligned}
$$

which proves the desired result. The last reduction is obtained by using that $\boldsymbol{y}$ and $\{F, \boldsymbol{z}\}$ are independent, where $\boldsymbol{z}^{\prime}=\left(\overline{\boldsymbol{x}}_{1}^{(1) \prime}, \overline{\boldsymbol{x}}_{2}^{(1) \prime}\right)-\left(\overline{\boldsymbol{x}}_{1}^{(2) \prime}, \overline{\boldsymbol{x}}_{2}^{(2) \prime}\right)$.

Now we will evaluate each expectation in Lemma 3.2. Considering the conditional expectation with respect to $G$ given $\left\{W_{(12)(12)}^{(1)}, W^{(2)}\right\}$, we can reduce it as follows.

$$
\begin{aligned}
\operatorname{Var}(\hat{\boldsymbol{\mu}}) & =\frac{1}{N^{2}}\binom{I_{p_{1}+p_{2}}}{\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1}}\left\{\left(N_{1}+N_{2}\right) \mathrm{E}\left[C \Sigma_{(12)(12)} C^{\prime}\right]\right. \\
& \left.+N_{3} \mathrm{E}\left[\binom{I_{p_{1}}}{F^{\prime}} \Sigma_{11}\left(I_{p_{1}} F\right)\right]\right\}\left[I_{p_{1}+p_{2}} \Sigma_{(12)(12)}^{-1} \Sigma_{(12) 3}\right]+\left(\begin{array}{cc}
O & O \\
O & a \Sigma_{33 \cdot 12}
\end{array}\right)
\end{aligned}
$$

where

$$
\begin{aligned}
a=\frac{1}{N_{1}} & \mathrm{E}\left[\operatorname { t r } ( W _ { ( 1 2 ) ( 1 2 ) } ^ { ( 1 ) } ) ^ { - 1 } \left\{\frac{N_{2}}{N_{1}\left(N_{1}+N_{2}\right)} \Sigma_{(12)(12)}\right.\right. \\
& \left.\left.+\frac{N_{3}}{N\left(N_{1}+N_{2}\right)}\binom{I_{p_{1}}}{F^{\prime}} \Sigma_{11}\left(I_{p_{1}} F\right)\right\}\right]
\end{aligned}
$$

Each expression in the above expression can be evaluated by using Lemmas 2.1 and 3.1. After simplification, we have the following theorem.

Theorem 3.1. Suppose that $N_{1}>p$. Then, the mean vector and the covariance of $\hat{\boldsymbol{\mu}}$ are given by
(i) $\quad \mathrm{E}[\hat{\boldsymbol{\mu}}]=\boldsymbol{\mu}$,
(ii) $\quad \operatorname{Var}[\hat{\mu}]=\binom{I_{p_{1}+p_{2}}}{\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1}}\left\{\frac{1}{N}\left(\begin{array}{cc}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\end{array}\right)\right.$

$$
\begin{aligned}
& \left.+\left(\begin{array}{cc}
O & O \\
O & \left(a_{1}+\frac{1}{N_{1}+N_{2}}\right) \Sigma_{22 \cdot 1}
\end{array}\right)\right\}\left(\begin{array}{ll}
I_{p_{1}+p_{2}} & \left.\Sigma_{(12)(12)}^{-1} \Sigma_{(12) 3}\right) \\
+\left(\begin{array}{cc}
O & O \\
O & \left(a_{2}+\frac{1}{N_{1}}\right) \Sigma_{33 \cdot 12}
\end{array}\right),\left(N_{1}>p_{1}+p_{2}+2\right)
\end{array}\right. \text { }
\end{aligned}
$$

where

$$
\begin{aligned}
a_{1}= & \frac{N_{3} p_{1}}{N\left(N_{1}+N_{2}\right)\left(N_{1}+N_{2}-p_{1}-2\right)}, \\
a_{2}= & \frac{N_{3} p_{1} p_{2}}{N\left(N_{1}+N_{2}\right)\left(N_{1}-p_{1}-p_{2}-2\right)}\left\{\frac{1}{N_{1}-p_{1}-2}-\frac{1}{N_{1}+N_{2}-p_{1}-2}\right\} \\
& +\frac{1}{N_{1}+N_{2}}\left\{\frac{N_{3} p_{1}}{N\left(N_{1}-p_{1}-2\right)}+\frac{N_{2}\left(p_{1}+p_{2}\right)}{N_{1}\left(N_{1}-p_{1}-p_{2}-2\right)}\right\} .
\end{aligned}
$$

Now, we consider asymptotic expression for the (ii) in Theorem 3.1 under the assumption (2). From Theorem 3.1 we can see that the asymptotic covariance matrix of $\sqrt{n}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})$ is given by

$$
\begin{aligned}
D= & \binom{I_{p_{1}+p_{2}}}{\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1}}\left(J_{1}+\frac{1}{\rho_{1}+\rho_{2}} J_{2}\right)\binom{I_{p_{1}+p_{2}}}{\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1}}^{\prime} \\
& +\frac{1}{\rho_{1}}\left(\begin{array}{cc}
O & O \\
O & \Sigma_{33 \cdot 12}
\end{array}\right),
\end{aligned}
$$

where $J_{1}$ and $J_{2}$ are given by (4).
It is interesting to compare the MLE's of $\boldsymbol{\mu}_{2}$ and $\boldsymbol{\mu}_{3}$ with their simple estimators $\tilde{\boldsymbol{\mu}}_{2}$ and $\tilde{\boldsymbol{\mu}}_{3}$ given by $\tilde{\boldsymbol{\mu}}_{2}=\frac{1}{N_{1}+N_{2}}\left\{N_{1} \overline{\boldsymbol{x}}_{2}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{2}^{(2)}\right\}$ and $\tilde{\boldsymbol{\mu}}_{3}=\overline{\boldsymbol{x}}_{3}^{(1)}$, respectively. From Theorem 3.1 we have that

$$
\text { (i) } \begin{aligned}
\Psi_{2} & =\operatorname{Var}\left(\tilde{\boldsymbol{\mu}}_{2}\right)-\operatorname{Var}\left(\hat{\boldsymbol{\mu}}_{2}\right) \\
& =\frac{N_{3}}{N\left(N_{1}+N_{2}\right)} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}-a_{1} \Sigma_{22 \cdot 1}
\end{aligned}
$$

$$
=\frac{N_{3}}{N\left(N_{1}+N_{2}\right)}\left\{\Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}+O\left(N^{-1}\right)\right\},
$$

(ii) $\Psi_{3}=\operatorname{Var}\left(\tilde{\boldsymbol{\mu}}_{3}\right)-\operatorname{Var}\left(\hat{\boldsymbol{\mu}}_{3}\right)$

$$
\begin{aligned}
= & \frac{N_{2}}{N\left(N_{1}+N_{2}\right)} \Sigma_{3(12)} \Sigma_{(12)(12)}^{-1} \Sigma_{(12) 3}+\frac{N_{3}}{N\left(N_{1}+N_{2}\right)} \Sigma_{31} \Sigma_{11}^{-1} \Sigma_{13} \\
& -a_{1} \Sigma_{32 \cdot 1} \Sigma_{22 \cdot 1}^{-1} \Sigma_{23 \cdot 1}-a_{2} \Sigma_{33 \cdot 12} \\
= & \frac{1}{N_{1}+N_{2}}\left\{\frac{N_{2}}{N_{1}} \Sigma_{3(12)} \Sigma_{(12)(12)}^{-1} \Sigma_{(12) 3}+\frac{N_{3}}{N} \Sigma_{31} \Sigma_{11}^{-1} \Sigma_{13}+O\left(N^{-1}\right)\right\} .
\end{aligned}
$$

Here $\Sigma_{32 \cdot 1}=\Sigma_{23 \cdot 1}^{\prime}=\Sigma_{32}-\Sigma_{31} \Sigma_{11}^{-1} \Sigma_{12}$. The result (i) ((ii)) shows that $\hat{\boldsymbol{\mu}}_{2}\left(\hat{\boldsymbol{\mu}}_{3}\right)$ is asymptotically better than $\tilde{\boldsymbol{\mu}}_{2}\left(\tilde{\boldsymbol{\mu}}_{3}\right)$, since $\Psi_{2}\left(\Psi_{3}\right)$ is asymptotically positive semidefinite.

Next we examine the bias properties of $\hat{\Sigma}$ and $\hat{\Delta}$. The final results are summarized as follows:

Theorem 3.2. Suppose that $N_{1}>p$. Then
(i) $\quad \mathrm{E}[\hat{\Sigma}]=\frac{N-1}{N} \Sigma+\frac{1}{N}\left(\begin{array}{ccc}O & O & O \\ O & B_{22} & B_{23} \\ O & B_{32} & B_{33}\end{array}\right),\left(N_{1}>p_{1}+p_{2}+2\right)$,
(ii) $\quad \mathrm{E}[\hat{\Delta}]=\Delta-\frac{1}{N}\left(\begin{array}{ccc}\Delta_{11} & O & O \\ O & \frac{\left(p_{1}+1\right) N}{N_{1}+N_{2}} \Delta_{22} & O \\ O & O & \frac{\left(p_{1}+p_{2}+1\right) N}{N_{1}} \Delta_{33}\end{array}\right)$,
where $B_{22}=b_{1} \Sigma_{22 \cdot 1}, B_{23}=B_{32}^{\prime}=b_{1} \Sigma_{22 \cdot 1} \Delta_{23}, B_{33}=b_{1} \Delta_{32} \Sigma_{22 \cdot 1} \Delta_{23}+b_{2} \Sigma_{33 \cdot 12}$, and

$$
\begin{gathered}
b_{1}=-N_{3}\left\{N_{1}+N_{2}-\left(p_{1}+1\right)\left(p_{2}+2\right)\right\} /\left\{N\left(N_{1}+N_{2}\right)\left(N_{1}+N_{2}-p_{1}-2\right)\right\}, \\
b_{2}=-\frac{1}{N}\left[\frac{\left(N_{2}+N_{3}\right)\left\{N_{1}-\left(p_{1}+1\right)\left(p_{1}+p_{2}+2\right)\right\}}{N_{1}\left(N_{1}-p_{1}-p_{2}-2\right)}+\frac{p_{2} N N_{2}}{N_{1}\left(N_{1}+N_{2}\right)}\right] \\
\left.+\frac{p_{1} p_{2} N_{3}}{\left(N_{1}-p_{1}-p_{2}-2\right)\left(N_{1}+N_{2}-p_{1}-2\right)}\right] .
\end{gathered}
$$

Proof. Since $W^{(1)}, W^{(2)}$ and $W^{(3)}$ are independently distributed as Wishart distributions $W_{p}\left(\Sigma, N_{1}-1\right), W_{p_{1}+p_{2}}\left(\Sigma_{(12)(12)}, N_{2}\right)$ and $W_{p_{1}}\left(\Sigma_{11}, N_{3}\right)$, respectively, it follows that $W_{11}^{(1)}+W_{11}^{(2)}+W^{(3)}$ is distributed as a Wishart distribution $W_{p_{1}}\left(\Sigma_{11}, N-1\right)$, and hence

$$
\mathrm{E}\left[\hat{\Sigma}_{11}\right]=\frac{N-1}{N} \Sigma_{11}
$$



Using Lemma 2.1(ii), we obtain

$$
\mathrm{E}\left[\hat{\Sigma}_{12}\right]=\mathrm{E}\left[\hat{\Sigma}_{11} \Sigma_{11}^{-1} \Sigma_{12}\right]=\frac{N-1}{N} \Sigma_{12}
$$

Using Lemma 2.1 (i) and (ii), we obtain

$$
\begin{aligned}
\mathrm{E}\left[\hat{\Sigma}_{22}\right]= & \frac{N_{1}+N_{2}-p-1}{N_{1}+N_{2}} \Sigma_{22 \cdot 1}+\mathrm{E}\left[\operatorname{tr}\left(W_{11}^{(1)}+W_{11}^{(2)}\right)^{-1} \hat{\Sigma}_{11}\right] \Sigma_{22 \cdot 1} \\
& +\Sigma_{21} \Sigma_{11}^{-1} \mathrm{E}\left[\hat{\Sigma}_{11}\right] \Sigma_{11}^{-1} \Sigma_{12} \\
= & \frac{N-1}{N} \Sigma_{22}+\frac{1}{N} b_{1} \Sigma_{22 \cdot 1} .
\end{aligned}
$$

Similarly

$$
\begin{aligned}
\mathrm{E}\left[\hat{\Sigma}_{(12) 3}\right]= & \mathrm{E}\left[\hat{\Sigma}_{(12)(12)}\right] \Sigma_{(12)(12)}^{-1} \Sigma_{(12) 3}, \\
\mathrm{E}\left[\hat{\Sigma}_{33}\right]= & \frac{1}{N_{1}}\left(N_{1}-p_{1}-p_{2}-1\right) \Sigma_{33 \cdot 12}+\mathrm{E}\left[\operatorname{tr}\left(W_{(12)(12)}^{(1)}\right)^{-1} \hat{\Sigma}_{(12)(12)}\right] \Sigma_{33 \cdot 12} \\
& +\Sigma_{3(12)} \Sigma_{(12)(12)}^{-1} \mathrm{E}\left[W_{(12)(12)}^{(1)}\right] \Sigma_{(12)(12)}^{-1} \Sigma_{(12) 3} .
\end{aligned}
$$

Applying Lemma 3.1 (iv) to these expressions, we obtain the first result. The second result is easily proved by some fundamental properties of Wishart matrices as in Lemma 2.1.

From Theorem 3.2 (ii) we obtain an exact unbiased estimator $\tilde{\Delta}$ of $\Delta$ given by

$$
\begin{gathered}
\tilde{\Delta}_{11}=\frac{N}{N-1} \hat{\Delta}_{11}, \quad \tilde{\Delta}_{12}=\hat{\Delta}_{12}, \quad \tilde{\Delta}_{22}=\frac{N_{1}+N_{2}}{N_{1}+N_{2}-p_{1}-1} \hat{\Delta}_{22} \\
\tilde{\Delta}_{(12) 3}=\hat{\Delta}_{(12) 3}, \quad \tilde{\Delta}_{33}=\frac{N_{1}}{N_{1}-p_{1}-p_{2}-1} \hat{\Delta}_{33}
\end{gathered}
$$

### 3.3. Asymptotic Distributions of $\hat{\mu}$ and $\hat{\Delta}$

Asymptotic expansions of the distributions of $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$ will be obtained by the same method as in Subsection 2.3. The main idea is to obtain stochastic expansions of the MLE's in terms of

$$
\begin{gathered}
\boldsymbol{z}^{(1)}=\sqrt{n_{1}}\left(\overline{\boldsymbol{x}}^{(1)}-\boldsymbol{\mu}\right), \boldsymbol{z}^{(2)}=\sqrt{n_{2}}\binom{\overline{\boldsymbol{x}}_{1}^{(2)}-\boldsymbol{\mu}_{1}}{\overline{\boldsymbol{x}}_{2}^{(2)}-\boldsymbol{\mu}_{2}}, \boldsymbol{z}^{(3)}=\sqrt{n_{3}}\left(\overline{\boldsymbol{x}}^{(3)}-\boldsymbol{\mu}_{1}\right), \\
V^{(1)}=\sqrt{n_{1}}\left(S^{(1)}-\Sigma\right), V^{(2)}=\sqrt{n_{2}}\left(S^{(2)}-\Sigma_{(12)(12)}\right), V^{(3)}=\sqrt{n_{3}}\left(S^{(3)}-\Sigma_{11}\right) .
\end{gathered}
$$

Here we note that $\boldsymbol{z}^{(1)} \sim N_{p}(\mathbf{0}, \Sigma), \boldsymbol{z}^{(2)} \sim N_{p_{1}+p_{2}}\left(\mathbf{0}, \Sigma_{(12)(12)}\right), \boldsymbol{z}^{(3)} \sim N_{p_{1}}(\mathbf{0}$, $\left.\Sigma_{11}\right), V^{(i)}$ has an asymptotic expansion, and these are independent. However, the computations as in Subsection 2.3 become to be very complicated. So, we give the first term in the asymptotic expansion.

The asymptotic distribution of $\sqrt{n}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})$ is obtained from noting that $\sqrt{n} \operatorname{Var}(\hat{\boldsymbol{\mu}})$ tends to $D$ (see Theorem 3.1 and (6)). Therefore, the result is stated as in the following theorem.

Theorem 3.3. When $N_{i}$ 's are large, $\sqrt{n}(\hat{\boldsymbol{\mu}}-\boldsymbol{\mu})$ is asymptotically distributed as $N_{p}(\mathbf{0}, D)$, where $D$ is given by (6).

By the same way as in the case $k=2$, based on a stochastic expansion of $\hat{\Delta}$, it is shown that the characteristic function of $\sqrt{n}(\hat{\Delta}-\Delta)$ can be expanded as follows:

$$
\begin{array}{r}
\exp \left[-\left\{\operatorname{tr}\left(T_{11} \Delta_{11}\right)^{2}+\frac{2}{\rho_{1}+\rho_{2}} \operatorname{tr} T_{21} \Delta_{11}^{-1} T_{12} \Delta_{22}+\frac{1}{\rho_{1}+\rho_{2}} \operatorname{tr}\left(T_{22} \Delta_{22}\right)^{2}\right.\right. \\
\left.\left.+\frac{2}{\rho_{1}} \operatorname{tr} T_{3(12)} \Sigma_{(12)(12)}^{-1} T_{(12) 3} \Delta_{33}+\frac{1}{\rho_{1}} \operatorname{tr}\left(T_{33} \Delta_{33}\right)^{2}\right\}\right]+O\left(n^{-1 / 2}\right)
\end{array}
$$

where $T$ is partitioned in the same way as $\Sigma$. This implies that we can use the following normalized matrix $U$, which is partitioned in the same way as $\Delta$ and whose submatrices $U_{i j}$ 's are given by

$$
\begin{aligned}
U_{11} & =\sqrt{\frac{n}{2}} \Delta_{11}^{-1 / 2}\left(\hat{\Delta}_{11}-\Delta_{11}\right) \Delta_{11}^{-1 / 2} \\
U_{12} & =\sqrt{\frac{n}{2}}\left(\rho_{1}+\rho_{2}\right)^{1 / 2} \Delta_{11}^{1 / 2}\left(\hat{\Delta}_{12}-\Delta_{12}\right) \Delta_{22}^{-1 / 2}, \\
U_{22} & =\sqrt{\frac{n}{2}}\left(\rho_{1}+\rho_{2}\right)^{1 / 2} \Delta_{22}^{-1 / 2}\left(\hat{\Delta}_{22}-\Delta_{22}\right) \Delta_{22}^{-1 / 2}, \\
U_{(12) 3} & =\sqrt{\frac{n \rho_{1}}{2}} \Sigma_{(12)(12)}^{1 / 2}\left(\hat{\Delta}_{(12) 3}-\Delta_{(12) 3}\right) \Delta_{33}^{-1 / 2}, \\
U_{33} & =\sqrt{\frac{n \rho_{1}}{2}} \Delta_{33}^{-1 / 2}\left(\hat{\Delta}_{33}-\Delta_{33}\right) \Delta_{33}^{-1 / 2} .
\end{aligned}
$$

Theorem 3.4. Let $U=\left[u_{i j}\right]$ be the standardized statistic of $\sqrt{n}(\hat{\Delta}-\Delta)$ defined by (7). Then $u_{i j}$ is asymptotically distributed as $N\left(0, \frac{1}{2}\left(1+\delta_{i j}\right)\right)$, where $\delta_{i j}$ is the Kronecker's delta. Further, the different elements of $U$ are asymptotically independent.

Proof. The result follows from that the characteristic function of $U$ can be expressed as follows:

$$
\begin{aligned}
& \exp \left[-\frac{1}{2}\left\{\operatorname{tr} T_{11}^{2}+2 \operatorname{tr} T_{21} T_{12}+\operatorname{tr} T_{22}^{2}+2 \operatorname{tr} T_{(21) 3} T_{3(12)}+\operatorname{tr} T_{33}^{2}\right\}\right]+O\left(n^{-1 / 2}\right) \\
& =\exp \left[-\frac{1}{2} \operatorname{tr} T^{2}\right]+O\left(n^{-1 / 2}\right)
\end{aligned}
$$

## 4. $k$-STEP MONOTONE MISSING DATA

In this section, we consider the general case $k$. As in Sections 2 and 3 , we denote $\boldsymbol{x}$ by $\left(\boldsymbol{x}_{1}^{\prime}, \boldsymbol{x}_{2}^{\prime}, \ldots, \boldsymbol{x}_{k}^{\prime}\right)^{\prime}$ where $\boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \ldots, \boldsymbol{x}_{k}$ are $p_{1}, p_{2}, \ldots, p_{k^{-}}$ dimensional vectors, respectively. Suppose we have $N_{1}$ observations on $\boldsymbol{x}, N_{2}$ observations on $\boldsymbol{x}^{(2)}=\left(\boldsymbol{x}_{1}^{\prime}, \boldsymbol{x}_{2}^{\prime}, \ldots, \boldsymbol{x}_{k-1}^{\prime}\right)^{\prime}, \ldots$, and $N_{k}$ observations on $\boldsymbol{x}_{1}$, and these observation vectors are independently distributed. The sample covariance matrices based on $N_{i}$ observations are expressed as

$$
S^{(i)}=\frac{1}{n_{i}} \sum_{\alpha=1}^{N_{i}}\left(\boldsymbol{x}_{\alpha}^{(i)}-\overline{\boldsymbol{x}}^{(i)}\right)\left(\boldsymbol{x}_{\alpha}^{(i)}-\overline{\boldsymbol{x}}^{(i)}\right)^{\prime}, \quad i=1, \ldots, k,
$$

where $n_{i}=N_{i}-1$.
Following the partitions of $\boldsymbol{x}$ we partition $\boldsymbol{\mu}, \Sigma$, etc. as

$$
\boldsymbol{\mu}=\left(\begin{array}{c}
\boldsymbol{\mu}_{1} \\
\boldsymbol{\mu}_{2} \\
\vdots \\
\boldsymbol{\mu}_{k}
\end{array}\right), \quad \Sigma=\left(\begin{array}{cccc}
\Sigma_{11} & \Sigma_{12} & \cdots & \Sigma_{1 k} \\
\Sigma_{21} & \Sigma_{22} & \cdots & \Sigma_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
\Sigma_{k 1} & \Sigma_{k 2} & \cdots & \Sigma_{k k}
\end{array}\right), \quad \text { etc. }
$$

The usual transformed matrix $\Delta=\left[\Delta_{i j}\right]$ of $\Sigma$ is defined by

$$
\begin{aligned}
& \Delta_{11}=\Sigma_{11}, \quad \Delta_{12}=\Delta_{21}^{\prime}=\Sigma_{11}^{-1} \Sigma_{12} \\
& \Delta_{j j}=\Sigma_{j j}-\Sigma_{j(1 \ldots j-1)} \Sigma_{(1 \ldots j-1)(1 \ldots j-1)}^{-1} \Sigma_{(1 \ldots j-1) j} \\
& \Delta_{(1 \ldots j-1) j}=\left(\begin{array}{c}
\Delta_{1 j} \\
\vdots \\
\Delta_{j-1 j}
\end{array}\right)=\Delta_{j(1 \ldots j-1)}^{\prime} \\
& \quad=\Sigma_{(1 \ldots j-1)(1 \ldots j-1)}^{-1} \Sigma_{(1 \ldots j-1) j}, \quad j=2, \ldots, k
\end{aligned}
$$

We can obtain the MLE's $\hat{\mu}$ and $\hat{\Delta}$ numerically, following the steps (i) $\sim$ (iv) below.
(i) Sample mean vectors:

For $i=1, \ldots, k-j+1 ; j=1, \ldots, k$,

$$
\begin{aligned}
& \overline{\boldsymbol{x}}_{i}^{[j]}=\frac{1}{N_{1}+\cdots+N_{j}}\left(N_{1} \overline{\boldsymbol{x}}_{i}^{(1)}+\cdots+N_{j} \overline{\boldsymbol{x}}_{i}^{(j)}\right), \\
& \overline{\boldsymbol{x}}_{[i]}^{[j]}=\left(\begin{array}{c}
\overline{\boldsymbol{x}}_{1}^{[j]} \\
\vdots \\
\overline{\boldsymbol{x}}_{i}^{[j]}
\end{array}\right), \quad \overline{\boldsymbol{x}}_{[i]}^{(j)}=\left(\begin{array}{c}
\overline{\boldsymbol{x}}_{1}^{(j)} \\
\vdots \\
\overline{\boldsymbol{x}}_{i}^{(j)}
\end{array}\right) .
\end{aligned}
$$

(ii) Sample covariance matrices:

For $a, b, i=1, \ldots, k-j+1 ; j=1, \ldots, k$,

$$
\begin{aligned}
W^{(1)}= & n_{1} S^{(1)}, \\
W^{(j)}= & n_{j} S^{(j)}+\frac{N_{j}\left(N_{1}+\cdots+N_{j-1}\right)}{N_{1}+\cdots+N_{j}}\left(\overline{\boldsymbol{x}}_{[k-j+1]}^{(j)}-\overline{\boldsymbol{x}}_{[k-j+1]}^{[j-1]}\right) \\
& \quad \times\left(\overline{\boldsymbol{x}}_{[k-j+1]}^{(j)}-\overline{\boldsymbol{x}}_{[k-j+1]}^{[j-1]}\right)^{\prime}, \quad j=2, \ldots, k,
\end{aligned}
$$

(iii) MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\Delta}$ :

Using a conditional approach, it can be shown that the MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\Delta}$ are expressed as follows:

$$
\begin{aligned}
\hat{\boldsymbol{\mu}}_{1} & =\overline{\boldsymbol{x}}_{1}^{[k]}, \quad \hat{\boldsymbol{\mu}}_{i}=\overline{\boldsymbol{x}}_{i}^{[k-i+1]}-\hat{\Delta}_{i(1 \ldots i-1)}\left(\overline{\boldsymbol{x}}_{[i-1]}^{[k-i+1]}-\hat{\boldsymbol{\mu}}_{[i-1]}\right), \\
\hat{\Delta}_{i(1 \ldots i-1)} & =W_{i(1 \ldots i-1)}^{[k-i+1]}\left\{W_{(1 \ldots i-1)(1 \ldots i-1)}^{[k-i+1]}\right\}^{-1}, \quad \hat{\Delta}_{11}=\frac{1}{N_{1}+\cdots+N_{k}} W_{11}^{[k]}, \\
\hat{\Delta}_{i i} & =\frac{1}{N_{1}+\cdots+N_{k-i+1}} W_{i i-1 \ldots i-1}^{[k-i+1]}, \quad \hat{\boldsymbol{\mu}}_{[i]}^{\prime}=\left(\hat{\boldsymbol{\mu}}_{1}^{\prime}, \cdots, \hat{\boldsymbol{\mu}}_{i}^{\prime}\right) .
\end{aligned}
$$

(iv) MLE's $\hat{\Sigma}$ :

The MLE $\hat{\Sigma}$ of $\Sigma$ is obtained by using the transformation from $\Delta$ to $\Sigma$. In fact,

$$
\begin{aligned}
& \hat{\Sigma}_{11}=\hat{\Delta}_{11}, \quad \hat{\Sigma}_{12}=\hat{\Delta}_{11} \hat{\Delta}_{12}, \\
& \hat{\Sigma}_{j j}=\hat{\Delta}_{j j}+\hat{\Delta}_{j(1 \ldots j-1)} \hat{\Sigma}_{(1 \ldots j-1)(1 \ldots j-1)} \hat{\Delta}_{(1 \ldots j-1) j}, \\
& \hat{\Sigma}_{(1 \ldots j-1) j}=\hat{\Sigma}_{(1 \ldots j-1)(1 \ldots j-1)} \hat{\Delta}_{(1 \ldots j-1) j}, \quad j=2, \ldots, k .
\end{aligned}
$$

Lemma 4.1. Let $W^{(j)}, j=1, \ldots, k$, be the random matrices defined by (8). Then $W^{(1)}, \ldots, W^{(k)}$ are mutually independent, and

$$
\begin{aligned}
W^{(1)} & \sim W_{p}\left(\Sigma, N_{1}-1\right) \\
W^{(j)} & \sim W_{p_{1}+\cdots+p_{k-j+1}}\left(\Sigma_{(1 \ldots k-j+1)(1 \ldots k-j+1)}, N_{j}\right), \quad j=2, \ldots, k .
\end{aligned}
$$

Proof. The result is proved by noting that for $j=2, \ldots, k$,

$$
\begin{aligned}
\overline{\boldsymbol{x}}_{[k-j+1]}^{(j)}- & \overline{\boldsymbol{x}}_{[k-j+1]}^{[j-1]} \\
& \sim N_{p_{1}+\cdots+p_{k-j+1}}\left(\mathbf{0}, \frac{N_{1}+\cdots+N_{j}}{N_{j}\left(N_{1}+\cdots+N_{j-1}\right)} \Sigma_{(1 \ldots k-j+1)(1 \ldots k-j+1)}\right),
\end{aligned}
$$

and they are independent.
Using the above expressions of MLE's and Lemma 4.1, we can obtain some analogous results on the properties of MLE's. These are obtained by the lines similar to the ones as in the cases $k=2$ and 3 . So, we give them without proofs. Fujisawa (1995) has proved Theorem 4.2 (i).

Theorem 4.1. Suppose that $N_{1}>p$. Then, the MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\Delta}$ satisfy the following properties: For $i=2, \ldots, k$,
(i) $\quad \Delta_{i(1 \ldots i-1)}$ and $\left\{\overline{\boldsymbol{x}}_{[i-1]}^{[k-i+1]}, \hat{\boldsymbol{\mu}}_{[i]}\right\}$ are independent,
(ii) $\quad \hat{\Delta}_{i i}$ and $\left\{\hat{\Delta}_{(1 \ldots i-1)(1 \ldots i-1)}, \hat{\Delta}_{i(1 \ldots i-1)},\right\}$ are independent, in particular, $\hat{\Delta}_{11}, \ldots, \hat{\Delta}_{k k}$ are independent,
(iii)

$$
\begin{aligned}
\left(N_{1}+\cdots\right. & \left.+N_{k}\right) \hat{\Delta}_{11} \sim W_{p_{1}}\left(\Delta_{11}, N_{1}+\cdots+N_{k}-1\right) \\
\left(N_{1}+\cdots+\right. & \left.N_{k-i+1}\right) \hat{\Delta}_{i i} \\
& \sim W_{p_{i}}\left(\Delta_{i i}, N_{1}+\cdots+N_{k-i+1}-p_{1}-\cdots-p_{i-1}-1\right)
\end{aligned}
$$

Now we note that the condition $N_{1}>p$ mentioned in Section 1 is a necessary and sufficient condition for the MLE's of ( $\boldsymbol{\mu}, \Sigma$ ) to exist uniquely, which is equivalent to the one for the MLE of $\Sigma$ to exist uniquely. This will be seen from Theorem 4.1 (iii). In fact, the latter condition is equivalent to the one for the MLE's of $\Delta_{i i}, i=1,2, \ldots, k$, to exist uniquely. Therefore, we have that this condition is given by

$$
\begin{aligned}
& N_{1}+\cdots+N_{k}-1 \geq p \\
& N_{1}+\cdots+N_{k-i+1}-p_{1}-\cdots-p_{i-1}-1 \geq p_{i}, \quad(i=2, \ldots, k)
\end{aligned}
$$

which is equivalent to the condition $N_{1}>p$.
Theorem 4.2. Suppose that $N_{1}>p$. Then
(i) $\quad \mathrm{E}[\hat{\boldsymbol{\mu}}]=\boldsymbol{\mu}$,
(ii) $\quad \mathrm{E}\left[\hat{\Delta}_{11}\right]=\left(1-\frac{1}{N_{1}+\cdots+N_{k}}\right) \Delta_{11}$.



For $i=2, \ldots, k$,

$$
\begin{aligned}
& \mathrm{E}\left[\hat{\Delta}_{i(1 \ldots i-1)}\right]=\Delta_{i(1 \ldots i-1)} \\
& \mathrm{E}\left[\hat{\Delta}_{i i}\right]=\left(1-\frac{p_{1}+\cdots+p_{i-1}+1}{N_{1}+\cdots+N_{k-i+1}}\right) \Delta_{i i}
\end{aligned}
$$

Theorem 4.3. Let $\rho_{i}=n_{i} / n, i=1, \ldots, k$, and

$$
\begin{aligned}
U_{i i}= & \sqrt{\frac{n}{2}}\left\{\rho_{1}+\cdots+\rho_{k-i+1}\right\}^{1 / 2} \Delta_{11}^{-1 / 2}\left(\hat{\Delta}_{11}-\Delta_{11}\right) \Delta_{11}^{-1 / 2}, i=1, \ldots, k, \\
U_{(1 \ldots i-1) i}= & \sqrt{\frac{n}{2}}\left\{\rho_{1}+\cdots+\rho_{k-i+1}\right\}^{1 / 2} \Sigma_{(1 \ldots i-1) i}^{1 / 2}\left(\hat{\Delta}_{(1 \ldots i-1) i}-\Delta_{(1 \ldots i-1) i}\right) \Delta_{i i}^{-1 / 2}, \\
& i=1, \ldots, k .
\end{aligned}
$$

Then the $(i, j)$ element $u_{i j}$ of $U$ is asymptotically distributed as $N\left(0, \frac{1}{2}\left(1+\delta_{i j}\right)\right)$. Further, the different elements of $U$ are asymptotically independent.

We can expect that the MLE $\hat{\boldsymbol{\mu}}$ possesses the same optimum properties as in the cases $k=2$ and 3 , in the comparison with the simple estimator $\tilde{\boldsymbol{\mu}}$ of $\boldsymbol{\mu}$. However, it becomes very complicated to derive the exact covariance matrix of $\hat{\boldsymbol{\mu}}$, which is left as a future problem.

## 5. NUMERICAL EXAMPLE

In order to explain our results, we consider a multivariate normal population $N_{p}(\mu, \Sigma)$ whose true parameters are given as

$$
\boldsymbol{\mu}^{\prime}=(9.159,25.431,13.165,31.925,28.588,8.778)
$$

and

$$
\Sigma=\left(\begin{array}{rrrrrr}
2.835 & -0.122 & 0.544 & 0.053 & 0.207 & 0.202 \\
-1.286 & 39.235 & 0.166 & 0.533 & 0.343 & 0.128 \\
2.870 & 3.251 & 9.806 & 0.486 & 0.274 & 0.187 \\
0.559 & 20.749 & 9.465 & 38.694 & 0.401 & 0.092 \\
1.913 & 11.803 & 4.699 & 13.688 & 30.100 & 0.445 \\
0.593 & 1.395 & 1.020 & 0.992 & 4.253 & 3.035
\end{array}\right) .
$$

Here the upper parts of $\Sigma$ denote correlation coefficient. Note that such expressions for covariance matrices are used in this section. These population
quantities were taken from the ones in Srivastava and Carter (Problem of 12.5 in page 339).

Based on a set of 50 samples from this population, we construct two artificial samples with the following missing patterns and consider the corresponding estimation problems.

Case (i). $p=q_{1}=4, q_{2}=2, N=N_{1}+N_{2}, N_{1}=30, N_{2}=20$.
In this case, the samples of the first four variates are used. The first 30 observations are four dimensional complete data and the remainder 20 observations are two dimensional missing data.

Case (ii). $p=q_{1}=6, q_{2}=4, q_{3}=2, N=N_{1}+N_{2}+N_{3}, N_{1}=20, N_{2}= 15, N_{3}=15$.

In the case (ii), the first 20 observations are six dimensional complete data, the second 15 observations are four dimensional missing data and the last 15 observations consist of two dimensional missing data.

For the case (i), we obtain the MLE's by using a closed form in Section 2 as follows:

$$
\hat{\boldsymbol{\mu}}^{\prime}=(9.159,25.431,12.986,32.302)
$$

and covariance matrix

$$
\hat{\Sigma}=\left(\begin{array}{rrrr}
2.778 & -0.122 & 0.474 & -0.064 \\
-1.260 & 38.450 & 0.062 & 0.375 \\
2.340 & 1.143 & 8.756 & 0.460 \\
-0.583 & 12.803 & 7.488 & 30.307
\end{array}\right)
$$

On the other hand, the MLE's which are composed of only complete data are

$$
\bar{\mu}^{\prime}=(9.223,26.179,13.085,32.546)
$$

and covariance matrix

$$
\bar{\Sigma}=\left(\begin{array}{rrrr}
2.802 & -0.090 & 0.475 & -0.048 \\
-0.816 & 29.280 & 0.061 & 0.328 \\
2.386 & 0.995 & 9.017 & 0.466 \\
-0.437 & 9.741 & 7.686 & 30.182
\end{array}\right) .
$$

From Theorem 2.1 we have

$$
\operatorname{Var}[\hat{\boldsymbol{\mu}}]=\left(\begin{array}{cccc}
0.051 & 0.088 & 0.263 & 0.153 \\
0.017 & 0.740 & 0.149 & 0.300 \\
0.031 & 0.067 & 0.273 & 0.309 \\
0.036 & 0.269 & 0.168 & 1.086
\end{array}\right)
$$

On the other hand,

$$
\operatorname{Var}[\bar{\mu}]=\left(\begin{array}{llll}
0.086 & 0.086 & 0.335 & 0.192 \\
0.028 & 1.233 & 0.189 & 0.380 \\
0.052 & 0.111 & 0.281 & 0.340 \\
0.060 & 0.449 & 0.192 & 1.134
\end{array}\right)
$$

It is seen that $\hat{\boldsymbol{\mu}}$ is better than $\overline{\boldsymbol{\mu}}$ on the criteria of bias and variance.
For the case (ii), first we show how the MLE's can be computed. The MLE's can be obtained by the four steps (i) $\sim$ (iv) in Section 4, though an explicit expression in subsection 3.1 is available for 3 -step monotone case. The first step (i) may be divided as follows.

$$
\begin{aligned}
\left(\mathrm{i}_{1}\right) ; \overline{\boldsymbol{x}}_{[1]}^{[1]} & =\overline{\boldsymbol{x}}_{1}^{[1]}=\overline{\boldsymbol{x}}_{1}^{(1)}, \quad \overline{\boldsymbol{x}}_{[2]}^{[1]}=\binom{\overline{\boldsymbol{x}}_{1}^{[1]}}{\overline{\boldsymbol{x}}_{2}^{1]}}=\binom{\overline{\boldsymbol{x}}_{1}^{(1)}}{\overline{\boldsymbol{x}}_{2}^{(1)}}=\overline{\boldsymbol{x}}_{[2]}^{(1)}, \\
\overline{\boldsymbol{x}}_{[3]}^{[1]} & =\left(\begin{array}{l}
\overline{\boldsymbol{x}}_{1}^{[1]} \\
\overline{\boldsymbol{x}}_{2}^{[1]} \\
\overline{\boldsymbol{x}}_{3}^{[1]}
\end{array}\right)=\left(\begin{array}{l}
\overline{\boldsymbol{x}}_{1}^{(1)} \\
\overline{\boldsymbol{x}}_{2}^{(1)} \\
\overline{\boldsymbol{x}}_{3}^{(1)}
\end{array}\right)=\overline{\boldsymbol{x}}_{[3]}^{(1)}, \\
\left(\mathrm{i}_{2}\right) ; \overline{\boldsymbol{x}}_{[1]}^{(2)} & =\overline{\boldsymbol{x}}_{1}^{(2)}, \quad \overline{\boldsymbol{x}}_{[1]}^{[2]}=\overline{\boldsymbol{x}}_{1}^{[2]}=\frac{1}{N_{1}+N_{2}}\left(N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{1}^{(2)}\right), \\
\overline{\boldsymbol{x}}_{[2]}^{(2)} & =\binom{\overline{\boldsymbol{x}}_{1}^{(2)}}{\overline{\boldsymbol{x}}_{2}^{(2)}}, \quad \overline{\boldsymbol{x}}_{[2]}^{[2]}=\binom{\overline{\boldsymbol{x}}_{1}^{[2]}}{\overline{\boldsymbol{x}}_{2}^{[2]}}=\frac{1}{N_{1}+N_{2}}\binom{N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{1}^{(2)}}{N_{1} \overline{\boldsymbol{x}}_{2}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{2}^{(2)}}, \\
\left(\mathrm{i}_{3}\right) ; \overline{\boldsymbol{x}}_{[1]}^{(3)} & =\overline{\boldsymbol{x}}^{(3)}, \quad \overline{\boldsymbol{x}}_{[1]}^{[3]}=\overline{\boldsymbol{x}}_{1}^{[3]}=\frac{1}{N}\left(N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}_{1}^{(2)}+N_{3} \overline{\boldsymbol{x}}^{(3)}\right) .
\end{aligned}
$$

The second step (ii) is to compute

$$
\begin{aligned}
& W^{(1)}=n_{1} S^{(1)}=\left(\begin{array}{lll}
W_{11}^{(1)} & W_{12}^{(1)} & W_{13}^{(1)} \\
W_{21}^{(1)} & W_{22}^{(1)} & W_{23}^{(1)} \\
W_{31}^{(1)} & W_{32}^{(1)} & W_{33}^{(1)}
\end{array}\right), \\
& W^{(2)}=n_{2} S^{(2)}+\frac{N_{1} N_{2}}{N_{1}+N_{2}}\left(\overline{\boldsymbol{x}}_{[2]}^{(2)}-\overline{\boldsymbol{x}}_{[2]}^{(1)}\right)\left(\overline{\boldsymbol{x}}_{[2]}^{(2)}-\overline{\boldsymbol{x}}_{[2]}^{(1)}\right)^{\prime}=\left(\begin{array}{ll}
W_{11}^{(2)} & W_{12}^{(2)} \\
W_{21}^{(2)} & W_{22}^{(2)}
\end{array}\right), \\
& W^{(3)}=n_{3} S^{(3)}+\frac{N_{3}\left(N_{1}+N_{2}\right)}{N}\left(\overline{\boldsymbol{x}}_{[1]}^{(3)}-\overline{\boldsymbol{x}}_{[1]}^{[2]}\right)\left(\overline{\boldsymbol{x}}_{[1]}^{(3)}-\overline{\boldsymbol{x}}_{[1]}^{[2]}\right)^{\prime}=W_{11}^{(3)} .
\end{aligned}
$$

Further, $W_{a b}^{[j]}$ 's are obtained as

$$
\begin{aligned}
& W^{[1]}=W^{(1)}, \quad W_{a b}^{[1]}=W_{a b}^{(1)} \\
& W^{[2]}=W_{(12)(12)}^{(1)}+W^{(2)}=\left(\begin{array}{ll}
W_{11}^{[2]} & W_{12}^{[2]} \\
W_{21}^{[2]} & W_{22}^{[2]}
\end{array}\right) \\
& W_{11}^{[3]}=W^{(3)}
\end{aligned}
$$

By using the quantities as in the steps (i) and (ii), the third step (iii) is compute $\hat{\boldsymbol{\mu}}$ and $\hat{\Delta}$ as follows :

$$
\begin{aligned}
& \hat{\boldsymbol{\mu}}_{1}=\overline{\boldsymbol{x}}_{1}^{[3]}, \hat{\Delta}_{11}=\frac{1}{N} W_{11}^{[3]}, \hat{\Delta}_{21}=W_{21}^{[2]}\left(W_{11}^{[2]}\right)^{-1}, \hat{\Delta}_{22}=\frac{1}{N_{1}+N_{2}} W_{22 \cdot 1}^{[2]}, \\
& \hat{\boldsymbol{\mu}}_{2}=\overline{\boldsymbol{x}}_{2}^{[2]}-\hat{\Delta}_{21}\left(\overline{\boldsymbol{x}}_{[1]}^{[2]}-\hat{\boldsymbol{\mu}}_{1}\right), \quad \hat{\Delta}_{3(12)}=W_{3(12)}^{[1]}\left\{W_{(12)(12)}^{[1]}\right\}^{-1}=\hat{\Delta}_{(12) 3}^{\prime}, \\
& \hat{\boldsymbol{\mu}}_{3}=\overline{\boldsymbol{x}}_{3}^{[1]}-\hat{\Delta}_{3(12)}\left(\overline{\boldsymbol{x}}_{[2]}^{[1]}-\hat{\boldsymbol{\mu}}_{[2]}\right), \quad \hat{\Delta}_{33}=\frac{1}{N_{1}} W_{33 \cdot 12}^{[1]}=\frac{1}{N_{1}} W_{33 \cdot 12}^{(1)} .
\end{aligned}
$$

Finally, we obtain the MLE's $\hat{\Sigma}_{i j}$ 's by using $\hat{\Delta}_{i j}$.

$$
\begin{aligned}
\hat{\Sigma}_{11} & =\hat{\Delta}_{11}, \quad \hat{\Sigma}_{12}=\hat{\Delta}_{11} \hat{\Delta}_{12}, \quad \hat{\Sigma}_{22}=\hat{\Delta}_{22}+\hat{\Delta}_{21} \hat{\Sigma}_{11} \hat{\Delta}_{12} \\
\hat{\Sigma}_{(12) 3} & =\hat{\Sigma}_{(12)(12)} \hat{\Delta}_{(12) 3}, \quad \hat{\Sigma}_{33}=\hat{\Delta}_{33}+\hat{\Delta}_{3(12)} \hat{\Sigma}_{(12)(12)} \hat{\Delta}_{(12) 3}
\end{aligned}
$$

These give the MLE's as

$$
\begin{aligned}
\hat{\boldsymbol{\mu}}^{\prime} & =(9.159,25.431,12.999,31.791,29.014,9.132), \\
\hat{\Sigma} & =\left(\begin{array}{rrrrrr}
2.779 & -0.122 & 0.556 & -0.024 & -0.102 & -0.269 \\
-1.260 & 38.450 & 0.133 & 0.558 & 0.619 & 0.260 \\
2.901 & 2.583 & 9.797 & 0.477 & 0.020 & -0.370 \\
-0.256 & 21.908 & 9.451 & 40.022 & 0.566 & -0.121 \\
-0.786 & 17.655 & 0.290 & 16.481 & 21.177 & 0.077 \\
-0.696 & 2.507 & -1.801 & -1.192 & 0.551 & 2.416
\end{array}\right),
\end{aligned}
$$

while the MLE's which are made only from the complete data are

$$
\begin{aligned}
\overline{\boldsymbol{\mu}}^{\prime} & =(9.377,25.436,13.169,32.688,29.371,9.048), \\
\bar{\Sigma} & =\left(\begin{array}{rrrrrr}
3.199 & 0.108 & 0.602 & -0.122 & -0.015 & -0.154 \\
1.052 & 29.435 & 0.068 & 0.401 & 0.529 & 0.278 \\
2.735 & 0.942 & 6.461 & 0.164 & -0.119 & -0.281 \\
-1.011 & 10.070 & 1.936 & 21.450 & 0.483 & -0.044 \\
-0.114 & 12.446 & -1.310 & 9.689 & 18.774 & 0.082 \\
-0.420 & 2.299 & -1.088 & -0.314 & 0.540 & 2.325
\end{array}\right) .
\end{aligned}
$$

For 3 -step monotone case, we derive an explicit expression of $\operatorname{Var}(\hat{\boldsymbol{\mu}})$ in Theorem 3.1, which gives

$$
\operatorname{Var}[\hat{\boldsymbol{\mu}}]=\left(\begin{array}{cccccc}
0.051 & 0.088 & 0.283 & 0.165 & 0.117 & 0.075 \\
0.017 & 0.740 & 0.161 & 0.323 & 0.172 & 0.024 \\
0.031 & 0.067 & 0.235 & 0.317 & 0.093 & 0.052 \\
0.036 & 0.269 & 0.149 & 0.938 & 0.276 & 0.104 \\
0.027 & 0.152 & 0.046 & 0.274 & 1.052 & 0.320 \\
0.008 & 0.010 & 0.012 & 0.048 & 0.156 & 0.226
\end{array}\right) .
$$

On the other hand,

$$
\operatorname{Var}[\overline{\boldsymbol{\mu}}]=\left(\begin{array}{cccccc}
0.129 & 0.088 & 0.334 & 0.192 & 0.174 & 0.122 \\
0.043 & 1.850 & 0.189 & 0.380 & 0.260 & 0.040 \\
0.078 & 0.167 & 0.422 & 0.341 & 0.143 & 0.080 \\
0.090 & 0.674 & 0.289 & 1.701 & 0.375 & 0.142 \\
0.067 & 0.380 & 0.100 & 0.525 & 1.151 & 0.334 \\
0.021 & 0.026 & 0.025 & 0.089 & 0.172 & 0.230
\end{array}\right) .
$$

It is also seen that $\hat{\boldsymbol{\mu}}$ is better than $\overline{\boldsymbol{\mu}}$ on the criteria of bias and variance.

## ACKNOWLEDGEMENTS

The authors wish to thank the referees and Professor Dudewicz for their valuable comments.

## REFERENCES

Anderson, S. A. and Perlman, M. D. (1991). Lattice-ordered conditional independence models for missing data, Statistics and Probability Letters, 12, 465-486.

Anderson, T.W.(1957). Maximum likelihood estimates for a multivariate normal distribution when some observations are missing, Journal of the American Statistical Association, 52, 200-203.

Anderson, T. W., and Olkin, I. (1985). Maximum-likelihood estimation of the parameters of a multivariate normal distribution, Linear Algebra and Its Applications, 70, 147-171.

Bhargava, R. P. (1975). Some one-sample hypothesis testing problems when there is a monotone sample from a multivariate normal population, Annals of the Institute of Statistical Mathematics, 27, 327-339.

Dempster, A. P., Laird, N. M. and Rubin, D. B. (1977). Maximum likelihood from incomplete data via the EM algorithm, Journal of the Royal Statistical Society, Ser. B, 39, 1-38.

Fujikoshi, Y. (1977). An asymptotic expansion for the distributions of the latent roots of the Wishart matrix with multiple population roots, Annals of the Institute of Statistical Mathematics, 29, 379-387.

Fujisawa, H. (1995). A note on the maximum likelihood estimators for multivariate normal distribution with monotone data, Communications in Statistics A, Theory and Methods, 24, 1377-1382.



Jinadasa, K. G., and Tracy, D. S. (1992). Maximum likelihood estimation for multivariate normal distribution with monotone sample, Communications in Statistics A, Theory and Methods, 21, 41-50.

Little, R. J. A., and Rubin, D. B. (1987). Statistical Analysis with Missing Data, Wiley, New York.

Muirhead, R. J. (1982). Aspects of Multivariate Statistical Theory, Wiley, New York.

Rubin, D. B. (1974). Characterizing the estimation of parameters in incom plete-data problems, Journal of the American Statistical Association, 69, 467-474.

Rubin, D. B. (1976). Inference and missing data, Biometrika, 63, 581-592.
Siotani, M., Hayakawa, T., and Fujikoshi, Y. (1985). Modern Multivariate Statistical Analysis: A Graduate Course and Handbook, American Sciences Press, Inc., Columbus, Ohio.

Srivastava, M. S. (1985), Multivariate data with missing observations, Communications in Statistics, Theory and Methods, 14, 775-792.

Srivastava, M. S., and Carter, E. M. (1983). An Introduction to Applied Multivariate Statistics, North-Holland, New York.
.
![](https://cdn.mathpix.com/cropped/d2d1cfb3-cb43-4ee6-977d-70deecdfa631-33.jpg?height=1613&width=1094&top_left_y=274&top_left_x=161)

