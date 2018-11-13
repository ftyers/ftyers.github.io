import sys
import re


#1. get dictionary
dictionary = {}
with open('alpha-komi-zyrian.tsv', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
for line in lines:
    row = line.split('\t')
    row = [letter.strip() for letter in row]
    for i in range(len(lines)):
        dictionary[row[0]] = row[1]
        dictionary[row[0].capitalize()] = row[1].capitalize() #save capitalization

#2. read the conllu file
for line in sys.stdin.readlines():
    if '\t' not in line:
        continue
    row = line.split('\t')
    if len(row) != 10:
        continue
    word = row[1]
    translit = ''
    for letter in word: #transliterate words one by one
        if letter in dictionary:
            translit += dictionary[letter]
        else:
            translit += letter

#3. change the transliteration to provide correct mappings / mappings from many characters to one character
    if re.search('(.*)?dz.*', translit):
        translit = re.sub("(.*?)dz(.*?)", r"\1dž'\2", translit)
    if re.search('Dz.*', translit):
        translit = re.sub("Dz(.*?)", r"Dž'\1", translit)
    if re.search('.*tš.*', translit):
        translit = re.sub("(.*?)tš(.*?)", r"\1č\2", translit)

#4. add transliteration into the mics column 9
    row[8] = 'Translit=' + translit
    output = row[0:10]

#5. print the result to standart output
    print('\t'.join(output))
