# 1) Write a function called search_by_content which has two parameters: target and to_search. The function will
# return a list of files containing to_search. If target represents a file, this will be the only file searched. If
# target represents a directory, all the files found in the directory (recursively) will be searched. If target does
# not exist an empty list will be returned.
import os


def search_by_content(target, to_search):
    file_list = []

    def rec_search():
        for (root, directories, files) in os.walk(target):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                if check_file(full_fileName):
                    file_list.append(fileName)

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

    if is_dir(target):
        rec_search()
    else:
        if check_file(target):
            print(list(target))

    return file_list


print(search_by_content("test_dir", "123"))
