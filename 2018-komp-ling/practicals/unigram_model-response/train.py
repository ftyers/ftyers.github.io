tags = []	#all tags in the order as in text
words = []	#all words in the order as in text
tags_freq = {}	#tags as keys and number of their appearence in text(pseudo'frequency') as values
words_freq = {}	#words as keys and their frequency as values
word_tag_freq = {} #frequency of the appearence of the word with some tag
with open('ru_syntagrus.conllu', 'r', encoding='utf-8') as data:
	for line in data:
	#extracting words and tags from the data
		row = line.split('\t')
		if str(row[0]).isdigit():
			word = row[2]
			tag = row[3]
			tags.append(tag)
			words.append(word)
			#counting tag's frequency
			if tag not in tags_freq:
				tags_freq[tag] = 1
			else:
				tags_freq[tag] += 1
			#counting word's frequency
			if word not in words_freq:
				words_freq[word] = 1
			else:
				words_freq[word] += 1
			#counting word+tag's frequency
			if word in word_tag_freq:
				if tag not in word_tag_freq[word]:
					word_tag_freq[word][tag] = 1
				else:
					word_tag_freq[word][tag] += 1
			else:
				word_tag_freq[word] = {}
				word_tag_freq[word][tag] = 1
#counting the number of all accurences of all tags
all_tags = 0
for tag in tags_freq:
	all_tags += tags_freq[tag]
#counting probability of the appearence of each possible tag, round it to 4 digits after comma
tag_p = {}
for tag in tags_freq:
	tag_p[tag] = round(tags_freq[tag]/all_tags, 4)

output = zip(tags, words)	#all tags+words in the order as in text

with open('output.tsv', 'w+', encoding='utf-8') as result:
	result.write('# P'+'\t'+'count_tw'+'\t'+'tag'+'\t'+'count_w'+'\t'+'form'+'\n') #column names
	for tag in tags_freq:
		result.write(str(tag_p[tag])+'\t'+str(tags_freq[tag])+'\t'+str(tag)+'\t'+'-'+'\t'+'-'+'\n') #information about tags
	for i in output: 
		pair_freq = word_tag_freq[i[1]][i[0]]
		word_freq = words_freq[i[1]]
		word_tag_p = round(pair_freq/word_freq, 4)
		result.write(str(word_tag_p)+'\t'+str(pair_freq)+'\t'+i[0]+'\t'+str(word_freq)+'\t'+i[1]+'\n') #information about forms and their tags