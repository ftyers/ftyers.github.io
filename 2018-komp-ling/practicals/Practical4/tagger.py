import sys

model = open(sys.argv[1]).readlines()
pos_final =  {'ADJ': 0.0000001, 'ADP': 0.00000010, 'ADV': 0.00000010, 
        'AUX': 0.00000010, 'CCONJ': 0.00000010, 
        'DET': 0.00000010, 'INTJ': 0.00000010,
        'NOUN': 0.00000010, 'NUM': 0.00000010, 'PART': 0.00000010, 
        'PRON': 0.00000010, 'PROPN': 0.00000010, 'PUNCT': 0.00000010,
         'SCONJ': 0.00000010, 'SYM': 0.00000010, 
         'VERB':0.00000010, 'X': 0.00000010}
pos_tags = {'ADJ': 0, 'ADP': 0, 'ADV': 0, 'AUX': 0, 
         'CCONJ': 0, 'DET': 0, 'INTJ': 0,
                'NOUN': 0, 'NUM': 0, 'PART': 0, 
                'PRON': 0, 'PROPN': 0, 'PUNCT': 0,
                    'SCONJ': 0, 'SYM': 0, 'VERB':0, 'X': 0}

words = {}
for line in model:
    line = line[:-1].split('\t')
    if len(line) == 4 and line[-1] =='-':
        pos_final[line[2]] = line[0]
        print(pos_final)
    if len(line) == 4 and line[-1] !='-':
        words.update({line[3]:pos_tags.copy()})
        words[line[3]][line[2]]=line[0]
   

def tag(word):
    res = []
    if word not in words:
        return 'X'
    else:
        for pos, val in words[word].items():
            if val!=0:
                res.append((pos, float(val)*float(pos_final[pos])))
        res.sort(key=lambda x: x[1], reverse=True)
        return res[0][0]

            

for i in sys.stdin:
    parse = i.split('\t')
    if len(parse)>3:
        parse[3] = tag(parse[1])
        print('\t'.join(parse))
    else:
        print(parse[0])
