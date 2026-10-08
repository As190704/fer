# ==========================================
# FILE: app.py
# The command-line interface for the Expense Tracker.
# Imports storage.py to persist data, but never touches
# the CSV file directly itself.
# ==========================================

from datetime import datetime
import storage

VALID_CATEGORIES = ["Food", "Rent", "Gas", "Utilities", "Entertainment",
                     "Shopping", "Health", "Other"]


def print_banner():
    print("=" * 50)
    print("   COMMAND-LINE EXPENSE TRACKER & CSV EXPORTER")
    print("=" * 50)


def print_menu():
    print("\n----------------------------------")
    print(" [1] Add Expense")
    print(" [2] View Summary (by category)")
    print(" [3] View All Transactions")
    print(" [4] Clear All Data")
    print(" [5] Exit")
    print("----------------------------------")


def get_valid_date():
    """
    Prompts for a date, defaults to today if left blank,
    and validates the format using datetime.strptime.
    Loops until a valid date or blank input is given.
    """
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

        if not date_input:
            return datetime.today().strftime('%Y-%m-%d')

        try:
            # This both validates AND normalizes the format
            parsed_date = datetime.strptime(date_input, '%Y-%m-%d')
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            print("⚠️  Invalid date format! Please use YYYY-MM-DD (e.g., 2024-03-15).")


def get_valid_category():
    """
    Prompts for a category. Accepts free text but guards against
    an empty string, since a blank category is meaningless in a ledger.
    """
    while True:
        category = input(f"Enter category {VALID_CATEGORIES}: ").strip().title()

        if not category:
            print("⚠️  Category cannot be empty. Please try again.")
            continue

        return category


def get_valid_amount():
    """
    Prompts for an amount and wraps conversion in a try/except block.
    This is the core defensive-programming requirement of the project —
    typos like 'twenty bucks' must NOT crash the application.
    """
    while True:
        raw_amount = input("Enter amount spent: $").strip()

        try:
            amount = float(raw_amount)

            if amount <= 0:
                print("⚠️  Amount must be greater than zero. Try again.")
                continue

            return amount

        except ValueError:
            print("⚠️  Invalid input! Please enter a numeric value (e.g., 19.99).")


def handle_add_expense():
    """Coordinates collecting a full expense record and saving it."""
    print("\n--- Add New Expense ---")
    date = get_valid_date()
    category = get_valid_category()
    amount = get_valid_amount()

    storage.append_to_csv(date, category, amount)
    print(f"\n✅ Successfully logged ${amount:.2f} under '{category}' on {date}!")


def handle_view_summary():
    """Displays total spending grouped by category, plus a grand total."""
    totals = storage.get_total_by_category()

    print("\n--- Expense Summary ---")
    if not totals:
        print("No expenses recorded yet.")
        return

    for category, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category:<15} ${total:>10.2f}")

    grand_total = sum(totals.values())
    print("-" * 28)
    print(f"  {'TOTAL':<15} ${grand_total:>10.2f}")


def handle_view_all():
    """Displays every individual transaction in a readable table."""
    expenses = storage.read_all_expenses()

    print("\n--- All Transactions ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'Date':<12} {'Category':<15} {'Amount':>10}")
    print("-" * 40)
    for row in expenses:
        try:
            amount = float(row["Amount"])
            print(f"{row['Date']:<12} {row['Category']:<15} ${amount:>9.2f}")
        except (ValueError, KeyError):
            continue  # skip any corrupted row rather than crashing


def handle_clear_data():
    """Asks for confirmation before wiping all stored expenses."""
    confirm = input("Are you sure you want to delete ALL data? (yes/no): ").strip().lower()
    if confirm == "yes":
        storage.delete_all_expenses()
        print("🗑️  All expense data has been cleared.")
    else:
        print("Cancelled. No data was deleted.")


def run_tracker():
    """Main application entry point — contains the primary menu loop."""
    storage.initialize_csv()
    print_banner()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_summary()
        elif choice == "3":
            handle_view_all()
        elif choice == "4":
            handle_clear_data()
        elif choice == "5":
            print("\n👋 Goodbye! Your expenses are saved in expenses.csv")
            break
        else:
            print("⚠️  Invalid choice, please select a number between 1 and 5.")


if __name__ == "__main__":
    run_tracker()