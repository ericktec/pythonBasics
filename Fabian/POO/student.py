class Student(object):
    def __init__(self,name, score):
        self.name=name
        self.score=score
        print(f'hello {name}')

    def print_details(self):
        print(f'name: {self.name}')
        print(f'score: {self.score}')

student1=Student('Fabian', [99,99,100])
student2=Student('AnotherGuy', [12,43,79])

student2.print_details()
