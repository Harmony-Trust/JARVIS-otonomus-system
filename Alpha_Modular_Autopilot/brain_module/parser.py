# 📦 JARVIS Module: Parsey v2050
# Tujuan: Orkestrasi agent, integrasi Supabase, dan parsing input NLP

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
AGENT_DIR = os.path.join(BASE_DIR, 'control', 'agents')
INTEGRATION_DIR = os.path.join(BASE_DIR, 'integrations')

for path in [AGENT_DIR, INTEGRATION_DIR]:
    if path not in sys.path:
        sys.path.insert(0, path)

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

# === Supabase Integration Check ===
try:
    from supabase.supabase_client import store_payload
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    if not supabase_url or not supabase_key:
        logging.warning("⚠️ Supabase credentials not set.")
    else:
        logging.info("🛠️ Supabase client ready.")
except Exception as e:
    logging.error(f"❌ Supabase client error: {e}")
    logging.debug(traceback.format_exc())

# === NLP Parser Core ===
def parse_input(text):
    # TODO: Improve NLP & intent parsing
    return {"intent": "auto_dispatch", "content": text}

print("\n🔍 Parsey selesai mengorkestrasi agent, integrasi Supabase, dan parser NLP.\n")
