"""
Given a sorted array of integers arr and an integer target, 
find the index of the first and last position of target in arr.

If target can't be found in arr, return [-1, -1]

Binary search solution

Time Complexity: O(log n)

"""

class Solution:
    def first_and_last(self, arr, target):
        if len(arr) == 0 or arr[0] > target or arr[-1] < target:
            return [-1, -1]
        
        start = self.find_start(arr, target)
        end = self.find_end(arr, target)
        
        return [start, end]
    
    def find_start(self, arr, target):
        if arr[0] == target:
            return 0
        
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid-1] < target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


    def find_end(self, arr, target):
        if arr[-1] == target:
            return len(arr)-1
        
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid+1] > target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1

arr = [2,4,5,5,5,5,7,9,9]
target = 5
solution = Solution()
# print(Solution().first_and_last([2,4,5,5,5,5,7,9,9],5))      
print(Solution.first_and_last(solution, arr, target))
        