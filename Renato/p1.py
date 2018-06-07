
try:
  height = input("Enter the height: ")
  while True:
    height = int(height)
    while height > 0:
      print("*" * height)
      height -= 1
    height = input("Another height: ")
except:
  print('Wow is not a number!')