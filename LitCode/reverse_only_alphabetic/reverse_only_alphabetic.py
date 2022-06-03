"""
You have given a string. 
There can have multiple special characters inside the string. 
Write a program to reverse the given string. 
The position of the special characters should not be changed.
"""
class Solution:
    def reverseOnlyAlphabetical(self, str):               
        # convert string into list
        str_array = list(str)
        
        left = 0
        right = len(str_array) - 1
        
        while left < right:
            if not str_array[left].isalpha():
                left += 1
            elif not str_array[right].isalpha():
                right -= 1
            else:
                # swap the element in the list if both elements are alphabets
                str_array[left], str_array[right] = str_array[right], str_array[left]
                left += 1
                right -= 1

        # convert list into string 
        # by concatenating each element in the list
        return ''.join(str_array)                                   
                
str = 'sea!$hells3'
print(Solution().reverseOnlyAlphabetical(str))
#  'sll!$ehaes3'