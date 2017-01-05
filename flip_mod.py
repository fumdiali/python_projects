# simple module that reverses the order of given input
##              Written by Patrick C. Diali   Jan 2017
import time


def flip():
  print("\t*"*5)
  print("\t\tWelcome To Flipper!")
  print("\t*"*5)
  print("Type any group of xters(words,letters,numbers)and press ENTER: ")
  name = input()
  
  try:
    flipped = name[::-1]
    print("Let me FLIP it..")
    time.sleep(3)
    print(flipped)
    print("Whoop!There it is!!")
  except Exception as e:
    print(e)

flip()
