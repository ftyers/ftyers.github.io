import sys
from matplotlib import pyplot as plt

x = []
y = []

fd = open('ranks.txt', 'r', encoding='utf-8')
for line_number, line in enumerate(fd):
    line = line.strip()
    if line == '':
        continue
	
    row = line_number, line.split('\t')
    #print(row)
    x.append(int(row[0]))
    y.append(int(row[1][0]))

plt.plot(x, y, 'ro')
plt.show()