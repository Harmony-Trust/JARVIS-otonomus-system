safePullRebase.sh
#!/bin/bash

set -e

echo "🚀 Starting safePullRebase.sh"

# Pastikan berada di root repo
cd "$(git rev-parse --show-toplevel)"

# Hapus index.lock kalau ada
if [ -f .git/index.lock ]; then
  echo "⚠️ Menghapus index.lock yang tertinggal..."
  rm -f .git/index.lock
fi

# Cek perubahan
CHANGES=$(git status --porcelain)
if [ -n "$CHANGES" ]; then
  echo "🔍 Ada perubahan lokal."

  # Coba commit dulu
  git add .
  if git diff --cached --quiet; then
    echo "🗃️ Tidak ada perubahan yang cukup untuk di-commit. Melakukan stash..."
    git stash push -m "Auto stash before rebase"
    STASHED=true
  else
    git commit -m "Auto commit sebelum rebase"
    STASHED=false
  fi
else
  echo "✅ Tidak ada perubahan lokal."
  STASHED=false
fi

# Pull dengan rebase
echo "📡 Menarik perubahan dari remote..."
if git pull --rebase origin main; then
  echo "✅ Pull & rebase berhasil!"
else
  echo "❌ Terjadi masalah saat rebase. Menyimpan log..."
  cp .git/rebase-apply/patch ./rebase-error.patch
fi

# Kembalikan stash jika perlu
if [ "$STASHED" = true ]; then
  echo "🔁 Mengembalikan stash..."
  git stash pop || {
    echo "⚠️ Konflik saat apply stash. Simpan manual!"
    exit 1
  }
fi

echo "🎉 Selesai. Repo aman dan sinkron!"
