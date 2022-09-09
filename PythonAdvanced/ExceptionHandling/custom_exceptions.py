"""
Defining your own exception types will state your code's intent 
more clearly and make it easier to debug.

Derive your custom exceptions from Python's built-in Exception
class or from more specific exception classes like ValueError or 
KeyError
"""
class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)

validate('jane')