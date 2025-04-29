# Functions in Python - Part 2.
# Adding arguments to functions. Arguments are values that are passed to a function when it is called.

def add_numbers(number1, number2, number3):
    result = number1 + number2 + number3
    print("Sum: " + str(result))

add_numbers(10, 5, 25)
add_numbers(2, 12, 22)
add_numbers(1, 1, 1)

"""
# This will raise a TypeError because the function expects 3 arguments:
add_numbers(1, 2, 3, 4)
"""