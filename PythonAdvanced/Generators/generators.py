"""
Generator functions allow you to declare a function that behaves like an iterator.

They allow programmers to make an iterator in a fast, easy, and clean way.

They have lazy execution (producing items only when asked for). 
For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.
"""
def check_prime(number):    
    for divisor in range(2, int(number ** 0.5) + 1):        
        if number % divisor == 0:            
            return False    
        return True

def Primes(max):    
    number = 1    
    while number < max:        
        number += 1        
        if check_prime(number):            
            yield number

primes = Primes(1000)
for prime in primes:
    print(prime)