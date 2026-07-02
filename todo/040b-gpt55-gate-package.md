# todo/040b — Layer-3 cross-model gate, round 2: GPT-5.5 audit of the engine-gap derivations

**Provenance.** Round 1 of the todo/040 cross-model protocol sent the Phase-0 DA-engine finding
to Claude Fable 5 (`todo/040-cross-model-derivation-handoff.md`); Fable's audit
(`todo/040-audit-response-fable5.md`, commit `cc62ad7`) resolved the fork with NEW analytic
results: an exact per-unit identity for the engine-vs-FITTED gap, a master formula
$\Xi=b_\Sigma+\operatorname{Var}(\mu^\ast)$, a Schur-concavity cancellation lemma, the
$-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$ Laplace coefficient, the bootstrap
second-moment identity, and a small MAR-only imbalance term. Per the standing cross-model
protocol, those new derivations get an independent off-lineage check **before** they land in
`manuscript/derivation.qmd`. This package is that check.

**How to run (Marcus).** The runner sends each mode as its own API call and hard-truncates the
file at the answer-key banner near the bottom, so the key is never transmitted:

```
py verification/run_layer3_openai.py gpt-5.5 --effort xhigh --timeout 86400 \
    --package todo/040b-gpt55-gate-package.md --tag -da-engine
```

Launch backgrounded (xhigh runs are long; default timeout 24 h). Outputs land at
`verification/cache/layer3-gpt-5.5-da-engine-modeA.md` / `-modeB.md`.

**What "pass" means.** Mode A (blind) lands the same objects and coefficients independently;
Mode B (red-team) sustains the claims, or its refutations are triaged against the
exact-identity evaluator (`verification/spikes/audit-engine-formula.R`) and win only if they
survive that. Any sustained refutation reopens the todo/040 framing call.

---

## MODE A — blind derivation (no access to our answers; derive from scratch)

You are auditing a statistical derivation at maximum reasoning effort. Work from first
principles. Show all algebra. Do not assume any decomposition of the measured effects beyond
what you derive.

### Setup

Data: $n$ i.i.d. rows of a $p$-variate normal $N(\mu_0,\Sigma_0)$, $p=4$, $\mu_0=0$,
$$\Sigma_0=\begin{pmatrix}1&.6&.3&0\\ .6&1&0&.3\\ .3&0&1&.5\\ 0&.3&.5&1\end{pmatrix}.$$
Missingness is MAR and non-monotone: $R_1\mid X_3\sim\mathrm{Bern}(\Phi(-0.5+0.4X_3))$,
$R_2\mid X_4\sim\mathrm{Bern}(\Phi(-0.5+0.4X_4))$ independently ($\approx32\%$ of $X_1$ and of
$X_2$ missing; $X_3,X_4$ always observed; a row can miss $X_1$, $X_2$, both, or neither).
Parameter $\theta=(\mu,\operatorname{vech}\Sigma)$, $k=14$. $\hat\theta_{\text{obs}}$ = the
observed-data MLE (EM). $I_{\text{com}}$, $I_{\text{obs}}$ = complete- and observed-data
expected information at $\hat\theta_{\text{obs}}$ (for this model $I_{\text{obs}}$ is exactly
block-diagonal between $\mu$ and $\operatorname{vech}\Sigma$);
$I_{\text{mis}\mid\text{obs}}=I_{\text{com}}-I_{\text{obs}}$;
$\mathrm{RIV}=I_{\text{obs}}^{-1}I_{\text{com}}-I_k$. At this design
$\operatorname{tr}(\mathrm{RIV})\approx5.6$, and the average number of missing cells per row is
$\approx0.65$.

Per incomplete unit $i$ with observed block $O$ and missing block $M$ (at
$\hat\theta=(\hat\mu,\hat\Sigma)$): $\hat B_i=\hat\Sigma_{MO}\hat\Sigma_{OO}^{-1}$,
$\hat V_i=\hat\Sigma_{MM}-\hat B_i\hat\Sigma_{OM}$ (Schur complement),
$\hat m_i=\hat\mu_M+\hat B_i(y_{O,i}-\hat\mu_O)$.

Every imputation engine below draws an imputation parameter $\phi=(\mu^\ast,\Sigma^\ast)$ given
$Y_{\text{obs}}$ and then imputes each unit's missing block from the conditional normal
$N(m_i(\phi),V_i(\phi))$ (with $m_i,V_i$ the conditional-mean and Schur maps evaluated at
$\phi$). The average complete-data log-likelihood over $M\to\infty$ completions, evaluated at
the FIXED point $\hat\theta_{\text{obs}}$, is
$\bar Q_{\text{engine}}(\hat\theta_{\text{obs}})$. The comparison baseline is FITTED:
$\phi\equiv\hat\theta_{\text{obs}}$ (a point mass — deterministic congenial imputation). The
object of interest, computed paired per dataset and normalized by
$\operatorname{tr}(\mathrm{RIV})$, is
$$D=\bar Q_{\text{engine}}(\hat\theta_{\text{obs}})-\bar Q_{\text{fitted}}(\hat\theta_{\text{obs}}).$$

Engines:

- **E1 Laplace/BvM draw:** $\theta^\ast\sim N(\hat\theta_{\text{obs}},I_{\text{obs}}^{-1})$ on
  $(\mu,\operatorname{vech}\Sigma)$, redrawing if $\Sigma^\ast$ is not positive definite
  (rejection rate measured $\approx0$).
- **E2 exact Bayesian DA, Jeffreys prior** $|\Sigma|^{-(p+1)/2}$: Tanner–Wong alternation — I-step
  completes $Y_{\text{mis}}$ from the conditional normal at the current $(\mu,\Sigma)$; P-step
  draws $\Sigma\sim\mathrm{IW}(n-1,\,SS)$ with $SS$ the completed-data sum of squares about the
  completed-data mean $\bar y$, then $\mu\mid\Sigma\sim N(\bar y,\Sigma/n)$. Stationary draws
  (long burn-in, thinned). Marginally $\phi\sim\pi(\phi\mid Y_{\text{obs}})$.
- **E3 bootstrap EMB** (the Amelia construction): resample $n$ rows (with their missingness
  patterns) with replacement, run EM on the resample to its MLE $\tilde\theta$ (covariance
  divisor $n$), impute the ORIGINAL data from $\tilde\theta$.

Measured facts (all high-power, two independent implementations for E2; you must explain them,
not assume them):

| engine | $D/\operatorname{tr}(\mathrm{RIV})$ at $N{=}200$ | $N$-scan behavior |
|---|---|---|
| E2 Jeffreys DA (two independent engines agree to 3rd decimal) | $-0.783$ (se .002) | $-0.783,-0.766,-0.764,-0.746$ at $N=200/500/1000/2000$; $a+b/n$ fit $\to\approx-0.74$ (persistent) |
| E1 Laplace | $-0.121$ (se .002) | $\to\approx-0.106$ (persistent) |
| E3 bootstrap EMB | $-0.087$ (se .003) | $-0.099,-0.047,-0.029,-0.019$; $\to\approx-0.01\ldots-0.02$ |
| (context) brms/HMC, weakly-informative LKJ+half-$t$ | $-1.36$ (se .15, $R{=}6$) | not scanned |

For every engine the drawn $\theta^\ast$'s covariance matches $I_{\text{obs}}^{-1}$ (measured
trace ratios 1.00–1.05), so under-propagation of parameter uncertainty is excluded.

Known anchor (previously cross-verified, part of the problem statement): when $\Sigma$ is KNOWN
and only $\mu$ is estimated, the posterior-draw engine satisfies
$D=-C_n=-\tfrac12\operatorname{tr}(\mathrm{RIV})$ (all missing information is
$\mu$-information in that regime), while deterministic FITTED gives $0$.

### Tasks (derive; show the algebra)

- **A1.** Derive an exact (no-expansion) expression for $D$ for an arbitrary draw law of
  $\phi=(\mu^\ast,\Sigma^\ast)$, exploiting that the completion is conditional-Gaussian and the
  evaluation point is fixed at $\hat\theta_{\text{obs}}$.
- **A2.** Reduce A1 to persistent (leading) order as $n\to\infty$ with the pattern mix fixed.
  Identify the functional(s) of the draw law that control the persistent value of $D$, and give
  closed-form persistent coefficients for E1, E2, E3 in terms of information-matrix objects,
  $p$, and pattern quantities. State which engine(s) give $D\to0$ and why.
- **A3.** Settle the covariance-plug-in effect: for a MEAN-CENTERED draw of $\Sigma^\ast$
  (e.g. E1), is $\mathbb{E}[V_i(\Sigma^\ast)]-\hat V_i$ positive or negative semidefinite
  (inflation or deflation of the imputation spread), and does this effect contribute a
  persistent term to $D$ — alone, or in combination with other terms? Be precise about what
  cancels against what, and under which missingness mechanism the cancellation is exact.
- **A4.** State the necessary-and-sufficient leading-order condition on the draw law for
  $D=o(1)$ — i.e., exactly which class of "proper MI" engines the
  $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ deviance-bias theorem (whose FITTED form is the
  baseline here) is a theorem about. Explain mechanistically why E3 satisfies it and E1/E2 do
  not, given that all three propagate the same $I_{\text{obs}}^{-1}$ parameter variance.
- **A5.** Is there any MAR-specific persistent contribution to $D$ (present for the drawing
  engines under this MAR design but exactly zero under MCAR at the same rates)? If yes, derive
  its structure and estimate its order of magnitude at this design; if no, prove there is none.

Deliverable: derivations first; then a summary table engine $\to$ persistent coefficient
(symbolic, plus numeric where the given design quantities suffice); then a one-paragraph verdict
on whether the measured table is fully explained. If you conclude any measured phenomenon must
be an artifact, identify which measurement and the mechanism of the artifact.

<!-- MODE-A END -->

## MODE B — red-team the stated derivations

You are auditing, at maximum reasoning effort, a set of NEW derivations produced by another
model (Claude Fable 5) that resolve an empirical engine-dependence finding. Your job is to
BREAK them: verify or refute each claim with algebra, hunt for the error modes listed at the
end, and try to construct counterexamples. Sustaining everything is an acceptable outcome only
if you genuinely tried to break it.

### Setup (self-contained)

Same model and design throughout: $n$ i.i.d. rows of $N(\mu_0,\Sigma_0)$, $p=4$, $\mu_0=0$,
$$\Sigma_0=\begin{pmatrix}1&.6&.3&0\\ .6&1&0&.3\\ .3&0&1&.5\\ 0&.3&.5&1\end{pmatrix},$$
MAR non-monotone missingness $R_1\mid X_3\sim\mathrm{Bern}(\Phi(-0.5+0.4X_3))$,
$R_2\mid X_4\sim\mathrm{Bern}(\Phi(-0.5+0.4X_4))$ ($\approx32\%$ each; $X_3,X_4$ complete). An
MCAR variant uses $\Phi(-0.468)$ with no covariate dependence (same rates).
$\theta=(\mu,\operatorname{vech}\Sigma)$, $k=14$; $\hat\theta_{\text{obs}}$ = observed-data MLE
(EM); $I_{\text{obs}}$ (block-diagonal in $\mu$ vs $\operatorname{vech}\Sigma$ for this model),
$I_{\text{com}}$, $I_{\text{mis}\mid\text{obs}}=I_{\text{com}}-I_{\text{obs}}$,
$\mathrm{RIV}=I_{\text{obs}}^{-1}I_{\text{com}}-I_k$;
$\mathrm{RIV}_{\mu\mu}$ denotes the $\mu$-block
$[I_{\text{obs}}^{-1}]_{\mu\mu}[I_{\text{mis}\mid\text{obs}}]_{\mu\mu}$. Measured at this
design: $\operatorname{tr}(\mathrm{RIV})=5.63$,
$\operatorname{tr}(\mathrm{RIV}_{\mu\mu})=1.14$ ($\mu$ share $0.202$, stable in $n$), average
missing cells per row $0.648$.

Per incomplete unit $i$ (blocks $O,M$ at $\hat\theta$): $\hat B_i=\hat\Sigma_{MO}\hat\Sigma_{OO}^{-1}$,
$\hat V_i=\hat\Sigma_{MM}-\hat B_i\hat\Sigma_{OM}$, $C_i=[\,I_{|M|},\ -\hat B_i\,]$ (so
$m_i(\theta)$ has $\partial m_i/\partial\mu=C_i$ exactly), fitted mean
$\hat m_i=\hat\mu_M+\hat B_i(y_{O,i}-\hat\mu_O)$, fitted-completed residual $r_i$ ($M$-entries
$\hat m_i-\hat\mu_M$, $O$-entries $y_{O,i}-\hat\mu_O$).

Engines: **E1** Laplace $\theta^\ast\sim N(\hat\theta_{\text{obs}},I_{\text{obs}}^{-1})$
(PD-rejection; measured rejection rate $0.0000$); **E2** exact Jeffreys-prior
($|\Sigma|^{-(p+1)/2}$) data augmentation (I-step conditional-normal completion; P-step
$\Sigma\sim\mathrm{IW}(n-1,SS)$, $SS$ = completed sum of squares about $\bar y$;
$\mu\mid\Sigma\sim N(\bar y,\Sigma/n)$; stationary draws); **E3** bootstrap EMB (resample rows
with patterns, EM to the divisor-$n$ MLE $\tilde\theta$, impute the original data). All impute
$Y_{\text{mis},i}\mid\phi\sim N(m_i(\phi),V_i(\phi))$. Object:
$D=\bar Q_{\text{engine}}(\hat\theta_{\text{obs}})-\bar Q_{\text{fitted}}(\hat\theta_{\text{obs}})$
(infinite-$M$; FITTED = point mass at $\hat\theta_{\text{obs}}$), paired per dataset,
normalized by $\operatorname{tr}(\mathrm{RIV})$.

### The claims under audit

**C1 (exact identity).** For any draw law of $\phi$ and any unit $i$, with
$d_i=m_i(\phi)-\hat m_i$:
$$q_i(\phi)-q_i(\hat\theta)=-\tfrac12\Big[d_i^\top\hat V_i^{-1}d_i+\operatorname{tr}\big(\hat V_i^{-1}(V_i(\phi)-\hat V_i)\big)\Big]$$
exactly (no expansion), where $q_i$ is the completion-averaged per-unit contribution to
$\bar Q(\hat\theta_{\text{obs}})$. Supporting facts claimed: $[\hat\Sigma^{-1}]_{MM}=\hat V_i^{-1}$,
and the cross term vanishes because $[\hat\Sigma^{-1}r_i]_M=\hat V_i^{-1}(r_{i,M}-\hat B_ir_{i,O})=0$.
Hence $D=-\tfrac12\sum_i\operatorname{tr}(\hat V_i^{-1}(M_{2,i}-\hat V_i))$ with $M_{2,i}$ the
engine's imputation-predictive second moment about the fitted mean.

**C2 (Schur derivatives).** With $\Delta$ symmetric and
$\dot B(\Delta)=(\Delta_{MO}-\hat B\Delta_{OO})\hat\Sigma_{OO}^{-1}$:
$V'[\Delta]=C\Delta C^\top$ (envelope theorem on $V(\Sigma)=\min_B(I,-B)\Sigma(I,-B)^\top$) and
$V''[\Delta,\Delta]=-2\,\dot B(\Delta)\hat\Sigma_{OO}\dot B(\Delta)^\top\preceq0$: the Schur
complement is matrix-CONCAVE in $\Sigma$, so a mean-centered $\Sigma^\ast$ draw DEFLATES
$\mathbb{E}[V_i(\Sigma^\ast)]$. (This contradicts the round-1 conjecture of a "Jensen
INFLATION of the Schur complement" — decide who is right.) Also claimed exact:
$C_i\hat\Sigma C_i^\top=\hat V_i$ and
$\sum_i C_i^\top\hat V_i^{-1}C_i=[I_{\text{mis}\mid\text{obs}}]_{\mu\mu}$ (block-inversion).

**C3 (cancellation lemma).** Expanding C1 to second order in $\delta=\phi-\hat\theta$ (bias
$b$, covariance $\Phi$): the $\Sigma$-part of the mean-wander,
$\operatorname{tr}(\mathbb{E}[\dot B^\top\hat V^{-1}\dot B]\,r_Or_O^\top)$ summed over units,
and the concavity term $-\operatorname{tr}(\mathbb{E}[\dot B^\top\hat V^{-1}\dot B]\,\hat\Sigma_{OO})$
summed over units, cancel exactly in expectation whenever the within-pattern law of $Y_O$ has
second moment $\hat\Sigma_{OO}$ — true under MCAR; under MAR the pattern-conditional law of
$Y_O$ is shifted and the residual is a design-imbalance cross term ("IMB", C8). The
$\mu\Sigma$ cross-wander vanishes ($I_{\text{obs}}$ block-diagonality + symmetric $\mu$-draws).
Order bookkeeping claimed: per-unit absolute third-order remainders are $O(n^{-3/2})$
($O(n^{-1/2})$ after summing); SIGNED third-moment terms are $O(n^{-2})$ per unit because
$\mathbb{E}[\delta^{\otimes3}]=O(n^{-2})$ for posterior/Laplace/bootstrap draws — hence no
skewness ("shape") term can persist.

**C4 (master formula).**
$$D=-\tfrac12\sum_i\operatorname{tr}\big(\hat V_i^{-1}C_i\,\Xi\,C_i^\top\big)-\mathrm{IMB}+o(1),
\qquad \Xi=b_\Sigma+\operatorname{Var}(\mu^\ast),$$
with $b_\Sigma=\mathbb{E}[\Sigma^\ast\mid Y_{\text{obs}}]-\hat\Sigma$. With
$\operatorname{Var}(\mu^\ast)=[I_{\text{obs}}^{-1}]_{\mu\mu}$ the $\operatorname{Var}(\mu^\ast)$
part contracts to $-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$ exactly (via C2's last
identity).

**C5 (E1 Laplace).** $b_\Sigma=0$, so the persistent value is
$D_{\text{E1}}=-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})-\mathrm{IMB}$
$=-0.1011-0.006\approx-0.107$ at this design — matching the measured asymptote $-0.106$. The
$\mu$-wander term is claimed to be the paper's known-scale posterior-draw imputation variance
$C_n$ surviving as its $\mu$-block in the estimated-scale regime (for known scale
$\mathrm{RIV}_{\mu\mu}=\mathrm{RIV}$ and it reduces to the anchor
$-\tfrac12\operatorname{tr}(\mathrm{RIV})$).

**C6 (E2 Jeffreys-IW).** Complete-data posterior mean:
$\mathbb{E}[\Sigma\mid Y]=\tfrac{n}{n-p-2}\hat\Sigma_{\text{ML}}$, i.e.
$b_\Sigma=\tfrac{p+2}{n}\hat\Sigma+O(n^{-2})$ RELATIVE TO THE MLE (claimed: the natural
constant here is $p+2=6$, not $p+1$ — the $(n-1)/(n-p-2)$ form is relative to the
divisor-$(n-1)$ $S$). Since $C\hat\Sigma C^\top=\hat V$, a proportional bias contracts in
closed form: $-\tfrac{\kappa}{2}n_{\text{mis}}$. Under missingness the posterior-mean
inflation is anisotropic (per block roughly $(p{+}2)/[n(1-\mathrm{FMI}_{\text{block}})]$);
measured: diagonal-average $n\kappa\approx7.07$, contraction-weighted $\approx11.3$ at
$N{=}200$ ($10.7$ at $N{=}1000$). Persistent total
$D_{\text{E2}}=-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})-\tfrac12\sum_i\operatorname{tr}(\hat V_i^{-1}C_ib_\Sigma C_i^\top)-\mathrm{IMB}$.
Corollary claimed: the round-1 "deflated arm" (every draw rescaled by the SCALAR
$(N{-}p{-}2)/(N{-}1)$), which landed at $-0.244$, removed only the isotropic part of
$b_\Sigma$; its leftover $\approx-0.12$ is residual ANISOTROPIC centering bias, not an
"IW-shape" effect — no persistent shape term is possible by C3's order argument, and
recentring by the measured MATRIX bias collapses E2 onto E1 (measured $-0.150$ vs $-0.124$ at
$N{=}200$; $-0.138$ vs $-0.122$ at $N{=}1000$).

**C7 (E3 bootstrap).** Complete-data identity, exact:
$\tilde\Sigma+(\tilde\mu-\hat\mu)(\tilde\mu-\hat\mu)^\top=\tfrac1n\sum_j(y_j^\ast-\hat\mu)(y_j^\ast-\hat\mu)^\top$,
so $\mathbb{E}^\ast[\tilde\Sigma+(\tilde\mu-\hat\mu)^{\otimes2}]=\hat\Sigma$ and
$\Xi_{\text{E3}}=0$: the divisor-$n$ deflation of the resampled MLE is the same empirical
moment as the $\tilde\mu$ wander. With missing data
$\Xi_{\text{E3}}=\widehat{\mathrm{Bias}}^\ast(\hat\Sigma_{\text{obs}})+\operatorname{Var}^\ast(\tilde\mu)$,
whose $\mu$-part cancels at $O(1/n)$, leaving the non-$\mu$ (Cox–Snell curvature) part of the
MLE's own bias — small; measured pieces at $N{=}200$: $b_\Sigma$ contraction $+0.071$ vs
$\mu$-wander $-0.114$ (sum $-0.043$, shrinking with $n$). Hence Amelia converges to FITTED up
to a $\lesssim0.01$-scale floor (its measured $N{=}2000$ value $-0.019$ $\approx$ IMB $+$
residual).

**C8 (IMB, the weakest claim).** The MAR-only design-imbalance term
$$\mathrm{IMB}=\tfrac12\sum_{\text{patterns}}\operatorname{tr}\Big(\mathbb{E}\big[\dot B^\top\hat V^{-1}\dot B\big]\Big(\textstyle\sum_{\text{rows}}r_Or_O^\top-n_{\text{pat}}\hat\Sigma_{OO}\Big)\Big),$$
carried by EVERY drawing engine (it scales with the draw's $\Sigma$-covariance, not its mean),
absent for FITTED, exactly zero under MCAR. Measured: $-0.0049$ (se $.0012$) at $N{=}200$ MAR,
$-0.0065$ (se $.0005$) at $N{=}1000$ MAR, $+0.0003$ (se $.0011/.0006$) under MCAR at both
$N$. NO closed form has been derived yet — deriving one (from the pattern-conditional moments
of $Y_O$ under this probit-MAR design) or refuting its persistence is part of your task.

**C9 (scope).** The $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ deviance-bias theorem (FITTED
baseline) holds at leading order exactly for engines with $\Xi=o(1/n)$ per cell
("second-moment-matched to the MLE plug-in"): FITTED, bootstrap/EMB, recentred posterior
draws. Genuine Bayesian posterior draws have $\Xi=\operatorname{Var}(\mu^\ast)+b_\Sigma\succ0$
by construction (their predictive over-dispersion is what Rubin's between-imputation variance
captures) and carry the C4 discount; the magnitude is prior-dependent only through $b_\Sigma$
(consistent with brms $-1.36$ vs Jeffreys $-0.78$ at $N{=}200$).

### Evidence (exact-identity evaluation over parameter draws only — no imputation MC; all
values $/\operatorname{tr}(\mathrm{RIV})$, mean (se) over datasets)

Production, MAR:

| quantity | $N{=}200$ ($R{=}240/120$) | $N{=}1000$ ($R{=}160/60$) | engine-measured (round 1) |
|---|---|---|---|
| E1 full | $-0.1236\,(22)$ | $-0.1220\,(47)$ | $-0.121\ldots-0.123$; asymptote $-0.106$ |
| E1 $\mu$-only draw | $-0.1010\,(2)$ | $-0.1010\,(2)$ | — |
| analytic $-\operatorname{tr}(\mathrm{RIV}_{\mu\mu})/2\operatorname{tr}$ | $-0.1011$ | $-0.1011$ | — |
| E1 $\Sigma$-only draw | $-0.0209\,(21)$ | $-0.0207\,(46)$ | — |
| E2 full | $-0.7867\,(60)$ | $-0.7589\,(130)$ | $-0.783\,(23)$; asymptote $-0.74$ |
| E2 matrix-recentred | $-0.1497\,(24)$ | $-0.1380\,(15)$ | (scalar-deflated arm: $-0.244$) |
| E2 $b_\Sigma$ contraction | $-0.6493\,(48)$ | $-0.6230\,(125)$ | — |
| E2 master ($b{+}\operatorname{Var}\mu$) | $-0.7643\,(50)$ | $-0.7329\,(127)$ | — |
| E2 $n\kappa$ (diag-avg) | $7.066\,(36)$ | $6.734\,(88)$ | complete-data $(p{+}2)=6$ |
| E3 full | $-0.0884\,(77)$ | $-0.0673\,(195)$ | Amelia $-0.087\,(25)$; $-0.019$ @ $N{=}2000$ |
| E3 $b_\Sigma$ contraction | $+0.0707\,(62)$ | $+0.0726\,(196)$ | — |
| E3 $\mu$-wander | $-0.1137\,(10)$ | $-0.1099\,(10)$ | — |
| E3 master | $-0.0430\,(66)$ | $-0.0373\,(196)$ | — |

MCAR discriminator ($N{=}200$, $R{=}240/60$): E1 full $-0.1183\,(21)$, $\mu$-only
$-0.1006\,(2)$, $\Sigma$-only $-0.0160\,(21)$; E2 full $-0.7276\,(78)$, recentred
$-0.1144\,(27)$; E3 full $-0.0455\,(104)$.

$\Sigma$-only split (E1; "imbalance" = contraction against
$\sum r_Or_O^\top-n_{\text{pat}}\hat\Sigma_{OO}$; "matched" = the C3-cancelling pair;
"b-shift" = the finite-$S$ Monte-Carlo mean of the drawn $\Sigma^\ast$ bias, shared seeds
across cells):

| cell | $\Sigma$-only | imbalance | matched | b-shift | matched$-$b-shift |
|---|---|---|---|---|---|
| MAR $200$ | $-0.0209\,(21)$ | $-0.0049\,(12)$ | $-0.0159\,(18)$ | $-0.0028\,(18)$ | $-0.0131$ |
| MAR $1000$ | $-0.0207\,(46)$ | $-0.0065\,(5)$ | $-0.0142\,(47)$ | $-0.0118\,(47)$ | $-0.0024$ |
| MCAR $200$ | $-0.0160\,(21)$ | $+0.0003\,(11)$ | $-0.0163\,(18)$ | $-0.0029\,(18)$ | $-0.0134$ |
| MCAR $1000$ | $-0.0137\,(47)$ | $+0.0003\,(6)$ | $-0.0140\,(47)$ | $-0.0116\,(47)$ | $-0.0024$ |

PD-rejection rate for E1: $0.0000$ at every cell. The interpretation under audit: imbalance is
the persistent MAR-only IMB; matched$-$b-shift is the genuine higher-order transient (decays
$\approx5.4\times$ from $N{=}200$ to $N{=}1000$); the b-shift column is a mean-zero shared-draw
MC fluctuation (same seeds reproduce the same $-0.012$ excursion in MAR and MCAR at
$N{=}1000$).

### Your tasks

- **B1.** Verify or refute C1–C4 line by line (the identity, the derivatives, the concavity
  sign, the cancellation, the order bookkeeping, the $\mu$-block contraction). Any refutation
  needs explicit algebra.
- **B2.** Verify C5 and C6, including: the $(p{+}2)$-vs-$(p{+}1)$ baseline question; whether a
  persistent skew/shape term is truly impossible; whether "anisotropic residual of scalar
  deflation" fully accounts for the round-1 deflated arm at $-0.244$; whether the E2 recentred
  values ($-0.150/-0.138$) vs E1 ($-0.124/-0.122$) residual $\approx-0.02$ is consistent with
  the claimed finite-$n$ terms or signals something persistent that the recentring missed.
- **B3.** Verify C7. In particular: is the missing-data statement
  $\Xi_{\text{E3}}=\widehat{\mathrm{Bias}}^\ast(\hat\Sigma_{\text{obs}})+\operatorname{Var}^\ast(\tilde\mu)$
  with $\mu$-part cancellation correct, and is the leftover really the non-$\mu$ Cox–Snell bias
  part? Could the E3 floor instead be persistent at a larger value than claimed?
- **B4.** C8 is the weakest link: derive a closed form for IMB under this probit-MAR design
  (the pattern-conditional moments of $Y_O$ are computable: $R_1$ depends on $X_3$ only, $R_2$
  on $X_4$ only), or show IMB should vanish and the measured $-0.005/-0.0065$ has another
  source. Check its claimed engine-universality (it depends on the draw's $\Sigma$-covariance,
  not its mean).
- **B5.** Attack C9's scope statement: construct, if you can, an engine with
  $\Xi=o(1/n)$ per cell whose $D$ does NOT vanish, or an engine with $\Xi\not=o(1/n)$ whose
  $D$ does — i.e., test necessity and sufficiency. Also state whether "second-moment-matched"
  is the right condition to put in a manuscript, or whether a cleaner equivalent exists.
- **B6.** List anything in the evidence tables inconsistent with C1–C9 that the interpretation
  glossed over.

Deliverable: a claim-by-claim verdict table (SUSTAIN / REFUTE / ESCALATE with one-line reason),
then the algebra for every refutation/escalation, then your C8 derivation (or impossibility
argument), then an overall verdict: do these results, as scoped by C9, survive adversarial
audit for inclusion in a derivation manuscript?

---

## GRADING KEY (never transmitted — the runner truncates the package at this header)

Expected Mode-A landings (grade independence of derivation, not wording):

1. **A1:** the exact per-unit identity of C1 (equivalently the $M_{2,i}$ second-moment form).
   Key steps: $[\hat\Sigma^{-1}]_{MM}=\hat V^{-1}$ and the vanishing cross term.
2. **A2:** the controlling functional $\Xi=b_\Sigma+\operatorname{Var}(\mu^\ast)$ (any
   equivalent form), with E1 $\to-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$
   ($\approx-0.101$ given the $\mu$ share; the share itself was withheld from Mode A — landing
   the OBJECT suffices), E2 $\to$ E1 value minus the $b_\Sigma$ contraction with complete-data
   $\kappa=(p{+}2)/n$ (accept $(p{+}1)$ only if explicitly tied to the $S_{n-1}$ baseline and
   corrected), E3 $\to0$ via the second-moment identity.
3. **A3:** concavity/DEFLATION (not inflation), and the exact cancellation against the
   $\Sigma$-mean-wander; exactness under MCAR. A blind reproduction of round 1's "Jensen
   inflation" claim is a FAIL on this item.
4. **A4:** the $\Xi=o(1/n)$-per-cell class ("second-moment-matched"); bootstrap in, Bayes out;
   mechanism = the divisor-$n$ deflation vs posterior over-dispersion.
5. **A5:** a MAR-only imbalance cross term of the C8 structure (order $10^{-2}$ or below at
   this design). Full credit for the structure; the $-0.006$ value was withheld.

Partial-credit note: the known-scale anchor hands Mode A the $\mu$-wander term; credit for C5
therefore requires the $\Sigma$-side cancellation argument, not just the $\mu$-block. Mode-A
"artifact" verdicts against any of the four measured branches count as escalations and are
triaged against the exact-identity evaluator
(`verification/spikes/audit-engine-formula.R`, cache
`verification/cache/spikes/audit-engine-formula.rds`) before acceptance.

Escalation policy (both modes): any refutation with algebra goes back through the evaluator
(which computes D from parameter draws alone — imputation-free, so sampler bugs are out of
scope for it) and through the p=1 closed-form toy (Jeffreys: $-1$; Laplace: $-1/4$; bootstrap:
$0$, all exact at leading order, all reproduced). A Mode-B SUSTAIN across C1–C7 + any verdict
on C8 clears the gate; C8's closed form is a welcome bonus either way. Gate artifacts:
todo/040-audit-response-fable5.md (the claims), this package, and the two response files under
verification/cache/.
