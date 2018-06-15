
''' hacer un robot que responda hola y despues espera un tema
y despues da un speech y despues pedir otro tema'''
from datetime import datetime

class Robot:
    def __init__(self):
        self.answers = {
            'Hello': ' Hola,Como puedo ayudarte?',
            'Como estas?': 'Muy bien, gracias',
            'Que hora es?':datetime.now().time()}
        print('Hola')
        self.chat()

    def pregunta(self,entrada):
        return self.answers[entrada]

    def chat(self):
        while True:
            entrada = input('..')
            if (entrada == 'adios'):
                print("Adios, :v")
                break
            try:
                print(self.pregunta(entrada))
            except:
                print('No se de que hablas')

a = Robot()
