class Subject:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Student:
    Subjects = []
    def __init__(self,name,subjects):
        self.name = name
        for key, value in subjects.items():
            self.Subjects.append(Subject(key, value))
            print(f'{key} added with {value}')

    def getAverage(self):
        promedio = 0
        for x in range (0,len(self.Subjects)):
            promedio += int(self.Subjects[x].score) 
        promedio = promedio/len(self.Subjects)
        print(promedio)
            
