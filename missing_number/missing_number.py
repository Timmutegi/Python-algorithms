"""
Find the missing number in the array

A naive solution is to simply search for every integer between 1 and n 
in the input array, stopping the search as soon as there is a missing number. 
But we can do better. Here is a linear, O(n), solution that uses the 
arithmetic series sum formula.​​ 
"""
def find_missing(input):
    sum_of_elements = sum(input)

    n = len(input) + 1
    actual_sum = (n * (n+1)) / 2

    return actual_sum - sum_of_elements