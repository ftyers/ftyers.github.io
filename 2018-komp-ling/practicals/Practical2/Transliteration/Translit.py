import sys

def clear_data(directory):
    ud_rus_sents=open(directory, 'r', encoding='utf-8').read().split('\n\n')
    parsed_data=[]
    for sent in ud_rus_sents:
        ud_rus = sent.split('\n')
        clear_sentence= []
        for line in ud_rus:
            line_s=line.split('\t')
            for word in line_s:
                if len(line_s) > 2:
                    line_s[2:] = ('-'*8)
            clear_sentence.append(line_s)
        parsed_data.append(clear_sentence)
    return parsed_data

def prepare_symb_dict(direc):
    transdict = []
    transl = open(direc, 'r', encoding = 'utf-8').read().split('\n')
    for line in transl[:-1]:
        if len(line)>2:
            let, let_tr = line.split('\t')
            transdict.append((let, let_tr))
    transdict = dict(transdict)
    return transdict

def trans_sent(k,transdict):
    sent = k
    for line in sent[2:]:
        translit=''
        for symbol in line[1]:
            if symbol in transdict:
                translit+=transdict[symbol]
            else:
                translit += symbol
        if len(translit)!=0 and translit[0]=='e' :
            translit='y'+translit
        if len(translit)!=0 and translit[0]=='E':
            translit='Y'+translit
        line[-1] = translit
    return sent

def main():
    test_data = sys.argv[1]
    dict = sys.argv[2]
    data = []
    clear_d = clear_data(test_data)
    transdict = prepare_symb_dict(dict)
    for sentence in clear_d:
        data.append(trans_sent(sentence, transdict))
    for sent in data:
        for line in sent:
            print ('\t'.join(line))

if __name__ == '__main__':
    main()