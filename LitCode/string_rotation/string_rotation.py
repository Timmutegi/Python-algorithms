# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

#SOLUTION
def isRotation(string1, string2):
    if len(string1) == len(string2):
        string1Double = string1 + string1
        return string1Double in string2


s1 = 'waterbottle'
s2 = 'erbottlewat'

print(isRotation(s1, s2))