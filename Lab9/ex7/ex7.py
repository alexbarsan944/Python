# 7. Write a function that parses a given archive and extracts the files with a certain extension.
# The function will have two parameters - container_path (a string representing the path of the container) and
# extension (a string representing the extension we are looking for).

# The container has the following format:
# - Starts with the string "CONTAINER"
# - The following byte represents the number of files in the archive
# - After the previously mentioned byte, for each file there will be
#  -> 4 - unsigned integer, little endian bytes representing the size.
#  -> 50 bytes representing the file name. (if the name has less than 50 characters, it will be padded with whitespaces)
#  -> The body of the file
# Test file: https://we.tl/t-FQFRxzaMjf

