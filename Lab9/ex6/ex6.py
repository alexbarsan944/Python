# 6. Write a function which receives a path to a directory as an argument and returns a dictionary with the following
# fields:
# - full_path - absolute path of the directory
# - total_size - the total size of the files found recursively in the directory
# - files - a list of relative paths of the files found inside the directory
# - dirs - a list of absolute paths to the directories found inside the directroy.
import os
import pprint


def six(path):
    def get_file_size(f_path):
        return os.path.getsize(f_path)

    def get_total_dir_size():
        total_dir_size = 0
        for (root, directories, files) in os.walk(path):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                total_dir_size += get_file_size(full_fileName)
        return total_dir_size

    def get_file_list():
        lista = []
        for root, dirs, files in os.walk("."):
            for d in dirs:
                lista.append(os.path.relpath(os.path.join(root, d), "."))
            for f in files:
                lista.append(os.path.relpath(os.path.join(root, f), "."))
        return lista

    def get_dir_abspath():
        lista = []
        for root, dirs, files in os.walk("."):
            for d in dirs:
                lista.append(os.path.abspath(d))
        return lista

    ret_dict = {'full_path': os.path.abspath(path), 'total_size': get_total_dir_size(), 'files': get_file_list(),
                'dirs': get_dir_abspath()}

    return pprint.pprint(ret_dict, width=2)


print(six('test_dir'))
