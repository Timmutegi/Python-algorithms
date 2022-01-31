class Solution:
    def reverse_string(self, str):
        start = 0
        end = len(str) - 1
        res = ''
        str_array = list(str)
        
        while start <= end:
            str_array[start] = str[end]
            str_array[end] = str[start]
            start += 1
            end -= 1
            
        return res.join(str_array)

print(Solution().reverse_string('jake'))            
        
        