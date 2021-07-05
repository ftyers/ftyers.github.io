
# coding: utf-8

import sys

freq = []

#reading the dictionary file and making tuples 'frequency - word'
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        (f,w) = line.split('\t')
        freq.append((int(f), w))

#sorting the list 'top-down'
freq.sort(reverse=True)

#ranking the words according to their frequency
rank = 1 
min = freq[0][0]
ranks = []
for i in range(0, len(freq)):
    if freq[i][0] < min:
        rank = rank + 1
        min = freq[i][0]
    #this time make lists, not tuples
    ranks.append([rank, freq[i][0], freq[i][1]])

#transform our initial list
res = open(sys.argv[2], 'w')

for val in ranks:
    val2 = '\t'.join(map(str,val))
    res.write(val2 + '\n')
    
res.close()
