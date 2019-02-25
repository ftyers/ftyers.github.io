import sys

vocab = {}
f = open(sys.argv[1], 'r')
for line in f.readlines():
    if '\t' not in line:
        continue
    row = line.split('\t')
    if len(row) != 10:
        continue
    form = row[1]
    if form not in vocab:
        vocab[form] = 0
    vocab[form] = vocab[form] + 1

freq = []
for w in vocab:
    freq.append('%d\t%s' % (vocab[w], w))

freq.sort(reverse=True)
print(*freq, sep='\n')


