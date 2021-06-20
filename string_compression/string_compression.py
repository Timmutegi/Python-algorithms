# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

# SOLUTION
def compress(string):
    index = 0
    compressed = ''
    len_str = len(string)
    while index != len_str:
        count = 1
        while (index < len_str-1) and (string[index] == string[index+1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed += str(string[index])
        else:
            compressed += str(string[index]) + str(count)
        index = index + 1
    return compressed

string = 'aabcccccaaa'
print(compress(string))