#!/usr/bin/env python3

import re, sys

def pluralizer(word):
    '''takes word with <pl> at the end an adds 's' or 'es' in dependency of context'''
    w = ''
    if re.match('[A-Za-z]+(ch|sh|tz|s|x)\<pl\>', word):
        w = word[:-4] +'e'
    elif re.match('[A-Za-z]+\<pl\>', word):
        w = word[:-4]
    else:
        print(word + ' can\'t be pluralized')
        return
    return(w + 's')

for line in sys.stdin.readlines():
    print(pluralizer(line.strip()))
