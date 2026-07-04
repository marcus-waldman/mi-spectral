# todo/045b — Layer-3 cross-model gate: canonical-GLM FITTED-arm deviance gap (todo/045 Q2 3a)

**Provenance.** The todo/045 investigation (Phase-3 Bernoulli HARKing adjudication, quorum
determination AMENDED with OBJ-05/06/07/08) required a real derivation of whether the paper's
$+\tfrac12\operatorname{tr}(\mathrm{RIV})$ FITTED-arm result holds for a Bernoulli/logit GLM.
The in-repo derivation (Fable 5, max effort, 2026-07-04; `todo/045` §3.1) answers yes via a new
cancellation lemma, plus a nonzero base-measure correction for Poisson and a proper-draw
discount corollary — all CAS-verified (`verification/cas-wolfram/verify_bernoulli_fitted_gap.py`).
Per the standing cross-model protocol those new derivations get an independent off-lineage check
BEFORE any manuscript-facing text is rewritten. Mode A is the blinded independent re-derivation
that quorum objection OBJ-05 said was missing (for this claim; the original Phase-3 registration
stays reported as a miss).

**How to run (already launched 2026-07-04, backgrounded).** The runner sends each mode as its
own API call and hard-truncates this file at the grading-key banner, so the key is never
transmitted:

```
py verification/run_layer3_openai.py gpt-5.5-pro --effort xhigh --timeout 86400 \
    --package todo/045b-gpt55-gate-package.md --tag -bern-glm
```

Outputs land at `verification/cache/layer3-gpt-5.5-pro-bern-glm-modeA.md` / `-modeB.md`.

**What "pass" means.** Mode A (blind) independently lands the same structure: the Bernoulli
asymptote, the base-measure dependence for Poisson (sign and mechanism), the proper-draw
discount, and the known-scale location values. Mode B (red-team) sustains claims C1–C8, or its
refutations are triaged against the CAS script and the exact enumerations and win only if they
survive that. Any sustained refutation reopens todo/045 §3.1 before anything lands in the
manuscript.

---

## MODE A — blind derivation (no access to our answers; derive from scratch)

You are auditing a statistical derivation at maximum reasoning effort. Work from first
principles. Show all algebra. Derive; do not pattern-match.

### Setup

Data: $N$ i.i.d. pairs $(x_i, Y_i)$. The response follows a one-parameter exponential family
with CANONICAL link,
$$ f(y\mid x;\beta)=h(y)\exp\{y\eta - A(\eta)\},\qquad \eta = x^\top\beta,\quad \beta\in\mathbb{R}^q, $$
with $x^\top=(1, x)$ (intercept plus one covariate, $q=2$), $x\sim N(0,1)$, true
$\beta_0=(0.3,\,0.9)$. The covariate is always observed; the response $Y$ is missing completely
at random (MCAR) with rate $r=0.22$, independently of everything. So the observed-data MLE
$\hat\beta_{\text{obs}}$ is the complete-case MLE, and the complete-data MLE
$\hat\beta_{\text{com}}$ uses all $N$ responses (which exist in the simulation).

Multiple imputation, congenial (imputation model = analysis model), in the FITTED /
deterministic-FIML arm: missing responses are drawn from $f(\cdot\mid x_i;\hat\beta_{\text{obs}})$,
and the number of imputations is taken to infinity, so each missing unit contributes its exact
expectation $\mathbb{E}_{\tilde Y\sim f(\cdot;\hat\beta_{\text{obs}})}[\log f(\tilde Y\mid x_i;\hat\beta_{\text{obs}})]$
to the averaged completed-data log-likelihood $\bar Q_\infty(\hat\beta_{\text{obs}})$ (observed
units contribute their actual log-density at $\hat\beta_{\text{obs}}$).

The statistic of interest is
$$ T \;=\; \bar Q_\infty(\hat\beta_{\text{obs}}) \;-\; \ell_{\text{com}}(\hat\beta_{\text{com}}), $$
where $\ell_{\text{com}}$ is the complete-data log-likelihood of all $N$ actual responses. Define
the informations at $\beta_0$: $I_{\text{com}} = \mathbb{E}[\sum_{i=1}^N A''(\eta_i)x_ix_i^\top]$,
$I_{\text{obs}} = (1-r)I_{\text{com}}$ (MCAR), $I_{\text{mis}} = I_{\text{com}}-I_{\text{obs}}$,
and $\operatorname{tr}(\mathrm{RIV}) = \operatorname{tr}(I_{\text{obs}}^{-1}I_{\text{mis}}) = q\,r/(1-r)$.

Background you may take as given (it is published work of the paper under audit): for the
multivariate normal with estimated covariance, $\mathbb{E}[T] = +\tfrac12\operatorname{tr}(\mathrm{RIV}) + O(1/N)$
under MCAR; for a known-scale location-only fit, $\mathbb{E}[T]=0$ (this FITTED arm) and
$-\tfrac12\operatorname{tr}(\mathrm{RIV})$ (proper posterior-draw MI). Do NOT assume either
value transfers to the families below; derive what actually happens.

### Questions

**A1.** Derive $\mathbb{E}[T]$ to $O(1)$ (i.e., keep all $O(1)$ terms, drop $O(1/N)$) for the
general canonical family above, as a function of the design distribution and the family
$(A, h)$. State explicitly whether and how the answer depends on the base measure $h$, and
through which mechanism the MLE's $O(1/N)$ bias enters at $O(1)$. Give the coefficient of
$\operatorname{tr}(\mathrm{RIV})$ and any additional terms in closed form (population
functionals are fine).

**A2.** Instantiate for Bernoulli with the logit link ($h\equiv1$): what is
$\lim_{N\to\infty}\mathbb{E}[T]/\operatorname{tr}(\mathrm{RIV})$ at the stated design? A number.

**A3.** Instantiate for Poisson with the log link ($h(y)=1/y!$): does the limit equal
Bernoulli's? If not, give the extra term's closed-form structure (in terms of
$g(\eta):=\mathbb{E}_\eta[\log h(Y)]$ and the design), and determine its SIGN at the stated
design if you can.

**A4.** Now replace the FITTED arm by a proper-draw arm: for each imputation, first draw
$\beta^\ast\sim N(\hat\beta_{\text{obs}},\, I_{\text{obs}}^{-1})$, then impute missing responses
from $f(\cdot\mid x_i;\beta^\ast)$; $\bar Q_\infty$ is still evaluated at
$\hat\beta_{\text{obs}}$. Derive
$\lim_{N\to\infty}\mathbb{E}[T_{\text{draw}}-T_{\text{fitted}}]/\operatorname{tr}(\mathrm{RIV})$
in closed form for the general canonical family, and give the number for the Bernoulli design.

**A5.** For a Student-$t$ location family with fixed scale and degrees of freedom
($y = \mu + \sigma t_\nu$, only $\mu$ estimated, $\sigma=1$, $\nu=5$, no covariate), state
$\lim \mathbb{E}[T_{\text{fitted}}]/\operatorname{tr}(\mathrm{RIV})$ and
$\lim \mathbb{E}[T_{\text{draw}}]/\operatorname{tr}(\mathrm{RIV})$ (draws
$\mu^\ast\sim N(\hat\mu_{\text{obs}}, I_{\text{obs}}^{-1})$). Justify briefly from your A1
mechanism.

Show your work. If your derivation produces a result that contradicts the background MVN claim's
naive extrapolation, say so plainly — the point of this audit is to find what is actually true.

<!-- MODE-A END -->

## MODE B — red-team the in-repo derivation

You are auditing the following derivation adversarially at maximum reasoning effort. For each
enumerated claim: SUSTAIN (with a proof sketch of why it is right), or REFUTE (with explicit
algebra locating the error), or ESCALATE (state exactly what additional check would decide it).
Do not defer to authority; the derivation was produced by another AI and has passed a CAS check
whose scope you should also scrutinize (e.g., does the CAS verify the claim actually needed, or
a neighboring identity?).

### The setting

[Identical to Mode A's Setup — canonical one-parameter exponential-family GLM, $\eta=x^\top\beta$,
$x^\top=(1,x)$, $x\sim N(0,1)$, $\beta_0=(0.3,0.9)$, $q=2$, response-only MCAR at $r=0.22$,
FITTED arm with $M=\infty$ (analytic anchor $-H_i(\hat\beta_{\text{obs}})$ per missing unit),
$T=\bar Q_\infty(\hat\beta_{\text{obs}})-\ell_{\text{com}}(\hat\beta_{\text{com}})$,
$\operatorname{tr}(\mathrm{RIV})=qr/(1-r)$.]

### The derivation under audit (claims C1–C8)

Notation: $w=A''$, $A'''$ the third derivative, $g(\eta)=\mathbb{E}_\eta[\log h(Y)]$,
$\Omega=\mathbb{E}[wXX^\top]$ at $\beta_0$ with $X^\top=(1,x)$,
$J_\bullet=\sum_\bullet w_ix_ix_i^\top$ realized informations, $\delta=\hat\beta_{\text{obs}}-\beta_0$.

- **C1.** $\mathbb{E}[\ell_{\text{com}}(\hat\beta_{\text{obs}})-\ell_{\text{com}}(\hat\beta_{\text{com}})]
  = -\tfrac12\operatorname{tr}(\mathrm{RIV}) + O(1/N)$, with no family-specific $O(1)$ term (the
  third-order Taylor terms contribute $O(1/N)$ because $\mathbb{E}[(x^\top\delta)^3]=O(N^{-2})$).
- **C2.** The imputation-bias term decomposes as
  $\mathbb{E}[\bar Q_\infty(\hat\beta_{\text{obs}})-\ell_{\text{com}}(\hat\beta_{\text{obs}})]
  = \operatorname{tr}(\mathrm{RIV}) + (A) + (C) + O(1/N)$ with
  $(A)=\alpha^\top\mathbb{E}[\delta]$, $\alpha=\sum_{\text{mis}}(g'_i+\eta_iw_i)x_i$, and
  $(C)=\tfrac12\operatorname{tr}(\mathcal H_\phi J_{\text{obs}}^{-1})$,
  $\mathcal H_\phi=\sum_{\text{mis}}(g''_i+\eta_iA'''_i)x_ix_i^\top$.
- **C3.** For a canonical link, $\mathbb{E}[\delta] = -\tfrac12 J_{\text{obs}}^{-1}
  \sum_{j\in\text{obs}}A'''_j\,(x_j^\top J_{\text{obs}}^{-1}x_j)\,x_j + O(N^{-2})$.
- **C4 (Lemma P).** $\mathbb{E}[\eta wX^\top]\,\Omega^{-1}\,\mathbb{E}[A'''(X^\top\Omega^{-1}X)X]
  = \mathbb{E}[\eta A'''(X^\top\Omega^{-1}X)]$ exactly, for any design distribution and any
  $A$, because $\eta=X^\top\beta_0$ and $\Omega=\mathbb{E}[wXX^\top]$; consequently the
  $(\eta w,\eta A''')$ parts of $(A)$ and $(C)$ cancel at $O(1)$ under MCAR, leaving
  $(A)+(C)=\Delta_h+O(1/N)$ with
  $\Delta_h=\tfrac{r}{1-r}\big[-\tfrac12\mathbb{E}[g'X^\top]\Omega^{-1}\mathbb{E}[A'''(X^\top\Omega^{-1}X)X]
  +\tfrac12\mathbb{E}[g''X^\top\Omega^{-1}X]\big]$.
- **C5.** Bernoulli/logit has $h\equiv1$, so $\Delta_h=0$ and
  $\mathbb{E}[T_{\text{fitted}}]=+\tfrac12\operatorname{tr}(\mathrm{RIV})+O(1/N)$ — the
  multivariate-normal headline value transfers exactly to this family (mechanism: a Cox–Snell /
  cross-entropy-curvature cancellation, not the MVN's Wishart log-determinant identity).
- **C6.** Poisson/log has $g(\eta)=-\mathbb{E}_{\mu=e^\eta}[\log Y!]$ with
  $g'(\eta)=-\mu\,\mathbb{E}[\log(Y+1)]$ and
  $g''(\eta)=-\mu\,\mathbb{E}[\log(Y+1)]-\mu^2\,\mathbb{E}[\log\tfrac{Y+2}{Y+1}]$ (derived from
  $\partial_\mu P_k = P_{k-1}-P_k$); Gauss–Hermite quadrature at the stated design gives
  $\Delta_h/\operatorname{tr}(\mathrm{RIV})=-0.396$ (bias part $+0.688$, curvature part
  $-1.084$), so the Poisson FITTED limit is $+0.104$, not $+0.5$.
- **C7.** The proper-draw arm ($\beta^\ast\sim N(\hat\beta_{\text{obs}},I_{\text{obs}}^{-1})$,
  $\bar Q$ still evaluated at $\hat\beta_{\text{obs}}$) satisfies
  $\mathbb{E}[T_{\text{draw}}-T_{\text{fitted}}]
  = \tfrac{r}{2(1-r)}\,\mathbb{E}[(g''+\eta A''')(X^\top\Omega^{-1}X)] + O(1/N)$ — i.e. exactly
  the $(C)$ functional once more, because the draw doubles the variance entering $(C)$ and
  changes nothing else at $O(1)$. At the Bernoulli design this equals
  $K/(2q)\cdot\operatorname{tr}(\mathrm{RIV})$ with
  $K=\mathbb{E}[\eta A'''X^\top\Omega^{-1}X]=-1.042$, i.e. a discount ratio $-0.261$.
- **C8.** Student-$t$ location with fixed $(\sigma,\nu)$: the conditional missing-data entropy is
  constant in $\mu$, so FITTED $\to 0$ and the proper draw $\to-\tfrac12\operatorname{tr}(\mathrm{RIV})$,
  matching the paper's known-scale collapse.

Evidence the derivation cites (scrutinize the SCOPE of each): a sympy check of the entropy
identities and of Lemma P (symbolic 3-point design + 12 exact-rational 4-point designs); exact
finite-$n$ enumerations for the intercept-only Bernoulli design (ratio $\to\tfrac12$, residual
$\approx0.59/n$) and a two-point $x=\pm1$ design (exact $\mathbb{E}[\hat\beta]$ matches C3's
formula to 2% at $n_g=240$; ratio $\to\tfrac12$); Gauss–Hermite quadrature for the constants in
C6/C7. Also: an N=200 Monte-Carlo (R=1000) measured FITTED ratio $+0.846$ (se $0.161$) and
paired draw-FITTED ratio $-0.223$ (se $0.022$) BEFORE this derivation existed; an N-scan to
discriminate "large finite-N constant" from "wrong asymptote" is registered but had not run when
this package was written.

### Mode B questions

**B1.** Verdict on each of C1–C8 (sustain / refute / escalate), with algebra for any refutation.

**B2.** The single most likely error, if there is one: is Lemma P's cancellation actually the
right pairing — i.e., does $(A)$ use the SAME $J_{\text{obs}}$-weighted geometry as $(C)$ at the
$O(1)$ order, including the $J_{\text{all}}$-vs-$J_{\text{obs}}$ distinction in
$\alpha=\sum_{\text{mis}}(\cdot)$ vs $b$'s $\sum_{\text{obs}}(\cdot)$, under MCAR where
$\Sigma_{\text{mis}} \approx \tfrac{r}{1-r}\Sigma_{\text{obs}}$? Check the bookkeeping.

**B3.** C7 claims the draw arm adds exactly one extra copy of $(C)$'s functional. Verify the
variance bookkeeping: FITTED has $\operatorname{Var}(\tilde\phi)=\operatorname{Var}(\hat\beta_{\text{obs}})$
already inside $(C)$; the draw adds $I_{\text{obs}}^{-1}$ on top. Does the Term-A main piece
(the $\operatorname{tr}(\mathrm{RIV})$ cross term) really stay unchanged (the draw noise is
independent of $\hat\beta_{\text{obs}}$)?

**B4.** Is there any additional $O(1)$ term the decomposition misses for a DISCRETE response —
e.g., from the non-smoothness of the MLE map on lattice data, from the separation event, or from
the anchor's exactness claim $\bar Q_\infty$-per-missing-row $=-H_i(\hat\beta_{\text{obs}})$?

**B5.** The finite-$N$ story: the measured $N{=}200$ FITTED ratio is $+0.846$ (se $0.161$)
against the claimed asymptote $+0.5$. Is an $O(1/N)$ term with constant $\approx 70$ on the
ratio scale plausible for this design given the intercept-only exact constant is $\approx0.6$
and the two-point design's $\approx1.6$? What design feature (if any) could inflate it by two
orders of magnitude — or should we expect the true ratio at $N=200$ to be much closer to $0.5$
than the noisy point estimate suggests?

## GRADING KEY (never transmitted; for scoring the responses)

Mode A expected landings: A1 = $\tfrac12\operatorname{tr}(\mathrm{RIV})+\Delta_h$ with the
$(A)$-vs-$(C)$ cancellation (Lemma P) and $h$ entering only through $g$; the MLE bias enters via
$\alpha^\top\mathbb{E}[\delta]$ with $\alpha=O(N)$ extensive in $n_{\text{mis}}$. A2 = $+0.5$.
A3 = NOT equal; extra term $\Delta_h/\operatorname{tr}(\mathrm{RIV})$, negative at this design
($-0.396$; curvature part dominates the bias part). A4 = $\mathbb{E}[(g''+\eta A''')X^\top\Omega^{-1}X]/(2q)$;
Bernoulli $=-0.261$. A5 = $0$ and $-\tfrac12$.

Mode B: C1–C8 all believed correct (CAS + exact enumerations); B2's bookkeeping is the sharpest
place to look (the $(1-r)$ factors cancel between $b\propto 1/n_{\text{obs}}$ and
$\Sigma_{\text{mis}}\propto rN$; verified in the exact two-point enumeration); B4's anchor
exactness is an identity ($\mathbb{E}_{f_\theta}[\log f_\theta]=-H$), the separation event is
exponentially rare and $T$ stays bounded on it; B5's honest answer is "the scan decides — the
exact-design constants are small, so a large part of the $+0.35$ excess is plausibly Monte-Carlo
noise (2.1 se), and the registered N-scan (R=200k at N=200) settles it."
