# a simple calculator
#            Written by Patrick C. Diali 
#                    Jan 2017
#operation methods
def add(a,b):
  return a + b

def sub(a,b):
  return a - b

def mult(a,b):
  return a * b

def div(a,b):
  return a / b

#main 
def calc():
  name = input("Enter a user name: ")
  print("Hello,"+name.capitalize()+".Ready to calculate?")
  num1 = int(input("Enter a number: "))
  num2 = int(input("And another: "))
  print("What operation do you wish to perform: ")
  ops = int(input('''\t
         a. Addition: press 1
         b. Subtraction: press 2
         c. Multiplication: press 3
         d. Division: press 4 
           > '''))

  if ops == 1:
    print("The SUM is ",add(num1,num2))
  elif ops == 2:
    print(str(num1)+" - "+str(num2)+" = ",sub(num1,num2))
  elif ops == 3:
    print("Alright,let's multiply!Result is ",mult(num1,num2))
  elif ops == 4:
    print(str(num1)+" / "+str(num2)+" = ",div(num1,num2))
  else:
    print("I don't understand")



calc() # call the main method,this runs the program
