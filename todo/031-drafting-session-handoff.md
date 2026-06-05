# todo/031 — Drafting-session handoff: mi-spectral.qmd from the argument map

**Status:** EXECUTED 2026-06-05. `manuscript/mi-spectral.qmd` drafted from scratch in the
8-section map order (§1 intro/C5, §2 background/B1–B11, §3 setup+theorem/S1–S7→C1–C2,
§4 LRT/C3+L2–L5, §5 IC/C4+I4–I7, §6 numerical studies, §7 discussion/G1–G6, §8 provenance),
~8,800 words, all 28 citekeys read in-session before first use. Plan decisions: §6 standalone
but thin (headline numbers stated where propositions are; shared apparatus + candor notes in §6);
§2 prose with 6 numbered displays; Laplace framing in Rubin's structure with the Tierney–Kadane
parenthetical. Verified: clean Quarto render (0 warnings); 9-agent adversarial map-conformance
review (0 blocking, 5 material — all fixed and re-confirmed); /derivation-audit PASS
(0 BLOCKER / 0 WARN). Original handoff below for the record.
**Goal of the drafting session:** write `manuscript/mi-spectral.qmd` (currently absent from the
working tree — deleted deliberately; the superseded draft survives in git at `75d3ea7`) by walking
the argument DAG left to right. Enter plan mode first; the plan is the section-by-section walk.

## State of the world

- **The argument map is the drafting spine.** Two synchronized representations:
  - `todo/030-concept-map.md` — repo-local text: 5 central propositions (C1–C5), premises
    (S1–S7), application satellites (L2–L5, I4–I7), gaps (G1–G6), typed edges, standing classes
    (T = proved + CAS; M = Monte-Carlo-confirmed; E = empirical/scoped), the DAG orientation
    convention, and the diff rule.
  - litrev DB (project MI-SPECTRAL) — same content plus the Background layer (B1–B11) added
    2026-06-05; 37 propositions, 44 edges, every substantive node carrying evidence rows.
    Render: `visualize_argument_map(project='MI-SPECTRAL', layout='dag')`. Insights backing the
    evidence: `_notes/2026-06-05_synthesis_derivation-argument-map.md` and
    `_notes/2026-06-05_synthesis_background-corpus-verification.md`.
- **The canonical source of all mathematics:** `manuscript/derivation.qmd` (anchors used by the
  map: @sec-thm, @sec-termA, @sec-combine, @sec-lrt-*, @sec-ic-*). The manuscript condenses and
  re-narrates it; it never re-derives.
- **The background corpus is acquired and verified** (todo/003, 2026-06-05 section, with verbatim
  claim-check quotes): DLR 1977, Wei–Tanner 1990, Akaike 1974 (re-acquired after a wrong-PDF
  incident — the first attachment was an agronomy thesis; fully purged), Meng–Rubin 1991,
  Orchard–Woodbury 1972, Tierney–Kadane 1986, plus the owned corpus (Rubin 1976/1987, Schafer,
  Little–Rubin, Meng 1994, Xie–Meng, K&M 1998, Efron–Hinkley, Wilks, Li et al. 1991 ×2,
  Meng–Rubin 1992, Chan–Meng, Chan, Pawitan, Konishi–Kitagawa, Shimodaira ×2,
  Cavanaugh–Shumway, Claeskens–Consentino, Hens–Aerts, Vuong, Wang–Robins, Nielsen, ...).

## Manuscript structure (= the DAG, left to right)

| § | Content | Map nodes |
|---|---|---|
| 1 Introduction | problem, informal result, positioning | C5 framing C1–C4 as forward pointers |
| 2 Background | the standard results later sections consume, in the sources' own words | B1–B11 |
| 3 Setup and main theorem | objects, premises, the theorem, MAR term | S1–S7 → C1, C2 |
| 4 Application I: likelihood-ratio comparison | differential bias, overstatement, pairing, non-nested | C3, L2–L5 |
| 5 Application II: IC selection | corrected criterion, preregistered recovery, ladder | C4, I4–I7 |
| 6 Numerical studies | the Monte Carlo evidence at standing M, presented descriptively | evidence layer |
| 7 Discussion | the gaps, each next to the claim it limits | G1–G6 |
| 8 Provenance and authorship | JAIGP transparency statement | — |

Background walk (B-nodes in narrative order): ignorability (Rubin 1976) → EM and the Q-function
(DLR 1977) → missing-information principle + EM rate (Orchard–Woodbury 1972; Meng–Rubin 1991) →
Rubin's rules as exact posterior moments, r_inf = B/U-bar (Rubin 1987 Result 3.2, eq. 3.1.7) →
the single normal-approximation step (Rubin §2.10/3.2.13) → imputation as Monte Carlo
integration of the E-step (Wei–Tanner 1990, Remark 2) → congeniality (Meng 1994) → AIC as
bias-corrected plug-in (Akaike 1974) → Wilks (1938) → observed-vs-expected information under MAR
(K&M 1998) → MI test combining/calibration (Meng–Rubin 1992 → Chan 2022). Each item is restated
because a named later proposition consumes it — say which, in the text, when natural.

## Binding decisions already made

1. **Laplace framing (decided 2026-06-05, Rubin ch. 3 read):** Rubin's rules are *exact*
   posterior-moment identities (Result 3.2; total variance over imputation draws); the single
   approximation is "the usual approximation of the posterior distribution as normal" (§2.10,
   at 3.2.13). State it in Rubin's structure. "(a Laplace-type approximation;
   @Tierney01031986)" is an optional parenthetical only. Rubin never writes "Laplace."
2. **Trust ordering:** within every section, standing-T material before standing-M, M before E;
   never give an E-finding (the weak-signal floor, engine robustness) a T-tone. The three
   prose rules: precision (every assertion checkable), concision (no decorative restatement),
   trust-ordered organization. Banned: house jargon ("ledger", "witness", "machine-checked",
   "consume") AND businessy/figurative jargon ("where it bites", "honest fences",
   "funnel/hub/rider"). See memory `feedback_outside_reader_prose`.
3. **Diff rule:** a manuscript sentence asserting a relationship not present as a map edge is
   either a missing edge (add it, with evidence) or an unsupported claim (delete it).
4. **Novelty statement (C5, fixed):** the penalty is not new — it is AIC_{x;y}
   [@shimodairaInformationCriterionModel2017]. New: (i) the imputation/estimation decomposition,
   (ii) the MAR (A)+(C) design-imbalance term, (iii) the proper-MI extension. Chan calibrates
   the reference; this work centers the numerator. Both are necessary.
5. **Old draft is salvage, not scaffold:** `git show 75d3ea7:manuscript/mi-spectral.qmd` to
   consult; do not resurrect its structure. Its failure mode was inheriting derivation.qmd's
   proof order instead of the map's narrative order.

## Citation discipline (hard constraints)

- Every `@<citekey>` requires `literature/<citekey>.md` to exist AND **to have been read in the
  drafting session itself** — the in-session requirement does not carry over from this session.
  Re-read each file (targeted sections suffice) before first citing it. The PreToolUse hook
  blocks unbacked keys; `@TODO:<slug>` is the drafting placeholder.
- Orchard–Woodbury is **resolved and citeable** as `woodburyMissingInformationPrinciple1972`
  (year fixed to 1972 on 2026-06-05; the key deliberately keeps the user-pinned `woodbury` slug —
  cite the key exactly as written; the bib author field is correctly Orchard-first).
- Pinned date-keys pending cosmetic normalization (citable as-is): `Meng01121991`,
  `Tierney01031986`.

## Process

- **Plan mode first.** Clarify in the plan: how much of §6 (numerical studies) stands alone vs
  folds into §4/§5; target length; whether §2 background runs as prose or with displayed
  equations.
- Render check: `quarto render manuscript/mi-spectral.qmd`.
- After a full draft exists: `/derivation-audit` supports any `manuscript/*.qmd`; a multi-agent
  (ultracode) adversarial pass against the map is the planned review step — one agent per
  section checking every assertion has an edge, every gap lands in §7, every standing is
  honestly toned. Do not use multi-agent for the drafting itself.
