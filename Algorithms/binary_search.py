"""
The binary search pattern, as the name suggests, is used to search an element in a list of
elements. Though linear search is a simple alternative to binary search, the time complexity
of linear search is O(n). This is bad, because it means that if the element exists at the last index,
the whole list has to be iterated. It reduces the search complexity to O(log(n)).

The binarySearch routine returns the index of the item where the value is found. 
If the value does not exist in the array, it returns -1.
"""

class Solution():
    def binarySearch(self, arr, num):
        first = 0
        last = len(arr) - 1
        index = -1
        
        mid = (first + last) // 2  # Floor Division
                
        while (index == -1 and first <= last):
            if (num < arr[mid]):
                last = mid
            elif (num > arr[mid]):
                first = mid
            else:
                index = mid
                                
        return index
        

arr = [1, 3, 6, 10, 12]
num = 6
print(Solution().binarySearch(arr, num))
        