# Todo 003 — Reference acquisition backlog

**Status:** Living document. New entries added whenever a paper is proposed during planning but not yet acquired.

## Why this exists

The PreToolUse citation hook prevents `@<citekey>` tokens from landing in `manuscript/` without a backing `literature/<citekey>.md`. That catches violations *at the edit*. But during planning/conversation Claude (or the human) often **proposes** papers by name from training knowledge — citations of intent, not yet citations of record. Without tracking, these proposals leak silently: by the time we draft a section, the question "did we ever acquire that?" gets lost.

This file is the running list of proposals through to either acquisition (paper enters Zotero → lit-sync → eligible for `@cite`) or rejection (we don't actually need it).

## Lifecycle

```
proposed ──► queued ──► acquired ──► verified ──► cited
              │
              └──► rejected (we decided we don't need it)
```

- **proposed** — first mentioned in conversation. Probably from Claude's training-weight knowledge. **Not yet citeable.**
- **queued** — confirmed we want to acquire. Added to Zotero `mi-spectral` collection (possibly as a stub `_needs-pdf` entry).
- **acquired** — PDF in `Google Drive/Literature/MI-SPECTRAL/`, Mathpix-converted, `literature/<citekey>.md` exists.
- **verified** — read in-session, the claim attributed to it has been checked against the actual text. **Eligible for citation per CLAUDE.md.**
- **cited** — actually appears as `@<citekey>` in `manuscript/`.
- **rejected** — examined and decided unnecessary; remove from active queue.

## Discipline

- Whenever Claude proposes a paper by name in conversation (e.g., "as in Ledoit-Wolf shrinkage"), **add a row to this table within the same session**, even if it's just `[proposed]` with a partial citation. Otherwise the proposal evaporates.
- The conversation entry should record: (a) what claim it was meant to support, (b) approximately where in the manuscript it would land, (c) whether it's a "must have" or "nice to have" for the paper.
- Promote `proposed → queued` only when a human (the user, not Claude) confirms acquisition.
- Once acquired, follow the normal acquisition pipeline (Zotero → migrate → index_papers → lit-sync). Then mark `acquired`.

## Active queue

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| Ledoit, O. & Wolf, M. — shrinkage estimation of covariance matrices | **rejected (subsumed by Lam 2019)** | — | — | — | Initially proposed 2026-05-22 from my training-weight knowledge. After Consensus search (2026-05-22, saved at `~/Google Drive/Literature/MI-SPECTRAL/_notes/consensus-regularized-covariance-2026-05-22.md`), decided Lam (2019) review is the single canonical citation. |
| Marchenko, V. A. & Pastur, L. A. (1967) | **rejected (subsumed by Lam 2019)** | — | — | — | Same — generic-phrasing decision plus Lam (2019) covers MP-based methods. |
| **Lam, C. (2019).** "High-dimensional covariance matrix estimation." *Wiley Interdisciplinary Reviews: Computational Statistics* 12. DOI: 10.1002/wics.1485 | acquired | **Single future-work citation** for the small-$M$ / $M \leq k$ regime. WIREs review covers all the families (structural, shrinkage, rotation-invariant, Bayesian/robust). | Discussion (§10) future-work paragraph | Medium | In `literature/lamHighdimensionalCovarianceMatrix2020.md`; in RAG. Treated as future-reference pointer only — no deep read needed. |
| **Chan, K. W. (2021).** "General and feasible tests with multiply-imputed datasets." *Annals of Statistics* (date as listed in Chan-Meng 2022 references; volume TBD — may have been published post-2022). | **proposed — URGENT** | **Potentially closest predecessor to mi-spectral.** Chan-Meng (2022) explicitly cite this paper as "a possible remedy" for the EFMI-violation regime, which is precisely mi-spectral's target. **Must read before finalizing §1 contribution claims** — may reshape what we claim as novel, or in the worst case fully preempt our contribution. | §1 Introduction (lineage), C1–C4 framing, §7 Related Work | **High — read carefully** | Discovered 2026-05-22 in §2.3 of Chan-Meng (2022). Search hint: title is "General and feasible tests with multiply-imputed datasets" by Kwun Chuen Gary Chan, *Annals of Statistics*. Listed as "to appear" in 2022 references — actual publication may be late 2022 or 2023. Try Annals of Statistics archive or arXiv. |
| **Satterthwaite, F. E. (1946).** "An Approximate Distribution of Estimates of Variance Components." *Biometrics Bulletin* 2(6), 110–114. DOI: 10.2307/3002019 | queued (in Zotero, 2026-05-22) | **HIGH — anchor for moment-matching variance approximation.** Our scaled-shifted form $a\chi^2 + b$ is the two-moment Satterthwaite generalization. | §6 and §7 (introducing the correction); reviewers will demand this cite. | High | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| **Imhof, J. P. (1961).** "Computing the Distribution of Quadratic Forms in Normal Variables." *Biometrika* 48(3–4), 419–426. DOI: 10.1093/biomet/48.3-4.419 | queued (in Zotero, 2026-05-22) | Exact distribution of $\sum_j \lambda_j Z_j^2$ (generalized chi-squared) that our scaled-shifted approximates | §6 (defining the target distribution); V5/V6 witnesses for exact-vs-approximation comparison | Medium | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| **Davies, R. B. (1980).** "Algorithm AS 155: The Distribution of a Linear Combination of χ² Random Variables." *Applied Statistics* 29(3), 323–333. DOI: 10.2307/2346911 | queued (in Zotero, 2026-05-22) | Computational algorithm for generalized chi-squared distribution (Imhof alternative) | §6 if we discuss computational details of the exact reference distribution | Medium | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| `claeskensconsentinoVariableSelectionIncomplete2008` | acquired (literature/) | Anchor citation for the block-diagonal decomposition of RIV under $(β, α)$ when $X$ has missingness | Discussion (§10), one sentence on the missing-covariates extension | Medium | Zotero key U3F5HN8W (also in MI-IC); markdown synced; in MI-SPECTRAL RAG. Not yet read in-session. |
| `consentinoclaeskensOrderSelectionTests2010` | **verified (cold-read 2026-05-22)** | Adjacent prior MI-testing work — omnibus order-selection lack-of-fit testing. **NOT a competitor for our headline.** They use Meng-Rubin's scalar-r F-reference as-is; no EFMI/anisotropy treatment; "order" in their sense ≠ our spectral order. | §7 Related Work, one sentence | Medium | Zotero key 9U4662KK; markdown synced; in RAG. Cited in body as adjacent literature; doesn't preempt any C1–C3 claim. |
| **Honaker, J., King, G. & Blackwell, M. (2011).** "Amelia II: A Program for Missing Data." *Journal of Statistical Software* 45(7), 1–47. | **proposed** | Canonical citation for the EMB (Expectation-Maximization with Bootstrapping) imputation algorithm used as the primary MI engine in `verification/`. Replaces `norm::da.norm` (Schafer 1997) after W1 pilot revealed `norm` was delivering systematically different posterior draws (Term 1 ~5× too small). | §3 (W1 implementation), §4 (W2 implementation), §5 (W3 implementation), §6 (Methods / Simulation Design) | High | Pilot validated 2026-05-22; engine swap committed at the corresponding pre-registration amendment. Need PDF acquisition + lit-sync before any `@honakerAmeliaIIProgram2011` citation in `manuscript/`. |

## Derivation-ledger references (proposed 2026-05-23)

Surfaced while mapping the formalized derivation ledger (explicit axioms / regularity
conditions / lemmas, each step tagged). Backbone already covered by the corpus above
(van der Vaart, Matrix Cookbook, Anderson, Meng 1994, Rubin 1976/1987, Schafer,
Little-Rubin, Cavanaugh-Shumway). These four are the gaps; the first two carry the
theorem's hard content (L2, L3).

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Louis, T. A. (1982).** "Finding the Observed Information Matrix When Using the EM Algorithm." *JRSS-B* 44(2), 226-233. | **proposed -> likely REJECT (subsumed by Schafer, owned)** | Missing-information principle `I_obs = I_com - I_mis|obs` (ledger D7) and score projection `E[U_com U_obs^T] = I_obs` (ledger L3). | §3 derivation (D7, L3); appendix ledger | Low | **Search 2026-05-23:** `schaferAnalysisIncompleteMultivariate1997` SS3 "The missing information principle" states D7 directly as eq (3.19) `I_c = I_o + I_m`, with the rigorous derivation and the interchange-of-differentiation regularity, and names Orchard-Woodbury (1972) / DLR (1977) / Louis (1982) / Meng-Rubin (1991a) as the primary sources. Schafer (owned) read in-session -> VERIFIED for D7. Cite Schafer; acquire Louis only if a reviewer wants the primary-source observed-information formula specifically. NOTE: Schafer's "fraction of missing information" D = I_c^{-1} I_m (EM rate) is NOT our RIV = I_obs^{-1} I_mis -- the ledger must define and relate the two (shared I_mis, different left factor). |
| **Hausman, J. A. (1978).** "Specification Tests in Econometrics." *Econometrica* 46(6), 1251-1271. | **proposed -> likely REJECT** | Efficient-estimator orthogonality -> `Var(theta_obs - theta_com) = I_obs^{-1} - I_com^{-1}` (ledger L2, the line where the -1/2 k bug hid). | §3 derivation (L2); appendix ledger | Low | **Search 2026-05-23:** van der Vaart Ch 11 (Projections) carries the needed machinery -- `cov(T, S_hat) = var S_hat` (md line 5147) and the Pythagorean rule for variances (line 5132), i.e. `var(T - S_hat) = var(T) - var(S_hat)` when `S_hat` is the projection. With the efficient estimator as the projection (efficiency chapter) + Louis (1982) missing-data specialization, L2 is grounded in owned material. Drop Hausman unless we want the one-line applied statement. |
| **Magnus, J. R. & Neudecker, H. (2019).** *Matrix Differential Calculus with Applications in Statistics and Econometrics*, 3rd ed. Wiley. citekey `magnusMatrixDifferentialCalculus2019` | **VERIFIED (acquired 2026-05-23)** | Duplication-matrix / `vech` identities and the MVN Fisher-information closed form via matrix calculus (ledger A8). | §3 (MVN instantiation); appendix ledger | Medium | **Search 2026-05-23 (re-checked broadly):** `petersen2008matrix` (Matrix Cookbook) HAS `vec` (full vectorization, Sec 10.2.2) + Kronecker/trace identities, but NOT `vech` (half-vec) or the duplication matrix `D_p` (no index entry; every "vec" hit is full vectorization). `anderson...2003` likewise lacks it (its 6 "duplication" hits are all the gamma-function formula). So the Cookbook covers A3-A5 (vec/Kronecker/trace) but not (Anderson's 6 "duplication" hits are all the gamma-function duplication formula). Needed ONLY IF the manuscript presents the MVN Fisher info in explicit `vech`/duplication form. The abstract theorem is parameterization-free and never touches `vech`; the MVN closed form is already verified numerically (Sympy notebook). Decision pending the §3 framing fork (explicit `vech` vs coordinate-free matrix form citing Anderson). **RESOLVED 2026-05-23 -> Option A (explicit `vech`).** Migrated (litrev) -> Mathpix-converted (47-pp excerpt) -> lit-synced to `literature/magnusMatrixDifferentialCalculus2019.md` -> read in-session. Confirmed: Ch 3 SS15 defines `vech` + duplication matrix `D_n` (`D_n vech(A)=vec A`, eq 23) and `(D_n'(A(x)A)D_n)^{-1}`; the MVN section derives the information matrix for `mu, vech(Omega)` as `n Omega^{-1}` and `(n/2) D_m'(Omega^{-1}(x)Omega^{-1})D_m` -- identical to our `fisher_info_com_mvn`. Eligible for `@magnusMatrixDifferentialCalculus2019`. |
| **Orchard, T. & Woodbury, M. A. (1972).** "A Missing Information Principle: Theory and Applications." *Proc. 6th Berkeley Symp.* | **proposed** | Original missing-information principle. | §3 / ledger provenance footnote | Low | Likely subsumed by Louis (1982) + Little-Rubin (2019). Acquire only if we want the primary-source attribution. |

## Methods/credibility references (proposed 2026-05-25)

Surfaced while discussing an IMRAD restructure: the manuscript needs an explicit
**Background** (demonstrated command of the lineage) and a **Methods** section that
houses the current §2 verification material *descriptively* rather than defensively.
For Methods to read as principled rather than idiosyncratic, the verification choices
(pre-registration, reproducibility layering, CAS check of LLM-generated algebra) should
sit in an established literature. None of the three veins below is in `literature/` yet;
all are training-weight proposals, **not citeable** until acquired + read in-session.
Citations are approximate and must be checked against the actual text.

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Nosek, B. A., Ebersole, C. R., DeHaven, A. C. & Mellor, D. T. (2018).** "The preregistration revolution." *PNAS* 115(11), 2600–2606. | **proposed** | Grounds the "hypotheses frozen at SHA ddc9037 before simulation" claim in an established norm rather than an idiosyncratic choice — separates evidence from storytelling. | Methods (verification subsection); current §2 "predictions registered before data" paragraph | High | Approx. cite from training knowledge — verify authors/volume/pages. Pre-registration is the load-bearing norm for the W1/W2/W3 apparatus. |
| **Peng, R. D. (2011).** "Reproducible research in computational science." *Science* 334(6060), 1226–1227. | **proposed** | Grounds the three-layer reproducibility (IDEAS.md / run_all.R / caches) and the second-language re-implementation as recognized practice. | Methods (reproducibility subsection) | Medium | Canonical short citation for computational reproducibility. Verify before citing. |
| **AI-assisted-math / proof-verification reference (specific paper TBD)** — candidate veins: formal proof assistants (Lean/mathlib), or recent LLM mathematical-reliability work (e.g. a FrontierMath-style benchmark or an LLM-hallucination-in-reasoning study). | **proposed — needs scoping** | *The* load-bearing citation: justifies *why* an AI-assisted derivation specifically requires the CAS/symbolic check and the four-route triangulation. Turns the verification section from idiosyncratic to principled. | Methods (why-verify framing); current §2 opening | High | No specific paper chosen yet — needs a Consensus/Semantic Scholar pass to pick the right anchor. JAIGP audience makes this the citation most likely to be scrutinized. Acquire deliberately. |

## Finite-sample observed-vs-expected information (proposed 2026-05-30)

Surfaced while diagnosing the W1 finite-sample remainder (why $\hat B + \tfrac12\operatorname{tr}(\mathrm{RIV})$
sits ~10% from zero and does not visibly decay over $N=200\dots2000$). The
`verification/_scratch_b_diagnostic.R` triangulation showed three measurements of $\operatorname{tr}(\mathrm{RIV})$
at $N=500$ split into two camps: closed-form **expected**-information $=5.62$ vs.
numerical-Hessian **observed** $=6.13$ and Rubin between/within **sample-based** $=6.20$.
The $\hat B$ term tracks the observed/sample value, not the expected one — the classic
Efron–Hinkley distinction. This is now load-bearing for the W1 evidence (it reconciles
the theorem's expected-info $\mathrm{RIV}=I_{\text{obs}}^{-1}I_{\text{mis}}$ with the
sample-based $\mathrm{RIV}$ the operational correction actually subtracts).

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Efron, B. & Hinkley, D. V. (1978).** "Assessing the accuracy of the maximum likelihood estimator: Observed versus expected Fisher information." *Biometrika* 65(3), 457–487. | **verified (read in-session 2026-05-31; citekey `efronAssessingAccuracyMaximum1978`)** | The finite-sample W1 remainder: $\hat B$ tracks observed/sample-based $\operatorname{tr}(\mathrm{RIV})$ (≈6.2 at $N=500$), not expected-information (5.62); the ~10% gap is observed-vs-expected information. Grounds benchmarking the bias terms against the sample-based (Rubin between/within) $\operatorname{tr}(\mathrm{RIV})$ and reconciling it with the theorem's expected-info statement. | §3 (W1 numerical confirmation, finite-sample remainder); Methods/Discussion note on expected-info RIV (theorem) vs sample RIV (correction) | Medium–High | Surfaced 2026-05-30 via `_scratch_b_diagnostic.R`. Decomposition: the remainder is ~entirely the variance-identity term (ledger L2); Taylor + evaluation-point pieces vanish cleanly. Training-weight proposal — verify exact volume/pages before citing. Relates to the Hausman/L2 row above (the $\operatorname{Var}(\hat\theta_{\text{obs}}-\hat\theta_{\text{com}})=I_{\text{obs}}^{-1}-I_{\text{com}}^{-1}$ identity, which holds only asymptotically — Efron–Hinkley explains the finite-sample deviation). |

## Information-matrix distinction: J (score-variance) vs I (expected Hessian) (proposed 2026-05-31)

Surfaced when the user pointed to Pawitan's AIC derivation (§13.6, "Robustness of
likelihood specification"), which gives the penalty as $\operatorname{trace}(\mathcal{J}_k\mathcal{I}_k^{-1})$
with $\mathcal{J}=E[UU']$ (score variance / outer product) and $\mathcal{I}=-E[\partial^2\ell]$
(expected negative Hessian). Under correct specification $\mathcal{J}=\mathcal{I}$ (info
equality) and the trace = $k$ (ordinary AIC); under misspecification it is TIC. This is
the precise framework for our 2026-05-30/31 finding: B's $-\tfrac12\operatorname{tr}(\mathrm{RIV})$
weights the estimator-gap variance by the **curvature** $\mathcal{I}_{\text{com}}$ but we
substituted the **expected-information** gap variance $I_{\text{obs}}^{-1}-I_{\text{com}}^{-1}$
(an implicit $\mathcal{J}=\mathcal{I}$ assumption), whereas the gap's *actual* variance is the
sandwich/score-variance ($\mathcal{J}$-flavored) object — exactly the expected-RIV (5.5) vs
sample/observed-RIV (6.1) split. Our `fisher_info_{com,obs}_mvn` compute the $\mathcal{I}$
(expected-Hessian) version only; Rubin between/within and the numerical Hessian give the
$\mathcal{J}$/sandwich version. The derivation must say which information sits in each slot.

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Pawitan, Y. (2001).** *In All Likelihood: Statistical Modelling and Inference Using Likelihood.* Oxford University Press. (§3.5 Lindsey AIC; §13.6 robustness, eq. for $\operatorname{trace}(\mathcal{J}_k\mathcal{I}_k^{-1})$ and (13.4).) | **verified (read in-session 2026-05-31; citekey `pawitanAllLikelihoodStatistical2013`)** | The $\mathcal{J}$ vs $\mathcal{I}$ distinction and $E[n(\hat\theta-\theta_0)'\mathcal{I}(\hat\theta-\theta_0)]\approx\operatorname{tr}(\mathcal{J}\mathcal{I}^{-1})$ — the framework clarifying which information enters tr(RIV); connects our IC application to TIC. | §setup (define both informations), §3.3 (expected-vs-sample RIV), §5 (IC↔TIC) | **High** | Verified in `literature/pawitanAllLikelihoodStatistical2013.md` §13.6: $\mathcal{J}\equiv E(UU')$ (L14618), sandwich $\mathcal{I}^{-1}\mathcal{J}\mathcal{I}^{-1}$ (L14696), **"model correct ⇒ $\mathcal{J}=\mathcal{I}$, reduces to $\mathcal{I}^{-1}$ naive"** (L14699), $\operatorname{trace}(\mathcal{J}\mathcal{I}^{-1})$ (L14707). Pawitan's $\mathcal{I}$=expected Hessian, $\mathcal{J}$=score variance — note convention (opposite of some texts). (Acquired edition is the 2013 printing → year in citekey.) |
| **Konishi, S. & Kitagawa, G. (1996).** "Generalised information criteria in model selection." *Biometrika* 83(4), 875–890. | **verified (read in-session 2026-05-31; citekey `konishiGeneralisedInformationCriteria1996`)** | TIC/GIC anchor: GIC = bias-corrected log-likelihood when "the parametric family does not necessarily contain the true distribution" (Thm 2.1) — the misspecification generalization of AIC's $k$ to a $\operatorname{tr}(\mathcal{J}\mathcal{I}^{-1})$-type penalty. | §5 (IC↔TIC lineage) | **High** | Chosen TIC anchor (accessible substitute for Takeuchi 1976). In `literature/`. |
| **Burnham, K. P. & Anderson, D. R.** *Model Selection and Multimodel Inference* (2nd ed.). Springer. | acquired (`literature/burnhamModelSelectionMultimodel2010.md`) | Textbook TIC discussion; secondary/optional given Konishi–Kitagawa is the primary anchor. | §5 (optional) | Low | Acquired + indexed. Cite only if a textbook-level TIC reference is wanted alongside KK. (litrev key year 2010; verify edition/year if cited.) |
| **Takeuchi, K. (1976).** "Distribution of informational statistics and a criterion of model fitting." *Suri-Kagaku* 153, 12–18 (in Japanese). | **superseded — not acquired** | Origin of TIC. | — | — | Hard to obtain (Japanese, 1976). Cite via Konishi–Kitagawa (1996, verified) instead; keep Takeuchi as a historical-origin mention only. |

## Recently rejected (kept as a record so we don't re-propose)

- **2026-05-22 — Wood, A. T. A. (1989).** "An F approximation to the distribution of a linear combination of chi-squared variables." *Comm. Stat. — Simul. Comp.* 18(4), 1439–1456. DOI: `10.1080/03610918908812585`. Reason: We're sticking with χ² reference (not F), so the F-approximation is not load-bearing. Citation lineage for the scaled-shifted moment-matching form is already covered by Satterthwaite (1946) + Satorra-Bentler (2010) + Asparouhov-Muthén (2006). Imhof (1961) + Davies (1980) cover the exact reference distribution. Full text was also not freely available, which would have been a small acquisition cost — combined with non-load-bearing status → reject. Re-propose only if we change framing to F-reference.
- **2026-05-22 — Ledoit & Wolf (specific paper TBD)** and **Marchenko & Pastur (1967).** Reason: Subsumed by Lam (2019) review which covers the same ground in one citation. See proposed entry above.

## Recently promoted to `literature/` (kept as a record)

- **2026-05-22:** `claeskensconsentinoVariableSelectionIncomplete2008` and `consentinoclaeskensOrderSelectionTests2010` — both acquired via Zotero/migrate/index/lit-sync. The 2010 paper has been read cold and `verified` (synthesis in conversation 2026-05-22; reads as adjacent, not competing).
- *(Phase 1 corpus from `todo/001` already in `literature/` since session opening.)*

---

*Last updated: 2026-05-30*
