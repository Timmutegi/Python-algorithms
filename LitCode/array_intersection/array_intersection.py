"""
Write a function that takes two arrays as inputs and returns their intersection.
"""
class Solution():
    def intersection(self, arr1, arr2):
        res = []
        for item in set(arr1):
            if item in arr2:
                res.append(item)
                
        return res
        
# arr1 = ['green', 'orange', 'blue', 'red']
# arr2 = ['black', 'green', 'red', 'purple']
arr1 = [1,2,2,1]
arr2 = [2,2]

print(Solution().intersection(arr1, arr2))