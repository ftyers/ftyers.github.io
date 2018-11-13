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


# Downloaded two parsed sentences files from https://github.com/UniversalDependencies:
# - ru_pud-ud-test.conllu (1,5 Mb)
# - ru_syntagrus-ud-dev.conllu (10 Mb)

# cat ru_pud-ud-test.conllu | python3 transliteration.py
# python3 transliteration.py < ru_pud-ud-test.conllu > text.txt
# to get a list sorted by frequency:
# python3 transliteration.py < ru_pud-ud-test.conllu | sort -nr  > text.txt
# or it's also possible to use the for loop you advised, but I had
# difficulty using your code as I kept warning  'list indices must be integers or slices, not tuple'
# so I wrote the same with the format function


freq = []

for w in vocab:
	freq.append((vocab[w], w))

# freq.sort(reverse=True)

for i in freq:
	print ('{}\t{}'.format(i[0], i[1]))

# now I have a unique word list arranged by frequency
