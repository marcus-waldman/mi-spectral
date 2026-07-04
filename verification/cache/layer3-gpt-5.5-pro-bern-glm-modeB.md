# Layer-3 modeB response — model=gpt-5.5-pro

## Short verdict

I do **not** find an algebraic refutation of the Lemma-P cancellation or of the FITTED Bernoulli \(+1/2\) asymptote. The \(J_{\rm obs}\) vs \(J_{\rm all}\) bookkeeping is correct at \(O(1)\).  

C6/C7 numerical constants are the only parts I would **escalate**: the formulas reduce to one-dimensional integrals, but the quoted Gauss–Hermite values need independent reproduction.

Let \(\rho=r/(1-r)\), \(a=A'''\), \(z=X^\top\Omega^{-1}X\), \(X=(1,x)^\top\).

---

## B1. C1–C8 verdicts

### C1 — **SUSTAIN**

Conditional on design/missingness, write \(J_a=J_{\rm all}=J_o+J_m\). First-order MLE expansions give

\[
\hat\beta_o-\hat\beta_c
=
J_o^{-1}S_o-J_a^{-1}(S_o+S_m)+O_p(N^{-1}),
\]

with \(\operatorname{Var}(S_o)=J_o\), \(\operatorname{Var}(S_m)=J_m\). Hence

\[
\operatorname{Var}(\hat\beta_o-\hat\beta_c\mid X,R)
=
J_o^{-1}-J_a^{-1}+O(N^{-2}).
\]

Then

\[
\mathbb E[\ell_a(\hat\beta_o)-\ell_a(\hat\beta_c)\mid X,R]
=
-\frac12 \operatorname{tr}\{J_a(J_o^{-1}-J_a^{-1})\}+O(N^{-1})
=
-\frac12 \operatorname{tr}(J_mJ_o^{-1})+O(N^{-1}).
\]

Under MCAR,

\[
\mathbb E\operatorname{tr}(J_mJ_o^{-1})
=
q\,\frac r{1-r}+O(N^{-1})
=
\operatorname{tr}(\mathrm{RIV})+O(N^{-1}).
\]

Third-order log-likelihood terms are \(N\cdot O(N^{-2})=O(N^{-1})\), so no family-specific \(O(1)\) term appears.

---

### C2 — **SUSTAIN**, with notation caveat

For a missing row, with \(s_i=X_i^\top\delta\),

\[
\bar q_i(\hat\eta_i)-\ell_i(Y_i;\hat\eta_i)
=
[A'(\eta_i+s_i)-A'(\eta_i)](\eta_i+s_i)
+g(\eta_i+s_i)-g(\eta_i),
\]

after expectation over the true missing \(Y_i\). Taylor expansion gives

\[
(g_i'+\eta_iw_i)s_i
+
w_i s_i^2
+
\frac12(g_i''+\eta_iA_i''')s_i^2
+
O(s_i^3).
\]

Summing over missing rows:

- the \(w_i s_i^2\) term gives \(\operatorname{tr}(J_mJ_o^{-1})=\operatorname{tr}(\mathrm{RIV})+O(N^{-1})\);
- the linear term gives \((A)=\alpha^\top \mathbb E[\delta]\);
- the remaining quadratic curvature gives \((C)=\frac12\operatorname{tr}(\mathcal H_\phi J_o^{-1})\).

Caveat: literally, \((A)\) and \((C)\) should be read as conditional/leading expected quantities. The displayed notation suppresses an outer expectation over the random design and missingness.

---

### C3 — **SUSTAIN**

For canonical GLMs, conditional on the observed design,

\[
0=S-J_o\delta-\frac12\sum_{j\in o}A_j'''(X_j^\top\delta)^2X_j+O_p(N^{-1/2}),
\]

so

\[
\delta
=
J_o^{-1}S
-
\frac12J_o^{-1}
\sum_{j\in o}A_j'''(X_j^\top J_o^{-1}S)^2X_j
+O_p(N^{-3/2}).
\]

Taking expectation over the observed responses,

\[
\mathbb E[(X_j^\top J_o^{-1}S)^2\mid X,R]
=
X_j^\top J_o^{-1}X_j,
\]

hence

\[
\mathbb E[\delta\mid X,R]
=
-\frac12J_o^{-1}
\sum_{j\in o}A_j'''(X_j^\top J_o^{-1}X_j)X_j
+O(N^{-2}).
\]

The sign and factor are correct.

---

### C4 — **SUSTAIN**

Lemma P is exactly true. Since \(\eta=X^\top\beta_0\),

\[
\mathbb E[\eta wX^\top]
=
\beta_0^\top\mathbb E[wXX^\top]
=
\beta_0^\top\Omega.
\]

Therefore

\[
\mathbb E[\eta wX^\top]\Omega^{-1}
\mathbb E[A'''zX]
=
\beta_0^\top\mathbb E[A'''zX]
=
\mathbb E[\eta A'''z].
\]

The cancellation is also paired with the correct \(J_{\rm obs}\)-geometry; see B2 below.

---

### C5 — **SUSTAIN**, asymptotically

For Bernoulli/logit, \(h\equiv1\), so \(g=g'=g''=0\). C4 cancels the \((\eta w,\eta A''')\) parts, leaving

\[
\mathbb E[\bar Q_\infty(\hat\beta_o)-\ell_{\rm com}(\hat\beta_o)]
=
\operatorname{tr}(\mathrm{RIV})+O(N^{-1}).
\]

Combining with C1 gives

\[
\mathbb E[T_{\rm fitted}]
=
+\frac12\operatorname{tr}(\mathrm{RIV})+O(N^{-1}).
\]

This is not finite-\(N\) exact; it is the \(O(1)\) asymptotic coefficient.

---

### C6 — **ESCALATE for the quoted numerical constants; algebra SUSTAINED**

The Poisson derivative identities are correct. For \(Y\sim\mathrm{Pois}(\mu)\),

\[
\partial_\mu \mathbb E f(Y)
=
\mathbb E[f(Y+1)-f(Y)].
\]

With \(f(Y)=\log Y!\),

\[
g'(\eta)
=
-\mu\,\mathbb E_\mu[\log(Y+1)],
\]

and

\[
g''(\eta)
=
-\mu\,\mathbb E_\mu[\log(Y+1)]
-\mu^2\,\mathbb E_\mu\!\left[\log\frac{Y+2}{Y+1}\right].
\]

For the stated lognormal design, \(A'''=w=\mu\), and one can reduce the quadrature check to

\[
\frac{\Delta_{\rm bias}}{\operatorname{tr}(\mathrm{RIV})}
=
\frac{\mathbb E[\mu L_1(\mu)]}{2m},
\]

\[
\frac{\Delta_{\rm curv}}{\operatorname{tr}(\mathrm{RIV})}
=
-\frac14\mathbb E[(\mu L_1(\mu)+\mu^2L_2(\mu))z],
\]

where

\[
L_1(\mu)=\mathbb E_\mu[\log(Y+1)],\qquad
L_2(\mu)=\mathbb E_\mu\!\left[\log\frac{Y+2}{Y+1}\right],
\]

\[
m=\mathbb E[\mu]=e^{0.3+0.9^2/2},\qquad
z=\frac{(x-0.9)^2+1}{m}.
\]

An independent adaptive quadrature or high-order Gauss–Hermite computation of these two scalar expectations decides the quoted \(+0.688\), \(-1.084\), and hence \(\Delta_h/\operatorname{tr}(\mathrm{RIV})=-0.396\). I see no algebraic error, but I would not mark the numerical value sustained without reproducing it independently.

---

### C7 — **SUSTAIN for the variance bookkeeping/formula; ESCALATE only the quoted \(K=-1.042\) numeric**

Let \(s=X^\top(\hat\beta_o-\beta_0)\) and \(\zeta=X^\top(\beta^\ast-\hat\beta_o)\). Conditional on the observed data, \(\mathbb E[\zeta]=0\) and \(\operatorname{Var}(\zeta)=X^\top I_o^{-1}X\).

FITTED missing-row expansion:

\[
D_f
=
p\,s+w s^2+\frac12 c s^2+O_3,
\]

where

\[
p=g'+\eta w,\qquad c=g''+\eta A'''.
\]

DRAW expansion, still evaluated at \(\hat\beta_o\):

\[
D_d
=
p\,s+w s^2+\frac12 c s^2
+\frac12 c\,\mathbb E[\zeta^2\mid\mathrm{obs}]
+O_3.
\]

There is no extra \(w\zeta^2\) term because the likelihood evaluation parameter remains \(\hat\beta_o\). Also, \(w s\zeta\) averages to zero. Therefore

\[
\mathbb E[T_{\rm draw}-T_{\rm fitted}]
=
\frac12\mathbb E\operatorname{tr}(\mathcal H_\phi J_o^{-1})
=
\frac{\rho}{2}
\mathbb E[(g''+\eta A''')z]+O(N^{-1}).
\]

For Bernoulli, \(g=0\), so the ratio is \(K/(2q)\) with

\[
K=\mathbb E[\eta A'''z].
\]

The quoted \(K=-1.042\) needs independent quadrature, but the formula and variance bookkeeping are correct.

---

### C8 — **SUSTAIN**, for regular fixed-scale location families

For a fixed-scale location family, including Student-\(t\) with fixed \((\sigma,\nu)\), the entropy is location-invariant. Thus the FITTED missing anchor is exactly \(-H\), independent of \(\mu\). For missing rows,

\[
-H-\mathbb E_{\mu_0}\log f(Y;\hat\mu)
=
\mathrm{KL}(f_{\mu_0},f_{\hat\mu})
=
\frac12 I(\hat\mu-\mu_0)^2+o_p(N^{-1}).
\]

Summing gives \(+\frac12\operatorname{tr}(\mathrm{RIV})\), which cancels C1’s \(-\frac12\operatorname{tr}(\mathrm{RIV})\). Hence FITTED \(\to0\).

For the draw arm,

\[
\mathbb E_{Y^\ast\sim f_{\mu^\ast}}\log f(Y^\ast;\hat\mu)
=
-H-\mathrm{KL}(f_{\mu^\ast},f_{\hat\mu}),
\]

so the draw contributes an additional \(-\frac12\operatorname{tr}(\mathrm{RIV})\). Thus proper draw \(\to-\frac12\operatorname{tr}(\mathrm{RIV})\).

---

## B2. Is Lemma P paired with the right \(J_{\rm obs}\) geometry?

Yes. The leading bookkeeping is

\[
(A)
=
-\frac12\alpha_m^\top J_o^{-1}b_o,
\]

where

\[
\alpha_m=\sum_{i\in m}(g_i'+\eta_iw_i)X_i,
\]

\[
b_o=
\sum_{j\in o}
A_j'''(X_j^\top J_o^{-1}X_j)X_j.
\]

Using \(J_o=n_o\Omega+O_p(\sqrt N)\),

\[
J_o^{-1}=\frac1{n_o}\Omega^{-1}+O_p(N^{-3/2}),
\]

\[
X_j^\top J_o^{-1}X_j
=
\frac1{n_o}z_j+O_p(N^{-3/2}).
\]

Therefore

\[
b_o
=
\frac1{n_o}\sum_{j\in o}A_j'''z_jX_j+O_p(N^{-1/2})
=
\mathbb E[A'''zX]+O_p(N^{-1/2}),
\]

and

\[
\alpha_m
=
n_m\mathbb E[(g'+\eta w)X]+O_p(\sqrt N).
\]

Thus

\[
(A)
=
-\frac{\rho}{2}
\mathbb E[(g'+\eta w)X^\top]\Omega^{-1}
\mathbb E[A'''zX]
+O_p(N^{-1/2}),
\]

with expectation error \(O(N^{-1})\).

Meanwhile,

\[
(C)
=
\frac12\operatorname{tr}(\mathcal H_\phi J_o^{-1})
=
\frac{\rho}{2}
\mathbb E[(g''+\eta A''')z]
+O_p(N^{-1/2}).
\]

The \(\eta\)-parts are therefore

\[
(A)_\eta
=
-\frac{\rho}{2}
\mathbb E[\eta wX^\top]\Omega^{-1}\mathbb E[A'''zX],
\]

\[
(C)_\eta
=
+\frac{\rho}{2}
\mathbb E[\eta A'''z].
\]

Lemma P makes these exactly equal and opposite. The \(J_{\rm all}\) matrix belongs to C1’s complete-likelihood loss, not to the imputation-bias expansion. Using \(J_{\rm all}^{-1}\) inside C2 would be wrong, but C2/C3 correctly use \(J_{\rm obs}^{-1}\).

---

## B3. Draw-arm variance bookkeeping

C7’s variance accounting is correct under the stated draw scheme.

The key point is that \(\beta^\ast\) changes the imputation distribution but \(\bar Q\) is still evaluated at \(\hat\beta_o\). Therefore the draw perturbation \(\zeta\) enters the imputation mean and \(g\)-term, but not the evaluation shift. Hence:

- the FITTED \(w s^2\) term, which gives \(\operatorname{tr}(\mathrm{RIV})\), stays unchanged;
- \(w s\zeta\) has conditional mean zero;
- there is no \(w\zeta^2\) term;
- the only additional \(O(1)\) term is

\[
\frac12(g''+\eta A''')\operatorname{Var}(\zeta).
\]

So the draw adds exactly one extra copy of the \((C)\)-functional, not one extra copy of the whole imputation-bias term.

---

## B4. Any missing \(O(1)\) terms for discrete responses?

I do not see an additional \(O(1)\) term from discreteness.

- **Lattice/nonsmooth MLE map:** the likelihood is smooth in \(\beta\). The statistic is lattice-valued, but Edgeworth/lattice corrections enter at \(O(N^{-1})\), not \(O(1)\), away from boundary pathologies.

- **Separation/nonexistence:** logistic separation can make the MLE undefined at finite \(N\). Under the stated overlapping logistic model, separation probability should decay rapidly with \(N\). It is not an asymptotic \(O(1)\) correction, but it can matter for finite-\(N\) Monte Carlo if not handled explicitly.

- **Poisson boundary events:** all-zero or degenerate configurations have exponentially small probability under this design.

- **Anchor exactness:** for \(M=\infty\), the fitted missing-row anchor is exactly

\[
\mathbb E_{\hat\eta}[\log f(Y;\hat\eta)]
=
A'(\hat\eta)\hat\eta-A(\hat\eta)+g(\hat\eta)
=
-H(\hat\eta),
\]

also for discrete responses. No smooth-density approximation is being used.

---

## B5. Finite-\(N\) story

Here

\[
\operatorname{tr}(\mathrm{RIV})
=
2\cdot\frac{0.22}{0.78}
\approx0.564.
\]

The observed fitted ratio \(0.846\) versus asymptotic \(0.5\) means a ratio-scale correction of

\[
0.846-0.5=0.346.
\]

If this were purely \(c/N\) at \(N=200\), then

\[
c\approx 200(0.346)\approx69.
\]

That is much larger than the intercept-only and two-point constants, but those are bounded-leverage designs. The Gaussian covariate design has unbounded leverage

\[
z_i=X_i^\top\Omega^{-1}X_i,
\]

and \(O(N^{-1})\) terms can involve moments like \(\mathbb E[z^2]\) or inverse-information fluctuations. That is the one plausible mechanism for a much larger finite-\(N\) coefficient.

Still, for \(\beta=(0.3,0.9)\), \(n_{\rm obs}\approx156\), and no obvious near-singularity, a coefficient near \(70\) would be surprisingly large unless rare high-leverage or near-separated samples dominate. The MC point is only about \(2.1\) standard errors above \(0.5\), so I would not treat it as strong evidence against the asymptote.

The decisive check is the registered \(N\)-scan. If the asymptote is \(0.5\) with \(c\approx70\), one would expect rough ratios

\[
N=400:\quad 0.5+70/400\approx0.675,
\]

\[
N=800:\quad 0.5+70/800\approx0.588.
\]

If the ratio stays near \(0.8\), then the derivation is missing an \(O(1)\) term. If it falls approximately linearly in \(1/N\), the derivation survives and the \(N=200\) point is a finite-\(N\)/Monte-Carlo artifact.
