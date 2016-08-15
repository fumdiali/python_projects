#another guessing game in python3
import random


print("************************")
print("Welcome To My Guess Game")
print("************************")
print()

found = False
attempt = 0
minNum = 1
maxNum = 37
magicNum = random.randint(minNum,maxNum)

name = input("Choose a user name: ")
print("Welcome {}.Let's begin..".format(name))
print("I'm thinking of a number between 1 - 37..")
print("Take 3 guesses of what my number is: ")

while not found and attempt < 3:
    try:
        guess = int(input("> "))
        attempt +=1
        if guess == magicNum:
            found = True
            print("That's correct!")
            print("Thanks for playing")
        if attempt == 3:
            print("You're out of tries!")
            print("The number is {}".format(magicNum))
        elif guess < magicNum:
            print("Nope!Too low!Try again..")
        elif guess > magicNum:
            print("Aargh!Too much!!Try again..")
        else:
            print("You got it in {} tries!".format(attempt))
    except ValueError:
        print("Please,enter a number!")

