import random #to enable us generate random words
import time # for pause and effect

print("Welcome to WordGame!")
print("********************")
print("Created by Chukwufumn'anya P. Diali")
print("August,2016")
print()


#random word generator function
def get_random_word():
    uname = input("Enter a username: ")
    print("Alright,{}. BEGIN!!".format(uname))
    time.sleep(2)
    print("------------")
    print("Instructions:")
    print("-------------")
    print("I have a 6 letter word..")
    print("Fill in the blanks to reveal the secret word,guess the letters..")
    time.sleep(3)
    print("_ _ _ _ _ _ ")
        
    words = ["fee","fii","foo","fum"] #list of words
    word = words[random.randint(0,len(words)-1)]
    return word


def play_game():
    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()

    while playing:
        strikes += 1
        if strikes >= max_strikes:
            playing = False

    if strikes >= max_strikes:
        print("You lost!")
        print("Go again?")
    else:
        print("You won!Congrats!")

play_game() #starts the entire game


