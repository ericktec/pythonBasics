# Listas

""" 
  El usuario tendra que introducir valores numericos, los cuales se almacenarán para después sacar el promedio 
  y mostrarlo cuando el valor introducido NO sea numerico

  input > 5
  input > 6
  input > 7
  input > 8
  input > 's'
  output > 'promedio: 6.5'

"""
myList = []
sum = 0
while True:
  num = input('')
  if num.isnumeric():
     sum += int(num)
     myList.append(sum)
  else:
    break
prom = sum / len(myList)
print(f'Promedio: {prom}')