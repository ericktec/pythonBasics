
def suma():
    while True:
        try:
            num1=int(input("Dame el primer numero a sumar"))
            num2=int(input("Dame el segundo numero a sumar"))
            sum=num1+num2
            print("El resultado de la suma es %d" % sum)
            if sum>10:
                break
            pass
        except ValueError:
            print("HA habido un error")
            break





suma()
