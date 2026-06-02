# Layer-3 modeB response — model=gpt-5.5

## Verdict up front

The claim is **wrong under MAR in general**. The realized observed information and the “naive Fisher” information do **not** have the same leading deterministic limit under a MAR mechanism that selects patterns as a function of always-observed variables.

The key error is treating the units in a missingness pattern as if their observed residuals have population moments

\[
E(e_O\mid P)=0,\qquad E(e_Oe_O^\top\mid P)=\Sigma_{OO}.
\]

Under MAR this is generally false. Pattern membership is a selection event depending on observed coordinates, so those conditional moments are shifted at **population order**, i.e. \(O(1)\) per observation, not \(O(n^{-1})\). Therefore the trace difference is generally **\(O(1)\)**, not \(O(n^{-1})\). The empirical fact — “few tenths, stable in \(n\), zero under MCAR” — is exactly what one should expect from a genuine MAR selection effect.

---

# 1. Compute \(E[i_O(\theta_0)]\) and compare to \(i_N(\theta_0)\)

Let pattern \(P\) have observed set \(O\), with \(q=|O|\). Write

\[
e_O = X_O-\mu_O,\qquad 
A=\Sigma_{OO},\qquad 
S=A^{-1}.
\]

For units in pattern \(P\), define the selected residual moments

\[
m_P := E(e_O\mid P),
\]

and

\[
B_P := E(e_Oe_O^\top\mid P).
\]

The naive Fisher information \(i_N\) uses

\[
m_P^{\text{naive}}=0,\qquad B_P^{\text{naive}}=\Sigma_{OO}=A.
\]

But under MAR, if pattern probabilities depend on always-observed coordinates, then the law of \(X_O\mid P\) is generally not the marginal Gaussian law of \(X_O\). Instead,

\[
f(x_O\mid P)
\propto 
\Pr(P\mid x_{\text{always obs}})\, f(x_O).
\]

So unless the propensity is constant or happens to preserve the first two moments,

\[
E(e_O\mid P)\neq 0,
\]

and/or

\[
E(e_Oe_O^\top\mid P)\neq \Sigma_{OO}.
\]

These differences are population-level selection effects. They do **not** shrink with \(n\). Sample quantities satisfy

\[
\frac{1}{n_P}\sum_{i\in P}e_{O,i}\to m_P,
\]

and

\[
\frac{1}{n_P}\sum_{i\in P}e_{O,i}e_{O,i}^\top\to B_P,
\]

with stochastic error \(O_p(n_P^{-1/2})\). Thus the discrepancy between \(E[i_O]\) and \(i_N\) is \(O(n)\) in total information, or \(O(1)\) after normalizing by \(n\).

So the claim \(D=O(n^{-1})\) is not correct under MAR in general.

---

# 2. Closed-form block difference \(E[i_O]-i_N\)

Let \(L_P\) be the selection matrix extracting \(X_O\) from \(X\), so

\[
X_O=L_PX,\qquad \Sigma_{OO}=L_P\Sigma L_P^\top.
\]

Let \(D_p\) be the duplication matrix for \(\operatorname{vech}\Sigma\), and define

\[
R_P := L_P\otimes L_P,
\]

so that

\[
\operatorname{vec}(\Sigma_{OO})
=
R_P\operatorname{vec}(\Sigma)
=
R_PD_p\operatorname{vech}(\Sigma).
\]

For one observation in pattern \(P\), the expected realized observed-information blocks at \(\theta_0\) are as follows.

## \(\mu\mu\) block

The \(\mu\mu\) block does not depend on residual moments:

\[
J^{O}_{\mu\mu,P}
=
L_P^\top S L_P.
\]

This equals the naive block,

\[
J^{N}_{\mu\mu,P}
=
L_P^\top S L_P.
\]

So

\[
\Delta_{\mu\mu,P}:=
J^{O}_{\mu\mu,P}-J^{N}_{\mu\mu,P}
=
0.
\]

## \(\mu\)–\(\operatorname{vech}\Sigma\) cross block

For the realized observed information, the cross block is proportional to the pattern residual sum. Taking expectation under the selected law gives

\[
J^{O}_{\mu\sigma,P}
=
L_P^\top
\left(m_P^\top S\otimes S\right)
R_PD_p,
\]

where \(\sigma=\operatorname{vech}\Sigma\).

The naive Fisher information sets this block to zero:

\[
J^{N}_{\mu\sigma,P}=0.
\]

Therefore

\[
\boxed{
\Delta_{\mu\sigma,P}
=
L_P^\top
\left(m_P^\top S\otimes S\right)
R_PD_p.
}
\]

This is one of the main places the claimed argument fails. Under MAR, \(m_P\) is generally nonzero. Hence the \(\mu\)–\(\operatorname{vech}\Sigma\) block is generally nonzero at leading order. Under MCAR, \(m_P=0\), so this block vanishes.

## \(\operatorname{vech}\Sigma\)–\(\operatorname{vech}\Sigma\) block

The realized covariance-information block depends on the pattern second moment \(B_P=E(e_Oe_O^\top\mid P)\). The selected expected observed block is

\[
J^{O}_{\sigma\sigma,P}
=
\frac12
D_p^\top R_P^\top
\left[
(SB_PS\otimes S)
+
(S\otimes SB_PS)
-
(S\otimes S)
\right]
R_PD_p.
\]

The naive Fisher block plugs in \(B_P=A=\Sigma_{OO}\), giving

\[
J^{N}_{\sigma\sigma,P}
=
\frac12
D_p^\top R_P^\top
(S\otimes S)
R_PD_p.
\]

Thus

\[
\boxed{
\Delta_{\sigma\sigma,P}
=
\frac12
D_p^\top R_P^\top
\left[
\{S(B_P-A)S\otimes S\}
+
\{S\otimes S(B_P-A)S\}
\right]
R_PD_p.
}
\]

This block is nonzero whenever the selected second moment differs from the population second moment:

\[
B_P\neq \Sigma_{OO}.
\]

Again, under MCAR,

\[
B_P=\Sigma_{OO},
\]

so the block vanishes.

---

## Total expected information

Let \(\pi_P=\Pr(P)\). The per-observation expected realized information is

\[
J_O
=
\sum_P \pi_P J^O_P,
\]

while the naive per-observation information is

\[
J_N
=
\sum_P \pi_P J^N_P.
\]

Equivalently, in total sample information,

\[
E[i_O(\theta_0)]
=
nJ_O,
\qquad
i_N(\theta_0)
\approx nJ_N.
\]

The leading difference is

\[
E[i_O(\theta_0)]-i_N(\theta_0)
=
n(J_O-J_N),
\]

where \(J_O-J_N\) contains the nonzero \(\mu\)–\(\operatorname{vech}\Sigma\) and \(\Sigma\Sigma\) pieces above.

So the difference is \(O(n)\) in total information, i.e. \(O(1)\) per observation.

---

# 3. Explicit selected moments under MAR

Suppose the MAR mechanism depends on always-observed coordinates \(A\). For pattern \(P\), write the observed variables as

\[
O=A\cup B,
\]

where \(A\) are always observed and \(B\) are additional variables observed in pattern \(P\). Partition residuals as

\[
e_O=
\begin{pmatrix}
e_A\\
e_B
\end{pmatrix}.
\]

Let the pattern propensity be

\[
w_P(e_A)=\Pr(P\mid e_A),
\]

and define

\[
\pi_P=E\{w_P(e_A)\}.
\]

Then the selected first two moments of \(e_A\) are

\[
a_P
=
E(e_A\mid P)
=
\frac{E\{e_A w_P(e_A)\}}{\pi_P},
\]

and

\[
C_P
=
E(e_Ae_A^\top\mid P)
=
\frac{E\{e_Ae_A^\top w_P(e_A)\}}{\pi_P}.
\]

For Gaussian \(X\), the conditional law of \(e_B\mid e_A\) satisfies

\[
E(e_B\mid e_A)
=
\Gamma e_A,
\qquad
\Gamma
=
\Sigma_{BA}\Sigma_{AA}^{-1},
\]

and

\[
\operatorname{Var}(e_B\mid e_A)
=
\Sigma_{B\mid A}
=
\Sigma_{BB}
-
\Sigma_{BA}\Sigma_{AA}^{-1}\Sigma_{AB}.
\]

Therefore

\[
m_P
=
E(e_O\mid P)
=
\begin{pmatrix}
a_P\\
\Gamma a_P
\end{pmatrix},
\]

and

\[
B_P
=
E(e_Oe_O^\top\mid P)
=
\begin{pmatrix}
C_P & C_P\Gamma^\top\\
\Gamma C_P & \Sigma_{B\mid A}+\Gamma C_P\Gamma^\top
\end{pmatrix}.
\]

The population moment is

\[
\Sigma_{OO}
=
\begin{pmatrix}
\Sigma_{AA} & \Sigma_{AA}\Gamma^\top\\
\Gamma\Sigma_{AA} & \Sigma_{B\mid A}+\Gamma\Sigma_{AA}\Gamma^\top
\end{pmatrix}.
\]

Thus

\[
B_P-\Sigma_{OO}
=
\begin{pmatrix}
C_P-\Sigma_{AA} & (C_P-\Sigma_{AA})\Gamma^\top\\
\Gamma(C_P-\Sigma_{AA}) & \Gamma(C_P-\Sigma_{AA})\Gamma^\top
\end{pmatrix}.
\]

So the selected moments equal the population moments iff

\[
a_P=0
\]

and

\[
C_P=\Sigma_{AA}.
\]

Under MCAR, \(w_P(e_A)\) is constant, so

\[
a_P=0,\qquad C_P=\Sigma_{AA},
\]

and therefore

\[
m_P=0,\qquad B_P=\Sigma_{OO}.
\]

Under genuine MAR, \(w_P(e_A)\) is nonconstant. Then typically

\[
a_P\neq 0
\]

and/or

\[
C_P\neq \Sigma_{AA},
\]

so the information blocks differ at leading order.

---

# 4. Consequence for the trace difference \(D\)

Let

\[
I_{\text{com}}=nJ_{\text{com}}.
\]

Also write

\[
i_N=nJ_N+o_p(n),
\]

and

\[
i_O=nJ_O+O_p(\sqrt n),
\]

with

\[
J_O=E[i_O]/n.
\]

Then

\[
\operatorname{tr}(i_N^{-1}I_{\text{com}})
=
\operatorname{tr}(J_N^{-1}J_{\text{com}})+o_p(1),
\]

and

\[
\operatorname{tr}(i_O^{-1}I_{\text{com}})
=
\operatorname{tr}(J_O^{-1}J_{\text{com}})+o_p(1).
\]

Therefore the leading deterministic trace difference is

\[
\boxed{
D_\infty
=
\operatorname{tr}(J_N^{-1}J_{\text{com}})
-
\operatorname{tr}(J_O^{-1}J_{\text{com}}).
}
\]

If \(J_O\neq J_N\), this is generally an \(O(1)\) number. It does not shrink like \(1/n\).

The exact scalar equality \(D_\infty=0\) would require

\[
\operatorname{tr}\{(J_N^{-1}-J_O^{-1})J_{\text{com}}\}=0.
\]

But the information-convention effect vanishes structurally when

\[
J_O=J_N,
\]

which, in block terms, requires the selected residual moments to match the population residual moments, pattern by pattern up to possible exact cancellations:

\[
E(e_O\mid P)=0,
\]

and

\[
E(e_Oe_O^\top\mid P)=\Sigma_{OO}.
\]

MCAR guarantees this. General MAR does not.

Thus the empirical behavior — a few tenths in magnitude, roughly stable over \(n\), and disappearing under MCAR — is consistent with a genuine \(O(1)\) MAR effect, not with a finite-\(n\) artifact.

---

# 5. Final referee verdict

The information convention **does matter at \(O(1)\)** for the RIV trace under MAR.

The naive expected information \(i_N\) treats pattern-specific observed residuals as if they were drawn from the unselected marginal law. That is valid under MCAR but not under MAR. Under MAR, pattern membership selects units according to observed variables, shifting

\[
E(e_O\mid P)
\]

and/or

\[
E(e_Oe_O^\top\mid P).
\]

Those shifted moments enter directly into the realized observed-information expectation, especially through:

1. the \(\mu\)–\(\operatorname{vech}\Sigma\) cross block, which \(i_N\) incorrectly sets to zero; and  
2. the \(\operatorname{vech}\Sigma\) block, where \(i_N\) incorrectly plugs in \(\Sigma_{OO}\) instead of \(E(e_Oe_O^\top\mid P)\).

The single computation that settles the issue is:

\[
\boxed{
\text{Compute }E[i_O(\theta_0)]\text{ under the actual joint data-and-missingness law and compare it to }i_N(\theta_0).
}
\]

Equivalently, compute the patternwise selected moments

\[
E(e_O\mid P),\qquad E(e_Oe_O^\top\mid P),
\]

plug them into the observed-information block formulas above, and compare the resulting trace with the naive one. If those selected moments differ from \(0\) and \(\Sigma_{OO}\), the trace difference is genuinely \(O(1)\).
