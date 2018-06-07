""" Pedir dos numeros al usuario, realizar la suma, 
si la suma es mayor a 10 salir, si es menor, volver a 
pedir el par de numeros., si se ingresa texto, salir también. """

try:
  while True:
    one = int(input('First number? '))
    two = int(input('Second one? '))
    sum = one + two
    if sum < 10: 
      print(f"The sum is {sum}")
    else:
      break  
except:
  print('this is not a number!!!')
print('bye!')