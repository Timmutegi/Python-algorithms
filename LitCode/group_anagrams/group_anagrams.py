"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        my_dict = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in my_dict:
                my_dict[sorted_str].append(str)
            else:
                my_dict[sorted_str] = [str]
        
        return my_dict.values()
            