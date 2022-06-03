# Implement an algorithm to determine if a string has all unique characters.

# SOLUTION

def isUnique(string):
    string_set = set(string)
    is_unique = True if len(string) == len(string_set) else False
    print(is_unique)

string = 'algorithm'
isUnique(string)
