---
citekey: cordeiroBiasCorrectionARMA1994
item_type: article
authors: 'Cordeiro, Gauss M. and Klein, Ruben'
year: 1994
title: 'Bias Correction in {ARMA} Models'
venue: 'Statistics \& Probability Letters'
volume: 19
issue: 3
pages: 169--176
doi: 10.1016/0167-7152(94)90100-7
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\cordeiro_bias_correction_arma_1994.pdf'
pdf_sha256: f0df23cfd97d996a44c4c003e75fc73b7103dc04ede986631bd15aa14e86f02a
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-01T23:14:22Z
---
# Bias correction in ARMA models 

Gauss M. Cordeiro<br>Universidade Federal de Pernambuco, Departamento de Economia, Cidade Universitária, Recife, PE, Brazil<br>Ruben Klein<br>Laboratório Nacional de Computação Científica, Botafogo, Rio de Janeiro, RJ, Brazil

Received May 1992
Revised May 1993


#### Abstract

We give a general matrix formula for computing the bias of the exact unconditional maximum likelihood estimate in ARMA models, with known and unknown mean, up to order $1 / n$, where $n$ is the length of the series. Some illustrative examples are presented.


Keywords: ARMA model; bias correction; maximum likelihood estimate.

## 1. Introduction

In this paper we derive a general matrix formula for computing second-order biases of the exact unconditional maximum likelihood (MLEs) in ARMA models with known and unknown mean. The formula depends only on the covariance matrix structure $V$, its inverse $V^{-1}$ and the first and second partial derivatives of either $V$ or $V^{-1}$. Expressions for $V$ or $V^{-1}$ for general ARMA models are given, for instance, in Shaman (1973), Galbraith and Galbraith (1974) and Ljung and Box (1979).

It is possible, but algebraically hard, to find explicit expressions for the second-order biases in terms of the parameters in particular cases. The use of an algebraic computation package like REDUCE (Hearn, 1984) or MAPLE (see Char et al., 1988) is very helpful. We have found such expressions for the AR(1), AR(2), and MA(1) processes and they appear to work properly. But for particular values of the parameters, it is quite easy to compute the biases numerically via a language supporting numerical linear algebra such as GAUSS, APL or Splus. For doing this, it is sufficient to find $V, V^{-1}$ and the first two partial derivatives of either one with respect to the parameters of the model. We also shown that the bias of the MLE up to order $1 / n$ for the unknown mean case decomposes in the sum of the bias up to order $1 / n$ of the MLE for the known mean case plus a term that also depends only on $V, V^{-1}$ and the first two partial derivatives of either one with respect to the parameters. It is shown that the MLE for the unknown mean is unbiased up to order $1 / n$. In this way it becomes clear how the bias depends on whether or not the mean is estimated.

Tanaka (1984) computed these biases for the cases of known and unknown mean, through the use of asymptotic expansions associated with the MLEs in ARMA models. He has no such decomposition of

[^0]the bias. We believe our method is much simpler than his and has great advantages for numerical purposes.

Bias for other estimators have been studied in the literature. In particular, Shaman and Stine (1988) studied the bias of least-squares and Yule-Walker estimators for autoregressive processes, and Marriot and Pope (1954) had already shown for the AR(1) case, that the bias of the least squares estimates depends on whether or not the mean is estimated.

Godolphin and de Gooijer (1982) and Magee (1989) present small simulation studies for the MA(1) and AR(1) models respectively, where the bias for the MLE is estimated from the simulation.

## 2. A general matrix expression for the bias

Let $\ell(\beta)$ be the total $\log$ likelihood for some vector $\beta$ of unknown parameters of dimension $p$. We assume that $\ell(\beta)$ is regular with respect to all $\beta$ derivatives up to and including those of third order. We define joint cumulants of the log likelihood derivatives by $k_{i j}=E\left(\partial^{2} \ell / \partial \beta_{i} \partial \beta_{j}\right), k_{i j l}=E\left(\partial^{3} \ell / \partial \beta_{i} \partial \beta_{j} \partial \beta_{l}\right)$ and $k_{i j, l}=\mathrm{E}\left\{\left(\partial^{2} \ell / \partial \beta_{i} \partial \beta_{j}\right)\left(\partial \ell / \partial \beta_{l}\right)\right\}$ for $i, j, l=1, \ldots, p$. Furthermore, we define the following cumulant derivative $k_{i j}^{(l)}=\partial k_{i j} / \partial \beta_{l}$ for $i, j, l=1, \ldots, p$. The total Fisher Information matrix of order $p$ for $\beta$ is $K=\left\{-k_{i j}\right\}$ and let $K^{-1}=\left\{-k^{i j}\right\}$ be its inverse. All $k$ 's are assumed to be $\mathrm{O}(n)$, where $n$ is the sample size.

Cox and Snell (1968) showed that for independent, but not necessarily identically distributed observations, the bias $b$ of the MLE $\hat{\beta}$ of $\beta$ reduces to

$$
b_{s}=E\left(\hat{\beta_{s}}-\beta_{s}\right)=\sum_{i, j, l=1}^{p} k^{s i} k^{j l}\left\{\frac{1}{2} k_{i j l}+k_{i j, l}\right\}+\mathrm{O}\left(n^{-2}\right)
$$

for $s=1, \ldots, p$. Recently, Cordeiro and McCullagh (1991) using (1) derived general formulae for second-order biases of MLEs of all parameters in generalized linear models. We now apply formula (1) for ARMA models. It is important to point out that (1) continues to be valid for non-independent observations provided that all $k$ 's are $\mathrm{O}(n)$, as is the case for ARMA models. This follows by examining the orders of the terms in the Taylor series expansions and their expectations in Cox and Snell's (1968) proof.

We can rewrite (1) up to order $n^{-1}$ as

$$
b_{s}=\sum_{i=1}^{p} k^{s i} \sum_{j, l=1}^{p}\left\{k_{i j}^{(l)}-\frac{1}{2} k_{i j l}\right\} k^{j l},
$$

for $s=1, \ldots, p$.
In matrix notation, the vector $b$ is then

$$
b=E(\hat{\beta}-\beta)=K^{-1} A \operatorname{vec}\left(K^{-1}\right)+\mathrm{O}\left(n^{-2}\right)
$$

where vec $\left(K^{-1}\right)$ is the vector obtained by stacking the columns of $K^{-1}$ and where $A=\left\{A^{(1)}|\cdots| A^{(p)}\right\}$, with $A^{(l)}=\left\{a_{i j}^{(l)}\right\}$ having its $(i, j)$ th element defined by $a_{i j}^{(l)}=k_{i j}^{(l)}-\frac{1}{2} k_{i j l}$ for $l=1, \ldots, p$. The bias corrected MLE is given by $\tilde{\beta}=\hat{\beta}-\hat{K}^{-1} \hat{A}$ vec $\left(\hat{K}^{-1}\right)$, where $\hat{K}^{-1}$ and $\hat{A}$ are the matrices $K^{-1}$ and $A$ computed at $\hat{\beta}$, and would be expected to have better sampling properties than the uncorrected $\hat{\beta}$.

## 3. Bias of the MLE in ARMA models

An ARMA ( $p, q$ ) model is defined by

$$
y_{t}-\mu-\alpha_{1}\left(y_{t-1}-\mu\right)-\cdots-\alpha_{p}\left(y_{t-p}-\mu\right)=u_{t}-\theta_{1} u_{t-1}-\cdots-\theta_{q} u_{t-q},
$$

where the $u_{t}$ 's are independent random variables with mean $\mu$ and variance $\sigma^{2}$ and $y=\left(y_{1} \ldots y_{n}\right)^{\mathrm{T}}$ is the observed time series of length $n$. Let $\beta=\left(\alpha_{1}, \ldots, \alpha_{p}, \theta_{1}, \ldots, \theta_{q}, \sigma^{2}\right)^{\mathrm{T}}$ be the $(p+q+1)$ vector of unknown parameters in the known mean case and let $\beta^{*}=\left(\beta^{\mathrm{T}}, \mu\right)^{\mathrm{T}}$ be the $(p+q+2)$ vector of unknown parameters in the unknown mean case.

The log likelihood $\ell(\beta)$ for $\beta$ given $y$ is

$$
\ell(\beta)=-\frac{1}{2} n \log (2 \pi)-\frac{1}{2} n \log \left(\sigma^{2}\right)-\frac{1}{2} \log (|V|)-\left(\left(y-\mu 1_{n}\right)^{\mathrm{T}} V^{-1}\left(y-\mu 1_{n}\right)\right) / 2 \sigma^{2},
$$

where $\sigma^{2} V$ is the covariance matrix of $y$,

$$
V=V\left(\alpha_{1}, \ldots, \alpha_{p}, \theta_{1}, \ldots, \theta_{q}\right)
$$

and $1_{n}$ is the $n$-dimensional vector with all entries equal to 1 .
We define the derivatives, for $i, j-1, \ldots, p+q, V_{i}=\partial V / \partial \beta_{i}, V^{i}=\partial V^{-1} / \partial \beta_{i}, V_{i j}=\partial^{2} V / \partial \beta_{i} \partial \beta_{j}$ and $V^{i j}=\partial^{2} V^{-1} / \partial \beta_{i} \partial \beta_{j}$ and adopt the following notation:

$$
\begin{aligned}
& \tilde{V}_{i}=V^{-1} V_{i}, \quad \tilde{V}^{i}=V^{i} V=-\bar{V}_{i}, \quad \tilde{V}_{i j}=V^{-1} V_{i j}, \quad \tilde{V}^{i j}=V^{i j} V, \\
& m_{i}=\operatorname{tr}\left(\tilde{V}_{i}\right), \quad m^{i}=\operatorname{tr}\left(\tilde{V}^{i}\right)=-m_{i}, \quad m_{i j}=\operatorname{tr}\left(\tilde{V}_{i j}\right), \quad m^{i j}=\operatorname{tr}\left(\tilde{V}^{i j}\right), \\
& m_{i, j}=\operatorname{tr}\left(\tilde{V}_{i} \tilde{V}_{j}\right), \quad m^{i, j}=\operatorname{tr}\left(\tilde{V}^{i} \tilde{V}^{j}\right), \\
& m_{i j, l}=\operatorname{tr}\left(\tilde{V}_{i j} \tilde{V}_{l}\right), \quad m^{i j, l}=\operatorname{tr}\left(\tilde{V}^{i j} \tilde{V}^{l}\right), \quad m_{i, j, l}=\operatorname{tr}\left(\tilde{V}_{i} \tilde{V}_{j} \tilde{V}_{l}\right), \quad m^{i, j, l}=\operatorname{tr}\left(\tilde{V}^{i} \tilde{V}^{j} \tilde{V}^{l}\right) .
\end{aligned}
$$

The $m$ 's defined above satisfy certain equations which facilitate their calculations. For example, $m_{i j}=2 m^{i, j}-m^{i j}, m^{i j}=2 m_{i, j}-m_{i j}, m_{r i, j}=m^{r i, j}-m^{r, i, j}-m^{r, j, i}, m_{i, j, r}=-m^{i, j, r}$ and so on

Differentiating (3) and making use of the relations $V^{i}=-V^{-1} V_{i} V^{-1}, \partial \log |V| / \partial \beta_{i}=\operatorname{tr}\left(V^{-1} V_{i}\right)$, together with the multiplicative rule for differentiation and the equation $E\left(\left(y-\mu 1_{n}\right)^{\mathrm{T}} G\left(y-\mu 1_{n}\right)\right)= \sigma^{2} \operatorname{tr}(V G)$, for any positive definite matrix $G$ (see Press, 1982 and Mardia and Marshall, 1984), we find after some algebra the following.

Case 1. Known mean.

$$
\begin{aligned}
K & =\frac{1}{2}\left(\begin{array}{cc}
\left(m_{i, j}\right) & \left(m_{i} / \sigma^{2}\right) \\
\left(m_{j} / \sigma^{2}\right) & n / \sigma^{4}
\end{array}\right)_{1 \leq i, j \leq p+q} \\
& =\frac{1}{2}\left(\begin{array}{cc}
\left(m^{i, j}\right) & \left(-m^{i} / \sigma^{2}\right) \\
\left(-m^{j} / \sigma^{2}\right) & n / \sigma^{4}
\end{array}\right)_{1 \leq i, j \leq p+q} \\
A^{(l)} & =-\frac{1}{4}\left(\begin{array}{cc}
\left(m_{l i, j}+m_{l j, i}-m_{i j, l}\right) & \left.m_{l i} / \sigma^{2}\right) \\
\left(m_{l j} / \sigma^{2}\right) & 2 m_{l} / \sigma^{4}
\end{array}\right)_{1 \leq i, j \leq p+q} \\
& =-\frac{1}{4}\left(\begin{array}{cc}
\left(m^{l i, j}+m^{l j, i}+m^{i j, l}-2 m^{i, j, l}\right) & \left(\left(2 m^{l, i}-m^{l i}\right) / \sigma^{2}\right) \\
\left(\left(2 m^{l, j}-m^{l j}\right) / \sigma^{2}\right) & -2 m^{l} / \sigma^{4}
\end{array}\right)_{1 \leq i, j \leq p+q}
\end{aligned}
$$

for $l=1, \ldots, p+q$, and

$$
\begin{aligned}
A^{\left(\sigma^{2}\right)}=A^{(p+q+1)} & =-\frac{1}{4}\left(\begin{array}{cc}
\left(\left(2 m_{i, j}-m_{i j}\right) / \sigma^{2}\right) & 0 \\
0 & 0
\end{array}\right)_{1 \leq i, j \leq p+q} \\
& =-\frac{1}{4}\left(\begin{array}{cc}
\left(m^{i j} / \sigma^{2}\right) & 0 \\
0 & 0
\end{array}\right)_{1 \leq i, j \leq p+q}
\end{aligned}
$$

Case 2. Unknown mean. In this case $\beta^{*}=\left(\beta^{\mathrm{T}}, \mu\right)^{\mathrm{T}}$ is the $(p+q+2)$ vector of unknown parameters and

$$
\begin{aligned}
& b^{*}=\left(b_{\beta}^{* \mathrm{~T}}, b_{\mu}^{*}\right)^{\mathrm{T}}=E\left(\hat{\beta}^{*}-\beta^{*}\right)=K^{*-1} A^{*} \operatorname{vec}\left(K^{*-1}\right)+\mathrm{O}\left(n^{-2}\right), \\
& K^{*}=\left(\begin{array}{cc}
K & O \\
O & 1_{n}^{\mathrm{T}} V^{-1} 1_{n} / \sigma^{2}
\end{array}\right) \\
& A^{*}=\left(A^{*(1)} \mid \cdots\right. \\
& A^{*(I)}=\left(\begin{array}{cc}
A^{(l)} & O \\
O & 1_{n}^{\mathrm{T}} V^{l} 1_{n} / 2 \sigma^{2}
\end{array}\right), \quad l=1, \ldots, p+q, \\
& A^{*\left(\sigma^{2}\right)}=\left(\begin{array}{cc}
A^{\left(\sigma^{2}\right)} & O \\
O & -1_{n}^{\mathrm{T}} V^{-1} 1_{n} / 2 \sigma^{4}
\end{array}\right)
\end{aligned}
$$

and

$$
A^{*(\mu)}=\left(\begin{array}{cc}
O & a^{*} \\
a^{* T} & O
\end{array}\right)
$$

where

$$
a^{*}=\left(1_{n}^{\mathrm{T}} V^{1} 1_{n} / 2 \sigma^{2}, \ldots, 1_{n}^{\mathrm{T}} V^{p+q} 1_{n} / 2 \sigma^{2},-1_{n}^{\mathrm{T}} V^{-1} 1_{n} / 2 \sigma^{4}\right)^{\mathrm{T}}
$$

is a $(p+q+1)$-dimensional vector, and $K, A^{l}, l=1, \ldots, p+q, A^{\left(\sigma^{2}\right)}$ are as in Case 1 . Then

$$
b_{\mu}^{*}=0+\mathrm{O}\left(n^{-2}\right)
$$

and

$$
b_{\beta}^{*}=b+c+\mathrm{O}\left(n^{-2}\right)
$$

where

$$
b=K^{-1} A \operatorname{vec}\left(K^{-1}\right)
$$

is the bias in the known mean case and

$$
c=\sigma^{2}\left(1_{n}^{\mathrm{T}} V^{-1} 1_{n}\right)^{-1} K^{-1} a^{*}
$$

is the added term for the bias in the unknown mean case.

## 4. Computation of the biases

Formula (2) in conjunction with (4)-(15) may be implemented in a computer algebra system to obtain bias-corrected MLEs in ARMAmodels to order $n^{-1}$ with minimal effort. In fact, for an ARMA( $p, q$ ) model, we know $V$ and $V^{-1}$, and we can find $V^{i}, V_{i}, V_{i j}$ or $V, V^{1}, V^{i j}$. Furthermore, we can evaluate these matrices at a particular value of $\beta$, for example, at $\hat{\beta}$. Thus, we can calculate, at least numerically, all the $\tilde{V}$ 's and $m$ 's given in Section 3. Therefore, in the known mean case, we can obtain $K$ and $A$ from (4)-(6). Inverting $K$ and using (2), we obtain the biases by simple matrix multiplication. For the unknown mean case, we just have to add to $b$ the second term, $c$, in (13).

## 5. Application to special models

To apply algebraically formula (2) to a specific example involves a lot of work. In the examples below, we have used the algebraic computing packages REDUCE and MAPLE to verify some computations and to do some others. Let us consider the cases with known and unknown mean.

Example 1. A stationary $\operatorname{AR}(1)$. The model is given by

$$
y_{t}-\mu-\alpha\left(y_{t-1}-\mu\right)=u_{t}, \quad|\alpha|<1, \quad t=1, \ldots, n .
$$

The matrix $V$ has a very simple form

$$
V=\left(1-\alpha^{2}\right)^{-1}\left(\begin{array}{cc}
1 & \alpha \cdots \alpha^{n-1} \\
\alpha^{n-1} & \alpha^{n-2} \cdots 1
\end{array}\right)
$$

and, therefore, we can compute the biases of $\hat{\alpha}$ and $\hat{\sigma}^{2}$ to order $n^{-1}$ from (2) and (4)-(15).
Case 1. Known mean case. We have

$$
b_{\alpha}=E(\hat{\alpha}-\alpha)=\frac{-2 \alpha\left(1-\alpha^{2}\right)\left[n^{3}\left(1-\alpha^{2}\right)-2 n^{2}\left(1-2 \alpha^{2}\right)+n\left(1-5 \alpha^{2}\right)+2 \alpha^{2}\right]}{\left[n^{2}\left(1-\alpha^{2}\right)-n\left(1-3 \alpha^{2}\right)-2 \alpha^{2}\right]^{2}}
$$

and

$$
b_{\sigma^{2}}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)-\frac{-n\left(1-\alpha^{2}\right) \sigma^{2}}{n^{2}\left(1-\alpha^{2}\right)-n\left(1-3 \alpha^{2}\right)-2 \alpha^{2}}
$$

We can approximate further, up to $\mathrm{O}\left(n^{-1}\right)$, and the last two equations become

$$
b_{\alpha}=E(\hat{\alpha}-\alpha)=-2 \alpha / n \quad \text { and } \quad b_{\sigma^{2}}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)-\sigma^{2} / n .
$$

Case 2. Unknown mean case. We have after approximations, up to $\mathrm{O}\left(n^{-1}\right)$,

$$
c_{\alpha}=\frac{-(1+\alpha)}{n} \quad \text { and } \quad c_{\sigma^{2}}=\frac{-\sigma^{2}}{n}
$$

and the biases up to $\mathrm{O}\left(n^{-1}\right)$ are given by

$$
b_{\alpha}^{*}=E(\hat{\alpha}-\alpha)=-\frac{2 \alpha}{n}-\frac{1+\alpha}{n}=-\frac{1+3 \alpha}{n}
$$

and

$$
b_{\sigma^{2}}^{*}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)=-\frac{\sigma^{2}}{n}-\frac{\sigma^{2}}{n}=-\frac{2 \sigma^{2}}{n}
$$

These results are in agreement with the results obtained by Tanaka (1984, p. 66).
Example 2. An invertible MA(1). The model is

$$
y_{t}-\mu=u_{t}-\theta u_{t-1}, \quad|\theta|<1, \quad t=1, \ldots, n .
$$

Shaman (1973) gave a closed-form expression for $V^{-1}$ for a moving average process of order $q$. Using (2) and (4)-(15), we can compute the biases of $\hat{\theta}$ and $\hat{\sigma}^{2}$.

Case 1. Known mean case. We have

$$
b_{\theta}=E(\hat{\theta}-\theta)=\theta\left(1-\theta^{2}\right)\left(1-\theta^{2 n+2}\right) A / B^{2}
$$

and

$$
b_{\sigma^{2}}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)=-\sigma^{2} n\left(1-\theta^{2}\right)\left(1-\theta^{2 n+2}\right)^{2} / B
$$

where

$$
\begin{aligned}
A= & n^{4}\left[2 \theta^{2 n}\left(1-\theta^{2}\right)^{2}\left(\theta^{2 n+2}-2 \theta^{2 n}+1\right)\right] \\
& -n^{3}\left[\left(1-\theta^{2}\right)\left(\theta^{6 n+4}-2 \theta^{6 n+2}+3 \theta^{4 n+4}-12 \theta^{4 n+2}+10 \theta^{4 n}+6 \theta^{2 n+2}-5 \theta^{2 n}-1\right)\right] \\
& -n^{2}\left[\left(1-\theta^{2 n}\right)\left(1-\theta^{2 n+2}\right)\left(\theta^{2 n+4}+3 \theta^{2 n+2}-8 \theta^{2 n}+5 \theta^{2}-1\right)\right] \\
& +n\left[2\left(1-\theta^{2 n}\right)^{2}\left(5 \theta^{2 n+2}-4 \theta^{2}-1\right)\right]-4 \theta^{2}\left(1-\theta^{2 n}\right)^{3}
\end{aligned}
$$

and

$$
\begin{aligned}
B= & n^{3}\left[2 \theta^{2 n}\left(1-\theta^{2}\right)^{2}\right]-n^{2}\left[\left(1-\theta^{2}\right)\left(\theta^{4 n+2}+3 \theta^{2 n+2}-3 \theta^{2 n}-1\right)\right] \\
& +n\left[\left(1-\theta^{2 n}\right)\left(\theta^{2 n+4}+3 \theta^{2 n+2}-3 \theta^{2}-1\right)\right]-2 \theta^{2}\left(1-\theta^{2 n}\right)^{2}
\end{aligned}
$$

If $\theta^{2 n} \cong \mathrm{O}$, we conclude, ignoring terms of order less than $n^{-1}$, that

$$
b_{\theta}=E(\hat{\theta}-\theta)=\frac{\theta\left(1-\theta^{2}\right)\left[n^{3}\left(1-\theta^{2}\right)+n^{2}\left(1-5 \theta^{2}\right)-2 n\left(1+4 \theta^{2}\right)-4 \theta^{2}\right]}{\left[n^{2}\left(1-\theta^{2}\right)-n\left(1+3 \theta^{2}\right)-2 \theta^{2}\right]^{2}}
$$

and

$$
b_{\sigma^{2}}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)=\frac{-\sigma^{2} n\left(1-\theta^{2}\right)}{n^{2}\left(1-\theta^{2}\right)-n\left(1+3 \theta^{2}\right)-2 \theta^{2}}
$$

Thus, to $\mathrm{O}\left(n^{-1}\right)$, it follows

$$
b_{\theta}=E(\hat{\theta}-\theta)=\theta / n \quad \text { and } \quad b_{\sigma^{2}}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)=-\sigma^{2} / n .
$$

Case 2. Unknown mean case. We have after approximations, up to $\mathrm{O}\left(n^{-1}\right)$,

$$
c_{\theta}=\frac{1+\theta}{n} \quad \text { and } \quad c_{\sigma^{2}}=\frac{-\sigma^{2}}{n}
$$

Then the biases, up to $\mathrm{O}\left(n^{-1}\right)$, are given by

$$
b_{\theta}^{*}=E(\hat{\theta}-\theta)=\frac{\theta}{n}+\frac{1+\theta}{n}=\frac{1+2 \theta}{n}
$$

and

$$
b_{\sigma^{2}}^{*}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)=-\frac{\sigma^{2}}{n}-\frac{\sigma^{2}}{n}=-\frac{2 \sigma^{2}}{n}
$$

These results coincide with the rcsults of Tanaka (1984, p. 66).
Example 3. A stationary $\operatorname{AR}(2)$. The model is given by

$$
y_{t}-\mu-\alpha_{1}\left(y_{t-1}-\mu\right)-\alpha_{2}\left(y_{t-2}-\mu\right)=u_{t}, \quad t=1, \ldots, n,
$$

where the roots of $\alpha(z)=1-\alpha_{1} z-\alpha_{2} z^{2}$ are such that $|z|>1$. Hence using (2) and (4)-(15), we can compute up to $\mathrm{O}\left(n^{-1}\right)$, the biases of $\hat{\alpha}_{1}, \hat{\alpha}_{2}$ and $\hat{\sigma}^{2}$.

Case 1. Known mean case. We have

$$
\begin{aligned}
& b_{\alpha_{1}}=E\left(\hat{\alpha}_{1}-\alpha_{1}\right)=-\alpha_{1}\left(\alpha_{2}+1\right)\left[n\left(\left(\alpha_{2}-1\right)^{2}-\alpha_{1}^{2}\right)-2\left(3 \alpha_{2}^{2}+1-\alpha_{1}^{2}\right)\right] / D_{1} . \\
& b_{\alpha_{2}}=E\left(\hat{\alpha}_{2}-\alpha_{2}\right) \\
& \quad=-\left(\alpha_{2}+1\right)\left[n\left(3 \alpha_{2}+1\right)\left(\left(\alpha_{2}-1\right)^{2}-\alpha_{1}^{2}\right)-2 \alpha_{2}\left(5 \alpha_{2}^{2}-6 \alpha_{2}-3 \alpha_{1}^{2}+1\right)\right] / D_{1} \\
& b_{\sigma^{2}}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)=-\sigma^{2}\left[2 n^{2}\left(\left(\alpha_{2}-1\right)^{2}-\alpha_{1}^{2}\right)\left(\alpha_{2}+1\right)\right. \\
& \quad-n\left(\left(9 \alpha_{2}^{2}+2 \alpha_{2}-3\right)\left(\alpha_{2}-1\right)-\left(7 \alpha_{2}+5\right) \alpha_{1}^{2}\right)+8 \alpha_{2}^{2}\left(\alpha_{2}-1\right) \\
& \left.\quad-2 \alpha_{1}^{2}\left(3 \alpha_{2}+1\right)\right] / D_{2}
\end{aligned}
$$

where

$$
\begin{aligned}
D_{1}= & n^{2}\left(\left(\alpha_{2}-1\right)^{2}-\alpha_{1}^{2}\right)\left(\alpha_{2}+1\right)-n\left(\alpha_{2}^{2}\left(7 \alpha_{2}-5\right)-\alpha_{1}^{2}\left(5 \alpha_{2}+3\right)+1-3 \alpha_{2}\right) \\
& +4 \alpha_{2}^{2}\left(3 \alpha_{2}-1\right)-2 \alpha_{1}^{2}\left(3 \alpha_{2}+1\right)
\end{aligned}
$$

and

$$
\begin{aligned}
D_{2}= & n^{3}\left(\left(\alpha_{2}-1\right)^{2}-\alpha_{1}^{2}\right)\left(\alpha_{2}+1\right)-n^{2}\left(\left(9 \alpha_{2}^{2}+2 \alpha_{2}-3\right)\left(\alpha_{2}-1\right)-\left(7\left(\alpha_{2}+5\right) \alpha_{1}^{2}\right)\right. \\
& +2 n\left(13 \alpha_{2}^{3}-7 \alpha_{2}^{2}-3 \alpha_{2}+1-4 \alpha_{1}^{2}\left(2 \alpha_{2}+1\right)\right)-8 \alpha_{2}^{2}\left(3 \alpha_{2}-1\right)+4 \alpha_{1}^{2}\left(3 \alpha_{2}+1\right)
\end{aligned}
$$

To order $n^{-1}$ we hence have

$$
\begin{aligned}
& b_{\alpha_{1}}=E\left(\hat{\alpha}_{1}-\alpha_{1}\right)=-\alpha_{1} / n, \quad b_{\alpha_{2}}=E\left(\hat{\alpha}_{2}-\alpha_{2}\right)=-\left(3 \alpha_{2}+1\right) / n \quad \text { and } \\
& b_{\sigma^{2}}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)=-2 \sigma^{2} / n
\end{aligned}
$$

Case 2. Unknown mean case. We have, after approximations, up to $\mathrm{O}\left(n^{-1}\right)$,

$$
c_{\alpha_{1}}=\frac{-\left(1+\alpha_{2}\right)}{n}, \quad c_{\alpha_{2}}=\frac{-\left(1+\alpha_{2}\right)}{n} \quad \text { and } \quad c_{\sigma^{2}}=\frac{-\sigma^{2}}{n} .
$$

Then the biases, up to $\mathrm{O}\left(n^{-1}\right)$, are given by

$$
\begin{aligned}
& b_{\alpha_{1}}^{*}=E\left(\hat{\alpha}_{1}-\alpha_{1}\right)=-\frac{\alpha_{1}}{n}-\frac{1+\alpha_{2}}{n}=-\frac{1+\alpha_{1}+\alpha_{2}}{n}, \\
& b_{\alpha_{2}}^{*}=E\left(\hat{\alpha}_{2}-\alpha_{2}\right)=-\frac{1+3 \alpha_{2}}{n}-\frac{1+\alpha_{2}}{n}=-\frac{2\left(1+2 \alpha_{2}\right)}{n}
\end{aligned}
$$

and

$$
b_{\sigma^{2}}^{*}=E\left(\hat{\sigma}^{2}-\sigma^{2}\right)=-\frac{2 \sigma^{2}}{n}-\frac{\sigma^{2}}{n}=-\frac{3 \sigma^{2}}{n}
$$

These results again agree with the results of Tanaka (1984, p. 66).

## Acknowledgment

The authors thank Telma Suaiden Klein for the computations in MAPLE.

## References

Char, B.W., K.O. Geddes, G.H. Gonnet, M.B. Monagan and S.M. Watt (1988), Maple Reference Manual (WATCOM Publications Ltd., Waterloo, Canada, 5th ed.).
Cordeiro, G.M. and P. McCullagh (1991), Bias correction in generalized linear models, J.R. Statist. Soc. B 53, 629-643.
Cox, D.R. and E.J. Snell (1968), A general definition of residuals, J.R. Statist. Soc. B 30, 248-275.
Galbraith, R.F. and J.I. Galbraith (1974), On the inverses of some patterned matrices arising in the theory of stationary time series, J. Appl. Prob. 11, 63-71.
Godolphin, E.J. and S.G. de Gooijer (1982), On the maximum likelihood estimation of the parameters of a Gaussian moving average process, Biometrika 69, 443-451.
Hearn, A.C. (ed.) (1984), Reduce User's Manual, version 3.1 (The Rand Corporation).
Ljung, G.M. and G.E.P. Box (1979), The likelihood function of stationary autoregressive-moving average models, Biometrika 66, 265-270.
Magee, L. (1989), Bias approximation for covariance parame-
ter estimators in the linear model with AR(1) errors, Commun. Statist-Theory Meth. 18, 395-422.
Mardia, K.V. and R.J. Marshall (1984), Maximum likelihood estimation of models for residual covariance in spatial regression, Biometrika 71, 135-146.
Marriot, F.H.C. and J.A. Pope (1954), Bias in the estimation of autocorrelations, Biometrika 41, 390-402.
Press, S.J. (1982), Applied Multivariate Analysis Including Bayesian and Frequentist Methods of Inference (Krieger Publishing Company, Melbourne, Florida).
Shaman, P. (1973), On the inverse of the covariance matrix for an autoregressive-moving average process, Biometrika 60, 193-196.
Shaman, P. and R.A. Stine (1988), The bias of autoregressive coefficient estimators, J. Amer. Statist. Assoc. 83, 842-848.
Tanaka, K. (1984), An asymptotic expansion associated with the maximum likelihood estimators in ARMA models, J.R. Statist. Soc. B 46, 58-67.


[^0]:    Correspondence to: Dr. R. Klein, Laboratorio Nacional de Computação Científica, Rua Lauro Muller 455, 22290-160 Rio de Janeiro, RJ, Brazil.

