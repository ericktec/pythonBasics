
''' Functiones '''

'''
  iterativamente se pediran numeros al usuario seguidos por un string que puede ser 
  el signo "+" ó "-". a partir de ahí el siguiente elmento insertado
  se sumará o restará deacuerdo el valor del signo... el programa terminará cuando se inserte
  otro string que sea distinto de + o -

1
+
5
6
=====
9
-
5
4
'''

'''
input >> 5
input >> +
input >> 5
output >> 10
input >> +
input >> 3
output >> 13
input >> -
input >> 1
output >> 12
'''
# add = lambda n1,n2: n1 + n2
def add(n1, n2):
  return n1 + n2

# subtract = lambda n1,n2: n1 - n2
def subtract(n1, n2):
  return n1 - n2

try:
  while True:
    n1 = int(input(''))
    sign = input('')
    n2 = int(input(''))
    print('----')
    if sign == '+':
      print(add(n1,n2))
    elif sign == '-':
      print(subtract(n1,n2))
    else:
      break
    print(' ')
except:
  pass


# ==================== iterative sum extended:
'''

add = lambda n1,n2: n1 + n2
subtract = lambda n1,n2: n1 - n2

n1 = int(input(''))
try:
  while True:
    sign = input('')
    n2 = int(input(''))
    print('----')
    if sign == '+':
      n1 = add(n1,n2)
    elif sign == '-':
      n1 = subtract(n1,n2)
    else:
      break
    print(n1)
except:
  pass

'''