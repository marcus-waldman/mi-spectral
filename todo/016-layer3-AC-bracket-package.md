# Layer-3 cross-model adversarial package — non-monotone (A)+(C) completeness (todo/015)

**Purpose.** A self-contained packet for a *different model family* (GPT-5.5 via API) to
stress-test the one load-bearing judgment of todo/015: under congenial proper MI / FIML on a
**non-monotone MAR** design, is the leading-order O(1) design-imbalance term **fully**
`(A)+(C) = αᵀE[δ] + ½ tr(H_φ I_obs⁻¹)` (two terms, ≈ −0.22), or is there a **third O(1) term**
— a selected-vs-population missing-information / cross eval–impute curvature residual — that
would lift it toward the empirical ≈ −0.46?

This is genuinely open: our own finite-difference probe of the candidate third term was dominated
by single-dataset sampling noise (±0.3) and did not settle it. Independence is on the MODEL axis.

**Sequencing:** Mode A first (blind: enumerate every O(1) term from scratch), then Mode B
(red-team our two-term decomposition against the empirical gap). Grade against the key at the
bottom (★ GRADING KEY — REMOVE BEFORE SENDING ★; the runner hard-truncates there).

---

## GRADING OUTCOME (run 2026-06-02, gpt-5.5, reasoning_effort=high)

Responses: `verification/cache/layer3-gpt-5.5-ac-mode{A,B}.md`. Both high quality and on-target.

**What GPT-5.5 caught (a real, independent catch).** The two-term claim **is incomplete in form**.
Mode A (blind) reproduced the exact expansion `A_rb = g'δ + δ'Cδ + ½δ'Hδ` and showed the gradient
term carries **two** O(1) pieces, not one:
`E[g'δ] = E[g]'E[δ] + tr(I_obs⁻¹ Cov(S_obs, g))`. Our analytic assembly *and* our FD
"cross-check" both computed only `E[g]'E[δ]` (the (A) term) — sharing the omission, which is why
they agreed at −0.22. Mode A also derived `C = conditional missing information` and, by Louis,
`tr(E[C] I_obs⁻¹) = RIV` (the cross term cancels with the consistent `I_com−I_obs` definition).
Mode B reframed the candidate gap as a selected-vs-population missing-info `Δ`, *with the correct
caveat* that `Δ` cancels when the RIV uses the selected (Louis) missing information.

**Verification of the named terms** (`verification/scratch-bcov-check.R`,
`verification/scratch-realized-vs-expected.R`):
- `B_cov = tr(I_obs⁻¹ Cov(S_obs, g))` = **−0.02** (MAR), −0.006 (MCAR): a genuine term that
  vanishes under MCAR exactly as predicted, but **numerically tiny** — it does *not* supply the
  ≈ −0.24 gap. So `(A)+(C)+B_cov ≈ −0.24`, still far from the empirical −0.46.
- `Δ` (cross-Hessian bracket) → **0** to leading order: by Louis the committed RIV (= `I_com−I_obs`)
  already uses the *selected* missing information, so `tr(E[C] I_obs⁻¹) = RIV` exactly; the noisy
  single-dataset bracket values were realized-vs-expected sampling noise.
- The actual O(1) carrier appears to be the **realized-vs-expected observed information**: the
  empirical `rem` subtracts the realized observed-info Hessian, and (paired, precise)
  `tr(RIV; realized) − tr(RIV; expected Fisher) ≈ +0.6`, roughly N-stable (−0.62 @800 → −0.59
  @1500). GPT-5.5 Mode B §4 dismissed this as O(1/n) — **incorrectly**; under MAR selection it
  looks O(1).

**Lavaan re-measurement result (2026-06-02, `verification/scratch-rem-realized-expected-lavaan.R`,
`cache/rem-realized-expected-lavaan.rds`).** Redid the realized-vs-expected check with **lavaan
FIML** (em_mvn was unreliable here). Lavaan reproduces the committed `rem_real` sign within MCSE
(pipeline validated). The paired info-gap is pinned (±0.006): `tr_exp − tr_real = −0.63 (n=800),
−0.58 (n=1500)`, matching the em-based gap (robust). Anchoring `rem_exp = committed_rem_real − gap`:

| convention | n=800 | n=1500 |
|---|---|---|
| **realized** info (K&M; = empirical) | −0.336 | −0.456 |
| **expected** Fisher info | **+0.29** | **+0.13** |

So **(A)+(C) swings ~0.6 with the information convention**, and the analytic **−0.22 matches NEITHER
column** → **OUTCOME (b): a residual is revealed.** The likely resolution: my analytic −0.22 is the
*expected/population-information* value, while the manuscript's RIV and the empirical −0.46 use the
*realized/selected (K&M-standard)* observed information, which carries an extra **O(1) MAR term ≈ −0.6**
(the selected-vs-population second moments in the realized Hessian; zero under MCAR). i.e. **−0.46 is
plausibly the correct (A)+(C) under the K&M convention**, NOT a finite-n artifact — which **contradicts
the committed reframe** (`446d1a4`, which called −0.46 a "finite-$n$ (realized-information) offset" and
−0.22 "the leading order").

**Net / disposition (UPDATED).** The honest reframe's specifics are now **in question** — the −0.22
is the wrong information convention for the manuscript's K&M RIV. **Next step (todo):** recompute the
analytic (A)+(C) with the **realized/selected** observed information consistently (pinning the θ₀-vs-θ̂
piece) and confirm it reproduces ≈ −0.46; if it does, correct `@sec-termA` to "−0.46 = realized-info
(A)+(C); −0.22 = expected-info contrast." **Do NOT trust the committed −0.22-leading-order wording
until this is settled.** (Caveat: asymptotes are 2-point extrapolations; the gap's slight shrink
−0.63→−0.58 leaves the realized-info (A)+(C) limit uncertain — possibly more negative than −0.46.)

---

---

## MODE A — blind re-derivation (paste from here to the Mode-A end marker)

> You are a mathematical statistician. Solve the following self-contained problem from scratch,
> using only your own knowledge of likelihood asymptotics and multiple-imputation theory. Show
> every step and name the standard results you use. Do not assume a particular final number.
>
> **Setup.** `X ~ N(μ, Σ)` in `ℝ^p`, parameter `θ = (μ, vech Σ) ∈ ℝ^k`. We observe `n` i.i.d.
> units; on each, some coordinates are **missing at random** under an ignorable mechanism whose
> propensity depends only on coordinates that are *always observed* (so the mechanism is genuinely
> MAR and its parameter is distinct from `θ`). The missing-data pattern is **non-monotone** (the
> incomplete patterns do not nest), so the observed-data likelihood does not factor into a sequence
> of complete-data regressions.
>
> Let `ℓ_com(θ;Y)` be the complete-data log-likelihood; `θ̂_obs` the observed-data (FIML) MLE,
> which under ignorability is consistent for the truth `θ₀` and has an `O(n⁻¹)` bias with
> `b_Σ := lim_n n·E[Σ̂_obs − Σ₀]` (the second-order MLE bias; only its Σ-block will matter below).
> Write `I_com`, `I_obs` for the complete- and observed-data expected Fisher information,
> `I_{mis|obs} := I_com − I_obs`, and `RIV := tr(I_obs⁻¹ I_{mis|obs})`.
>
> **Imputation / Q-function.** A congenial, proper analyst imputes the missing entries by drawing
> from the fitted model `P(Y_mis | Y_obs, φ)`; define the infinite-imputation averaged
> complete-data log-likelihood, evaluated at `θ_eval` with completions drawn from `φ`,
> ```
>   F(θ_eval, φ) := E_{Y_mis ~ P(·|Y_obs, φ)} [ ℓ_com(θ_eval; Y_obs, Y_mis) ]   (sum over units).
> ```
> Form the Rao-Blackwellized imputation-bias statistic (eval and impute both at the fit, minus
> impute at the truth):
> ```
>   A_rb := F(θ̂_obs, θ̂_obs) − F(θ̂_obs, θ₀).
> ```
>
> **Question.** Compute, to leading order in `n`, the constant `D := E[A_rb] − RIV`, the
> outer expectation over the data law (and imputation draws). Specifically:
>
> 1. Expand `A_rb` in `δ := θ̂_obs − θ₀` to second order, keeping BOTH the impute-slot and the
>    eval-slot dependence. Identify every `O(1)` contribution to `E[A_rb]` in terms of: the
>    gradient `∇_φ F`, the impute-slot Hessian `∇²_φ F`, the **cross** eval–impute Hessian
>    `C := ∇_{θ_eval}∇_φ F |_{θ₀}`, `E[δ] = b_Σ/n`, and `Var(δ) = I_obs⁻¹`.
> 2. Give a probabilistic identity for `C` (hint: it involves the missing-data score). Is
>    `tr(C · I_obs⁻¹)` equal to `RIV` exactly? Compute `C` as an expectation and decide whether,
>    under **MAR selection**, the relevant conditional/missing information is evaluated on the
>    **selected (incomplete) units** or on the population — and whether those coincide.
> 3. Hence write `D` as a sum of named `O(1)` terms. State which terms vanish under **MCAR** and
>    which survive under **MAR**. Confirm the order is `O(1)` (not `O(n)` or `O(n⁻¹)`).
>
> Be explicit about which probability law each expectation is under, and flag any term that a
> two-term answer `D = αᵀE[δ] + ½ tr(∇²_φ F · I_obs⁻¹)` would miss.

<!-- MODE-A END -->

---

## MODE B — adversarial red-team (paste the brief + the lemma sheet + this prompt)

> You are an adversarial referee. Below is a claim and an empirical fact that appear to conflict.
> Find which is wrong, or reconcile them, with specific technical argument.
>
> **The claim.** For congenial proper MI / FIML on a non-monotone MAR Gaussian design, the
> `O(1)` design-imbalance constant `D := E[A_rb] − RIV` (notation as in the setup below) decomposes
> into exactly **two** terms,
> ```
>   D = (A) + (C),   (A) = αᵀ E[δ],   (C) = ½ tr(H_φ I_obs⁻¹),
> ```
> with `α = ∇_φ F|θ₀` the (covariance-only) entropy gradient, `H_φ = ∇²_φ F|θ₀` the cross-entropy
> curvature, `E[δ] = b_Σ/n` the second-order MLE bias. The claim explicitly asserts that **the
> eval-slot curvature exactly supplies `RIV`, so no further `O(1)` term enters** — i.e. the cross
> eval–impute Hessian satisfies `tr(C I_obs⁻¹) = RIV` exactly. Evaluated analytically this two-term
> `D ≈ −0.22` and is `n`-independent; the MCAR control gives `D → 0`.
>
> **The empirical fact.** A direct high-replication simulation of `D = E[A_rb] − RIV` (with `RIV`
> the realized observed-information trace at the fit) gives, for the same non-monotone design,
> `−0.34` at `n=800` and `−0.46` at `n=1500`, **still increasing in magnitude with `n`** — about
> twice the two-term constant and trending past it. (The monotone design shows the same direction:
> two-term `≈ −0.22`, empirical `−0.18 → −0.27`, increasing.)
>
> **Your tasks — do not skip any.**
> 1. Is the assertion `tr(C I_obs⁻¹) = RIV` correct **under MAR**? Derive `C = ∇_{θ_eval}∇_φ F|θ₀`
>    as an expectation. Standard arguments give `C = Σ_i E[ U_{mis|obs,i} U_{mis|obs,i}ᵀ ]` (a
>    conditional/missing-information matrix). Under MAR the units that are *incomplete* are a
>    **selected** subsample (the propensity depends on the always-observed coordinates). Does `C`
>    therefore equal the **population** `I_{mis|obs}` (giving `tr(C I_obs⁻¹)=RIV`), or the
>    **selected-subsample** missing information (giving `tr(C I_obs⁻¹) = RIV + Δ`, `Δ ≠ 0` under
>    MAR, `Δ = 0` under MCAR)? If `Δ ≠ 0`, it is a genuine **third** `O(1)` design-imbalance term
>    the two-term claim omits.
> 2. If a third term exists, give its closed form `Δ = tr((I_{mis|obs}^{sel} − I_{mis|obs}^{pop}) I_obs⁻¹)`
>    (or correct it), confirm `Δ = 0` under MCAR, and check its sign/order is consistent with the
>    empirical `D` lying *beyond* the two-term constant and growing toward it with `n`.
> 3. Alternatively, argue the gap is **not** a third leading-order term but a higher-order /
>    finite-`n` (realized- vs expected-information) artifact that vanishes as `n→∞` — in which case
>    the two-term `−0.22` is the true asymptote and the empirical `−0.46` is pre-asymptotic. Which
>    is it? Give the decisive distinguishing computation.
> 4. Verdict: is the leading-order `D` two terms (`≈−0.22`) or three (`≈−0.46`)? What single
>    computation would settle it beyond doubt?

### Lemma sheet (hand to the model with Mode B)

- **Setup recap.** `F(a,b) = Σ_i E_{Y_mis~P(·|Y_obs,b)}[ℓ_com(a; Y_i)]`;
  `A_rb = F(θ̂_obs,θ̂_obs) − F(θ̂_obs,θ₀)`; `δ=θ̂_obs−θ₀`, `E[δ]=b_Σ/n`, `Var(δ)=I_obs⁻¹`;
  `RIV = tr(I_obs⁻¹ I_{mis|obs})`, `I_{mis|obs}=I_com−I_obs`.
- **Full/observed/conditional score split (Fisher–Louis).** `U_com = U_obs + U_{mis|obs}`,
  `E[U_{mis|obs}|Y_obs]=0`, `E[U_com U_{mis|obs}ᵀ | Y_obs] = E[U_{mis|obs}U_{mis|obs}ᵀ|Y_obs] =: J_{mis|obs}(Y_obs)`.
  Population: `E_{Y_obs}[J_{mis|obs}] = I_{mis|obs}`.
- **MLE expansion.** `√n(θ̂_obs−θ₀) ⇝ N(0, I_obs⁻¹)`, plus the `O(n⁻¹)` bias `b_Σ/n`.
- **MAR / ignorability.** Mechanism depends only on always-observed coordinates ⇒ no score for
  `θ`; but the incomplete units are a *selected* subsample of the data law (their always-observed
  coordinates are shifted), so any quantity averaged over incomplete units uses the **selected**
  law, which differs from the population law unless MCAR.
- **Observation.** `J_{mis|obs}(Y_obs)` for the Gaussian depends on the observed residuals
  `e_O = Y_O − μ_O` (through the conditional-mean Jacobian `∂m/∂Σ ∝ e_O`); hence its expectation
  over the **selected incomplete** units involves the *selected* second moments `E[e_O e_Oᵀ | incomplete]`,
  not the population `Σ_OO`.

---

## ★ GRADING KEY — REMOVE BEFORE SENDING TO ANY MODEL ★

*(Never paste below this line into the API call. For the author's grading only. The runner
`verification/run_layer3_openai.py` hard-truncates at this `##` header.)*

**Our current position (todo/015, honest-reframe commit `446d1a4`).** The two-term leading-order
`D = αᵀE[δ] + ½tr(H_φ I_obs⁻¹) ≈ −0.22` is computed two independent ways (analytic α/H_φ AND
finite-differencing the analytic `F`), with MCAR control → 0. We currently treat the empirical
`−0.46` as a higher-order / realized-information gap (Mode-B task 3) and reframed the manuscript
accordingly. BUT our own finite-difference estimate of the candidate third term `Δ` was dominated
by single-dataset noise (`Δ̂ ∈ {−0.32, −0.08, +0.22, +0.38}` across seeds/N) and did NOT settle
whether `Δ` is a genuine `O(1)` term or noise around 0.

**High-value catches:**
- **(Flips our reframe.)** A clean derivation that `C = selected I_{mis|obs} ≠ population
  I_{mis|obs}` under MAR, giving a nonzero `O(1)` `Δ = tr((I_mis^sel − I_mis^pop) I_obs⁻¹)` with
  the right sign/magnitude (≈ −0.24, the gap), and `Δ=0` under MCAR. If GPT-5.5 derives this
  independently, the true `(A)+(C)` is the **three-term** `≈−0.46`, the empirical was right all
  along, and the manuscript should report the third term — NOT call `−0.46` a higher-order
  artifact. **Escalate: this reverses the disposition.**
- **(Corroborates our reframe.)** A rigorous argument that `tr(C I_obs⁻¹)=RIV` holds even under MAR
  (the selected-vs-population difference cancels / is `O(n⁻¹)`), so the two-term `−0.22` is the
  asymptote and `−0.46` is pre-asymptotic. Then Mode-B task-4's "decisive computation" tells us how
  to confirm at larger `n`.

**Divergence trigger to escalate:** Mode A (blind) spontaneously produces a third `O(1)` term from
the cross eval–impute curvature under selection — that is the strongest possible independent signal,
since it is not prompted by the empirical gap.
