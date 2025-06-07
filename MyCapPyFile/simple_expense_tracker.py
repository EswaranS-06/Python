import datetime
from openpyxl import Workbook

# List to store expenses
expenses = []
categories = ['Groceries', 'Transportation', 'Entertainment', 'Utilities', 'Other']
budgets = {category: float('inf') for category in categories}

def add_expense():
    try:
        amount = float(input("Amount spent: "))
        description = input("Description: ")

        print("Choose a category:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        category_index = int(input("Enter category number: ")) - 1
        category = categories[category_index]

        date = datetime.date.today().isoformat()

        expense = {'date': date, 'amount': amount, 'description': description, 'category': category}
        expenses.append(expense)

        # Budget warning
        total_in_category = sum(e['amount'] for e in expenses if e['category'] == category)
        if total_in_category > budgets.get(category, float('inf')):
            print("⚠️ Budget exceeded for", category)
    except:
        print("❌ Invalid input. Try again.")

def set_budget():
    print("Choose a category to set budget:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    index = int(input("Category number: ")) - 1
    category = categories[index]
    budget = float(input(f"Set budget for {category}: "))
    budgets[category] = budget
    print("✅ Budget set.")

def list_expenses():
    if not expenses:
        print("No expenses yet.")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['date']} | {e['amount']} | {e['description']} | {e['category']}")

def export_to_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Expenses"

    ws.append(["Date", "Amount", "Description", "Category"])

    for e in expenses:
        ws.append([e['date'], e['amount'], e['description'], e['category']])

    filename = f"expenses_{datetime.date.today()}.xlsx"
    wb.save(filename)
    print(f"✅ Expenses exported to {filename}")

def show_summary():
    total = sum(e['amount'] for e in expenses)
    print(f"\n📊 Total Spending: {total}")
    print("By category:")
    for cat in categories:
        cat_total = sum(e['amount'] for e in expenses if e['category'] == cat)
        print(f"{cat}: {cat_total}")

def search_expenses():
    term = input("Enter keyword or date (YYYY-MM-DD): ").lower()
    results = [e for e in expenses if term in e['description'].lower() or term in e['date']]
    for e in results:
        print(f"{e['date']} | {e['amount']} | {e['description']} | {e['category']}")
    if not results:
        print("No matches found.")

def menu():
    while True:
        print("\n📘 Expense Tracker")
        print("1. Add Expense")
        print("2. Set Budget")
        print("3. List Expenses")
        print("4. Export to Excel")
        print("5. Show Summary")
        print("6. Search")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            set_budget()
        elif choice == '3':
            list_expenses()
        elif choice == '4':
            export_to_excel()
        elif choice == '5':
            show_summary()
        elif choice == '6':
            search_expenses()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
