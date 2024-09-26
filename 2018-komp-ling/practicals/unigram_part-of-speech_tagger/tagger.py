#! /usr/bin/env python

import sys

model = open(sys.argv[1])

#{word: {tag:tag_count}}
word_info = {} 
for line in model:
    
    if line.startswith('#'):
        continue
    
    word = line.split('\t')[3].strip()
    tag = line.split('\t')[2]
    count_tag = int(line.split('\t')[1])

    if not word in word_info:
        word_info[word]= {}
        word_info[word][tag] = 0
    elif tag not in word_info[word]:
        word_info[word][tag] = 0
    word_info[word][tag] += count_tag

#{word: tag}
word_tag = {}
for word, tags in word_info.items():
    word_tag[word] = max(tags, key=tags.get)

def tagger(line, dictionary):
    line = line.split('\t')
    word = line[1]
    tag = dictionary[word]
    line[3] = tag
    new_line = ('\t').join([field for field in line])
    return new_line

out = open('output.conllu','w')
for line in sys.stdin.readlines():
    line = line.strip()
    if line.startswith('#'):
        print(line)
    else:
        print(tagger(line, word_tag))
