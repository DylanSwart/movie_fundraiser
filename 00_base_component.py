# Introduction and instructions


# Not Blank Function goes here
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

name = ""
count = 0
MAX_TICKETS = 5

# Start of Loop
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
