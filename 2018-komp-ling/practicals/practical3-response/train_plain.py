import sys


# to create empty lists for our tokens, tags and word-tag pairs
tokens, tags, pairs = [], [], []


# to read in a file as the first command line argument given and get the values
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if '\t' not in line:
            continue
        row = line.split('\t')
        tokens.append(row[1])
        tags.append(row[3])
        pairs.append(row[3] + '\t' + row[1])


# to set up a matrix for our tags
tag_matrix = {}
for tag in tags:
    if tag not in tag_matrix:
        tag_matrix[tag] = {}
    for freq in [tags.count(tag)]:
        if freq not in tag_matrix[tag]:
            tag_matrix[tag][freq] = tags.count(tag)


# to set up a matrix for our pairs
pair_matrix = {}
for pair in pairs:
    if pair not in pair_matrix:
        pair_matrix[pair] = {}
    for freq in [pairs.count(pair)]:
        if freq not in pair_matrix[pair]:
            pair_matrix[pair][freq] = pairs.count(pair)


# to print the column names
print('\t'.join(['# P', 'count', 'tag', 'form']))


# to print our tag matrix
for tag in tag_matrix:
    for freq in tag_matrix[tag]:
        print(round(tag_matrix[tag][freq] / len(tokens), 2), \
              '\t%d\t%s\t%s' % (tag_matrix[tag][freq], tag, '_'))


# to print our pair matrix
for pair in pair_matrix:
    for freq in pair_matrix[pair]:
        print(round(pair_matrix[pair][freq] / tokens.count(pair.split('\t')[1]), 2),\
              '\t%d\t%s' % (pair_matrix[pair][freq], (pair)))
