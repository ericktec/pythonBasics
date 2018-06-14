class Subject:
    def __init__(self, name, score):
        self.name=name
        self.score=score


class Student:
    def __init__(self, name, subjects):
        self.name=name
        self.Subjects=[]
        self.s=subjects
        for key, value in subjects.items():
            self.Subjects.append(Subject(key, value))
            print(f'{key} added with {value}')

        print(f'hello {name}')
    def getAverage(self):
        cal=[]
        for key, value in self.s.items():
            cal.append(value)

        return sum(cal)/len(cal)


    #def print_details(self):
        #print(f'name: {self.name}')
        #print(f'score: {self.score}')
    #def getAverage(self):
        #return sum(self.score)/len(self.score)
