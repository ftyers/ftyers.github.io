import sys

with open(sys.argv[1])  as f:
    dictionary = sorted([l.strip() for l in f], key=len, reverse=True)

def tokenize(sentence):
    if not len(sentence)==0:
        try:
            word = next(w for w in dictionary if sentence.startswith(w))
        except StopIteration:
            word = sentence[0]
        return word + tokenize(sentence[len(word):])

for sentence in sys.stdin:
    for word in tokenize(sentence):
        print(word)