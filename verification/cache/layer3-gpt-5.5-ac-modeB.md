# Layer-3 modeB response — model=gpt-5.5

## Short verdict

The assertion

\[
\operatorname{tr}(C I_{\rm obs}^{-1})=\mathrm{RIV}
\]

is **not correct under MAR if “RIV” is being computed with the unselected/population missing-information matrix**. The mixed eval–impute Hessian \(C=\nabla_{\theta_{\rm eval}}\nabla_{\phi}F\) is the **selected-subsample conditional/missing information**, because only incomplete units contribute and those incomplete units are MAR-selected on always-observed coordinates.

Thus the expansion has an additional leading \(O(1)\) term

\[
\Delta
=
\operatorname{tr}\!\left[
\{I_{\rm mis|obs}^{\rm sel}-I_{\rm mis|obs}^{\rm pop}\}I_{\rm obs}^{-1}
\right],
\]

which is zero under MCAR and generally nonzero under MAR. If the two-term calculation gives \(-0.22\) and the simulation is around \(-0.46\), the missing term is plausibly

\[
\Delta \approx -0.24.
\]

So, subject to checking the precise definition of the simulated RIV, the leading-order answer is **three terms**, not two.

Important caveat: if the simulated “realized observed-information RIV” is truly the Louis/observed-information missing information for the same selected MAR sample, then that RIV already equals the selected \(C\)-term asymptotically, and this particular \(\Delta\) would cancel. The decisive computation is therefore to compare the actual mixed Hessian \(C\) to the actual missing-information matrix used in the RIV calculation.

---

# 1. Derivation of the mixed eval–impute Hessian

For unit \(i\), let its observed pattern be \(r_i\), with observed coordinates \(O_i\) and missing coordinates \(M_i\). Write

\[
F_i(a,b)
=
E_b\{\ell_{\rm com}(a;Y_i)\mid Y_{O_i}\}.
\]

Let

\[
U_{\rm com}(a;Y)=\nabla_a \ell_{\rm com}(a;Y),
\]

and let

\[
U_{\rm obs}(a;Y_O)
=
\nabla_a \ell_{\rm obs}(a;Y_O)
=
E_a\{U_{\rm com}(a;Y)\mid Y_O\}.
\]

The conditional/missing score is

\[
U_{\rm mis|obs}(a;Y)
=
U_{\rm com}(a;Y)-U_{\rm obs}(a;Y_O)
=
\nabla_a \log p_a(Y_M\mid Y_O).
\]

Now compute the mixed derivative:

\[
C_i
:=
\nabla_a\nabla_b F_i(a,b)\big|_{a=b=\theta_0}.
\]

Because the \(b\)-dependence enters only through the conditional imputation density,

\[
\nabla_b E_b\{U_{\rm com}(a;Y)\mid Y_O\}
=
E_b\left[
U_{\rm com}(a;Y)
\{\nabla_b\log p_b(Y_M\mid Y_O)\}^{\top}
\mid Y_O
\right].
\]

At \(a=b=\theta_0\),

\[
\nabla_b\log p_b(Y_M\mid Y_O)\big|_{\theta_0}
=
U_{\rm mis|obs}(\theta_0;Y).
\]

Therefore

\[
C_i
=
E_{\theta_0}
\left[
U_{\rm com}(\theta_0;Y)
U_{\rm mis|obs}(\theta_0;Y)^{\top}
\mid Y_O
\right].
\]

Using

\[
U_{\rm com}=U_{\rm obs}+U_{\rm mis|obs},
\qquad
E(U_{\rm mis|obs}\mid Y_O)=0,
\]

we get

\[
C_i
=
E_{\theta_0}
\left[
U_{\rm mis|obs}U_{\rm mis|obs}^{\top}
\mid Y_O
\right]
=:J_{\rm mis|obs}(Y_O).
\]

Thus for the full sample,

\[
C
=
\sum_i C_i
=
\sum_i J_{\rm mis|obs,i}(Y_{O_i}).
\]

Complete cases have no missing component, so their \(J_{\rm mis|obs,i}=0\). Therefore the mixed eval–impute Hessian is contributed only by incomplete units.

---

# 2. Under MAR, \(C\) is selected-subsample missing information

Let \(R_i\) denote the missingness pattern. Under MAR,

\[
P(R_i=r\mid Y_i)
=
P(R_i=r\mid Y_{O_r}),
\]

so the missingness mechanism is ignorable for likelihood inference about \(\theta\), but it does **not** imply that the incomplete cases are distributed like the population. The incomplete cases are selected according to the MAR propensity.

Let

\[
q_r(o)=P(R=r\mid Y_{O_r}=o),
\]

and let \(f_r(o)\) be the population marginal density of \(Y_{O_r}\). Then the selected missing-information contribution is

\[
I_{\rm mis|obs}^{\rm sel}
=
n\sum_r
\int
q_r(o)\,
J_r(o)\,
f_r(o)\,do.
\]

Equivalently, with \(\pi_r=P(R=r)\),

\[
I_{\rm mis|obs}^{\rm sel}
=
n\sum_r
\pi_r
E\{J_r(Y_{O_r})\mid R=r\}.
\]

By contrast, the unselected/population version with the same pattern proportions would be

\[
I_{\rm mis|obs}^{\rm pop}
=
n\sum_r
\pi_r
E\{J_r(Y_{O_r})\}.
\]

These are equal only if

\[
E\{J_r(Y_{O_r})\mid R=r\}
=
E\{J_r(Y_{O_r})\},
\]

which holds under MCAR but not generally under MAR.

Therefore the mixed eval–impute Hessian satisfies

\[
C
=
I_{\rm mis|obs}^{\rm sel},
\]

not the unselected population object.

Hence, if the RIV being subtracted is

\[
\mathrm{RIV}_{\rm pop}
=
\operatorname{tr}
\left(
I_{\rm obs}^{-1}I_{\rm mis|obs}^{\rm pop}
\right),
\]

then

\[
\operatorname{tr}(C I_{\rm obs}^{-1})
=
\operatorname{tr}
\left(
I_{\rm mis|obs}^{\rm sel}I_{\rm obs}^{-1}
\right)
=
\mathrm{RIV}_{\rm pop}
+
\Delta,
\]

with

\[
\boxed{
\Delta
=
\operatorname{tr}
\left[
\{I_{\rm mis|obs}^{\rm sel}
-
I_{\rm mis|obs}^{\rm pop}\}
I_{\rm obs}^{-1}
\right].
}
\]

This is the omitted third \(O(1)\) term.

Under MCAR, \(q_r(o)=\pi_r\), so

\[
E\{J_r(Y_{O_r})\mid R=r\}=E\{J_r(Y_{O_r})\},
\]

and therefore

\[
I_{\rm mis|obs}^{\rm sel}=I_{\rm mis|obs}^{\rm pop},
\qquad
\Delta=0.
\]

That matches the MCAR control.

---

# 3. Gaussian form: why the selected second moments matter

For a Gaussian unit, partition

\[
Y=(Y_O,Y_M),
\]

with

\[
Y_M\mid Y_O
\sim
N(m,V),
\]

where

\[
m
=
\mu_M+\Sigma_{MO}\Sigma_{OO}^{-1}(Y_O-\mu_O),
\]

and

\[
V
=
\Sigma_{MM}-\Sigma_{MO}\Sigma_{OO}^{-1}\Sigma_{OM}.
\]

Let

\[
e_O=Y_O-\mu_O.
\]

For covariance parameters \(\phi_j,\phi_k\), write

\[
B=\Sigma_{MO}\Sigma_{OO}^{-1},
\qquad
A_j=\frac{\partial B}{\partial \phi_j},
\qquad
V_j=\frac{\partial V}{\partial \phi_j}.
\]

Then the conditional Fisher/missing-information block has the schematic form

\[
[J_r(e_O)]_{jk}
=
e_O^{\top}A_j^{\top}V^{-1}A_k e_O
+
\frac12
\operatorname{tr}
\left(
V^{-1}V_jV^{-1}V_k
\right).
\]

The second term is not affected by selection on \(Y_O\), but the first term is. Therefore

\[
E_{\rm sel}[J_r]-E_{\rm pop}[J_r]
\]

contains terms of the form

\[
\operatorname{tr}
\left[
A_j^{\top}V^{-1}A_k
\left\{
E(e_Oe_O^{\top}\mid R=r)-\Sigma_{OO}
\right\}
\right].
\]

So under MAR, if the incomplete units have selected observed-coordinate residual second moments different from the population moments, then

\[
I_{\rm mis|obs}^{\rm sel}
\neq
I_{\rm mis|obs}^{\rm pop}.
\]

This is exactly the mechanism described in the lemma sheet.

The sign of \(\Delta\) is design-dependent. If the MAR propensity selects incomplete units with smaller observed residual variance in the directions driving the conditional mean Jacobian, then

\[
I_{\rm mis|obs}^{\rm sel}-I_{\rm mis|obs}^{\rm pop}
\]

can be negative in the relevant trace metric, giving

\[
\Delta<0.
\]

That is consistent with the empirical observation that

\[
D_{\rm emp}
\]

lies below the two-term value.

Numerically, if

\[
D_{\rm two-term}\approx -0.22
\]

and the empirical value is approaching roughly

\[
D_{\rm emp}\approx -0.46,
\]

then the implied missing term is

\[
\Delta
\approx
-0.46-(-0.22)
=
-0.24.
\]

That is an \(O(1)\) discrepancy, not a small finite-\(n\) correction.

---

# 4. Why this is not plausibly a realized-vs-expected-information artifact

Let total information scale as

\[
I_{\rm obs,n}=n i_{\rm obs}+O_p(\sqrt n),
\]

and similarly

\[
I_{\rm mis,n}=n i_{\rm mis}+O_p(\sqrt n).
\]

Then

\[
\operatorname{tr}
\left(
I_{\rm obs,n}^{-1}I_{\rm mis,n}
\right)
=
\operatorname{tr}
\left(
i_{\rm obs}^{-1}i_{\rm mis}
\right)
+
O_p(n^{-1/2}),
\]

and its expectation differs from the limit by \(O(n^{-1})\) under ordinary regularity.

Likewise, the next Taylor terms in the expansion of \(A_{\rm rb}\) are not \(O(1)\): the third derivative of \(F\) is \(O(n)\), while \(\delta^3=O_p(n^{-3/2})\), giving \(O_p(n^{-1/2})\), with expectation typically \(O(n^{-1})\).

So a persistent gap of size \(0.2\)–\(0.25\), especially one that grows in magnitude from \(n=800\) to \(n=1500\), is not naturally explained by realized-versus-expected information or ordinary higher-order terms. It is exactly the scale one expects from an omitted \(O(1)\) trace term such as \(\Delta\).

---

# 5. The decisive computation

The single computation that settles the matter is:

\[
T
=
\operatorname{tr}
\left[
\left\{
C-I_{\rm mis|obs}^{\rm RIV}
\right\}
I_{\rm obs}^{-1}
\right],
\]

where

\[
C
=
\nabla_{\theta_{\rm eval}}\nabla_{\phi}F(\theta_0,\theta_0)
=
\sum_i J_{\rm mis|obs,i}(Y_{O_i}),
\]

and \(I_{\rm mis|obs}^{\rm RIV}\) is the missing-information matrix actually used in the RIV subtraction.

Equivalent operational version:

1. Simulate a very large population under the true Gaussian model.
2. Apply the same MAR mechanism.
3. For each incomplete unit compute the Louis conditional missing-information matrix

   \[
   J_i
   =
   E_{\theta_0}
   [
   U_{\rm mis|obs,i}U_{\rm mis|obs,i}^{\top}
   \mid Y_{O_i}
   ].
   \]

4. Average those \(J_i\)’s over the selected incomplete units to get

   \[
   I_{\rm mis|obs}^{\rm sel}.
   \]

5. Separately compute the unselected/population version

   \[
   I_{\rm mis|obs}^{\rm pop}.
   \]

6. Compute

   \[
   \Delta
   =
   \operatorname{tr}
   \left[
   \{I_{\rm mis|obs}^{\rm sel}-I_{\rm mis|obs}^{\rm pop}\}
   I_{\rm obs}^{-1}
   \right].
   \]

If \(\Delta\approx -0.24\), the observed \(-0.46\) is the correct leading-order limit and the two-term \(-0.22\) claim is false.

If instead \(C\) equals the exact missing-information matrix used in the realized RIV calculation, so that

\[
T\to 0,
\]

then this particular third-term explanation is wrong and the gap must come from some other error in the analytic expansion.

But mathematically, under MAR, the mixed eval–impute Hessian is the selected missing information. Therefore the claim that it automatically equals the population RIV is false. The leading-order expansion is three-term unless the RIV is defined using that same selected missing-information matrix.
