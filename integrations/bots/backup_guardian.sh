#!/bin/bash
# 🛡️ JARVIS Super Guardian - Backup & Restore System
# Creator: Daniswara x Copilot

set -e

# === Konfigurasi Direktori ===
PROJECT_DIR="$HOME/OneDrive/Desktop/AGUNG DATABASE/JARVIS"
BACKUP_DIR="$PROJECT_DIR/.jarvis_restore"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
BACKUP_PATH="$BACKUP_DIR/backup-$TIMESTAMP"
LOG_FILE="$BACKUP_DIR/guardian-log.txt"

# === File Penting untuk Proteksi ===
PROTECTED=(
  "config/secrets.py"
  "control/harmony/quota_policy_engine.py"
  "integrations/bots/safePullRebase.sh"
  "main.py"
)

# === Fungsi Backup Otomatis ===
backup() {
  echo "🔐 Membuat backup di $BACKUP_PATH..."
  mkdir -p "$BACKUP_PATH"
  for file in "${PROTECTED[@]}"; do
    cp --parents "$PROJECT_DIR/$file" "$BACKUP_PATH"
  done
  echo "$(date +"%Y-%m-%d %H:%M:%S") ✅ Backup selesai di $BACKUP_PATH" | tee -a "$LOG_FILE"
}

# === Fungsi Restore Otomatis ===
restore() {
  latest=$(ls -td "$BACKUP_DIR"/backup-* | head -1)
  echo "🧬 Restore dari $latest..."
  cp -r "$latest"/* "$PROJECT_DIR"
  echo "$(date +"%Y-%m-%d %H:%M:%S") ✅ Sistem JARVIS dipulihkan ke versi sebelumnya." | tee -a "$LOG_FILE"
}

# === Monitoring File Integrity ===
checksum() {
  echo "🔎 Checksum file..."
  for file in "${PROTECTED[@]}"; do
    full_path="$PROJECT_DIR/$file"
    if [ -f "$full_path" ]; then
      sha256sum "$full_path"
    else
      echo "⚠️ File hilang: $file"
    fi
  done | tee -a "$LOG_FILE"
}

# === Menu Eksekusi ===
case "$1" in
  backup)
    backup
    ;;
  restore)
    restore
    ;;
  checksum)
    checksum
    ;;
  *)
    echo "📘 Penggunaan: $0 {backup|restore|checksum}"
    exit 1
    ;;
esac
