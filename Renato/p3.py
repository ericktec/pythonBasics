""" pedir un numero al usuario y evaluar si es par o impar. 
Solamente imprimir: "es impar"cuando sea impar o "es par" lo opuesto """

num = int(input('Give me a number '))

if (num % 2) == 0:
  print('Is odd!')
else:
  print('is even!')  


# print('Is odd!' if (num % 2) == 0 else 'is even!')
  
