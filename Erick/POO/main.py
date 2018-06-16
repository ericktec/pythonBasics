class BankAccount :
    def __init__(self):
        self.balance = 0

    def desposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def witdraw(self, amount):
        while amount>self.balance:
            try:
                amount = int(input("Introduce un valor valido para hacer tu retiro "))
            except ValueError:
                amount = amount
            
        self.balance -= amount
        return self.balance

def validateInput(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Solo puede introducir numeros enteros")




print("Si desea hacer un deposito presione la tecla 1")
print("Si desea hacer un retiro presione la tecla 2")
print("si desea ver el estado de cuenta presione la tecla 3")
print("si desea salir presiones la tecla 4")
bankAccount = BankAccount()
opcion = validateInput("")
while opcion > 4 or opcion < 1 :
    opcion = validateInput("Introduzca una opcion valida ")
while opcion <= 3 :
    if(opcion == 1):
        bankAccount.desposit(validateInput("Introduce la cantidad que deseas depositar "))

    elif (opcion == 2):
        if (bankAccount.balance == 0):
            print("No tiene dinero")
        else:
            bankAccount.witdraw(validateInput("Introduzca la cantidad que deseas retirar "))

    elif (opcion == 3):
        print("Tu estado de cuenta es de ", bankAccount.balance)

    print("Si desea hacer un deposito presione la tecla 1")
    print("Si desea hacer un retiro presione la tecla 2")
    print("si desea ver el estado de cuenta presione la tecla 3")
    print("si desea salir presiones la tecla 4")
    opcion = int(input())
    while opcion > 4 or opcion < 1 :
        opcion = validateInput("Introduzca una opcion valida ")