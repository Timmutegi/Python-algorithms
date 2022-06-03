"""
Given a sorted array of integers arr and an integer target, 
find the index of the first and last position of target in arr.

If target can't be found in arr, return [-1, -1]

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def first_and_last(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                start = i
                while i+1 < len(arr) and arr[i+1] == target:
                    i += 1
                return [start, i]
            
        return [-1, -1]
        