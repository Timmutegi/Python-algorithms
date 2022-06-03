def helloWorld():
    print('Hello world!!!')

def greetings(name):
    if not name:
        return
    print('Hi ' + name)

def checkNum(num):
    if (num%2) == 0:
        print('EVEN')
    else:
        print('ODD')


# helloWorld()
# greetings('Timothy')
checkNum(5)