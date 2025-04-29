# Functions in Python - Part 3.
# Returning values from functions.

number1 = 5
number2 = 10

def add_numbers(number1, number2):
    result = number1 + number2
    # The 'return' statement allows a function to provide a value back to the code that called it.
    return result

print("Sum: " + str(add_numbers(number1, number2)))

"""
# You can also assign the output of a function to a variable and then display it.
sum_result = add_numbers(number1, number2)
print("Sum: " + str(sum_result))
"""