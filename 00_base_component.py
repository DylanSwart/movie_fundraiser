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
count = 0
MAX_TICKETS = 5

while name != "xxx" and count <= MAX_TICKETS:

    # Tells user how many seats are left
    if count < 4:
        print("You have {} seats "
              "left".format(MAX_TICKETS - count))

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

    count += 1

    # End of ticket loop

# Calculate profits ETC
if count == MAX_TICKETS:
    print("You have sold all available tickets")

else:
    print("You have sold {} tickets. \n "
          "There is {} seats still available".format(count, MAX_TICKETS - count))

    # calculate ticket price

    # Loop to ask user for snacks

    # Calculate snacks price

    # ask user for payment method and apply surcharge if needed

# Calculate total sales and profit

# Out put data to text file
