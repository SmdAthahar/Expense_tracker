from datetime import datetime


def log_operation(message):

    try:

        current_time = datetime.now()

        with open("expense.log", "a") as file:

            file.write(
                str(current_time) + " - " + message + "\n"
            )

    except Exception as error:

        print("Error while writing log:", error)