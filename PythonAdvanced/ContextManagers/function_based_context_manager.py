"""
Python's generator functions and the contextlib.contextmanager decorator provide an alternative and 
convenient way to implement the context management protocol. If you decorate an appropriately coded 
generator function with @contextmanager, then you get a function-based context manager that automatically 
provides both required methods, .__enter__() and .__exit__(). This can make your life more pleasant 
by saving you some boilerplate code.
"""
from contextlib import contextmanager

@contextmanager
def hello_context_manager():
    print("Entering the context...")
    yield("Hello, World!")
    print("Leaving the context...")

def main():
    with hello_context_manager() as hello:
        print(hello)

main()