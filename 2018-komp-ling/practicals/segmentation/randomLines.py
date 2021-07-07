#!/usr/bin/python

import random
with open("wiki.txt", "r", encoding='utf-8') as wiki, open('sample.txt', 'w', encoding='utf-8') as f:
    lines = []
    for line in wiki:
        lines.append(line)
    for num in random.sample(range(len(lines)), 100):
        print(lines[num], file=f)