import sys


# to create empty lists for our tokens, tags and word-tag pairs
tokens, tags, pairs = [], [], []


# to set up a matrix
def get_matrix(list):
    matrix = {}
    for element in list:
        if element not in matrix:
            matrix[element] = {}
        for freq in [list.count(element)]:
            if freq not in matrix[element]:
                matrix[element][freq] = list.count(element)
    return matrix


# to set up a matrix for our tags
def tag_matrix():
    for tag in get_matrix(tags):
        for freq in get_matrix(tags)[tag]:
            print(round(get_matrix(tags)[tag][freq] / len(tokens), 2),\
                  '\t%d\t%s\t%s' % (get_matrix(tags)[tag][freq], tag, '_'))


# to set up a matrix for our pairs
def pair_matrix():
    for pair in get_matrix(pairs):
        for freq in get_matrix(pairs)[pair]:
            print(round(get_matrix(pairs)[pair][freq] / tokens.count(pair.split('\t')[1]), 2), \
                  '\t%d\t%s' % (get_matrix(pairs)[pair][freq], (pair)))


def main():
    # read in a file as the first command line argument and get the values
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            if '\t' not in line:
                continue
            row = line.split('\t')
            tokens.append(row[1])
            tags.append(row[3])
            pairs.append(row[3] + '\t' + row[1])
    # get matrices for tags, pairs
    get_matrix(tags)
    get_matrix(pairs)
    # print all the results
    print('\t'.join(['# P', 'count', 'tag', 'form']))
    tag_matrix()
    pair_matrix()


if __name__ == '__main__':
    main()
