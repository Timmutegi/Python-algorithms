"""
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.
"""
class Solution(object):
    def twoSum(self, nums, target):
        my_dict = {}
        for index, num in enumerate(nums):
            value = target - num
            if value in my_dict and my_dict[value] != index:
                return [my_dict[value], index]

            my_dict[nums[index]] = index
                
nums = [2, 4, 5, 6]
target = 11
print(Solution().twoSum(nums, target))
