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

## Step 6 — Smoke run

Before the full sweep:
- Run W3-sweep on **one cell** (e.g., N=200, MAR, non-monotone, FIML, R=200) to confirm the pipeline works end-to-end.
- Verify the output cache file is well-formed and the selection-rate summary is plausible (should roughly match the preregistered prod numbers).

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

## Step 9 — Run W2 spot checks (limited)

W2 is *not* part of the comprehensive sweep (todo/005 §3). But add two spot-check cells for transparency in §4 of the manuscript:
- **MNAR cell**: W2 at (N=200, MNAR, non-monotone, M=200, congenial). Compares to preregistered cell.
- **Uncongenial cell**: W2 at (N=200, MAR, non-monotone, M=200, uncongenial empri=0.5*N). Same comparison.

Each cell: same 8-δ grid, R=1000 (lower than W3's 2000, since W2 is exploratory). Cost: ~85 min each. Total ~3 hours.

---

## Step 10 — Aggregate results

Write `verification/W3-sweep-summary.R` that:
- Loads all 60 W3-sweep cache files.
- Builds one tidy data frame: (pattern, mech, N, M, cong, engine, oracle_rate, uncorr_rate, corrected_rate, SB_rate, W3A_gap, W3B_gap, W3C_concordance).
- Outputs a CSV `verification/cache/W3-sweep-summary.csv`.
- Prints a per-factor margins table (mean W3-A across cells holding one factor fixed at each level).
- Saves marginal effect plots if helpful for the manuscript.

Repeat for W1 sweep.

---

## Step 11 — Evaluate hypotheses

For each H1–H6 in todo/005 §1:
- Compute the empirical test.
- Compare to pass criterion.
- Mark PASS / FAIL / OBSERVATIONAL.

Write a brief summary (markdown or comment block in W3-sweep-summary.R) reporting outcomes.

---

## Step 12 — Update todo/005 version history

Add a "Sweep complete" entry with the date, summary of which hypotheses passed/failed/were observational, and pointer to the summary CSV.

---

## Step 13 — Update IDEAS.md

Add a new "Comprehensive sweep results (2026-MM-DD)" section after the existing empirical-update section. Summarize the sweep findings in 2-3 paragraphs:
- What was tested (60 cells, 5 factors).
- Which hypotheses passed.
- Where the framework's safety margin is (uncongeniality breakdown, MNAR behavior).
- Implications for §3/§4/§5 of the manuscript.

---

## Step 14 — Commit and push

One commit covering the sweep:
- New files: `verification/W1-sweep.R`, `verification/W3-sweep.R`, `verification/W3-sweep-summary.R`, `verification/00-test-ampute-vs-apply-mar.R`, `verification/cache/W1-sweep-*.rds`, `verification/cache/W3-sweep-*.rds`, `verification/cache/W3-sweep-summary.csv`.
- Modified: `verification/00-setup.R` (added `apply_missingness_ampute`, modified `impute_mvn_amelia` to accept `empri`).
- Modified: `todo/005-comprehensive-sweep-hypotheses.md` (version history updated).
- Modified: `IDEAS.md` (new sweep-results section).

Commit message should summarize: design (60 cells × R=2000), engine totals, hypothesis outcomes (e.g., "H1/H2-MAR/H3/H4/H6 pass; H5 informative; H2-MNAR observational"), key surprises if any.

Push to `origin/main`.

---

## Step 15 — Hand back to user

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
| Smoke run (step 6) | 5 min |
| W1 sweep (step 7) | 15 min |
| W3 sweep (step 8) | ~2.3 hours |
| W2 spot-checks (step 9) | ~3 hours |
| Aggregate + evaluate (steps 10-11) | 30 min |
| Update docs + commit (steps 12-14) | 30 min |
| **Total** | **~8 hours** |

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
