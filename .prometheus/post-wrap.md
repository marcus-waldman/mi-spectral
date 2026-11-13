# Post-wrap hook — re-derive the wiki from the charter

Invoked by `/prometheus:wrap` step 5, after the charter has been rewritten, validated, and
committed. The charter you are about to read is therefore **final for this session** — the
canon in its settled state.

## Why this hook exists

`wiki/` is a **derived** briefing bundle over the canon (see `wiki/schema.md` §1.1). The
charter churns every session, and nothing else guards the charter → wiki derivation — left
alone, the wiki silently rots into asserting things the canon has since superseded. **This
hook is that guard.** The wrap is the right cadence: it is the only moment the charter
reliably changes, and it fires once per session.

## What to do

1. **Read the canon.** `.prometheus/charter.md` — the **Decisions made** log above all (it
   is append-only and supersedes in place, so read for *supersessions*, not just additions),
   plus Goal / Current milestone / Next 3 actions for the status line.

2. **Find what the wiki now gets wrong.** Read `wiki/index.md` for the catalog, then the
   pages whose `sources:` front-matter cites the charter. Compare their claims to the canon.
   Two failure modes, in priority order:
   - **Wrong** — a page asserts something the charter has since superseded. This is a
     defect: the canon wins (`wiki/schema.md` §1.1). Fix it.
   - **Missing** — a decision or thread in the charter that no page mentions at all. Add it
     where it belongs, or flag the gap in the report if it needs a new page (step 5).

3. **Edit only what drifted.** If every affected page is already accurate, **make no edits
   at all** — not even to `wiki/log.md` — and say so in the report. A no-op is a good
   outcome.

4. **Obey the wiki's contract** (`wiki/schema.md` — read it before editing): derived, not
   canonical (never edit the charter to match the wiki — fixes flow canon → wiki); never
   assert what you cannot cite; keep the front-matter contract (non-empty `type:`, accurate
   `sources:`, `updated:` = today on every page you touch); "link, don't repeat"
   (`wiki/decisions/decisions.md` is the single canonical decisions list); bundle-relative
   absolute links (`/decisions/decisions.md`). Touch nothing outside `wiki/`.

5. **A new page is a judgment call, not an automatic step.** Prefer folding new facts into
   an existing page and **flagging the gap in your report** for the owner, rather than
   growing the wiki unilaterally at wrap time.

6. **If (and only if) you changed pages:** append one dated bullet to `wiki/log.md`
   summarizing the sync, then validate and commit:

   ```
   py "C:/Users/marcu/git-repositories/prometheus/scripts/wiki_validate.py" wiki
   git add -- wiki/
   git commit -m "wiki: sync to charter (post-wrap)"
   ```

   The validator must exit 0. **If it fails, do not commit** — report the problem and leave
   `wiki/` dirty for the owner. On a local-only repo (`wiki/` is git-ignored) skip the
   add/commit — the refreshed pages on disk are the deliverable; say so in the report.

7. **Report** (folded into the wrap's report): pages changed and why, any gap you flagged
   for the owner, and the commit sha — or "wiki already accurate, no changes."

## Scope guardrails

- Stage and commit **`wiki/` only**. The charter commit is already done and is not yours to
  amend.
- This hook does **not** push. The owner pushes.
