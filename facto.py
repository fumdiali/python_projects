# find a number's factorial using recursion

def fact_num(n):
  if n == 1: #base case
    return n
  else:
    return(n * fact_num(n-1) ) #recursive call

# get user input
num = int(input("Enter a number: "))
if num < 0:
  print("Factorial doesn't exist for negative numbers.")
elif num == 0:
  print("Factorial of zero is 1")
else:
  print("Factorial of ",num," is ",fact_num(num))
