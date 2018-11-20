import sys

vocab = {} # dict to store frequency list

data = open('ru_syntagrus.conllu', 'r', encoding = 'utf-8')
# for each of the lines of input
for line in data.readlines(): 
	# if there is no tab character, skip the line
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

freq = []

for w in vocab:
	freq.append((vocab[w], w))

freq.sort(reverse=True)

fd = open('freq.txt', 'w+', encoding = 'utf-8')
for w in freq:
	fd.write('%d\t%s\n' % (w[0], w[1]))
fd.close()