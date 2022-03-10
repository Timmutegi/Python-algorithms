"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
"""
class Solution():
    def isValid(self, input):
        stack = []
        
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for ch in input:
            if ch in mapping: 
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
            
            
        return True if not stack else False
        
input = "()[]{}"
print(Solution().isValid(input))