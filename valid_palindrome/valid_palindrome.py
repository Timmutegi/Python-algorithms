class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''
        
        for character in s:
            if character.isalnum():
                newString = newString + character.lower()
                
        return newString == newString[::-1]
    
print(Solution().isPalindrome('A man, a plan, a canal: Panama'))