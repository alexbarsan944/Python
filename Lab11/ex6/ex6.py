# Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship
# means replacing characters from odd positions with *.
import re


def censor(text):
    reg = r'^[aeiou].*[aeiou]$'
    word_list = text.split()
    index = 0

    for i in word_list:
        if re.match(reg, i):
            word_list[index] = '*' * len(i)
        index += 1

    result = ' '.join(word_list)

    return result


print(censor('aaa aeiouB abc dea iasjkdadsa'))
