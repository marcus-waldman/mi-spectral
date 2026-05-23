---
citekey: imhofComputingDistributionQuadratic1961
item_type: article
authors: 'Imhof, J. P.'
year: 1961
title: Computing the Distribution of Quadratic Forms in Normal Variables
venue: Biometrika
volume: 48
issue: 3-4
pages: 419--426
doi: 10.1093/biomet/48.3-4.419
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\imhof_computing_distribution_quadratic_1961.pdf'
pdf_sha256: fd0a1820a03c2142cfa13d3f1d50efb546d9b7bff07234508513d51739b30b6a
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-23T01:22:37Z
---
This is the published version of the publication, made available in accordance with the publisher's policy.

Computing the distribution of quadratic forms in normal variables

Imhof, Jean-Pierre

## How to cite

IMHOF, Jean-Pierre. Computing the distribution of quadratic forms in normal variables. In: Biometrika, 1961, vol. 48, $\mathrm{n}^{\circ}$ 3-4, p. 419-426. doi: 10.1093/biomet/48.3-4.419

This publication URL: https://archive-ouverte.unige.ch/unige:101766
Publication DOI: 10.1093/biomet/48.3-4.419
© The author(s). This work is licensed under a Backfiles purchase (National Licenses Project) https://www.unige.ch/biblio/aou/fr/guide/info/references/licences/

Last deposit update in Archive ouverte UNIGE on 15.03.2023 08:48

# Computing the distribution of quadratic forms in normal variables 

By J. P. IMHOF<br>University of Geneva

## 1. Introduction

In this paper exact and approximate methods are given for computing the distribution of quadratic forms in normal variables. In statistical applications the interest centres in general, for a quadratic form $Q$ and a given value $x$, around the probability $P\{Q>x\}$. Methods of computation have previously been given e.g. by Box (1954), Gurland (1955) and by Grad \& Solomon (1955). None of these methods is very easily applicable except, when it can be used, the finite series of Box. Furthermore, all the methods are valid only for quadratic forms in central variables. Situations occur where quadratic forms in non-central variables must be considered as well. Let $\mathrm{x}=\left(x_{1}, \ldots, x_{n}\right)^{\prime}$ be a column random vector which follows a multidimensional normal law with mean vector $O$ and covariance matrix $\Sigma$. Let $\mu=\left(\mu_{1}, \ldots, \mu_{n}\right)^{\prime}$ be a constant vector, and consider the quadratic form $Q=(\mathbf{x}+\mu)^{\prime} \mathbf{A}(\mathbf{x}+\mu)$. If $\Sigma$ is non-singular, one can by means of a non-singular linear transformation (Scheffé (1959), p. 418) express $Q$ in the form

$$
Q=\sum_{r=1}^{m} \lambda_{r} \chi_{h_{r} ; \delta_{r}^{2}}^{2} .
$$

The $\lambda_{r}$ are the distinct non-zero characteristic roots of $\mathbf{A} \boldsymbol{\Sigma}$, the $h_{r}$ their respective orders of multiplicity, the $\delta_{r}$ are certain linear combinations of $\mu_{1}, \ldots, \mu_{n}$ and the $\chi_{h_{r} ; \delta_{r}^{2}}^{2}$ are independent $\chi^{2}$-variables with $h_{r}$ d.f. (degrees of freedom) and non-centrality parameter $\delta_{r}^{2}$. The variable $\chi_{h ; \delta^{2}}^{2}$ is defined here by the relation $\chi_{h ; \delta^{2}}^{2}=\left(x_{1}+\delta\right)^{2}+\sum_{2}^{h} x_{i}^{2}$, where $x_{1}, x_{2}, \ldots, x_{h}$ are independent unit normal deviates. In case $\boldsymbol{\Sigma}$ is singular but $\mathbf{A}$ is not, a similar decomposition can be obtained except that an additive constant might figure in the right-hand member of $(1 \cdot 1)$. This is the case for instance if $Q=\left(x_{1}+x_{2}\right)^{2}+x_{3}^{2}$, where the linear constraint $x_{1}+x_{2}=c$ is imposed.

We illustrate the reduction of a quadratic form to the form (l•1) on the correlator

$$
w=\sum_{1}^{n}\left(x_{i}-\mu_{i}\right)\left(y_{i}-\eta_{i}\right),
$$

where the $x_{i}$ and $y_{i}$ are normal deviates with zero means and we assume that

$$
\operatorname{cov}\left(x_{i}, x_{j}\right)=\operatorname{cov}\left(y_{i}, y_{j}\right)=\delta_{i j}, \quad \operatorname{cov}\left(x_{i}, y_{j}\right)=\rho \delta_{i j} \quad \text { and } \quad|\rho|<1 .
$$

Expressions for the probability density of $w$ have been given in some particular cases of these assumptions by Roe \& White (1961). Let

$$
z=\left(x_{1}, \ldots, x_{n}, y_{1}, \ldots, y_{n}\right)^{\prime} \quad \text { and } \quad \zeta=\left(\mu_{1}, \ldots, \mu_{n}, \eta_{1}, \ldots, \eta_{n}\right)^{\prime} .
$$

Then $w=(z-\zeta)^{\prime} \mathbf{A}(z-\zeta)$, where $\mathbf{A}$ and the covariance matrix $\mathbf{\Sigma}$ of $\mathbf{z}$ can be partitioned into square submatrices of $n$ rows each: If U denotes the unit (identity) matrix,

$$
\boldsymbol{\Sigma}=\left[\begin{array}{cc}
\mathbf{U} & \rho \mathbf{U} \\
\rho \mathbf{U} & \mathbf{U}
\end{array}\right], \quad \mathbf{A}=\left[\begin{array}{cc}
\mathbf{O} & \mathbf{U} \\
\mathbf{U} & \mathbf{O}
\end{array}\right] .
$$

Under the linear transformation $\mathbf{z}^{*}=\mathbf{P z}$, where

$$
\mathbf{P}=2^{-\frac{1}{2}}\left[\begin{array}{lr}
(1-\rho)^{-1} \mathrm{U} & -(1-\rho)^{-1} \mathrm{U} \\
(1+\rho)^{-1} \mathrm{U} & (1+\rho)^{-1} \mathrm{U}
\end{array}\right]
$$

the correlator takes the form $w=\left(\mathbf{z}^{*}-\zeta^{*}\right)^{\prime} \mathbf{A}^{*}\left(\mathbf{z}^{*}-\zeta^{*}\right)$, where $\zeta^{*}=\mathbf{P} \zeta$ and $\mathbf{A}^{*}$ is a diagonal matrix having its $n$ first diagonal elements equal to $\rho-1$, the $n$ remaining ones equal to $\rho+1$. The covariance matrix of $z^{*}$ is the unit matrix. The random variable $w$ can therefore be written

$$
w=(\rho+1) \chi_{n ; \delta_{1}^{2}}^{2}+(\rho-1) \chi_{n ; \delta_{2}^{2}}^{2}
$$

a linear combination of two independent $\chi^{2}$-variables with non-centrality parameters $\delta_{1}^{2}=\frac{1}{2}(1+\rho)^{-1} \sum_{1}^{n}\left(\mu_{i}+\eta_{i}\right)^{2}$ and $\delta_{2}^{2}=\frac{1}{2}(1-\rho)^{-1} \sum_{1}^{n}\left(\mu_{i}-\eta_{i}\right)^{2}$.

## 2. Finite expressions

Box (1954) has considered the case where in (1•1) $\delta_{r}^{2}=0$ and $h_{r}=2 \nu_{r}(r=1, \ldots, m)$, the $\nu_{r}$ being positive integers. In statistical applications, it is often possible to arrange for the d.f.'s to be even. A problem in the theory of Gaussian noise where this condition is always fulfilled is described by Davenport \& Root (1958). Box has then expressed the probability $P\{Q>x\}$ by means of a finite series of $\chi^{2}$ probabilities. Using a different proof, a modified and often more convenient form of his result will be obtained, as well as a corresponding expression for the probability density $g(x)$ of $Q$. Suppose $\lambda_{1}, \ldots, \lambda_{m}$ have been ordered, so that $\lambda_{1}>\lambda_{2}>\ldots>\lambda_{p}>0>\lambda_{p+1}>\ldots>\lambda_{m}$. Let $n=\sum_{1}^{m} \nu_{r}$ and $q=\sum_{1}^{p} \nu_{r}$.

Theorem. If $x>0$, then

$$
P\left[\sum_{1}^{m} \lambda_{r} \chi_{2_{r}}^{2}>x\right]=\sum_{k=1}^{p} \frac{1}{\left(v_{k}-1\right)!}\left[\frac{\partial^{v_{1}-1}}{\partial \lambda^{v_{1}-1}} F_{k}(\lambda, x)\right]_{\lambda=\lambda_{k}}
$$

where

$$
F_{k}(\lambda, x)=\lambda^{n-1} \exp \{-x /(2 \lambda)\} \prod_{\substack{r=1 \\ r+k}}^{m}\left(\lambda-\lambda_{r}\right)^{\rightarrow_{r}}
$$

Proof. Let $\lambda_{1}^{\prime}, \ldots, \lambda_{q}^{\prime}, \lambda_{q+1}^{\prime}, \ldots, \lambda_{n}^{\prime}$ be real, pairwise unequal parameters such that $\lambda_{s}^{\prime}>0$ for $s=1, \ldots, q$ and $\lambda_{s}^{\prime}<0$ for $s=q+1, \ldots, n$. Let $Q^{\prime}=\sum_{1}^{n} \lambda_{s}^{\prime} \chi_{2}^{2}(s)$, where the $n \chi^{2}$-variables $\chi_{2}^{3}(s)$ with two d.f. each are independent. The characteristic function $\phi^{\prime}(t)$ of $Q^{\prime}$ is

$$
\phi^{\prime}(t)=\prod_{1}^{n}\left(1-2 i \lambda_{s}^{\prime} t\right)^{-1}
$$

and correspondingly the probability density is

$$
g^{\prime}(x)=\frac{1}{2 \pi} \int_{-\infty}^{+\infty} e^{-i t x} \prod_{1}^{n}\left(1-2 i \lambda^{\prime}, t\right)^{-1} d t
$$

The integrand having simple poles only, one finds for $x>0$

$$
g^{\prime}(x)=\sum_{s=1}^{q} t_{s}(x) \prod_{s^{\prime}=1}^{n}\left(\lambda_{s}^{\prime}-\lambda_{s}^{\prime}\right)^{-1}
$$

where $\Pi^{\prime}$ indicates that the factor corresponding to $s^{\prime}=8$ is omitted, and where

$$
t_{s}(x)=\frac{1}{2} \lambda_{s}^{\prime 0-2} \exp \left\{-x /\left(2 \lambda_{s}^{\prime}\right)\right\} .
$$

in which $X$ and $Y$ are independent Poisson variables with expected values $\frac{1}{2} x$ and $\frac{1}{2} \delta^{2}$, respectively. Johnson (1959) rediscovered this equality and used it as a starting point to The density $g(x)$ of $Q$ can now be obtained by a passage to the limit. Let $\sigma_{0}=0, \sigma_{k}=\sum_{r=1}^{k} \nu_{r}$ for $k=1, \ldots, m$. For positive distinct integers $a, b, \ldots, d$ all not larger than $m$, denote by lim the passage to the limit
$a, b, \ldots, d$

$$
\lambda_{\sigma_{a-1}+1}^{\prime}, \ldots, \lambda_{\sigma_{a}}^{\prime} \rightarrow \lambda_{a}, \ldots, \lambda_{\sigma_{d-1}+1}^{\prime}, \ldots, \lambda_{\sigma_{d}}^{\prime} \rightarrow \lambda_{d}
$$

Then $g(x)=\lim _{1,2, \ldots, m} g^{\prime}(x)$ can be written

$$
\begin{aligned}
g(x)= & \sum_{k=1}^{p} \lim _{k} \sum_{s=-\sigma_{k-1}+1}^{\sigma_{k}} t_{s}(x) \prod_{s-\sigma_{k-1}+1}^{\sigma_{k}}\left(\lambda_{s}^{\prime}-\lambda_{s}^{\prime}\right)^{-1} \\
& \times \lim _{1, \ldots, k-1} \prod_{s<\sigma_{k-1}}\left(\lambda_{s}^{\prime}-\lambda_{s}^{\prime}\right)^{-1} \lim _{k+1, \ldots, m} \prod_{s>\sigma_{k}}\left(\lambda_{s}^{\prime}-\lambda_{s}^{\prime}\right)^{-1} \\
= & -\sum_{k=1}^{p} \lim _{k} \sum_{s=-\sigma_{k-1}+1}^{\sigma_{k}}\left\{f_{k}\left(\lambda_{s}^{\prime}, x\right) \prod_{s=\sigma_{k-1}+1}^{\sigma_{k}}\left(\lambda_{s}^{\prime}-\lambda_{s}^{\prime}\right)^{-1}\right\},
\end{aligned}
$$

where $f_{k}(\lambda, x)=(\partial / \partial x) F_{k}(\lambda, x)$. One recognizes the summation over $s$ as the divided difference of order $\nu_{k}-1$ of the function $f_{k}(\lambda, x)$, corresponding to the $\nu_{k}$ 'abscissas' $\lambda_{\sigma_{1-1}+1}^{\prime}, \ldots, \lambda_{\sigma_{k}}^{\prime}$. Hence, by a well-known result, one has for $x>0$

$$
a(x)=-\sum_{k=1}^{p} \frac{1}{\left(\nu_{k}-1\right)!}\left[\frac{\partial^{v_{k}-1}}{\partial \lambda^{v_{k}-1}} f_{k}(\lambda, x)\right]_{\lambda-\lambda_{k}} .
$$

Upon integrating this expression, formula (2•1) results. For $x<0$, one must substitute $\sum_{p+1}^{m}$ for $-\sum_{1}^{p}$ in (2.2) and $1-\sum_{p+1}^{m}$ for $\sum_{1}^{p}$ in (2.1).

A particular case of the theorem is

$$
P\left\{\chi_{2}^{2}>x\right\}=\frac{1}{(\nu-1)!}\left[\frac{\partial^{\nu-1}}{\partial \lambda^{\nu-1}}\left\{\lambda^{\nu-1} e^{-x(2 \lambda)}\right\}\right]_{\lambda-1} .
$$

Even using this, it is not easily possible to establish in general the equivalence of (2.1) with formula (2-11) of Box (1954).

The formulae $(2 \cdot 1)$ and $(2 \cdot 2)$ are very convenient to use when all $\nu_{k}$ are small. With increasing $\nu_{k}$ 's, the labour of computing the corresponding derivatives of $F_{k}(\lambda, x)$, or $f_{k}(\lambda, x)$ rapidly becomes considerable. The numerical method of the next section is then often easier to apply.

Consider now the case where the variables are non-central. The characteristic function of $(1 \cdot 1)$ is

$$
\phi(t)=\prod_{1}^{m}\left(1-2 i \lambda_{r} t\right)^{-\frac{1}{2} h_{r}} \exp \left\{i \sum_{1}^{m} \frac{\delta_{r}^{2} \lambda_{r} t}{1-2 i \lambda_{r} t}\right\} .
$$

To obtain the probability density by integration of the inversion formula appears hopeless, except in the particular case $m=1$. One finds then for the density $p_{n}\left(x, \delta^{2}\right)$ of $\chi_{n ; \delta^{2}}^{2}$ the relation

$$
p_{n}\left(x, \delta^{2}\right)=\frac{1}{2} \exp \left\{-\frac{1}{2}\left(x+\delta^{2}\right)\right\}\left(x^{\frac{1}{2}} / \delta\right)^{\frac{1}{2} n-1} I_{\frac{1}{n} n-1}\left(\delta x^{\frac{1}{2}}\right),
$$

where $I_{v}(z)$ is the Bessel function of purely imaginary argument, of order $\nu$. This formula has been given first by Fisher (1928) who pointed out on the same occasion the relation

$$
P\left\{\chi_{2_{r} ; 8^{r}}^{2}<x\right\}=P\{X-Y \geqslant \nu\},
$$

derive some simple approximations for $P\left\{\chi_{n ; \delta^{*}}^{8}<x\right\}$. However, expressions in finite terms obtainable for such probabilities, when $n$ is odd, by integrating ( $2 \cdot 4$ ) do not seem to have previously been written down explicitly. We shall give the first few of them, which are simple enough to be useful in numerical work. It is necessary to assume $n>1$. Write then $n=2 m+3(m=0,1, \ldots)$. A classical formula permits the expression in finite terms of the Bessel function of half integral order appearing in (2.4). One finds

$$
p_{n}\left(x, \delta^{2}\right)=\frac{1}{2 \delta^{n-2}(2 \pi)^{\frac{1}{2}}}\left[e^{-\frac{1}{2} a^{2}} \sum_{r=0}^{m}(-1)^{r} A_{m}(r, x)+(-1)^{m+1} e^{-\frac{1}{2} b^{2}} \sum_{r=0}^{m} A_{m}(r, x)\right]
$$

where

$$
a=x^{\frac{1}{2}}-\delta, \quad b=x^{\frac{1}{2}}+\delta, \quad A_{m}(r, x)=\frac{(m+r)!\left(\delta x^{\frac{1}{2}}\right)^{m-r}}{2^{r} r!(m-r)!} .
$$

The above density can be integrated explicitly. If $I(x)$ denotes the cumulative distribution function of a unit normal variable, the result is found to be

$$
P\left\{\chi_{n ; \delta^{*}}^{2}>x\right\}=2-I(a)-I(b)+\frac{1}{\delta^{n-2}(2 \pi)^{\frac{1}{2}}}\left[K_{n}(\delta, a)-K_{n}(\delta,-b)\right]
$$

where $K_{n}(\delta, x)=\exp \left\{-\frac{1}{2} x^{2}\right\} P_{n}(\delta, x)$ and $P_{n}(\delta, x)$ is a polynomial in $\delta$ of degree $n-3$. The general expression for $P_{n}(\delta, x)$ is not simple. The polynomials corresponding to the values $n=3,5,7$ and 9 are

$$
\begin{aligned}
& P_{3}(\delta, x) \equiv 1, \quad P_{5}(\delta, x)=2 \delta^{2}+x \delta-1 \\
& P_{7}(\delta, x)=3 \delta^{4}+3 x \delta^{3}+\left(x^{2}-4\right) \delta^{2}-3 x \delta+3 \\
& P_{9}(\delta, x)=4 \delta^{6}+6 x \delta^{5}+\left(4 x^{2}-10\right) \delta^{4}+\left(x^{3}-15 x\right) \delta^{3}-\left(6 x^{2}-18\right) \delta^{2}+15 x \delta-15 .
\end{aligned}
$$

In the applications, $b$ is often large enough so that one can assume $I(b)=1, K_{n}(\delta,-b)=0$.

## 3. Numerical inversion of the characteristic function

In this section we show that the cumulative distribution function $F(x)$ of the variable $Q$ defined by ( $1 \cdot 1$ ) can be obtained quite easily by straightforward numerical integration of an inversion formula. The standard inversion formula gives an expression not for $F(x)$ itself, but for the difference $F(x)-F(0)$. If $Q$, as is the case, for instance, in (1•2), is not strictly positive, a formula is needed which gives $F(x)$ directly. Such a formula is implicit in work of Gurland (1948) and has been later derived explicitly by Gil-Pelaez (1951), namely

$$
F(x)=\frac{1}{2}-\frac{1}{\pi} \int_{0}^{\infty} t^{-1} \mathscr{J}\left\{e^{-i t x} \phi(t)\right\} d t
$$

where $\mathscr{J}(z)$ denotes the imaginary part of $z$ and where the characteristic function $\phi(t)$ of $Q$ is given by ( $2 \cdot 3$ ). Using the relations

$$
\begin{gathered}
\arg \left[(1-i b t)^{-0}\right]=g \tan ^{-1}(b t), \quad\left|(1-i b t)^{-0}\right|=\left(1+b^{2} t^{2}\right)^{-\frac{1}{2} a}, \\
\arg [\exp \{i a t /(1-i b t)\}]=a t /\left(1+b^{2} t^{2}\right), \quad|\exp \{i a t /(1-i b t)\}|=\exp \left\{-a b t^{2} /\left(1+b^{2} t^{2}\right)\right\},
\end{gathered}
$$

one finds that for the quadratic form $Q$ of (1.1), equation (3.1) can be written, after the substitution $2 t=u$ is made,

$$
P\{Q>x\}=\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \frac{\sin \theta(u)}{u \varphi(u)} d u
$$

where

$$
\begin{aligned}
& \theta(u)=\frac{1}{2} \sum_{1}^{m}\left[h_{r} \tan ^{-1}\left(\lambda_{r} u\right)+\delta_{r}^{2} \lambda_{r} u\left(1+\lambda_{r}^{2} u^{2}\right)^{-1}\right]-\frac{1}{2} x u \\
& \rho(u)=\prod_{1}^{m}\left(1+\lambda_{r}^{2} u^{8}\right)^{\frac{1}{h_{r}}} \exp \left\{\frac{1}{2} \sum_{1}^{m}\left(\delta_{r} \lambda_{r} u\right)^{2} /\left(1+\lambda_{r}^{2} u^{2}\right)\right\}
\end{aligned}
$$

The following relations are immediate

$$
\begin{aligned}
& \lim _{u \rightarrow 0} \frac{\sin \theta(u)}{u p(u)}=\frac{1}{2} \sum_{1}^{m} \lambda_{r}\left(h_{r}+\delta_{r}^{2}\right)-\frac{1}{2} x \\
& \lim _{u \rightarrow \infty} \theta(u)=\left\{\begin{array}{lll}
-\infty & \text { if } & x>0 \\
+\infty & \text { if } & x<0 \\
\frac{\pi}{4} \sum_{1}^{m} h_{r} \lambda_{r}\left|\lambda_{r}\right|^{-1} & \text { if } & x=0
\end{array}\right.
\end{aligned}
$$

The function $u \rho(u)$ increases monotonically towards $+\infty$. Therefore, in numerical work the integration in (3.2) will be carried over a finite range $0 \leqslant u \leqslant U$ only; the degree of approximation obtained will depend (apart from rounding-off errors) on two sources of error: (i) the 'error of integration' resulting from the use of an approximate rule for computing

$$
I_{U}=\pi^{-1} \int_{0}^{U}[u \rho(u)]^{-1} \sin \theta(u) d u
$$

and (ii) the 'error of truncation'

$$
t_{U}=\pi^{-1} \int_{U}^{\infty}[u \rho(u)]^{-1} \sin \theta(u) d u
$$

Noticing that $x>y$ implies $x^{2}\left(1+x^{2}\right)^{-1}>y^{2}\left(1+y^{2}\right)^{-1}$, one finds that $\left|t_{U}\right|$ can be bounded above by $T_{U}$, where

$$
T_{U}^{-1}=\pi k U^{k} \prod_{1}^{m}\left|\lambda_{r}\right|^{\frac{1}{2} h_{r}} \exp \left\{\frac{1}{2} \sum_{1}^{m} \delta_{r}^{2} \lambda_{r}^{2} U^{2}\left(1+\lambda_{r}^{2} U^{2}\right)^{-1}\right\},
$$

and where we have put $k=\frac{1}{2} \sum_{1}^{m} h_{r}$. One can hopefully expect that $T_{U}$ will often be satisfactorily small, even for moderate values of $U$. It does not seem feasible on the other hand to obtain an upper bound for the error of integration resulting from the application of a standard quadrature formula. With equal step formulae (in the application of which the ordinate at the origin is given by ( $3 \cdot 3$ )), a common procedure is then to carry out the integration repeatedly, each time halving the step of integration until two consecutive results agree to the desired accuracy. In order to gather some more detailed information relative to the performance of the two simplest and most commonly used rules, namely, the trapezoidal rule and Simpson's rule, we have preferred to follow a different procedure. Given a tolerance $\epsilon$, numerical integration in (3.2) was carried out by using steps of length $j / 10$. The integer $j$ was then increased, one unit at a time, until the largest value was attained such that, for the first even number of steps yielding a bound $T_{U} \leqslant \varepsilon$, the values of the integral obtained by the trapezoidal rule and by Simpson's rule, say $J_{T}$ and $J_{S}$, still satisfy $\left|J_{T}-J_{S}\right| \leqslant \epsilon$. Results for the values $\epsilon=0.01$ and $\epsilon=0.001$ are given in Table 1. The following unexpected behaviour was observed in all cases: As $j$ increases, $J_{S}$ departs from the correct value of the integral 'more rapidly' than does $J_{T}$. In other words, to achieve a given accuracy, longer steps are permissible with the trapezoidal rule than with Simpson's rule. Some computations made with
a formula（sometimes referred to as Hardy＇s rule）based on approximation of the integrand with polynomials of degree six seem to indicate that in fact，the higher the degree of the approximation polynomials used，the shorter the step of integration must be．Accordingly， only the results obtained with the trapezoidal rule are recorded in columns（i）and（ii）of Table 1 and are seen to be of much greater accuracy than the value of $\epsilon$ would let one

Table 1．Probability that the quadratic form $Q$ exceeds $x$
（i）Integration in（3．3）with the trapezoidal rule and $n$ steps of length $j$ ，for tolerance $\epsilon=0.01$ ； （ii）same for tolerance $\varepsilon=0.001$ ；（iii）exact values；（iv）Pearson＇s three－moment $\chi^{2}$ approximation； （v）Patnaik＇s two－moment $\chi^{2}$ approximation．
| $Q$ | $\epsilon=0.01$ |  |  |  | $\epsilon=0.001$ |  |  | （iii） | （iv） | （v） |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $x$ | $n$ | $j$ | （i） | n | $j$ | （ii） |  |  |  |
| $Q_{1}=0.6 \chi_{1}^{2}+0.3 \chi_{1}^{2}+0.1 \chi_{1}^{2}$ | 0.1 | 16 | $1 \cdot 9$ | 0.9478 | 136 | 1.0 | 0.9457 | 0.9458 | 1.0000 | 0.9184 |
|  | 0.7 | 14 | $2 \cdot 2$ | －5076 | 114 | $1 \cdot 2$ | － 5065 | －5064 | 0.4901 | －5079 |
|  | 2 | 10 | 3.0 | －1262 | 86 | 1.6 | －1240 | －1240 | －1264 | －1310 |
| $Q_{2}=0 \cdot 6 \chi_{2}^{2}+0 \cdot 3 \chi_{2}^{2}+0 \cdot 1 \chi_{2}^{2}$ | $0 \cdot 2$ | 8 | 1.2 | 0.9903 | 24 | 0.8 | 0.9930 | 0.9936 | 1.0000 | 0.9867 |
|  | 2 | 6 | 1.9 | －4020 | 20 | 1.0 | －3997 | －3998 | 0.3961 | －4098 |
|  | 6 | 8 | 1.1 | －0159 | 20 | 1.0 | － 0161 | － 0161 | ． 0162 | － 0145 |
| $Q_{2}=0.6 \chi_{6}^{2}+0.3 \chi_{4}^{2}+0.1 \chi_{2}^{2}$ | 1 | 6 | 0.7 | 0.9980 | 14 | 0.4 | 0.9974 | 0.9973 | 0.9984 | 0.9961 |
|  | 5 | 4 | 1.1 | －4354 | 8 | 0.7 | －4353 | －4353 | －4346 | －4400 |
|  | 12 | 8 | 0.6 | －0087 | 12 | 0.5 | ． 0088 | ． 0088 | －0087 | － 0080 |
| $Q_{4}=0 \cdot 6 \chi_{2}^{2}+0 \cdot 3 \chi_{4}^{2}+0 \cdot 1 \chi_{4}^{2}$ | 1 | 8 | 1.1 | 0.9663 | 16 | 0.7 | 0.9666 | 0.9666 | 0.9767 | 0.9522 |
|  | 3 | 6 | 1.4 | －4201 | 10 | 1.0 | ． 4195 | ． 4196 | －4156 | －4330 |
|  | 8 | 10 | 0.8 | ． 0088 | 14 | 0.8 | ． 0087 | ． 0087 | － 0086 | －0066 |
| $Q_{5}=0 \cdot 7 \chi_{6 ; 6}^{2}+0 \cdot 3 \chi_{2 ; 2}^{2}$ | 2 | 6 | 0.3 | 0.9938 | 14 | 0.2 | 0.9937 | 0.9939 | 0.9928 | 0.9954 |
|  | 10 | 4 | 0.7 | 4098 | 8 | 0.4 | －4086 | －4087 | －4089 | ． 4045 |
|  | 20 | 6 | 0.3 | － 0223 | 10 | 0.3 | － 0221 | －0221 | － 0221 | ． 0230 |
| $Q_{s}=0.7 \chi_{1 ;}^{2}+0.3 \chi_{1 ; 2}^{2}$ | 1 | 8 | 0.4 | 0.9544 | 48 | 0.3 | 0.9549 | 0.9549 | 0.9515 | 0.9719 |
|  | 6 | 6 | 0.7 | －4079 | 36 | 0.4 | －4075 | －4076 | －4084 | － 3948 |
|  | 15 | 8 | 0.4 | － 0224 | 36 | 0.4 | ． 0223 | － 0223 | － 0223 | ． 0246 |
| $\$ Q_{3}+1 Q_{4}$ | 1.5 | 8 | 1.2 | 0.9891 | 12 | 0.9 | 0.9890 | 0.9891 | 0.9923 | 0－9842 |
|  | 4 | 4 | 2.4 | －3463＊ | 8 | 1.4 | － 3453 | －3453 | －3449 | － 3552 |
|  | 7 | 8 | 1.2 | － 0154 | 12 | 1.0 | ． 0154 | － 0154 | 0.154 | ． 0131 |
| $\$ Q_{8}-1 Q_{4}$ | －2 | 6 | 1.6 | 0.9103 | 10 | 1.2 | 0.0102 | 0.9102 | 0.9011 | － |
|  | 0 | 4 | 2.2 | －4052 | 10 | 1.3 | －4061 | －4061 | －4221 | － |
|  | 2.5 | 8 | 1.1 | ． 0097 | 14 | 0.8 | ． 0098 | － 0097 | ． 0032 | － |
| $\frac{1}{2} Q_{5}+\frac{1}{2} Q_{6}$ | 3.5 | 6 | 0.6 | 0.9563 | 10 | 0.4 | 0.9563 | 0.9563 | 0.9560 | 0.9605 |
|  | 8 | 4 | 1.1 | －4161 | 8 | 0.6 | －4152 | －4152 | －4153 | －4101 |
|  | 13 | 6 | 0.6 | ． 0462 | 8 | 0.5 | － 0462 | － 0462 | － 0461 | ． 0474 |
| $\frac{1}{2} Q_{5}-\frac{1}{2} Q_{6}$ | －2 | 6 | 0.6 | 0.0218 | 8 | 0.5 | 0.0218 | 0.9218 | $0.9166 \dagger$ | 一 |
|  | 2 | 2 | 3.9 | ． 4685 | 4 | 1.4 | －4782 | －4779 | －4810 † | 一 |
|  | 7 | 6 | 0.6 | ． 0396 | 10 | $0 \cdot 4$ | ． 0396 | ． 0396 | ． $0387 \dagger$ | － |
| $f\left(Q_{3}+Q_{4}+Q_{5}+Q_{5}\right)$ | 3 | 10 | 1.0 | 0.9842 | 16 | 0.7 | 0.9842 | 0－9842 | 0.9840 | 0.9837 |
|  | 6 | 6 | 2.0 | －4270＊ | 10 | $1 \cdot 2$ | ． 4264 | －4264 | －4264 | － 4270 |
|  | 10 | 12 | 0.9 | ． 0117 | 14 | 0.8 | ． 0117 | －0117 | － 0117 | － 0116 |
| $\frac{1}{6}\left(Q_{3}-Q_{5}\right)+\frac{8}{6}\left(Q_{6}-Q_{4}\right)$ | －3 | 12 | 0－9 | 0.9861 | 18 | 0.7 | 0.9861 | 0.9861 | 0.9904 | 一 |
|  | 0 | 6 | 2.0 | ． 5180 | 12 | 1.1 | ． 5170 | ． 5170 | －5154 | 一 |
|  | 4 | 12 | 0－9 | － 0152 | 16 | 0－8 | ． 0152 | ． 0152 | － 0139 | 一 |


＊Corresponds to first maximum of $\left|J_{T}-J_{S}\right|$ ．† Wilson－Hilferty approximation．
suspect. We have in several cases computed the correction terms, up to the one involving finite differences of orders one to six, which are to be added to the trapezoidal rule according to Gregory's formula. They have proved to give no reliable estimate of the error of integration resulting from the use of the trapezoidal rule. For $\epsilon=0.01$, it was found in two cases that as $j$ increases, $\left|J_{T}-J_{S}\right|$ first increases to reach a maximum smaller than $0 \cdot 01$, then decreases again. The results corresponding to the value of $j$ for which $\left|J_{T}-J_{S}\right|$ attains its first maximum are then recorded. It is clear that under such circumstances, the procedure we have followed is not an adequate one to use in general practice. Another example of this is provided by $Q=\frac{1}{2} Q_{5}-\frac{1}{2} Q_{6}$, for $x=2$. In this case, it was necessary to increase $j$ up to 3.9 before $\left|J_{T}-J_{S}\right|$ reached $\epsilon=0.01$, while two steps of length 1.5 already make $T_{U}<0.01$ and give the better value 0.4787 . It is hoped, however, that a sufficient variety of quadratic forms is covered so that Table 1 can serve as a useful guide for the length of the step of integration to be used in any particular case. To help in this purpose, all quadratic forms listed satisfy $\sum_{1}^{m}\left|\lambda_{r}\right|=1$.

The probability density $g(x)$ of the quadratic form $Q$ could be computed by using a formula analogous to (3.2). In fact,

$$
g(x)=\pi^{-1} \int_{0}^{\infty}[\rho(u)]^{-1} \cos \theta(u) d u
$$

Due to the absence of the factor $u^{-1}$ in the integrand, numerical integration, for the same accuracy, can be expected to require a slightly larger number of steps than is needed to compute the distribution function.

## 4. The accuracy of some approximations

Recently Johnson (1959) has shown that Pearson's (1959) three-moment central $\chi^{2}$ approximation to the distribution of non-central $\chi^{2}$ is remarkably accurate in both tails of the distribution. It is therefore natural to extend this approximation to the general case of the quadratic form $Q$ of (1•1). Let $E(Q)$ and $\sigma(Q)$ be the mean and standard deviation of $Q$. Following Pearson, we write for a positive quadratic form $Q$,

$$
Q \cong\left(\chi^{2}-h^{\prime}\right)\left(2 h^{\prime}\right)^{-\frac{1}{2}} \sigma(Q)+E(Q)
$$

and determine $h^{\prime}$ so that both members have equal third moments. This amounts to taking

$$
P\{Q>x\} \cong P\left\{\chi_{k^{\prime}}^{\Omega}>y\right\},
$$

where $\quad h^{\prime}=c_{2}^{3} / c_{3}^{8}, \quad y=\left(x-c_{1}\right)\left(h^{\prime} / c_{2}\right)^{\frac{1}{2}}+h^{\prime}, \quad c_{j}=\sum_{1}^{m} \lambda_{r}^{\prime}\left(h_{r}+j \delta_{r}^{2}\right) \quad(j=1,2,3)$.
If $Q$ is non-positive, the same approximation can be used but one must assume that $c_{3}>0$. Otherwise, approximate the distribution of $-Q$. The values obtained from (4.1) are shown in column (iv) of Table 1. For the quadratic form $\frac{1}{2} Q_{5}-\frac{1}{2} Q_{6}$, one has $h^{\prime}=1395.85$. In this case, the Wilson-Hilferty approximation was used to evaluate the right-hand member of (4•1). The merits of the three-moment approximation are obvious, particularly in the upper tail of positive quadratic forms. For such forms, the approximate values given by the standard two-moment (Patnaik) approximation are indicated in column (v). It is seen that the three-moment approximation, which requires very little more work, gives a much better fit than is achieved with the Patnaik approximation. While there is an appreciable loss of accuracy for non-positive forms, the approximation still gives useful indications which can suffice for certain practical purposes.

Most of the computations summarized in Table 1 have been performed on the Ferranti 'Mercury' computer at CERN, Geneva. I am much indebted to the late Director General of that organization, Prof. C. J. Bakker, who made it possible for me to use the facilities of the computer service.

I wish to thank the Referee for suggesting some notable improvements in the presentation of the paper.

## References

Box, G. E. P. (1954). Some theorems on quadratic forms applied in the study of analysis of variance problems, I. Effect of inequality of variance in the one-way classification. Ann. Math. Statist. 25, 290-302.
Davenport, W. B. \& Root, W. L. (1958). An Introduction to the Theory of Random Signals and Noise. New York: McGraw-Hill.
Fisher, R. A. (1928). The general sampling distribution of the multiple correlation coefficient. Proc. Roy. Soc. A, 121, 654-73.
Gil-Pelaez, J. (1951). Note on the inversion theorem. Biometrika, 38, 481-2.
Grad, A. \& Solomon, H. (1955). Distribution of quadratic forms and some applications. Ann. Math. Statist. 26, 464-77.
Gurland, J. (1948). Inversion formulae for the distribution of ratios. Ann. Math. Statist. 19, 228-37.
Gurland, J. (1955). Distribution of definite and indefinite quadratic forms. Ann. Math. Statist. 26, 122-7.
Johnson, N. L. (1959). On an extension of the connexion between Poisson and $\chi^{2}$ distributions. Biometrika, 46, 352-63.
Prarson, E. S. (1959). Note on an approximation to the distribution of non-central $\chi^{2}$. Biometrika, 46, 364.
Roe, G. M. \& White, G. M. (1961). Probability density functions for correlators with noisy reference signals. IRE Trans. on Information Theory, IT-7, 13-18.
Scheffet, H. (1959). The Analysis of Variance. New York: John Wiley and Sons.

