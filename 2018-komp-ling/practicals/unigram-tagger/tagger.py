import sys

model = open(sys.argv[1]).readlines()

pos_tags = {'ADJ': 0, 'ADP': 0, 'ADV': 0, 'AUX': 0, 
         'CCONJ': 0, 'DET': 0, 'INTJ': 0,
                'NOUN': 0, 'NUM': 0, 'PART': 0, 
                'PRON': 0, 'PROPN': 0, 'PUNCT': 0,
                    'SCONJ': 0, 'SYM': 0, 'VERB':0, 'X': 0}
					
result =  {'ADJ': 0.0000001, 'ADP': 0.0000001, 'ADV': 0.0000001, 
        'AUX': 0.0000001, 'CCONJ': 0.0000001, 
        'DET': 0.0000001, 'INTJ': 0.0000001,
        'NOUN': 0.0000001, 'NUM': 0.0000001, 'PART': 0.0000001, 
        'PRON': 0.0000001, 'PROPN': 0.0000001, 'PUNCT': 0.0000001,
         'SCONJ': 0.0000001, 'SYM': 0.0000001, 
         'VERB':0.0000001, 'X': 0.0000001}
		 
words = {}

for line in model:
    line = line[:-1].split('\t')
    if len(line) == 4 and line[-1] =='-':
        result[line[2]] = line[0]
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
                res.append((pos, float(val)*float(result[pos])))
        res.sort(key=lambda x: x[1], reverse=True)
        return res[0][0]


for i in sys.stdin:
    parse = i.split('\t')
    if len(parse)>3:
        parse[3] = tag(parse[1])
        print('\t'.join(parse))
    else:
        print(parse[0])