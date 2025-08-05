# 🚀 System Bootstrap Entry - Ultra Initialization

import time
import logging
from control.harmony.harmony_core import start_harmony

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [Bootstrap] %(message)s")
    logging.info("🚀 JARVIS System Bootstrap started.")
    start_time = time.time()

    try:
        status = start_harmony()
        logging.info(f"System status: {status}")
    except Exception as e:
        logging.error(f"Bootstrap failed: {e}")
        status = "Error"

    elapsed = time.time() - start_time
    logging.info(f"Bootstrap completed in {elapsed:.2f} seconds.")
    print(f"\n✨ JARVIS Bootstrap Selesai. Status: {status}\n")

if __name__ == "__main__":
    main()
