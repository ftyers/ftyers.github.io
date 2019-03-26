import sys
from nltk.tokenize import sent_tokenize

for text in sys.stdin:
    for j in sent_tokenize(text):
        print(j)
    

