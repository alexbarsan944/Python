# 6) Write two functions that receives as parameters 2 lists of tuples, both lists having the same length. Each tuple
# represents a point in the cartesian system. One function will use the map function and one function will use the
# zip function. The functions will both return a list of tuples (a, b, c) representing the lines determined by the
# points. To calculate a line take a point from the first list and a point from the second list.

def six(list1: list(), list2: list()):
    def getLine(tup1: tuple(), tup2: tuple()):
        a = tup2[1] - tup1[1]
        b = tup1[0] - tup2[0]
        c = a * (tup1[0]) + b * (tup1[1])
        return a, b, c

    def zipFunction():
        retlist = []
        for i in range(0, len(list1)):
            retlist.append(getLine(list1[i], list2[i]))
        return retlist

    def mapFunction():
        return list(map(getLine, list1, list2))

    print(zipFunction())
    print(mapFunction())


six([(2, 3), (4, 5)], [(-1, 2), (-3, 5)])
