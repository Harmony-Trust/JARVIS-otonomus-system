# 🚀 JARVIS System Bootstrap v2050 - Ultra Initialization Entry Point

import time
import logging
from control.harmony.harmony_core import start_harmony

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [Bootstrap] %(message)s")
    logging.info("🚀 JARVIS System Bootstrap dimulai.")
    start_time = time.time()

    try:
        status = start_harmony()
        logging.info(f"🧩 Harmony status: {status}")
    except Exception as e:
        logging.error(f"❌ Bootstrap gagal: {e}")
        status = "Error"

    elapsed = time.time() - start_time
    logging.info(f"⏱️ Bootstrap selesai dalam {elapsed:.2f} detik.")
    print(f"\n✨ JARVIS Bootstrap Selesai. Status: {status}\n")
    print(f"System status: {status}")  # Tambahan dari versi lama

if __name__ == "__main__":
    main()
