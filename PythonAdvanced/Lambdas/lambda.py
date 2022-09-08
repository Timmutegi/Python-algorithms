"""
Lambda keyword in Python provides a shortcut for declaringsmall anonymous functions

Lambda functions do not use regular Python statements and always include an implicit return statement
"""

# Example 1
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x:x[1]))

# Example 2
add = lambda x, y: x + y
print(add(5, 3))

# Example 3
sorted(range(-5, 6), key=lambda x: x * x)