# Component 6v2 snack checker

# Function here
def string_check(choice, options):

    for var_list in options:

        is_valid = ""
        chosen = ""

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

# Valid snacks hold list of all snacks
# Valid options for each snack e.g pc for Pita Chips


valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "m", "mms", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

check_snack = "Invalid choice"
while check_snack == "Invalid choice":
    want_snack = input("Do you want to order snacks?: ").lower()
    check_snack = string_check(want_snack, yes_no)

# Loop 6 times
for item in range(0, 6):

    # Ask user for desired snack and put it in lowercase
    desired_snack = input("snack: ").lower()

    # Check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack choice: ", snack_choice)
