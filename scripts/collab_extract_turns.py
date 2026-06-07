# todo/032 Phase A — inventory of user turns in the mi-spectral session transcripts.
#
# Corpus reconciliation (2026-06-07). D-13 says "35 files": at ratification the
# project directory held 35 *.jsonl files = 34 substantive transcripts + one
# 149-byte bridge-session stub (682aca99-*) with no turns. The stub is excluded
# here. The session EXECUTING this analysis (1088cf6b-*, created 2026-06-07
# 14:52 UTC, after D-13) is excluded: it post-dates the frozen corpus and its
# only turn is the execution command itself. Coded corpus: 34 transcripts,
# including 35b5e1cf-* (the session that created todo/032 and ratified D-13).
#
# Keeps: type == "user", non-meta turns whose content carries actual user text.
# Drops (counted per reason): tool_result-only turns, isMeta turns,
# local-command stdout, pure slash-command invocations, harness continuation
# summaries, pure interrupt markers, system-reminder-only content, and trivial
# approvals (bare "yes"/"ok"/"continue" and the like).
#
# Output: verification/cache/collab-analysis/turns/<session>.json (per-session
# turn lists with a short assistant-context tail per turn, for the Phase B
# coders) and verification/cache/collab-analysis/inventory-summary.json.

import json
import os
import re
import sys

TRANSCRIPT_DIR = r"C:\Users\marcu\.claude\projects\C--Users-marcu-git-repositories-mi-spectral"
OUT_DIR = r"C:\Users\marcu\git-repositories\mi-spectral\verification\cache\collab-analysis"

# The frozen D-13 corpus minus the stub: 34 transcripts, 2026-05-22 -> 2026-06-07.
SESSIONS = [
    "131f54f1-70bc-4c26-ad95-f33ffef8e114",
    "1659f932-e1fb-4871-87f8-79a8dd621fec",
    "1877b2af-5b1d-47df-b9c3-997037091294",
    "1cff4222-cee2-48d9-8e41-1fab7a7085e2",
    "29059e85-c96d-4109-8b7b-d82aae911a69",
    "336e846b-886e-4798-85cd-fe63f884c53e",
    "35b5e1cf-a2f6-446c-8655-3074f353af3e",
    "3a3eaa27-6d23-40e9-9d6b-bd9a72bbd9fb",
    "424fd178-25d8-42db-9a54-2d29573214c6",
    "4298ccb8-74a0-403e-b187-393a45936459",
    "5ee18e70-d722-4568-a849-2b741a9794b8",
    "63b28d6e-4646-4397-8e15-3f073347a9fc",
    "7e0e49ed-851c-471c-aa32-5501c6006406",
    "8d32c67f-d28c-4b6a-a63f-22d086df4200",
    "8e25a96f-3de6-4216-a425-d1f649cd20a2",
    "9436d7e4-cbee-4fc1-ad1e-adced7a10e59",
    "972eb380-19df-4264-b371-9020a0012e1a",
    "9ca8497e-dcbe-4b60-b9bd-1769b2e90320",
    "a01c567f-546b-4537-a8e8-f1abe936e394",
    "a33dbba8-2632-4e54-a46a-0d6f1ac15409",
    "ad1b9287-51d2-4269-a3ac-eb1ca8e8da04",
    "af507d14-2e1b-4f6a-b57d-905ab269ccfc",
    "b27ba43d-0ea7-4ea3-8c0a-711ae1acbd26",
    "c691d23e-0311-4162-baa3-ff3355ae725f",
    "c7fe11b9-1e49-40d2-a1d1-58d9b18d6d40",
    "cc106375-7a38-4c2a-b373-097ab14989db",
    "d680983c-5b45-49cd-99af-076df15a981e",
    "da40242c-a05a-41f8-8537-2af19515284d",
    "dc9724ea-fef4-423e-96d4-802101901e29",
    "dce75291-440a-4e1d-aa14-d6d6be4be933",
    "e0ce3eb6-1f8d-4334-83f5-a0e7e13b3d38",
    "ea505749-6826-4c13-99c5-804311090f69",
    "eabfef36-044b-40b9-afb9-7b4861f6c8e8",
    "f42f0b2f-eca0-460a-a8be-d1f6350e78ab",
]

TRIVIAL_RE = re.compile(
    r"^(y|yes|yep|yeah|ok|okay|k|sure|go|go ahead|proceed|continue|do it|"
    r"yes please|please proceed|sounds good|lgtm|approved?|good|great|fine|"
    r"thanks?|thank you|ty|perfect|nice|cool|done|next)[.!?]*$",
    re.IGNORECASE,
)
SYS_REMINDER_RE = re.compile(r"<system-reminder>.*?</system-reminder>", re.DOTALL)
CAVEAT_RE = re.compile(r"<local-command-caveat>.*?</local-command-caveat>", re.DOTALL)
INTERRUPT_RE = re.compile(r"^\[Request interrupted by user[^\]]*\]\s*$")


def text_of(content):
    """Pull the user-authored text out of a message content field."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
        return "\n".join(parts)
    return ""


def assistant_text_of(content):
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
        return "\n".join(parts)
    if isinstance(content, str):
        return content
    return ""


def classify_drop(raw_text):
    """Return a drop reason for harness/trivial turns, or None to keep."""
    t = raw_text.strip()
    if not t:
        return "empty"
    if t.startswith("<task-notification>"):
        # harness-injected background-task notification, not a human turn
        # (identified during Phase B: three coding agents independently
        # proposed a "system-notification" code for these)
        return "task_notification"
    if "<local-command-stdout>" in t:
        return "command_stdout"
    if "<command-name>" in t:
        return "slash_command"
    if t.startswith("This session is being continued from a previous conversation"):
        return "continuation_summary"
    if INTERRUPT_RE.match(t):
        return "pure_interrupt"
    return None


def main():
    os.makedirs(os.path.join(OUT_DIR, "turns"), exist_ok=True)
    summary = {"sessions": [], "totals": {}}
    total_kept = 0
    total_raw_user = 0
    drop_counts = {}
    all_words = 0

    for sid in SESSIONS:
        path = os.path.join(TRANSCRIPT_DIR, sid + ".jsonl")
        turns = []
        n_raw = 0
        last_assistant_tail = ""
        first_ts = None
        last_ts = None
        session_drops = {}

        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                otype = obj.get("type")
                if otype == "assistant":
                    at = assistant_text_of((obj.get("message") or {}).get("content"))
                    if at.strip():
                        last_assistant_tail = at[-600:]
                    continue
                if otype != "user":
                    continue
                msg = obj.get("message") or {}
                content = msg.get("content")
                # tool_result-only turns are harness traffic, not Marcus
                if isinstance(content, list) and all(
                    isinstance(b, dict) and b.get("type") == "tool_result" for b in content
                ):
                    continue
                n_raw += 1
                ts = obj.get("timestamp")
                if first_ts is None:
                    first_ts = ts
                last_ts = ts

                if obj.get("isMeta"):
                    session_drops["is_meta"] = session_drops.get("is_meta", 0) + 1
                    continue

                raw = text_of(content)
                reason = classify_drop(raw)
                if reason:
                    session_drops[reason] = session_drops.get(reason, 0) + 1
                    continue

                # strip harness-injected spans, keep what Marcus typed
                clean = SYS_REMINDER_RE.sub("", raw)
                clean = CAVEAT_RE.sub("", clean)
                clean = clean.strip()
                if not clean:
                    session_drops["reminder_only"] = session_drops.get("reminder_only", 0) + 1
                    continue
                if TRIVIAL_RE.match(clean) or len(clean) < 12:
                    session_drops["trivial"] = session_drops.get("trivial", 0) + 1
                    continue

                turns.append(
                    {
                        "uuid": obj.get("uuid"),
                        "timestamp": ts,
                        "text": clean,
                        "n_words": len(clean.split()),
                        "context_before": last_assistant_tail,
                    }
                )

        all_words += sum(t["n_words"] for t in turns)
        total_kept += len(turns)
        total_raw_user += n_raw
        for k, v in session_drops.items():
            drop_counts[k] = drop_counts.get(k, 0) + v

        out = {
            "session_id": sid,
            "first_timestamp": first_ts,
            "last_timestamp": last_ts,
            "n_raw_user_turns": n_raw,
            "n_kept": len(turns),
            "drops": session_drops,
            "turns": turns,
        }
        with open(os.path.join(OUT_DIR, "turns", sid + ".json"), "w", encoding="utf-8") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)

        summary["sessions"].append(
            {
                "session_id": sid,
                "first_timestamp": first_ts,
                "last_timestamp": last_ts,
                "n_raw_user_turns": n_raw,
                "n_kept": len(turns),
                "drops": session_drops,
            }
        )

    summary["totals"] = {
        "n_sessions": len(SESSIONS),
        "n_raw_user_turns": total_raw_user,
        "n_kept": total_kept,
        "n_kept_words": all_words,
        "drops": drop_counts,
    }
    with open(os.path.join(OUT_DIR, "inventory-summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1, ensure_ascii=False)

    print(f"sessions: {len(SESSIONS)}")
    print(f"raw user turns (non-tool-result): {total_raw_user}")
    print(f"kept substantive turns: {total_kept} ({all_words} words)")
    print(f"drops: {json.dumps(drop_counts)}")
    by_date = {}
    for s in summary["sessions"]:
        d = (s["first_timestamp"] or "?")[:10]
        by_date[d] = by_date.get(d, 0) + s["n_kept"]
    for d in sorted(by_date):
        print(f"  {d}: {by_date[d]} turns")


if __name__ == "__main__":
    sys.exit(main())
