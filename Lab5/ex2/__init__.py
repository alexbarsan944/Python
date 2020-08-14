# 5) Write a function with one parameter which represents a list. The function will return a new list containing all
# the numbers found in the given list.

# Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]

def five(lst: list()):
    retList = []
    for i in lst:
        if isinstance(i, (float, int)):
            retList.append(i)
    print(retList)


five([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0])
