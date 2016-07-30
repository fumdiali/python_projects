class Calc(object):
    #define class to simulate a simple calculator
    def __init__(self):

        #begin with zero
      self.current = 0

    def add(self,amt):
	#add number to current
      self.current += amt

    def getCurrent(self):
      return self.current
