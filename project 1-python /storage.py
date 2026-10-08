# ==========================================
# FILE: storage.py
# Handles all file I/O for the expense tracker.
# This module has ZERO print statements —
# it is purely responsible for data persistence.
# ==========================================
import os
import csv

CSV_FILE= "expenses.csv"
HEADERS=["Date","Category","Amount"]

"""
    Creates the CSV file with headers if it doesn't already exist.
    Safe to call every time the app starts — it won't overwrite existing data.
    """
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(  CSV_FILE, mode= 'w',newline ='') as file:
            writer = csv.writer(file)
            writer.writer(HEADERS)

"""
    Appends a single structured expense row to the local CSV file.
    Uses 'a' (append) mode so existing records are never erased.
    """

def append_to_csv(date, category, amount):
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, f"{amount:.2f}"])


def read_all_expenses():
    """
    Reads every expense row from the CSV and returns it as a list
    of dictionaries, e.g.:
    [{"Date": "2024-01-01", "Category": "Food", "Amount": "12.50"}, ...]

    Returns an empty list if the file doesn't exist or has no data rows.
    """
    if not os.path.exists(CSV_FILE):
        return []

    expenses = []
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return expenses


def get_total_by_category():
    """
    Aggregates all expenses and returns a dictionary mapping
    category -> total amount spent, e.g. {"Food": 45.50, "Rent": 900.0}
    """
    expenses = read_all_expenses()
    totals = {}

    for row in expenses:
        category = row["Category"]
        try:
            amount = float(row["Amount"])
        except (ValueError, KeyError):
            # Skip corrupted rows instead of crashing the summary report
            continue
        totals[category] = totals.get(category, 0) + amount

    return totals


def get_grand_total():
    """Returns the sum of all logged expenses as a float."""
    return sum(get_total_by_category().values())


def delete_all_expenses():
    """
    Resets the CSV file back to just the header row.
    Useful for a 'clear data' feature.
    """
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)

# written in 2022