# Introduction and instructions
print("Welcome to the movie fundraiser")
# Ask if they have used this before
intro = input("Have you used this program before? ")
instructions = ("How To Use, \n"
                "When asked a question please enter what it is asking")

if intro == "Yes":
    print("Ok welcome back")

elif intro == "No":
    print(instructions)

else:
    print("That was not an option please try again")
