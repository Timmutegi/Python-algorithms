"""
Given a string paragraph and a string array of the banned words banned, 
return the most frequent word that is not banned. It is guaranteed 
there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
"""

from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned_words = set(banned)
        ans = ''
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []
        
        for p, char in enumerate(paragraph):
            #1. Iterate through characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    continue
                    
            #2. At the end of one word or the paragraph
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned_words:
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                word_buffer = []
                
                
        return ans

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))