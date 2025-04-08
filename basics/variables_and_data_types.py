# Variables and Data Types in Python:
# Note: Unlike other programming languages, Python does NOT require you to declare the type of a variable when you create it.

# Variables in Python:
global_variable = "I am a Global Variable."  # Global Variables can be accessed from anywhere in the code.

def my_function():
    local_variable = "I am a Local Variable."  # Local Variables can only be accessed within the function they are defined in.
    # To modify a Local Variable to Global Variable inside a function, you need to declare it as 'global'.
    global turn_variable_global
    turn_variable_global = "Now I am a Global Variable."
    print(local_variable)   # This will work because 'local_variable' is defined in the same scope.
    print(global_variable)  # This will also work because 'global_variable' is defined in the global scope.

"""
print(local_variable)  # This will cause a NameError because 'local_variable' is NOT defined in this scope."
"""

my_function()
print(turn_variable_global)  # This will work because 'turn_variable_global' is now a Global Variable.

# Data Types in Python:
boolean = True  # Boolean variables can be either 'True' or 'False'.
"""
Complex Numbers in Python:
# Create a complex number:
x = 3 + 4j

# Accessing the real and imaginary parts:
print(x.real)  # Output: 3
print(x.imag)  # Output: 4
"""
dictionary = {"name": "Bruce", "age": 28}  # Dictionaries are "key": "value" pairs.
float_number = 3.14   # Floating point numbers are used for decimal values.
integer = 1991  # Integer numbers are whole numbers.
l = [1, 3, 5, 7, 9, "a", "b", "c", False]  # Lists can contain different data types.
s = {1, 2, 2, 3, 4, 5, 5, 5, 6}  # Sets are unordered collections of unique elements.
string = "Alfred"  # Strings are sequences of characters.
t = (1, 3, 5, 7, 9, "a", "b", "c", False)  # Tuples are immutable Lists.
"""
t[0] = 10  # This will cause a TypeError because Tuples are immutable.
"""

# Change the 'boolean' variable to another Data Type to check different Data Types:
# e.g., print("\nType: " + str(type(t)))
print("\nType: " + str(type(boolean)))