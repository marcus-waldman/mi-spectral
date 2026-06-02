# Layer-3 cross-model adversarial package — realized- vs expected-information O(1) term (todo/018)

**Purpose.** A self-contained packet for a *different model family* (GPT-5.5 via API) to derive,
from scratch and blind, the one load-bearing object of todo/018: under ignorable **MAR** on a
**non-monotone** Gaussian design, the **O(1) difference between two information conventions** used to
form the relative increase in variance (RIV) that the multiple-imputation deviance numerator is
referred to — the **realized observed information** (the negative Hessian of the observed-data
log-likelihood at the fit) versus the **naive expected information** (the Fisher information computed
by plugging the model's population conditional covariances into the per-pattern observed-data
information, with the missingness pattern treated as fixed by design).

The empirical finding to be explained (Mode B) is that a *paired* trace difference between these two
information conventions is an **O(1)** quantity under MAR, roughly stable in the sample size `n`. Is
that a genuine leading-order effect of MAR selection, or a finite-`n` artifact? Derive it.

**Sequencing:** Mode A first (blind: from scratch, is `E[observed info] = expected info` under MAR,
and if not what is the discrepancy), then Mode B (red-team the claim that the two conventions
coincide to leading order). Grade against the key at the bottom (★ GRADING KEY — REMOVE BEFORE
SENDING ★; the runner hard-truncates there). Independence is on the MODEL axis.

---

## GRADING OUTCOME (run 2026-06-02, gpt-5.5, reasoning_effort=medium)

Responses: `verification/cache/layer3-gpt-5.5-acinfo-mode{A,B}.md`. Both high quality, on-target, and
in **complete agreement** with the WAY-1 Claude analytic derivation (`verification/term-ac-realized-info.R`).

**Cross-model agreement (the bar — met on every load-bearing point).**
- **`E[i_O] ≠ i_N` under MAR.** Mode A (blind) derived, from scratch, that the expected realized
  observed information replaces the population residual moments by the per-pattern **selected** moments
  `m_r^sel = E[e_r|R=r]` (cross block) and `C_r^sel = E[e_r e_r^⊤|R=r]` (Σ block) — exactly WAY-1's
  `I_U` build from `m1_P, M2_P`.
- **`ΔI` block structure (identical).** `μμ` block `= 0`; `μ–vechΣ` cross block `∝ m_r^sel` (the
  selection shift `i_N` drops); `vechΣ` block `∝ C_r^sel − Σ_OO` (selected-minus-population 2nd
  moment). Same boxed forms in Mode B (eqs 9–11 ↔ WAY-1 cross/Σ blocks).
- **Closed form (identical).** `D = tr(J_N^{-1} J_com) − tr(J_O^{-1} J_com) = tr(J_N^{-1} ΔJ J_O^{-1} J_com)`,
  via the same inverse identity `A^{-1}−B^{-1}=A^{-1}(B−A)B^{-1}` — exactly WAY-1's
  `tr(I_N^{-1} I_com) − tr(I_U^{-1} I_com)`.
- **Order `O(1)` under MAR (the prior blind spot, now cleared).** BOTH modes get `D = O(1)` ("neither
  `O(n)` nor `O(n^{-1})`; the `n`'s cancel in the trace functional"). Mode B (red-team) **explicitly
  rejects** the offered `O(n^{-1})` off-ramp: "shifted at **population order**, i.e. `O(1)` per
  observation, not `O(n^{-1})`." This is the exact error todo/016's Mode B made (calling the
  realized-vs-expected gap `O(1/n)`) — **not repeated** by an independent run.
- **`D = 0` iff MCAR.** Both give the necessary-and-sufficient condition `m_r^sel = 0` and
  `C_r^sel = Σ_OO`, automatic under MCAR — matching WAY-1 + K&M.
- **Recommendation (spontaneous).** Mode A, unprompted, cites **Kenward & Molenberghs** (plus Louis
  1982, Efron–Hinkley 1978) and concludes "**Use the observed information, i.e. the realized negative
  Hessian**" — the exact Step-0 verdict, recovered blind off the Claude lineage.

**Net / disposition.** The realized-information term is **derived two independent ways that agree**:
WAY-1 (Claude analytic, numeric `Δ_KM ≈ −0.55` non-monotone / `−0.44` monotone, build vs MC to
`1e-11`, MCAR `→ 0`) and WAY-2 (GPT-5.5 blind + red-team, symbolic, `O(1)`-under-MAR, `0`-iff-MCAR,
K&M recommendation). The convention is settled (observed/realized; K&M 1998), the `(A)+(C)` value is
the realized `−0.34 → −0.46`, and `todo/016`'s open flag is closed. No divergence; nothing to escalate.

---

## MODE A — blind re-derivation (paste from here to the Mode-A end marker)

> You are a mathematical statistician. Solve the following self-contained problem from scratch,
> using only your own knowledge of likelihood theory and missing-data asymptotics. Show every step
> and name the standard results you use. Do not assume a particular final number.
>
> **Setup.** `X ~ N(μ, Σ)` in `ℝ^p`, parameter `θ = (μ, vech Σ)`. We observe `n` i.i.d. units; on
> each unit some coordinates are missing under an **ignorable MAR** mechanism whose propensity
> depends only on coordinates that are *always observed* (so the mechanism is genuinely MAR and its
> parameter is distinct from `θ`). The pattern is **non-monotone** (incomplete patterns do not nest),
> so the observed-data likelihood does not factor into a sequence of complete-data regressions. Let
> `ℓ_obs(θ) = Σ_i log p(y_i^{O_i}; μ_{O_i}, Σ_{O_i O_i})` be the observed-data (FIML) log-likelihood,
> `θ̂` its maximizer (consistent for the truth `θ₀` under ignorability).
>
> **Two information matrices.** Consider two `k×k` matrices for the same model and data
> (`k = p + p(p+1)/2`):
>
> 1. The **observed information** `i_O(θ) = −∇²_θ ℓ_obs(θ)`, the realized negative Hessian. It is
>    *data-dependent*: for a Gaussian, its `vech Σ` block depends on the observed residual
>    second moments `Σ_i e_{O_i} e_{O_i}^⊤` and its `μ–vech Σ` cross block depends on the observed
>    residual sums `Σ_i e_{O_i}` (where `e_{O_i} = y_i^{O_i} − μ_{O_i}`).
> 2. The **naive expected information** `i_N(θ)`, obtained by taking the expectation of the
>    per-pattern observed information **as if the pattern were fixed by design** — i.e. replacing the
>    observed residual moments by their *population* values under `X ~ N(μ,Σ)` (`E[e_O]=0`,
>    `E[e_O e_O^⊤]=Σ_{OO}`). For the Gaussian this `i_N` is **block diagonal** in `(μ, vech Σ)` (the
>    cross block vanishes because `E[e_O]=0`).
>
> **Question.** Work to leading order in `n`, at `θ = θ₀`.
>
> 1. Compute `E[i_O(θ₀)]`, the expectation of the realized observed information under the **true
>    data-and-missingness law** (the *unconditional* law that includes the random missingness
>    pattern), for the Gaussian. Be explicit about which law each expectation is taken under. Does
>    `E[i_O(θ₀)] = i_N(θ₀)`? In particular, evaluate `E[e_{O} | unit is in pattern P]` and
>    `E[e_{O} e_{O}^⊤ | unit is in pattern P]` for an **incomplete** pattern `P` — are these the
>    population `0` and `Σ_{OO}`, or are they shifted because the units falling in pattern `P` are a
>    **selected** subsample (their always-observed coordinates have a propensity-weighted law)?
> 2. If `E[i_O] ≠ i_N`, give the discrepancy `ΔI := E[i_O(θ₀)] − i_N(θ₀)` in closed form. Identify
>    which blocks (`μμ`, `μ–vech Σ`, `vech Σ–vech Σ`) are nonzero and which **selected moments**
>    carry them (the per-pattern selected residual mean and the selected residual second moment).
> 3. Let `I_com` be the complete-data expected information and define the trace functional
>    `T(i) := tr(i^{-1} I_com)` (the object the RIV is built from). Give the leading-order
>    `D := T(i_N) − T(E[i_O]) = tr(i_N^{-1} I_com) − tr(E[i_O]^{-1} I_com)`. State its order in `n`
>    (is it `O(1)`, `O(n)`, or `O(n^{-1})`?). Prove that `D = 0` under **MCAR** and is generically
>    nonzero under **MAR**, and give the necessary-and-sufficient condition for `D = 0`.
> 4. State which standard references first made the observed-vs-expected information distinction
>    matter specifically for **MAR** missing-data inference, and what they recommend.

<!-- MODE-A END -->

---

## MODE B — adversarial red-team (paste the brief + the lemma sheet + this prompt)

> You are an adversarial referee. Below is a claim and an empirical fact that appear to conflict.
> Find which is wrong, or reconcile them, with specific technical argument.
>
> **The claim.** For FIML on a non-monotone MAR Gaussian design, the relative-increase-in-variance
> trace `T(i) = tr(i^{-1} I_com)` (with `I_com` the complete-data information) is **insensitive to
> the information convention** to leading order: whether one uses the realized observed information
> `i_O = −∇²ℓ_obs` or the naive expected (Fisher) information `i_N` that plugs in the population
> conditional covariances `Σ_{OO}` with the pattern treated as fixed, the difference
> `D = tr(i_N^{-1} I_com) − tr(i_O^{-1} I_com)` is `O(n^{-1})` and vanishes asymptotically. Hence the
> design-imbalance correction to the deviance numerator does not depend on which information one
> subtracts.
>
> **The empirical fact.** A direct, **paired** high-replication simulation of
> `D = tr(i_N^{-1} I_com) − tr(i_O^{-1} I_com)` (both evaluated at the same FIML fit on the same
> dataset, then averaged) gives, for a four-variate non-monotone MAR design, a value of order
> **a few tenths in magnitude that is roughly stable across `n`** (it does not shrink like `1/n`),
> and it goes to `0` when the same design is made MCAR (pattern assigned independently of the data).
>
> **Your tasks — do not skip any.**
> 1. Is the claim `D = O(n^{-1})` correct under MAR? Compute `E[i_O(θ₀)]` under the true
>    data-and-missingness law and compare to `i_N(θ₀)`. The crux: for an **incomplete** pattern `P`,
>    are the *selected* residual moments `E[e_O | P]` and `E[e_O e_O^⊤ | P]` equal to the population
>    `0` and `Σ_{OO}`? Under MAR the propensity depends on the always-observed coordinates, so units
>    in pattern `P` are a **selected** subsample. Decide whether this selection shifts the moments at
>    `O(1)` or only `O(n^{-1})`.
> 2. If `E[i_O] − i_N` is a nonzero `O(1)` matrix, give it in closed form, name the blocks that are
>    nonzero (in particular the `μ–vech Σ` cross block that `i_N` sets to zero), and the selected
>    moments that carry them. Confirm it vanishes under MCAR.
> 3. Hence give the order of `D = tr(i_N^{-1}I_com) − tr(E[i_O]^{-1}I_com)` in `n`, and the
>    necessary-and-sufficient condition for `D = 0`. Decide: is the empirical "few tenths, n-stable,
>    zero under MCAR" consistent with a **genuine `O(1)` MAR effect**, or with a finite-`n` artifact?
> 4. Verdict: does the information convention matter at `O(1)` for the RIV trace under MAR, or not?
>    What single computation settles it beyond doubt?

### Lemma sheet (hand to the model with Mode B)

- **Setup recap.** `X~N(μ,Σ)`; FIML observed-data log-likelihood
  `ℓ_obs(θ) = Σ_i log φ(y_i^{O_i}; μ_{O_i}, Σ_{O_i O_i})`. `i_O = −∇²ℓ_obs` (realized);
  `i_N` = per-pattern Fisher info with population moments, pattern fixed (block-diagonal in
  `(μ, vech Σ)`). `I_com` = complete-data expected information. `T(i)=tr(i^{-1}I_com)`.
- **Gaussian observed-info blocks (per pattern `P`, observed set `O`, `n_P` units).** With
  `S = Σ_{OO}^{-1}`, `M_P = Σ_{i∈P} e_{O,i} e_{O,i}^⊤`, `r_P = Σ_{i∈P} e_{O,i}`:
  μ-block `n_P S`; `vech Σ` block depends on `M_P` (equals the population form when `M_P → n_P Σ_{OO}`);
  μ–`vech Σ` cross block `∝ r_P` (equals `0` when `r_P → 0`).
- **MAR / ignorability.** The mechanism depends only on always-observed coordinates ⇒ no score for
  `θ`; but units in a given incomplete pattern are a **selected** subsample of the data law (their
  always-observed coordinates are propensity-shifted), so any moment averaged over the units of a
  pattern uses the **selected** law, which differs from the population law unless MCAR.
- **MLE asymptotics.** `√n(θ̂−θ₀) ⇝ N(0, i^{-1})` with `i` the unconditional expected information
  `= E[i_O]`; the bias of `θ̂` is `O(n^{-1})`.

---

## ★ GRADING KEY — REMOVE BEFORE SENDING TO ANY MODEL ★

*(Never paste below this line into the API call. For the author's grading only. The runner
`verification/run_layer3_openai.py` hard-truncates at this `##` header.)*

**Our position (todo/018, Step 0 + WAY-1 analytic).** Step 0 settled the convention from
Kenward & Molenberghs (1998, *Statistical Science*): under MAR the **observed** (realized Hessian)
information is the principled choice; the naive expected (population-`Σ_OO`, pattern-fixed) Fisher
information is **biased**, and the bias is **zero iff MCAR** (their bivariate-Gaussian §3.2 gives the
nonzero `μ–σ` cross terms `∝ α_1 = E(Y_1|r=1)−μ_1`, the selection shift). So `−0.46` (realized) is the
correct `(A)+(C)`; `−0.22` is the naive expected-info value.

**WAY-1 (Claude analytic, `verification/term-ac-realized-info.R`).** `ΔI := E[i_O]−i_N` has: zero
`μμ` block; a `vech Σ` block `∝ (M2_P^sel − Σ_OO)` (selected-vs-population 2nd moment); and a
`μ–vech Σ` **cross block `∝ m1_P^sel = E[e_O|P]`** (the K&M selection shift) that `i_N` drops. Built
from the per-pattern selected moments it reproduces `E[observed_info]` to `1e-11`. The trace gap
`D = tr(i_N^{-1}I_com) − tr(E[i_O]^{-1}I_com)` is `O(1)` under MAR (`≈ −0.5` at `θ₀`, non-monotone),
`≈ 0` under MCAR, matching the committed lavaan paired gap (`−0.63→−0.58`, at `θ̂`).

**High-value catches / agreement bar (cross-check vs Claude's WAY-1):**
- **(Agreement.)** GPT-5.5 derives, blind, that `E[i_O] ≠ i_N` under MAR by an `O(1)` matrix whose
  **`μ–vech Σ` cross block** is carried by the **selected residual mean** `E[e_O|P] ≠ 0`, vanishing
  iff MCAR — i.e. the same `ΔI` and the same necessary-and-sufficient condition. If it independently
  reproduces the cross-block / selected-moment mechanism and the `O(1)`-under-MAR order, the two
  lineages **agree** and the realized convention (`−0.46`) is confirmed derived two ways.
- **(Strong independent signal.)** GPT-5.5 spontaneously cites Kenward & Molenberghs (1998) / Little
  & Rubin's observed-information recommendation under MAR — not prompted in the blind text.
- **(Escalate / divergence.)** GPT-5.5 argues `D = O(n^{-1})` (Mode B task 1) — i.e. the selection
  shift is finite-`n`, not `O(1)`. That would contradict WAY-1 and the empirical; investigate (this
  is the exact failure mode todo/016 Mode B hit when it wrongly called the realized-vs-expected gap
  `O(1/n)`).

**Divergence trigger to escalate:** Mode A (blind) concludes the two conventions coincide at `O(1)`
(`E[i_O] = i_N` under MAR) — the opposite of WAY-1. Then re-examine the selected-moment argument
before trusting either.
