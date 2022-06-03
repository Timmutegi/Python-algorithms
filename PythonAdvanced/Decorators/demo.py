# Python decorators allow you to change the behavior of a function without modifying the function itself

# Here is the syntax of a basic Python decoator
def my_decorator_func(func):
    def wrapper_func():
        # Do something before the function
        func()
        # Do something after the function
    return wrapper_func

"""
We use a decorator by placing the name of the decorator
directly above the function we want to use it on.
You prefix the decorator function with an @ symbol
"""

@my_decorator_func
def my_func():
    pass