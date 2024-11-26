import sys
import re
answers = open(sys.argv[1]).read().split('#')

for j in sys.stdin:
    for k in answers:
        if len(k)>len(j) and j[1:]==k[:len(j)-1]:
            lines = k.split('\n')
            print(j)
            for indx, line in enumerate(lines):
                line = line.split('\t')
                if len(line)>3:
                    k = ['-']*6
                    new_string = [str(indx), line[1],'-', line[3]]
                    new_string.extend(k)
                    print('\t'.join(new_string))

