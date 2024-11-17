import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


def log_expense():
    name = input("Enter your name: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., groceries, utilities, entertainment): ")
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, date, description, amount, category])


def analyze_expenses():
    expenses = pd.read_csv(
        "expenses.csv", names=["Name", "Date", "Description", "Amount", "Category"]
    )
    total_expenses = expenses.groupby("Name")["Amount"].sum()
    avg_daily_expense = expenses["Amount"].sum() / len(expenses["Date"].unique())
    print("Total expenses per member:")
    print(total_expenses)
    print(f"Average daily expense for the household: {avg_daily_expense:.2f}")


def show_expense_trends():
    expenses = pd.read_csv(
        "expenses.csv", names=["Name", "Date", "Description", "Amount", "Category"]
    )
    expenses["Date"] = pd.to_datetime(expenses["Date"])
    monthly_expenses = (
        expenses.groupby(expenses["Date"].dt.date)["Amount"].sum().cumsum()
    )
    plt.plot(monthly_expenses.index, monthly_expenses.values)
    plt.xlabel("Date")
    plt.ylabel("Cumulative Expenses")
    plt.title("Expense Trends Over the Last Month")
    plt.xticks(rotation=45)
    plt.show()


def generate_expense_report():
    expenses = pd.read_csv(
        "expenses.csv", names=["Name", "Date", "Description", "Amount", "Category"]
    )
    monthly_expenses = expenses.groupby("Name")["Amount"].sum()
    category_expenses = expenses.groupby("Category")["Amount"].sum()
    print("Monthly Expenses per Member:")
    print(monthly_expenses)
    print("Expenses by Category:")
    print(category_expenses)
    months = expenses["Date"].apply(lambda x: x[:7]).unique()
    monthly_totals = [
        expenses[expenses["Date"].str.startswith(month)]["Amount"].sum()
        for month in months
    ]
    plt.bar(months, monthly_totals)
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.title("Monthly Expenses Comparison")
    plt.show()


def set_budget():
    budgets = {}
    with open("budgets.csv", "a+", newline="") as f:
        f.seek(0)
        reader = csv.reader(f)
        budgets = {rows[0]: float(rows[1]) for rows in reader}
        while True:
            category = input("Enter category to set budget (or 'done' to finish): ")
            if category == "done":
                break
            budget = float(input(f"Enter budget for {category}: "))
            budgets[category] = budget
            writer = csv.writer(f)
            writer.writerow([category, budget])


def check_budget():
    expenses = pd.read_csv(
        "expenses.csv", names=["Name", "Date", "Description", "Amount", "Category"]
    )
    category_totals = expenses.groupby("Category")["Amount"].sum()
    budgets = pd.read_csv("budgets.csv", names=["Category", "Budget"])
    for _, row in budgets.iterrows():
        category = row["Category"]
        if category in category_totals and category_totals[category] > row["Budget"]:
            print(f"Warning: Budget exceeded for {category}")


def backup_data():
    if os.path.exists("expenses.csv"):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        os.rename("expenses.csv", f"backup_expenses_{timestamp}.csv")
        print("Backup completed.")
    else:
        print("No data to backup.")


def restore_data():
    backups = [file for file in os.listdir() if file.startswith("backup_expenses_")]
    if backups:
        latest_backup = sorted(backups)[-1]
        os.rename(latest_backup, "expenses.csv")
        print("Data restored from latest backup.")
    else:
        print("No backup file found.")


def main():
    if not os.path.exists("expenses.csv"):
        open("expenses.csv", "w").close()
    if not os.path.exists("budgets.csv"):
        open("budgets.csv", "w").close()
    while True:
        choice = input(
            "1. Log Expense\n2. Analyze Expenses\n3. Show Expense Trends\n4. Generate Expense Report\n5. Set Budget\n6. Check Budget\n7. Backup Data\n8. Restore Data\n9. Exit\nChoose an option: "
        )
        if choice == "1":
            log_expense()
        elif choice == "2":
            analyze_expenses()
        elif choice == "3":
            show_expense_trends()
        elif choice == "4":
            generate_expense_report()
        elif choice == "5":
            set_budget()
        elif choice == "6":
            check_budget()
        elif choice == "7":
            backup_data()
        elif choice == "8":
            restore_data()
        elif choice == "9":
            break


main()
