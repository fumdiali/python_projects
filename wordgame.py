print("Welcome to WordGame!")
print("********************")
print("Created by Chukwufumn'anya P. Diali")
print("August,2016")
print()

import random #to enable us generate random words

print("Instructions:")
print("Fill in the blanks to reveal the secret word,guess the letters..")

#random word generator function
def get_random_word():
    words = ["fee","fii","foo","fum"] #list of words
    word = words[random.randint(0,len(words)-1)]
    return word

uname = input("Enter a username: ")
print("Alright,{}. BEGIN!!".format(uname))
get_random_word()

