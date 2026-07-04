# Layer-3 modeB response — model=gpt-5.5-pro

## Verdict table

| claim | verdict | one-line reason |
|---|---:|---|
| **C1** | **SUSTAIN** | The identity is exact; block-inverse algebra gives \(K_{MM}=\hat V^{-1}\) and kills the linear cross term. |
| **C2** | **SUSTAIN** | Schur derivative and second derivative signs are correct; Schur complement is concave, not convex. The \(\mu\)-missing-info identity is exact. |
| **C3** | **ESCALATE** | The second-order cancellation algebra is right for local regular draws, but “exact under MCAR” and “cross-wander vanishes” need asymptotic/local/block-orthogonality qualifications. |
| **C4** | **SUSTAIN, qualified** | Master formula follows from C1–C3 at leading order; the \(\mu\)-block contraction is exact when \(\operatorname{Var}(\mu^\ast)=[I_{\rm obs}^{-1}]_{\mu\mu}\). Watch the sign convention for IMB. |
| **C5** | **SUSTAIN** | Laplace has \(b_\Sigma=0\) up to exponentially small PD-truncation effects; the surviving term is exactly the \(\mu\)-block known-scale anchor plus MAR imbalance. |
| **C6** | **ESCALATE / partly refute** | \(p+2\) relative to divisor-\(n\) MLE is correct and persistent “IW shape” is not available for regular local draws; however the scalar-deflation explanation is numerically inconsistent with the stated factor unless the deflated arm did something else. |
| **C7** | **ESCALATE** | Complete-data bootstrap identity is exact; missing-data “\(\mu\)-part cancellation” is plausible via raw second moments, but the remaining Cox–Snell bias can be \(O(1)\) after summing and is not proven to be \(\le .01\). |
| **C8** | **SUSTAIN, qualified** | MAR imbalance has a closed-form population expression and is zero under MCAR; it depends on the covariance of \(\Sigma^\ast\), so “universal” only among engines with the same asymptotic \(\Sigma\)-covariance. |
| **C9** | **REFUTE as stated** | \(\Xi=o(1/n)\) is neither necessary nor sufficient unless one also assumes local draws and zero/controlled IMB; the exact clean condition is aggregate predictive second-moment matching from C1. |

---

# 1. C1–C4 algebra audit

## C1: exact identity

Order variables as \((M,O)\). Let

\[
\hat\Sigma=
\begin{pmatrix}
\hat\Sigma_{MM}&\hat\Sigma_{MO}\\
\hat\Sigma_{OM}&\hat\Sigma_{OO}
\end{pmatrix},\qquad
\hat B=\hat\Sigma_{MO}\hat\Sigma_{OO}^{-1},
\]

\[
\hat V=\hat\Sigma_{MM}-\hat\Sigma_{MO}\hat\Sigma_{OO}^{-1}\hat\Sigma_{OM}.
\]

The block inverse is

\[
\hat\Sigma^{-1}
=
\begin{pmatrix}
\hat V^{-1} & -\hat V^{-1}\hat B\\
-\hat B^\top \hat V^{-1}
&
\hat\Sigma_{OO}^{-1}+\hat B^\top\hat V^{-1}\hat B
\end{pmatrix}.
\]

So indeed

\[
[\hat\Sigma^{-1}]_{MM}=\hat V^{-1}.
\]

For fixed observed \(y_O\), the fitted conditional mean is

\[
\hat m=\hat\mu_M+\hat B(y_O-\hat\mu_O).
\]

Let

\[
r_O=y_O-\hat\mu_O,\qquad r_M=\hat m-\hat\mu_M=\hat B r_O.
\]

Then

\[
[\hat\Sigma^{-1}r]_M
=
\hat V^{-1}r_M-\hat V^{-1}\hat B r_O
=
\hat V^{-1}(\hat B r_O-\hat B r_O)=0.
\]

Now let the imputation engine draw \(\phi\), with conditional missing mean \(m(\phi)=\hat m+d\) and conditional variance \(V(\phi)\). The complete-data quadratic at \(\hat\theta\) is

\[
(y-\hat\mu)^\top \hat\Sigma^{-1}(y-\hat\mu).
\]

Taking expectation over \(Y_M\mid y_O,\phi\), the difference from the fitted plug-in conditional distribution is

\[
d^\top \hat V^{-1}d
+
\operatorname{tr}\{\hat V^{-1}(V(\phi)-\hat V)\},
\]

because the linear term vanishes by the calculation above. Therefore

\[
q_i(\phi)-q_i(\hat\theta)
=
-\frac12
\left[
d_i^\top\hat V_i^{-1}d_i+
\operatorname{tr}\{\hat V_i^{-1}(V_i(\phi)-\hat V_i)\}
\right].
\]

So C1 is exact.

Equivalently, if

\[
M_{2,i}
=
\mathbb E_\phi\left[V_i(\phi)+d_i d_i^\top\right]
\]

is the engine’s imputation-predictive second moment about the fitted conditional mean, then

\[
D
=
-\frac12\sum_i
\operatorname{tr}
\left[
\hat V_i^{-1}(M_{2,i}-\hat V_i)
\right].
\]

That is the cleanest exact characterization.

---

## C2: Schur derivatives and concavity

Let \(A=\hat\Sigma_{OO}\), \(E=\hat\Sigma_{MO}\), \(B=EA^{-1}\), and perturb \(\Sigma\mapsto \hat\Sigma+t\Delta\). Write

\[
\dot B(\Delta)
=
(\Delta_{MO}-B\Delta_{OO})A^{-1}.
\]

The Schur complement is

\[
V(\Sigma)=\Sigma_{MM}-\Sigma_{MO}\Sigma_{OO}^{-1}\Sigma_{OM}.
\]

First derivative:

\[
V'[\Delta]
=
\Delta_{MM}
-\Delta_{MO}A^{-1}\hat\Sigma_{OM}
-\hat\Sigma_{MO}A^{-1}\Delta_{OM}
+\hat\Sigma_{MO}A^{-1}\Delta_{OO}A^{-1}\hat\Sigma_{OM}.
\]

Since \(B=\hat\Sigma_{MO}A^{-1}\), this is

\[
V'[\Delta]
=
\Delta_{MM}
-\Delta_{MO}B^\top
-B\Delta_{OM}
+B\Delta_{OO}B^\top.
\]

With \(C=[\,I,\,-B\,]\),

\[
C\Delta C^\top
=
\Delta_{MM}
-\Delta_{MO}B^\top
-B\Delta_{OM}
+B\Delta_{OO}B^\top.
\]

Thus

\[
V'[\Delta]=C\Delta C^\top.
\]

Second derivative:

\[
V''[\Delta,\Delta]
=
-2\,\dot B(\Delta)A\dot B(\Delta)^\top
\preceq 0.
\]

So the Schur complement is matrix-concave in \(\Sigma\). Therefore a mean-centered covariance draw satisfies, by Jensen,

\[
\mathbb E[V(\Sigma^\ast)]\preceq V(\mathbb E\Sigma^\ast)=\hat V.
\]

So the round-1 conjecture of Jensen inflation of the Schur complement had the sign wrong.

Also,

\[
C\hat\Sigma C^\top
=
\hat\Sigma_{MM}
-B\hat\Sigma_{OM}
-\hat\Sigma_{MO}B^\top
+B\hat\Sigma_{OO}B^\top
=
\hat V.
\]

Finally, for one row,

\[
I_{\rm com,\mu\mu}^{(i)}=\hat\Sigma^{-1},
\qquad
I_{\rm obs,\mu\mu}^{(i)}
=
P_O^\top \hat\Sigma_{OO}^{-1}P_O.
\]

Using the block inverse above,

\[
I_{\rm com,\mu\mu}^{(i)}-I_{\rm obs,\mu\mu}^{(i)}
=
C_i^\top \hat V_i^{-1}C_i.
\]

Summing,

\[
\sum_i C_i^\top \hat V_i^{-1}C_i
=
[I_{\rm mis\mid obs}]_{\mu\mu}.
\]

So C2 is sustained.

---

## C3: second-order expansion and cancellation

Let

\[
\delta_\mu=\mu^\ast-\hat\mu,\qquad
\Delta=\Sigma^\ast-\hat\Sigma.
\]

To first order,

\[
d_i
=
C_i\delta_\mu+\dot B_i(\Delta)r_{O,i}
+O(\|\delta\|^2).
\]

Also,

\[
V_i(\Sigma^\ast)-\hat V_i
=
C_i\Delta C_i^\top
-\dot B_i(\Delta)\hat\Sigma_{OO,i}\dot B_i(\Delta)^\top
+O(\|\Delta\|^3),
\]

because \(V''/2=-\dot B\hat\Sigma_{OO}\dot B^\top\).

Plugging into C1 and taking draw expectation gives, up to \(o(n^{-1})\) per row,

\[
\begin{aligned}
\mathbb E_\phi[q_i(\phi)-q_i(\hat\theta)]
=
-\frac12\Big[
&
\operatorname{tr}\{\hat V_i^{-1}C_i b_\Sigma C_i^\top\}
\\
&+
\operatorname{tr}\{\hat V_i^{-1}C_i\operatorname{Var}(\mu^\ast) C_i^\top\}
\\
&+
\operatorname{tr}\left\{
H_i\left(r_{O,i}r_{O,i}^\top-\hat\Sigma_{OO,i}\right)
\right\}
\\
&+
2\,\mathbb E\{\delta_\mu^\top C_i^\top \hat V_i^{-1}\dot B_i(\Delta)r_{O,i}\}
\Big],
\end{aligned}
\]

where

\[
H_i=\mathbb E_\phi[\dot B_i(\Delta)^\top \hat V_i^{-1}\dot B_i(\Delta)].
\]

The cancellation is visible in the third line:

- the mean-wander from \(\Sigma\) contributes  
  \[
  +\operatorname{tr}(H_i r_{O,i}r_{O,i}^\top),
  \]
- the Schur-concavity term contributes  
  \[
  -\operatorname{tr}(H_i\hat\Sigma_{OO,i}).
  \]

Thus, within a pattern,

\[
\sum_{i\in{\rm pat}}
\operatorname{tr}\{H_{\rm pat}(r_{O,i}r_{O,i}^\top-\hat\Sigma_{OO})\}
\]

is the leftover imbalance term.

Under MCAR, at the population level,

\[
\mathbb E[r_Or_O^\top\mid{\rm pat}]=\Sigma_{OO},
\]

so this term vanishes asymptotically. Under MAR it need not vanish, because the pattern-conditional distribution of \(Y_O\) is tilted.

### Qualification

The algebra is correct, but the wording “cancel exactly under MCAR” is too strong finite-sample language. At finite \(n\),

\[
\sum_{i\in{\rm pat}}r_{O,i}r_{O,i}^\top-n_{\rm pat}\hat\Sigma_{OO}
\]

is not exactly zero. Under MCAR it is \(O_p(n^{1/2})\), while \(H_i=O(n^{-1})\), so the contribution is \(O_p(n^{-1/2})\) and vanishes. That is asymptotic exactness, not finite-sample exactness.

The \(\mu\Sigma\) cross term vanishes for E1 if the Laplace covariance is block diagonal between \(\mu\) and \(\Sigma\). It also vanishes to leading order for regular posterior/bootstrap laws under block-orthogonality. But this is an assumption. It is not a purely algebraic identity for every possible draw law.

### Order bookkeeping

For regular local draws,

\[
\delta=O_p(n^{-1/2}).
\]

Per-row absolute third-order Taylor remainder is \(O_p(n^{-3/2})\). Summed over \(n\) rows, that is \(O_p(n^{-1/2})\), hence negligible.

For Laplace/posterior/bootstrap regular laws,

\[
\mathbb E[\delta^{\otimes 3}]=O(n^{-2}),
\]

so signed cubic terms contribute \(n\cdot O(n^{-2})=O(n^{-1})\). Hence no persistent skew/shape term exists for those regular local engines.

But this conclusion requires locality/Lindeberg-type control. A contrived rare-large-jump engine can violate it.

---

## C4: master formula and \(\mu\)-block contraction

Ignoring the cross term under the orthogonality condition above, and grouping the imbalance contribution, the leading expansion is

\[
D
=
-\frac12\sum_i
\operatorname{tr}\left[
\hat V_i^{-1}C_i
\{b_\Sigma+\operatorname{Var}(\mu^\ast)\}
C_i^\top
\right]
-\mathrm{IMB}
+o(1),
\]

with

\[
\Xi=b_\Sigma+\operatorname{Var}(\mu^\ast).
\]

The \(\mu\)-wander part contracts as

\[
\sum_i
\operatorname{tr}
\left[
\hat V_i^{-1}C_i\operatorname{Var}(\mu^\ast)C_i^\top
\right]
=
\operatorname{tr}
\left[
\operatorname{Var}(\mu^\ast)
\sum_i C_i^\top\hat V_i^{-1}C_i
\right].
\]

Using C2,

\[
\sum_i C_i^\top\hat V_i^{-1}C_i
=
[I_{\rm mis\mid obs}]_{\mu\mu}.
\]

If

\[
\operatorname{Var}(\mu^\ast)=[I_{\rm obs}^{-1}]_{\mu\mu},
\]

then

\[
\sum_i
\operatorname{tr}
\left[
\hat V_i^{-1}C_i\operatorname{Var}(\mu^\ast)C_i^\top
\right]
=
\operatorname{tr}(\mathrm{RIV}_{\mu\mu}).
\]

So the contribution is

\[
-\frac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu}).
\]

This part is exact conditional on that variance equality.

---

# 2. C5 and C6

## C5: Laplace E1

For E1,

\[
\theta^\ast\sim N(\hat\theta,I_{\rm obs}^{-1}).
\]

Ignoring exponentially small PD-truncation effects,

\[
b_\Sigma=\mathbb E[\Sigma^\ast-\hat\Sigma]=0.
\]

Therefore

\[
D_{\rm E1}
=
-\frac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})
-\mathrm{IMB}
+o(1).
\]

Numerically,

\[
-\frac12
\frac{\operatorname{tr}(\mathrm{RIV}_{\mu\mu})}
{\operatorname{tr}(\mathrm{RIV})}
=
-\frac12\frac{1.14}{5.63}
\approx -0.101.
\]

That matches the \(\mu\)-only rows. Adding the MAR imbalance of roughly \(-0.005\) to \(-0.006\) in normalized \(D\)-units gives the claimed asymptotic neighborhood \(-0.106\) to \(-0.107\).

### Sign convention note

C4 defines

\[
D=\cdots-\mathrm{IMB}.
\]

But the evidence table’s “imbalance” column appears to report the contribution to \(D\), i.e. \(-\mathrm{IMB}\). Thus the table values \(-0.0049,-0.0065\) correspond to \(\mathrm{IMB}>0\). This should be cleaned up in the manuscript.

---

## C6: Jeffreys-IW posterior

### \(p+2\) versus \(p+1\)

The specified prior is

\[
\pi(\mu,\Sigma)\propto |\Sigma|^{-(p+1)/2}.
\]

For complete data,

\[
\Sigma\mid Y
\sim
\operatorname{IW}(n-1,SS),
\]

where

\[
SS=\sum_i(y_i-\bar y)(y_i-\bar y)^\top.
\]

Under the standard inverse-Wishart parameterization,

\[
\mathbb E[\Sigma\mid Y]
=
\frac{SS}{(n-1)-p-1}
=
\frac{SS}{n-p-2}.
\]

The divisor-\(n\) MLE is

\[
\hat\Sigma_{\rm ML}=SS/n.
\]

Therefore

\[
\mathbb E[\Sigma\mid Y]
=
\frac{n}{n-p-2}\hat\Sigma_{\rm ML}
=
\left(1+\frac{p+2}{n}+O(n^{-2})\right)\hat\Sigma_{\rm ML}.
\]

So relative to the divisor-\(n\) MLE the constant is \(p+2\), not \(p+1\).

Relative to the divisor-\((n-1)\) sample covariance \(S=SS/(n-1)\),

\[
\mathbb E[\Sigma\mid Y]
=
\frac{n-1}{n-p-2}S
=
\left(1+\frac{p+1}{n}+O(n^{-2})\right)S.
\]

So both constants appear, depending on the reference estimator. C6 is correct relative to the MLE.

### Persistent shape/skew term?

For the IW posterior,

\[
\Sigma^\ast-\hat\Sigma=O_p(n^{-1/2}),
\]

\[
\mathbb E[(\Sigma^\ast-\hat\Sigma)^{\otimes 3}]=O(n^{-2}).
\]

Thus a cubic contribution is \(O(n^{-2})\) per row and \(O(n^{-1})\) after summing. Fourth-order terms are even smaller after summing. Therefore, for regular IW posterior draws, there is no persistent “shape” term once first-order bias and second-order covariance effects are accounted for.

That part of C6 is sustained.

---

## Scalar-deflated arm: quantitative problem

This is the strongest algebraic problem in C6.

Let

\[
K(A)=\sum_i \operatorname{tr}(\hat V_i^{-1}C_iAC_i^\top).
\]

For proportional \(A=\hat\Sigma\),

\[
C_i\hat\Sigma C_i^\top=\hat V_i,
\]

so

\[
K(\hat\Sigma)=\sum_i |M_i|=n_{\rm mis}.
\]

The normalized \(b_\Sigma\)-contraction is

\[
D_b
=
-\frac{1}{2\,\operatorname{tr}(\mathrm{RIV})}K(b_\Sigma).
\]

At \(N=200\), the table gives

\[
D_b\approx -0.649.
\]

Now suppose every covariance draw is scalar-deflated by

\[
c=\frac{n-p-2}{n-1}.
\]

For \(n=200,p=4\),

\[
c=\frac{194}{199}\approx 0.97487,
\qquad
1-c\approx 0.02513.
\]

The new covariance mean bias is

\[
b_{\Sigma,c}
=
c(\hat\Sigma+b_\Sigma)-\hat\Sigma
=
c b_\Sigma+(c-1)\hat\Sigma.
\]

Therefore

\[
D_{b,c}
=
cD_b
-\frac{1}{2T}(c-1)n_{\rm mis},
\qquad
T=\operatorname{tr}(\mathrm{RIV}).
\]

Using \(T=5.63\) and \(n_{\rm mis}\approx0.648n=129.6\),

\[
-\frac{1}{2T}(c-1)n_{\rm mis}
=
\frac{(1-c)n_{\rm mis}}{2T}
\approx
\frac{0.02513\cdot129.6}{11.26}
\approx
0.289.
\]

So

\[
D_{b,c}
\approx
0.9749(-0.649)+0.289
\approx
-0.344.
\]

Adding the \(\mu\)-wander and MAR imbalance gives roughly

\[
-0.344-0.101-0.006\approx -0.451.
\]

But the round-1 scalar-deflated arm reportedly landed at \(-0.244\).

Even using the stronger centering factor \(c=(n-p-2)/n=194/200=0.97\), one gets roughly

\[
D_{b,c}\approx -0.285,
\]

and total

\[
-0.285-0.101-0.006\approx -0.392.
\]

So the stated scalar factor cannot, by this contraction algebra, move E2 from about \(-0.78\) to \(-0.244\). To land at \(-0.244\), the scalar operation would need to remove an effective normalized \(b_\Sigma\)-contraction of about \(0.51\), corresponding to an effective scalar subtraction closer to \(9/n\), not \(5/n\) or \(6/n\).

Therefore the explanation

> scalar deflation removed only the isotropic part and left \(\approx -0.12\) anisotropic residual

is not established by the stated algebra and appears numerically inconsistent with the stated deflation factor, unless the round-1 “deflated arm” involved additional operations beyond scalar multiplication of \(\Sigma^\ast\).

This subclaim should be treated as refuted or at least escalated until the actual transformed \(b_\Sigma\) contraction is reported.

---

## E2 matrix-recentering residual

The matrix-recentered E2 values are

\[
-0.1497\quad(N=200),
\qquad
-0.1380\quad(N=1000),
\]

whereas E1 full is roughly

\[
-0.1236,\quad -0.1220.
\]

The residuals are about

\[
-0.026,\quad -0.016.
\]

Those are not huge, but they are not negligible relative to the claimed \(\le .01\)-scale finite-\(n\) residue. Since regular IW shape terms should vanish as \(O(n^{-1})\) after summing, the residual should be explicitly decomposed before claiming collapse onto E1. Possible explanations include:

1. imperfect recentering target,
2. remaining nonlinear bias in \(V(\Sigma)\) or \(B(\Sigma)\),
3. finite parameter-draw Monte Carlo mean shift,
4. different \(\Sigma\)-covariance-induced IMB,
5. a genuine Cox–Snell-type \(O(1/n)\) parameter bias with a non-negligible constant.

But it should not be labeled “IW shape” if the draw law is regular/local.

---

# 3. C7: bootstrap EMB audit

## Complete-data identity

For complete data, let

\[
\hat\mu=\bar y,\qquad
\hat\Sigma=\frac1n\sum_j(y_j-\bar y)(y_j-\bar y)^\top.
\]

For a bootstrap resample with weights \(W_j\),

\[
\tilde\mu=\frac1n\sum_j W_j y_j,
\]

\[
\tilde\Sigma
=
\frac1n\sum_j W_j(y_j-\tilde\mu)(y_j-\tilde\mu)^\top.
\]

Then exactly,

\[
\tilde\Sigma
+
(\tilde\mu-\hat\mu)(\tilde\mu-\hat\mu)^\top
=
\frac1n\sum_j W_j(y_j-\hat\mu)(y_j-\hat\mu)^\top.
\]

Taking bootstrap expectation,

\[
\mathbb E^\ast[\tilde\Sigma]
+
\mathbb E^\ast[(\tilde\mu-\hat\mu)(\tilde\mu-\hat\mu)^\top]
=
\hat\Sigma.
\]

Thus

\[
b_\Sigma+\operatorname{Var}^\ast(\tilde\mu)=0
\]

up to the distinction between centered and uncentered variance, which is irrelevant at \(O(n^{-1})\). So the complete-data C7 identity is exact.

## Missing-data case

For missing data, the exact complete-data identity no longer holds because \(\tilde\Sigma\) is the observed-data EM MLE in the bootstrap sample, not a direct empirical covariance around \(\tilde\mu\).

However, the right way to understand the claimed cancellation is through the raw second moment parameter

\[
\Psi=\Sigma+\mu\mu^\top.
\]

To leading order,

\[
b_\Sigma+\operatorname{Var}^\ast(\tilde\mu)
=
\mathbb E^\ast[\tilde\Psi-\hat\Psi]
+o(n^{-1}).
\]

So the \(\mu\)-part cancellation means:

- covariance-MLE bias contains a negative “estimated mean” part,
- adding \(\operatorname{Var}^\ast(\tilde\mu)\) cancels that part,
- the leftover is the bootstrap bias of the raw second-moment estimator.

That is plausibly the “non-\(\mu\) Cox–Snell curvature” piece.

But that leftover is generally \(O(1/n)\) per covariance cell. After contraction over \(n\) rows, it can produce an \(O(1)\) limiting contribution to \(D\). There is no general theorem here forcing it to vanish.

The evidence is also not decisive:

\[
\text{E3 master } -0.0430\quad(N=200),
\]

\[
\text{E3 master } -0.0373\quad(N=1000).
\]

That does not show clear \(1/n\) decay. It is compatible with a persistent normalized floor around \(0.03\)–\(0.04\), though the \(N=1000\) SE is large. The Amelia \(N=2000\) value \(-0.019\) is suggestive but not enough to prove a \(\le .01\) floor.

So C7’s complete-data identity is sustained, but the missing-data convergence claim should be weakened unless the Cox–Snell bias constant is derived or directly estimated across larger \(n\).

---

# 4. C8: closed-form MAR imbalance

Let \(R_j=1\) denote that \(X_j\) is missing, with

\[
\Pr(R_1=1\mid X_3)=g(X_3),
\qquad
\Pr(R_2=1\mid X_4)=g(X_4),
\]

\[
g(x)=\Phi(a+bx),\qquad a=-0.5,\quad b=0.4.
\]

Let a pattern be \(m=(m_1,m_2)\in\{0,1\}^2\), where \(m_j=1\) means \(X_j\) is missing. Then

\[
M(m)=\{j\le2:m_j=1\},
\]

\[
O(m)=\{3,4\}\cup\{j\le2:m_j=0\}.
\]

Only patterns with \(M(m)\neq\varnothing\) contribute to \(D\).

## 4.1 Population IMB formula

For a given engine \(e\), define

\[
H_{m,e}
=
\mathbb E_e[
\dot B_m(\Delta)^\top
V_m^{-1}
\dot B_m(\Delta)
],
\]

where \(\Delta=\Sigma^\ast-\hat\Sigma\). Since \(\Delta=O_p(n^{-1/2})\),

\[
H_{m,e}=O(n^{-1}).
\]

Let

\[
\bar H_{m,e}=nH_{m,e}.
\]

Let

\[
A_m
=
\mathbb E[X_{O(m)}X_{O(m)}^\top\mid m]
-
\Sigma_{O(m)O(m)}.
\]

Then the large-\(n\) MAR imbalance contribution is

\[
D_{\rm IMB,e}
=
-\frac12
\sum_{m:M(m)\neq\varnothing}
\pi_m
\operatorname{tr}(\bar H_{m,e}A_m),
\]

where

\[
\pi_m=\Pr(R_1=m_1,R_2=m_2).
\]

Equivalently, if one defines

\[
\mathrm{IMB}_e
=
\frac12
\sum_m
\pi_m
\operatorname{tr}(\bar H_{m,e}A_m),
\]

then

\[
D_{\rm IMB,e}=-\mathrm{IMB}_e.
\]

This resolves the sign convention issue.

The only missing ingredients are \(A_m\) and \(\bar H_{m,e}\). The \(A_m\) have closed forms under the probit-MAR design.

---

## 4.2 Pattern-conditional moments

Let

\[
Z=(X_3,X_4)^\top.
\]

Then

\[
Z\sim N(0,A),
\qquad
A=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix},
\qquad
\rho=0.5.
\]

Let \(U_1,U_2\stackrel{\rm iid}{\sim}N(0,1)\), independent of \(Z\), and define

\[
L_j=U_j-bZ_j.
\]

Then

\[
R_j=1
\iff
U_j\le a+bZ_j
\iff
L_j\le a.
\]

The latent vector \(L=(L_1,L_2)\) is normal with

\[
\operatorname{Var}(L)=I_2+b^2A
=
\begin{pmatrix}
1+b^2&b^2\rho\\
b^2\rho&1+b^2
\end{pmatrix}.
\]

Let

\[
\tau^2=1+b^2=1.16,
\]

\[
r_L=\frac{b^2\rho}{1+b^2}
=
\frac{0.16\cdot0.5}{1.16}
\approx 0.06897,
\]

\[
t=\frac{a}{\tau}
\approx -0.46424.
\]

For pattern \(m\), define signs

\[
s_j=
\begin{cases}
+1,&m_j=1,\\
-1,&m_j=0.
\end{cases}
\]

Let

\[
W_j=s_jL_j/\tau.
\]

Then \(W=(W_1,W_2)\) is standard bivariate normal with correlation

\[
r_m=s_1s_2r_L.
\]

The pattern event is

\[
W_1\le s_1t,\qquad W_2\le s_2t.
\]

Thus

\[
\pi_m
=
\Phi_2(s_1t,s_2t;r_m).
\]

Numerically, approximately,

\[
\Pr(R_j=1)=\Phi(t)\approx0.321,
\]

and because \(r_L\) is small positive,

\[
\pi_{11}\approx 0.112,\qquad
\pi_{10}=\pi_{01}\approx0.209,\qquad
\pi_{00}\approx0.470.
\]

Now compute \(Z\mid m\). Since \((Z,L)\) is jointly normal,

\[
\mathbb E[Z\mid L]=K L,
\]

where

\[
K=\operatorname{Cov}(Z,L)\operatorname{Var}(L)^{-1}.
\]

Here

\[
\operatorname{Cov}(Z,L)=-bA,
\]

so

\[
K=-bA(I+b^2A)^{-1}.
\]

Let

\[
S_Z=A-K\operatorname{Var}(L)K^\top.
\]

Then

\[
\mathbb E[Z\mid m]
=
K\,\mathbb E[L\mid m],
\]

\[
\mathbb E[ZZ^\top\mid m]
=
S_Z+K\,\mathbb E[LL^\top\mid m]K^\top.
\]

The truncated moments of \(L\mid m\) come from the bivariate truncated normal \(W\mid W\le u_m\), where

\[
u_m=(s_1t,s_2t).
\]

If

\[
P_m=\Phi_2(u_m;r_m),
\]

then for \(W\sim N(0,R_m)\),

\[
R_m=
\begin{pmatrix}
1&r_m\\
r_m&1
\end{pmatrix},
\]

the Tallis formulas give

\[
\mathbb E[W\mid W\le u_m]
=
-R_m\nabla_{u}\log P_m,
\]

and

\[
\mathbb E[WW^\top\mid W\le u_m]
=
R_m+2R_m\{\nabla_{R_m}\log P_m\}R_m.
\]

Then

\[
\mathbb E[L\mid m]
=
\tau\,\operatorname{diag}(s_1,s_2)
\mathbb E[W\mid W\le u_m],
\]

\[
\mathbb E[LL^\top\mid m]
=
\tau^2
\operatorname{diag}(s_1,s_2)
\mathbb E[WW^\top\mid W\le u_m]
\operatorname{diag}(s_1,s_2).
\]

That gives \(\mathbb E[Z]\) and \(\mathbb E[ZZ^\top]\) under every missingness pattern.

---

## 4.3 Adding \(X_1,X_2\)

Let

\[
X_A=(X_1,X_2)^\top.
\]

The conditional law of \(X_A\mid Z\) is

\[
X_A\mid Z\sim N(\Lambda Z,\Omega),
\]

where

\[
\Lambda=\Sigma_{A Z}\Sigma_{ZZ}^{-1}.
\]

For the supplied \(\Sigma_0\),

\[
\Lambda
=
\begin{pmatrix}
0.4&-0.2\\
-0.2&0.4
\end{pmatrix},
\]

and

\[
\Omega
=
\Sigma_{AA}-\Lambda\Sigma_{ZZ}\Lambda^\top
=
\begin{pmatrix}
0.88&0.66\\
0.66&0.88
\end{pmatrix}.
\]

Therefore, for each pattern \(m\),

\[
\mathbb E[X_A\mid m]
=
\Lambda\mathbb E[Z\mid m],
\]

\[
\mathbb E[X_AZ^\top\mid m]
=
\Lambda\mathbb E[ZZ^\top\mid m],
\]

\[
\mathbb E[X_AX_A^\top\mid m]
=
\Omega+\Lambda\mathbb E[ZZ^\top\mid m]\Lambda^\top.
\]

Assemble the full \(4\times4\) second moment

\[
T_m=\mathbb E[XX^\top\mid m],
\]

then take the observed block

\[
T_{m,OO}.
\]

Finally,

\[
A_m=T_{m,OO}-\Sigma_{OO}.
\]

This is the closed-form pattern-conditional moment needed for IMB.

---

## 4.4 Engine covariance factor

For each pattern \(m\),

\[
\dot B_m(\Delta)
=
(\Delta_{MO}-B_m\Delta_{OO})\Sigma_{OO}^{-1}.
\]

Let

\[
Z_\Sigma=\sqrt n(\Sigma^\ast-\hat\Sigma-b_\Sigma).
\]

For regular E1/E2/E3 engines,

\[
Z_\Sigma\Rightarrow N(0,\Omega_{\Sigma,e}).
\]

Then

\[
\bar H_{m,e}
=
\mathbb E
\left[
\dot B_m(Z_\Sigma)^\top
V_m^{-1}
\dot B_m(Z_\Sigma)
\right].
\]

Equivalently, if \(\operatorname{vec}\dot B_m=L_m\operatorname{vech}Z_\Sigma\), then

\[
(\bar H_{m,e})_{ab}
=
\sum_{u,v\in M(m)}
(V_m^{-1})_{uv}
\,L_{m,ua}^\top
\Omega_{\Sigma,e}
L_{m,vb}.
\]

This shows precisely why IMB depends on the covariance of \(\Sigma^\ast\), not on \(b_\Sigma\).

Thus:

- E1 and E2 have the same leading IMB if their asymptotic \(\Sigma\)-covariances agree.
- Matrix recentering changes \(b_\Sigma\) but not \(\Omega_{\Sigma,e}\), so it does not remove IMB.
- A \(\mu\)-only engine has no \(\Sigma\)-covariance and hence no IMB.
- FITTED has no parameter covariance and hence no IMB.
- Scalar deflation changes \(\Omega_{\Sigma,e}\) by \(1+O(1/n)\), so leading IMB is unchanged.

Under MCAR, \(A_m=0\) for every pattern, so IMB is zero at population level. The observed MCAR table values near \(0.0003\) are consistent with this.

---

# 5. C9 attack: \(\Xi=o(1/n)\) is not the right standalone condition

C9 says that the fitted-baseline deviance-bias theorem holds for engines with

\[
\Xi=b_\Sigma+\operatorname{Var}(\mu^\ast)=o(1/n)
\]

per cell.

That condition is neither necessary nor sufficient as stated.

## 5.1 Not sufficient under MAR

Construct an engine that fixes \(\mu^\ast=\hat\mu\) and draws only

\[
\Sigma^\ast=\hat\Sigma+n^{-1/2}Z,
\qquad
\mathbb E[Z]=0,
\]

with regular local covariance matching E1.

Then

\[
b_\Sigma=0,\qquad
\operatorname{Var}(\mu^\ast)=0,
\]

so

\[
\Xi=0.
\]

But under MAR, the covariance of \(\Sigma^\ast\) creates the imbalance term,

\[
D=-\mathrm{IMB}+o(1),
\]

which is generally nonzero. This is exactly the E1 \(\Sigma\)-only mechanism.

So \(\Xi=o(1/n)\) is not sufficient unless one also assumes MCAR or explicitly requires the covariance-induced imbalance term to vanish.

## 5.2 Not necessary

Let

\[
K_n(A)=\sum_i \operatorname{tr}(\hat V_i^{-1}C_iAC_i^\top).
\]

Choose a nonzero symmetric matrix \(A\) such that

\[
K_n(A)=0.
\]

This is always possible if indefinite \(A\) is allowed, because \(K_n(\cdot)\) is one scalar linear functional on a 10-dimensional covariance-matrix space.

Now define a deterministic engine

\[
\mu^\ast=\hat\mu,\qquad
\Sigma^\ast=\hat\Sigma+\frac{A}{n}.
\]

Then

\[
\Xi=\frac{A}{n},
\]

which is not \(o(1/n)\), but

\[
D
=
-\frac12K_n(A/n)+o(1)
=
o(1).
\]

So \(\Xi=o(1/n)\) is not necessary. The necessary leading condition is not \(\Xi=o(1/n)\), but rather that its contraction through the missingness operator vanish.

## 5.3 Nonlocal draw counterexample

Even with \(\Xi=0\), persistent shape effects can be manufactured if locality is dropped.

Example: with probability \(1-2/n\), set \(\Sigma^\ast=\hat\Sigma\); with probability \(1/n\), set \(\Sigma^\ast=A\); with probability \(1/n\), set \(\Sigma^\ast=2\hat\Sigma-A\), choosing \(A\) so both matrices are positive definite. Then

\[
\mathbb E[\Sigma^\ast]=\hat\Sigma,
\]

so \(b_\Sigma=0\), and with \(\mu\) fixed,

\[
\Xi=0.
\]

But each rare large jump changes the summed complete-data \(Q\) by \(O(n)\), and it occurs with probability \(O(1/n)\), so it contributes \(O(1)\) to \(D\).

This violates the C3 order argument because the engine is not local:

\[
\mathbb E\|\Sigma^\ast-\hat\Sigma\|^3=O(1/n),
\]

not \(O(n^{-3/2})\).

So the manuscript should state a local-draw/Lindeberg condition if it wants to exclude persistent shape terms.

## 5.4 Cleaner condition

The exact C1 condition is:

\[
D=o(1)
\iff
\sum_i
\operatorname{tr}
\left[
\hat V_i^{-1}(M_{2,i}-\hat V_i)
\right]
=o(1),
\]

where

\[
M_{2,i}
=
\mathbb E_\phi[V_i(\phi)+d_id_i^\top].
\]

That is the clean necessary and sufficient condition.

For regular local engines, this becomes the leading condition

\[
\sum_i
\operatorname{tr}
\left[
\hat V_i^{-1}C_i\Xi C_i^\top
\right]
+
2\,\mathrm{IMB}
=
o(1).
\]

Under MCAR, \(\mathrm{IMB}=0\), and a sufficient condition is indeed

\[
\Xi=o(1/n).
\]

But under MAR, \(\Xi=o(1/n)\) alone is insufficient.

Also, “genuine Bayesian posterior draws have \(\Xi\succ0\) by construction” is too strong. A prior can induce negative \(b_\Sigma\) relative to the MLE large enough to offset or exceed \(\operatorname{Var}(\mu^\ast)\) in some directions. Posterior predictive overdispersion relative to the posterior mean parameter is real, but \(\Xi\) is measured relative to the observed-data MLE plug-in, so its sign is prior-dependent through \(b_\Sigma\).

---

# 6. Evidence table issues the interpretation glosses over

1. **IMB sign convention is inconsistent.**  
   C4 uses \(D=\cdots-\mathrm{IMB}\), but C8 reports measured IMB values as negative. The table’s “imbalance” column appears to be the contribution to \(D\), i.e. \(-\mathrm{IMB}\).

2. **E1 full at \(N=1000\) is more negative than the claimed asymptote.**  
   The table gives \(-0.1220\), while the analytic asymptote is about \(-0.107\). The decomposition attributes much of this to finite parameter-draw “b-shift.” That is plausible, but then the table is not a clean engine-expectation table despite “exact-identity evaluation.”

3. **MCAR E1 \(\Sigma\)-only is not zero in the table.**  
   It is \(-0.0160\) at \(N=200\), \(-0.0137\) at \(N=1000\). The decomposition says this is matched finite-\(n\)/parameter-MC residue, not population IMB. Fine, but it should be separated from the asymptotic claim.

4. **Scalar-deflated E2 arm is quantitatively inconsistent.**  
   The stated scalar factor should not move E2 from \(-0.78\) to \(-0.244\) given the measured \(b_\Sigma\)-contraction \(-0.649\). Algebra predicts a much more negative value unless additional transformations occurred.

5. **E2 matrix-recentered residual remains noticeable.**  
   \(-0.150\) vs E1 \(-0.124\) at \(N=200\), and \(-0.138\) vs \(-0.122\) at \(N=1000\). This may be finite-\(n\), but it is not yet demonstrated to vanish at the claimed rate.

6. **E3 master does not clearly shrink.**  
   \(-0.0430\) at \(N=200\), \(-0.0373\) at \(N=1000\). This is consistent with a persistent Cox–Snell floor unless further evidence is supplied.

7. **MCAR E3 full \(-0.0455\) is not close to zero.**  
   If EMB is claimed to be second-moment matched to FITTED under MCAR, this value needs explanation as finite-\(n\) Cox–Snell bias or bootstrap implementation residue.

8. **“Engine-universal IMB” needs qualification.**  
   It is universal only for engines with the same leading \(\Sigma\)-draw covariance. It vanishes for FITTED and \(\mu\)-only engines, and changes if the covariance of \(\Sigma^\ast\) is deliberately altered.

---

# Overall verdict

The core derivation C1–C5 largely survives adversarial audit:

- C1 exact identity is correct.
- C2 Schur derivative and concavity sign are correct.
- C3 cancellation mechanism is correct at leading order for regular local parameter draws.
- C4 master formula is correct with a clear sign convention for IMB.
- C5 explains E1 convincingly.

C6 and C7 need tightening:

- The \(p+2\) IW baseline is correct.
- Persistent IW skew/shape is not available for regular local posterior draws.
- But the scalar-deflation account is algebraically inconsistent with the stated deflation factor and measured \(b_\Sigma\)-contraction.
- E2 recentring and E3 EMB residuals need a Cox–Snell or finite-\(n\) decomposition before claiming they vanish to \(\le .01\).

C8 is real: MAR imbalance need not vanish, has a closed-form population expression under this probit design, and is zero under MCAR. But its sign convention and “universality” should be stated carefully.

C9 should be rewritten. The manuscript should not use \(\Xi=o(1/n)\) as the standalone scope condition. The clean condition is exact predictive second-moment matching:

\[
\sum_i
\operatorname{tr}
\left[
\hat V_i^{-1}(M_{2,i}-\hat V_i)
\right]
=o(1).
\]

For local regular engines this reduces to a contracted \(\Xi\) condition plus the IMB term, not merely \(\Xi=o(1/n)\).

So: the main E1/E2 mechanism survives, including the \(\mu\)-block discount and the absence of persistent IW shape. But the scalar-deflation explanation, EMB floor claim, and C9 scope statement need revision before inclusion in a derivation manuscript.
