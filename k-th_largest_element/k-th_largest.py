"""
Given an array of integers, and an integer k,
find the k-th largest element

Solution using priority queue
"""

import heapq

class Solution(object):
    def find_largest(self, arr, k):
        arr = [-elem for elem in arr]
        heapq.heapify(arr)
        for i in range(k-1):
            heapq.heappop(arr)
            
        return -heapq.heappop(arr)

                
nums = [2, 4, 5, 6]
k = 2
print(Solution().find_largest(nums, k))
