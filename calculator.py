"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/patsofatso/lab11-BT-JY
# Partner 1: Brandon Tran
# Partner 2: Jacob Young

# First example
import math

# <<<<<<< HEAD
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")

    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
# >>>>>>> ba688b471595ca1b590041d08438c36e7f727e2b
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero")
    return b / a

def logarithm(a, b):
    if a == 0 or b == 0:
        raise ValueError("outside domain")
    elif a < 0 or b < 0:
        raise ValueError("outside domain")
    return math.log(b, a)


def exponent(a, b):
    return a**b