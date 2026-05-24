---
citekey: magnusMatrixDifferentialCalculus2019
item_type: book
authors: 'Magnus, Jan R. and Neudecker, Heinz'
year: 2019
title: Matrix Differential Calculus with Applications in Statistics and Econometrics
publisher: Wiley
isbn: 978-1-119-54119-6 978-1-119-54121-9 978-1-119-54116-5
series: Wiley Series in Probability and Statistics
edition: 3rd ed
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\magnus_matrix_differential_calculus_2019.pdf'
pdf_sha256: 6202c98ff3dae17bb0e6763bb7ca8b076ac8f0cc8ce9e09857568e5decf0c71d
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-24T00:38:20Z
---
Matrix Differential Calculus with Applications in Statistics and Econometrics

## WILEY SERIES IN PROBABILITY AND STATISTICS

Established by Walter E. Shewhart and Samuel S. Wilks

Editors: David J. Balding, Noel A. C. Cressie, Garrett M. Fitzmaurice, Geof H. Givens, Harvey Goldstein, Geert Molenberghs, David W. Scott, Adrian F. M. Smith, and Ruey S. Tsay

Editors Emeriti: J. Stuart Hunter, Iain M. Johnstone, Joseph B. Kadane, and Jozef L. Teugels

The Wiley Series in Probability and Statistics is well established and authoritative. It covers many topics of current research interest in both pure and applied statistics and probability theory. Written by leading statisticians and institutions, the titles span both state-of-the-art developments in the field and classical methods.

Reflecting the wide range of current research in statistics, the series encompasses applied, methodological, and theoretical statistics, ranging from applications and new techniques made possible by advances in computerized practice to rigorous treatment of theoretical approaches. This series provides essential and invaluable reading for all statisticians, whether in academia, industry, government, or research.

A complete list of the titles in this series can be found at http://www.wiley.com/go/wsps

# Matrix Differential Calculus with Applications in Statistics and Econometrics 

## Third Edition

## Jan R. Magnus

Department of Econometrics and Operations Research, Vrije Universiteit Amsterdam, The Netherlands
and

## Heinz Neudecker ${ }^{\dagger}$

Amsterdam School of Economics,
University of Amsterdam, The Netherlands

## Wiley

This third edition first published 2019
(c) 2019 John Wiley \& Sons

## Edition History

John Wiley \& Sons (1e, 1988) and John Wiley \& Sons (2e, 1999)

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording or otherwise, except as permitted by law. Advice on how to obtain permission to reuse material from this title is available at http://www.wiley.com/go/permissions.

The right of Jan R. Magnus and Heinz Neudecker to be identified as the authors of this work has been asserted in accordance with law.

## Registered Offices

John Wiley \& Sons, Inc., 111 River Street, Hoboken, NJ 07030, USA
John Wiley \& Sons Ltd, The Atrium, Southern Gate, Chichester, West Sussex, PO19 8SQ, UK

## Editorial Office

9600 Garsington Road, Oxford, OX4 2DQ, UK

For details of our global editorial offices, customer services, and more information about Wiley products visit us at www.wiley.com.

Wiley also publishes its books in a variety of electronic formats and by print-on-demand. Some content that appears in standard print versions of this book may not be available in other formats.

## Limit of Liability/Disclaimer of Warranty

While the publisher and authors have used their best efforts in preparing this work, they make no representations or warranties with respect to the accuracy or completeness of the contents of this work and specifically disclaim all warranties, including without limitation any implied warranties of merchantability or fitness for a particular purpose. No warranty may be created or extended by sales representatives, written sales materials or promotional statements for this work. The fact that an organization, website, or product is referred to in this work as a citation and/or potential source of further information does not mean that the publisher and authors endorse the information or services the organization, website, or product may provide or recommendations it may make. This work is sold with the understanding that the publisher is not engaged in rendering professional services. The advice and strategies contained herein may not be suitable for your situation. You should consult with a specialist where appropriate. Further, readers should be aware that websites listed in this work may have changed or disappeared between when this work was written and when it is read. Neither the publisher nor authors shall be liable for any loss of profit or any other commercial damages, including but not limited to special, incidental, consequential, or other damages.

Library of Congress Cataloging-in-Publication Data applied for
ISBN: 9781119541202

Cover design by Wiley
Cover image: © phochi/Shutterstock
Typeset by the author in LATEX

## Contents

Preface ..... xiii
Part One - Matrices
1 Basic properties of vectors and matrices ..... 3
1 Introduction ..... 3
2 Sets ..... 3
3 Matrices: addition and multiplication ..... 4
4 The transpose of a matrix ..... 6
5 Square matrices ..... 6
6 Linear forms and quadratic forms ..... 7
7 The rank of a matrix ..... 9
8 The inverse ..... 10
9 The determinant ..... 10
10 The trace ..... 11
11 Partitioned matrices ..... 12
12 Complex matrices ..... 14
13 Eigenvalues and eigenvectors ..... 14
14 Schur's decomposition theorem ..... 17
15 The Jordan decomposition ..... 18
16 The singular-value decomposition ..... 20
17 Further results concerning eigenvalues ..... 20
18 Positive (semi)definite matrices ..... 23
19 Three further results for positive definite matrices ..... 25
20 A useful result ..... 26
21 Symmetric matrix functions ..... 27
Miscellaneous exercises ..... 28
Bibliographical notes ..... 30
2 Kronecker products, vec operator, and Moore-Penrose inverse ..... 31
1 Introduction ..... 31
2 The Kronecker product ..... 31
3 Eigenvalues of a Kronecker product ..... 33
4 The vec operator ..... 34
5 The Moore-Penrose (MP) inverse ..... 36
6 Existence and uniqueness of the MP inverse ..... 37
7 Some properties of the MP inverse ..... 38
8 Further properties ..... 39
9 The solution of linear equation systems ..... 41
Miscellaneous exercises ..... 43
Bibliographical notes ..... 45
3 Miscellaneous matrix results ..... 47
1 Introduction ..... 47
2 The adjoint matrix ..... 47
3 Proof of Theorem 3.1 ..... 49
4 Bordered determinants ..... 51
5 The matrix equation $A X=0$ ..... 51
6 The Hadamard product ..... 52
7 The commutation matrix $K_{m n}$ ..... 54
8 The duplication matrix $D_{n}$ ..... 56
9 Relationship between $D_{n+1}$ and $D_{n}$, I ..... 58
10 Relationship between $D_{n+1}$ and $D_{n}$, II ..... 59
11 Conditions for a quadratic form to be positive (negative) subject to linear constraints ..... 60
12 Necessary and sufficient conditions for $r(A: B)=r(A)+r(B)$ ..... 63
13 The bordered Gramian matrix ..... 65
14 The equations $X_{1} A+X_{2} B^{\prime}=G_{1}, X_{1} B=G_{2}$ ..... 67
Miscellaneous exercises ..... 69
Bibliographical notes ..... 70
Part Two - Differentials: the theory
4 Mathematical preliminaries ..... 73
1 Introduction ..... 73
2 Interior points and accumulation points ..... 73
3 Open and closed sets ..... 75
4 The Bolzano-Weierstrass theorem ..... 77
5 Functions ..... 78
6 The limit of a function ..... 79
7 Continuous functions and compactness ..... 80
8 Convex sets ..... 81
9 Convex and concave functions ..... 83
Bibliographical notes ..... 86
5 Differentials and differentiability ..... 87
1 Introduction ..... 87
2 Continuity ..... 88
3 Differentiability and linear approximation ..... 90
4 The differential of a vector function ..... 91
5 Uniqueness of the differential ..... 93
6 Continuity of differentiable functions ..... 94
7 Partial derivatives ..... 95
8 The first identification theorem ..... 96
9 Existence of the differential, I ..... 97
10 Existence of the differential, II ..... 99
11 Continuous differentiability ..... 100
12 The chain rule ..... 100
13 Cauchy invariance ..... 102
14 The mean-value theorem for real-valued functions ..... 103
15 Differentiable matrix functions ..... 104
16 Some remarks on notation ..... 106
17 Complex differentiation ..... 108
Miscellaneous exercises ..... 110
Bibliographical notes ..... 110
6 The second differential ..... 111
1 Introduction ..... 111
2 Second-order partial derivatives ..... 111
3 The Hessian matrix ..... 112
4 Twice differentiability and second-order approximation, I ..... 113
5 Definition of twice differentiability ..... 114
6 The second differential ..... 115
7 Symmetry of the Hessian matrix ..... 117
8 The second identification theorem ..... 119
9 Twice differentiability and second-order approximation, II ..... 119
10 Chain rule for Hessian matrices ..... 121
11 The analog for second differentials ..... 123
12 Taylor's theorem for real-valued functions ..... 124
13 Higher-order differentials ..... 125
14 Real analytic functions ..... 125
15 Twice differentiable matrix functions ..... 126
Bibliographical notes ..... 127
7 Static optimization ..... 129
1 Introduction ..... 129
2 Unconstrained optimization ..... 130
3 The existence of absolute extrema ..... 131
4 Necessary conditions for a local minimum ..... 132
5 Sufficient conditions for a local minimum: first-derivative test ..... 134
6 Sufficient conditions for a local minimum: second-derivative test ..... 136
7 Characterization of differentiable convex functions ..... 138
8 Characterization of twice differentiable convex functions ..... 141
9 Sufficient conditions for an absolute minimum ..... 142
10 Monotonic transformations ..... 143
11 Optimization subject to constraints ..... 144
12 Necessary conditions for a local minimum under constraints ..... 145
13 Sufficient conditions for a local minimum under constraints ..... 149
14 Sufficient conditions for an absolute minimum under constraints ..... 154
15 A note on constraints in matrix form ..... 155
16 Economic interpretation of Lagrange multipliers ..... 155
Appendix: the implicit function theorem ..... 157
Bibliographical notes ..... 159
Part Three - Differentials: the practice
8 Some important differentials ..... 163
1 Introduction ..... 163
2 Fundamental rules of differential calculus ..... 163
3 The differential of a determinant ..... 165
4 The differential of an inverse ..... 168
5 Differential of the Moore-Penrose inverse ..... 169
6 The differential of the adjoint matrix ..... 172
7 On differentiating eigenvalues and eigenvectors ..... 174
8 The continuity of eigenprojections ..... 176
9 The differential of eigenvalues and eigenvectors: symmetric case ..... 180
10 Two alternative expressions for $\mathrm{d} \lambda$ ..... 183
11 Second differential of the eigenvalue function ..... 185
Miscellaneous exercises ..... 186
Bibliographical notes ..... 189
9 First-order differentials and Jacobian matrices ..... 191
1 Introduction ..... 191
2 Classification ..... 192
3 Derisatives ..... 192
4 Derivatives ..... 194
5 Identification of Jacobian matrices ..... 196
6 The first identification table ..... 197
$7 \quad$ Partitioning of the derivative ..... 197
8 Scalar functions of a scalar ..... 198
9 Scalar functions of a vector ..... 198
10 Scalar functions of a matrix, I: trace ..... 199
11 Scalar functions of a matrix, II: determinant ..... 201
12 Scalar functions of a matrix, III: eigenvalue ..... 202
13 Two examples of vector functions ..... 203
14 Matrix functions ..... 204
15 Kronecker products ..... 206
16 Some other problems ..... 208
17 Jacobians of transformations ..... 209
Bibliographical notes ..... 210
10 Second-order differentials and Hessian matrices ..... 211
1 Introduction ..... 211
2 The second identification table ..... 211
3 Linear and quadratic forms ..... 212
4 A useful theorem ..... 213
5 The determinant function ..... 214
6 The eigenvalue function ..... 215
7 Other examples ..... 215
8 Composite functions ..... 217
9 The eigenvector function ..... 218
10 Hessian of matrix functions, I ..... 219
11 Hessian of matrix functions, II ..... 219
Miscellaneous exercises ..... 220
Part Four - Inequalities
11 Inequalities ..... 225
1 Introduction ..... 225
2 The Cauchy-Schwarz inequality ..... 226
3 Matrix analogs of the Cauchy-Schwarz inequality ..... 227
4 The theorem of the arithmetic and geometric means ..... 228
5 The Rayleigh quotient ..... 230
6 Concavity of $\lambda_{1}$ and convexity of $\lambda_{n}$ ..... 232
7 Variational description of eigenvalues ..... 232
8 Fischer's min-max theorem ..... 234
9 Monotonicity of the eigenvalues ..... 236
10 The Poincaré separation theorem ..... 236
11 Two corollaries of Poincaré's theorem ..... 237
12 Further consequences of the Poincaré theorem ..... 238
13 Multiplicative version ..... 239
14 The maximum of a bilinear form ..... 241
15 Hadamard's inequality ..... 242
16 An interlude: Karamata's inequality ..... 242
17 Karamata's inequality and eigenvalues ..... 244
18 An inequality concerning positive semidefinite matrices ..... 245
19 A representation theorem for $\left(\sum a_{i}^{p}\right)^{1 / p}$ ..... 246
20 A representation theorem for $\left(\operatorname{tr} A^{p}\right)^{1 / p}$ ..... 247
21 Hölder's inequality ..... 248
22 Concavity of $\log |A|$ ..... 250
23 Minkowski's inequality ..... 251
24 Quasilinear representation of $|A|^{1 / n}$ ..... 253
25 Minkowski's determinant theorem ..... 255
26 Weighted means of order $p$ ..... 256
27 Schlömilch's inequality ..... 258
28 Curvature properties of $M_{p}(x, a)$ ..... 259
29 Least squares ..... 260
30 Generalized least squares ..... 261
31 Restricted least squares ..... 262
32 Restricted least squares: matrix version ..... 264
Miscellaneous exercises ..... 265
Bibliographical notes ..... 269
Part Five - The linear model
12 Statistical preliminaries ..... 273
1 Introduction ..... 273
2 The cumulative distribution function ..... 273
3 The joint density function ..... 274
4 Expectations ..... 274
5 Variance and covariance ..... 275
6 Independence of two random variables ..... 277
$7 \quad$ Independence of $n$ random variables ..... 279
8 Sampling ..... 279
9 The one-dimensional normal distribution ..... 279
10 The multivariate normal distribution ..... 280
11 Estimation ..... 282
Miscellaneous exercises ..... 282
Bibliographical notes ..... 283
13 The linear regression model ..... 285
1 Introduction ..... 285
2 Affine minimum-trace unbiased estimation ..... 286
3 The Gauss-Markov theorem ..... 287
4 The method of least squares ..... 290
5 Aitken's theorem ..... 291
6 Multicollinearity ..... 293
7 Estimable functions ..... 295
8 Linear constraints: the case $\mathcal{M}\left(R^{\prime}\right) \subset \mathcal{M}\left(X^{\prime}\right)$ ..... 296
9 Linear constraints: the general case ..... 300
10 Linear constraints: the case $\mathcal{M}\left(R^{\prime}\right) \cap \mathcal{M}\left(X^{\prime}\right)=\{0\}$ ..... 302
11 A singular variance matrix: the case $\mathcal{M}(X) \subset \mathcal{M}(V)$ ..... 304
12 A singular variance matrix: the case $r\left(X^{\prime} V^{+} X\right)=r(X)$ ..... 305
13 A singular variance matrix: the general case, I ..... 307
14 Explicit and implicit linear constraints ..... 307
15 The general linear model, I ..... 310
16 A singular variance matrix: the general case, II ..... 311
17 The general linear model, II ..... 314
18 Generalized least squares ..... 315
19 Restricted least squares ..... 316
Miscellaneous exercises ..... 318
Bibliographical notes ..... 319
14 Further topics in the linear model ..... 321
1 Introduction ..... 321
2 Best quadratic unbiased estimation of $\sigma^{2}$ ..... 322
3 The best quadratic and positive unbiased estimator of $\sigma^{2}$ ..... 322
4 The best quadratic unbiased estimator of $\sigma^{2}$ ..... 324
5 Best quadratic invariant estimation of $\sigma^{2}$ ..... 326
6 The best quadratic and positive invariant estimator of $\sigma^{2}$ ..... 327
7 The best quadratic invariant estimator of $\sigma^{2}$ ..... 329
8 Best quadratic unbiased estimation: multivariate normal case ..... 330
9 Bounds for the bias of the least-squares estimator of $\sigma^{2}$, I ..... 332
10 Bounds for the bias of the least-squares estimator of $\sigma^{2}$, II ..... 333
11 The prediction of disturbances ..... 335
12 Best linear unbiased predictors with scalar variance matrix ..... 336
13 Best linear unbiased predictors with fixed variance matrix, I ..... 338
14 Best linear unbiased predictors with fixed variance matrix, II ..... 340
15 Local sensitivity of the posterior mean ..... 341
16 Local sensitivity of the posterior precision ..... 342
Bibliographical notes ..... 344
Part Six - Applications to maximum likelihood estimation
15 Maximum likelihood estimation ..... 347
1 Introduction ..... 347
2 The method of maximum likelihood (ML) ..... 347
3 ML estimation of the multivariate normal distribution ..... 348
4 Symmetry: implicit versus explicit treatment ..... 350
5 The treatment of positive definiteness ..... 351
6 The information matrix ..... 352
7 ML estimation of the multivariate normal distribution: distinct means ..... 354
8 The multivariate linear regression model ..... 354
9 The errors-in-variables model ..... 357
10 The nonlinear regression model with normal errors ..... 359
11 Special case: functional independence of mean and variance parameters ..... 361
12 Generalization of Theorem 15.6 ..... 362
Miscellaneous exercises ..... 364
Bibliographical notes ..... 365
16 Simultaneous equations ..... 367
1 Introduction ..... 367
2 The simultaneous equations model ..... 367
3 The identification problem ..... 369
4 Identification with linear constraints on $B$ and $\Gamma$ only ..... 371
5 Identification with linear constraints on $B, \Gamma$, and $\Sigma$ ..... 371
6 Nonlinear constraints ..... 373
7 FIML: the information matrix (general case) ..... 374
8 FIML: asymptotic variance matrix (special case) ..... 376
9 LIML: first-order conditions ..... 378
10 LIML: information matrix ..... 381
11 LIML: asymptotic variance matrix ..... 383
Bibliographical notes ..... 388
17 Topics in psychometrics ..... 389
1 Introduction ..... 389
2 Population principal components ..... 390
3 Optimality of principal components ..... 391
4 A related result ..... 392
5 Sample principal components ..... 393
6 Optimality of sample principal components ..... 395
7 One-mode component analysis ..... 395
8 One-mode component analysis and sample principal components ..... 398
9 Two-mode component analysis ..... 399
10 Multimode component analysis ..... 400
11 Factor analysis ..... 404
12 A zigzag routine ..... 407
13 A Newton-Raphson routine ..... 408
14 Kaiser's varimax method ..... 412
15 Canonical correlations and variates in the population ..... 414
16 Correspondence analysis ..... 417
17 Linear discriminant analysis ..... 418
Bibliographical notes ..... 419
Part Seven - Summary
18 Matrix calculus: the essentials ..... 423
1 Introduction ..... 423
2 Differentials ..... 424
3 Vector calculus ..... 426
4 Optimization ..... 429
5 Least squares ..... 431
6 Matrix calculus ..... 432
7 Interlude on linear and quadratic forms ..... 434
8 The second differential ..... 434
9 Chain rule for second differentials ..... 436
10 Four examples ..... 438
11 The Kronecker product and vec operator ..... 439
12 Identification ..... 441
13 The commutation matrix ..... 442
14 From second differential to Hessian ..... 443
15 Symmetry and the duplication matrix ..... 444
16 Maximum likelihood ..... 445
Further reading ..... 448
Bibliography ..... 449
Index of symbols ..... 467
Subject index ..... 471

## Preface

## Preface to the first edition

There has been a long-felt need for a book that gives a self-contained and unified treatment of matrix differential calculus, specifically written for econometricians and statisticians. The present book is meant to satisfy this need. It can serve as a textbook for advanced undergraduates and postgraduates in econometrics and as a reference book for practicing econometricians. Mathematical statisticians and psychometricians may also find something to their liking in the book.

When used as a textbook, it can provide a full-semester course. Reasonable proficiency in basic matrix theory is assumed, especially with the use of partitioned matrices. The basics of matrix algebra, as deemed necessary for a proper understanding of the main subject of the book, are summarized in Part One, the first of the book's six parts. The book also contains the essentials of multivariable calculus but geared to and often phrased in terms of differentials.

The sequence in which the chapters are being read is not of great consequence. It is fully conceivable that practitioners start with Part Three (Differentials: the practice) and, dependent on their predilections, carry on to Parts Five or Six, which deal with applications. Those who want a full understanding of the underlying theory should read the whole book, although even then they could go through the necessary matrix algebra only when the specific need arises.

Matrix differential calculus as presented in this book is based on differentials, and this sets the book apart from other books in this area. The approach via differentials is, in our opinion, superior to any other existing approach. Our principal idea is that differentials are more congenial to multivariable functions as they crop up in econometrics, mathematical statistics, or psychometrics than derivatives, although from a theoretical point of view the two concepts are equivalent.

The book falls into six parts. Part One deals with matrix algebra. It lists, and also often proves, items like the Schur, Jordan, and singular-value decompositions; concepts like the Hadamard and Kronecker products; the vec operator; the commutation and duplication matrices; and the Moore-Penrose
inverse. Results on bordered matrices (and their determinants) and (linearly restricted) quadratic forms are also presented here.

Part Two, which forms the theoretical heart of the book, is entirely devoted to a thorough treatment of the theory of differentials, and presents the essentials of calculus but geared to and phrased in terms of differentials. First and second differentials are defined, 'identification' rules for Jacobian and Hessian matrices are given, and chain rules derived. A separate chapter on the theory of (constrained) optimization in terms of differentials concludes this part.

Part Three is the practical core of the book. It contains the rules for working with differentials, lists the differentials of important scalar, vector, and matrix functions (inter alia eigenvalues, eigenvectors, and the MoorePenrose inverse) and supplies 'identification' tables for Jacobian and Hessian matrices.

Part Four, treating inequalities, owes its existence to our feeling that econometricians should be conversant with inequalities, such as the Cauchy-Schwarz and Minkowski inequalities (and extensions thereof), and that they should also master a powerful result like Poincaré's separation theorem. This part is to some extent also the case history of a disappointment. When we started writing this book we had the ambition to derive all inequalities by means of matrix differential calculus. After all, every inequality can be rephrased as the solution of an optimization problem. This proved to be an illusion, due to the fact that the Hessian matrix in most cases is singular at the optimum point.

Part Five is entirely devoted to applications of matrix differential calculus to the linear regression model. There is an exhaustive treatment of estimation problems related to the fixed part of the model under various assumptions concerning ranks and (other) constraints. Moreover, it contains topics relating to the stochastic part of the model, viz. estimation of the error variance and prediction of the error term. There is also a small section on sensitivity analysis. An introductory chapter deals with the necessary statistical preliminaries.

Part Six deals with maximum likelihood estimation, which is of course an ideal source for demonstrating the power of the propagated techniques. In the first of three chapters, several models are analysed, inter alia the multivariate normal distribution, the errors-in-variables model, and the nonlinear regression model. There is a discussion on how to deal with symmetry and positive definiteness, and special attention is given to the information matrix. The second chapter in this part deals with simultaneous equations under normality conditions. It investigates both identification and estimation problems, subject to various (non)linear constraints on the parameters. This part also discusses full-information maximum likelihood (FIML) and limited-information maximum likelihood (LIML), with special attention to the derivation of asymptotic variance matrices. The final chapter addresses itself to various psychometric problems, inter alia principal components, multimode component analysis, factor analysis, and canonical correlation.

All chapters contain many exercises. These are frequently meant to be complementary to the main text.

A large number of books and papers have been published on the theory and applications of matrix differential calculus. Without attempting to describe their relative virtues and particularities, the interested reader may wish to consult Dwyer and Macphail (1948), Bodewig (1959), Wilkinson (1965), Dwyer (1967), Neudecker (1967, 1969), Tracy and Dwyer (1969), Tracy and Singh (1972), McDonald and Swaminathan (1973), MacRae (1974), Balestra (1976), Bentler and Lee (1978), Henderson and Searle (1979), Wong and Wong (1979, 1980), Nel (1980), Rogers (1980), Wong (1980, 1985), Graham (1981), McCulloch (1982), Schönemann (1985), Magnus and Neudecker (1985), Pollock (1985), Don (1986), and Kollo (1991). The papers by Henderson and Searle (1979) and Nel (1980), and Rogers' (1980) book contain extensive bibliographies.

The two authors share the responsibility for Parts One, Three, Five, and Six, although any new results in Part One are due to Magnus. Parts Two and Four are due to Magnus, although Neudecker contributed some results to Part Four. Magnus is also responsible for the writing and organization of the final text.

We wish to thank our colleagues F. J. H. Don, R. D. H. Heijmans, D. S. G. Pollock, and R. Ramer for their critical remarks and contributions. The greatest obligation is owed to Sue Kirkbride at the London School of Economics who patiently and cheerfully typed and retyped the various versions of the book. Partial financial support was provided by the Netherlands Organization for the Advancement of Pure Research (Z. W. O.) and the Suntory Toyota International Centre for Economics and Related Disciplines at the London School of Economics.

London/Amsterdam
April 1987

Jan R. Magnus
Heinz Neudecker

## Preface to the first revised printing

Since this book first appeared - now almost four years ago - many of our colleagues, students, and other readers have pointed out typographical errors and have made suggestions for improving the text. We are particularly grateful to R. D. H. Heijmans, J. F. Kiviet, I. J. Steyn, and G. Trenkler. We owe the greatest debt to F. Gerrish, formerly of the School of Mathematics in the Polytechnic, Kingston-upon-Thames, who read Chapters 1-11 with awesome precision and care and made numerous insightful suggestions and constructive remarks. We hope that this printing will continue to trigger comments from our readers.

London/Tilburg/Amsterdam
February 1991

Jan R. Magnus
Heinz Neudecker

## Preface to the second edition

A further seven years have passed since our first revision in 1991. We are happy to see that our book is still being used by colleagues and students. In this revision we attempted to reach three goals. First, we made a serious attempt to keep the book up-to-date by adding many recent references and new exercises. Second, we made numerous small changes throughout the text, improving the clarity of exposition. Finally, we corrected a number of typographical and other errors.

The structure of the book and its philosophy are unchanged. Apart from a large number of small changes, there are two major changes. First, we interchanged Sections 12 and 13 of Chapter 1, since complex numbers need to be discussed before eigenvalues and eigenvectors, and we corrected an error in Theorem 1.7. Second, in Chapter 17 on psychometrics, we rewrote Sections 8-10 relating to the Eckart-Young theorem.

We are grateful to Karim Abadir, Paul Bekker, Hamparsum Bozdogan, Michael Browne, Frank Gerrish, Kaddour Hadri, Tõnu Kollo, Shuangzhe Liu, Daan Nel, Albert Satorra, Kazuo Shigemasu, Jos ten Berge, Peter ter Berg, Götz Trenkler, Haruo Yanai, and many others for their thoughtful and constructive comments. Of course, we welcome further comments from our readers.

Tilburg/Amsterdam
March 1998

Jan R. Magnus
Heinz Neudecker

## Preface to the third edition

Twenty years have passed since the appearance of the second edition and thirty years since the book first appeared. This is a long time, but the book still lives. Unfortunately, my coauthor Heinz Neudecker does not; he died in December 2017. Heinz was my teacher at the University of Amsterdam and I was fortunate to learn the subject of matrix calculus through differentials (then in its infancy) from his lectures and personal guidance. This technique is still a remarkably powerful tool, and Heinz Neudecker must be regarded as its founding father.

The original text of the book was written on a typewriter and then handed over to the publisher for typesetting and printing. When it came to the second edition, the typeset material could no longer be found, which is why the second edition had to be produced in an ad hoc manner which was not satisfactory. Many people complained about this, to me and to the publisher, and the publisher offered us to produce a new edition, freshly typeset, which would look good. In the mean time, my Russian colleagues had proposed to translate the book into Russian, and I realized that this would only be feasible if they had a good English EATEX text. So, my secretary Josette Janssen at Tilburg University and I produced a $\mathrm{EAT}_{\mathrm{EX}}$ text with expert advice from Jozef Pijnenburg. In the process of retyping the manuscript, many small changes
were made to improve the readability and consistency of the text, but the structure of the book was not changed. The English $\mathrm{ET}_{\mathrm{EX}} \mathrm{X}$ version was then used as the basis for the Russian edition,

## Matrichnoe Differenzial'noe Ischislenie s Prilozhenijami k Statistike i Ekonometrike,

translated by my friends Anatoly Peresetsky and Pavel Katyshev, and published by Fizmatlit Publishing House, Moscow, 2002. The current third edition is based on this English $\mathrm{ET}_{\mathrm{EX}} \mathrm{X}$ version, although I have taken the opportunity to make many improvements to the presentation of the material.

Of course, this was not the only reason for producing a third edition. It was time to take a fresh look at the material and to update the references. I felt it was appropriate to stay close to the original text, because this is the book that Heinz and I conceived and the current text is a new edition, not a new book. The main changes relative to the second edition are as follows:

- Some subjects were treated insufficiently (some of my friends would say 'incorrectly') and I have attempted to repair these omissions. This applies in particular to the discussion on matrix functions (Section 1.21), complex differentiation (Section 5.17), and Jacobians of transformations (Section 9.17).
- The text on differentiating eigenvalues and eigenvectors and associated continuity issues has been rewritten, see Sections 8.7-8.11.
- Chapter 10 has been completely rewritten, because I am now convinced that it is not useful to define Hessian matrices for vector or matrix functions. So I now define Hessian matrices only for scalar functions and for individual components of vector functions and individual elements of matrix functions. This makes life much easier.
- I have added two additional sections at the end of Chapter 17 on psychometrics, relating to correspondence analysis and linear discriminant analysis.
- Chapter 18 is new. It can be read without consulting the other chapters and provides a summary of the whole book. It can therefore be used as an introduction to matrix calculus for advanced undergraduates or Master's and PhD students in economics, statistics, mathematics, and engineering who want to know how to apply matrix calculus without going into all the theoretical details.

In addition, many small changes have been made, references have been updated, and exercises have been added. Over the past 30 years, I received many queries, problems, and requests from readers, about once every 2 weeks, which amounts to about 750 queries in 30 years. I responded to all of them and a number of these problems appear in the current text as exercises.

I am grateful to Don Andrews, Manuel Arellano, Richard Baillie, Luc Bauwens, Andrew Chesher, Gerda Claeskens, Russell Davidson, Jean-Marie

Dufour, Ronald Gallant, Eric Ghysels, Bruce Hansen, Grant Hillier, Cheng Hsiao, Guido Imbens, Guido Kuersteiner, Offer Lieberman, Esfandiar Maasoumi, Whitney Newey, Kazuhiro Ohtani, Enrique Sentana, Cezary Sielużycki, Richard Smith, Götz Trenkler, and Farshid Vahid for general encouragement and specific suggestions; to Henk Pijls for answering my questions on complex differentiation and Michel van de Velden for help on psychometric issues; to Jan Brinkhuis, Chris Muris, Franco Peracchi, Andrey Vasnev, Wendun Wang, and Yuan Yue on commenting on the new Chapter 18; to Ang Li for exceptional research assistance in updating the literature; and to Ilka van de Werve for expertly redrawing the figures. No blame attaches to any of these people in case there are remaining errors, ambiguities, or omissions; these are entirely my own responsibility, especially since I have not always followed their advice.

Cross-References. The numbering of theorems, propositions, corollaries, figures, tables, assumptions, examples, and definitions is with two digits, so that Theorem 3.5 refers to Theorem 5 in Chapter 3. Sections are numbered 1, 2,... within each chapter but always referenced with two digits so that Section 5 in Chapter 3 is referred to as Section 3.5. Equations are numbered (1), (2), ... within each chapter, and referred to with one digit if it refers to the same chapter; if it refers to another chapter we write, for example, see Equation (16) in Chapter 5. Exercises are numbered 1, 2,... after a section.

Notation. Special symbols are used to denote the derivative (matrix) D and the Hessian (matrix) H. The differential operator is denoted by d. The third edition follows the notation of earlier editions with the following exceptions. First, the symbol for the vector $(1,1, \ldots, 1)^{\prime}$ has been altered from a calligraphic $s$ to $\imath$ (dotless $i$ ); second, the symbol if for imaginary root has been replaced by the more common $i$; third, $\mathrm{v}(A)$, the vector indicating the essentially distinct components of a symmetric matrix $A$, has been replaced by $\operatorname{vech}(A)$; fourth, the symbols for expectation, variance, and covariance (previously $\mathcal{E}, \mathcal{V}$, and $\mathcal{C}$ ) have been replaced by E , var, and cov, respectively; and fifth, we now denote the normal distribution by N (previously $\mathcal{N}$ ). A list of all symbols is presented in the Index of Symbols at the end of the book.

Brackets are used sparingly. We write $\operatorname{tr} A$ instead of $\operatorname{tr}(A)$, while $\operatorname{tr} A B$ denotes $\operatorname{tr}(A B)$, not $(\operatorname{tr} A) B$. Similarly, vec $A B$ means vec $(A B)$ and $\mathrm{d} X Y$ means $\mathrm{d}(X Y)$. In general, we only place brackets when there is a possibility of ambiguity.

I worked on the third edition between April and November 2018. I hope the book will continue to be useful for a few more years, and of course I welcome comments from my readers.

Note to the reader:
This preview of the the third edition of Matrix Differential Calculus contains only Chapter 18, the final chapter. This chapter is different from the other chapters in the book and can be read independently. It attempts to summarize matrix calculus for the user who does not want to go into all the details.

Chapter 18 is available free of charge. When quoting results from this chapter, please refer to:

Magnus, J. R. and H. Neudecker (2019). Matrix Differential Calculus with Applications in Statistics and Econometrics, Third Edition, John Wiley, New York.

## CHAPTER 18

## Matrix calculus: the essentials

## 1 INTRODUCTION

This chapter differs from the other chapters in this book. It attempts to summarize the theory and the practical applications of matrix calculus in a few pages, leaving out all the subtleties that the typical user will not need. It also serves as an introduction for (advanced) undergraduates or Master's and PhD students in economics, statistics, mathematics, and engineering, who want to know how to apply matrix calculus without going into all the theoretical details. The chapter can be read independently of the rest of the book.

We begin by introducing the concept of a differential, which lies at the heart of matrix calculus. The key advantage of the differential over the more common derivative is the following. Consider the linear vector function $f(x)= A x$ where $A$ is an $m \times n$ matrix of constants. Then, $f(x)$ is an $m \times 1$ vector function of an $n \times 1$ vector $x$, and the derivative $\mathrm{D} f(x)$ is an $m \times n$ matrix (in this case, the matrix $A$ ). But the differential $\mathrm{d} f$ remains an $m \times 1$ vector. In general, the differential $\mathrm{d} f$ of a vector function $f=f(x)$ has the same dimension as $f$, irrespective of the dimension of the vector $x$, in contrast to the derivative $\mathrm{D} f(x)$.

The advantage is even larger for matrices. The differential $\mathrm{d} F$ of a matrix function $F(X)$ has the same dimension as $F$, irrespective of the dimension of the matrix $X$. The practical importance of working with differentials is huge and will be demonstrated through many examples.

We next discuss vector calculus and optimization, with and without constraints. We emphasize the importance of a correct definition and notation for the derivative, present the 'first identification theorem', which links the first differential with the first derivative, and apply these results to least squares. Then we extend the theory from vector calculus to matrix calculus and obtain the differentials of the determinant and inverse.

Matrix Differential Calculus with Applications in Statistics and Econometrics, Third Edition. Jan R. Magnus and Heinz Neudecker.
© 2019 John Wiley \& Sons Ltd. Published 2019 by John Wiley \& Sons Ltd.

A brief interlude on quadratic forms follows, the primary purpose of which is to show that if $x^{\prime} A x=0$ for all $x$, then this does not imply that $A$ is zero, but only that $A^{\prime}=-A$. We then define the second differential and the Hessian matrix, prove the 'second identification theorem', which links the second differential with the Hessian matrix, and discuss the chain rule for second differentials. The first part of this chapter ends with four examples.

In the second (more advanced) part, we introduce the vec operator and the Kronecker product, and discuss symmetry (commutation and duplication matrices). Many examples are provided to clarify the technique. The chapter ends with an application to maximum likelihood estimation, where all elements discussed in the chapter come together.

The following notation is used. Unless specified otherwise, $\phi$ denotes a scalar function, $f$ a vector function, and $F$ a matrix function. Also, $x$ denotes a scalar or vector argument, and $X$ a matrix argument. All functions and variables in this chapter are real. Parentheses are used sparingly. We write $\mathrm{d} X, \operatorname{tr} X$, and vec $X$ without parentheses, and also $\mathrm{d} X Y, \operatorname{tr} X Y$, and vec $X Y$ instead of $\mathrm{d}(X Y), \operatorname{tr}(X Y)$, and $\operatorname{vec}(X Y)$. However, we write $\operatorname{vech}(X)$ with parentheses for historical reasons.

## 2 DIFFERENTIALS

We assume that the reader is familiar with high-school calculus. This includes not only simple derivatives, such as

$$
\frac{d x^{2}}{d x}=2 x, \quad \frac{d e^{x}}{d x}=e^{x}, \quad \frac{d \sin x}{d x}=\cos x
$$

but also the chain rule, for example:

$$
\frac{d(\sin x)^{2}}{d x}=\frac{d(\sin x)^{2}}{d \sin x} \frac{d \sin x}{d x}=2 \sin x \cos x=\sin (2 x)
$$

We now introduce the concept of a differential, by expressing (1) as

$$
\mathrm{d} x^{2}=2 x \mathrm{~d} x, \quad \mathrm{~d} e^{x}=e^{x} \mathrm{~d} x, \quad \mathrm{~d} \sin x=\cos x \mathrm{~d} x,
$$

where we write d rather than $d$ to emphasize that this is a differential rather than a derivative. The two concepts are closely related, but they are not the same.

The concept of differential may be confusing for students who remember their mathematics teacher explain to them that it is wrong to view $d x^{2} / d x$ as a fraction. They might wonder what $\mathrm{d} x$ and $\mathrm{d} x^{2}$ really are. What does $\mathrm{d} x^{2}= 2 x \mathrm{~d} x$ mean? From a geometric point of view, it means that if we replace the graph of the function $\phi(x)=x^{2}$ at some value $x$ by its linear approximation, that is, by the tangent line at the point $\left(x, x^{2}\right)$, then an increment $\mathrm{d} x$ in $x$ leads to an increment $\mathrm{d} x^{2}=2 x \mathrm{~d} x$ in $x^{2}$ in linear approximation. From an algebraic point of view, if we replace $x$ by $x+\mathrm{d} x$ ('increment $\mathrm{d} x$ '), then $\phi(x)$ is replaced by

$$
\phi(x+\mathrm{d} x)=(x+\mathrm{d} x)^{2}=x^{2}+2 x \mathrm{~d} x+(\mathrm{d} x)^{2} .
$$

For small $\mathrm{d} x$, the term $(\mathrm{d} x)^{2}$ will be very small and, if we ignore it, we obtain the linear approximation $x^{2}+2 x \mathrm{~d} x$. The differential $\mathrm{d} x^{2}$ is, for a given value of $x$, just a function of the real variable $\mathrm{d} x$, given by the formula $\mathrm{d} x^{2}=2 x \mathrm{~d} x$.

This may sound complicated, but working with differentials is easy. The passage from (1) to (2) holds generally for any (differentiable) real-valued function $\phi$, and the differential $\mathrm{d} \phi$ is thus given by the formula

$$
\mathrm{d} \phi=\frac{d \phi(x)}{d x} \mathrm{~d} x
$$

Put differently,

$$
\mathrm{d} \phi=\alpha(x) \mathrm{d} x \Longleftrightarrow \frac{d \phi(x)}{d x}=\alpha(x),
$$

where $\alpha$ may depend on $x$, but not on $\mathrm{d} x$. Equation (3) is a special case of the first identification theorem (Theorem 18.1) in the next section. It shows that we can identify the derivative from the differential (and vice versa), and it shows that the new concept differential is equivalent to the familiar concept derivative. We will always work with the differential, as this has great practical advantages.

The differential is an operator, in fact a linear operator, and we have

$$
\mathrm{d} a=0, \quad \mathrm{~d}(a x)=a \mathrm{~d} x,
$$

for any scalar constant $a$, and

$$
\mathrm{d}(x+y)=\mathrm{d} x+\mathrm{d} y, \quad \mathrm{~d}(x-y)=\mathrm{d} x-\mathrm{d} y .
$$

For the product and the ratio, we have

$$
\mathrm{d}(x y)=(\mathrm{d} x) y+x \mathrm{~d} y, \quad \mathrm{~d}\left(\frac{1}{x}\right)=-\frac{\mathrm{d} x}{x^{2}} \quad(x \neq 0),
$$

and, in addition to the differential of the exponential function $\mathrm{d} e^{x}=e^{x} \mathrm{~d} x$,

$$
\mathrm{d} \log x=\frac{\mathrm{d} x}{x} \quad(x>0)
$$

The chain rule, well-known for derivatives, also applies to differentials and is then called Cauchy's rule of invariance. For example,

$$
\mathrm{d}(\sin x)^{2}=2 \sin x \mathrm{~d} \sin x=2 \sin x \cos x \mathrm{~d} x=\sin (2 x) \mathrm{d} x,
$$

or

$$
\mathrm{d} e^{x^{2}}=e^{x^{2}} \mathrm{~d} x^{2}=2 e^{x^{2}} x \mathrm{~d} x
$$

or, combining the two previous examples,

$$
\begin{aligned}
\mathrm{d} e^{\sin x^{2}} & =e^{\sin x^{2}} \mathrm{~d} \sin x^{2}=e^{\sin x^{2}} \cos x^{2} \mathrm{~d} x^{2} \\
& =2 x e^{\sin x^{2}} \cos x^{2} \mathrm{~d} x .
\end{aligned}
$$

The chain rule is a good example of the general principle that things are easier - sometimes a bit, sometimes a lot - in terms of differentials than in terms of derivatives. The chain rule in terms of differentials states that taking differentials of functions preserves composition of functions. This is easier than the chain rule in terms of derivatives. Consider, for example, the function $z=h(x)=(\sin x)^{2}$ as the composition of the functions

$$
y=g(x)=\sin x, \quad z=f(y)=y^{2}
$$

so that $h(x)=f(g(x))$. Then $\mathrm{d} y=\cos x \mathrm{~d} x$, and hence

$$
\mathrm{d} z=2 y \mathrm{~d} y=2 y \cos x \mathrm{~d} x=2 \sin x \cos x \mathrm{~d} x
$$

as expected.
The chain rule is, of course, a key instrument in differential calculus. Suppose we realize that $x$ in (4) depends on $t$, say $x=t^{2}$. Then, we do not need to compute the differential of $\left(\sin t^{2}\right)^{2}$ all over again. We can use (4) and simply write

$$
\mathrm{d}\left(\sin t^{2}\right)^{2}=\sin \left(2 t^{2}\right) \mathrm{d} t^{2}=2 t \sin \left(2 t^{2}\right) \mathrm{d} t .
$$

The chain rule thus allows us to apply the rules of calculus sequentially, one after another.

In this section, we have only concerned ourselves with scalar functions of a scalar argument, and the reader may wonder why we bother to introduce differentials. They do not seem to have a great advantage over the more familiar derivatives. This is true, but when we come to vector functions of vector arguments, then the advantage will become clear.

## 3 VECTOR CALCULUS

Let $x(n \times 1)$ and $y(m \times 1)$ be two vectors and let $y$ be a function of $x$, say $y=f(x)$. What is the derivative of $y$ with respect to $x$ ? To help us answer this question, we first consider the linear equation

$$
y=f(x)=A x
$$

where $A$ is an $m \times n$ matrix of constants. The derivative is $A$ and we write

$$
\frac{\partial f(x)}{\partial x^{\prime}}=A .
$$

The notation $\partial f(x) / \partial x^{\prime}$ is just notation, nothing else. We sometimes write the derivative as $\mathrm{D} f(x)$ or as $\mathrm{D} f$, but we avoid the notation $f^{\prime}(x)$ because this may cause confusion with the transpose. The proposed notation emphasizes that we differentiate an $m \times 1$ column vector $f$ with respect to a $1 \times n$ row vector $x^{\prime}$, resulting in an $m \times n$ derivative matrix.

More generally, the derivative of $f(x)$ is an $m \times n$ matrix containing all partial derivatives $\partial f_{i}(x) / \partial x_{j}$, but in a specific ordering, namely

$$
\frac{\partial f(x)}{\partial x^{\prime}}=\left(\begin{array}{cccc}
\partial f_{1}(x) / \partial x_{1} & \partial f_{1}(x) / \partial x_{2} & \ldots & \partial f_{1}(x) / \partial x_{n} \\
\partial f_{2}(x) / \partial x_{1} & \partial f_{2}(x) / \partial x_{2} & \ldots & \partial f_{2}(x) / \partial x_{n} \\
\vdots & \vdots & & \vdots \\
\partial f_{m}(x) / \partial x_{1} & \partial f_{m}(x) / \partial x_{2} & \ldots & \partial f_{m}(x) / \partial x_{n}
\end{array}\right) .
$$

There is only one definition of a vector derivative, and this is it. Of course, one can organize the $m n$ partial derivatives in different ways, but these other combinations of the partial derivatives are not derivatives, have no practical use, and should be avoided.

Notice that each row of the derivative in (6) contains the partial derivatives of one element of $f$ with respect to all elements of $x$, and that each column contains the partial derivatives of all elements of $f$ with respect to one element of $x$. This is an essential characteristic of the derivative. As a consequence, the derivative of a scalar function $y=\phi(x)$, such as $y=a^{\prime} x$ (where $a$ is a vector of constants), is a row vector; in this case, $a^{\prime}$. So the derivative of $a^{\prime} x$ is $a^{\prime}$, not $a$.

The rules in the previous section imply that the following rules apply to vector differentials, where $x$ and $y$ are vectors and $a$ is a vector of real constants, all of the same order:

$$
\begin{aligned}
& \mathrm{d} a=0, \quad \mathrm{~d}\left(x^{\prime}\right)=(\mathrm{d} x)^{\prime}, \quad \mathrm{d}\left(a^{\prime} x\right)=a^{\prime} \mathrm{d} x, \\
& \mathrm{~d}(x+y)=\mathrm{d} x+\mathrm{d} y, \quad \mathrm{~d}(x-y)=\mathrm{d} x-\mathrm{d} y,
\end{aligned}
$$

and

$$
\mathrm{d}\left(x^{\prime} y\right)=(\mathrm{d} x)^{\prime} y+x^{\prime} \mathrm{d} y
$$

Now we can see the advantage of working with differentials rather than with derivatives. When we have an $m \times 1$ vector $y$, which is a function of an $n \times 1$ vector of variables $x$, say $y=f(x)$, then the derivative is an $m \times n$ matrix, but the differential $\mathrm{d} y$ or $\mathrm{d} f$ remains an $m \times 1$ vector. This is relevant for vector functions, and even more relevant for matrix functions and for second-order derivatives, as we shall see later. The practical advantage of working with differentials is therefore that the order does not increase but always stays the same.

Corresponding to the identification result (3), we have the following relationship between the differential and the derivative.

## Theorem 18.1 (first identification theorem):

$$
\mathrm{d} f=A(x) \mathrm{d} x \Longleftrightarrow \frac{\partial f(x)}{\partial x^{\prime}}=A(x)
$$

This theorem shows that there is a one-to-one correspondence between first-order differentials and first-order derivatives. In other words, the differential identifies the derivative.

Example 18.1: Consider the linear function $\phi(x)=a^{\prime} x$, where $a$ is a vector of constants. This gives

$$
\mathrm{d} \phi=a^{\prime} \mathrm{d} x
$$

so that the derivative is $a^{\prime}$, as we have seen before.
Example 18.2a: Next, consider the quadratic function $\phi(x)=x^{\prime} A x$, where $A$ is a matrix of constants. Here, we have

$$
\mathrm{d} \phi=(\mathrm{d} x)^{\prime} A x+x^{\prime} A \mathrm{~d} x=x^{\prime} A^{\prime} \mathrm{d} x+x^{\prime} A \mathrm{~d} x=x^{\prime}\left(A+A^{\prime}\right) \mathrm{d} x .
$$

The derivative is $x^{\prime}\left(A+A^{\prime}\right)$, and in the special case where $A$ is symmetric, the derivative is $2 x^{\prime} A$.

Now suppose that $z=f(y)$ and that $y=g(x)$, so that $z=f(g(x))$. Then,

$$
\frac{\partial z}{\partial x^{\prime}}=\frac{\partial z}{\partial y^{\prime}} \frac{\partial y}{\partial x^{\prime}}
$$

This is the chain rule for vector functions. The corresponding result for differentials is the following.

Theorem 18.2 (chain rule for first differentials): Let $z=f(y)$ and $y=g(x)$, so that $z=f(g(x))$. Then,

$$
\mathrm{d} z=A(y) B(x) \mathrm{d} x
$$

where $A(y)$ and $B(x)$ are defined through

$$
\mathrm{d} z=A(y) \mathrm{d} y, \quad \mathrm{~d} y=B(x) \mathrm{d} x .
$$

Example 18.3: Let $x=\left(x_{1}, x_{2}, x_{3}\right)^{\prime}$ and

$$
f(x)=\binom{x_{1}^{2}-x_{2}^{2}}{x_{1} x_{2} x_{3}}
$$

Then, the differential is

$$
\begin{aligned}
\mathrm{d} f & =\binom{\mathrm{d}\left(x_{1}^{2}\right)-\mathrm{d}\left(x_{2}^{2}\right)}{\mathrm{d}\left(x_{1} x_{2} x_{3}\right)}=\binom{2 x_{1} \mathrm{~d} x_{1}-2 x_{2} \mathrm{~d} x_{2}}{\left(\mathrm{~d} x_{1}\right) x_{2} x_{3}+x_{1}\left(\mathrm{~d} x_{2}\right) x_{3}+x_{1} x_{2} \mathrm{~d} x_{3}} \\
& =\left(\begin{array}{ccc}
2 x_{1} & -2 x_{2} & 0 \\
x_{2} x_{3} & x_{1} x_{3} & x_{1} x_{2}
\end{array}\right)\left(\begin{array}{l}
\mathrm{d} x_{1} \\
\mathrm{~d} x_{2} \\
\mathrm{~d} x_{3}
\end{array}\right)
\end{aligned}
$$

which identifies the derivative as

$$
\frac{\partial f(x)}{\partial x^{\prime}}=\left(\begin{array}{ccc}
2 x_{1} & -2 x_{2} & 0 \\
x_{2} x_{3} & x_{1} x_{3} & x_{1} x_{2}
\end{array}\right)
$$

Example 18.4a: Let $x=\left(x_{1}, x_{2}\right)^{\prime}, y=\left(y_{1}, y_{2}\right)^{\prime}$, and

$$
\phi(y)=e^{y_{1}} \sin y_{2}, \quad y_{1}=x_{1} x_{2}^{2}, \quad y_{2}=x_{1}^{2} x_{2}
$$

Then,

$$
\mathrm{d} \phi=\left(\mathrm{d} e^{y_{1}}\right) \sin y_{2}+e^{y_{1}} \mathrm{~d} \sin y_{2}=a(y)^{\prime} \mathrm{d} y
$$

where

$$
a(y)=e^{y_{1}}\binom{\sin y_{2}}{\cos y_{2}}, \quad \mathbf{d} y=\binom{\mathbf{d} y_{1}}{\mathbf{d} y_{2}} .
$$

Also,

$$
\mathrm{d} y=\left(\begin{array}{cc}
x_{2}^{2} & 2 x_{1} x_{2} \\
2 x_{1} x_{2} & x_{1}^{2}
\end{array}\right)\binom{\mathrm{d} x_{1}}{\mathrm{~d} x_{2}}=B(x) \mathrm{d} x .
$$

Hence,

$$
\mathrm{d} \phi=a(y)^{\prime} \mathrm{d} y=a(y)^{\prime} B(x) \mathrm{d} x=c_{1} \mathrm{~d} x_{1}+c_{2} \mathrm{~d} x_{2}
$$

where

$$
\begin{aligned}
& c_{1}=x_{2} e^{y_{1}}\left(x_{2} \sin y_{2}+2 x_{1} \cos y_{2}\right), \\
& c_{2}=x_{1} e^{y_{1}}\left(x_{1} \cos y_{2}+2 x_{2} \sin y_{2}\right),
\end{aligned}
$$

so that the derivative is $\partial \phi(x) / \partial x^{\prime}=\left(c_{1}, c_{2}\right)$.

## 4 OPTIMIZATION

Let $\phi(x)$ be a scalar differentiable function that we wish to optimize with respect to an $n \times 1$ vector $x$. Then we obtain the differential $\mathrm{d} \phi=a(x)^{\prime} \mathrm{d} x$, and set $a(x)=0$. Suppose, for example, that we wish to minimize the function

$$
\phi(x)=\frac{1}{2} x^{\prime} A x-b^{\prime} x
$$

where the matrix $A$ is positive definite. The differential is

$$
\mathrm{d} \phi=x^{\prime} A \mathrm{~d} x-b^{\prime} \mathrm{d} x=(A x-b)^{\prime} \mathrm{d} x
$$

(Recall that a positive definite matrix is symmetric, by definition.) The solution $\hat{x}$ needs to satisfy $A \hat{x}-b=0$, and hence $\hat{x}=A^{-1} b$. The function $\phi$ has an absolute minimum at $\hat{x}$, which can be seen by defining $y=x-\hat{x}$ and writing

$$
y^{\prime} A y=\left(x-A^{-1} b\right)^{\prime} A\left(x-A^{-1} b\right)=2 \phi(x)+b^{\prime} A^{-1} b
$$

Since $A$ is positive definite, $y^{\prime} A y$ has a minimum at $y=0$ and hence $\phi(x)$ has a minimum at $x=\hat{x}$. This holds for the specific linear-quadratic function (7) and it holds more generally for any (strictly) convex function. Such functions attain a (strict) absolute minimum.

Next suppose there is a restriction, say $g(x)=0$. Then we need to optimize subject to the restriction, and we need Lagrangian theory. This works as follows. First define the Lagrangian function, usually referred to as the Lagrangian,

$$
\psi(x)=\phi(x)-\lambda g(x)
$$

where $\lambda$ is the Lagrange multiplier. Then we obtain the differential of $\psi$ with respect to $x$,

$$
\mathrm{d} \psi=\mathrm{d} \phi-\lambda \mathrm{d} g
$$

and set it equal to zero. The equations

$$
\frac{\partial \phi(x)}{\partial x^{\prime}}=\lambda \frac{\partial g(x)}{\partial x^{\prime}}, \quad g(x)=0
$$

are the first-order conditions. From these $n+1$ equations in $n+1$ unknowns ( $x$ and $\lambda$ ), we solve $x$ and $\lambda$.

If the constraint $g$ is a vector rather than a scalar, then we have not one but several (say, $m$ ) constraints. In that case we need $m$ multipliers and it works like this. First, define the Lagrangian

$$
\psi(x)=\phi(x)-l^{\prime} g(x),
$$

where $l=\left(\lambda_{1}, \lambda_{2}, \ldots, \lambda_{m}\right)^{\prime}$ is a vector of Lagrange multipliers. Then, we obtain the differential of $\psi$ with respect to $x$ :

$$
\mathrm{d} \psi=\mathrm{d} \phi-l^{\prime} \mathrm{d} g
$$

and set it equal to zero. The equations

$$
\frac{\partial \phi(x)}{\partial x^{\prime}}=l^{\prime} \frac{\partial g(x)}{\partial x^{\prime}}, \quad g(x)=0
$$

constitute $n+m$ equations (the first-order conditions). If we can solve these equations, then we obtain the solutions, say $\hat{x}$ and $\hat{l}$.

The Lagrangian method gives necessary conditions for a local constrained extremum to occur at a given point $\hat{x}$. But how do we know that this point is in fact a maximum or a minimum? Sufficient conditions are available but they may be difficult to verify. However, in the special case where $\phi$ is linearquadratic (or more generally, convex) and $g$ is linear, $\phi$ attains an absolute minimum at the solution $\hat{x}$ under the constraint $g(x)=0$.

## 5 LEAST SQUARES

Suppose we are given an $n \times 1$ vector $y$ and an $n \times k$ matrix $X$ with linearly independent columns, so that $r(X)=k$. We wish to find a $k \times 1$ vector $\beta$, such that $X \beta$ is 'as close as possible' to $y$ in the sense that the 'error' vector $e=y-X \beta$ is minimized. A convenient scalar measure of the 'error' would be $e^{\prime} e$ and our objective is to minimize

$$
\phi(\beta)=\frac{e^{\prime} e}{2}=\frac{(y-X \beta)^{\prime}(y-X \beta)}{2}
$$

where we note that we write $e^{\prime} e / 2$ rather than $e^{\prime} e$. This makes no difference, since any $\beta$ which minimizes $e^{\prime} e$ will also minimize $e^{\prime} e / 2$, but it is a common trick, useful because we know that we are minimizing a quadratic function, so that a ' 2 ' will appear in the derivative. The $1 / 2$ neutralizes this 2 .

Differentiating $\phi$ in (8) gives

$$
\mathrm{d} \phi=e^{\prime} \mathrm{d} e=e^{\prime} \mathrm{d}(y-X \beta)=-e^{\prime} X \mathrm{~d} \beta
$$

Hence, the optimum is obtained when $X^{\prime} e=0$, that is, when $X^{\prime} X \hat{\beta}=X^{\prime} y$, from which we obtain

$$
\hat{\beta}=\left(X^{\prime} X\right)^{-1} X^{\prime} y
$$

the least-squares solution.
If there are constraints on $\beta$, say $R \beta=r$, then we need to solve

$$
\begin{array}{ll}
\text { minimize } & \phi(\beta) \\
\text { subject to } & R \beta=r
\end{array}
$$

We assume that the $m$ rows of $R$ are linearly independent, and define the Lagrangian

$$
\psi(\beta)=(y-X \beta)^{\prime}(y-X \beta) / 2-l^{\prime}(R \beta-r)
$$

where $l$ is a vector of Lagrange multipliers. The differential is

$$
\begin{aligned}
\mathrm{d} \psi & =\mathrm{d}(y-X \beta)^{\prime}(y-X \beta) / 2-l^{\prime} \mathrm{d}(R \beta-r) \\
& =(y-X \beta)^{\prime} \mathrm{d}(y-X \beta)-l^{\prime} R \mathrm{~d} \beta \\
& =-(y-X \beta)^{\prime} X \mathrm{~d} \beta-l^{\prime} R \mathrm{~d} \beta
\end{aligned}
$$

Setting the differential equal to zero and denoting the restricted estimators by $\tilde{\beta}$ and $\tilde{l}$, we obtain the first-order conditions

$$
(y-X \tilde{\beta})^{\prime} X+\tilde{l}^{\prime} R=0, \quad R \tilde{\beta}=r
$$

or, written differently,

$$
X^{\prime} X \tilde{\beta}-X^{\prime} y=R^{\prime} \tilde{l}, \quad R \tilde{\beta}=r
$$

We do not know $\tilde{\beta}$ but we know $R \tilde{\beta}$. Hence, we premultiply by $R\left(X^{\prime} X\right)^{-1}$. Letting $\hat{\beta}=\left(X^{\prime} X\right)^{-1} X^{\prime} y$ as in (9), this gives

$$
r-R \hat{\beta}=R\left(X^{\prime} X\right)^{-1} R^{\prime} \tilde{l}
$$

Since $R$ has full row rank, we can solve for $l$ :

$$
\tilde{l}=\left(R\left(X^{\prime} X\right)^{-1} R^{\prime}\right)^{-1}(r-R \hat{\beta}),
$$

and hence for $\beta$ :

$$
\tilde{\beta}=\hat{\beta}+\left(X^{\prime} X\right)^{-1} R^{\prime} \tilde{l}=\hat{\beta}+\left(X^{\prime} X\right)^{-1} R^{\prime}\left(R\left(X^{\prime} X\right)^{-1} R^{\prime}\right)^{-1}(r-R \hat{\beta})
$$

Since the constraint is linear and the function $\phi$ is linear-quadratic as in (7), it follows that the solution $\tilde{\beta}$ indeed minimizes $\phi(\beta)=e^{\prime} e / 2$ under the constraint $R \beta=r$.

## 6 MATRIX CALCULUS

We have moved from scalar calculus to vector calculus, now we move from vector calculus to matrix calculus. When discussing matrices we assume that the reader is familiar with matrix addition and multiplication, and also knows the concepts of a determinant $|A|$ and an inverse $A^{-1}$. An important function of a square matrix $A=\left(a_{i j}\right)$ is its trace, which is defined as the sum of the diagonal elements of $A$ : $\operatorname{tr} A=\sum_{i} a_{i i}$. We have

$$
\operatorname{tr} A=\operatorname{tr} A^{\prime}
$$

which is obvious because a matrix and its transpose have the same diagonal elements. Less obvious is

$$
\operatorname{tr} A^{\prime} B=\operatorname{tr} B A^{\prime}
$$

for any two matrices $A$ and $B$ of the same order (but not necessarily square). This follows because

$$
\begin{aligned}
\operatorname{tr} A^{\prime} B & =\sum_{j}\left(A^{\prime} B\right)_{j j}=\sum_{j} \sum_{i} a_{i j} b_{i j} \\
& =\sum_{i} \sum_{j} b_{i j} a_{i j}=\sum_{i}\left(B A^{\prime}\right)_{i i}=\operatorname{tr} B A^{\prime}
\end{aligned}
$$

The rules for vector differentials in Section 3 carry over to matrix differentials. Let $A$ be a matrix of constants and let $\alpha$ be a scalar. Then, for any $X$,

$$
\mathrm{d} A=0, \quad \mathrm{~d}(\alpha X)=\alpha \mathrm{d} X, \quad \mathrm{~d}\left(X^{\prime}\right)=(\mathrm{d} X)^{\prime},
$$

and, for square $X$,

$$
\mathrm{d} \operatorname{tr} X=\operatorname{tr} \mathrm{d} X
$$

If $X$ and $Y$ are of the same order, then

$$
\mathrm{d}(X+Y)=\mathrm{d} X+\mathrm{d} Y, \quad \mathrm{~d}(X-Y)=\mathrm{d} X-\mathrm{d} Y,
$$

and, if the matrix product $X Y$ is defined,

$$
\mathrm{d}(X Y)=(\mathrm{d} X) Y+X \mathrm{~d} Y
$$

Two less trivial differentials are the determinant and the inverse. For nonsingular $X$ we have

$$
\mathrm{d}|X|=|X| \operatorname{tr} X^{-1} \mathrm{~d} X
$$

and in particular, when $|X|>0$,

$$
\mathrm{d} \log |X|=\frac{\mathrm{d}|X|}{|X|}=\operatorname{tr} X^{-1} \mathrm{~d} X
$$

The proof of (11) is a little tricky and is omitted (in this chapter, but not in Chapter 8).

The differential of the inverse is, for nonsingular $X$,

$$
\mathrm{d} X^{-1}=-X^{-1}(\mathrm{~d} X) X^{-1}
$$

This we can prove easily by considering the equation $X^{-1} X=I$. Differentiating both sides gives

$$
\left(\mathrm{d} X^{-1}\right) X+X^{-1} \mathrm{~d} X=0
$$

and the result then follows by postmultiplying with $X^{-1}$.
The chain rule also applies to matrix functions. More precisely, if $Z= F(Y)$ and $Y=G(X)$, so that $Z=F(G(X))$, then

$$
\mathrm{d} Z=A(Y) B(X) \mathrm{d} X
$$

where $A(Y)$ and $B(X)$ are defined through

$$
\mathrm{d} Z=A(Y) \mathrm{d} Y, \quad \mathrm{~d} Y=B(X) \mathrm{d} X
$$

as in Theorem 18.2.
Regarding constrained optimization, treated for vector functions in Section 18.4, we note that this can be easily and elegantly extended to matrix constraints. If we have a matrix $G$ (rather than a vector $g$ ) of constraints and a matrix $X$ (rather than a vector $x$ ) of variables, then we define a matrix of multipliers $L=\left(\lambda_{i j}\right)$ of the same dimension as $G=\left(g_{i j}\right)$. The Lagrangian then becomes

$$
\psi(X)=\phi(X)-\operatorname{tr} L^{\prime} G(X)
$$

where we have used the fact, also used in (10) above, that

$$
\operatorname{tr} L^{\prime} G=\sum_{i} \sum_{j} \lambda_{i j} g_{i j}
$$

## 7 INTERLUDE ON LINEAR AND QUADRATIC FORMS

Before we turn from first to second differentials, that is, from linear forms to quadratic forms, we investigate under what conditions a linear or quadratic form vanishes. The sole purpose of this section is to help the reader appreciate Theorem 18.3 in the next section.

A linear form is an expression such as $A x$. When $A x=0$, this does not imply that either $A$ or $x$ is zero. For example, if

$$
A=\left(\begin{array}{rr}
1 & -1 \\
-2 & 2 \\
3 & -3
\end{array}\right), \quad x=\binom{1}{1}
$$

then $A x=0$, but neither $A=0$ nor $x=0$.
However, when $A x=0$ for every $x$, then $A$ must be zero, which can be seen by taking $x$ to be each elementary vector $e_{i}$ in turn. (The $i$ th elementary vector is the vector with one in the $i$ th position and zeros elsewhere.)

A quadratic form is an expression such as $x^{\prime} A x$. When $x^{\prime} A x=0$, this does not imply that $A=0$ or $x=0$ or $A x=0$. Even when $x^{\prime} A x=0$ for every $x$, it does not follow that $A=0$, as the example

$$
A=\left(\begin{array}{rr}
0 & 1 \\
-1 & 0
\end{array}\right)
$$

demonstrates. This matrix $A$ is skew-symmetric, that is, it satisfies $A^{\prime}=-A$. In fact, when $x^{\prime} A x=0$ for every $x$ then it follows that $A$ must be skewsymmetric. This can be seen by taking $x=e_{i}$ which implies that $a_{i i}=0$, and then $x=e_{i}+e_{j}$ which implies that $a_{i j}+a_{j i}=0$.

In the special case where $x^{\prime} A x=0$ for every $x$ and $A$ is symmetric, then $A$ is both symmetric ( $A^{\prime}=A$ ) and skew-symmetric ( $A^{\prime}=-A$ ), and hence $A=0$.

## 8 THE SECOND DIFFERENTIAL

The second differential is simply the differential of the first differential:

$$
\mathrm{d}^{2} f=\mathrm{d}(\mathrm{~d} f)
$$

Higher-order differentials are similarly defined, but they are seldom needed.
Example 18.2b: Let $\phi(x)=x^{\prime} A x$. Then, $\mathrm{d} \phi=x^{\prime}\left(A+A^{\prime}\right) \mathrm{d} x$ and

$$
\begin{aligned}
\mathrm{d}^{2} \phi & =\mathrm{d}\left(x^{\prime}\left(A+A^{\prime}\right) \mathrm{d} x\right)=(\mathrm{d} x)^{\prime}\left(A+A^{\prime}\right) \mathrm{d} x+x^{\prime}\left(A+A^{\prime}\right) \mathrm{d}^{2} x \\
& =(\mathrm{d} x)^{\prime}\left(A+A^{\prime}\right) \mathrm{d} x
\end{aligned}
$$

since $\mathrm{d}^{2} x=0$.

The first differential leads to the first derivative (sometimes called the Jacobian matrix) and the second differential leads to the second derivative (called the Hessian matrix). We emphasize that the concept of Hessian matrix is only useful for scalar functions, not for vector or matrix functions. When we have a vector function $f$ we shall consider the Hessian matrix of each element of $f$ separately, and when we have a matrix function $F$ we shall consider the Hessian matrix of each element of $F$ separately.

Thus, let $\phi$ be a scalar function and let

$$
\mathrm{d} \phi=a(x)^{\prime} \mathrm{d} x, \quad \mathrm{~d} a=(\mathrm{H} \phi) \mathrm{d} x,
$$

where

$$
a(x)^{\prime}=\frac{\partial \phi(x)}{\partial x^{\prime}}, \quad \mathrm{H} \phi=\frac{\partial a(x)}{\partial x^{\prime}}=\frac{\partial}{\partial x^{\prime}}\left(\frac{\partial \phi(x)}{\partial x^{\prime}}\right)^{\prime} .
$$

The $i j$ th element of the Hessian matrix $\mathrm{H} \phi$ is thus obtained by first calculating $a_{j}(x)=\partial \phi(x) / \partial x_{j}$ and then $(\mathrm{H} \phi)_{i j}=\partial a_{j}(x) / \partial x_{i}$. The Hessian matrix contains all second-order partial derivatives $\partial^{2} \phi(x) / \partial x_{i} \partial x_{j}$, and it is symmetric if $\phi$ is twice differentiable.

The Hessian matrix is often written as

$$
\mathrm{H} \phi=\frac{\partial^{2} \phi(x)}{\partial x \partial x^{\prime}}
$$

where the expression on the right-hand side is a notation, the precise meaning of which is given by

$$
\frac{\partial^{2} \phi(x)}{\partial x \partial x^{\prime}}=\frac{\partial}{\partial x^{\prime}}\left(\frac{\partial \phi(x)}{\partial x^{\prime}}\right)^{\prime}
$$

Given (13) and using the symmetry of $\mathrm{H} \phi$, we obtain the second differential as

$$
\mathrm{d}^{2} \phi=(\mathrm{d} a)^{\prime} \mathrm{d} x=(\mathrm{d} x)^{\prime}(\mathrm{H} \phi) \mathrm{d} x
$$

which shows that the second differential of $\phi$ is a quadratic form in $\mathrm{d} x$.
Now, suppose that we have obtained, after some calculations, that $\mathrm{d}^{2} \phi= (\mathrm{d} x)^{\prime} B(x) \mathrm{d} x$. Then,

$$
(\mathrm{d} x)^{\prime}(\mathrm{H} \phi-B(x)) \mathrm{d} x=0
$$

for all $\mathrm{d} x$. Does this imply that $\mathrm{H} \phi=B(x)$ ? No, it does not, as we have seen in the previous section. It does, however, imply that

$$
(\mathrm{H} \phi-B(x))^{\prime}+(\mathrm{H} \phi-B(x))=0
$$

and hence that $\mathrm{H} \phi=\left(B(x)+B(x)^{\prime}\right) / 2$, using the symmetry of $\mathrm{H} \phi$. This proves the following result.

## Theorem 18.3 (second identification theorem):

$$
\mathrm{d}^{2} \phi=(\mathrm{d} x)^{\prime} B(x) \mathrm{d} x \Longleftrightarrow \mathrm{H} \phi=\frac{B(x)+B(x)^{\prime}}{2} .
$$

The second identification theorem shows that there is a one-to-one correspondence between second-order differentials and second-order derivatives, but only if we make the matrix $B(x)$ in the quadratic form symmetric. Hence, the second differential identifies the second derivative.

Example 18.2c: Consider again the quadratic function $\phi(x)=x^{\prime} A x$. Then we can start with $\mathrm{d} \phi=x^{\prime}\left(A+A^{\prime}\right) \mathrm{d} x$, as in Example 18.2b, and obtain $\mathrm{d}^{2} \phi=(\mathrm{d} x)^{\prime}\left(A+A^{\prime}\right) \mathrm{d} x$. The matrix in the quadratic form is already symmetric, so we obtain directly $\mathrm{H} \phi=A+A^{\prime}$.

Alternatively - and this is often quicker - we differentiate $\phi$ twice without writing out the first differential in its final form. From

$$
\mathrm{d} \phi=(\mathrm{d} x)^{\prime} A x+x^{\prime} A \mathrm{~d} x
$$

we thus obtain

$$
\mathrm{d}^{2} \phi=2(\mathrm{~d} x)^{\prime} A \mathrm{~d} x
$$

which identifies the Hessian matrix as $\mathrm{H} \phi=A+A^{\prime}$. (Notice that the matrix $A$ in (16) is not necessarily symmetric.)

Even with such a simple function as $\phi(x)=x^{\prime} A x$, the advantage and elegance of using differentials is clear. Without differentials we would need to prove first that $\partial a^{\prime} x / \partial x^{\prime}=a^{\prime}$ and $\partial x^{\prime} A x / \partial x^{\prime}=x^{\prime}\left(A+A^{\prime}\right)$, and then use (15) to obtain

$$
\frac{\partial^{2} x^{\prime} A x}{\partial x \partial x^{\prime}}=\frac{\partial\left(x^{\prime}\left(A+A^{\prime}\right)\right)^{\prime}}{\partial x^{\prime}}=\frac{\partial\left(A+A^{\prime}\right) x}{\partial x^{\prime}}=A+A^{\prime},
$$

which is cumbersome in this simple case and not practical in more complex situations.

## 9 CHAIN RULE FOR SECOND DIFFERENTIALS

Let us now return to Example 18.2b. The function $\phi$ in this example is a function of $x$, and $x$ is the argument of interest. This is why $\mathrm{d}^{2} x=0$. But if $\phi$ is a function of $x$, which in turn is a function of $t$, then it is no longer true that $\mathrm{d}^{2} x$ equals zero. More generally, suppose that $z=f(y)$ and that $y=g(x)$, so that $z=f(g(x))$. Then,

$$
\mathrm{d} z=A(y) \mathrm{d} y
$$

and

$$
\mathrm{d}^{2} z=(\mathrm{d} A) \mathrm{d} y+A(y) \mathrm{d}^{2} y
$$

This is true whether or not $y$ depends on some other variables. If we think of $z$ as a function of $y$, then $\mathrm{d}^{2} y=0$, but if $y$ depends on $x$ then $\mathrm{d}^{2} y$ is not zero; in fact,

$$
\mathrm{d} y=B(x) \mathrm{d} x, \quad \mathrm{~d}^{2} y=(\mathrm{d} B) \mathrm{d} x
$$

This gives us the following result.
Theorem 18.4 (chain rule for second differentials): Let $z=f(y)$ and $y=g(x)$, so that $z=f(g(x))$. Then,

$$
\mathrm{d}^{2} z=(\mathrm{d} A) B(x) \mathrm{d} x+A(y)(\mathrm{d} B) \mathrm{d} x,
$$

where $A(y)$ and $B(x)$ are defined through

$$
\mathrm{d} z=A(y) \mathrm{d} y, \quad \mathrm{~d} y=B(x) \mathrm{d} x .
$$

In practice, one usually avoids Theorem 18.4 by going back to the first differential $\mathrm{d} z=A(y) \mathrm{d} y$ and differentiating again. This gives (17), from which we obtain the result step by step.

Example 18.4b: Let

$$
\phi\left(y_{1}, y_{2}\right)=e^{y_{1}} \sin y_{2}, \quad y_{1}=x_{1} x_{2}^{2}, \quad y_{2}=x_{1}^{2} x_{2}
$$

Then, by Theorem 18.4,

$$
\mathrm{d}^{2} \phi=(\mathrm{d} a)^{\prime} B(x) \mathrm{d} x+a(y)^{\prime}(\mathrm{d} B) \mathrm{d} x
$$

where

$$
a(y)=e^{y_{1}}\binom{\sin y_{2}}{\cos y_{2}}, \quad B(x)=\left(\begin{array}{cc}
x_{2}^{2} & 2 x_{1} x_{2} \\
2 x_{1} x_{2} & x_{1}^{2}
\end{array}\right) .
$$

Now, letting

$$
C(y)=e^{y_{1}}\left(\begin{array}{rr}
\sin y_{2} & \cos y_{2} \\
\cos y_{2} & -\sin y_{2}
\end{array}\right)
$$

and

$$
D_{1}(x)=2\left(\begin{array}{cc}
0 & x_{2} \\
x_{2} & x_{1}
\end{array}\right), \quad D_{2}(x)=2\left(\begin{array}{cc}
x_{2} & x_{1} \\
x_{1} & 0
\end{array}\right)
$$

we obtain

$$
\mathrm{d} a=C(y) \mathrm{d} y=C(y) B(x) \mathrm{d} x
$$

and

$$
\mathrm{d} B=\left(\mathrm{d} x_{1}\right) D_{1}(x)+\left(\mathrm{d} x_{2}\right) D_{2}(x) .
$$

It is convenient to write $\mathrm{d} x_{1}$ and $\mathrm{d} x_{2}$ in terms of $\mathrm{d} x$, which can be done by defining $e_{1}=(1,0)^{\prime}$ and $e_{2}=(0,1)^{\prime}$. Then, $\mathrm{d} x_{1}=e_{1}^{\prime} \mathrm{d} x$ and $\mathrm{d} x_{2}=e_{2}^{\prime} \mathrm{d} x$, and hence

$$
\begin{aligned}
\mathrm{d}^{2} \phi & =(\mathrm{d} a)^{\prime} B(x) \mathrm{d} x+a(y)^{\prime}(\mathrm{d} B) \mathrm{d} x \\
& =(\mathrm{d} x)^{\prime} B(x) C(y) B(x) \mathrm{d} x+a(y)^{\prime}\left(\left(\mathrm{d} x_{1}\right) D_{1}(x)+\left(\mathrm{d} x_{2}\right) D_{2}(x)\right) \mathrm{d} x \\
& =(\mathrm{d} x)^{\prime} B(x) C(y) B(x) \mathrm{d} x+(\mathrm{d} x)^{\prime} e_{1} a(y)^{\prime} D_{1}(x) \mathrm{d} x+(\mathrm{d} x)^{\prime} e_{2} a(y)^{\prime} D_{2}(x) \mathrm{d} x \\
& =(\mathrm{d} x)^{\prime}\left[B(x) C(y) B(x)+e_{1} a(y)^{\prime} D_{1}(x)+e_{2} a(y)^{\prime} D_{2}(x)\right] \mathrm{d} x
\end{aligned}
$$

Some care is required where to position the scalars $e_{1}^{\prime} \mathrm{d} x$ and $e_{2}^{\prime} \mathrm{d} x$ in the matrix product. A scalar can be positioned anywhere in a matrix product, but we wish to position the two scalars in such a way that the usual matrix multiplication rules still apply.

Having obtained the second differential in the desired form, Theorem 18.3 implies that the Hessian is equal to

$$
\begin{aligned}
\mathrm{H} \phi= & B(x) C(y) B(x)+\frac{1}{2}\left(e_{1} a(y)^{\prime} D_{1}(x)+D_{1}(x) a(y) e_{1}^{\prime}\right) \\
& +\frac{1}{2}\left(e_{2} a(y)^{\prime} D_{2}(x)+D_{2}(x) a(y) e_{2}^{\prime}\right)
\end{aligned}
$$

## 10 FOUR EXAMPLES

Let us provide four examples to show how the second differential can be obtained. The first three examples relate to scalar functions and the fourth example to a matrix function. The matrix $X$ has order $n \times q$ in Examples 18.5a and 18.6a, and order $n \times n$ in Examples 18.7a and 18.8a.

Example 18.5a: Let $\phi(X)=\operatorname{tr} X^{\prime} A X$. Then,

$$
\begin{aligned}
\mathrm{d} \phi & =\mathrm{d}\left(\operatorname{tr} X^{\prime} A X\right)=\operatorname{tr} \mathrm{d}\left(X^{\prime} A X\right) \\
& =\operatorname{tr}(\mathrm{d} X)^{\prime} A X+\operatorname{tr} X^{\prime} A \mathrm{~d} X=\operatorname{tr} X^{\prime}\left(A+A^{\prime}\right) \mathrm{d} X
\end{aligned}
$$

and

$$
\mathrm{d}^{2} \phi=\mathrm{d} \operatorname{tr} X^{\prime}\left(A+A^{\prime}\right) \mathrm{d} X=\operatorname{tr}(\mathrm{d} X)^{\prime}\left(A+A^{\prime}\right) \mathrm{d} X
$$

Example 18.6a: Let $\phi(X)=\log \left|X^{\prime} X\right|$. Then,

$$
\begin{aligned}
\mathrm{d} \phi & =\mathrm{d} \log \left|X^{\prime} X\right|=\operatorname{tr}\left(X^{\prime} X\right)^{-1} \mathrm{~d}\left(X^{\prime} X\right) \\
& =\operatorname{tr}\left(X^{\prime} X\right)^{-1}(\mathrm{~d} X)^{\prime} X+\operatorname{tr}\left(X^{\prime} X\right)^{-1} X^{\prime} \mathrm{d} X=2 \operatorname{tr}\left(X^{\prime} X\right)^{-1} X^{\prime} \mathrm{d} X
\end{aligned}
$$

and

$$
\begin{aligned}
\mathrm{d}^{2} \phi= & 2 \mathrm{~d}\left(\operatorname{tr}\left(X^{\prime} X\right)^{-1} X^{\prime} \mathrm{d} X\right) \\
= & 2 \operatorname{tr}\left(\mathrm{~d}\left(X^{\prime} X\right)^{-1}\right) X^{\prime} \mathrm{d} X+2 \operatorname{tr}\left(X^{\prime} X\right)^{-1}(\mathrm{~d} X)^{\prime} \mathrm{d} X \\
= & -2 \operatorname{tr}\left(X^{\prime} X\right)^{-1}\left(\mathrm{~d} X^{\prime} X\right)\left(X^{\prime} X\right)^{-1} X^{\prime} \mathrm{d} X+2 \operatorname{tr}\left(X^{\prime} X\right)^{-1}(\mathrm{~d} X)^{\prime} \mathrm{d} X \\
= & -2 \operatorname{tr}\left(X^{\prime} X\right)^{-1}(\mathrm{~d} X)^{\prime} X\left(X^{\prime} X\right)^{-1} X^{\prime} \mathrm{d} X \\
& -2 \operatorname{tr}\left(X^{\prime} X\right)^{-1} X^{\prime}(\mathrm{d} X)\left(X^{\prime} X\right)^{-1} X^{\prime} \mathrm{d} X+2 \operatorname{tr}\left(X^{\prime} X\right)^{-1}(\mathrm{~d} X)^{\prime} \mathrm{d} X \\
= & 2 \operatorname{tr}\left(X^{\prime} X\right)^{-1}(\mathrm{~d} X)^{\prime} M \mathrm{~d} X-2 \operatorname{tr}\left(X^{\prime} X\right)^{-1} X^{\prime}(\mathrm{d} X)\left(X^{\prime} X\right)^{-1} X^{\prime} \mathrm{d} X
\end{aligned}
$$

where $M=I_{n}-X\left(X^{\prime} X\right)^{-1} X^{\prime}$. Let us explain some of the steps in more detail. The second equality follows from considering $\left(X^{\prime} X\right)^{-1} X^{\prime} \mathrm{d} X$ as a product
of three matrices: $\left(X^{\prime} X\right)^{-1}, X^{\prime}$, and $\mathrm{d} X$ (a matrix of constants), the third equality uses the differential of the inverse in (12), and the fourth equality separates $\mathrm{d} X^{\prime} X$ into $(\mathrm{d} X)^{\prime} X+X^{\prime} \mathrm{d} X$.

Example 18.7a: Let $\phi(X)=\operatorname{tr} X^{k}$ for $k=1,2, \ldots$ Then, for $k \geq 1$,

$$
\begin{aligned}
\mathrm{d} \phi & =\operatorname{tr}(\mathrm{d} X) X^{k-1}+\operatorname{tr} X(\mathrm{~d} X) X^{k-2}+\cdots+\operatorname{tr} X^{k-1} \mathrm{~d} X \\
& =k \operatorname{tr} X^{k-1} \mathrm{~d} X
\end{aligned}
$$

and for $k \geq 2$,

$$
\mathrm{d}^{2} \phi=k \operatorname{tr}\left(\mathrm{~d} X^{k-1}\right) \mathrm{d} X=k \sum_{j=0}^{k-2} \operatorname{tr} X^{j}(\mathrm{~d} X) X^{k-2-j} \mathrm{~d} X
$$

Example 18.8a: Let $F(X)=A X^{-1} B$. Then,

$$
\mathrm{d} F=A\left(\mathrm{~d} X^{-1}\right) B=-A X^{-1}(\mathrm{~d} X) X^{-1} B
$$

and

$$
\begin{aligned}
\mathrm{d}^{2} F & =-A\left(\mathrm{~d} X^{-1}\right)(\mathrm{d} X) X^{-1} B-A X^{-1}(\mathrm{~d} X)\left(\mathrm{d} X^{-1}\right) B \\
& =2 A X^{-1}(\mathrm{~d} X) X^{-1}(\mathrm{~d} X) X^{-1} B
\end{aligned}
$$

These four examples provide the second differential; they do not yet provide the Hessian matrix. In Section 18.14, we shall discuss the same four examples and obtain the Hessian matrices.

## 11 THE KRONECKER PRODUCT AND VEC OPERATOR

The theory and the four examples in the previous two sections demonstrate the elegance and simplicity of obtaining first and second differentials of scalar, vector, and matrix functions. But we also want to relate these first and second differentials to Jacobian matrices (first derivatives) and Hessian matrices (second derivatives). For this we need some more machinery, namely the vec operator and the Kronecker product.

First, the vec operator. Consider an $m \times n$ matrix $A$. This matrix has $n$ columns, say $a_{1}, \ldots, a_{n}$. Now define the $m n \times 1$ vector vec $A$ as the vector which stacks these columns one underneath the other:

$$
\operatorname{vec} A=\left(\begin{array}{c}
a_{1} \\
a_{2} \\
\vdots \\
a_{n}
\end{array}\right)
$$

For example, if

$$
A=\left(\begin{array}{lll}
1 & 2 & 3 \\
4 & 5 & 6
\end{array}\right)
$$

then $\operatorname{vec} A=(1,4,2,5,3,6)^{\prime}$. Of course, we have

$$
\mathrm{d} \operatorname{vec} X=\operatorname{vec} \mathrm{d} X
$$

If $A$ and $B$ are matrices of the same order, then we know from (10) that $\operatorname{tr} A^{\prime} B=\sum_{i j} a_{i j} b_{i j}$. But ( $\left.\operatorname{vec} A\right)^{\prime}(\operatorname{vec} B)$ is also equal to this double sum. Hence,

$$
\operatorname{tr} A^{\prime} B=(\operatorname{vec} A)^{\prime}(\operatorname{vec} B)
$$

an important equality linking the vec operator to the trace.
We also need the Kronecker product. Let $A$ be an $m \times n$ matrix and $B$ a $p \times q$ matrix. The $m p \times n q$ matrix defined by

$$
\left(\begin{array}{ccc}
a_{11} B & \ldots & a_{1 n} B \\
\vdots & & \vdots \\
a_{m 1} B & \ldots & a_{m n} B
\end{array}\right)
$$

is called the Kronecker product of $A$ and $B$ and is written as $A \otimes B$. The Kronecker product $A \otimes B$ is thus defined for any pair of matrices $A$ and $B$, unlike the matrix product $A B$ which exists only if the number of columns in $A$ equals the number of rows in $B$ or if either $A$ or $B$ is a scalar.

The following three properties justify the name Kronecker product:

$$
\begin{aligned}
A \otimes B \otimes C & =(A \otimes B) \otimes C=A \otimes(B \otimes C), \\
(A+B) \otimes(C+D) & =A \otimes C+A \otimes D+B \otimes C+B \otimes D,
\end{aligned}
$$

if $A$ and $B$ have the same order and $C$ and $D$ have the same order (not necessarily equal to the order of $A$ and $B$ ), and

$$
(A \otimes B)(C \otimes D)=A C \otimes B D
$$

if $A C$ and $B D$ exist.
The transpose of a Kronecker product is

$$
(A \otimes B)^{\prime}=A^{\prime} \otimes B^{\prime}
$$

If $A$ and $B$ are square matrices (not necessarily of the same order), then

$$
\operatorname{tr}(A \otimes B)=(\operatorname{tr} A)(\operatorname{tr} B)
$$

and if $A$ and $B$ are nonsingular, then

$$
(A \otimes B)^{-1}=A^{-1} \otimes B^{-1}
$$

The Kronecker product and the vec operator are related through the equality

$$
\text { vec } a b^{\prime}=b \otimes a,
$$

where $a$ and $b$ are column vectors of arbitrary order. Using this inequality, we see that

$$
\begin{aligned}
\operatorname{vec}\left(A b e^{\prime} C\right) & =\operatorname{vec}(A b)\left(C^{\prime} e\right)^{\prime}=\left(C^{\prime} e\right) \otimes(A b) \\
& =\left(C^{\prime} \otimes A\right)(e \otimes b)=\left(C^{\prime} \otimes A\right) \text { vec } b e^{\prime}
\end{aligned}
$$

for any vectors $b$ and $e$. Then, writing $B=\sum_{j} b_{j} e_{j}^{\prime}$ where $b_{j}$ and $e_{j}$ denote the $j$ th column of $B$ and $I$, respectively, we obtain the following important relationship, which is used frequently.

Theorem 18.5: For any matrices $A, B$, and $C$ for which the product $A B C$ is defined, we have

$$
\text { vec } A B C=\left(C^{\prime} \otimes A\right) \text { vec } B \text {. }
$$

## 12 IDENTIFICATION

When we move from vector calculus to matrix calculus, we need an ordering of the functions and of the variables. It does not matter how we order them (any ordering will do), but an ordering is essential. We want to define matrix derivatives within the established theory of vector derivatives in such a way that trivial changes such as relabeling functions or variables have only trivial consequences for the derivative: rows and columns are permuted, but the rank is unchanged and the determinant (in the case of a square matrix) is also unchanged, apart possibly from its sign. This is what we need to achieve. The arrangement of the partial derivatives matters, because a derivative is more than just a collection of partial derivatives. It is a mathematical concept, a mathematical unit.

Thus motivated, we shall view the matrix function $F(X)$ as a vector function $f(x)$, where $f=\operatorname{vec} F$ and $x=\operatorname{vec} X$. We then obtain the following extension of the first identification theorem:

$$
\mathrm{d} \operatorname{vec} F=A(X) \mathrm{d} \operatorname{vec} X \Longleftrightarrow \frac{\partial \operatorname{vec} F(X)}{\partial(\operatorname{vec} X)^{\prime}}=A(X),
$$

and, similarly, for the second identification theorem:

$$
\mathrm{d}^{2} \phi=(\mathrm{d} \operatorname{vec} X)^{\prime} B(X) \mathrm{d} \operatorname{vec} X \Longleftrightarrow \mathrm{H} \phi=\frac{B(X)+B(X)^{\prime}}{2},
$$

where we notice, as in Section 18.8, that we only provide the Hessian matrix for scalar functions, not for vector or matrix functions.

## 13 THE COMMUTATION MATRIX

At this point, we need to introduce the commutation matrix. Let $A$ be an $m \times n$ matrix. The vectors vec $A$ and vec $A^{\prime}$ contain the same $m n$ elements, but in a different order. Hence, there exists a unique $m n \times m n$ matrix, which transforms vec $A$ into vec $A^{\prime}$. This matrix contains $m n$ ones and $m n(m n-1)$ zeros and is called the commutation matrix, denoted by $K_{m n}$. (If $m=n$, we write $K_{n}$ instead of $K_{n n}$.) Thus,

$$
K_{m n} \operatorname{vec} A=\operatorname{vec} A^{\prime} .
$$

It can be shown that $K_{m n}$ is orthogonal, i.e. $K_{m n}^{\prime}=K_{m n}^{-1}$. Also, premultiplying (20) by $K_{n m}$ gives $K_{n m} K_{m n} \operatorname{vec} A=\operatorname{vec} A$, which shows that $K_{n m} K_{m n}= I_{m n}$. Hence,

$$
K_{m n}^{\prime}=K_{m n}^{-1}=K_{n m}
$$

The key property of the commutation matrix enables us to interchange (commute) the two matrices of a Kronecker product:

$$
K_{p m}(A \otimes B)=(B \otimes A) K_{q n}
$$

for any $m \times n$ matrix $A$ and $p \times q$ matrix $B$. This is easiest shown, not by proving a matrix identity but by proving that the effect of the two matrices on an arbitrary vector is the same. Thus, let $X$ be an arbitrary $q \times n$ matrix. Then, by repeated application of (20) and Theorem 18.5,

$$
\begin{aligned}
K_{p m}(A \otimes B) & \text { vec } X=K_{p m} \text { vec } B X A^{\prime}=\text { vec } A X^{\prime} B^{\prime} \\
& =(B \otimes A) \text { vec } X^{\prime}=(B \otimes A) K_{q n} \text { vec } X
\end{aligned}
$$

Since $X$ is arbitrary, (21) follows.
The commutation matrix has many applications in matrix theory. Its importance in matrix calculus stems from the fact that it transforms $\mathrm{d} \operatorname{vec} X^{\prime}$ into $\mathrm{d} \operatorname{vec} X$. The simplest example is the matrix function $F(X)=X^{\prime}$, where $X$ is an $n \times q$ matrix. Then,

$$
\mathrm{d} \operatorname{vec} F=\operatorname{vec} \mathrm{d} X^{\prime}=K_{n q} \operatorname{vec} \mathrm{~d} X
$$

so that the derivative is $\mathrm{D} \operatorname{vec} F=K_{n q}$.
The commutation matrix is also essential in identifying the Hessian matrix from the second differential. The second differential of a scalar function often takes the form of a trace, either $\operatorname{tr} A(\mathrm{~d} X)^{\prime} B \mathrm{~d} X$ or $\operatorname{tr} A(\mathrm{~d} X) B \mathrm{~d} X$. We then have the following result, based on (19) and Theorem 18.5.

Theorem 18.6: Let $\phi$ be a twice differentiable real-valued function of an $n \times q$ matrix $X$. Then,

$$
\mathrm{d}^{2} \phi=\operatorname{tr} A(\mathrm{~d} X)^{\prime} B \mathrm{~d} X \Longleftrightarrow \mathrm{H} \phi=\frac{1}{2}\left(A^{\prime} \otimes B+A \otimes B^{\prime}\right)
$$

and

$$
\mathrm{d}^{2} \phi=\operatorname{tr} A(\mathrm{~d} X) B \mathrm{~d} X \Longleftrightarrow \mathrm{H} \phi=\frac{1}{2} K_{q n}\left(A^{\prime} \otimes B+B^{\prime} \otimes A\right) .
$$

To identify the Hessian matrix from the first expression, we do not need the commutation matrix, but we do need the commutation matrix to identify the Hessian matrix from the second expression.

## 14 FROM SECOND DIFFERENTIAL TO HESSIAN

We continue with the same four examples as discussed in Section 18.10, showing how to obtain the Hessian matrices from the second differentials, using Theorem 18.6.

Example 18.5b: Let $\phi(X)=\operatorname{tr} X^{\prime} A X$, where $X$ is an $n \times q$ matrix. Then,

$$
\mathrm{d} \phi=\operatorname{tr} X^{\prime}\left(A+A^{\prime}\right) \mathrm{d} X=\operatorname{tr} C^{\prime} \mathrm{d} X=(\operatorname{vec} C)^{\prime} \mathrm{d} \operatorname{vec} X
$$

where $C=\left(A+A^{\prime}\right) X$, and $\mathrm{d}^{2} \phi=\operatorname{tr}(\mathrm{d} X)^{\prime}\left(A+A^{\prime}\right) \mathrm{d} X$. Hence, the derivative is $\mathrm{D} \phi=(\operatorname{vec} C)^{\prime}$ and the Hessian is $\mathrm{H} \phi=I_{q} \otimes\left(A+A^{\prime}\right)$.

Example 18.6b: Let $\phi(X)=\log \left|X^{\prime} X\right|$, where $X$ is an $n \times q$ matrix of full column rank. Then, letting $C=X\left(X^{\prime} X\right)^{-1}$ and $M=I_{n}-X\left(X^{\prime} X\right)^{-1} X^{\prime}$,

$$
\mathrm{d} \phi=2 \operatorname{tr} C^{\prime} \mathrm{d} X=2(\operatorname{vec} C)^{\prime} \mathrm{d} \operatorname{vec} X
$$

and

$$
\mathrm{d}^{2} \phi=2 \operatorname{tr}\left(X^{\prime} X\right)^{-1}(\mathrm{~d} X)^{\prime} M \mathrm{~d} X-2 \operatorname{tr} C^{\prime}(\mathrm{d} X) C^{\prime} \mathrm{d} X
$$

This gives $\mathrm{D} \phi=2(\operatorname{vec} C)^{\prime}$ and

$$
\mathrm{H} \phi=2\left(X^{\prime} X\right)^{-1} \otimes M-2 K_{q n}\left(C \otimes C^{\prime}\right) .
$$

Example 18.7b: Let $\phi(X)=\operatorname{tr} X^{k}$ for $k=1,2, \ldots$, where $X$ is a square $n \times n$ matrix. Then, for $k \geq 1$,

$$
\mathrm{d} \phi=k \operatorname{tr} X^{k-1} \mathrm{~d} X=k\left(\operatorname{vec} X^{\prime k-1}\right)^{\prime} \mathrm{d} \operatorname{vec} X
$$

and for $k \geq 2$,

$$
\mathrm{d}^{2} \phi=k \sum_{j=0}^{k-2} \operatorname{tr} X^{j}(\mathrm{~d} X) X^{k-2-j} \mathrm{~d} X
$$

This gives $\mathrm{D} \phi=k\left(\operatorname{vec} X^{\prime k-1}\right)^{\prime}$ and

$$
\mathrm{H} \phi=(k / 2) \sum_{j=0}^{k-2} K_{n}\left(X^{\prime j} \otimes X^{k-2-j}+X^{\prime k-2-j} \otimes X^{j}\right)
$$

Example 18.8b: Let $F(X)=A X^{-1} B$, where $X$ is a nonsingular $n \times n$ matrix. Then, using Theorem 18.5,

$$
\mathrm{d} \operatorname{vec} F=-\left(\left(X^{-1} B\right)^{\prime} \otimes\left(A X^{-1}\right)\right) \mathrm{d} \operatorname{vec} X,
$$

and hence

$$
\mathrm{D} \operatorname{vec} F=-\left(X^{-1} B\right)^{\prime} \otimes\left(A X^{-1}\right)
$$

To obtain the Hessian matrix of the $s$ th element of $F$, we let

$$
C_{t s}=X^{-1} B e_{t} e_{s}^{\prime} A X^{-1}
$$

where $e_{s}$ and $e_{t}$ are elementary vectors with 1 in the $s$ th (respectively, tth) position and zeros elsewhere. Then,

$$
\mathrm{d}^{2} F_{s t}=2 e_{s}^{\prime} A X^{-1}(\mathrm{~d} X) X^{-1}(\mathrm{~d} X) X^{-1} B e_{t}=2 \operatorname{tr} C_{t s}(\mathrm{~d} X) X^{-1}(\mathrm{~d} X)
$$

and hence

$$
\mathrm{H} F_{s t}=K_{n}\left(C_{t s}^{\prime} \otimes X^{-1}+X^{\prime-1} \otimes C_{t s}\right)
$$

## 15 SYMMETRY AND THE DUPLICATION MATRIX

Many matrices in statistics and econometrics are symmetric, for example variance matrices. When we differentiate with respect to symmetric matrices, we must take the symmetry into account and we need the duplication matrix.

Let $A$ be a square $n \times n$ matrix. Then $\operatorname{vech}(A)$ will denote the $\frac{1}{2} n(n+1) \times 1$ vector that is obtained from vec $A$ by eliminating all elements of $A$ above the diagonal. For example, for $n=3$,

$$
\operatorname{vec} A=\left(a_{11}, a_{21}, a_{31}, a_{12}, a_{22}, a_{32}, a_{13}, a_{23}, a_{33}\right)^{\prime}
$$

and

$$
\operatorname{vech}(A)=\left(a_{11}, a_{21}, a_{31}, a_{22}, a_{32}, a_{33}\right)^{\prime}
$$

In this way, for symmetric $A$, vech $(A)$ contains only the generically distinct elements of $A$. Since the elements of vec $A$ are those of $\operatorname{vech}(A)$ with some repetitions, there exists a unique $n^{2} \times \frac{1}{2} n(n+1)$ matrix which transforms, for symmetric $A$, $\operatorname{vech}(A)$ into vec $A$. This matrix is called the duplication matrix and is denoted by $D_{n}$. Thus,

$$
D_{n} \operatorname{vech}(A)=\operatorname{vec} A \quad\left(A=A^{\prime}\right)
$$

The matrix $D_{n}$ has full column rank $\frac{1}{2} n(n+1)$, so that $D_{n}^{\prime} D_{n}$ is nonsingular. This implies that $\operatorname{vech}(A)$ can be uniquely solved from (23), and we have

$$
\operatorname{vech}(A)=\left(D_{n}^{\prime} D_{n}\right)^{-1} D_{n}^{\prime} \operatorname{vec} A \quad\left(A=A^{\prime}\right)
$$

One can show (but we will not do so here) that the duplication matrix is connected to the commutation matrix by

$$
K_{n} D_{n}=D_{n}, \quad D_{n}\left(D_{n}^{\prime} D_{n}\right)^{-1} D_{n}^{\prime}=\frac{1}{2}\left(I_{n^{2}}+K_{n}\right)
$$

Much of the interest in the duplication matrix is due to the importance of the matrix $D_{n}^{\prime}(A \otimes A) D_{n}$, where $A$ is an $n \times n$ matrix. This matrix is important, because the scalar function $\phi(X)=\operatorname{tr} A X^{\prime} A X$ occurs frequently in statistics and econometrics, for example in the next section on maximum likelihood. When $A$ and $X$ are known to be symmetric we have

$$
\begin{aligned}
\mathrm{d}^{2} \phi & =2 \operatorname{tr} A(\mathrm{~d} X)^{\prime} A \mathrm{~d} X=2(\mathrm{~d} \operatorname{vec} X)^{\prime}(A \otimes A) \mathrm{d} \operatorname{vec} X \\
& =2(\mathrm{~d} \operatorname{vech}(X))^{\prime} D_{n}^{\prime}(A \otimes A) D_{n} \mathrm{~d} \operatorname{vech}(X)
\end{aligned}
$$

and hence, $\mathrm{H} \phi=2 D_{n}^{\prime}(A \otimes A) D_{n}$.
From the relationship (again not proved here)

$$
D_{n}\left(D_{n}^{\prime} D_{n}\right)^{-1} D_{n}^{\prime}(A \otimes A) D_{n}=(A \otimes A) D_{n}
$$

which is valid for any $n \times n$ matrix $A$, not necessarily symmetric, we obtain the inverse

$$
\left(D_{n}^{\prime}(A \otimes A) D_{n}\right)^{-1}=\left(D_{n}^{\prime} D_{n}\right)^{-1} D_{n}^{\prime}\left(A^{-1} \otimes A^{-1}\right) D_{n}\left(D_{n}^{\prime} D_{n}\right)^{-1}
$$

where $A$ is nonsingular. Finally, we present the determinant:

$$
\left|D_{n}^{\prime}(A \otimes A) D_{n}\right|=2^{\frac{1}{2} n(n-1)}|A|^{n+1}
$$

## 16 MAXIMUM LIKELIHOOD

This final section brings together most of the material that has been treated in this chapter: first and second differentials, the Hessian matrix, and the treatment of symmetry (duplication matrix).

We consider a sample of $m \times 1$ vectors $y_{1}, y_{2}, \ldots, y_{n}$ from the multivariate normal distribution with mean $\mu$ and variance $\Omega$, where $\Omega$ is positive definite and $n \geq m+1$. The density of $y_{i}$ is

$$
f\left(y_{i}\right)=(2 \pi)^{-m / 2}|\Omega|^{-1 / 2} \exp \left(-\frac{1}{2}\left(y_{i}-\mu\right)^{\prime} \Omega^{-1}\left(y_{i}-\mu\right)\right)
$$

and since the $y_{i}$ are independent and identically distributed, the joint density of $\left(y_{1}, \ldots, y_{n}\right)$ is given by $\prod_{i} f\left(y_{i}\right)$. The 'likelihood' is equal to the joint density, but now thought of as a function of the parameters $\mu$ and $\Omega$, rather than of the observations. Its logarithm is the 'loglikelihood', which here takes the form

$$
\Lambda(\mu, \Omega)=-\frac{m n}{2} \log 2 \pi-\frac{n}{2} \log |\Omega|-\frac{1}{2} \sum_{i=1}^{n}\left(y_{i}-\mu\right)^{\prime} \Omega^{-1}\left(y_{i}-\mu\right)
$$

The maximum likelihood estimators are obtained by maximizing the loglikelihood (which is the same, but usually easier, as maximizing the likelihood). Thus, we differentiate $\Lambda$ and obtain

$$
\begin{aligned}
\mathrm{d} \Lambda= & -\frac{n}{2} \mathrm{~d} \log |\Omega|+\frac{1}{2} \sum_{i=1}^{n}(\mathrm{~d} \mu)^{\prime} \Omega^{-1}\left(y_{i}-\mu\right) \\
& -\frac{1}{2} \sum_{i=1}^{n}\left(y_{i}-\mu\right)^{\prime}\left(\mathrm{d} \Omega^{-1}\right)\left(y_{i}-\mu\right)+\frac{1}{2} \sum_{i=1}^{n}\left(y_{i}-\mu\right)^{\prime} \Omega^{-1} \mathrm{~d} \mu \\
= & -\frac{n}{2} \mathrm{~d} \log |\Omega|-\frac{1}{2} \sum_{i=1}^{n}\left(y_{i}-\mu\right)^{\prime}\left(\mathrm{d} \Omega^{-1}\right)\left(y_{i}-\mu\right)+\sum_{i=1}^{n}\left(y_{i}-\mu\right)^{\prime} \Omega^{-1} \mathrm{~d} \mu \\
= & -\frac{n}{2} \operatorname{tr}\left(\Omega^{-1} \mathrm{~d} \Omega+S \mathrm{~d} \Omega^{-1}\right)+\sum_{i=1}^{n}\left(y_{i}-\mu\right)^{\prime} \Omega^{-1} \mathrm{~d} \mu
\end{aligned}
$$

where

$$
S=S(\mu)=\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\mu\right)\left(y_{i}-\mu\right)^{\prime}
$$

Denoting the maximum likelihood estimators by $\hat{\mu}$ and $\hat{\Omega}$, letting $\hat{S}=S(\hat{\mu})$, and setting $\mathrm{d} \Lambda=0$ then implies that

$$
\operatorname{tr}\left(\hat{\Omega}^{-1}-\hat{\Omega}^{-1} \hat{S} \hat{\Omega}^{-1}\right) \mathrm{d} \Omega=0
$$

for all $\mathrm{d} \Omega$ and

$$
\sum_{i=1}^{n}\left(y_{i}-\hat{\mu}\right)^{\prime} \hat{\Omega}^{-1} \mathrm{~d} \mu=0
$$

for all $\mathrm{d} \mu$. This, in turn, implies that

$$
\hat{\Omega}^{-1}=\hat{\Omega}^{-1} \hat{S} \hat{\Omega}^{-1}, \quad \sum_{i=1}^{n}\left(y_{i}-\hat{\mu}\right)=0
$$

Hence, the maximum likelihood estimators are given by

$$
\hat{\mu}=\frac{1}{n} \sum_{i=1}^{n} y_{i}=\bar{y}
$$

and

$$
\hat{\Omega}=\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)\left(y_{i}-\bar{y}\right)^{\prime}
$$

We note that the condition that $\Omega$ is symmetric has not been imposed. But since the solution (28) is symmetric, imposing the condition would have made no difference.

The second differential is obtained by differentiating (26) again. This gives

$$
\begin{aligned}
\mathrm{d}^{2} \Lambda= & -\frac{n}{2} \operatorname{tr}\left(\left(\mathrm{~d} \Omega^{-1}\right) \mathrm{d} \Omega+(\mathrm{d} S) \mathrm{d} \Omega^{-1}+S \mathrm{~d}^{2} \Omega^{-1}\right)-n(\mathrm{~d} \mu)^{\prime} \Omega^{-1} \mathrm{~d} \mu \\
& +\sum_{i=1}^{n}\left(y_{i}-\mu\right)^{\prime}\left(\mathrm{d} \Omega^{-1}\right) \mathrm{d} \mu
\end{aligned}
$$

We are usually not primarily interested in the Hessian matrix but in its expectation. Hence, we do not evaluate (29) further and first take expectations. Since $\mathrm{E}(S)=\Omega$ and $\mathrm{E}(\mathrm{d} S)=0$, we obtain

$$
\begin{aligned}
\mathrm{Ed}^{2} \Lambda & =-\frac{n}{2} \operatorname{tr}\left(\left(\mathrm{~d} \Omega^{-1}\right) \mathrm{d} \Omega+\Omega \mathrm{d}^{2} \Omega^{-1}\right)-n(\mathrm{~d} \mu)^{\prime} \Omega^{-1} \mathrm{~d} \mu \\
& =\frac{n}{2} \operatorname{tr} \Omega^{-1}(\mathrm{~d} \Omega) \Omega^{-1} \mathrm{~d} \Omega-n \operatorname{tr}(\mathrm{~d} \Omega) \Omega^{-1}(\mathrm{~d} \Omega) \Omega^{-1}-n(\mathrm{~d} \mu)^{\prime} \Omega^{-1} \mathrm{~d} \mu \\
& =-\frac{n}{2} \operatorname{tr} \Omega^{-1}(\mathrm{~d} \Omega) \Omega^{-1} \mathrm{~d} \Omega-n(\mathrm{~d} \mu)^{\prime} \Omega^{-1} \mathrm{~d} \mu,
\end{aligned}
$$

using the facts that $\mathrm{d} \Omega^{-1}=-\Omega^{-1}(\mathrm{~d} \Omega) \Omega^{-1}$ and

$$
\begin{aligned}
\mathrm{d}^{2} \Omega^{-1} & =-\left(\mathrm{d} \Omega^{-1}\right)(\mathrm{d} \Omega) \Omega^{-1}-\Omega^{-1}(\mathrm{~d} \Omega) \mathrm{d} \Omega^{-1} \\
& =2 \Omega^{-1}(\mathrm{~d} \Omega) \Omega^{-1}(\mathrm{~d} \Omega) \Omega^{-1} .
\end{aligned}
$$

To obtain the 'information matrix' we need to take the symmetry of $\Omega$ into account and this is where the duplication matrix appears. So far, we have avoided the vec operator and in practical situations one should work with differentials (rather than with derivatives) as long as possible. But we cannot go further than (30) without use of the vec operator. Thus, from (30),

$$
\begin{aligned}
& -\operatorname{Ed}^{2} \Lambda=\frac{n}{2} \operatorname{tr} \Omega^{-1}(\mathrm{~d} \Omega) \Omega^{-1} \mathrm{~d} \Omega+n(\mathrm{~d} \mu)^{\prime} \Omega^{-1} \mathrm{~d} \mu \\
& \quad=\frac{n}{2}(\mathrm{~d} \operatorname{vec} \Omega)^{\prime}\left(\Omega^{-1} \otimes \Omega^{-1}\right) \mathrm{d} \operatorname{vec} \Omega+n(\mathrm{~d} \mu)^{\prime} \Omega^{-1} \mathrm{~d} \mu \\
& \quad=\frac{n}{2}(\mathrm{~d} \operatorname{vech}(\Omega))^{\prime} D_{m}^{\prime}\left(\Omega^{-1} \otimes \Omega^{-1}\right) D_{m} \mathrm{~d} \operatorname{vech}(\Omega)+n(\mathrm{~d} \mu)^{\prime} \Omega^{-1} \mathrm{~d} \mu
\end{aligned}
$$

Hence, the information matrix for $\mu$ and $\operatorname{vech}(\Omega)$ is

$$
\mathcal{F}=n\left(\begin{array}{cc}
\Omega^{-1} & 0 \\
0 & \frac{1}{2} D_{m}^{\prime}\left(\Omega^{-1} \otimes \Omega^{-1}\right) D_{m}
\end{array}\right) .
$$

The results on the duplication matrix in Section 18.15 also allow us to obtain the inverse:

$$
(\mathcal{F} / n)^{-1}=\left(\begin{array}{cc}
\Omega & 0 \\
0 & 2\left(D_{m}^{\prime} D_{m}\right)^{-1} D_{m}^{\prime}(\Omega \otimes \Omega) D_{m}\left(D_{m}^{\prime} D_{m}\right)^{-1}
\end{array}\right)
$$

and the determinant:

$$
|\mathcal{F} / n|=|\Omega| \cdot\left|2\left(D_{m}^{\prime} D_{m}\right)^{-1} D_{m}^{\prime}(\Omega \otimes \Omega) D_{m}\left(D_{m}^{\prime} D_{m}\right)^{-1}\right|=2^{m}|\Omega|^{m+2} .
$$

## FURTHER READING

§2-3. Chapter 5 discusses differentials in more detail, and contains the first identification theorem (Theorem 5.6) and the chain rule for first differentials (Theorem 5.9), officially called 'Cauchy's rule of invariance'.
§4. Optimization is discussed in Chapter 7.
§5. See Chapter 11, Sections 11.29-11.32 and Chapter 13, Sections 13.4 and 13.19.
§6. The trace is discussed in Section 1.10, the extension from vector calculus to matrix calculus in Section 5.15, and the differentials of the determinant and inverse in Sections 8.3 and 8.4.
§7. See Section 1.6 for more detailed results.
§8-9. Second differentials are introduced in Chapter 6. The second identification theorem is proved in Section 6.8 and the chain rule for second differentials in Section 6.11.
§11. See Chapter 2 for many more details on the vec operator and the Kronecker product. Theorem 2.2 is restated here as Theorem 18.5.
§12. See Sections 5.15 and 10.2.
§13 and § 15 . The commutation matrix and the duplication matrix are discussed in Chapter 3.
§16. Many aspects of maximum likelihood estimation are treated in Chapter 15 .

