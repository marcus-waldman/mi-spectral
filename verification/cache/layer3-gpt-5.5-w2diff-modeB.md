# Layer-3 modeB response — model=gpt-5.5

Let

\[
A=I_{\rm obs},\qquad M=I_{\rm mis},\qquad C=I_{\rm com}=A+M,
\]

all of order \(n\). Let \(Q(\theta)=\bar Q(\theta)=\ell_{\rm obs}(\theta)+F(\theta,\hat\theta_{\rm obs})\), and let \(L_c(\theta)=\ell_{\rm com}(\theta)\). For the null tangent space write \(\mathcal T=\operatorname{col}(G)\), and define the \(C\)-orthogonal projection

\[
P_C=G(G'CG)^{-1}G'C,\qquad R_C=I-P_C.
\]

For a model \(m\), its “level” discrepancy is

\[
T_m=Q(\hat\theta_m)-L_c(\tilde\theta_m),
\]

where \(\hat\theta_m\) maximizes \(Q\) over the model and \(\tilde\theta_m\) maximizes \(L_c\). With the usual LR convention,

\[
D=\frac{d_L-d_{\rm com}}2=T_f-T_0.
\]

Below, “\(O_p(n^{-1/2})\)” for parameter displacements means the usual MLE scale.

---

## 1. Attack on C3: do the linear terms fail to cancel?

### Strong attack

One might argue:

- \(T_f\) and \(T_0\) are evaluated at different fitted points.
- The gradient of the level contrast \(Q-L_c\) at \(\theta_0\) is \(O_p(\sqrt n)\).
- Since \(\hat\theta_f-\hat\theta_0=O_p(n^{-1/2})\), the contraction is \(O_p(1)\), but if the gradients themselves are evaluated at different fitted points, perhaps their difference is \(O_p(\sqrt n)\), producing an uncancelled \(O_p(\sqrt n)\) term.
- Worse, the \(F\)-expansion contains \(\alpha_R=\nabla_\phi F(\theta_0,\theta_0)=O(n)\), so perhaps \(\alpha_R'(\hat\theta_f-\hat\theta_0)=O_p(\sqrt n)\).

That is the planted objection. The last step is the error.

### Explicit expansion

Write \(\hat\theta_{\rm obs}=\theta_0+\delta\), with

\[
\delta=A^{-1}S+O_p(n^{-1})=O_p(n^{-1/2}).
\]

For a fitted point \(\theta_0+a\), with \(a=O_p(n^{-1/2})\), expand \(F\) in both arguments:

\[
F(\theta_0+a,\theta_0+\delta)
=
F_{00}
+\alpha_R'\delta
+\frac12\delta'H_R\delta
+a'J_R\delta
-\frac12 a'K_R a
+O_p(n^{-1/2}),
\]

where

\[
J_R=F_{\psi\phi}(\theta_0,\theta_0)=O_p(n),\qquad 
K_R=-F_{\psi\psi}(\theta_0,\theta_0)=O_p(n),
\]

with means \(I_{\rm mis}\). Crucially:

\[
F_\psi(\theta_0,\theta_0)=0
\]

by F1, so there is no term \(\alpha_R'a\). The \(\alpha_R\)-term is

\[
\alpha_R'\delta,
\]

and \(\delta\) is the shared imputation-parameter displacement. It is identical in \(T_f\) and \(T_0\).

Similarly, write

\[
R(\theta):=L_c(\theta)-\ell_{\rm obs}(\theta)
\]

for the realized conditional loglikelihood contribution. Then

\[
R(\theta_0+a)
=
R_0+u_R'a-\frac12 a'K_Ra+O_p(n^{-1/2}),
\]

with \(u_R=O_p(\sqrt n)\). Hence

\[
Q(\theta_0+a)-L_c(\theta_0+a)
=
\underbrace{F_{00}+\alpha_R'\delta+\frac12\delta'H_R\delta-R_0}_{\text{common heavy constant}}
+
\underbrace{a'J_R\delta-u_R'a+O_p(1)}_{\text{fit-dependent but only }O_p(1)}.
\]

The heavy \(O_p(\sqrt n)\) level noise is in the common constant. It cancels exactly in \(T_f-T_0\).

The fit-dependent linear piece is

\[
(a_f-a_0)'J_R\delta-u_R'(a_f-a_0).
\]

At \(H_0\) and under \(h/\sqrt n\) local alternatives,

\[
a_f-a_0=O_p(n^{-1/2}),\qquad J_R\delta=O_p(\sqrt n),\qquad u_R=O_p(\sqrt n),
\]

so the whole expression is \(O_p(1)\), not \(O_p(\sqrt n)\).

Equivalently, using the quadratic LR form,

\[
d_L
=
\delta'R_C'CR_C\delta+o_p(1),
\]

while for the complete-data MLE displacement \(\eta=C^{-1}S_{\rm com}+o_p(n^{-1/2})\),

\[
d_{\rm com}
=
\eta'R_C'CR_C\eta+o_p(1).
\]

Thus

\[
2D=d_L-d_{\rm com}
=
\delta'R_C'CR_C\delta-\eta'R_C'CR_C\eta+o_p(1).
\]

Both terms are quadratic forms in tight asymptotic normal scores with bounded limiting spectra. Therefore

\[
\operatorname{sd}(D)=O(1)
\]

at \(H_0\) and under \(h/\sqrt n\) local alternatives.

At a fixed alternative, however, the full and null pseudo-true points are separated by \(O(1)\). Then the difference

\[
\sum_i \{e_i(\theta_f^\ast)-e_i(\theta_0^\ast)\}
\]

for the conditional-entropy contrast has nonzero per-observation variance generically, so its standard deviation is \(O(\sqrt n)\). Thus the reversion to \(O(\sqrt n)\) at fixed alternatives is real.

**Adjudication of the C3 attack:** fails. C3 survives.

---

## 2. Attack on C1: should the projection metric be \(I_{\rm obs}\)?

The tempting argument is: all estimation noise comes from the observed-data MLE, so the null fit should project in the \(A=I_{\rm obs}\) metric. That confuses covariance with curvature.

### Compute the Hessian of \(Q\)

For the conditional density \(c_\theta(y_{\rm mis}\mid y_{\rm obs})\),

\[
F(\psi,\phi)=E_\phi[\log c_\psi(Y_{\rm mis}\mid Y_{\rm obs})].
\]

At \((\theta_0,\theta_0)\),

\[
F_\psi(\theta_0,\theta_0)=0,
\]

and by the conditional information identity,

\[
F_{\psi\phi}(\theta_0,\theta_0)=I_{\rm mis},\qquad
F_{\psi\psi}(\theta_0,\theta_0)=-I_{\rm mis}.
\]

Therefore

\[
\nabla^2 Q(\theta_0)
=
\nabla^2\ell_{\rm obs}(\theta_0)+F_{\psi\psi}(\theta_0,\hat\theta_{\rm obs}),
\]

so

\[
-\nabla^2 Q(\theta_0)
=
I_{\rm obs}+I_{\rm mis}+O_p(\sqrt n)
=
I_{\rm com}+O_p(\sqrt n).
\]

Thus the curvature metric is \(C=I_{\rm com}\), not \(A=I_{\rm obs}\).

### Consistency check: the unconstrained maximizer must be \(\hat\theta_{\rm obs}\)

This is decisive. Since

\[
\nabla_\psi F(\hat\theta_{\rm obs},\hat\theta_{\rm obs})=0
\]

by conditional score unbiasedness, and

\[
\nabla \ell_{\rm obs}(\hat\theta_{\rm obs})=0,
\]

we have

\[
\nabla Q(\hat\theta_{\rm obs})=0.
\]

So the unrestricted maximizer of \(Q\) is exactly the observed-data MLE \(\hat\theta_{\rm obs}\) locally.

Now expand around \(\theta_0\). Let \(\delta=\hat\theta_{\rm obs}-\theta_0\). Then

\[
\nabla Q(\theta_0)
=
S+I_{\rm mis}\delta+o_p(\sqrt n).
\]

Since \(S=A\delta+o_p(\sqrt n)\),

\[
\nabla Q(\theta_0)
=
(A+M)\delta+o_p(\sqrt n)
=
C\delta+o_p(\sqrt n).
\]

With curvature \(C\), the Newton displacement is

\[
C^{-1}\nabla Q(\theta_0)=\delta+o_p(n^{-1/2}),
\]

as required. If the curvature were \(A\), the displacement would be

\[
A^{-1}C\delta
=
\delta+A^{-1}M\delta,
\]

which is generally not \(\delta\). So the \(I_{\rm obs}\)-metric attack contradicts the exact self-consistency of \(Q\).

### Compute the C1 expectation formula

Because the unrestricted \(Q\)-maximizer has displacement \(\delta\), the constrained \(Q\)-maximizer is its \(C\)-orthogonal projection:

\[
\hat\delta_0=P_C\delta
=
G(G'CG)^{-1}G'C\delta.
\]

Therefore

\[
d_L
=
(\delta-P_C\delta)'C(\delta-P_C\delta)+o_p(1)
=
\delta'R_C'CR_C\delta+o_p(1).
\]

Since \(\operatorname{Var}(\delta)=A^{-1}+o(n^{-1})\),

\[
E[d_L]
=
\operatorname{tr}(R_C'CR_C A^{-1})+O(n^{-1}).
\]

Now

\[
R_C'CR_C
=
C-CG(G'CG)^{-1}G'C.
\]

Thus

\[
E[d_L]
=
\operatorname{tr}(CA^{-1})
-
\operatorname{tr}\!\left((G'CG)^{-1}G'C A^{-1} C G\right)
+O(n^{-1}).
\]

Use

\[
CA^{-1}=I+MA^{-1},
\]

so

\[
\operatorname{tr}(CA^{-1})=k+\operatorname{tr}(A^{-1}M).
\]

Also,

\[
G'C A^{-1} C G
=
G'C G+G'C A^{-1}M G.
\]

Therefore

\[
\operatorname{tr}\!\left((G'CG)^{-1}G'C A^{-1} C G\right)
=
k_0+
\operatorname{tr}\!\left((G'CG)^{-1}G'C A^{-1}M G\right).
\]

Hence

\[
E[d_L]
=
q_d+\operatorname{tr}(A^{-1}M)
-
\operatorname{tr}\!\left((G'CG)^{-1}G'C A^{-1}M G\right)
+O(n^{-1}).
\]

By Wilks,

\[
E[d_{\rm com}]=q_d+O(n^{-1}).
\]

Therefore

\[
E[d_L-d_{\rm com}]
=
\operatorname{tr}(A^{-1}M)
-
\operatorname{tr}\!\left((G'CG)^{-1}G'C A^{-1}M G\right)
+O(n^{-1}).
\]

Restoring notation,

\[
E[d_L-d_{\rm com}]
=
\operatorname{tr}(RIV_f)
-
\operatorname{tr}\!\left[
(G'I_{\rm com}G)^{-1}
G'I_{\rm com}I_{\rm obs}^{-1}I_{\rm mis}G
\right]
+O(n^{-1}).
\]

That is C1.

**Adjudication of the C1 attack:** fails. The correct projection metric is \(I_{\rm com}\), not \(I_{\rm obs}\). C1 survives.

---

## 3. Attack on C2: can the self-contained difference understate C1?

We need compare

\[
B_0
=
\operatorname{tr}\!\left((G'AG)^{-1}G'MG\right)
\]

with

\[
B_C
=
\operatorname{tr}\!\left((G'CG)^{-1}G'C A^{-1}M G\right).
\]

C2 says \(B_C\ge B_0\), so the self-contained difference

\[
\operatorname{tr}(A^{-1}M)-B_0
\]

is at least the C1 difference

\[
\operatorname{tr}(A^{-1}M)-B_C.
\]

### Whitening proof

Let

\[
H=A^{-1/2}MA^{-1/2}\succeq 0,\qquad U=A^{1/2}G.
\]

Then

\[
B_0
=
\operatorname{tr}\!\left((U'U)^{-1}U'HU\right).
\]

Let \(Q\) be an orthonormal basis for \(\mathcal S=\operatorname{col}(U)\). Then

\[
B_0=\operatorname{tr}(Q'HQ).
\]

Next,

\[
G'CG=U'(I+H)U,
\]

and

\[
G'C A^{-1}M G
=
U'(I+H)HU.
\]

Hence

\[
B_C
=
\operatorname{tr}\!\left(
[Q'(I+H)Q]^{-1}Q'(I+H)HQ
\right).
\]

Block \(H\) relative to \(\mathcal S\oplus\mathcal S^\perp\):

\[
H=
\begin{pmatrix}
H_{11} & H_{12}\\
H_{12}' & H_{22}
\end{pmatrix},
\]

where

\[
H_{11}=Q'HQ.
\]

Then

\[
Q'(I+H)Q=I+H_{11},
\]

and

\[
Q'(I+H)HQ
=
H_{11}+H_{11}^2+H_{12}H_{12}'
=
(I+H_{11})H_{11}+H_{12}H_{12}'.
\]

Therefore

\[
B_C
=
\operatorname{tr}(H_{11})
+
\operatorname{tr}\!\left((I+H_{11})^{-1}H_{12}H_{12}'\right).
\]

But

\[
B_0=\operatorname{tr}(H_{11}),
\]

so

\[
B_C-B_0
=
\operatorname{tr}\!\left((I+H_{11})^{-1}H_{12}H_{12}'\right)
\ge 0.
\]

Equality holds iff

\[
H_{12}=0.
\]

Since \(H\) is symmetric, \(H_{12}=0\) iff \(\mathcal S=\operatorname{col}(A^{1/2}G)\) is an invariant subspace of

\[
H=A^{-1/2}MA^{-1/2}.
\]

Thus no counterexample exists: the self-contained difference cannot understate C1.

In the equal-fraction case \(H=\lambda I\), every subspace is invariant and

\[
B_C=B_0=\lambda k_0,
\]

so both differences equal \(\lambda q_d\).

**Adjudication of the C2 attack:** fails. C2 survives.

---

## 4. Attack on C4: do the \((A)+(C)\) terms differ at \(O(\sqrt n)\) or \(O(1)\) even at \(H_0\)?

The alleged problem is that the conditional-entropy gradients are evaluated at different fitted points. But the leading \((A)+(C)\) term is not evaluated at the two fitted points. It comes from the common imputation-parameter expansion at the common truth \(\theta_0\).

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
O_p(n^{-1/2}),
\]

with

\[
\delta=\hat\theta_{\rm obs}-\theta_0.
\]

Taking expectations gives the level contribution

\[
(A)+(C)
=
\alpha'E[\delta]
+
\frac12\operatorname{tr}(H_\phi A^{-1})
+
O(n^{-1}).
\]

This term is common to \(T_f\) and \(T_0\). It cancels in \(T_f-T_0\), hence in \(D\), at \(H_0\).

The fitted-point dependence enters through the \(\psi\)-argument:

\[
F(\theta_0+a,\hat\theta_{\rm obs})
-
F(\theta_0,\hat\theta_{\rm obs})
=
a'J_R\delta-\frac12a'K_Ra+O_p(n^{-1/2}).
\]

Those terms are \(O_p(1)\) because \(a=O_p(n^{-1/2})\), \(J_R,K_R=O_p(n)\), and \(\delta=O_p(n^{-1/2})\). They are the ordinary RIV/projection terms, not the \((A)+(C)\) design-imbalance term. Again, there is no \(\alpha_R'a\) term because \(F_\psi(\theta_0,\theta_0)=0\).

So the proposed \(O(n)\times O(n^{-1/2})=O(\sqrt n)\) term is spurious: it attaches the \(\phi\)-gradient \(\alpha_R\) to a \(\psi\)-displacement.

### Local alternatives

Under \(h/\sqrt n\) local alternatives, the full and null pseudo-true points differ by \(O(n^{-1/2})\). The design-imbalance functional has the form

\[
B(\theta)
=
\alpha(\theta)'E_\theta[\delta]
+
\frac12\operatorname{tr}\{H_\phi(\theta)I_{\rm obs}(\theta)^{-1}\}
+
O(n^{-1}).
\]

Write per-observation quantities

\[
\alpha(\theta)=n a(\theta),\qquad
H_\phi(\theta)=n h(\theta),\qquad
I_{\rm obs}(\theta)=n i(\theta),
\]

and

\[
E_\theta[\delta]=n^{-1}b(\theta)+O(n^{-2}).
\]

Then

\[
B(\theta)
=
a(\theta)'b(\theta)
+
\frac12\operatorname{tr}\{h(\theta)i(\theta)^{-1}\}
+
O(n^{-1}),
\]

which is an \(O(1)\) smooth function of \(\theta\). Therefore if the two pseudo-true points differ by \(O(n^{-1/2})\),

\[
B(\theta_f^\ast)-B(\theta_0^\ast)=O(n^{-1/2})=o(1).
\]

At fixed alternatives or in non-nested comparisons, the pseudo-true points can differ by \(O(1)\), and then the \((A)+(C)\) differential is genuinely \(O(1)\).

**Adjudication of the C4 attack:** fails. C4 survives.

---

## 5. Verdicts

| Claim | Verdict | Reason |
|---|---:|---|
| **C1** | **SUSTAINED** | The curvature of \(Q\) is \(I_{\rm com}\), not \(I_{\rm obs}\). The unrestricted \(Q\)-maximizer must reproduce \(\hat\theta_{\rm obs}\), which forces the \(I_{\rm com}\) metric. The stated C1 formula follows. |
| **C2** | **SUSTAINED** | After whitening, \(B_C-B_0=\operatorname{tr}((I+H_{11})^{-1}H_{12}H_{12}')\ge0\). Equality iff \(\operatorname{col}(I_{\rm obs}^{1/2}G)\) is invariant under \(I_{\rm obs}^{-1/2}I_{\rm mis}I_{\rm obs}^{-1/2}\). |
| **C3** | **SUSTAINED** | The heavy \(O_p(\sqrt n)\) level noise is a common realized constant and cancels exactly in \(T_f-T_0\). Remaining fitted-point terms are \(O_p(1)\) at \(H_0\) and local alternatives. At fixed alternatives, \(O(\sqrt n)\) noise generically returns. |
| **C4** | **SUSTAINED** | The \((A)+(C)\) design-imbalance term is common at \(H_0\) and cancels to leading order. Local alternatives give only \(O(n^{-1/2})\) differential; fixed alternatives can give genuine \(O(1)\). |

No contradiction with C1 arises in Task 2. The correct H0 differential bias is

\[
E[d_L-d_{\rm com}]
=
\operatorname{tr}(RIV_f)
-
\operatorname{tr}\!\left[
(G'I_{\rm com}G)^{-1}
G'I_{\rm com}I_{\rm obs}^{-1}I_{\rm mis}G
\right]
+
O(n^{-1}),
\]

not the self-contained observed-metric expression

\[
\operatorname{tr}(RIV_f)-\operatorname{tr}(RIV_0).
\]
