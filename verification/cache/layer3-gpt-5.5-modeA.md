# Layer-3 modeA response — model=gpt-5.5

Let \(\theta_0\) denote the true parameter. I will take \(I_{\rm com},I_{\rm obs}\) to be the \(n\)-sample expected information matrices; using per-observation information gives the same \(RIV\).

I treat the main case stated in the prompt, \(\hat\phi=\hat\theta_{\rm obs}\). If an additional posterior draw is used as \(\hat\phi\), its \(O_p(n^{-1/2})\) variation changes the \(O(1)\) constant unless the posterior-draw scheme is specified.

---

## 1. Observed/conditional factorization

Let \(R_i\) be the missingness pattern for unit \(i\), and write

\[
O_i=(R_i,Y_{i,{\rm obs}})
\]

for the observed part. Under MAR and ignorability, the true conditional law of the missing part given \(O_i\) is the model conditional law at \(\theta_0\):

\[
Y_{i,{\rm mis}}\mid O_i \sim q_{\theta_0,i}(\cdot\mid O_i),
\]

where

\[
q_{\theta,i}(y_{\rm mis}\mid O_i)
=
p_\theta(y_{\rm mis}\mid Y_{i,{\rm obs}},R_i).
\]

The complete likelihood factors as

\[
p_\theta(Y_i)
=
p_\theta(O_i)\,q_{\theta,i}(Y_{i,{\rm mis}}\mid O_i),
\]

so

\[
\ell_{\rm com}(\theta;Y)
=
\ell_{\rm obs}(\theta;O)
+
\sum_{i=1}^n \log q_{\theta,i}(Y_{i,{\rm mis}}\mid O_i).
\]

Define the conditional negative entropy term

\[
c_i(\theta)
:=
E_{\theta}\!\left[
\log q_{\theta,i}(Y_{i,{\rm mis}}\mid O_i)
\mid O_i
\right].
\]

Then, because imputations are drawn from the fitted law \(q_{\hat\theta_{\rm obs},i}\),

\[
\bar Q_\infty(\hat\theta_{\rm obs})
=
\ell_{\rm obs}(\hat\theta_{\rm obs})
+
\sum_{i=1}^n c_i(\hat\theta_{\rm obs}).
\]

Let

\[
C_n(\theta):=\sum_{i=1}^n c_i(\theta).
\]

---

## 2. The key nonzero term

We first compute

\[
A_n
:=
E\!\left[
\bar Q_\infty(\hat\theta_{\rm obs})
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right].
\]

Conditional on the observed data \(O=(O_1,\dots,O_n)\),

\[
\bar Q_\infty(\hat\theta_{\rm obs})
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
=
C_n(\hat\theta_{\rm obs})
-
\sum_{i=1}^n
\log q_{\hat\theta_{\rm obs},i}(Y_{i,{\rm mis}}\mid O_i).
\]

Taking the conditional expectation under the true data law \(P_{\theta_0}\),

\[
\begin{aligned}
E_{\theta_0}\!\left[
\bar Q_\infty(\hat\theta_{\rm obs})
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\mid O
\right]
&=
C_n(\hat\theta_{\rm obs})
-
\sum_{i=1}^n
E_{\theta_0}\!\left[
\log q_{\hat\theta_{\rm obs},i}(Y_{i,{\rm mis}}\mid O_i)
\mid O_i
\right] \\
&=
\{C_n(\hat\theta_{\rm obs})-C_n(\theta_0)\}
+
\sum_{i=1}^n
KL\!\left(
q_{\theta_0,i}(\cdot\mid O_i),
q_{\hat\theta_{\rm obs},i}(\cdot\mid O_i)
\right).
\end{aligned}
\]

Therefore

\[
A_n
=
\Delta_n
+
E\sum_{i=1}^n
KL\!\left(
q_{\theta_0,i},
q_{\hat\theta_{\rm obs},i}
\right),
\]

where the design-dependent entropy-bias term is

\[
\boxed{
\Delta_n
:=
E\!\left[
C_n(\hat\theta_{\rm obs})-C_n(\theta_0)
\right].
}
\]

Now use the standard LAN/quadratic expansion of KL divergence. Conditional on \(O_i\),

\[
KL(q_{\theta_0,i},q_{\theta,i})
=
\frac12
(\theta-\theta_0)^\top
I_{{\rm mis},i}(O_i)
(\theta-\theta_0)
+
o(\|\theta-\theta_0\|^2),
\]

where

\[
I_{{\rm mis},i}(O_i)
=
\operatorname{Var}_{\theta_0}\!\left[
\partial_\theta \log p_\theta(Y_i)\mid O_i
\right].
\]

Summing over \(i\),

\[
\sum_{i=1}^n I_{{\rm mis},i}(O_i)
=
I_{\rm mis\mid obs}+o_p(n).
\]

Also,

\[
\hat\theta_{\rm obs}-\theta_0
=
I_{\rm obs}^{-1}S_{\rm obs}(\theta_0)+o_p(n^{-1/2}),
\]

and

\[
\operatorname{Var}(\hat\theta_{\rm obs})
=
I_{\rm obs}^{-1}+o(n^{-1}).
\]

Hence

\[
E\sum_{i=1}^n
KL(q_{\theta_0,i},q_{\hat\theta_{\rm obs},i})
=
\frac12
\operatorname{tr}
\left(
I_{\rm obs}^{-1}I_{\rm mis\mid obs}
\right)
+
o(1)
=
\frac12 RIV+o(1).
\]

Thus

\[
\boxed{
E\!\left[
\bar Q_\infty(\hat\theta_{\rm obs})
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right]
=
\frac12 RIV+\Delta_n+o(1).
}
\]

This is generally **not zero**. It would be exactly zero if the averaging law were the true law \(q_{\theta_0}\), because then \(\bar Q_\infty\) would be the conditional expectation of \(\ell_{\rm com}\) given \(O\). But the averaging law is \(q_{\hat\theta_{\rm obs}}\), not \(q_{\theta_0}\), and the fitted-law KL term contributes \(\frac12RIV\) to first order.

---

## 3. Expected complete-data likelihood gain

Now compute

\[
B_n
:=
E\!\left[
\ell_{\rm com}(\hat\theta_{\rm com};Y)
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right].
\]

Use the standard likelihood quadratic expansion around \(\hat\theta_{\rm com}\):

\[
\ell_{\rm com}(\hat\theta_{\rm com})
-
\ell_{\rm com}(\hat\theta_{\rm obs})
=
\frac12
(\hat\theta_{\rm com}-\hat\theta_{\rm obs})^\top
I_{\rm com}
(\hat\theta_{\rm com}-\hat\theta_{\rm obs})
+
o_p(1).
\]

The complete and observed MLEs satisfy

\[
\hat\theta_{\rm com}-\theta_0
=
I_{\rm com}^{-1}S_{\rm com}(\theta_0)+o_p(n^{-1/2}),
\]

\[
\hat\theta_{\rm obs}-\theta_0
=
I_{\rm obs}^{-1}S_{\rm obs}(\theta_0)+o_p(n^{-1/2}).
\]

By the missing-information principle/Louis identity,

\[
S_{\rm obs}(\theta_0)
=
E_{\theta_0}\!\left[
S_{\rm com}(\theta_0)\mid O
\right],
\]

so

\[
\operatorname{Cov}(S_{\rm com},S_{\rm obs})=I_{\rm obs}.
\]

Therefore

\[
\operatorname{Var}(\hat\theta_{\rm com}-\hat\theta_{\rm obs})
=
I_{\rm obs}^{-1}-I_{\rm com}^{-1}+o(n^{-1}).
\]

Thus

\[
\begin{aligned}
B_n
&=
\frac12
\operatorname{tr}
\left[
I_{\rm com}
\left(
I_{\rm obs}^{-1}-I_{\rm com}^{-1}
\right)
\right]
+o(1)\\
&=
\frac12
\left\{
\operatorname{tr}(I_{\rm com}I_{\rm obs}^{-1})-k
\right\}
+o(1)\\
&=
\frac12
\operatorname{tr}(I_{\rm obs}^{-1}I_{\rm mis\mid obs})
+o(1)\\
&=
\boxed{\frac12 RIV+o(1)}.
\end{aligned}
\]

---

## 4. Main result for \(T\)

Recall

\[
T
=
\bar Q_\infty(\hat\theta_{\rm obs})
-
\ell_{\rm com}(\hat\theta_{\rm com};Y).
\]

Decompose:

\[
T
=
\left[
\bar Q_\infty(\hat\theta_{\rm obs})
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right]
-
\left[
\ell_{\rm com}(\hat\theta_{\rm com};Y)
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right].
\]

Taking expectations and using the two calculations above,

\[
E[T]
=
\left(
\frac12RIV+\Delta_n
\right)
-
\frac12RIV
+
o(1).
\]

Hence

\[
\boxed{
E[T]
=
\Delta_n+o(1),
}
\]

where

\[
\boxed{
\Delta_n
=
E\!\left[
C_n(\hat\theta_{\rm obs})-C_n(\theta_0)
\right]
}
\]

is the fitted-model conditional-entropy bias. Equivalently, since \(c_i(\theta)\) is minus a conditional entropy,

\[
\Delta_n
=
-
E\!\left[
H_{\hat\theta_{\rm obs}}(Y_{\rm mis}\mid Y_{\rm obs},R)
-
H_{\theta_0}(Y_{\rm mis}\mid Y_{\rm obs},R)
\right].
\]

So the \(RIV/2\) term from fitting the imputation law cancels the \(RIV/2\) complete-data maximization gain. What remains is the design/model-dependent entropy plug-in bias.

---

## 5. MCAR versus MAR

Let \(r\) index missingness patterns.

### MCAR

Under MCAR,

\[
P(R=r\mid Y)=\pi_r,
\]

so expectations are taken with respect to

\[
\pi_r\,p_{\theta_0,r}(y_{\rm obs})\,dy_{\rm obs}.
\]

Thus

\[
I_{\rm obs}^{\rm MCAR}
=
n\sum_r \pi_r
E_{\theta_0}
\left[
s_r(Y_{\rm obs})s_r(Y_{\rm obs})^\top
\right],
\]

and similarly for \(I_{\rm mis\mid obs}^{\rm MCAR}\). The main formula becomes

\[
\boxed{
E_{\rm MCAR}[T]
=
\Delta_{\rm MCAR}+o(1),
}
\]

where

\[
\Delta_{\rm MCAR}
=
E_{\rm MCAR}
\left[
C_n(\hat\theta_{\rm obs})-C_n(\theta_0)
\right].
\]

If the conditional entropy \(H_\theta(Y_{\rm mis}\mid Y_{\rm obs},R)\) is locally independent of \(\theta\), then \(\Delta_{\rm MCAR}=0\), and therefore

\[
E_{\rm MCAR}[T]=o(1).
\]

Example: multivariate normal with known covariance and unknown mean. The conditional covariance is fixed, so the conditional entropy does not depend on \(\mu\). Then \(\Delta_{\rm MCAR}=0\).

If covariance parameters are estimated, \(\Delta_{\rm MCAR}\) is generally nonzero.

For a multivariate normal,

\[
Y\sim N(\mu,\Sigma),
\]

the conditional law of \(Y_{\rm mis}\mid Y_{\rm obs}\) is normal with covariance

\[
\Sigma_{{\rm mis}\mid{\rm obs}}
=
\Sigma_{mm}-\Sigma_{mo}\Sigma_{oo}^{-1}\Sigma_{om}.
\]

Therefore

\[
c_i(\mu,\Sigma)
=
-\frac12
\left\{
d_{{\rm mis},i}\log(2\pi e)
+
\log |\Sigma_{{\rm mis}\mid{\rm obs},i}|
\right\}.
\]

So

\[
\Delta_{\rm MCAR}
=
-\frac12
E_{\rm MCAR}
\sum_{i=1}^n
\log
\frac{
|\hat\Sigma_{{\rm mis}\mid{\rm obs},i}|
}{
|\Sigma_{0,{\rm mis}\mid{\rm obs},i}|
}
+o(1).
\]

This depends on the missingness pattern probabilities and on the covariance-estimation bias.

### MAR

Under MAR,

\[
P(R=r\mid Y)=\psi_r(Y_{\rm obs}),
\]

so the observed-data expectation is taken with respect to

\[
\psi_r(y_{\rm obs})\,p_{\theta_0,r}(y_{\rm obs})\,dy_{\rm obs}.
\]

The same algebra holds, but both \(RIV\) and \(\Delta_n\) are now MAR-design dependent:

\[
\boxed{
E_{\rm MAR}[T]
=
\Delta_{\rm MAR}+o(1),
}
\]

with

\[
\Delta_{\rm MAR}
=
E_{\rm MAR}
\left[
C_n(\hat\theta_{\rm obs})-C_n(\theta_0)
\right].
\]

The difference from MCAR is not an additional universal \(RIV\) term. Rather, the entropy-bias term is evaluated under the MAR-weighted observed-data law. In particular, when missingness depends on observed values, \(\Delta_{\rm MAR}\) can contain extra covariance terms between the observed-data score and the derivative of the conditional entropy.

A useful delta-method expansion is the following. Let

\[
c(O_i;\theta)
=
E_\theta[
\log q_\theta(Y_{i,{\rm mis}}\mid O_i)\mid O_i],
\]

\[
a(O_i)=\partial_\theta c(O_i;\theta_0),
\qquad
B(O_i)=\partial_\theta^2 c(O_i;\theta_0),
\]

and let \(s_{\rm obs}(O_i)\) be the observed-data score. With per-observation observed information \(J_{\rm obs}=I_{\rm obs}/n\), and with MLE bias

\[
E(\hat\theta_{\rm obs}-\theta_0)=\frac{\beta}{n}+o(n^{-1}),
\]

one obtains

\[
\Delta
=
\bar a^\top \beta
+
\operatorname{tr}\!\left[
J_{\rm obs}^{-1}
E\{s_{\rm obs}(O_i)a(O_i)^\top\}
\right]
+
\frac12
\operatorname{tr}\!\left[
J_{\rm obs}^{-1}\bar B
\right],
\]

where \(\bar a=E[a(O_i)]\) and \(\bar B=E[B(O_i)]\). Under MCAR these expectations use \(\pi_r p_{\theta_0,r}\); under MAR they use \(\psi_r(y_{\rm obs})p_{\theta_0,r}\).

---

## 6. Final summary

\[
\boxed{
E\!\left[
\bar Q_\infty(\hat\theta_{\rm obs})
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right]
=
\frac12 RIV+\Delta_n+o(1).
}
\]

This expectation is generally **not zero**, because the imputation law is fitted at \(\hat\theta_{\rm obs}\), not at the true \(\theta_0\).

Also,

\[
\boxed{
E\!\left[
\ell_{\rm com}(\hat\theta_{\rm com};Y)
-
\ell_{\rm com}(\hat\theta_{\rm obs};Y)
\right]
=
\frac12 RIV+o(1).
}
\]

Therefore,

\[
\boxed{
E[T]
=
E\!\left[
\bar Q_\infty(\hat\theta_{\rm obs})
-
\ell_{\rm com}(\hat\theta_{\rm com};Y)
\right]
=
\Delta_n+o(1).
}
\]

The \(RIV/2\) terms cancel. The remaining leading term is the design-dependent fitted conditional-entropy bias \(\Delta_n\). Under MCAR, \(\Delta_n\) depends on pattern probabilities. Under MAR, it depends on the full MAR weighting mechanism through the observed-data law.
