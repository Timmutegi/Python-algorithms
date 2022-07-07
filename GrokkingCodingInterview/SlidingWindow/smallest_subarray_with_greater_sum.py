"""
Given an array of positive integers and a number S, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to S. 

Return 0 if no such subarray exists.

Example:
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum greater than or equal to 7 is [5, 2].
"""
def smallest_subarray_sum(s, arr):
  
  min_length = len(arr)
  window_sum = 0
  window_start = 0

  for window_end in range(0, len(arr)):
        window_sum += arr[window_end]  # add the next element
        # shrink the window as small as possible until the 'window_sum' is smaller than 's'
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
      
  if min_length == len(arr):
    return 0
  return min_length


def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()