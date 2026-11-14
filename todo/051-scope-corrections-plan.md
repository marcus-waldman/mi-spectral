# todo/051 — Scope corrections after the 2026-11-13 adversarial review

**Status: DRAFT, nothing applied.** Every change below is Marcus's call. Locked level3 prose
changes only through a `manuscript/plan/updates/` script; the scope change itself needs a
dated amendment in `decisions.md` (proposed D-27).

**Provenance.**
- The theoretical-statistician-agent session sent `manuscript/derivation.qmd` lines 195–1315
  (@ `cfc6b0b`) to Gemini 4 Argon high (headless agy) on 2026-11-13.
- The review is in `~/git-repositories/theoretical-statistician-agent/lit/kg/verification/half-trace-riv-bias/`
  (`xfamily/result.json`; the MC check is `adjudication/cx1-results.md`). Its open items are in
  `lit/kg/review/disputes.md`.
- Each item was then checked by hand in the MI-SPECTRAL session the same day (findings below).

## 0. Gate question (answer first)

**Answered 2026-11-13 (Marcus): not yet submitted.** These are pre-submission edits; the
deliverable is an amended `mi-spectral-apa.pdf`, and no revision note is needed.

**Has the JAIGP submission happened?** If not, these are pre-submission edits. If it has, the
same edits become a revision, and the response must say what changed and why. Which one
applies changes the deliverable (an amended PDF, or a revision with a change note), but not
the edit list.

## 1. Findings

| ID | Finding | Verdict | Evidence | Numbers affected? |
|---|---|---|---|---|
| F1 | ½tr(RIV) fails for a structured (shared-scale) covariance under MCAR. With N₂(μ, σ²I), Y2 always observed, Y1 MCAR-missing on π, and FIML: E[T] = 3π/(2(2−π)), against ½tr(RIV) = ½[π/(1−π) + π/(2−π)]. The gap is −π²/[2(1−π)(2−π)], which is O(1). | Confirmed | Hand derivation via E log χ²; Gemini MC: 0.518/0.510/0.489 against the 0.500 prediction (0.667 per the theorem) at π = .5. The saturated bivariate control reproduces ½tr(RIV). | No. Every simulation imputes under the saturated model. |
| F2 | D-22 (second-moment-matched imputers only) went into `derivation.qmd` alone. The theorem's hypotheses still include R5 (Rubin-proper posterior draws). The manuscript states the result for posterior draws: abstract; S4-P4 defines φ̃ as a posterior draw; S5-P22 recommends "a fully Bayesian sampler". | Confirmed | `decisions.md:136`; `mi-spectral-apa.qmd` has no restriction text. Gemini's CX2 (univariate, prior ∝ 1/σ²) agrees with the paper's own D: D = −tr(RIV), so E[T] = −½tr(RIV). | No. FIML and Amelia EMB are second-moment-matched. |
| F3 | `derivation.qmd:740` defines (A)+(C) with −tr(RIV); `:746` and `:1022` do not, and `:1024-1025` says no −tr(RIV) enters. | Confirmed (typo) | Text | No |
| F4 | The displayed H_φ (`derivation.qmd:1041`) has +½∂²tr(S₀⁻¹S); the correct sign is −½. | Confirmed (display only) | `verification/term-a-mar-closedform.R:112` uses the correct sign and is checked against finite differences | No |
| F5 | Term B orders: the B2 remainder is O_p(n^-1/2), not O_p(n^-3/2); the B3 error in expectation is O(n^-1), not O(n^-3/2). The step from O_p to expectations needs a moment condition. | Confirmed (statement) | The cubic term's expectation is O(n^-1), so E[B] = −½tr(RIV) + O(n^-1) stands. For the MVN, Wishart moments exist at moderate n. | No |
| F6 | Under MAR, Term A omits Cov(α(R), δ) = O(1). | Not supported for monotone MAR; **open for non-monotone** | MC, bivariate monotone, strong selection, 40k reps: Cov = −0.0004 ± 0.0023 (n=200) and +0.0007 ± 0.0023 (n=800), against E[α]ᵀE[δ] ≈ 0.25. α lies along the missing block's conditional covariance, whose estimate is independent of R given the predictors. | Possibly the −0.22 analytic approximation (non-monotone only) |
| F7 | The b_Σ recursion uses the unconditional Σ_PP where it should use the selected covariance. | Rejected | Σ_PP enters through the FIML Σ̂_PP (consistent for the population value); the selected Σ⁽ʲ⁾_PP enters through Var(β̂_j), as written. | — |
| F8 | The IC section attributes each candidate's ½tr(RIV_k) level to the theorem. W3 scores all candidates on saturated-model imputations (`verification/_modules/w3-sweep.R:82`), so the per-candidate level comes from Proposition L1. It equals ½tr(RIV_k) only in L2's equality case, which the W3 family satisfies. | Confirmed (justification, not result) | `derivation.qmd:1800`, level3 S4-P16 | No |

Also already conceded in the text: the −0.22 approximation uses expected information and is
not reproduced by finite differences (Gemini's item 3d).

## 2. Decisions for Marcus (D-27)

**Ratified 2026-11-13 (Marcus, recorded as D-27 in `decisions.md`):** 1 Option A (narrow);
2 full carry-over; abstract names the engines (drops "proper"); 4 run the non-monotone
check first. Item 3 (F8) is still open.

1. **Theorem scope (F1).**
   - **Option A (recommended):** state the theorem for the multivariate normal with an
     *unrestricted* covariance, which is what D1 and the proof cover, plus the canonical GLMs
     of Lemma P. Add F1 as a second displayed scope case next to the known-scale collapse.
   - **Option B:** first derive the general MCAR residual for structured covariances. This is
     new work (a candidate condition is that the parameters of each pattern's conditional
     distribution are variation-independent of those of the always-observed variables);
     better as future work in the Discussion.
2. **Imputer scope in the manuscript (F2).** Carry D-22 into the manuscript. Recommended:
   - name the imputers covered (deterministic FIML and bootstrap-EM) wherever the result is
     stated;
   - give the posterior-draw correction D once in S4, with the Jeffreys example;
   - rewrite the S5-P22 advice. A fully Bayesian sampler is not the conservative choice for
     this bias.

   Open sub-question: keep "proper" in the abstract, glossed as "second-moment-matched", or
   drop it.
3. **IC justification (F8).** Re-derive the per-candidate level from L1, and present
   ½tr(RIV_k) as exact in L2's equality case (which the W3 family satisfies) and as an
   overstatement otherwise. The W3 numbers and the corrected criterion's formula stay.
4. **F6.** Either run the non-monotone check (§4, item 2) before the edits land, or add a
   one-sentence limitation that the −0.22 approximation omits the selection covariance for
   non-monotone patterns, pending that check.

## 3. Edit list

### `manuscript/derivation.qmd` (not locked; edit directly, then render)
- `:59-62` (intro result): restrict the scope to the unrestricted-covariance MVN (and
  Lemma P). Name the second-moment-matched imputer.
- `:724-736` (theorem): hypotheses R1–R4, R6, R7, plus a second-moment-matched imputer in
  place of R5. Point to the D-22 callout for posterior draws. Narrow "any regular likelihood
  with an estimated scale or covariance".
- `:740`: delete "−tr(RIV)" (F3).
- `:799-838` (scope section): add F1 as a closed-form scope case. Include the saturated control.
- `:975-980` (lemma order counting): state Var(δ) = I_obs⁻¹ for a draw-free imputer, and say
  that a posterior draw doubles it (the origin of D).
- `:1041`: change +½ to −½ (F4).
- `:878-885` (B2/B3): correct the orders (F5). Add a moment condition to R1/L1 (uniform
  integrability of n‖θ̂ − θ₀‖² and existence of E[Σ̂⁻¹]; the latter holds for the MVN at
  moderate n).
- `:1798-1806` (IC criterion): re-justify via L1 and L2 (F8).

### `manuscript/plan/level3-paragraphs.json` (locked; one update script)
Proposed script: `manuscript/plan/updates/update-scope-corrections-<date>.py`. Paragraphs:
- `abstract`: unrestricted covariance; imputer wording (F1, F2).
- `S1-P4` and `S1-P6`: the result as stated in the introduction. S1-P6 claims the extension
  to proper MI as a contribution; reword it to the second-moment-matched imputer with the
  disclosed posterior-draw correction.
- `S1-P6b`: contribution 2 scope.
- `S2-P7`: the background on proper vs improper imputation ends by claiming the extension to
  proper MI; align it with D-22.
- `S4-P2` and `S4-P6`: theorem statement and hypotheses (F1, F2).
- `S4-P4`: φ̃ definition. Name the covered imputers; posterior draws carry D.
- `S4-P7b`: order counting (F2), and note F6 if decision 4 says so.
- New short paragraph or display after `S4-P8` (known-scale collapse): the F1 scope case.
- `S4-P16`: IC justification via L1 and L2 (F8). `S6-P4c` (BIC) inherits the same sentence.
- `S5-P22`: replace the "fully Bayesian sampler … conservative" advice.
- `S6-P1`: mechanism scope. `S6-P2` (G2, proper-MI carry-over): check it against D-22.
  `S6-P4` (G6): restate the instantiation limit with F1.

### Other files
- `manuscript/plan/level1-thesis.json:11` and the level4 proposition for the theorem: scope
  wording.
- `manuscript/plan/decisions.md`: D-27 (scope narrowed to unrestricted covariance; D-22
  carried into the manuscript; F3–F5 corrections; rejected options).
- `CLAUDE.md` "Core contribution": the same scope wording.
- `.prometheus/charter.md` (Decisions made, Next actions) at the next wrap. The wiki follows
  from the post-wrap hook.

## 4. New verification

1. `verification/spikes/cx1-shared-scale.R`: MC of F1 at π ∈ {.2, .5, .7} and n ∈ {100, 400,
   1600}, with the saturated control. Pair it with a CAS check of the closed form
   (`verification/cas-wolfram/verify_cx1_shared_scale.py`). Write the predictions down
   before the run, as in `todo/004`.
2. Non-monotone check of F6: extend the monotone MC
   (`/tmp/claude-1000/-home-marcu--claude-spares-spare-0n6PG7/08fe1d1c-b7f8-4a39-80b4-51a0e951c3e5/scratchpad/cov_alpha_delta.py`,
   to be copied into `verification/spikes/` if adopted) to the four-variate phase-8 ampute
   design.
3. After the edits:
   - `py scripts/check_plan.py` green
   - `py scripts/corpus_vocab_check.py` and `py scripts/color_commentary_flag.py`
   - `py scripts/build_manuscript_apa.py`
   - render `mi-spectral-apa.qmd` and `derivation.qmd` with the pinned Quarto 1.7.32
   - `/derivation-audit` at 0/0

## 5. Order of operations

1. Answer §0; ratify the D-27 options (§2).
2. Run §4 items 1–2 (both are exploratory; neither changes a reported number).
3. Edit `derivation.qmd`; render; `/derivation-audit`.
4. Draft the level3 changes unit by unit (the `/section-review` Phase 3 loop), then apply them
   with one update script.
5. Rebuild and render the manuscript; update `decisions.md`, `status.json`, `CLAUDE.md`;
   commit together.

## 6. Unchanged

- Every reported number (W1–W4, ladder, known-scale, Lemma P).
- The preregistered originals at SHA `ddc9037`.
- The corrected criterion's formula.
- The likelihood-ratio propositions L1–L4, which rest on the saturated full model.
