# Default and Keyword Arguments in Python Functions.
# Default and Keyword Arguments let users set default parameter values and pass arguments by name.

# Default Arguments:
def greeting(user_name="Guest"):
    print("Hello, " + user_name + "!")

greeting()         # Here, the default value "Guest" is used.
greeting("Jason")  # Here, the provided value "Jason" is used.

# Keyword Arguments:
def introduce(name, age, city):
    print("My name is " + name + ", I am " + str(age) + " years old, and I'm from " + city + ".")

introduce(name="Steve", age=25, city="New York City")
introduce(city="Dayton", age=35, name="Bruce")  # Order does NOT matter.