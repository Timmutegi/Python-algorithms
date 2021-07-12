"""
Write a function that returns a true or false value
given a magazine and a word that we want to spell
"""

from collections import defaultdict

class Solution(object):
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1


        for c in note:
            if letters[c] <= 0:
                return False
        
        return True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
#True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
#False