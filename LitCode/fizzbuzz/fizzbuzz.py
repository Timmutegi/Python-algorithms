"""
Write a function that returns the string representation of all numbers from 1 to n based on
the following rules:
• If it's a multiple of 3, represent it as "fizz".
• If it's a multiple of 5, represent it as "buzz".
• If it's a multiple of both 3 and 5, represent it as "fizzbuzz".
• If it's neither, just return the number itself.
As such, fizzBuzz(15) would result in '12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz'.
"""
class Solution:
    def fizzbuzz(self, n):
        res = ''
        for i in range(n):
            number = i + 1
            if number % 3 == 0 and number % 5 == 0:
                res += 'fizzbuzz'           
            elif number % 3 == 0:
                res += 'fizz'
            elif number % 5 == 0:
                res += 'buzz'
            else:
                res += str(number)
                
        return res               
                

print(Solution().fizzbuzz(15))