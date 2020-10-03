# Sa se scrie o functie care primeste ca parametru un sir de caractere regex, un sir de caractere text si un numar
# intreg x si returneaza acele substring-uri de lungime maxim x care fac match pe expresia regulata data.
import re


def two(reg_str, text, x):
    result = re.search(reg_str, text)
    for i in range(result.lastindex + 1):
        if len(result.group(i)) <= x:
            print(result.group(i))


two(r"(\d+)[^\d]*(\d+)", "Price is 1000 USD, 900 EUR", 3)
