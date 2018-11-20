import sys


freq = []
ranks = []


def frequency():
    with open(sys.argv[1], 'r') as file:
        for line in file.readlines():
            line = line.strip('\n')
            (f, w) = line.split('\t')
            freq.append((int(f), w))
    return freq


def ranking(freq):
    rank = 1
    min = freq[0][0]
    for i in range(0, len(freq)): 
        if freq[i][0] < min: 
            rank = rank + 1
            min = freq[i][0]
        ranks.append((rank, freq[i][0], freq[i][1]))
    return ranks


def output():
    for w in ranks:
        print('%d\t%d\t%s' % (w[0], w[1], w[2]))


def main():
    frequency()
    ranking(freq)
    output()


if __name__ == '__main__':
    main()
       

