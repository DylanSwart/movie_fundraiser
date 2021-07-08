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


# Main routine goes here

# Set up dictionaries / lists needed for data

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
