# Functions in Python - Part 1.
# This 1st Part focuses on introducing the fundamentals of defining and calling functions in Python.

number1 = 10
number2 = 2

"""
# To define a function, we use the keyword 'def' followed by the function name and parentheses.
def function_name():
    instructions
"""

# Defining functions to perform basic operations:
def add_numbers():
    result = number1 + number2
    print("Sum: " + str(result))

def subtract_numbers():
    result = number1 - number2
    print("Subtraction: " + str(result))

def multiply_numbers():
    result = number1 * number2
    print("Multiplication: " + str(result))

def divide_numbers():
    result = number1 / number2
    print("Division: " + str(result))

# To use the functions, we have to call them.
add_numbers()
subtract_numbers()
multiply_numbers()
divide_numbers()

"""
# A function can call another functions.
def calculate():
    add_numbers()
    subtract_numbers()
    multiply_numbers()
    divide_numbers()

calculate()
"""