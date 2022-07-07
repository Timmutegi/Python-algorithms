"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''
        
        for character in s:
            if character.isalnum():
                newString = newString + character.lower()
                
        return newString == newString[::-1]
    
print(Solution().isPalindrome('A man, a plan, a canal: Panama'))