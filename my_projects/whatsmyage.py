from datetime import datetime

print("************************")
print(" Guess My Age Game ")
print("************************")

#display date and start time
now = datetime.now()
print('%s/%s/%s' % (now.day, now.month, now.year))
print("Login time: %s:%s:%s" % (now.hour, now.minute, now.second))

#prompt user for name
name = input("Enter your username:")

print("Welcome,"+name+".I'm older than 35.Guess how old I am..")

#initialise variable to prevent Python error
my_age = 0

#loop prompt for user action,without input validation
while my_age != 39:
    my_age = input("Enter your guess >")
    if int(my_age) >= 40:
        print("Nope! I'm actually younger than 40!")
    elif int(my_age) <= 38:
        print("Nah!I'm older!Try again..")
    elif int(my_age) == 39:
        print("Correct!I AM 39!Still young,eh?")
        break
    else:
        print("Invalid input")

print("Thanks for playing.Goodbye,"+name)


#print("*-*-*-*-*-*-*-*-*-*-")

#print("Now,let's try one more thing..")
#pick = input("Pick a number between 1 & 2:")
#if type(pick) == 1 or 2:
 #   print("Well done!You chose {}".format(pick))
#else:
 #   print("What have you just done???I said a NUMBER!")

