# todo/040 — derivation.qmd amendment, staged draft (NOT landed)

**Status: DRAFT, gate returned MIXED (2026-07-02).** This stages the exact text Fable's audit
(`todo/040-audit-response-fable5.md`, commit `cc62ad7`) recommends for `manuscript/derivation.qmd`.
The GPT-5.5 Pro xhigh gate (`todo/040b-gpt55-gate-package.md`; responses at
`verification/cache/layer3-gpt-5.5-pro-da-engine-mode{A,B}.md`) ran 2026-07-02 and did **not**
clear cleanly per the package's own escalation policy ("A Mode-B SUSTAIN across C1–C7... clears
the gate"): Mode A (blind) independently reproduced the core mechanism (Schur concavity —
deflation not inflation, corrects round 1; E2≈7×E1 via a Σ-centering constant of 0/(p+2)/−1 for
Laplace/Jeffreys/bootstrap; E3→0 exactly). Mode B (red-team) sustained C1/C2/C4/C5, escalated
C3 (wording only — "exact under MCAR" needs an asymptotic qualifier)/C6/C7, and **refuted C9 as
literally stated** (the scope condition in Amendment 2 below). C8 (IMB) came back SUSTAIN with a
genuine closed-form derivation (Tallis truncated-bivariate-normal moments for this exact
probit-MAR design) — this closes the open "IMB closed form" charter question as a bonus.

**Triage against the escalation policy (in progress):**
- **C9 (scope condition) — REVISION REQUIRED, done below.** Mode B constructed three
  counterexamples: (1) a μ-fixed, Σ-only-drawn engine has Ξ=0 but D≠0 under MAR because IMB is a
  *separate* additive term in C4's own master formula — not really a new finding, just that the
  scope sentence needs to say "Ξ=o(1/n) AND the IMB term vanishes/is controlled," not "Ξ=o(1/n)"
  alone; (2) an adversarially-constructed bias direction lying in the kernel of the contraction
  functional can have Ξ≠o(1/n) yet D=o(1) — true but a measure-zero technicality for any engine
  anyone would actually use (their bias points along Σ̂ or another generic direction, never an
  engineered kernel direction) — worth a one-clause caveat, not a rewrite; (3) a pathological
  rare-large-jump engine with b_Σ=0 can still contribute O(1) to D — this is a real gap: the scope
  statement needs an explicit **regularity/locality** qualifier (Op(n^{-1/2}) draws with
  controlled third moments), which every engine actually under discussion (E1/E2/E3) already
  satisfies but which C9 never stated as a hypothesis. Amendment 2 below is revised accordingly.
- **C6 (the −0.244 "deflated arm" number) — CHECKED EMPIRICALLY, see result below.** Mode B
  recomputed what a pure scalar deflation c=(N−p−2)/(N−1) of the conjugate engine's Σ* draws
  should give algebraically and got ≈−0.34 to −0.39, not the round-1 reported −0.244 — a real
  ~30% gap, not a Mode B arithmetic error (I independently re-derived the same −0.344 by hand).
  Traced the deflation to `verification/spikes/diag-nscaling.R:29`: it recenters at
  $S=SS/(N-1)$ (the *unbiased* sample covariance), which the round-1 handoff table loosely
  labeled "the MLE" — an actual mislabeling, though a small one (S vs the divisor-N MLE differ by
  a factor $N/(N-1)\approx1.005$ at $N{=}200$, far too small to explain a 30% gap on its own). Ran
  a low-noise check with the exact-identity evaluator (`enga_eval_engine`/`enga_contract_Xi`,
  R=60, paired same-seed draws) reproducing the *exact* deflated P-step from `diag-nscaling.R`.
  **Result: the −0.244 number is solid (independently reproduced at −0.2399, se .0075 — well
  within 1 SE), but the linear-rescaling mechanism both Mode B and I assumed to explain it is
  wrong.** The measured deflated $b_\Sigma$ contraction came back **−0.1010** (se .0062), not the
  **−0.343** linear rescaling predicts — a 3× miss in the opposite direction from Mode B's
  concern (the true residual is *smaller*, not the -0.24 vs predicted -0.34-0.39 gap Mode B
  flagged). Reason: `impute_conj_deflated` deflates the scale matrix **inside the P-step of an
  iterative data-augmentation chain**, not as a one-shot rescale of an otherwise-unmodified
  chain's stationary output (unlike `enga_recentre_sigma`'s matrix recentring, which *is* a clean
  post-hoc shift of already-stationary draws, unaffected by this). A smaller drawn $\Sigma$ feeds
  back into a less-dispersed I-step imputation, which feeds back into a smaller $SS$ at the next
  P-step — the deflated chain settles at a genuinely different, non-linearly-related stationary
  bias, not "$c$ times the undeflated chain's bias." **Consequence:** Fable's own "83% centering
  bias / 13% mu-wander / ~4% imbalance" decomposition (audit response §2, "Correction to the
  handoff's expected decomposition") rests on the same flawed isotropic-vs-anisotropic-residual
  reading of the −0.244 number and should **not** be carried into the manuscript as stated — drop
  that percentage breakdown. This does **not** touch the drafted callout above: it cites only the
  matrix-recentred value ($-0.150$, a clean post-hoc operation, unaffected) and the full Jeffreys
  value ($-0.78$), never the scalar-deflated-arm number or its isotropic/anisotropic story.
  Reproduction: `triage-c6-deflated-arm.R` (scratchpad this session; worth promoting to
  `verification/_modules/` alongside `engine-gap-audit.R` if this DA-feedback finding is kept).
- **C7 (bootstrap floor "≤0.01") — PARTIALLY ALREADY ADDRESSED, flagging for Marcus.** Mode B's
  complaint is about the *new* exact-identity "E3 master" 2-point comparison (N=200/1000,
  `audit-engine-formula.R`'s evidence table), which is genuinely underpowered to show 1/n decay.
  But the paper's actual validated claim rests on the *original* Amelia engine's 4-point N-scan
  (`verification/spikes/phase0a-calibrated.R`: −0.099/−0.047/−0.029/−0.019 at
  N=200/500/1000/2000), which already shows clean ≈O(1/N) decay to a value well inside the
  (A)+(C) noise band — that evidence doesn't need redoing. The cheap fix, if wanted: extend the
  new exact-identity E3 arm to the same four N points (parameter-draw-only Monte Carlo, no
  imputation, so this is inexpensive) so the mechanism decomposition has the same N-coverage as
  the headline claim. Not done yet — flagging for a decision, not blocking.

Per the resume instructions this session: nothing here lands until (1) the above triage is
resolved (C6 empirically, C9 by the revision below) and (2) Marcus ratifies the framing. Do not
apply these edits with Edit/Write/Bash against `manuscript/derivation.qmd` until both conditions
are met and Marcus says so explicitly.

Supporting artifacts built this session (both pass/reproduce cleanly):
- `verification/cas-wolfram/verify_engine_gap_sympy.py` — SymPy check of the four algebraic
  lemmas (concrete p=3 instantiation) + the p=1 closed-form toy table (Jeffreys −1, Laplace
  −1/4, bootstrap 0), all 10 checks PASS.
- `verification/_modules/engine-gap-audit.R` — the spike promoted to a cached-RDS +
  summary.csv module (`run_engine_gap_audit(R_per_cell, cl, out_dir)`); smoke-tested at R=4,
  reproduces the audit's headline numbers (mu-share ≈0.20–0.205, cj_full ≈−0.78, matching the
  reported −0.783/−0.759). **Not wired into `run_all.R`'s phase dispatch** — that integration
  is a follow-up once the framing is ratified, not done here to avoid touching the single
  entrypoint file without explicit sign-off.

Nothing about the theorem's headline number, the Term A/B split, or the paper's own W1/W3
validation (which used Amelia's EMB, a second-moment-matched engine) changes. This amendment
narrows the *scope statement* of when $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ holds and
discloses a characterized, computable correction for the engines it excludes.

---

## Amendment 1 — D9, lines 383–394

Fable's finding: the gloss $\tilde\phi\approx\hat\theta_{\text{obs}}$ describes the draw's *mean*
only; treating it as sufficient for the deviance (a sum of $n$ per-cell $O(1/n)$-sensitive terms)
is exactly the gap the audit closes. Minimal fix: one forward-pointing sentence at the end of the
existing paragraph — no other change to D9's content, which is otherwise correct.

**Current (line 394 ends the paragraph):**
> ...exactly as the EM E-step conditions $Q(\theta\mid\theta^{(t)})$ on the current iterate —
> **not** on the unknown truth $\theta_0$.

**Proposed (append one sentence):**
> ...exactly as the EM E-step conditions $Q(\theta\mid\theta^{(t)})$ on the current iterate —
> **not** on the unknown truth $\theta_0$. Whether this mean-level approximation is enough to
> leave $\bar Q_\infty$'s bias unchanged depends on the imputation engine, not only on the mean
> of $\tilde\phi$; the callout below makes this precise.

---

## Amendment 2 — new callout after line 426 (before "Notation clash", line 428)

This is the substantive addition: Fable's master formula, scoped and disclosed. Placed right
after the existing "$\bar Q_\infty$ is the fitted predictive, not the oracle" callout, since it
answers the natural next question that callout raises (fitted at $\hat\theta_{\text{obs}}$ — but
drawn how?).

**New block (insert as its own `.callout-important`):**

> ::: {.callout-important}
> ## The $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ headline needs a second-moment-matched imputer
>
> Write $\Xi=b_\Sigma+\operatorname{Var}(\mu^\ast)$ for an imputer's centering bias in $\Sigma$
> plus its draw covariance in $\mu$, both evaluated against the fitted $\hat\theta_{\text{obs}}$.
> For an imputer whose draw is *regular* — $\hat\theta_{\text{obs}}+O_p(n^{-1/2})$ with controlled
> third moments, the condition every engine below satisfies, and which excludes only pathological
> constructions such as a draw that rarely jumps to a fixed distant value — the
> $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ headline holds, to leading order, whenever
> $\Xi=o(1/n)$ per completed cell **and** the design-imbalance term below also vanishes or is
> controlled; call an imputer meeting both conditions *second-moment-matched*. Deterministic FIML
> meets both trivially, since it does not draw a parameter at all. Bootstrap resampling with an EM
> plug-in, the engine this paper's own simulations use, meets the first: for complete data
> $\mathbb{E}^\ast[\tilde\Sigma+(\tilde\mu-\hat\mu)(\tilde\mu-\hat\mu)^\top]=\hat\Sigma$ exactly, so
> the bootstrap's covariance deflation cancels its mean's draw variance, and $\Xi$ is zero up to a
> residual of the observed-data estimator's own bias under missingness; like every drawing engine,
> though, the bootstrap still carries the small design-imbalance term under MAR.
>
> A genuine Bayesian posterior draw is not second-moment-matched, by construction: a proper draw
> is *over*-dispersed relative to the plug-in (Rubin's between-imputation variance rule is built
> to capture exactly that extra spread), so $\Xi\succ0$. Such a draw carries a persistent,
> computable correction to the headline,
> $$
> D=-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})-\tfrac12\sum_i\operatorname{tr}\!\big(\hat V_i^{-1}C_i\,b_\Sigma\,C_i^\top\big)-\mathrm{IMB}+o(1).
> $$
> $\mathrm{RIV}_{\mu\mu}$ is the mean block of $\mathrm{RIV}$. For a unit with missing block $M$
> and observed block $O$, $\hat B=\hat\Sigma_{MO}\hat\Sigma_{OO}^{-1}$ and
> $\hat V=\hat\Sigma_{MM}-\hat B\hat\Sigma_{OM}$ are the fitted regression map and conditional
> covariance of @sec-alg's Schur complement, and $C=[I,-\hat B]$ carries a full covariance
> perturbation to its effect on $\hat V$. $\mathrm{IMB}$ shares its design-imbalance origin with
> $(A)+(C)$ (@sec-termA) but arises from the imputer's own $\Sigma$-draw rather than from the
> fitted model. It is present under MAR for every drawing engine (deterministic FIML excepted,
> since it never draws $\Sigma$) and exactly zero under MCAR; measured at
> $\approx-0.006\operatorname{tr}(\mathrm{RIV})$ in this paper's own W1 cell, not yet derived in
> closed form. Every other piece is computable from quantities the derivation already defines;
> $b_\Sigma$ is prior-dependent, so no engine-free correction constant exists — a Jeffreys-prior
> draw measured here gives $\approx-0.78\operatorname{tr}(\mathrm{RIV})$ at $N=200$, while
> recentring the same draws at their own measured $b_\Sigma$ collapses the correction to
> $\approx-0.15\operatorname{tr}(\mathrm{RIV})$, matching a mean-centered Gaussian draw.
>
> `[mc]` the four algebraic identities behind this reduction — the Schur-complement derivative
> and its concavity, the resulting cancellation, and the block-inverse identity that isolates
> $\mathrm{RIV}_{\mu\mu}$ — reduce to zero symbolically
> (`verification/cas-wolfram/verify_engine_gap_sympy.py`); the numerical values above are
> measured directly from each engine's parameter draws, with no imputation or log-likelihood
> evaluation needed (`verification/_modules/engine-gap-audit.R`).
> :::

**Revision note (2026-07-02, post-gate):** the previous draft stated the scope condition as bare
$\Xi=o(1/n)$, presented as necessary and sufficient. GPT-5.5 Pro's red-team pass (Mode B, C9)
constructed valid counterexamples against both directions: an engine can have $\Xi=0$ and still
have $D\neq0$ under MAR (the design-imbalance term is a separate additive piece, not absorbed
into $\Xi$ — already true of Fable's own C4 formula, just not stated as a joint condition), and an
adversarially chosen bias direction lying in the kernel of the missing-information contraction can
have $\Xi\neq o(1/n)$ with $D=o(1)$ anyway (a measure-zero technicality for any engine actually
used in practice). A third construction (a rare-large-jump engine with zero mean bias) shows the
regularity/locality of the draw law was an unstated hypothesis, not a free consequence. The block
above adds the design-imbalance condition explicitly, states $\Xi=o(1/n)$ as *sufficient given
regularity* rather than as an unqualified iff, and names the regularity condition. This changes
no number in the paper; it only tightens which engines the scope sentence covers.

**Open editorial call flagged for Marcus, not resolved here:** the brms weakly-informative number
($\approx-1.36\operatorname{tr}(\mathrm{RIV})$ at $N=200$) is left OUT of the primary version
above, since the charter's open question "brms cell: manuscript or response-letter-only" is
unresolved and this callout would be the first place it entered `manuscript/`. If brms is
cleared for the manuscript, the last sentence of paragraph 2 could instead or additionally read:
"...a Jeffreys-prior draw and a weakly informative one measured here differ by nearly a factor of
two ($\approx-0.78\operatorname{tr}(\mathrm{RIV})$ vs $\approx-1.36\operatorname{tr}(\mathrm{RIV})$
at $N=200$)" — but that activates the Bürkner/Stan/LKJ citation trio (`todo/003`, conditional
row) and needs a higher-$R$ brms cell (current SE .15 at R=6, per the open question).

**Notation reconciliation needed before landing:** this draft defines $\hat B$, $\hat V$, $C$
inline rather than assuming they already exist in @sec-termA, because I have not read
@sec-termA's own missing/observed-block notation in this session and do not want to guess it
incorrectly. Before this lands, check whether @sec-termA already has established symbols for the
same per-unit $M$/$O$ split and reconcile (reuse @sec-termA's notation if it exists, rather than
carrying a second parallel notation for the same object).

---

## Amendment 3 — known-scale callout, near line 759

Fable's Q4(a)(2): connect the known-scale $C_n$ (already proved) to the new estimated-scale
engine-class result, so the reader sees the known-scale case as the $\mu$-only special case of
the general statement rather than a separate fact.

**Current (line 757–759):**
> the two arms differing by the posterior-draw imputation variance $C_n=\tfrac12\operatorname{tr}(\mathrm{RIV})$
> — so deterministic FIML and proper MI are **not** interchangeable for a known-scale fit.

**Proposed (append one sentence):**
> the two arms differing by the posterior-draw imputation variance $C_n=\tfrac12\operatorname{tr}(\mathrm{RIV})$
> — so deterministic FIML and proper MI are **not** interchangeable for a known-scale fit. This
> $C_n$ does not vanish once the scale is estimated: for any imputer whose draw is not
> second-moment-matched to the plug-in, it survives as the $\mu$-block
> $\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})$ of the correction in @sec-qfun, and only a
> second-moment-matched imputer such as bootstrap resampling with an EM plug-in cancels it.

---

## Proposed decisions.md entry (draft — do not assign a D-number until ratified)

> ## DA-engine scope amendment: the headline needs a second-moment-matched imputer (2026-07-0?,
> pending ratification)
>
> A cross-model audit (Claude Fable 5, max effort; `todo/040-audit-response-fable5.md`,
> `cc62ad7`), triggered by the v1 review's data-augmentation gap (r1#8), found that
> `derivation.qmd`'s estimated-scale $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ headline as
> stated ("deterministic FIML and proper MI alike", line 423) over-generalizes: a genuine
> Bayesian posterior draw is over-dispersed relative to the fitted plug-in by construction, and
> the deviance — a sum of $n$ per-cell $O(1/n)$-sensitive terms — resolves that over-dispersion
> into an $O(1)$ correction. The headline is scoped to *second-moment-matched* imputers
> ($\Xi=b_\Sigma+\operatorname{Var}(\mu^\ast)=o(1/n)$ per cell): deterministic FIML trivially,
> and bootstrap resampling with an EM plug-in (Amelia's EMB, this paper's own validated engine)
> via an exact complete-data second-moment identity. A genuine posterior draw carries the
> disclosed, computable correction $D=-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})-\tfrac12\sum_i\operatorname{tr}(\hat V_i^{-1}C_ib_\Sigma C_i^\top)-\mathrm{IMB}$.
> This paper's own W1/W3 simulations are unaffected (Amelia's EMB is second-moment-matched); the
> amendment narrows the scope statement and adds a disclosed correction term for the engines it
> excludes, not a change to any reported number. Verification: four algebraic lemmas checked
> symbolically (`verification/cas-wolfram/verify_engine_gap_sympy.py`, 10/10 PASS, incl. a
> closed-form $p=1$ toy table); the numerical decomposition promoted to a cached module
> (`verification/_modules/engine-gap-audit.R`). Landed in `derivation.qmd` at D9 (:383–394), the
> fitted-vs-oracle callout (:404–426, new callout inserted), and the known-scale callout
> (:750–766).

---

## Preconditions checklist before any of the above lands

- [ ] GPT-5.5 xhigh gate run on Fable's new derivations (master formula, cancellation lemma,
      $\mathrm{RIV}_{\mu\mu}$ identity, IMB) — package built at `todo/040b-gpt55-gate-package.md`
      (`be318c3`), not yet launched (needs Marcus's explicit "go").
- [ ] Any gate escalation triaged per the package's policy (refutation routes back through
      `verification/spikes/audit-engine-formula.R` and the $p=1$ closed-form toy before
      acceptance — the toy is now built and passing, see above).
- [ ] Marcus ratifies the Q4(a)-strengthened framing (or directs otherwise).
- [ ] Notation reconciliation with @sec-termA (see Amendment 2 note above).
- [ ] Editorial call on the brms sentence (see Amendment 2 note above) — depends on the open
      "brms: manuscript or response-letter-only" charter question.
- [ ] Provenance: von Hippel-Bartlett 2021 + Efron 1979 acquired (Zotero → `/lit-sync`); Wang-Robins
      1998, Nielsen 2003, Schafer 1997 `:3502-3532`, Honaker 2011 re-verified in-session at
      drafting time with Appendix-A source pointers (all four already `literature/`-resident per
      the audit's provenance accounting).
- [ ] Apply via Bash, not Edit/Write (the citation hook misfires on `manuscript/` subdir edits —
      `feedback_citation_hook_cwd_bug`).
