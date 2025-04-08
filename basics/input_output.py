# Input and Output in Python:
# Note: The 'str()' function is used to convert a variable to a string. Otherwise, it will cause a TypeError.

# The following input function stores user input in 'user_name' and prints a greeting using it.
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

# Now, the following inputs are stored as integers in 'n1' and 'n2', respectively.
n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))

# The 'result' variable holds their sum and prints it.
result = n1 + n2
print("\nResult is = " + str(result))