"""
Given an array of integers, and an integer k,
find the k-th largest element
"""
class Solution(object):
    def find_largest(self, nums, k):
        if k > len(nums):
            return 0
        
        nums = sorted(nums)
        
        return nums[-(k)]

                
nums = [2, 4, 5, 6]
k = 4
print(Solution().find_largest(nums, k))
