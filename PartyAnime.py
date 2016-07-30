#code to practice with Classes and objects

class PartyAnime:
    name = ""
    age = 0
    def guest(self):
      self.name = input("Enter your name:")
      print("Hello, ",self.name)
      self.age = input("How old are you?")


boy = PartyAnime()
girl = PartyAnime()

print("Boys first..")
boy.guest()
print("Now for the girls..")
girl.guest()
print("Thank you both!Good Bye!")
