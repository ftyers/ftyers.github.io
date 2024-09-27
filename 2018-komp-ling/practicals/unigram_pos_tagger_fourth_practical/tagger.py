import sys

def model_tags(model):
	tags = {} # tag + freq dictionary
	words = {} # word + tag + freq dictionary
	with open(model, 'r', encoding="utf8") as f:
		model = f.readlines()
		for line in model:
			if line.startswith("#"):
				continue
			row = line.strip().split('\t')
			if row[2] not in tags:
				tags[row[2]] = float(row[0])
			else:
				if row[3] not in words:
					words[row[3]] = [(row[2], float(row[0]))]
				else:
					words[row[3]] += [(row[2], float(row[0]))]
	return tags, words

def max_tag(tags):
	# choose max tag in the model
	max_freq = max([i for i in tags.values()])
	for tag, freq in tags.items():
		if max_freq == freq:
			return tag

def max_word_tags(words):
	# choose the most freq tag for each word
	words_and_tags = {}
	for word in words:
		if len(words[word]) == 1:
			words_and_tags[word] = words[word][0][0]
		elif len(words[word]) > 1:
			tags = []
			for i in words[word]:
				tags.append(i)
			max_tag = max([j[1] for j in tags])
			for tag in tags:
				if tag[1] == max_tag:
					words_and_tags[word] = tag[0]
	return words_and_tags

def tagger(input_file, model_words, max_tag):

	with open(input_file, "r") as f:
		input = f.readlines()

		for line in input:
			if line.startswith('#') or line == '\n':
				print(line.strip())
			else:
				row = line.strip().split('\t')
				if len(row) != 10:
					continue
				if row[1].lower() in model_words:
					row[3] = model_words[row[1].lower()]
				else:
					row[3] = max_tag
				print('\t'.join(row))

def main():
	# parse the arguments - input and model
	input_file, model = sys.argv[1:]

	tags, words = model_tags(model)
	maxi_tag = max_tag(tags)
	model_words = max_word_tags(words)
	tagger(input_file, model_words, maxi_tag)

if __name__ == '__main__':
	main()