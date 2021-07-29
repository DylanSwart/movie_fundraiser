# Component 6v3 snack checker

# Function goes here
def string_check(choice, options):

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
        return "invalid choice"


# Snack List goes here
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "m", "mms", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# Yes/No list here
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
if check_snack == "yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # Ask user for desired snack
        desired_snack = input("snack: ").lower()

        # Exit code
        if desired_snack == "xxx":
            break

        # Check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        print("Snack choice: ", snack_choice)

        # Add snack to list
        # Check if snack is not exit code
        if snack_choice != "xxx" and snack_choice != "Invalid choice":
            snack_order.append(snack_choice)

# Show snack order
print()
if len(snack_order) == 0:
    print("Snacks order: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)
