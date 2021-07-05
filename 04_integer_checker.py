# Component 3 Integer Checker
# Function Goes here
def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # Ask user for number check if valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response

            else:
                print(error)

        # If a integer is not entered display a error message
        except ValueError:
            print(error)


# Main Routine goes here
age = int_check("Age: ", 12, 130)
