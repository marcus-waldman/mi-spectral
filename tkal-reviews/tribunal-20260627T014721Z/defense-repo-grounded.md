# Repo-grounded defense — S5 simulation claims

Authored by the defender **with repository access** (the harness defender had none, which is why it conceded all 21 challenges by default). Each consolidated issue is answered with the actual artifact, date, or recomputation. Disposition is one of **REBUT** (challenge does not stand), **CONCEDE-AMEND** (stands; minimal rewrite), or **PARTIAL** (rebut the sting, amend the wording).

All numbers below are recomputed in-session from committed artifacts.

---

## Issue 1 — W1 goalpost (2.77 → augmented 2.42–2.55). Examiners: unanimous **blocking**.

**Challenge.** "Confirms the completed theorem" rests on a band introduced during analysis; the estimate 2.43 misses the registered 2.77; the augmentation may be estimate-chasing.

**Evidence (recomputed from `W1-prod-fiml*.rds`, four N cells):**

| cell | T̂ | se | z vs 2.774 |
|---|---|---|---|
| N=200 | 3.087 | 0.339 | +0.92 |
| N=500 | 1.762 | 0.530 | −1.91 |
| N=1000 | 0.865 | 0.731 | −2.61 (the one disclosed miss) |
| N=2000 | 2.038 | 1.065 | −0.69 |
| **inverse-variance pool** | **2.434** | **0.258** | **−1.32** |

- The pooled 95% CI is **[1.93, 2.94]**, which **contains the pre-registered target 2.774**. The pooled preregistered data do **not reject** 2.77 (z = −1.32, p ≈ 0.19). The premise "2.43 misses 2.77" is a 1.3-se point gap, not a rejection.
- The O(1) MAR term (A)+(C) is **independently derived from the missingness mechanism** (Cox-Snell, commit `08ee37b`, 2026-06-01; monotone closed form `914bbf0` same day), **two-CAS + Monte-Carlo verified**, with value **≈ −0.22 set by theory, not fit to 2.43**. Then 2.774 + (−0.22) ≈ 2.55, with the band lower edge 2.42 at (A)+(C) ≈ −0.35 — inside the analytically-anchored range.
- The whole episode is logged in a **dated amendment** (`todo/004`, Amendment 2, 2026-06-04): it records that (A)+(C) "did not exist in the theory at freeze time (SHA ddc9037)," reports the per-cell N=1000 FAIL, and gives pooled 2.434 ± 0.258 vs 2.774 (−1.3 se) vs augmented (within 0.0–0.5 se).

**Disposition: PARTIAL.** The estimate-chasing reading is **rebutted** — the target is not rejected, the term is independently derived and dated, the miss is disclosed. The legitimate residue is **wording**: "confirms the completed theorem" reads as if 2.42–2.55 were the pre-registered target.

**Action (minimal).** S5-P12: replace "confirms the completed theorem at 2.43 ± 0.26 against the order-one-augmented prediction" with "the pooled estimate 2.43 ± 0.26 is consistent with the leading-order target 2.77 (z = −1.3) and centers on the O(1)-augmented prediction 2.42–2.55." Cite the dated derivation and Amendment 2. Keep the N=1000 miss. **Not** a collapse to "post-hoc consistency check"; the augmentation is a verified, dated, independent correction.

---

## Issue 2 — Block-diagonal equality (projected ≡ naive to 3.6e-15). Examiners: unanimous **blocking**.

**Challenge.** Study 7 claims projected-trace superiority where the two trace formulas provably coincide; the 0.824 vs 0.904 gap is a moment-map (naive-input) effect, not a trace-formula effect — structural luck sold as general.

**Evidence.**
- The manuscript **already discloses the equality** as a *structural limit*: S5-P20 tables "block-diagonal family, naive vs projected trace … agree to 3.6×10⁻¹⁵." It does not hide it or claim the ladder distinguishes the formulas there.
- "Overstates the projected trace elsewhere" is a **proved** result (Gram/Schur, `@prp-naive` / the `@sec-lrt` projected-trace theorem — firm tier), not an empirical extrapolation, and is **measured at the bias level in Study 8** (~9% off-equality, `w4-dissimilar-summary.csv`: trnaive 8.74 vs trperp 7.95 on the AR candidate).

**Disposition: PARTIAL.** Rebut the "structural luck sold as general" framing — the equality is disclosed and the general inequality is proved + measured in Study 8, not inferred from the ladder. Concede the prose **conflates** the moment-map (naive-input) gap with trace-formula superiority.

**Action (minimal).** S5-P20: state explicitly that in the block-diagonal ladder family the two trace formulas coincide (3.6e-15), so the 0.824 vs 0.904 gap is a **naive-input moment-map** effect; attribute trace-formula superiority to the proof (`@prp-naive`) and its measured instance in Study 8. This separates two claims the current prose runs together; it does not retract a result.

---

## Issue 3 — W3C = 1.000 "100% land on saturated." Examiners: 2 blocking / 1 major.

**Challenge.** Nested set ordered by RIV with saturated at the top → any monotone downward bias forces all errors onto saturated → near-tautology, not mechanism confirmation. Holds even uncongenially where the correction overshoots.

**Evidence.**
- W3-C was a **pre-registered directional prediction** (`todo/005` H2, line 96), and the prereg **expected it to drop** under uncongeniality (H5, line 152) and MNAR (H2, line 96). It instead held at **1.000 across all 60 cells + rate + engine + congeniality variants** (sweep verdict, line 208). A prediction the registrants thought would break, that held, is a measured robustness result — not a tautology presented as discovery.
- That said, the examiners are correct that in a nested RIV-ordered set the saturated endpoint is the generic overfit sink, so the 1.000 confirms the **direction** of the bias, it does not **discriminate** the specific spectral decomposition from a generic monotone bias.

**Disposition: PARTIAL.** Concede the rescope from "mechanism confirmation" to "directional confirmation"; rebut the "artifact/hidden" sting (it was a registered prediction tested across the sweep).

**Action.** S5-P17: state the 1.000 as "consistent with the predicted bias direction; the nested RIV ordering makes the saturated model the natural overfit sink, so this confirms direction rather than discriminating the decomposition," and note it was a registered prediction that held across all sweep variants. Move discriminating weight to the recovery magnitude and Study 8.

---

## Issue 4 — Uncongenial / MNAR omission = hidden D-05 failure. Examiners: 1 blocking / 2 major.

**Challenge.** The uncongenial overshoot (uncorrected > oracle; corrected overshoots, oracle−corr negative) and MNAR cells are not in the headline; if any was registered to pass, omitting it is a hidden failure.

**Evidence (`todo/005`).**
- **H5 (congeniality), line 158:** "congenial cells pass … **Uncongenial cells are observational — we expect W3-A to drop … and W3-C to drop**." Line 160: "transparent stress-test evidence of where the framework's safety margin ends. The paper's §6 (Discussion) acknowledges this."
- **H2-MNAR, line 100:** "*transparent observational report only* — **no required pass**."

So uncongenial and MNAR were **registered as observational, never pass-targets**. Omitting them from the *headline* is not a D-05 violation — D-05 governs unmet *pass-criterion* predictions.

**Disposition: REBUT (strong) + small AMEND.** Not a hidden failure. But the prereg **committed §6 to acknowledge** the uncongenial limit, so that disclosure must actually be present and should name the overshoot.

**Action.** Ensure §6 carries the committed uncongenial disclosure (it is a pre-registered reporting commitment, not a patch), naming the overshoot behavior; optionally add a one-line pointer from S5-P17. No headline change required.

---

## Issue 5 — 52-σ engineered separation. Examiners: unanimous **major**.

**Challenge.** The 52-σ rejection is achieved by a 70–79% / ~0% missingness extreme; "rules it out outright" reads as general superiority.

**Evidence.** The design paragraph S5-P7 already states the cell is built to separate the formulas ("which agree under equal missing information and diverge when it is uneven … the first coordinate made heavily missing"). Correctness rests on the **2.64/2.70 match** to the projected prediction 2.64, not the σ count.

**Disposition: CONCEDE-AMEND (cosmetic).** Not hidden, but the prose should localize the 52-σ to the engineered cell.

**Action.** S5-P15: frame the 52-σ as "maximal-separation exclusion of the naive formula in an engineered cell," rest correctness on the 2.64 match. Report a balanced-missingness number if available (else state it is not measured).

---

## Issue 6 — "Statistically indistinguishable" overshoot + weak-cell attribution. Examiners: flagged ×3.

**Challenge.** Two-moment/equating (0.904/0.903) exceed oracle (0.899) one-sided at SE ≈ 0.010; "information loss rather than calibration error" is asserted, not decomposed.

**Disposition: CONCEDE-AMEND.** Both fair.

**Action.** State indistinguishability as a two-sided interval |arm − oracle| < k·SE with k and SE given; flag the small overshoot if it exceeds it. Relabel the weak-cell attribution as an interpretation/conjecture unless a weak-cell error decomposition is added.

---

## Issue 7 — Reproducibility of RDS-backed headlines. Examiners: 1 blocking / 1 major / 1 minor.

**Challenge.** Studies 1–5 numbers (2.43, 0.025/−0.536, 0.042/0.034, 2.64/2.70) are backed by `.rds` not transcribed; Study 9's "2–3% / 0.011" cites only a directory; "cannot be checked even in principle."

**Evidence.** I just recomputed 2.434 ± 0.258 directly from the four committed `W1-prod-fiml*.rds` files (table in Issue 1). The numbers **are** reproducible from committed artifacts via `verification/run_all.R` and `verification/w1-h1-pooled-reconciliation.R`; the manuscript cites them. The "cannot be checked even in principle" claim is an artifact of the **tribunal proposal** not transcribing the RDS rows, not a manuscript defect. **Exception:** Study 9 (S5-P22) points at the `run_all-prod` directory, not a specific row — that loose pointer is a genuine gap.

**Disposition: REBUT (mostly) + one real AMEND.** Reproducible-in-principle is satisfied. The Study 9 pointer is the one legitimate fix.

**Action.** Tighten S5-P22 to cite the exact engine-sensitivity rows/columns (or remove the "2–3% / 0.011" figures pending that); resolve the ncratio label mapping in S5-P19. No other headline change.

---

## Bottom line

Decomposed against the repository, the two unanimous "blockers" are **wording/scoping amendments**, not structural failures, and the "hidden failure" charge is **rebutted by the pre-registration** (uncongenial/MNAR were registered observational). The real, warranted edits are small and local:

1. S5-P12 — soften "confirms" → "consistent with," cite the dated independent (A)+(C) derivation + Amendment 2. *(rebut estimate-chasing)*
2. S5-P20 — separate the naive-input moment-map gap from trace-formula superiority; point the latter to the proof + Study 8. *(rebut structural-luck framing)*
3. S5-P17 — "direction not mechanism" rescope; note the registered prediction held across the sweep.
4. §6 — make sure the pre-registered uncongenial/overshoot disclosure is actually present.
5. S5-P15 — localize the 52-σ to the engineered cell; correctness rests on the 2.64 match.
6. S5-P18/19 — two-sided interval for "indistinguishable"; conjecture-label the weak-cell attribution.
7. S5-P22 — tighten the Study 9 pointer (the one genuine reproducibility gap).

None of these retracts a result or changes a headline number. The harness verdict ("amend everything, risk of collapse") was an artifact of a defender with no access to the artifacts.
