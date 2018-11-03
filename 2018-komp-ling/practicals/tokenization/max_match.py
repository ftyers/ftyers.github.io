import sys

with open(sys.argv[1], encoding='utf8') as f:
	dictionary = sorted([l.strip() for l in f], key=len, reverse=True)
	# последний символ словаря оказывался пустым, поэтому у меня была проблема
	dictionary = dictionary[:-1]

def tokenize(sentence):
	if len(sentence) == 0:
		return []
	for word in dictionary:
		if sentence.startswith(word):
			return [word] + tokenize(sentence[len(word):])

	return [sentence[0]] + tokenize(sentence[1:])

for sentence in sys.stdin:
	for word in tokenize(sentence):
		print(word)