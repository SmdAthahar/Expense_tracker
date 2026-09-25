import csv

from validation import validate_amount
from validation import validate_category
from validation import validate_description

from logger import log_operation

from expense_package.helpers import find_expense


def load_expenses():

    expenses = []

    try:

        with open("expenses.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                expenses.append(row)

    except FileNotFoundError:

        pass

    except Exception as error:

        print("Error while loading expenses:", error)

    return expenses


def save_expenses(expenses):

    try:

        with open("expenses.csv", "w", newline="") as file:

            fieldnames = [
                "id",
                "date",
                "description",
                "category",
                "amount"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for expense in expenses:

                writer.writerow(expense)

        print("Expenses saved successfully.")

    except Exception as error:

        print("Error while saving expenses:", error)


def get_next_id(expenses):

    if len(expenses) == 0:

        return 1

    highest_id = 0

    for expense in expenses:

        current_id = int(expense["id"])

        if current_id > highest_id:

            highest_id = current_id

    return highest_id + 1


def add_expense(expenses):

    print()
    print("----- Add Expense -----")

    try:

        description = input("Enter description: ")
        description = validate_description(description)

        category = input("Enter category: ")
        category = validate_category(category)

        amount = input("Enter amount: ")
        amount = validate_amount(amount)

        date = input("Enter date (YYYY-MM-DD): ")

        expense_id = get_next_id(expenses)

        expense = {
            "id": str(expense_id),
            "date": date,
            "description": description,
            "category": category,
            "amount": str(amount)
        }

        expenses.append(expense)

        save_expenses(expenses)

        print("Expense added successfully.")

        log_operation(
            "Expense added: " + description
        )

    except ValueError as error:

        print("Error:", error)


def delete_expense(expenses):

    print()
    print("----- Delete Expense -----")

    try:

        expense_id = input("Enter expense ID: ")

        expense = find_expense(expenses, expense_id)

        if expense is not None:

            expenses.remove(expense)

            save_expenses(expenses)

            print("Expense deleted successfully.")

            log_operation(
                "Expense deleted: " + expense["description"]
            )

        else:

            print("Expense not found.")

    except Exception as error:

        print("Error:", error)


def update_expense(expenses):

    print()
    print("----- Update Expense -----")

    try:

        expense_id = input("Enter expense ID: ")

        expense = find_expense(expenses, expense_id)

        if expense is not None:

            print("Expense found.")

            description = input("Enter new description: ")
            description = validate_description(description)

            category = input("Enter new category: ")
            category = validate_category(category)

            amount = input("Enter new amount: ")
            amount = validate_amount(amount)

            date = input("Enter new date (YYYY-MM-DD): ")

            expense["description"] = description
            expense["category"] = category
            expense["amount"] = str(amount)
            expense["date"] = date

            save_expenses(expenses)

            print("Expense updated successfully.")

            log_operation(
                "Expense updated: " + description
            )

        else:

            print("Expense not found.")

    except ValueError as error:

        print("Error:", error)