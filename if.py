def sample():

 while True:
  num = 39
  guess = int(input("Guess the author's age(e.g. 21):"))

  if guess == num:
        print("Yes! I'm {} years old!".format(num))
        break
  elif guess > num:
        print("Nope!I'm NOT {}!".format(guess))
  elif guess < num:
        print("I'm older than {}..".format(guess))
  else:
        print("Invalid guess..")

 print("Goodbye")

sample()
