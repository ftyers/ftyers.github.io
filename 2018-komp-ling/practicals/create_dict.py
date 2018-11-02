from io import open
from conllu import parse_incr

def main():
    print('Name of conllu file to parse:')
    train = str(input())
    print('Name of dictionary to save:')
    name = str(input())
    all_sent=[]
    data_file = open(train, "r", encoding="utf-8")
    for tokenlist in parse_incr(data_file):
        for token in tokenlist:
            all_sent.append(token['form'])
    k = list(set(all_sent))
    k.sort(key = lambda s: len(s), reverse=True)
    data_file.close()
    diction = open(name, 'w', encoding='utf-8')
    for line in k:
        diction.write(line + '\n')
    diction.close()
    print('Dictionary is seccefully created. Number of words is {}'.format(len(diction)))

main()