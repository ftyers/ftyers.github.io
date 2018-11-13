import sys

freq = []



fd = open('text.txt', 'r')

'''for line in fd.readlines():
    line = line.strip('\n')
    f, w = line.split('\t')
    freq.append((int(f), w))

# print (freq[0])

rank = 1
min = freq[0][0]
ranks = []

for i in range(len(freq)):
    if freq[i][0] < min:
        rank = rank + 1
        min = freq[i][0]
    ranks.append((rank, freq[i][0], freq[i][1]))


for i in ranks:
    print (i, '\n')'''

# Let's make one loop!

rank = 1
ranks = []
for line in fd.readlines():
    line = line.strip('\n')
    f, w = line.split('\t')

    f = int(f)
    if
    if f < min:
        rank += 1
        min = rank
    freq.append((rank, f, w))



for i in freq:
    print (i, '\n')