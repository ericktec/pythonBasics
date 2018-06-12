
class Antenna(object):
    color= ""
    longitud = ""

class Hair(object):
    color = ""
    texture = ""

class Eye(object):
    shape = ""
    color = ""
    size = ""

class Parent(object):
    color = ""
    size = ""
    aspect = ""
    antennas = Antenna()
    eyes = Eye()
    hair = Hair()

    def floatAction(self):
        print('I\' am floating')

class OtherParent(object):
    color = ""
    size = ""
    aspect = ""
    antennas = Antenna()
    eyes = Eye()
    hair = Hair()

    def flyAction(self):
        print('I\' am flying')

class NewObj(Obj):
    def floatAction(self):
        print("I \' am floating but different")

