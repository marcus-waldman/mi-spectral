# todo/046 — session handoff (2026-07-03 → next session)

**STATUS: OPEN.** Written at the end of a session that closed most of Phase 4 of the v1-review
response (13/15 comments drafted), then ran Phase 3 (non-normal), got called out by Marcus for a
HARKing-shaped write-up, ran it through an adversarial quorum (AMENDED, one objection unresolved),
and registered a full investigation (`todo/045`) rather than patch the manuscript text in place.
This file is the resume prompt for whoever (or whichever session) picks this up next.

## Recommended model / effort

**Sonnet 5, effort high**, same as the saved default. Q1 (`todo/045` Sec.2) is a reading/writing
retrospective, no special effort needed. Q2 (Sec.3) is real mathematical re-derivation (whether the
paper's R1-R7 regularity conditions hold for a Bernoulli/logit-link GLM) — if that derivation turns
out to be genuinely new (not just confirming existing conditions transfer trivially), it must go
through the project's standing cross-model derivation protocol
(`feedback_crossmodel_derivation_protocol`: GPT-5.5 at xhigh effort, backgrounded, 24h timeout)
before being treated as settled — the same gate the DA-engine master formula went through. Do not
skip that gate this time; skipping exactly this kind of check (deriving a condition and trusting it
without independent verification) is what produced last session's HARKing finding in the first
place.

## Resume prompt (paste as the opening message)

Resume mi-spectral. Confirm `git branch --show-current` first (should be
`da-engine-phase0-todo040`, in sync with `origin` — everything pushed as of `a5b23f7`). Read
`.prometheus/charter.md` first for full current-state context — it was wrapped at the end of last
session (`a5b23f7`, referencing `8c4ed35`), so check `git log` against `last_synced_commit` before
assuming it's current, and run `/prometheus:wrap` if commits have landed since.

**Where things stand.** The v1-review response milestone has two independent threads, and they
must NOT be conflated. **Thread 1 (Phase 4, solid, don't re-open):** 13 of 15 response-letter
comments are DRAFTED and landed — r3#1 (BIC), r1#7 (heavy-tail N=1000), r1#9 (nested-confound), and
all nine Tier C notation/consistency fixes (proof#10/11, contra#12-15, r2#4-6). Committed and
pushed (`fd52e99`), `check_plan` green, manuscript rendered clean. Only r3#3 (congeniality
diagnosis) remains untouched, blocked on sourcing a citable method (log candidates to `todo/003`
first). None of this is affected by Thread 2 below and should not be redone.

**Thread 2 (Phase 3, STALE, the actual work for this session):** the non-normal illustration
(Gamma via brms, Bernoulli via `mice`) ran at R=1000. Gamma landed cleanly — FITTED +0.318 (se
0.200) inside the interval around the predicted +0.5, the brms Bayesian draw more negative
(-0.520), matching the DA-engine's persistent-discount mechanism from earlier in this same
v1-review response. **Gamma is not in question and needs no further work.** Bernoulli missed both
of its registered targets badly (FITTED +0.853 vs. registered ~0, ~5.3 se; the mice Bayesian draw
+0.628 vs. registered ~-0.5, ~7 se, wrong sign). A same-session post-hoc calculation (Bernoulli's
entropy has $dH/dp=-\operatorname{logit}(p)\neq0$, so it fails the theorem's own known-scale
condition) was used to re-score Bernoulli against the general-case +0.5 target instead — landed as
Discussion paragraph G9 (`S6-P4d`), `decisions.md` D-24, and a response-letter r3#2 entry, **before**
Marcus flagged it as HARKing ("why did we select Bernoulli... that seems really weak").

An adversarial `tkal-in-ket` quorum (Gemini lead + Claude-Opus 4.8 peer — `gpt-5.5-pro` could not
be used, its Responses API times out under xhigh effort and its Chat Completions fallback 404s
outright for `-pro` models, a harness gap worth remembering for future quorums/tribunals) returned
**AMENDED**. Conceded outright, not just softened: (OBJ-05) the +0.5 target was not independently
derivable before the miss — the same advocate, same two inputs, reached opposite conclusions
before vs. after seeing data, and no blinded/timestamped re-derivation exists to rule out the miss
having driven the correction; (OBJ-07) the 2.2 se gap between +0.853 and +0.5 is unattributed, so
"same sign, same ballpark" oversold a confirmation with no evidence behind it. **Sustained, not
resolved: OBJ-08** — whether Gamma+Bernoulli suffices to answer r3#2 without a genuine two-parameter
known-scale exemplar (Student-t/Laplace, fixed scale), since Bernoulli's correction removed the
only intended known-scale test and that collapse remains verified only in the multivariate normal
family. Full record: `tkal-reviews/quorum-phase3-bernoulli-20260703/DETERMINATION.md`.

Marcus's ruling at session close: stop patching the write-up. The next session runs a real
investigation into **why** the registration HARKed and **why** the numbers look the way they do,
registered as `todo/045-phase3-bernoulli-investigation.md`. The response-letter r3#2 entry,
Discussion G9, and `decisions.md` D-24 are flagged STALE — left in place, not deleted, known to
overclaim relative to what the quorum found tenable. Do not cite, extend, or build on them until
`todo/045` closes. All of this (the Phase-3 illustration, the quorum transcript at
`tkal-reviews/quorum-phase3-bernoulli-20260703/`, and this stale-flagged text) is already committed
and pushed (`459e2c8`) — the STALE flag is a status marker in the text and in this handoff, not an
uncommitted/pending state.

**Task 1 — `todo/045` Q1 (process retrospective, Sec.2, no code, do this first).** Reconstruct
exactly what happened in `todo/040` Sec.9's registration: was the entropy-gradient condition
($\alpha=-\mathcal{E}'$, entropy must be parameter-free for the known-scale collapse) ever derived
for Bernoulli specifically, or only pattern-matched against "no dispersion parameter"? Read the
actual registration text, don't assume from memory. Then check whether the SAME shortcut affected
the Gamma choice — it happened to be right (Gamma's entropy does depend on shape), but was that
derived at registration time or also just assumed by analogy to MVN's $(\mu,\Sigma)$? If both
choices were analogy-based and only one got lucky, that's a systemic process gap, not a
Bernoulli-specific mistake, and changes the fix from "watch for tricky one-parameter families" to
"always derive $\alpha$ explicitly, every family, no exceptions." Write the concrete process fix
(a registration-doc requirement, possibly a CLAUDE.md addition): the entropy-gradient condition
must be derived inline and dated in the registration text before any pass criterion naming a target
value is written.

**Task 2 — `todo/045` Q2 (substantive re-derivation, Sec.3, real work, possibly new code).** Derive
whether the paper's R1-R7 regularity conditions actually hold for a Bernoulli/logit-link GLM with
response-only MCAR missingness (not just that Bernoulli escapes the known-scale collapse, which is
already proven and solid — whether it actually lands on the general case's +0.5 magnitude, which is
not yet established). Cross-model-verify if this derivation is genuinely new. Then investigate the
unattributed 2.2 se gap: run an N-scan on the Bernoulli FITTED arm ($N\in\{200,500,1000,2000\}$,
mice-only, cheap — no brms needed) to see whether the ratio moves toward +0.5 as $N$ grows
(evidence of a finite-sample term) or sits fixed near +0.85 (evidence of a genuinely different
asymptote); check the FIML-analytic anchor construction for a discreteness-specific correction via
CAS (sympy), analogous to `verification/cas-wolfram/verify_engine_gap_sympy.py`'s approach; and
consider whether `mice`'s `logreg` approximation itself (not exact MCMC) contributes to the
Bayesian-draw anomaly, cross-checkable against a brms probit/latent-continuous construction. Then,
informed by what 3a/3b find, resolve OBJ-08 with evidence: decide whether a genuine two-parameter
known-scale exemplar (Student-t or Laplace, scale and df held fixed) needs to be registered and run
from scratch — with the entropy-gradient condition derived and dated BEFORE any code, per Task 1's
fix, so this second family doesn't repeat the exact failure just adjudicated.

**Task 3 — only after Task 1/2 close:** rewrite the response-letter r3#2 entry, Discussion G9, and
`decisions.md` D-24 ONCE, correctly, reflecting whatever Q1/Q2 actually find — not a patch of the
existing stale text. Then finish r3#3 (congeniality diagnosis), then per-paragraph annotation +
compile-enablement + derivation-audit 0/0 + Zenodo + JAIGP.

**Constraints carried forward.** Frozen preregistered originals (`W1-bias-decomposition.R`,
`W2-lrt-power.R`, `W3-model-selection.R` @ SHA ddc9037) untouched. Edit level3 prose via a dedicated
`manuscript/plan/updates/*.py` script (the established pattern this session used nine times),
never the rendered qmd directly. The citation hook misfires on Edit/Write of files under
`manuscript/` subdirectories — use Bash for those writes. Any new empirical decision gets a dated
amendment in the relevant todo file before code, not after. The reproducibility fold-in gate
(Marcus, 2026-07-03) applies to any new cited result — fold into `run_all.R`/`aggregate.R`/CLAUDE.md
before citing, not after; `verification/spikes/phase3-nonnormal-illustration.R` already has a
CLAUDE.md Commands entry from this session and can be extended (e.g. for an N-scan or a new
known-scale exemplar) rather than replaced. Everything from last session is already committed and
pushed to `origin` (three commits, `fd52e99`/`459e2c8`/`8c4ed35`, plus the charter wrap `a5b23f7`) —
working tree should be clean at the start of this session; if it isn't, something changed since,
so check `git status` before assuming otherwise.
