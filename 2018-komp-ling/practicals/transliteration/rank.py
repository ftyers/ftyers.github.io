import sys
import argparse


# принимаем на вход имя файла, чтобы загрузить из него частотный словарь
parser = argparse.ArgumentParser()
parser.add_argument("frequency_list", help="Find the rank of a word in the sorted frequency list. Takes a frequency list from a file and outputs a ranked frequency list to standard output")
args = parser.parse_args()


# функция распаковки частотного словаря для алгоритма подсчета рангов
def frequency_list_unpack(filename):
    freq = []
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            (f, w) = line.split('\t')
            freq.append((int(f), w))
    # чтобы алгоритм работал корректно, на вход нужно падать 
    # частотный словарь, отсортированный по возрастанию
    freq.sort(reverse=False)
    return freq


# функция для подсчета рангов
def count_ranks(freq):
    rank = 1
    min = freq[0][0]
    ranks = []
    for i in range(0, len(freq)):
        if freq[i][0] > min:
            rank = rank + 1
            min = freq[i][0]
        ranks.append((rank, freq[i][0], freq[i][1]))
    return print(ranks)


def main():
	freq = frequency_list_unpack(args.frequency_list)
	count_ranks(freq)

if __name__ == '__main__':
    main()
