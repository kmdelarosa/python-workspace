"""CSV/JSON export and deduplication for scraped listings."""
import csv
import json
import os
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
FIELDNAMES = ["title", "company", "location", "date_posted", "url"]


def save_results(listings: list[dict], format: str = "csv"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Deduplicate against existing saved data
    listings = _deduplicate(listings)

    if format in ("csv", "both"):
        _save_csv(listings, timestamp)
    if format in ("json", "both"):
        _save_json(listings, timestamp)

    print(f"Saved {len(listings)} unique listings.")


def _save_csv(listings, timestamp):
    path = os.path.join(OUTPUT_DIR, f"listings_{timestamp}.csv")
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(listings)
    print(f"CSV saved: {path}")


def _save_json(listings, timestamp):
    path = os.path.join(OUTPUT_DIR, f"listings_{timestamp}.json")
    with open(path, "w") as f:
        json.dump(listings, f, indent=2)
    print(f"JSON saved: {path}")


def _deduplicate(listings: list[dict]) -> list[dict]:
    """Remove listings whose URLs have already been saved."""
    seen_urls = set()
    for filename in os.listdir(OUTPUT_DIR) if os.path.exists(OUTPUT_DIR) else []:
        if filename.endswith(".csv"):
            with open(os.path.join(OUTPUT_DIR, filename)) as f:
                for row in csv.DictReader(f):
                    seen_urls.add(row.get("url", ""))

    return [l for l in listings if l["url"] not in seen_urls]
