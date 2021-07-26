# Component 4 Yes No String
def string_checker(question, to_check):

    error = "Please enter Yes or No"

    valid = False
    while not valid:

        # Ask questions and put response in lowercase
        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                # Checks if response is first letter
                # Item List
                if response == item[0]:
                    # Returns the whole response not just the first letter
                    return item

        print("Sorry that wasn't a valid response")


# Main Routine goes here


for item in range(0, 6):
    want_snacks = string_checker("Do you want "
                                 "snacks?: ", ["yes", "no"])
    print("Answer OK, you said: {}".format(want_snacks))
    print()
