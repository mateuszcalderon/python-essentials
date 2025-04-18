# 'while' Loop in Python:
# Note: 'while' loops run until a condition changes, ideal for unpredictable iterations.

count = 0
while (count <= 5):
    print("Count: " + str(count))
    count += 1

"""
# We can create a countdown using the '-=' operator.
count = 5
while count > 0:
    print("Countdown: " + str(count))
    count -= 1
"""

# We can also use 'while' loops to iterate over a collection of items, but keep in mind it's less efficient than a for loop.
# It is NOT recommended to do this, but it is possible.
pets  = ["Cat", "Dog", "Fish", "Rabbit", "Rat", "Snake"]

pets_length = len(pets)
pet = 0
while (pet < pets_length):
    print(pets[pet])  # Prints each pet in the list.
    pet += 1

# A 'while' loop can dynamically populate a collection of items as conditions change.
vehicles = []
vehicle = input("Enter a vehicle: ")
while vehicle != "-1":                        # Continues until the user enters '-1'.
    vehicles.append(vehicle)                  # Adds the vehicle to the list.
    vehicle = input("Enter a new vehicle: ")  # Prompts for another vehicle.

for x in vehicles:  # Iterates through the list of vehicles.
    print(x)        # Prints each vehicle in the list.