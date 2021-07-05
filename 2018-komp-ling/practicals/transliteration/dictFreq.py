import sys


vocab = {}
freq = []


def get_frequency():
    for line in sys.stdin.readlines():
        if '\t' not in line:
            continue
        row = line.split('\t')
        if len(row) != 10:
            continue
        form = row[1]
        if form not in vocab:
            vocab[form] = 0
        vocab[form] = vocab[form] + 1
    for w in vocab:
        freq.append((vocab[w], w))
    return freq.sort(reverse=True)


def results():
    with open('freq.txt', 'w+', encoding='utf-8') as f:
        for w in freq:
            f.write('%d\t%s\n' % (w[0], w[1]))
        f.close()


def main():
    get_frequency()
    results()


if __name__ == '__main__':
    main()
