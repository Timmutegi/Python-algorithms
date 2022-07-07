"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. 
You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
"""
def fruits_into_baskets(fruits):
  window_start = 0
  char_frequency = {}
  max_length = 0

  for window_end in range(len(fruits)):
    right_char = fruits[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    while len(char_frequency) > 2:
      left_char = fruits[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)
  return max_length

  return -1