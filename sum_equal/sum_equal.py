"""
Given an array of integers and a value, determine if there are any two 
integers in the array whose sum is equal to the given value. 
Return true if the sum exists and return false if it does not.
"""
def find_sum_of_two(arr, val):
    found_values = set()
    for num in arr:
        if val - num in found_values:
            return True

        found_values.add(num)

    return False