"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)
        
        substring = ''
        maxLen = 1
        for i in s:
            if i not in substring:                      
                substring = substring + i
                maxLen = max(maxLen, len(substring))    
            else: 
                substring = substring.split(i)[1] + i   
        return maxLen 
    
print(Solution().lengthOfLongestSubstring('abcabcbb'))