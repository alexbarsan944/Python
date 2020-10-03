import re


def four(s):
    res = re.findall('.[^A-Z]*', s)
    s = ("_".join(res)).lower()
    print(four("UpperCamelCase"))
    return s
    pass