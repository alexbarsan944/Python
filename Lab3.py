# 1.Write a function that receives as parameters two lists a and b and returns a set of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)

def one(a: list(), b: list()):
    aSet = set(a)
    bSet = set(b)
    resultSet = set()

    intersection = frozenset(aSet.intersection(bSet))
    union = frozenset(aSet.union(bSet))
    aMinusB = frozenset(aSet.difference(bSet))
    bMinusA = frozenset(bSet.difference(aSet))

    resultSet.add(intersection)
    resultSet.add(union)
    resultSet.add(aMinusB)
    resultSet.add(bMinusA)

    return resultSet


# one(range(1, 5), range(3, 8))


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys
#  are the characters in the character string and the values are the number of occurrences of that character in the given text.
# Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
# {'A': 1, '': 2, 'n': 1, 'a': 2, 'r': 2, '.': 1}.


def two(String):
    retDictionary = {String[i]: String.count(String[i]) for i in range(0, len(String) - 1)}
    print(dict(sorted(retDictionary.items(), key=lambda x: x[1], reverse=True)))  # print sorted by value, descending


# two("Ana are mere.")

# 3. Compare two dictionaries without using the operator "==" and return a list of differences as follows:
# (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def three(a: dict(), b: dict()):
    retList = list()

    def iterdict(d, nonRecDict=dict()):
        for k, v in d.items():
            if isinstance(v, dict):
                iterdict(v)
            else:
                nonRecDict.update({k: v})
        return nonRecDict

    nonRecDict1 = iterdict(a)
    # print(nonRecDict1)
    newA = nonRecDict1.copy()
    nonRecDict2 = iterdict(b)
    newB = nonRecDict2.copy()
    # print(nonRecDict2)

    for k, v in newA.items():
        if k in newB.keys() and v != newB[k]:
            retList.append(k)  # these keys have different values in the given 2 dictionaries
    return retList


# print(three({1: {2: {3: 4, 5: 6}, 3: {4: 5, 6: 7}}, 2: {3: {4: 5}, 4: {6: 7}}}, {1: {2: {3: 99, 5: 99}, 3: {4: 5, 6: 7}}, 2: {3: {4: 5}, 4: {6: 7}}}))


# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element. Example:
# build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link ")
# returns  the string = "<a href=\"http://python.org \" _class = \" my-link \" id = \" someid \ "> Hello there </a>"

def build_xml_element(tag, content, **data):
    key = "<" + tag + " "
    value = ">" + content + "</" + tag + ">"

    retTag = []
    retTag.append(key)
    retTag.append(value)

    retString = ""
    for i in data:
        retString += i + '=' + '\"' + data.get(i) + '\"'
    print(retString.join(retTag))


# build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ")


# 5. The validate_dict function that receives as a parameter a set of tuples that represent validation rules for a dictionary with string keys and values
# of the string type and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered
# valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix". The function will return True
# if the given dictionary matches all the rules, False otherwise.

# Example:
# the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are respected
# for "key1" and "key2" "key3" that does not appear in the rules.


def validate_dict(s: set(), d: set()):
    def matchTuple(a: tuple(), b: set()):
        prefix = a[1]
        middle = a[2]
        suffix = a[3]

        dict = b[1]

        # print("prefix: " + "\'" + prefix + "\'," + " middle: " + "\'" + middle + "\'," + " suffix: " + "\'" + suffix + "\'")
        # print("dict: " + dict)
        for i in range(0, len(prefix)):
            if dict[i] != prefix[i]:
                return False
        if middle not in dict:
            return False
        for i in range(0, len(suffix), -1):
            if dict[i] != suffix[i]:
                return False
        return True

    for i in s:
        for j in set(d.items()):
            if matchTuple(i, j) == False:
                return False
    return True


# print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))


# 6. Write a function that receives as a parameter a set and returns a tuple (a, b),
# representing the number of unique elements in the set, and b representing the number of duplicate elements in the set.

def six(s: set()):
    return len(s), 0


# print(six({1, 2, 3, 4, 5, 5, 5, 5, 6}))

# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by
# two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
"""
Ex: {1,2}, {2, 3} =>

{

    "{1, 2} | {2, 3}": 3,

    "{1, 2} & {2, 3}": 1,

    "{1, 2} - {2, 3}": 1,

    ...

}
"""


def seven(*s: set()):
    op = {'|': lambda x, y: x | y,
          '&': lambda x, y: x & y,
          '-': lambda x, y: x - y}
    retDict = dict()
    for k in ["|", "&", "-"]:
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s)):
                string = str()
                string += str(s[i]) + " " + str(k) + " " + str(s[j])
                retDict[string] = (op[k](s[i], s[j]))

    def print_dict(dct):
        for key, value in dct.items():
            print("{} : {}".format(key, value))

    print_dict(retDict)


seven({1, 2}, {2, 3})
