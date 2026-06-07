---
citekey: vanbuurenFlexibleImputationMissing2018a
item_type: book
authors: 'Van Buuren, Stef'
year: 2018
title: 'Flexible Imputation of Missing Data, Second Edition'
venue: Chapman and Hall/CRC
doi: 10.1201/9780429492259
isbn: 978-0-429-49225-9
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\vanbuurenFlexibleImputationMissing2018a.pdf (generated FROM this markdown via pandoc+typst, not the other way around)'
pdf_sha256: d3979bd7fde4ae48d6d77bcf22473f6dd67901f2f101db77e3ba01381fe28aa8
source_repo: https://github.com/stefvanbuuren/fimdbook
source_commit: 6627496a411d27478125836b88cf0f96eb1b51ff
chapters_included: '1 (Introduction), 5 (Analysis of imputed data)'
conversion_note: 'R code chunks replaced by [R code chunk omitted]; HTML comments stripped; prose verbatim from the .Rmd sources. Remaining chapters available at the source repo. Citekey confirmed against the BBT export 2026-06-06 (entry vanbuurenFlexibleImputationMissing2018a).'
converted_via: 'direct extraction from bookdown .Rmd source, 2026-06-06'
last_synced: 2026-06-06T23:11:53Z
---

# (PART) Part I: Basics {-}

# Introduction {#ch:introduction}

> We should be suspicious of any dataset (large or small) which appears perfect.
>
> --- David J. Hand

[R code chunk omitted]

## The problem of missing data {#sec:problem}

### Current practice {#sec:current}

The mean of the numbers 1, 2 and 4 can be calculated in `R` as

[R code chunk omitted]

where `y` is a vector containing three numbers, and where `mean(y)` is the
`R` expression that returns their mean. Now suppose that the last
number is missing. `R` indicates this by the symbol `NA`, which stands
for “not available”:

[R code chunk omitted]

The mean is now undefined, and
`R` informs us about this outcome
by setting the mean to `NA`. It is possible to
add an extra argument `na.rm = TRUE` to the
function call. This removes any missing data before calculating the
mean:

[R code chunk omitted]

This makes it possible to calculate a result, but of course the set of
observations on which the calculations are based has changed. This may
cause problems in statistical inference and interpretation.

It gets worse with multivariate analysis. For example, let us try to
predict daily ozone concentration (ppb) from wind speed (mph) using the
built-in `airquality` dataset. We fit a linear
regression model by calling the `lm()`
function to predict daily ozone levels, as follows:

[R code chunk omitted]

Many `R` users have seen this
message. The code cannot continue because there are missing values. One
way to circumvent the problem is to omit any incomplete records by
specifying the `na.action = na.omit` argument
to `lm()`. The regression weights can now be
obtained as

[R code chunk omitted]

This works. For example, we may produce diagnostic plots by
`plot(fit)` to study the quality of the model. In practice, 
it is cumbersome to supply the `na.action()` function each 
time. We can change the setting in `options` as

[R code chunk omitted]

which eliminates the error message once and for all. Users of other
software packages like `SPSS`, `SAS` and `Stata` enjoy the “luxury” that
this deletion option has already been set for them, so the calculations
can progress silently. Next, we wish to plot the predicted ozone levels
against the observed data, so we use `predict()` to calculate the 
predicted values, and add these to the data to prepare for plotting.

[R code chunk omitted]

Argg... that doesn’t work either. The error message tells us that the
two datasets have a different number of rows. The `airquality` data has 
153 rows, whereas there are only 116 predicted values. The problem, 
of course, is that there are missing data. The `lm()` function dropped any
incomplete rows in the data. We find the indices of the first six cases by

[R code chunk omitted]

The total number of deleted cases is found as

[R code chunk omitted]

The number of missing values per variable in the data is

[R code chunk omitted]

so in our regression model, all 37 deleted cases have missing ozone
scores.

Removing the incomplete cases prior to analysis is known as 
*listwise deletion* or *complete-case analysis*. In `R`, there are 
two related functions for the subset of complete cases, `na.omit()` 
and `complete.cases()`.

Figure \@ref(fig:plotair9) plots the predicted against the observed values.
Here we adopt the Abayomi convention for the colors [@ABAYOMI2008]:
Blue refers to the observed part of the data, red to the
synthetic part of the data (also called the *imputed values* or
*imputations*), and black to the combined data (also called the *imputed data* 
or *completed data*). The printed version of the first edition of
this book used gray instead of blue. The blue points on the left are all
from the complete cases, whereas the figure on the right plots the
points for the incomplete cases (in red). Since there are no measured
ozone levels in that part of the data, the possible values are indicated
by 37 horizontal lines.

[R code chunk omitted]

[R code chunk omitted]
(ref:plotair9) Predicted versus measured ozone levels for the observed (left, blue) and missing values (right, red).

Listwise deletion allows the calculations to proceed, but it may
introduce additional complexities in interpretation. Let’s try to find a
better predictive model by including solar radiation
(`Solar.R`) into the model as

[R code chunk omitted]

Observe that the number of deleted days increased is now 42 since some
rows had no value for `Solar.R`. Thus,
changing the model altered the sample.

There are methodological and statistical issues associated with this
procedure. Some questions that come to mind are:

-   Can we compare the regression coefficients from both
    models?

-   Should we attribute differences in the coefficients to changes
    in the model or to changes in the subsample?

-   Do the estimated coefficients generalize to the study
    population?

-   Do we have enough cases to detect the effect of
    interest?

-   Are we making the best use of the costly collected
    data?

Getting the software to run is one thing, but this alone does not
address the challenges posed by the missing data. Unless the analyst, or
the software vendor, provides some way to work around the missing
values, the analysis cannot continue because calculations on missing
values are not possible. There are many approaches to circumvent this
problem. Each of these affects the end result in a different way. Some
solutions are clearly better than others, and there is no solution that
will always work. This chapter reviews the major approaches, and
discusses their advantages and limitations.

### Changing perspective on missing data {#sec:changingperspective}

The standard approach to missing data is to delete them. It is
illustrative to search for missing values in published data. @HAND1994
published a highly useful collection of small datasets across the
statistical literature. The collection covers an impressive variety of
topics. Only 13 out of the 510 datasets in the collection actually had a
code for the missing data. In many cases, the missing data problem has
probably been “solved” in some way, usually without telling us how many
missing values there were originally. It is impossible to track down the
original data for most datasets in Hand’s book. However, we can easily
do this for dataset number 357, a list of scores of 34 athletes in 10
sport events at the 1988 Olympic decathlon in Seoul. The table itself is
complete, but a quick search on the Internet revealed that initially 39
instead of 34 athletes participated. Five of them did not finish for
various reasons, including the dramatic disqualification of the German
favorite Jürgen Hingsen because of three false starts in the 100-meter
sprint. It is probably fair to assume that deletion occurred silently in
many of the other datasets.

The inclination to delete the missing data is understandable. Apart from
the technical difficulties imposed by the missing data, the occurrence
of missing data has long been considered a sign of sloppy research. It
is all too easy for a referee to write:

> This study is weak because of the large amount of missing data.

Publication chances are likely to improve if there is no hint of
missingness. @ORCHARD1972 [p. 697] remarked:

> Obviously the best way to treat missing data is not to have them.

Though there is a lot of truth in this statement, Orchard
and Woodbury realized the impossibility of attaining this ideal in
practice. The prevailing scientific practice is to downplay the missing
data. Reviews on reporting practices are available in various fields:
clinical trials [@WOOD2004; @POWNEY2014; @DIAZ2014; @AKL2015], cancer
research [@BURTON2004], educational research [@PEUGH2004], epidemiology
[@KLEBANOFF2008; @KARAHALIOS2012], developmental psychology
[@JELICIC2009], general medicine [@MACKINNON2010], developmental
pediatrics [@AYLWARD2010], and otorhinolaryngology, head and neck
surgery [@NETTEN2017]. The picture that emerges from these studies is
quite consistent:

-   The presence of missing data is often not explicitly stated in
    the text;

-   Default methods, such as listwise deletion are used without
    mentioning them;

-   Different tables are based on different sample sizes;

-   Model-based missing data methods, such as direct likelihood,
    full information maximum likelihood and multiple imputation, are
    notably underutilized.

Helpful resources include the STROBE [@VANDENBROUCKE2007] and CONSORT
checklists and flow charts [@SCHULZ2010]. @GOMES2016 showed cases where
the subset of full patient-reported outcomes is a selective, leading to
misleading results. @PALMER2017 suggested a classification scheme for
the reasons of nonresponse in patient-reported outcomes.

Missing data are there, whether we like it or not. In the social
sciences, it is nearly inevitable that some respondents will refuse to
participate or to answer certain questions. In medical studies,
attrition of patients is very common. The theory, methodology and
software for handling incomplete data problems have been vastly expanded
and refined over the last decades. The major statistical analysis
packages now have facilities for performing the appropriate analyses.
This book aims to contribute to a better understanding of the issues
involved, and provides a methodology for dealing with incomplete data
problems in practice.

## Concepts of MCAR, MAR and MNAR {#sec:MCAR}

Before we review a number of simple fixes for the missing data in
Section \@ref(sec:simplesolutions) let us take a short look at the terms
MCAR, MAR and MNAR. A more detailed definition of these concepts will be
given later in Section \@ref(sec:notation). @RUBIN1976 classified missing
data problems into three categories. In his theory every data point has
some likelihood of being missing. The process that governs these
probabilities is called the *missing data mechanism* or
*response mechanism*. The model for the process is called
the *missing data model* or *response model*.

If the probability of being missing is the same for all cases, then the
data are said to be missing completely at random (MCAR). This
effectively implies that causes of the missing data are unrelated to the
data. We may consequently ignore many of the complexities that arise
because data are missing, apart from the obvious loss of information. An
example of MCAR is a weighing scale that ran out of batteries. Some of
the data will be missing simply because of bad luck. Another example is
when we take a random sample of a population, where each member has the
same chance of being included in the sample. The (unobserved) data of
members in the population that were not included in the sample are MCAR.
While convenient, MCAR is often unrealistic for the data at hand.

If the probability of being missing is the same only within groups
defined by the *observed* data, then the data are missing at random
(MAR). MAR is a much broader class than MCAR. For example, when placed
on a soft surface, a weighing scale may produce more missing values than
when placed on a hard surface. Such data are thus not MCAR. If, however,
we know surface type and if we can assume MCAR *within* the type of
surface, then the data are MAR. Another example of MAR is when we take a
sample from a population, where the probability to be included depends
on some known property. MAR is more general and more realistic than
MCAR. Modern missing data methods generally start from the MAR
assumption.

If neither MCAR nor MAR holds, then we speak of missing not at random
(MNAR). In the literature one can also find the term NMAR (not missing
at random) for the same concept. MNAR means that the probability of
being missing varies for reasons that are unknown to us. For example,
the weighing scale mechanism may wear out over time, producing more
missing data as time progresses, but we may fail to note this. If the
heavier objects are measured later in time, then we obtain a
distribution of the measurements that will be distorted. MNAR includes
the possibility that the scale produces more missing values for the
heavier objects (as above), a situation that might be difficult to
recognize and handle. An example of MNAR in public opinion research
occurs if those with weaker opinions respond less often. MNAR is the
most complex case. Strategies to handle MNAR are to find more data about
the causes for the missingness, or to perform what-if analyses to see
how sensitive the results are under various scenarios.

Rubin’s distinction is important for understanding why some methods will
work, and others not. His theory lays down the conditions under which a
missing data method can provide valid statistical inferences. Most
simple fixes only work under the restrictive and often unrealistic MCAR
assumption. If MCAR is implausible, such methods can provide biased
estimates.

## Ad-hoc solutions {#sec:simplesolutions}

### Listwise deletion {#sec:listwise}

Complete-case analysis (listwise deletion) is the default way of
handling incomplete data in many statistical packages, including
`SPSS`, `SAS` and `Stata`. The function `na.omit()` does the same in
`S-PLUS` and `R`. The procedure eliminates all
cases with one or more missing values on the analysis variables. An
important advantage of complete-case analysis is convenience. If the
data are MCAR, listwise deletion produces unbiased estimates of means,
variances and regression weights. Under MCAR, listwise deletion produces
standard errors and significance levels that are correct for the reduced
subset of data, but that are often larger relative to all available
data.

A disadvantage of listwise deletion is that it is potentially wasteful.
It is not uncommon in real life applications that more than half of the
original sample is lost, especially if the number of variables is large.
@KING2001 estimated that the percentage of incomplete records in the
political sciences exceeded 50% on average, with some studies having
over 90% incomplete records. It will be clear that a smaller subsample
could seriously degrade the ability to detect the effects of interest.

If the data are not MCAR, listwise deletion can severely bias estimates
of means, regression coefficients and correlations. @LITTLE2002 [pp.
41–44] showed that the bias in the estimated mean increases with the
difference between means of the observed and missing cases, and with the
proportion of the missing data. @SCHAFER2002 reported an elegant
simulation study that demonstrates the bias of listwise deletion under
MAR and MNAR. However, complete-case analysis is not always bad. The
implications of the missing data are different depending on where they
occur (outcomes or predictors), and the parameter and model form of the
complete-data model. In the context of regression analysis, listwise
deletion possesses some unique properties that make it attractive in
particular settings. There are cases in which listwise deletion can
provide better estimates than even the most sophisticated procedures.
Since their discussion requires a bit more background than can be given
here, we defer the treatment to Section \@ref(sec:when).

Listwise deletion can introduce inconsistencies in reporting. Since
listwise deletion is automatically applied to the active set of
variables, different analyses on the same data are often based on
different subsamples. In principle, it is possible to produce one global
subsample using all active variables. In practice, this is unattractive
since the global subsample will always have fewer cases than each of the
local subsamples, so it is common to create different subsets for
different tables. It will be evident that this complicates their
comparison and generalization to the study population.

In some cases, listwise deletion can lead to nonsensical subsamples. For
example, the rows in the `airquality` dataset
used in Section \@ref(sec:current) correspond to 154 consecutive days
between May 1, 1973 and September 30, 1973. Deleting days affects the
time basis. It would be much harder, if not impossible, to perform
analyses that involve time, e.g., to identify weekly patterns or to fit
autoregressive models that predict from previous days.

The opinions on the merits of listwise deletion vary. @MIETTINEN1985 [p.
231] described listwise deletion as

> …the only approach that assures that no bias is introduced under any
> circumstances…

a bold statement, but incorrect. At the other end of the spectrum we
find @ENDERS2010 [p. 39]:

> In most situations, the disadvantages of listwise deletion far
> outweigh its advantages.

@SCHAFER2002 [p. 156] cover the middle ground:

> If a missing data problem can be resolved by discarding only a small
> part of the sample, then the method can be quite effective.

The leading authors in the field are, however, wary of providing advice
about the percentage of missing cases below which it is still acceptable
to do listwise deletion. @LITTLE2002 argue that it is difficult to
formulate rules of thumb since the consequences of using listwise
deletion depend on more than the missing data rate alone. @VACH1994 [p.
113] expressed his dislike for simplistic rules as follows:

> It is often supposed that there exists something like a critical
> missing rate up to which missing values are not too dangerous. The
> belief in such a global missing rate is rather stupid.

### Pairwise deletion {#sec:pairwise}

*Pairwise deletion*, also known as *available-case analysis*, attempts
to remedy the data loss problem of listwise deletion. The method
calculates the means and (co)variances on all observed data. Thus, the
mean of variable $X$ is based on all cases with observed data on $X$,
the mean of variable $Y$ uses all cases with observed $Y$-values, and so
on. For the correlation and covariance, all data are taken on which both
$X$ and $Y$ have non-missing scores. Subsequently, the matrix of summary
statistics are fed into a program for regression analysis, factor
analysis or other modeling procedures.

`SPSS`, `SAS` and `Stata` contain many procedures with an option for
pairwise deletion. In `R` we can calculate the means and correlations
of the `airquality` data under pairwise deletion in `R` as:

[R code chunk omitted]

The standard `lm()` function does not take means and covariances as
input, but the `lavaan` package [@ROSSEEL2012] provides this feature:

[R code chunk omitted]

The method is simple, and appears to use all available information.
Under MCAR, it produces consistent estimates of mean, correlations and
covariances [@LITTLE2002 p. 55]. The method has also some shortcomings.
First, the estimates can be biased if the data are not MCAR. Further,
the covariance and/or correlation matrix may not be positive definite,
which is requirement for most multivariate procedures. Problems are
generally more severe for highly correlated variables [@LITTLE1992]. It
is not clear what sample size should be used for calculating standard
errors. Taking the average sample size yields standard errors that are
too small[@LITTLE1992]. Also, pairwise deletion requires numerical data
that follow an approximate normal distribution, whereas in practice we
often have variables of mixed types.

The idea to use all available information is good, but the proper
analysis of the pairwise matrix requires sophisticated optimization
techniques and special formulas to calculate the standard errors
[@VANPRAAG1985; @MARSH1998], which somewhat defeats its utility.
Pairwise deletion works best used if the data approximate a multivariate
normal distribution, if the correlations between the variables are low,
and if the assumption of MCAR is plausible. It is not recommended for
other cases.

### Mean imputation {#sec:meanimp}

A quick fix for the missing data is to replace them by the mean. We may
use the mode for categorical data. Suppose we want to impute the mean in
`Ozone` and `Solar.R` of the `airquality` data. `SPSS`, `SAS` and `Stata`
have pre-built functions that substitute the mean. This book uses the
`R` package `mice` [@VANBUUREN2011B]. This software is a contributed
package that extends the functionality of `R`. Before `mice` can be
used, it must be installed. An easy way to do this is to type:

[R code chunk omitted]

which searches the Comprehensive R Archive Network (CRAN), and installs
the requested package on the local computer. After succesful
installation, the `mice` package can be loaded by

[R code chunk omitted]

Imputing the mean in each variable can now be done by

[R code chunk omitted]

The argument `method = mean` specifies mean imputation, the argument
`m = 1` requests a single imputed dataset, and `maxit = 1` sets
the number of iterations to 1 (no iteration). The latter two options can
be left to their defaults with essentially the same result.

[R code chunk omitted]
(ref:plotmeanimp) Mean imputation of `Ozone`. Blue indicates the observed data, red indicates the imputed values.

Mean imputation distorts the distribution in several ways. Figure
\@ref(fig:plotmeanimp) displays the distribution of
`Ozone` after imputation. In the figure on the
left, the red bar at the mean stands out. Imputing the mean here
actually creates a bimodal distribution. The standard deviation in the
imputed data is equal to 28.7, much smaller than from the observed data
alone, which is 33. The figure on the right-hand side shows that the
relation between `Ozone` and `Solar.R` is distorted because of the
imputations. The correlation drops from 0.35 in the blue points
to 0.3 in the combined data.

Mean imputation is a fast and simple fix for the missing data. However,
it will underestimate the variance, disturb the relations between
variables, bias almost any estimate other than the mean and bias the
estimate of the mean when data are not MCAR. Mean imputation should
perhaps only be used as a rapid fix when a handful of values are
missing, and it should be avoided in general.

### Regression imputation {#sec:regimp}

Regression imputation incorporates knowledge of other variables with the
idea of producing smarter imputations. The first step involves building
a model from the observed data. Predictions for the incomplete cases are
then calculated under the fitted model, and serve as replacements for
the missing data. Suppose that we predict `Ozone` by linear regression
from `Solar.R`.

[R code chunk omitted]

[R code chunk omitted]
(ref:plotregimp) Regression imputation: Imputing `Ozone` from the regression line.

Another possibility for regression imputation uses `mice`:

[R code chunk omitted]

Figure \@ref(fig:plotregimp) shows the result. The imputed values correspond to
the most likely values under the model. However, the ensemble of imputed
values vary less than the observed values. It may be that each of the
individual points is the best under the model, but it is very unlikely
that the real (but unobserved) values of `Ozone` would have had this distribution.
Imputing predicted values also has an effect on the correlation. The red
points have a correlation of 1 since they are located on a line. If the
red and blue dots are combined, then the correlation
increases from 0.35 to 0.39. Note that this upward bias grows with the
percent missing ozone levels (here 24%).

Regression imputation yields unbiased estimates of the means under MCAR,
just like mean imputation, and of the regression weights of the
imputation model if the explanatory variables are complete. Moreover,
the regression weights are unbiased under MAR if the factors that
influence the missingness are part of the regression model. In the
example this corresponds to the situation where `Solar.R` would explain
any differences in the probability that `Ozone` is missing. On the
other hand, correlations are biased upwards, and the variability of the
imputed data is systematically underestimated. The degree of
underestimation depends on the explained variance and on the proportion
of missing cases [@LITTLE2002 p. 64].

Imputing predicted values can yield realistic imputations if the
prediction is close to perfection. If so, the method reconstructs the
missing parts from the available data. In essence, there was not really
any information missing in the first place, it was only coded in a
different form.

Regression imputation, as well as its modern incarnations in machine
learning is probably the most dangerous of all methods described here.
We may be led to believe that we’re to do a good job by preserving the
relations between the variables. In reality however, regression
imputation artificially strengthens the relations in the data.
Correlations are biased upwards. Variability is underestimated.
Imputations are too good to be true. Regression imputation is a recipe
for false positive and spurious relations.

### Stochastic regression imputation {#sec:sri}

Stochastic regression imputation is a refinement of regression
imputation attempts to address correlation bias by adding noise to the
predictions. The following code imputes `Ozone` from `Solar.R` by
stochastic regression imputation.

[R code chunk omitted]
[R code chunk omitted]
(ref:plotsri) Stochastic regression imputation of `Ozone`.

The `method = norm.nob` argument requests a plain, non-Bayesian,
stochastic regression method. This method first
estimates the intercept, slope and residual variance under the linear
model, then calculates the predicted value for each missing value, and
adds a random draw from the residual to the prediction. We will come
back to the details in Section \@ref(sec:linearnormal). The
`seed` argument makes the solution reproducible. Figure \@ref(fig:plotsri)
shows that the addition of noise to the predictions opens up the
distribution of the imputed values, as intended.

Note that some new complexities arise. There is one imputation with a
negative value. Such values need not be due to the draws from the
residual distribution, but can also be a consequence of the use of a
linear model for non-negative data. In fact, Figure \@ref(fig:plotair9) shows
several negative predicted values in the observed data. Since negative
`Ozone` concentrations do not exist in the real world, we cannot
consider negative values as plausible imputations.
Note also that the high end of the distribution is not well covered. The
observed data form a cone, i.e., the data are heteroscedastic, but the
imputation model assumes equal dispersion around the regression line.
The variability of `Ozone` increases up to the
solar radiation level of 250 langleys, and decreases after that. Though
it is unclear whether this is a genuine meteorological phenomenon, the
imputation model does not account for this feature.

Nevertheless, stochastic regression imputation represents a major
conceptual advance. Some analysts may find it counterintuitive to
“spoil” the best prediction by adding random noise, yet this is
precisely what makes it suitable for imputation. A well-executed
stochastic regression imputation preserves not only the regression
weights, but also the correlation between variables (cf. Exercise
\@ref(exr:sriexr)). The main idea to draw from the residuals is very 
powerful, and forms the basis of more advanced imputation techniques.

### LOCF and BOCF {#sec:locf}

Last observation carried forward (LOCF) and baseline observation carried
forward (BOCF) are ad-hoc imputation methods for longitudinal data. The
idea is to take the previous observed value as a replacement for the
missing data. When multiple values are missing in succession, the method
searches for the last observed value.

The function `fill()` from the `tidyr` package applies LOCF by filling in the
last known value. This is useful in situations where values are recorded
only as they change, as in time-to-event data. For example, we may use
LOCF to fill in `Ozone` by

[R code chunk omitted]

[R code chunk omitted]
(ref:locf2) Imputation of `Ozone` by last observation carried forward (LOCF).

Figure \@ref(fig:locf2) plots the results of the first 80 days of the
`Ozone` series. The stretches of red dots
indicate the imputations, and are constant within the same batch of
missing ozone levels. The real, unseen values are likely to vary within
these batches, so applying LOCF here gives implausible imputations.

LOCF is convenient because it generates a complete dataset. It can be
applied with confidence in cases where we are certain what the missing
values should be, for example, for administrative variables in
longitudinal data. For outcomes, LOCF is dubious. The method has long
been used in clinical trials. The U.S. Food and Drug Administration
(FDA) has traditionally viewed LOCF as the preferred method of analysis,
considering it conservative and less prone to selection than listwise
deletion. However, @MOLENBERGHS2007 [pp. 47–50] show that the bias can
operate in both directions, and that LOCF can yield biased estimates
even under MCAR. LOCF needs to be followed by a proper statistical
analysis method that distinguishes between the real and imputed data.
This is typically not done however. Additional concerns about a reversal
of the time direction are given in @KENWARD2009.

The Panel on Handling Missing Data in Clinical Trials recommends that
LOCF and BOCF should not be used as the primary approach for handling
missing data unless the assumptions that underlie them are
scientifically justified [@NRC2010 p. 77].

### Indicator method {#sec:indicator}

Suppose that we want to fit a regression, but there are missing values
in one of the explanatory variables. The indicator method
[@MIETTINEN1985 p. 232] replaces each missing value by a zero and
extends the regression model by the response indicator. The procedure is
applied to each incomplete variable. The user analyzes the extended
model instead of the original.

In `R` the indicator method can be coded as

[R code chunk omitted]

Observe that since the missing data are in `Ozone` we needed to
reverse the direction of the regression model.

The indicator method has been popular in public health and epidemiology.
An advantage is that the indicator method retains the full dataset.
Also, it allows for systematic differences between the observed and the
unobserved data by inclusion of the response indicator, and could be
more efficient. @WHITE2005 pointed out that the method can be useful to
estimate the treatment effect in randomized trials when a baseline
covariate is partially observed. If the missing data are restricted to
the covariate, if the interest is solely restricted to estimation of the
treatment effect, if compliance to the allocated treatment is perfect
and if the model is linear without interactions, then using the
indicator method for that covariate yields an unbiased estimate of the
treatment effect. This is true even if the missingness depends on the
covariate itself. Additional work can be found in @GROENWOLD2012
[@SULLIVAN2016]. It is not yet clear whether the coverage of the
confidence interval around the treatment estimate will be satisfactory
for multiple incomplete baseline covariates.

The conditions under which the indicator method works may not be met in
practice. For example, the method does not allow for missing data in the
outcome, and generally fails in observational data. It has been shown
that the method can yield severely biased regression estimates, even
under MCAR and for low amounts of missing data
[@VACH1991; @GREENLAND1995; @KNOL2010]. The indicator method may have
its uses in particular situations, but fails as a generic method to
handle missing data.

### Summary {#sec:simplesummary}

  ------------ ------ ---------------- ------------- -------------
                         Unbiased                    Standard Error
                Mean     Reg Weight     Correlation
  Listwise      MCAR        MCAR           MCAR        Too large
  Pairwise      MCAR        MCAR           MCAR       Complicated
  Mean          MCAR         –               –         Too small
  Regression    MAR         MAR              –         Too small
  Stochastic    MAR         MAR             MAR        Too small
  LOCF           –           –               –         Too small
  Indicator      –           –               –         Too small
  ------------ ------ ---------------- ------------- -------------

  : (\#tab:simple) Overview of assumptions made by ad-hoc methods.

Table \@ref(tab:simple) provides a summary of the methods discussed in this
section. The table addresses two topics: whether the method yields the
correct results on average (unbiasedness), and whether it produces the
correct standard error. Unbiasedness is evaluated with respect to three
types of estimates: the mean, the regression weight (with the incomplete
variable as dependent) and the correlation.

The table identifies the assumptions on the missing data mechanism each
method must make in order to produce unbiased estimates. The first line
of the table should be read as follows:

1.  *Listwise deletion* produces an unbiased estimate of the
    *mean* provided that the data are *MCAR*;

2.  *Listwise deletion* produces an estimate of the standard error
    that is *too large*.

The interpretation of the other lines is similar. The “–” sign in some
cells indicates that the method cannot produce unbiased estimates.
Observe that both deletion methods require MCAR for all types.
Regression imputation and stochastic regression imputation can yield
unbiased estimates under MAR. In order to work, the model needs to be
correctly specified. LOCF and the indicator method are incapable of
providing consistent estimates, even under MCAR. Note that some special
cases are not covered in Table \@ref(tab:simple). For example, listwise
deletion is unbiased under two special MNAR scenarios (cf. Section
\@ref(sec:when)).

Listwise deletion produces standard errors that are correct for the
subset of complete cases, but in general too large for the entire
dataset. Calculation of standard errors under pairwise deletion is
complicated. The standard errors after single imputation are too small
since the standard calculations make no distinction between the observed
data and the imputed data. Correction factors for some situations have
been developed [@SCHAFER2000], but a more convenient solution is
multiple imputation.

## Multiple imputation in a nutshell {#sec:nutshell}

### Procedure

Multiple imputation creates $m>1$ complete datasets. Each of these
datasets is analyzed by standard analysis software. The $m$ results are
pooled into a final point estimate plus standard error by pooling rules
(“Rubin’s rules”). Figure \@ref(fig:miflow) illustrates the three main
steps in multiple imputation: imputation, analysis and pooling.

[R code chunk omitted]
(ref:miflow) Scheme of main steps in multiple imputation.

The analysis starts with observed, incomplete data. Multiple imputation
creates several complete versions of the data by replacing the missing
values by plausible data values. These plausible values are drawn from a
distribution specifically modeled for each missing entry. Figure
\@ref(fig:miflow) portrays $m=3$ imputed datasets. In practice, $m$ is
often taken larger (cf. Section \@ref(sec:howmany)). The number $m=3$ is
taken here just to make the point that the technique creates multiple
versions of the imputed data. The three imputed datasets are identical
for the observed data entries, but differ in the imputed values. The
magnitude of these difference reflects our uncertainty about what value
to impute.

The second step is to estimate the parameters of interest from each
imputed dataset. This is typically done by applying the analytic method
that we would have used had the data been complete. The results will
differ because their input data differ. It is important to realize that
these differences are caused only because of the uncertainty about what
value to impute.

The last step is to pool the $m$ parameter estimates into one estimate,
and to estimate its variance. The variance combines the conventional
sampling variance (within-imputation variance) and the extra variance
caused by the missing data extra variance caused by the missing data
(between-imputation variance). Under the appropriate conditions, the
pooled estimates are unbiased and have the correct statistical
properties.

### Reasons to use multiple imputation

Multiple imputation [@RUBIN1987; @RUBIN1996] solves the problem of “too
small” standard errors in Table \@ref(tab:simple). Multiple imputation is
unique in the sense that it provides a mechanism for dealing with the
inherent uncertainty of the imputations themselves.

Our level of confidence in a particular imputed value is expressed as
the variation across the $m$ completed datasets. For example, in a
disability survey, suppose that the respondent answered the item whether
he could walk, but did not provide an answer to the item whether he
could get up from a chair. If the person can walk, then it is highly
likely that the person will also be able to get up from the chair. Thus,
for persons who can walk, we can draw a “yes” for missing “getting up
from a chair” with a high probability, say 0.99, and use the drawn value
as the imputed value. In the extreme, if we are really certain, we
always impute the same value for that person. In general however, we are
less confident about the true value. Suppose that, in a growth study,
height is missing for a subject. If we only know that this person is a
woman, this provides some information about likely values, but not so
much. So the range of plausible values from which we draw is much larger
here. The imputations for this woman will thus vary a lot over the
different datasets. Multiple imputation is able to deal with both
high-confidence and low-confidence situations equally well.

Another reason to use multiple imputation is that it separates the
solution of the missing data problem from the solution of the
complete-data problem. The missing-data problem is solved first, the
complete-data problem next. Though these phases are not completely
independent, the answer to the scientifically interesting question is
not obscured anymore by the missing data. The ability to separate the
two phases simplifies statistical modeling, and hence contributes to a
better insight into the phenomenon of scientific study.

### Example of multiple imputation {#sec:miexample}

Continuing with the `airquality` dataset, it is straightforward to 
apply multiple imputation. The following code imputes the missing 
data twenty times, fits a linear regression model to predict `Ozone` 
in each of the imputed datasets, pools the twenty sets of estimated 
parameters, and calculates the Wald statistics for testing 
significance of the weights.

[R code chunk omitted]

There is much more to say about each of these steps, but it shows that
multiple imputation need not be a daunting task. Assuming we have set
`options(na.action = na.omit)`, fitting the same model to the complete 
cases can be done by

[R code chunk omitted]

The solutions are nearly identical here, which is due to the fact that
most missing values occur in the outcome variable. The standard errors
of the multiple imputation solution are slightly smaller than in the
complete-case analysis. Multiple imputation is often more efficient than
complete-case analysis. Depending on the data and the model at hand, the
differences can be dramatic.

[R code chunk omitted]
(ref:plotairmi) Multiple imputation of `Ozone`. Plotted are the imputed values from the first imputation.

Figure \@ref(fig:plotairmi) shows the distribution and scattergram for the
observed and imputed data combined. The imputations are taken from the
first completed dataset. The blue and red distributions are
quite similar. Problems with the negative values as in Figure
\@ref(fig:plotsri) are now gone since the imputation method used observed data
as donors to fill the missing data. Section \@ref(sec:pmm) describes the
method in detail. Note that the red points respect the heteroscedastic
nature of the relation between `Ozone` and `Solar.R`. All in all, the red 
points look as if they could have been measured if they had not been 
missing. The reader can easily recalculate the solution and inspect these 
plots for the other imputations.

[R code chunk omitted]
(ref:air10) Multiple imputation of `Ozone`. Plotted are the observed values (in blue) and the multiply imputed values (in red).

Figure \@ref(fig:air10) plots the completed `Ozone` data. The
imputed data of all five imputations are plotted for the days with
missing `Ozone` scores. In order to avoid clutter, the
lines that connect the dots are not drawn for the imputed values. Note
that the pattern of imputed values varies substantially over the days.
At the beginning of the series, the values are low and the spread is
small, in particular for the cold and windy days 25–27. The small spread
for days 25–27 indicates that the model is quite sure of these values.
High imputed values are found around the hot and sunny days 35–42,
whereas the imputations during the moderate days 52–61 are consistently
in the moderate range. Note how the available information helps
determine sensible imputed values that respect the relations between
wind, temperature, sunshine and ozone.

One final point. The `airquality` data is a
time series of 153 days. It is well known that the standard error of the
ordinary least squares (OLS) estimate is inefficient (too large) if the
residuals have positive serial correlation [@HARVEY1981]. The first
three autocorrelations of the `Ozone` are
indeed large: 0.48, 0.31 and 0.29. The residual autocorrelations are
however small and within the confidence interval: 0.13, $-0.02$ and
0.04. The inefficiency of OLS is thus negligible here.

## Goal of the book {#sec:goal}

The main goal of this book is to add multiple imputation to the tool
chest of practitioners. The text explains the ideas underlying multiple
imputation, discusses when multiple imputation is useful, how to do it
in practice and how to report the results of the steps taken.

The computations are done with the help of the `R` package `mice`,
written by Karin Groothuis-Oudshoorn and myself [@VANBUUREN2011B]. The
book thus also serves as an extended tutorial on the practical
application of `mice`. Online materials that accompany the book
can be found on www.multiple-imputation.com. My hope
is that this hands-on approach will facilitate understanding of the key
ideas in multiple imputation.

## What the book does not cover {#sec:doesnotcover}

The field of missing data research is vast. This book focuses on
multiple imputation. The book does not attempt cover the enormous body
of literature on alternative approaches to incomplete data. This section
briefly reviews three of these approaches.

### Prevention {#sec:prevention}

With the exception of @MCKNIGHT2007 [Chapter 4], books on missing data
do not mention prevention. Yet, prevention of the missing data is the
most direct attack on problems caused by the missing data. Prevention is
fully in spirit with the quote of Orchard and Woodbury given on p. .
There is a lot one could do to prevent missing data. The remainder of
this section lists point-wise advice.

Minimize the use of intrusive measures, like blood samples. Visit the
subject at home. Use incentives to stimulate response, and try to match
up the interviewer and respondent on age and ethnicity. Adapt the mode
of the study (telephone, face to face, web questionnaire, and so on) to
the study population. Use a multi-mode design for different groups in
your study. Quickly follow-up for people that do not respond, and where
possible try to retrieve any missing data from other sources.

In experimental studies, try to minimize the treatment burden and
intensity where possible. Prepare a well-thought-out flyer that explains
the purpose and usefulness of your study. Try to organize data
collection through an authority, e.g., the patient’s own doctor. Conduct
a pilot study to detect and smooth out any problems.

Economize on the number of variables collected. Only collect the
information that is absolutely essential to your study. Use short forms
of measurement instruments where possible. Eliminate vague or ambivalent
questionnaire items. Use an attractive layout of the instruments.
Refrain from using blocks of items that force the respondent to stay on
a particular page for a long time. Use computerized adaptive testing
where feasible. Do not allow other studies to piggy-back on your data
collection efforts.

Do not overdo it. Many Internet questionnaires are annoying because they
force the respondent to answer. Do not force your respondent. The result
will be an apparently complete dataset with mediocre data. Respect the
wish of your respondent to skip items. The end result will be more
informative.

Use double coding in the data entry, and chase up any differences
between the versions. Devise nonresponse forms in which you try to find
out why people they did not respond, or why they dropped out.

Last but not least, consult experts. Many academic centers have
departments that specialize in research methodology. Sound expert advice
may turn out to be extremely valuable for keeping your missing data rate
under control.

Most of this advice can be found in books on research methodology and
data quality. Good books are @SHADISH2001, @DELEEUW2008, @DILLMAN2008
and @GROVES2009.

### Weighting procedures {#sec:weighting}

Weighting is a method to reduce bias when the probability to be selected
in the survey differs between respondents. In sample surveys, the
responders are weighted by design weights, which are inversely
proportional to their probability of being selected in the survey. If
there are missing data, the complete cases are re-weighted according to
design weights that are adjusted to counter any selection effects
produced by nonresponse. The method is widely used in official
statistics. Relevant pointers include @COCHRAN1977 and @SARNDAL1992 and
@BETHLEHEM2002.

The method is relatively simple in that only one set of weights is
needed for all incomplete variables. On the other hand, it discards data
by listwise deletion, and it cannot handle partial response. Expressions
for the variance of regression weights or correlations tend to be
complex, or do not exist. The weights are estimated from the data, but
are generally treated as fixed. The implications for this are unclear
[@LITTLE2002 p. 53].

There has been interest recently in improved weighting procedures that
are “double robust” [@SCHARFSTEIN1999; @BANG2005]. This estimation
method requires specification of three models: Model A is the
scientifically interesting model, Model B is the response model for the
outcome, and model C is the joint model for the predictors and the
outcome. The dual robustness property states that: if either Model B or
Model C is wrong (but not both), the estimates under Model A are still
consistent. This seems like a useful property, but the issue is not free
of controversy [@KANG2007].

### Likelihood-based approaches {#sec:likelihood}

Likelihood-based approaches define a model for the observed data. Since
the model is specialized to the observed values, there is no need to
impute missing data or to discard incomplete cases. The inferences are
based on the likelihood or posterior distribution under the posited
model. The parameters are estimated by maximum likelihood, the EM
algorithm, the sweep operator, Newton–Raphson, Bayesian simulation and
variants thereof. These methods are smart ways to skip over the missing
data, and are known as direct likelihood, full information maximum
likelihood (FIML), and more recently, pairwise likelihood estimation.

Likelihood-based methods are, in some sense, the “royal way” to treat
missing data problems. The estimated parameters nicely summarize the
available information under the assumed models for the complete data and
the missing data. The model assumptions can be displayed and evaluated,
and in many cases it is possible to estimate the standard error of the
estimates.

Multiple imputation extends likelihood-based methods by adding an extra
step in which imputed data values are drawn. An advantage of this is
that it is generally easier to calculate the standard errors for a wider
range of parameters. Moreover, the imputed values created by multiple
imputation can be inspected and analyzed, which helps us to gauge the
effect of the model assumptions on the inferences.

The likelihood-based approach receives an excellent treatment in the
book by @LITTLE2002. A less technical account that should appeal to
social scientists can be found in @ENDERS2010 [chapters 3–5].
@MOLENBERGHS2007 provide a hands-on approach of likelihood-based methods
geared toward clinical studies, including extensions to data that are
MNAR. The pairwise likelihood method was introduced by @KATSIKATSOU2012
and has been implemented in `lavaan`.

## Structure of the book {#sec:structure}

This book consists of three main parts: basics, case studies and
extensions. Chapter \@ref(ch:mi) reviews the history of multiple imputation
and introduces the notation and theory. Chapter \@ref(ch:univariate)
provides an overview of imputation methods for univariate missing data.
Chapter \@ref(ch:multivariate) distinguishes three approaches to attack the
problem of multivariate missing data. Chapter \@ref(ch:analysis) reviews
issues pertaining to the analysis of the imputed datasets.

Chapter \@ref(ch:practice) discusses practical issues for multivariate
missing data. Chapter \@ref(ch:multilevel) discusses the problem how to
impute for nested data so as to preserve the multilevel structure.
Chapter \@ref(ch:ice) explores the use of multiple imputation to estimate
individual causal effects.

Chapters \@ref(ch:measurement)–\@ref(ch:longitudinal) contain case studies of
the techniques described in the previous chapters. Chapter
\@ref(ch:measurement) deals with “problems with the columns,” while Chapter
\@ref(ch:selection) addresses “problems with the rows”. Chapter
\@ref(ch:longitudinal) discusses studies on problems with both rows and
columns.

Chapter \@ref(ch:conclusion) concludes the main text with a discussion of
limitations and pitfalls, reporting guidelines, alternative applications
and future extensions.

## Exercises {#ex:ch1}

```{exercise, name = "Reporting practice", label = "report"}
What are the reporting practices in your field? Take a random sample 
of articles that have appeared during the last 10 years in the leading 
journal in your field. Select only those that present quantitative 
analyses, and address the following topics:
  
1. Did the authors report that there were missing data?
  
2. If not, can you infer from the text that there must have
   been missing data?
  
3. Did the authors discuss how they handled the missing
   data?
  
4. Were the missing data properly addressed?
  
5. Can you detect a trend over time in reporting practice?
  
6. Would the editors of the journal be interested in your findings?

```

```{exercise, name = "Loss of information", label = "caseslost"}
Suppose that a dataset consists of 100 cases and 10 variables. 
Each variable contains 10% missing values. What is the 
largest possible subsample under listwise deletion? What
is the smallest? If each variable is MCAR, how many cases will
remain?
```

```{exercise, name = "Stochastic regression imputation", label = "sriexr"}
The correlation of the data in Figure \@ref(fig:plotsri) is 
equal to 0.33. This is relatively low compared to the other 
correlations reported in Section \@ref(sec:simplesolutions). 
This seems to contradict the statement that stochastic regression 
imputation does not bias the correlation. Could this low correlation 
be due to random variation?

1. Rerun the code with a different `seed` value. What is the 
   correlation now?
     
2. Write a loop to apply apply stochastic regression imputation 
   with the `seed` increasing from 1 to 1000. Calculate the 
   regression weight and the correlation for each solution, and 
   plot the histogram. What are the mean, minimum and maximum 
   values of the correlation?
     
3. Do your results indicate that stochastic regression imputation 
   alters the correlation?

```


```{exercise, name = "Stochastic regression imputation (continued)", label = "sricontinued"}
The largest correlation found in the previous exercise exceeds the value found
in Section \@ref(sec:regimp). This seems odd since the correlation of
the imputed values under regression imputation is equal to 1, and hence the 
imputed data have a maximal contribution to the overall correlation.

1. Can you explain why this could happen?

2. Adapt the code from the previous exercise to test your explanation. 
   Was your explanation satisfactory?

3. If not, can you think of another reason, and test that?
   Hint: Find out what is special about the solutions with the
   largest correlations.

```

```{exercise, name = "Nonlinear model", label = "nonlinear"}
The model fitted to the `airquality` data in Section \@ref(sec:miexample) 
is a simple linear model. Inspection of the residuals reveals that 
there is a slight curvature in the average of the residuals.

1. Start from the completed cases, and use `plot(fit)` to obtain 
   diagnostic plots. Can you explain why the curvature shows up?

2. Experiment with solutions, e.g., by transforming `Ozone` or 
   by adding a quadratic term to the model. Can you make the 
   curvature disappear? Does the amount of explained variance 
   increase?

3. Does the curvature also show up in the imputed data? If so, 
   does the same solution work? Hint: You can assess the 
   $j^\mathrm{th}$ fitted model by `getfit(fit, j)`, where
   `fit` was created by `with(imp,...)`.

4. Advanced: Do you think your solution would necessitate
   drawing new imputations?

```

---

# Analysis of imputed data {#ch:analysis}

> You must use a computer to do data science; you cannot do it in
> your head, or with pencil and paper.
> 
> --- Hadley Wickham

[R code chunk omitted]

Creating plausible imputations is the most challenging activity in
multiple imputation. Once we have the multiply imputed data, we can
estimate the parameters of scientific interest from each of the $m$
imputed datasets, but now without the need to deal with the missing
data, as all data are now complete. These repeated analyses produce $m$
results.

The $m$ results will feed into step 3 (pooling the results). The pooling
step to derive the final statistical inferences is relatively
straightforward, but its application in practice is not entirely free of
problems. First of all, the complete-data analyses are nontrivial.
Historically, the imputation literature (including the first edition of
this book) has concentrated on step 1 (creating the imputations) and on
step 3 (pooling the results), and has worked from the notion that step 2
(estimating the parameters) is well-specified and easy to execute once
the data are complete. In practice step 2 can be quite involved. The
step often includes model searching, optimization, validation,
prediction, assessment of the quality of model fit, in fact, step 2 may
embrace almost any aspect of machine learning and data science. All the
analyses need to be repeated for each of the $m$ datasets, which may put
a considerable burden on the data analyst.

Fortunately, thanks to tremendous advances in recent computational
technology, the use of modern data science techniques in step 2 is now
becoming feasible. This chapter focuses on step 2. The next chapter
addresses issues related to step 3.

## Workflow

[R code chunk omitted]
(ref:miflowb) Scheme of main steps in multiple imputation.

Figure \@ref(fig:miflowb) outlines the three main steps in any multiple
imputation analysis. In step 1, we create several $m$ complete versions
of the data by replacing the missing values by plausible data values.
The task of step 2 is to estimate the parameters of scientific or
commercial interest from each imputed dataset. Step 3 involves pooling
the $m$ parameter estimates into one estimate, and obtaining an estimate
of its variance. The results allow us to arrive at valid decisions from
the data, accounting for the missing data and having the correct type I
error rate.

Class Name    Produced by    Description
----- ------- -------------- ---------------------------------------
`mids`  `imp`   `mice()`       multiply imputed dataset
`mild`  `idl`   `complete()`   multiply imputed list of data
`mira`  `fit`   `with()`       multiple imputation repeated analyses
`mipo`  `est`   `pool()`       multiple imputation pooled results

: (\#tab:classes) Overview of the classes in the `mice` package.

### Recommended workflows {#sec:goodworkflows}

There is more than one way to divide the work that implements the steps
of Figure \@ref(fig:miflowb). The classic workflow in `mice` runs functions
`mice()`, `with()` and `pool()` in succession, each time saving
the intermediate result:

[R code chunk omitted]

The objects `imp`, `fit` and `est` have classes `mids`, `mira` and `mipo`,
respectively. See Table \@ref(tab:classes) for an overview. The classic
workflow works because `mice` contains a `with()` function that 
understands how to deal with a `mids`-object. The classic `mids` workflow 
has been widely adopted, but there are more possibilities.

The `magrittr` package introduced the pipe operator to `R`. This operator
removes the need to save and reread objects, resulting in more compact
and better readable code:

[R code chunk omitted]

The `with()` function handles two tasks: to fill in the missing data 
and to analyze the data. Splitting these over two separate functions 
provided the user easier access to the imputed data, and hence is more 
flexible. The following code uses the `complete()` function to save 
the imputed data as a list of dataset (i.e., as an object with class
`mild`), and then executes the analysis on each dataset by the 
`lapply()` function.

[R code chunk omitted]

If desired, we may extend the `mild` workflow by recycling through 
multiple arguments by means of the `Map` function.

[R code chunk omitted]

RStudio has been highly successful with the introduction of the free and
open `tidyverse` ecosystem for data acquisition, organization, analysis, 
visualization and reproducible research. The book by @WICKHAM2017 
provides an excellent introduction to data science using `tidyverse`. The
`mild` workflow can be written in `tidyverse` as

[R code chunk omitted]

Manipulating the imputed data is easy if we store the imputed data in
`long` format.

[R code chunk omitted]

The `long` format can be processed by the `dplyr::do()` function into 
a list-column and pooled, as follows:

[R code chunk omitted]

These workflows yield identical estimates, but allow for different
extensions.

### Not recommended workflow: Averaging the data {#sec:badworkflowa}

Researchers are often tempted to average the multiply imputed data, and
analyze the averaged data as if it were complete. This method yields
incorrect standard errors, confidence intervals and $p$-values, and thus
should not be used if any form of statistical testing or uncertainty
analysis is to be done on the imputed data. The reason is that the
procedure ignores the between-imputation variability, and hence shares
all the drawbacks of single imputation. See Section 
\@ref(sec:simplesolutions).

Averaging the data and analyzing the aggregate is easy to do with
`dplyr`:

[R code chunk omitted]

This workflow is faster and easier than the methods in Section
\@ref(sec:goodworkflows), since there is no need to replicate the analyses
$m$ times. In the words of @DEMPSTER1983, this workflow is

> ... seductive because it can lull the user into the pleasurable state
> of believing that the data are complete after all.

The ensuing statistical analysis does not know which data are observed
and which are missing, and treats all data values as real, which will
underestimate the uncertainty of the parameters. The reported standard
errors and $p$-values after data-averaging are generally too low. The
correlations between the variables of the averaged data will be too
high. For example, the correlation matrix is the average data

[R code chunk omitted]

are more extreme than the average of the $m$ correlation matrices[^1]

[R code chunk omitted]

which is an example of ecological fallacy. As researchers tend to like
low $p$-values and high correlations, there is a cynical reward for the
analysis of the average data. However, analysis of the average data
cannot give a fair representation of the uncertainties associated with
the underlying data, and hence is not recommended.

### Not recommended workflow: Stack imputed data {#sec:badworkflowb}

A variation on this theme is to stack the imputed data, thus creating
$m\times n$ complete records. Each record is weighted by a factor $1/m$,
so that the total sample size is equal to $n$. The statistical analysis
amounts to performing a weighted linear regression. If the scientific
interest is restricted to point estimates and if the complete-data model
is linear, this analysis of the stacked imputed data will yield unbiased
estimates. Be aware that routine methods for calculating test
statistics, confidence intervals or $p$-values will provide invalid
answers if applied to the stacked imputed data.

Creating and analyzing a stacked imputed dataset is easy:

[R code chunk omitted]

While the estimated regression coefficients are unbiased, we cannot
trust the standard errors, $t$-values and so on. An advantage of
stacking over averaging is that it is easier to analyze categorical
data. Although stacking can be useful in specific contexts, like
variable selection, in general it is not recommended.

### Repeated analyses {#sec:repeated}

The appropriate way to analyze multiply imputed data is to fit the
complete-data model on each imputed dataset separately. In
`mice` we can use the `with()` command for this purpose. This
function takes two main arguments. The first argument of the call is a
`mids` object produced by `mice()`. The second argument is an expression
that is to be applied to each completed dataset. The `with()` function 
implements the following loop ($\ell=1,\dots,m$):

1.  it creates the $\ell^\mathrm{th}$ imputed dataset

2.  it runs the expression on the imputed dataset

3.  it stores the result in the list `fit$analyses`

For example, we fit a regression model to each dataset and print out the
estimates from the first and second completed datasets by

[R code chunk omitted]

Note that the estimates differ from each other because of the
uncertainty created by the missing data. Applying the standard pooling
rules is done by

[R code chunk omitted]

which shows the correct estimates after multiple imputation.

Any `R` expression produced by `expression()` can be evaluated on the
multiply imputed data. For example, suppose we want to calculate the
difference in frequencies between categories 1 and 2 of `hyp`. 
This is conveniently done by the following statements:

[R code chunk omitted]

All the major software packages nowadays have ways to execute the $m$
repeated analyses to the imputed data.

## Parameter pooling {#sec:pooling}

### Scalar inference of normal quantities

Section \@ref(sec:inference) describes Rubin’s rules for pooling the
results from the $m$ complete-data analyses. These rules are based on
the assumption that the parameter estimates $\hat Q$ are normally
distributed around the population value $Q$ with a variance of $U$. Many
types of estimates are approximately normally distributed, e.g., means,
standard deviations, regression coefficients, proportions and linear
predictors. Rubin’s pooling rules can be applied directly to such
quantities [@SCHAFER1997; @MARSHALL2009].

### Scalar inference of non-normal quantities {#sec:poolnon}

How should we combine quantities with non-normal distributions:
correlation coefficients, odds ratios, relative risks, hazard ratios,
measures of explained variance and so on? The quality of the pooled
estimate and the confidence intervals can be improved when pooling is
done in a scale for which the distribution is close to normal. Thus,
transformation toward normality and back-transformation into the
original scale improves statistical inference.

As an example, consider transforming a correlation coefficient
$\rho_\ell$ for $\ell=1,\dots,m$ toward normality using the Fisher $z$
transformation

$$
z_\ell = \frac{1}{2}\ln{\frac{1+\rho_\ell}{1-\rho_\ell}}(\#eq:fisher)
$$

For large samples, the distribution of $z_\ell$ is normal with variance
$\sigma^2 = 1/(n-3)$. It is straightforward to calculate the pooled
correlation $\bar z$ and its variance by Rubin’s rules. The result can
be back-transformed by the inverse Fisher transformation

$$
\bar \rho = \frac{e^{2\bar z}-1}{e^{2\bar z}+1}(\#eq:invfisher)
$$

The confidence interval of $\bar \rho$ is calculated in the $z$-scale as
usual, and then back-transformed by Equation \@ref(eq:invfisher).

  Statistic                  Transformation          Source
  -------------------------- ----------------------- ---------------
  Correlation                Fisher $z$              @SCHAFER1997
  Odds ratio                 Logarithm               @AGRESTI1990
  Relative risk              Logarithm               @AGRESTI1990
  Hazard ratio               Logarithm               @MARSHALL2009
  Explained variance $R^2$   Fisher $z$ on root      @HAREL2009
  Survival probabilities     Complementary log-log   @MARSHALL2009
  Survival distribution      Logarithm               @MARSHALL2009

  : (\#tab:transforms) Suggested transformations toward normality for 
  various types of statistics. The transformed quantities can be 
  pooled by Rubin’s rules.

Table \@ref(tab:transforms) suggests transformations toward approximate
normality for various types of statistics. There are quantities for
which the distribution is complex or unknown. Examples include the
Cramér $C$ statistic [@BRAND1999] and the discrimination index
[@MARSHALL2009]. Ideally, the entire sampling distribution should be
pooled in such cases, but the corresponding pooling methods have yet to
be developed. The current advice is to search for ad hoc transformations
to make the sampling distribution close to normality, and then apply
Rubin’s rules.

## Multi-parameter inference {#sec:multiparameter}

There are many situations where we need to test whether a set of
parameters is significantly different from zero. For example, if a
categorical variable enters the analysis through a set of dummy
variables, all parameters related to this set should be tested
simultaneously. More generally, ANOVA type of designs can be formulated
and tested as a multi-parameter inference regression problem.
@VANGINKEL2014 provide many practical examples with missing data.

@SCHAFER1997 distinguished three types of statistics in multi-parameter
tests: $D_1$ (multivariate Wald test), $D_2$ (combining test statistics)
and $D_3$ (likelihood ratio test). The next sections outline the idea of
each approach, and demonstrate how these tests can be performed as part
of the repeated data analyses .

### $D_1$ Multivariate Wald test {#sec:wald}

The multivariate Wald test is an extension of the procedure for scalar
quantities as described in Section \@ref(sec:singlepar). The procedure
tests whether $Q = Q_0$, where $Q_0$ is a $k$-vector of values under the
null hypothesis (typically all zeros). The multivariate Wald test
requires an estimate of the variance-covariance matrix $U$ of $\bar Q$.
We could use $T$ from Equation \@ref(eq:poolT), but this estimate can be
unreliable. The problem is that for small $m$, the estimate of the
between-imputation variance $B$ is unstable, and if $m\leq k$, it is not
even full rank. Thus $T$ can be unreliable if $B$ is a substantial
component of $T$.

@LI1991B proposed an estimate of $T$ in which $B$ and $\bar U$ are
assumed to be proportional to each other. A more stable estimate of the
total variance is then $\tilde T = (1+r_1)\bar U$, where $r_1 = \bar r$
(from Equation \@ref(eq:barrm)) is the average fraction of missing
information.

Under the assumption that $(Q_0 - \bar Q)$ is sufficiently close to a
normal distribution, the $D_1$-statistic

$$
D_1 = (\bar Q-Q_0)'\tilde T^{-1}(\bar Q-Q_0)/k (\#eq:d1)
$$ 

follows an $F$-distribution $F_{k,\nu_w}$ with $k$ and $\nu_1$ degrees of
freedom, where 

$$
\nu_1 = \left\{\begin{array}
      {l@{\quad}l}
    4 + (t-4)[1+(1-2t^{-1})r_1^{-1}]^2 & \mathrm{if} \quad t = k(m-1) > 4\\
    t(1+k^{-1})(1+r_1^{-1})^2/2 & \mathrm{otherwise}(\#eq:dfwald)
  \end{array} \right.
$$ 

The $p$-value for $D_1$ is

$$
P_1 = \Pr[F_{k,\nu_1}>D_1]  (\#eq:waldp)
$$

The assumption that the fraction of missing information is the same
across all variables and statistics is unlikely to hold in practice.
However, @LI1991B provide encouraging simulation results for situations
where this assumption is violated. Except for some extreme cases, the
level of the procedure was close to the nominal level, while the loss of
power from such violations was modest.

The work of @LI1991B is based on large samples. @REITER2007 developed a
small-sample version for the degrees of freedom using ideas similar to
@BARNARD1999A. Reiter’s $\nu_f$ spans several lines of text, and is not
given here. A simulation study conducted by Reiter showed marked
improvements over the earlier formulation, especially in smaller
samples. Simulation work by @GRUND2016a and @LIU2017 confirmed that for
small samples (say $n < 50$) $\nu_f$ is more conservative than $\nu_1$,
and produced type I errors rates closer to their nomimal value.
@RAGHU2015 recently provided an elegant alternative based on Equation
\@ref(eq:newnu) with $\nu_\mathrm{obs}$ substituted as
$\nu_\mathrm{obs} = (\nu_\mathrm{com}+1)\nu_\mathrm{com}/(\nu_\mathrm{com}+3)(1+\bar r)$.
It is not yet known how this correction compares to $\nu_1$ and $\nu_f$.

The `mice` package implements the multivariate
Wald test as the `D1()` function. Let us
impute the `nhanes2` data, and fit the linear
regression of `chl` on `age` and `bmi`.

[R code chunk omitted]

We want to simplify the model by testing for `age`. Since `age`
is a categorical variable with three categories, removing it involves
deleting two columns at the same time, hence the univariate Wald test
does not apply. The solution is to fit the model without `age`, and 
run the multivariate Wald statistic to test whether the model estimates 
are different.

[R code chunk omitted]

Since the Wald test is significant, removing `age` from the model 
reduces its predictive power.

### $D_2$ Combining test statistics$^\spadesuit$ {#sec:chi}

The multivariate Wald test may become cumbersome when $k$ is large, or
when many tests are to be done. Some analytic models may not produce an
estimate of $Q$, or of its variance-covariance matrix. For example,
nonparametric tests like the sign test or Wilcoxon-Mann-Whitney produce
a $p$-value, and no estimate of $Q$. In cases like these, we can still
calculate a combined significance test using the $m$ test statistics
(e.g., $p$-values, $Z$-values, $\chi^2$-values, $t$-values) as input.

@RUBIN1987 [p. 87] and @LI1991 describe a procedure for pooling the
values of the test statistics. Suppose that $d_\ell$ is the test
statistic obtained from the analysis of the $\ell^\mathrm{th}$ imputed
dataset $Y_\ell$, $\ell=1,\dots,m$. Let $\bar d = m^{-1}\sum_\ell d_\ell$ 
be the average test statistic. The statistic for the combined test is

$$
D_2 = \frac{\bar dk^{-1}-(m+1)(m-1)^{-1}r_2}{1+r_2}  (\#eq:D2)
$$

where the relative increase of the variance is calculated as

$$
r_2 = \left(1+\frac{1}{m}\right)\frac{1}{m-1}\sum_{\ell=1}^m\left(\sqrt{d_\ell}-\overline{\sqrt{d}}\right)^2 (\#eq:r2)
$$

with $\overline{\sqrt{d}} = m^{-1}\sum_\ell \sqrt{d_\ell}$, so that
$r_2$ equals the sample variance of $\sqrt{d_1}$, $\sqrt{d_2}$, …,
$\sqrt{d_m}$ multiplied by $(1 + 1/m)$. The $p$-value for testing the
null hypothesis is 

$$
P_2 = \Pr[F_{k,\nu_2} > D_2] (\#eq:p2)
$$ 

where

$$
\nu_2 = k^{-3/m}(m-1)(1+r_2^{-1})^2  (\#eq:nu2)
$$

The procedure assumes that the test statistic is approximately normally
distributed. This is clearly not the case for $p$-values, which follow a
uniform distribution under the null. One may transform the $p$-values to
approximate normality, combine and back-transform afterwards. Based on
this idea, @LICHT2010 [pp. 40–43] proposed a method for obtaining
significance levels from repeated $p$-values similar to Equation
\@ref(eq:D2) with custom $r_2$ and $\nu_2$.

In context of significance testing for logistic regression, @EEKHOUT2017
suggest taking the median of the $m$ $p$-values as the combined
$p$-value, an exceedingly simple method. It nevertheless appears to
outperform more sophisticated techniques if the variable to be tested is
categorical with more than two categories. It would be useful to explore
whether this *median $P$ rule* has wider validity.

Let us continue with the previous example. Suppose that our software
cannot export the variance-covariance matrix in each repeated analysis,
but it does provide a table with the Wald statistics for testing
`age`. The `D2`
function calculates the $D_2$-statistic and its degrees of freedom as

[R code chunk omitted]

In contrast to the previous analysis, observe that the $D_2$-statistic
is not significant at an $\alpha$-level of 0.05. The reason is that the
$D_2$ test is less informed by the data, and hence less powerful than
the $D_1$ test.

### $D_3$ Likelihood ratio test$^\spadesuit$ {#sec:likelihoodratio}

The likelihood ratio test [@MENG1992] is designed to handle situations
where one cannot obtain the covariance matrices of the complete-data
estimates. This could be the case if the dimensionality of $Q$ is high,
which can occur with partially classified contingency tables. For large
$n$ the procedure is equivalent to the method of Section \@ref(sec:wald).
The likelihood ratio test is the preferred method for testing random
effects [@SINGER2003], and connects to global model fit statistics in
structural equation models [@ENDERS2016a].

Let the vector $Q$ contain the parameters of interest. We wish to test
the hypothesis $Q=Q_0$ for some given $Q_0$. The usual scenario is that
we compare two models, one where $Q$ can vary freely and one more
restrictive model that constrains $Q=Q_0$.

The procedure for calculating the likelihood ratio test is as follows.
First, estimate $\bar Q$ (for the full model) and $\bar Q_0$ (for the
restricted model) from the $m$ datasets by Rubin’s rules. Calculate the
value of the log-likelihood functions $l(\hat Q_\ell)$ (for the full
model) and $l(\hat Q_{0,\ell})$ (for the restricted model), and
determine the average of the likelihood ratio tests across the $m$
datasets, i.e.,

$$
\hat d = m^{-1} \sum_\ell -2(l(\hat Q_{0,\ell}) - l(\hat Q_\ell))(\#eq:hatd)
$$

Then re-estimate the full and restricted models, with their model
parameters fixed to $\bar Q$ and $\bar Q_0$, respectively, and average
the corresponding likelihood ratio tests as

$$
\bar d = m^{-1} \sum_\ell -2(l(\bar Q_{0,\ell}) - l(\bar Q_\ell))(\#eq:bard)
$$

The test statistic proposed by @MENG1992 is

$$
D_3 = \frac{\bar d}{k(1+r_3)}  (\#eq:D3)
$$

where

$$
r_3 = \frac{m+1}{k(m-1)}(\hat d-\bar d)(\#eq:r3)
$$ 

estimates the average relative increase in variance due to nonresponse. The quantity
$r_3$ is asymptotically equivalent to $\bar r$ from Equation
\@ref(eq:barrm). The $p$-value for $D_3$ is equal to

$$
P_3 = \Pr[F_{k,\nu_3} > D_3](\#eq:p3)
$$ 

where $\nu_3=\nu_1$, or equal Reiter’s correction for small samples.

The likelihood ratio test does not require normality. For complete data,
the likelihood ratio test is invariant to scale changes, which is the
reason that many prefer the likelihood ratio scale over the Wald test.
However, @SCHAFER1997 [p. 118] observed that the invariance property is
lost in multiple imputation because the averaging operations in
Equations \@ref(eq:hatd) and \@ref(eq:bard) may yield somewhat different
results under nonlinear transformations of $l(Q)$. He advised that the
best results will be obtained if the distribution of $Q$ is
approximately normal. One may transform the parameters to achieve
normality, provided that appropriate care is taken to infer that the
result is still within the allowable parameter space.

@LIU2017 found in their simulations that $D_3$ can become negative, a
nonsensical value, in some scenarios. They suggest that a value of
$r_3 > 10$ or a 1000% increase in sampling variance due to missing data
may act as warning signals for this anomaly.

Routine use of the likelihood ratio statistic has long been hampered by
difficulties in calculating the likelihood ratio tests for the models
with fixed parameters $\bar Q$ and $\bar Q_0$. With the advent of the
`broom` package [@ROBINSON2017], the
calculations have become feasible for a wide class of models. The
`D3()` function in
`mice` can be used to calculate the likelihood
ratio test. We apply it to the data from previous examples by

[R code chunk omitted]

The $D_3$-statistic strongly indicates that
`age` is a significant predictor. Note however
the extremely large value for $r_3$ (column
`riv`), so the result must be taken with a
grain of salt. The likely cause for this anomaly could well be the lack
of a small-sample correction for this test.

### $D_1$, $D_2$ or $D_3$?

If the estimates are approximately normal and if the software can
produce the required variance-covariance matrices, we recommend using
$D_1$ with an adjustment for small samples if $n < 100$. $D_1$ is a
direct extension of Rubin’s rules to multi-parameter problems,
theoretically convincing, mature and widely applied. $D_1$ is
insensitive to the assumption of equal fractions of missing information,
is well calibrated, works well with small $m$ (unless the fractions of
information are large and variable) and suffers only modest loss of
power. The relevant literature
[@RUBIN1987; @LI1991B; @REITER2007; @GRUND2016a; @LIU2017] is quite
consistent.

If only the test statistics are available for pooling, then the
$D_2$-statistic is a good option, provided that the number of
imputations $m > 20$. The test is easy to calculate and applies to
different test statistics. For $m < 20$, the power may be low. $D_2$
tends to become optimistic for high fractions of missing information
$(> 0.3)$, and this effect unfortunately increases with sample size
[@GRUND2016a]. Thus, careless application of $D_2$ to large datasets
with many missing values may yield high rates of false positives.

The likelihood ratio statistic $D_3$ is theoretically sound. Calculation
of $D_3$ requires refitting the repeated analysis models with the
estimates constrained to their pooled values. This was once an issue,
but probably less so in the future. $D_3$ is asymptotically equivalent
to $D_1$, and may be preferred for theoretical reasons: it does not
require normality in the complete-data model, it is often more powerful
and it may be more stable than if $k$ is large (as $\bar U$ need not be
inverted). @GRUND2016a, @LIU2017 and @EEKHOUT2017 found that $D_3$
produces Type 1 error rates that were comparable to $D_1$. $D_3$ tends
to be somewhat conservative in smaller samples, especially with high
fractions of missing information and with high $k$. Also, $D_3$ has
lower statistical power in some of the extreme scenarios. For small
samples, $D_1$ has a slight edge over $D_3$, so given the current
available evidence $D_1$ is the better option for $n < 200$. In larger
samples ($n \geq 200$) $D_1$ and $D_3$ appear equally good, so the
choice between them is mostly a matter of convenience.

## Stepwise model selection {#sec:stepwise}

The standard multiple imputation scheme consists of three phases:

1.  Imputation of the missing data $m$ times;

2.  Analysis of the $m$ imputed datasets;

3.  Pooling of the parameters across $m$ analyses.

This scheme is difficult to apply if stepwise model selection is part of
the statistical analysis in phase 2. Application of stepwise variable
selection methods may result in sets of variables that differ across the
$m$ datasets. It is not obvious how phase 3 should be done.

### Variable selection techniques

@BRAND1999 [chap. 7] was the first to recognize and treat the variable
selection problem. He proposed a solution in two steps. The first step
involves performing stepwise model selection separately on each imputed
dataset, followed by the construction of a new supermodel that contains
all variables that were present in at least half of the initial models.
The idea is that this criterion excludes variables that were selected
accidentally. Moreover, it is a rough correction for multiple testing.
Second, a special procedure for backward elimination is applied to all
variables present in the supermodel. Each variable is removed in turn,
and the pooled likelihood ratio $p$-value (Equation \@ref(eq:p3)) is
calculated. If the largest $p$-value is larger than 0.05, the
corresponding variable is removed, and the procedure is repeated on the
smaller model. The procedure stops if all $p \leq 0.05$. The procedure
was found to be a considerable improvement over complete-case analysis.

@YANG2005 proposed variable selection techniques using Bayesian model
averaging. The authors studied two methods. The first method, called
“impute then select,” applies Bayesian variable selection methods on the
imputed data. The second method, called “simultaneously impute and
select” combines selection and missing data imputation into one Gibbs
sampler. Though the latter slightly outperformed the first method, the
first method is more broadly applicable. Application of the second
method seems to require equivalent imputation and analysis models, thus
defeating one of the main advantages of multiple imputation.

@WOOD2008 and @VERGOUWE2010 studied several scenarios for variable
selection. We distinguish three general approaches:

1.  *Majority*. A method that selects variables in the final that appear
    in at least half of the models.

2.  *Stack*. Stack the imputed datasets into a single dataset, assign a
    fixed weight to each record and apply the usual variable
    selection methods.

3.  *Wald*. Stepwise model selection is based on the Wald statistic
    calculated from the multiply imputed data.

The majority method is identical to step 1 of @BRAND1999, whereas the
Wald test method is similar to Brand’s step 2, with the likelihood ratio
test replaced by the Wald test. The Wald test method is recommended
since it is a well-established approach that follows Rubin’s rules,
whereas the majority and stack methods fail to take into account the
uncertainty caused by the missing data. Indeed, @WOOD2008 found that the
Wald test method is the only procedure that preserved the type I error.

@ZHAO2017 review recent work on variable selection on imputed data.
These authors favor approaches based on the least absolute shrinkage and
selection operator (LASSO) [@TIBSHIRANI1996]. The MI-LASSO method by
@CHEN2013 tests the coefficients across all the stacked datasets, thus
ensuring model consistency across different imputations. @MARINO2017
proposed an extension to select covariates in multilevel models.

In practice, it may be useful to combine methods. The Wald test method
is computationally intensive, but is now easily available in
`mice` as the `D1()` function. A strong point of the
majority method is that it gives insight into the variability between
the imputed datasets. An advantage of the stack method is that only one
dataset needs to be analyzed. The discussion of @WOOD2008 contains
additional simulations of a two-step method, in which a preselection
made by the majority and stack methods is followed by the Wald test.
This yielded a faster method with better theoretical properties. In
practice, a judicious combination of approaches might turn out best.

### Computation

The following steps illustrate the main steps involved by implementing a
simple majority method to select variables in
`mice`.

[R code chunk omitted]

This code imputes the `boys` data $m = 10$
times, fits a stepwise linear model to predict
`tv` (testicular volume) separately to each of
the imputed dataset. The following code blocks counts how many times
each variable was selected.

[R code chunk omitted]

The `lapply()` function is used three times.
The first statement extracts the model formulas fitted to the $m$
imputed datasets. The second `lapply()` call
decomposes the model formulas into pieces, and the third call extracts
the names of the variables included in all $m$ models. The
`table()` function counts the number of times
that each variable in the 10 replications. Variables
`age`, `gen` and
`reg` are always included, whereas
`hc` was selected in only one of the models.
Since `hgt` appears in more than 50% of the
models, we can use the Wald test to determine whether it should be in
the final model.

[R code chunk omitted]

The $p$-value is equal to 0.173, so `hgt` is
not needed in the model. If we go one step further, and remove
`phb`, we obtain

[R code chunk omitted]

The significant difference ($p=0.029$) between the models implies that
`phb` should be retained. We obtain similar
results for the other three variables, so the final model contains
`age`, `gen`,
`reg` and `phb`.

### Model optimism {#sec:optimism}

The main danger of data-driven model building strategies is that the
model found may depend highly on the sample at hand. For example,
@VIALLEFONT2001 showed that of the variables declared to be
“significant” with $p$-values between 0.01 and 0.05 by stepwise variable
selection, only 49% actually were true risk factors. Various solutions
have been proposed to counter such *model optimism*. A popular procedure
is bootstrapping the model as developed in @SAUERBREI1992 and
@HARRELL2001. Although @AUSTIN2008 found it ineffective to identify true
predictors, this method has often been found to work well for developing
predictive models. The method randomly draws multiple samples with
replacement from the observed sample, thus mimicking the sampling
variation in the population from which the sample was drawn. Stepwise
regression analyses are replayed in each bootstrap sample. The
proportion of times that each prognostic variable is retained in the
stepwise regression model is known as the *inclusion frequency*
[@SAUERBREI1992]. This proportion provides information about the
strength of the evidence that an indicator is an independent predictor.
In addition, each bootstrap model can be fitted to the original sample.
The difference between the apparent performance and the bootstrap
performance provides the basis for performance measures that correct for
model optimism. @STEYERBERG2009 [p. 95] provides an easy-to-follow
procedure to calculate such *optimism-corrected performance* measures.

Clearly, the presence of missing data adds uncertainty to the model
building process, so optimism can be expected to be more severe with
missing data. It is not yet clear what the best way is to estimate
optimism from incomplete data. @HEYMANS2007 explored the combination of
multiple imputation and the bootstrap. There appear to be at least four
general procedures:

1.  *Imputation*. Multiple imputation generates 100 imputed datasets.
    Automatic backward selection is applied to each dataset. Any
    differences found between the 100 fitted models are due to the
    missing data.

2.  *Bootstrap*. 200 bootstrap samples are drawn from one singly imputed
    completed data. Automatic backward selection is applied to
    each dataset. Any differences found between the 200 fitted models
    are due to sampling variation.

3.  *Nested bootstrap*. The bootstrap method is applied on each of the
    multiply imputed datasets. Automatic backward selection is applied
    to each of the $100 \times 200$ datasets. Differences between the
    fitted model portray both sampling and missing data uncertainty.

4.  *Nested imputation*. The imputation method is applied on each of the
    bootstrapped datasets.

@HEYMANS2007 observed that the imputation method produced a wider range
of inclusion frequencies than the bootstrap method. This is attractive
since a better separation of strong and weak predictors may ease model
building. The area under the curve is an overall index of predictive
strength. Though the type of method had a substantial effect on the
apparent $c$-index estimate, the optimism-corrected $c$-index estimate
was quite similar. The optimism-corrected calibration slope estimates
tended to be lower in the methods involving imputation, thus
necessitating more shrinkage.

A drawback of the method is the use of classic stepwise variable
selection techniques, which do not generalize well to high-dimensional
data. @MUSORO2014 improved the methods of @HEYMANS2007 through their use
of the LASSO.

@LONG2015 developed a procedure, called bootstrap imputation and
stability selection (BI-SS) , that generates bootstrap samples from the
original data, imputes each bootstrap sample by single imputation,
obtains the randomized LASSO estimate from each sample, and then selects
the active set according to majority. The multiple imputation random
LASSO (MIRL) method by @LIU2016 first performs multiple imputation,
obtains bootstrap samples from each imputed dataset, estimates
regression weights under LASSO, and then selects the active set by
majority. It is not yet known how BS-SS and MIRL compare to each other.

## Parallel computation

Multiple imputation is a parallel technique. If there are $m$ processors
available, it is possible to generate the $m$ imputed datasets, estimate
the $m$ complete-data statistics and store the $m$ results by $m$
independent parallel streams. The overhead needed is minimal since each
stream requires the same amount of processor time. If more than $m$
processors are available, a better alternative is to subdivide each
stream into several substreams. Huge savings in execution time can be
obtained in this way [@BEDDO2002].

Unfortunately, `R` is single-threaded, so the
exploitation of the parallel nature of multiple imputation is not
automatic, and requires some additional work. There are currently three
alternatives to perform the calculation of
`mice` in a parallel fashion.

1.  @GORDON2014 presents a fully worked out example code that builds
    upon the `doParallel` library, and that combines `complete()` and
    `ibind()`. With some programming this example can be adapted 
    to other datasets.

2.  The `parlMICE()` function is a wrapper around `mice()` that can
    divide the imputations over multiple cores or CPUs. 
    @SCHOUTEN2017 show that substantial gains are already possible 
    with three free cores, especially for a combination of a large 
    number of imputations $m$ and a large sample size $n$.

3.  The `par.mice()` function in the `micemd` package [@MICEMD] takes 
    the same arguments as the `mice()` function, plus two extra arguments
    related to the parallel calculations. It also builds on the 
    `parallel` package.

The last two options are quite similar. Application of these methods is
especially beneficial for simulation studies, where the same model needs
to be replicated a large number of times. Support for multi-core
processing is likely to grow, so keep an eye on the Internet.

## Conclusion

The statistical analysis of the multiply imputed data involved repeated
analysis followed by parameter pooling. Rubin’s rules apply to a wide
variety of quantities, especially if these quantities are transformed
toward normality. Dedicated statistical tests and model selection
technique are now available. Although many techniques for complete data
now have their analogues for incomplete data, the present
state-of-the-art does not cover all. As multiple imputation becomes more
familiar and more routine, we will see new post-imputation methodology
that will be progressively more refined.

## Exercises {#ex:ch:analysis}

@ALLISON1976 investigated the interrelationship between sleep,
ecological and constitutional variables. They assessed these variables
for 39 mammalian species. The authors concluded that slow-wave sleep is
negatively associated with a factor related to body size. This suggests
that large amounts of this sleep phase are disadvantageous in large
species. Also, paradoxical sleep was associated with a factor related to
predatory danger, suggesting that large amounts of this sleep phase are
disadvantageous in prey species.

@ALLISON1976 performed their analyses under complete-case analysis. In
this exercise we will recompute the regression equations for slow wave
(“nondreaming”) sleep (hrs/day) and paradoxical (“dreaming”) sleep
(hrs/day), as reported by the authors. Furthermore, we will evaluate the
imputations.

```{exercise, name = "Complete-case analysis", label = "completecase"}
Compute the regression equations (1) and (2) from the paper 
of @ALLISON1976 under complete-case analysis.

```

```{exercise, name = "Imputation", label = "imputation"}
The `mammalsleep` data are part of the `mice` package.
Impute the data with `mice()` under all the default settings. 
Recalculate the regression equations (1) and (2) on the 
multiply imputed data.

```

```{exercise, name = "Traces", label = "traces"}
Inspect the trace plot of the MICE algorithm. Does the algorithm 
appear to converge?

```

```{exercise, name = "More iterations", label = "moreiterations"}
Extend the analysis with 20 extra iterations using 
`mice.mids()`. Does this affect your conclusion about convergence?

```

```{exercise, name = "Distributions", label = "distributions"}
Inspect the data with diagnostic plots for univariate data. 
Are the univariate distributions of the observed and 
imputed data similar? Can you explain why they do 
(or do not) differ?

```

```{exercise, name = "Relations", label = "relations"}
Inspect the data with diagnostic plots for the most interesting 
bivariate relations. Are the relations similar in the observed
and imputed data? Can you explain why they do (or do not) differ?

```

```{exercise, name = "Defaults", label = "defaults"}
Consider each of the seven default choices from Section
\@ref(sec:choices) in turn. Do you think the default is 
appropriate for your data? Explain why.

```

```{exercise, name = "Improvement", label = "improvement"}
Do you have particular suggestions for improvement? Which? 
Implement one (or more) of your suggestions. Do the results
now look more plausible or realistic? Explain. What happened 
to the regression equations?

```

```{exercise, name = "Multivariate analyses", label = "multivariate"}
Repeat the factor analysis and the stepwise regression. 
Beware: There might be pooling problems.

```
