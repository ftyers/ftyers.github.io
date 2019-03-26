#-*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

def maxmatch(s, dictionary):
    if not s:
        return [] # уточнить
    for i in range(len(s), 0, -1):
        firstword = s[:i]
        remainder = s[i:]
        if firstword in dictionary:
            return[firstword] + maxmatch(remainder, dictionary)
        
    # no word was found, so make a one-character word
    ###firstword = s[0]
    ###remainder = s[1:]
    return[firstword] + maxmatch(remainder, dictionary)

text = open(sys.argv[1])
words = open(sys.argv[2])
tokenized = open(sys.argv[3], 'w')

dictionary = [i.rstrip('\n') for i in words.readlines()]

for line in text:
	tokenized.write(' '.join(maxmatch(line, dictionary)))
