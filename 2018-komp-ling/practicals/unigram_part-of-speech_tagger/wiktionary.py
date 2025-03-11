#! /usr/bin/env python

import sys

def strip_html(h):
    res = ''
    inTag = False
    for c in h: 
        if c == '<':
            inTag = True
            continue
        if c == '>':
            inTag = False
            continue
        if not inTag:
            res = res + c
    return res

h1 = '_';
stem = '_'
zkod = '_'
ipa = '_'

# for line in sys.stdin.readlines(): 
for line in sys.stdin.readlines():
    
    line = line.strip()
    text = strip_html(line);
    
    if line.count('<h1>') > 0: 
        h1 = strip_html(line)
        
    if h1 != 'Русский': 
        continue

    if text.count('Корень:') > 0:
        stem = text.split(':')[1].split(';')[0]
        
    if text.count('МФА') > 0:
        ipa = text.split('&#91;')[1].split('&#93')[0]
    if text.count('тип склонения') > 0:
        zkod = text.split('склонения')[1].split(' ')[1]
        
if stem != '_' and zkod != '_' and ipa != '_':
    print('%s\t%s\t%s' % (stem, zkod, ipa))