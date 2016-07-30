#from random import randint
'''cant get this to work
in python3'''
import sys
print("Welcome to Guesser!")
print("-------------------")

'''def selection():
    choice = input("Enter a number b/w 1 and 10:")

    if choice == 7:
      print("Nice! You guessed {}! That's my lucky number..".format(choice))
    else:
      print("Sorry,{} is not the right number. Try again.".format(choice))

selection()'''
def main():
    name = input("Enter your username:")
    print("Welcome,{}.Are you ready to play?".format(name))
    myAge = 39
    found = False

    while not found:
      userNum = input("Guess a number between 1 and 50:")
      if userNum == myAge:
        print("Correct!That's how old i am!")
        found = True
        #break
      elif userNum >= 40:
        print("Too high!Lower..")
      elif userNum <= 38:
        print("Too low..higher..")
      else:
        print("Enter a number,please..")

#if __name__ == "__main__":
    #main()
main()
