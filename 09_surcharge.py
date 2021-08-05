# Component 8 Surcharge
import pandas

# Function goes here


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

# Main Routine


payment = [
    ["cash", "ca"],
    ["credit", "cr"]
]


# Loop until exit code is given
name = ""
while name != "xxx":
    name = input("Name: ")

    if name == "xxx":
        break

    # Ask for payment method
    how_pay = "Invalid choice"
    while how_pay == "Invalid choice":
        how_pay = input("Please choose a payment option (Cash) or (Credit)").lower()
        how_pay = string_check(how_pay, payment)

    # Ask for subtotal
    subtotal = float(input("Sub Total: $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal

    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Sub Total: ${:.2f} | Surcharge: ${:.2f} |"
          "Total payable: ${:.2f}".format(name, subtotal, surcharge, total))
