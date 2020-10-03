# Sa se scrie o functie care parcurge recursiv un director si afiseaza acele fisiere a caror nume face match pe o
# expresie regulata data ca parametru sau contine un sir de caractere care face match pe aceeasi expresie. Fisierele
# care satisfac ambele conditii vor fi afisate prefixate cu ">>"

import os


def search_by_content(target, to_search):
    file_list = []

    def rec_search():
        for (root, directories, files) in os.walk(target):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                if check_file(full_fileName):
                    file_list.append(fileName)
                    # todo regex the name of the file

    def is_dir(path):
        if os.path.isdir(path):
            return 1
        elif os.path.isfile(path):
            return 0

    def check_file(f):
        try:
            f = open(f)
            for line in f:
                if to_search in line.strip():
                    return 1
            f.close()
        except:
            return []
        # todo regex the file

    if is_dir(target):
        rec_search()
    else:
        if check_file(target):
            print(list(target))

    return file_list


print(search_by_content("test_dir", "123"))
