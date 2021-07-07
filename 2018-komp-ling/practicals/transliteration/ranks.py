import sys

fd = open('reversecount', 'r')
freq = []
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
for e in ranks:
	print(e)
