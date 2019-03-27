import sys
import csv
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

train = {}
for line in open(sys.argv[2]).readlines():
    word = line.split()[3]
    inf = []
    pos = (line.split()[0], line.split()[2])
    if word not in train:
        train[word] = inf
    else:
        train[word].append(pos)

def tagger(word, dicti):
    p = morph.parse(word)[0]
    word = p.normal_form
    try:
        if dicti[word]:
            if len(dicti[word]) > 1:
                cur = dicti[word][0]
                for i in dicti[word]:
                    if i[0] > cur[0]:
                        cur = (i[0], i[1])
                return cur[1]        
            else:
                return dicti[word][0][1]     
            
    except KeyError:
        return 'OOV'


def proc(file):
    for line in open(file).readlines():
        if line.startswith('#'):
            with open('tagged', 'a') as f:
                f.write(line)
            continue
        line = line.split()
        line[2] = tagger(line[1], train)
        with open('tagged', 'a') as f:
            writer = csv.writer(f, delimiter='\t',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(line)
            
            
proc(sys.argv[1])
            
            
            
            
        