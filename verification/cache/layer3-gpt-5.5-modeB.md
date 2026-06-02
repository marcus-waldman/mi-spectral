# Layer-3 modeB response — model=gpt-5.5

## Verdict

The weakest premise is the definition of \(\bar Q_\infty\). As written,

\[
\bar Q_\infty(\theta):=E\{\ell_{\rm com}(\theta;Y)\mid Y_{\rm obs}\}
\]

denotes the **true conditional expectation** unless an imputation-law subscript is added. If that is the object, then the proof’s Term-A calculation cannot be right: by the tower property its expectation is exactly zero. The claimed \(+\operatorname{tr}({\rm RIV})\) comes from a different object: an **imputation-posterior predictive average**, and in fact usually of a **chosen likelihood kernel/contrast**, not the full complete-data log-density. Without that restatement, the headline \(+\tfrac12\operatorname{tr}({\rm RIV})\) is not robust.

---

## 1. Definition of \(\bar Q_\infty\): true conditional vs imputation predictive

Let \(E_0\) denote expectation under the true data law at \(\theta_0\). If

\[
Q_0(\theta)=E_0\{\ell_{\rm com}(\theta;Y)\mid Y_{\rm obs}\},
\]

then \(\hat\theta_{\rm obs}\) is \(Y_{\rm obs}\)-measurable, so

\[
E_0\!\left[
Q_0(\hat\theta_{\rm obs})
-\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right]
=
E_0\!\left[
E_0\{\ell_{\rm com}(\hat\theta_{\rm obs};Y)\mid Y_{\rm obs}\}
-\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right]
=0.
\]

So under the literal definition, Term A has expectation \(0\), not \(+\operatorname{tr}({\rm RIV})\). Then the total comparison becomes, to first order,

\[
E_0\!\left[
Q_0(\hat\theta_{\rm obs})-\ell_{\rm com}(\hat\theta_{\rm com})
\right]
=
E_0\!\left[
\ell_{\rm com}(\hat\theta_{\rm obs})
-\ell_{\rm com}(\hat\theta_{\rm com})
\right]
=
-\frac12\operatorname{tr}({\rm RIV})+o(1),
\]

not \(+\frac12\operatorname{tr}({\rm RIV})\).

The manuscript’s Term-A step instead uses something like

\[
Q_{\rm imp}(\theta)
=
E_{\tilde\phi\mid Y_{\rm obs}}^{\rm imp}
E_{Y_{\rm mis}\mid Y_{\rm obs},\tilde\phi}^{\rm imp}
\{\ell_{\rm com}(\theta;Y_{\rm obs},Y_{\rm mis})\}.
\]

That is not \(E_0\{\ell_{\rm com}(\theta;Y)\mid Y_{\rm obs}\}\). The difference

\[
E_0\{Q_{\rm imp}(\hat\theta_{\rm obs})-Q_0(\hat\theta_{\rm obs})\}
\]

is exactly where the claimed imputation-bias term could arise.

More precisely, if one works with a complete-data likelihood **kernel/contrast** \(\ell_{\rm com}^\dagger\) with \(Y\)-only constants removed, then the local expansion gives

\[
E_0\{Q_{\rm imp}^\dagger(\hat\theta_{\rm obs})
      -Q_0^\dagger(\hat\theta_{\rm obs})\}
\approx
\operatorname{tr}\!\left(I_{\rm mis\mid obs}I_{\rm obs}^{-1}\right)
=
\operatorname{tr}({\rm RIV}).
\]

That is the object yielding \(+\operatorname{tr}({\rm RIV})\).

But the literal true-conditional object \(Q_0\) yields \(0\). Also, if one uses the full normalized complete-data log-density rather than a kernel, additional \(Y_{\rm mis}\)-dependent but \(\theta\)-free terms appear; those can contribute \(O(1)\) and can even cancel the \(+\operatorname{tr}({\rm RIV})\) term.

Concrete check: normal mean, known variance, MCAR. Let \(n_o\) observed and \(n_m\) missing, so \({\rm RIV}=n_m/n_o\). With the full density

\[
\ell_{\rm com}(\mu)=-\frac12\sum_i(y_i-\mu)^2+\text{const},
\]

proper posterior predictive imputation with \(\tilde\mu\mid Y_{\rm obs}\sim N(\bar Y_o,1/n_o)\) gives

\[
E\{Q_{\rm imp}(\bar Y_o)-\ell_{\rm com}(\bar Y_o)\}=0.
\]

But if one drops the \(-\frac12\sum y_i^2\) term and uses the kernel

\[
\ell_{\rm com}^\dagger(\mu)=\mu\sum_i y_i-\frac n2\mu^2,
\]

then

\[
E\{Q_{\rm imp}^\dagger(\bar Y_o)
-\ell_{\rm com}^\dagger(\bar Y_o)\}
=
\frac{n_m}{n_o}
=
\operatorname{tr}({\rm RIV}).
\]

So the \(+\operatorname{tr}({\rm RIV})\) term is not a property of the advertised conditional expectation of the full log-density. It is a property of a specific imputation-predictive likelihood-kernel convention.

---

## 2. The \(-\frac12\operatorname{tr}({\rm RIV})\) term

This part is essentially correct, provided \(\hat\theta_{\rm com}\) is the actual complete-data MLE for the same sample.

Let \(U_{\rm obs}\) and \(U_{\rm com}\) be observed- and complete-data scores at \(\theta_0\). Louis’ identity gives

\[
U_{\rm obs}=E(U_{\rm com}\mid Y_{\rm obs}),
\]

hence

\[
\operatorname{Cov}(U_{\rm obs},U_{\rm com})
=
\operatorname{Var}(U_{\rm obs})
=
I_{\rm obs}.
\]

Using the MLE linearizations,

\[
\hat\theta_{\rm obs}-\theta_0
=
I_{\rm obs}^{-1}U_{\rm obs}+o_p(n^{-1/2}),
\]

\[
\hat\theta_{\rm com}-\theta_0
=
I_{\rm com}^{-1}U_{\rm com}+o_p(n^{-1/2}),
\]

we get

\[
\operatorname{Cov}(\hat\theta_{\rm obs},\hat\theta_{\rm com})
=
I_{\rm obs}^{-1}
\operatorname{Cov}(U_{\rm obs},U_{\rm com})
I_{\rm com}^{-1}
=
I_{\rm com}^{-1}.
\]

Therefore

\[
\operatorname{Var}(\hat\theta_{\rm obs}-\hat\theta_{\rm com})
=
I_{\rm obs}^{-1}-I_{\rm com}^{-1}.
\]

Taylor expanding the complete-data loglikelihood around \(\hat\theta_{\rm com}\),

\[
\ell_{\rm com}(\hat\theta_{\rm obs})
-\ell_{\rm com}(\hat\theta_{\rm com})
=
-\frac12
(\hat\theta_{\rm obs}-\hat\theta_{\rm com})'
I_{\rm com}
(\hat\theta_{\rm obs}-\hat\theta_{\rm com})
+o_p(1),
\]

so

\[
E[B]
=
-\frac12
\operatorname{tr}\!\left[
I_{\rm com}
\left(I_{\rm obs}^{-1}-I_{\rm com}^{-1}\right)
\right]
+o(1).
\]

Since \(I_{\rm com}=I_{\rm obs}+I_{\rm mis\mid obs}\),

\[
E[B]
=
-\frac12
\left\{
\operatorname{tr}(I_{\rm com}I_{\rm obs}^{-1})-k
\right\}
+o(1)
=
-\frac12
\operatorname{tr}(I_{\rm mis\mid obs}I_{\rm obs}^{-1})
+o(1)
=
-\frac12\operatorname{tr}({\rm RIV})
+o(1).
\]

So the covariance claim

\[
\operatorname{Cov}(\hat\theta_{\rm obs},\hat\theta_{\rm com})=I_{\rm com}^{-1}
\]

is correct to first order.

Minor correction: if one incorrectly used \(\operatorname{Var}(\hat\theta_{\rm obs})\) with complete-data curvature, the term would be

\[
-\frac12\operatorname{tr}(I_{\rm com}I_{\rm obs}^{-1})
=
-\frac12\{k+\operatorname{tr}({\rm RIV})\},
\]

not merely \(-\frac12 k\). The \(-\frac12 k\) result would come from using observed-data curvature instead.

---

## 3. Congeniality/properness: what is actually used?

The \(-\frac12\operatorname{tr}({\rm RIV})\) calculation does not need Rubin properness or Meng congeniality. It needs regular likelihood theory, ignorability, and Louis’ identity.

For the Term-A cross term, however, the proof needs more than “proper MI” in a generic sense. It needs something like

\[
E_{\rm imp}(\tilde\phi\mid Y_{\rm obs})
=
\hat\theta_{\rm obs}+o_p(n^{-1/2}),
\]

and hence

\[
\operatorname{Cov}(\tilde\phi,\hat\theta_{\rm obs})
=
\operatorname{Cov}\!\left(
E_{\rm imp}(\tilde\phi\mid Y_{\rm obs}),
\hat\theta_{\rm obs}
\right)
=
\operatorname{Var}(\hat\theta_{\rm obs})+o(n^{-1})
=
I_{\rm obs}^{-1}+o(n^{-1}).
\]

This follows under a correct, congenial parametric imputation model plus a Bernstein–von Mises type posterior approximation. It is not a consequence of Rubin properness alone.

Similarly,

\[
T_\infty=I_{\rm obs}^{-1}
\]

requires more than \(m\to\infty\). Infinite \(m\) removes Monte Carlo error only. To identify Rubin’s total variance with the observed-data MLE variance, one needs a congenial/self-efficient setup in which

\[
W_\infty\approx I_{\rm com}^{-1},
\qquad
B_\infty\approx I_{\rm obs}^{-1}-I_{\rm com}^{-1},
\]

so that

\[
T_\infty=W_\infty+B_\infty\approx I_{\rm obs}^{-1}.
\]

This is true in the standard regular congenial likelihood case, but it is not guaranteed merely by saying “proper MI.” Uncongeniality, non-self-efficient complete-data procedures, prior shrinkage of non-negligible order, or an imputation parameter not aligned with the analysis parameter can break the required covariance and variance identities.

---

## 4. MAR \((A)+(C)\) term

If \(\bar Q_\infty\) is the literal true conditional expectation, then there is no Term-A bias under MAR or MCAR:

\[
E_0\{Q_0(\hat\theta_{\rm obs})-\ell_{\rm com}(\hat\theta_{\rm obs})\}=0
\]

exactly. So the MAR \((A)+(C)\) term only belongs to the imputation-predictive/kernel version of the result.

For that version, an \(O(1)\) design-imbalance term is plausible: the information matrices scale as \(O(n)\), while

\[
\hat\theta_{\rm obs}-\theta_0=O_p(n^{-1/2}),
\qquad
\tilde\phi-\theta_0=O_p(n^{-1/2}),
\]

so products like

\[
(\hat\theta_{\rm obs}-\theta_0)'
I_{\rm mis\mid obs}
(\tilde\phi-\theta_0)
\]

are \(O_p(1)\). Thus the term is not \(O(n)\), and it is not generally \(O(n^{-1})\) when the missing fraction tends to a nonzero limit.

For the quoted bivariate-monotone expression

\[
\frac{n_{\rm mis}}{n_{\rm obs}}
\left[
1-\frac12\operatorname{tr}(Q_{\rm mis}Q_{\rm obs}^{-1})
\right],
\]

the MCAR cancellation is algebraically correct at the population/leading-order level if \(Q_{\rm mis}=Q_{\rm obs}\) and the matrix dimension is \(2\), because then

\[
\operatorname{tr}(Q_{\rm mis}Q_{\rm obs}^{-1})=\operatorname{tr}(I_2)=2.
\]

But this is model-specific. It is not a general MAR theorem. Also, finite-sample MCAR cancellation is only approximate unless the realized \(Q_{\rm mis}\) and \(Q_{\rm obs}\) are exactly equal; typically their difference is sampling noise, so the remaining contribution is lower order.

---

## Conclusion

The headline sign is not robust. Under the definition actually written,

\[
\bar Q_\infty(\theta)
=
E_0\{\ell_{\rm com}(\theta;Y)\mid Y_{\rm obs}\},
\]

Term A has expectation \(0\), so the leading sign is

\[
-\frac12\operatorname{tr}({\rm RIV}),
\]

not \(+\frac12\operatorname{tr}({\rm RIV})\).

To make the claimed

\[
+\frac12\operatorname{tr}({\rm RIV})
\]

statement correct and unambiguous, the manuscript must minimally restate the definitions as follows:

1. Define \(\bar Q_\infty\) as an **imputation-posterior predictive** expectation, not a true conditional expectation:

   \[
   \bar Q_{\infty}^{\rm imp}(\theta)
   =
   E_{\tilde\phi\mid Y_{\rm obs}}^{\rm imp}
   E_{Y_{\rm mis}\mid Y_{\rm obs},\tilde\phi}^{\rm imp}
   \{\ell_{\rm com}^\dagger(\theta;Y_{\rm obs},Y_{\rm mis})\}.
   \]

2. Specify that \(\ell_{\rm com}^\dagger\) is a fixed complete-data likelihood **kernel/contrast** with \(Y\)-only constants removed, e.g.

   \[
   \ell_{\rm com}^\dagger(\theta;Y)
   =
   \ell_{\rm com}(\theta;Y)-\ell_{\rm com}(\theta_0;Y),
   \]

   or an equivalent LAN contrast. The result is not invariant to arbitrary data-dependent constants.

3. Add explicit asymptotic assumptions ensuring

   \[
   E_{\rm imp}(\tilde\phi\mid Y_{\rm obs})
   =
   \hat\theta_{\rm obs}+o_p(n^{-1/2}),
   \qquad
   \operatorname{Cov}(\tilde\phi,\hat\theta_{\rm obs})
   =
   I_{\rm obs}^{-1}+o(n^{-1}),
   \]

   and

   \[
   T_\infty=I_{\rm obs}^{-1}+o(n^{-1}).
   \]

With those clarified definitions, the decomposition

\[
E[A]=+\operatorname{tr}({\rm RIV})+(A)+(C)+o(1),
\qquad
E[B]=-\frac12\operatorname{tr}({\rm RIV})+o(1)
\]

can yield the advertised

\[
+\frac12\operatorname{tr}({\rm RIV})+(A)+(C)+o(1).
\]

But under the stated definition as a true conditional expectation of the complete-data log-density, the claim is false.
