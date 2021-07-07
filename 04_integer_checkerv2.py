# Component 3 integer check Version 2

# Function Goes here
def int_check(question):

    error = "Please enter a whole number between 12 " \
            "and 130"

    valid = False
    while not valid:

        # Ask user for number check if valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        # If a integer is not entered display a error message
        except ValueError:
            print(error)


# Main Routine goes here
age = int_check("Age: ")
