from pprint import pprint

class Solution(object):
    def find_most_repeated_character(self, sentence):
        count_dict = {}
        for ch in sentence:
            if ch in count_dict:
                count_dict[ch] += 1
            else:
                count_dict[ch] = 1

        # pprint(count_dict, width=1)
    
        count_sorted = sorted(count_dict.items(), key=lambda kv: kv[1], reverse=True)

        return count_sorted[0]


print(Solution().find_most_repeated_character("This is a common interview question"))
