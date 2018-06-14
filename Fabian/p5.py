def promedio():
    cal=[]
    pregunta=''
    while True:
        cal.append(int(input("Introduce calificacion ")))
        pregunta=(input("Quieres introducior otra calificacion? (y/n) "))
        if((pregunta!='y') ):
            promedio=sum(cal)/len(cal)
            print(f"EL promedio de tus calificaciones es {promedio}")
            break

promedio()
