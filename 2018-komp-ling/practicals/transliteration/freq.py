import sys

vocab = {} # dict to store frequency list

# for each of the lines of input
for line in sys.stdin.readlines(): 
	# if there is no tab character, skip the line
	if '\t' not in line:
		continue
	# make a list of the cells in the row
	row = line.split('\t')
	# if there are not 10 cells, skip the line
	if len(row) != 10:
		continue
	# if the token is punctuation sign, skip the line
	if row[3] == 'PUNCT':
		continue
	# the form is the value of the second cell
	form = row[1].lower()
	# if we haven't seen it yet, set the frequency count to 0
	if form not in vocab:
		vocab[form] = 0
	vocab[form] = vocab[form] + 1

# sort by frequency
freq = []
for w in vocab:
	freq.append((vocab[w], w))
freq.sort(reverse=True)

# writing to file
fs = open('freq_sort.txt', 'w+')
for w in freq:
	print('%d\t%s' % (w[0], w[1]), file = fs, sep = '\n')

fs.close()