# Current status — read this when resuming

**Last updated:** 2026-05-23 (comprehensive sweep complete).

**Project:** JAIGP theory paper on deviance-bias correction for the Q-function under congenial multiple imputation, with applications to LRT model comparison and information-criterion model selection.

## How to resume

1. Read this file.
2. Read `IDEAS.md` — the "Comprehensive sweep results (2026-05-23)" section near the bottom has the freshest empirical landings: 60-cell W3 sweep + 18-cell W1 sweep + H3b rate arm + Phase 4 parameter-bias measurement, all run via the centralized `verification/run_all.R`. The "Reframing note (2026-05-22)" at top explains the major mid-session pivot.
3. Read `CLAUDE.md` Scope + Core contribution sections.
4. The active work item is **manuscript drafting** — all empirical witnesses are now in. Open side artifacts: `todo/007-sympy-proof-verification.md` (Sympy/Quarto algebra-verification companion to W1, pickup-able cold).

**Reproducing the empirical evidence**: `Rscript verification/run_all.R 2000 prod all 20`. Single command, ~3 hours on 20 cores, all 5 phases. Outputs at `verification/cache/run_all-prod/phase{0,1,2,3,4,5}/`.

## What happened this session

**Big things, in chronological order:**

1. **Phase 1 corpus acquisition** — closed. 26 references in `literature/<citekey>.md`, all verified or acquired, indexed in litrev RAG. Pipeline: Zotero → migrate to drive folder → Mathpix conversion → lit-sync → citation hook enforces at edit time.
2. **Infrastructure built** — `scripts/lit_sync.py` (BBT → literature/<citekey>.md bridge), `.claude/hooks/check_citations.py` (PreToolUse hook blocking unverified cites), `.claude/skills/lit-sync/SKILL.md` (invokable as `/lit-sync`).
3. **Upstream issues filed at litrev_mcp:** #21 (embed batch overflow on math-heavy long books — patched and verified) and #22 (Windows hardening for generate_index_script — proposed fixes).
4. **Manuscript design converged** through extended discussion on style, contributions, voice, witness placement.
5. **Mid-session reframe (the big one)** — read Chan (2022, *Annals of Statistics*) "General and feasible tests with multiply-imputed datasets" and discovered it substantially preempts the original spectral-correction headline. Pivoted the paper to the deviance-bias decomposition (originally Claim 1), with Chan & Meng (2022) and Chan (2022) AoS repositioned as adjacent test-calibration work that consumes our bias-corrected numerator. See IDEAS.md Reframing note for details.
6. **Three documents updated to reflect the reframe:** IDEAS.md (major rewrite, archive at bottom), litrev `_context.md`, CLAUDE.md.
7. **Witness apparatus reduced** from V1–V7 (spectral correction validation) to W1/W2/W3 (deviance-bias-focused). W1 validates the theorem; W2 quantifies LRT power loss under local alternatives; W3 demonstrates model-selection distortion under uncorrected MI-AIC/BIC.

## Next action (pick up here)

**Write `todo/004-simulation-hypotheses.md`.** For each of W1, W2, W3:

- **W1 (theorem validation):** Empirical $E[\bar Q_\infty(\hat\theta_{\text{obs}}) - \ell_{\text{com}}(\hat\theta_{\text{obs}})]$ should match $+\tfrac{1}{2}\text{tr}(\text{RIV})$. Imputation-bias term should match $+\text{tr}(\text{RIV})$. Estimation-mismatch should match $-\tfrac{1}{2}\text{tr}(\text{RIV})$.
- **W2 (LRT power):** Under local alternatives $\theta = \theta_0 + n^{-1/2}\delta$, bias-corrected LRT statistic has higher power than bias-uncorrected (both using Chan 2022 AoS reference distribution). Gap widens with $\|\delta\|$. Four configurations: oracle, bias-corrected + Chan, bias-uncorrected + Chan, bias-uncorrected + EFMI/Meng-Rubin.
- **W3 (model selection bias):** Uncorrected MI-AIC systematically favors models with smaller RIV. True-model selection rate for corrected MI-AIC ≈ oracle; uncorrected drops by some materially-large fraction.

For each: predicted outcome, simulation design (N, M, missingness pattern, models compared), fallback path if prediction fails. Pre-registered design.

## Then implement W1, W2, W3

Three pending tasks (#25, #26, #27) — execute in order W1 → W2 → W3. W1 is the gate: if it fails empirically, the framework is wrong and the paper doesn't justify. W3 is the headline empirical claim; gets the most polish once W1/W2 are solid.

Code lives in `verification/`:

```
verification/
├── 00-setup.R                  # shared MVN data gen, MI, fits
├── W1-bias-decomposition.R     # theorem validation
├── W2-lrt-power.R              # LRT power under local alternatives
├── W3-model-selection.R        # MI-AIC/BIC accuracy
└── cache/                      # RDS outputs read by manuscript
```

## Open user actions

- **Task #13:** Refresh BBT keys for 3 Zotero items still in snake_case (`li1991large`, `li1991significance`, `petersen2008matrix`). Cosmetic — corpus works without it, but breaks the camelCase pattern of the other 23. Right-click each → Better BibTeX → Refresh BibTeX key in Zotero desktop. Then re-export BBT.

## Project state at a glance

| Component | Status |
|---|---|
| Phase 1 literature corpus (todo/001) | ✅ 26 papers, all verified/acquired |
| Citation-discipline infrastructure | ✅ lit-sync skill + check_citations.py hook live |
| Reference-acquisition backlog (todo/003) | ✅ tracking system in place |
| Chan-Meng verification reading (todo/002) | ✅ both papers cold-read, machinery understood |
| Project narrative (IDEAS.md, CLAUDE.md, litrev) | ✅ all updated for the 2026-05-22 reframe |
| Witness apparatus design | ✅ W1/W2/W3 defined; pre-registration document pending |
| Simulation code (verification/) | ⏸ not started |
| Manuscript draft (manuscript/) | ⏸ not started |

## Key documents

- `IDEAS.md` — directional anchor, reframing note + archive
- `CLAUDE.md` — scope, core contribution, lineage, citation discipline, R style
- `manuscript/mi-spectral.qmd` — empty Quarto stub waiting for §3 draft
- `literature/<citekey>.md` — 26 source markdown files, hook-protected
- `literature/mi-spectral-better-bibTeX.bib` — BBT export, source of truth for citekeys
- `scripts/lit_sync.py` — Zotero/BBT → literature/ bridge
- `.claude/hooks/check_citations.py` — PreToolUse enforcement
- `.claude/skills/lit-sync/SKILL.md` — `/lit-sync` slash command
- `verification/` — empty, awaiting W1/W2/W3 implementations
- `todo/001-literature-and-hooks.md` — closed (Phase 1 corpus acquisition)
- `todo/002-verification-implementation.md` — Chan-Meng reading queue, mostly closed
- `todo/003-references-to-acquire.md` — living reference backlog
- `todo/004-simulation-hypotheses.md` — closed (W1/W2/W3 preregistered at SHA ddc9037; results in IDEAS.md)
- `todo/005-comprehensive-sweep-hypotheses.md` — closed (sweep complete 2026-05-23; H3b partial)
- `todo/006-comprehensive-sweep-execution.md` — closed (executed)
- `todo/007-sympy-proof-verification.md` — open side artifact (Sympy/Quarto algebra-verification notebook spec; pickup-able cold)

## External issues filed

- [litrev_mcp #21](https://github.com/marcus-waldman/litrev_mcp/issues/21) — embed batch overflow on math-heavy long books. Patched (tiktoken-based token counting, 100K batch cap).
- [litrev_mcp #22](https://github.com/marcus-waldman/litrev_mcp/issues/22) — Windows hardening for generate_index_script (SSL cert via truststore + UTF-8 stdout). Proposed fixes; pending upstream.
