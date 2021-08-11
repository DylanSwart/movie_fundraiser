# Import statements
import pandas
import re

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


# Get snack function
def get_snack():

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

    # Holds snack order for one person
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # Ask user for desired snack
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # If item has a number separate it into two
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # Remove white space around snack
        desired_snack = desired_snack.strip()

        # Check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # Check snack amount is less than 5
        if amount >= 5:
            print("Sorry we have a max of 4 snacks")
            snack_choice = "Invalid choice"

        # Add snack and amount to the list

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # Check that snack is not exit code
        if snack_choice != "xxx" and snack_choice != "Invalid choice":
            snack_order.append(snack_row)


# Ticket function
def check_tickets(tickets_sold, ticket_limit):

    # Tell user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats "
              "left".format(ticket_limit - tickets_sold))

    # Warn user if there is one seat left
    else:
        print("There is one seat left")

    return ""


# Profit function
def get_ticket_price():

    # Get age
    age = int_check("age: ")

    # Check if the age is valid
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"

    elif age > 130:
        print("That is very old it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5

    elif age < 65:
        ticket_price = 10.5

    else:
        ticket_price = 6.5

    return ticket_price

# Main routine goes here

# Set up dictionaries / lists needed for data


yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# List of payment options
payment = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# ask user if they have used this program before

# Loop ticket information


name = ""
ticket_count = 0
ticket_sales = 0
MAX_TICKETS = 5

# variables for data frame
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Store surcharge multiplier
surcharge_multi_list = []

# Data Frame dict
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_multi_list
}

# Cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}


while name != "xxx" and ticket_count <= MAX_TICKETS:

    # Check number of tickets limit
    check_tickets(ticket_count, MAX_TICKETS)

    # Get details

    # Get name can't be blank

    name = not_blank("Name: ",
                     "Sorry this can't be blank," 
                     "please enter your name")

    # Ends loop if exit name is given
    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()

    # If age is invalid restart loop
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # Add name and ticket price to the list
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snack

    # Ask user if they want snacks
    check_snack = "Invalid choice"
    while check_snack == "Invalid choice":
        want_snack = input("Do you want snacks?: ").lower()
        check_snack = string_check(want_snack, yes_no)

    # If user input is yes ask what snacks they want
    if check_snack == "Yes":
        snack_order = get_snack()

    else:
        snack_order = []

    # Assume No snacks have been bought
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

            # Get payment method and work out surcharge if needed
            # Ask for payment method
            how_pay = "Invalid choice"
            while how_pay == "Invalid choice":
                how_pay = input("Please choose a payment option (Cash) or (Credit)").lower()
                how_pay = string_check(how_pay, payment)

            if how_pay == "Credit":
                surcharge_multiplier = 0.05

            else:
                surcharge_multiplier = 0

            surcharge_multi_list.append(surcharge_multiplier)

# End of tickets/ snacks/ name loop

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# Create column called Sub Total
# Fill it with price of tickets and snacks

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn'] * price_dict['Popcorn'] + \
    movie_frame['Water'] * price_dict['Water'] + \
    movie_frame['Pita Chips'] * price_dict['Pita Chips'] + \
    movie_frame['M&Ms'] * price_dict['M&Ms'] + \
    movie_frame['Orange Juice'] * price_dict['Orange Juice']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# Shorten snack names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                          'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': 'SM'})

# Set up columns to be printed
pandas.set_option('display.max_columns', None)

# Floats set to 2 dp
pandas.set_option('precision', 2)

print_all = input("Print all Columns? (y) for yes or (n) for no")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total'
                       'Surcharge', 'Total']])

print()

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

# Out put data to text file
