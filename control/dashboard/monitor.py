# 🧠 JARVIS Monitor v2050 - Real-Time Observer + Analyzer Integration

import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from analyzer import analyze_event
from audit_log import log_event

logging.basicConfig(level=logging.INFO, format="%(asctime)s [Monitor] %(message)s")

WATCH_PATH = "./distribution/logs"

class JARVISMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        logging.info(f"📁 File berubah: {event.src_path}")
        payload = {
            "event_type": "modified",
            "file_path": event.src_path
        }

        # 🔍 Analisis otomatis
        analysis = analyze_event(payload)

        # 📝 Audit log
        log_event("monitor", "file_modified", {
            "path": event.src_path,
            "analysis": analysis
        })

        logging.info(f"🧠 Analisis: {analysis.get('summary')}")

def start_monitor():
    observer = Observer()
    observer.schedule(JARVISMonitorHandler(), path=WATCH_PATH, recursive=True)
    observer.start()
    logging.info(f"🚀 Monitoring dimulai di folder: {WATCH_PATH}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("🛑 Monitoring dihentikan.")

    observer.join()

if __name__ == "__main__":
    start_monitor()
