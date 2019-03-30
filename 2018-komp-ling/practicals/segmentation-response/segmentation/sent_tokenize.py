import sys
from nltk.tokenize import sent_tokenize
for paragraph in sys.stdin:
    for sentence in sent_tokenize(paragraph.decode('utf-8'), language='russian'):
        print(sentence.encode('utf-8'))
