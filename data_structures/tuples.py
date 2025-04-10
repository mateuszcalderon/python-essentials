# Tuples are immutable Lists.
# And like Lists, Tuples can contain different data types.

sample_tuple = (1, 3, 5, 7, 9, "a", "b", "c", False)
vehicles = ("Bicycle", "Bus", "Car", "Motorcycle")
"""
Trying to add, rename or remove an item from a Tuple will cause a TypeError because Tuples are immutable.
vehicles.append("Truck")
vehicles[3] = "Tractor"
vehicles.remove("Car")
"""
# Just like a List, you can access elements in a Tuple using index.
print(vehicles[0])  # Output: Bicycle
print("Printing the 'sample_tuple' tuple: " + str(sample_tuple))
print("Printing the 'vehicles' tuple before using Type Casting: " + str(vehicles))

# We can indirectly modify a Tuple by converting it to a List and then back to a Tuple. All this using a Type Casting conversion.
# It is NOT recommended to do this, but it is possible.
vehicles_list = list(vehicles)   # Converting Tuple to List.
vehicles_list[3] = "Tractor"     # Modifying the List.
vehicles = tuple(vehicles_list)  # Converting the List back to Tuple.
print("Printing the 'vehicles' tuple after using Type Casting: " + str(vehicles))

# The 'len()' function gives the tuple's length.
print("'vehicles' tuple length: " + str(len(vehicles)))