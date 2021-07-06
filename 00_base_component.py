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

    # Get name can't be blank

    name = not_blank("Name: ",
                     "Sorry this can't be blank," 
                     "please enter your name")

    # Get age have to be between 12 and 130

    # calculate ticket price

    # Loop to ask user for snacks

    # Calculate snacks price

    # ask user for payment method and apply surcharge if needed

# Calculate total sales and profit

# Out put data to text file


