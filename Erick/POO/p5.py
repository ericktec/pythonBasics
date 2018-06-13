def promedio():
    calificaciones = []
    sum = 0
    while True:
        num = input("Intorduce un valor")
        if num.isnumeric():
            calificaciones.append(int(num))
            sum += int(num) 
        else:
            prom = sum/ len(calificaciones)
            print("El promedio es %1.4f"%(prom))
            break
promedio()