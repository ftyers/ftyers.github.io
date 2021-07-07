#!/usr/bin/python
import re
import decimal
import collections
import sys
from pathlib import Path    # requires Python 3.4


def write2file(file, count, all, tag, form):
    precise = decimal.Decimal(count) / decimal.Decimal(all)
    p = decimal.Decimal(precise).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP)
    file.write(f'{p}\t{count}\t{tag}\t{form}\n')
    return


if len(sys.argv) > 2:
    if Path(sys.argv[1]).is_file():
        with open(sys.argv[1], 'r', encoding="UTF-8") as src, \
                open(sys.argv[2], 'w', encoding='utf-8') as dest:
            word2pos = {}
            posdict = collections.Counter()

            for x in src.readlines():
                match = re.search('\d+\t.*?\t(.*?)\t([A-Z]+).*', x)
                if match:
                    word = match.group(1)
                    pos = match.group(2)
                    if word:
                        posdict[pos] += 1
                        if word in word2pos:
                            this = word2pos[word]
                            if pos in this:
                                this[pos] += 1
                            else:
                                this[pos] = 1
                        else:
                            word2pos[word] = {pos:1}

            dest.write(f'# P\tcount\ttag\tform\n')

            posttl = sum(posdict.values())
            for x in posdict.most_common():
                write2file (dest, x[1], posttl, x[0], "–")

            for x in word2pos:
                thisttl = 0
                for y in word2pos[x]:
                    thisttl += word2pos[x][y]
                for y in word2pos[x]:
                    write2file(dest, word2pos[x][y], thisttl, y, x)

            print("Successfully completed! Tokens/words quantity: " + str(posttl) + "/"+ str(len(word2pos)))
    else:
        print("Source file does not exist!")
else:
    print("Not enough command line arguments!")