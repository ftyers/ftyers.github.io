import sys
import matplotlib.pyplot as plt

x = []
y = []

fd = open('freq.txt', 'r')
for line in fd.readlines():
    line = line.strip()
    if line == '':
        continue

    row = line.split('\t')
    x.append(int(row[0]))
    y.append(int(row[1]))

plt.plot(x, y, 'ro')
plt.show()