import math

def CalcularRaiz(numero):
    if numero<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(numero)

op1 = int(input("Introduce un valor"))
try:
    print(CalcularRaiz(op1))
except ValueError as NegativeError:
    print(NegativeError)

print("El programa ha finalizado")
