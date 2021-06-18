# PROBLEM:

# Given a smaller string "s" and a bigger string "b", 
# Design an algorithm to find all permutations of the shorter string within the longer one. 
# Print the location of each permutation. 

# SOLUTION:
s = 'abbc'
b = 'cbabadcbbabbcbabaabccbabc'

for index, letter in enumerate(b):
    if letter in s:
        if len(b[index: index+4]) == len(s):
            if sorted(b[index: index+4]) == sorted(s):
                print(index+1)
