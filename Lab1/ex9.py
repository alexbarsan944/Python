# 9 Write a functions that determine the most common letter in a string. For example if the string is "an apple is
# not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.

def most_common(string: str()):
    freq = {}
    string = string.lower()
    for i in string:
        if 'a' <= i <= 'z':
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
    return sorted(freq.values())[-1]


print(most_common("an apple is not a tomato"))
