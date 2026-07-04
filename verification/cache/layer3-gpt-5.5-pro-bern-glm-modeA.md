# Layer-3 modeA response — model=gpt-5.5-pro

Let \(p=1-r\), and write the covariate vector as  
\[
Z=(1,X)^\top,\qquad X\sim N(0,1),\qquad \eta=Z^\top\beta_0 .
\]
All population expectations below are over \(X\) at \(\beta_0\). Define
\[
m=A'(\eta),\qquad v=A''(\eta),\qquad w=A'''(\eta),
\]
and
\[
K:=\mathbb E[vZZ^\top],
\]
so that
\[
I_{\rm com}=NK,\qquad I_{\rm obs}=NpK,\qquad 
\operatorname{tr}(\mathrm{RIV})=\operatorname{tr}\{(NpK)^{-1}NrK\}=q\,\frac r p .
\]

Also define the base-measure functional
\[
g(\eta):=\mathbb E_\eta[\log h(Y)].
\]

---

## A1. General canonical-family derivation

For a missing unit, the fitted-arm contribution is the self-expected log density
\[
b(\eta)
:=\mathbb E_{\tilde Y\sim f_\eta}\{\log f(\tilde Y;\eta)\}
=g(\eta)+A'(\eta)\eta-A(\eta).
\]
Its first two derivatives are
\[
b'(\eta)=g'(\eta)+\eta A''(\eta)=g'(\eta)+\eta v,
\]
\[
b''(\eta)=g''(\eta)+A''(\eta)+\eta A'''(\eta)
=g''(\eta)+v+\eta w.
\]

Let \(\delta=\hat\beta_{\rm obs}-\beta_0\). Decompose
\[
T
=
\{\ell_{\rm obs}(\hat\beta_{\rm obs})-\ell_{\rm obs}(\beta_0)\}
-
\{\ell_{\rm com}(\hat\beta_{\rm com})-\ell_{\rm com}(\beta_0)\}
+
\sum_{i:R_i=0}\{b_i(\hat\beta_{\rm obs})-\ell_i(\beta_0;Y_i)\}.
\]
The first two maximization terms each have expectation \(q/2+o(1)\), so they cancel to \(O(1)\). Also
\[
\mathbb E\{b_i(\beta_0)-\ell_i(\beta_0;Y_i)\mid X_i,R_i=0\}=0.
\]
Thus the \(O(1)\) contribution is from expanding the missing self-entropy term:
\[
\sum_{i:R_i=0}\{b_i(\hat\beta_{\rm obs})-b_i(\beta_0)\}
=
D^\top\delta+\frac12\delta^\top C\delta+o_p(1),
\]
where
\[
D=\sum_{i:R_i=0} d_i Z_i,\qquad d_i=g'(\eta_i)+\eta_i v_i,
\]
and
\[
C=\sum_{i:R_i=0} e_i Z_iZ_i^\top,\qquad 
e_i=g''(\eta_i)+v_i+\eta_i w_i.
\]

The observed MLE has \(O(N^{-1})\) bias. A direct score expansion gives
\[
\mathbb E(\hat\beta_{\rm obs}-\beta_0)
=
-\frac{1}{2Np}K^{-1}c+o(N^{-1}),
\]
with
\[
c:=\mathbb E\!\left[w\,Z\,(Z^\top K^{-1}Z)\right].
\]
This is the mechanism by which the MLE bias enters at \(O(1)\): the linear missing-gradient sum \(D\) has expectation \(O(N)\), so \(D^\top \mathbb E\delta\) is \(O(1)\).

Let
\[
\mu_d:=\mathbb E[dZ],\qquad L:=\mathbb E[eZZ^\top].
\]
Then
\[
\mathbb E[D^\top\delta]
=
-\frac r{2p}\,\mu_d^\top K^{-1}c+o(1),
\]
and
\[
\mathbb E\!\left[\frac12\delta^\top C\delta\right]
=
\frac r{2p}\operatorname{tr}(K^{-1}L)+o(1).
\]
Therefore
\[
\boxed{
\mathbb E[T_{\rm fitted}]
=
\frac r{2p}
\left\{
\operatorname{tr}(K^{-1}L)-\mu_d^\top K^{-1}c
\right\}
+o(1).
}
\]

This simplifies nicely. Define
\[
\mu_g:=\mathbb E[g'(\eta)Z],\qquad 
G_2:=\mathbb E[g''(\eta)ZZ^\top].
\]
Because \(\eta=Z^\top\beta_0\),
\[
\mu_d=K\beta_0+\mu_g,
\]
and
\[
L=K+\mathbb E[\eta wZZ^\top]+G_2.
\]
Also
\[
\operatorname{tr}\{K^{-1}\mathbb E[\eta wZZ^\top]\}
=
\beta_0^\top c.
\]
Hence the \(A'''\)-terms cancel algebraically, leaving
\[
\boxed{
\mathbb E[T_{\rm fitted}]
=
\frac r{2p}\{q+\Delta_h\}+o(1),
}
\]
where
\[
\boxed{
\Delta_h
:=
\operatorname{tr}(K^{-1}G_2)-\mu_g^\top K^{-1}c.
}
\]
Equivalently,
\[
\boxed{
\frac{\mathbb E[T_{\rm fitted}]}{\operatorname{tr}(\mathrm{RIV})}
\to
\frac12+\frac{\Delta_h}{2q}.
}
\]

So the apparent \(+\tfrac12\operatorname{tr}(\mathrm{RIV})\) term is universal only up to the extra base-measure term \(\Delta_h\). The base measure \(h\) enters through \(g'(\eta)\) and \(g''(\eta)\). If \(h\) is constant, then \(g'\equiv g''\equiv0\), so \(\Delta_h=0\).

---

## A2. Bernoulli-logit, \(h\equiv 1\)

For Bernoulli-logit,
\[
A(\eta)=\log(1+e^\eta),\qquad h\equiv1,
\]
so
\[
g\equiv0,\qquad \mu_g=0,\qquad G_2=0.
\]
Therefore \(\Delta_h=0\), and
\[
\boxed{
\frac{\mathbb E[T_{\rm fitted}]}{\operatorname{tr}(\mathrm{RIV})}
\to \frac12.
}
\]
This is exact for any design distribution, so at the stated design the number is

\[
\boxed{0.5.}
\]

---

## A3. Poisson-log, \(h(y)=1/y!\)

For Poisson-log,
\[
A(\eta)=e^\eta,\qquad v=w=e^\eta=\lambda.
\]
The fitted limit is
\[
\boxed{
\frac{\mathbb E[T_{\rm fitted}]}{\operatorname{tr}(\mathrm{RIV})}
\to
\frac12+\frac{\Delta_{\rm Pois}}{2q},
}
\]
where
\[
\Delta_{\rm Pois}
=
\operatorname{tr}(K^{-1}G_2)-\mu_g^\top K^{-1}c.
\]
Thus it need not equal the Bernoulli value.

For the stated normal design, write \(\eta=\alpha+\gamma X\) with \(\alpha=0.3,\gamma=0.9\), and \(M=\mathbb E[e^\eta]=e^{\alpha+\gamma^2/2}\). Then
\[
K=M
\begin{pmatrix}
1 & \gamma\\
\gamma & 1+\gamma^2
\end{pmatrix},
\]
and one obtains
\[
\boxed{
\Delta_{\rm Pois}
=
\frac1M
\mathbb E\!\left[
\{(X-\gamma)^2+1\}g''(\alpha+\gamma X)-2g'(\alpha+\gamma X)
\right].
}
\]

For Poisson,
\[
g(\eta)=\mathbb E_\lambda[-\log(Y!)],\qquad \lambda=e^\eta.
\]
Let
\[
L_1(\lambda):=\mathbb E_\lambda[\log(Y+1)],
\]
\[
L_2(\lambda):=\mathbb E_\lambda\!\left[\log\frac{Y+2}{Y+1}\right].
\]
Then
\[
g'(\eta)=-\lambda L_1(\lambda),
\]
\[
g''(\eta)=-\lambda L_1(\lambda)-\lambda^2 L_2(\lambda).
\]
After exponential tilting, with \(U\sim N(0,1)\) and
\[
\Lambda_U=e^{\alpha+\gamma^2+\gamma U},
\]
the extra term becomes
\[
\boxed{
\Delta_{\rm Pois}
=
\mathbb E_U\!\left[
(1-U^2)L_1(\Lambda_U)
-
(1+U^2)\Lambda_U L_2(\Lambda_U)
\right].
}
\]

Here \(L_2(\lambda)>0\). Also
\[
\mathbb E[(1-U^2)F(U)]=-\mathbb E[F''(U)]
\]
for standard normal \(U\), and for \(F(U)=L_1(\Lambda_U)\), \(F''(U)>0\). Hence the first term is negative and the second term is negative. Therefore

\[
\boxed{
\Delta_{\rm Pois}<0
}
\]
at the stated design. So the Poisson-log fitted limit is strictly smaller than Bernoulli’s \(1/2\).

---

## A4. Proper-draw arm: \(T_{\rm draw}-T_{\rm fitted}\)

For one missing unit, conditional on \(\hat\beta_{\rm obs}\), write
\[
t=Z^\top(\beta^\ast-\hat\beta_{\rm obs}),
\qquad 
t\sim N(0,Z^\top I_{\rm obs}^{-1}Z).
\]
The draw-arm contribution minus the fitted-arm contribution is
\[
\mathbb E_t\{g(\hat\eta+t)+A'(\hat\eta+t)\hat\eta\}
-
\{g(\hat\eta)+A'(\hat\eta)\hat\eta\}.
\]
Taylor expansion in \(t\) gives
\[
\frac12\{g''(\eta)+\eta A'''(\eta)\}Z^\top I_{\rm obs}^{-1}Z+o(N^{-1})
\]
per missing unit. Summing over missing units,

\[
\boxed{
\mathbb E[T_{\rm draw}-T_{\rm fitted}]
=
\frac r{2p}
\operatorname{tr}
\left[
K^{-1}
\mathbb E\{(g''(\eta)+\eta w)ZZ^\top\}
\right]
+o(1).
}
\]
Therefore
\[
\boxed{
\frac{\mathbb E[T_{\rm draw}-T_{\rm fitted}]}
{\operatorname{tr}(\mathrm{RIV})}
\to
\frac1{2q}
\operatorname{tr}
\left[
K^{-1}
\mathbb E\{(g''(\eta)+\eta w)ZZ^\top\}
\right].
}
\]

For Bernoulli-logit, \(g\equiv0\), \(w=v(1-2m)\), \(m=\operatorname{logit}^{-1}(\eta)\). Numerical Gaussian quadrature at \(\beta_0=(0.3,0.9)\) gives
\[
K\approx
\begin{pmatrix}
0.20976 & -0.01835\\
-0.01835 & 0.15654
\end{pmatrix},
\]
and
\[
S:=\mathbb E[\eta wZZ^\top]
\approx
\begin{pmatrix}
-0.05930 & -0.01960\\
-0.01960 & -0.11369
\end{pmatrix}.
\]
Thus
\[
\operatorname{tr}(K^{-1}S)\approx -1.0416.
\]
Since \(q=2\),
\[
\boxed{
\frac{\mathbb E[T_{\rm draw}-T_{\rm fitted}]}
{\operatorname{tr}(\mathrm{RIV})}
\to
\frac{-1.0416}{4}
\approx -0.260.
}
\]
So for Bernoulli at this design, the proper-draw arm lowers the fitted-arm value by about \(0.260\,\operatorname{tr}(\mathrm{RIV})\).

---

## A5. Student-\(t_5\) location, fixed scale, no covariate

For a fixed-shape location family,
\[
f(y;\mu)=f_0(y-\mu),
\]
the self-expected log density is translation-invariant:
\[
\mathbb E_{\tilde Y\sim f(\cdot;\mu)}
[\log f(\tilde Y;\mu)]
=
\int f_0(u)\log f_0(u)\,du,
\]
so its derivative and second derivative with respect to \(\mu\) are zero. Therefore the fitted-arm missing contribution has no \(O(1)\) term, and the observed/complete likelihood maximization terms cancel.

Thus
\[
\boxed{
\frac{\mathbb E[T_{\rm fitted}]}
{\operatorname{tr}(\mathrm{RIV})}
\to 0.
}
\]

For the draw arm, a draw \(\mu^\ast-\hat\mu_{\rm obs}\) has variance \(I_{\rm obs}^{-1}\). A second-order shift expansion gives per missing unit
\[
-\frac12 I_\mu I_{\rm obs}^{-1},
\]
where \(I_\mu\) is the one-observation Fisher information for \(\mu\). Summing over missing units yields
\[
-\frac12\frac r p=-\frac12\operatorname{tr}(\mathrm{RIV}),
\]
because here \(q=1\). Hence
\[
\boxed{
\frac{\mathbb E[T_{\rm draw}]}
{\operatorname{tr}(\mathrm{RIV})}
\to -\frac12.
}
\]

So the MVN estimated-covariance \(+\tfrac12\operatorname{tr}(\mathrm{RIV})\) result does **not** transfer universally. Bernoulli-logit happens to give \(+1/2\), Poisson-log has an additional negative base-measure term, and fixed-shape location families give \(0\) in the fitted arm and \(-1/2\) in the draw arm.
