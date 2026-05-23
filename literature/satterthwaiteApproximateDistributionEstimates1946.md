---
citekey: satterthwaiteApproximateDistributionEstimates1946
item_type: article
authors: 'Satterthwaite, F. E.'
year: 1946
title: 'An {Approximate Distribution} of {Estimates} of {Variance Components}'
venue: Biometrics Bulletin
volume: 2
issue: 6
pages: 110
doi: 10.2307/3002019
eprint: 10.2307/3002019
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\satterthwaite_approximate_distribution_estimates_1946.pdf'
pdf_sha256: a662def141e838b4bb395930681ad6d99617ee2daeffc896d99802e69d9e3089
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-23T01:22:37Z
---
An Approximate Distribution of Estimates of Variance Components
Author(s): F. E. Satterthwaite
Source: Biometrics Bulletin, Vol. 2, No. 6 (Dec., 1946), pp. 110-114
Published by: The International Biometric Society
Stable URL: https://www.jstor.org/stable/3002019
Accessed: 23-05-2026 00:56 UTC

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms \& Conditions of Use, available at https://about.jstor.org/terms

# AN APPROXIMATE DISTRIBUTION OF ESTIMATES OF VARIANCE COMPONENTS 

F. E. Satterthwaite<br>General Electric Company, Ft. Wayne, Indiana

## 1. Introduction

In many problems, only simple mean square statistics are required to estimate whatever variances are involved. If the underlying populations are normal, these mean squares are distributed as is chi-square and may therefore be used in the standard chi-square, Student's $t$ and Fisher's $z$ tests. Frequently, however, the variances must be estimated by linear combinations of mean squares. Crump (1) has recently discussed a problem of this type, based on the following data:

Analysis of Variance of Total Egg Production of 12 Females
(D. melanogaster) from 25 Races in 4 Experiments
| Source of Variation | Degrees of Freedom | Mean Square | Average...Value of the Mean Square |
| :--- | :--- | :--- | :--- |
| Experiments | 3 | $M S_{e}=46,659$ | $\sigma_{z}{ }^{2}+12 \sigma_{e r}{ }^{2}+300 \sigma_{e^{2}}$ |
| Races | 24 | $M S_{r}=3,243$ | $\sigma_{z}{ }^{2}+12 \sigma \sigma_{e r}{ }^{2}+4 \sigma_{r^{2}}{ }^{2}$ |
| $\mathbf{E} \times \mathbf{R}$ | 72 | $M S_{\text {er }}=459$ | $\sigma_{z}{ }^{2}+12 \sigma_{e r}{ }^{2}$ |
| Within Subclasses | 1,100 | $M S_{z}=231$ | $\sigma_{z}{ }^{2}$ |


The variance of the mean of the $i$ th race is shown in his paper to be estimated by

$$
\begin{aligned}
V_{. i \cdot} & =\frac{1}{e}\left(\hat{\sigma}_{e}^{2}+\hat{\sigma}_{e r}^{2}\right)+\frac{1}{e n}\left(\sigma_{z}^{2}\right) \\
& =\frac{1}{e}\left\{\frac{M S_{e}-M S_{e r}}{300}+\frac{M S_{e r}-M S_{z}}{12}\right\}+\frac{1}{e n}\left(M S_{z}\right) \\
& \left.=\frac{1}{e}\left\{\frac{M S_{e}}{300}+\frac{24 M S_{e r}}{300}\right\}+\left(\frac{1}{n}-\frac{1}{12}\right) M S_{z}\right\}
\end{aligned}
$$

where $e$ is the number of experiments and $n$ is the number of females in each experiment. Variance estimates such as (2) have been called complex estimates (2). Thus a complex estimate of variance is a linear function of independent mean squares.

It is stated in (1) that "increasing the number of females indefinitely still leaves us with

$$
V\left(\bar{x}_{. i \cdot}\right)=\frac{M S_{e}+24 M S_{e r}-25 M S_{z}}{300 e}=\frac{173}{e} \cdot "
$$

Conclusions are then reached without analysis of the sampling errors involved. Now the standard deviation of $V\left(\bar{x}_{. i}.\right)$ is very large

$$
\begin{aligned}
\left\{\hat{V}\left[\hat{V}\left(\bar{x}_{. i \cdot}\right)\right]\right\}^{\frac{1}{2}} & =\frac{\sqrt{2}}{300 e}\left[\frac{\left(M S_{e}\right)^{2}}{5}+\frac{\left(24 M S_{e r}\right)^{2}}{74}+\frac{\left(25 M S_{z}\right)^{2}}{1102}\right]^{\frac{1}{2}} \\
& =0.57 \hat{V}\left(\bar{x}_{. i \cdot}\right)
\end{aligned}
$$

and further analysis leading to confidence limits for $V\left(\bar{x}_{. i}.\right)$ should be helpful in choosing a course of action.

The writer has studied the distribution of complex estimates of variance in a paper (2) in Psychometrika. Since this paper may not be readily available to biometricians, the principal results are outlined below and a few applications are given.

## 2. The Distribution of Complex Estimates of Variance

The exact distribution of a complex estimate of variance is too involved for everyday use. It is therefore proposed to use, as an approximation to the exact distribution, a chi-square distribution in which the number of degrees of freedom is chosen so as to provide good agreement between the two. This is accomplished by arranging that the approximating chi-square have a variance equal to that of the exact distribution. If $M S_{1}, M S_{2}, \ldots$ are independent mean squares with $r_{1}, r_{2}, \ldots$ degrees of freedom and

$$
\hat{V}_{s}=a_{1}\left(M S_{1}\right)+a_{2}\left(M S_{2}\right)+\ldots
$$

is a complex estimate of variance based on them, the number of degrees of freedom of the approximating chi-square is found to be given by

$$
r_{s}=\frac{\left[a_{1} E\left(M S_{1}\right)+a_{2} E\left(M S_{2}\right)+\ldots\right]^{2}}{\frac{\left[a_{1} E\left(M S_{1}\right)\right]^{2}}{r_{1}}+\frac{\left[a_{2} E\left(M S_{2}\right)\right]^{2}}{r_{2}}+\ldots}
$$

where $E()$ denotes mean or expected values.
In practice, the expected values of the independent mean squares will not be known. The observed values will usually be substituted in (6), giving, as an estimate of $r_{s}$,

$$
\hat{r}_{s}=\frac{\left[a_{1}\left(M S_{1}\right)+a_{2}\left(M S_{2}\right)+\ldots\right]^{2}}{\frac{\left[a_{1}\left(M S_{1}\right)\right]^{2}}{r_{1}}+\frac{\left[a_{2}\left(M S_{2}\right)\right]^{2}}{r_{2}}+\ldots}
$$

An approximation of this type for a slightly simpler problem was first suggested by H. Fairfield Smith (3). In his problem, there were only two mean squares and $a_{1}=a_{2}=1$. This approximation does not support the use of $r+2$ in place of $r$ as a correction for bias [(1) formula 3].

The writer has checked the accuracy of the suggested approximations by calculating the exact distribution for a number of special cases. Typical results are as follows:

| $r_{1}$ | $r_{2}$ | $\frac{E\left(M S_{1}\right)}{E\left(M S_{2}\right)}$ | $r_{s}$ | $\chi^{2}(95 \%)$ |  | $\chi^{2}(99.9 \%)$ |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  | exact | approx. | exact | approx. |
| 4 | 2 | 4 | 100/33 | 7.9 | 8.0 | 16.2 | 17.3 |
| 8 | 4 | 1 | 32/ 3 | 19.4 | 19.5 | 30.5 | 31.0 |
| 6 | 4 | 2 | 54/ 7 | 15.1 | 15.3 | 26.0 | 27.2 |
| 20 | 4 | 2 | 180/21 | 16.2 | 17.0 | 27.7 | 29.0 |
| 4 | 2 | 1 | 16/ 3 | 11.5 | 11.7 | 21.3 | 22.3 |

The above discrepancies between the exact and the approximate chi-squares, even for the extreme 99.9 percent case, are very small compared with their sampling errors. Thus it appears that the approximation may be used with confidence. Furthermore, we know from general reasoning that if $r_{s}$ is large, both the approximate and the exact distributions approach the same normal distribution ; if $r_{s}$ is small, the sampling errors in the chi-squares are large and refinement is superfluous.

Some care must be taken in the cases where one or more of the $a$ 's in (5) are negative. If it is possible for $\hat{V}_{s}$ to be negative with a fairly large probability, the approximate distribution will become rather poor since it can not allow negative estimates. However, here again the sampling errors in $\hat{V}_{s}$ will be quite large compared with its expected value so that only the sketchiest of conclusions can be drawn in any case.

## 3. Further Analysis of Crump's Example

The distribution of Crump's estimate of the residual variance of the race means,

$$
\hat{V}\left(\bar{x}_{. i .}\right)=\frac{\left(M S_{e}\right)+24\left(M S_{e r}\right)-25\left(M S_{z}\right)}{300 e}
$$

can now be approximated. Thus

$$
\begin{aligned}
\hat{V}\left(x_{. i .}\right) & =\frac{1}{e}\left[\frac{46,659}{300}+\frac{(24)(459)}{300}-\frac{(25)(231)}{300}\right] \\
& =\frac{1}{e}[155+37-19]=\frac{173}{e}
\end{aligned}
$$

From (7) we have

$$
\begin{aligned}
\hat{r}_{s} & =\frac{[155+37-19]^{2}}{\frac{(155)^{2}}{3}+\frac{(37)^{2}}{72}+\frac{(19)^{2}}{1,100}} \\
& =\frac{29,929}{8,008+19+1}=3.7
\end{aligned}
$$

From chi-square tables interpolated for 3.7 d.f. at the 5 percent and 95 percent points we find that, with a high degree of probability,

$$
0.60<\frac{3.7 \hat{V}}{V}<9.0
$$

or

$$
\begin{aligned}
\frac{(3.7)(173)}{(9.0) e} & <V \\
\frac{71}{e}<V & <\frac{(3.7)(173)}{(0.60) e} \\
e & <\frac{1,067}{e}
\end{aligned}
$$

Thus if it were necessary to reduce $V$ to 9 and if time were important so that a second series of experiments could not be made, we should run

$$
e=\frac{1,067}{9}=119
$$

experiments in the first series for confidence that $V$ would be properly reduced. On the other hand, if the experiments were expensive and time not important, we might run

$$
e=\frac{(3.7)(173)}{(5.6)(9)}=13
$$

experiments and then get a more accurate estimate of $V$ to determine how many additional experiments should be run ( 5.6 obtained from the 20 percent point for chi-square, 3.7 d.f.).

## 4. Difference of Means

The usual estimate of variance used in Student $t$ tests for the difference of two means is

$$
V_{t}=\left[\frac{r_{1}\left(M S_{1}\right)+r_{2}\left(M S_{2}\right)}{r_{1}+r_{2}}\right]\left[\frac{1}{r_{1}+1}+\frac{1}{r_{2}+1}\right]
$$

with

$$
r_{t}=r_{1}+r_{2}
$$

degrees of freedom. This assumes that both populations have the same variance. Seldom do we have positive evidence that this is so and often we have evidence that the variances are different. For example, $F=\left(M S_{1}\right) /\left(M S_{2}\right)$ may be significant. Note that a non-significant $F$ is not evidence that the variances are equal, especially if one of the $M S$ 's has a small number of degrees of freedom.

The assumption of equal variances can be avoided by use of a complex estimate of variance,

$$
\hat{V}_{s}=\frac{M S_{1}}{r_{1}+1}+\frac{M S_{2}}{r_{2}+1}
$$

with

$$
\hat{r}_{s}=\frac{\left.\left\{\left[M S_{1} / r_{1}+1\right)\right]+\left[M S_{2} /\left(r_{2}+1\right)\right]\right\}^{2}}{\frac{\left[M S_{1} /\left(r_{1}+1\right)\right]^{2}}{r_{1}}+\frac{\left[M S_{2} /\left(r_{2}+1\right)\right]^{2}}{r_{2}}}
$$

degrees of freedom.
For example, consider the numerical case:

$$
\begin{aligned}
& M S_{1}=100, r_{1}=99, \\
& M S_{2}=90, r_{2}=9 .
\end{aligned}
$$

By the standard analysis one would obtain

$$
\begin{aligned}
\hat{V}_{t} & =\left[\frac{(99)(100)+(9)(90)}{108}\right]\left[\frac{1}{100}+\frac{1}{10}\right]=10.9 \\
r_{t} & =99+9=108
\end{aligned}
$$

The complex estimate gives

$$
\begin{aligned}
& \hat{r}_{s}=\frac{100}{100}+\frac{90}{10}=10.0 \\
& \hat{r}_{s}=\frac{(1+9)^{2}}{\frac{1^{2}}{99}+\frac{9^{2}}{9}}=11.1
\end{aligned}
$$

One will sometimes reach different conclusions with 108 degrees of freedom from those he will reach with 11 degrees of freedom.

If from general reasoning or other a priori considerations it is believed that both $M S_{1}$ and $M S_{2}$ are independent estimates of the same variance, then the use of 108 degrees of freedom is justified. On the other hand, if the given data are the entire admissible knowledge, then the use of more than 11 degrees of freedom is not valid.

## 5. Conclusion

In many practical problems the most efficient estimate of variance available is a linear function of two or more independent mean-squares. Usually the exact distribution of such estimates is too complicated for practical use. A satisfactory approximation can be based on the chisquare distribution with the number of degrees of freedom determined by (7).

Many problems, such as the difference of means, can be more conservatively analyzed by use of complex estimates of variance. Assumptions regarding homogeneity of variance can then be avoided.

## REFERENCES

(1) Crump, S. Lee. The estimation of variance components in the analysis of variance. Biometrics Bulletin 2:1:7-11. February 1946.
(2) Satterthwaite, Franklin E. Synthesis of variance. Psychometrika 6:309-316. October 1941.
(3) Smith, H. Fairfield. The problem of comparing the results of two experiments with unequal errors. Journal of the Council of Scientific and Industrial Research 9:211-212. August 1936.

