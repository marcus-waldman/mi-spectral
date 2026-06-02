# Layer-3 modeA response — model=gpt-5.5

Let \(O_i=(R_i,Y_{i,\mathrm{obs}})\) denote the observed data for unit \(i\), including its missingness pattern \(R_i\). Let \(M_i=Y_{i,\mathrm{mis}}\). All expectations below are under the true joint law

\[
Y_i\sim N_p(\mu_0,\Sigma_0),\qquad 
R_i\mid Y_i \sim \pi_r(A_i),
\]

where \(A_i\) are the always-observed coordinates. The imputation conditional law is the model law \(p_\phi(M_i\mid O_i)\), which is valid under ignorability/MAR.

I use total-sample information matrices, so \(I_{\mathrm{obs}}=O(n)\), \(I_{\mathrm{obs}}^{-1}=O(n^{-1})\), and

\[
\operatorname{Var}(\delta)=\operatorname{Var}(\hat\theta_{\mathrm{obs}}-\theta_0)
=I_{\mathrm{obs}}^{-1}+o(n^{-1}).
\]

Write

\[
\delta=\hat\theta_{\mathrm{obs}}-\theta_0.
\]

For compactness define, at \((\theta_{\rm eval},\phi)=(\theta_0,\theta_0)\),

\[
g:=\nabla_\phi F,\qquad 
H:=\nabla_\phi^2 F,\qquad 
C:=\nabla_{\theta_{\rm eval}}\nabla_\phi F.
\]

All three are random observed-data functions and are sums over units, hence \(O_p(n)\).

---

## 1. Taylor expansion of \(A_{\rm rb}\)

Define

\[
f(a,b):=F(\theta_0+a,\theta_0+b).
\]

Then

\[
A_{\rm rb}
=F(\theta_0+\delta,\theta_0+\delta)
 -F(\theta_0+\delta,\theta_0)
=f(\delta,\delta)-f(\delta,0).
\]

A second-order Taylor expansion around \((0,0)\) gives

\[
\begin{aligned}
f(\delta,\delta)
&=f(0,0)
+F_\theta^\top \delta
+F_\phi^\top \delta \\
&\quad
+\frac12 \delta^\top F_{\theta\theta}\delta
+\delta^\top F_{\theta\phi}\delta
+\frac12 \delta^\top F_{\phi\phi}\delta
+o_p(1),
\end{aligned}
\]

whereas

\[
f(\delta,0)
=f(0,0)
+F_\theta^\top\delta
+\frac12\delta^\top F_{\theta\theta}\delta
+o_p(1).
\]

The eval-slot-only terms cancel. Therefore

\[
\boxed{
A_{\rm rb}
=
g^\top\delta
+\delta^\top C\delta
+\frac12\delta^\top H\delta
+o_p(1).
}
\]

The three leading pieces are:

\[
\boxed{
\text{gradient term: } g^\top\delta,
}
\]

\[
\boxed{
\text{eval--impute cross term: } \delta^\top C\delta,
}
\]

\[
\boxed{
\text{impute-slot curvature term: } \frac12\delta^\top H\delta.
}
\]

The cross term \(\delta^\top C\delta\) is the term missed by an expansion that treats only the imputation slot.

Let \(S_{\rm obs}:=\nabla_\theta \ell_{\rm obs}(\theta_0)\) be the observed-data score. The usual MLE expansion gives

\[
\delta
=
I_{\rm obs}^{-1}S_{\rm obs}
+\frac{b}{n}
+o_p(n^{-1/2}),
\]

where \(b\) is the \(O(n^{-1})\) MLE bias vector. In this problem only the covariance block matters, so effectively

\[
b=(0,\operatorname{vech} b_\Sigma).
\]

Taking expectations,

\[
E[\delta]=\frac{b}{n}+o(n^{-1}),\qquad 
\operatorname{Var}(\delta)=I_{\rm obs}^{-1}+o(n^{-1}).
\]

Now decompose the expectation of the gradient term:

\[
E[g^\top\delta]
=
E[g]^\top E[\delta]
+
E\{(g-Eg)^\top(\delta-E\delta)\}.
\]

Using \(\delta-E\delta=I_{\rm obs}^{-1}S_{\rm obs}+o_p(n^{-1/2})\),

\[
\boxed{
E[g^\top\delta]
=
E[g]^\top \frac{b}{n}
+
\operatorname{tr}\!\left(
I_{\rm obs}^{-1}\operatorname{Cov}(S_{\rm obs},g)
\right)
+o(1).
}
\]

The second term is \(O(1)\). It is often silently missed.

For the quadratic terms, since \(C,H=O_p(n)\) and \(\delta=O_p(n^{-1/2})\),

\[
E[\delta^\top C\delta]
=
\operatorname{tr}\!\left(E[C]\,I_{\rm obs}^{-1}\right)
+o(1),
\]

and

\[
E\!\left[\frac12\delta^\top H\delta\right]
=
\frac12
\operatorname{tr}\!\left(E[H]\,I_{\rm obs}^{-1}\right)
+o(1).
\]

Therefore

\[
\boxed{
E[A_{\rm rb}]
=
E[g]^\top\frac{b}{n}
+
\operatorname{tr}\!\left(
I_{\rm obs}^{-1}\operatorname{Cov}(S_{\rm obs},g)
\right)
+
\operatorname{tr}\!\left(E[C]\,I_{\rm obs}^{-1}\right)
+
\frac12\operatorname{tr}\!\left(E[H]\,I_{\rm obs}^{-1}\right)
+o(1).
}
\]

Each displayed term is \(O(1)\).

---

## 2. Probabilistic identity for the cross Hessian \(C\)

Let

\[
s_{\rm com}(Y;\theta)
:=\nabla_\theta \ell_{\rm com}(\theta;Y)
\]

be the complete-data score, and let

\[
s_{\rm obs}(O;\theta)
:=\nabla_\theta \ell_{\rm obs}(\theta;O)
\]

be the observed-data score. Define the missing-data conditional score

\[
s_{\rm mis}(Y;\theta)
:=
\nabla_\theta \log p_\theta(Y_{\rm mis}\mid Y_{\rm obs},R).
\]

Under MAR ignorability,

\[
p_\theta(Y_{\rm mis}\mid Y_{\rm obs},R)
=
p_\theta(Y_{\rm mis}\mid Y_{\rm obs}),
\]

so \(R\) only determines which conditional distribution is used.

The Fisher identity gives

\[
s_{\rm obs}(O;\theta_0)
=
E_0\{s_{\rm com}(Y;\theta_0)\mid O\}.
\]

Also,

\[
s_{\rm com}(Y;\theta_0)
=
s_{\rm obs}(O;\theta_0)+s_{\rm mis}(Y;\theta_0),
\]

with

\[
E_0\{s_{\rm mis}(Y;\theta_0)\mid O\}=0.
\]

Now

\[
F_{\theta_{\rm eval}}(\theta_0,\theta_0)
=
E_0\{s_{\rm com}(Y;\theta_0)\mid O\}.
\]

Differentiate this with respect to the imputation parameter \(\phi\). Differentiating a conditional expectation gives multiplication by the conditional score. Thus, for one unit,

\[
\begin{aligned}
C_i
&=
\nabla_{\theta_{\rm eval}}\nabla_\phi
E_\phi\{\ell_{\rm com}(\theta_{\rm eval};Y)\mid O_i\}
\bigg|_{\theta_{\rm eval}=\phi=\theta_0} \\
&=
E_0\!\left[
s_{\rm com}(Y_i;\theta_0)
s_{\rm mis}(Y_i;\theta_0)^\top
\mid O_i
\right].
\end{aligned}
\]

Using \(s_{\rm com}=s_{\rm obs}+s_{\rm mis}\) and \(E(s_{\rm mis}\mid O)=0\),

\[
\boxed{
C_i
=
E_0\!\left[
s_{\rm mis}(Y_i;\theta_0)
s_{\rm mis}(Y_i;\theta_0)^\top
\mid O_i
\right].
}
\]

Equivalently,

\[
\boxed{
C_i
=
\operatorname{Var}_0\{s_{\rm com}(Y_i;\theta_0)\mid O_i\}.
}
\]

Therefore

\[
\boxed{
C=\sum_{i=1}^n C_i
=
\sum_{i=1}^n
\operatorname{Var}_0\{s_{\rm com}(Y_i;\theta_0)\mid O_i\}.
}
\]

This is the conditional missing information.

Taking expectation over the true observed-data law,

\[
E[C]
=
E\!\left[
\operatorname{Var}_0\{S_{\rm com}\mid O\}
\right],
\]

where \(S_{\rm com}=\sum_i s_{\rm com}(Y_i;\theta_0)\).

By Louis’ missing-information identity,

\[
I_{\rm com}
=
I_{\rm obs}
+
E[C],
\]

so

\[
\boxed{
E[C]=I_{\rm mis\mid obs}:=I_{\rm com}-I_{\rm obs}.
}
\]

Consequently,

\[
\boxed{
\operatorname{tr}\!\left(E[C]\,I_{\rm obs}^{-1}\right)
=
\operatorname{tr}\!\left(I_{\rm obs}^{-1}I_{\rm mis\mid obs}\right)
=
\mathrm{RIV}.
}
\]

Important nuance: the random sample matrix \(C\) itself is not exactly \(I_{\rm mis\mid obs}\). The equality is for its expectation, or equivalently its probability limit after scaling by \(n\).

### MAR selection issue

For pattern \(r\), let \(o_r\) be the observed coordinates and \(m_r\) the missing coordinates. Define

\[
J_r(y_{o_r})
:=
\operatorname{Var}_0\{s_{\rm com}(Y;\theta_0)\mid Y_{o_r}=y_{o_r},R=r\}.
\]

Under MAR,

\[
P(R=r\mid Y)=\pi_r(A),
\]

where \(A\) are the always-observed coordinates. Therefore

\[
E[C_i]
=
\sum_r
E_0\!\left[
\pi_r(A)\,J_r(Y_{o_r})
\right].
\]

Thus the missing information is evaluated on the actually selected incomplete units. It is not, in general,

\[
\sum_r P(R=r)\,E_0\{J_r(Y_{o_r})\}.
\]

Those coincide under MCAR, because then \(\pi_r(A)\) is constant, but under genuine MAR they need not coincide. So:

\[
\boxed{
\text{Under MAR, the relevant missing information is selected-pattern information, not population-pattern information.}
}
\]

If \(I_{\rm mis\mid obs}\) is correctly defined as \(I_{\rm com}-I_{\rm obs}\) under the actual MAR observed-data experiment, then

\[
\operatorname{tr}(E[C]I_{\rm obs}^{-1})=\mathrm{RIV}.
\]

If instead one plugs in an unselected population missing-information matrix, the equality generally fails under MAR.

---

## 3. Final expression for \(D=E[A_{\rm rb}]-\mathrm{RIV}\)

From the expansion above,

\[
E[A_{\rm rb}]
=
E[g]^\top\frac{b}{n}
+
\operatorname{tr}\!\left(
I_{\rm obs}^{-1}\operatorname{Cov}(S_{\rm obs},g)
\right)
+
\operatorname{tr}\!\left(E[C]\,I_{\rm obs}^{-1}\right)
+
\frac12\operatorname{tr}\!\left(E[H]\,I_{\rm obs}^{-1}\right)
+o(1).
\]

Therefore

\[
\boxed{
D
=
E[g]^\top\frac{b}{n}
+
\operatorname{tr}\!\left(
I_{\rm obs}^{-1}\operatorname{Cov}(S_{\rm obs},g)
\right)
+
\left\{
\operatorname{tr}\!\left(E[C]\,I_{\rm obs}^{-1}\right)
-\mathrm{RIV}
\right\}
+
\frac12\operatorname{tr}\!\left(E[H]\,I_{\rm obs}^{-1}\right)
+o(1).
}
\]

With the correct selected MAR information,

\[
\operatorname{tr}\!\left(E[C]\,I_{\rm obs}^{-1}\right)
=
\mathrm{RIV},
\]

so the cross-information contribution cancels the subtracted RIV, giving

\[
\boxed{
D
=
E[g]^\top\frac{b}{n}
+
\operatorname{tr}\!\left(
I_{\rm obs}^{-1}\operatorname{Cov}(S_{\rm obs},g)
\right)
+
\frac12\operatorname{tr}\!\left(E[H]\,I_{\rm obs}^{-1}\right)
+o(1).
}
\]

The four named \(O(1)\) pieces before cancellation are:

1. **MLE bias \(\times\) imputation-gradient term**
   \[
   B_{\rm bias}
   :=
   E[g]^\top\frac{b}{n}.
   \]

2. **Gradient-score covariance term**
   \[
   B_{\rm cov}
   :=
   \operatorname{tr}\!\left(
   I_{\rm obs}^{-1}\operatorname{Cov}(S_{\rm obs},g)
   \right).
   \]

3. **Eval-impute cross-information term**
   \[
   B_{\rm cross}
   :=
   \operatorname{tr}\!\left(E[C]\,I_{\rm obs}^{-1}\right).
   \]

4. **Pure impute-slot curvature term**
   \[
   B_{\rm curv}
   :=
   \frac12\operatorname{tr}\!\left(E[H]\,I_{\rm obs}^{-1}\right).
   \]

Thus

\[
D
=
B_{\rm bias}
+
B_{\rm cov}
+
(B_{\rm cross}-\mathrm{RIV})
+
B_{\rm curv}
+o(1).
\]

With correctly selected MAR information, \(B_{\rm cross}=\mathrm{RIV}\), so

\[
D
=
B_{\rm bias}+B_{\rm cov}+B_{\rm curv}+o(1).
\]

---

## Normal-model simplification of \(g\)

For a pattern \(r\), let

\[
V_r(\Sigma)
=
\Sigma_{m_rm_r}
-
\Sigma_{m_ro_r}\Sigma_{o_ro_r}^{-1}\Sigma_{o_rm_r}
\]

be the conditional covariance of \(Y_{m_r}\mid Y_{o_r}\).

For the Gaussian model,

\[
q_r(\theta_0,\phi)
=
E_\phi\{\ell_{\rm com}(\theta_0;Y)\mid O,R=r\}
\]

depends on \(\phi\) through the conditional mean and covariance. At \(\phi=\theta_0\), the derivative with respect to the conditional mean vanishes, while the derivative with respect to the conditional covariance gives

\[
dq_r
=
-\frac12 \operatorname{tr}\{V_r(\Sigma_0)^{-1}dV_r\}.
\]

Therefore

\[
\boxed{
g_{i,\mu}=0,
\qquad
g_{i,\Sigma}
=
-\frac12
\nabla_{\operatorname{vech}\Sigma}
\log |V_{R_i}(\Sigma_0)|.
}
\]

So only the \(\Sigma\)-block of \(E[\delta]\), namely \(b_\Sigma/n\), enters \(B_{\rm bias}\).

---

## MCAR versus MAR

Under **MCAR**, the pattern \(R\) is independent of \(Y\). For the Gaussian model \(g_i\) is pattern-dependent but, at \(\theta_0\), not otherwise data-dependent. Hence

\[
E\{S_{\rm obs}\mid R=r\}=0,
\]

so

\[
\boxed{
B_{\rm cov}=0\quad\text{under MCAR.}
}
\]

Also, under MCAR, selected-pattern and population-pattern missing information coincide, so there is no selection discrepancy in \(B_{\rm cross}\).

However, \(B_{\rm bias}\) and \(B_{\rm curv}\) do not generally vanish under MCAR. They vanish only in special cases, for example with no missingness or if the relevant bias/curvature happens to be zero.

Under genuine **MAR**, the pattern probabilities depend on always-observed variables. Then

\[
E\{S_{\rm obs}\mid R=r\}
\]

need not be zero, and therefore

\[
\boxed{
B_{\rm cov}\ \text{generally survives under MAR.}
}
\]

Also, the selected-pattern missing information

\[
\sum_r E_0[\pi_r(A)J_r(Y_{o_r})]
\]

generally differs from the corresponding unselected population average. Thus any calculation using population rather than selected missing information will generally be wrong under MAR.

Finally, the whole correction is \(O(1)\):

\[
E[g]^\top E[\delta]=O(n)O(n^{-1})=O(1),
\]

\[
\operatorname{tr}\{I_{\rm obs}^{-1}\operatorname{Cov}(S_{\rm obs},g)\}
=O(n^{-1})O(n)=O(1),
\]

\[
\operatorname{tr}(E[C]I_{\rm obs}^{-1})=O(n)O(n^{-1})=O(1),
\]

and

\[
\operatorname{tr}(E[H]I_{\rm obs}^{-1})=O(n)O(n^{-1})=O(1).
\]

So \(D\) is \(O(1)\), not \(O(n)\) and not \(O(n^{-1})\).

A two-term answer of the form

\[
D=\alpha^\top E[\delta]
+\frac12\operatorname{tr}(\nabla_\phi^2F\,I_{\rm obs}^{-1})
\]

misses at least the eval-impute cross term \(\delta^\top C\delta\), whose expectation is the RIV contribution, and under MAR it also misses the \(O(1)\) gradient-score covariance term

\[
\operatorname{tr}\!\left(
I_{\rm obs}^{-1}\operatorname{Cov}(S_{\rm obs},g)
\right).
\]
