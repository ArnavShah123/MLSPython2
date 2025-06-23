print("Hello")
def add(a, b):
  print("add = ", a + b)


def sub(a, b):
  print("sub = ", a - b)


def mul(a, b):
  print("mul = ", a * b)


def div(a, b):
  if b==0:
    print("ZeroDivisionError: division by zero")
    return
  print("div = ", a / b)




def exp(a, b):
  print("exp = ", a**b)


def choice():
  print("Choose 1 for addition")
  print()
  print("Choose 2 for subtraction")
  print()
  print("Choose 3 for multiplication")
  print()
  print("Choose 4 for division")
  print()
  print("Choose 5 for exponents")
  print()
  print("Choose 6 for exit")
  print()


def calculator():
  while True:
    choice()
    i = int(input("Enter your choice: "))
    if i == 1:
      add(int(input("Enter a number: ")), int(input("Enter a number: ")))
      print("--------")

    elif i == 2:

      sub(int(input("Enter a number: ")), int(input("Enter a number: ")))
      print("--------")

    elif i == 3:

      mul(int(input("Enter a number: ")), int(input("Enter a number:")))
      print("--------")

    elif i == 4:

      div(int(input("Enter a numerator: ")), int(input("Enter a denominator: ")))
      print("--------")

    elif i == 5:

      exp(int(input("Enter a number: ")), int(input("Enter a number: ")))
      print("--------")

    elif i == 6:
      print("Bye!")
      break
    else:
      print()
      print("Enter Valid choice between 1 and 6.")

calculator()
