import sys
from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()

word_tag = {}
f = open(sys.argv[2]).read()
for line in f.splitlines():
    word = line.split('\t')[4]
    pos = (line.split()[0], line.split()[2])
    if word not in word_tag:
        word_tag[word] = []
        word_tag[word].append(pos)
    else:
        word_tag[word].append(pos)

#print(word_tag)

def predict(word, dict):
    p = morph.parse(word)[0]
    word = p.normal_form
    try:
        if len(dict[word]) > 1:
            for tag in dict[word]:
                if tag[0] >= dict[word][0][0]:
                    return tag[1]        
        else:
            return dict[word][0][1]     
            
    except KeyError:
        return 'UNK'  #unknown word


def tagger(file):
    f = open(file).read()
    for line in f.splitlines():
        if line.startswith('#'):
            with open('output.conllu', 'a', encoding='utf-8') as f:
                f.write(line+'\n')
                f.close()
            continue
        else:
            row = line.strip().split('\t')
            #print(row)
            row[3] = predict(row[1], word_tag)
            #print(row)
            with open('output.conllu', 'a', encoding='utf-8') as f:
                f.write('\t'.join(row)+'\n')
                f.close()
            
            
tagger(sys.argv[1])
