"""CSV parsing and validation for the report generator."""
import csv
import os

REQUIRED_COLUMNS = ["date", "category", "amount"]


def load_csv(path: str) -> list[dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")

    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for col in REQUIRED_COLUMNS:
            if col not in reader.fieldnames:
                raise ValueError(f"Missing required column: '{col}'")

        for i, row in enumerate(reader, start=1):
            try:
                row["amount"] = float(row["amount"])
                rows.append(row)
            except ValueError:
                print(f"Warning: skipping row {i} — invalid amount '{row['amount']}'")

    return rows
