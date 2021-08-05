# Import statements

# Functions go here

# Not blank function

def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)

# integer checker function


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

# String check function goes here


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
        return "Invalid choice"

# Main routine goes here

# Set up dictionaries / lists needed for data


yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "m", "mms", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

# ask user if they have used this program before

# Loop ticket information


name = ""
ticket_count = 0
ticket_sales = 0
MAX_TICKETS = 5

while name != "xxx" and ticket_count <= MAX_TICKETS:

    # Tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats "
              "left".format(MAX_TICKETS - ticket_count))

    # Warns user that there is one seat left
    else:
        print("There is ONE seat left")

    # Get details

    # Get name can't be blank

    name = not_blank("Name: ",
                     "Sorry this can't be blank," 
                     "please enter your name")

    # Ends loop if exit name is given
    if name == "xxx":
        break

    # Gets user age between 12 and 130
    age = int_check("Age: ")

    # Checks if age is valid
    if age < 12:
        print("Sorry you are to young to view this movie")
        continue

    elif age > 130:
        print("That is very old it looks like a mistake")
        continue

    if age < 16:
        ticket_price = 7.5

    elif age < 65:
        ticket_price = 10.5

    else:
        ticket_price = 6.5

    print("{} : ${:.2f}".format(name, ticket_price))

    ticket_count += 1
    ticket_sales += ticket_price

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
    if check_snack == "Yes":

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

# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Profit from Tickets: ${:.2f}".format(ticket_profit))

# End of ticket loop

# Calculate profits ETC
if ticket_count == MAX_TICKETS:
    print("You have sold all available tickets")

else:
    print("You have sold {} tickets. \n "
          "There is {} seats still available".format(ticket_count, MAX_TICKETS - ticket_count))

    # calculate ticket price

    # Loop to ask user for snacks

    # Calculate snacks price

    # ask user for payment method and apply surcharge if needed

# Calculate total sales and profit

# Out put data to text file
