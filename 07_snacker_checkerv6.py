# Component 6 snack checker version 6
import re


def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # If the snack is in the list return full response
        if choice in var_list:

            # Get full name of snack and put it in title case
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # If chosen option is not valid set to no
        else:
            is_valid = "no"

    # If snack is not ok ask question again
    if is_valid == "yes":
        return chosen

    else:
        return "Invalid choice"


# Regular expressions
number_regex = "^[1-9]"

# Snack list
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "m", "mms", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "c"]
]

# Yes_no list
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Holds snack order for one person
snack_order = []

# Ask user if they want snacks
check_snack = "Invalid choice"
while check_snack == "Invalid choice":
    want_snack = input("Do you want snacks?: ").lower()
    check_snack = string_check(want_snack, yes_no)

# If user input is yes ask what snacks they want
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # Ask user for desired snack
        desired_snack = input("snack: ").lower()

        snack_row = []

        # Exit code
        if desired_snack == "xxx":
            break

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # Remove white space around desired snack
        desired_snack = desired_snack.strip()

        # Check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # Check if snack number is valid
        if amount >= 5:
            print("Sorry we have a max of 4 snacks")
            snack_choice = "Invalid choice"

        # Add snack to list
        amount_snack = "{} {}".format(amount, snack_choice)

        # Add snack and amount to list

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # Check if snack is not exit code
        if snack_choice != "xxx" and snack_choice != "Invalid choice":
            snack_order.append(snack_row)

# Show snack order
print()
if len(snack_order) == 0:
    print("Snacks order: None")

else:
    print("Snacks Ordered: ")

    '''for item in snack_order:
        print(item)
        '''

    print(snack_order)
