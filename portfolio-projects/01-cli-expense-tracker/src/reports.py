"""Summary and reporting for the expense tracker."""
from tracker import _read_all


def summary():
    rows = _read_all()
    if not rows:
        print("No expenses recorded.")
        return

    totals_by_category = {}
    totals_by_month = {}

    for r in rows:
        cat = r["category"]
        amount = float(r["amount"])
        month = r["date"][:7]  # YYYY-MM

        totals_by_category[cat] = totals_by_category.get(cat, 0) + amount
        totals_by_month[month] = totals_by_month.get(month, 0) + amount

    print("\n--- By Category ---")
    for cat, total in sorted(totals_by_category.items()):
        print(f"  {cat:<20} ${total:>8.2f}")

    print("\n--- By Month ---")
    for month, total in sorted(totals_by_month.items()):
        print(f"  {month:<10}           ${total:>8.2f}")

    grand_total = sum(float(r["amount"]) for r in rows)
    print(f"\n  Total: ${grand_total:.2f}")
