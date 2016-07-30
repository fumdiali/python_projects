
def calc():
    nums = [1,2,3,4,5]
    for i in nums:
      print(i,"...")
    for x in range(6,11):
      print("and ",x)

calc()


def say_hi_to():
    name = input("Enter your username:")
    print("Hello,",name,"!")

say_hi_to()

def tunums():
    print("Enter 2 numbers:")
    num1 = input()
    num2 = input()
    num1 = int(num1)
    num2 = int(num2)
    both = num1 + num2
    print("The sum of your numbers is:",both)

tunums()
