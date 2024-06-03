import json
from datetime import datetime
import os

# Main function
def main():
    print("Welcome to Personal Finance Manager!")
    # Example menu
    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Set Monthly Budget")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            set_monthly_budget()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to add a transaction
def add_transaction():
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Rent, Entertainment): ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    transaction = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    if not os.path.exists('transactions.json'):
        with open('transactions.json', 'w') as file:
            json.dump([], file)

    with open('transactions.json', 'r') as file:
        transactions = json.load(file)

    transactions.append(transaction)

    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)

    print("Transaction added successfully!")

# Function to view transactions
def view_transactions():
    if not os.path.exists('transactions.json'):
        print("No transactions found.")
        return

    with open('transactions.json', 'r') as file:
        transactions = json.load(file)

    for transaction in transactions:
        print(f"Amount: {transaction['amount']}, Category: {transaction['category']}, Date: {transaction['date']}, Description: {transaction['description']}")

# Function to generate report
def generate_report():
    if not os.path.exists('transactions.json'):
        print("No transactions found.")
        return

    with open('transactions.json', 'r') as file:
        transactions = json.load(file)

    report = {}
    for transaction in transactions:
        category = transaction['category']
        amount = transaction['amount']
        if category in report:
            report[category] += amount
        else:
            report[category] = amount

    print("Expense Report:")
    for category, amount in report.items():
        print(f"{category}: {amount}")

# Function to set monthly budget
def set_monthly_budget():
    budget = float(input("Enter your monthly budget: "))

    with open('budget.txt', 'w') as file:
        file.write(str(budget))

    print("Monthly budget set successfully!")

if __name__ == "__main__":
    main()
