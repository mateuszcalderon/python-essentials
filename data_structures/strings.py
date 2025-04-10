# Strings in Python:
# A string is, in short, a "list" of characters that can be manipulated in various ways.

nice_message      = "Python is cool!"
lowercase_message = "python is cool!"
uppercase_message = "PYTHON IS COOL!"
spaced_message    = "  Python is cool!  "

# Indexing and Slicing string:
print(nice_message[0])    # Output: P
print(nice_message[0:6])  # Output: Python
print(nice_message[7:9])  # Output: is
print(nice_message[10:])  # Output: cool!

# Functions and Methods for strings:
# The 'len()' function gives the string's length.
print("len() function: " + str(len(nice_message)))

# The 'lower()' method makes the string lowercase.
print("lower() method: " + uppercase_message.lower())

# The 'upper()' method makes the string uppercase.
print("upper() method: " + lowercase_message.upper())

# The 'strip()' method removes leading and trailing whitespace or specified characters from a string.
print("strip() method: " + spaced_message.strip())

# The 'split()' method divides the string into a list.
print("split() method: " + str(nice_message.split(" ")))

# The 'replace()' method swaps one phrase for another in the string.
print("replace() method: " + nice_message.replace("cool", "awesome"))

# The 'in' operator checks for a substring in a string and returns 'True' or 'False'.
word_to_search = "Python" in nice_message
print(word_to_search)  # Output: True

# The 'not in' operator checks if a substring is absent in a string and returns 'True' or 'False'.
word_to_search = "Python" not in nice_message
print(word_to_search)  # Output: False

# Concatenating strings:
text1 = "Python"
text2 = "is a programming language."
phrase = text1 + " " + text2
print(phrase)

city = "Gotham City"
day = 19
month = "February"
year = 1972
date = "\"{}, {}th {}, {}. Bruce Wayne is born...\""

# The 'format()' method inserts formatted values into curly bracket placeholders.
print(date.format(city, day, month, year))