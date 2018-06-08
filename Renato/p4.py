''' 
El usuario introduce dos valores un texto y un numero.
Si el texto es igual a "Suma" y el numero es mayor a 10 imprimir la sumatoria de si mismo 
hasta llegar a ser mayor o igual a 100.
la sumatoria: 11 + 11 + 11 ....
en pantalla se visualizaría:
11
22
33
44
..
99
cualquier caso diferente de entrada salir del programa.

 '''
# sinle line comment

num = int(input('The number: '))
string = input('The action: ')
if num > 10 and string == 'suma':
  sum = num
  while sum <= 100:
    print(sum)
    sum += num # sum = sum + num