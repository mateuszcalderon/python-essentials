# 'if', 'elif', 'else' Statements in Python:
# Unlike the 'if.py' example, this structure checks multiple conditions in one block, executing the first 'True' case while skipping the rest.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    print("Result is = " + str(a + b))
elif operation == "-":
    print("Result is = " + str(a - b))
elif operation == "*":
    print("Result is = " + str(a * b))
elif operation == "/":
    print("Result is = " + str(a / b))
else:
    print("Invalid operation!")

temperature_condition = "hot"
weather = "sunny"

# The 'and' operator returns 'True' only if both conditions being evaluated are 'True'.
if weather == "sunny" and temperature_condition == "hot":
    print("Great day for a picnic!")  # Both conditions are true, so this message is printed.
else:
    print("Good day for a movie!")    # At least one condition being false, this message is printed.

"""
# The 'or' operator returns 'True' if at least one of the conditions being evaluated is 'True'.
if weather == "sunny" or temperature_condition == "hot":
    print("Good day for a picnic!")   # At least one condition is true, so this message is printed.
else:
    print("Great day for a movie!")   # Both conditions being false, this message is printed.
"""
# Dive into my Truth Table on GitHub: https://github.com/mateuszcalderon/python-essentials