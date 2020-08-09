# 1. Write a function that receives as parameter a list of tuples
# (last_name, first_name) and returns the list sorted by first_name.

def one(*tup: tuple()):
    print(sorted(tup, key=lambda t: (t[1])))


# one(("Bulovswky", "Bula"), ("aaa", "AAA"), ("Becali", "Gigi"))


# 2. Write a function that receives as parameter a sorted list of tuples (last_name, first_name)
# like in ex.1 and a string representing a first_name. Check if the first_name is in the list.

def two(first_name: str(), *tup: tuple()):
    for i in tup:
        if first_name in i:
            return True
    return False


# print(two("Bula", ('aaa', 'AAA'), ('Bulovswky', 'Bula'), ('Becali', 'Gigi')))


# Build a apply_operator function (operator, a, b) that will apply over a and b the rule specified by the global dictionary.
# Implement it so that if a new operator is added, it is not necessary to change the function.

def apply_operator(operator, a, b):
    op = {
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "//": lambda a, b: a // b,
        "%": lambda a, b: a % b
    }
    try:
        return op[operator](a, b)
    except ArithmeticError:
        return "ArithmeticError"
    except:
        return "Invalid operator"


# print(apply_operator("/", 5, 0))
# print(apply_operator("*", 5, a))


# 4. Consider a globally defined dictionary similar to the one above, with the difference that the functions
# given as values of the dictionary can receive any combination of parameters.
# Write a function apply_function that receives as a parameter the name of an operation and applies the
# corresponding function over the arguments received.
# Implement it so that if a new function is added, it is not necessary to change the function apply_function.

func_dict = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}


def apply_function(operation, *a, **b):
    try:
        func_dict[operation](*a, **b)
    except:
        print("Invalid operation")


# apply_function(("print_all"), (1, 2, 3), (5, 6, 7), key1=1, key2=3)


# 5. Write a function that receives a variable number of dictionaries and returns a dictionary with all the keys and
# values from the given dictionaries.
# If the same key is in multiple dictionaries, the value will be a list that contains the values of that key in each dictionary.

def five(*dic: dict()):
    def getKeyListValue(key: str()):
        retList = list()
        for i in dic:
            for j in i.items():
                if j[0] == key:
                    retList.append(j[1])
        return retList

    retDict = dict()
    for i in dic:
        for j in i.items():
            retDict[j[0]] = getKeyListValue(j[0])
    print(retDict)


# five({"jimmy": 1, "john": 1, "abcdef": 123456}, {"jimmy": 2, "bula": 3, "abc": 321}, {"abc": 123})


# 6. Write a function that receives as parameter a recursive dictionary and a string with default value '-'.


def six(dic: dict(), sep='-'):
    def trace(dic, lista=list()):
        for k, v in dic.items():
            if isinstance(v, dict):
                lista.append(k)
                trace(v)
            else:
                if len(lista) > 0:
                    print(sep.join(lista), end=sep)
                print(k, v, sep=sep)

    trace(dic)


# six({'a': 1, 'b': {'c': 3, 'd': {'e': 5, 'f': 6}}})
"""
'a' - 1
'b' - 'c' - 3
'b' - 'd' - 'e' - 5
'b' - 'd' - 'f' - 6
"""
