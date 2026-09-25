from expenses import (
    load_expenses,
    add_expense,
    delete_expense,
    update_expense
)

from reports import (
    monthly_summary,
    category_summary,
    highest_expense,
    export_report,
    generate_monthly_report
)

from logger import log_operation



def display_menu():

    print()
    print("==============================")
    print("      PERSONAL EXPENSE TRACKER")
    print("==============================")

    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Update Expense")
    print("4. Monthly Summary")
    print("5. Category-wise Summary")
    print("6. Highest Expense")
    print("7. Export Report")
    print("8. Generate Monthly Report")
    print("9. Exit")

    print("==============================")


expenses = load_expenses()

log_operation("Expense Tracker started")



while True:

    display_menu()

    try:

        choice = int(
            input("Enter your choice: ")
        )

        if choice == 1:

            add_expense(expenses)

        elif choice == 2:

            delete_expense(expenses)

        elif choice == 3:

            update_expense(expenses)

        elif choice == 4:

            monthly_summary(expenses)

        elif choice == 5:

            category_summary(expenses)

        elif choice == 6:

            highest_expense(expenses)

        elif choice == 7:

            export_report(expenses)

        elif choice == 8:

            generate_monthly_report(expenses)

        elif choice == 9:

            log_operation(
                "Expense Tracker closed"
            )

            print(
                "Thank you for using Expense Tracker."
            )

            break

        else:

            print(
                "Invalid choice. Please enter 1 to 9."
            )

    except ValueError:

        print(
            "Please enter a valid number."
        )

    except Exception as error:

        print(
            "Something went wrong:",
            error
        )

        log_operation(
            "Unexpected error: "
            + str(error)
        )