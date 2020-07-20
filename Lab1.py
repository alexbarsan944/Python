# 1. Find The greatest common divisor of multiple numbers read from the console.


def one():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    def cmmdc(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    print(cmmdc(a, b))


# /1

# 2. Write a script that calculates how many vowels are in a string.


def two():
    s = str(input("Enter string: "))
    k = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, len(s)):
        if s[i].lower() in vowels:
            k = k + 1
    print(k)


# /2

# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def three(s1, s2):
    print(s2.count(s1))


# /3

# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
import re


def four(s):
    res = re.findall('.[^A-Z]*', s)
    s = ("_".join(res)).lower()
    print(four("UpperCamelCase"))
    return s
    pass


# 5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):

def printRow(matrix):
    size = len(matrix) - 1
    k = 0
    for i in matrix[k][0][size]:
        print(i)


def five():
    def ptrOuter(matrix, level):
        size = len(matrix[0])
        for i in range(level, size - level):  # top
            print(matrix[level][i], end='')
        for i in range(level + 1, size - level):  # right
            print(matrix[i][size - 1 - level], end='')
        for i in range(size - 1 - level, level, -1):  # bottom
            print(matrix[size - level - 1][i - 1], end='')
        for i in range(size - level - 1, level + 1, -1):  # left
            print(matrix[i - 1][level], end='')

    matrix = [['f', 'i', 'r', 's'],
              ['n', '_', 'l', 't'],
              ['o', 'b', 'a', '_'],
              ['h', 't', 'y', 'p'],
              ]
    for i in range(0, len(matrix[0]) // 2):
        ptrOuter(matrix, i)

# five()

# / 5
