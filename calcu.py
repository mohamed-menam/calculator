import math


def addition(x, y):
    """
    Parameters
    ----------
    x:float
       any number
    y:float
       any number
    return addition of  x ,y
    """
    return x+y


def subtraction(x, y):
    """
    Parameters
    ----------
    x:float
       any number
    y:float
       any number
    return subtraction of x ,y
    """
    return x-y


def multiplication(x, y):
    """
    Parameters
    ----------
    x:float
       any number
    y:float
       any number
    return multiplication of  x ,y
    """
    return x*y


def division(x, y):
    """
    Parameters
    ----------
    x:float
       any number
    y:float
       any number
    return division of x ,y
    """
    return x/y


def square(x):
    """
    Parameters
    ----------
    x:float
       any number
    y:float
       any number
    return squareroot of x 
    """
    return math.sqrt(x)


def power(x, y):
    """
    Parameters
    ----------
    x:float
       any number
    y:float
       any number
    return power x of y
    """
    return x**y


operations = ["+", "-", "/", "*", "**", "~"]
for o in operations:
    print(o)

operation = input("Enter  operation type :")
if operation == "~":
    number = float(input("Enter the number :"))
    print(square(number))

numbers = input("Enter the numbers :").split()
try:
    i, j = numbers
    x, y = float(i), float(j)
except ValueError:
    print("error.. please enter 2 number")

try:
    if operation == "+":
        print(addition(x, y))
    elif operation == "-":
        print(subtraction(x, y))
    elif operation == "/":
        try:
            print(division(x, y))
        except ZeroDivisionError:
            print("number not division by zero")
    elif operation == "*":
        print(multiplication(x, y))
    elif operation == "**":
        print(power(x, y))
    else:
        print("the operation is not find")
except NameError:
    print("..")
