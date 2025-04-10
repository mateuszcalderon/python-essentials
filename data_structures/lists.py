# Lists are used to store multiple items in a single variable.
# Lists can store different data types, including strings, integers, and even other lists.

pets  = ["Cat", "Dog", "Fish", "Rabbit", "Rat", "Snake"]
critters = list(pets)  # Copying a list to another list.
wildlife = ["Bear", "Elephant", "Lion"]
wildlife.append("Zebra")  # Adding an element to the end of the list.
pets.remove("Dog")        # Removing an element from the list.
"""
wildlife.remove("Kangaroo")  # Trying to remove an element that doesn't exist on a list will raise a ValueError.
"""
# Here are two different ways to remove elements from a list:
pets.pop()   # Removing the last element from the list.
del pets[1]  # Deleting the second element from the list.

# Indexing list:
print(pets[0])  # Output: Cat

print("Printing the 'pets' list: " + str(pets))
print("Printing the 'critters' list: " + str(critters))

fauna = critters + wildlife  # Concatenating lists.
print("Printing the 'fauna' list: " + str(fauna))

# Getting the length of the list using the 'len()' function:
print("'fauna' list length: " + str(len(fauna)))