import sys
import re

soft = ['ch', 'sh', 'tz', 's', 'x']

for line in sys.stdin.readlines():
	if re.search(str([i for i in soft])+'<PL>', line):
		line = line.replace('<PL>','es')
		print(line)
	else:
		line = line.replace('<PL>','s')
		print(line)