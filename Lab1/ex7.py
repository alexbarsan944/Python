# 7 Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will
# extract only the first number that is found.

def extractNumber(string: str()):
    n_list = str()
    for i in range(0, len(string)):
        if '0' <= string[i] <= '9':
            for j in range(i, len(string)):
                if '0' <= string[j] <= '9':
                    n_list += string[j]
                else:
                    return int(n_list)


print(extractNumber("abc123abc123"))
