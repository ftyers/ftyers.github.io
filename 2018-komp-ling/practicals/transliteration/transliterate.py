import sys
import re


v = {} # to create an empty dictionary

# to create a dictionary from a table given as the first command line argument 
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        items = line.split('\t')
        key, v[key] = items[0], items[1]

# to read in a conllu file as the second command line argument
with open(sys.argv[2], 'r') as c:
    for line in c.readlines():
        if '\t' not in line:
            continue
        row = line.split('\t')
        if len(row) != 10:
            continue
        tokens = row[1]
        # to transliterate tokens in the second column
        transliterated = ''
        for letter in tokens:
            if letter in v:
                transliterated += v[letter]
            else:
                transliterated += letter
        '''
        to provide mappings on ambigous cyrillic letter 'e' - 'e'|'je':
        the transliteration table is implemented so that 'e' is transliterated to'je'.
        We need to save the results when 'je' is the beginning of a token or preceeded by a vowel,
        "'" and "''". Thus, we only need to implement 'je' -> 'e' mapping in the transliterated
        tokens when 'je' is preceeded by a consonant:
        '''
        transliterated = re.sub('([^aoeiuyAOEIU′″])je', r'\1e', transliterated)
        # to store the transliterated tokens in the 10th column
        row[9] = 'Translit=' + transliterated
        # to output the conllu file with the transliterated tokens to std output
        print('\t'.join(row[0:10]))
