# 10 Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.

def count_words(string: str()):
    def test_if_text():
        for i in range(1, len(string)):
            if string[i] == ' ':
                if not string[i - 1].isalpha() and string[i + 1].isalpha():
                    return 0
        return 1

    if test_if_text() == 0:
        return "Not a text"
    else:
        return string.count(' ') + 1


print(count_words("I have Python exam"))
