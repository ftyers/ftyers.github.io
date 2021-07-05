import re
import sys


soft = {'ch<PL>':'ches', 'sh<PL>':'shes', 'tz<PL>':'tzes', 's<PL>':'ses', 'x<PL>':'xes'}

for line in sys.stdin.readlines():
    lines = line.strip()
    for key, value in soft.items():
        lines = lines.replace(key, value)
    lines = re.sub('<PL>', 's', lines)
    print(lines)