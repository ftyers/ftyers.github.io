tags = []
words = []
tags_freq = {}
words_freq = {}
word_tag_freq = {}
with open('ru_syntagrus.conllu', 'r', encoding='utf-8') as data:
	for line in data:
		row = line.split('\t')
		if str(row[0]).isdigit():
			word = row[2]
			tag = row[3]
			tags.append(tag)
			words.append(word)
			if(tag not in tags_freq):
				tags_freq[tag] = 1
			else:
				tags_freq[tag] += 1

			if word not in words_freq:
				words_freq[word] = 1
			else:
				words_freq[word] += 1

			if word in word_tag_freq:
				if tag not in word_tag_freq[word]:
					word_tag_freq[word][tag] = 1
				else:
					word_tag_freq[word][tag] += 1
			else:
				word_tag_freq[word] = {}
				word_tag_freq[word][tag] = 1
all_tags = 0
for tag in tags_freq:
	all_tags += tags_freq[tag]
tag_p = {}
for tag in tags_freq:
	tag_p[tag] = round(tags_freq[tag]/all_tags, 4)

output = zip(tags, words)

with open('output.tsv', 'w+', encoding='utf-8') as result:
	result.write('# P'+'\t'+'count_tw'+'\t'+'tag'+'\t'+'count_w'+'\t'+'form'+'\n')
	for tag in tags_freq:
		result.write(str(tag_p[tag])+'\t'+str(tags_freq[tag])+'\t'+str(tag)+'\t'+'-'+'\t'+'-'+'\n')
	for i in output:
		pair_freq = word_tag_freq[i[1]][i[0]]
		word_freq = words_freq[i[1]]
		word_tag_p = round(pair_freq/word_freq, 4)
		result.write(str(word_tag_p)+'\t'+str(pair_freq)+'\t'+i[0]+'\t'+str(word_freq)+'\t'+i[1]+'\n')