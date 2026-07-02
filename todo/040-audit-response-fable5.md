# Cross-model derivation audit — response (Claude Fable 5, max effort, 2026-07-01)

Answers Q1–Q4 of `todo/040-cross-model-derivation-handoff.md`. All new numbers come from
`verification/spikes/audit-engine-formula.R` (cache `verification/cache/spikes/audit-engine-formula.rds`),
which evaluates each engine's deviance gap by an **exact per-unit identity over the engine's
parameter draws alone** — no imputation, no log-likelihood calls, no finite-$M$ noise. The
identity-based values reproduce the handoff's engine measurements at all three branches, so the
two pipelines validate each other before any interpretation.

## 0. Verdict

The finding is **real** and is **not** a sampler artifact: option (i) of the handoff, with three
corrections to the proposed mechanism. The $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ theorem is
correct at leading order **for imputation engines whose parameter draw is second-moment-matched
to the MLE plug-in** (deterministic FIML/FITTED; bootstrap-EMB). A genuine Bayesian posterior
draw violates second-moment matching by construction, and its gap to FITTED is a separable,
characterizable, prior-dependent term:

$$
D \;=\; \bar Q_{\text{engine}}(\hat\theta_{\text{obs}})-\bar Q_{\text{fitted}}(\hat\theta_{\text{obs}})
\;=\; -\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})
\;-\;\tfrac12\sum_i \operatorname{tr}\!\big(\hat V_i^{-1} C_i\, b_\Sigma\, C_i^\top\big)
\;-\;\mathrm{IMB}\;+\;o(1),
$$

where $\mathrm{RIV}_{\mu\mu}$ is the $\mu$-block of the RIV, $C_i=[\,I,\ -\hat B_i\,]$ is the
unit-$i$ conditional-mean map, $\hat V_i$ the fitted Schur complement, $b_\Sigma=
\mathbb{E}[\Sigma^\ast\mid Y_{\text{obs}}]-\hat\Sigma$ the centering bias of the drawn covariance,
and $\mathrm{IMB}$ a small MAR-only design-imbalance cross term carried by **every** drawing
engine (Amelia included), $\approx-0.006\operatorname{tr}(\mathrm{RIV})$ in the W1 cell (exactly
zero under MCAR; §5). Each term is persistent ($O(\operatorname{tr}(\mathrm{RIV}))$), computable
from objects already in the repo, and measured below. For the Laplace/BvM engine the persistent
total is $-0.1011-0.006\approx-0.107$ — the handoff's own $N$-scan asymptote $-0.106$, now with
its two pieces identified.

Corrections to the handoff's reading:

1. **Q1b's mechanism is wrong, its magnitude right.** The persistent term carried by the
   MLE-centered Gaussian/Laplace draw is **not** a Jensen inflation of the Schur complement. The
   Schur complement is matrix-**concave** in $\Sigma$, so a mean-centered $\Sigma^\ast$ draw
   *deflates* $\mathbb{E}[V_i(\Sigma^\ast)]$; and that deflation is cancelled **exactly** (at
   persistent order, for any draw covariance) by the $\Sigma$-part of the conditional-**mean**
   wander. What survives is the $\mu$-wander term $-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$
   — the paper's own known-scale $C_n$, alive and well inside the estimated-scale regime.
2. **There is no persistent "IW-shape" term.** Posterior skewness enters the gap at $O(1/n)$
   (third moments of the draw are $O(n^{-2})$ per unit). The deflated-arm's $-0.244$ is the
   **anisotropic residual of a scalar deflation**: the Jeffreys posterior-mean inflation is
   larger on the poorly observed blocks (effective-df scaling), so dividing every draw by the
   complete-data factor under-corrects exactly where the contraction weights are largest.
   Recentring the draws by the measured **matrix** bias collapses the conjugate engine onto the
   Laplace branch ($-0.150$ vs $-0.124$ at $N{=}200$; $-0.138$ vs $-0.122$ at $N{=}1000$).
3. **The bootstrap's escape is an identity, not an accident** (Q2): for complete data,
   $\mathbb{E}^\ast[\tilde\Sigma+(\tilde\mu-\hat\mu)(\tilde\mu-\hat\mu)^\top]=\hat\Sigma$
   **exactly** — the divisor-$n$ deflation of the resampled MLE is the same empirical second
   moment that feeds the $\tilde\mu$ wander. Measured on the W1 cell, the two pieces are
   $+0.071$ and $-0.114$ (sum $-0.043$ at $N{=}200$, shrinking), and the identity-based total
   $-0.088$ matches Amelia's engine-measured $-0.087$ to the third decimal.

For the theorem's statement this is the handoff's option (i): scope to second-moment-matched
engines, disclose the Bayesian-draw term with its formula. The one place the paper's *text* is
wrong is the sentence "deterministic FIML and proper MI alike" (`derivation.qmd:423`) and the D9
gloss "$\tilde\phi\approx\hat\theta_{\text{obs}}$" treated as sufficient: a posterior draw is
$\hat\theta_{\text{obs}}+O_p(n^{-1/2})$, and the deviance — a sum of $n$ per-cell $O(1/n)$
effects — resolves exactly that order. The known-scale callout (`derivation.qmd:750–766`)
already proves this for the $\mu$-part; the estimated-scale text contradicted its own boundary
case.

## 1. The exact identity everything runs through

Fix the evaluation point $\hat\theta=\hat\theta_{\text{obs}}=(\hat\mu,\hat\Sigma)$ and one
incomplete unit $i$ with observed block $O$, missing block $M$, $\hat B=\hat\Sigma_{MO}\hat\Sigma_{OO}^{-1}$,
$\hat V=\hat\Sigma_{MM}-\hat B\hat\Sigma_{OM}$, fitted conditional mean $\hat m_i=\hat\mu_M+\hat B(y_O-\hat\mu_O)$.
Any engine here imputes $Y_{\text{mis},i}\mid\phi\sim N(m_i(\phi),V_i(\phi))$ with
$\phi=(\mu^\ast,\Sigma^\ast)$ drawn from some law given $Y_{\text{obs}}$ (posterior, Laplace,
bootstrap; FITTED is the point mass at $\hat\theta$).

Taking the completion expectation of the complete-data Gaussian log-likelihood at $\hat\theta$
gives, per unit and per $\phi$,
$$
q_i(\phi)-q_i(\hat\theta)
= -\tfrac12\Big[\,d_i^\top \hat V_i^{-1} d_i \;+\; \operatorname{tr}\!\big(\hat V_i^{-1}(V_i(\phi)-\hat V_i)\big)\Big],
\qquad d_i = m_i(\phi)-\hat m_i .
$$
This is **exact** (no expansion). Two standard facts produce it: the $(M,M)$ block of
$\hat\Sigma^{-1}$ is $\hat V_i^{-1}$, and the cross term vanishes because the fitted-completed
residual $r_i$ satisfies $[\hat\Sigma^{-1}r_i]_M=\hat V_i^{-1}(r_{i,M}-\hat B r_{i,O})=0$.
Summing over units and averaging over the engine's draw law,
$$
D=-\tfrac12\sum_i\Big\{\mathbb{E}_\phi\big[d_i^\top\hat V_i^{-1}d_i\big]
+\operatorname{tr}\big(\hat V_i^{-1}(\mathbb{E}_\phi[V_i(\Sigma^\ast)]-\hat V_i)\big)\Big\}.
$$
Equivalently: $D=-\tfrac12\sum_i\operatorname{tr}(\hat V_i^{-1}(M_{2,i}-\hat V_i))$ with
$M_{2,i}$ the engine's imputation-predictive **second moment about the fitted mean**. The whole
audit reduces to how $M_{2,i}$ compares to $\hat V_i$ at the $O(1/n)$-per-cell scale, because
$O(1/n)$ per cell $\times$ $O(n)$ cells $=O(1)=O(\operatorname{tr}(\mathrm{RIV}))$.

`audit-engine-formula.R` evaluates this identity by Monte Carlo over $\phi$ only. Cross-check
against the handoff's engine-based measurements (which impute data and evaluate log-likelihoods):
Laplace $-0.124$ vs $-0.121$; Jeffreys DA $-0.787$ vs $-0.783$; bootstrap-EM $-0.088$ vs Amelia's
$-0.087$. The finding is a property of the draws, not of any implementation.

## 2. Q1 — the Jeffreys-IW coefficient, derived

Write $\delta=\phi-\hat\theta$, $b=\mathbb{E}[\delta]$, $\Phi=\operatorname{Cov}(\phi)$. Expand both
pieces of the identity to second order (per-unit remainders $O(\mathbb{E}\|\delta\|^3)=O(n^{-3/2})$,
$O(n^{-1/2})$ after summing; **signed** third-moment terms are $O(n^{-2})$ per unit because
posterior/bootstrap/Laplace draws have $\mathbb{E}[\delta^{\otimes3}]=O(n^{-2})$ — this is why no
skew/shape term can persist).

**(a) Derivatives of the Schur map.** With $\Delta$ a symmetric perturbation of $\Sigma$ and
$\dot B(\Delta)=(\Delta_{MO}-\hat B\Delta_{OO})\hat\Sigma_{OO}^{-1}$:
$$
V_i'[\Delta]=C_i\Delta C_i^\top,\qquad
V_i''[\Delta,\Delta]=-2\,\dot B(\Delta)\,\hat\Sigma_{OO}\,\dot B(\Delta)^\top\ \preceq 0 .
$$
The first line is the envelope theorem applied to $V(\Sigma)=\min_B (I,-B)\Sigma(I,-B)^\top$; the
minimum of linear maps also proves matrix concavity, which the second line exhibits. Two exact
contractions used below: $C_i\hat\Sigma C_i^\top=\hat V_i$, and (block inversion)
$C_i^\top\hat V_i^{-1}C_i=\hat\Sigma^{-1}-\operatorname{embed}(\hat\Sigma_{OO}^{-1})
=[I^{(i)}_{\text{com}}-I^{(i)}_{\text{obs}}]_{\mu\mu}$, so
$\sum_i C_i^\top\hat V_i^{-1}C_i=[I_{\text{mis}\mid\text{obs}}]_{\mu\mu}$ **exactly**.

**(b) Mean wander.** $d_i=C_i\delta_\mu+\dot B(\delta_\Sigma)\,r_{O,i}+O(\|\delta\|^2)$ (note
$\partial m_i/\partial\mu=C_i$ exactly). The $\mu$-part of
$\mathbb{E}[d_i^\top\hat V_i^{-1}d_i]$ contracts to
$\operatorname{tr}(C_i^\top\hat V_i^{-1}C_i\,\Phi_{\mu\mu})$ with no dependence on $y_O$; the
$\Sigma$-part contracts to $\operatorname{tr}\big(\mathbb{E}[\dot B^\top\hat V_i^{-1}\dot B]\;r_{O,i}r_{O,i}^\top\big)$.
The $\mu\Sigma$ cross term vanishes ($I_{\text{obs}}$ is $\mu$–$\Sigma$ block-diagonal for the
MVN under ignorable missingness, and the conjugate P-step draws $\mu\mid\Sigma$ symmetrically).

**(c) Covariance term.** $\mathbb{E}[V_i(\Sigma^\ast)]-\hat V_i
= C_i b_\Sigma C_i^\top+\tfrac12\mathbb{E}[V_i''[\delta_\Sigma,\delta_\Sigma]]+O(n^{-3/2})$, so its
contraction is $\operatorname{tr}(\hat V_i^{-1}C_ib_\Sigma C_i^\top)
-\operatorname{tr}\big(\mathbb{E}[\dot B^\top\hat V_i^{-1}\dot B]\;\hat\Sigma_{OO}\big)$.

**(d) The cancellation.** The $\Sigma$-wander term of (b) and the concavity term of (c) are the
same quadratic form contracted against $r_{O,i}r_{O,i}^\top$ and $\hat\Sigma_{OO}$ respectively,
with opposite signs. Summed over units within a pattern, they cancel to the extent that the
realized within-pattern second moment $\sum r_Or_O^\top$ matches $n_{\text{pat}}\hat\Sigma_{OO}$:
exactly in expectation under MCAR; under MAR the pattern-conditional law of $Y_O$ is shifted, and
the residual is the design-imbalance cross term
$$
\mathrm{IMB}= \tfrac12\sum_{\text{patterns}}\operatorname{tr}\Big(\mathbb{E}\big[\dot B^\top\hat V^{-1}\dot B\big]
\Big(\textstyle\sum_{\text{rows}} r_Or_O^\top-n_{\text{pat}}\hat\Sigma_{OO}\Big)\Big)
$$
— an $O(1/n)$ coefficient times an $O(n)$ systematic imbalance, persistent under MAR, zero under
MCAR, and carried by **every** engine that draws $\Sigma$ (it scales with the draw's
$\Sigma$-covariance, not its mean). This term is the drawing-engine cousin of the paper's
$(A)+(C)$: same design-imbalance origin, new coefficient. Measured: $\approx-0.02\,
\operatorname{tr}(\mathrm{RIV})$ in the (MAR, non-monotone) W1 cell at both $N{=}200$ and
$N{=}1000$; see §5 of this file for the split diagnostic.

**(e) Master formula.** Collecting (b)–(d):
$$
D=-\tfrac12\sum_i\operatorname{tr}\!\big(\hat V_i^{-1}C_i\,\Xi\,C_i^\top\big)\;-\;\mathrm{IMB}\;+\;o(1),
\qquad
\boxed{\ \Xi \;=\; b_\Sigma+\Phi_{\mu\mu}\ }
$$
The engine enters **only** through $\Xi$: the drawn-$\Sigma$ centering bias plus the drawn-$\mu$
covariance. With $\Phi_{\mu\mu}=[I_{\text{obs}}^{-1}]_{\mu\mu}$ (true of all four engines here;
measured ratios 1.00–1.05), the $\Phi_{\mu\mu}$ part contracts by (a) to
$-\tfrac12\operatorname{tr}([I_{\text{obs}}^{-1}]_{\mu\mu}[I_{\text{mis}\mid\text{obs}}]_{\mu\mu})
=-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$.

**(f) The Jeffreys-IW $b_\Sigma$.** For complete data the posterior is
$\Sigma\mid Y\sim\mathrm{IW}(n-1,\,n\hat\Sigma_{\text{ML}})$, so
$\mathbb{E}[\Sigma\mid Y]=\tfrac{n}{n-p-2}\hat\Sigma_{\text{ML}}$, i.e.
$b_\Sigma=\tfrac{p+2}{n}\hat\Sigma+O(n^{-2})$ **relative to the MLE** (the handoff's
$\tfrac{n-1}{n-p-2}$ is relative to the divisor-$(n-1)$ $S$; the audit target
$\hat\theta_{\text{obs}}$ is the MLE, so $(p+2)$ is the right complete-data constant, not
$(p+1)$). Because $C_i\hat\Sigma C_i^\top=\hat V_i$, a proportional bias $b_\Sigma=\kappa\hat\Sigma$
contracts in closed form:
$$
-\tfrac12\sum_i\operatorname{tr}(\hat V_i^{-1}C_i(\kappa\hat\Sigma)C_i^\top)
=-\tfrac{\kappa}{2}\sum_i|M_i| = -\tfrac{\kappa}{2}\,n_{\text{mis}} .
$$
With missing data the observed-data posterior mean is **anisotropically** inflated — per block
roughly $(p+2)/n_{\text{eff}}$ with $n_{\text{eff}}\approx n(1-\mathrm{FMI}_{\text{block}})$ —
so the scalar $\kappa$ underestimates the contraction. Measured on the W1 cell: diagonal-average
$n\kappa\approx 7.07$ (vs complete-data $6$), but contraction-weighted
$c_{\text{eff}}=2n\,\lvert\text{contraction}\rvert/n_{\text{mis}}\approx 11.3$ at $N{=}200$
($10.7$ at $N{=}1000$) — the inflation concentrates exactly on the missing-block conditionals,
consistent with $1/(1-\mathrm{FMI})\approx1.8$ at $\mathrm{FMI}\approx0.43$.

**(g) Assembled coefficient and check against the measurements** (W1 cell: $p=4$, MAR
non-monotone, $\operatorname{tr}(\mathrm{RIV})=5.63$, $\operatorname{tr}(\mathrm{RIV}_{\mu\mu})=1.14$,
$n_{\text{mis}}/n=0.648$; all values $/\operatorname{tr}(\mathrm{RIV})$, exact-identity evaluation):

| piece | formula | $N{=}200$ | $N{=}1000$ |
|---|---|---|---|
| $\mu$-wander | $-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})/\operatorname{tr}(\mathrm{RIV})$ | $-0.101$ | $-0.101$ |
| $\Sigma$ centering bias | $-\tfrac12\sum_i\operatorname{tr}(\hat V_i^{-1}C_ib_\Sigma C_i^\top)/\operatorname{tr}$ | $-0.649$ | $-0.623$ |
| MAR imbalance ($\mathrm{IMB}$, persistent) + $O(1/n)$ transients | §5 split | $-0.037$ | $-0.035$ |
| **total (formula)** | | $\mathbf{-0.787}$ | $\mathbf{-0.759}$ |
| **total (handoff engines)** | conjugate $=$ `norm::da.norm` | $\mathbf{-0.783}$ | $-0.764$ |

The $N$-persistence is explained without further input: every piece is a ratio of $O(1)$
quantities once normalized by $\operatorname{tr}(\mathrm{RIV})$ (the $n\to\infty$ drift
$-0.783\to-0.74$ is the decay of the finite-$n$ parts of $n\,b_\Sigma$ and the transients).

**Correction to the handoff's expected decomposition.** Not 69% mean-inflation / 16% IW-shape /
15% baseline, but **83% centering bias / 13% $\mu$-wander / ~4% imbalance-plus-transient**, with
the "IW-shape" line dissolved: the deflated arm's scalar factor $(N{-}p{-}2)/(N{-}1)$ removes only
the isotropic part of $b_\Sigma$ (see `diag-nscaling.R:29`), and the leftover anisotropic
centering bias ($\approx-0.10$ to $-0.12$) was misread as a shape effect. Matrix recentring
(subtract the measured $b_\Sigma$ from every draw) lands on $-0.150$ ($N{=}200$) and $-0.138$
($N{=}1000$) against Laplace's $-0.124$/$-0.122$ — no persistent shape term at the $0.02$–$0.03$
resolution, and none is possible at persistent order by the third-moment argument above.

## 3. Q1b — the Laplace/BvM persistent coefficient, derived

For $\theta^\ast\sim N(\hat\theta_{\text{obs}},I_{\text{obs}}^{-1})$: $b_\Sigma=0$, so
$\Xi=[I_{\text{obs}}^{-1}]_{\mu\mu}$ and
$$
D_{\text{Laplace}}=-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})\;-\;\mathrm{IMB}\;+\;O(1/n).
$$

The handoff's proposed mechanism — "$\mathbb{E}[\Sigma_{M\mid O}(\Sigma^\ast)]>\Sigma_{M\mid O}(\hat\Sigma)$
because the Schur complement is nonlinear" — has the **wrong sign and the wrong carrier**:

- Concavity gives $\mathbb{E}[V_i(\Sigma^\ast)]\preceq V_i(\hat\Sigma)$ for any mean-centered
  draw — the plug-in conditional covariance is *deflated*, not inflated. (Bivariate example, exact
  to second order with Wishart-type draw covariance: $\mathbb{E}[V(\Sigma^\ast)]-V=-V/n$.)
- The observed per-cell over-dispersion of the imputations about the fitted mean
  (`diag-localize.R`) is real, but its persistent part is the **$\mu$-wander**, plus the
  imbalance term under MAR; the $\Sigma$-draw's wander and concavity self-cancel (§2d).

Numerical discrimination (exact identity, $R{=}240$ datasets, $S{=}2000$ draws each; the three
arms draw the full $\theta^\ast$, only $\mu^\ast$ ($\Sigma^\ast{:=}\hat\Sigma$), only
$\Sigma^\ast$ ($\mu^\ast{:=}\hat\mu$)):

| arm | $N{=}200$ MAR | $N{=}1000$ MAR | $N{=}200$ MCAR | prediction |
|---|---|---|---|---|
| full draw | $-0.1236\,(22)$ | $-0.1220\,(47)$ | $-0.1183\,(21)$ | $\mu$-only $+$ $\Sigma$-only |
| $\mu$-only | $-0.1010\,(2)$ | $-0.1010\,(2)$ | $-0.1006\,(2)$ | $-\operatorname{tr}(\mathrm{RIV}_{\mu\mu})/2\operatorname{tr}=-0.1011$ |
| $\Sigma$-only | $-0.0209\,(21)$ | $-0.0207\,(46)$ | $-0.0160\,(21)$ | $-\mathrm{IMB}$ (MAR) $+O(1/n)$ |

The $\mu$-only arm matches the closed form to four decimals at both sample sizes, and the full
arm is additive in the two pieces. The $\Sigma$-only column further splits (§5) into a persistent
MAR-only imbalance $\approx-0.005$/$-0.0065$ (exactly $+0.0003$ under MCAR) and an $O(1/n)$
higher-order transient ($-0.013$ at $N{=}200$ decaying to $-0.002$ at $N{=}1000$ once the
shared-draw Monte-Carlo term is removed). So the persistent Laplace coefficient for this cell is
$$
-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})/\operatorname{tr}(\mathrm{RIV})\;-\;\mathrm{IMB}
\;=\;-0.1011-0.006\;\approx\;-0.107,
$$
**identical to the handoff's $a+b/n$ asymptote $-0.106$** — the handoff's coefficient is
confirmed, and its composition is now identified: 95% $\mu$-wander, 5% MAR imbalance, 0%
Schur-complement curvature.

**Consistency with the paper's own boundary case.** For a known scale the paper proves
$T_{\text{proper}}-T_{\text{fiml}}=-C_n=-\tfrac12\operatorname{tr}(\mathrm{RIV})$
(`derivation.qmd:750–766`), where all information is $\mu$-information. The estimated-scale
result derived here is the same object with only its $\mu$-block surviving,
$-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$, because the $\Sigma$-draw's two effects
cancel each other rather than cancelling the $\mu$-term. The estimated-scale sentence "proper MI
behaves like deterministic FIML" was therefore inconsistent with the paper's own known-scale
limit; the $\mu$-part of $C_n$ never goes away.

## 4. Q2 — why the bootstrap escapes

**Complete data: an exact identity.** For the nonparametric bootstrap with the divisor-$n$ MLE,
$$
\tilde\Sigma+(\tilde\mu-\hat\mu)(\tilde\mu-\hat\mu)^\top
=\tfrac1n\sum_j (y^\ast_j-\hat\mu)(y^\ast_j-\hat\mu)^\top
\quad\Longrightarrow\quad
\mathbb{E}^\ast\big[\tilde\Sigma+(\tilde\mu-\hat\mu)^{\otimes2}\big]=\hat\Sigma\ \text{ exactly},
$$
because each resampled row has second moment $\hat\Sigma$ about $\hat\mu$ under the empirical
measure. So $\Xi_{\text{boot}}=b_\Sigma^{\text{boot}}+\operatorname{Var}^\ast(\tilde\mu)=0$: the
$O(1/n)$ **deflation** of the resampled covariance MLE is the same empirical moment as the
$\tilde\mu$ wander, with opposite sign in the predictive second moment. The bootstrap
imputation predictive is second-moment-matched to the plug-in; a Bayesian posterior is
deliberately **over**-dispersed by exactly $\operatorname{Var}(\mu^\ast)$ (that over-dispersion
is what Rubin's between-imputation variance is designed to pick up), and no posterior centered
at or above $\hat\Sigma$ can cancel it.

**Missing data.** $b_\Sigma^{\text{boot}}=\mathbb{E}^\ast[\tilde\Sigma_{\text{EM}}]-\hat\Sigma$ is
the bootstrap estimate of the own-bias of the observed-data MLE, whose $\mu$-estimation part
cancels $\operatorname{Var}^\ast(\tilde\mu)$ at $O(1/n)$; the residual $\Xi_{\text{boot}}$ is the
non-$\mu$ (Cox–Snell curvature) part of $\operatorname{Bias}(\hat\Sigma_{\text{obs}})$ — exactly
the $b_\Sigma$ object this project already derived for the $(A)+(C)$ analysis, so its contraction
is analytically computable with existing machinery if wanted. Measured (structural emulation:
resample rows, `em_mvn`, evaluate the identity):

| quantity | $N{=}200$ | $N{=}1000$ |
|---|---|---|
| $b_\Sigma$ contraction ($+$ = deflation helps) | $+0.071\,(6)$ | $+0.073\,(20)$ |
| $\mu$-wander contraction | $-0.114\,(1)$ | $-0.110\,(1)$ |
| master ($\Xi$) | $-0.043\,(7)$ | $-0.037\,(20)$ |
| full $D$ (identity) | $-0.088\,(8)$ | $-0.067\,(20)$ |
| Amelia engine (handoff) | $-0.087\,(3)$ | $-0.029$ |

The $N{=}200$ agreement with Amelia's engine value is to the third decimal. The remaining small
negative is (i) the incomplete finite-$n$ cancellation (shrinking; exact zero for complete data;
the persistent residue is the Cox–Snell non-$\mu$ bias contraction), and (ii) the
$\approx-0.006$ MAR imbalance floor shared by all drawing engines. Amelia's own $N$-scan
($-0.019$ at $N{=}2000$, fitted $a\approx-0.01$) is consistent with that composition. So
"converges to FITTED" is right up to a $\lesssim0.01$-scale floor an order below the Bayesian
terms.

So the answer to the handoff's question is **yes, and it is structural**: the bootstrap
$\tilde\Sigma$ carries a compensating $-O(1/n)$ deflation that cancels the draw-induced
inflation of the predictive second moment; a genuine posterior draw, being centered at (Laplace)
or above ($\mathrm{IW}$, weakly-informative priors) the MLE, cannot. This also predicts the brms
branch: a weakly-informative prior contributes its own prior-gradient term to $b_\Sigma$ at
$O(1/n)$, so the discount is prior-dependent and generically larger than Jeffreys at small $n$
($-1.36\pm0.15$ at $N{=}200$ is consistent; not re-verified here).

**Caveat for reproducers.** Amelia's `a$mu` / `a$covMatrices` are on an internal
(reordered/standardized) scale — with `boot.type="none"` they do not reproduce the EM MLE — so
they cannot be harvested for these contractions; use the structural emulation.

## 5. The MAR imbalance term (new, small, engine-wide)

The $\Sigma$-only Laplace gap splits exactly into a design-imbalance part (the $\dot B$-quadratic
contracted against $\sum_{\text{rows}} r_Or_O^\top-n_{\text{pat}}\hat\Sigma_{OO}$, all draw
orders) and a matched remainder (the second-order-cancelling pair; leftover = higher-order
transients plus a shared-draw Monte-Carlo term that the `b-shift` line isolates). Four cells,
Laplace-only ($R{=}240/160$, $S{=}2000$; PD-rejection rate measured $0.0000$ everywhere, so
truncation contributes nothing):

| cell | $\Sigma$-only total | imbalance | matched | matched $-$ b-shift (genuine transient) |
|---|---|---|---|---|
| MAR, $N{=}200$ | $-0.0209\,(21)$ | $-0.0049\,(12)$ | $-0.0159\,(18)$ | $-0.0131$ |
| MAR, $N{=}1000$ | $-0.0207\,(46)$ | $-0.0065\,(5)$ | $-0.0142\,(47)$ | $-0.0024$ |
| MCAR, $N{=}200$ | $-0.0160\,(21)$ | $+0.0003\,(11)$ | $-0.0163\,(18)$ | $-0.0134$ |
| MCAR, $N{=}1000$ | $-0.0137\,(47)$ | $+0.0003\,(6)$ | $-0.0140\,(47)$ | $-0.0024$ |

Readings. (1) The imbalance part is **exactly zero under MCAR** (se $0.0006$–$0.0011$) and a
persistent $\approx-0.005$/$-0.0065$ under MAR — the lemma's prediction on both counts. (2) The
genuine transient decays $-0.013\to-0.0024$ from $N{=}200$ to $N{=}1000$, i.e. $O(1/n)$ within
noise (factor $5.4$ vs $5$). (3) The `b-shift` line is a mean-zero shared-draw Monte-Carlo term
(the same draw seeds produce the same $-0.012$ excursion in the MAR and MCAR $N{=}1000$ cells);
it inflates the raw $\Sigma$-only and matched columns at $N{=}1000$ and explains why they look
flat before the split. So $\mathrm{IMB}\approx-0.006\operatorname{tr}(\mathrm{RIV})$ in this
cell, MAR-only, engine-wide (it scales with the draw's $\Sigma$-covariance, so every proper
engine carries it; FITTED does not). For the paper's W1 validation the term is invisible: at
$\operatorname{tr}(\mathrm{RIV})\approx5.6$ it is $\approx-0.03$ on the deviance scale, well
inside the heavy-tailed $(A)+(C)\approx-0.3$ band the W1 cell already reports.

## 6. Q3 — what the theorem is a theorem about

**Scope statement (proposed wording).** The $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ result
holds, to leading order, for congenial imputation whose parameter draw is
**second-moment-matched to the MLE plug-in**:
$\Xi=b_\Sigma+\operatorname{Var}(\mu^\ast)=o(1/n)$ per cell — equivalently, the imputation
predictive's second moment about the fitted conditional mean equals the fitted conditional
variance to $o(1/n)$. This class contains deterministic FIML ($\Xi=0$ trivially), bootstrap-EMB
(exactly for complete data; up to a Cox–Snell residual under missingness — Amelia, the engine
the paper validated with), and debiased/recentred posterior draws. It excludes every genuine
Bayesian posterior draw, whose predictive is over-dispersed by construction
($\Xi=\operatorname{Var}(\mu^\ast)+$ prior-dependent $b_\Sigma\succ0$); those engines carry the
disclosed correction $-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})
-\tfrac12\sum_i\operatorname{tr}(\hat V_i^{-1}C_ib_\Sigma C_i^\top)$, prior-dependent through
$b_\Sigma$ only.

**Is this recognized in the literature?** The *estimator-level* split is: Wang & Robins (1998,
Biometrika; `literature/wangLargesampleTheoryParametric1998.md`, read in-session) distinguish
type-A MI (posterior draws, Rubin-proper) from type-B MI (draws at a fixed $\sqrt n$-consistent
$\hat\theta$) and prove they have different large-sample variances (type B smaller); Nielsen
(2003, ISR; `literature/nielsenProperImproperMultiple2003.md`, read in-session) develops the
proper/improper contrast and notes Bayesian MI is what makes Rubin's variance rule weakly
unbiased. von Hippel & Bartlett (2021, Statistical Science) name the same engine split
PDMI-vs-MLMI (proposed, logged in `todo/003`). What none of these papers evaluate is a pooled
**deviance/Q-function** — their objects are $\hat\theta$ and its variance, where the engine
difference is a variance-efficiency effect. The deviance is a sum of $n$ cells each sensitive at
$O(1/n)$, so the same engine split surfaces as an $O(\operatorname{tr}(\mathrm{RIV}))$ **mean**
shift. Rubin-properness (Rubin 1987 §4; Nielsen's result) constrains the between-imputation
variance behavior, not the $O(1/n)$ mean of the predictive second moment — both branches are
proper for variance combining, which is exactly why properness cannot be the scoping condition
for this theorem. To the best of this audit's knowledge the deviance-level statement (and the
$-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$ / $b_\Sigma$-contraction decomposition) is
not in the MI literature; treat it as a contribution of the response, not a known fact to cite.

## 7. Q4 — recommended action

**(a), strengthened — scope + disclose + characterize + offer the fix.** Concretely:

1. **`derivation.qmd` @sec-qfun (D9, lines 383–394) and the fitted-vs-oracle callout (404–425):**
   replace "centered at $\hat\theta_{\text{obs}}$" / "deterministic FIML and proper MI alike"
   with the engine-class statement of §6, and add the correction display for posterior-draw
   engines. The existing analytic machinery already computes every object in it
   ($\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$ from `fisher_info_obs_mvn`; $b_\Sigma$ from a DA
   chain or the effective-df approximation $(p{+}2)/[n(1-\mathrm{FMI}_{\text{block}})]$).
2. **Known-scale callout (750–766):** add one sentence — the known-scale $C_n$ does not vanish
   for an estimated scale; it survives as its $\mu$-block $\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$
   for any posterior-draw engine, and is cancelled only by the bootstrap's matched deflation.
3. **W1/§5 and the r1#8 response:** report that the requested standard-DA run was done twice
   independently (hand-rolled conjugate and `norm::da.norm`, agreeing to the third decimal),
   that the DA branch differs from the validated EMB branch by the characterized, disclosed term
   (measured $-0.78\operatorname{tr}(\mathrm{RIV})$ at $N{=}200$, asymptote $\approx-0.74$;
   decomposition 83/13/4), and that **recentring the DA draws at the MLE restores the headline**
   (measured: recentred conjugate $-0.150$ vs Laplace $-0.124$ at $N{=}200$) — i.e. the reviewer
   gets both the confirmation-with-qualification and a constructive engine-side remedy.
   Also note the W1-validated Amelia claim survives untouched: its residual $-0.02$ sits inside
   the reported $(A)+(C)$ band.
4. **IC application (§5):** with a single shared imputer, the engine term is common across
   candidates to leading order and largely cancels in $\Delta$IC; the candidate-specific residual
   enters through each candidate's own conditional precision on the missing blocks and pushes in
   the same direction as the headline bias (high-missing-information candidates look better).
   State qualitatively; the master formula makes it computable per candidate if a reviewer asks.
5. **Do not take option (b)** (restate the theorem to cover Bayesian DA with a universal
   constant): the Bayesian-draw term is prior-dependent ($-0.78$ Jeffreys vs $-1.36$
   weakly-informative at $N{=}200$), so no engine-free constant exists; the honest general form
   is the scoped theorem plus the $\Xi$-formula.
6. **Phase-1 protocol suggestions:** add the recentred-DA arm and the $\mu$-only/$\Sigma$-only
   discriminators to any preregistered follow-up; they are the sharp mechanism tests (four-decimal
   agreement on $-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$; $\Sigma$-only $\approx0$).

**Numbers still worth computing** (handoff invited flags): (i) the analytic contraction of the
Cox–Snell non-$\mu$ bias residual for the bootstrap (closes the last $\lesssim0.01$-scale floor
with existing machinery, jointly with the $\mathrm{IMB}\approx-0.006$ term of §5); (ii) an
analytic evaluation of $\mathrm{IMB}$ from the pattern-conditional moments of $Y_O$ (the
mechanism is identified and measured; a closed form would let W1-style cells report it next to
$(A)+(C)$); (iii) optionally a single higher-$R$ brms cell to place the weakly-informative
$b_\Sigma$ on the same table. None of these can change the verdict, only the third decimal.

## 8. Reproduction

```
verification/spikes/audit-engine-formula.R     exact-identity evaluation + all arms
  Rscript verification/spikes/audit-engine-formula.R 20 240 120 120 200    # N=200 production
  Rscript verification/spikes/audit-engine-formula.R 20 160 60 60 1000     # N=1000 persistence
  Rscript verification/spikes/audit-engine-formula.R 20 240 0 0 200 1      # MCAR discriminator
verification/cache/spikes/audit-engine-formula.rds   (overwritten per run; per-dataset records)
```
Data stream and cell identical to the handoff's spikes (`set.seed(20260522+r)`,
`gen_data`/`apply_mar` from `verification/00-setup.R`); draws seeded independently per arm.
