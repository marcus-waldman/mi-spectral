# todo/032 / D-13 deposit preparation — manifest + sensitive-content scan.
#
# Prepares (does NOT execute) the D-13 transcript deposit:
#   1. deposit-manifest.md — SHA-256, size, and time span for each of the 35
#      D-13 corpus files (34 substantive transcripts + the bridge-session stub).
#   2. deposit-sensitive-scan.md — pattern scan for credentials, local paths,
#      emails, and personal-matter keywords, with masked context excerpts, so
#      the human author can decide on redactions before anything is deposited.
#      Per D-13, any redaction must itself be logged.
#
# Outputs land in verification/cache/collab-analysis/ for review.

import hashlib
import json
import os
import re

TRANSCRIPT_DIR = r"C:\Users\marcu\.claude\projects\C--Users-marcu-git-repositories-mi-spectral"
OUT_DIR = r"C:\Users\marcu\git-repositories\mi-spectral\verification\cache\collab-analysis"

STUB = "682aca99-527e-4829-9c49-eac907c8e7e5"
EXECUTING_SESSION = "1088cf6b-2b12-418d-b171-b05e8a00cb2a"  # post-D-13, excluded

# Pattern -> (label, severity). Severity: HIGH = likely credential, must resolve
# before deposit; MEDIUM = identifying but expected provenance; LOW = informational.
PATTERNS = [
    (r"sk-[A-Za-z0-9_\-]{20,}", "OpenAI-style secret key", "HIGH"),
    (r"ghp_[A-Za-z0-9]{36}", "GitHub personal access token", "HIGH"),
    (r"github_pat_[A-Za-z0-9_]{22,}", "GitHub fine-grained PAT", "HIGH"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key id", "HIGH"),
    (r"AIza[0-9A-Za-z_\-]{35}", "Google API key", "HIGH"),
    (r"xox[baprs]-[A-Za-z0-9\-]{10,}", "Slack token", "HIGH"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "PEM private key", "HIGH"),
    (r"eyJ[A-Za-z0-9_\-]{20,}\.eyJ[A-Za-z0-9_\-]{20,}", "JWT", "HIGH"),
    (r"(?i)\bBearer\s+[A-Za-z0-9_\-\.=]{25,}", "Bearer token", "HIGH"),
    (r"(?i)api[_\-]?key['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}", "api_key assignment", "HIGH"),
    (r"(?i)(secret|token|passwd|password)['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{8,}", "secret/password assignment", "HIGH"),
    (r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", "email address", "MEDIUM"),
    (r"C:\\+Users\\+marcu", "local Windows path with username", "MEDIUM"),
    (r"(?i)\b(ssn|social security|credit card|bank account|routing number)\b", "financial/identity keyword", "MEDIUM"),
    (r"(?i)\b(medication|prescription|physician|psychiatr\w+|therapist|therapy session)\b", "health keyword", "MEDIUM"),
    (r"\b\d{3}[-.]\d{3}[-.]\d{4}\b", "phone-number-shaped string", "LOW"),
]

# Suppression rules applied after pattern matching (each suppression is counted
# and reported, never silent):
#   base64-run  — the match sits inside a >=60-char base64-ish run (embedded
#                 binary/blob content, not a credential).
#   identifier  — the "value" side of an assignment is itself an identifier or
#                 accessor (get_..., os.environ, *_key, *_KEY), not a literal.
BASE64_RUN_RE = re.compile(r"[A-Za-z0-9+/=]{60,}")
IDENTIFIER_VALUE_RE = re.compile(
    r"(?i)[:=]\s*['\"]?(get_|os\.|environ|zotero_api|api_key|your_)|_key\s*\(?\s*\)?\s*$"
)


def suppressed(label, matched_text, text, start, end):
    """Return a suppression reason, or None if the hit stands."""
    if label in ("Google API key", "financial/identity keyword", "JWT"):
        window = text[max(0, start - 200) : end + 200]
        for run in BASE64_RUN_RE.finditer(window):
            lo = max(0, start - 200) + run.start()
            hi = max(0, start - 200) + run.end()
            if lo <= start and end <= hi:
                return "base64-run"
    if label in ("api_key assignment", "secret/password assignment"):
        if IDENTIFIER_VALUE_RE.search(matched_text):
            return "identifier"
    return None


def mask(s):
    """Mask the middle of a matched string so the report itself is safe."""
    if len(s) <= 8:
        return s[0] + "*" * (len(s) - 1)
    return s[:4] + "*" * min(12, len(s) - 8) + s[-4:]


def scan_file(path):
    hits = {}
    supp = {}
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for pat, label, sev in PATTERNS:
        found = []
        for m in re.finditer(pat, text):
            reason = suppressed(label, m.group(0), text, m.start(), m.end())
            if reason:
                key = f"{label} [{reason}]"
                supp[key] = supp.get(key, 0) + 1
                continue
            ctx_start = max(0, m.start() - 50)
            ctx = text[ctx_start:m.start()] + "[" + mask(m.group(0)) + "]"
            found.append(ctx[-110:].replace("\n", " "))
        if found:
            hits[label] = {"severity": sev, "count": len(found), "examples": found[:3]}
    return hits, supp


def main():
    files = sorted(os.listdir(TRANSCRIPT_DIR))
    corpus = [f for f in files if f.endswith(".jsonl") and not f.startswith(EXECUTING_SESSION)]

    # --- manifest ---
    rows = []
    for fname in corpus:
        path = os.path.join(TRANSCRIPT_DIR, fname)
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        first_ts = last_ts = None
        n_user = 0
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                ts = obj.get("timestamp")
                if ts:
                    if first_ts is None:
                        first_ts = ts
                    last_ts = ts
                if obj.get("type") == "user":
                    n_user += 1
        rows.append(
            {
                "file": fname,
                "bytes": os.path.getsize(path),
                "sha256": h.hexdigest(),
                "first_ts": first_ts or "-",
                "last_ts": last_ts or "-",
                "n_user_lines": n_user,
                "note": "bridge-session stub (no turns)" if fname.startswith(STUB) else "",
            }
        )

    man = []
    man.append("# D-13 transcript deposit — manifest (PREPARED, NOT DEPOSITED)")
    man.append("")
    man.append("Generated by `scripts/collab_deposit_prep.py` on 2026-06-07.")
    man.append("")
    man.append(f"Corpus: {len(corpus)} files (the D-13 set: 34 substantive transcripts plus one")
    man.append("149-byte bridge-session stub). The session that executed the todo/032 analysis")
    man.append(f"({EXECUTING_SESSION}.jsonl) post-dates D-13 ratification and is")
    man.append("EXCLUDED here; if it is to be deposited too, it must be hashed after it ends.")
    man.append("")
    total = sum(r["bytes"] for r in rows)
    man.append(f"Total size: {total:,} bytes ({total / 1e6:.1f} MB).")
    man.append("")
    man.append("| file | bytes | sha256 | first ts | last ts | user lines | note |")
    man.append("|---|---|---|---|---|---|---|")
    for r in rows:
        man.append(
            f"| {r['file']} | {r['bytes']:,} | `{r['sha256']}` | {r['first_ts'][:19]} | {r['last_ts'][:19]} | {r['n_user_lines']} | {r['note']} |"
        )
    man.append("")
    man.append("Re-verify any file with:")
    man.append("```")
    man.append('Get-FileHash -Algorithm SHA256 "<path>"')
    man.append("```")
    with open(os.path.join(OUT_DIR, "deposit-manifest.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(man) + "\n")

    # --- sensitive scan ---
    rep = []
    rep.append("# D-13 transcript deposit — sensitive-content scan (FOR REVIEW)")
    rep.append("")
    rep.append("Generated by `scripts/collab_deposit_prep.py` on 2026-06-07. Matched strings are")
    rep.append("masked in this report. Severity: HIGH = likely credential, resolve before any")
    rep.append("deposit; MEDIUM = identifying but expected provenance (author identity, local")
    rep.append("paths); LOW = informational / probable false positive. Per D-13, any redaction")
    rep.append("of the deposited files must itself be logged.")
    rep.append("")
    agg = {}
    per_file = {}
    supp_agg = {}
    for fname in corpus:
        hits, supp = scan_file(os.path.join(TRANSCRIPT_DIR, fname))
        if hits:
            per_file[fname] = hits
            for label, info in hits.items():
                if label not in agg:
                    agg[label] = {"severity": info["severity"], "count": 0, "files": 0}
                agg[label]["count"] += info["count"]
                agg[label]["files"] += 1
        for k, v in supp.items():
            supp_agg[k] = supp_agg.get(k, 0) + v
    rep.append("## Summary")
    rep.append("")
    rep.append("| pattern | severity | total matches | files affected |")
    rep.append("|---|---|---|---|")
    sev_rank = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    for label in sorted(agg, key=lambda k: (sev_rank[agg[k]["severity"]], -agg[k]["count"])):
        a = agg[label]
        rep.append(f"| {label} | {a['severity']} | {a['count']:,} | {a['files']} |")
    rep.append("")
    rep.append("## Per-file detail (HIGH and MEDIUM keyword hits only; examples masked)")
    rep.append("")
    for fname in corpus:
        hits = per_file.get(fname, {})
        detail = {
            k: v
            for k, v in hits.items()
            if v["severity"] == "HIGH"
            or k in ("financial/identity keyword", "health keyword")
        }
        if not detail:
            continue
        rep.append(f"### {fname}")
        rep.append("")
        for label, info in detail.items():
            rep.append(f"- **{label}** ({info['severity']}, {info['count']} match(es)):")
            for ex in info["examples"]:
                rep.append(f"  - `...{ex}`")
        rep.append("")
    if not any(
        v["severity"] == "HIGH" for hits in per_file.values() for v in hits.values()
    ):
        rep.append("_No HIGH-severity (credential-shaped) matches survive suppression._")
        rep.append("")
    if supp_agg:
        rep.append("## Suppressed matches (counted, never silent)")
        rep.append("")
        rep.append("| pattern [suppression reason] | matches suppressed |")
        rep.append("|---|---|")
        for k in sorted(supp_agg):
            rep.append(f"| {k} | {supp_agg[k]:,} |")
        rep.append("")
    rep.append("## Analyst classification (manual review, 2026-06-07)")
    rep.append("")
    rep.append("The first scan pass (before the suppression rules above were added) raised")
    rep.append("four HIGH-severity match groups. Each was inspected in full context and")
    rep.append("classified; the suppression rules encode exactly these findings:")
    rep.append("")
    rep.append("1. `api_key assignment` (2 matches, 424fd178): the matched text is")
    rep.append("   `api_key = get_zotero_api_key` — a tool result quoting source code of")
    rep.append("   `scripts/` helpers; a function call, not a literal credential.")
    rep.append("2. `Google API key` (2 matches, 5ee18e70 + 63b28d6e): `AIza...`-shaped")
    rep.append("   substrings inside >=60-char base64 runs (embedded blob content);")
    rep.append("   random collisions, not keys.")
    rep.append("3. `financial/identity keyword` (5 matches, 2 files): four are quotations of")
    rep.append("   Rubin (1987), preface — the United States Social Security Administration in")
    rep.append("   the historical account of multiple imputation's origin; one is `/SSN+`")
    rep.append("   inside a base64 run. None is personal financial information.")
    rep.append("4. An earlier `health keyword` pattern that included `diagnos*` produced")
    rep.append("   ~13,000 matches, all statistical ('diagnostic', 'diagnose the bug').")
    rep.append("   The pattern was narrowed to clinical terms. All 34 surviving matches were")
    rep.append("   then inspected individually: every one is quoted methodology literature")
    rep.append("   (the fluvoxamine worked example; the UK700 psychiatric-case-management")
    rep.append("   trial in a variable-selection paper; NHANES lipid-lowering-medication")
    rep.append("   rates) or the word 'prescription' used rhetorically or mathematically.")
    rep.append("   No personal health information is present.")
    rep.append("")
    rep.append("Remaining MEDIUM categories are expected provenance, present by design of")
    rep.append("D-13 (the author is identified; local paths identify the machine layout):")
    rep.append("")
    rep.append("- Local Windows paths with the username `marcu` appear throughout (~35k")
    rep.append("  matches): tool calls, file listings, configuration. Removing them would")
    rep.append("  gut the record; D-13 anticipated path exposure. Recommend: deposit as-is.")
    rep.append("- Email addresses (~300 matches): predominantly the author's own git/Zotero")
    rep.append("  identities and emails quoted from acquired papers' title pages.")
    rep.append("  Recommend: deposit as-is; the author identity is public per JAIGP norms.")
    rep.append("")
    rep.append("No redaction is recommended by this scan. If Marcus elects any redaction,")
    rep.append("it must be logged per D-13 (file, byte range, reason, replacement).")
    rep.append("")
    with open(os.path.join(OUT_DIR, "deposit-sensitive-scan.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(rep) + "\n")

    print(f"manifest: {len(corpus)} files, {total / 1e6:.1f} MB")
    print("scan summary:")
    for label in sorted(agg, key=lambda k: (sev_rank[agg[k]["severity"]], -agg[k]["count"])):
        a = agg[label]
        print(f"  [{a['severity']}] {label}: {a['count']:,} matches in {a['files']} files")


if __name__ == "__main__":
    main()
