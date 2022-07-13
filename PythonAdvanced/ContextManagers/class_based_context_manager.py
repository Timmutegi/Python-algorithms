"""
To implement the context management protocol and create class-based context managers, 
you need to add both the .__enter__() and the __exit__() special methods to your classes.

When the with statement executes, it calls .__enter__() on the context manager object to signal that 
you're entering into a new runtime context. If you provide a target variable with the as specifier, 
then the return value of .__enter__() is assigned to that variable.

When the flow of execution leaves the context, .__exit__() is called. If no exception occurs in the with code block, 
then the three last arguments to .__exit__() are set to None. Otherwise, they hold the type, value, 
and traceback associated with the exception at hand.
"""
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep="\n")

def main():
    with HelloContextManager() as hello:
        print(hello)

main()