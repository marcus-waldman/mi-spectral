# Layer-3 modeA response — model=gpt-5.5-pro

I will write everything at the fixed evaluation point \(\hat\theta_{\rm obs}\), dropping hats except where useful. Let
\[
\Sigma=\hat\Sigma,\quad \mu=\hat\mu,\quad \Omega=\Sigma^{-1}.
\]

## A1. Exact expression for \(D\)

For one row with missing block \(M\) and observed block \(O\), write
\[
A=\Sigma_{OO}^{-1},\qquad B=\Sigma_{MO}A,\qquad 
V=\Sigma_{MM}-\Sigma_{MO}A\Sigma_{OM},
\]
\[
m=\mu_M+B(y_O-\mu_O).
\]
The complete-data quadratic form at the fixed fitted point decomposes as
\[
(y-\mu)'\Omega(y-\mu)
=(y_O-\mu_O)'\Sigma_{OO}^{-1}(y_O-\mu_O)
+(y_M-m)'V^{-1}(y_M-m).
\]
Thus only the conditional term changes across imputation engines. If an engine draws
\(\phi=(\mu^\ast,\Sigma^\ast)\) and imputes
\[
Y_M^\ast\mid Y_O,\phi\sim N(m^\ast,V^\ast),
\]
then
\[
\mathbb E_\phi\mathbb E_{\phi}\!\left[(Y_M^\ast-m)'V^{-1}(Y_M^\ast-m)\right]
=
\mathbb E_\phi\left[
\operatorname{tr}(V^{-1}V^\ast)
+(m^\ast-m)'V^{-1}(m^\ast-m)
\right].
\]
For FITTED, \(m^\ast=m,\ V^\ast=V\), so the corresponding expectation is \(|M|\). Therefore, exactly,
\[
\boxed{
D
=
-\frac12\sum_{i:M_i\neq\varnothing}
\mathbb E_\phi\left[
\operatorname{tr}\{V_i^{-1}(V_i^\ast-V_i)\}
+(m_i^\ast-m_i)'V_i^{-1}(m_i^\ast-m_i)
\right].
}
\]
Equivalently,
\[
D=-\frac12\sum_i
\operatorname{tr}\left[
V_i^{-1}
\left\{
\mathbb E_\phi(V_i^\ast-V_i)
+
\mathbb E_\phi[(m_i^\ast-m_i)(m_i^\ast-m_i)']
\right\}
\right].
\]
This is exact; no large-\(n\) approximation has been used.

---

## A2. Leading persistent order

For a pattern \(r=(M,O)\), define
\[
L_r=P_M-B_rP_O,\qquad A_r=\Sigma_{OO}^{-1},
\]
and, for a symmetric perturbation \(\Delta=\Sigma^\ast-\Sigma\),
\[
K_r(\Delta)=\Delta_{MO}-B_r\Delta_{OO}
=L_r\Delta P_O'.
\]
Two exact Schur identities are useful:
\[
B_r^\ast-B_r=K_r(\Delta)(\Sigma_{OO}+\Delta_{OO})^{-1},
\]
and
\[
V_r^\ast-V_r
=
L_r\Delta L_r'
-
K_r(\Delta)(\Sigma_{OO}+\Delta_{OO})^{-1}K_r(\Delta)'.
\]
Also, with \(\delta_\mu=\mu^\ast-\mu\),
\[
m_i^\ast-m_i
=
L_r\delta_\mu
+
K_r(\Delta)(\Sigma_{OO}+\Delta_{OO})^{-1}
\{y_{O,i}-\mu_O-\delta_{\mu,O}\}.
\]

Assume the draw law satisfies, for fixed pattern mix,
\[
\sqrt n\,\delta_\mu\Rightarrow Z_\mu,\qquad
\sqrt n\,\Delta\Rightarrow Z_\Sigma,
\]
and
\[
n\,\mathbb E(\Delta)\to B_\Sigma.
\]
Let
\[
S_r=\lim \frac1{n_r}\sum_{i\in r}(y_{O,i}-\mu_O)(y_{O,i}-\mu_O)',\qquad
\eta_r=\lim \frac1{n_r}\sum_{i\in r}(y_{O,i}-\mu_O).
\]
Then the persistent limit of \(D\) is
\[
\boxed{
\begin{aligned}
D_\infty
=
-\frac12\sum_r \pi_r
\Big[
&\operatorname{tr}\{V_r^{-1}L_rB_\Sigma L_r'\}\\
&+\operatorname{tr}\{V_r^{-1}L_r\,\mathbb E(Z_\mu Z_\mu')\,L_r'\}\\
&+2\,\mathbb E\{Z_\mu'L_r'V_r^{-1}K_r(Z_\Sigma)A_r\eta_r\}\\
&+\mathbb E\operatorname{tr}\{V_r^{-1}K_r(Z_\Sigma)
(A_rS_rA_r-A_r)
K_r(Z_\Sigma)'\}
\Big].
\end{aligned}
}
\]
For the three engines here the \(\mu\)-\(\Sigma\) covariance block is zero to leading order, so the third term vanishes.

The \(\mu\)-term is
\[
-\frac12\operatorname{tr}\left(J_{\rm obs,\mu\mu}^{-1}J_{\rm mis,\mu\mu}\right),
\]
where \(J=I/n\). In this design,
\[
\operatorname{tr}(\mathrm{RIV}_\mu)
=\operatorname{tr}\left(J_{\rm obs,\mu\mu}^{-1}J_{\rm com,\mu\mu}\right)-4
\approx 1.11.
\]
Thus the mean-block alone gives
\[
-\frac12\operatorname{tr}(\mathrm{RIV}_\mu)
\approx -0.56,
\qquad
\frac{-0.56}{\operatorname{tr}(\mathrm{RIV})}
\approx -0.10.
\]

Now define the covariance-bias amplification matrix
\[
G_\Sigma
=
\operatorname{unvech}\!\left[
J_{\rm obs,\Sigma\Sigma}^{-1}
J_{\rm com,\Sigma\Sigma}
\operatorname{vech}(\Sigma)
\right],
\]
and the linear functional
\[
\Lambda(B)
=
\sum_r\pi_r\operatorname{tr}\{V_r^{-1}L_rBL_r'\}.
\]
For complete data, the \(O(n^{-1})\) centering constants are:

\[
\begin{array}{c|c}
\text{engine} & n\,\mathbb E(\Sigma^\ast-\Sigma)\\
\hline
\text{Laplace/BvM} & 0\\
\text{Jeffreys posterior} & (p+2)\Sigma\\
\text{bootstrap ML} & -\Sigma
\end{array}
\]

With missing data, EM/missing-information amplification replaces \(\Sigma\) by \(G_\Sigma\). Hence
\[
n\,\mathbb E(\Sigma^\ast-\Sigma)
=
c\,G_\Sigma
\]
with
\[
c_{\rm E1}=0,\qquad c_{\rm E2}=p+2,\qquad c_{\rm E3}=-1.
\]

The bootstrap identity is the key balance:
\[
\sum_i
\operatorname{tr}\left[
V_i^{-1}
\left\{
\mathbb E_{\rm boot}(V_i^\ast-V_i)
+
\mathbb E_{\rm boot}[(m_i^\ast-m_i)(m_i^\ast-m_i)']
\right\}
\right]
=o(1).
\]
Equivalently,
\[
D_{\rm E3}\to 0.
\]
Therefore the zero-centered contribution equals \(\Lambda(G_\Sigma)\), and for an engine with centering constant \(c\),
\[
\boxed{
D_\infty(c)
=
-\frac12(1+c)\Lambda(G_\Sigma).
}
\]

Thus:

\[
\boxed{
D_{\rm E1,\infty}=-\frac12\Lambda(G_\Sigma),
}
\]
\[
\boxed{
D_{\rm E2,\infty}=-\frac{p+3}{2}\Lambda(G_\Sigma),
}
\]
\[
\boxed{
D_{\rm E3,\infty}=0.
}
\]

For \(p=4\), E2 should be approximately \(7\) times E1. With \(\Lambda(G_\Sigma)\approx 1.18\),
\[
\frac{D_{\rm E1}}{\operatorname{tr}(\mathrm{RIV})}
\approx -\frac{0.5(1.18)}{5.6}
\approx -0.105,
\]
and
\[
\frac{D_{\rm E2}}{\operatorname{tr}(\mathrm{RIV})}
\approx -\frac{3.5(1.18)}{5.6}
\approx -0.74.
\]

---

## A3. Covariance plug-in effect

For a mean-centered covariance draw, \(\mathbb E\Delta=0\). The exact Schur identity gives
\[
V^\ast-V=L\Delta L'-K(\Delta)(\Sigma_{OO}+\Delta_{OO})^{-1}K(\Delta)'.
\]
Taking expectation,
\[
\boxed{
\mathbb E(V^\ast)-V
=
-\mathbb E\left[
K(\Delta)(\Sigma_{OO}+\Delta_{OO})^{-1}K(\Delta)'
\right]
\preceq 0.
}
\]
So a mean-centered random covariance draw deflates the conditional imputation spread.

But that deflation does not by itself determine \(D\). The same covariance draw also randomizes the conditional regression coefficient \(B\), producing the conditional-mean term
\[
-\frac12\sum_i
\mathbb E\operatorname{tr}
\{V^{-1}K(\Delta)A x_ix_i'A K(\Delta)'\},
\qquad x_i=y_{O,i}-\mu_O.
\]
The spread-deflation contribution is
\[
+\frac12\sum_i
\mathbb E\operatorname{tr}
\{V^{-1}K(\Delta)A K(\Delta)'\}.
\]
Under MCAR,
\[
\frac1{n_r}\sum_{i\in r}x_ix_i'\to \Sigma_{OO},
\]
so
\[
A\Sigma_{OO}A=A,
\]
and those two covariance-draw terms cancel at persistent order. Under MAR they do not cancel exactly because \(S_r\neq\Sigma_{OO}\).

Thus:

- mean-centered covariance draws deflate \(V\);
- that deflation cancels slope/random-\(B\) variation under MCAR;
- it leaves a small MAR-specific term under this design;
- it does not cancel random \(\mu\)/intercept variation;
- the bootstrap covariance bias \(nE(\Sigma^\ast-\Sigma)=-G_\Sigma\) supplies the missing deflation and makes \(D\to0\).

---

## A4. Necessary and sufficient leading condition for \(D=o(1)\)

From A1,
\[
D=o(1)
\]
if and only if
\[
\boxed{
\sum_i
\operatorname{tr}\left[
V_i^{-1}
\left\{
\mathbb E(V_i^\ast-V_i)
+
\mathbb E[(m_i^\ast-m_i)(m_i^\ast-m_i)']
\right\}
\right]
=o(1).
}
\]
At leading order this is
\[
\boxed{
\Lambda(B_\Sigma)+T=0,
}
\]
where \(T\) is the quadratic contribution from the \(I_{\rm obs}^{-1}\) parameter variance. For engines with the correct first-order covariance \(I_{\rm obs}^{-1}\), this reduces to
\[
\boxed{
n\,\mathbb E(\Sigma^\ast-\Sigma)=-G_\Sigma
}
\]
up to directions annihilated by \(\Lambda\).

That is the precise class of “proper” engines for this deviance-bias theorem: not merely engines with covariance \(I_{\rm obs}^{-1}\), but engines whose \(O(n^{-1})\) covariance centering makes the mixture conditional second moment equal the fitted conditional second moment.

Mechanistically:

- E1 propagates \(I_{\rm obs}^{-1}\) variance but has zero covariance centering, so the random \(\mu\)/intercept contribution remains.
- E2 propagates the same variance but has positive Jeffreys/IW covariance centering \(+(p+2)G_\Sigma/n\), making the imputation distribution persistently too spread out relative to FITTED.
- E3 has negative ML-bootstrap centering \(-G_\Sigma/n\), exactly balancing fitted-mean variability; hence \(D\to0\).

---

## A5. MAR-specific persistent term

Yes. The MAR-specific term is
\[
\boxed{
\mathcal M_{\rm MAR}
=
\sum_r\pi_r
\mathbb E\operatorname{tr}\left[
V_r^{-1}K_r(Z_\Sigma)
A_r(S_r-\Sigma_{OO,r})A_r
K_r(Z_\Sigma)'
\right].
}
\]
If a draw law had nonzero \(\mu\)-\(\Sigma\) cross-covariance, there would also be
\[
2\sum_r\pi_r
\mathbb E\{Z_\mu'L_r'V_r^{-1}K_r(Z_\Sigma)A_r\eta_r\},
\]
but this is zero for E1/E2/E3 to leading order.

Under MCAR, \(S_r=\Sigma_{OO,r}\) and \(\eta_r=0\), so the MAR term is exactly zero. Under this MAR probit design, missingness selects on \(X_3,X_4\), so \(S_r-\Sigma_{OO,r}\neq0\). Numerically the effect is small: the \(\mu\)-block gives \(\operatorname{tr}(\mathrm{RIV}_\mu)\approx1.11\), while
\[
\Lambda(G_\Sigma)\approx1.18,
\]
so
\[
\mathcal M_{\rm MAR}\approx 0.07.
\]
Therefore the MAR-specific contribution to \(D/\operatorname{tr}(\mathrm{RIV})\) is roughly

\[
\text{E1:}\quad -\frac12\frac{0.07}{5.6}\approx -0.006,
\]
\[
\text{E2:}\quad -\frac{p+3}{2}\frac{0.07}{5.6}
\approx -0.04\text{ to }-0.05,
\]
and E3 cancels it in the total because \(c=-1\).

---

## Summary table

Let
\[
\Lambda(G_\Sigma)\approx1.18,\qquad \operatorname{tr}(\mathrm{RIV})\approx5.6,\qquad p=4.
\]

| engine | \(c\) in \(nE(\Sigma^\ast-\Sigma)=cG_\Sigma\) | persistent \(D_\infty\) | normalized |
|---|---:|---:|---:|
| E1 Laplace/BvM | \(0\) | \(-\frac12\Lambda(G_\Sigma)\) | \(\approx -0.105\) |
| E2 Jeffreys DA | \(p+2=6\) | \(-\frac{p+3}{2}\Lambda(G_\Sigma)=-7\cdot \frac12\Lambda(G_\Sigma)\) | \(\approx -0.74\) |
| E3 bootstrap EMB | \(-1\) | \(0\) | \(0\) |

## Verdict

The measured table is explained. The key is that \(D\) is sensitive to the \(O(n^{-1})\) centering of \(\Sigma^\ast\), not only to the \(O(n^{-1})\) covariance \(I_{\rm obs}^{-1}\). E1 has the right covariance but zero centering, giving the small persistent \(\mu\)/intercept term. E2 has the same covariance but Jeffreys/IW covariance centering \(+(p+2)G_\Sigma/n\), giving approximately \(p+3=7\) times the E1 effect, matching \(-0.74\). E3 has ML-bootstrap centering \(-G_\Sigma/n\), which exactly balances fitted-mean variability, so \(D\to0\). No listed measurement needs to be an artifact.
