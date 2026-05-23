---
citekey: reiterSmallsampleDegreesFreedom2007b
item_type: article
authors: 'Reiter, J. P.'
year: 2007
title: Small-Sample Degrees of Freedom for Multi-Component Significance Tests with Multiple Imputation for Missing Data
venue: Biometrika
volume: 94
issue: 2
pages: 502--508
doi: 10.1093/biomet/asm028
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\reiter_small_sample_degrees_2007.pdf'
pdf_sha256: 3099eb59f9b645c813111026756789d77701d89c1977904e73b18e4da6ed1122
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T23:01:52Z
---
## Small-sample degrees of freedom for

# multi-component significance tests with multiple 

imputation for missing data

JEROME P. REITER

Institute of Statistics and Decision Sciences, Duke University
Box 90251, Durham, North Carolina 27708-0251, U.S.A.
jerry@stat.duke.edu


#### Abstract

\section*{SUMMARY}

When performing multi-component significance tests with multiplyimputed datasets, analysts can use a Wald-like test statistic and a reference $F$-distribution. The currently employed degrees of freedom in the denominator of this $F$-distribution is derived assuming an infinite sample size. For modest complete-data sample sizes, this degrees of freedom can be unrealistic; for example, it may exceed the complete-data degrees of freedom. This paper presents an alternative denominator degrees of free-


dom that is always less than or equal to the complete-data denominator degrees of freedom, and equals the currently employed denominator degrees of freedom for infinite sample sizes. Its advantages over the currently employed degrees of freedom are illustrated with a simulation.

Some key words: Missing data; Multiple imputation; Significance test.

## 1 INTRODUCTION

Multiple imputation (Rubin, 1987) has been used to handle missing data in both large samples (Heitjan \& Little, 1991; Schafer et al., 1998; Raghunathan \& Paulin, 1998) and modest samples; see, for example, the examples in Schafer (1997). The basic idea is to fill in the missing data, $Y_{\text {mis }}$, with draws from the conditional distribution of $Y_{\text {mis }}$ given the observed data, or from approximations of that distribution such as those of Raghunathan et al. (2001). These draws are repeated independently $l=1, \ldots, m$ times to obtain $m$ completed datasets, $D^{(1)}, \ldots, D^{(m)}$. The analyst computes point and variance estimates of interest in each $D^{(l)}$, and then combines these estimates using the rules described in Rubin (1987). Multiple rather than single imputations are used so that analysts can estimate the variability due to imputing missing data.

Analysts of the completed datasets may desire to test some $k$-dimensional null hypothesis. Currently, they can do so by using a Wald-like test statistic and the reference $F$-distribution derived by Li et al. (1991). Alternatively, they can use a
likelihood ratio test that is asymptotically equivalent to the Wald-like test and uses an equivalent reference $F$-distribution (Meng \& Rubin, 1992). The denominator degrees of freedom, $v_{\mathrm{w}}$, in these $F$-distributions was obtained under the assumption of infinite sample size. However, for a modest sample size, $v_{\mathrm{w}}$ can exceed the denominator degrees of freedom that would be used if the data were complete, $v_{\text {com }}$. This can result in a larger proportion of $p$-values below desired significance levels than would be expected under the null hypothesis for a test with valid frequentist properties.

This paper presents an alternative denominator degrees of freedom, $v_{\mathrm{f}}$, that is always less than or equal to $v_{\text {com }}$, and equals $v_{\text {w }}$ for infinite sample sizes. The degrees of freedom is derived using second-order Taylor series expansions and so has several terms. It is given by the following two equations:

$$
\begin{aligned}
v_{\mathrm{f}}= & 4+1 / z \\
z= & \frac{1}{v_{\mathrm{com}}^{*}-4(1+a)}+\frac{1}{t-4}\left(\frac{a^{2}\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}}{(1+a)^{2}\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}}\right) \\
& +\frac{1}{t-4}\left(\frac{8 a^{2}\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}}{(1+a)\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}^{2}}+\frac{4 a^{2}}{(1+a)\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}}\right) \\
& +\frac{1}{t-4}\left(\frac{4 a^{2}}{\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}}+\frac{16 a^{2}\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}}{\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}^{3}}\right) \\
& +\frac{1}{t-4}\left(\frac{8 a^{2}}{\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}^{2}}\right),
\end{aligned}
$$

where

$$
\begin{aligned}
r_{m} & =(1+1 / m) \operatorname{tr}\left(B_{m} \bar{U}_{m}^{-1}\right) / k \\
v_{\mathrm{com}}^{*} & =\left(\frac{v_{\mathrm{com}}+1}{v_{\mathrm{com}}+3}\right) v_{\mathrm{com}} \\
t & =k(m-1) \\
a & =r_{m} t /(t-2)
\end{aligned}
$$

and $B_{m}$ and $\bar{U}_{m}$ are the usual multiple imputation quantities defined in §2. For moderately large values of $v_{\text {com }}$ and $t$, the first two terms in the expression for $z$ dominate, and this motivates the approximation

$$
v_{\mathrm{fapp}}=4+\left\{\frac{1}{v_{\mathrm{com}}^{*}-4(1+a)}+\frac{1}{t-4}\left(\frac{a^{2}\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}}{(1+a)^{2}\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}}\right)\right\}^{-1} .
$$

The derivation of $v_{\mathrm{f}}$ and $v_{\text {fapp }}$ uses some intermediate results of Barnard \& Rubin (1999), who derived an adjusted degrees of freedom for the reference $t$-distributions used for inferences in multiple imputation. They did not recommend an adjusted degrees of freedom for multi-component significance tests with modest sample sizes.

## 2 SIGNIFICANCE TESTS WITH MULTIPLE IMPUTATION

Using the $m$ imputed datasets, the analyst seeks inferences about some $k$-component estimand $Q$. For $l=1, \ldots, m$, in each $D^{(l)}$ let $Q^{(l)}$ be the $k \times 1$ estimator of $Q$, and let $U^{(l)}$ be the estimator of the $k \times k$ covariance matrix associated with $Q^{(l)}$. The
following quantities are needed for inference:

$$
\begin{aligned}
\bar{Q}_{m} & =\sum_{l=1}^{m} Q^{(l)} / m \\
B_{m} & =\sum_{l=1}^{m}\left(Q^{(l)}-\bar{Q}_{m}\right)\left(Q^{(l)}-\bar{Q}_{m}\right)^{\prime} /(m-1) \\
\bar{U}_{m} & =\sum_{l=1}^{m} U^{(l)} / m
\end{aligned}
$$

The analyst can estimate $Q$ using $\bar{Q}_{m}$ and can estimate the variance associated with $\bar{Q}_{m}$ using $T_{m}=\bar{U}_{m}+(1+1 / m) B_{m}$ (Rubin, 1987, Ch. 3).

As discussed by Rubin (1987, p. 98) and Li et al. (1991), the estimator $B_{m}$ can have large variance, especially when $k$ is large relative to $m$. These authors recommend that analysts test the null hypothesis that $Q=Q_{0}$ by using a Wald-like test statistic,

$$
W_{m}=\frac{\left(\bar{Q}_{m}-Q_{0}\right)^{\prime} \bar{U}_{m}^{-1}\left(\bar{Q}_{m}-Q_{0}\right)}{k\left(1+r_{m}\right)}
$$

As the reference distribution for $W_{m}$, they recommend using an $F$-distribution, $F_{k, v_{\mathrm{w}}}$, with $k$ degrees of freedom in the numerator and $v_{\mathrm{w}}$ degrees of freedom in the denominator, where

$$
v_{\mathrm{w}}=4+(t-4)\left(1+\frac{1-2 / t}{r_{m}}\right)^{2}
$$

when $t>4$. When $t \leq 4$, which does not often occur in practice, they recommend setting $v_{\mathrm{w}}=(m-1)\left(1+1 / r_{m}\right)^{2}(k+1) / 2$. The $p$-value for testing $Q=Q_{0}$ equals $\operatorname{pr}\left(F_{k, v_{\mathrm{w}}}>W_{m}\right)$.

The statistic $W_{m}$ and the reference $F$-distribution based on (5) are the standard for multi-component significance testing with multiply-imputed datasets. For example, they are implemented in the multiple imputation routines in the software packages SAS and Stata, and they are recommended by popular texts describing multiple imputation (Schafer, 1997, pp. 112-4; Little \& Rubin, 2002, pp. 212-3).

## 3 DERIVATION OF $v_{\mathrm{f}}$

### 3.1 Intermediate results when $m=\infty$

To derive $v_{\mathrm{f}}$, we use some results of Barnard \& Rubin (1999). Let $S_{m}=\left\{\bar{Q}_{m}, \bar{U}_{m}, B_{m}\right\}$. They approximate the conditional distribution of $Q$ given ( $S_{m}, B_{\infty}$ ), where $B_{\infty}$ is the value of $B_{m}$ if $m=\infty$, as

$$
\left(Q \mid S_{m}, B_{\infty}\right) \sim t_{v_{\mathrm{obs}}}\left\{\bar{Q}_{m}, \bar{U}_{m}+(1+1 / m) B_{\infty}\right\}
$$

where

$$
v_{\mathrm{obs}}=v_{\mathrm{com}}^{*} \operatorname{tr}\left\{\bar{U}_{m}\left(\bar{U}_{m}+B_{\infty}\right)^{-1}\right\} / k
$$

This approximation is reasonable provided that the complete data inferences would be derived from a $k$-variate $t$-distribution with $v_{\text {com }}$ degrees of freedom, that the $U^{(l)}$ can be considered fixed because they have less variability than the $Q^{(l)}$, so that it is reasonable to act as if $U^{(l)}=\bar{U}_{m}=\bar{U}_{\infty}$, and that $B_{\infty} / m$ is small relative to $\bar{U}_{m}+B_{\infty}$.

Barnard \& Rubin (1999) represent (6) as a mixture of normal distributions over the distribution of $T_{\infty, m}=\bar{U}_{m}+(1+1 / m) B_{\infty}$; that is,

$$
\begin{aligned}
\left(Q \mid S_{m}, B_{\infty}, T\right) & \sim N\left(\bar{Q}_{m}, T\right) \\
\left(v_{\mathrm{obs}} T_{\infty, m}^{1 / 2} T^{-1} T_{\infty, m}^{1 / 2} \mid S_{m}, B_{\infty}\right) & \sim \operatorname{Wi}\left(v_{\mathrm{obs}}, I\right),
\end{aligned}
$$

where $I$ is the identity matrix and $T$ is implicitly defined by (8) and (9). Thus, conditional on $\left(S_{m}, B_{\infty}, T\right)$, the $p$-value for the test of some multi-component null hypothesis, $Q=Q_{0}$, can be obtained from

$$
\operatorname{pr}\left\{\chi_{k}^{2}>\left(\bar{Q}_{m}-Q_{0}\right)^{\prime} T^{-1}\left(\bar{Q}_{m}-Q_{0}\right) \mid S_{m}, B_{\infty}, T\right\}
$$

where $\chi_{k}^{2}$ is a chi-squared random variable on $k$ degrees of freedom. We now need to integrate (10) over the distributions of $T$ and $B_{\infty}$ to obtain the $p$-value conditional only on $S_{m}$.

From (8) and (9), we integrate (10) over the distribution of ( $T \mid S_{m}, B_{\infty}$ ) as follows:

$$
\begin{aligned}
& \int \operatorname{pr}\left\{\chi_{k}^{2}>\left(\bar{Q}_{m}-Q_{0}\right)^{\prime} T_{\infty, m}^{-1 / 2}\left(T_{\infty, m}^{1 / 2} T^{-1} T_{\infty, m}^{1 / 2}\right) T_{\infty, m}^{-1 / 2}\left(\bar{Q}_{m}-Q_{0}\right) \mid S_{m}, B_{\infty}, T\right\} \\
& f\left(T \mid S_{m}, B_{\infty}\right) d T \\
= & \operatorname{pr}\left\{F_{k, v_{\mathrm{obs}}}>\left(\bar{Q}_{m}-Q_{0}\right)^{\prime} T_{\infty, m}^{-1}\left(\bar{Q}_{m}-Q_{0}\right) / k \mid S_{m}, B_{\infty}\right\} .
\end{aligned}
$$

Following Rubin (1987, pp. 96-8) and Li et al. (1991), we assume that that $B_{\infty}$ is proportional to $\bar{U}_{m}$, i.e. $B_{\infty}=r_{\infty} \bar{U}_{m}$, where $r_{\infty}$ is a scalar quantity, so that we can
write (11) as

$$
\begin{aligned}
& \operatorname{pr}\left(\left.F_{k, v_{\mathrm{obs}}}>\frac{\left(\bar{Q}_{m}-Q_{0}\right)^{\prime} \bar{U}_{m}^{-1}\left(\bar{Q}_{m}-Q_{0}\right)}{k\left\{1+(1+1 / m) r_{\infty}\right\}} \right\rvert\, S_{m}, r_{\infty}\right) \\
& =\operatorname{pr}\left(\left.F_{k, v_{\mathrm{obs}}} \frac{1+(1+1 / m) r_{\infty}}{1+r_{m}}>\frac{\left(\bar{Q}_{m}-Q_{0}\right)^{\prime} \bar{U}_{m}^{-1}\left(\bar{Q}_{m}-Q_{0}\right)}{k\left(1+r_{m}\right)} \right\rvert\, S_{m}, r_{\infty}\right)
\end{aligned}
$$

The test statistic in (12) equals $W_{m}$ from (4). We now need to integrate (12) over the distribution of $\left(r_{\infty} \mid S_{m}\right)$. The integral can be evaluated numerically, but it is desirable to have a closed-form approximation. First, we simplify the calculations by replacing $v_{\text {obs }}$ in ( 7 ) with

$$
v_{\mathrm{obs}, m}=v_{\mathrm{com}}^{*} \operatorname{tr}\left[\bar{U}_{m}\left\{\bar{U}_{m}+(1+1 / m) B_{\infty}\right\}^{-1}\right] / k
$$

that is, we add a $B_{\infty} / m$ to $\bar{U}_{m}+B_{\infty}$. This decreases the denominator degrees of freedom compared to $v_{\text {obs }}$ and so leads to conservative inferences. Under the proportionality assumption,

$$
v_{\mathrm{obs}, m}=v_{\mathrm{com}}^{*} /\left\{1+(1+1 / m) r_{\infty}\right\}
$$

From (12) and (13),

$$
\begin{aligned}
F_{k, v_{\mathrm{obs}}} \frac{1+(1+1 / m) r_{\infty}}{1+r_{m}} & \bumpeq F_{k, v_{\mathrm{obs}, m}} \frac{1+(1+1 / m) r_{\infty}}{1+r_{m}} \\
& =\left(\frac{\chi_{k}^{2} / k}{\chi_{v_{\mathrm{obs}, m}}^{2} / v_{\mathrm{obs}, m}}\right)\left(\frac{1+(1+1 / m) r_{\infty}}{1+r_{m}}\right) \\
& =\left(\frac{v_{\mathrm{com}}^{*}}{1+r_{m}}\right)\left(\frac{\chi_{k}^{2} / k}{\chi_{v_{\mathrm{obs}, m}}^{2}}\right)
\end{aligned}
$$

Following Li et al. (1991), we approximate the distribution in (14) as a multiple of an $F$ distribution, $\delta F_{k, w}$. The approximation matches the first two moments of $\delta F_{k, w}$ with approximations to the first two moments of $\left\{v_{\text {com }}^{*} /\left(1+r_{m}\right)\right\}\left\{\left(\chi_{k}^{2} / k\right) / \chi_{v_{\text {obs }, m}}^{2}\right\}$.

### 3.2 Approximation of first moment

To approximate the first moment of the expression in (14), we use an iterated expectation, conditioning on $\left(S_{m}, r_{\infty}\right)$ for the inner expectation. Since the expectation of $1 / \chi_{v_{\mathrm{obs}, m}}^{2}$ equals $1 /\left(v_{\mathrm{obs}, m}-2\right)$,

$$
E\left(\left.\frac{\chi_{k}^{2} / k}{\chi_{v_{\mathrm{obs}, m}}^{2}} \right\rvert\, S_{m}, r_{\infty}\right)=\frac{\chi_{k}^{2} / k}{v_{\mathrm{obs}, m}-2}=\frac{\chi_{k}^{2} / k}{v_{\mathrm{com}}^{*} /\left\{1+(1+1 / m) r_{\infty}\right\}-2} .
$$

From Rubin (1987, p. 97), when $B_{\infty}=r_{\infty} \bar{U}_{m}$,

$$
\left(\left.\frac{k(m-1) \operatorname{tr}\left(B_{m} \bar{U}_{m}^{-1}\right) / k}{r_{\infty}} \right\rvert\, S_{m}\right) \sim \chi_{k(m-1)}^{2} .
$$

Substituting (16) into (15), and using $r_{m}$ and $t$ as defined in §1, we obtain

$$
\frac{\chi_{k}^{2} / k}{v_{\mathrm{com}}^{*} /\left\{1+(1+1 / m) r_{\infty}\right\}-2}=\frac{\chi_{k}^{2} / k}{v_{\mathrm{com}}^{*} /\left(1+r_{m} t / \chi_{t}^{2}\right)-2} .
$$

Using the first term in a Taylor series expansion of (17) in $1 / \chi_{t}^{2}$ around its expectation $1 /(t-2)$, we arrive at an expression for the first moment:

$$
E\left(\left.\frac{\left(\chi_{k}^{2} / k\right) v_{\text {com }}^{*} /\left(1+r_{m}\right)}{v_{\text {com }}^{*} /\left(1+r_{m} t / \chi_{t}^{2}\right)-2} \right\rvert\, S_{m}\right) \bumpeq \frac{v_{\text {com }}^{*} /\left(1+r_{m}\right)}{v_{\text {com }}^{*} /\left\{1+r_{m} t /(t-2)\right\}-2} .
$$

### 3.3 Approximation of second moment

To approximate the second moment of the expression in (14), we again use an iterated expectation, conditioning on $\left(S_{m}, r_{\infty}\right)$ for the inner expectation. Since the expectation of $\left(1 / \chi_{v_{\mathrm{obs}, m}}^{2}\right)^{2}$ equals $1 /\left\{\left(v_{\mathrm{obs}, m}-2\right)\left(v_{\mathrm{obs}, m}-4\right)\right\}$, we have

$$
\begin{aligned}
& E\left\{\left.\left(\left\{v_{\mathrm{com}}^{*} /\left(1+r_{m}\right)\right\} \frac{\chi_{k}^{2} / k}{\chi_{v_{\mathrm{obs}, m}}^{2}}\right)^{2} \right\rvert\, S_{m}, r_{\infty}\right\}=\left\{v_{\mathrm{com}}^{*} /\left(1+r_{m}\right)\right\}^{2} \frac{\left(\chi_{k}^{2} / k\right)^{2}}{\left(v_{\mathrm{obs}, m}-2\right)\left(v_{\mathrm{obs}, m}-4\right)} \\
& =\left\{v_{\mathrm{com}}^{*} /\left(1+r_{m}\right)\right\}^{2} \frac{\left(\chi_{k}^{2} / k\right)^{2}}{\left\{v_{\mathrm{com}}^{*} /\left(1+r_{m} t / \chi_{t}^{2}\right)-2\right\}\left\{v_{\mathrm{com}}^{*} /\left(1+r_{m} t / \chi_{t}^{2}\right)-4\right\}}
\end{aligned}
$$

We approximate the expectation of (19) using the first three terms in a Taylor series expansion of (19) in $1 / \chi_{t}^{2}$ around its expectation $1 /(t-2)$. Ignoring the $\left\{v_{\text {com }}^{*} /(1+\right. \left.\left.r_{m}\right)\right\}^{2}$ temporarily, we have

$$
\begin{aligned}
& E\left(\left.\frac{\left(\chi_{k}^{2} / k\right)^{2}}{\left\{v_{\text {com }}^{*} /\left(1+r_{m} t / \chi_{t}^{2}\right)-2\right\}\left\{v_{\text {com }}^{*} /\left(1+r_{m} t / \chi_{t}^{2}\right)-4\right\}} \right\rvert\, S_{m}\right) \\
\bumpeq & \frac{k(k+2)}{k^{2}}\left[H\{1 /(t-2)\}+\frac{1}{2} H^{\prime \prime}\{1 /(t-2)\} E\left\{\left.\left(\frac{1}{\chi_{t}^{2}}-\frac{1}{t-2}\right)^{2} \right\rvert\, S_{m}\right\}\right] \\
= & \frac{k(k+2)}{k^{2}}\left(H\{1 /(t-2)\}+\frac{1}{2} H^{\prime \prime}\{1 /(t-2)\} \frac{2}{(t-2)^{2}(t-4)}\right),
\end{aligned}
$$

where $H\{1 /(t-2)\}$ and $H^{\prime \prime}\{1 /(t-2)\}$ are respectively the first term and second derivative in the expansion. The term associated with the first derivative disappears because we are expanding around $E\left(1 / \chi_{t}^{2}\right)$.

The first term in the expansion is

$$
H\left(\frac{1}{t-2}\right)=\frac{1}{\left[v_{\mathrm{com}}^{*} /\left\{1+r_{m} t /(t-2)\right\}-2\right]\left[v_{\mathrm{com}}^{*} /\left\{1+r_{m} t /(t-2)\right\}-4\right]} .
$$

The second derivative, written here using $a$ as defined in § 1 and $c=r_{m} t$, is

$$
\begin{aligned}
H^{\prime \prime}\left(\frac{1}{t-2}\right)= & \frac{2 c^{2}}{\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}} \\
& +\frac{16 c^{2}(1+a)}{\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}^{2}} \\
& +\frac{8 c^{2}(1+a)}{\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}^{2}\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}} \\
& +\frac{8 c^{2}(1+a)^{2}}{\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}^{3}} \\
& +\frac{32 c^{2}(1+a)^{2}}{\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}^{3}} \\
& +\frac{16 c^{2}(1+a)^{2}}{\left\{v_{\mathrm{com}}^{*}-2(1+a)\right\}^{2}\left\{v_{\mathrm{com}}^{*}-4(1+a)\right\}^{2}}
\end{aligned}
$$

The second moment is found by substituting (21) and (22) in (20). For brevity, it is not repeated here. We note that multiplication of (22) by the $1 /(t-2)^{2}$ in (20) allows us to replace $c^{2}$ with $a^{2}$ in the final form of $v_{\mathrm{f}}$.

### 3.4 Final form of $v_{f}$

We now set these two moments from (18) and (20) equal to the first two moments of $\delta F_{k, w}$, which are

$$
\begin{aligned}
E\left(\delta F_{k, w} \mid S_{m}\right) & =\delta w /(w-2) \\
E\left(\delta^{2} F_{k, w}^{2}\right) & =\delta^{2}(w / k)^{2} k(k+2) /\{(w-2)(w-4)\}
\end{aligned}
$$

Solving, we obtain

$$
\delta=(1-2 / w) \frac{v_{\mathrm{com}}^{*} /\left(1+r_{m}\right)}{v_{\mathrm{com}}^{*} /\left\{1+r_{m} t /(t-2)\right\}-2}
$$

and $w=v_{\mathrm{f}}$ as defined in (1) and (2). Setting $\delta=1$, as will be approximately the case for reasonably large $v_{\text {com }}^{*}$ and $t$, results in the reference distribution $F_{k, v_{\mathrm{f}}}$.

## 4 ILLUSTRATIVE SIMULATIONS

This section illustrates the improved performance of the adjusted degrees of freedom using simulations. The setting is to test whether or not some $k$ linear regression coefficients equal zero. The predictors are generated from a $k$-variate normal distribution with a mean equal to zero and a covariance matrix with one on all diagonals and 0.5
on all off-diagonals. The response is generated independently from a normal distribution with mean zero and variance equal to one. We examine two settings, one based on a small sample in which $n_{\text {com }}=50$ and $k=4$ and one based on a moderately large sample in which $n_{\text {com }}=200$ and $k=9$. Missing data are generated by randomly deleting $10 \%$ of all values in the generated dataset. The missing data are imputed using the routine 'proc MI' in SAS, which completes the missing data via by drawing augmentation from a multivariate normal distribution. There are $m=5$ completed datasets for both simulations.

For each completed dataset $l=1, \ldots, m$, let $\hat{\beta}^{(l)}$ be the estimate of the $k$ coefficients of interest, and let $\hat{U}^{(l)}$ be the $k \times k$ covariance matrix associated with those coefficients. Let $\bar{\beta}=\sum_{l=1}^{m}=\hat{\beta}^{(l)}$. The test statistic is $W_{m}=\bar{\beta}^{\prime} \bar{U}_{m}^{-1} \bar{\beta} /\left\{k\left(1+r_{m}\right)\right\}$. The complete-data degrees of freedom, $v_{\text {com }}$, equals $n_{\text {com }}-k$.

Table 1 displays simulated significance levels when using $W_{m}$ and reference $F$ distributions based on $v_{\mathrm{f}}$ from (1) and (2), and on $v_{\mathrm{w}}$ from (5) of Li et al. (1991). It also displays the simulated levels when using $v_{\text {fapp }}$ from (3). The simulated levels are computed from 10,000 independent runs of the simulation. The inferences based on $v_{\mathrm{f}}$ or $v_{\text {fapp }}$ are better calibrated than those based on $v_{\mathrm{w}}$. The $v_{\mathrm{w}}$ in both settings on average is substantially larger than $v_{\text {com }}$, which results in the anti-conservative nature of the $F$-test based on $v_{\mathrm{w}}$. Inferences based on $v_{\text {fapp }}$ are only slightly less well calibrated than inferences based on $v_{\mathrm{f}}$.

These illustrative simulations, coupled with the theoretical results, suggest that
using $v_{\mathrm{f}}$ or $v_{\text {fapp }}$ leads to better calibrated inferences than does using $v_{\mathrm{w}}$ when performing multi-component significance tests with multiply-imputed data. In addition to improving testing for multiple imputation for missing data, the approach used to derive the denominator degrees of freedom might lead to improved testing when multiple imputation is used for protecting data confidentiality (Raghunathan et al., 2003; Reiter, 2005). This is an area for further research.

## 5 ACKNOWLEDGEMENT

This research was supported by a grant from the U.S. National Science Foundation.

## References

BARNARD, J. \& RUBIN, D. B. (1999). Small sample degrees of freedom with multiple imputation. Biometrika 86, 948-55.

HEITJAN, D. F. \& LITTLE, R. J. A. (1991). Multiple imputation for the Fatal Accident Reporting System. Appl. Statist. 40, 13-29.

LI, K. H., RAGHUNATHAN, T. E. \& RUBIN, D. B. (1991). Large sample significance levels from multiply imputed data using moment-based statistics and an $f$ reference distribution. J. Am. Statist. Assoc. 86, 1065-73.

LITTLE, R. J. A. \& RUBIN, D. B. (2002). Statistical Analysis with Missing Data, 2nd ed. New York: John Wiley \& Sons.

MENG, X. L. \& RUBIN, D. B. (1992). Performing likelihood ratio tests with multiplyimputed data sets. Biometrika 79, 103-11.

RAGHUNATHAN, T. E., LEPKOWSKI, J. M., VAN HOEWYK, J. \& SOLENBERGER, P. (2001). A multivariate technique for multiply imputing missing values using a series of regression models. Survey Methodol. 27, 85-96.

RAGHUNATHAN, T. E. \& PAULIN, G. S. (1998). Multiple imputation of income in the Consumer Expenditure Survey: Evaluation of statistical inference. In Proceedings of the Section on Business \& Economic Statistics of the American Statistical Association, pp. 1-10. Alexandria: Am. Statist. Assoc.

RAGHUNATHAN, T. E., REITER, J. P. \& RUBIN, D. B. (2003). Multiple imputation for statistical disclosure limitation. J. of Offic. Statist. 19, 1-16.

REITER, J. P. (2005). Significance tests for multi-component estimands from multiply-imputed, synthetic microdata. J. of Statist. Plan. and Infer. 131, 365-77.

RUBIN, D. B. (1987). Multiple Imputation for Nonresponse in Surveys. New York: John Wiley \& Sons.

SCHAFER, J. L. (1997). Analysis of Incomplete Multivariate Data. Boca Raton: Chapman and Hall.

SCHAFER, J. L., EZZATI-RICE, T. M., JOHNSON, W., KHARE, M., LITTLE, R. J. A. \& RUBIN, D. B. (1998). The NHANES III multiple imputation project. In Proceedings of the Section on Survey Research Methods of the American Statistical Association, pp. 28-37. Alexandria: Am. Statist. Assoc.

Table 1: Simulated significance levels for testing regression coefficients.
| Scenario | Avg. df | $\alpha=0.10$ | $\alpha=0.05$ | $\alpha=0.01$ |
| :--- | :--- | :--- | :--- | :--- |
| $n_{\text {com }}=50, k=4$ |  |  |  |  |
| $v_{f}$ | 32.8 | 0.103 | 0.054 | 0.012 |
| $v_{\text {fapp }}$ | 34.8 | 0.105 | 0.057 | 0.012 |
| $v_{\mathrm{w}}$ | 384.4 | 0.127 | 0.072 | 0.020 |
| $n_{\text {com }}=200, k=9$ |  |  |  |  |
| $v_{f}$ | 138.9 | 0.108 | 0.056 | 0.012 |
| $v_{\text {approx }}$ | 141.4 | 0.108 | 0.056 | 0.012 |
| $v_{\mathrm{w}}$ | 673.2 | 0.117 | 0.064 | 0.016 |


