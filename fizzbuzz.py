# simple fizzbuzz program

print("*\t\t" *5)
print("\t\t\tA simple 'FizzBuzz' interpretation")
print("*\t\t" * 5)

for count in range(1, 100):
  if count % 3 == 0 and count % 5 == 0:
    print("FizzBuzz!")
  elif count % 3 == 0:
    print("Fizz..")
  elif count % 5 == 0:
    print("Buzz..")
  else:
    print(count)

print("That's all,folks!")
