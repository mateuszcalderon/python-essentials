# Lambda Functions in Python.
# Lambda Functions are small anonymous functions defined using the 'lambda' keyword.

add = lambda a, b: a + b
delta = lambda b, a, c: (b ** 2) - 4 * a * c
print("Sum: " + str(add(4, 6)))
print("Delta: " + str(delta(-5, 1, 6)))
# A Lambda function can be used without being assigned to a variable.
print("Multiplication: " + str((lambda x, y: x * y)(2, 3)))
# A nested Lambda is a Lambda inside another Lambda.
nested_lambda = lambda x: lambda y: x * y
multiply = nested_lambda(2)  # The outer function sets 'x = 2', and the inner function uses it.
print("Nested Lambda: " + str(multiply(3)))