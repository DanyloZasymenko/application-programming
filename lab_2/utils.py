import re


def readByPattern(path, pattern):
    words = []
    with open(path, mode='r', encoding='utf-8') as a:
        for line in a:
            for word in re.findall(pattern, line):
                words.append(word)
    return words
