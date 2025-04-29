# *args and **kwargs in Python.
# *args passes tuples, while **kwargs passes dictionaries to functions.

# *args Example:
def greeting(*args):
    for name in args:
        print("Hello, " + name + "!")

greeting("Freddy", "Jason", "Michael", "Chucky")

# **kwargs Example:
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))

show_info(name="Freddy", age=26, city="Springwood")

# Both *args and **kwargs can be used together in a function definition.
# The following example was provided by b001 at https://www.youtube.com/watch?v=4jBJhCaNrWU.
def order_pizza(size, *toppings, **details):
    print("Ordered a " + size + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

    print("Details of the order are:")
    for key, value in details.items():
        print("- " + key + ": " + str(value))

order_pizza("large", "olives", "pepperoni", delivery=True, tip=5)