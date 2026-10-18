"""Add, list, and delete expenses from the CSV store."""
import csv
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATA_FILE = os.path.join(DATA_DIR, "expenses.csv")
FIELDNAMES = ["id", "date", "category", "amount", "description"]


def _ensure_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def _read_all():
    _ensure_file()
    with open(DATA_FILE, "r", newline="") as f:
        return list(csv.DictReader(f))


def _write_all(rows):
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def _next_id(rows):
    if not rows:
        return 1
    return max(int(r["id"]) for r in rows) + 1


def add_expense():
    rows = _read_all()
    date = input("Date (YYYY-MM-DD) [today]: ").strip() or datetime.today().strftime("%Y-%m-%d")
    category = input("Category: ").strip()
    amount = input("Amount: ").strip()
    description = input("Description: ").strip()

    try:
        float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    row = {"id": _next_id(rows), "date": date, "category": category,
           "amount": amount, "description": description}
    rows.append(row)
    _write_all(rows)
    print(f"Expense #{row['id']} added.")


def list_expenses():
    rows = _read_all()
    category = input("Filter by category (leave blank for all): ").strip()
    if category:
        rows = [r for r in rows if r["category"].lower() == category.lower()]

    if not rows:
        print("No expenses found.")
        return

    print(f"\n{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':>8}  Description")
    print("-" * 60)
    for r in rows:
        print(f"{r['id']:<5} {r['date']:<12} {r['category']:<15} {float(r['amount']):>8.2f}  {r['description']}")


def delete_expense():
    expense_id = input("Enter expense ID to delete: ").strip()
    rows = _read_all()
    new_rows = [r for r in rows if r["id"] != expense_id]
    if len(new_rows) == len(rows):
        print(f"No expense with ID {expense_id}.")
        return
    _write_all(new_rows)
    print(f"Expense #{expense_id} deleted.")
