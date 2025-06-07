import json
from collections import defaultdict
import matplotlib.pyplot as plt

expenses = []
categories = {
    "default": ["Groceries", "Transportation", "Entertainment", "Utilities"],
    "custom": []
}


def save_data():
    with open("expenses.json", "w") as f:
        json.dump({"expenses": expenses, "categories": categories}, f)


def load_data():
    global expenses, categories
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
            expenses = data.get("expenses", [])
            categories = data.get("categories", {"default": [], "custom": []})
    except FileNotFoundError:
        pass


def list_all_categories():
    return categories["default"] + categories["custom"]


def add_category():
    name = input("Enter new custom category name: ")
    if name in list_all_categories():
        print("Category already exists.")
    else:
        categories["custom"].append(name)
        print(f"Added category '{name}'.")


def remove_category():
    name = input("Enter custom category to remove: ")
    if name in categories["custom"]:
        categories["custom"].remove(name)
        print(f"Removed category '{name}'.")
    else:
        print("Custom category not found.")


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        all_cats = list_all_categories()
        print("Available categories:")
        for i, cat in enumerate(all_cats, 1):
            print(f"{i}. {cat}")

        cat_index = int(input("Select a category by number: ")) - 1
        if cat_index < 0 or cat_index >= len(all_cats):
            raise ValueError("Invalid category selected.")

        category = all_cats[cat_index]
        expenses.append({
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        })
        print("Expense added.")
    except Exception as e:
        print("Error:", e)


def view_summary_by_category():
    summary = defaultdict(list)
    for e in expenses:
        summary[e["category"]].append(e["amount"])

    print("\nCategory-wise Summary:")
    for category, amounts in summary.items():
        print(f"{category}: Total = {sum(amounts):.2f}, Average = {sum(amounts)/len(amounts):.2f}")


def show_statistics():
    summary = defaultdict(float)
    for e in expenses:
        summary[e["category"]] += e["amount"]

    if not summary:
        print("No expenses to analyze.")
        return

    max_cat = max(summary, key=summary.get)
    min_cat = min(summary, key=summary.get)
    total = sum(summary.values())

    print(f"\nHighest Spending: {max_cat} (${summary[max_cat]:.2f})")
    print(f"Lowest Spending: {min_cat} (${summary[min_cat]:.2f})")

    print("\nSpending Percentage by Category:")
    for cat, val in summary.items():
        print(f"{cat}: {(val / total * 100):.2f}%")


def display_chart():
    summary = defaultdict(float)
    for e in expenses:
        summary[e["category"]] += e["amount"]

    if not summary:
        print("No data to display.")
        return

    labels = list(summary.keys())
    sizes = list(summary.values())

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.axis("equal")
    plt.title("Spending by Category")
    plt.show()


def main():
    load_data()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Add Custom Category")
        print("3. Remove Custom Category")
        print("4. View Category Summary")
        print("5. Show Statistics")
        print("6. Display Chart")
        print("7. Save and Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            add_category()
        elif choice == "3":
            remove_category()
        elif choice == "4":
            view_summary_by_category()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            display_chart()
        elif choice == "7":
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
