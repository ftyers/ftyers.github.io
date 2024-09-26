import sys

transl = {}

with open('transl_dict.txt', 'r', encoding='utf-8') as d:
    for line in d.readlines():
        rus, eng = line.split('\t')
        if rus not in transl:
            transl[rus] = eng.strip()

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if '\t' not in line:
            continue
        line = line.strip().split('\t')
        word = line[1]
        transl_word = []
        for letter in word:
            if letter in transl:
                transl_word.append(transl[letter])
            else:
                transl_word.append(letter)
        line.append('Translit=' + ''.join(transl_word))
        print('\t'.join(line))
