# Precision inventory: derivation.qmd + response letter (todo/049, flag-only)

**Date: 2026-07-05. The queued R11 follow-up of D-26 (decisions.md), applied to the two
documents outside todo/048's scope: `manuscript/derivation.qmd` and
`manuscript/reviews/v1/response/response-letter.md`. FLAG-ONLY — no edit in this commit.**
Rule of record: R11 (typed precision; see `precision-addendum-2026-07-05.md` for the full
statement and the ratified taxonomy). This pass is precision-only: derivation.qmd keeps its
own register (D-08), and no register/vocabulary rule is imported. Line numbers are the two
files at commit `26d7148`.

Classes, as ratified: **E1** = genuinely exact (identity / definition / iff / sampler /
exact-rational enumeration) — KEEP. **E2** = leading-order or Monte-Carlo-agreement claim
wearing exactness — RESCOPE (proposed wording given). **E3** = idiomatic intensifier — KEEP
or THIN. Two further groups this document needs that the manuscript's did not:
**measurement-precision senses** ("machine precision", "imprecise", "higher precision",
"precisely estimable") — outside R11's reserved-word rule, listed for completeness, no
action; and **record** — verbatim quoted source text, untouchable.

Grep basis: `exact|exactly|precisely` plus the completeness scan of `precise` and
`identically`. derivation.qmd: 114 hit-lines (a few lines carry two instances).
response-letter.md: 15 hit-lines.

The headline is the expected one: **an E1 supermajority.** The derivation is dense with
genuinely exact content — CAS-verified identities, exact-rational enumerations, iff
conditions, Lemma P's cancellation, sampler senses, and M=∞ anchors — and its theorem
displays already carry explicit remainders. Five E2 rescopes, two borderlines, and an
optional E3 thin set is the whole action surface.

---

## Part 1 — `manuscript/derivation.qmd`

### E2 — five proposed rescopes

| # | line | current | proposed | why |
|---|---|---|---|---|
| 1 | :99 | "how much more than the mean a correction can match — the whole null distribution per pair, exactly; nothing on the noncentral side, in principle" | "— the whole null distribution per pair, up to asymptotic approximation; nothing on the noncentral side, in principle" | @sec-ic-ladder's own statement (:1951) scopes equating as "exact there up to asymptotic approximation" (the weights are estimated; the law is limiting). The intro summary drops that scope. The proposed phrase is the section's own. |
| 2 | :155 | "@sec-lrt develops the likelihood-ratio application: the exact differential bias of the MI deviance numerator at the null" | "the closed-form leading-order differential bias of the MI deviance numerator at the null" | Verbatim twin of ratified rescope #2 (manuscript :64, applied in the S1 batch). The differential bias is a leading-order object. |
| 3 | :1513 | "Three things are derived here: the exact differential bias of the MI deviance numerator at the null (it is *not* the difference …)" | "the closed-form leading-order differential bias of the MI deviance numerator at the null (it is *not* the difference …)" | Same object, same fix as #2. |
| 4 | :1991 | "The noncentral side shrinks, exactly as the law predicts." | "The noncentral side shrinks as the law predicts." | The same sentence's own numbers agree within Monte Carlo error only ($0.586$ against predicted $0.570$; $0.362$ against $0.398$) — the ratified rationale of manuscript rescope #6 (exactness asserted where the sentence reports approximate agreement). |
| 5 | :2043 | "the first two are theorems with exact empirical confirmation" | "the first two are theorems with direct empirical confirmation" | The named confirmations (the $a_k$ / $1/\lambda_{\max}$ shrinkage, the copula invariance) were measured within Monte Carlo error; the theorems are exact, the confirmations are not. |

### Borderline — two for Marcus's call

| # | line | current | note |
|---|---|---|---|
| 6 | :1697 | "the run reproduces the *mechanism* of Proposition L4 exactly." | The qualitative mechanism did reproduce in full (the per-model level is $O(1)$ tens of standard errors from zero, collapses under the MCAR twin, decouples across candidates), so "exactly" is defensible as "in every predicted respect" — but it invites the magnitude reading, and the magnitudes are Monte Carlo. **Recommend the thin:** "the run reproduces the mechanism of Proposition L4." Cost zero. |
| 7 | :1839 | "carries a differential bias $-[\operatorname{tr}(\mathrm{RIV}_j) - \operatorname{tr}(\mathrm{RIV}_k)]$: the candidate with *more* missing information about its own parameters looks artificially better, by exactly the amount of extra missing information." | Twin of ratified borderline #7 (manuscript S4-P16, KEPT because "the antecedent is the already-scoped leading term") — except this sentence lacks that in-sentence scope: the manuscript version says "a differential bias **whose leading term is** the surplus", this one states the bias as if it were the whole. **Recommend Option A (align):** "carries a differential bias whose leading term is $-[\operatorname{tr}(\mathrm{RIV}_j) - \operatorname{tr}(\mathrm{RIV}_k)]$: …", keeping "by exactly" — the KEEP rationale then holds verbatim. Option B: keep as-is per the #7 precedent. |

### E1 — keep (65 instances)

Grouped by the licensing sense; every line listed.

**Iff / vanishing identities.**

| line | instance | why it is genuinely exact |
|---|---|---|
| :68 | "nonzero exactly when the missing and observed units have different conditioning-variable distributions and zero under MCAR" | iff on $(A)+(C)$, which is *defined* as the leading-order piece (ratified precedent: manuscript :508) |
| :469, :760, :1109, :2982, :3110 | "exactly zero under MCAR" (×5: the IMB term; $\Delta_{\mathrm{KM}}$; the two K&M cross-term blocks; the selected-Gaussian closed form) | each functional vanishes identically at $b=0$ / MCAR — an evaluation of a closed form, not a limit |
| :1629 | "zero exactly when $H_{12}=0$" | iff, pure algebra (manuscript :332 precedent) |
| :1562 | "the evaluation-slot gradient … vanishes identically at $(\theta_0,\theta_0)$" | the conditional-score identity (the density integrates to one) |

**The $(A)+(C)$-cancellation family.** The functional is imputation-determined and
model-independent at the null, so its differential vanishes identically; the $O(n^{-1})$
model-specific survivor is named explicitly at :1680, mirroring the ratified treatment of
manuscript :267/:494 (exactness on the defined leading-order object, remainder named nearby).

| line | instance |
|---|---|
| :84 | "$(A)+(C)$ design-imbalance part cancels *exactly* at the null" |
| :786 | "the paired differential's $(A)+(C)$ content cancels *exactly*" |
| :1516 | "the exact cancellation of the design-imbalance term $(A)+(C)$ at the null" |
| :1689 | "its *differential*, which is exactly zero at the null" |
| :1773 | "the noise orders and exact $(A)+(C)$ cancellation of Propositions L3–L4" |

**Definitional identifications and closed-form identities.**

| line | instance | why |
|---|---|---|
| :86, :1741 | "is precisely the mean inflation that a correctly calibrated reference distribution already absorbs" (×2) | the spectrum-sum identity $\sum_j\lambda_j = q_d + \operatorname{tr}(\mathrm{RIV}_\perp)$, exact algebra within the limiting law (manuscript :350 precedent) |
| :123 | "reproduces exactly that $\operatorname{tr}(\mathrm{RIV})$" | identity between two closed-form penalties (ours and the 2017 missing-data criterion's) |
| :259 | "differ by exactly the information the missing data would have supplied" | the missing-information principle: $I_{\text{mis}} = I_{\text{com}} - I_{\text{obs}}$, definitional |
| :346 | "is exactly what `fisher_info_obs_mvn` computes" | identification with the code object |
| :450 | "$\mathbb{E}^\ast[\tilde\Sigma+(\tilde\mu-\hat\mu)(\tilde\mu-\hat\mu)^\top]=\hat\Sigma$ exactly" | the complete-data bootstrap second-moment identity |
| :964 | "pieces $(A)$ and $(C)$ are exactly the first- and second-order terms of the Taylor expansion" | definitional identification; the display two lines down carries its $O(n^{-3/2})$ |
| :999 | table entry "$0$ (exact)" | the two closed-form entries cancel identically ($+n_{\text{mis}}/(2n_{\text{obs}}) - n_{\text{mis}}/(2n_{\text{obs}})$) |
| :1014 | "The exact Term-A integrand is …" | the closed form, named against the leading-order approximation used later |
| :1017 | "it is exactly the Rao-Blackwellized $A_{\text{rb}}$" | identification |
| :1029, :1030 | "$I_{\text{com}}-I_{\text{obs}}^{O}$ is exactly that selected missing information" / "the cancellation … is **exact under the realized (observed-information) convention**" | algebraic identity under the stated convention |
| :1064 | "The exact small-sample bias of $\hat\Sigma$ under monotone missingness is classical" | names the classical closed form |
| :1118 | "shifts $(A)+(C)$ by exactly $\Delta_{\mathrm{KM}}$" | definitional identity (both conventions share $A_{\text{rb}}$; the displayed relation is algebra — :1124's own "near-identity" names the same fact: a definitional consequence, not an independent measurement) |
| :1340 | "$\operatorname{tr}(\mathrm{RIV})=q\,r/(1-r)$ exactly" | expected-information identity under response-only MCAR |
| :1343 | "the deterministic-FIML evaluation is exact for any family" | a missing row's contribution *is* the negative entropy; the $M=\infty$ identity |
| :1400 | "these cancel exactly, for every design distribution and every canonical family" | Lemma P (ratified precedent: manuscript :504) |
| :1427 | "the estimated-scale headline $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ transfers exactly, for every design distribution" | licensed by $\Delta_h=0$, the identity stated as the same sentence's antecedent ("$h\equiv1$, so $g\equiv0$ and $\Delta_h=0$:") — coefficient exactness in R11's sanctioned sense |
| :1434 | "the analytic anchor exact at $M=\infty$ (R7)" | Rubin's $M=\infty$ identity |
| :1442 | "the draw arm sits below FITTED by exactly one further copy of the $(C)$ functional" | exactness attaches to the object (one copy of the named functional); the display that follows carries its $+O(n^{-1})$ |
| :1578 | "it reproduces exactly the naive $\operatorname{tr}(\mathrm{RIV}) - \operatorname{tr}(\mathrm{RIV}_0)$" | formula-level identity: the substitution maps one closed form onto the other (manuscript :307 precedent) |
| :1623 | "The overstatement has an exact closed form" | matrix identity (manuscript :324 precedent) |
| :1630 | "The overstatement is therefore precisely the missing-information coupling" | direct reading of that identity (manuscript :332 precedent) |
| :1809 | "is exactly *half* that of the earlier … criteria" | relation between two closed-form penalty formulas (manuscript :360 precedent) |
| :1847 | "corrections are exactly the 'self-contained levels' whose *difference* …" | definitional identification (manuscript :362 precedent) |
| :1850 | "sits at the exact equality case" | the algebraic equality case of the proposition (manuscript :362 precedent) |
| :1893 | "giving $T_k = N[\log\lvert\hat\Sigma_k\rvert - \log\lvert S^{*}\rvert]$ exactly" | closed form for block-diagonal constraints (manuscript :377 precedent) |
| :1945 | "the probability-integral-transform exactness of the equated statistic" | PIT is exact given the reference law; the law's asymptotic status is stated at :1951 |
| :2020 | "the naive trace difference and the exact complement trace agree *to machine precision*" | "exact" names the closed-form object (manuscript :484 precedent); the agreement figure ($3.6\times10^{-15}$) is the measurement |
| :2023 | "which is precisely the invariance condition under which Proposition L2 holds with equality" | identification of the equality condition (manuscript :400 precedent) |
| :3093 | "embedded in the full index set exactly as in `fisher_info_obs_mvn`" | construction identity with the code implementation |

**Sampler / exact-enumeration senses.**

| line | instance |
|---|---|
| :1293 | "The exact alternative is data augmentation" (manuscript :408 precedent, verbatim) |
| :1304 | "drawing from the exact observed-data posterior" |
| :1389 | "the exact enumerated $\mathbb{E}[\hat\beta]$ on a two-point design" |
| :1411 | "12 exact-rational four-point designs" |
| :1468 | "the exact-enumeration constants" |
| :1500 | "exact enumeration gives $\approx0.6/n$ …" |

**CAS reduction identities.**

| line | instance |
|---|---|
| :752 | "reduces exactly to the bivariate value" |
| :1145 | "reduces **exactly** to the monotone closed form" |
| :1156 | "reduces exactly to the bivariate value" (general-$p$) |
| :1637 | "exact equality under constructed invariance" |
| :2530 | "is **symbolic** (exact, parameterization-free)" |
| :2622 | section header "(abstract, exact)" |

**Already R11-compliant scoped forms (the template patterns; do not touch).**

| line | instance |
|---|---|
| :39 | "derives that bias exactly, to leading order" |
| :571 | "the hypothesis under which some later step is exact to leading order" |
| :692 | "This identity is exact only to leading order" |
| :873 | "elementary and exact to leading order" |
| :1679 | "identical realizations … cancel exactly to leading order" |
| :1951 | "with equating exact there up to asymptotic approximation" |

Also in the E1 sense but additionally inside **executable code cells** (edit surface is
prose only; these would not be touched in any case): :2669 and :2673 (`lst-mc-combine`
caption and printed "exact zero" — a symbolic-zero assertion), :3041 (the Tier-B printed
"[exact]" — same).

One further E1 not in a group above: :1664 "literally the same realization in both levels
and cancel exactly, dataset by dataset — not merely in expectation" — identical realized
constants subtracted (manuscript :340 precedent); the leading-order residual is scoped at
:1679.

### E3 — idiomatic instances (15): recommended thins marked

| line | instance | disposition |
|---|---|---|
| :755, :763, :1201, :1222, :1688 | "exact magnitude" (×5, all in the $(A)+(C)$ standalone-value discussion) | **THIN to "magnitude" (recommended, all five).** "Exact" here means "the true value", in sentences whose content is that the value is *not* sharply pinned — no exactness claim is being made, and these five are the densest non-identity use in the document. Cost zero. |
| :457 | "built to capture exactly that extra spread" | THIN optional ("built to capture that extra spread"); twin of letter :276 — treat the pair the same way |
| :3070 | "shows exactly where the cross term comes from" | THIN optional ("shows where the cross term comes from") |
| :396 | "exactly as the EM E-step conditions … on the current iterate" | KEEP (manuscript :168 precedent, kept) |
| :426 | "Term A is instead $+\operatorname{tr}(\mathrm{RIV})$ precisely because the completions are drawn at the fitted $\tilde\phi$" | KEEP ("precisely because" reason idiom; the exactness attaches to the reason, not the equality) |
| :919 | "$A$ is nonzero precisely because the imputations use $\tilde\phi\approx\hat\theta_{\text{obs}}\neq\theta_0$" | KEEP (same idiom) |
| :857 | "the lemma is stated precisely to forestall it" | KEEP ("in precise form" sense) |
| :1584 | "the realized-pairing route made precisely the $I_{\text{obs}}$-metric error" | KEEP (identifies which error; historical statement about the route) |
| :1655 | "The mechanism is worth stating precisely" | KEEP ("with precision" sense) |
| :1776 | "locating the objection's error precisely" | KEEP (same sense) |
| :1994 | "This is the toy made exact" | KEEP (the shrinkage law's closed-form constants are the exact version of the toy argument) |

### Measurement-precision senses — outside the rule, no action (26 lines)

"machine precision" (:753, :1144–45, :1169, :1204, :2521, :2532, :2799, :2890, :3052,
:3054), "heavy-tailed and imprecise" / "imprecise" / "untrended" measurement statements
(:766, :1008, :1084, :1123, :1161), "ultra-precise paired contrast" (:761), "the genuine
precise check" (:1126), "What is precise is …" (:1224), "precisely estimable" (:91, :158 —
the "with precision" sense; the paired differential *is* measured tightly, template :267
precedent), "Each estimator's precision" (:258), "asymptotic precision" (:269), "The
precise conditions are stated as assumptions" (:229), "stated precisely as an assumption"
(:523), "the callout below makes this precise" (:400), "independently reconfirmed at higher
precision" (none here — letter :308).

### Record — untouchable (1)

:2379 — verbatim quoted source text in the Appendix A fingerprint for the 2022 Annals
SMI paper ("Precisely, we first generate …"). Quotation, not prose; out of scope.

---

## Part 2 — `manuscript/reviews/v1/response/response-letter.md`

Quoted reviewer text is untouchable; two hit-lines sit inside the r1#8 quotation block
(:251 "rather than exact data augmentation", :252 "depend on exact posterior draws") and
are out of scope.

### E2 — none

No instance in the letter attaches exactness to a leading-order equality; the letter's
magnitude claims all carry their standard errors inline.

### E1 — keep (6)

| line | instance | why |
|---|---|---|
| :99 | "cancel exactly for any canonical link" | Lemma P (the manuscript :504 precedent, verbatim object) |
| :101 | "including exact finite-$n$ enumerations that need no Monte Carlo" | exact-enumeration sense |
| :258 | "Two independent exact data-augmentation engines were built" | sampler sense |
| :323 | "which is exactly the complete-data second-moment identity ($\mathbb{E}^\ast[\ldots]=\hat\Sigma$)" | identification with the displayed identity |
| :335 | "the bootstrap-floor exact-identity check" | names the exact-identity evaluator (a tool) |
| :415 | "$0.0185$, which sits exactly on a floating-point rounding boundary" | a finite fact about the stored number's binary representation, explained in the same sentence |

### E3 — idiomatic (6): recommended thins marked

| line | instance | disposition |
|---|---|---|
| :95 | "a post-hoc correction prompted by a miss is exactly the pattern an adversarial review flagged" | **THIN (recommended):** "is the pattern an adversarial review flagged" |
| :176 | "shows the posterior predictive check catching exactly an imputation/analysis incompatibility" | **THIN (recommended):** "catching just such an imputation/analysis incompatibility" (also repairs the awkward "exactly an") |
| :426 | "Confirmed exactly as described, and traced to two further occurrences" | **THIN (recommended):** "Confirmed as described, and traced to two further occurrences" |
| :172 | "the exact one-sided situation an applied secondary analyst is in" | KEEP or thin to "the one-sided situation …" — identification-flavored; your call |
| :276 | "Rubin's between-imputation variance rule exists to capture exactly that extra spread" | twin of derivation :457 — same call for both |
| :348 | "is indeed confounded in exactly the way described" | KEEP (recommended): the confound in that nested family *is* complete — every nesting step raises both complexity and missing information — so "exactly" concedes the reviewer's point accurately |

### Measurement sense — no action (1)

:308 "independently reconfirmed at higher precision".

---

## Incidental finding: an authorized manuscript rescope never landed

While mirroring the ratified borderline calls, one D-26 item turned out to be a straggler:
**E2 rescope #6 (S5-P13)** was authorized ("The addendum's six E2 rescopes are AUTHORIZED",
decisions.md D-26) but never applied. Evidence: the S4 batch script applied #5 with an
explicit "R11 rescope #5" label (`update-batch-s4-register-20260705.py:86`), the S5 batch
script's only S5-P13 edit is the caption-convention sentence
(`update-batch-s5-register-20260705.py:33`), and both `level3-paragraphs.json` (:2192) and
the built `mi-spectral-apa.qmd` (:452) still read "and the two arms differ by exactly the
posterior-draw imputation variance" — in the same sentence that reports agreement "within
Monte Carlo error of their targets", which was the addendum's stated reason for the
rescope. The ratified replacement wording is on record: "and the difference between the
two arms matches the predicted posterior-draw imputation variance."

Proposed handling: apply it in this pass's apply step (a small `manuscript/plan/updates/`
script + rebuild + render), since the authorization already exists — flagged here so it is
an explicit line item rather than a silent ride-along.

---

## What this inventory asks Marcus to decide

1. Approve the five derivation E2 rescopes (#1–#5).
2. Call the two borderlines: #6 (:1697; thin recommended) and #7 (:1839; Option A — insert
   "whose leading term is" and keep "by exactly" — recommended).
3. Choose the derivation E3 thin set (recommended: the five "exact magnitude" instances,
   plus :457 and :3070; the remaining eight keep).
4. Letter: approve the three recommended E3 thins (:95, :176, :426) and call :172, :276,
   :348 (recommendations above; :276 should match whatever :457 gets).
5. The manuscript straggler (authorized rescope #6, S5-P13): apply now with the ratified
   wording, or defer to a separate commit.

Apply step (after the gate): E2/E3 changes only, via a guarded script or root-cwd edits;
then `quarto render manuscript/derivation.qmd` exit 0 with all Appendix B cells executing,
the derivation-audit mechanical engine at 0 blocker / 0 warn, and `check_plan.py` green.
