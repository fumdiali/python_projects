# simple maze,console-game

import time

print("*******************")
print(" ~  My House  ~  ")
print("*******************")


print("   __________||__   ")
print("  /              \   ")
print(" /            ___ \  ")
print(" |      ___   |_| |  ")
print(" |______| |_______|  ")
print("")


def comeIn():
    entrance = input("Do you wish to enter?(Y/N)").upper()
    if entrance == 'Y':
        hall()
    else:
        game_over()

def hall():
    name = input("Enter your user name: ")
    choice = input("Welcome {}.There are 2 doors 'A' and 'B',pick one: ".format(name)).upper()
    time.sleep(1)
    if choice == 'A':
        doorOne()
    elif choice == 'B':
        doorTwo()
    else:
        print("Invalid choice!")

def game_over():
    print("Shame.Goodbye!")

def doorOne():
    print("You chose Door One!Enter..")
    print("It is a dusty bedroom,without a bed.In a corner is an old,wooden chair.In it sits an old woman..")
    challenge = input("'What is 2 plus 2',she asks. > ")
    time.sleep(1)
    if str(challenge) == '4':
        print("That's correct!")
    else:
        print("Wrong!You must be punished!")

def doorTwo():
    print("You chose Door Two!Enter..")
    print("You enter a dark room,pitch black.A deep voice speaks..")
    challenge2 = input("'What is the national currency of Nigeria?' > ")
    time.sleep(1)
    if challenge2 == 'naira':
        print("That's correct!")
    else:
        print("Wrong!It's the Naira!")
#main game starts here
comeIn()

