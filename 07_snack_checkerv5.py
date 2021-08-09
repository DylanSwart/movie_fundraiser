# Component 6 snack checker v5
import re


test_strings = [
    "popcorn",
    "2 pc",
    "1.5 oj",
    "4 oj"
]

for item in test_strings:

    # Regular expressions
    number_regex = "^[1-9]"

    # If item has number separate it in twi
    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]

    else:
        amount = 1
        desired_snack = item

    # Remove white space around snack
    desired_snack = desired_snack.strip()

    # If item does not have a number in front set it to 1

    # Print order
    print("Amount: ", amount)
    print("Snack: ", desired_snack)
    print("Length: ", len(desired_snack))
