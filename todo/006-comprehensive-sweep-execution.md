# Todo 006 — Comprehensive sweep: execution checklist for fresh session

**Purpose:** This file is self-contained operational instructions for a fresh Claude session to implement and execute the comprehensive sweep designed in `todo/005-comprehensive-sweep-hypotheses.md`. Read this file + the listed context files in order, then execute the steps.

**Last updated:** 2026-05-23.

---

## Step 0 — Resume context (read in this order)

1. `todo/000-current-status.md` — overall project status.
2. `IDEAS.md` — directional anchor including the W1/W2/W3 empirical findings.
3. `CLAUDE.md` — scope and core contribution.
4. `todo/004-simulation-hypotheses.md` — original preregistered hypotheses (frozen at SHA ddc9037).
5. **`todo/005-comprehensive-sweep-hypotheses.md` — the new preregistered sweep hypotheses (THIS sweep is testing these).**
6. Skim `verification/00-setup.R`, `verification/W1-bias-decomposition.R`, `verification/W3-model-selection.R` to see existing infrastructure.

---

## Step 1 — Sign-off check

Before any code:
- Confirm with the user that todo/005 has been read and signed off (the sweep hypotheses are frozen).
- If not yet signed off, pause and request sign-off. **Do not run the sweep against un-signed-off predictions.**

---

## Step 1.5 — Confirmed design decisions (user sign-off 2026-05-23)

Three design choices the user confirmed in conversation; bake into the sweep code:

1. **Monotone missingness rate spec**: 40% on the **deepest variable (X_4)**. Pattern frequencies chosen so X_4 marginal rate is 40%; X_3 ≈ 25%, X_2 ≈ 10%, X_1 = 0% (always observed). Most natural analog to the non-monotone 40%-on-tested-partition spec.

2. **Pre-flight tr(RIV) table** (Step 6b below): compute analytic tr(RIV) per candidate per pattern before the sweep. Documents the empirical anchor for H1 and lets us flag pattern-specific surprises before committing R=2000 of compute.

3. **Warm starts in `chan_smi_test_k1`** for Chan SMI's LOO fits. Specifics:
   - Modify `mle_chol_sigma12` (and its W3 analogs for the candidate-model constraints) to accept optional `par_init` argument; if provided, skip data-derived initialization.
   - In `chan_smi_test_k1`: fit stacked-all first, save resulting Cholesky params, pass as `par_init` to all leave-one-out fits.
   - Single-imputation fits use data-derived initial (different dataset size; warm-start from stacked-all may not help).
   - Expected speedup: 2–3× on Chan SMI at M=200 (LOO fits dominate); modest at M=20.

## Step 2 — Implement the `mice::ampute` wrapper

Goal: a function `apply_missingness_ampute(X, prop, mech, pattern_type)` in `verification/00-setup.R` that produces missingness via `mice::ampute()` and returns `list(Y, R)` matching the format of the existing `apply_mar`.

**Arguments:**
- `X` — complete-data matrix (N × p).
- `prop` — target marginal missingness (default 0.40).
- `mech` — "MAR" or "MNAR" (no MCAR in this sweep).
- `pattern_type` — "non_monotone" or "monotone".

**For non-monotone** (matches our preregistered setup):
- Pattern matrix: independent missingness on X_1 and X_2, X_3 and X_4 always observed.
- Specify via `mice::ampute(X, prop = prop, patterns = rbind(c(0,1,1,1), c(1,0,1,1), c(0,0,1,1)), freq = ..., mech = mech)`.
- Tune `freq` so marginal rate on X_1 and X_2 averages `prop`.

**For monotone:**
- Pattern matrix: `rbind(c(1,1,1,0), c(1,1,0,0), c(1,0,0,0))`.
- `freq` chosen so X_4 has roughly `prop` marginal rate (deepest variable).

**MAR weights:** for MAR, set `weights` matrix so missingness depends on observed variables (analog to our existing apply_mar's dependence on X_3 / X_4).

**MNAR weights:** for MNAR, set `weights` matrix so missingness depends on the missing variables themselves.

**Return:** `list(Y = matrix-with-NAs, R = 0/1-mask)` exactly matching `apply_mar`'s output format so it can drop into existing W1/W3 scripts.

---

## Step 3 — Validation smoke test

Create `verification/00-test-ampute-vs-apply-mar.R`:

1. At a tuned matching cell (apply_mar's existing parameters → ampute's MAR with patterns + prop adjusted to match), generate N=10000 samples with each method.
2. Verify marginal missingness rates match within 1 pp.
3. Verify the conditional structure approximately matches (e.g., P(X_1 missing | X_3 above/below median) is similar).
4. Print PASS / FAIL.

**Gate:** if the smoke test fails, debug before proceeding to the sweep.

---

## Step 4 — Implement uncongeniality wiring

In `verification/00-setup.R`, add an `empri` argument to `impute_mvn_amelia`:

```r
impute_mvn_amelia <- function(Y, M, empri = 0, ...) {
  # pass empri to Amelia::amelia(..., empri = empri)
}
```

Default `empri = 0` preserves existing behavior (congenial). When called with `empri = 0.5 * N`, generates uncongenial imputations per the preregistered §0.5.

---

## Step 5 — Update W3 script to accept sweep parameters

Either:
- (a) Modify `verification/W3-model-selection.R` to accept extra CLI args for `pattern`, `mech`, `empri`, `prop`.
- (b) Write a new `verification/W3-sweep.R` that defines the 60-cell grid, iterates over cells, calls W3 logic for each.

Option (b) is cleaner. Sketch:

```r
# verification/W3-sweep.R
source("verification/00-setup.R")
# Define 60 cells (see todo/005 §0.6).
cells <- expand.grid(
  pattern = c("non_monotone", "monotone"),
  mech    = c("MAR", "MNAR"),
  N       = c(200, 500, 1000),
  # engine + M + cong combos:
  engine_M_cong = list(
    list(engine = "fiml",   M = NA,  empri = 0),
    list(engine = "amelia", M = 20,  empri = 0),
    list(engine = "amelia", M = 200, empri = 0),
    list(engine = "amelia", M = 20,  empri = 0.5),  # 0.5 * N
    list(engine = "amelia", M = 200, empri = 0.5)
  )
)
# For each cell, run R=2000 replicates of W3, save to verification/cache/W3-sweep/<cell-id>.rds
```

**R = 2000 replicates per cell** (per todo/005 §0.6).

**Note on `empri = 0.5`:** this is a fraction-of-N convention. Inside the per-cell driver, multiply by N to get actual empri value (`empri_actual = cell$empri * cell$N`).

---

## Step 6 — Single-cell smoke run

Before the full sweep:
- Run W3-sweep on **one cell** (e.g., N=200, MAR, non-monotone, FIML, R=200) to confirm the pipeline works end-to-end.
- Verify the output cache file is well-formed and the selection-rate summary is plausible (should roughly match the preregistered prod numbers).

## Step 6b — Pre-flight tr(RIV) table

Compute analytic tr(RIV) for each candidate model {M_A, M_B, M_C, M_D} under each pattern × mech × N combination (`tr_riv_analytic_general` from `00-setup.R`, restricted to each model's free-parameter set). Build a table:

| pattern | mech | N | tr_M_A | tr_M_B | tr_M_C | tr_M_D | ordering |
|---|---|---|---|---|---|---|---|

Save as `verification/cache/W3-sweep-rivs-preflight.csv`. Verify:
- Non-monotone matches preregistered prod (M_A < M_C < M_B < M_D, approximately).
- Monotone may show different ordering — document it explicitly. This sets the expectation for H1's prediction (monotone gives more heterogeneous candidate-level RIV, larger W3-A) or its counter-prediction (orderings change in a way that breaks H1).

This 10-min calculation is the empirical anchor for H1's prediction. If the orderings don't look favorable for H1, flag it BEFORE running the full sweep — may need to revise the prediction or the candidate models.

## Step 6c — Full-grid R=100 sanity sweep

Before committing to R=2000 across all 60 cells, run the full sweep at R=100 first:
- All 60 cells at R=100 each.
- Compute: FIML (12 × 5s = 1 min) + Amelia M=20 (24 × 5s = 2 min) + Amelia M=200 (24 × 10s = 4 min) = **~7 min total**.
- Check per cell:
  - No errors (all cells completed).
  - Selection rates roughly plausible (oracle ~0.7–0.9 at MAR + congenial cells; magnitudes reasonable).
  - W3-C is high (~0.9+) at MAR + congenial cells, low or near-zero issues elsewhere flagged.
- If anything looks off (mechanism wired wrong, uncongeniality producing weird imputations, monotone pattern not amputing as expected): debug before the production R=2000 run.
- Cache: `verification/cache/W3-sanity/<cell-id>.rds`. Discard after R=2000 sweep, or keep for comparison.

This is the most important step. R=100 is too noisy for hypothesis testing but catches all the wiring bugs at low cost.

---

## Step 7 — Run W1 sweep (cheap, do first)

In parallel with W3 (or first since it's faster):
- Adapt `verification/W1-bias-decomposition.R` or write a similar `verification/W1-sweep.R`.
- 60 cells × R=2000.
- FIML engine only is fine (W1 result is engine-independent for total bias; engine differences only matter for W2/W3).
- Expected total: ~15 min.

---

## Step 8 — Run W3 sweep (main attraction)

Per-cell costs (with optimized custom-Cholesky pipeline + p=4 + R=2000 + 20 cores):
- FIML × 12 cells × 100s = ~20 min
- Amelia M=20 × 24 cells × 100s = ~40 min
- Amelia M=200 × 24 cells × 200s = ~80 min

**Total: ~140 min ≈ 2.3 hours.** Run in one session.

Recommended order:
- FIML first (cheap, gets the picture).
- Amelia M=20 next.
- Amelia M=200 last.

Within each engine bucket, iterate over cells in (cong, N, mech, pattern) order so partial results are interpretable if interrupted.

---

## Step 9 — Run W3 H3b rate side experiment (small, cheap)

Per todo/005 §H3b: 6-cell experiment to test the rate-N relationship.
- Cells: 3 (N ∈ {200, 500, 1000}) × 2 (rate ∈ {20%, 60%}) at fixed (MAR, non-monotone, M=200, congenial Amelia).
- R = 2000 per cell.
- Cost: ~6 cells × 200s = 20 min.
- Cache: `verification/cache/W3-sweep-rate/<cell-id>.rds`.

Test H3b: W3-A scales linearly with rate, N-invariant within each rate.

## Step 10 — Run W2 spot checks (limited)

W2 is *not* part of the comprehensive sweep (todo/005 §3). But add two spot-check cells for transparency in §4 of the manuscript:
- **MNAR cell**: W2 at (N=200, MNAR, non-monotone, M=200, congenial). Compares to preregistered cell.
- **Uncongenial cell**: W2 at (N=200, MAR, non-monotone, M=200, uncongenial empri=0.5*N). Same comparison.

Each cell: same 8-δ grid, R=1000 (lower than W3's 2000, since W2 is exploratory). Cost: ~85 min each. Total ~3 hours.

---

## Step 11 — Aggregate results

Write `verification/W3-sweep-summary.R` that:
- Loads all 60 main-sweep W3 cache files PLUS the 6 H3b rate-experiment files.
- Builds one tidy data frame: (pattern, mech, N, rate, M, cong, engine, oracle_rate, uncorr_rate, corrected_rate, SB_rate, W3A_gap, W3B_gap, W3C_concordance).
- Outputs a CSV `verification/cache/W3-sweep-summary.csv`.
- Prints a per-factor margins table (mean W3-A across cells holding one factor fixed at each level).
- Saves marginal effect plots if helpful for the manuscript.

Repeat for W1 sweep.

---

## Step 12 — Evaluate hypotheses

For each H1–H6 and H3b in todo/005 §1:
- Compute the empirical test.
- Compare to pass criterion.
- Mark PASS / FAIL / OBSERVATIONAL.

Write a brief summary (markdown or comment block in W3-sweep-summary.R) reporting outcomes.

---

## Step 13 — Update todo/005 version history

Add a "Sweep complete" entry with the date, summary of which hypotheses passed/failed/were observational, and pointer to the summary CSV.

---

## Step 14 — Update IDEAS.md

Add a new "Comprehensive sweep results (2026-MM-DD)" section after the existing empirical-update section. Summarize the sweep findings in 2-3 paragraphs:
- What was tested (60 main cells + 6 H3b rate cells + 2 W2 spot checks, 6 factors total).
- Which hypotheses passed.
- Where the framework's safety margin is (uncongeniality breakdown, MNAR behavior).
- Implications for §3/§4/§5 of the manuscript.

---

## Step 15 — Commit and push

One commit covering the sweep:
- New files: `verification/W1-sweep.R`, `verification/W3-sweep.R`, `verification/W3-sweep-summary.R`, `verification/00-test-ampute-vs-apply-mar.R`, `verification/cache/W1-sweep-*.rds`, `verification/cache/W3-sweep-*.rds`, `verification/cache/W3-sweep-rate/*.rds`, `verification/cache/W3-sweep-summary.csv`.
- Modified: `verification/00-setup.R` (added `apply_missingness_ampute`, modified `impute_mvn_amelia` to accept `empri`).
- Modified: `todo/005-comprehensive-sweep-hypotheses.md` (version history updated).
- Modified: `IDEAS.md` (new sweep-results section).

Commit message should summarize: design (60 main cells + 6 H3b rate cells × R=2000), engine totals, hypothesis outcomes (e.g., "H1/H2-MAR/H3/H3b/H4/H6 pass; H5 informative; H2-MNAR observational"), key surprises if any.

Push to `origin/main`.

---

## Step 16 — Hand back to user

Brief recap message:
- Sweep is done, X of Y cells ran successfully.
- Quantitative criteria: X passed, Y failed, Z observational.
- Headline findings.
- Recommend next step (manuscript drafting, sensitivity to other factors, real-data demonstration, etc.).

---

## Compute budget summary

| Stage | Time |
|---|---|
| Implementation (steps 2-5) | 1-2 hours |
| Single-cell smoke run (step 6) | 5 min |
| Pre-flight tr(RIV) table (step 6b) | 10 min |
| R=100 sanity sweep (step 6c) | ~7 min |
| W1 sweep (step 7) | 15 min |
| W3 sweep (step 8) | ~2.3 hours (with 2-3x warm-start speedup, more like ~1 hour) |
| H3b rate experiment (step 9) | ~10 min (with warm-start speedup) |
| W2 spot-checks (step 10) | ~3 hours |
| Aggregate + evaluate (steps 11-12) | 30 min |
| Update docs + commit (steps 13-15) | 30 min |
| **Total** | **~6-8 hours** (warm starts shave ~1.5h off Chan SMI, depending on actual convergence improvements) |

Realistic for one day's work in a fresh session. If anything overruns, the W3 sweep is the highest-priority and W2 spot-checks can be deferred.

---

## Quick-reference cheat sheet

- **R per cell**: 2000.
- **p**: 4.
- **N grid**: {200, 500, 1000}.
- **M grid** (Amelia only): {20, 200}.
- **Mech**: {MAR, MNAR} via `mice::ampute`.
- **Pattern**: {non_monotone, monotone}.
- **Congeniality**: Amelia `empri = 0` (cong) or `empri = 0.5 * N` (uncong); FIML always cong.
- **Missingness rate**: 40% marginal target.
- **Seed**: `set.seed(20260522 + r)` per worker.
- **Parallelism**: 20-core PSOCK cluster via `pbapply::pblapply(..., cl = cl)`.

---

## Open questions to flag to user before sweep (if needed)

If during implementation any design decision is ambiguous, ask the user BEFORE running the sweep. Don't silently make framework-affecting choices. Specific risk points:
- How to tune `mice::ampute` `weights` to get an MAR mechanism comparable to our existing apply_mar (matching marginal rates).
- How to set MNAR strength (β coefficient in the missingness model).
- Whether monotone freq should produce 40% on the deepest variable or 40% marginal across all variables.
- Whether `empri = 0.5 * N` is the right uncongenial strength (vs `empri = 0.1*N` or `empri = N`).
