# 6 Write a function that validates if a number is a palindrome.

def pal(string: str()):
    for i in range(0, len(string) // 2):
        if not string[i] == string[len(string) - 1]:
            return "Palindrom"
    return "Not palindrom"


print(pal("aaabbaaa"))
print(pal("aaaabaaa"))
