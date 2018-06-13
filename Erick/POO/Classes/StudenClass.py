class Student(object):
    __number = 0
    def increment(self):
        self.__number += 1
    def getNumber(self):
        return self.__number
    def __init__(self,name,score):
        self.name = name
        self.score = score
        print("New student")
    def print_details(self):
        print("name %s score %s"%(self.name, self.score))
    def getAverage(self):
        return sum(self.score)/len(self.score)
