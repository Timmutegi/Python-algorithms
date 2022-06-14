"""
Given an array of integers that is already sorted in increasing order, return indices of the two numbers 
such that they add up to a specific target.

Example:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""
class Solution:
    def twoSum(self, numbers, target):
        l , r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]
                
        return []                                      
        