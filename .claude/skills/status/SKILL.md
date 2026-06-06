---
name: status
description: Project-manager dashboard for the mi-spectral manuscript. Use when the user asks "/status", "where are we", "what's next", "what am I blocked on", "what's waiting on me", or at the start of a manuscript work session. Derives the picture from manuscript/plan/status.json, decisions.md, the level files, and git — never from session memory — and reports drift if they disagree.
---

# status

The project manager. Marcus juggles several projects; this dashboard must answer, in one
screen, (1) where the manuscript is, (2) what only Marcus can do, (3) what Claude can do
without him, (4) whether the recorded state matches reality.

**Derive, never recall.** Every line of the dashboard comes from files and git as they
are right now. If session memory disagrees with the files, the files win and the
discrepancy is reported.

## Steps

1. **Read state.** `manuscript/plan/status.json`, `manuscript/plan/decisions.md`, and the
   `metadata.status` + `metrics_gate` of each `manuscript/plan/level*.json`.
2. **Check drift.**
   - `git status --porcelain` on `manuscript/plan/` and `manuscript/mi-spectral.qmd`:
     uncommitted changes mean a review cycle ended without its commit phase — report it.
   - `git log -1 --format=%cd --date=short` vs `status.json.last_updated`: commits after
     the last status update mean status may be stale — report it.
   - If level3 `compile_enabled` is true: compare mtimes of `level3-paragraphs.json` and
     `manuscript/mi-spectral.qmd`; an older qmd is stale — report it.
   - Run `py scripts/check_plan.py`; report anything non-green.
3. **Citation backlog.** From `level4-evidence.json`, count entries by `evidence_status`
   (`proposed` / `queued` / `acquired` not yet `verified`). Cross-check `proposed` against
   `todo/003-references-to-acquire.md` and flag entries present in one but not the other.
4. **Render the dashboard** (compact, plain text):
   - Header: project, goal, phase, last_updated (+ stale warning if drift found).
   - Section table: id, title, state, blocking dependency if any.
   - Levels line: level1–4 states and gate pass/fail where evaluated.
   - **Waiting on Marcus** — numbered, each with the exact artifact path and a time
     estimate. This is the most important block; if `blocked_on.who == "marcus"`, lead
     with it.
   - **Claude can do without Marcus** — concrete next actions not gated on annotation.
   - Open decisions (id + one-line label + status).
   - Citation backlog counts.
   - Drift report (or "none — status matches git").
5. **ClickUp mirror (only if `status.json.clickup.list_id` is set).** Sync each section's
   state to its ClickUp task; update `last_synced`. If `list_id` is null, do NOT create
   anything; once per project, offer to set the mirror up and record the answer in
   `status.json.clickup` (`list_id: "declined"` suppresses future offers).

## Rules

- Read-only except for the optional ClickUp sync and `clickup.last_synced`. The dashboard
  never edits plan content, never advances states.
- If `status.json` is missing or unparseable, say so and reconstruct a best-effort view
  from git + the level files, clearly labeled as reconstructed.
- Keep the dashboard under ~40 lines. Detail lives in the files; this is the glance.
