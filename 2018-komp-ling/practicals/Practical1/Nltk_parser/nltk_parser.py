#!/usr/bin/env python3
import fileinput
file = []
for line in fileinput.input():
	file.append(line[:-1])
text = ' '.join(file)

import nltk
from nltk.tokenize import sent_tokenize

sent_tokenize_list = sent_tokenize(text)

f=open('out1.txt', 'w', encoding='utf-8')
for i in sent_tokenize_list:
	f.write(i+'\n')
print(sent_tokenize_list)
