"""Entry point for the CLI Expense Tracker."""
from tracker import add_expense, delete_expense, list_expenses
from reports import summary


def main_menu():
    options = {
        "1": ("Add expense", add_expense),
        "2": ("List expenses", list_expenses),
        "3": ("Summary", summary),
        "4": ("Delete expense", delete_expense),
        "5": ("Quit", None),
    }
    while True:
        print("\n--- Expense Tracker ---")
        for key, (label, _) in options.items():
            print(f"  {key}. {label}")
        choice = input("Select option: ").strip()
        if choice == "5":
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main_menu()
