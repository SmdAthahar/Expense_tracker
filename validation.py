def validate_amount(amount):

    try:

        amount = float(amount)

        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        return amount

    except ValueError:
        raise ValueError("Please enter a valid amount.")


def validate_category(category):

    category = category.strip()

    if category == "":
        raise ValueError("Category cannot be empty.")

    return category


def validate_description(description):

    description = description.strip()

    if description == "":
        raise ValueError("Description cannot be empty.")

    return description