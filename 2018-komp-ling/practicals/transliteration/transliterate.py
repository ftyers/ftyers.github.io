import sys

transl_dict = {}

with open('transliteration_table.txt', 'r', encoding='utf8') as infile:
    for line in infile.readlines():
        ru, en = line.split('\t')
        if ru not in transl_dict:
            transl_dict[ru] = en.strip()

with open(sys.argv[1], 'r', encoding='utf8') as inf:
    for line in inf.readlines():
        if '\t' not in line:
            continue
        line = line.strip().split('\t')
        word = line[1]
        transl_word = []
        for letter in word:
            if letter in transl_dict:
                transl_word.append(transl_dict[letter])
            else:
                transl_word.append(letter)
        line.append('Translit=' + ''.join(transl_word))
        print('\t'.join(line))