def main(x):
    for i in range(x,0,-1):
        print("*"*x)
        x-=1

def piramide(x):
    while x>0:
        print("*"*x)
        x-=1


while True:
    try:
        num=int(input("Inserta la altura"))
        break
        pass
    except ValueError:
        print("SOlo introduce numeros enteros")
piramide(num)
