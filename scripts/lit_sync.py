#!/usr/bin/env python3
"""
lit-sync: bridge from Better BibTeX export to mi-spectral/literature/<citekey>.md.

For each entry in literature/mi-spectral-better-bibTeX.bib:
  1. Use the BBT citekey from the entry header (`@type{citekey,`).
  2. Find the migrated PDF in Google Drive/Literature/MI-SPECTRAL/ via direct
     `<citekey>.pdf` match first, then a (firstauthor-surname, year) heuristic.
  3. SHA-256 the PDF, look up the cached Mathpix conversion at
     Google Drive/Literature/.litrev/mathpix_cache/<sha256>.md.
  4. If literature/<citekey>.md already exists with a matching pdf_sha256 in
     its YAML frontmatter, skip. Otherwise write frontmatter + cached markdown.

After processing, scan mi-spectral/manuscript/ for `@citekey` tokens and warn
if any reference a key we haven't synced (the PreToolUse hook enforces at edit
time; this is just a courtesy check).

Idempotent. Re-runs are no-ops when nothing has changed.

Pre-reqs:
  - Better BibTeX export saved to literature/mi-spectral-better-bibTeX.bib
    (in Zotero: right-click mi-spectral collection -> Export Collection
    -> Better BibTeX -> save to the literature/ folder)
  - migrate_zotero_attachments has put PDFs in MI-SPECTRAL/ drive folder
  - index_papers.py has been run (populates the Mathpix cache)
"""

import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import bibtexparser
from bibtexparser.bparser import BibTexParser

PROJECT_ROOT = Path(r"C:\Users\marcu\git-repositories\mi-spectral")
LITERATURE_DIR = PROJECT_ROOT / "literature"
MANUSCRIPT_DIR = PROJECT_ROOT / "manuscript"
BIB_FILE = LITERATURE_DIR / "mi-spectral-better-bibTeX.bib"
DRIVE_PROJECT_DIR = Path(r"C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL")
MATHPIX_CACHE = Path(r"C:\Users\marcu\Google Drive\Literature\.litrev\mathpix_cache")

INVALID_CITEKEY_RE = re.compile(r"[^A-Za-z0-9_:\-]")


def parse_bib(path: Path) -> list[dict]:
    """Parse the BBT export. Returns a list of entries (dicts)."""
    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    with path.open("r", encoding="utf-8") as f:
        db = bibtexparser.load(f, parser=parser)
    return db.entries


def first_author_surname(entry: dict) -> Optional[str]:
    """Extract first author's surname (lowercased) from a BibTeX `author` field."""
    raw = entry.get("author", "")
    if not raw:
        return None
    # BibTeX joins authors with ' and '. First author's name is before the first ' and '.
    first = raw.split(" and ")[0].strip()
    # "Last, First" form
    if "," in first:
        surname = first.split(",", 1)[0].strip()
    else:
        # "First Last" form - take last whitespace-separated token
        surname = first.split()[-1] if first.split() else ""
    return surname.lower().strip("{}") or None


def year_from_entry(entry: dict) -> str:
    year = entry.get("year", "")
    m = re.search(r"\b(\d{4})\b", str(year))
    return m.group(1) if m else ""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _citekey_words(citekey: str) -> list[str]:
    """Extract the title-distinctive words from a BBT citekey.

    BBT citekey format: <firstauthor[+coauthors]><Word1Word2Word3...><year>[a-z]?
    Splitting on capital letters recovers the lowercased word list. This is more
    reliable for disambiguating PDFs in snake_case folders than the raw title
    field, because BBT picks distinctive words (skipping stopwords like "of",
    "and", "the"), whereas title.split()[:3] often includes them.
    """
    # Strip trailing 4-digit year + optional disambiguator suffix
    m = re.match(r"^(.+?)(\d{4})[a-z]?$", citekey)
    if not m:
        return [citekey.lower()]
    body = m.group(1)
    # Split on capital letter boundaries; lowercase the result
    parts = re.findall(r"[A-Z]+[a-z]*|[a-z]+", body)
    return [p.lower() for p in parts if p]


def _score_candidate(pdf: Path, words: list[str]) -> int:
    """How many words from `words` appear in pdf.stem (case-insensitive)."""
    stem = pdf.stem.lower()
    return sum(1 for w in words if w in stem)


def find_pdf_in_drive(entry: dict, drive_dir: Path, citekey: str) -> Optional[Path]:
    # Pass 0: direct citekey.pdf match (handles items named after BBT keys)
    direct = drive_dir / f"{citekey}.pdf"
    if direct.exists():
        return direct

    surname = first_author_surname(entry)
    year = year_from_entry(entry)
    if not surname:
        return None

    # Citekey-derived word list for disambiguation (more distinctive than raw title)
    ck_words = _citekey_words(citekey)

    def best_match(candidates: list[Path]) -> Optional[Path]:
        if not candidates:
            return None
        if len(candidates) == 1:
            return candidates[0]
        # Score each candidate by citekey-word overlap; return the unique max
        scored = [(_score_candidate(p, ck_words), p) for p in candidates]
        scored.sort(key=lambda t: (-t[0], t[1].name))
        top_score = scored[0][0]
        top = [p for s, p in scored if s == top_score]
        if len(top) == 1:
            return top[0]
        # Still tied — fall back to raw title-word match
        title = (entry.get("title", "") or "").lower()
        title_words = re.findall(r"[a-z]+", title)[:3]
        for pdf in top:
            if all(w in pdf.stem.lower() for w in title_words):
                return pdf
        return top[0]

    # Pass 1: surname + year both in filename
    if year:
        cands = [p for p in drive_dir.glob("*.pdf")
                 if surname in p.stem.lower() and year in p.stem.lower()]
        if cands:
            return best_match(cands)

    # Pass 2: surname only (for year-mismatch cases like petersen2008matrix.pdf w/ year 2012)
    cands = [p for p in drive_dir.glob("*.pdf") if surname in p.stem.lower()]
    return best_match(cands)


def get_existing_pdf_hash(lit_path: Path) -> Optional[str]:
    if not lit_path.exists():
        return None
    try:
        text = lit_path.read_text(encoding="utf-8")
    except Exception:
        return None
    m = re.search(r"^pdf_sha256:\s*([0-9a-f]{64})\s*$", text, re.MULTILINE)
    return m.group(1) if m else None


def yaml_escape(value: str) -> str:
    if value is None:
        return ""
    value = str(value)
    if any(c in value for c in ":#@&*!|>'\"%`{}[],") or value.strip() != value or not value:
        return "'" + value.replace("'", "''") + "'"
    return value


def clean_braces(s: str) -> str:
    """BibTeX double-braced fields - strip outer braces for display."""
    if not s:
        return ""
    return re.sub(r"\{([^{}]*)\}", r"\1", s)


def build_frontmatter(entry: dict, citekey: str, pdf_path: Path, pdf_hash: str) -> str:
    lines = ["---"]
    lines.append(f"citekey: {yaml_escape(citekey)}")
    lines.append(f"item_type: {yaml_escape(entry.get('ENTRYTYPE', ''))}")
    lines.append(f"authors: {yaml_escape(clean_braces(entry.get('author', '')))}")
    lines.append(f"year: {yaml_escape(year_from_entry(entry))}")
    lines.append(f"title: {yaml_escape(clean_braces(entry.get('title', '')))}")
    for src, dst in [
        ("journal", "venue"),
        ("booktitle", "venue"),
        ("publisher", "publisher"),
        ("volume", "volume"),
        ("number", "issue"),
        ("pages", "pages"),
        ("doi", "doi"),
        ("isbn", "isbn"),
        ("eprint", "eprint"),
        ("series", "series"),
        ("edition", "edition"),
    ]:
        v = entry.get(src)
        if v:
            lines.append(f"{dst}: {yaml_escape(clean_braces(str(v)))}")
    lines.append(f"source_pdf: {yaml_escape(str(pdf_path))}")
    lines.append(f"pdf_sha256: {pdf_hash}")
    lines.append("converted_via: mcp__litrev__convert_pdf (Mathpix)")
    lines.append(f"last_synced: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def scan_manuscript_for_cites(manuscript_dir: Path) -> set:
    cites = set()
    if not manuscript_dir.exists():
        return cites
    # Pandoc cite syntax: @key preceded by whitespace/[/(/;/-/line start (not by a word char like in emails)
    pattern = re.compile(r"(?<!\w)@(?!TODO:)([A-Za-z][A-Za-z0-9_:\-]+)")
    for ext in ("qmd", "md", "tex", "rmd"):
        for f in manuscript_dir.rglob(f"*.{ext}"):
            try:
                content = f.read_text(encoding="utf-8")
            except Exception:
                continue
            cites.update(pattern.findall(content))
    return cites


def main():
    LITERATURE_DIR.mkdir(parents=True, exist_ok=True)

    if not BIB_FILE.exists():
        print(f"ERROR: BibTeX export not found at {BIB_FILE}", file=sys.stderr)
        print("In Zotero: right-click `mi-spectral` collection -> Export Collection ->", file=sys.stderr)
        print("           Better BibTeX -> save to the literature/ folder with that filename.", file=sys.stderr)
        sys.exit(1)

    print(f"lit-sync: {BIB_FILE.name} -> {LITERATURE_DIR}")
    print(f"  PDFs:          {DRIVE_PROJECT_DIR}")
    print(f"  Mathpix cache: {MATHPIX_CACHE}")
    print()

    entries = parse_bib(BIB_FILE)
    print(f"Parsed {len(entries)} entries from BBT export")
    print()

    written, uptodate = [], []
    bad_citekey, no_pdf, no_cache = [], [], []

    for entry in entries:
        citekey = entry.get("ID", "")
        title = (entry.get("title", "") or "")[:60]

        # 1. Validate citekey
        if INVALID_CITEKEY_RE.search(citekey):
            bad_chars = set(INVALID_CITEKEY_RE.findall(citekey))
            print(f"  [{citekey}] {title}")
            print(f"    SKIP: citekey has invalid characters {sorted(bad_chars)} - fix the underlying Zotero entry.")
            bad_citekey.append(citekey)
            continue

        # 2. Find PDF
        pdf = find_pdf_in_drive(entry, DRIVE_PROJECT_DIR, citekey)
        if not pdf:
            print(f"  [{citekey}] {title}")
            print(f"    SKIP: PDF not found in {DRIVE_PROJECT_DIR.name}/")
            no_pdf.append(citekey)
            continue

        # 3. Hash PDF
        pdf_hash = sha256_file(pdf)

        # 4. Idempotency
        lit_path = LITERATURE_DIR / f"{citekey}.md"
        if get_existing_pdf_hash(lit_path) == pdf_hash:
            print(f"  [{citekey}] up-to-date")
            uptodate.append(citekey)
            continue

        # 5. Mathpix cache lookup
        cache_path = MATHPIX_CACHE / f"{pdf_hash}.md"
        if not cache_path.exists():
            print(f"  [{citekey}] {title}")
            print(f"    SKIP: Mathpix cache miss ({pdf_hash[:12]}...). Run index_papers.py.")
            no_cache.append(citekey)
            continue

        # 6. Write
        markdown = cache_path.read_text(encoding="utf-8")
        frontmatter = build_frontmatter(entry, citekey, pdf, pdf_hash)
        lit_path.write_text(frontmatter + markdown, encoding="utf-8")
        print(f"  [{citekey}] wrote {lit_path.name} ({len(markdown):,} chars)")
        written.append(citekey)

    print()
    print("=" * 60)
    print(f"Wrote:                    {len(written)}")
    print(f"Already up-to-date:       {len(uptodate)}")
    print(f"Skipped (bad citekey):    {len(bad_citekey)}")
    print(f"Skipped (no PDF):         {len(no_pdf)}")
    print(f"Skipped (no cache):       {len(no_cache)}")

    if bad_citekey:
        print()
        print("Citekeys with invalid characters (fix in Zotero, then re-export BBT):")
        for k in bad_citekey:
            print(f"  - {k!r}")

    if no_pdf:
        print()
        print("Entries with no matching PDF in the drive folder:")
        for k in no_pdf:
            print(f"  - {k}")

    if no_cache:
        print()
        print("Entries with PDF but no Mathpix cache (run `py index_papers.py` first):")
        for k in no_cache:
            print(f"  - {k}")

    # Manuscript cite check
    cites = scan_manuscript_for_cites(MANUSCRIPT_DIR)
    if cites:
        synced = set(written) | set(uptodate)
        unmatched = cites - synced
        if unmatched:
            print()
            print("WARNING: manuscript/ references citekeys not synced:")
            for c in sorted(unmatched):
                print(f"  @{c}")
            print("(The PreToolUse hook is what enforces this at edit time.)")


if __name__ == "__main__":
    main()
