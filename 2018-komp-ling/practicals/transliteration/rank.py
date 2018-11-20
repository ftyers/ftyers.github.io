import sys

freq = []

fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	(f, w) = line.split('\t')
	freq.append((int(f), w))

rank = 1
min = freq[0][0]
ranks = []
for i in range(0, len(freq)): 
	if freq[i][0] < min: 
		rank = rank + 1
		min = freq[i][0]
	ranks.append((rank, freq[i][0], freq[i][1]))

for w in ranks:
	print('%d\t%d\t%s' % (w[0],w[1],w[2]))