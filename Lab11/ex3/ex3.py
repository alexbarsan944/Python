# Sa se scrie o functie care primeste ca parametru un sir de caractere text si o lista de expresii regulate si
# returneaza o lista de siruri de caractere care fac match pe cel putin o expresie regulata data ca parametru.
import re


def three(text, *regex_list):
    retlist = []
    for r in regex_list:
        result = re.match(r, text)
        if not result is None:
            retlist.append(result.group(result.lastindex))
    print(retlist)


three("File size if 12345 bytes", r".*?(\d+)", r".*?(\w+)")
