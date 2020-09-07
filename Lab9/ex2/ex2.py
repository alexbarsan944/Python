# 2) Write a function get_file_info that has one parameter representing a file path. The function will return a
# dictionary with the following fields:
# - full_path - the absolute path of the file
# - file_size - the size of the file
# - file_extension - the file's extension
# - can_read/can_write - True or False, if the user can read from the file/write in the file.
import os


def get_file_info(file_path):
    ret_dict = {}
    ret_dict['full_path '] = os.path.abspath(file_path)
    ret_dict['size'] = os.path.getsize(file_path)
    ret_dict['file_extension'] = os.path.splitext(file_path)[1]
    ret_dict['can_read'] = os.access(file_path, os.R_OK)
    ret_dict['can_write'] = os.access(file_path, os.W_OK)

    return ret_dict


print(get_file_info("./test_dir/test_file"))
