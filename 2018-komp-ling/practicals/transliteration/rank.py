import sys

freq = []

fd = open(sys.argv[1], 'r', encoding='utf8')
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


f = open('rank_freq.txt', 'w+')
for r in ranks:
	print('%d\t%d\t%s' % (r[0], r[1], r[2]),  file = f, sep = '\n')

f.close()
