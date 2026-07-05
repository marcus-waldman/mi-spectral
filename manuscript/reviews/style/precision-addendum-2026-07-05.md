# Precision addendum: the "exact/exactly/precisely" inventory (todo/048, ratification record)

**Date: 2026-07-05. Raised by Marcus during Phase C review, before ratification: "exactly"
reads as bold given the truncated Taylor expansions the results rely on. FLAG-ONLY — no
manuscript edit.** This addendum is a **claim-strength item, not a style item**: the Phase C
demonstrations deliberately preserved every "exactly" verbatim under the hedge-invariance
rule, and changing any of them requires Marcus's explicit authorization as its own line
item (T-06-adjacent), tracked separately from the register sweep even if executed in the
same Phase D batches. That keeps the audit trail clean: the style pass changes no claims;
the precision pass changes exactly the instances authorized here.

## The proposed rule (rubric item R11 / conflict C9)

> **Typed precision.** "Exact", "exactly", and "precisely" are reserved for (i)
> finite-sample algebraic identities and closed forms, (ii) definitional identifications,
> (iii) if-and-only-if conditions, and (iv) the exact-sampler sense standard in the MCMC
> literature. A claim whose content is leading-order (built on a truncated expansion,
> carrying an $O(n^{-1})$ or $o(1)$ remainder) either takes the scope word — "to leading
> order", "up to $O(n^{-1})$" — or attaches the exactness to the coefficient, never to the
> equality ("the leading term is exactly $\tfrac12\operatorname{tr}(\mathrm{RIV})$").
> Idiomatic intensifiers ("is exactly that kind of error") are thinned where cheap.

The manuscript already contains the template sentences the rule generalizes:
qmd `:260` "Their **leading parts** cancel exactly when ..." and `:345` "identical
realizations, so they cancel exactly **to leading order**". The register supports the
rule: Meng & Rubin write "equivalent in large samples" and use $A \bumpeq B$
($= B + o(1)$ a.s.) notation (`mengPerformingLikelihoodRatio1992b:165`); the exemplars
attach the qualifier. And the convention worth defending survives it: coefficient
exactness (the constant is the pinned rational $\tfrac12$, not $\approx 0.5$) is a real,
distinguishing claim of this paper — the rule moves "exactly" onto the coefficient rather
than deleting it.

## Full inventory: 49 instances, classed and dispositioned

Classes: **E1** = genuinely exact (identity / definition / iff / sampler) — KEEP.
**E2** = leading-order claim wearing exactness — RESCOPE (proposed wording given).
**E3** = idiomatic intensifier — KEEP or THIN (cheap, optional).
Line numbers are `manuscript/mi-spectral-apa.qmd` at commit `c75eb4f`.

### E2 — the six mandatory rescopes (the exposure Marcus flagged)

| # | qmd | level3 | current | proposed |
|---|---|---|---|---|
| 1 | :58 | S1-P4 | "This paper's central result describes that bias exactly." | "This paper's central result describes the leading term of that bias exactly." |
| 2 | :64 | S1-P6 | "Fourth, the exact differential bias of the likelihood-ratio numerator at the null in the complete-data metric." | "Fourth, the closed-form leading-order differential bias of the likelihood-ratio numerator at the null in the complete-data metric." |
| 3 | :102 | S2-P7 | "the main theorem prices it exactly" (Demo 3 interim: "quantifies that contribution exactly") | "the main theorem quantifies that contribution to leading order" |
| 4 | :102 | S2-P7 | "so the two forms differ by precisely the posterior-draw contribution" | "so the two forms differ, to leading order, by the posterior-draw contribution" |
| 5 | :271 | S4-P8 | "The two arms differ by exactly the posterior-draw imputation variance of @sec-background's proper-imputation paragraph." | "The two arms differ, to leading order, by the posterior-draw imputation variance of @sec-background's proper-imputation paragraph." |
| 6 | :434 | S5-P13 | "and the two arms differ by exactly the posterior-draw imputation variance" (results prose; the same sentence reports agreement only within Monte Carlo error) | "and the difference between the two arms matches the predicted posterior-draw imputation variance" |

### Borderline — two instances for Marcus's call

| # | qmd | level3 | current | note |
|---|---|---|---|---|
| 7 | :360 | S4-P16 | "looks artificially better by exactly that surplus" | the same sentence earlier says "whose **leading term** is the surplus", so "that surplus" is already the scoped object; defensible as-is, or thin to "by that surplus" |
| 8 | :480 | S5-P20 | table caption "Each row pairs an exact structural prediction with its measured value" | rows 1–2 are algebraic identities; row 3 (per-model map cannot calibrate the difference) is a qualitative impossibility quantified by measurement — "a structural prediction" (dropping "exact") covers all three rows |

### E1 — keep (35 instances)

| qmd | level3 | instance | why it is genuinely exact |
|---|---|---|---|
| :104 (×3) | S2-P8 | "exact posterior-moment identities" / "their exact form" / "exact identities rather than asymptotic approximations" | Rubin's Result 3.2: conditional-moment identities, exact at $M=\infty$ — Rubin's own framing |
| :106 (×2) | S2-P8 | "the exact identities" / "these exact moment identities" | same objects |
| :112 | S2-P10 | "That added bias is exactly what the main theorem quantifies." | identification of the object, not a magnitude claim |
| :116 | S2-P12 | "carries exactly their MAR cross term" | structural identification of a named term |
| :125 | S2-P13 | "is exactly this maximize-then-average statistic" | definitional |
| :139 | S3-P7 | "A wrong design reproduces its artifact exactly." | fixed seeds: bit-identical reproduction, a finite-sample fact |
| :159 | S4-P3 | "this matrix is exactly Rubin's $r_\infty$ in matrix form" | definitional identification; its premises ($\bar U_\infty = I_{\text{com}}^{-1}$, $T_\infty = I_{\text{obs}}^{-1}$) are stated in the same sentence |
| :260 | S4-P7b | "Their leading parts cancel exactly when ..." | the template: exactness attached to the leading parts |
| :267 | S4-P7b | "The term is zero exactly when the two distributions agree" | iff on $(A)+(C)$, which is *defined* as the leading-order piece; @eq-ac carries its $+\,O(n^{-1})$ |
| :267 | S4-P7b | "its exact vanishing under MCAR" | same object; the neighboring G1 sentence names the $O(1/n)$ remainder separately |
| :307 | S4-P10 | "Substituting $I_{\text{obs}}$ for the curvature reproduces exactly the naive difference" | formula-level identity: the substitution maps one closed form onto the other |
| :324 | S4-P11 | "The gap also has an exact closed form" | matrix identity @eq-gap |
| :332 (×2) | S4-P11 | "The gap is zero exactly when $H_{12}=0$" / "therefore precisely the missing-information coupling" | iff, pure algebra; and its direct interpretation |
| :340 | S4-P12 | "The mechanism is exact cancellation of realizations" | identical realized constants subtracted; the residual is scoped at :345 |
| :345 | S4-P13 | "identical realizations, so they cancel exactly to leading order" | the other template |
| :350 | S4-P14 | "@eq-lrt-bias is precisely the mean inflation that a correctly calibrated reference distribution already absorbs" | the spectrum-sum identity $\sum_j \lambda_j = q_d + \operatorname{tr}(\mathrm{RIV}_\perp)$ is exact algebra within the limiting law, which the preceding sentence names |
| :360 | S4-P16 | "its missing-data surcharge is exactly half that of the earlier ... criteria" | relation between two closed-form penalty formulas ($\operatorname{tr}$ vs $2\operatorname{tr}$) |
| :362 (×2) | S4-P17 | "are exactly the self-contained levels whose difference ..." / "falls at the exact equality case" | definitional identification; the algebraic equality case of @prp-naive |
| :377 | S4-P19 | "$\hat d_k = N[\log\lvert\hat\Sigma_k\rvert - \log\lvert S^{*}\rvert]$ exactly" | closed-form identity for block-diagonal constraints |
| :400 (×2) | S4-P22 | "the naive trace difference and the exact projected trace coincide" / "This is exactly the equality condition of @prp-naive" | algebraic; confirmed to $3.6\times10^{-15}$ |
| :408 | S5-P2 | "The exact alternative is data augmentation." | exact-sampler sense (standard MCMC terminology) |
| :476 | S5-P20 | table row "exact equality" | algebraic |
| :484 | S5-P21 | "overstates the exact projected trace by about $9$ percent" | "exact" names the closed-form object; "about 9 percent" is the measurement |
| :494 | S6-P2 (G1) | "its exact MCAR vanishing" | same guarded G1 framing; the $O(1/n)$ remainder is named in the same sentence |
| :496 | S6-P3 (G3) | "Exact data augmentation was not run" | sampler sense |
| :504 | S6-P4d (G9) | "the two order-one design terms in the theorem's proof cancel exactly for any canonical link" | Lemma P: an algebraic identity between the two named order-one terms — the objects are pre-scoped |
| :508 | S6-P6 | "is nonzero exactly when the missing and observed units differ on the conditioning variables" | iff on the leading-order term, as at :267 |
| :508 | S6-P6 | "an exact-engine replication" | sampler sense |

### E3 — idiomatic intensifiers: thin where cheap (6 instances, all optional)

| qmd | level3 | instance | option |
|---|---|---|---|
| :62 | S1-P5 | "the third level is met exactly to the extent the data permit" | "met to the extent the data permit" |
| :133 | S3-P4 | "is exactly that kind of error" | keep, or "is precisely that kind of error" → "is an error of that kind" |
| :168 | S4-P4 | "exactly as the EM E-step conditions on the current iterate" | keep ("in the same way as") |
| :267 | S4-P7b | "derived and measured precisely in the next part" | keep ("with precision" sense — and the paired differential is measured tightly) |
| :352 | S4-P14 | "matters instead exactly where no reference distribution stands ..." | "matters instead where ..." |
| :446 | S5-P16 | "This is exactly the failure mode the result specifies." | "This is the failure mode the result specifies." |

None of these is a magnitude claim; the case for thinning is density alone — at 49
occurrences a referee stops distinguishing the classes, and the E2 instances get laundered
by the E1/E3 bulk. Thinning even half of E3 restores the signal that a surviving "exactly"
means an identity.

## Interaction with the Phase C demonstrations

Two demonstrations contain E2 instances that their proposed texts preserved verbatim
(correctly, under the style-pass hedge invariance). If Marcus ratifies both the register
direction and this addendum, the combined wordings are:

- **Demo 2 (S1-P4):** "... and this paper's central result describes the leading term of
  that bias exactly."
- **Demo 3 (S2-P7):** "... and the main theorem quantifies that contribution to leading
  order: in the known-scale case the bias is zero under improper imputation at the
  observed-data estimate but $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ under proper
  imputation, so the two forms differ, to leading order, by the posterior-draw
  contribution."

All other demonstrations are unaffected (their "exactly" instances are E1: Demo 4's
"exactly half" and "by exactly that surplus" — the latter borderline #7 above).

## What this addendum asks Marcus to decide

1. Adopt rule R11/C9 into the rubric (it becomes part of the same Phase D decisions.md
   amendment set).
2. Authorize the six E2 rescopes as a claim-strength change (its own dated line item).
3. Call the two borderline instances (#7, #8).
4. Choose whether to thin the E3 set (recommended: yes, all six — cost is zero).

Companion check for Phase D: `derivation.qmd` and the response letter use the same
vocabulary and are OUT of the todo/048 scope; if the rule is adopted, a one-off grep pass
over them should be queued as a separate follow-up so the documents do not drift apart.
