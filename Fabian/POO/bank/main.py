'''
    Bank Account

'''
class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self, amount):
        self.balance+=amount
        return self.balance
    def withdraw(self, amount):
        self.balance-=amount
        return self.balance

def main():
    bankAccount1=BankAccount()
    while True:
        print('------------------------------------------')
        print('Inserta la opcion deseada:')
        print('a) Depositar')
        print('b) Retirar')
        print('c) Mostrar saldo')
        print('cualquier tecla) SAlIR')
        option=input('...')
        if (option=='a'):
                amount=int(input('inserta la cantidad a depositar... '))
                print(f'Tu saldo es de ${bankAccount1.deposit(amount)}')
        elif(option=='b'):
            amount=int(input('inserta la cantidad a retirar... '))
            if(amount>bankAccount1.balance):
                print('No tienes el saldo suficiente :v')
                print(f'Tu saldo es de ${bankAccount1.balance}')
            else:
                print(f'Tu saldo es de ${bankAccount1.withdraw(amount)}')
        elif(option=='c'):
            print(f'Tu saldo es de ${bankAccount1.balance}')
        else:
            break

main()
