# 2. Write a script that calculates how many vowels are in a string.


def two():
    s = str(input("Enter string: "))
    k = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, len(s)):
        if s[i].lower() in vowels:
            k = k + 1
    print(k)