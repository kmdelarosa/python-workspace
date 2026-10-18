"""JSON persistence for finance data."""
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATA_FILE = os.path.join(DATA_DIR, "finance.json")

_DEFAULT_DATA = {"transactions": [], "budgets": {}}


def load_data() -> dict:
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        save_data(_DEFAULT_DATA.copy())
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data: dict):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
