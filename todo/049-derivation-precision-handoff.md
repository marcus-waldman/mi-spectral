# todo/049 — session handoff: R11 typed-precision pass over derivation.qmd + the response letter

**STATUS: EXECUTED (2026-07-05, same day). Inventory `6aa2243` (flag-only, mirroring the
ratified template: derivation 114 hit-lines -> 5 E2 / 2 borderline / 15 E3 / 65 E1 / 26
measurement-sense / 1 record; letter 15 hit-lines -> 0 E2 / 6 E1 / 6 E3 / 2 quoted).
Marcus gated per item and approved all recommendations. Applied `4ac5a90` (14 derivation
+ 4 letter edits, guarded script, all count-asserted); incidental D-26 straggler found
and closed at `e6fd0b1` (authorized rescope #6, S5-P13, was missing from the S5 batch —
applied with the ratified wording via `update-r11-rescope6-s5p13-20260705.py` + rebuild +
PDF render exit 0). Verification: derivation render exit 0 (20/20 Appendix B cells),
derivation-audit engine PASS 0 blocker / 0 warn / 16 pre-existing INFO (= `4e93aaf`
baseline), check_plan green throughout. The E1 supermajority predicted below held.**

**(Original handoff, written 2026-07-05 immediately after the todo/048 style review
completed end to end and the evidence-map table landed; kept as the record.)** This
is the follow-up D-26 explicitly queued and Marcus explicitly signalled as next ("Before
we go over the derivation.md..."): apply the R11 typed-precision rule to the two documents
OUTSIDE todo/048's scope — `manuscript/derivation.qmd` and
`manuscript/reviews/v1/response/response-letter.md`. This file is the self-contained spec
+ resume prompt.

## Recommended model / effort

**Fable 5, effort HIGH.** The task is per-instance classification and judgment (is this
"exactly" a finite-sample identity or a leading-order claim?), not new mathematics — the
same profile as the todo/048 session, which ran at HIGH and whose classifications survived
Marcus's scrutiny unchanged. The cross-model xhigh derivation protocol does NOT apply: no
claim's mathematical content changes; only its stated precision scope. Escalate a single
instance to a CAS check (sympy) only if its E1-vs-E2 classification genuinely turns on
algebra you cannot verify by reading.

## The rule being applied (R11, D-26 — verbatim from the decisions record)

"exact/exactly/precisely" is reserved for (i) finite-sample algebraic identities and
closed forms, (ii) definitional identifications, (iii) if-and-only-if conditions, and
(iv) the exact-sampler sense standard in the MCMC literature. A claim whose content is
leading-order (built on a truncated expansion, carrying an $O(n^{-1})$ or $o(1)$
remainder) either takes the scope word ("to leading order", "up to $O(n^{-1})$") or
attaches the exactness to the COEFFICIENT, never to the equality ("the leading term is
exactly $\tfrac12\operatorname{tr}(\mathrm{RIV})$"). Idiomatic intensifiers are thinned
where cheap.

**The template of record:** `manuscript/reviews/style/precision-addendum-2026-07-05.md` —
the manuscript's 49-instance inventory with the E1/E2/E3 taxonomy, per-instance
dispositions, and proposed wordings. Mirror its structure exactly (Marcus has already
ratified that format and that taxonomy).

## Scope and scale

- **IN:** `manuscript/derivation.qmd` (~2,637 lines; ~90 hit-lines for
  exact/exactly/precisely — expect MORE instances than lines) and
  `manuscript/reviews/v1/response/response-letter.md` (14 hit-lines).
- **OUT:** the main manuscript (already done, @`ede60c2` + the D-26 sweep), level3,
  CLAUDE.md, the guards (already recalibrated), todo/ registration docs (historical
  record — do NOT retro-edit frozen registrations), tkal-review transcripts (frozen).
- **PRECISION-ONLY, not a register sweep.** derivation.qmd's register is its own
  (D-08: the sourced-audit companion; deliberately technical; D-17's no-quotes rule does
  NOT apply to it). Do not import the manuscript's R1/R2 sentence-architecture rules, the
  vocabulary gate, or the caption conventions. Only R11.
- **Expect an E1 supermajority.** derivation.qmd is dense with genuinely exact content
  (CAS-verified identities, exact-rational enumerations, iff conditions, Lemma P's exact
  cancellation of the two order-one functionals, "exact sampler"/"exact-identity
  evaluator" senses, Rubin's Result 3.2 identities). The manuscript's ratio was 35 E1 /
  6 E2 / 6 E3 of 49; the derivation's E2 fraction is likely lower still. Do not
  manufacture rescopes to look thorough — a mostly-KEEP inventory is the expected
  honest outcome. Special care: Appendix B text describing what the CAS cells verify
  ("verified exactly", "matches exactly") is usually E1 (symbolic equality or
  exact-rational arithmetic IS exact); Monte Carlo comparisons ("matches", "within") are
  where E2 candidates hide.
- **Known anchors already consistent with R11** (do not "fix" these): the theorem
  displays carry explicit $+\,O(n^{-1})$ / $O(1/N)$ remainders; Lemma P's cancellation is
  an identity between the named order-one terms; the D-22/D-25 scope callouts were
  drafted post-quorum with the scope words in place.

## Process (mirror todo/048's ratified pattern)

1. **Inventory (flag-only).** Grep both files for `exact|exactly|precisely` (also scan
   `precise` and "identically" for completeness), classify every instance E1/E2/E3 with
   `:line` refs and quoted context, propose the rescope wording for each E2 and the thin
   for each E3. Commit as
   `manuscript/reviews/style/derivation-precision-inventory-<date>.md`. NO edits yet.
2. **Marcus's gate.** He approves/amends per instance (he has ratified this taxonomy
   once already; present borderlines honestly as borderlines).
3. **Apply** via a guarded script or careful Edits (see gotchas), E2/E3 changes only,
   nothing else in the touched sentences.
4. **Verify:** `quarto render manuscript/derivation.qmd` MUST exit 0 with all Appendix B
   cells executing (the qmd embeds executable sympy/numpy — a botched edit near a code
   cell breaks execution, not just prose); then run the `/derivation-audit` mechanical
   engine and require 0 blocker / 0 warn (baseline: 0/0 as of `4e93aaf`); `py
   scripts/check_plan.py` stays green (it resolves `deriv:` anchors against
   derivation.qmd — do not break an anchor).
5. **Letter:** same inventory→gate→apply, lighter; the letter quotes reviewer comments
   verbatim — NEVER edit inside a quoted reviewer block; only the response prose.
6. Commit per document or together; push.

## Known gotchas (all previously bitten)

- **Citation hook cwd bug:** Edit/Write on `manuscript/` paths can misfire if cwd is a
  subdirectory — work from the repo root; if it misfires anyway, fall back to a Python
  script. NEVER a Bash heredoc for content with backslashes (it eats one escape level;
  `\tfrac` → TAB; the todo/045c landing bug).
- **Branch check:** `git branch --show-current` = `main` before any render.
- **Slow first render** = tinytex updating; let it finish (background it).
- **derivation.qmd anchors:** `{#sec-...}`, `{#eq-...}`, `[mc]` hooks, and the Appendix A
  source-fingerprint blocks are load-bearing (check_plan + derivation-audit resolve
  them); edits must not touch anchor syntax.
- **Frozen registrations:** if an E2-looking "exactly" sits inside quoted historical text
  (a registration excerpt, a gate transcript quote), it is RECORD, not prose — leave it
  and note it in the inventory as out-of-scope.

## Context from this session (2026-07-05, for orientation)

todo/048 completed end to end: rubric/review/demos (`c75eb4f`), precision addendum
(`ede60c2`), D-26 + guard recalibration (`0cf2e1a`), six Marcus-gated section batches
(`8057b4f`..`1b621dc`), closing commit (`a5ca468`: vocab gate FATAL, ladder naming
clause, exit 15.2→17.1 w/s). Then the evidence-map table (Marcus's claims-to-evidence
directive): S5-P1b `@tbl-evidence-map` with the verdict column defined against the
pre-registered pass criteria (`e31fd0c`/`787b8d8`). Manuscript = 88 paragraphs, renders
exit 0, check_plan green under the fatal gate. Full record: decisions.md D-26, the
charter's 2026-07-05 session note, and `manuscript/reviews/style/`.

## Marcus prerequisites: NONE blocking

Both target files are in-repo; the template addendum is committed; no acquisitions needed.

## Resume prompt (paste as the opening message)

Resume mi-spectral. Confirm `git branch --show-current` first (should be `main`, in sync
with `origin`; last substantive commit `787b8d8`, the evidence-map verdict column; charter
wrap after it). Read `.prometheus/charter.md` for current state.

Task — the R11 typed-precision pass over `manuscript/derivation.qmd` and
`manuscript/reviews/v1/response/response-letter.md`, per
`todo/049-derivation-precision-handoff.md` (read it in full first; it is the spec of
record): build the full exact/exactly/precisely inventory for both documents with
per-instance E1/E2/E3 classification, :line refs, and proposed wordings, mirroring the
ratified template at `manuscript/reviews/style/precision-addendum-2026-07-05.md`; commit
it flag-only and present it at my gate. NO edits before my approval. After approval:
apply E2/E3 changes only (guarded script or root-cwd Edits, never a Bash heredoc), then
`quarto render manuscript/derivation.qmd` exit 0 with all Appendix B cells executing,
the derivation-audit engine at 0 blocker / 0 warn, and check_plan green. This is
precision-only — derivation.qmd keeps its own register (D-08), and quoted reviewer text
in the letter is untouchable. Expect an E1 supermajority; a mostly-KEEP inventory is the
honest outcome, not a failure to find work.
