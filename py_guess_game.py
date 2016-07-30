#using Python3
from datetime import datetime

print("*********************")
print(" Guess My Age Game ")
print("*********************")

#display time and date
now = datetime.now()
print("%s-%s-%s" % (now.day,now.month,now.year))
print("Login time:%s:%s:%s" % (now.hour,now.minute,now.second))

#user input value validation
def user_input(message):
    age = 0
    
    while True:
        try:
            age = int(input(message))
        except ValueError:
            print("Please,enter just a number!")
            continue
        else:
            return age
            break

#Main program starts here
name = input("Enter your username:")
print("Hello,"+name+".I'm older than 35.")
my_age = 0

#loop through user's guesses,break out when my_age == 39
while my_age !=39:
    my_age = user_input("Guess my age > ")
    if my_age >= 40:
        print("I'm actually YOUNGER than 40..")
        
    elif my_age <= 38:
        print("Nah!I'm older..")
        
    else:
        print("Correct!You got it!!")
        break

print("Thanks for playing.Goodbye,"+name+"!!")
