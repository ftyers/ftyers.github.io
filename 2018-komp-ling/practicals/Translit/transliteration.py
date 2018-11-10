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
	# the form is the value of the second cell
	form = row[1]
	# if we haven't seen it yet, set the frequency count to 0
	if form not in vocab:
		vocab[form] = 0
	vocab[form] = vocab[form] + 1

# print out the frequency list
for w in vocab:
	print('%d\t%s' % (vocab[w], w))

# get tokenization file for russian (test)

