import sys

def main():
    k={}
    pos_tags = {'ADJ': 0, 'ADP': 0, 'ADV': 0, 'AUX': 0, 'CCONJ': 0, 'DET': 0, 'INTJ': 0,
                'NOUN': 0, 'NUM': 0, 'PART': 0, 'PRON': 0, 'PROPN': 0, 'PUNCT': 0,
                    'SCONJ': 0, 'SYM': 0, 'VERB':0, 'X': 0}
    pos_final =  {'ADJ': 0, 'ADP': 0, 'ADV': 0, 'AUX': 0, 'CCONJ': 0, 'DET': 0, 'INTJ': 0,
                'NOUN': 0, 'NUM': 0, 'PART': 0, 'PRON': 0, 'PROPN': 0, 'PUNCT': 0,
                    'SCONJ': 0, 'SYM': 0, 'VERB':0, 'X': 0}
    word_count = 0
    test_data = open(sys.argv[1]).readlines()
    for line in test_data:
        line = line.split('\t')
        if len(line) > 3:
            if line[1] not in k:
                k[line[1]] = pos_tags.copy()
            if line[1] in k:
                k[line[1]][line[3]]+=1
                pos_final[line[3]]+=1
                word_count+=1
    print('# P      Count      tag     form')
    for i in pos_final.keys():
        if pos_final[i]!=0:
            print(pos_final[i]/word_count, pos_final[i], i, '-', sep='\t')
    for word, tags in k.items():
        s = sum(list(tags.values()))
        for tag in tags.keys():
            if tags[tag]!=0:
                print(tags[tag]/s,s,tag,word, sep='\t')
if __name__ == '__main__':
    main()

