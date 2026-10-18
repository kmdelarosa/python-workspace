"""Load and validate the extension-to-folder mapping config."""
import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")


def load_config() -> dict:
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Config not found at {CONFIG_PATH}")
    with open(CONFIG_PATH) as f:
        config = json.load(f)
    if not isinstance(config, dict):
        raise ValueError("config.json must be a JSON object mapping extensions to folder names.")
    return config
