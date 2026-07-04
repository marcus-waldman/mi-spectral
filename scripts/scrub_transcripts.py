#!/usr/bin/env python3
"""
scrub_transcripts.py — redact secrets and personal identifiers from Claude Code
session transcripts (or any text dump) before publishing them for provenance.

Design goals
------------
* Safe by default: DRY RUN unless you pass --apply. Nothing is written until you
  have seen the report.
* No personal data lives in this file. The Windows username is read from the
  environment; your personal email is caught by a generic free-mail-domain rule.
  So this script is safe to commit to a public repo and reuse on future projects.
* Two modes:
  - COPY (recommended): pass --out-dir to write a redacted COPY to a new folder
    and leave the original raw transcripts untouched. Text files are redacted;
    everything else is copied verbatim, so the output is a complete, publishable
    mirror. This is the safe default workflow — publish the copy, keep the raw.
  - IN-PLACE: with no --out-dir, files are overwritten where they sit. It NEVER
    writes a backup INTO the target folder (a *.bak of an unredacted file in a
    published folder would defeat the point); use --backup-dir (outside the
    folder) or rely on Drive version history.

What it AUTO-REDACTS (default on)
---------------------------------
1. Provider secrets (high precision): Anthropic / OpenAI / Google API keys,
   Google OAuth tokens, GitHub / GitLab tokens, AWS access-key IDs, Slack tokens,
   Bearer tokens, and PEM private-key blocks.
2. Your Windows home path: ...\\Users\\<you>\\...  ->  ...\\Users\\user\\...
   (matched only in a path context so it can never corrupt names like "marcus").
3. Personal free-mail addresses (gmail/outlook/yahoo/icloud/proton/...).
   Institutional (.edu/.org/.gov) and cited-author addresses are KEPT by default
   because they are already public and are often the legitimate contact.

Opt-in
------
  --redact-email X     also redact this exact address (repeatable)
  --redact-all-emails  redact EVERY email (will also nuke code like G@np.x — careful)
  --redact-edu         treat .edu/.ac.* addresses as personal too
  --aggressive         also redact generic  key/secret/password = <value>  assignments
                       (higher recall, can over-match legit config — review the diff)

What it CANNOT decide for you (printed in a REVIEW MANUALLY section)
-------------------------------------------------------------------
Third-party personal data, confidential/embargoed content (peer reviews,
unpublished grants), regulated data (PHI/HIPAA, FERPA), candid remarks, private
URLs with tokens, internal hostnames/IPs. The script surfaces candidates; you judge.

Usage
-----
  # preview (dry run): redacted copy of .claude -> .claude_redacted
  py scrub_transcripts.py "C:\\...\\.claude" --out-dir "C:\\...\\.claude_redacted"

  # build the redacted copy for real (source .claude is left untouched):
  py scrub_transcripts.py "C:\\...\\.claude" --out-dir "C:\\...\\.claude_redacted" --apply

  # in-place variant (overwrites the source folder):
  py scrub_transcripts.py "C:\\...\\.claude" --apply
"""

import argparse
import os
import re
import shutil
import sys

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

TEXT_EXTS = {
    ".jsonl", ".json", ".ndjson", ".md", ".markdown", ".txt", ".log",
    ".csv", ".tsv", ".yaml", ".yml", ".html", ".xml",
}
SKIP_DIRS = {".git", "__pycache__", "node_modules", "_gsdata_"}  # _gsdata_ = Google Drive recycle/sync metadata
SKIP_FILES = {"desktop.ini", "thumbs.db", ".ds_store"}            # OS/sync junk, never publish
IMAGE_DOC_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tif", ".tiff",
                  ".pdf", ".docx", ".doc", ".pptx", ".xlsx"}      # binaries that may hold PII; flag for review
MAX_MB_DEFAULT = 200  # skip files larger than this (likely binary)

FREEMAIL_DOMAINS = {
    "gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.uk", "ymail.com",
    "hotmail.com", "outlook.com", "live.com", "msn.com", "icloud.com",
    "me.com", "mac.com", "proton.me", "protonmail.com", "pm.me",
    "aol.com", "gmx.com", "zoho.com", "hey.com",
}

# (name, compiled regex). Each matched span is replaced by [REDACTED-SECRET-<name>].
# Patterns are anchored on a non-alphanumeric boundary where needed so that a
# chance substring inside a base64 blob (e.g. ...eAIza...) is NOT matched.
SECRET_PATTERNS = [
    ("anthropic",   re.compile(r"(?<![A-Za-z0-9])sk-ant-[A-Za-z0-9_\-]{20,}")),
    ("openai",      re.compile(r"(?<![A-Za-z0-9])sk-(?:proj-)?[A-Za-z0-9]{20,}")),
    ("google-api",  re.compile(r"(?<![A-Za-z0-9_])AIza[0-9A-Za-z_\-]{35}(?![A-Za-z0-9_\-])")),
    ("google-oauth",re.compile(r"ya29\.[0-9A-Za-z_\-]{20,}")),
    ("github",      re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("gitlab",      re.compile(r"\bglpat-[0-9A-Za-z_\-]{20,}\b")),
    ("aws-akid",    re.compile(r"(?<![A-Z0-9])A(?:KIA|SIA|IDA|GPA|ROA)[0-9A-Z]{16}(?![A-Z0-9])")),
    ("slack",       re.compile(r"\bxox[baprs]-[0-9A-Za-z\-]{10,}")),
    ("bearer",      re.compile(r"Bearer\s+[A-Za-z0-9._\-]{20,}")),
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----")),
]

# Opt-in (--aggressive): redact only the VALUE after a key/secret/password marker.
AGGRESSIVE_ASSIGN = re.compile(
    r"(?i)\b(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret)"
    r"(['\"]?\s*[:=]\s*['\"]?)([A-Za-z0-9/_+\-]{16,})"
)

EMAIL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")

# Detection-only (REVIEW MANUALLY) patterns:
URL_WITH_TOKEN = re.compile(
    r"https?://[^\s\"'<>]*(?:token|key|secret|sig|signature|access_token|"
    r"X-Amz-|AWSAccessKeyId|password)[^\s\"'<>]*", re.I)
IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
PHONE = re.compile(r"(?<!\d)(?:\+?\d[\d\-\s().]{8,}\d)(?!\d)")
WIN_USERHOME = re.compile(r"[Uu]sers[\\/]+([A-Za-z0-9._\-]+)")

PRIVATE_IP = re.compile(r"^(?:10\.|127\.|192\.168\.|169\.254\.|172\.(?:1[6-9]|2\d|3[01])\.|0\.|255\.)")


def build_home_pattern(username: str) -> re.Pattern:
    """Match the username only when it directly follows a path marker
    (Users\\, Users/, Users-), and is not followed by an alphanumeric — so
    'marcu' is replaced but 'marcus' / 'marcus.waldman' never is."""
    u = re.escape(username)
    return re.compile(r"(Users[\\/]+|Users-)" + u + r"(?![A-Za-z0-9])")


def iter_files(root, self_path, skip_realpath=None):
    """Yield every file under root, skipping VCS dirs, this script, and an
    optional nested directory (e.g. the output dir, so we never recurse into it)."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIRS
            and (skip_realpath is None
                 or os.path.realpath(os.path.join(dirpath, d)) != skip_realpath)
        ]
        for fn in filenames:
            if fn.lower() in SKIP_FILES:
                continue
            p = os.path.join(dirpath, fn)
            if os.path.abspath(p) == os.path.abspath(self_path):
                continue
            yield p


def classify(path, max_mb):
    """'text' (redact it), 'binary' (copy verbatim), or 'oversize' (copy, don't read)."""
    ext = os.path.splitext(path)[1].lower()
    try:
        if os.path.getsize(path) > max_mb * 1024 * 1024:
            return "oversize"
    except OSError:
        return "binary"
    if ext and ext not in TEXT_EXTS:
        return "binary"
    return "text"  # known text ext, or no ext (confirmed by utf-8 read at use site)


def email_is_personal(addr, redact_all, redact_edu, extra, keep):
    low = addr.lower()
    if low in (k.lower() for k in keep):
        return False
    if low in (e.lower() for e in extra):
        return True
    if redact_all:
        return True
    domain = low.rsplit("@", 1)[-1]
    if domain in FREEMAIL_DOMAINS:
        return True
    if redact_edu and (domain.endswith(".edu") or ".ac." in domain):
        return True
    return False


def scrub_text(text, opts):
    counts = {}

    def bump(k, n):
        if n:
            counts[k] = counts.get(k, 0) + n

    if not opts.no_secrets:
        for name, rx in SECRET_PATTERNS:
            text, n = rx.subn(f"[REDACTED-SECRET-{name}]", text)
            bump(f"secret:{name}", n)

    if opts.aggressive:
        text, n = AGGRESSIVE_ASSIGN.subn(r"\1\2[REDACTED-SECRET]", text)
        bump("secret:assignment", n)

    if not opts.no_paths and opts.home_pat is not None:
        text, n = opts.home_pat.subn(r"\1" + opts.home_replacement, text)
        bump("path:username", n)

    if not opts.no_emails:
        def repl_email(m):
            addr = m.group(0)
            if email_is_personal(addr, opts.redact_all_emails, opts.redact_edu,
                                 opts.redact_email, opts.keep_email):
                repl_email.n += 1
                return "[redacted-email]"
            return addr
        repl_email.n = 0
        text = EMAIL.sub(repl_email, text)
        bump("email:personal", repl_email.n)

    return text, counts


def flag_text(text, flags, username):
    for addr in set(EMAIL.findall(text)):
        # skip obvious code false-positives like  G@np.linalg.inv
        if re.search(r"\.(?:py|js|R|inv|array|diag|normal|randn|cholesky)$", addr):
            continue
        flags["emails"].add(addr)
    for u in WIN_USERHOME.findall(text):
        if u.lower() != username.lower() and u.lower() not in ("user", "public", "default", "all users"):
            flags["other_usernames"].add(u)
    for url in URL_WITH_TOKEN.findall(text):
        flags["token_urls"].add(url[:120])
    for ip in IPV4.findall(text):
        if not PRIVATE_IP.match(ip) and ip not in ("0.0.0.0",):
            flags["public_ips"].add(ip)
    for ph in PHONE.findall(text):
        digits = re.sub(r"\D", "", ph)
        if 9 <= len(digits) <= 15:
            flags["phone_like"].add(ph.strip())


def main():
    ap = argparse.ArgumentParser(description="Redact secrets/PII from transcripts (dry-run by default).")
    ap.add_argument("directory", nargs="?", default=".", help="source folder to scan (default: current dir)")
    ap.add_argument("--out-dir", default=None,
                    help="write a redacted COPY here instead of editing in place; the source is "
                         "never modified (text files redacted, other files copied verbatim)")
    ap.add_argument("--force", action="store_true", help="allow writing into an existing, non-empty --out-dir")
    ap.add_argument("--skip-binaries", action="store_true",
                    help="in --out-dir mode, do NOT copy non-text files (images/PDFs/etc.); they can't be scrubbed")
    ap.add_argument("--apply", action="store_true", help="actually write (in-place overwrite, or build --out-dir); otherwise dry run")
    ap.add_argument("--username", default=os.environ.get("USERNAME") or os.environ.get("USER") or "",
                    help="Windows account name to scrub from paths (default: from environment)")
    ap.add_argument("--home-replacement", default="user", help="replacement for the username (default: user)")
    ap.add_argument("--redact-email", action="append", default=[], metavar="ADDR",
                    help="also redact this exact email (repeatable)")
    ap.add_argument("--keep-email", action="append", default=[], metavar="ADDR",
                    help="never redact this email (repeatable)")
    ap.add_argument("--redact-all-emails", action="store_true", help="redact every email address")
    ap.add_argument("--redact-edu", action="store_true", help="also treat .edu/.ac.* as personal")
    ap.add_argument("--aggressive", action="store_true", help="also redact generic key/secret/password=VALUE")
    ap.add_argument("--no-secrets", action="store_true", help="skip secret redaction")
    ap.add_argument("--no-paths", action="store_true", help="skip username/path scrub")
    ap.add_argument("--no-emails", action="store_true", help="skip email redaction")
    ap.add_argument("--backup-dir", default=None, help="mirror originals here BEFORE overwriting (keep OUTSIDE the target)")
    ap.add_argument("--max-mb", type=int, default=MAX_MB_DEFAULT, help=f"skip files larger than this (default {MAX_MB_DEFAULT})")
    opts = ap.parse_args()

    root = os.path.abspath(opts.directory)
    if not os.path.isdir(root):
        sys.exit(f"error: not a directory: {root}")
    if opts.backup_dir and os.path.abspath(opts.backup_dir).startswith(root):
        sys.exit("error: --backup-dir must be OUTSIDE the target directory (else originals get published)")

    out_dir = os.path.abspath(opts.out_dir) if opts.out_dir else None
    if out_dir:
        if out_dir == root or out_dir.startswith(root + os.sep) or root.startswith(out_dir + os.sep):
            sys.exit("error: --out-dir must be a sibling of the source (not inside it or containing it)")
        if os.path.isdir(out_dir) and os.listdir(out_dir) and not opts.force:
            sys.exit(f"error: {out_dir} exists and is not empty; pass --force to write into it")

    opts.home_pat = build_home_pattern(opts.username) if opts.username else None
    if not opts.no_paths and not opts.username:
        print("warning: no username detected; path scrub disabled (pass --username)", file=sys.stderr)

    self_path = os.path.abspath(__file__)
    total_counts = {}
    flags = {"emails": set(), "other_usernames": set(), "token_urls": set(),
             "public_ips": set(), "phone_like": set(), "binaries": set()}
    files_scanned = files_changed = files_copied = files_skipped = 0

    if out_dir:
        print(f"COPY mode: source stays untouched; redacted copy -> {out_dir}\n")

    for p in iter_files(root, self_path, skip_realpath=out_dir):
        kind = classify(p, opts.max_mb)
        rel = os.path.relpath(p, root)
        dest = os.path.join(out_dir, rel) if out_dir else None

        if kind == "text":
            try:
                with open(p, "r", encoding="utf-8", newline="") as f:
                    original = f.read()
            except (UnicodeDecodeError, OSError):
                kind = "binary"  # not really text; fall through to copy/skip below
            else:
                files_scanned += 1
                flag_text(original, flags, opts.username)
                scrubbed, counts = scrub_text(original, opts)
                for k, v in counts.items():
                    total_counts[k] = total_counts.get(k, 0) + v
                changed = scrubbed != original
                if changed:
                    files_changed += 1
                    hits = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
                    verb = "WOULD REDACT" if not opts.apply else "REDACTED"
                    print(f"  {verb}: {rel}  [{hits}]")
                if opts.apply:
                    if out_dir:                       # always write the copy, changed or not
                        os.makedirs(os.path.dirname(dest), exist_ok=True)
                        with open(dest, "w", encoding="utf-8", newline="") as f:
                            f.write(scrubbed)
                    elif changed:                     # in-place: only rewrite changed files
                        if opts.backup_dir:
                            bdst = os.path.join(opts.backup_dir, rel)
                            os.makedirs(os.path.dirname(bdst), exist_ok=True)
                            with open(bdst, "w", encoding="utf-8", newline="") as bf:
                                bf.write(original)
                        with open(p, "w", encoding="utf-8", newline="") as f:
                            f.write(scrubbed)

        if kind in ("binary", "oversize") and out_dir:
            ext = os.path.splitext(p)[1].lower()
            if ext in IMAGE_DOC_EXTS:                 # content we can't scrub -> flag for review
                flags["binaries"].add(rel)
            if opts.skip_binaries:
                files_skipped += 1
                continue
            files_copied += 1                         # copy verbatim into the mirror
            if opts.apply:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy2(p, dest)

    # ---- summary ----
    print("\n" + "=" * 70)
    print(f"Scanned {files_scanned} text files under {root}")
    if out_dir:
        print(f"{'Would write' if not opts.apply else 'Wrote'} {files_scanned} text + "
              f"{files_copied} other files to {out_dir} ({files_changed} redacted"
              + (f"; {files_skipped} binaries skipped" if files_skipped else "") + ").")
    else:
        print(f"{'Would change' if not opts.apply else 'Changed'} {files_changed} files in place.")
    if total_counts:
        print("\nRedactions by category:")
        for k, v in sorted(total_counts.items()):
            print(f"  {k:28s} {v}")
    else:
        print("No redactions matched.")

    # ---- review-manually section (detection only) ----
    print("\n" + "-" * 70)
    print("REVIEW MANUALLY (not auto-redacted — your judgment):")
    def show(title, s, limit=40):
        s = sorted(s)
        print(f"\n  {title} ({len(s)}):")
        for x in s[:limit]:
            print(f"    - {x}")
        if len(s) > limit:
            print(f"    ... and {len(s) - limit} more")
    bin_title = ("Images/PDFs copied verbatim — CANNOT be scrubbed, open each"
                 if not opts.skip_binaries else "Images/PDFs found (skipped, not copied)")
    show(bin_title, flags["binaries"])
    show("Distinct emails kept (verify none are private/third-party)", flags["emails"])
    show("Other Windows usernames in paths", flags["other_usernames"])
    show("URLs containing token/key/signature", flags["token_urls"])
    show("Public IP addresses", flags["public_ips"])
    show("Phone-like number strings", flags["phone_like"])
    print("\n  Also check by hand (no pattern catches these):")
    print("    - third-party personal data (collaborators, students, patients)")
    print("    - confidential/embargoed content (peer reviews, unpublished grants, others' data)")
    print("    - regulated data (PHI/HIPAA, FERPA), candid remarks about people/venues")
    print("    - content that leaked in from OTHER projects")

    if not opts.apply:
        target = f"build {out_dir}" if out_dir else "overwrite in place"
        print(f"\n>>> DRY RUN — nothing written. Re-run with --apply to {target}. <<<")
    print("=" * 70)


if __name__ == "__main__":
    main()
