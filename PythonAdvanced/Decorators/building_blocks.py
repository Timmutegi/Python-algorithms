# To get a better understanding of how decorators work, the following concepts are essential:

# 1 - In Python, a function is an object

def my_function():
    print('I am a function')

# Assign the fuction to a variable without parenthesis.

descriptin = my_function

# Access the function from the variable it was assigned to
print(descriptin())

# 2 - A function can be nested within another function
def outer_function():
    def inner_function():
        print('I came from the inner function')

    # Executing the inner function inside the outer function

    inner_function()

outer_function()

# 3 - Since a function can be nested inside another funciton it can also be returned
def outer_function():
    '''Assign task to student'''
    task = 'Read Python book chapter 3'

    def inner_function():
        print(task)

    return inner_function

homework = outer_function()

# 4 - A function can be passed to another function as an argument
def friendly_reminder(func):
    '''Reminder for husband'''

    func()
    print('Don\'t forget to bring your wallet!')


def action():
    print('I am going to the store to buy you something nice')

# Calling the friendly reminder function with the action function used as an argument
friendly_reminder(action)