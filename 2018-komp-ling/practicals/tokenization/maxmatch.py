# Mikhailov Vladislav

import sys


with open(sys.argv[1]) as f:
    dictionary = sorted([line.strip() for line in f], key=len, reverse=True)


def tokenize(sentence):
    tokens = []
    word_length = 0
    while word_length < len(sentence):
        word = longest_word(sentence[word_length:])
        tokens.append(word)
        word_length += len(word)
    return tokens


def longest_word(sentence):
    sen_length = len(sentence)
    while sen_length > 1:
        remain = sentence[:sen_length]
        if remain in dictionary:
            return remain
        sen_length -= 1
    return sentence[0]


for sentence in sys.stdin:
    for word in tokenize(sentence):
        word = word.strip('\n')
        print(word)
