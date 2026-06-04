# Layer-3 modeA response — model=gpt-5.5

Let

\[
A:=I_{\rm com},\qquad B:=I_{\rm obs},\qquad M:=I_{\rm mis}=A-B,
\]

all evaluated at \(\theta_0\). Thus \(A,B=O(n)\), \(A^{-1},B^{-1}=O(n^{-1})\), and \(M=O(n)\). Let

\[
J_o:=-\nabla^2 l_{\rm obs}(\theta_0)=B+O_p(n^{1/2})
\]

be the realized observed information. Write \(\delta:=\delta_{\rm obs}=\hat\theta_{\rm obs}-\theta_0=O_p(n^{-1/2})\). Also write the realized missing information

\[
M_R:=\nabla_\psi\nabla_\phi F(\theta_0,\theta_0)=M+O_p(n^{1/2}).
\]

I use \(G\) for the \(k\times k_0\) null tangent matrix, \(k_0=k-q_d\).

---

# 1. Local geometry of the MI objective

The MI objective is

\[
\bar Q(\theta)=l_{\rm obs}(\theta)+F(\theta,\hat\theta_{\rm obs}).
\]

We need its score and Hessian at \(\theta_0\).

## 1.1 Conditional-score identities for \(F\)

For each unit,

\[
F_i(\psi,\phi)=E_\phi\{\log p_\psi(Y_{\rm mis}\mid Y_{\rm obs})\}.
\]

The conditional score identity gives

\[
\nabla_\psi F(\phi,\phi)=0.
\]

Differentiating this identity with respect to \(\phi\) at \(\phi=\theta_0\),

\[
\nabla_{\psi\psi}^2F(\theta_0,\theta_0)+\nabla_{\psi\phi}^2F(\theta_0,\theta_0)=0.
\]

By (F2),

\[
\nabla_{\psi\phi}^2F(\theta_0,\theta_0)=M_R,
\]

so

\[
\nabla_{\psi\psi}^2F(\theta_0,\theta_0)=-M_R.
\]

Also, by (F1),

\[
\nabla_\psi F(\theta_0,\theta_0)=0.
\]

## 1.2 Score \(Z=\nabla \bar Q(\theta_0)\)

We have

\[
Z=\nabla l_{\rm obs}(\theta_0)+\nabla_\psi F(\theta_0,\hat\theta_{\rm obs})
=S+\nabla_\psi F(\theta_0,\theta_0+\delta).
\]

Taylor expand in the second argument:

\[
\nabla_\psi F(\theta_0,\theta_0+\delta)
=
\nabla_\psi F(\theta_0,\theta_0)
+
\nabla_{\psi\phi}^2F(\theta_0,\theta_0)\delta
+
O_p(n\|\delta\|^2).
\]

Because \(\|\delta\|=O_p(n^{-1/2})\),

\[
n\|\delta\|^2=O_p(1).
\]

Therefore

\[
\nabla_\psi F(\theta_0,\hat\theta_{\rm obs})
=
M_R\delta+O_p(1),
\]

and hence

\[
\boxed{
Z=S+M_R\delta+O_p(1).
}
\]

Now use the observed-score expansion for \(\hat\theta_{\rm obs}\):

\[
0=\nabla l_{\rm obs}(\hat\theta_{\rm obs})
=
S-J_o\delta+O_p(n\|\delta\|^2)
=
S-J_o\delta+O_p(1).
\]

Thus

\[
S=J_o\delta+O_p(1).
\]

Therefore

\[
Z=(J_o+M_R)\delta+O_p(1).
\]

Since \(J_o+M_R=A+O_p(n^{1/2})\),

\[
\boxed{
Z=A\delta+O_p(1).
}
\]

Equivalently, because \(\delta=B^{-1}S+O_p(n^{-1})\),

\[
\boxed{
Z=A B^{-1}S+O_p(1).
}
\]

Thus \(Z=O_p(n^{1/2})\).

## 1.3 Hessian \(J=-\nabla^2\bar Q(\theta_0)\)

We have

\[
-\nabla^2\bar Q(\theta_0)
=
-\nabla^2 l_{\rm obs}(\theta_0)
-
\nabla_{\psi\psi}^2F(\theta_0,\hat\theta_{\rm obs}).
\]

Taylor expand

\[
\nabla_{\psi\psi}^2F(\theta_0,\hat\theta_{\rm obs})
=
\nabla_{\psi\psi}^2F(\theta_0,\theta_0)+O_p(n\|\delta\|)
=
-M_R+O_p(n^{1/2}).
\]

Therefore

\[
J
=
J_o+M_R+O_p(n^{1/2})
=
A+O_p(n^{1/2}).
\]

So

\[
\boxed{
J=-\nabla^2\bar Q(\theta_0)=A+O_p(n^{1/2}).
}
\]

Moreover,

\[
Z=J\delta+O_p(1).
\]

## 1.4 Does \(\hat\psi\) equal \(\hat\theta_{\rm obs}\)?

Yes. In fact, \(\hat\theta_{\rm obs}\) is an exact stationary point of \(\bar Q\).

Indeed,

\[
\nabla \bar Q(\hat\theta_{\rm obs})
=
\nabla l_{\rm obs}(\hat\theta_{\rm obs})
+
\nabla_\psi F(\hat\theta_{\rm obs},\hat\theta_{\rm obs}).
\]

The first term is zero by definition of the observed-data MLE, and the second term is zero by the conditional-score identity. Hence

\[
\nabla \bar Q(\hat\theta_{\rm obs})=0.
\]

Moreover, for fixed \(\phi=\hat\theta_{\rm obs}\),

\[
F(\psi,\phi)
=
E_\phi\{\log p_\psi(Y_{\rm mis}\mid Y_{\rm obs})\}
\le
E_\phi\{\log p_\phi(Y_{\rm mis}\mid Y_{\rm obs})\}
=
F(\phi,\phi),
\]

because the difference is a conditional KL divergence. Also

\[
l_{\rm obs}(\psi)\le l_{\rm obs}(\hat\theta_{\rm obs}).
\]

Thus

\[
\bar Q(\psi)\le \bar Q(\hat\theta_{\rm obs}),
\]

so, under uniqueness,

\[
\boxed{
\hat\psi=\hat\theta_{\rm obs}.
}
\]

Locally,

\[
\hat\psi-\theta_0=J^{-1}Z+O_p(n^{-1})=\delta+O_p(n^{-1}).
\]

But globally, in this construction, the equality is exact.

## 1.5 Constrained maximizer and the projection metric

Let

\[
\theta=g(\gamma),\qquad \gamma=\gamma_0+\eta,
\]

so that

\[
g(\gamma_0+\eta)=\theta_0+G\eta+O(\|\eta\|^2).
\]

Since the maximizer is \(O_p(n^{-1/2})\) from \(\gamma_0\), the curvature term is \(O_p(n^{-1})\).

The local quadratic expansion of \(\bar Q\) is

\[
\bar Q(\theta_0+t)
=
\bar Q(\theta_0)+Z't-\frac12 t'Jt+O_p(n\|t\|^3).
\]

For \(t=G\eta+O(\|\eta\|^2)\),

\[
\bar Q(g(\gamma_0+\eta))
=
\bar Q(\theta_0)+Z'G\eta-\frac12\eta'G'JG\eta+O_p(n^{-1/2}).
\]

The first-order condition gives

\[
G'Z-G'JG\hat\eta=O_p(1).
\]

Because \(G'JG=O(n)\),

\[
\boxed{
\hat\eta=(G'JG)^{-1}G'Z+O_p(n^{-1}).
}
\]

Therefore

\[
\boxed{
g(\hat\gamma^*)-\theta_0
=
G(G'JG)^{-1}G'Z+O_p(n^{-1}).
}
\]

Since the unconstrained local maximizer is

\[
\hat\psi-\theta_0=J^{-1}Z+O_p(n^{-1}),
\]

the constrained displacement is

\[
G(G'JG)^{-1}G'J(\hat\psi-\theta_0)+O_p(n^{-1}).
\]

Thus the constrained maximizer is the projection of \(\hat\psi-\theta_0\) onto \(\operatorname{col}(G)\) in the \(J\)-metric. Since \(J=A+O_p(n^{1/2})\), the limiting metric is the complete-information metric \(I_{\rm com}\), not the observed-information metric \(I_{\rm obs}\).

So

\[
\boxed{
\text{The constrained maximizer projects in the } I_{\rm com}\text{ metric, not the }I_{\rm obs}\text{ metric.}
}
\]

---

# 2. Differential bias \(E[d_L-d_{\rm com}]\) at \(H_0\)

At \(H_0\), both the full and constrained maximizers are \(O_p(n^{-1/2})\) from \(\theta_0\). Use the quadratic expansion of \(\bar Q\).

## 2.1 Expansion of \(d_L\)

The unconstrained maximized increment is

\[
\bar Q(\hat\psi)-\bar Q(\theta_0)
=
\frac12 Z'J^{-1}Z+O_p(n^{-1/2}).
\]

The constrained increment is

\[
\bar Q(g(\hat\gamma^*))-\bar Q(\theta_0)
=
\frac12 Z'G(G'JG)^{-1}G'Z+O_p(n^{-1/2}).
\]

Therefore

\[
d_L
=
2\{\bar Q(\hat\psi)-\bar Q(g(\hat\gamma^*))\}
\]

satisfies

\[
d_L
=
Z'\left\{
J^{-1}-G(G'JG)^{-1}G'
\right\}Z
+
O_p(n^{-1/2}).
\]

Taking expectations, the Taylor remainder has expectation \(O(n^{-1})\), because the third central moments of the MLE displacement are \(O(n^{-2})\). Since \(J=A+O_p(n^{1/2})\),

\[
J^{-1}-G(G'JG)^{-1}G'
=
A^{-1}-G(G'AG)^{-1}G'
+
O_p(n^{-3/2}).
\]

Also

\[
Z=A\delta+O_p(1),
\]

and

\[
E(\delta\delta')=B^{-1}+O(n^{-2}).
\]

Thus

\[
E[d_L]
=
\operatorname{tr}
\left[
\left\{
A^{-1}-G(G'AG)^{-1}G'
\right\}
A B^{-1}A
\right]
+
O(n^{-1}).
\]

Therefore

\[
\boxed{
E[d_L]
=
\operatorname{tr}
\left[
\left\{
I_{\rm com}^{-1}
-
G(G'I_{\rm com}G)^{-1}G'
\right\}
I_{\rm com}I_{\rm obs}^{-1}I_{\rm com}
\right]
+
O(n^{-1}).
}
\]

## 2.2 Expansion of \(d_{\rm com}\)

For complete data, Wilks’ theorem gives, under \(H_0\),

\[
\boxed{
E[d_{\rm com}]=q_d+O(n^{-1}).
}
\]

Equivalently, the complete-data LR has local quadratic form

\[
d_{\rm com}
=
S_{\rm com}'
\left\{
A^{-1}-G(G'AG)^{-1}G'
\right\}
S_{\rm com}
+
O_p(n^{-1/2}),
\]

with \(E(S_{\rm com}S_{\rm com}')=A\), so

\[
E[d_{\rm com}]
=
\operatorname{tr}
\left[
\left\{
A^{-1}-G(G'AG)^{-1}G'
\right\}A
\right]
+
O(n^{-1})
=
k-k_0+O(n^{-1})
=
q_d+O(n^{-1}).
\]

## 2.3 Differential bias

Subtracting,

\[
E[d_L-d_{\rm com}]
=
\operatorname{tr}
\left[
\left\{
A^{-1}-G(G'AG)^{-1}G'
\right\}
A B^{-1}A
\right]
-q_d
+
O(n^{-1}).
\]

Thus

\[
\boxed{
E[d_L-d_{\rm com}]
=
\operatorname{tr}
\left[
\left\{
I_{\rm com}^{-1}
-
G(G'I_{\rm com}G)^{-1}G'
\right\}
I_{\rm com}I_{\rm obs}^{-1}I_{\rm com}
\right]
-q_d
+
O(n^{-1}).
}
\]

A useful equivalent form is obtained using \(A=B+M\). Since

\[
\operatorname{tr}(B^{-1}A)=k+\operatorname{tr}(B^{-1}M),
\]

and

\[
G'AB^{-1}AG
=
G'AG+G'AB^{-1}MG,
\]

we get

\[
\boxed{
E[d_L-d_{\rm com}]
=
\operatorname{tr}(B^{-1}M)
-
\operatorname{tr}
\left[
(G'AG)^{-1}G'AB^{-1}MG
\right]
+
O(n^{-1}).
}
\]

In original notation,

\[
\boxed{
E[d_L-d_{\rm com}]
=
\operatorname{tr}(I_{\rm obs}^{-1}I_{\rm mis})
-
\operatorname{tr}
\left[
(G'I_{\rm com}G)^{-1}
G'I_{\rm com}I_{\rm obs}^{-1}I_{\rm mis}G
\right]
+
O(n^{-1}).
}
\]

---

# 3. Comparison with \(\operatorname{tr}(\mathrm{RIV}_f)-\operatorname{tr}(\mathrm{RIV}_0)\)

The self-contained traces are

\[
\operatorname{tr}(\mathrm{RIV}_f)
=
\operatorname{tr}(B^{-1}M),
\]

and

\[
\operatorname{tr}(\mathrm{RIV}_0)
=
\operatorname{tr}\{(G'BG)^{-1}G'MG\}.
\]

The formula from Task 2 instead involves

\[
\operatorname{tr}\{(G'AG)^{-1}G'AB^{-1}MG\}.
\]

So, in general,

\[
\boxed{
E[d_L-d_{\rm com}]
\neq
\operatorname{tr}(\mathrm{RIV}_f)-\operatorname{tr}(\mathrm{RIV}_0).
}
\]

The two coincide only under a special invariance condition.

## 3.1 Whitening by the complete information

Let

\[
C:=A^{-1/2}BA^{-1/2}.
\]

Since \(B\le A\),

\[
0<C\le I.
\]

Let

\[
U:=A^{1/2}G.
\]

Let \(W\) be an orthonormal basis for \(\operatorname{col}(U)\), so \(W'W=I_{k_0}\). Define

\[
P:=WW',
\]

the Euclidean projection onto \(A^{1/2}\operatorname{col}(G)\).

In these coordinates, the Task 2 bias becomes

\[
\boxed{
E[d_L-d_{\rm com}]
=
\operatorname{tr}\{(I-P)(C^{-1}-I)\}
+
O(n^{-1}).
}
\]

The self-contained trace difference becomes

\[
\operatorname{tr}(\mathrm{RIV}_f)-\operatorname{tr}(\mathrm{RIV}_0)
=
\operatorname{tr}(C^{-1}-I)
-
\left[
\operatorname{tr}\{(W'CW)^{-1}\}-k_0
\right].
\]

Therefore

\[
\operatorname{tr}(\mathrm{RIV}_f)-\operatorname{tr}(\mathrm{RIV}_0)
=
\operatorname{tr}(C^{-1})
-
\operatorname{tr}\{(W'CW)^{-1}\}
-q_d.
\]

Meanwhile,

\[
E[d_L-d_{\rm com}]
=
\operatorname{tr}(C^{-1})
-
\operatorname{tr}(W'C^{-1}W)
-q_d
+
O(n^{-1}).
\]

Hence

\[
E[d_L-d_{\rm com}]
-
\{\operatorname{tr}(\mathrm{RIV}_f)-\operatorname{tr}(\mathrm{RIV}_0)\}
\]

equals

\[
\operatorname{tr}\{(W'CW)^{-1}\}
-
\operatorname{tr}(W'C^{-1}W)
+
O(n^{-1}).
\]

## 3.2 Sign of the discrepancy

For a positive definite matrix \(C\),

\[
W'C^{-1}W-(W'CW)^{-1}\succeq 0.
\]

This follows from the Schur complement. Complete \(W\) to an orthogonal matrix \((W,V)\) and write

\[
C=
\begin{pmatrix}
C_{11} & C_{12}\\
C_{21} & C_{22}
\end{pmatrix}
\]

in the \((W,V)\) basis. Then

\[
W'CW=C_{11},
\]

while

\[
W'C^{-1}W
=
(C_{11}-C_{12}C_{22}^{-1}C_{21})^{-1}.
\]

Because

\[
C_{11}-C_{12}C_{22}^{-1}C_{21}\preceq C_{11},
\]

inverting reverses the Loewner order, so

\[
W'C^{-1}W\succeq C_{11}^{-1}=(W'CW)^{-1}.
\]

Therefore

\[
\operatorname{tr}\{(W'CW)^{-1}\}
-
\operatorname{tr}(W'C^{-1}W)
\le 0.
\]

Thus

\[
\boxed{
E[d_L-d_{\rm com}]
\le
\operatorname{tr}(\mathrm{RIV}_f)-\operatorname{tr}(\mathrm{RIV}_0)
+
O(n^{-1}).
}
\]

Equivalently, the self-contained RIV-trace difference generally overstates the actual MI deviance differential bias.

## 3.3 Equality condition

Equality holds iff

\[
W'C^{-1}W=(W'CW)^{-1},
\]

which by the Schur-complement argument holds iff

\[
C_{12}=0.
\]

That is, \(\operatorname{col}(W)\) must be invariant under \(C\). Returning to the original coordinates, this condition is

\[
\boxed{
A^{-1}B\,\operatorname{col}(G)\subseteq \operatorname{col}(G).
}
\]

Equivalently,

\[
\boxed{
I_{\rm com}^{-1}I_{\rm obs}\operatorname{col}(G)
\subseteq
\operatorname{col}(G).
}
\]

Since \(M=A-B\), this is also equivalent to

\[
\boxed{
I_{\rm com}^{-1}I_{\rm mis}\operatorname{col}(G)
\subseteq
\operatorname{col}(G).
}
\]

Geometrically: the null tangent space must reduce the observed/complete-information operator. Equivalently, the null tangent space and its \(I_{\rm com}\)-orthogonal complement must also be \(I_{\rm obs}\)-orthogonal.

---

# 4. Noise of the paired differential \(D=T_f-T_0\)

Recall

\[
D=T_f-T_0=\frac{d_L-d_{\rm com}}2.
\]

Although each level \(T_f,T_0\) has \(O_p(n^{1/2})\) noise, their difference is much smaller at \(H_0\).

## 4.1 Decompose the two levels at \(H_0\)

At \(H_0\),

\[
\theta_0=g(\gamma_0).
\]

Write

\[
B_R(\theta_0)
:=
\bar Q(\theta_0)-l_{\rm com}(\theta_0)
=
l_{\rm obs}(\theta_0)+F(\theta_0,\hat\theta_{\rm obs})-l_{\rm com}(\theta_0).
\]

Then

\[
T_f
=
B_R(\theta_0)
+
\{\bar Q(\hat\psi)-\bar Q(\theta_0)\}
-
\{l_{\rm com}(\hat\theta_{\rm com})-l_{\rm com}(\theta_0)\},
\]

and

\[
T_0
=
B_R(\theta_0)
+
\{\bar Q(g(\hat\gamma^*))-\bar Q(\theta_0)\}
-
\{l_{\rm com}(g(\hat\gamma_{\rm com}))-l_{\rm com}(\theta_0)\}.
\]

Thus the common base term \(B_R(\theta_0)\) cancels exactly in

\[
D=T_f-T_0.
\]

## 4.2 Which \(O_p(n^{1/2})\) pieces cancel?

Expand \(B_R(\theta_0)\) in the imputation parameter:

\[
F(\theta_0,\hat\theta_{\rm obs})
=
F(\theta_0,\theta_0)
+
\alpha_R'\delta
+
\frac12\delta'H_R\delta
+
O_p(n\|\delta\|^3).
\]

Since \(\delta=O_p(n^{-1/2})\),

\[
O_p(n\|\delta\|^3)=O_p(n^{-1/2}).
\]

Therefore

\[
B_R(\theta_0)
=
\underbrace{
l_{\rm obs}(\theta_0)+F(\theta_0,\theta_0)-l_{\rm com}(\theta_0)
}_{O_p(n^{1/2})}
+
\underbrace{\alpha_R'\delta}_{O_p(n^{1/2})}
+
\underbrace{\frac12\delta'H_R\delta}_{O_p(1)}
+
O_p(n^{-1/2}).
\]

The two \(O_p(n^{1/2})\) pieces are:

1. the conditional log-likelihood residual

   \[
   l_{\rm obs}(\theta_0)+F(\theta_0,\theta_0)-l_{\rm com}(\theta_0),
   \]

   which is a sum of conditional mean-zero terms;

2. the MAR/imputation-parameter linear term

   \[
   \alpha_R'\delta,
   \]

   because \(\alpha_R=O_p(n)\) and \(\delta=O_p(n^{-1/2})\).

Both are identical in \(T_f\) and \(T_0\). Therefore both cancel exactly in \(D\).

The remaining terms are likelihood-ratio increments, which are \(O_p(1)\).

## 4.3 Order of \(sd(D)\) at \(H_0\)

Using the quadratic expansions,

\[
d_L
=
Z'\left\{
A^{-1}-G(G'AG)^{-1}G'
\right\}Z
+
O_p(n^{-1/2}),
\]

and

\[
d_{\rm com}
=
S_{\rm com}'
\left\{
A^{-1}-G(G'AG)^{-1}G'
\right\}
S_{\rm com}
+
O_p(n^{-1/2}).
\]

Here \(Z=O_p(n^{1/2})\), \(S_{\rm com}=O_p(n^{1/2})\), and the middle matrix is \(O(n^{-1})\). Therefore both quadratic forms are \(O_p(1)\). Hence

\[
D=\frac12(d_L-d_{\rm com})=O_p(1),
\]

and

\[
\boxed{
sd(D)=O(1)\qquad\text{at }H_0.
}
\]

Generically the variance has a nonzero finite limit, so \(sd(D)=\Theta(1)\), except in degenerate cases such as no missing information in the tested directions.

## 4.4 Local alternatives

Now take

\[
\theta_n=g(\gamma_0)+\frac{h}{\sqrt n},
\qquad h\notin \operatorname{col}(G).
\]

The full and constrained pseudo-truths are separated by \(O(n^{-1/2})\). Choose \(\theta_n\) as the common reference. Then

\[
T_f
=
B_R(\theta_n)
+
O_p(1),
\]

and

\[
T_0
=
B_R(\theta_n)
+
O_p(1).
\]

The common base

\[
B_R(\theta_n)=\bar Q(\theta_n)-l_{\rm com}(\theta_n)
\]

again has \(O_p(n^{1/2})\) noise, but it cancels in the difference. The remaining increments are noncentral LR-type quantities with noncentrality \(O(1)\). Hence

\[
\boxed{
sd(D)=O(1)
\qquad
\text{under }n^{-1/2}\text{-local alternatives.}
}
\]

Again, generically \(sd(D)=\Theta(1)\).

## 4.5 Fixed alternatives

Under a fixed alternative, the full and null pseudo-truths are \(O(1)\) apart. Let those population points be \(\bar\theta_f\) and \(\bar\theta_0\). Then the relevant contrast is no longer a local \(O(n^{-1/2})\) contrast. The difference between the imputed-data contrast and the complete-data contrast is now a sum of \(n\) nondegenerate per-unit residuals.

Schematically,

\[
D
=
\sum_{i=1}^n
\left[
E\{r_i(\bar\theta_f,\bar\theta_0)\mid Y_{{\rm obs},i}\}
-
r_i(\bar\theta_f,\bar\theta_0)
\right]
+
O_p(1),
\]

where \(r_i(\bar\theta_f,\bar\theta_0)\) is the complete-data log-likelihood contrast between two \(O(1)\)-separated parameter values. The summands have variance \(O(1)\), so the sum has variance \(O(n)\). Therefore

\[
\boxed{
sd(D)=O(n^{1/2})
\qquad
\text{under fixed alternatives.}
}
\]

Generically,

\[
sd(D)=\Theta(n^{1/2}).
\]

This is the same order as in ordinary non-nested likelihood comparison: the paired cancellation removes common level noise only when the two fitted parameter values are \(O(n^{-1/2})\) apart.

---

# 5. The \((A)+(C)\) differential

The full-model level theorem says

\[
E[T_f]
=
\frac12\operatorname{tr}(B^{-1}M)
+
(A)+(C)
+
O(n^{-1}),
\]

with

\[
(A)+(C)
=
\alpha'E\delta+\frac12\operatorname{tr}(H_\phi B^{-1})+O(n^{-1}).
\]

The important question is whether these \((A)+(C)\) terms survive in the paired difference \(T_f-T_0\).

## 5.1 Expansion of the pure \((A)+(C)\) terms

At \(H_0\),

\[
F(\theta_0,\hat\theta_{\rm obs})
=
F(\theta_0,\theta_0)
+
\alpha_R'\delta
+
\frac12\delta'H_R\delta
+
O_p(n^{-1/2}).
\]

The pure imputation-parameter contribution is therefore

\[
\alpha_R'\delta+\frac12\delta'H_R\delta.
\]

This same term appears in both \(T_f\) and \(T_0\), because both levels use the same \(F\) and the same \(\hat\theta_{\rm obs}\). Hence

\[
\boxed{
\text{The leading \((A)+(C)\) terms cancel exactly in }T_f-T_0.
}
\]

Thus, at \(H_0\),

\[
\boxed{
(A+C)_f-(A+C)_0=O(n^{-1})
\quad\text{in expectation, and zero through }O(1).
}
\]

More explicitly,

\[
E[T_f]
=
(A+C)
+
\frac12\operatorname{tr}(B^{-1}M)
+
O(n^{-1}),
\]

whereas

\[
E[T_0]
=
(A+C)
+
\frac12
\operatorname{tr}\left[
(G'AG)^{-1}G'AB^{-1}MG
\right]
+
O(n^{-1}).
\]

Therefore

\[
E[T_f-T_0]
=
\frac12
\left\{
\operatorname{tr}(B^{-1}M)
-
\operatorname{tr}\left[
(G'AG)^{-1}G'AB^{-1}MG
\right]
\right\}
+
O(n^{-1}),
\]

which is exactly half the Task 2 formula. The \((A)+(C)\) part is not responsible for the differential bias at \(H_0\). The differential bias comes from the LR geometry, specifically from projecting in the \(I_{\rm com}\) metric.

## 5.2 What does not cancel?

The cross term

\[
t'M_R\delta
\]

appears when expanding

\[
F(\theta_0+t,\theta_0+\delta).
\]

Indeed,

\[
F(\theta_0+t,\theta_0+\delta)
=
F(\theta_0,\theta_0)
+
\alpha_R'\delta
+
\frac12\delta'H_R\delta
+
t'M_R\delta
-\frac12t'M_Rt
+\cdots.
\]

The pure terms

\[
\alpha_R'\delta,\qquad \frac12\delta'H_R\delta
\]

cancel between the two levels. The cross term \(t'M_R\delta\) does not cancel, because \(t\) differs between the full and constrained fits. But this term is part of the likelihood-ratio/RIV contribution, not part of the level-theorem \((A)+(C)\) contribution.

## 5.3 Local alternatives

Under the local alternatives

\[
\theta_n=g(\gamma_0)+\frac{h}{\sqrt n},
\]

take \(\theta_n\) as the common expansion point. Then

\[
F(\theta_n,\hat\theta_{\rm obs})
=
F(\theta_n,\theta_n)
+
\alpha_R(\theta_n)'\delta_n
+
\frac12\delta_n'H_R(\theta_n)\delta_n
+
O_p(n^{-1/2}),
\]

where

\[
\delta_n=\hat\theta_{\rm obs}-\theta_n=O_p(n^{-1/2}).
\]

The same pure \((A)+(C)\) term appears in both levels, so it cancels through \(O(1)\). If one expands the two levels about their own local pseudo-truths, those pseudo-truths differ by \(O(n^{-1/2})\), so smoothness gives

\[
\Delta\alpha=O(n^{1/2}),\qquad \Delta H=O(n^{1/2}).
\]

Therefore the expected \((A)+(C)\) differential is only

\[
\Delta\alpha' E\delta_n
+
\frac12\operatorname{tr}(\Delta H\,B^{-1})
=
O(n^{1/2})O(n^{-1})
+
O(n^{1/2})O(n^{-1})
=
O(n^{-1/2}).
\]

Thus,

\[
\boxed{
(A+C)_f-(A+C)_0=o(1)
\quad\text{under }n^{-1/2}\text{-local alternatives.}
}
\]

The paired LR part remains \(O_p(1)\), but the level-theorem \((A)+(C)\) differential does not contribute an \(O(1)\) bias.

## 5.4 Fixed alternatives

Under a fixed alternative, the full and null pseudo-truths are \(O(1)\) apart. Let them be \(\bar\theta_f\) and \(\bar\theta_0\), and let the imputation probability limit be \(\bar\phi\). Define

\[
a_R(\psi,\bar\phi):=\nabla_\phi F(\psi,\bar\phi),
\qquad
H_R(\psi,\bar\phi):=\nabla_{\phi\phi}^2F(\psi,\bar\phi).
\]

The \((A)+(C)\)-type difference between the two levels contains

\[
\{a_R(\bar\theta_f,\bar\phi)-a_R(\bar\theta_0,\bar\phi)\}'(\hat\theta_{\rm obs}-\bar\phi)
\]

and

\[
\frac12
(\hat\theta_{\rm obs}-\bar\phi)'
\{H_R(\bar\theta_f,\bar\phi)-H_R(\bar\theta_0,\bar\phi)\}
(\hat\theta_{\rm obs}-\bar\phi).
\]

Because \(\bar\theta_f-\bar\theta_0=O(1)\),

\[
a_R(\bar\theta_f,\bar\phi)-a_R(\bar\theta_0,\bar\phi)=O_p(n),
\]

and

\[
H_R(\bar\theta_f,\bar\phi)-H_R(\bar\theta_0,\bar\phi)=O_p(n).
\]

Also

\[
\hat\theta_{\rm obs}-\bar\phi=O_p(n^{-1/2}).
\]

Therefore the linear term is

\[
O_p(n)O_p(n^{-1/2})=O_p(n^{1/2}),
\]

while the quadratic term is

\[
O_p(n)O_p(n^{-1})=O_p(1).
\]

In expectation, the linear term contributes \(O(1)\), because

\[
E(\hat\theta_{\rm obs}-\bar\phi)=O(n^{-1}),
\]

and the quadratic term also contributes \(O(1)\). Therefore

\[
\boxed{
(A+C)_f-(A+C)_0=O(1)
\quad\text{in expectation under fixed alternatives,}
}
\]

but its realized centered contribution can be \(O_p(n^{1/2})\). This is one source of the \(O(n^{1/2})\) noise of \(D\) under fixed alternatives.

---

# Summary of the main conclusions

1. The MI score and Hessian at \(\theta_0\) are

   \[
   Z=S+M_R\delta_{\rm obs}+O_p(1)=I_{\rm com}\delta_{\rm obs}+O_p(1),
   \]

   and

   \[
   J=-\nabla^2\bar Q(\theta_0)=I_{\rm com}+O_p(n^{1/2}).
   \]

2. The unconstrained MI maximizer equals the observed-data MLE:

   \[
   \hat\psi=\hat\theta_{\rm obs}.
   \]

3. The constrained MI maximizer is the \(I_{\rm com}\)-metric projection of \(\hat\theta_{\rm obs}\) onto the null tangent space.

4. At \(H_0\),

   \[
   E[d_L-d_{\rm com}]
   =
   \operatorname{tr}(I_{\rm obs}^{-1}I_{\rm mis})
   -
   \operatorname{tr}
   \left[
   (G'I_{\rm com}G)^{-1}
   G'I_{\rm com}I_{\rm obs}^{-1}I_{\rm mis}G
   \right]
   +
   O(n^{-1}).
   \]

5. This is generally not equal to

   \[
   \operatorname{tr}(\mathrm{RIV}_f)-\operatorname{tr}(\mathrm{RIV}_0).
   \]

   Equality holds iff

   \[
   I_{\rm com}^{-1}I_{\rm obs}\operatorname{col}(G)
   \subseteq
   \operatorname{col}(G).
   \]

   The discrepancy has a definite sign:

   \[
   E[d_L-d_{\rm com}]
   \le
   \operatorname{tr}(\mathrm{RIV}_f)-\operatorname{tr}(\mathrm{RIV}_0)
   +
   O(n^{-1}).
   \]

6. Although \(T_f\) and \(T_0\) individually have \(O_p(n^{1/2})\) noise, their paired difference satisfies

   \[
   sd(D)=O(1)
   \]

   at \(H_0\) and under \(n^{-1/2}\)-local alternatives.

7. Under fixed alternatives,

   \[
   sd(D)=O(n^{1/2}).
   \]

8. The level-theorem \((A)+(C)\) terms cancel through \(O(1)\) at \(H_0\) and under local alternatives. They are not responsible for the \(O(1)\) differential bias at \(H_0\). Under fixed alternatives, their expected difference is \(O(1)\), while their realized centered contribution can be \(O_p(n^{1/2})\).
