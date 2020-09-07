# 4. Write a function that receives as a parameter a path that represents a directory on the system. The function
# will recursively browse the files and directories at the given path and will display at the console all the paths
# it has found and their type (FILE, DIRECTORY, UNKNOWN. You are NOT allowed to use os.walk.
import glob
import os


def print_file_type(path):
    folders = [f for f in glob.glob(path + "**/*", recursive=True)]
    for f in folders:
        if os.path.isfile(f):
            print(f, " is a file")
        elif os.path.isdir(f):
            print(f, " is a dir")
        else:
            print("is unknown")


print_file_type("../ex2/")
