import sys

exeprions = {'man':'men', 'person':'people', 'woman':'women', 'mouse':'mice',
             'foot':'feet', 'child': 'children', 'tooth':'teeth', 'goose':'geese', 'ox':'oxen'}
f_exeptions = ['roof', 'belief', 'chef', 'chief']
no_changes_exeptions = ['sheep', 'series', 'species', 'deer', 'fish', 'moose', 'salmon',\
                        'aircraft', 'trout', 'means']

word = sys.argv[1]

if word in exeprions:
    print(exeprions[word])
elif word.endswith('is'):
    print(word[:-2] + 'es')
elif word.endswith('us'):
    print(word[:-2] + 'i')
elif word.endswith('s' or 'ss' or 'sh' or 'ch' or 'tch' or 'z' or 'x'):
    print(word + 'es')
elif word not in f_exeptions and word.endswith('f' or 'fe'):
    print(word[:-1] + 'ves')
elif word in no_changes_exeptions:
    print(word)
elif word.endswith('ay' or 'ey' or 'oy'):
    print(word + 's')
elif word.endswith('y'):
    print(word[:-1] + 'ies')
elif word.endswith('a'):
    print(word[:-1] + 'ae')
elif word.endswith('um'):
    print(word[:-2] + 'a')
else:
    print(word, 's')
