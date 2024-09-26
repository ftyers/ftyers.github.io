import sys

freq = []

fd = open(sys.argv[1], 'r', encoding='utf-8')
for line in fd.readlines():
    line = line.strip('\n')
    (f, w) = line.split('\t')
    freq.append((int(f), w))

ranks = []
for counter in range(0, len(freq)):
    ranks.append((counter + 1, freq[counter][0], freq[counter][1]))

for w in ranks:
    print('%d\t%s\t%s' % (w[0], w[1], w[2]))
