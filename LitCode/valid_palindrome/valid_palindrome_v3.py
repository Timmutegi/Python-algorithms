"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        
        s = s.lower()
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left].isalnum() == False or s[left] == " ":
                left += 1
            elif s[right].isalnum() == False or s[right] == " ":
                right -= 1
            else:
                return False
        
        return True