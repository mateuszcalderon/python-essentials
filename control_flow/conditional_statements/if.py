# 'if' Statement in Python:
# Note: Using 'if' statements independently works, but it's NOT the most efficient approach. However, for learning purposes, this structure helps demonstrate how individual 'if' statements behave.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
operation = input("Enter an operation (+, -, *, /): ")

# When a 'if' statement is true, the rest of the 'if' statements are NOT executed.
if operation == "+":
    print("Result is = " + str(a + b))

if operation == "-":
    print("Result is = " + str(a - b))

if operation == "*":
    print("Result is = " + str(a * b))

if operation == "/":
    print("Result is = " + str(a / b))

# After checking all conditions, normal execution continues.
print("Ending program...")