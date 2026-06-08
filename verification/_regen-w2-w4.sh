#!/usr/bin/env bash
# Pre-submission regeneration of W2 + W4 (not in the 2026-06-07 gate; receipt notes it).
# Runs sequentially so the 20-core PSOCK cluster is never oversubscribed.
# Snapshots the committed (git-tracked) caches first, then diffs after each run.
set -u
cd "$(dirname "$0")/.."   # repo root
RSCRIPT="/c/Program Files/R/R-4.5.1/bin/Rscript.exe"
SNAP="verification/cache/_regen-snapshot-20260607"
LOG="verification/cache/regen-w2-w4-runlog.txt"
mkdir -p "$SNAP"

echo "=== W2+W4 regen started $(date -u +%Y-%m-%dT%H:%M:%SZ) ===" | tee "$LOG"

# --- snapshot committed evidence-of-record (figure inputs) ---
cp verification/cache/W2-prod-amelia.rds        "$SNAP/" 2>/dev/null
cp verification/cache/w4-nonnested-summary.csv  "$SNAP/" 2>/dev/null
cp verification/cache/w4-dissimilar-summary.csv "$SNAP/" 2>/dev/null
echo "snapshot written to $SNAP" | tee -a "$LOG"

run () {  # $1 = label, rest = command
  local label="$1"; shift
  echo "" | tee -a "$LOG"
  echo "--- $label  start $(date -u +%H:%M:%SZ) ---" | tee -a "$LOG"
  "$@" >> "$LOG" 2>&1
  local rc=$?
  echo "--- $label  end   $(date -u +%H:%M:%SZ)  exit=$rc ---" | tee -a "$LOG"
  return $rc
}

run "W2 prod amelia"      "$RSCRIPT" verification/W2-lrt-power.R prod amelia 20
run "W4 nonnested R=20000" "$RSCRIPT" verification/w4-nonnested-vuong.R 20000 20
run "W4 dissimilar R=20000" "$RSCRIPT" verification/w4-dissimilar-vuong.R 20000 20

# --- diff regenerated vs committed snapshot ---
echo "" | tee -a "$LOG"
echo "=== DIFF vs committed snapshot ===" | tee -a "$LOG"
for f in w4-nonnested-summary.csv w4-dissimilar-summary.csv; do
  if diff -q "$SNAP/$f" "verification/cache/$f" >/dev/null 2>&1; then
    echo "$f: BYTE-IDENTICAL" | tee -a "$LOG"
  else
    echo "$f: DIFFERS (see git diff)" | tee -a "$LOG"
  fi
done
# W2 rds: compare via R (RDS bytes can differ on metadata; compare the stored content)
"$RSCRIPT" -e '
  a <- readRDS("verification/cache/_regen-snapshot-20260607/W2-prod-amelia.rds")
  b <- readRDS("verification/cache/W2-prod-amelia.rds")
  cat("W2 identical():", identical(a, b), "\n")
' >> "$LOG" 2>&1

echo "" | tee -a "$LOG"
echo "=== W2+W4 regen finished $(date -u +%Y-%m-%dT%H:%M:%SZ) ===" | tee -a "$LOG"
