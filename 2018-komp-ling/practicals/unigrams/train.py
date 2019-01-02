#!/usr/bin/env python3
''' Word probability and part-of-speech tag probability from annotated text

(e.g. the relative frequency of the word and  relative frequency of the part-of-speech tag)
'''
import sys

conllu_f = open(sys.argv[1], 'r')
table_f = open(sys.argv[2], 'a')

token_tag = {}
tag_freq = {}
token_num = 0

for line in conllu_f:
    # read token and it's tag if the string is relevant
    if line.startswith('\n'):
    	continue
    if line.startswith('#'):
        continue
    token = line.split('\t')[1]
    #token = line.split('\t')[1].lower()
    tag = line.split('\t')[3]
    # add token if not in dict
    if token not in token_tag:
        token_tag[token] = {}
    # add tag for token if no such tag
    if tag not in  token_tag[token]:
        token_tag[token][tag] = 0
    # increase counter for token-tag pair
    token_tag[token][tag] += 1
   
    # create tag frequency list
    if tag not in tag_freq:
        tag_freq[tag] = {}
        tag_freq[tag] = 0
    tag_freq[tag] += 1
    
    # increase total number of tokens
    token_num +=1
    
# print the table: frequency of POS/word-tag pair for the particular token, count of tag-token pair, tag, token 
print('# P\tcount\ttag\tform', file = table_f)
for tag in tag_freq:
    print('%.2f\t%s\t%s\t-' % (tag_freq[tag]/token_num, tag_freq[tag], tag), file = table_f)
for token in token_tag:
    for tag in token_tag[token]:
        print('%.2f\t%s\t%s\t%s' % (token_tag[token][tag]/sum(token_tag[token].values()), token_tag[token][tag], tag, token), file = table_f)