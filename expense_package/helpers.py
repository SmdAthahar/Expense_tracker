def find_expense(expenses, expense_id):

    for expense in expenses:

        if expense["id"] == expense_id:

            return expense

    return None


def get_total_expenses(expenses):

    total = 0

    for expense in expenses:

        total = total + float(expense["amount"])

    return total