# todo/046 — session handoff (2026-07-03/04 → next session)

**STATUS: EXECUTED 2026-07-04.** The Q2 task below was run start to finish on Fable 5 at max
effort: 3a derived + CAS-verified (Lemma P; todo/045 §3.1, commit `4aaeaae`), 3b/3c registered
pre-production and executed same day (all five substantive criteria PASS; §3.4, commit
`afa4438`), the r3#2/G9/D-24 rewrites STAGED in `todo/045c-staged-rewrites.md` (commit
`bb5ebec`) pending the GPT-5.5 Pro gate verdict (`todo/045b`, launched same day) and Marcus's
ratification. Remaining: triage the gate, then land per todo/045c §5. Original handoff text
below, kept for the record. Written at the end of a session that closed most of Phase 4 of the v1-review
response (13/15 comments drafted), ran Phase 3 (non-normal), got called out by Marcus for a
HARKing-shaped write-up, ran it through an adversarial quorum (AMENDED, one objection unresolved),
registered a full investigation (`todo/045`), and then — continued the same day — executed and
closed Q1 of that investigation (the process retrospective). This file is the resume prompt for
whoever (or whichever session) picks this up next, to start Q2.

## Recommended model / effort

**Q2's core derivation task (Sec.3a: does R1-R7 hold for a Bernoulli/logit-link GLM) should run on
Fable 5 at max effort**, not Sonnet. This matches the established precedent for genuinely novel
mathematical derivation in this repo — the DA-engine master formula ($D=-\tfrac12\operatorname{tr}(\mathrm{RIV}_{\mu\mu})-\ldots$)
was derived the same way (`todo/040`, "FABLE AUDIT VERDICT," 2026-07-01/02, max effort), not by
Sonnet. Q2a is the same kind of task: a real, previously-unverified extension of the theorem's
regularity conditions to a new likelihood family, not a mechanical check. **After Fable's
derivation, it still must go through the project's standing cross-model verification protocol**
(`feedback_crossmodel_derivation_protocol`: GPT-5.5 Pro at xhigh effort, backgrounded, 24h
timeout) as an independent second step — Fable deriving it is not a substitute for that
independent check, the same two-step process (Fable derives, GPT-5.5 Pro independently verifies)
that resolved the DA-engine question cleanly. Skipping the independent-verification half of this
is exactly the shape of gap that produced last session's HARKing finding in the first place (an
unverified derivation trusted because it came from a capable source, not because it was checked).

The rest of Q2 (Sec.3b's N-scan reruns and the CAS discreteness check) is mechanical/computational
and fine on **Sonnet 5, high effort**, same as the saved default — no need for Fable there unless
the CAS check surfaces something that itself needs a new derivation. Resolving OBJ-08 (Sec.3c) is a
judgment call informed by 3a/3b's findings, Sonnet + Marcus.

## Resume prompt (paste as the opening message)

Resume mi-spectral. Confirm `git branch --show-current` first (should be
`da-engine-phase0-todo040`, in sync with `origin`). Read `.prometheus/charter.md` first for full
current-state context — it was wrapped at the end of last session (commit `ed8c131` at the time of
the last wrap; check `git log` against `last_synced_commit` before assuming it's current, and run
`/prometheus:wrap` if commits have landed since).

**Where things stand.** The v1-review response milestone has two independent threads. **Thread 1
(Phase 4, solid, closed, don't re-open):** 13 of 15 response-letter comments DRAFTED and landed —
r3#1 (BIC), r1#7, r1#9, all nine Tier C fixes. Only r3#3 (congeniality diagnosis) remains,
blocked on sourcing a citable method. Committed and pushed.

**Thread 2 (Phase 3, the `todo/045` investigation) — Q1 is now CLOSED, Q2 is next.** Recap: the
Phase-3 non-normal illustration (Gamma via brms, Bernoulli via `mice`) found Gamma confirms the
theorem's pattern cleanly, but Bernoulli missed both of its registered targets badly and got
re-scored against a different target only after the miss — which Marcus correctly flagged as
HARKing-shaped. An adversarial `tkal-in-ket` quorum (Gemini lead + Claude-Opus peer) determined
**AMENDED**: conceded that the corrected +0.5 target was not independently derivable before the
miss, and that the 2.2 se residual gap is unattributed; **sustained (OBJ-08, unresolved):** whether
Gamma+Bernoulli suffices to answer r3#2 without a genuine known-scale exemplar. Full record:
`tkal-reviews/quorum-phase3-bernoulli-20260703/DETERMINATION.md`. The response-letter r3#2 entry,
Discussion G9, and `decisions.md` D-24 are flagged STALE — landed and committed, but known to
overclaim, and not to be cited, extended, or built on until this investigation closes.

**Q1 (process retrospective) is CLOSED — read `todo/045-phase3-bernoulli-investigation.md` Sec.2,
"Q1 FINDINGS," for the full account rather than re-deriving it.** Short version: `todo/040` Sec.9
states, verbatim, that the known-scale scope callout gave the prediction "with no new derivation
needed" — Bernoulli's classification was asserted by analogy, never derived, and the entropy
formula/derivative first appear in Sec.10, after the miss. The identical description-only pattern
was used for Gamma, but Gamma's analogy is structurally sound (a genuine second, independent
parameter playing the same role $\Sigma$ plays for MVN) while Bernoulli's is a category error (no
such parameter exists at all — "no dispersion parameter" was wrongly mapped onto "dispersion
parameter held fixed," opposite conditions). Both derivatives were computed and verified this
session (sympy + numeric spot-checks): $dH_{\text{Gamma}}/d\beta=X_i\neq0$,
$dH_{\text{Gamma}}/d\text{shape}=1-1/\text{shape}+(1-\text{shape})\psi'(\text{shape})\neq0$,
$dH_{\text{Bernoulli}}/dp=-\operatorname{logit}(p)$ (re-confirmed, already in the manuscript). The
process fix (write the entropy formula, differentiate w.r.t. every estimated parameter, state
explicitly what licenses an analogy, before any target is registered) is in `todo/045` Sec.2 and
applies to everything below.

**Task — `todo/045` Q2 (Sec.3), start to finish.**
1. **3a (Fable 5, max effort — see "Recommended model" above).** Derive whether the paper's R1-R7
   regularity conditions actually hold for a Bernoulli/logit-link GLM with response-only MCAR
   missingness — not just that Bernoulli escapes the known-scale collapse (proven, Q1), but whether
   it actually lands on the general case's $+0.5$ magnitude, which is not yet established. Apply
   Q1's process fix directly: derive inline, dated, before trusting any target. Then send the
   derivation through the standing cross-model protocol (GPT-5.5 Pro, xhigh, backgrounded, 24h
   timeout) as an independent check — do not treat Fable's output as settled without it.
2. **3b (Sonnet, high effort).** Investigate the unattributed 2.2 se gap: an N-scan on the
   Bernoulli FITTED arm ($N\in\{200,500,1000,2000\}$, mice-only, cheap, no brms needed) to see
   whether the ratio moves toward $+0.5$ as $N$ grows or sits fixed near $+0.85$; a CAS
   (sympy) check of the FIML-analytic anchor for a discreteness-specific correction, analogous to
   `verification/cas-wolfram/verify_engine_gap_sympy.py`; and whether `mice`'s `logreg`
   approximation itself (not exact MCMC) contributes, cross-checkable against a brms
   probit/latent-continuous construction.
3. **3c.** Informed by 3a/3b, resolve OBJ-08 with evidence: decide whether a genuine
   two-parameter known-scale exemplar (Student-t or Laplace, scale and df held fixed) needs to be
   registered and run from scratch — with the entropy-gradient condition derived and dated BEFORE
   any code, per the Q1 process fix, so this second family doesn't repeat the exact failure just
   adjudicated.
4. **Only after 1-3 close:** rewrite the response-letter r3#2 entry, Discussion G9, and
   `decisions.md` D-24 ONCE, correctly, reflecting whatever Q2 actually finds — not a patch of the
   existing stale text. Then r3#3, per-paragraph annotation, compile-enablement, derivation-audit
   0/0, Zenodo, JAIGP.

**Constraints carried forward.** Frozen preregistered originals (`W1-bias-decomposition.R`,
`W2-lrt-power.R`, `W3-model-selection.R` @ SHA ddc9037) untouched. Edit level3 prose via a dedicated
`manuscript/plan/updates/*.py` script, never the rendered qmd directly. The citation hook misfires
on Edit/Write of files under `manuscript/` subdirectories — use Bash for those writes. Any new
empirical decision gets a dated amendment in the relevant todo file before code, not after. The
reproducibility fold-in gate applies to any new cited result — fold into
`run_all.R`/`aggregate.R`/CLAUDE.md before citing, not after; `verification/spikes/phase3-nonnormal-illustration.R`
already has a CLAUDE.md Commands entry and can be extended (e.g. for the N-scan or a new
known-scale exemplar) rather than replaced. Working tree should be clean at the start of this
session (last session's work, including the Q1 findings, is committed and pushed) — if it isn't,
something changed since, so check `git status` before assuming otherwise.
