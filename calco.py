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
  print("Hello,"+name.capitalize())
  #roll = input("Ready to calculate?(Y/N)")

  num1 = int(input("Enter a number: "))
  num2 = int(input("And another: "))
  print("What operation do you wish to perform: ")
  ops = int(input('''\t
         a. Addition: press 1
         b. Subtraction: press 2
         c. Multiplication: press 3
         d. Division: press 4
            Press 0 to quit 
           > '''))
  
  if ops == 1:
    print("The SUM is ",add(num1,num2))
  elif ops == 2:
    print(str(num1)+" - "+str(num2)+" = ",sub(num1,num2))
  elif ops == 3:
    print("Alright,let's multiply! Result is ",mult(num1,num2))
  elif ops == 4:
    print(str(num1)+" / "+str(num2)+" = ",div(num1,num2))
  elif ops == 0:
    print("Goodbye!")
  else:
    print("Invalid selection!")



calc() # call the main method,this runs the program
