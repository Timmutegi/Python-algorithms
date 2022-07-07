"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = "adc"
        s2 = "dcda"
        
        l, r = 0 , len(s1) 

        while r < len(s2):
            if sorted(s2[l:r]) == sorted(s1):
                return True
            else:
                print(s2[l:r])
                l += 1
                r += 1
                
        return False