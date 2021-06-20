# Implement an algorithm to determine if a string has all unique characters.

# SOLUTION
string = 'algorithm'
string_set = set(string)
is_unique = True if len(string) == len(string_set) else False
print(is_unique)
