class Antenna(object):
        color=''
        logitude=''


class Hair(object):
        color=''
        texture=''


class Eye(object):
        shape=''
        color=''
        size=''

class Object(object):
        color=''
        size=''
        aspect=''
        antennas=Antenna()
        eyes=Eye()
        hair=Hair()

        def floatAction(self):
            print('I\'m floating!')


class newObject(object):
        def floatAction(self):
            print('I\'m floating but different!')

myObject=Object()
mynewObject=newObject()

mynewObject.floatAction()
myObject.color='Rojo'
print(myObject.color)
myObject.floatAction()
