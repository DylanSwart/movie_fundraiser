# Component 5 Yes No String
def yes_no(question):

    error = "Please enter Yes or No"

    valid = False
    while not valid:

        # Ask questions and put response in lowercase
        response = input(question).lower()

        if response == "yes" or response == "Y":
            return "yes"
        elif response == "no" or response == "N":
            return "no"
        else:
            print(error)

# Main Routine goes here


for item in range(0, 6):
    want_snacks = yes_no("Do you want snacks: ")
    print("Answer OK, you said: {}".format(want_snacks))
    print()
