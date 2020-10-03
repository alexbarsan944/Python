# 5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix
# in spiral order (as in the example):

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
