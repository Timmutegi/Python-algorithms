"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Time Complexity: O(S+T)
Space Complexity: 
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1
            
        for ch in t:
            if ch in t_dict:
                t_dict[ch] += 1
            else:
                t_dict[ch] = 1
                
        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False
            

        return True