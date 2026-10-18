"""Report generation for the finance dashboard."""


def print_summary(data: dict):
    transactions = data.get("transactions", [])
    budgets = data.get("budgets", {})

    if not transactions:
        print("No transactions to report.")
        return

    totals = {}
    income_total = 0.0

    for t in transactions:
        if t["type"] == "income":
            income_total += t["amount"]
        else:
            totals[t["category"]] = totals.get(t["category"], 0) + t["amount"]

    expense_total = sum(totals.values())

    print("\n--- Summary Report ---")
    print(f"  Total Income:   ${income_total:>8.2f}")
    print(f"  Total Expenses: ${expense_total:>8.2f}")
    print(f"  Net:            ${income_total - expense_total:>8.2f}")

    print("\n--- Expenses by Category ---")
    for cat, total in sorted(totals.items()):
        budget = budgets.get(cat)
        budget_str = f" (budget: ${budget:.2f}, remaining: ${budget - total:.2f})" if budget else ""
        print(f"  {cat:<20} ${total:>8.2f}{budget_str}")
