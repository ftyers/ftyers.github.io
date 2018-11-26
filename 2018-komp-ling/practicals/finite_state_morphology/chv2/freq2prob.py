import sys, math as maths
f = {}; fs = []
total = 0
for line in sys.stdin.readlines():
	row = line.strip().split(' ')
	if len(row) < 2: continue
	form = row[1]
	freq = int(row[0])
	fs.append(form)
	f[form] = freq
	total += freq
for form in fs: 
	print('%s\t%.4f' % (form, -maths.log(f[form]/total)))
