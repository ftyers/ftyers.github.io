#create a dictionary for transliteration using our table
dictionary = {}
with open('table.txt', 'r', encoding = 'utf-8') as table:
	for line in table:
		row = line.split('\t')
		dictionary[row[0]] = row[1].replace('\n','')

#function that trasliterate one word
def transliterate(trans_word):
	word = ''
	for letter in trans_word:
		if letter in dictionary:
			word += dictionary[letter]
		else:
			word += letter
	return 'Transliteration = ' + word

#create a list with words form conllu file with their transliteration
tokens = []

with open('ru_syntagrus.conllu', 'r', encoding = 'utf-8') as data:
	for line in data:
		row = line.split('\t')
		if(str(row[0]).isdigit()):
			trans = transliterate(row[1])
			tokens.append([row[1],trans])

#write to the file
result = open('results.conllu', 'w+', encoding = 'utf-8')
for row in tokens:
	row = '\t'.join(row)
	result.write(row + '\n')
result.close()