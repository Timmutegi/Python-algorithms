class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False
    
print(Solution().containsDuplicate([1, 2, 3, 1]))