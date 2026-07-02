---
citekey: efronBootstrapMethodsAnother1979
item_type: article
authors: 'Efron, B.'
year: 1979
title: 'Bootstrap {Methods}: {Another Look} at the {Jackknife}'
venue: The Annals of statistics
publisher: Institute of Mathematical Statistics
volume: 7
issue: 1
pages: 1--26
doi: 10.1214/aos/1176344552
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\efron_bootstrap_methods_another_1979.pdf'
pdf_sha256: 96fc5600d047117aebba6c7415fe3457772d8a3a7bea20785a564f6eae2910ff
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-07-02T21:12:38Z
---
# THE 1977 RIETZ LECTURE 

# BOOTSTRAP METHODS: ANOTHER LOOK AT THE JACKKNIFE 

By B. Efron<br>Stanford University


#### Abstract

We discuss the following problem: given a random sample $\mathbf{X}= \left(X_{1}, X_{2}, \ldots, X_{n}\right)$ from an unknown probability distribution $F$, estimate the sampling distribution of some prespecified random variable $R(\mathbf{X}, F)$, on the basis of the observed data $\mathbf{x}$. (Standard jackknife theory gives an approximate mean and variance in the case $R(\mathbf{X}, F)=\theta(\hat{F})-\theta(F), \theta$ some parameter of interest.) A general method, called the "bootstrap," is introduced, and shown to work satisfactorily on a variety of estimation problems. The jackknife is shown to be a linear approximation method for the bootstrap. The exposition proceeds by a series of examples: variance of the sample median, error rates in a linear discriminant analysis, ratio estimation, estimating regression parameters, etc.


1. Introduction. The Quenouille-Tukey jackknife is an intriguing nonparametric method for estimating the bias and variance of a statistic of interest, and also for testing the null hypothesis that the distribution of a statistic is centered at some prespecified point. Miller [14] gives an excellent review of the subject.

This article attempts to explain the jackknife in terms of a more primitive method, named the "bootstrap" for reasons which will become obvious. In principle, bootstrap methods are more widely applicable than the jackknife, and also more dependable. In Section 3, for example, the bootstrap is shown to (asymptotically) correctly estimate the variance of the sample median, a case where the jackknife is known to fail. Section 4 shows the bootstrap doing well at estimating the error rates in a linear discrimination problem, outperforming "cross-validation," another nonparametric estimation method.

We will show that the jackknife can be thought of as a linear expansion method (i.e., a "delta method") for approximating the bootstrap. This helps clarify the theoretical basis of the jackknife, and suggests improvements and variations likely to be successful in various special situations. Section 3, for example, discusses jackknifing (or bootstrapping) when one is willing to assume symmetry or smoothness of the underlying probability distribution. This point reappears more emphatically in Section 7, which discusses bootstrap and jackknife methods for regression models.

The paper proceeds by a series of examples, with little offered in the way of general theory. Most of the examples concern estimation problems, except for Remark F of Section 8, which discusses Tukey's original idea for $t$-testing using the

[^0]www.jstor.org
jackknife. The bootstrap results on this point are mixed (and won't be reported here), offering only slight encouragement for the usual jackknife $t$ tests.

John Hartigan, in an important series of papers [5, 6, 7], has explored ideas closely related to what is called bootstrap "Method 2" in the next section, see Remark I of Section 8. Maritz and Jarrett [13] have independently used bootstrap "Method 1" for estimating the variance of the sample median, deriving equation (3.4) of this paper and applying it to the variance calculation. Bootstrap "Method 3," the connection to the jackknife via linear expansions, relates closely to Jaeckel's work on the infinitesimal jackknife [10]. If we work in a parametric framework, this approach to the bootstrap gives Fisher's information bound for the asymptotic variance of the maximum likelihood estimator, see Remark K of Section 8.
2. Bootstrap methods. We discuss first the one-sample situation in which a random sample of size $n$ is observed from a completely unspecified probability distribution $F$,

$$
X_{i}=x_{i}, \quad X_{i} \sim_{\text {ind }} F \quad i=1,2, \ldots, n .
$$

In all of our examples $F$ will be a distribution on either the real line or the plane, but that plays no role in the theory. We let $\mathbf{X}=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ and $\mathbf{x}= \left(x_{1}, x_{2}, \ldots, x_{n}\right)$ denote the random sample and its observed realization, respectively.

The problem we wish to solve is the following. Given a specified random variable $R(\mathbf{X}, F)$, possibly depending on both $\mathbf{X}$ and the unknown distribution $F$, estimate the sampling distribution of $R$ on the basis of the observed data $\mathbf{x}$.

Traditional jackknife theory focuses on two particular choices of $R$. Let $\theta(F)$ be some parameter of interest such as the mean, correlation, or standard deviation of $F$, and $t(\mathbf{X})$ be an estimator of $\theta(F)$, such as the sample mean, sample correlation, or a multiple of the sample range. Then the sampling distribution of

$$
R(\mathbf{X}, F)=t(\mathbf{X})-\theta(F),
$$

or more exactly its mean (the bias of $t$ ) and variance, is estimated using the standard jackknife theory, as described in Section 5. The bias and variance estimates say $\widehat{\operatorname{Bias}}(t)$ and $\widehat{\operatorname{Var}}(t)$, are cleverly constructed functions of $\mathbf{X}$ obtained by recomputing $t(\cdot) n$ times, each time removing one component of $\mathbf{X}$ from consideration. The second traditional choice of $R$ is

$$
R(\mathbf{X}, F)=\frac{t(\mathbf{X})-\widehat{\operatorname{Bias}}(t)-\theta(F)}{(\widehat{\operatorname{Var}}(t))^{\frac{1}{2}}} .
$$

Tukey's original suggestion was to treat (2.3) as having a standard Student's $t$ distribution with $n-1$ degrees of freedom. (See Remark F, Section 8.) Random variables (2.2), (2.3) play no special role in the bootstrap theory, and, as a matter of fact, some of our examples concern other choices of $R$.

The bootstrap method for the one-sample problem is extremely simple, at least in principle:

1. Construct the sample probability distribution $\hat{F}$, putting mass $1 / n$ at each point $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$.
2. With $\hat{F}$ fixed, draw a random sample of size $n$ from $\hat{F}$, say

$$
X_{i}^{*}=x_{i}^{*}, X_{i}^{*} \sim_{\text {ind }} \hat{F} \quad i=1,2, \cdots, n
$$

Call this the bootstrap sample, $\mathbf{X}^{*}=\left(X_{1}^{*}, X_{2}^{*}, \cdots, X_{n}^{*}\right), \mathbf{x}^{*}=\left(x_{1}^{*}, x_{2}^{*}, \cdots, x_{n}^{*}\right)$. Notice that we are not getting a permutation distribution since the values of $\mathbf{X}^{*}$ are selected with replacement from the set $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$. As a point of comparison, the ordinary jackknife can be thought of as drawing samples of size $n-1$ without replacement.
3. Approximate the sampling distribution of $R(\mathbf{X}, F)$ by the bootstrap distribution of

$$
R^{*}=R\left(\mathbf{X}^{*}, \hat{F}\right),
$$

i.e., the distribution of $R^{*}$ induced by the random mechanism (2.4), with $\hat{F}$ held fixed at its observed value.

The point is that the distribution of $R^{*}$, which in theory can be calculated exactly once the data $\mathbf{x}$ is observed, equals the desired distribution of $R$ if $F=\hat{F}$. Any nonparametric estimator of $R$ 's distribution, i.e., one that does a reasonably good estimation job without prior restrictions on the form of $F$, must give close to the right answer when $F=\hat{F}$, since $\hat{F}$ is a central point amongst the class of likely $F$ 's, having observed $\mathbf{X}=\mathbf{x}$. Making the answer exactly right for $F=\hat{F}$ is Fisher consistency applied to our particular estimation problem.

Just how well the distribution of $R^{*}$ approximates that of $R$ depends upon the form of $R$. For example, $R(\mathbf{X}, F)=t(\mathbf{X})$ might be expected to bootstrap less successfully than $R(\mathbf{X}, F)=\left[t(\mathbf{X})-E_{F} t\right] /\left(\operatorname{Var}_{F} t\right)^{\frac{1}{2}}$. This is an important question, related to the concept of pivotal quantities, Barnard [2], but is discussed only briefly here, in Section 8. Mostly we will be content to let the varying degrees of success of the examples speak for themselves.

As the simplest possible example of the bootstrap method, consider a probability distribution $F$ putting all of its mass at zero or one, and let the parameter of interest be $\theta(F)=\operatorname{Prob}_{F}\{X=1\}$. The most obvious random variable of interest is

$$
R(\mathbf{X}, F)=\bar{X}-\theta(F) \quad \bar{X}=\left(\sum_{i=1}^{n} X_{i} / n\right) .
$$

Having observed $\mathbf{X}=\mathbf{x}$, the bootstrap sample $\mathbf{X}^{*}=\left(X_{1}^{*}, X_{2}^{*}, \ldots, X_{n}^{*}\right)$ has each component independently equal to one with probability $\bar{x}=\theta(\hat{F})$, zero with probability $1-\bar{x}$. Standard binomial results show that

$$
R^{*}=R\left(\mathbf{X}^{*}, \hat{F}\right)=\bar{X}^{*}-\bar{x}
$$

has mean and variance

$$
E_{*}\left(\bar{X}^{*}-\bar{x}\right)=0, \quad \operatorname{Var}_{*}\left(\bar{X}^{*}-\bar{x}\right)=\bar{x}(1-\bar{x}) / n
$$

(Notations such as " $E_{*}$," "Var," "Prob, " etc. indicate probability calculations relating to the bootstrap distribution of $\mathbf{X}^{*}$, with $\mathbf{x}$ and $\hat{F}$ fixed.) The implication that $\bar{X}$ is unbiased for $\theta$, with variance approximately equal to $\bar{x}(1-\bar{x}) / n$, is universally familiar.

As a second example, consider estimating $\theta(F)=\operatorname{Var}_{F} X$, the variance of an arbitrary distribution on the real line, using the estimator $t(\mathbf{X})=\sum_{i=1}^{n}\left(X_{i}-\right. \bar{X})^{2} /(n-1)$. Perhaps we wish to know the sampling distribution of

$$
R(\mathbf{X}, F)=t(\mathbf{X})-\theta(F)
$$

Let $\mu_{k}(F)$ indicate the $k$ th central moment of $F, \mu_{k}(F)=E_{F}\left(X-E_{F} X\right)^{k}$, and $\hat{\mu}_{k}=\mu_{k}(\hat{F})$, the $k$ th central moment of $\hat{F}$. Standard sampling theory results, as in Cramér [3], Section 27.4, show that

$$
R^{*}=R\left(\mathbf{X}^{*}, \hat{F}\right)=t\left(\mathbf{X}^{*}\right)-\theta(\hat{F})
$$

has

$$
E_{*} R^{*}=0, \quad \operatorname{Var}_{*} R^{*}=\frac{\hat{\mu}_{4}-((n-3) /(n-1)) \hat{\mu}_{2}^{2}}{n} .
$$

The approximation $\operatorname{Var}_{F} t(\mathbf{X}) \approx \operatorname{Var}_{*} R^{*}$ is (almost) the jackknife estimate for $\operatorname{Var}_{F} t$.

The difficult part of the bootstrap procedure is the actual calculation of the bootstrap distribution. Three methods of calculation are possible:
Method 1. Direct theoretical calculation, as in the two examples above and the example of the next section.

Method 2. Monte Carlo approximation to the bootstrap distribution. Repeated realizations of $\mathbf{X}^{\boldsymbol{*}}$ are generated by taking random samples of size $n$ from $\hat{F}$, say $\mathbf{x}^{\boldsymbol{*} \mathbf{1}}, \mathbf{x}^{\boldsymbol{*} \mathbf{2}}, \ldots, \mathbf{x}^{\boldsymbol{*} \boldsymbol{N}}$, and the histogram of the corresponding values $R\left(\mathbf{x}^{* 1}, \hat{F}\right), R\left(\mathbf{x}^{* 2}, \hat{F}\right), \ldots, R\left(\mathbf{x}^{* N}, \hat{F}\right)$ is taken as an approximation to the actual bootstrap distribution. This approach is illustrated in Sections 3, 4 and 8.

Method 3. Taylor series expansion methods can be used to obtain the approximate mean and variance of the bootstrap distribution of $R^{*}$. This turns out to be the same as using some form of the jackknife, as shown in Section 5.
In Section 4 we consider a two sample problem where the data consists of a random sample $\mathbf{X}=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ from $F$ and an independent random sample $\mathbf{Y}=\left(Y_{1}, Y_{2}, \ldots, Y_{n}\right)$ from $G, F$ and $G$ arbitrary probability distributions on a given space. In order to estimate the sampling distribution of a random variable $R((\mathbf{X}, \mathbf{Y}),(F, G))$, having observed $\mathbf{X}=\mathbf{x}, \mathbf{Y}=\mathbf{y}$, the one-sample bootstrap method can be extended in the obvious way: $\hat{F}$ and $\hat{G}$, the sample probability distributions corresponding to $F$ and $G$, are constructed; bootstrap samples $X_{i}{ }^{*} \sim \hat{F}, i= 1,2, \ldots, m, Y_{j}^{*} \sim \hat{G}, j=1,2, \ldots, n$, are independently drawn; and finally the bootstrap distribution of $R^{*}=R\left(\left(\mathbf{X}^{*}, Y^{*}\right),(\hat{F}, \hat{G})\right)$ is calculated, for use as an approximation to the actual distribution of $R$. The calculation of the bootstrap distribution proceeds by any of the three methods listed above. (The third method
makes clear the correct analogue of the jackknife procedure for nonsymmetric situations, such as the two sample problem; see the remarks of Section 6.)

So far we have only used nonparametric maximum likelihood estimators, $\hat{F}$ and ( $\hat{F}, \hat{G}$ ), to begin the bootstrap procedure. This isn't crucial, and as the examples of Sections 3 and 7 show, it is sometimes more convenient to use other estimates of the underlying distributions.
3. Estimating the median. Suppose we are in the one-sample situation (2.1), with $F$ a distribution on the real line, and we wish to estimate the median of $F$ using the sample median. Let $\theta(F)$ indicate the median of $F$, and let $t(\mathbf{X})$ be the sample median,

$$
t(\mathbf{X})=X_{(m)}
$$

where $X_{(1)} \leqslant X_{(2)} \leqslant \cdots \leqslant X_{(n)}$ is the order statistic, and we have assumed an odd sample size $n=2 m-1$ for convenience. Once again we take $R(\mathbf{X}, F)=t(\mathbf{X})- \theta(F)$, and hope to say something about the sampling distribution of $R$ on the basis of the observed random sample.

Having observed $\mathbf{X}=\mathbf{x}$, we construct the bootstrap sample $\mathbf{X}^{\boldsymbol{*}}=\mathbf{x}^{\boldsymbol{*}}$ as in (2.4). Let

$$
N_{i}^{*}=\sharp\left\{X_{i}^{*}=x_{i}\right\}
$$

the number of times $x_{i}$ is selected in the bootstrap sampling procedure. The vector $\mathbf{N}^{*}=\left(N_{1}^{*}, N_{2}^{*}, \cdots, N_{n}^{*}\right)$ has a multinomial distribution with expectation one in each of the $n$ cells.

Denote the observed order statistic $x_{(1)} \leqslant x_{(2)} \leqslant x_{(3)} \leqslant \cdots \leqslant x_{(n)}$, and the corresponding $N^{*}$ values $N_{(1)}^{*}, N_{(2)}^{*}, \cdots, N_{(n)}^{*}$. (Ties $x_{i}=x_{i^{\prime}}$ can be broken by assigning the lower value of $i, i^{\prime}$ to the lower position in the order statistic.) The bootstrap value of $R$ is

$$
R^{*}=R\left(\mathbf{X}^{*}, \hat{F}\right)=X_{(m)}^{*}-x_{(m)}
$$

We notice that for any integer value $l, 1 \leqslant l<n$,

$$
\begin{aligned}
\operatorname{Prob}_{*}\left\{X_{(m)}^{*}>x_{(l)}\right\} & =\operatorname{Prob}_{*}\left\{N_{(1)}^{*}+N_{(2)}^{*}+\cdots+N_{(l)}^{*} \leqslant m-1\right\} \\
& =\operatorname{Prob}\left\{\operatorname{Binomial}\left(n, \frac{l}{n}\right) \leqslant m-1\right\} \\
& =\sum_{j=0}^{m-1}\binom{n}{j}\left(\frac{l}{n}\right)^{j}\left(\frac{n-l}{n}\right)^{n-j} .
\end{aligned}
$$

Therefore

$$
\begin{aligned}
\operatorname{Prob}_{*}\left\{R^{*}=x_{(l)}-x_{(m)}\right\}= & \operatorname{Prob}\left\{\operatorname{Binomial}\left(n, \frac{l-1}{n}\right) \leqslant m-1\right\} \\
& -\operatorname{Prob}\left\{\operatorname{Binomial}\left(n, \frac{l}{n}\right) \leqslant m-1\right\}
\end{aligned}
$$

a result derived independently by Maritz and Jarrett [13].

The case $n=13(m=7)$ gives the following bootstrap distribution for $R^{*}$ :

$$
\begin{array}{ccccccc}
l= & 2 \text { or } 12 & 3 \text { or } 11 & 4 \text { or } 10 & 5 \text { or } 9 & 6 \text { or } 8 & 7 \\
\hline(3.5)= & .0015 & .0142 & .0550 & .1242 & .1936 & .2230
\end{array} .
$$

For any given random sample of size 13 we can compute

$$
E_{*}\left(R^{*}\right)^{2}=\sum_{l=1}^{13}\left[x_{(l)}-x_{(7)}\right]^{2} \operatorname{Prob}_{*}\left\{R^{*}=x_{(l)}-x_{(7)}\right\},
$$

and use this number as an estimate of $E_{F} R^{2}=E_{F}[t(\mathbf{X})-\theta(F)]^{2}$, the expected squared error of estimation for the sample median. Standard asymptotic theory, applied to the case where $F$ has a bounded continuous density $f(x)$, shows that as the sample size $n$ goes to infinity, the quantity $n E_{*}\left(R^{*}\right)^{2}$ approaches $1 / 4 f^{2}(\theta)$, where $f(\theta)$ is the density evaluated at the median $\theta(F)$. This is the correct asymptotic value, see Kendall and Stuart [11], page 237. The standard jackknife applied to the sample median gives a variance estimate which is not even asymptotically consistent (Miller [14], page 8, is incorrect on this point): $n \widehat{\operatorname{Var}}(R) \rightarrow \left(1 / 4 f^{2}(\theta)\right)\left[\chi_{2}^{2} / 2\right]^{2}$. The random variable $\left[\chi_{2}^{2} / 2\right]^{2}$ has mean 2 and variance 20.

Suppose we happened to know that the probability distribution $F$ was symmetric. In that case we could replace $\hat{F}$ by the symmetric probability distribution obtained from $\hat{F}$ by reflection about the median,

$$
\begin{aligned}
\hat{F}_{\mathrm{SYM}}: \quad \text { probability mass } \frac{1}{2 n-1} \text { at } & x_{(1)}, x_{(2)}, \ldots, x_{(n)} \quad \text { and } \\
& 2 x_{(m)}-x_{(1)}, \ldots, 2 x_{(m)}-x_{(n)} .
\end{aligned}
$$

This is not the nonparametric maximum likelihood estimator for $F$, but has similar asymptotic properties, see Hinkley [8]. Let $z_{(1)} \leqslant z_{(2)} \leqslant \cdots \leqslant z_{(2 n-1)}$ be the ordered values appearing in the distribution of $\hat{F}_{\text {SYM }}$. The bootstrap procedure starting from $\hat{F}_{\text {SYM }}$ gives

$$
\begin{aligned}
\operatorname{Prob}_{*}\left\{R^{*}=z_{(l)}-x_{(m)}\right\}= & \operatorname{Prob}\left\{\operatorname{Binomial}\left(n, \frac{l-1}{2 n-1}\right) \leqslant m-1\right\} \\
& -\operatorname{Prob}\left\{\operatorname{Binomial}\left(n, \frac{l}{2 n-1}\right) \leqslant m-1\right\},
\end{aligned}
$$

by the same argument leading to (3.5). For $n=13$ the bootstrap probabilities (3.9) equal

$$
\begin{array}{cccccc}
l= & 4 \text { or } 22 & 5 \text { or } 21 & 6 \text { or } 20 & 7 \text { or } 19 & 8 \text { or } 18 \\
\hline(3.9)= & .0016 & .0051 & .0125 & .0245 & .0414 \\
l= & 9 \text { or } 17 & 10 \text { or } 16 & 11 \text { or } 15 & 12 \text { or } 14 & 13 \\
\hline(3.9)= & .0614 & .0820 & .1002 & .1125 & .1170
\end{array}
$$

The corresponding estimate of $E_{F} R^{2}$ would be $\sum_{l=1}^{25}\left[z_{(l)}-x_{(7)}\right]^{2} \operatorname{Prob}_{*}\left\{R^{*}=z_{(l)}\right. \left.-x_{(7)}\right\}$.
Usually we would not be willing to assume $F$ symmetric in a nonparametric estimation situation. However in dealing with continuous variables we might be
willing to attribute a moderate amount of smoothness to $F$. This can be incorporated into the bootstrap procedure at step (2.4). Instead of choosing each $X_{i}^{*}$ randomly from the set $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$, we can take

$$
X_{i}^{*}=\bar{x}+c\left[x_{I_{i}}-\bar{x}+\hat{\sigma} Z_{i}\right]
$$

where the $I_{i}$ are chosen independently and randomly from the set $\{1,2, \ldots, n\}$, and the $Z_{i}$ are a random sample from some fixed distribution having mean 0 and variance $\sigma_{Z}^{2}$, for example the uniform distribution on $\left[-\frac{1}{2}, \frac{1}{2}\right]$, which has $\sigma_{Z}^{2}= 1 / 12$. The most obvious choice is a normal distribution for the $Z_{i}$, but this would be self-serving in the Monte Carlo experiment which follows, where the $X_{i}$ themselves are normally distributed. The quantities $\bar{x}, \hat{\sigma}$, and $c$ appearing in (3.11) are the sample mean, sample standard deviation $\left(=\left(\hat{\mu}_{2}\right)^{\frac{1}{2}}\right)$, and $\left[1+\sigma_{Z}^{2}\right]^{-\frac{1}{2}}$, respectively, so that $X_{i}^{*}$ has mean $\bar{x}$ and variance $\hat{\sigma}^{2}$ under the bootstrap sampling procedure. In using (3.11) in place of (2.4), we are replacing $\hat{F}$ with a smoothed "window" estimator, having the same mean and variance as $\hat{F}$.

A small Monte Carlo experiment was run to compare the various bootstrap methods suggested above. Instead of comparing the squared error of the sample median, the quantity bootstrapped was

$$
R(\mathbf{X}, F)=\frac{|t(\mathbf{X})-\theta(F)|}{\sigma(F)}
$$

the absolute error of the sample median relative to the population standard deviation. (This quantity is more stable numerically, because the absolute value is less sensitive than the square and also because $R^{*}=\left|t\left(\mathbf{X}^{*}\right)-\theta(\hat{F})\right| / \hat{\sigma}$ is scale invariant, which eliminates the component of variation due to $\hat{\sigma}$ differing from $\sigma(F)$. The stability of (3.12) greatly increased the effectiveness of the Monte Carlo trial.)

The Monte Carlo experiment was run with $n=13, X_{i} \sim_{\text {ind }} \mathscr{N}(0,1), i= 1,2, \ldots, n$. In this situation the true expectation of $R$ is

$$
E_{F} R=0.95
$$

The first two columns of Table 1 show $E_{F} R^{*}$ for each trial, using the bootstrap probabilities (3.6), and then (3.10) for the symmetrized version. It is not possible to theoretically calculate $E_{*} R^{*}$ for the smoothed bootstrap (3.11), so these entries of Table 1 were obtained by a secondary Monte Carlo simulation, as described in "Method 2" of Section 2. A total of $N=50$ replications $\mathbf{x}^{* j}$ were generated for each trial. This means that the values in the table are only unbiased estimates of the actual bootstrap expectations $E_{*} R^{*}$ (which could be obtained by letting $N \rightarrow \infty$ ); the standard error being about .15 for each entry. The effect of this approximation is seen in the column " $d=0$," which would exactly equal column "(3.6)" if $N \rightarrow \infty$. (Within each trial, the same set of random numbers was used to generate the four different uniform distributions for $Z_{i}, d=0, .25, .5,1$.)

TABLE 1*
| Trial \# | Unsmoothed |  | Smoothed Bootstrap (3.11) |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Bootstrap |  | $Z_{i}$ uniform dist. on [ $-d / 2, d / 2$ ] |  |  |  | $Z_{i}$ triangular dist., $\sigma_{Z}^{2}=1 / 12$ |
|  | (3.6) | (3.10) | $d=0$ | $d=.25$ | $d=.5$ | $d=1$ |  |
| 1 | 1.07 | 1.18 | 1.09 | 1.10 | 1.12 | 1.11 | 1.16 |
| 2 | . 96 | . 74 | 1.10 | 1.10 | 1.08 | 1.09 | 1.15 |
| 3 | 1.22 | . 74 | 1.36 | 1.35 | 1.33 | 1.43 | 1.52 |
| 4 | 1.38 | 1.51 | 1.44 | 1.41 | 1.38 | 1.28 | 1.30 |
| 5 | 1.00 | . 83 | 1.03 | 1.05 | 1.09 | 1.14 | 1.17 |
| 6 | 1.13 | 1.21 | 1.27 | 1.26 | 1.23 | 1.20 | 1.26 |
| 7 | 1.07 | . 98 | 1.01 | . 94 | . 83 | . 79 | . 92 |
| 8 | 1.51 | 1.40 | 1.40 | 1.45 | 1.47 | 1.51 | 1.50 |
| 9 | . 56 | . 64 | . 69 | . 71 | . 74 | . 80 | . 81 |
| 10 | 1.05 | . 86 | 1.14 | 1.17 | 1.20 | 1.13 | 1.22 |
| Ave. | 1.09 | 1.01 | 1.15 | 1.15 | 1.15 | 1.15 | 1.20 |
| S.D. | . 26 | . 30 | . 23 | . 23 | . 23 | . 23 | . 22 |


*Ten Monte Carlo trials of $X_{i} \sim_{\text {ind }} \mathscr{I}(0,1), i=1,2, \ldots, 13$ were used to compare different bootstrap methods for estimating the expected value of random variable (3.12). The true expectation is 0.95 . The quantities tabled are $E_{*} R^{*}$, the bootstrap expectation for that trial. The values in the first two columns are for the bootstrap as described originally, and for the symmetrized version (3.8)-(3.10). The smoothed bootstrap expectations were approximated using a secondary Monte Carlo simulation for each trial, $N=50$, as described in "Method 2," Section 2. Each of these entries estimates the actual value of $E_{*} R^{*}$ unbiasedly with a standard error of about .15 . The column " $d=0$ " would exactly equal column "(3.6)" if $N \rightarrow \infty$.

The most notable feature of Table 1 is that the simplest form of the bootstrap, "(3.6)," seems to do just as well as the symmetrical or smoothed versions. A larger Monte Carlo investigation of the same situation as in Table 1, 200 trials, 100 bootstrap replications per trial, was just a little more favorable to the smoothed bootstrap methods:

|  | $(3.6)$ | $(3.10)$ | $d=0$ | $d=.25$ | $d=.5$ | $d=1$ | $d=2$ |
| ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| AVE.: | 1.01 | 1.00 | 1.00 | 1.01 | 1.00 | .99 | .93 |
| S.D.: | .31 | .33 | $.32[.31]$ | $.32[.30]$ | $.32[.30]$ | $.30[.29]$ | $.26[.25]$. |

(The figures in square brackets are estimated standard deviations if $N$ were increased from 100 to $\infty$, obtained by a components of variance calculation.) Remembering that we are trying to estimate the true value $E_{F} R=.95$, these seem like good performances for a nonparametric method based on a sample size of just 13.

The symmetrized version of the bootstrap might be expected to do relatively better than the unsymmetrized version if $R$ itself was of a less symmetric form than (3.12), e.g., $R(\mathbf{X}, F)=\exp \left\{X_{(m)}-\theta(F)\right\}$. Likewise, the smoothed versions of the bootstrap might be expected to do relatively better if $R$ itself were less smooth, e.g., $R(\mathbf{X}, F)=\operatorname{Prob}\left\{X_{(m)}>\theta(F)+\sigma(F)\right\}$. However no evidence to support these guesses is available at present.
4. Error rate estimation in discriminant analysis. This section discusses the estimation of error rates in a standard linear discriminant analysis problem. There is a tremendous literature on this problem, nicely summarized in Toussaint [17]. In the two examples considered below, bootstrap methods outperform the commonly used "leave-one-out," or cross-validation, approach (Lachenbruch and Mickey [12]).

The data in the discriminant problem consists of independent random samples from two unknown continuous probability distributions $F$ and $G$ on some $k$-dimensional space $R^{k}$,

$$
\begin{array}{rlrl}
X_{i} & =x_{i}, & X_{i} \sim_{\text {ind }} F & \\
Y_{j} & =y_{j}, & Y_{j} \sim_{\text {ind }} G & \\
& j=1,2, \ldots, m \\
& & j=1,2, \ldots, n
\end{array}
$$

On the basis of the observed data $\mathbf{X}=\mathbf{x}, \mathbf{Y}=\mathbf{y}$ we use some method (linear discriminant analysis in the examples below) to partition $R^{k}$ into two complementary regions $A$ and $B$, the intent being to ascribe a future observation $z$ to the $F$ distribution if $z \in A$, or to the $G$ distribution if $z \in B$.

The obvious estimate of the error rate, for the $F$ distribution, associated with the partition $(A, B)$ is

$$
\widehat{\operatorname{error}}_{F}=\frac{\#\left\{x_{i} \in B\right\}}{m},
$$

which will tend to underestimate the true error rate

$$
\operatorname{error}_{F}=\operatorname{Prob}_{F}\{X \in B\}
$$

(In probability calculation (4.3), $B$ is considered fixed, at its observed value, even though it is originally determined by a random mechanism.) We will be interested in the distribution of the difference

$$
R((\mathbf{X}, \mathbf{Y}),(F, G))=\operatorname{error}_{F}-\widehat{\operatorname{error}}_{F},
$$

and the corresponding quantity for the distribution $G$. We could directly consider the distribution of $\widehat{\text { error }}_{F}$, but concentrating on the difference (4.4) is much more efficient for comparing different estimation methods. This point is discussed briefly at the end of the section.

Given $\mathbf{x}$ and $\mathbf{y}$, we define the region $B$ by

$$
B=\left\{z:(\bar{y}-\bar{x})^{\prime} S^{-1}\left(z-\frac{\bar{x}+\bar{y}}{2}\right)>\log \frac{m}{n}\right\}
$$

where $\bar{x}=\Sigma x_{i} / m, \bar{y}=\Sigma y_{j} / n$, and $S=\left[\Sigma\left(x_{i}-\bar{x}\right)\left(x_{i}-\bar{x}\right)^{\prime}+\Sigma\left(y_{j}-\bar{y}\right)\left(y_{j}-\right.\right. \left.\bar{y})^{\prime}\right] /(m+n)$. This is the maximum likelihood estimate of the optimum division under multivariate normal theory, and differs just slightly (in the definition of $S$ ) from the estimated version of the Fisher linear discriminant function discussed in Chapter 6 of Anderson [1].
"Method 2," the brute force application of the bootstrap via simulation, is implemented as follows: given the data $\mathbf{x}, \mathbf{y}$, bootstrap random samples

$$
\begin{array}{lll}
X_{i}^{*}=x_{i}^{*}, & X_{i}^{*} \sim_{\text {ind }} \hat{F} & i=1,2, \ldots, m \\
Y_{j}^{*}=y_{j}^{*}, & Y_{j}^{*} \sim_{\text {ind }} \hat{G} & j=1,2, \ldots, n
\end{array}
$$

are generated, $\hat{F}$ and $\hat{G}$ being the sample probability distributions corresponding to $F$ and $G$. This yields a region $B^{*}$ defined by (4.5) with $\bar{x}^{*}, \bar{y}^{*}, S^{*}$ replacing $\bar{x}, \bar{y}, S$. The bootstrap random variable in this case is

$$
R^{*}=R\left(\left(\mathbf{X}^{*}, \mathbf{Y}^{*}\right),(\hat{F}, \hat{G})\right)=\frac{\sharp\left\{x_{i} \in B^{*}\right\}}{m}-\frac{\sharp\left\{x_{i}^{*} \in B^{*}\right\}}{m} .
$$

In other words, (4.7) is the difference between the actual error rate, actual now being defined with respect to the "true" distribution $\hat{F}$, and the apparent error rate obtained by counting errors in the bootstrap sample.

Repeated independent generation of ( $\mathbf{X}^{*}, \mathbf{Y}^{*}$ ) yields a sequence of independent realizations of $R^{*}$, say $R^{* 1}, R^{* 2}, \ldots, R^{* N}$, which are then used to approximate the actual bootstrap distribution of $R^{*}$, this hopefully being a reasonable estimate of the unknown distribution of $R$. For example, the bootstrap expectation $E_{*} R^{*}= \sum_{j=1}^{N} R^{* j} / N$ can be used as an estimate of the true expectation $E_{F, G} R$.

To test out this theory, bivariate normal choices of $F$ and $G$ were investigated,

$$
F: X \sim \mathscr{M}_{2}\left(\binom{-\frac{1}{2}}{0}, \mathrm{I}\right) G: Y \sim \mathscr{M}_{2}\left(\binom{\frac{1}{2}}{0}, \mathrm{I}\right) .
$$

Two sets of sample sizes, $m=n=10$ and $m=n=20$, were looked at, with the results shown in Table 2. (The entries of Table 2 were themselves estimated by averaging over repeated Monte Carlo trials, which should not be confused with the

TABLE 2*
| Random Variable | $m=n=10$ |  |  | $m=n=20$ |  |  | Remarks |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Mean | (S.E.) | S.D. | Mean | (S.E.) | S.D. |  |
| Error Rate Diff. (4.4) $R$ | . 062 | (.003) | . 143 | . 028 | (.002) | . 103 | Based on 1000 trials |
| Bootstrap Expectation $E_{*} R^{*}$ | . 057 | (.002) | . 026 | . 029 | (.001) | . 015 | Based on 100 trials; $N=100$ Bootstrap |
|  |  |  | [.023] |  |  | [.011] | Replications per trial. (Figure in |
| Bootstrap Standard $S D_{*}\left(R^{*}\right)$ | . 131 | (.0013) | . 016 | . 097 | (.002) | . 010 | brackets is S.D. if |
| Deviation |  |  |  |  |  |  | $N=\infty$.) |
| Cross-Validation Diff. $\tilde{R}$ | . 054 | (.009) | . 078 | . 032 | (.002) | . 043 | Based on 40 trials |


[^1]
[^0]:    Received June 1977; revised December 1977.
    AMS 1970 subject classifications. Primary 62G05, 62G15; Secondary 62H30, 62J05.
    Key words and phrases. Jackknife, bootstrap, resampling, subsample values, nonparametric variance estimation, error rate estimation, discriminant analysis, nonlinear regression.

[^1]:    *The error rate difference (4.4) for linear discriminant analysis, investigated for bivariate normal samples (4.8). Sample sizes are $m=n=10$ and $m=n=20$. The values for the bootstrap method were obtained by Method 2, $N=100$ bootstrap replications per trial. The bootstrap method gives useful estimates of both the mean and standard deviation of $R$. The cross-validation method was nearly unbiased for the expectation of $R$, but had about three times as large a standard deviation. All of the quantities in this table were estimated by repeated Monte Carlo trials; standard errors are given for the means.



Monte Carlo replications used in the bootstrap process. "Replications" will always refer to the bootstrap process, "trials" to repetitions of the basic situation.) Because situation (4.8) is symmetric, only random variable (4.4), and not the corresponding error rate for $G$, need be considered.
Table 2 shows that with $m=n=10$, the random variable (4.4) has mean and standard deviation approximately (.062, .143). The apparent error rate underestimates the true error rate by about $6 \%$, on the average, but the standard deviation of the difference is $14 \%$ from trial to trial, so bias is less troublesome than variability in this situation. The bootstrap method gave an average of .057 for $E_{*} R^{*}$, which, allowing for sampling error, shows that the statistic $E_{*} R^{*}$ is nearly an unbiased estimator for $E_{F, G} R$. Unbiasedness is not enough, of course; we want $E_{*} R^{*}$ to have a small standard deviation, ideally zero, so that we can rely on it as an estimate. The actual value of its standard deviation, .026 , is not wonderful, but does indicate that most of the trials yielded $E_{*} R^{*}$ in the range [.02, .09], which means that the statistician would have obtained a reasonably informative estimate of the true bias $E_{F, G} R=.062$.

As a point of comparison, consider the cross-validation estimate of $R$, say $\tilde{R}$, obtained by: deleting one $x$ value at a time from the vector $\mathbf{x}$; recomputing $B$ using (4.5), to get a new region $\tilde{B}$ (it is important not to change $m$ to $m-1$ in recomputing $B$-doing so results in badly biased estimation of $R$ ); seeing if the deleted $x$ value is correctly classified by $\tilde{B}$; counting the proportion of $x$ values misclassified in this way to get a cross-validated error rate $\overbrace{\text { error }}^{F}$; and finally, defining $\tilde{R}=\overbrace{\text { error }}^{F}{ }_{F}-\widehat{\text { error }}_{F}$. The last row of Table 2 shows that $\tilde{R}$ has mean and standard deviation approximately ( $.054, .078$ ). That is, $\tilde{R}$ is three times as variable as $E_{*} R^{*}$ as an estimator of $E_{F, G} R$.

The bootstrap standard deviation of $R^{*}, S D_{*}\left(R^{*}\right)=\left\{\sum_{j=1}^{N}\left[R^{* j}-E_{*} R^{*}\right\}^{2} /(N\right. -1)\}^{\frac{1}{2}}$, can be used as an estimate of $S D_{F, G}(R)$, the actual standard deviation of $R$. Table 2 shows that $S D_{*}\left(R^{*}\right)$ had mean and standard deviation (.131, .016) across the 100 trials. Remembering that $S D_{F, G}(R)=.143$, the bootstrap estimate $S D_{*}\left(R^{*}\right)$ is seen to be a quite useful estimator of the actual standard deviation of $R$.

How much better would the bootstrap estimator $E_{*} R^{*}$ perform if the number of bootstrap replications $N$ were increased from 100 to, say, 10,000 ? A components of variance analysis of all the data going into Table 2 showed that only moderate further improvement is possible. As $N \rightarrow \infty$, the trial-to-trial standard deviation of $E_{*} R^{*}$ would decrease from .026 to about .023 (from .015 to .011 in the case $m=n=20$ ).

The reader may wonder which is the best estimator of the error rate error ${ }_{F}$ itself, rather than of the difference $R$. In terms of expected squared error, the order of preference is $\widehat{\text { error }}_{F}+E_{*} R^{*}$ (the bias-corrected value based on the bootstrap), $\widehat{\text { error }}_{F}$, and lastly error ${ }_{F}$, but the differences are quite small in the two situations of Table 2. The large variability of $\widehat{\text { error }}_{F}$, compared to its relatively small bias, makes
bias correction an almost fruitless chore in these two situations. (Of course, this might not be so in more difficult discriminant problems.) The bootstrap estimates of $E_{F, G} R$ and $S D_{F, G}(R)$ considered together make it clear that this is the case, which is a good recommendation for the bootstrap approach.
5. Relationship with the jackknife. This section concerns "Method 3" of approximating the bootstrap distribution, Taylor series expansion (or the delta method), which turns out to be the same as the usual jackknife theory. To be precise, it is the same as Jaeckel's infinitesimal jackknife [10, 14], a useful mathematical device which differs only in detail from the standard jackknife. Many of the calculations below, and in Remarks G-K of Section 8, can be found in Jaeckel's excellent paper, which offers considerable insight into the workings of jackknife methods.

Returning to the one-sample situation, define $P_{i}^{*}=N_{i}^{*} / n$, where $N_{i}^{*}=\#\left\{X_{i}^{*}=\right. x_{i}$ ) as at (3.2), and the corresponding vector

$$
\mathbf{P}^{*}=\left(P_{1}^{*}, P_{2}^{*}, \cdots, P_{n}^{*}\right) .
$$

By the properties of the multinomial distribution, $\mathbf{P}^{*}$ has mean vector and covariance matrix

$$
E_{*} \mathbf{P}^{*}=\mathbf{e} / n, \quad \operatorname{Cov}_{*} \mathbf{P}^{*}=\mathbf{I} / n^{2}-\mathbf{e}^{\prime} \mathbf{e} / n^{3}
$$

under the bootstrap sampling procedure, where $\mathbf{I}$ is the identity matrix and $\mathbf{e}=(1,1,1, \ldots, 1)$.

Given the observed data vector $\mathbf{X}=\mathbf{x}$, and therefore $\hat{F}$, we can use the abbreviated notation

$$
R\left(\mathbf{P}^{*}\right)=R\left(\mathbf{X}^{*}, \hat{F}\right)
$$

for the bootstrap realization of $R$ corresponding to $\mathbf{P}^{\boldsymbol{*}}$. In making this definition we assume that the random variable of interest, $R(\mathbf{X}, F)$, is symmetrically defined in the sense that its value is invariant under any permutation of the components of $X$, so that it is sufficient to know $\mathbf{N}^{*}=n \mathbf{P}^{*}$ in order to evaluate $R\left(\mathbf{X}^{*}, \hat{F}\right)$. This is always the case in standard applications of the jackknife.

We can approximate the bootstrap distribution of $R\left(\mathbf{X}^{*}, \hat{F}\right)$ by expanding $R\left(\mathbf{P}^{*}\right)$ in a Taylor series about the value $\mathbf{P}^{*}=\mathbf{e} / n$, say

$$
R\left(\mathbf{P}^{*}\right) \doteq R(\mathbf{e} / n)+\left(\mathbf{P}^{*}-\mathbf{e} / n\right) \mathbf{U}+\frac{1}{2}\left(\mathbf{P}^{*}-\mathbf{e} / n\right) \mathbf{V}\left(\mathbf{P}^{*}-\mathbf{e} / n\right)^{\prime}
$$

Here

$$
\mathbf{U}=\left(\begin{array}{c}
\vdots \\
\frac{\partial R\left(\mathbf{P}^{*}\right)}{\partial P_{i}^{*}} \\
\vdots
\end{array}\right)_{\boldsymbol{P}^{*}=e / n} \quad \mathbf{V}=\left(\begin{array}{ccc}
\vdots & & \\
\cdots & \partial^{2} R\left(\mathbf{P}^{*}\right) & \\
\hdashline & \partial P_{i}^{*} \partial P_{j}^{*} & \cdots \\
& \vdots
\end{array}\right)_{\boldsymbol{P}^{*}=e / n}
$$

Expansion (5.4), and definitions (5.5), assume that the definition of $R\left(\mathbf{P}^{*}\right)$ can be smoothly interpolated between the lattice point values originally contemplated for $\mathbf{P}^{*}$. How to do so will be obvious in most specific cases, but a general recipe is difficult to provide. See Remarks G and H of Section 8.

The restriction $\Sigma P_{i}{ }^{*}=1$ has been ignored in (5.4), (5.5). This computational convenience is justified by extending the definition of $R\left(\mathbf{P}^{\boldsymbol{*}}\right)$ to all vectors $\mathbf{P}^{\boldsymbol{*}}$ having nonnegative components, at least one positive, by the homogeneous extension

$$
R\left(\mathbf{P}^{*}\right)=R\left(\frac{\mathbf{P}^{*}}{\sum_{i=1}^{n} P_{i}^{*}}\right)
$$

It is easily shown that the homogeneity of definition (5.6) implies

$$
\mathbf{e U}=0, \quad \mathbf{e V}=-n \mathbf{U}^{\prime}, \quad \mathbf{e V} \mathbf{e}^{\prime}=0 .
$$

From (5.2) and (5.4) we get the approximation to the bootstrap expectation

$$
E_{*} R\left(\mathrm{P}^{*}\right) \doteq R(\mathbf{e} / n)+\frac{1}{2} \operatorname{trace} \mathbf{V}\left[\mathbf{I} / n^{2}-\mathbf{e}^{\prime} \mathbf{e} / n^{3}\right]=R(\mathbf{e} / n)+\frac{1}{2 n} \bar{V}
$$

where

$$
\bar{V}=\sum_{i=1}^{n} V_{i i} / n
$$

Ignoring the last term in (5.4) gives a cruder approximation for the bootstrap variance,

$$
\operatorname{Var}_{*} R\left(\mathbf{P}^{*}\right) \doteq \mathbf{U}^{\prime}\left[\mathbf{I} / n^{2}-\mathbf{e}^{\prime} \mathbf{e} / n^{3}\right] \mathbf{U}=\sum_{i=1}^{n} U_{i}^{2} / n^{2}
$$

(Both (5.8) and (5.10) involve the use of (5.7).)
Results (5.8) and (5.10) are essentially the jackknife expressions for bias and variance. The usual jackknife theory considers $R(\mathbf{X}, F)=\theta(\hat{F})-\theta(F)$, the difference between the obvious nonparametric estimator of some parameter $\theta(F)$ and $\theta(F)$ itself. In this case $R\left(\mathbf{X}^{*}, F\right)=\theta\left(\hat{F}^{*}\right)-\theta(\hat{F}), \hat{F}^{*}$ being the empirical distribution of the bootstrap sample, so that $R(\mathbf{e} / n)=\theta(\hat{F})-\theta(\hat{F})=0$. Then (5.8) becomes $E_{*}\left[\theta\left(\hat{F}^{*}\right)-\theta(\hat{F})\right] \doteq(1 / 2 n) \bar{V}$, suggesting $E_{F}[\theta(\hat{F})-\theta(F)] \approx(1 / 2 n) \bar{V}$; likewise (5.10) becomes $\operatorname{Var}_{*}\left[\theta\left(\hat{F}^{*}\right)-\theta(\hat{F})\right] \doteq \Sigma U_{i}^{2} / n^{2}$, suggesting $\operatorname{Var}_{F} \theta(\hat{F}) \approx \Sigma U_{i}^{2} / n^{2}$.
The approximations

$$
\operatorname{Bias}_{F} \theta(\hat{F}) \approx \frac{1}{2 n} \bar{V}, \quad \operatorname{Var}_{F} \theta(\hat{F}) \approx \sum_{i=1}^{n} U_{i}^{2} / n^{2}
$$

exactly agree with those given by Jaeckel's infinitesimal jackknife [10], which themselves differ only slightly from the ordinary jackknife expressions. Without going into details, which are given in Jaeckel [10] and Miller [14], the ordinary jackknife replaces the derivatives $U_{i}=\partial R\left(\mathbf{P}^{*}\right) / \partial P_{i}$ with finite differences

$$
\tilde{U}_{i}=(n-1)\left(R_{.}^{*}-R_{(i)}^{*}\right)
$$

where $R_{(i)}^{*}=R\left(\mathbf{e}_{(i)} /(n-1)\right), \mathbf{e}_{(i)}$ being the vector with zero in the $i$ th coordinate and ones elsewhere, and $R^{*}=\sum_{i=1}^{n} R_{(i)}^{*} / n$. Expansion (5.4) combines with (5.7) to give

$$
\tilde{U}_{i} \doteq \frac{n-2}{n-1} U_{i}-\frac{1}{2(n-1)}\left(V_{i i}-\bar{V}\right),
$$

so that $\tilde{U}_{i} / U_{i}=1+O(1 / n)$. The ordinary jackknife estimate of variance is $\sum_{i=1}^{n} \tilde{U}_{i}^{2} / n \cdot(n-1)$, differing from the variance expression in (5.11) by a factor $1+O(1 / n)$, the same statement being true for the bias. (In the familiar case $R=\theta(\hat{F})-\theta(F)$, definition (5.12) becomes $\tilde{U}_{i}=(n-1)\left(\hat{\theta}-\hat{\theta}_{(i)}\right)$, where $\hat{\theta}_{(i)}$ is the estimate of $\theta$ with $x_{i}$ removed from the sample, and $\hat{\theta}_{i}=\Sigma_{i} \hat{\theta}_{(i)} / n$; the jackknife estimate of $\theta$ is $\tilde{\theta}=\hat{\theta}+(n-1)(\hat{\theta}-\hat{\theta})$, and $\tilde{\theta}_{i}=\tilde{\theta}+\tilde{U}_{i}$, is the $i$ th pseudo-value, to use the standard terminology.)
As an example of Method 3, consider ratio estimation, where the $X_{i}$ are bivariate observations, say $X_{i}=\left(Y_{i}, Z_{i}\right)$, and we wish to estimate $\theta(F)=E_{F} Y / E_{F} Z$. (Take $Y, Z>0$ for convenience.) Let $t(\mathbf{X})=\bar{Y} / \bar{Z}$, and $R(\mathbf{X}, F)=t(\mathbf{X}) / \theta(F)$. It is easily verified that

$$
U_{i}=\frac{y_{i}}{\bar{y}}-\frac{z_{i}}{\bar{z}}, \quad V_{i j}=2 \frac{z_{i}}{\bar{z}} \frac{z_{j}}{\bar{z}}-\left(\frac{y_{i}}{\bar{y}} \frac{z_{j}}{\bar{z}}+\frac{y_{j}}{\bar{y}} \frac{z_{i}}{\bar{z}}\right),
$$

and that (5.8), (5.10) give

$$
\begin{aligned}
E_{*} R^{*} & \doteq 1-\frac{1}{n^{2}}\left\{\Sigma_{i}\left(\frac{y_{i}}{\bar{y}}-1\right)\left(\frac{z_{i}}{\bar{z}}-1\right)-\Sigma_{i}\left(\frac{z_{i}}{\bar{z}}-1\right)^{2}\right\}, \\
\operatorname{Var}_{*} R^{*} & \doteq \frac{1}{n^{2}} \Sigma_{i}\left[\frac{y_{i}}{\bar{y}_{\partial}}-\frac{z_{i}}{\bar{z}}\right]^{2} .
\end{aligned}
$$

The biased corrected estimate for $\theta(F)$ is $t(\mathbf{X}) / E_{*} R^{*}$, with approximate variance $(\hat{\theta} / n)^{2} \Sigma\left[y_{i} / \bar{y}-z_{i} / \bar{z}\right]^{2}$. If the statistician feels uneasy about expressions (5.15) for any particular data set, perhaps because of outlying values, Method 2 can be invoked to check the bootstrap distribution of $t\left(\mathbf{X}^{*}\right)$ directly.

The infinitesimal jackknife and the ordinary jackknife can both be applied starting from $\hat{F}_{\text {SYM }}$, (3.8), rather than from $\hat{F}$. It is easiest to see how for the infinitesimal jackknife. Expansion (5.4) is still valid except that $\mathbf{U}$ is now a $(2 n-1) \times 1$ vector, $\mathbf{V}$ is a $(2 n-1) \times(2 n-1)$ matrix, and $\mathbf{P}^{*}$ has bootstrap mean $\mathbf{e} /(2 n-1)$, covariance matrix $(1 / n)\left[\mathbf{I} /(2 n-1)-\mathbf{e}^{\prime} \mathbf{e}(2 n-1)^{2}\right]$. The variance approximation corresponding to (5.10) is

$$
\operatorname{Var}_{* \mathrm{SYM}} R\left(\mathbf{P}^{*}\right)=\frac{\sum_{l=1}^{2 n-1} U_{l}^{2}}{n(2 n-1)}
$$

6. Wilcoxon's statistic. We again consider the two-sample situation (4.1), this time with $F$ and $G$ being continuous probability distributions on the real line. The
parameter of interest will be

$$
\theta(F, G)=P_{F, G}(X<Y)
$$

estimated by Wilcoxon's statistic

$$
\hat{\theta}=\theta(\hat{F}, \hat{G})=\frac{1}{m n} \sum_{i=1}^{m} \sum_{j=1}^{n} I\left(X_{i}, Y_{j}\right),
$$

where

$$
\begin{aligned}
I(a, b) & =1 & & a<b \\
& =0 & & a \geqslant b .
\end{aligned}
$$

The bootstrap variance of $\hat{\theta}$ can be calculated directly by Method 1 , and will turn out below to be the same as the standard variance approximation for Wilcoxon's statistic. The comparison with Method 3, the infinitesimal jackknife, illustrates how this theory works in a two-sample situation. More importantly, it suggests the correct analogue of the ordinary jackknife for such situations.

There has been considerable interest in extending the ordinary jackknife to "unbalanced" situations, i.e., those where it is not clear what the correct analogue of "leave one out" is, see Miller [15], Hinkley [9]. In the two-sample problem, for example, should we leave out one $x_{i}$ at a time, then one $y_{j}$ at a time, or should we leave out all $m n$ pairs $\left(x_{i}, y_{j}\right)$ one at a time? (The former turns out to be correct.) This problem gets more crucial in the next section, where we consider regression problems.

Let $R((\mathbf{X}, \mathbf{Y}),(F, G))$ be $\hat{\theta}$ itself, so that the bootstrap value of $R$ corresponding to $\left(\mathbf{X}^{*}, \mathbf{Y}^{*}\right)$ is $R\left(\left(\mathbf{X}^{*}, \mathbf{Y}^{*}\right),(\hat{F}, \hat{G})\right)=\hat{\theta}^{*}$,

$$
\hat{\theta}^{*}=\frac{1}{m n} \Sigma_{i} \Sigma_{j} I\left(X_{i}^{*}, Y_{j}^{*}\right)
$$

Letting $I_{i j}^{*}=I\left(X_{i}^{*}, Y_{j}^{*}\right)$, straightforward calculations familiar from standard nonparametric theory, give

$$
E_{*} I_{i j}^{*}=\hat{\theta}, \quad \operatorname{Var}_{*} I_{i j}^{*}=\hat{\theta}(1-\hat{\theta}), \quad E_{*} I_{i j}^{*} I_{i^{\prime} j^{\prime}}^{*}=\hat{\theta}^{2} \quad i \neq i^{\prime}, j \neq j^{\prime}
$$

and

$$
\begin{array}{ll}
E_{*} I_{i j}^{*} I_{i j^{\prime}}^{*}=\int_{-\infty}^{\infty}[1-\hat{G}(z)]^{2} d \hat{F}(z) \equiv \hat{\alpha}, & j \neq j^{\prime} \\
E_{*} I_{i j}^{*} I_{i^{\prime} j}^{*}=\int_{-\infty}^{\infty} \hat{F}^{2}(z) d \hat{G}(z) \equiv \hat{\beta}, & i \neq i^{\prime}
\end{array}
$$

Using these results in (6.4) gives

$$
\operatorname{Var}_{*} \hat{\theta}^{*}=\frac{(n-1)\left(\hat{\alpha}-\hat{\theta}^{2}\right)+(m-1)(\hat{\beta}-\hat{\theta})^{2}+\hat{\theta}(1-\hat{\theta})}{m n},
$$

which is the usual estimate for the variance of the Wilcoxon statistic, see Noether [16], page 32.

Method 3, the Taylor series or infinitesimal jackknife, proceeds as in Section 5, with obvious modifications for the two-sample situation. Let $\mathbf{N}_{F}^{*}=$ ( $N_{F 1}^{*}, N_{F 2}^{*}, \cdots, N_{F m}$ ) be the numbers of times $x_{1}, x_{2}, \cdots, x_{m}$ occur in the bootstrap sample $\mathrm{X}^{*}$, likewise $\mathrm{N}_{G}^{*}=\left(N_{G 1}^{*}, N_{G 2}^{*}, \cdots, N_{G n}^{*}\right)$ for $\mathrm{Y}^{*}$, and define $\mathbf{P}_{F}{ }^{*}=\mathbf{N}_{F}^{*} / m, \mathbf{P}_{G}^{*}=\mathbf{N}_{G}^{*} / n$, these being independent random vectors with mean and covariance as in (5.2). The expansion corresponding to (5.4) is

$$
\begin{aligned}
R\left(\mathbf{P}_{F}^{*}, \mathbf{P}_{G}^{*}\right)= & R(\mathbf{e} / m, \mathbf{e} / n)+\left(\mathbf{P}_{F}^{*}-\mathbf{e} / m\right) \mathbf{U}_{F}+\left(\mathbf{P}_{G}^{*}-\mathbf{e} / n\right) \mathbf{U}_{G} \\
& +\frac{1}{2}\left[\left(\mathbf{P}_{F}^{*}-\mathbf{e} / m\right) V_{F}\left(\mathbf{P}_{F}^{*}-\mathbf{e} / m\right)^{\prime}\right. \\
& +2\left(\mathbf{P}_{F}^{*}-\mathbf{e} / m\right) V_{F G}\left(\mathbf{P}_{G}^{*}-\mathbf{e} / n\right)^{\prime} \\
& \left.+\left(\mathbf{P}_{G}^{*}-\mathbf{e} / n\right) V_{G}\left(\mathbf{P}_{G}^{*}-\mathbf{e} / n\right)^{\prime}\right]
\end{aligned}
$$

where

$$
U_{F i}=\partial R / \partial P_{F i}^{*}, \quad V_{F i i^{\prime}}=\partial^{2} R / \partial P_{F i}^{*} \partial P_{F i^{\prime}}^{*}, \quad V_{F G i j}=\partial^{2} R / \partial P_{F i}^{*} \partial P_{G j}^{*},
$$

all the derivatives being evaluated at $\left(\mathbf{P}_{F}^{*}, \mathbf{P}_{G}^{*}\right)=(\mathbf{e} / m, \mathbf{e} / n)$, analogous definitions applying to $\mathbf{U}_{G}$ and $\mathbf{V}_{G}$.
The results corresponding to (5.8) and (5.10) are

$$
E_{*} R^{*} \doteq R(\mathbf{e} / m, \mathbf{e} / n)+\frac{1}{2}\left[\frac{\bar{V}_{F}}{m}+\frac{\bar{V}_{G}}{n}\right]
$$

and

$$
\operatorname{Var}_{*} R^{*} \doteq \sum_{i=1}^{m} U_{F i}^{2} / m^{2}+\sum_{j=1}^{n} U_{G j}^{2} / n^{2}
$$

$\bar{V}_{F}=\Sigma_{i} V_{F i i} / m, \bar{V}_{G}=\Sigma_{j} V_{G j j} / n$. For $R=\theta(\hat{F}, \hat{G})-\theta(F, G)$, the approximations corresponding to (5.11) are

$$
\operatorname{Bias}_{F, G} \theta(\hat{F}, \hat{G}) \approx \frac{1}{2}\left[\frac{\bar{V}_{F}}{m}+\frac{\bar{V}_{G}}{n}\right], \quad \operatorname{Var}_{F, G} \theta(F, G) \approx \frac{\sum_{i=1}^{m} U_{F i}^{2}}{m^{2}}+\frac{\sum_{j=1}^{n} U_{G j}^{2}}{n^{2}}
$$

For the case of the Wilcoxon statistic (6.11) (or (6.12)) gives

$$
\operatorname{Var}_{*} \hat{\theta}^{*} \doteq \frac{n\left[\hat{\alpha}-\hat{\theta}^{2}\right]+m\left[\hat{\beta}-\hat{\theta}^{2}\right]}{m n}
$$

which should be compared with (6.7).
How can we use the ordinary jackknife to get results like (6.12)? A direct analogy of (5.12) can be carried through, but it is simpler to change definitions slightly, letting

$$
\begin{aligned}
D_{(i,)} & =R(\mathbf{e} / m, \mathbf{e} / n)-R\left(\mathbf{e}_{(i)} /(m-1), \mathbf{e} / n\right) \\
D_{(, j)} & =R(\mathbf{e} / m, \mathbf{e} / n)-R\left(\mathbf{e} / m, \mathbf{e}_{(j)} /(n-1)\right),
\end{aligned}
$$

the difference from $R((\mathbf{x}, \mathbf{y}),(\hat{F}, \hat{G}))$ obtained by deleting $x_{i}$ from $\mathbf{x}$ or $y_{j}$ from $\mathbf{y}$. Expansion (6.8) gives

$$
\begin{aligned}
D_{(i,)} & \doteq \frac{m-2}{(m-1)^{2}} U_{F i}-\frac{1}{2(m-1)^{2}} V_{F i i} \\
D_{(, j)} & \doteq \frac{(n-2)^{2}}{(n-1)^{2}} U_{G j}-\frac{1}{2(n-1)^{2}} V_{G j j}
\end{aligned}
$$

From (6.15) it is easy to obtain approximations for the bias and variance expressions in terms of the $D$ 's:

$$
-\left[\sum_{i=1}^{m} D_{(i,)}+\sum_{j=1}^{n} D_{(, j)}\right] \doteq \frac{1}{2}\left[\left(\frac{m}{m-1}\right)^{2} \bar{V}_{F}+\left(\frac{n}{n-1}\right)^{2} \bar{V}_{G}\right]
$$

which, as $m$ and $n$ grow large, approaches the second term in (6.10). (For $R=\hat{\theta}-\theta$, this gives the bias-corrected estimate $\tilde{\theta}=(m+n-1) \hat{\theta}-\Sigma_{i} \hat{\theta}_{(i,)}- \Sigma_{j} \hat{\theta}_{(, j)}$.) Likewise, just using the first line of (6.8) gives

$$
\sum_{i=1}^{m} D_{(i,)}^{2}+\sum_{j=1}^{n} D_{(, j)}^{2} \doteq \frac{m^{2}(m-2)^{2}}{(m-1)^{4}} \frac{\sum_{i=1}^{m} U_{F i}^{2}}{m^{2}}+\frac{n^{2}(n-2)^{2}}{(n-1)^{2}} \frac{\sum_{j=1}^{n} U_{G j}^{2}}{n^{2}}
$$

which approaches (6.11) as $m, n \rightarrow \infty$.
The advantage of the $D$ 's over expressions like (5.12) is that no group averages, such as $R_{.}^{*}$, need be defined. Group averages are easy enough to define in the two-sample problem, but are less clear in more complicated situations such as regression. Expressions (6.16) and (6.17) are easy to extend to any situation (which doesn't necessarily mean they give good answers-see the remarks of the next section!).
7. Regression models. A reasonably general regression model is

$$
X_{i}=g_{i}(\beta)+\epsilon_{i} \quad i=1,2, \ldots, n
$$

the $g(\cdot)$ being known functions of the unknown parameter vector $\beta$, and

$$
\epsilon_{i} \sim_{\text {ind }} F \quad i=1,2, \ldots, n
$$

All that is assumed known about $F$ is that it is centered at zero in some sense, perhaps $E_{F} \epsilon=0$ or Median $_{F} \epsilon=0$. Having observed $\mathbf{X}=\mathbf{x}$, we use some fitting technique to estimate $\beta$, perhaps least squares,

$$
\hat{\beta}: \min _{\beta} \sum_{i=1}^{n}\left[x_{i}-g_{i}(\beta)\right]^{2},
$$

and wish to say something about the sampling distribution of $\hat{\beta}$.
Method 2, the brute force application of the bootstrap, can be carried out by defining $\hat{F}$ as the sample probability distribution of the residuals $\hat{\boldsymbol{\epsilon}}_{i}$,

$$
\hat{F}: \text { mass } \frac{1}{n} \quad \text { at } \quad \hat{\epsilon}_{i}=x_{i}-g_{i}(\hat{\beta}), \quad i=1,2, \ldots, n
$$

(If one of the components of $\beta$ is a translation parameter for the functions $g(\cdot)$, then $\hat{F}$ has mean zero. If not, and if the assumption $E_{F} \epsilon=0$ is very firm, one might still modify $\hat{F}$ by translation to achieve zero mean.) The bootstrap sample, given $(\hat{\beta}, \hat{F})$, is

$$
X_{i}^{*}=g_{i}(\hat{\beta})+\epsilon_{i}^{*}, \quad \epsilon_{i}^{*} \sim_{\text {ind }} \hat{F} \quad i=1,2, \ldots, n .
$$

Each realization of (2.5) yields a realization of $\hat{\beta^{*}}$ by the same minimization process that gave $\hat{\beta}$,

$$
\hat{\beta}^{*}: \min _{\beta} \sum_{i=1}^{n}\left[x_{i}^{*}-g_{i}(\beta)\right]^{2} .
$$

Repeated independent bootstrap replications give a random sample $\hat{\beta}^{* 1}, \hat{\beta}^{* 2}, \hat{\beta}^{* 3}, \ldots, \hat{\beta}^{* N}$ which can be used to estimate the bootstrap distribution of $\hat{\beta}^{*}$.

A handy test case is the familiar linear model, $g_{i}(\beta)=c_{i} \beta, c_{i}$ a known $1 \times p$ vector, with first coordinate $c_{i 1}=1$ for convenience. Let $\mathbf{C}$ be the $n \times p$ matrix whose $i$ th row is $c_{i}$, and $\mathbf{G}$ the $p \times p$ matrix $\mathbf{C}^{\prime} \mathbf{C}$, assumed nonsingular. Then the least squares estimator $\hat{\beta}=\mathbf{G}^{-1} \mathbf{C}^{\prime} \mathbf{X}$ has mean $\beta$ and covariance matrix $\boldsymbol{\sigma}_{F}^{2} \mathbf{G}^{-1}$ by the usual theory.

The bootstrap values $\epsilon_{i}^{*}$ used in (7.5) are independent with mean zero and variance $\hat{\boldsymbol{\sigma}}^{2}=\sum_{i=1}^{n}\left[x_{i}-g(\hat{\beta})\right]^{2} / n$. This implies that $\hat{\beta}^{*}=\mathbf{G}^{-1} \mathbf{C}^{\prime} \mathbf{X}^{*}$ has bootstrap mean and variance

$$
E_{*} \hat{\beta}^{*}=\hat{\beta}, \quad \operatorname{Cov}_{*} \hat{\beta}^{*}=\hat{\sigma}^{2} \mathbf{G}^{-1}
$$

The implication that $\hat{\beta}$ is unbiased for $\beta$, with covariance matrix approximately equal to $\hat{\sigma}^{2} \mathbf{G}^{-1}$, agrees with traditional theory, except perhaps in using the estimate $\hat{\sigma}^{2}$ for $\sigma^{2}$.

Miller [15] and Hinkley [9] have applied, respectively, the ordinary jackknife and infinitesimal jackknife to the linear regression problem. They formulate the situation as a one-sample problem, with $\left(c_{i}, x_{i}\right)$ as the $i$ th observed data point, essentially removing one row at a time from the model $\mathbf{X}=\mathbf{C} \beta+\boldsymbol{\epsilon}$. The infinitesimal jackknife gives the approximation

$$
\operatorname{Cov} \hat{\beta} \approx \mathbf{G}^{-1}\left[\sum_{i=1}^{n} c_{i}^{\prime} c_{i} \hat{\epsilon}_{i}^{2}\right] \mathbf{G}^{-1}
$$

(and the ordinary jackknife a quite similar expression) for the estimated covariance matrix. This doesn't look at all like (7.7)!

The trouble lies in the fact that the jackknife methods as used above ignore an important aspect of the regression model, namely that the errors $\epsilon_{i}$ are assumed to have the same distribution for every value of $i$. To make (7.8) agree with (7.7) it is only necessary to "symmetrize" the data set by adding hypothetical data points, corresponding to all the possible values of the residual $\hat{\epsilon}$, at each value of $i$, say

$$
\begin{aligned}
x_{i j}=c_{i} \hat{\beta}+\hat{\epsilon}_{j} & \\
& j=1,2, \ldots, n \quad(i=1,2, \ldots, n) .
\end{aligned}
$$

Notice that the bootstrap implicitly does this at step (7.5). Applying the infinitesimal jackknife to data set (7.9), and remembering to take account of the artificially increased amount of data as at step (5.16), gives covariance estimate (7.7).

Returning to the nonlinear regression model (7.1), (7.2), where bootstrap-jackknife methods may really be necessary in order to get estimates of variability for $\hat{\beta}$, we now suspect that jackknife procedures like "leave out one row at a time" may be inefficient unless preceded by some form of data symmetrization such as (7.9). To put things the other way, as in Hinkley [9], such procedures tend to give consistent estimates of $\operatorname{Cov} \hat{\beta}$ without assumption (7.2) that the residuals are identically distributed. The price of such complete generality is low efficiency. Usually assumption (7.2) can be roughly justified, perhaps after suitable transformations on $X$, in which case the bootstrap should give a better estimate of $\operatorname{Cov} \hat{\beta}$.

## 8. Remarks.

Remark A. Method 2, the straightforward calculation of the bootstrap distribution by repeated Monte Carlo sampling, is remarkably easy to implement on the computer. Given the original algorithm for computing $R$, only minor modifications are necessary to produce bootstrap replications $R^{* 1}, R^{* 2}, \ldots, R^{* N}$. The amount of computer time required is just about $N$ times that for the original computations. For the discriminant analysis problem reported in Table 2, each trial of $N=100$ replications, $m=n=20$, took about 0.15 seconds and cost about 40 cents on Stanford's $370 / 168$ computer. For a single real data set with $m=n=20$, we might have taken $N=1000$, at a cost of $\$ 4.00$.

Remark B. Instead of estimating $\theta(F)$ with $t(\mathbf{X})$, we might make a transformation $\phi=g(\theta), s=g(t)$, and estimate $\phi(F)=g(\theta(F))$ with $s(\mathbf{X})=g(t(\mathbf{X}))$. That is, we might consider the random variable $S(\mathbf{X}, \mathbf{F})=s(\mathbf{X})-\phi(F)$ instead of $R(\mathbf{X}, \mathbf{F}) =t(\mathbf{X})-\theta(F)$. The effect of such a transformation on the bootstrap is very simple: a bootstrap realization $R^{*}=R^{*}\left(\mathbf{X}^{*}, \hat{F}\right)=t\left(\mathbf{X}^{*}\right)-\theta(F)$ transforms into $S=S\left(\mathbf{X}^{*}, \hat{F}\right)=g\left(t\left(\mathbf{X}^{*}\right)\right)-g(\theta(\hat{F}))$, or more simply

$$
S^{*}=g\left(R^{*}+\hat{\theta}\right)-g(\hat{\theta})
$$

so the bootstrap distribution of $R^{*}$ transforms into that of $S^{*}$ by (8.1).
Figure 1 illustrates a simple example. Miller [14], page 12, gives 9 pairs of numbers having sample Pearson correlation coefficient $\hat{\rho}=.945$. The top half of Figure 1 shows the histogram of $N=1000$ bootstrap replications of $\hat{\rho}^{*}-\hat{\rho}$, the bottom half the corresponding histogram of $\tanh ^{-1} \hat{\rho}^{*}-\tanh ^{-1} \hat{\rho}$. The first distribution straggles off to the left, the second distribution to the right. The median is above zero, but only slightly so compared to the spread of the distributions, indicating that bias correction is not likely to be important in this example.
The purpose of making transformations is, presumably, to improve the inference process. In the example above we might be willing to believe, on the basis of normal theory, that $\tanh ^{-1} \hat{\rho}-\tanh ^{-1} \rho$ is more nearly pivotal than $\hat{\rho}-\rho$ (see

![](https://cdn.mathpix.com/cropped/30bdd573-cfe1-492f-8bad-87e533904dd9-20.jpg?height=1748&width=1242&top_left_y=352&top_left_x=308)
FIG. 1. The top histogram shows $N=1000$ bootstrap replications of $\hat{\rho}^{*}-\hat{\rho}$ for the nine data pairs from Miller [10]: $(1.15,1.38),(1.70,1.72),(1.42,1.59)$, $(1.38,1.47),(2.80,1.66),(4.70,3.45),(4.80,3.87),(1.41,1.31),(3.90,3.75)$. The bottom histogram shows the corresponding replications for $\tanh ^{-1} \hat{\rho}^{*}$ $\tanh ^{-1} \hat{\rho}$. The $1 / 6,1 / 2$, and $5 / 6$ quantiles are shown for both distributions. All quantiles transform according to equation (8.1).



Remark E) and so more worthwhile investigating by the bootstrap procedure. This does not mean that the bootstrap gives more accurate results, only that the results are more useful. Notice that if $g(\cdot)$ is monotone, then any quantile of the bootstrap distribution of $R^{*}$ maps into the corresponding quantile of $S^{*}$ via (8.1), and vice-versa. In particular, if we use the median (rather than the mean) to estimate the center of the bootstrap distribution, then we get the same answer working directly with $\hat{\theta}^{*}-\hat{\theta}$ ( $\hat{\rho}^{*}-\hat{\rho}$ in the example), or first transforming to $\hat{\phi}^{*}-\hat{\phi} \left(\tanh ^{-1} \hat{\rho}^{*}-\tanh ^{-1} \hat{\rho}\right)$, taking the median, and finally transforming back to the original scale.

Remark C. The bias and variance expressions (5.11) suggested by the infinitesimal jackknife transform exactly as in more familiar applications of the "delta method." That is, if $\phi=g(\theta), \hat{\phi}=g(\hat{\theta})$ as above, and $\widehat{\operatorname{Bias}}_{F} \hat{\theta}, \widehat{\operatorname{Var}}_{F} \hat{\theta}$ are as given in formula (5.11), then it is easy to show that

$$
\begin{aligned}
& \widehat{\operatorname{Bias}}_{F} \hat{\phi}=g^{\prime}(\hat{\theta}) \widehat{\operatorname{Bias}}_{F} \hat{\theta}+\frac{g^{\prime \prime}(\hat{\theta})}{2} \widehat{\operatorname{Var}}_{F} \hat{\theta} \\
& \widehat{\operatorname{Var}}_{F} \hat{\phi}=\left[g^{\prime}(\hat{\theta})\right]^{2} \widehat{\operatorname{Var}}_{F}^{\prime} \hat{\theta}
\end{aligned}
$$

In the context of this paper, the infinitesimal jackknife is the delta method; starting from a known distribution, that of $\mathbf{P}^{*}$, approximations to the moments of an arbitrary function $R\left(\mathbf{P}^{*}\right)$ are derived by Taylor series expansion. See Gray et al. [4] for a closely related result.

Remark D. A standard nonparametric confidence statement for the median $\theta(F), n=13$, is

$$
\operatorname{Prob}_{F}\left\{x_{(4)}<\theta<x_{(10)}\right\}=\operatorname{Prob}\left\{4 \leqslant \operatorname{Bi}\left(13, \frac{1}{2}\right) \leqslant 9\right\}=.908 .
$$

If we make the continuity correction of halving the end point probabilities, (3.6) gives

$$
\operatorname{Prob}_{*}\left\{x_{(4)}<\hat{\theta}^{*}<x_{(10)}\right\}=.914
$$

where $\hat{\theta}^{*}=X_{(m)}^{*}$, the bootstrap value of the sample median. The agreement of (8.4) with (8.3) looks striking, until we try to use (8.4) for inference about $\theta$; (8.4) can be rewritten as $\operatorname{Prob}_{*}\left\{x_{(4)}-x_{(7)}<\hat{\theta}^{*}-\hat{\theta}<x_{(10)}-x_{(7)}\right\}$ (remembering that $\hat{\theta}= x_{(7)}$ ), which suggests

$$
\operatorname{Prob}_{F}\left\{x_{(4)}-x_{(7)}<\hat{\theta}-\theta<x_{(10)}-x_{(7)}\right\} \approx .914 .
$$

The resulting confidence interval statement for $\theta$, again using $\hat{\theta}=x_{(7)}$, is

$$
\operatorname{Prob}_{F}\left\{2 x_{(7)}-x_{(10)}<\theta<2 x_{(7)}-x_{(4)}\right\} \approx .914,
$$

which is the reflection of interval (8.3) about the median!
The trouble here has nothing in particular to do with the bootstrap, and does not arise from the possibly large approximation error in statement (8.5), but rather in the inferential step from (8.5) to (8.6), which tries to use $\hat{\theta}-\theta$ as a pivotal quantity.

The same difficulty can be exhibited in parametric families: suppose we know that $F$ is a translation of a standard exponential distribution (density $e^{-x}, x>0$ ). Then there exist two positive numbers $a$ and $b, a<b$, such that $\operatorname{Prob}_{F}\{-a<\hat{\theta}-\theta< b\}=.91$. The corresponding interval statement $\operatorname{Prob}_{F}\left\{x_{(7)}-b<\theta<x_{(7)}+a\right\}=$ .91 will tend to look more like (8.6) than (8.3).

Remark E. The difficulty above is a reminder that the bootstrap, and the jackknife, provide approximate frequency statements, not approximate likelihood statements. Fundamental inference problems remain, no matter how well the bootstrap works. For example, even if the bootstrap expectation $E_{*}\left(\hat{\theta}^{*}-\theta\right)^{2}$ very accurately estimates $E_{F}(\hat{\theta}-\theta)^{2}$, the resulting interval estimate for $\theta$ given $\hat{\theta}$ will be useless if small changes in $F$ (or more exactly, in $\theta(F)$ ), result in large changes in $E_{F}(\hat{\theta}-\theta)^{2}$.

For the correlation coefficient, as discussed in Remark B, Fisher showed that $\tanh ^{-1} \hat{\rho}-\tanh ^{-1} \rho$ is nearly pivotal when sampling from bivariate normal populations. That is, its distribution is nearly the same for all bivariate normal populations, at least in the range $-.9<\rho<.9$. This property tends to ameliorate inference difficulties, and is the principal reason for transforming variables, as in Remark B. The theory of pivotal quantities is well developed in parametric families, see Barnard [2], but not in the nonparametric context of this paper.

Remark F. The classic pivotal quantity is Student's $t$-statistic. Tukey has suggested using the analogous quantity (2.3) for hypothesis testing purposes, relying on the standard $t$ tables for significance points. This amounts to treating (2.3) as a pivotal quantity for all choices of $F, \theta(F)$, and $t(\mathbf{X})$. The only theoretical justifications for this rather optimistic assumption apply to large samples, where the Student $t$ effect rapidly becomes negligible, see Miller [14]. Given the current state of the theory, one is as well justified in comparing (2.3) to a $\mathscr{N}(0,1)$ distribution as to a Student's $t$ distribution (except when $t(\mathbf{X})=\bar{X}$ ).

An alternative approach is to bootstrap (2.3) by Method 2 to obtain a direct estimate of its distribution, instead of relying on the $t$ distribution, and then compare the observed value of (2.3) to the bootstrap distribution.

Remark G. The rationale for bootstrap methods becomes particularly clear when the sample space $\mathscr{X}$ of the $X_{i}$ is a finite set, say

$$
\mathfrak{X}=\{1,2,3, \ldots, L\} .
$$

The distribution $F$ can now be represented by the vector of probabilities $\mathbf{f}= \left(f_{1}, f_{2}, \ldots, f_{L}\right), f_{l}=\operatorname{Prob}_{F}\left\{X_{i}=l\right\}$. For a given random sample $\mathbf{X}$ let $\hat{f}_{l}=\#\left\{X_{i}=\right. l\} / n$ and $\hat{\mathbf{f}}=\left(\hat{f}_{1}, \hat{f}_{2}, \ldots, \hat{f}_{L}\right)$, so that if $R(\mathbf{X}, F)$ is symmetrically defined in the components of $\mathbf{X}$ we can write it as a function of $\hat{\mathbf{f}}$ and $\mathbf{f}$, say

$$
R(\mathbf{X}, F)=Q(\hat{\mathbf{f}}, \mathbf{f}) .
$$

Likewise $R\left(\mathbf{X}^{*}, \hat{F}\right)=Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$, where $\hat{f}_{l}^{*}=\#\left\{X_{i}^{*}=l\right\} / n$ and $\hat{\mathbf{f}}^{*}= \left(\hat{f_{1}^{*}}, \hat{f_{2}^{*}}, \ldots, \hat{f}_{L}^{*}\right)$.

Bootstrap methods estimate the sampling distribution of $Q(\hat{\mathbf{f}}, \mathbf{f})$, given the true distribution $\mathbf{f}$, by the conditional distribution of $Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$ given the observed value of $\hat{\mathbf{f}}$. This is plausible because

$$
\hat{\mathbf{f}} \mid \mathbf{f} \sim \mathfrak{M}_{L}(n, \mathbf{f}) \quad \text { and } \quad \hat{\mathbf{f}}^{*} \mid \hat{\mathbf{f}} \sim \mathfrak{M}_{L}(n, \hat{\mathbf{f}}),
$$

where $\mathfrak{N}_{L}(n, \mathbf{f})$ is the $L$-category multinomial distribution with sample size $n$, probability vector $\mathbf{f}$. In large samples we expect $\hat{\mathbf{f}}$ to be close to $\mathbf{f}$, so that for reasonable functions $Q(\cdot, \cdot)(8.9)$ should imply the approximate validity of the bootstrap method.

The asymptotic validity of the bootstrap is easy to verify in this framework, assuming some regularity conditions on $Q(\cdot, \cdot)$. Suppose that $Q(\mathbf{f}, \mathbf{f})=0$ for all $\mathbf{f}$ (as it does in the usual jackknife situation where $R(\mathbf{X}, F)=\theta(\hat{F})-\theta(F)$ ); that the vector $\mathbf{u}\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$ with $l$ th component equal to $\partial Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right) / \partial \hat{f}_{l}^{*}$ exists continuously for $\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$ in an open neighborhood of ( $\mathbf{f}, \mathbf{f}$ ); and that $\mathbf{u}=\mathbf{u}(\mathbf{f}, \mathbf{f})$ does not equal zero. By Taylor's theorem, and the fact that $\hat{\mathbf{f}}$ * and $\hat{\mathbf{f}}$ converge to $\mathbf{f}$ with probability one,

$$
Q(\hat{\mathbf{f}}, \mathbf{f})=(\hat{\mathbf{f}}-\mathbf{f})\left(\mathbf{u}+\boldsymbol{\epsilon}_{n}\right) \quad \text { and } \quad Q\left(\hat{\mathbf{f}}^{*}, \mathbf{f}\right)=\left(\hat{\mathbf{f}}^{*}-\hat{\mathbf{f}}\right)\left(\mathbf{u}+\hat{\boldsymbol{\epsilon}}_{n}\right),
$$

both $\boldsymbol{\epsilon}_{n}$ and $\hat{\boldsymbol{\epsilon}}_{n}$ converging to zero with probability one. From (8.9) and the fact that $\hat{\mathbf{f}}$ converges to $\mathbf{f}$ with probability one, we have

$$
\left.n^{\frac{1}{2}}(\hat{\mathbf{f}}-\mathbf{f}) \right\rvert\, \mathbf{f} \rightarrow \mathscr{M}_{L}\left(\mathbf{0}, Z_{f}\right) \quad \text { and } \left.\quad n^{\frac{1}{2}}(\hat{\mathbf{f}} *-\hat{\mathbf{f}}) \right\rvert\, \hat{\mathbf{f}} \rightarrow \mathscr{M}_{L}\left(\mathbf{0}, Z_{f}\right),
$$

where $\Sigma_{f}$ is the matrix with element ( $l, m$ ) equal to $f_{l}\left(\delta_{l m}-f_{m}\right)$. Combining (8.10) and (8.11) shows that the bootstrap distribution of $n^{\frac{1}{2}} Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$, given $\hat{\mathbf{f}}$, is asymptotically equivalent to the sampling distribution of $n^{\frac{1}{2}} Q(\hat{\mathbf{f}}, \mathbf{f})$, given the true probability distribution $\mathbf{f}$. Both have the limiting distribution $\mathscr{M}\left(0, \mathbf{u}^{\prime} Z_{f} \mathbf{u}\right)$.

The argument above assumes that the form of $Q(\cdot, \cdot)$ does not depend upon $n$. More careful considerations are necessary in cases like (2.3) where $Q(\cdot, \cdot)$ does depend on $n$, but in a minor way. Some nondifferentiable functions such as the sample median (3.3) can also be handled by a smoothing argument, though direct calculation of the limiting distribution is easier in that particular case.

Remark H. Taylor expansion (5.4) looks suspicious because the dimension of the vectors involved increases with the sample size $n$. However in situation (8.7), (8.8), it is easy to verify that (5.4) is the same as the second order Taylor expansion of $Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$, for $\hat{\mathbf{f}}^{*}$ near $\hat{\mathbf{f}}$,

$$
Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right) \doteq Q(\hat{\mathbf{f}}, \hat{\mathbf{f}})+\left(\hat{\mathbf{f}}^{*}-\hat{\mathbf{f}}\right) \hat{\mathbf{u}}+\frac{1}{2}\left(\hat{\mathbf{f}}^{*}-\hat{\mathbf{f}}\right) \hat{\mathbf{v}}\left(\hat{\mathbf{f}}^{*}-\hat{\mathbf{f}}\right) .
$$

Here $\hat{\mathbf{u}}$ has $l$ th element $\partial Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right) /\left.\partial \hat{\mathbf{f}}_{l}^{*}\right|_{\hat{\mathbf{f}}^{*}=\hat{\mathbf{f}}}$ and $\hat{\mathbf{v}}$ has $l, m$ th element $\partial^{2} Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right) /\left.\partial \hat{f}_{l}^{*} \partial f_{m}^{*}\right|_{\hat{\mathbf{f}}}=\hat{\mathbf{f}}$. The dimension of the vectors in (8.12) is $L$, and does not increase with sample size $n$. Expressions (5.8), (5.10) are the standard delta theory approximation for the mean and variance of $Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$, given $\hat{\mathbf{f}}$, obtained from (8.12) and the distributional properties of $\hat{\mathbf{f}}^{*} \mid \hat{\mathbf{f}} \sim \mathfrak{N}_{L}(n, \hat{\mathbf{f}})$.

Remark I. Hartigan [5, 7] has suggested using subsample values to obtain confidence statements for an estimated parameter. His method consists of choosing a vector $\mathbf{x}^{\boldsymbol{*}}$ whose components are a nonempty subset of the observed data vector $\mathbf{X}=\mathbf{x}$ (so each component $x_{i}$ appears either zero or one time in $\mathbf{x}^{*}$ ). This process is repeated $N$ times, where $N$ is small compared to $2^{n}$, giving vectors $\mathbf{x}^{\boldsymbol{*} \mathbf{1}}, \mathbf{x}^{\boldsymbol{*} \mathbf{2}}, \cdots, \mathbf{x}^{\boldsymbol{*} N}$ and corresponding subsample values $t\left(\mathbf{x}^{\boldsymbol{*} \mathbf{1}}\right), t\left(\mathbf{x}^{\boldsymbol{*} \mathbf{2}}\right), \cdots, t\left(\mathbf{x}^{\boldsymbol{*} \boldsymbol{N}}\right)$ for some symmetric estimator $t(\cdot)$ defined for samples of an arbitrary size. By a clever choice of the vectors $\mathbf{x}^{* j}$, and for certain special estimation problems, the $t\left(\mathbf{x}^{* j}\right)$ can be used to make precise confidence statements about an unknown parameter. More importantly in the context of this paper, Hartigan shows that by choosing the $\mathbf{x}^{* j}$ randomly, without replacement, from the $2^{n}-1$ possible nonempty subsamples of $x$, asymptotically valid confidence statements can be made under fairly general conditions. This is very similar to bootstrap Method 2, except that the $\mathbf{x}^{* j}$ are selected by subsampling rather than bootstrapping.

In the finite case (8.7), let $\mathbf{x}^{\boldsymbol{*}}$ be a randomly selected subsample vector, and let $\hat{f_{l}^{*}}=\#\left\{x_{i}^{*}=l\right\} /\left(\right.$ number of components of $\left.\mathbf{x}^{*}\right)$, so $\hat{\mathbf{f}^{*}}=\left(\hat{f_{1}^{*}}, \hat{f_{2}^{*}}, \cdots, \hat{f_{L}^{*}}\right)$, as before, is the vector of proportions in the artificially created sample. It is easy to show that $\left.n^{\frac{1}{2}}\left(\hat{\mathbf{f}}^{*}-\hat{\mathbf{f}}\right) \right\rvert\, \hat{\mathbf{f}} \rightarrow \mathscr{T}_{L}\left(\mathbf{0}, \Sigma_{f}\right)$, as at (8.11), which is all that is needed to get the same asymptotic properties obtained for the bootstrap. (Conversely, it can be shown that bootstrap samples have the same asymptotic "typicality" properties Hartigan discusses in [5, 7].) The bootstrap may give better small sample performance, because the similarity in (8.9), which is unique to the bootstrap, is a stronger property than the asymptotic equivalence (8.11), and also because the artificial samples used by the bootstrap are the same size as the original sample. However, no evidence one way or the other is available at the present time.

Hartigan's 1971 paper [6] introduces another method of resampling, useful for constructing prediction intervals, which only involves artificial samples of the same size as the real sample. Let $\left\{x_{1}^{*}, x_{2}^{*}, \cdots, x_{n}^{*}\right\}$ be a set of size $n$, each element of which is selected with replacement from $\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$. There are $\binom{2 n-1}{n-1}$ distinct such sets, not counting differences in the order of selection. (For example $\left\{x_{1}, x_{2}\right\}$ yields the three sets $\left\{x_{1}, x_{1}\right\},\left\{x_{2}, x_{2}\right\},\left\{x_{1}, x_{2}\right\}$.) The random version of Hartigan's second method selects $\mathbf{x}^{\boldsymbol{*}}$, or more exactly the set of components of $\mathbf{x}^{\boldsymbol{*}}$, with equal probability from among these $\binom{2 n-1}{n-1}$ possible choices. It can be shown that this results in $\left.n^{\frac{1}{2}}\left(\hat{\mathbf{f}}^{*}-\hat{\mathbf{f}}\right) \right\rvert\, \hat{\mathbf{f}} \rightarrow \Re_{L}\left(\mathbf{0}, 2 Z_{f}\right)$, so that the asymptotic covariance matrix is twice what it is in (8.11). Looking at (8.10), one sees that for this resampling scheme, $2^{-\frac{1}{2}} Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$ has the same asymptotic distribution as $Q(\hat{\mathbf{f}}, \mathbf{f})$.

It is not difficult to construct other resampling schemes which give correct asymptotic properties. The important question, but one which has not been investigated, is which scheme is most efficient and reliable in small samples.

Remark J. In situation (8.7), (8.8), the ordinary jackknife depends on evaluating $Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$ for vectors $\hat{\mathbf{f}}^{*}$ of the form $\hat{\mathbf{f}}_{(l)}^{*}$,

$$
\left(\hat{\mathbf{f}}_{(l)}^{*}-\hat{\mathbf{f}}\right)=\frac{1}{n-1}\left(\hat{\mathbf{f}}-\mathbf{e}_{l}\right)
$$

$\mathbf{e}_{l}=(0,0, \ldots, 1,0, \ldots, 0), 1$ in the $l$ th place. (The values of $l$ needed are those occurring in the observed sample $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$; a maximum of $\min (n, L)$ different $l$ values are possible.) Notice that

$$
\left\|\hat{\boldsymbol{f}}_{(l)}^{*}-\hat{\boldsymbol{f}}\right\| \leqslant \frac{2^{\frac{1}{2}}}{n-1}
$$

The "resampling" vectors $\hat{\boldsymbol{f}}_{(l)}^{*}$ are distance $O(1 / n)$ away from $\hat{\mathbf{f}}$, as compared to $O_{p}\left(n^{-\frac{1}{2}}\right)$ for the bootstrap vectors $\hat{\mathbf{f}}^{*}$, as seen in (8.11). In the case of the median, (3.3), the jackknife fails because of its overdependence on the behavior of $Q\left(\hat{\mathbf{f}}^{*}, \hat{\mathbf{f}}\right)$ for $\hat{\mathbf{f}}^{*}$ very near $\hat{\mathbf{f}}$. In this case the derivative of the function $Q(\cdot, \cdot)$ is too irregular for the jackknife's quadratic extrapolation formulas to work. The grouped jackknife, in which the $\hat{\mathbf{f}}^{*}$ vectors are created by removing observations from $\mathbf{x}$ in groups of size $g$ at a time, see page 1 of Miller [14], overcomes this objection if $g$ is sufficiently large. (The calculations above suggest $g=O\left(n^{\frac{1}{2}}\right)$.) As a matter of fact, the grouped jackknife gives the correct asymptotic variance for the median. If $g$ is really large, say $g=n / 2$, and the removal groups are chosen randomly, then this resampling method is almost the same as Hartigan's subsampling plan, discussed in Remark I.

Remark K. We have applied the bootstrap in a nonparametric way, but there is no reason why it cannot be used in parametric problems. The only change necessary is that at (2.4), $\hat{F}$ is chosen to be the parametric m.le. for $F$, rather than the nonparametric m.l.e. As an example, suppose that $F$ is known to be normal, with unknown mean and variance, and that we are interested in the expectation of $R(\mathbf{X}, F)=I_{[a, b]}(\bar{X})$, i.e., the probability that $\bar{X}$ occurs in a prespecified interval $[a, b]$. Then the nonparametric bootstrap estimate is $E_{*} R^{*}=\hat{G}^{(n)}(b)-\hat{G}^{(n)}(a)$, where $\hat{G}^{(n)}$ is the cdf of $\sum_{i=1}^{n} X_{i}^{*} / n$, obtained by convoluting the sample distribution $\hat{F} n$ times and then rescaling by division by $n$. The parametric bootstrap estimate is $E_{*} R^{*}=\Phi\left((b-\bar{x}) /\left(\hat{\sigma}-n^{\frac{1}{2}}\right)\right)-\Phi\left((a-\bar{x}) /\left(\hat{\sigma} / n^{\frac{1}{2}}\right)\right)$, where $\hat{\sigma}=\hat{\mu}_{2}{ }^{\frac{1}{2}}$ and $\Phi(\cdot)$ is the standard normal cdf. If $F$ is really normal and if $n$ is moderately large, $n \geqslant 20$ according to standard Edgeworth series calculations, then the two estimates will usually be in close agreement.

It can be shown that the parametric version of Method 3 of the bootstrap, applied to estimating the variance of the m.l.e. in a one parameter family, gives the usual approximation: one over the Fisher information. The calculation is almost the same as that appearing in Section 3 of Jaeckel [10].

Acknowledgments. I am grateful to Professors Rupert Miller and David Hinkley for numerous discussions, suggestions and references, and to Joseph Verducci for help with the numerical computations. The referees contributed several helpful ideas, especially concerning the connection with Hartigan's work, and the large sample theory. I also wish to thank the many friends who suggested names more colorful than Bootstrap, including Swiss Army Knife, Meat Axe, Swan-Dive, Jack-Rabbit, and my personal favorite, the Shotgun, which, to paraphrase Tukey, "can blow the head off any problem if the statistician can stand the resulting mess."

## REFERENCES

[1] Anderson, T. W. (1958). An Introduction to Multivariate Statistical Analysis. Wiley, New York.
[2] Barnard, B. (1974). Conditionality, pivotals, and robust estimation. Proceedings of the Conference on Foundational Questions in Statistical Inference. Memoirs No. 1, Dept. of Theoretical Statist., Univ. of Aarhus, Denmark.
[3] Cramér, H. (1946). Mathematical Methods in Statistics. Princeton Univ. Press.
[4] Gray, H., Schucany, W. and Watkins, T. (1975). On the generalized jackknife and its relation to statistical differentials. Biometrika 62 637-642.
[5] Hartigan, J. A. (1969). Using subsample values as typical values. J. Amer. Statist. Assoc. 64 1303-1317.
[6] Hartigan, J. A. (1971). Error analysis by replaced samples. J. Roy. Statist. Soc. Ser. B 33 98-110.
[7] Hartigan, J. A. (1975). Necessary and sufficient conditions for asymptotic joint normality of a statistic and its subsample values. Ann. Statist. 3573-580.
[8] Hinkley, D. (1976 ${ }^{\text {a }}$ ). On estimating a symmetric distribution. Biometrika 63680.
[9] Hinkley, D. $\left(1976{ }^{\text {b }}\right)$. On jackknifing in unbalanced situations. Tèchnical Report No. 22, Division of Biostatistics, Stanford Univ.
[10] Jaeckel, L. (1972). The infinitesimal jackknife. Bell Laboratories Memorandum \#MM 72-1215-11.
[11] Kendall, M. and Stuart, A. (1950). The Advanced Theory of Statistics. Hafner, New York.
[12] Lachenbruch, P. and Mickey, R. (1968). Estimation of error rates in discriminant analysis. Technometrics 10 1-11.
[13] Maritz, J. S. and Jarrett, R. G. (1978). A note on estimating the variance of the sample median. J. Amer. Statist. Assoc. 73 194-196.
[14] Miller, R. G. (1974). The jackknife-a review. Biometrika 61 1-15.
[15] Miller, R. G. (1974) ${ }^{\text {b }}$ ). An unbalanced jackknife. Ann. Statist. 2 880-891.
[16] Noether, G. (1967). Elements of Nonparametric Statistics. Wiley, New York.
[17] Toussaint, G. (1974). Bibliography on estimation of misclassification. IEEE Trans. Information Theory 20 472-479.

Department of Statistics
Stanford University
Stanford, California 94305

