import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() ' f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: calling {func.__name__}() ' f'returned {original_result!r}')

        return original_result

    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

say('Jane', 'Hello, World')