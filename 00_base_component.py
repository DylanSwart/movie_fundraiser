# Introduction and instructions


# Function goes here
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


# Main Routine goes here
name = not_blank("Name: ",
                 "Sorry this can't be blank," 
                 "please enter your name")

# Start Loop
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count <= MAX_TICKETS:
    print("You have {} seats "
          "left".format(MAX_TICKETS - count))

    # Get Details
    name = input("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets")

else:
    print("You have sold {} tickets. \n"
          "There are still {} tickets left".format(count, MAX_TICKETS - count))
