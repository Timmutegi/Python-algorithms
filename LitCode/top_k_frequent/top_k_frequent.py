"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_dict = {}
        res = []
        for num in nums:
            if num in my_dict:
                my_dict[num] = my_dict[num] + 1
            else:
                my_dict[num] = 1
        
        values = my_dict.values()
        keys = my_dict.keys()
        length = len(keys) - k
        lst = sorted(values)[length:]
        for num in lst:
            position = values.index(num)            
            res.append(keys[position])
            my_dict.pop(keys[position])
            values = my_dict.values()
            keys = my_dict.keys()
            
        return res