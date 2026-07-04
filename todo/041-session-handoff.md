# todo/041 — session handoff (2026-07-02 → next session)

**STATUS: CLOSED (2026-07-02).** Everything below was written before Marcus's ratification;
kept only as a historical record of the staging/triage process. **The DA-engine thread is now
fully landed** — derivation.qmd edits + decisions.md D-22 committed (`2ed3f3a`), render-verified,
provenance verify-reads done for the four already-owned papers. See `.prometheus/charter.md`
(current milestone + decisions log) for the up-to-date state; do not act on "The one decision
needed" below as if it were still open. The only remaining item from this thread is Marcus
acquiring the 2-3 not-yet-owned references (charter Next 3 actions #1).

## Where things stood at the time of writing (superseded)

The engine-scope fork opened by the v1 review's data-augmentation gap (r1#8) is now
**derived (Fable 5) → cross-model audited (GPT-5.5 Pro, blind + red-team, xhigh) → triaged**.
The theorem holds for second-moment-matched, regular-draw imputation engines (deterministic
FIML; bootstrap/EMB — the engine this paper's own simulations validated with); genuine
Bayesian posterior draws carry a characterized, disclosed correction. The exact text for the
three `derivation.qmd` edits this implies is staged, gate-cleared, and **waiting on Marcus's
read and ratification** — nothing has landed in the manuscript yet.

## The one decision needed (RESOLVED — Marcus ratified, see charter)

Read `todo/040-derivation-amendment-draft.md` in full — it is short and self-contained: the
exact proposed text for D9 (`derivation.qmd:383-394`), a new scope-and-correction callout
(after `:426`), and the known-scale callout (`:750-766`), plus a draft `decisions.md` entry.
It already incorporates everything the gate triage forced (the C9 scope-condition revision;
dropping Fable's now-discredited "83%/13%/4%" percentage story while keeping the underlying
numbers, which are solid). If Marcus is satisfied: land the three edits + the decisions.md
entry (assign the next D-number) via Bash (the citation hook misfires on Edit/Write under
`manuscript/`). If not: say what needs to change and iterate before landing anything.

## Ordered next actions once ratified

1. **Land the derivation.qmd amendment** (above) + provenance acquisition: von Hippel-Bartlett
   2021 + Efron 1979 into Zotero → `/lit-sync`; verify-reads of Wang-Robins 1998, Nielsen 2003,
   Schafer 1997 `:3502-3532`, Honaker 2011 (all four already `literature/`-resident) at drafting
   time with Appendix-A source pointers.
2. **Phase 1** — fold the DA evidence into the r1#8 response letter: confirmation-with-
   characterization (two independent Jeffreys engines agree to the 3rd decimal; Amelia's
   validation stands, its floor sits inside the (A)+(C) band; recentred-DA is the constructive
   remedy). Do **not** use the deflated-arm percentage story — the gate triage found its
   mechanism wrong (see `todo/040-derivation-amendment-draft.md`'s C6 note).
3. **Phase 2** — MI-BIC block. CHECK the phase2 cell RDS for raw per-rep
   `ell_com/barL/npar/trRIV` before deciding whether to re-aggregate from cache or rerun
   (open question, unresolved, not this session's work).
4. **Phase 3** (non-normal, gated on the MVN-scope call) + **Phase 4** (Tier C/A fixes, letter,
   annotation + compile-enablement → compile + derivation-audit 0/0 → Zenodo → JAIGP).

## Lower-priority / optional, not blocking

- **IMB closed form:** Mode B (GPT-5.5 Pro) delivered a candidate closed form under this exact
  probit-MAR design (Tallis truncated-bivariate-normal moments;
  `verification/cache/layer3-gpt-5.5-pro-da-engine-modeB.md` sec. 4). Not yet independently
  verified — CAS-check it or numerically confirm against the measured −0.005/−0.0065 before
  citing it anywhere.
- **C7 bootstrap-floor N-scan:** extend `verification/_modules/engine-gap-audit.R`'s E3 arm to
  N=500/2000 (cheap, parameter-draw-only) so the new exact-identity mechanism decomposition has
  the same N-coverage as the already-solid original 4-point Amelia scan.
- **Module wiring:** `engine-gap-audit.R` is a standalone module, not yet wired into
  `run_all.R`'s phase dispatch. Do this only if/when the framing is ratified and the evidence
  becomes citable in the manuscript.
- **`triage-c6-deflated-arm.R`** (this session's scratchpad script that found the DA-feedback
  mechanism) is not yet promoted into the repo. Promote it alongside `engine-gap-audit.R` if the
  finding needs to be reproducible from a tracked location rather than just recorded in the
  charter/commit message.

## Key artifacts (this thread)

- `todo/040-audit-response-fable5.md` — Fable's derivation (the claims C1-C9, the master formula).
- `todo/040b-gpt55-gate-package.md` — the cross-model gate package (Mode A/B prompts + grading key).
- `verification/cache/layer3-gpt-5.5-pro-da-engine-mode{A,B}.md` — the actual gate responses.
- `todo/040-derivation-amendment-draft.md` — **the thing to read first**; staged manuscript text +
  full gate-triage notes (C9 revision, C6 finding), preconditions checklist.
- `verification/cas-wolfram/verify_engine_gap_sympy.py` — symbolic verification, 10/10 pass.
- `verification/_modules/engine-gap-audit.R` — the promoted evaluator module.
- `verification/run_layer3_openai.py` — the cross-model gate runner (now supports `-pro` models).

## Constraints carried forward

Frozen preregistered originals (W1/W2/W3 @ `ddc9037`) untouched. Edit level3 not rendered qmds
(D-21). The citation hook misfires on Edit/Write under `manuscript/` — use Bash there. Branch
`da-engine-phase0-todo040` — confirm with the user before pushing further work past what's
already pushed. brms stays response-letter-only unless the user decides otherwise (the todo/003
Bürkner/Stan/LKJ trio is conditional on that).
