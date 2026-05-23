---
citekey: wilksLargeSampleDistributionLikelihood1938a
item_type: article
authors: 'Wilks, S. S.'
year: 1938
title: 'The {Large-Sample Distribution} of the {Likelihood Ratio} for {Testing Composite Hypotheses}'
venue: The Annals of Mathematical Statistics
volume: 9
issue: 1
pages: 60--62
doi: 10.1214/aoms/1177732360
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\wilks_large_sample_distribution_1938.pdf'
pdf_sha256: 3f71dffb265d9a52a067db4ccf17dd6447544755eac147c6eee1384fe3c2ebe8
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T23:01:52Z
---
# THE LARGE-SAMPLE DISTRIBUTION OF THE LIKELIHOOD RATIO FOR TESTING COMPOSITE HYPOTHESES ${ }^{1}$ 

By S. S. Wilks

By applying the principle of maximum likelihood, J. Neyman and E. S. Pearson ${ }^{2}$ have suggested a method for obtaining functions of observations for testing what are called composite statistical hypotheses, or simply composite hypotheses. The procedure is essentially as follows: A population $K$ is assumed in which a variate $x$ ( $x$ may be a vector with each component representing a variate) has a distribution function $f\left(x, \theta_{1}, \theta_{2}, \cdots \theta_{h}\right)$, which depends on the parameters $\theta_{1}, \theta_{2} \cdots \theta_{h}$. A simple hypothesis is one in which the $\theta$ 's have specified values. A set $\Omega$ of admissible hypotheses is considered which consists of a set of simple hypotheses. Geometrically, $\Omega$ may be represented as a region in the $h$-dimensional space of the $\theta$ 's. A set $\omega$ of simple hypotheses is specified by taking all simple hypotheses of the set $\Omega$ for which $\theta_{i}=\theta_{0 i}, i= m+1, m+2, \cdots h$.

A random sample $O_{n}$ of $n$ individuals is considered from $K . O_{n}$ may be geometrically represented as a point in an $n$-dimensional space of the $x$ 's. The probability density function associated with $O_{n}$ is

$$
P=\prod_{\alpha=1}^{n} f\left(x_{\alpha}, \theta_{1}, \theta_{2}, \cdots \theta_{h}\right)
$$

Let $P_{\Omega}\left(O_{n}\right)$ be the least upper bound of $P$ for the simple hypotheses in $\Omega$, and $P_{\omega}\left(O_{n}\right)$ the least upper bound of $P$ for those in $\omega$. Then

$$
\lambda=\frac{P_{\omega}\left(O_{n}\right)}{P_{0}\left(O_{n}\right)}
$$

is defined as the likelihood ratio for testing the composite hypothesis $H$ that $O_{n}$ is from a population with a distribution characterized by values of the $\theta_{i}$ for some simple hypothesis in the set $\omega$. When we say that $H$ is true, we shall mean that $O_{n}$ is from some population of the set just described. In most of the cases of any practical importance, $P$ and its first and second derivatives with respect to the $\theta_{i}$ are continuous functions of the $\theta_{i}$ almost everywhere in a certain region of the $\theta$-space for almost all possible samples $O_{n}$. We shall only consider the case in which $P_{\Omega}\left(O_{n}\right)$ and $P_{\omega}\left(O_{n}\right)$ can be determined from the first and second order derivatives with respect to the $\theta$ 's.

[^0]A considerable number of currently used statistical functions for making tests of significance can be expressed in terms of $\lambda$ ratios, and in many cases involving normal distribution theory, the exact sampling distribution of $\lambda$ is known. However, it is often useful when dealing with large samples to have an approximation to the distribution of $\lambda$. We shall consider such an approximation for those cases (which include most of the ones of any practical importance) in which optimum estimates of the $\theta$ 's exist. That is, we shall assume the existence of functions $\tilde{\theta}_{i}\left(x_{1}, \cdots x_{n}\right)$ (maximum likelihood estimates of the $\theta_{i}$ ) such that ${ }^{8}$ their distribution is

$$
\frac{\left|c_{i j}\right|^{\frac{1}{2}}}{(2 \pi)^{h / 2}} e^{-\frac{1}{i} \sum_{i, j-1}^{h} c_{i j} z_{i} \dot{z}_{j}}(1+\phi) d z_{1} \cdots d z_{h}
$$

where $z_{i}=\left(\bar{\theta}_{i}-\theta_{i}\right) \sqrt{n}, c_{i j}=-E\left(\frac{\partial^{2} \log f}{\partial \theta_{i} \partial \theta_{j}}\right), E$ denoting mathematical expectation, and $\phi$ is of order $1 / \sqrt{ } \bar{n}$ and $\left\|c_{i j}\right\|$ is positive definite. Denoting (3) by $J d z_{1} d z_{2} \cdots d z_{h}$, and differentiating $J$ with respect to $\theta_{k}$, we get

$$
\frac{1}{2}\left(\frac{1}{\left|c_{i j}\right|} \frac{\partial\left|c_{i j}\right|}{\partial \theta_{k}}-\sum_{i, j} \frac{\partial c_{i j}}{\partial \theta_{k}} z_{i} z_{j}+\sqrt{ } \bar{n} \sum_{j} c_{k j} z_{j}\right) J, \quad k=1,2, \cdots h
$$

Since $c_{i j}=O(1)$ and $\left|c_{i j}\right| \neq 0$, it can be seen from (4) that the values of $\theta_{k}$ which maximize $J$ differ from $\bar{\theta}_{k}, k=1,2, \cdots h$, by terms of order $1 / \sqrt{n}$. Therefore, the maximum $P_{\mathrm{a}}\left(O_{n}\right)$ of $J$ with respect to the $\theta_{k}$ is $\frac{\left|c_{i j}\right|^{\frac{1}{2}}}{(2 \pi)^{k / 2}}\left(1+\phi^{\prime}\right)$, where $\phi^{\prime}=O(1 / \sqrt{n})$.

To get $P_{\omega}\left(O_{n}\right)$, we let $\theta_{i}=\theta_{0 i}, i=m+1, m+2, \cdots h$, and note that $J$ can be written as

$$
J_{0}=\frac{\left|c_{0 i j}\right|^{\frac{1}{2}}}{(2 \pi)^{h / 2}}, e^{-\frac{1}{\sum_{i, i-1}^{m} c_{i j} z_{i}^{\prime} z_{j}^{\prime}-1 x_{0}^{2}}}\left(1+\phi_{0}^{\prime}\right)
$$

where

$$
\chi_{0}^{2}=\sum_{i, j=m+1}^{h} c_{i j}^{\prime} z_{i} z_{j}, \quad \phi_{0}^{\prime}=O(1 / \sqrt{n})
$$

and $\left\|c_{i j}^{\prime}\right\|$ is the inverse of the matrix obtained by deleting the first $m$ rows and first $m$ columns from $\left\|c_{i j}\right\|^{-1}$ and $z_{i}^{\prime}=z_{i}-L_{i}, L_{i}$ being a linear function of $\theta_{0, m+1} \cdots \theta_{0 h}$, and $c_{0 i j}$ is the value of $c_{i j}$ with $\theta_{i}=\theta_{0 i}, i=m+1, m+2, \cdots h$, that is, when $H$ is true. Taking the maximum $P_{\omega}\left(O_{n}\right)$ of expression (5) with respect to $\theta_{1}, \theta_{2}, \cdots \theta_{m}$, we get

$$
P_{\omega}=\frac{\left|c_{0 i j}\right|^{\frac{2}{2}}}{(2 \pi)^{h / 2}} e^{-\frac{1}{2} x_{0}^{2}}\left(1+\phi_{0}^{\prime \prime}\right) \quad \quad \phi_{0}^{\prime \prime}=O(1 / \sqrt{n})
$$

[^1]Hence, when $H$ is true, we have, from (5) and (7)

$$
\lambda=\frac{P_{\omega}\left(O_{n}\right)}{P_{\Omega}\left(O_{n}\right)}=e^{-\frac{1}{2} x_{0}^{2}}(1+O(1 / \sqrt{n})) .
$$

Therefore, except for terms of order $1 / \sqrt{n}$,

$$
-2 \log \lambda=\chi_{0}^{2} .
$$

Now, the characteristic function of $-2 \log \lambda$ is

$$
\begin{aligned}
\phi(t) & =E\left(e^{i t(-2 \log \lambda)}\right)=\int \cdots \int J_{0} e^{i t\left(x_{0}^{2}+o(1 / \sqrt{n})\right)} d z_{1} \cdots d z_{h} \\
& =\frac{\left|c_{i j}\right|^{3}}{(2 \pi)^{h / 2}} \int \cdots \int e^{-\frac{1}{i} \sum_{i-1}^{m} c_{i j} z_{i}^{\prime} z_{j}^{\prime}+x_{0}^{2}\left(i t-\frac{1}{2}\right)}(1+O(1 / \sqrt{n})) d z_{1} \cdots d z_{h}
\end{aligned}
$$

It can be shown that on any finite interval $|t|<a, \phi(t)$ approaches uniformly, as $n \rightarrow \infty$, the function

$$
\left(\frac{1}{2}\right)^{\frac{h-m}{2}}\left(\frac{1}{2}-i t\right)^{-\frac{h-m}{2}} .
$$

But (11) is the characteristic function of any quantity distributed like $\chi^{2}$ with $h-m$ degrees of freedom.

We can summarize in the
Theorem: If a population with a variate $x$ is distributed according to the probability function $f\left(x, \theta_{1}, \theta_{2} \cdots \theta_{h}\right)$, such that optimum estimates $\tilde{\theta}_{i}$ of the $\theta_{i}$ exist which are distributed in large samples according to (3), then when the hypothesis $H$ is true that $\theta_{i}=\theta_{0 i}, i=m+1, m+2, \cdots h$, the distribution of $-2 \log \lambda$, where $\lambda$ is given by (2) is, except for terms of order $1 / \sqrt{n}$, distributed like $\chi^{2}$ with $h-m$ degrees of freedom.

Princeton University,
Princeton, N. J.


[^0]:    ${ }^{1}$ Presented to the American Mathmatical Society, March 26, 1937.
    ${ }^{2}$ Phil. Trans. Roy. Soc. London, Ser. A, Vol. 231, p. 295.

[^1]:    ${ }^{8}$ For conditions under which the $\tilde{\theta}$ 's exist which are distributed according to (3), see J. L. Doob, Probability and Statistics, Trans. Amer. Math. Soc. Vol. 36, p. 759-775.

