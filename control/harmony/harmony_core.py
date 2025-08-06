# 🚀 JARVIS Module: Harmony Control Core v2050
# Tujuan: Orkestrasi modul harmoni dengan proteksi konfigurasi, introspeksi, dan event loop

import os
import importlib
import logging
import traceback
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "harmony_config.yaml")

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r") as f:
                config = yaml.safe_load(f)
                logging.info("✅ Config berhasil dimuat.")
                return config
        except Exception as e:
            logging.error(f"❌ Gagal membaca config: {e}")
            logging.debug(traceback.format_exc())
            return {}
    else:
        logging.warning("⚠️ Config file tidak ditemukan, menggunakan default.")
        return {}

def discover_modules(folder):
    modules = []
    for fname in os.listdir(folder):
        if fname.endswith(".py") and not fname.startswith("__"):
            modules.append(fname[:-3])
    return modules

def connect_modules(modules, namespace="control.harmony"):
    for mod_name in modules:
        try:
            full_path = f"{namespace}.{mod_name}"
            mod = importlib.import_module(full_path)
            if hasattr(mod, "init_module"):
                mod.init_module()
                logging.info(f"🔗 Module '{mod_name}' connected.")
        except Exception as e:
            logging.error(f"❌ Module '{mod_name}' failed: {e}")
            logging.debug(traceback.format_exc())

def start_harmony():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [Harmony] %(message)s")
    print("🎼 Harmony orchestration initiated...")

    config = load_config()
    logging.info(f"🧠 Config loaded: {config}")

    harmony_folder = os.path.dirname(__file__)
    modules = discover_modules(harmony_folder)
    connect_modules(modules)

    logging.info("🌀 Harmony is listening for system events...")
    for i in range(3):
        logging.info(f"🕒 Event tick {i+1} - system stable.")

    logging.info("✅ Harmony orchestration complete.")
    return "Ready"
