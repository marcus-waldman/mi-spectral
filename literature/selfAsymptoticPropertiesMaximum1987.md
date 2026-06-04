---
citekey: selfAsymptoticPropertiesMaximum1987
item_type: article
authors: 'Self, Steven G. and Liang, Kung-Yee'
year: 1987
title: 'Asymptotic {Properties} of {Maximum Likelihood Estimators} and {Likelihood Ratio Tests} under {Nonstandard Conditions}'
venue: Journal of the American Statistical Association
volume: 82
issue: 398
pages: 605--610
doi: 10.1080/01621459.1987.10478472
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\self_asymptotic_properties_maximum_1987.pdf'
pdf_sha256: 3bf99818a63b7dde58c82e5978681829c4372f17c8d2f9c2f46d123508ccd797
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-06-04T16:25:20Z
---
# Asymptotic Properties of Maximum Likelihood Estimators and Likelihood Ratio Tests Under Nonstandard Conditions 

Author(s): Steven G. Self and Kung-Yee Liang
Source: Journal of the American Statistical Association, Vol. 82, No. 398 (Jun., 1987), pp. 605-610
Published by: Taylor \& Francis on behalf of the American Statistical Association
Stable URL: https://www.jstor.org/stable/2289471
Accessed: 04-06-2026 15:43 UTC

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about TSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms \& Conditions of Use, available at https://about.jstor.org/terms

# Asymptotic Properties of Maximum Likelihood Estimators and Likelihood Ratio Tests Under Nonstandard Conditions 

STEVEN G. SELF and KUNG-YEE LIANG*


#### Abstract

Large sample properties of the likelihood function when the true parameter value may be on the boundary of the parameter space are described. Specifically, the asymptotic distribution of maximum likelihood estimators and likelihood ratio statistics are derived. These results generalize the work of Moran (1971), Chant (1974), and Chernoff (1954). Some of Chant's results are shown to be incorrect.

The approach used in deriving these results follows from comments made by Moran and Chant. The problem is shown to be asymptotically equivalent to the problem of estimating the restricted mean of a multivariate Gaussian distribution from a sample of size 1. In this representation the Gaussian random variable corresponds to the limit of the normalized score statistic and the estimate of the mean corresponds to the limit of the normalized maximum likelihood estimator. Thus the limiting distribution of the maximum likelihood estimator is the same as the distribution of the projection of the Gaussian random variable onto the region of admissible values for the mean. A variety of examples is provided for which the limiting distributions of likelihood ratio statistics are mixtures of chi-squared distributions. One example is provided with a nuisance parameter on the boundary for which the asymptotic distribution is not a mixture of chi-squared distributions.


KEY WORD: Boundary.

## 1. INTRODUCTION

The purpose of this article is to derive large sample properties of the likelihood surface under conditions similar to Cramér's (1946) but allowing the true parameter value to be on the boundary of the parameter space. The results are stated in terms of properties of maximum likelihood estimators in the loose sense. By analogy to Kulldorf (1957), we define any point in the parameter space at which a local maximum of the likelihood function occurs to be a maximum likelihood estimator in the loose sense. The results presented include the existence of a consistent maximum likelihood estimator, the large sample distribution of that estimator, and the large sample distribution of likelihood ratio statistics.

Previous work in this area includes that done by Moran (1971) and Chant (1974), who investigated the large sample distribution of maximum likelihood estimators. Moran considered the special case of a rectangular parameter space with at most two coordinates of the parameter on the boundary. Chant described the relationship between the $\mathrm{C}(\alpha)$ test and tests based on maximum likelihood estimators. In discussing their results, both Moran and Chant mentioned the asymptotic equivalence of this problem with the problem of estimating the restricted mean of a multivariate Gaussian distribution. The approach taken

[^0]here may be considered a rigorous development of these comments.

Let $f(x ; \theta)$ be the probability density function of a random variable $X$ indexed by $\theta=\left(\theta_{1}, \ldots, \theta_{p}\right)$, where $\theta$ takes values in the parameter space $\Omega$, a subset of $R^{P}$. We assume that distinct values of $\theta$ correspond to distinct probability distributions. Let $X_{1}, \ldots, X_{N}$ be $N$ independent observations on $X$ and denote the log-likelihood function, $\sum \log f\left(X_{i} ; \theta\right)$, by $l_{N}(\theta)$. We assume the almost sure existence of the first three derivatives of $l_{N}(\theta)$ with respect to $\theta$ on the intersection of neighborhoods of the true parameter value and $\Omega$. If the true parameter value, denoted by $\theta_{0}$, is on the boundary of $\Omega$, the derivatives of $l_{N}(\theta)$ are taken from the appropriate side. Moreover, on the intersection of neighborhoods of $\theta_{0}$ and $\Omega, N^{-1}$ times the absolute value of the third derivative of $l_{N}(\theta)$ is bounded by a function of $X_{1}, \ldots, X_{N}$ whose expectation exists. We denote the first two derivatives of $l_{N}(\theta)$ by $U_{N}(\theta)$ and $-I_{N}(\theta)$, respectively. Finally, the expectation of $N^{-1} I_{N}(\theta)$, denoted by $I(\theta)$, is assumed to be positive definite on neighborhoods of $\theta_{0}$ and at $\theta_{0}$ is equal to the variancecovariance matrix of $N^{-1 / 2} U_{N}\left(\theta_{0}\right)$.

## 2. CONSISTENCY AND WEAK CONVERGENCE OF THE MAXIMUM LIKELIHOOD ESTIMATOR

Following Chernoff (1954), we offer the following definition:

Definition. The set $\Omega \subset R^{P}$ is approximated at $\theta_{0}$ by a cone with vertex at $\theta_{0}, C_{\Omega}$, if
(1) $\inf _{x \in C_{\Omega}}\|x-y\|=o\left(\left\|y-\theta_{0}\right\|\right)$ for all $y \in \Omega$
and
(2) $\inf _{y \in \Omega}\|x-y\|=o\left(\left\|x-\theta_{0}\right\|\right)$ for all $x \in C_{\Omega}$.

Recall that a cone with vertex at $\theta_{0}, C$, is a set of points such that if $x \in C$ then $a\left(x-\theta_{0}\right)+\theta_{0} \in C$, where $a$ is any real, nonnegative number. Let $C-\theta_{0}$ denote the set obtained by translating a cone, $C$, with vertex at $\theta_{0}$ so that its vertex lies at the origin. From now on we will assume that $\Omega$ is regular enough to be approximated by a cone with vertex at $\theta_{0}$. This condition is mild enough to encompass a wide variety of shapes for $\Omega$. For instance, it is easy to show that a sphere may be approximated at a point by the plane tangent to the sphere at that point.

We first give a consistency result for the maximum like-
© 1987 American Statistical Association Journal of the American Statistical Association June 1987, Vol. 82, No. 398, Theory and Methods
lihood estimator when $\theta_{0}$ is on the boundary of $\Omega$. For this result we require that near $\theta_{0}, \Omega$ behave like a closed set. Specifically, we will assume that the intersection of $\Omega$ and the closure of neighborhoods centered about $\theta_{0}$ constitute closed subsets of $R^{P}$.

Theorem 1. If the foregoing conditions hold, then with probability tending to 1 as $N \rightarrow \infty$ there exists a sequence of points in $\Omega, \hat{\theta}_{N}$, at which local maxima of $l_{N}(\theta)$ occur, and that converges to $\theta_{0}$ in probability. Moreover, $N^{1 / 2}\left(\hat{\theta}_{N}-\theta_{0}\right)=O_{p}(1)$.

Proof. Pick $\delta>0$. Since the intersection of $\Omega$ and the closure of a $\delta$ neighborhood about $\theta_{0}$ is closed, $l_{N}(\theta)$ must have a local maximum on this set. If it can be shown that this maximum occurs at a point in $\Omega$ at a distance from $\theta_{0}$ less than $\delta$ with probability tending toward 1 , then the existence and consistency of $\hat{\theta}_{N}$ will follow immediately. This may be shown by proving that $l_{N}(\theta)<l_{N}\left(\theta_{0}\right)$ with probability tending toward 1 for all $\theta$ in $\Omega$ that are at a distance $\delta$ from $\theta_{0}$. The same argument used by Lehmann (1983, pp. 429-432), which relies on a Taylor series expansion of $l_{N}(\theta)$ about $\theta_{0}$, may be used to establish this inequality. The root- $N$ consistency then follows from arguments in Chernoff's (1954) lemma 1.

To show weak convergence of $\hat{\theta}_{N}$, we proceed in two steps. First, a quadratic approximation to $l_{N}(\theta)$ is made and the value of $\theta$ that maximizes this quadratic function, $\tilde{\theta}_{N}$, is shown to be asymptotically equivalent to $\hat{\theta}_{N}$. The large sample distribution of $\tilde{\theta}_{N}$ is then derived by arguments similar to those of Chernoff (1954).

Lemma 1. Under the conditions stated in Section 1 and for all $\theta$ such that $\theta-\theta_{0}=O_{p}\left(N^{-1 / 2}\right)$, two times $N^{-1} l_{N}(\theta)-N^{-1} l_{N}\left(\theta_{0}\right)$ is equal to

$$
\begin{aligned}
& -\left(Z_{N}-\left(\theta-\theta_{0}\right)\right)^{\prime} I\left(\theta_{0}\right)\left(Z_{N}-\left(\theta-\theta_{0}\right)\right) \\
& \quad+N^{-2} U_{N}^{\prime}\left(\theta_{0}\right) I^{-1}\left(\theta_{0}\right) U_{N}\left(\theta_{0}\right)+O_{p}(1)\left\|\theta-\theta_{0}\right\|^{3}
\end{aligned}
$$

where $Z_{N}=N^{-1} I^{-1}\left(\theta_{0}\right) U_{N}\left(\theta_{0}\right)$. Moreover, if $\Omega$ is convex in a neighborhood of $\theta_{0}$ then $N^{1 / 2}\left|\hat{\theta}_{N}-\tilde{\theta}_{N}\right|=o_{p}(1)$, where $\tilde{\theta}_{N}$ is the value of $\theta$ in $\Omega$ at which the first term in (2.1) is maximized.

Proof. Expression (2.1) follows from a Taylor series expansion of $l_{N}(\theta)$ about $\theta_{0}$ and a reexpression in terms of $Z_{N}$. To show that $N^{1 / 2}\left|\hat{\theta}_{N}-\tilde{\theta}_{N}\right|=o_{p}(1)$, let $g_{N}(\theta)$ denote the first two terms in expression (2.1) and let $r_{N}(\theta)$ denote the last term. Because $g_{N}$ is a positive definite quadratic function, the desired result will follow from the convexity of $\Omega$ upon showing that $\left|g_{N}\left(\hat{\theta}_{N}\right)-g_{N}\left(\tilde{\theta}_{N}\right)\right|$ is $o_{p}\left(N^{-1}\right)$. By using (2.1) we have

$$
\begin{aligned}
0 \leq 2 N^{-1}\left[l_{N}\left(\hat{\theta}_{N}\right)\right. & \left.-l_{N}\left(\tilde{\theta}_{N}\right)\right] \\
& =g_{N}\left(\hat{\theta}_{N}\right)-g_{N}\left(\tilde{\theta}_{N}\right)+r_{N}\left(\hat{\theta}_{N}\right)-r_{N}\left(\hat{\theta}_{N}\right)
\end{aligned}
$$

Since $g_{N}\left(\hat{\theta}_{N}\right)-g_{N}\left(\tilde{\theta}_{N}\right)$ is negative, it follows that it must be bounded in absolute value by $r_{N}\left(\hat{\theta}_{N}\right)-r_{N}\left(\tilde{\theta}_{N}\right)$. This term is seen to be $O_{p}\left(N^{-3 / 2}\right)$ by the results of Theorem 1 and by noting that the same arguments used in Theorem 1 may be applied to demonstrate the root- $N$ consistency of $\tilde{\theta}_{N}$.

We now derive a representation for the asymptotic distribution of $N^{1 / 2}\left(\hat{\theta}_{N}-\theta_{0}\right)$.

Theorem 2. Let $Z$ be a random variable with a multivariate Gaussian distribution with mean $\theta$ and covariance matrix $I^{-1}\left(\theta_{0}\right)$, where $\theta$ is restricted to lie in $C_{\Omega}-\theta_{0}$. Let $F$ denote the distribution of the maximum likelihood estimate of $\theta$ based on a single realization of $Z$ when $\theta=0$, hereafter denoted by $\hat{\theta}$. Then under the conditions given previously, the limiting distribution of $N^{1 / 2}\left(\hat{\theta}_{N}-\theta_{0}\right)$ equals $F$.

Proof. Two approximations are made. First, $\Omega$ is approximated by $C_{\Omega}$ as the set over which $l_{N}(\theta)$ is maximized. This is justified by the root- $N$ consistency of $\hat{\theta}_{N}$ and the definition of approximating cones given previously. The second approximation, justified in Lemma 1, replaces $l_{N}(\theta)$ by the quadratic form

$$
\left(N^{1 / 2} Z_{N}-N^{1 / 2}\left(\theta-\theta_{0}\right)\right)^{\prime} I\left(\theta_{0}\right)\left(N^{1 / 2} Z_{N}-N^{1 / 2}\left(\theta-\theta_{0}\right)\right) .
$$

This expression is maximized over values of $\theta$ in $C_{\Omega}$ or, equivalently, values of $N^{1 / 2}\left(\theta-\theta_{0}\right)$ in $C_{\Omega}-\theta_{0}$. The result follows upon noting that the limit law of $N^{1 / 2} Z_{N}$ is multivariate Gaussian with mean 0 and covariance matrix $I^{-1}\left(\theta_{0}\right)$.

Although the representation given in Theorem 2 reduces the general problem of computing the limiting distribution of $N^{1 / 2}\left(\hat{\theta}_{N}-\theta_{0}\right)$ to a single class of considerably simpler problems, the solution to the simpler problem in any given case might still be rather arduous. We now offer several special cases in which the representation given in Theorem 2 may be used to compute the limiting distribution of $N^{1 / 2}\left(\hat{\theta}_{N}-\theta_{0}\right)$.

Case 1. Suppose that $\theta_{0}$ is an interior point of $\Omega$. Then $C_{\Omega}-\theta_{0}=R^{P}$. The maximum likelihood estimator, $\hat{\theta}$, in the previous representation equals $Z$, so $F$ is multivariate Gaussian with mean 0 and covariance matrix $I^{-1}\left(\theta_{0}\right)$.

Case 2. Suppose that $\Omega=\Omega_{1} \times \cdots \times \Omega_{p}$, where $\Omega_{i}$ are closed intervals in $R^{1}$ and $\theta_{01}$ is a left endpoint of $\Omega_{1}$ and $\theta_{0 i}$ are interior points of $\Omega_{i}$ for $2 \leq i \leq p$. Then $C_{\Omega}- \theta_{0}=[0, \infty) \times R^{p-1}$ and $\hat{\theta}$ has the representation
$\left[\begin{array}{c}Z_{1} \\ Z_{2} \\ \vdots \\ Z_{p}\end{array}\right] I\left\{Z_{1}>0\right\}+\left[\begin{array}{c}0 \\ Z_{2}-\left(I^{21} / I^{11}\right) Z_{1} \\ \vdots \\ Z_{p}-\left(I^{p 1} / I^{11}\right) Z_{1}\end{array}\right] I\left\{Z_{1}<0\right\}$,
where $I^{i j}=I^{i j}\left(\theta_{0}\right)$ are elements of the matrix $I^{-1}\left(\theta_{0}\right)$. Upon noting that the elements of the vector in the second term in (2.2) and the event $\left\{Z_{1}<0\right\}$ are independent, we see that this representation corresponds to the result described in Moran's (1971) theorem 1 and Chant's (1974) case (i). The vector in the second term in (2.2) is simply the projection of $Z$ onto the half-plane $\left\{Z_{1} \geq 0\right\}$, where the projection is taken according to the metric defined by $I\left(\theta_{0}\right)$.

In the previous example, the fact that $\hat{\theta}$ is multivariate Gaussian conditional on $\hat{\theta}_{1}=0$ stems from the fact that the event $\left\{Z_{1}<0\right\}$ and components of $\hat{\theta}$ in the second term of (2.2) are independent. This independence between elements of $\hat{\theta}$ and events characterizing which coordinates
of $\hat{\theta}$ are zero does not obtain when there is more than one coordinate of $\theta_{0}$ on the boundary. For example, let $p= 2, C_{\Omega}=[0, \infty) \times[0, \infty)$, and $\theta_{01}=\theta_{02}=0$. Then $\hat{\theta}^{\prime}$ may be written as $(0,0),\left(0, Z_{2}-\left(I^{21} / I^{11}\right) Z_{1}\right),\left(Z_{1}-\left(I^{12} / I^{22}\right) Z_{2}\right.$, 0 ), or ( $Z_{1}, Z_{2}$ ) depending in which of four regions ( $Z_{1}, Z_{2}$ ) falls. The regions are given by $\left\{Z_{1}-\left(I^{12} / I^{11}\right) Z_{2}<0, Z_{2}\right. \left.-\left(I^{21} / I^{11}\right) Z_{1}<0\right\},\left\{Z_{2}-\left(I^{21} / I^{11}\right) Z_{1}>0, Z_{1}<0\right\},\left\{Z_{1}-\right. \left.\left(I^{12} / I^{22}\right) Z_{2}>0, Z_{2}<0\right\}$, and $\left\{Z_{1}>0, Z_{2}>0\right\}$, respectively. Simple calculation of the distribution of $Z_{2}-\left(I^{21} / I^{11}\right) Z_{1}$, say, conditional on ( $Z_{1}, Z_{2}$ ) falling in the second region demonstrates the nonnormality of the components of the distribution of $\hat{\theta}$, although if $I^{21}=0$, the components are half-normal. A counterexample to Chant's theorem 2, in which he states that all components of the mixture are multivariate Gaussian, may be constructed by taking the original estimation problem to correspond to the asymptotic representation given previously. Then for every $N$, the maximum likelihood estimator has the representation given previously and, therefore, in the limit does not have a distribution corresponding to a mixture of multivariate Gaussians.

The error in Chant's proof appears in the specifications of the inequalities that characterize the configuration of $\hat{\theta}_{i}$ 's equal to zero. In the counterexample, for instance, Chant computed the second component of the mixture as the distribution of $Z_{2}-\left(I^{21} / I^{11}\right) Z_{1}$ conditional on $\left\{Z_{1}<0\right\}$ rather than conditional on $\left\{Z_{1}<0, Z_{2}\right.$ $\left.\left(I^{21} / I^{11}\right) Z_{1}>0\right\}$.

Case 3. Suppose that $\Omega$ is as in Case 2, $\theta_{01}, \ldots, \theta_{0 q}$ are left endpoints of $\Omega_{1}, \ldots, \Omega_{q}$, and $\theta_{0 i}$ are interior points of $\Omega_{i}(q+1<i<p)$. There are $2^{q}$ possible configurations of the first $q$ coordinates of $\hat{\theta}$, where the configuration is taken to mean which coordinates of $\hat{\theta}$ are zero. The $i$ th such configuration is characterized by a set of inequalities satisfied by $q$ linear combinations of $Z$, denoted by $\left\{L_{i} Z>0\right\}$. In addition, given the $i$ th configuration, $\hat{\theta}$ is simply the projection of $Z, P_{i} Z$, onto the appropriate edge of $C_{\Omega}-\theta_{0} . P_{i}=I- I^{-1}\left(\theta_{0}\right) B_{i}\left[B_{i}^{\prime} I^{-1}\left(\theta_{0}\right) B_{i}\right]^{+} B_{i}^{\prime}$, with $B_{i}$ a diagonal matrix with ones as diagonal elements corresponding to coordinates of $\hat{\theta}$ that are zero, and zeros otherwise. Thus $\hat{\theta}$ may be written as $\sum P_{i} Z I\left\{L_{i} Z>0\right\}$ and the distribution of $\hat{\theta}, F(\cdot)$ may be written as $\sum_{i} P\left[L_{i} Z_{i}>0\right] P\left[P_{i} Z \leq(\cdot) \mid L_{i} Z_{i}>0\right]$.

## 3. LARGE SAMPLE DISTRIBUTION OF LIKELIHOOD RATIO STATISTICS

In many problems, it is desired to test the hypothesis that $\theta_{0}$ lies in a subset of $\Omega$, denoted by $\Omega_{0}$, versus the alternative that $\theta_{0}$ lies in the complement of $\Omega_{0}$ in $\Omega$, denoted by $\Omega_{1}$. When $\Omega_{0}$ is an $r$-dimensional subset of $\Omega, \theta_{0}$ is a boundary point of both $\Omega_{0}$ and $\Omega_{1}$ but $\theta_{0}$ is an interior point of $\Omega$, and under suitable regularity conditions, the asymptotic distribution of the likelihood ratio test statistic, $-2 \ln \lambda_{N}$, is $\chi^{2}$ on $p-r$ df. Chernoff (1954) provided a representation of the asymptotic distribution of $-2 \ln \lambda_{N}$ when $\Omega_{0}$ and $\Omega_{1}$ both have the same dimension as $\Omega, \theta_{0}$ is a boundary point of both $\Omega_{0}$ and $\Omega_{1}$, and $\theta_{0}$ is also interior point of $\Omega$. The following theorem generalizes these results
to the case in which $\theta_{0}$ is a boundary point of $\Omega$. We will assume from now on that both $\Omega$ and $\Omega_{0}$ are regular enough to be approximated by cones with vertices at $\theta_{0}$.

Theorem 3. Let $Z$ be a random variable with a multivariate Gaussian distribution with mean $\theta$ and covariance matrix $I^{-1}\left(\theta_{0}\right)$, and let $C_{\Omega_{0}}$ and $C_{\Omega_{1}}$ be non-empty cones approximating $\Omega_{0}$ and $\Omega_{1}$ at $\theta_{0}$, respectively. Then under the regularity conditions given in Section 1, the asymptotic distribution of the likelihood ratio statistic, $-2 \ln \lambda_{N}$, is the same as the distribution of the likelihood ratio test of $\theta \in C_{\Omega_{0}}$ versus the alternative $\theta \in C_{\Omega_{1}}$ based on a single realization of $Z$ when $\theta=\theta_{0}$.

The proof follows immediately from the approximations described in Section 2 and Chernoff's (1954) theorem 1.

The asymptotic representation of the likelihood ratio statistic given by Theorem 3 may be written as

$$
\begin{aligned}
\sup _{\theta \in C_{\Omega}-\theta_{0}}\{-(Z & \left.-\theta)^{\prime} I\left(\theta_{0}\right)(Z-\theta)\right\} \\
& -\sup _{\theta \in C_{\Omega_{0}}-\theta_{0}}\left\{-(Z-\theta)^{\prime} I\left(\theta_{0}\right)(Z-\theta)\right\},
\end{aligned}
$$

where $Z$ has a multivariate Gaussian distribution with mean 0 and covariance matrix $I^{-1}\left(\theta_{0}\right)$. It is convenient to rewrite (3.1) as

$$
\inf _{\theta \in \tilde{C}_{0}}\|\tilde{Z}-\theta\|^{2}-\inf _{\theta \in \tilde{C}}\|\tilde{Z}-\theta\|^{2}
$$

with $\tilde{C}=\left\{\tilde{\theta}: \tilde{\theta}=\Lambda^{1 / 2} P^{T} \theta\right.$ for all $\left.\theta \in C_{\Omega}-\theta_{0}\right\}$ and $\tilde{C}_{0}=\left\{\tilde{\theta}: \tilde{\theta}=\Lambda^{1 / 2} P^{T} \theta\right.$ for all $\left.\theta \in C_{\Omega_{0}}-\theta_{0}\right\}$, where $\tilde{Z}$ has a multivariate Gaussian distribution with mean 0 and identity covariance matrix and $P \Lambda P^{T}$ represents the spectral decomposition of $I\left(\theta_{0}\right)$. Once the problem is changed to $\tilde{Z}$ and the new parameter sets, probabilities can be computed using the standard Gaussian distribution. Note that the probability structure is retained through orthogonal transformations of $\tilde{Z}$.

We now present some special cases in which the representation given by (3.2) is used to calculate the distribution of likelihood ratio statistics. We will assume from here on that $\Omega=\Omega_{1} \times \cdots \times \Omega_{p}$, where the $\Omega_{i}$ 's are either closed, half-open, or open intervals in $R^{1}$. In these examples we partition the parameter vector into four components: the first $q$ coordinates of $\theta$ will represent the parameters of interest, with true values on the boundary; the next $s$ coordinates of $\theta$ are parameters of interest that have true values not on the boundary; the next $t$ coordinates of $\theta$ will represent nuisance parameters with true values on the boundary; and finally the last $p-q- s-t$ coordinates of $\theta$ will represent nuisance parameters with true values not on the boundary. Thus $\theta$ may be written as $\left(\theta_{1}, \ldots, \theta_{q}, \theta_{q+1}, \ldots, \theta_{q+s}, \theta_{q+s+1}, \ldots\right.$, $\left.\theta_{q+s+t}, \theta_{q+s+t+1}, \ldots, \theta_{p}\right)$ and the parameter configuration for the special cases described subsequently can be characterized by the four-tuple ( $q, s, t, p-q-s-t$ ). We consider likelihood ratio tests of the hypothesis $\theta_{1}=\theta_{01}$, $\theta_{2}=\theta_{02}, \theta_{q+s}=\theta_{0 q+s}$ with $\theta_{q+s+1}, \ldots, \theta_{p}$ left unspecified.

Case 4. Suppose that the parameter configuration is
given by ( $0, s, 0, p-s$ ), so there are no parameters on the boundary. Then $\tilde{C}=R^{p}$ and $\tilde{C}_{0}$ is a $p-s$ dimensional subspace of $R^{p}$. By representing $\tilde{Z}$ in terms of a new orthonormal basis for $R^{p}$ in which the last $p-s$ basis vectors span $\tilde{C}_{0}$, we have Equation (3.2) reducing to

$$
\sum_{i=1}^{s} \tilde{Z}_{i}^{2},
$$

which has a chi-squared distribution on $s$ df.
Case 5. Consider the parameter configuration ( $1,0,0$, $p-1$ ). Then after an orthonormal transformation, we have $\tilde{C}=[0, \infty) \times R^{p-1}$ and $\tilde{C}_{0}=\{0\} \times R^{p-1}$. Thus Equation (3.2) can be reduced to

$$
\tilde{Z}_{1}^{2} I\left(\tilde{Z}_{1}>0\right) .
$$

Consequently, the asymptotic distribution of $-2 \ln \lambda_{N}$ can easily be seen to be a 50:50 mixture of $\chi_{0}^{2}$ and $\chi_{1}^{2}$. A typical example of this kind is the variance component problem (Miller 1977), in which we are interested in testing the existence of a single random effect.

Case 6. Consider the parameter configuration ( $1,1,0$, $p-2)$. Then, after an orthonormal transformation, we have $\tilde{C}=[0, \infty) \times R^{p-1}$ and $\tilde{C}_{0}=\{0\} \times\{0\} \times R^{p-2}$. Equation (3.2) can be expressed as

$$
\tilde{Z}_{1}^{2} I\left(\tilde{Z}_{1}>0\right)+\tilde{Z}_{2}^{2},
$$

which has a 50:50 mixture of $\chi_{1}^{2}$ and $\chi_{2}^{2}$ as its distribution. By using the variance component problem as an illustration, we are testing in this example that the random effect is null and the mean is equal to $\mu_{0}$, a constant, simultaneously while leaving the other parameters, such as the error variance, totally unspecified.

In Cases 5 and 6 we take advantage of the fact that there is only one boundary parameter and it occurs as a parameter of interest. Cases 7 and 8 show that the asymptotic distribution of the likelihood ratio statistic may become considerably more complicated once the aforementioned conditions do not hold. This distribution is most conveniently expressed as a mixture, with the components of the mixture identified with different regions of $R^{P}$ into which $\tilde{Z}$ may fall.

Case 7. Consider the parameter configuration (2, $p$, 0,0 ). The shaded region in Figure 1 represents $\tilde{C}$, and $\tilde{C}_{0}$ is the origin. In the shaded region, the likelihood ratio test reduces to $\tilde{Z}_{1}^{2}+\tilde{Z}_{2}^{2}$, which has a $\chi_{2}^{2}$ distribution. In regions 1 and 3, (3.2) yields squared Gaussian variables and, therefore, has a $\chi_{1}^{2}$ distribution. Finally, Equation (3.2) reduces to zero in region 2 . Note that the angle in $\tilde{C}$ is less than $180^{\circ}$. This is true because the convexity of $C_{\Omega}-\theta_{0}$ is preserved under the linear mapping into $\tilde{C}$. The mixing probability, $p$, for the shaded region can be calculated as

$$
\begin{aligned}
\cos ^{-1}\left\{\frac{(10) P^{T} \Lambda^{1 / 2} \Lambda^{1 / 2} P\binom{0}{1}}{\left\|\Lambda^{1 / 2} P\binom{0}{1}\right\|\left\|\Lambda^{1 / 2} P\binom{1}{0}\right\|}\right\} / 2 & \\
& =\cos ^{-1}\left\{I_{12} /\left(\sqrt{ } I_{11} I_{22}\right)\right\} / 2 \pi
\end{aligned}
$$

where the $I_{i j}$ 's are the $(i, j)$ entries of the information matrix $I\left(\theta_{0}\right)$. Thus the asymptotic distribution of $-2 \ln \lambda_{N}$ is a mixture of $\chi_{0}^{2}, \chi_{1}^{2}$, and $\chi_{2}^{2}$ with mixing probabilities $\frac{1}{2} -p, \frac{1}{2}$, and $p$, respectively, where $p \leq \frac{1}{2}$ from the previous angle result.

Case 8. Consider the parameter configuration ( $1,0,1$, 0 ). There are six different regions that must be considered.

![](https://cdn.mathpix.com/cropped/9b877226-8129-4eaf-ae58-e17a7d4af15d-5.jpg?height=884&width=1196&top_left_y=1677&top_left_x=432)
Figure 1. Diagram of the Parameter Space for Case 7. The shaded region, $\tilde{C}$, represents admissible parameter values under the alternative hypothesis. Under the null hypothesis, the parameter is located at the origin. The asymptotic distribution of the likelihood ratio test is a mixture of $\chi_{0}^{2}, \chi_{1}^{2}$, and $\chi_{2}^{2}$ distributions with mixing probabilities depending on the angle in $\tilde{C}$.

The shaded region in Figure 2 represents $\tilde{C}$, and $\tilde{C_{0}}$ is the half-line in the same direction as the vector $\Lambda^{1 / 2} P\binom{0}{1}$ with endpoint at the origin. In regions 1, 2, and 6, Equation (3.2) can be expressed as $\tilde{Z}_{1}^{2}+\tilde{Z}_{2}^{2}$, a single squared normal random variable, and $\tilde{Z}_{2}^{2}$, respectively. In regions 3, 4, and 5, (3.2) may be written as $\left\|Y^{2}\right\|,\left\|Y^{2}\right\|-\tilde{Z}_{1}^{2}$, respectively, where $Y$ is the projection of $\tilde{Z}$ onto $\Lambda_{\tilde{1} / 2} P\binom{1}{0}$. The distribution of these quantities conditional on $\tilde{Z}$ being in the associated regions is not chi-squared. If $\alpha$ represents the angle in region 3, then by straightforward calculation the probability of (3.2) exceeding the value $y^{2}$ conditional on $\tilde{Z}$ being in region 3 is seen to be

$$
\frac{\left\{\int_{y / \tan \alpha}^{\infty} \Phi(x \tan \alpha) d \Phi(x)-\Phi(y)[1-\Phi(y \cot \alpha)]\right\}}{\left\{\int_{0}^{\infty} \Phi(x \tan \alpha) d \Phi(\alpha)-\frac{1}{4}\right\}},
$$

where $\Phi(\cdot)$ is the standard Gaussian cumulative distribution function. The conditional distribution of (3.2) for region 5 has the same form. In a similar but more tedious calculation, the probability of (3.2) exceeding the value $y^{2}$ conditional on $\tilde{Z}$ falling in region 4 is given by

$$
\frac{\left\{\frac{1}{2}-\int_{0}^{u \tan \alpha} \Phi(f(x, u, \alpha)) d \Phi(x)-\int_{u \tan \alpha}^{\infty} \Phi(x \cot \alpha) d \Phi(x)\right\}}{\left\{\frac{1}{2}-\int_{0}^{\infty} \Phi(x \cot \alpha) d \Phi(x)\right\}},
$$

where $f(x, u, \alpha)=\left[\left(x^{2}+y^{2}\right)^{1 / 2}-x \sin \alpha\right] / \cos \alpha$ with $\alpha$ representing the angle in region 4 . In principle, tests could be constructed from these distributions together with mix-
ing probabilities calculated from the information matrix, as in Case 8.

When the information matrix is diagonal, the orthogonal structure of $C_{\Omega}-\theta_{0}$ and $C_{\Omega_{0}}-\theta_{0}$ is retained upon transformation to $\tilde{C}$ and $\tilde{C}_{0}$, respectively. This makes explicit evaluation of Equation (3.2) much easier.

Case 9. Suppose that $I\left(\theta_{0}\right)$ is diagonal. Then $\tilde{C}= \tilde{\Omega}_{1} \times \tilde{\Omega}_{2} \times \cdots \times \tilde{\Omega}_{p}$, where $\tilde{\Omega}_{i}$ is either $[0, \infty)$ or $(-\infty$, $\infty$ ) depending on whether the true value for the $i$ th coordinate of the parameter vector is on the boundary or not. Similarly, $\tilde{C}_{0}=\tilde{\Omega}_{01} \times \cdots \times \tilde{\Omega}_{0 p}$, where $\Omega_{0 i}=\{0\}$ for $i \leq i \leq q+s$ and $\tilde{\Omega}_{0 i}=\tilde{\Omega}_{i}$ for $q+s+1 \leq i \leq p$. Because of the orthogonal structure of these sets, the projection of $\tilde{Z}$ onto these sets may be performed coordinatewise. Equation (3.2) may then be reduced to

$$
\sum_{i=1}^{q} \tilde{Z}_{i}^{2} I\left\{\tilde{Z}_{i}>0\right\}+\sum_{i=q+1}^{q+s} \tilde{Z}_{i}^{2} .
$$

Thus the asymptotic distribution of the likelihood ratio statistic is a mixture of $\chi^{2}$ distributions on $s, \ldots, q+s$ df , where the mixing probability for the $\chi_{k}^{2}$ component is $\binom{q}{k-s} 2^{-q}$ 。

## 4. DISCUSSION

Recently, Shapiro (1985) investigated the asymptotic distribution of a class of test statistics (which includes likelihood ratio statistics) for the special case in which $\theta_{0}$ is on the boundary of $\Omega_{0}$ but is an interior point of $\Omega$. By using virtually the same approach as in this work, Shapiro characterized this asymptotic distribution as a mixture of chi-squared distributions. When $\theta_{0}$ is an interior point of

![](https://cdn.mathpix.com/cropped/9b877226-8129-4eaf-ae58-e17a7d4af15d-6.jpg?height=922&width=1253&top_left_y=1605&top_left_x=400)
Figure 2. Diagram of the Parameter Space for Case 8. The shaded region, $\tilde{C}$, represents admissible parameter values under the alternative hypothesis. The half-line in the same direction as the vector $\Lambda^{1 / 2} P(1)$ with endpoint at the origin represents admissible parameter values under the null hypothesis. The asymptotic distribution of the likelihood ratio test may be represented as a mixture of distributions. Some of the mixed distributions are $\chi^{2}$ and others are not.

$\Omega$, the second term in expression (3.2) is identically zero. This representation then corresponds to Shapiro's Lemma 2.2. It is interesting to note that our Cases $5-7$ and Case 9 do not satisfy Shapiro's assumptions yet still yield a mixture of chi-squared distributions. Case 8, in which a nuisance parameter is on the boundary, demonstrates that the asymptotic distribution is not always a mixture of chisquared distributions.

It has been suggested that it is possible to derive the previous results by a slightly different approach. If the family of probability distributions given in Section 1 can be embedded in a larger class of distributions such that $\theta_{0}$ is an interior point of the parameter space within this larger class, then asymptotic properties of the maximum likelihood estimator within this larger class of models may be derived by standard methods. In fact, a referee has suggested that one can always "reflect" the parametric distributions across the boundary to create this larger problem. Projection of an asymptotic representation of this estimator onto the original parameter space may then be used to represent the maximum likelihood estimator in the original problem. This is fundamentally the same approach as the one used here in that the variable being projected onto $C_{\Omega}-\theta_{0}$ in Theorem 2, $N^{1 / 2} Z_{N}$, is asymptotically equivalent to the "unrestricted maximum likelihood estimator." The feature that characterizes the solution to the problem is the process of projection itself rather than the exact source of the Gaussian random variable that is being projected.

Although the distribution of a likelihood ratio statistic may be derived for any fixed $\theta_{0}$ in $\Omega_{0}$, this distribution is generally different for different $\theta_{0}$ in $\Omega_{0}$. These distributions typically vary over $\Omega_{0}$ in a discontinuous way when some of the nuisance parameters may be on a boundary. For example, consider Case 5 with $p=2$ and Case 8. The asymptotic distributions for these two cases are quite different, yet the only difference between the two cases is whether the true value of the nuisance parameter is on the boundary or not. This discontinuity can also affect the quality of the asymptotic approximation, since this de-
pends on the proximity of the nuisance parameter to the boundary relative to the precision with which the parameter can be estimated. One can imagine a situation in which the nuisance parameter is not on the boundary but is close enough so that the distribution for a given finite sample corresponds more closely to Case 8 than to Case 5.

Because the distribution may vary over $\Omega_{0}$, there may be some difficulty in determining a critical value that will give correct asymptotic size. One possibility is to compute critical values corresponding to every $\theta_{0}$ in $\Omega_{0}$ and then use the largest of these values. Another approach would be to use estimates of the nuisance parameters to identify the possible location of $\theta_{0}$ within $\Omega_{0}$ and use critical values associated with this location. One possibility for doing this is to use critical values corresponding to the analogous multivariate normal testing problem, where the true values of the nuisance parameters and covariance matrix are taken to be equal to the maximum likelihood estimates and observed information matrix, respectively. This approach might also enhance the asymptotic approximation to the finite sample problem.
[Received October 1984. Revised August 1986.]

## REFERENCES

Chant, D. (1974), "On Asymptotic Tests of Composite Hypotheses in Nonstandard Conditions," Biometrika, 61, 291-298.
Chernoff, H. (1954), "On the Distribution of the Likelihood Ratio," Annals of Mathematical Statistics, 25, 573-578.
Cramér, H. (1946), Mathematical Methods of Statistics, Princeton, NJ: Princeton University Press.
Kulldorf, G. (1957), "On the Conditions for Consistency and Asymptotic Efficiency of Maximum Likelihood Estimates," Skandinavisk Aktuarietidshrift, 40, 129-144.
Lehmann, E. L. (1983), Theory of Point Estimation, New York: John Wiley.
Miller, J. J. (1977), "Asymptotic Properties of Maximum Likelihood Estimates in the Mixed Model of the Analysis of Variance," The Annals of Statistics, 5, 746-762.
Moran, P. A. P. (1971), "Maximum Likelihood Estimators in Non-Standard Conditions," Proceedings of the Cambridge Philosophical Society, 70, 441-450.
Shapiro, A. (1985), "Asymptotic Distribution of Test Statistics in the Analysis of Moment Structures Under Inequality Constraints," Biometrika, 72, 133-144.


[^0]:    * Steven G. Self is Associate Member, Fred Hutchinson Cancer Research Center, Seattle, WA 98104. Kung-Yee Liang is Associate Professor, Department of Biostatistics, Johns Hopkins University, Baltimore, MD 21205. This work was supported in part by National Institutes of Health Grant GM-32502.

