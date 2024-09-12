import nltk
import sys

segmenter = nltk.tokenize.punkt.PunktSentenceTokenizer()


for text in sys.stdin:
    for j in segmenter.tokenize(text):
        print(j)
