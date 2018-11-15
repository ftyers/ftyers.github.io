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

min = 0
ranks = []
text = fd.readlines()
for i in range(len(text)):
    line = text[i].strip('\n')
    f, w = line.split('\t')
    f = int(f)
    if i == 0:
        min = f
        rank = 1
    if f < min:
        rank += 1
        min = f
    freq.append((rank, f, w))



for i in freq:
    print (i, '\n')