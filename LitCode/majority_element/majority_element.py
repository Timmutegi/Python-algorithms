"""
Suppose we're given an array of numbers like the following: [4, 2, 4]
Could you find the majority element? A majority is defined as "the greater part, or more than
half, of the total. It is a subset of a set consisting of more than half of the set's elements."
"""
class Solution:
    def find_majority_element(self, arr):
        sortedNums = sorted(arr)
        return sortedNums[round(len(arr)/2)]
    

# arr = [4, 2, 2, 3, 2]
arr = [4, 2, 4]    
print(Solution().find_majority_element(arr))    