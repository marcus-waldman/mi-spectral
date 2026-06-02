# Layer-3 modeA response — model=gpt-5.5

## Notation

Let

- \(R\in\mathcal R\) denote the missingness pattern.
- \(O_r\subset\{1,\dots,p\}\) be the coordinates observed under pattern \(r\).
- \(W\subset O_r\) be the coordinates always observed.
- \(E_r\) be the coordinate-selection matrix such that \(X_{O_r}=E_rX\).
- \(\rho_r=P_0(R=r)\).
- \(\pi_r(x_W)=P_0(R=r\mid X_W=x_W)\), with \(\sum_r\pi_r(x_W)=1\).

The MAR assumption here is

\[
P(R=r\mid X)=P(R=r\mid X_W)=\pi_r(X_W),
\]

with \(\pi_r\) distinct from the Gaussian parameter \(\theta=(\mu,\operatorname{vech}\Sigma)\). Expectations under the full joint law of \((X,R)\) will be denoted \(E_0\). Expectations under the marginal Gaussian law of \(X\) alone will be denoted \(E_X\).

For a given pattern \(r\), write

\[
S_r=\Sigma_{O_rO_r},\qquad A_r=S_r^{-1},\qquad e_r=X_{O_r}-\mu_{O_r}.
\]

At the truth \(\theta_0=(\mu_0,\Sigma_0)\), all quantities below are evaluated at \(\mu_0,\Sigma_0\).

---

# 1. Unconditional expectation of the realized observed information

For one observation in pattern \(r\), the observed-data loglikelihood contribution is

\[
\ell_r(\mu,\Sigma)
=
-\frac12\log |S_r|
-\frac12 e_r^\top S_r^{-1}e_r
-\frac{|O_r|}{2}\log(2\pi).
\]

For local parameters \((m,S)=(\mu_{O_r},\Sigma_{O_rO_r})\), with \(A=S^{-1}\), the score blocks are

\[
s_m=Ae,
\]

and, for a symmetric perturbation \(H\) of \(S\),

\[
s_S(H)
=
\frac12\operatorname{tr}\{A(ee^\top-S)AH\}.
\]

The realized negative Hessian, viewed bilinearly in two parameter perturbations \((a,H)\) and \((b,K)\), is

\[
\begin{aligned}
i_r\{(a,H),(b,K)\}
&=
a^\top A b
+
a^\top A K A e
+
b^\top A H A e
\\
&\quad
-\frac12\operatorname{tr}(A K A H)
\\
&\quad
+\frac12\operatorname{tr}(A K A H A ee^\top)
+
\frac12\operatorname{tr}(A H A K A ee^\top).
\end{aligned}
\tag{1}
\]

Thus the \(\mu\mu\) block is constant, the \(\mu\)–\(\Sigma\) block is linear in \(e\), and the \(\Sigma\Sigma\) block is linear in \(ee^\top\).

Now take expectation under the true joint law of \((X,R)\). For pattern \(r\),

\[
P_0(R=r)=\rho_r=E_X[\pi_r(X_W)].
\]

The selected first and second residual moments are

\[
m_r^{\mathrm{sel}}
=
E_0[e_r\mid R=r]
=
\frac{E_X[\pi_r(X_W)e_r]}{\rho_r},
\tag{2}
\]

and

\[
C_r^{\mathrm{sel}}
=
E_0[e_re_r^\top\mid R=r]
=
\frac{E_X[\pi_r(X_W)e_re_r^\top]}{\rho_r}.
\tag{3}
\]

Therefore

\[
E_0[i_O(\theta_0)]
=
n\sum_{r\in\mathcal R}\rho_r\,
E_0[i_r(\theta_0)\mid R=r],
\tag{4}
\]

where in (1) we replace \(e\) by \(m_r^{\mathrm{sel}}\) in the cross block and \(ee^\top\) by \(C_r^{\mathrm{sel}}\) in the covariance block.

By contrast, the “naive expected information” \(i_N\) described in the question treats the pattern as if fixed by design and replaces residual moments by their unconditional Gaussian population values,

\[
E_X[e_r]=0,\qquad E_X[e_re_r^\top]=S_r.
\]

Hence

\[
i_N(\theta_0)
=
n\sum_{r\in\mathcal R}\rho_r\, i_r^{\mathrm{naive}}(\theta_0),
\tag{5}
\]

where the \(\mu\)–\(\Sigma\) block vanishes and the covariance block uses \(C_r=S_r\).

Thus, in general,

\[
E_0[i_O(\theta_0)]\neq i_N(\theta_0)
\]

under MAR, because \(R\) is not independent of \(X\). The pattern-specific observed sample is a selected subsample.

---

## Selected moments for an incomplete pattern

Let \(O_r=W\cup V_r\), where \(W\) are the always-observed coordinates and \(V_r\) are the additional coordinates observed in pattern \(r\). Partition

\[
e_r=
\begin{pmatrix}
e_W\\
e_{V_r}
\end{pmatrix}.
\]

Define

\[
\delta_r
=
E_0[e_W\mid R=r]
=
\frac{E_X[\pi_r(X_W)e_W]}{\rho_r},
\]

and

\[
M_r
=
E_0[e_We_W^\top\mid R=r]
=
\frac{E_X[\pi_r(X_W)e_We_W^\top]}{\rho_r}.
\]

Under the Gaussian law,

\[
E[e_{V_r}\mid e_W]
=
\Sigma_{V_rW}\Sigma_{WW}^{-1}e_W.
\]

Let

\[
B_r=\Sigma_{V_rW}\Sigma_{WW}^{-1},
\]

and

\[
\Omega_r
=
\Sigma_{V_rV_r}
-
\Sigma_{V_rW}\Sigma_{WW}^{-1}\Sigma_{WV_r}.
\]

Then

\[
m_r^{\mathrm{sel}}
=
E_0[e_r\mid R=r]
=
\begin{pmatrix}
\delta_r\\
B_r\delta_r
\end{pmatrix},
\tag{6}
\]

and

\[
C_r^{\mathrm{sel}}
=
E_0[e_re_r^\top\mid R=r]
=
\begin{pmatrix}
M_r & M_rB_r^\top\\
B_rM_r & B_rM_rB_r^\top+\Omega_r
\end{pmatrix}.
\tag{7}
\]

These are generally not

\[
0
\quad\text{and}\quad
\Sigma_{O_rO_r}.
\]

They reduce to the population moments only if the pattern propensity \(\pi_r(X_W)\) does not distort the first two moments of \(X_W\), i.e.

\[
\delta_r=0,
\qquad
M_r=\Sigma_{WW}.
\]

Under MCAR, \(\pi_r(X_W)\equiv \rho_r\), so this holds automatically. Under genuine MAR, it generally fails.

---

# 2. Closed-form discrepancy \(\Delta I=E_0[i_O]-i_N\)

Let \(H,K\) denote symmetric perturbations of the full covariance matrix \(\Sigma\), and let

\[
H_r=E_rHE_r^\top,\qquad K_r=E_rKE_r^\top.
\]

Let \(u,v\in\mathbb R^p\) be perturbations of \(\mu\), and write

\[
u_r=E_ru,\qquad v_r=E_rv.
\]

Define the selected second-moment discrepancy

\[
B_r^{\mathrm{sel}}
=
C_r^{\mathrm{sel}}-S_r.
\]

Then the discrepancy bilinear form is

\[
\Delta I\{(u,H),(v,K)\}
=
n\sum_{r\in\mathcal R}\rho_r\,
\Delta_r\{(u,H),(v,K)\},
\]

where

\[
\begin{aligned}
\Delta_r\{(u,H),(v,K)\}
&=
u_r^\top A_r K_r A_r m_r^{\mathrm{sel}}
+
v_r^\top A_r H_r A_r m_r^{\mathrm{sel}}
\\
&\quad
+\frac12
\operatorname{tr}\!\left(A_rK_rA_rH_rA_rB_r^{\mathrm{sel}}\right)
\\
&\quad
+\frac12
\operatorname{tr}\!\left(A_rH_rA_rK_rA_rB_r^{\mathrm{sel}}\right).
\end{aligned}
\tag{8}
\]

This gives the block structure immediately.

---

## Block structure

### \(\mu\mu\) block

The \(\mu\mu\) block of the observed information for pattern \(r\) is

\[
A_r=S_r^{-1},
\]

which is nonrandom. Therefore

\[
\Delta I_{\mu\mu}=0.
\]

So the naive and true expected observed information agree in the \(\mu\mu\) block.

---

### \(\mu\)–\(\operatorname{vech}\Sigma\) block

The discrepancy in the cross block is carried by the selected residual mean

\[
m_r^{\mathrm{sel}}=E_0[e_r\mid R=r].
\]

For pattern \(r\), the local cross-block discrepancy is

\[
\Delta I_{\mu,\Sigma}^{(r)}(u,K)
=
n\rho_r\,u_r^\top A_rK_rA_rm_r^{\mathrm{sel}}.
\tag{9}
\]

Equivalently, in vectorized form, with \(G_r=(E_r\otimes E_r)D_p\), where \(D_p\) is the duplication matrix,

\[
\Delta I_{\mu,\operatorname{vech}\Sigma}^{(r)}
=
n\rho_r\,
E_r^\top
\left\{
(m_r^{\mathrm{sel}})^\top A_r\otimes A_r
\right\}
G_r.
\tag{10}
\]

The naive expected information has zero cross block because it uses \(E_X[e_r]=0\). Under MAR, however,

\[
E_0[e_r\mid R=r]\neq 0
\]

generically, so the true expected observed information need not be block diagonal.

---

### \(\operatorname{vech}\Sigma\)–\(\operatorname{vech}\Sigma\) block

The covariance-block discrepancy is carried by

\[
B_r^{\mathrm{sel}}
=
C_r^{\mathrm{sel}}-S_r
=
E_0[e_re_r^\top\mid R=r]-\Sigma_{O_rO_r}.
\]

For covariance perturbations \(H,K\),

\[
\begin{aligned}
\Delta I_{\Sigma\Sigma}^{(r)}(H,K)
&=
n\rho_r
\Bigg[
\frac12
\operatorname{tr}\!\left(A_rK_rA_rH_rA_rB_r^{\mathrm{sel}}\right)
\\
&\qquad\qquad
+
\frac12
\operatorname{tr}\!\left(A_rH_rA_rK_rA_rB_r^{\mathrm{sel}}\right)
\Bigg].
\end{aligned}
\tag{11}
\]

Thus this block is nonzero whenever the selected residual second moment differs from the population covariance.

---

# 3. Trace functional \(T(i)=\operatorname{tr}(i^{-1}I_{\mathrm{com}})\)

The complete-data expected information for \(n\) complete Gaussian observations is

\[
I_{\mathrm{com}}
=
nJ_{\mathrm{com}},
\]

with

\[
J_{\mathrm{com},\mu\mu}=\Sigma^{-1},
\]

\[
J_{\mathrm{com},\mu,\operatorname{vech}\Sigma}=0,
\]

and

\[
J_{\mathrm{com},\operatorname{vech}\Sigma,\operatorname{vech}\Sigma}
=
\frac12
D_p^\top(\Sigma^{-1}\otimes\Sigma^{-1})D_p.
\]

Likewise write

\[
i_N=nJ_N,
\qquad
E_0[i_O]=nJ_O,
\]

where

\[
J_O=J_N+\Delta J,
\qquad
\Delta I=n\Delta J.
\]

Then

\[
T(i_N)
=
\operatorname{tr}\{(nJ_N)^{-1}(nJ_{\mathrm{com}})\}
=
\operatorname{tr}(J_N^{-1}J_{\mathrm{com}}),
\]

and

\[
T(E_0[i_O])
=
\operatorname{tr}\{(nJ_O)^{-1}(nJ_{\mathrm{com}})\}
=
\operatorname{tr}(J_O^{-1}J_{\mathrm{com}}).
\]

Therefore

\[
D
=
T(i_N)-T(E_0[i_O])
=
\operatorname{tr}(J_N^{-1}J_{\mathrm{com}})
-
\operatorname{tr}(J_O^{-1}J_{\mathrm{com}}).
\tag{12}
\]

Equivalently,

\[
D
=
\operatorname{tr}\!\left[
\{J_N^{-1}-J_O^{-1}\}J_{\mathrm{com}}
\right].
\]

Using the matrix inverse identity

\[
A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1},
\]

with \(A=J_N\), \(B=J_O\), gives

\[
D
=
\operatorname{tr}\!\left(
J_N^{-1}\Delta J\,J_O^{-1}J_{\mathrm{com}}
\right).
\tag{13}
\]

Because \(J_N,J_O,J_{\mathrm{com}}\) are all \(O(1)\) per unit, the leading-order discrepancy \(D\) is

\[
D=O(1).
\]

It is neither \(O(n)\) nor \(O(n^{-1})\); the \(n\)’s cancel in the trace functional.

---

## MCAR case

Under MCAR,

\[
\pi_r(X_W)\equiv \rho_r.
\]

Therefore

\[
m_r^{\mathrm{sel}}
=
E_X[e_r]=0,
\]

and

\[
C_r^{\mathrm{sel}}
=
E_X[e_re_r^\top]=S_r.
\]

Hence

\[
\Delta J=0,
\]

so

\[
J_O=J_N,
\]

and therefore

\[
D=0.
\]

Thus the naive fixed-pattern expected information agrees with the true unconditional expectation of the observed information under MCAR.

---

## Genuine MAR case

Under genuine MAR, \(\pi_r(X_W)\) is nonconstant. Then the pattern-specific distribution of \(X_W\) is propensity-weighted:

\[
f_{X_W\mid R=r}(x_W)
=
\frac{\pi_r(x_W)f_{X_W}(x_W)}{\rho_r}.
\]

Consequently, generically,

\[
E_0[e_W\mid R=r]\neq 0
\]

and/or

\[
E_0[e_We_W^\top\mid R=r]\neq \Sigma_{WW}.
\]

By the Gaussian conditional moment formulas, this usually implies

\[
m_r^{\mathrm{sel}}\neq 0
\]

and/or

\[
C_r^{\mathrm{sel}}\neq S_r.
\]

Therefore

\[
\Delta J\neq 0
\]

generically, and hence

\[
D
=
\operatorname{tr}\!\left(
J_N^{-1}\Delta J\,J_O^{-1}J_{\mathrm{com}}
\right)
\]

is generically nonzero.

There can be accidental cancellations, but they are nongeneric.

---

## Necessary and sufficient condition for \(D=0\)

The exact necessary-and-sufficient condition is

\[
\boxed{
\operatorname{tr}\!\left(
J_N^{-1}\Delta J\,J_O^{-1}J_{\mathrm{com}}
\right)=0.
}
\tag{14}
\]

Equivalently,

\[
\boxed{
\operatorname{tr}(J_N^{-1}J_{\mathrm{com}})
=
\operatorname{tr}(J_O^{-1}J_{\mathrm{com}}).
}
\tag{15}
\]

A stronger, more interpretable sufficient condition is

\[
\Delta J=0.
\]

In terms of selected moments, \(\Delta J=0\) holds if, for every pattern \(r\),

\[
m_r^{\mathrm{sel}}=0
\]

and

\[
C_r^{\mathrm{sel}}=S_r.
\]

That is,

\[
E_0[e_r\mid R=r]=0,
\qquad
E_0[e_re_r^\top\mid R=r]=\Sigma_{O_rO_r}.
\]

Under MCAR this is automatic. Under MAR it requires the propensity weights \(\pi_r(X_W)\) to leave the first two moments of every observed subvector unchanged. That can happen in special balanced cases, but it is not generic.

---

# 4. References and recommendation

The general distinction between observed and expected Fisher information goes back to, among others,

- Orchard and Woodbury, who developed early missing-information identities;
- Dempster, Laird and Rubin’s EM framework;
- Louis (1982), who gave the standard formula for the observed information in incomplete-data likelihoods;
- Efron and Hinkley (1978), who emphasized the inferential relevance of observed rather than expected information for conditional accuracy of likelihood inference.

For MAR missing-data likelihood inference specifically, the distinction was emphasized especially by Kenward and Molenberghs, notably in their work on likelihood-based frequentist inference under MAR. Their key point is that, under MAR, the expected information for the observed-data likelihood depends on the missingness distribution, whereas the realized observed information is directly available from the observed-data likelihood itself.

The practical recommendation in that literature is:

\[
\boxed{
\text{Use the observed information, i.e. the realized negative Hessian of the observed-data loglikelihood,}
}
\]

or an equivalent Louis/EM observed-information calculation, rather than a naive expected information matrix obtained by treating the missingness patterns as fixed by design and replacing residual moments by unconditional population moments. Under MCAR the two agree to leading order, but under genuine MAR they generally do not.
