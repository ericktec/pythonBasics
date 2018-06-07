def piramidefor():
	height = validacionEnteros("Escribe la altura de la piramide")
	while height<=0:
		height = validacionEnteros("Escribe la altura de la piramide mayor a cero")
	for x in range (height,0,-1):
		print("*"*x)

def piramidewhile():
	height = validacionEnteros("Escribe la altura de la piramide")
	while height<=0:
		height = validacionEnteros("Escribe la altura de la piramide mayor a cero")
	while height >= 1:
		print("*"*height)
		height = height-1

def validacionEnteros(mensaje):
    while True:
        try:
            num=int(input(mensaje))
            break
        except ValueError:
            print("Solo se puede introducir números enteros")
    return num

piramidefor()
piramidewhile()
