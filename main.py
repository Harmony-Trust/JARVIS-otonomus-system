# 📦 JARVIS Bootstrap v2050
# Tujuan: Menginisialisasi sistem JARVIS dengan proteksi, logging, dan modularisasi

import os
import sys
import importlib
import logging
import traceback

# === Logging Setup ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# === Dynamic Path Setup ===
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CONTROL_DIR = os.path.join(BASE_DIR, 'control')
HARMONY_DIR = os.path.join(CONTROL_DIR, 'harmony')
AGENT_DIR = os.path.join(CONTROL_DIR, 'agents')

for path in [CONTROL_DIR, HARMONY_DIR, AGENT_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

# === Package Assurance ===
for folder in [CONTROL_DIR, HARMONY_DIR, AGENT_DIR]:
    init_path = os.path.join(folder, '__init__.py')
    if not os.path.exists(init_path):
        with open(init_path, 'w') as f:
            f.write("# Auto-created to register package\n")

# === Load Core Harmony Engine ===
try:
    from harmony_core import start_harmony
    start_harmony()
    logging.info("🎼 Harmony Engine started.")
except Exception as e:
    logging.error(f"❌ Harmony Engine Error: {e}")
    logging.debug(traceback.format_exc())

# === Load All Agents Automatically ===
def load_agents(agent_folder):
    for filename in os.listdir(agent_folder):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, 'start_agent'):
                    module.start_agent()
                    logging.info(f"🤖 Agent '{module_name}' started.")
            except Exception as err:
                logging.error(f"❌ Agent '{module_name}' failed: {err}")
                logging.debug(traceback.format_exc())

load_agents(AGENT_DIR)

# === Supabase & ENV Setup ===
try:
    from integrations.supabase.supabase_client import store_payload
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    if not supabase_url or not supabase_key:
        logging.warning("⚠️ Supabase credentials not set.")
    else:
        logging.info("🛠️ Supabase client ready.")
except Exception as e:
    logging.error(f"❌ Supabase client error: {e}")
    logging.debug(traceback.format_exc())

# === Optional: Voice Interface ===
try:
    from voice_listener import init_listener
    init_listener()
    logging.info("🎙️ Voice listener active.")
except Exception as e:
    logging.info("🔕 Voice listener not active.")

# === Optional: CLI Command Interface ===
try:
    from harmony_cli import cli_loop
    cli_loop()
    logging.info("🧭 CLI loop initiated.")
except Exception as e:
    logging.info("🧭 CLI loop not initiated.")

# === Optional: Momentum Engine & Campaign Push ===
try:
    from momentum_engine import init_momentum
    init_momentum()
    from campaign_pusher import run_push_cycle
    run_push_cycle()
    logging.info("📡 Distribution modules enabled.")
except Exception as e:
    logging.info("📡 Distribution modules not yet enabled.")

print("\n✨ JARVIS Bootstrap Selesai. Sistem siap digerakkan!\n")
