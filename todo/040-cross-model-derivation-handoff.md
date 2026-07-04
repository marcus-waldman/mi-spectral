# Cross-model derivation audit — handoff

**Topic.** An empirical finding from the mi-spectral project's Phase-0 data-augmentation (DA)
spike appears to contradict the paper's headline for one class of imputation engine. We need a
frontier-model derivation audit to decide whether it is (i) a separable, prior-dependent
finite-sample term that leaves the leading-order theorem intact, or (ii) a genuine qualification
of the "holds for proper multiple imputation" claim.

**How to use this file.** It is self-contained. Read §1–§5, then answer Q1–Q4 in §6. The setup,
theorem, and the numbers in §4 are all real and reproduced by two independent engines; nothing
here is hypothetical. Be adversarial: if the finding is an artifact of our sampler, say why with
a derivation; if it is real, say what it implies for the theorem's scope. Show the algebra for the
leading-order claim in Q1 — that is the load-bearing step.

---

## 1. Setup and notation

- Data are $n$ i.i.d. draws from a $p$-variate normal $N(\mu,\Sigma)$, $p=4$, parameter
  $\theta=(\mu,\operatorname{vech}\Sigma)$, $k=p+p(p+1)/2=14$. Some entries are missing at random
  (MAR); the analysis model is the unstructured MVN (so the imputer is congenial with it).
- $\hat\theta_{\text{obs}}$ = observed-data MLE (EM/FIML). $\hat\theta_{\text{com}}$ =
  complete-data MLE on the fully-observed $X$.
- $I_{\text{com}}$, $I_{\text{obs}}$ = complete- and observed-data expected Fisher information;
  $I_{\text{mis}\mid\text{obs}}=I_{\text{com}}-I_{\text{obs}}$;
  $\mathrm{RIV}=I_{\text{obs}}^{-1}I_{\text{com}}-I_k$, $\operatorname{tr}(\mathrm{RIV})=
  \operatorname{tr}(I_{\text{obs}}^{-1}I_{\text{com}})-k$.
- The MI Q-function (infinite-imputation limit), with imputation parameter $\tilde\phi$:
  $$\bar Q_\infty(\theta)=\mathbb{E}_{\tilde\phi}\,\mathbb{E}_{Y_{\text{mis}}\mid Y_{\text{obs}},\tilde\phi}
  \big[\ell_{\text{com}}(\theta;Y_{\text{obs}},Y_{\text{mis}})\big].$$
- The deviance-bias objects and their headline targets (congenial, **estimated-scale** MVN):
  $$T=\bar Q_\infty(\hat\theta_{\text{obs}})-\ell_{\text{com}}(\hat\theta_{\text{com}}),\quad
    A=\bar Q_\infty(\hat\theta_{\text{obs}})-\ell_{\text{com}}(\hat\theta_{\text{obs}}),\quad
    B=\ell_{\text{com}}(\hat\theta_{\text{obs}})-\ell_{\text{com}}(\hat\theta_{\text{com}}).$$
  $T=A+B$. Headline: $\mathbb{E}[A]=+\operatorname{tr}(\mathrm{RIV})$,
  $\mathbb{E}[B]=-\tfrac12\operatorname{tr}(\mathrm{RIV})$, so
  $\mathbb{E}[T]=+\tfrac12\operatorname{tr}(\mathrm{RIV})$ (plus an $O(1)$ MAR design-imbalance
  term $(A)+(C)$, immaterial to this audit — it is common across the engines compared below).

## 2. How the derivation (manuscript/derivation.qmd) treats "proper MI"

Verbatim positions from `manuscript/derivation.qmd`:

- **@sec-qfun (D9), lines 383–394.** $\tilde\phi$ is "under congenial proper MI a draw from the
  imputation posterior fit to $Y_{\text{obs}}$, **centered at $\hat\theta_{\text{obs}}$**"; "the
  inner expectation conditions on the *fitted* $\tilde\phi\approx\hat\theta_{\text{obs}}$."
- **Fitted-vs-oracle callout, lines 404–425.** $\bar Q_\infty$ averages over the *fitted*
  imputation law $P(\cdot\mid Y_{\text{obs}},\tilde\phi)$ with
  $\tilde\phi\approx\hat\theta_{\text{obs}}$ — **not** the oracle law at $\theta_0$ (which would
  give the tower-property $\mathbb{E}[A]=0$ and $\mathbb{E}[T]=-\tfrac12\operatorname{tr}(\mathrm{RIV})$).
  It concludes: "imputing from the fitted $\hat\theta_{\text{obs}}$ — **deterministic FIML and
  proper MI alike** — gives $\mathbb{E}[A]=+\operatorname{tr}(\mathrm{RIV})$ and the total
  $+\tfrac12\operatorname{tr}(\mathrm{RIV})$."
- **Known-scale case, lines 750–766.** When $\Sigma$ is *known* (location-only fit), the two
  arms separate:
  $\mathbb{E}[T]_{\text{known scale}}=0$ (deterministic FIML) vs $-\tfrac12\operatorname{tr}(\mathrm{RIV})$
  (proper MI), "the two arms differing by the posterior-draw imputation variance
  $C_n=\tfrac12\operatorname{tr}(\mathrm{RIV})$ — so deterministic FIML and proper MI are **not**
  interchangeable for a known-scale fit." This is verified with a genuine posterior-draw engine
  (see §3).

**Crucial detail about the paper's proper-MI construction.** The one place the paper actually runs
a posterior-draw ("proper") sampler is the *known-scale* experiment
`verification/rederivation-knownvar.R`. There the posterior draw is
$$\tilde\mu \sim N(\hat\theta_{\text{obs}},\,I_{\text{obs}}^{-1}),$$
i.e. a **Gaussian posterior centered at the MLE** (the Laplace / Bernstein–von Mises
approximation), $\Sigma$ held fixed. For a location parameter this is exact (posterior mean = MLE).
The analytic proper value is $\bar Q_{\text{proper}}=\bar Q_{\text{fiml}}-C_n$ with
$C_n=\tfrac12\sum_i\operatorname{tr}(\Sigma_0^{-1}H_i\,\Phi\,H_i^\top)$, $\Phi=I_{\text{obs}}^{-1}$.

**What was NOT run.** For the **estimated-scale** $+\tfrac12\operatorname{tr}(\mathrm{RIV})$
headline, no exact posterior-draw DA engine was used. The $+\tfrac12$ value is verified by
(a) the deterministic-FIML plug-in $\bar Q_{\text{fiml\_analytic}}(\hat\theta_{\text{obs}},
\hat\theta_{\text{obs}},\cdot)$ (imputation parameter fixed at $\hat\theta_{\text{obs}}$),
(b) the analytic conditional-entropy plug-in bias $\Delta_n=\tfrac12\operatorname{tr}(\mathrm{RIV})
+[(A)+(C)]$, and (c) the W1 simulation with **Amelia** (EMB = bootstrap + EM), which lacks a
prior. The step $\tilde\phi\approx\hat\theta_{\text{obs}}$ is an assumption, not a tested identity,
for the estimated-scale regime.

## 3. The empirical finding (Phase-0, todo/040 §8; all reproduced)

We built an exact conjugate Bayesian DA imputer for the MVN missing-data model under the standard
reference prior $p(\mu,\Sigma)\propto|\Sigma|^{-(p+1)/2}$: I-step draws $Y_{\text{mis}}\mid
Y_{\text{obs}},\theta$ (conditional normal); P-step draws
$\Sigma\sim\text{Inv-Wishart}(n-1,\,SS)$, $\mu\mid\Sigma\sim N(\bar y,\Sigma/n)$, $SS=$
completed-data sum of squares. Standard Tanner–Wong / Schafer data augmentation.

On the W1 cell ($N=200$, MAR, non-monotone), paired to the exact FITTED value
$T_{\text{fiml}}=\bar Q_{\text{fiml\_analytic}}(\hat\theta_{\text{obs}},\hat\theta_{\text{obs}},\cdot)
-\ell_{\text{com}}(\hat\theta_{\text{com}})$ and normalized by $\operatorname{tr}(\mathrm{RIV})$:

All values are paired to the exact FITTED value per replicate and normalized by
$\operatorname{tr}(\mathrm{RIV})$. N=200 unless noted; $R$ = replications.

| imputation engine | prior on $\Sigma$ | $(\,\mathbb{E}[T]-\mathbb{E}[T_{\text{fiml}}]\,)/\operatorname{tr}(\mathrm{RIV})$ |
|---|---|---|
| exact conjugate DA | Jeffreys $|\Sigma|^{-(p+1)/2}$ | **−0.783** (se .0023, $R{=}20000$) |
| **Schafer `norm::da.norm`** | Jeffreys | **−0.783** (se .0031, $R{=}10000$) |
| **brms / Stan** (joint MVN, HMC) | weakly-informative (LKJ(1) + half-$t$) | **−1.36** (se .15, $R{=}6$ — estimate) |
| conjugate DA, IW **re-centered at the MLE** ($\mathbb{E}[\Sigma\mid Y]=S$) | — | **−0.244** (se .0020, $R{=}20000$) |
| direct Gaussian posterior $\theta\!\sim\!N(\hat\theta_{\text{obs}},I_{\text{obs}}^{-1})$ | Laplace/BvM (MLE-centered) | **−0.121** (se .0020, $R{=}20000$) |
| Amelia EMB (bootstrap + EM) | none (frequentist) | **−0.087** (se .0025, $R{=}20000$) |

- **The two independent Jeffreys-IW engines are identical** — hand-rolled conjugate $-0.783$ and
  Schafer's `norm::da.norm` $-0.783$ agree to the third decimal at $R{=}10^4$. The finding is a
  property of the METHOD, not the implementation. brms, under a completely different
  weakly-informative prior, is also on the branch ($-1.36$; prior-dependent magnitude). The two
  MLE-centered constructions — Amelia's bootstrap ($-0.087$) and the Gaussian/Laplace posterior
  ($-0.121$) — sit near zero (small, but at $R{=}20000$ resolved below zero,
  $\approx-0.1\operatorname{tr}(\mathrm{RIV})$). So the divergence is **not** a Jeffreys-improper-prior
  artifact; it is general to drawing $\Sigma$ from a real Bayesian posterior rather than centering
  it at the MLE.
- **Decomposition of the $-0.783$ (conjugate, Jeffreys), $R{=}20000$:**
  (i) the $\Sigma$ posterior-**mean** inflation $\tfrac{n-1}{n-p-2}$ dominates —
  removing it (deflated arm) moves $-0.783\to-0.244$, i.e. $\approx-0.539$ ($\sim$69%);
  (ii) a higher-order IW-shape term (deflated $-0.244$ vs MLE-centered Gaussian $-0.121$)
  $\approx-0.122$ ($\sim$16%); (iii) a small baseline parameter-draw term carried even by the
  MLE-centered Gaussian/Laplace construction, $\approx-0.12$ ($\sim$15%). Mean-inflation is the
  dominant but not sole driver.
- **N-persistence (conjugate):** $-0.783,\,-0.766,\,-0.764,\,-0.746$ at $N=200,500,1000,2000$
  ($R=20000,10000,5000,2500$; se $.002,.004,.009,.017$). A small, now-resolved downward drift
  ($\sim$2σ), but a fit $a+b/n$ gives asymptote $a\approx-0.74$ with $b\approx-8$ — i.e. it
  **converges to a nonzero constant $\approx-0.74$**, it does NOT vanish (an $O(1/n)$ term would
  have fallen $\sim$10× to $\approx-0.08$ by $N{=}2000$). The term is **persistent,
  $O(\operatorname{tr}(\mathrm{RIV}))$, coefficient $\approx-0.74$**.
- **The two "correctly-centered" proper engines DIVERGE as $n\to\infty$** (paired FITTED-relative
  gap $(T-T_{\text{fiml}})/\operatorname{tr}(\mathrm{RIV})$, tight at all $N$; $R$ up to $8000$):

  | engine | $N{=}200$ | $500$ | $1000$ | $2000$ | $a+b/n$ limit |
  |---|---|---|---|---|---|
  | Amelia (bootstrap EMB) | $-0.099$ | $-0.047$ | $-0.029$ | $-0.019$ | $\to \mathbf{0}$ (≈$-0.01$) |
  | Gaussian/Laplace draw $N(\hat\theta_{\text{obs}},I_{\text{obs}}^{-1})$ | $-0.123$ | $-0.104$ | $-0.099$ | $-0.108$ | $\to \mathbf{-0.106}$ (persistent) |

  **Amelia — the engine the paper actually validated with — converges to FITTED/$+\tfrac12$** (its
  $N{=}200$ shortfall is a finite-$n$ $O(1/n)$ term that vanishes). But the **correct Laplace
  posterior draw persists at $\approx-0.11$** even though it is MLE-centered with no prior
  inflation. That persistent $-0.11$ is the **Jensen effect of imputing with a *drawn* covariance**:
  $\mathbb{E}[\Sigma_{M\mid O}(\Sigma^\ast)]>\Sigma_{M\mid O}(\hat\Sigma)$ because the conditional
  (Schur) covariance is nonlinear in $\Sigma$, and $O(1/n)$/cell × $O(n)$ cells $=O(1)$. The IW's
  $-0.74$ = this Jensen term ($-0.11$) + IW skew ($-0.12$) + the removable mean-inflation ($-0.54$).
  **The open mechanistic puzzle: why does the bootstrap (Amelia) uniquely escape the Jensen term
  and converge, while every genuine Bayesian posterior draw (Gaussian, IW, brms) carries a
  persistent $O(\operatorname{tr}(\mathrm{RIV}))$ discount?**
- **The direct Gaussian-posterior sampler** — which IS the paper's known-scale construction
  ($N(\hat\theta_{\text{obs}},I_{\text{obs}}^{-1})$) generalized to include $\Sigma$ — gives
  $-0.14$, close to Amelia's $-0.10$ and far from the exact-IW $-0.79$. So the paper's
  Laplace-posterior "proper MI" construction is internally consistent with the Amelia validation;
  the divergence is specifically **exact Inverse-Wishart posterior vs Gaussian/Laplace posterior**.
- **Mechanism (dominant part; see the decomposition above).** The Jeffreys IW posterior mean of
  $\Sigma$ is inflated, $\mathbb{E}[\Sigma\mid Y]=SS/(n-p-2)=\tfrac{n-1}{n-p-2}\,S$. This inflates
  the imputation conditional variance by $O(p/n)$ per missing cell; summed across the $O(n)$
  missing cells it is an $O(\operatorname{tr}(\mathrm{RIV}))$ downward shift of
  $\bar Q_\infty(\hat\theta_{\text{obs}})$. Removing it (the deflated arm, $\mathbb{E}[\Sigma\mid
  Y]=S$) accounts for $\approx69\%$ of the conjugate effect ($-0.783\to-0.244$); the remaining
  $\approx-0.244$ is a higher-order IW-shape term ($\approx-0.12$) plus the small baseline
  parameter-draw term ($\approx-0.12$) the MLE-centered constructions also carry.
- **Engine correctness controls (all pass).** The I-step is exact (fixing $\theta=\hat\theta_{\text{obs}}$
  and drawing only $Y_{\text{mis}}$ reproduces the deterministic FITTED value to
  $-0.04\pm0.17$). The conjugate chain's marginal $\theta^\ast$ dispersion matches analytic
  $I_{\text{obs}}^{-1}$ (relative Frobenius 0.15 vs $I_{\text{obs}}^{-1}$, 0.33 vs
  $I_{\text{com}}^{-1}$). Amelia's own $\tilde\theta$ dispersion also matches $I_{\text{obs}}^{-1}$
  (ratio 1.03) — i.e. Amelia is **not** under-propagating *parameter* uncertainty; the dominant
  difference between Amelia and the IW DA is the posterior *mean* of $\Sigma$.

## 4. The precise tension

The derivation asserts (estimated scale) that $\tilde\phi\approx\hat\theta_{\text{obs}}$ makes
proper MI behave like deterministic FIML ($\mathbb{E}[T]=+\tfrac12\operatorname{tr}(\mathrm{RIV})$).
The high-power N-scan (§3) shows this is engine-dependent:

- **Amelia's bootstrap EMB converges to FITTED** ($-0.099\to 0$ as $n$ grows, $\sim O(1/n)$). The
  paper validated the headline with Amelia, so its empirical claim is asymptotically sound.
- **Every genuine Bayesian posterior draw carries a *persistent* $O(\operatorname{tr}(\mathrm{RIV}))$
  discount** that does not vanish: the correct MLE-centered Gaussian/Laplace draw $\to-0.11$
  (pure Jensen effect — imputing with a *drawn* $\Sigma$ inflates $\mathbb{E}[\Sigma_{M\mid O}]$
  because the Schur complement is nonlinear in $\Sigma$); the Jeffreys IW $\to-0.74$ (Jensen +
  IW-skew + the $\tfrac{n-1}{n-p-2}$ mean-inflation); brms weakly-informative $-1.36$ at $N{=}200$.

So the reviewer's "standard data augmentation engine" (a Bayesian DA — `norm`/Schafer, brms,
mice) sits on a persistent branch, while the paper's validated Amelia converges to the headline.
This mirrors the paper's own **known-scale** result (proper MI $\neq$ deterministic FIML, differ by
$C_n$) — but there $\Sigma$ is fixed, so there is no draw-$\Sigma$ Jensen term. For **estimated**
scale the paper argues proper $=$ fitted; that holds for the *bootstrap* engine but not for any
*Bayesian posterior-draw* engine, where the draw-$\Sigma$ Jensen term (and, under an improper
prior, the mean-inflation) persists.

The sharp open question this raises: **why does the bootstrap (Amelia) escape the Jensen term and
converge to FITTED, while the Gaussian/Laplace, IW, and HMC posterior draws all retain a persistent
$O(\operatorname{tr}(\mathrm{RIV}))$ discount?** Both propagate the same $I_{\text{obs}}^{-1}$
parameter variance; they differ in how $\Sigma$'s draw enters the imputation's conditional
covariance.

## 5. Reproduction

```
verification/da-conjugate-engine.R                 impute_mvn_conjugate() (Jeffreys IW DA)
verification/spikes/phase0a-da-conjugate.R          R=100 conjugate vs Amelia vs analytic
verification/spikes/diag-fitted-vs-proper.R         fixed-theta = FITTED control
verification/spikes/diag-tiebreak.R                 Amelia theta-tilde dispersion + gauss-post sampler
verification/spikes/diag-localize.R                 per-cell over-dispersion localization
verification/spikes/diag-nscaling.R                 N=200/500/1000 + deflated-IW arm
verification/spikes/phase0a-confirm-xl.R            100x run: R=20000 magnitude + N-persistence + norm parallel
verification/spikes/phase0a-calibrated.R           paired FITTED-relative amelia/gauss N-persistence (the Q2 divergence)
verification/rederivation-knownvar.R                paper's proper-MI (Gaussian, known-scale)
verification/rederivation-L0-fitted-vs-oracle.R     paper's FITTED / oracle / Delta_n checks
manuscript/derivation.qmd  @sec-qfun (379–426), known-scale (748–769), C_n (1160–1194)
```

## 6. Questions to answer (Q1–Q4)

**Q1 (the load-bearing derivation).** Derive the leading-order coefficient of
$\mathbb{E}[T_{\text{proper,IW}}]-\mathbb{E}[T_{\text{fitted}}]$ where $T_{\text{proper,IW}}$ uses
an exact Jeffreys-prior Inverse-Wishart posterior draw of $\Sigma$ (mean $\tfrac{n-1}{n-p-2}S$) and
$T_{\text{fitted}}$ fixes $\tilde\phi=\hat\theta_{\text{obs}}$. **Empirically this difference is
persistent, not vanishing**: normalized by $\operatorname{tr}(\mathrm{RIV})$ it converges to
$\approx-0.74$ (values $-0.783,-0.766,-0.764,-0.746$ at $N=200,500,1000,2000$, $R$ up to $2\times10^4$;
a fit $a+b/n$ gives $a\approx-0.74$; an $O(1/n)$-only term would have fallen $\sim$10× to
$\approx-0.08$ by $N{=}2000$). The two independent Jeffreys engines (conjugate, `norm::da.norm`)
agree to the third decimal ($-0.783$). Derive this $O(\operatorname{tr}(\mathrm{RIV}))$ coefficient
and check it against the measured decomposition: the $\Sigma$ posterior-mean inflation
$\tfrac{n-1}{n-p-2}$ should contribute the dominant $\approx69\%$ ($-0.539$ of $-0.783$), with the
remainder from the higher-order IW shape ($\approx-0.12$) and a baseline parameter-draw term
($\approx-0.12$). If instead you can
show the effect *should* vanish and our simulation is being misread, show where. Give the algebra
and the closed-form coefficient (in terms of $p$, the missing pattern, and the per-cell missing
information).

**Q1b (the Jensen term — also load-bearing).** The MLE-centered Gaussian/Laplace draw
$\theta^\ast\sim N(\hat\theta_{\text{obs}},I_{\text{obs}}^{-1})$ has NO prior mean-inflation, yet
its $(T-T_{\text{fitted}})/\operatorname{tr}(\mathrm{RIV})$ **persists at $\approx-0.106$** (does not
vanish; §3 table). Our claim is that this is the Jensen term
$\tfrac12\sum_{\text{cells}}\operatorname{tr}\!\big(\hat\Sigma_{M\mid O}^{-1}\,
\mathbb{E}[\Sigma_{M\mid O}(\Sigma^\ast)-\Sigma_{M\mid O}(\hat\Sigma)]\big)$, an $O(1/n)$-per-cell ×
$O(n)$-cell $=O(1)$ effect from the nonlinearity (Schur complement) of $\Sigma_{M\mid O}$ in
$\Sigma$. Derive its coefficient and confirm/refute the persistence.

**Q2 (the anomaly — why does Amelia converge?).** Amelia's bootstrap EMB **converges to FITTED**
($-0.099\to 0$, $\sim O(1/n)$), while the Gaussian/Laplace, IW, and brms posterior draws all
retain a persistent discount. All propagate the same $I_{\text{obs}}^{-1}$ parameter variance
(measured: Amelia's $\tilde\theta$ dispersion ratio $1.03$ vs $I_{\text{obs}}^{-1}$). Why does the
bootstrap escape the draw-$\Sigma$ Jensen term while genuine Bayesian draws do not? Is it that the
bootstrap $\tilde\Sigma$ (an MLE on resampled data, divisor $n$) carries a compensating $-O(1/n)$
finite-sample deflation that cancels the Jensen inflation, whereas a posterior draw symmetric about
$\hat\Sigma$ does not? This determines which engine class the theorem is really a theorem about.

**Q3 (scope of the theorem).** Given Q1/Q1b/Q2, state precisely which construction of "proper MI"
the $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ leading-order theorem is a theorem about. Is the
correct reading "holds for proper MI whose imputation parameter is a consistent, MLE-centered draw
with no draw-$\Sigma$ Jensen inflation (bootstrap/EMB, or a bias-corrected posterior)" — with the
Bayesian-posterior-draw discount (Jensen $\approx-0.11$; + prior mean-inflation under Jeffreys)
being a separable, characterizable term to disclose? Is any of this recognized in the MI literature
(Rubin 1987; Meng 1994; Schafer 1997 DA vs the Bayesian bootstrap / EMB)?

**Q4 (recommended action).** For the paper and the response to reviewer r1#8 (who asked to confirm
the headline under "a standard data augmentation engine"): (a) scope the theorem to the
bootstrap/EMB (MLE-centered) construction the paper validated, and report the Bayesian-posterior-draw
term (Jensen + prior mean-inflation) as an additional, disclosed, characterized correction —
noting the applied model-selection direction is unharmed (the term scales with each candidate's own
$\operatorname{tr}(\mathrm{RIV})$, reinforcing the high-RIV-favoring bias); (b) treat it as a genuine
problem requiring the theorem restated to cover Bayesian DA; or (c) something else. Justify from
Q1–Q3.

Please show the Q1 algebra explicitly.
