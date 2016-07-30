print("Welcome to MatchMakr!")
print("---------------------")

#Gender selection
print("Please select your gender:")
print("Male:1")
print("Female:2")

#Get user choice
sex = input("> ")

#Determine gender
if sex == 1:
    print("You are Male..")
    #for Python3..throws error
    #choice = input("Select your preference(M/F):")
    #works in Python2 and 3
    choice = raw_input("Your preference(M/F):")
    if choice == 'M':
        print("Are you homo or just curious?")
    elif choice == 'F':
        print("What kind of woman do you like?")
    else:
        print("I don't understand your preference!")
elif sex == 2:
    print("You are Female..")
    #for Python3..throws error
    #choice = input("Select your preference(M/F):")
    #for Python2..works in 3 too
    choice = raw_input("Select your preference(M/F):")
    if choice == 'F':
        print("Are you a lez or just curious?")
    elif choice == 'M':
        print("What kind of man interests you?")
    else:
        print("I don't understand your preference..")
else:
    print("Invalid selection(Choose 1 or 2)")


#Python2 input syntax
move = raw_input("Proceed(Y/N)?")
#Python3 input syntax
#move = input("Proceed(Y/N)?")
if move == 'Y':
        print("Let's go..")
elif move == 'N':
        print("Good Bye!")
else:
        print("What do you mean???Please,enter 'Y' or 'N'!")
