# Level-2 annotation extract — cycle 1 (2026-06-06)

Source: `manuscript/plan/level2-sections.json` (drafted at commit 14bf9c5 under the
ratified 6-move Level 1). Six units, one per section blueprint: the goal statement,
then the super-propositions (SPs). Annotate anywhere under a unit with
`#[COMMENTS: ...]`; you can target a single SP (e.g. `#[COMMENTS: S4-SP5 ...]`).
Mark whole-unit approvals with `#[OK]`. Unmarked units are approved-by-silence only
after you confirm that reading at hand-back. Evidence pointers are abbreviated here;
the JSON carries the full lists.

---

## U1 — S1 INTRODUCTION (sec-intro, M1) — est. 4-5 paragraphs

**Goal:** Convince an applied MI-literate reader that (i) MI's major inferential
results are settled but LRT/IC are not — on the field's own testimony; (ii) the
yardstick is the complete-data replication principle, three levels; (iii) this paper
resolves criterion replication everywhere and characterizes the decision-rate
boundary exactly; (iv) only then, the AI meta layer — one closing paragraph.
Defers notation (S2), proofs (S4), apparatus (S5). Gates: T-06 typing,
todo/003 scoping caution (novelty = the PRINCIPLE, not full-data benchmarking).

- **SP1** MI mature, settled results — on the field's own testimony (SG2002, Enders 2025, Rubin 1987).
- **SP2** LRT/IC documented-open: C-C 2010 flags MI-AIC theory beyond scope; Schomaker–Heumann "sparse" + averaged criteria "not supported"; no IC-after-MI in three state-of-the-art accounts.
- **SP3** The replication principle, three levels, asserted-here — scoped: empirical full-data benchmarking precedented (Wood 2008, C-C 2010), the named principle + achievability characterization is not.
- **SP4** Headline: +½tr(RIV) + (A)+(C); correction restores criterion replication everywhere; decision-rate replication complete at null, information-bounded under signal.
- **SP5** Upstream of Chan (complementary); penalty = Shimodaira's AIC_{x;y}, prior uses target prediction not replication.
- **SP6** Meta layer: one closing paragraph pointing to Methods.

#[ ]

## U2 — S2 BACKGROUND AND NOTATION (sec-background, M2) — est. 12-15 paragraphs

**Goal:** Notation + precision restatement in the source's own terms, three-tier
gradient (calculus-based entry → graduate → specialist); each restatement names the
dependent proposition (D-04); pre-empts the two standard conflations; no symbol
introduced twice.

- **SP1** (T1) Y = {Y_obs, Y_mis}, R; two likelihoods, two MLE targets θ̂_com / θ̂_obs.
- **SP2** (T1) Ignorability; when R drops out (Rubin 1976).
- **SP3** (T1) Missing-information principle via Hessians; RIV defined here.
- **SP4** (T2) EM/Q-function; MCEM bridge — MI's averaged log-likelihood as Monte Carlo Q.
- **SP5** (T2) Rubin's rules as exact posterior-moment identities; congeniality.
- **SP6** (T3) AIC as bias-corrected plug-in; Wilks.
- **SP7** (T3) Observed vs expected information under MAR (K–M convention, T-02); EM rate matrix ≠ RIV.
- **SP8** (T3) MI test-combining line (Meng–Rubin → Chan) + the prior MI-AIC (C-C 2010, penalty 2p_S, theory flagged open) as launch points for the applications.

#[ ]

## U3 — S3 METHODS: THE WORKFLOW (sec-methods, M3, NEW) — est. 7-9 paragraphs

**Goal:** The AI-human workflow as method — factual passive voice (T-05), one
paragraph per part, every gate paragraph ends with what it cannot catch; sign episode
is the single narrative; protocol records to appendices (D-08 note); sits low on the
technical gradient, not announced.

- **SP1** Roles and decision discipline (prompter of record, dated decision log).
- **SP2** Sourced derivation + mechanical citation hook; blind spot: existence, not understanding.
- **SP3** Derive → dual-CAS → Monte Carlo; trust tiers defined once; blind spot: shared wrong conditioning.
- **SP4** Preregistration before code, dated amendments, failures reported; blind spot: disciplines reporting, doesn't validate derivations.
- **SP5** Cross-model blind + instructed-to-refute; the 8-of-9 sign episode as worked example.
- **SP6** Reproducibility (seeds, caches, single entrypoints); blind spot: numbers, not interpretation.

#[ ]

## U4 — S4 DERIVATIONS (sec-derivations, M4a) — est. 20-26 paragraphs

**Goal:** The analytic content, trust-tier graded, as the level-by-level answer to
the S1 principle: (a) theorem = criterion replication; (b) LRT = decision-rate for
testing; (c) IC = decision-rate for selection. Headline numbers inline (D-03);
proofs to companion (D-08). Technical peak.

- **SP1** E[T] = +½tr(RIV) + (A)+(C), fitted-imputation convention, oracle contrast up front (D-02).
- **SP2** Estimated-scale requirement (known-scale collapse); (A)+(C) three-tier standing.
- **SP3** Pooled MC 2.43 ± 0.26 vs analytic 2.42-2.55, inline.
- **SP4** LRT: tr(RIV_⊥) in the I_com metric; naive ALWAYS overstates (52 se).
- **SP5** Pairing collapses noise O(√n)→O(1); (A)+(C) cancels exactly at null; returns only under separation.
- **SP6** IC: +tr(RIV_k) = Shimodaira's AIC_{x;y}; 100% of misclassifications on largest-RIV candidate.
- **SP7** Ladder: rungs 2-3 reach oracle on null side (0.904/0.903 vs 0.899); noncentral shrinkage exact; floor 0.17.
- **SP8** Each subsection opens by naming its principle level.

#[ ]

## U5 — S5 SIMULATION STUDIES (sec-simulations, M4b) — est. 10-13 paragraphs

**Goal:** The consolidated preregistered account as one auditable unit; subheads
"Simulation studies: setup" / "Simulation studies: results" (D-09-A1); "repetitions"
never "replications" (T-07); failures prominent (D-05). Steps back down the gradient.

- **SP1** Setup: apparatus once — designs, mechanisms, engines, repetitions, seeds, prereg + amendment history.
- **SP2** Results: frozen predictions graded (W1, W2 differential, W3/ladder C1-C6, W4 non-nested), each tied to its committed artifact.
- **SP3** Failures as a unit: similar-pair below resolution; N=1000 at 2.6 se; component-level 9-20% misses.
- **SP4** Engine sensitivity scoped (EMB within 2-3% / 0.011) — empirical, not analytic.

#[ ]

## U6 — S6 DISCUSSION (sec-discussion, M5) — est. 9-11 paragraphs

**Goal:** Inverse gradient — open technical (G1-G6 next to their claims, conjecture
labeled), broaden until the close is readable by the S1 reader; plain-language
verdict as the takeaway block; NO separate Conclusion; ends with the provenance
declaration.

- **SP1** G1-G6 with evidential standing.
- **SP2** Power dominance as labeled conjecture (W2 partial support).
- **SP3** Three directions: covariate shift; exact-engine replication; selection-aware calibration (sequel).
- **SP4** Plain-language verdict: corrected criterion matches complete data on average; null side behaves as complete; signal side costs power irrecoverably.
- **SP5** Workflow reflection, itself trust-ordered.
- **SP6** Provenance declaration closes the paper.

#[ ]
