"""Entry point for the Personal Finance Dashboard."""
from storage import load_data, save_data
from models.transaction import Transaction
from reports import print_summary


def main_menu():
    data = load_data()
    options = {
        "1": "Add transaction",
        "2": "List transactions",
        "3": "Summary report",
        "4": "Set budget",
        "5": "Quit",
    }
    while True:
        print("\n--- Personal Finance Dashboard ---")
        for key, label in options.items():
            print(f"  {key}. {label}")
        choice = input("Select option: ").strip()

        if choice == "1":
            _add_transaction(data)
            save_data(data)
        elif choice == "2":
            _list_transactions(data)
        elif choice == "3":
            print_summary(data)
        elif choice == "4":
            _set_budget(data)
            save_data(data)
        elif choice == "5":
            break
        else:
            print("Invalid option.")


def _add_transaction(data):
    t_type = input("Type (expense/income): ").strip().lower()
    date = input("Date (YYYY-MM-DD): ").strip()
    category = input("Category: ").strip()
    amount = input("Amount: ").strip()
    description = input("Description: ").strip()

    try:
        next_id = max((t["id"] for t in data["transactions"]), default=0) + 1
        t = Transaction(next_id, date, category, amount, description, t_type)
        data["transactions"].append(t.to_dict())
        print(f"Transaction #{next_id} added.")
    except ValueError:
        print("Invalid amount.")


def _list_transactions(data):
    transactions = data.get("transactions", [])
    if not transactions:
        print("No transactions recorded.")
        return
    print(f"\n{'ID':<5} {'Date':<12} {'Type':<10} {'Category':<15} {'Amount':>8}  Description")
    print("-" * 65)
    for t in transactions:
        print(f"{t['id']:<5} {t['date']:<12} {t['type']:<10} {t['category']:<15} {t['amount']:>8.2f}  {t['description']}")


def _set_budget(data):
    category = input("Category: ").strip()
    limit = input("Monthly limit: ").strip()
    try:
        data["budgets"][category] = float(limit)
        print(f"Budget set: {category} = ${float(limit):.2f}/month")
    except ValueError:
        print("Invalid amount.")


if __name__ == "__main__":
    main_menu()
