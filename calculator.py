import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    
    if a <= 0 or b <= 0:
        raise ValueError("Both arguments must be positive for logarithm calculation")
    if a == 1:
        raise ValueError("Base cannot be 1 for logarithm calculation")
    
    
    return math.log(b) / math.log(a)

def exponent(a, b):
    return a ** b

###############

def sub(a, b):
    return a - b
def mul(a, b):

    return a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):# use math library + raise ValueError

    if a <= 0 or b <= 0:
        raise ValueError("Both arguments must be positive for logarithm calculation")
    if a == 1:
        raise ValueError("Base cannot be 1 for logarithm calculation")

    return math.log(b) / math.log(a)


def exp(a, b):
    return a**b
