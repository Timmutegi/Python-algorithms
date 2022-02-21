"""
In a given array of numbers, one element will show up once and the others will each show
up twice. Can you find the number that only appears once in O(n) linear time? 
Bonus points if you can do it in O(1) space as well.
"""
class Solution:
    def lonelyNumber(self, numbers):
        res = []
        
        for num in numbers:
            if num in res:
                res.remove(num)
            else:
                res.append(num)
        
        return res[0]

numbers = [4,1,4,7,9,4,7,1]    
print(Solution().lonelyNumber(numbers))    