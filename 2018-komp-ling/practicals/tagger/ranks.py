import sys
import matplotlib.pyplot as plt

x = []
y = []

fd = open('ranks.txt', 'r', encoding = "utf-8")
for line in fd.readlines():
        line = line.strip()
        if line == '':
                continue
	
        row = line.split('\t')
        x.append(float(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, 'ro')
plt.show()