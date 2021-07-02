# Introduction and instructions
# Component 1 introduction and instructions
# introduction to the program
print("Welcome to the movie fundraiser \n"
      "Please follow what the program says. \n"
      "there are limit seats of 150 seats available in the theater")


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

