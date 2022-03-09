"""
A sliding window is a sublist or subarray that runs over an underlying data structure. The
data structure is iterable and ordered, such as an array or a string. At a high level, you
can think of it as a subset of the two pointers method. It normally encompasses searching
for a longest, shortest or optimal sequence that satisfies a given condition.
"""

class SlidingWindow():
    def min_window(self, s, req_chars):
        # hash to keep account of how many required characters we've checked off
        # each key will represent a character in req_chars
        # we preset each to 1 and will look to lower it to 0 when each is fulfilled
        hash = {}
        for c in req_chars:
            hash[c] = 1
        # trackers that we need
        # this is a counter to measure string length against
        counter = len(req_chars)
        begin = 0
        end = 0
        substr_size = float("inf")
        head = 0
        
        while end < len(s): # continue running while there's more elements in `s` to process
            if hash.get(s[end], -1) > 0: # we've found a letter we needed to fulfill
                # modify the length counter so we know how close we are to a length match
                counter -= 1
                # modify the dictionary to say we've gotten this character requirement
                if s[end] in hash:
                    hash[s[end]] -= 1
                    
            # extend our window
            end += 1
                
            while counter == 0: # valid
                if end - begin < substr_size:
                    head = begin
                    substr_size = end - head
                # we want to shrink it from the beginning now
                # to make it the minimum size possible
                if s[begin] in hash:
                    hash[s[begin]] += 1
                    # this is a character we need
                    if hash[s[begin]] > 0:
                        counter += 1
                    
                begin += 1
            
        return "" if substr_size == float("inf") else s[head:substr_size]

print(SlidingWindow().min_window("abcalgosomedailyr", "ad"))

        