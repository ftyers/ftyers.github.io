import sys

vocab = {} # dict to store Russian to English letters

f = open('trans_dict.txt', 'r')
for i in f.readlines():
    i = i.strip('\n')
    r, e = i.split('\t')
    vocab[r] = e

# This string will help us check whether we need to change Russian 'е' to 'e' or 'ye'
# Because 'e' changes to 'ye' after a vowel, 'ь', 'ъ' or at the beginning of the sentence
vowels = 'уУеЕъЪаАоОэЭьЬяЯиИюЮыЫ'

for line in sys.stdin.readlines():
    if '\t' not in line:
        continue
    row = line.split('\t')
    if len(row) != 10:
        continue
    subst = ''
    # this is to check if it's the beginning of a word:
    p = ''
    for i in row[1]:
        # checking if the letter is a Cyrillic letter:
        if i in vocab:
            # checking if it's a 'e' after at a particular position:
            if i == 'е' and (p in vowels or p == ''):
                subst+= 'y' + vocab[i]
            elif i == 'Е' and (p in vowels or p == ''):
                subst+= 'Y' + vocab[i]
            else:
                subst += vocab[i]
                p = i
        else:
            subst += i

    print ('{}\t{}'.format(row[1], subst))
    subst = ''
    p = ''
f.close()
