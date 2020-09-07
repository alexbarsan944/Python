# 5. Write a function that has 3 parameters: source (a path to a file), directory (a path to a directory) and
# buffer_size (an integer). The function will copy the given file into the given directory, using a buffer of the
# third parameter size, in bytes.

import os


def five(source, directory, buffer_size):
    try:
        fo = open(directory + '/' + source, "wt")
    except:
        print('coulnt create new file in directory')
    try:
        f = open(source, 'r+')
    except:
        print('couldnt open source')

    file_size = os.path.getsize(source)
    while file_size > 0:
        line = f.readline(buffer_size)
        file_size -= buffer_size
        fo.write(line)
    f.close()


five('test_file.txt', 'test_dir', 5)
