# 'break', 'continue', and 'pass' Statements in Python:
# The 'break' statement exits a loop, the 'continue' skips to the next iteration, and the 'pass' does nothing.

break_list = [2, 4, 5, 6, 8, 10, 12]
continue_list = [2, 4, 6, 8, 9, 10, 12]

# 'break': Exits a loop immediately.
print("'break' Statement:")
for numbers in break_list:
    if numbers % 2 != 0:  # Check if the number is NOT even.
        print("There is an odd number in the list!")
        break
    else:
        print(numbers, end=" ")  # The 'end= " "' argument keeps output on the same line instead of starting a new one.
else:
    print("There are NO odd numbers in the list!")

# 'continue': Skips the current iteration and moves to the next.
print("\n'continue' Statement:")
for numbers in continue_list:
    if numbers % 2 != 0:
        print("An odd number has been ignored!")
        continue
    else:
        print(numbers, end=" ")

# 'pass': Does nothing; a placeholder for future code.
def my_function():
    pass