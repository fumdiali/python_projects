print("*******************")
print("Welcome to my App")
print("*******************")

def mono():
    fname=input("Enter your first name:")
    lname=input("Enter your last name:")


    combo=fname[0].upper()+lname[0].upper()
    print("Hello,{0}.Your monogram is {1}".format(fname,combo))
    print("Thanks for playing. Goodbye!")

mono()
