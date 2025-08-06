# 📦 JARVIS Module: PluginLoader v2050
# Tujuan: Memuat plugin modular secara dinamis dengan proteksi, logging, dan introspeksi

import importlib
import os
import logging
import traceback

PLUGIN_NAMESPACE = "control.plugins"

def load_plugins(plugin_folder="control/plugins"):
    plugins = []
    if not os.path.exists(plugin_folder):
        logging.warning(f"📁 Folder plugin tidak ditemukan: {plugin_folder}")
        return plugins

    for fname in os.listdir(plugin_folder):
        if fname.endswith(".py") and not fname.startswith("__"):
            mod_name = fname[:-3]
            full_module_path = f"{PLUGIN_NAMESPACE}.{mod_name}"
            try:
                mod = importlib.import_module(full_module_path)
                plugins.append(mod)
                logging.info(f"✅ Plugin dimuat: {full_module_path}")
            except Exception as e:
                logging.error(f"❌ Gagal memuat plugin {full_module_path}: {e}")
                logging.debug(traceback.format_exc())
    return plugins
