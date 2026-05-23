---
citekey: andersonIntroductionMultivariateStatistical2003
item_type: book
authors: 'Anderson, T. W.'
year: 2003
title: An Introduction to Multivariate Statistical Analysis
publisher: Wiley-Interscience
isbn: 978-0-471-36091-9
series: Wiley Series in Probability and Statistics
edition: 3rd ed
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\anderson_introduction_multivariate_statistical_2003.pdf'
pdf_sha256: 3bdbf6faaf7fe098e9113ae0fc06d60d62d60d391db9d5c9de74f64e9ac8aaae
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T23:01:52Z
---
# An Introduction to Multivariate Statistical Analysis 

Third Edition

T. W. ANDERSON<br>Stanford University<br>Department of Statistics<br>Stanford, CA

Copyright © 2003 by John Wiley \& Sons, Inc. All rights reserved.
Published by John Wiley \& Sons, Inc. Hoboken, New Jersey Published simultaneously in Canarla,

No part of this publication may be reproduced, stored in a retrieval system or transmitted in any form or by any me'ns, electronic, mechanical, photocopying, recording, scanning or otherwise, except as penmitted under Section 107 or 108 ol the 1976 United States Copyright Act, without ejther the prior writ'en permission of the Publisher, or at thorization through payment of the appropriate per-copy fee to the Copyright Clearance Center, Inc., 222 Rosewood Drive, Damvers, MA 01923, 978-750-8400, fax 978-750-4470, or on the web at www.copyright.com. Requests to the $2^{2}$ ublisher for permission should be addressed to the Permissions Department, John Wiley \& Sons, Inc., 111 River Street, Hoboken, NJ 07030, (201) 748-6011, fax (201) 748-6008, e-mail: permreq@wiley.com.

Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best efforts in preparing this book, they make no representations or warranties with respect to the accuracy or completeness of the contents of this book and specifically disclaim any implied warranties of merchantability or fitness for a particular purpose. No warranty may be created or extended by sales representatives or written sales materials. The advice and strategies contained herein may not be suitable for your situation. You should consult with a professional where appropriate. Neither the publisher nor author shall be liable for any loss of profit or any other commercial damages, including but not limited to special, incidental, consequential, or other damages.

For general information on our other products and services please contact our Customer Care Department within the U.S. at 877-762-2974, outside the U.S. at 317-572-3993 or fax 317-572-4002.

Wiley also publishes its books in a variety of electronic formats. Some content that appears in print, however, may not be available in electronic format.

## Library of Congress Cataloging-in-Publication Data

Anderson, T. W. (Theodore Wilbur), 1918-
An introduction to multivariate statistical analysis / Theodore W. Anderson.--3rd ed. p. cm.-- (Wiley series in probability and mathematical statistics)

Includes hihliographical references and index.
ISBN 0-471-36091-0 (cloth : acid-free paper)

1. Multivariate analysis. I. Title. II. Series.

QA278.A516 2003
519.5'35--dc21

2002034317

Printed in the United States of America

To
DOROTHY

## Contents

Preface to the Third Edition ..... XV
Preface to the Second Edition ..... xvii
Preface to the First Edition ..... xix
1 Introduction ..... 1
1.1. Multivariate Statistical Analysis, ..... 1
1.2. The Multivariate Normal Distribution, ..... 3
2 The Multivariate Normal Distribution ..... 6
2.1. Introduction, ..... 6
2.2. Notions of Multivariate Distributions, ..... 7
2.3. The Multivariate Normal Distribution, ..... 13
2.4. The Distribution of Linear Combinations of Normally Distributed Variates; Independence of Variates; Marginal Distributions, ..... 23
2.5. Conditional Distributions and Multiple Correlation Coefficient, ..... 33
2.6. The Characteristic Function; Moments, ..... 41
2.7. Flliptically Contoured Distributions, ..... 47
Problems, ..... 56
3 Estimation of the Mean Vector and the Covariance Matrix ..... 66
3.1. Introduction, ..... 66
3.2. The Maximum Likelihood Estimators of the Mean Vector and the Covariance Matrix, ..... 67
3.3. The Distribution of the Sample Mean Vector; Inference Concerning the Mean When the Covariance Matrix Is Known, ..... 74
3.4. Theoretical Properties of Estimators of the Mean Vector, ..... 83
3.5. Improved Estimation of the Mean, ..... 91
3.6. Elliptically Contoured Distributions, ..... 101
Problems, ..... 108
4 The Distributions and Uses of Sample Correlation Coefficients ..... 115
4.1. Introduction, ..... 115
4.2. Correlation Coclicient of a Bivariate Sample, ..... 116
4.3. Partial Correlation Coefficients; Conditional Distributions, ..... 136
4.4. The Multiple Correlation Coefficient, ..... 144
4.5. Elliptically Contoured Distributions, ..... 158
Problems, ..... 163
5 The Generalized $T^{2}$-Statistic ..... 170
5.1. Introduction, ..... 170
5.2. Derivation of the Generalized $T^{2}$-Statistic and Its Distribution, ..... 171
5.3. Uses of the $T^{2}$-Statistic, ..... 177
5.4. The Distribution of $T^{2}$ under Alternative Hypotheses; The Power Function, ..... 185
5.5. The Two-Sample Problem with Unequal Covariance Matrices, ..... 187
5.6. Some Optimal Properties of the $T^{2}$-Test, ..... 190
5.7. Elliptically Contoured Distributions, ..... 199
Problems, ..... 201
6 Classification of Observations ..... 207
6.1. The Problem of Classification, ..... 207
6.2. Standards of Good Classification, ..... 208
6.3. Proccdures of Classification into One of Two Populations with Known Probability Distributions, ..... 211
6.4. Classification into One of Two Known Multivariate Normal Populations, ..... 215
6.5. Classification into One of Two Multivariate Normal Populations When the Parameters Are Estimated, ..... 219
6.6. Probabilities of Misclassification, ..... 227
6.7. Classification into One of Several Populations, ..... 233
6.8. Classification into One of Several Multivariate Normal Populations, ..... 237
6.9. An Example of Classification into One of Several Multivariate Normal Populations, ..... 240
6.10. Classification into One of Two Known Multivariate Normal Populations with Unequal Covariance Matrices, ..... 242
Problems, ..... 248
7 The Distribution of the Sample Covariance Matrix and the Sample Generalized Variance ..... 251
7.1. Introduction, ..... 251
7.2. The Wishart Distribution, ..... 252
7.3 Some Properties of the Wishart Distribution, ..... 258
7.4. Cochran's Theorem, ..... 262
7.5. The Generalized Variance, ..... 264
7.6. Distribution of the Set of Correlation Coefficients When the Population Covariance Matrix Is Diagonal, ..... 270
7.7. The Inverted Wishart Distribution and Bayes Estimation of the Covariance Matrix, ..... 272
7.8. Improved Estimation of the Covariance Matrix, ..... 276
7.9. Elliptically Contoured Distributions, ..... 282
Problems, ..... 285
8 Testing the General Linear Hypothesis; Multivariate Analysis of Variance ..... 291
8.1. Introduction, ..... 291
8.2. Estimators of Parameters in Multivariate Linear Regiession, ..... 292
8.3. Likelihood Ratio Criteria for Testing Linear Hypotheses about Regression Coefficients, ..... 298
8.4. The Distribution of the Likelihood Ratio Criterion When the Hypothesis Is True, ..... 304
8.5. An Asymptotic Expansion of the Distribution of the Likelihood Ratio Criterion, ..... 316
8.6. Other Criteria for Testing the Linear Hypothesis, ..... 326
8.7. Tests of Hypotheses about Matrices of Regression Coefficients and Confidence Regions, ..... 337
8.8. Testing Equality of Means of Several Normal Distributions with Common Covariance Matrix, ..... 342
8.9. Multivariate Analysis of Variance, ..... 346
8.10. Some Optimal Properties of Tests, ..... 353
S.11. Elliptically Contoured Distributions, ..... 370
Problems, ..... 374
9 Testing Independence of Sets of Variates ..... 381
9.1. Imtroductiom, ..... 381
9. 2. Whe Likelihood Ratio Criterion for Testing Independence of Sets of Variates, ..... 381
9.3. Ihe Distribution of the Likelihood Ratio Criterion When the Null Hypothesis Is True, ..... 386
9.4. An Asymptotic Expansion of the Distribution of the Likelihood Ratio Criterion, ..... 390
9.5. Other Criteria, ..... 391
9.6. Step-Down Procedures, ..... 393
9.7. An Example, ..... 396
9.8. The Case of Two Sets of Variates, ..... 397
9.9. Admissibility of the Likelihood Ratio Test, ..... 401
9.10. Monotonicity of Power Functions of Tests of Independence of Sets, ..... 402
9.11. Elliptically Contoured Distributions, ..... 404
Problems, ..... 408
10 Testing Hypotheses of Equality of Covariance Matrices and Equality of Mean Vectors and Covariance Matrices
10.1. Introduction, ..... 411
10.2. Criteria for Testing Equality of Several Covariance Matrices, ..... 412
10.3. Criteria for Testing That Several Normal Distributions Are Identical, ..... 415
10.4. Distributions of the Criteria, ..... 417
10.5. Asymptotic Expansions of the Distributions of the Criteria, ..... 424
10.6. The Case of Two Populations, ..... 427
10.7. Testing the Hypothesis That a Covariance Matrix Is Proportional to a Given Matrrix; The Sphericity Test, ..... 431
10.8. Testing the Hypothesis That a Covariance Matrix Is Equal to a Given Matrix, ..... 438
10.9. Testing the Hypothesis That a Mean Vector and a Covariance Matrix Are Equal to a Given Vector and Matrix, ..... 444
10.10. Admissibility of Tests, ..... 446
10.11. Elliptically Contoured Distributions, ..... 449
Problems, ..... 454
11 Principal Components ..... 459
11.1. Introduction, ..... 459
11.2. Definition of Principal Components in the Population, ..... 460
11.3. Maximum Likelihood Estimators of the Principal Components and Their Variances, ..... 467
11.4. Computation of the Maximum Likelihood Estimates of the Principal Components, ..... 469
11.5. An Example, ..... 471
11.6. Statistical Inference, ..... 473
11.7. Testing Hypotheses about the Characteristic Roots of a Covariance Matrix, ..... 478
11.8. Elliptically Contoured Distributions, ..... 482
Problems, ..... 483
12 Canonical Correlations and Canonical Variables ..... 487
12.1. Introduction, ..... 487
12.2. Canonical Correlations and Variates in the Population, ..... 488
12.3. Estimation of Canonical Correlations and Variates, ..... 498
12.4. Statistical Inference, ..... 503
12.5. An Example, ..... 505
12.6. Linearly Related Expected Values, ..... 508
12.7. Reduced Rank Regression, ..... 514
12.8. Simultaneous Equations Models, ..... 515
Problems, ..... 526
13 The Distributions of Characteristic Roots and Vectors ..... 528
13.1. Introduction, ..... 528
13.2. The Case of Two Wishart Matrices, ..... 529
13.3. The Case of One Nonsingular Wishart Matrix, ..... 538
13.4. Canonical Correlations, ..... 543
13.5. Asymptotic Distributions in the Case of One Wishart Matrix, ..... 545
13.6. Asymptotic Distributions in the Case of Two Wishart Matrices, ..... 549
13.7. Asymptotic Distribution in a Regression Model, ..... 555
13.8. Elliptically Contoured Distributions, ..... 563
Problems, ..... 567
14 Factor Analysis
14.1. Introduction, ..... 569
14.2. The Model, ..... 570
14.3. Maximum Likelihood Estimators for Random Oithogonal Factors, ..... 576
14.4. Estimation for Fixed Factors, ..... 586
14.5. Factor Interpretation and Transformation, ..... 587
14.6. Estimation for Identification by Specified Zeros, ..... 590
14.7. Estimation of Factor Scores, ..... 591
Problems, ..... 593
15 Patterns of Dependence; Graphical Models ..... 595
15.1. Introduction, ..... 595
15.2. Undirected Graphs, ..... 596
15.3. Directed Graphs, ..... 604
15.4. Chain Graphs, ..... 610
15.5. Statistical Inference, ..... 613
Appendix A Matrix Theory ..... 624
A.1. Definition of a Matrix and Operations on Matrices, ..... 624
A.2. Characteristic Roots and Vectors, ..... 631



A.3. Partitioned Vectors and Matrices, ..... 635
A.4. Some Miscellaneous Results, ..... 639
A.5. Gram-Schmidt Orthogonalization and the Solntion of Linear Equations, ..... 647
Appendix B Tables ..... 651
B.1. Wilks' Likelihood Criterion: Factors $C(p, m, M)$ to Adjust to $X_{p, m}^{2}$, where $M=n-p+1$, ..... 651
B.2. Tables of Significance Points for the Lawley-Hotelling Trace Test, ..... 657
B.3. Tables of Significance Points for the Bartlett-Nanda-Pillai Trace Test, ..... 673
B.4. Tables of Significance Points for the Roy Maximum Root Test, ..... 677
B.5. Significance Points for the Modified Likelihood Ratio Test of Equality of Covariance Matrices Based on Equal Sample Sizes, ..... 681
B.6. Correction Factors for Significance Points for the Sphericity Test, ..... 683
B.7. Significance Points for the Modified Likelihood Ratio Test $\mathbf{\Sigma}=\mathbf{\Sigma}_{0}$, ..... 685
References ..... 687
Index ..... 713
"

## Preface to the Third Edition

For some forty years the first and second editions of this book have been used by students to acquire a basic knowledge of the theory and methods of multivariate statistical analysis. The book has also served a wider community of statisticians in furthering their understanding and proficiency in this field. Since the second edition was published, multivariate analysis has been developed and extended in many directions. Rather than attempting to cover, or even survey, the enlarged scope, I have elected to elucidate several aspects that are particularly interesting and useful for methodology and comprehension.

Earlier editions included some methods that could be carried out on an adding machine! In the twenty-first century, however, computational techniques have become so highly developed and improvements come so rapidly that it is impossible to include all of the relevant methods in a volume on the general mathematical theory. Some aspects of statistics exploit computational power such as the resampling technologies; these are not covered here.

The definition of multivariate statistics implies the treatment of variables that are interrelated. Several cliapters are devoted to measures of correlation and tests of independence. A new chapter, "Patterns of Dependence; Graphical Models" has been added. A so-called graphical model is a set of vertices or nodes identifying observed variables together with a new set of edges suggesting dependences between variables. The algebra of such graphs is an outgrowth and development of path analysis and the study of causal chains. A graph may represent a sequence in time or logic and may suggest causation of one set of variables by another set.

Another new topic systematically presented in the third edition is that of elliptically contoured distributions. The multivariate normal distribution, which is characterized by the mean vector and covariance matrix, has a limitation that the fourth-order moments of the variables are determined by the first- and second-order moments. The class of elliptically contoured
distribution relaxes this restriction. A density in this class has contours of equal density which are ellipsoids as does a normal density, but the set of fourth-order moments has one further degree of freedom. This topic is expounded by the addition of sections to appropriate chapters.

Reduced rank regression developed in Chapters 12 and 13 provides a method of reducing the number of regression coefficients to be estimated in the regression of one set of variables to another. This approach includes the limited-information maximum-likelihood estimator of an equation in a simultaneous equations model.

The preparation of the third edition has been benefited by advice and comments of readers of the first and second editions as well as by reviewers of the current revision. In addition to readers of the earlier editions listed in those prefaces I want to thank Michael Perlman and Kathy Richards for their assistance in getting this manuscript ready.

T. W. Anderson

Stanford, California
February 2003

## Preface to the Second Edition

Twenty-six years have passed since the first edition of this book was published. During that time great advances have been made in multivariate statistical analysis-particularly in the areas treated in that volume. This new edition purports to bring the original edition up to date by substantial revision, rewriting, and additions. The basic approach has been maintained, namely, a mathematically rigorous development of statistical methods for observations consisting of several measurements or characteristics of each subject and a study of their properties. The general outline of topics has been retained.

The method of maximum likelihood has been augmented by other considerations. In point estimation of the mean vector and covariance matrix alternatives to the maximum likelihood estimators that are better with respect to certain loss functions, such as Stein and Bayes estimators, have been introduced. In testing hypotheses likelihood ratio tests have been supplemented by other invariant procedures. New results on distributions and asymptotic distributions are given; some significant points are tabulated. Properties of these procedures, such as power functions, admissibility, unbiasedness, and monotonicity of power functions, are studied. Simultaneous confidence intervals for means and covariances are developed. A chapter on factor analysis replaces the chapter sketching miscellaneous results in the first edition. Some new topics, including simultaneous equations models and linear functional relationships, are introduced. Additional problems present further results.

It is impossible to cover all relevant material in this book; what seems most important has been included. For a comprehensive listing of papers until 1966 and books until 1970 the reader is referred to A Bibliography of Multivariate Statistical Analysis by Anderson, Das Gupta, and Styan (1972). Further references can be found in Multivariate Analysis: A Selected and

Abstracted Bibliography, 1957-1972 by Subrahmaniam and Subrahmaniam (1973).

I am in debt to many students, colleagues, and friends for their suggestions and assistance; they include Yasuo Amemiya, James Berger, Byoung-Seon Choi. Arthur Cohen, Margery Cruise, Somesh Das Gupta, Kai-Tai Fang, Gene Golub, Aaron Han, Takeshi Hayakawa, Jogi Henna, Huang Hsu, Fred Huffer, Mituaki Huzii, Jack Kiefer, Mark Knowles, Sue Leurgans, Alex McMillan, Masashi No, Ingram Olkin, Kartik Patel, Michael Perlman, Allen Sampson, Ashis Sen Gupta, Andrew Siegel, Charles Stein, Patrick Strout, Akimichi Takemura, Joe Verducci, Marlos Viana, and Y. Yajima. I was helped in preparing the manuscript by Dorothy Anderson, Alice Lundin, Amy Schwartz, and Pat Struse. Special thanks go to Johanne Thiffault and George P. H. Styan for their precise attention. Support was contributed by the Army Research Office, the National Science Foundation, the Office of Naval Research, and IBM Systems Research Institute.

Seven tables of significance points are given in Appendix B to facilitate carrying out test procedures. Tables 1, 5, and 7 are Tables 47, 50, and 53, respectively, of Biometrika Tables for Statisticians, Vol. 2, by E. S. Pearson and H. O. Hartley; permission of the Biometrika Trustees is hereby acknowledged. Table 2 is made up from three tables prepared by A. W. Davis and published in Biometrika (1970a), Annals of the Institute of Statistical Mathematics (1970b) and Communications in Statistics, B. Simulation and Computation (1980). Tables 3 and 4 are Tables 6.3 and 6.4, respectively, of Concise Statistical Tables, edited by Ziro Yamauti (1977) and published by the Japanese Standards Association; this book is a concise version of Statistical Tables and Formulas with Computer Applications, JSA-1972. Table 6 is Table 3 of The Distribution of the Sphericity Test Criterion, ARL 72-0154, by B. N. Nagarsenker and K. C. S. Pillai, Acrospace Rescarch Laboratorics (1972). The author is indebted to the authors and publishers listed above for permission to reproduce these tables.

T. W. Anderson

Slanford. California
June 1984

## Preface to the First Edition

This book has been designed primarily as a text for a two-semester course in multivariate statistics. It is hoped that the book will also serve as an introduction to many topics in this area to statisticians who are not students and will be used as a reference by other statisticians.

For several years the book in the form of dittoed notes has been used in a two-semester sequence of graduate courses at Columbia University; the first six chapters constituted the text for the first semester, emphasizing correlation theory. It is assumed that the reader is familiar with the usual theory of univariate statistics, particularly methods based on the univariate normal distribution. A knowledge of matrix algebra is also a prerequisite; however, an appendix on this topic has been included.

It is hoped that the more basic and important topics are treated here, though to some extent the coverage is a matter of taste. Some of the more recent and advanced developments are only briefly touched on in the late chapter.

The method of maximum likelihood is used to a large extent. This leads to reasonable procedures; in some cases it can be proved that they are optimal. In many situations, however, the theory of desirable or optimum procedures is lacking.

Over the years this manuscript has been developed, a number of students and colleagues have been of considerable assistance. Allan Birnbaum, Harold Hotelling, Jacob Horowitz, Howard Levene, Ingram Olkin, Gobind Seth, Charles Stein, and Henry Teicher are to be mentioned particularly. Acknowledgements are also due to other members of the Graduate Mathematical

Statistics Society at Columbia University for aid in the preparation of the manuscript in dittoed form. The preparation of this manuscript was supported in part by the Office of Naval Research.

T. W. Anderson

Center for Advanced Study in the Behavioral Sciences
Stanford, Califomia
December 1957

## CHAPTER 1

## Introduction

### 1.1. MULTIVARIATE STATISTICAL ANALYSIS

Multivariate statistical analysis is concerned with data that consist of sets of measurements on a number of individuals or objects. The sample data may be heights and weights of some individuals drawn randomly from a population of school children in a given city, or the statistical treatment may be made on a collection of measurements, such as lengths and widths of petals and lengths and widths of sepals of iris plants taken from two species, or one may study the scores on batteries of mental tests administered to a number of students.

The measurements made on a single individual can be assembled into a column vector. We think of the entire vector as an observation from a multivariate population or distribution. When the individual is drawn randomly, we consider the vector as a random vector with a distribution or probability law describing that population. The set of observations on all individuals in a sample constitutes a sample of vectors, and the vectors set side by side make up the matrix of observations. ${ }^{\dagger}$ The data to be analyzed then are thought of as displayed in a matrix or in several matrices.

We shall see that it is helpful in visualizing the data and understanding the methods to think of each observation vector as constituting a point in a Euclidean space, each coordinate corresponding to a measurement or variable. Indeed, an early step in the statistical analysis is plotting the data; since

[^0]An Introduction to Multivanate Statistical Analysis, Third Edition. By T. W. Anderson ISBN 0-471-36091-0 Copyright © 2003 John Wiley \& Sons, Inc.
most statisticians are limited to two-dimensional plots, two coordinates of the observation are plotted in turn.

Characteristics of a univariate distribution of essential interest are the mean as a measure of location and the standard deviation as a measure of variability; similarly the mean and standard deviation of a univariate sample are important summary measures. In multivariate analysis, the means and variances of the separate measurements-for distributions and for samples -have corresponding relevance. An essential aspect, however, of multivariate analysis is the dependence between the different variables. The dependence between two variables may involve the covariance between them, that is, the average products of their deviations from their respective means. The covariance standardized by the corresponding standard deviations is the correlation coefficient; it serves as a measure of degree of dependence. A set of summary statistics is the mean vector (consisting of the univariate means) and the covariance matrix (consisting of the univariate variances and bivariate covariances). An alternative set of summary statistics with the same information is the mean vector, the set of standard deviations, and the correlation matrix. Similar parameter quantities describe location, variability, and dependence in the population or for a probability distribution. The multivariate normal distribution is completely determined by its mean vector and covariance matrix, and the sample mean vector and covariance matrix constitute a sufficient set of statistics.

The measurement and analysis of dependence between variables, between sets of variables, and between variables and sets of variables are fundamental to multivariate analysis. The multiple correlation coefficient is an extension of the notion of correlation to the relationship of one variable to a set of variables. The partial correlation coefficient is a measure of dependence between two variables when the effects of other correlated variables have been removed. The various correlation coefficients computed from samples are used to estimate corresponding correlation coefficients of distributions. In this book tests of hypotheses of independence are developed. The properties of the estimators and test procedures are studied for sampling from the multivariate normal distribution.

A number of statistical problems arising in multivariate populations are straightforward analogs of problems arising in univariate populations; the suitable methods for handling these problems are similarly related. For example, in the univariate case we may wish to test the hypothesis that the mean of a variable is zero; in the multivariate case we may wish to test the hypothesis that the vector of the means of several variables is the zero vector. The analog of the Student $t$-test for the first hypothesis is the generalized $T^{2}$-test. The analysis of variance of a single variable is adapted to vector


[^0]:    ${ }^{\dagger}$ When data are listed on paper by individual, it is natural to print the measurements on one individual as a row of the table; then one individual corresponds to a row vector. Since we prefer to operate algebraically with column vectors, we have chosen to treat observations in terms of column vectors. (In practice, the basic data set may well be on cards, tapes, or disks.)



observations; in regression analysis, the dependent quantity may be a vector variable. A comparison of variances is generalized into a comparison of covariance matrices.

The test procedures of univariate statistics are generalized to the multivariate case in such ways that the dependence between variables is taken into account. These methods may not depend on the coordinate system; that is, the procedures may be invariant with respect to linear transformations that leave the null hypothesis invariant. In some problems there may be families of tests that are invariant; then choices must be made. Optimal properties of the tests are considered.

For some other purposes, however, it may be important to select a coordinate system so that the variates have desired statistical properties. One might say that they involve characterizations of inherent properties of normal distributions and of samples. These are closely related to the algebraic problems of canonical forms of matrices. An example is finding the normalized linear combination of variables with maximum or minimum variance (finding principal components); this amounts to finding a rotation of axes that carries the covariance matrix to diagonal form. Another example is characterizing the dependence between two sets of variates (finding canonical correlatious). These problems involve the characteristic roots and vectors of various matrices. The statistical properties of the corresponding sample quantities are treated.

Some statistical problems arise in models in which means and covariances are restricted. Factor analysis may be based on a model with a (population) covariance matrix that is the sum of a positive definite diagonal matrix and a positive semidefinite matrix of low rank; linear structural relationships may have a similar formulation. The simultaneous equations system of econometrics is another example of a special model.

### 1.2. THE MULTIVARIATE NORMAL DISTRIBUTION

The statistical methods treated in this book can be developed and evaluated in the context of the multivariate normal distribution, though many of the procedures are useful and effective when the distribution sampled is not normal. A major reason for basing statistical analysis on the normal distribution is that this probabilistic model approximates well the distribution of continuous measurements in many sampled populations. In fact, most of the methods and theory have been developed to serve statistical analysis of data. Mathematicians such as Adrian (1808), Laplace (1811), Plana (1813), Gauss
(1823), and Bravais (1846) studicd the bivariate normal density. Francis Galton, the geneticist, introduced the ideas of correlation, regression, and homoscedasticity in the study of pairs of measurements, one made on a parent and one in an offspring. [See, e.g., Galton (1889).] He enunciated the theory of the multivariate normal distribution as a generalization of observed properties of samples.

Karl Pearson and others carried on the development of the theory and use of different kinds of correlation coefficients ${ }^{\dagger}$ for studying proble.ns in genetics, biology, and other fields. R. A. Fisher further developed methods for agriculture, botany, and anthropology, including the discriminant function for classification problems. In another direction, analysis of scores or mental tests led to a theory, including factor analysis, the sampling theory of which is based on the normal distribution. In these cases, as well as in agricultural experiments, in engineering problems, in certain economic problems, and in other fields, the multivariate normal distributions have been found to be sufficiently close approximations to the populations so that statistical analyses based on these models are justified.

The univariate normal distribution arises frequently because the effect studied is the sum of many independent random effects. Similarly, the multivariate normal distribution often occurs because the multiple measurements are sums of small independent effects. Just as the central limit theorem leads to the univariate normal distrioution for single variables, so does the general central limit theorem for several varjables lead to the multivariate normal distribution.

Statistical theory based on the normal distribution has the advantage that the multivariate methods based on it are extensively developed and can be studied in an organized and systematic way. This is due not only to the need for such methods because they are of practical usi, but also to the fact that normal theory is amenable to exact mathematical treatment. The suitable methods of analysis are mainly based on standard operations of matrix algebra; the distributions of many statistics involved can be obtained exactly or at least characterized; and in many cases optimum properties of procedures can be deduced.

The point of view in this book is to state problems of inference in terms of the multivariate normal distributions, develop efficient and often optimum methods in this context, and evaluate significance and confidence levels in these terms. This approach gives coherence and rigor to the exposition, but, by its very nature, cannot exhaust consideration of multivariate statistical analysis. The procedures are appropriate to many nonnormal distributions,

[^0]but their adequacy may be open to question. Roughly speaking, inferences about means are robust because of the operation of the central limit theorem, but inferences about covariances are sensitive to normality, the variability of sample covariances depending on fourth-order moments.

This inflexibility of normal methods with respect to moments of order greater than two can be reduced by including a larger class of elliptically contoured distributions. In the univariate case the normal distribution is determined by the mean and variance; higher-order moments and properties such as peakedness and long tails are functions of the mean and variance. Similarly, in the multivariate case the means and covariances or the means, variances, and correlations determine all of the properties of the distribution. That limitation is alleviated in one respect by consideration of a broad class of elliptically contoured distributions. That class maintains the dependence structure, but permits more general peakedness and long tails. This study leads to more robust methods.

The development of computer technology has revolutionized multivariate statistics in several respects. As in univariate statistics, modern computers permit the evaluation of observed variability and significance of results by resampling methods, such as the bootsirap and cross-validation. Such methodology reduces the reliance on tables of significance points as well as eliminates some restrictions of the normal distribution.

Nonparametric techniques are available when nothing is known about the underlying distributions. Space does not permit inclusion of these topics as well as other considerations of data analysis, such as treatment of outliers and transformations of variables to approximate normality and homoscedasticity.

The availability of modern computer facilities makes possible the analysis of large data sets and that ability permits the application of multivariate methods to new areas, such as image analysis, and more effective analysis of data, such as meteorological. Moreover, new problems of statistical analysis arise, such as sparseness of parameter or data matrices. Because hardware and software development is so explosive and programs require specialized knowledge, we are content to make a few remarks here and there about computation. Packages of statistical programs are available for most of the methods.

## The Multivariate Normal Distribution

### 2.1. INTRODUCTION

In this chapter we discuss the multivariate normal distribution and some of its properties. In Section 2.2 are considered the fundamental notions of multivariate distributions: the definition by means of multivariate density functions, marginal distributions, conditional distributions, expected values, and moments. In Section 2.3 the multivariate normal distribution is defined; the parameters are shown to be the means, variances, and covariances or the means, variances, and correlations of the components of the random vector. In Section 2.4 it is shown that linear combinations of normal variables are normally distributed and hence that marginal distributions are normal. In Section 2.5 we see that conditional distributions are also normal with means that are linear functions of the conditioning variables; the coefficients are regression coefficients. The variances, covariances, and correlations-called partial correlations-are constants. The multiple correlation coefficient is the maximum correlation between a scalar random variable and linear combination of other random variables; it is a measure of association between one variable and a set of others. The fact that marginal and conditional distributions of normal distributions are normal makes the treatment of this family of distributions coherent. In Section 2.6 the characteristic function, moments, and cumulants are discussed. In Section 2.7 elliptically contoured distributions are defined; the properties of the normal distribution are extended to this larger class of distributions.

[^1]
### 2.2. NOTIONS OF MULTIVARIATE DISTRIBUTIONS

### 2.2.1. Joint Distributions

In this section we shall consider the notions of joint distributions of several variables, derived marginal distributions of subsets of variables, and derived conditional distributions. First consider the case of two (real) random variables ${ }^{\dagger} X$ and $Y$. Probabilities of events defined in terms of these variables can be obtained by operations involving the cumulative distribution function (abbreviated as cdf),

$$
F(x, y)=\operatorname{Pr}\{X \leq x, Y \leq y\}
$$

defined for every pair of real numbers $(x, y)$. We are interested in cases where $F(x, y)$ is absolutely continuous; this means that the following partial derivative exists almost everywhere:

$$
\frac{\partial^{2} F(x, y)}{\partial \because \partial y}=f(x, y)
$$

and

$$
F(x, y)=\int_{-\infty}^{y} \int_{-\infty}^{x} f(u, v) d u d v
$$

The nonnegative function $f(x, y)$ is called the density of $X$ and $Y$. The pair of random variables ( $X, Y$ ) defines a random point in a plane. The probability that ( $X, Y$ ) falls in a rectangle is

$$
\begin{aligned}
& \operatorname{Pr}\{x \leq X \leq x+\Delta x, y \leq Y \leq y+\Delta y\} \\
& \quad:=F(x+\Delta x, y+\Delta y)-F(x+\Delta x, y)-F(x, y+\Delta y)+F(x, y) \\
& \quad=\int_{y}^{y+\Delta y} \int_{x}^{\lambda+\Delta x} f(u, v) d u d v
\end{aligned}
$$

$(\Delta x>0, \Delta y>0)$. The probability of the random point ( $X, Y$ ) falling in any set $E$ for which the following int-gral is defined (that is, any measurable set $E$ ) is

$$
\operatorname{Pr}\{(X, Y) \in E\}=\iint_{E} f(x, y) d x d y
$$

[^2]This follows from the definition of the integral [as the limit of sums of the sort (4)]. If $f(x, y)$ is continuous in both variables, the probability element $f(x, y) \Delta y \Delta x$ is approximately the probability that $X$ falls between $x$ and $x+\Delta x$ and $Y$ falls between $y$ and $y+\Delta y$ since

$$
\begin{aligned}
\operatorname{Pr}\{x \leq X \leq x+\Delta x, y \leq Y \leq y+\Delta y\} & =\int_{y}^{y+\Delta y} \int_{x}^{x+\Delta x} f(u, v) d u d v \\
& =f\left(x_{0}, y_{0}\right) \Delta x \Delta y
\end{aligned}
$$

for some $x_{0}, y_{0}\left(x \leq x_{0} \leq x+\Delta x, y \leq y_{0} \leq y+\Delta y\right)$ by the mean value theorem of calculus. Since $f(u, v)$ is continuous, (6) is approximately $f(x, y) \Delta x \Delta y$. In fact,

$$
\begin{aligned}
& \left.\lim _{\substack{\Delta y \rightarrow 0 \\
\Delta y \rightarrow 0}} \frac{1}{\Delta x \Delta y} \right\rvert\, \operatorname{Pr}\{x \leq X \leq x+\Delta x, y \leq Y \leq y+\Delta y\} \\
& -f(x, y) \Delta x \Delta y \mid=0 .
\end{aligned}
$$

Now we consider the case of $p$ random variables $X_{1}, X_{2}, \ldots, X_{p}$. The cdf is

$$
F\left(x_{1}, \ldots, x_{p}\right)=\operatorname{Pr}\left\{X_{1} \leq x_{1}, \ldots, X_{p} \leq x_{p}\right\}
$$

defined for every set of real numbers $x_{\mathrm{J}}, \ldots, x_{p}$. The density function, if $F\left(x_{1}, \ldots, x_{p}\right)$ is absolutely continuous, is

$$
\frac{\partial^{p} F\left(x_{1}, \ldots, x_{p}\right)}{\partial x_{1} \cdots \partial x_{p}}=f\left(x_{1}, \ldots, x_{p}\right)
$$

(almost everywhere), and

$$
F\left(x_{1}, \ldots, x_{p}\right)=\int_{-\infty}^{\lambda_{p}} \ldots \int_{-\infty}^{x_{1}} f\left(u_{1}, \ldots, u_{p}\right) d u_{1} \cdots d u_{p}
$$

The probability of falling in any (measurable) set $R$ in the $p$-dimensional Euclidean space is

$$
\left.\operatorname{Pr}_{1}^{\prime}\left(X_{1}, \ldots, X_{p}\right) \in R\right\}=\int \frac{\ldots}{R} \int f\left(x_{1}, \ldots, x_{p}\right) d x_{1} \cdots d x_{p} .
$$

The probability element $f\left(x_{1}, \ldots, x_{p}\right) \Delta x_{1} \cdots \Delta x_{p}$ is approximately the probability $\operatorname{Pr}\left\{x_{1} \leq X_{1} \leq x_{1}+\Delta x_{1}, \ldots, x_{p} \leq X_{p} \leq x_{p}+\Delta x_{p}\right\}$ if $f\left(x_{1}, \ldots, x_{p}\right)$ is
continuous. The joint moments are defined as ${ }^{\dagger}$

$$
\mathscr{E} X_{1}^{h_{1}} \cdots X_{p}^{h_{p}}=\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} x_{1}^{h_{1}} \cdots x_{p}^{h_{p}} f\left(x_{1}, \ldots, x_{p}\right) d x_{1} \cdots d x_{p} .
$$

### 2.2.2. Marginal Distributions

Given the cdf of two random variables $X, Y$ as being $F(x, y)$, the marginal cdf of $X$ is

$$
\begin{aligned}
\operatorname{Pr}\{X \leq x\} & =\operatorname{Pr}\{X \leq x, Y \leq \infty\} \\
& =F(x, \infty)
\end{aligned}
$$

Let this be $F(x)$. Clearly

$$
F(x)=\int_{-\infty}^{x} \int_{-\infty}^{\infty} f(u, v) d v d u
$$

We call

$$
\int_{-\infty}^{\infty} f(u, v) d v=f(u)
$$

say, the marginal density of $X$. Then (14) is

$$
F(x)=\int_{-\infty}^{x} f(u) d u
$$

In a similar fashion we define $G(y)$, the marginal $\operatorname{cdf}$ of $Y$, and $g(y)$, the marginal density of $Y$.

Now we turn to the general case. Given $F\left(x_{1}, \ldots, x_{p}\right)$ as the cdf of $X_{1}, \ldots, X_{p}$, we wish to find the marginal cdf of some of $X_{1}, \ldots, X_{p}$, say, of $X_{1}, \ldots, X_{r}(r<p)$. It is

$$
\begin{aligned}
\operatorname{Pr}\{ & \left.X_{1} \leq x_{1}, \ldots, X_{r} \leq x_{r}\right\} \\
& =\operatorname{Pr}\left\{X_{1} \leq x_{1}, \ldots, X_{r} \leq x_{r}, X_{r+1} \leq \infty, \ldots, X_{p} \leq \infty\right\} \\
& =F\left(x_{1}, \ldots, x_{r}, \infty, \ldots, \infty\right)
\end{aligned}
$$

The marginal density of $X_{1}, \ldots, X_{r}$ is

$$
\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} f\left(x_{1}, \ldots, x_{r}, u_{r+1}, \ldots, u_{p}\right) d u_{r+1} \cdots d u_{p}
$$

[^3]The marginal distribution and density of any other subset of $X_{1}, \ldots, X_{p}$ are obtained in the obviously similar fashion.

The joint moments of a subset of variates can be computed from the marginal distribution; for example,

$$
\begin{aligned}
\mathscr{E} X_{1}^{h_{1}} \cdots X_{r}^{h_{r}}= & \mathscr{E} X_{1}^{h_{1}} \cdots X_{r}^{h_{r}} X_{r+1}^{0} \cdots X_{p}^{0} \\
= & \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} x_{1}^{h_{1}} \cdots x_{r}^{h_{r}} f\left(x_{1}, \ldots, x_{p}\right) d x_{1} \cdots d x_{p} \\
= & \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} x_{1}^{h_{1}} \cdots x_{r}^{h_{r}} \\
& \cdot\left[\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} f\left(x_{1}, \ldots, x_{p}\right) d x_{r+1} \cdots d x_{p}\right] d x_{1} \cdots d x_{r}
\end{aligned}
$$

### 2.2.3. Statistical Independence

Two random variables $X, Y$ with $\operatorname{cdf} F(x, y)$ are said to be independent if

$$
F(x, y)=F(x) G(y)
$$

where $F(x)$ is the marginal cdf of $X$ and $G(y)$ is the marginal cdf of $Y$. This implies that the density of $X, Y$ is

$$
\begin{aligned}
f(x, y) & =\frac{\partial^{2} F(x, y)}{\partial x \partial y}=\frac{\partial^{2} F(x) G(y)}{\partial x \partial y} \\
& =\frac{d F(x)}{d x} \frac{d G(y)}{d y} \\
& =f(x) g(y)
\end{aligned}
$$

Conversely, if $f(x, y)=f(x) g(y)$, then

$$
\begin{aligned}
F(x, y) & =\int_{-\infty}^{y} \int_{-\infty}^{x} f(u, v) d u d v=\int_{-\infty}^{y} \int_{-\infty}^{x} f(u) g(v) d u d v \\
& =\int_{-\infty}^{x} f(u) d u \int_{-\infty}^{y} g(v) d v=F(x) G(y)
\end{aligned}
$$

Thus an equivalent definition of independence in the case of densities existing is that $f(x, y)=f(x) g(y)$. To see the implications of statistical independence, given any $x_{1}<x_{2}, y_{1}<y_{2}$, we consider the probability

$$
\begin{aligned}
\operatorname{Pr}\left\{x_{1} \leq X \leq x_{2}, y_{1}\right. & \left.\leq Y \leq y_{2}\right\} \\
& =\int_{y_{1}}^{y_{2}} \int_{x_{1}}^{x_{2}} f(u, v) d u d v=\int_{x_{1}}^{x_{2}} f(u) d u \int_{y_{1}}^{y_{2}} g(v) d v \\
& =\operatorname{Pr}\left\{x_{1} \leq X \leq x_{2}\right\} \operatorname{Pr}\left\{y_{1} \leq Y \leq y_{2}\right\}
\end{aligned}
$$

The probability of $X$ falling in a given interval and $Y$ falling in a given interval is the product of the probability of $X$ falling in the interval and the probability of $Y$ falling in the other interval.

If the cc'f of $X_{1}, \ldots, X_{p}$ is $F\left(x_{1}, \ldots, x_{p}\right)$, the set of random variables is said to be mutually independent if

$$
F\left(x_{\mathrm{I}}, \ldots, x_{p}\right)=F_{\mathrm{I}}\left(x_{\mathrm{I}}\right) \cdots F_{p}\left(x_{p}\right),
$$

where $F_{i}\left(x_{i}\right)$ is the marginal cdf of $X_{i}, i=1, \ldots, p$. The set $X_{1}, \ldots, X_{r}$ is said to be independent of the set $X_{r+1}, \ldots, X_{p}$ if

$$
F\left(x_{1}, \ldots, x_{p}\right)=F\left(x_{1}, \ldots, x_{r}, \infty, \ldots, \infty\right) \cdot F\left(\infty, \ldots, \infty, x_{r+1}, \ldots, x_{r}\right) .
$$

One result of independence is that joint moments factor. For example, if $X_{1}, \ldots, X_{p}$ are mutually independent, then

$$
\begin{aligned}
\mathscr{E} X_{1}^{h_{1}} \cdots X_{p}^{h_{p}} & =\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} x_{1}^{h_{1}} \cdots x_{p}^{h_{p}} f_{1}\left(x_{1}\right) \cdots f_{p}\left(x_{p}\right) d x_{1} \cdots d x_{p} \\
& =\prod_{i=1}^{p} \int_{-\infty}^{\infty} x_{i}^{h_{1}} f_{i}\left(x_{1}\right) d x_{1} \\
& =\prod_{t=1}^{p}\left\{\mathscr{E} X_{1}^{h_{1}}\right\} .
\end{aligned}
$$

### 2.2.4. Conditional Distributions

If $A$ and $B$ are two events such that the probability of $A$ and $B$ occurring simultaneously is $P(A B)$ and the probability of $B$ occurring is $P(B)>0$, then the conditional probability of $A$ occurring given that $B$ has occurred is $P(A B) / P(B)$. Suppose the event $A$ is $X$ falling in the interval $\left[x_{1}, x_{2}\right]$ and the event $B$ is $Y$ falling in $\left[y_{1}, y_{2}\right]$. Then the conditional probability that $X$ falls in $\left[x_{1}, x_{2}\right]$, given that $Y$ falls in $\left[y_{1}, y_{2}\right]$, is

$$
\begin{aligned}
\operatorname{Pr}\left\{x_{1} \leq X \leq x_{2} \mid y_{1} \leq Y \leq y_{2}\right\} & =\frac{\operatorname{Pr}\left\{x_{1} \leq X \leq x_{2}, y_{1} \leq Y \leq y_{2}\right\}}{\operatorname{Pr}\left\{y_{1} \leq Y \leq y_{2}\right\}} \\
& =\frac{\int_{x_{1}}^{x_{2}} \int_{y_{1}}^{y_{2}} f(u, v) d v d u}{\int_{y_{1}}^{y_{2}} g(v) d v}
\end{aligned}
$$

Now let $y_{1}=y, y_{2}=y+\Delta y$. Then for a continuous density,

$$
\int_{y}^{y+\Delta y} g(v) d v=g\left(y^{*}\right) \Delta y
$$

where $y \leq y^{*} \leq y+\Delta y$. Also

$$
\int_{y}^{y+\Delta y} f(u, v) d t=f\left[u, y^{*}(u)\right] \Delta y
$$

where $y \leq y^{*}(u) \leq y+\Delta y$. Therefore,

$$
\operatorname{Pr}\left\{x_{\mathrm{I}} \leq X \leq x_{2} \mid y \leq Y \leq y+\Delta y\right\}=\int_{x_{1}}^{x_{2}} \frac{f\left[u, y^{*}(u)\right]}{g\left(y^{*}\right)} d u .
$$

It will be noticed that for fixed $y$ and $\Delta y(>0)$, the integrand of $(30)$ behaves as a univariate density function. Now for $y$ such that $g(y)>0$, we define $\operatorname{Pr}\left\{x_{1} \leq X \leq 1, \mid Y=y\right\}$, the probability that $X$ lies between $x_{1}$ and $x_{2}$, given that $Y$ is $y$, as the limit of (30) as $\Delta y \rightarrow 0$. Thus

$$
\operatorname{Pr}\left\{x_{1} \leq X \leq x_{2} \mid Y=y\right\}=\int_{x_{1}}^{x_{2}} f(u \mid y) d u
$$

where $f(u \mid y)=f(u, y) / g(y)$. For given $y, f(u \mid y)$ is a density function and is called the conditional density of $X$ given $y$. We note that if $X$ and $Y$ are independent, $f(x \mid y)=f(x)$.

In the general case of $X_{1}, \ldots, X_{p}$ with $\operatorname{cdf} F\left(x_{1}, \ldots, x_{p}\right)$, the conditional density of $X_{1}, \ldots, X_{r}$, given $X_{r+1}=x_{r+1}, \ldots, X_{p}=x_{p}$, is

$$
\frac{f\left(x_{1}, \ldots, x_{p}\right)}{\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} f\left(u_{1}, \ldots, u_{r}, x_{r+1}, \ldots, x_{p}\right) a u_{1} \cdots d u_{r}} .
$$

For a more general discussion of conditional probabilities, the reader is referred to Chung (1974), Kolmogorov (1950), Loève (1977), (1978), and Neveu (1965).

### 2.2.5. Transformation of Variables

Let the density of $X_{1}, \ldots, X_{p}$ be $f\left(x_{1}, \ldots, x_{p}\right)$. Consider the $p$ real-valued functions

$$
y_{i}=y_{1}\left(x_{1}, \ldots, x_{p}\right), \quad i=1, \ldots, p
$$

We assume that the transformation from the $x$-space to the $y$-space is one-to-one; ${ }^{\dagger}$ the inverse transformation is

$$
x_{1}=x_{1}\left(y_{1}, \ldots, y_{p}\right), \quad i=1, \ldots, p
$$

${ }^{\dagger}$ More precisely. we assume this is true for the part of the $x$-space for which $f\left(x_{1}, \ldots, x_{p}\right)$ is positive.


[^0]:    ${ }^{\dagger}$ For a detailed study of the development of the ideas of correlation, see Walker (1931).

[^1]:    . An Introduction to Multurarate Statistical Analyss, "Thrd Editon. By '1. W. Anderson ISBN 0-47!-36091-0 Copyright © 2003 John Wiley \& Sons, Inc.

[^2]:    ${ }^{\dagger}$ In Chapter 2 we shall distinguish between random variables and running variables by use of capital and lowercase letters, respectively. In later chapters we may be unable to hold to this convention because of other complications of notation.

[^3]:    ${ }^{\dagger} \mathscr{E}$ will be used to denote mathematical expectation.



Let the random variables $Y_{1}, \ldots, Y_{p}$ be defined by

$$
Y_{1}=y_{i}\left(X_{1}, \ldots, X_{p}\right), \quad i=1, \ldots, p .
$$

Then the density of $Y_{1}, \ldots, Y_{p}$ is

$$
g\left(y_{1}, \ldots, y_{p}\right)=f\left[x_{1}\left(y_{1}, \ldots, y_{p}\right), \ldots, x_{p}\left(y_{1}, \ldots, y_{p}\right)\right] J\left(y_{1}, \ldots, y_{p}\right),
$$

where $J\left(y_{1}, \ldots, y_{p}\right)$ is the Jacobian

$$
J\left(y_{1}, \ldots, y_{p}\right)=\bmod \left|\begin{array}{cccc}
\frac{\partial x_{1}}{\partial y_{1}} & \frac{\partial x_{1}}{\partial y_{2}} & \ldots & \frac{\partial x_{1}}{\partial y_{p}} \\
\frac{\partial x_{2}}{\partial y_{1}} & \frac{\partial x_{2}}{\partial y_{2}} & \ldots & \frac{\partial x_{2}}{\partial y_{p}} \\
\vdots & \vdots & & \vdots \\
\frac{\partial x_{p}}{\partial y_{1}} & \frac{\partial x_{p}}{\partial y_{2}} & \ldots & \frac{\partial x_{p}}{\partial y_{p}}
\end{array}\right| .
$$

We assume the derivatives exist, and "mod" means modulus or absolute value of the expression following it. The probability that ( $X_{1}, \ldots, X_{p}$ ) falls in a region $R$ is given by (11); the probability that ( $Y_{1}, \ldots, Y_{p}$ ) falls in a region $S$ is

$$
\operatorname{Pr}\left\{\left(Y_{1}, \ldots, Y_{p}\right) \in S\right\}=\int \cdots \int \underset{S}{\ldots} \int g\left(y_{1}, \ldots, y_{p}\right) d y_{1} \cdots d y_{p} .
$$

If $S$ is the transform of $R$, that is, if each point of $R$ transforms by (33) into a point of $S$ and if each point of $S$ transforms into $R$ by (34), then (11) is equal to (38) by the usual theory of transformation of multiple integrals. From this follows the assertion that (36) is the density of $Y_{1}, \ldots, Y_{p}$.

### 2.3. THE MULTIVARIATE NORMAL DISTRIBUTION

The univariate normal density function can be written

$$
k e^{-\frac{1}{2} \alpha(x-\beta)^{2}}=k e^{-\frac{1}{2}(x-\beta) \alpha(x-\beta)},
$$

where $\alpha$ is positive and $k$ is chosen so that the integral of (1) over the entire $x$-axis is unity. The density function of a multivariate normal distribution of $X_{1}, \ldots, X_{p}$ has an analogous form. The scalar variable $x$ is replaced by a vector

$$
x=\left(\begin{array}{c}
x_{1} \\
\vdots \\
x_{p}
\end{array}\right) ;
$$

the scalar constant $\beta$ is replaced by a vector

$$
\boldsymbol{b}=\left(\begin{array}{c}
b_{1} \\
\vdots \\
b_{p}
\end{array}\right) ;
$$

and the positive constant $\alpha$ is replaced by a positive definite (symmetric) matrix

$$
\boldsymbol{A}=\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 p} \\
a_{21} & a_{22} & \cdots & a_{2 p} \\
\vdots & \vdots & & \vdots \\
a_{p 1} & a_{p 2} & \cdots & a_{p p}
\end{array}\right) .
$$

The square $\alpha(x-\beta)^{2}=(x-\beta) \alpha(x-\beta)$ is replaced by the quadratic form

$$
(x-b)^{\prime} A(x-b)=\sum_{i, j=1}^{p} a_{i}\left(x_{i}-b_{i}\right)\left(x_{j}-b_{j}\right) .
$$

Thus the density function of a $p$-variate normal distribution is

$$
f\left(x_{1}, \ldots, x_{p}\right)=K e^{-\frac{1}{3}(x-b)^{\prime} A(x-b)},
$$

where $K(>0)$ is chosen so that the integral over the entire $p$-dimensional Euclidean space of $x_{1}, \ldots, x_{p}$ is unity.

Written in matrix notation, the similarity of the multivariate normal density (6) to the univariate density (1) is clear. Throughout this book we shall use matrix notation and operations. The reader is referred to the Appendix for a review of matrix theory and for definitions of our notation for matrix operations.

We observe that $f\left(x_{1}, \ldots, x_{p}\right)$ is nonnegative. Since $\boldsymbol{A}$ is positive definite,

$$
(x-b)^{\prime} A(x-b) \geq 0
$$

and therefore the density is bounded; that is,

$$
f\left(x_{1}, \ldots, x_{p}\right) \leq K .
$$

Now let us determine $K$ so that the integral of (6) over the $p$-dimensional space is one. We shall evaluate

$$
K^{*}=\int_{\infty}^{\infty} \cdots \int_{\infty}^{\infty} e^{-\frac{1}{3}(x-b)^{\prime} A(x-b)} d x_{p} \cdots d x_{1} .
$$

We use the fact (see Corollary A.1.6 in the Appendix) that if $\boldsymbol{A}$ is positive definite, there exists a nonsingular matrix $\boldsymbol{C}$ such that

$$
C^{\prime} A C=I,
$$

where $\boldsymbol{I}$ denotes the identity and $\boldsymbol{C}^{\prime}$ the transpose of $\boldsymbol{C}$. Let

$$
x-b=C y
$$

where

$$
y=\left(\begin{array}{c}
y_{1} \\
\vdots \\
y_{p}
\end{array}\right) .
$$

Then

$$
(x-b)^{\prime} A(x-b)=y^{\prime} C^{\prime} A C y=y^{\prime} y .
$$

The Jacobian of the transformation is

$$
J=\bmod |C|
$$

where $\bmod |\boldsymbol{C}|$ indicates the absolute value of the determinant of $\boldsymbol{C}$. Thus (9) becomes

$$
K^{*}=\bmod |C| \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} e^{-\frac{1}{2} y^{\prime} y} d y_{p} \cdots d y_{1}
$$

We have

$$
e^{-\frac{1}{2} y^{\prime} y}=\exp \left(-\frac{1}{2} \sum_{i=1}^{p} y_{i}^{2}\right)=\prod_{i=1}^{\mu} e^{-\frac{1}{2} y_{i}^{2}},
$$

where $\exp (z)=e^{z}$. We can write (15) as

$$
\begin{aligned}
K^{*} & =\bmod |C| \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} e^{-\frac{1}{2} y_{1}^{2} \cdots e^{-\frac{1}{3} y_{p}^{2}} d y_{p} \cdots d y_{1}} \\
& =\bmod |C| \prod_{i=1}^{p}\left\{\int_{-\infty}^{\infty} e^{-\frac{1}{2} y_{i}^{2}} d y_{i}\right\} \\
& =\bmod |C| \prod_{i=1}^{p}\{\sqrt{2 \pi}\} \\
& =\bmod |C|(2 \pi)^{\frac{1}{2} p}
\end{aligned}
$$

by virtue of

$$
\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-\frac{1}{2} t^{2}} d t=1
$$

Corresponding to (10) is the determinantal equation

$$
\left|C^{\prime}\right| \cdot|A| \cdot|C|=|I| .
$$

Since

$$
\left|C^{\prime}\right|=|C|,
$$

and since $|\boldsymbol{I}|=1$, we deduce from (19) that

$$
\bmod |\boldsymbol{C}|=1 / \sqrt{|\boldsymbol{A}|}
$$

Thus

$$
K=1 / K^{*}=\sqrt{|A|}(2 \pi)^{-\frac{1}{2} p} .
$$

The normal density function is

$$
\frac{\sqrt{|A|}}{(2 \pi)^{\frac{1}{2} p}} e^{-\frac{1}{2}(x-b)^{\prime} A(x-b)}
$$

We shall now show the significance of $\boldsymbol{b}$ and $\boldsymbol{A}$ by finding the first and second moments of $X_{\mathrm{I}}, \ldots, X_{p}$. It will be convenient to consider these random variables as constituting a random vector

$$
\boldsymbol{X}=\left(\begin{array}{c}
X_{1} \\
\vdots \\
X_{p}
\end{array}\right) .
$$

We shall define generally a random matrix and the expected value of a random matrix; a random vector is considered as a special case of a random matrix with one column.

Definition 2.3.1. $A$ random matrix $Z$ is a matrix

$$
Z=\left(Z_{g h}\right), \quad g=1, \ldots, m, \quad h=1, \ldots, n
$$

of random variables $Z_{11}, \ldots, Z_{m n}$.

If the random variables $Z_{11}, \ldots, Z_{m n}$ can take on only a finite number of values, the random matrix $\boldsymbol{Z}$ can be one of a finite number of matrices, say $Z(1), \ldots, Z(q)$. If the probability of $Z=Z(i)$ is $p_{t}$, then we should like to define $\mathscr{E} Z$ as $\sum_{i=1}^{q} Z(i),_{r}$. Then $\mathscr{E} Z=\left(\mathscr{E} Z_{g h}\right)$. If the random variables $Z_{11}, \ldots, Z_{m n}$ have a joint density, then by operating with Riemann sums we can define $\mathscr{E} Z$ as the limit (if the limit exists) of approximating sums of the kind occurring in the discrete case; then again $\mathscr{E} Z=\left(\mathscr{E} Z_{g h}\right)$. Therefore, in general we shall use the following definition:

Definition 2.3.2. The expected value of a random matrix $\boldsymbol{Z}$ is

$$
\mathscr{E} Z=\left(\mathscr{E} Z_{g h}\right), \quad g=1, \ldots, m, \quad h=1, \ldots, n .
$$

In particular if $Z$ is $X$ defined by (24), the expected value

$$
\mathscr{E} X=\left(\begin{array}{c}
\mathscr{E} X_{1} \\
\vdots \\
\mathscr{E} X_{p}
\end{array}\right)
$$

is the mean or mean vector of $X$. We shall usually denote this mean vector by $\boldsymbol{\mu}$. If $\boldsymbol{Z}$ is $(\boldsymbol{X}-\boldsymbol{\mu})(\boldsymbol{X}-\boldsymbol{\mu})^{\prime}$, the expected value is

$$
\mathscr{C}(X)=\mathscr{E}(X-\mu)(X-\mu)^{\prime}=\left[\mathscr{E}\left(X_{t}-\mu_{t}\right)\left(X_{j}-\mu_{j}\right)\right],
$$

the covariance or covariance matrix of $X$. The $i$ th diagonal element of this matrix, $\mathscr{E}\left(X_{l}-\mu_{l}\right)^{2}$, is the variance of $X_{t}$, and the $i, j$ th off-diagonal element, $\mathscr{E}\left(X_{i}-\mu_{i}\right)\left(X_{j}-\mu_{j}\right)$, is the covariance of $X_{i}$ and $X_{j}, i \neq j$. We shall usually denote the covariance matrix by $\Sigma$. Note that

$$
\mathscr{B}(X)=\mathscr{E}\left(X X^{\prime}-\mu X^{\prime}-X \mu^{\prime}+\mu \mu^{\prime}\right)=\mathscr{E} X X^{\prime}-\mu \mu^{\prime} .
$$

The operation of taking the expected value of a random matrix (or vector) satisfies certain rules which we can summarize in the following lemma:

Lemma 2.3.1. If $\boldsymbol{Z}$ is an $m \times n$ random matrix, $\boldsymbol{D}$ is an $l \times m$ real matrix, $E$ is an $n \times q$ real matrix, and $F$ is an $l \times q$ real matrix, then

$$
\mathscr{E}(D Z E+F)=D(\mathscr{E} Z) E+F .
$$

Proof. The element in the $i$ th row and $j$ th column of $\mathscr{E}(\boldsymbol{D Z E}+\boldsymbol{F})$ is

$$
\mathscr{E}\left(\sum_{h, g} d_{i h} Z_{h g} e_{g)}+f_{i}\right)=\sum_{h, g} d_{i h}\left(\mathscr{E} Z_{h g}\right) e_{g j}+f_{i j},
$$

which is the element in the $i$ th row and $j$ th column of $D(\mathscr{E} Z) E+F$.

Lemma 2.3.2. If $Y=D X+f$, where $X$ is a random vector, then

$$
\begin{aligned}
\mathscr{E} Y & =D \mathscr{E} X+f, \\
\mathscr{C}(Y) & =D \mathscr{C}(X) D^{\prime} .
\end{aligned}
$$

Prouf. The first assertion follows directly from Lemma 2:3.1, and the second from

$$
\begin{aligned}
\mathscr{C}(Y) & =\mathscr{E}(Y-\mathscr{E} Y)(Y-\mathscr{E} Y)^{\prime} \\
& =\mathscr{E}[D X+f-(D \mathscr{E} X+f)][D X+f-(D \mathscr{E} X+f)]^{\prime} \\
& =\mathscr{E}[D(X-\mathscr{E} X)][D(X-\mathscr{E} X)]^{\prime} \\
& =\mathscr{E}\left[D(X-\mathscr{E} X)(X-\mathscr{E} X)^{\prime} D^{\prime}\right],
\end{aligned}
$$

which yields the right-hand side of (33) by Lemma 2.3.1.
When the transformation corresponds to (11), that is, $\boldsymbol{X}=\boldsymbol{C Y}+\boldsymbol{b}$, then $\mathscr{E} \boldsymbol{X}=\boldsymbol{C} \mathscr{E} \boldsymbol{Y}+\boldsymbol{b}$. By the transformation theory given in Section 2.2, the density of $Y$ is proportional to (16); that is, it is

$$
\frac{1}{(2 \pi)^{\frac{1}{3} p}} e^{-\frac{1}{y} y^{\prime} y}=\prod_{j=1}^{P}\left\{\frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{y} y^{2}}\right\} .
$$

The expected value of the $i$ th component of $Y$ is

$$
\begin{aligned}
\mathscr{E} Y_{1} & =\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} y_{1} \prod_{j=1}^{p}\left\{\frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} y_{i}^{2}}\right\} d y_{1} \cdots d y_{p} \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} y_{i} e^{-\frac{1}{2} y_{i}^{2}} d y_{1} \prod_{j=1}^{p}\left\{\int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} y_{j}^{2}} d y_{j}\right\} \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} y_{i} e^{-\frac{1}{2} y_{i}^{2}} d y_{i} \\
& =0
\end{aligned}
$$

The last equality follows because ${ }^{\dagger} y_{i} e^{-\frac{1}{2} y_{1}^{2}}$ is an odd function of $y_{i}$. Thus $\mathscr{E} \boldsymbol{Y}=\mathbf{0}$. Therefore, the mean of $\boldsymbol{X}$, denoted by $\boldsymbol{\mu}$, is

$$
\boldsymbol{\mu}=\mathscr{E} \boldsymbol{X}=\boldsymbol{b} .
$$

From (33) we see that $\mathscr{C}(\boldsymbol{X})=\boldsymbol{C}\left(\mathscr{E}^{\circ} \mathbf{Y} Y^{\prime}\right) \boldsymbol{C}^{\prime}$. The $i$, jth element of $\mathscr{E} \mathbf{Y} Y^{\prime}$ is

$$
\mathscr{E} Y_{i} Y_{j}=\int_{-c}^{\infty} \cdots \int_{-\infty}^{\infty} y_{i} y_{j} \prod_{h=1}^{p}\left\{\frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} y_{h}^{2}}\right\} d y_{1} \cdots d y_{p}
$$

because the density of $Y$ is (35). If $i=j$, we have

$$
\begin{aligned}
\mathscr{E} Y_{t}^{2} & =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} y_{t}^{2} e^{-\frac{1}{2} y_{t}^{2}} d y_{i} \prod_{\substack{h=1 \\
h \neq i}}^{p}\left\{\int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} y_{h}^{2}} d y_{h}\right\} \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} y_{t}^{2} e^{-\frac{1}{2} y_{t}^{2}} d y_{i} \\
& =1
\end{aligned}
$$

The last equality follows because the next to last expression is the expected value of the square of a variable normally distributed with mean 0 and variance 1. If $i \neq j$, (38) becomes

$$
\begin{aligned}
\mathscr{E} Y_{i} Y_{j}= & \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} y_{i} e^{-\frac{1}{2} y_{i}^{2}} d y_{i} \cdot \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} y_{j} e^{-\frac{1}{2} y_{j}^{2}} d y_{j} \\
& \cdot \prod_{\substack{h=1 \\
h \neq i, j}}^{p}\left\{\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-\frac{1}{2} y_{h}^{2}} d y_{h}\right\} \\
= & 0, \quad i \neq j,
\end{aligned}
$$

since the first integration gives 0 . We can summarize (39) and (40) as

$$
\mathscr{E} Y Y^{\prime}=I .
$$

Thus

$$
\mathscr{E}(X-\mu)(X-\mu)^{\prime}=C I C^{\prime}=C C^{\prime} .
$$

From (10) we obtain $A=\left(C^{\prime}\right)^{-1} C^{-1}$ by multiplication by $\left(C^{\prime}\right)^{-1}$ on the left and by $C^{-1}$ on the right. Taking inverses on both sides of the equality
${ }^{\dagger}$ Alternatively, the last equality follows because the next to last expression is the expected value of a normally distributed variable with mean 0 .
gives us

$$
C C^{\prime}=A^{-1}
$$

Thus, the covariance matrix of $X$ is

$$
\boldsymbol{\Sigma}=\mathscr{E}(X-\boldsymbol{\mu})(X-\boldsymbol{\mu})^{\prime}=A^{-1} .
$$

From (43) we see that $\Sigma$ is positive definite. Let us summarize these results.
Theorem 2.3.1. If the density of a $p$-dimensional random vector $X$ is (23), then the expected value of $X$ is $b$ and the covariance matrix is $A^{-1}$. Conversely, given a vector $\boldsymbol{\mu}$ and a positive definite matrix $\boldsymbol{\Sigma}$, there is a multivariate normal density

$$
(2 \pi)^{-\frac{1}{2} p}|\Sigma|^{-\frac{1}{2}} e^{-\frac{1}{2}(x-\mu)^{\prime} \Sigma^{-1}(x-\mu)}
$$

such that the expected value of the vector with this density is $\mu$ and the covariance matrix is $\mathbf{\Sigma}$.

We shall denote the density (45) as $n(x \mid \mu, 2)$ and the distribution law as $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$.

The $i$ th ciagonal element of the covariance matrix, $\sigma_{i f}$, is the variance of the $i$ th component of $X$; we may sometimes denote this by $\sigma_{i}{ }^{2}$. The correlation coefficient between $X_{1}$ and $X_{1}$ is defined as

$$
\rho_{i j}=\frac{\sigma_{i j}}{\sqrt{\sigma_{i l}} \sqrt{\sigma_{j j}}}=\frac{\sigma_{i j}}{\sigma_{i} \sigma_{j}}
$$

This measure of association is symmetric in $X_{i}$ and $X_{j}: \rho_{i j}=\rho_{j n}$. Since

$$
\left(\begin{array}{ll}
\sigma_{u i} & \sigma_{i j} \\
\sigma_{j i} & \sigma_{j l}
\end{array}\right)=\left(\begin{array}{cc}
\sigma_{\imath}^{2} & \sigma_{\imath} \sigma_{\jmath} \rho_{i \jmath} \\
\sigma_{\imath} \sigma_{\jmath} \rho_{\imath j} & \sigma_{\jmath}^{2}
\end{array}\right)
$$

is positive definite (Corollary A.1.3 of the Appendix), the determinant

$$
\left|\begin{array}{cc}
\sigma_{i}^{2} & \sigma_{\imath} \sigma_{\jmath} \rho_{\imath \jmath} \\
\sigma_{\imath} \sigma_{\jmath} \rho_{i j} & \sigma_{\jmath}^{2}
\end{array}\right|=\sigma_{\imath}^{2} \sigma_{\jmath}^{2}\left(1-\rho_{i j}^{2}\right)
$$

is positive. Therefore, $-1<\rho_{1 j}<1$. (For singular distributions, see Section 2.4.) The multivariate normal density can be parametrized by the means $\mu_{p}$, $i=1, \ldots, p$, the variances $\sigma_{i}^{2}, i=1, \ldots, p$, and the correlations $\rho_{i j}, i<j i, j=1, \ldots, p$.

As a special case of the preceding theory, we consider the bivariate normal distribution. The mean vector is

$$
\mathscr{E}\binom{X_{1}}{X_{2}}=\binom{\mu_{1}}{\mu_{2}}
$$

the covariance matrix may be written

$$
\begin{aligned}
\Sigma & =\mathscr{E}\left(\begin{array}{cc}
\left(X_{1}-\mu_{1}\right)^{2} & \left(X_{1}-\mu_{1}\right)\left(X_{2}-\mu_{2}\right) \\
\left(X_{2}-\mu_{2}\right)\left(X_{1}-\mu_{1}\right) & \left(X_{2}-\mu_{2}\right)^{2}
\end{array}\right) \\
& =\left(\begin{array}{ll}
\sigma_{11} & \sigma_{12} \\
\sigma_{21} & \sigma_{22}
\end{array}\right)=\left(\begin{array}{cc}
\sigma_{1}^{2} & \sigma_{1} \sigma_{2} \rho \\
\sigma_{1} \sigma_{2} \rho & \sigma_{2}^{2}
\end{array}\right),
\end{aligned}
$$

where $\sigma_{\mathrm{I}}^{2}$ is the variance of $X_{1}, \sigma_{2}^{2}$ the variance of $X_{2}$, and $\rho$ the correlation between $X_{1}$ and $X_{2}$. The inverse of (50) is

$$
\Sigma^{-1}=\frac{1}{1-\rho^{2}}\left(\begin{array}{cc}
\frac{1}{\sigma_{1}^{2}} & -\frac{\rho}{\sigma_{1} \sigma_{2}} \\
-\frac{\rho}{\sigma_{1} \sigma_{2}} & \frac{1}{\sigma_{2}^{2}}
\end{array}\right) .
$$

The density function of $X_{1}$ and $X_{2}$ is

$$
\begin{aligned}
\frac{1}{2 \pi \sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}} \exp \{- & \frac{1}{2\left(1-\rho^{2}\right)}\left[\frac{\left(x_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}\right. \\
& \left.\left.\quad-2 \rho \frac{\left(x_{1}-\mu_{1}\right)\left(x_{2}-\mu_{2}\right)}{\sigma_{1} \sigma_{2}}+\frac{\left(x_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right]\right\} .
\end{aligned}
$$

Theorem 2.3.2. The correlation coefficient $\rho$ of any bivariate distribution is invariant with respect to transformations $X_{i}^{*}=b_{i} X_{i}+c_{i}, b_{i}>0, i=1,2$. Every function of the parameters of a bivariate normal distribution that is invariant with respect to such transformations is a function of $\rho$.

Proof. The variance of $X_{t}^{*}$ is $b_{t}^{2} \sigma_{t}^{2}, i=1,2$, and the covariance of $X_{1}^{*}$ and $X_{2}^{*}$ is $b_{1} b_{2} \sigma_{1} \sigma_{2} \rho$ by Lemma 2.3.2. Insertion of these values into the definition of the correlation between $X_{1}^{*}$ and $X_{2}^{*}$ shows that it is $\rho$. If $f\left(\mu_{1}, \mu_{2}, \sigma_{1}, \sigma_{2}, \rho\right)$ is invat iant with respect to such transformations, it must be $f(0,0,1,1, \rho)$ by choice of $b_{i}=1 / \sigma_{i}$ and $c_{i}=-\mu_{i} / \sigma_{i}, i=1,2$. $\square$

The correlation coefficient $\rho$ is the natural measure of association between $X_{1}$ and $X_{2}$. Any function of the parameters of the bivariate normal distribution that is independent of the scale and location parameters is a function of $\rho$. The standardized variable (or standard score) is $Y_{1}=\left(X_{i}-\mu_{i}\right) / \sigma_{i}$. The mean squared difference between the two standardized variables is

$$
\mathscr{E}\left(Y_{1}-Y_{2}\right)^{2}=2(1-\rho) .
$$

The smaller (53) is (that is, the larger $\rho$ is), the more similar $Y_{1}$ and $Y_{2}$ are. If $\rho>0, X_{1}$ and $X_{2}$ tend to be positively related, and if $\rho<0$, they tend to be negatively related. If $\rho=0$, the density (52) is the product $o$ the marginal densities of $X_{1}$ and $X_{2}$; hence $X_{1}$ and $X_{2}$ are independent.

It will be noticed that the density function (45) is constant on ellipsoids

$$
(x-\mu)^{\prime} \Sigma^{-1}(x-\mu)=c
$$

for even positive value of $c$ in a $p$-dimensional Euclidean space. The center of each ellipsoid is at the point $\boldsymbol{\mu}$. The shape and orientation of the ellipsoid are determined by $\boldsymbol{\Sigma}$, and the size (given $\boldsymbol{\Sigma}$ ) is determined by $c$. Because (54) is a sphere if $\Sigma=\sigma^{2} I, n\left(x \mid \mu, \sigma^{2} I\right)$ is known as a spherical normal density.

Let us consider in detail the bivariate case of the density (52). We transform coordinates by $\left(x_{1}-\mu_{1}\right) / \sigma_{1}=y_{1}, i=1,2$, so that the centers of the loci of constant density are at the origin. These loci are defined by

$$
\frac{1}{1-\rho^{2}}\left(y_{1}^{2}-2 \rho y_{1} y_{2}+y_{2}^{2}\right)=c .
$$

The interepts on the $y_{1}$-axis and $y_{2}$-axis are equal, If $\rho>0$, the major axis of the ellipse is along the $45^{\circ}$ line with a length of $2 \sqrt{c(1+\rho)}$, and the minor axis has a length of $2 \sqrt{c(1-\rho)}$, If $\rho<0$, the major axis is along the $135^{\circ}$ line with a length of $2 \sqrt{c(1-\rho)}$, and the minor axis has a length of $2 \sqrt{c(1+\rho)}$. The value of $\rho$ determines the ratio of these lengths. In this bivariate case we can think of the density function as a surface above the plane. The contours of equal density are contours of equal altitude on a topographical map; they indicate the shape of the hill (or probability surface). If $\rho>0$, the hill will tend to run along a line with a positive slope; most of the hill will be in the first and third quadrants. When we transform back to $x_{i}=\sigma_{i} y_{i}+\mu_{i}$, we expand each contour by a factor of $\sigma_{t}$ in the direction of the $i$ th axis and shift the center to ( $\mu_{1}, \mu_{2}$ ).



The numerical values of the cdf of the univariate normal variable are obtained from tables found in most statistical texts. The numerical values of

$$
\begin{aligned}
F\left(x_{1}, x_{2}\right) & =\operatorname{Pr}\left(X_{1} \leq x_{1}, X_{2} \leq x_{2}\right\} \\
& =\operatorname{Pr}\left\{\frac{X_{1}-\mu_{1}}{\sigma_{1}} \leq y_{1}, \frac{X_{2}-\mu_{2}}{\sigma_{2}} \leq y_{2}\right\}
\end{aligned}
$$

where $y_{1}=\left(x_{1}-\mu_{1}\right) / \sigma_{1}$ and $y_{2}=\left(x_{2}-\mu_{2}\right) / \sigma_{2}$, can be found in Pearson (1931). An extensive table has been given by the National Bureau of Standards (1959). A bibliography of such tables has been given by Gupta (1963). Pearson has also shown that

$$
F\left(x_{1}, x_{2}\right)=\sum_{j=0}^{\infty} \rho^{j} \tau_{j}\left(y_{1}\right) \tau_{j}\left(y_{2}\right),
$$

where the so-called tetrachoric functions $\tau_{j}(y)$ are tabulated in Pearson (1930) up to $\tau_{19}(y)$. Harris and Soms (1980) have studied generalizations of (57).

### 2.4. THE DISTRIBUTION OF LINEAR COMBINATIONS OF NORMALLY DISTRIBUTED VARIATES; INDEPENDENCE OF VARIATES; MARGINAL DISTRIBUTIONS

One of the reasons that the study of normal multivariate distributions is so useful is that marginal distributions and conditional distributions derived from multivariate normal distributions are also normal distributions. Moreover, linear combinations of multivariate normal variates are again normally distributed. First we shall show that if we make a nonsingular linear transformation of a vector whose components have a joint distribution with a normal density, we obtain a vector whose components are jointly distributed with a normal density.

Theorem 2.4.1. Let $X$ (with $p$ components) be distributed according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. Then

$$
Y=C X
$$

is distributed according to $N\left(\boldsymbol{C} \boldsymbol{\mu}, \boldsymbol{C} \boldsymbol{\Sigma} \boldsymbol{C}^{\prime}\right)$ for $\boldsymbol{C}$ nonsingular.
Proof. The density of $Y$ is obtained from the density of $X, n(x \mid \mu, \Sigma)$, by replacing $x$ by

$$
x=C^{-1} y,
$$

and multiplying by the Jacobian of the transformation (2),
(3) $\quad \bmod \left|\boldsymbol{C}^{-1}\right|=\frac{1}{\bmod |\boldsymbol{C}|}=\sqrt{\frac{1}{|\boldsymbol{C}|^{2}}}=\sqrt{\frac{|\boldsymbol{\Sigma}|}{|\boldsymbol{C}| \cdot|\boldsymbol{\Sigma}| \cdot\left|\boldsymbol{C}^{\prime}\right|}}=\frac{|\boldsymbol{\Sigma}|^{i}}{\left|\boldsymbol{C} \boldsymbol{\Sigma} \boldsymbol{C}^{\prime}\right|^{\frac{1}{2}}}$.

The quadratic form in the exponent of $n(x \mid \mu, \Sigma)$ is

$$
Q=(x-\mu)^{\prime} \Sigma^{-1}(x-\mu) .
$$

The transformation (2) carries $Q$ into

$$
\begin{aligned}
Q & =\left(C^{-1} y-\mu\right)^{\prime} \Sigma^{-1}\left(C^{-1} y-\mu\right) \\
& =\left(C^{-1} y-C^{-1} C \mu\right)^{\prime} \Sigma^{-1}\left(C^{-1} y-C^{-1} C \mu\right) \\
& =\left[C^{-1}(y-C \mu)\right]^{\prime} \Sigma^{-1}\left[C^{1}(y-C \mu)\right] \\
& =(y-C \mu)^{\prime}\left(C^{-1}\right)^{\prime} \Sigma^{-1} C^{-1}(y-C \mu) \\
& =(y-C \mu)^{\prime}\left(C \Sigma C^{\prime}\right)^{-1}(y-C \mu)
\end{aligned}
$$

since $\left(C^{-1}\right)^{\prime}=\left(C^{\prime}\right)^{-1}$ by virtue of transposition of $C C^{-1}=I$. Thus the density of $Y$ is

$$
\begin{aligned}
& n\left(C^{-1} y \mid \mu, \Sigma\right) \bmod |C|^{-1} \\
& \quad=(2 \pi)^{-\frac{1}{2} f^{\prime}}\left|C \Sigma C^{\prime}\right|^{-\frac{1}{2}} \exp \left[-\frac{1}{2}(y-C \mu)^{\prime}\left(C \Sigma C^{\prime}\right)^{-1}(y-C \mu)\right] \\
& \quad=n\left(y \mid C \mu, C \Sigma C^{\prime}\right)
\end{aligned}
$$

Now let us consider two sets of random variables $X_{1}, \ldots, X_{q}$ and $X_{q+1}, \ldots, X_{p}$ forming the vectors

$$
\boldsymbol{X}^{(1)}=\left(\begin{array}{c}
X_{1} \\
\vdots \\
X_{q}
\end{array}\right), \quad \boldsymbol{X}^{(2)}=\left(\begin{array}{c}
X_{q+1} \\
\vdots \\
X_{p}
\end{array}\right) .
$$

These variables form the random vector

$$
\boldsymbol{X}=\binom{\boldsymbol{X}^{(1)}}{\boldsymbol{X}^{(2)}}=\left(\begin{array}{c}
X_{1} \\
\vdots \\
X_{p}
\end{array}\right)
$$

Now let us assume that the $p$ variates have a joint normal distribution with mean vectors

$$
\mathscr{E} X^{(1)}=\mu^{(1)}, \quad \mathscr{E} X^{(2)}=\mu^{(2)},
$$

and covariance matrices

$$
\begin{aligned}
& \mathscr{E}\left(X^{(1)}-\mu^{(1)}\right)\left(X^{(1)}-\mu^{(1)}\right)^{\prime}=\Sigma_{11}, \\
& \mathscr{E}\left(X^{(2)}-\mu^{(2)}\right)\left(X^{(2)}-\mu^{(2)}\right)^{\prime}=\Sigma_{22}, \\
& \mathscr{E}\left(X^{(1)}-\mu^{(1)}\right)\left(X^{(2)}-\mu^{(2)}\right)^{\prime}=\Sigma_{12} .
\end{aligned}
$$

We say that the random vector $X$ has been partitioned in (8) into subvectors, that

$$
\mu=\binom{\mu^{(1)}}{\mu^{(2)}}
$$

has been partitioned similarly into subvectors, and that

$$
\Sigma=\left(\begin{array}{ll}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{array}\right)
$$

has been partitioned similarly into submatrices. Here $\boldsymbol{\Sigma}_{21}=\boldsymbol{\Sigma}_{12}^{\prime}$. (See Appendix, Section A.3.)

We shall show that $X^{(1)}$ and $X^{(2)}$ are independently normally distributed if $\Sigma_{12}=\Sigma_{21}^{\prime}=0$. Then

$$
\Sigma=\left(\begin{array}{cc}
\Sigma_{11} & 0 \\
0 & \Sigma_{22}
\end{array}\right) .
$$

Its inverse is

$$
\Sigma^{-1}=\left(\begin{array}{cc}
\Sigma_{11}^{-1} & 0 \\
0 & \Sigma_{22}^{-1}
\end{array}\right) .
$$

Thus the quadratic form in the exponent of $n(\boldsymbol{x} \mid \boldsymbol{\mu}, \Sigma)$ is

$$
\begin{aligned}
Q & =(x-\mu)^{\prime} \Sigma^{-1}(x-\mu) \\
& =\left[\left(x^{(1)}-\mu^{(1)}\right)^{\prime},\left(x^{(2)}-\mu^{(2)}\right)^{\prime}\right]\left(\begin{array}{cc}
\Sigma_{11}^{-1} & 0 \\
0 & \Sigma_{22}^{-1}
\end{array}\right)\binom{x^{(1)}-\mu^{(1)}}{x^{(2)}-\mu^{(2)}} \\
& =\left[\left(x^{(1)}-\mu^{(1)}\right)^{\prime} \Sigma_{11}^{-1},\left(x^{(2)}-\mu^{(2)}\right)^{\prime} \Sigma_{22}^{-1}\right]\binom{x^{(1)}-\mu^{(1)}}{x^{(2)}-\mu^{(2)}} \\
& =\left(x^{(1)}-\mu^{(1)}\right)^{\prime} \Sigma_{11}^{-1}\left(x^{(1)}-\mu^{(1)}\right)+\left(x^{(2)}-\mu^{(2)}\right)^{\prime} \Sigma_{22}^{-1}\left(r^{(2)}-\mu^{(2)}\right) \\
& =Q_{1}+Q_{2},
\end{aligned}
$$

say, where

$$
\begin{aligned}
& Q_{1}=\left(x^{(1)}-\mu^{(1)}\right)^{\prime} \Sigma_{11}^{-1}\left(x^{(1)}-\mu^{(1)}\right), \\
& Q_{2}=\left(x^{(2)}-\mu^{(2)}\right)^{\prime} \Sigma_{22}^{-1}\left(x^{(2)}-\mu^{(2)}\right) .
\end{aligned}
$$

Also we note that $|\Sigma|=\left|\Sigma_{11}\right| \cdot\left|\Sigma_{22}\right|$. The density of $X$ can be written

$$
\begin{aligned}
n(x \mid \boldsymbol{\mu}, \boldsymbol{\Sigma}) & =\frac{1}{(2 \pi)^{\frac{1}{2} p}|\boldsymbol{\Sigma}|^{\frac{1}{3}}} e^{-\frac{1}{2} Q} \\
& =\frac{1}{(2 \pi)^{\frac{1}{3} q}\left|\boldsymbol{\Sigma}_{\mathbf{I}}\right|^{\frac{1}{2}}} e^{-\frac{1}{2} Q_{1}} \cdot \frac{1}{(2 \pi)^{\frac{1}{2}(p-q)}\left|\boldsymbol{\Sigma}_{22}\right|^{\frac{1}{2}}} e^{-\frac{1}{2} Q_{2}} \\
& =n\left(x^{(1)} \mid \boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}_{11}\right) n\left(x^{(2)} \mid \boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}_{22}\right)
\end{aligned}
$$

The marginal density of $\boldsymbol{X}^{(1)}$ is given by the integral

$$
\begin{aligned}
\int_{-\infty}^{\infty} & \cdots \int_{-\infty}^{\infty} n(x \mid \boldsymbol{\mu}, \boldsymbol{\Sigma}) d x_{q+1} \cdots d x_{p} \\
& =n\left(x^{(1)} \mid \boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}_{11}\right) \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} n\left(x^{(2)} \mid \boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}_{22}\right) d x_{q+1} \cdots d x_{p} \\
& =n\left(x^{(1)} \mid \boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}_{11}\right)
\end{aligned}
$$

Thus the marginal distribution of $\boldsymbol{X}^{(1)}$ is $N\left(\boldsymbol{\mu}^{(1)}, \mathbf{\Sigma}_{11}\right)$; similarly the marginal distribution of $X^{(2)}$ is $N\left(\boldsymbol{\mu}^{(2)}, \Sigma_{22}\right)$. Thus the joint density of $X_{1}, \ldots, X_{p}$ is the product of the marginal density of $X_{1}, \ldots, X_{q}$ and the marginal density of $X_{q+1}, \ldots, X_{p}$, and therefore the two sets of variates are independent. Since the numbering of variates can always be done so that $X^{(1)}$ consists of any subset of the variates, we have proved the sufficiency in the following theorem:

Theorem 2.4.2. If $X_{1}, \ldots, X_{p}$ have a joint normal distribution, a necessary and sufficient condition for one subset of the random variables and the subset consisting of the remaining variables to be independent is that each covariance of a variable from one set and a variable from the other set is 0 .

The ne cessity follows from the fact that if $X_{1}$ is from one set and $X_{j}$ from the other, then for any density (see Section 2.2.3)

$$
\begin{aligned}
\sigma_{i_{j}}= & \mathscr{E}\left(X_{i}-\mu_{t}\right)\left(X_{j}-\mu_{j}\right) \\
= & \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty}\left(x_{i}-\mu_{l}\right)\left(x_{j}-\mu_{j}\right) f\left(x_{1}, \ldots, x_{q}\right) \\
& \cdot f\left(x_{q+1}, \ldots, x_{p}\right) d x_{1} \cdots d x_{p} \\
= & \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty}\left(x_{i}-\mu_{t}\right) f\left(x_{1}, \ldots, x_{q}\right) d x_{1} \cdots d x_{q} \\
& \cdot \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty}\left(x_{j}-\mu_{j}\right) f\left(x_{q+1}, \ldots, x_{p}\right) d x_{q+1} \cdots d x_{p} \\
= & 0 .
\end{aligned}
$$

Since $\sigma_{i j}=\sigma_{i} \sigma_{j} \rho_{i j}$, and $\sigma_{i}, \sigma_{j} \neq 0$ (we tacitly assume that $\mathbf{\Sigma}$ is nonsingular), the condition $\sigma_{i j}=0$ is equivalent to $\rho_{t j}=0$. Thus if one set of variates is uncorrelated with the remaining variates, the two sets are independent. It should be emphasized that the implication of independence by lack of correlation depends on the assumption of normality, but the converse is always true.

Let us consider the special case of the bivariate normal distribution. Then $\boldsymbol{X}^{(1)}=X_{1}, \quad \boldsymbol{X}^{(2)}=X_{2}, \quad \boldsymbol{\mu}^{(1)}=\mu_{1}, \quad \boldsymbol{\mu}^{(2)}=\mu_{2}, \quad \boldsymbol{\Sigma}_{11}=\sigma_{11}=\sigma_{1}^{2}, \quad \boldsymbol{\Sigma}_{22}=\sigma_{22}=\sigma_{2}^{2}$, and $\Sigma_{12}=\Sigma_{21}=\sigma_{12}=\sigma_{1} \sigma_{2} \rho_{12}$. Thus if $X_{1}$ and $X_{2}$ have a bivariate normal distribution, they are independent if and only if they are uncorrelated. If they are uncorrelated, the marginal distribution of $X_{i}$ is normal with mean $\mu_{i}$ and variance $\sigma_{i}{ }^{2}$. The above discussion also proves the following corollary:

Corollary 2.4.1. If $X$ is distributed according to $N(\mu, \Sigma)$ and if a set of components of $X$ is uncorrelated with the other components, the marginal distribution of the set is multivariate normal with means, variances, and covariances obtained by taking the corresponding components of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$, respectively.

Now let us show that the corollary holds even if the two sets are not independent. We partition $\boldsymbol{X}, \boldsymbol{\mu}$, and $\boldsymbol{\Sigma}$ as before. We shall make a nonsingular linear transformation to subvectors

$$
\begin{aligned}
& Y^{(1)}=X^{(1)}+B X^{(2)}, \\
& Y^{(2)}=X^{(2)},
\end{aligned}
$$

choosing $B$ so that the components of $\boldsymbol{Y}^{(1)}$ are uncorrelated with the
components of $Y^{(2)}=X^{(2)}$. The matrix $B$ must satisfy the equation

$$
\begin{aligned}
0 & =\mathscr{E}\left(Y^{(1)}-\mathscr{E} Y^{(1)}\right)\left(Y^{(2)}-\mathscr{E} Y^{(2)}\right)^{\prime} \\
& =\mathscr{E}\left(X^{(1)}+E X^{(2)}-\mathscr{E} X^{(1)}-B \mathscr{E} X^{(2)}\right)\left(X^{(2)}-\mathscr{E} X^{(2)}\right)^{\prime} \\
& =\mathscr{E}\left[\left(X^{(1)}-\mathscr{E} X^{(1)}\right)+B\left(X^{(2)}-\mathscr{E} X^{(2)}\right)\right]\left(X^{(2)}-\mathscr{E} X^{(2)}\right)^{\prime} \\
& =\Sigma_{12}+B \Sigma_{22} .
\end{aligned}
$$

Thus $B=-\Sigma_{12} \Sigma_{22}^{-1}$ and

$$
Y^{(1)}=X^{(1)}-\Sigma_{12} \Sigma_{22}^{-1} X^{(2)} .
$$

The vector

$$
\binom{Y^{(1)}}{Y^{(2)}}=Y=\left(\begin{array}{cc}
I & -\Sigma_{12} \Sigma_{22}^{-1} \\
0 & I
\end{array}\right) X
$$

is a nonsingular transform of $X$, and therefore has a normal distribution with

$$
\begin{aligned}
\mathscr{E}\binom{Y^{(1)}}{Y^{(2)}} & =\mathscr{E}\left(\begin{array}{cc}
I & -\Sigma_{12} \Sigma_{22}^{-1} \\
0 & I
\end{array}\right) X \\
& =\left(\begin{array}{cc}
I & -\Sigma_{12} \Sigma_{22}^{-1} \\
0 & I
\end{array}\right)\binom{\mu^{(1)}}{\mu^{(2)}} \\
& =\binom{\mu^{(1)}-\Sigma_{12} \Sigma_{22}^{-1} \mu^{(2)}}{\mu^{(2)}}=\binom{v^{(1)}}{v^{(2)}} \\
& =v,
\end{aligned}
$$

say, and

$$
\begin{aligned}
\mathscr{C}(Y) & =\mathscr{E}(Y-v)(Y-v)^{\prime} \\
& =\left(\begin{array}{cc}
\mathscr{E}\left(Y^{(1)}-v^{(1)}\right)\left(Y^{(1)}-v^{(1)}\right)^{\prime} & \mathscr{E}\left(Y^{(1)}-v^{(1)}\right)\left(Y^{(2)}-v^{(2)}\right)^{\prime} \\
\mathscr{E}\left(Y^{(2)}-v^{(2)}\right)\left(Y^{(1)}-v^{(1)}\right)^{\prime} & \mathscr{E}\left(Y^{(2)}-v^{(2)}\right)\left(Y^{(2)}-v^{(2)}\right)^{\prime}
\end{array}\right) \\
& =\left(\begin{array}{cc}
\Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} & 0 \\
0 & \Sigma_{22}
\end{array}\right)
\end{aligned}
$$

since

$$
\begin{aligned}
& \mathscr{E}\left(Y^{(1)}-\nu^{(1)}\right)\left(Y^{(1)}-\nu^{(1)}\right)^{\prime} \\
&= \mathscr{E}\left[\left(X^{(1)}-\mu^{(1)}\right)-\Sigma_{12} \Sigma_{22}^{-1}\left(X^{(2)}-\mu^{(2)}\right)\right] \\
& \cdot\left[\left(X^{(1)}-\mu^{(1)}\right)-\Sigma_{12} \Sigma_{22}^{-1}\left(X^{(2)}-\mu^{(2)}\right)\right]^{\prime} \\
&= \Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}+\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{22} \Sigma_{22}^{-1} \Sigma_{21} \\
&= \Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}
\end{aligned}
$$

Thus $Y^{(1)}$ and $Y^{(2)}$ are independent, and by Corollary 2.4.1 $X^{(2)}=Y^{(2)}$ has the marginal distribution $N\left(\boldsymbol{\mu}^{(2)}, \Sigma_{22}\right)$. Because the numbering of the components of $X$ is arbitrary, we can state the following theorem:

Theorem 2.4.3. If $X$ is distributed according to $N(\mu, \Sigma)$, the marginal distribution of any set of components of $\boldsymbol{X}$ is multivariate normal with means, variances, and covariances obtained by taking the corresponding components of $\mu$ and $\Sigma$, respectively.

Now consider any transformation

$$
Z=D X
$$

where $\boldsymbol{Z}$ has $q$ components and $\boldsymbol{D}$ is a $q \times p$ real matrix. The expected value of $\boldsymbol{Z}$ is

$$
\mathscr{E} Z=D \mu
$$

and the covariance matrix is

$$
\mathscr{E}(Z-D \mu)(Z-D \mu)^{\prime}=D \Sigma D^{\prime}
$$

The case $q=p$ and $D$ nonsingular has been treated above. If $q \leq p$ and $D$ is of rank $q$, we can find a $(p-q) \times p$ matrix $E$ such that

$$
\binom{\boldsymbol{Z}}{W}=\binom{D}{E} X
$$

is a nonsingular transformation. (See Appendix, Section A.3.) Then $\boldsymbol{Z}$ and $\boldsymbol{W}$ have a joint normal distribution, and $\boldsymbol{Z}$ has a marginal normal distribution by Theorem 2.4.3. Thus for $D$ of rank $q$ (and $X$ having a nonsingular distribution, that is, a density) we have proved the following theorem:

Theorem 2.4.4. If $X$ is distributed according to $N(\mu, \Sigma)$, then $Z=D X$ is distributed according to $N\left(D \boldsymbol{\mu}, \boldsymbol{D} \boldsymbol{\Sigma} \boldsymbol{D}^{\prime}\right)$, where $\boldsymbol{D}$ is a $q \times p$ matrix of rank $q \leq p$.

The remainder of this section is devoted to the singular or degenerate normal distribution and the extension of Theorem 2.4.4 to the case of any matrix $D$. A singular distribution is a distribution in $p$-space that is concentrated on a lower dimensional set; that is, the probability associated with any set not intersecting the given set is 0 . In the case of the singular normal distribution the mass is concentrated on a given linear set [that is, the intersection of a number of ( $p-1$ )-dimensional hyperplanes]. Let $y$ be a set of coordinates in the linear set (the number of coordinates equaling the dimensionality of the linear set); then the parametric definition of the linear set can be given as $\boldsymbol{x}=\boldsymbol{A} \boldsymbol{y}+\boldsymbol{\lambda}$, where $\boldsymbol{A}$ is a $p \times q$ matrix and $\boldsymbol{\lambda}$ is a $p$-vector. Suppose that $Y$ is normally distributed in the $q$-dimensional linear set; then we say that

$$
X=A Y+\lambda
$$

has a singular or degenerate normal distribution in $p$-space. If $\mathscr{E} Y=\boldsymbol{\nu}$, then $\mathscr{E} X=A \nu+\lambda=\mu$, say. If $\mathscr{E}(Y-\nu)(Y-\nu)^{\prime}=T$, then

$$
\mathscr{E}(X-\mu)(X-\mu)^{\prime}=\mathscr{E} A(Y-\nu)(Y-\nu)^{\prime} A^{\prime}=A T A^{\prime}=\Sigma,
$$

say. It should be noticed that if $p>q$, then $\Sigma$ is singular and therefore has no inverse, and thus we cannot write the normal density for $\boldsymbol{X}$. In fact, $\boldsymbol{X}$ cannot have a density at all, because the fact that the probability of any set not intersecting the $q$-set is 0 would imply that the density is 0 almost everywhere.

Now. conversely, let us see that if $X$ has mean $\mu$ and covariance matrix $\Sigma$ of rank $r$, it can be written as (34) (except for 0 probabilities), where $X$ has an arbitrary distribution, and $\boldsymbol{Y}$ of $r(\leq p)$ components has a suitable distribution. If $\mathbf{\Sigma}$ is of rank $r$, there is a $p \times p$ nonsingular matrix $\boldsymbol{B}$ such that

$$
\boldsymbol{B} \boldsymbol{\Sigma} \boldsymbol{B}^{\prime}=\left(\begin{array}{cc}
\boldsymbol{I}_{r} & 0 \\
0 & 0
\end{array}\right),
$$

where the identity is of order $r$. (See Theorem A.4.1 of the Appendix.) The transformation

$$
B X=V=\binom{V^{(1)}}{V^{(2)}}
$$

defines a random vector $V$ with covariance matrix (36) and a mean vector

$$
\mathscr{E} V=B \mu=\nu=\binom{\nu^{(1)}}{\nu^{(2)}},
$$

say. Since the variances of the elements of $V^{(2)}$ are zero, $V^{(2)}=\nu^{(2)}$ with probability 1. Now partition

$$
B^{-1}=\left(\begin{array}{ll}
C & D
\end{array}\right),
$$

where $\boldsymbol{C}$ consists of $r$ columns. Then (37) is equivalent to

$$
X=B^{-1} V=\left(\begin{array}{ll}
C & D
\end{array}\right)\binom{V^{(1)}}{V^{(2)}}=C V^{(1)}+D V^{(2)} .
$$

Thus with probability 1

$$
X=C V^{(1)}+D \nu^{(2)},
$$

which is of the form of (34) with $\boldsymbol{C}$ as $\boldsymbol{A}, \boldsymbol{V}^{(1)}$ as $\boldsymbol{Y}$, and $\boldsymbol{D} \boldsymbol{\nu}^{(2)}$ as $\boldsymbol{\lambda}$.
Now we give a formal definition of a normal distribution that includes the singular distribution.

Definition 2.4.1. A random vector $X$ of $p$ components with $\mathscr{E} \boldsymbol{X}=\boldsymbol{\mu}$ and $\mathscr{E}(\boldsymbol{X}-\boldsymbol{\mu})(\boldsymbol{X}-\boldsymbol{\mu})^{\prime}=\boldsymbol{\Sigma}$ is said to be normally distributed [or is said to be distributed according to $N(\mu, \Sigma)]$ if there is a transformation (34), where the number of rows of $A$ is $p$ and the number of columns is the rank of $\Sigma$, say $r$, and $Y$ (of $r$ components) has a nonsingular normal distribution, that is, has a density

$$
k e^{-\frac{1}{2}(y-v)^{\prime} T^{-1}(y-v)} .
$$

It is clear that if $\Sigma$ has rank $p$, then $A$ can be taken to be $I$ and $\lambda$ to be $\mathbf{0}$; then $X=Y$ and Definition 2.4.1 agrees with Section 2.3. To avoid redundancy in Definition 2.4.1 we could take $\boldsymbol{T}=\boldsymbol{I}$ and $\boldsymbol{\nu}=\mathbf{0}$.

Theorem 2.4.5. If $\boldsymbol{X}$ is distributed according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, then $\boldsymbol{Z}=\boldsymbol{D} \boldsymbol{X}$ is distributed according to $N\left(D \mu, D \Sigma D^{\prime}\right)$.

This theorem includes the cases where $X$ may have a nonsingular or a singular distribution and $D$ may be nonsingular or of rank less than $q$. Since $X$ can be represented by (34), where $Y$ has a nonsingular distribution
$N(\boldsymbol{v}, \boldsymbol{T})$, we can write

$$
Z=D A Y+D \lambda,
$$

where $D A$ is $q \times r$. If the rank of $D A$ is $r$, the theorem is proved. If the rank is less than $r$, say $s$, then the covariance matrix of $Z$,

$$
D A T A^{\prime} D^{\prime}=E
$$

say, is of rank $s$. By Theorem A.4.1 of the Appendix, there is a nonsingular matrix

$$
\boldsymbol{F}=\binom{\boldsymbol{F}_{1}}{\boldsymbol{F}_{2}}
$$

such that

$$
\begin{aligned}
F E F^{\prime} & =\left(\begin{array}{ll}
F_{1} E F_{1}^{\prime} & F_{1} E F_{2}^{\prime} \\
F_{2} E F_{1}^{\prime} & F_{2} E F_{2}^{\prime}
\end{array}\right) \\
& =\left(\begin{array}{ll}
\left(F_{1} D A\right) T\left(F_{1} D A\right)^{\prime} & \left(F_{1} D A\right) T\left(F_{2} D A\right)^{\prime} \\
\left(F_{2} D A\right) T\left(F_{1} D A\right)^{\prime} & \left(F_{2} D A\right) T\left(F_{2} D A\right)^{\prime}
\end{array}\right)=\left(\begin{array}{cc}
I_{s} & 0 \\
0 & 0
\end{array}\right) .
\end{aligned}
$$

Thus $F_{1} D A$ is of rank $s$ (by the converse of Theorem A.1.1 of the Appendix), and $\boldsymbol{F}_{2} \boldsymbol{D} \boldsymbol{A}=\mathbf{0}$ because each diagonal element of $\left(\boldsymbol{F}_{2} \boldsymbol{D} \boldsymbol{A}\right) \boldsymbol{T}\left(\boldsymbol{F}_{2} \boldsymbol{D A}\right)^{\prime}$ is à quadratic form in a row of $\boldsymbol{F}_{2} D A$ with positive definite matrix $\boldsymbol{T}$. Thus the covariance matrix of $\boldsymbol{F} \boldsymbol{Z}$ is (46), and

$$
F Z=\binom{F_{1}}{F_{2}} D A Y+F D \lambda=\binom{F_{1} D A Y}{0}+F D \lambda=\binom{U_{1}}{0}+F D \lambda,
$$

say. Clearly $\boldsymbol{U}_{\mathbf{1}}$ has a nonsingular normal distribution. Let $\boldsymbol{F}^{-\mathbf{1}}=\left(\begin{array}{ll}\boldsymbol{G}_{1} & \boldsymbol{G}_{2}\end{array}\right)$. Then

$$
Z=G_{1} U_{1}+D \lambda,
$$

which is of the form (34).
The developments in this section can be illuminated by considering the geometric interpretation put forward in the previous section. The density of $\boldsymbol{X}$ is constant on the ellipsoids (54) of Section 2.3. Since the transformation (2) is a linear transformation (i.e., a change of coordinate axes), the density of



$Y$ is constant on ellipsoids

$$
(y-C \mu)^{\prime}\left(C \Sigma C^{\prime}\right)^{-1}(y-C \mu)=k .
$$

The marginal distribution of $X^{(1)}$ is the projection of the mass of the distribution of $X$ onto the $q$-dimensional space of the first $q$ coordinate axes. The surfaces of constant density are again ellipsoids. The projection of mass on any line is normal.

### 2.5. CONDITIONAL DISTRIBUTIONS AND MULTIPLE CORRELATION COEFFICIENT

### 2.5.1. Conditional Distributions

In this section we find that conditional distributions derived from joint normal distribution are normal. The conditional distributions are of a particularly simple nature because the means depend only linearly on the variates held fixed, and the variances and covariances do not depend at all on the values of the fixed variates. The theory of partial and multiple correlation discussed in this section was originally developed by Karl Pearson (1896) for three variables and exiended by Yule (1897 $\hat{a}, 1897 \mathrm{~b}$ ).

Let $\boldsymbol{X}$ be distributed according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ (with $\boldsymbol{\Sigma}$ nonsingular). Let us partition

$$
\boldsymbol{X}=\binom{\boldsymbol{X}^{(1)}}{\boldsymbol{X}^{(2)}}
$$

as before into $q$ - and ( $p-q$ )-component subvectors, respectively. We shall use the algebra developed in Section 2.4 here. The joint density of $\boldsymbol{Y}^{(\mathbf{1})}=\boldsymbol{X}^{(\mathbf{1})} -\Sigma_{12} \Sigma_{22}^{-1} X^{(2)}$ and $Y^{(2)}=X^{(2)}$ is

$$
n\left(y^{(1)} \mid \mu^{(1)}-\Sigma_{12} \Sigma_{22}^{-1} \mu^{(2)}, \Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}\right) n\left(y^{(2)} \mid \mu^{(2)}, \Sigma_{22}\right) .
$$

The density of $X^{(1)}$ and $X^{(2)}$ then can be obtained from this expression by substituting $x^{(1)}-\Sigma_{12} \Sigma_{22}^{-1} x^{(2)}$ for $y^{(1)}$ and $x^{(2)}$ for $y^{(2)}$ (the Jacobian of this transformation being 1); the resulting density of $X^{(1)}$ and $X^{(2)}$ is

$$
\begin{array}{r}
f\left(x^{(1)}, x^{(2)}\right)=\frac{1}{(2 \pi)^{\frac{1}{2} q} \sqrt{\left|\Sigma_{11 \cdot 2}\right|}} \exp \left\{-\frac{1}{2}\left[\left(x^{(1)}-\mu^{(1)}\right)-\Sigma_{12} \Sigma_{22}^{-1}\left(x^{(2)}-\mu^{(2)}\right)\right]^{\prime}\right. \\
\left.\cdot \Sigma_{11 \cdot 2}^{-1}\left[\left(x^{(1)}-\mu^{(1)}\right)-\Sigma_{12} \Sigma_{22}^{-1}\left(x^{(2)}-\mu^{(2)}\right)\right]\right\} \\
\cdot \frac{1}{(2 \pi)^{\frac{1}{2}(p-q)} \sqrt{\left|\Sigma_{22}\right|}} \exp \left[-\frac{1}{2}\left(x^{(2)}-\mu^{(2)}\right)^{\prime} \Sigma_{22}^{-1}\left(x^{(2)}-\mu^{(2)}\right)\right],
\end{array}
$$

where

$$
\Sigma_{11 \cdot 2}=\Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} .
$$

This density must be $n(x \mid \boldsymbol{\mu}, \boldsymbol{\Sigma})$. The conditional density of $\boldsymbol{X}^{(1)}$ given that $X^{(2)}=x^{(2)}$ is the quotient of (2) and the marginal density of $X^{(2)}$ at the point $x^{(2)}$, which is $n\left(x^{(2)} \mid \mu^{(2)}, \Sigma_{22}\right)$, the second factor of (2). The quotient is
(4)

$$
\begin{aligned}
& f\left(x^{(1)} \mid x^{(2)}\right)=\frac{1}{(2 \pi)^{\frac{1}{2} q} \sqrt{\left|\Sigma_{11 \cdot 2}\right|}} \exp \left(-\frac{1}{2}\left[\left(x^{(1)}-\mu^{(1)}\right)-\Sigma_{12} \Sigma_{22}^{-1}\left(x^{(2)}-\mu^{(2)}\right)\right]\right. \\
&\left.\cdot \Sigma_{11 \cdot 2}^{-1}\left[\left(x^{(1)}-\mu^{(1)}\right)-\Sigma_{12} \Sigma_{22}^{-1}\left(x^{(2)}-\mu^{(2)}\right)\right]\right\} .
\end{aligned}
$$

It is understood that $x^{(2)}$ consists of $p-q$ numbers. The density $f\left(\boldsymbol{x}^{(1)} \mid \boldsymbol{x}^{(2)}\right)$ is a $q$-variate normal density with mean

$$
\mathscr{E}\left(X^{(1)} \mid x^{(2)}\right)=\mu^{(1)}+\Sigma_{12} \Sigma_{22}^{-1}\left(x^{(2)}-\mu^{(2)}\right)=\nu\left(x^{(2)}\right),
$$

say. and covariance matrix

$$
\mathscr{E}\left\{\left[X^{(1)}-v\left(x^{(2)}\right)\right]\left[X^{(1)}-v\left(x^{(2)}\right)\right]^{\prime} \mid x^{(2)}\right\}=\Sigma_{11,2}=\Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} .
$$

It should be noted that the mean of $X^{(1)}$ given $x^{(2)}$ is simply a linear function of $x^{(2)}$. and the covariance matrix of $X^{(1)}$ given $x^{(2)}$ does not depend on $x^{(2)}$ at all.

Definition 2.5.1. The matrix $\mathbf{\beta}=\mathbf{\Sigma}_{12} \mathbf{\Sigma}_{22}^{-1}$ is the matrix of regression coefficients of $X^{(1)}$ on $\boldsymbol{x}^{(2)}$.

The element in the $i$ th row and $(k-q)$ th column of $\mathbf{\beta}=\mathbf{\Sigma}_{12} \mathbf{\Sigma}_{22}^{-1}$ is often denoted by

$$
\beta_{1 k} q+1 \ldots k-1 . k+1 \ldots p, \quad i=1, \ldots, q, \quad k=q+1, \ldots, p .
$$

The vector $\boldsymbol{\mu}^{(1)}+\boldsymbol{\beta}\left(x^{(2)}-\boldsymbol{\mu}^{(2)}\right)$ is called the regression function.
Let $\sigma_{1,4+1} ., p$ be the $i, j$ th element of $\Sigma_{11,2}$. We call these partial covanances, $\sigma_{n q+1}, p$ is a partial variance.

## Definition 2.5.2

$$
\rho_{1 j q+1, \ldots p}=\frac{\sigma_{1 j q+1, \ldots p}}{\sqrt{\sigma_{1 q q+1, \ldots p}} \sqrt{\sigma_{j q+1, \ldots p}}}, \quad i, j=1, \ldots, q,
$$

is the partial correlation between $X_{1}$ and $X_{j}$ holding $X_{q+1}, \ldots, X_{p}$ fixed.

The numbering of the components of $X$ is arbitrary and $q$ is arbitrary. Hence, the above serves to define the conditional distribution of any $q$ components of $\boldsymbol{X}$ given any other $p-q$ components. In the case of partial covariances and correlations the conditioning variables are indicated by the. subscripts after the dot, and in the case of regression coefficients the dependent variable is indicated by the first subscript, the relevant conditioning variable by the second subscript, and the other conditioning variables by the subscripts after the dot. Further, the notation accommodates the conditional distribution of any $q$ variables conditional on any other $r-q$ variables $(q \leq r \leq p)$.

Theorem 2.5.1. Let the components of $\boldsymbol{X}$ be divided into two groups composing the subvectors $\boldsymbol{X}^{(1)}$ and $\boldsymbol{X}^{(2)}$. Suppose the mean $\boldsymbol{\mu}$ is similarly divided into $\boldsymbol{\mu}^{(1)}$ and $\boldsymbol{\mu}^{(2)}$, and suppose the covariance matrix $\boldsymbol{\Sigma}$ of $\boldsymbol{X}$ is divided into $\boldsymbol{\Sigma}_{11}, \boldsymbol{\Sigma}_{12}, \boldsymbol{\Sigma}_{22}$, the covariance matrices of $\boldsymbol{X}^{(1)}$, of $\boldsymbol{X}^{(1)}$ and $\boldsymbol{X}^{(2)}$, and of $\boldsymbol{X}^{(2)}$, respectively. Then if the distribution of $\boldsymbol{X}$ is normal, the conditional distribution of $X^{(1)}$ given $X^{(2)}=x^{(2)}$ is normal with mean $\mu^{(1)}+\Sigma_{12} \Sigma_{22}^{-1}\left(x^{(2)}-\mu^{(2)}\right)$ and covariance matrix $\Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}$.

As an example of the above considerations let us consider the bivariate normal distribution and find the conditional distribution of $X_{1}$ given $X_{2}=x_{2}$. In this case $\boldsymbol{\mu}^{(1)}=\mu_{1}, \boldsymbol{\mu}^{(2)}=\mu_{2}, \boldsymbol{\Sigma}_{11}=\sigma_{1}^{2}, \boldsymbol{\Sigma}_{12}=\sigma_{1} \sigma_{2} \rho$, and $\boldsymbol{\Sigma}_{22}=\sigma_{2}^{2}$. Thus the $1 \times 1$ matrix of regression coefficients is $\Sigma_{12} \Sigma_{22}^{-1}=\sigma_{1} \rho / \sigma_{2}$, and the $1 \times 1$ matrix of partial covariances is

$$
\mathbf{\Sigma}_{11 \cdot 2}=\mathbf{\Sigma}_{11}-\mathbf{\Sigma}_{12} \mathbf{\Sigma}_{22}^{-1} \mathbf{\Sigma}_{21}=\sigma_{1}^{2}-\sigma_{1}^{2} \sigma_{2}^{2} \rho^{2} / \sigma_{2}^{2}=\sigma_{1}^{2}\left(1-\rho^{2}\right) .
$$

The density of $X_{1}$ given $x_{2}$ is $n\left[x_{1} \mid \mu_{1}+\left(\sigma_{1} \rho / \sigma_{2}\right)\left(x_{2}-\mu_{2}\right), \sigma_{1}^{2}\left(1-\rho^{2}\right)\right]$. The mean of this conditional distribution increases with $x_{2}$ when $\rho$ is positive and decreases with increasing $x_{2}$ when $\rho$ is negative. It may be noted that when $\sigma_{1}=\sigma_{2}$, for example, the mean of the conditional distribution of $x_{1}$ does not increase relative to $\mu_{1}$ as much as $x_{2}$ increases relative to $\mu_{2}$. [Galton (1889) observed that the average heights of sons whose fathers' heights were above average tended to be less than the fathers' heights; he called this effect "regression towards mediocrity."] The larger $|\rho|$ is, the smaller the variance of the conditional distribution, that is, the more information $x_{2}$ gives about $x_{1}$. This is another reason for considering $\rho$ a measure of association between $X_{1}$ and $X_{2}$.

A geometrical interpretation of the theory is enlightening. The density $f\left(x_{1}, x_{2}\right)$ can be thought of as a surface $z=f\left(x_{1}, x_{2}\right)$ over the $x_{1}, x_{2}$-plane. If we intersect this surface with the plane $x_{2}=c$, we obtain a curve $z=f\left(x_{1}, c\right)$ over the line $x_{2}=c$ in the $x_{1}, x_{2}$-plane. The ordinate of this curve is
proportional to the conditional density of $X_{1}$ given $x_{2}=c$; that is, it is proportional to the ordinate of the curve of a univariate normal distribution. In the more general case it is convenient to consider the ellipsoids of constant density in the $p$-dimensional space. Then the surfaces of constant density of $f\left(x_{1}, \ldots, x_{q} \mid c_{q+1}, \ldots, c_{p}\right)$ are the intersections of the surfaces of constant density of $f\left(x_{1}, \ldots, x_{p}\right)$ and the hyperplanes $x_{q+1}=c_{q+1}, \ldots, x_{p}= c_{p}$; these are again ellipsoids.

Further clarification of these ideas may be had by consideration of an actual population which is idealized by a normal distribution. Consider, for example, a population of father-son pairs. If the population is reasonably homogeneous, the heights of fathers and the heights of corresponding sons have approximately a normal distribution (over a certain range). A conditional distribution may be obtained by considering sons of all fataters whose height is, say, 5 feet, 9 inches (to the accuracy of measurement); the heights of these sons will have an approximate univariate normal distribution. The mean of this normal distribution will differ from the mean of the heights of sons whose fathers' heights are 5 feet, 4 inches, say, but the variances will be about the same.

We could also consider triplets of observations, the height of a father, height of the oldest son, and height of the next oldest son. The collection of heights of two sons given that the fathers' heights are 5 feet, 9 inches is a conditional distribution of two variables; the correlation between the heights of oldest and next oldest sons is a partial correlation coefficient. Holding the fathers' heights constant eliminates the effect of heredity from fathers; however, one would expect that the partial correlation coefficient would be positive, since the effect of mothers' heredity and environmental factors would tend to cause brothers' heights to vary similarly.

As we have remarked above, any conditional distribution obtained from a normal distribution is normal with the mean a linear function of the variables held fixed and the covariance matrix constant. In the case of nonnormal distributions the conditional distribution of one set of variates oil another does not usually have these properties. However, one can construct nonnormal distributions such that some conditional distributions have these properties. This can be done by taking as the density of $\boldsymbol{X}$ the product $\boldsymbol{n}\left[\boldsymbol{x}^{(1)} \mid \boldsymbol{\mu}^{(1)}+\right. \left.\mathbf{B}\left(x^{(2)}-\boldsymbol{\mu}^{(2)}\right), \Sigma_{11 \cdot 2}\right] f\left(x^{(2)}\right)$, whicre $f\left(x^{(2)}\right)$ is an arbitrary density.

### 2.5.2. The Multiple Correlation Coefficient

We again consider $X$ partitioned into $X^{(1)}$ and $X^{(2)}$. We shall study some properties of $B X^{(2)}$.

Definition 2.5.3. The vector $X^{(1 \cdot 2)}=X^{(1)}-\mu^{(1)}-\mathrm{B}\left(X^{(2)}-\mu^{(2)}\right)$ is the vector of residuals of $X^{(1)}$ from its regression on $X^{(2)}$.

Theorem 2.5.2. The components of $\boldsymbol{X}^{(1 \cdot 2)}$ are uncorrelated with the components of $X^{(2)}$.

Proof. The vector $X^{(1 \cdot 2)}$ is $Y^{(1)}-\mathscr{E} Y^{(1)}$ in (25) of Section 2.4.
Let $\boldsymbol{\sigma}_{(i)}^{\prime}$ be the $i$ th row of $\boldsymbol{\Sigma}_{12}$, and $\boldsymbol{\beta}_{(i)}^{\prime}$ the ith row of $\boldsymbol{\beta}$ (i.e., $\boldsymbol{\beta}_{(i)}^{\prime}= \left.\sigma_{(i)}^{\prime} \Sigma_{22}^{-1}\right)$. Let $\mathscr{V}(Z)$ be the variance of $Z$.

Theorem 2.5.3. For every vector $\boldsymbol{\alpha}$

$$
\mathscr{V}\left(X_{i}^{(1-2)}\right) \leq \mathscr{V}\left(X_{i}-\alpha^{\prime} X^{(2)}\right) .
$$

Proof. By Theorem 2.5.2

$$
\begin{aligned}
& \mathscr{V}\left(X_{i}-\alpha^{\prime} X^{(2)}\right) \\
& \quad=\mathscr{E}\left[X_{i}-\mu_{i}-\alpha^{\prime}\left(X^{(2)}-\mu^{(2)}\right)\right]^{2} \\
& \quad=\mathscr{E}\left[X_{i}^{(1 \cdot 2)}-\mathscr{E} X_{i}^{(1 \cdot 2)}+\left(\beta_{(1)}-\alpha\right)^{\prime}\left(X^{(2)}-\mu^{(2)}\right)\right]^{2} \\
& \quad=\mathscr{V}\left[X_{i}^{(1 \cdot 2)}\right]+\left(\beta_{(1)}-\alpha\right)^{\prime} \mathscr{E}\left(X^{(2)}-\mu^{(2)}\right)\left(X^{(2)}-\mu^{(2)}\right)^{\prime}\left(\beta_{(i)}-\alpha\right) \\
& \quad=\mathscr{V}\left(X_{i}^{(1 \cdot 2)}\right)+\left(\beta_{(1)}-\alpha\right)^{\prime} \Sigma_{22}\left(\beta_{(i)}-\alpha\right)
\end{aligned}
$$

Since $\Sigma_{22}$ is positive definite, the quadratic form in $\beta_{(i)}-\alpha$ is nonnegative and attains its minimum of 0 at $\alpha=\beta_{(i)}$.

Since $\mathscr{E} \boldsymbol{X}^{(1 \cdot 2)}=\mathbf{0}, \mathscr{V}\left(X_{i}^{(1 \cdot 2)}\right)=\mathscr{E}\left(X_{i}^{(1 \cdot 2)}\right)^{2}$. Thus $\mu_{i}+\boldsymbol{\beta}_{(i)}^{\prime}\left(\boldsymbol{X}^{(2)}-\boldsymbol{\mu}^{(2)}\right)$ is the best linear predictor of $X_{i}$ in the sense that of all functions of $X^{(2)}$ of the form $\boldsymbol{a}^{\prime} \boldsymbol{X}^{(2)}+\boldsymbol{c}$, the mean squared error of the above is a minimum.

Theorem 2.5.4. For every vector $\boldsymbol{\alpha}$

$$
\operatorname{Corr}\left(X_{i}, \boldsymbol{\beta}_{(I)}^{\prime} \boldsymbol{X}^{(2)}\right) \geq \operatorname{Corr}\left(X_{i}, \boldsymbol{\alpha}^{\prime} \boldsymbol{X}^{(2)}\right) .
$$

Proof. Since the correlation between two variables is unchanged when either or both is multiplied by a positive constant, we can assume that
$\mathscr{E}\left[\boldsymbol{\alpha}^{\prime}\left(\boldsymbol{X}^{(2)}-\boldsymbol{\mu}^{(2)}\right)\right]^{2}=\mathscr{E}\left[\boldsymbol{\beta}_{(1)}^{\prime}\left(\boldsymbol{X}^{(2)}-\boldsymbol{\mu}^{(2)}\right)\right]^{2}$. Then the expansion of (10) is

$$
\begin{aligned}
& \sigma_{i i}-2 \mathscr{E}\left(X_{1}-\mu_{1}\right) \boldsymbol{\beta}_{(i)}^{\prime}\left(\boldsymbol{X}^{(2)}-\boldsymbol{\mu}^{(2)}\right)+\mathscr{V}\left(\boldsymbol{\beta}_{(i)}^{\prime} \boldsymbol{X}^{(2)}\right) \\
& \leq \sigma_{i i}-2 \mathscr{E}\left(X_{1}-\mu_{t}\right) \boldsymbol{\alpha}^{\prime}\left(\boldsymbol{X}^{(2)}-\boldsymbol{\mu}^{(2)}\right)+\mathscr{V}\left(\boldsymbol{\alpha}^{\prime} \boldsymbol{X}^{(2)}\right)
\end{aligned}
$$

This leads to

$$
\frac{\mathscr{E}\left(X_{i}-\mu_{1}\right) \boldsymbol{\beta}_{(1)}^{\prime}\left(X^{(2)}-\mu^{(2)}\right)}{\sqrt{\sigma_{\mathrm{i} 1}} \mathscr{V}\left(\boldsymbol{\beta}_{(1)}^{\prime} X^{(2)}\right)} \geq \frac{\mathscr{E}\left(X_{i}-\mu_{\mathrm{i}}\right) \boldsymbol{\alpha}^{\prime}\left(X^{(2)}-\mu^{(2)}\right)}{\sqrt{\sigma_{\mathrm{i} 1} \mathscr{V}\left(\boldsymbol{\alpha}^{\prime} X^{(2)}\right)}} .
$$

Definition 2.5.4. The maximum correlation between $X_{i}$ and the linear combination $\boldsymbol{\alpha}^{\prime} \boldsymbol{X}^{(2)}$ is called the multiple correlation coefficient between $X_{i}$ and $\boldsymbol{X}^{(2)}$.

It follows that this is

$$
\begin{aligned}
\bar{R}_{1 q+1, \ldots \ldots p} & =\frac{\mathscr{E} \beta_{(r)}^{\prime}\left(X^{(2)}-\mu^{(2)}\right)\left(X_{i}-\mu_{i}\right)}{\sqrt{\sigma_{i 1}} \sqrt{\mathscr{E} \beta_{(r)}^{\prime}\left(X^{(2)}-\mu^{(2)}\right)\left(X^{(2)}-\mu^{(2)}\right)^{\prime} \beta_{(i)}}} \\
& =\frac{\sigma_{(i)}^{\prime} \Sigma_{22}^{-1} \sigma_{(r)}}{\sqrt{\sigma_{i 1}} \sqrt{\sigma_{(i)}^{\prime} \Sigma_{22}^{-1} \sigma_{(1)}}}=\frac{\sqrt{\sigma_{(i)}^{\prime} \Sigma_{22}^{-I} \sigma_{(i)}}}{\sqrt{\sigma_{i 1}}}
\end{aligned}
$$

A useful formula is

$$
1-\bar{R}_{r q+1 \ldots p p}^{2}=\frac{\sigma_{i 1}-\boldsymbol{\sigma}_{(1)}^{r} \Sigma_{22}^{-1} \boldsymbol{\sigma}_{(1)}}{\sigma_{1 i}}=\frac{\left|\Sigma_{i}\right|}{\sigma_{i i}\left|\Sigma_{22}\right|}
$$

where Theorem A.3.2 of the Appendix has been applied to

$$
\Sigma_{1}=\left(\begin{array}{ll}
\sigma_{i 1} & \sigma_{(i)}^{\prime} \\
\sigma_{(11} & \Sigma_{22}
\end{array}\right)
$$

Since

$$
\sigma_{1 r q+1, \ldots p}=\sigma_{11}-\sigma_{(i)}^{\prime} \Sigma_{22}^{-1} \sigma_{(i)}
$$

it follows that

$$
\sigma_{i n q+1 \ldots . p}=\left(1-\bar{R}_{1 \cdot q+1 \ldots . p}^{2}\right) \sigma_{i r}
$$

This shows incidentally that any partial variance of a component of $\boldsymbol{X}$ cannot be greater than the variance. In fact, the larger $\bar{R}_{r, q+I, \ldots, p}$ is, the greater the
reduction in variance on going to the conditional distribution. This fact is another reason for considering the multiple correlation coefficient a measure of association between $X_{i}$ and $X^{(2)}$.

That $\boldsymbol{\beta}_{(1)}^{r} \boldsymbol{X}^{(2)}$ is the best linear predictor of $X_{i}$ and has the maximum correlation between $X_{i}$ and linear functions of $X^{(2)}$ depends only on the covariance structure, without regard to normality. Even if $X$ does not have a normal distribution, the regression of $X^{(1)}$ on $X^{(2)}$ can be defined by $\boldsymbol{\mu}^{(1)}+\boldsymbol{\Sigma}_{12} \boldsymbol{\Sigma}_{22}^{-1}\left(\boldsymbol{X}^{(2)}-\boldsymbol{\mu}^{(-1)}\right)$; the residuals can be defined by Definition 2.5.3; and partial covariances and correlations can be defined as the covariances and correlations of residuals yielding (3) and (8). Then these quantities do not necessarily have interpretations in terms of conditional distributions. In the case of normality $\mu_{i}+\boldsymbol{\beta}_{(i)}^{\prime}\left(\boldsymbol{x}^{(2)}-\boldsymbol{\mu}^{(2)}\right)$ is the conditional expectation of $X_{i}$ given $X^{(2)}=x^{(2)}$. Without regard to normality, $X_{i}-\mathscr{E} X_{i} \mid X^{(2)}$ is uncorrelated with any function of $X^{(2)}, \mathscr{E} X_{i} \mid X^{(2)}$ minimizes $\mathscr{E}\left[X_{i}-h\left(X^{(2)}\right)\right]^{2}$ with respect to functions $h\left(\boldsymbol{X}^{(2)}\right)$ of $\boldsymbol{X}^{(2)}$, and $\mathscr{E} X_{i} \mid \boldsymbol{X}^{(2)}$ maximizes the correlation between $X_{i}$ and functions of $X^{(2)}$. (See Problems 2.48 to 2.51.)

### 2.5.3 Some Formulas for Partial Correlations

We now consider relations between several conditional distributions obtained by holding several different sets of variates fixed. These relations are useful because they enable us to compute one set of conditional parameters from another set. A very special case is

$$
\rho_{12 \cdot 3}=\frac{\rho_{12}-\rho_{13} \rho_{23}}{\sqrt{1-\rho_{13}^{2}} \sqrt{1-\rho_{23}^{2}}} ;
$$

this follows from (8) when $p=3$ and $q=2$. We shall now find a generalization of this result. The derivation is tedious, but is given here for completeness.

Let

$$
\boldsymbol{X}=\left(\begin{array}{l}
\boldsymbol{X}^{(1)} \\
\boldsymbol{X}^{(2)} \\
\boldsymbol{X}^{(3)}
\end{array}\right),
$$

where $\boldsymbol{X}^{(1)}$ is of $p_{1}$ components, $\boldsymbol{X}^{(2)}$ of $p_{2}$ components, and $\boldsymbol{X}^{(3)}$ of $p_{3}$ components. Suppose we have the conditional distribution of $\boldsymbol{X}^{(1)}$ and $\boldsymbol{X}^{(2)}$ given $X^{(3)}=x^{(3)}$; how do we find the conditional distribution of $X^{(1)}$ given $X^{(2)}=x^{(2)}$ and $X^{(3)}=x^{(3)}$ ? We use the fact that the conditional density of $X^{(1)}$
given $X^{(2)}=x^{(2)}$ and $X^{(3)}=x^{(3)}$ is

$$
\begin{aligned}
f\left(x^{(1)} \mid x^{(2)}, x^{(3)}\right) & =\frac{f\left(x^{(1)}, x^{(2)}, x^{(3)}\right)}{f\left(x^{(2)}, x^{(3)}\right)} \\
& =\frac{f\left(x^{(1)}, x^{(2)}, x^{(3)}\right) / f\left(x^{(3)}\right)}{f\left(x^{(2)}, x^{(3)}\right) / f\left(x^{(3)}\right)} \\
& =\frac{f\left(x^{(1)}, x^{(2)} \mid x^{(3)}\right)}{f\left(x^{(2)} \mid x^{(3)}\right)} .
\end{aligned}
$$

In the case of normality the conditional covariance matrix of $X^{(1)}$ and $X^{(2)}$ giver $X^{(3)}=\boldsymbol{x}^{(3)}$ is

$$
\begin{aligned}
b\left[\left(X^{(1)}\right) \mid X^{(3)}\right] & =\left(\begin{array}{ll}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{array}\right)-\binom{\Sigma_{13}}{\Sigma_{23}} \Sigma_{33}^{-1}\left(\begin{array}{ll}
\Sigma_{31} & \Sigma_{32}
\end{array}\right) \\
& =\left(\begin{array}{ll}
\Sigma_{11 \cdot 3} & \Sigma_{12 \cdot 3} \\
\Sigma_{21 \cdot 3} & \Sigma_{22 \cdot 3}
\end{array}\right)
\end{aligned}
$$

say, where

$$
\Sigma=\left(\begin{array}{lll}
\Sigma_{11} & \Sigma_{12} & \Sigma_{13} \\
\Sigma_{21} & \Sigma_{22} & \Sigma_{23} \\
\Sigma_{31} & \Sigma_{32} & \Sigma_{33}
\end{array}\right) .
$$

The conditional covariance of $\boldsymbol{X}^{(1)}$ given $\boldsymbol{X}^{(2)}=x^{(2)}$ and $\boldsymbol{X}^{(3)}=x^{(3)}$ is calculated from the conditional covariances of $\boldsymbol{X}^{(1)}$ and $\boldsymbol{X}^{(2)}$ given $\boldsymbol{X}^{(3)}=\boldsymbol{x}^{(3)}$ as

$$
\mathscr{C}\left[X^{(1)} \mid x^{(2)}, x^{(3)}\right]=\Sigma_{11 \cdot 3}-\Sigma_{12 \cdot 3}\left(\Sigma_{22 \cdot 3}\right)^{-1} \Sigma_{21 \cdot 3} .
$$

This result permits the calculation of $\sigma_{i j p_{1}+1, \ldots, p}, i, j=1, \ldots, p_{1}$, from $\sigma_{i j, p_{1}+p_{2}, \ldots, p}, i, j=1, \ldots, p_{1}+p_{2}$.

In particular, for $p_{1}=q, p_{2}=1$, and $p_{3}=p-q-1$, we obtain

$$
\begin{aligned}
& \sigma_{i j \cdot q+1, \ldots, p}=\sigma_{1 j \cdot q+2, \ldots, p}-\frac{\sigma_{i, q+1 \cdot q+2, \ldots, p} \sigma_{j, q+1 \cdot q+2, \ldots, p}}{\sigma_{q+1, q+1 \cdot q+2, \ldots, p}}, \\
& \quad i, j=1, \ldots, q .
\end{aligned}
$$

Since

$$
\sigma_{i \cdot q+1, \ldots, p}=\sigma_{1 \cdot q+2, \ldots, p}\left(1-\rho_{i, q+1 \cdot q+2, \ldots, p}^{2}\right),
$$

we obtain

$$
\rho_{i j, q+1, \ldots, p}=\frac{\rho_{t, q+2, \ldots, p}-\rho_{1, q+1, q+2, \ldots, p} \rho_{j, q+1, q+2, \ldots, p}}{\sqrt{1-\rho_{1, q+1, q+2, \ldots, p}^{2}} \sqrt{1-\rho_{j, q+1, q+2, \ldots, p}^{2}}} .
$$

This is a useful recursion formula to compute from ( $\rho_{i j}$ ) in succession $\left\{\rho_{t / p}\right\},\left\{\rho_{t / p-1, p}\right\}, \ldots, \rho_{12 \cdot 3, \ldots, p}$.

### 2.6. THE CHARACTERISTIC FUNCTION; MOMENTS

### 2.6.1. The Characteristic Function

The characteristic function of a multivariate normal distribution has a form similar to the density function. From the characteristic function, moments and cumulants can be found easily.

Definition 2.6.1. The characteristic function of a random vector $X$ is

$$
\phi(t)=\mathscr{E} e^{i t^{\prime} X}
$$

defined for every real vector $t$.

- To make this definition meaningful we need to define the expected value of a complex-valued function of a random vector.

Definition 2.6.2. Let the complex-valued function $g(x)$ be written as $g(x) =g_{1}(x)+i g_{2}(x)$, where $g_{1}(x)$ and $g_{2}(x)$ are real-valued. Then the expected value of $g(X)$ is

$$
\mathscr{E} g(X)=\mathscr{E} g_{1}(X)+i \mathscr{E} g_{2}(X) .
$$

In particular, since $e^{i \theta}=\cos \theta+i \sin \theta$,

$$
\mathscr{E} e^{1 t^{\prime} X}=\mathscr{E} \cos t^{\prime} X+i \mathscr{E} \sin t^{\prime} X .
$$

To evaluate the characteristic function of a vector $X$, it is often convenient to use the following lemma:

Lemma 2.6.1. Let $X^{\prime}=\left(X^{(1) \prime} X^{(2) \prime}\right)$. If $X^{(1)}$ and $X^{(2)}$ are independent and $g(x)=g^{(1)}\left(x^{(1)}\right) g^{(2)}\left(x^{(2)}\right)$, then

$$
\mathscr{E} g(X)=\mathscr{E} g^{(1)}\left(X^{(1)}\right) \mathscr{E} g^{(2)}\left(X^{(2)}\right)
$$

Proof. If $g(x)$ is real-valued and $X$ has a density,

$$
\begin{aligned}
\mathscr{E} g(X)= & \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} g(x) f(x) d x_{1} \cdots d x_{p} \\
= & \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} g^{(1)}\left(x^{(1)}\right) g^{(2)}\left(x^{(2)}\right) f^{(1)}\left(x^{(1)}\right) f^{(2)}\left(x^{(2)}\right) d x_{1} \cdots d x_{p} \\
= & \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} g^{(1)}\left(x^{(1)}\right) f^{(1)}\left(x^{(1)}\right) d x_{1} \cdots d x_{q} \\
& \cdot \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} g^{(2)}\left(x^{(2)}\right) f^{(2)}\left(x^{(2)}\right) d x_{q+1} \cdots d x_{p} \\
= & \mathscr{E} g^{(1)}\left(X^{(1)}\right) \mathscr{E} g^{(2)}\left(X^{(2)}\right)
\end{aligned}
$$

If $g(x)$ is complex-valued,

$$
\begin{aligned}
g(x)= & {\left[g_{1}^{(1)}\left(x^{(1)}\right)+i g_{2}^{(1)}\left(x^{(1)}\right)\right]\left[g_{1}^{(2)}\left(x^{(2)}\right)+i g_{2}^{(2)}\left(x^{(2)}\right)\right] } \\
= & g_{1}^{(1)}\left(x^{(1)}\right) g_{1}^{(2)}\left(x^{(2)}\right)-g_{2}^{(1)}\left(x^{(1)}\right) g_{2}^{(2)}\left(x^{(2)}\right) \\
& +i\left[g_{2}^{(1)}\left(x^{(1)}\right) g_{1}^{(2)}\left(x^{(2)}\right)+g_{1}^{(1)}\left(x^{(1)}\right) g_{2}^{(2)}\left(x^{(2)}\right)\right]
\end{aligned}
$$

Then

$$
\begin{aligned}
\mathscr{E} g(X)= & \mathscr{E}\left[g_{1}^{(1)}\left(X^{(1)}\right) g_{1}^{(2)}\left(X^{(2)}\right)-g_{2}^{(1)}\left(X^{(1)}\right) g_{2}^{(2)}\left(X^{(2)}\right)\right] \\
& +i \mathscr{E}\left[g_{2}^{(1)}\left(X^{(1)}\right) g_{1}^{(2)}\left(X^{(2)}\right)+g_{1}^{(1)}\left(X^{(1)}\right) g_{2}^{(2)}\left(X^{(2)}\right)\right] \\
= & \mathscr{E} g_{1}^{(1)}\left(X^{(1)}\right) \mathscr{E} g_{1}^{(2)}\left(X^{(2)}\right)-\mathscr{E} g_{2}^{(1)}\left(X^{(1)}\right) \mathscr{E} g_{2}^{(2)}\left(X^{(2)}\right) \\
& +i\left[\mathscr{E} g_{2}^{(1)}\left(X^{(1)}\right) \mathscr{E} g_{1}^{(2)}\left(X^{(2)}\right)+\mathscr{E} g_{1}^{(1)}\left(X^{(1)}\right) \mathscr{E} g_{2}^{(2)}\left(X^{(2)}\right)\right] \\
= & {\left[\mathscr{E} g_{1}^{(1)}\left(X^{(1)}\right)+i \mathscr{E} g_{2}^{(1)}\left(X^{(1)}\right)\right]\left[\mathscr{E} g_{1}^{(2)}\left(X^{(2)}\right)+i \mathscr{E} g_{2}^{(2)}\left(X^{(2)}\right)\right] } \\
= & \mathscr{E} g^{(1)}\left(X^{(1)}\right) \mathscr{E} g^{(2)}\left(X^{(2)}\right) .
\end{aligned}
$$

By applying Lemma 2.6.1 successively to $g(X)=e^{i t^{\prime} X}$, we derive
Lemma 2.6.2. If the components of $X$ are mutually independent,
(8)

$$
\mathscr{E} e^{i \prime^{\prime} X}=\prod_{j=1}^{p} \mathscr{E} e^{i\left(t_{j} X\right)}
$$

We now find the characteristic function of a random vector with a normal distribution.



Theorem 2.6.1. The characteristic function of $\boldsymbol{X}$ distributed according to $N(\mu, \Sigma)$ is

$$
\phi(t)=\mathscr{E} e^{i t^{\prime} X}=e^{i t^{\prime} \mu-\frac{1}{t^{\prime}} t^{\prime} \Sigma}
$$

for every real vector $t$.
Proof. From Corollary A.1.6 of the Appendix we know there is a nonsingular matrix $C$ such that

$$
C^{\prime} \Sigma^{-1} C=I .
$$

Thus

$$
\Sigma^{-1}=C^{\prime-1} C^{-1}=\left(C C^{\prime}\right)^{-1}
$$

Let

$$
X-\mu=C Y .
$$

Then $\mathbf{Y}$ is distributed according to $N(\mathbf{0}, I)$.
Now the characteristic function of $\mathbf{Y}$ is

$$
\psi(u)=\mathscr{E} e^{i u^{\prime} Y}=\prod_{j=1}^{p} \mathscr{E} e^{i u_{j} I_{l}} .
$$

Since $Y_{j}$ is distributed according to $N(0,1)$,

$$
\psi(u)=\prod_{j=1}^{p} e^{-\frac{1}{2} u_{j}^{2}}=e^{-\frac{1}{2} u^{\prime} u} .
$$

Thus

$$
\begin{aligned}
\phi(t) & =\mathscr{E} e^{i f^{\prime} X}=\mathscr{E} e^{t t^{\prime}(C Y+\mu)} \\
& =e^{t t^{\prime} u} \mathscr{E} e^{i t^{\prime} C Y} \\
& =e^{i t^{\prime} \mu} e^{-\frac{1}{2}\left(f^{\prime} C\right)\left(t^{\prime} C\right)^{\prime}}
\end{aligned}
$$

for $t^{\prime} C=u^{\prime}$; the third equality is verified by writing both sides of it as integrals. But this is

$$
\begin{aligned}
\phi(t) & =e^{i t^{\prime} \mu} e^{-\frac{1}{2} t^{\prime} C C^{\prime} t} \\
& =e^{i t^{\prime} \mu-\frac{1}{2^{\prime}} t^{\prime} \Sigma t}
\end{aligned}
$$

by (11). This proves the theorem.

The characteristic function of the normal distribution is very useful. For example, we can use this method of proof to demonstrate the results of Section 2.4. If $Z=D X$, then the characteristic function of $Z$ is

$$
\begin{aligned}
\mathscr{E} e^{u \prime} Z & =\mathscr{E} e^{i t^{\prime} D X}=\mathscr{E} e^{i\left(D^{\prime} t^{\prime} X\right.} \\
& =e^{u\left(D^{\prime} t^{\prime} \mu-\frac{1}{2}\left(D^{\prime} t^{\prime} \Sigma\left(D^{\prime} t\right)\right.\right.} \\
& =e^{u t^{\prime}(D \mu)-\frac{1}{2} t^{\prime}\left(D \Sigma D^{\prime}\right) t},
\end{aligned}
$$

which is the characteristic function of $N\left(D \mu, D \Sigma D^{\prime}\right)$ (by Theorem 2.6.1).
It is interesting to use the characteristic function to show that it is only the multivariate normal distribution that has the property that every linear combination of variates is normally distributed. Consider a vector $Y$ of $p$ components with density $f(y)$ and characteristic function

$$
\psi(u)=\mathscr{E} e^{i u^{\prime} \gamma}=\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} e^{i u^{\prime} y} f(y) d y_{1} \cdots d y_{p},
$$

and suppose the mean of $\mathbf{Y}$ is $\boldsymbol{\mu}$ and the covariance matrix is $\mathbf{\Sigma}$. Suppose $\boldsymbol{u}^{\prime} \mathbf{Y}$ is normally distributed for every $u$. Then the characteristic function of such linear combination is

$$
\mathscr{E} e^{t t u^{\prime} Y}=e^{t t u^{\prime} \mu-\frac{1}{2} t^{2} u^{\prime} \Sigma u} .
$$

Now set $t=1$. Since the right-hand side is then the characteristic function of $N(\mu, \Sigma)$, the result is proved (by Theorem 2.6.1 above and 2.6.3 below).

Theorem 2.6.2. If every linear combination of the components of a vector $\mathbf{Y}$ is normally distributed, then $\mathbf{Y}$ is normally distributed.

It might be pointed out in passing that it is essential that every linear combination be normally distributed for Theorem 2.6.2 to hold. For instance, if $\mathbf{Y}=\left(Y_{1}, Y_{2}\right)^{\prime}$ and $Y_{1}$ and $Y_{2}$ are not independent, then $Y_{1}$ and $Y_{2}$ can each have a marginal normal distribution. An example is most easily given geometrically. Let $X_{1}, X_{2}$ have a joint normal distribution with means 0 . Move the same mass in Figure 2.1 from rectangle $A$ to $C$ and from $B$ to $D$. It will be seen that the resulting distribution of $Y$ is such that the marginal distributions of $Y_{1}$ and $Y_{2}$ are the same as $X_{1}$ and $X_{2}$, respectively, which are normal, and yet the joint distribution of $Y_{1}$ and $Y_{2}$ is not normal.

This example can be used also to demonstrate that two variables, $Y_{1}$ and $Y_{2}$, can be uncorrelated and the marginal distribution of each may be normal,

![](https://cdn.mathpix.com/cropped/4eec0a48-aad4-4a4d-8fab-6400a6d4e190-063.jpg?height=469&width=468&top_left_y=232&top_left_x=572)
Figure 2.1

but the pair need not have a joint normal distribution and need not be independent. This is done by choosing the rectangles so that for the resultant distribution the expected value of $Y_{1} Y_{2}$ is zern. It is clear geometrically that this can be done.

For future reference we state two useful theorems concerning characteristic functions.

Theorem 2.6.3. If the random vector $X$ has the density $f(x)$ and the characteristic function $\phi(t)$, then

$$
f(x)=\frac{1}{(2 \pi)^{p}} \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} e^{-t r^{\prime} x} \phi(t) d t_{1} \cdots d t_{p} .
$$

This shows that the characteristic function determines the density function uniquely. If $X$ does not have a density, the characteristic function uniquely defines the probability of any continuity interval. In the univariate case a continuity interval is an interval such that the cdf does not have a discontinuity at an endpoint of the interval.
' Theorem 2.6.4. Let $\left\{F_{j}(x)\right\}$ be a sequence of $\operatorname{cdf} s$, and let $\left\{\phi_{j}(t)\right\}$ be the sequence of corresponding characteristic functions, A necessary and sufficient condition for $F_{j}(x)$ to converge to a $\operatorname{cdf} F(x)$ is that, for every $t, \phi_{j}(t)$ converges to a limit $\phi(t)$ that is continuous at $t=0$. When this condition is satisfied, the timit $\phi(t)$ is identical with the characteristic function of the limiting distribution $F(x)$.

For the proofs of these two theorems, the reader is referred to Cramer (1946), Sections 10.6 and 10.7.

### 2.6.2. The Moments and Cumulants

The moments of $X_{1}, \ldots, X_{p}$ with a joint normal distribution can be obtained from the characteristic function (9). The mean is

$$
\begin{aligned}
\mathscr{E} X_{h} & =\left.\frac{1}{i} \frac{\partial \phi}{\partial t_{h}}\right|_{t=0} \\
& =\left.\frac{1}{i}\left\{-\sum_{j} \sigma_{h j} t,+i \mu_{h}\right\} \phi(t)\right|_{t=0} \\
& =\mu_{h} .
\end{aligned}
$$

The second moment is

$$
\begin{aligned}
\mathscr{E} X_{h} X_{j} & =\left.\frac{1}{i^{2}} \frac{\partial^{2} \phi}{\partial t_{h} \partial t_{j}}\right|_{t=0} \\
& =\left.\frac{1}{i^{2}}\left\{\left(-\sum_{k} \sigma_{h k} t_{k}+i \mu_{h}\right)\left(-\sum_{k} \sigma_{k} t_{k}+i \mu_{j}\right)-\sigma_{h j}\right\} \phi(t)\right|_{t=0} \\
& =\sigma_{h j}+\mu_{h} \mu_{j}
\end{aligned}
$$

Thus

$$
\begin{aligned}
\operatorname{Variance}\left(X_{i}\right) & =\mathscr{E}\left(X_{t}-\mu_{t}\right)^{2}=\sigma_{i t} \\
\operatorname{Covariance}\left(X_{t}, X_{j}\right) & =\mathscr{E}\left(X_{i}-\mu_{i}\right)\left(X_{j}-\mu_{j}\right)=\sigma_{t y}
\end{aligned}
$$

Any third moment about the mean is

$$
\mathscr{E}\left(X_{1}-\mu_{t}\right)\left(X_{j}-\mu_{j}\right)\left(X_{k}-\mu_{k}\right)=0 .
$$

The fourth moment about the mean is

$$
\mathscr{E}\left(X_{\imath}-\mu_{\imath}\right)\left(X_{j}-\mu_{j}\right)\left(X_{k}-\mu_{k}\right)\left(X_{l}-\mu_{l}\right)=\sigma_{i j} \sigma_{k l}+\sigma_{i k} \sigma_{j l}+\sigma_{I I} \sigma_{j k}
$$

Every moment of odd order is 0 .
Definition 2.6.3. If all the moments of a distribution exist, then the cumulants are the coefficients $\kappa$ in

$$
\log \phi(t)=\sum_{s_{1}, \ldots s_{p} \neq 0}^{\infty} \kappa_{s_{1} \cdots s_{p}} \frac{\left(i t_{1}\right)^{s_{1}} \cdots\left(i t_{p}\right)^{s_{p}}}{s_{1}!\cdots s_{p}!} .
$$

In the case of the multivariate normal distribution $\kappa_{10} \ldots 0=\mu_{1}, \ldots, \kappa_{0} \ldots 01 =\mu_{p}, \kappa_{20} \ldots 0=\sigma_{11}, \ldots, \kappa_{0 \cdots 02}=\sigma_{p p}, \kappa_{110} \ldots 0=\sigma_{12}, \ldots$. The cumulants for which $\sum s_{i}>2$ are 0 .

### 2.7. ELLIPTICALLY CONTOURED DISTRIBUTIONS

### 2.7.1. Spherically and Elliptically Contoured Distributions

It was noted at the end of Section 2.3 that the density of the multivariate normal distribution with mean $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$ is constant on concentric ellipsoids

$$
(x-\mu)^{\prime} \Sigma^{-1}(x-\mu)=k .
$$

A general class of distributions with this property is the class of elliptically contoured distributions with density

$$
|\boldsymbol{\Lambda}|^{-\frac{1}{2}} g\left[(x-\boldsymbol{v})^{\prime} \boldsymbol{\Lambda}^{-1}(x-\boldsymbol{v})\right],
$$

where $\mathbf{\Lambda}$ is a positive definite matrix, $g(\cdot) \geq 0$, and

$$
\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} g\left(y^{\prime} y\right) d y_{1} \cdots d y_{p}=1 .
$$

If $\boldsymbol{C}$ is a nonsingular matrix such that $\boldsymbol{C}^{\prime} \boldsymbol{\Lambda}^{-1} \boldsymbol{C}=\boldsymbol{I}$, the transformation $x-v=C y$ carries the density (2) to the density $g\left(y^{\prime} y\right)$. The contours of constant density of $g\left(y^{\prime} y\right)$ are spheres centered at the origin. The class of such densities is known as the spherically contoured distributions. Elliptically contoured distributions do not necessarily have densities, but in this exposition only distributions witly densities will be treated for statistical inference.

A spherically contoured density can be expressed in polar coordinates by the transformation
(4)

$$
\begin{aligned}
y_{1} & =r \sin \theta_{1}, \\
y_{2} & =r \cos \theta_{1} \sin \theta_{2}, \\
y_{3} & =r \cos \theta_{1} \cos \theta_{2} \sin \theta_{3}, \\
\vdots & \\
y_{p-1} & =r \cos \theta_{1} \cos \theta_{2} \cdots \cos \theta_{p-2} \sin \theta_{p-2}, \\
y_{p} & =r \cos \theta_{1} \cos \theta_{2} \cdots \cos \theta_{p-2} \cos \theta_{p-1},
\end{aligned}
$$

where $-\frac{1}{2} \pi<\theta_{i} \leq \frac{1}{2} \pi, i=1, \ldots, p-2,-\pi<\theta_{p-1} \leq \pi$, and $0 \leq r<\infty$. Note that $y^{\prime} y=r^{2}$. The Jacobian of the transformation (4) is $r^{p-1} \cos ^{p-2} \theta_{1} \cos ^{p-3} \theta_{2} \cdots \cos \theta_{p-2}$. See Problem 7.1. If $g\left(y^{\prime} y\right)$ is the density of $\boldsymbol{Y}$, then the density of $R, \Theta_{1}, \ldots, \Theta_{p-1}$ is

$$
r^{p-1} \cos ^{p-2} \theta_{1} \cos ^{p-3} \theta_{2} \cdots \cos \theta_{p-2} g\left(r^{2}\right)
$$

Note that $R, \Theta_{1}, \ldots, \Theta_{p-1}$ are independently distributed. Since

$$
\int_{-\pi / 2}^{\pi / 2} \cos ^{h}{ }^{1} \theta d \theta=\frac{\Gamma\left(\frac{1}{2} h\right) \Gamma\left(\frac{1}{2}\right)}{\Gamma\left[\frac{1}{2}(h+1)\right]}
$$

(Problem 7.2), the marginal density of $R$ is

$$
C(p) g\left(r^{2}\right) r^{p-1}
$$

where
(8)

$$
\begin{aligned}
C(p) & =\frac{2 \cdot T^{\frac{1}{2} p}}{\Gamma\left(\frac{1}{2} p\right)} \\
& =\int_{-\pi}^{\pi} \int_{-\pi / 2}^{\pi / 2} \cdots \int_{-\pi / 2}^{\pi / 2} \cos ^{p-2} \theta_{1} \cos ^{p-3} \theta_{2} \cdots \cos \theta_{p-2} d \theta_{1} \cdots d \theta_{p-2} d \theta_{p-1}
\end{aligned}
$$

The marginal density of $\Theta_{1}$ is $\Gamma\left[\frac{1}{2}(p-i)\right] \cos ^{p-1-1} \theta /\left\{\Gamma\left(\frac{1}{2}\right) \Gamma\left[\frac{1}{2}(p-i-1)\right]\right\}$, $i=1, \ldots, p-2$, and of $\theta_{p-1}$ is $1 /(2 \pi)$.

In the normal case of $N(\mathbf{0}, \boldsymbol{I})$ the density of $\boldsymbol{Y}$ is

$$
g\left(y^{\prime} y\right)=(2 \pi)^{-\frac{1}{2} p} \exp \left(-\frac{1}{2} y^{\prime} y\right),
$$

and the density of $R=\left(Y^{\prime} Y\right)^{\frac{1}{2}}$ is $r^{p-1} \exp \left(-\frac{1}{2} r^{2}\right) /\left[2^{\frac{1}{2} p-1} \Gamma\left(\frac{1}{2} p\right)\right]$. The density of $r^{2}=v$ is $v^{\frac{1}{2} p-1} e^{-\frac{1}{2} v} /\left[2^{\frac{1}{2} p} \Gamma\left(\frac{1}{2} p\right)\right]$. This is the $\chi^{2}$-density with $\boldsymbol{p}$ degrees of freedom.

The constant $C(p)$ is the surface area of a sphere of unit radius in $p$ dimensions. The random vector $U$ with coordinates $\sin \Theta_{1}, \cos \Theta_{1} \sin \Theta_{2}, \ldots$, $\cos \Theta_{1} \cos \Theta_{2} \cdots \cos \Theta_{p-1}$, where $\Theta_{1}, \ldots, \Theta_{p-1}$ are independently distributed each with the uniform distribution over ( $-\pi / 2, \pi / 2$ ) except for $\Theta_{p-1}$ having the uniform distribution over ( $-\pi, \pi$ ), is said to be uniformly distributed on the unit sphere. (This is the simplest example of a spherically contoured distribution not having a density.) A stochastic representation of $Y$ with the
density $g\left(y^{\prime} y\right)$ is

$$
Y \stackrel{d}{=} R U,
$$

where $R$ has the density (7).
Since each of the densities of $\Theta_{1}, \ldots, \Theta_{p-1}$ are even,

$$
\mathscr{E} U=0 .
$$

Because $R$ and $U$ are independent,

$$
\mathscr{E} Y=0
$$

if $\mathscr{E} R<\infty$. Further,

$$
\mathscr{E} Y Y^{\prime}=\mathscr{E} R^{2} \mathscr{E} U U^{\prime}
$$

if $\mathscr{E} R^{2}<\infty$. By symmetry $\mathscr{E} U_{1}^{2}=\cdots=\mathscr{E} U_{p}^{2}=1 / p$ because $\sum_{-1}^{p} U_{1}^{2}=1$. Again by symmetry $\mathscr{E} U_{1} U_{2}=\mathscr{E} U_{1} U_{3}=\cdots=\mathscr{E} U_{p-1} U_{p}$. In particular $\mathscr{E} U_{1} U_{2} =\mathscr{E} \sin \Theta_{1} \cos \Theta_{1} \sin \Theta_{2}$, the integrand of which is an odd function of $\theta_{1}$ and of $\theta_{2}$. Hence, $\mathscr{E} U_{1} U_{j}=0, i \neq j$. To summarize,

$$
\mathscr{E} U U^{\prime}=(1 / p) I_{p}
$$

and

$$
\mathscr{E} Y Y^{\prime}=(1 / p) \mathscr{E} R^{2} I_{p}
$$

(if $\mathscr{E} R^{2}<\infty$ ).
The distinguishing characteristic of the class of spherically contoured distributions is that $O Y \stackrel{d}{=} Y$ for every orthogonal matrix $O$.

Theorem 2.7.1. If Y has the density $g\left(y^{\prime} y\right)$, then $\boldsymbol{Z}=\boldsymbol{O Y}$, where $\boldsymbol{O}^{\prime} \boldsymbol{O}=\boldsymbol{I}$, has the density $g\left(z^{\prime} z\right)$.

Proof. The transformation $z=O y$ has Jacobian 1. $\square$

We shall extend the definition of $Y$ being spherically contoured to any distribution with the property $O Y \stackrel{d}{=} \boldsymbol{Y}$.

Corollary 2.7.1. If $Y$ is spherically contoured with stochastic representation $Y \stackrel{d}{=} R U$ with $R^{2}=Y^{\prime} Y$, then $U$ is spherically contoured.

Proof. If $\boldsymbol{Z}=\boldsymbol{O} \boldsymbol{Y}$ and hence $\boldsymbol{Z} \stackrel{d}{=} \boldsymbol{Y}$, and $\boldsymbol{Z}$ has the stochastic representation $Z=S V$, where $S^{2}=Z^{\prime} Z$, then $S=R$ and $V=O U \stackrel{d}{=} U$. $\square$

The density of $\boldsymbol{X}=\boldsymbol{\nu}+\boldsymbol{C Y}$ is (2). From (11) and (14) we derive the following theorem:

Theorem 2.7.2. If $X$ has the density (2) and $\mathscr{E} R^{2}<\infty$,

$$
\mathscr{E} X=\mu=\nu, \quad \mathscr{C}(X)=\mathscr{E}(X-\mu)(X-\mu)^{\prime}=\Sigma=(1 / p) \mathscr{E} R^{2} \Lambda .
$$

In fact if $\mathscr{E} R^{m}<\infty$, a moment of $X$ of order $h(\leq m)$ is $\mathscr{E}\left(X_{1}-\mu_{1}\right)^{h_{1}} \ldots \left(X_{p}-\mu_{p}\right)^{h_{p}}=\mathscr{E} Z_{1}^{h_{1}} \cdots Z_{p}^{h_{p}} \mathscr{E} R^{h} / \mathscr{E}\left(\chi_{p}^{2}\right)^{\frac{1}{2} h}$, where $Z$ has the distribution $N(\mathbf{0}, \Sigma)$ and $h=h_{1}+\cdots+h_{p}$.

Theorem 2.73. If $X$ has the density (2), $\mathscr{E} R^{2}<\infty$, and $f[c \mathscr{C}(X)]= f[\mathscr{C}(\boldsymbol{X})]$ for all $c>0$, then $f[\mathscr{C}(\boldsymbol{X})]=f(\boldsymbol{\Sigma})$.

In particular $\rho_{1 j}(X)=\sigma_{i j} / \sqrt{\sigma_{11} \sigma_{17}}=\lambda_{i j} / \sqrt{\lambda_{i j} \lambda_{j j}}$, where $\Sigma=\left(\sigma_{i j}\right)$ and $\Lambda=$ ( $\lambda_{\mathrm{t}}$ ) .

### 2.7.2. Distributions of Linear Combinations; Marginal Distributions

First we consider a spherically contoured distribution with density $g\left(y^{\prime} y\right)$. Let $y^{\prime}=\left(y_{1}^{\prime}, y_{2}^{\prime}\right)$, where $y_{1}$ and $y_{2}$ have $q$ and $p-q$ components, respectively. The marginal density of $y_{2}$ is

$$
\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} g\left(y_{1}^{\prime} y_{1}+y_{2}^{\prime} y_{2}\right) d y_{1} \cdots d y_{q} .
$$

Express $y_{1}$ in polar coordinates (4) with $r$ replaced by $r_{1}$ and $p$ replaced by $q$. Then the marginal density of $y_{2}$ is

$$
g_{2}\left(y_{2}^{\prime} y_{2}\right)=C(q) \int_{0}^{\infty} g\left(r_{1}^{2}+y_{2}^{\prime} y_{2}\right) r_{1}^{q-1} d r_{1} .
$$

This expression shows that the marginal distribution of $\boldsymbol{y}_{2}$ has a density which is spherically contoured.

Now consider a vector $X^{\prime}=\left(X^{(1) \prime}, X^{(2) \prime}\right)$ with density (2). If $\mathscr{E} R^{2}<\infty$, the covariance matrix of $X$ is (15) partitioned as (14) of Section 2.4. Let $Z^{(1)}=X^{(1)}-\Sigma_{12} \Sigma_{22}^{-1} X^{(2)}=X^{(1)}-\Lambda_{12} \Lambda_{22}^{-1} X^{(2)}, \quad Z^{(2)}=X^{(2)}, \quad \tau^{(1)}= v^{(1)}-\Sigma_{12} \Sigma_{22}^{-1} v^{(2)}=v^{(1)}-\Lambda_{12} \Lambda_{22}^{-1} v^{(2)}, \tau^{(2)}=v^{(2)}$. Then the density of $Z^{\prime}=$ ( $Z^{(1) \prime}, Z^{(2) \prime}$ ) is

$$
\begin{aligned}
\left|\Lambda_{11 \cdot 2}\right|^{-\frac{1}{2}}\left|\Lambda_{22}\right|^{-\frac{1}{2}} g & {\left[\left(z^{(1)}-\boldsymbol{\tau}^{(1)}\right)^{\prime} \Lambda_{11 \cdot 2}\left(z^{(1)}-\boldsymbol{\tau}^{(1)}\right)\right.} \\
& \left.+\left(z^{(2)}-\boldsymbol{v}^{(2)}\right)^{\prime} \boldsymbol{\Lambda}_{22}^{\prime}\left(z^{(2)}-\boldsymbol{v}^{(2)}\right)\right] .
\end{aligned}
$$

Note that $Z^{(1)}$ and $Z^{(2)}$ are uncorrelated even though possibly dependent. Let $\boldsymbol{C}_{\mathbf{1}}$ and $\boldsymbol{C}_{2}$ be $q \times q$ and $(p-q) \times(p-q)$ matrices satisfying $\boldsymbol{C}_{\mathbf{1}} \boldsymbol{\Lambda}_{\mathrm{II} \cdot 2}^{-1} \boldsymbol{C}_{\mathrm{I}}^{\prime} =I_{q}$ and $C_{2} \Lambda_{22}^{-1} C_{2}^{\prime}=I_{p-q}$. Define $y^{(1)}$ and $y^{(2)}$ by $z^{(1)}-\tau^{(1)}=C_{1} y^{(1)}$ and $z^{(2)}-v^{(2)}=C_{2} y^{(2)}$. Then $Y^{(1)}$ and $Y^{(2)}$ have the density $g\left(y^{(1) \prime} y^{(1)}+y^{(2) \prime} y^{(2)}\right)$. The marginal density of $Y^{(2)}$ is (17), and the marginal density of $X^{(2)}=Z^{(2)}$ is

$$
\begin{aligned}
& \left|\boldsymbol{\Lambda}_{22}\right|^{-\frac{1}{2}} g_{2}\left[\left(x^{(2)}-\boldsymbol{v}^{(2)}\right)^{\prime} \boldsymbol{\Lambda}_{22}^{-1}\left(x^{(2)}-\boldsymbol{v}^{(2)}\right)\right] \\
& \quad=C(q) \int_{0}^{\infty} g\left[r_{1}^{2}+\left(x^{(2)}-\boldsymbol{v}^{(2)}\right)^{\prime} \boldsymbol{\Lambda}_{22}^{-1}\left(x^{(2)}-\boldsymbol{v}^{(2)}\right] r_{1}^{q-1} d r_{1}\right.
\end{aligned}
$$

The moments of $Y_{2}$ can be calculated from the moments of $Y$.
The generalization of Theorem 2.4.1 to elliptically contoured distributions is the following: Let $\boldsymbol{X}$ with $p$ components have the density (2). Then $\boldsymbol{Y}=\boldsymbol{C X}$ has the density $\left|\boldsymbol{C} \boldsymbol{\Lambda} \boldsymbol{C}^{\prime}\right|^{-\frac{1}{2}} g\left[(x-\boldsymbol{C} \boldsymbol{v})^{\prime}\left(\boldsymbol{C} \boldsymbol{\Lambda} \boldsymbol{C}^{\prime}\right)^{-1}(x-\boldsymbol{C} \boldsymbol{v})\right]$ for $\boldsymbol{C}$ nonsingular.

The generalization of Theorem 2.4.4 is the following: If $X$ has the density (2), then $Z=D X$ has the density

$$
\left|\boldsymbol{D} \boldsymbol{\Lambda} \boldsymbol{L}^{\prime}\right|^{-\frac{1}{2}} g_{2}\left[(z-\boldsymbol{D} \boldsymbol{v})^{\prime}\left(D \boldsymbol{\Lambda} D^{\prime}\right)^{-1}(z-\boldsymbol{D} \boldsymbol{v})\right],
$$

where $D$ is a $q \times p$ matrix of rank $q \leq p$ and $g_{2}$ is given by (17).
We can also characterize marginal distributions in terms of the representation (9). Consider

$$
\boldsymbol{Y}=\binom{\boldsymbol{Y}^{(1)}}{\boldsymbol{Y}^{(2)}} \stackrel{d}{=} R U=R\binom{U^{(1)}}{U^{(2)}},
$$

where $Y^{(1)}$ and $U^{(1)}$ have $q$ components and $Y^{(2)}$ and $U^{(2)}$ have $p-q$ components. Then $R_{2}^{2}=Y^{(2) \prime} Y^{(2)}$ has the distribution of $R^{2} U^{(2) \prime} U^{(2)}$, and

$$
U^{(2)} U^{(2)}=\frac{U^{(2)} U^{(2)}}{U^{\prime} U} \stackrel{d}{=} \frac{Y^{(2) \prime} Y^{(2)}}{Y^{\prime} Y} .
$$

In the case $Y \sim N\left(0, I_{p}\right)$, (22) has the beta distribution, say $B(p-q, q)$, with density

$$
\frac{\Gamma(p / 2)}{\Gamma(q / 2) \Gamma[(p-q) / 2]} z^{\frac{1}{2}(p-q)-1}(1-z)^{\frac{1}{2} q-1}, \quad 0 \leq z \leq 1 .
$$

Hence, in general,

$$
Y^{(2)} \stackrel{d}{=} R_{2} V,
$$

where $R_{2}^{2} \stackrel{d}{=} R^{2} b, b \sim B(p-q, q), V$ has the uniform distribution of $v^{\prime} v=1$ in $p_{2}$ dimensions, and $R^{2}, b$, and $V$ are independent. All marginal distributions are elliptically contoured.

### 2.7.3. Conditional Distributions and Multiple Correlation Coefficient

The density of the conditional distribution of $y_{1}$ given $y_{2}$ when $y=\left(y_{1}^{\prime}, y_{2}^{\prime}\right)^{\prime}$ has the spherical density $g\left(y^{\prime} y\right)$ is

$$
\frac{g\left(y_{1}^{\prime} y_{1}+y_{2}^{\prime} y_{2}\right)}{g_{2}\left(y_{2}^{\prime} y_{2}\right)}=\frac{g\left(y_{1}^{\prime} y_{1}+r_{2}^{2}\right)}{g_{2}\left(r_{2}^{2}\right)},
$$

where the marginal density $g_{2}\left(y_{2}^{\prime} y_{2}\right)$ is given by (17) and $r_{2}^{2}=y_{2}^{\prime} y_{2}$. In terms of $y_{1}$, (25) is a spherically contoured distribution (depending on $r_{2}^{2}$ ).

Now consider $X=\left(X_{1}^{\prime}, X_{2}^{\prime}\right)^{\prime}$ with density (2). The conditional density of $X^{(1)}$ given $X^{(2)}=x^{(2)}$ is

$$
\begin{aligned}
& \left|\boldsymbol{\Lambda}_{11 \cdot 2}\right|^{-\frac{1}{2}} g\left\{\left[\left(x^{(1)}-\nu^{(1)}\right)^{\prime}-\left(x^{(2)}-\nu^{(2)}\right)^{\prime} \boldsymbol{B}^{\prime}\right] \boldsymbol{\Lambda}_{11 \cdot 2}^{-1}\left[x^{(1)}-\nu^{(1)}-\boldsymbol{B}\left(x^{(2)}-\nu^{(2)}\right)\right]\right. \\
& \left.+\left(x^{(2)}-\nu^{(2)}\right)^{\prime} \boldsymbol{\Lambda}_{22}^{-1}\left(x^{(2)}-\nu^{(2)}\right)\right\} \\
& \quad \div g_{2}\left[\left(x^{(2)}-\nu^{(2)}\right)^{\prime} \boldsymbol{\Lambda}_{22}^{-1}\left(x^{(2)}-\nu^{(2)}\right)\right] \\
& =\left|\boldsymbol{\Lambda}_{11 \cdot 2}\right|^{-\frac{1}{2}} g\left[\left[x^{(1)}-\nu^{(1)}-\boldsymbol{B}\left(x^{(2)}-\nu^{(2)}\right)\right]^{\prime} \boldsymbol{\Lambda}_{11 \cdot 2}^{-1}\left[x^{(1)}-\nu^{(1)}-\boldsymbol{B}\left(x^{(2)}-\nu^{(2)}\right)\right]+r_{2}^{2}\right\} \\
& \quad \div g_{2}\left(r_{2}^{2}\right),
\end{aligned}
$$

where $r_{2}^{2}=\left(x^{(2)}-\boldsymbol{v}^{(2)}\right)^{\prime} \boldsymbol{\Lambda}_{22}^{-1}\left(x^{(2)}-\boldsymbol{v}^{(2)}\right)$ and $\boldsymbol{B}=\boldsymbol{\Lambda}_{12} \boldsymbol{\Lambda}_{22}^{-1}$. The density (26) is elliptically contoured in $x^{(1)}-\boldsymbol{v}^{(1)}-\boldsymbol{B}\left(x^{(2)}-\boldsymbol{v}^{(2)}\right)$ as a function of $\boldsymbol{x}^{(1)}$. The conditional mean of $X^{(1)}$ given $X^{(2)}=x^{(2)}$ is

$$
\mathscr{E}\left(X^{(1)} \mid x^{(2)}\right)=\nu^{(1)}+B\left(x^{(2)}-\nu^{(2)}\right)
$$

if $\mathscr{E}\left(R_{1}^{2} \mid y_{2}^{\prime} y_{2}=r_{2}^{2}\right)<\infty$ in (25), where $R_{1}^{2}=Y_{1}^{\prime} Y_{1}$. Also the conditional covariance matrix is $\left(\mathscr{E} r_{2}^{2} / q\right) \Lambda_{11.2}$. It follows that Definition 2.5.2 of the partial correlation coefficient holds when $\left(\sigma_{i j q+1, \ldots, p}\right)=\Sigma_{11 \cdot 2}=\Sigma_{11}+\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}$ and $\Sigma$ is the parameter matrix given above.

Theorems 2.5.2, 2.5.3, and 2.5.4 are true for any elliptically contoured distribution for which $\mathscr{E} R^{2}<\infty$.

### 2.7.4 The Characteristic Function; Moments

The characteristic function of a random vector $\boldsymbol{Y}$ with a spherically contoured distribution $\mathscr{E} e^{i t^{\prime} Y}$ has the property of invariance over orthogonal



transformations, that is,

$$
\begin{aligned}
\mathscr{E} e^{i t^{\prime} O Y} & =\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} e^{i t^{\prime} O y} g\left(y^{\prime} y\right) d y_{1} \cdots d y_{p} \\
& =\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} e^{i t^{\prime} z} g\left(z^{\prime} z\right) d z_{1} \cdots d z_{p} \\
& =\mathscr{E} e^{i t^{\prime} z}
\end{aligned}
$$

where $Z=O Y$ also has the density $g\left(y^{\prime} y\right)$. The equality (28) for all orthogonal $O$ implies $\mathscr{E} e^{\left[t^{\prime} Z\right.}$ is a function of $t^{\prime} t$. We write

$$
\mathscr{E} e^{t t^{\prime} Y}=\phi\left(t^{\prime} t\right) .
$$

Then for $\boldsymbol{X}=\boldsymbol{\mu}+\boldsymbol{C Y}$

$$
\begin{aligned}
\mathscr{E} i^{i t^{\prime} X} & =e^{i t^{\prime} \mu} \mathscr{E} e^{i t^{\prime} C Y} \\
& =e^{i t \mu} \phi\left(t^{\prime} C C^{\prime} t\right) \\
& =e^{i t^{\prime} \mu} \phi\left(t^{\prime} \Lambda t\right)
\end{aligned}
$$

when $\boldsymbol{\Lambda}=\boldsymbol{C} \boldsymbol{C}^{\prime}$. Conversely, any characteristic function of the form $e^{i t^{\prime} \mu} \phi\left(t^{\prime} \Lambda t\right)$ corresponding to a density corresponds to a random vector $X$ with the density (2).

The moments of $X$ with an elliptically contoured distribution can be found from the characteristic function $e^{1 \mu^{\prime} \mu} \phi\left(t^{\prime} \Sigma t\right)$ or from the representation $\boldsymbol{X}=\boldsymbol{\mu}+\boldsymbol{R} \boldsymbol{C} \boldsymbol{U}$, where $\boldsymbol{C}^{\prime} \mathbf{\Lambda}^{-1} \boldsymbol{C}=\boldsymbol{I}$. Note that

$$
\begin{aligned}
& \mathscr{E} R^{2}=C(p) \int_{0}^{\infty} r^{p+1} g\left(r^{2}\right) d r=-2 p \phi^{\prime}(0) \\
& \mathscr{E} R^{4}=C(p) \int_{0}^{\infty} r^{p+3} g\left(r^{2}\right) d r=4 p(p+2) \phi^{\prime \prime}(0)
\end{aligned}
$$

Consider the higher-order moments of $Y=R U$. The odd-order moments of $R$ are 0 , and hence the odd-order moments of $Y$ are 0 .

We have

$$
\mathscr{E}\left(X_{i}-\mu_{i}\right)\left(X_{j}-\mu_{j}\right)\left(X_{k}-\mu_{k}\right)=0 .
$$

In fact, all moments of $X-\mu$ of odd order are 0 .
Consider $\mathscr{E} U_{i} U_{j} U_{k} U_{i}$. Because $U^{\prime} U=1$,

$$
1=\sum_{1, j=1}^{p} \mathscr{E} U_{i}^{2} U_{j}^{2}=p \mathscr{E} U_{1}^{4}+p(p-1) \mathscr{E} U_{1}^{2} U_{2}^{2}
$$

Integration of $\mathscr{E} \sin ^{4} \Theta_{t}$ gives $\mathscr{E} U_{t}^{4}=3 /[p(p+2)]$; then (34) implies $\mathscr{E} U_{1}^{2} U_{2}^{2}=1 /[p(p+2)]$. Hence $\mathscr{E} Y_{1}^{4}=3 \mathscr{E} R^{4} /[p(p+2)]$ and $\mathscr{E} Y_{1}^{2} Y_{2}^{2}= \mathscr{E} R^{4} /[p(p+2)]$. Unless $i=j=k=l$ or $i=j \neq k=l$ or $i=k \neq j=l$ or $i=l \neq j=k$. we have $\mathscr{E} U_{t} U_{,} U_{k} U_{l}=0$. To summarize $\mathscr{E} U_{l} U_{j} U_{k} U_{l}=\left(\delta_{i j} \delta_{k l}+\right. \left.\delta_{t h} \delta_{j l}+\delta_{t l} \delta_{j k}\right) /[p(p+2)]$. The fourth-order moments of $\boldsymbol{X}$ are

$$
\begin{aligned}
\mathscr{E}\left(X_{t}\right. & \left.-\mu_{t}\right)\left(X_{j}-\mu_{j}\right)\left(X_{k}-\mu_{k}\right)\left(X_{l}-\mu_{l}\right) \\
& =\frac{\mathscr{E} R^{4}}{p(p+2)}\left(\lambda_{t j} \lambda_{k l}+\lambda_{t k} \lambda_{j l}+\lambda_{i l} \lambda_{j k}\right) \\
& =\frac{\mathscr{E} R^{4}}{\left(\mathscr{E} R^{2}\right)^{2}} \frac{p}{p+2}\left(\sigma_{t j} \sigma_{k l}+\sigma_{t k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}\right)
\end{aligned}
$$

The fourth cumulant of the $i$ th component of $X$ standardized by its standard deviation is

$$
\begin{aligned}
\frac{\mathscr{E}\left(X_{t}-\mu_{t}\right)^{4}}{\left[\mathscr{E}\left(X_{t}-\mu_{t}\right)^{2}\right]^{2}}-3 & =\frac{\frac{3 \mathscr{E} R^{4}}{p(p+2)}-3\left(\frac{\mathscr{E} R^{2}}{p}\right)^{2}}{\left(\frac{\mathscr{E} R^{2}}{p}\right)^{2}} \\
& =3\left[\frac{\mathscr{E} R^{4}}{\left(\mathscr{E} R^{2}\right)^{2}} \frac{p}{p+2}-1\right]=3\left[\frac{\phi^{\prime \prime}(0)}{\left[\phi^{\prime}(0)\right]^{2}}-1\right] \\
& =3 \kappa
\end{aligned}
$$

say. This is known as the kurtosis. (Note that $\kappa$ is $\frac{1}{3} \mathscr{E}\left\{\left(X_{t}-\mu_{i}\right)^{4} /\right. \left.\left[\mathscr{E}\left(X_{t}-\mu_{t}\right)^{2}\right]^{2}\right\}-1$.) The standardized fourth cumulant is $3 \kappa$ for every component of $X$. The fourth cumulant of $X_{i}, X_{j}, X_{k}$, and $X_{i}$ is

$$
\begin{aligned}
\kappa_{1, k l} & =\mathscr{E}\left(X_{1}-\mu_{t}\right)\left(X_{1}-\mu_{1}\right)\left(X_{k}-\mu_{k}\right)\left(X_{1}-\mu_{1}\right)-\left(\sigma_{t j} \sigma_{k l}+\sigma_{i k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}\right) \\
& =\kappa\left(\sigma_{t j} \sigma_{k l}+\sigma_{t k} \sigma_{j l}+\sigma_{1 l} \sigma_{j k}\right)
\end{aligned}
$$

For the normal distribution $\kappa=0$. The fourth-order moments can be written

$$
\begin{gathered}
\mathscr{E}\left(X_{t}-\mu_{t}\right)\left(X_{1}-\mu_{j}\right)\left(X_{k}-\mu_{k}\right)\left(X_{l}-\mu_{l}\right) \\
=(1+\kappa)\left(\sigma_{t l} \sigma_{k l}+\sigma_{t k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}\right)
\end{gathered}
$$

More detail about elliptically contoured distributions can be found in Fang and Zhang (1990).

The class of elliptically contoured distributions generalizes the normal distribution, introducing more flexibility; the kurtosis is not required to be 0 . The typical "bell-shaped surface" of $|\boldsymbol{\Lambda}|^{-\frac{1}{2}} g\left[(x-\boldsymbol{v})^{\prime} \boldsymbol{\Lambda}^{-1}(x-\boldsymbol{v})\right]$ can be more or less peaked than in the case of the normal distribution. In the next subsection some examples are given.

### 2.7.5. Examples

(1) The multivariate $t$-distribution. Suppose $Z \sim N\left(\mathbf{0}, I_{p}\right), m s^{2} \stackrel{d}{=} \chi_{m}^{2}$, and $Z$ and $s^{2}$ are independent. Define $Y=(1 / s) Z$. Then the density of $Y$ is

$$
\frac{\Gamma\left(\frac{m+p}{2}\right)}{\Gamma\left(\frac{m}{2}\right) m^{p / 2} \pi^{p / 2}}\left(1+\frac{y^{\prime} y}{m}\right)^{-\frac{m+p}{2}},
$$

and

$$
\frac{R^{2}}{p}=\frac{\|\boldsymbol{Y}\|^{2}}{p} \sim F_{p, m}=\frac{m}{p} \frac{\chi_{p}^{2}}{\chi_{m}^{2}} .
$$

If $X=\boldsymbol{\mu}+\boldsymbol{C Y}$, the density $\sigma^{\prime \prime} X$ is

$$
\frac{\Gamma\left(\frac{m+p}{2}\right)}{\Gamma\left(\frac{m}{2}\right) m^{p / 2} \pi^{p / 2}}|\Lambda|^{-\frac{1}{2}}\left[1+\frac{(x-\mu)^{\prime} \Lambda^{-1}(x-\mu)}{m}\right]^{-\frac{1}{2}(m+p)} .
$$

(2) Contaminated normal. The contaminated normal distribution is a mixture of two normal distributions with proportional covariance matrices and the same mean vector. The density can be written

$$
\begin{aligned}
& (1-\varepsilon) \frac{1}{(2 \pi)^{p / 2}|\Lambda|^{\frac{1}{2}}} e^{-\frac{1}{2}(x-\mu)^{\prime} \Lambda^{-1}(z-\mu)} \\
& \quad+\varepsilon \cdot \frac{1}{(2 \pi)^{p / 2}|c \Lambda|^{\frac{1}{2}}} e^{-(1 / 2 c)(x-\mu)^{\prime} \Lambda^{-1}(x-\mu)}
\end{aligned}
$$

where $c>0$ and $0 \leq \varepsilon \leq 1$. Usually $\varepsilon$ is rather small and $c$ rather large.
(3) Mixtures of normal distributions. Let $w(v)$ be a cumulative distribution function over $0 \leq v \leq \infty$. Then a mixture of normal densities is defined by

$$
\int_{0}^{\infty} n\left(x \mid \mu, \frac{1}{v^{2}} \Sigma\right) d w(v)
$$

which is an elliptically contoured density. The random vector $X$ with this density has a representation $X=w Z$, where $Z \sim N(\mu, \Sigma)$ and $w \sim w(w)$ are independent.

Fang, Kotz, and Ng (1990) have discussed (43) and have given other examples of elliptically contoured distributions.

## PROBLEMS

2.1. (Sec.2.2) Let $f(x, y)=1,0 \leq x \leq 1,0 \leq y \leq 1$, $=0$, otherwise.

Find:
(a) $F(x, y)$.
(b) $F(x)$.
(c) $f(x)$.
(d) $f(x \mid y)$. [Note: $f\left(x_{0} \mid y_{0}\right)=0$ if $f\left(x_{0}, y_{0}\right)=0$.]
(e) $\mathscr{c}^{\prime} X^{\prime \prime} Y^{\prime \prime}$.
(f) Prove $X$ and $Y$ are independent.
2.2. (Sec. 2.2) Let $f(x, y)=2,0 \leq y \leq x \leq 1$, $=0$, otherwise.

Find:
(a) $F(x, y)$.
(b) $F(x)$.
(c) $f(x)$.
(d) $G(y)$.
(e) $g(y)$.
(f) $f(x \mid y)$.
(g) $f(y \mid x)$.
(h) $\mathscr{E} X^{n} Y^{m}$.
(i) Are $X$ and $Y$ independent?
2.3. (Sec. 2.2) Let $f(x, y)=C$ for $x^{2}+y^{2} \leq k^{2}$ and 0 elsewhere. Prove $C= 1 /\left(\pi k^{2}\right), \mathscr{E} \boldsymbol{X}=\mathscr{E} Y=0, \mathscr{E} X^{2}=\mathscr{E} Y^{2}=k^{2} / 4$, and $\mathscr{E} X Y=0$. Are $X$ and $Y$ indeperdent?
2.4. (Sec. 2.2) Let $F\left(x_{1}, x_{2}\right)$ be the joint cdf of $X_{1}, X_{2}$, and let $F_{1}\left(x_{i}\right)$ be the marginal cdf of $X_{1}, i=1,2$. Prove that if $F_{i}\left(x_{i}\right)$ is continuous, $i=1,2$, then $F\left(x_{1}, x_{2}\right)$ is continuous.
2.5. (Scc. 22) Show that if the set $X_{1}, \ldots, X_{r}$ is independent of the set $X_{r+1}, \ldots, X_{p}$, then

$$
\mathscr{E} g\left(X_{1}, \ldots, X_{r}\right) h\left(X_{r+1}, \ldots, X_{p}\right)=\mathscr{E} g\left(X_{1}, \ldots, X_{r}\right) \mathscr{E} h\left(X_{r+1}, \ldots, X_{p}\right) .
$$

72.6. (Sec. 2.3) Sketch the ellipses $f(x, y)=0.06$, where $f(x, y)$ is the bivariate normal density with
(a) $\mu_{x}=1, \mu_{y}=2, \sigma_{x}^{2}=1, \sigma_{y}^{2}=1, \rho_{x y}=0$.
(b) $\mu_{x}=0, \mu_{y}=0, \sigma_{x}^{2}=1, \sigma_{y}^{2}=1, \rho_{x y}=0$.
(c) $\mu_{x}=0, \mu_{y}=0, \sigma_{x}^{2}=1, \sigma_{y}^{2}=1, \rho_{x y}=0.2$
(d) $\mu_{x}=0, \mu_{y}=0, \sigma_{x}^{2}=1, \sigma_{y}^{2}=1, \rho_{x y}=0.8$.
(e) $\mu_{x}=0, \mu_{y}=0, \sigma_{x}^{2}=4, \sigma_{y}^{2}=1, \rho_{\lambda y}=0.8$.
2.7. (Sec. 2.3) Find $b$ and $A$ so that the following densities can be written in the form of (23). Also find $\mu_{x}, \mu_{y}, \sigma_{x}, \sigma_{y}$ and $\rho_{x y}$.
(a) $\frac{1}{2 \pi} \exp \left(-\frac{1}{2}\left[(x-1)^{2}+(y-2)^{2}\right]\right\}$.
(b) $\frac{1}{2.4 \pi} \exp \left(-\frac{x^{2} / 4-1.6 x y / 2+y^{2}}{0.72}\right)$.
(c) $\frac{1}{2 \pi} \exp \left[-\frac{1}{2}\left(x^{2}+y^{2}+4 x-6 y+13\right)\right]$.
(d) $\frac{1}{2 \pi} \exp \left[-\frac{1}{2}\left(2 x^{2}+y^{2}+2 x y-22 x-14 y+65\right)\right]$.
2.8. (Sec. 2.3) For each matrix $A$ in Problem 2.7 find $C$ so that $C^{\prime} A C=I$.
2.9. (Sec. 2.3) Let $\boldsymbol{b}=\mathbf{0}$.

$$
A=\left(\begin{array}{lll}
7 & 3 & 2 \\
3 & 4 & 1 \\
2 & 1 & 2
\end{array}\right)
$$

(a) Write the density (23).
(b) Find $\Sigma$.
2.10. (Sec. 2.3) Prove that the principal axes of (55) of Section 2.3 are along the $45^{\circ}$ and $135^{\circ}$ lines with lengths $2 \sqrt{c(1+\rho)}$ and $2 \sqrt{c(1-\rho)}$, respectively, by transforming according to $y_{1}=\left(z_{1}+z_{2}\right) / \sqrt{2}, y_{2}=\left(z_{1}-z_{2}\right) / \sqrt{2}$.
2.11. (Sec. 2.3) Suppose the scalar random variables $X_{1}, \ldots, X_{n}$ are independent and have a density which is a function only of $x_{1}^{2}+\cdots+x_{n}^{2}$. Prove that the $X_{i}$ are normally distributed with mean 0 and common variance. Indicate the mildest conditions on the density for your proof.
2.12. (Sec. 2.3) Show that if $\operatorname{Pr}\{X \geq 0, Y \geq 0\}=\alpha$ for the distribution

$$
N\left[\binom{0}{0},\left(\begin{array}{ll}
1 & \rho \\
\rho & 1
\end{array}\right)\right],
$$

then $\rho=\cos (1-2 \alpha) \pi$. [Hint: Let $X=U, Y=\rho U+\sqrt{1-\rho^{2}} V$ and verify $\rho= \cos 2 \pi\left(\frac{1}{2}-\alpha\right)$ geometrically.]
2.13. (Sec. 2.3) Prove that if $\rho_{i j}=\rho, i \neq j, i, j=1, \ldots, p$, then $\rho \geq-1 /(p-1)$.
2.14. (Sec, 2.3) Concentration ellipsoid. Let the density of the $p$-component $Y$ be $f(y)=\Gamma\left(\frac{1}{2} p+1\right) /[(p+2) \pi]^{\frac{1}{2}} p$ for $y^{\prime} y \leq p+2$ and 0 elsewhere. Then $\mathscr{E} Y=0$ and $\mathscr{E} Y Y^{\prime}=I$ (Problem 7.4). From this result prove that if the density of $X$ is $g(x)=\sqrt{|A|}\left[\left(\frac{1}{2} p+1\right) /[(p+2) \pi]^{\frac{1}{2} p}\right.$ for $(x-\mu)^{\prime} A(x-\mu) \leq p+2$ and 0 elsewhere, then $\mathscr{r} X=\mu$ and $\mathscr{E}(X-\mu)(X-\mu)^{\prime}=A^{-1}$.
2.15. (Sec. 2,4) Show that when $X$ is normally distributed the components are mutually independent if and only if the covariance matrix is diagonal.
2.16. (Sec. 2.4) Find necessary and sufficient conditions on $A$ so that $A Y+\boldsymbol{\lambda}$ has a continuous cdf.
2.17. (Sec. 2.4) Which densities in Problem 2.7 define distributions in which $X$ and $Y$ are independent?
2.18. (Sec. 2.4)
(a) Write the marginal density of $X$ for each case in Problem 2.6.
(b) Indicate the marginal distribution of $X$ for each case in Problem 2.7 by the notation $N(a, b)$.
(c) Write the marginal density of $X_{1}$ and $X_{2}$ in Problem 2.9.
2.19. (Sec. 2.4) What is the distribution ol $Z=X-Y$ when $X$ and $Y$ have each of the densities in Problem 2.6?
2.20. (Sec. 2.4) What is the distribution of $X_{1}+2 X_{2}-3 X_{3}$ when $X_{1}, X_{2}, X_{3}$ have the distribution defined in Problem 2.9?
2.21. (Sec. 2.4) Let $X=\left(X_{1}, X_{2}\right)^{\prime}$. where $X_{1}=X$ and $X_{2}=a X+b$ and $X$ has the distribution $N(0,1)$. Find the cdf of $X$.
2.22. (Sec. 2.4) Let $X_{1}, \ldots, X_{N}$ be independently distributed, each according to $N\left(\mu, \sigma^{2}\right)$.
(a) What is the distribution of $X=\left(X_{1}, \ldots, X_{N}\right)^{\prime}$ ? Find the vector of means and the covariance matrix.
(b) Using Theorem 2.4.4, find the marginal distribution of $\bar{X}=\Sigma X_{i} / N$.
2.23. (Sec. 2.4) Let $X_{1}, \ldots, X_{N}$ be independently distributed with $X_{1}$ having distribution $N\left(\beta+\gamma z_{i}, \sigma^{2}\right)$, where $z_{i}$ is a given number, $i=1, \ldots, N$, and $\Sigma_{i} z_{i}=0$.
(a) Find the distribution of $\left(X_{1}, \ldots, X_{N}\right)^{\prime}$.
(b) Find the distribution of $\bar{X}$ and $g=\sum X_{i} z_{i} / \sum z_{1}^{2}$ for $\sum z_{i}^{2}>0$.
2.24. (Sec. 2.4) Let $\left(X_{1}, Y_{1}\right)^{\prime},\left(X_{2}, Y_{2}\right)^{\prime},\left(X_{3}, Y_{3}\right)^{\prime}$ be independently distributed, $\left(X_{1}, Y_{1}\right)^{\prime}$ according to

$$
N\left[\binom{\mu}{\nu},\left(\begin{array}{cc}
\sigma_{x x} & \sigma_{x y} \\
\sigma_{x y} & \sigma_{y y}
\end{array}\right)\right], \quad i=1,2,3
$$

(a) Find the distribution of the six variables.
(b) Find the distribution of $(\bar{X}, \bar{Y})^{\prime}$.
2.25. (Sec. 24) Let $X$ have a (singular) normal distribution with mean $\mathbf{0}$ and covariance matrix

$$
\Sigma=\left(\begin{array}{ll}
4 & 2 \\
2 & 1
\end{array}\right)
$$

(a) Prove $\Sigma$ is of rank 1.
(b) Find $a$ so $X=a^{\prime} Y$ and $Y$ has a nonsingular normal distribution, and give the density of $Y$.
2.26. (Sec. 2.4) Let

$$
\mathbf{\Sigma}=\left(\begin{array}{rrr}
2 & -1 & 3 \\
-1 & 5 & -3 \\
3 & -3 & 5
\end{array}\right) .
$$

(a) Find a vector $\boldsymbol{u} \neq \mathbf{0}$ so that $\mathbf{\Sigma} \boldsymbol{u}=\mathbf{0}$. [Hint; Take cofactors of any column.]
(b) Show that any matrix of the form $\boldsymbol{G}=(\boldsymbol{H} \boldsymbol{u})$, where $\boldsymbol{H}$ is $3 \times 2$, has the property

$$
G^{\prime} \Sigma G=\left(\begin{array}{cc}
H^{\prime} \Sigma & 0 \\
0 & 0
\end{array}\right)
$$

(c) Using (a) and (b), find $B$ to satisfy (36).
(d) Find $B^{-1}$ and partition according to (39).
(e) Verify that $C C^{\prime}=\Sigma$.
2.27. (Sec. 2.4) Prove that if the joint (marginal) distribution of $X_{1}$ and $X_{2}$ is singular (that is, degenerate), then the joint distribution of $X_{1}, X_{2}$, and $X_{3}$ is singular.
2.28. (Sec. 2.5) In cach part of Problem 2.6, find the conditional distribution of $\boldsymbol{X}$ given $Y=y$, find the conditional distribution of $Y$ given $X=x$, and plot each regression line on the appropriale graph in Problem 2,6.
2.29. (Sec. 2.5) Let $\mu=0$ and

$$
\Sigma=\left(\begin{array}{ccc}
1 . & 0.80 & -0.40 \\
0.80 & 1 . & -0.56 \\
-0.40 & -0.56 & 1 .
\end{array}\right) .
$$

(a) Find the conditional distribution of $X_{1}$ and $X_{3}$, given $X_{2}=x_{2}$.
(b) What is the partial correlation between $X_{1}$ and $X_{3}$ given $X_{2}$ ?
2.30. (Sec. 2.5) In Problem 2.9, find the conditional distribution of $X_{1}$ and $X_{2}$ given $X_{3}=x_{3}$.
2.31. (Sec. 2.5) Verify (20) directly from Theorem 2.5.1.
2.32. (Sec. 2.5)
(a) Show that finding $\boldsymbol{\alpha}$ to maximize the absolute value of the correlation between $X_{1}$ and $\boldsymbol{\alpha}^{\prime} \boldsymbol{X}^{(2)}$ is equivalent to maximizing $\left(\boldsymbol{\sigma}_{10}^{\prime} \boldsymbol{\alpha}\right)^{\frac{1}{2}}$ subject to $\alpha^{\prime} 2_{22} \alpha$ constant.
(b) Find $\boldsymbol{\alpha}$ by maximizing $\left(\boldsymbol{\sigma}_{(1)}^{\prime} \boldsymbol{\alpha}\right)^{2}-\lambda\left(\boldsymbol{\alpha}^{\prime} \Gamma_{22} \boldsymbol{\alpha}-c\right)$, where $c$ is a constant and $\lambda$ is a Lagrange multiplier.
2.33. (Sec. 2.5) Invariance of the multiple correlation coefficient. Prove that $\vec{R}_{i \cdot q+1}, \ldots, P$ is an invariant characteristic of the multivariate normal distribution of $\boldsymbol{X}_{i}$ and $\boldsymbol{X}^{(2)}$ under the transformation $x_{1}^{*}=b_{i} x_{i}+c_{i}$ for $b_{i} \neq 0$ and $\boldsymbol{X}^{(2) *}=\boldsymbol{H} \boldsymbol{X}^{(2)}+\boldsymbol{k}$ for $\boldsymbol{H}$ nonsingular and that every function of $\mu_{i}, \sigma_{i i}, \boldsymbol{\sigma}_{(i)}, \boldsymbol{\mu}^{(2)}$, and $\boldsymbol{\Sigma}_{22}$ that is invariant is a function of $\bar{R}_{i \cdot q+1} \ldots \ldots p$.
2.34. (Sec. 2.5) Prove that

$$
1-\bar{R}_{i q+1, \ldots, p}^{2}=\frac{1}{\left|\rho_{k j}\right|}\left|\begin{array}{cc}
1 & \rho_{i j} \\
\rho_{k i} & \rho_{k j}
\end{array}\right|, \quad k, j=q+1, \ldots, p .
$$

2.35. (Sec. 2.5) Find the multiple correlation coefficient between $X_{1}$ and $\left(X_{2}, X_{3}\right)$ in Problem 2.29.
2.36. (Sec. 2.5) Prove explicitly that if $\mathbf{\Sigma}$ is positive definite,

$$
|\Sigma|=\left|\Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}\right| \cdot\left|\Sigma_{22}\right| .
$$

2.37. (Sec. 2.5) Prove Hadamard's inequalip

$$
|\Sigma| \leq \prod_{i=1}^{p} \sigma_{1 i}
$$

[Hint: Using Problem 2.36, prove $|\boldsymbol{\Sigma}| \leq \sigma_{11}\left|\boldsymbol{\Sigma}_{22}\right|$, where $\boldsymbol{\Sigma}_{22}$ is $(p-1) \times$ ( $p-1$ ), and apply induction.]
238. (Sec. 2.5) Prove equality holds in Problem 2.37 if and only if $\mathbf{\Sigma}$ is diagonal.
239. (Sec. 2.5) Prove $\beta_{12 \cdot 3}=\sigma_{12 \cdot 3} / \sigma_{22 \cdot 3}=\rho_{13 \cdot 2} \sigma_{1 \cdot 2} / \sigma_{3 \cdot 2}$ and $\beta_{13 \cdot 2}=\sigma_{13 \cdot 2} / \sigma_{33 \cdot 2}= \rho_{13 \cdot 2} \sigma_{1 \cdot 2} / \sigma_{3 \cdot 2}$, where $\sigma_{i \cdot k}^{2}=\sigma_{i n \cdot k}$.
2.40. (Sec. 25) Let $\left(X_{1}, X_{2}\right)$ have the density $n(x \mid 0, \Sigma)=f\left(x_{1}, x_{2}\right)$. Let the density of $X_{2}$ given $X_{1}=x_{1}$ be $f\left(x_{2} \mid x_{1}\right)$. Let the joint density of $X_{1}, X_{2}, X_{3}$ be $f\left(x_{1}, x_{2}\right) f\left(x_{3} \mid x_{1}\right)$. Find the covariance matrix of $X_{1}, X_{2}, X_{3}$ and the partial correlation between $X_{2}$ and $X_{3}$ for given $X_{1}$.
2.41. (Sec. 2.5) Prove $1-\bar{R}_{1 \cdot 23}^{2}=\left(1-\rho_{13}^{2}\right)\left(1-\rho_{12 \cdot 3}^{2}\right)$. [Hint: Use the fact that the variance of $X_{1}$ in the conditional distribution given $x_{2}$ and $x_{3}$ is $\left(1-\bar{R}_{1 \cdot 23}^{2}\right) \sigma_{11 \cdot}$.]
2.42. (Sec. 2.5) If $p=2$, can there be a difference between the simple correlation between $X_{1}$ and $x_{2}$ and the multiple correlation between $\boldsymbol{X}_{1}$ and $\boldsymbol{X}^{(2)}=\boldsymbol{X}_{2}$ ? Explain.
2.43. (Sec. 2.5) Prove

$$
\begin{aligned}
\beta_{i k \cdot q+1, \ldots, k-1, k+1, \ldots, p} & =\frac{\sigma_{i k \cdot q-1, \ldots, k-1, k+1, \ldots, p}}{\sigma_{k k \cdot q+1, \ldots, k-1, k+1, \ldots, p}} \\
& =\rho_{i k \cdot q-1, \ldots, k-1, k+1, \ldots, p} \frac{\sigma_{i \cdot q+1, \ldots, k-1, k+1, \ldots, p}}{\sigma_{k \cdot q+1, \ldots, k-1, k+1, \ldots, p}},
\end{aligned}
$$

। $\quad i=1, \ldots, q, \quad k=q+1, \ldots, p$, where $\sigma_{j \cdot q+1}^{2} \ldots . k-1, k+1, \ldots, p= \sigma_{j j \cdot q+1}, \ldots, k-1, k+1, \ldots, p, j=i, k$. [Hint: Prove this for the special case $k=q+1$ by using Problem 2.56 with $p_{1}=q, p_{2}=1, p_{3}=p-q-1$.]
44. (Sec. 2.5) Give a necessary and sufficient condition for $\bar{R}_{i \cdot q+1, \ldots, p}=0$ in terms of $\sigma_{i, q+1}, \ldots, \sigma_{i p}$.
2.45. (Sec. 2.5) Show

$$
1-\bar{R}_{i \cdot q+1, \ldots, p}^{2}=\left(1-\rho_{i p}^{2}\right)\left(1-\rho_{i, p-1 \cdot p}^{2}\right) \cdots\left(1-\rho_{i, q-1 \cdot q+2, \ldots, p}^{2}\right) .
$$

[Hint: Use (19) and (27) successively.]
2.46. (Sec. 2.5) Show

$$
\rho_{i j q+1, \ldots, p}^{2}=\beta_{i j, q+1, \ldots, p} \beta_{j \cdot q+1, \ldots, p}
$$

2.47. (Sec. 2.5) Prove

$$
\rho_{12 \cdot 3 \cdots p}=\frac{-\sigma^{12}}{\sqrt{\sigma^{11} \sigma^{22}}} .
$$

[Hint: Apply Theorem A.3.2 of the Appendix to the cofactors used to calculate $\sigma^{i j}$.]
2.48. (Sec. 2.5) Show that for any joint distribution for which the expectations exist and any function $h\left(x^{(2)}\right)$ that

$$
\mathscr{E}\left(X_{i}-\mathscr{E} X_{i} \mid X^{(2)}\right) h\left(X^{(2)}\right)=0
$$

[Hint: In the above take the expectation first with respect to $X_{i}$ conditional on $X^{(2)}$.]
2.49. (Sec. 2.5) Show that for any function $h\left(x^{(2)}\right)$ and any joint distribution of $X_{t}$ and $X^{(2)}$ for which the relevant expectations exist, $\mathscr{E}\left[X_{i}-h\left(X^{(2)}\right)\right]^{2}=\mathscr{E}\left[X_{i}-\right. \left.g\left(X^{(2)}\right)\right]^{2}+\mathscr{E}\left[g\left(X^{(2)}\right)-h\left(X^{(2)}\right)\right]^{2}$, where $g\left(x^{(2)}\right)=\mathscr{E} X_{i} \mid x^{(2)}$ is the conditional expectation of $X_{i}$ given $X^{(2)}=x^{(2)}$. Hence $g\left(X^{(2)}\right)$ minimizes the mean squared error of prediction. [Hint: Use Problem 2.48.]
2.50. (Sec. 2.5) Show that for any function $h\left(x^{(2)}\right)$ and any joint distribution of $X_{i}$ and $X^{(2)}$ for which the relevant expectations exist, the correlation between $X_{i}$ and $h\left(X^{(2)}\right)$ is not greater than the correlation between $X_{i}$ and $g\left(X^{(2)}\right)$, where $g\left(x^{(2)}\right)=\mathscr{E} X_{i} \mid x^{(2)}$.
2.51. (Sec. 2.5) Show that for any vector function $h\left(x^{(2)}\right)$

$$
\mathscr{E}\left[X^{(1)}-h\left(X^{(2)}\right)\right]\left[X^{(1)}-i\left(X^{(2)}\right)\right]^{\prime}-\mathscr{E}\left[X^{(1)}-\mathscr{E} X^{(1)} \mid X^{(2)}\right]\left[X^{(1)}-\mathscr{E} X^{(1)} \mid X^{(2)}\right]^{\prime}
$$

is positive semidefinite. Note this generalizes Theorem 2.5.3 and Problem 2.49.
2.52. (Sec. 2.5) Verify that $\Sigma_{12} \Sigma_{22}^{-1}=-\Psi_{11}^{-1} \Psi_{12}$, where $\Psi=\Sigma^{-1}$ is partitioned similarly to $\Sigma$.
2.53. (Sec. 2.5) Show

$$
\begin{aligned}
\Sigma^{-1} & =\left(\begin{array}{cc}
\Sigma_{11 \cdot 2}^{-1} & -\Sigma_{11 \cdot 2}^{-1} \Sigma_{12} \Sigma_{22}^{-1} \\
-\Sigma_{22}^{-1} \Sigma_{21} \Sigma_{11 \cdot 2}^{-1} & \Sigma_{22}^{-1} \Sigma_{21} \Sigma_{11 \cdot 2}^{-1} \Sigma_{12} \Sigma_{22}^{-1}+\Sigma_{22}^{-1}
\end{array}\right) \\
& =\left(\begin{array}{cc}
0 & 0 \\
0 & \Sigma_{22}^{-1}
\end{array}\right)+\binom{I}{-\beta^{\prime}} \Sigma_{11 \cdot 2}^{-1}(I-\beta)
\end{aligned}
$$

where $\mathbf{B}=\mathbf{\Sigma}_{12} \mathbf{\Sigma}_{22}^{-1}$. [Hint: Use Theorem A.3.3 of the Appendix and the fact that $\Sigma^{-1}$ is symmetric.]



2.54. (Sec. 2.5) Use Problem 2.53 to show that

$$
x^{\prime} \Sigma^{-1} x=\left(x^{(1)}-\Sigma_{12} \Sigma_{22}^{-1} x^{(2)}\right)^{\prime} \Sigma_{11 \cdot 2}^{-1}\left(x^{(1)}-\Sigma_{12} \Sigma_{22}^{-1} x^{(2)}\right)+x^{(2) \prime} \Sigma_{22}^{-1} x^{(2)} .
$$

2.55. (Sec. 2.5) Show

$$
\begin{aligned}
\mathscr{E}\left(X^{(1)} \mid x^{(2)}, x^{(3)}\right)= & \mu^{(1)}+\Sigma_{13} \Sigma_{33}^{-1}\left(x^{(3)}-\mu^{(3)}\right) \\
& +\left(\Sigma_{12}-\Sigma_{13} \Sigma_{33}^{-1} \Sigma_{32}\right)\left(\Sigma_{22}-\Sigma_{23} \Sigma_{33}^{-1} \Sigma_{32}\right)^{-1} \\
& \cdot\left[x^{(2)}-\mu^{(2)}-\Sigma_{23} \Sigma_{33}^{-1}\left(x^{(3)}-\mu^{(3)}\right)\right] .
\end{aligned}
$$

2.56. (Sec. 2.5) Prove by matrix algebra that

$$
\begin{aligned}
\Sigma_{11}-\left(\Sigma_{12} \Sigma_{13}\right) & \left(\begin{array}{cc}
\Sigma_{22} & \Sigma_{23} \\
\Sigma_{32} & \Sigma_{33}
\end{array}\right)^{-1}\binom{\Sigma_{21}}{\Sigma_{31}}=\Sigma_{11}-\Sigma_{13} \Sigma_{33}^{-1} \Sigma_{31} \\
& -\left(\Sigma_{12}-\Sigma_{13} \Sigma_{33}^{-1} \Sigma_{32}\right)\left(\Sigma_{22}-\Sigma_{23} \Sigma_{33}^{-1} \Sigma_{32}\right)^{-1}\left(\Sigma_{21}-\Sigma_{23} \Sigma_{33}^{-1} \Sigma_{31}\right) .
\end{aligned}
$$

2.57. (Sec. 2.5) Invariance of the partial correlation coefficient. Prove that $\rho_{12,3}, \ldots, p$ is invariant under the transformations $x_{i}^{*}=a_{i} x_{i}+b_{i}^{\prime} x^{(3)}+c_{i}, a_{i}>0, i=1,2, x^{(3) *} \boldsymbol{C} \boldsymbol{C} \boldsymbol{x}^{(\mathbf{3})}+\boldsymbol{d}$, where $\boldsymbol{x}^{(\mathbf{3})}=\left(\boldsymbol{x}_{3}, \ldots, \boldsymbol{x}_{p}\right)^{\prime}$, and that any function of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ that is invariant under these transformations is a function of $\rho_{12 \cdot 3, \ldots} \cdot \rho^{\circ}$.
2.58. (Sec. 2.5) Suppose $X^{(1)}$ and $X^{(2)}$ of $q$ and $p-q$ components, respectively, have the density

$$
\frac{|A|^{\frac{1}{2}}}{(2 \pi)^{\frac{1}{2} p}} e^{-\frac{1}{2} Q},
$$

where

$$
\begin{aligned}
Q= & \left(x^{(1)}-\mu^{(1)}\right)^{\prime} A_{11}\left(x^{(1)}-\mu^{(1)}\right)+\left(x^{(1)}-\mu^{(1)}\right)^{\prime} A_{12}\left(x^{(2)}-\mu^{(2)}\right) \\
& +\left(x^{(2)}-\mu^{(2)}\right)^{\prime} A_{21}\left(x^{(1)}-\mu^{(1)}\right)+\left(x^{(2)}-\mu^{(2)}\right)^{\prime} A_{22}\left(x^{(2)}-\mu^{(2)}\right) .
\end{aligned}
$$

Show that $Q$ can be written as $Q_{1}+Q_{2}$, where
$Q_{1}=\left[\left(x^{(1)}-\mu^{(1)}\right)+A_{11}^{-1} A_{12}\left(x^{(2)}-\mu^{(2)}\right)\right]^{\prime} A_{11}\left[\left(x^{(1)}-\mu^{(1)}\right)+A_{11}^{-1} A_{12}\left(x^{(2)}-\mu^{(2)}\right)\right]$
$Q_{2}=\left(x^{(2)}-\mu^{(2)}\right)^{\prime}\left(A_{22}-A_{21} A_{11}^{-1} A_{12}\right)\left(x^{(2)}-\mu^{(2)}\right)$.
Show that the marginal density of $X^{(2)}$ is

$$
\frac{\left|A_{22}-A_{21} A_{11}^{-1} A_{12}\right|^{\frac{1}{2}}}{(2 \pi)^{\frac{1}{2}(p-q)}} e^{-\frac{1}{2} Q_{2}} .
$$

Show that the conditional density of $X^{(1)}$ given $X^{(2)}=x^{(2)}$ is

$$
\frac{\left|A_{11}\right|^{\frac{1}{2}}}{(2 \pi)^{\frac{1}{2} g}} e^{-\frac{1}{2} Q_{1}}
$$

(without using the Appendix). This problem is meant to furnish an alternative proof of Theorems 2.4.3 and 2.5.1.
2.59. (Sec. 2.6) Prove Lemma 26.2 in detail.
2.60. (Sec. 2.6) Let $\boldsymbol{Y}$ be distributed according to $N(\boldsymbol{0}, \boldsymbol{\Sigma})$. Differentiating the characteristic function, verify (25) and (26).
2.61. (Sec. 2.6) Verify (25) and (26) by using the transformation $\boldsymbol{X}-\boldsymbol{\mu}=\boldsymbol{C Y}$, where $\boldsymbol{\Sigma}=\boldsymbol{C} \boldsymbol{C}^{\prime}$, and integrating the density of $\boldsymbol{Y}$.
2.62. (Sec. 2.6) Let the density of $(X, Y)$ be

$$
\begin{array}{ll}
2 n(x \mid 0,1) n(y \mid 0,1), & 0 \leq y \leq x<\infty, 0 \leq-x \leq y<\infty, \\
0 \leq-y \leq-x<\infty, 0 \leq x \leq-y<\infty, & \text { otherwise. }
\end{array}
$$

Show that $X, Y, X+Y, X-Y$ each have a marginal normal distribution.
2.63. (Sec. 2.6) Suppose $X$ is distributed according to $N(\mathbf{0}, \mathbf{\Sigma})$. Let $\mathbf{\Sigma}=\left(\boldsymbol{\sigma}_{1}, \ldots, \boldsymbol{\sigma}_{p}\right)$. Prove

$$
\begin{aligned}
\mathscr{E}\left(X X^{\prime} \otimes X X^{\prime}\right) & =\Sigma \otimes \Sigma+\operatorname{vec} \Sigma(\operatorname{vec} \Sigma)^{\prime}+\left[\begin{array}{ccc}
\sigma_{1} \sigma_{1}^{\prime} & \cdots & \sigma_{p} \sigma_{1}^{\prime} \\
\vdots & & \vdots \\
\sigma_{1} \sigma_{p}^{\prime} & \cdots & \sigma_{p} \sigma_{p}^{\prime}
\end{array}\right] \\
& =(I+K)(\Sigma \otimes \Sigma)+\operatorname{vec} \Sigma(\operatorname{vec} \Sigma)^{\prime},
\end{aligned}
$$

where

$$
\operatorname{vec} \Sigma=\left[\begin{array}{c}
\sigma_{1} \\
\vdots \\
\sigma_{p}
\end{array}\right], \quad K=\left[\begin{array}{ccc}
\varepsilon_{1} \varepsilon_{1}^{\prime} & \cdots & \varepsilon_{p} \varepsilon_{1}^{\prime} \\
\vdots & & \vdots \\
\varepsilon_{1} \varepsilon_{p}^{\prime} & \cdots & \varepsilon_{p} \varepsilon_{p}^{\prime}
\end{array}\right],
$$

and $\boldsymbol{\varepsilon}_{i}$ is a column vector with 1 in the $i$ th position and 0's elsewhere.
2.64. Complex normal distribution. Let $\left(X^{\prime}, Y^{\prime}\right)^{\prime}$ have a normal distribution with mean vector ( $\left.\mu_{X}^{\prime}, \mu_{Y}^{\prime}\right)^{\prime}$ and covariance matrix

$$
\boldsymbol{\Sigma}=\left(\begin{array}{cc}
\boldsymbol{\Gamma} & -\boldsymbol{\Phi} \\
\boldsymbol{\Phi} & \boldsymbol{\Gamma}
\end{array}\right)
$$

where $\mathbf{\Gamma}$ is positive definite and $\boldsymbol{\Phi}=-\boldsymbol{\Phi}^{\prime}$ (skew symmetric). Then $\mathbf{Z}=\boldsymbol{X}+i \mathbf{Y}$ is said to have a complex normal distribution with mean $\theta=\mu_{X}+i \mu_{Y}$ and covariance matrix $\delta(\mathbf{Z}-\theta)(\mathbf{Z}-\theta)^{*}=\mathbf{P}=\mathbf{Q}+i \mathbf{R}$, where $\mathbf{Z}^{*}=\boldsymbol{X}^{\prime}-i \mathbf{Y}^{\prime}$. Note that $\boldsymbol{P}$ is Hermitian and positive definite.
(a) Show $Q=2 \Gamma$ and $R=2 \Phi$.
(b) Show $|\boldsymbol{P}|^{2}=|2 \boldsymbol{\Sigma}|$. [Hint: $|\boldsymbol{\Gamma}+i \boldsymbol{\Phi}|=|\boldsymbol{\Gamma}-i \boldsymbol{\Phi}|$.]
(c) Show

$$
P^{-1}=\left(Q+R Q^{-1} R\right)^{-1}-i Q^{-1} R\left(Q+R Q^{-1} R\right)^{-1}
$$

Note that the inverse of a Hermitian matrix is Hermitian.
(d) Show that the density of $X$ and $Y$ can be written

$$
\pi^{-p} \mid P^{-1} e^{-(x-0)^{*} P^{-1}(z-0)}
$$

2.65. Complex normal (continued). If $\mathbf{Z}$ has the complex normal distribution of Problem 2.64, show that $W=A Z$, where $A$ is a nonsingular complex matrix, has the complex normal distribution with mean $A \theta$ and covariance matrix $B(W)= A P A^{*}$.
2.66. Show that the characteristic function of $\mathbf{Z}$ defined in Problem 2.64 is

$$
\mathscr{E} e^{f \mathscr{R}\left(u^{*} z\right)}=e^{\prime \mathscr{H} u^{*} 0-u^{*} P u},
$$

where $\mathscr{R}(x+i y)=x$.
2.67. (Sec. 2.2) Show that $\int_{-4}^{a} e^{-x^{1} / 2} d x / \sqrt{2 \pi}$ is approximately $\left(1-e^{-2 a^{2} / \pi}\right)^{1 / 2}$. [Hint: The probability that $(X, Y)$ falls in a square is approximately the probability that ( $X, Y$ ) falls in an approximating circle [Pólya (1949)]]
2.68. (Sec. 2.7) For the multivariate $t$-distribution with density (41) show that $\mathscr{E} X=\mu$ and $\mathscr{E}(X)=[m /(m-2)] \mathbf{A}$.

## CHAPTER 3

## Estimation of the Mean Vector and the Covariance Matrix

### 3.1. INTRODUCTION

The multivariate normal distribution is specified completely by the mean vector $\mu$ and the covariance matrix $\Sigma$. The first statistical problem is how to estimate these parameters on the basis of a sample of observations. In Section 3.2 it is shown that the maximum likelihood estimator of $\boldsymbol{\mu}$ is the sample mean; the maximum likelihood estimator of $\mathbf{\Sigma}$ is proportional to the matrix of sample variances and covariances. A sample variance is a sum of squares of deviations of observations from the sample mean divided by one less than the number of observations in the sample; a sample covariance is similarly defined in terms of cross products. The sample covariance matrix is an unbiased estimator of $\Sigma$.

The distribution of the sample mean vector is given in Section 3.3, and it is shown how one can test the hypothesis that $\mu$ is a given vector when $\Sigma$ is known. The case of $\Sigma$ unknown will be treated in Chapter 5.

Some theoretical properties of the sample mean are given in Section 3.4, and the Baves estimator of the population mean is derived for a normal a priori distribution. In Section 3.5 the James-Stein estimator is introduced; improvements over the simple mean for the mean squared error loss function are discussed.

In Section 3.6 estimators of the mean vector and covariance matrix of elliptically contoured distributions and the distributions of the estimators are treated.

[^0]
### 3.2. THE MAXIMUM LIKELIHOOD ESTIMATORS OF THE MEAN VECTOR AND THE COVARIANCE MATRIX

Given a sample of (vector) observations from a $p$-variate (nondegenerate) normal distribution, we ask for estimators of the mean vector $\mu$ and the covariance matrix $\mathbf{\Sigma}$ of the distribution. We shall deduce the maximum likelihood estimators.

It turns out that the method of maximum likelihood is very useful in various estimation and hypothesis testing problems concerning the multivariate normal distribution. The maximum likelihood estimators or modifications of them often have some optimum properties. In the particular case studied here, the estimators are asymptotically efficient [Cramér (1946), Sec. 33.3].

Suppose our sample of $N$ observations on $\boldsymbol{X}$ distributed according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}$, where $N>p$. The likelihood function is

$$
\begin{aligned}
L & =\prod_{\alpha=1}^{N} n\left(x_{\alpha} \mid \mu, \Sigma\right) \\
& =\frac{1}{(2 \pi)^{\frac{1}{2} p N}|\Sigma|^{\frac{1}{2} N}} \exp \left[-\frac{1}{2} \sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu\right)^{\prime} \Sigma^{-1}\left(x_{\alpha}-\mu\right)\right]
\end{aligned}
$$

In the likelihood function the vectors $x_{1}, \ldots, x_{N}$ are fixed at the sample values and $L$ is a function of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$. To emphasize that these quantities are variables (and not parameters) we shall denote them by $\boldsymbol{\mu}^{*}$ and $\boldsymbol{\Sigma}^{*}$. Then the logarithm of the likelihood function is

$$
\begin{aligned}
\log L= & -\frac{1}{2} p N \log 2 \pi-\frac{1}{2} N \log \left|\Sigma^{*}\right| \\
& -\frac{1}{2} \sum_{\alpha=1}^{N}\left(\boldsymbol{x}_{\alpha}-\boldsymbol{\mu}^{*}\right)^{\prime} \Sigma^{*-1}\left(\boldsymbol{x}_{\alpha}-\boldsymbol{\mu}^{*}\right) .
\end{aligned}
$$

Since $\log L$ is an increasing function of $L$, its maximum is at the same point in the space of $\mu^{*}, \Sigma^{*}$ as the maximum of $L$. The maximum likelihcod estimators of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are the vector $\boldsymbol{\mu}^{*}$ and the positive definite matrix $\boldsymbol{\Sigma}^{*}$ that maximize $\log L$. (It remains to be seen that the supremum oi $\log L$ is attained for a positive definite matrix $\Sigma^{*}$.)

Let the sample mean vector be

$$
\overline{\mathrm{x}}=\frac{1}{N} \sum_{\alpha=1}^{N} \mathrm{x}_{\alpha}=\left(\begin{array}{c}
\frac{1}{N} \sum_{\alpha=1}^{N} x_{1 \alpha} \\
\vdots \\
\frac{1}{N} \sum_{\alpha=1}^{N} x_{p \alpha}
\end{array}\right)=\left(\begin{array}{c}
\bar{x}_{1} \\
\vdots \\
\bar{x}_{p}
\end{array}\right),
$$

where $x_{\alpha}=\left(x_{1 \alpha}, \ldots, x_{p \alpha}\right)^{\prime}$ and $\bar{x}_{1}=\sum_{\alpha=1}^{N} x_{i \alpha} / N$, and let the matrix of sums of squares and cross products of deviations about the mean be

$$
\begin{aligned}
A & =\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime} \\
& =\left[\sum_{\alpha=1}^{N}\left(x_{i \alpha}-\bar{x}_{i}\right)\left(x_{j \alpha}-\bar{x}_{j}\right)\right], \quad i, j=1, \ldots, p .
\end{aligned}
$$

It will be convenient to use the following lemma:

Lemma 3.2.1. Let $x_{1}, \ldots, x_{N}$ be $N$ ( $p$-component) vectors, and let $\bar{x}$ be defined by (3). Then for any vector $b$

$$
\sum_{\alpha=1}^{N}\left(x_{\alpha}-b\right)\left(x_{\alpha}-b\right)^{\prime}=\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}+N(\bar{x}-b)(\bar{x}-b)^{\prime} .
$$

## Proof

(6)

$$
\begin{aligned}
\sum_{\alpha=1}^{N}\left(x_{\alpha}-b\right)\left(x_{\alpha}-b\right)^{\prime}= & \sum_{\alpha=1}^{N}\left[\left(x_{\alpha}-\bar{x}\right)+(\bar{x}-b)\right]\left[\left(x_{\alpha}-\bar{x}\right)+(\bar{x}-b)\right]^{\prime} \\
= & \sum_{\alpha=1}^{N}\left[\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}+\left(x_{\alpha}-\bar{x}\right)(\bar{x}-b)^{\prime}\right. \\
& \left.+(\bar{x}-b)\left(x_{\alpha}-\bar{x}\right)^{\prime}+(x-x b)(\bar{x}-b)^{\prime}\right] \\
= & \sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}+\left[\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\right](\bar{x}-b)^{\prime} \\
& +(\bar{x}-b) \sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)^{\prime}+N(\bar{x}-b)(\bar{x}-b)^{\prime}
\end{aligned}
$$

The second and third terms on the right-hand side are 0 because $\sum\left(x_{\alpha}-\bar{x}\right)= \sum x_{\alpha}-N \bar{x}=0$ by (3).

When we let $\boldsymbol{b}=\boldsymbol{\mu}^{*}$, we have

$$
\begin{aligned}
\sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu^{*}\right)\left(x_{\alpha}-\mu^{*}\right)^{\prime} & =\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}+N\left(\bar{x}-\mu^{*}\right)\left(\bar{x}_{x^{\prime}}-\mu^{*}\right)^{\prime} \\
& =A+N\left(\bar{x}-\mu^{*}\right)\left(\bar{x}-\mu^{*}\right)^{\prime}
\end{aligned}
$$

Using this result and the properties of the trace of a matrix ( $\operatorname{tr} C D=\Sigma c_{i j} d_{p} =\operatorname{tr} D C$ ), we have
(8)

$$
\begin{aligned}
\sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu^{*}\right)^{\prime} \Sigma^{*-1}\left(x_{\alpha}-\mu^{*}\right) & =\operatorname{tr} \sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu^{*}\right)^{\prime} \Sigma^{*-1}\left(x_{\alpha}-\mu^{*}\right) \\
& =\operatorname{tr} \sum_{\alpha=1}^{N} \Sigma^{*-1}\left(x_{\alpha}-\mu^{*}\right)\left(x_{\alpha}-\mu^{*}\right)^{\prime} \\
& =\operatorname{tr} \Sigma^{*-1} A+\operatorname{tr} \Sigma^{*-1} N\left(\bar{x}-\mu^{*}\right)\left(\bar{x}-\mu^{*}\right)^{\prime} \\
& =\operatorname{tr} \Sigma^{*-1} A+N\left(\bar{x}-\mu^{*}\right)^{\prime} \Sigma^{*-1}\left(\bar{x}-\mu^{*}\right)
\end{aligned}
$$

Thus we can write (2) as

$$
\begin{aligned}
\log L= & -\frac{1}{2} p N \log (2 \pi)-\frac{1}{2} N \log \left|\Sigma^{*}\right| \\
& -\frac{1}{2} \operatorname{tr} \Sigma^{*-1} A-\frac{1}{2} N\left(\bar{x}-\mu^{*}\right)^{\prime} \Sigma^{*-1}\left(\bar{x}-\mu^{*}\right) .
\end{aligned}
$$

Since $\Sigma^{*}$ is positive definite, $\Sigma^{*-1}$ is positive definite, and $N(\bar{x}- \left.\boldsymbol{\mu}^{*}\right)^{\prime} \boldsymbol{\Sigma}^{*-1}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}^{*}\right) \geq 0$ and is 0 if and only if $\boldsymbol{\mu}^{*}=\overline{\boldsymbol{x}}$. To maximize the second and third terms of (9) we use the following lemma (which is also used in later chapters):

Lemma 3.2.2. If $D$ is positive definite of order $p$, the maximum of

$$
f(\boldsymbol{G})=N|\log | \boldsymbol{G} \mid-\operatorname{tr} \boldsymbol{G}^{-1} \boldsymbol{D}
$$

with respect to positive definite matrices $G$ exists, occurs at $G=(1 / N) D$, and has the value

$$
f[(1 / N) D]=p N \log N-N \log |D|-p N .
$$

Proof. Let $D=E E^{\prime}$ and $E^{\prime} G^{-1} E=H$. Ther $G=E H^{-1} E^{\prime}$, and $|G|=|E| \cdot\left|H^{-1}\right| \cdot\left|E^{\prime}\right|=\left|H^{-1}\right| \cdot\left|E E^{\prime}\right|=|D| /|H|$, and $\operatorname{tr} G^{-1} D=\operatorname{tr} G^{-1} E E^{\prime}= \operatorname{tr} E^{\prime} G^{-1} E=\operatorname{tr} H$. Then the function to be maximized (with respect to positive definite $\boldsymbol{H}$ ) is

$$
f=-N \log |D|+N \log |H|-\operatorname{tr} H .
$$

Let HT. TT, where $T$ is lower triangular (Corollary A.1.7). Then the maximum of

$$
\begin{aligned}
f & =-N \log |D|+N \log |T|^{2}-\operatorname{tr} T T^{\prime} \\
& =-N \log |D|+\sum_{i=1}^{p}\left(N \log t_{i i}^{2}-t_{i i}^{2}\right)-\sum_{i>j} t_{i j}^{2}
\end{aligned}
$$

occurs at $t_{n}^{2}=N, t_{n}=0, i \neq j$; that is, at $H=N I$. Then $G=(1 / N) E E^{\prime}= (1 / N) D$.

Theorem 3.2.1. If $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}$ constitute a sample from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with $p<N$, the maximum likelihood estimators of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are $\hat{\boldsymbol{\mu}}=\overline{\boldsymbol{x}}=(1 / N) \Sigma_{\alpha=1}^{N} \boldsymbol{x}_{\alpha}$ and $\hat{\Sigma}=(1 / N) \sum_{\alpha \cdot 1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}$, respectively.

Other methods of deriving the maximum likelihood estimators have been discussed by Anderson and Olkin (1985). See Problems 3.4, 3.8, and 3.12.

Computation of the estimate $\hat{\mathbf{\Sigma}}$ is made easier by the specialization of Lemma 3.2.1 ( $\boldsymbol{b}=\mathbf{0}$ )

$$
\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}=\sum_{\alpha=1}^{N} x_{\alpha} x_{\alpha}^{\prime}-N \bar{x} \bar{x}^{\prime}
$$

An element of $\sum_{\alpha=1}^{N} x_{\alpha} x_{\alpha}^{\prime}$ is computed as $\sum_{\alpha=1}^{N} x_{t \alpha} x_{j \alpha}$, and an element of $N \bar{x} \bar{x}^{\prime}$ is computed as $N \bar{x}_{1} \bar{x}$, or $\left(\sum_{\alpha=1}^{N} x_{1 \alpha}\right)\left(\sum_{\alpha=1}^{N} x_{j \alpha}\right) / N$. It should be noted that if $N>p$. the probability is 1 of drawing a sample so that (14) is positive definite; see Problem 3.17.

The covariance matrix can be written in terms of the variances or standard deviations and correlation coefficients. These are uniquely defined by the variances and covariances. We assert that the maximum likelihood estimators of functions of the parameters are those functions of the maximum likelihood estimators of the parameters.

Lemma 3.2.3. Let $f(\theta)$ be a real-valued function defined on a set $S$, and let $\phi$ be a single-valued function, with a single-valued inverse, on $S$ to a set $S^{*}$; that is, to each $\theta \in S$ there corresponds a unique $\theta^{*} \in S^{*}$, and, conversely, to each $\theta^{*} \in S^{*}$ there corresponds a unique $\theta \in S$. Let

$$
g\left(\theta^{*}\right)=f\left[\phi^{-1}\left(\theta^{*}\right)\right]
$$

Then if $f(\theta)$ attains a maximum at $\theta=\theta_{0}, g\left(\theta^{*}\right)$ attains a maximum at $\theta^{*}=\theta_{0}^{*}=\phi\left(\theta_{0}\right)$. If the maximum of $f(\theta)$ at $\theta_{0}$ is unique, so is the maximum of $g\left(\theta^{*}\right)$ at $\theta_{0}^{*}$.

Proof. By hypothesis $f\left(\theta_{0}\right) \geq f(\theta)$ for all $\theta \in S$. Then for any $\theta^{*} \in S^{*}$

$$
g\left(\theta^{*}\right)=\int\left[\phi^{-1}\left(\theta^{*}\right)\right]=f(\theta) \leq f\left(\theta_{0}\right)=g\left[\phi\left(\theta_{0}\right)\right]=g\left(\theta_{11}^{*}\right) .
$$

Thus $g\left(\theta^{*}\right)$ attains a maximum at $\theta_{0}^{*}$. If the maximum of $f(\theta)$ at $\theta_{0}$ is unique, there is strict inequality above for $\theta \neq \theta_{0}$, and the maximum of $g\left(\theta^{*}\right)$ is unique.

We have the following corollary:

Corollary 3.2.1. If on the basis of a given sample $\hat{\theta}_{1}, \ldots, \hat{\theta}_{m}$ are maximum likelihood estimators of the parameters $\theta_{1}, \ldots, \theta_{m}$ of a distribution, then $\phi_{1}\left(\hat{\theta}_{1}, \ldots, \hat{\theta}_{m}\right), \ldots, \phi_{m}\left(\hat{\theta}_{1}, \ldots, \hat{\theta}_{m}\right)$ are maximum likelihood estiruators of $\phi_{1}\left(\theta_{1}, \ldots, \theta_{m}\right), \ldots, \phi_{m}\left(\theta_{1}, \ldots, \theta_{m}\right)$ if the transformation from $\theta_{1}, \ldots, \theta_{m}$ to $\phi_{1}, \ldots, \phi_{m}$ is one-to-one. If the estimators of $\theta_{1}, \ldots, \theta_{m}$ are unique, then the estimators of $\phi_{1}, \ldots, \phi_{m}$ are unique.

Corollary 3.2.2. If $\mathbf{x}_{1}, \ldots, \mathbf{x}_{N}$ constitutes a sample from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, where $\sigma_{i j}=\sigma_{i} \sigma_{j} \rho_{i j}\left(\rho_{i i}=1\right)$, then the maximum likelihood estimator of $\boldsymbol{\mu}$ is $\hat{\boldsymbol{\mu}}=\overline{\boldsymbol{x}}= (1 / N) \Sigma_{\alpha} x_{\alpha}$; the maximum likelihood estimator of $\sigma_{i}^{2}$ is $\hat{\sigma}_{i}^{2}=(1 / N) \Sigma_{\alpha}\left(x_{i \alpha}-\right. \left.\bar{x}_{i}\right)^{2}=(1 / N)\left(\Sigma_{\alpha} x_{1 \alpha}^{2}-N \bar{x}_{i}^{2}\right)$, where $x_{i \alpha}$ is the ith component of $x_{\alpha}$ and $\bar{x}_{i}$ is the $i$ th component of $\bar{x}$; and the maximum likelihood estimator of $\rho_{i j}$ is

$$
\begin{aligned}
\hat{\rho}_{i j} & =\frac{\sum_{\alpha=1}^{N}\left(x_{i \alpha}-\bar{x}_{i}\right)\left(x_{j \alpha}-\bar{x}_{j}\right)}{\sqrt{\sum_{\alpha=1}^{N}\left(x_{i \alpha}-\bar{x}_{i}\right)^{2}} \sqrt{\sum_{\alpha=1}^{N}\left(x_{j \alpha}-\bar{x}_{j}\right)^{2}}} \\
& =\frac{\sum_{\alpha=1}^{N} x_{i \alpha} x_{j \alpha}-N \bar{x}_{i} \bar{x}}{\sqrt{\sum_{\alpha=1}^{N} x_{i \alpha}^{2}-N \bar{x}_{i}^{2}} \sqrt{\sum_{\alpha=1}^{N} x_{j \alpha}^{2}-N \bar{x}_{j}^{2}}} .
\end{aligned}
$$

Proof. The set of parameters $\mu_{1}=\mu_{i}, \sigma_{i}^{2}=\sigma_{i t}$, and $\rho_{i j}=\sigma_{i j} / \sqrt{\sigma_{i i} \sigma_{j j}}$ is a one-to-one transform of the set of parameters $\mu_{i}$ and $\sigma_{i j}$. Therefore, by Corollary 3.2.1 the estimator of $\mu_{i}$ is $\hat{\mu}_{i}$, of $\sigma_{i}{ }^{2}$ is $\hat{\sigma}_{i j}$, and of $\rho_{1 j}$ is

$$
\hat{\rho}_{i j}=\frac{\hat{\sigma}_{i j}}{\sqrt{\hat{\sigma}_{i i} \hat{\sigma}_{j j}}},
$$

Pearson (1896) gave a justification for this estimator of $\rho_{i}$, and (17) is sometimes called the Pearson correlation coefficient. It is also called the simple correlation coefficient. It is usually denoted by $r_{1}$.
${ }^{\dagger}$ The assumption that the transformation is one-to-onc is made so that the set $\phi_{1}, \ldots, \phi_{m}$ uniquely defines the likelihood. An alternative in case $\theta^{*}=\phi(\theta)$ does not have a unique inverse is to define $s\left(\theta^{*}\right)=\left(\theta: \phi(\theta)=\theta^{*}\right)$ and $g\left(\theta^{*}\right)=\sup f(\theta) \mid \theta \in S\left(\theta^{*}\right)$, which is considered the "induced likelihood" when $f(\theta)$ is the likelihood function. Then $\hat{\theta}^{*}=\phi(\hat{\theta})$ maximizes $g\left(\theta^{*}\right)$, for $g\left(\theta^{*}\right)=\sup f(\theta)\left|\theta \in S\left(\theta^{*}\right) \geq \sup f(\theta)\right| \theta \in S=f(\hat{\theta})=g\left(\hat{\theta}^{*}\right)$ for all $\theta^{*} \in S^{*}$. [See, e.g., Zehna (1966). 1

![](https://cdn.mathpix.com/cropped/ea6dc2c4-db5d-4760-b8fb-75b4fec65223-090.jpg?height=296&width=738&top_left_y=235&top_left_x=437)
Figure 3.1

A convenient geometrical interpretation of this sample $\left(x_{1}, x_{2}, \ldots, x_{N}\right)=X$ s is in terms of the rows of $\boldsymbol{X}$. Let

$$
X=\left(\begin{array}{ccc}
x_{11} & \cdots & x_{1 N} \\
\vdots & & \vdots \\
x_{p t} & \cdots & x_{p N}
\end{array}\right)=\left(\begin{array}{c}
u_{1}^{\prime} \\
\vdots \\
u_{p}^{\prime}
\end{array}\right) ;
$$

that is, $u_{i}^{\prime}$ is the $i$ th row of $\boldsymbol{X}$. The vector $u_{i}$ can be considered as a vector in an $N$-dimensional space with the $\alpha$ th coordinate of one endpoint being $x_{1 \alpha}$ and the other endpoint at the origin. Thus the sample is represented by $p$ vectors in $N$-dimensional Euclidean space. By definition of the Euclidean metric, the squared length of $u_{i}$ (that is, the squared distance of one endpoint from the other) is $u_{i}^{\prime} u_{i}=\sum_{\alpha-1}^{N} x_{i \alpha}^{2}$.

Now let us show that the cosine of the angle between $\boldsymbol{u}_{i}$ and $\boldsymbol{u}_{j}$ is $u_{i}^{\prime} u_{j} / \sqrt{u_{i}^{\prime} u_{i} u_{j}^{\prime} u_{j}}=\sum_{\alpha=1}^{N} x_{i \alpha} x_{j \alpha} / \sqrt{\sum_{\alpha=1}^{N} x_{i \alpha}^{2} \sum_{\alpha=1}^{N} x_{j \alpha}^{2}}$. Choose the scalar $d$ so the vector $d u_{j}$ is orthogonal to $u_{i}-d u_{j}$; that is, $0=d u_{j}^{\prime}\left(u_{i}-d u_{j}\right)=d\left(u_{j}^{\prime} u_{i}-\right. \left.d u_{j}^{\prime} u_{j}\right)$. Therefore, $d=u_{j}^{\prime} u_{i} / u_{j}^{\prime} u_{j}$. We decompose $u_{i}$ into $u_{i}-d u_{j}$ and $d u_{j} \left[u_{i}=\left(u_{i}-d u_{j}\right)+d u_{j}\right]$ as indicated in Figure 3.1. The absolute value of the cosine of the angle between $u_{i}$ and $u_{j}$ is the length of $d u_{j}$ divided by the length of $u_{i}$; that is, it is $\sqrt{d u_{j}^{\prime}\left(d u_{j}\right) / u_{i}^{\prime} u_{i}}=\sqrt{d u_{j}^{\prime} u_{j} d / u_{i}^{\prime} u_{i}}$; the cosine is $\boldsymbol{u}_{i}^{\prime} \boldsymbol{u}_{j} / \sqrt{\boldsymbol{u}_{i}^{\prime} \boldsymbol{u}_{i} \boldsymbol{u}_{i}^{\prime} \boldsymbol{u}_{j}}$. This proves the desired result.

To give a geometric interpretation of $a_{i i}$ and $a_{i j} / \sqrt{a_{i i} a_{j j}}$, we introduce the equiangular line, which is the line going through the origin and the point $(1,1, \ldots, 1)$. See Figure 3.2. The projection of $u_{i}$ on the vector $\varepsilon=(1,1, \ldots, 1)^{\prime}$ is $\left(\varepsilon^{\prime} u_{i} / \varepsilon^{\prime} \varepsilon\right) \varepsilon=\left(\sum_{\alpha} x_{i \alpha} / \sum_{\alpha} 1\right) \varepsilon=\bar{x}_{i} \varepsilon=\left(\bar{x}_{i}, \bar{x}_{i}, \ldots, \bar{x}_{i}\right)^{\prime}$. Then we decompose $u_{i}$ into $\bar{x}_{i} \varepsilon$, the projection on the equiangular line, and $u_{i}-\bar{x}_{i} \varepsilon$, the projection of $\boldsymbol{u}_{l}$ on the plane perpendicular to the equiangular line. The squared length of $u_{i}-\bar{x}_{i} \varepsilon$ is $\left(u_{j}-\bar{x}_{i} \varepsilon\right)^{\prime}\left(u_{i}-\bar{x}_{i} \varepsilon\right)=\sum_{\alpha}\left(x_{i \alpha}-\bar{x}_{i}\right)^{2}$; this is $N \hat{\sigma}_{i i}=a_{i i}$. Translate $u_{i}-\bar{x}_{j} \varepsilon$ and $u_{j}-\bar{x}_{j} \mathrm{e}$, so that each vector has an endpoint at the origin; the $\alpha$ th coordinate of the first vector is $x_{i \alpha}-\bar{x}_{l}$, and of


[^0]:    An Introduction to Multivariate Statistical Analysis, Third Edition. By T. W. Anderson ISBN 0-471-36091-0 Copyright © 2003 John Wiley \& Sons, Inc.



![](https://cdn.mathpix.com/cropped/dbd68db4-4e6d-4608-b6d5-72fb2dab0a2c-091.jpg?height=555&width=1001&top_left_y=173&top_left_x=307)
Figure 3.2

the second is $x_{j \alpha}-\bar{x}_{j}$. The cosine of the angle between these two vectors is

$$
\begin{aligned}
r_{i j} & =\frac{\left(u_{j}-\bar{x}_{i} \varepsilon\right)^{\prime}\left(u_{j}-\bar{x}_{j} \varepsilon\right)}{\sqrt{\left(u_{i}-\bar{x}_{i} \varepsilon\right)^{\prime}\left(u_{i}-\bar{x}_{i} \varepsilon\right)\left(u_{j}-\bar{x}_{j} \varepsilon\right)^{\prime}\left(u_{j}-\bar{x}_{j} \varepsilon\right)}} \\
& =\frac{\sum_{\alpha=1}^{N}\left(x_{i \alpha}-\bar{x}_{i}\right)\left(x_{j \alpha}-\bar{x}_{j}\right)}{\sqrt{\sum_{\alpha=1}^{N}\left(x_{j \alpha}-\bar{x}_{i}\right)^{2} \sum_{\alpha=1}^{N}\left(x_{j \alpha}-\bar{x}_{j}\right)^{2}}} .
\end{aligned}
$$

As an example of the calculations consider the data in Table 3.1 and graphed in Figure 3.3, taken from Student(1908). The measurement $x_{11}=1.9$ on the first patient is the increase in the number of hours of sleep due to the use of the sedative $A, x_{21}=0.7$ is the increase in the number of hours due to

Table 3.1. Increase in Sleep
| Patient | Drug $A$ <br> $x_{1}$ | Drug $B$ <br> $x_{2}$ |
| :---: | :---: | :---: |
| 1 | 1.9 | 0.7 |
| 2 | 0.8 | -1.6 |
| 3 | 1.1 | -0.2 |
| 4 | 0.1 | -1.2 |
| 5 | -0.1 | -0.1 |
| 6 | 4.4 | 3.4 |
| 7 | 5.5 | 3.7 |
| 8 | 1.6 | 0.8 |
| 9 | 4.6 | 0.0 |
| 10 | 3.4 | 2.0 |


![](https://cdn.mathpix.com/cropped/dbd68db4-4e6d-4608-b6d5-72fb2dab0a2c-092.jpg?height=934&width=983&top_left_y=228&top_left_x=331)
Figure 3.3. Increase in sleep.

sedative $\boldsymbol{B}$, and so on. Assuming that each pair (i.e., each row in the table) is an observation from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, we find that

$$
\begin{aligned}
& \hat{\boldsymbol{\mu}}=\overline{\boldsymbol{x}}=\binom{2.33}{0.75}, \\
& \hat{\mathbf{\Sigma}}=\left(\begin{array}{ll}
3.61 & 2.56 \\
2.56 & 2.88
\end{array}\right), \\
& S=\left(\begin{array}{ll}
4.01 & 2.85 \\
2.85 & 3.20
\end{array}\right),
\end{aligned}
$$

and $\hat{\rho}_{12}=r_{12}=0.7952$. ( $S$ will be defined later.)

### 3.3. THE DISTRIBUTION OF THE SAMPLE MEAN VECTOR; INFERENCE CONCERNING THE MEAN WHEN THE COVARIANCE MATRIX IS KNOWN

### 3.3.1. Distribution Theory

In the univariate case the mean of a sample is distributed normally and independently of the sample variance. Similarly, the sample mean $\bar{X}$ defined in Section 3.2 is distributed normally and independently of $\hat{\mathbf{\Sigma}}$.

To prove this result we shall make a transformation of the set of observation vectors. Because this kind of transformation is used several times in this book, we first prove a more general theorem.

Theorem 3.3.1. Suppose $X_{1}, \ldots, X_{N}$ are independent, where $X_{\alpha}$ is distributed according to $N\left(\boldsymbol{\mu}_{\alpha}, \boldsymbol{\Sigma}\right)$. Let $\boldsymbol{C}=\left(c_{\alpha \beta}\right)$ be an $N \times N$ orthogonal matrix. Then $\boldsymbol{Y}_{\alpha}=\sum_{\beta=1}^{N} c_{\alpha \beta} \boldsymbol{X}_{\beta}$ is distributed according to $N\left(\boldsymbol{\nu}_{\alpha}, \boldsymbol{\Sigma}\right)$, where $\boldsymbol{\nu}_{\alpha}= \sum_{\beta=1}^{N} c_{\alpha \beta} \boldsymbol{\mu}_{\beta}, \alpha=1, \ldots, N$, and $\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{N}$ are independent.

Proof. The set of vectors $Y_{1}, \ldots, Y_{N}$ have a joint normal distribution, because the entire set of components is a set of linear combinations of the components of $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{N}$, which have a joint normal distribution. The expected value of $\boldsymbol{Y}_{\alpha}$ is

$$
\begin{aligned}
\mathscr{E} Y_{\alpha} & =\mathscr{E} \sum_{\beta=1}^{N} c_{\alpha \beta} X_{\beta}=\sum_{\beta=1}^{N} c_{\alpha \beta} \mathscr{E} X_{\beta} \\
& =\sum_{\beta=1}^{N} c_{\alpha \beta} \boldsymbol{\mu}_{\beta}=\boldsymbol{\nu}_{\alpha} .
\end{aligned}
$$

The covariance matrix between $Y_{\alpha}$ and $Y_{\gamma}$ is

$$
\begin{aligned}
\mathscr{C}\left(\boldsymbol{Y}_{\alpha}, \boldsymbol{Y}_{\gamma}^{\prime}\right) & =\mathscr{E}\left(\boldsymbol{Y}_{\alpha}-\boldsymbol{v}_{\alpha}\right)\left(\boldsymbol{Y}_{\gamma}-\boldsymbol{v}_{\gamma}\right)^{\prime} \\
& =\mathscr{E}\left[\sum_{\beta=1}^{N} c_{\alpha \beta}\left(\boldsymbol{X}_{\beta}-\boldsymbol{\mu}_{\beta}\right)\right]\left[\sum_{\varepsilon=1}^{N} c_{\gamma \delta}\left(\boldsymbol{X}_{\varepsilon}-\boldsymbol{\mu}_{\varepsilon}\right)^{\prime}\right] \\
& =\sum_{\beta, \varepsilon=1}^{N} c_{\alpha \beta} c_{\gamma \varepsilon} \mathscr{E}\left(\boldsymbol{X}_{\beta}-\boldsymbol{\mu}_{\beta}\right)\left(\boldsymbol{X}_{\varepsilon}-\boldsymbol{\mu}_{\varepsilon}\right)^{\prime} \\
& =\sum_{\beta, \varepsilon=1}^{N} c_{\alpha \beta} c_{\gamma \varepsilon} \delta_{\beta \varepsilon} \boldsymbol{\Sigma} \\
& =\sum_{\beta=1}^{N} c_{\alpha \beta} c_{\gamma \beta} \boldsymbol{\Sigma} \\
& =\delta_{\alpha \gamma} \boldsymbol{\Sigma}
\end{aligned}
$$

where $\delta_{\alpha \gamma}$ is the Kronecker delta ( $=1$ if $\alpha=\gamma$ and $=0$ if $\alpha \neq \gamma$ ). This shows that $\boldsymbol{Y}_{\boldsymbol{\alpha}}$ is independent of $\boldsymbol{Y}_{\boldsymbol{\gamma}}, \alpha \neq \gamma$, and $\boldsymbol{Y}_{\boldsymbol{\alpha}}$ has the covariance matrix $\Sigma$. $\square$

We also use the following general lemma:
Lemma 3.3.1. If $C=\left(c_{\alpha \beta}\right)$ is orthogonal, then $\sum_{\alpha=1}^{N} x_{\alpha} x_{\alpha}^{\prime}=\sum_{\alpha=1}^{N} y_{\alpha} y_{\alpha}^{\prime}$, where $y_{\alpha}=\sum_{\beta=1}^{N} c_{\alpha \beta} x_{\beta}, \alpha=1, \ldots, N$.

Proof

$$
\begin{aligned}
\sum_{\alpha=1}^{N} y_{\alpha} y_{\alpha}^{\prime} & =\sum_{\alpha} \sum_{\beta} c_{\alpha \beta} x_{\beta} \sum_{\gamma} c_{\alpha \gamma} x_{\gamma}^{\prime} \\
& =\sum_{\beta, \gamma}\left(\sum_{\alpha} c_{\alpha \beta} c_{\alpha \gamma}\right) x_{\beta} x_{\gamma}^{\prime} \\
& =\sum_{\beta, \gamma} \delta_{\beta \gamma} x_{\beta} x_{\gamma}^{\prime} \\
& =\sum_{\beta} x_{\beta} x_{\beta}^{\prime}
\end{aligned}
$$

Let $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{N}$ be independent, each distributed according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. There exists an $N \times N$ orthogonal matrix $B=\left(b_{\alpha \beta}\right)$ with the last row

$$
(1 / \sqrt{N}, \ldots, 1 / \sqrt{N}) .
$$

(See Lemma A.4.2.) This transformation is a rotation in the $N$-dimensional space described in Section 3.2 with the equiangular line going into the $N$ th coordinate axis. Let $\boldsymbol{A}=N \hat{\boldsymbol{\Sigma}}$, defined in Section 3.2, and let

$$
Z_{\alpha}=\sum_{\beta=1}^{N} b_{\alpha \beta} X_{\beta} .
$$

Then

$$
\boldsymbol{Z}_{N}=\sum_{\beta=1}^{N} b_{N \beta} \boldsymbol{X}_{\beta}=\sum_{\beta=1}^{N} \frac{1}{\sqrt{N}} \boldsymbol{X}_{\beta}=\sqrt{N} \overline{\boldsymbol{X}} .
$$

By Lemma 3.3.1 we have

$$
\begin{aligned}
A & =\sum_{\alpha=1}^{N} X_{\alpha} X_{\alpha}^{\prime}-N \bar{X} \bar{X}^{\prime} \\
& =\sum_{\alpha=1}^{N} Z_{\alpha} Z_{\alpha}^{\prime}-Z_{N} Z_{N}^{\prime} \\
& =\sum_{\alpha=1}^{N-1} Z_{\alpha} Z_{\alpha}^{\prime}
\end{aligned}
$$

Since $\boldsymbol{Z}_{N}$ is independent of $\boldsymbol{Z}_{1}, \ldots, \boldsymbol{Z}_{N-1}$, the mean vector $\overline{\boldsymbol{X}}$ is independent of $A$. Since

$$
\mathscr{E} \mathbf{Z}_{N}=\sum_{\beta=1}^{N} b_{N \beta} \mathscr{E} \boldsymbol{X}_{\beta}=\sum_{\beta=1}^{N} \frac{1}{\sqrt{N}} \boldsymbol{\mu}=\sqrt{N} \boldsymbol{\mu},
$$

$\boldsymbol{Z}_{N}$ is distributed according to $N(\sqrt{N} \boldsymbol{\mu}, \boldsymbol{\Sigma})$ and $\overline{\boldsymbol{X}}=(1 / \sqrt{N}) \boldsymbol{Z}_{N}$ is distributed according to $N[\mu,(1 / N) \Sigma]$. We note

$$
\begin{aligned}
\mathscr{E} Z_{\alpha} & =\sum_{\beta=1}^{N} b_{\alpha \beta} \mathscr{E} X_{\beta}=\sum_{\beta=1}^{N} b_{\alpha \beta} \boldsymbol{\mu} \\
& =\sum_{\beta=1}^{N} b_{\alpha \beta} b_{N \beta} \sqrt{N} \boldsymbol{\mu} \\
& =0, \quad \alpha \neq N .
\end{aligned}
$$

Theorem 3.3.2. The mean of a sample of size $N$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is distributed according to $N[\boldsymbol{\mu},(1 / N) \boldsymbol{\Sigma}]$ and independently of $\hat{\boldsymbol{\Sigma}}$, the maximum likelihood estimator of $\mathbf{\Sigma} . N \hat{\mathbf{\Sigma}}$ is distributed as $\sum_{\alpha=1}^{N-1} \boldsymbol{Z}_{\alpha} \boldsymbol{Z}_{\alpha}^{\prime}$, where $\boldsymbol{Z}_{\alpha}$ is distributed according to $N(\mathbf{0}, \mathbf{\Sigma}), \alpha=1, \ldots, N-1$, and $\mathbf{Z}_{1}, \ldots, Z_{N-1}$ are independent.

Definition 3.3.1. An estimator $t$ of a parameter vector $\theta$ is unbiased if and only if $\mathscr{E}_{\theta} t=\boldsymbol{\theta}$.

Since $\mathscr{E} \bar{X}=(1 / N) \mathscr{E} \sum_{\alpha=1}^{N} \boldsymbol{X}_{\alpha}=\boldsymbol{\mu}$, the sample mean is an unbiased estimator of the population mean. However,

$$
\mathscr{E} \hat{\mathbf{\Sigma}}=\frac{1}{N} \mathscr{E} \sum_{\alpha=1}^{N-1} Z_{\alpha} Z_{\alpha}^{\prime}=\frac{N-1}{N} \Sigma
$$

Thus $\hat{\mathbf{\Sigma}}$ is a biased estimator of $\mathbf{\Sigma}$. We shall therefore define

$$
S=\frac{1}{N-1} A=\frac{1}{N-1} \sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}
$$

as the sample covariance matrix. It is an unbiased estimator of $\mathbf{\Sigma}$ and the diagonal elements are the usual (unbiased) sample variances of the components of $X$.

### 3.3.2 Tests and Confidence Regions for the Mean Vector When the Covariance Matrix Is Known

A statistical problem of considerable importance is that of testing the hypothesis that the mean vector of a normal distribution is a given vector.
and a related problem is that of giving a confidence region for the unknown vector of means. We now go on to study these problems under the assumption that the covariance matrix $\boldsymbol{\Sigma}$ is known. In Chapter 5 we consider these problems when the covariance matrix is unknown.

In the univariate case one bases a test or a confidence interval on the fact that the difference between the sample mean and the population mean is normally distributed with mean zero and known variance; then tables of the normal distribution can be used to set up significance points or to compute confidence intervals. In the multivariate case one uses the fact that the difference between the sample mean vector and the population mean vector is normally distributed with mean vector zero and known covariance matrix. One could set up limits for each component on the basis of the distribution, but this procedure has the disadvantages that the choice of limits is somewhat arbitrary and in the case of tests leads to tests that may be very poor against some alternatives, and, moreover, such limits are difficult to compute because tables are available only for the bivariate case. The procedures given below, however, are easily computed and furthermore can be given general intuitive and theoretical justifications.

The procedures and evaluation of their properties are based on the following theorem:

Theorem 3.3.3. If the m-component vector $Y$ is distributed according to $N(\boldsymbol{\nu}, \boldsymbol{T})$ (nonsingular), then $\boldsymbol{Y}^{\prime} \boldsymbol{T}^{-1} \boldsymbol{Y}$ is distributed according to the noncentral $\chi^{2}$-distribution with in degrees of freedom and noncentrality parameter $\nu^{\prime} T^{-1} \nu$. If $\boldsymbol{\nu}=\mathbf{0}$, the distribution is the central $\chi^{2}$-distribution.

Proof. Let $\boldsymbol{C}$ be a nonsingular matrix such that $\boldsymbol{C T C}{ }^{\prime}=\boldsymbol{I}$, and define $\boldsymbol{Z}=\boldsymbol{C Y}$. Then $\boldsymbol{Z}$ is normally distributed with mean $\mathscr{E} \boldsymbol{Z}=\boldsymbol{C} \mathscr{E} \boldsymbol{Y}=\boldsymbol{C} \boldsymbol{v}=\boldsymbol{\lambda}$, say, and covariance matrix $\mathscr{E}(Z-\lambda)(Z-\lambda)^{\prime}=\mathscr{E} C(Y-\nu)(Y-\nu)^{\prime} C^{\prime}=C T C^{\prime}=I$. Then $Y^{\prime} T^{-1} Y=Z^{\prime}\left(C^{\prime}\right)^{-1} T^{-1} C^{-1} Z=Z^{\prime}\left(C T C^{\prime}\right)^{-1} Z=Z^{\prime} Z$, which is the sum of squares of the components of $Z$. Similarly $\boldsymbol{\nu}^{\prime} T^{-1} \boldsymbol{\nu}=\boldsymbol{\lambda}^{\prime} \boldsymbol{\lambda}$. Thus $\boldsymbol{Y}^{\prime} T^{-1} \boldsymbol{Y}$ is distributed as $\sum_{i=1}^{m} Z_{i}^{2}$, where $Z_{1}, \ldots, Z_{m}$ are independently normally distributed with means $\lambda_{1}, \ldots, \lambda_{m}$, respectively, and variances 1 . By definition this distribution is the noncentral $\chi^{2}$-distribution with noncentrality parameter $\sum_{1=1}^{m} \lambda_{1}^{2}$. See Section 3.3.3. If $\lambda_{1}=\cdots=\lambda_{m}=0$, the distribution is central. (See Problem 7.5.)

Since $\sqrt{N}(\overline{\boldsymbol{X}}-\boldsymbol{\mu})$ is distributed according to $N(\mathbf{0}, \boldsymbol{\Sigma})$, it follows from the theorem that

$$
N(\overline{\boldsymbol{X}}-\boldsymbol{\mu})^{\prime} \mathbf{\Sigma}^{-1}(\overline{\boldsymbol{X}}-\boldsymbol{\mu})
$$

has a (central) $\chi^{2}$-distribution with $p$ degrees of freedom. This is the fundamental fact we use in setting up tests and confidence regions concerning $\mu$.

Let $\chi_{p}^{2}(\alpha)$ be the number such that

$$
\operatorname{Pr}\left\{\chi_{p}^{2}>\chi_{p}^{2}(\alpha)\right\}=\alpha .
$$

Thus

$$
\operatorname{Pr}\left\{N(\overline{\boldsymbol{X}}-\boldsymbol{\mu})^{\prime} \boldsymbol{\Sigma}^{-1}(\overline{\boldsymbol{X}}-\boldsymbol{\mu})>\chi_{p}^{2}(\alpha)\right\}=\alpha .
$$

To test the hypothesis that $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}$, where $\boldsymbol{\mu}_{0}$ is a specified vector, we use as our critical region

$$
N\left(\bar{x}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\bar{x}-\boldsymbol{\mu}_{0}\right)>\chi_{p}^{2}(\boldsymbol{\alpha}) .
$$

If we obtain a sample such that (15) is satisfied, we reject the null liypothesis. It can be seen intuitively that the probability is greater than $\alpha$ of rejecting the hypothesis if $\boldsymbol{\mu}$ is very different from $\boldsymbol{\mu}_{0}$, since in the space of $\bar{x}$ (15) defines an ellipsoid with center at $\boldsymbol{\mu}_{0}$, and when $\boldsymbol{\mu}$ is far from $\boldsymbol{\mu}_{0}$ the density of $\bar{x}$ will be concentrated at a point near the edge or outside of the ellipsoid. The quantity $N\left(\overline{\boldsymbol{X}}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\overline{\boldsymbol{X}}-\boldsymbol{\mu}_{0}\right)$ is distributed as a noncentral $\chi^{2}$ with $p$ degrees of freedom and noncentrality parameter $N\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)$ when $\overline{\boldsymbol{X}}$ is the mean of a sample of $N$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ [given by Bose (1936a), (1936b)]. Pearson (1900) first proved Theorem 3.3.3 for $\boldsymbol{\nu}=\mathbf{0}$.

Now consider the following statement made on the basis of a sample with mean $\bar{x}$ : "The mean of the distribution satisfies

$$
N\left(\bar{x}-\mu^{*}\right)^{\prime} \Sigma^{-1}\left(\bar{x}-\mu^{*}\right) \leq \chi_{p}^{2}(\alpha)
$$

as an inequality on $\boldsymbol{\mu}^{*}$." We see from (14) that the probability that a sample will be drawn such that the above statement is true is $1-\alpha$ because the event in (14) is equivalent to the statement being false. Thus, the set of $\boldsymbol{\mu}^{*}$ satisfying (16) is a confidence region for $\boldsymbol{\mu}$ with confidence $1-\boldsymbol{\alpha}$.

In the $p$-dimensional space of $\bar{x}$, (15) is the surface and exterior of an ellipsoid with center $\boldsymbol{\mu}_{0}$, the shape of the ellipsoid depending on $\boldsymbol{\Sigma}^{-1}$ and the size on $(1 / N) \chi_{p}^{2}(\alpha)$ for given $\boldsymbol{\Sigma}^{-1}$. In the $p$-dimensional space of $\boldsymbol{\mu}^{*}$ (16) is the surface and interior of an ellipsoid with its center at $\bar{x}$. If $\Sigma^{-1}=I$, then (14) says that the probability is $\alpha$ that the distance between $\bar{x}$ and $\boldsymbol{\mu}$ is greater than $\sqrt{\chi_{p}^{2}(\alpha) / N}$.

Theorem 3.3.4. If $\bar{x}$ is the mean of a sample of $N$ drawn from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ and $\boldsymbol{\Sigma}$ is known, then (15) gives a critical region of size $\boldsymbol{\alpha}$ for testing the hypothesis $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}$, and (16) gives a confidence region for $\boldsymbol{\mu}$ of confidence $1-\boldsymbol{\alpha}$. Here $\chi_{p}^{2}(\alpha)$ is chosen to satisfy (13).

The same technique can be used for the corresponding two-sample problems. Suppose we have a sample $\left\{x_{\alpha}^{(1)}\right\}, \alpha=1, \ldots, N_{1}$, from the distribution $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)$, and a sample $\left\{x_{r r}^{(2)}\right\}, \alpha=1, \ldots, N_{2}$, from a second normal population $N\left(\boldsymbol{\mu}^{(2)}, \mathbf{\Sigma}\right)$ with the same covariance matrix. Then the two sample means

$$
\bar{x}^{(1)}=\frac{1}{N_{1}} \sum_{\alpha=1}^{N_{1}} x_{\alpha}^{(1)}, \quad \bar{x}^{(2)}=\frac{1}{N_{2}} \sum_{\alpha=1}^{N_{2}} x_{\alpha}^{(2)}
$$

are distributed independently according to $N\left[\boldsymbol{\mu}^{(1)},\left(1 / N_{1}\right) \boldsymbol{\Sigma}\right]$ and $N\left[\mu^{(2)},\left(1 / N_{2}\right) \Sigma\right]$, respectively. The difference of the two sample means, $y=\bar{x}^{(1)}-\bar{x}^{(2)}$, is distributed according to $\left.N^{1} \boldsymbol{v},\left[\left(1 / N_{1}\right)+\left(1 / N_{2}\right)\right] \boldsymbol{\Sigma}\right\}$, where $\boldsymbol{v}=\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}$. Thus

$$
\frac{N_{1} N_{2}}{N_{1}+N_{2}}(y-v)^{\prime} \Sigma^{-1}(y-v) \leq \chi_{p}^{2}(\alpha)
$$

is a confidence region for the difference $\boldsymbol{v}$ of the two mean vectors, and a critical region for testing the hypothesis $\boldsymbol{\mu}^{(1)}=\boldsymbol{\mu}^{(2)}$ is given by

$$
\frac{N_{1} N_{2}}{N_{1}+N_{2}}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)^{\prime} \Sigma^{-1}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)>\chi_{p}^{2}(\alpha) .
$$

Mahalanobis (1930) suggested $\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)$ as a measure of the distance squared between two populations. Let $C$ be a matrix such that $\boldsymbol{\Sigma}=\boldsymbol{C} \boldsymbol{C}^{\prime}$ and let $\boldsymbol{v}^{(i)}=\boldsymbol{C}^{-1} \boldsymbol{\mu}^{(i)}, i=1,2$. Then the distance squared is ( $\boldsymbol{\nu}^{(1)}- \left.\boldsymbol{v}^{(2)}\right)^{\prime}\left(\boldsymbol{v}^{(1)}-\boldsymbol{v}^{(2)}\right)$, which is the Euclidean distance squared.

### 3.3.3. The Noncentral $\boldsymbol{\chi}^{\mathbf{2}}$-Distribution; the Power Function

The power function of the test (15) of the null hypothesis that $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}$ can be evaluated from the noncentral $\chi^{2}$-distribution. The central $\chi^{2}$-distribution is the distribution of the sum of squares of independent (scalar) normal variables with means 0 and variances 1 ; the noncentral $\chi^{2}$-distribution is the generalization of this when the means may be different from 0 . Let $Y$ (of $p$ components) be distributed according to $N(\boldsymbol{\lambda}, \boldsymbol{I})$. Let $\boldsymbol{Q}$ be an orthogonal
matrix with elements of the first row being

$$
q_{1 i}=\frac{\lambda_{i}}{\sqrt{\lambda^{\prime} \lambda}}, \quad i=1, \ldots, p
$$

Then $\boldsymbol{Z}=\boldsymbol{Q} \boldsymbol{Y}$ is distributed according to $N(\boldsymbol{\tau}, \boldsymbol{I})$, where

$$
\boldsymbol{\tau}=\left(\begin{array}{c}
\tau \\
0 \\
\vdots \\
0
\end{array}\right)
$$

and $\tau=\sqrt{\lambda^{\prime} \lambda}$. Let $V=V^{\prime} Y=Z^{\prime} Z=\sum_{i=1}^{p} Z_{i}^{2}$. Then $W=\sum_{i=2}^{p} Z_{i}^{2}$ has a $\chi^{2}$ distribution with $p-1$ degrees of freedom (Problem 7.5), and $Z_{1}$ and $W$ have as joint density

$$
\begin{aligned}
\frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}\left(z_{1}-\tau\right)^{2}} \frac{1}{2^{\frac{1}{2}(p-1)} \Gamma\left[\frac{1}{2}(p\right.} & -1)] w^{\frac{1}{2}(p-1)-1} e^{-\frac{1}{2} w} \\
& =C e^{-\frac{1}{2}\left(\tau^{2}+z_{1}^{2}+w^{-}\right)} w^{\frac{1}{2}(p-3)} e^{\tau z_{1}} \\
& =C e^{-\frac{1}{3}\left(\tau^{2}+z_{1}^{2}+w\right)} w^{\frac{1}{3}(p-3)} \sum_{\alpha=0}^{\infty} \frac{\tau^{\alpha} z_{1}^{\alpha}}{\alpha!}
\end{aligned}
$$

where $C^{-1}=2^{\frac{1}{2} p} \sqrt{\pi} \Gamma\left[\frac{1}{2}(p-1)\right]$. The joint density of $V=W+Z_{1}^{2}$ and $Z_{1}$ is obtained by substituting $w=v-z_{1}^{2}$ (the Jacobian being 1):

$$
C e^{-\frac{1}{2}\left(\tau^{2}+v\right)}\left(v-z_{1}^{2}\right)^{\frac{1}{3}(p-3)} \sum_{\alpha=0}^{\infty} \frac{\tau^{\alpha} z_{1}^{\alpha}}{\alpha!} .
$$

The joint density of $V$ and $U=Z_{1} / \sqrt{V}$ is ( $d z_{1}=\sqrt{v} d u$ )

$$
C e^{-\frac{1}{2}\left(r^{2}+v\right)} v^{\frac{1}{2}(p-2)}\left(1-u^{2}\right)^{\frac{1}{2}(p-3)} \sum_{\alpha=0}^{\infty} \frac{\tau^{\alpha} v^{\frac{1}{1} \alpha} u^{\alpha}}{\alpha!} .
$$

The admissible range of $z_{1}$ given $v$ is $-\sqrt{v}$ to $\sqrt{v}$, and the admissible range of $u$ is -1 to 1 . When we integrate (24) with respect to $u$ term by term, the terms for $\alpha$ odd integrate to 0 , since such a term is an odd function of $u$. In
the other integrations we substitute $u=\sqrt{s}$ ( $d u=\frac{1}{2} d s / \sqrt{s}$ ) to obtain

$$
\begin{aligned}
\int_{-1}^{1}\left(1-u^{2}\right)^{\frac{1}{2}(p-3)} u^{2 \beta} d u & =2 \int_{0}^{1}\left(1-u^{2}\right)^{\frac{1}{2}(p-3)} u^{2 \beta} d u \\
& =\int_{0}^{1}(1-s)^{\frac{1}{2}(p-3)} s^{\beta-\frac{1}{2}} d s \\
& =B\left[\frac{1}{2}(p-1), \beta+\frac{1}{2}\right] \\
& =\frac{\Gamma\left[\frac{1}{2}(p-1)\right] \Gamma\left(\beta+\frac{1}{2}\right)}{\Gamma\left(\frac{1}{2} p+\beta\right)}
\end{aligned}
$$

by the usual properties of the beta and gamma functions. Thus the density of $V^{\prime}$ is

$$
\frac{1}{2^{\frac{1}{2} p} \sqrt{\pi}} e^{-\frac{1}{2}\left(\tau^{2}+v\right)} v^{\frac{1}{2} p-1} \sum_{\beta=0}^{\infty} \frac{\left(\tau^{2}\right)^{\beta} v^{\beta}}{(2 \beta)!} \frac{\Gamma\left(\beta+\frac{1}{2}\right)}{\Gamma\left(\frac{1}{2} p+\beta\right)} .
$$

We can use the duplication formula for the gamma function $\Gamma(2 \beta+1)=(2 \beta)$ ! (Problem 7.37),

$$
\Gamma(2 \beta+1)=\Gamma\left(\beta+\frac{1}{2}\right) \Gamma(\beta+1) 2^{2 \beta} / \sqrt{\pi},
$$

to rewrite (26) as

$$
\frac{1}{2^{\frac{1}{2} p}} e^{-\frac{1}{2}\left(\tau^{2}+v\right)} v^{\frac{1}{2} p-1} \sum_{\beta=0}^{\infty}\left(\frac{\tau^{2}}{4}\right)^{\beta} \frac{1}{\beta!\Gamma\left(\frac{1}{2} p+\beta\right)} v^{\beta} .
$$

This is the density of the noncentral $\chi^{2}$-distribution with $p$ degrees of freedom and noncentrality parameter $\tau^{2}$.

Theorem 3.3.5. If $Y$ of $p$ components is distributed according to $N(\boldsymbol{\lambda}, \boldsymbol{I})$, then $V=\boldsymbol{Y}^{\prime} \boldsymbol{Y}$ has the density (28), where $\tau^{2}=\boldsymbol{\lambda}^{\prime} \boldsymbol{\lambda}$.

To obtain the power function of the test (15), we note that $\sqrt{N}\left(\overline{\boldsymbol{X}}-\boldsymbol{\mu}_{0}\right)$ has the distribution $N\left[\sqrt{N}\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right), \boldsymbol{\Sigma}\right]$. From Theorem 3.3.3 we obtain the following corollary:

Corollary 3.3.1. If $\overline{\boldsymbol{X}}$ is the mean of a random sample of $N$ drawn from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, then $N\left(\overline{\boldsymbol{X}}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\overline{\boldsymbol{X}}-\boldsymbol{\mu}_{0}\right)$ has a noncentral $\chi^{2}$-distribution with $p$ degrees of freedom and noncent ality parameter $N\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)$.



### 3.4. THEORETICAL PROPERTIES OF ESTIMATORS OF THE MEAN VECTOR

### 3.4.1. Properties of Maximum Likelihood Estimators

It was shown in Section 3.3.1 that $\bar{x}$ and $S$ are unbiased estimators of $\boldsymbol{\mu}$ and $\Sigma$, respectively. In this subsection we shall show that $\bar{x}$ and $S$ are sufficient statistics and are complete.

## Sufficiency

A statistic $\boldsymbol{T}$ is sufficient for a family of distributions of $\boldsymbol{X}$ or for a parameter $\boldsymbol{\theta}$ if the conditional distribution of $\boldsymbol{X}$ given $\boldsymbol{T}=\boldsymbol{t}$ does not depend on $\boldsymbol{\theta}$ [e.g., Cramér (1946), Section 32.4]. In this sense the statistic $\boldsymbol{T}$ gives as much information about $\boldsymbol{\theta}$ as the entire sample $\boldsymbol{X}$. (Of course, this idea depends strictly on the assumed family of distributions.)

Factorization Theorem. A statistic $t(y)$ is sufficient for $\theta$ if and only if the density $f(y \mid \theta)$ can be factored as

$$
f(y \mid \theta)=g[t(y), \theta] h(y),
$$

where $g[t(y), \theta]$ and $h(y)$ are nonnegative and $h(y)$ does not depend on $\theta$.
Theorem 3.4.1. If $x_{1}, \ldots, x_{N}$ are observations from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, then $\bar{x}$ and $S$ are sufficient for $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$. If $\boldsymbol{\mu}$ is given, $\Sigma_{\alpha=1}^{N}\left(x_{\alpha}-\boldsymbol{\mu}\right)\left(x_{\alpha}-\boldsymbol{\mu}\right)^{\prime}$ is sufficient for $\boldsymbol{\Sigma}$. If $\boldsymbol{\Sigma}$ is given, $\bar{x}$ is sufficient for $\boldsymbol{\mu}$.

Proof. The density of $X_{1}, \ldots, X_{N}$ is
(2) $\prod_{\alpha=1}^{N} n\left(x_{\alpha} \mid \boldsymbol{\mu}, \boldsymbol{\Sigma}\right)$

$$
\begin{aligned}
& =(2 \pi)^{-\frac{1}{2} N p}|\boldsymbol{\Sigma}|^{-\frac{1}{2} N} \exp \left[-\frac{1}{2} \operatorname{tr} \boldsymbol{\Sigma}^{-1} \sum_{\alpha=1}^{N}\left(x_{\alpha}-\boldsymbol{\mu}\right)\left(x_{\alpha}-\boldsymbol{\mu}\right)^{\prime}\right] \\
& =(2 \pi)^{-\frac{1}{2} N p}|\boldsymbol{\Sigma}|^{-\frac{1}{2} N} \exp \left\{-\frac{1}{2}\left[N(\overline{\boldsymbol{x}}-\boldsymbol{\mu})^{\prime} \boldsymbol{\Sigma}^{-1}(\overline{\boldsymbol{x}}-\boldsymbol{\mu})+(N-1) \operatorname{tr} \boldsymbol{\Sigma}^{-1} \boldsymbol{S}\right]\right\}
\end{aligned}
$$

The right-hand side of (2) is in the form of (1) for $\overline{\boldsymbol{x}}, \boldsymbol{S}, \boldsymbol{\mu}, \boldsymbol{\Sigma}$, and the middle is in the form of (1) for $\sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu\right)\left(x_{\alpha}-\mu\right)^{\prime}, \mathbf{\Sigma}$; in each case $h\left(x_{1}, \ldots, x_{N}\right) =1$. The right-hand side is in the form of (1) for $\bar{x}, \boldsymbol{\mu}$ with $h\left(x_{1}, \ldots, x_{N}\right)= \exp \left\{-\frac{1}{2}(N-1) \operatorname{tr} \Sigma^{-1} S\right\}$.

Note that if $\boldsymbol{\Sigma}$ is given, $\overline{\boldsymbol{x}}$ is sufficient for $\boldsymbol{\mu}$, but if $\boldsymbol{\mu}$ is given, $\boldsymbol{S}$ is not sufficient for $\boldsymbol{\Sigma}$.

## Completeness

To prove an optimality property of the $T^{2}$-test (Section 5.5), we need the result that ( $\overline{\boldsymbol{x}}, \boldsymbol{S}$ ) is a complete sufficient set of statistics for ( $\boldsymbol{\mu}, \boldsymbol{\Sigma}$ ).

Definition 3.4.1. A family of distributions of $\boldsymbol{y}$ indexed by $\boldsymbol{\theta}$ is complete if for every real-valued function $g(y)$,

$$
\mathscr{E}_{\theta} g(y) \equiv 0
$$

identically in $\theta$ implies $g(y)=0$ except for a set of $y$ of probability 0 for every $\theta$.
If the family of distributions of a sufficient set of statistics is complete, the set is called a complete sufficient set.

Theorem 3.4.2. The sufficient set of statistics $\overline{\boldsymbol{x}}, S$ is complete for $\boldsymbol{\mu}, \mathbf{\Sigma}$ when the sample is drawn from $N(\boldsymbol{\mu}, \mathbf{\Sigma})$.

Proof. We can define the sample in terms of $\bar{x}$ and $z_{1}, \ldots, z_{n}$ as in Section 3.3 with $n=N-1$. We assume for any function $g(\bar{x}, A)=g(\bar{x}, n S)$ that

$$
\begin{aligned}
& \int \cdots \int K|\Sigma|^{-\frac{1}{2} N} g\left(\bar{x}, \sum_{\alpha=1}^{n} z_{\alpha} z_{\alpha}^{\prime}\right) \\
& \quad \cdot \exp \left\{-\frac{1}{2}\left[N(\bar{x}-\mu)^{\prime} \Sigma^{-1}(\bar{x}-\mu)+\sum_{\alpha=1}^{n} z_{\alpha}^{\prime} \Sigma^{-1} z_{\alpha}\right]\right\} \\
& \quad \cdot d \bar{x} \prod_{\alpha=1}^{n} d z_{\alpha} \equiv 0, \quad \forall \mu, \Sigma
\end{aligned}
$$

where $K=\sqrt{N}(2 \pi)^{-\frac{1}{2} p N}, d \bar{x}=\prod_{i=1}^{p} d \bar{x}_{i}$, and $d z_{\alpha}=\prod_{i=1}^{p} d z_{i \alpha}$. If we let $\boldsymbol{\Sigma}^{-1} =I-2 \Theta$, where $\Theta=\Theta^{\prime}$ and $I-2 \Theta$ is positive definite, and let $\mu= (I-2 \Theta)^{-1} t$, then (4) is
(5)

$$
\begin{aligned}
0 \equiv & \int \cdots \int K|I-2 \Theta|^{\frac{1}{2} N} g\left(\bar{x}, \sum_{\alpha=1}^{n} z_{\alpha} z_{\alpha}^{\prime}\right) \\
& \cdot \exp \left\{-\frac{1}{2}\left[\operatorname{tr}(I-2 \Theta)\left(\sum_{\alpha=1}^{n} z_{\alpha} z_{\alpha}^{\prime}+N \bar{x} \bar{x}^{\prime}\right)\right.\right. \\
& \left.\left.\quad-2 N t^{\prime} \bar{x}+N t^{\prime}(I-2 \Theta)^{-1} t\right]\right\} d \bar{x} \prod_{\alpha=1}^{n} d z_{\alpha} \\
= & |I-2 \Theta|^{\frac{1}{2} N} \exp \left\{-\frac{1}{2} N t^{\prime}(I-2 \Theta)^{-1} t\right\} \int \cdots \int g\left(\bar{x}, B-N \bar{x} \bar{x}^{\prime}\right) \\
& \cdot \exp \left[\operatorname{tr} \Theta B+t^{\prime}(N \bar{x})\right] n[\bar{x} \mid \mathbf{0},(1 / N) I] \prod_{\alpha=1}^{n} n\left(z_{\alpha} \mid \mathbf{0}, I\right) d \bar{x} \prod_{\alpha=1}^{n} d z_{\alpha}
\end{aligned}
$$

where $B=\sum_{\alpha=1}^{n} z_{\alpha} z_{\alpha}^{\prime}+N \bar{x} x^{\prime}$. Thus

$$
\begin{aligned}
0 & \equiv \mathscr{E} g\left(\overline{\boldsymbol{x}}, \boldsymbol{B}-N \overline{\boldsymbol{x}} \overline{\boldsymbol{x}}^{\prime}\right) \exp \left[\operatorname{tr} \boldsymbol{\Theta} \boldsymbol{B}+t^{\prime}(N \bar{x})\right] \\
& =\int \cdots \int g\left(\overline{\boldsymbol{x}}, \boldsymbol{B}-N \overline{\boldsymbol{x}} \overline{\boldsymbol{x}}^{\prime}\right) \exp \left[\operatorname{tr} \boldsymbol{\Theta} \boldsymbol{B}+t^{\prime}(N \bar{x})\right] h(\overline{\boldsymbol{x}}, \boldsymbol{B}) d \overline{\boldsymbol{x}} d \boldsymbol{B}
\end{aligned}
$$

where $h(\overline{\boldsymbol{x}}, \boldsymbol{B})$ is the ioint density of $\overline{\boldsymbol{x}}$ and $\boldsymbol{B}$ and $d \boldsymbol{B}=\Pi_{1 \leq 1} d b_{1,}$. The right-hand side of (6) is the Laplace transform of $g\left(\overline{\boldsymbol{x}}, \boldsymbol{B}-N \overline{\boldsymbol{x}} \overline{\boldsymbol{x}}^{\prime}\right) h(\overline{\boldsymbol{x}}, \boldsymbol{B})$. Since this is $0, g(\overline{\boldsymbol{x}}, \boldsymbol{A})=0$ except for a set of measure 0 . $\square$

## Efficiency

If a $q$-component random vector $\boldsymbol{Y}$ has mean vector $\mathscr{E} \boldsymbol{Y}=\boldsymbol{\nu}$ and covariance matrix $\mathscr{E}(\boldsymbol{Y}-\boldsymbol{\nu})(\boldsymbol{Y}-\boldsymbol{\nu})^{\prime}=\boldsymbol{\Psi}$, then

$$
(\boldsymbol{y}-\boldsymbol{v})^{\prime} \boldsymbol{\Psi}^{-1}(\boldsymbol{y}-\boldsymbol{v})=q+2
$$

is called the concentration ellipsoid of $\boldsymbol{Y}$. [See Cramér (1946), p. 300.] The density defined by a uniform distribution over the interior of this ellipsoid has the same mean vector and covariance matrix as $\boldsymbol{Y}$. (See Problem 2.14.) Let $\boldsymbol{\theta}$ be a vector of $q$ parameters in a distribution, and let $t$ be a vector of unbiased estimators (that is, $\mathscr{E} t=\boldsymbol{\theta}$ ) based on $N$ observations from that distribution with covariance matrix $\Psi$. Then the ellipsoid

$$
N(t-\boldsymbol{\theta})^{\prime} \mathscr{E}\left(\frac{\partial \log f}{\partial \boldsymbol{\theta}}\right)\left(\frac{\partial \log f}{\partial \boldsymbol{\theta}}\right)^{\prime}(t-\boldsymbol{\theta})=q+2
$$

lies entirely within the ellipsoid of concentration of $t ; \partial \log f / \partial \theta$ denotes the column vector of derivatives of the density of the distribution (or probability function) with respect to the components of $\boldsymbol{\theta}$. The discussion by Cramér (1946, p. 495) is in terms of scalar observations, but it is clear that it holds true for vector observations. If (8) is the ellipsoid of concentration of $t$, then $t$ is said to be efficient. In general, the ratio of the volume of (8) to that of the ellipsoid of concentration defines the efficiency of $t$. In the case of the multivariate normal distribution, if $\boldsymbol{\theta}=\boldsymbol{\mu}$, then $\overline{\boldsymbol{x}}$ is efficient. If $\boldsymbol{\theta}$ includes both $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$, then $\overline{\boldsymbol{x}}$ and $\boldsymbol{S}$ have efficiency $[(N-1) / N]^{p(\mu+1) / 2}$. Under suitable regularity conditions, which are satisfied by the multivariate normal distribution,

$$
\mathscr{E}\left(\frac{\partial \log f}{\partial \boldsymbol{\theta}}\right)\left(\frac{\partial \log f}{\partial \boldsymbol{\theta}}\right)^{\prime}=-\mathscr{6} \frac{\partial^{2} \log f}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{\prime}} .
$$

This is the information matrix for one observation. The Cramér-Rao lower
bound is that for any unbiased estimator $t$ the matrix

$$
N \mathscr{E}(t-\boldsymbol{\theta})(t-\boldsymbol{\theta})^{\prime}-\left[-\mathscr{E} \frac{\partial^{2} \log f}{\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}^{\prime}}\right]^{-1}
$$

is positive semidefinite. (Other lower bounds can also be given.)

## Consistency

Definition 3.4.2. A sequence of vectors $t_{n}=\left(t_{1 n}, \ldots, t_{m n}\right)^{\prime}, n=1,2, \ldots$, is a consistent estimator of $\boldsymbol{\theta}=\left(\theta_{1}, \ldots, \theta_{m}\right)^{\prime}$ if plim $_{\eta_{1} \rightarrow \infty} t_{i n}=\theta_{i}, i=1, \ldots, m$.

By the law of large numbers each component of the sample mean $\bar{x}$ is a consistent estimator of that component of the vector of expected values $\boldsymbol{\mu}$ if the observation vectors are independently and identically distributed with mean $\boldsymbol{\mu}$, and hence $\overline{\boldsymbol{x}}$ is a consistent estinator of $\boldsymbol{\mu}$. Normality is not involved.

An element of the sample covariance matrix is

$$
s_{1,}=\frac{1}{N-1} \sum_{\alpha=1}^{N}\left(x_{1 \alpha}-\mu_{1}\right)\left(x_{j \alpha}-\mu_{j}\right)-\frac{N}{N-1}\left(\bar{x}_{i}-\mu_{1}\right)\left(\bar{x}_{1}-\mu_{1}\right)
$$

by Lemma 3.2.1 with $\boldsymbol{b}=\boldsymbol{\mu}$. The probability limit of the second term is 0 . The probability limit of the first term is $\sigma_{1}$ if $x_{1}, x_{2}, \ldots$ are independently and identically distributed with mean $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$. Then $\boldsymbol{S}$ is a consistent estimator of $\boldsymbol{\Sigma}$.

## Asymptotic Nornality

First we prove a multivariate central limit theorem.
Theorem 3.4.3. Let the $m$-component vectors $Y_{1}, Y_{2}, \ldots$ be independently and identically distributed with means $\mathscr{E} \boldsymbol{Y}_{\alpha}=\boldsymbol{\nu}$ and covariance matrices $\mathscr{E}\left(\boldsymbol{Y}_{\alpha}-\boldsymbol{\nu}\right)\left(\boldsymbol{Y}_{\alpha}-\boldsymbol{\nu}\right)^{\prime}=\boldsymbol{T}$. Then the limiting distribution of $(1 / \sqrt{n}) \sum_{\alpha=1}^{n}\left(\boldsymbol{Y}_{\alpha}-\boldsymbol{\nu}\right)$ as $n \rightarrow \infty$ is $N(\mathbf{0}, T)$.

Proof. Let

$$
\phi_{n}(t, u)=\mathscr{E} \exp \left[i u t^{\prime} \frac{1}{\sqrt{n}} \sum_{\alpha=1}^{n}\left(\boldsymbol{Y}_{\alpha}-\boldsymbol{v}\right)\right],
$$

where $u$ is a scalar and $t$ an $m$-component vector. For fixed $t, \phi_{n}(t, u)$ can be considered as the characteristic function of $(1 / \sqrt{n}) \sum_{\alpha=1}^{n}\left(\boldsymbol{t}^{\prime} \boldsymbol{Y}_{\alpha}-\mathscr{E}^{\prime} \boldsymbol{t}_{\alpha}\right)$. By
the univariate central limit theorem [Cramér (1946), p. 215], the limiting distribution is $N\left(0, t^{\prime} T t\right)$. Therefore (Theorem 2.6.4),

$$
\lim _{n \rightarrow \infty} \phi_{n}(t, u)=e^{-\frac{1}{2} u^{2} t T t}
$$

for every $u$ and $t$. (For $t=0$ a special and obvious argument is used.) Let $u=1$ to obtain

$$
\lim _{n \rightarrow \infty} \mathscr{E} \exp \left[i t^{\prime} \frac{1}{\sqrt{n}} \sum_{\alpha=1}^{n}\left(Y_{\alpha}-v\right)\right]=e^{-\frac{1}{2} \prime T r}
$$

for every $t$. Since $e^{-\frac{1}{2} t^{\prime} \mathbf{T} t}$ is continuous at $t=0$, the convergence is uniform in some neighborhood of $t=0$. The theorem follows. $\square$

Now we wish to show that the sample covariance matrix is asymptotically normally distributed as the sample size increases.

Theorem 3.4.4. Let $\boldsymbol{A}(n)=\sum_{\alpha=1}^{N}\left(\boldsymbol{X}_{\alpha}-\overline{\boldsymbol{X}}_{N}\right)\left(\boldsymbol{X}_{\alpha}-\overline{\boldsymbol{X}}_{N}\right)^{r}$, where $\boldsymbol{X}_{1}, \boldsymbol{X}_{2}, \ldots$ are independently distributed according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ and $n=N-1$. Then the limiting distribution of $\boldsymbol{B}(n)=(1 / \sqrt{n})[\boldsymbol{A}(n)-n \boldsymbol{\Sigma}]$ is normal with mean $\mathbf{0}$ and covariances

$$
\mathscr{E} b_{i j}(n) b_{k l}(n)=\sigma_{i k} \sigma_{i l}+\sigma_{i l} \sigma_{i k} .
$$

Proof. As shown earlier, $A(n)$ is distributed as $A(n)=\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{r}$, where $\boldsymbol{Z}_{1}, \boldsymbol{Z}_{2}, \ldots$ are distributed independently according to $N(0, \boldsymbol{\Sigma})$. We arrange the elements of $Z_{\alpha} Z_{\alpha}^{r}$ in a vector such as

$$
Y_{\alpha}=\left(\begin{array}{c}
Z_{1 \alpha}^{2} \\
Z_{1 \alpha} Z_{2 \alpha} \\
\vdots \\
Z_{2 \alpha}^{2} \\
\vdots \\
Z_{p \alpha}^{2}
\end{array}\right) .
$$

the moments of $\mathbf{Y}_{\alpha}$ can be deduced from the moments of $\mathbf{Z}_{\alpha}$ as given in Section 2.6. We have $\mathscr{E} Z_{1 \alpha} Z_{j \alpha}=\sigma_{i j}, \mathscr{E} Z_{i \alpha} Z_{j \alpha} Z_{k \alpha} Z_{i \alpha}=\sigma_{i j} \sigma_{k l}+\sigma_{i k} \sigma_{j l}+ \sigma_{i l} \sigma_{j k}, \mathscr{E}\left(Z_{i \alpha} Z_{i \alpha}-\sigma_{i j}\right)\left(Z_{k \alpha} Z_{l \alpha}-\sigma_{k l}\right)=\sigma_{i k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}$. Thus the vectors $\mathbf{Y}_{\alpha}$ defined by (16) satisfy the conditions of Theorem 3.4.3 with the elements of $\boldsymbol{v}$ being the elements of $\boldsymbol{\Sigma}$ arranged in vector form similar to (16)
and the elements of $\boldsymbol{T}$ being given above. If the elements of $A(n)$ are arranged in vector form similar to (16), say the vector $W(n)$, then $W(n)-n \boldsymbol{v} =\sum_{\alpha=1}^{n}\left(\boldsymbol{Y}_{\alpha}-\boldsymbol{v}\right)$. By Theorem 3.4.3, $(1 / \sqrt{n})[\boldsymbol{W}(n)-n \boldsymbol{v}]$ has a limiting normal distribution with mean $\mathbf{0}$ and the covariance matrix of $\mathbf{Y}_{\alpha}$.

The elements of $\boldsymbol{B}(n)$ will have a limiting normal distribution with mean $\mathbf{0}$ if $x_{1}, x_{2}, \ldots$ are independently and identically distributed with finite fourthorder moments, but the covariance structure of $\boldsymbol{B}(n)$ will depend on the fourth-order moments.

### 3.4.2. Decision Theory

It may be enlightening to consider estimation in teims of decision theory. We review some of the concepts. An observation $x$ is made on a random variable $X$ (which may be a vector) whose distribution $P_{\theta}$ depends on a parameter $\theta$ which is an element of a set $\Theta$. The statistician is to make a decision $d$ in a set $D$. A decision procedure is a function $\delta(x)$ whose domain is the set of values of $X$ and whose range is $D$. The loss in making decision $d$ when the distribution is $P_{\theta}$ is a nonnegative function $L(\theta, d)$. The evaluation of a procedure $\delta(x)$ is on the basis of the risk function

$$
R(\theta, \delta)=\mathscr{E}_{\theta} L[\theta, \delta(X)]
$$

For example, if $d$ and $\theta$ are univariate, the loss may be squared error, $L(\theta, d)=(\theta-d)^{2}$, and the risk is the mean squared error $\mathscr{E}_{\theta}[\delta(X)-\theta]^{2}$.

A decision procedure $\delta(x)$ is as good as a procedure $\delta^{*}(x)$ if

$$
R(\theta, \delta) \leq R\left(\theta, \delta^{*}\right)
$$

$\delta(x)$ is better than $\delta^{*}(x)$ if (18) holds with a strict inequality for at least one value of $\theta$. A procedure $\delta^{*}(x)$ is inadmissible if there exists another procedure $\delta(x)$ that is better than $\delta^{*}(x)$. A procedure is admissible if it is not inadmissible (i.e., if there is no procedure better than it) in terms of the given loss function. A class of procedures is complete if for any procedure not in the class there is a better procedure in the class. The class is minimal complete if it does not contain a proper complete subclass. If a minimal complete class exists, it is identical to the class of admissible procedures. When such a class is available, there is no (mathematical) need to use a procedure outside the minimal complete class. Sometimes it is convenient to refer to an essentially complete class, which is a class of procedures such that for every procedure outside the class there is one in the class that is just as good.

For a given procedure the risk function is a function of the parameter. If the parameter can be assigned an a priori distribution, say, with density $\rho(\theta)$, then the average loss from use of a decision procedure $\delta(x)$ is

$$
r(\rho, \delta)=\mathscr{E}_{p} R(\theta, \delta)=\mathscr{E}_{p} \mathscr{E}_{\theta} L[\theta, \delta(X)] .
$$

Given the a priori density $\rho$, the decision procedure $\delta(x)$ that minimizes $r(\rho, \delta)$ is the Bayes procedure, and the resulting minimum of $r(\rho, \delta)$ is the Bayes risk. Under general conditions Bayes procedures are admissible and admissible procedures are Bayes or limits of Bayes procedures. If the density of $X$ given $\theta$ is $f(x \mid \theta)$, the joint density of $X$ and $\theta$ is $f(x \mid \theta) \rho(\theta)$ and the average risk of a procedure $\delta(x)$ is

$$
\begin{aligned}
r(\rho, \delta) & =\int_{\Theta} \int_{X} L[\theta, \delta(x)] f(x \mid \theta) \rho(\theta) d x d \theta \\
& =\int_{X}\left\{\int_{\Theta} L[\theta, \delta(x)] g(\theta \mid x) d \theta\right\} f(x) d x
\end{aligned}
$$

here

$$
f(x)=\int_{\Theta} f(x \mid \theta) \rho(\theta) d \theta, \quad g(\theta \mid x)=\frac{f(x \mid \theta) \rho(\theta)}{f(x)}
$$

are the marginal density of $X$ and the a posteriori density of $\theta$ given $x$. The procedure that minimizes $r(\rho, \delta)$ is one that for each $x$ minimizes the expression in braces on the right-hand side of (20), that is, the expectation of $L[\theta, \delta(x)]$ with respect to the a posteriori distribation. If $\theta$ and $d$ are vectors ( $\boldsymbol{\theta}$ and $\boldsymbol{d}$ ) and $L(\boldsymbol{\theta}, \boldsymbol{d})=(\boldsymbol{\theta}-\boldsymbol{d})^{\prime} Q(\boldsymbol{\theta}-\boldsymbol{d})$, where $\boldsymbol{Q}$ is positive definite, then

$$
\begin{aligned}
\mathscr{E}_{\theta \mid x} L[\boldsymbol{\theta}, d(x)]= & \mathscr{E}_{\theta \mid x}[\boldsymbol{\theta}-\mathscr{E}(\boldsymbol{\theta} \mid x)]^{\prime} Q[\boldsymbol{\theta}-\mathscr{E}(\boldsymbol{\theta} \mid x)] \\
& +[\mathscr{E}(\boldsymbol{\theta} \mid x)-d(x)]^{\prime} Q[\mathscr{E}(\boldsymbol{\theta} \mid x)-d(x)] .
\end{aligned}
$$

The minimum occurs at $d(x)=\mathscr{E}(\boldsymbol{\theta} \mid x)$, the mean of the a posteriori distribution.

Theorem 3.4.5. If $x_{1}, \ldots, x_{N}$ are independently distributed, each $x_{\alpha}$ according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, and if $\boldsymbol{\mu}$ has an a priori distribution $N(\boldsymbol{\nu}, \boldsymbol{\Phi})$, then the a posteriori distribution of $\mu$ given $x_{1}, \ldots, x_{N}$ is normal with mean

$$
\boldsymbol{\Phi}\left(\boldsymbol{\Phi}+\frac{1}{N} \boldsymbol{\Sigma}\right)^{-1} \bar{x}+\frac{1}{N} \boldsymbol{\Sigma}\left(\boldsymbol{\Phi}+\frac{1}{N} \boldsymbol{\Sigma}\right)^{-1} \nu
$$

and covariance matrix

$$
\mathbf{\Phi}-\mathbf{\Phi}\left(\mathbf{\Phi}+\frac{1}{N} \mathbf{\Sigma}\right)^{-1} \mathbf{\Phi} .
$$

Proof. Since $\bar{x}$ is sufficient for $\boldsymbol{\mu}$, we need only consider $\bar{x}$, which has the distribution of $\boldsymbol{\mu}+\boldsymbol{\nu}$, where $\boldsymbol{\nu}$ has the distribution $N[\mathbf{0},(1 / N) \boldsymbol{\Sigma}]$ and is independent of $\boldsymbol{\mu}$. Then the joint distribution of $\boldsymbol{\mu}$ and $\overline{\boldsymbol{x}}$ is

$$
N\left[\binom{\boldsymbol{\nu}}{\boldsymbol{\nu}},\left(\begin{array}{cc}
\boldsymbol{\Phi} & \boldsymbol{\Phi} \\
\boldsymbol{\Phi} & \boldsymbol{\Phi}+\frac{1}{N} \boldsymbol{\Sigma}
\end{array}\right)\right] .
$$

The mean of the conditional distribution of $\boldsymbol{\mu}$ given $\overline{\boldsymbol{x}}$ is (by Theorem 2.5.1)

$$
\boldsymbol{v}+\boldsymbol{\Phi}\left(\boldsymbol{\Phi}+\frac{1}{N} \boldsymbol{\Sigma}\right)^{-1}(\overline{\boldsymbol{x}}-\boldsymbol{v}),
$$

which reduces to (23).

Corollary 3.4.1. If $x_{1}, \ldots, x_{N}$ are independently distributed, each $x_{\alpha}$ according to $N(\mu, \Sigma), \mu$ has an a priori distribution $N(\nu, \Phi)$, and the loss function is $(d-\mu)^{\prime} Q(d-\mu)$, then the Bayes estimator of $\mu$ is (23).

The Bayes estimator of $\boldsymbol{\mu}$ is a kind of weighted average of $\overline{\boldsymbol{x}}$ and $\boldsymbol{\nu}$, the prior mean of $\boldsymbol{\mu}$. If $(1 / N) \boldsymbol{\Sigma}$ is small compared to $\boldsymbol{\Phi}$ (e.g., if $N$ is large), $\boldsymbol{v}$ is given little weight. Put another way, if $\boldsymbol{\Phi}$ is large, that is, the prior is relatively uninformative, a large weight is put on $\overline{\boldsymbol{x}}$. In fact, as $\boldsymbol{\Phi}$ tends to $\infty$ in the sense that $\boldsymbol{\Phi}^{-1} \rightarrow \mathbf{0}$, the estimator approaches $\overline{\boldsymbol{x}}$.

A decision procedure $\delta_{0}(x)$ is minimax if

$$
\sup _{\theta} R\left(\theta, \delta_{0}\right)=\inf _{\delta} \sup _{\theta} R(\theta, \delta) .
$$

Theorem 3.4.6. If $x_{1}, \ldots, x_{N}$ are independently distributed each according to $N(\mu, \Sigma)$ and the loss function is $(d-\mu)^{\prime} Q(d-\mu)$, then $\bar{x}$ is a minimax estimator.

Proof. This follows from a theorem in statistical decision theory that if a procedure $\delta_{0}$ is extended Bayes [i.e., if for arbitrary $\varepsilon, r\left(\rho, \delta_{0}\right) \leq r\left(\rho, \delta_{\rho}\right)+\varepsilon$ for suitable $\rho$, where $\delta_{\rho}$ is the corresponding Bayes procedure] and if $R\left(\theta, \delta_{0}\right)$ is constant, then $\delta_{0}$ is minimax. [See, e.g., Ferguson (1967), Theorem 3 of Section 2.11.] We find

$$
\begin{aligned}
R(\boldsymbol{\mu}, \bar{x}) & =\mathscr{E}(\bar{x}-\boldsymbol{\mu})^{\prime} \boldsymbol{Q}(\bar{x}-\boldsymbol{\mu}) \\
& =\mathscr{E} \operatorname{tr} \boldsymbol{Q}(\bar{x}-\boldsymbol{\mu})(\bar{x}-\boldsymbol{\mu})^{\prime} \\
& =\frac{1}{N} \operatorname{tr} \boldsymbol{Q} .
\end{aligned}
$$

Let (23) be $d(\bar{x})$. Its average risk is

$$
\begin{aligned}
& \mathscr{E}_{\bar{x}} \mathscr{E}_{\mu}\left\{\operatorname{tr} Q[d(\bar{x})-\boldsymbol{\mu}][d(\bar{x})-\boldsymbol{\mu}]^{\prime} \mid \bar{x}\right\} \\
& \quad=\mathscr{E}_{\bar{x}} \operatorname{tr} Q\left[\mathbf{\Phi}-\mathbf{\Phi}\left(\mathbf{\Phi}+\frac{1}{N} \mathbf{\Sigma}\right)^{-1} \mathbf{\Phi}\right]=\operatorname{tr} Q \mathbf{\Phi}\left(\mathbf{\Phi}+\frac{1}{N} \mathbf{\Sigma}\right)^{-1} \frac{1}{N} \mathbf{\Sigma} \\
& \quad=\operatorname{tr} Q\left(I+\frac{1}{N} \mathbf{\Sigma} \mathbf{\Phi}^{-1}\right)^{-1} \frac{1}{N} \mathbf{\Sigma} \rightarrow \frac{1}{N} \operatorname{tr} Q \mathbf{\Sigma}
\end{aligned}
$$

as $\boldsymbol{\Phi}^{-1} \rightarrow \mathbf{0}$. $\square$

For more discussion of decision theory see Ferguson (1967). DeGroot (1970), or Berger (1980b).

### 3.5. IMPROVED ESTIMATION OF THE MEAN

### 3.5.1. Introduction

The sample mean $\bar{x}$ seems the natural estimator of the population mean $\boldsymbol{\mu}$ based on a sample from $N(\mu, \Sigma)$. It is the maximum likelihood estimator, a sufficient statistic when $\boldsymbol{\Sigma}$ is known, and the minimum variance unbiased estimator. Moreover, it is equivariant in the sense that if an arbitrary vector $\boldsymbol{v}$ is added to each observation vector and to $\mu$, the error of estimation $\overline{(x+\nu)}-(\mu+\nu)=\bar{x}-\mu$ is independent of $\nu$; in other words, the error does not depend on the choice of origin. However, Stein (1956b) showed the startling fact that this conventional estimator is not admissible with respect to the loss function that is the sum of mean squared errors of the components when $\Sigma=I$ and $p \geq 3$. James and Stein (1961) produced an estimator which has a smaller sum of mean squared errors; this estimator will be studied in Section 3.5.2. Subsequent studies have shown that the phenomenon is widespread and the implications imperative.

### 3.5.2. The James-Stein Estimator

The loss function

$$
L(\boldsymbol{\mu}, \boldsymbol{m})=(\boldsymbol{m}-\boldsymbol{\mu})^{\prime}(\boldsymbol{m}-\boldsymbol{\mu})=\sum_{i=1}^{p}\left(m_{i}-\mu_{\mathrm{r}}\right)^{2}=\|\boldsymbol{m}-\boldsymbol{\mu}\|^{2}
$$

is the sum of mean squared errors of the components of the estimator. We shall show [James and Stein (1961)] that the sample mean is inadmissible by
displaying an alternative estimator that has a smaller expected loss for every mean vector $\mu$. We assume that the normal distribution sampled has covariance matrix proportional to $I$ with the constant of proportionality known. It will be convenient to take this constant to be such that $Y=(1 / N) \sum_{\alpha=1}^{n} X_{\alpha}=\bar{X}$ has the distribution $N(\mu, I)$. Then the expected loss or risk of the estimator $\boldsymbol{Y}$ is simply $\mathscr{E}\|\boldsymbol{Y}-\boldsymbol{\mu}\|^{2}=\operatorname{tr} \boldsymbol{I}=p$. The estimator proposed by James and Stein is (essentially)

$$
m(y)=\left(1-\frac{p-2}{\|y-v\|^{2}}\right)(y-v)+v,
$$

where $\nu$ is an arbitrary fixed vector and $p \geq 3$. This estimator shrinks the observed $y$ toward the specified $\boldsymbol{v}$. The amount of shrinkage is negligible if $y$ is very different from $\nu$ and is considerable if $y$ is close to $\nu$. In this sense $\nu$ is a favored point.

Theorem 3.5.1. With respect to the loss function (1), the risk of the estimator (2) is less than the risk of the estimator $\mathbf{Y}$ for $p \geq 3$.

We shall show that the risk of $Y$ minus the risk of (2) is positive by applying the following lemma due to Stein (1974).

Lemma 3.5.1. If $f(x)$ is a function such that

$$
f(b)-f(a)=\int_{a}^{b} f^{\prime}(x) d x
$$

for all $a$ and $b(a<b)$ and if

$$
\int_{-\infty}^{\infty}\left|f^{\prime}(x)\right| \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d x<\infty .
$$

then

$$
\int_{-\infty}^{\infty} f(x)(x-\theta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d x=\int_{-\infty}^{\infty} f^{\prime}(x) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d x
$$



Proof of Lemma. We write the left-hand side of (5) as

$$
\begin{aligned}
\int_{\theta}^{\infty}[ & f(x)-f(\theta)](x-\theta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d x \\
& +\int_{-\infty}^{\theta}[f(x)-f(\theta)](x-\theta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d x \\
= & \int_{\theta}^{\infty} \int_{\theta}^{x} f^{\prime}(y)(x-\theta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d y d x \\
& -\int_{-\infty}^{\theta} \int_{x}^{\theta} f^{\prime}(y)(x-\theta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d y d x \\
= & \int_{\theta}^{\infty} \int_{y}^{\infty} f^{\prime}(y)(x-\theta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d x d y \\
& -\int_{-\infty}^{\theta} \int_{-\infty}^{y} f^{\prime}(y)(x-\theta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{2}} d x d y
\end{aligned}
$$

which yields the right-hand side of (5). Fubini's theorem justifies the interchange of order of integration. (See Problem 3.22.)

The lemma can also be derived by integration by parts in special cases.
Proof of Theorem 3.5.1. The difference in risks is
(7) $\Delta R(\mu)=\S_{\mu}\left[\|\mathbf{Y}-\mu\|^{2}-\|m(\boldsymbol{Y})-\mu\|^{2}\right\}$

$$
\begin{aligned}
& =\mathscr{E}_{\mu}\left\{\|\boldsymbol{Y}-\boldsymbol{\mu}\|^{2}-\left\|\left(1-\frac{p-2}{\|\boldsymbol{Y}-\boldsymbol{\nu}\|^{2}}\right)(\boldsymbol{Y}-\boldsymbol{\nu})+\boldsymbol{\nu}-\boldsymbol{\mu}\right\|^{2}\right. \\
& =\mathscr{E}_{\boldsymbol{\mu}}\left\{\sum_{t=1}^{p}\left(Y_{i}-\mu_{1}\right)^{2}-\sum_{i=1}^{p}\left[\left(Y_{1}-\mu_{1}\right)-\frac{p-2}{\|\boldsymbol{Y}-\boldsymbol{\nu}\|^{2}}\left(Y_{1}-\boldsymbol{\nu}_{1}\right)\right]^{2}\right\} \\
& =\mathscr{E}_{\boldsymbol{\mu}}\left\{2 \frac{p-2}{\|\boldsymbol{Y}-\boldsymbol{\nu}\|^{2}} \sum_{i=1}^{p}\left(Y_{t}-\mu_{t}\right)\left(Y_{t}-\boldsymbol{\nu}_{t}\right)-\frac{(p-2)^{2}}{\|\boldsymbol{Y}-\boldsymbol{\nu}\|^{2}}\right\}
\end{aligned}
$$

Now we use Lemma 3.5.1 with
(8) $f\left(y_{1}\right)=\frac{y_{i}-\nu_{i}}{\sum_{j=1}^{p}\left(y_{j}-\nu_{j}\right)^{2}}, f^{\prime}\left(y_{i}\right)=\frac{1}{\sum_{j=1}^{p}\left(y_{j}-\nu_{j}\right)^{2}}-\frac{2\left(y_{i}-\nu_{i}\right)^{2}}{\left[\sum_{j=1}^{p}\left(y_{j}-\nu_{j}\right)^{2}\right]^{2}}$.
[For $p \geq 3$ the condition (4) is satisfied.] Then (7) is
(9) $\Delta R(\boldsymbol{\mu})=\mathscr{E}_{\boldsymbol{\mu}}\left\{2(p-2) \sum_{i=\mathbf{I}}^{p}\left[\frac{1}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{2}}-\frac{2\left(y_{i}-\nu_{i}\right)^{2}}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{4}}\right]-\frac{(p-2)^{2}}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{2}}\right\}$

$$
=(p-2)^{2} \mathscr{E}_{\mu} \frac{1}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{2}}>0 .
$$

This theorem states that 1 is inadmissible for estimating $\mu$ when $p \geq 3$, since the estimator (2) has a smaller risk for every $\boldsymbol{\mu}$ (regardless of the choice of $\boldsymbol{v}$ ).

The risk is the sum of the mean squared errors $\mathscr{E}\left[m_{i}(Y)-\mu_{i}\right]^{2}$. Since $Y_{1} \ldots, Y_{p}$ are independent and only the distribution of $Y_{i}$ depends on $\mu_{i}$, it is puzzling that the improved estimator uses all the $Y_{j}$ 's to estimate $\mu_{k}$; it seems that irrelevant information is being used. Stein explained the phenomenon by arguing that the sample distance squared of $\boldsymbol{Y}$ from $\boldsymbol{\nu}$, that is, $\|\boldsymbol{Y}-\boldsymbol{\nu}\|^{2}$, overestimates the squared distance of $\mu$ from $\boldsymbol{v}$ and hence that the estimator $\boldsymbol{Y}$ could be improved by bringing it nearer $\boldsymbol{v}$ (whatever $\boldsymbol{v}$ is). Berger (1980a), following Brown, illustrated by Figure 3.4. The four points $x_{1}, x_{2}, x_{3}, x_{4}$ represent a spherical distribution centered at $\mu$. Consider the effects of shrinkage. The average distance of $m\left(x_{1}\right)$ and $m\left(x_{3}\right)$ from $\mu$ is a little greater than that of $x_{1}$ and $x_{3}$, but $\boldsymbol{m}\left(x_{2}\right)$ and $\boldsymbol{m}\left(x_{4}\right)$ are a little closer to $\boldsymbol{\mu}$ than $x_{2}$ and $x_{\downarrow}$ are if the shrinkage is a certain amount. If $p=3$, there are two more points (not on the line $\boldsymbol{\nu}, \boldsymbol{\mu}$ ) that are shrunk closer to $\boldsymbol{\mu}$.

![](https://cdn.mathpix.com/cropped/8b5ac672-00d8-402d-a438-382999d5094a-112.jpg?height=555&width=947&top_left_y=1759&top_left_x=353)
Figure 3.4. Effect of shrinkage.

The risk of the estimator (2) is

$$
\mathscr{E}_{\mu}\|m(Y)-\mu\|^{2}=p-(p-2)^{2} \mathscr{E}_{\mu} \frac{1}{\|\boldsymbol{Y}-\nu\|^{2}},
$$

where $\|\mathbf{Y}-\boldsymbol{\nu}\|^{2}$ has a noncentral $\chi^{2}$-distribution with $p$ degrees of freedom and noncentrality parameter $\|\boldsymbol{\mu}-\boldsymbol{\nu}\|^{2}$. The farther $\boldsymbol{\mu}$ is from $\boldsymbol{\nu}$, the less the improvement due to the James-Stein estimator, but there is always some improvement. The density of $\|\boldsymbol{Y}-\boldsymbol{\nu}\|^{2}=V$, say, is (28) of Section 3.3.3, where $\boldsymbol{\tau}^{2}=\|\boldsymbol{\mu}-\boldsymbol{\nu}\|^{2}$. Then

$$
\begin{aligned}
\mathscr{E}_{\mu} \frac{1}{\|\boldsymbol{Y}-\boldsymbol{\nu}\|^{2}} & =\mathscr{E}_{\tau^{2}} V^{-1} \\
& =e^{-\frac{1}{2} \tau^{2}} 2^{-\frac{1}{2} p} \sum_{\beta=0}^{\infty}\left(\frac{\tau^{2}}{4}\right)^{\beta} \frac{1}{\beta!\Gamma\left(\frac{1}{2} p+\beta\right)} \int_{0}^{\infty} v^{\frac{1}{2} p+\beta-2} e^{-\frac{1}{2} p} d v \\
& =e^{-\frac{1}{2} \tau^{2}} 2^{-\frac{1}{2} p} \sum_{\beta=0}^{\infty}\left(\frac{\tau^{2}}{4}\right)^{\beta} \frac{\Gamma\left(\frac{1}{2} p+\beta-1\right) 2^{!p+\beta-1}}{\beta!\Gamma\left(\frac{1}{2} p+\beta\right)} \\
& =\frac{1}{2} e^{-\frac{1}{2} \tau^{2}} \sum_{\beta=0}^{\infty}\left(\frac{\tau^{2}}{2}\right)^{\beta} \frac{1}{\beta!\left(\frac{1}{2} p+\beta-1\right)}
\end{aligned}
$$

for $p \geq 3$. Note that for $\mu=\nu$, that is, $\tau^{2}=0$, (11) is $1 /(p-2)$ and the mean squared error (10) is 2 . For large ${ }^{\mu}$ the reduction in risk is considerable.

Table 3.2 gives values of the risk for $p=10$ and $\sigma^{2}=1$. For example, if $\boldsymbol{\tau}^{2}=\|\boldsymbol{\mu}-\boldsymbol{\nu}\|^{2}$ is 5 , the mean squared error of the James-Stein estimator is 8.86, compared to 10 for the natural estimator; this is the case if $\mu_{i}-\nu_{i}= 1 / \sqrt{2}=0.707, i=1, \ldots, 10$, for instance.

Table 3.2 ${ }^{\dagger}$. Average Mean Squared Error of the James-Stein Estimator for $p=10$ and $\sigma^{2}=1$
| $\boldsymbol{\tau}^{2}=\\|\boldsymbol{\mu}-\boldsymbol{\nu}\\|^{2}$ | $\mathscr{E}_{\boldsymbol{\mu}}\\|\boldsymbol{m}(\boldsymbol{Y})-\boldsymbol{\mu}\\|^{2}$ |
| :---: | :---: |
| 0.0 | 2,00 |
| 0.5 | 4.78 |
| 1.0 | 6.21 |
| 2.0 | 7.51 |
| 3.0 | 8.24 |
| 4.0 | 8.62 |
| 5.0 | 8.86 |
| 6.0 | 9.03 |


[^0]An obvious question in using an estimator of this class is how to choose the vector $\boldsymbol{v}$ toward which the observed mean vector is shrunk; any $\boldsymbol{v}$ yields an estimator better than the natural one. However, as seen from Table 3.2, the improvement is small if $\|\boldsymbol{\mu}-\boldsymbol{v}\|$ is very large. Thus, to be effective some knowledge of the position of $\mu$ is necessary. A disadvantage of the procedure is that it is not objective; the choice of $\boldsymbol{v}$ is up to the investigator.

A feature of the estimator we have been studying that seems disadvantageous is that for small values of $\|\boldsymbol{Y}-\boldsymbol{\nu}\|$, the multiplier of $\boldsymbol{Y}-\boldsymbol{\nu}$ is negative; that is, the estimator $m(Y)$ is in the direction from $\nu$ opposite to that of $Y$. This disadvantage can be overcome and the estimator improved by replacing the factor by 0 when the factor is negative.

Definition 3.5.1. For any function $g(u)$, let

$$
\begin{aligned}
g^{+}(u) & =g(u), & & g(u) \geq 0, \\
& =0, & & g(u)<0 .
\end{aligned}
$$

Lemma 3.5.2 When $X$ is distributed according to $N(\mu, I)$,

$$
\mathscr{E}_{\mu}\left\{\left\|g^{+}(\|X\|) X-\mu\right\|^{2}\right\} \leq \mathscr{E}_{\mu}\left\{\|g(\|X\|) X-\mu\|^{2}\right\} .
$$

Proof. The right-hand side of (13) minus the left-hand side is

$$
\mathscr{E}_{\mu}\left\{g^{2}(\|X\|)\|X\|^{2}-\left[g^{+}(\|X\|)\right]^{2}\|X\|^{2}\right\} \geq 0
$$

plus 2 times

$$
\begin{aligned}
\mathscr{E}_{\mu}^{\infty} \boldsymbol{\mu}^{\prime} \boldsymbol{X} & {\left[g^{+}(\|\boldsymbol{X}\|)-g(\|\boldsymbol{X}\|)\right] } \\
= & \|\boldsymbol{\mu}\| \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} y_{1}\left[g^{+}(\|\boldsymbol{y}\|)-g(\|\boldsymbol{y}\|)\right] \\
& \cdot \frac{1}{(2 \pi)^{\frac{1}{2} p}} \exp \left\{-\frac{1}{2}\left[\sum_{i=1}^{p} y_{i}^{2}-2 y_{1}\|\boldsymbol{\mu}\|+\|\boldsymbol{\mu}\|^{2}\right]\right\} d y,
\end{aligned}
$$

where $\boldsymbol{y}^{\prime}=\boldsymbol{x}^{\prime} \boldsymbol{P},(\|\boldsymbol{\mu}\|, 0, \ldots, 0)=\boldsymbol{\mu}^{\prime} \boldsymbol{P}$, and $\boldsymbol{P} \boldsymbol{P}^{\prime}=\boldsymbol{I}$. [The first column of $\boldsymbol{P}$ is $(1 /\|\boldsymbol{\mu}\|) \boldsymbol{\mu}$.] Then (15) is $\|\boldsymbol{\mu}\|$ times

$$
\begin{gathered}
e^{-\frac{1}{2}\|\mu\|^{2}} \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \int_{0}^{\infty} y_{1}\left[g^{+}\left(\|y\|_{1}\right)-g(\|y\|)\right]\left[e^{\|\mu\| y_{1}}-e^{-\|\mu\| y_{1}}\right] \\
\cdot \frac{1}{(2 \pi)^{\frac{1}{2} p}} e^{-\frac{1}{2} \sum_{p_{-1}} y_{r}^{2}} d y_{1} d y_{2} \cdots d y_{p} \geq 0
\end{gathered}
$$

(by replacing $y_{1}$ by $-y_{1}$ for $y_{1}<0$ ). $\square$

Theorem 3.5.2. The estimator

$$
m^{+}(y)=\left(1-\frac{p-2}{\|y-\nu\|^{2}}\right)^{+}(y-\nu)+\nu
$$

has smaller risk than $m(y)$ defined by (2) and is minimax.
Proof. In Lemma 3.5.2, let $g(u)=1-(p-2) / u^{2}$ and $\boldsymbol{X = \mathbf { Y } - \boldsymbol { v } \text { , and }}$ replace $\boldsymbol{\mu}$ by $\boldsymbol{\mu}-\boldsymbol{\nu}$. The second asscrtion in the theorem follows from Theorem 3.4.6.

The theorem shows that $\boldsymbol{m}(\boldsymbol{Y})$ is not admissible. However, it is known that $m^{+}(Y)$ is also not admissible, but it is believed that not much further improvement is possible.

This approach is easily extended to the case where one observes $x_{1}, \ldots, x_{\mathrm{v}}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ with loss function $L(\boldsymbol{\mu}, \boldsymbol{m})=(\boldsymbol{m}-\boldsymbol{\mu})^{\prime} \boldsymbol{\Sigma}^{-1}(\boldsymbol{m}-\boldsymbol{\mu})$. Let $\boldsymbol{\Sigma}= \boldsymbol{C} \boldsymbol{C}^{\prime}$ for some nonsingular $\boldsymbol{C}, x_{\alpha}=\boldsymbol{C} x_{\alpha}^{*}, \boldsymbol{\alpha}=1, \ldots, N, \boldsymbol{\mu}=\boldsymbol{C} \boldsymbol{\mu}^{*}$, and $L^{*}\left(\boldsymbol{m}^{*}, \boldsymbol{\mu}^{*}\right)=\left\|\boldsymbol{m}^{*}-\boldsymbol{\mu}^{*}\right\|^{2}$. Then $x_{1}^{*}, \ldots, x_{N}^{*}$ are observations from $N\left(\boldsymbol{\mu}^{*}, \boldsymbol{I}\right)$, and the problem is reduced to the earlier one. Then

$$
\left(1-\frac{p-2}{N(\bar{x}-\boldsymbol{v})^{\prime} \boldsymbol{\Sigma}^{-1}(\overline{\boldsymbol{x}}-\boldsymbol{v})}\right)^{+}(\overline{\boldsymbol{x}}-\boldsymbol{v})+\boldsymbol{v}
$$

is a minimax estimator of $\mu$.

### 3.5.3. Estimation for a General Known Covariance Matrix and an Arbitrary Quadratic Loss Function

Let the parent distribution be $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, where $\boldsymbol{\Sigma}$ is known, and let the loss function be

$$
L(\mu, m)=(m-\mu)^{\prime} Q(m-\mu),
$$

where $Q$ is an arbitrary positive definite matrix which reflects the relative importance of errors in different directions. (If the loss function were singular, the dimensionality of $x$ could be reduced so as to make the loss maxix nonsingular.) Then the sample mean $\bar{x}$ has the distribution $N(\boldsymbol{\mu},(1 / N) \boldsymbol{\Sigma})$ and risk (expected loss)

$$
\mathscr{E}(\bar{x}-\mu)^{\prime} Q(\bar{x}-\mu)=\mathscr{E} \operatorname{tr} Q(\bar{x}-\mu)(\bar{x}-\mu)^{\prime}=\frac{1}{N} \operatorname{tr} Q \Sigma,
$$

which is constant, not depending on $\mu$.

Several estimators that improve on $\bar{x}$ have been proposed. First we take up an estimator proposed independently bv Berger (1975) and Hudson (1974).

Theorem 3.5.3. Let $r(z), 0 \leq z<\infty$, be a nondecreasing differentiable function such that $0 \leq r(z) \leq 2(p-2)$. Then for $p \geq 3$

$$
m=\left(I-\frac{r\left(N^{2}(\bar{x}-\nu)^{\prime} \Sigma^{-1} Q^{-1} \Sigma^{-1}(\bar{x}-\nu)\right)}{N(\bar{x}-\nu)^{\prime} \Sigma^{-1} Q^{-1} \Sigma^{-1}(\bar{x}-\nu)} Q^{-1} \Sigma^{-1}\right)(\bar{x}-\nu)+\nu
$$

has smaller risk than $\bar{x}$ and is minimax.
Proof. There exists a matrix $C$ such that $C^{\prime} Q C=I$ and $(1 / N) \Sigma=C \Delta C^{\prime}$ where $\Delta$ is diagonal with diagonal elements $\delta_{\mathrm{I}} \geq \delta_{2} \geq \cdots \geq \delta_{p}>0$ (Theorem A. 2.2 of the Appendix). Let $\bar{x}=C y+\nu$ and $\boldsymbol{\mu}=C \boldsymbol{\mu}^{*}+\nu$. Then $y$ has the distribution $N\left(\boldsymbol{\mu}^{*}, \boldsymbol{\Delta}\right)$, and the transformed loss function is

$$
L^{*}\left(m^{*}, \mu^{*}\right)=\left(m^{*}-\mu^{*}\right)^{\prime}\left(m^{*}-\mu^{*}\right)=\left\|m^{*}-\mu^{*}\right\|^{2} .
$$

The extimator (21) of $\boldsymbol{\mu}$ is translormed to the extimator of $\boldsymbol{\mu}^{*}=\boldsymbol{C}^{-1}(\boldsymbol{\mu}-\boldsymbol{\nu})$,

$$
m^{*}(y)=\left(I-\frac{r\left(y^{\prime} \Delta^{-2} y\right)}{y^{\prime} \Delta^{-2} y} \Delta^{-1}\right) y .
$$

We now proceed as in the proof of Theorem 3.5.1. The difference in risks between $y$ and $m^{*}$ is

$$
\begin{aligned}
\Delta R\left(\boldsymbol{\mu}^{*}\right) & =\mathscr{E}_{\mu^{*}}\left\{\left\|\boldsymbol{Y}-\boldsymbol{\mu}^{*}\right\|^{2}-\left\|\boldsymbol{m}^{*}(\boldsymbol{Y})-\boldsymbol{\mu}^{*}\right\|^{2}\right\} \\
& =\mathscr{E}_{\mu^{*}}\left\{2 \frac{r\left(\boldsymbol{Y}^{\prime} \Delta^{-2} \boldsymbol{Y}\right)}{\boldsymbol{Y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{Y}} \sum_{i=1}^{p} \frac{1}{\delta_{1}} Y_{1}\left(Y_{1}-\mu_{1}^{*}\right)-\frac{r^{2}\left(\boldsymbol{Y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{Y}\right)}{\boldsymbol{Y}^{\prime} \Delta^{-2} \boldsymbol{Y}}\right\} .
\end{aligned}
$$

Since $r(z)$ is differentiable, we use Lemma 3.5.1 with $(x-\theta)=\left(y_{i}-\mu_{i}^{*}\right) \delta_{i}$ and

$$
\begin{aligned}
& f\left(y_{1}\right)=\frac{r\left(\boldsymbol{y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{y}\right)}{\boldsymbol{y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{y}} y_{1}, \\
& f^{\prime}\left(y_{1}\right)=\frac{r\left(\boldsymbol{y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{y}\right)}{\boldsymbol{y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{y}}+\frac{2 r^{\prime}\left(\boldsymbol{y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{y}\right)}{\boldsymbol{y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{y}} \frac{y_{1}^{2}}{\delta_{1}^{2}}-\frac{2 r\left(\boldsymbol{y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{y}\right)}{\left(\boldsymbol{y}^{\prime} \boldsymbol{\Delta}^{-2} \boldsymbol{y}\right)^{2}} \frac{y_{1}^{2}}{\delta_{1}^{2}} .
\end{aligned}
$$

Then

$$
\Delta R\left(\mu^{*}\right)=\mathscr{E}_{\mu^{*}}\left\{2(p-2) \frac{r\left(Y^{\prime} \Delta^{-2} Y\right)}{Y^{\prime} \Delta^{-2} Y}+4 r^{\prime}\left(Y^{\prime} \Delta^{-2} Y\right)-\frac{r^{2}\left(Y^{\prime} \Delta^{-2} Y\right)}{Y^{\prime} \Delta^{-2} Y}\right\} \geq 0
$$

since $r\left(y^{\prime} \Delta^{-2} y\right) \leq 2(p-2)$ and $r^{\prime}\left(y^{\prime} \Delta^{-2} y\right) \geq 0$. $\square$

Corollary 3.5.1. For $p \geq 3$

$$
\left\{I-\frac{\min \left[p-2, N^{2}(\bar{x}-v)^{\prime} \Sigma^{-1} Q^{-1} \Sigma^{-1}(\bar{x}-v)\right]}{N(\bar{x}-v)^{\prime} \Sigma^{-1} Q^{-1} \Sigma^{-1}(\bar{x}-v)} Q^{-1} \Sigma^{-1}\right\}(\bar{x}-v)+v
$$

has smaller rish than $\bar{x}$ and is minimax.

Proof. the function $r(z)=\min (p-2, z)$ is differentiable except at $z= p-2$. The function $r(z)$ can be approximated arbitrarily closely by a differentiable function. (For example, the corner at $z=p-2$ can be smoothed by a circular arc of arbitrary small radius.) We shall not give the details of the proof. $\square$

In canonical form $y$ is shrunk by a scalar times a diagonal matrix. The larger the variance of a component is, the less the effect of the shrinkage.

Berger (1975) has proved these results for a more general density, that is, for a mixture of normals. Berger (1976) has also proved in the case of normality that if

$$
r(z)=\frac{z \int_{0}^{\alpha} u^{\frac{1}{2} p-c+1} e^{-\frac{1}{2} u z} d u}{\int_{0}^{\alpha} u^{\frac{1}{2} p-c} e^{-\frac{1}{2} u z} d u}
$$

for $3-\frac{1}{2} p \leq c<1+\frac{1}{2} p$, where $\alpha$ is the smallest characteristic root of $\Sigma Q$, then the estimator $m$ given by (21) is minimax, is admissible if $c<2$, and is proper Bayes if $c<1$.

Another approach to minimax estimators has been introduced by Bhattacharya (1966). Let $C$ be such that $C^{-1}(1 / N) \Sigma\left(C^{-1}\right)^{\prime}=I$ and $C^{\prime} Q C=Q^{*}$, which is diagonal with diagonal elements $q_{1}^{*} \geq q_{2}^{*} \geq \cdots \geq q_{p}^{*}>0$. Then $y=$
$\boldsymbol{C}^{-\boldsymbol{I}} \bar{x}$ has the distribution $N\left(\boldsymbol{\mu}^{*}, \boldsymbol{I}\right)$, and the loss function is

$$
\begin{aligned}
\boldsymbol{L}^{*}\left(\boldsymbol{m}^{*}, \boldsymbol{\mu}^{*}\right) & =\sum_{i=1}^{p} q_{i}^{*}\left(m_{i}^{*}-\mu_{i}^{*}\right)^{2} \\
& =\sum_{i=1}^{p} \sum_{j=i}^{p} \alpha_{j}\left(m_{i}^{*}-\mu_{i}^{*}\right)^{2} \\
& =\sum_{j=1}^{p} \alpha_{j} \sum_{i=1}^{j}\left(m_{i}^{*}-\mu_{i}^{*}\right)^{2} \\
& =\sum_{j=1}^{p} \alpha_{j}\left\|\boldsymbol{m}^{*(J)}-\boldsymbol{\mu}^{*(J)}\right\|^{2}
\end{aligned}
$$

where $\alpha_{j}=q_{j}^{*}-q_{j+1}^{*}, j=1, \ldots, p-1, \alpha_{p}=q_{p}^{*}, m^{*(l)}=\left(m_{1}^{*}, \ldots, m_{j}^{*}\right)^{\prime}$, and $\boldsymbol{\mu}^{*(j)}=\left(\mu_{1}^{*}, \ldots, \mu_{j}^{*}\right)^{\prime}, j=1, \ldots, p$. This decomposition of the loss function suggests combining minimax estimators of the vectors $\mu^{*(j)}, j=1, \ldots, p$. Let $\boldsymbol{y}^{(j)}=\left(y_{1}, \ldots, y_{j}\right)^{\prime}$.

Theorem 3.5.4. If $\boldsymbol{h}^{(j)}\left(\boldsymbol{y}^{(j)}\right)=\left[h_{\mathrm{I}}^{(j)}\left(\boldsymbol{y}^{(j)}\right), \ldots, h^{(j)}\left(\boldsymbol{y}^{(j)}\right)\right]^{\prime}$ is a minimax estimator of $\boldsymbol{\mu}^{*(j)}$ under the loss function $\left\|\boldsymbol{m}^{*(j)}-\boldsymbol{\mu}^{*(j)}\right\|^{2}, j=1, \ldots, p$, then

$$
\frac{1}{q_{i}^{*}} \sum_{j=1}^{p} \alpha_{j} h_{i}^{(j)}\left(y^{(j)}\right), \quad i=1, \ldots, p
$$

is a minimax estimator of $\mu_{1}^{*}, \ldots, \mu_{p}^{*}$.
Proof. First consider the randomized estimator defined by

$$
\operatorname{Pr}\left\{G_{i}(y)=h_{i}^{(\nu)}\left(y^{(j)}\right)\right\}=\frac{\alpha j}{q_{i}^{*}}, \quad j=i, \ldots, p
$$

for the $i$ th component. Then the risk of this estimator is

$$
\begin{aligned}
\sum_{i=1}^{p} q_{i}^{*} \mathscr{E}_{\mu^{*}}\left[G_{i}(Y)-\mu_{t}^{*}\right]^{2} & =\sum_{i=1}^{p} q_{i}^{*} \sum_{j=i}^{p} \frac{\alpha_{j}}{q_{i}^{*}} \mathscr{E}_{\mu^{*}}\left[h_{i}^{(j)}\left(Y^{(j)}\right)-\mu_{i}^{*}\right]^{2} \\
& =\sum_{j=1}^{p} \alpha_{j} \sum_{i=1}^{j} \mathscr{E}_{\mu^{*}}\left[h_{1}^{(j)}\left(Y^{(j)}\right)-\mu_{i}^{*}\right]^{2} \\
& =\sum_{j=1}^{p} \alpha_{j} \mathscr{E}_{\mu^{*}}\left\|h^{(j)}\left(Y^{(j)}\right)-\mu^{*(j)}\right\|^{2} \\
& \leq \sum_{j=1}^{p} \alpha_{j} j=\sum_{j=1}^{p} q_{j}^{*} \\
& =\mathscr{E}_{\mu^{*}} L^{*}\left(Y, \mu^{*}\right)^{*}
\end{aligned}
$$

and hence the estimator defined by (32) is minimax.

Since the expected value of $G_{i}(Y)$ with respect to (32) is (31) and the loss function is convex, the risk of the estimator (31) is less than that of the randomized estimator (by Jensen's inequality).

### 3.6. ELLIPTICALLY CONTOURED DISTRIBUTIONS

### 3.6.1. Observations Elliptically Contoured

Let $x_{1}, \ldots, x_{N}$ be $N(=n+1)$ independent observations on a random vector $\boldsymbol{X}$ with density $|\boldsymbol{\Lambda}|^{-\frac{1}{2}} g\left[\left(x_{\alpha}-\boldsymbol{v}\right)^{\prime} \boldsymbol{\Lambda}^{-1}\left(x_{\alpha}-\boldsymbol{v}\right)\right]$. The density of the sample is

$$
|\boldsymbol{\Lambda}|^{-\frac{1}{2} N} \prod_{\alpha=1}^{N} g\left[(x-\boldsymbol{v})^{\prime} \boldsymbol{\Lambda}^{-1}(x-\boldsymbol{v})\right] .
$$

The sample mean $\bar{x}$ and covariance matrix $S=(1 / n)\left[\sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu\right)\left(x_{\alpha}-\mu\right)^{\prime}\right. \left.-N(\bar{x}-\mu)(\bar{x}-\mu)^{\prime}\right]$ are unbiased estimators of the mean $\mu=\nu$ and the covariance matrix $\Sigma=\left[\mathscr{E} R^{2} / p\right] \Lambda$, where $R^{2}=(x-v)^{\prime} \Lambda^{-1}(x-v)$.

Theorem 3.6.1. The covariances of the mean and covariance of a sample of $N$ from $|\boldsymbol{\Lambda}|^{-\frac{1}{2}} g\left[(x-\boldsymbol{v})^{\prime} \boldsymbol{\Lambda}^{-1}(x-\boldsymbol{v})\right]$ with $\mathscr{E} R^{4}<\infty$ are

$$
\begin{aligned}
\mathscr{E}(\bar{x}-\boldsymbol{\mu})(\bar{x}-\boldsymbol{\mu})^{\prime}= & \frac{1}{N} \boldsymbol{\Sigma}, \\
\mathscr{E}\left(s_{i j}-\sigma_{i j}\right)(\bar{x}-\boldsymbol{\mu})= & \mathbf{0}, \\
\mathscr{E}\left(s_{i j}-\sigma_{i j}\right)\left(s_{k l}-\sigma_{k l}\right)= & \frac{\kappa}{N}\left(\sigma_{i j} \sigma_{k l}+\sigma_{i k} \sigma_{i l}+\sigma_{i l} \sigma_{j k}\right) \\
& +\frac{1}{n}\left(\sigma_{i k} \sigma_{j l}+\sigma_{i l} \sigma_{k l}\right), \quad i, j=1 \ldots, j, k, l=1 \ldots, p .
\end{aligned}
$$

Lemma 3.6.1. The second-order moments of the elements of $\boldsymbol{S}$ are
(5) $\mathscr{E} s_{i j} s_{k l}=\sigma_{i l} \sigma_{k l}+\frac{1}{n}\left(\sigma_{i k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}\right)+\frac{\kappa}{N}\left(\sigma_{i j} \sigma_{k l}+\sigma_{i k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}\right)$,

$$
i, j, k, l,=1, \ldots, p
$$

Proof of Lemma 3.6.1. We have
(6) $\mathscr{E} \sum_{\alpha, \beta=\mathrm{I}}^{N}\left(x_{\imath \alpha}-\mu_{\imath}\right)\left(x_{\jmath \alpha}-\mu_{l}\right)\left(x_{k \beta}-\mu_{k}\right)\left(s_{1 \beta}-\mu_{i}\right)$

$$
\begin{aligned}
= & N \mathscr{E}\left(x_{i \alpha}-\mu_{1}\right)\left(x_{1 \alpha}-\mu_{1}\right)\left(x_{k \alpha}-\mu_{k}\right)\left(x_{1 \alpha}-\mu_{1}\right) \\
& +N(N-1) \mathscr{E}\left(x_{1 \alpha}-\mu_{1}\right)\left(x_{1 \alpha}-\mu_{1}\right) \mathscr{E}\left(x_{k \beta}-\mu_{k}\right)\left(x_{1 \beta}-\mu_{1}\right) \\
= & N(1+\kappa)\left(\sigma_{1 j} \sigma_{k 1}+\sigma_{i k} \sigma_{1 i}+\sigma_{1 i} \sigma_{1 k}\right)+N(N-1) \sigma_{1 j} \sigma_{k 1},
\end{aligned}
$$

$$
\begin{aligned}
& \mathscr{S} N^{-}\left(\bar{x}_{1}-\mu_{i}\right)\left(\bar{x}_{j}-\mu_{j}\right)\left(\bar{x}_{k}-\mu_{k}\right)\left(\bar{x}_{l}-\mu_{l}\right) \\
& =\frac{1}{N^{2}} \sum_{\alpha, \beta, \gamma, \delta=1}^{N}\left(x_{1 \alpha}-\mu_{l}\right)\left(x_{j \beta}-\mu_{j}\right)\left(x_{k \gamma}-\mu_{\gamma}\right)\left(x_{l \delta}-\mu_{l}\right) \\
& =\frac{1}{N}(1+\kappa)\left(\sigma_{i j} \sigma_{k l}+\sigma_{i k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}\right) \\
& \quad+\frac{N-1}{N}\left(\sigma_{i j} \sigma_{k i}+\sigma_{i k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \sum_{\alpha=1}^{N}\left(x_{i \alpha}-\mu_{1}\right)\left(x_{j \alpha}-\mu_{j}\right) \frac{1}{N} \sum_{\beta \cdot \gamma=1}^{N}\left(x_{k \beta}-\mu_{k}\right)\left(x_{i \gamma}-\mu_{\gamma}\right) \\
& \quad=(1+\kappa)\left(\sigma_{i j} \sigma_{k i}+\sigma_{i k} \sigma_{j l}+\sigma_{i l} \sigma_{j k}\right)+(N-1) \sigma_{i j} \sigma_{k l}
\end{aligned}
$$

It will be convenient to use more matrix algebra. Define vec $\boldsymbol{B}, \boldsymbol{B} \otimes \boldsymbol{C}$ (the Kronecker product), and $\boldsymbol{K}_{m \cdot}$ (the commutator matrix) by

$$
\begin{aligned}
\operatorname{vec} B & =\operatorname{vec}\left(b_{1}, \ldots, b_{n}\right)=\left[\begin{array}{c}
b_{1} \\
\vdots \\
b_{n}
\end{array}\right], \\
B \otimes C & =\left[\begin{array}{ccc}
b_{11} C & \cdots & b_{1 n} C \\
\vdots & & \vdots \\
b_{m 1} C & \cdots & b_{m n} C
\end{array}\right], \\
K_{m n} \operatorname{vec} B & =\operatorname{vec} B^{\prime} .
\end{aligned}
$$

See. e.g., Magnus and Neudecker (1979) or Section A. 5 of the Appendix. We can rewrite (4) as

$$
\begin{aligned}
\mathscr{U}(\operatorname{vec} S) & =\mathscr{E}(\operatorname{vec} S-\operatorname{vec} \Sigma)(\operatorname{vec} S-\operatorname{vec} \Sigma)^{\prime} \\
& =\frac{n \kappa+N}{n N}\left(I_{p}+K_{p p}\right)(\Sigma \otimes \Sigma)+\frac{\kappa}{N} \operatorname{vec} \Sigma(\operatorname{vec} \Sigma)^{\prime}
\end{aligned}
$$

## Theorem 3.6.2

(13)

$$
\begin{aligned}
& \sqrt{n}\left[\begin{array}{c}
(\overline{\boldsymbol{x}}-\boldsymbol{\mu}) \\
\operatorname{vec} S-\operatorname{vec} \Sigma
\end{array}\right] \\
& \xrightarrow{d} N\left[\binom{\mathbf{0}}{\mathbf{0}},\left(\begin{array}{cc}
\Sigma & 0 \\
\mathbf{0} & (\kappa+1)\left(\boldsymbol{I}_{p^{2}}+\boldsymbol{K}_{p D}\right)(\Sigma \otimes \Sigma)+\kappa \operatorname{vec} \Sigma(\operatorname{vec} \Sigma)^{\prime}
\end{array}\right)\right]
\end{aligned}
$$


[^0]:    ${ }^{\dagger}$ From Efron and Morris (1977).



This theorem follows from the central limit theorem for independent identically distributed random vectors (with finite fourth moments). The theorem forms the basis for large-sample inference.

### 3.6.2. Estimation of the Kurtosis Parameter

To apply the large-sample distribution theory derived for normal distributions to problems of inference for elliptically contoured distributions it is necessary to know or estimate the kurtosis parameter $\kappa$. Note that

$$
\begin{aligned}
\mathscr{E}\left[(X-\mu)^{\prime} \Sigma^{-1}(X-\mu)\right]^{2} & =\left(\frac{p}{\mathscr{E} R^{2}}\right)^{2} \mathscr{E}\left(Y^{\prime} Y\right)^{2} \\
& =\frac{p^{2} \mathscr{E} R^{4}}{\left(\mathscr{E} R^{2}\right)^{2}}=p(p+2)(1+\kappa)
\end{aligned}
$$

Since $\bar{x} \xrightarrow{p} \mu$ and $S \xrightarrow{p} \Sigma$,

$$
\frac{1}{N} \sum_{\alpha=1}^{N}\left[\left(x_{\alpha}-\bar{x}\right)^{\prime} S^{-1}\left(x_{\alpha}-\bar{x}\right)\right]^{2} \xrightarrow{p} p(p+2)(1+\kappa) .
$$

A consistent estimator of $\kappa$ is

$$
\hat{\kappa}=\frac{1}{p(p+2)} \frac{1}{N} \sum_{\alpha=1}^{N}\left[\left(x_{\alpha}-\bar{x}\right)^{\prime} S^{-1}\left(x_{\alpha}-\bar{x}\right)\right]^{2}-1 .
$$

Mardia (1970) proposed using $M$ to form a consistent estimator of $\kappa$.

### 3.6.3. Maximum Likelihood Estimation

We have considered using $S$ as an estimator of $\Sigma=\left(\mathscr{E} R^{2} / p\right) \Lambda$. When the parent distribution is normal, $\boldsymbol{S}$ is the sufficient statistic invariant with respect to translations and hence is the efficient unbiased estimator. Now we study other estimators.

We consider first the maximum likelihood estimators of $\boldsymbol{\mu}$ and $\boldsymbol{\Lambda}$ when the form of the density $g(\cdot)$ is known. The logarithm of the likelihood function is

$$
\log L=-\frac{N}{2} \log |\Lambda|+\sum_{\alpha=1}^{N} \log g\left[\left(x_{\alpha}-\mu\right)^{\prime} \Lambda^{-1}\left(x_{\alpha}-\mu\right)\right] .
$$

The derivatives of $\log L$ with respect to the components of $\boldsymbol{\mu}$ are

$$
\frac{\partial \log L}{\partial \boldsymbol{\mu}}=-2 \sum_{\alpha=1}^{N} \frac{g^{\prime}\left[\left(x_{\alpha}-\boldsymbol{\mu}\right)^{\prime} \Lambda^{-1}\left(x_{\alpha}-\boldsymbol{\mu}\right)\right]}{g\left[\left(x_{\alpha}-\boldsymbol{\mu}\right)^{\prime} \Lambda^{-1}\left(x_{\alpha}-\boldsymbol{\mu}\right)\right]} \Lambda^{-1}\left(x_{\alpha}-\boldsymbol{\mu}\right) .
$$

Setting the vector of derivatives equal to $\mathbf{0}$ leads to the equation

$$
\sum_{\alpha=1}^{N} \frac{g^{\prime}\left[\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)^{\prime} \hat{\boldsymbol{\Lambda}}^{-1}\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)\right]}{g\left[\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)^{\prime} \hat{\boldsymbol{\Lambda}}^{-1}\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)\right]} x_{\alpha}=\hat{\boldsymbol{\mu}} \sum_{\alpha=1}^{N} \frac{g^{\prime}\left[\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)^{\prime} \hat{\boldsymbol{\Lambda}}^{-1}\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)\right]}{g\left[\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)^{\prime} \hat{\boldsymbol{\Lambda}}^{-1}\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)\right]} .
$$

Setting equal to 0 the derivatives of $\log L$ with respect to the elements of $\mathbf{\Lambda}^{-1}$ gives

$$
\hat{\boldsymbol{\Lambda}}=-\frac{2}{N} \sum_{\alpha=1}^{N} \frac{g^{\prime}\left[\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)^{\prime} \hat{\boldsymbol{\Lambda}}^{-1}\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)\right]}{g\left[\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)^{\prime} \hat{\boldsymbol{\Lambda}}^{-1}\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)\right]}\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)^{\prime} .
$$

The estimator $\hat{\boldsymbol{\Lambda}}$ is a kind of weighted average of the rank 1 matrices $\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)\left(x_{\alpha}-\hat{\boldsymbol{\mu}}\right)^{\prime}$. In the normal case the weights are $1 / N$. In most cases (19) and (20) cannot be solved explicitly, but the solution may be approximated by iterative methods.

The covariance matrix of the limiting normal distribution of $\sqrt{N}$ (vec $\hat{\Lambda}-$ vec $\boldsymbol{\Lambda}$ ) is

$$
\mathscr{C}(\operatorname{vec} \hat{\Lambda})=\sigma_{1 g}\left(I_{p^{2}}+K_{p p}\right)(\mathbf{\Lambda} \otimes \mathbf{\Lambda})+\sigma_{2 g} \operatorname{vec} \mathbf{\Lambda}(\operatorname{vec} \mathbf{\Lambda})^{\prime},
$$

where

$$
\begin{aligned}
\sigma_{1 g} & =\frac{p(p+2)}{4 \mathscr{E}\left[\frac{g^{\prime}\left(R^{2}\right)}{g\left(R^{2}\right)} R^{2}\right]^{2}}, \\
\sigma_{2 g} & =\frac{2 \sigma_{1 g}\left(1-\sigma_{1 g}\right)}{2+p\left(1-\sigma_{1 g}\right)} .
\end{aligned}
$$

See Tyler (1982).

### 3.6.4. Elliptically Contoured Matrix Distributions

Let

$$
\mathbf{Y}=\left[\begin{array}{c}
y_{1}^{\prime} \\
\vdots \\
y_{N}^{\prime}
\end{array}\right]
$$

be an $N \times p$ random matrix with density $g\left(Y^{\prime} Y\right)=g\left(\sum_{\alpha=1}^{N} y_{\alpha} y_{\alpha}^{\prime}\right)$. Note that the density $g\left(Y^{\prime} Y\right)$ is invariant with respect to orthogonal transformations $\boldsymbol{Y}^{\boldsymbol{*}}=\mathbf{O}_{N} \boldsymbol{Y}$. Such densities are known as left spherical matrix densities. An example is the density of $N$ observations from $N\left(\mathbf{0}, \boldsymbol{I}_{p}\right)$,

$$
g\left(Y^{\prime} Y\right)=\frac{1}{(2 \pi)^{\frac{1}{2} p N}} e^{-\frac{1}{2} \operatorname{tr} Y^{\prime} Y}
$$

In this example $Y$ is also right spherical: $Y O_{p} \stackrel{d}{=} Y$. When $Y$ is both left spherical and right spherical, it is known as spherical. Further, if $Y$ has the density (25), vec $\boldsymbol{Y}$ is spherical; in general if $\boldsymbol{Y}$ has a density, the density is of the form

$$
\begin{aligned}
g\left(\mathrm{t} \cdot \boldsymbol{Y}^{\prime} \boldsymbol{Y}\right) & =g\left(\sum_{\alpha=1}^{N} \sum_{\ell=1}^{p} y_{\ell \alpha}^{2}\right)=g\left(\operatorname{tr} \boldsymbol{Y} \boldsymbol{Y}^{\prime}\right) \\
& =g\left[(\operatorname{vec} \boldsymbol{Y})^{\prime} \operatorname{vec} \boldsymbol{Y}\right]=g\left[\left(\operatorname{vec} \boldsymbol{Y}^{\prime}\right)^{\prime} \operatorname{vec} \boldsymbol{Y}^{\prime}\right]
\end{aligned}
$$

We call this model vector-spherical. Define

$$
X=Y C^{\prime}+\varepsilon_{N} \mu^{\prime},
$$

where $\boldsymbol{C}^{\prime} \boldsymbol{\Lambda}^{-1} \boldsymbol{C}=\boldsymbol{I}_{p}$ and $\boldsymbol{\varepsilon}_{N}^{\prime}=(1, \ldots, 1)$. Since (27) is equivalent to $\boldsymbol{Y}= \left(\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \boldsymbol{\mu}^{\prime}\right)\left(\boldsymbol{C}^{\prime}\right)^{-1}$ and $\left(\boldsymbol{C}^{\prime}\right)^{-1} \boldsymbol{C}^{-1}=\mathbf{A}^{-1}$, the matrix $X$ has the density

$$
\begin{aligned}
& |\boldsymbol{\Lambda}|^{-N / 2} g\left[\operatorname{tr}\left(X-\boldsymbol{\varepsilon}_{N^{\prime}} \boldsymbol{\mu}^{\prime}\right) \boldsymbol{\Lambda}^{-1}\left(X-\boldsymbol{\varepsilon}_{N} \boldsymbol{\mu}^{\prime}\right)^{\prime}\right] \\
& \quad=|\boldsymbol{\Lambda}|^{-N / 2} g\left[\sum_{\alpha=1}^{N}\left(x_{\alpha}-\boldsymbol{\mu}\right)^{\prime} \boldsymbol{\Lambda}^{-1}\left(x_{\alpha}-\boldsymbol{\mu}\right)\right] .
\end{aligned}
$$

From (26) we deduce that vec $\boldsymbol{Y}$ has the representation

$$
\operatorname{vec} Y \stackrel{d}{=} R \operatorname{vec} U
$$

where $w=R^{2}$ has the density

$$
\frac{\pi^{\frac{1}{2} N p}}{\Gamma(N p / 2)} w^{\frac{1}{2} N p-1} g(w),
$$

vec $U$ has the uniform distribution on $\sum_{\alpha=1}^{N} \sum_{i=1}^{p} u_{i \alpha}^{2}=1$, and $R$ and vec $U$ are independent. The covariance matrix of vec $Y$ is

$$
\mathscr{E} \operatorname{vec} Y(\operatorname{vec} Y)^{\prime}=\frac{\mathscr{E} R^{2}}{N p} I_{N p}=\frac{\mathscr{E} R^{2}}{N p}\left(I_{n} \otimes I_{N}\right)
$$

Since vec $\boldsymbol{F} \boldsymbol{G} \boldsymbol{H}=\left(\boldsymbol{H}^{\prime} \otimes \mathbf{F}\right)$ vec $\boldsymbol{G}$ for any conformable matrices $\boldsymbol{F}, \boldsymbol{G}$, and $\boldsymbol{H}$, we can write (27) as

$$
\operatorname{vec} \boldsymbol{X}=\left(\boldsymbol{C} \otimes I_{N}\right) \operatorname{vec} Y+\boldsymbol{\mu} \otimes \varepsilon_{N} .
$$

Thus

$$
\begin{aligned}
\mathscr{E} \operatorname{vec} X & =\boldsymbol{\mu} \otimes \varepsilon_{N} \\
\mathscr{C}(\operatorname{vec} X) & =\left(\boldsymbol{C} \otimes I_{N}\right) \mathscr{C}(\operatorname{vec} Y)\left(\boldsymbol{C}^{\prime} \otimes I_{N}\right)=\frac{\mathscr{E} R^{2}}{N p} \boldsymbol{\Lambda} \otimes I_{N} \\
\mathscr{E}(\text { row of } \boldsymbol{X}) & =\boldsymbol{\mu}^{\prime} \\
\mathscr{C}\left(\text { row of } X^{\prime}\right) & =\frac{\mathscr{E} R^{2}}{N p} \boldsymbol{\Lambda}
\end{aligned}
$$

The rows of $\boldsymbol{X}$ are uncorrelated (though not necessarily independent). From (32) we obtain

$$
\begin{aligned}
& \operatorname{vec} \boldsymbol{X} \stackrel{d}{=} R\left(\boldsymbol{C} \otimes \boldsymbol{I}_{N}\right) \operatorname{vec} \boldsymbol{U}+\boldsymbol{\mu} \otimes \boldsymbol{\varepsilon}_{N} \\
& \quad \boldsymbol{X} \stackrel{d}{=} R \boldsymbol{U} \boldsymbol{C}^{\prime}+\boldsymbol{\varepsilon}_{N} \boldsymbol{\mu}^{\prime}
\end{aligned}
$$

Since $\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \boldsymbol{\mu}^{\prime}=\left(\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \overline{\boldsymbol{x}}^{\prime}\right)+\boldsymbol{\varepsilon}_{N}(\overline{\boldsymbol{X}}-\boldsymbol{\mu})^{\prime}$ and $\boldsymbol{\varepsilon}_{N}^{\prime}\left(\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \overline{\boldsymbol{x}}^{\prime}\right)=\mathbf{0}$, we can write the density of $X$ as

$$
|\boldsymbol{\Lambda}|^{-N / 2} g\left[\operatorname{tr} \boldsymbol{\Lambda}^{-1}\left(x-\boldsymbol{\varepsilon}_{N} \overline{\boldsymbol{x}}^{\prime}\right)^{\prime}\left(\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \bar{x}^{\prime}\right)+N(\overline{\boldsymbol{x}}-\boldsymbol{\mu})^{\prime} \boldsymbol{\Lambda}^{-1}(\overline{\boldsymbol{x}}-\boldsymbol{\mu})\right],
$$

where $\overline{\boldsymbol{x}}=(1 / N) X^{\prime} \boldsymbol{\varepsilon}_{N}$. This shows that a sufficient set of statistics for $\boldsymbol{\mu}$ and $\boldsymbol{\Lambda}$ is $\overline{\boldsymbol{x}}$ and $n S=\left(\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \bar{x}^{\prime}\right)^{\prime}\left(\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \bar{x}^{\prime}\right)$, as for the normal distribution. The maximum likelihood estimators can be derived from the following theorem, which will be used later for other models.

Theorem 3.6.3. Suppose the $m$-component vector $Z$ has the density $|\boldsymbol{\Phi}|^{-\frac{1}{4}} h\left[(z-\boldsymbol{v})^{\prime} \boldsymbol{\Phi}^{-\mathbf{I}}(z-\boldsymbol{v})\right]$, where $w^{\frac{1}{2} m} h(w)$ has a finite positive maximum at $w_{h}$ and $\boldsymbol{\Phi}$ is a positive definite matrix. Let $\Omega$ be a set in the space of ( $\boldsymbol{\nu}, \boldsymbol{\Phi}$ ) such that if $(\boldsymbol{\nu}, \boldsymbol{\Phi}) \in \Omega$ then $(\boldsymbol{\nu}, c \boldsymbol{\Phi}) \in \Omega$ for all $c>0$. Suppose that on the basis of an observation $z$ when $h(w)=$ const $e^{-\frac{1}{2} w}$ (i.e., $Z$ has a normal distribution) the maximum likelihood estimator $(\overline{\boldsymbol{v}}, \overline{\boldsymbol{\Phi}}) \in \Omega$ exists and is unique with $\overline{\mathbf{\Phi}}$ positive definite with probability 1. Then the maximum likelihood estimator of ( $\boldsymbol{\nu}, \boldsymbol{\Phi}$ ) for arbitrary $h(\cdot)$ is

$$
\hat{\boldsymbol{v}}=\overline{\boldsymbol{v}}, \quad \hat{\boldsymbol{\Phi}}=\frac{m}{w_{h}} \overline{\boldsymbol{\Phi}}
$$

and the maximum of the likelihood is $|\hat{\boldsymbol{\Phi}}|^{-\frac{1}{2}} h\left(w_{h}\right)$ [Anderson, Fang, and Hsu (1986)].

Proof. Let $\boldsymbol{\Psi}=|\boldsymbol{\Phi}|^{-1 / m} \boldsymbol{\Phi}$ and

$$
d=(z-\boldsymbol{\nu})^{\prime} \boldsymbol{\Phi}^{-1}(z-\boldsymbol{\nu})=\frac{(z-\boldsymbol{\nu})^{\prime} \boldsymbol{\Psi}^{-1}(z-\boldsymbol{\nu})}{|\boldsymbol{\Phi}|^{1 / m}} .
$$

Then $(\boldsymbol{\nu}, \boldsymbol{\Phi}) \in \Omega$ and $|\boldsymbol{\Psi}|=1$. The likelihood is

$$
\left[(z-\boldsymbol{v})^{\prime} \boldsymbol{\Psi}^{-1}(z-\boldsymbol{v})\right]^{-\frac{1}{2} m} d^{\frac{1}{2} m} h(d) .
$$

Under normality $h(d)=(2 \pi)^{-\frac{1}{2} / n} e^{-\frac{1}{2} d}$, and the maximum of (42) is attained at $\boldsymbol{\nu}=\overline{\boldsymbol{\nu}}, \boldsymbol{\Psi}=\overline{\boldsymbol{\Psi}}=|\overline{\boldsymbol{\Phi}}|^{-1 / m} \overline{\boldsymbol{\Phi}}$, and $d=m$. For arbitrary $h(\cdot)$ the maximum of (42) is attained at $\hat{\boldsymbol{\nu}}=\overline{\boldsymbol{\nu}}, \hat{\boldsymbol{B}}=\overline{\boldsymbol{B}}$, and $\hat{d}=w_{h}$. Then the maximum likelihood estimator of $\boldsymbol{\Phi}$ is

$$
\hat{\boldsymbol{\Phi}}=|\hat{\boldsymbol{\Phi}}|^{1 / m} \hat{\boldsymbol{\Psi}}=\frac{|\hat{\boldsymbol{\Phi}}|^{1 / m}}{|\overline{\boldsymbol{\Phi}}|^{1 / m}} \overline{\boldsymbol{\Phi}} .
$$

Then (40) follows from (43) by use of (41).
Theorem 3.6.4. Let $X(N \times p)$ have the density (28), where $w^{\frac{1}{2} N p} g(w)$ has a finite positive maximum at $w_{g}$. Then the maximum likelihood estimators of $\mu$ and $\mathbf{\Lambda}$ are

$$
\hat{\boldsymbol{\mu}}=\overline{\boldsymbol{x}}, \quad \hat{\boldsymbol{\Lambda}}=\frac{N p}{w_{g}} \boldsymbol{A},
$$

where $A=\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}$.
Corollary 3.6.1. Let $\boldsymbol{X}(N \times p)$ have the density (28). Then the maximum likelihood estimators of $\nu,\left(\lambda_{11}, \ldots, \lambda_{p p}\right)$, and $\rho_{i p}, i, j=1, \ldots, p$, are $\bar{x}$, $\left(p / w_{g}\right)\left(a_{11}, \ldots, a_{p p}\right)$, and $a_{i j} / \sqrt{a_{i i} a_{j j}}, i, j=1, \ldots, p$.

Proof. Corollary 3.6.1 follows from Theorem 3.6.3 and Corollary 3.2.1.
Theorem 3.6.5. Let $f(X)$ be a vector-valued function of $X(N \times p)$ such that

$$
f\left(X+\varepsilon_{N} \nu^{\prime}\right)=f(X)
$$

for all v und

$$
f(c X)=f(X)
$$

for all $c$. Then the distribution of $f(X)$ where $X$ has an arbitrary density (28) is the same as its distribution where $X$ has the normal density (28).

Proof. Substitution of the representation (27) into $f(X)$ gives

$$
f(X)=f\left(Y C^{\prime}+E_{N} \mu^{\prime}\right)=f\left(Y C^{\prime}\right)
$$

by (45). Let $f(X)=h(\operatorname{vec} X)$. Then by (46), $h(c X)=h(X)$ and

$$
\begin{aligned}
f\left(Y C^{\prime}\right) & =h\left[\left(C \otimes I_{N}\right) \operatorname{vec} Y\right]=h\left[R\left(C \otimes I_{N}\right) \operatorname{vec} U\right] \\
& =h\left[\left(C \otimes I_{N}\right) \operatorname{vec} U\right] .
\end{aligned}
$$

Any statistic satisfying (45) and (46) has the same distribution for all $g(\cdot)$. Hence, if its distribution is known for the normal case, the distribution is valid for all elliptically contoured distributions.

Any function of the sufficient set of statistics that is translation-invariant, that is, that satisfies (45), is a function of $\boldsymbol{S}$. Thus inference concerning $\boldsymbol{\Sigma}$ can be based on $S$.

Corollary 3.6.2. Let $f(X)$ be a vector-valued function of $X(N \times p)$ such that (46) holds for all $c$. Then the distribution of $f(X)$ where $X$ has arbitrary density (28) with $\boldsymbol{\mu}=\mathbf{0}$ is the same as its distribution where $\boldsymbol{X}$ has normal density (28) with $\boldsymbol{\mu}=\mathbf{0}$.

Fang and Zhang (1990) give this corollary as Theorem 2.5.8.

## PROBLEMS

3.1. (Sec. 3.2) Find $\hat{\mu}, \hat{\Sigma}$, and ( $\hat{\rho}_{t}$, ) for the data given in Table 3.3, taken from Frets (1921).
3.2. (Sec.3.2) Verify the numerical results of (21).
3.3. (Sec.3.2) Compute $\hat{\mu}, \hat{\Sigma}, S$, and $\hat{\rho}$ for the following pairs of observations: $(34,55),(12,29),(33,75),(44,89),(89,62),(59,69),(50,41),(88,67)$. Plot the observations.
3.4. (Sec. 3.2) Use the facts that $\left|\boldsymbol{C}^{*}\right|=\Pi \lambda_{1}, \operatorname{tr} \boldsymbol{C}^{*}=\sum \lambda_{1}$, and $\boldsymbol{C}^{*}=I$ if $\lambda_{1}=\cdots =\lambda_{p}=1$, where $\lambda_{1}, \ldots, \lambda_{p}$ are the characteristic roots of $C^{*}$, to prove Lemma 3.2.2. [Hint: Use $f$ as given in (12).]

Table 3.3 ${ }^{\dagger}$. Head Lengths and Breadths of Brothers
| Head Length, First Son, $x_{1}$ | Head Breadth, First Son, $x_{2}$ | Head Length, Second Son, $x_{3}$ | Head Breadth, Second Son, $x_{4}$ |
| :--- | :--- | :--- | :--- |
|  |  |  |  |
| 191 | 155 | 179 | 145 |
| 195 | 149 | 201 | 152 |
| 181 | 148 | 185 | 149 |
| 183 | 153 | 188 | 149 |
| 176 | 144 | 171 | 142 |
| 208 | 157 | 192 | 152 |
| 189 | 150 | 190 | 149 |
| 197 | 159 | 189 | 152 |
| 188 | 152 | 197 | 159 |
| 192 | 150 | 187 | 151 |
| 179 | 158 | 186 | 148 |
| 183 | 147 | 174 | 147 |
| 174 | 150 | 185 | 152 |
| 190 | 159 | 195 | 157 |
| 188 | 151 | 187 | 158 |
| 163 | $13^{\prime \prime}$ | 161 | 130 |
| 195 | 155 | 183 | 158 |
| 186 | 153 | 173 | 148 |
| 181 | 145 | 182 | 146 |
| 175 | 140 | 165 | 137 |
| 192 | 154 | 185 | 152 |
| 174 | 143 | 178 | 147 |
| 176 | 139 | 176 | 143 |
| 197 | 167 | 200 | 158 |
| 190 | 163 | 187 | 150 |


${ }^{\dagger}$ These data, used in examples in the first edition of this book, came from Rao (1952), p. 245. Izenman (1980) has indicated some entries were apparently incorrectly copied from Frets (1921) and corrected them (p. 579).
3.5. (Sec. 3.2) Let $x_{1}$ be the body weight (in kilograms) of a cat and $x_{2}$ the heart weight (in grams). [Data from Fisher (1947b).]
(a) In a sample of 47 female cats the relevant data are

$$
\sum x_{\alpha}=\binom{110.9}{432.5}, \quad \sum x_{\alpha} x_{\alpha}^{\prime}=\left(\begin{array}{rr}
265.13 & 1029.62 \\
1029.62 & 4064.71
\end{array}\right) .
$$

Find $\hat{\mu}, \hat{\Sigma}, S$, and $\hat{\rho}$.

Table 3.4. Four Measurements on Three Species of Iris (in centimeters)
| In's setosa |  |  |  | Iris versicolor |  |  |  | Iris virginica |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sepal length | Sepal width | Petal length | Petal width | Sepal length | Sepal width | Petal length | Petal width | Sepal length | Sepal width | Petal length | Petal width |
| 5.1 | 3.5 | 1.4 | 0.2 | 7.0 | 3.2 | 4.7 | 1.4 | 6.3 | 3.3 | 6.0 | 2.5 |
| 4.9 | 3.0 | 1.4 | 0.2 | 6.4 | 3.2 | 4.5 | 1.5 | 5.8 | 2.7 | 5.1 | 1.9 |
| 4.7 | 3.2 | 1.3 | 0.2 | 6.9 | 3.1 | 4.9 | 1.5 | 7.1 | 3.0 | 5.9 | 2.1 |
| 4.6 | 3.1 | 1.5 | 0.2 | 5.5 | 2.3 | 4.0 | 1.3 | 6.3 | 2.9 | 5.6 | 1.8 |
| 5.0 | 3.6 | 1.4 | 0.2 | 6.5 | 2.8 | 4.6 | 1.5 | 6.5 | 3.0 | 5.8 | 2.2 |
| 5.4 | 3.9 | 1.7 | 0.4 | 5.7 | 2.8 | 4.5 | 1.3 | 7.6 | 3.0 | 6.6 | 2.1 |
| 4.6 | 3.4 | 1.4 | 0.3 | 6.3 | 3.3 | 4.7 | 1.6 | 4.9 | 2.5 | 4.5 | 1.7 |
| 5.0 | 3.4 | 1.5 | 0.2 | 4.9 | 2.4 | 3.3 | 1.0 | 7.3 | 2.9 | 6.3 | 1.8 |
| 4.4 | 2.9 | 1.4 | 0.2 | 6.6 | 2.9 | 4.6 | 1.3 | 6.7 | 2.5 | 5.8 | 1.8 |
| 4.9 | 3.1 | 1.5 | 0.1 | 5.2 | 2.7 | 3.9 | 1.4 | 7.2 | 3.6 | 6.1 | 2.5 |
| 5.4 | 3.7 | 1.5 | 0.2 | 5.0 | 2.0 | 3.5 | 1.0 | 6.5 | 3.2 | 5.1 | 2.0 |
| 4.8 | 3.4 | 1.6 | 0.2 | 5.9 | 3.0 | 4.2 | 1.5 | 6.4 | 2.7 | 5.3 | 1.9 |
| 4.8 | 3.0 | 1.4 | 0.1 | 6.0 | 2.2 | 4.0 | 1.0 | 6.8 | 3.0 | 5.5 | 2.1 |
| 4.3 | 3.0 | 1.1 | 0.1 | 6.1 | 2.9 | 4.7 | 1.4 | 5.7 | 2.5 | 5.0 | 2.0 |
| 5.8 | 4.0 | 1.2 | 0.2 | 5.6 | 2.9 | 3.6 | 1.3 | 5.8 | 2.8 | 5.1 | 2.4 |
| 5.7 | 4.4 | 1.5 | 0.4 | 6.7 | 3.1 | 4.4 | 1.4 | 6.4 | 3.2 | 5.3 | 2.3 |
| 5.4 | 3.9 | 1.3 | 0.4 | 5.6 | 3.0 | 4.5 | 1.5 | 6.5 | 3.0 | 5.5 | 1.8 |
| 5.1 | 3,5 | 1.4 | 0.3 | 5.8 | 2.7 | 4.1 | 1.0 | 7.7 | 3.8 | 6.7 | 2.2 |
| 5.7 | 3.8 | 1.7 | 0.3 | 6.2 | 2,2 | 4.5 | 1.5 | 7.7 | 2.6 | 6.9 | 2.3 |
| 5.1 | 3.8 | 1.5 | 0.3 | 5.6 | 2,5 | 3.9 | 1.1 | 6.0 | 2.2 | 5.0 | 1.5 |
| 5.4 | 3.4 | 1.7 | 0.2 | 5.9 | 3.2 | 4.8 | 1.8 | 6.9 | 3.2 | 5.7 | 2.3 |
| 5.1 | 3.7 | 1.5 | 0.4 | 6.1 | 2.8 | 4.0 | 1.3 | 5.6 | 2.8 | 4.9 | 2.0 |
| 4,6 | 3.6 | 1.0 | 0.2 | 6,3 | 2.5 | 4.9 | 1.5 | 7.7 | 2.8 | 6.7 | 2.0 |
| 5.1 | 3.3 | 1.7 | 0.5 | 6.1 | 2.8 | 4.7 | 1,2 | 6.3 | 2.7 | 4.9 | 1.8 |
| 4.8 | 3.4 | 1.9 | 0.2 | 6.4 | 2.9 | 4.3 | 1.3 | 6.7 | 3.3 | 5.7 | 2.1 |
| 5.0 | 3.0 | 1.6 | 0.2 | 6.6 | 3.0 | 4.4 | 1.4 | 7.2 | 3.2 | 6.0 | 1.8 |
| 5.0 | 3.4 | 1.6 | 0.4 | 6.8 | 2.8 | 4.8 | 1.4 | 6.2 | 2.8 | 4.8 | 1.8 |
| 5.2 | 3.5 | 1.5 | 0.2 | 6.7 | 3.0 | 5.0 | 1.7 | 6.1 | 3.0 | 4.9 | 1.8 |
| 5.2 | 3.4 | 1.4 | 0.2 | 6.0 | 2.9 | 4.5 | 1.5 | 6.4 | 2.8 | 5.6 | 2.1 |
| 4.7 | 3.2 | 1.6 | 0.2 | 5.7 | 2.6 | 3.5 | 1,0 | 7.2 | 3.0 | 5.8 | 1.6 |
| 4.8 | 3.1 | 1.6 | 0.2 | 5.5 | 2.4 | 3.8 | 1.1 | 7.4 | 2.8 | 6.1 | 1.9 |
| 5.4 | 3.4 | 1.5 | 0.4 | 5.5 | 2,4 | 3.7 | 1.0 | 7.9 | 3.8 | 6.4 | 2.0 |
| 5.2 | 4.1 | 1.5 | 0.1 | 5.8 | 2.7 | 3.9 | 1,2 | 6.4 | 2.8 | 5.6 | 2.2 |
| 5.5 | 4.2 | 1,4 | 0.2 | 6.0 | 2.7 | 5.1 | 1.6 | 6.3 | 2.8 | 5.1 | 1.5 |
| 4.9 | 3.1 | 1.5 | 0.2 | 5.4 | 3.0 | 4.5 | 1.5 | 6.1 | 2.6 | 5.6 | 1.4 |
| 5.0 | 3.2 | 1.2 | 0.2 | 6.0 | 3.4 | 4.5 | 1.6 | 7.7 | 3.0 | 6.1 | 2.3 |
| 5,5 | 3.5 | 1.3 | 0.2 | 6.7 | 3.1 | 4.7 | 1.5 | 6.3 | 3.4 | 5.6 | 2.4 |
| 4.9 | 3.6 | 1.4 | 0.1 | 6.3 | 2.3 | 4.4 | 1.3 | 6.4 | 3.1 | 5.5 | 1.8 |
| 4.4 | 3.0 | 1.3 | 0.2 | 5.6 | 3.0 | 4.1 | 1.3 | 6.0 | 3.0 | 4.8 | 1.8 |
| 5.1 | 3.4 | 1.5 | 0.2 | 5.5 | 2.5 | 4.0 | 1.3 | 6.9 | 3.1 | 5.4 | 2.1 |


Table 3.4. (Continued)
| Iris setosa |  |  |  | Iris versicolor |  |  |  | Iris virginica |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sepal length | Sepal width | Petal length | Petal width | Sepal length | Sepal width | Petal length | Petal width | Sepal length | Sepal width | Petal length | Petal width |
| 5.0 | 3.5 | 1.3 | 0.3 | 5.5 | 2.6 | 4.4 | 1.2 | 6.7 | 3.1 | 5.6 | 2.4 |
| 4.5 | 2.3 | 1,3 | 0.3 | 6.1 | 3.0 | 4.6 | 1.4 | 6.9 | 3.1 | 5.1 | 2.3 |
| 4.4 | 3.2 | 1.3 | 0.2 | 5.8 | 2.6 | 4.0 | 1.2 | 5.8 | 2.7 | 5.1 | 1.9 |
| 5.0 | 3.5 | 1.6 | 0.6 | 5.0 | 2.3 | 3.3 | 1.0 | 6.8 | 3.2 | 5.9 | 2.3 |
| 5.1 | 3.8 | 1.9 | 0.4 | 5.6 | 2.7 | 4.2 | 1.3 | 6.7 | 3.3 | 5.7 | 2.5 |
| 4.8 | 3.0 | 1.4 | 0.3 | 5.7 | 3.0 | 4.2 | 1.2 | 6.7 | 3.0 | 5.2 | 2.3 |
| 5.1 | 3.8 | 1.6 | 0.2 | 5.7 | 2.9 | 4.2 | 1.3 | 6.3 | 2.5 | 5.0 | 1.9 |
| 4.6 | 3.2 | 1.4 | 0.2 | 6.2 | 2.9 | 4.3 | 1.3 | 6.5 | 3.0 | 5.2 | 2.0 |
| 5.3 | 3.7 | 1.5 | 0.2 | 5.1 | 2.5 | 3.0 | 1.1 | 6.2 | 3.4 | 5.4 | 2.3 |
| 5.0 | 3.3 | 1.4 | 0.2 | 5.7 | 2.8 | 4.1 | 1.3 | 5.9 | 3.0 | 5.1 | 1.8 |


(b) In a sample of 97 male cats the relevant data are

$$
\sum x_{a}=\binom{281.3}{1098.3}, \quad \sum x_{\alpha} x_{a}^{\prime}=\left(\begin{array}{rr}
836.75 & 3275.55 \\
3275.55 & 13056.17
\end{array}\right) .
$$

Find $\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\Sigma}}, S$, and $\hat{\boldsymbol{\rho}}$.
3.6. Find $\hat{\boldsymbol{\mu}}, \overline{\boldsymbol{\Sigma}}$, and ( $\hat{\rho}_{i j}$ ) for Iris setosa from Table 3.4, taken from Edgar Anderson's famous iris data [Fisher (1936)].
3.7. (Sec. 3.2) Invariance of the sample correlation coefficient. Prove that $r_{12}$ is an invariant characteristic of the sufficient statistics $\bar{x}$ and $S$ of a bivariate sample under location and scale transformations ( $x_{i \alpha}^{*}=b_{i} x_{i \alpha}+c_{i}, b_{l}>0, i=1,2, \alpha= 1, \ldots, N$ ) and that every function of $\bar{x}$ and $S$ that is invariant is a function of $\boldsymbol{r}_{12}$. [Hint: See Theorem 2.3.2.]
3.8. (Sec. 3.2) Prove Lemma 3.2 .2 by induction. [Hint: Let $\boldsymbol{H}_{1}=h_{11}$,

$$
\boldsymbol{H}_{i}=\left(\begin{array}{cc}
\boldsymbol{H}_{1-1} & \boldsymbol{h}_{(1)} \\
\boldsymbol{h}_{(1)}^{\prime} & h_{i i}
\end{array}\right), \quad i=2, \ldots, p,
$$

and use Problem 2.36.]
3.9. (Sec. 2.2) Show that

$$
\frac{1}{N(N-1)} \sum_{\alpha<\beta}\left(x_{\alpha}-x_{\beta}\right)\left(x_{\alpha}-x_{\beta}\right)^{\prime}=\frac{1}{N-1} \sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime} .
$$

(Note: When $p=1$, the left-hand side is the average squared differences of the observations.)
3.10. (Sec. 3.2) Estimation of $\Sigma$ when $\mu$ is known. Show that if $x_{1}, \ldots, x_{N}$ constitute a sample from $N(\mu, \Sigma)$ and $\mu$ is known, then $(1 / N) \Sigma_{\alpha=1}^{N}\left(x_{\alpha}-\mu\right)\left(x_{\alpha}-\mu\right)^{\prime}$ is the maximum likelihood estimator of $\mathbf{\Sigma}$.
3.11. (Sec. 3.2) Estimation of parameters of a complex normal distribution. Let $z_{1}, \ldots, z_{N}$ be $N$ observations from the complex normal distributions with mean $\boldsymbol{\theta}$ and covariance matrix $\boldsymbol{P}$. (See Problem 2.64.)
(a) Show that the maximum likelihood estimators of $\boldsymbol{\theta}$ and $\boldsymbol{P}$ are

$$
\hat{\boldsymbol{\theta}}=\bar{z}=\frac{1}{N} \sum_{\alpha=1}^{N} z_{\alpha}, \quad \hat{\boldsymbol{P}}=\frac{1}{N} \sum_{\alpha=1}^{N}\left(z_{\alpha}-\bar{z}\right)\left(z_{\alpha}-\bar{z}\right)^{*} .
$$

(b) Show that $\bar{z}$ has the complex normal distribution with mean $\boldsymbol{\theta}$ and covariance matrix $(1 / N) \boldsymbol{P}$.
(c) Show that $\bar{z}$ and $\hat{P}$ are independently distributed and that $N \hat{P}$ has the distribution of $\sum_{\alpha=1}^{n} W_{\alpha} W_{\alpha}^{*}$, where $W_{1}, \ldots, W_{n}$ are independently distributed, each according to the complex normal distribution with mean $\mathbf{0}$ and covariance matrix $P$, and $n=N-1$.
3.12. (Sec. 3.2) Prove Lemma 3.2.2 by using Lemma 3.2.3 and showing $N \log |\boldsymbol{C}|-$ tr $C D$ has a maximum at $C=N D^{-1}$ by setting the derivatives of this function with respect to the elements of $\boldsymbol{C}=\boldsymbol{\Sigma}^{-1}$ equal to 0 . Show that the function of $\boldsymbol{C}$ tends to $-\infty$ as $\boldsymbol{C}$ tends to a singular matrix or as one or more elements of $\boldsymbol{C}$ tend to $\infty$ and/or $-\infty$ (nondiagonal elements); for this latter, the equivalent of (13) can be used.
3.13. (Sec. 3.3) Let $X_{\alpha}$ be distributed according to $N\left(\gamma c_{\alpha}, \Sigma\right), \alpha=1, \ldots, N$, where $\Sigma c_{\alpha}^{2}>0$. Show that the distribution of $g=\left(1 / \Sigma c_{\alpha}^{2}\right) \Sigma c_{\alpha} X_{\alpha}$ is $N\left[\gamma,\left(1 / \Sigma c_{\alpha}^{2}\right) \Sigma\right]$. Show that $E=\sum_{\alpha}\left(X_{\alpha}-g c_{\alpha}\right)\left(X_{\alpha}-g c_{\alpha}\right)^{\prime}$ is independently distributed as $\sum_{\alpha=1}^{N-1} Z_{\alpha} Z_{\alpha}^{\prime}$, where $Z_{1}, \ldots, Z_{N}$ are independent, each with distribution $N(\mathbf{0}, \Sigma)$. [Hint: Let $Z_{\alpha}=\sum b_{\alpha \beta} X_{\beta}$, where $b_{N \beta}=c_{\beta} / \sqrt{\sum c_{\alpha}^{2}}$ and $B$ is orthogonal.]
3.14. (Sec. 3.3) Prove that the power of the test in (19) is a function only of $p$ and $\left[N_{1} N_{2} /\left(N_{1}+N_{2}\right)\right]\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)$, given $\boldsymbol{\alpha}$.
3.15. (Sec. 3.3) Efficiency of the mean. Prove that $\bar{x}$ is efficient for estimating $\mu$.
3.16. (Sec. 3.3) Prove that $\tilde{x}$ and $S$ have efficiency $[(N-1) / N]^{p(p+1) / 2}$ for estimating $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$.
3.17. (Sec. 3.2) Prove that $\operatorname{Pr}\{|A|=0\}=0$ for $A$ defined by (4) when $N>p$. [Hint: Argue that if $\mathbf{Z}_{p}^{*}=\left(\mathbf{Z}_{1}, \ldots, \mathbf{Z}_{p}\right)$, then $\left|\mathbf{Z}_{,}^{*}\right| \neq 0$ implies $A=\mathbf{Z}_{p}^{*} Z_{p}^{* \prime}+ \sum_{\alpha-j+1}^{N-1} Z_{\alpha} Z_{\alpha}^{\prime}$ is positive definite. Prove $\operatorname{Pr}\left\{\left|Z_{j}^{*}\right|=Z_{j j}\left|Z_{j-1}^{*}\right|+\sum_{i=1}^{j-1} Z_{i j} \operatorname{cof}\left(Z_{i j}\right)\right. =0\}=0$ by induction, $j=2, \ldots, p$.]



3.18. (Sec. 3.4) Prove

$$
\begin{gathered}
I-\boldsymbol{\Phi}(\boldsymbol{\Phi}+\boldsymbol{\Sigma})^{-1}=\boldsymbol{\Sigma}(\boldsymbol{\Phi}+\boldsymbol{\Sigma})^{-1} . \\
\boldsymbol{\Phi}-\boldsymbol{\Phi}(\boldsymbol{\Phi}+\boldsymbol{\Sigma})^{-1} \mathbf{\Phi}=\left(\boldsymbol{\Phi}^{-1}+\boldsymbol{\Sigma}^{-1}\right)^{-1} .
\end{gathered}
$$

3.19. (Sec. 3.4) Prove $(1 / N) \sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu\right)\left(x_{\alpha}-\mu\right)^{\prime}$ is an unbiased estimator of $\Sigma$ when $\mu$ is known.
3.20. (Sec. 3.4) Show that

$$
\boldsymbol{\Phi}\left(\boldsymbol{\Phi}+\frac{1}{N} \boldsymbol{\Sigma}\right)^{-1} \boldsymbol{x}+\frac{1}{N} \boldsymbol{\Sigma}\left(\boldsymbol{\Phi}+\frac{1}{N} \boldsymbol{\Sigma}\right)^{-1} \boldsymbol{\nu}=\left(\boldsymbol{\Phi}^{-1}+N \boldsymbol{\Sigma}^{-1}\right)^{-1}\left(N \boldsymbol{\Sigma}^{-1} \boldsymbol{x}+\boldsymbol{\Phi}^{-1} \boldsymbol{\nu}\right)
$$

3.21. (Sec. 3.5) Demonstrate Lemma 3.5.1 using integration by parts.
3.22. (Sec. 3.5) Show that

$$
\begin{aligned}
& \int_{\theta}^{\infty} \int_{y}^{\infty}\left|f^{\prime}(y)(x-\theta) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(x-\theta)^{\prime}}\right| d x d y=\int_{0}^{\infty}\left|f^{\prime}(y)\right| \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2}(y-\theta)^{\prime}} d y \\
& \int_{-\infty}^{\theta} \int_{-\infty}^{y}\left|f^{\prime}(y)(\theta-x) \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{y}(1-\theta)^{2}}\right| d x d y=\int_{-\infty}^{\theta}\left|f^{\prime}(y)\right| \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{y}(1-\theta)^{2}} d y
\end{aligned}
$$

3.23. Let $Z(k)=\left(Z_{i j}(k)\right)$, where $i=1, \ldots, p, j=1 \ldots, q$ and $k=1.2 \ldots$ be a sequence of random matrices. Let one norm of a matrix $A$ be $N_{1}(A)= \max _{i,}, \bmod \left(a_{i j}\right)$, and anothcr be $N_{2}(A)=\sum_{1,} a_{i j}^{2}=\operatorname{tr} A A^{\prime}$. Some alternative ways of defining stochastic convergence of $Z(k)$ to $B(p \times q)$ are
(a) $N_{1}(Z(k)-B)$ converges stochastically to 0 .
(b) $N_{2}(Z(k)-B)$ converges stochastically to 0 , and
(c) $Z_{i j}(k)-b_{i j}$ converges stochastically to $0, i=1, \ldots, p, j=1, \ldots q$.

Prove that these three definitions are equivalent. Note that the definition of $X(k)$ converging stochastically to $a$ is that lor every arbilrary positive $\delta$ and $\varepsilon$. we can find $K$ large enough so that for $k>K$

$$
\operatorname{Pr}\{|X(k)-a|<\delta\}>1-\varepsilon .
$$

3.24. (Sec. 3.2) Covariance matrices with linear structure [Anderson (1969)]. Let
(i)

$$
\Sigma=\sum_{\mathfrak{b}=11}^{q} \sigma_{\mathfrak{b}} G_{g},
$$

where $\boldsymbol{G}_{0}, \ldots, \boldsymbol{G}_{q}$ are given symmetric matrices such that there exists at least one $(q+1)$-tuplet $\sigma_{0}, \sigma_{1}, \ldots, \sigma_{q}$ such that (i) is positive definite. Show that the likelihood equations based on $N$ observations are
(ii) $\quad-\frac{N}{2} \operatorname{tr} \Sigma^{-1} G_{g}+\frac{1}{2} \operatorname{tr} A \Sigma^{-1} G_{g} \Sigma^{-1}=0, \quad g=0,1, \ldots, q$.

Show that an iterative (scoring) method can be based on
(iii) $\quad \sum_{h=0}^{q} \operatorname{tr} \hat{\Sigma}_{i-1}^{-1} G_{g} \hat{\Sigma}_{i-1}^{-1} G_{h} \hat{\sigma}_{h}^{(i)}=\frac{1}{N} \operatorname{tr} \hat{\Sigma}_{i-1}^{-1} G_{g} \hat{\Sigma}_{i-1}^{-1} A, \quad g=0,1, \ldots, q$, where $\hat{\Sigma}_{i-1} \Sigma_{g-0}^{q} \hat{\sigma}_{g}^{(i-1)} G_{g}$.

## The Distributions and Uses of Sample Correlation Coefficients

### 4.1. INTRODUCTION

In Chapter 2, in which the multivariate normal distribution was introduced, it was shown that a measure of dependence between two normal variates is the correlation coefficient $\rho_{i j}=\sigma_{i j} / \sqrt{\sigma_{i i} \sigma_{j j}}$. In a conditional distribution of $X_{1}, \ldots, X_{q}$ given $X_{q+1}=x_{q+1}, \ldots, X_{p}=x_{p}$, the partial correlation $\rho_{i j \cdot q+1, \ldots, p}$ measures the dependence between $X_{i}$ and $X_{j}$. The third kind of correlation discussed was the multiple correlation which measures the relationship between one variate and a set of others. In this chapter we treat the sample equivalents of these quantities; they are point estimates of the population quantities. The distributions of the sample correlations are found. Tests of hypotheses and confidence intervas are developed,

In the cases of joint normal distributions these correlation coefficients are the natural measures of dependence. In the population they are the only parameters except for location (means) and scale (standard deviations) parameters. In the sample the correlation coefficients are derived as the reasonable estimates of the population correlations. Since the sample means and standard deviations are location and scale estimates, the sample correlations (that is, the standardized sample second moments) give all possible information about the population correlations. The sample correlations are the functions of the sufficient statistics that are invariant with respect to location and scale transformations; the population correlations are the functions of the parameters that are invariant with respect to these transformations.

[^0]In regression theory or least squares, one variable is considered random or dependent, and the others fixed or independent. In correlation theory we consider several variables as random and treat them symmetrically. If we start with a joint normal distribution and hold all variables fixed except one, we obtain the least squares model because the expected value of the random variable in the conditional distribution is a linear function of the variables held fixed. The sample regression coefficients obtained in least squares are functions of the sample variances and correlations.

In testing independence we shall see that we arrive at the same tests in either casc (i.e., in the joint normal distribution or in the conditional distribution of least squares). The probability theory under the null hypothesis is the same. The distribution of the test criterion when the null hypothesis is not true differs in the two cases. If all variables may be considered random, one uses correlation theory as given here; if only one variable is random, one uses least squares theory (which is considered in some generality in Chapter 8).

In Section 4.2 we derive the distribution of the sample correlation coefficient, first when the corresponding population correlation coefficient is 0 (the two normal variables being independent) and then for any value of the population coefficient. The Fisher $z$-transform yields a useful approximate normal distribution. Exact and approximate confidence intervals are developed. In Section 4.3 we carry out the same program for partial correlations, that is, correlations in conditional normal distributions. In Section 4.4 the distributions and other properties of the sample multiple correlation coefficient are studied. In Section 4.5 the asymptotic distributions of these correlations are derived for elliptically contoured distributions. A stochastic representation for a class of such distributions is found.

### 4.2. CORRELATION COEFFICIENT OF A BIVARIATE SAMPLE

### 4.2.1. The Distribution When the Population Correlation Coefficient Is Zero; Tests of the Hypothesis of Lack of Correlation

In Section 3.2 it was shown that if one has a sanple (of $p$-component vectors) $x_{1}, \ldots, x_{N}$ from a normal distribution, the maximum likelihood estimator of the correlation between $X_{1}$ and $X_{j}$ (two components of the random vector $X$ ) is

$$
r_{i j}=\frac{\sum_{a=1}^{N}\left(x_{i \alpha}-\bar{x}_{i}\right)\left(x_{j \alpha}-\bar{x}_{j}\right)}{\sqrt{\sum_{\alpha=1}^{N}\left(x_{i \alpha}-\bar{x}_{j}\right)^{2}} \sqrt{\sum_{\alpha=1}^{N}\left(x_{j \alpha}-\bar{x}_{j}\right)^{2}}},
$$

where $x_{i \alpha}$ is the $i$ th component of $x_{\alpha}$ and

$$
\tilde{x}_{\imath}=\frac{1}{N} \sum_{\alpha=1}^{N} x_{\imath \alpha}
$$

In this section we shall find the distribution of $r_{i j}$ when the population correlation between $X_{i}$ and $X_{j}$ is zero, and we shall see how to use the sample correlation coefficient to test the hypothesis that the population coefficient is zero.

For convenience we shall treat $r_{12}$; the same theory holds for each $r_{i j}$. Since $r_{12}$ depends only on the first two coordinates of each $x_{\alpha}$, to find the distribution of $r_{12}$ we need only consider the joint distribution of ( $x_{11}, x_{21}$ ), $\left(x_{12}, x_{22}\right), \ldots,\left(x_{1 N}, x_{2 N}\right)$. We can reformulate the problems to be considered here, therefore, in terms of a bivariate normal distribution. Let $x_{1}^{*}, \ldots, x_{N}^{*}$ be observation vectors from

$$
N\left[\binom{\mu_{l}}{\mu_{2}},\left(\begin{array}{cc}
\sigma_{1}^{2} & \sigma_{l} \sigma_{2} \rho \\
\sigma_{2} \sigma_{1} \rho & \sigma_{2}^{2}
\end{array}\right)\right] .
$$

We shall consider

$$
r=\frac{a_{12}}{\sqrt{a_{11}} \sqrt{a_{22}}},
$$

where

$$
a_{i j}=\sum_{\alpha=1}^{N}\left(x_{i \alpha}-\bar{x}_{i}\right)\left(x_{j \alpha}-\bar{x}_{l}\right), \quad \quad i . j=1,2 .
$$

and $\bar{x}_{i}$ is defined by (2), $x_{i_{0}}$ being the $i$ th component of $x_{\alpha}^{*}$.
From Section 3.3 we see that $a_{11}, a_{12}$, and $a_{22}$ are distributed like

$$
a_{i j}=\sum_{\alpha=1}^{n} z_{r \alpha} z_{j \alpha}, \quad i . j=1,2,
$$

where $n=N-1,\left(z_{1 \alpha}, z_{2 \alpha}\right)$ is distributed according to

$$
N\left[\binom{0}{0},\left(\begin{array}{cc}
\sigma_{1}^{2} & \sigma_{1} \sigma_{2} \rho \\
\sigma_{2} \sigma_{1} \rho & \sigma_{2}^{2}
\end{array}\right)\right],
$$

and the pairs $\left(z_{11}, z_{21}\right), \ldots,\left(z_{1 N}, z_{2 N}\right)$ are independently distributed.

![](https://cdn.mathpix.com/cropped/fea3fe5c-7211-45a5-bbc6-e1625dffa6eb-136.jpg?height=552&width=741&top_left_y=228&top_left_x=433)
Figure 4.1

Define the $n$-component vector $v_{t}=\left(z_{t 1}, \ldots, z_{i n}\right)^{\prime}, i=1,2$. These two vectors can be represented in an $n$-dimensional space; see Figure 4.1. The correlation coefficient is the cosine of the angle, say $\theta$, between $v_{1}$ and $v_{2}$. (See Section 3.2.) To find the distribution of $\cos \theta$ we shall first find the distribution of $\cot \theta$. As shown in Section 3.2, if we let $b=v_{2}^{\prime} v_{1} / v_{1}^{\prime} v_{1}$, then $v_{2}-b v_{1}$ is orthogonal to $v_{1}$ and

$$
\cot \theta=\frac{b\left\|v_{1}\right\|}{\left\|v_{2}-b v_{1}\right\|}
$$

If $v_{1}$ is fixed, we can rotate coordinate axes so that the first coordinate axis lies along $v_{1}$. Then $b v_{1}$ has only the first coordinate different from zero, and $\boldsymbol{v}_{2}-b \boldsymbol{v}_{1}$ has this first coordinate equal to zero. We shall show that $\cot \theta$ is proportional to a $t$-variable when $\rho=0$.

We use the following lemma.
Lemma 4.2.1. If $Y_{1}, \ldots, Y_{n}$ are independently distributed, if $Y_{\alpha}=\left(Y_{\alpha}^{(1) \prime}, Y_{\alpha}^{(2) \prime}\right)$ has the density $f\left(y_{\alpha}\right)$, and if the conditional density of $Y_{\alpha}^{(2)}$ given $Y_{\alpha}^{(1)}=y_{\alpha}^{(1)}$ is $f\left(y_{\alpha}^{(2)} \mid y_{\alpha}^{(1)}\right), \alpha=1, \ldots, n$. then in the conditional distribution of $Y_{1}^{(2)}, \ldots, Y_{n}^{(2)}$ given $Y_{1}^{(1)}=y_{1}^{(1)}, \ldots, y_{n}^{(1)}=y_{n}^{(1)}$, the random vectors $Y_{1}^{(2)}, \ldots, Y_{n}^{(2)}$ are independent and the density of $Y_{\alpha}^{(2)}$ is $f\left(y_{\alpha}^{(2)} \mid y_{\alpha}^{(1)}\right), \alpha=1, \ldots, n$.

Proof. The marginal density of $Y_{1}^{(1)} \ldots, Y_{n}^{(1)}$ is $\Pi_{\alpha=1}^{n} f_{1}\left(y_{\alpha}^{(1)}\right)$, where $f_{1}\left(y_{\alpha}^{(1)}\right)$ is the marginal density of $Y_{\alpha}^{(1)}$, and the conditional density of $Y_{1}^{(2)}, \ldots, Y_{n}^{(2)}$ given $Y_{1}^{(1)}=y_{1}^{(1)}, \ldots, Y_{n}^{(1)}=y_{n}^{(1)}$ is

$$
\frac{\prod_{\alpha=1}^{n} f\left(y_{\alpha}\right)}{\prod_{\alpha=1}^{n} f_{1}\left(y_{\alpha}^{(1)}\right)}=\prod_{\alpha=1}^{n} \frac{f\left(y_{\alpha}\right)}{f_{1}\left(y_{\alpha}^{(1)}\right)}=\prod_{\alpha=1}^{n} f\left(y_{\alpha}^{(2)} \mid y_{\alpha}^{(1)}\right) .
$$

Write $V_{i}=\left(Z_{i 1}, \ldots, Z_{i n}\right)^{\prime}, i=1,2$, to denote random vectors. The conditional distribution of $Z_{2 \alpha}$ given $Z_{1 \alpha}=z_{1 \alpha}$ is $N\left(\beta z_{1 \alpha}, \sigma^{2}\right)$, where $\beta=\rho \sigma_{2} / \sigma_{1}$ and $\sigma^{2}=\sigma_{2}^{2}\left(1-\rho^{2}\right)$. (See Section 2.5.) The density of $V_{2}$ given $V_{1}=v_{1}$ is $N\left(\beta v_{1}, \sigma^{2} I\right)$ since the $Z_{2 a}$ are independent. Let $b=V_{2}^{\prime} v_{i} / v_{1}^{\prime} v_{1}\left(=a_{21} / a_{11}\right)$, so that $b v_{1}^{\prime}\left(\boldsymbol{V}_{2}-b v_{1}\right)=0$, and let $U=\left(\boldsymbol{V}_{2}-b v_{1}\right)^{\prime}\left(\boldsymbol{V}_{2}-b v_{1}\right)=\boldsymbol{V}_{2}^{\prime} \boldsymbol{V}_{2}-b^{2} v_{1}^{\prime} v_{1}$ ( $=a_{22}-a_{12}^{2} / a_{11}$ ). Then $\cot \theta=b \sqrt{a_{11} / U}$. The rotation of coordinate axes involves choosing an $n \times n$ orthogonal matrix $C$ with first row $(1 / c) v_{1}^{\prime}$, where $c^{2}=\nu_{1}^{\prime} \nu_{1}$.

We now apply Theorem 3.3.1 with $X_{\alpha}=Z_{2 \alpha}$. Let $Y_{\alpha}=\sum_{\beta} c_{\alpha \beta} Z_{2 \beta}, \alpha= 1, \ldots, n$. Then $Y_{1}, \ldots, Y_{n}$ are independently normally distributed with variance $\sigma^{2}$ and means

$$
\begin{array}{ll}
\mathscr{E} Y_{1}=\sum_{\gamma=1}^{n} c_{1 \gamma} \beta z_{1 \gamma}=\frac{\beta}{c} \sum_{\gamma=1}^{n} z_{1 \gamma}^{2}=\beta c, & \\
\mathscr{E} Y_{\alpha}=\sum_{\gamma=1}^{n} c_{\alpha \gamma} \beta z_{1 \gamma}=\beta c \sum_{\gamma=1}^{n} c_{\alpha \gamma} c_{1 \gamma}=0, & \alpha \neq 1
\end{array}
$$

We have $b=\sum_{\text {ne }=1}^{n} Z_{2 \text { n } z_{1 \alpha}} / \sum_{\text {α }=1}^{n} z_{1 \alpha}^{2}=c \sum_{\alpha=1}^{n} Z_{2 \alpha} c_{1 \alpha} / c^{2}=Y_{1} / c$ and, from Lemma 3.3.1,

$$
\begin{aligned}
U & =\sum_{\alpha=1}^{n} Z_{2 \alpha}^{2}-b^{2} \sum_{\alpha=1}^{n} z_{1 \alpha}^{2}=\sum_{\alpha=1}^{n} Y_{\alpha}^{2}-Y_{1}^{2} \\
& =\sum_{\alpha=2}^{n} Y_{\alpha}^{2}
\end{aligned}
$$

which is independent of $b$. Then $U / \sigma^{2}$ has a $\chi^{2}$-distribution with $n-1$ degrees of freedom.

Lemma 4.2.2. If $\left(Z_{1 \alpha}, Z_{2 \alpha}\right), \alpha=1, \ldots, n$, are independent, each pair with density (7), then the conditional distributions of $b=\sum_{\alpha=1}^{n} Z_{2 \alpha} Z_{1 \alpha} / \sum_{\alpha=1}^{n} Z_{1 \alpha}^{2}$ and $U / \sigma^{2}=\sum_{a=1}^{n}\left(Z_{2 \alpha}-b Z_{1 \alpha}\right)^{2} / \sigma^{2}$ given $Z_{1 \alpha}=z_{1 \alpha}, \alpha=1, \ldots, n$, are $N\left(\beta, \sigma^{2} / c^{2}\right)\left(c^{2}=\sum_{\alpha=1}^{n} z_{1 \alpha}^{2}\right)$ and $\chi^{2}$ with $n-1$ degrees of freedom, respectively; and $b$ and $U$ are independent.

If $\rho=0$, then $\beta=0$, and $b$ is distributed conditionally according to $N\left(0, \sigma^{2} / c^{2}\right)$, and

$$
\frac{c b / \sigma}{\sqrt{\frac{U / \sigma^{2}}{n-1}}}=\frac{c b}{\sqrt{\frac{U}{n-1}}}
$$

has a conditional $t$-distribution with $n-1$ degrees of freedom. (See Problem 4.27.) However, this random variable is

$$
\begin{aligned}
\sqrt{n-1} \frac{\sqrt{a_{11}} a_{12} / a_{11}}{\sqrt{a_{22}-a_{12}^{2} / a_{11}}} & =\sqrt{n-1} \frac{a_{12} / \sqrt{a_{11} a_{22}}}{\sqrt{1-\left[a_{12}^{2} /\left(a_{11} a_{22}\right)\right]}} \\
& =\sqrt{n-1} \frac{r}{\sqrt{1-r^{2}}} .
\end{aligned}
$$

Thus $\sqrt{n-1} r / \sqrt{1-r^{2}}$ has a conditional $t$-distribution with $n-1$. degrees of freedom. The density of $t$ is

$$
\frac{\Gamma\left(\frac{1}{2} n\right)}{\sqrt{n-1} \Gamma\left[\frac{1}{2}(n-1)\right] \sqrt{\pi}}\left(1+\frac{t^{2}}{n-1}\right)^{-\frac{1}{2} n},
$$

and the density of $W=r / \sqrt{1-r^{2}}$ is

$$
\frac{\Gamma\left(\frac{1}{2} n\right)}{\Gamma\left[\frac{1}{2}(n-1)\right] \sqrt{\pi}}\left(1+w^{2}\right)^{-\frac{1}{2} n} .
$$

Since $w=r\left(1-r^{2}\right)^{-\frac{1}{2}}$, we have $d w / d r=\left(1-r^{2}\right)^{-\frac{1}{2}}$. Therefore the density of $r$ is (replacing $n$ by $N-1$ )

$$
\frac{\Gamma\left[\frac{1}{2}(N-1)\right]}{\Gamma\left[\frac{1}{2}(N-2)\right] \sqrt{\pi}}\left(1-r^{2}\right)^{\frac{1}{2}(N-4)} .
$$

It should be noted that (17) is the conditional density of $r$ for $\boldsymbol{v}_{1}$ fixed. However, since (17) does not depend on $\nu_{1}$, it is also the marginal density of $r$.

Theorem 4.2.1. Let $X_{1}, \ldots, X_{N}$ be independent, each with distribution $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. If $\rho_{i j}=0$, the density of $r_{i j}$ defined by (1) is (17).

From (17) we see that the density is symmetric about the origin. For $N>4$, it has a mode at $r=0$ and its order of contact with the $r$-axis at $\pm 1$ is $\frac{1}{2}(N-5)$ for $N$ odd and $\frac{1}{2} N-3$ for $N$ even. Since the density is even, the odd moments are zero; in particular, the mean is zero. The even moments are found by integration (letting $x=r^{2}$ and using the definition of the beta function). That $\mathscr{E} r^{2 m}=\Gamma\left[\frac{1}{2}(N-1)\right] \Gamma\left(m+\frac{1}{2}\right) /\left(\sqrt{\pi} \Gamma\left[\frac{1}{2}(N-1)+m\right]\right\}$ and in particular that the variance is $1 /(N-1)$ may be verified by the reader.

The most important use of Theorem 4.2.1 is to find significance points for testing the hypothesis that a pair of variables are not correlated. Consider the
hypothesis

$$
H: \rho_{i j}=0
$$

for some particular pair ( $i, j$ ). It would seem reasonable to reject this hypothesis if the corresponding sample correlation coefficient were very different from zero. Now how do we decide what we mean by "very different"?

Let us suppose we are interested in testing $H$ against the alternative hypotheses $\rho_{i j}>0$. Then we reject $H$ if the sample correlation coefficient $r_{i j}$ is greater than some number $r_{0}$. The probability of rejecting $H$ when $H$ is true is

$$
\int_{r_{0}}^{1} k_{N}(r) d r
$$

where $k_{N}(r)$ is (17), the density of a correlation coefficient based on $N$ observations. We choose $r_{0}$ so (19) is the desired significance level. If we test $H$ against alternatives $\rho_{i j}<0$, we reject $H$ when $r_{i j}<-r_{0}$.

Now suppose we are interested in alternatives $\rho_{1 j} \neq 0$; that is, $\rho_{1 j}$ may be either positive or negative. Then we reject the hypothesis $H$ if $r_{1 j}>r_{1}$ or $r_{i j}<-r_{!}$. The probability of rejection when $H$ is true is

$$
\int_{-1}^{-r_{1}} k_{N}(r) d r+\int_{r_{1}}^{1} k_{N}(r) d r .
$$

The number $r_{1}$ is chosen so that (20) is the desired significance level.
The significance points $r_{1}$ are given in many books, including Table VI of Fisher and Yates (1942); the index $n$ in Table VI is equal to odr $N-2$. Since $\sqrt{N-2} r / \sqrt{1-r^{2}}$ has the $t$-distribution with $N-2$ degrees of freedom, $t$-tables can also be used. Against alternatives $\rho_{i j} \neq 0$, reject $H$ if

$$
\sqrt{N-2} \frac{\left|r_{i j}\right|}{\sqrt{1-r_{i j}^{2}}}>t_{N-2}(\alpha),
$$

where $t_{N-2}(\alpha)$ is the two-tailed significance point of the $t$-statistic with $N-2$ degrees of freedom for significance level $\alpha$. Against alternatives $\rho_{i j}>0$. reject $H$ if

$$
\sqrt{N-2} \frac{r_{i j}}{\sqrt{1-r_{i j}^{2}}}>t_{N-2}(2 \alpha) .
$$

From (13) and (14) we see that $\sqrt{N-2} r / \sqrt{1-r^{2}}$ is the proper statistic for testing the hypothesis that the regression of $V_{2}$ on $v_{1}$ is zero. In terms of the original observation $\left\{x_{1 \alpha}\right\}$. we have

$$
\sqrt{N-2} \frac{r}{\sqrt{1-r^{2}}}=\frac{b \sqrt{\sum_{\alpha=1}^{N}\left(x_{1 \alpha}-\bar{x}_{1}\right)^{2}}}{\sqrt{\sum_{\alpha=1}^{1}\left[x_{2 \alpha}-\bar{x}_{2}-b\left(x_{1 \alpha}-\bar{x}_{1}\right)\right]^{2} /(N-2)}},
$$

where $b=\sum_{\alpha=1}^{\prime}\left(x_{2 \alpha}-\bar{x}_{2}\right)\left(x_{1 \alpha}-\bar{x}_{1}\right) / \sum_{\alpha=1}^{\wedge}\left(x_{1 \alpha}-\bar{x}_{1}\right)^{2}$ is the least squares regression coefficient of $x_{20}$ on $x_{1, \mathrm{r}}$. It is seen that the tcst of $\rho_{12}=0$ is equivalent to the test that the regression of $X_{2}$ on $x_{1}$ is zero (i.e., that $\rho_{12} \sigma_{2} / \sigma_{1}=0$ ).

To illustrate this procedure we consider the example given in Section 3.2. Let us test the null hypothesis that the effects of the two drugs are uncorrelated against the alternative that they are positively correlated. We shall use the $5 \%$ level of significance. For $N=10$, the $5 \%$ significance point ( $r_{0}$ ) is 0.5494 . Our observed correlation coefficient of 0.7952 is significant; we reject the hypothesis that the effects of the two drugs are independent.

### 4.2.2. The Distribution When the Population Correlation Coefficient Is Nonzero; Tests of Hypotheses and Confidence Intervals

To find the distribution of the sample correlation coefficient when the population coefficient is different from zero, we shall first derive the joint density of $a_{11}, a_{12}$, and $a_{22}$. In Section 4.2.1 we saw that, conditional on $\boldsymbol{v}_{1}$ held fixed. the random variables $b=a_{12} / a_{11}$ and $U / \sigma^{2}=\left(a_{22}-a_{12}^{2} / a_{11}\right) / \sigma^{2}$ are distributed independently according to $N\left(\beta, \sigma^{2} / c^{2}\right)$ and the $\chi^{2}$-distribution with $n-1$ degrees of freedom, respectively. Denoting the density of the $\chi^{2}$-distribution by $g_{n-1}(u)$, we write the conditional density of $b$ and $U$ as $n\left(b \mid \beta, \sigma^{2} / a_{11}\right) g_{n-1}\left(u / \sigma^{2}\right) / \sigma^{2}$. The joint density of $V_{1}, b$, and $U$ is $n\left(r_{1} \mid \mathbf{0}, \sigma_{1}^{2} I\right) n\left(b \mid \beta, \sigma^{2} / a_{11}\right) g_{n-1}\left(u / \sigma^{2}\right) / \sigma^{2}$. The marginal density of $V_{1}^{\prime} V_{1} / \sigma_{1}^{2}=a_{11} / \sigma_{1}^{2}$ is $g_{n}(u)$; that is, the density of $a_{11}$ is

$$
\frac{1}{\sigma_{1}^{2}} g_{n}\left(\frac{a_{11}}{\sigma_{1}^{2}}\right)=\int_{v_{1} v_{1}=a_{11}} \cdots \int_{1} n\left(v_{1} \mid 0, \sigma_{1}^{2} I\right) d W,
$$

where $d W$ is the proper volume element.
The integration is over the sphere $v_{1}^{\prime} v_{1}=a_{11}$; thus, $d W$ is an element of area on this sphere. (See Problem 7.1 for the use of angular coordinates in


[^0]:    An Introduction to Multivariate Statstical Anabsis, Third Edition. By T. W. Anderson ISBN 0-471-36091-0 Copyright © 2003 John Wiley \& Sons, Inc.



defining $d W$.) Thus the joint density or $b, U$, and $a_{11}$ is

$$
\begin{aligned}
\int_{v_{1}^{\prime} v_{1}=a_{11}} \cdots & n\left(b \mid \beta, \sigma^{2} / a_{11}\right) g_{n-1}\left(u / \sigma^{2}\right) \frac{1}{\sigma^{2}} n\left(v_{1} \mid 0, \sigma_{1}^{2} I\right) d W \\
& =\frac{g_{n}\left(a_{11} / \sigma_{1}^{2}\right) n\left(b \mid \beta, \sigma^{2} / a_{11}\right) g_{n-1}\left(u / \sigma^{2}\right)}{\sigma_{1}^{2} \sigma^{2}} \\
= & \frac{\left(a_{11}\right)^{\frac{1}{2} n-1}}{\left(2 \sigma_{1}^{2}\right)^{\frac{1}{2} n} \Gamma\left(\frac{1}{2} n\right)} \exp \left(-\frac{a_{11}}{2 \sigma_{1}^{2}}\right) \frac{\sqrt{a_{11}}}{\sqrt{2 \pi \sigma^{2}}} \exp \left[-\frac{a_{11}}{2 \sigma^{2}}(b-\beta)^{2}\right] \\
& \cdot \frac{1}{\left(2 \sigma^{2}\right)^{\frac{1}{2}(n-1)} \Gamma\left[\frac{1}{2}(n-1)\right]} u^{\frac{1}{2}(n-3)} \exp \left(-\frac{u}{2 \sigma^{2}}\right)
\end{aligned}
$$

Now let $b=a_{12} / a_{11}, U=a_{22}-a_{12}^{2} / a_{11}$. The Jacobian is

$$
\left|\frac{\partial(b, u)}{\partial\left(a_{12}, a_{22}\right)}\right|=\left|\begin{array}{cc}
\frac{1}{a_{11}} & 0 \\
-2 \frac{a_{12}}{a_{11}} & 1
\end{array}\right|=\frac{1}{a_{11}} .
$$

Thus the density of $a_{11}, a_{12}$, and $a_{22}$ for $a_{11} \geq 0, a_{22} \geq 0$, and $a_{11} a_{22}-a_{12}^{2} \geq 0$ is

$$
\frac{a_{11}^{\frac{1}{2}(n-3)}\left(\frac{a_{1 \mathrm{I}} a_{22}-a_{12}^{2}}{a_{11}}\right)^{\frac{1}{2}(n-3)} e^{-\frac{1}{2} Q}}{2^{n} \sigma_{1}^{n} \sigma_{2}^{n}\left(1-\rho^{2}\right)^{\frac{1}{2} n} \sqrt{\pi} \Gamma\left(\frac{1}{2} n\right) \Gamma\left[\frac{1}{2}(n-1]\right]},
$$

where

$$
\begin{aligned}
Q & =\frac{a_{11}}{\sigma_{1}^{2}}+\frac{a_{11}}{\sigma^{2}}\left(\frac{a_{12}^{2}}{a_{11}^{2}}-2 \rho \frac{\sigma_{1} \sigma_{2}}{\sigma_{1}^{2}} \frac{a_{12}}{a_{11}}+\frac{\rho^{2} \sigma_{1}^{2} \sigma_{2}^{2}}{\sigma_{1}^{4}}\right)+\frac{1}{\sigma^{2}}\left(a_{22}-\frac{a_{12}^{2}}{a_{11}}\right) \\
& =a_{11}\left[\frac{1}{\sigma_{1}^{2}}+\frac{\rho^{2} \sigma_{1}^{2} \sigma_{2}^{2}}{\sigma_{1}^{4} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\right]-2 a_{12} \frac{\rho \sigma_{2}}{\sigma_{1} \sigma_{2}^{2}\left(1-\rho^{2}\right)}+\frac{a_{22}}{\sigma_{2}^{2}\left(1-\rho^{2}\right)} \\
& =\frac{1}{1-\rho^{2}}\left(\frac{a_{11}}{\sigma_{1}^{2}}-2 \rho \frac{a_{12}}{\sigma_{1} \sigma_{2}}+\frac{a_{22}}{\sigma_{2}^{2}}\right)
\end{aligned}
$$

The density can be written

$$
\frac{|A|^{\frac{1}{2}(n-3)} e^{-\frac{1}{2} Q}}{2^{n}|\Sigma|^{\frac{1}{2} n} \sqrt{\pi} \Gamma\left(\frac{1}{2} n\right) \Gamma\left[\frac{1}{2}(n-1)\right]}
$$

for $A$ positive definite, and. 0 otherwise. This is a special case of the Wishart density derived in Chapter 7.

We want to find the density of

$$
r=\frac{a_{12}}{\sqrt{a_{11} a_{22}}}=\frac{a_{12} /\left(\sigma_{1} \sigma_{2}\right)}{\sqrt{\left(a_{11} / \sigma_{1}^{2}\right)\left(a_{22} / \sigma_{2}^{2}\right)}}=\frac{a_{12}^{*}}{\sqrt{a_{11}^{*} a_{22}^{*}}},
$$

where $a_{11}^{*}=a_{11} / \sigma_{1}^{2}, a_{22}^{*}=a_{22} / \sigma_{2}^{2}$, and $a_{12}^{*}=a_{12} /\left(\sigma_{1} \sigma_{2}\right)$. The transformation is equivalent to setting $\sigma_{1}=\sigma_{2}=1$. Then the density of $a_{11}, a_{22}$, and $r=a_{12} / \sqrt{a_{11} a_{22}}\left(d a_{12}=d r \sqrt{a_{11} a_{22}}\right)$ is

$$
\frac{a_{11}^{\frac{1}{2} n-1} a_{22}^{\frac{1}{2} n-1}\left(1-r^{2}\right)^{\frac{1}{2}(n-3)} e^{-\frac{1}{2} Q}}{2^{n}\left(1-\rho^{2}\right)^{\frac{1}{2} n} \sqrt{\pi} \Gamma\left(\frac{1}{2} n\right) \Gamma\left[\frac{1}{2}(n-1)\right]},
$$

where

$$
Q=\frac{a_{11}-2 \rho r \sqrt{a_{11}} \sqrt{a_{22}}+a_{22}}{1-\rho^{2}} .
$$

To find the density of $r$, we must integrate (31) with respect to $a_{11}$ and $a_{22}$ over the range 0 to $\infty$. There are various ways of carrying out the integration, which result in different expressions for the density. The method we shall indicate here is straightforward. We expand part of the exponential:

$$
\exp \left[\frac{\rho r \sqrt{a_{11}} \sqrt{a_{22}}}{\left(1-\rho^{2}\right)}\right]=\sum_{\alpha=0}^{\infty} \frac{\left(\rho r \sqrt{a_{11}} \sqrt{a_{22}}\right)^{\alpha}}{\alpha!\left(1-\rho^{2}\right)^{\alpha}}
$$

Then the density (31) is

$$
\begin{aligned}
& \frac{\left(1-r^{2}\right)^{\frac{1}{2}(n-3)}}{\left(1-\rho^{2}\right)^{\frac{1}{2} n} 2^{n} \sqrt{\pi} \Gamma\left(\frac{1}{2} n\right) \Gamma\left[\frac{1}{2}(n-1)\right]} \sum_{\alpha=0}^{\infty} \frac{(\rho r)^{\alpha}}{\alpha!\left(1-\rho^{2}\right)^{\alpha}} \\
& \quad \cdot\left\{\exp \left[-\frac{a_{11}}{2\left(1-\rho^{2}\right)}\right] a_{11}^{(n+\alpha) / 2-1}\right\}\left\{\exp \left[-\frac{a_{22}}{2\left(1-\rho^{2}\right)}\right] a_{22}^{(n+\alpha) / 2-1}\right\}
\end{aligned}
$$

Since

$$
\int_{0}^{\infty} a^{\frac{1}{2}(n+\alpha)-1} \exp \left[-\frac{a}{2\left(1-\rho^{2}\right)}\right] d a=\Gamma\left[\frac{1}{2}(n+\alpha)\right]\left[2\left(1-\rho^{2}\right)\right]^{\frac{1}{3}(n+\alpha)} .
$$

the integral of (34) (term-by-term integration is permissible) is

$$
\begin{aligned}
& \frac{\left(1-r^{2}\right)^{\frac{1}{2}(n-3)}}{\left(1-\rho^{2}\right)^{\frac{1}{2} n} 2^{n} \sqrt{\pi} \Gamma\left(\frac{1}{2} n\right) \Gamma\left[\frac{1}{2}(n-1)\right]} \\
& \quad-\sum_{\alpha=0}^{\infty} \frac{(\rho r)^{\alpha}}{\alpha!\left(1-\rho^{2}\right)^{\alpha}} \Gamma^{2}\left[\frac{1}{2}(n+\alpha)\right] 2^{n+\alpha}\left(1-\rho^{2}\right)^{n+\alpha} \\
& =\frac{\left(1-\rho^{2}\right)^{\frac{1}{2} n}\left(1-r^{2}\right)^{\frac{1}{2}(n-3)}}{\sqrt{\pi} \Gamma\left(\frac{1}{2} n\right) \Gamma\left[\frac{1}{2}(n-1)\right]} \sum_{\alpha=0}^{\infty} \frac{(2 \rho r)^{\alpha}}{\alpha!} \Gamma^{2}\left[\frac{1}{2}(n+\alpha)\right]
\end{aligned}
$$

The duplication formula for the gamma function is

$$
\Gamma(2 z)=\frac{2^{2 z-1} \Gamma(z)\left(z+\frac{1}{2}\right)}{\sqrt{\pi}}
$$

It can be used to modify the constant in (36).
Theorem 4.2.2. The correlation coefficient in a sample of $N$ from a bwariate normal distribution with correlation $\rho$ is distributed with density

$$
\begin{aligned}
& \frac{2^{n-2}\left(1-\rho^{2}\right)^{\frac{1}{2} n}\left(1-r^{2}\right)^{\frac{1}{5}(n-3)}}{(n-2)!\pi} \sum_{\alpha=0}^{\infty} \frac{(2 \rho r)^{\alpha}}{\alpha!} \Gamma^{2}\left[\frac{1}{2}(n+\alpha)\right] \\
&-1 \leq r \leq 1
\end{aligned}
$$

where $n=N-1$.
The distribution of $r$ was first found by Fisher (1915). He also gave as another form of the density,

$$
\frac{\left(1-\rho^{2}\right)^{\frac{1}{2} n}\left(1-r^{2}\right)^{\frac{1}{3}(n-3)}}{\pi(n-2)!}\left[\left.\frac{d^{n-1}}{d x^{n-1}}\left\{\frac{\cos ^{-1}(-x)}{\sqrt{1-x^{2}}}\right\}\right|_{x=r \rho}\right] .
$$

See Problem 4.24.

Hotelling (1953) has made an exhaustive study of the distribution of $r$. He has recommended the following form:

$$
\begin{aligned}
& \frac{n-1}{\sqrt{2 \pi}} \frac{\Gamma(n)}{\Gamma\left(n+\frac{1}{2}\right)}\left(1-\rho^{2}\right)^{\frac{1}{2} n}\left(1-r^{2}\right)^{\frac{1}{4}(n-3)} \\
& \quad \cdot(1-\rho r)^{-n+\frac{1}{2}} F\left(\frac{1}{2}, \frac{1}{2} ; n+\frac{1}{2} ; \frac{1+\rho r}{2}\right)
\end{aligned}
$$

where

$$
F(a, b ; c ; x)=\sum_{j=0}^{\infty} \frac{\Gamma(a+j)}{\Gamma(a)} \frac{\Gamma(b+j)}{\Gamma(b)} \frac{\Gamma(c)}{\Gamma(c+j)} \frac{x^{j}}{j!}
$$

is a hypergeometric function. (See Problem 4.25.) The series in (40) converges more rapidly than the one in (38). Hotelling discusses methods of integrating the density and also calculates moments of $r$.

The cumulative distribution of $r$,

$$
\operatorname{Pr}\left\{r \leq r^{*}\right\}=F\left(r^{*} \mid N, \rho\right),
$$

has been tabulated by David (1938) for $\rho=0(.1) .9, V=3(1) 25,50,100,200$, 400, and $r^{*}=-1(.05) 1$. (David's $n$ is our $N$.) It is clear from the density (38) that $F\left(r^{*} \mid N, \rho\right)=1-F\left(-r^{*} \mid N,-\rho\right)$ because the density for $r, \rho$ is equal to the density for $-r,-\rho$. These tables can be used for a number of statistical procedures.

First, we consider the problem of using a sample to test the hypothesis

$$
H: \rho=\rho_{0} .
$$

If the alternatives are $\rho>\rho_{0}$, we reject the hypothesis if the sample correlation coefficient is greater than $r_{0}$, where $r_{0}$ is chosen so $1-F\left(r_{0} \mid N, \rho_{0}\right)=\alpha$, the significance level. If the alternatives are $\rho<\rho_{0}$, we reject the hypothesis if the sample correlation coefficient is less than $r_{0}^{\prime}$, where $r_{0}^{\prime}$ is chosen so $F\left(r_{0}^{\prime} \mid N, \rho_{0}\right)=\alpha$. If the alternatives are $\rho \neq \rho_{0}$, the region of rejection is $r>r_{1}$ and $r<r_{1}^{\prime}$, where $r_{1}$ and $r_{1}^{\prime}$ are chosen so $\left[1-F\left(r_{1} \mid N, \rho_{0}\right)\right]+F\left(r_{1}^{\prime} \mid N, \rho_{0}\right)=\alpha$. David suggests that $r_{1}$ and $r_{1}^{\prime}$ be chosen so $\left[1-F\left(r_{1} \mid N, \rho_{0}\right)\right]=F\left(r_{1}^{\prime} \mid N, \rho_{0}\right) =\frac{1}{2} \alpha$. She has shown (1937) that for $N \geq 10,|\rho| \leq 0.8$ this critical region is nearly the region of an unbiased test of $H$, that is, a test whose power function has its minimum at $\rho_{0}$.

It should be pointed out that any test based on $r$ is invariant under transformations of location and scale, that is, $x_{1 \alpha}^{*}=b_{i} x_{1 \alpha}+c_{i}, b_{1}>0, i=1,2$,
${ }^{\dagger} \rho=(X .1) .9$ means $\rho=0,0.1,0.2, \ldots, 0.9$.

Table 4.1. A Power Function
| $\rho$ | Probability |
| :---: | :---: |
| -1.0 | 0.0000 |
| -0.8 | 0.0000 |
| -0.6 | 0.0004 |
| -0.4 | 0.0032 |
| -0.2 | 0.0147 |
| 0.0 | 0.0500 |
| 0.2 | 0.1376 |
| 0.4 | 0.3215 |
| 0.6 | 0.6235 |
| 0.8 | 0.9279 |
| 1.0 | 1.0000 |


$\alpha=1, \ldots, N$; and $r$ is essentially the only invariant of the sufficient statistics (Problem 3.7). The above procedure for testing $H: \rho=\rho_{0}$ against alternatives $\rho>\rho_{0}$ is uniformly most powerful among all invariant tests. (See Problems 4.16, 4.17, and 4.18.)

As an example suppose one wishes to test the hypothesis that $\rho=0.5$ against alternatives $\rho \neq 0.5$ at the $5 \%$ level of significance using the correlation observed in a sample of 15. In David's tables we find (by interpolation) that $F(0.027 \mid 15,0.5)=0.025$ and $F(0.805 \mid 15,0.5)=0.975$. Hence we reject the hypothesis if our sample $r$ is less than 0.027 or greater than 0.805 .

Secondly, we can use David's tables to compute the power function of a test of correlation. If the region of rejection of $H$ is $r>r_{1}$ and $r<r_{1}^{\prime}$, the power of the test is a function of the true correlation $\rho$, namely $\left[1-F\left(r_{1} \mid N, \rho\right)+\left[F\left(r_{1}^{\prime} \mid N, \rho\right)\right]\right.$; this is the probability of rejecting the null hypothesis when the population correlation is $\rho$.

As an example consider finding the power function of the test for $\rho=0$ considered in the preceding section. The rejection region (one-sided) is $r \geq 0.5494$ at the $5 \%$ significance level. The probabilities of rejection are given in Table 4.1. The graph of the power function is illustrated in Figure 4.2.

Thirdly, David's computations lead to confidence regions for $\rho$. For given $N, r_{1}^{\prime}$ (defining a significance point) is a function of $\rho$, say $f_{1}(\rho)$, and $r_{1}$ is another function of $\rho$, say $f_{2}(\rho)$, such that

$$
\operatorname{Pr}\left\{f_{1}(\rho)<r<f_{2}(\rho) \mid \rho\right\}=1-\alpha .
$$

Clearly, $f_{1}(\rho)$ and $f_{2}(\rho)$ are monotonically increasing functions of $\rho$ if $r_{1}$ and $r_{\text {I }}^{\prime}$ are chosen so $1-F\left(r_{1} \mid N . \rho\right)=\frac{1}{2} \alpha=F\left(r_{1}^{\prime} \mid N, \rho\right)$. If $\rho=f_{i}^{-1}\left(r^{\prime}\right)$ is the

![](https://cdn.mathpix.com/cropped/9396746c-196a-4cd6-8859-a78ff2954eb5-146.jpg?height=410&width=1013&top_left_y=228&top_left_x=299)
Figure 4.2. A power function.

inverse of $r=f_{i}(\rho), i=1,2$, then the inequality $f_{1}(\rho)<r$ is equivalent to ${ }^{\dagger} \rho<f_{\mathrm{I}}^{-1}(r)$, and $r<f_{2}(\rho)$ is equivalent to $f_{2}^{-1}(r)<\rho$. Thus (44) can be written

$$
\operatorname{Pr}\left\{f_{2}^{-1}(r)<\rho<f_{1}^{-1}(r) \mid \rho\right\}=1-\alpha .
$$

This equation says that the probability is $1-\alpha$ that we draw a sample such that the interval ( $f_{2}^{-1}(r), f_{1}^{-1}(r)$ ) covers the parameter $\rho$. Thus this interval is a confidence interval for $\rho$ with confidence coefficient $1-\alpha$. For a given $N$ and $\alpha$ the curves $r=f_{1}(\rho)$ and $r=f_{2}(\rho)$ appear as in Figure 4.3. In testing the hypothesis $\rho=\rho_{0}$, the intersection of the line $\rho=\rho_{0}$ and the two curves gives the significance points $r_{1}$ and $r_{1}^{\prime}$. In setting up a confidence region for $\rho$ on the basis of a sample correlation $r^{*}$, we find the limits $f_{2}^{-1}\left(r^{*}\right)$ and

![](https://cdn.mathpix.com/cropped/9396746c-196a-4cd6-8859-a78ff2954eb5-146.jpg?height=677&width=920&top_left_y=1509&top_left_x=351)
Figure 4.3

${ }^{\dagger}$ The point $\left(f_{1}(\rho), \rho\right)$ on the first curve is to the left of $(r, \rho)$, and the point $\left(r, f_{1}^{-1}(r)\right)$ is above $(r, \rho)$.
$f_{\mathrm{I}}^{-1}\left(r^{*}\right)$ by the intersection of the line $r=r^{*}$ with the two curves. David gives these curves for $\alpha=0.1,0.05,0.02$, and 0.01 for various values of $N$. Onesided confidence regions can be obtained by using only one inequality above.

The tables of $F(r \mid N, \rho)$ can also be used instead of the curves for finding the confidence interval. Given the sample value $r^{*}, f_{1}^{-1}\left(r^{*}\right)$ is the value of $\rho$ such that $\frac{1}{2} \alpha=\operatorname{Pr}\left\{r \leq r^{*} \mid \rho\right\}=F\left(r^{*} \mid N, \rho\right)$, and similarly $f_{2}^{-1}\left(r^{*}\right)$ is the value of $\rho$ such that $\frac{1}{2} \alpha=\operatorname{Pr}\left\{r \geq r^{*} \mid \rho\right\}=1-F\left(r^{*} \mid N, \rho\right)$. The interval between these two values of $\rho,\left(f_{2}^{-1}\left(r^{*}\right), f_{1}^{-1}\left(r^{*}\right)\right)$, is the confidence interval.

As an example, consider the confidence interval with confidence coefficient 0.95 based on the correlation of 0.7952 observed in a sample of 10 . Using Graph II of David, we find the two limits are 0.34 and 0.94 . Hence we state that $0.34<\rho<0.94$ with confidence $95 \%$.

Definition 4.2.1. Let $L(x, \theta)$ be the likelihood function of the observation vector $\boldsymbol{x}$ and the parameter vector $\boldsymbol{\theta} \in \boldsymbol{\Omega}$. Let a null hypothesis be defined by a proper subset $\omega$ of $\Omega$. The likelihood ratio criterion is

$$
\lambda(x)=\frac{\sup _{\theta \in \omega} L(\boldsymbol{x}, \boldsymbol{\theta})}{\sup _{0 \in \Omega} L(\boldsymbol{x}, \boldsymbol{\theta})} .
$$

The likelihood ratio test is the procedure of rejecting the null hypothesis when $\lambda(x)$ is less than a predetermined constant.

Intuitively, one rejects the null hypothesis if the density of the observations under the most favorable choice of parameters in the null hypothesis is much less than the density under the most favorable unrestricted choice of the parameters. Likelihood ratio tets have some desirable features; see Lehmann (1959), for example. Wald (1943) has proved some favorable asymptotic properties. For most hypotheses concerning the multivariate normal distribution, likelihood ratio tests are appropriate and often are optimal.

Let us consider the likelihood ratio test of the hypothesis that $\rho=\rho_{0}$ based on a sample $x_{1}, \ldots, x_{N}$ from the bivariate normal distribution. The set $\Omega$ consists of $\mu_{1}, \mu_{2}, \sigma_{1}, \sigma_{2}$, and $\rho$ such that $\sigma_{1}>0, \sigma_{2}>0 .-1<\rho<1$. The set $\omega$ is the subset for which $\rho=\rho_{0}$. The likelihood maximized in $\Omega$ is (by Lemmas 3.2.2 and 3.2.3)

$$
\max _{\Omega} L=\frac{N^{N} e^{-N}}{(2 \pi)^{N}\left(1-r^{2}\right)^{\frac{1}{N} N} a_{11}^{N / 2} a_{22}^{2}} .
$$

Under the null hypothesis the likelihood function is

$$
\frac{1}{(2 \pi)^{N}\left(1-\rho_{0}^{2}\right)^{\frac{1}{2} N}\left(\sigma^{2}\right)^{N}} \exp \left[-\frac{\alpha_{11} / \tau+\tau a_{22}-2 \rho_{0} a_{12}}{2 \sigma^{2}\left(1-\rho_{0}^{2}\right)}\right],
$$

where $\sigma^{2}=\sigma_{1} \sigma_{2}$ and $\tau=\sigma_{1} / \sigma_{2}$. The maximum of (48) with respect to $\tau$ occurs at $\hat{\tau}=\sqrt{a_{11}} / \sqrt{a_{22}}$. The concentrated likelihood is

$$
\frac{1}{(2 \pi)^{N}\left(1-\rho_{0}^{2}\right)^{\frac{1}{2} N}\left(\sigma^{2}\right)^{N}} \exp \left[-\frac{\sqrt{a_{11}} \sqrt{a_{22}}\left(1-\rho_{0} r\right)}{\sigma^{2}\left(1-\rho_{0}^{2}\right)}\right] ;
$$

the maximum of (49) occurs at

$$
\hat{\sigma}^{2}=\frac{a_{11}^{\frac{1}{1}} a_{22}^{\frac{1}{2}}\left(1-\rho_{0} r\right)}{N\left(1-\rho_{0}^{2}\right)} .
$$

The likelihood ratio criterion is, therefore,

$$
\frac{\max _{\omega} L}{\max _{\Omega} L}=\frac{\left(1-\rho_{0}^{2}\right)^{\frac{1}{2} N}\left(1-r^{2}\right)^{\frac{1}{2} N}}{\left(1-\rho_{0} r\right)^{N}}=\left[\frac{\left(1-\rho_{0}^{2}\right)\left(1-r^{2}\right)}{\left(1-\rho_{0} r\right)^{2}}\right]^{\frac{1}{2} N} .
$$

The likelihood ratio test is $\left(1-\rho_{0}^{2}\right)\left(1-r^{2}\right)\left(1-\rho_{0} r\right)^{-2}<c$, where $c$ is chosen so the probability of the inequality when samples are drawn from normal populations with correlation $\rho_{0}$ is the prescribed significance level. The critical region can be written equivalently as

$$
\left(\rho_{0}^{2} c-\rho_{0}^{2}+1\right) r^{2}-2 \rho_{0} c r+c-1+\rho_{0}^{2}>0
$$

or

$$
\begin{aligned}
& r>\frac{\rho_{0} c+\left(1-\rho_{0}^{2}\right) \sqrt{1-c}}{\rho_{0}^{2} c+1-\rho_{0}^{2}}, \\
& r<\frac{\rho_{0} c-\left(1-\rho_{0}^{2}\right) \sqrt{1-c}}{\rho_{0}^{2} c+1-\rho_{0}^{2}},
\end{aligned}
$$

Thus the likelihood ratio test of $H: \rho=\rho_{0}$ against alternatives $\rho \neq \rho_{0}$ has a rejection region of the form $r>r_{1}$ and $r<r_{1}^{\prime}$; but $r_{1}$ and $r_{1}^{\prime}$ are not chosen so that the probability of each inequality is $\alpha / 2$ when $H$ is true, but are taken to be of the form given in (53), where $c$ is chosen so that the probability of the two inequalities is $\alpha$.

### 4.2.3. The Asymptotic Distribution of a Sample Correlation Coefficient and Fisher's $\boldsymbol{z}$

In this section we shall show that as the sample size increases, a sample correlation coefficient tends to be normally distributed. The distribution of a particular function of a sample correlation, Fisher's $z$ [Fisher (1921)], which has a variance approximately independent of the population correlation, tends to norma.ity faster.

We are particularly interested in the sample correlation coefficient

$$
r(n)=\frac{A_{i j}(n)}{\sqrt{A_{i i}(n) A_{j j}(n)}}
$$

for some $i$ and $j, i \neq j$. This can also be written

$$
r(n)=\frac{C_{1 j}(n)}{\sqrt{C_{1 u}(n) C_{j j}(n)}},
$$

where $C_{g h}(n)=A_{g h}(n) / \sqrt{\sigma_{g g} \sigma_{h h}}$. The set $C_{\imath i}(n), C_{\jmath j}(n)$, and $C_{\imath j}(n)$ is distributed like the distinct elements of the matrix

$$
\sum_{\alpha=1}^{n}\binom{Z_{i \alpha}^{*}}{Z_{j \alpha}^{*}}\left(Z_{i \alpha}^{*}, Z_{j \alpha}^{*}\right)=\sum_{\alpha=1}^{n}\binom{Z_{i \alpha} / \sqrt{\sigma_{u}}}{Z_{j \alpha} / \sqrt{\sigma_{j j}}}\left(Z_{i \alpha} / \sqrt{\sigma_{u}}, Z_{j \alpha} / \sqrt{\sigma_{j j}}\right),
$$

where the ( $Z_{1 \alpha}^{*}, Z_{1 \alpha}^{*}$ ) are independent, each with distribution

$$
N\left[\binom{0}{0},\left(\begin{array}{ll}
1 & \rho \\
\rho & 1
\end{array}\right)\right],
$$

where

$$
\rho=\frac{\sigma_{t j}}{\sqrt{\sigma_{t i} \sigma_{f j}}} .
$$

Let

$$
\begin{aligned}
U(n) & =\frac{1}{n}\left(\begin{array}{l}
C_{u}(n) \\
C_{j j}(n) \\
C_{u}(n)
\end{array}\right), \\
b & =\left(\begin{array}{l}
1 \\
1 \\
\rho
\end{array}\right) .
\end{aligned}
$$

Then by Theorem 3.4.4 the vector $\sqrt{n}[U(n)-\boldsymbol{b}]$ has a limiting normal distribution with mean 0 and covariance matrix

$$
\left(\begin{array}{ccc}
2 & 2 \rho^{2} & 2 \rho \\
2 \rho^{2} & 2 & 2 \rho \\
2 \rho & 2 \rho & 1+\rho^{2}
\end{array}\right) .
$$

Now we need the general theorem:
Theorem 4.2.3. Let $\{U(n)\}$ be a sequence of $m$-component random vectors and $\boldsymbol{b}$ a fixed vector such that $\sqrt{n}[U(n)-\boldsymbol{b}]$ has the limiting distribution $N(\mathbf{0}, \mathbf{T})$ as $n \rightarrow \infty$. Let $f(u)$ be a vector-valued function of $u$ such that each component $f_{j}(u)$ has a nonzero differential at $u=\boldsymbol{b}$, and let $\partial f_{j}(u) /\left.\partial u_{1}\right|_{u=b}$ be the $i$, $j$ th component of $\boldsymbol{\Phi}_{b}$. Then $\sqrt{n}\{f[u(n)]-f(b)\}$ has the limiting distribution $N\left(\mathbf{0}, \boldsymbol{\Phi}_{b}^{\prime} \mathbf{T} \boldsymbol{\Phi}_{b}\right)$.

Proof. See Serfling (1980), Section 3.3, or Rao (1973), Section 6a.2. A function $g(u)$ is said to have a differential at $b$ or to be totally differentiable at $\boldsymbol{b}$ if the partial derivatives $\partial g(u) / \partial u$, exist at $u=\boldsymbol{b}$ and for every $\varepsilon>0$ there exists a neighborhood $N_{\varepsilon}(b)$ such that

$$
\left|g(u)-g(b)-\sum_{i=1}^{m} \frac{\partial g(u)}{\partial u_{i}}\left(u_{i}-b_{i}\right)\right| \leq \varepsilon\|u-b\| \quad \text { for all } u \in N_{\varepsilon}(b) .
$$ $\square$

It is clear that $U(n)$ defined by (57) with $\boldsymbol{b}$ and $\mathbf{T}$ defined by (58) and (59), respectively, satisfies the conditions of the theorem. The function

$$
r=\frac{u_{3}}{\sqrt{u_{1} u_{2}}}=u_{3} u_{1}^{-\frac{1}{2}} u_{2}^{-\frac{1}{2}}
$$

satisfies the conditions; the elements of $\boldsymbol{\Phi}_{b}$ are

$$
\begin{aligned}
& \left.\frac{\partial r}{\partial u_{1}}\right|_{u=b}=-\left.\frac{1}{2} u_{3} u_{1}^{-\frac{3}{2}} u_{2}^{-\frac{1}{2}}\right|_{u=b}=-\frac{1}{2} \rho, \\
& \left.\frac{\partial r}{\partial u_{2}}\right|_{u=b}=-\left.\frac{1}{2} u_{3} u_{1}^{-\frac{3}{2}} u_{2}^{-\frac{1}{2}}\right|_{u=b}=-\frac{1}{2} \rho, \\
& \left.\frac{\partial r}{\partial u_{3}}\right|_{u=b}=\left.u_{1}^{-\frac{1}{2}} u_{2}^{-\frac{1}{2}}\right|_{u=b}=1,
\end{aligned}
$$



and $f(b)=\rho$. The variance of the limiting distribution of $\sqrt{n}[r(n)-\rho]$ is

$$
\begin{gathered}
\left(-\frac{1}{2} \rho,-\frac{1}{2} \rho, 1\right)\left(\begin{array}{ccc}
2 & 2 \rho^{2} & 2 \rho \\
2 \rho^{2} & 2 & 2 \rho \\
2 \rho & 2 \rho & 1+\rho^{2}
\end{array}\right)\left(\begin{array}{c}
-\frac{1}{2} \rho \\
-\frac{1}{2} \rho \\
1
\end{array}\right) \\
\quad=\left(\rho-\rho^{3}, \rho-\rho^{3}, 1-\rho^{2}\right)\left(\begin{array}{c}
-\frac{1}{2} \rho \\
-\frac{1}{2} \rho \\
1
\end{array}\right) \\
\quad=1-2 \rho^{2}+\rho^{4} \\
\quad=\left(1-\rho^{2}\right)^{2}
\end{gathered}
$$

Thus we obtain the following:
Theorem 4.2.4. If $r(n)$ is the sample correlation coefficient of a sample of $N (=n+1)$ from a normal distribution with correlation $\rho$, then $\sqrt{n}[r(n)-\rho] / \left(1-\rho^{2}\right)$ or $\left.\sqrt{N}[r(n)-\rho] /\left(1-\rho^{2}\right)\right]$ has the limiting distribution $N(0,1)$.

It is clear from Theorem 4.2.3 that if $f(x)$ is differentiable at $x=\rho$. then $\sqrt{n}[f(r)-f(\rho)]$ is asymptotically normally distributed with mean zero and variance

$$
\left(\left.\frac{\partial f}{\partial x}\right|_{x=\rho}\right)^{2}\left(1-\rho^{2}\right)^{2} .
$$

A useful function to consider is one whose asymptotic variance is constant (here unity) independent of the parameter $\rho$. This function satisfies the equation

$$
f^{\prime}(\rho)=\frac{1}{1-\rho^{2}}=\frac{1}{2}\left(\frac{1}{1+\rho}+\frac{1}{1-\rho}\right)
$$

Thus $f(\rho)$ is taken as $\left.\frac{1}{2}[\log (1+\rho)-\log (1-\rho)]=\frac{1}{2} \log (1+\rho) /(1-\rho)\right]$. The so-called Fisher's $z$ is

$$
z=\frac{1}{2} \log \frac{1+r}{1-r}=\tanh ^{-1} r,
$$

where $r=\tanh z=\left(e^{z}-e^{-z}\right) /\left(e^{z}+e^{-z}\right)$. Let

$$
\zeta=\frac{1}{2} \log \frac{1+\rho}{1-\rho}
$$

Theorem 4.2.5. Let $z$ be defined by (65), where $r$ is the correlation coefficient of a sample of $N(=n+1)$ from a bivariate normal distribution with correlation $\rho$; let $\zeta$ be defined by (66). Then $\sqrt{n}(z-\zeta)$ has a limiting normal distribution with mean 0 and variance 1.

It can be shown that to a closer approximation

$$
\begin{gathered}
\mathscr{E} z \sim \zeta+\frac{\rho}{2 n} . \\
\mathscr{E}(z-\zeta)^{2} \sim \frac{1}{n-2} \sim \mathscr{E}\left(z-\zeta-\frac{\rho}{2 n}\right)^{2} .
\end{gathered}
$$

The latter follows from

$$
\mathscr{E}(z-\zeta)^{2}=\frac{1}{n}+\frac{8-\rho^{2}}{4 n^{2}}+\cdots
$$

and holds good for $\rho^{2} / n^{2}$ small. Hotelling (1953) gives moments of $z$ to order $n^{-3}$. An important property of Fisher's $z$ is that the approach to normality is much more rapid than for $r$. David (1938) makes some comparisons between the labulated probabilities and the probabilities computed by assuming $z$ is normally distributed. She recommends that for $N>25$ one take $z$ as normally distributed with mean and variance given by (67) and (68). Konishi (1978a, 1978b, 1979) has also studied $z$. [Ruben (1966) has suggested an alternative approach, which is more complicated, but possibly more accurate.]

We shall now indicate how Theorem 4.2.5 can be used.
a. Suppose we wish to test the hypothesis $\rho=\rho_{0}$ on the basis of a sample of $N^{\top}$ against the alternatives $\rho \neq \rho_{1}$. We compute $r$ and then $z$ by (65). Let

$$
\zeta_{0}=\frac{1}{2} \log \frac{1+\rho_{0}}{1-\rho_{0}} .
$$

Then a region of rejection at the 5\% significance I:vel is

$$
\sqrt{N-3}\left|z-\zeta_{0}\right|>1.96 .
$$

A better region is

$$
\sqrt{N-3}\left|z-\zeta_{0}-\frac{\frac{1}{2} \rho_{0}}{N-1}\right|>1.96 .
$$

b. Suppose we have a sample of $N_{1}$ from one population and a sample of $N_{2}$ from a second population. How do we test the hypothesis that the two
correlation coefficients are equal, $\rho_{1}=\rho_{2}$ ? From Theorem 4.2.5 we know that if the null hypothesis is true then $z_{1}-z_{2}$ [where $z_{1}$ and $z_{2}$ are defined by (65) for the two sample correlation coefficients] is asymptotically normally distributed with mean 0 and variance $1 /\left(N_{1}-3\right)+1 /\left(N_{2}-3\right)$. As a critical region of size $5 \%$, we use

$$
\frac{\left|z_{1}-z_{2}\right|}{\sqrt{1 /\left(N_{1}-3\right)+1 /\left(N_{2}-3\right)}}>1.96
$$

c. Under the conditions of paragraph $b$, assume that $\rho_{1}=\rho_{2}=\rho$. How do we use the results of both samples to give a joint estimate of $\rho$ ? Since $z_{1}$ and $z_{2}$ have variances $1 /\left(N_{1}-3\right)$ and $1 /\left(N_{2}-3\right)$, respectively, we can estimate $\zeta$ by

$$
\frac{\left(N_{1}-3\right) z_{1}+\left(N_{2}-3\right) z_{2}}{N_{1}+N_{2}-6}
$$

and convert this to an estimate of $\rho$ by the inverse of (65).
d. Let $r$ be the sample correlation from $N$ observations. How do we obtain a confidence interval for $\rho$ ? We know that approximately

$$
\operatorname{Pr}\{-1.96 \leq \sqrt{N-3}(z-\zeta) \leq 1.96\}=0.95 .
$$

From this we deduce that $[-1.96 / \sqrt{N-3}+z, 1.96 / \sqrt{N-3}+z]$ is a confidence interval for $\zeta$. From this we obtain an interval for $\rho$ using the fact $\rho=\tanh \zeta=\left(e^{\zeta}-e^{-\zeta}\right) /\left(e^{\zeta}+e^{-\zeta}\right)$, which is a monotonic transformation. Thus a $95 \%$ confidence interval is

$$
\tanh (z-1.96 / \sqrt{N-3}) \leq \rho \leq \tanh (z+1.96 / \sqrt{N-3}) .
$$

The bootstrap method has been developed to assess the variability of a sample quantity. See Efron (1982). We shall illustrate the method on the sample correlation coefficient, but it can be applied to other quantities studied in this book.

Suppose $x_{1}, \ldots, x_{N}$ is a sample from some bivariate population not necessarily normal. The approach of the bootstrap is to consider these $N$ vectors as a finite population of size $N$; a random vector $\boldsymbol{X}$ has the (discrete) probability

$$
\operatorname{Pr}\left\{X=x_{\alpha}\right\}=\frac{1}{N}, \quad \alpha=1, \ldots, N
$$

A random sample of size $N$ drawn from this finite population has a probability distribution, and the correlation coefficient calculated from such a sample has a (discrete) probability distribution, say $p_{N}(r)$. The bootstrap proposes to use this distribution in place of the unobtainable distribution of the correlation coefficient of random samples from the parent population. However, it is prohibitively expensive to compute; instead $p_{N}(r)$ is estimated by the empirical distribution of $r$ calculated from a large number of random samples from (77). Diaconis and Efron (1983) have given an example of $N=15$; they find the empirical distribution closely resembles the actual distribution of $r$ (essentially obtainable in this special case). An advantage of this approach is that it is not necessary to assume knowledge of the parent population; a disadvantage is the massive computation.

### 4.3. PARTIAL CORRELATION COEFFICIENTS; CONDITIONAL DISTRIBUTIONS

### 4.3.1. Estimation of Partial Correlation Coefficients

Partial correlation coefficients in normal distributions are correlation coefficients in conditional distributions. It was shown in Section 2.5 that if $X$ is distributed according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, where

$$
X=\binom{X^{(1)}}{X^{(2)}}, \quad \mu=\binom{\mu^{(1)}}{\mu^{(2)}}, \quad \Sigma=:\left(\begin{array}{ll}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{array}\right),
$$

then the conditional distribution of $X^{(1)}$ given $X^{(2)}=x^{(2)}$ is $N\left[\boldsymbol{\mu}^{(1)}+\boldsymbol{B}\left(x^{(2)}-\right.\right. \left.\left.\boldsymbol{\mu}^{(2)}\right), \boldsymbol{\Sigma}_{11 \cdot 2}\right]$, where

$$
\begin{aligned}
\beta & =\Sigma_{12} \Sigma_{22}^{-1}, \\
\Sigma_{11 \cdot 2} & =\Sigma_{11}-\Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} .
\end{aligned}
$$

The partial correlations of $X^{(1)}$ given $x^{(2)}$ are the correlations calculated in the usual way from $\Sigma_{11 \cdot 2}$. In this section we are interested in statistical problems concerning these correlation coefficients.

First we consider the problem of estimation on the basis of a sample of $N$ from $N(\mu, \Sigma)$. What are the maximum likelihood estimators of the partial correlations of $X^{(1)}$ (of $q$ components), $\rho_{1, q+1, \ldots, p}$ ? We know that the
maximum likelihood estimator of $\Sigma$ is $(1 / N) A$, where

$$
\begin{aligned}
A & =\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime} \\
& =\sum_{\alpha=1}^{N}\binom{x_{\alpha}^{(1)}-\bar{x}^{(1)}}{x_{\alpha}^{(2)}-\bar{x}^{(2)}}\left(x_{11}^{(1) \prime}-\bar{x}^{(1) \prime}, x_{\alpha}^{(2) \prime}-\bar{x}^{(2) \prime}\right) \\
& =\left(\begin{array}{ll}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{array}\right)
\end{aligned}
$$

and $\bar{x}=(1 / N) \sum_{\alpha=1}^{N} x_{\alpha}=\left(\bar{x}^{(1) \prime} \bar{x}^{(2) \prime}\right)^{\prime}$. The correspondence between $\Sigma$ and $\boldsymbol{\Sigma}_{11 \cdot 2}, \boldsymbol{\beta}$, and $\boldsymbol{\Sigma}_{22}$ is one-to-one by virtue of (2) and (3) and

$$
\begin{aligned}
& \Sigma_{12}=\beta \Sigma_{22}, \\
& \Sigma_{11}=\Sigma_{11 \cdot 2}+\beta \Sigma_{22} \beta^{\prime} .
\end{aligned}
$$

We can now apply Corollary 3.2.1 to the effect that maximum likelihood estimators of functions of parameters are those functions of the maximum likelihood estimators of those parameters.

Theorem 4.3.1. Let $x_{1}, \ldots, x_{N}$ be a sample from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, where $\boldsymbol{\mu}$ and $\Sigma$ are partitioned as in (1). Define $A$ by (4) and $\left(\bar{x}^{(1) \prime} \bar{x}^{(2) \prime}\right)= (1 / N) \sum_{\alpha=1}^{N}\left(x_{\alpha}^{(1) \prime} x_{\alpha}^{(2) \prime}\right)$. Then the maximum likelihood estimators of $\mu^{(1)} \cdot \mu^{(2)}$. $\mathbf{\beta}, \boldsymbol{\Sigma}_{11 \cdot 2}$, and $\boldsymbol{\Sigma}_{22}$ are $\hat{\boldsymbol{\mu}}^{(1)}=\dot{\boldsymbol{x}}^{(1)}, \hat{\boldsymbol{\mu}}^{(2)}=\overline{\boldsymbol{x}}^{(2)}$,

$$
\hat{\mathbf{B}}=A_{12} A_{22}^{-1}, \quad \hat{\Sigma}_{11 \cdot 2}=\frac{1}{N}\left(A_{11}-A_{12} A_{22}^{-1} A_{21}\right),
$$

and $\hat{\mathbf{\Sigma}}_{22}=(1 / N) A_{22}$, respectively.
In turn, Corollary 3.2.1 can be used to obtain the maximum likelihood estimators of $\boldsymbol{\mu}^{(1)}, \boldsymbol{\mu}^{(2)}, \boldsymbol{\beta}, \boldsymbol{\Sigma}_{22}, \sigma_{11 q+1} ., p^{,} i=1, \ldots, q$. and $\rho_{1, q+1}, \ldots p$, $i, j=1, \ldots, q$. It follows that the maximum likelihood estimators of the partial correlation coefficients are

$$
\hat{\rho}_{\imath, q+1, \ldots, p}=\frac{\hat{\sigma}_{\imath, q+1, . . p}}{\sqrt{\hat{\sigma}_{i \imath \cdot q+1, p} \hat{\sigma}_{\jmath, q+1 \ldots p}}}, \quad \quad i, j=1 \ldots, q .
$$

where $\hat{\sigma}_{\imath \cdot q+1} \ldots, p$ is the $i, j$ th element of $\hat{\mathbf{\Sigma}}_{11 \cdot 2}$.

Theorem 4.3.2. Let $x_{1}, \ldots, x_{N}$ be a sample of $N$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. The maximum likelihood estimators of $\rho_{i r q+1}, \ldots p$, the partial correlations of the first $q$ components conditional on the last $p-q$ components, are given by

$$
\hat{\rho}_{\imath \cdot q+1} \ldots \ldots p=\frac{a_{\imath \cdot q+1}, \ldots, p}{\sqrt{a_{i t \cdot q+1}, \ldots, p} a_{\jmath \cdot q+1, \ldots, p}}, \quad i, j=1, \ldots, q,
$$

where

$$
\left(a_{11 \cdot q+1 .} \quad . p\right)=A_{11}-A_{12} A_{22}^{-1} A_{21}=A_{11 \cdot 2} .
$$

The estimator $\hat{\rho}_{t, q+1, \ldots, p}$, denoted by $r_{1, q+1, \ldots, p}$, is called the sample partial correlation coefficient between $X_{1}$ and $X$, holding $X_{q+1}, \ldots, X_{p}$ fixed. It is also called the sample partial correlation coefficient between $X_{i}$ and $X_{j}$ having taken account of $X_{q+1}, \ldots, X_{p}$. Note that the calculations can be done in terms of ( $r_{t}$ ).

The matrix $\boldsymbol{A}_{11 \cdot 2}$ can also be represented as

$$
\begin{aligned}
\boldsymbol{A}_{11} & =\sum_{\alpha=1}^{N^{\prime}}\left[x_{\alpha}^{(1)}-\bar{x}^{(1)}-\hat{\mathbf{B}}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\right]\left[x_{\alpha}^{(1)}-\bar{x}^{(1)}-\hat{\mathbf{B}}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\right]^{\prime} \\
& =\boldsymbol{A}_{11}-\hat{\mathbf{B}} \boldsymbol{A}_{22} \hat{\mathbf{B}}^{\prime}
\end{aligned}
$$

The vector $x_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}-\hat{\mathbf{B}}\left(x_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)$ is the residual of $x_{\alpha}^{(1)}$ from its regression on $x_{\alpha}^{(2)}$ and 1 . The partial correlations are simple correlations between these residuals. The definition can be used also when the distributions involved are not normal.

Two geometric interpretations of the above theory can be given. In $p$-dimensional space $x_{1}, \ldots, x_{N}$ represent $N$ points. The sample regression function

$$
x^{(1)}=\bar{x}^{(1)}+\hat{\mathbf{B}}\left(x^{(2)}-\bar{x}^{(2)}\right)
$$

is a ( $p-q$ )-dimensional hyperplane which is the intersection of $q(p-1)$ dimensional hyperplanes,

$$
x_{1}=\bar{x}_{1}+\sum_{j=q+1}^{p} \hat{\beta}_{i}\left(x_{j}-\bar{x}_{j}\right), \quad i=1, \ldots, q
$$

where $x_{i}, x$, are running variables. Here $\hat{\beta}_{i j}$ is an element of $\hat{\mathbf{B}}=\hat{\mathbf{\Sigma}}_{12} \hat{\mathbf{\Sigma}}_{22}^{-1}= A_{12} A_{22}^{-1}$. The ith row of $\hat{\mathbf{B}}$ is ( $\hat{\beta}_{1, q+1}, \ldots, \hat{\beta}_{1 p}$ ). Each right-hand side of (13) is the least squares regression function of $x_{1}$ on $x_{q+1}, \ldots, x_{p}$; that is, if we project the points $x_{1}, \ldots, x_{N}$ on the coordinate hyperplane of $x_{i}, x_{q+1}, \ldots, x_{p}$,

![](https://cdn.mathpix.com/cropped/7d03b9cd-db11-46a8-8f85-be81fc52a9c2-157.jpg?height=808&width=1346&top_left_y=236&top_left_x=136)
Figure 4.4

then (13) is the regression plane. The point with coordinates

$$
\begin{array}{rlr}
x_{i}=\bar{x}_{i}+\sum_{j=q+1}^{p} \hat{\beta}_{i j}\left(x_{j \alpha}-\bar{x}_{j}\right), & i=1, \ldots, q, \\
x_{j}=x_{j \alpha}, & j=q+1, \ldots, p,
\end{array}
$$

is on the hyperplane (13). The difference in the $i$ th coordinate of $x_{\alpha}$ and the point (14) is $y_{i \alpha}=x_{i \alpha}-\left[\bar{x}_{i}+\sum_{j=q+1}^{p} \hat{\beta}_{i j}\left(x_{j \alpha}-\bar{x}_{j}\right)\right]$ for $i=1, \ldots, q$ and 0 for the other coordinates. Let $y_{\alpha}^{\prime}=\left(y_{1 \alpha}, \ldots, y_{q \alpha}\right)$. These points can be represented as $N$ points in a $q$-dimensional space. Then $A_{11 \cdot 2}=\sum_{\alpha=1}^{N} y_{\alpha} y_{\alpha}^{\prime}$.

We can also interpret the sample as $p$ points in $N$-space (Figure 4.4). Let $u_{j}=\left(x_{j,}, \ldots, x_{j N}\right)^{\prime}$ be the $j$ th point, and let $\varepsilon=(1, \ldots, 1)^{\prime}$ be another point. The point with coordinates $\bar{x}_{i}, \ldots, \bar{x}_{i}$ is $\bar{x}_{i} \varepsilon$. The projection of $u_{i}$ on the hyperplane spanned by $u_{q+1}, \ldots, u_{p}, \varepsilon$ is

$$
\hat{u}_{i}=\bar{x}_{i} \varepsilon+\sum_{j=q+\mathrm{I}}^{p} \hat{\beta}_{i j}\left(u_{j}-\bar{x}_{j} \varepsilon\right) ;
$$

this is the point on the hyperplane that is at a minimum distance from $u_{i}$. Let $u_{i}^{*}$ be the vector from $\hat{u}_{i}$ to $u_{i}$, that is, $u_{i}-\hat{u}_{i}$, or, equivalently, this vector translated so that one endpoint is at the origin. The set of vectors $u_{1}^{*}, \ldots, u_{q}^{*}$ are the projections of $u_{1}, \ldots, u_{q}$ on the hyperplane orthogonal to
$u_{q+1}, \ldots, u_{p}, \varepsilon$. Then $u_{1}^{* \prime} u_{1}^{*}=a_{w \cdot q+1, \ldots, p}$, the length squared of $u_{i}^{*}$ (i.e., the square of the distance of $u$ from $\hat{u}_{i}$ ). Then $u_{i}^{* \prime} u_{j}^{*} / \sqrt{u_{i}^{* \prime} u_{i}^{*} u_{j}^{* \prime} u_{j}^{*}}=r_{i j \cdot q+1}, \ldots, p$ is the cosine of the angle between $u_{i}^{*}$ and $u_{j}^{*}$.

As an example of the use of partial correlations we consider some data [Hooker (1907)] on yield of hay ( $X_{1}$ ) in hundredweights per acre, spring rainfall ( $X_{2}$ ) in inches, and accumulated temperature above $42^{\circ} \mathrm{F}$ in the spring $\left(X_{3}\right)$ for an English area over 20 years. The estimates of $\mu_{t}, \sigma_{t} \left(=\sqrt{\sigma_{t i}}\right)$, and $\rho_{t j}$ are

$$
\begin{aligned}
\hat{\boldsymbol{\mu}} & =\bar{x}=\left(\begin{array}{c}
28.02 \\
4.91 \\
594
\end{array}\right), \\
\left(\begin{array}{l}
\hat{\sigma}_{1} \\
\hat{\sigma}_{2} \\
\hat{\sigma}_{3}
\end{array}\right) & =\left(\begin{array}{c}
4.42 \\
1.10 \\
85
\end{array}\right), \\
\left(\begin{array}{lll}
1 & \hat{\rho}_{12} & \hat{\rho}_{13} \\
\hat{\rho}_{21} & 1 & \hat{\rho}_{23} \\
\hat{\rho}_{31} & \hat{\rho}_{32} & 1
\end{array}\right) & =\left(\begin{array}{rrr}
1.00 & 0.80 & -0.40 \\
0.80 & 1.00 & -0.56 \\
-0.40 & -0.56 & 1.00
\end{array}\right) .
\end{aligned}
$$

From the correlations we observe that yield and rainfall are positively related, yield and temperature are negatively related, and rainfall and temperature are negatively related. What interpretation is to be given to the apparent negative relation between yield and temperature? Does high temperature tend to cause low yield, or is high temperature associated with low rainfall and hence with low yield? To answer this question we consider the correlation between yield and temperature when rainfall is held fixed; that is, we use the data given above to estimate the partial correlation between $X_{1}$ and $X_{3}$ with $X_{2}$ held fixed. It is ${ }^{\dagger}$

$$
r_{132}=\frac{\hat{\sigma}_{13 \cdot 2}}{\sqrt{\hat{\sigma}_{11 \cdot 2} \hat{\sigma}_{33 \cdot 2}}}=0.097 .
$$

Thus, ' $f$ the effect of rainfall is removed, yield and temperature are positively correlated. The conclusion is that both high raninfall and high temperature increase hay yield, but in most years high rainfall occurs with low temperature and vice versa.

[^0]
### 4.3.2 The Distribution of the Sample Partial Correlation Coefficient

In order to test a hypothesis about a population partial correlation coefficient we want the distribution of the sample partial correlation coefficient. The partial correlations are computed from $A_{11 \cdot 2}=A_{11}-A_{12} A_{22}^{-1} A_{21}$ (as indicated in Theorem 4.3.1) in the same way that correlations are computed from $A$. To obtain the distribution of a simple correlation we showed that $A$ was distributed as $\sum_{a=1}^{N-1} Z_{\alpha} Z_{\alpha}^{\prime}$, where $Z_{1}, \ldots, Z_{N-1}$ are distributed independently according to $N(\mathbf{0}, \Sigma)$ and independent of $\bar{X}$ (Theorem 3.3.2). Here we want to show that $A_{11 \cdot 2}$ is distributed as $\sum_{a=1}^{N-1-(p-q)} U_{a} U_{a}^{\prime}$. where $U_{1:} \ldots, U_{N-1-(p-q)}$ are distributed independently according to $N\left(\mathbf{0}, \Sigma_{11 \cdot 2}\right)$ and independently of $\hat{\mathbf{B}}$. The distribution of a partial correlation coefficient will follow from the characterization of the distribution of $A_{112}$. We state the theorem in a general form; it will be used in Chapter 8, where we treat regression in detail. The following corollary applies it to $A_{11}$, expressed in terms of residuals.

Theorem 4.3.3. Suppose $Y_{1}, \ldots, Y_{m}$ are independent with $Y_{\alpha}$ distributed according to $N\left(\Gamma \boldsymbol{w}_{\alpha}, \boldsymbol{\Phi}\right)$, where $\boldsymbol{w}_{\alpha}$ is an $r$-component vector. Let $\boldsymbol{H}=\sum_{\alpha=1}^{m} \boldsymbol{w}_{\alpha} \boldsymbol{w}_{\alpha}^{\prime}$. assumed nonsingular, $G=\sum_{\alpha=1}^{m} Y_{\alpha} \boldsymbol{w}_{\alpha}^{\prime} \boldsymbol{H}^{-1}$, and

$$
C=\sum_{\alpha=1}^{m}\left(Y_{\alpha}-G w_{\alpha}\right)\left(Y_{\alpha}-G w_{\alpha}\right)^{\prime}=\sum_{\alpha=1}^{m} Y_{\alpha} Y_{\alpha}^{\prime}-G H G^{\prime} .
$$

Then $\boldsymbol{C}$ is distributed as $\sum_{\alpha=1}^{m-r} U_{\alpha} U_{\alpha}^{\prime}$, where $U_{1}, \ldots, U_{m-r}$ are independenth distributed according to $N(\mathbf{0}, \mathbf{\Phi})$ and independently of $G$.

Proof. The rows of $Y=\left(Y_{1}, \ldots, Y_{m}\right)$ are random vectors in an $m$-dimensional space, and the rows of $\boldsymbol{W}=\left(\boldsymbol{w}_{1}, \ldots, \boldsymbol{w}_{m}\right)$ are fixed vectors in that space. The idea of the proof is to rotate coordinate axes so that the last $r$ axes are in the space spanned by the rows of $W$. Let $E_{2}=F W$, where $F$ is a square matrix such that $F H F^{\prime}=I$. Then

$$
\begin{aligned}
E_{2} E_{2}^{\prime} & =F W W^{\prime} F^{\prime}=F \sum_{\alpha=1}^{m} w_{a} w_{\alpha}^{\prime} F^{\prime} \\
& =F H F^{\prime}=I .
\end{aligned}
$$

Thus the $m$-component rows of $E_{2}$ are orthogonal and of unit length. It is possible to find an $(m-r) \times m$ matrix $E_{1}$ such that

$$
E=\binom{E_{1}}{E_{2}}
$$

is orthogoual. (See Appendix, Lemma A.4.2.) Now let $\boldsymbol{U}=\boldsymbol{Y} \boldsymbol{E}^{\prime}$ (i.e., $\boldsymbol{U}_{\alpha}= \left.\sum_{\beta=1}^{m} e_{\alpha \beta} \boldsymbol{Y}_{\beta}\right)$. By Theorem 3.3.1 the columns of $U=\left(U_{1}, \ldots, U_{m}\right)$ are independently and normally distributed, each with covariance matrix $\boldsymbol{\Phi}$. The means are given by

$$
\begin{aligned}
& \mathscr{E} U=\mathscr{E} Y E^{\prime}=\Gamma W E^{\prime} \\
& =\Gamma F^{-1} E_{2}\left(\begin{array}{ll}
E_{1}^{\prime} & E_{2}^{\prime}
\end{array}\right) \\
& =\left(\begin{array}{ll}
0 & \Gamma F^{-1}
\end{array}\right)
\end{aligned}
$$

by orthogonality of $\boldsymbol{E}$. To complete the proof we need to show that $\boldsymbol{C}$ transforms to $\sum_{\alpha=1}^{m-1} U_{\alpha} U_{\alpha}^{\prime}$. We have

$$
\sum_{\alpha=1}^{m} Y_{\alpha} Y_{\alpha}^{\prime}=Y Y^{\prime}=U E E^{\prime} U^{\prime}=U U^{\prime}=\sum_{\alpha=1}^{m} U_{\alpha} U_{\alpha}^{\prime}
$$

Note that

$$
\begin{aligned}
G & =Y W^{\prime} H^{-1}=U E E_{2}^{\prime}\left(F^{-1}\right)^{\prime} F^{\prime} F \\
& =U\binom{E_{1}}{E_{2}} E_{2}^{\prime} F \\
& =U\binom{0}{I} F=U^{(2)} F,
\end{aligned}
$$

where $U^{(2)}=\left(U_{m-r+1}, \ldots, U_{m}\right)$. Then

$$
G H G^{\prime}=U^{(2)} F H F^{\prime} U^{(2) \prime}=U^{(2)} U^{(2) \prime}=\sum_{\alpha=m-r+1}^{m} U_{\alpha} U_{\alpha}^{\prime} .
$$

Thus $\boldsymbol{C}$ is

$$
\sum_{a 1}^{m} Y_{\alpha} Y_{\alpha}^{\prime}-G H G^{\prime}=\sum_{\alpha 1}^{m} U_{\alpha} U_{\alpha}^{\prime}-\sum_{\alpha r-m-r+1}^{m} U_{\alpha} U_{\alpha}^{\prime}=\sum_{\alpha=1}^{m-r} U_{\alpha} U_{\alpha}^{\prime} .
$$

This proves the theorem.
It follows from the above considerations that when $\Gamma=\mathbf{0}$, the $\mathscr{E} U=\mathbf{0}$, and we obtain the following:

Corollary 4.3.1. If $\Gamma=\mathbf{0}$, the matrix GHG $^{\prime}$ defined in Theorem 4.3.3 is distributed as $\sum_{\alpha=m-r+1}^{m} U_{\alpha} U_{\alpha}^{\prime}$, where $U_{m-r+1}, \ldots, U_{m}$ are independently distributed, each according to $N(\mathbf{0}, \mathbf{\Phi})$.


[^0]:    ${ }^{\dagger}$ We compute with $\hat{\Sigma}$ as if it were $\Sigma$.



We now find the distribution of $\boldsymbol{A}_{11 \cdot 2}$ in the same form. It was shown in Theorem 3.3.1 that $\boldsymbol{A}$ is distributed as $\sum_{\alpha=1}^{N-1} \boldsymbol{Z}_{\alpha} \boldsymbol{Z}_{\alpha}^{\prime}$, where $\boldsymbol{Z}_{1}, \ldots, \boldsymbol{Z}_{N-1}$ are independent, each with distribution $N(\mathbf{0}, \mathbf{\Sigma})$. Let $\boldsymbol{Z}_{\alpha}$ be partitioned into two subvectors of $q$ and $p-q$ components, respectively:

$$
Z_{\alpha}=\binom{Z_{\alpha}^{(1)}}{Z_{\alpha}^{(2)}} .
$$

Then $\boldsymbol{A}_{i j}=\sum_{\alpha=1}^{N} \boldsymbol{Z}_{\alpha}^{(i)} \boldsymbol{Z}_{a}^{(1) \prime}$. By Lemma 4.2.1, conditionally on $\boldsymbol{Z}_{1}^{(2)}= z_{1}^{(2)}, \ldots, Z_{N-1}^{(2)}=z_{N-1}^{(2)}$, the random vectors $Z_{1}^{(1)}, \ldots, Z_{N-1}^{(1)}$ are independently distributed, with $\boldsymbol{Z}_{\alpha}^{(1)}$ distributed according to $N\left(\boldsymbol{\beta} z_{\alpha}^{(2)}, \boldsymbol{\Sigma}_{11 \cdot 2}\right)$, where $\boldsymbol{\beta}= \boldsymbol{\Sigma}_{12} \boldsymbol{\Sigma}_{22}^{-1}$ and $\boldsymbol{\Sigma}_{11 \cdot 2}=\boldsymbol{\Sigma}_{11}-\boldsymbol{\Sigma}_{12} \boldsymbol{\Sigma}_{22}^{-1} \boldsymbol{\Sigma}_{21}$. Now we apply Theorem 4.3 .3 with $\boldsymbol{Z}_{\alpha}^{(1)}=\boldsymbol{Y}_{\alpha}, \boldsymbol{Z}_{\alpha}^{(2)}=\boldsymbol{w}_{\alpha}, N-1=m, p-q=r, \boldsymbol{\beta}=\boldsymbol{\Gamma}, \boldsymbol{\Sigma}_{11 \cdot 2}=\boldsymbol{\Phi}, \boldsymbol{A}_{11}=\sum_{\alpha=1}^{N-1} \boldsymbol{Y}_{\alpha} \boldsymbol{Y}_{\alpha}^{i}$, $\boldsymbol{A}_{12} \boldsymbol{A}_{22}^{-\mathrm{I}}=\boldsymbol{G}, \boldsymbol{A}_{22}=\boldsymbol{H}$. We find that the conditional distribution of $\boldsymbol{A}_{11}- \left(A_{12} A_{22}^{-1}\right) A_{22}\left(A_{22}^{-1} A_{12}^{\prime}\right)=A_{11 \cdot 2}$ given $Z_{a}^{(2)}=z_{a}^{(2)}, \alpha=1, \ldots, N-1$, is that of $\sum_{\alpha=1}^{N-1-(p-q)} U_{\alpha} U_{\alpha}^{\prime}$, where $U_{1}, \ldots, U_{N-1-(p-q)}$ are independent, each with distribution $N\left(\mathbf{0}, \Sigma_{11-2}\right)$. Since this distribution does not depend on $\left\{z_{\alpha}^{(2)}\right\}$, we obtain the following theorem:

Theorem 4.3.4. The matrix $A_{112}=A_{11}-A_{12} A_{22}^{-1} A_{21}$ is distributed as $\sum_{\alpha=1}^{N-1-(p-q)} U_{\alpha} U_{\alpha}^{r}$, where $U_{1}, \ldots, U_{N-1-(p-q)}$ are independently distributed, each according to $N\left(\mathbf{0}, \boldsymbol{\Sigma}_{11 \cdot 2}\right)$, and independently of $\boldsymbol{A}_{12}$ and $\boldsymbol{A}_{22}$.

Corollary 4.3.2. If $\Sigma_{12}=0 \quad(\mathbf{B}=0)$, then $\boldsymbol{A}_{11 \cdot 2}$ is distributed as $\sum_{\alpha=1}^{\Lambda-1-(p-q)} U_{\alpha} U_{\alpha}^{\prime}$ and $A_{12} A_{22}^{-1} A_{21}$ is distributed as $\sum_{\alpha=N-(p-q)}^{N-1} U_{\alpha} U_{\alpha}^{\prime}$, where $U_{1}, \ldots, U_{N-1}$ are independently distributed, each according to $N\left(\mathbf{0}, \Sigma_{11 \cdot 2}\right)$.

Now it follows that the distribution of $r_{i j q+1, \ldots . p}$ based on $N$ observations is the same as that of a simple correlation coefficient based on $N-(p-q)$ observations with a corresponding population correlation value of $\rho_{\mathrm{i} / q+1, \ldots, p^{\circ}, \ldots}$

Theorem 4.3.5. If the edf of $r_{i j}$ based on a sample of $N$ from a normal distribution with correlation $\rho_{i j}$ is denoted by $F\left(r \mid N, \rho_{i j}\right)$, then the cdf of the sample partial correlation $r_{11} q+1$, ... based on a sample of $N$ from a normal distribution with partial correlation coefficient $\rho_{i j, q+1}, \ldots$, is $\boldsymbol{F}[\boldsymbol{r} \mid \boldsymbol{N}- \left.(p-q), \rho_{i f q+1}, \ldots, p\right]$.

This distribution was derived by Fisher (1924).

### 4.3.3. Tests of Hypotheses and Confidence Regions for Partial Correlation Coefficients

Since the distribution of a sample partial correlation $r_{t / q+I_{1} \ldots, p}$ based on a sample of $N$ from a distribution with population correlation $\rho_{i f \cdot q+1}, \ldots, \rho$
equal to a certain value, $\rho$, say, is the same as the distribution of a simple correlation $r$ based on a sample of size $N-(p-q)$ from a distribution with the corresponding population correlation of $\rho$, all statistical inference procedures for the simple population correlation can be used for the partial correlation. The procedure for the partial correlation is exactly the same except that $N$ is replaced by $N-(p-q)$. To illustrate this rule we give two examples.

Example 1. Suppose that on the basis of a sample of size $N$ we wish to obtain a confidence interval for $\rho_{i j q+1, \ldots, p}$. The sample partial correlation is $r_{i j, q+1, \ldots, p}$. The procedure is to use David's charts for $N-(p-q)$. In the example at the end of Section 4.3.1, we might want to find a confidence interval for $\rho_{12 \cdot 3}$ with confidence coefficient 0.95 . The sample partial correlation is $r_{12 \cdot 3}=0.759$. We use the chart (or table) for $N-(p-q)=20-1=19$. The interval is $0.50<\rho_{12 \cdot 3}<0.88$.

Example 2. Suppose that on the basis of a sample of size $N$ we use Fisher's $z$ for an approximate significance test of $\rho_{i j \cdot q+1, \ldots, p}=\rho_{0}$ against two-sided alternatives. We let

$$
\begin{aligned}
z & =\frac{1}{2} \log \frac{1+r_{i j \cdot q+1, \ldots, p}}{1-r_{i j \cdot q+1, \ldots, p}}, \\
\zeta_{0} & =\frac{1}{2} \log \frac{1+\rho_{0}}{1-\rho_{0}} .
\end{aligned}
$$

Then $\sqrt{N-(p-q)-3}\left(z-\zeta_{0}\right)$ is compared with the significance points of the standardized normal distribution. In the example at the end of Section 4.3.1, we might wish to test the hypothesis $\rho_{13 \cdot 2}=0$ at the 0.05 level. Then $\zeta_{0}=0$ and $\sqrt{20-1-3}(0.0973)=0.3892$. This value is clearly nonsignificant ( $|0.3892|<1.96$ ), and hence the data do not indicate rejection of the null hypothesis.

To answer the question whether two variables $x_{1}$ and $x_{2}$ are related when both may be related to a vector $x^{(2)}=\left(x_{3}, \ldots, x_{p}\right)$, two approaches may be used. One is to consider the regression of $x_{1}$ on $x_{2}$ and $x^{(2)}$ and test whether the regression of $x_{1}$ on $x_{2}$ is 0 . Another is $t$ ) test whether $\rho_{12 \cdot 3, \ldots, p}=0$. Problems 4.43-4.47 show that these approaches lead to exactly the same test.

### 4.4. THE MULTIPLE CORRELATION COEFFICIENT

### 4.4.1. Estimation of the Multiple Correlation Coefficient

The population multiple correlation between one variate and a set of variates was defined in Section 2.5. For the sake of convenience in this section we shall treat the case of the multiple correlation between $X_{1}$ and the vector
$X^{(2)}=\left(X_{2}, \ldots, X_{p}\right)^{\prime}$; we shall not need subscripts on $R$. The variables can always be numbered so that the desired multiple correlation is this one (any irrelevant variables being omitted). Then the multiple correlation in the population is

$$
\bar{R}=\frac{\beta^{\prime} \Sigma_{22} \beta}{\sqrt{\sigma_{11} \beta^{\prime} \Sigma_{22} \beta}}=\sqrt{\frac{\beta^{\prime} \Sigma_{22} \beta}{\sigma_{11}}}=\sqrt{\frac{\sigma_{(1)}^{\prime} \Sigma_{22}^{-1} \sigma_{(1)}}{\sigma_{11}}},
$$

where $\boldsymbol{\beta}, \boldsymbol{\sigma}_{(1)}$, and $\boldsymbol{\Sigma}_{22}$ are defined by

$$
\begin{aligned}
& \Sigma=\left(\begin{array}{ll}
\sigma_{\mathrm{I} 1} & \sigma_{(1)}^{\prime} \\
\sigma_{(\mathrm{I})} & \Sigma_{22}
\end{array}\right), \\
& \boldsymbol{\beta}=\Sigma_{22}^{-\mathrm{I}} \sigma_{(\mathrm{I})} .
\end{aligned}
$$

Given a sample $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}(N>p)$, we cstimate $\boldsymbol{\Sigma}$ by $\boldsymbol{S}=[N /(N-1)] \hat{\boldsymbol{\Sigma}}$ or

$$
\hat{\boldsymbol{\Sigma}}=\frac{1}{N} \boldsymbol{A}=\frac{1}{N} \sum_{\boldsymbol{\alpha}=\mathbf{I}}^{N}\left(\boldsymbol{x}_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}=\left(\begin{array}{ll}
\hat{\sigma}_{11} & \hat{\boldsymbol{\sigma}}_{(1)}^{\prime} \\
\hat{\boldsymbol{\sigma}}_{(1)} & \hat{\boldsymbol{\Sigma}}_{22}
\end{array}\right),
$$

and we estimate $\boldsymbol{\beta}$ by $\hat{\boldsymbol{\beta}}=\hat{\boldsymbol{\Sigma}}_{22}^{-1} \hat{\boldsymbol{\sigma}}_{(1)}=A_{22}^{-1} a_{(1)}$. We define the sample multiple correlation coefficient by

$$
R=\sqrt{\frac{\hat{\boldsymbol{\beta}}^{\prime} \hat{\boldsymbol{\Sigma}}_{22} \hat{\boldsymbol{\beta}}}{\hat{\boldsymbol{\sigma}}_{11}}}=\sqrt{\frac{\hat{\boldsymbol{\sigma}}_{(1)}^{\prime} \hat{\boldsymbol{\Sigma}}_{22}^{-1} \hat{\boldsymbol{\sigma}}_{(1)}}{\hat{\sigma}_{11}}}=\sqrt{\frac{a_{(11}^{\prime} A_{22}^{-1} a_{(1)}}{a_{11}}} .
$$

That this is the maximum likelihood estimator of $\bar{R}$ is justified by Corollary 3.2.1, since we can define $\bar{R}, \boldsymbol{\sigma}_{(1)}, \Sigma_{22}$ as a one-to-one transformation of $\Sigma$. Another expression for $R$ [sce (16) of Section 2.5] follows from

$$
1-R^{2}=\frac{|\hat{\Sigma}|}{\hat{\sigma}_{11}\left|\hat{\Sigma}_{22}\right|}=\frac{|A|}{a_{11}\left|A_{22}\right|} .
$$

The quantities $R$ and $\hat{\boldsymbol{\beta}}$ have properties in the sample that are similar to those $\bar{R}$ and $\boldsymbol{\beta}$ have in the population. We have analogs of Theorems 2.5.2, 2.5.3, and 2.5.4. Let $\hat{x}_{1 \alpha}=\bar{x}_{1}+\hat{\boldsymbol{\beta}}^{\prime}\left(\boldsymbol{x}_{\alpha}^{(2)}-\bar{x}^{(2)}\right)$, and $x_{1 \alpha}^{*}=x_{1 \alpha}-\hat{x}_{1 \alpha}$ be the residual.

Theorem 4.4.1. The residuals $x_{1 \alpha}^{*}$ are uncorrelated in the sample with the components of $\boldsymbol{x}_{\alpha}^{(2)}, \alpha=1, \ldots, N$. For every vector a
(7) $\sum_{\alpha=1}^{N}\left[x_{1 \alpha}-\bar{x}_{1}-\hat{\boldsymbol{\beta}}^{\prime}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\right]^{2} \leq \sum_{\alpha=1}^{N}\left[x_{1 \alpha}-\bar{x}_{1}-a^{\prime}\left(x_{n}^{(2)}-\bar{x}^{(2)}\right)\right]^{2}$.

The sample correlation berween $x_{1 \alpha}$ and $a^{\prime} x_{\alpha}^{(2)}, \alpha=1, \ldots, N$, is maximized for $\boldsymbol{a}=\hat{\boldsymbol{\beta}}$. and that maximum correlation is $R$.

Proof. Since the sample mean of the residuals is 0 , the vector of sample covariances between $x_{1 \alpha}^{*}$ and $x_{0}^{(2)}$ is proportional to
(8) $\sum_{\alpha=1}^{X}\left[\left(x_{1 \alpha}-\bar{x}_{1}\right)-\hat{\boldsymbol{\beta}}^{\prime}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\right]\left(x_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)^{\prime}=\boldsymbol{a}_{(1)}^{\prime}-\hat{\boldsymbol{\beta}}^{\prime} \boldsymbol{A}_{22}=\mathbf{0}$.

The right-hand side of (7) can be written as the left-hand side plus

$$
\begin{aligned}
& \sum_{\alpha=1}^{N}\left[(\hat{\boldsymbol{\beta}}-a)^{\prime}\left(x_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)\right]^{2} \\
& \quad=(\hat{\boldsymbol{\beta}}-a)^{\prime} \sum_{\alpha=1}^{N}\left(x_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)\left(\boldsymbol{x}_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)^{\prime}(\hat{\boldsymbol{\beta}}-a)
\end{aligned}
$$

which is 0 if and only if $a=\hat{\boldsymbol{\beta}}$. To prove the third assertion we consides the vector $a$ for which $\sum_{\alpha=1}^{N}\left[a^{\prime}\left(x_{\alpha}^{(2)}-\tilde{x}^{(2)}\right)\right]^{2}=\sum_{\alpha=1}^{N}\left[\hat{\boldsymbol{\beta}}^{\prime}\left(x_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)\right]^{2}$, since the correlation is unchanged when the linear function is mulitplied by a positive constant. From (7) we obtain

$$
\begin{aligned}
a_{11} & -2 \sum_{\alpha=1}^{N}\left(x_{1 \alpha}-\bar{x}_{1}\right) \hat{\boldsymbol{\beta}}^{\prime}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)+\sum_{\alpha=1}^{N}\left[\hat{\boldsymbol{\beta}}^{\prime}\left(\boldsymbol{x}_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\right]^{2} \\
& \leq a_{11}-2 \sum_{\alpha=1}^{N}\left(x_{1 \alpha}-\overline{\boldsymbol{x}}_{1}\right) a^{\prime}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)+\sum_{\alpha=1}^{N}\left[a^{\prime}\left(\boldsymbol{x}_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)\right]^{2}
\end{aligned}
$$

from which we deduce
(11) $\frac{\sum_{\alpha=1}^{N}\left(x_{1 \mathrm{n}}-\bar{x}_{1}\right)\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)^{\prime} a}{\sqrt{a_{11}} \sqrt{\sum_{\alpha=1}^{Y}\left[a^{\prime}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\right]^{2}}} \leq \frac{\sum_{\alpha=1}^{N}\left(x_{1 \alpha}-\bar{x}_{1}\right)\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)^{\prime} \hat{\boldsymbol{\beta}}}{\sqrt{a_{11}} \sqrt{\sum_{\alpha=1}^{N}\left[\hat{\boldsymbol{\beta}}^{\prime}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\right]^{2}}}$

$$
=-\frac{a_{(1)}^{\prime} \hat{\boldsymbol{\beta}}}{\sqrt{a_{11}} \sqrt{\hat{\boldsymbol{\beta}}^{\prime} \boldsymbol{A}_{22} \hat{\boldsymbol{\beta}}}},
$$

which is (5).
Thus $\bar{x}_{1}+\hat{\boldsymbol{\beta}}^{\prime}\left(\boldsymbol{x}_{u}^{(2)}-\bar{x}^{(2)}\right)$ is the best linear predictor of $x_{1 \alpha}$ in the sample, and $\hat{\boldsymbol{\beta}}^{\prime} x_{\alpha}^{(2)}$ is the linear function of $x_{\alpha}^{(2)}$ that has naximum sample correlation
with $x_{1 a}$. The minimum sum of squares of deviations [the left-hand side of (7)] is

$$
\begin{aligned}
\sum_{\alpha=1}^{N}\left[\left(x_{1 \alpha}-\bar{x}_{1}\right)-\hat{\boldsymbol{\beta}}^{\prime}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\right]^{2} & =a_{11}-\hat{\boldsymbol{\beta}}^{\prime} A_{22} \hat{\boldsymbol{\beta}} \\
& =a_{11}-a_{(1)}^{\prime} A_{22}^{-1} a_{(1)} \\
& =a_{11 \cdot 2}
\end{aligned}
$$

as defined in Section 4.3 with $q=1$. The maximum likelihood estimator of $\sigma_{\mathrm{II} \cdot 2}$ is $\hat{\sigma}_{1 \mathrm{I} \cdot 2}=a_{11 \cdot 2} / N$. It follows that

$$
\hat{\sigma}_{11 \cdot 2}=\left(1-R^{2}\right) \hat{\sigma}_{11} .
$$

Thus $1-R^{2}$ measures the proportional reduction in the variance by using residuals. We can say that $R^{2}$ is the fraction of the variance explained by $\boldsymbol{x}^{(2)}$. The larger $R^{2}$ is, the more the variance is decreased by use of the explanatory variables in $\boldsymbol{x}^{(2)}$.

In $p$-dimensional space $x_{1}, \ldots, x_{N}$ represent $N$ points. The sample regression function $x_{1}=\overline{\boldsymbol{x}}_{1}+\hat{\boldsymbol{\beta}}^{\prime}\left(\boldsymbol{x}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)$ is the ( $p-1$ )-dimensional hyperplane that minimizes the squared deviations of the points from the hyperplane, the deviations being calculated in the $x_{1}$-direction. The hyperplane goes through the point $\bar{x}$.

In $N$-dimensional space the rows of $\left(x_{1}, \ldots, x_{N}\right)$ represent $p$ points. The $N$-component vector with $\alpha$ th component $x_{i \alpha}-\bar{x}_{t}$ is the projection of the vector with $\alpha$ th component $x_{1 \alpha}$ on the plane orthogonal to the equiangular line. We have $p$ such vectors; $a^{\prime}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)$ is the $\alpha$ th component of a vector in the hyperplane spanned by the last $p-1$ vectors. Since the right-hand side of (7) is the squared distance between the first vector and the linear combination of the last $p-1$ vectors, $\hat{\boldsymbol{\beta}}^{\prime}\left(\boldsymbol{x}_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)$ is a component of the vector which minimizes this squared distance. The interpretation of (8) is that the vector with $\alpha$ th component ( $\left.x_{1 \alpha}-\bar{x}_{1}\right)-\hat{\boldsymbol{\beta}}^{\prime}\left(\boldsymbol{x}_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)$ is orthogonal to each of the last $p-1$ vectors. Thus the vector with $\alpha$ th component $\hat{\boldsymbol{\beta}}^{\prime}\left(\boldsymbol{x}_{\alpha}^{(2)}-\right. \bar{x}^{(2)}$ ) is the projection of the first vector on the hyperplane. See Figure 4.5. The length squared of the projection vector is

$$
\sum_{\alpha=1}^{N}\left[\hat{\boldsymbol{\beta}}^{\prime}\left(\boldsymbol{x}_{\alpha}^{(2)}-\overline{\boldsymbol{x}}^{(2)}\right)\right]^{2}=\hat{\boldsymbol{\beta}}^{\prime} \boldsymbol{A}_{22} \hat{\boldsymbol{\beta}}=a_{(1)}^{\prime} \boldsymbol{A}_{22}^{-1} a_{(1)},
$$

and the length squared of the first vector is $\sum_{\alpha=1}^{N}\left(x_{1 \alpha}-\bar{x}_{1}\right)^{2}=a_{11}$. Thus $R$ is the cosine of the angle between the first vector and its projection.

![](https://cdn.mathpix.com/cropped/f0976b51-978a-43b6-8018-468529dca235-166.jpg?height=642&width=1007&top_left_y=230&top_left_x=305)
Figure 4.5

In Section 3.2 we saw that the simple correlation coefficient is the cosine of the angle between the two vectors involved (in the plane orthogonal to the equiangular line). The property of $R$ that it is the maximum correlation between $x_{\mathrm{I} \alpha}$ and linear combinations of the components of $x_{\alpha}^{(2)}$ corresponds to the geometric property that $R$ is the cosine of the smallest angle between the vector with components $x_{1 \alpha}-\bar{x}_{\mathrm{j}}$ and a vector in the hyperplane spanned by the other $p-1$ vectors.

The geometric interpretations are in terms of the vectors in the ( $N-1$ )dimensional hyperplane orthogonal to the equiangular line. It was shown in Section 3.3 that the vector ( $x_{i \mathbf{1}}-\bar{x}_{i}, \ldots, x_{i N}-\bar{x}_{i}$ ) in this hyperplane can be designated as $\left(z_{i 1}, \ldots, z_{i, N-1}\right)$, where the $z_{i \alpha}$ are the coordinates referred to an $(N-1)$-dimensional coordinate system in the hyperplane. It was shown that the new coordinates are obtained from the old by the transformation $z_{i \alpha}=\sum_{\beta=1}^{N} b_{\alpha \beta} x_{i \beta}, \alpha=1, \ldots, N$, where $\boldsymbol{B}=\left(b_{\alpha \beta}\right)$ is an orthogonal matrix with last row $(1 / \sqrt{N}, \ldots, 1 / \sqrt{N})$. Then

$$
a_{i j}=\sum_{\alpha=1}^{N}\left(x_{i \alpha}-\bar{x}_{i}\right)\left(x_{j \alpha}-\bar{x}_{j}\right)=\sum_{\alpha=1}^{N-1} z_{i \alpha} z_{j \alpha} .
$$

It will be convenient to refer to the multiple correlatior defined in terms of $z_{i \alpha}$ as the multiple correlation without subtracting the means.

The population multiple correlation $\bar{R}$ is essentially the only function of the parameters $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ that is invariant under changes of location, changes of scale of $X_{1}$, and nonsingular linear transformations of $X^{(2)}$, that is, transformations $X_{1}^{*}=c X_{1}+d, X^{(2) *}=C X^{(2)}+d$. Similarly, the sample multiple correlation coefficient $R$ is essentially the only function of $\bar{x}$ and $\hat{\Sigma}$, the
sufficient set of statistics for $\mu$ and $\sum$, that is invariant under these transformations. Just as the simple correlation $r$ is a measure of association between two scalar variables in a sample, the multiple correlation $R$ is a measure of association between a scalar variable and a vector variable in a sample.

### 4.4.2. Distribution of the Sample Multiple Correlation Coefficient When the Population Multiple Correlation Coefficient Is Zero

From (5) we have

$$
R^{2}=\frac{a_{(1)}^{\prime} A_{22}^{-1} a_{(1)}}{a_{11}} ;
$$

then

$$
1-R^{2}=1-\frac{a_{(1)}^{\prime} A_{22}^{-1} a_{(1)}}{a_{11}}=\frac{a_{11}-a_{(1)}^{\prime} A_{22}^{-1} a_{(1)}}{a_{11}}=\frac{a_{11} \div}{a_{11}} .
$$

and

$$
\frac{R^{2}}{1-R^{2}}=\frac{a_{(1)}^{\prime} A_{22}^{-1} a_{(1)}}{a_{11} 2} .
$$

For $q=1$, Corollary 4.3.2 states that when $\boldsymbol{\beta}=\mathbf{0}$, that is, when $\bar{R}=0 . a_{11}$, is distributed as $\sum_{\alpha=1}^{N-p} V_{\alpha}^{2}$ and $a_{(1)}^{\prime} A_{22}^{-1} a_{(1)}$ is distributed as $\sum_{\alpha=N-p+1}^{N-1} V_{\alpha}^{\prime}$. where $V_{\mathrm{I}}, \ldots, V_{N-1}$ are independent, each with distribution $N\left(0, \sigma_{112}\right)$. Then $a_{11 \cdot 2} / \sigma_{11 \cdot 2}$ and $a_{(1)}^{\prime} A_{22}^{-1} a_{(1)} / \sigma_{112}$ are distributed independently as $x^{2}$-variables with $N-p$ and $p-1$ degrees of freedom, respectively. Thus

$$
\begin{aligned}
\frac{R^{2}}{1-R^{2}} \cdot \frac{N-p}{p-1} & =\frac{a_{(1)}^{\prime} A_{22}^{-1} a_{(1)} / \sigma_{11,2}}{a_{112} / \sigma_{112}} \cdot \frac{N-p}{p-1} \\
& =\frac{\chi_{p-1}^{2}}{\chi_{N-p}^{2}} \cdot \frac{N-p}{p-1} \\
& =F_{p-1,1-p}
\end{aligned}
$$

has the $F$-distribution with $p-1$ and $N-p$ degrees of freedom. The density of $F$ is

$$
\frac{\Gamma\left[\frac{1}{2}(N-1)\right]}{\Gamma\left[\frac{1}{2}(p-1)\right] \Gamma\left[\frac{1}{2}(N-p)\right]}\left(\frac{p-1}{N-p}\right)^{\frac{1}{4}(p-1)} f^{\frac{1}{4}(p-1)-1}\left(1+\frac{p-1}{N-p} f\right)^{-\frac{1}{2}(N-1)} .
$$

Thus the density of

$$
R=\sqrt{\frac{\frac{p-1}{N-p} F_{p-1, N-p}}{1+\frac{p-1}{N-p} F_{p-1, N-p}}}
$$

is

$$
2 \frac{\Gamma\left[\frac{1}{2}(N-1)\right]}{\Gamma\left[\frac{1}{2}(p-1)\right] \Gamma\left[\frac{1}{2}(N-p)\right]} R^{p-2}\left(1-R^{2}\right)^{\frac{1}{2}(N-p)-1}, \quad 0 \leq R \leq 1 .
$$

Theorem 4.4.2. L.et $R$ be the sample multiple correlation coefficient [defined by (5)] between $X_{1}$ and $X^{(2) \prime}=\left(X_{2}, \ldots, X_{p}\right)$ based on a sample of $N$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. If $\bar{R}=0\left[\right.$ that is, if $\left.\left(\sigma_{12}, \ldots, \sigma_{1 p}\right)^{\prime}=\mathbf{0}=\boldsymbol{\beta}\right]$, then $\left[R^{2} /\left(1-R^{2}\right)\right]$. $[(N-p) /(p-1)]$ is distributed as $F$ with $p-1$ and $N-p$ degrees of freedom.

It should be noticed that $p-1$ is the number of components of $X^{(2)}$ and that $N-p=N-(p-1)-1$. If the multiple correlation is between a component $X$, and $q$ other components, the numbers are $q$ and $N-q-1$.

It might be observed that $R^{2} /\left(1-R^{2}\right)$ is the quantity that arises in regression (or least squares) theory for testing the hypothesis that the regression of $X_{1}$ on $X_{2}, \ldots, X_{p}$ is zero.

If $\bar{R} \neq 0$, the distribution of $R$ is much more difficult to derive. This distribution will be obtained in Section 4.4.3.

Now let us consider the statistical problem of testing the hypothesis $H: \bar{R}=0$ on the basis of a sample of $N$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. [ $\bar{R}$ is the population multiple correlation between $X_{1}$ and $\left(X_{2}, \ldots, X_{p}\right)$.] Since $\bar{R} \geq 0$, the alternatives considered are $\bar{R}>0$.

Let us derive the likelihood ratio test of this hypothesis. The likelihood function is

$$
L\left(\mu^{*} \cdot \Sigma^{*}\right)=\frac{1}{(2 \pi)^{\frac{1}{2} p N}\left|\Sigma^{*}\right|^{\frac{1}{2} N}} \exp \left[-\frac{1}{2} \sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu^{*}\right)^{\prime} \Sigma^{*-1}\left(x_{\alpha}-\mu^{*}\right)\right]
$$

The observations are given; $L$ is a function of the indeterminates $\boldsymbol{\mu}^{*}, \boldsymbol{\Sigma}^{*}$. Let $\omega$ be the region in the parameter space $\Omega$ specified by the null hypothesis. The likelihood ratio criterion is

$$
\lambda=\frac{\max _{\boldsymbol{\mu}^{*}, \boldsymbol{\Sigma}^{*} \in \omega} L\left(\boldsymbol{\mu}^{*}, \boldsymbol{\Sigma}^{*}\right)}{\max _{\boldsymbol{\mu}^{*}, \boldsymbol{\Sigma}^{*} \in \Omega} L\left(\boldsymbol{\mu}^{*}, \boldsymbol{\Sigma}^{*}\right)}
$$

Here $\Omega$ is the space of $\mu^{*}, \Sigma^{*}$ positive definite, and $\omega$ is the region in this space where $\bar{R}=\sqrt{\sigma_{(1)}^{\prime} \Sigma_{22}^{-1}} \overline{\sigma_{(1)}} / \sqrt{\sigma_{11}}=0$, that is, where $\sigma_{(1)}^{\prime} \Sigma_{22}^{-1} \sigma_{(1)}=0$. Because $\boldsymbol{\Sigma}_{22}^{-1}$ is positive definite, this condition is equivalent to $\boldsymbol{\sigma}_{(1)}=\mathbf{0}$. The maximum of $L\left(\boldsymbol{\mu}^{\boldsymbol{*}}, \boldsymbol{\Sigma}^{\boldsymbol{*}}\right)$ over $\Omega$ occurs at $\boldsymbol{\mu}^{\boldsymbol{*}}=\hat{\boldsymbol{\mu}}=\overline{\boldsymbol{x}}$ and $\boldsymbol{\Sigma}^{\boldsymbol{*}}=\hat{\boldsymbol{\Sigma}}=(1 / N) \boldsymbol{A} =(1 / N) \sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}$ and is

$$
\max _{\mu^{*}, \Sigma^{*} \in \Omega} L\left(\mu^{*}, \Sigma^{*}\right)=\frac{N^{-\frac{1}{2} p N} e^{\frac{1}{2} p N}}{(2 \pi)^{\frac{1}{2} p N}|A|^{\frac{1}{2} N}} .
$$

In $\omega$ the likelihood function is

$$
\begin{aligned}
& L\left(\boldsymbol{\mu}^{*}, \Sigma^{*} \mid \boldsymbol{\sigma}_{(1)}^{*}=\mathbf{0}\right)=\frac{1}{(2 \pi)^{\frac{1}{2} N} \sigma_{11}^{* \frac{1}{2} N}} \exp \left[-\frac{1}{2} \sum_{\alpha=1}^{N}\left(x_{1 \alpha}-\mu_{1}^{*}\right)^{2} / \sigma_{11}^{*}\right] \\
& \cdot \frac{1}{(2 \pi)^{\frac{1}{2}(p-1) N}\left|\Sigma_{22}^{*}\right|^{\frac{1}{2} N}} \exp \left[-\frac{1}{2} \sum_{\alpha=1}^{N}\left(\boldsymbol{x}_{\alpha}^{(2)}-\mu^{(2) *}\right)^{\prime} \Sigma_{22}^{*-1}\left(\boldsymbol{x}_{\alpha}^{(2)}-\mu^{(2) *}\right)\right] .
\end{aligned}
$$

The first factor is maximized at $\mu_{1}^{*}=\hat{\mu}_{1}=\bar{x}_{1}$ and $\sigma_{11}^{*}=\sigma_{11}^{*}=(1 / N) a_{11}$, and the second factor is maximized at $\boldsymbol{\mu}^{(2) *}=\hat{\boldsymbol{\mu}}^{(2)}=\tilde{\boldsymbol{x}}^{(2)}$ and $\boldsymbol{\Sigma}_{22}^{*}=\hat{\boldsymbol{\Sigma}}_{22}= (1 / N) \boldsymbol{A}_{22}$. The value of the maximized function is

$$
\max _{\mu^{*}, \Sigma^{*} \in \omega} L\left(\mu^{*}, \Sigma^{*}\right)=\frac{N^{\frac{1}{2} N} e^{-\frac{1}{2} N}}{(2 \pi)^{\frac{1}{2} N} a_{11}^{\frac{1}{2} N}} \cdot \frac{N^{\frac{1}{2}(p-1) N} e^{-\frac{1}{2}(p-1) N}}{(2 \pi)^{\frac{1}{2}(p-1) N}\left|A_{22}\right|^{\frac{1}{2} N}} .
$$

Thus the likelihood ratio criterion is [see (6)]

$$
\lambda=\frac{|A|^{\frac{1}{2} N}}{a_{11}^{\frac{1}{2} N}\left|A_{22}\right|^{\frac{1}{2} N}}=\left(1-R^{2}\right)^{\frac{1}{2} N} .
$$

The likelihood ratio test consists of the critical region $\lambda<\lambda_{0}$, where $\lambda_{0}$ is chosen so the probability of this inequality when $\bar{R}=0$ is the significance level $\alpha$. An equivalent test is

$$
1-\lambda^{2 / N}=R^{2}>1-\lambda_{0}^{2 / N} .
$$

Since $\left[R^{2} /\left(1-R^{2}\right)\right][(N-p) /(p-1)]$ is a monotonic function of $R$, an equivalent test involves this ratio being larger than a constant. When $\bar{R}=0$, this ratio has an $F_{p-1, N-p}$-distribution. Hence, the critical region is

$$
\frac{R^{2}}{1-R^{2}} \cdot \frac{N-p}{p-1}>F_{p-1, N-p}(\alpha),
$$

where $F_{p-I, N-p}(\alpha)$ is the (upper) significance point corresponding to the $\alpha$ significance level.

Theorem 4.4.3. Given a sample $\boldsymbol{x}_{\mathbf{I}}, \ldots, \boldsymbol{x}_{N}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, the likelihood ratio test at significance level $\alpha$ for the hypothesis $\bar{R}=0$, where $\bar{R}$ is the population multiple correlation coefficient between $X_{1}$ and $\left(X_{2}, \ldots, X_{p}\right)$, is given by (30), where $R$ is the sample multiple correlation coefficient defined by (5).

As an example consider the data given at the end of Section 4.3.1. The sample multiple correlation coefficient is found from

$$
1-R^{2}=\frac{\left|\begin{array}{ccc}
1 & r_{12} & r_{13} \\
r_{21} & 1 & r_{23} \\
r_{31} & r_{32} & 1
\end{array}\right|}{\left|\begin{array}{cc}
1 & r_{23} \\
r_{32} & 1
\end{array}\right|}=\frac{\left|\begin{array}{rrr}
1.00 & 0.80 & -0.40 \\
0.80 & 1.00 & -0.56 \\
-0.40 & -0.56 & 1.00
\end{array}\right|}{\left|\begin{array}{rr}
1.00 & -0.56 \\
-0.56 & 1.00
\end{array}\right|}=0.357 .
$$

Thus $R$ is 0.802 . If we wish to test the hypothesis at the 0.01 level that hay yield is independent of spring rainfall and temperature, we compare the observed $\left[R^{2} /\left(1-R^{2}\right)\right][(20-3) /(3-1)]=15.3$ with $F_{2,17}(0.01)=6.11$ and find the result significant; that is, we reject the null hypothesis.

The test of independence between $X_{1}$ and $\left(X_{2}, \ldots, X_{p}\right)=\boldsymbol{X}^{(2) \prime}$ is equivalent to the test that if the regression of $X_{1}$ on $\boldsymbol{x}^{(2)}$ (that is, the conditional expected value of $X_{1}$ given $X_{2}=x_{2}, \ldots, X_{p}=x_{p}$ ) is $\mu_{1}+\boldsymbol{\beta}^{\prime}\left(\boldsymbol{x}^{(2)}-\boldsymbol{\mu}^{(2)}\right)$, the vector of regression coefficients is $\mathbf{0}$. Here $\hat{\boldsymbol{\beta}}=\boldsymbol{A}_{22}^{-\mathbf{I}} a_{(\mathbf{I})}$ is the usual least squares estimate of $\boldsymbol{\beta}$ with expected value $\boldsymbol{\beta}$ and covariance matrix $\sigma_{\text {II }-2} A_{22}^{-1}$ (when the $\boldsymbol{X}_{\alpha}^{(2)}$ are fixed), and $a_{11 \cdot 2} /(N-p)$ is the usual estimate of $\sigma_{11 \cdot 2}$. Thus [see (18)]

$$
\frac{R^{2}}{1-R^{2}} \cdot \frac{N-p}{p-1}=\frac{\hat{\boldsymbol{\beta}}^{\prime} \boldsymbol{A}_{22} \hat{\boldsymbol{\beta}}}{a_{1 \mathrm{I} \cdot 2}} \cdot \frac{N-p}{p-1}
$$

is the usual $F$-statistic for testing the hypothesis that the regression of $X_{\mathrm{I}}$ on $x_{2}, \ldots, x_{p}$ is 0 . In this book we are primarily interested in the multiple correlation coefficient as a measure of association between one variable and a vector of variables when both are random. We shall not treat problems of univariate regression. In Chapter 8 we study regression when the dependent variable is a vector.

## Adjusted Multiple Correlation Coefficient

The expression (17) is the ratio of $a_{\mathrm{II} \cdot 2}$, the sum of squared deviations from the fitted regression, to $a_{11}$, the sum of squared deviations around the mean. To obtain unbiased estimators of $\sigma_{11}$ when $\boldsymbol{\beta}=\mathbf{0}$ we would divide these quantities by their numbers of degrees of freedom, $N-p$ and $N-1$,



respectively. Accordingly we can define an adjusted multiple correlation coefficient $R^{*}$ by

$$
1-R^{* 2}=\frac{a_{11 \cdot 2} /(N-p)}{a_{11} /(N-1)}=\frac{N-1}{N-p}\left(1-R^{\prime}\right),
$$

which is equivalent to

$$
R^{* 2}=R^{2}-\frac{p-1}{N-p}\left(1-R^{2}\right) .
$$

This quantity is smaller than $R^{2}$ (unless $p=1$ or $R^{2}=1$ ). A possible merit to it is that it takes account of $p$; the idea is that the larger $p$ is relative to $N$, the greater the tendency of $R^{2}$ to be large by chance.

### 4.4.3. Distribution of the Sample Multiple Correlation Coefficient When the Population Multiple Correlation Coefficient Is Not Zero

In this subsection we shall find the distribution of $R$ when the null hypothesis $\bar{R}=0$ is not true. We shall find that the distribution depends only on the population multiple correlation coefficient $\bar{R}$.

First let us consider the conditional distribution of $R^{2} /\left(1-R^{2}\right)= a_{(1)}^{\prime} A_{22}^{-1} a_{(1)} / a_{11 \cdot 2}$ given $Z_{\alpha}^{(2)}=z_{\alpha}^{(2)}, \alpha=1, \ldots, n$. Under these conditions $Z_{11}, \ldots, Z_{1 n}$ are independently distributed, $Z_{1 \alpha}$ according to $N\left(\beta^{\prime} z_{\mathrm{a}}^{(2)}, \sigma_{112}\right)$, where $\boldsymbol{\beta}=\boldsymbol{\Sigma}_{22}^{-1} \boldsymbol{\sigma}_{(1)}$ and $\sigma_{11 \cdot 2}=\sigma_{11}-\boldsymbol{\sigma}_{(1)}^{\prime} \boldsymbol{\Sigma}_{22}^{-1} \boldsymbol{\sigma}_{(1)}$. The conditions are those of Theorem 4.3.3 with $Y_{\alpha}=Z_{1 \alpha}, \Gamma=\boldsymbol{\beta}^{\prime}, \boldsymbol{w}_{\alpha}=\boldsymbol{z}_{\alpha}^{(2)}, r=p-1, \boldsymbol{\Phi}=\sigma_{11 \cdot 2}$, $m=n$. Then $a_{11 \cdot 2}=a_{11}-a_{(1)}^{\prime} A_{22}^{-1} a_{(1)}$ corresponds to $\sum_{n-1}^{m} Y_{n} Y_{n}^{\prime}-G H G^{\prime}$. and $a_{11-2} / \sigma_{11-2}$ has a $\chi^{2}$-distribution with $n-(p-1)$ degrees of freedom. $a_{(1)}^{\prime} A_{22}^{-1} a_{(1)}=\left(A_{22}^{-1} a_{(1)}\right)^{\prime} A_{22}\left(A_{22}^{-1} a_{(1)}\right)$ corresponds to $G H G^{\prime}$ and is distributed as $\sum_{\alpha} U_{\alpha}^{2}, \alpha=n-(p-1)+1, \ldots, n$, where $\operatorname{Var}\left(U_{\alpha}\right)=\sigma_{11,2}$ and

$$
\mathscr{E}\left(U_{n-p+2}, \ldots, U_{n}\right)=\Gamma F^{-1},
$$

where $\boldsymbol{F} \boldsymbol{H} \boldsymbol{F}^{\prime}=\boldsymbol{I}\left[\boldsymbol{H}=\boldsymbol{F}^{-1}\left(\boldsymbol{F}^{\prime}\right)^{-1}\right]$. Then $\boldsymbol{a}_{(1)}^{\prime} \boldsymbol{A}_{22}^{-1} a_{(1)} / \sigma_{11 \cdot 2}$ is distributed as $\sum_{\alpha}\left(U_{\alpha} / \sqrt{\sigma_{112}}\right)^{2}$, where $\operatorname{Var}\left(U_{x} / \sqrt{\sigma_{11 \cdot 2}}\right)=1$ and

$$
\begin{aligned}
\sum_{\alpha=n-p+2}^{n}\left(\frac{\mathscr{E} U_{\alpha}}{\sqrt{\sigma_{11 \cdot 2}}}\right)^{2} & =\frac{1}{\sigma_{112}} \Gamma \boldsymbol{F}^{-1}\left(\Gamma \boldsymbol{F}^{-1}\right)^{\prime}=\frac{\Gamma \boldsymbol{H} \Gamma^{\prime}}{\sigma_{112}} \\
& =\frac{\boldsymbol{\beta}^{\prime} \boldsymbol{A}_{22} \boldsymbol{\beta}}{\sigma_{11 \cdot 2}} .
\end{aligned}
$$

Thus (conditionally) $a_{(1)}^{\prime} A_{22}^{\prime} a_{(1)} / \sigma_{11}$, has a noncentral $\lambda^{2}$-distribution with
$p-1$ degrees of freedom and noncentrality parameter $\boldsymbol{\beta}^{\prime} \boldsymbol{A}_{22} \boldsymbol{\beta} / \sigma_{11-2}$. (See Theorem 5.4,1.) We are led to the following theorem:

Theorem 4.4.4. Let $R$ be the sample multiple correlation coefficient between $X_{(1)}$ and $X^{(2) \prime}=\left(X_{2}^{\prime}, \ldots, X_{p}\right)$ based on $N$ observations $\left(x_{11}, x_{1}^{(2)}\right), \ldots,\left(x_{1 N}, x_{N}^{(2)}\right)$. The conditional distribution of $\left.\left[R^{2} /\left(1-R^{2}\right)\right][N-p) /(p-1)\right]$ given $x_{\alpha}^{(2)}$ fixed is noncentral $F$ with $p-1$ and $N-p$ degrees of freedom and noncentrality parameter $\beta^{\prime} A_{22} \beta / \sigma_{11,2}$.

The conditional density (from Theorem 5.4.1) of $F=\left[R^{2} /\left(1-R^{2}\right)\right][(N- p) /(p-1)]$ is

$$
\begin{aligned}
& \frac{(p-1) \exp \left[-\frac{1}{2} \beta^{\prime} A_{22} \beta / \sigma_{11 \cdot 2}\right]}{(N-p) \Gamma\left[\frac{1}{2}(N-p)\right]} \\
& \quad \sum_{\alpha=0}^{\infty} \frac{\left(\frac{\beta^{\prime} A_{22} \beta}{2 \sigma_{11 \cdot 2}}\right)^{\alpha}\left[\frac{(p-1) f}{N-p}\right]^{\frac{1}{2}(p-1)+\alpha-1} \Gamma^{\left[\frac{1}{2}(N-1)+\alpha\right]}}{\alpha!\Gamma\left[\frac{1}{2}(p-1)+\alpha\right]\left[1+\frac{(p-1) f}{N-p}\right]^{\frac{1}{2}(N-1)+\alpha}}
\end{aligned}
$$

and the conditional density of $W=R^{2}$ is $(d f=[(N-p) /(p-1)](1- \left.w)^{-2} d w\right)$

$$
\begin{aligned}
& \frac{\exp \left[-\frac{1}{2} \beta^{\prime} A_{22} \beta / \sigma_{112}\right]}{\Gamma\left[\frac{1}{2}(N-p)\right]}(1-w)^{\frac{1}{2}(N-p)-1} \\
& \cdot \sum_{\alpha=0}^{\infty} \frac{\left(\frac{\beta^{\prime} A_{22} \beta}{2 \sigma_{11 \cdot 2}}\right)^{\alpha} w^{\frac{1}{2}(p-1)+\alpha-1} \Gamma\left[\frac{1}{2}(N-1)+\alpha\right]}{\alpha!\Gamma\left[\frac{1}{N}(p-1)+\alpha\right]}
\end{aligned} .
$$

To obtain the unconditional density we need to multiply (38) by the density of $Z_{1}^{(2)} \ldots, Z_{n}^{(2)}$ to obtain the joint density of $W$ and $Z_{1}^{(2)}, \ldots, Z_{n}^{(2)}$ and then integrate with respect to the latter set to obtain the marginal density of $W$. We have

$$
\begin{aligned}
\frac{\beta^{\prime} A_{22} \beta}{\sigma_{11 \cdot 2}} & =\frac{\beta^{\prime} \sum_{\alpha=1}^{n} z_{\alpha}^{(2)} z_{\alpha}^{(2)} \beta}{\sigma_{11 \cdot 2}} \\
& =\sum_{\alpha=1}^{n}\left(\frac{\beta^{\prime} z_{\alpha}^{(2)}}{\sqrt{\sigma_{11 \cdot 2}}}\right)^{2}
\end{aligned}
$$

Since the distribution of $\boldsymbol{Z}_{\alpha}^{(2)}$ is $N\left(\mathbf{0}, \boldsymbol{\Sigma}_{22}\right)$, the distribution of $\boldsymbol{\beta}^{\prime} Z_{\alpha}^{(2)} / \sqrt{\sigma_{\mathbf{1 1} \cdot 2}}$ is normal with mean zero and variance

$$
\begin{aligned}
\mathscr{E}\left(\frac{\boldsymbol{\beta}^{\prime} Z_{\alpha}^{(2)}}{\sqrt{\Sigma_{11 \cdot 2}}}\right)^{2} & =\frac{\mathscr{E} \boldsymbol{\beta}^{\prime} Z_{\alpha}^{(2)} Z_{\alpha}^{(2)} \boldsymbol{\beta}}{\sigma_{11 \cdot 2}} \\
& =\frac{\boldsymbol{\beta}^{\prime} \Sigma_{22} \boldsymbol{\beta}}{\sigma_{11}-\boldsymbol{\beta}^{\prime} \Sigma_{22} \boldsymbol{\beta}}=\frac{\boldsymbol{\beta}^{\prime} \Sigma_{22} \boldsymbol{\beta} / \sigma_{11}}{1-\boldsymbol{\beta}^{\prime} \Sigma_{22} \boldsymbol{\beta} / \sigma_{11}} \\
& =\frac{\bar{R}^{2}}{1-\bar{R}^{2}}
\end{aligned}
$$

Thus $\left(\boldsymbol{\beta}^{\prime} A_{22} \boldsymbol{\beta} / \sigma_{11,2}\right) /\left[\bar{R}^{2} /\left(1-\bar{R}^{2}\right)\right]$ has a $\chi^{2}$-distribution with $n$ degrees of freedom. Let $\bar{R}^{2} /\left(1-\bar{R}^{2}\right)=\phi$. Then $\boldsymbol{\beta}^{\prime} \boldsymbol{A}_{22} \boldsymbol{\beta} / \sigma_{11 \cdot 2}=\phi \chi_{n}^{2}$. We compute

$$
\begin{aligned}
& \mathscr{E} e^{-\frac{1}{2} \phi_{n}^{2} n}\left(\frac{\phi \chi_{n}^{2}}{2}\right)^{\alpha} \\
& \quad=\frac{\phi^{\alpha}}{2^{\alpha}} \int_{0}^{\infty} u^{\alpha} e^{-\frac{1}{2} \phi u} \frac{1}{2^{\frac{1}{2} n} \Gamma\left(\frac{1}{2} n\right)} u^{\frac{1}{2} n-1} e^{-\frac{1}{2} u} d u \\
& \quad=\frac{\phi^{\alpha}}{2^{\alpha}} \int_{0}^{\infty} \frac{1}{2^{\frac{1}{2} n} \Gamma\left(\frac{1}{2} n\right)} u^{\frac{1}{2} n+\alpha-1} e^{-\frac{1}{2}(1+\phi) u} d u \\
& \quad=\frac{\phi^{\alpha}}{(1+\phi)^{\frac{1}{2} n+\alpha}} \frac{\Gamma\left(\frac{1}{2} n+\alpha\right)}{\Gamma\left(\frac{1}{2} n\right)} \int_{0}^{\infty} \frac{1}{2^{\frac{1}{2} n+\alpha} \Gamma\left(\frac{1}{2} n+\alpha\right)} v^{\frac{1}{2} n+\alpha-1} e^{-\frac{1}{2} v} d v \\
& \quad=\frac{\phi^{\alpha}}{(1+\phi)^{\frac{1}{2} n+\alpha}} \frac{\Gamma\left(\frac{1}{2} n+\alpha\right)}{\Gamma\left(\frac{1}{2} n\right)}
\end{aligned}
$$

Applying this result to (38), we obtain as the density of $R^{2}$

$$
\frac{\left(1-R^{2}\right)^{\frac{1}{2}(n-p-1)}\left(1-\bar{R}^{2}\right)^{\frac{1}{2} n}}{\Gamma\left[\frac{1}{2}(n-p+1)\right] \Gamma\left(\frac{1}{2} n\right)} \sum_{\mu=0}^{\infty} \frac{\left(\bar{R}^{2}\right)^{\mu}\left(R^{2}\right)^{\frac{1}{2}(p-1)+\mu-1} \Gamma^{2}\left(\frac{1}{2} n+\mu\right)}{\mu!\Gamma\left[\frac{1}{2}(p-1)+\mu\right]} .
$$

Fisher (1928) found this distribution. It can also be written

$$
\begin{aligned}
\frac{\Gamma\left(\frac{1}{2} n\right)\left(1-\bar{R}^{2}\right)^{\frac{1}{2} n}}{\Gamma\left[\frac{1}{2}(n-p+1)\right] \Gamma\left[\frac{1}{2}(p-1)\right]}\left(R^{2}\right)^{\frac{1}{2}(p-3)} & \left(1-R^{2}\right)^{\frac{1}{2}(n-p-1)} \\
\cdot & F\left[\frac{1}{2} n, \frac{1}{2} n ; \frac{1}{2}(p-1) ; R^{2} \widetilde{R}^{2}\right],
\end{aligned}
$$

where $F$ is the hypergeometric function defined in (41) of Section 4.2.

Another form of the density can be obtained when $n-p+1$ is even. We have

$$
\begin{aligned}
& \sum_{\mu=0}^{\infty} \frac{\left(R^{2} \bar{R}^{2}\right)^{\mu}}{\mu!} \frac{\Gamma^{2}\left(\frac{1}{2} n+\mu\right)}{\Gamma\left[\frac{1}{2}(p-1)+\mu\right]} \\
& \quad=\left.\sum_{\mu=0}^{\infty} \frac{\left(R^{2} \bar{R}^{2}\right)^{\mu}}{\mu!} \Gamma\left(\frac{1}{2} n+\mu\right)\left(\frac{\partial}{\partial t}\right)^{\frac{1}{2}(n-p+1)} t^{\frac{1}{2} n+\mu-1}\right|_{t=1} \\
& \quad=\left.\left(\frac{\partial}{\partial t}\right)^{\frac{1}{2}(n-p+1)} t^{\frac{1}{2} n-1} \sum_{\mu=0}^{\infty} \frac{\left(t \bar{R}^{2} R^{2}\right)^{\mu}}{\mu!} \frac{\Gamma\left(\frac{1}{2} n+\mu\right)}{\Gamma\left(\frac{1}{2} n\right)}\right|_{t=1} \Gamma\left(\frac{1}{2} n\right) \\
& \quad=\left.\Gamma\left(\frac{1}{2} n\right)\left(\frac{\partial}{\partial t}\right)^{\frac{1}{2}(n-p+1)} t^{\frac{1}{2} n-1}\left(1-t R^{2} \bar{R}^{2}\right)^{-\frac{1}{2} n}\right|_{t=1}
\end{aligned}
$$

The density is therefore

$$
\begin{aligned}
& \frac{\left(1-\bar{R}^{2}\right)^{\frac{1}{2} n}\left(R^{2}\right)^{\frac{1}{2}(p-3)}\left(1-R^{2}\right)^{\frac{1}{2}(n-p-1)}}{\Gamma\left[\frac{1}{2}(n-p+1)\right]} \\
& \left.\quad \cdot\left(\frac{\partial}{\partial t}\right)^{\frac{1}{2}(n-p+1)} t^{\frac{1}{2} n-1}\left(1-t R^{2} \bar{R}^{2}\right)^{-\frac{1}{2} n}\right|_{t=1}
\end{aligned}
$$

Theorem 4.4.5. The density of the square of the multiple correlation coefficient, $R^{2}$, between $X_{1}$ and $X_{2}, \ldots, X_{p}$ based on a sample of $N=n+1$ is given by (42) or (43) [or (45) in the case of $n-p+1$ even], where $\bar{R}^{2}$ is the corresponding population multiple correlation coefficient.

The moments of $R$ are

$$
\begin{aligned}
\mathscr{E} R^{h}= & \frac{\left(1-\bar{R}^{2}\right)^{\frac{1}{2} n}}{\Gamma\left[\frac{1}{2}(n-p+1)\right] \Gamma\left(\frac{1}{2} n\right)} \sum_{\mu=0}^{\infty} \frac{\left(\bar{R}^{2}\right)^{\mu} \Gamma^{2}\left(\frac{1}{2} n+\mu\right)}{\Gamma\left[\frac{1}{2}(p-1)+\mu\right] \mu!} \\
& \cdot \int_{0}^{1}\left(1-R^{2}\right)^{\frac{1}{2}(n-p+1)-1}\left(R^{2}\right)^{\frac{1}{2}(p+h-1)+\mu-1} d\left(R^{2}\right) \\
= & \frac{\left(1-\bar{R}^{2}\right)^{\frac{1}{2} n}}{\Gamma\left(\frac{1}{2} n\right)} \sum_{\mu=0}^{\infty} \frac{\left(\bar{R}^{2}\right)^{\mu} \Gamma^{2}\left(\frac{1}{2} n+\mu\right) \Gamma\left[\frac{1}{2}(p+h-1)+\mu\right]}{\mu!\Gamma\left[\frac{1}{2}(p-1)+\mu\right] \Gamma\left[\frac{1}{2}(n+h)+\mu\right]}
\end{aligned}
$$

The sample multiple correlation tends to overestimate the population multiple correlation. The sample multiple correlation is the maximum sample correlation between $x_{1}$ and linear combinations of $\boldsymbol{x}^{(2)}$ and hence is greater
than the sample correlation between $x_{1}$ and $\boldsymbol{\beta}^{\prime} \boldsymbol{x}^{(2)}$; however, the latter is the simple sample correlation corresponding to the simple population correlation between $x_{1}$ and $\boldsymbol{\beta}^{\prime} \boldsymbol{x}^{(2)}$, which is $\bar{R}$, the population multiple correlation.

Suppose $R_{1}$ is the multiple correlation in the first of two samples and $\hat{\boldsymbol{\beta}}_{1}$ is the estimate of $\boldsymbol{\beta}$; then the simple correlation between $x_{1}$ and $\hat{\boldsymbol{\beta}}_{1}^{\prime} x^{(2)}$ in the second sample will tend to be less than $R_{1}$ and in particular will be less than $R_{2}$, the multiple ccrrelation in the second sample. This has been called "the shrinkage of the multiple correlation."

Kramer (1963) and Lee (1972) have given tables of the upper significance points of $R$. Gajjar (1967), Gurland (1968), Gurland and Milton (1970), Khatri (1966), and Lee (1917b) have suggested approximations to the distributions of $R^{2} /\left(1-R^{2}\right)$ and obtained large-sample results.

### 4.4.4. Some Optimal Properties of the Multiple Correlation Test

Theorem 4.4.6. Given the observations $x_{1}, \ldots, x_{N}$ from $N(\mu, \Sigma)$, of all tests of $\bar{R}=0$ at a given significance level based on $\bar{x}$ and $A=\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}$ that are invariant with respect to transformations

$$
\begin{aligned}
& \bar{x}_{1}^{*}=c \bar{x}_{1}+d, \quad \bar{x}^{(2) *}=C \bar{x}^{(2)}+d, \\
& a_{11}^{*}=c^{2} a_{11}, \quad a_{(1)}^{*}=c C a_{(1)}, \quad A_{22}^{*}=C A_{22} C^{\prime},
\end{aligned}
$$

any critical rejection region given by $R$ greater than a constant is unifomby most powerful.

Proof. The multiple correlation cocfficient $R$ is invariant under the transformation, and any function of the sufficient statistics that is invariant is a function of $R$. (See Problem 4.34.) Therefore, any invariant test must be based on $R$. The Neyman-Pearson fundamental lemma applied to testing the null hypothesis $\bar{R}=0$ against a specific alternative $\bar{R}=\bar{R}_{0}>0$ tells us the most powerful test at a given level of significance is based on the ratio of the density of $R$ for $\bar{R}=\bar{R}_{0}$, which is (42) times $2 R$ [because (42) is the density of $R^{2}$ ], to the density for $R=0$, which is (22). The ratio is a positive constant times

$$
\sum_{\mu=0}^{\infty} \frac{\left(\bar{R}_{0}^{2}\right)^{\mu} \Gamma^{2}\left(\frac{1}{2} n+\mu\right)}{\mu!\Gamma\left[\frac{1}{2}(p-1)+\mu\right]} R^{p-2+2 \mu} .
$$

Since (48) is an increasing function of $R$ for $R \geq 0$, the set of $R$ for which (48) is greater than a constant is an interval of $R$ greater than a constant.

Theorem 4.4.7. On the basis of observations $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, of all tests of $\bar{R}=0$ at a given significance level with power depending only on $\bar{R}$, the test with critical region given by $R$ greater than a constant is uniformly most powerful.

Theorem 4.4.7 follows from Theorem 4.4.6 in the same way that Theorem 5.6.4 follows from Theorem 5.6.1.

### 4.5. ELLIPTICALLY CONTOURED DISTRIBUTIONS

### 4.5.1. Observations Elliptically Contoured

Suppose $x_{1} \ldots x_{N}$ are $N$ independent observations on a random $p$-vector $\boldsymbol{X}$ with density

$$
|\boldsymbol{\Lambda}|^{-\frac{1}{2}} g\left[(x-v)^{\prime} \boldsymbol{\Lambda}^{-1}(x-v)\right] .
$$

The sample covariance matrix $S$ is an unbiased estimator of the covariance matrix $\Sigma=\left[\mathscr{E} R^{2} / p\right] \Lambda$, where $R^{2}=(\boldsymbol{X}-\boldsymbol{v})^{\prime} \Lambda^{-1}(\boldsymbol{X}-\boldsymbol{v})$ and $\mathscr{E} R^{2}<\infty$. An estimator of $\rho_{1 j}=\sigma_{1 j} / \sqrt{\sigma_{11} \sigma_{j j}}=\lambda_{1 j} / \sqrt{\lambda_{11} \lambda_{j J}}$ is $r_{1 j}=s_{1 j} / \sqrt{s_{11} s_{j j}}, i, j= 1 . \ldots, p$. The small-sample distribution of $r_{1 j}$ is in general difficult to obtain, but the asymptotic distribution can be obtained from the limiting normal distribution of $\sqrt{N}(S-\Sigma)$ given in (13) of Section 3.6.

First we prove a general theorem on asymptotic distributions of functions of the sample covariance matrix $S$ using Theorems 4.2.3 and 3.6.5. Define

$$
s=\operatorname{vec} S, \quad \boldsymbol{\sigma}=\operatorname{vec} \Sigma .
$$

Theorem 4.5.1. Let $f(s)$ be a vector-valued function such that each component of $f(s)$ has a nonzero differential at $s=\boldsymbol{\sigma}$. Suppose $S$ is the covariance of a sample from (1) such that $\mathscr{E} R^{4}<\infty$. Then

$$
\begin{aligned}
\sqrt{N}[f(s)-f(\boldsymbol{\sigma})] & =\frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}^{\prime}} \sqrt{N}(s-\boldsymbol{\sigma})+o_{p}(1) \\
& \xrightarrow{d} N\left\{\mathbf{0}, \frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}^{\prime}}\left[2(1+\kappa)(\mathbf{\Sigma} \otimes \mathbf{\Sigma})+\kappa \boldsymbol{\sigma} \boldsymbol{\sigma}^{\prime}\right]\left(\frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}^{\prime}}\right)^{\prime}\right\}
\end{aligned}
$$

Corollary 4.5.1. If

$$
f(c s)=f(s)
$$

for all $c>0$ and all positive definite $S$ and the conditions of Theorem 4.5.1 hold, then
(5) $\quad \sqrt{N}[f(s)-f(\boldsymbol{\sigma})] \xrightarrow{d} N\left[\mathbf{0}, 2(1+\kappa) \frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}^{\prime}}(\boldsymbol{\Sigma} \otimes \boldsymbol{\Sigma})\left(\frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}^{\prime}}\right)^{\prime}\right]$.

Proof. From (4) we deduce

$$
0=\frac{\partial f(c s)}{\partial c}=\frac{\partial f(c s)}{\partial s^{\prime}} \frac{\partial(c s)}{\partial c}=\frac{\partial f(c s)}{\partial s^{\prime}} s .
$$

That is,

$$
\frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}^{\prime}} \boldsymbol{\sigma}=\mathbf{0} .
$$ $\square$

The conclusion of Corollary 4.5.1 can be framed as

$$
\frac{\sqrt{N}}{\sqrt{1+\kappa}}[f(s)-f(\boldsymbol{\sigma})] \xrightarrow{d} N\left[0,2 \frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}^{\prime}}(\boldsymbol{\Sigma} \otimes \boldsymbol{\Sigma})\left(\frac{\partial f(\boldsymbol{\sigma})}{\partial \boldsymbol{\sigma}^{\prime}}\right)^{\prime}\right] .
$$

The limiting normal distribution in (8) holds in particular when the sample is drawn from the normal distribution. The corollary holds true if $\kappa$ is replaced by a consistent estimator $\hat{\kappa}$. For example, a consistent estimator of $1+\hat{\kappa}$ given by (16) of Section 3.6 is

$$
1+\hat{\kappa}=\sum_{\alpha=1}^{N}\left[\left(x_{\alpha}-\bar{x}\right)^{\prime} S^{-1}\left(x_{\alpha}-\bar{x}\right)\right]^{2} /\left[N_{p}(p+2)\right] .
$$

A sample correlation such as $f(s)=r_{i j}=s_{i j} / \sqrt{s_{i i} s_{j j}}$ or a set of such correlations is a function of $S$ that is invariant under scale transformations; that is, it satisfies (4).

Corollary 4.5.2. Under the conditions of Theorem 4.5.1,

$$
\sqrt{\frac{N}{1+\hat{\kappa}}} \frac{\left(r_{i j}-\rho_{i j}\right)}{\sqrt{1-r_{i j}^{2}}} \xrightarrow{d} N(0,1) .
$$

As in the case of the observations normally distributed,

$$
\sqrt{\frac{N}{1+\hat{\kappa}}}\left(\frac{1}{2} \log \frac{1+r_{i j}}{1-r_{i j}}-\frac{1}{2} \log \frac{1+\rho_{i j}}{1-\rho_{i j}}\right) \xrightarrow{d} N(0,1) .
$$

Of course, any improvement of (11) over (10) depends on the distribution samples.

Partial correlations such as $r_{i j, q+1, \ldots, p}, i, j=1, \ldots, q$, are also invariant functions of $S$.

Corollary 4.5.3. Under the conditions of Theorem 4.5.1,

$$
\sqrt{\frac{N}{1+\hat{\kappa}}}\left(r_{i j . q+1, \ldots, p}-\rho_{i j . q+1, \ldots, p}\right) \xrightarrow{d} N(0,1) .
$$

Now let us consider the asymptotic distribution of $R^{2}$, the square of the multiple correlation, when $\bar{R}^{2}$, the square of the population multiple correlation, is 0 . We use the notation of Section 4.4. $\bar{R}^{2}=0$ is equvialent to $\boldsymbol{\sigma}_{(1)}=\mathbf{0}$. Since the sample and population multiple correlation coefficients between $X_{1}$ and $X^{(2)}=\left(X_{2}, \ldots, X_{p}\right)^{\prime}$ are invariant with respect to linear transformations (47) of Section 4.4, for purposes of studying the distribution of $R^{2}$ we can assume $\boldsymbol{\mu}=\mathbf{0}$ and $\boldsymbol{\Sigma}=\boldsymbol{I}_{p}$. In that case $s_{11} \xrightarrow{p} 1, \boldsymbol{s}_{(1)} \xrightarrow{p}$, and $S_{22} \xrightarrow{p} I_{p-1}$. Furthermore, for $k, i \neq 1$ and $j=l=1$, Lemma 3.6.1 gives

$$
\mathscr{E} s_{(1)} s_{(1)}^{\prime}=\left(\frac{1}{n}+\frac{\kappa}{N}\right) I_{p-1} .
$$

Theorem 4.5.2. Under the conditions of Theorem 4.5.1

$$
\sqrt{\frac{N}{1+\kappa}} s_{(1)} \xrightarrow{d} N\left(0, I_{p-1}\right) .
$$

Corollary 4.5.4. Under the conditions of Theorem 4.5.1

$$
\frac{N R^{2}}{1+\hat{\kappa}}=\frac{N s_{(1)}^{\prime} S_{22}^{-1} s_{(1)}}{(1+\hat{\kappa}) s_{11}} \xrightarrow{d} \chi_{p-1}^{2} .
$$

### 4.5.2. Elliptically Contoured Matrix Distributions

Now let us turn to the model

$$
|\Lambda|^{-N / 2} g\left[\operatorname{tr}\left(X-\varepsilon_{N} \nu^{\prime}\right) \Lambda^{-1}\left(X-\varepsilon_{N} \nu^{\prime}\right)^{\prime}\right]
$$

based on the vector spherical model $g\left(\operatorname{tr} Y^{\prime} Y\right)$. The unbiased estimators of $\boldsymbol{\nu}$ and $\boldsymbol{\Sigma}_{\boldsymbol{\gamma}}=\left(\mathscr{E} R^{2} / p\right) \boldsymbol{\Lambda}$ are $\overline{\boldsymbol{x}}=(1 / N) \boldsymbol{X}^{\prime} \boldsymbol{\varepsilon}_{N}$ and $S=(1 / n) A$, where $A= \left(X-\varepsilon_{n} \bar{x}^{\prime}\right)^{\prime}\left(X-\varepsilon_{N} \bar{x}^{\prime}\right)$.

Since

$$
\left(\boldsymbol{X}-\varepsilon_{N} v^{\prime}\right)^{\prime}\left(\boldsymbol{X}-\varepsilon_{N} v^{\prime}\right)=A+N(\bar{x}-v)(\bar{x}-v)^{\prime},
$$

$\boldsymbol{A}$ and $\overline{\boldsymbol{x}}$ are a complete set of sufficient statistics.
The maximum likelihood estimators of $\boldsymbol{v}$ and $\boldsymbol{\Lambda}$ are $\hat{\boldsymbol{v}}=\overline{\boldsymbol{x}}$ and $\hat{\boldsymbol{\Lambda}}= \left(p / w_{g}\right) A$. The maximum likelihood estimator of $\rho_{i j}=\lambda_{1 j} / \sqrt{\lambda_{i i} \lambda_{j j}}= \sigma_{i j} / \sqrt{\sigma_{i i} \sigma_{j j}}$ is $\hat{\rho}_{i j}=a_{i j} / \sqrt{a_{1 i} a_{j j}}=s_{i j} / \sqrt{s_{i i} s_{j j}}$ (Theorem 3.6.4).

The sample correlation $r_{1 j}$ is a function $f(\boldsymbol{X})$ that satisfies the conditions (45) and (46) of Theorem 3.6.5 and hence has the same distribution for an arbitrary density $g[\operatorname{tr}(\cdot)]$ as for the normal density $g[\operatorname{tr}(\cdot)]=$ const $e^{-\frac{1}{2} \operatorname{tr}(\cdot)}$. Similarly, a partial correlation $r_{i j, q+1, \ldots, p}$ and a multiple correlation $R^{2}$ satisfy the conditions, and the conclusion holds.

Theorem 4.5.3. When $X$ has the vector elliptical density (16), the distributions of $r_{1,}, r_{1, q+1}$, and $R^{2}$ are the distributions derived for normally distributed observations.

It follows from Theorem 4.5.3 that the asymptotic distributions of $r_{11}$. $r_{i j . q+1, \ldots p, p}$, and $R^{2}$ are the same as for sampling from normal distributions.

The class of left spherical matrices $Y$ with densities is the class of $g\left(Y^{\prime} Y\right)$. Let $\boldsymbol{X}=\boldsymbol{Y} \boldsymbol{C}^{\prime}+\boldsymbol{\varepsilon}_{\boldsymbol{N}} \boldsymbol{v}^{\prime}$, where $\boldsymbol{C}^{\prime} \boldsymbol{\Lambda}^{-\mathbf{I}} \boldsymbol{C}=\boldsymbol{I}$, that is, $\boldsymbol{\Lambda}=\boldsymbol{C} \boldsymbol{C}^{\prime}$. Then $\boldsymbol{X}$ has the density

$$
|\boldsymbol{C}|^{-N} g\left[\boldsymbol{C}^{-1}\left(\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \boldsymbol{v}^{\prime}\right)^{\prime}\left(\boldsymbol{X}-\boldsymbol{\varepsilon}_{N} \boldsymbol{v}^{\prime}\right)\left(\boldsymbol{C}^{\prime}\right)^{-1}\right] .
$$

We now find a stochastic representation of the matrix $Y$.
Lemma 4.5.1. Let $V=\left(\nu_{1}, \ldots, \nu_{p}\right)$, where $\nu_{1}$ is an $N$-component vector. $i=1, \ldots, p$. Define recursively $w_{1}=v_{1}$,

$$
w_{1}=v_{1}-\sum_{j=1}^{i-1} \frac{v_{1}^{\prime} w_{j}}{w_{j}^{\prime} w_{j}} w_{j}, \quad i=2, \ldots p .
$$

Let $u_{i}=w_{i} /\left\|w_{i}\right\|$. Then $\left\|u_{i}\right\|=1, i=1, \ldots, p$, and $u_{i}^{\prime} u_{j}=0, i \neq j$. Further,

$$
V=U T^{\prime},
$$

where $U=\left(u_{1}, \ldots, u_{p}\right) ; t_{n}=\left\|w_{i}\right\|, i=1 \ldots, p ; t_{i j}=v_{i}^{\prime} w_{j},\left\|w_{j}\right\|=v_{i}^{\prime} u_{j}, j= 1, \ldots, i-1, i=1, \ldots, p ;$ and $t_{i j}=0, i<j$.

The proof of the lemma is given in the first part of Section 7.2 and as the Gram-Schmidt orthogonalization in the Appendix (Section A.5.1). This lemma generalizes the construction in Section 3.2; see Figure 3.1. See also Figure 7.1.

Note that $T$ is lower triangular, $U^{\prime} U=I_{p}$, and $V^{\prime} V=T T^{\prime}$. The last equation, $t_{n} \geq 0, i=1, \ldots, p$, and $t_{n j}=0, i<j$, can be solved uniquely for $T$. Thus $T$ is a function of $V^{\prime} V$ (and the restrictions).

Let $Y(N \times p)$ have the density $g\left(Y^{\prime} Y\right)$. and let $O_{\wedge}$ be an orthogonal $N \times N$ matrix. Then $Y^{*}=O_{N} Y$ has the density $g\left(Y^{*} Y^{*}\right)$. Hence $Y^{*}= O_{N} Y \stackrel{d}{=} Y$. Let $Y^{*}=U^{*} T^{* \prime}$, where $t_{n}^{*}>0, i=1, \ldots, p$, and $t_{n}^{*}=0, i<j$. From $Y^{*} Y^{*}=Y^{\prime} Y$ it follows that $T^{*} T^{* \prime}=T T^{\prime}$ and hence $T^{*}=T, Y^{*}=U^{*} T$. and $\boldsymbol{U}^{*}=\boldsymbol{O}_{N} \boldsymbol{U} \stackrel{d}{=} \boldsymbol{U}$. Let the space of $\boldsymbol{U}(N \times p)$ such that $\boldsymbol{U}^{\prime} \boldsymbol{U}=\boldsymbol{I}_{p}$ be denoted $O(N \times p)$.

Definition 4.5.1. If $U(N \times p)$ satisfies $U^{\prime} U=I_{p}$ and $O 、 U \stackrel{!}{=} U$ for all orthogonal $O_{N}$, then $U$ is uniformly distributed on $O(N \times p)$.

The space of $U$ satisfying $U^{\prime} U=I_{p}$ is known as a Steifel manifold. The probability measure of Definition 4.5.1 is known as the Haar invariant distribution. The property $O_{N} U \stackrel{d}{=} U$ for all orthogonal $O_{N}$ defines the (normalized) measure uniquely [Halmos (1956)].

Theorem 4.5.4. If $Y(N \times p)$ has the density $g\left(Y^{\prime} Y\right)$, then $U$ defined by $\boldsymbol{Y}=\boldsymbol{U} \boldsymbol{T}^{\prime}, \boldsymbol{U}^{\prime} \boldsymbol{U}=\boldsymbol{I}_{p}, t_{11}>0, i=1, \ldots, p$, and $t_{i j}=0, i<j$, is uniformly distributed on $O(N \times p)$.

The proof of Corollary 7.2.1 shows that for arbitrary $g(\cdot)$ the density of $T$ is

$$
\prod_{i=1}^{p}\left\{C\left[\frac{1}{2}(N+1-i)\right] t_{n}^{N-1}\right\} g\left(\operatorname{tr} T T^{\prime}\right),
$$

where $C(\cdot)$ is defined in (8) of Section 2.7.
The stochastic representation of $Y(N \times p)$ with density $g\left(Y^{\prime} Y\right)$ is

$$
Y=U T^{\prime},
$$

where $U(N \times p)$ is uniformly distributed on $O(N \times p)$ and $T$ is lower triangular with positive diagonal elements and has density (21).

Theorem 4.5.5. Let $\boldsymbol{f}(\boldsymbol{X})$ be a vector-valued function of $\boldsymbol{X}(N \times p)$ such that

$$
f\left(X+\varepsilon_{N} v^{\prime}\right)=f(X)
$$

for all $\boldsymbol{v}$ and

$$
f\left(X G^{\prime}\right)=f(X)
$$

for all $G(p \times p)$. Then the distribution of $f(X)$ where $X$ has an arbitrary density (18) is the same as the distribution of $f(X)$ where $X$ has the normal density (18).

Proof. From (23) we find that $f(X)=f\left(Y C^{\prime}\right)$, and from (24) we find $f\left(Y C^{\prime}\right)=f\left(U T^{\prime} C^{\prime}\right)=f(U)$, which is the same for arbitrary and normal densities (18). $\square$

Corollary 4.5.5. Let $f(X)$ be a vector-valued function of $X(N \times p)$ with the density (18), where $\boldsymbol{v}=\mathbf{0}$. Suppose (24) holds for all $\boldsymbol{G}(p \times p)$. Then the distribution of $f(\boldsymbol{X})$ for an arbitrary density (18) is the same as the distribution of $f(X)$ when $X$ has the normal density (18).



The condition (24) of Corollary 4.5.5 is that $f(X)$ is invariant with respect to linear transformations $\boldsymbol{X} \rightarrow \boldsymbol{X G}$.

The density (18) can be written as

$$
|C|^{-1} g\left\{C^{-1}\left[A+N(\bar{x}-v)(\bar{x}-v)^{\prime}\right]\left(C^{\prime}\right)^{-1}\right\},
$$

which shows that $A$ and $\bar{x}$ are a complete set of sufficient statistics for $\boldsymbol{\Lambda}=\boldsymbol{C} \boldsymbol{C}^{\prime}$ and $\boldsymbol{\nu}$.

## PROBLEMS

4.1. (Sec. 4.2.1) Sketch

$$
k_{N}(r)=\frac{\Gamma\left[\frac{1}{2}(N-1)\right]}{\Gamma\left(\frac{1}{2} N-1\right) \sqrt{\pi}}\left(1-r^{2}\right)^{\frac{1}{2}(N-4)}
$$

for (a) $N=3$, (b) $N=4$, (c) $N=5$, and (d) $N=10$.
4.2. (Sec.4.2.1) Using the data of Problem 3.1, test the hypothesis that $X_{1}$ and $X_{2}$ are independent against all alternatives of dependence at significance level 0.01 .
4.3. (Sec. 4.2.1) Suppose a sample correlation of 0.65 is observed in a sample of 10 . Test the hypothesis of independence against the alternatives of positive correlation at significance level 0.05 .
4.4. (Sec. 4.2.2) Suppose a sample correlation of 0.65 is observed in a sample of 20 . Test the hypothesis that the population correlation is 0.4 against the alternatives that the population correlation is greater than 0.4 at significance level 0.05 .
4.5. (Sec. 4.2.1) Find the significance points for testing $\rho=0$ at the 0.01 level with $N=15$ observations against alternatives (a) $\rho \neq 0$, (b) $\rho>0$, and (c) $\rho<0$.
4.6. (Sec. 4.2.2) Find significance points for testing $\rho=0.6$ at the 0.01 level with $N=20$ observations against alternatives (a) $\rho \neq 0.6$, (b) $\rho>0.6$, and (c) $\rho<0.6$.
4.7. (Sec. 4.2.2) Tablulate the power function at $\rho=-1(0.2) 1$ for the tests in Problem 4.5. Sketch the graph of each power function.
4.8. (Sec. 4.2.2) Tablulate the power function at $\rho=-1(0.2) 1$ for the tests in Problem 4.6. Sketch the graph of each power function.
4.9. (Sec. 4.2.2) Using the data of Problem 3.1, find a (two-sided) confidence interval for $\rho_{12}$ with confidence coefficient 0.99 .
4.10. (Sec. 4.2.2) Suppose $N=10, r=0.795$. Find a one-sided confidence interval for $\rho$ [of the form ( $r_{0}, 1$ )] with confidence coefficient 0.95 .
4.11. (Sec. 4.2.3) Use Fisher's $z$ to test the hypothesis $p=0.7$ against alternatives $\mu \neq 0.7$ at the 0.05 level with $r=0.5$ and $N=50$.
4.12. (Sec. 4.2.3) Use Fisher's $z$ to test the hypothesis $\rho_{1}=\rho_{2}$ against the alternatives $\rho_{1} \neq \rho_{2}$ at the 0.01 level with $r_{1}=0.5, N_{1}=40, r_{2}=0.6, N_{2}=40$.
4.13. (Sec. 4.2.3) Use Fisher's $z$ to estimate $\rho$ based on sample correlations of -0.7 ( $N=30$ ) and of $-0.6(N=40)$.
4.14. (Sec. 4.2.3) Use Fisher's $z$ to obtain a confidence interval for $p$ with confidence 0.95 based on a sample correlation of 0.65 and a sample size of 25 .
4.15. (Sec. 4.2.2). Prove that when $N=2$ and $\rho=0, \operatorname{Pr}\{r=1\}=\operatorname{Pr}\{r=-1\}=\frac{1}{2}$.
4.16. (Sec. 4.2) Let $k_{N}(r, \rho)$ be the density of the sample corrclation coefficient $r$ for a given value of $\rho$ and $N$. Prove that $r$ has a monotone likelihood ratio; that is, show that if $\rho_{1}>\rho_{2}$, then $k_{N}\left(r, \rho_{1}\right) / k_{N}\left(r, \rho_{2}\right)$ is monotonically increasing in $r$. [Hint: Using (40), prove that if

$$
F\left[\frac{1}{2}, \frac{1}{2} ; n+\frac{1}{2} ; \frac{1}{2}(1+\rho r)\right]=\sum_{\alpha=0}^{\infty} c_{\alpha}(1+\rho r)^{\alpha}=g(r, \rho)
$$

has a monotone ratio, then $k_{N}(r, \rho)$ does. Show

$$
\frac{\partial^{2}}{\partial \rho \partial r} \log g(r, \rho)=\frac{\sum_{\alpha, \beta=0}^{\infty} c_{\alpha} c_{\beta}\left[(\alpha-\beta)^{2} r \rho+(\alpha+\beta)\right](1+r \rho)^{\alpha+\beta-2}}{2\left[\sum_{\alpha=0}^{\infty} c_{\alpha}(1+r \rho)^{\alpha}\right]^{2}} ;
$$

if ( $\partial^{2} / \partial \rho \partial r$ ) $\log g(r, \rho)>0$, then $g(r, \rho)$ has a monotone ratio. Show the numerator of the above expression is positive by showing that for each $\alpha$ the sum on $\beta$ is positive; use the fact that $c_{\alpha+1}<\frac{1}{2} c_{\alpha}$.]
4.17. (Sec.4.2) Show that of all tests of $\rho_{0}$ against a specific $\rho_{1}\left(>\rho_{0}\right)$ based on $r$, the procedures for which $r>c$ implies rejection are the best. [Hint: This follows from Problem 4.16.]
4.18. (Sec. 4.2) Show that of all tests of $\rho=\rho_{0}$ against $\rho>\rho_{0}$ based on $r$, a procedure for which $r>c$ implies rejection is uniformly most powerful.
4.19. (Sec. 4.2) Prove $r$ has a monotone likelihood ratio for $r>0, \rho>0$ by proving $h(r)=k_{N}\left(r, \rho_{1}\right) / k_{N}\left(r, \rho_{2}\right)$ is monotonically increasing for $\rho_{1}>\rho_{2}$. Here $h(r)$ is a constant times $\left(\sum_{\alpha=0}^{\infty} c_{\alpha} \rho_{1}^{\alpha} r^{\alpha}\right) /\left(\sum_{\alpha=0}^{\infty} c_{\alpha} \rho_{2}^{\alpha} r^{\alpha}\right)$. In the numerator of $h^{\prime}(r)$, show that the coefficient of $r^{\beta}$ is positive.
4.20. (Sec. 4.2) Prove that if $\boldsymbol{\Sigma}$ is diagonal, then the sets $r_{i j}$ and $a_{i n}$ are independently distributed. [Hint: Use the facts that $r_{i j}$ is invariant under scale transformations and that the density of the observations depends only on the $a_{i i}$.]
4.21. (Sec. 4.2.1) Prove that if $\rho=0$

$$
\mathscr{E} r^{2 m}=\frac{\Gamma\left[\frac{1}{2}(N-1)\right] \Gamma\left(m+\frac{1}{2}\right)}{\sqrt{\pi} \Gamma\left[\frac{1}{2}(N-1)+m\right]} .
$$

4.22. (Sec. 4.2.2) Prove $f_{1}(\rho)$ and $f_{2}(\rho)$ are monotonically increasing functions of $\rho$.
4.23. (Sec. 4.2.2) Prove that the density of the sample correlation $r$ [given by (38)] is

$$
\frac{n-1}{\pi}\left(1-\rho^{2}\right)^{\frac{1}{2} n}\left(1-r^{2}\right)^{\frac{1}{2}(n-3)} \int_{0}^{1} \frac{x^{n-1} d x}{(1-\rho r)^{n} \sqrt{1-x^{2}}}
$$

[Hint: Expand $(1-\rho r x)^{-n}$ in a power series, integrate, and use the duplication formula for the gamma function.]
4.24. (Sec. 4.2) Prove that (39) is the density of $r$. [Hint: From Problem 2.12 show

$$
\int_{0}^{\infty} \int_{1}^{\infty} e^{-\frac{1}{2}\left(y^{2}-2 x y z+z^{2}\right)} d y d z=\frac{\cos ^{-1}(-x)}{\sqrt{1-x^{2}}}
$$

Then argue

$$
\int_{0}^{\infty} \int_{0}^{\infty}(y z)^{n-1} e^{-\frac{1}{z}\left(y^{2}-2 x y z+z^{2}\right)} d y d z=\frac{d^{n-1}}{d x^{n-1}} \frac{\cos ^{-1}(-x)}{\sqrt{1-x^{2}}}
$$

Finally show that the integral of (31) with respect to $a_{11}\left(=y^{2}\right)$ and $a_{22}\left(=z^{2}\right)$ is (39).]
4.25. (Sec. 4.2) Prove that (40) is the density of $r$. [Hint: In (31) let $a_{11}=u e^{-t}$ and $a_{22}=u e^{v}$; show that the density of $v(0 \leq v<\infty)$ and $r(-1 \leq r \leq 1)$ is

$$
\frac{n-1}{\pi \sqrt{2}}\left(1-\rho^{2}\right)^{\frac{1}{2} n}(1-\rho r)^{-n+\frac{1}{2}}\left(1-r^{2}\right)^{\frac{1}{2}(n-3)} v^{-\frac{1}{2}}(1-v)^{n-1}\left[1-\frac{1}{2}(1+\rho r) v\right]^{-\frac{1}{2}}
$$

Use the expansion

$$
(1-y)^{-\frac{1}{2}}=\sum_{j=0}^{\infty} \frac{\Gamma\left(j+\frac{1}{2}\right)}{\Gamma\left(\frac{1}{2}\right) j!} y^{j} .
$$

Show that the integral is (40).]
4.26. (Sec. 4.2) Prove for integer $h$

$$
\begin{aligned}
\mathscr{E} r^{2 h-1} & =\frac{\left(1-\rho^{2}\right)^{\frac{1}{2} n}}{\sqrt{\pi} \Gamma\left(\frac{1}{2} n\right)} \sum_{\beta=0}^{\infty} \frac{(2 \rho)^{2 \beta+1}}{(2 \beta+1)!} \frac{\Gamma^{2}\left[\frac{1}{2}(n+1)+\beta\right] \Gamma\left(h+\beta+\frac{3}{2}\right)}{\Gamma\left(\frac{1}{2} n+h+\beta+1\right)} \\
\mathscr{6} r^{2 h} & =\frac{\left(1-\rho^{2}\right)^{\frac{1}{2} n}}{\sqrt{\pi} \Gamma\left(\frac{1}{2} n\right)} \sum_{\beta=0}^{\infty} \frac{(2 \rho)^{2 \beta}}{(2 \beta)!} \frac{\Gamma^{2}\left(\frac{1}{2} n+\beta\right) \Gamma\left(h+\beta+\frac{1}{2}\right)}{\Gamma\left(\frac{1}{2} n+h+\beta\right)}
\end{aligned}
$$

4.27. (Sec. 4.2) The $i$-distribution. Prove that if $X$ and $Y$ are independently distributed, $X$ having the distribution $N(0,1)$ and $Y$ having the $\chi^{2}$-distribution with $m$ degrees of freedom, then $W=X / \sqrt{Y / m}$ has the density'

$$
\frac{1\left[\frac{1}{2}(m+1)\right]}{\sqrt{m} \sqrt{\pi} \Gamma\left(\frac{1}{2} m\right)}\left(1+\frac{l^{2}}{m}\right)^{-\frac{1}{2}(m+1)}
$$

[Hint: In the joint density of $X$ and $Y$, let $x=t w^{\frac{1}{2}} m^{-\frac{1}{2}}$ and integrate out $w$.]
4,28. (Sec. 4.2) Prove

$$
\mathscr{E} r=\frac{\left(1-\rho^{2}\right)^{\frac{1}{2} n}}{\Gamma\left(\frac{1}{2} n\right)} \sum_{\beta=0}^{\infty} \frac{\rho^{2 \beta+1} \Gamma^{2}[1}{\beta!\Gamma\left[\frac{1}{2} n+\beta+1\right]} .
$$

[Hins: Use Problem 4.26 and the duplication formula for the gamma function.]
4.29. (Sec. 4.2) Show that $\sqrt{n}\left(i_{i j}-\rho_{i j}\right),(i, j)=(1,2),(1,3),(2,3)$, have a joint limiting distribution with variances $\left(1-\rho_{i j}^{2}\right)^{2}$ and covariances of $r_{i j}$ and $r_{i k}, j \neq k$ being $\frac{1}{2}\left(2 \rho_{j k}-\rho_{i j} \rho_{j k}\right)\left(1-\rho_{i j}^{2}-\rho_{i k}^{2}-\rho_{j k}^{2}\right)+\rho_{j k}^{2}$.
4.30. (Sec. 4.3.2) Find a confidence interval for $\rho_{13.2}$ with confidence 0.95 based on $r_{13:}=0.097$ and $N=20$.
4.31. (Scc. 4.3.2) Use Fisher's $=10$ test the hypothesis $\rho_{12.34}=0$ against alternatives $\rho_{1234} \neq 0$ at significance level 0.01 with $r_{12-34}=0.14$ and $N=40$.
4.32. (Sec. 4.3) Show that the incquality $r_{123}^{2} \leq 1$ is the same as the inequality $\left|r_{1 j}\right| \geq 0$. where $\left|r_{i j}\right|$ denotes the determinant of the $3 \times 3$ correlation matrix.
4.33. (Sec. 4.3) Invariance of the sample partial correlation coefficient. Prove that $r_{12 \cdot 3 \ldots} \rho$ is invariant under the transformations $x_{1 \alpha}^{*}=a_{i} x_{i \alpha}+b_{i} x_{\alpha}^{(3)}+c_{i}, a_{i}>0$, $i=1,2, x_{\alpha}^{(3) *}=C x_{\alpha}^{(3)}+b, \alpha=1, \ldots, N$, where $x_{\alpha}^{(3)}=\left(x_{3 \alpha}, \ldots, x_{p \alpha}\right)^{\prime}$, and that any function of $\bar{x}$ and $\hat{\sum}$ that is invariant under these transformations is a function of $r_{12 \cdot 3, \ldots,} \rho$.
4.34. (Sec. 4.4) Invariance of the sample multiple correlation coefficient. Prove that $R$ is a function of the sufficient statistics $\bar{x}$ and $S$ that is invariant under changes of location and scale of $x_{1 \alpha}$ and nonsingular linear transformations of $x_{\alpha}^{(2)}$ (that is. $\left.x_{1_{\alpha}}^{*}=c x_{1_{\alpha}}+d, x_{\alpha}^{(2) *}=C x_{\alpha}^{(2)}+d, \alpha=1, \ldots, N\right)$ and that every function of $\bar{x}$ and $S$ that is invariant is a function of $R$.
4.35. (Sec. 4.4) Prove that conditional on $Z_{1 \alpha}=z_{1 \alpha}, \alpha=1, \ldots, n, R^{2} /\left(1-R^{2}\right)$ is distributed like $T^{2} /\left(N^{*}-1\right)$, where $T^{2}=N^{*} \overline{\boldsymbol{x}}^{\prime} S^{-1} \overline{\boldsymbol{x}}$ based on $N^{*}=n$ observations on a vector $X$ with $p^{*}=p-1$ components, with mean vector $\left(c / \sigma_{11}\right) \sigma_{(\mathrm{b})}^{\prime} \left(n c^{2}=\sum z_{1 \alpha}^{2}\right)$ and covariance matrix $\boldsymbol{\Sigma}_{22 \cdot 1}=\boldsymbol{\Sigma}_{22}-\left(1 / \sigma_{11}\right) \boldsymbol{\sigma}_{(1)} \boldsymbol{\sigma}_{(1)}^{\prime}$. [Hint: The conditional distribution of $Z_{\alpha}^{(2)}$ given $Z_{1 \alpha}=z_{1 \alpha}$ is $N\left[\left(1 / \sigma_{11}\right) \sigma_{(1)} z_{1 \alpha}, \Sigma_{22 \cdot 1}\right]$. There is an $n \times n$ orthogonal matrix $B$ which carries $\left(z_{11}, \ldots, z_{1 n}\right)$ into $(c, \ldots, c)$ and $\left(Z_{i 1}, \ldots, Z_{i n}\right)$ into $\left(Y_{i 1}, \ldots, Y_{i n}, i=2, \ldots, p\right.$. Let the new $X_{\alpha}^{\prime}$ be $\left(Y_{2 \alpha}, \ldots, Y_{\rho \alpha}\right)$.]
4.36. (Sec.4.4) Prove that the noncentrality parameter in the distribution in Problem 4.35 is $\left(a_{11} / \sigma_{11}\right) \bar{R}^{2} /\left(1-\bar{R}^{2}\right)$.
4.37. (Sec. 4.4) Find the distribution of $R^{2} /\left(1-R^{2}\right)$ by multiplying the density of Problem 4.35 by the density of $a_{11}$ and integrating with respect to $a_{11}$.
4.38. (Sec. 4.4) Show that the density of $r^{2}$ derived from (38) of Section 4.2 is identical with (42) in Section 4.4 for $p=2$. [Hint: Use the duplication formula for the gamma function.]
4.39. (Sec. 4.4) Prove that (30) is the uniformly most powerful test of $\bar{R}=0$ based on $r$. [Hint: Use the Neyman-Pearson fundamental lemma.]
4.40. (Sec. 4.4) Prove that (47) is the unique unbiased estimator of $\vec{R}^{2}$ based on $R^{2}$.
4.41. The estimates of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ in Problem 3.1 are

$$
\begin{aligned}
\bar{x} & =\left(\begin{array}{lllll}
185.72 & 151.12 & 183.84 & 149.24
\end{array}\right)^{\prime} \\
S & =\left(\begin{array}{rrrrr}
95.2933 & 52.8683 & 69.6617 & 46.1117 \\
52.8683 & 54.3600 & 51.3117 & 35.0533 \\
99.6617 & 51.3117 & 100.8067 & 56.5400 \\
69.66117 & 35.0533 & 56.5400 & 45.0233
\end{array}\right) .
\end{aligned}
$$

(a) Find the estimates of the parameters of the conditional distribution of ( $x_{3}, x_{4}$ ) given ( $x_{1}, x_{2}$ ); that is, find $S_{21} S_{11}^{-1}$ and $S_{22 \cdot 1}=S_{22}-S_{21} S_{11}^{-1} S_{12}$.
(b) Find the partial correlation $r_{34 \cdot 12}$.
(c) Use Fisher's $z$ to find a confidence interval for $\rho_{34 \cdot 12}$ with confidence 0.95 .
(d) Find the sample multiple correlation coefficients between $x_{;}$and ( $x_{1}, x_{2}$ ) and between $x_{4}$ and ( $x_{1}, x_{2}$ ).
(e) Test the hypotheses that $x_{3}$ is independent of ( $x_{1}, x_{2}$ ) and $x_{4}$ is independent of ( $x_{1}, x_{2}$ ) at significance levels 0.05 .
4.42. Let the components of $X$ correspond to scores on tests in arithmetic speed ( $X_{1}$ ), arithmetic power ( $X_{2}$ ), memory for words ( $X_{3}$ ), memory for meaningful symbols ( $X_{4}$ ), and memory for meaningless symbols ( $X_{5}$ ). The observed correla-
tions in a sample of 140 are [Kelley (1928)]

$$
\left(\begin{array}{lllll}
1.0000 & 0.4248 & 0.0420 & 0.0215 & 0.0573 \\
0.4248 & 1.0000 & 0.1487 & 0.2489 & 0.2843 \\
0.0420 & 0.1487 & 1.0000 & 0.6693 & 0.4662 \\
0.0215 & 0.2489 & 0.6693 & 1.0000 & 0.6915 \\
0.0573 & 0.2843 & 0.4662 & 0.6915 & 1.0000
\end{array}\right)
$$

(a) Find the partial correlation between $X_{4}$ and $X_{5}$, holding $X_{3}$ fixed.
(b) Find the partial correlation between $X_{1}$ and $X_{2}$, holding $X_{3}, X_{4}$, and $X_{5}$ fixed.
(c) Find the multiple correlation between $X_{1}$ and the set $X_{3}, X_{4}$, and $X_{5}$.
(d) Test the hypothesis at the $1 \%$ significance level that arithmetic speed is independent of the three memory scores.
4.43. (Sec. 4.3) Prove that if $\rho_{1 j \cdot q+1, \ldots, p}=0$, then $\sqrt{N-2-(p-q)} r_{i j \cdot q+1, \ldots, p} / \sqrt{1-r_{t / q+1 \ldots, p}^{2}}$ is distributed according to the $t$-distribution with $N-2-(p-q)$ degrees of freedom.
4.44. (Sec. 4.3) Let $X^{\prime}=\left(X_{1}, X_{2}, X^{(2)}\right)$ have the distribution $N(\mu, \Sigma)$. The conditional distribution of $X_{1}$ given $X_{2}=x_{2}$ and $X^{(2)}=x^{(2)}$ is .

$$
N\left[\mu_{1}+\gamma_{2}\left(x_{2}-\mu_{2}\right)+\gamma^{\prime}\left(x^{(2)}-\mu^{(2)}\right), \sigma_{1 \mid \cdot 2, \ldots, p}\right],
$$

where

$$
\left(\begin{array}{ll}
\sigma_{22} & \sigma_{(2)}^{i} \\
\sigma_{(2)} & \Sigma_{22}
\end{array}\right)\binom{\gamma_{2}}{\gamma}=\binom{\sigma_{12}}{\sigma_{(1)}} .
$$

The estimators of $\gamma_{2}$ and $\gamma$ are defined by

$$
\left(\begin{array}{ll}
a_{22} & a_{(2)}^{\prime} \\
a_{(2)} & A_{22}
\end{array}\right)\binom{c_{2}}{c}=\binom{a_{12}}{a_{(1)}}
$$

Show $c_{2}=a_{12 \cdot 3, \ldots, \rho} / a_{22 \cdot 3, \ldots, \rho}$. [Hint: Solve for $c$ in terms of $c_{2}$ and the $a$ 's, and substitute.]
4.45. (Sec. 4.3) In the notation of Problem 4.44, prove

$$
\begin{aligned}
a_{11 \cdot 2, \ldots, \rho} & =a_{11}-a_{(1)}^{i} A_{22}^{-1} a_{(1)}-c_{2}^{2}\left(a_{22}-a_{(2)}^{f} A_{22}^{-1} a_{(2)}\right) \\
& =a_{11 \cdot 3, \ldots, p}-c_{2}^{2} a_{22 \cdot 3, \ldots, \rho} .
\end{aligned}
$$

Hint: Use

$$
a_{11 \cdot 2 \ldots, p}=a_{11}-\left(c_{2} \quad c^{\prime}\right)\left(\begin{array}{ll}
a_{22} & a_{(2)}^{\prime} \\
a_{(2)} & A_{22}
\end{array}\right)\binom{c_{2}}{c}
$$

4.46. (Sec. 4.3) Prove that $1 / a_{22 \cdot 3 \ldots}$ is the eiement in the upper lefi-hand corner of

$$
\left(\begin{array}{ll}
a_{22} & a_{(2)}^{\prime} \\
a_{(2)} & A_{22}
\end{array}\right)^{-1}
$$

4.47. (Sec. 4.3) Using the results in Problems 4.43-4.46, prove that the test for $\rho_{12 \cdot 3, \ldots, p}=0$ is equivalent to the usual $t$-test for $\gamma_{7}=0$.
4.48. Missing observations. Let $X=\left(Y^{\prime} Z^{\prime}\right)^{\prime}$, where $Y$ has $p$ components and $Z$ has $q$ components, be distributed according to $N(\mu, \Sigma)$, where

$$
\boldsymbol{\mu}=\binom{\boldsymbol{\mu}_{y}}{\boldsymbol{\mu}_{z}}, \quad \boldsymbol{\Sigma}=\left(\begin{array}{ll}
\boldsymbol{\Sigma}_{y y} & \boldsymbol{\Sigma}_{y z} \\
\boldsymbol{\Sigma}_{z y} & \boldsymbol{\Sigma}_{z z}
\end{array}\right) .
$$

Let $M$ observations be made on $X$, and $N-M$ additional observations be made on $\boldsymbol{Y}$. Find the maximum likelihood estimates of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$. [Anderson (1957).] [Hint: Express the likelihood function in terms of the marginal density of $Y$ and the conditional density of $Z$ given $Y$.]
4.49. Suppose $X$ is distributed according to $N(\mathbf{0}, \mathbf{\Sigma})$, where

$$
\boldsymbol{\Sigma}=\left(\begin{array}{lll}
1 & \rho & \rho^{2} \\
\rho & 1 & \rho \\
\rho^{2} & \rho & 1
\end{array}\right)
$$

Show that on the basis of one observation, $x^{\prime}=\left(x_{1}, x_{2}, x_{3}\right)$, we can obtain a confidence interval for $\rho$ (with confidence coefficient $1-\alpha$ ) by using as endpoints of the interval the solutions in $t$ of

$$
\left[x_{2}^{2}+\chi_{3}^{2}(\alpha)\right] t^{2}-2\left(x_{1} x_{3}+x_{2} x_{3}\right) t+x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-\chi_{3}^{2}(\alpha)=0,
$$

where $\chi_{3}^{2}(\alpha)$ is the significance point of the $\chi^{2}$-distribution with three degrees of freedom at significance level $\alpha$.

## CHAPTER 5

## The Generalized $T^{2}$-Statistic

### 5.1. INTRODUCTION

One of the most important groups of problems in univariate statistics relates to the mean of a given distribution when the variance of the distribution is unknown. On the basis of a sample one may wish to decide whether the mean is equal to a number specified in advance, or one may wish to give an interval within which the mean lies. The statistic usually used in univariate statistics is the difference between the mean of the sample $\bar{x}$ and the hypothetical population mean $\mu$ divided by the sample standard deviation $s$. If the distribution sampled is $N\left(\mu, \sigma^{2}\right)$, then

$$
I=\sqrt{N} \frac{\bar{x}-\mu}{s}
$$

has the well-known $t$-distribution with $N-1$ degrees of freedo n , where $N$ is the number of observations in the sample. On the basis of this fact, one can set up a test of the hypothesis $\mu=\mu_{0}$, where $\mu_{0}$ is specified, or one can set up a confidence interval for the unknown parameter $\mu$.

The multivariate analog of the square of $t$ given in (1) is

$$
T^{2}=N(\overline{\boldsymbol{x}}-\boldsymbol{\mu})^{\prime} S^{-1}(\overline{\boldsymbol{x}}-\boldsymbol{\mu}),
$$

where $\bar{x}$ is the mean vector of a sample of $N$, and $S$ is the sample covariance matrix. It will be shown how this statistic can be used for testing hypotheses about the mean vector $\mu$ of the population and for obtaining confidence regions for the unknown $\boldsymbol{\mu}$. The distribution of $T^{2}$ will be obtained when $\boldsymbol{\mu}$ in (2) is the mean of the distribution sampled and when $\boldsymbol{\mu}$ is different from

[^0]the population mean. Hotelling (1931) proposed the $T^{2}$-statistic for two samples and derived the distribution when $\boldsymbol{\mu}$ is the population mean.

In Section 5.3 various uses of the $T^{2}$-statistic are presented, including simultaneous confidence intervals for all linear combinations of the mean vector. A James-Stein estimator is given when $\boldsymbol{\Sigma}$ is unknown. The power function of the $T^{2}$-test is treated in Section 5.4, and the multivariate Behrens-Fisher problem in Section 5.5. In Section 5.6, optimum properties of the $T^{2}$-test are considered, with regard to both invariance and admissibility. Stein's criterion for admissibility in the general exponential family is proved and applied. The last section is devoted to inference about the mean in elliptically contoured distributions.

### 5.2. DERIVATION OF THE GENERALIZED $\boldsymbol{T}^{\mathbf{2}}$-STATISTIC AND ITS DISTRIBUTION

### 5.2.1. Derivation of the $\boldsymbol{T}^{\mathbf{2}}$-Statistic As a Function of the Likelihood Ratio Criterion

Although the $T^{2}$-statistic has many uses, we shall begin our discussion by showing that the likelihood ratio test of the hypothesis $H: \boldsymbol{\mu}=\boldsymbol{\mu}_{0}$ on the basis of a sample from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is based on the $T^{2}$-statistic given in (2) of Section 5.1. Suppose we have $N$ observations $x_{1}, \ldots, x_{N}(N>p)$. The likelihood function is

$$
L(\boldsymbol{\mu}, \boldsymbol{\Sigma})=(2 \pi)^{-\frac{1}{2} p N}|\boldsymbol{\Sigma}|^{-\frac{1}{2} N} \exp \left[-\frac{1}{2} \sum_{\alpha=1}^{N}\left(x_{\alpha}-\boldsymbol{\mu}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(x_{\alpha}-\boldsymbol{\mu}\right)\right] .
$$

The observations are given; $L$ is a function of the indeterminates $\boldsymbol{\mu}, \boldsymbol{\Sigma}$. (We shall not distinguish in notation between the indeterminates and the parameters.) The likelihood ratio criterion is

$$
\lambda=\frac{\max _{\Sigma} L\left(\boldsymbol{\mu}_{0}, \mathbf{\Sigma}\right)}{\max _{\boldsymbol{\mu}, \mathbf{\Sigma}} L(\boldsymbol{\mu}, \mathbf{\Sigma})},
$$

that is, the numerator is the maximum of the likelihood function for $\boldsymbol{\mu}, \boldsymbol{\Sigma}$ in the parameter space restricted by the null hypothesis ( $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}, \boldsymbol{\Sigma}$ positive definite), and the denominator is the maximum over the entire parameter space ( $\boldsymbol{\Sigma}$ positive definite). When the parameters are unrestricted, the maximum occurs when $\boldsymbol{\mu}, \boldsymbol{\Sigma}$ are defined by the maximum likelihood estimators
(Section 3.2) of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$,

$$
\begin{aligned}
& \hat{\boldsymbol{\mu}}_{\Omega}=\overline{\boldsymbol{x}} \\
& \hat{\boldsymbol{\Sigma}}_{\Omega}=\frac{1}{N} \sum_{\alpha=1}^{N}\left(x_{\alpha}-\overline{\boldsymbol{x}}\right)\left(x_{\alpha}-\overline{\boldsymbol{x}}\right)^{\prime}
\end{aligned}
$$

When $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}$, the likelihood function is maximized at

$$
\hat{\Sigma}_{\omega}=\frac{1}{N} \sum_{\alpha=1}^{N}\left(x_{\omega}-\mu_{0}\right)\left(x_{\alpha}-\mu_{0}\right)^{\prime}
$$

by Lemma 3.2.2. Furthermore, by Lemma 3.2.2

$$
\begin{aligned}
\max _{\boldsymbol{\Sigma}, \boldsymbol{\mu}} L(\boldsymbol{\mu}, \boldsymbol{\Sigma}) & =\frac{1}{(2 \pi)^{\frac{1}{2} p N}\left|\hat{\boldsymbol{\Sigma}}_{\Omega}\right|^{\frac{1}{2} N}} e^{-\frac{1}{2} p N} \\
\max _{\boldsymbol{\Sigma}} L\left(\boldsymbol{\mu}_{0}, \boldsymbol{\Sigma}\right) & =\frac{1}{(2 \pi)^{\frac{1}{2} p N}\left|\hat{\boldsymbol{\Sigma}}_{\boldsymbol{\omega}}\right|^{\frac{1}{2} N}} e^{-\frac{1}{2} p N}
\end{aligned}
$$

Thus the likelihood ratio criterion is

$$
\begin{aligned}
\lambda & =\frac{\left|\hat{\boldsymbol{\Sigma}}_{\Omega}\right|^{\frac{1}{2} N}}{\left|\hat{\boldsymbol{\Sigma}}_{\omega}\right|^{\frac{1}{2} N}}=\frac{\left|\sum\left(\boldsymbol{x}_{\alpha}-\overline{\boldsymbol{x}}\right)\left(\boldsymbol{x}_{\alpha}-\overline{\boldsymbol{x}}\right)^{\prime}\right|^{\frac{1}{2} N}}{\left|\sum\left(\boldsymbol{x}_{\alpha}-\boldsymbol{\mu}_{0}\right)\left(\boldsymbol{x}_{\alpha}-\boldsymbol{\mu}_{0}\right)^{\prime}\right|^{\frac{1}{2} N}} \\
& =\frac{|\boldsymbol{A}|^{\frac{1}{2} N}}{\left|\boldsymbol{A}+N\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)^{\prime}\right|^{\frac{1}{2} N}}
\end{aligned}
$$

where

$$
A=\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}=(N-1) S .
$$

Application of Corollary A.3.1 of the Appendix shows

$$
\begin{aligned}
\lambda^{2 / N} & =\frac{|\boldsymbol{A}|}{\left|\boldsymbol{A}+\left[\sqrt{N}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)\right]\left[\sqrt{N}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)\right]^{\prime}\right|} \\
& =\frac{1}{1+N\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)^{\prime} A^{-1}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)} \\
& =\frac{1}{\mathbf{1}+T^{2} /(N-1)}
\end{aligned}
$$

where
(11) $\quad T^{2}=N\left(\bar{x}-\mu_{0}\right)^{\prime} S^{-1}\left(\bar{x}-\mu_{0}\right)=(N-1) N\left(\bar{x}-\mu_{0}\right)^{\prime} A^{-1}\left(\bar{x}-\mu_{0}\right)$.


[^0]:    An Inrroduction to Mulvivariate Statistical Andhsis. Third Edition. By T. W. Anderson ISBN 0-471-36091-0 Copyright © 2003 John Wiley \& Sons, Inc.



The likelihood ratio test is defined by the critical region (region of rejection)

$$
\lambda \leq \lambda_{0},
$$

where $\lambda_{0}$ is chosen so that the probability of (12) when the null hypothesis is true is equal to the significance level. If we take the $\frac{1}{2} N$ th root of both sides of (12) and invert, subtract 1 , and multiply by $N-1$, we obtain

$$
T^{2} \geq T_{0}^{2},
$$

where

$$
T_{0}^{2}=(N-1)\left(\lambda_{0}^{-2 / N}-1\right) .
$$

Theorem 5.2.1. The likelihood ratio test of the hypothesis $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}$ for the distribution $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is given by (13), where $T^{2}$ is defined by (11), $\overline{\boldsymbol{x}}$ is the mean of a sample of $N$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma}), S$ is the covariance matrix of the sample, and $T_{0}^{-2}$ is chosen so that the probability of (13) under the null hypothesis is equal to the chosen significance level.

The Student $t$-test has the property that when testing $\mu=0$ it is invariant with respect to scale transformations. If the scalar random variable $X$ is distributed according to $N\left(\mu, \sigma^{2}\right)$, then $X^{*}=c X$ is distributed according to $N\left(c \mu, c^{2} \sigma^{2}\right)$, which is in the same class of distributions, and the hypothesis $\mathscr{E} X=0$ is equivalent to $\mathscr{E} X^{*}=\mathscr{E} c X=0$. If the observations $x_{\alpha}$ are transformed similarly $\left(x_{\alpha}^{*}=c x_{\alpha}\right)$, then, for $c>0, t^{*}$ computed from $x_{\alpha}^{*}$ is the same as $t$ computed from $x_{\alpha}$. Thus, whatever the unit of measurement the statistical result is the same.

The generalized $T^{2}$-test has a similar property. If the vector random variable $\boldsymbol{X}$ is distributed according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, then $\boldsymbol{X}^{*}=\boldsymbol{C} \boldsymbol{X}($ for $|\boldsymbol{C}| \neq \mathbf{0})$ is distributed according to $N\left(\boldsymbol{C} \boldsymbol{\mu}, \boldsymbol{C} \boldsymbol{\Sigma} \boldsymbol{C}^{\prime}\right)$, which is in the same class of distributions. The hypothesis $\mathscr{E} \boldsymbol{X}=\mathbf{0}$ is equivalent to the hypothesis $\mathscr{E} \boldsymbol{X}^{*}=\mathscr{E} \boldsymbol{C X}=\mathbf{0}$. If the observations $x_{\alpha}$ are transformed in the same way, $x_{\alpha}^{*}=C x_{\alpha}$, then $T^{* 2}$ computed on the basis of $\boldsymbol{x}_{\alpha}^{*}$ is the same as $T^{2}$ computed on the basis of $\boldsymbol{x}_{\alpha}$. This follows from the facts that $\bar{x}^{*}=C \bar{x}$ and $A=C A C^{\prime}$ and the following lemma:

Lemma-5.2.1. For any $p \times p$ nonsingular matrices $\boldsymbol{C}$ and $\boldsymbol{H}$ and atty vector $\boldsymbol{k}$,

$$
k^{\prime} H^{-1} k=(C k)^{\prime}\left(C H C^{\prime}\right)^{-1}(C k) .
$$

Proof. The right-hand side of (15) is

$$
\begin{aligned}
(C k)^{\prime}\left(C H C^{\prime}\right)^{-1}(C k) & =k^{\prime} C^{\prime}\left(C^{\prime}\right)^{-1} H^{-1} C^{-1} C k \\
& =k^{\prime} H^{-1} k .
\end{aligned}
$$

We shall show in Section 5.6 that of all tests invariant with respect to such transformations, (13) is the uniformly most powerful.

We can give a geometric interpretation of the $\frac{1}{2} N$ th root of the likelihood ratio criterion,

$$
\lambda^{2 / N}=\frac{\left|\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}\right|}{\left|\sum_{\alpha=1}^{N}\left(x_{\alpha}-\mu_{0}\right)\left(x_{\alpha}-\mu_{0}\right)^{\prime}\right|},
$$

in terms of parallelotopes. (See Section 7.5.) In the $p$-dimensional representation the numerator of $\lambda^{2 / N}$ is the sum of squares of volumes of all parallelotopes with principal edges $p$ vectors, each with one endpoint at $\bar{x}$ and the other at an $\boldsymbol{x}_{\mathbf{a}}$. The denominator is the sum of squares of volumes of all parallelotopes with principal edges $p$ vectors, each with one endpoint at $\boldsymbol{\mu}_{0}$ and the other at $\boldsymbol{x}_{\alpha}$. If the sum of squared volumes involving vectors emanating from $\bar{x}$, the "center" of the $x_{\mathrm{a}}$, is much less than that involving vectors emanating from $\boldsymbol{\mu}_{0}$, then we reject the hypothesis that $\boldsymbol{\mu}_{0}$ is the mean of the distribution.

There is also an interpretation in the $N$-dimensional representation. Let $y_{1}=\left(x_{1}, \ldots, x_{1 N}\right)^{\prime}$ be the $i$ th vector. Then

$$
\sqrt{N} \bar{x}_{1}=\sum_{\alpha=1}^{N} \frac{1}{\sqrt{N}} x_{1 \alpha}
$$

is the distance from the origin of the projection of $y_{t}$ on the equiangular line (with direction cosines $1 / \sqrt{N}, \ldots, 1 / \sqrt{N}$ ). The coordinates of the projection are $\left(\bar{x}_{1}, \ldots, \bar{x}_{1}\right)$. Then $\left(x_{i 1}-\bar{x}_{i}, \ldots, x_{i N}-\bar{x}_{i}\right)$ is the projection of $y_{i}$ on the plane through the origin perpendicular to the equiangular line. The numerator of $\lambda^{2 / N}$ is the square of the $p$-dimensional volume of the parallelotope with principal edges, the vectors ( $x_{11}-\bar{x}_{1}, \ldots, x_{1 N}-\bar{x}_{i}$ ). A point ( $x_{i 1}- \mu_{0 i}, \ldots, x_{i N}-\mu_{0 i}$ ) is obtained from $y_{i}$ by translation parallel to the equiangular line (by a distance $\sqrt{N} \mu_{0 i}$ ). The denominator of $\lambda^{2 / N}$ is the square of the volume of the parallelotope with principal edges these vectors. Then $\lambda^{2 / N}$ is the ratio of these squared volumes.

### 5.2.2. The Distribution of $\boldsymbol{T}^{\mathbf{2}}$

In this subsection we will find the distribution of $T^{2}$ under general conditions, including the case when the null hypothesis is not true. Let $T^{2}=Y^{\prime} S^{-1} Y$ where $\boldsymbol{Y}$ is distributed according to $N(\boldsymbol{\nu}, \boldsymbol{\Sigma})$ and $n S$ is distributed independently as $\sum_{n=1}^{n} Z_{n} Z_{r}^{\prime}$ with $Z_{1}, \ldots, Z_{n}$ independent, each with distribution
$N(\mathbf{0}, \boldsymbol{\Sigma})$. The $T^{2}$ defined in Section 5.2.1 is a special case of this with $\boldsymbol{Y}=\sqrt{N}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)$ and $\boldsymbol{v}=\sqrt{N}\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)$ and $n=N-1$. Let $\boldsymbol{D}$ be a nonsingular matrix such that $\boldsymbol{D} \boldsymbol{\Sigma} \boldsymbol{D}^{\prime}=\boldsymbol{I}$, and define

$$
Y^{*}=D Y, \quad S^{*}=D S D^{\prime}, \quad v^{*}=D v .
$$

Then $T^{2}=\mathbf{Y}^{*} \boldsymbol{S}^{*-1} \mathbf{Y}^{*}$ (by Lemma 5.2.1), where $\mathbf{Y}^{*}$ is distributed according to $N\left(\nu^{*}, I\right)$ and $n S^{*}$ is distributed independently as $\sum_{\alpha=1}^{n} Z_{\alpha}^{*} Z_{\alpha}^{* \prime}= \sum_{\alpha=1}^{n} D Z_{\alpha}\left(D Z_{\alpha}\right)^{\prime}$ with the $Z_{\alpha}^{*}=D Z_{\alpha}$ independent, each with distribution $N(\mathbf{0}, \boldsymbol{I})$. We note $\boldsymbol{v}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{v}=\boldsymbol{v}^{* \prime}(\boldsymbol{I})^{-1} \boldsymbol{v}^{*}=\boldsymbol{v}^{* \prime} \boldsymbol{v}^{*}$ by Lemma 5.2.1.

Let the frist row of a $p \times p$ orthogonal matrix $Q$ be defined by

$$
q_{1 i}=\frac{Y_{i}^{*}}{\sqrt{Y^{*} Y^{*}}}, \quad i=1, \ldots, p
$$

this is permissible because $\sum_{l=1}^{P} q_{1 i}^{2}=1$. The other $p-1$ rows can be defined by some arbitrary rule (Lemma A.4.2 of the Appendix). Since $Q$ depends on $Y^{*}$, it is a random matrix. Now let

$$
\begin{aligned}
& U=Q Y^{*} \\
& B=Q n S^{*} Q^{\prime} .
\end{aligned}
$$

From the way $Q$ was defined,

$$
\begin{aligned}
U_{1} & =\sum q_{1 i} Y_{1}^{*}=\sqrt{\mathbf{Y}^{* \prime} \mathbf{Y}^{*}} \\
U_{j} & =\sum q_{j i} Y_{1}^{*}=\sqrt{\mathbf{Y}^{* \prime} \mathbf{Y}^{*}} \sum q_{j t} q_{1 i}=0 .
\end{aligned}
$$

Then

$$
\begin{aligned}
\frac{T^{2}}{n} & =U^{\prime} B^{-1} U=\left(U_{1}, 0, \ldots, 0\right)\left(\begin{array}{cccc}
b^{11} & b^{12} & \cdots & b^{1 p} \\
b^{21} & b^{22} & \cdots & b^{2 p} \\
\vdots & \vdots & & \vdots \\
b^{p 1} & b^{p 2} & \cdots & b^{p p}
\end{array}\right)\left(\begin{array}{c}
U_{1} \\
0 \\
\vdots \\
0
\end{array}\right) \\
& =U_{1}^{2} b^{11},
\end{aligned}
$$

where $\left(b^{i j}\right)=\boldsymbol{B}^{-1}$. By Theorem A.3.3 of the Appendix, $1 / b^{11}=b_{11}$ $\boldsymbol{b}_{(1)}^{\prime} \boldsymbol{B}_{22}^{-1} \boldsymbol{b}_{(1)}=b_{11 \cdot 2, \ldots, p}$, where

$$
\boldsymbol{B}=\left(\begin{array}{ll}
b_{11} & \boldsymbol{b}_{(1)}^{\prime} \\
\boldsymbol{b}_{(1)} & \boldsymbol{B}_{22}
\end{array}\right),
$$

and $T^{2} / n=U_{1}^{2} / b_{11 \cdot 2, \ldots, p}=\mathbf{Y}^{*} \mathbf{Y}^{*} / b_{11 \cdot 2, \ldots, p}$. The conditional distribution of $\boldsymbol{B}$ given $\boldsymbol{\varrho}$ is that of $\sum_{\alpha=1}^{n} V_{\alpha} V_{\alpha}^{\prime}$, where conditionally the $V_{\alpha}=Q Z_{\alpha}^{*}$ are
independent, each with distribution $N(\mathbf{0}, \boldsymbol{I})$. By Theorem $4.3 .3 b_{11,2, \ldots, p}$ is conditionally distributed as $\sum_{\alpha=1}^{n-(\rho-1)} W_{\alpha ;}^{2}$, where conditionally the $W_{\alpha}$ are independent, each with the distribution $N(0,1)$; that is, $b_{11 \cdot 2, \ldots, p}$ is conditionally distributed as $\chi^{2}$ with $n-(p-1)$ degrees of freedom. Since the conditional distribution of $b_{11 \cdot 2, \ldots, p}$ does not depend on $Q$, it is unconditionally distributed as $\chi^{2}$. The quantity $\boldsymbol{Y}^{* \prime} \boldsymbol{Y}^{*}$ has a noncentral $\chi^{2}$-distribution with $p$ degrees of freedom and noncentrality parameter $\boldsymbol{\nu}^{* \prime} \boldsymbol{\nu}^{*}=\boldsymbol{\nu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\nu}$. Then $T^{2} / n$ is distributed as the ratio of a noncentral $\chi^{2}$ and an independent $\chi^{2}$.

Theorem 5.2.2. Let $T^{2}=\mathbf{Y}^{\prime} \mathbf{S}^{-1} \mathbf{Y}$, where $\mathbf{Y}$ is distributed according to $N(\boldsymbol{\nu}, \boldsymbol{\Sigma})$ and $n \boldsymbol{S}$ is independently distributed as $\Sigma_{n=1}^{\prime \prime} Z_{\alpha} Z_{n}^{\prime}$ with $Z_{1}, \ldots, Z_{n}$ independent, each with distribution $N(\mathbf{0}, \boldsymbol{\Sigma})$. Then $\left.\left(T^{2} / n\right)[n-p+1) / p\right]$ is distributed as a noncentral $F$ with $p$ and $n-p+1$ degrees of freedom and noncentrality parameter $\boldsymbol{\nu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\nu}$. If $\boldsymbol{\nu}=\mathbf{0}$, the distribution is central $F$.

We shall call this the $T^{2}$-distribution with $n$ degrees of freedom.

Corollary 5.2.1. Let $x_{1}, \ldots, x_{N}$ be a sample from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, and let $T^{2}= N\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right) \boldsymbol{S}^{-1}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)$. The distribution of $\left[T^{2} /(N-1)\right][(N-p) / p]$ is noncentral $F$ with $p$ and $N-p$ degrees of freedom and noncentrality parameter $N\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)$. If $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}$, then the $F$-distribution is central.

The above derivation of the $T^{2}$-distribution is due to Bowker (1960). The noncentral $F$-density and tables of the distribution are discussed in Section 5.4.

For large samples the distribution of $T^{2}$ given by Corollary 5.2.1 is approximately valid even if the parent distribution is not normal; in this sense the $T^{2}$-test is a robust procedure.

Theorem 5.2.3. Let $\left\{X_{\alpha}\right\}, \alpha=1,2, \ldots$, be a sequence of independently identically distributed random vectors with mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$; let $\overline{\boldsymbol{X}}_{N}=(1 / N) \Sigma_{\alpha=1}^{N} \boldsymbol{X}_{\alpha}, \boldsymbol{S}_{N}=[1 /(N-1)] \Sigma_{\alpha=1}^{N}\left(\boldsymbol{X}_{\alpha}-\overline{\boldsymbol{X}}_{N}\right)\left(\boldsymbol{X}_{\alpha}-\overline{\boldsymbol{X}}_{N}\right)^{\prime}$, and $T_{N}^{2}=N\left(\overline{\boldsymbol{X}}_{N}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{S}_{N}^{-1}\left(\overline{\boldsymbol{X}}_{N}-\boldsymbol{\mu}_{0}\right)$. Then the limiting distribution of $T_{N}^{2}$ as $N \rightarrow \infty$ is the $\chi^{2}$-distribution with $p$ degrees of freedom if $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}$.

Proof. By the central limit theorem (Theorem 4.2.3) ine limiting distribution of $\sqrt{N}\left(\overline{\boldsymbol{X}}_{N}-\boldsymbol{\mu}\right)$ is $N(\mathbf{0}, \boldsymbol{\Sigma})$. The sample covariance matrix converges stochastically to $\boldsymbol{\Sigma}$. Then the limiting distribution of $T_{N}^{2}$ is the distribution of $\mathbf{Y}^{\prime} \boldsymbol{\Sigma}^{-1} \mathbf{Y}$, where $\mathbf{Y}$ has the distribution $N(\mathbf{0}, \boldsymbol{\Sigma})$. The theorem follows from Theorem 3.3.3.

When the null hypothesis is true, $T^{2} / n$ is distributed as $\chi_{p}^{2} / \chi_{n-p+1}^{2}$, and $\lambda^{2 / N}$ given by (10) has the distribution of $\chi_{n-p+1}^{2} /\left(\chi_{n-p+1}^{2}+\chi_{p}^{2}\right)$. The density of $V=\chi_{a}^{2} /\left(\chi_{a}^{2}+\chi_{b}^{2}\right)$, when $\chi_{a}^{2}$ and $\chi_{b}^{2}$ are independent. is

$$
\frac{\Gamma\left[\frac{1}{2}(a+b)\right]}{\Gamma\left(\frac{1}{2} a\right) \Gamma\left(\frac{1}{2} b\right)} v^{\frac{1}{2} a-1}(1-v)^{\frac{1}{2} b-1}=\beta\left(v ; \frac{1}{2} a, \frac{1}{2} b\right) ;
$$

this is the density of the beta distribution with parameters $\frac{1}{2} d$ and $\frac{1}{2} b$ (Problem 5.27). Thus the distribution of $\lambda^{2 ; N}=\left(1+T^{2} / n\right)^{-1}$ is the beta distribution with parameters $\frac{1}{2} p$ and $\frac{1}{2}(n-p+1)$.

### 5.3. USES OF THE $\boldsymbol{T}^{2}$-STATISTIC

### 5.3.1. Testing the Hypothesis That the Mean Vector Is a Given Vector

The likelihood ratio test of the hypothesis $\boldsymbol{\mu}=\boldsymbol{\mu}_{0}$ on the basis of a sample of $N$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is equivalent to

$$
T^{2} \geq T_{0}^{2}
$$

as given in Section 5.2.1. If the significance level is $\alpha$, then the $100 \alpha \%$ point of the $F$-distribution is taken, that is,

$$
T_{0}^{2}=\frac{(N-1) p}{\overline{N-p}} F_{\rho, N-\rho}(\alpha)=T_{\rho, N-1}^{2}(\alpha),
$$

say. The choice of significance level may depend on the power of the test. We shall discuss this in Section 5.4.

The statistic $T^{2}$ is computed from $\overline{\boldsymbol{x}}$ and $\boldsymbol{A}$. The vector $\boldsymbol{A}^{-1}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)=\boldsymbol{b}$ is the solution of $\boldsymbol{A} \boldsymbol{b}=\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}$. Then $T^{2} /(N-1)=N\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{b}$.

Note that $T^{2} /(N-1)$ is the nonzero root of

$$
\left|N\left(\bar{x}-\boldsymbol{\mu}_{0}\right)\left(\bar{x}-\boldsymbol{\mu}_{0}\right)^{\prime}-\lambda A\right|=0 .
$$

Lemma 5.3.1. If $\boldsymbol{v}$ is a vector of $\boldsymbol{p}$ components and if $\boldsymbol{B}$ is a nonsingular $p \times p$ matrix, then $\boldsymbol{v}^{\prime} \boldsymbol{B}^{-1} \boldsymbol{v}$ is the nonzero root of

$$
\left|\boldsymbol{\nu} \boldsymbol{\nu}^{\prime}-\lambda \boldsymbol{B}\right|=0 .
$$

Proof. The nonzero root, say $\lambda_{1}$, of (4) is associated with a characteristic vector $\boldsymbol{\beta}$ satisfying

$$
\nu \nu^{\prime} \beta=\lambda_{1} B \beta .
$$

![](https://cdn.mathpix.com/cropped/ec040d83-777d-4837-ae04-3d5c1077084f-196.jpg?height=323&width=634&top_left_y=236&top_left_x=489)
Figure 5.1. A confidence ellipse.

Since $\lambda_{1} \neq 0, \boldsymbol{\nu}^{\prime} \boldsymbol{\beta} \neq \mathbf{0}$. Multiplying on the left by $\boldsymbol{\nu}^{\prime} \boldsymbol{B}^{-1}$, we obtain

$$
\left(\boldsymbol{\nu}^{\prime} \boldsymbol{B}^{-1} \boldsymbol{\nu}\right)\left(\boldsymbol{\nu}^{\prime} \boldsymbol{\beta}\right)=\lambda_{1}\left(\boldsymbol{\nu}^{\prime} \boldsymbol{\beta}\right) .
$$

In the case above $\boldsymbol{\nu}=\sqrt{N}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)$ and $\boldsymbol{B}=\boldsymbol{A}$.

### 5.3.2. A Confidence Region for the Mean Vector

If $\boldsymbol{\mu}$ is the mean of $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, the probability is $1-\alpha$ of drawing a sample of $N$ with mean $\bar{x}$ and covariance matrix $S$ such that

$$
N(\bar{x}-\boldsymbol{\mu})^{\prime} S^{-1}(\bar{x}-\boldsymbol{\mu}) \leq T_{p, N-1}^{2}(\alpha) .
$$

Thus, if we compute (7) for a particular sample, we have confidence $1-\alpha$ that (7) is a true statement concerning $\boldsymbol{\mu}$. The inequality

$$
N(\bar{x}-m)^{\prime} S^{-1}(\bar{x}-m) \leq T_{p . N-1}^{2}(\alpha)
$$

is the interior and boundary of an ellipsoid in the $p$-dimensional space of $m$ with center at $\overline{\boldsymbol{x}}$ and with size and shape depending on $S^{-1}$ and $\alpha$. See Figure 5.1. We state that $\mu$ lies within this ellipsoid with confidence $1-\alpha$. Over random samples (8) is a random ellipsoid.

### 5.3.3. Simultaneous Confidence Intervals for All Linear Combinations of the Mean Vector

From the confidence region (8) for $\mu$ we can obtain confidence intervals for linear functions $\boldsymbol{\gamma}^{\prime} \boldsymbol{\mu}$ that hold simultaneously with a given confidence coefficient.

Lemma 5.3.2 (Generalized Cauchy-Schwarz Inequality). For a positive definite matrix $S$,

$$
\left(\gamma^{\prime} y\right)^{2} \leq \gamma^{\prime} S \gamma y^{\prime} S^{-1} y .
$$

Proof. Let $b=\boldsymbol{\gamma}^{\prime} \boldsymbol{y} / \boldsymbol{\gamma}^{\prime} \boldsymbol{S} \boldsymbol{\gamma}$. Then

$$
\begin{aligned}
0 & \leq(y-b S \gamma)^{\prime} S^{-1}(y-b S \gamma) \\
& =y^{\prime} S^{-1} y-b \gamma^{\prime} S S^{-1} y-y^{\prime} S^{-1} S \gamma b+b^{2} \gamma^{\prime} S S^{-1} S \gamma \\
& =y^{\prime} S^{-1} y-\frac{\left(\gamma^{\prime} y\right)^{2}}{\gamma^{\prime} S \gamma}
\end{aligned}
$$

which yields (9).
When $\boldsymbol{y}=\overline{\boldsymbol{x}}-\boldsymbol{\mu}$, then (9) implies that

$$
\begin{aligned}
\left|\boldsymbol{\gamma}^{\prime}(\overline{\boldsymbol{x}}-\boldsymbol{\mu})\right| & \leq \sqrt{\boldsymbol{\gamma}^{\prime} \boldsymbol{S} \boldsymbol{\gamma}(\overline{\boldsymbol{x}}-\boldsymbol{\mu})^{\prime} \boldsymbol{S}^{-1}(\overline{\boldsymbol{x}}-\boldsymbol{\mu})} \\
& \leq \sqrt{\boldsymbol{\gamma}^{\prime} \boldsymbol{S} \boldsymbol{\gamma}} \sqrt{T_{p, N-1}^{2}(\alpha) / N}
\end{aligned}
$$

holds for all $\gamma$ with probability $1-\alpha$. Thus we can assert with confidence $1-\alpha$ that the unknown parameter vector satisfies simultaneously for all $\gamma$ the inequalities

$$
\left|\boldsymbol{\gamma}^{\prime} \overline{\boldsymbol{x}}-\boldsymbol{\gamma}^{\prime} \boldsymbol{m}\right| \leq \sqrt{\boldsymbol{\gamma}^{\prime} \boldsymbol{S} \boldsymbol{\gamma}} \sqrt{T_{p, N-1}^{2}(\alpha) / N} .
$$

The confidence region (8) can be explored by setting $\boldsymbol{\gamma}$ in (12) equal to simple vectors such as $(1,0, \ldots, 0)^{\prime}$ to obtain $m_{1},(1,-1,0, \ldots, 0)$ to yield $m_{1}-m_{2}$, and so on. It should be noted that if only one linear function $\boldsymbol{\gamma}^{\prime} \boldsymbol{\mu}$ were of interest, $\sqrt{T_{p, N-1}^{2}(\alpha)}=\sqrt{n p F_{p, n-p+1}(\alpha) /(n-p+1)}$ would be replaced by $t_{n}(\alpha)$.

### 5.3.4. Two-Sample Problems

Another situation in which the $T^{2}$-statistic is used is one in which the null hypothesis is that the mean of one normal population is equal to the mean of the other where the covariance matrices are assumed equal but unknown. Suppose $y_{1}^{(i)}, \ldots, y_{N_{t}}^{(t)}$ is a sample from $N\left(\boldsymbol{\mu}^{(i)}, \boldsymbol{\Sigma}\right), i=1,2$. We wish to test the null hypothesis $\boldsymbol{\mu}^{(1)}=\boldsymbol{\mu}^{(2)}$. The vector $\overline{\boldsymbol{y}}^{(i)}$ is distributed according to $N\left[\boldsymbol{\mu}^{(i)},\left(1 / N_{i}\right) \boldsymbol{\Sigma}\right]$. Consequently $\sqrt{N_{1} N_{2} /\left(N_{1}+N_{2}\right)}\left(\overline{\boldsymbol{y}}^{(1)}-\overline{\boldsymbol{y}}^{(2)}\right)$ is distributed according to $N(\mathbf{0}, \Sigma$ ! under the null hypothesis. If we let

$$
\begin{aligned}
S=\frac{1}{N_{1}+N_{2}-2}\left\{\sum _ { \alpha = 1 } ^ { N _ { 1 } } ( y _ { \alpha } ^ { ( 1 ) } - \overline { y } ^ { ( 1 ) } ) \left(y_{\alpha}^{(1)}\right.\right. & \left.-\bar{y}^{(1)}\right)^{\prime} \\
& \left.+\sum_{\alpha=1}^{N_{2}}\left(y_{\alpha}^{(2)}-\bar{y}^{(2)}\right)\left(y_{\alpha}^{(2)}-\bar{y}^{(2)}\right)^{\prime}\right\}
\end{aligned}
$$

then $\left(N_{1}+N_{2}-2\right) S$ is distributed as $\sum_{\alpha=1}^{N_{1}+N_{2}-2} Z_{\alpha} Z_{\alpha}^{\prime}$, where $Z_{\alpha}$ is distributed according to $N(\mathbf{0}, \mathbf{\Sigma})$. Thus

$$
T^{2}=\frac{N_{1} N_{2}}{N_{1}+N_{2}}\left(\bar{y}^{(1)}-\bar{y}^{(2)}\right)^{\prime} S^{-1}\left(\bar{y}^{(1)}-\bar{y}^{(2)}\right)
$$

is distributed as $T^{2}$ with $N_{1}+N_{2}-2$ degrees of freedom. The critical region is

$$
T^{2}>\frac{\left(N_{1}+N_{2}-2\right) p}{N_{1}+N_{2}-p-1} F_{p, N_{1}+N_{2}-p-1}(\alpha)
$$

with significance level $\alpha$.
A confidence region for $\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}$ with confidence level $1-\alpha$ is the set of vectors $m$ satisfying

$$
\begin{aligned}
\left(\bar{y}^{(1)}\right. & \left.-\bar{y}^{(2)}-m\right)^{\prime} S^{-1}\left(\bar{y}^{(1)}-\bar{y}^{(2)}-m\right) \\
& \leq \frac{N_{1}+N_{2}}{N_{1} N_{2}} T_{p, N_{1}+N_{2}-2}^{2}(\alpha) \\
& =\frac{N_{1}+N_{2}}{N_{1} N_{2}} \frac{\left(N_{1}+N_{2}-2\right) p}{N_{1}+N_{2}-p-1} F_{p, N_{1}+N_{2}-p-1}(\alpha)
\end{aligned}
$$

Simultaneous confidence intervals are

$$
\left|\gamma^{\prime}\left(\bar{y}^{(1)}-\bar{y}^{(2)}\right)-\gamma^{\prime} m\right| \leq \sqrt{\gamma^{\prime} S \gamma} \sqrt{\frac{N_{1}+N_{2}}{N_{1} N_{2}} T_{p, N_{1}+N_{2}-2}^{2}(\alpha)} .
$$

An example may be taken from Fisher (1936). Let $x_{1}=$ sepal length, $x_{2}=$ sepal width, $x_{3}=$ petal length, $x_{4}=$ petal width. Fifty observations are taken from the population Iris versicolor (1) and 50 from the population Iris setosa (2). See Table 3.4. The data may be sumunarized (in centimeters) as

$$
\begin{aligned}
& \bar{x}^{(1)}=\left(\begin{array}{l}
5.936 \\
2.770 \\
4.260 \\
1.326
\end{array}\right), \\
& \bar{x}^{(2)}=\left(\begin{array}{l}
5.006 \\
3.428 \\
1.462 \\
0.246
\end{array}\right),
\end{aligned}
$$

$$
98 S=\left(\begin{array}{rrrr}
19.1434 & 9.0356 & 9.7634 & 3.2394 \\
9.0356 & 11.8658 & 4.6232 & 2.4746 \\
9.7634 & 4.6232 & 12.2978 & 3.8794 \\
3.2394 & 2.4746 & 3.8794 & 2.4604
\end{array}\right) .
$$

The value of $T^{2} / 98$ is 26.334 , and $\left(T^{2} / 98\right) \times \frac{95}{4}=625.5$. This value is highly significant c.mpared to the $F$-value for 4 and 95 degrees of freedom of 3.52 at the 0.01 significance level.

Simultaneous confidence intervals for the differences of component means $\mu_{i}^{(1)}-\mu_{1}^{(2)}, i=1,2,3,4$, are $0.930 \pm 0.337,-0.658 \pm 0.265,-2.798 \pm 0.270$. and $1.080 \pm 0.121$. In each case 0 does not lie in the interval. [Since $t_{9 s}(.01)< T_{4,98}(.01)$, a univariate test on any component would lead to rejection of the null hypothesis.] The last two components show the most significant differences from 0 .

### 5.3.5. A Problem of Several Samples

After considering the above example, Fisher considers a third sample drawn from a population assumed to have the same covariance matris. He treats the same measurements on 50 Iris virginica (Table 3.4). There is a theoretical reason for believing the gene structures of these three species to be such that the mean vectors of the three populations are related as

$$
3 \boldsymbol{\mu}^{(1)}=\boldsymbol{\mu}^{(3)}+2 \boldsymbol{\mu}^{(2)},
$$

where $\boldsymbol{\mu}^{(3)}$ is the mean vector of the third population.
This is a special case of the following general problem. Let $\left\{x_{\alpha}^{(\cdot)}\right\} . \alpha= 1, \ldots, N_{t}, i=1, \ldots, q$, be samples from $N\left(\boldsymbol{\mu}^{(t)}, \boldsymbol{\Sigma}\right), i=1, \ldots, q$, respectively. Let us test the hypothesis

$$
H: \sum_{i=1}^{q} \beta_{1} \boldsymbol{\mu}^{(1)}=\boldsymbol{\mu},
$$

where $\beta_{1}, \ldots, \beta_{q}$ are given scalars and $\boldsymbol{\mu}$ is a given vector. The criterion is

$$
T^{2}=c\left(\sum_{i=1}^{q} \beta_{i} \bar{x}^{(l)}-\mu\right)^{\prime} S^{-1}\left(\sum_{t=1}^{q} \beta_{i} \bar{x}^{(l)}-\mu\right) .
$$

where

$$
\bar{x}^{(t)}=\frac{1}{N_{t}} \sum_{\alpha=1}^{N_{t}} x_{\alpha}^{(1)},
$$

$$
\begin{aligned}
\left(\sum_{i=1}^{q} N_{i}-q\right) S & =\sum_{i=1}^{q} \sum_{\alpha=1}^{N_{i}}\left(x_{\alpha}^{(i)}-\bar{x}^{(i)}\right)\left(x_{\alpha}^{(i)}-\bar{x}^{(i)}\right)^{\prime} \\
\frac{1}{c} & =\sum_{i=1}^{q} \frac{\beta_{i}^{2}}{N_{i}} .
\end{aligned}
$$

This $T^{2}$ has the $T^{2}$-distribution with $\sum_{i=1}^{q} N_{i}-q$ degrees of freedom.
Fisher actually assumes in his example that the covariance matrices of the three populations may be different. Hence he uses the technique described in Section 5.5.

### 53.6. A Problem of Symmetry

Consider testing the hypothesis $H: \mu_{1}=\mu_{2}=\cdots=\mu_{p}$ on the basis of a sample $x_{1}, \ldots, x_{N}$ from $N(\mu, \Sigma)$, where $\boldsymbol{\mu}^{\prime}=\left(\mu_{1}, \ldots, \mu_{p}\right)$. Let $\boldsymbol{C}$ be any $(p-1) \times p$ matrix of rank $p-1$ such that

$$
C_{\varepsilon}=0,
$$

where $\varepsilon^{\prime}=(1, \ldots, 1)$. Then

$$
y_{\alpha}=C x_{\alpha}, \quad \alpha=1, \ldots, N,
$$

has mean $\boldsymbol{C} \boldsymbol{\mu}$ and covariance matrix $\boldsymbol{C} \boldsymbol{\Sigma} \boldsymbol{C}^{\prime}$. The hypothesis $H$ is $\boldsymbol{C} \boldsymbol{\mu}=\mathbf{0}$. The statistic to be used is

$$
T^{2}=N \bar{y}^{\prime} \boldsymbol{S}^{-1} \bar{y}
$$

where

$$
\begin{aligned}
\bar{y} & =\frac{1}{N} \sum_{\alpha=1}^{N} y_{\alpha}=C \bar{x} \\
S & =\frac{1}{N-1} \sum_{\alpha=1}^{N}\left(y_{\alpha}-\bar{y}\right)\left(y_{\alpha}-\bar{y}\right)^{\prime} \\
& =\frac{1}{N-1} C \sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime} C^{\prime}
\end{aligned}
$$

This statistic has the $T^{2}$-distribution with $N-1$ degrees of freedom for a ( $p-1$ )-dimensional distribution. This $T^{2}$-statistic is invariant under any linear transformation in the $p-1$ dimensions orthogonal to $\boldsymbol{\varepsilon}$. Hence the statistic is independent of the choice of $\boldsymbol{C}$.

An example of this sort has been given by Rao (1948b). Let $N$ be the amount of cork in a boring from the north into a cork tree; let $E, S$, and $W$ be defined similarly. The set of amounts in four borings on one tree is



considered as an observation from a 4 -variate normal distribution. The question is whether the cork trees have the same amount of cork on each side. We make a transformation

$$
\begin{aligned}
& y_{1}=N-E-W+S, \\
& y_{2}=S-W, \\
& y_{3}=N-S .
\end{aligned}
$$

The number of observations is 28 . The vector of means is

$$
\bar{y}=\left(\begin{array}{l}
8.86 \\
4.50 \\
0.86
\end{array}\right) ;
$$

the covariance matrix for $y$ is

$$
S=\left(\begin{array}{rrr}
128.72 & 61.41 & -21.02 \\
61.41 & 56.93 & -28.30 \\
-21.02 & -28.30 & 63.53
\end{array}\right) .
$$

The value of $T^{2} /(N-1)$ is 0.768 . The statistic $0.768 \times 25 / 3=6.402$ is to be compared with the $F$-significance point with 3 and 25 degrees of freedom. It is significant at the $1 \%$ level.

### 5.3.7. Improved Estimation of the Mean

In Section 3.5 we considered estimation of the mean when the covariance matrix was known and showed that the Stein-type estimation based on this knowledge yielded lower quadratic risks than did the sample mean. In particular, if the loss is $(m-\mu)^{\prime} \boldsymbol{\Sigma}^{-1}(m-\mu)$, then

$$
\left(1-\frac{p-2}{N(\bar{x}-v)^{\prime} \Sigma^{-1}(\bar{x}-v)}\right)^{+}(\bar{x}-v)+v
$$

is a minimax estimator of $\mu$ for any $\nu$ and has a smaller risk than $\bar{x}$ when $p \geq 3$. When $\Sigma$ is unknown, we consider replacing it by an estimator, namely, a multiple of $A=n S$.

Theorem 5.3.1. When the loss is $(\boldsymbol{m}-\boldsymbol{\mu})^{\prime} \boldsymbol{\Sigma}^{-1}(\boldsymbol{m}-\boldsymbol{\mu})$, the estimator for $p \geq 3$ given by

$$
\left(1-\frac{a}{N(\bar{x}-v)^{\prime} A^{-1}(\bar{x}-v)}\right)(\bar{x}-v)+v
$$

has smaller risk than $\bar{x}$ and is minimax for $0<a<2(p-2) /(n-p+3)$, and the risk is minimized for $a=(p-2) /(n-p+3)$.

Proof. As in the case when $\Sigma$ is known (Section 3.5.2), we can make a transformation that carries $(1 / N) \boldsymbol{\Sigma}$ to $\boldsymbol{I}$. Then the problem is to estimate $\boldsymbol{\mu}$ based on $Y$ with the distribution $N(\mu, I)$ and $A=\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}$, where $\boldsymbol{Z}_{1}, \ldots, \boldsymbol{Z}_{n}$ are independently distributed, each according to $N(\mathbf{0}, I)$, and the loss function is $(\boldsymbol{m}-\boldsymbol{\mu})^{\prime}(\boldsymbol{m}-\boldsymbol{\mu})$. (We have dropped a factor of $N$.) The difference in risks is

$$
\begin{aligned}
\Delta R(\boldsymbol{\mu})= & \mathscr{E}_{\boldsymbol{\mu}}\left\{\|\boldsymbol{Y}-\boldsymbol{\mu}\|^{2}-\left\|\left(1-\frac{a}{(Y-v)^{\prime} A^{-1}(Y-v)}\right)(\boldsymbol{Y}-v)+v-\boldsymbol{\mu}\right\|^{2}\right\} \\
= & \mathscr{E}_{\boldsymbol{\mu}}\left\{2 \frac{a}{(\boldsymbol{Y}-v)^{\prime} A^{-1}(\boldsymbol{Y}-v)} \sum_{i=1}^{p}\left(Y_{i}-\mu_{l}\right)\left(Y_{l}-\nu_{i}\right)\right. \\
& \left.-\frac{a^{2}}{\left[(\boldsymbol{Y}-v)^{\prime} A^{-1}(\boldsymbol{Y}-v)\right]^{2}}\|\boldsymbol{Y}-v\|^{2}\right\} .
\end{aligned}
$$

The proof of Theorem 5.2.2 shows that $(Y-v)^{\prime} A^{-1}(Y-v)$ is distributed as $\|\boldsymbol{Y}-\boldsymbol{v}\|^{2} / \chi_{n-p+1}^{2}$, where the $\chi_{n-p+1}^{2}$ is independent of $\boldsymbol{Y}$. Then the difference in risks is

$$
\begin{aligned}
\Delta R(\boldsymbol{\mu})= & \mathscr{E}_{\boldsymbol{\mu}}\left\{\frac{2 a \chi_{n-p+1}^{2}}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{2}} \sum_{i=1}^{p}\left(Y_{i}-\mu_{l}\right)\left(Y_{l}-\nu_{l}\right)-\frac{a^{2}\left(\chi_{n-p+1}^{2}\right)^{2}}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{2}}\right\} \\
= & \mathscr{E}_{\boldsymbol{\mu}}\left\{\frac{2 a(p-2) \chi_{n-p+1}^{2}}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{2}}-\frac{a^{2}\left(\chi_{n-p+1}^{2}\right)^{2}}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{2}}\right\} \\
= & \{2(p-2)(n-p+1) a \\
& \left.\quad-\left[2(n-p+1)+(n-p+1)^{2}\right] a^{2}\right\} \mathscr{E}_{\boldsymbol{\mu}} \frac{1}{\|\boldsymbol{Y}-\boldsymbol{v}\|^{2}} .
\end{aligned}
$$

The factor in braces is $n-p+1$ times $2(p-2) a-(n-p+3) a^{2}$, which is positive for $0<a<2(p-2) /(n-p+3)$ and is maximized for $a= (p-2) /(n-p+3)$.

The improvement over the risk of $\boldsymbol{Y}$ is $(n-p+1)(p-2)^{2} /(n-p+3)$. $\mathscr{E}_{\mu}\|Y-v\|^{-2}$, as compared to the improvement $(p-2)^{2} \mathscr{E}_{\mu}\|Y-v\|^{-2}$ of $m(y)$ of Section 3.5 when $\Sigma$ is known.

Corollary 5.3.1. The extimator for $p \geq 3$

$$
\left(1-\frac{a}{N(\bar{x}-v)^{\prime} A^{-1}(\bar{x}-v)}\right)^{+}(\bar{x}-v)+v
$$

has smaller risk than (36) and is minimat for $0<a<2(p-2) /(n-p+3)$.
Proof. This corollary follows from Theorem 5.3.1 and Lemma 3.5.2. $\square$

The risk of (39) is not necessarily minimized at $a=(p-2) /(n-p+3)$. but that value seems like a good choicc. This is the cstimator (18) of Section 3.5 with $\Sigma$ replaced by $[1 /(n-p+3)] A$.

When the loss function is $(m-\mu)^{\prime} Q(m-\mu)$, where $Q$ is an arbitrary positive definite matrix, it is harder to present a uniformly improved estimator that is attractive. The estimators of Section 3.5 can be used with $\mathbf{\Sigma}$ replaced by an estimate.

### 5.4. THE DISTRIBUTION OF $T^{2}$ UNDER ALTERNATIVE HYPOTHESES; THE POWER FUNCTION

In Section 5.2.2 we showed that $\left(T^{2} / n\right)(N-p) / p$ has a noncentral $F$-distribution. In this section we shall discuss the noncentral $F$-distribution. its tabulation, and applications to procedures based on $T^{2}$.

The noncentral $F$-distribution is defined is the distribution of the ratio of a noncentral $x^{2}$ and an independent $x^{2}$ divided by the ratio of correspond ing degrees of freedom. Let $V$ have the noncentral $x^{2}$-distribution with $p$ degrees of freedom and noncentrality parameter $\tau^{2}$ (as given in Theorem 3.3.5), and let $W$ be independently distributed as $x^{2}$ with $m$ degrees of freedom. We shall find the density of $F=(V / p) /(W / m)$, which is the noncentral $F$ with noncentrality parameter $\tau^{2}$. The joint density of $V$ and $W$ is (28) of Section 3.3 multiplied by the density of $W$, which is $2^{-\frac{1}{2} m} \Gamma^{-1}\left(\frac{1}{2} m\right) w^{\frac{1}{2} m-1} e^{-\frac{1}{2} w}$. The joint density of $F$ and $W(d v=p w d f / m)$ is
(1) $\frac{e^{-\frac{1}{2} \tau^{2}}}{2^{\frac{1}{2}(p+m)} \Gamma\left(\frac{1}{2} m\right)} e^{-\frac{1}{2} w(1+p / / m)}$

$$
\frac{p}{m} \sum_{\beta=0}^{\infty}\left(\frac{\tau^{2}}{4}\right)^{\beta} \frac{1}{\beta!\Gamma\left(\frac{1}{2} p+\beta\right)}\left(\frac{p f}{m}\right)^{\frac{1}{p}+\beta \cdots 1} w^{\left.\frac{1}{( } p+m\right)+\beta-1} .
$$

The marginal density, obtained by integrating (1) with respect to $w$ from 0 to $\infty$, is

$$
\frac{p e^{-\frac{1}{1} \tau^{2}}}{m \Gamma\left(\frac{1}{2} m\right)} \sum_{\beta=0}^{\infty} \frac{\left(\tau^{2} / 2\right)^{\beta}\left(p f^{\prime} / m\right)^{\frac{1}{n-\beta-1}} \Gamma\left[\frac{1}{2}(p+m)+\beta\right]}{\beta!\Gamma\left(\frac{1}{2} p+\beta\right)(1+p f / m)^{\frac{1}{1}(p-m 1-\beta}} .
$$

Theorem 5.4.1. If $V$ has a noncentral $\chi^{2}$-distribution with $p$ degrees of freedom and noncentrality parameter $\tau^{2}$, and $W$ has an independent $\chi^{2}$-distribution with $m$ degrees of freedom, then $F=(V / p) /(W / m)$ has the density (2).

The density (2) is the density of the noncentral $F$-distribution.
If $T^{2}=N\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)^{\prime} S^{-1}\left(\overline{\boldsymbol{x}}-\boldsymbol{\mu}_{0}\right)$ is based on a sample of $N$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, then $\left(T^{2} / n\right)(N-p) / p$ has the noncentral $F$-distribution with $p$ and $N-p$ degrees of freedom and noncentrality parameter $N\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}-\boldsymbol{\mu}_{0}\right)= \tau^{2}$. From (2) we find that the density of $T^{2}$ is

$$
\begin{aligned}
& \frac{e^{-\frac{1}{2} \tau^{2}}}{(N-1) \Gamma\left[\frac{1}{2}(N-p)\right]} \sum_{\beta=0}^{\infty} \frac{\left(\tau^{2} / 2\right)^{\beta}\left[t^{2} /(N-1)\right]^{\frac{1}{2} p+\beta-1} \Gamma\left(\frac{1}{2} N+\beta\right)}{\beta!\Gamma\left(\frac{1}{2} p+\beta\right)\left[1+t^{2} /(N-1)\right]^{\frac{1}{2} N+\beta}} \\
& =\frac{\Gamma\left(\frac{1}{2} N\right)}{(N-1) \Gamma\left[\frac{1}{2}(N-p)\right] \Gamma\left(\frac{1}{2} p\right)}\left(\frac{t^{2}}{N-1}\right)^{\frac{1}{2} p-1}\left(1+\frac{t^{2}}{N-1}\right)^{-\frac{1}{1} N} \\
& \quad \cdot e^{-\frac{1}{2} \tau^{2}}{ }_{1} F_{1}\left(\frac{1}{2} N ; \frac{1}{2} p ; \frac{\tau^{2} t^{2}}{2(N-1)}\right),
\end{aligned}
$$

where

$$
{ }_{1} F_{1}(a ; b ; x)=\sum_{\beta=0}^{\infty} \frac{\Gamma(a+\beta) \Gamma(b)}{\Gamma(a) \Gamma(b+\beta)} \frac{x^{\beta}}{\beta!} .
$$

The density (3) is the density of the noncentral $T^{2}$-distribution.
Tables have been given by Tang (1938) of the probability of accepting the null hypothesis (that is, the probability of Type II error) for various values of $\tau^{2}$ and for significance levels 0.05 and 0.01 . His number of degrees of freedouil $f_{1}$ is our $p$ [1(1)8], his $f_{2}$ is our $n-p+1[2,4(1) 30,60, \infty]$, and his noncentrality parameter $\phi$ is related to our $\tau^{2}$ by

$$
\phi=\frac{\tau}{\sqrt{p+1}}
$$

[I( $\left.\left.\frac{1}{2}\right) 3(1) 8\right]$. His accompanying tables of significance points are for $T^{2} /\left(T^{2}+\right. N-1$ ).

As an example, suppose $p=4, n-p+1=20$, and consider testing the null hypothesis $\boldsymbol{\mu}=\mathbf{0}$ at the $1 \%$ level of significance. We would like to know the probability, say, that we accept the null hypothesis when $\phi=2.5$ ( $\tau^{2}=$ : 31.25). It is 0.227 . If we think the disadvantage of accepting the null hypothesis when $N, \mu$, and $\Sigma$ are such that $\tau^{2}=31.25$ is less than the disadvantage of rejecting the null hypothesis when it is true, then we may find it
reasonable to conduct the test as assumed. However, if the disadvantage of one type of error is about equal to that of the other, it would seem reasonable to bring down the probability of a Type II error. Thus, if we use a significance level of $5 \%$, the probability of Type II error (for $\phi=2.5$ ) is only 0.043.

Lehmer (1944) has computed tables of $\phi$ for given significance level and given probability of Type II error. Here tables can be used to see what value of $\tau^{2}$ is needed to make the probability of acceptance of the null hypothesis sufficiently low when $\boldsymbol{\mu} \neq \mathbf{0}$. For instance, if we want to be able to reject the hypothesis $\boldsymbol{\mu}=\mathbf{0}$ on the basis of a sample for a given $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$, we may be able to choose $N$ so that $N \boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}=\tau^{2}$ is sufficiently large. Of course, the difficulty with these considerations is that we usually do not know exactly the values of $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ (and hence of $\tau^{2}$ ) for which we want the probability of rejection at a certain value.

The distribution of $T^{2}$ when the null hypothesis is not true was derived by different methods by Hsu (1938) and Bose and Roy (1938).

### 5.5. THE TWO-SAMPLE PROBLEM WITH UNEQUAL COVARIANCE MATRICES

If the covariance matrices are not the same, the $T^{2}$-test for equality of mean vectors has a probability of rejection under the null hypothesis that depends on these matrices. If the difference between the matrices is small or if the sample sizes are large, there is no practical effect. However, if the covariance matrices are quite different and/or the sample sizes are relatively small, the nominal significance level may be distorted. Hence we develop a procedure with assigned significance level. Let $\left\{x_{\alpha}^{(i)}\right\}, \alpha=1, \ldots, N_{i}$, be samples from $N\left(\boldsymbol{\mu}^{(1)}, \mathbf{\Sigma}_{i}\right), i=1,2$. We wish to test the hypothesis $H: \boldsymbol{\mu}^{(1)}=\boldsymbol{\mu}^{(2)}$. The mean $\vec{x}^{(1)}$ of the first sample is normally distributed with expected value

$$
\mathscr{E} \bar{x}^{(1)}=\mu^{(1)}
$$

and covariance matrix

$$
\mathscr{E}\left(\bar{x}^{(1)}-\mu^{(1)}\right)\left(\bar{x}^{(1)}-\mu^{(1)}\right)^{\prime}=\frac{1}{N_{1}} \Sigma_{1} .
$$

Similarly, the mean $\bar{x}^{(2)}$ of the second sample is normally distributed with expected value

$$
\mathscr{E} \bar{x}^{(2)}=\mu^{(2)}
$$

and covariance matrix

$$
\mathscr{E}\left(\bar{x}^{(2)}-\mu^{(2)}\right)\left(\bar{x}^{(2)}-\mu^{(2)}\right)^{\prime}=\frac{1}{N_{2}} \Sigma_{2} .
$$

Thus $\overline{\boldsymbol{x}}^{(1)}-\overline{\boldsymbol{x}}^{(2)}$ has mean $\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}$ and covariance matrix $\left(1 / N_{1}\right) \boldsymbol{\Sigma}_{1}+ \left(1 / N_{2}\right) \Sigma_{2}$. We cannot use the technique of Section 5.2, however, because

$$
\sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(1)}-\tilde{x}^{(1)}\right)\left(x_{\alpha}^{(1)}-\tilde{x}^{(1)}\right)^{\prime}+\sum_{\alpha=1}^{N_{2}}\left(x_{\alpha}^{(2)}-\tilde{x}^{(2)}\right)\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)^{\prime}
$$

does not have the Wishart distribution with covariance matrix a multiple of $\left(1 / N_{1}\right) \Sigma_{1}+\left(1 / N_{2}\right) \Sigma_{2}$.

If $N_{1}=N_{2}=N$, say, we can use the $T^{2}$-test in an obvious way. Let $\boldsymbol{y}_{\alpha}=\boldsymbol{x}_{\alpha}^{(1)}-\boldsymbol{x}_{\alpha}^{(2)}$ (assuming the numbering of the observations in the two samples is independent of the observations themselves). Then $y_{\alpha}$ is normally distributed with mean $\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}$ and covariance matrix $\boldsymbol{\Sigma}_{1}+\boldsymbol{\Sigma}_{2}$, and $y_{1}, \ldots, y_{N}$ are independent. Let $\bar{y}=(1 / N) \sum_{\alpha=1}^{N} y_{\alpha}=\bar{x}^{(1)}-\bar{x}^{(2)}$, and define $S$ by
(6) $(N-1) S=\sum_{\alpha=1}^{N}\left(y_{\alpha}-\bar{y}\right)\left(y_{\alpha}-\bar{y}\right)^{\prime}$

$$
=\sum_{\alpha=1}^{N}\left(x_{\alpha}^{(1)}-x_{\alpha}^{(2)}-\bar{x}^{(1)}+\bar{x}^{(2)}\right)\left(x_{\alpha}^{(1)}-x_{\alpha}^{(2)}-\bar{x}^{(1)}+\bar{x}^{(2)}\right)^{\prime} .
$$

Then

$$
T^{2}=N \bar{y}^{\prime} S^{-1} \bar{y}
$$

is suitable for testing the hypothesis $\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}=\mathbf{0}$, and has the $T^{2}$-distribution with $N-1$ degrees of freedom. It should be observed that if we had known $\Sigma_{1}=\Sigma_{2}$, we would have used a $T^{2}$-statistic with $2 N-2$ degrees of freedom; thus we have lost $N-1$ degrees of freedom in constructing a test which is independent of the two covariance matrices. If $N_{1}=N_{2}=50$ as in the example in Section 5.3.4, then $T_{4.49}^{2}(.01)=15.93$ as compared to $T_{4.98}^{2}(.01) =14.52$.

Now let us turn our attention to the case of $N_{1} \neq N_{2}$. For convenience, let $N_{1}<N_{2}$. Then we define
(8) $y_{\alpha}=x_{\alpha}^{(1)}-\sqrt{\frac{N_{1}}{N_{2}}} x_{\alpha}^{(2)}+\frac{1}{\sqrt{N_{1} N_{2}}} \sum_{\beta=1}^{N_{1}} x_{\beta}^{(2)}-\frac{1}{N_{2}} \sum_{\gamma=1}^{N_{2}} x_{\gamma}^{(2)}, \quad \alpha=1, \ldots, N_{1}$

The expected value of $y_{\alpha}$ is

$$
\mathscr{E} y_{\alpha}=\boldsymbol{\mu}^{(1)}-\sqrt{\frac{N_{1}}{N_{2}}} \boldsymbol{\mu}^{(2)}+\frac{N_{1}}{\sqrt{N_{1} N_{2}}} \boldsymbol{\mu}^{(2)}-\frac{N_{2}}{N_{2}} \boldsymbol{\mu}^{(2)}=\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)} .
$$

The covariance matrix of $y_{\alpha}$ and $y_{\beta}$ is

$$
\mathscr{E}\left(y_{\alpha}-\mathscr{E} y_{a}\right)\left(y_{\beta}-\mathscr{E} y_{\beta}\right)^{\prime}=\delta_{\alpha \beta}\left(\Sigma_{1}+\frac{N_{1}}{N_{2}} \Sigma_{2}\right) .
$$

Thus a suitable statistic for testing $\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}=\mathbf{0}$, which has the $T^{2}$-distribution with $N_{1}-1$ degrees of freedom, is

$$
T^{2}=N_{1} \bar{y}^{\prime} S^{-1} \bar{y},
$$

where

$$
\bar{y}=\frac{1}{N_{1}} \sum_{\alpha=1}^{N_{1}} y_{\alpha}=\bar{x}^{(1)}-\bar{x}^{(2)}
$$

and

$$
\left(N_{1}-1\right) S=\sum_{\alpha=1}^{N_{1}}\left(y_{\alpha}-\bar{y}\right)\left(y_{\alpha}-\bar{y}\right)^{\prime}=\sum_{\alpha=1}^{N_{1}}\left(u_{\alpha}-\bar{u}\right)\left(u_{\alpha}-\bar{u}\right)^{\prime},
$$

where $\vec{u}=\left(1 / N_{1}\right) \sum_{\alpha=1}^{N_{1}} u_{\alpha}$ and $u_{\alpha}=\boldsymbol{x}_{\alpha}^{(1)}-\sqrt{N_{1} / N_{2}} \boldsymbol{x}_{\alpha}^{(2)}, \alpha=1, \ldots, N_{1}$.
This procedure was suggested by Scheffé (1943) in the univariate case. Scheffé showed that in the univariate case this technique gives the shortest confidence intervals obtained by using the $t$-distribution. The advantage of the method is that $\bar{x}^{(1)}-\bar{x}^{(2)}$ is used, and this statistic is most relevant to $\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}$. The sacrifice of observations in estimating a covariance matrix is not so important. Bennett (1951) gave the extension of the procedure to the multivariate case.

This approach can be used for more general cases. Let $\left\{x_{\alpha}^{(t)}\right\}, \alpha=1, \ldots, N_{l}$, $i=1, \ldots, q$, be samples from $N\left(\mu^{(i)}, \Sigma_{i}\right), i=1, \ldots, q$, respectively. Consider testing the hypothesis

$$
H: \sum_{l=1}^{q} \beta_{l} \boldsymbol{\mu}^{(l)}=\boldsymbol{\mu},
$$

where $\beta_{1}, \ldots, \beta_{q}$ are given scalars and $\boldsymbol{\mu}$ is a given vector. If the $N_{1}$ are unequal, take $N_{1}$ to be the smallest. Let

$$
y_{\alpha}=\beta_{1} x_{\alpha}^{(1)}+\sum_{i=2}^{q} \beta_{i} \sqrt{\frac{N_{1}}{N_{l}}}\left(x_{\alpha}^{(l)}-\frac{1}{N_{1}} \sum_{\beta=1}^{N_{1}} x_{\beta}^{(l)}+\frac{1}{\sqrt{N_{1} N_{l}}} \sum_{\gamma=1}^{N_{1}} x_{\gamma}^{(l)}\right) .
$$

Then $\mathscr{E} y_{0}=\sum_{i=1}^{q} \beta_{i} \mu^{(i)}$, and

$$
\mathscr{E}\left(y_{\alpha}-\mathscr{E} y_{a}\right)\left(y_{\beta}-\mathscr{E} y_{\beta}\right)^{\prime}=\delta_{a \beta}\left(\sum_{i=1}^{\eta} \frac{\beta_{i}^{2} N_{1}}{N_{i}} \Sigma_{i}\right) .
$$

Let $\bar{y}$ and $S$ be defined by

$$
\tilde{y}=\frac{1}{N_{1}} \sum_{\alpha=1}^{N_{1}} y_{\alpha}=\sum_{i=1}^{q} \beta_{i} \bar{x}^{(i)}, \quad \bar{x}^{(j)}=\frac{1}{N_{1}} \sum_{\beta=1}^{N_{t}} x_{\beta}^{(i)},
$$

$$
\left(N_{\mathrm{l}}-\mathrm{l}\right) S=\sum_{\alpha=1}^{N_{1}}\left(\boldsymbol{y}_{a}-\overline{\boldsymbol{y}}\right)\left(\boldsymbol{y}_{\mathrm{ax}}-\overline{\boldsymbol{y}}\right)^{\prime}
$$

Then

$$
T^{2}=N_{1}(\bar{y}-\mu)^{\prime} S^{-1}(\bar{y}-\mu)
$$

is suitable for testing $H$, and when the hypothesis is true, this statistic has the $T^{2}$-distribution for dimension $p$ with $N_{1}-1$ degrees of freedom. If we let $u_{\alpha}=\sum_{1-1}^{q} \beta_{1} \sqrt{N_{1} / N_{l}} x_{\alpha}^{(1)}, \alpha=1, \ldots, N_{1}$, then $S$ can be defined as

$$
\left(N_{1}-1\right) S=\sum_{\alpha=1}^{N_{1}}\left(u_{\alpha}-\bar{u}\right)\left(u_{\alpha}-\bar{u}\right)^{\prime} .
$$

Another problem that is amenable to this kind of treatment is testing the hypothesis that two subvectors have equal means. Let $\boldsymbol{x}=\left(\boldsymbol{x}^{(1) \prime}, \boldsymbol{x}^{(2) \prime}\right)^{\prime}$ be distributed normally with mean $\boldsymbol{\mu}=\left(\boldsymbol{\mu}^{(1) \prime}, \boldsymbol{\mu}^{(2) \prime}\right)^{\prime}$ and covariance matrix

$$
\Sigma=\left(\begin{array}{ll}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{array}\right) .
$$

We assume that $\boldsymbol{x}^{(1)}$ and $\boldsymbol{x}^{(2)}$ are each of $q$ components. Then $y=\boldsymbol{x}^{(1)}-\boldsymbol{x}^{(2)}$ is distributed normally with mean $\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}$ and covariance matrix $\boldsymbol{\Sigma}_{\boldsymbol{y}}=\boldsymbol{\Sigma}_{11} -\Sigma_{21}-\Sigma_{12}+\Sigma_{22}$. To test the hypothesis $\mu^{(1)}=\mu^{(2)}$ we use a $T^{2}$-statistic $N \bar{y}^{\prime} S_{1}^{-1} \bar{y}$, where the mean vector and covariance matrix of the sample are partitioned similarly to $\mu$ and $\Sigma$.

### 5.6. SOME OPTIMAL PROPERTIES OF THE $T^{2}$-TEST

### 5.6.1. Optimal Invariant Tests

In this section we shall indicate that the $T^{2}$-test is the best in certain classes of tests and sketch briefly the proofs of these results.

The hypothesis $\boldsymbol{\mu}=\mathbf{0}$ is to be tested on the basis of the $N$ observations $x_{1}, \ldots, x_{N}$ from $N(\mu, \Sigma)$. First we consider the class of tests based on the
statistics $A=\sum\left(x_{\alpha}-\bar{x}\right)\left(x_{a}-\bar{x}\right)^{\prime}$ and $\bar{x}$ which are invariant with respect to the transformations $A^{*}=C A C^{\prime}$ and $\bar{x}^{*}=C \bar{x}$, where $C$ is nonsingular. The transformation $\boldsymbol{x}_{\alpha}^{*}=\boldsymbol{C} \boldsymbol{x}_{\alpha}$ leaves the problem invariant; that is, in terms of $\boldsymbol{x}_{\alpha}^{*}$ we test the hypothesis $\mathscr{E} x_{\alpha}^{*}=0$ given that $x_{1}^{*}, \ldots, x_{N}^{*}$ are $N$ observations from a multivariate normal population. It seems reasonable that we require a solution that is also invariant with respect to these transformations; that is, we look for a critical region that is not changed by a nonsingular linear transformation. (The defination of the region is the same in different coordinate systems.)

Theorem 5.6.1. Given the observations $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, of all tests of $\mu=\mathbf{0}$ based on $\overline{\boldsymbol{x}}$ and $A=\sum\left(\boldsymbol{x}_{\alpha}-\overline{\boldsymbol{x}}\right)\left(\boldsymbol{x}_{\alpha}-\overline{\boldsymbol{x}}\right)^{\prime}$ that are invariant with respect to transformations $\bar{x}^{*}=\overline{C x}, A^{*}=C A C^{\prime}$ ( $C$ nonsingular), the $T^{2}$-test is uniformly most powerful.

Proof. First, as we have seen in Section 5.2.1, any test based on $T^{2}$ is invariant. Second, this function is essentially the only invariant, for if $f(\bar{x}, A)$ is invariant, then $f(\overline{\boldsymbol{x}}, A)=f\left(\overline{\boldsymbol{x}}^{*}, \boldsymbol{I}\right)$, where only the first coordinate of $\overline{\boldsymbol{x}}^{*}$ is different from zero and it is $\sqrt{\bar{x}^{\prime} A^{-1} \bar{x}}$. (There is a matrix $C$ such that $\boldsymbol{C} \overline{\boldsymbol{x}}=\overline{\boldsymbol{x}}^{*}$ and $\boldsymbol{C A} C^{\prime}=\boldsymbol{I}$.) Thus $f(\overline{\boldsymbol{x}}, A)$ depends only on $\overline{\boldsymbol{x}}^{\prime} A^{-1} \tilde{\boldsymbol{x}}$. Thus an invariant test must be based on $\bar{x}^{\prime} A^{-1} \tilde{x}$. Third, we can apply the NeymanPearson fundamental lemma to the distribution of $T^{2}$ [(3) of Section 5.4] to find the uniformly most powerful test based on $T^{2}$ against a simple alternative $\tau^{2}=N \boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$. The most powerful test of $\tau^{2}=0$ is based on the ratio of (3) of Section 5.4 to (3) with $\tau^{2}=0$. The critical region is

$$
\begin{array}{r}
c<e^{-\frac{1}{2} \tau^{2}} \sum_{\alpha=0}^{\infty} \frac{\left(\tau^{2} / 2\right)^{\alpha}\left(t^{2} / n\right)^{\frac{1}{2} p+\alpha-1}\left(1+t^{2} / n\right)^{-\frac{1}{2}(n+1)-\tau} \Gamma\left[\frac{1}{2}(n+1)+\alpha\right]}{\alpha!\Gamma\left(\frac{1}{2} p+\alpha\right)} \\
/ \frac{\left(t^{2} / n\right)^{\frac{1}{2} p-1}\left(1+t^{2} / n\right)^{-\frac{1}{2}(n+1)} \Gamma\left[\frac{1}{2}(n+1)\right]}{\Gamma\left(\frac{1}{2} p\right)} \\
=\frac{\Gamma\left(\frac{1}{2} p\right)}{\Gamma\left[\frac{1}{2}(n+1)\right]} e^{-\frac{1}{2} \tau^{2}} \sum_{\alpha=0}^{\infty} \frac{\left(\tau^{2} / 2\right)^{\alpha} \Gamma\left[\frac{1}{2}(n+1)+\alpha\right]}{\alpha!\Gamma\left(\frac{1}{2} p+\alpha\right)}\left(\frac{t^{2} / n}{1+t^{2} / n}\right)^{\alpha} .
\end{array}
$$

The right-hand side of (1) is a strictly increasing function of $\left(t^{2} / n\right) /\left(1+t^{2} / n\right)$, hence of $t^{2}$. Thus the inequality is equivalent to $t^{2}>k$ for $k$ suitably chosen. Since this does not depend on the alternative $\tau^{2}$, the test is uniformly most powerful invariant. $\square$

Definition 5.6.1. A critical function $\psi(\bar{r}, A)$ is a function with values between 0 and 1 (inclusive) such that $\mathscr{E} \psi(\bar{x}, A)=\varepsilon$, the significance level, when $\boldsymbol{\mu}=\mathbf{0}$.

A randomized test consists of rejecting the hypothesis with probability $\psi(\boldsymbol{x}, \boldsymbol{B})$ when $\overline{\boldsymbol{x}}=\boldsymbol{x}$ and $\boldsymbol{A}=\boldsymbol{B}$. A nonrandomized test is defined when $\psi(\bar{x}, A)$ takes on only the values 0 and 1 . Using the form of the Neyman-Pearson lemma appropriate for critical functions, we obtain the following corollary:

Corollary 5.6.1. On the basis of observations $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, of all randomized tests based on $\overline{\boldsymbol{x}}$ and $\boldsymbol{A}$ that are invariant with respect to transformations $\bar{x}^{*}=C \bar{x}, A^{*}=C A C^{\prime}(C$ nonsingular $)$, the $T^{2}$-test is uniformly most powerful.

Theorem 5.6.2. On the basis of observations $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, of all tests of $\boldsymbol{\mu}=\mathbf{0}$ that are invariant with respect to transformations $\boldsymbol{x}_{\boldsymbol{\alpha}}^{*}=C x_{\boldsymbol{\alpha}}$ (C nonsingular), the $T^{2}$-test is a uniformly most powerful test; that is, the $T^{2}$-test is at least as powerful as any other invariant test.

Proof. Let $\psi\left(x_{1}, \ldots, x_{N}\right)$ be the critical function of an invariant test. Then

$$
\mathscr{E}\left[\psi\left(x_{1}, \ldots, x_{N}\right)\right]=\mathscr{E}_{\bar{x}, A}\left\{\mathscr{E}\left[\psi\left(x_{1}, \ldots, x_{N}\right) \mid \bar{x}, A\right]\right\} .
$$

Since $\overline{\boldsymbol{x}}, \boldsymbol{A}$ are sufficient statistics for $\boldsymbol{\mu}, \boldsymbol{\Sigma}$, the expectation $\mathscr{E}\left[\psi\left(\boldsymbol{x}_{1}, \ldots\right.\right.$, $\left.\left.\boldsymbol{x}_{N}\right) \mid \overline{\boldsymbol{x}}, \boldsymbol{A}\right]$ depends only on $\overline{\boldsymbol{x}}, \boldsymbol{A}$, It is invariant and has the same power as $\psi\left(x_{I}, \ldots, x_{N}\right)$. Thus each test in this larger class can be replaced by one in the smaller class (depending only on $\overline{\boldsymbol{x}}$ and $\boldsymbol{A}$ ) that has identical power. Corollary 5.6,1 completes the proof.

Theorem 5.6.3. Given observations $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, of all tests of $\boldsymbol{\mu}=\mathbf{0}$ based on $\overline{\boldsymbol{x}}$ and $\boldsymbol{A}=\sum\left(\boldsymbol{x}_{\alpha}-\overline{\boldsymbol{x}}\right)\left(\boldsymbol{x}_{\alpha}-\overline{\boldsymbol{x}}\right)^{\prime}$ with power depending only on $N \mu^{\prime} \Sigma^{-1} \mu$, the $T^{2}$-test is uniformly most powerful.

Proof. We wish to reduce this theorem to Theorem 5.6.1 by identifying the class of tests with power depending on $N \boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$ with the class of invariant tests. We need the following definition:

Definition 5.6.2. A test $\psi\left(x_{1}, \ldots, x_{N}\right)$ is said to be almost invariant if

$$
\psi\left(x_{1}, \ldots, x_{N}\right)=\psi\left(C x_{1}, \ldots, C x_{N}\right)
$$

for all $\boldsymbol{x}_{I}, \ldots, \boldsymbol{x}_{N}$ except for a set of $\boldsymbol{x}_{I}, \ldots, \boldsymbol{x}_{N}$ of Lebesgue measure zero; this exception set may depend on $C$.



It is clear that Theorems 5.6.1 and 5.6.2 hold if we extend the definition of invariant test to mean that (3) holds except for a fixed set of $r_{1}, \ldots, x_{1}$ of measure 0 (the set not depending on $\boldsymbol{C}$ ). It has been shown by Hunt and Stein [Lehmann (1959)] that in our problem almost invariance implics invariance (in the broad sense).

Now we wish to argue that if $\psi(\bar{x}, A)$ has power depending only on $N \boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$, it is almost invariant. Since the power of $\psi(\overline{\boldsymbol{x}}, A)$ depends only on $N^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$, the power is

$$
\begin{aligned}
\mathscr{E}_{\mu, \Sigma} \psi(\bar{x}, A) & \equiv \mathscr{E}_{C^{-1} \mu, C^{-1} \Sigma\left(C^{-1}, \psi(\bar{x}, A)\right.} \\
& \equiv \mathscr{E}_{\mu, \Sigma} \psi\left(C \bar{x}, C A C^{\prime}\right)
\end{aligned}
$$

The second and third terms of (4) are merely different ways of writing the same integral. Thus

$$
\mathscr{E}_{\mu, \Sigma}\left[\psi(\bar{x}, A)-\psi\left(C \bar{x}, C A C^{\prime}\right)\right] \equiv 0,
$$

identically in $\boldsymbol{\mu}, \boldsymbol{\Sigma}$. Since $\overline{\boldsymbol{x}}, A$ are a complete sufficient set of statistics for $\boldsymbol{\mu}, \boldsymbol{\Sigma}$ (Theorem 3.4.2), $f(\overline{\boldsymbol{x}}, A)=\psi(\overline{\boldsymbol{x}}, A)-\psi\left(\overline{\boldsymbol{x}}, C A C^{\prime}\right)=0$ almost everywhere. Theorem 5.6.3 follows. $\square$

As Theorem 5.6.2 follows from Theorem 5.6.1, so does the following theorem from Theorem 5.6.5:

Theorem 5.6.4. On the basis of observations $x_{\mathrm{I}}, \ldots, x_{N}$ from $N(\mu . \Sigma)$. of all tests of $\boldsymbol{\mu}=\mathbf{0}$ with power depending only on $N \boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$, the $T^{2}$-est is a uniformly most powerful test.

Theorem 5.6 .4 was first proved by Simaika (1941). The results and proofs given in this section follow Lehmann (1959). Hsu (1945) has proved an optimal property of the $T^{2}$-test that involves averaging the power over $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$.

### 5.6.2. Admissible Tests

We now turn to the question of whether the $T^{2}$-test is a good test compared to all possible tests; the comparison in the previous section was to the restricted class of invariant tests. The main result is that the $T^{-}$-test is admissible in the class of all tests; that is, there is no other procedure that is better.

Definition 5.6.3. A test $T^{*}$ of the null hypothesis $H_{0}: \omega \in \Omega_{0}$ against the alternative $\omega \in \Omega_{1}$ (disjoint from $\Omega_{0}$ ) is admissible if there exists no other test $T$
such that

$$
\begin{array}{ll}
\operatorname{Pr}\left\{\text { Reject } H_{0} \mid T, \omega\right\} \leq \operatorname{Pr}\left\{\text { Reject } H_{0} \mid T^{*}, \omega\right\}, & \omega \in \Omega_{0}, \\
\operatorname{Pr}\left\{\text { Reject } H_{0} \mid T, \omega\right\} \geq \operatorname{Pr}\left\{\text { Reject } H_{0} \mid T^{*}, \omega\right\}, & \omega \in \Omega_{1},
\end{array}
$$

with strict inequality for at least one $\omega$.
The admissibility of the $T^{2}$-test follows from a theorem of Stein (1956a) that applies to any exponential family of distributions.

An exponential family of distributions ( $\mathbb{H}, \mathscr{B}, m, \Omega, P$ ) consists of a finite dimensional Euclidean space $\mathscr{A}$, a measure $m$ on the $\sigma$-algebra $\mathscr{B}$ of all ordinary Borel sets of $\mathscr{U}$, a subset $\Omega$ of the adjoint space $\mathscr{U}^{\prime}$ (the linear space of all real-valued linear functions on $\mathscr{Y}$ ) such that

$$
\psi(\omega)=\int_{\mathscr{Y}} e^{\omega^{\prime} y} d m(y)<\infty, \quad \omega \in \Omega
$$

and $P$, the function on $\Omega$ to the set of probability measures on $\mathscr{B}$ given by

$$
P_{c}(A)=\frac{1}{\psi(\omega)} \int_{-1} e^{\omega^{\prime} y} d m(y), \quad A \in \mathscr{B}
$$

The family of normal distributions $N(\mu, \mathbf{\Sigma})$ constitutes an exponential family, for the density can be written

$$
n(\boldsymbol{x} \mid \boldsymbol{\mu}, \boldsymbol{\Sigma})=\frac{e^{-\frac{1}{2} \mu \cdot \mathbf{\Sigma}^{-1} \mu}}{(2 \pi)^{\frac{1}{1} P}|\boldsymbol{\Sigma}|^{\frac{1}{2}}} e^{\left(\mu \cdot \mathbf{\Sigma}^{-1}\right) x+\operatorname{tr}\left(-\frac{1}{2} \mathbf{\Sigma}^{-1}\right) x x^{t}} .
$$

We map from $\mathscr{X}^{\prime}$ to $\mathscr{Y}$; the vector $y=\left(y^{(1) \prime}, y^{(2) \prime}\right)^{\prime}$ is composed of $y^{(1)}=x$ and $\boldsymbol{y}^{(2)}=\left(x_{1}^{2}, 2 x_{1} x_{2}, \ldots, 2 x_{1} x_{p}, x_{2}^{2}, \ldots, x_{p}^{2}\right)^{\prime}$. The vector $\boldsymbol{\omega}=\left(\boldsymbol{\omega}^{(1) \prime}, \boldsymbol{\omega}^{(2) \prime}\right)^{\prime}$ is composed of $\boldsymbol{\omega}^{(1)}=\boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$ and $\boldsymbol{\omega}^{(2)}=-\frac{1}{2}\left(\sigma^{11}, \sigma^{12}, \ldots, \sigma^{1 p}, \sigma^{22}, \ldots, \sigma^{\rho p}\right)^{l}$, where $\left(\sigma^{i /}\right)=\Sigma^{-1}$; the transformation of parameters is one to one. The measure $m(A)$ of a set $A \in \mathscr{B}$ is the ordinary Lebesgue measure of the set of $x$ that maps into the set $A$. (Note that the probability measure in $\mathscr{G}$ is not defined by a density.)

Theorem 5.6.5 (Stein). Let ( $\mathscr{Y}, \mathscr{B}, m, \Omega, P$ ) be an exponential family and $\Omega_{0}$ a nonempty proper subset of $\Omega$. (i) Let $A$ be a subset of $y$ that is closed and convex. (ii) Suppose that for every vector $\boldsymbol{\omega} \in \mathscr{Y}^{\prime}$ and real $c$ for which $\left\{y \mid \omega^{\prime} y>c\right\}$ and $A$ are disjoint, there exists $\omega_{1} \in \Omega$ such that for arbitrarily large $\lambda$ the vector $\omega_{1}+\lambda \omega \in \Omega-\Omega_{0}$. Then the test with acceptance region $A$ is admissible for testing the hypothesis that $\omega \in \Omega_{0}$ against the alternative $\omega \in \Omega-\Omega_{0}$.

![](https://cdn.mathpix.com/cropped/b0faea94-7f5a-432a-9816-abe3a57981a7-213.jpg?height=451&width=887&top_left_y=238&top_left_x=364)
Figure 5.2

The conditions of the theorem are illustrated in Figure 5.2, which is drawn simultaneously in the space $\mathscr{Y}$ and the set $\Omega$.

Proof. The critical function of the test with acceptance region $A$ is $\phi_{A}(y)=0 . y \in A$, and $\phi_{A}(y)=1, y \notin A$. Suppose $\phi(y)$ is the critical function of a better test, that is,

$$
\begin{array}{lr}
\int \phi(y) d P_{\omega}(y) \leq \int \phi_{A}(y) d P_{\omega}(y), & \omega \in \Omega_{0} \\
\int \phi(y) d P_{\omega}(y) \geq \int \phi_{A}(y) d P_{\omega}(y), & \omega \in \Omega-\Omega_{0}
\end{array}
$$

with strict inequality for some $\boldsymbol{\omega}$; we shall show that this assumption leads to a contradiction. Let $B=\{y \mid \phi(y)<1\}$. (If the competing test is nonrandomized, $B$ is its acceptance region.) Then

$$
\left\{y \mid \phi_{A}(y)-\phi(y)>0\right\}=\bar{A} \cap B,
$$

where $\bar{A}$ is the complement of $A$. The $m$-measure of the set (12) is positive; otherwise $\phi_{A}(y)=\phi(y)$ almost everywhere, and (10) and (11) would hold with equality for all $\omega$. Since $A$ is convex, there exists an $\omega$ and a $c$ such that the intersection of $\bar{A} \cap B$ and $\left\{y \mid \boldsymbol{\omega}^{\prime} \boldsymbol{y}>c\right\}$ has positive $m$-measure. (Since $A$ is closed, $\bar{A}$ is open and it can be covered with a denumerable collection of open spheres, for example, with rational radii and centers with rational coordinates. Because there is a hyperplane separating $A$ and each sphere, there exists a denumerable coilection of open half-spaces $H_{j}$ disjoint from $A$ that covers $\bar{A}$. Then at least one half-space has an intersection with $\bar{A} \cap B$ with positive $m$-measure.) By hypothesis there exists $\omega_{1} \in \Omega$ and an arbitrarily large $\lambda$ such that

$$
\omega_{\lambda}=\omega_{1}+\lambda \omega \in \Omega-\Omega_{0} .
$$

Then

$$
\begin{aligned}
& \int\left[\phi_{A}(y)-\phi(y)\right] d P_{\omega_{\lambda}}(y) \\
& =\frac{1}{\psi\left(\omega_{\lambda}\right)} \int\left[\phi_{A}(y)-\phi(y)\right] e^{\omega_{\lambda}^{\prime} y} d m(y) \\
& =\frac{\psi\left(\omega_{1}\right)}{\psi\left(\omega_{\lambda}\right)} \int\left[\phi_{A}(y)-\phi(y)\right] e^{\lambda \omega^{\prime} y} d P_{\omega_{1}}(y) \\
& =\frac{\psi\left(\omega_{1}\right)}{\psi\left(\omega_{\lambda}\right)} e^{\lambda c} \int\left[\phi_{A}(y)-\phi(y)\right] e^{\lambda\left(\omega^{\prime} y-c\right)} d P_{\omega_{1}}(y) \\
& =\frac{\psi\left(\omega_{1}\right)}{\psi\left(\omega_{\lambda}\right)} e^{\lambda c}\left\{\int_{\omega^{\prime} y>c}\left[\phi_{A}(y)-\phi(y)\right] e^{\lambda\left(\omega^{\prime} y-c\right)} d P_{\omega_{1}}(y)\right. \\
& \left.\quad+\int_{\omega^{\prime} y \leq c}\left[\phi_{A}(y)-\phi(y)\right] e^{\lambda\left(\omega^{\prime} y-c\right)} d P_{\omega_{1}}(y)\right\}
\end{aligned}
$$

For $\omega^{\prime} y>c$ we have $\phi_{A}(y)=1$ and $\phi_{A}(y)-\phi(y) \geq 0$, and $\left\{y \mid \phi_{A}(y)-\phi(y)\right. >0$ \} has positive measure; therefore, the first integral in the braces approaches $\infty$ as $\lambda \rightarrow \infty$. The second integral is bounded because the integrand is bounded by 1 , and hence the last expression is positive for sufficiently large $\lambda$. This contradicts (11).

This proof was given by Stein (1956a). It is a generalization of a theorem of Birnhaum (1955).

Corollary 5.6.2. If the conditions of Theorem 5.6.5 hold except that $A$ is not necessarily closed, but the boundary of $A$ has m-measure 0 , then the conclusion of Theorem 5.6.5 holds.

Proof. The closure of $A$ is convex (Problem 5.18), and the test with acceptance region equal to the closure of $A$ differs from $A$ by a set of probability 0 for all $\omega \in \Omega$. Furthermore,

$$
\begin{aligned}
\boldsymbol{A} \cap\left\{\boldsymbol{y} \mid \boldsymbol{\omega}^{\prime} \boldsymbol{y}>c\right\}=\varnothing & \Rightarrow A \subset\left\{\boldsymbol{y} \mid \boldsymbol{\omega}^{\prime} \boldsymbol{y} \leq c\right\} \\
& \Rightarrow \text { closure } \boldsymbol{A} \subset\left\{\boldsymbol{y} \mid \boldsymbol{\omega}^{\prime} \boldsymbol{y} \leq c\right\}
\end{aligned}
$$

Then Theorem 5.6.5 holds with $A$ replaced by the closure of 4 .
Theorem 5.6.6. Based on observations $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}$ from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, Hotelling's $T^{2}$-test is admissible for testing the hypothesis $\boldsymbol{\mu}=\mathbf{0}$.

Proof. To apply Theorem 5.6.5 we put the distribution of the observations into the form of an exponential family. By Theorems 3.3.1 and 3.3.2 we can transform $x_{1}, \ldots, x_{N}$ to $z_{\alpha}=\sum_{\beta=1}^{N} c_{\alpha \beta} x_{\beta}$, where ( $c_{\alpha \beta}$ ) is orthogonal and $z_{\wedge} =\sqrt{N} \tilde{x}$. Then the density of $z_{1}, \ldots, z_{N}$ (with respect to Lebesgue measure) is

$$
\frac{e^{-\frac{1}{2} N \mu^{\prime} \Sigma^{-1} \mu}}{(2 \pi)^{\frac{1}{2} p N}|\Sigma|^{\frac{1}{2} N}} \exp \left[\sqrt{N} \boldsymbol{\mu}^{\prime} \Sigma^{-1} z_{N}+\operatorname{tr}\left(-\frac{1}{2} \Sigma^{-1}\right) \sum_{\alpha=1}^{N} z_{a} z_{\alpha}^{\prime}\right] .
$$

The vector $y=\left(y^{(1)}, y^{(2) \prime}\right)^{\prime}$ is composed of $y^{(1)}=z_{N}(=\sqrt{N} \bar{x})$ and $y^{\left.\prime^{\prime}\right)}= \left(b_{11}, 2 b_{12}, \ldots, 2 b_{1 p}, b_{22}, \ldots, b_{p p}\right)^{\prime}$, where

$$
B=\sum_{\alpha=1}^{N} z_{\alpha} z_{\alpha}^{\prime}\left(=\sum_{\alpha=1}^{N} x_{\alpha} x_{\alpha}^{\prime}\right) .
$$

The vector $\boldsymbol{\omega}=\left(\boldsymbol{\omega}^{(1) \prime}, \boldsymbol{\omega}^{(2) \prime}\right)^{\prime}$ is composed of $\boldsymbol{\omega}^{(1)}=\sqrt{N} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$ and $\boldsymbol{\omega}^{(2)}= -\frac{1}{2}\left(\sigma^{11}, \sigma^{12}, \ldots, \sigma^{1 p}, \sigma^{22}, \ldots, \sigma^{p p}\right)^{\prime}$. The measure $m(A)$ is the Lebesgue measure of the set of $z_{1}, \ldots, z_{N}$ that maps into the set $A$.

Lemma 5.6.1. Let $B=A+N \bar{x} \bar{x}^{\prime}$. Then

$$
N \bar{x}^{\prime} A^{-1} \bar{x}=\frac{N \bar{x}^{\prime} B^{-1} \bar{x}}{1-N \bar{x}^{\prime} B^{-1} \bar{x}} .
$$

Proof of Lemma. If we let $\boldsymbol{B}=\boldsymbol{A}+\sqrt{N} \overline{\boldsymbol{x}} \sqrt{N} \overline{\boldsymbol{x}}^{\prime}$ in (10) of Section 5.2, we obtain by Corollary A.3.1

$$
\begin{aligned}
\frac{1}{1+T^{2} /(N-1)} & =\lambda^{2 / N}=\frac{\left|B-\sqrt{N} \bar{x} \sqrt{N} \bar{x}^{\prime}\right|}{|B|} \\
& =1-N \bar{x}^{\prime} B^{-1} \bar{x}
\end{aligned}
$$

Thus the acceptance region of a $T^{2}$-test is

$$
A=\left\{z_{N}, \boldsymbol{B} \mid z_{N}^{\prime} \boldsymbol{B}^{-1} z_{N^{\prime}} \leq k, \boldsymbol{B} \text { positive definite }\right\}
$$

for a suitable $k$.
The function $\boldsymbol{z}_{N}^{\prime} \boldsymbol{B}^{-1} \boldsymbol{z}_{N}$ is convex in ( $\boldsymbol{z}, \boldsymbol{B}$ ) for $\boldsymbol{B}$ positive definite (Problem 5.17). Therefore, the set $z_{N}^{\prime} B^{-1} z_{N} \leq k$ is convex. This shows that the set $A$ is convex. Furthermore, the closure of $A$ is convex (Problem 5.18), and the probability of the boundary of $A$ is 0 .

Now consider the other condition of Theorem 5.6.5. Suppose $A$ is disjoint with the half-space

$$
c<\boldsymbol{\omega}^{\prime} \boldsymbol{y}=\boldsymbol{\nu}^{\prime} z_{N}-\frac{1}{2} \operatorname{tr} \Lambda \mathbf{B},
$$

where $A$ is a symmetric matrix and $B$ is positive semidefinite. We shall take $\Lambda_{1}=I$. We want to show that $\boldsymbol{\omega}_{1}+\lambda \boldsymbol{\omega} \in \Omega-\Omega_{0}$; that is, that $\boldsymbol{\nu}_{1}+\lambda \boldsymbol{\nu} \neq 0$ (which is trivial) and $\Lambda_{1}+\lambda \Lambda$ is positive defirite for $\lambda>0$. This is the case when $\Lambda$ is positive semidefinite. Now we shall show that a half-space (21) disjoint with $A$ and $\Lambda$ not positive semidefinite implies a contradiction. If $\Lambda$ is not positive semidefinite, it can be written (by Corollary A.4.1 of the Appendix)

$$
\Lambda=D\left[\begin{array}{rrr}
I & 0 & 0 \\
0 & -I & 0 \\
0 & 0 & 0
\end{array}\right] D^{\prime},
$$

where $\boldsymbol{D}$ is nonsingular. If $\Lambda$ is not positive semidefinite, $\boldsymbol{-} \boldsymbol{I}$ is not vacuous, because its order is the number of negative characteristic roots of $\Lambda$. Let $z_{1}=(1 / \gamma) z_{0}$ and

$$
B=\left(D^{\prime}\right)^{-1}\left[\begin{array}{rrr}
I & 0 & 0 \\
0 & \gamma I & 0 \\
0 & 0 & I
\end{array}\right] D^{-1}
$$

Then

$$
\boldsymbol{\omega}^{\prime} \boldsymbol{y}=\frac{1}{\gamma} \boldsymbol{\nu}^{\prime} z_{0}+\frac{1}{2} \operatorname{tr}\left[\begin{array}{rrr}
-\boldsymbol{I} & \mathbf{0} & \mathbf{0} \\
\mathbf{0} & \gamma \boldsymbol{J} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \mathbf{0}
\end{array}\right],
$$

which is greater than $c$ for sufficiently large $\gamma$. On the other hand

$$
z_{N}^{\prime} B^{-1} z_{N}=\frac{1}{\gamma^{2}} z_{0}^{\prime} D\left[\begin{array}{rrr}
\boldsymbol{I} & \mathbf{0} & \mathbf{0} \\
\mathbf{0} & \gamma^{-1} \boldsymbol{I} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \boldsymbol{I}
\end{array}\right] D^{\prime} z_{0}
$$

which is less than $k$ for sufficiently large $\gamma$. This contradicts the fact that (20) and (21) are disjoint. Thus the conditions of Theorem 5.6.5 are satisfied and the theorem is proved.

This proof is due to Stein.
An alternative proof of admissibility is to show that the $T^{2}$-test is a proper Bayes procedure. Suppose an arbitrary random vector $X$ has density $f(\boldsymbol{x} \mid \boldsymbol{\omega})$ for $\omega \in \Omega$. Consider testing the null hypothesis $H_{0}: \omega \in \Omega_{0}$ against the alternative $H_{1}: \omega \in \Omega-\Omega_{0}$. Let $\Pi_{0}$ be a prior finite measure on $\Omega_{0}$, and $\Pi_{1}$ a prior finite measure on $\Omega_{1}$. Then the Bayes procedure (with $0-1$ loss
function) is to reject $H_{0}$ if

$$
\frac{\int f(\boldsymbol{x} \mid \boldsymbol{\omega}) \Pi_{1}(d \boldsymbol{\omega})}{\int f(\boldsymbol{x} \mid \boldsymbol{\omega}) \Pi_{0}(d \boldsymbol{\omega})} \geq c
$$

for some $c(0 \leq c \leq \infty)$. If equality in (26) occurs with probability 0 for all $\boldsymbol{\omega} \in \Omega_{0}$, then the Bayes procedure is unique and hence admissible. Since the measures are finite, they can be normed to be probability measures. For the $T^{2}$-test of $H_{0}: \boldsymbol{\mu}=\mathbf{0}$ a pair of measures is suggested in Problem 5.15. (This pair is not unique.) The reader can verify that with these measures (26) reduces to the complement of (20).

Among invariant tests it was shown that the $T^{2}$-test is uniformly most powerful; that is, it is most powerful against every value of $\boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$ among invariant tests of the specified significance level. We can ask whether the $T^{2}$-test is "best" against a specified value of $\boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$ among all tests. Here "best" can be taken to mean admissible minimax; and "minimax" means maximizing with respect to procedures the minimum with respect to parameter values of the power. This property was shown in the simplest case of $p=2$ and $N=3$ by Giri, Kiefer, and Stein (1963). The property for general $p$ and $N$ was announced by Salaevskĩ (1968). He has furnished a proof for the case of $p=2$ [Šalaevskĩ̆ (1971)], but has not given a proof for $p>2$.

Giri and Kiefer (1964) have proved the $T^{2}$-test is locally minimax (as $\boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu} \rightarrow 0$ ) and asymptotically (logarithmically) minimax as $\boldsymbol{\mu}^{\prime} \check{\Sigma}^{-1} \boldsymbol{\mu} \rightarrow \infty$.

### 5.7. ELLIPTICALLY CONTOL RED DISTRIBUTIONS

### 5.7.1. Observations Elliptically Contoured

When $x_{1}, \ldots, x_{N}$ constitute a sample of $N$ from

$$
|\Lambda|^{-\frac{1}{2}} g\left[(x-v)^{\prime} \Lambda^{-1}(x-v)\right],
$$

the sample mean $\bar{x}$ and covariance $S$ are unbiased estimators of the distribution mean $\mu=v$ and covariance matrix $\Sigma=\left(\mathscr{E} R^{2} / p\right) \Lambda$, where $R^{2}= (\boldsymbol{X}-\boldsymbol{v})^{\prime} \boldsymbol{\Lambda}^{-1}(\boldsymbol{X}-\boldsymbol{v})$ has finite expectation. The $T^{2}$-statistic, $T^{2}=N(\overline{\boldsymbol{x}}- \boldsymbol{\mu})^{\prime} S^{-1}(\overline{\boldsymbol{x}}-\boldsymbol{\mu})$, can be used for tests and confidence regions for $\boldsymbol{\mu}$ when $\boldsymbol{\Sigma}$ (or $\mathbf{\Lambda}$ ) is unknown, but the small-sample distribution of $T^{2}$ in general is difficult to obtain. However, the limiting distribution of $T^{2}$ when $N \rightarrow \infty$ is obtained from the facts that $\sqrt{N}(\overline{\boldsymbol{x}}-\boldsymbol{\mu}) \xrightarrow{d} N(\mathbf{0}, \mathbf{\Sigma})$ and $\boldsymbol{S} \xrightarrow{p} \boldsymbol{\Sigma}$ (Theorem 3.6.2).

Theorem 5.7.1. Let $x_{1}, \ldots, x_{N}$ be a sample from (1). Assume $\mathscr{E} R^{2}<\infty$. Then $T^{2} \xrightarrow{d} \chi_{p}^{2}$.

Proof. Theorem 3.6.2 implies that $N(\bar{x}-\boldsymbol{\mu})^{\prime} \boldsymbol{\Sigma}^{-1}(\bar{x}-\boldsymbol{\mu}) \xrightarrow{d} \chi_{p}^{2}$ and $N(\bar{x} -\boldsymbol{\mu})^{\prime} \boldsymbol{\Sigma}^{-1}(\overline{\boldsymbol{x}}-\boldsymbol{\mu})-T^{2} \xrightarrow{p} 0$. $\square$

Theorem 5.7.1 implies that the procedures in Section 5.3 can be done on an asymptotic basis for elliptically contoured distributions. For example, to test the null hypothesis $\boldsymbol{\mu}=\boldsymbol{\mu}_{11}$, reject the null hypothesis if

$$
N\left(\bar{x}-\boldsymbol{\mu}_{0}\right)^{\prime} S^{-1}\left(\bar{x}-\boldsymbol{\mu}_{0}\right) \geq \chi_{p}^{2}(\alpha),
$$

where $\chi_{p}^{2}(\alpha)$ is the $\alpha$-significance point of the $\chi^{2}$-distribution with $p$ degrees of freedom the limiting probability of (2) when the null hypothesis is true and $N \rightarrow \infty$ is $\alpha$. Similarly the confidence region $N(\bar{x}-m)^{\prime} S^{-1}(\bar{x}-m) \leq \chi_{p}^{2}(\alpha)$ has limiting confidence $1-\alpha$.

### 5.7.2. Elliptically Contoured Matrix Distributions

Let $X(N \times p)$ have the density

$$
|C|^{-N} g\left[C^{-1}\left(X-\varepsilon_{N} v^{\prime}\right)^{\prime}\left(X-\varepsilon_{N} v^{\prime}\right)\left(C^{\prime}\right)^{-1}\right]
$$

based on the left spherical density $g\left(\boldsymbol{Y}^{\prime} \boldsymbol{Y}\right)$. Here $\boldsymbol{Y}$ has the representation $\boldsymbol{Y} \stackrel{d}{=} \boldsymbol{U} \boldsymbol{R}^{\prime}$, where $\boldsymbol{U}(N \times p)$ has the uniform distribution on $O(N \times p), \boldsymbol{R}$ is lower triangular, and $\boldsymbol{U}$ and $\boldsymbol{R}$ are independent. Then $\boldsymbol{X} \stackrel{d}{=} \boldsymbol{\varepsilon}_{N} \boldsymbol{v}^{\prime}+\boldsymbol{U} \boldsymbol{R}^{\prime} \boldsymbol{C}^{\prime}$. The $T^{2}$-criterion to test the hypothesis $\boldsymbol{v}=\mathbf{0}$ is $N \overline{\boldsymbol{x}}^{\prime} S^{-1} \overline{\boldsymbol{x}}$, which is invariant with respect to transformations $\boldsymbol{X} \rightarrow \boldsymbol{X} \boldsymbol{G}$. By Corollary 4.5.5 we obtain the following theorem.

Theorem 5.7.2. Suppose $X$ has the density (3) with $\boldsymbol{v}=\mathbf{0}$ and $T^{2}= N \bar{x}^{\prime} S^{-1} \bar{x}$. Then $\left[T^{2} /(N-1)\right][(N-p) / p]$ has the distribution of $F_{p, N-p}= \left(\chi_{p}^{2} / p\right) /\left[\chi_{N-p}^{2} /(N-p)\right]$.

Thus the tests of hypotheses and construction of confidence regions at stated significance and confidence levels are valid for left spherical distributions.

The $T^{2}$-criterion for $H: \boldsymbol{v}=\mathbf{0}$ is

$$
T^{2}=N \bar{x}^{\prime} S^{-1} \bar{x} \stackrel{d}{=} N \bar{u}^{\prime} S_{u}^{-1} \bar{u},
$$

since $X^{d} U R^{\prime} C^{\prime}$,

$$
\bar{x}^{\prime}=\frac{1}{N} \boldsymbol{\varepsilon}_{N}^{\prime} X \stackrel{d}{=}\left(\frac{1}{N} \boldsymbol{\varepsilon}_{N}^{\prime} U\right) \boldsymbol{R}^{\prime} \boldsymbol{C}^{\prime}=\bar{u}^{\prime}(C R)^{\prime},
$$

and ⋅

$$
\begin{aligned}
S & =\frac{1}{N-1}\left(X^{\prime} X-N x \tilde{x}^{\prime}\right)=\frac{1}{N-1}\left[C R U^{\prime} U R C^{\prime}-C R \bar{u} \bar{u}^{\prime}\left(C^{\prime} R\right)^{\prime}\right] \\
& =C R S_{u}(C R)^{\prime}
\end{aligned}
$$

### 5.7.3. Linear Combinations

Läuter, Glimm, and Kropf (1996a, 1996b. 1996c) have observed that a statistician can use $X^{\prime} X=C R R^{\prime} C^{\prime}$ when $\nu=0$ to determine a $p \times q$ matrix $D$ and base a $T$-test on the transform $Z=X D$. Specifically, define

$$
\begin{aligned}
& \bar{z}^{\prime}=\frac{1}{N} \varepsilon_{N}^{\prime} Z=\bar{x}^{\prime} D, \\
& S_{Z}=\frac{1}{N-1}\left(Z^{\prime} Z-N \overline{z \bar{z}^{\prime}}\right)=D^{\prime} S D, \\
& T_{D}^{2}=N \bar{z}^{\prime} S_{Z}^{-1} \bar{z}^{\prime} .
\end{aligned}
$$

Since $\boldsymbol{Q}_{N} Z \stackrel{d}{=} \boldsymbol{Q}_{N} U R^{\prime} \boldsymbol{C}^{\prime} \stackrel{d}{=} U R^{\prime} \boldsymbol{C}^{\prime}=Z$, the matrix $Z$ is based on the leftspherical $Y D$ and hence has the representation $Z=V R^{* \prime}$, where $V(N \times q)$ has the uniform distribution on $O(N \times p)$, independent of $\boldsymbol{R}^{* \prime}$ (upper triangular) having the distribution derived from $R^{*} R^{* \prime}=Z^{\prime} Z$. The distribution of $T^{2} /(N-1)$ is $F_{q, N-q} q /(N-q)$.

The matrix $D$ can also involve prior information as well as knowledge of $X^{\prime} X$. If $p$ is large, $q$ can be small; the power of the test based on $T_{D}^{2}$ may be more powerful than a test based on $T^{2}$.

Läuter, Glimm, and Kropf give several examples of choosing $D$. One of them is to chose $D(p \times 1)$ as $\left[\operatorname{Diag}\left(X^{\prime} X\right)^{-\frac{1}{2}}\right] \boldsymbol{\varepsilon}_{p}$, where Diag $A$ is a diagonal matrix with $i$ th diagonal element $a_{i r}$. The statistic $T_{D}^{\prime}$ is called the standardized sum statistic:

## PROBLEMS

5.1. (Sec. 5.2) Let $\boldsymbol{x}_{\boldsymbol{\alpha}}$ be distributed according to $N\left(\boldsymbol{\mu}+\boldsymbol{\beta}\left(z_{\boldsymbol{\alpha}}-\vec{z}\right), \boldsymbol{\Sigma}\right), \alpha= ], \ldots, N$, where $\bar{z}=(1 / N) \Sigma z_{\alpha}$. Let $b=\left[1 / \Sigma\left(z_{\alpha}-\bar{z}\right)^{2}\right] \Sigma x_{\alpha}\left(z_{\alpha}-\bar{z}\right),(N-2) S= \sum\left[x_{\alpha}-\bar{x}-b\left(z_{\alpha}-\bar{z}\right)\right]\left[x_{\alpha}-\bar{x}-b\left(z_{\alpha}-\bar{z}\right)\right]^{\prime}$, and $T^{2}=\sum\left(z_{\alpha}-\bar{z}\right)^{2} b^{\prime} S^{-1} b$. Show that $T^{2}$ has the $T^{2}$-distribution with $N-2$ degrees of freedom. [Hinr: See Problem 3.13.]
5.2. (Sec. 5.2.2) Show that $T^{2} /(N-1)$ can be written as $R^{2} /\left(1-R^{2}\right)$ with the correspondences given in Table 5.1.

Table 5.1
| Section 5.2 | Section 4.4 |
| :--- | :--- |
| $x_{0 a}=1 / \sqrt{N}$ | $z_{1 a}$ |
| $x_{a}$ | $z_{a}^{(2)}$ |
| $\sqrt{N} \bar{x}$ | $a_{(1)}=\sum z_{1 a} z_{a}^{(2)}$ |
| $B=\sum x_{a} x_{a}^{\prime}$ | $A_{22}=\sum z_{a}^{(2)} z_{a}^{(2)}$ |
| $1=\sum x_{0 a}^{2}$ | $a_{11}=\sum z_{1 a}^{2}$ |
| $T^{2}$ | $\frac{R^{2}}{1-R^{2}}$ |
| $\overline{N-1}$ | $p-1$ |
| $p$ | $n$ |
| $N$ |  |


5.3. (Sec. 5.2 2) Let

$$
\frac{R^{2}}{1-R^{2}}=\frac{\sum u_{a} x_{a}^{\prime}\left(\sum x_{a} x_{a}^{\prime}\right)^{-1} \sum u_{a} x_{a}}{\sum u_{a}^{2}-\sum u_{a} x_{a}^{\prime}\left(\sum x_{a} x_{a}^{\prime}\right)^{-1} \sum u_{a} x_{a}},
$$

where $u_{1}, \ldots u_{N}$ are $N$ numbers and $x_{1}, \ldots, x_{N}$ are independent, each with the distribution $N(\mathbf{0}, \mathbf{\Sigma})$. Prove that the distribution of $R^{2} /\left(1-R^{2}\right)$ is independent of $u_{1}, \ldots, u_{N^{-}}$[Hint: There is an orthogonal $N \times N$ matrix $\boldsymbol{C}$ that carries $\left(t_{1}, \ldots, u_{N}\right)$ into a vector proportional to $(1 / \sqrt{N}, \ldots, 1 / \sqrt{N})$.]
5.4. (Sec. 5.2.2) Use Problems 5.2 and 5.3 to show that $\left[T^{2} /(N-1)\right][(N-p) / p]$ has the $F_{p, N-p}$-distribution (under the null hypothesis). [Note: This is the analysis that corresponds to Hotelling's geometric proof (1931).]
5.5. (Sec. 5.2.2) Let $T^{2}=N \bar{x}^{\prime} S^{-1} \bar{x}$, where $\bar{x}$ and $S$ are the mean vector and covariance matrix of a sample of $N$ from $N(\mu, \Sigma)$. Show that $T^{2}$ is distributed the same when $\boldsymbol{\mu}$ is replaced by $\lambda=(\tau, 0, \ldots, 0)^{\prime}$, where $\tau^{2}=\boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$, and $\boldsymbol{\Sigma}$ is replaced by $I$.
5.6. (Sec. 5.2.2) Let $u=\left[T^{2} /(N-1)\right] /\left[1+T^{2} /(N-1)\right]$. Show that $u= \boldsymbol{\gamma} \boldsymbol{V}^{\prime}\left(\boldsymbol{V} \boldsymbol{V}^{\prime}\right)^{-1} \boldsymbol{V} \boldsymbol{\gamma}^{\prime}$, where $\boldsymbol{\gamma}=(1 / \sqrt{N}, \ldots, 1 / \sqrt{N})$ and

$$
V=\left(\begin{array}{c}
v_{1} \\
\vdots \\
v_{p}
\end{array}\right)=\left(\begin{array}{ccc}
x_{11} & \cdots & x_{1 N} \\
\vdots & & \vdots \\
x_{p 1} & \cdots & x_{p N}
\end{array}\right) .
$$



5.7. (Sec. 5.2.2) Let

$$
\begin{aligned}
& v_{1}^{*}=v_{1}, \\
& v_{i}^{*}=v_{1}-\frac{v_{i} v_{1}^{\prime}}{v_{1} v_{1}^{\prime}} v_{1}=v_{1}\left(I-\frac{1}{v_{1} v_{1}^{\prime}} v_{1}^{\prime} v_{1}\right), \quad i \neq 1 \\
& \gamma^{*}=\gamma-\frac{\gamma v_{1}^{\prime}}{v_{1} v_{1}^{\prime}} v_{1} \\
& V^{*}=\left(\begin{array}{c}
v_{1}^{*} \\
\vdots \\
v_{p}^{*}
\end{array}\right) .
\end{aligned}
$$

Prove that $U=s+(1-s) w$, where

$$
\begin{aligned}
& s=\frac{\left(\gamma \nu_{1}^{* \prime}\right)^{2}}{\nu_{1}^{*} \nu_{1}^{* \prime}}=\frac{\left(\gamma \nu_{1}^{\prime}\right)^{2}}{\nu_{1} \nu_{1}^{\prime}}, \\
& w=\frac{1}{\gamma^{*} \gamma^{* \prime}} \gamma^{*}\left(\begin{array}{c}
\nu_{2}^{*} \\
\vdots \\
\nu_{p}^{*}
\end{array}\right)^{\prime}\left(\begin{array}{ccc}
\nu_{2}^{*} \nu_{2}^{* \prime} & \cdots & \nu_{2}^{*} \nu_{p}^{* \prime} \\
\vdots & & \vdots \\
\nu_{p}^{*} \nu_{2}^{* \prime} & \cdots & \nu_{p}^{*} \nu_{p}^{* \prime}
\end{array}\right)^{-1}\left(\begin{array}{c}
\nu_{2}^{*} \\
\vdots \\
\nu_{p}^{*}
\end{array}\right) \gamma^{* \prime} .
\end{aligned}
$$

Hint: $\boldsymbol{E V}=\boldsymbol{V}^{*}$, where

$$
\boldsymbol{E}=\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
-\frac{\boldsymbol{v}_{2} \boldsymbol{v}_{1}^{\prime}}{\boldsymbol{v}_{1} \boldsymbol{v}_{1}^{\prime}} & 1 & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
-\frac{\boldsymbol{v}_{p} \boldsymbol{v}_{1}^{\prime}}{\boldsymbol{v}_{1} \boldsymbol{v}_{1}^{\prime}} & 0 & \cdots & 1
\end{array}\right) .
$$

5.8. (Sec. 5.2.2) Prove that $w$ has the distribution of the square of a multiple correlation between one vector and $p-1$ vcctors in ( $N-1$ )-space without subtracting means; that is, it has density

$$
\frac{\Gamma\left[\frac{1}{2}(N-1)\right]}{\Gamma\left[\frac{1}{2}(N-p)\right] \Gamma\left[\frac{1}{2}(p-1)\right]} w^{\frac{1}{2}(p-1)-1}(1-w)^{\frac{1}{2}(N-p)-1}
$$

[Hint: The transformation of Problem 5.7 is a projection of $\boldsymbol{\nu}_{2}, \ldots, \boldsymbol{\nu}_{p}, \boldsymbol{\gamma}$ on the ( $N-1$ )-space orthogonal to $\boldsymbol{\nu}_{1}$.]
5.9. (Sec. 52,2) Verify that $r=s /(1-s)$ multiplied by $(N-1) / 1$ has the noncentral $F$-distribution with 1 and $N-1$ degrees of freedom and noncentrality parameter $N T^{2}$.
5.10. (Sec. 5.2.2) From Problems 5.5-5.9, verify Corollary 5.2.1.
5.11. (Sec. 5.3) Use the data in Section 3.2 to test the hypothesis that neither drug has a soporific effect at significance level 0.01 .
5.12. (Sec. 5.3) Using the data in Section 3.2, give a confidence region for $\mu$ with confidence coefficient 0.95 .
5.13. (Sec. 5.3) Prove the statement in Section 5.3.6 that the $T^{2}$-statistic is independent of the choice of $\boldsymbol{C}$.
5.14. (Sec. 5.5) Use the data of Problem 4.41 to test the hypothesis that the mean head length and breadth of first sons are equal to those of second sons at significance level 0.01.
5.15. (Sec. 5.6.2) $T^{2}$-test as a Bayes procedure [Kiefer and Schwartz (1965)]. Let $x_{1}, \ldots, x_{N}$ be independently distributed, each according to $N(\mu, \Sigma)$. Let $\Pi_{0}$ be defined by $[\boldsymbol{\mu}, \boldsymbol{\Sigma}]=\left[\boldsymbol{0},\left(\boldsymbol{I}+\boldsymbol{\eta} \boldsymbol{\eta}^{\prime}\right)^{-1}\right]$ with $\boldsymbol{\eta}$ having a density proportional to $\left|\boldsymbol{I}+\boldsymbol{\eta} \boldsymbol{\eta}^{\prime}\right|^{-\frac{1}{2} N}$, and let $\boldsymbol{\Pi}_{1}$ be defined by $[\boldsymbol{\mu}, \boldsymbol{\Sigma}]=\left[\left(\boldsymbol{I}+\boldsymbol{\eta} \boldsymbol{\eta}^{\prime}\right)^{-1} \boldsymbol{\eta},\left(\boldsymbol{I}+\boldsymbol{\eta} \boldsymbol{\eta}^{\prime}\right)^{-1}\right]$ with $\boldsymbol{\eta}$ having a density proportional to

$$
\left|\boldsymbol{I}+\boldsymbol{\eta} \boldsymbol{\eta}^{\prime}\right|^{-\frac{1}{2} N} \exp \left[\frac{1}{2} N \boldsymbol{\eta}^{\prime}\left(\boldsymbol{I}+\boldsymbol{\eta} \boldsymbol{\eta}^{\prime}\right)^{-1} \boldsymbol{\eta}\right] .
$$

(a) Show that the neasures are finite for $N>p$ by showing $\boldsymbol{\eta}^{\prime}\left(I+\boldsymbol{\eta} \boldsymbol{\eta}^{\prime}\right)^{-1} \boldsymbol{\eta} \leq 1$ and verifying that the integral of $\left|I+\eta \eta^{\prime}\right|^{-\frac{1}{2} N}=\left(1+\eta \eta^{\prime}\right)^{-\frac{1}{2} N}$ is finite.
(b) Show that the inequality (26) is equivalent to $N \bar{x}^{\prime}\left(\sum_{\alpha=1}^{N} x_{\alpha} x_{\alpha}^{\prime}\right)^{-1} \bar{x} \geq k$. Hence the $T^{2}$-test is Bayes and thus admissible.
5.16. (Sec. 5.6.2) Let $g(t)=f\left[t y_{1}+(1-t) y_{2}\right]$, where $f(y)$ is a real valued function of the vector $y$. Prove that if $g(t)$ is convex, then $f(y)$ is convex.
5.17. (Sec. 5.6.2) Show that $z^{\prime} B^{-1} z$ is a convex function of $(z, B)$, where $B$ is a positive definite matrix. [Hint: Use Problem 5.16.]
5.18. (Sec. 5.6.2) Prove that if the set $A$ is convex, then the closure of $A$ is convex.
5.19. (Sec. 5.3) Let $\bar{x}$ and $S$ be based on $N$ observations from $N(\mu, \Sigma)$, and let $x$ be an additional observation from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. Show that $x-\overline{\boldsymbol{x}}$ is distributed according to

$$
N[\mathbf{0},(1+1 / N) \boldsymbol{\Sigma}] .
$$

Verify that $[N /(N+1)](x-\bar{x})^{\prime} S^{-1}(x-\bar{x})$ has the $T^{2}$-distribution with $N-1$ degrees of freedom. Show how this statistic can be used to give a prediction region for $x$ based on $\bar{x}$ and $S$ (i.e., a region such that one has a given confidence that the next observation will fall into it).
5.20. (Sec. 5.3) Let $x_{\alpha}^{(i)}$ be observations from $N\left(\boldsymbol{\mu}^{(i)}, \Sigma_{i}\right), \alpha=1, \ldots, N, i=1,2$. Find the likelihood ratio criterion for testing the hyoothesis $\mu^{(1)}=\mu^{(2)}$.
5.21. (Sec. 5.4) Prove that $\boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$ is larger for $\boldsymbol{\mu}^{\prime}=\left(\mu_{1}, \mu_{2}\right)$ than for $\boldsymbol{\mu}=\mu_{1}$ by verifying

$$
\frac{1}{1-\rho^{2}}\left(\frac{\mu_{1}^{2}}{\sigma_{1}^{2}}-2 \rho \frac{\mu_{1} \mu_{2}}{\sigma_{1} \sigma_{2}}+\frac{\mu_{2}^{2}}{\sigma_{2}^{2}}\right)=\frac{\mu_{1}^{2}}{\sigma_{1}^{2}}+\frac{\left(\mu_{2}-\rho \sigma_{2} \mu_{1} / \sigma_{1}\right)^{2}}{\left(1-\rho^{2}\right) \sigma_{2}^{2}} .
$$

Discuss the power of the test $\mu_{1}=0$ compared to the power of the test $\mu_{1}=0$, $\mu_{2}=0$.
5.22. (Sec. 5.3)
(a) Using the data of Section 5.3.4, test the hypothesis $\mu_{1}^{(1)}=\mu_{1}^{(2)}$.
(b) Test the hypothesis $\mu_{1}^{(1)}=\mu_{1}^{(2)}, \mu_{2}^{(1)}=\mu_{2}^{(2)}$.
5.23. (Sec. 5.4) Let

$$
\mu=\binom{\mu^{(1)}}{\mu^{(2)}}, \quad \Sigma=\left(\begin{array}{ll}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{array}\right) .
$$

Prove $\boldsymbol{\mu}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu} \geq \boldsymbol{\mu}^{(1)} \boldsymbol{\Sigma}_{11}^{-1} \boldsymbol{\mu}^{(1)}$. Give a condition for strict inequality to hold. [Hint: This is the vector analog of Problem 5.21.]
5.24. Let $X^{(i) \prime}=\left(Y^{(i) \prime}, Z^{(i) \prime}\right), i=1,2$, where $Y^{(i)}$ has $p$ components and $Z^{(1)}$ has $q$ components, be distributed according to $N\left(\boldsymbol{\mu}^{(i)}, \boldsymbol{\Sigma}\right)$, where

$$
\mu^{(i)}=\binom{\mu_{y}^{(1)}}{\mu_{z}^{(i)}}, \quad \boldsymbol{\Sigma}=\left(\begin{array}{cc}
\Sigma_{y y} & \Sigma_{y z} \\
\Sigma_{z y} & \Sigma_{z z}
\end{array}\right), \quad i=1,2 .
$$

Find the likelihood ratio criterion (or equivalent $T^{2}$-criterion) for testing $\mu_{:}^{(1)}= \boldsymbol{\mu}_{z}^{(2)}$ given $\boldsymbol{\mu}_{y}^{(1)}=\boldsymbol{\mu}_{y}^{(2)}$ on the basis of a sample of $N_{i}$ on $\boldsymbol{X}^{(1)}, i=1,2$. [Hint: Express the likelihood in terms of the marginal density of $Y^{(1)}$ and the conditional density of $Z^{(i)}$ given $Y^{(i)}$.]
5.25. Find the distribution of the criterion in the preceding problem under the null hypothesis.
5.26. (Sec. 5.5) Suppose $x_{\alpha}^{(g)}$ is an observation from $N\left(\mu^{(g)} \cdot \Sigma_{k}\right), \alpha=1 \ldots N_{k}$. $g=1, \ldots, q$.
(a) Show that the hypothesis $\boldsymbol{\mu}^{(1)}=\cdots=\boldsymbol{\mu}^{(q)}$ is equivalent to $\mathscr{E} y_{\alpha}^{(i)}=\mathbf{0}$, $i=1, \ldots, q-1$, where

$$
\begin{array}{r}
y_{\alpha}^{(l)}=a_{1}^{(l)} x_{\alpha}^{(l)}+\sum_{g=2}^{q} a_{g}^{(i)}\left(\frac{N_{1}}{N_{g}}\right)^{\frac{1}{2}}\left[x_{\alpha}^{(g)}-\frac{1}{N_{1}} \sum_{\beta=1}^{N_{1}} x_{\beta}^{(g)}+\frac{1}{\left(N_{1} N_{g}\right)^{\frac{1}{2}}} \sum_{\beta=1}^{N_{g}} x_{\beta}^{(g)}\right], \\
\alpha=1, \ldots, N_{1}, \quad i=1, \ldots, q-1 ;
\end{array}
$$

$N_{1} \leq N_{g} . g=2, \ldots, q ;$ and $\left.(q)^{(i)}, \ldots, a_{q}^{(i)}\right), i=1, \ldots, q-1$, are linearly indeperident.
(b) Show how to construct a $T^{2}$-test of the hypothesis using $\left(\bar{y}^{(1) \prime}, \ldots, \bar{y}^{(q-1)^{\prime}}\right)^{\prime}$ yielding an $F$-statistic with $(q-1) p$ and $N-(q-1) p$ degrees of freedom [Anderson (1963b)].
5.27. (Sec.5.2) Prove (25) is the density of $V=x_{a}^{2} /\left(x_{a}^{2}+x_{b}^{2}\right)$. [Hint: In the joint density of $U=\chi_{a}^{2}$ and $W=\chi_{b}^{2}$ make the transformation $u=v w(1-v)^{-1}, w=w$ and integrate out $w$.]

## Classification of Observations

### 6.1. THE PROBLEM OF CLASSIFICATION

The problem of classification arises when an investigator makes a number of measurements on an individual and wishes to classify the individual into one of several categories on the basis of these measurements. The investigator cannot identify the individual with a category directly but must use these measurements. In many cases it can be assumed that there are a finite number of categories or populations from which the individual may have come and each population is characterized by a probability distribution of the measurements. Thus an individual is considered as a random observation from this population. The question is: Given an individual with certain measurements, from which population did the person arise?

The problem of classification may be considered as a problem of "statistical decision functions." We have a number of hypotheses: Each hypothesis is that the distribution of the observation is a given one. We must accept one of these hypotheses and reject the others. If only two populations are admitted, we have an elementary problem of testing one hypothesis of a specified distribution against another.

In some instances, the categories are specified beforehand in the sense that the probability distributions of the measurements are assumed completely known. In other cases, the form of each distribution may be known, but the parameters of the distribution must be estimated from a sample from that population.

Let us give an example of a problem of classification. Prospective students applying for admission into college are given a battery of tests; the "ector of

[^0]scores is a set of measurements $x$. The prospective student may be a member of one population consisting of those students who will successfully complete college training or, rather, have potentialities for successfully completing training, or the student may be a member of the other population, those who will not complete the college course successfully. The problem is to classify a student applying for admission on the basis of his scores on the entrance examination.

In this chapter we shall develop the theory of classification in general terms and then apply it to cases involving the normal distribution. In Section 6.2 the problem of classification with two populations is defined in terms of decision theory, and in Section 6.3 Bayes and admissible solutions are obtained. In Section 6.4 the theory is applied to two known normal populations, differing with respect to means, yielding the population linear discriminant function. When the parameters are unknown, they are replaced by estimates (Section 6.5). An alternative procedure is maximum likelihood. In Section 6.6 the probabilities of misclassification by the two methods are evaluated in terms of asymptotic expansions of the distributions. Then these developments are carried out for scvcral populations. Finally, in Scction 6.10 linear procedures for the two populations are studied when the covariance matrices are different and the parameters are known.

### 6.2. STANDARDS OF GOOD CLASSIFICATION

### 6.2.1. Preliminary Considerations

In constructing a procedure of classification, it is desired to minimize the probability of misclassification, or, more specifically, it is desired to minimize on the average the bad effects of misclassification. Now let us make this notion precise. For convenience we shall now consider the case of only two categories. Later we shall treat the more general case. This section develops the ideas of Section 3.4 in more detail for the problem of two decisions.

Suppose an individual is an observation from either population $\pi_{1}$ or population $\pi_{2}$. The classification of an observation depends on the vector of measurements $x^{\prime}=\left(x_{1}, \ldots, x_{p}\right)$ on that individual. We set up a rule that if an individual is characterized by certain sets of values of $x_{1}, \ldots, x_{p}$ that person will be classified as from $\pi_{1}$, if other values, as from $\pi_{2}$.

We can think of an observation as a point in a $p$-dimensional space. We divide this space into two regions. If the observation falls in $R_{1}$, we classify it as coming from population $\pi_{1}$, and if it falls in $R_{2}$ we classify it as coming from population $\pi_{2}$.

In following a given classification procedure, the statistician can make two kinds of errors in classification. If the individual is actually from $\pi_{1}$, the

Table 6.1
|  |  | Statistician's Decision |  |
| :--- | :---: | :---: | :---: |
|  |  | $\pi_{1}$ | $\pi_{2}$ |
| Population | $\pi_{1}$ | 0 | $C(2 \mid 1)$ |
|  | $\pi_{2}$ | $C(1 \mid 2)$ | 0 |
|  |  |  |  |


statistician can classify him or her as coming from population $\pi_{2}$; if from $\pi_{2}$, the statistician can classify him or her as from $\pi_{1}$. We need to know the relative undesirability of these two kinds of misclassification. Let the cost of the first type of misclassification be $C(2 \mid 1)(>0)$, and let the cost of misclassifying an individual from $\pi_{2}$ as from $\pi_{1}$ be $C(1 \mid 2)(>0)$. These costs may be measured in any kind of units. As we shall see later, it is only the ratio of the two costs that is important. The statistician may not know these costs in each case, but will often have at least a rough idea of them.

Table 6.1 indicates the costs of correct and incorrect classification. Clearly, a good classification procedure is one that minimizes in some sense or other the cost of misclassification.

### 6.2.2 Two Cases of Two Populations

We shall consider ways of defining "minimum cost" in two cases. In onc case we shall suppose that we have a priori probabilities of the two populations. Let the probability that an observation conces from population $\pi_{1}$ be $q_{1}$ and from population $\pi_{2}$ be $q_{2}\left(q_{1}+q_{2}=1\right)$. The probability properties of population $\pi_{1}$ are specified by a distribution function. For convenience we shall treat only the case where the distribution has a density, although the case of discrete probabilities lends itself to almost the same treatment. Let the density of population $\pi_{1}$ be $p_{1}(\boldsymbol{x})$ and that of $\pi_{2}$ be $p_{2}(\boldsymbol{x})$. If we have a region $R_{1}$ of classification as from $\pi_{1}$, the probability of correctly classifying an observation that actually is drawn from population $\pi_{1}$ is

$$
P(1 \mid 1, R)=\int_{R_{1}} p_{1}(x) d x
$$

where $d x=d x_{1} \cdots d x_{p}$, and the probability of misclassification of an observation from $\pi_{1}$ is

$$
P(2 \mid 1, R)=\int_{R_{2}} p_{1}(x) d x
$$

Similarly, the probability of correctly classifying an observation from $\pi_{2}$ is

$$
\left.P^{\prime} 2 \mid 2, R\right)=\int_{R} p_{2}(x) d x
$$

and the probability of misclassifying such an observation is

$$
P(1 \mid 2, R)=\int_{R_{1}} p_{2}(x) d x
$$

Since the probability of drawing an observation from $\pi_{1}$ is $q_{1}$, the probability of drawing an observation from $\pi_{1}$ and correctly classifying it is $q_{1} P(1 \mid 1, R)$; that is. this is the probability of the situation in the upper left-hand corner of Table 6.1. Similarly, the probability of drawing an observation from $\pi_{1}$ and misclassifying it is $q_{1} P(2 \mid 1, R)$. The probability associated with the lower left-hand corner of Table 6.1 is $q_{2} P(1 \mid 2, R)$, and with the lower right-hand corner is $q_{2} P(2 \mid 2, R)$.

What is tac average or expected loss from costs of misclassification? It is the sum of the products of costs of misclassifications with their respective probabilities of occurrence:

$$
C(2 \mid 1) P(2 \mid 1, R) q_{1}+C(1 \mid 2) P(1 \mid 2, R) q_{2} .
$$

It is this average loss that we wish to minimize. That is, we want to divide our space into regions $R_{1}$ and $R_{2}$ such that the expected loss is as small as possible. A procedure that minimizes (5) for given $q_{1}$ and $q_{2}$ is called a Bayes procedure.

In the example of admission of students, the undesirability of misclassification is, in one instance, the expense of teaching a student who will noi complete the course successfully and is, in the other instance, the undesirability of excluding from college a potentially good student.

The other case we shall treat is that in which there are no known a priori probabilities. In this case the expected loss if the observation is from $\pi_{1}$ is

$$
C(2 \mid 1) P(2 \mid 1, R)=r(1, R) ;
$$

the expected loss if the observation is from $\pi_{2}$ is

$$
C(1 \mid 2) P(1 \mid 2, R)=r(2, R) .
$$

We do not know whether the observation is from $\pi_{1}$ or from $\pi_{2}$, and we do not know probabilities of these two instances.

A procedure $R$ is at least as good as a procedure $R^{*}$ if $r(1, R) \leq r\left(1, R^{*}\right)$ and $r(2, R) \leq r\left(2, R^{*}\right) ; R$ is better than $R^{*}$ if at least one of these inequalities is a strict inequality. Usually there is no one procedure that is better than all other procedures or is at least as good as all other procedures. A procedure $R$ is called admissible if there is no procedure better than $R$; we shall be interested in the entire class of admissible procedures. It will be shown that under certain conditions this class is the same as the class of Bayes proce-
dures. A class of procedures is complete if for every procedure outside the class there is one in the class which is better; a class is called essentially complete if for every procedure outside the class there is one in the class which is at least as good. A minimal complete class (if it exists) is a complete class such that no proper subset is a complete class; a similar definition holds for a minimal essentially complete class. Under certain conditions we shall show that the admissible class is minimal complete. To simplify the discussion we shall consider procedures the same if they only differ on sets of probability zero. In fact, throughout the next section we shall make statements which are meant to hold except for sets of probability zero without saying so explicitly.

A principle that usually leads to a unique procedure is the minimax principle. A procedure is minimax if the maximum expected loss, $r(i, R)$, is a minimum. From a conservative point of view, this may be considered an optimum procedure. For a general discussion of the concepts in this section and the next see Wald (1950), Blackwell and Girshick (1954), Ferguson (1967), DeGroot (1970), and Berger (1980b).

### 6.3. PROCEDURES OF CLASSIFICATION INTO ONE OF TWO POPULATIONS WITH KNOWN PROBABILITY DISTRIBUTIONS

### 6.3.1. The Case When A Priori Probabilities Are Known

We now turn to the problem of choosing regions $R_{1}$ and $R_{2}$ so as to minimize (5) of Section 6.2. Since we have a priori probabilities, we can define joint probabilities of the population and the observed set of variables. The probability that an observation comes from $\pi_{1}$ and that each variate is less than the corresponding component in $y$ is

$$
\int_{-\infty}^{y_{p}} \cdots \int_{-\infty}^{y_{1}} q_{1} p_{1}(x) d x_{1} \cdots d x_{p} .
$$

We can also define the conditional probability that an observation came from a certain population given the values of the observed variates. For instance, the conditional probability of coming from population $\pi_{1}$, given an observation $x$, is

$$
\frac{q_{1} p_{1}(x)}{q_{1} p_{1}(x)+q_{2} p_{2}(x)} .
$$

Suppose for a moment that $C(1 \mid 2)=C(2 \mid 1)=1$. Then the expected loss is

$$
q_{1} \int_{R_{2}} p_{1}(\boldsymbol{x}) d \boldsymbol{x}+q_{2} \int_{R_{1}} p_{2}(\boldsymbol{x}) d \boldsymbol{x}
$$

This is also the probability of a misclassification; hence we wish to minimize the probability of misclassification.

For a given observed point $x$ we minimize the probability of a misclassification by assigning the population that has the higher conditional probability. If

$$
\frac{q_{1} p_{1}(x)}{q_{1} p_{1}(x)+q_{2} p_{2}(x)} \geq \frac{q_{2} p_{2}(x)}{q_{1} p_{1}(x)+q_{2} p_{2}(x)},
$$

we choose population $\pi_{1}$. Otherwise we choose population $\pi_{2}$. Since we minimize the probability of misclassification at each point, we minimize it over the whole space. Thus the rule is

$$
\begin{aligned}
& R_{1}: q_{1} p_{1}(x) \geq q_{2} p_{2}(x), \\
& R_{2}: q_{1} p_{1}(x)<q_{2} p_{2}(x) .
\end{aligned}
$$

If $q_{1} p_{1}(x)=q_{2} p_{2}(x)$, the point could be classified as either from $\pi_{1}$ or $\pi_{2}$; we have arbitrarily put it into $R_{1}$. If $q_{1} p_{1}(\boldsymbol{x})+q_{2} p_{2}(\boldsymbol{x})=0$ for a given $\boldsymbol{x}$, that point also may go into either region.

Now let us prove formally that (5) is the best procedure. For any procedure $R^{*}=\left(R_{1}^{*}, R_{2}^{*}\right)$, the probability of misclass'fication is

$$
\begin{aligned}
& q_{1} \int_{R_{2}^{*}} p_{1}(x) d x+q_{2} \int_{R_{1}^{*}} p_{2}(x) d x \\
& \quad=\int_{R_{2}^{*}}\left[q_{1} p_{1}(x)-q_{2} p_{2}(x)\right] d x+q_{2} \int p_{2}(x) d x
\end{aligned}
$$

On the right-hand side the second term is a given number; the first term is minimized if $R_{2}^{*}$ includes the points $\boldsymbol{x}$ such that $q_{1} p_{1}(\boldsymbol{x})-q_{2} p_{2}(\boldsymbol{x})<0$ and excludes the points for which $q_{1} p_{1}(x)-q_{2} p_{2}(x)>0$. If

$$
\operatorname{Pr}\left\{\left.\frac{p_{1}(x)}{p_{2}(x)}=\frac{q_{2}}{q_{1}} \right\rvert\, \pi_{i}\right\}=0,
$$

$$
i=1,2 .
$$

then the Bayes procedure is unique except for sets of probability zero.
Now we notice that mathematically the problem was: given nonnegative constants $q_{1}$ and $q_{2}$ and nonnegative functions $p_{1}(\boldsymbol{x})$ and $p_{2}(\boldsymbol{x})$, choose regions $R_{1}$ and $R_{2}$ so as to minimize (3). The solution is (5). If we wish to minimize (5) of Section 6.2, which can be written

$$
\left[C(2 \mid 1) q_{1}\right] \int_{R_{2}} p_{1}(x) d x+\left[C(1 \mid 2) q_{2}\right] \int_{R_{1}} p_{2}(x) d x
$$


[^0]:    An Introduction to Multivariate Statistical Analysis, Third Edition. By T. W. Anderson ISBN 0-471-36091-0 Copyright © 2003 John Wlley \& Sons, Inc.



we choose $R_{1}$ and $R_{2}$ according to

$$
\begin{aligned}
& R_{1}:\left[C(2 \mid 1) q_{1}\right] p_{1}(x) \geq\left[C(1 \mid 2) q_{2}\right] p_{2}(x), \\
& R_{2}:\left[C(2 \mid 1) q_{1}\right] p_{1}(x)<\left[C(1 \mid 2) q_{2}\right] p_{2}(x),
\end{aligned}
$$

since $C(2 \mid 1) q_{1}$ and $C(1 \mid 2) q_{2}$ are nonnegative constants. Another way of writing (9) is

$$
\begin{aligned}
& R_{1}: \frac{p_{1}(x)}{p_{2}(x)} \geq \frac{C(1 \mid 2) q_{2}}{C(2 \mid 1) q_{1}}, \\
& R_{2}: \frac{p_{1}(x)}{p_{2}(x)}<\frac{C(1 \mid 2) q_{2}}{C(2 \mid 1) q_{1}} .
\end{aligned}
$$

Theorem 6.3.1. If $q_{1}$ aid $q_{2}$ are a priori probabilities of drawing an observation from population $\pi_{1}$ with density $p_{1}(\boldsymbol{x})$ and $\pi_{2}$ with density $p_{2}(\boldsymbol{x})$, respectively, and if the cost of misclassifying an observation from $\pi_{1}$ as from $\pi_{2}$ is $C(2 \mid 1)$ and an observation from $\pi_{2}$ as from $\pi_{1}$ is $C(1 \mid 2)$, then the regions of classification $R_{1}$ and $R_{2}$, defined by (10), minimize the expected cost. If

$$
\operatorname{Pr}\left\{\left.\frac{p_{1}(x)}{p_{2}(x)}=\frac{q_{2} C(1 \mid 2)}{q_{1} C(2 \mid 1)} \right\rvert\, \pi_{1}\right\}=0, \quad i=1,2,
$$

then the procedure is unique except for sets of probability zero.

### 6.3.2. The Case When No Set of A Priori Probabilities Is Known

In many instances of classification the statistician cannot assign a priori probabilities to the two populations. In this case we shall look for the class of admissible procedures, that is, the set of procedures that cannot be improved upon.

First, let us prove that a Bayes procedure is admissible. Let $R=\left(R_{1}, R_{2}\right)$ be a Bayes procedure for a given $q_{1}, q_{2}$; is there a procedure $R^{*}=\left(R_{1}^{*}, R_{2}^{*}\right)$ such that $P\left(1 \mid 2, R^{*}\right) \leq P(1 \mid 2, R)$ and $P\left(2 \mid 1, R^{*}\right) \leq P(2 \mid 1, R)$ with at least one strict inequality? Since $R$ is a Bayes procedure,

$$
q_{1} P(2 \mid 1, R)+q_{2} P(1 \mid 2, R) \leq q_{1} P\left(2 \mid 1, R^{*}\right)+q_{2} P\left(1 \mid 2, R^{*}\right) .
$$

This inequality can be written

$$
q_{1}\left[P(2 \mid 1, R)-P\left(2 \mid 1, R^{*}\right)\right] \leq q_{2}\left[P\left(1 \mid 2, R^{*}\right)-P(1 \mid 2, R)\right] .
$$

Suppose $0<q_{1}<1$. Then if $P\left(1 \mid 2, R^{*}\right)<P(1 \mid 2, R)$, the right-hand side of (13) is less than zero and therefore $P(2 \mid 1, R)<P\left(2 \mid 1, R^{*}\right)$. Then $P\left(2 \mid 1, R^{*}\right) <P(2 \mid 1 . R)$ similarly implies $P(1 \mid 2, R)<P\left(1 \mid 2, R^{*}\right)$. Thus $R^{*}$ is not better than $R$, and $R$ is admissible. If $q_{1}=0$, then (13) implies $0 \leq P\left(1 \mid 2, R^{*}\right)$ $P(1 \mid 2, R)$. For a Bayes procedure, $R_{1}$ includes only points for which $p_{2}(x)=0$. Therefore, $P(1 \mid 2, R)=0$ and if $R^{*}$ is to be better $P\left(1 \mid 2, R^{*}\right)=0$. If $\operatorname{Pr}\left(p_{2}(x)\right. \left.=0 \mid \pi_{1}\right\}=0$, then $P(2 \mid 1, R)=\operatorname{Pr}\left\{p_{2}(x)>0 \mid \pi_{1}\right\}=1$. If $P\left(1 \mid 2, R^{*}\right)=0$, then $R_{1}^{*}$ contains only points for which $p_{2}(x)=0$. Then $P\left(2 \mid 1, R^{*}\right)=\operatorname{Pr}\left(R_{2}^{*} \mid \pi_{1}\right) =\operatorname{Pr}\left\{p_{2}(x)>0 \mid \pi_{1}\right\}=1$, and $R^{*}$ is not better than $R$.

Theorem 6.3.2. If $\operatorname{Pr}\left\{p_{2}(x)=0 \mid \pi_{1}\right\}=0$ and $\operatorname{Pr}\left\{p_{1}(x)=0 \mid \pi_{2}\right\}=0$, th:n every Bayes procedure is admissible.

Now let us prove the converse, namely, that every admissible procedure is a Bayes procedure. We assume ${ }^{\dagger}$

$$
\operatorname{Pr}\left\{\left.\frac{p_{1}(x)}{p_{2}(x)}=k \right\rvert\, \pi_{1}\right\}=0, \quad \quad i=1,2, \quad 0 \leq k \leq \infty .
$$

Then for any $q_{1}$ the Bayes procedure is unique. Moreover, the cdf of $p_{1}(x) / p_{2}(x)$ for $\pi_{1}$ and $\pi_{2}$ is continuous.

Let $R$ be an admissible procedure. Then there exists a $k$ such that

$$
\begin{aligned}
P(2 \mid 1, R) & =\operatorname{Pr}\left\{\left.\frac{p_{1}(\boldsymbol{x})}{p_{2}(\boldsymbol{x})} \leq k \right\rvert\, \pi_{1}\right\} \\
& =P\left(2 \mid 1, R^{*}\right)
\end{aligned}
$$

where $R^{*}$ is the Bayes procedure corresponding to $q_{2} / q_{1}=k$ [i.e., $q_{1}=1 /(1 +k)]$. Since $R$ is admissible, $P(1 \mid 2, R) \leq P\left(1 \mid 2, R^{*}\right)$. However, since by Theorem 6.3.2 $R^{*}$ is admissible, $P(1 \mid 2, R) \geq P\left(1 \mid 2, R^{*}\right)$; that is, $P(1 \mid 2, R)= P\left(1 \mid 2, R^{*}\right)$. Therefore, $R$ is also a Bayes procedure; by the uniqueness of Bayes procedures $R$ is the same as $R^{*}$.

Theorem 6.3.3. If (14) holds, then every admissible procedure is a Bayes procedure.

The proof of Theorem 6.3.3 shows that the ciass of Bayes procedures is complete. For if $R$ is any procedure outside the class, we construct a Bayes proccdure $R^{*}$ so that $P(2 \mid 1, R)=P\left(2 \mid 1, R^{*}\right)$. Then, since $R^{*}$ is admissible, $P(1 \mid 2, R) \geq P\left(1 \mid 2, R^{*}\right)$. Furthermore, the class of Bayes procedures is minimal complete since it is identical with the class of admissible procedures.
$p_{1}(x) / p_{2}(x)=x$ means $p_{2}(x)=0$.

Theorem 6.3.4. If (14) holds, the class of Bayes procedures is minimal complete.

Finally, let us consider the minimax procedure. Let $P\left(i \mid j, q_{1}\right)=P(i \mid j, R)$, where $R$ is the Bayes procedure corresponding to $q_{1} . P\left(i \mid j, q_{1}\right)$ is a continuous function of $q_{1} . P\left(2 \mid 1, q_{1}\right)$ varies from 1 to 0 as $q_{1}$ goes from 0 to 1 ; $P\left(1 \mid 2, q_{1}\right)$ varies from 0 to 1 . Thus there is a value of $q_{1}$, say $q_{1}^{*}$, such that $P\left(2 \mid 1, q_{1}^{*}\right)=P\left(1 \mid 2, q_{1}^{*}\right)$. This is the minimax solution, for if there were another procedure $R^{*}$ such that $\max \left\{P\left(2 \mid 1, R^{*}\right), P\left(1 \mid 2, R^{*}\right)\right\} \leq P\left(2 \mid 1, q_{1}^{*}\right)= P\left(1 \mid 2, q_{1}^{*}\right)$, that would contradict the fact that every Bayes solution is admissible.

### 6.4. CLASSIFICATION INTO ONE OF TWO KNOWN MULTIVARIATE NORMAL POPULATIONS

Now we slall use the general procedure outlined above in the case of two multivariate normal populations with equal covariance matrices, namely, $N\left(\boldsymbol{\mu}^{(1)}, \mathbf{\Sigma}\right)$ and $N\left(\boldsymbol{\mu}^{(2)}, \mathbf{\Sigma}\right)$, where $\boldsymbol{\mu}^{(1) \prime}=\left(\mu_{1}^{(i)}, \ldots, \mu_{p}^{(i)}\right)$ is the vector of means of the $i$ th population, $i=1,2$, and $\boldsymbol{\Sigma}$ is the matrix of variances and covariances of each population. [The approach was first used by Wald (1944).] Then the $i$ th density is

$$
p_{i}(\boldsymbol{x})=\frac{1}{(2 \pi)^{\frac{1}{2} p}|\boldsymbol{\Sigma}|^{\frac{1}{2}}} \exp \left[-\frac{1}{2}\left(\boldsymbol{x}-\boldsymbol{\mu}^{(i)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{x}-\boldsymbol{\mu}^{(i)}\right)\right] .
$$

The ratio of densities is

$$
\begin{aligned}
\frac{p_{1}(\boldsymbol{x})}{p_{2}(\boldsymbol{x})}= & \frac{\exp \left[-\frac{1}{2}\left(\boldsymbol{x}-\boldsymbol{\mu}^{(1)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{x}-\boldsymbol{\mu}^{(1)}\right)\right]}{\exp \left[-\frac{1}{2}\left(\boldsymbol{x}-\boldsymbol{\mu}^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{x}-\boldsymbol{\mu}^{(2)}\right)\right]} \\
= & \exp \left\{-\frac{1}{2}\left[\left(\boldsymbol{x}-\boldsymbol{\mu}^{(1)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{x}-\boldsymbol{\mu}^{(1)}\right)\right.\right. \\
& \left.\left.-\left(\boldsymbol{x}-\boldsymbol{\mu}^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{x}-\boldsymbol{\mu}^{(2)}\right)\right]\right\} .
\end{aligned}
$$

The region of classification into $\pi_{1}, R_{1}$, is the set of $x$ 's for which (2) is greater than or equal to $k$ (for $k$ suitably chosen). Since the logarithmic function is monotonically increasing, the inequality can be written in terms of the logarithm of (2) as

$$
-\frac{1}{2}\left[\left(. x-\mu^{(1)}\right)^{\prime} \mathbf{\Sigma}^{-1}\left(\boldsymbol{x}-\mu^{(1)}\right)-\left(\boldsymbol{x}-\mu^{(2)}\right)^{\prime} \mathbf{\Sigma}^{-1}\left(\boldsymbol{x}-\mu^{(2)}\right)\right] \geq \log k .
$$

The left-hand side of (3) can be expanded as

$$
\begin{aligned}
-\frac{1}{2}\left[x^{\prime} \Sigma^{-1} x-x^{\prime} \Sigma^{-1} \mu^{(1)}-\mu^{(1) \prime} \Sigma^{-1} x-\mu^{(1) \prime} \Sigma^{-1} \mu^{(1)}\right. & \\
& \left.-x^{\prime} \Sigma^{-1} x+x^{\prime} \Sigma^{-1} \mu^{(2)}+\mu^{(2) \prime} \Sigma^{-1} x-\mu^{(2) \prime} \Sigma^{-1} \mu^{(2)}\right] .
\end{aligned}
$$

By rearrangement of the terms we obtain

$$
\boldsymbol{x}^{\prime} \boldsymbol{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)-\frac{1}{2}\left(\mu^{(1)}+\mu^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right) .
$$

The first term is the well-known discriminant function. It is a function of the components of the observation vector.

The following theorem is now a direct consequence of Theorem 6.3.1.
Theorem 6.4.1. If $\pi_{i}$ has the density (1), $i=1,2$, the best regions of classification are given by

$$
\begin{aligned}
& R_{1}: \boldsymbol{x}^{\prime} \boldsymbol{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)-\frac{1}{2}\left(\mu^{(1)}+\mu^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right) \geq \log k, \\
& R_{2}: \boldsymbol{x}^{\prime} \boldsymbol{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)-\frac{1}{2}\left(\mu^{(1)}+\mu^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)<\log k .
\end{aligned}
$$

If a priori probabilities $q_{1}$ and $q_{2}$ are known, then $k$ is given by

$$
k=\frac{q_{2} C(1 \mid 2)}{q_{1} C(2 \mid 1)}
$$

In the particular case of the two populations being equally likely and the costs being equal, $k=1$ and $\log k=0$. Then the region of classification into $\pi_{1}$ is

$$
R_{1}: \boldsymbol{x}^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right) \geq \frac{1}{2}\left(\boldsymbol{\mu}^{(1)}+\boldsymbol{\mu}^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right) .
$$

If we dc not have a priori probabilities, we may select $\log k=c$, say, on the basis of making the expected losses due to misclassification equal. Let $\boldsymbol{X}$ be a ranoom observation. Then we wish to find the distribution of

$$
U=\boldsymbol{X}^{\prime} \boldsymbol{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)-\frac{1}{2}\left(\mu^{(1)}+\mu^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)
$$

on the assamption that $X$ is distributed according to $N\left(\boldsymbol{\mu}^{(1)}, \mathbf{\Sigma}\right)$ and then on the assumption that $X$ is distributed according to $N\left(\mu^{(2)}, \Sigma\right)$. When $X$ is distributed according to $N\left(\boldsymbol{\mu}^{\boldsymbol{(} \mathbf{I})}, \mathbf{\Sigma}\right), U$ is normally distributed with mean

$$
\begin{aligned}
\mathscr{E}_{1} U & =\mu^{(1) \prime} \mathbf{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)-\frac{1}{2}\left(\mu^{(1)}+\mu^{(2)}\right)^{\prime} \mathbf{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right) \\
& =\frac{1}{2}\left(\mu^{(1)}-\mu^{(2)}\right)^{\prime} \mathbf{\Sigma}^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)
\end{aligned}
$$

and variance

$$
\begin{aligned}
\operatorname{Var}_{1}(U) & =\mathscr{E}_{1}\left(\mu^{(1)}-\mu^{(2)}\right)^{\prime} \Sigma^{-1}\left(X-\mu^{(1)}\right)\left(X-\mu^{(1)}\right)^{\prime} \Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right) \\
& =\left(\mu^{(1)}-\mu^{(2)}\right)^{\prime} \Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)
\end{aligned}
$$

The Mahalanobis squared distance between $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)$ and $N\left(\boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}\right)$ is

$$
\left(\mu^{(1)}-\mu^{(2)}\right)^{\prime} \Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)=\Delta^{2},
$$

say. Then $U$ is distributed according to $N\left(\frac{1}{2} \Delta^{2}, \Delta^{2}\right)$ if $X$ is distributed according to $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)$. If $\boldsymbol{X}$ is distributed according to $N\left(\boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}\right)$, then

$$
\begin{aligned}
\mathscr{E}_{2} U & =\mu^{(2) \prime} \Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)-\frac{1}{2}\left(\mu^{(1)}+\mu^{(2)}\right)^{\prime} \Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right) \\
& =\frac{1}{2}\left(\mu^{(2)}-\mu^{(1)}\right)^{\prime} \Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right) \\
& =-\frac{1}{2} \Delta^{2} .
\end{aligned}
$$

The variance is the same as when $X$ is distributed according to $N\left(\mu^{(1)} . \Sigma\right)$ because it depends only on the second-order moments of $X$. Thus $U$ is distributed according to $N\left(-\frac{1}{2} \Delta^{2}, \Delta^{2}\right)$.

The probability of misclassification if the observation is from $\pi_{1}$ is

$$
P(2 \mid 1)=\int_{-\infty}^{c} \frac{1}{\sqrt{2 \pi} \Delta} e^{-\frac{1}{2}\left(z-\frac{1}{2} \Delta^{2}\right)^{2} / \Delta^{2}} d z=\int_{-\infty}^{\left(c-\frac{1}{2} \Delta^{2}\right) / \Delta} \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2^{2}}} d y
$$

and the probability of misclassification if the observation is from $\pi_{2}$ is

$$
P(1 \mid 2)=\int_{c}^{\infty} \frac{1}{\sqrt{2 \pi} \Delta} e^{-\frac{1}{2}\left(z+\frac{1}{2} \Delta^{2}\right)^{2} \Delta} d z \approx \int_{\left(c+\frac{1}{2} \Delta^{2}\right) / \Delta}^{\infty} \frac{1}{\sqrt{2 \pi}} e^{\cdot \frac{1}{2} y^{2}} d y
$$

Figure 6.1 indicates the two probabilities as the shaded portions in the tails

![](https://cdn.mathpix.com/cropped/99f89cca-f7e9-4df9-9a73-74ddc8f77122-235.jpg?height=306&width=1108&top_left_y=2016&top_left_x=295)
Figure 6.1

For the minimax solution we choose $c$ so that

$$
C(1 \mid 2) \int_{\left(c+\frac{\dot{L}}{\dot{Z}} \Delta^{2}\right) / \Delta}^{\infty} \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{3} y^{2}} d y=C(2 \mid 1) \int_{-\infty}^{\left(1-\frac{1}{2} \Delta^{2}\right) / \Delta} \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} y^{2}} d y
$$

Theorem 6.4.2. If the $\pi_{1}$ have densities (1), $i=1,2$, the minimax regions of classification are given by (6) where $c=\log k$ is chosen by the condition (16) with $C(i \mid j)$ the two costs of misclassification.

It should be noted that if the costs of misclassification are equal, $c=0$ and the probability of misclassification is

$$
\int_{1 / 2}^{\infty} \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} y^{2}} d y
$$

In case the costs of misclassification are unequal, $c$ could be determined to sufficient accuracy by a trial-and-error method with the normal tables.

Both terms in (5) involve the vector

$$
\delta=\Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right) .
$$

This is obtained as the solution of

$$
\Sigma \delta=\left(\mu^{(1)}-\mu^{(2)}\right)
$$

by an efficient computing method. The discriminant function $\boldsymbol{x}^{\prime} \boldsymbol{\delta}$ is the linear function that maximizes

$$
\frac{\left[\mathscr{E}_{1}\left(X^{\prime} d\right)-\mathscr{E}_{2}\left(X^{\prime} d\right)\right]^{2}}{\operatorname{Var}\left(X^{\prime} d\right)}
$$

for all choices of $\boldsymbol{d}$. The numerator of (20) is

$$
\left[\mu^{(1) \prime} d-\mu^{(2) \prime} d\right]^{2}=d^{\prime}\left[\left(\mu^{(1)}-\mu^{(2)}\right)\left(\mu^{(1)}-\mu^{(2)}\right)^{\prime}\right] d ;
$$

the denominator is

$$
d^{\prime} \mathscr{E}(X-\mathscr{E} X)(X-\mathscr{E} X)^{\prime} d=d^{\prime} \Sigma d
$$

We wish to maximize (21) with respect to $d$, holding (22) constant. If $\lambda$ is a Lagrange multiplicr, we ask for the maximum of

$$
\boldsymbol{d}^{\prime}\left[\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)^{\prime}\right] \boldsymbol{d}-\lambda\left(\boldsymbol{d}^{\prime} \mathbf{\Sigma} \boldsymbol{d}-1\right) .
$$

The derivatives of (23) with respect to the components of $\boldsymbol{d}$ are set equal to zero to obtain

$$
2\left[\left(\mu^{(1)}-\mu^{(2)}\right)\left(\mu^{(1)}-\mu^{(2)}\right)^{\prime}\right] d=2 \lambda \Sigma d .
$$

Since $\left(\boldsymbol{\mu}^{\boldsymbol{(} \mathbf{1} \boldsymbol{)}}-\boldsymbol{\mu}^{(2)}\right)^{\prime} \boldsymbol{d}$ is a scalar, say $\boldsymbol{\nu}$, we can write (24) as

$$
\mu^{(1)}-\mu^{(2)}=\frac{\lambda}{\nu} \Sigma d .
$$

Thus the solution is proportional to $\delta$.
We may finally note that if we have a sample of $N$ from either $\pi_{1}$ or $\pi_{2}$, we use the mean of the sample and classify it as from $N\left[\mu^{(1)},(1 / N) \Sigma\right]$ or $N\left[\boldsymbol{\mu}^{(2)},(1 / N) \boldsymbol{\Sigma}\right]$.

### 6.5. CLASSIFICATION INTO ONE OF TWO MULTIVARIATE NORMAL POPULATIONS WHEN THE PARAMETERS ARE ESTIMATED

### 6.5.1 The Criterion of Clas sification

Thus far we have assumed that the two populations are known exactly, In most applications of this theory the populations are not known, but must be inferred from samples, one from each population. We shall now treat the case in which we have a sample from each of two normal populations and we wish to use that information in classifying another observation as coming from one of the two populations.

Suppose that we have a sample $x_{1}^{(1)}, \ldots, x_{N_{1}}^{(1)}$ from $N\left(\mu^{(1)}, \Sigma\right)$ and a sample $x_{1}^{(2)}, \ldots, x_{\Lambda_{2}}^{(2)}$ from $N\left(\mu^{(2)}, \Sigma\right)$. In one terminology these are "training samples." On the basis of this information we wish to classify the observation $x$ as coming from $\pi_{1}$ to $\pi_{2}$. Clearly, our best estimate of $\boldsymbol{\mu}^{(1)}$ is $\overline{\boldsymbol{x}}^{(1)}=\sum_{1}^{N_{1}} \boldsymbol{x}_{\alpha}^{(1)} / N_{1}$, of $\boldsymbol{\mu}^{(2)}$ is $\overline{\boldsymbol{x}}^{(2)}=\sum_{1}^{N_{2}} \boldsymbol{x}_{\alpha}^{(2)} / N_{2}$, and of $\boldsymbol{\Sigma}$ is $\boldsymbol{S}$ defined by

$$
\begin{aligned}
\left(N_{1}+N_{2}-2\right) S= & \sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(1)}-\bar{x}^{(1)}\right)\left(x_{\alpha}^{(1)}-\bar{x}^{(1)}\right)^{\prime} \\
& +\sum_{\alpha=1}^{N_{2}}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)^{\prime}
\end{aligned}
$$

We substitute these estimates for the parameters in (5) of Section 6.4 to obtain

$$
W(x)=x^{\prime} S^{-1}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)-\frac{1}{2}\left(\bar{x}^{(1)}+\bar{x}^{(2)}\right)^{\prime} S^{-1}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right) .
$$

The first term of (2) is the discriminant function based on two samples [suggested by Fisher (1936)]. It is the linear function that has greatest variance between samples relative to the variance within samples (Problem 6.12). We propose that (2) be used as the criterion of classification in the same way that (5) of Section 6.4 is used.

When the populations are known, we can argue that the classification criterion is the best in the sense that its use minimizes the expected loss in the case of known a priori probabilities and generates the class of admissible procedures when a priori probabilities are not known. We cannot justify the use of (2) in the same way. However, it seems intuitively reasonable that (2) should give good results. Another criterion is indicated in Section 6.5.5.

Suppose we have a sample $x_{1}, \ldots, x_{N}$ from either $\pi_{1}$ or $\pi_{2}$, and we wish to classify the sample as a whole. Then we define $S$ by

$$
\begin{aligned}
\left(N_{1}+N_{2}+N\right. & -3) S=\sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(1)}-\bar{x}^{(1)}\right)\left(x_{\alpha}^{(1)}-\bar{x}^{(1)}\right)^{\prime} \\
& +\sum_{\alpha=1}^{N_{2}}\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)\left(x_{\alpha}^{(2)}-\bar{x}^{(2)}\right)^{\prime}-\sum_{\alpha=1}^{N}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime},
\end{aligned}
$$

where

$$
\bar{x}=\frac{1}{N} \sum_{\alpha=1}^{N} x_{\kappa}
$$

Then the criterion is

$$
\left[\bar{x}-\frac{1}{2}\left(\bar{x}^{(1)}+\bar{x}^{(2)}\right)\right]^{\prime} S^{-1}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right) .
$$

The larger $N$ is, the smaller are the probabilities of misclassification.

### 6.5.2. On the Distribution of the Criterion

Let

$$
\begin{aligned}
W & =X^{\prime} S^{-1}\left(\bar{X}^{(1)}-\bar{X}^{(2)}\right)-\frac{1}{2}\left(\bar{X}^{(1)}+\bar{X}^{(2)}\right)^{\prime} S^{-1}\left(\bar{X}^{(1)}-\bar{X}^{(2)}\right) \\
& =\left[X-\frac{1}{2}\left(\bar{X}^{(1)}+\bar{X}^{(2)}\right)\right] S^{-1}\left(\bar{X}^{(1)}-\bar{X}^{(2)}\right)
\end{aligned}
$$

for random $\boldsymbol{X}, \overline{\boldsymbol{X}}^{(1)}, \overline{\boldsymbol{X}}^{(2)}$, and $\boldsymbol{S}$.

The distribution of $W$ is extremely complicated. It depends on the sample sizes and the unknown $\Delta^{2}$. Let

$$
\begin{aligned}
& \boldsymbol{Y}_{1}=c_{1}\left[\boldsymbol{X}-\left(N_{1}+N_{2}\right)^{-1}\left(N_{1} \bar{X}^{(1)}+N_{2} \bar{X}^{(2)}\right)\right], \\
& \boldsymbol{Y}_{2}=c_{2}\left(\bar{X}^{(1)}-\bar{X}^{(2)}\right),
\end{aligned}
$$

where $c_{1}=\sqrt{\left(N_{1}+N_{2}\right) /\left(N_{1}+N_{2}+1\right)}$ and $c_{2}=\sqrt{N_{1} N_{2} /\left(N_{1}+N_{2}\right)}$. Then $Y_{1}$ and $Y_{2}$ are independently normally distributed with covariance matrix $\mathbf{\Sigma}$. The expected value of $\boldsymbol{Y}_{2}$ is $\boldsymbol{c}_{2}\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)$, and the expected value of $\boldsymbol{Y}_{1}$ is $c_{1}\left[N_{2} /\left(N_{1}+N_{2}\right)\right]\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)$ if $\boldsymbol{X}$ is from $\pi_{1}$ and $-c_{1}\left[N_{1} /\left(N_{1}+N_{2}\right)\right]\left(\boldsymbol{\mu}^{(1)}-\right. \left.\boldsymbol{\mu}^{(2)}\right)$ if $\boldsymbol{X}$ is from $\pi_{2}$. Let $\boldsymbol{Y}=\left(\boldsymbol{Y}_{1} \boldsymbol{Y}_{2}\right)$ and

$$
\boldsymbol{M}=\boldsymbol{Y}^{\prime} \boldsymbol{S}^{-1} \boldsymbol{Y}=\left(\begin{array}{ll}
m_{11} & m_{12} \\
m_{21} & m_{22}
\end{array}\right) .
$$

Then

$$
W=\sqrt{\frac{N_{1}+N_{2}+1}{N_{1} N_{2}}} m_{12}+\frac{N_{1}-N_{2}}{2 N_{1} N_{2}} m_{22} .
$$

The density of $M$ has been given by Sitgreaves (1952). Anderson (1951a) and Wald (1944) have also studied the distribution of $W$.

If $N_{1}=N_{2}$, the distribution of $W$ for $X$ from $\pi_{1}$ is the same as that of $-W$ for $X$ from $\pi_{2}$. Thus, if $W \geq 0$ is the region of classification as $\pi_{1}$, then the probability of misclassifying $X$ when it is from $\pi_{1}$ is equal to the probability of misclassifying it when it is from $\pi_{2}$.

### 6.5.3 The Asymptotic Distribution of the Criterion

In the case of large samples from $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)$ and $N\left(\boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}\right)$, we can apply limiting distribution theory. Since $\bar{X}^{(1)}$ is the mean of a sample of $N_{1}$ independent observations from $N\left(\boldsymbol{\mu}^{(1)}, \mathbf{\Sigma}\right)$, we know that

$$
\operatorname{plim}_{N_{1} \rightarrow \infty} \overline{\boldsymbol{X}}^{(1)}=\boldsymbol{\mu}^{(1)} .
$$

The explicit definition of (11) is as follows: Given arbitrary positive $\delta$ and $\varepsilon$. we can find $N$ large enough so that for $N_{1} \geq N$

$$
\operatorname{Pr}\left(\left|\bar{X}_{i}^{(1)}-\mu_{i}^{(1)}\right|<\delta, i=1, \ldots, p\right\}>1-\varepsilon .
$$

(See Problem 3.23.) This can be proved by using the Tchebycheff inequality. Similarly.

$$
\operatorname{plim}_{N_{2} \rightarrow \infty} \bar{X}^{(2)}=\mu^{(2)},
$$

and

$$
\operatorname{plim} S=\Sigma
$$

as $N_{1} \rightarrow x, N_{2} \rightarrow \infty$ or as both $N_{1}, N_{2} \rightarrow \infty$. From (14) we obtain

$$
\operatorname{plim} S^{-1}=\Sigma^{-1},
$$

since the probability limits of sums, differences, products, and quotients of random variables are the sums, differences, products, and quotients of their probability limits as long as the probability limit of each denominator is different from zero [Cramér (1946), p. 254]. Furthermore,

$$
\operatorname{plim}_{N_{1} . N_{2} \rightarrow \infty} S^{-1}\left(\bar{X}^{(1)}-\bar{X}^{(2)}\right)=\Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)
$$

It follows then that the limiting distribution of $W$ is the distribution of $U$. For sufficiently large samples from $\pi_{1}$ and $\pi_{2}$ we can use the criterion as if we knew the population exactly and make only a small error. [The result was first given by Wald (1944).]

Theorem 6.5.1. Let $W$ be given by (6) with $\bar{X}^{(1)}$ the mean of a sample of $N_{1}$ from $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right), \vec{X}^{(2)}$ the mean of a sample of $N_{2}$ from $N\left(\boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}\right)$, and $\mathbf{S}$ the estimate of $\Sigma$ based on the pooled sample. The limiting distribution of $W$ as $N_{1} \rightarrow \infty$ and $N_{2} \rightarrow \infty$ is $N\left(\frac{1}{2} \Delta^{2}, \Delta^{2}\right)$ if $X$ is distributed according to $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)$ and is $N\left(-\frac{1}{2} \Delta^{2}, \Delta^{2}\right)$ if $X$ is distributed according to $N\left(\boldsymbol{\mu}^{(2)}, \mathbf{\Sigma}\right)$.

### 6.5.4. Another Derivation of the Criterion

A convenient mnemonic derivation of the criterion is the use of regression of a dummy variate [given by Fisher (1936)]. Let

$$
y_{\alpha}^{(1)}=\frac{N_{2}}{N_{1}+N_{2}}, \quad \alpha=1, \ldots, N_{1}, \quad y_{\alpha}^{(2)}=\frac{-N_{1}}{N_{1}+N_{2}}, \quad \alpha=1, \ldots, N_{2} .
$$



Then formally find the regression on the variates $x_{\alpha}^{(i)}$ by choosing $b$ to minimize

$$
\sum_{i=1}^{2} \sum_{\alpha=1}^{N_{i}}\left[y_{\alpha}^{(1)}-b^{\prime}\left(x_{\alpha}^{(i)}-\bar{x}\right)\right]^{2},
$$

where

$$
\bar{x}=\frac{N_{\mathrm{I}} \bar{x}^{(\mathrm{I})}+N_{2} \bar{x}^{(2)}}{\bar{N}_{\mathrm{I}}+\bar{N}_{2}} .
$$

The normal equations are

$$
\begin{aligned}
\sum_{i=\mathrm{I}}^{2} \sum_{\alpha=1}^{N_{i}}\left(x_{\alpha}^{(i)}-\bar{x}\right)\left(x_{\alpha}^{(i)}-\bar{x}\right)^{\prime} b & =\sum_{i=1}^{2} \sum_{\alpha=1}^{N_{i}} y_{\alpha}^{(i)}\left(x_{\alpha}^{(1)}-\bar{x}\right) \\
& =\frac{N_{1} N_{2}}{N_{1}+N_{2}}\left[\left(\bar{x}^{(1)}-\vec{x}\right)-\left(\bar{x}^{(2)}-\bar{x}\right)\right] \\
& =\frac{N_{1} N_{2}}{N_{1}+N_{2}}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right) .
\end{aligned}
$$

The matrix multiplying $b$ can be written as

$$
\begin{aligned}
& \sum_{i=1}^{2} \sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(i)}-\bar{x}\right)\left(\bar{x}_{\alpha}^{(i)}-\bar{x}\right)^{\prime} \\
&= \sum_{i=1}^{2} \sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(1)}-\bar{x}^{(i)}\right)\left(x_{\alpha}^{(i)}-\bar{x}^{(i)}\right)^{\prime} \\
&+N_{1}\left(\bar{x}^{(1)}-\bar{x}\right)\left(\bar{x}^{(1)}-\bar{x}\right)^{\prime}+N_{2}\left(\bar{x}^{(2)}-\bar{x}\right)\left(\bar{x}^{(2)}-\bar{x}\right)^{\prime} \\
&= \sum_{i=1}^{2} \sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(i)}-\bar{x}^{(i)}\right)\left(x_{\alpha}^{(i)}-\bar{x}^{(1)}\right)^{\prime} \\
&+\frac{N_{1} N_{2}}{N_{1}+N_{2}}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)^{\prime} .
\end{aligned}
$$

Thus (21) can be written as

$$
A b=\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)\left[\frac{N_{1} N_{2}}{\bar{N}_{1}+\bar{N}_{2}}-\frac{\dot{N}_{1} N_{2}}{\bar{N}_{1}+\bar{N}_{2}}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)^{\prime} b\right],
$$

where

$$
A=\sum_{i=1}^{2} \sum_{\alpha=1}^{N_{l}}\left(x_{\alpha}^{(i)}-\bar{x}^{(i)}\right)\left(x_{\alpha}^{(i)}-\bar{x}^{(i)}\right)^{\prime}
$$

Since $\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)^{\prime} b$ is a scalar, we see that the solution $b$ of (23) is proportional to $S^{-1}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)$.

### 6.5.5. The Likelihood Ratio Criterion

Another criterion which can be used in classification is the likelihood ratio criterion. Consider testing the composite null hypothesis that $x, x_{1}^{(1)}, \ldots, x_{N_{1}}^{(1)}$ are drawn from $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)$ and $\boldsymbol{x}_{1}^{(2)}, \ldots, \boldsymbol{x}_{N_{2}}^{(2)}$ are drawn from $N\left(\boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}\right)$ against the composite alternative hypothesis that $x_{1}^{(1)}, \ldots, x_{N_{1}}^{(1)}$ are drewn from $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)$ and $x, x_{1}^{(2)}, \ldots, x_{N_{2}}^{(2)}$ are drawn from $N\left(\boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}\right)$, with $\boldsymbol{\mu}^{(1)}, \boldsymbol{\mu}^{(2)}$, and $\boldsymbol{\Sigma}$ unspecified. Under the first hypothesis the maximum likelihood estimators of $\boldsymbol{\mu}^{(1)}, \boldsymbol{\mu}^{(2)}$, and $\boldsymbol{\Sigma}$ are

$$
\begin{aligned}
& \hat{\boldsymbol{\mu}}_{1}^{(1)}=\frac{N_{1} \overline{\boldsymbol{x}}^{(1)}+\boldsymbol{x}}{N_{1}+1}, \\
& \hat{\boldsymbol{\mu}}_{1}^{(2)}=\overline{\boldsymbol{x}}^{(2)}, \\
& \hat{\boldsymbol{\Sigma}}_{1}=\frac{1}{N_{1}+N_{2}+1}\left[\sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(1)}-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)\left(x_{\alpha}^{(1)}-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)^{\prime}+\left(x-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)\left(x-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)^{\prime}\right. \\
& \left.+\sum_{\alpha=1}^{N_{2}}\left(x_{\alpha}^{(2)}-\hat{\boldsymbol{\mu}}_{1}^{(2)}\right)\left(x_{\alpha}^{(2)}-\hat{\boldsymbol{\mu}}_{1}^{(2)}\right)^{\prime}\right] .
\end{aligned}
$$

Since

$$
\begin{aligned}
\sum_{\alpha=1}^{N_{1}} & \left(x_{\alpha}^{(1)}-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)\left(x_{\alpha}^{(1)}-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)^{\prime}+\left(x-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)\left(x-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)^{\prime} \\
= & \sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)\left(x_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)^{\prime}+N_{1}\left(\overline{\boldsymbol{x}}^{(1)}-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)\left(\overline{\boldsymbol{x}}^{(1)}-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)^{\prime} \\
& +\left(x-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)\left(x-\hat{\boldsymbol{\mu}}_{1}^{(1)}\right)^{\prime} \\
= & \sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)\left(x_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)^{\prime}+\frac{N_{1}}{N_{1}+1}\left(x-\overline{\boldsymbol{x}}^{(1)}\right)\left(x-\overline{\boldsymbol{x}}^{(1)}\right)^{\prime}
\end{aligned}
$$

we can write $\hat{\mathbf{\Sigma}}_{\text {I }}$ as

$$
\hat{\mathbf{\Sigma}}_{1}=\frac{1}{N_{\mathrm{L}}+N_{2}+\overline{1}}\left[A+\frac{N}{N_{1}+1}\left(x-\bar{x}^{(1)}\right)\left(x-\bar{x}^{(1)}\right)^{\prime}\right],
$$

where $\boldsymbol{A}$ is given by (24). Under the assumptions of the alternative hypothesis we find (by considerations of symmetry) that the maximum likelihood estimators of the parameters are

$$
\begin{aligned}
& \hat{\boldsymbol{\mu}}_{2}^{(1)}=\overline{\boldsymbol{x}}^{(1)} \\
& \hat{\boldsymbol{\mu}}_{2}^{(2)}=\frac{N_{2} \overline{\boldsymbol{x}}^{(2)}+x}{N_{2}+1} \\
& \hat{\boldsymbol{\Sigma}}_{2}=\frac{1}{N_{1}+N_{2}+1}\left[A+\frac{N_{2}}{N_{2}+1}\left(x-\overline{\boldsymbol{x}}^{(2)}\right)\left(x-\overline{\boldsymbol{x}}^{(2)}\right)^{\prime}\right] .
\end{aligned}
$$

The likelihood ratio criterion is, therefore, the $\left(N_{1}+N_{2}+1\right) / 2$ th power of

$$
\frac{\left|\hat{\boldsymbol{\Sigma}}_{2}\right|}{\left|\hat{\boldsymbol{\Sigma}}_{1}\right|}=\frac{\left|A+\frac{N_{2}}{N_{2}+1}\left(x-\bar{x}^{(2)}\right)\left(x-\bar{x}^{(2)}\right)^{\prime}\right|}{\left|A+\frac{N_{1}}{N_{1}+1}\left(x-\bar{x}^{(1)}\right)\left(x-\bar{x}^{(1)}\right)^{\prime}\right|} .
$$

This ratio can also be written (Corollary A.3.1)

$$
\begin{aligned}
& \frac{1+\frac{N_{2}}{N_{2}+1}\left(x-\bar{x}^{(2)}\right)^{\prime} A^{-1}\left(x-\bar{x}^{(2)}\right)}{1+\frac{N_{1}}{N_{1}+1}\left(x-\bar{x}^{(1)}\right)^{\prime} A^{-1}\left(x-\bar{x}^{(1)}\right)} \\
& \quad=\frac{n+\frac{N_{2}}{N_{2}+1}\left(x-\bar{x}^{(2)}\right)^{\prime} S^{-1}\left(x-\bar{x}^{(2)}\right)}{n+\frac{N_{1}}{N_{1}+1}\left(x-\bar{x}^{(1)}\right)^{\prime} S^{-1}\left(x-\bar{x}^{(1)}\right)}
\end{aligned}
$$

where $n=N_{\mathrm{I}}+N_{2}-2$. The region of classification into $\pi_{1}$ consists of those points for which the ratio (30) is greater than or equal to a given number $K_{n}$. It can be written

$$
\begin{aligned}
R_{1}: & n+\frac{N_{2}}{N_{2}+1}\left(x-\bar{x}^{(2)}\right)^{\prime} S^{-1}\left(x-\bar{x}^{(2)}\right) \\
& \geq K_{n}\left[n+\frac{N_{1}}{N_{1}+1}\left(x-\bar{x}^{(1)}\right)^{\prime} S^{-1}\left(x-\bar{x}^{(1)}\right)\right]
\end{aligned}
$$

If $K_{n}=1+2 c / n$ and $N_{1}$ and $N_{2}$ are large, the region (31) is approximately $W(x) \geq c$.

If we take $K_{n}=1$, the rule is to classify as $\pi_{1}$ if (30) is greater than 1 and as $\pi_{2}$ if (30) is less than 1 . This is the maximum likelihood rule. Let

$$
\begin{aligned}
Z=\frac{1}{2}[ & \frac{N_{2}}{N_{2}+1}\left(x-\bar{x}^{(2)}\right)^{\prime} S^{-1}\left(x-\bar{x}^{(2)}\right) \\
& \left.-\frac{N_{\mathrm{I}}}{N_{\mathrm{I}}+1}\left(x-\bar{x}^{(\mathrm{I})}\right)^{\prime} S^{-1}\left(x-\bar{x}^{(\mathrm{I})}\right)\right] .
\end{aligned}
$$

Then the maximum likelihood rule is to classify as $\pi_{1}$ if $Z>0$ and $\pi_{2}$ if $Z<0$. Roughly speaking, assign $x$ to $\pi_{1}$ or $\pi_{2}$ according to whether the distance to $\overline{\boldsymbol{x}}^{(1)}$ is less or greater than the distance to $\overline{\boldsymbol{x}}^{(2)}$. The difference between $W$ and $Z$ is

$$
\begin{aligned}
W-Z=\frac{1}{2}[ & \frac{1}{N_{2}+1}\left(x-\bar{x}^{(2)}\right)^{\prime} S^{-1}\left(x-\bar{x}^{(2)}\right) \\
& \left.-\frac{1}{N_{1}+1}\left(x-\bar{x}^{(1)}\right)^{\prime} S^{-1}\left(x-\bar{x}^{(1)}\right)\right]
\end{aligned}
$$

which has the probability limit 0 as $N_{1}, N_{2} \rightarrow \infty$. The probabilities of misclassification with $W$ are equivalent asymptotically to those with $Z$ for large samples.

Note that for $N_{1}=N_{2}, Z=\left[N_{1} /\left(N_{1}+1\right)\right] W$. Then the symmetric test based on the cutoff $c=0$ is the same for $Z$ and $W$.

### 6.5.6. Invariance

The classification problem is invariant with respect to transformations

$$
\begin{array}{rlr}
x_{\alpha}^{(1) *} & =B x_{\alpha}^{(1)}+c, & \alpha=1, \ldots, N_{1}, \\
x_{\alpha}^{(2) *} & =B x_{\alpha}^{(2)}+c, & \alpha=1, \ldots, N_{2}, \\
x^{*} & =B x+c, &
\end{array}
$$

where $\boldsymbol{B}$ is nonsingular and $\boldsymbol{c}$ is a vector. This transformation induces the following transformation on the sufficient statistics:

$$
\begin{aligned}
\vec{x}^{(1) *} & =B \vec{x}^{(1)}+c, & \vec{x}^{(2) *} & =B \vec{x}^{(2)}+c, \\
x^{*} & =B x+c, & S^{*} & =B S B^{\prime}
\end{aligned}
$$

with the same transformations on the parameters, $\boldsymbol{\mu}^{(1)}, \boldsymbol{\mu}^{(2)}$, and $\boldsymbol{\Sigma}$. (Note that $\mathscr{E} x=\mu^{(1)}$ or $\mu^{(2)}$.) Any invariant of the parameters is a function of
$\Delta^{2}=\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)^{\prime} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)$. There exists a matrix $\boldsymbol{B}$ and a vector $\boldsymbol{c}$ such that

$$
\begin{aligned}
\boldsymbol{\mu}^{(1) *} & =\boldsymbol{B} \boldsymbol{\mu}^{(1)}+\boldsymbol{c}=\mathbf{0}, \quad \boldsymbol{\mu}^{(2) *}=\boldsymbol{B} \boldsymbol{\mu}^{(2)}+\boldsymbol{c}=(\Delta, 0, \ldots, 0)^{\prime} \\
\boldsymbol{\Sigma}^{*} & =\boldsymbol{B} \boldsymbol{\Sigma} \boldsymbol{B}^{\prime}=\boldsymbol{I} .
\end{aligned}
$$

Therefore, $\Delta^{2}$ is the minimal invariant of the parameters. The elements of $M$ defined by (9) are invariant and are the minimal invariants of the sufficient statistics. Thus invariant procedures depend on $M$, and the distribution of $M$ depends only on $\Delta^{2}$. The statistics $W$ and $Z$ are invariant.

### 6.6. PROBABILITIES OF MISCLASSIFICATION

### 6.6.1. Asymptotic Expansions of the Probabilities of Misclassification Using $\boldsymbol{W}$

We may want to know the probabilities of misclassification before we draw the two samples for determining the classification rule, and we may want to know the (conditional) probabili.ies of misclassification after drawing the samples. As observed earlier, the exact distributions of $W$ and $Z$ are very difficult to calculate. Therefore, we treat asymptotic expansions of their probabilities as $N_{1}$ and $N_{2}$ increase. The background is that the limiting distribution of $W$ and $Z$ is $N\left(\frac{1}{2} \Delta^{2}, \Delta^{2}\right)$ if $x$ is from $\pi_{1}$ and is $N\left(-\frac{1}{2} \Delta^{2}, \Delta^{2}\right)$ if $x$ is from $\pi_{2}$.

Okamoto (1963) obtained the asymptotic expansion of the distribution of $W$ to terms of order $n^{-2}$, and Siotani and Wang $(1975,1977)$ to terms of order $n^{-3}$. [Bowker and Sitgreaves (1961) treated the case of $N_{1}=N_{2}$.] Let $\Phi(\cdot)$ and $\phi(\cdot)$ be the cdf and density of $N(0,1)$, respectively.

Theorem 6.6.1. As $N_{1} \rightarrow \infty, N_{2} \rightarrow \infty$, and $N_{1} / N_{2} \rightarrow$ a positive limit ( $n= N_{1}+N_{2}-2$ ),

$$
\begin{aligned}
\operatorname{Pr}\{ & \left.\left.\frac{W-\frac{1}{2} \Delta^{2}}{\Delta} \leq u \right\rvert\, \pi_{\mathrm{I}}\right\} \\
& =\Phi(u)-\phi(u)\left\{\frac{1}{2 N_{\mathrm{I}} \Delta^{2}}\left[u^{3}+(p-3) u-p \Delta\right]\right. \\
& +\frac{1}{2 N_{2} \Delta^{2}}\left[u^{3}+2 \Delta u^{2}+\left(p-3+\Delta^{2}\right) u+(p-2) \Delta\right] \\
& \left.+\frac{1}{4 n}\left[4 u^{3}+4 \Delta u^{2}+\left(6 p-6+\Delta^{2}\right) u+2(p-1) \Delta\right]\right\}+O\left(n^{-2}\right)
\end{aligned}
$$

and $\operatorname{Pr}\left\{\left.-\left(W+\frac{1}{2} \Delta^{2}\right) / \Delta \leq u \right\rvert\, \pi_{2}\right\}$ is (1) with $N_{1}$ and $N_{2}$ interchanged.

The rule using $W$ is to assign the observation $x$ to $\pi_{\mathrm{I}}$ if $W(x)>c$ and to $\pi_{2}$ if $W(x) \leq c$. The probabilities of misclassification are given by Theorem 6.6 .1 with $u=\left(c-\frac{1}{2} \Delta^{2}\right) / \Delta$ and $u=-\left(c+\frac{1}{2} \Delta^{2}\right) / \Delta$, respectively. For $c=0$, $u=-\frac{1}{2} \Delta$. If $N_{1}=N_{2}$, this defines an exact minimax procedure [Das Gupta (1965)].

## Corollary 6.6.1

$$
\begin{aligned}
\operatorname{Pr}\{W & \left.\leq 0 \mid \pi_{\mathrm{I}}, \lim _{n \rightarrow \infty} \frac{N_{\mathrm{I}}}{N_{2}}=1\right\} \\
& =\Phi\left(-\frac{\mathrm{I}}{2} \Delta\right)+\frac{1}{n} \phi\left(\frac{\mathrm{I}}{2} \Delta\right)\left[\frac{p-1}{\Delta}+\frac{p}{4} \Delta\right]+o\left(n^{-\mathrm{I}}\right) \\
& =\operatorname{Pr}\left\{W \geq 0 \mid \pi_{2}, \lim _{n \rightarrow \infty} \frac{N_{\mathrm{I}}}{N_{2}}=1\right\} .
\end{aligned}
$$

Note that the correction term is positive, as far as this correction goes; that is, the probability of misclassification is greater than the value of the normal approximation. The correction term (to order $n^{-1}$ ) increases with $p$ for given $\Delta$ and decreases with $\Delta$ for given $p$.

Since $\Delta$ is usually unknown, it is relevant to Studentize $W$. The sample Mahalanobis squared distance

$$
D^{2}=\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)^{\prime} S^{-1}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)
$$

is an estimator of the population Mahalanobis squared distance $\Delta^{2}$. The expectation of $D^{2}$ is

$$
\mathscr{E} D^{2}=\frac{n}{n-p-1}\left[\Delta^{2}+p\left(\frac{1}{N_{\mathrm{I}}}+\frac{1}{N_{2}}\right)\right] .
$$

See Problem 6.14. If $N_{1}$ and $N_{2}$ are large, this is approximately $\Delta^{2}$.
Anderson (1973b) showed the following:
Theorem 6.6.2. If $N_{1} / N_{2} \rightarrow a$ positive limit as $n \rightarrow \infty$,

$$
\begin{aligned}
& \operatorname{Pr}\left\{\left.\frac{W-\frac{1}{2} D^{2}}{D} \leq u \right\rvert\, \pi_{\mathrm{I}}\right\} \\
& =\boldsymbol{\Phi}(u)-\phi(u)\left\{\frac{1}{N_{\mathrm{I}}}\left(\frac{u}{2}-\frac{p-1}{\Delta}\right)+\frac{1}{n}\left[\frac{u^{3}}{4}+\left(p-\frac{3}{4}\right) u\right]\right\}+O\left(n^{-2}\right),
\end{aligned}
$$

(6) $\quad \operatorname{Pr}\left\{\left.-\frac{W+\frac{1}{2} D^{2}}{D} \leq u \right\rvert\, \pi_{2}\right\}$

$$
=\Phi(u)-\phi(u)\left\{\frac{1}{N_{2}}\left(\frac{u}{2}-\frac{p-1}{\Delta}\right)+\frac{1}{n}\left[\frac{u^{3}}{4}+\left(p-\frac{3}{4}\right) u\right]\right\}+O\left(n^{-2}\right)
$$

Usually, one is interested in $u \leq 0$ (small probabilities of error). Then the correction term is positive; that is, the normal approximation underestimates the probability of misclassification.

One may want to choose the cutoff point $c$ so that one probability of misclassification is controlled. Let $\alpha$ be the desired $\operatorname{Pr}\left\{W<c \mid \pi_{1}\right\}$. Anderson (1973b, 1973c) derived the following theorem:

Theorem 6.6.3. Let $u_{0}$ be such that $\Phi\left(u_{0}\right)=\alpha$, and ler

$$
u=u_{0}-\frac{1}{N_{\mathrm{I}}}\left[\frac{p-1}{D}-\frac{1}{2} u_{0}\right]+\frac{1}{n}\left[\left(p-\frac{3}{4}\right) u_{0}+\frac{1}{4} u_{11}^{3}\right] .
$$

Then as $N_{1} \rightarrow \infty, N_{2} \rightarrow \infty$, and $N_{1} / N_{2} \rightarrow a$ positive limit,

$$
\operatorname{Pr}\left\{\left.\frac{W-\frac{1}{2} D^{2}}{D} \leq u \right\rvert\, \pi_{1}\right\}=\alpha+O\left(n^{-2}\right)
$$

Then $c=D u+\frac{1}{2} D^{2}$ will attain the desired probability $\alpha$ to within $O\left(n^{-2}\right)$.
We now turn to evaluating the probabilities of misclassification after the two samples have been drawn. Conditional on $\bar{x}^{(1)}, \bar{x}^{(2)}$, and $S$, the random variable $W$ is normally distributed with conditional mean

$$
\begin{aligned}
\mathscr{E}\left(W \mid \pi_{1}, \bar{x}^{(1)}, \bar{x}^{(2)}, S\right) & =\left[\mu^{(1)}-\frac{1}{2}\left(\bar{x}^{(1)}+\bar{x}^{(2)}\right)\right]^{\prime} S^{-1}\left(\bar{x}^{(1)}-\bar{x}^{(-1)}\right) \\
& =\mu^{(1)}\left(\bar{x}^{(1)}, \bar{x}^{(2)}, S\right)
\end{aligned}
$$

when $x$ is from $\pi_{1}, i=1,2$, and conditional variance

$$
\begin{aligned}
\mathscr{V}\left(W \mid \bar{x}^{(1)}, \bar{x}^{(2)}, S\right) & =\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)^{\prime} S^{-1} \Sigma S^{-1}\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right) \\
& =\sigma^{2}\left(\bar{x}^{(1)}, \bar{x}^{(2)}, S\right) .
\end{aligned}
$$

Note that these means and variance are functions of the samples with probability limits

$$
\begin{aligned}
& \operatorname{plim}_{N_{1}, N_{2} \rightarrow \infty} \mu^{(i)}\left(\bar{x}^{(1)}, \bar{x}^{(2)}, S\right)=(-1)^{1-1} \frac{1}{2} \Delta^{2} \\
& \operatorname{plim}_{N_{1}, N_{2} \rightarrow \infty} \sigma^{2}\left(\bar{x}^{(1)}, \bar{x}^{(2)}, S\right)=\Delta^{2}
\end{aligned}
$$

For large $N_{1}$ and $N_{2}$ the conditional probabilities of misclassification are close to the limiting normal probabilities (with high probability relative to $\bar{x}^{(1)}, \bar{x}^{(2)}$. and $S$ ).

When $c$ is the cutoff point, probabilities of misclassification conditional on $\bar{x}^{(1)}, \bar{x}^{(2)}$, and $S$ are

$$
\begin{aligned}
& P\left(2 \mid 1, c, \bar{x}^{(1)}, \bar{x}^{(2)}, S\right)=\Phi\left[\frac{c-\mu^{(1)}\left(\bar{x}^{(1)}, \bar{x}^{(2)}, S\right)}{\sigma\left(\bar{x}^{(1)}, \bar{x}^{(2)}, S\right)}\right], \\
& P\left(1 \mid 2, c, \bar{x}^{(1)}, \bar{x}^{(2)}, S\right)=1-\Phi\left[\frac{c-\mu^{(2)}\left(\bar{x}^{(1)}, \bar{x}^{(2)}, S\right)}{\sigma\left(\bar{x}^{(1)}, \bar{x}^{(2)}, S\right)}\right] .
\end{aligned}
$$

In (12) write $c$ as $D u_{1}+\frac{1}{2} D^{2}$. Then the argument of $\Phi(\cdot)$ in (12) is $u_{1} D / \sigma+\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)^{\prime} S^{-1}\left(\bar{x}^{(1)}-\mu^{(1)}\right) / \sigma$; the first term converges in probability to $u_{1}$, the second term tends to 0 as $N_{1} \rightarrow \infty, N_{2} \rightarrow \infty$, and (12) to $\Phi\left(u_{1}\right)$. In (13) write $c$ as $D u_{2}-\frac{1}{2} D^{2}$. Then the argument of $\Phi(\cdot)$ in (13) is $u_{2} D / \sigma+\left(\bar{x}^{(1)}-\bar{x}^{(2)}\right)^{\prime} S^{-1}\left(\bar{x}^{(2)}-\mu^{(2)}\right) / \sigma$. The first term converges in probability to $u_{2}$ and the second term to 0 ; (13) converges to $1-\Phi\left(u_{2}\right)$.

For given $\bar{x}^{(1)}, \bar{x}^{(2)}$, and $S$ the (conditional) probabilities of misclassification (12) and (13) are functions of the parameters $\boldsymbol{\mu}^{(1)}, \boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}$ and can be estimated. Consider them when $c=0$. Then (12) and (13) converge in probability to $\Phi\left(-\frac{1}{2} \Delta\right)$; that suggests $\Phi\left(-\frac{1}{2} D\right)$ as an estimator of (12) and (13). A better estimator is $\Phi\left(-\frac{1}{2} \bar{D}\right)$, where $\bar{D}^{2}=(n-p-1) D^{2} / n$, which is closer to being an unbiased estimator of $\Delta^{2}$. [See (4).] McLachlan (1973, 1974a, 1974b, 1974c) gave an estimator of (12) whose bias is of order $n^{-2}$ : it is

$$
\Phi\left(-\frac{1}{2} D\right)+\phi\left(\frac{1}{2} D\right)\left\{\frac{p-D}{N_{1} D}+\frac{1}{32 n}\left[-D^{3}+4(4 p-1) D\right]\right\} .
$$

[McLachlan gave (14) to terms of order $n^{-1}$.] McLachlan explored the properties of these and other estimators, as did Lachenbruch and Mickey (1968).

Now consider (12) with $c=D u_{1}+\frac{1}{2} D^{2} ; u_{1}$ might be chosen to control $P(2 \mid 1)$ conditional on $\overline{\boldsymbol{x}}^{(1)}, \overline{\boldsymbol{x}}^{(2)}, S$. This conditional probability as a function of $\bar{x}^{(1)}, \bar{x}^{(2)}, S$ is a random variable whose distribution may be approximated. McLachlan showed the following:

Theorem 6.6.4. As $N_{1} \rightarrow \infty, N_{2} \rightarrow \infty$, and $N_{1} / N_{2} \rightarrow a$ positive limit,

$$
\begin{aligned}
\operatorname{Pr}\{ & \sqrt{n} \\
& \left.\frac{P\left(2 \mid 1, D u_{1}+\frac{1}{2} D^{2}, \bar{x}^{(1)}, \bar{x}^{(2)}, S\right)-\Phi\left(u_{1}\right)}{\phi\left(u_{2}\right)\left[\frac{1}{2} u_{1}^{2}+n / N_{1}\right]^{\frac{1}{3}}} \leq x\right\} \\
& =\Phi\left[x-\frac{(p-1) n / N_{1}-\left(p-\frac{3}{4}+n / N_{1}\right) u_{1}-u_{1}^{3} / 4}{\sqrt{n}\left[\frac{1}{2} u_{1}^{2}+n / N_{1}\right]^{\frac{1}{4}}}\right]+O\left(n^{-2}\right) .
\end{aligned}
$$

McLachlan (1977) gave a method of selecting $u_{1}$ so that the probability of one misclassification is less than a preassigned $\delta$ with a preassigned confidence level $1-\varepsilon$.

### 6.6.2. Asymptotic Expansions of the Probabilities of Misclassification Using $Z$

We now turn our attention to $Z$ defined by (32) of Section 6.5. The results are parallel to those for $W$. Memon and Okamoto (1971) expanded the distribution of $Z$ to terms of order $n^{-2}$, and Siotani and Wang (1975), (1977) to terms of order $n^{-3}$.

Theorem 6.6.5. As $N_{1} \rightarrow \infty, N_{2} \rightarrow \infty$, and $N_{1} / N_{2}$ approaches a positive limit ,

$$
\begin{aligned}
\operatorname{Pr}\{ & \left.\left.\frac{Z-\frac{1}{2} \Delta^{2}}{\Delta} \leq u \right\rvert\, \pi_{1}\right\} \\
= & \Phi(u)-\phi(u)\left\{\frac{1}{2 N_{1} \Delta^{2}}\left[u^{3}+\Delta u^{2}+(p-3) u-\Delta\right]\right. \\
& +\frac{1}{2 N_{2} \Delta^{2}}\left[u^{3}+\Delta u^{2}+\left(p-3-\Delta^{2}\right) u-\Delta^{3}-\Delta\right] \\
& \left.+\frac{1}{4 n}\left[4 u^{3}+4 \Delta u^{2}+\left(6 p-6+\Delta^{2}\right) u+2(p-1) \Delta\right]\right\}+O\left(n^{-2}\right),
\end{aligned}
$$

and $\operatorname{Pr}\left\{\left.-\left(Z+\frac{1}{2} \Delta^{2}\right) / \Delta \leq u \right\rvert\, \pi_{2}\right\}$ is (16) with $N_{1}$ and $N_{2}$ interchanged.
When $c=0$, then $u=-\frac{1}{2} \Delta$. If $N_{1}=N_{2}$, the rule with $Z$ is identical to the rule with $W$, and the probability of misclassification is given by (2).

Fujikoshi and Kanazawa (1976) proved
Theorem 6.6.6

$$
\begin{aligned}
\operatorname{Pr} & \left\{\left.\frac{Z-\frac{1}{2} D^{2}}{D} \leq u \right\rvert\, \pi_{1}\right\} \\
& =\Phi(u)-\phi(u)\left\{\frac{1}{2 N_{1} \Delta}\left[u^{2}+\Delta u-(p-1)\right]\right. \\
& -\frac{1}{2 N_{2} \Delta}\left[u^{2}+2 \Delta u+p-1+\Delta^{2}\right] \\
& \left.+\frac{1}{4 n}\left[u^{3}+(4 p-3) u\right]\right\}+O\left(n^{-2}\right)
\end{aligned}
$$

$$
\begin{aligned}
\operatorname{Pr} & \left\{\left.-\frac{Z+\frac{1}{2} D^{2}}{D} \leq u \right\rvert\, \pi_{2}\right\} \\
& =\Phi(u)-\phi(u)\left\{-\frac{1}{2 N_{1} \Delta}\left[u^{2}+2 \Delta u+p-1+\Delta^{2}\right]\right. \\
& \left.\quad+\frac{1}{2 N_{2} \Delta}\left[u^{2}+\Delta u-(p-1)\right]+\frac{1}{4 n}\left[u^{3}+(4 p-3) u\right]\right\}+O\left(n^{-2}\right)
\end{aligned}
$$

Kanazawa (1979) showed the following:
Theorem 6.6.7. Let $u_{0}$ be such that $\Phi\left(u_{0}\right)=\alpha$, and let

$$
\begin{aligned}
u= & u_{0}+\frac{1}{2 N_{1} D}\left[u_{0}^{2}+D u_{0}-(p-1)\right] \\
& -\frac{1}{2 N_{2} D}\left[u_{0}^{2}+D u_{0}+(p-1)-D^{2}\right] \\
& +\frac{1}{4 n}\left[u_{0}^{3}+(4 p-5) u_{0}\right]
\end{aligned}
$$

Then as $N_{1} \rightarrow \infty, N_{2} \rightarrow \infty$, and $N_{1} / N_{2} \rightarrow$ a positive limit,

$$
\operatorname{Pr}\left\{\frac{Z-\frac{1}{2} D^{2}}{D} \leq u\right\}=\alpha+O\left(n^{-2}\right)
$$

Now consider the probabilities of misclassification after the samples have been drawn. The conditional distribution of $Z$ is not normal; $Z$ is quadratic in $x$ unless $N_{1}=N_{2}$. We do not have expressions equivalent to (12) and (13). Siotani (1980) showed the following:

Theorem 6.6.8. As $N_{1} \rightarrow \infty, N_{2} \rightarrow \infty$, and $N_{1} / N_{2} \rightarrow$ a positive limit,

$$
\begin{aligned}
\operatorname{Pr}\{ & \left\{\sqrt{\frac{N_{1} N_{2}}{N_{1}+N_{2}}} \frac{P\left(2 \mid 1,0, \bar{x}^{(1)}, \bar{x}^{(2)}, S\right)-\Phi\left(-\frac{1}{2} \Delta\right)}{\phi\left(\frac{1}{2} \Delta\right)} \leq x\right\} \\
& =\Phi\left[x-2 \sqrt{\frac{N_{1} N_{2}}{N_{1}+N_{2}}}\left\{\frac{1}{16 N_{1} \Delta}\left[4(p-1)-\Delta^{2}\right]\right.\right. \\
& \left.\left.+\frac{1}{16 N_{2}}\left[4(p-1)+3 \Delta^{2}\right]-\frac{(p-1) \Delta}{4 n}\right\}\right]+O\left(n^{-2}\right)
\end{aligned}
$$

It is also possible to obtain a similar expression for $P\left(2 \mid 1, D u_{1}+\right. \frac{1}{2} D^{2}, \bar{x}^{(1)}, \bar{x}^{(2)}, S$ ) for $Z$ and a confidence interval. See Siotani (1980).



### 6.7. CLASSIFICATION INTO ONE OF SEVERAL POPULATIONS

Let us now consider the problem of classifying an observation into one of several populations. We shall extend the consideration of the previous sections to the cases of more than two populations. Let $\pi_{1}, \ldots, \pi_{m}$ be $m$ populations with density functions $p_{1}(x), \ldots, p_{m}(x)$, respectively. We wish to divide the space of observations into $m$ mutually exclusive and exhaustive regions $R_{1}, \ldots, R_{m}$. If an obseivation falls into $R_{1}$, we shall say that it comes from $\pi_{i}$. Let the cost of misclassifying an observation from $\pi_{1}$ as coming from $\pi_{j}$ be $C(j \mid i)$. The probability of this misclassification is

$$
P(j \mid i, R)=\int_{R_{j}} p_{\imath}(x) d x
$$

Suppose we have a priori probabilities of the populations, $q_{1}, \ldots, q_{m}$. Then the expected loss is

$$
\sum_{i=1}^{m} q_{i}\left\{\sum_{\substack{j=1 \\ j \neq 1}}^{m} C(j \mid i) P(j \mid i, R)\right\} .
$$

We should like to choose $R_{1}, \ldots, R_{m}$ to make this a minimum.
Since we have a priori probabilities for the populations, we can define the conditional probability of an observation coming from a population given the values of the components of the vector $x$. The conditional probability of the observation coming from $\pi_{1}$ is

$$
\frac{q_{1} p_{1}(x)}{\sum_{k=1}^{n} q_{k} p_{k}(x)} .
$$

If we classify the observation as from $\pi_{j}$, the expected loss is

$$
\sum_{\substack{i=1 \\ i \neq j}}^{m} \frac{q_{1} p_{1}(x)}{\sum_{k=1}^{m} q_{k} p_{k}(x)} C(j \mid i)
$$

We minimize the expected loss at this point if we choose $j$ so as to minimize (4); that is, we consider

$$
\sum_{\substack{i=1 \\ i \neq j}}^{n} q_{i} p_{1}(x) C(j \mid i)
$$

for all $j$ and select that $j$ that gives the minimum. (If two different indices give the minimum, it is irrelevant which index is selected.) This procedure assigns the point $x$ to one of the $R_{j^{\prime}}$. Following this procedure for each $x$, we define our regions $R_{1}, \ldots, R_{m}$. The classification procedure, then, is to classify an observation as coming from $\pi_{j}$ if it falls in $R_{j}$.

Theorem 6.7.1. If $q_{1}$ is the a priori probability of drawing an observation from population $\pi_{1}$ with density $p_{1}(x), i=1, \ldots, m$, and if the cost of misclassifying an observation from $\pi_{i}$ as from $\pi_{j}$ is $C(j \mid i)$, then the regions of classification, $R_{1}, \ldots, R_{m}$, that minimize the expected cost are defined by assigning $x$ to $R_{\lambda}$ if

$$
\sum_{\substack{i=1 \\ i \neq k}}^{m} q_{i} p_{1}(x) C(k \mid i)<\sum_{\substack{i=1 \\ l \neq j}}^{m} q_{1} p_{1}(x) C(j \mid i), \quad j=1, \ldots, m, \quad j \neq k
$$

[If (6) holds for all $j(j \neq k)$ except for $h$ indices and the inequality is replaced by equality for those indices, then this point can be assigned to any of the $h+1 \pi ' s$.] If the probability of equality between the right-hand and left-hand sides of (6) is zero for each $k$ and $j$ under $\pi_{1}$ (each $i$ ), then the minimizing procedure is unique except for sets of probability zero.

Proof. We now verify this result. Let

$$
h_{j}(x)=\sum_{\substack{i=1 \\ l \neq j}}^{m} q_{i} p_{i}(x) C(j \mid i) .
$$

Then the expected loss of a procedure $R$ is

$$
\sum_{j=1}^{m} \int_{R_{j}} h_{j}(x) d x=\int h(x \mid R) d x
$$

where $h(x \mid R)=h_{j}(x)$ for $x$ in $R_{j}$. For the Bayes procedure $R^{*}$ described in the theorem, $h(x \mid R)$ is $h\left(x \mid R^{*}\right)=\min _{i} h_{i}(x)$. Thus; the difference between the expected loss for any procedure $R$ and for $R^{*}$ is

$$
\begin{aligned}
\int\left[h(x \mid R)-h\left(x \mid R^{*}\right)\right] d x & =\sum_{j} \int_{R_{j}}\left[h_{j}(x)-\min h_{i}(x)\right] d x \\
& \geq 0
\end{aligned}
$$

Equality can hold only if $h_{1}(x)=\min h_{1}(x)$ for $x$ in $R_{J}$ except for sets of probability zero.

Let us see how this method applies when $C(j \mid i)=1$ for all $i$ and $j, i \neq j$. Then in $R_{k}$

$$
\sum_{\substack{i=1 \\ i \neq k}}^{m} q_{i} p_{i}(x)<\sum_{\substack{i=1 \\ i \neq j}}^{m} q_{i} p_{i}(x), \quad j \neq k
$$

Subtracting $\sum_{i=1, i \neq k . j}^{m} q_{l} p_{l}(x)$ from both sides of (10), we obtain

$$
q_{j} p_{j}(x)<q_{k} p_{k}(x), \quad j \neq k
$$

In this case the point $x$ is in $R_{k}$ if $k$ is the index for which $q_{i} p_{i}(x)$ is a maximum; that is, $\pi_{k}$ is the most probable population.

Now suppose that we do not have a priori probabilities. Then we cannot define an unconditional expected loss for a classification procedure. However, we can define an expected loss on the condition that the observation comes from a given population. The conditional expected loss if the observation is from $\pi_{i}$ is

$$
\sum_{\substack{j=1 \\ j \neq 1}}^{m} C(j \mid i) P(j \mid i, R)=r(i, R) .
$$

A procedure $R$ is at least as good as $R^{*}$ if $r(i, R) \leq r\left(i, R^{*}\right), i=1, \ldots, m ; R$ is better if at least one inequality is strict. $R$ is admissible if there is no procedure $R^{*}$ that is better. A class of procedures is complete if for every procedure $R$ outside the class there is a procedure $R^{*}$ in the class that is better.

Now let us show that a Bayes procedure is admissible. Let $R$ be a Bayes procedure; let $R^{*}$ be another procedure. Since $R$ is Bayes,

$$
\sum_{i=1}^{m} q_{i} r(i, R) \leq \sum_{i=1}^{m} q_{i} r\left(i, R^{*}\right) .
$$

Suppose $q_{1}>0, q_{2}>0, r\left(2, R^{*}\right)<r(2, R)$, and $r\left(i, R^{*}\right) \leq r(i, R), i=3, \ldots, m$. Then

$$
q_{\mathrm{I}}\left[r(1, R)-r\left(1, R^{*}\right)\right] \leq \sum_{i=2}^{m} q_{i}\left[r\left(i, R^{*}\right)-r(i, R)\right]<0
$$

and $r(1, R)<r\left(1, R^{*}\right)$. Thus $R^{*}$ is not better than $R$.

Theorem 6.7.2. If $q_{i}>0, i=1, \ldots, m$, then a Bayes procedure is admissible.

We shall now assume that $C(i \mid j)=1, i \neq j$, and $\operatorname{Pr}\left\{p_{i}(x)=0 \mid \pi_{j}\right\}=0$. The latter condition implies that all $p_{i}(x)$ are positive on the same set (except fcr a set of measure 0). Suppose $q_{i}=0$ for $i=1, \ldots, t$, and $q_{i}>0$ for $i=t+ 1, \ldots, m$. Then for the Bayes solution $R_{i}, i=1, \ldots, t$, is empty (except for a set of probability 0 ), as seen from (11) [that is, $p_{m}(x)=0$ for $x$ in $R_{i}$ ]. It follows that $r(i, R)=\sum_{j \neq i} P(j \mid i, R)=1-P(i \mid i, R)=1$ for $i=1, \ldots, t$. Then $\left(R_{t+1}, \ldots, R_{m}\right)$ is a Bayes solution for the problem involving $p_{t+1}(x), \ldots, p_{m}(x)$ and $q_{t+1}, \ldots, q_{m}$. It follows from Theorem 6.7.2 that no procedure $R^{*}$ for which $P\left(i \mid i, R^{*}\right)=0, i=1, \ldots, t$, can be better than the Bayes procedure. Now consider a procedure $R^{*}$ such that $R_{1}^{*}$ includes a set of positive probability so that $P\left(1 \mid 1, R^{*}\right)>0$. For $R^{*}$ to be better than $R$,

$$
\begin{aligned}
P(i \mid i, R) & =\int_{R_{t}} p_{t}(x) d x \\
& \leq P\left(i \mid i, R^{*}\right)=\int_{R_{t}^{*}} p_{t}(x) d x, \quad i=2, \ldots, m
\end{aligned}
$$

In such a case a procedure $R^{* *}$ where $R_{i}^{* *}$ is empty, $i=1, \ldots, t, R_{i}^{* *}=R_{i}^{*}$, $i=t+1, \ldots, m-1$, and $R_{m}^{* *}=R_{m}^{*} \cup R_{1}^{*} \cup \cdots \cup R_{t}^{*}$ would give risks such that

$$
\begin{aligned}
P\left(i \mid i, R^{* *}\right) & =0, & i=1, \ldots, t, \\
P\left(i \mid i, R^{* *}\right) & =P\left(i \mid i, R^{*}\right) \geq P(i \mid i, R), & i=t+1, \ldots, m-1, \\
P\left(m \mid m, R^{* *}\right) & >P\left(m \mid m, R^{*}\right) \geq P(m \mid m, R) . &
\end{aligned}
$$

Then $R_{t+1}^{* *}, \ldots, R_{m}^{* *}$ ) would be better than ( $R_{t+1}, \ldots, R_{m}$ ) for the ( $m-t$ )decision problem, which contradicts the preceding discussion.

Theorem 6.7.3. If $C(i \mid j)=1, i \neq j$, and $\operatorname{Pr}\left\{p_{i}(x)=0 \mid \pi_{j}\right\}=0$, then a Bayes procedure is admissible.

The converse is true without conditions (except that the parameter space is finite).

Theorem 6.7.4. Every admissible procedure is a Bayes procedure.
We shall not prove this theorem. It is Theorem 1 of Section 2.10 of Ferguson (1967), for example. The class of Bayes procedures is minimal complete if each Bayes procedure is unique (for the specified probabilities).

The minimax procedure is the Bayes procedure for which the risks are equal.

There are available general treatments of statistical decision procedures by Wald (1950), Blackwell and Girshick (1954), Ferguson (1967), De Groot (1970), Berger (1980b), and others.

### 6.8. CLASSIFICATION INTO ONE OF SEVERAL MULTIVARIATE NORMAL POPULATIONS

We shall now apply the theory of Section 6.7 to the case in which each population has a normal distribution. [See von Mises (1945).] We assume that the means are different and the covariance matrices are alike. Let $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)$ be the distribution of $\pi_{1}$. The density is given by (1) of Section 6.4. At the outset the parameters are assumed known. For general costs with known a priori probabilities we can form the $m$ functions (5) of Section 6.7 and define the region $R_{j}$ as consisting of points $x$ such that the $j$ th function is minimum.

In the remainder of our discussion we shall assume that the costs of misclassification are equal. Then we use the functions

$$
u_{j k}(x)=\log \frac{p_{j}(x)}{p_{k}(x)}=\left[x-\frac{1}{2}\left(\boldsymbol{\mu}^{(j)}+\boldsymbol{\mu}^{(k)}\right)\right]^{t} \boldsymbol{\Sigma}^{-1}\left(\boldsymbol{\mu}^{(j)}-\boldsymbol{\mu}^{(k)}\right) .
$$

If a priori probabilities are known, the region $R_{j}$ is defined by those $x$ satisfying

$$
R_{j}: u_{j k}(x)>\log \frac{q_{k}}{q_{j}}, \quad \quad k=1, \ldots, m . \quad k \neq j .
$$

Theorem 6.8.1. If $q_{1}$ is the a priori probability of drawing an observation from $\pi_{1}=N\left(\boldsymbol{\mu}^{(i)}, \boldsymbol{\Sigma}\right), i=1, \ldots, m$, and if the costs of misclassification are equal, then the regions of classification, $R_{1}, \ldots, R_{m}$, that minimize the expected cost are defined by (2), where $u_{j k}(x)$ is given by (1).

It should be noted that each $u_{j k}(x)$ is the classification function related to the $j$ th and $k$ th populations, and $u_{j k}(x)=-u_{k j}(x)$. Since these are linear functions, the region $R_{i}$ is bounded by hyperplanes. If the means span an ( $m-1$ )-dimensional hyperplane (for example, if the vectors $\mu^{(i)}$ are linearly independent and $p \geq m-1$ ), then $R_{t}$ is bounded by $m-1$ hyperplanes.

In the case of no set of a priori probabilities known. the region $R_{1}$ is defined by inequalities

$$
u_{j k}(x) \geq c_{j}-c_{k},
$$

$$
k=1, \ldots, m, \quad k \neq j .
$$

The constants $c_{k}$ can be taken nonnegative. These sets of regions form the class of admissible procedures. For the minimax procedure these constants are determined so all $P(i \mid i, R)$ are equal.

We now show how to evaluate the probabilities of correct classification. If $X$ is a random observation, we consider the random variables

$$
U_{\mu}=\left[X-\frac{1}{2}\left(\mu^{(i)}+\mu^{(i)}\right)\right]^{\prime} \Sigma^{-1}\left(\mu^{(j)}-\mu^{(i)}\right) .
$$

Here $U_{\mu}=-U_{t j}$. Thus we use $m(m-1) / 2$ classification functions if the means span an ( $m-1$ )-dimensional hyperplane. If $X$ is from $\pi_{j}$, then $U_{j i}$ is distributed according to $N\left(\frac{1}{2} \Delta_{j!}^{2}, \Delta_{j!}^{2}\right)$, where

$$
\Delta_{\mu}^{2}=\left(\mu^{(\mu)}-\mu^{(l)}\right)^{\prime} \Sigma^{-1}\left(\mu^{(\mu)}-\mu^{(l)}\right) .
$$

The covariance of $U_{\mu \prime}$ and $U_{\mu k}$ is

$$
\Delta_{j k . \mu}=\left(\boldsymbol{\mu}^{(j)}-\boldsymbol{\mu}^{(k)}\right)^{\prime} \mathbf{\Sigma}^{-1}\left(\boldsymbol{\mu}^{(j)}-\boldsymbol{\mu}^{(i)}\right) .
$$

To determine the constants $c$, we consider the integrals

$$
P(j \mid j . R)=\int_{c_{1}-c_{m}}^{\infty} \cdots \int_{c_{1}-c_{1}}^{\infty} f_{j} d u_{j 1} \cdots d u_{j, j-1} d u_{j, j+1} \cdots d u_{j m}
$$

where $f_{j}$ is the density of $U_{\mu}, i=1,2, \ldots, m, i \neq j$.
Theorem 6.8.2. If $\pi_{1}$ is $N\left(\mu^{(1)}, \Sigma\right)$ and the costs of misclassification are equal, then the regions of classification, $R_{1}, \ldots, R_{m}$, that minimize the maximum conditional expected loss are defined by (3), where $u_{j k}(x)$ is given by (1). The constants $c_{1}$ are determined so that the integrals (7) are equal.

As an example consider the case of $m=3$. There is no loss of generality in taking $p=2$, for the density for higher $p$ can be projected on the two-dimensional plane determined by the means of the t'ree populations if they are not collinear (i.e., we can transform the vector $x$ into $u_{12}, u_{13}$, and $p-2$ other coordinates, where these last $p-2$ components are distributed independently of $u_{12}$ and $u_{13}$ and with zero means). The regions $R_{\mathrm{j}}$ are determined by three half lines as shown in Figure 6.2. If this procedure is minimax, we cannot move the line between $R_{1}$ and $R_{2}$ rearer ( $\mu_{1}^{(\mathrm{I})}, \mu_{2}^{(\mathrm{I})}$ ), the line between $R_{2}$ and $R_{3}$ nearer ( $\mu_{1}^{(2)}, \mu_{2}^{(2)}$ ), and the line between $R_{3}$ and $R_{1}$ nearer ( $\mu_{1}^{(3)}, \mu_{2}^{(3)}$ ) and still retain the equality $P(1 \mid 1, R)=P(2 \mid 2, R)=P(3 \mid 3, R)$ without leaving a triangle that is not included in any region. Thus, since the regions must exhaust the space, the lines must meet in a point, and the equality of probabilities determines $c_{t}-c_{1}$ uniquely.

![](https://cdn.mathpix.com/cropped/e0e01d36-0fbe-41f6-b480-cb02adca42a3-257.jpg?height=585&width=995&top_left_y=235&top_left_x=312)
Figure 6.2. Classification regions.

To do this in a specific case in which we have numerical values for the components of the vectors $\boldsymbol{\mu}^{(1)}, \boldsymbol{\mu}^{(2)}, \boldsymbol{\mu}^{(3)}$, and the mat.ix $\boldsymbol{\Sigma}$, we would consider the three ( $\leq p+1$ ) joint distributions, each of two $U_{i j}$ 's $(j \neq i)$. We could try the values of $c_{i}=0$ and, using tables [Pearson (1931)] of the bivariate normal distribution, compute $P(i \mid i, R)$. By a trial-and-error method we could obtain $c_{i}$ to approximate the above condition.

The preceding theory has been given on the assumption that the parameters are known. If they are not known and if a sample from each population is available, the estimators of the parameters can be substituted in the definition of $u_{i j}(x)$. Let the observations be $x_{1}^{(\mathrm{t})}, \ldots, x_{N_{1}}^{(\mathrm{t})}$ from $N\left(\mu^{(i)}, \Sigma\right)$, $i=1, \ldots, m$. We estimate $\mu^{(i)}$ by

$$
\bar{x}^{(t)}=\frac{1}{N_{i}} \sum_{\alpha=1}^{N_{i}} x_{\alpha}^{(1)}
$$

and $\Sigma$ by $S$ defined by

$$
\left(\sum_{i=1}^{m} N_{l}-m\right) S=\sum_{i=1}^{m} \sum_{\alpha=1}^{N_{i}}\left(x_{\alpha}^{(1)}-\bar{x}^{(i)}\right)\left(x_{\alpha}^{(i)}-\bar{x}^{(i)}\right)^{\prime} .
$$

Then, the analog of $u_{i j}(x)$ is

$$
w_{i j}(x)=\left[x-\frac{1}{2}\left(\bar{x}^{(i)}+\bar{x}^{(j)}\right)\right] S^{-1}\left(\bar{x}^{(i)}-\bar{x}^{(i)}\right) .
$$

If the variables above are random, the distributions are different from those of $U_{i j}$. However, as $N_{i} \rightarrow \infty$, the joint distributions approach those of $U_{i j}$. Hence, for sufficiently large samples one can use the theory given above.

Table 6.2
|  | Mean |  |  |
| :--- | :---: | :---: | :---: |
| Measurement | Brahmin <br> $\left(\pi_{1}\right)$ | Artisan <br> $\left(\pi_{2}\right)$ | Korwa <br> $\left(\pi_{3}\right)$ |
| Stature $\left(x_{1}\right)$ | 164.51 | 160.53 | 158.17 |
| Sitting height $\left(x_{2}\right)$ | 86.43 | 81.47 | 81.16 |
| Nasal depth $\left(x_{3}\right)$ | 25.49 | 23.84 | 21.44 |
| Nasal height $\left(x_{4}\right)$ | 51.24 | 48.62 | 46.72 |


### 6.9. AN EXAMPLE OF CLASSIFICATION INTO ONE OF SEVERAL MULTIVARIATE NORMAL POPULATIONS

Rao (1948a) considers three populations consisting of the Brahmin caste ( $\pi_{1}$ ), the Artisan caste ( $\pi_{2}$ ), and the Korwa caste ( $\pi_{3}$ ) of India. The measurements for each individual of a caste are stature ( $x_{1}$ ), sitting height ( $x_{2}$ ), nasal depth ( $x_{3}$ ), and nasal height ( $x_{4}$ ). The means of these variables in the three populations are given in Table 6.2. The matrix of correlations for all the populations is

$$
\left[\begin{array}{llll}
1.0000 & 0.5849 & 0.1774 & 0.1974 \\
0.5849 & 1.0000 & 0.2094 & 0.2170 \\
0.1774 & 0.2094 & 1.0000 & 0.2910 \\
0.1974 & 0.2170 & 0.2910 & 1.0000
\end{array}\right] .
$$

The standard deviations are $\sigma_{\mathrm{I}}=5.74, \sigma_{2}=3.20, \sigma_{3}=1.75, \sigma_{4}=3.50$. We assume that each population is normal. Our problem is to divide the space of the four variables $x_{\mathrm{I}}, x_{2}, x_{3}, x_{4}$ into three regions of classification. We assume that the costs of misclassification are equal. We shall find (i) a set of regions under the assumption that drawing a new observation from each population is equally likely $\left(q_{1}=q_{2}=q_{3}=\frac{1}{3}\right)$, and (ii) a set of regions such that the largest probability of misclassification is minimized (the minimax solution).

We first compute the coefficients of $\boldsymbol{\Sigma}^{-\boldsymbol{I}}\left(\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}\right)$ and $\boldsymbol{\Sigma}^{-\boldsymbol{I}}\left(\boldsymbol{\mu}^{(\boldsymbol{I})}-\boldsymbol{\mu}^{(3)}\right)$. Then $\Sigma^{-1}\left(\mu^{(2)}-\mu^{(3)}\right)=\Sigma^{-1}\left(\mu^{(1)}-\mu^{(3)}\right)-\Sigma^{-1}\left(\mu^{(1)}-\mu^{(2)}\right)$. Then we calculate $\frac{1}{2}\left(\mu^{(i)}+\mu^{(j)}\right)^{\prime} \Sigma^{-1}\left(\mu^{(i)}-\mu^{(j)}\right)$. We obtain the discriminant functions ${ }^{\dagger}$

$$
\begin{aligned}
& u_{\mathrm{I} 2}(x)=-0.0708 x_{1}+0.4990 x_{2}+0.3373 x_{3}+0.0887 x_{4}-43.13, \\
& u_{\mathrm{I} 3}(x)=0.0003 x_{\mathrm{I}}+0.3550 x_{2}+1.1063 x_{3}+0.1375 x_{4}-62.49, \\
& u_{23}(x)=0.0711 x_{\mathrm{I}}-0.1440 x_{2}+0.7690 x_{3}+0.0488 x_{4}-19.36 .
\end{aligned}
$$

[^0]Table 6.3
| Population of $x$ | $u$ | Means | Standard Deviation | Correlation |
| :--- | :--- | :--- | :--- | :--- |
| $\pi_{1}$ | $u_{12}$ | 1.491 | 1.727 | 0.8658 |
|  | $u_{13}$ | 3.487 | 2.641 |  |
| $\pi_{2}$ | $u_{21}$ | 1.491 | 1.727 | -0.3894 |
|  | $u_{23}$ | 1.031 | 1.436 |  |
| $\pi_{3}$ | $u_{31}$ | 3.487 | 2.641 | 0.7983 |
|  | $u_{32}$ | 1.031 | 1.436 |  |


The other three functions are $u_{21}(x)=-u_{12}(x), u_{31}(x)=-u_{13}(x)$, and $u_{32}(x)=-u_{23}(x)$. If there are a priori probabilities and they are equal, the best set of regions of classification are $R_{1}: u_{12}(x) \geq 0, u_{13}(x) \geq 0 ; R_{2}$ : $u_{21}(x) \geq 0, u_{23}(x) \geq 0$; and $R_{3}: u_{31}(x) \geq 0, u_{32}(x) \geq 0$. For example, if we obtain an individual with measurements $x$ such that $u_{12}(x) \geq 0$ and $u_{13}(x) \geq$ 0 , we classify him as a Brahmin.

To find the probabilities of misclassification when an individual is drawn from population $\pi_{g}$ we need the means, variances, and covariances of the proper pairs of $u$ 's. They are given in Table 6.3.'

The probabilities of misclassification are then obtained by use of the tables for the bivariate normal distribution. These probabilities are 0.21 for $\pi_{1}, 0.42$ for $\pi_{2}$, and 0.25 for $\pi_{3}$. For example, if measurements are made on a Brahmin, the probability that he is classified as an Artisan or Korwa is 0.21 ,

The minimax solution is obtained by finding the constants $c_{1}, c_{2}$, and $c_{;}$ for (3) of Section 6.8 so that the probabilities of misclassification are equal. The regions of classification are

$$
\begin{array}{ll}
R_{1}^{\prime}: u_{12}(x) \geq 0.54, & u_{13}(x) \geq 0.29 ; \\
R_{2}^{\prime}: u_{21}(x) \geq-0.54, & u_{23}(x) \geq-0.25 ; \\
R_{3}^{\prime}: u_{31}(x) \geq-0.29, & u_{32}(x) \geq 0.25 .
\end{array}
$$

The common probability of misclassification (to two decimal places) is 0.30 . Thus the maximum probability of misclassification has been reduced from 0.42 to 0.30 .

[^1]
### 6.10. CLASSIFICATION INTO ONE OF TWO KNOWN MULTIVARIATE NORMAL POPULATIONS WITH UNEQUAL COVARIANCE MATRICES

### 6.10.1. Likelihood Procedures

Let $\pi_{1}$ and $\pi_{2}$ be $N\left(\mu^{(1)}, \Sigma_{1}\right)$ and $N\left(\mu^{(2)}, \Sigma_{2}\right)$ with $\mu^{(1)} \neq \mu^{(2)}$ and $\Sigma_{1} \neq \Sigma_{2}$. When the parameters are known, the likelihood ratio is

$$
\begin{aligned}
\frac{p_{1}(x)}{p_{2}(x)}= & \frac{\left|\Sigma_{2}\right|^{\frac{1}{2}} \exp \left[-\frac{1}{2}\left(x-\mu^{(1)}\right)^{\prime} \Sigma_{1}^{-1}\left(x-\mu^{(1)}\right)\right]}{\left|\Sigma_{1}\right|^{\frac{1}{2}} \exp \left[-\frac{1}{2}\left(x-\mu^{(2)}\right)^{\prime} \Sigma_{2}^{-1}\left(x-\mu^{(2)}\right)\right]} \\
= & \left|\Sigma_{2}\right|^{\frac{1}{2}}\left|\Sigma_{1}\right|^{-\frac{1}{2}} \exp \left[\frac{1}{2}\left(x-\mu^{(2)}\right)^{\prime} \Sigma_{2}^{-1}\left(x-\mu^{(2)}\right)\right. \\
& \left.\quad-\frac{1}{2}\left(x-\mu^{(1)}\right)^{\prime} \Sigma_{1}^{-1}\left(x-\mu^{(1)}\right)\right] .
\end{aligned}
$$

The logarithm of (1) is quadratic in $x$. The probabilities of misclassification are difficult to compute. [One can make a linear transformation of $x$ so that its covariance matrix is $\boldsymbol{I}$ and the matrix of the quadratic form is diagonal; then the logarithm of (1) has the distribution of a linear combination of noncentral $\chi^{2}$-variables plus a constant.]

When the parameters are unknown, we consider the problem as testing the hypothesis that $x, x_{1}^{(1)}, \ldots, x_{N_{1}}^{(1)}$ are observations from $N\left(\boldsymbol{\mu}^{(1)}, \mathbf{\Sigma}_{1}\right)$ and $x_{1}^{(2)}, \ldots, x_{x_{2}}^{(2)}$ are observations from $N\left(\mu^{(2)}, \Sigma_{2}\right)$ against the alternative that $x_{1}^{(1)}, \ldots x_{v_{1}}^{(1)}$ are observations from $N\left(\mu^{(1)}, \Sigma_{1}\right)$ and $x, x_{1}^{(2)}, \ldots, x_{N_{2}}^{(2)}$ are observations from $N\left(\boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}_{2}\right)$. Under the first hypothesis the maximum likelihood estimators are $\hat{\boldsymbol{\mu}}_{1}^{(1)}=\left(N_{1} \overline{\boldsymbol{x}}^{(1)}+x\right) /\left(N_{1}+1\right), \hat{\boldsymbol{\mu}}_{1}^{(2)}=\overline{\boldsymbol{x}}^{(2)}$,

$$
\begin{aligned}
& \hat{\Sigma}_{1}(1)=\frac{1}{N_{1}+1}\left[A_{1}+\frac{N_{1}}{N_{1}+1}\left(x-\bar{x}^{(1)}\right)\left(x-x^{(1)}\right)^{\prime}\right], \\
& \hat{\Sigma}_{2}(1)=\frac{1}{N_{2}} A_{2},
\end{aligned}
$$

where $\boldsymbol{A}_{i}=\sum_{\alpha=1}^{N_{1}}\left(x_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)\left(x_{\alpha}^{(1)}-\overline{\boldsymbol{x}}^{(1)}\right)^{\prime}, i=1$, 2. (See Section 6.5.5.) Under the second hypothesis the maxinum likelihood estimators are $\hat{\boldsymbol{\mu}}_{2}^{(1)}=\bar{x}^{(1)}$, $\hat{\boldsymbol{\mu}}_{2}^{(2)}=\left(N_{2} \overline{\boldsymbol{x}}^{(2)}+\boldsymbol{x}\right) /\left(N_{2}+1\right)$,

$$
\begin{aligned}
& \hat{\boldsymbol{\Sigma}}_{\mathbf{I}}(2)=\frac{1}{N_{1}} \boldsymbol{A}_{1} \\
& \hat{\boldsymbol{\Sigma}}_{2}(2)=\frac{1}{N_{2}+1}\left[\boldsymbol{A}_{2}+\frac{N_{2}}{N_{2}+1}\left(x-\overline{\boldsymbol{x}}^{(2)}\right)\left(x-\overline{\boldsymbol{x}}^{(2)}\right)^{\prime}\right] .
\end{aligned}
$$


[^0]:    ${ }^{\dagger}$ Due to an error in computations, Rao's discriminant functions are incorrect. I am indebted to Mr. Peter Frank for assistance in the computations.

[^1]:    ${ }^{\dagger}$ Some numerical errors in Anderson (1951a) are corrected in Table 6.3 and (3).



The likelihood ratio criterion is

$$
\begin{aligned}
\frac{\left|\hat{\mathbf{\Sigma}}_{1}(2)\right|^{\frac{1}{2} N_{1}}\left|\hat{\mathbf{\Sigma}}_{2}(2)\right|^{\frac{1}{2}\left(N_{2}+1\right)}}{\left|\hat{\mathbf{\Sigma}}_{1}(1)\right|^{\frac{1}{2}\left(N_{1}+1\right)}\left|\hat{\mathbf{\Sigma}}_{2}(1)\right|^{\frac{1}{2} N_{2}}}= & \frac{\left[1+\left(x-\bar{x}^{(2)}\right)^{\prime} \boldsymbol{A}_{2}^{-1}\left(x-\bar{x}^{(2)}\right)\right]^{\frac{1}{2}\left(N_{2}+1\right)}}{\left[1+\left(x-\bar{x}^{(1)}\right)^{\prime} \boldsymbol{A}_{1}^{-1}\left(x-\bar{x}^{(1)}\right)\right]^{\frac{1}{2}\left(N_{1}+1\right)}} \\
& \cdot \frac{\left.\left.\left(N_{1}+1\right)^{\frac{1}{2}\left(N_{1}+1\right) p} N_{2}^{\frac{1}{3} N_{2} p}\right|_{\boldsymbol{A}_{2}}\right|^{\frac{1}{2}}}{\left.\left.N_{1}^{\frac{1}{2} N_{1} p}\left(N_{2}+1\right)^{\frac{1}{2}\left(N_{2}+1\right) p}\right|_{\boldsymbol{A}_{1}}\right|^{\frac{1}{2}}} .
\end{aligned}
$$

The observation $x$ is classified into $\pi_{1}$ if (4) is greater than 1 and into $\pi_{2}$ if (4) is less than 1 .

An alternative criterion is to plug estimates into the logarithm of (1). Use

$$
\frac{1}{2}\left[\left(x-\bar{x}^{(2)}\right)^{\prime} S_{2}^{-1}\left(x-\bar{x}^{(2)}\right)-\left(x-\ddot{x}^{(1)}\right)^{\prime} S_{1}^{-1}\left(x-\bar{x}^{(1)}\right)\right]
$$

to classify into $\pi_{1}$ if (5) is large and into $\pi_{2}$ if (5) is small. Again it is difficult to evaluate the probabilities of misclassification.

### 6.10.2. Linear Procedures

The best procedures when $\boldsymbol{\Sigma}_{1} \neq \boldsymbol{\Sigma}_{2}$ are not linear; when the parameters are known, the best procedures are based on a quadratic function of the vector observation $x$. The procedure depends very much on the assumed normality. For example, in the case of $p=1$, the region for classification with one population is an interval and for the other is the complement of the interval -that is, where the observation is sufficiently large or sufficiently small. In the bivariate case the regions are defined by conic sections; for example, the region of classification into one population might be the interior of an ellipse or the region between two hyperbolas. In general, the regions are defined by means of a quadratic function of the observations which is not necessarily a positive definite quadratic form. These procedures depend very much on the assumption of normality and especially on the shape of the normal distribution far from its center. For instance, in the univariate case cited above the region of classification into the first population is a finite interval because the density of the first population falls off in either direction more rapidly than the density of the second because its standard deviation is smaller.

One may want to use a classification procedure in a situation where the two populations are centered around different points and have different patterns of scatter, and where one considers multivariate normal distributions to be reasonably good approximations for these two populations near their centers and between their two centers (though not far from the centers, where the densities are small). In such a case one may want to divide the
sample space into the two regions of classification by some simple curve or surface. The simplest is a line or hyperplane; the procedure may then be termed linear.

Let $\boldsymbol{b}(\neq \mathbf{0})$ be a vector (of $p$ components) and $\boldsymbol{c}$ a scalar. An observation $x$ is classified as from the first population if $b^{\prime} x \geq c$ and as from the second if $b^{\prime} x<c$. We are primarily interested in situations where the important difference between the two populations is the difference between the centers; we assume $\mu^{(1)} \neq \mu^{(2)}$ as well as $\Sigma_{1} \neq \Sigma_{2}$, and that $\Sigma_{1}$ and $\Sigma_{2}$ are nonsingular.

When sampling from the $i$ th population, $\boldsymbol{b}^{\prime} x$ has a univariate normal distribution with mean $\mathscr{E}\left(\boldsymbol{b}^{\prime} x \mid \pi_{i}\right)=\boldsymbol{b}^{\prime} \boldsymbol{\mu}^{(i)}$ and variance

$$
\mathscr{E}\left(\boldsymbol{b}^{\prime} x-\boldsymbol{b}^{\prime} \boldsymbol{\mu}^{(i)}\right)^{2}\left|\pi_{i}=\mathscr{E} \boldsymbol{b}^{\prime}\left(x-\boldsymbol{\mu}^{(i)}\right)\left(x-\boldsymbol{\mu}^{(i)}\right)^{\prime} \boldsymbol{b}\right| \pi_{i}=\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{i} \boldsymbol{b} .
$$

The probability of misclassifying an observation when it comes from the first population is

$$
\begin{aligned}
P(2 \mid 1) & =\operatorname{Pr}\left\{b^{\prime} x<c \mid \pi_{1}\right\}=\operatorname{Pr}\left\{\left.\frac{b^{\prime} x-b^{\prime} \mu^{(1)}}{\left(b^{\prime} \Sigma_{1} b\right)^{\frac{1}{2}}}<\frac{c-b^{\prime} \mu^{(1)}}{\left(b^{\prime} \Sigma_{1} b\right)^{\frac{1}{2}}} \right\rvert\, \pi_{1}\right\} \\
& =\Phi\left(\frac{c-b^{\prime} \mu^{(1)}}{\left(b^{\prime} \Sigma_{1} b\right)^{\frac{1}{2}}}\right)=1-\Phi\left(\frac{b^{\prime} \mu^{(1)}-c}{\left(b^{\prime} \Sigma_{1} b\right)^{\frac{1}{2}}}\right)
\end{aligned}
$$

The probability of misclassifying an observation when it comes from the second population is

$$
\begin{aligned}
P(1 \mid 2) & =\operatorname{Pr}\left\{b^{\prime} x \geq c \mid \pi_{2}\right\}=\operatorname{Pr}\left\{\left.\frac{b^{\prime} x-b^{\prime} \mu^{(2)}}{\left(b^{\prime} \Sigma_{2} b\right)^{\frac{1}{2}}} \geq \frac{c-b^{\prime} \mu^{(2)}}{\left(b^{\prime} \Sigma_{2} b\right)^{\frac{1}{2}}} \right\rvert\, \tau_{2}\right\} \\
& =1-\Phi\left(\frac{c-b^{\prime} \mu^{(2)}}{\left(b^{\prime} \Sigma_{2} b\right)^{\frac{1}{2}}}\right)
\end{aligned}
$$

It is desired to make these probabilities small or, equivalently, to make the arguments

$$
y_{1}=\frac{\boldsymbol{b}^{\prime} \boldsymbol{\mu}^{(1)}-c}{\left(\boldsymbol{b}^{\prime} \Sigma_{1} b\right)^{\frac{1}{2}}}, \quad y_{2}=\frac{c-\boldsymbol{b}^{\prime} \boldsymbol{\mu}^{(2)}}{\left(\boldsymbol{b}^{\prime} \Sigma_{2} b\right)^{\frac{1}{2}}}
$$

large. We shall consider making $y_{1}$ large for given $y_{2}$.
When we eliminate $c$ from (9), we obtain

$$
y_{1}=\left[\boldsymbol{b}^{\prime} \gamma-y_{2}\left(\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{2} \boldsymbol{b}\right)^{\frac{1}{2}}\right]\left(\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{1} \boldsymbol{b}\right)^{-\frac{1}{2}},
$$

where $\boldsymbol{\gamma}=\boldsymbol{\mu}^{(1)}-\boldsymbol{\mu}^{(2)}$. To maximizc $y_{1}$ for given $y_{2}$ wc differentiate $y_{1}$ with respect to $b$ to obtain

$$
\begin{aligned}
\frac{\partial y_{1}}{\partial b}= & {\left[\gamma-y_{2}\left(b^{\prime} \boldsymbol{\Sigma}_{2} b\right)^{-\frac{1}{2}} \boldsymbol{\Sigma}_{2} b\right]\left(b^{\prime} \boldsymbol{\Sigma}_{1} b\right)^{-\frac{1}{2}} } \\
& -\left[b^{\prime} \gamma-y_{2}\left(b^{\prime} \boldsymbol{\Sigma}_{2} b\right)^{\frac{1}{2}}\right]\left(b^{\prime} \boldsymbol{\Sigma}_{1} b\right)^{-\frac{1}{2}} \boldsymbol{\Sigma}_{1} b .
\end{aligned}
$$

If we let

$$
\begin{aligned}
& t_{1}=\frac{b^{\prime} \gamma-y_{2}\left(b^{\prime} \Sigma_{2} b\right)^{\frac{1}{2}}}{b^{\prime} \Sigma_{1} b} \\
& t_{2}=\frac{y_{2}}{\sqrt{b^{\prime} \Sigma_{2} b^{\prime}}}
\end{aligned}
$$

then (11) set equal to 0 is

$$
\left(t_{1} \mathbf{\Sigma}_{\mathbf{1}}+t_{2} \mathbf{\Sigma}_{2}\right) b=\gamma .
$$

Note that (13) and (14) imply (12). If there is a pair $t_{1}, t_{2}$, and a vector $b$ Satisfying (12) and (13), then $c$ is obtained from (9) as

$$
c=y_{2} \sqrt{b^{\prime} \Sigma_{2} b}+b^{\prime} \mu^{(2)}=t_{2} b^{\prime} \Sigma_{2} b+b^{\prime} \mu^{(2)}
$$

Then from (9), (12), and (13)

$$
y_{\mathrm{I}}=\frac{b^{\prime} \mu^{(1)}-\left(t_{2} b^{\prime} \Sigma_{2} b+b^{\prime} \mu^{(2)}\right)}{\sqrt{b^{\prime} \Sigma_{1} b}}=t_{\mathrm{I}} \sqrt{b^{\prime} \Sigma_{1} b} .
$$

Now consider (14) as a function of $t(0 \leq t \leq 1)$. Let $t_{1}=t$ and $t_{2}=1-t$; then $\boldsymbol{b}=\left(t_{1} \Sigma_{1}+t_{2} \Sigma_{2}\right)^{-1} \gamma$. Define $v_{1}=t_{1} \sqrt{\boldsymbol{b}^{\prime} \Sigma_{1} \boldsymbol{b}}$ and $v_{2}=t_{2} \sqrt{\boldsymbol{b}^{\prime} \Sigma_{2} \boldsymbol{b}}$. The derivative of $v_{\mathrm{I}}^{2}$ with respect to $t$ is

$$
\begin{aligned}
& \frac{d}{d t} t^{2} \gamma^{\prime}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \Sigma_{1}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \gamma \\
&= 2 t \gamma^{\prime}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \Sigma_{1}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \gamma \\
&-t^{2} \gamma^{\prime}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1}\left(\Sigma_{1}-\Sigma_{2}\right)\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \\
& \cdot \Sigma_{1}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \gamma \\
&-t^{2} \gamma^{\prime}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \Sigma_{1}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \\
& \cdot\left(\Sigma_{1}-\Sigma_{2}\right)\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \gamma \\
&= t \gamma^{\prime}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1}\left\{\Sigma_{2}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \Sigma_{1}\right. \\
&\left.+\Sigma_{1}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \Sigma_{2}\right\}\left[t \Sigma_{1}+(1-t) \Sigma_{2}\right]^{-1} \gamma
\end{aligned}
$$

by the following lemma.

Lemma 6.10.1. If $\Sigma_{1}$ and $\Sigma_{2}$ are positive definite and $t_{1}>0, t_{2}>0$, then

$$
\Sigma_{2}\left[t_{1} \Sigma_{1}+t_{2} \Sigma_{2}\right]^{-1} \Sigma_{1}
$$

is posinive definite.
Proof. The matrix (18) is

$$
\Sigma_{2}\left[\Sigma_{1}\left(t_{1} \Sigma_{2}^{-1}+t_{2} \Sigma_{1}^{-1}\right) \Sigma_{2}\right]^{-1} \Sigma_{1}=\left(t_{1} \Sigma_{2}^{-1}+t_{2} \Sigma_{1}^{-1}\right)^{-1} .
$$

Similarly $d v_{2}^{2} / d t<0$. Since $v_{1} \geq 0, v_{2} \geq 0$, we see that $v_{\mathrm{I}}$ increases with $t$ from 0 at $t=0$ to $\sqrt{\boldsymbol{\gamma}^{\prime} \boldsymbol{\Sigma}_{\mathbf{I}}^{-1} \boldsymbol{\gamma}}$ at $t=1$ and $v_{2}$ decreases from $\sqrt{\boldsymbol{\gamma}^{\prime} \boldsymbol{\Sigma}_{2}^{-1} \boldsymbol{\gamma}}$ at $\imath=0$ to 0 at $l=1$. The coordinates $v_{1}$ and $v_{2}$ are continuous functions of $t$. For given $y_{2}, 0 \leq y_{2} \leq \sqrt{\gamma^{\prime} \Sigma_{2}^{-1} \gamma}$, there is a $t$ such that $y_{2}=v_{2}=t_{2} \sqrt{b^{\prime} \Sigma_{2} b}$ and $\boldsymbol{b}$ satisfies (14) for $t_{1}=t$ and $t_{2}=1-t$. Then $y_{1}=v_{1}=t_{1} \sqrt{\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{1} \boldsymbol{b}}$ maximizes $y_{1}$ for that value of $y_{2}$. Similarly given $y_{1}, 0 \leq y_{1} \leq \sqrt{\gamma^{\prime} \Sigma_{1}^{-1} \gamma}$, there is a $l$ such that $y_{1}=v_{1}=t_{1} \sqrt{\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{1} \boldsymbol{b}}$ and $\boldsymbol{b}$ satisfies (14) for $t_{\mathrm{I}}=t$ and $t_{2}=1-t$, and $y_{2}=v_{2}=t_{2} \sqrt{b^{\prime} \Sigma_{2} b}$ maximizes $y_{2}$. Note that $y_{1} \geq 0, y_{2} \geq 0$ implies the errors of misclassification are not greater than $\frac{1}{2}$.

We now argue that the set of $y_{1}, y_{2}$ defined this way correspond to admissible linear procedures. Let $x_{1}, x_{2}$ be in this set, and suppose another procedure defined by $z_{1}, z_{2}$ were better than $x_{1}, x_{2}$, that is, $x_{1} \leq z_{1}, x_{2} \leq z_{2}$ with at least one strict inequality. For $y_{1}=z_{1}$ let $y_{2}^{*}$ be the maximum $y_{2}$ among linear procedures; then $z_{1}=y_{1}, z_{2} \leq y_{2}^{*}$ and hence $x_{1} \leq y_{1}, x_{2} \leq y_{1}^{*}$. Hou ever, this is possible only if $x_{1}=y_{1}, x_{2}=y_{2}^{*}$, because $d y_{1} / d y_{2}<0$. Now we have a contradiction to the assumption that $z_{1}, z_{2}$ was better than $x_{1}, x_{2}$. Thus $x_{1} \cdot x_{2}$ corresponds to an admissible linear procedure.

## Use of Admissible Linear Procedures

Given $t_{1}$ and $t_{2}$ such that $t_{1} \Sigma_{1}+t_{2} \Sigma_{2}$ is positive definite, one would conlpute the optimum $\boldsymbol{b}$ by solving the linear equations (15) and then compute $c$ by one of (9). Usually $t_{1}$ and $t_{2}$ are not given, but a desired solution is specified in another way. We consider three ways.

## Minimization of One Probability of Misclassification for a Specified Probability of the Other

Suppose we are given $y_{2}$ (or, equivalently, the probability of misclassification when sampling from the second distribution) and we want to maximize $y_{1}$ (or. equivalently, minimize the probability of misclassification when sampling from the first distribution). Suppose $y_{2}>0$ (i.e., the given probability of misclassification is less than $\frac{1}{2}$ ). Then if the maximum $y_{1} \geq 0$, we want to find $t_{2}=1-t_{1}$ such that $y_{2}=t_{2}\left(b^{\prime} \Sigma_{2} b\right)^{\frac{1}{2}}$, where $b=\left[t_{1} \Sigma_{1}+t_{2} \Sigma_{2}\right]^{-1} \gamma$. The solu-
tion can be approximated by trial and error, since $y_{2}$ is an increasing function of $t_{2}$. For $t_{2}=0, y_{2}=0$; and for $t_{2}=1, y_{2}=\left(\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{2} \boldsymbol{b}\right)^{\frac{1}{2}}=\left(\boldsymbol{b}^{\prime} \boldsymbol{\gamma}\right)^{\frac{1}{2}}=\left(\boldsymbol{\gamma}^{\prime} \boldsymbol{\Sigma}_{2}^{-1} \boldsymbol{\gamma}\right)$, where $\boldsymbol{\Sigma}_{2} \boldsymbol{b}=\boldsymbol{\gamma}$. One could try other values of $t_{2}$ successively by solving (14) and inserting in $\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{2} \boldsymbol{b}$ until $t_{2}\left(\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{2} \boldsymbol{b}\right)^{\frac{1}{2}}$ agreed closely enough with the desired $y_{2} .\left[y_{1}>0\right.$ if the specified $y_{2}<\left(\boldsymbol{\gamma}^{\prime} \boldsymbol{\Sigma}_{2}^{-1} \boldsymbol{\gamma}\right)^{\frac{1}{2}}$.]

## The Minimax Procedure

The minimax procedure is the admissible procedure for which $y_{1}=y_{2}$. Since for this procedure both probabilities of correct classification are greater than $\frac{1}{2}$, we have $y_{1}=y_{2}>0$ and $t_{1}>0, t_{2}>0$. We want to find $t\left(=t_{1}=1-t_{2}\right)$ so that

$$
\begin{aligned}
0 & =y_{1}^{2}-y_{2}^{2}=t^{2} b^{\prime} \Sigma_{1} b-(1-t)^{2} b^{\prime} \Sigma_{2} b \\
& =b^{\prime}\left[t^{2} \Sigma_{1}-(1-t)^{2} \Sigma_{2}\right] b .
\end{aligned}
$$

Since $y_{1}^{2}$ increases with $t$ and $y_{2}^{2}$ decreases with increasing $t$, there is one and only one solution to (20), and this can be approximated by trial and error by guessing a value of $t(0<t<1)$, solving (14) for $\boldsymbol{b}$, and computing the quadratic form on the right of (20). Then another $t$ can be tried.

An alternative approach is to set $y_{1}=y_{2}$ in (9) and solve for $c$. Then the common value of $y_{1}=y_{2}$ is

$$
\frac{b^{\prime} \gamma}{\left(b^{\prime} \Sigma_{1} b\right)^{\frac{1}{2}}+\left(b^{\prime} \Sigma_{2} b\right)^{\frac{1}{2}}},
$$

and we want to find $\boldsymbol{b}$ to maximize this, where $\boldsymbol{b}$ is of the form

$$
\left[t \mathbf{\Sigma}_{1}+(1-t) \mathbf{\Sigma}_{2}\right]^{-1} \gamma
$$

with $0<t<1$.
When $\Sigma_{1}=\Sigma_{2}$, twice the maximum of (21) is the squared Mahalanobis distance between the populations. This suggests that when $\mathbf{\Sigma}_{\mathbf{I}}$ may be unequal to $\Sigma_{2}$, twice the maximum of (21) might be called the distance between the populations.

Welch and Wimpress (1961) have programmed the minimax procedure and applied it to the recognition of spoken sounds.

## Case of A Priori Probabilities

Suppose we are given a priori probabilities, $q_{1}$ and $q_{2}$, of the first and second populations, respectively. Then the probability of a misclassification is

$$
q_{1}\left[1-\boldsymbol{\Phi}\left(y_{1}\right)\right]+q_{2}\left[1-\boldsymbol{\Phi}\left(y_{2}\right)\right]=1-\left[q_{1} \boldsymbol{\Phi}\left(y_{1}\right)+q_{2} \boldsymbol{\Phi}\left(y_{2}\right)\right]
$$

which we want to minimize. The solution will be an admissible linear procedure. If we know it involves $y_{\mathrm{I}} \geq 0$ and $y_{2} \geq 0$, we can substitute $y_{1}=t\left(\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{1} \boldsymbol{b}\right)^{\frac{1}{2}}$ and $y_{2}=(1-t)\left(\boldsymbol{b}^{\prime} \boldsymbol{\Sigma}_{2} \boldsymbol{b}\right)^{\frac{1}{2}}$, where $\boldsymbol{b}=\left[t \boldsymbol{\Sigma}_{1}+(1-t) \boldsymbol{\Sigma}_{2}\right]^{-1} \gamma$, into (23) and set the derivative of (23) with respect to $t$ equal to 0 , obtaining

$$
q_{\mathrm{I}} \phi\left(y_{\mathrm{I}}\right) \frac{d y_{1}}{d t}+q_{2} \phi\left(y_{2}\right) \frac{d y_{2}}{d t}=0
$$

where $\phi(u)=(2 \pi)^{-\frac{1}{2}} e^{-\frac{1}{2} u^{2}}$. There does not seem to be any easy or direct way of solving (24) for $t$. The left-hand side of (24) is not necessarily monotonic. In fact, there may be several roots to (24). If there are, the absolute minimum will be found by putting the solution into (23). (We remind the reader that the curve of admissible error probabilities is not necessary convex.)

Anderson and Bahadur (1962) studied these linear procedures in general, including $y_{1}<0$ and $y_{2}<0$. Clunies-Ross and Riffenburgh (1960) approached the problem from a more geometric point of view.

## PROBLEMS

6.1. (Sec. 6.3) Let $\pi_{i}$ be $N\left(\boldsymbol{\mu}, \boldsymbol{\Sigma}_{i}\right), i=1,2$, Find the form of the admissible classification procedures.
6.2. (Sec. 6.3) Prove that every complete class of procedures includes the class of admissible procedures.
6.3. Sec. 6.3) Prove that if the class of admissible procedures is complete, it is minimal complete.
6.4. (Sec. 6.3) The Neyman-Pearson fundamental lemma states that of all tests at a given significance level of the null hypothesis that $x$ is drawn from $p_{1}(x)$ against alternative that it is drawn from $p_{2}(x)$ the most powerful test has the critical region $p_{1}(x) / p_{2}(x)<k$. Show that the discussion in Section 6.3 proves this result.
6.5. (Sec. 6.3) When $p(x)=n(x \mid \boldsymbol{\mu}, \boldsymbol{\Sigma})$ find the best test of $\boldsymbol{\mu}=\mathbf{0}$ against $\boldsymbol{\mu}=\boldsymbol{\mu}^{*}$ at significance level $\varepsilon$. Show that this test is uniformly most powerful against all alternatives $\mu=c \mu^{*}, c>0$. Prove that there is no uniformly most powerful test against $\boldsymbol{\mu}=\boldsymbol{\mu}^{(\mathbf{I})}$ and $\boldsymbol{\mu}=\boldsymbol{\mu}^{(\mathbf{2})}$ unless $\boldsymbol{\mu}^{(\mathbf{I})}=c \boldsymbol{\mu}^{(\mathbf{2})}$ for some $c>0$.
6.6. (Sec. 6.4) Let $P(2 \mid 1)$ and $P(1 \mid 2)$ be defined by (14) and (15). Prove if $-\frac{1}{2} \Delta^{2}<c<\frac{1}{2} \Delta^{2}$, then $P(2 \mid 1)$ and $P(1 \mid 2)$ are decreasing functions of $\Delta$.
6.7. (Sec. 6.4) Let $x^{\prime}=\left(x^{(1) \prime}, x^{(2) \prime}\right)$. Using Problem 5.23 and Problem 6.6, prove that the class of classification procedures based on $x$ is uniformly as good as the class of procedures based on $x^{(1)}$.
6.8. (Sec. 6.5.1) Find the criterion for classifying irises as Iris setosa or Iris versicolor on the basis of data given in Section 5.3.4. Classify a random sample of 5 Iris virginica in Table 3.4.
6.9. (Sec. 6.5.1) Let $W(x)$ be the classification criterion given by (2). Show that the $\boldsymbol{T}^{2}$-criterion for testing $N\left(\boldsymbol{\mu}^{(1)}, \boldsymbol{\Sigma}\right)=N\left(\boldsymbol{\mu}^{(2)}, \boldsymbol{\Sigma}\right)$ is proportional to $W\left(\boldsymbol{x}^{(1)}\right)$ and $W\left(\bar{x}^{(2)}\right)$.
6.10. (Sec. 6.5.1) Show that the probabilities of misclassification of $x_{1} \ldots, x_{N}$ (all assumed to be from either $\pi_{1}$ or $\pi_{2}$ ) decrease as $N$ increases.
6.11. (Sec. 6.5) Show that the elements of $M$ are invariant under the transformation (34) and that any function of the sufficient statistics that is invariant is a function of $M$.
6.12. (Sec. 6.5) Consider $d^{\prime} x^{(i)}$. Prove that the ratio

$$
\frac{\left(d^{\prime} \tilde{x}^{(1)}-d^{\prime} \tilde{x}^{(2)}\right)^{2}}{\sum_{\alpha=1}^{N_{1}}\left(d^{\prime} x_{\alpha}^{(1)}-d^{\prime} \tilde{x}^{(1)}\right)^{2}+\sum_{\alpha=1}^{N_{2}}\left(d^{\prime} x_{a}^{(2)}-d^{\prime} \bar{x}^{(2)}\right)^{2}}
$$

6.13. (Sec. 6.6) Show that the derivative of (2) to terms of order $n^{-1}$ is

$$
-\phi\left(\frac{1}{2} \Delta\right)\left\{\frac{1}{2}+\frac{1}{n}\left[\frac{p-1}{\Delta^{2}}+\frac{p-2}{4}-\frac{p}{8} \Delta^{2}\right]\right\} .
$$

6.14. (Sec. 6.6) Show $\mathscr{E} D^{2}$ is (4). [Hint: Let $\Sigma=I$ and show that $\mathscr{E}\left(S^{-1} \mid \Sigma=I\right)= [n /(n-p-1)] I$.]
6.15. (Sec. 6.6.2) Show

$$
\begin{aligned}
& \operatorname{Pr}\left\{\left.\frac{Z-\frac{1}{2} D^{2}}{D} \leq u \right\rvert\, \pi_{1}\right\}-\operatorname{Pr}\left\{\left.\frac{Z-\frac{1}{2} \Delta^{2}}{\Delta} \leq u \right\rvert\, \pi_{1}\right\} \\
& \quad=\phi(u)\left\{\frac{1}{2 N_{1} \Delta^{2}}\left[u^{3}+(p-3) u-\Delta^{2} u+p \Delta\right]\right. \\
& \quad+\frac{1}{2 N_{2} \Delta^{2}}\left[u^{3}+2 \Delta u^{2}+\left(p-3+\Delta^{2}\right) u-\Delta^{3}+p \Delta\right] \\
& \left.\quad+\frac{1}{4 n}\left[3 u^{3}+4 \Delta u^{2}+\left(2 p-3+\Delta^{2}\right) u+2(p-1) \Delta\right]\right\}+O\left(n^{-2}\right)
\end{aligned}
$$

6.16. (Sec. 6.8) Let $\pi_{i}$ be $N\left(\boldsymbol{\mu}^{(i)}, \boldsymbol{\Sigma}\right), i=1 \ldots, m$. If the $\boldsymbol{\mu}^{(i)}$ are on a line (i.e., $\boldsymbol{\mu}^{(i)}=\boldsymbol{\mu}+\boldsymbol{\nu}_{\boldsymbol{i}} \boldsymbol{\beta}$ ), show that for admissible procedures the $R_{t}$ are defined by parallel planes. Thus show that only one discriminant function $u_{f k}(x)$ need be used.
6.17. (Sec. 6.8) In Section 8.8 data are given on samples from four populations of skulls. Consider the first two measurements and the first three samples. Construct the classification functions $u_{i j}(x)$. Find the procedure for $q_{i}= N_{1} /\left(N_{1}+N_{2}+N_{3}\right)$. Find the minimax procedure.
6.18. (Sec. 6.10) Show that $b^{\prime} x=c$ is the equation of a plane that is tangent to an ellipsoid of constant density of $\pi_{1}$ and to an ellipsoid of constant density of $\pi_{2}$ at a common point.
6.19. (Sec. 6.8) Let $x_{1}^{(1)}, \ldots, x_{N_{1}}^{(1)}$ be observations from $N\left(\mu^{(1)}, \Sigma\right), i=1,2,3$, and let $\lambda$ be an observation to be classified. Give explicitly the maximum likelihood rule.
6.20. (Sec. 6.5) Verify (33).

## The Distribution of the Sample Covariance Matrix and the Sample Generalized Variance

### 7.1. INTRODUCTION

The sample covariance matrix, $S=[1 /(N-1)] \sum_{\alpha=1}^{n}\left(x_{\alpha}-\bar{x}\right)\left(x_{\alpha}-\bar{x}\right)^{\prime}$, is an unbiased estimator of the population covariance matrix $\boldsymbol{\Sigma}$. In Section 4.2 we found the density of $A=(N-1) S$ in the case of a $2 \times 2$ matrix. In Section 7.2 this result will be generalized to the case of a matrix $\boldsymbol{A}$ of any order. When $\Sigma=I$, this distribution is in a sense a generalization of the $\chi^{2}$-distribution. The distribution of $\boldsymbol{A}$ (or $\boldsymbol{S}$ ), often called the Wishart distribution, is fundamental to multivariate statistical analysis. In Sections 7.3 and 7.4 we discuss some properties of the Wishart distribution.

The generalized variance of the sample is defined as $|\boldsymbol{S}|$ in Section 7.5; it is a measure of the scatter of the sample. Its distribution is characterized. The density of the set of all correlation coefficients when the components of the observed vector are independent is obtaincd in Section 7.6.

The inverted Wishart distribution is introduced in Section 7.7 and is used as an a priori distribution of $\mathbf{\Sigma}$ to obtain a Bayes estimator of the covariance matrix. In Section 7.8 we consider improving on $S$ as an estimator of $\Sigma$ with respect to two loss functions. Section 7.9 treats the distributions for sampling from elliptically contoured distributions.

[^0]
### 7.2. THE WISHART DISTRIBUTION

We shall obtain the distribution of $A=\sum_{\alpha=1}^{N}\left(X_{\alpha}-\bar{X}\right)\left(X_{\alpha}-\bar{X}\right)^{\prime}$, where $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{N}(N>p)$ are independent, each with the distribution $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, As was shown in Section 3.3, $A$ is distributed as $\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}$, where $n=N-1$ and $Z_{1}, \ldots, Z_{n}$ are independent, each with the distribution $N(\mathbf{0}, \mathbf{\Sigma})$. We shall show that the density of $A$ for $A$ positive definite is

$$
\frac{|A|^{\frac{1}{2}(n-p-1)} \exp \left(-\frac{1}{2} \operatorname{tr} \Sigma^{-1} A\right)}{2^{\frac{1}{2} n p} \pi^{P(p-1) / 4}|\Sigma|^{\frac{1}{2} n} \prod_{i=1}^{P} \Gamma\left[\frac{1}{2}(n+1-i)\right]} .
$$

We shall first consider the case of $\mathbf{\Sigma}=\boldsymbol{I}$. Let

$$
\left(Z_{1}, \ldots, Z_{n}\right)=\left(\begin{array}{c}
v_{1}^{\prime} \\
\vdots \\
v_{p}^{\prime}
\end{array}\right)
$$

Then the elements of $A=\left(a_{i j}\right)$ are inner products of these $n$-component vectors, $a_{i j}=\nu_{i}^{\prime} \nu_{j}$. The vectors $\nu_{1}, \ldots, \nu_{p}$ are independently distributed, each according to $N\left(\mathbf{0}, \boldsymbol{I}_{n}\right)$. It will be convenient to transform to new coordinates according to the Gram-Schmidt orthogonalization. Let $w_{1}=v_{1}$,

$$
w_{i}=v_{i}-\sum_{j=1}^{i-1} w_{j} \frac{w_{j}^{\prime} v_{i}}{v_{j}^{\prime} w_{j}}, \quad i=2, \ldots, p
$$

We prove by induction that $w_{k}$ is orthogonal to $w_{i}, k<i$. Assume $w_{k}^{\prime} w_{h}=0$, $k \neq h, k, h=1, \ldots, i-1$; then take the inner product of $w_{k}$ and (3) to obtain $\boldsymbol{w}_{k}^{\prime} \boldsymbol{w}_{i}=0, k=1, \ldots, i-1$. (Note that $\operatorname{Pr}\left\{\left\|\boldsymbol{w}_{i}\right\|=0\right\}=0$.)

Define $t_{i i}=\left\|w_{i}\right\|=\sqrt{w_{i}^{\prime} w_{i}}, i=1, \ldots, p$, and $t_{i j}=v_{i}^{\prime} w_{j} /\left\|w_{j}\right\|, j=1, \ldots, i-1$, $i=2, \ldots, p$. Since $\nu_{i}=\sum_{j=1}^{i}\left(t_{i j} /\left\|w_{j}\right\|\right) w_{j}$,

$$
a_{h i}=v_{h}^{\prime} v_{i}=\sum_{j=1}^{\min (h, i)} t_{h j} t_{i j}
$$

If we define the lower triangular matrix $T=\left(t_{i j}\right)$ with $t_{i i}>0, i=1, \ldots, p$, and $t_{i j}=0, i<j$, then

$$
A=T T^{\prime}
$$

Note that $t_{i j}, j=1, \ldots, i-1$, are the first $i-1$ coordinates of $\nu_{i}$ in the coordinate system with $w_{1}, \ldots, w_{t-1}$ as the first $i-1$ coordinate axes. (See Figure 7.1.) The sum of the other $n-i+1$ coordinates squared is $\left\|v_{i}\right\|^{2}$-. $\sum_{j=1}^{i-1} t_{i j}^{2}=t_{i 1}^{2}=\left\|w_{i}\right\|^{2} ; w_{i}$ is the vector from $v_{i}$ to its projection on $w_{1}, \ldots, w_{i-1}$ (or equivalently on $\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{i-1}$ ).


[^0]:    An Introduction to Multivartate Statistical Analysis, Third Edition. By T. W. Anderson ISBN 0-47t-36091-0 Copyright © 2003 John Wilcy \& Sons, Inc.



![](https://cdn.mathpix.com/cropped/397b4457-0c9a-4bee-bec2-71401753afe8-271.jpg?height=777&width=922&top_left_y=232&top_left_x=351)
Figure 7.1. Transformation of corrdinates.

Lemma 7.2.1. Conditional on $w_{1}, \ldots, w_{t-1}$ (or equivalently on $v_{1}, \ldots, v_{1-1}$ ), $t_{i 1}, \ldots, t_{i, i-1}$ and $t_{i i}^{2}$ are independently distributed; $t_{i j}$ is distributed according to $N(0,1), i>j$; and $t_{n i}^{2}$ has the $i^{2}$-distribution with $n-i+1$ degrees of freedom.

Proof. The coordinates of $\nu_{1}$ referred to the new orthogonal coordinates with $v_{1}, \ldots, v_{1-1}$ defining the first coordinate axes are independently normally distributed with means 0 and variances 1 (Theorem 3.3.1). $t_{\|}^{2}$ is the sum of the coordinates squared omitting the first $i-1$.

Since the conditional distribution of $t_{11}, \ldots, t_{1 i}$ does not depend on $v_{1}, \ldots, v_{i-1}$, they are distributed independently of $f_{11}, t_{21}, t_{22}, \ldots, t_{\mathrm{r}-1, i-1}$.

Corollary 7.2.1. Let $Z_{1}, \ldots, Z_{n}(n \geq p)$ be independently distributed, each according to $N(\mathbf{0}, I)$; let $A=\sum_{n=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}=T T^{\prime}$, where $t_{i j}=0, i<j$, and $t_{i j}>0$, $i=1, \ldots, p$. Then $t_{11}, t_{21}, \ldots, t_{p p}$ are independently distributed; $t_{1}$, is distributed according to $N(0,1), i>j$, and $t_{i i}^{2}$ has the $\chi^{2}$-distribution with $n-i+1$ degrees of freedom.

Since $t_{\imath i}$ has density $2^{-\frac{1}{2}(n-\imath-1)} t^{n-\imath} e^{-\frac{1}{2} t^{2}} / \Gamma\left[\frac{1}{2}(n+1-i)\right]$, the joint density of $t_{i j}, j=1, \ldots, i, i=1, \ldots, p$, is

$$
\begin{aligned}
\prod_{i=1}^{p} & \frac{t_{i l}^{n-i} \exp \left(-\frac{1}{2} \sum_{j=1}^{l} t_{i j}^{2}\right)}{\pi^{\frac{1}{2}(i-1)} 2^{\frac{1}{n} n-1} \Gamma\left[\frac{1}{2}(n+1-i)\right]} \\
& =\frac{\prod_{i=1}^{p} t_{i n}^{n-l} \exp \left(-\frac{1}{2} \sum_{i=1}^{p} \sum_{j=1}^{l} t_{i j}^{2}\right)}{2^{\frac{1}{2} p(n-2)} \pi^{p(p-1) / 4} \prod_{i=1}^{p} \Gamma\left[\frac{1}{2}(n+1-i)\right]} .
\end{aligned}
$$

Let $C$ be a lower triangular matrix ( $c_{i j}=0, i<j$ ) such that $\Sigma=C C^{\prime}$ and $c_{11}>0$. The linear transformation $\boldsymbol{T}^{*}=\boldsymbol{C} \boldsymbol{T}$, that is,

$$
\begin{aligned}
t_{i j}^{*} & =\sum_{k=j}^{i} c_{i k} t_{k j}, & i \geq j, \\
& =0, & i<j,
\end{aligned}
$$

can be written

$$
\left[\begin{array}{c}
t_{11}^{*} \\
t_{21}^{*} \\
t_{22}^{*} \\
\vdots \\
t_{p 1}^{*} \\
\vdots \\
t_{p p}^{*}
\end{array}\right]=\left[\begin{array}{ccccccc}
c_{11} & 0 & 0 & \cdots & 0 & \cdots & 0 \\
x & c_{22} & 0 & \cdots & 0 & \cdots & 0 \\
x & x & c_{22} & \cdots & 0 & \cdots & 0 \\
\vdots & \vdots & \vdots & & \vdots & & \vdots \\
x & x & x & \cdots & c_{p p} & \cdots & 0 \\
\vdots & \vdots & \vdots & & \vdots & & \vdots \\
x & x & x & \cdots & x & \cdots & c_{p p}
\end{array}\right]\left[\begin{array}{c}
t_{11} \\
t_{21} \\
t_{22} \\
\vdots \\
t_{p 1} \\
\vdots \\
t_{p p}
\end{array}\right]
$$

where $x$ denotes an element, possibly nonzero. Since the matrix of the transformation is triangular, its determinant is the product of the diagonal elements, namely, $\prod_{i=1}^{P} c_{i r}^{i}$. The Jacobian of the transformation from $T$ to $T^{*}$ is the reciprocal of the determinant. The density of $T^{*}$ is obtained by substituting into (6) $t_{n}=t_{i n}^{*} / c_{n}$ and

$$
\begin{aligned}
\sum_{i=1}^{p} \sum_{j=1}^{1} t_{i j}^{2} & =\operatorname{tr} T T^{\prime} \\
& =\operatorname{tr} C^{-1} T^{*} T^{* \prime}\left(C^{-1}\right)^{\prime} \\
& =\operatorname{tr} T^{*} T^{* \prime} C^{\prime-1} C^{-1} \\
& =\operatorname{tr} T^{*} T^{* \prime} \Sigma^{-1}=\operatorname{tr} T^{* \prime} \Sigma^{-1} T^{*}
\end{aligned}
$$

and using $\prod_{t=1}^{p} c_{n}^{2}=|\boldsymbol{C}|\left|\boldsymbol{C}^{\prime}\right|=|\Sigma|$.
Theorem 7.2.1. Let $Z_{1}, \ldots, Z_{n}(n \geq p)$ be independently distributed, each according to $N(\mathbf{0}, \Sigma)$; let $A=\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}$; and let $A=T^{*} T^{* \prime}$, where $t_{i j}^{*}=0$, $i<j$, and $t_{11}^{*}>0$. Then the density of $T^{*}$ is

$$
\frac{\prod_{i=1}^{P} t_{i t}^{* n-t} e^{-\frac{1}{2} 1 \Gamma \Sigma^{-1} T^{*} T^{*}}}{2^{\frac{1}{2} p(n-2)} \pi^{p(p-1) / 4}|\Sigma|^{\frac{1}{2} n} \prod_{i=1}^{P} \Gamma\left[\frac{1}{2}(n+1-i)\right]} .
$$

We can write (4) as $a_{h i}=\sum_{j=1}^{t} t_{h_{j}}^{*} t_{i j}^{*}$ for $h \geq i$. Then

$$
\begin{array}{rlr}
\frac{\partial a_{h i}}{\partial t_{k l}^{*}} & =0, & k>h, \\
& =0, & k=h, l>i ;
\end{array}
$$

that is, $\partial a_{h_{i}} / \partial t_{k l}^{*}=0$ if $k, l$ is beyond $h, i$ in the lexicographic ordering. The Jacobian of the transformation from $A$ to $T^{*}$ is the determinant of the lower triangular matrix with diagonal elements

$$
\begin{array}{ll}
\frac{\partial a_{h h}}{\partial t_{h h}^{*}}=2 t_{h h}^{*} & \\
\frac{\partial a_{h i}}{\partial t_{h i}^{*}}=t_{i t}^{*} & h>i
\end{array}
$$

The Jacobian is therefore $2^{p} \prod_{i=1}^{p} t_{i i}^{* p+1-i}$. The Jacobian of the transformation from $T^{*}$ to $A$ is the reciprocal.

Theorem 7.2.2. Let $Z_{1}, \ldots, Z_{n}$ be independently distributed, each according to $N(\mathbf{0}, \mathbf{\Sigma})$. The density of $A=\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}$ is

$$
\frac{|A|^{\frac{1}{2}(n-p-1)} e^{-\frac{1}{2} \ln \Sigma^{-1} A}}{2^{\frac{1}{2} p n} \pi^{p(p-1) / 4}|\Sigma|^{\frac{1}{2} n} \prod_{i=1}^{p} \Gamma\left[\frac{1}{2}(n+1-i)\right]}
$$

for A positive definite, and 0 otherwise.
Corollary 7.2.2. Let $X_{1}, \ldots, X_{N}(N>p)$ be independently distributed, each according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. Then the density of $\boldsymbol{A}=\sum_{\alpha=1}^{N}\left(\boldsymbol{X}_{\alpha}-\overline{\boldsymbol{X}}\right)\left(\boldsymbol{X}_{\alpha}-\overline{\boldsymbol{X}}\right)^{\prime}$ is (14) for $n=N-1$.

The density (14) will be denoted by $w(A \mid \Sigma, n)$, and the associated distribution will be termed $W(\Sigma, n)$. If $n<p$, then $A$ does not have a density, but its distribution is nevertheless defined, and we shall refer to it as $W(\Sigma, n)$.

Corollary 7.2.3. Let $X_{1}, \ldots, X_{N}(N>p)$ be independently distributed, each according to $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. The distribution of $S=(1 / n) \sum_{\alpha=1}^{N}\left(\boldsymbol{X}_{\alpha}-\overline{\boldsymbol{X}}\right)\left(\boldsymbol{X}_{\alpha}-\overline{\boldsymbol{X}}\right)^{\prime}$ is $W[(1 / n) \Sigma, n]$, where $n=N-1$.

Proof. $S$ has the distribution of $\sum_{\alpha=1}^{n}\left[(1 / \sqrt{n}) Z_{\alpha}\right]\left[(1 / \sqrt{n}) Z_{\alpha}\right]^{\prime}$, where $(1 / \sqrt{n}) Z_{1}, \ldots,(1 / \sqrt{n}) Z_{N}$ are independently distributed, each according to $N(\mathbf{0},(1 / n) \Sigma)$. Theorem 7.2.2 implies this corollary.

The Wishart distribution for $p=2$ as given in Section 4,2,1 was derived by Fisher (1915), The distribution for arbitrary $p$ was obtained by Wishart (1928) by a geometric argument using $v_{1}, \ldots, v_{p}$ defined above. As noted in Section 3.2, the $i$ th diagonal element of $A$ is the squared length of the $i$ th vector, $a_{n}=v_{i}^{\prime} v_{i}=\left\|v_{i}\right\|^{2}$, and the $i, j$ th off-diagonal element of $A$ is the product of the lengths of $v_{t}$ and $v_{t}$ and the cosine of the angle between them. The matrix $A$ specifies the lengths and configuration of the vectors.

We shall give a geometric interpretation ${ }^{\dagger}$ of the derivation of the density of the rectangular coordinates $t_{i j}, i \geq j$, when $\Sigma=I$. The probability element of $t_{11}$ is approximately the probability that $\left\|\boldsymbol{v}_{1}\right\|$ lies in the interval $t_{11}<\left\|\boldsymbol{v}_{1}\right\| <t_{11}+d t_{11}$. This is the probability that $v_{1}$ falls in a spherical shell in $n$ dimensions with inner radius $t_{11}$ and thickness $d t_{11}$. In this region, the density $(2 \pi)^{-\frac{1}{2} n} \exp \left(-\frac{1}{2} v_{1}^{\prime} v_{1}\right)$ is approximately constant, namely, $(2 \pi)^{-\frac{1}{2} n} \exp \left(-\frac{1}{2} t_{11}^{2}\right)$. The surface area of the unit sphere in $n$ dimensions is $C(n)=2 \pi^{\frac{1}{2} n} / \Gamma\left(\frac{1}{2} n\right)$ (Problems 7.1-7.3), and the volume of the spherical shell is approximately $C(n) t_{11}^{n-1} d t_{11}$. The probability element is the product of the volume and approximate density, namely,

$$
2^{-\left(\frac{1}{2} n-1\right)} t_{11}^{n-1} \exp \left(-\frac{1}{2} t_{11}^{2}\right) d t_{11} / \Gamma\left(\frac{1}{2} n\right) .
$$

The probability element of $t_{i 1}, \ldots, t_{\mathrm{t}, i-1}, t_{i i}$ given $v_{1}, \ldots, v_{i-1}$ (i.e., given $\boldsymbol{w}_{1}, \ldots, \boldsymbol{w}_{i-1}$ ) is approximately the probability that $\boldsymbol{v}_{i}$ falls in the region for which $t_{i 1}<v_{i}^{\prime} w_{1} /\left\|w_{1}\right\|<t_{i 1}+d t_{i 1} \ldots, t_{i, i-1}<\nu_{1}^{\prime} w_{i-1} /\left\|w_{i-1}\right\|<t_{i, i-1}+d t_{i, i-1}$, and $t_{i i}<\left\|\boldsymbol{w}_{i}\right\|<t_{i i}-d t_{i i}$, where $\boldsymbol{w}_{i}$ is the projection of $\boldsymbol{v}_{i}$ on the ( $n-i+1$ )dimensional space orthogonal to $w_{1}, \ldots, w_{i-1}$. Each of the first $i-1$ pairs of inequalities defines the region between two hyperplanes (the different pairs being orthogonal). The last pair of inequalities defines a cylindrical shell whose intersection with the ( $i-1$ )-dimensional hyperplane spanned by $v_{1}, \ldots, v_{i-1}$ is a spherical shell in $n-i+1$ dimensions with inner radius $t_{i i}$. In this region the density $(2 \pi)^{-\frac{1}{2} n} \exp \left(-\frac{1}{2} \nu_{i}^{\prime} \nu_{i}\right)$ is approximately constant, namely, $(2 \pi)^{-\frac{1}{2} n} \exp \left(-\frac{1}{2} \Sigma_{j=1}^{t} t_{i j}^{2}\right)$. The volume of the region is approximately $d t_{i 1} \cdots d t_{l, i-1} C(n-i+1) t_{i i}^{n-1} d t_{i i}$. The probability element is

$$
\frac{2^{-\left(\frac{1}{2} n-1\right)} \pi^{-\frac{1}{2}(1-1)} t_{i i}^{n-i} \exp \left(-\frac{1}{2} \sum_{j=1}^{r} t_{i j}^{2}\right)}{\Gamma\left[\frac{1}{2}(n+1-i)\right]} d t_{i 1} \cdots d t_{i i} .
$$

Then the product of (15) and (16) for $i=2, \ldots, p$ is (6) times $d t_{\mathbf{1 1}} \cdots d t_{p p}$.
This aralysis, which exactly parallels the geometric derivation by Wishart [and later by Mahalanobis, Bose, and Roy (1937)], was given by Sverdrup

[^0](1947) [and by Fog (1948) for $p=3$ ]. Another method was used by Madow (1938), who drew on the distribution of correlation coefficients (for $\Sigma=I$ ) obtained by Hotelling by considering certain partial correlation coefficients. Hsu (1939b) gave an inductive proof, and Rasch (1948) gave a method involving the use of a functional equation. A dilierent method is to obtain the characteristic function and invert it, as was done by lngham (1933) and by Wishart and Bartlett (1933).

Cramér (1946) verified that the Wishart distribution has the characteristic function of $\boldsymbol{A}$. By means of alternative matrix transformations Elfving (1947), Mauldon (1955), and Olkin and Roy (1954) derived the Wishart distribution via the Bartlett decomposition; Kshirsagar (1959) based his derivation on random orthogonal transformations. Narain (1948), (1950) and Ogawa (1953) used a regression approach. James (1954), Khatri and Ramachandran (1958), and Khatri (1963) applied different methods. Giri (1977) used invariance. Wishart (1948) surveyed the derivations up to that date. Some of these methods are indicated in the problems.

The relation $\boldsymbol{A}=\boldsymbol{T} \boldsymbol{T}^{\prime}$ is known as the Bartlett decomposition [Bartlett (1939)], and the (nonzero) elements of $T$ were termed rectangular coordinates by Mahalanobis, Bose, and Roy (1937).

## Corollary 7.2.4

$$
\int_{B>0} \ldots \int|B|^{\prime-\frac{1}{2}(p+1)} e^{-1 \Gamma B} d B=\pi^{p(p-1) / 4} \prod_{t=1}^{p} \Gamma\left[t-\frac{1}{2}(i-1)\right] .
$$

Proof. Here $B>0$ denotes $B$ positive definite. Since (14) is a density, its integral for $\boldsymbol{A}>\mathbf{0}$ is 1 . Let $\boldsymbol{\Sigma}=\boldsymbol{I}, \boldsymbol{A}=2 \boldsymbol{B}(d \boldsymbol{A}=2 d \boldsymbol{B})$, and $n=2 t$. Then the fact that the integral is 1 is identical to (17) for $t$ a half integer. However, if we derive (14) from (6), we can let $n$ be any real number greater than $p-1$. In fact (17) holds for complex $t$ such that $R t>p-1$. (. S $t$ means the real part of $t$.) $\square$

Definition 7.2.1. The multivariate gamma function is

$$
\Gamma_{p}(t)=\pi^{p(p-1) / 4} \prod_{t=1}^{p} \Gamma\left[t-\frac{1}{2}(i-1)\right] .
$$

The Wishart density can be written

$$
w(\boldsymbol{A} \mid \boldsymbol{\Sigma}, n)=\frac{|\boldsymbol{A}|^{\frac{1}{2}(n-p-1)} e^{-\frac{1}{2}+r \backslash \prime}}{2^{1 / p n}|\boldsymbol{\Sigma}|^{1 / n} \Gamma_{p}\left(\frac{1}{2} n\right)} .
$$

### 7.3. SOME PROPERTIES OF THE WISHART DISTRIBUTION

### 73.1. The Characteristic Function

The characteristic function of the Wishart distribution can be obtained directly from the distribution of the observations. Suppose $Z_{1}, \ldots, Z_{n}$ are distributed independently, each with density

$$
\frac{1}{(2 \pi)^{\frac{1}{p} p}|\Sigma|^{\frac{1}{3}}} \exp \left(-\frac{1}{2} z^{\prime} \Sigma^{-1} z\right) .
$$

Let

$$
A=\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}
$$

Introduce the $p \times p$ matrix $\Theta=\left(\theta_{i j}\right)$ with $\theta_{i j}=\theta_{j!}$. The characteristic function of $A_{11}, A_{22}, \ldots, A_{p p}, 2 A_{12} 2 A_{13}, \ldots, 2 A_{p-1, p}$ is

$$
\begin{aligned}
\mathscr{E} \exp [i \operatorname{tr}(A \Theta)] & =\mathscr{E} \exp \left(i \operatorname{tr} \sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime} \Theta\right) \\
& =\mathscr{E} \exp \left(i \operatorname{tr} \sum_{\alpha=1}^{n} Z_{\alpha}^{\prime} \Theta Z_{\alpha}\right) \\
& =\mathscr{E} \exp \left(i \sum_{\alpha=1}^{n} Z_{\alpha}^{\prime} \Theta Z_{\alpha}\right)
\end{aligned}
$$

It follows from Lemma 2.6.1 that
(4) $\mathscr{E} \exp \left(i \sum_{\alpha=1}^{n} Z_{\alpha}^{\prime} \Theta Z_{\alpha}\right)=\prod_{\alpha=1}^{n} \mathscr{E} \exp \left(i Z_{\alpha}^{\prime} \Theta Z_{\alpha}\right)=\left[\mathscr{E} \exp \left(i Z^{\prime} \Theta Z\right)\right]^{n}$,
where $Z$ has the density (1). For $\Theta$ real, there is a real nonsingular matrix $B$ such that

$$
\begin{aligned}
B^{\prime} \Sigma^{-1} B & =I \\
B^{\prime} \Theta B & =D
\end{aligned}
$$

where $D$ is a real diagonal matrix (Theorem A.: 2 of the Appendix), If we let $z=B y$, then

$$
\begin{aligned}
\mathscr{E} \exp \left(i Z^{\prime} \Theta Z\right) & =\mathscr{E} \exp \left(i Y^{\prime} D Y\right) \\
& =\mathscr{E} \prod_{l=1}^{p} \exp \left(i d_{\|} Y_{l}^{2}\right) \\
& =\prod_{l=1}^{p} \mathscr{E} \exp \left(i d_{\|} Y_{j}^{2}\right)
\end{aligned}
$$

by Lemma 2.6.2. The $j$ th factor in the second product is $\mathscr{E} \exp \left(i d_{i i} Y_{i}^{2}\right)$, where $Y$, has the distribution $N(0,1)$; this is the characteristic function of the $\chi^{2}$-distribution with one degree of freedom, namely $\left(1-2 i d_{i i}\right)^{-\frac{1}{2}}$ [as can be proved by expanding $\exp \left(i d_{\|} y_{l}^{2}\right)$ in a power series and integrating term by term]. Thus

$$
\mathscr{E} \exp \left(i Z^{\prime} \Theta Z\right)=\prod_{l=1}^{p}\left(1-2 i d_{l l}\right)^{-\frac{1}{2}}=|I-2 i D|^{-\frac{1}{2}}
$$

since $I-2 i D$ is a diagonal matrix. From (5) and (6) we see that

$$
\begin{aligned}
|I-2 i D| & =\left|B^{\prime} \Sigma^{-1} B-2 i B^{\prime} \Theta B\right| \\
& =\left|B^{\prime}\left(\Sigma^{-1}-2 i \Theta\right) B\right| \\
& =\left|B^{\prime}\right| \cdot\left|\Sigma^{-1}-2 i \Theta\right| \cdot|B| \\
& =|B|^{2} \cdot\left|\Sigma^{-1}-2 i \Theta\right|,
\end{aligned}
$$

$\left|B^{\prime}\right| \cdot\left|\Sigma^{-1}\right| \cdot|B|=|I|=1$, and $|B|^{2}=1 /\left|\Sigma^{-1}\right|$. Combining the above results, we obtain

$$
\mathscr{E} \exp [i \operatorname{tr}(A \Theta)]=\frac{\left|\Sigma^{-1}\right|^{\frac{1}{2} n}}{\left|\Sigma^{-1}-2 i \Theta\right|^{\frac{1}{2} n}}=|I-2 i \Theta \Sigma|^{-\frac{1}{2} n} .
$$

It can be shown that the result is valid provided $\left(\mathscr{R}\left(\sigma^{t k}-2 i \theta_{j k}\right)\right)$ is positive definite. In particular, it is true for all real $\Theta$. It also holds for $\Sigma$ singular.

Theorem 7.3.1. If $Z_{1}, \ldots Z_{n}$ are independent, each with distribution $N(\mathbf{0}, \Sigma)$, then the characteristic function of $A_{11}, \ldots, A_{p p}, 2 A_{12}, \ldots, 2 A_{p-1, p}$, where $\left(A_{1,}\right)=A=\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}$, is given by (10).

### 7.3.2 The Sum of Wishart Matrices

Suppose the $A_{t}, i=1,2$, are distributed independently according to $W\left(\Sigma, n_{i}\right)$, respectively. Then $A_{1}$ is distributed as $\sum_{\alpha=1}^{n_{1}} Z_{\alpha} Z_{\alpha}^{\prime}$, and $A_{2}$ is distributed as $\sum_{\alpha=n_{1}+1}^{n_{1}+n_{2}} Z_{\alpha} Z_{\alpha}^{\prime}$, where $Z_{1}, \ldots, Z_{n_{1}+n_{2}}$ are independent, each with distribution $N(\mathbf{0}, \boldsymbol{\Sigma})$. Then $\boldsymbol{A}=\boldsymbol{A}_{1}+\boldsymbol{A}_{2}$ is distributed as $\sum_{\alpha=1}^{n} \boldsymbol{Z}_{\alpha} \boldsymbol{Z}_{\alpha}^{\prime}$, where $n=n_{1}+n_{2}$. Thus $\boldsymbol{A}$ is distributed according to $W(\boldsymbol{\Sigma}, n)$. Similarly, the sum of $q$ matrices distributed independently, each according to a Wishart distribution with covariance $\boldsymbol{\Sigma}$, has a Wishart distribution with covariance matrix $\boldsymbol{\Sigma}$ and number of degrees of freedom equal to the sum of the numbers of degrees of freedom of the component matrices.

Theorem 7.3.2. If $A_{1}, \ldots, A_{q}$ are independently distributed with $A_{1}$ distributed according to $W\left(\Sigma, n_{1}\right)$, then

$$
A=\sum_{i=1}^{q} A_{i}
$$

is distributed according to $W\left(\Sigma, \sum_{1}^{q}=_{1} n_{1}\right)$.

### 7.3.3. A Certain Linear Transformation

We shalt frequently make the transformation

$$
A=C B C^{\prime},
$$

where $\boldsymbol{C}$ is a nonsingular $p \times p$ matrix. If $\boldsymbol{A}$ is distributed according to $W(\boldsymbol{\Sigma}, n)$, then $B$ is distributed according to $W(\boldsymbol{\Phi}, n)$ where

$$
\Phi=C^{-1} \Sigma C^{\prime-1} .
$$

This is proved by the following argument: Let $A=\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}$, where $Z_{1}, \ldots, Z_{n}$ are independently distributed, each according to $N(\mathbf{0}, \mathbf{\Sigma})$. Then $\boldsymbol{Y}_{\alpha}=\boldsymbol{C}^{-1} Z_{\alpha}$ is distributed according to $N(\mathbf{0}, \Phi)$. However,

$$
B=\sum_{\alpha=1}^{n} Y_{\alpha} Y_{\alpha}^{\prime}=C^{-1} \sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime} C^{\prime-1}=C^{-1} A C^{\prime-1}
$$

is distributed according to $W(\boldsymbol{\Phi}, n)$. Finally, $|\partial(A) / \partial(B)|$, the Jacobian of the transformation (12), is

$$
\left|\frac{\partial(\boldsymbol{A})}{\partial(\boldsymbol{B})}\right|=\frac{w(\boldsymbol{B}, \boldsymbol{\Phi}, n)}{w(\boldsymbol{A}, \mathbf{\Sigma}, n)}=\frac{|\boldsymbol{B}|^{\frac{1}{2}\left(n-p^{-1}\right)}|\mathbf{\Sigma}|^{\frac{1}{2} n}}{|\boldsymbol{A}|^{\frac{1}{2}(n-p-1)}|\mathbf{\Phi}|^{\frac{1}{2} n}}=\bmod |\boldsymbol{C}|^{p+1} .
$$

Theorem 7.3.3 The Jacobian of the transformation (12) from $A$ to $B$, where $\boldsymbol{A}$ and $\boldsymbol{B}$ are symmetric, is $\bmod |\boldsymbol{C}|^{p+1}$.

### 7.3.4 Marginal Distribntions

If $\boldsymbol{A}$ is distributed according to $W(\Sigma, n)$, the marginal distribution of any arbitrary set of the elements of $\boldsymbol{A}$ may be awkward to obtain. However, the marginal distribution of some sets of elements can be found easily. We give some of these in the following two theorems.

Theorem 7.3.4. Let $A$ and $\Sigma$ be partitioned into $q$ and $p-q$ rows and columns,

$$
A=\left(\begin{array}{ll}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{array}\right), \quad \Sigma=\left(\begin{array}{ll}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{array}\right) .
$$

If $\boldsymbol{A}$ is distributed according to $W(\Sigma, n)$, then $\boldsymbol{A}_{11}$ is distributed according to $W\left(\Sigma_{11}, n\right)$.

Proof, $A$ is distributed as $\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}$, where the $Z_{\alpha,}$ are independent, each with the distribution $N(\mathbf{0}, \mathbf{\Sigma})$. Partition $\boldsymbol{Z}_{\alpha}$ into subvectors of $q$ and $p-q$ components, $Z_{\alpha}=\left(Z_{\alpha}^{(1) \prime}, Z_{\alpha}^{(2) \prime}\right)^{\prime}$. Then $Z^{(1)}, \ldots, Z_{n}^{(1)}$ are independent, each with the distribution $N\left(0, \Sigma_{11}\right)$, and $A_{11}$ is distributed as $\Sigma_{\alpha=1}^{n} Z_{\alpha}^{(1)} Z_{\alpha}^{(1) \prime}$, which has the distribution $W\left(\Sigma_{11}, n\right)$. $\square$

Theorem 7.3.5. Let $\boldsymbol{A}$ and $\Sigma$ be partitioned into $p_{1}, p_{2}, \ldots, p_{q}$ rows and columns $\left(p_{1}+\cdots+p_{q}=p\right)$,

$$
A=\left(\begin{array}{ccc}
A_{11} & \cdots & A_{1 q} \\
\vdots & & \vdots \\
A_{q 1} & \cdots & A_{q q}
\end{array}\right), \quad \Sigma=\left(\begin{array}{ccc}
\Sigma_{11} & \cdots & \Sigma_{1 q} \\
\vdots & & \vdots \\
\Sigma_{q 1} & \cdots & \Sigma_{q q}
\end{array}\right) .
$$

If $\boldsymbol{\Sigma}_{i j}=\mathbf{0}$ for $i \neq j$ and if $\boldsymbol{A}$ is distributed according to $W(\boldsymbol{\Sigma}, n)$, then $\boldsymbol{A}_{11}, \boldsymbol{A}_{22}, \ldots, \boldsymbol{A}_{\text {qq }}$ are independently distributed and $\boldsymbol{A}_{11}$ is distributed according to $W\left(\boldsymbol{\Sigma}_{i i}, n\right)$.

Proof. $A$ is distributed as $\sum_{\alpha=1}^{n} Z_{\alpha} Z_{\alpha}^{\prime}$, where $Z_{1}, \ldots, Z_{n}$ are independently distributed, each according to $N(\mathbf{0}, \Sigma)$. Let $Z_{\alpha}$ be partitioned

$$
Z_{\alpha}=\left(\begin{array}{c}
Z_{\alpha}^{(1)} \\
\vdots \\
Z_{\alpha}^{(l)}
\end{array}\right)
$$

as $\boldsymbol{A}$ and $\boldsymbol{\Sigma}$ have been partitioned. Since $\boldsymbol{\Sigma}_{i_{f}}=\mathbf{0}$, the sets $Z^{(1)} \ldots$, $Z_{n}^{(1)}, \ldots, Z_{1}^{(q)}, \ldots, Z_{n}^{(q)}$ are independent. Then $A_{11}=\sum_{\alpha=1}^{n} Z_{a}^{(1)} Z_{\alpha}^{(1)!}, \ldots A_{q q}= \sum_{\alpha=1}^{n} Z_{\alpha}^{(q)} Z_{\alpha}^{(q))}$ are independent. The rest ol Theorem 7.3.5 follows from Theorem 7.3.4. $\square$

### 7.3.5. Conditional Distributions

In Section 4.3 we considered estimation of the parameters of the conditional distribution of $\boldsymbol{X}^{(1)}$ given $\boldsymbol{X}^{(2)}=\boldsymbol{x}^{(2)}$. Application of Theorem 7.2.2 to Theorem 4.3 .3 yields the following theorem:

Theorem 7.3.6. Let $A$ and $\Sigma$ be partitioned into $q$ and $p-q$ rows and columis as in (16). If $A$ is distributed according to $W(\Sigma, n)$, the distribution of $A_{11 \cdot 2}=A_{11}-A_{12} A_{22}^{-1} A_{21}$ is $W\left(\Sigma_{11 \cdot 2}, n-p+q\right), n \geq p-q$.

Note that Theorem 7.3.6 implies that $A_{11 \cdot 2}$ is independent of $A_{22}$ and $A_{12} A_{22}^{-1}$ regardless of $\Sigma$.

### 7.4. COCHRAN'S THEOREM

Cochran's theorem [Cochran (1934)] is useful in proving that certain vector quadratic forms are distributed as sums of vector squares. It is a statistical statement of an algebraic theorem, which we shall give as a lemma.

Lemma 7.4.1. If the $N \times N$ symmetric matrix $C_{1}$ has rank $r_{i}, i=1, \ldots, m$, and

$$
\sum_{i=1}^{m} C_{i}=I_{N}
$$

then

$$
\sum_{i=1}^{m} r_{i}=N
$$

is a necessary and sufficient condition for there to exist an $N \times N$ orthogonal matrix $\boldsymbol{P}$ such that for $i=1, \ldots, m$

$$
P C_{1} P^{\prime}=\left(\begin{array}{ccc}
0 & 0 & 0 \\
0 & I & 0 \\
0 & 0 & 0
\end{array}\right)
$$

where $I$ is of order $r_{1}$, the upper left-hand $\mathbf{0}$ is square of order $\sum_{j=1}^{i-1} r_{j}$ (which is vacuous for $i=1$ ), and the lower-right hand $\mathbf{0}$ is square of order $\sum_{j=i+1}^{m} r_{j}$ (which is vacuous for $i=m$ ).

Proof. The necessity follows from the fact that (1) implies that the sum of (3) over $i=1 \quad m$ is $I_{S}$ Now let us.prove the sufficiency we assume (2)


[^0]:    ${ }^{\dagger}$ In the first edition of this book, the derivation of the Wishart distribution and its geometric Interpretation were in terms of the nonorthogonal vectors $v_{1}, \ldots, v_{p}$.























































































Anderson, T. W., and Yasuo Amemiya (1988b), Asymptotic distributions in factor analysis and linear structural relations, Proceedings of the International Conference on Advances in Multivariate Statistical Analysis (S. Das Gupta and J. K. Ghosh, eds.), Indian Statistical Institute. Calcutta, 1-22. [14.6]
Anderson, T. W., and R. R. Bahadur (1962), Classification into two multivariate normal distributions with different covariance matrices, Annals of Mathematical Statistics. 33, 420-431. [6.10]
Anderson. T. W., and Kai-Tai Fang (1990a), On the theory of multivariate elliptically contoured distributions and their applications, Statistical Inference in Elliptically Contoured and Related Distributions (Kai-Tai Fang and T. W. Anderson, eds.), Allerton Press, Inc., New York, 1-23. [4.5]
Anderson. T. W., and Kai-Tai Fang (1990b), Inference in multivariate elliptically contoured distributions based on maximum likelihood, Statistical Inference in Elliptically Contoured and Related Distributions (Kai-Tai Fang and T. W. Anderson. eds.). Allerton Press, Inc., New York, 201-216. [3.6]
Anderson. T. W., and Kai-Tai Fang (1992), Theory and applications of elliptically contoured and related distributions, The Development of Statistics: Recent Contriburions from China (X. R. Chen, K. T. Fang, and C. C. Yang, eds.), Longman Scientific and Technical, Harlow, Essex, 41-62. [10.11]
Anderson, T. W., Kai-Tai Fang, and Huang Hsu (1986), Maximum likelihood estimates and likelihood-ratio criteria for multivariate elliptically contoured distributions, Canadian Journal of Statistics, 14, 55-59. [Reprinted in Statistical Inference in Elliptically Contoured and Related Distributions (Kai-Tai Fang and T. W. Anderson, eds.), Allerton Press, Inc., New York, 1990, 217-223. [3.6]
Anderson. T. W., Somesh Das Gupta, and George P. H. Styan (1972), A Bibliography of Multivariate Statistical Analysis, Oliver \& Boyd, Edinburgh. (Reprinted by Robert E. Krieger, Malabar, Florida, 1977.) [Preface]
Anderson, T. W., Naoto Kunitomo, and Takamitsu Sawa (1983a), Evaluation of the distribution function of the limited information maximum likelihood estimator, Econometrica, 50, 1009-1027. [12.7]
Anderson, T. W., Naoto Kunitomo, and Takamitsu Sawa (1983b), Comparison of the densities of the TSLS and LIMLK estimators, Global Econometrics, Essays in Honor of Lawrence R. Klein (F. Gerard Adams and Bert Hickman, eds.), MIT, Cambridge, MA, 103-124. [12.7]
Anderson. T. W., and I. Olkin (1985), Maximum likelibood estimation of the parameters of a multivariate normal distribution, Linear Algebra and Its Applications, 70, 147-171. [3.2]
Anderson, T. W., and Michael D. Perlman (1987), Consistency of invariant tests for the multivariate analysis of variance, Proceedings of the Second International Tampere Conference in Statistics (Tarmo Pukkila and Simo Puntaner, eds.), Tampere, Finland, 225-243. [8.10]
Anderson, T. W., and Michael D. Perlman (1993), Parameter consistency of invariant tests for MANOVA and related multivariate hypotheses, Statistics and Probability: A Raghu Raj Bahadur Festschift (J. K. Ghosh, S. K. Mitra, K. R. Parthasarathy, and B. L. S. Prakasa Rao, eds.), Wiley Eastern Limited, 37-62. [8.10]

Anderson, T. W., and Herman Rubin (1949), Estimation of the parameters of a single equation in a complete system of stochastic equations, Annals of Mathematical Statistics, 20, 46-63. [Reprinted in Readings in Econometric Theory (J. Malcolm Dowling and Fred R. Glahe, eds.), Colorado Associated University, 1970, 358-375.] [12.8]
Anderson, T. W., and Herman Rubin (1950), The asymptotic properties of estimates of the parameters of a single equation in a complete system of stochastic equations, Annals of Mathematical Statistics, 21, 570-582. [Reprinted in Readings in Economerric Theory (J. Malcolm Dowling and Fred R. Glahe, eds.), Colorado Associated University, 1970, 376-388.] [12.8]
Anderson, T. W., and Herman Rubin (1956), Statistical inference in factor analysis, Proceedings of the Third Berkeley Symposium on Mathematical Statistics and Probability (Jerzy Ncyman, ed.), Vol. V, University of California, Berkeley and Los Angeles, 111-150. [14.2, 14.3, 14.4, 14.6]
Anderson, T. W., and Takamitsu Sawa (1973), Distributions of estimates of coefficients of a single equation in a simultaneous system and their asymptotic expansions, Econometrica, 41, 683-714. [12.7]
Anderson, T. W., and Takamitsu Sawa (1977), Tables of the distribution of the maximum likelihood estimate of the slope coefficient and approximations, Technical Report No. 234, Economics Series, Institute for Mathematical Studies in the Social Sciences, Stanford University, April. [12.7]
Anderson, T. W., and Takamitsu Sawa (1979), Evaluation of the distribution function of the two-stage least squares estimate, Econometrica, 47, 163-182. [12.7]
Anderson, T. W., and Takamitsu Sawa (1982), Exact and approximate distributions of the maximum likelihood estimator of a slope coefficient, Joumal of the Royal Statistical Society B, 44, 52-62. [12.7]
Anderson, T. W., and George P. H. Styan (1982), Cochran's theorem, rank additivity and tripotent matrices, Statistics and Probability: Essays in Honor of C. R. Rao (G. Kallianpur, P. R. Krishmaiah, and J. K. Ghosh, eds.), North-Holland, Amsterdam, 1-23. [7.4]
Anderson, T. W., and Akimichi Takemura (1982), A new proof of admissibility of tests in multivariate analysis, Journal of Multivariate Analysis, 12, 457-468. [8.10]
Andersson, Steen A., David Madigan, and Michael D. Perlman (2001), Alternative Markov properties for chain graphs, Scandinauian Joumal of Statistics, 28, 33-85. [15.2]
Barnard, M. M. (1935), The secular variations of skull characters in four series of Egyptian skulls, Annals of Eugenics, 6, 352-371. [8.8]
Barndorff-Nielson, O. E. (1978), Information and Exponential Families in Statistical Theory, John Wiley \& Sons, New York. [15.5]
Barnes, E. W. (1899), The theory of the gamma function, Messenger of Mathematics, 29, 64-129. [8.5]
Bartlett, M. S. (1934), The vector representation of a sample, Proceedings of the Cambridge Philosophical Society, 30, 327-340. [8.3]
Bartlett, M. S. (1937a), Properties of sufficiency and statistical tests, Proceedings of the Royal Society of London A, 160, 268-282. [10.2]

Bartlett, M. S. (1937b), The statistical conception of mental factors, British Joumal of Psychology, 28, 97-104. [14.7]
Bartlett, M. S. (1938), Further aspects of the theory of multiple regression, Proceedings of the Cambridge Philosophical Society, 34, 33-40. [14.7]
Bartlett, M. S. (1939), A note on tests of significance in multivariate analysis, Proceedings of the Cambridge Philosophical Society, 35, 180-185. [7.2, 8.6]
Bartlett, M. S. (1947), Multivariate analysis, Joumal of the Royal Statistical Society, Supplement, 9, 176-197. [8.8]
Bartlett, M. S. (1950), Tests of significance in factor analysis, British Journal of Psychology (Statistics Section), 3, 77-85. [14.3]
Basmann, R. L. (1957), A generalized classical method of linear estimation of coefficients in a structural equation, Econometrica, 25, 77-83. [12.8]
Basmann, R. L. (1961), A note on the exact finite sample frequency functions of generalized classical linear estimators in two leading overidentified cases, Journal of the American Statistical Association, 56, 619-636. [12.8]
Basmann, R. L. (1963), A note on the exact finite sample frequency functions of generalized classical linear estimators in a leading three-equation case, Journal of the American Statistical Association, 58, 161-171. [12.8]
Bennett, B. M. (1951), Note on a solution of the generalized Behrens-Fisher problem, Annals of the Institute of Statistical Mathematics, 2, 87-90. [5.5]
Berger, J. O. (1975), Minimax estimation of location vectors for a wide class of densities, Annals of Statistics, 3, 1318-1328. [3.5]
Berger, J. O. (1976), Admissibility results for generalized Bayes estimators of coordinates of a location vector, Annals of Statistics, 4, 334-356. [3.5]
Berger, J. O. (1980a), A robust generalized Bayes estimator and confidence region for a multivariate normal mean, Annals of Statistics, 8, 716-761. [3.5]
Berger, J. O. (1980b), Statistical Decision Theory, Foundations, Concepts and Methods, Springer-Verlag, New York. [3.4, 6.2, 6.7]
Berndt, Ernst R., and Eugene Savin (1977), Conflict among criteria for testing hypotheses in the multivariate linear regression model, Econometrica, 45, 1263-1277. [8.6]
Bhattacharya, P. K. (1966), Estimating the mean of a multivariate normal population with general quadratic loss function, Annals of Mathematical Statistics, 37, 1819-1824. [3.5]
Bimbaum, Allan (1955), Characterizations of complete classes of tests of some multiparametric hypotheses, with applications to likelihood ratio tests, Annals of Mathematical Statistics, 26, 21-36. [5.6, 8.10]
Björck, A., and G. Golub (1973), Numerical methods for computing angles between linear subspaces, Mathematics of Computation, 27, 579-594. [12.3]
Blackwell, David, and M. A. Girshick (1954), Theory of Games and Statistical Decisions, John Wiley \& Sons, New York. [6.2, 6.7]
Blalock, H. M., Jr (ed.) (1971), Causal Models in the So:ial Sciences, Aldine-Atheston, Chicago. [15.1]
Bonnescn, T., and W. Fenchel (1948), Theorie der Konvexen Körper, Chelsea, New York. [8.10]



Bose, R. C. (1936a), On the exact distribution and moment-coefficients of the $D^{2}$-statistic, Sankyā, 2, 143-154. [3.3]
Bose, R. C. (1936b), A note on the distribution of differences in mean values of two samples drawn from two multivariate normally distributed populations, and the definition of the $D^{2}$-statistic, Sankhyā, 2, 379-384. [3.3]
Bose, R. C., and S. N. Roy (1938), The distribution of the studentised $D^{2}$-statistic. Sankhyā, 4, 19-38. [5.4]
Bowker, A. H. (1960), A representation of Hotelling's $T^{2}$ and Anderson's classification statistic $W$ in terms of simple statistics, Contributions to Probability and Statistics (I. Olkin, S. G. Ghurye, W. Hoeffding, W. G. Madow and H. B. Mann. eds.), Stanford University, Stanford, California, 142-149. [5.2]
Bowker, A. H., and R. Stigreaves (1961), An asymptotic expansion for the distribution function of the $W$-classification statistic, Studies in Irem Analysis and Prediction (Herbert Solomon, ed.), Stanford University, Stanford, California, 293-310. [6.6]
Box, G. E. P. (1949), A general distribution theory for a class of likelihood criteria, Biometrika, 36, 317-346. [8.5, 9.4, 10.4, 10.5]
Bravais, Auguste (1846), Analyse mathématique sur les probabilités des erreurs de situation d'un point, Mémoires Présentés par Divers Savants à l'Académie Royale des Sciences de l'Institut de France, 9, 255-332. [1.2]
Brown, G. W. (1939), On the power of the $L_{1}$ test for equality of several variances, Annals of Mathematical Statistics, 10, 119-128. [10.2]
Browne, M. W. (1974), Generalized least squares estimates in the analysis of covariance structures, South African Statistical Journal, 8, 1-24. [14.3]
Chambers, Juhn M. (1977), Computational Methods for Data Anaţsis, John Wilev \& Sons, New York. [12.3]
Chan, Tony F., Gene H. Golub, and Randall J. LeVeque (1981), Algorithms for computing the sample variance: analysis and recommendations, unpublished. [3.2]
Chernoff, Herman (1956), Large sample theory: parametric case, Amals of Mathematical Statistics, 27, 1-22. [8.6]
Chernoff, Herman, and N. Divinsky (1953), The computation of maximum likelihood estimates of linear structural equations, Studies in Econometric Method (W. C. Hood and T. C. Koopmans, eds.), John Wiley \& Sons, Inc., New York. [12.8]
Chu, S. Sylvia, and K. C. S. Pillai (1979), Power comparisons of two-sided tests of equality of two covariance matrices based on six criteria. Annals of the Institute of Statistical Mathematics, 31, 185-205. [10.6]
Chung, Kai Lai (1974), A Course in Probability Theory, 2nd ed., Academic. New York. [2.2]
Clemm, D. S., P. R. Krishnaiah, and V. B. Waikar (1973). Tables for the extreme roots of the Wishart matrix, Journal of Statistical Computation and Simulation. 2. 65-92. [10.8]
Clunies-Ross, C. W., and R. H. Riffenburgh (1960), Geometry and linear discrimination, Biometrika, 47, 185-189. [6.10]
Cochran, W. G. (1934), The distribution of quadratic forms in a normal systeni. with applications to the analysis of covariance, Proceedings of the Cambridge Philosophical Society, 30, 178-191. [7.4]

Constantine, A. G. (1963), Some non-central distribution problems in multivariate analysis. Annals of Mathematical Statistics, 34, 1270-1285. [12.4]
Constantine. A. G. (1960). The distribution of Hotelling's generalised $T_{11}^{2}$. Annals of Mathematical Statistics, 37, 215-225. [8.6]
Consul. P. C. (1966). On the exact distributions of the likelihood ratio criteria for testing linear hypotheses about regression coefficients, Annals of Mathematical Statistics. 37, 1319-1330. [8.4]
Consul. P. C. (1967a), On the exact distributions of likelihcod ratio criteria for testing independence of sets of variates under the null hypotliesis, Annals of Mathematical Staristics, 38, 1160-1169. [9.3]
Consul, P. C. (1967b), On the exact distributions of the criterion $W$ for testing sphericity and in a $p$-variate normal distribution, Annals of Mathematical Statistics, 38, 1170-1174. [10.7]
Courant. R., and D. Hilbert (1953), Methods of Mathematical Physics, Interscience, New York. [9.10]
Cox. D. R., and N. Wermuth (1996), Multivariate Dependencies, Chapman and Hall, London. [15.1]
Cramér. H. (1946). Mathematical Methods of Statistics, Princeton University, Princeton. [2.6. 3.2, 3.4, 6.5, 7.2]
Dahm. P. Fred, and Wayne A. Fuller (1981), Generalized least squares estimation of the functional multivariate linear errors in variables model, unpublished. [14.3]
Daly. J. F. (1940), On the unbiased character of likelihood-ratio tests for independence in normal systems, Annals of Mathematical Statistics, 11, 1-32. [9.2]
Darlington. R. B., S. L. Weinberg, and H. J. Walberg (1973), Canonical variate analysis and related techniques, Review of Educational Research, 43, 433-454. [12.2]
Das Gupta. Somesh (1965), Optimum classification rules for classification into two multivariate normal populations, Annals of Mathematical Statistics, 36, 1174-1184. [6.6]
Das Gupta. S., T. W. Anderson, and G. S. Mudholkar (1964), Monotonicity of the power functions of some tests of the multivariate linear hypothesis, Annals of Mathematical Statistics, 35, 200-205. [8.10]
David, F. N. (1937), A note on unbiased limits for the correlation coefficient, Biometrika. 29, 157-160. [4.2]
David. F. N. (1938). Tables of the Ordinates and Probability Integral of the Distribution of the Correlation Coefficient in Small Samples, Cambridge University, Cambridge. [4.2]
Davis, A. W. (1968). A system of linear differential equations for the distribution of Hotelling's generalized $T_{0}^{2}$, Annals of Mathematical Statistics, 39, 815-832. [8.6]
Davis, A. W. (1970a), Exact distributions of Hotelling's generalized $T_{0}^{2}$, Biometrika, 57. 187-191. [Preface, 8.6]

Davis, A. W. (1970b), Further applications of a differential equation for Hotelling's generalized $T_{0}^{2}$, Annals of the Institute of Statistical Mathematics, 22, 77-87. [Preface. 8.6]
Davis, A. W. (1971), Percentile approximations for a class of likelihood ratio criteria, Biometrika, 58. 349-356. [10.8, 10.9]

Davis, A. W. (1972a), On the marginal distributions of the latent roots of the multivariate beta matrix, Annals of Mathematical Statistics, 43, 1664-1670. [8.6]
Davis, A. W. (1972b), On the distributions of the latent roots and traces of certain random matrices, Journal of Multivariate Analysis, 2, 189-200. [8.6]
Davis, A. W. (1980), Further tabulation of Hotelling's generalized $T_{0}^{2}$, Communications in Statistics, B9, 321-336. [Preface, 8.6]
Davis, A. W., and J. B. F. Field (1971), Tables of some multivariate test criteria, Technical Report No. 32, Division of Mathematical Statistics, C.S.I.R.O., Canberra, Australia. [10.8]
Davis, Harold T. (1933), Tables of the Higher Mathematical Functions, Vol. I, Principia Press, Bloomington, Indiana. [8.5]
Davis, Harold T, (1935), Tables of the Higher Mathematical Functions, Vol. II, Principia Press, Bloomington, Indiana. [8.5]
Deemer, Walter L., and Ingram Olkín (195I), The Jacobians of certain matrix transformations useful in multivariate analysis. Based on lectures of P. L. Hsu at the University of North Carolina, 1947, Biometrika, 38, 345-367, [13.2]
De Groot, Morris H. (1970), Optimal Statistical Decisions, McGraw-Hill, New York. [3.4, 6.2, 6.7]
Dempster, A. P. (1972), Covariance selection, Biometrics, 28, 157-175. [15.5]
Dempster, A. P., N. M. Laird, and D. B. Rubin (1977), Maximum likelihood from incomplete data vía the EM algorithm (with discussion), Joumal of the Royal Statistical Society B, 39, 1-38. [14.3]
Diaconis, Persi, and Bradley Efron (1983), Computer-intensive methods in statistics, Scientific American, 248, 116-130. [4.3]
Eaton, M. L., and M. D. Perlman (1974), A monotonicity property of the power functions of some invariant fests for MANOVA, Annals of Statistics, 2, 1022-1028. [8.10]
Edwards, D. (1995), Introduction to Graphical Modelling, Springer-Verlag, New York. [15.1]
Efron, Bradley (1982), The Jackknife, the Bootstrap, and Other Resampling Plars, Society for Industrial and Applied Mathematics, Philadelphia. [4.2]
Efron, Bradley, and Carl Morris (1977), Stein's paradox in statistics, Scientific American, 236, 119-127. [3.5]
Elfving, G. (1947), A simple method of deducing certain distributions connected with multivariate sampling, Skandinavisk Aktuarietidskrift, 30, 56-74. [7.2]
Fang, Kai-Tai, Samuel Kotz, and Kai-Wang Ng (1990), Symmetric Multivariate and Related Distributions, Chapman and Hall, New York. [2.7]
Fang, Kai-Tai, and Yaó-Ting Zhang (1990), Generalized Multivariate Analysis, Springer-Verlag, New York. [2.7, 3.6, 10.11, 7.9]
Ferguson, Thomas Shelburne (1967), Mathematical Statistics: A Decision Theoretic Approach, Academic, New York. [3.4, 6.2, 6.7]
Fisher, R. A. (1915), Frequency distribution of the values of the correlation coefficient in samples from an indefinitely large population, Biometrika, 10, 507-521. [4.2, 7.2]
Fisher, R. A. (1921), On the "probable error" of a coefficient of correlation deduced from a small sample, Metron, 1, Part 4, 3-32. [4.2]

Fisher, R. A. (1924), The distribution of the partial correlation coefficient, Metron, 3, 329-332. [4.3]
Fisher, R. A. (1928), The general sampling distribution of the multiple correlation coefficient, Proceedings of the Royal Society of London, A, 121, 654-673. [4.4]
Fisher, R. A. (1936), The use of multiple measurements in taxonomic problems, Annals of Eugenics, 7, 179-188. [5.3, 6.5, 11.5]
Fisher, R. A. (1939), The sampling distribution of some statistics obtained from non-Innear equations, Annals of Eugenics, 9, 238-249. [13.2]
Fisher, R A. (1947a), The Design of Experiments (4th ed.), Oliver and Boyd, Edinturgh. [8.9]
Fisher, R. A. (1947b), The analysis of covariance method for the relation between a part and the whole, Biomerrics, 3, 65-68. [3.P]
Fisher, R. A., and F. Yates (1942), Statistical Tables for Biological, Agricultural and Medical Research (2nd ed.), Oliver and Boyd, Edinburgh. [4.2]
Fog, David (1948), The geometrical method in the theory of sampling, Biometrika, 35, 46-54. [7.2]
Foster, F. G. (1957), Upper percentage points of the generalized beta d'stribution, II, Biometrika, 44, 441-453. [8.6]
Foster, F. G. (1958), Upper percentage points of the generalized beta distribution, III, Biometrika, 45, 492-503. [8.6]
Foster, F. G., and D. H. Rees (1957), Upper percentage points of the generalized beta distribution, I, Biometrika, 44, 237-247. [8.6]
Frets, G. P. (1921), Heredity of head form in man, Genetica, 3, 193-384. [3.P]
Frisch, R. (1929), Correlation and scatter in statistical variables, Nordic Statistical Journal, 8, 36-102. [7.5]
Frydenberg, M. (1990), The chain graph Markov property, Scandinavian Journal of Statistics, 17, 333-353. [15.2]
Fujikoshi, Y. (1973), Monotonicity of the power functions of some tests in general MANOVA models, Annals of Statistics, 1, 388-391. [8.6]
Fujikoshi, Y. (1974), The likelihood ratio tests for the dimensionality of regression coefficients, Journal of Multivariate Analysis, 4, 327-340. [12.4]
Fujikoshi, Y., and M. Kanazawa (1976), The ML classification statistic in covariate discriminant analysis and its asymptotic expansions, Essays in Probability and Statistics, 305-320. [6.6]
Fuller, Wayne A., Sastry, G. Pantula, and Yasuo Amemiya (1982), The covariance matrix of estimators for the factor model, unpublished. [14.4]
Gabriel, K. R. (1969), Simultaneous test procedures-some theory of multiple comparisons, Annals of Mathematical Statistics, 40, 224-250. [8.7]
Gajjar, A. V. (1967), Limiting distributions of certain transformations of multiple correlation coefficients, Metron, 26, 189-193. [4.4]
Galton, Francis (1889), Natural Inheritance, MacMillan, London. [1.2, 2.5]
Gauss, K. F. (1823), Theory of the Combination of Observations, Göttingen. [1.2]
Giri. N. (1977), Multivariate Statistical Inference, Academic, New York. [7.2, 7.7]
Giri, N., and J. Kiefer (1964), Local and asymptotic minimax properties of multivariate tests, Annals of Mathematical Statistics, 35, 21-35. [5.6]

Giri, N., J. Kiefer, and C. Stein (1963), Minimax character of Hotelling's $T^{2}$ test in the simplest case, Annals of Mathematical Statistics, 34, 1524-1535. [5.6]
Girshick, M. A. (1939), On the sampling theory of roots of determinantal equations. Annals of Mathematical Statistics, 10, 203-224. [13.2]
Gleser, Leon Jay (1981), Estimation in a multivariate "errors in variables" regression model: large sample results, Annals of Statistics, 9, 24-44. [12.7]
Glynn, W. J., and R. J. Muirhead (1978), Inference in canonical correlation analysis. Journal of Multivariate Analysis, 8, 468-478. [12.4]
Golub, Gene H., and Franklin T. Luk (1976), Singular value decomposition: applications and computations, unpublished. [12.3]
Golub, Gene H., and Charles F. Van Loan (1989), Matrix Computations (2nd ed.). Johns Hopkins University Press, Baltimore. [11.4, 12.3, A.5]
Grubbs, F. E. (1954), Tables of 1\% and 5\% probability levels of Hotellings generalized $T^{2}$ statistics, Technical Note No. 926, Ballistic Research Laboratory. Aberdeen Proving Ground, Maryland. [8.6]
Gupta, Shanti S. (1963), Bibliography on the multivariate normal integrals and related topics, Annals of Mathematical Statistics, 34, 829-838. [2.3]
Gurland, John (1968), A relatively simple form of the distribution of the multiple correlation coefficient, Journal of the Royal Statistical Society B, 30.276-283. [4.4]
Gurland, J., and R. Milton (1970), Further consideration of the distribution of the multiple correlation coefficient, Journal of the Royal Statistical Society B. 32. 381-394. [4.4]
Haavelmo, T. (1944), The probability approach in econometrics, Econometrica, 12. Supplement, 1-118. [12.7]
Haff, L. R. (1980), Empirical Bayes estimation of the multivariate normal covariance matrix, Annals of Statistics, 8, 586-597. [7.8]
Halmos, P. R. (1950), Measure Theory, D. van Nostrand. New York. [4.5. 13.3]
Harris, Bernard, and Andrew P, Soms (1980). The use of the tetrachoric series for evaluating multivariate pormal probabilities, Journal of Multivariate Analysis, 10. 252-267. [2.3]
Hayakawa, Takesi (1967), On the distribution of the maximum latent root of a positive definite symmetric random matrix, Annals of the Institute of Staristical Mathematics, 19, 1-17. [8.6]
Heck, D. L. (1960), Charts of some upper percentage points of the distribution of the largest characteristic root, Annals of Mathematical Statistics, 31, 625-642. [8.6]
Hickman, W. Braddock (1953), The Volume of Corporate Bond Financing Since 1900. Princeton University, Princeton, 82-90. [10.7]
Hoel, Paul G. (1937), A significance test for component analysis, Annals of Mathematical Statistics, 8, 149-158. [7.5]
Hooker, R. H. (1907), The correlation of the weather and crops, Joumal of the Royal Statistical Society, 70, 1-42. [4,2]
Hotelling, Harold (1931), The generalization of Student's ratio. Annals of Mathemarical Statistics, 2, 360-378. [5.1, 5.P]
Hotelling, Harold (1933), Analysis of a complex of statistical variables into principal components, Journal of Educational Psychology, 24, 417-441. 498-520. [11.1, 14.3]

Hotelling. Harold (1935), The most predictable criterion, Journal of Educational Psychologr. 26. 139-142. [12.2]
Hotelling, Harold (1936), Relations between two sets of variates, Biometrika, 28, 321-377. [12.1]
Hotelling. Harold (1947). Multivariate quality control, illustrated by the air testing of sample bombsights. Techniques of Statistical Analysis (C. Eisenhart, M. Hastay, and W. A. Wallis, eds.). McGraw-Hill, New York, III-184. [8.6]
Hotelling. Harold (1951), A generalized $T$ test and measure of multivariate dispersion. Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability (Jerzy Neyman. ed.), University of California, Los Angeles and Berkeley. 23-41. [8.6, 10.7]
Hotelling, Harold (1953). New light on the correlation coefficient and its transforms (with discussion), Journal of the Royal Statistical Society B, 15, 193-232, [4,2]
Howe. W. G. (1955). Some Contributions to Factor Analysis, U.S. Atomic Energy Commission Report. Oak Ridge National Laboratory, Oak Ridge, Tennessee. [14.2, 14.6]
Hsu. P. L. (1938). Notes on Hotellings generalized T, Annals of Nathematical Statistics. 9. 231-243. [5.4]
1Hsu. P. L. (1939a), On the distribution of the roots of certuin determinantal equations, Annals of Eugenics, 9, 250-258. [13.2]
Hsu. P. L. (1939b), A new proof of the joint product moment distribution, Proceedings of the Cambridge Philosophical Society, 35, 336-338. [7.2]
Hsu, P. L. (1945), On the power functions for the $E^{2}$-test and the $T^{2}$-test, Annals of Mathematical Statistics, 16, 278-286. [5.6]
Hudson. M. (1974), Empirical Bayes estimation, Technical Report No. 58, NSF contract GP 30711X-2, Department of Statistics, Stanford University. [3.5]
Immer, F. R.. H. D. Hayes, and LeRoy Powers (1934), Statistical determination of barley varietal adaptation, Journal of the American Society of Agronomy, 26, 403-407. [8.9]
Ingham, A. E. (1933), An integral which occurs in statistics, Proceedings of the Cambridge Philosophical Society, 29, 271-276. [7.2]
Ito, K. (1956), Asymptotic formulae for the distribution of Hotelling's generalized $T_{0}^{2}$ statistic, Annals of Mathematical Statistics, 27, 1091-1105. [8.6]
1to. K. (1960), Asymptotic formulae for the distribution of Hotelling's generalized $T_{0}^{2}$ statistic, 11, Annals of Mathematical Statistics, 31, 1148-1153, [8,6]
Izenman, A. J. (1975), Reduced-rank regression for the multivariate linear model, Joutrnal of Multivariate Analysis, 5, 248-264. [12.7]
Izenman, Alan Julian (1980), Assessing dimensionality in multivariate regression, Analysis of Variance, Handbook of Statistics, Vol. 1 (P. R. Krishnaiah, ed.), North-Holland. Amsterdam, 571-591. [3.P]
James, A. T. (1954), Normal multivariate analysis and the orthogonal group, Annals of Mathematical Statistics, 25, 40-75. [7.2]
James, A. T. (1964), Distributions of matrix variates and latent roots derived from normal samples, Annals of Mathematical Statistics, 35, 475-501. [8.6]

James, W., and C. Stein (1961), Estimation with quadratic loss, Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability (Jerzy Neyman, ed.), Vol. I, 361-379. University of California, Berkeley. [3.5, 7.8]
Japanese Standards Association (1972). Statistical Tables and Formulas with Computer Applications. [Preface]
Jennrich, Robert I., and Dorothy T. Thayer (1973), A note on Lawley's formulas for standard errors in maximum likelihood factor analysis, Psychometrika, 38, 571-580. [14.3]
Johansen, S. (1995), Likelihood-based Inference in Cointegrated Vector Autoregressive Models, Oxford University Press. [12.7]
Jolicoeur, Pierre, and J. E. Mosimann (1960), Size and shape variation in the painted turtle, a principal component analysis, Growth, 24, 339-354. Also in Benchmark Papers in Systematic and Evolutionary Biology (E. H. Bryant and W. R. Atchley, eds.), 2 (1975), 86-101. [11.P]
Jöreskog, K. G. (1969) A general approach to confirmatory maximum likelihood factor analysis, Psychometrika, 34, 183-202. [14.2]
Jöreskog, K. G., and Arthur S. Goldberger (1972), Factor analysis by generalized least squares, Psychometrika, 37, 243-260. [14.3]
Kaiser, Henry F. (1958), The varimax criterion for analytic rotation in factor analysis, Psychometrika, 23, 187-200. [14.5]
Kanazawa, M. (1979), The asymptotic cut-off point and comparison of error probabilities in covariate discriminant analysis, Journal of the Japan Statistical Society, 9, 7-17. [6.6]
Kelley, T. L. (1928), Crossroads in the Mind of Man, Stanford University, Stanford. [4.P, 9.P]
Kendall, M. G., and Alan Stuart (1973), The Advanced Theory of Statistics (3rd ed.), Vol. 2, Charles Griffin, London. [12.6]
Kennedy, William J., Jr., and James E. Gentle (1980), Statistical Computing, Marcel Dekker, New York. [12.3]
Khatri, C. G. (1963), Joint estimation of the parameters of multivariate normal populations, Joumal of Indian Statistical Association, 1, 125-133. [7.2]
Khatri, C. G. (1966), A note on a large sample distribution of a transformed multiple correlation coefficient, Annals of the Institute of Statistical Mathematics, 18, 375-380. [4.4]
Khatri, C. G. (1972), On the exact finite series distribution of the smallest or the largest root of matrices in three situations, Journal of Multivariate Analysis, 2, 201-207. [8.6]
Khatri, C. G., and K. C. Sreedharan Pillai (1966), On the moments of the trace of a matrix and approximations to its non-central distribution, Annals of Mathematical Statistics, 37, 1312-1318. [8.6]
Khatri, C. G., and K. C. S. Pillai (1968), On the non-central distributions of two test criteria in multivariate analysis of variance, Annals of Mathematical Statistics, 39, 215-226. [8.6]
Khatri, C. G., and K. V. Ramachandran (1958), Certain multivariate distribution problems, I (Wishart's distribution), Journal of the Maharaja Sayajairo, University of Baroda, 7, 79-82. [7.2]

Kiefer, J. (1957), Invariance, minimax sequential estimation, and continuous time processes, Annals of Mathematical Statistics, 28, 573-601. [7.8]
Kiefer, J. (1966), Multivariate optimality results, Multivariate Analysis (Parachuyi R. Krishnajah, ed.), Academic, New York, 255-274. [7.8]
Kiefer, J., and R. Schwartz (1965), Admissible Bayes character of $T^{2}-R^{2}$-, and other fully invariant tests for classical multivariate normal problems, Annals of Mathematical Statistics, 36, 747-770. [5.P, 9.9, 10.10]
Klotz, Jerome, and Joseph Putter (1969), Maximum likelihood estimation of the multivariate covariance components for the balanced one-way layout. Annals of Mathematical Statistics, 40, 1100-1105. [10.6]
Kolmogorov, A. (1950), Foundations of the Theory of Probability, Chelsea, New York. [2.2]
Konishi, Sadanori (1978a), An approximation to the distribution of the sample correlation coefficient, Biometrika, 65, 654-656. [4.2]
Konishi, Sadanori (1978b), Asymptotic expansions for the distributions of statistics based on a correlation matrix, Canadian Journal of Statistics, 6, 49-56. [4.2]
Konishi, Sadanori (1979), Asymptotic expansions for the distributions of functions of a correlation matrix, Journal of Multivariate Analysis, 9, 259-266. [4.2]
Koopmans, T. C., and Olav Reiersol (1950), The identification of structural characteristics, Annals of Mathematical Statistics, 21, 165-181. [14.2]
Korin, B. P. (1968), On the distribution of a statistic used for testing a covariance matrix, Biometrika, 55, 171-178. [10.8]
Korin, B. P. (1969), On testing the equality of $k$ covariance matrices, Biometrika, 56, 216-218. [10.5]
Kramer, K. H. (1963), Tables for constructing confidence limits on the multiple correlation coefficient, Journal of the American Statistical Association, 58, 1082-1085. [4.4]
Krishnaiah, P. R. (1978), Some recent developments on real multivariate distributions, Development in Statistics (P. R. Krishnaiah, ed.), Vol. 1, Academic, New York, 135-169. [8.6]
Krishnaiah, P. R. (1980), Computations of some multivariate distributions, Analysis of Variance, Handbook of Statistics, Vol. 1 (P. R. Krishnaiah, ed.), North-Holland, Amsterdam, 745-971.
Krishnaiah, P. R., and T. C. Chang (1972), On the exact distributions of the traces of $S_{1}\left(S_{1}+S_{2}\right)^{-1}$ and $S_{1} S_{2}^{-1}$, Sankhyā, A, 34, 153-160. [8.6]
Krishnaiah, P. R., and F. J. Schuurmann (1974), On the evaluation of some distributions that arise in simultaneous tests for the equality of the latent roots of the covariance matrix, Joumal of Multivariate Analysis, 4, 265-282. [10.7]
Kshirsagar, A. M. (1959), Bartlett decomposition and Wishart distribution, Annals of Mathematical Statistics, 30, 239-241. [7.2]
Kudo, H..(1955), On minimax invariant estimates of the transformation parameter, Natural Science Report, 6, 31-73, Ochanomizu University, Tokyo, Japan. [7.8]
Kunitomo, Naoto (1980), Asymptotic expansions of the distributions of estimators in a linear functional relationship and simultaneous equations, Joumal of the American Statistical Association, 75, 693-700. [12.7]

Lachenbruch, P. A., and M. R. Mickey (1968), Estimation of error rates in discriminant analysis, Technometrics, 10, 1-11. [6.6]
Laplace, P. S. (1811), Mémoire sur les intégrales définies et leur application aux probabilités, Mémoires de l'Institut Impérial de France, Année I810, 279-347. [1.2]
Lauritzen, Steffen L. (1996), Graphical Models, Clarendon Press, Oxford. [15.5]
Lauritzen, Steffen L., and N. Wermuth (1989), Graphical models for associations between variables some of which are qualitative and some quantitative, Annals of Statistics, 17, 31-57. [15.2]
Läuter, Jürgen, Ekkehard Glimm, and Siegfried Kropf (1996a). New multivariate tests for data with an inherent structure, Biometrics Journal, 38, 5-23. (Correction: 40. (1998), 1015.] [5.7]

Läuter, Jürgen, Ekkehard Glimm, and Siegfried Kropf (1996b), Multivariate tests based on left-spherically distributed linear scores. Annals of Statistics. 26. 1972-1988. [5.7]
Länter, Jürgen, Ekkehard Glimm, and Siegfried Kropf (1996c). Exact stable multivariate tests for applications in clinical research. ASA Proccedings of the Biophamaceutical Section, 46-55. [5.7]
Lawley, D. N. (1938), A generalization of Fisher's $z$ test, Biometrika, 30, 180-187. [8.6]
Lawley, D. N. (1940), The estimation of factor loadings by the method of maximum likelihood, Proceedings of the Royal Society of Edinburgh, Sec. A, 60, 64-82. [14.3]
Lawley, D. N. (1941), Further investigations in factor estimation, Proceedings of the Royal Society of Edinburgh, Sec. A, 61, 176-185. [14.4]
Lawley, D. N. (1953), A modified method of estimation in factor analysis and some large sample results, Uppsala Symposium on Psychological Factor Analysis. 17-19 March 1953, Uppsala, Almqvist and Wiksell, 35-42. [14.3]
Lawley, D. N. (1958), Estimation in factor analysis under various initial assumptions. British Journal of Statistical Psychology, 11, 1-12. [14.2, 14.6]
Lawley, D. N. (1959), Tests of significance in canonical analysis, Biometrika. 46. 59-66. [12.4]
Lawley, D. N. (1967), Some new results in maximum likeliho.d factor analysis. Proceedings of the Royal Society of Edinburgh, Sec. A, 87. 256-264. [14.3]
Lawley, D. N., and A. E. Maxwell (1971), Factor Analysis as a Statistical Method (2nd ed.), American Elsevier, New York. [14.3, 14.5]
Lee, Y. S. (1971a), Asymptotic formulae for the distribution of a multivariate test statistic: power comparisons of certain multivariate tests. Biomerrika. 58, 647-651. [8.6]
Lee, Y. S. (1971b), Some results on the sampling distribution of the multiple correlation coefficient, Journal of the Royal Statistical Society B, 33, 117-130. [4.4]
Lee, Y. S. (1972), Tables of upper percentage points of the multiple contelation coefficient, Biometrika, 59, 175-189. [4.4]
Lehmann, E. L. (1959), Testing Statistical Hypotheses, John Wiley \& Sons, New York. [4.2, 5.6]
Lehmer, Emma (1944), Inverse tables of probabilities of errors of the second kind. Annals of Mathematical Statistics, 15, 388-398. [5.4]

Loève. M. (1977). Probability Theory I (4th ed.), Springer-Verlag, New York. [2.2]
Loève, M. (1978), Probability Theory II (4th ed.), Springer-Verlag, New York. [2.2]
Madow. W. G. (1938), Contributions to the theory of multivariate statistical analysis, Transactions of the American Mathematical Society, 44, 454-495. [7.2]
Magnus, Jan R. (1988), Linear Structures, Charles Griffin and Co., London. [A.4]
Magnus, J. R., and H. Neudecker (1979), The commutation matrix: some properties and applications, The Annals of Statistics, 7, 381-394. [3.6]
Mahalanobis, P. C. (1930). On tests and measures of group divergence, Journal and Proceedings of the Asiatic Society of Bengal, 26, 541-588, [3.3]
Mahalanobis, P. C., R. C. Bose, and S. N. Roy (1937), Normalisation of statistical variates and the use of rectangular co-ordinates in the theory of sampling distributions, Sankhyā, 3, 1-40. [7.2]
Mallows, C. L. (1961), Latent vectors of random symmetric matrices, Biometrika, 48, 133-149. [11.6]
Mardia, K. V. (1970), Measures of multivariate skewness and kurtosis with applications, Biometrika, 57, 519-530. [3.6]
Mariano, Roberto S., and Takamitsu Sawa (1972), The exact finite-sample distribution of the limited-information maximum likelihood estimator in the case of two included endogenous variables, Journal of the Americar Statistical Association, 67, 159-163. [12.7]
Maronna, R. A. (1976), Robust M-estimators of multivariate location and scatter, Annals of Statistics, 4, 51-67. [3.6]
Marshall, A. W., and 1. Olkin (1979), Inequalities: Theory of Majorization and Its Applications, Academic, New York. [8.10]
Mathai, A. M. (1971), On the distribution of the likelihood ratio criterion for testing linear hypotheses on regression coefficients, Annals of the Institute of Statistical Mathematics, 23, 181-197. [8.4]
Mathai, A. M., and R. S. Katiyar (1979), Exact percentage points for testing independence, Bionietrika, 66, 353-356. [9.3]
Mathaj. A. M., and P. N. Rathie (1980), The exact non-null distribution for testing equality of covariance matrices, Sankhyā A, 42, 78-87. [10.4]
Mathai, A. M.. and R. K. Saxena (1973), Generalized Hypergeometric Functions with Applications in Statistics and Physical Sciences, Lecture Notes No. 348, SpringerVerlag, New York. [9.3]
Mauchly. J. W. (1940). Significance test for sphericity of a normal $n$-variate distribution, Annals of Mathematical Statistics, 11, 204-209. [10.7]
Mauldon, J. G. (1955), Pivotal quantitics for Wishart's and related distributions, and a paradox in fiducial theory, Journal of the Royal Statistical Society B, 17, 79-85. [7.2]
McDonald. Roderick P. (2002), What can we learn from path equations: identifiability, constraints, equivalence, Psychometrika, 67, 225-249. [15.1]
McLachlan, G. J. (1973), An asymptotic expansion of the expectation of the estimated error rate in discriminant analysis, Australian Journal of Statistics, 15, 210-214. [6.6]



MeLachlan, G. J, (1974a), An asymptotic unbiased technique for estimating the error rates in discriminant analysis. Biometrics. 30. 239-249. [6.6]
McLachlan, G. J. (1974b). Estimation of the errots of misclassification on the criterion of asymptotic mean square error, Technometrics, 16, 255-260. [6.6]
McLachlan, G. J. (1974c), The asymptotic distributions of the conditional error rate and risk in discriminant analysis, Biometrika, 61, 131-135. [6.6]
McLachlan, G. J. (1977), Constrained sample discrimination with the studentized classification statistic W, Communications in Statistics -Theory and Methods, A6, 575-583 [6.6]
Memon, A. Z., and M. Okamoto (1971), Asymptotic expansion of the distribution of The $Z$ statistic in discriminant analysis, Journal of Multivariate Analysis, 1, 294-307. [6,6]
Mijares, T. A. (1964), Percentage Points of the Sum $V_{1}^{(s)}$ of $s$ Roots $(s=1-50)$, The Statistical Center, University of the Philippines, Manila, [8,6]
Mikhail, N. N. (1965), A comparison of tests of the Wilks-Lawley hypothesis in multivariate analysis, Biometrika, 52, 149-156, [8.6]
Mood, A. M. (1951), On the distribution of the characteristic roots of normal second-moment matrices, Annals of Mathematical Statistics, 22, 266-273. [13.2]
Morris, Blair, and Ingram Olkin (1964), Some estimation and testing problems for factor analysis models, unpublished. [10.6]
Mudholkar, G. S. (1966), On confidence bounds associated with multivariate analysis of variance and non-independence between two sets of variates, Annals of Mathematical Statistics, 37, 1736-1746. [8.7]
Mudholkar, Govind S., and Madhusudan C. Trivedi (1980), A normal approximation for the distribution of the likelihood ratio statistic in multivariate analysis of variance, Biometrika, 67, 485-488. [8.5]
Mudholkar, Govind S., and Madhusudan C. Trivedi (1981), A normal approximation for the multivariate likelihood ratio statistics, Statistical Distributions in Scientific Work (C. Taillie et al., eds.), Vol. 5, 219-230, D. Reidel Publishing. [8,5]
Muirhead, R. J. (1970), Asymptotic distributions of some multivariate tests, Annals of Mathematical Statistics, 41, 1002-1010. [8.6]
Muirhead, R, J. (1980), The eflects of elliptical distributions on some standard procedures involving correlation coefficients: a review, Multivariate Statistical Analysis (R. P. Gupta, ed.), 143-159. [4.5]
Muirhead, Robb J. (1982), Aspects of Multivariate Statistical Theory, John Wiley and Sons, New York. [2.7, 3.6, 7.7]
Muirhead, R. J., and C. M. Waternaux (1980), Asymptotic distributions in canonical correlation analysis and other multivariate procedures for nonnormal populations, Biometrika, 67, 31-43. [4.5]
Nagao, Hisao (1973a), On some test criteria for covariance matrix, Annals of Statintics, 1, 700-709. [9.5, 10.2, 10.7, 10.8]
Nagao, Hisao (1973b), Asymptotic expansions of the distributions of Bartlett's test and sphericity test under the local ahernatives, Amnals of the Institute of Statistical Mathematies, 25, 407-422, [10.5, 10.6]
Nagao, Hisao (1973c), Nonnull distributions of two test criteria for incependence under local alternatives, Journal of Multivariate Analysis, 3, 435-444. [9.4]

Nagarsenker, B. N., and K. C. S. Pillai (1972), The Distribution of the Sphericity Test Criterion, ARL 72-0154, Aerospace Research Laboratories. [Preface]
Nagarsenker, B. N., and K. C. S. Pillai (1973a), The distribution of the sphericity test criterion, Joumal of Multivariate Analysis, 3, 226-235. [10.7]
Nagarsenker, B. N., and K. C. S. Pillai (1973b), Distribution of the likelihood ratio criterion for testing a hypothesis specifying a covariance matrix, Biometrika, 60, 359-364. [10.8]
Nagarsenker, B. N., and K. C. S. Pillai (1974), Distribution of the likelihood ratio criterion for testing $\boldsymbol{\Sigma}=\boldsymbol{\Sigma}_{0}, \boldsymbol{\mu}=\boldsymbol{\mu}_{0}$, Journal of Multivaric te Analysis, 4, 114-122. [10.9]
Nanda, D. N. (1948), Distribution of a root of a determinantal equation, Annals of Mathematical Statistics, 19, 47-57. [8.6]
Nanda, D. N. (1950), Distribution of the sum of roots of a determinantal equation under a certain condition, Annals of Mathematical Statistics, 21, 432-439. [8.6]
Nanda, D. N. (1951), Probability distribution tables of the larger root of a determinantal equation with two roots, Joumal of the Indian Society of Agriculiural Statistics, 3, 175-177. [8.6]
Narain, R. D. (1948), A new approach to samplirg distributions of the multivariate norinal theory, I, Journal of the Indian Society of Agricultural Statistics, 1, 59-69. [7.2]
Nariin, R. D. (1950), On the completely unbiased character of tests of independence in multivariate normal systems, Annals of Mathematical Statistics, 21, 293-298. [9.2]
National Bureau of Standards, United States (1959), Tables of the Bivariate Normal Distribution Function and Related Functions, U.S. Government Printing Office, Washington, D.C. [2.3]
Neveu, Jacques (1965), Mathematical Foundations of the Calculus of Probability, Holden-Day, San Francisco. [2.2]
Ogawa, J. (1953), On the sampling distributions of classical statistics in multivariate analysis, Osaka Mathematics Journal, 5, 13-52. [7.2]
Okamoto, Masashi (1963), An asymptotic expansion for the distribution of the linear discriminant function, Annals of Mathematical Statistics, 34, 1286-1301. (Correction, 39 (1968), 1358-1359.) [6.6]
Okamoto, Masashi (1973), Distinctness of the eigenvalues of a quadratic form in a multivariate sample, Annals of Statistics, 1, 763-765. [13.2]
Olkin, Ingram, and S. N. Roy (1954), On multivariate distribution theory, Annals of Mathematical Statistics, 25, 329-339. [7.2]
Olson, C. L. (1974), Comparative robustness of six tests in multivariate analysis of variance, Journal of the American Statistical Association, 69, 894-908, [8:6]
Pearl, Judea (2000), Causality: Models, Reasoning, and Inference, Cambridge University Press, Cambridge. [15.1]
Pearson, E. S., and H. O. Hartley (1972), Biometrika Tables for Statisticians, Vol. II, Cambridge (England), Published for the Biometrika Trustees at the University Press, [Preface, 8.4]
Pearson, E. S., and S. S. Wilks (1933), Methods of statistical analysis appropriate for $k$ samples of two variables, Biometrika, 25, 353-378. [10.5]

Pearson, K. (1896), Mathematical contributions to the theory of evolution-111. Regression, heredity and panmixia, Philosophical Transactions of the Royal Socieny of London, Series A, 187, 253-318. [2.5, 3.2]
Pearson, K. (1900), On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling, Philosophical Magazine, 50 (fifth series), 157-175. [3.3]
Pearson, K. (1901), On lines and planes of closest fit to systems of points in space, Philosophical Magazine, 2 (sixth series), 559-572. [11.2]
Pearson, K. (1930), Tables for Statisticians and Biometricians, Part I (3rd ed,), Canbridge University, Cambridge, [2.3]
Pearson, K. (1931), Tables for Statisticians and Biometricians. Part Il, Cambridge University, Cambridge, [2,3, 6.8]
Perlman, M. D. (1980), Unbiasedness of the likelihood ratio tests for equality of several covariance matrices and equality of several multivariate normal populations. Annals of Statistics, 8, 247-263. [10.2, 10.3]
Perlman, M. D., and 1. Olkin (1980), Unbiasedness of invariant tests for MANOVA and other multivariate problems, Annals of Statistics, 8, 1326-1341. [8.10]
Phillips, P. C. B. (1980), The exact distribution of instrumental variable estimators in an equation containing $n+1$ endogenous variables, Econometrica, 48, 861-878. [12,7]
Phillips, P, C, B. (1982), A new approach to small sample theory, Unpublished, Cowles Foundation for Research in Economics, Yale University. [12.7]
Pillai, K. C. S. (1954), On some distribution problems in multivariate analysis, Mimeo Series No. 54, Institute of Statistics, University of North Carolina, Chapel Hill, North Carolina. [8.6]
Pillai, K. C. S. (1955), Some new test criteria in multivariate analysis, Annals of Mathematical Statistics, 26, 117-121. [8.6]
Pillai, K. C. S. (1956), On the distribution of the largest or the smallest root of a matrix in multivariate analysis, Biometrika, 43, 122-127. [8.6]
Pillai, K. C. S. (1960), Statistical Tables for Tests of Maltinariate Hypotheses. Statistical Center, University of the Philippines, Manila, [8,6]
Pillai, K. C. S. (1964), On the moments of elementary symmetric functions of the roots of two matrices, Annals of Mathematical Statistics, 35, 1704-1712, [8,6]
Pillai, K. C. S. (1965), Ou the distribution of the largest characteristic root of a matrix in multivariate analysis, Biometrika, 52, 405-412. [8.6]
Pillai, K. C. S. (1967), Upper percentage points of the largest root of a matrix in multivariate analysis, Biometroka, 54, 189-194. [8.6]
Pillai, K, C. S., and A, K, Gupta (1969), On the exact distribution of Wilks' criterion. Biometrika, 56, 109-118. [8.4]
Pillai, K. C. S., and Y. S. Hsu (1979), Exact robustness studies of the test of independence based on four multivariate criteria and their distribution problems inder violations, Ann ils of the Institute of Statistical Mathematics. 31. Part A. 85-101. [8.6]
Pillai, K. C. S., and K. Jayachandran (1967), Power comparisons of tests of two multivariate hypotheses based on four criteria, Biomenika, 54, 195-210, [8,6]

Pillai, K. C. S., and K. Jayachandran (1970), On the exact distribution of Pillai's $V^{(s)}$ eriterion, Journal of the American Statistical Association, 65, 447-454, [8,6]
Pillai. K. C. S., and T. A. Mijares (1959), On the moments of the trace of a matrix and approximations to its distribution, Annals of Mathematical Statistics, 30, 1135-1140. [8.6]
Pillai, K. C. S., and B. N. Nagarsenker (1971), On the distribution of the sphericity test criterion in classical and complex normal populations having unknown covariance matrices. Annals of Mathematical Statistics, 42, 764-767. [10.7]
Pillai, K. C. S.. and P. Samson, Jr. (1959), On Hotelling's generalization of $T^{2}$, Biomerrika, 46, 160-168. [8.6]
Pillai. K. C. S.. and T. Sugiyama (1969), Non-central distributions of the largest latent roots of three matrices in multivariate analysis, Annals of the Institute of Statistical Mathernalics, 21, 321-327. [8.6]
Pillai, K. C. S., and D. L. Young (1971), On the exact distribution of Hotelling's generalized $T_{0}^{2}$, Journal of Multivariate Analysis, 1, 90-107. [8.6]
Plana, G. A. A. (1813), Mémoire sur divers problèmes de probabilité, Mémoires de l'Académic Impériale de Ticrin, pour les Années 1811-1812, 20, 355-408. [1.2]
Pólya, G. (1949), Remarks on computing the probability integral in one and two dimensions, Proceedings of the Berkeley Symposium on Mathematical Statistics and Probabiling (J. Neyman, ed.), 63-78. [2.P]
Rao. C. R. (1948a), The utilization of multiple measurentents in problems of biological classification, Joinnal of the Royal Stutistical Society B, 10, 159-193. [6.9]
Rabo. C. R. (1948b). Tests of significance in multivariate analysis, Biomerrika, 35, 58-79. [5.3]
Rao. C. Radhakrishna (1951), An asymptotic expausion of the distribution of Wilks's criterion, Bulletin of the International Statistical Institute, 33, Part 2, 177-180. [8.5]
Rao. C. R. (1952), Advanced Statistical Methods in Biometric Research, John Wiley \& Sons. New York. [12.5]
Rao. C. R. (1973). Linear Statistical Inference and Its Applications (2nd ed.), John Wiley \& Sons. New York. [4,2]
Rasch. G. (1948), A functional equation for Wishart's distribution, Annals of Mathematical Statistics, 19, 262-266. [7.2]
Reiersgl, Olav (1950), On the identifiability of parameters in Thurstone's multiple factor analysis. Psychometnka, 15, 121-149, [14.2]
Reinsel, G. C.. and R. P. Velu (1998), Multivariate Reduced-rank Regression, Springer, New York. [12,7]
Richardson. D. H. (1968), The exact distribution of a structural coefficient estimator, Journal of ilte American Statistical Association, 63, 1214-1226. [12.7]
Rothenberg. Thomas J. (1977), Edgeworth expansions for multivariate test statistics, 1P-255, Center for Research in Management Science, University of California, Berkeley. [8.6]
Roy. S. N. (1939), $\rho$-statistics or some gencralisations in analysis of variance appropriate to multivariate problems, Sankhyā, 4, 381-396. [13.2]
Roy. S. N. (1945), The individual sampling distribution of the maximum, the minimum and any intermediate of the $\rho$-statistics on the null-hypothesis, Sankhyā, 7, 1.33-158, [8.6]

Roy, S, N, (1953), On a heuristic method of test construction and its use in multivariate analysis, Annals of Mathematical Statistics, 24, 220-238. [8,6, 10.6]
Roy, S. N. (1957), Some Aspects of Multivarlate Analysis, John Wiley \& Sons, New York. [8.6, 10.6, 10.8]
Ruben, Harold (1966), Some new esults on the distribution of the sample correlation coefficient, Joumal of the Royal Statistical Society B, 28, 513-525. [4.2]
Rubin, Donald B., and Dorothy T. Thayer (1982), EM algorithms for ML factor analysis, Psychometrika, 47, 69-76. [14.3]
Ryan, D. A. J., J. J. Hubert, E. M. Carter, J. B. Sprague, and J. Parrot (1992), A reduced-rank multivariate regression approach to joint toxicity experiments, Biometrics, 48, 155-162. [12.7]
Šalaevskĩ, O. V. (1968), The minimax character of Hotelling's $T^{2}$ test (Rassian), Doklady Akademii Nauk SSSR, 180, 1048-1050. [5.6]
Šalaevskī, (Shalaevskii), O. V. (1971), Minimax character of Hotelling's $T^{2}$ test. I. Investigations in Classical Problems of Probability Theory and Mathematical Statistics, V. M. Kalinin and O. V. Shalaevskii (Seminar in Mathematics, V. I. Steklov Institute, Leningrad, Vol, 13), Consultants Bureau, New York. [5.6]
Sargan, J. D., and W. M. Mikhail (1971), A general approximation to the distribution of instrumental variables estimates, Econometrica, 39, 131-169. [12.7]
Sawa, Takamitsu (1969), The exact sampling distribution of ordinary least squares and two-stage least squares estimators, Jorunal of the American Statistical Association, 64, 923-937. [12.7]
Schatzoff, M. (1966a), Exact distributions of Wilks's likelihood ratio criterion, Biometrika, 53, 347-358, [8.4]
Schatzoff, M. (1966b), Sensitivity comparisons among tests of the general linear hypothesis, Joumal of the American Statistical Association, 61, 415-435. [8,6]
Scheffé, Henry (1942), On the ratio of the variances of two normal populations, Annals of Mathematical Statistics, 13, 371-388. [10.2]
Scheffé, Henry (1943). On solutions of the Behrens-Fisher problem, based on the $t$-distribution, Annals of Mathematical Statistics, 14, 35-44. [5.5]
Schmidli, H. (1996), Reduced-rank Regression, Physica, Berlin. [12.7]
Schuurmann, F. J., P. R. Krishnaiah, and A. K. Chattopadhyay (1975), Exact percentage points of the distribution of the trace of a multivariate beta matrix, Joumal of Statistical Computation and Simulation, 3, 331-343. [8.6]
Schuurmann, F. J., and V. B. Waikar (1973), Tables for the power function of Roy's two-sided test for testing hypothesis $\Sigma=I$ in the bivariate case, Communications in Statistics, 1, 271-280. [10.8]
Schuurmann, F. J., V. B. Waikar, and P. R, Krishnaíah (1975), Percentage points of the joint distribution of the extreme roots of the random matrix $S_{1}\left(S_{1}+S_{2}\right)^{-1}$, Journal of Statistical Computation and Simulation, 2, 17-38. [10.6]
Schwartz, R (1967), Admissible tests in multivariate analysis of variance, Annals of Mathematical Statistics, 38, 698-710. [8.10]
Serrling, Robert J. (1980), Approximation Theorems of Mathematical Statistics, John Wiley \& Sons, New York, [4.2]
Simaika, J. B. (1941), On an optimum property of two important statistical tests, Biometrika, 32, 70-80, [5,6]

Siotani, Minoru (1980), Asymptotic approximations to the conditional distributions of the classification statistic $Z$ and its studentized form $Z^{*}$, Tamkang Journal of Mathematics, 11, 19-32. [6.6]
Siotani, M., and R, H, Wang (1975), Further expansion formulae for error rates and comparison of the $W$ - and the $Z$-procedures in discriminant analysis, Technical Report No. 33, Department of Statistics, Kansas State University, Manhattan, Kansas, [6,6]
Siotani, M., and R. H. Wang (1977), Asymptotic Expansions for Error Rates and Comparison of the $W$-Procedure and the $Z$-Procedure in Discriminant Analysis, Multivariate Analysis IV, North-Holland, Amsterdam, 523-545. [6.6]
Sitgreaves, Rosedith (1952), On the distribution of two random matrices used in classification procedures, Annals of Mathematical Statistics, 23, 263-270. [6.5]
Solari, M. E. (1969), The "maximum likelihood solution" of the problem of estimating a linear functional relationship, Journal of the Royal Statistical Society B, 31, 372-375, [14,4]
Spearman, Charles (1904), "General-intelligence," objectively determined and measured, American Journal of Psychology, 15, 201-293. [14.2]
Speed, T. P., and H. Kiiveri (1986), Gaussian Markov distributions over finite graphs, Annals of Statistics, 14, 138-150. [15.5]
Srivastava, M. S., and C. G. Khatri (1979), An Introduction to Multivariate Statistics, North-Holland, New York. [10.9, 13.P]
Stein, C. (1956a), The admissibility of Hotelling's $T^{2}$-test, Annals of Mathematical Statistics, 27, 616-623, [5.6]
Stein, C. (1956b), Inadmissibility of the usual estimator for the mean of a multivariate normal distribution, Proceedings of the Third Berkeley Symposium on Mathematical and Statistical Probability (Jerzy Neyman, ed.), Vol. I, 197-206, University of Californía, Berkeley. [3.5]
Stein, C, (1974), Estimation of the parameters of a multivariate normal distribution, I. Estimation of the means, Technical Report No. 63, NSF Contract GP 30711X-2, Department of Statistics, Stanford University. [3,5]
Stoica, P., and M. Viberg (1996), Maximum likelihood parameter and rank estimation in reduced-rank multivariate linear regressions, IEEE Transaction Signal Processing, 44, 3069-3078. [12.7]
Student (W. S. Gosset) (1908), The probable error of a mean, Biometrika, 6, 1-25. [3.2]
Styan, George P. H. (1990), The Collected Papers of T. W. Anderson: 1943-1985, John Wiley \& Sons, Inc., New York. [Preface]
Subrahmaniam, Kocherlota, and Kathleen Subrahmaniam (1973), Multivariate Analysis: A Selected and Abstracted Bibliography, 1957-1972, Marcel Dekker, New York. [Preface]
Sugiura, Naríaki, and Hisao Nagao (1968), Unbiasedness of some test criteria for the equality of one or two covariance matrices, Annals of Mathematical Statistics, 39, 1686-1692. [10.8]
Sugiyama, T. (1967), Distribution of the largest latent root and the smallest latent root of the generalized $B$ statistic and $F$ statistic in multivariate analysis, Annals of Mathematical Statistics, 38, 1152-1159. [8.6]

Sugiyama, T, and K, Fukutomi (1966), On the distribution of the extreme characteristic roots of the matrices in multivariate analysis, Reports of Statistical Applicanion Research, Union of Japanese Scientists and Engineers, 13. [8,6]
Sverdrup, Erling (1947), Derivation of the Wishart discribution of the second order sample moments by straightforward integration of a multiple integral. Skandinavisk Aktuarietidskrift, 30, 151-166. [7.2]
Tang, P, C. (1938), The power function of the analysis of variance tests with tables and illustrations of their use, Statistical Resecrch Memoirs, 2, 126-157. [5.4]
Theil, H, (assisted by J, S, Cramer, H, Moerman, and A. Russchen) (1961), Economic Forecasts and Policy, (2nd rev, ed,), North-Holland, Amsterdam. Contributions to Economic Analysis No. XV (first published 1958). [12.8]
Thomson, Godfrey H. (193\%), Hotelling's method modified to give Spearman's "g." Journal of Educational I sychology, 25, 366-374. [14.3]
Thomson, Godfrey H. (1951), The Factorial Analysis of Human Ability (5th ed.). University of London, London. [14.7]
Thurstone, L. L. (1947), Multiple-Factor Analysis, University of Chicago. Chicago. [14.2, 14.5]
Tsay, R. S., and G. C. Tiao (1985), Use of canonical analysis in time series model identification, Biometrika, 72, 299-315. [12.7]
Tukey, J. W. (1949), Dyadic anova, an analysis of variance for vectors. Human Biologv, 21, 65-110. [8.9]
Tyler, David E, (1981), Asymptotic inference for cigenvectors, Amnats of Statistics, 9. 725-745. [11.7]
Tyler, David E. (1982), Radial estimates and the test for sphericity. Biometriha, 69. 429-436. [3.6]
Tyler, David E. (1983a); Robustness and efficiency properties of scatter matrices. Biometrika, 70, 411-420. [3.6]
Tyler, David E, (1983b), The asymptotic distribution of principal component roots under local alternatives to multiple roots, Annals of Statistics, 11. 1232-1242. [11.7]
Tyler, David E. (1987), A distribution free $M$-estimator of multivariate scatter, Amals of Statistics, 15, 234-251. [3.6]
Velu, R. P., G. C. Reinsel, and D. W. Wichern (1986), Reduced rank models for multíple tíme series, Biometrika, 73, 105-118, [12,7]
von Mises, R. (1945), On the classification of observation data into distinct groups. Annals of Mathematical Statistics, 16, 68-73. [6.8]
von Neumann, J. (1937), Some matrix-inequalities and merrization of matric-space. Tomsk University Review, 1286-300. Reprinted in John von Neuman Collected Works (A. H. Taub, ed.), 4 (1962), Pergamon. New York. 205-219. [A.4]
Wald, A. (1943), Tests of statistical hypotheses concerning several parameters when the number of observations is large, Transactions of the American Mathematical Society, 54, 426-482. [4.2]
Wald, A. (1944), On a statistical problem arising in the classification of an individual into one of two groups. Annals of Malhemalical Slalistics. 15, 145-162, [6.4, 6.5]
Wald, A. (1950), Statistical Decision Functions, John Wiley \& Sons, New York. [6,2. 6.7, 8.10]

Wald, A., and R. Brookner (1941), On the distribution of Wilks' statistic for testing the independence of several groups of variates, Annals of Mathematical Statistics, 12. 137-152. [8,4, 9,3]

Walker, Helen M. (1931), Studies in the History of Statistical Method, Williams and Wilkins, Baltimore. [1.1]
Welch, P. D., and R. S. Wimpress (1961), Two multivariate statistical c mputer programs and their application to the vowel recognition problem, Joumal of the Acoustical Society of America, 33, 426-434. [6.10]
Wermuth, N. (1980), Linear recursive equations, covariance selection and path analysis, Journal o, the American Statistical Association, 75, 963-972. [15,5]
Whittaker, E. T., and G. N. Watson (1943), A Course of Modern Analysis, Cambridge University, Cambridge, [8,5]
Whittaker. Joe (1990), Graphical Models in Applied Multivariate Statistics, John Wiley \& Sons, Ine.. Chichester, [15,1]
Wijsman, Robert A. (1979), Constructing all smallest simultaneous confidence sets in a given class. with applications to MANOVA, Amals of Statistics, 7, 1003-1018. [8.7]
Wijsman, Robert A. (1980), Smallest simultaneous confidence sets with applications in multivariate analysis. Multivariate Aralysis, V, 483-498. [8.7]
Wilkinson, James Hardy (1965), The Algebraic Eigenvalue Problem, Clarendon, Oxford. [11.4]
Wilkinson, J. H., and C. Reinsch (1971), Linear Algebra, Springer-Verlag, New York. [11.4]
Wilks, S. S. (1932), Certain generalizations in the analysis of variance, Biometrika, 24, 471-494. [7.5, 8.3, 10.4]
Wilks, S. S. (1934), Moment-generating operators for determinants of product moments in samples from a normal syttem. Annals of Mathematics, 35, 312-340. [8.3]
Wilks, S. S. (1935), On the independence of $k$ sets of normally distributed statistical variables, Econonetrica, 3, 309-326, [8.4, 9.3, 9.P]
Wishart, John (1928), The generalised product moment distribution in samples from a normal multívariate population, Biometrika, 20A, 32-52. [7.2]
Wishart, John (1948), Proofs of the distribution law of the second order inoment statistics, Biometrika, 35, 55-57, [7.2]
Wishart. John. and M. S. Bartlett (1933), The generalised product moment distribution in a normal system, Proceedings of the Cambridge Philosophical Society, 29, 260-270. [7.2]
Wold, H. D. A. (1954), Causality and econometrics, Econom trica 22, 162-177, [15,1]
Wold. H. D. A. (1960), A generalization of casual chain models, Econometrica, 28, 443-463. [15.1]
Woltz, W. G., W. A. Reid, and W. E. Colwell (1948), Sugar and nicotine in cured bright tobacco as related to mineral element composition, Proceedings of the Soil Sciences Society of America, 13, 385-387. [8.P]
Wright, Sewall (1921), Correlation and causation, Journal of Agricultural Research, 20, 557-585. [15.1]

Wright, Sewall (1934), The method of path coefficients, Annals of Mathematical Statistics, 5, 161-215. [15,1]
Yamauti, Ziro (1977), Concise Statistical Tables, Japanese Standards Association. [Preface]
Yates, F., and W. G. Cochran (1938), The analysis of groups of experiments, Journal of Agricultural Science, 28, 556. [8.9]
Yule, G. U. (1897a), On the significance of Bravais' formulae for regression \& c., in the case of skew correlation, Proceedings of the Royal Society of London, 60, 477-489. [2.5]
Yule, G. U. (1897b), On the theory of correlation, Journal of the Royal Statistical Society, 60, 812-854. [2.5]
Zehna, P. W. (1966), Invariance of maximum likelihood estimators, Annals of Mathematical Statistics, 37, 744. [3.2]



## Index

Absolutely continuous distribution, 8
Additivity of Wishart matrices, 259
Admissible, definition of, $88,210,235$
Admissible procedures, 235
Admissible test, definition of, 193
Stein's theorem for, 194
Almost invariant test, 192
Analysis of variance, random effects model, 429
likelihood ratio test of, 431
See also Multivariate analysis of variance
Anderson, Edgar, Iris data of, 111
A postcriori density, 89
of $\mu, 89$
of $\mu$ and $\Sigma, 274$
of $\boldsymbol{\mu}$, given $\overline{\boldsymbol{x}}$ and $\boldsymbol{S}, 275$
of $\Sigma, 273$
Asymptotic distribution of a lunction, 1.22
Asymptotic expansions of distributions of likelihood ratio criteria, 321
of gamma function, 318
Barley yields in two years, 349
Bartlett decomposition, 257
Bartlett-Nanda-Pillai trace criterion, see Linear hypothesis
Bayes estimator of covariance matrix, 273
Bayes estimator of mean vector, 90
Bayes procedure, 89
extended, 90
Bayes risk, 89
Bernoulli polynomials, 318
Best estimator or covariance matrix
invariant with respect to triangular linear transformations, 279, 281
proportional to sample covariance matrix. 277

Best linear predictor, 37. 497
and predictand. 497
See also Canonical correlations and variates
Best linear unbiased estimator. 298
Beta distribution, 177
Bhattacharya's estimator of the mean, 99
Bivariate normal density. 21, 35
distribution. 21. 35
computation of. 23
Bootstrap method, 135
c 17
Canonical analysis of regression coefficients. 508
sample. 510
Canonical correlations and variates. 487, 495
asymptotic disaribution of sample
contelanionas. 505
computation of. 501
distribution of sample, 545
invaríance of, 496
maximum likelihood estimators of, 501
sample. 500
testing number of nonzero correlations. 504
use in testing hypotheses of rank of covariance matrix. 504
Causal chain. 605
Central limit theorem. multivariate. 86
Characteristic function, 41
continuity theorem for, 45
inversion of. 45
of the multivariate normal distribution. 43
Characteristic roots and vectors. 631. 632
asymphotic dismibuminato of 545.550
distribution of roots of a symmetric matrix. 542
distribution of roofs of Wishart matrix. 540

Characteristic roots and vector (Continued)
of Wishart matrix in the metric of another, 529
asymptotic distribution of, 550
distribution of, 536
See also Principal components
Chi-squared distribution, 286
noncentral, 82
Cholesky decomposition, 631
Classification into normal populations
Bayes
into one of several, 236
into one of two, 204
discriminant function. 218
sample, 220
example, 240
invariance of procedures, 226
likelihood criterion for, 224
unequal covariance matrices, 242
linear, for unequal covariance matrices, 243
admissible, 246
maximum likelihood rule, 226
minimax
one of several, 238
one of two, 218
one of several, 237
one of two, 216
$W$-statistic. 219
asymptotic distribution of, 222
asymptotic expansion of misclassification probabilities, 227
Z-statistic, 226
asymptotic expansion of misclassification probabilities, 231
See also Classification procedures
Classification procedures
admissible, 210, 235
Into Several popula ions, 236
into two populations, 214
a priori probabilities, 209
Bayes, 89, 210
and admissible, 214, 236
into several populations, 234
into two populations, 216
complete class of, 211, 235
essentially, 211
minimal, 211
costs of misclassification, definition of, 208
expected loss from misclassification, 210
minimax, 211
for two populations, 215
probability of misclassification, 210, 227
See also Classification into normal populations

Cochran's theorem, 262
Coefficient of alienation, 400
Complete class of procedures, 88
essentially, 88
minimal, 88
Completeness, deffilition of, 84
of sample mean and covariance matrix, 84, 85
Complex normal distribution, 64
characteristic function of, 65
linear transformation in, 65
maximum likelihood estimators for, 112
Complex Wishart distribution, 287
Components of variance, 429
Concentration ellipsoid, 58, 85
Conditional density, 12 normal, 34
Conditional probability, 12
Conjugate family of distributions, 272
Consistency, definition of, 86
Contours of constant density, 22
Correlation coefficient
canonical, see Canonical correlations and variates
confidence interval for, 128
by use of Fisher's 2, 135
distribution of sample, asymptotic, 133
bootstrap method for, 135
tabulation of, 126
when population is not zero, 125
when population is zero, 121
distribution of set of sample 272
Fisher's $z, 134$
geometric interpretation of sample, 72
invariance of population, 21
invariance of sample, 111
likelihood ratio test, 130
maximum likelihood estimator of, 71
as measure of association, 22
moments of, 166
monotone likelihood ratio of, 164
multiple, see Multiple correlation coefficient
partial, see Partial correlation coefficient
in the population (simple, Pearson,
product-moment, total), 20
sample (Pearson), 71, 116
test of equality of two, 135
test of hypothesis about, 126
by Fisher's $z, 134$
power of, 128
test that it is zero, 121
Cosine of angle between two vectors, 72. See
also Correlation coefficient
Covariance, 17

Covariance matrix, 17
asymptotic distribution of sample, 86
Bayes estimator of, 273
characterization of distribution of sample, 77
confidence bounds for quadratic form in, 442
consistency of sample as estimator of population, 86
distribution of sample, 255
estimation, see Best estimator of
geometrical interpretation of sample, 72
with linear structure, 113
maximum likelihood estimator of, 70
computation of, 70
when the mean vector is known, 112
of normal distribution, 20
sample, 77
singular, 31
tests of hypotheses, see Testing that a covariance matrix is a given matrix; Testing that a covariance matrix is proportional to a given matrix; Testing that a covariance matrix and mean vector are equal to a given matrix and vector; Testing equality of covariance matrices; Testing equality of covariance matrices and mean vectors; Testing independence of sets of variates
unbiased estimator of, 77
Covariance selection models, 614
decomposition of, 618
estimation in, 614
Cramér-Rao lower bound, 85
Critical function, 192
Cumulants, 46
of a multivanate normal distribution, 46
Cumulative distribution function (cdf), 7

Decision procedure, 88
Degenerate normal distribution, 30
Density, 7
conditional, 12
normal, 34
marginal, 9
normal, 27, 29
multivariate normal, 20
Determinant, 626
derivative of, 642
symmetric matrix, 642
Dirichlet distribution, 290
Discriminant function, see Classification into normal populations
Distance, 631

Distance between two populations, 80
Distribution, see Canonical correlations; Characteristic roots; Correlation coefficient; Covariance matrix; Cumulative distribution function; Density; Generalized variance, Mean vector; Multiple correlation coefficient; Multivariate normal density; Multivariate $t$-distribution; Noncentral chi-squared distribution; Noncentral $F$-distribution; Noncentral $T^{2}$-distribution; Partial correlation coefficient; Principal components; Regression coefficients; $T^{2}$-test and statistic; Wishart distribution
Distribution of matrix of sums of squares and cross-products, see Wishart distribution
Duplication formula for gamma function, 82, 125, 309
§, 9
Efficiency of vector estimate, definition of, 85
Ellipsoid of concentration of vector estimate, 58, 85
Ellipsoid of constant density, 32
Elliptically contoured distribution, 47
characteristic function of, 53
characteristic roots and vectors, asymptotic distribution of, 482, 564
correlation coefficient, asymptotic distribution of, 159
covariance of, 50
covariance of sample covariance, 101
covariance of sample mean, 101
cumulants of, 54
kurtosis of, 54
likelihood ratio criterion for equality of covariance matrices, asymptotic distribution of, 451
likelihood ratio criterion for irdenendence of sets, asymptotic distribution of, 406
likelihood ratio criterion for linear hypotheses, asymptotic distribution of, 371
maximum likelihood estimator of parameters, 104
multiple correlation coefficient, asymptotic distribution of, 159
rectangular coordinates, asymptotic distribution of, 283
test for regression coefficients, 371
Elliptically contoured matrix distribution, 104
characteristic roots and vectors, distribution of, 483, 566
likelihood ratio criterion for equality of covariance matrices, distribution of, 454

Elliptically contoured matrix (Continued)
likelihood ratio criterion for independence of sets, distribution of, 408
likelihood ratio criterion for linear hypotheses, distribution of, 373
rectangular coordinates, distribution of, 285
stochastic representation, 160, 285
sufficient statistics, 160
$T^{2}$-distribution of, 200
Equiangular linc, 72
Exp, 15
Expected value of complex-valued function, 41
Exponential family of distributjons, 194
Extended region, 355
Factor analysis, 569
centroid method, 586
communalities, 581
conflimatory. 574
EM algorithm, 580, 593
exploratory, 574
general factor, 570
identification of structure in, 572 by specified zeros, 571, 593
loadings, 570
maximum likeljhood estimators, 578
asymptotic distribution of, 582
in case of identification by zeros, 590
nonexistence for fixed factors, 587
for random factors, 583
minimum distance methods, 583
modeI, 570
oblique factors, 571
orthogonal factors, 571
principal component analysis, relation to, 584
rotation of factors, 571
scores, estimation of, 591
simple structure, 573
space of factors, 572
transformations, 588
tests of fit for, 581
units of measurement, 575
varimax criterion, modified, 589
Factorization theorem, 83
Fisher's $z, 133$
asymptotic distribution of, 134
moments of, 134
See also Correlation coefficient; Partial correlation coefficient

## $\Gamma_{p}(t), 257$

Gamma function, multivariate, 257

Generalized analysis of variance, see
Multivariate analysis of variance;
Regression coefficients and function
Generalized $T^{2}$, see $T^{2}$-test and statistic
Generalized variance, 264
asymptotic distribution of sample, 270
distribution of sample, 268
geometric interpretation of sample in $N$ dimensions, 267
in $p$ dimensions, 268
invartance of, 465
moments of sample, 269
sample, 265
General lincar hypothesis, see Linear
hypothesis, testing of; Regression coefficients and function
Gram-Schmidt orthogonalization, 252, 647
Graphical modils, 595
adjacent, nonadjacent vertices, 596
AMP (Anderson-Madigan-Periman)
Markov chain, 612
ancestor, 605
boundary, 598
chain graph, 630
chid, 605
clique, 602
closure, 598
complete, 602
decomposition, 603
descendant, nondescendant, 605
edges, 595
directed, undirected, 596
LWF (L iuritzen-Wermuth-Frydenberg)
Markov chain, 610
Markov properties, 597
globally, 600
Iocally, 598
pairwise, 597
moral graph, 608
nodes, 595
pareift, 005
partial ordering, 605
path, 600
recursivc factorization, 609
separate, 600
vertices, 595
well-numbered, 607
Haar invariant distribution of orthogonal matrices, 162, 541
conditional distribution, 542
Hadamard's inequality, 61
Head lengths and breadths of brothers, 109
Hotelling's $T^{2}$, see $T^{2}$-test and statistic
Hypergeometric function, 126

Incomplete beta function, 329
Independence, 10
mutual, 11
of normal variables, 26
of sample mean vector and sample covariance matrix, 77
tests of, see Correlation coefficient; Multiple correlation coefficient; Testing independence of sets of variates
Information matrix, 85
Integral of a symmetric unimodal function over a symmetric convex set, 365
Intraclass correlation, 484
Invariance, see Classification into normal populations; Correlation coefficient; Generalized variance; Linear hypothesis; Multiple correlation coefficient; Partial correlation coefficient; $T^{2}$-test; Testing that a covariance matrix is a given matrix; Testing that a covariance matrix is proportional to a given matrix; Testing equality of covariance matrices; Testing equality of covariance matrices and means vectors; Testing independence of sets of variates
Inverted Wishart distribution 272
Iris, four measurements on, 110,180

Jacobian, 13
James-Stejn estimator, 91
for arbitrary known covariance matrix, 97
average mean squared error of, 95

Kronecker delta, 75
Kronecker product of matrices, 643
characteristic roots of, 643
determinant of, 643
Kurtosis, 54
estimation of, 103

Latin square, 377
Lawley-Hotelling trace criterion, see Linear hypothesis
Least squares estimator, 295
Likelihood, induced, 71
Likelihood function for sample from multivariate normal distribution, 67
Likelihood loss function for covariance matrix, 276
Likelihood ratio test, definition of, 129. See also Correlation coefficient; Linear hypothesis; Mean vector; Multiple correlation coefficient; Regression
coefficients; $T^{2}$-test; Testing that a covariance matrix is given matrix; Testing that a covariance matrix is proportional to given matrix: Testing that a covariance matrix and mean vector are equal to a given matrix and vector; Testing equality of covariance matrices; Testing equality of covariance matrices and mean vectors: Testing independence of sets of variates
Linear combinations of normal variables.
distribution of, 29
Linear equations, solution of, 606
by Gaussian elimination, 607
Linear functional relationship. 513
relation to simultaneous equations, 520
Linear hypothesis, testing of admissibility of, 353
necessary condition for, 363
Bartlett-Nanda-Pillai trace criteríon, 331
admissibility of, 379
asymptotic expansion of distribution of, 333
as Bayes procedure, 378
table of significance points of, 673
tabulation of power of, 333
canonical form of, 303
comparison of powers, 334
invariance of criteria, 327
Lawley-Hotelling trace criterion, 328
admissibility of, 379
asymptotic expansion of distribution of, 330
monotonicity of power function of, 368
table of significance points of, 657
tabulation of, 328
likelihood ratio criterion, 300
admissibility of, 378
asymptotic expansion of distribution of, 321
as Bayes procedurc, 378
distributions of, 306, $3[0$
$F$-approximation to distribution of, 326
geometric interpretation of, 302
moments of. 309
monotonicity of power function of, 368
normal approximation to distribution of, 323
table of significance points. 651
tabulation of distribution of. 314
Wilks* $\lambda, 300$
monotonicity of power function of an invariant test, 363
Roy's maximum root criterion, 333
distribution for $p=2,334$
monotonicity of power function of. 368

Linear hypothesis (Continued)
table of significance points, 677
tablulation of distribution of. 333
step-down test. 314
See also Regression coefficients and function
Linearly independent vectors, 627
Linear transformation of a normal vector, 23. 29. 31

Loss. 88
LR decomposition 630

Mahalanobis distance, 80, 217
sample. 228
Majorization, 355
weak. 355
Marginal density. 9
distribution. 9
normal, 27
Mathematical expectation, 9
Matrix, 624
bidiagonal, upper, 503
characteristic roots and vectors of, see
Characteristic roots and vectors
cofactor in, 627
convexíty, 358
definition of, 624
diagonalization of symmetric, 631
doubls stochastic, 646
eigenvalue. see Characteristic roots and vectors
Givens, 471, 649
Householder. 470, 650
idempotent. 635
identity, 626
inverse, 627
minor of, 627
nonsingular, 627
operations with, 625
positive definite, 628
positive semidefinite, 628
rank of, 628
symmetric, 626
trace of, 629
transpose, 625
triangular, 629
tridiagonal, 470
Matrix of sums of squares and cross-products of deviations from the means, 68
Maximum likelihood estimators, see Canonical correlations and variates; Correlation coefficient: Covariance matrix: Mean vector; Multiple correlation coefficient; Partial corrclation coefficient; Principal componentல; Regression coefficients; Variance

Maximum likelihood estimator of function of parameters, 71
Maximum of the likelihood function, 70
Maximum of variance of linear combinations, 464. See also Principal components

Mean vector, 17
asymptotic normality of sample, 86
completeness of sample as an estimator of' population, 84
confidence region for difference of two when common covariance matrix is known, 80
when covariance matrix is unknown. 180
consistency of sample as estimate of population, 86
distribution of sample, 76
efficiency of sample, 85
improved cstimalor when covariance matrix is unknown, 185
maximum likelihood estimator of, 70
sample, 67
simultaneous confidence regions for linear functions of, 178
testing equality of, in several distributions, 206
testing equality of two when common covariance matrix is known, 80
tests of hypothesis about
when covariance matrix is known, 80
when covariance matrix is unk own, see $T^{2}$-test
See also James-Stein estimator
Minimax, 90
Missing observations, maximum likelihood essimators, 168
Modulus, 13
Moments, 9, 4 I
factoring of, 11
from marginal distributions, 10
of normal distributions, 46
Monotone region, 355
in majorization, 355
Multiple correlation coefficient
adjusted, I53
distribution of sample
conditional, I54
when population correlation is not zero. 156
when population correlation is zero, 150
geometric interpretation of sample, 148
invariance of population, 60
invariance of sample, 166
likelihood ratio tess that in is zero, 151
as maximum correlation between one variable and lincar combination of other variables, 38
maximum likelihood estimator of, 147
moments of sample, 156
optimal properties of, 157
population, 38
sample, 145
tabulation of distribution of, 1.7
Multivariate analysis of variance (MANOVA), 346
Latin square, 377
one-way, 342
two-way, 346
See also Linear hypothesis, testing of
Multivariate beta distribution, 377
Multivariate of gamma function, 257
Multivariate normal density, 20
distribution, 20
computation of, 23
Multivariate $t$-distribution, 276, 289
$n(x \mid \mu, \Sigma), 20$
$N(\mu, \Sigma), 20$
Neyman-Pearson fundamental Iemina, 248
Noncentral chi-squared distribution, 82
Noncentral $F$-distribution, 186
tables of, 186
Noncentral $T^{2}$-distribution, 186
$O(N \times p), 161$
Orthonormal vectors, 647

Parallelotope, 266
volume of, 266
Partial correlation coefficient
computational formulas for, 39, 40,41
confidence intervals for, 143
distribution of sample, 143
geometric interpretation of sample, 138
invariance of population, 63
invariance of sample, 166
maximum likelihood estimator of, 138
in the population, 35
recursion formula for, 41
sample, 138
tests about, 144
Partial covariancc, 34
estimator of, 137
Partial variance, 34
Partioning of a matrix, 635
addition of, 635
of a covariance matrix, 25
delerininant of, 637
inverse of, 638
multiplication of, 635
Partioning of a vector, 635
of a mean vector, 25
of a random vector, 24
Path analysis, 596. See also Graphical models
Pearson correlation coefficient, see
Correlation coefficient
Plane of closest fit, 466
Polar coordinates, 285
Positive definite matrix, 628
Positive part of a function, 96
of the James-Stein estimator, 97
Positive semidefinite matrix, 628
Precision matrix, 272
unbiased estimator of, 274
Principal axes of ellipsoids of constant density, 465. See also Principal components

Principal components, 459
asymptotic distribution of sample, 473
computation of, 469
confidence region for, 475, 477
distribution of sample, 540,542
maximum likelihood estimator of, 467
population, 464
testing hypotheses about, 478, 479, 480
Probability element, 8
Product-moment correlation coefficient, see Correlation coefficient
$Q L$ algorithm, 471
$Q R$ algorithm, 471
decomposition, 647
Quadratic form, 628
Quadratic loss function for covariance matrix, 276
$r, 71$
: R (real part), 257
Ramdom matrix, 10
expected valuc of, 17
Random vector, 16
Randomized tcst, definition of, 192
Rectangular coordinates, 257
distribution of, 255, 257
Reduccd rank rcgression, 514
estimator, asymptotic distribution of, 550
Regression exelficients and function, 34
confidenec regions for, 339
distribution of sample, 297
geometric interpretation of sample, 138
maximum likelihood estimator of, 294
partial correlation, connection with, 61
sample, 294

Regression coefficients (Continued)
simultaneous confidence intervals for, 340 , 341
testing hypotheses of rank of, 512
testing they are zero, in case of one dependent variable, 152
Residuals from regression, 37
Risk function, 88

Selection of Ilnear combinations, 201
Simple correlation coefficient, See Correlation coefficient
Simultaneous equations, 513
estimation of coefficients, 518
least variance ratio (LVR), 519
limited information maximum likelihood (LIML), 519
two stage least squares (TSLS), 522
identification by zeros, 516
reduced form, 516
estimation of, 517
Singular normal distribution, 30, 31
Singular value decomposition, 498, 634
Spherical distribution, 105
left, 105
right, 105
vector, 105
Spherical normal distribution, 23
Spherically contoured distribution 47
stochastic representation, 49
uniform distribution, 48
Sphericity test, see Testing that a covariance matrix is proportional to a given matrix
Standardized sum statistics, 201
Standardized variable, 22
Steifel manifold, 162
Stochastic convergence, 113
of a sequence of random matrices, 113
Sufficiency, definition of, 83
Sufficiency of sample mean vector and covariance matrix, 83
Surface area of unit sphere, 286
Surfaces o constant density, 22
Symmetric matrix, 626
$T^{2}$-statistic, 176, See also $T^{2}$-test and statistic
$T^{2}$-test and statistic, 173
admissibility of, 196
as Bayes procedure, 199
distribution of statistic, 176
geometric interpretation of statistic, 174
invariance of, 173
as likelinood ratio test of mean vector, 176
limiting distribution of, 176
noncentral distribution of statistic, 186
optimal properties of, 190
power of, 186
tables of, 186
for testing equality of means when covariance matrices are different, 187
for testing equality of two mean vectors
when covariance matrix is unknown, 179
for testing symmetry in mean vector, 182
as uniformly most powerful invariant test of mean vector, 191
Testing that a covariance matrix is a given matrlx, 438
invariant tests of, 442
likelihood ratio criterion for, 438
modified likelihood ratio criterion for, 438 asymptotic expansion of distribution of, 442
moments of, 440
table of significance points, 685
Nagao's criterion, 442
Testing that a covariance matrix is
proportional to a given matrix, 431
invariant tests, 436
likelihood ratio criterion for, 434
admissibility, 458
asymptotic expansion of distribution of, 435
moments of, 434
table of significance points, 682
Nagao's criterion, 437
Testing that a covariance matrix and mean vector are equal to a given matrix and vector, 444
likelihood ratio criterion for, 444
asymptotic expansion of distribution of, 446
moments of, 445
Testing equality of covariance matrices, 412
invarianct tests, 428
likelihood ratio criterion for, 413
invariance of, 414
modified likelihood ratio criterion for, 413
admissibility of, 449
asymptotic expansion of distribution of, 425
distribution of, 420
moments of, 422
table of significance points, 681
Nagao's criterion for, 415
Testing equality of covariance matrices and mean vectors, 415
likelihood ratio criterion for, 415
asymptotic expansion of distribution of, 426
distribution of, 421
moments of, 422
unbiasedness of, 416
Testing independence of sets of variates, 381
and canonical correlations, 504
likelihood ratio criterion for, 384
admissibility of, 401
asymptotic expansion of distribution of, 390
distribution of, 388
invariance of, 386
moments of, 388
monotonicity of power function of, 404
unbiasedness of, 386
Nagao's test, 392
asymptotic expansion of distribution of. 392
stepdown tests, 393
Testing rank of regression matrices, 512
Tests of hypotheses, see Correlation coefficient; Generalized analysis of variance; Linear hypothesis; Mean vector; Multiple correlation coefficient; Partial correlation coefficient; Regression coefficients; $T^{2}$-test and statistic
Tetrachoric functions, 23

Total correlation coefficient, see Correlation coefficient
T. ace of a matrix. 629

Transformation of variables, 12
Unbiased estimator, definition of, 77
Unibased test, definition of, 364
Uniform distribution on unia sphere, 48
on $O(N \times p), 162$
Variance, 17
generalized, see Generalized variance maximum likelihood estimator of, 71
$w(\boldsymbol{A} \mid \boldsymbol{\Sigma}, n), 255$
$W(\Sigma n), 255$
$w^{-1}(B \mid \Psi, m), 272$
$w^{-1}(\mathbf{\Psi}, m), 272$
Wishart distribution, 256
characteristic function of, 258
geometric interpretation of, 256
marginal distributions of, 260
noncentral, 587
for $p=2,124$
$z$, see Fisher's $z$
Zonal polynomials, 473

