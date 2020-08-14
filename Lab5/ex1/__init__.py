# 4) Write a function that receives a variable number of arguments and keyword arguments.
# The function returns a list containing only the arguments which are dictionaries,
# containing minimum 2 keys and at least one string key with minimum 3 characters.
#  Returns -> [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]
def four(*args, **kwargs):
    retList = []

    def checkCondition(dic):
        if isinstance(dic, dict):
            if len(dic.keys()) >= 2:
                for k, v in dic.items():
                    if len(str(k)) > 2:
                        retList.append(dic)
                        break

    for i in args:
        checkCondition(i)
    for i in kwargs.values():
        checkCondition(i)

    print(retList)


four({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
     dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True})
