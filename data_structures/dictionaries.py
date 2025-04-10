# Dictionaries work using "key": "value" pairs.
# Note: Many functions and methods in this code also work with Lists and Tuples.
 
vehicle = {"Model": "SUV", "Color": "Black", "Transmission": "Automatic", "Year": "2025"}
vehicle["Year"] = "2024"        # Modifying the value of the key "Year".
vehicle["Is Electric?"] = True  # Adding a new key-value pair to the dictionary.

for key, value in vehicle.items():   # Iterating through the dictionary using a 'for' loop.
    print(key + " - " + str(value))  # Printing the key and value.

# Creating a dictionary with nested dictionaries:
vehicles = {"Car1": {
                "Model": "SUV", "Year": "2023"
                },
            "Car2": {
                "Model": "Pickup", "Year": "2022"
                }
}

model1 = {"Model": "Sedan", "Year": "2021"}
model2 = {"Model": "Hatchback", "Year": "2020"}

# Creating a dictionary from two dictionaries:
cars = {
        "Model1": model1,
        "Model2": model2,
}

# Here are two ways to access the value of a key in a dictionary using variables:
vehicle_color = vehicle["Color"]      # Accessing the value using directly the key.
vehicle_color = vehicle.get("Color")  # Using the 'get()' method to access the value of the key "Color".
print(vehicle_color)

# Two different ways to remove a key-value pair from a dictionary:
vehicle.pop("Transmission")  # Removing the key "Transmission" from the dictionary.
del vehicle["Year"]          # Deleting the key "Year" from the dictionary.

print("Printing the 'vehicle' dictionary: " + str(vehicle))
print("Printing the 'vehicles' dictionary: " + str(vehicles))
print("Printing the 'cars' dictionary: " + str(cars))




# The 'len()' function gives the dictionaries' length.
print("'vehicle' dictionary length: " + str(len(vehicle)))
print("'vehicles' dictionary length: " + str(len(vehicles)))
print("'cars' dictionary length: " + str(len(cars)))

"""
The 'clear()' method removes all the items from the dictionary.
vehicle.clear()
"""