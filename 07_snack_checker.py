# Component 6 snack checker
# Valid snacks hold list of all snacks
# Valid options for each snack e.g pc for Pita Chips

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "m", "mms", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]


# Initialise variables
snack_ok = ""
snack = ""

# Loop program three times
for item in range(0, 3):

    # Ask used for desired snack
    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        # If chosen snack is in valid snacks return full response
        if desired_snack in var_list:

            # Get full name of snack and put it in title case
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        # If chosen snack is not in valid snack set snack ok to no
        else:
            snack_ok = "no"

    # If the snack is not ok ask question again
    if snack_ok == "yes":
        print("Snack choice: ", snack)

    else:
        print("Invalid choice")
