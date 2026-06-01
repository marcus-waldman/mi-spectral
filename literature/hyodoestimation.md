---
citekey: hyodoestimation
item_type: techreport
authors: 'Hyodo, Masashi and Shutoh, Nobumichi and Seo, Takashi and Pavlenko, Tatjana'
year: 2013
title: Estimation of the Large Covariance Matrix with Two-Step Monotone Missing Data
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\hyodoestimation.pdf'
pdf_sha256: 4e6e771b19264d8b113304b46564a86e4473d2b3c6a9f30aa965cffecf00f11d
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T23:14:22Z
---
# Estimation of the large covariance matrix with two-step monotone missing data 

Masashi Hyodo ${ }^{1 *}$, Nobumichi Shutoh ${ }^{2}$,<br>Takashi Seo ${ }^{1}$, and Tatjana Pavlenko ${ }^{3}$

${ }^{1}$ Department of Mathematical Information Science, Tokyo University of Science
${ }^{2}$ Department of Health Sciences, Oita University of Nursing and Health Sciences
${ }^{3}$ Department of Mathematics, KTH Royal Institute of Technology

We suggest a shrinkage based technique for estimating covariance matrix in the high-dimensional normal model with missing data. Our asymptotic framework allows the dimensionality $p$ grow to infinity together with the sample size, $N$, and extends the methodology of Ledoit and Wolf (2004) to the case of 2-step monotone missing data. Two new shrinkage type estimators are derived and their dominance properties over the Ledoit and Wolf (2004) estimator are shown under the expected quadratic loss. We perform a simulation study and conclude that the proposed estimators are successful for a range of missing data scenarios.

Key Words Monotone missing data; High-dimensional estimation; Shrinkage type estimation.

[^0]
## 1 Introduction

Estimation of the covariance matrix $\Sigma$ in high dimensions has been important for many statistical procedures such as principal component analysis, linear regression and discriminant analysis. Some of these procedures require estimation of the covariance structure and eigenvalues of $\Sigma$ while the others need the inverse. It has long been known that standard estimators such as maximum likelihood or least squares developed for large sample sizes $N$ and relatively small number of variables $p$ do not provide a satisfactory solution in high dimensions. Therefore modification of these estimators is of crucial importance for high-dimensional problems.

During recent years, many methods for improving the estimators of $\Sigma$ and its inverse in the context of high dimensional data, i.e. if the number of variables $p$ is much larger than $N$, have been developed; see e.g., Kubokawa and Srivastava (2008) and Ledoit and Wolf (2004). However, all of these methods have been focused on the case where all data is observed. Since in practice data sets often contain missing patterns, it is important to develop approaches for high dimensional covariance estimation in presence of missing data.

In this study, we focus on a particular type of statistical missing data, a monotone missing scheme with missing values patterns occurring completely at random. In other words, we assume that the underlying missing-data mechanism is ignorable under parametric estimation. This type of missing data problem has been extensively studied in the statistical literature; see e.g. Anderson (1957), Bhargava (1975). The sample scheme treated in them is called a $k$-step monotone missing data. In particular, in Anderson and Olkin (1985), the MLE of $\Sigma$ for the case of 2-step monotone missing data was derived explicitly. Further, Kanda and Fujikoshi (1998) studied asymptotic properties of MLE of $\Sigma$ constructed by 2 -step monotone missing data and extend these results to the general case of $k$-step monotone missing data. However, in high dimensional situations, the MLE of $\Sigma$ is known to perform poorly even for the case of complete data, since it is usually impossible to collect
enough observations to fulfill $p \ll n$ condition.
In this paper, we present a solution to this problem by extending the idea of Ledoit and Wolf (2004) to the case of 2 -step monotone missing data and suggest a new estimator of the covariance matrix that is adjusted to high dimensionality in combination with missing data.

The rest of the paper is organized as follows. In Section 2, we set up 2-step monotone missing data scheme and derive some auxiliary unbiased estimators, which then will be used in Section 3 where we present our new shrinkage estimators. Section 4 reports numerical studies on the risk performance of the suggested estimators and comparison with results by Ledoit and Wolf (2004). We conclude in Section 5 and present the proof of key results in Appendix (A.2, A.3 and A.4).

## 2 Auxiliary unbiased estimators and their asymptotic property under the 2 -step monotone missing data

To specify the problem considered here, let $\boldsymbol{x}$ be the $p$-dimensional random vector distributed as $N_{p}(\boldsymbol{\mu}, \Sigma)$, where $\boldsymbol{\mu}$ is mean vector and $\Sigma$ is covariance matrix. Assume that $\boldsymbol{x}$ can be decomposed as $\left(\boldsymbol{x}_{1}^{\prime}, \boldsymbol{x}_{2}^{\prime}\right)^{\prime}$, where $\boldsymbol{x}_{1}$ and $\boldsymbol{x}_{2}$ are $p_{1}$ and $p_{2}$-dimensional vectors, respectively. Suppose now that we have $N_{1}$ independent observations on the full set of variables, $\boldsymbol{x}$, and $N_{2}$ independent observations on $\boldsymbol{x}_{1}$. We introduce some notation for the sample means and covariance matrices. Let $\overline{\boldsymbol{x}}^{(1)}$ denote the sample mean of $\boldsymbol{x}$ based on the $N_{1}$ observations, and $\overline{\boldsymbol{x}}^{(1)}=\left(\overline{\boldsymbol{x}}_{1}^{(1)^{\prime}}, \overline{\boldsymbol{x}}_{2}^{(1)^{\prime}}\right)^{\prime}, \overline{\boldsymbol{x}}_{i}^{(1)}: p_{i} \times 1, i=$ 1,2. Let further $\overline{\boldsymbol{x}}^{(2)}$ denote the $p_{1}$-dimensional sample mean vector for based on the $N_{2}$ observations. Throughout this paper, we use the letter $j$ only as running suffix for sample observations.

With above notations, the 2 -step monotone missing data scheme, described in Shutoh et al. (2011) can be presented by

$$
\boldsymbol{x}_{1}^{(1)}, \boldsymbol{x}_{2}^{(1)}, \ldots, \boldsymbol{x}_{N_{1}}^{(1)}, \boldsymbol{x}_{1}^{(2)}, \boldsymbol{x}_{2}^{(2)}, \ldots, \boldsymbol{x}_{N_{2}}^{(2)},
$$

where $\boldsymbol{x}_{j}^{(1)}\left(j=1, \ldots, N_{1}\right)$ denotes the $p$-dimensional sample vector and $\boldsymbol{x}_{j}^{(2)}(j=$
$\left.1, \ldots, N_{2}\right)$ denotes the $p_{1}$-dimensional sample vector. The graphical representation of this scheme is given in Figure 1.1.

## $\underline{\text { Please insert Figure } 1.1 \text { around here. }}$

Further the sample covariance matrices based on the $N_{1}$ and $N_{2}$ observations are expressed as

$$
S^{(1)}=\frac{1}{n_{1}} \sum_{j=1}^{N_{1}}\left(\boldsymbol{x}_{j}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)\left(\boldsymbol{x}_{j}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)^{\prime}, S^{(2)}=\frac{1}{n_{2}} \sum_{j=1}^{N_{2}}\left(\boldsymbol{x}_{j}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)\left(\boldsymbol{x}_{j}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)^{\prime},
$$

respectively, where $n_{i}=N_{i}-1, i=1,2$.
Let the partitions of $\boldsymbol{\mu}, \Sigma$ and $S^{(1)}$ corresponding to ones of $\boldsymbol{x}$ be

$$
\boldsymbol{\mu}=\binom{\boldsymbol{\mu}_{1}}{\boldsymbol{\mu}_{2}}, \quad \Sigma=\left(\begin{array}{cc}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{array}\right), \quad S^{(1)}=\left(\begin{array}{cc}
S_{11}^{(1)} & S_{12}^{(1)} \\
S_{21}^{(1)} & S_{22}^{(1)}
\end{array}\right) .
$$

respectively. Let $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$ denote the MLE of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$, respectively, and assume that $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$ can be partitioned in the same way as $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$. From Anderson and Olkin (1985), we can express the MLE's $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$ as follows

$$
\begin{aligned}
& \hat{\boldsymbol{\mu}}_{1}=\frac{1}{N}\left(N_{1} \overline{\boldsymbol{x}}_{1}^{(1)}+N_{2} \overline{\boldsymbol{x}}^{(2)}\right), \hat{\boldsymbol{\mu}}_{2}=\overline{\boldsymbol{x}}_{2}^{(1)}-\hat{\Sigma}_{21} \hat{\Sigma}_{11}^{-1}\left(\overline{\boldsymbol{x}}_{1}^{(1)}-\hat{\boldsymbol{\mu}}_{1}\right), \\
& \hat{\Sigma}_{11}=\frac{1}{N}\left(W_{11}^{(1)}+W^{(2)}\right), \hat{\Sigma}_{12}=\hat{\Sigma}_{11}\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}, \\
& \hat{\Sigma}_{22}=\frac{1}{N_{1}} W_{22 \cdot 1}^{(1)}+\hat{\Sigma}_{21} \hat{\Sigma}_{11}^{-1} \hat{\Sigma}_{12},
\end{aligned}
$$

where

$$
\begin{aligned}
& N=N_{1}+N_{2} \\
& W^{(1)}=n_{1} S^{(1)}, W^{(2)}=n_{2} S^{(2)}+\frac{N_{1} N_{2}}{N}\left(\overline{\boldsymbol{x}}_{1}^{(1)}-\overline{\boldsymbol{x}}^{(2)}\right)\left(\overline{\boldsymbol{x}}_{1}^{(1)}-\overline{\boldsymbol{x}}^{(2)}\right)^{\prime} \\
& W^{(1)}=\left(\begin{array}{ll}
W_{11}^{(1)} & W_{12}^{(1)} \\
W_{21}^{(1)} & W_{22}^{(1)}
\end{array}\right), W_{22 \cdot 1}^{(1)}=W_{22}^{(1)}-W_{21}^{(1)}\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)} .
\end{aligned}
$$

In Lemma 2.1 stated below, we propose two auxiliary unbiased estimators of $\Sigma$ under 2 -step monotone missing data.

Lemma 2.1. Let $\hat{\Sigma}_{1}$ and $\hat{\Sigma}_{2}$ be defined as

$$
\hat{\Sigma}_{1}=\left(\begin{array}{ll}
\hat{\Sigma}_{1,11} & \hat{\Sigma}_{1,12} \\
\hat{\Sigma}_{1,21} & \hat{\Sigma}_{1,22}
\end{array}\right), \hat{\Sigma}_{2}=\left(\begin{array}{cc}
\hat{\Sigma}_{2,11} & \hat{\Sigma}_{2,12} \\
\hat{\Sigma}_{2,21} & \hat{\Sigma}_{2,22}
\end{array}\right),
$$

where

$$
\begin{aligned}
& \hat{\Sigma}_{1,11}=\frac{1}{N-1}\left(W_{11}^{(1)}+W^{(2)}\right), \hat{\Sigma}_{1,12}=\hat{\Sigma}_{11}\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)} \\
& \hat{\Sigma}_{1,21}=\hat{\Sigma}_{1,12}^{\prime}, \hat{\Sigma}_{1,22}=b_{1} W_{22 \cdot 1}^{(1)}+\hat{\Sigma}_{21} \hat{\Sigma}^{-1} \hat{\Sigma}_{12} \\
& \hat{\Sigma}_{2,11}=\frac{1}{N-1}\left(W_{11}^{(1)}+W^{(2)}\right), \hat{\Sigma}_{2,12}=\frac{1}{N_{1}-1} W_{12}^{(1)} \\
& \hat{\Sigma}_{2,21}=\hat{\Sigma}_{2,12}^{\prime}, \hat{\Sigma}_{2,22}=\frac{1}{N_{1}-1} W_{22}^{(1)}
\end{aligned}
$$

and

$$
b_{1}=\frac{1}{N_{1}-p_{1}-1}\left(1-\frac{p_{1}}{N-1}-\frac{N_{2} p_{1}}{(N-1)\left(N_{1}-p_{1}-2\right)}\right)
$$

Then

$$
\mathrm{E}\left[\hat{\Sigma}_{1}\right]=\mathrm{E}\left[\hat{\Sigma}_{2}\right]=\Sigma
$$

Proof : See Appendix (A.2).
Due to the unbiasedness property, both estimators, $\hat{\Sigma}_{1}$ and $\hat{\Sigma}_{2}$ are expected to perform better than $S^{(1)}$ which is based on the complete data part only. The following lemma provides exact results on the relative performance accuracy of these three estimators in terms of expected quadratic loss.

Lemma 2.2. Let

$$
\beta_{0}=\frac{p}{n_{1}} a_{1}^{2}+\frac{1}{n_{1}} a_{2}
$$

where $a_{i}=\operatorname{tr} \Sigma^{i} / p$ and $\Sigma^{i}$ denotes $i$-th power of the matrix $\Sigma$ for $i=1,2$. Then,
(i) $\quad \mathrm{E}\left[\left\|S^{(1)}-\Sigma\right\|_{F}^{2}\right]=\beta_{0}$,
(ii) $\quad \mathrm{E}\left[\left\|\hat{\Sigma}_{1}-\Sigma\right\|_{F}^{2}\right]=\beta_{0}-m_{1}$,
(iii) $\quad \mathrm{E}\left[\left\|\hat{\Sigma}_{2}-\Sigma\right\|_{F}^{2}\right]=\beta_{0}-m_{2}$,
where $\|\cdot\|_{F}^{2}$ denotes the normalized Frobenious norm,

$$
\begin{aligned}
m_{1}= & \frac{N_{2}}{n n_{1}}\left\{p a_{1}^{2}+a_{2}-k_{1} \frac{\operatorname{tr} \Sigma_{22 \cdot 1}^{2}}{p}-k_{2} \frac{\left(\operatorname{tr} \Sigma_{22 \cdot 1}\right)^{2}}{p}-2 k_{3}\left(\frac{\operatorname{tr} \Sigma_{11} \operatorname{tr} \Sigma_{22 \cdot 1}}{p}\right.\right. \\
& \left.\left.+\frac{\operatorname{tr} \Sigma_{22 \cdot 1} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}}{p}+\frac{\operatorname{tr} \Sigma_{22 \cdot 1} \operatorname{tr} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}}{p}\right)\right\} \\
m_{2}= & \frac{N_{2}}{n n_{1}}\left(p a_{1}^{(11)^{2}}+a_{2}^{(11)}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
k_{1}= & \left(1-3 r_{1}+4 r_{1}^{2}-2 r_{1}^{3} r_{2}-\frac{4-11 r_{1}+6 r_{1}^{2} r_{2}}{n_{1}}+\frac{3-4 r_{1} r_{2}}{n_{1}^{2}}\right) \\
& \left\{\left(1-r_{1}\right)\left(1-r_{1}-\frac{1}{n_{1}}\right)\left(1-r_{1}-\frac{3}{n_{1}}\right)\right\}^{-1} \\
k_{2}= & \left(1-4 r_{1}+7 r_{1}^{2}-4 r_{1}^{3}-2 r_{1}^{3} r_{2}+2 r_{1}^{4} r_{2}\right. \\
& +\frac{8 r_{1}^{3} r_{2}-4 r_{1}^{2} r_{2}-15 r_{1}^{2}+16 r_{1}-5}{n_{1}}+\frac{8 r_{1}^{2} r_{2}-2 r_{1} r_{2}-12 r_{1}+7}{n_{1}^{2}} \\
& \left.+\frac{2 r_{1} r_{2}-3}{n_{1}^{3}}\right)\left\{\left(1-r_{1}\right)\left(1-r_{1}-\frac{1}{n_{1}}\right)^{2}\left(1-r_{1}-\frac{3}{n_{1}}\right)\right\}^{-1} \\
k_{3}= & \left(1-r_{1}-\frac{1}{n_{1}}\right)^{-1} \\
r_{1}= & \frac{p_{1}}{n_{1}}, r_{2}=\frac{n_{1}}{n}
\end{aligned}
$$

Proof : See Appendix (A.3).
It follows from (2.1)-(2.3) that $k_{i}=1+O\left(n^{-1}\right)$ for all $i$, assuming that $p$ is fixed and $n$ is relatively large. Then the following relationship between $m_{1}$ and $m_{2}$ holds

$$
\begin{aligned}
m_{2}= & m_{1}+\frac{N_{2}}{n n_{1}}\left(\frac{\operatorname{tr}\left(\Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right)^{2}}{p}+\frac{\Sigma_{21} \Sigma_{12}}{p}+\frac{\left(\operatorname{tr} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right)^{2}}{p}\right. \\
& \left.+\frac{\left(\operatorname{tr} \Sigma_{11} \operatorname{tr} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right)^{2}}{p}\right)+o\left(\frac{1}{n}\right)
\end{aligned}
$$

which implies that $\hat{\Sigma}_{1}$ is more accurate estimator than $\hat{\Sigma}_{2}$ in a large sample case. However, $\hat{\Sigma}_{1}$ will be worse than $S^{(1)}$ since $k_{1}, k_{2}$ and $k_{3}$ grow when $p_{1} / N_{1} \rightarrow 1$. On the other hand, since $\hat{\Sigma}_{2}$ does not depend on the relationship between $p_{1}$ and $N_{1}$, its accuracy is better than $S^{(1)}$. By this reason, it can be said that $\hat{\Sigma}_{2}$ is a flexibly accurate estimator.

## 3 The shrinkage estimator for high-dimensional data with 2 -step monotone missing values

On the complete samples, Ledoit and Wolf (2004) provide a shrinkage estimator for $\Sigma$ given by

$$
\hat{\Sigma}_{f}^{*}=\frac{\hat{\beta}_{f}}{\hat{\delta}_{f}} \hat{\mu}_{f} I+\frac{\hat{\alpha}_{f}}{\hat{\delta}_{f}} S^{(1)}
$$

where

$$
\hat{\alpha}_{f}=\hat{a}_{2}-\hat{a}_{1}^{2}, \hat{\beta}_{f}=\left(\frac{p}{n_{1}}\right) \hat{a}_{1}^{2}, \hat{\delta}_{f}=\hat{a}_{2}+\left(\frac{p}{n_{1}}-1\right) \hat{a}_{1}^{2}, \hat{\mu}_{f}=\hat{a}_{1}
$$

In this study, we extend this approach to the case of 2 -step monotone missing data using auxiliary estimators $\hat{\Sigma}_{1}$ and $\hat{\Sigma}_{2}$ derived in Section 2.

Ledoit and Wolf type estimator is derived by the linear combination $\Sigma^{*}=\rho_{1} I+ \rho_{2} \hat{\Sigma}_{b}$ of the identity matrix $I$ and the unbiased estimator $\hat{\Sigma}_{b}=\left(\hat{\Sigma}_{1}\right.$ or $\left.\hat{\Sigma}_{2}\right)$ whose expected quadratic loss is minimum. Observed that $\hat{\Sigma}^{*}=\hat{\Sigma}_{f}^{*}$ if $\hat{\Sigma}_{b}=S^{(1)}$. Following the technique of Ledoit and Wolf (2004), consider now the optimization problem

$$
\min _{\rho_{1}, \rho_{2}} \mathrm{E}\left[\left\|\Sigma^{*}-\Sigma\right\|_{F}^{2}\right] \text { s.t. } \Sigma^{*}=\rho_{1} I+\rho_{2} \hat{\Sigma}_{b}
$$

where the coefficients $\rho_{1}$ and $\rho_{2}$ are non-random. The solution of (3.1) is given by

$$
\Sigma^{*}=\frac{\beta}{\delta} \mu I+\frac{\alpha}{\delta} \hat{\Sigma}_{b}
$$

where $\mu=\operatorname{tr} \Sigma / p, \alpha=\|\Sigma-\mu I\|_{F}^{2}, \beta=\mathrm{E}\left[\left\|\hat{\Sigma}_{b}-\Sigma\right\|_{F}^{2}\right], \delta=\mathrm{E}\left[\left\|\hat{\Sigma}_{b}-\mu I\right\|_{F}^{2}\right]$. With this notations we obtain $\mu=a_{1}, \alpha=a_{2}-a_{1}^{2}$.

### 3.1 The suggested estimator based on $\hat{\Sigma}_{1}$

A crucial step of our estimation is to get the explicit expressions of $\mathrm{E}\left[\left\|\hat{\Sigma}_{1}-\Sigma\right\|_{F}^{2}\right]$ and $\mathrm{E}\left[\left\|\hat{\Sigma}_{1}-\mu I\right\|_{F}^{2}\right]$ in terms of $a_{i}$ and $a_{i}^{(22 \cdot 1)}$ which are functions of $\operatorname{tr} \Sigma_{22 \cdot 1}$. We consider the following conditions

$$
\begin{array}{ll}
\mathrm{C} 0: & n_{1}, n_{2}, p_{1}, p \rightarrow \infty, \frac{p_{1}}{n_{1}} \rightarrow c_{0} \in[0,1), \frac{p}{n_{i}} \rightarrow c_{i} \in(0, \infty), i=1,2 \\
\mathrm{C} 1: & 0<\lim _{p \rightarrow \infty} a_{i}=\lim _{p \rightarrow \infty} \operatorname{tr} \Sigma^{i} / p<\infty, i=1, \ldots, 4
\end{array}
$$

Using Lemma A.1, under the conditions C0 and C1,

$$
\mathrm{E}\left[\left\|\hat{\Sigma}_{1}-\Sigma\right\|_{F}^{2}\right]=\beta_{1}+o(1), \quad \mathrm{E}\left[\left\|\hat{\Sigma}_{1}-\mu I\right\|_{F}^{2}\right]=\delta_{1}+o(1)
$$

where

$$
\begin{aligned}
\beta_{1} & =\frac{p}{n_{1}} a_{1}^{2}-m_{1}^{*} \\
\delta_{1} & =a_{2}+\left(\frac{p}{n_{1}}-1\right) a_{1}^{2}-m_{1}^{*} \\
m_{1}^{*} & =m_{1}^{*}\left(a_{1}, a_{1}^{(22 \cdot 1)}\right)=\frac{N_{2} p}{n n_{1}}\left\{a_{1}^{2}-2 k_{3} a_{1}^{(22 \cdot 1)} a_{1}+\left(2 k_{3}-k_{2}\right) a_{1}^{(22 \cdot 1)^{2}}\right\}
\end{aligned}
$$

and $a_{1}^{(22 \cdot 1)}=\operatorname{tr} \Sigma_{22 \cdot 1} / p$. Thus, the asymptotically optimal linear combination of the identity matrix $I$ and $\hat{\Sigma}_{1}$ is given by

$$
\Sigma_{1}^{*}=\frac{\beta_{1}}{\delta_{1}} \mu I+\frac{\alpha}{\delta_{1}} \hat{\Sigma}_{1}
$$

Observe however that $\Sigma_{1}^{*}$ depends on unknown parameters. Therefore, the next step is to replace these parameters their consistent estimators, and show that the asymptotic properties of the resulting estimator are unchanged.

Under the conditions C 0 and C 1 , the consistent estimators of $\alpha$, $\beta_{1}$ and $\delta_{1}$ are given by

$$
\hat{\alpha}=\hat{a}_{2}-\hat{a}_{1}^{2}, \quad \hat{\beta}_{1}=\frac{p}{n_{1}} \hat{a}_{1}^{2}-\hat{m}_{1}^{*}, \quad \hat{\delta}_{1}=\left(p / n_{1}-1\right) \hat{a}_{1}^{2}+\hat{a}_{2}-\hat{m}_{1}^{*}
$$

where $\hat{m}_{1}^{*}=m_{1}^{*}\left(\hat{a}_{1}, \hat{a}_{1}^{(22 \cdot 1)}\right)$, and $\hat{a}_{1}, \hat{a}_{2}$ and $\hat{a}_{1}^{(22 \cdot 1)}$ are consistent estimators of the corresponding parameters

$$
\begin{aligned}
& \hat{a}_{1}=\frac{\operatorname{tr} S^{(1)}}{p}, \hat{a}_{2}=\frac{n_{1}^{2}}{\left(n_{1}-1\right)\left(n_{1}+2\right)}\left(\frac{\operatorname{tr} S^{(1)^{2}}}{p}-\frac{\left(\operatorname{tr} S^{(1)}\right)^{2}}{n_{1} p}\right) \\
& \hat{a}_{1}^{(22 \cdot 1)}=\frac{n_{1} \operatorname{tr} S_{22 \cdot 1}^{(1)}}{\left(n_{1}-p_{1}\right) p}
\end{aligned}
$$

Now, by combining (3.2) and (3.3), we define the our estimator as

$$
\hat{\Sigma}_{1}^{*}=\frac{\hat{\beta}_{1}}{\hat{\delta}_{1}} \hat{\mu} I+\frac{\hat{\alpha}}{\hat{\delta}_{1}} \hat{\Sigma}_{1}
$$

One can see that $\hat{\Sigma}_{1}^{*}$ has the same asymptotic properties as $\Sigma_{1}^{*}:\left\|\hat{\Sigma}_{1}^{*}-\Sigma_{1}^{*}\right\|_{F}^{2} \xrightarrow{P} 0$ and $\mathrm{E}\left[\left\|\hat{\Sigma}_{1}^{*}-\Sigma\right\|_{F}^{2}\right] \rightarrow \mathrm{E}\left[\left\|\Sigma^{*}-\Sigma\right\|_{F}^{2}\right]$ under conditions C 0 and C 1 .

Consider further the relationship between $\hat{\Sigma}_{1}^{*}$ and $\hat{\Sigma}_{f}^{*}$ by Ledoit and Wolf (2004) when using complete data part only. The following proposition provides conditions for the estimator $\hat{\Sigma}_{f}^{*}$ to dominate $\hat{\Sigma}_{f}^{*}$ under the expected quadratic loss.

Proposition 3.1. Under the conditions $C 1$ and $n_{1}, n_{2}, p_{1}, p \rightarrow \infty$ with $p_{1} / n_{1} \rightarrow 0$, $p / n_{i} \rightarrow c_{i} \in(0, \infty), i=1,2$ and $n_{i} /\left(n_{1}+n_{2}\right) \rightarrow c_{i} \in(0,1), i=3,4$

$$
\mathrm{E}\left[\left\|\hat{\Sigma}_{f}^{*}-\Sigma\right\|_{F}^{2}\right]-\mathrm{E}\left[\left\|\hat{\Sigma}_{1}^{*}-\Sigma\right\|_{F}^{2}\right] \rightarrow \frac{c_{1} c_{4} \alpha}{\delta_{0} \delta_{1}}\left(a_{1}^{2}-a_{1}^{(22 \cdot 1)}\right)^{2} .
$$

Proof : See Appendix (A.4).

### 3.2 The suggested estimator based on $\hat{\Sigma}_{2}$

The dominance property of $\hat{\Sigma}_{1}^{*}$ over $\hat{\Sigma}_{f}^{*}$ follows from the condition $p_{1} / n_{1} \rightarrow 0$, which is very strong. Furthermore, if $p_{1}>n_{1}, \hat{\Sigma}_{1}^{*}$ is not applicable due to singularity of $\hat{\Sigma}_{1}$. In this subsection, we get another condition for the estimator of $\Sigma$ to dominate $\hat{\Sigma}_{f}^{*}$ in the case of $p_{1}>n_{1}$. Using the technique of subsection 3.1 and by considering

$$
\mathrm{C} 3: \quad n_{1}, n_{2}, p_{1}, p \rightarrow \infty, \frac{p_{1}}{n_{1}} \rightarrow c_{0} \in[0, \infty), \frac{p}{n_{i}} \rightarrow c_{i} \in(0, \infty), i=1,2, ~ r=c_{i} \in(0,1), i=3,4, ~ y n k l\left(n_{1}+n_{2}\right) \rightarrow c_{i}=4
$$

we obtain

$$
\mathrm{E}\left[\left\|\hat{\Sigma}_{2}-\Sigma\right\|_{F}^{2}\right]=\beta_{2}+o(1), \quad \mathrm{E}\left[\left\|\hat{\Sigma}_{2}-\mu I\right\|_{F}^{2}\right]=\delta_{2}+o(1),
$$

where

$$
\beta_{2}=\frac{p}{n_{1}} a_{1}^{2}-m_{2}^{*}, \delta_{2}=a_{2}+\left(\frac{p}{n_{1}}-1\right) a_{1}^{2}-m_{2}^{*}, m_{2}^{*}=m_{2}^{*}\left(a_{1}^{(11)}\right)=\frac{N_{2} p}{n n_{1}} a_{1}^{(11)^{2}}
$$

and $a_{1}^{(11)}=\operatorname{tr} \Sigma_{11} / p$. Observe that C3 presents more flexible asymptotic framework than C 0 . Now, the asymptotically optimal linear combination of the identity matrix $I$ and $\hat{\Sigma}_{2}$ is given by

$$
\Sigma_{2}^{*}=\frac{\beta_{2}}{\delta_{2}} \mu I+\frac{\alpha}{\delta_{2}} \hat{\Sigma}_{2}
$$

Of this, we propose our estimator of the form

$$
\hat{\Sigma}_{2}^{*}=\frac{\hat{\beta}_{2}}{\hat{\delta}_{2}} \hat{\mu} I+\frac{\hat{\alpha}}{\hat{\delta}_{2}} \hat{\Sigma}_{2}
$$

where

$$
\hat{\alpha}=\hat{a}_{2}-\hat{a}_{1}^{2}, \hat{\beta}_{2}=\frac{p}{n_{1}} \hat{a}_{1}^{2}-m_{2}^{*}\left(\hat{a}_{1}^{(11)}\right), \hat{\delta}_{2}=\left(p / n_{1}-1\right) \hat{a}_{1}^{2}+\hat{a}_{2}-m_{2}^{*}\left(\hat{a}_{1}^{(11)}\right)
$$

and $\hat{a}_{1}^{(11)}=\operatorname{tr} S_{11}^{(1)} / p$.
By the same arguments as in subsection 3.1, $\Sigma_{2}^{*}$ and $\hat{\Sigma}_{2}^{*}$ have the same asymptotic properties because $\left\|\hat{\Sigma}_{2}^{*}-\Sigma_{2}^{*}\right\|_{F}^{2} \xrightarrow{P} 0$ and $\mathrm{E}\left[\left\|\hat{\Sigma}_{2}^{*}-\Sigma\right\|_{F}^{2}\right] \rightarrow \mathrm{E}\left[\left\|\Sigma_{2}^{*}-\Sigma\right\|_{F}^{2}\right]$ under conditions C1 and C3.

The dominance property of $\hat{\Sigma}_{2}^{*}$ over $\hat{\Sigma}_{f}^{*}$ follows from the following proposition.

Proposition 3.2. Under the conditions C1 and C3,

$$
\mathrm{E}\left[\left\|\hat{\Sigma}_{f}^{*}-\Sigma\right\|_{F}^{2}\right]-\mathrm{E}\left[\left\|\hat{\Sigma}_{2}^{*}-\Sigma\right\|_{F}^{2}\right] \rightarrow \frac{c_{1} c_{4} \alpha}{\delta_{0} \delta_{2}} a_{1}^{(11)^{2}}
$$

Proof : The proof of this proposition which we omit, is straightforward application of the technique derived in Appendix (A.4).

## 4 Numerical results

Using Monte Carlo simulations, we compare performance of our new estimators $\hat{\Sigma}_{1}^{*}$ and $\hat{\Sigma}_{2}^{*}$ to the shrinkage estimator by Ledoit and Wolf (2004).

The simulation experiment is planned as follows. The data are generated from the normal model with zero mean vector and covariance matrix

$$
\Sigma=\operatorname{diag}\left(\sigma_{1}, \sigma_{2}, \ldots, \sigma_{p}\right)\left(\rho^{|i-j|}\right) \operatorname{diag}\left(\sigma_{1}, \sigma_{2}, \ldots, \sigma_{p}\right)
$$

where $\sigma_{i}$ is a random variable following continuous uniform distribution on the interval $(0,5)$. For all simulations we assume $N_{1}=N_{2}$ for convenience. We set $p=100,150,200$, and for each one consider three different values of $\rho=0.2,0.5,0.8$ to vary the covariance parameters.

The first setting represents the case when missing part of the data asymptotically exceeds the complete part. We fix $p_{1}=10$, the size of complete part, and assume that $N_{1}=N_{2}=50$. This implies that $p_{2}$, the dimension of the missing part grows with $p$.

In the second setting, we vary the proportion of the data that are missing. To put it more precisely, for each $p=100,150,200$, we set $p_{1}=[q \times p]$, for $q=0.5,0.7,0.9$, and

$$
\Sigma=\operatorname{diag}\left(\sigma_{1}, \sigma_{2}, \ldots, \sigma_{p}\right)\left(0.8^{|i-j|}\right) \operatorname{diag}\left(\sigma_{1}, \sigma_{2}, \ldots, \sigma_{p}\right)
$$

where $\sigma_{i}$ is a random variable having continuous uniform distribution on the interval $(0,5)$. Here, $[a]$ denotes the integer part of $a$.

Within the first setting, three following estimators are evaluated: $\hat{\Sigma}_{f}^{*}, \hat{\Sigma}_{1}^{*}, \hat{\Sigma}_{2}^{*}$, whereas in the second setting we only focus on $\hat{\Sigma}_{f}^{*}$ and $\hat{\Sigma}_{2}^{*}$.

To evaluate performance accuracy we use the loss function based on normalized Frobenius norm, $\mathcal{L}(\Sigma, \Delta)=\|\Delta-\Sigma\|_{F}^{2}$, and define the risk function as the expected loss, $R(\Sigma, \Delta)=\mathrm{E}[\mathcal{L}(\Sigma, \Delta)]$, when estimating $\Sigma$ by $\Delta$. We asses the relative risk rate as follows

$$
R R(\Delta)=R(\Sigma, \Delta) / R\left(\Sigma, S^{(1)}\right)
$$

where $S^{(1)}$ is used reference estimator for all comparisons. For all the settings, the value of $R R$ is computed by 100,000 replications.

Tables 4.1-4.3 report the risk rates for all three estimators in the for the first setting, and figures 4.1-4.3 plot the risk rates for $\hat{\Sigma}_{f}^{*}$ and $\hat{\Sigma}_{2}^{*}$ as functions of $p$ for the second setting.

Overview through the simulation results reveals that our new estimators provide significant improvements over $\hat{\Sigma}_{f}^{*}$ for both types of missing scenarios. Although $R R$ s of $\hat{\Sigma}_{1}^{*}$ and $\hat{\Sigma}_{2}^{*}$ are very close to each other for all $\rho, \hat{\Sigma}_{2}^{*}$ dominates $\hat{\Sigma}_{1}^{*}$ in the case when missing part grows. As expected, $\hat{\Sigma}_{2}^{*}$ yields substantial improvement over $\hat{\Sigma}_{f}^{*}$ even in the case of fixed missing part. It could be observed that both estimators are sensitive to the size of $\rho \in(0,1)$ which is naturally expected in a $\operatorname{AR}(1)$ model.

In conclusion, both suggested estimators, $\hat{\Sigma}_{1}^{*}$ and $\hat{\Sigma}_{2}^{*}$ are shown to have dominance properties over $\hat{\Sigma}_{f}^{*}$ in high-dimensional normal model with 2 -step monotone missing data.

Please insert Tables 4.1-4.3 and Figures 4.1-4.3 around here.

## 5 Conclusion

This paper provided the estimators for $\Sigma$ in the case of 2 -step monotone missing data with high-dimensional setting by extending Ledoit and Wolf's (2004) estimator. The result provided a solution to the problem such that the existing MLE on the basis of 2-step monotone missing data is not also applicable in the case of high-dimensional setting. Further, it could be observed that our estimators were superior to Ledoit and Wolf's (2004) estimator in view of the relative risk rate for the performed simulations. In the future, we may also derive the theoretical results of the procedures with our estimators which are applicable to the high-dimensional and missing data.

## Appendix

To prove propositions 2.1 and 2.2 we need two additional lemmas stated below. For these proofs we need the some preliminary results formulated in Lemma A. 1 and Lemma A.2.

## A. 1 Preliminary results

Lemma 5.1. Suppose that $A$ follows Wishart distribution $W_{p}(\Sigma, n)$, where $A$ admits the similar partition as that of $\Sigma$ in Section 2, and let $A_{22 \cdot 1}=A_{22}-A_{21} A_{11}^{-1} A_{12}$. Then
(i) $\quad A_{22 \cdot 1} \sim W_{p}\left(\Sigma_{22 \cdot 1}, n-p_{1}\right)$, and $A_{22 \cdot 1}$ is independent of $A_{11}$ and $A_{12}$,
(ii) $\quad A_{12} \mid A_{11} \sim N_{p_{1} \times p_{2}}\left(V e c\left(A_{11} \Sigma_{11}^{-1} \Sigma_{12}\right), \Sigma_{22 \cdot 1} \otimes A_{11}\right)$

Proof. For the proof, see Muirhead (1982) and Siotani et al. (1985).
Now we state Lemma A.2.

Lemma 5.2. For $\hat{\Sigma}_{1}$ defined in Section 2, it holds that

$$
\begin{aligned}
\mathrm{E}\left[\operatorname{tr} \hat{\Sigma}_{1}^{2}\right]= & \frac{n_{1}+1}{n_{1}} \operatorname{tr} \Sigma^{2}+\frac{1}{n_{1}}(\operatorname{tr} \Sigma)^{2}-\frac{N_{2}}{n n_{1}}\left\{\operatorname{tr} \Sigma^{2}+(\operatorname{tr} \Sigma)^{2}-k_{1} \operatorname{tr} \Sigma_{22 \cdot 1}^{2}\right. \\
& -k_{2}\left(\operatorname{tr} \Sigma_{22 \cdot 1}\right)^{2}-2 k_{3}\left(\operatorname{tr} \Sigma_{22 \cdot 1} \operatorname{tr} \Sigma_{11}+\operatorname{tr} \Sigma_{22} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right. \\
& \left.+\operatorname{tr} \Sigma_{22} \operatorname{tr} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right\}
\end{aligned}
$$

where $k_{i}, i=1,2,3$ is defined in Lemma 2.2.

Proof. Using the following expression

$$
\mathrm{E}\left[\operatorname{tr} \hat{\Sigma}_{1}^{2}\right]=\mathrm{E}\left[\operatorname{tr}\left(\hat{\Sigma}_{1,11}^{2}+\hat{\Sigma}_{1,12} \hat{\Sigma}_{1,21}\right)\right]+\mathrm{E}\left[\operatorname{tr}\left(\hat{\Sigma}_{1,22}^{2}+\hat{\Sigma}_{1,21} \hat{\Sigma}_{1,12}\right)\right]
$$

and the results of Lemma A.1, we obtain

$$
\begin{aligned}
\mathrm{E}\left[\operatorname{tr}\left(\hat{\Sigma}_{1,11}^{2}+\hat{\Sigma}_{1,12} \hat{\Sigma}_{1,21}\right)\right]= & \frac{n+1}{n} \operatorname{tr}\left(\Sigma_{11}^{2}+\Sigma_{12} \Sigma_{21}\right)+\frac{1}{n} \operatorname{tr} \Sigma \operatorname{tr} \Sigma_{11} \\
& +\frac{N_{2}}{n\left(n_{1}-p_{1}-1\right)} \operatorname{tr} \Sigma_{22 \cdot 1} \operatorname{tr} \Sigma_{11}
\end{aligned}
$$

For the second term in (A.1) we get

$$
\begin{aligned}
\mathrm{E}\left[\operatorname{tr}\left(\hat{\Sigma}_{1,22}^{2}+\hat{\Sigma}_{1,21} \hat{\Sigma}_{1,12}\right)\right]= & \frac{1}{n^{2}} \mathrm{E}\left[\operatorname{tr} \hat{\Psi}_{21} W_{11}^{2} \hat{\Psi}_{12}\right]+b_{1}^{2} \mathrm{E}\left[\operatorname{tr} W_{22 \cdot 1}^{(1)^{2}}\right] \\
& +\frac{b_{1}}{n} \mathrm{E}\left[\operatorname{tr} \hat{\Psi}_{21} W_{11} \hat{\Psi}_{12} W_{22 \cdot 1}^{(1)}\right] \\
& +\frac{b_{1}}{n} \mathrm{E}\left[\operatorname{tr} W_{22 \cdot 1}^{(1)} \hat{\Psi}_{21} W_{11} \hat{\Psi}_{12}\right] \\
& +\frac{1}{n^{2}} \mathrm{E}\left[\operatorname{tr} \hat{\Psi}_{21} W_{11} \hat{\Psi}_{12} \hat{\Psi}_{21} W_{11} \hat{\Psi}_{12}\right]
\end{aligned}
$$

where $\hat{\Psi}_{21}=W_{21}^{(1)}\left(W_{11}^{(1)}\right)^{-1}$. From Lemma A.1,

$$
\begin{aligned}
\mathrm{E}\left[\operatorname{tr} \hat{\Psi}_{21} W_{11}^{2} \hat{\Psi}_{12}\right]= & n(n+1) \operatorname{tr} \Sigma_{21} \Sigma_{12}+n\left(\operatorname{tr} \Sigma_{11} \operatorname{tr} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right. \\
& \left.+\operatorname{tr} \Sigma_{22 \cdot 1} \operatorname{tr} \Sigma_{11}\right)+\frac{n N_{2}}{\left(n-p_{1}-1\right)} \operatorname{tr} \Sigma_{11} \operatorname{tr} \Sigma_{22 \cdot 1} \\
\mathrm{E}\left[\operatorname{tr} W_{22 \cdot 1}^{(1)^{2}}\right]= & \left(n_{1}-p_{1}\right)\left(n_{1}-p_{1}-1\right) \operatorname{tr} \Sigma_{22 \cdot 1}^{2} \\
& +\left(n_{1}-p_{1}\right)\left(\operatorname{tr} \Sigma_{22 \cdot 1}\right)^{2} \\
\mathrm{E}\left[\operatorname{tr} \hat{\Psi}_{21} W_{11} \hat{\Psi}_{12} W_{22 \cdot 1}^{(1)}\right]= & \left(n_{1}-p_{1}\right) p_{1}\left(1+\frac{N_{2}}{n_{1}-p_{1}-1}\right) \operatorname{tr} \Sigma_{22 \cdot 1}^{2} \\
& \left.+n\left(n_{1}-p_{1}\right) \operatorname{tr} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12} \Sigma_{22 \cdot 1}\right\} \\
\mathrm{E}\left[\operatorname{tr}\left(\hat{\Psi}_{21} W_{11} \hat{\Psi}_{12}\right)^{2}\right]= & \left\{p_{1}^{2}+\frac{2 p_{1}^{2} N_{2}}{n_{1}-p_{1}-1}+c_{1}\left(2 N_{2} p_{1}+N_{2}^{2} p_{1}^{2}\right)\right. \\
& \left.+2 c_{2}\left(N_{2} p_{1}+N_{2} p_{1}^{2}+N_{2}^{2} p_{1}\right)\right\} \operatorname{tr} \Sigma_{22 \cdot 1}^{2} \\
& +\left\{p_{1}+\frac{2 p_{1} N_{2}}{n_{1}-p_{1}-1}+c_{2}\left(2 N_{2} p_{1}+N_{2}^{2} p_{1}^{2}\right)\right. \\
& \left.+c_{2}\left(n_{1}-p_{1}-1\right)\left(N_{2} p_{1}+N_{2}^{2} p_{1}+N_{2} p_{1}^{2}\right)\right\} \\
& +\left\{\operatorname{tr} \Sigma_{22 \cdot 1}^{2}+\left(\operatorname{tr} \Sigma_{22 \cdot 1}\right)^{2}\right\}+2\left(n+N_{2}\right. \\
& \left.+\frac{N_{2}^{2}+N_{2} p_{1}+N_{2}}{n_{1}-p_{1}-1}\right) \operatorname{tr} \Sigma_{22 \cdot 1} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12} \\
& +2 n p_{1}\left(1+\frac{N_{2}}{n_{1}-p_{1}-1}\right) \operatorname{tr} \Sigma_{22 \cdot 1} \operatorname{tr} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12} \\
& +\left(n^{2}+n\right) \operatorname{tr}\left(\Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right)^{2} \\
& +n\left(\operatorname{tr} \Sigma_{21} \Sigma_{11}^{-1} \Sigma_{12}\right)^{2}
\end{aligned}
$$

Substituting (A.4)-(A.6) into (A.3), the proof of Lemma A. 1 is complete.

## A. 2 Proof of Lemma 2.1

Using the moment properties of the Wishart distribution and applying Lemma A.1, we get

$$
\begin{aligned}
\mathrm{E}\left[\hat{\Sigma}_{1,11}\right]= & \mathrm{E}\left[\frac{1}{N-1}\left(W_{11}^{(1)}+W^{(2)}\right)\right] \\
= & \frac{1}{N-1}\left\{\left(N_{1}-1\right) \Sigma_{11}+N_{2} \Sigma_{11}\right\} \\
= & \Sigma_{11} \\
\mathrm{E}\left[\hat{\Sigma}_{1,12}\right]= & \frac{1}{N-1} \mathrm{E}\left[\left(W_{11}^{(1)}+W^{(2)}\right)\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}\right] \\
= & \frac{1}{N-1} \mathrm{E}\left[W_{12}^{(1)}+W^{(2)}\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}\right] \\
= & \frac{1}{N-1}\left\{\left(N_{1}-1\right) \Sigma_{12}+N_{2} \Sigma_{12}\right\} \\
= & \Sigma_{12}, \\
\mathrm{E}\left[\hat{\Sigma}_{1,22}\right]= & \frac{1}{N_{1}-p_{1}-1}\left(1-\frac{p_{1}}{N-1}-\frac{N_{2} p_{1}}{(N-1)\left(N_{1}-p_{1}-2\right)}\right) \mathrm{E}\left[W_{22 \cdot 1}^{(1)}\right] \\
& +\frac{1}{N-1} \mathrm{E}\left[W_{21}^{(1)}\left(W_{11}^{(1)}\right)^{-1}\left(W_{11}^{(1)}+W^{(2)}\right)\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}\right] .
\end{aligned}
$$

Then, for the first term of (A.9) we have

$$
\begin{aligned}
& \frac{1}{N_{1}-p_{1}-1}\left(1-\frac{p_{1}}{N-1}-\frac{N_{2} p_{1}}{(N-1)\left(N_{1}-p_{1}-2\right)}\right) \mathrm{E}\left[W_{22 \cdot 1}^{(1)}\right] \\
& \quad=\left(1-\frac{p_{1}}{N-1}-\frac{N_{2} p_{1}}{(N-1)\left(N_{1}-p_{1}-2\right)}\right) \Sigma_{22 \cdot 1}
\end{aligned}
$$

For the second term of (A.9) we obtain

$$
\begin{aligned}
& \frac{1}{N-1} \mathrm{E}\left[W_{21}^{(1)}\left(W_{11}^{(1)}\right)^{-1}\left(W_{11}^{(1)}+W^{(2)}\right)\left(W_{11}^{(1)}\right)^{-1} W_{12}^{(1)}\right] \\
& \quad=\Sigma_{22}-\left(1-\frac{p_{1}}{N-1}-\frac{N_{2} p_{1}}{(N-1)\left(N_{1}-p_{1}-2\right)}\right) \Sigma_{22 \cdot 1}
\end{aligned}
$$

Substituting (A.10) and (A.11) into (A.9), we have

$$
\mathrm{E}\left[\hat{\Sigma}_{1,22}\right]=\Sigma_{22} .
$$

Combining (A.7), (A.8) and (A.12), we get $\mathrm{E}\left[\hat{\Sigma}_{1}\right]=\Sigma$.
The unbiasedness of $\hat{\Sigma}_{2}$ is easily shown by calculating the first moment of the Wishart matrices $W^{(1)}$ and $W^{(2)}$.

## A. 3 Proof of Lemma 2.2

The result in (i) is established in (see, e.g., Ledoit and Wolf (2004)). To show (ii) we first express it as

$$
\mathrm{E}\left[\left\|\hat{\Sigma}_{1}-\Sigma\right\|_{F}^{2}\right]=\mathrm{E}\left[\operatorname{tr} \hat{\Sigma}_{1}^{2}\right] / p-a_{2} .
$$

By using Lemma A.2, we can calculate $\mathrm{E}\left[\operatorname{tr} \hat{\Sigma}_{1}^{2}\right]$, which gives the statement (ii). It should be noted that (i) is shown assuming that $N_{2}=0$. Finaly, we give the proof of (iii), by first expressing

$$
\mathrm{E}\left[\left\|\hat{\Sigma}_{2}-\Sigma\right\|_{F}^{2}\right]=\mathrm{E}\left[\operatorname{tr} \hat{\Sigma}_{2}^{2}\right] / p-a_{2}
$$

and using the decomposition of $\hat{\Sigma}_{2}$ as

$$
\left(\begin{array}{cc}
\frac{n_{1}}{n} S_{11}^{(1)}+\frac{N_{2}}{n} S^{(2)} & S_{12}^{(1)} \\
S_{21}^{(1)} & S_{22}^{(1)}
\end{array}\right)
$$

Then

$$
\begin{aligned}
\frac{1}{p} \mathrm{E}\left[\operatorname{tr} \hat{\Sigma}_{2}^{2}\right]= & \frac{1}{p}\left\{\mathrm{E}\left[\operatorname{tr}\left(\frac{n_{1}}{n} S_{11}^{(1)}+\frac{N_{2}}{n} S^{(2)}\right)^{2}\right]+2 \mathrm{E}\left[\operatorname{tr} S_{12}^{(1)} S_{21}^{(1)}\right]\right. \\
& \left.+\mathrm{E}\left[\operatorname{tr} S_{22}^{(1)^{2}}\right]\right\} \\
= & \frac{1}{p}\left\{\frac{n_{1}+1}{n_{1}} \operatorname{tr} \Sigma^{2}+\frac{1}{n_{1}}(\operatorname{tr} \Sigma)^{2}\right\}-\frac{N_{2} p}{n n_{1}}\left\{\operatorname{tr} \Sigma_{11}^{2}+\left(\operatorname{tr} \Sigma_{11}\right)^{2}\right\}
\end{aligned}
$$

Substituting (A.14) into (A.13), we obtain (iii). It should be noted that (i) is shown assuming that $N_{2}=0$.

## A. 4 Proof of Proposition 3.1

Under the conditions C1 and assuming that $n_{1}, n_{2}, p_{1}, p \rightarrow \infty$ with $p_{1} / n_{1} \rightarrow 0$ and $p / n_{i} \rightarrow c_{i} \in(0, \infty), i=1,2$,

$$
\mathrm{E}\left[\left\|\hat{\Sigma}_{1}^{*}-\Sigma\right\|_{F}^{2}\right] \rightarrow \frac{\alpha \beta_{1}}{\delta_{1}} \text { and } \mathrm{E}\left[\left\|\hat{\Sigma}_{f}^{*}-\Sigma\right\|_{F}^{2}\right] \rightarrow \frac{\alpha \beta_{0}}{\delta_{0}}
$$

where $\delta_{0}=\alpha+\beta_{0}$. By using the continuous mapping theorem and (A.15), we obtain

$$
\mathrm{E}\left[\left\|\hat{\Sigma}_{f}^{*}-\Sigma\right\|_{F}^{2}\right]-\mathrm{E}\left[\left\|\hat{\Sigma}_{1}^{*}-\Sigma\right\|_{F}^{2}\right] \rightarrow \frac{\alpha \beta_{0}}{\delta_{0}}-\frac{\alpha \beta_{1}}{\delta_{1}} .
$$

On the other hand, under the same assumptions as above,

$$
\frac{\alpha \beta_{0}}{\delta_{0}}-\frac{\alpha \beta_{1}}{\delta_{1}}=\frac{\alpha}{\delta_{0} \delta_{1}}\left(\beta_{0}-\beta_{1}\right)=\frac{\alpha}{\delta_{0} \delta_{1}} m_{1} \rightarrow \frac{N_{2} p \alpha}{n n_{1} \delta_{0} \delta_{1}}\left(a_{1}^{2}-a_{1}^{(22 \cdot 1)}\right)^{2} .
$$

Combining (A.16) and (A.17), Proposition 3.1 follows.

## Acknowledgments

The authors would like to extend their sincere gratitude to the referee who gave invaluable comments and suggestions, which have greatly enhanced this paper. Any remaining errors are the authors' responsibility. This research was in part supported by grants from the Forum for Asian Studies (4440101-2010), Stockholm University, Sweden. M.Hyodo's research was in part supported by Grant-in-Aid for JSPS Fellow (23-9731). T. Seo's research was in part supported by Grant-in-Aid for Scientific Research (C) (23500360). T. Pavlenko's research was in part supported by grants from Swedish Research Council (421-2008-1966).

## References

Anderson, T. W. (1957). Maximum likelihood estimates for multivariate normal distribution when some observations are missing. Journal of the American Statistical Association, 52, 200-203.

Anderson, T.W. and Olkin, I. (1985). Maximum likelihood estimation of the parameters of multivariate normal distribution. Linear Algebra and Its Applications, 70, 147-171.

Bhargava, R. P. (1975). Some one-sample hypothesis testing problems when there is monotone sample from a multivariate normal population. Annals of the Institute of Statistical Mathematics, 27, 327-339.

Fujikoshi, Y. and Seo, T. (1998). Asymptotic approximations for EPMC's of the linear and the quadratic discriminant function when the sample size and the dimension are large. Random Operators and Stochastic Equations, 6, 269-280.

Jinadasa, K. G. and Tracy, D. S. (1992). Maximum likelihood estimation for multivariate normal distribution with monotone sample. Communications in Statistics A, Theory and Methods, 21, 41-50.

Kanda, T. and Fujikoshi, Y. (1998). Some basic properties of the MLE's for a multivariate normal distribution with monotone missing data. American Journal of Mathematical and Management Sciences, 18, 161-190.

Kubokawa, T. and Srivastava, M. S. (2008). Estimation of the precision matrix of a singular Wishart distribution and its application in high-dimensional data. Journal of Multivariate Analysis, 99, 1906-1928.

Little, R. J. A. and Rubin, D. R. (1987). Statistical Analysis with Missing Data, Wiley, New York.

Ledoit, O. and Wolf, M. (2004). A well-conditioned estimator for large dimensional covariance matrices. Journal of Multivariate Analysis, 88, 365-411.

Muirhead, R. J. (1982). Aspects of multivariate statistical theory, Wiley, New York.

Shutoh, N., Hyodo, M. and Seo, T. (2011). An asymptotic approximation for EPMC in linear discriminant analysis based on two-step monotone missing samples. Journal of Multivariate Analysis, 102, 252-263.

Siotani, M., Hayakawa, T. and Fujikoshi, Y. (1985). Modern Multivariate Statistical Analysis, A Graduate Course and Handbook. Ohio:American Science Press.

Table 4.1: The risk rates when $\rho=0.2$
|  | $p=100$ | $p=150$ | $p=200$ |
| :---: | :--- | :--- | :--- |
| $R R\left(\hat{\Sigma}_{f}^{*}\right)$ | 0.1968 | 0.1347 | 0.1050 |
| $R R\left(\hat{\Sigma}_{1}^{*}\right)$ | 0.1946 | 0.1336 | 0.1044 |
| $R R\left(\hat{\Sigma}_{2}^{*}\right)$ | 0.1942 | 0.1336 | 0.1044 |


Table 4.2: The risk rates when $\rho=0.5$
|  | $p=100$ | $p=150$ | $p=200$ |
| :---: | :--- | :--- | :--- |
| $R R\left(\hat{\Sigma}_{f}^{*}\right)$ | 0.3392 | 0.2550 | 0.2161 |
| $R R\left(\hat{\Sigma}_{1}^{*}\right)$ | 0.3319 | 0.2511 | 0.2135 |
| $R R\left(\hat{\Sigma}_{2}^{*}\right)$ | 0.3309 | 0.2507 | 0.2134 |


Table 4.3: The risk rates when $\rho=0.8$
|  | $p=100$ | $p=150$ | $p=200$ |
| :---: | :--- | :--- | :--- |
| $R R\left(\hat{\Sigma}_{f}^{*}\right)$ | 0.6821 | 0.5826 | 0.5039 |
| $R R\left(\hat{\Sigma}_{1}^{*}\right)$ | 0.6574 | 0.5634 | 0.4895 |
| $R R\left(\hat{\Sigma}_{2}^{*}\right)$ | 0.6508 | 0.5625 | 0.4890 |


![](https://cdn.mathpix.com/cropped/7529ca39-054e-4b47-afbd-1a3a0997635f-20.jpg?height=346&width=862&top_left_y=296&top_left_x=566)
Figure 1.1: 2 -step monotone missing data

$R R(\Delta)$ plotted as a function of the number of variables for $\Delta=\hat{\Sigma}_{f}^{*}($ solid $)$ and $\Delta=\hat{\Sigma}_{2}^{*}($ dashed $)$.

![](https://cdn.mathpix.com/cropped/7529ca39-054e-4b47-afbd-1a3a0997635f-20.jpg?height=259&width=435&top_left_y=1169&top_left_x=315)
Fig.4.1. $q=0.5$.

![](https://cdn.mathpix.com/cropped/7529ca39-054e-4b47-afbd-1a3a0997635f-20.jpg?height=259&width=433&top_left_y=1169&top_left_x=760)
Fig.4.2. $q=0.7$.

![](https://cdn.mathpix.com/cropped/7529ca39-054e-4b47-afbd-1a3a0997635f-20.jpg?height=259&width=441&top_left_y=1169&top_left_x=1197)
Fig.4.3. $q=0.9$.


[^0]:    Mathematics Subject Classification 62H12; 62F12.

