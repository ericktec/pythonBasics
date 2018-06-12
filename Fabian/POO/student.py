class Student(object):
    def _init_(self,name, score):
        self.name=name
        self.score=score
        print(f'hello {name}')

    def print_details(self):
        print(f'name: {self.name}')
        print(f'score: {self.score}')

student=Student()
