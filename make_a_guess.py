#another guessing game in python3
# this is the poorly commented version..apologies
import random


print("************************")
print("Welcome To My Guess Game")
print("************************")
print()

found = False
attempt = 0
minNum = 1
maxNum = 30
magicNum = random.randint(minNum,maxNum)

name = input("Choose a user name: ")
print("Welcome {}.Let's begin..".format(name))
print("I'm thinking of a number between 1 and 30..")
print("Take 3 guesses of what my number is: ")

while not found and attempt < 3:
    try:
        guess = int(input("> "))
        attempt +=1
        if guess == magicNum:
            found = True
            print("That's correct!")
            print("You got it in {} tries!".format(attempt))
            print("Thanks for playing")
            break
        if attempt == 3:
            print("You're out of tries!")
            print("The number is {}".format(magicNum))
        elif guess < magicNum:
            if attempt == 2:
                print("Too low!You have one more guess..")
            else:
                print("Nope!Too low!Try again..")
        #elif guess < magicNum:
           # print("Nope!Too low!Try again..")
        elif guess > magicNum:
            if attempt == 2:
                print("Aaargh!Too high!You have one more guess..")
            else:
                print("Too high!Try again..") #print("Aargh!Too much!!Try again..")
        else:
            print("Oops!Something is very wrong!")
    except ValueError:
        print("Please,enter a number!")

