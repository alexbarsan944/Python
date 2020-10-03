# 1) Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
# alpha-numeric characters.
import re


def word_extractor(text):
    retList = re.findall(r'\w+', text)
    return retList


print(word_extractor('I am a sentence !!!'))
