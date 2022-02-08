"""
You have given a string. 
There can have multiple special characters inside the string. 
Write a program to reverse the given string. 
The position of the special characters should not be changed.
"""
class Solution:
    def reverseOnlyAlphabetical(self, str):               
        #convert string into list
        listSample=list(str)
        
        i = 0
        j = len(listSample)-1
        
        while i < j:
            if not listSample[i].isalpha():
                i += 1
            elif not listSample[j].isalpha():
                j -= 1
            else:
                #swap the element in the list 
                #if both elements are alphabets
                listSample[i], listSample[j]=listSample[j], listSample[i]
                i+=1
                j-=1

        # convert list into string 
        # by concatenating each element in the list
        return ''.join(listSample)                                   
                
str = 'sea!$hells3'
print(Solution().reverseOnlyAlphabetical(str))
#  'sll!$ehaes3'