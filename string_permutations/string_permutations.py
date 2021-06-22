# PROBLEM:

# Given a smaller string "s" and a bigger string "b", 
# Design an algorithm to find all permutations of the shorter string within the longer one. 
# Print the location of each permutation. 

# SOLUTION:


def findPermutation(smallString, largeString):
    for index, character in enumerate(b):
        if character in s:
            if len(b[index: index+4]) == len(s):
                if sorted(b[index: index+4]) == sorted(s):
                    print(index+1)
                    

s = 'abbc'
b = 'cbabadcbbabbcbabaabccbabc'
findPermutation(s, b)