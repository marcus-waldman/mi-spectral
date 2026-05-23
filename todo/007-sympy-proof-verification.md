# Todo 007 — Sympy verification of the deviance-bias theorem

**Purpose:** Self-contained operational instructions for a fresh Claude session to build a Quarto notebook that *symbolically verifies* the central theorem of the JAIGP paper (the Q-function deviance-bias decomposition) using Sympy. Companion to the numerical witness W1, sitting one rung up the rigor ladder: where W1 verifies the *answer* (E[T] ≈ +½ tr(RIV) numerically), Sympy verifies the *algebra* (the chain of identities that produces the answer).

**Last updated:** 2026-05-23 (paused mid-sweep-execution session for future pickup).

---

## Step 0 — Resume context (read in this order)

1. `CLAUDE.md` — scope, core contribution, citation discipline.
2. `IDEAS.md` — directional anchor. Key sections:
   - "Headline contribution" — the theorem stated for both decomposition halves.
   - "Methodological notes" — point 1 on the custom Cholesky + analytic gradient.
3. `verification/00-setup.R` — concrete code for I_com (`fisher_info_com_mvn`), I_obs (`fisher_info_obs_mvn`), tr(RIV) (`tr_riv_analytic`), and the analytic FIML Q-function (`barQ_fiml_analytic`). These are the load-bearing R implementations the Sympy verification should match symbolically.
4. `verification/cache/W1-prod-fiml.rds` (and the W1 sweep cache) — numerical reference values for the theorem at concrete configurations. Sympy results should match these to machine precision when evaluated at the same θ and missingness pattern.

**Sister paper:** `~/git-repositories/MI-IC/` — the v4.5 derivation source lives there in their `derivation_v4_5.md` (or equivalent). That's the human-readable proof. We are translating *that algebra* into Sympy, stripped of SEM language.

---

## Step 1 — Environment setup

Confirm Sympy ≥ 1.13 (matrix expression simplification matters; older versions are rougher).

```
py -c "import sympy; print(sympy.__version__)"
```

Quarto with the Python kernel. Engine: `jupyter` for Quarto (`quarto check`).

Output file: `manuscript/proof-verification-sympy.qmd`. Rendered HTML lives at `manuscript/proof-verification-sympy.html`, ignored by git. The `.qmd` itself is committed.

---

## Step 2 — Tier A: MVN-concrete verification

Goal: verify the theorem symbolically at the 4-dim MVN running example.

### 2.1 Setup
- Define `mu` as `MatrixSymbol(4, 1)`, `Sigma` as `MatrixSymbol(4, 4)` with `is_symmetric=True`.
- Use a small concrete missingness pattern: X_3, X_4 fully observed; X_1, X_2 each missing on roughly half the rows (split into 4 patterns: (1,1), (1,0), (0,1), (0,0), with weights w_pat summing to N).
- Avoid p > 4 if possible; the 14-dim vech(Σ) parameter space is at the edge of Sympy's comfort.

### 2.2 Fisher information identities (load-bearing)
- Closed-form `I_com(mu, Sigma)` — block-diagonal on `(mu, vech(Sigma))`. Cross-check against `fisher_info_com_mvn` in R.
- Closed-form `I_obs(mu, Sigma; pattern weights)` — pattern-mixture sum. Cross-check against `fisher_info_obs_mvn`.
- `I_mis|obs = I_com − I_obs`.
- **Verify symbolically**: `I_com = I_obs + I_mis_given_obs` (information identity). If Sympy can't simplify it directly, evaluate at a specific numeric Σ and check element-wise.

### 2.3 RIV definition + tr(RIV)
- `RIV = I_obs.inv() @ I_mis_given_obs` (Sympy `MatMul`, not numeric).
- `tr(RIV)` via `Trace(RIV).rewrite(Sum)`. May require manual rewrite rules.

### 2.4 Term B: ℓ_com expansion around θ_com
- `ell_com(theta)` for MVN is closed form. Symbolically expand to second order at `theta_com`.
- Term B = `E[ell_com(theta_obs) - ell_com(theta_com)]`. Should reduce to `-½ tr(I_com Var(theta_obs))` = `-½ tr(I_com I_obs^{-1})` = `-½ (k + tr(RIV))` = `-½ k - ½ tr(RIV)`.
- The `-½ k` is a constant (parameter dimension); the structural piece is `-½ tr(RIV)`.

### 2.5 Term A: bar Q expansion under FIML "imputation" (deterministic phi_tilde = theta_obs)
- Use the closed-form `barQ_fiml_analytic` formula from `verification/00-setup.R` lines 196-249.
- Expand around `theta_obs`. Identify the trace term that gives `+tr(I_obs^{-1} I_mis|obs Var(theta_obs))` = `+tr(RIV)`.

### 2.6 Combine
- T = A + B should reduce symbolically (or numerically at the cross-check) to `+½ tr(RIV)` plus the `-½ k` parameter-dimension constant.

### 2.7 Numerical cross-check (gate)
- Load the W1-prod cache. Pick one (theta, R) configuration from the W1 cache.
- Plug into the symbolic expressions. Verify Sympy's numerical evaluation matches the R cache's empirical mean within MCSE.

---

## Step 3 — Tier B (optional, harder): abstract generalization

Goal: verify the *general* theorem (any regular likelihood) at the symbolic block-matrix level, not committed to MVN.

### 3.1 Abstract objects
- `MatrixSymbol("I_com", k, k, positive_definite=True)`
- `MatrixSymbol("I_obs", k, k, positive_definite=True)`
- Define `I_mis_given_obs = I_com - I_obs`, take `RIV = I_obs.inv() @ I_mis_given_obs` as a defined matrix expression.

### 3.2 Score-equation expansion
- `theta_obs - theta_com = I_com^{-1} U_com(theta_com)` to leading order, where `U_com` is the complete-data score.
- `E[U_com U_com^T] = I_com`.
- `E[(theta_obs - theta_com)(theta_obs - theta_com)^T] = I_obs^{-1}` (sandwich, observed-data MLE).

### 3.3 ℓ_com second-order expansion (abstract)
- Use Sympy `MatrixSymbol` Taylor expansion or write a manual second-order expander.
- Expected output: `ell_com(theta_obs) - ell_com(theta_com) = U_com^T (theta_obs - theta_com) - ½ (theta_obs - theta_com)^T I_com (theta_obs - theta_com) + o_p(1)`.

### 3.4 Imputation-side expansion
- Bar Q under proper MI satisfies (Meng 1994): `bar Q_inf(theta) = E_{tilde phi | Y_obs}[ ell_com(theta; Y_obs, Y_mis(tilde phi)) ]`.
- Expand at `theta_obs`. The `+tr(RIV)` term should appear from the imputation variance contribution.

### 3.5 Where Sympy will likely fight you
- Symbolic `Trace[A @ B.inv() @ C]` simplification. Pattern: define helper functions that pre-cycle and pre-distribute traces.
- Non-commutative expansion of `(A + epsilon B)^{-1} ≈ A^{-1} - epsilon A^{-1} B A^{-1}` — may need to write the perturbation manually.

If Tier B hits the wall: **document where the abstract version breaks down**, scope the notebook to Tier A only with a note that Tier A's concrete MVN verification combined with W1's preregistered numerical witnesses constitutes the empirical-rigor stack for the JAIGP submission.

---

## Step 4 — Notebook structure

```
manuscript/proof-verification-sympy.qmd
├── 1. Setup and notation
├── 2. The information identity (verify I_com = I_obs + I_{mis|obs})
├── 3. Defining RIV and tr(RIV)
├── 4. Term B: -½ tr(RIV) from estimation mismatch
├── 5. Term A: +tr(RIV) from imputation bias (via FIML analytic Q)
├── 6. Combining: T = A + B = +½ tr(RIV)
├── 7. Numerical cross-check against W1 prod cache
└── 8. (Tier B) Abstract generalization
```

Each section: math statement → Sympy verification → check.

Style: terse, more verification-as-code than expository. The expository version lives in the manuscript §3.

---

## Step 5 — Done-when criteria

**Tier A complete when:**
- Information identity `I_com = I_obs + I_mis|obs` symbolically verified (or numerically verified to machine precision at multiple Σ).
- `+tr(RIV)`, `-½ tr(RIV)`, `+½ tr(RIV)` all appear as the predicted residual after the Taylor manipulation.
- Numerical cross-check against W1 cache matches within MCSE.
- Quarto renders cleanly to HTML.
- Committed to repo with a manuscript reference: §3 should add a "Symbolic verification of the algebra is in `proof-verification-sympy.qmd`" footnote.

**Tier B complete when:**
- The abstract version produces the same `+½ tr(RIV)` answer at the symbolic block-matrix level without committing to MVN.
- Document any places where Sympy required hand-holding (e.g., manual rewrite rules) — these are honest disclosures about the limits of mechanical verification.

---

## Pain points to expect (Sympy gotchas)

1. **`Trace` simplification** is incomplete. Helper: write a small `tr_simplify(expr)` that applies known identities (`Tr(A @ B) = Tr(B @ A)`, `Tr(A + B) = Tr(A) + Tr(B)`) repeatedly.
2. **Matrix inverse expansion**: `(I + eps X)^{-1}` doesn't auto-expand. Write manually.
3. **`MatrixSymbol` with structure** (symmetric, positive-definite): assumptions partially honored, especially in `.inv()`. May need explicit symmetric substitution.
4. **`vech` / duplication matrix**: not in Sympy. Build manually via index manipulation.
5. **Conditional expectations** symbolically: clunky. For the MI imputation conditional, evaluate as deterministic θ_obs (FIML-style) — matches the `barQ_fiml_analytic` strategy.

If a step truly won't go through symbolically, **fall back to numerical evaluation at a fixed Σ** and document. This is the "concrete MVN verification" half of the goal; abstract Tier B is gravy.

---

## Session log — 2026-05-23 (executed; Tier A + Tier B core done)

Delivered `manuscript/proof-verification-sympy.qmd` (committed) -> `.html` (gitignored).
Fixture generator `verification/W1-sympy-fixture.R` -> `manuscript/proof-verification-fixture.json` (committed). Renders clean with the Quarto `python3` jupyter engine.

**Done-when criteria met.** Information identity (definitional + numeric PSD of `I_mis|obs`, min eig ~ -2.6e-13); `+tr / -½tr / +½tr` all appear as exact symbolic residual-zero after the trace manipulation; numerical cross-check passes — Python reimplementations of `fisher_info_com_mvn`, `fisher_info_obs_mvn`, `barQ_fiml_analytic`, `loglik_mvn` match the R code to machine precision (I_com 2.7e-12, tr(RIV) 7e-15, barL/A/B/T diff 0.0); `½ tr(RIV)=3.837` lies within the W1-sweep-prod MCSE band of `E[T]=3.67 +/- 0.45`.

**Tier B partial-done.** The combination identity `T = ½ tr(RIV)` is verified at the abstract `MatrixSymbol` level (no MVN commitment), and the covariance input (L2) `Var(theta_obs - theta_com) = I_obs^{-1} - I_com^{-1}` is *derived* symbolically from the score relations via the cross-information projection `E[U_com U_obs^T] = I_obs`. Not attempted: a from-scratch symbolic Taylor expansion of an arbitrary log-likelihood (the lemmas L1-L4 are stated, not machine-derived from a generic density). No Mathematica fallback needed.

### CORRECTION to §2.4 above (load-bearing — fix before relying on this spec again)

§2.4 as written claims Term B `= -½ tr(I_com Var(theta_obs)) = -½ tr(I_com I_obs^{-1}) = -½(k + tr(RIV)) = -½k - ½tr(RIV)`. **This is wrong.** The second-order Taylor of `ell_com` is in the *difference* `theta_obs - theta_com` (expanded at the maximizer `theta_com`), so the relevant covariance is `Var(theta_obs - theta_com) = I_obs^{-1} - I_com^{-1}` (L2), not `Var(theta_obs)`. The k-terms cancel: `E[B] = -½ tr(I_com (I_obs^{-1} - I_com^{-1})) = -½(tr(RIV)+k - k) = -½ tr(RIV)`, with **no -½k constant.** The W1 cache confirms unambiguously (N=500: B_hat=-4.19 tracks -½tr(RIV)=-3.84, not -½(k+tr(RIV))=-10.84). The notebook flags this in a callout.

### Sympy gotchas confirmed / added (for future sessions)

1. **`sympy.simplify` raises on any `Trace` expression** (signsimp/cancel bug, sympy 1.14). Do not call it on traces. Route everything through the `trace_normal` helper in the notebook (linearity + `Trace(c*I)=c*n` + cyclic canonicalization).
2. **Cyclic invariance** of `Trace` is not built in — `trace_normal` rotates `MatMul` factors to a canonical order so `Trace(AB)` and `Trace(BA)` collapse.
3. **`MatrixSymbol` is not symmetric by default**, so `X.T` and `(X.T)^{-1}` leak and block cancellation. The notebook's `symmetric_reduce` replaces `Transpose(MatrixSymbol) -> MatrixSymbol` (all informations are symmetric by convention). Without this, Tier B leaves `Trace(I_com.T^{-1} I_com)` uncancelled.
4. **vech / duplication matrix**: built manually (mirrors `00-setup.R`); shared by NumPy and Sympy.
5. **Conditional expectations / FIML pattern-sum**: the reduction of the per-pattern conditional-variance trace terms to `tr(RIV)` does NOT go through symbolically (the "clunky" gotcha). Verified numerically instead (barQ Python==R to machine precision). The Schur-complement conditional variance is shown symbolically for one pattern as the mechanism.

### Environment note

The Quarto `jupyter` engine needs Jupyter + ipykernel, which were **not** installed in the system Python (`py`). Installed via `py -m pip install jupyter ipykernel`. `quarto check` flagged this ("Jupyter is not available"). Future sessions on a fresh box must install these before rendering.

---

## Effort estimate

| Tier | Time |
|---|---|
| A (MVN-concrete) | 2–4 hours of focused back-and-forth, expect ~half on Sympy matrix-simplification debugging |
| B (abstract) | Additional 4–8 hours; may require partial Mathematica fallback for one or two steps |
| Polish + manuscript integration | 30 min |

Realistic deliverable in a single session: **Tier A done end-to-end + Tier B's outline section with `# TODO` notes for places that need Mathematica**.

---

## Relation to the JAIGP rigor story

This notebook is the *algebraic* verification companion to W1's *numerical* verification. Together they give:
- W1: the answer is right at multiple concrete configurations (60 cells × R=2000 in the comprehensive sweep, FIML + Amelia engines).
- Sympy notebook: the chain of identities that produces the answer is mechanically checked.

A reviewer who is skeptical of the AI-assisted derivation has two independent verification artifacts to look at, neither requiring them to reverify the proof by hand.

Not a substitute for Lean/Coq formalization (see the conversation note in MEMORY archive or this commit's discussion). That remains a multi-year project. Sympy is the *high-leverage middle ground* for this paper's submission window.
