import sys
import os
#file = os.dir("C:\\Users\\MiNB\\ubuntu\\WikiExtractor\\syntagrus-ud-test.conllu")
file = open("syntagrus-ud-test.conllu", 'r')

vocab = {} # dict to store frequency list
freq = []

# for each of the lines of input
for line in file:
	if '\t' not in line:
		continue
	# make a list of the cells in the row
	row = line.split('\t')
	# if there are not 10 cells, skip the line
	if len(row) != 10:
		continue
	# the form is the value of the second cell
	form = row[1]
	# if we haven't seen it yet, set the frequency count to 0
	if form not in vocab:
		vocab[form] = 0
	vocab[form] = vocab[form] + 1

for w in vocab:
	freq.append((vocab[w], w))
freq.sort(reverse=True)

# print out the frequency list
# for w in vocab:
#	print('%d\t%s' % (vocab[w], w)

print(freq[:4])
