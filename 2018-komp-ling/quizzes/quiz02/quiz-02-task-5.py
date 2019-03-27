import sys
import re

print('Insert word with <PL> tag')
for line in sys.stdin:
        if re.search('[s|c]h<PL>$', line) or re.search('tz<PL>$', line) or re.search('[x|s]<PL>$', line):
            plural_str = line[:line.index('<PL>')] + 'e' + 's'
            print(plural_str)
        else:
            plural_str = line[:line.index('<PL>')] + 's'
            print(plural_str)
