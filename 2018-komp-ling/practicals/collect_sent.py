from io import open
from conllu import parse_incr

def main():
    print('Extract sentences from the file:')
    test_file = str(input())

    print('Write sentences to file:')
    res_file= str(input())

    print('Write gold sentences to file:')
    gold_file= str(input())

    data = open(test_file, "r", encoding="utf-8")
    all_sent = []
    gold_sent = []

    for tokenlist in parse_incr(data):
        all_sent.append(tuple(dict(tokenlist.metadata).values())[1])
        sent=[]
        for token in tokenlist:
            sent.append(token['form'])
        gold_sent.append(' '.join(sent))
    
    res = open(res_file, 'w', encoding='utf-8')
    for line in all_sent:
        res.write(line + '\n')
    res.close()
    print('{} sentences were extracted and writen to {}'.format(len(all_sent), res_file))

    gd = open(gold_file, 'w', encoding='utf-8')
    for line in gold_sent:
        gd.write(line + '\n')
    gd.close()
    print('{} sentences were extracted and writen to {}'.format(len(gold_sent), gold_file))

if __name__ == '__main__':
    main()