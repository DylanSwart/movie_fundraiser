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

    # Get name can't be blank

    name = not_blank("Name: ",
                     "Sorry this can't be blank," 
                     "please enter your name")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all available tickets")

else:
    print("You have sold {} tickets. \n "
          "There is {} seats still availavle".format(count, MAX_TICKETS - count))

    # Get age have to be between 12 and 130

    # calculate ticket price

    # Loop to ask user for snacks

    # Calculate snacks price

    # ask user for payment method and apply surcharge if needed

# Calculate total sales and profit

# Out put data to text file


