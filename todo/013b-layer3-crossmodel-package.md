# Layer-3 cross-model adversarial package (todo/013, Layer 3)

**Purpose.** A self-contained packet for a *different model family* (o-series / GPT, via API).
No repo access, no agentic rig — paste the relevant section into one API call. Two modes.
Surgical target = the **conceptual premises** the free layers (0–2) flagged, where a CAS is
silent and shared Claude priors are the only residual risk:

1. the definition of `Q̄_∞` (fitted imputation predictive vs the true conditional expectation
   `E[ℓ_com|Y_obs]`) — the free-layer fork that flips the headline sign;
2. the `−½` "MI's estimand is `θ̂_com`" premise;
3. congeniality / properness.

**Sequencing:** run **Mode A first** (blind, clean definition → does it reproduce `+½tr(RIV)`?),
then **Mode B** (red-team the manuscript's actual wording). Grade against the key at the bottom
(★ GRADING KEY — REMOVE BEFORE SENDING ★).

---

## MODE A — blind re-derivation (paste from here to the Mode-A end marker)

> You are a mathematical statistician. Solve the following self-contained problem from
> scratch, using only your own knowledge of likelihood asymptotics and multiple-imputation
> theory. Show every step and name the standard results you use.
>
> **Setup.** Let `p(x; θ)`, `θ ∈ ℝ^k`, be a regular parametric model (smooth, identifiable,
> nonsingular Fisher information, differentiation under the integral valid). Concretely you may
> take the multivariate normal `N(μ, Σ)`, `θ = (μ, vech Σ)`. We observe `n` i.i.d. units; on each,
> some coordinates are **missing at random** under an ignorable mechanism (missingness depends
> only on observed coordinates; its parameter is distinct from `θ`).
>
> `ℓ_com(θ; Y)` is the complete-data log-likelihood, MLE `θ̂_com`. `ℓ_obs(θ; Y_obs)` is the
> observed-data log-likelihood, MLE `θ̂_obs`. Write `I_com`, `I_obs` for the complete- and
> observed-data expected Fisher information, `I_{mis|obs} := I_com − I_obs`, and
> `RIV := tr(I_obs⁻¹ I_{mis|obs})`.
>
> **The imputation/Q-function — read carefully.** An analyst fits a *congenial, proper*
> imputation model to `Y_obs`, obtaining imputation parameter `φ̂` (under congeniality `φ̂` is the
> observed-data fit, i.e. `φ̂ = θ̂_obs`, possibly with a proper posterior draw around it). Missing
> entries are completed by **drawing from the fitted model** `P(Y_mis | Y_obs, φ̂)`. The
> infinite-imputation averaged complete-data log-likelihood is
> ```
>   Q̄_∞(θ) := lim_{m→∞} (1/m) Σ_l ℓ_com(θ; Y_obs, Ỹ_mis^(l)),   Ỹ_mis^(l) ~ P(· | Y_obs, φ̂).
> ```
> **Note the averaging law is the FITTED model at `φ̂`, NOT the true data law at the unknown `θ0`.**
> (These coincide only if `φ̂ = θ0`; they do not, and the difference is part of what you must find.)
>
> **Question.** Compute, to leading order in `n`, `E[ T ] = E[ Q̄_∞(θ̂_obs) − ℓ_com(θ̂_com; Y) ]`,
> the outer expectation over the data law (and the imputation draws). Express the answer in terms
> of `RIV` and any design-dependent quantities. State separately how the answer changes between
> MCAR and MAR. Be explicit about which probability law each expectation is taken over, and about
> whether `E[ Q̄_∞(θ̂_obs) − ℓ_com(θ̂_obs; Y) ]` is or is not zero, with proof.

<!-- MODE-A END -->

---

## MODE B — adversarial red-team (paste the brief + the lemma sheet + this prompt)

> You are an adversarial referee. Below is a derivation claiming that, under congenial proper
> multiple imputation, `E[ Q̄_∞(θ̂_obs) − ℓ_com(θ̂_com) ] = +½ tr(RIV) + [(A)+(C)] + O(n⁻¹)`,
> decomposing as `E[A] = +tr(RIV) + (A)+(C)` (imputation bias) and `E[B] = −½ tr(RIV)`
> (estimation mismatch). Your job is to **find the error or the weakest premise**. Be specific and
> technical. In particular, address — do not skip — each of the following:
>
> 1. **The definition of `Q̄_∞`.** The derivation defines `Q̄_∞(θ) := E[ℓ_com(θ;Y) | Y_obs]`,
>    "the expectation over the imputation posterior." Is that equality correct? `θ̂_obs` is a
>    function of `Y_obs` alone. If `Q̄_∞(θ̂_obs)` were literally `E[ℓ_com(θ̂_obs;Y)|Y_obs]` under
>    the *true* data law, what would the tower property give for `E[Q̄_∞(θ̂_obs) − ℓ_com(θ̂_obs)]`,
>    and what would that do to the headline sign? Does the proof's Term-A step (which averages the
>    missing-data log-density under the *imputation* parameter `φ̃` vs the *truth* `θ0`) silently
>    use a different object than the definition advertises? Pin down exactly which object yields
>    `+tr(RIV)` and which yields `0`, and decide which one the stated definition denotes.
>
> 2. **The `−½` term.** `E[B] = E[ℓ_com(θ̂_obs) − ℓ_com(θ̂_com)] = −½ tr(RIV)` is claimed to arise
>    because MI's estimand is `θ̂_com` and the relevant variance is `Var(θ̂_obs − θ̂_com) =
>    I_obs⁻¹ − I_com⁻¹` (NOT `Var(θ̂_obs)`, which would give `−½k`). Verify or refute, including
>    the claim `Cov(θ̂_obs, θ̂_com) = I_com⁻¹`.
>
> 3. **Congeniality / properness.** Are R4–R7 (Meng congeniality, Rubin properness, self-
>    efficiency, `m→∞`) actually used where claimed, and are they sufficient for
>    `Var(θ̂_obs) = T_∞ = I_obs⁻¹` and for the Term-A cross-term `Cov(φ̃, θ̂_obs) = I_obs⁻¹`?
>
> 4. **MAR `(A)+(C)`.** The derivation claims an extra `O(1)` design-imbalance term under MAR
>    (zero under MCAR), bivariate-monotone closed form `(n_mis/n_obs)[1 − ½ tr(Q_mis Q_obs⁻¹)]`.
>    Is the order count (`O(1)`, not `O(n)` or `O(n⁻¹)`) and the MCAR-cancellation correct?
>
> Conclude with: is the headline sign robust, and if not, what minimal restatement of the
> definitions would make the `+½ tr(RIV)` claim correct and unambiguous?

### Lemma sheet (verbatim source excerpts; hand to the model with Mode B)

All quotations are from the cited sources' local copies (`literature/<key>.md`), reproduced for
the red-team's reference.

- **MLE linear expansion / Fisher info (van der Vaart 1998, Thm 5.39).**
  `√n(θ̂_n − θ) = n^{-1/2} Σ_i I_θ⁻¹ ℓ̇_θ(X_i) + o_P(1) ⇝ N(0, I_θ⁻¹)`; `P_θ ℓ̇_θ = 0`,
  `P_θ ℓ̈_θ = −I_θ`. Hence `Var(θ̂_obs)=I_obs⁻¹`, `Var(θ̂_com)=I_com⁻¹`.

- **Fisher / Louis score identity (Schafer 1997, eq 3.2; van der Vaart score-mean-zero).**
  `ℓ(θ|Y) = ℓ(θ|Y_obs) + log P(Y_mis|Y_obs,θ) + c`. Differentiating and taking `E[·|Y_obs]`:
  `U_obs = E[U_com | Y_obs]`; hence `Cov(U_obs, U_com) = Var(U_obs) = I_obs`, and
  `Cov(θ̂_obs, θ̂_com) = I_obs⁻¹ I_obs I_com⁻¹ = I_com⁻¹`, so
  `Var(θ̂_obs − θ̂_com) = I_obs⁻¹ − I_com⁻¹`.

- **Missing-information identity (Schafer 1997, eq 3.19).**
  `I_c(θ) = I_o(θ) + I_m(θ)` (complete = observed + missing), `≽ 0`. With our notation
  `I_com = I_obs + I_{mis|obs}`, so `tr(I_obs⁻¹ I_com) = k + tr(RIV)`.

- **Congeniality (Meng 1994, Defs 1–2).** `[θ̂(Z_o),U(Z_o)] ≃ [E_f(θ|Z_o),V_f(θ|Z_o)]`,
  `[θ̂(Z_c),U(Z_c)] ≃ [E_f(θ|Z_c),V_f(θ|Z_c)]`, and `f(Y_mis|Z_o)=g(Y_mis|Z_o,A)`.

- **Variance recovery (Rubin 1987, §4.2 Result 4.1).** Under proper MI with a randomization-valid
  complete-data inference, the infinite-`m` `T_∞` is randomization-valid for `T_0`; combined with
  regularity, `T_∞ = Var(θ̂_obs) = I_obs⁻¹` (this is what identifies `RIV` with Rubin's `r_∞`).

- **Ignorability (Rubin 1976; Little & Rubin 2019, Def 6.4 / Thm 6.1A).** MAR + distinct
  parameters ⇒ the mechanism contributes no score for `θ`; every identity above holds under MAR.

- **The proof's Term-A step (verbatim from the manuscript, for the red-team to scrutinize).**
  "`A = E_{Y_obs}[ E_{φ̃}[ℓ_mis|obs(θ̂_obs)] − E_{θ0}[ℓ_mis|obs(θ̂_obs)] ]`" — i.e. the
  missing-data log-density averaged under the imputation parameter `φ̃` minus under the truth
  `θ0`. With `Cov(φ̃, θ̂_obs)=I_obs⁻¹`, the cross-term gives `tr(I_{mis|obs} I_obs⁻¹)=tr(RIV)`.

---

## ★ GRADING KEY — REMOVE BEFORE SENDING TO ANY MODEL ★

*(Never paste below this line into the API call. For the author's grading only.)*

**What the free layers (0–2) established, run to ground numerically:**

- **Mode-A expected outcome:** with the *fitted-imputation* definition pinned (as written above),
  a correct derivation lands on `E[T] = +½ tr(RIV) + [(A)+(C)] + O(n⁻¹)`, with
  `E[A] = +tr(RIV) + (A)+(C)` and `E[B] = −½ tr(RIV)`. Confirmed empirically (FIML & Amelia):
  `E[A]/tr(RIV) ≈ 1`, `E[T]/(½tr(RIV)) ≈ 1`. A model that still returns `−½` even with the fitted
  definition explicit is over-anchored on the tower-property shortcut — investigate.

- **Mode-B expected high-value catch:** the equality `Q̄_∞ = E[ℓ_com|Y_obs]` is the soft spot.
  Read as the *true*-law conditional expectation, `θ̂_obs`'s `Y_obs`-measurability ⇒
  `E[A] = 0` by the tower property ⇒ headline flips to `−½ tr(RIV)`. **8 of 9 blind Claude
  re-derivations took this reading.** The `+½` requires `Q̄_∞` to average over the *fitted* model
  `P(·|Y_obs, φ̂)`, `φ̂ ≈ θ̂_obs ≠ θ0`; the proof body uses this (correct) object, but the D9
  *notation* advertises the (wrong) oracle object. A sharp red-team should flag this; if it does,
  that corroborates the Layer-0 finding from an independent model family.

- **Robust (do not expect refutation):** `E[B] = −½ tr(RIV)` with `Var(θ̂_obs−θ̂_com)=I_obs⁻¹−I_com⁻¹`
  (9/9 blind + framing-independent routes + CAS + experiment). The MAR `(A)+(C)` term, order `O(1)`,
  zero under MCAR (re-derived independently by route R2 *and* by Wolfram `verify_term_ac.py`).

**Divergence triggers to escalate:** a Mode-A model returning `−½` *with the fitted definition
explicit*; a Mode-B model that refutes `Var(θ̂_obs−θ̂_com)=I_obs⁻¹−I_com⁻¹`; or any principled
objection to congeniality giving `Cov(φ̃,θ̂_obs)=I_obs⁻¹`.
