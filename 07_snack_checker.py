# Component 6 snack checker
# Valid snacks hold list of all snacks
# Valid options for each snack e.g pc for Pita Chips

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]


# Initialised variables
snacks_ok = ""
snack = ""

# Loop three times
for item in range(0, 3):

    # Ask user for wanted snacks
    desired_snacks = input("Snacks: ").lower()

    for var_list in valid_snacks:

        # If snacks is in the list return full response
        if desired_snacks in var_list:

            # Get full name of snack in title case
            snack = var_list[0].title()
            snacks_ok = "yes"
            break

        # If chosen snack is not valid
        else:
            snack_ok = "no"
