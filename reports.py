from expense_package.helpers import get_total_expenses
from logger import log_operation



def monthly_summary(expenses):

    print()
    print("----- Monthly Summary -----")

    month = input("Enter month (YYYY-MM): ")

    total = 0

    for expense in expenses:

        if expense["date"].startswith(month):

            total = total + float(expense["amount"])

    print("Month:", month)
    print("Total Expenses:", total)

    log_operation(
        "Monthly summary generated for " + month
    )


def category_summary(expenses):

    print()
    print("----- Category-wise Summary -----")

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = float(expense["amount"])

        if category in categories:

            categories[category] = (
                categories[category] + amount
            )

        else:

            categories[category] = amount

    for category in categories:

        print(
            category,
            ":",
            categories[category]
        )

    log_operation("Category-wise summary generated")


def highest_expense(expenses):

    print()
    print("----- Highest Expense -----")

    if len(expenses) == 0:

        print("No expenses available.")

        return

    highest = expenses[0]

    for expense in expenses:

        if float(expense["amount"]) > float(highest["amount"]):

            highest = expense

    print("ID:", highest["id"])
    print("Description:", highest["description"])
    print("Category:", highest["category"])
    print("Amount:", highest["amount"])

    log_operation("Highest expense checked")


def export_report(expenses):

    print()
    print("----- Export Report -----")

    try:

        total = get_total_expenses(expenses)

        with open("expense_report.txt", "w") as file:

            file.write("PERSONAL EXPENSE REPORT\n")
            file.write("=======================\n\n")

            for expense in expenses:

                file.write(
                    "ID: " + expense["id"] + "\n"
                )

                file.write(
                    "Date: " + expense["date"] + "\n"
                )

                file.write(
                    "Description: "
                    + expense["description"]
                    + "\n"
                )

                file.write(
                    "Category: "
                    + expense["category"]
                    + "\n"
                )

                file.write(
                    "Amount: "
                    + expense["amount"]
                    + "\n"
                )

                file.write("-----------------------\n")

            file.write(
                "\nTotal Expenses: "
                + str(total)
            )

        print("Report exported successfully.")

        log_operation("Expense report exported")

    except Exception as error:

        print("Error while exporting report:", error)


def generate_monthly_report(expenses):

    try:

        month = input(
            "Enter month for report (YYYY-MM): "
        )

        total = 0

        with open(
            "monthly_report.txt",
            "w"
        ) as file:

            file.write(
                "MONTHLY EXPENSE REPORT\n"
            )

            file.write(
                "======================\n\n"
            )

            file.write(
                "Month: " + month + "\n\n"
            )

            for expense in expenses:

                if expense["date"].startswith(month):

                    file.write(
                        expense["description"]
                        + " - "
                        + expense["amount"]
                        + "\n"
                    )

                    total = total + float(
                        expense["amount"]
                    )

            file.write(
                "\nTotal: " + str(total)
            )

        print(
            "Monthly report generated successfully."
        )

        log_operation(
            "Monthly report generated for " + month
        )

    except Exception as error:

        print("Error:", error)