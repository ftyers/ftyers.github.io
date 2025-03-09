import nltk
import sys

#tokenization to extract words from the text
from nltk.tokenize import word_tokenize
path = '/home/gugutse/Documents/monkey.txt'
word_tokenize_list = []
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        word_tokenize_list += word_tokenize(line)
    

#making a dictionary 'word - its frequency'
dictionary = {}

for word in word_tokenize_list:
    word = word.lower().strip()
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1

for word in dictionary:
	print('%d\t%s' % (dictionary[word], word))

