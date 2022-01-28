
"""
Fibonacci series solution
"""
class Solution:
    def fibonacci(self, n):
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        return self.fibonacci(n-1) + self.fibonacci(n - 2)
    
    
print(Solution().fibonacci(9))