# 3) Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list
# will all the vowels in a given string.
# For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].

s = "Programming in Python is fun"
vowels = "aeiouAEIOU"


def ptrVowelsFromString(s: str()):
    retList = []
    for i in range(0, len(s)):
        if s[i] in vowels:
            retList.append(s[i])
    return retList


print(list(filter(lambda x: x[0] in vowels, s)))  # 1
print(ptrVowelsFromString(s))  # 2
print([i for i in s if i in vowels])  # 3

