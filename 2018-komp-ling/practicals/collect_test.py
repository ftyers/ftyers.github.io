from io import open
from conllu import parse_incr

def main():
    print('Extract sentences from the file:')
    test_file = str(input())
    print('Write sentences to file:')
    res_file= str(input())
    data_test = open(test_file, "r", encoding="utf-8")
    all_sent = []

    for tokenlist in parse_incr(data_test):
        all_sent.append(tuple(dict(tokenlist.metadata).values())[1])

    f = open(res_file, 'w', encoding='utf-8')
    for line in all_sent:
        f.write(line + '\n')
    f.close()
    print('{} sentences were extracted and writen to {}'.format(len(all_sent), res_file))

if __name__ == '__main__':
    main()