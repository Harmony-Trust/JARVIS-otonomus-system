import importlib
import os

def load_plugins(plugin_folder="control/plugins"):
    plugins = []
    for fname in os.listdir(plugin_folder):
        if fname.endswith(".py") and not fname.startswith("__"):
            mod_name = fname[:-3]
            mod = importlib.import_module(f"control.plugins.{mod_name}")
            plugins.append(mod)
    return plugins