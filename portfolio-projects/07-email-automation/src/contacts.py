"""Load and validate contacts from a CSV file."""
import csv
import os

REQUIRED_FIELDS = ["name", "email"]


def load_contacts(path: str) -> list[dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Contacts file not found: {path}")

    contacts = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            for field in REQUIRED_FIELDS:
                if not row.get(field):
                    raise ValueError(f"Row {i} missing required field: '{field}'")
            contacts.append(dict(row))

    return contacts
