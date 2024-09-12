import nltk
import sys

segmenter = nltk.tokenize.punkt.PunktSentenceTokenizer()
segms = []

for text in sys.stdin:
	segms += [i for i in segmenter.tokenize(text)]
	
print(segms)
