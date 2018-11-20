import sys

vocab = {} # mapping Russian to English letters

fd = open('transliteration_table', 'r')
file = open("syntagrus-ud-test.conllu", 'r')

for line in fd.readlines():
    line = line.strip('\n')
    key, val = line.split('\t')
    vocab[key] = val

# e changes to je under a condition of being after a vowel, 'ь', 'ъ' or at the beginning of the sentence
condition = 'уеъаоэьяиюы'

# for line in sys.stdin.readlines():
for line in file.readlines():
    if '\t' not in line:
        continue
    row = line.split('\t')
    if len(row) != 10:
        continue
    changeto = ''
    for char in row[1]:
        # checking if the letter is a Cyrillic letter:
        if char.lower() in vocab:
            # checking if it's a 'e' after at a particular position:
            if char == 'е' or char == 'Е':
                if row[1].index(char)==0 or row[1][row[1].index(char)-1].lower() in condition:
                    if char.istitle():
                        changeto += 'J' + vocab[char.lower()]
                    else:
                        changeto += 'j' + vocab[char.lower()]
                else:
                    changeto += vocab[char.lower()]
            else:
                if char.istitle():
                    changeto += vocab[char.lower()].upper()
                else:
                    changeto += vocab[char]
        else:
            changeto += char

    print ('{}\t{}'.format(row[1], changeto))
    changeto = ''
fd.close()
