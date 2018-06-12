class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
        print("New student")
    def print_details(self):
        print("name %s score %s"%(self.name, self.score))

student = Student("Erick", 342)
student.print_details()
 