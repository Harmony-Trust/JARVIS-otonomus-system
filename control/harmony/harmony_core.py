# 🚀 Harmony Control Core - Ultra Orchestration Engine

import os
import importlib
import logging

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "harmony_config.yaml")

def load_config():
    if os.path.exists(CONFIG_PATH):
        import yaml
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f)
    else:
        logging.warning("Config file not found, using default config.")
        return {}

def discover_modules(folder):
    modules = []
    for fname in os.listdir(folder):
        if fname.endswith(".py") and not fname.startswith("__"):
            modules.append(fname[:-3])
    return modules

def connect_modules(modules, folder):
    for mod_name in modules:
        try:
            mod = importlib.import_module(mod_name)
            if hasattr(mod, "init_module"):
                mod.init_module()
                logging.info(f"Module '{mod_name}' connected.")
        except Exception as e:
            logging.error(f"Module '{mod_name}' failed: {e}")

def start_harmony():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [Harmony] %(message)s")
    print("🎼 Harmony orchestration initiated...")

    config = load_config()
    logging.info(f"Config loaded: {config}")

    # Discover and connect harmony modules
    harmony_folder = os.path.dirname(__file__)
    modules = discover_modules(harmony_folder)
    connect_modules(modules, harmony_folder)

    # Listen to system events (simple loop)
    logging.info("Harmony is listening for system events...")
    # Simulasi event loop sederhana
    for i in range(3):
        logging.info(f"Event tick {i+1} - system stable.")

    logging.info("Harmony orchestration complete.")
    return "Ready"
