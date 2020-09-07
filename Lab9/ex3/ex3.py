# 3. Write a function that receives a filename as a parameter and writes the data from the os.environ in the file
# given as parameter. Each line containing an entry in this dictionary, in the form of the key [tab] value.
import os
import pprint


def print_environ():
    try:
        f = open("output.txt", "wt")
        pprint.pprint(dict(os.environ), f, width=1)
        f.close()
    except:
        print("couldn't create file")
    finally:
        print("file created")


print_environ()
