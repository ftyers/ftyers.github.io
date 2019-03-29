import sys
import matplotlib.pyplot as plt

x = []
y = []

fd = open('chv.freq.txt', 'r', encoding="utf-8-sig")
count = 0
for line in fd.readlines():
        line = line.strip()
        if line == '':
                continue
	
        row = line.split(' ')
        count += 1
        x.append(count)
        y.append(int(row[0]))

plt.plot(x, y, 'ro')
plt.show()