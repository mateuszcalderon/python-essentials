# 'for' Loop in Python:
# The 'for' loop is used to iterate over a sequence of items (e.g., dictionaries, lists, strings).

pets  = ["Cat", "Dog", "Fish", "Rabbit", "Rat", "Snake"]

# A 'for' loop can check conditions for items in a collection.
for pet in pets:
    print(pet)                                    # Prints each pet in the list.
    if pet == "Fish":
        print("Fish is my favorite pet!")         # Prints a message when the pet is 'Fish'.
    elif pet == "Snake":
        print("Snake is my least favorite pet!")  # Prints a message when the pet is 'Snake'.