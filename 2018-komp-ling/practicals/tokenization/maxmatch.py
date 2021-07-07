#!/usr/bin/python
import sys


def tokenize(sent, index):
    if len(sent) == 0:
        return []
    try:
        word = next(w for w in index if sent.startswith(w))
    except StopIteration:
        word = sent[0]
        return [sent]
    return [word] + tokenize(sent[len(word):], index)


if len(sys.argv) > 1:
    with open(sys.argv[1], 'r', encoding='utf-8') as f,\
    open('test.txt', 'w', encoding='utf-8') as o:
        index = sorted([l.strip() for l in f], key=len,reverse=True)
        inp = []
        if len(sys.argv) > 2:
            src = open(sys.argv[2], 'r', encoding='utf-8')
            inp = src.read().splitlines()
        elif sys.stdin:
            inp = sys.stdin
        else:
            print("Please pass correct data!")
            exit()
        for line in inp:
            res = tokenize(line.strip(), index)
            print(" ".join(res))
else:
    print("Please pass correct arguments!")