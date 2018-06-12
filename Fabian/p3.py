

def im_par():

  while True:
      try:
           num=int(input("Introduce numero a probar "))
           if num%2==0:
               print("el numero es par")
               break

      except ValueError:
          print("Inserta solo numeros")
          pass

      pass




im_par()
