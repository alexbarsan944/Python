# Sa se scrie o functie care primeste ca parametru path-ul catre un document xml si un dictionar attrs si returneaza
# acele elemente care au ca atribute toate cheile din dictionar si ca valoare valorile corespunzatoare. De exemplu,
# pentru dictionarul {"class": "url", "name": "url-form", "data-id": "item"} se vor selecta elementele care au
# atributele: class="url" si name="url-form" si data-id="item".
import re


def get_xml_elements(path, dictionary: dict()):
    lines = str()
    try:
        f = open(path)
        for line in f:
            lines += line
    except:
        print('file didnt open')

    def create_regex():
        line = str()
        reg1 = r'<.*>\s*'
        reg2 = r'\s+<\/.*>'

        for k, v in dictionary.items():
            line += '<' + k + '>' + v + '</' + k + '>' + '|'

        line = (line[0:-1])
        final_reg = reg1 + line + reg2
        return final_reg

    reg = create_regex()
    result = re.match(reg, lines)

    result = re.match('<.*?>', result.group(0)).group(0)
    print(result)
    pass


get_xml_elements('file.xml', {"class": "url", "name": "url-form", "data-id": "item"})
